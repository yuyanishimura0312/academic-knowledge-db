#!/usr/bin/env python3
"""Phase 9-B: 三項リンクテーブルの自動populate。

Strategy: For each concept that has both (a) a poetics_text_concept_link
and (b) a concept_original_source, create a triple linking them.
This builds the canonical triangle: theory-text → original passage → poetic example.
"""
import sqlite3
import uuid
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Find concepts that have both a quote and at least one linked text
    cur.execute("""
        SELECT DISTINCT cos.concept_id, cos.id AS source_id, cos.source_work_title,
               cos.source_author, cos.source_locator
        FROM concept_original_source cos
    """)
    quoted_concepts = {r[0]: (r[1], r[2], r[3], r[4]) for r in cur.fetchall()}
    print(f"Concepts with quotes: {len(quoted_concepts)}")

    cur.execute("""
        SELECT concept_id, text_id, link_type, discussion_locus
        FROM poetics_text_concept_link
    """)
    text_links = cur.fetchall()
    print(f"Text-concept links: {len(text_links)}")

    inserted = 0
    skipped_no_quote = 0
    seen_triples = set()
    cur.execute("SELECT concept_id, text_id, source_id FROM concept_text_source_triple")
    for r in cur.fetchall():
        seen_triples.add((r[0], r[1], r[2]))

    for concept_id, text_id, link_type, discussion_locus in text_links:
        if concept_id not in quoted_concepts:
            skipped_no_quote += 1
            continue
        source_id, work, author, locator = quoted_concepts[concept_id]
        key = (concept_id, text_id, source_id)
        if key in seen_triples:
            continue
        seen_triples.add(key)
        triple_type = "theory_example" if link_type in ("例証", "分析対象") else "critique_example" if link_type == "批判対象" else "transmission"
        rel_note = f"{author or ''}の『{work or ''}』{locator or ''}における当概念の founding 言明と、本テクストの間に link_type='{link_type}' の関係。"
        if discussion_locus:
            rel_note += f" 議論箇所: {discussion_locus}"
        cur.execute("""INSERT INTO concept_text_source_triple
            (id, concept_id, text_id, source_id, triple_type, relationship_note,
             confidence, discussion_locator)
            VALUES (?,?,?,?,?,?,?,?)""",
            (str(uuid.uuid4()), concept_id, text_id, source_id,
             triple_type, rel_note, 7, discussion_locus or locator))
        inserted += 1

    conn.commit()

    print(f"\n=== Triple population results ===")
    print(f"Triples inserted: {inserted}")
    print(f"Text links skipped (concept has no quote): {skipped_no_quote}")

    cur.execute("SELECT COUNT(*) FROM concept_text_source_triple")
    print(f"Total triples: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(DISTINCT concept_id) FROM concept_text_source_triple")
    print(f"Distinct concepts in triples: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(DISTINCT text_id) FROM concept_text_source_triple")
    print(f"Distinct texts in triples: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(DISTINCT source_id) FROM concept_text_source_triple")
    print(f"Distinct sources in triples: {cur.fetchone()[0]}")

    cur.execute("SELECT triple_type, COUNT(*) FROM concept_text_source_triple GROUP BY triple_type")
    print("\nBy triple_type:")
    for t, n in cur.fetchall():
        print(f"  {t}: {n}")

    cur.execute("""SELECT hc.name_ja, COUNT(*) FROM concept_text_source_triple ctst
                    JOIN humanities_concept hc ON ctst.concept_id = hc.id
                    GROUP BY hc.name_ja ORDER BY 2 DESC LIMIT 10""")
    print("\nTop concepts by triples:")
    for n, c in cur.fetchall():
        print(f"  {n}: {c}")

    conn.close()


if __name__ == "__main__":
    main()
