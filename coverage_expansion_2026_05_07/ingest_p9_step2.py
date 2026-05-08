#!/usr/bin/env python3
"""Ingest P9 step 2 outputs (薄分野拡張)."""
from __future__ import annotations
import argparse, json, re, sqlite3, sys, uuid
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT.parent / "academic.db"
TASKS = json.loads((ROOT / "p9_step2_tasks.json").read_text(encoding="utf-8"))["tasks"]
TASK_BY_ID = {t["id"]: t for t in TASKS}
OUTPUTS = ROOT / "p9_step2_outputs"

REQUIRED = ["name_ja", "name_en", "definition", "era_start"]
ALLOWED_FIELDS = {"name_ja", "name_en", "name_original", "definition", "impact_summary", "subfield", "school_of_thought", "era_start", "era_end", "methodology_level", "target_domain", "application_conditions", "when_to_apply", "framing_questions", "opposing_concept_names", "keywords_ja", "keywords_en"}


def _try_parse_objects(raw):
    objs = []; i = 0; n = len(raw)
    while i < n:
        if raw[i] != "{":
            i += 1; continue
        depth = 0; in_str = False; esc = False; start = i
        while i < n:
            c = raw[i]
            if esc: esc = False
            elif c == "\\": esc = True
            elif c == '"': in_str = not in_str
            elif not in_str:
                if c == "{": depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        try:
                            d = json.loads(raw[start:i+1])
                            if isinstance(d, dict) and "name_ja" in d: objs.append(d)
                        except json.JSONDecodeError: pass
                        i += 1; break
            i += 1
        else: break
    return objs


def extract_array(raw):
    raw = raw.strip()
    if not raw: return []
    try:
        d = json.loads(raw)
        return d if isinstance(d, list) else []
    except: pass
    fence = re.search(r"```(?:json)?\s*(.*?)```", raw, re.DOTALL)
    if fence:
        try:
            d = json.loads(fence.group(1))
            return d if isinstance(d, list) else []
        except: pass
    cands = []
    for m in re.finditer(r"\[\s*\{", raw):
        s = m.start(); depth = 0
        for j in range(s, len(raw)):
            c = raw[j]
            if c == "[": depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0: cands.append((s, j+1)); break
    best = []
    for s, e in cands:
        try:
            d = json.loads(raw[s:e])
            if isinstance(d, list) and len(d) > len(best): best = d
        except: continue
    return best if best else _try_parse_objects(raw)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--commit", action="store_true")
    args = p.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    existing = {}
    for tbl in ("humanities_concept", "social_theory", "natural_discovery", "engineering_method", "arts_question"):
        existing[tbl] = {(r["name_en"] or "").strip().lower() for r in conn.execute(f"SELECT name_en FROM {tbl}") if r["name_en"]}

    grand = {"parsed": 0, "kept": 0, "deduped": 0, "inserted": 0, "by_table": {}}
    for tid, task in TASK_BY_ID.items():
        path = OUTPUTS / f"{tid}.json"
        if not path.exists() or path.stat().st_size < 100: continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        entries = extract_array(raw)
        if not entries:
            print(f"[fail] {tid}"); continue
        table = task["table"]; sub = task["subfield"]
        kept = []; seen = set()
        for e in entries:
            grand["parsed"] += 1
            if not all(e.get(f) for f in REQUIRED): continue
            try: e["era_start"] = int(e["era_start"])
            except: continue
            e["subfield"] = sub
            if len(e.get("definition", "")) < 30: continue
            ne = e["name_en"].strip().lower()
            if ne in existing[table] or ne in seen:
                grand["deduped"] += 1; continue
            seen.add(ne); kept.append(e)
        print(f"[{tid}] parsed={len(entries)} kept={len(kept)} → {table}/{sub}")
        grand["kept"] += len(kept)
        grand["by_table"].setdefault(table, 0); grand["by_table"][table] += len(kept)
        if args.commit and kept:
            cols = ["id"] + sorted(ALLOWED_FIELDS)
            ph = ",".join("?" * len(cols))
            sql = f"INSERT INTO {table} ({','.join(cols)}) VALUES ({ph})"
            rows = []
            for e in kept:
                vals = [str(uuid.uuid4())]
                for c in sorted(ALLOWED_FIELDS):
                    v = e.get(c)
                    if isinstance(v, list): v = ",".join(str(x) for x in v)
                    vals.append(v)
                rows.append(vals)
            conn.executemany(sql, rows)
            grand["inserted"] += len(rows)

    if args.commit: conn.commit()
    conn.close()
    print(f"\nsummary: {grand}")
    print("Mode:", "COMMITTED" if args.commit else "DRY-RUN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
