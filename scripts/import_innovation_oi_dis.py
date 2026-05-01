#!/usr/bin/env python3
"""
Import disruptive_innovation_dynamics and open_innovation_ecosystems subfield
JSON data into innovation_theory table.
Usage: python3 scripts/import_innovation_oi_dis.py
"""

import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
DATA_DIR = Path(__file__).parent.parent / "collected" / "innovation"

FILES = [
    "inno_dis_001_050.json",
    "inno_dis_051_100.json",
    "inno_dis_101_150.json",
    "inno_dis_151_200.json",
    "inno_open_001_050.json",
    "inno_open_051_100.json",
    "inno_open_101_150.json",
    "inno_open_151_200.json",
]

COLS = [
    "id", "name_ja", "name_en", "definition", "impact_summary",
    "subfield", "category", "era_start", "era_end",
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

        file_count = 0
        for rec in records:
            # Convert list fields to JSON string (store as JSON array text)
            for field in ["key_researchers", "key_works"]:
                if field in rec and isinstance(rec[field], list):
                    rec[field] = json.dumps(rec[field], ensure_ascii=False)

            # Check if already exists
            existing = cur.execute(
                "SELECT id FROM innovation_theory WHERE id = ?", (rec["id"],)
            ).fetchone()
            if existing:
                skipped += 1
                continue

            # Build insert using only columns present in the record
            cols_present = [c for c in COLS if c in rec]
            placeholders = ", ".join("?" for _ in cols_present)
            col_str = ", ".join(cols_present)
            values = [rec[c] for c in cols_present]

            cur.execute(
                f"INSERT INTO innovation_theory ({col_str}) VALUES ({placeholders})",
                values,
            )
            total += 1
            file_count += 1

        print(f"  {fname}: {file_count}件インポート")

    conn.commit()
    conn.close()
    print(f"\n完了: 合計{total}件インポート, {skipped}件スキップ（既存）")


if __name__ == "__main__":
    import_files()
