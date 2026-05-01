#!/usr/bin/env python3
"""
Insert inno_sys_001 to inno_sys_100 into innovation_theory table.
"""
import json
import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
COLLECTED_DIR = Path("/Users/nishimura+/projects/research/academic-knowledge-db/collected/innovation")

JSON_FILES = [
    "inno_sys_001_040_nis1.json",
    "inno_sys_021_040_nis2.json",
    "inno_sys_041_070_ris.json",
    "inno_sys_071_100_tis_sis.json",
]

def load_records():
    records = []
    seen_ids = set()
    for fname in JSON_FILES:
        fpath = COLLECTED_DIR / fname
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        for rec in data:
            if rec["id"] not in seen_ids:
                seen_ids.add(rec["id"])
                records.append(rec)
    return records

def insert_records(records):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    inserted = 0
    skipped = 0
    errors = []

    for rec in records:
        try:
            # Convert list fields to JSON strings
            key_researchers = json.dumps(rec.get("key_researchers", []), ensure_ascii=False)
            key_works = json.dumps(rec.get("key_works", []), ensure_ascii=False)

            cur.execute("""
                INSERT OR IGNORE INTO innovation_theory (
                    id, name_ja, name_en,
                    definition, impact_summary,
                    subfield, school_of_thought,
                    era_start, era_end,
                    schumpeter_layer, innovation_type,
                    cognitive_mechanism,
                    key_researchers, key_works,
                    keywords_ja, keywords_en,
                    opposing_concept_names,
                    status, source_reliability, data_completeness,
                    created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                rec["id"],
                rec.get("name_ja", ""),
                rec.get("name_en", ""),
                rec.get("definition", ""),
                rec.get("impact_summary", ""),
                rec.get("subfield", "innovation_systems"),
                rec.get("school_of_thought", ""),
                rec.get("era_start"),
                rec.get("era_end"),
                rec.get("schumpeter_layer", "macro"),
                rec.get("innovation_type", "systemic"),
                rec.get("cognitive_mechanism", ""),
                key_researchers,
                key_works,
                rec.get("keywords_ja", ""),
                rec.get("keywords_en", ""),
                rec.get("opposing_concept_names", ""),
                "active",
                "secondary",
                80,
                datetime.now().isoformat(),
                datetime.now().isoformat(),
            ))

            if cur.rowcount > 0:
                inserted += 1
            else:
                skipped += 1
                print(f"  SKIP (already exists): {rec['id']}")

        except Exception as e:
            errors.append((rec["id"], str(e)))
            print(f"  ERROR {rec['id']}: {e}")

    conn.commit()
    conn.close()
    return inserted, skipped, errors

def main():
    print("Loading records from JSON files...")
    records = load_records()
    print(f"  Total unique records loaded: {len(records)}")

    # Verify IDs
    ids = sorted([r["id"] for r in records])
    print(f"  ID range: {ids[0]} ~ {ids[-1]}")

    print("\nInserting into academic.db...")
    inserted, skipped, errors = insert_records(records)

    print(f"\n=== Result ===")
    print(f"  Inserted : {inserted}")
    print(f"  Skipped  : {skipped}")
    print(f"  Errors   : {len(errors)}")

    if errors:
        print("\nError details:")
        for eid, emsg in errors:
            print(f"  {eid}: {emsg}")

    # Verify
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM innovation_theory WHERE id LIKE 'inno_sys_%'")
    total = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM innovation_theory WHERE id BETWEEN 'inno_sys_001' AND 'inno_sys_100'")
    front = cur.fetchone()[0]
    conn.close()

    print(f"\n=== DB Verification ===")
    print(f"  Total inno_sys_* records : {total}")
    print(f"  inno_sys_001~100 records : {front}")
    print("Done.")

if __name__ == "__main__":
    main()
