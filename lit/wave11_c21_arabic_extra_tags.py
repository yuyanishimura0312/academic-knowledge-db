"""Supplement: add more fourth_transform tags to wave11 Arabic add40 concepts.

Run after wave11_c21_arabic_add40.py to bring fourth_transform_tags coverage
above the >=12 threshold required for the wave.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


# (concept_id, axis, status, rationale, related_ai_phenomenon)
EXTRA_TAGS = [
    (1435, "言語", "rethinking",
     "ムワッシャハの最終句ハルジャはアラビア語とロマンス諸語の混淆を技法化する。多言語並行的に振る舞うLLMの言語混在現象の中世的祖型として再読される。",
     "多言語LLMにおけるコードスイッチング"),
    (1444, "正典", "rethinking",
     "シーラト・アンタルは口承+筆写+市場語りの混合的正典化を経た。AI時代における集合的・累積的テクスト正典化の歴史的祖型。",
     "AI生成による集合的テクスト累積と正典化"),
    (1446, "作者性", "rethinking",
     "バニー・ヒラール口承叙事は無名の語り手たちの累積的創作物である。LLMの集合的・無名的作者性の歴史的並行物として再読可能。",
     "LLMの集合的無名作者性"),
    (1452, "言語", "rethinking",
     "マッラーシュの寓意的散文は近代政治概念のアラビア語化を試みた。AI時代における概念翻訳と言語的近代化の祖型。",
     "AI翻訳と概念近代化"),
    (1455, "創造性", "rethinking",
     "アドゥニースは古典詩学からの脱抑制を「動性（mutahawwil）」として理論化した。AI時代の創造性論議への重要参照点。",
     "AI生成における創造性と脱抑制"),
    (1456, "受容", "rethinking",
     "ダルウィーシュ詩はパレスチナ集団的記憶の媒体として受容された。AI生成テキストが集合的記憶の媒体になり得るかという理論的問題の参照点。",
     "AI生成と集合的記憶の媒体化"),
    (1462, "物語", "rethinking",
     "カナファーニー作品は離散経験の凝縮的物語化を達成する。AI生成における離散・移動経験の物語化可能性の祖型。",
     "AI生成における離散経験の物語化"),
    (1467, "主体", "rethinking",
     "ハナーン・アッ=シャイフは家父長制下の女性主体を文学的に構築した。AI時代のジェンダー化された主体生成への参照点。",
     "AI生成におけるジェンダー化された主体構築"),
    (1473, "真正性", "rethinking",
     "シュクリ『裸の麺麭』は識字後に獲得された口語的真正性を文学化する。AI時代のテキスト真正性論議の参照点。",
     "AI生成テキストと識字的真正性"),
]


def main() -> int:
    count = 0
    with LitDB() as db:
        for cid, axis, status, rationale, ai_phen in EXTRA_TAGS:
            try:
                db.tag_fourth_transform(cid, axis=axis, status=status,
                                        rationale=rationale,
                                        related_ai_phenomenon=ai_phen)
                count += 1
            except LitDBError as e:
                print(f"  [warn] cid={cid}: {e}")
        print(f"[c21-add40 extras] +{count} fourth_transform tags")
    return 0


if __name__ == "__main__":
    sys.exit(main())
