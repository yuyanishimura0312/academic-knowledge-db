#!/usr/bin/env python3
"""Wave 38: Add 30 deep genre niche concepts to subfield_id=21 (lit_genre)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"

# 5 clusters x 6 concepts = 30
# (name_ja, name_en, name_original, original_script, region, period_id, definition, importance, fourth_status, fourth_note, tier, canonical)
CONCEPTS = [
    # Cluster 1: ホラーゴシック
    ("ラヴクラフト式コズミック・ホラー", "Lovecraftian cosmic horror", "Lovecraftian cosmic horror", "latin", "世界", 129,
     "人類を矮小化する宇宙的他者性を描くホラー下位ジャンル。クトゥルフ神話を中核に展開。", 4, "rethinking", "AI/気候危機下で再評価", "tier1", None),
    ("フォーク・ホラー・リバイバル", "Folk horror revival", "Folk horror revival", "latin", "世界", 130,
     "土着信仰・農村風景・古代儀礼を媒介に田園の暗部を描く2000年代以降の復興潮流。", 4, "rethinking", "脱都市・脱植民地視点で再考", "tier1", None),
    ("ボディ・ホラー（クローネンバーグ系）", "Body horror (Cronenbergian)", "Body horror", "latin", "世界", 130,
     "身体変容・崩壊・侵食を主題化する身体恐怖サブジャンル。技術と肉体の境界を問う。", 4, "rethinking", "ポストヒューマン身体論で再考", "tier1", None),
    ("スラッシャー・フィクション", "Slasher fiction", "Slasher fiction", "latin", "世界", 130,
     "連続殺人者と若者集団を定型に置く暴力描写中心のホラー下位ジャンル。", 3, "partial", "ジェンダー暴力批評で再考", "tier2", None),
    ("クワイエット・ホラー（シャーリイ・ジャクスン系）", "Quiet horror", "Quiet horror", "latin", "世界", 129,
     "静謐な日常侵食と心理的不安を中心に置く非派手ホラー下位ジャンル。", 4, "invariant", "心理的不安の普遍性が継続", "tier1", None),
    ("スプラッターパンク", "Splatterpunk", "Splatterpunk", "latin", "世界", 130,
     "極端な流血・残虐描写と反権威的態度を結合した1980年代ホラー反主流派。", 3, "partial", "暴力表現倫理で再評価", "tier2", None),

    # Cluster 2: 児童・絵本ジャンル
    ("ピクチャーブック理論", "Picture book theory", "Picture book theory", "latin", "世界", 269,
     "絵と文の双方向関係（icontext）を中心に絵本の意味生成を解明する理論枠組み。", 4, "rethinking", "デジタル絵本でメディア論的再考", "tier1", None),
    ("ワードレス・ピクチャーブック", "Wordless picture book", "Wordless picture book", "latin", "世界", 129,
     "文字を持たず絵のみで物語を構築する絵本下位ジャンル。読者の能動的読解を要請。", 4, "invariant", "言語横断的価値が継続", "tier1", None),
    ("コンセプト・ブック", "Concept book", "Concept book", "latin", "世界", 129,
     "色・形・数等の概念学習を主目的とする乳幼児向け絵本下位ジャンル。", 3, "invariant", "発達段階に対応する基本機能", "tier2", None),
    ("YAグラフィックノベル", "Graphic novel YA", "Graphic novel YA", "latin", "世界", 130,
     "青少年読者を主対象とする長編コミック形式のYA文学下位ジャンル。アイデンティティ主題が中心。", 4, "rethinking", "視覚リテラシーで再考", "tier1", None),
    ("ミドルグレード・フィクション", "Middle grade fiction", "Middle grade fiction", "latin", "世界", 130,
     "8-12歳読者を対象とする児童文学市場区分。冒険・友情・成長を主題とする。", 3, "partial", "市場区分の文化差を再考", "tier2", None),
    ("ビギニング・リーダー（初期読者本）", "Beginning reader genre", "Beginning reader", "latin", "世界", 129,
     "語彙制限・短文反復で構成された就学初期向け読書教材ジャンル。", 3, "invariant", "識字教育の基幹形式", "tier2", None),

    # Cluster 3: 風刺・諷刺・コメディ
    ("モック・エピック（擬似英雄詩）", "Mock-epic", "Mock-epic", "latin", "世界", 128,
     "些事を英雄詩形式で誇張的に描く諷刺詩ジャンル。Pope『髪盗み』が代表。", 4, "invariant", "形式と内容の落差は普遍的諷刺技法", "tier1", None),
    ("ヒューディブラスティック詩", "Hudibrastic verse", "Hudibrastic verse", "latin", "世界", 128,
     "Butler『ヒューディブラス』由来の四歩格滑稽脚韻を用いる風刺韻文ジャンル。", 3, "invariant", "形式上の固有性は継続", "tier2", None),
    ("ランプーン", "Lampoon", "Lampoon", "latin", "世界", 128,
     "個人を激烈に嘲笑する短い諷刺作品ジャンル。匿名・暴力的諧謔を伴う。", 3, "partial", "ネット時代に形式変容", "tier2", None),
    ("ピカレスク・コミック", "Picaresque comic", "Picaresque comic", "latin", "世界", 128,
     "悪漢の遍歴を喜劇的に語るピカレスク下位ジャンル。社会階層諷刺を含む。", 3, "invariant", "社会風刺機能は継続", "tier2", None),
    ("マナー喜劇（風俗喜劇）", "Comedy of manners", "Comedy of manners", "latin", "世界", 128,
     "上流階級の社交慣習と恋愛駆引きを諷刺する喜劇ジャンル。Restoration期に確立。", 4, "partial", "階級表象論で再考", "tier1", None),
    ("観念喜劇小説", "Comic novel of ideas", "Comic novel of ideas", "latin", "世界", 130,
     "哲学・思想論争を喜劇的展開で描く小説下位ジャンル。Huxley・Lodge等。", 3, "invariant", "知的諷刺の枠組み継続", "tier2", None),

    # Cluster 4: 旅行・冒険・サバイバル
    ("文学的トラベル・ライティング", "Travel writing (literary)", "Travel writing", "latin", "世界", 130,
     "旅行体験を文学的散文として叙述するノンフィクション・ジャンル。Chatwin等。", 4, "rethinking", "ポストツーリズム時代に再考", "tier1", None),
    ("冒険小説", "Adventure novel", "Adventure novel", "latin", "世界", 128,
     "未踏地・危険・身体行動を中心とする物語ジャンル。19世紀後半に大衆化。", 4, "partial", "植民地批判の対象として再考", "tier1", None),
    ("サバイバル文学", "Survival literature", "Survival literature", "latin", "世界", 130,
     "極限環境下の生存闘争を主題化する物語ジャンル。フィクション・実録両形式。", 4, "rethinking", "気候危機文学と接続", "tier1", None),
    ("ロビンソナード", "Robinsonade", "Robinsonade", "latin", "世界", 128,
     "孤島漂着者の自給自足と再文明化を描く下位ジャンル。Defoeに由来。", 4, "rethinking", "脱植民地・脱資本主義視点で再考", "tier1", None),
    ("ロスト・ワールド・フィクション", "Lost world fiction", "Lost world fiction", "latin", "世界", 129,
     "辺境に残存する古代世界の発見を描く冒険SF下位ジャンル。Doyle『失われた世界』等。", 3, "rethinking", "オリエンタリズム批判で再考", "tier2", None),
    ("極地探検ナラティブ", "Polar exploration narrative", "Polar exploration narrative", "latin", "世界", 129,
     "南北極探検記を中心とする実録/フィクション下位ジャンル。Shackleton等。", 3, "rethinking", "気候変動文脈で再評価", "tier2", None),

    # Cluster 5: ジャンル横断・実験形式
    ("スリップストリーム", "Slipstream", "Slipstream", "latin", "世界", 130,
     "SF/ファンタジー/主流文学の境界を撹乱する横断的ジャンル概念。Sterling命名。", 4, "rethinking", "ジャンル境界の流動化が加速", "tier1", None),
    ("ビザロ・フィクション", "Bizarro fiction", "Bizarro fiction", "latin", "世界", 130,
     "意図的に奇怪・不条理な展開を追求する21世紀インディペンデント小説ジャンル。", 3, "partial", "オンライン文学経済で再考", "tier2", None),
    ("スチームパンク", "Steampunk", "Steampunk", "latin", "世界", 130,
     "19世紀蒸気技術と代替歴史を融合するSF下位ジャンル。1980年代に確立。", 4, "rethinking", "技術代替史の再評価", "tier1", None),
    ("ウィアード・ウェスト", "Weird West", "Weird West", "latin", "世界", 130,
     "西部劇に超自然・ホラー要素を融合する横断ジャンル。King『ダーク・タワー』等。", 3, "partial", "ジャンル混淆論で再考", "tier2", None),
    ("ニュー・ウィアード", "New Weird", "New Weird", "latin", "世界", 130,
     "ホラー/ファンタジー/SFを越境する21世紀初頭の文学運動。Miéville等が主導。", 4, "rethinking", "ポストジャンル時代を象徴", "tier1", None),
    ("ホーントロジー・フィクション", "Hauntology fiction", "Hauntology fiction", "latin", "世界", 130,
     "Derrida由来の亡霊論を文学化し失われた未来を主題化する21世紀潮流。", 4, "rethinking", "未来感覚の喪失を主題化", "tier1", None),
]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    inserted = 0
    skipped = 0
    for c in CONCEPTS:
        (name_ja, name_en, name_orig, script, region, period_id,
         definition, importance, fourth_status, fourth_note, tier, canonical) = c
        try:
            cur.execute("""
                INSERT INTO concepts (
                    name_ja, name_en, name_original, original_script,
                    subfield_id, region, period_id, definition,
                    importance_score, fourth_transform_status, fourth_transform_note,
                    source_tier, canonical_in_region
                ) VALUES (?, ?, ?, ?, 21, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, script, region, period_id,
                  definition, importance, fourth_status, fourth_note, tier, canonical))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP {name_ja}: {e}")
            skipped += 1

    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
