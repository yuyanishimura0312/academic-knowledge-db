from __future__ import annotations

from lit_db_helper import LitDB, LitDBError


SUBFIELD = "lit_africa"
REGION = "アフリカ"


CONCEPTS: list[dict] = [
    # 1. アフリカ詩細部
    dict(name_ja="オキグボ『ヘヴンズゲート』", name_en="Christopher Okigbo, Heavensgate",
         definition="イボ霊性とモダニズムの断片詩法が交差する初期詩篇。"),
    dict(name_ja="オスンダレ『市場の歌』", name_en="Niyi Osundare, Songs of the Marketplace",
         definition="市場の声を民主的詩語へ変えるヨルバ系英語詩集。"),
    dict(name_ja="アウォーノル『約束と希望』", name_en="Kofi Awoonor, The Promise of Hope",
         definition="エウェ哀歌形式で亡命、祖国、死者への呼びかけを編む詩集。"),
    dict(name_ja="マパンジェ『縄なしで跳ぶ』", name_en="Jack Mapanje, Skipping Without Ropes",
         definition="検閲後のマラウイ政治を諷刺と寓意で刻む獄中以後の詩。"),
    dict(name_ja="オカラ『声』", name_en="Gabriel Okara, The Voice",
         definition="イジョ語的構文で内なる声と共同体倫理を小説化する実験作。"),
    dict(name_ja="コジョ・レイン『甘い国を探して』", name_en="Kojo Laing, Search Sweet Country",
         definition="ガーナ都市を多言語的ナンセンスと寓話で再編する小説。"),

    # 2. スワヒリ・アフリカ言語文学
    dict(name_ja="シャアバン・ロバート『クサディキカ』", name_en="Shaaban Robert, Kusadikika",
         definition="架空国家裁判を通じて正義と統治を問うスワヒリ語寓話小説。"),
    dict(name_ja="ケジラハビ『キチュワマジ』", name_en="Euphrase Kezilahabi, Kichwamaji",
         definition="実存的不安と社会停滞をスワヒリ語散文で描くタンザニア小説。"),
    dict(name_ja="サイド・モハメド『アサリ』", name_en="Said Mohamed, Asali",
         definition="ザンジバル的記憶と権力批判を凝縮するスワヒリ語小説。"),
    dict(name_ja="ンギュギ『マティガリ』ギクユ語版", name_en="Ngugi wa Thiong'o, Matigari in Gikuyu",
         definition="ギクユ語で植民地後の正義探求を寓話化した抵抗小説。"),
    dict(name_ja="セティロアネのソト語神学詩", name_en="Gabriel Setiloane Sotho writing",
         definition="ソト語的霊性を詩的神学へ移す南部アフリカ表現。"),
    dict(name_ja="セローテのソト語響き", name_en="Wally Mongane Serote Sotho resonance",
         definition="英語詩にソト語の呼吸と反アパルトヘイト声調を響かせる技法。"),

    # 3. ハウサ・ヨルバ文学
    dict(name_ja="ファグンワ『森の勇士』", name_en="D. O. Fagunwa, Ogboju Ode Ninu Igbo Irunmale",
         definition="ヨルバ語で精霊森の冒険を長編化した先駆的幻想小説。"),
    dict(name_ja="アキンウミ・イソラのヨルバ小説", name_en="Akinwumi Isola Yoruba novel",
         definition="ヨルバ語で都市倫理、家族、近代化を描く教育的長編群。"),
    dict(name_ja="アブバカル・イマム『マガナ・ジャリ・チェ』", name_en="Abubakar Imam, Magana Jari Ce",
         definition="説話集形式でハウサ語散文の教訓性と娯楽性を確立した作品。"),
    dict(name_ja="ハウサ語ロマンス文学", name_en="Hausa romance literature",
         definition="カノ市場圏で恋愛、結婚、都市生活を扱う大衆小説潮流。"),
    dict(name_ja="ヨルバ・オペラ劇", name_en="Yoruba operatic theatre",
         definition="歌、舞踊、巡業劇を融合し都市観客へ届いたヨルバ演劇形式。"),
    dict(name_ja="マリ『スンジャタ』口承叙事詩", name_en="Oral epic of Sundiata",
         definition="グリオが王権起源とマンデ共同体記憶を語り継ぐ英雄叙事詩。"),

    # 4. コンゴ盆地・大湖地域
    dict(name_ja="ソニー・ラブー・タンシ『反人民』", name_en="Sony Labou Tansi, L'Antipeuple",
         definition="独裁国家の暴力をグロテスクな笑いで解体するコンゴ小説。"),
    dict(name_ja="アンリ・ロペス『泣き笑い』", name_en="Henri Lopes, Le Pleurer-rire",
         definition="架空独裁者の言語劇で政治茶番と語りの信頼性を崩す小説。"),
    dict(name_ja="チカヤ・ユ・タンシ『腹』", name_en="Tchicaya U Tam'si, Le Ventre",
         definition="身体、飢え、植民地後の傷を濃密な比喩で刻むコンゴ詩。"),
    dict(name_ja="ドンガラ『集合写真』", name_en="Emmanuel Dongala, Photo de groupe",
         definition="革命と失望の記憶を群像的視点で写し取るコンゴ短編的表現。"),
    dict(name_ja="ガトレ『過去の前方』", name_en="Gilbert Gatore, The Past Ahead",
         definition="ルワンダ虐殺後の罪責と沈黙を断片的に追う小説。"),
    dict(name_ja="ムカソンガ『ゴキブリ』", name_en="Scholastique Mukasonga, Cockroaches",
         definition="ツチ迫害の家族記憶を証言文学として刻むルワンダ回想録。"),

    # 5. 移民系アフリカ詩
    dict(name_ja="ワルサン・シャイア『母への教え』", name_en="Warsan Shire, Teaching My Mother How to Give Birth",
         definition="ソマリ離散女性の身体、戦争、家族記憶を鋭く語る詩集。"),
    dict(name_ja="イルサ・デイリー＝ウォード『骨』", name_en="Yrsa Daley-Ward, Bone",
         definition="西インド系アフリカ離散の身体感覚と欲望を短詩で綴る詩集。"),
    dict(name_ja="イヌア・エラムズ『ラプソディ』", name_en="Inua Ellams, Rhapsody",
         definition="ナイジェリア系英国詩の都市音楽性と移動感覚を凝縮する作品。"),
    dict(name_ja="ヘロン・ハビラ『旅人たち』", name_en="Helon Habila, Travellers",
         definition="欧州滞在アフリカ人の亡命、難民性、芸術を連作的に描く小説。"),
    dict(name_ja="イムボロ・ムブエ『見よ、夢見る者たちを』", name_en="Imbolo Mbue, Behold the Dreamers",
         definition="カメルーン移民家族と米金融危機を重ねるディアスポラ小説。"),
    dict(name_ja="トペ・フォラリン『希望の近さ』", name_en="Tope Folarin, A Particular Kind of Black Man",
         definition="ナイジェリア系米国少年の同化、家族、黒人性を問う小説。"),
]


def main() -> int:
    if len(CONCEPTS) != 30:
        raise SystemExit(f"expected 30 concepts, got {len(CONCEPTS)}")
    for entry in CONCEPTS:
        if len(entry["definition"]) > 100:
            raise SystemExit(f"definition too long: {entry['name_ja']}")

    inserted = 0
    with LitDB() as db:
        for raw in CONCEPTS:
            entry = {
                **raw,
                "subfield_code": SUBFIELD,
                "region": REGION,
                "period_id": None,
                "original_script": "roman",
                "importance_score": 3,
                "source_tier": "secondary",
                "canonical_in_region": "minor",
            }
            try:
                db.insert_concept(**entry)
                inserted += 1
            except LitDBError as exc:
                print(f"[error] {entry['name_ja']}: {exc}")
    print(f"inserted_or_existing={inserted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
