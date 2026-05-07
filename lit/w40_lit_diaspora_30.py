from lit_db_helper import LitDB


CONCEPTS = [
    # 1. Indian Ocean micro-diasporas
    ("ハドラミー・マウリド写本圏", "Hadhrami mawlid manuscript circuit", "ディアスポラ", 166, "東アフリカ・東南アジアを巡るハドラミー系預言者讃歌写本網。"),
    ("スワヒリ・アラビア文字移民詩", "Swahili Ajami migrant poetry", "ディアスポラ", 166, "アジャミ表記で港市移動を歌うスワヒリ語詩の小伝統。"),
    ("マプラー・パーダパットゥ移民歌", "Mappila padappattu migrant song", "ディアスポラ", 166, "マラバール海民の移動記憶を含むマプラー戦歌・航海歌。"),
    ("ボーラ商人書簡物語", "Bohra merchant epistolary tale", "ディアスポラ", 166, "グジャラート商人の家族書簡から生まれる散文的移民語り。"),
    ("ザンジバル・グジャラート印刷圏", "Zanzibar Gujarati print sphere", "ディアスポラ", 166, "ザンジバルのグジャラート語新聞・小冊子が作る移民公共圏。"),
    ("コモロ・シラジ系譜詩", "Comorian Shirazi genealogy verse", "ディアスポラ", 166, "シラジ起源を韻文化で語るコモロ系譜詩の伝統。"),
    # 2. Sephardi and Judeo-language survivals
    ("ラディーノ・コプラ移民歌", "Ladino kopla migrant song", "ディアスポラ", 166, "セファルディ離散の祝祭・嘆きを歌うラディーノ連詩。"),
    ("ジュデオ・アラビア語ゲニザ書簡文学", "Judeo-Arabic Geniza letter literature", "ディアスポラ", 166, "カイロ・ゲニザ書簡に残る商旅と家族分離の散文文化。"),
    ("ブハラ・ユダヤ・バイト詩", "Bukharan Jewish bait poetry", "ディアスポラ", 166, "ペルシア語系バイトで移住と儀礼を歌うブハラ・ユダヤ詩。"),
    ("イタルキーム・ピユート亡命譜", "Italki piyyut exile repertory", "ディアスポラ", 166, "イタリア系ユダヤ礼拝詩に刻まれた追放と寄留の譜系。"),
    ("カライム語キナー写本", "Karaim qinah manuscripts", "ディアスポラ", 166, "クリミア・リトアニアのカライム語哀歌写本伝統。"),
    ("ユダヤ・タート語移住短編", "Judeo-Tat migrant short fiction", "ディアスポラ", 167, "山岳ユダヤ人の移住経験を描くユダヤ・タート語短編。"),
    # 3. Black Atlantic marginal archives
    ("クリオ語ブロードサイド哀歌", "Krio broadside elegy", "ディアスポラ", 167, "シエラレオネの印刷ビラに載る解放奴隷系哀歌。"),
    ("ガリフナ・ドゥグ詠唱譚", "Garifuna dugu chant narrative", "ディアスポラ", 167, "祖霊儀礼ドゥグに接続するガリフナ語の移動記憶譚。"),
    ("グッラー聖歌説話", "Gullah spiritual tale", "ディアスポラ", 167, "海島クレオール共同体の霊歌と説話が交差する語り。"),
    ("サラマカ口承マルーン年代記", "Saramaka oral maroon chronicle", "ディアスポラ", 167, "逃亡奴隷共同体の戦争・移動を伝えるサラマカ口承史。"),
    ("ニグロ・キュラソー詩", "Curaçao Negritude verse", "ディアスポラ", 167, "パピアメント語で黒人性と島外移動を問う小詩系譜。"),
    ("ブラック・ノヴァスコシア捕囚説話", "Black Nova Scotian captivity tale", "ディアスポラ", 167, "ロイヤリスト系黒人入植者の移住・拘束を語る地域説話。"),
    # 4. East/Central European minor diasporas
    ("アルブレシュ叙事歌", "Arbëresh epic song", "ディアスポラ", 166, "南伊アルバニア系共同体に残る亡命起源の叙事歌。"),
    ("ブルゲンラント・クロアチア移民劇", "Burgenland Croatian migrant drama", "ディアスポラ", 167, "国境地帯クロアチア語共同体の移住と同化を描く小演劇。"),
    ("ルシン離散新聞連載小説", "Rusyn diaspora newspaper serial", "ディアスポラ", 167, "米国ルシン新聞に連載された出稼ぎ・帰郷小説。"),
    ("ソルブ語移民暦物語", "Sorbian migrant almanac tale", "ディアスポラ", 167, "ソルブ語暦本に載る鉱山移民と村落記憶の短話。"),
    ("ポントス・ギリシア嘆き歌", "Pontic Greek lament song", "ディアスポラ", 167, "黒海ギリシア人追放をポントス方言で歌う哀歌。"),
    ("クリミア・タタール・スルギュン詩", "Crimean Tatar Sürgün poetry", "ディアスポラ", 167, "強制移住スルギュンの記憶を刻むクリミア・タタール詩。"),
    # 5. Micro-debates and digital manuscript afterlives
    ("亡命余白注釈", "exilic marginalia", "ディアスポラ", 168, "移民蔵書の余白書き込みを離散的読書として読む概念。"),
    ("帰還不能方言論争", "unreturnable dialect debate", "ディアスポラ", 168, "継承語方言を本国基準で直すべきかをめぐる小論争。"),
    ("二世翻字アクセント", "second-generation transliteration accent", "ディアスポラ", 168, "二世作家の翻字揺れを発音記憶として読む視点。"),
    ("越境同人誌ディアスポラ", "transborder zine diaspora", "ディアスポラ", 168, "移民コミュニティ同人誌が作る小規模な越境文学圏。"),
    ("難民PDFサミズダート", "refugee PDF samizdat", "ディアスポラ", 168, "亡命者がPDFで流通させる非公式出版と検閲回避の形態。"),
    ("継承語校正の暴力", "heritage-language copyediting violence", "ディアスポラ", 168, "移民語の揺れを編集が標準化する際の喪失を問う概念。"),
]


def main() -> None:
    with LitDB() as db:
        for name_ja, name_en, region, period_id, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_diaspora",
                region=region,
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )


if __name__ == "__main__":
    main()
