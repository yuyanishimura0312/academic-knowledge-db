#!/usr/bin/env python3
import sqlite3

DB = "lit.sqlite"

VALID_AXES = ("作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語")


def choose_tags(name, definition):
    text = f"{name} {definition or ''}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis not in [t[0] for t in tags]:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["写本", "断片", "版", "伝来", "校訂", "年代記", "伝記", "解題", "口承", "多変種"]):
        add("真正性", "rethinking", "写本伝承・版差・口承変異は、AI生成テキストの来歴判定と真正性評価を再考させる。", "生成AIによる文体模倣、来歴不明テキスト、デジタル校訂")
    if any(k in text for k in ["翻訳", "翻案", "受容", "影響", "範例", "由来", "系譜", "原典", "範例", "範型"]):
        add("受容", "partial", "中世作品の翻案・受容連鎖は、AI時代の再利用と変形的生成を考える比較軸になる。", "生成AIによる翻案、リミックス、スタイル転移")
    if any(k in text for k in ["語", "俗語", "方言", "ラテン語", "古英語", "中英語", "古フランス語", "古ノルド", "中高ドイツ語", "カスティーリャ", "ガリシア"]):
        add("言語", "rethinking", "ラテン語・俗語・地域語の選択は、多言語AIが文学的権威と表現をどう媒介するかに関わる。", "機械翻訳、多言語生成、低資源言語モデル")
    if any(k in text for k in ["物語", "ロマン", "サガ", "叙事詩", "劇", "寓話", "夢", "聖杯", "アーサー", "トリスタン", "聖人伝", "説話"]):
        add("物語", "rethinking", "物語型・ジャンル規則・反復モチーフは、AIによる物語生成の構造的資源として再考される。", "LLM物語生成、プロット生成、ジャンル模倣")
    if any(k in text for k in ["詩人", "作者", "著した", "執筆", "編纂", "監修", "作", "無名", "口述", "書記"]):
        add("作者性", "rethinking", "単独作者・共同編纂・匿名性・口述筆記の揺れは、AI共著時代の作者概念に直結する。", "AI共著、匿名生成、プロンプトによる制作")
    if any(k in text for k in ["詩学", "形式", "韻律", "頭韻", "脚韻", "セスティーナ", "ジャンル", "創始", "発明", "技巧"]):
        add("創造性", "partial", "定型・技巧・ジャンル発明は、規則に基づく生成と創造性の関係を検討させる。", "制約付き生成、形式模倣、創作支援AI")
    if any(k in text for k in ["自伝", "独白", "女性", "恋愛", "主体", "夢想者", "主人公", "発話", "神秘"]):
        add("主体", "rethinking", "語り手・恋愛主体・神秘的経験主体は、AIが生成する声と人格の扱いを問い直す。", "AIペルソナ、合成話者、一人称生成")
    if any(k in text for k in ["最大", "代表", "重要", "集大成", "決定版", "正典", "古典", "頂点", "中心"]):
        add("正典", "partial", "代表作・集大成としての位置づけは、AI検索・推薦が正典を再配列する問題に関わる。", "AI検索、推薦アルゴリズム、教育用生成AI")
    if any(k in text for k in ["奇蹟", "聖母", "聖人", "神学", "解釈", "寓意", "教化", "道徳", "宗教"]):
        add("受容", "partial", "宗教的読解と教化の制度は、AIが解釈共同体や受容実践を変える論点になる。", "自動注釈、AIチューター、解釈支援")

    if not tags:
        add("物語", "partial", "中世文学概念として、ジャンル・伝承・語りの形式がAI生成文化との比較対象になる。", "生成AIによるジャンル模倣")
    if len(tags) == 1:
        fallback = "言語" if tags[0][0] != "言語" else "受容"
        add(fallback, "partial", "中世テキストの媒体・伝承・読解環境は、AI時代の再媒介と比較できる。", "デジタル人文学、機械翻訳、生成AI注釈")

    return tags[:2]


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    rows = cur.execute(
        """
        SELECT c.id, c.name_ja, c.definition
        FROM concepts c
        LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
        WHERE c.subfield_id = 2 AND ftt.id IS NULL
        GROUP BY c.id
        ORDER BY c.id
        """
    ).fetchall()

    inserted = 0
    for concept_id, name, definition in rows:
        for axis, status, rationale, phenomenon in choose_tags(name, definition):
            cur.execute(
                """
                INSERT OR IGNORE INTO fourth_transform_tags
                    (concept_id, axis, status, rationale, related_ai_phenomenon)
                VALUES (?, ?, ?, ?, ?)
                """,
                (concept_id, axis, status, rationale, phenomenon),
            )
            inserted += cur.rowcount

    con.commit()
    remaining = cur.execute(
        """
        SELECT COUNT(*)
        FROM concepts c
        LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
        WHERE c.subfield_id = 2 AND ftt.id IS NULL
        """
    ).fetchone()[0]
    con.close()
    print(f"inserted={inserted} concepts_processed={len(rows)} remaining={remaining}")


if __name__ == "__main__":
    main()
