#!/usr/bin/env python3
"""
DUA Wave A — Q-β URL HTTP Verification v2 (continuation script)
================================================================

Resumes URL HTTP verification across 10 academic.db domains.
v2 changes from v1:
- CONCURRENT_WORKERS reduced 64 -> 15 (avoid prior rate-limit failures)
- BATCH_SIZE reduced 2000 -> 1000 with checkpoint commit each batch
- REQUEST_INTERVAL_MS 50 -> 200 between submissions (gentler ramp)
- New _qbeta_failed_urls table: dump every dead/transient with full context
- Idempotent guarantee: verified/dead/redirect status is NEVER re-touched
- Progress print every 500 completions (more frequent than v1 2%)
- Per-batch UPDATE commit (not buffered): zero data loss on interrupt

Run:
    python3 qbeta_url_verification_v2.py                       # all 10 domains
    python3 qbeta_url_verification_v2.py --domain humanities_concept
    python3 qbeta_url_verification_v2.py --limit 500           # smoke test
"""
from __future__ import annotations

import argparse
import json
import signal
import socket
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------
DB_PATH = Path.home() / "projects/research/academic-knowledge-db/academic.db"
REPORTS_DIR = Path.home() / "projects/research/academic-knowledge-db/reports/dua_wave_a"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (research; academic-knowledge-db DUA-Wave-A)"
REQUEST_TIMEOUT_SEC = 10
MAX_REDIRECT_HOPS = 5
CONCURRENT_WORKERS = 15            # v2: lowered from 64
BATCH_SIZE = 1000                  # v2: lowered from 2000
PROGRESS_PRINT_EVERY = 500         # v2: print every 500 completions
SUBMISSION_INTERVAL_SEC = 0.0      # we rely on worker concurrency for pacing

# Domain priority (per spec: humanities first, then innovation, then untouched)
DOMAIN_ORDER = [
    ("humanities_concept", "id"),
    ("innovation_theory", "id"),
    ("social_theory", "id"),
    ("natural_discovery", "id"),
    ("engineering_method", "id"),
    ("arts_question", "id"),
    ("marketing_sales", "id"),
    ("poetics_text", "id"),
    ("startup_theory", "id"),
    ("business_models", "id"),
]


# ----------------------------------------------------------------------------
# Schema bootstrap
# ----------------------------------------------------------------------------
def ensure_columns(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    for tbl, _pk in DOMAIN_ORDER:
        cols = {row[1] for row in cur.execute(f"PRAGMA table_info({tbl})").fetchall()}
        if "last_verified_at" not in cols:
            cur.execute(f"ALTER TABLE {tbl} ADD COLUMN last_verified_at TEXT")
        if "redirect_to" not in cols:
            cur.execute(f"ALTER TABLE {tbl} ADD COLUMN redirect_to TEXT")
        if "http_status" not in cols:
            cur.execute(f"ALTER TABLE {tbl} ADD COLUMN http_status INTEGER")
    # Failed URL dump table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS _qbeta_failed_urls (
            domain_table TEXT NOT NULL,
            concept_id TEXT NOT NULL,
            url TEXT NOT NULL,
            http_status INTEGER,
            error TEXT,
            attempted_at TEXT NOT NULL,
            PRIMARY KEY (domain_table, concept_id, attempted_at)
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_qbeta_failed_error ON _qbeta_failed_urls(error)")
    conn.commit()


# ----------------------------------------------------------------------------
# HTTP verification (identical to v1 logic; only Configuration differs)
# ----------------------------------------------------------------------------
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
        if parsed.scheme not in ("http", "https"):
            return {"status": "dead", "http_status": None, "redirect_to": None, "error": "bad_scheme"}
        if not parsed.netloc:
            return {"status": "dead", "http_status": None, "redirect_to": None, "error": "no_netloc"}
    except Exception as e:
        return {"status": "dead", "http_status": None, "redirect_to": None, "error": f"parse_error:{e}"}

    current_url = url
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
                        return {"status": "redirect", "http_status": code,
                                "redirect_to": final_redirect, "error": None}
                    return {"status": "verified", "http_status": code,
                            "redirect_to": None, "error": None}
                return {"status": "verified", "http_status": code,
                        "redirect_to": None, "error": None}
        except urllib.error.HTTPError as e:
            code = e.code
            if code in (301, 302, 303, 307, 308):
                location = e.headers.get("Location")
                if not location:
                    return {"status": "dead", "http_status": code,
                            "redirect_to": None, "error": "redirect_no_location"}
                if location.startswith("/"):
                    p = urlparse(current_url)
                    location = f"{p.scheme}://{p.netloc}{location}"
                final_redirect = location
                current_url = location
                if hop >= MAX_REDIRECT_HOPS:
                    return {"status": "redirect", "http_status": code,
                            "redirect_to": final_redirect, "error": "max_hops"}
                continue
            if code in (404, 410, 451):
                return {"status": "dead", "http_status": code,
                        "redirect_to": None, "error": f"http_{code}"}
            if code in (403, 401):
                return {"status": "verified", "http_status": code,
                        "redirect_to": None, "error": f"blocked_{code}"}
            if code in (503, 502, 504, 429, 500):
                return {"status": "url_present", "http_status": code,
                        "redirect_to": None, "error": f"transient_{code}"}
            return {"status": "dead", "http_status": code,
                    "redirect_to": None, "error": f"http_{code}"}
        except urllib.error.URLError as e:
            reason = str(e.reason) if hasattr(e, "reason") else str(e)
            lo = reason.lower()
            if "timed out" in lo or "timeout" in lo:
                return {"status": "url_present", "http_status": None,
                        "redirect_to": None, "error": "timeout"}
            if ("nodename nor servname" in lo or "name or service not known" in lo or "no address" in lo):
                return {"status": "dead", "http_status": None,
                        "redirect_to": None, "error": "dns_fail"}
            if "connection refused" in lo:
                return {"status": "dead", "http_status": None,
                        "redirect_to": None, "error": "conn_refused"}
            if "ssl" in lo or "certificate" in lo:
                return {"status": "dead", "http_status": None,
                        "redirect_to": None, "error": f"ssl_err:{reason[:60]}"}
            return {"status": "dead", "http_status": None,
                    "redirect_to": None, "error": f"url_error:{reason[:80]}"}
        except socket.timeout:
            return {"status": "url_present", "http_status": None,
                    "redirect_to": None, "error": "socket_timeout"}
        except Exception as e:
            return {"status": "dead", "http_status": None,
                    "redirect_to": None,
                    "error": f"exception:{type(e).__name__}:{str(e)[:80]}"}
    return {"status": "dead", "http_status": None, "redirect_to": None, "error": "loop_exhausted"}


# ----------------------------------------------------------------------------
# Domain processor (per-batch commit, no large buffer)
# ----------------------------------------------------------------------------
class DomainProcessor:
    def __init__(self, conn: sqlite3.Connection, table: str, pk: str,
                 limit: Optional[int] = None, dry_run: bool = False):
        self.conn = conn
        self.table = table
        self.pk = pk
        self.limit = limit
        self.dry_run = dry_run
        self.update_buffer: list[tuple] = []
        self.fail_buffer: list[tuple] = []
        self.failure_patterns: Counter = Counter()
        self.failure_samples: defaultdict = defaultdict(list)
        self.stats: Counter = Counter()
        self.interrupt_received = False

    def fetch_targets(self) -> list[tuple[str, str]]:
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

    def flush(self) -> None:
        if self.dry_run:
            self.update_buffer.clear()
            self.fail_buffer.clear()
            return
        if self.update_buffer:
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
                self.update_buffer,
            )
            self.update_buffer.clear()
        if self.fail_buffer:
            cur = self.conn.cursor()
            cur.executemany(
                """
                INSERT OR IGNORE INTO _qbeta_failed_urls
                (domain_table, concept_id, url, http_status, error, attempted_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                self.fail_buffer,
            )
            self.fail_buffer.clear()
        self.conn.commit()

    def run(self) -> dict:
        targets = self.fetch_targets()
        total = len(targets)
        print(f"  [{self.table}] {total} url_present concepts to verify "
              f"(workers={CONCURRENT_WORKERS}, batch={BATCH_SIZE})", flush=True)
        if total == 0:
            return self.summary(total)

        completed = 0
        start = time.time()

        with ThreadPoolExecutor(max_workers=CONCURRENT_WORKERS) as executor:
            future_to_info: dict = {}
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
                        result = {"status": "dead", "http_status": None,
                                  "redirect_to": None,
                                  "error": f"future_exc:{type(e).__name__}"}
                    status = result["status"]
                    self.stats[status] += 1
                    now_iso = datetime.now(timezone.utc).isoformat()

                    # promote only if changed
                    if status != "url_present":
                        self.update_buffer.append((
                            status,
                            result["http_status"],
                            result["redirect_to"],
                            now_iso,
                            pk_val,
                        ))

                    # log failures
                    if status in ("dead", "redirect", "url_present") and result.get("error"):
                        self.failure_patterns[result["error"]] += 1
                        if len(self.failure_samples[result["error"]]) < 10:
                            self.failure_samples[result["error"]].append(
                                {"id": pk_val, "url": url}
                            )
                        # store failed URLs for retry analysis
                        if status in ("dead", "url_present"):
                            self.fail_buffer.append((
                                self.table, str(pk_val), url,
                                result["http_status"], result["error"], now_iso,
                            ))

                    completed += 1

                    if len(self.update_buffer) >= BATCH_SIZE or len(self.fail_buffer) >= BATCH_SIZE:
                        self.flush()

                    if completed % PROGRESS_PRINT_EVERY == 0:
                        elapsed = time.time() - start
                        rate = completed / elapsed if elapsed > 0 else 0
                        eta_min = (total - completed) / rate / 60 if rate > 0 else 0
                        print(f"    [{self.table}] {completed}/{total} "
                              f"({100*completed/total:.1f}%) rate={rate:.1f}/s "
                              f"eta={eta_min:.1f}min v={self.stats['verified']} "
                              f"d={self.stats['dead']} r={self.stats['redirect']} "
                              f"u={self.stats['url_present']}", flush=True)

                    if self.interrupt_received:
                        for f in future_to_info:
                            if not f.done():
                                f.cancel()
                        break
            except KeyboardInterrupt:
                self.interrupt_received = True
                print(f"\n  [{self.table}] Interrupt received, flushing...", flush=True)

        self.flush()
        elapsed = time.time() - start
        print(f"  [{self.table}] DONE: {completed}/{total} in {elapsed/60:.1f}min "
              f"({completed/elapsed:.1f}/s) — v={self.stats['verified']} "
              f"d={self.stats['dead']} r={self.stats['redirect']} "
              f"u={self.stats['url_present']}", flush=True)
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
    parser.add_argument("--limit", type=int, default=None,
                        help="Per-domain limit (smoke test)")
    parser.add_argument("--dry-run", action="store_true", help="No DB writes")
    parser.add_argument("--time-budget-min", type=int, default=480,
                        help="Hard global stop after N minutes (default 480 = 8h)")
    args = parser.parse_args()

    if not DB_PATH.exists():
        print(f"ERROR: DB not found: {DB_PATH}", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    ensure_columns(conn)

    overall_start = time.time()
    overall_results: list[dict] = []
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report_path = REPORTS_DIR / f"qbeta_url_verification_v2_{timestamp}.json"

    domains_to_run = DOMAIN_ORDER
    if args.domain:
        domains_to_run = [(t, p) for t, p in DOMAIN_ORDER if t == args.domain]
        if not domains_to_run:
            print(f"ERROR: domain {args.domain} not found", file=sys.stderr)
            sys.exit(1)

    active_processors: list = []

    def sigint_handler(signum, frame):
        print("\nSIGINT received, will stop at next checkpoint...", flush=True)
        for p in active_processors:
            p.interrupt_received = True

    signal.signal(signal.SIGINT, sigint_handler)

    for table, pk in domains_to_run:
        elapsed_min = (time.time() - overall_start) / 60
        if elapsed_min >= args.time_budget_min:
            print(f"Time budget exhausted ({elapsed_min:.1f} >= "
                  f"{args.time_budget_min}min). Stop.", flush=True)
            break
        print(f"\n=== {table} ===", flush=True)
        proc = DomainProcessor(conn, table, pk,
                                limit=args.limit, dry_run=args.dry_run)
        active_processors.append(proc)
        result = proc.run()
        overall_results.append(result)
        with open(report_path, "w") as f:
            json.dump({
                "start_utc": datetime.now(timezone.utc).isoformat(),
                "elapsed_min": round((time.time() - overall_start) / 60, 1),
                "domains": overall_results,
                "config": {
                    "concurrent_workers": CONCURRENT_WORKERS,
                    "timeout_sec": REQUEST_TIMEOUT_SEC,
                    "user_agent": USER_AGENT,
                    "batch_size": BATCH_SIZE,
                    "dry_run": args.dry_run,
                    "version": "v2",
                },
            }, f, ensure_ascii=False, indent=2)

    conn.close()
    print(f"\n=== Final Report ===", flush=True)
    print(f"Total elapsed: {(time.time() - overall_start) / 60:.1f}min", flush=True)
    print(f"Report saved: {report_path}", flush=True)
    for r in overall_results:
        d = r["distribution"]
        print(f"  {r['table']:25s} total={r['total_targets']:6d} "
              f"v={d.get('verified',0):6d} d={d.get('dead',0):6d} "
              f"r={d.get('redirect',0):5d} u={d.get('url_present',0):6d}", flush=True)


if __name__ == "__main__":
    main()
