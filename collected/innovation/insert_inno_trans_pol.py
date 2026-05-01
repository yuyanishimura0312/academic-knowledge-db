#!/usr/bin/env python3
"""
Insert inno_trans_001~200 (D1) and inno_pol_001~200 (D2) into innovation_theory table.
"""
import json
import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
COLLECTED_DIR = Path("/Users/nishimura+/projects/research/academic-knowledge-db/collected/innovation")

JSON_FILES = [
    "inno_trans_001_050.json",
    "inno_trans_051_100.json",
    "inno_trans_101_150.json",
    "inno_trans_151_200.json",
    "inno_pol_001_050.json",
    "inno_pol_051_100.json",
    "inno_pol_101_150.json",
    "inno_pol_151_200.json",
]

def load_records():
    records = []
    seen_ids = set()
    for fname in JSON_FILES:
        fpath = COLLECTED_DIR / fname
        if not fpath.exists():
            print(f"  WARNING: File not found: {fpath}")
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        for rec in data:
            if rec["id"] not in seen_ids:
                seen_ids.add(rec["id"])
                records.append(rec)
            else:
                print(f"  DUPLICATE skipped: {rec['id']} (from {fname})")
    return records

def insert_records(records):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    inserted = 0
    skipped = 0
    errors = []

    for rec in records:
        try:
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
                rec.get("subfield", ""),
                rec.get("school_of_thought", ""),
                rec.get("era_start"),
                rec.get("era_end"),
                rec.get("schumpeter_layer", "meso"),
                rec.get("innovation_type", ""),
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

    if not records:
        print("No records found. Exiting.")
        return

    ids = sorted([r["id"] for r in records])
    print(f"  First ID: {ids[0]}")
    print(f"  Last ID : {ids[-1]}")

    # Count by prefix
    trans_count = sum(1 for r in records if r["id"].startswith("inno_trans_"))
    pol_count = sum(1 for r in records if r["id"].startswith("inno_pol_"))
    print(f"  inno_trans_* : {trans_count}")
    print(f"  inno_pol_*   : {pol_count}")

    print("\nInserting into academic.db...")
    inserted, skipped, errors = insert_records(records)

    print(f"\n=== Insert Result ===")
    print(f"  Inserted : {inserted}")
    print(f"  Skipped  : {skipped}")
    print(f"  Errors   : {len(errors)}")

    if errors:
        print("\nError details:")
        for eid, emsg in errors:
            print(f"  {eid}: {emsg}")

    # Verify counts
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM innovation_theory")
    total_all = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM innovation_theory WHERE id LIKE 'inno_trans_%'")
    total_trans = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM innovation_theory WHERE id LIKE 'inno_pol_%'")
    total_pol = cur.fetchone()[0]
    conn.close()

    print(f"\n=== DB Verification ===")
    print(f"  Total innovation_theory records : {total_all}")
    print(f"  inno_trans_* records            : {total_trans}")
    print(f"  inno_pol_* records              : {total_pol}")
    print("Done.")

if __name__ == "__main__":
    main()
