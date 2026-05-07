#!/usr/bin/env python3
"""Auto-link poetics concepts to texts using rule-based heuristics.

Creates poetics_text_concept_link entries based on:
- form_genre matching concept name (e.g. "ソネット" → ソネット概念)
- culture_region/era matching subfield (e.g. 古代ギリシャ → 古典詩学)
- author surname matching researcher → linked concepts
- specific known canonical pairings (Aristotle ↔ Greek tragedy etc.)

Conservative: only adds links the heuristics are confident about.
"""

import sqlite3
import uuid
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"


# Form/genre → concept name patterns (substring matches in name_ja)
FORM_TO_CONCEPT_PATTERNS = {
    "ソネット": ["ソネット"],
    "テルツァ・リーマ": ["三行", "テルツァ"],
    "ガザル": ["ガザル"],
    "カスィーダ": ["カスィーダ"],
    "ハイク": ["俳"],
    "俳諧": ["俳"],
    "和歌": ["和歌"],
    "短歌": ["短歌", "和歌"],
    "長歌": ["長歌", "万葉"],
    "悲歌": ["エレジー", "悲歌"],
    "頌歌": ["頌歌", "オード"],
    "叙事詩": ["叙事詩"],
    "教訓詩": ["教訓"],
    "バラード": ["バラード"],
    "悲劇合唱歌": ["カタルシス", "悲劇"],
    "ルバーイー": ["ルバーイー", "四行"],
    "マスナヴィー": ["マスナヴィー"],
    "ハカ": ["口承詩"],
    "時調": ["時調"],
    "詞": ["詞"],
}

# Culture region → relevant subfield keywords
REGION_SUBFIELD = {
    "古代ギリシャ・ローマ": "古典詩学",
    "中世ヨーロッパ": "中世・ルネサンス詩学",
    "近代ヨーロッパ": None,  # too broad
    "中国古典": "比較詩学",
    "日本古典": "比較詩学",
    "東アジア": "比較詩学",
    "サンスクリット": "比較詩学",
    "アラビア・ペルシア": "比較詩学",
    "仏典詩偈": "比較詩学",
}


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Load concepts indexed by name_ja
    cur.execute("SELECT id, name_ja, subfield FROM humanities_concept WHERE subfield IN ('古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム','近代美学・詩学','現象学的詩学','中世・ルネサンス詩学','ポスト構造主義詩学','受容理論','認知詩学','比較詩学','デジタル詩学')")
    concepts = cur.fetchall()
    by_name = {n: (cid, sf) for cid, n, sf in concepts}

    # Existing links to avoid duplicates
    cur.execute("SELECT text_id, concept_id FROM poetics_text_concept_link")
    existing = {(t, c) for t, c in cur.fetchall()}

    # Load texts
    cur.execute("""SELECT id, title_ja, author_name_display, form_genre, culture_region,
                    era_year, era_period, length_lines FROM poetics_text""")
    texts = cur.fetchall()

    new_links = []

    def add_link(text_id, concept_id, link_type, locus=None, strength=5):
        if (text_id, concept_id) in existing:
            return
        existing.add((text_id, concept_id))
        new_links.append((text_id, concept_id, link_type, locus, strength))

    for tid, title, author, form, region, year, era, lines in texts:
        # 1. Form-based linking
        if form:
            for form_kw, name_patterns in FORM_TO_CONCEPT_PATTERNS.items():
                if form_kw in form:
                    for pattern in name_patterns:
                        for cname, (cid, sf) in by_name.items():
                            if pattern in cname:
                                add_link(tid, cid, "例証", locus=f"form={form}")

        # 2. Region-based subfield linking (use 比較詩学 specific subfield-rooted concepts)
        if region in REGION_SUBFIELD and REGION_SUBFIELD[region]:
            sf = REGION_SUBFIELD[region]
            sf_concepts = [(cn, ci) for cn, (ci, csf) in by_name.items() if csf == sf]
            # Limit to one or two best matches per text — pick the comparative-poetics broad ones
            for cname, cid in sf_concepts:
                # Match by region keyword in concept name
                if region == "中国古典" and "唐詩" in cname:
                    add_link(tid, cid, "分析対象", locus="region=中国古典")
                elif region == "アラビア・ペルシア" and ("ガザル" in cname or "ペルシア" in cname or "アラビア" in cname):
                    add_link(tid, cid, "分析対象", locus="region=アラビア・ペルシア")
                elif region == "サンスクリット" and ("サンスクリット" in cname or "ヴェーダ" in cname or "ラサ" in cname):
                    add_link(tid, cid, "分析対象", locus="region=サンスクリット")
                elif region == "日本古典" and ("和歌" in cname or "俳諧" in cname or "幽玄" in cname or "もののあはれ" in cname):
                    add_link(tid, cid, "分析対象", locus="region=日本古典")

        # 3. Specific author-based pairings (well-known canonical analyses)
        a = (author or "").lower()
        # Aristotle Poetics analyzed Greek tragedy
        if region == "古代ギリシャ・ローマ" and form and ("悲劇" in form or "tragedy" in form.lower()):
            for cn in ["カタルシス（浄化）", "ミメーシス（模倣）", "叙事詩と悲劇の比較"]:
                if cn in by_name:
                    cid, _ = by_name[cn]
                    add_link(tid, cid, "分析対象", locus="Aristotle Poetics")
        # Longinus On Sublime - Sappho fr.31, Pindar
        if "sappho" in a or "pindar" in a or "homer" in a:
            for cn in ["ヒュプソス（崇高）", "崇高の五源泉", "崇高の大いなる精神"]:
                if cn in by_name:
                    cid, _ = by_name[cn]
                    add_link(tid, cid, "例証", locus="Longinus On the Sublime")
        # Shklovsky → Russian Formalism: any Russian poet
        if region == "近代ヨーロッパ" and ("pushkin" in a or "lermontov" in a or "mayakov" in a):
            for cn in ["異化", "詩的言語", "詩的言語の革命"]:
                if cn in by_name:
                    cid, _ = by_name[cn]
                    add_link(tid, cid, "分析対象", locus="Russian Formalism analyses")
        # Symbolism - Baudelaire, Rimbaud, Verlaine, Mallarmé
        if any(x in a for x in ["baudelaire", "rimbaud", "verlaine", "mallarm"]):
            for cn in ["メタファー（隠喩）", "詩的言語"]:
                if cn in by_name:
                    cid, _ = by_name[cn]
                    add_link(tid, cid, "例証", locus="Symbolist canon")

    # Insert
    for text_id, concept_id, link_type, locus, strength in new_links:
        cur.execute("""INSERT INTO poetics_text_concept_link
            (id, text_id, concept_id, link_type, discussion_locus, strength)
            VALUES (?,?,?,?,?,?)""",
            (str(uuid.uuid4()), text_id, concept_id, link_type, locus, strength))

    conn.commit()
    print(f"Auto-linked: {len(new_links)} new text↔concept links")

    cur.execute("""SELECT hc.name_ja, COUNT(*) AS n FROM poetics_text_concept_link l
                  JOIN humanities_concept hc ON hc.id = l.concept_id
                  GROUP BY hc.name_ja ORDER BY n DESC LIMIT 15""")
    print("\nTop concepts now linked to texts:")
    for n, c in cur.fetchall():
        print(f"  {n}: {c}")

    cur.execute("SELECT COUNT(*) FROM poetics_text_concept_link")
    print(f"\nTotal concept_links: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(DISTINCT concept_id) FROM poetics_text_concept_link")
    print(f"Distinct concepts linked: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(DISTINCT text_id) FROM poetics_text_concept_link")
    print(f"Distinct texts linked: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
