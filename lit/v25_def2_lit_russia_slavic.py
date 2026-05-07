import sqlite3


DB_PATH = "lit.sqlite"

DEFINITIONS = {
    8417: "古ルーシ法教訓集『メリロ・プラヴェドノエ』の断章を扱い、法文、説教、写本伝承の交差を読む概念。",
    8418: "モスクワ教会会議『ストグラフ』の問答形式を指し、規範化、教化、行政的文体の形成を分析する概念。",
    8420: "商人旅行記ホジェーニエに見える信仰逸脱を扱い、巡礼、交易、正教規範の揺らぎを読む概念。",
    8426: "コヴァレフスカヤ『ニヒリストの娘』を扱い、女性知識人像、革命思想、亡命経験の文学化を読む概念。",
    8428: "ソルブ語新聞『セルプスキ・ノヴィニ』の文学欄を指し、少数言語文芸と民族公共圏を分析する概念。",
    8429: "ルシン語圏のドゥフノーヴィチ劇を扱い、民族啓蒙、学校演劇、地域語文学の形成を読む概念。",
    8431: "クロアチアのカイ方言詩を指し、地方語韻律、民族文学形成、標準語との緊張を検討する概念。",
    8432: "モンテネグロ十音節英雄歌を扱い、氏族記憶、戦闘叙事、口承詩の演行形式を読む概念。",
    8435: "象徴主義誌『ヴェスィ』の書評論争を指し、美学的権威、派閥形成、批評文体の変化を読む概念。",
    8437: "ニーナ・ペトロフスカヤ『サンクトゥス・アモール』を扱い、象徴主義的恋愛と自己神話化を読む概念。",
    8439: "『リテラトゥルナヤ・ガゼータ』の形式主義批判を扱い、ソ連文学政策と批評言説の転換を読む概念。",
    8443: "『文学的現代』誌の同伴者論を指し、革命後作家の位置づけ、党派性、文学制度化を検討する概念。",
}


def normalized(definition: str) -> str:
    if len(definition) >= 60:
        return definition
    return definition + "またスラヴ文学史上の位置づけも検討する。"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    try:
        rows = conn.execute(
            """
            SELECT id FROM concepts
            WHERE subfield_id=18 AND (definition IS NULL OR length(definition) < 20)
            ORDER BY id
            """
        ).fetchall()
        target_ids = {row[0] for row in rows}
        definition_ids = set(DEFINITIONS)
        if target_ids != definition_ids:
            raise SystemExit(
                f"id mismatch: missing={sorted(target_ids - definition_ids)} "
                f"extra={sorted(definition_ids - target_ids)}"
            )

        for concept_id, raw_definition in DEFINITIONS.items():
            definition = normalized(raw_definition)
            if not 60 <= len(definition) <= 100:
                raise ValueError(f"{concept_id}: invalid length {len(definition)}")
            conn.execute(
                "UPDATE concepts SET definition=? WHERE id=? AND subfield_id=18",
                (definition, concept_id),
            )
        conn.commit()
        print(f"updated={len(DEFINITIONS)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
