#!/usr/bin/env python3
"""Wave 42: add 30 hyper-niche concepts to lit_genre."""

from lit_db_helper import LitDB


CONCEPTS = [
    # 1. Itinerant print and ephemeral booklets
    ("旅芸人暦チャップブック", "Itinerant almanac chapbook", "itinerant almanac chapbook", "latin", "巡回芸人の暦・占い・逸話を束ねた廉価小冊子ジャンル。"),
    ("港湾水先案内怪談本", "Harbor pilot ghost chapbook", "harbor pilot ghost chapbook", "latin", "水先案内人の事故譚と幽霊目撃を集める港湾廉価怪談。"),
    ("巡礼宿奇跡小冊子", "Pilgrim-inn miracle booklet", "pilgrim-inn miracle booklet", "latin", "巡礼宿の治癒・失踪・聖遺物逸話を短く売る信心小冊子。"),
    ("市場辻占い恋愛譚", "Market fortune-love tale", "market fortune-love tale", "latin", "市場の辻占い文句を恋愛筋へ転用する民衆小説。"),
    ("行商薬売り証言譚", "Peddler-medicine testimonial tale", "patent-medicine testimonial tale", "latin", "万能薬広告の体験談を冒険・回心譚へ膨らませる小冊子。"),
    ("河岸説教バラッド物語", "Quayside sermon-ballad tale", "quayside sermon-ballad tale", "latin", "河岸の説教歌を犯罪戒め物語に変えるバラッド散文。"),
    # 2. Micro-regional crime and border mysteries
    ("ルクセンブルク鉱山ノワール", "Luxembourg mine noir", "Luxembourg mine noir", "latin", "鉄鉱山の労働記憶と国境通勤を暗部にする犯罪小説。"),
    ("イストリア三言語ミステリ", "Istrian trilingual mystery", "Istrian trilingual mystery", "latin", "伊・斯・クロアチア語の聞き違いを謎解きに使う半島ミステリ。"),
    ("シェトランド油田探偵譚", "Shetland oilfield detective tale", "Shetland oilfield detective tale", "latin", "北海油田労働と島嶼親族網を事件構造にする探偵小説。"),
    ("オーランド自治島犯罪譚", "Aland autonomy crime tale", "Aland autonomy crime tale", "latin", "自治法と言語境界を動機に組み込むバルト海犯罪小説。"),
    ("ラップランド税関スリラー", "Lapland customs thriller", "Lapland customs thriller", "latin", "越境密輸と雪原検問を追跡装置にする北方スリラー。"),
    ("メノルカ要塞ミステリ", "Menorcan fortress mystery", "Menorcan fortress mystery", "latin", "港湾要塞の軍事記憶と観光開発を謎に絡める島嶼ミステリ。"),
    # 3. Occupational romance and domestic microgenres
    ("電報局夜勤ロマンス", "Telegraph-office night-shift romance", "telegraph-office night-shift romance", "latin", "夜勤電報局の符号誤読と遠距離求婚を筋にする職業ロマンス。"),
    ("製帽工場ストライキ恋愛譚", "Hat-factory strike romance", "hat-factory strike romance", "latin", "製帽工場の争議と恋愛選択を重ねる都市労働ロマンス。"),
    ("薬草園看護婦ロマンス", "Herb-garden nurse romance", "herb-garden nurse romance", "latin", "療養院薬草園の看護労働と回復恋愛を描く職業小説。"),
    ("駅弁売り娘出世譚", "Station-bento girl success tale", "station lunch girl success tale", "latin", "駅弁売りの接客技能と鉄道移動を階層上昇へ結ぶ物語。"),
    ("写真館助手求婚譚", "Photography-studio assistant courtship", "photography-studio assistant courtship", "latin", "写真館助手の肖像修整と縁談を絡める都市恋愛小説。"),
    ("電話交換手暗号恋愛譚", "Switchboard cipher romance", "switchboard cipher romance", "latin", "電話交換手が暗号化された恋文と事件通話を読むロマンス。"),
    # 4. Speculative infrastructure and weird science
    ("真空管修道院SF", "Vacuum-tube monastery SF", "vacuum-tube monastery SF", "latin", "修道院の計算機化と信仰規律を真空管技術で描くSF。"),
    ("潮汐発電島ユートピア", "Tidal-power island utopia", "tidal-power island utopia", "latin", "潮汐発電だけで運営される島の労働制度を描くユートピア。"),
    ("気送管都市探偵譚", "Pneumatic-tube city detective tale", "pneumatic-tube city detective tale", "latin", "気送管網の誤配と密書を手掛かりにする都市探偵SF。"),
    ("藻類酸素惑星ロマンス", "Algae-oxygen planet romance", "algae-oxygen planet romance", "latin", "藻類酸素化計画の失敗と植民恋愛を絡める惑星ロマンス。"),
    ("鉱山カナリア終末譚", "Mine-canary apocalypse tale", "mine-canary apocalypse tale", "latin", "坑内カナリアの異変を文明崩壊の兆候にする終末小説。"),
    ("自動人形検疫ホラー", "Automaton quarantine horror", "automaton quarantine horror", "latin", "自動人形の感染疑惑と隔離手続きを恐怖化する怪奇SF。"),
    # 5. Children's club and miniature institutional tales
    ("少年測候所クラブ物語", "Boy weather-station club story", "weather-station club story", "latin", "少年クラブが気象観測で遭難や犯罪を解く教育冒険譚。"),
    ("少女切手交換クラブ譚", "Girl stamp-exchange club tale", "stamp-exchange club tale", "latin", "切手交換を国際友情と謎解きへ広げる少女クラブ小説。"),
    ("児童灯台見習い物語", "Child lighthouse-apprentice story", "lighthouse-apprentice story", "latin", "灯台見習いの規律と救難を児童向け成長譚にする物語。"),
    ("寄宿学校養蜂クラブ譚", "Boarding-school beekeeping club tale", "beekeeping club tale", "latin", "寄宿学校の養蜂活動を規律違反と和解に結ぶ児童小説。"),
    ("玩具病院道徳絵本", "Toy-hospital moral picturebook", "toy-hospital picturebook", "latin", "壊れた玩具の治療を親切・節約の教訓にする絵本型。"),
    ("町立水族館児童探偵譚", "Municipal-aquarium child detective tale", "aquarium child detective tale", "latin", "町立水族館の飼育記録と盗難を結びつける児童探偵譚。"),
]


def main() -> None:
    inserted = 0
    with LitDB("lit.sqlite") as db:
        existing = {
            row[0]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 21"
            )
        }
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            if name_ja in existing:
                continue
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code="lit_genre",
                region="周縁横断",
                period_id=None,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
    print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
