#!/usr/bin/env python3
import sqlite3

DB = "lit.sqlite"


def choose_tags(name, definition):
    text = f"{name} {definition or ''}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis not in [t[0] for t in tags]:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["翻訳", "ラテン語化", "翻案", "ギリシャ", "ギリシア", "ヘブライ語", "ローマ", "受け継", "継承"]):
        add("翻訳", "partial", "古典語間の移植と翻案は、AI翻訳が文体・権威・意味を再媒介する論点になる。", "機械翻訳、文体転写、多言語生成")
    if any(k in text for k in ["語", "文体", "韻律", "ヘクサメター", "エレゲイア", "イアンボス", "合唱", "ラテン語", "ギリシア語", "ヘブライ語", "修辞", "弁論", "文法"]):
        add("言語", "rethinking", "韻律・文体・修辞規範は、LLMが言語形式を模倣し変換する時代に再検討される。", "LLM文体模倣、韻律生成、修辞生成")
    if any(k in text for k in ["詩人", "作者", "著した", "執筆", "作", "編んだ", "編纂", "偽作", "伝わる", "ダビデ作"]):
        add("作者性", "rethinking", "作者名・帰属・偽作・編纂の揺れは、AI共著と生成物の帰属問題に接続する。", "AI共著、生成物の帰属、スタイル模倣")
    if any(k in text for k in ["物語", "小説", "叙事詩", "悲劇", "喜劇", "劇", "遍歴", "筋", "神話", "聖人伝", "福音書", "歴史叙述"]):
        add("物語", "rethinking", "筋・ジャンル・神話的型は、AIによる物語生成の構造的素材として再考される。", "プロット生成、ジャンル模倣、神話リライト")
    if any(k in text for k in ["主体", "主人公", "女性", "英雄", "預言者", "賢者", "イエス", "ヨブ", "アエネーアス", "恋愛", "嘆き", "好奇心"]):
        add("主体", "rethinking", "語り手・英雄・宗教的主体の構成は、AIペルソナと合成された声の問題を照らす。", "AIペルソナ、一人称生成、合成話者")
    if any(k in text for k in ["代表", "最古", "最大", "標準", "体系化", "完成", "確立", "頂点", "集大成", "古典", "正典", "根本"]):
        add("正典", "partial", "代表作・標準形式としての位置づけは、AI検索や推薦が正典配列を変える問題に関わる。", "AI検索、推薦アルゴリズム、教材生成")
    if any(k in text for k in ["断片", "パピルス", "現存", "完全", "伝わる", "再発見", "注解", "要約", "散逸", "唯一"]):
        add("真正性", "rethinking", "断片伝承・注解・散逸文献の証言は、生成テキストの来歴判定と真正性評価に関わる。", "来歴不明テキスト、AI補完、デジタル校訂")
    if any(k in text for k in ["影響", "受容", "後世", "ルネサンス", "中世", "範例", "祖型", "伝統", "教化", "教育"]):
        add("受容", "partial", "古典の再読・教育・後世受容は、AIによる注釈と再流通で変化する。", "自動注釈、AIチューター、リミックス生成")
    if any(k in text for k in ["詩学", "形式", "技法", "機知", "発明", "技巧", "構成", "比喩", "寓意"]):
        add("創造性", "partial", "形式技法とジャンル規則は、制約付き生成と創造性の関係を問う材料になる。", "制約付き生成、創作支援AI、形式模倣")

    if not tags:
        add("受容", "partial", "古典文学概念として、AI時代の読解・注釈・再利用の対象になる。", "AI注釈、生成AIによる再解釈")
    if len(tags) == 1:
        fallback = "物語" if tags[0][0] != "物語" else "言語"
        add(fallback, "partial", "ジャンルや表現形式の反復は、AI生成文化との比較軸になる。", "生成AIによるジャンル模倣")

    return tags[:2]


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    rows = cur.execute(
        """
        SELECT c.id, c.name_ja, c.definition
        FROM concepts c
        LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
        WHERE c.subfield_id = 1 AND ftt.id IS NULL
        GROUP BY c.id
        ORDER BY c.id
        LIMIT 100
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
        WHERE c.subfield_id = 1 AND ftt.id IS NULL
        """
    ).fetchone()[0]
    con.close()
    print(f"inserted={inserted} concepts_processed={len(rows)} remaining={remaining}")


if __name__ == "__main__":
    main()
