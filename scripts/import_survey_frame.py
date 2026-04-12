#!/usr/bin/env python3
"""Import survey frame JSON into the database."""

import sqlite3
import json
import uuid
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"


def import_survey_frame(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")

    domain = data.get("domain")
    frames = data.get("frames", [])

    # Build parent name -> id map
    name_to_id = {}
    imported = 0

    for item in frames:
        frame_id = str(uuid.uuid4())
        name = item.get("name", "")
        name_to_id[name] = frame_id

        parent_id = name_to_id.get(item.get("parent")) if item.get("parent") else None

        values = {
            "id": frame_id,
            "domain": domain,
            "level": item.get("level", 1),
            "parent_id": parent_id,
            "name": name,
            "name_en": item.get("name_en"),
            "description": item.get("description"),
            "estimated_unit_count": item.get("estimated_unit_count"),
            "survey_status": "not_started",
            "survey_priority": item.get("survey_priority", 3),
            "key_references": json.dumps(item.get("key_references", []), ensure_ascii=False),
        }

        cols = ", ".join(values.keys())
        placeholders = ", ".join(["?"] * len(values))
        conn.execute(
            f"INSERT OR REPLACE INTO survey_frame ({cols}) VALUES ({placeholders})",
            list(values.values())
        )
        imported += 1

    conn.commit()
    conn.close()
    print(f"Imported {imported} survey frame entries for domain: {domain}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python import_survey_frame.py <file.json>")
        sys.exit(1)
    import_survey_frame(sys.argv[1])
