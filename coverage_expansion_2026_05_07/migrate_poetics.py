#!/usr/bin/env python3
"""Migrate '詩学・文学理論' from humanities_concept to arts_question/文学理論・物語論.

Steps:
  1. Insert into arts_question with subfield='文学理論・物語論' (new IDs)
  2. Move humanities_concept_relations referencing these to arts_question_relations
  3. Update cross_domain_relations references (source_domain='humanities_concept' → 'arts_question')
  4. Delete from humanities_concept
"""
from __future__ import annotations

import argparse
import sqlite3
import uuid
from pathlib import Path

DB = Path(__file__).parent.parent / "academic.db"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--commit", action="store_true")
    args = p.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Get all 詩学・文学理論 entries from humanities_concept
    rows = list(conn.execute("""
        SELECT * FROM humanities_concept
        WHERE subfield = '詩学・文学理論'
    """).fetchall())
    print(f"Source rows: {len(rows)}")

    # Check arts_question schema
    art_cols = [c[1] for c in conn.execute("PRAGMA table_info(arts_question)").fetchall()]
    hum_cols = [c[1] for c in conn.execute("PRAGMA table_info(humanities_concept)").fetchall()]
    common_cols = [c for c in art_cols if c in hum_cols]
    print(f"Common cols: {len(common_cols)}")

    # Build ID mapping for relation migration
    id_map = {}
    for r in rows:
        new_id = str(uuid.uuid4())
        id_map[r["id"]] = new_id

    # Prepare insert rows
    insert_rows = []
    for r in rows:
        vals = [id_map[r["id"]]]
        for c in common_cols[1:]:  # skip id
            v = r[c]
            if c == "subfield":
                v = "文学理論・物語論"
            insert_rows.append(v) if False else None
            vals.append(v)
        insert_rows.append(vals)

    cols_str = ",".join(common_cols)
    placeholders = ",".join("?" * len(common_cols))
    insert_sql = f"INSERT INTO arts_question ({cols_str}) VALUES ({placeholders})"

    # Get existing relations referencing these entries
    hum_rels_to_move = []
    for r in conn.execute("SELECT * FROM humanities_concept_relations WHERE source_concept_id IN (SELECT id FROM humanities_concept WHERE subfield = '詩学・文学理論') OR target_concept_id IN (SELECT id FROM humanities_concept WHERE subfield = '詩学・文学理論')"):
        # Only migrate if BOTH endpoints are being moved
        if r["source_concept_id"] in id_map and r["target_concept_id"] in id_map:
            hum_rels_to_move.append(r)
    print(f"Relations to migrate (both endpoints in poetics): {len(hum_rels_to_move)}")

    # Cross-domain relations
    cross_to_update = list(conn.execute("""
        SELECT * FROM cross_domain_relations
        WHERE (source_domain = 'humanities_concept' AND source_id IN (SELECT id FROM humanities_concept WHERE subfield = '詩学・文学理論'))
           OR (target_domain = 'humanities_concept' AND target_id IN (SELECT id FROM humanities_concept WHERE subfield = '詩学・文学理論'))
    """).fetchall())
    print(f"Cross-domain relations to update: {len(cross_to_update)}")

    if not args.commit:
        print("\nDRY-RUN. Use --commit to execute.")
        return 0

    # Execute migration
    print("\n[committing]")
    cur.executemany(insert_sql, insert_rows)
    print(f"  inserted into arts_question: {len(insert_rows)}")

    # Migrate relations: arts_question_relations
    arts_rels_inserts = []
    for r in hum_rels_to_move:
        arts_rels_inserts.append((
            str(uuid.uuid4()),
            id_map[r["source_concept_id"]],
            id_map[r["target_concept_id"]],
            r["relation_type"],
            r["relation_description"],
            r["strength"] if "strength" in r.keys() else 5,
        ))
    if arts_rels_inserts:
        cur.executemany(
            "INSERT INTO arts_question_relations (id, source_concept_id, target_concept_id, relation_type, relation_description, strength) VALUES (?,?,?,?,?,?)",
            arts_rels_inserts,
        )
    print(f"  inserted into arts_question_relations: {len(arts_rels_inserts)}")

    # Update cross_domain_relations
    cross_updates = 0
    for r in cross_to_update:
        new_src_id = id_map.get(r["source_id"], r["source_id"])
        new_tgt_id = id_map.get(r["target_id"], r["target_id"])
        new_src_dom = "arts_question" if r["source_domain"] == "humanities_concept" and r["source_id"] in id_map else r["source_domain"]
        new_tgt_dom = "arts_question" if r["target_domain"] == "humanities_concept" and r["target_id"] in id_map else r["target_domain"]
        cur.execute(
            "UPDATE cross_domain_relations SET source_id=?, source_domain=?, target_id=?, target_domain=? WHERE id=?",
            (new_src_id, new_src_dom, new_tgt_id, new_tgt_dom, r["id"]),
        )
        cross_updates += 1
    print(f"  updated cross_domain_relations: {cross_updates}")

    # Delete from humanities_concept (and orphan relations)
    cur.execute("DELETE FROM humanities_concept_relations WHERE source_concept_id IN (SELECT id FROM humanities_concept WHERE subfield = '詩学・文学理論') OR target_concept_id IN (SELECT id FROM humanities_concept WHERE subfield = '詩学・文学理論')")
    deleted_rels = cur.rowcount
    print(f"  deleted humanities_concept_relations: {deleted_rels}")
    cur.execute("DELETE FROM humanities_concept WHERE subfield = '詩学・文学理論'")
    deleted_concepts = cur.rowcount
    print(f"  deleted humanities_concept: {deleted_concepts}")

    conn.commit()
    conn.close()
    print("\nMigration complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
