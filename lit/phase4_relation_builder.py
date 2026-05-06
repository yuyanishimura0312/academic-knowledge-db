"""
LIT-DB Phase 4 Relation Builder

Runs after Phase 2 collection + Phase 3 verification. Performs:
1. Cross-subfield relation enrichment (Phase 2 limited relations to within-subfield)
2. Genealogy link extraction (geneal_links between ancestor/descendant concepts)
3. Fourth-transformation tag completion (suggest missing axes for under-tagged concepts)
4. Cross-domain link expansion (PT/PHIL/AN/MG/Era-Talents bridging)
5. Bidirectional relation verification

Usage:
    python phase4_relation_builder.py --suggest-cross-subfield
    python phase4_relation_builder.py --suggest-genealogy
    python phase4_relation_builder.py --suggest-tags
    python phase4_relation_builder.py --report
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

DB_PATH = Path(__file__).parent / "lit.sqlite"


# Heuristic dictionaries for cross-subfield concept suggestion.
# These mappings reflect known intellectual genealogies — to be expanded
# as Phase 2 collection completes.
CROSS_SUBFIELD_KEYWORDS = {
    # mimesis (Greek) ↔ 神思 (Chinese) ↔ imitatio (Latin/Renaissance) ↔ Romantic originality
    "creativity_genealogy": [
        ("mimesis", "西欧", "古典古代"),
        ("imitatio", "西欧", "ルネサンス"),
        ("神思", "東アジア", "中国古典"),
        ("originality", "西欧", "ロマン主義"),
        ("machine creativity", "理論", "デジタル・AI"),
    ],
    # narrative theory cross-pollination
    "narrative_genealogy": [
        ("epic", "西欧", "古典古代"),
        ("monogatari", "東アジア", "日本古典"),
        ("章回小説", "東アジア", "中国古典"),
        ("maqama", "南西アジア", "アラブ"),
        ("Songline", "周縁横断", "先住民"),
    ],
    # 作者性 across regions
    "authorship_genealogy": [
        ("oral tradition", "西欧", "古典古代"),
        ("古詩十九首", "東アジア", "中国古典"),
        ("私小説", "東アジア", "日本近現代"),
        ("AI co-authorship", "理論", "デジタル・AI"),
    ],
}


def open_db() -> sqlite3.Connection:
    if not DB_PATH.exists():
        print(f"DB not found: {DB_PATH}", file=sys.stderr)
        sys.exit(1)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def find_concepts_by_keyword(conn: sqlite3.Connection, keyword: str) -> list:
    cur = conn.cursor()
    pat = f"%{keyword}%"
    cur.execute(
        """SELECT id, name_ja, name_en, name_original, region, subfield_id
           FROM concepts
           WHERE name_ja LIKE ? OR name_en LIKE ? OR name_original LIKE ?""",
        (pat, pat, pat),
    )
    return [dict(r) for r in cur.fetchall()]


def suggest_cross_subfield_relations(conn: sqlite3.Connection, dry_run: bool = True) -> list[dict]:
    """For each genealogy cluster, find existing concepts and propose relations between them."""
    suggestions = []
    for cluster_name, anchors in CROSS_SUBFIELD_KEYWORDS.items():
        found = []
        for keyword, expected_region, era in anchors:
            matches = find_concepts_by_keyword(conn, keyword)
            for m in matches:
                if m["region"] == expected_region or expected_region in (m["region"] or ""):
                    found.append({"keyword": keyword, "era": era, **m})
        # propose pairwise 'parallels' relations within the cluster
        for i, a in enumerate(found):
            for b in found[i + 1 :]:
                if a["subfield_id"] != b["subfield_id"]:
                    suggestions.append({
                        "cluster": cluster_name,
                        "source_id": a["id"],
                        "source_name": a["name_ja"],
                        "target_id": b["id"],
                        "target_name": b["name_ja"],
                        "relation_type": "parallels" if cluster_name.endswith("_genealogy") else "extends",
                    })
    if not dry_run:
        cur = conn.cursor()
        for s in suggestions:
            cur.execute(
                """INSERT INTO relations (source_type, source_id, target_type, target_id,
                                          relation_type, description, bidirectional, confidence)
                   VALUES ('concept', ?, 'concept', ?, ?, ?, 1, 4)""",
                (s["source_id"], s["target_id"], s["relation_type"],
                 f"cross-subfield genealogy cluster: {s['cluster']}"),
            )
        conn.commit()
    return suggestions


def suggest_genealogy_links(conn: sqlite3.Connection, dry_run: bool = True) -> list[dict]:
    """Look at concept descriptions for genealogical hints (extends, criticizes, follows)."""
    cur = conn.cursor()
    cur.execute(
        """SELECT id, name_ja, definition, development, background, subfield_id, region
           FROM concepts WHERE development IS NOT NULL OR background IS NOT NULL"""
    )
    suggestions = []
    rows = [dict(r) for r in cur.fetchall()]

    # naive keyword scan for ancestor mentions
    ancestor_markers = ["継承", "発展", "起源", "由来", "から派生", "を受けて", "を批判", "を踏まえ"]
    for r in rows:
        text = " ".join(filter(None, [r["development"], r["background"]]))
        for marker in ancestor_markers:
            if marker in text:
                suggestions.append({
                    "concept_id": r["id"],
                    "concept_name": r["name_ja"],
                    "marker": marker,
                    "context_snippet": text[:200],
                })
                break
    return suggestions


def suggest_tag_completion(conn: sqlite3.Connection) -> list[dict]:
    """Find concepts without fourth_transform_tags but whose subfield has high tag density."""
    cur = conn.cursor()
    cur.execute(
        """SELECT c.id, c.name_ja, c.subfield_id, s.name_ja AS sf_name
           FROM concepts c JOIN subfields s ON s.id = c.subfield_id
           LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
           WHERE ftt.id IS NULL"""
    )
    untagged = [dict(r) for r in cur.fetchall()]

    cur.execute(
        """SELECT s.id, s.name_ja,
                  COUNT(DISTINCT c.id) AS concepts_total,
                  COUNT(DISTINCT ftt.concept_id) AS concepts_tagged
           FROM subfields s
           LEFT JOIN concepts c ON c.subfield_id = s.id
           LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
           GROUP BY s.id"""
    )
    sf_density = {row["id"]: row for row in cur.fetchall()}

    suggestions = []
    for u in untagged:
        sf = sf_density.get(u["subfield_id"])
        if sf and sf["concepts_total"]:
            density = sf["concepts_tagged"] / sf["concepts_total"]
            if density >= 0.30 and density <= 0.60:
                suggestions.append({
                    "concept_id": u["id"],
                    "concept_name": u["name_ja"],
                    "subfield": u["sf_name"],
                    "current_density": density,
                    "rationale": f"領域内タグ密度{density:.0%}に対し未タグ。軸の見直し推奨。",
                })
    return suggestions


def report(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM concepts")
    cn = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM relations")
    rn = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM geneal_links")
    gn = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM cross_domain")
    cdn = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM fourth_transform_tags")
    tn = cur.fetchone()[0]
    cur.execute("SELECT COUNT(DISTINCT axis) FROM fourth_transform_tags")
    axes_used = cur.fetchone()[0]

    print(f"concepts:           {cn}")
    print(f"relations:          {rn}")
    print(f"geneal_links:       {gn}")
    print(f"cross_domain:       {cdn}")
    print(f"fourth_tx_tags:     {tn}")
    print(f"axes_used:          {axes_used}/9")
    print()

    cs = suggest_cross_subfield_relations(conn, dry_run=True)
    print(f"cross-subfield suggestions: {len(cs)}")
    for s in cs[:5]:
        print(f"  [{s['cluster']}] {s['source_name']} <-> {s['target_name']} ({s['relation_type']})")

    gs = suggest_genealogy_links(conn, dry_run=True)
    print(f"genealogy hints found in {len(gs)} concepts")

    ts = suggest_tag_completion(conn)
    print(f"tag completion candidates: {len(ts)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suggest-cross-subfield", action="store_true")
    ap.add_argument("--suggest-genealogy", action="store_true")
    ap.add_argument("--suggest-tags", action="store_true")
    ap.add_argument("--apply-cross-subfield", action="store_true",
                    help="actually insert proposed relations (use after review)")
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    conn = open_db()
    try:
        if args.suggest_cross_subfield:
            for s in suggest_cross_subfield_relations(conn, dry_run=True):
                print(s)
        elif args.apply_cross_subfield:
            n = len(suggest_cross_subfield_relations(conn, dry_run=False))
            print(f"applied {n} cross-subfield relations")
        elif args.suggest_genealogy:
            for s in suggest_genealogy_links(conn, dry_run=True):
                print(s)
        elif args.suggest_tags:
            for s in suggest_tag_completion(conn):
                print(s)
        else:
            report(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
