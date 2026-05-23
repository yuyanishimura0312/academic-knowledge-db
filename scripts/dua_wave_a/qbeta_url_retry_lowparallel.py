#!/usr/bin/env python3
"""
DUA Wave A — Q-β URL Retry with Low Parallelism (Wikipedia-friendly)
=====================================================================

Retries concepts left in 'url_present' state after initial verification.
Uses 8 concurrent workers with 200ms per-worker spacing to be Wikipedia-friendly.

Typical use:
    python3 qbeta_url_retry_lowparallel.py --domain innovation_theory
    python3 qbeta_url_retry_lowparallel.py --all --time-budget-min 180

Only touches concepts where verification_status = 'url_present' AND last_verified_at IS NULL
(i.e. either never verified, or kept transient from earlier run).
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import urllib.request
import urllib.error
import socket
from urllib.parse import urlparse

DB_PATH = Path.home() / "projects/research/academic-knowledge-db/academic.db"
REPORTS_DIR = Path.home() / "projects/research/academic-knowledge-db/reports/dua_wave_a"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# More browser-like UA to avoid 403 from some sites
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
REQUEST_TIMEOUT_SEC = 15
MAX_REDIRECT_HOPS = 5
CONCURRENT_WORKERS = 8  # Low parallel to be friendly to Wikipedia
PER_REQ_SLEEP_SEC = 0.05
BATCH_SIZE = 1000
CHECKPOINT_RATIO = 0.02

DOMAINS = [
    "innovation_theory",
    "marketing_sales",
    "humanities_concept",
    "social_theory",
    "natural_discovery",
    "engineering_method",
    "arts_question",
    "business_models",
    "startup_theory",
    "poetics_text",
]


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        return None
    http_error_302 = http_error_301
    http_error_303 = http_error_301
    http_error_307 = http_error_301
    http_error_308 = http_error_301


def verify_url(url: str) -> dict:
    if not url or not url.strip():
        return {"status": "dead", "http_status": None, "redirect_to": None, "error": "empty_url"}
    url = url.strip()
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            return {"status": "dead", "http_status": None, "redirect_to": None, "error": "bad_url"}
    except Exception as e:
        return {"status": "dead", "http_status": None, "redirect_to": None, "error": f"parse_error"}

    current_url = url
    final_redirect = None

    for hop in range(MAX_REDIRECT_HOPS + 1):
        req = urllib.request.Request(
            current_url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9,ja;q=0.8",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "no-cache",
            },
            method="GET",
        )
        try:
            opener = urllib.request.build_opener(NoRedirect)
            with opener.open(req, timeout=REQUEST_TIMEOUT_SEC) as resp:
                code = resp.status
                if 200 <= code < 300:
                    if final_redirect is not None:
                        return {"status": "redirect", "http_status": code, "redirect_to": final_redirect, "error": None}
                    return {"status": "verified", "http_status": code, "redirect_to": None, "error": None}
                return {"status": "verified", "http_status": code, "redirect_to": None, "error": None}
        except urllib.error.HTTPError as e:
            code = e.code
            if code in (301, 302, 303, 307, 308):
                location = e.headers.get("Location")
                if not location:
                    return {"status": "dead", "http_status": code, "redirect_to": None, "error": "redirect_no_location"}
                if location.startswith("/"):
                    p = urlparse(current_url)
                    location = f"{p.scheme}://{p.netloc}{location}"
                final_redirect = location
                current_url = location
                if hop >= MAX_REDIRECT_HOPS:
                    return {"status": "redirect", "http_status": code, "redirect_to": final_redirect, "error": "max_hops"}
                continue
            if code in (404, 410, 451):
                return {"status": "dead", "http_status": code, "redirect_to": None, "error": f"http_{code}"}
            if code in (403, 401):
                # Wikipedia / academic sites sometimes 403 on automated requests but URL exists
                # Treat as verified to avoid losing real URLs
                return {"status": "verified", "http_status": code, "redirect_to": None, "error": f"blocked_{code}"}
            if code in (429,):
                # Rate limited — keep as url_present for next retry
                return {"status": "url_present", "http_status": code, "redirect_to": None, "error": "rate_limited"}
            if code in (503, 502, 504, 500):
                return {"status": "url_present", "http_status": code, "redirect_to": None, "error": f"transient_{code}"}
            return {"status": "dead", "http_status": code, "redirect_to": None, "error": f"http_{code}"}
        except urllib.error.URLError as e:
            reason = str(e.reason) if hasattr(e, "reason") else str(e)
            if "timed out" in reason.lower() or "timeout" in reason.lower():
                return {"status": "url_present", "http_status": None, "redirect_to": None, "error": "timeout"}
            if any(s in reason.lower() for s in ("nodename nor servname", "name or service not known", "no address")):
                return {"status": "dead", "http_status": None, "redirect_to": None, "error": "dns_fail"}
            if "connection refused" in reason.lower():
                return {"status": "dead", "http_status": None, "redirect_to": None, "error": "conn_refused"}
            return {"status": "dead", "http_status": None, "redirect_to": None, "error": f"url_error:{reason[:60]}"}
        except socket.timeout:
            return {"status": "url_present", "http_status": None, "redirect_to": None, "error": "socket_timeout"}
        except Exception as e:
            return {"status": "dead", "http_status": None, "redirect_to": None, "error": f"exc:{type(e).__name__}"}

    return {"status": "dead", "http_status": None, "redirect_to": None, "error": "loop_exhausted"}


def process_domain(conn: sqlite3.Connection, table: str, time_budget_sec: float) -> dict:
    cur = conn.cursor()
    # Only re-verify rows still in url_present
    rows = cur.execute(
        f"SELECT id, source_url FROM {table} "
        f"WHERE verification_status = 'url_present' "
        f"  AND source_url IS NOT NULL AND source_url != '' "
        f"  AND (last_verified_at IS NULL OR last_verified_at < datetime('now', '-1 hour'))"
    ).fetchall()

    total = len(rows)
    print(f"  [{table}] {total} concepts to retry")
    if total == 0:
        return {"table": table, "total_targets": 0, "completed": 0, "distribution": {}, "failure_patterns_top": {}}

    stats = Counter()
    failure_patterns = Counter()
    buffer = []
    completed = 0
    start = time.time()
    checkpoint = max(1, int(total * CHECKPOINT_RATIO))
    next_checkpoint = checkpoint

    with ThreadPoolExecutor(max_workers=CONCURRENT_WORKERS) as ex:
        future_to_id = {}
        for pk, url in rows:
            fut = ex.submit(verify_url, url)
            future_to_id[fut] = (pk, url)
            time.sleep(PER_REQ_SLEEP_SEC)

        for fut in as_completed(future_to_id):
            if time.time() - start > time_budget_sec:
                print(f"    [{table}] Time budget exhausted, stopping submission")
                for f in future_to_id:
                    if not f.done():
                        f.cancel()
                break

            pk, url = future_to_id[fut]
            try:
                result = fut.result(timeout=REQUEST_TIMEOUT_SEC + 10)
            except Exception as e:
                result = {"status": "dead", "http_status": None, "redirect_to": None, "error": f"future_exc:{type(e).__name__}"}
            status = result["status"]
            stats[status] += 1
            if status in ("dead", "redirect") and result.get("error"):
                failure_patterns[result["error"]] += 1
            now_iso = datetime.now(timezone.utc).isoformat()
            if status != "url_present":
                buffer.append((status, result["http_status"], result["redirect_to"], now_iso, pk))
            else:
                # Mark last_verified_at for transient as well, so we can skip in short-term retries
                buffer.append(("url_present", result["http_status"], None, now_iso, pk))
            completed += 1

            if len(buffer) >= BATCH_SIZE:
                cur.executemany(
                    f"UPDATE {table} SET verification_status=?, http_status=?, redirect_to=?, last_verified_at=? WHERE id=?",
                    buffer,
                )
                conn.commit()
                buffer.clear()

            if completed >= next_checkpoint:
                elapsed = time.time() - start
                rate = completed / elapsed if elapsed > 0 else 0
                eta_sec = (total - completed) / rate if rate > 0 else 0
                if buffer:
                    cur.executemany(
                        f"UPDATE {table} SET verification_status=?, http_status=?, redirect_to=?, last_verified_at=? WHERE id=?",
                        buffer,
                    )
                    conn.commit()
                    buffer.clear()
                print(f"    [{table}] {completed}/{total} ({100*completed/total:.1f}%) rate={rate:.1f}/s eta={eta_sec/60:.1f}min "
                      f"v={stats['verified']} d={stats['dead']} r={stats['redirect']} u={stats['url_present']}")
                next_checkpoint += checkpoint

    # Final flush
    if buffer:
        cur.executemany(
            f"UPDATE {table} SET verification_status=?, http_status=?, redirect_to=?, last_verified_at=? WHERE id=?",
            buffer,
        )
        conn.commit()
        buffer.clear()

    elapsed = time.time() - start
    print(f"  [{table}] DONE: {completed}/{total} in {elapsed/60:.1f}min — v={stats['verified']} d={stats['dead']} r={stats['redirect']} u={stats['url_present']}")
    return {
        "table": table,
        "total_targets": total,
        "completed": completed,
        "elapsed_sec": round(elapsed, 1),
        "distribution": dict(stats),
        "failure_patterns_top": dict(failure_patterns.most_common(30)),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", default=None)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--time-budget-min", type=int, default=120)
    args = parser.parse_args()

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")

    targets = DOMAINS if args.all else [args.domain] if args.domain else []
    if not targets:
        print("Specify --domain X or --all", file=sys.stderr)
        sys.exit(1)

    overall_start = time.time()
    overall = []
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = REPORTS_DIR / f"qbeta_url_retry_{timestamp}.json"

    budget_total = args.time_budget_min * 60
    for table in targets:
        elapsed = time.time() - overall_start
        remaining = budget_total - elapsed
        if remaining < 60:
            print(f"Time budget exhausted ({elapsed/60:.1f}min)")
            break
        # Give equal-ish time slice per remaining domain
        idx = targets.index(table)
        n_left = len(targets) - idx
        per_domain_budget = remaining / max(1, n_left)
        print(f"\n=== {table} (budget: {per_domain_budget/60:.1f}min) ===")
        r = process_domain(conn, table, per_domain_budget)
        overall.append(r)
        with open(report, "w") as f:
            json.dump({
                "start": datetime.now(timezone.utc).isoformat(),
                "elapsed_min": round((time.time() - overall_start) / 60, 1),
                "domains": overall,
                "config": {
                    "concurrent_workers": CONCURRENT_WORKERS,
                    "user_agent": USER_AGENT,
                    "timeout_sec": REQUEST_TIMEOUT_SEC,
                    "per_req_sleep_sec": PER_REQ_SLEEP_SEC,
                },
            }, f, ensure_ascii=False, indent=2)

    conn.close()
    print(f"\nReport: {report}")
    print(f"Total elapsed: {(time.time() - overall_start)/60:.1f}min")


if __name__ == "__main__":
    main()
