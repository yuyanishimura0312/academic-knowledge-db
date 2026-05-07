import sqlite3

DB = "lit.sqlite"
SUBFIELD_ID = 15
LIMIT = 80

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}


def pick_tags(name, definition):
    text = f"{name} {definition}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis in AXES and axis not in [t[0] for t in tags] and len(tags) < 2:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["口承", "民話", "物語", "叙事詩", "説話", "語り", "寓話", "回想", "記憶", "自伝", "日記", "三部作", "多視点"]):
        add("物語", "rethinking", "共同体記憶と語りの構造がAI要約や再生成で組み替えられる", "AI要約")
    if any(k in text for k in ["語", "英語", "仏語", "フランス語", "葡語", "アラビア語", "スワヒリ", "ハウサ", "ヨルバ", "ピジン", "翻訳", "多言語"]):
        add("言語", "rethinking", "植民地語と在地語の緊張がAI翻訳で平準化されやすい", "AI翻訳")
    if any(k in text for k in ["翻訳", "文学化", "採集", "媒介", "パリ", "世界", "越境"]):
        add("翻訳", "partial", "文化媒介と翻訳者の介入がAI翻訳で見えにくくなる", "AI翻訳")
    if any(k in text for k in ["作家", "詩人", "批評家", "思想家", "語り手", "女性長編小説作家", "ノーベル", "ブッカー"]):
        add("作者性", "partial", "作家の歴史的位置と声の固有性がAI共著で揺らぐ", "AI共著")
    if any(k in text for k in ["女性", "黒人", "アフリカ人", "主体", "アイデンティティ", "ネグリチュード", "フェミニズム", "差別", "亡命", "難民", "植民地", "独立", "アパルトヘイト"]):
        add("主体", "rethinking", "植民地後主体や当事者性の表象が生成AIで再配置される", "生成AI")
    if any(k in text for k in ["正典", "代表作", "最大の達成", "先駆", "初", "受賞", "賞", "発禁", "制度", "出版社", "批評誌"]):
        add("正典", "partial", "アフリカ文学の正典化と推薦経路がAI検索で再編される", "推薦AI")
    if any(k in text for k in ["読者", "市場", "大衆", "映画化", "BBC", "ドキュメンタリー", "観客", "受容", "発行"]):
        add("受容", "partial", "流通圏と読者形成がAI推薦や要約で変化する", "推薦AI")
    if any(k in text for k in ["美学", "詩学", "形式", "実験", "断片", "風刺", "諷刺", "脱構築", "グロテスク", "幻想", "SF", "スリラー"]):
        add("創造性", "rethinking", "形式的革新が生成モデルに模倣・再利用される", "文体生成")
    if any(k in text for k in ["真正", "本質", "固有", "伝統", "祖先", "トーテム", "氏族", "神", "霊性", "土着"]):
        add("真正性", "rethinking", "伝統や当事者性の真正性が合成表象で争点化する", "生成AI")

    if not tags:
        add("主体", "rethinking", "植民地後の主体位置が生成AI表象で再検討される", "生成AI")
    if len(tags) == 1:
        if tags[0][0] != "物語":
            add("物語", "rethinking", "歴史経験の語り方がAI要約で再配列される", "AI要約")
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
