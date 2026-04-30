#!/usr/bin/env python3
"""
Import innovation_systems subfield JSON data into innovation_theory table.
Usage: python3 scripts/import_innovation_systems.py
"""

import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
DATA_DIR = Path(__file__).parent.parent / "collected" / "social_sciences"

FILES = [
    "innovation_systems_101_150.json",
    "innovation_systems_151_200.json",
]

COLS = [
    "id", "name_ja", "name_en", "definition", "impact_summary",
    "subfield", "school_of_thought", "era_start", "era_end",
    "schumpeter_layer", "innovation_type", "cognitive_mechanism",
    "key_researchers", "key_works", "keywords_ja", "keywords_en",
    "opposing_concept_names",
]


def import_files():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    cur = conn.cursor()

    total = 0
    skipped = 0

    for fname in FILES:
        fpath = DATA_DIR / fname
        if not fpath.exists():
            print(f"File not found: {fpath}")
            continue

        with open(fpath) as f:
            records = json.load(f)

        for rec in records:
            # Convert list fields to comma-separated strings
            for field in ["key_researchers", "key_works"]:
                if field in rec and isinstance(rec[field], list):
                    rec[field] = "; ".join(rec[field])

            # Check if already exists
            existing = cur.execute(
                "SELECT id FROM innovation_theory WHERE id = ?", (rec["id"],)
            ).fetchone()
            if existing:
                skipped += 1
                continue

            # Build insert
            cols_present = [c for c in COLS if c in rec]
            placeholders = ", ".join("?" for _ in cols_present)
            col_str = ", ".join(cols_present)
            values = [rec[c] for c in cols_present]

            cur.execute(
                f"INSERT INTO innovation_theory ({col_str}) VALUES ({placeholders})",
                values,
            )
            total += 1

        print(f"  {fname}: processed {len(records)} records")

    conn.commit()
    conn.close()
    print(f"\n完了: {total}件インポート, {skipped}件スキップ（既存）")


if __name__ == "__main__":
    import_files()
