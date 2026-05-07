import sqlite3

DB = "lit.sqlite"
SUBFIELD_ID = 6
LIMIT = 80

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}


def pick_tags(name, definition):
    text = f"{name} {definition}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis in AXES and axis not in [t[0] for t in tags] and len(tags) < 2:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["内的独白", "自由間接話法", "意識", "主体", "個人", "疎外", "不安", "芸術家", "独白", "声"]):
        add("主体", "rethinking", "近代的主体の内面化がAI人格生成で再配置される", "AI人格生成")
    if any(k in text for k in ["語り", "物語", "小説", "短編", "長編", "挿話", "サーガ", "神話", "歴史", "記憶", "時間", "トラウマ", "エピファニー"]):
        add("物語", "rethinking", "断片的語りや時間構成がAI要約で平準化されうる", "AI要約")
    if any(k in text for k in ["文体", "統辞", "言語", "語", "新造語", "自由詩", "多言語", "引用", "自動記述", "句法", "翻訳"]):
        add("言語", "rethinking", "文体実験の言語的抵抗が生成AIで模倣・平準化される", "文体生成")
    if any(k in text for k in ["翻訳", "亡命", "欧州", "英語", "仏語", "独語", "ロシア", "イタリア", "スペイン", "アメリカ"]):
        add("翻訳", "partial", "越境的受容がAI翻訳で加速し文脈差が薄れる", "AI翻訳")
    if any(k in text for k in ["運動", "宣言", "前衛", "美学", "詩学", "形式", "技法", "方法", "モンタージュ", "断片", "実験", "構成"]):
        add("創造性", "rethinking", "前衛的形式発明が生成AIの様式模倣で再考される", "生成AI")
    if any(k in text for k in ["作者", "作家", "詩人", "ジョイス", "プルースト", "カフカ", "ウルフ", "マン", "フォークナー", "リルケ", "イェイツ"]):
        add("作者性", "partial", "強い作家様式がAI共著とスタイル模倣で揺らぐ", "AI共著")
    if any(k in text for k in ["正典", "代表", "中心", "賞", "受賞", "体系化", "確立", "範型", "古典", "聖書", "ホメロス"]):
        add("正典", "partial", "モダニズム正典の選別がAI推薦で再編される", "推薦AI")
    if any(k in text for k in ["雑誌", "流通", "読者", "受容", "出版", "市場", "見世物", "機関誌"]):
        add("受容", "partial", "前衛作品の流通と読者形成がAI推薦で変化する", "推薦AI")
    if any(k in text for k in ["真正", "自伝", "当事者", "民俗", "神秘", "無意識", "自動筆記"]):
        add("真正性", "rethinking", "経験や霊感の真正性が合成生成で争点化する", "合成テキスト")

    if not tags:
        add("創造性", "rethinking", "モダニズム的実験が生成AIの様式生成で再考される", "生成AI")
    if len(tags) == 1:
        if tags[0][0] != "物語":
            add("物語", "rethinking", "形式と主題の構成がAI要約で再配列される", "AI要約")
        else:
            add("言語", "partial", "語りの言語的細部がAI変換で失われやすい", "AI翻訳")
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
