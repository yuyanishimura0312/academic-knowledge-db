#!/usr/bin/env python3
"""Import Phase 2 poetics collection (4 subagent JSON files) into academic.db.

Handles:
- ID deduplication across files
- Skip if ID already exists in DB
- Originator -> humanities_concept_researchers link
- Relations only inserted if both endpoints exist
"""

import json
import sqlite3
import uuid
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "academic.db"
COLLECT_DIR = Path("/tmp/poetics_collect")
FILES = [
    "A_structuralist_formalism.json",
    "B_rhetoric_classical.json",
    "C_modern_phenomenology.json",
    "D_poststructuralist_cognitive_comparative.json",
]


def load_all():
    concepts, researchers, relations = {}, {}, []
    for fname in FILES:
        with (COLLECT_DIR / fname).open() as f:
            d = json.load(f)
        for c in d.get("concepts", []):
            cid = c["id"]
            if cid not in concepts:
                concepts[cid] = c
        for r in d.get("researchers", []):
            rid = r["id"]
            if rid not in researchers:
                researchers[rid] = r
        for rel in d.get("relations", []):
            relations.append(rel)
    return list(concepts.values()), list(researchers.values()), relations


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=OFF")
    cur = conn.cursor()

    concepts, researchers, relations = load_all()
    print(f"Loaded: {len(concepts)} concepts, {len(researchers)} researchers, {len(relations)} relations")

    # Existing IDs
    cur.execute("SELECT id FROM humanities_concept")
    existing_concept_ids = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT id FROM researchers")
    existing_researcher_ids = {r[0] for r in cur.fetchall()}

    # Insert researchers (normalize field names across agents)
    r_ins = r_skip = 0
    for r in researchers:
        if r["id"] in existing_researcher_ids:
            r_skip += 1
            continue
        name_full = r.get("name_full") or r.get("name_en") or r.get("name_ja") or r["id"]
        themes = r.get("research_themes") or ", ".join(filter(None, [r.get("main_school"), r.get("key_concepts")])) or None
        bio = r.get("biography_brief") or r.get("biography") or None
        cur.execute("""
            INSERT INTO researchers (id, name_full, name_ja, birth_year, death_year,
                nationality, primary_institution, research_themes, biography_brief)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, (
            r["id"], name_full, r.get("name_ja"),
            r.get("birth_year"), r.get("death_year"),
            r.get("nationality"), r.get("primary_institution"),
            themes, bio,
        ))
        existing_researcher_ids.add(r["id"])
        r_ins += 1
    print(f"Researchers: inserted {r_ins}, skipped (existed) {r_skip}")

    # Insert concepts
    c_ins = c_skip = 0
    for c in concepts:
        if c["id"] in existing_concept_ids:
            c_skip += 1
            continue
        cur.execute("""
            INSERT INTO humanities_concept (
                id, name_ja, name_en, name_original, definition, impact_summary,
                subfield, school_of_thought, era_start, era_end,
                methodology_level, keywords_ja, keywords_en,
                status, source_reliability, data_completeness)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            c["id"], c.get("name_ja"), c.get("name_en"), c.get("name_original"),
            c.get("definition"), c.get("impact_summary"),
            c.get("subfield"), c.get("school_of_thought"),
            c.get("era_start"), c.get("era_end"),
            c.get("methodology_level"),
            c.get("keywords_ja"), c.get("keywords_en"),
            c.get("status", "active"), c.get("source_reliability", "secondary"), 70,
        ))
        existing_concept_ids.add(c["id"])
        c_ins += 1

        # Originator link
        oid = c.get("originator_id")
        if oid and oid in existing_researcher_ids:
            try:
                cur.execute("""
                    INSERT OR IGNORE INTO humanities_concept_researchers
                        (concept_id, researcher_id, role, year_associated, note)
                    VALUES (?,?,?,?,?)
                """, (c["id"], oid, "originator", c.get("year_proposed"), c.get("founding_work")))
            except sqlite3.IntegrityError:
                pass
    print(f"Concepts: inserted {c_ins}, skipped (existed) {c_skip}")

    # Insert relations (only if both endpoints exist)
    rel_ins = rel_skip_missing = rel_skip_dup = 0
    seen_rel = set()
    for rel in relations:
        s, t = rel.get("source_id"), rel.get("target_id")
        rt = rel.get("relation_type", "related")
        if s not in existing_concept_ids or t not in existing_concept_ids:
            rel_skip_missing += 1
            continue
        key = (s, t, rt)
        if key in seen_rel:
            rel_skip_dup += 1
            continue
        seen_rel.add(key)
        rel_id = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO humanities_concept_relations
                (id, source_concept_id, target_concept_id, relation_type,
                 relation_description, strength, is_confirmed)
            VALUES (?,?,?,?,?,?,?)
        """, (
            rel_id, s, t, rt, rel.get("description"),
            rel.get("strength", 5), 1,
        ))
        rel_ins += 1
    print(f"Relations: inserted {rel_ins}, skipped(missing endpoint) {rel_skip_missing}, skipped(dup) {rel_skip_dup}")

    conn.commit()

    # Final stats
    cur.execute("""
        SELECT subfield, COUNT(*) FROM humanities_concept
        WHERE subfield IN ('古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム',
                          '近代美学・詩学','現象学的詩学','中世・ルネサンス詩学',
                          'ポスト構造主義詩学','受容理論','認知詩学','比較詩学','デジタル詩学')
        GROUP BY subfield ORDER BY COUNT(*) DESC
    """)
    print("\n=== Final poetics subfield counts in DB ===")
    total = 0
    for sf, n in cur.fetchall():
        print(f"  {sf}: {n}")
        total += n
    print(f"  TOTAL: {total}")

    cur.execute("""
        SELECT COUNT(DISTINCT r.id) FROM researchers r
        JOIN humanities_concept_researchers hcr ON r.id = hcr.researcher_id
        JOIN humanities_concept hc ON hc.id = hcr.concept_id
        WHERE hc.subfield IN ('古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム',
                          '近代美学・詩学','現象学的詩学','中世・ルネサンス詩学',
                          'ポスト構造主義詩学','受容理論','認知詩学','比較詩学','デジタル詩学')
    """)
    print(f"  Researchers linked: {cur.fetchone()[0]}")

    cur.execute("""
        SELECT COUNT(*) FROM humanities_concept_relations rel
        JOIN humanities_concept c1 ON rel.source_concept_id = c1.id
        JOIN humanities_concept c2 ON rel.target_concept_id = c2.id
        WHERE c1.subfield LIKE '%詩学%' OR c2.subfield LIKE '%詩学%'
           OR c1.subfield LIKE '%美学%' OR c2.subfield LIKE '%美学%'
           OR c1.subfield LIKE '%修辞%' OR c2.subfield LIKE '%修辞%'
           OR c1.subfield LIKE '%受容%' OR c2.subfield LIKE '%受容%'
           OR c1.subfield LIKE '%フォルマ%' OR c2.subfield LIKE '%フォルマ%'
    """)
    print(f"  Relations: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
