import sqlite3

DB = "lit.sqlite"
SUBFIELD_ID = 17
LIMIT = 80

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}


def pick_tags(name, definition):
    text = f"{name} {definition}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis in AXES and axis not in [t[0] for t in tags] and len(tags) < 2:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["郷札", "漢字", "ハングル", "漢文", "字喃", "チュノム", "タガログ語", "英語", "中国語", "マレー語", "タミル語", "多言語", "国文", "母語", "固有語"]):
        add("言語", "rethinking", "固有表記や多言語性がAI翻訳で平準化されやすい", "AI翻訳")
    if any(k in text for k in ["翻案", "翻訳", "翻訳した", "ラーマーヤナ", "漢喃", "スペイン語", "英訳", "世界"]):
        add("翻訳", "rethinking", "翻案と媒介の層がAI翻訳で見えにくくなる", "AI翻訳")
    if any(k in text for k in ["叙事詩", "小説", "説話", "物語", "神話", "夢", "伝", "伝奇", "口承", "年代記", "家族史", "三代", "非線形", "多重視点"]):
        add("物語", "rethinking", "語りの構造と伝承経路がAI要約で再配列される", "AI要約")
    if any(k in text for k in ["主体", "自我", "女性", "民衆", "移民", "難民", "亡命", "覚醒", "抵抗", "労働者", "植民地", "ディアスポラ"]):
        add("主体", "rethinking", "歴史的主体の位置取りがAI生成表象で争点化する", "AI人格")
    if any(k in text for k in ["正典", "代表", "最高峰", "教科", "最古", "体系化", "収録", "編纂", "アンソロジー", "国家賞", "UNESCO"]):
        add("正典", "partial", "地域文学の正典化がAI推薦と教材生成で再編される", "推薦AI")
    if any(k in text for k in ["詩人", "作家", "著した", "編んだ", "創刊", "文人", "僧", "女性作家", "政治家"]):
        add("作者性", "partial", "作家像と作品署名の意味がAI共著で揺らぐ", "AI共著")
    if any(k in text for k in ["詩形", "定型", "リズム", "韻文", "自由詩", "モダニズム", "マジック・リアリズム", "断章", "融合", "寓話", "実験"]):
        add("創造性", "rethinking", "形式的発明が生成AIの文体模倣で再評価される", "文体生成")
    if any(k in text for k in ["受容", "読者", "流通", "市場", "受賞", "映像", "翻訳出版", "国外", "教材"]):
        add("受容", "partial", "越境受容と読者形成がAI推薦で変化する", "推薦AI")
    if any(k in text for k in ["固有", "真正", "土着", "民族", "民謡", "国民", "当事者", "植民地以後"]):
        add("真正性", "rethinking", "民族的・土着的表象の真正性が生成AIで争点化する", "生成AI")

    if not tags:
        add("物語", "rethinking", "地域的記憶の語りがAI要約で変質しうる", "AI要約")
    if len(tags) == 1:
        if tags[0][0] != "主体":
            add("主体", "rethinking", "語り手と集団主体の位置がAI人格生成で揺らぐ", "AI人格")
        else:
            add("物語", "rethinking", "歴史経験の構成がAI要約で再配列される", "AI要約")
    return tags[:2]


def main():
    con = sqlite3.connect(DB)
    rows = con.execute(
        """
        SELECT c.id, c.name_ja, c.definition
        FROM concepts c
        LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
        WHERE c.subfield_id = ? AND ftt.id IS NULL
        LIMIT ?
        """,
        (SUBFIELD_ID, LIMIT),
    ).fetchall()

    before = con.total_changes
    for concept_id, name, definition in rows:
        for axis, status, rationale, phenomenon in pick_tags(name or "", definition or ""):
            con.execute(
                """
                INSERT OR IGNORE INTO fourth_transform_tags
                    (concept_id, axis, status, rationale, related_ai_phenomenon)
                VALUES (?, ?, ?, ?, ?)
                """,
                (concept_id, axis, status, rationale, phenomenon),
            )
    con.commit()
    inserted = con.total_changes - before
    con.close()
    print(f"inserted={inserted} concepts={len(rows)}")


if __name__ == "__main__":
    main()
