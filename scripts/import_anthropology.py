"""
人類学概念DB (anthropology-concepts) から humanities_concept テーブルへ
500概念をインポートするスクリプト。

- anthropology-concepts/data/anthropology.db の concepts テーブルから取得
- survey_frame に実際のsubfield値に対応するL3ノードを自動追加
- 文化人類学のsurvey_frame domain を humanities_concept に設定
"""

import sqlite3, os, uuid

ACADEMIC_DB = os.path.expanduser("~/projects/research/academic-knowledge-db/academic.db")
ANTHRO_DB = os.path.expanduser("~/projects/research/anthropology-concepts/data/anthropology.db")

COMMON_COLS = [
    "id", "name_ja", "name_en", "name_original", "definition",
    "impact_summary", "subfield", "school_of_thought",
    "era_start", "era_end", "methodology_level", "target_domain",
    "application_conditions", "when_to_apply", "framing_questions",
    "opposing_concept_names", "keywords_ja", "keywords_en",
    "status", "source_reliability", "data_completeness",
    "created_at", "updated_at"
]

# Map subfield values to L2 parent names
SUBFIELD_TO_L2 = {
    "文化人類学": "象徴人類学", "医療人類学": "医療人類学",
    "経済人類学": "経済人類学", "政治人類学": "政治人類学",
    "心理人類学": "象徴人類学", "都市人類学": "政治人類学",
    "移民研究": "政治人類学", "方法論": "象徴人類学",
    "ジェンダー人類学": "政治人類学", "応用人類学": "経済人類学",
    "環境人類学": "経済人類学", "宗教人類学": "宗教人類学",
    "歴史人類学": "象徴人類学", "教育人類学": "象徴人類学",
    "言語人類学": "象徴人類学", "STS": "感覚・物質文化研究",
    "社会人類学": "象徴人類学", "ポストコロニアル研究": "政治人類学",
    "親族研究": "象徴人類学", "開発人類学": "経済人類学",
    "法人類学": "政治人類学", "食の人類学": "感覚・物質文化研究",
    "デジタル人類学": "感覚・物質文化研究", "未来の人類学": "象徴人類学",
    "科学技術社会論（STS）": "感覚・物質文化研究",
    "フェミニスト人類学": "政治人類学", "認知人類学": "象徴人類学",
    "先住民研究": "政治人類学", "時間の人類学": "象徴人類学",
    "物質文化研究": "感覚・物質文化研究", "考古学/人類学": "象徴人類学",
    "視覚人類学": "感覚・物質文化研究", "記憶の人類学": "象徴人類学",
    "インフラの人類学": "感覚・物質文化研究", "グローバル化研究": "政治人類学",
    "メディア人類学": "感覚・物質文化研究", "公共人類学": "経済人類学",
    "技術の人類学": "感覚・物質文化研究", "理論": "象徴人類学",
    "生態学的人類学": "経済人類学", "アフリカ哲学": "象徴人類学",
    "ジェンダー研究": "政治人類学",
    # English subfields
    "economic_anthropology": "経済人類学", "environmental_anthropology": "経済人類学",
    "political_anthropology": "政治人類学", "anthropology_of_religion": "宗教人類学",
    "cultural_anthropology": "象徴人類学", "digital_anthropology": "感覚・物質文化研究",
    "methodology": "象徴人類学", "social_anthropology": "象徴人類学",
    "legal_anthropology": "政治人類学", "kinship_studies": "象徴人類学",
    "symbolic_anthropology": "象徴人類学", "microsociology": "象徴人類学",
    "cognitive_anthropology": "象徴人類学", "anthropology_of_body": "感覚・物質文化研究",
    "ecological_anthropology": "経済人類学", "multispecies_studies": "経済人類学",
    "political_economy": "経済人類学", "political_philosophy": "政治人類学",
    "psychological_anthropology": "象徴人類学", "ritual_studies": "象徴人類学",
    "social_theory": "象徴人類学", "sociology": "象徴人類学",
    "sociology_of_religion": "宗教人類学", "systems_theory": "象徴人類学",
}


def main():
    if not os.path.exists(ANTHRO_DB):
        print(f"Error: {ANTHRO_DB} not found")
        return

    src = sqlite3.connect(ANTHRO_DB)
    dst = sqlite3.connect(ACADEMIC_DB)
    cur = dst.cursor()

    # 1. Import concepts
    cols_str = ", ".join(COMMON_COLS)
    placeholders = ", ".join(["?"] * len(COMMON_COLS))
    rows = src.execute(f"SELECT {cols_str} FROM concepts").fetchall()

    existing = cur.execute("SELECT COUNT(*) FROM humanities_concept").fetchone()[0]
    if existing > 0:
        print(f"humanities_concept already has {existing} records. Skipping import.")
    else:
        inserted = 0
        for row in rows:
            try:
                cur.execute(f"INSERT INTO humanities_concept ({cols_str}) VALUES ({placeholders})", row)
                inserted += 1
            except Exception as e:
                print(f"  Skip {row[0]}: {e}")
        print(f"Imported {inserted} concepts")

    # 2. Ensure L3 subfield nodes exist in survey_frame
    subs = cur.execute("""
        SELECT subfield, COUNT(*) FROM humanities_concept
        WHERE subfield IS NOT NULL AND subfield != ''
        GROUP BY subfield
    """).fetchall()

    existing_l3 = set(r[0] for r in cur.execute(
        "SELECT name FROM survey_frame WHERE domain='humanities_concept' AND level=3"
    ).fetchall())

    # Build L2 lookup
    l2_map = {}
    for r in cur.execute("""
        SELECT sf2.id, sf2.name FROM survey_frame sf2
        WHERE sf2.domain='humanities_concept' AND sf2.level=2
    """).fetchall():
        l2_map[r[1]] = r[0]

    added = 0
    for sub, count in subs:
        if sub in existing_l3:
            continue
        l2_name = SUBFIELD_TO_L2.get(sub)
        if not l2_name:
            continue
        parent_id = l2_map.get(l2_name)
        if not parent_id:
            continue
        uid = str(uuid.uuid4())
        cur.execute("""INSERT INTO survey_frame (id, domain, level, parent_id, name, name_en, survey_priority)
                       VALUES (?, 'humanities_concept', 3, ?, ?, ?, 2)""",
                    (uid, parent_id, sub, sub))
        added += 1

    dst.commit()
    total = cur.execute("SELECT COUNT(*) FROM humanities_concept").fetchone()[0]
    matched = cur.execute("""
        SELECT COUNT(*) FROM humanities_concept h
        WHERE EXISTS (SELECT 1 FROM survey_frame sf WHERE sf.name = h.subfield
                      AND sf.domain='humanities_concept' AND sf.level=3)
    """).fetchone()[0]
    print(f"Total: {total}, Matched to L3: {matched}, New L3s added: {added}")

    src.close()
    dst.close()


if __name__ == "__main__":
    main()
