from lit_db_helper import LitDB


SUBFIELD = "lit_digital_ai"
REGION = "理論"
PERIOD_ID = 197


CONCEPTS = [
    # 会話ログと可読性
    ("温度ログ注釈詩", "temperature履歴を詩行注として読む生成詩実践。", "temperature log poetry"),
    ("再生成差分読解", "同一プロンプトの複数出力差分から文体揺れを読む方法。", "regeneration diff reading"),
    ("停止シーケンス句読法", "stop sequenceが物語の切断や沈黙を作る句読技法。", "stop sequence punctuation"),
    ("トークン予算韻律", "文脈長制限が反復や省略の韻律を生む現象。", "token budget prosody"),
    ("安全拒否エピローグ", "拒否応答を作品末尾の制度的声として読む概念。", "safety refusal epilogue"),
    ("会話ロール叙述法", "system/user/assistantロール差を語りの階層に転用する技法。", "chat role narration"),
    # RAGと記憶
    ("検索ヒット脚注詩学", "RAGの取得断片を脚注的権威として配置する詩学。", "retrieval-hit footnote poetics"),
    ("コンテキスト腐敗物語", "長い会話で初期設定が摩耗し物語が変質する現象。", "context decay narrative"),
    ("ベクトル近傍隠喩", "埋め込み空間の近傍性を隠喩生成の根拠にする技法。", "vector-neighbor metaphor"),
    ("リランキング正典論", "検索再順位付けが参照される正典を作る仕組み。", "reranking canon theory"),
    ("メモリピン作者性", "固定メモリ項目が継続作品の作者声を縛る現象。", "memory-pin authorship"),
    ("引用スニペット叙事", "断片引用の継ぎ接ぎで進むRAG型物語形式。", "citation snippet narrative"),
    # マルチモーダル生成
    ("altテキスト逆エクフラシス", "画像代替テキストから視覚詩を再生成する実践。", "alt-text reverse ekphrasis"),
    ("OCR信頼度韻律", "文字認識の信頼度数値を詩の強弱に読む方法。", "OCR confidence prosody"),
    ("字幕タイミング物語論", "字幕の開始・終了時刻を語りの間として分析する概念。", "subtitle timing narratology"),
    ("画像プロンプト余白論", "生成画像の未指定領域を読者的余白として扱う視点。", "image prompt margin theory"),
    ("声質クローン叙述者", "合成声の声質再現が語り手の同一性を担う現象。", "voice-clone narrator"),
    ("フレーム補間抒情", "動画補間の中間フレームに抒情的曖昧さを読む概念。", "frame interpolation lyricism"),
    # プラットフォーム微形式
    ("Discordスレッド章法", "Discordスレッド分岐を章立てとして用いる連載技法。", "Discord thread chaptering"),
    ("AO3タグ順序詩学", "AO3タグの並び順が読解期待を作る仕組み。", "AO3 tag order poetics"),
    ("Substack追記連載", "メール配信後の追記更新を連載時間として読む形式。", "Substack addendum seriality"),
    ("Notionデータベース小説", "Notion DBの行・プロパティで人物や事件を記述する小説。", "Notion database fiction"),
    ("TikTok字幕掌編", "自動字幕と短尺動画で成立する超短編物語形式。", "TikTok caption microfiction"),
    ("Gitコミット叙事詩", "コミット履歴を改稿過程ではなく物語本体として読む形式。", "Git commit epic"),
    # 低資源・文字体系
    ("ルビ埋め込みRAG", "ルビ情報を検索単位に含め日本語古典読解を補助する方法。", "ruby-aware RAG"),
    ("異体字正規化批評", "異体字統合が失わせる文献差異を批評対象にする概念。", "variant-normalization critique"),
    ("方言ASR小説化", "方言音声認識の誤変換を利用した口承小説化。", "dialect ASR fiction"),
    ("低資源MT自己注釈", "低資源翻訳モデルの誤訳を作品内注釈に転用する技法。", "low-resource MT self-annotation"),
    ("縦書きレイアウト幻覚", "縦書きOCRやLLMが段組を誤読し生成する虚構構造。", "vertical layout hallucination"),
    ("混在文字プロンプト詩", "複数文字体系の混在がモデル応答を揺らす詩作法。", "mixed-script prompt poetry"),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        for name_ja, definition, name_en in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=PERIOD_ID,
                definition=definition,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="minor",
            )
    print(f"inserted_or_seen={len(CONCEPTS)}")


if __name__ == "__main__":
    main()
