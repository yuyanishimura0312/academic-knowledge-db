#!/usr/bin/env python3
"""Wave 40: 30 hyper-niche lit_digital_ai concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_digital_ai"
REGION = "理論"
PERIOD_ID = None

CONCEPTS = [
    # Cluster 1: prompt micro-poetics
    ("ネガティブプロンプト詩学", "negative prompt poetics", "negative prompt poetics", "latin", "生成しない語を指定して作品の輪郭を作る記述技法。"),
    ("seed値作者性", "seed authorship", "seed authorship", "latin", "乱数種の選択を作者的判断として読むAI生成論。"),
    ("temperature文体論", "temperature stylistics", "temperature stylistics", "latin", "温度設定が比喩密度や逸脱度を変える文体分析。"),
    ("top-p物語制御", "top-p narrative control", "top-p narrative control", "latin", "核サンプリング値で物語の予測性を調整する技法。"),
    ("プロンプト連鎖連載", "prompt-chain seriality", "prompt-chain seriality", "latin", "前回出力を次回入力にして続くAI連載形式。"),
    ("システム漏洩読解", "system prompt leak reading", "system prompt leak reading", "latin", "漏れた隠し指示を作品の副本文として読む方法。"),
    # Cluster 2: retrieval and corpus substrate
    ("埋め込みドリフト物語論", "embedding drift narratology", "embedding drift narratology", "latin", "ベクトル空間の時間差が物語解釈をずらす現象。"),
    ("チャンク境界詩学", "chunk-boundary poetics", "chunk-boundary poetics", "latin", "分割単位の切れ目が検索生成文の意味を変える効果。"),
    ("ベクトルDB副本文", "vector database paratext", "vector database paratext", "latin", "索引化された埋め込みを作品周辺の副本文と見る概念。"),
    ("検索温度混交文体", "retrieval-temperature style mix", "retrieval-temperature style mix", "latin", "検索文脈と生成温度の相互作用で生じる文体。"),
    ("セマンティックキャッシュ作者性", "semantic cache authorship", "semantic cache authorship", "latin", "再利用応答の蓄積が作者声を固定する現象。"),
    ("重複除去コーパス詩学", "deduplication corpus poetics", "deduplication corpus poetics", "latin", "重複除去が定型句や反復美を消す訓練データ問題。"),
    # Cluster 3: character agents and fan writing
    ("Lorebook詩学", "lorebook poetics", "lorebook poetics", "latin", "AI物語で世界設定辞書が展開を拘束する仕組み。"),
    ("メモリ窓ロマンス", "memory-window romance", "memory-window romance", "latin", "会話記憶の窓幅が親密性の連続を作る恋愛物語。"),
    ("ペルソナカード同人誌", "persona-card fanfic", "persona-card fanfic", "latin", "キャラ定義カードを原作にするAI同人創作形式。"),
    ("OOC割込み物語論", "OOC interruption narratology", "OOC interruption narratology", "latin", "ロール外発話が虚構契約を破る瞬間の分析。"),
    ("キャノン固定プロンプト", "canon-lock prompting", "canon-lock prompting", "latin", "原作設定から逸脱しないよう制約する同人AI指示。"),
    ("親密性ファインチューニング", "intimacy fine-tuning", "intimacy fine-tuning", "latin", "恋人AIの語調を関係履歴へ適応させる調整。"),
    # Cluster 4: multimodal and voice text
    ("OCRノイズ韻律", "OCR noise prosody", "OCR noise prosody", "latin", "誤認字列が詩行のリズムや視覚性を変える効果。"),
    ("キャプション整列物語論", "caption alignment narratology", "caption alignment narratology", "latin", "画像説明文と場面叙述のずれを読む分析。"),
    ("潜在キャプション詩", "latent-caption poem", "latent-caption poem", "latin", "画像生成モデル内部の説明語を詩素材にする形式。"),
    ("タイムスタンプ台詞詩学", "timestamped transcript poetics", "timestamped transcript poetics", "latin", "字幕時刻と発話断片が作る映像由来の文体。"),
    ("合成朗読ブレスモデル", "synthetic narration breath model", "synthetic narration breath model", "latin", "AI朗読の息継ぎ推定が詩句解釈を変える現象。"),
    ("音素プロンプト韻律", "phoneme prompt prosody", "phoneme prompt prosody", "latin", "音素列指示で朗読の韻律を作る音声AI技法。"),
    # Cluster 5: evaluation and refusal forms
    ("干し草針精読", "needle-in-haystack close reading", "needle-in-haystack close reading", "latin", "長文内の一点回収能力を精読能力として測る発想。"),
    ("ベンチ汚染正典化", "benchmark contamination canonization", "benchmark contamination canonization", "latin", "評価データ混入で作品がAI読解の正典になる現象。"),
    ("Self-BLEU文体模倣", "Self-BLEU style imitation", "Self-BLEU style imitation", "latin", "生成文同士の類似度で文体模倣の狭さを測る手法。"),
    ("散文パープレキシティ", "prose perplexity", "prose perplexity", "latin", "言語モデルの驚き度で散文の予測困難性を見る指標。"),
    ("LLM批評者較正", "LLM-as-critic calibration", "LLM-as-critic calibration", "latin", "AI批評の採点傾向を人間評価に合わせて補正する作業。"),
    ("拒否応答副本文", "refusal paratext", "refusal paratext", "latin", "安全拒否文を作品周辺の制度的テクストとして読む概念。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            assert len(definition) <= 100, name_ja
            before = db.find_concept(name_ja, REGION, PERIOD_ID)
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
            after = db.find_concept(name_ja, REGION, PERIOD_ID)
            if before is None and after is not None:
                inserted += 1
    print(f"INSERTED={inserted}")


if __name__ == "__main__":
    main()
