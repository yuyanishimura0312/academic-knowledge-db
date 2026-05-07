#!/usr/bin/env python3
import sqlite3

DB = "lit.sqlite"
SUBFIELD_ID = 23

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}
STATUSES = {"rethinking", "partial", "invariant"}


def pick_tags(name, definition):
    text = f"{name} {definition}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis not in AXES or status not in STATUSES:
            raise ValueError((axis, status))
        if axis not in [tag[0] for tag in tags] and len(tags) < 2:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["機械翻訳", "NMT", "Transformer", "Attention", "LLM", "AI", "Meta", "BERTScore", "METEOR", "chrF", "IBM", "ポストエディット", "MTPE"]):
        add("翻訳", "rethinking", "自動翻訳と評価指標が翻訳判断を人間の実践からモデル運用へ拡張する", "機械翻訳・LLM翻訳")
        add("言語", "rethinking", "言語差が埋め込み・注意機構・自動評価の対象として再記述される", "多言語モデル")
    elif any(k in text for k in ["翻訳", "訳", "通訳", "等価", "逐語", "意訳", "重訳", "自己訳", "対訳", "不可", "ローカリ"]):
        add("翻訳", "rethinking", "等価性・媒介・編集介入がAI翻訳時代に再評価される", "AI翻訳・ポストエディット")
        add("真正性", "partial", "原典への忠実性と訳者の介入範囲が生成補助で曖昧になる", "AI訳文検証")
    if any(k in text for k in ["世界文学", "比較文学", "正典", "古典", "制度", "市場", "出版社", "賞", "流通", "中心", "周辺", "世界システム"]):
        add("正典", "partial", "翻訳・推薦・データ化が世界文学の代表性と可視性を再編する", "AI推薦・翻訳市場分析")
        add("受容", "partial", "読者接触と国際流通が検索・推薦・翻訳基盤で媒介される", "プラットフォーム流通")
    if any(k in text for k in ["植民", "ポストコロニアル", "帝国", "権力", "検閲", "抵抗", "活動家", "紛争", "亡命", "政治"]):
        add("主体", "rethinking", "翻訳者・通訳者が中立的媒介ではなく政治的行為者として問われる", "AI媒介の責任主体")
        add("受容", "partial", "翻訳が権力関係と読者の解釈枠を作る過程が可視化される", "AIによる言説拡散")
    if any(k in text for k in ["フェミニスト", "ジェンダー", "女性", "身体", "感情", "倫理", "声", "翻訳者", "通訳者", "エージェント", "媒介者"]):
        add("主体", "rethinking", "訳者の声・身体・倫理的判断がAI支援で再配置される", "人間AI協働翻訳")
        add("作者性", "partial", "訳者の創造的寄与と責任表示が生成補助で再交渉される", "AI共訳")
    if any(k in text for k in ["詩", "韻", "文体", "語根", "方言", "訛り", "代名詞", "語彙", "文法", "言語", "語", "多言語", "低リソース"]):
        add("言語", "rethinking", "語彙・韻律・方言差がモデル処理で平準化または強調される", "多言語LLM・低リソース翻訳")
        add("創造性", "partial", "文体的補償や翻案が生成支援で新しい選択肢を持つ", "AI文体変換")
    if any(k in text for k in ["物語", "小説", "叙事", "民話", "聖人伝", "外典", "年代記", "ロマンス", "歌詞", "SF", "児童文学"]):
        add("物語", "partial", "物語形式が翻訳・要約・再生成を通じて別の読解単位に変わる", "生成AI要約・翻案")
    if any(k in text for k in ["ボルヘス", "カニバル", "翻案", "書き換え", "rewrite", "操作", "交渉", "創造性"]):
        add("創造性", "rethinking", "翻訳を再創造や書き換えと見る議論が生成AIで先鋭化する", "生成AI翻案")
        add("作者性", "partial", "原作者・訳者・生成モデルの寄与境界が問い直される", "AI共著")

    if not tags:
        add("翻訳", "partial", "翻訳を通じた意味移動の条件がAI支援環境で変化する", "AI翻訳")
    if len(tags) == 1:
        if tags[0][0] != "言語":
            add("言語", "partial", "言語差と文体差が機械処理の単位として扱われる", "多言語LLM")
        else:
            add("受容", "partial", "検索・推薦・自動翻訳が読者への到達経路を変える", "AI推薦")
    return tags[:2]


def main():
    con = sqlite3.connect(DB)
    rows = con.execute(
        """
        SELECT c.id, c.name_ja, c.definition
        FROM concepts c
        LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
        WHERE c.subfield_id = ? AND ftt.id IS NULL
        ORDER BY c.id
        """,
        (SUBFIELD_ID,),
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
    remaining = con.execute(
        """
        SELECT COUNT(*)
        FROM concepts c
        LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
        WHERE c.subfield_id = ? AND ftt.id IS NULL
        """,
        (SUBFIELD_ID,),
    ).fetchone()[0]
    con.close()
    print(f"concepts={len(rows)} inserted={inserted} remaining={remaining}")


if __name__ == "__main__":
    main()
