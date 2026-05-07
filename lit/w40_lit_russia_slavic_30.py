#!/usr/bin/env python3
"""Wave 40 C18: 30 hyper-niche Russia/Slavic concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD = "lit_russia_slavic"
REGION = "東欧・ロシア"

P_MED_SLAV = 220
P_SENT = 200
P_ROM = 201
P_GOLD = 291
P_REAL = 202
P_SILVER = 203
P_FORM = 204
P_BALKAN = 211

CONCEPTS = [
    # Manuscript and Church Slavonic micro-traditions
    ("ノヴゴロド第一年代記若年編集", "Novgorod First Chronicle Younger Redaction", "Новгородская первая летопись младшего извода", "cyrillic", P_MED_SLAV, "ノヴゴロド都市記憶を保つ後期年代記写本系統。"),
    ("トルコヴァヤ・パレヤ写本群", "Explanatory Paleia manuscript tradition", "Толковая Палея", "cyrillic", P_MED_SLAV, "聖書外典と注解を編む中世スラヴ百科的叙述。"),
    ("メリロ・プラヴェドノエ断章", "Merilo Pravednoe fragments", "Мерило Праведное", "cyrillic", P_MED_SLAV, "法規範と教訓を併せたルーシ道徳法文集。"),
    ("ストゴラフ問答文体", "Stoglav question-answer style", "Стоглав", "cyrillic", P_MED_SLAV, "一五五一年教会会議録の問答型規範叙述。"),
    ("ヴェリキエ・ミネイ・チェチイ編纂", "Great Menaion Reader compilation", "Великие Минеи Четьи", "cyrillic", P_MED_SLAV, "月別聖人伝を巨大化したマカリイ府主教の編纂事業。"),
    ("ホジェーニエ商人記の信仰逸脱", "Merchant hozhenie confessional drift", "хожение", "cyrillic", P_MED_SLAV, "巡礼記が商旅と異教観察へずれる叙述型。"),

    # Provincial and imperial-edge prose
    ("ナリェージヌィ『ロシアのジルブラス』", "Narezhny Russian Gil Blas", "Российский Жилблаз", "cyrillic", P_SENT, "ピカレスク形式で地方官僚社会を諷刺した初期長編。"),
    ("ブルガーリン『イワン・ヴィジギン』", "Bulgarin Ivan Vyzhigin", "Иван Выжигин", "cyrillic", P_ROM, "保守的冒険譚として読まれた初期大衆小説。"),
    ("ラジェチニコフ『氷の家』", "Lazhechnikov Ice House", "Ледяной дом", "cyrillic", P_GOLD, "アンナ女帝期を舞台にした忘れられた歴史小説。"),
    ("ザゴスキン『ユーリー・ミロスラフスキー』", "Zagoskin Yuri Miloslavsky", "Юрий Милославский", "cyrillic", P_ROM, "動乱時代を国民叙事化した初期歴史ロマンス。"),
    ("ベストゥージェフ＝マルリンスキー海洋譚", "Bestuzhev-Marlinsky sea tales", "морские повести", "cyrillic", P_ROM, "士官経験に基づく海戦と冒険のロマン派短編群。"),
    ("ソフィヤ・コヴァレフスカヤ『ニヒリストの娘』", "Kovalevskaya A Nihilist Girl", "Нигилистка", "cyrillic", P_REAL, "女性知識人の政治選択を描く亡命期中編。"),

    # Minor Slavic regional revivals
    ("カシューブ語『レムスの生涯と冒険』", "Kashubian Remus", "Żëcé i przigòdë Remùsa", "latin", P_BALKAN, "カシューブ語で民族覚醒を寓話化した地方長編。"),
    ("ソルブ語『セルプスキ・ノヴィニ』文学欄", "Sorbian Serbske Nowiny literary column", "Serbske Nowiny", "latin", P_BALKAN, "少数言語新聞が担った詩と散文の掲載圏。"),
    ("ルシン語『ドゥフノーヴィチ劇』", "Rusyn Dukhnovych drama", "Добродѣтель превышает богатство", "cyrillic", P_BALKAN, "ルシン啓蒙運動で上演された教訓劇。"),
    ("プレシェーレン『洗礼』ボグミル論", "Preseren Baptism Bogomila debate", "Krst pri Savici", "latin", P_BALKAN, "スロヴェニア叙事詩のヒロイン解釈をめぐる小論点。"),
    ("カイ方言クロアチア詩", "Kajkavian Croatian verse", "kajkavska poezija", "latin", P_BALKAN, "標準語外のカイ方言で続いた地方抒情詩。"),
    ("モンテネグロ十音節英雄歌", "Montenegrin decasyllabic heroic song", "junačke pjesme", "latin", P_BALKAN, "グスレ伴奏で伝承された部族英雄歌の型。"),

    # Silver Age side currents and tiny circles
    ("アレクサンドル・ドブロリューボフ沈黙詩学", "Alexander Dobrolyubov poetics of silence", "поэтика молчания", "cyrillic", P_SILVER, "象徴派詩人の離脱と沈黙をめぐる聖性読解。"),
    ("ムサゲート出版社神智学圏", "Musaget theosophical publishing circle", "Мусагет", "cyrillic", P_SILVER, "象徴主義と神智学を結んだ小出版社ネットワーク。"),
    ("『ヴェスィ』書評戦争", "Vesy review polemics", "Весы", "cyrillic", P_SILVER, "象徴派誌の書評欄で展開した詩壇内抗争。"),
    ("クズミーン『美しき明晰性』", "Kuzmin beautiful clarity", "прекрасная ясность", "cyrillic", P_SILVER, "アクメイズム前史に置かれる小さな反象徴主義綱領。"),
    ("ニーナ・ペトロフスカヤ『サンクトゥス・アモール』", "Nina Petrovskaya Sanctus Amor", "Sanctus Amor", "latin", P_SILVER, "象徴派サロンの愛と破滅を映す短編集。"),
    ("ロシア・イマジニスト雑誌『ホテル』", "Russian Imaginist journal Gostinitsa", "Гостиница для путешествующих в прекрасном", "cyrillic", P_SILVER, "短命イマジニスト誌に残る比喩論と同人詩。"),

    # Formalist and Soviet micro-debates
    ("リテラトゥルナヤ・ガゼータ形式主義討伐", "Literaturnaya Gazeta anti-formalist campaign", "Литературная газета", "cyrillic", P_FORM, "一九三〇年代初頭の形式主義批判記事群。"),
    ("ルィトモロギヤ韻律統計論", "Russian rhythmology metrics debate", "ритмология", "cyrillic", P_FORM, "詩行リズムを統計化するフォルマリズム周辺論争。"),
    ("ペレヴェルゼフ社会生成論", "Pereverzev social genesis theory", "социальный генезис", "cyrillic", P_FORM, "文学人物を階級心理から読む初期マルクス主義批評。"),
    ("ナップ『オン・ポストゥ』路線", "Na postu RAPP line", "На посту", "cyrillic", P_FORM, "ラップ系誌が掲げた党派的文学統制の攻撃文体。"),
    ("『文学的現代』同伴者論", "Literary Contemporary fellow-traveller debate", "Литературный современник", "cyrillic", P_FORM, "革命同伴作家の位置づけを争う雑誌論争。"),
    ("ロツィヤーノフ版プーシキン注釈", "Lotsianov Pushkin commentary", "пушкинский комментарий", "cyrillic", P_FORM, "本文異同と注釈方法をめぐるソ連初期プーシキン学。"),
]


def main() -> None:
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, script, period_id, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            before = db.find_concept(name_ja, REGION, period_id)
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            if before is None:
                inserted += 1
    print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
