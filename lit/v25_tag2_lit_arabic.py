import sqlite3

DB = "lit.sqlite"
SUBFIELD_ID = 13
LIMIT = 80

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}


def pick_tags(name, definition):
    text = f"{name} {definition}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis in AXES and axis not in [t[0] for t in tags] and len(tags) < 2:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["ムアッラカ", "正典", "規範", "範例", "頂点", "代表作", "古典", "選集", "重要", "制度"]):
        add("正典", "partial", "古典的権威と選別基準がAI推薦で再配列される", "推薦AI")
    if any(k in text for k in ["語り", "物語", "叙事", "逸話", "伝記", "旅行記", "記録", "対話", "小説", "演劇", "来世訪問記"]):
        add("物語", "rethinking", "語りの配列と記憶化がAI要約で再構成される", "AI要約")
    if any(k in text for k in ["詩人", "作家", "文人", "著した", "著者", "批評家", "劇作家", "編纂者", "宮廷詩人"]):
        add("作者性", "partial", "詩人・文人の作家像がAI共著で揺らぐ", "AI共著")
    if any(k in text for k in ["修辞", "技巧", "形式", "詩作", "実験", "装飾", "韻律", "押韻", "描写", "融合", "自由詩"]):
        add("創造性", "rethinking", "定型と技巧の生成手続きがAI模倣で問われる", "文体生成")
    if any(k in text for k in ["口語", "アラビア語", "明晰", "語順", "文法", "語彙", "発音", "俗語", "方言", "フランス語", "多言語"]):
        add("言語", "rethinking", "文語・口語・翻訳語の差異がAIで平準化されやすい", "AI翻訳")
    if any(k in text for k in ["翻訳", "翻案", "西欧", "ヨーロッパ", "フランス語", "世界文学", "比較", "植民地", "マグレブ"]):
        add("翻訳", "rethinking", "越境受容の媒介性がAI翻訳で不可視化される", "AI翻訳")
    if any(k in text for k in ["読まれ", "流通", "上演", "出版", "雑誌", "市場", "受賞", "ベストセラー", "大衆", "読者"]):
        add("受容", "partial", "流通と読者形成がAI推薦で変化する", "推薦AI")
    if any(k in text for k in ["主体", "アイデンティティ", "女性", "部族", "名誉", "亡命", "離散", "植民地", "パレスチナ", "自己", "自賛"]):
        add("主体", "rethinking", "集団・個人の主体位置がAI表象で再検討される", "AI人格")
    if any(k in text for k in ["伝承", "伝承上", "写本", "異本", "真正", "原型", "起源", "祖型", "改悛", "口承"]):
        add("真正性", "rethinking", "伝承・写本・起源の真正性が生成AIで争点化する", "生成AI")

    if not tags:
        add("正典", "partial", "文学史上の位置づけがAI検索で再編される", "検索AI")
    if len(tags) == 1:
        if tags[0][0] != "創造性":
            add("創造性", "rethinking", "形式的特徴がAI文体生成で再演される", "文体生成")
        else:
            add("受容", "partial", "作品評価と流通がAI推薦で変化する", "推薦AI")
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
