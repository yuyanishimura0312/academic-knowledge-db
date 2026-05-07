import sqlite3

DB = "lit.sqlite"
SUBFIELD_ID = 20
LIMIT = 80

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}


def pick_tags(name, definition):
    text = f"{name} {definition}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis in AXES and axis not in [t[0] for t in tags] and len(tags) < 2:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["多言語", "Spanglish", "クレオール", "華語", "イディッシュ", "日本語", "英語", "フランス語", "スペイン語", "言語"]):
        add("言語", "rethinking", "混成語の声と文体がAI翻訳で平準化されやすい", "AI翻訳")
    if any(k in text for k in ["翻訳", "媒介", "文化翻訳", "西洋読者", "世界30言語"]):
        add("翻訳", "rethinking", "文化媒介の権力差がAI翻訳で見えにくくなる", "AI翻訳")
    if any(k in text for k in ["主体", "アイデンティティ", "意識", "第二世代", "移民", "難民", "亡命", "帰属", "境界"]):
        add("主体", "rethinking", "離散主体の揺れがAI人格生成で再配置される", "AI人格")
    if any(k in text for k in ["真正性", "ステレオタイプ", "批判", "オリエンタリズム", "市場", "西洋"]):
        add("真正性", "rethinking", "当事者性と表象の真正性が生成AIで争点化する", "生成AI")
    if any(k in text for k in ["サーガ", "ナラティブ", "回想", "一人称", "独白", "語り", "物語", "記憶", "トラウマ", "家族史"]):
        add("物語", "rethinking", "記憶継承の語りがAI再構成で変質しうる", "記憶生成")
    if any(k in text for k in ["作家", "作者", "作家性", "批評家", "詩人", "語り手"]):
        add("作者性", "partial", "越境作家の位置取りがAI共著で曖昧になる", "AI共著")
    if any(k in text for k in ["代表", "制度", "受賞", "賞", "規範", "中心", "標準", "制度的", "ノーベル", "ブッカー", "全米図書賞", "ピューリツァー"]):
        add("正典", "partial", "周縁文学の正典化がAI推薦で再編される", "推薦AI")
    if any(k in text for k in ["読者", "承認", "可視化", "受容", "成功", "映像化", "BBC", "Apple TV"]):
        add("受容", "partial", "越境作品の流通と読者像がAI推薦で変わる", "推薦AI")
    if any(k in text for k in ["美学", "詩学", "形式", "実験", "融合", "断片", "メタフィクション", "書き換え", "再書き"]):
        add("創造性", "rethinking", "混成的形式の生成手続きがAI模倣で問われる", "文体生成")

    if not tags:
        add("主体", "rethinking", "離散経験の主体化がAI表象で再検討される", "生成AI")
    if len(tags) == 1:
        if tags[0][0] != "物語":
            add("物語", "rethinking", "移動と記憶の構成がAI要約で再配列される", "AI要約")
        else:
            add("主体", "rethinking", "語りの主体位置がAI人格生成で揺らぐ", "AI人格")
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
