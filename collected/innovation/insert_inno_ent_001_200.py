#!/usr/bin/env python3
"""Insert inno_ent_001 through inno_ent_200 into academic.db innovation_theory table."""

import json
import sqlite3
import glob
import os

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
JSON_DIR = "/Users/nishimura+/projects/research/academic-knowledge-db/collected/innovation"

def load_entries():
    entries = []
    pattern = os.path.join(JSON_DIR, "inno_ent_*.json")
    files = sorted(glob.glob(pattern))
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            entries.extend(data)
    print(f"Loaded {len(entries)} entries from {len(files)} files")
    return entries

def insert_entries(entries):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    sql = """
    INSERT OR REPLACE INTO innovation_theory (
        id, name_ja, name_en, definition, impact_summary,
        subfield, category, school_of_thought, era_start, era_end,
        schumpeter_layer, innovation_type, cognitive_mechanism,
        key_researchers, key_works, keywords_ja, keywords_en,
        opposing_concept_names, methodology_level, status,
        source_reliability, data_completeness
    ) VALUES (
        :id, :name_ja, :name_en, :definition, :impact_summary,
        :subfield, :category, :school_of_thought, :era_start, :era_end,
        :schumpeter_layer, :innovation_type, :cognitive_mechanism,
        :key_researchers, :key_works, :keywords_ja, :keywords_en,
        :opposing_concept_names, :methodology_level, :status,
        :source_reliability, :data_completeness
    )
    """

    success = 0
    errors = 0
    for entry in entries:
        # Serialize list fields to JSON strings
        for field in ["key_researchers", "key_works", "keywords_ja", "keywords_en", "opposing_concept_names"]:
            if field in entry and isinstance(entry[field], list):
                entry[field] = json.dumps(entry[field], ensure_ascii=False)

        # Set defaults for missing fields
        entry.setdefault("era_end", None)
        entry.setdefault("methodology_level", None)
        entry.setdefault("status", "active")
        entry.setdefault("source_reliability", 4)
        entry.setdefault("data_completeness", 80)
        entry.setdefault("schumpeter_layer", None)
        entry.setdefault("innovation_type", None)
        entry.setdefault("cognitive_mechanism", None)
        entry.setdefault("opposing_concept_names", None)

        try:
            cur.execute(sql, entry)
            success += 1
        except Exception as e:
            print(f"Error inserting {entry.get('id')}: {e}")
            errors += 1

    conn.commit()
    conn.close()
    print(f"Inserted: {success}, Errors: {errors}")
    return success

def verify():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM innovation_theory WHERE id LIKE 'inno_ent_%'")
    count = cur.fetchone()[0]
    conn.close()
    print(f"Verification: {count} inno_ent_* entries in innovation_theory")
    return count

if __name__ == "__main__":
    entries = load_entries()
    inserted = insert_entries(entries)
    verify()
