#!/usr/bin/env python3
"""Wave 43: add 30 ultra-niche lit_digital_ai concepts."""

from lit_db_helper import LitDB


CONCEPTS = [
    # 1. RAG・検索副本文
    ("埋め込み空白脚注", "Embedding-gap footnote poetics", "embedding-gap footnote poetics", "latin", "検索で近傍化されない沈黙を脚注的意味として読むRAG詩学。"),
    ("再ランキング語り手偏差", "Reranker narrator skew", "reranker narrator skew", "latin", "リランキングが語り手の焦点化を偏らせる現象の読解概念。"),
    ("失敗検索プロローグ", "Failed-retrieval prologue", "failed-retrieval prologue", "latin", "検索不能な前提を導入部の不在として物語化する形式。"),
    ("チャンク重複リフレイン", "Chunk-overlap refrain", "chunk-overlap refrain", "latin", "重複チャンクが反復句のように生成文体へ戻る現象。"),
    ("ベクトル孤児引用", "Vector-orphan quotation", "vector-orphan quotation", "latin", "出典近傍を失った引用片が権威だけ残すRAG副本文。"),
    ("検索閾値サスペンス", "Retrieval-threshold suspense", "retrieval-threshold suspense", "latin", "検索閾値の通過可否を謎の開示遅延として読む技法。"),
    # 2. エージェント物語
    ("ツール呼出し叙法", "Tool-call narration", "tool-call narration", "latin", "外部ツール実行ログを叙述単位にするエージェント物語技法。"),
    ("関数戻り値伏線", "Function-return foreshadowing", "function-return foreshadowing", "latin", "関数の戻り値を後段の伏線として読むAI物語構成。"),
    ("プラン更新章法", "Plan-update chaptering", "plan-update chaptering", "latin", "エージェントの計画更新を章立てとして使う生成物語形式。"),
    ("サブエージェント合唱", "Subagent choral narration", "subagent choral narration", "latin", "複数エージェントの報告を合唱的語りへ編成する形式。"),
    ("権限拒否クライマックス", "Permission-denial climax", "permission-denial climax", "latin", "権限不足や拒否応答を物語の頂点に転化する技法。"),
    ("監査ログ内面独白", "Audit-log interior monologue", "audit-log interior monologue", "latin", "監査ログを機械主体の内面独白として読む概念。"),
    # 3. 合成音声・字幕詩学
    ("息継ぎタグ韻律", "Breath-tag prosody", "breath-tag prosody", "latin", "合成朗読の息継ぎタグを韻律記号として扱う詩学。"),
    ("話者分離叙述者", "Diarized narrator", "diarized narrator", "latin", "話者分離結果が複数の叙述者を作る音声テクスト概念。"),
    ("字幕遅延エンジャンブメント", "Subtitle-lag enjambment", "subtitle-lag enjambment", "latin", "字幕の表示遅延を詩行またぎとして読む映像詩学。"),
    ("声紋カノン模倣", "Voiceprint canon mimicry", "voiceprint canon mimicry", "latin", "声紋の類似度で正典的語りを模倣する合成音声詩学。"),
    ("無音区間句読法", "Silence-interval punctuation", "silence-interval punctuation", "latin", "ASRの無音区間を句読点の代替として読む音声文学概念。"),
    ("タイムコード脚韻", "Timecode rhyme", "timecode rhyme", "latin", "一致する時刻配置を脚韻のように読む字幕・音声詩学。"),
    # 4. マルチモーダル読解
    ("OCR枠線隠喩", "OCR-box metaphorics", "OCR-box metaphorics", "latin", "文字認識の矩形枠を読解上の視線や監禁の比喩にする概念。"),
    ("画像埋め込み地の文", "Image-embedding exposition", "image-embedding exposition", "latin", "画像埋め込みの類似度を地の文の説明力として読む概念。"),
    ("CLIP誤読アレゴリー", "CLIP-misreading allegory", "CLIP-misreading allegory", "latin", "画像言語モデルの誤分類を寓意生成として読む批評概念。"),
    ("レイアウト幻覚欄外譚", "Layout-hallucinated marginalia", "layout-hallucinated marginalia", "latin", "存在しない欄外や段組みを生成する幻覚の読解概念。"),
    ("altテキスト余白声", "Alt-text margin voice", "alt-text margin voice", "latin", "代替テキストを画面外の欄外語りとして扱う概念。"),
    ("ピクセル近傍引用", "Pixel-neighbor citation", "pixel-neighbor citation", "latin", "画素特徴の近さで画像引用の系譜を構成する読解概念。"),
    # 5. 合成評価・ベンチ詩学
    ("評価プロンプト正典化", "Evaluation-prompt canonization", "evaluation-prompt canonization", "latin", "評価用プロンプトが読解規範を固定する過程への批評概念。"),
    ("採点ルーブリック語り", "Rubric narration", "rubric narration", "latin", "採点基準そのものが物語の声を形成するLLM評価詩学。"),
    ("ベンチ漏洩記憶譚", "Benchmark-leak memory tale", "benchmark-leak memory tale", "latin", "漏洩ベンチを機械の既読記憶として読む概念。"),
    ("拒否率文体指標", "Refusal-rate style index", "refusal-rate style index", "latin", "拒否応答の頻度をジャンルや文体の指標にする分析概念。"),
    ("相互採点カノン闘争", "Peer-eval canon struggle", "peer-eval canon struggle", "latin", "モデル同士の採点を正典形成の競合として読む概念。"),
    ("合成読者較正", "Synthetic-reader calibration", "synthetic-reader calibration", "latin", "AI読者の反応分布を批評読者像へ調整する方法概念。"),
]


def main() -> None:
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        existing = {
            row[0]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 24"
            )
        }
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            if name_ja in existing:
                skipped += 1
                continue
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code="lit_digital_ai",
                region="理論",
                period_id=None,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
    print(f"inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
