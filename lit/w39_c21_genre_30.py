#!/usr/bin/env python3
"""Wave 39: add 30 ultra-niche lit_genre concepts."""

from lit_db_helper import LitDB, LitDBError

CONCEPTS = [
    # 1. 地域小語圏ミステリ
    ("フェロー諸島ノワール", "Faroese noir", "Faroese noir", "latin", "北大西洋の島嶼共同体を舞台にした少数語圏ノワール。"),
    ("アイスランド村落ミステリ", "Icelandic village mystery", "íslensk sveitakrimmi", "latin", "孤立集落の血縁と土地記憶を謎解きに絡めるアイスランド小説型。"),
    ("フリースラント探偵小説", "Frisian detective fiction", "Fryske detektive", "latin", "フリジア語圏の地方性を前景化する低流通ミステリ。"),
    ("ソルブ語犯罪小説", "Sorbian crime fiction", "serbska kriminalka", "latin", "ドイツ東部ソルブ語共同体を舞台にする少数民族犯罪小説。"),
    ("ウェールズ語警察小説", "Welsh-language police novel", "nofel heddlu Gymraeg", "latin", "ウェールズ語で地域警察と二言語社会を描く警察小説。"),
    ("サーミ・アークティック・スリラー", "Sami Arctic thriller", "Sámi Arctic thriller", "latin", "サーミ社会と北極圏資源問題を絡めた寒冷地スリラー。"),
    # 2. 忘れられた冒険・植民地周縁
    ("少年帝国ロビンソナード", "Boys' empire robinsonade", "boys' empire robinsonade", "latin", "少年雑誌で帝国開拓を漂流物語に変換したロビンソナード変種。"),
    ("プランテーション・ゴシック", "Plantation Gothic", "Plantation Gothic", "latin", "奴隷制の残響を屋敷怪異に刻む米南部ゴシック下位型。"),
    ("ジャングル・ロマンス", "Jungle romance", "jungle romance", "latin", "熱帯奥地を恋愛・冒険・植民地幻想の舞台にする大衆小説型。"),
    ("リーフ・フィクション", "Reef fiction", "reef fiction", "latin", "珊瑚礁・難破・島嶼交易を核にする南洋冒険小説の細分。"),
    ("駅馬車ウェスタン短編", "Stagecoach Western short story", "stagecoach western", "latin", "駅馬車襲撃と街道空間に特化した西部劇短編の定型。"),
    ("ダイムノベル海賊譚", "Dime-novel pirate tale", "dime-novel pirate tale", "latin", "廉価冊子で流通した海賊冒険譚の扇情的サブジャンル。"),
    # 3. 児童・少女雑誌の隠れ形式
    ("孤児院学校物語", "Orphanage school story", "orphanage school story", "latin", "寄宿学校物語を孤児院制度へ移した児童文学の忘れられた型。"),
    ("お転婆少女冒険譚", "Tomboy adventure tale", "tomboy adventure tale", "latin", "少女主人公の逸脱行動と屋外冒険を売りにした少女雑誌小説。"),
    ("日曜学校リワードブック", "Sunday-school reward book", "Sunday-school reward book", "latin", "善行褒賞として配布された教訓的児童小説の出版ジャンル。"),
    ("瀕死児童センチメンタル", "Dying-child sentimental tale", "dying-child tale", "latin", "幼い死を信仰・涙・家庭徳目へ結ぶヴィクトリア朝児童物語。"),
    ("ゴリウォグ絵本系譜", "Golliwog picture-book tradition", "Golliwog books", "latin", "人種化された人形像を反復した問題含みの英語圏絵本系譜。"),
    ("少女探偵クラブ物語", "Girls' detective club story", "girls' detective club story", "latin", "少女集団の暗号・尾行・校内捜査を描く児童探偵小説型。"),
    # 4. パルプSF・奇想雑誌の変種
    ("シャンブロウ型惑星ロマンス", "Shambleau-type planetary romance", "Shambleau planetary romance", "latin", "異星の官能的脅威を惑星冒険に組み込むパルプSF変種。"),
    ("剣と惑星もの", "Sword and planet", "sword and planet", "latin", "剣戟冒険を異星舞台へ移植する惑星ロマンス下位ジャンル。"),
    ("エディソネード", "Edisonade", "Edisonade", "latin", "少年発明家が機械で冒険と征服を進める初期SF冒険型。"),
    ("ビッグ・ダム・オブジェクトSF", "Big Dumb Object SF", "Big Dumb Object", "latin", "巨大人工物の探索を核にするセンス・オブ・ワンダー系SF。"),
    ("クラークスワールド型フラッシュSF", "Flash SF magazine fiction", "flash science fiction", "latin", "ウェブ雑誌で流通する短尺高密度の現代SF形式。"),
    ("菌類ホラーSF", "Fungal horror SF", "fungal horror", "latin", "菌糸・胞子・寄生を恐怖と進化想像に使うSFホラー細分。"),
    # 5. ロマンス・女性大衆小説の細部
    ("医師看護師ロマンス", "Doctor-nurse romance", "doctor-nurse romance", "latin", "病院階層とケア労働を恋愛定型に組み込む職業ロマンス。"),
    ("シーク・ロマンス", "Sheikh romance", "sheikh romance", "latin", "砂漠の支配者男性像を中心にしたオリエンタリズム的ロマンス。"),
    ("ミルズ&ブーン医療ライン", "Mills & Boon medical line", "Mills & Boon Medical", "latin", "医療職場を舞台にしたMills & Boonの専門ロマンス系列。"),
    ("ガヴァネス・ロマンス", "Governess romance", "governess romance", "latin", "家庭教師女性の階級移動と恋愛を描く歴史ロマンス下位型。"),
    ("ウェイトレス・サクセス・ロマンス", "Waitress success romance", "waitress success romance", "latin", "低賃金女性の上昇婚と自立を絡める20世紀大衆ロマンス型。"),
    ("郵便花嫁西部ロマンス", "Mail-order bride Western romance", "mail-order bride Western romance", "latin", "通信結婚と辺境共同体形成を組み合わせる西部ロマンス細分。"),
]


def main() -> None:
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        existing = {
            row[0]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 21"
            )
        }
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            if name_ja in existing:
                skipped += 1
                continue
            try:
                db.insert_concept(
                    name_ja=name_ja,
                    name_en=name_en,
                    name_original=name_original,
                    original_script=script,
                    subfield_code="lit_genre",
                    region="横断",
                    period_id=None,
                    definition=definition,
                    importance_score=2,
                    source_tier="secondary",
                    canonical_in_region="marginal",
                )
                inserted += 1
            except LitDBError as exc:
                skipped += 1
                print(f"SKIP {name_ja}: {exc}")
    print(f"inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
