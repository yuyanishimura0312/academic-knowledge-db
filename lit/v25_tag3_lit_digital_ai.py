import sqlite3

DB = "lit.sqlite"
SUBFIELD_ID = 24
LIMIT = 80

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}


def pick_tags(name, definition):
    text = f"{name} {definition}"
    tags = []

    def add(axis, status, rationale, phenomenon):
        if axis in AXES and axis not in [t[0] for t in tags] and len(tags) < 2:
            tags.append((axis, status, rationale, phenomenon))

    if any(k in text for k in ["ChatGPT", "GPT", "LLM", "AI", "生成", "機械協働", "計算論的創造性", "Writesonic", "Rytr", "Sudowrite", "NovelAI"]):
        add("作者性", "rethinking", "生成モデルが執筆主体と責任表示を再編する", "生成AI・AI共著")
        add("創造性", "rethinking", "創作手続きが人間固有の発想から計算的生成へ拡張される", "AI創作支援")
    if any(k in text for k in ["訴訟", "著作権", "規制", "GDPR", "EU AI法", "倫理", "データ", "無断学習", "透明性", "水印", "検出"]):
        add("真正性", "rethinking", "出所・同意・真正性の判断がAI訓練と生成で争点化する", "AI著作権・透明性規制")
        add("作者性", "rethinking", "権利帰属と責任主体が生成AI利用で曖昧になる", "AI訓練データ")
    if any(k in text for k in ["ナラティブ", "物語", "フィクション", "ゲーム", "IF", "Twine", "Inkle", "Storyspace", "分岐", "RAG", "Sora", "Runway", "ポッドキャスト", "Audio"]):
        add("物語", "rethinking", "物語の分岐・検索・映像化がAIで動的に再構成される", "生成ナラティブ")
    if any(k in text for k in ["キャラクター", "Replika", "Character.AI", "Inworld", "コンパニオン", "親密性", "主体", "会話"]):
        add("主体", "rethinking", "人物像や語りの主体がAIエージェントとして振る舞う", "AIキャラクター")
    if any(k in text for k in ["翻訳", "多言語", "言語", "Arabic", "韓国語", "中国語", "日本語", "Indic", "Bharat", "Aya", "Jais", "Qwen", "HyperCLOVA"]):
        add("言語", "rethinking", "低リソース言語や文体差が言語モデルで処理対象化される", "多言語LLM")
        add("翻訳", "partial", "AI翻訳が文学的等価性と媒介の条件を変える", "AI翻訳")
    if any(k in text for k in ["NER", "OCR", "GIS", "Wikidata", "IIIF", "Mirador", "HathiTrust", "文化分析", "計算論的精読", "書簡ネットワーク", "タグセット", "Stylo"]):
        add("言語", "partial", "文学テキストが機械可読な特徴量として再記述される", "デジタルヒューマニティーズ")
        add("受容", "partial", "検索・可視化・推薦が研究と読解の入口を変える", "計算的受容分析")
    if any(k in text for k in ["オープンアクセス", "クリエイティブ・コモンズ", "MOOC", "ビューア", "コミュニティ", "Wikidata", "プラットフォーム"]):
        add("受容", "partial", "流通基盤と学習環境が読者・研究者の接触面を変える", "プラットフォーム化")
    if any(k in text for k in ["正典", "代表", "標準", "世界標準", "基盤", "コーパス", "研究利用基盤"]):
        add("正典", "partial", "データ化された標準基盤が参照範囲と評価軸を再編する", "AI検索・推薦")
    if any(k in text for k in ["コード", "アスキー", "グリッチ", "Oulipo", "詩", "生成テクスト", "拡散モデル"]):
        add("創造性", "rethinking", "制約・コード・ノイズの詩学が生成技術で再実装される", "コード生成・生成詩")
        add("言語", "partial", "文字・コード・モデル出力の境界が文学的素材になる", "コードワーク")

    if not tags:
        add("物語", "partial", "デジタル環境で文学形式と読解経路が変化する", "デジタル文学")
    if len(tags) == 1:
        if tags[0][0] != "受容":
            add("受容", "partial", "AI検索・推薦・配信が作品との接触を媒介する", "AI推薦")
        else:
            add("正典", "partial", "デジタル基盤が参照される作品群を再編する", "デジタルアーカイブ")
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
