#!/usr/bin/env python3
"""Remove duplicate name_en entries within each domain table.
Keep the entry with the most fields filled, longer definition."""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

DB = Path(__file__).parent.parent / "academic.db"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--commit", action="store_true")
    args = p.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    total_removed = 0
    for tbl in ("humanities_concept", "social_theory", "natural_discovery", "engineering_method", "arts_question"):
        # Find duplicates
        dups = conn.execute(f"""
            SELECT name_en, COUNT(*) c FROM {tbl}
            WHERE name_en IS NOT NULL AND TRIM(name_en) != ''
            GROUP BY name_en HAVING c > 1
        """).fetchall()
        removed = 0
        for d in dups:
            ne = d["name_en"]
            rows = conn.execute(f"""
                SELECT id, name_ja, definition, impact_summary, school_of_thought, era_start, keywords_en
                FROM {tbl} WHERE name_en = ?
                ORDER BY (LENGTH(COALESCE(definition,'')) + LENGTH(COALESCE(impact_summary,''))) DESC
            """, (ne,)).fetchall()
            keep = rows[0]
            for row in rows[1:]:
                if args.commit:
                    conn.execute(f"DELETE FROM {tbl} WHERE id = ?", (row["id"],))
                removed += 1
        print(f"[{tbl}] dup groups={len(dups)} removed={removed}")
        total_removed += removed

    if args.commit:
        conn.commit()
    conn.close()
    print(f"\nTotal removed: {total_removed} ({'COMMITTED' if args.commit else 'DRY-RUN'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
