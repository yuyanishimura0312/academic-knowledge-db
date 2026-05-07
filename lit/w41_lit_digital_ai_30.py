#!/usr/bin/env python3
"""Wave 41: 30 hyper-niche lit_digital_ai concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_digital_ai"
REGION = "理論"
PERIOD_ID = None

CONCEPTS = [
    # Cluster 1: regional minority e-lit practices
    ("フリウリ語Twine詩", "Friulian Twine poetry", "Friulian Twine poetry", "latin", "少数ロマンス語で分岐詩を作る電子文学実践。"),
    ("カレリア語IF復興", "Karelian IF revival", "Karelian IF revival", "latin", "危機言語の語彙復興を対話型物語で試す制作圏。"),
    ("サーミ語チャットボット叙事詩", "Sami chatbot epic", "Sami chatbot epic", "latin", "口承叙事の応答形式を会話AIで再演する試み。"),
    ("オック語ボット吟遊詩", "Occitan troubadour bot", "Occitan troubadour bot", "latin", "トルバドゥール詩型を自動生成する少数語ボット。"),
    ("ブルトン語電子カンティク", "Breton digital kantik", "Breton digital kantik", "latin", "ブルトン聖歌詩を画面上で再配列する電子詩形式。"),
    ("ラディーノ語WhatsApp小説", "Ladino WhatsApp novel", "Ladino WhatsApp novel", "latin", "セファルディ語の短文交換で進むチャット小説形式。"),
    # Cluster 2: forgotten network and screen-text forms
    ("Minitel連載小説", "Minitel serial fiction", "Minitel serial fiction", "latin", "仏ビデオテックス網で分割配信された画面小説。"),
    ("Ceefaxテレテキスト詩", "Ceefax teletext poetry", "Ceefax teletext poetry", "latin", "英国文字放送の低解像度画面を詩面にする形式。"),
    ("Prestel電子詩", "Prestel electronic poem", "Prestel electronic poem", "latin", "初期ビデオテックス端末向けに組まれた画面詩。"),
    ("BBSリレー俳句ログ", "BBS relay haiku log", "BBS relay haiku log", "latin", "掲示板投稿の連鎖を連句的に読むログ文学。"),
    ("HyperCard方言民話スタック", "HyperCard dialect folktale stack", "HyperCard dialect folktale stack", "latin", "方言民話をカード遷移で読む初期マルチメディア作品。"),
    ("PalmPilot掌編小説", "PalmPilot flash fiction", "PalmPilot flash fiction", "latin", "PDAの小画面制約で書かれた超短編デジタル小説。"),
    # Cluster 3: manuscript, OCR, and HTR edge cases
    ("Fraktur長s誤読詩学", "Fraktur long-s OCR poetics", "Fraktur long-s OCR poetics", "latin", "長いsの誤認が韻や語義を崩すOCR読解論。"),
    ("ナスタアリークHTR行分割", "Nastaliq HTR line segmentation", "Nastaliq HTR line segmentation", "latin", "斜行ペルシア文字の自動行認識が詩句を乱す問題。"),
    ("縦書きルビ埋め込み", "vertical ruby embedding", "vertical ruby embedding", "latin", "縦書き注音が埋め込み検索で本文化する現象。"),
    ("変体仮名HTRコーパス", "hentaigana HTR corpus", "hentaigana HTR corpus", "latin", "変体仮名資料の手書き認識で作る古典読解基盤。"),
    ("椰子葉写本OCR綴葉", "palm-leaf OCR foliation", "palm-leaf OCR foliation", "latin", "綴じ穴や葉番号がOCR上で本文へ混入する問題。"),
    ("白樺文書TEI断片", "birchbark TEI fragment", "birchbark TEI fragment", "latin", "白樺樹皮文書の欠損をTEI断片として符号化する実践。"),
    # Cluster 4: low-resource literary translation AI
    ("アイヌ語LLM訳注詩学", "Ainu LLM annotation poetics", "Ainu LLM annotation poetics", "latin", "低資源語訳でAI注釈が本文解釈を過剰誘導する問題。"),
    ("ヨルバ声調MT詩", "Yoruba tone MT poetry", "Yoruba tone MT poetry", "latin", "声調情報の脱落が機械翻訳詩の意味を変える現象。"),
    ("ナワトル語形態素プロンプト", "Nahuatl morpheme prompting", "Nahuatl morpheme prompting", "latin", "膠着的形態素を明示してAI翻訳を制御する技法。"),
    ("ガリシア語LLM自己翻訳", "Galician LLM self-translation", "Galician LLM self-translation", "latin", "周縁語作家がAIで自作を大言語へ移す実践。"),
    ("アムハラ語OCR翻訳連鎖", "Amharic OCR translation chain", "Amharic OCR translation chain", "latin", "文字認識誤りが逐次翻訳で増幅する文学資料問題。"),
    ("タミル古典MTサンドヒ", "Tamil classical MT sandhi", "Tamil classical MT sandhi", "latin", "連声解析の失敗が古典詩翻訳を歪める機械翻訳論点。"),
    # Cluster 5: agentic and platform subgenre variants
    ("Discordダイスボット叙事詩", "Discord dice-bot epic", "Discord dice-bot epic", "latin", "乱数ボットの判定ログから生成される共同叙事詩。"),
    ("Telegram分岐民話", "Telegram branching folktale", "Telegram branching folktale", "latin", "メッセージボタンで選択肢を進める民話再話形式。"),
    ("VTuber人格小説ログ", "VTuber persona fiction log", "VTuber persona fiction log", "latin", "配信人格の発話ログを虚構テクストとして読む形式。"),
    ("TRPGセッションRAG小説", "TRPG session RAG fiction", "TRPG session RAG fiction", "latin", "プレイ記録検索で次話を生成するキャンペーン小説。"),
    ("ファンWikiカノンRAG", "fan-wiki canon RAG", "fan-wiki canon RAG", "latin", "ファンWiki検索で二次創作の設定整合性を保つ方法。"),
    ("AO3タグ埋め込み詩学", "AO3 tag embedding poetics", "AO3 tag embedding poetics", "latin", "同人タグの埋め込みが欲望分類を固定する現象。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            assert len(definition) <= 100, name_ja
            exists_anywhere = db.conn.execute(
                "SELECT id FROM concepts WHERE name_ja = ?", (name_ja,)
            ).fetchone()
            if exists_anywhere:
                raise RuntimeError(f"concept already exists: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                period_id=PERIOD_ID,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
    print(f"INSERTED={inserted}")


if __name__ == "__main__":
    main()
