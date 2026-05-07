#!/usr/bin/env python3
"""Phase 10-B: relations importer."""
import json
import re
import sqlite3
import uuid
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
RELATIONS_DIR = Path("/tmp/poetics_relations_p10")


def parse_lenient(raw):
    raw = raw.strip()
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", raw, re.DOTALL)
    if m:
        raw = m.group(1)
    if not raw.startswith("{"):
        s, e = raw.find("{"), raw.rfind("}")
        if s != -1 and e != -1:
            raw = raw[s:e+1]
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id FROM humanities_concept")
    valid_ids = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT source_concept_id, target_concept_id, relation_type FROM humanities_concept_relations")
    existing = {(r[0], r[1], r[2]) for r in cur.fetchall()}

    inserted = skipped_existing = skipped_invalid = 0
    files_loaded = 0
    for f in sorted(RELATIONS_DIR.glob("*.json")):
        d = parse_lenient(f.read_text())
        if not d or "relations" not in d:
            continue
        files_loaded += 1
        for r in d["relations"]:
            s = r.get("source_concept_id")
            t = r.get("target_concept_id")
            rt = r.get("relation_type", "related_to")
            if not s or not t or s == t:
                skipped_invalid += 1
                continue
            if s not in valid_ids or t not in valid_ids:
                skipped_invalid += 1
                continue
            key = (s, t, rt)
            if key in existing:
                skipped_existing += 1
                continue
            existing.add(key)
            cur.execute("""INSERT INTO humanities_concept_relations
                (id, source_concept_id, target_concept_id, relation_type,
                 relation_description, strength, is_confirmed)
                VALUES (?,?,?,?,?,?,?)""",
                (str(uuid.uuid4()), s, t, rt,
                 r.get("relation_description"),
                 r.get("strength", 5),
                 r.get("is_confirmed", 1)))
            inserted += 1
    conn.commit()

    print(f"=== Relations import ===")
    print(f"Files: {files_loaded}")
    print(f"Inserted: {inserted}")
    print(f"Skipped (existing): {skipped_existing}")
    print(f"Skipped (invalid): {skipped_invalid}")

    cur.execute("SELECT COUNT(*) FROM humanities_concept_relations")
    print(f"\nTotal relations: {cur.fetchone()[0]}")
    cur.execute("""SELECT relation_type, COUNT(*) FROM humanities_concept_relations
                   GROUP BY relation_type ORDER BY 2 DESC""")
    print("\nBy type:")
    for t, n in cur.fetchall():
        print(f"  {t}: {n}")
    conn.close()


if __name__ == "__main__":
    main()
