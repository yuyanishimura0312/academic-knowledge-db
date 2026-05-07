#!/usr/bin/env python3
"""Wave 41: add 30 hyper-niche concepts to lit_genre."""

from lit_db_helper import LitDB


CONCEPTS = [
    # 1. Minor-language crime and parish mysteries
    ("アラン語渓谷犯罪小説", "Aranese valley crime fiction", "Aranese valley crime fiction", "latin", "ピレネー少数語共同体の地形と法慣習を謎解き化する犯罪小説。"),
    ("ミランダ語国境ミステリ", "Mirandese border mystery", "Mirandese border mystery", "latin", "ポルトガル北東部の少数語境界を事件構造に組む探偵譚。"),
    ("フェロー捕鯨ノワール", "Faroese whaling noir", "Faroese whaling noir", "latin", "捕鯨共同体の倫理対立を暗部として描く島嶼犯罪小説。"),
    ("ガーンジー占領ミステリ", "Guernsey occupation mystery", "Guernsey occupation mystery", "latin", "占領記憶と島内沈黙を謎にするチャネル諸島ミステリ。"),
    ("セトゥマー民俗探偵譚", "Setomaa folklore detective tale", "Setomaa folklore detective tale", "latin", "エストニア南東部の歌謡儀礼を手掛かりにする民俗探偵小説。"),
    ("ヴォティア語村落犯罪譚", "Votic village crime tale", "Votic village crime tale", "latin", "消滅危機言語の村落記憶を事件化するバルト周縁犯罪譚。"),
    # 2. Manuscript and chapbook genre traditions
    ("チャップブック夢占い譚", "Chapbook dream-divination tale", "chapbook dream-divination tale", "latin", "夢判断表と逸話を混ぜて安価に流通した小冊子物語。"),
    ("ブルターニュ青本聖者譚", "Breton blue-book saint tale", "livre bleu Breton", "latin", "青表紙廉価本で読まれた聖者奇跡譚のブルターニュ型。"),
    ("ルボーク怪物列伝", "Lubok monster catalogue tale", "лубочная чудовищная повесть", "cyrillic", "怪物図像と短い説話を結びつけたロシア民衆版画物語。"),
    ("ベンガル・バッタラ怪談本", "Battala ghost chapbook", "Battala bhuter boi", "latin", "カルカッタ廉価出版で流通したベンガル語怪談小冊子。"),
    ("ジャワ・スラット予言物語", "Javanese serat prophecy tale", "serat ramalan", "latin", "写本詩形で王権交替や災厄を語るジャワ予言物語。"),
    ("エチオピア魔除け巻物譚", "Ethiopian talismanic scroll tale", "ketab magical scroll narrative", "latin", "護符巻物の図像と短文が物語化するエチオピア写本伝統。"),
    # 3. Forgotten serial and magazine variants
    ("一銭蒸気船連載譚", "Penny steamboat serial", "penny steamboat serial", "latin", "河川蒸気船の事故と逃亡を連載化した廉価冒険小説。"),
    ("少年無線クラブ物語", "Boy wireless-club story", "wireless-club story", "latin", "無線通信趣味を少年探偵・救難筋へ結びつける雑誌物語。"),
    ("少女園芸クラブ物語", "Girl gardening-club story", "gardening-club story", "latin", "園芸クラブ活動を友情と地域改良に重ねる少女雑誌小説。"),
    ("植民地測量士ロマンス", "Colonial surveyor romance", "colonial surveyor romance", "latin", "測量旅行と婚姻筋を重ねる帝国周縁の職業ロマンス。"),
    ("タイプ鋳造工場怪談", "Type-foundry ghost story", "type-foundry ghost story", "latin", "活字鋳造所の労働音と事故記憶を怪異化する都市怪談。"),
    ("百貨店夜警スリラー", "Department-store night-watch thriller", "department-store night-watch thriller", "latin", "閉店後の売場と警備労働を舞台にする都市スリラー。"),
    # 4. Micro-SF and weird theory niches
    ("エーテル航路保険SF", "Ether-route insurance SF", "ether-route insurance SF", "latin", "宇宙航路保険と事故査定を筋にする初期科学ロマンス細分。"),
    ("菌糸通信惑星譚", "Mycelial telegraph planet tale", "mycelial telegraph planet tale", "latin", "菌糸ネットワークを惑星通信と社会秩序に見立てるSF。"),
    ("自動書記探偵ホラー", "Automatic-writing detective horror", "automatic-writing detective horror", "latin", "霊媒の自動書記を証拠と誤読の装置にする探偵怪奇譚。"),
    ("昆虫王国ユートピア", "Insect-kingdom utopia", "insect-kingdom utopia", "latin", "昆虫社会を理想国家や労働秩序の寓話にする空想小説。"),
    ("図書館閉架迷宮譚", "Closed-stack labyrinth tale", "closed-stack labyrinth tale", "latin", "閉架書庫を迷宮化し索引と記憶を恐怖化する書物幻想。"),
    ("気圧改造都市SF", "Barometric city-engineering SF", "barometric city-engineering SF", "latin", "気圧制御都市の生活と破綻を描く工学空想小説。"),
    # 5. Hyper-specific romance and domestic fiction
    ("女郵便飛行士ロマンス", "Woman airmail-pilot romance", "airmail-pilot romance", "latin", "航空郵便と女性操縦士の危険労働を恋愛筋に重ねる小説。"),
    ("温泉療養地求婚譚", "Spa-resort courtship tale", "spa-resort courtship tale", "latin", "療養地の滞在規則と身体回復を恋愛進行に使う大衆小説。"),
    ("帽子店見習い出世物語", "Milliner apprentice success tale", "milliner apprentice tale", "latin", "帽子店見習いの技能習得と階層上昇を描く都市職業譚。"),
    ("灯台島未亡人ロマンス", "Lighthouse-island widow romance", "lighthouse-island widow romance", "latin", "灯台島の喪失記憶と再婚を軸にする海辺ロマンス。"),
    ("貸本屋娘メロドラマ", "Lending-library daughter melodrama", "lending-library daughter melodrama", "latin", "貸本屋の読書回路と縁談を絡める家庭メロドラマ。"),
    ("共同洗濯場人情小説", "Communal-laundry heartwarmer", "communal-laundry heartwarmer", "latin", "共同洗濯場を噂・和解・縁結びの場にする温情小説。"),
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
