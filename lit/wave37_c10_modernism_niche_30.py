#!/usr/bin/env python3
"""Wave 37 cluster 10: lit_eu_modernism niche 30 concepts."""
import sqlite3

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"
SUBFIELD_ID = 10
PERIOD_ID = 22  # モダニズム期 西欧
REGION = "西欧"

CONCEPTS = [
    # 1: 英米モダニズム細部
    ("Pound Cantos LXXIV", "The Pisan Cantos LXXIV", "The Cantos LXXIV", "latin", "ピサ収容所体験を記す『ピサ詩篇』冒頭、断片化と記憶の交錯する長詩"),
    ("HD Trilogy", "H.D. Trilogy", "Trilogy", "latin", "H.D.が大戦下ロンドンで書いた三部詩、神話と密儀詩学の再生"),
    ("Mina Loy Lunar Baedeker", "Mina Loy Lunar Baedeker", "Lunar Baedeker", "latin", "ミナ・ロイの未来派的詩集、女性身体と都市を断片詩で描く"),
    ("Jean Toomer Cane", "Jean Toomer Cane", "Cane", "latin", "ハーレム・ルネサンスのジーン・トゥーマー、詩・散文・劇の混成形式作品"),
    ("Djuna Barnes Nightwood", "Djuna Barnes Nightwood", "Nightwood", "latin", "ジューナ・バーンズの夜の小説、クィア欲望と退廃のバロック散文"),
    ("Mary Butts Crystal Cabinet", "Mary Butts Crystal Cabinet", "The Crystal Cabinet", "latin", "メアリ・バッツの自伝、土地霊性と前衛の交差点を描く"),
    # 2: 仏前衛
    ("Apollinaire Calligrammes", "Apollinaire Calligrammes", "Calligrammes", "latin", "アポリネールの視覚詩集、活字配置で形象化する図形詩"),
    ("Cendrars Prose Transsibérien", "Cendrars La Prose du Transsibérien", "La Prose du Transsibérien", "latin", "サンドラールとドローネー協作の長尺折本詩、シベリア鉄道叙事"),
    ("Reverdy Plupart temps", "Reverdy La plupart du temps", "La plupart du temps", "latin", "ルヴェルディの詩集、空白と省略によるキュビスム詩学"),
    ("Larbaud Barnabooth", "Valery Larbaud Barnabooth", "A.O. Barnabooth", "latin", "ラルボーの仮名詩人バルナブース、コスモポリタン旅行詩"),
    ("Ramuz Histoire soldat", "Ramuz Histoire du soldat", "Histoire du soldat", "latin", "ラミュ台本、ストラヴィンスキー音楽の語り物舞台詩劇"),
    ("Jouve Sueur sang", "Jouve Sueur de sang", "Sueur de sang", "latin", "ピエール・ジューヴの詩集、精神分析と神秘の暗黒詩学"),
    # 3: 独墺前衛
    ("Trakl Grodek", "Trakl Grodek", "Grodek", "latin", "トラークル絶筆詩、第一次大戦戦場の死の詠嘆"),
    ("Heym Umbra Vitae", "Georg Heym Umbra Vitae", "Umbra Vitae", "latin", "ゲオルク・ハイムの詩集、表現主義都市黙示録"),
    ("Stramm Patrouille", "August Stramm Patrouille", "Patrouille", "latin", "シュトラム極限圧縮詩、戦場のスタッカート言語実験"),
    ("Schwitters Ursonate", "Schwitters Ursonate", "Ursonate", "latin", "シュヴィッタースの音響詩、無意味音節による原初ソナタ"),
    ("Ball Karawane", "Hugo Ball Karawane", "Karawane", "latin", "フーゴ・バルのダダ音響詩、キャバレー・ヴォルテール初演"),
    ("Arp wolkenpumpe", "Arp Die Wolkenpumpe", "Die Wolkenpumpe", "latin", "ハンス・アルプのダダ詩集、自動筆記と偶然の言語"),
    # 4: 露モダニズム
    ("Khlebnikov Zangezi", "Khlebnikov Zangezi", "Зангези", "cyrillic", "フレーブニコフの超言語劇詩、ザンゲジによる星の言語"),
    ("Mayakovsky Bedbug", "Mayakovsky The Bedbug", "Клоп", "cyrillic", "マヤコフスキー諷刺劇『南京虫』、ソヴィエト未来戯画"),
    ("Tsvetaeva Crysolite", "Tsvetaeva Poem of the End", "Поэма Конца", "cyrillic", "ツヴェターエワ『終りの詩』、別離の極限詩"),
    ("Mandelstam Tristia", "Mandelstam Tristia", "Tristia", "cyrillic", "マンデリシュタームの詩集、アクメイズム古典回帰の哀歌"),
    ("Pasternak Sister Life", "Pasternak My Sister Life", "Сестра моя — жизнь", "cyrillic", "パステルナーク詩集『わが妹なる生』、自然と革命の抒情"),
    ("Kuzmin Wings", "Kuzmin Wings", "Крылья", "cyrillic", "クズミン小説『翼』、ロシア初の同性愛公然小説"),
    # 5: 中欧南欧
    ("Pessoa Heteronyms theory", "Pessoa Heteronyms theory", "heterónimos", "latin", "ペソアの異名理論、複数仮構詩人による多声的詩学"),
    ("Hašek Švejk", "Hašek The Good Soldier Švejk", "Osudy dobrého vojáka Švejka", "latin", "ハシェクの兵士シュヴェイクもの、反戦諷刺長篇"),
    ("Karel Čapek RUR", "Karel Čapek R.U.R.", "R.U.R.", "latin", "チャペックの戯曲、ロボット概念を導入した未来劇"),
    ("Witkacy Pure Form", "Witkiewicz Pure Form theory", "Czysta Forma", "latin", "ヴィトカツィの純粋形式論、形而上感覚を喚起する前衛劇理論"),
    ("Bruno Schulz Cinnamon", "Bruno Schulz Cinnamon Shops", "Sklepy cynamonowe", "latin", "シュルツ短篇集『肉桂色の店』、神話的少年期幻想"),
    ("Stanisław Witkiewicz Insatiability", "Witkiewicz Insatiability", "Nienasycenie", "latin", "ヴィトカツィ反ユートピア小説『飽くことなき』、東洋侵攻の終末劇"),
]

def main():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, defi in CONCEPTS:
        try:
            c.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition, importance_score)
                VALUES (?,?,?,?,?,?,?,?,?)
            """, (name_ja, name_en, name_orig, script, SUBFIELD_ID, REGION, PERIOD_ID, defi, 3))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    conn.close()
    print(f"INSERTED={inserted} SKIPPED={skipped}")

if __name__ == "__main__":
    main()
