#!/usr/bin/env python3
"""Ingest Step 2/3/4 outputs into academic.db.

Reads step234_outputs/*.json, validates, dedupes, inserts.
Each task spec has expected subfield from step234_tasks.json.
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
TASKS = json.loads((ROOT / "step234_tasks.json").read_text(encoding="utf-8"))["tasks"]
TASK_BY_ID = {t["id"]: t for t in TASKS}
OUTPUTS = ROOT / "step234_outputs"
TAXONOMY = json.loads((ROOT / "step1_taxonomy" / "taxonomy_v1.json").read_text(encoding="utf-8"))

REQUIRED = ["name_ja", "name_en", "definition", "subfield", "era_start"]
ALLOWED_FIELDS = {
    "name_ja", "name_en", "name_original", "definition", "impact_summary",
    "subfield", "school_of_thought", "era_start", "era_end",
    "methodology_level", "target_domain", "application_conditions",
    "when_to_apply", "framing_questions", "opposing_concept_names",
    "keywords_ja", "keywords_en",
}


def _try_parse_objects(raw: str) -> list[dict]:
    """Find every {...} top-level block and parse individually."""
    objs = []
    i = 0
    n = len(raw)
    while i < n:
        if raw[i] != "{":
            i += 1
            continue
        depth = 0
        in_str = False
        esc = False
        start = i
        while i < n:
            c = raw[i]
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = not in_str
            elif not in_str:
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        chunk = raw[start:i+1]
                        try:
                            d = json.loads(chunk)
                            if isinstance(d, dict) and "name_ja" in d:
                                objs.append(d)
                        except json.JSONDecodeError:
                            pass
                        i += 1
                        break
            i += 1
        else:
            break
    return objs


def extract_json_array(raw: str) -> list[dict]:
    raw = raw.strip()
    if not raw:
        return []
    # Try direct parse
    try:
        d = json.loads(raw)
        return d if isinstance(d, list) else []
    except json.JSONDecodeError:
        pass
    # Code fence
    fence = re.search(r"```(?:json)?\s*(.*?)```", raw, re.DOTALL)
    if fence:
        try:
            d = json.loads(fence.group(1))
            return d if isinstance(d, list) else []
        except json.JSONDecodeError:
            pass
    # Find every "[" possibly starting a JSON array (followed by {) and try parse
    candidates = []
    for m in re.finditer(r"\[\s*\{", raw):
        start = m.start()
        depth = 0
        for i in range(start, len(raw)):
            c = raw[i]
            if c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0:
                    candidates.append((start, i + 1))
                    break
    best = []
    for s, e in candidates:
        try:
            d = json.loads(raw[s:e])
            if isinstance(d, list) and len(d) > len(best):
                best = d
        except json.JSONDecodeError:
            continue
    if best:
        return best
    # Last resort: parse each {...} block individually
    return _try_parse_objects(raw)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--commit", action="store_true")
    args = p.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    existing = {}
    for tbl in ("humanities_concept", "social_theory", "natural_discovery", "engineering_method", "arts_question"):
        existing[tbl] = {(r["name_en"] or "").strip().lower() for r in conn.execute(f"SELECT name_en FROM {tbl}") if r["name_en"]}

    grand = {"parsed": 0, "kept": 0, "deduped": 0, "inserted": 0, "by_table": {}}
    for tid, task in TASK_BY_ID.items():
        path = OUTPUTS / f"{tid}.json"
        if not path.exists() or path.stat().st_size < 100:
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        entries = extract_json_array(raw)
        if not entries:
            print(f"[fail] {tid}: no parseable JSON ({len(raw)} bytes)")
            continue

        table = task["table"]
        canonical_subfield = task["subfield"]
        canon_set = set(TAXONOMY["domains"][table]["subfields"])

        kept = []
        seen_local = set()
        for e in entries:
            grand["parsed"] += 1
            if not all(e.get(f) for f in REQUIRED):
                continue
            if not isinstance(e.get("era_start"), int):
                try:
                    e["era_start"] = int(e["era_start"])
                except (TypeError, ValueError):
                    continue
            # Force the canonical subfield (task-specified)
            e["subfield"] = canonical_subfield
            if len(e.get("definition", "")) < 30:
                continue
            ne = e["name_en"].strip().lower()
            if ne in existing[table] or ne in seen_local:
                grand["deduped"] += 1
                continue
            seen_local.add(ne)
            kept.append(e)

        print(f"[{tid}] parsed={len(entries)} kept={len(kept)} → {table}/{canonical_subfield}")
        grand["kept"] += len(kept)
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
    print("Mode:", "COMMITTED" if args.commit else "DRY-RUN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
