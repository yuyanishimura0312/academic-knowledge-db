import sqlite3

DB = "lit.sqlite"
SUBFIELD_ID = 22
LIMIT = 80

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}


def pick_tags(name, definition):
    text = f"{name} {definition}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis in AXES and axis not in [t[0] for t in tags] and len(tags) < 2:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["ナラトロジー", "物語", "語り", "プロット", "焦点化", "ディエゲーシス", "ファブラ", "キャラクター", "出来事", "幻想"]):
        add("物語", "rethinking", "語りの構造分析はAI要約と物語生成で再編される", "AI物語生成")
    if any(k in text for k in ["読者", "受容", "読書", "期待の地平", "モデル読者", "読者反応", "交渉", "効用"]):
        add("受容", "rethinking", "読者反応と解釈共同体は推薦AIで再構成される", "推薦AI")
    if any(k in text for k in ["主体", "アイデンティティ", "女性", "黒人", "植民地", "ディアスポラ", "クィア", "フェミニ", "精神分析", "意識", "身体", "情動"]):
        add("主体", "rethinking", "主体位置と表象の条件がAI人格生成で揺らぐ", "AI人格生成")
    if any(k in text for k in ["正典", "アンソロジー", "標準", "教科書", "制度", "文学史", "価値", "世界文学", "代表", "批評史"]):
        add("正典", "partial", "批評的正典の選別がAI検索と推薦で更新される", "AI推薦")
    if any(k in text for k in ["作家", "作者", "著者", "女性作家", "共著", "伝記", "エクリチュール", "詩人"]):
        add("作者性", "partial", "作者の位置と声がAI共著で再定義される", "AI共著")
    if any(k in text for k in ["言語", "記号論", "意味", "エクリチュール", "テクスト", "ディスクール", "翻訳", "多言語"]):
        add("言語", "rethinking", "記号と文体の差異が大規模言語モデルで操作対象化する", "LLM")
    if any(k in text for k in ["翻訳", "文化翻訳", "植民地的差異", "媒介", "世界", "越境"]):
        add("翻訳", "rethinking", "翻訳と文化媒介の非対称性がAI翻訳で見えにくくなる", "AI翻訳")
    if any(k in text for k in ["真正", "本物", "物質", "印刷", "書物", "アーカイヴ", "証言", "トラウマ", "当事者"]):
        add("真正性", "rethinking", "証言や物質性の真正性が生成AIで争点化する", "生成AI")
    if any(k in text for k in ["想像力", "美学", "形式", "フォルマリズム", "創造", "詩学", "実験", "デジタル", "進化", "環境"]):
        add("創造性", "partial", "文学形式の生成手続きがAI模倣で検証される", "文体生成")

    if not tags:
        add("言語", "rethinking", "批評概念の言語化がLLMで再利用される", "LLM")
    if len(tags) == 1:
        fallback = "物語" if tags[0][0] != "物語" else "受容"
        add(fallback, "partial", "文学理論の操作概念がAI読解で部分的に変容する", "AI読解")
    return tags[:2]


def main():
    con = sqlite3.connect(DB, timeout=30)
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
