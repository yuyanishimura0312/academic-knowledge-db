#!/usr/bin/env python3
"""Ingest task23 outputs (Tasks 2/3) into academic.db.

Task 2 entries: subfield specified by task spec
Task 3 entries: subfield from JSON entry (must match canonical taxonomy)
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
TASKS = json.loads((ROOT / "task23_specs.json").read_text(encoding="utf-8"))["tasks"]
TASK_BY_ID = {t["id"]: t for t in TASKS}
OUTPUTS = ROOT / "task23_outputs"
TAXONOMY = json.loads((ROOT / "step1_taxonomy" / "taxonomy_v1.json").read_text(encoding="utf-8"))

REQUIRED = ["name_ja", "name_en", "definition", "era_start"]
ALLOWED_FIELDS = {
    "name_ja", "name_en", "name_original", "definition", "impact_summary",
    "subfield", "school_of_thought", "era_start", "era_end",
    "methodology_level", "target_domain", "application_conditions",
    "when_to_apply", "framing_questions", "opposing_concept_names",
    "keywords_ja", "keywords_en",
}


def _try_parse_objects(raw: str) -> list[dict]:
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
                        try:
                            d = json.loads(raw[start:i+1])
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


def extract_array(raw: str) -> list[dict]:
    raw = raw.strip()
    if not raw:
        return []
    try:
        d = json.loads(raw)
        return d if isinstance(d, list) else []
    except json.JSONDecodeError:
        pass
    fence = re.search(r"```(?:json)?\s*(.*?)```", raw, re.DOTALL)
    if fence:
        try:
            d = json.loads(fence.group(1))
            return d if isinstance(d, list) else []
        except json.JSONDecodeError:
            pass
    candidates = []
    for m in re.finditer(r"\[\s*\{", raw):
        s = m.start()
        depth = 0
        for j in range(s, len(raw)):
            c = raw[j]
            if c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0:
                    candidates.append((s, j+1))
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
        entries = extract_array(raw)
        if not entries:
            print(f"[fail] {tid}: no parseable JSON ({len(raw)} bytes)")
            continue

        table = task["table"]
        canon_set = set(TAXONOMY["domains"][table]["subfields"])
        is_distrib = task.get("subfield_distribute", False)

        kept = []
        seen_local = set()
        for e in entries:
            grand["parsed"] += 1
            if not all(e.get(f) for f in REQUIRED):
                continue
            try:
                e["era_start"] = int(e["era_start"])
            except (TypeError, ValueError):
                continue
            if is_distrib:
                # T3: must match canonical
                sub = e.get("subfield", "")
                if sub not in canon_set:
                    # try fuzzy match
                    matched = False
                    for c in canon_set:
                        if c in sub or sub in c:
                            e["subfield"] = c
                            matched = True
                            break
                    if not matched:
                        continue
            else:
                # T2: force task spec subfield
                e["subfield"] = task["subfield"]
            if len(e.get("definition", "")) < 30:
                continue
            ne = e["name_en"].strip().lower()
            if ne in existing[table] or ne in seen_local:
                grand["deduped"] += 1
                continue
            seen_local.add(ne)
            kept.append(e)

        print(f"[{tid}] parsed={len(entries)} kept={len(kept)} → {table}")
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
