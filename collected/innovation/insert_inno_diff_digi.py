#!/usr/bin/env python3
"""Insert inno_diff (C3) and inno_digi (C4) entries into academic.db innovation_theory table."""

import json
import sqlite3
import glob
import os

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
JSON_DIR = "/Users/nishimura+/projects/research/academic-knowledge-db/collected/innovation"

def load_entries(prefix):
    entries = []
    pattern = os.path.join(JSON_DIR, f"{prefix}_*.json")
    files = sorted(glob.glob(pattern))
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            entries.extend(data)
    print(f"  Loaded {len(entries)} entries from {len(files)} files for prefix '{prefix}'")
    return entries

def normalize_json_field(value):
    """Convert list to JSON string if needed; keep string as-is."""
    if isinstance(value, list):
        return json.dumps(value, ensure_ascii=False)
    return value

def insert_entries(entries):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    sql = """
    INSERT OR REPLACE INTO innovation_theory (
        id, name_ja, name_en, definition, impact_summary,
        subfield, category, era_start, schumpeter_layer,
        key_researchers, key_works
    ) VALUES (
        :id, :name_ja, :name_en, :definition, :impact_summary,
        :subfield, :category, :era_start, :schumpeter_layer,
        :key_researchers, :key_works
    )
    """

    success = 0
    errors = 0
    for entry in entries:
        try:
            # Normalize list fields to JSON strings
            entry["key_researchers"] = normalize_json_field(entry.get("key_researchers"))
            entry["key_works"] = normalize_json_field(entry.get("key_works"))
            cur.execute(sql, entry)
            success += 1
        except Exception as e:
            print(f"  ERROR inserting {entry.get('id', '?')}: {e}")
            errors += 1

    conn.commit()
    conn.close()
    print(f"  Inserted: {success}, Errors: {errors}")
    return success

def main():
    all_entries = []

    print("=== Loading C3: diffusion_adoption_user ===")
    diff_entries = load_entries("inno_diff")
    all_entries.extend(diff_entries)

    print("=== Loading C4: platform_digital_innovation ===")
    digi_entries = load_entries("inno_digi")
    all_entries.extend(digi_entries)

    print(f"\nTotal entries to insert: {len(all_entries)}")
    print("\n=== Inserting into DB ===")
    total_inserted = insert_entries(all_entries)

    print(f"\n=== Done: {total_inserted} entries inserted ===")

    # Verify
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT subfield, COUNT(*) FROM innovation_theory GROUP BY subfield ORDER BY subfield")
    rows = cur.fetchall()
    conn.close()

    print("\n=== Verification: subfield counts ===")
    total = 0
    for row in rows:
        print(f"  {row[0]}: {row[1]}")
        total += row[1]
    print(f"  TOTAL: {total}")

if __name__ == "__main__":
    main()
