#!/usr/bin/env python3
"""
DUA Wave A — Q-β URL HTTP Verification
=======================================

Verifies source_url for all concepts in academic.db across 10 domains.
Promotes verification_status from 'url_present' to 'verified'/'dead'/'redirect'
based on actual HTTP GET results.

Design principles:
- ThreadPoolExecutor with 20 concurrent workers per domain batch
- 10-second timeout per request, max 5 redirect hops
- Idempotent: re-running skips already verified/dead concepts
- Batched SQLite writes (5000 rows per UPDATE transaction)
- Progress checkpoints every 5% with commit
- Interrupt-safe (CTRL-C lands cleanly at next checkpoint)
- Failure pattern analysis dumped as JSON report

Usage:
    python3 qbeta_url_verification.py [--domain humanities_concept] [--limit 1000] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import os
import signal
import sqlite3
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import urllib.request
import urllib.error
import socket

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------
DB_PATH = Path.home() / "projects/research/academic-knowledge-db/academic.db"
REPORTS_DIR = Path.home() / "projects/research/academic-knowledge-db/reports/dua_wave_a"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (research; academic-knowledge-db DUA-Wave-A)"
REQUEST_TIMEOUT_SEC = 10
MAX_REDIRECT_HOPS = 5
CONCURRENT_WORKERS = 64  # increased from 20 for better throughput
REQUEST_INTERVAL_MS = 50  # per worker, very light throttling
BATCH_SIZE = 2000  # SQLite write batch size
CHECKPOINT_RATIO = 0.02  # commit every 2%

# Domain priority order (per spec)
DOMAIN_ORDER = [
    # Wave A2 expansion NOT touching these 3 first
    ("innovation_theory", "id"),
    ("marketing_sales", "id"),
    ("poetics_text", "id"),
    # Small, completed Era 3 sample
    ("business_models", "id"),
    # 5 core domains (Wave A2 in flight, write carefully)
    ("humanities_concept", "id"),
    ("social_theory", "id"),
    ("natural_discovery", "id"),
    ("engineering_method", "id"),
    ("arts_question", "id"),
    # Last
    ("startup_theory", "id"),
]


# ----------------------------------------------------------------------------
# Schema bootstrap
# ----------------------------------------------------------------------------
def ensure_columns(conn: sqlite3.Connection) -> None:
    """Add last_verified_at, redirect_to, http_status columns if missing."""
    cur = conn.cursor()
    for tbl, _pk in DOMAIN_ORDER:
        cols = {row[1] for row in cur.execute(f"PRAGMA table_info({tbl})").fetchall()}
        if "last_verified_at" not in cols:
            cur.execute(f"ALTER TABLE {tbl} ADD COLUMN last_verified_at TEXT")
        if "redirect_to" not in cols:
            cur.execute(f"ALTER TABLE {tbl} ADD COLUMN redirect_to TEXT")
        if "http_status" not in cols:
            cur.execute(f"ALTER TABLE {tbl} ADD COLUMN http_status INTEGER")
    conn.commit()


# ----------------------------------------------------------------------------
# HTTP verification
# ----------------------------------------------------------------------------
class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Track redirects but don't auto-follow beyond what we want."""

    def http_error_301(self, req, fp, code, msg, headers):
        return None

    http_error_302 = http_error_301
    http_error_303 = http_error_301
    http_error_307 = http_error_301
    http_error_308 = http_error_301


def verify_url(url: str) -> dict:
    """
    Verify a single URL. Returns dict with:
      - status: 'verified' / 'dead' / 'redirect' / 'url_present' (transient retry)
      - http_status: HTTP status code or None
      - redirect_to: final URL if redirected
      - error: error message if failed
    """
    if not url or not url.strip():
        return {"status": "dead", "http_status": None, "redirect_to": None, "error": "empty_url"}

    url = url.strip()
    # Basic URL sanity check
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return {"status": "dead", "http_status": None, "redirect_to": None, "error": "bad_scheme"}
        if not parsed.netloc:
            return {"status": "dead", "http_status": None, "redirect_to": None, "error": "no_netloc"}
    except Exception as e:
        return {"status": "dead", "http_status": None, "redirect_to": None, "error": f"parse_error:{e}"}

    current_url = url
    redirect_chain = []
    final_redirect = None

    for hop in range(MAX_REDIRECT_HOPS + 1):
        req = urllib.request.Request(
            current_url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en;q=0.9, ja;q=0.8",
            },
            method="GET",
        )

        try:
            opener = urllib.request.build_opener(NoRedirect)
            with opener.open(req, timeout=REQUEST_TIMEOUT_SEC) as resp:
                code = resp.status
                if 200 <= code < 300:
                    if final_redirect is not None:
                        return {
                            "status": "redirect",
                            "http_status": code,
                            "redirect_to": final_redirect,
                            "error": None,
                        }
                    return {
                        "status": "verified",
                        "http_status": code,
                        "redirect_to": None,
                        "error": None,
                    }
                # 2xx without normal codes — count as verified
                return {
                    "status": "verified",
                    "http_status": code,
                    "redirect_to": None,
                    "error": None,
                }
        except urllib.error.HTTPError as e:
            code = e.code
            if code in (301, 302, 303, 307, 308):
                location = e.headers.get("Location")
                if not location:
                    return {"status": "dead", "http_status": code, "redirect_to": None, "error": "redirect_no_location"}
                # Resolve relative URL
                if location.startswith("/"):
                    p = urlparse(current_url)
                    location = f"{p.scheme}://{p.netloc}{location}"
                redirect_chain.append(location)
                final_redirect = location
                current_url = location
                if hop >= MAX_REDIRECT_HOPS:
                    return {
                        "status": "redirect",
                        "http_status": code,
                        "redirect_to": final_redirect,
                        "error": "max_hops",
                    }
                continue
            if code in (404, 410, 451):
                return {"status": "dead", "http_status": code, "redirect_to": None, "error": f"http_{code}"}
            if code in (403, 401):
                # Some sites block bots but URL exists — count as verified with warning
                return {"status": "verified", "http_status": code, "redirect_to": None, "error": f"blocked_{code}"}
            if code in (503, 502, 504, 429, 500):
                # transient
                return {"status": "url_present", "http_status": code, "redirect_to": None, "error": f"transient_{code}"}
            # Other 4xx/5xx
            return {"status": "dead", "http_status": code, "redirect_to": None, "error": f"http_{code}"}
        except urllib.error.URLError as e:
            reason = str(e.reason) if hasattr(e, "reason") else str(e)
            if "timed out" in reason.lower() or "timeout" in reason.lower():
                return {"status": "url_present", "http_status": None, "redirect_to": None, "error": "timeout"}
            if "nodename nor servname" in reason.lower() or "name or service not known" in reason.lower() or "no address" in reason.lower():
                return {"status": "dead", "http_status": None, "redirect_to": None, "error": "dns_fail"}
            if "connection refused" in reason.lower():
                return {"status": "dead", "http_status": None, "redirect_to": None, "error": "conn_refused"}
            return {"status": "dead", "http_status": None, "redirect_to": None, "error": f"url_error:{reason[:80]}"}
        except socket.timeout:
            return {"status": "url_present", "http_status": None, "redirect_to": None, "error": "socket_timeout"}
        except Exception as e:
            return {"status": "dead", "http_status": None, "redirect_to": None, "error": f"exception:{type(e).__name__}:{str(e)[:80]}"}

    return {"status": "dead", "http_status": None, "redirect_to": None, "error": "loop_exhausted"}


# ----------------------------------------------------------------------------
# Domain processor
# ----------------------------------------------------------------------------
class DomainProcessor:
    def __init__(self, conn: sqlite3.Connection, table: str, pk: str, limit: Optional[int] = None, dry_run: bool = False):
        self.conn = conn
        self.table = table
        self.pk = pk
        self.limit = limit
        self.dry_run = dry_run
        self.results_buffer = []  # list of (status, http_status, redirect_to, last_verified_at, pk_value)
        self.failure_patterns = Counter()
        self.failure_samples = defaultdict(list)  # error -> list of (id, url)
        self.stats = Counter()
        self.interrupt_received = False

    def fetch_targets(self) -> list[tuple[str, str]]:
        """Fetch (id, url) for concepts with url_present status."""
        cur = self.conn.cursor()
        sql = f"""
        SELECT {self.pk}, source_url
        FROM {self.table}
        WHERE verification_status = 'url_present'
          AND source_url IS NOT NULL
          AND source_url != ''
        """
        if self.limit:
            sql += f" LIMIT {self.limit}"
        return cur.execute(sql).fetchall()

    def flush_buffer(self) -> int:
        """Write buffered results to DB."""
        if not self.results_buffer or self.dry_run:
            self.results_buffer.clear()
            return 0
        cur = self.conn.cursor()
        cur.executemany(
            f"""
            UPDATE {self.table}
            SET verification_status = ?,
                http_status = ?,
                redirect_to = ?,
                last_verified_at = ?
            WHERE {self.pk} = ?
            """,
            self.results_buffer,
        )
        count = len(self.results_buffer)
        self.conn.commit()
        self.results_buffer.clear()
        return count

    def run(self) -> dict:
        targets = self.fetch_targets()
        total = len(targets)
        print(f"  [{self.table}] {total} concepts to verify")
        if total == 0:
            return self.summary(total)

        checkpoint_step = max(1, int(total * CHECKPOINT_RATIO))
        next_checkpoint = checkpoint_step
        completed = 0
        start = time.time()

        with ThreadPoolExecutor(max_workers=CONCURRENT_WORKERS) as executor:
            future_to_info = {}
            for pk_val, url in targets:
                if self.interrupt_received:
                    break
                fut = executor.submit(verify_url, url)
                future_to_info[fut] = (pk_val, url)

            try:
                for fut in as_completed(future_to_info):
                    pk_val, url = future_to_info[fut]
                    try:
                        result = fut.result(timeout=REQUEST_TIMEOUT_SEC + 5)
                    except Exception as e:
                        result = {"status": "dead", "http_status": None, "redirect_to": None, "error": f"future_exc:{type(e).__name__}"}

                    status = result["status"]
                    self.stats[status] += 1
                    if status in ("dead", "redirect") and result.get("error"):
                        self.failure_patterns[result["error"]] += 1
                        if len(self.failure_samples[result["error"]]) < 10:
                            self.failure_samples[result["error"]].append({"id": pk_val, "url": url})

                    now_iso = datetime.now(timezone.utc).isoformat()
                    # Only update if changed from url_present (don't downgrade)
                    if status != "url_present":
                        self.results_buffer.append((
                            status,
                            result["http_status"],
                            result["redirect_to"],
                            now_iso,
                            pk_val,
                        ))

                    completed += 1
                    if len(self.results_buffer) >= BATCH_SIZE:
                        self.flush_buffer()

                    if completed >= next_checkpoint:
                        elapsed = time.time() - start
                        rate = completed / elapsed if elapsed > 0 else 0
                        eta_sec = (total - completed) / rate if rate > 0 else 0
                        written = self.flush_buffer() if self.results_buffer else 0
                        print(f"    [{self.table}] {completed}/{total} ({100*completed/total:.1f}%) "
                              f"rate={rate:.1f}/s eta={eta_sec/60:.1f}min "
                              f"v={self.stats['verified']} d={self.stats['dead']} r={self.stats['redirect']} u={self.stats['url_present']}")
                        next_checkpoint += checkpoint_step

                    if self.interrupt_received:
                        # cancel remaining
                        for f in future_to_info:
                            if not f.done():
                                f.cancel()
                        break
            except KeyboardInterrupt:
                self.interrupt_received = True
                print(f"\n  [{self.table}] Interrupt received, finalizing...")

        # Final flush
        self.flush_buffer()
        elapsed = time.time() - start
        print(f"  [{self.table}] DONE: {completed}/{total} in {elapsed/60:.1f}min "
              f"({completed/elapsed:.1f}/s) — v={self.stats['verified']} d={self.stats['dead']} "
              f"r={self.stats['redirect']} u={self.stats['url_present']}")
        return self.summary(total, completed=completed, elapsed=elapsed)

    def summary(self, total: int, completed: int = 0, elapsed: float = 0.0) -> dict:
        return {
            "table": self.table,
            "total_targets": total,
            "completed": completed,
            "elapsed_sec": round(elapsed, 1),
            "distribution": dict(self.stats),
            "failure_patterns_top": dict(self.failure_patterns.most_common(30)),
            "failure_samples": {k: v for k, v in list(self.failure_samples.items())[:30]},
        }


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", help="Run for specific domain only", default=None)
    parser.add_argument("--limit", type=int, help="Limit per domain (testing)", default=None)
    parser.add_argument("--dry-run", action="store_true", help="No DB writes")
    parser.add_argument("--time-budget-min", type=int, default=600, help="Total time budget in minutes")
    args = parser.parse_args()

    if not DB_PATH.exists():
        print(f"ERROR: DB not found: {DB_PATH}", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    ensure_columns(conn)

    overall_start = time.time()
    overall_results = []
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report_path = REPORTS_DIR / f"qbeta_url_verification_{timestamp}.json"

    domains_to_run = DOMAIN_ORDER
    if args.domain:
        domains_to_run = [(t, p) for t, p in DOMAIN_ORDER if t == args.domain]
        if not domains_to_run:
            print(f"ERROR: domain {args.domain} not found", file=sys.stderr)
            sys.exit(1)

    # Signal handler
    def sigint_handler(signum, frame):
        print("\nSIGINT received, shutting down at next checkpoint...")
        for proc in active_processors:
            proc.interrupt_received = True

    active_processors = []
    signal.signal(signal.SIGINT, sigint_handler)

    for table, pk in domains_to_run:
        elapsed_min = (time.time() - overall_start) / 60
        if elapsed_min >= args.time_budget_min:
            print(f"Time budget exhausted ({elapsed_min:.1f}min >= {args.time_budget_min}min). Stopping.")
            break

        print(f"\n=== {table} ===")
        proc = DomainProcessor(conn, table, pk, limit=args.limit, dry_run=args.dry_run)
        active_processors.append(proc)
        result = proc.run()
        overall_results.append(result)

        # Write intermediate report
        with open(report_path, "w") as f:
            json.dump({
                "start": datetime.now(timezone.utc).isoformat(),
                "elapsed_min": round((time.time() - overall_start) / 60, 1),
                "domains": overall_results,
                "config": {
                    "concurrent_workers": CONCURRENT_WORKERS,
                    "timeout_sec": REQUEST_TIMEOUT_SEC,
                    "user_agent": USER_AGENT,
                    "batch_size": BATCH_SIZE,
                    "dry_run": args.dry_run,
                },
            }, f, ensure_ascii=False, indent=2)

    conn.close()

    print(f"\n=== Final Report ===")
    print(f"Total elapsed: {(time.time() - overall_start) / 60:.1f}min")
    print(f"Report saved: {report_path}")

    # Print summary
    for r in overall_results:
        d = r["distribution"]
        print(f"  {r['table']:25s} total={r['total_targets']:6d} v={d.get('verified',0):6d} d={d.get('dead',0):6d} r={d.get('redirect',0):5d} u={d.get('url_present',0):6d}")


if __name__ == "__main__":
    main()
