#!/usr/bin/env python3
import sqlite3

DB = "lit.sqlite"
SUBFIELD_ID = 5
LIMIT = 80

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}


def pick_tags(name, definition):
    text = f"{name} {definition}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis in AXES and axis not in [t[0] for t in tags] and len(tags) < 2:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["口語", "方言", "自由間接話法", "文体", "語り口", "民衆語り", "言葉", "言語"]):
        add("言語", "rethinking", "写実的文体と口語差異がAI生成文で平準化されうる", "文体生成")
    if any(k in text for k in ["翻訳", "英訳", "世界", "国民", "国際", "欧州", "受容"]):
        add("翻訳", "partial", "国民文学間の媒介がAI翻訳で再配置される", "AI翻訳")
    if any(k in text for k in ["一人称", "視点", "意識", "内面", "心理", "語り手", "回想", "枠物語", "複数の語り手"]):
        add("物語", "rethinking", "視点と内面の構成がAI要約や再生成で変質する", "AI要約")
    if any(k in text for k in ["女性", "青年", "娘", "母", "労働者", "農民", "移民", "主体", "覚醒", "成長", "孤立"]):
        add("主体", "rethinking", "階級・ジェンダー主体の表象がAI人格生成で問い直される", "AI人格")
    if any(k in text for k in ["代表", "規範", "頂点", "中心", "運動", "教説", "理論", "綱領", "体系化", "正典"]):
        add("正典", "partial", "文学史上の規範化がAI推薦と教材生成で再編される", "推薦AI")
    if any(k in text for k in ["読者", "批評", "論争", "成功", "受賞", "映像化", "出版", "連載", "雑誌"]):
        add("受容", "partial", "作品流通と評価の履歴がAI推薦で増幅・偏向される", "推薦AI")
    if any(k in text for k in ["作家", "作者", "書簡", "詩人", "批評家", "理論家", "門下", "師事"]):
        add("作者性", "partial", "作者の観察方法や文体責任がAI共著で曖昧になる", "AI共著")
    if any(k in text for k in ["実験", "形式", "方法", "観察", "自然主義", "リアリズム", "ヴェリズモ", "ノヴェレ", "短編"]):
        add("創造性", "rethinking", "観察にもとづく形式創造が生成AI模倣で再評価される", "生成AI")
    if any(k in text for k in ["写実", "リアリズム", "自然主義", "調査", "記録", "真正", "観察", "生活", "社会"]):
        add("真正性", "rethinking", "現実観察の真正性が合成テキストで検証困難になる", "合成データ")

    if not tags:
        add("物語", "rethinking", "社会経験を組織する語りがAI再構成で変質しうる", "AI要約")
    if len(tags) == 1:
        if tags[0][0] != "主体":
            add("主体", "rethinking", "個人と社会の関係がAI人格生成で再配置される", "AI人格")
        else:
            add("物語", "rethinking", "主体形成の物語構造がAI再生成で揺らぐ", "生成AI")
    return tags[:2]


def main():
    con = sqlite3.connect(DB, timeout=10)
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
