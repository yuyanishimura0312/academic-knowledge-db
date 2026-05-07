from lit_db_helper import LitDB


ROWS = [
    # 1. French documentary surfaces
    ("パリ古着屋値札の階級読解", "Parisian secondhand price-tag class reading", 120, "古着屋の値札で没落階級と虚栄の距離を示す細部。"),
    ("地方駅待合室の新聞回覧", "Provincial station newspaper circulation", 120, "駅待合室の回覧新聞で噂と政治温度を測る場面型。"),
    ("家財差押え目録の心理化", "Psychologized distraint inventory", 120, "差押え目録を羞恥と家族崩壊の内面記録に変える技法。"),
    ("料理献立表の姦通暗号", "Menu adultery code", 120, "献立の選択で密会費用と欲望の節度を暗示する小道具。"),
    ("県庁廊下の待機描写", "Prefecture-corridor waiting scene", 120, "県庁廊下の待機で地方官僚制の鈍さを描く場面。"),
    ("葬儀香典帳の社交序列", "Funeral condolence-ledger hierarchy", 120, "香典帳の名順と金額で町の社交序列を読む技法。"),

    # 2. British institutional minutiae
    ("貸馬車乗場の相続情報網", "Cab-rank inheritance information network", 121, "貸馬車乗場の噂で遺産と婚姻の情報流通を示す場面。"),
    ("日曜学校賞状の道徳演出", "Sunday-school prize moral staging", 121, "賞状授与で慈善家の視線と児童の服従を演出する細部。"),
    ("鉄道手荷物札の誤配筋", "Railway luggage-label misdelivery plot", 121, "手荷物札の誤配で身分錯誤と偶然を現実化する筋。"),
    ("下宿朝食卓の沈黙配列", "Boarding-house breakfast silence array", 121, "朝食卓の席順と沈黙で下宿人の階層差を示す描写。"),
    ("救貧監督官の訪問記録", "Poor-law inspector visit record", 121, "訪問記録の文体で貧困家庭を制度の対象に変える技法。"),
    ("牧師館ピアノ譜面の求婚圧", "Parsonage piano-score courtship pressure", 121, "譜面選びで求婚期待と家庭教養の圧を示す場面。"),

    # 3. Germanic legal and rural objects
    ("村裁判所ベンチの証言配置", "Village-court bench testimony layout", 173, "法廷ベンチの位置で村落内の力関係を可視化する技法。"),
    ("家畜売買証書のノヴェレ化", "Livestock bill-of-sale Novelle device", 173, "家畜売買証書を婚姻・負債・名誉の結節点にする筋。"),
    ("小駅貨物台帳の地方時間", "Small-station freight ledger temporality", 173, "貨物台帳の遅延で地方社会の時間差を測る細部。"),
    ("教会席札の身分境界", "Church pew-card status boundary", 173, "教会席札で家格と共同体内の排除を示す小道具。"),
    ("山村郵便袋の遅延焦点", "Mountain mailbag delay focal point", 173, "郵便袋の遅れを知らせと悲劇の焦点にする構成。"),
    ("湯治宿請求書の欲望計算", "Spa-inn invoice desire calculus", 173, "湯治宿の請求書で恋愛と家計不安を同時に示す細部。"),

    # 4. Iberian and Italian local economies
    ("質屋札束の母娘自然主義", "Pawn-ticket mother-daughter naturalism", 172, "質屋札束で母娘の貧困継承を物証化する描写。"),
    ("港湾積荷票の欲望地理", "Harbor cargo-slip geography of desire", 172, "積荷票で植民地商品と都市欲望の接点を示す細部。"),
    ("オリーブ搾油場の群集焦点", "Olive-press crowd focalization", 172, "搾油場の労働音を共同体の群集焦点にする場面。"),
    ("漁村聖像行列の負債劇", "Fishing-village icon procession debt drama", 171, "聖像行列を漁師家族の負債と名誉の劇に変える筋。"),
    ("葡萄収穫帳の季節決定論", "Vintage ledger seasonal determinism", 172, "収穫帳で労働周期と家族運命を結びつける技法。"),
    ("共同井戸待ち列の噂合唱", "Communal-well queue rumor chorus", 171, "井戸待ち列の会話で村の監視と噂を合唱化する話法。"),

    # 5. Naturalist observation and threshold optics
    ("医院待合室の症候群配置", "Clinic waiting-room syndrome layout", 122, "待合室の患者配置で遺伝・環境・貧困を並置する技法。"),
    ("屠畜場検印の身体記号", "Slaughterhouse stamp body sign", 122, "検印を労働身体と商品化の境界記号にする細部。"),
    ("写真館背景幕の社会偽装", "Studio backdrop social disguise", 123, "写真館の背景幕で人物の身分演技を露呈させる装置。"),
    ("街灯点灯夫の焦点移動", "Lamplighter focal shift", 123, "点灯夫の移動で街区ごとの視点を滑らせる場面転換。"),
    ("昆虫標本箱の家族比喩", "Insect-case family metaphor", 122, "標本箱を家族分類と退化観察の比喩にする技法。"),
    ("劇場切符半券の記憶痕", "Theater ticket-stub memory trace", 174, "半券を欲望・消費・回想の物質的痕跡にする細部。"),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        for name_ja, name_en, period_id, definition in ROWS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_eu_realism",
                region="西欧",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )
        db.conn.commit()


if __name__ == "__main__":
    main()
