import sqlite3

DB = "lit.sqlite"
SUBFIELD_ID = 20
LIMIT = 100

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}


def pick_tags(name, definition):
    text = f"{name} {definition}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis in AXES and axis not in [t[0] for t in tags] and len(tags) < 2:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["英語", "クレオール", "奴隷英語", "多言語", "母への手紙", "語", "言語", "Spanglish"]):
        add("言語", "rethinking", "離散の混成語・声・文体がAI翻訳やLLMで平準化されうる", "AI翻訳・多言語LLM")
    if any(k in text for k in ["翻訳", "媒介", "世界", "越境", "西洋", "接触", "グローバル"]):
        add("翻訳", "partial", "文化間媒介の非対称性がAI翻訳で不可視化されやすい", "AI翻訳")
    if any(k in text for k in ["移民", "難民", "亡命", "離散", "ディアスポラ", "養子", "第二世代", "混血", "帰属", "自己", "主体"]):
        add("主体", "rethinking", "帰属と移動で揺れる主体がAI人格生成で再表象される", "AI人格・生成AI")
    if any(k in text for k in ["語り", "物語", "回想", "記憶", "家族", "世代", "母娘", "三世代", "トラウマ", "歴史", "叙事詩"]):
        add("物語", "rethinking", "記憶継承と家族史の構成がAI要約・再生成で変質する", "AI要約・記憶生成")
    if any(k in text for k in ["作家", "詩人", "作者", "回想録", "自伝", "マニフェスト", "証言"]):
        add("作者性", "partial", "当事者作家の位置と証言性がAI共著で曖昧化する", "AI共著")
    if any(k in text for k in ["真正", "当事者", "表象", "批判", "オリエンタリズム", "ステレオタイプ", "逆転", "書き換え"]):
        add("真正性", "rethinking", "当事者性と表象の真正性が生成AIによる代替表象で問われる", "生成AI")
    if any(k in text for k in ["代表", "確立", "受賞", "賞", "ブッカー", "ピューリッツァー", "全米図書賞", "規範", "礎石", "画期作"]):
        add("正典", "partial", "周縁文学の正典化がAI検索・推薦で再配列される", "AI検索・推薦")
    if any(k in text for k in ["読者", "受容", "観光", "市場", "映像化", "承認", "可視化"]):
        add("受容", "partial", "越境作品の読者形成と流通がAI推薦に媒介される", "AI推薦")
    if any(k in text for k in ["実験", "形式", "メタフィクション", "幻想", "マジックリアリズム", "スペキュラティブ", "代替歴史", "詩学", "融合"]):
        add("創造性", "rethinking", "混成形式と歴史改変の創造性が生成AIの模倣可能性で再考される", "文体生成")

    if not tags:
        add("主体", "rethinking", "離散経験の主体化がAI表象で再検討される", "生成AI")
    if len(tags) == 1:
        if tags[0][0] != "物語":
            add("物語", "rethinking", "移動と記憶の語りがAI要約で再配列される", "AI要約")
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
