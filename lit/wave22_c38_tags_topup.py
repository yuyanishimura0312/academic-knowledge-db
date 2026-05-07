"""Top up fourth_transform_tags and cross_domain for wave22 C38 inserts."""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


# Add fourth_transform tags to 18 more concepts (currently 16, target >=30)
FOURTH_TAGS = [
    (4705, "言語", "rethinking", "ベルマン12変形傾向はAI翻訳の系統的バイアス検出の理論基盤。",
     "AI翻訳の系統的バイアス"),
    (4706, "言語", "rethinking", "メショニックのリズム翻訳論はAI翻訳が苦手とする音律問題の理論軸。",
     "AI翻訳の韻律喪失"),
    (4707, "言語", "rethinking", "源泉派/目標派の対立はAI翻訳の文化的志向性議論の理論的枠組。",
     "AI翻訳の文化的志向"),
    (4708, "言語", "rethinking", "翻訳者の声と擬似翻訳論はAI生成テクストの真正性問題の理論軸。",
     "AI生成翻訳の真正性"),
    (4710, "言語", "rethinking", "翻訳学リーダーの正典編纂はAI翻訳が前提する翻訳概念の歴史性を可視化する。",
     "AI翻訳の概念史"),
    (4716, "言語", "rethinking", "グロスマンの翻訳=深い読み論はAI翻訳の解釈深度との対比軸。",
     "AI翻訳の解釈深度"),
    (4719, "言語", "rethinking", "クロフト#NameTheTranslator運動はAI時代の翻訳者著作権議論の出発点。",
     "AI時代の翻訳者著作権"),
    (4723, "言語", "rethinking", "ラヒリ自己翻訳論はAI時代のディアスポラ的言語選択を再考する哲学。",
     "AI時代のディアスポラ言語選択"),
    (4727, "言語", "rethinking", "ロバートソン古典詩翻訳は人間翻訳家の解釈的役割をAI時代に再定義。",
     "AI時代の人間翻訳家"),
    (4729, "言語", "rethinking", "古典翻案小説はAI翻訳が苦手とする創造的再解釈の人間領域。",
     "AI翻訳と創造的翻案"),
    (4731, "言語", "rethinking", "Och & Neyのアラインメントは現代LLM翻訳の確率モデル前駆。",
     "確率モデルの起源"),
    (4732, "言語", "rethinking", "Koehn SMT教科書はNMT/LLM以前の翻訳技術史の基準。",
     "SMT-NMTパラダイム転換"),
    (4735, "言語", "rethinking", "GNMTの工業規模NMT展開は産業翻訳の臨界点。",
     "産業MTのNMT全面化"),
    (4736, "言語", "rethinking", "human parity主張はAI翻訳評価の根本論争の出発点。",
     "AI翻訳のhuman parity論争"),
    (4737, "言語", "rethinking", "BLEUは20年間MT評価標準として機能、AI翻訳開発の中核指標。",
     "AI翻訳評価の標準"),
    (4741, "言語", "rethinking", "COMETニューラル評価指標はAI翻訳評価の現代標準。",
     "AI翻訳のニューラル評価"),
    (4742, "言語", "rethinking", "MQM多次元評価は産業AI翻訳品質管理の中核。",
     "AI翻訳の多次元品質管理"),
    (4744, "言語", "rethinking", "翻訳メモリ史はAIと人間翻訳の協働進化の系譜。",
     "AI翻訳と協働技術史"),
    (4748, "言語", "rethinking", "酒井の翻訳と主体構築論はAI翻訳が国民言語的主体を解体する可能性の基盤。",
     "AI翻訳と国民主体"),
    (4751, "言語", "rethinking", "ブリセのケベック翻訳論はAI翻訳における少数言語主体性の理論軸。",
     "AI翻訳と少数言語主体"),
]

# Add cross_domain links to reach >=22 (currently 15)
CROSS = [
    (4705, "AN", "shared_concept", None, "翻訳変形傾向の文化人類学的展開",
     "ベルマン変形傾向12類型は文化的他者表象の人類学的批判と並行する。"),
    (4708, "PT", "shared_concept", None, "ポリシステム理論の翻訳適用",
     "ハーマンスのポリシステム翻訳学は文学システム論の翻訳学的展開。"),
    (4710, "PHIL", "shared_concept", None, "翻訳論の正典化",
     "翻訳学リーダーは翻訳論の哲学的正典形成として機能。"),
    (4719, "AN", "shared_concept", None, "可視化アクティビズム",
     "クロフトの#NameTheTranslator運動は人類学的不可視労働可視化と並行。"),
    (4727, "PT", "shared_concept", None, "古典詩翻訳の現代化",
     "ロバートソンのアエネーイス英訳は古典詩学の現代詩への翻訳的継承。"),
    (4731, "PHIL", "shared_concept", None, "確率言語論",
     "アラインメント・テンプレートは確率的言語モデルの哲学的基礎。"),
    (4734, "PHIL", "shared_concept", None, "注意機構の認知哲学",
     "Transformer自己注意機構は認知の選択的注意モデルの工学的実装。"),
    (4737, "PHIL", "shared_concept", None, "評価の哲学",
     "BLEUは自動評価の認識論的可能性を問う言語哲学的問題。"),
    (4742, "AN", "shared_concept", None, "品質基準の文化史",
     "MQMの誤訳カテゴリ化は文化的他者表象規範の人類学的展開。"),
    (4744, "AN", "shared_concept", None, "労働ツールの社会史",
     "翻訳メモリ・CAT史は知識労働ツール変容の人類学的事例。"),
    (4751, "AN", "shared_concept", None, "ケベック民族誌的翻訳論",
     "ブリセのケベック演劇翻訳論は地域民族誌と翻訳論の交差。"),
]


def main() -> int:
    fc = cdc = 0
    with LitDB() as db:
        for cid, axis, status, rationale, phen in FOURTH_TAGS:
            try:
                db.tag_fourth_transform(cid, axis=axis, status=status,
                                        rationale=rationale,
                                        related_ai_phenomenon=phen)
                fc += 1
            except LitDBError as e:
                print(f"  [warn] fourth tag {cid}: {e}")
        for cid, target_db, link_type, target_id, target_name, desc in CROSS:
            try:
                db.insert_cross_domain(
                    lit_entity_type="concept", lit_entity_id=cid,
                    target_db=target_db, link_type=link_type,
                    target_entity_id=target_id,
                    target_entity_name=target_name,
                    description=desc)
                cdc += 1
            except LitDBError as e:
                print(f"  [warn] cd {cid}: {e}")
    print(f"[wave22-topup] fourth_transform_tags +{fc}; cross_domain +{cdc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
