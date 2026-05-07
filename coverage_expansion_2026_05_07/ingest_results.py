#!/usr/bin/env python3
"""Phase 3: Validate Codex JSON outputs and ingest into academic.db.

Reads outputs/*.json, validates schema, dedupes against existing name_en in
the target table, fills sensible defaults, and bulk-inserts as new rows.

Usage:
    python3 ingest_results.py            # Dry-run report
    python3 ingest_results.py --commit   # Actually insert
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).parent
PROJECT_ROOT = ROOT.parent
DB = PROJECT_ROOT / "academic.db"
DEFS = json.loads((ROOT / "task_definitions.json").read_text(encoding="utf-8"))
OUTPUTS = ROOT / "outputs"

TASK_BY_ID = {t["id"]: t for t in DEFS["tasks"]}

REQUIRED = ["name_ja", "name_en", "definition", "subfield", "era_start"]
ALLOWED_FIELDS = {
    "name_ja", "name_en", "name_original", "definition", "impact_summary",
    "subfield", "school_of_thought", "era_start", "era_end",
    "methodology_level", "target_domain", "application_conditions",
    "when_to_apply", "framing_questions", "opposing_concept_names",
    "keywords_ja", "keywords_en",
}


def extract_json_array(raw: str) -> list[dict]:
    """Codex sometimes wraps the JSON in code fences or chatter."""
    raw = raw.strip()
    if not raw:
        return []
    # Try direct parse first
    try:
        data = json.loads(raw)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        pass
    # Strip code fences
    fence_match = re.search(r"```(?:json)?\s*(.*?)```", raw, re.DOTALL)
    if fence_match:
        try:
            data = json.loads(fence_match.group(1))
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            pass
    # Find first [ ... ] block
    bracket = re.search(r"\[[\s\S]*\]", raw)
    if bracket:
        try:
            data = json.loads(bracket.group(0))
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            pass
    return []


def validate_entry(e: dict, allowed_subfields: set[str]) -> tuple[bool, str]:
    for f in REQUIRED:
        if not e.get(f):
            return False, f"missing {f}"
    if not isinstance(e.get("era_start"), int):
        try:
            e["era_start"] = int(e["era_start"])
        except (TypeError, ValueError):
            return False, "era_start not int"
    if e["subfield"] not in allowed_subfields:
        # allow loose matching: substring
        for s in allowed_subfields:
            if s in e["subfield"] or e["subfield"] in s:
                e["subfield"] = s
                break
        else:
            return False, f"subfield not in cluster: {e['subfield']}"
    if len(e["definition"]) < 30:
        return False, "definition too short"
    return True, ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", action="store_true")
    args = parser.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Cache existing name_en per table
    existing = {}
    for tbl in ("humanities_concept", "social_theory", "natural_discovery", "engineering_method", "arts_question"):
        existing[tbl] = {
            (row["name_en"] or "").strip().lower()
            for row in conn.execute(f"SELECT name_en FROM {tbl}")
            if row["name_en"]
        }

    grand = {"parsed": 0, "valid": 0, "deduped": 0, "inserted": 0, "by_table": {}}
    for task_id, task in TASK_BY_ID.items():
        path = OUTPUTS / f"{task_id}.json"
        if not path.exists() or path.stat().st_size == 0:
            print(f"[skip] {task_id}: no output yet")
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        entries = extract_json_array(raw)
        if not entries:
            print(f"[fail] {task_id}: no parseable JSON ({len(raw)} bytes)")
            continue

        table = task["table"]
        allowed_subfields = set(task["subfields"])
        # also allow loose: existing subfields
        for row in conn.execute(f"SELECT DISTINCT subfield FROM {table}"):
            if row[0]:
                allowed_subfields.add(row[0])

        kept = []
        seen_local = set()
        for e in entries:
            grand["parsed"] += 1
            ok, reason = validate_entry(e, allowed_subfields)
            if not ok:
                continue
            grand["valid"] += 1
            ne = e["name_en"].strip().lower()
            if ne in existing[table] or ne in seen_local:
                grand["deduped"] += 1
                continue
            seen_local.add(ne)
            kept.append(e)

        print(f"[{task_id}] parsed={len(entries)} valid={len(kept)+grand['deduped']-grand['deduped']} kept={len(kept)} → {table}")
        grand["by_table"].setdefault(table, 0)
        grand["by_table"][table] += len(kept)

        if args.commit and kept:
            cols = ["id"] + sorted(ALLOWED_FIELDS)
            placeholders = ",".join("?" * len(cols))
            sql = f"INSERT INTO {table} ({','.join(cols)}) VALUES ({placeholders})"
            rows = []
            for e in kept:
                vals = [str(uuid.uuid4())]
                for c in sorted(ALLOWED_FIELDS):
                    v = e.get(c)
                    if isinstance(v, list):
                        v = ",".join(str(x) for x in v)
                    vals.append(v)
                rows.append(vals)
            conn.executemany(sql, rows)
            grand["inserted"] += len(rows)

    if args.commit:
        conn.commit()
    conn.close()

    print("\n=== summary ===")
    for k, v in grand.items():
        print(f"  {k}: {v}")
    print(f"\nDB: {DB}")
    print(f"Mode: {'COMMITTED' if args.commit else 'DRY-RUN (use --commit)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
