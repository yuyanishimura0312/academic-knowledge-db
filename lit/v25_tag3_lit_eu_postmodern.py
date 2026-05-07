import sqlite3

DB = "lit.sqlite"
SUBFIELD_ID = 7
LIMIT = 80

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}


def pick_tags(name, definition):
    text = f"{name} {definition}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis in AXES and axis not in [t[0] for t in tags] and len(tags) < 2:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["メタフィクション", "自己言及", "作者", "作家", "著者", "自伝", "オートフィクション", "本人", "実名"]):
        add("作者性", "rethinking", "作者・語り手・生成主体の境界がAI共著で再編される", "AI共著")
    if any(k in text for k in ["形式", "技法", "実験", "パスティーシュ", "パロディ", "断片", "ハイブリッド", "コード", "タイポグラフィ", "文体"]):
        add("創造性", "rethinking", "引用・模倣・形式実験の創造性がAI文体生成で問い直される", "文体生成")
    if any(k in text for k in ["物語", "小説", "語り", "語り手", "入れ子", "フレーム", "時間構造", "連作", "ナラティブ", "フィクション"]):
        add("物語", "rethinking", "非線形・多層的な語りがAI要約と生成で再構成される", "AI要約")
    if any(k in text for k in ["主体", "自己", "意識", "家族", "女性", "人種", "移民", "喪失", "記憶", "ポストヒューマニズム"]):
        add("主体", "rethinking", "自己・身体・集団の主体位置がAI表象で揺らぐ", "AI人格")
    if any(k in text for k in ["正典", "規範", "代表", "到達点", "ピューリッツァー", "ブッカー", "ベストセラー", "文学史", "古典"]):
        add("正典", "partial", "評価と文学史的位置づけがAI推薦で再配列される", "推薦AI")
    if any(k in text for k in ["読者", "受容", "出版", "市場", "大衆", "流通", "上演", "SNS", "メディア", "ベストセラー"]):
        add("受容", "partial", "読者形成と流通経路がAI推薦で変化する", "推薦AI")
    if any(k in text for k in ["翻訳", "多言語", "英語", "フランス語", "ドイツ語", "イタリア", "世界文学", "越境", "移民"]):
        add("翻訳", "partial", "越境的読解の媒介性がAI翻訳で変化する", "AI翻訳")
    if any(k in text for k in ["歴史的事実", "事実", "伝記", "写真", "記録", "文書", "発見", "実在", "真正", "記憶"]):
        add("真正性", "rethinking", "記録・事実・虚構の境界が生成AIで争点化する", "生成AI")
    if any(k in text for k in ["言語", "記号論", "修辞", "脚注", "引用", "文体", "方言", "コード", "無句読点", "声"]):
        add("言語", "rethinking", "言語差・文体・記号操作がLLM生成で平準化される", "LLM")

    if not tags:
        add("物語", "partial", "ポストモダン以後の語りの単位がAI生成で再検討される", "生成AI")
    if len(tags) == 1:
        if tags[0][0] != "受容":
            add("受容", "partial", "作品評価と読者接続がAI推薦で変化する", "推薦AI")
        else:
            add("創造性", "rethinking", "形式的特徴がAI文体生成で再演される", "文体生成")
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
