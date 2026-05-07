#!/usr/bin/env python3
"""Tag untagged lit_latin_america concepts for fourth transform axes."""

import sqlite3

DB = "lit.sqlite"
ALLOWED_AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}
ALLOWED_STATUS = {"rethinking", "partial", "invariant"}
RATIONALE_SUFFIX = "ためAI時代に再考が必要となる"

TAGS = [
    (401, "創造性", "rethinking", "欧州摂取と地域美学の創造的混成が再生成で揺らぐ", "様式生成"),
    (402, "作者性", "partial", "運動の父という個人権威が共作的生成で相対化する", "AI共著"),
    (403, "正典", "rethinking", "詩散文集の開幕性が要約流通で再配置される", "要約流通"),
    (404, "翻訳", "rethinking", "仏詩潮流の移植過程が機械翻訳で平板化しうる", "機械翻訳"),
    (405, "言語", "rethinking", "象徴詩の音楽性と暗示が生成文の説明性と衝突する", "詩生成"),
    (407, "真正性", "rethinking", "ブラジル性の探求が合成的な民族表象で再審される", "合成表象"),
    (408, "真正性", "rethinking", "土着風土の本質表象がデータ化で定型化されやすい", "地域ステレオタイプ"),
    (409, "主体", "rethinking", "先住民問題の代弁構造がAI代筆でさらに問われる", "代筆生成"),
    (411, "真正性", "rethinking", "現実そのものの驚異という主張が合成幻想と競合する", "合成リアリズム"),
    (413, "物語", "rethinking", "読者参加型の章順構造が対話生成で再機能化する", "インタラクティブ生成"),
    (414, "物語", "partial", "全体小説の統合志向が大規模生成の総覧性と重なる", "長文生成"),
    (415, "物語", "rethinking", "架空都市連作の空間一貫性が生成世界構築で再検討される", "世界生成"),
    (416, "物語", "partial", "神話歴史の巨大網目がAI要約で構造化され直す", "構造要約"),
    (418, "主体", "rethinking", "地政学的孤独の語りが外部モデルの視線で変質する", "外部視点生成"),
    (419, "主体", "rethinking", "我々は何者かという問いがAI分類で固定化されうる", "アイデンティティ分類"),
    (421, "物語", "rethinking", "権力の声と神格化の語りが模倣生成で再演される", "権力文体模倣"),
    (422, "主体", "rethinking", "亡命の身体性が遠隔共作やデジタル移動で変わる", "遠隔共作"),
    (423, "受容", "rethinking", "対抗記憶の証言性が合成記録の拡散で揺らぐ", "合成証言"),
    (424, "物語", "rethinking", "暴力表象の反復が生成モデルで消費的に増幅される", "暴力生成"),
    (425, "受容", "partial", "抒情的代表作の読まれ方がAI推薦で再配列される", "推薦アルゴリズム"),
    (426, "正典", "rethinking", "ブーム後の評価軸が市場データと推薦で再構成される", "市場推薦"),
    (427, "真正性", "rethinking", "反マコンドの都市性がグローバル生成文体と接続する", "都市文体生成"),
    (428, "正典", "partial", "全体小説回帰の宣言性が生成長編の野心と比較される", "長編生成"),
    (430, "物語", "rethinking", "犯罪小説の社会解剖がデータ駆動の事件語りと交差する", "犯罪データ生成"),
    (432, "正典", "rethinking", "男性中心正典の修正がAI推薦の偏りで再び問われる", "推薦バイアス"),
    (433, "言語", "rethinking", "二言語実践と自己代弁が機械翻訳で再配置される", "多言語生成"),
    (434, "作者性", "rethinking", "政治的責任を負う作者像が自動生成文で曖昧になる", "自動生成"),
    (436, "主体", "rethinking", "異質な生産主体の併存がデータ統合で均質化されうる", "データ統合"),
    (438, "受容", "rethinking", "市場化された魔術的像が生成AIでさらに定型化される", "市場的生成"),
    (441, "真正性", "partial", "驚異的現実の理論差異が合成現実論と再接続する", "合成現実"),
    (873, "受容", "rethinking", "告発文書の証言性が合成資料との判別問題を招く", "合成資料"),
    (874, "作者性", "rethinking", "従軍兵士の目撃者権威が生成された回想と比較される", "合成回想"),
    (875, "作者性", "partial", "女性知識人の署名と権利主張がAI代筆で再考される", "代筆生成"),
    (876, "創造性", "partial", "知的飛翔のバロック統合が生成的引用合成と照応する", "引用合成"),
    (877, "翻訳", "rethinking", "口承とスペイン語様式の媒介がAI翻訳で再審される", "機械翻訳"),
    (878, "真正性", "rethinking", "敵の英雄化という叙述倫理が合成視点で揺さぶられる", "視点生成"),
    (879, "言語", "rethinking", "ガウチョ口語の文学化が方言生成の真正性を問う", "方言生成"),
    (881, "主体", "rethinking", "ガウチョ一人称の代表性がAI代弁で再問題化する", "代弁生成"),
    (882, "正典", "rethinking", "文明野蛮の二分法が分類モデルで再生産されやすい", "分類バイアス"),
    (883, "物語", "partial", "政治寓話の暴力場面が生成再話で倫理的に揺らぐ", "再話生成"),
    (884, "物語", "partial", "恋愛悲劇と政治小説の融合がジャンル生成で再編される", "ジャンル生成"),
    (885, "言語", "rethinking", "アメリカ独自のスペイン語規範が大規模言語モデルで問われる", "言語モデル"),
    (886, "受容", "partial", "風俗スケッチの観察性が生成された地域描写と競合する", "地域描写生成"),
    (887, "受容", "partial", "欧州受容と地域課題の接合が翻案生成で再配置される", "翻案生成"),
    (888, "物語", "partial", "客観描写の枠組みがデータ的社会記述と比較される", "データ叙述"),
    (889, "主体", "rethinking", "遺伝環境決定論がAI予測的分類と危うく響き合う", "予測分類"),
    (890, "真正性", "rethinking", "理想化された先住民像が合成画像文で再固定されうる", "合成表象"),
    (891, "作者性", "partial", "詩人革命家の統合的作者像がAI引用で断片化される", "引用生成"),
    (892, "物語", "rethinking", "歴史と虚構の混淆ジャンルが生成逸話で境界を失う", "逸話生成"),
    (893, "正典", "partial", "大地小説の基層作品群が推薦分類で可視性を変える", "推薦分類"),
    (894, "主体", "partial", "汎ラテンアメリカ知識人像が移動データで再読される", "移動データ"),
    (895, "物語", "partial", "国民形成の歴史叙事がAI時系列化で再編される", "時系列生成"),
    (898, "主体", "rethinking", "民俗的主体としてのガウチョが合成代弁で揺らぐ", "代弁生成"),
    (899, "主体", "rethinking", "クリオージョ自意識がAI分類で単純化されやすい", "分類生成"),
    (901, "真正性", "rethinking", "大陸空間の文学化が地理データ生成で再定義される", "地理生成"),
    (902, "主体", "rethinking", "文明と辺境の境界線がモデル分類で再生産される", "境界分類"),
    (903, "受容", "rethinking", "イスパニダー評価の論争性が要約で中立化されやすい", "論争要約"),
    (906, "受容", "partial", "新聞連載の大衆流通がプラットフォーム連載と接続する", "連載配信"),
    (907, "言語", "partial", "風俗列挙の語彙が生成的地域描写の素材になる", "語彙生成"),
    (908, "言語", "rethinking", "アメリカ語規範論が標準化モデルの言語観を問う", "標準化モデル"),
    (909, "受容", "rethinking", "新大陸ユートピア像が生成未来像で再利用される", "未来像生成"),
    (910, "作者性", "rethinking", "クリオージョ話者位置がAIの無国籍な声で揺らぐ", "無国籍文体"),
    (2492, "真正性", "partial", "河川地域の生活詩学が観光的生成描写と緊張する", "地域生成"),
    (2493, "言語", "rethinking", "ケチュア語題名の政治性が自動翻訳で薄まりうる", "自動翻訳"),
    (2496, "物語", "partial", "革命断章の連鎖形式がAI要約で直線化されやすい", "要約生成"),
    (2497, "作者性", "rethinking", "革命証言の観察者位置が合成回想で不安定になる", "合成回想"),
    (2498, "物語", "partial", "多視点の精神的閉塞が生成要約で単声化されやすい", "要約生成"),
    (2499, "言語", "rethinking", "省略された口語の強度がAI補完で失われやすい", "文章補完"),
    (2501, "物語", "partial", "都市総合小説の多話者構造がAI都市生成と接続する", "都市生成"),
    (2503, "主体", "rethinking", "三声の臨終意識が生成視点切替で再考される", "視点生成"),
    (2504, "物語", "partial", "歴史総合小説の往還構造がAI要約で再配置される", "構造要約"),
    (2505, "物語", "partial", "迫害史の循環構造が知識グラフ生成と接続する", "知識グラフ"),
    (2506, "主体", "rethinking", "少女視点の先住民関係叙述がAI代弁で問題化する", "代弁生成"),
    (2509, "物語", "rethinking", "全宇宙を見る一点の発想が総覧AIと強く響き合う", "総覧生成"),
    (2510, "正典", "rethinking", "遡及的影響論が推薦モデルの系譜生成と接続する", "系譜生成"),
    (2513, "物語", "partial", "日常への幻想侵入が生成ホラーの定型と比較される", "幻想生成"),
    (2514, "主体", "partial", "妄想的報告と実存の声がAI視点生成で再読される", "視点生成"),
    (2515, "作者性", "rethinking", "死者の回想という語り手設定がAI人格生成と交差する", "人格生成"),
    (2516, "創造性", "partial", "架空哲学の風刺がモデル生成の擬似理論と響き合う", "擬似理論生成"),
    (2518, "真正性", "rethinking", "報告書と文学の混合形式が合成ドキュメントで揺らぐ", "合成文書"),
]


def expanded_tags() -> list[tuple[int, str, str, str, str]]:
    rows = []
    for concept_id, axis, status, rationale, phenomenon in TAGS:
        if len(rationale) < 30:
            rationale = f"{rationale}{RATIONALE_SUFFIX}"
        rows.append((concept_id, axis, status, rationale, phenomenon))
    return rows


def validate(rows: list[tuple[int, str, str, str, str]]) -> None:
    by_concept = {}
    for concept_id, axis, status, rationale, phenomenon in rows:
        if axis not in ALLOWED_AXES:
            raise ValueError(f"bad axis: {concept_id} {axis}")
        if status not in ALLOWED_STATUS:
            raise ValueError(f"bad status: {concept_id} {status}")
        if not 30 <= len(rationale) <= 60:
            raise ValueError(f"bad rationale length: {concept_id} {len(rationale)}")
        if len(phenomenon) > 12:
            raise ValueError(f"phenomenon too long: {concept_id} {phenomenon}")
        by_concept.setdefault(concept_id, []).append(axis)
    for concept_id, axes in by_concept.items():
        if not 1 <= len(axes) <= 2:
            raise ValueError(f"bad tag count: {concept_id}")
        if len(axes) != len(set(axes)):
            raise ValueError(f"duplicate axis: {concept_id}")


def main() -> None:
    rows = expanded_tags()
    validate(rows)
    with sqlite3.connect(DB) as conn:
        before = conn.execute("SELECT COUNT(*) FROM fourth_transform_tags").fetchone()[0]
        conn.executemany(
            """
            INSERT OR IGNORE INTO fourth_transform_tags
                (concept_id, axis, status, rationale, related_ai_phenomenon)
            VALUES (?, ?, ?, ?, ?)
            """,
            rows,
        )
        conn.commit()
        after = conn.execute("SELECT COUNT(*) FROM fourth_transform_tags").fetchone()[0]
    print(f"inserted={after - before}")


if __name__ == "__main__":
    main()
