#!/usr/bin/env python3
"""Wave 38: lit_cn_modern (subfield_id=9) +30 concepts, 5 clusters x 6."""
import sqlite3, os

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"
SUBFIELD_ID = 9
REGION = "東アジア"
PERIOD_LATE20 = 27   # 改革開放期
PERIOD_21C = 12      # 現代

# (name_ja, name_en, name_original, original_script, period_id, definition, importance)
CONCEPTS = [
    # Cluster 1: 海外華人作家
    ("張愛玲『色、戒』", "Eileen Chang Lust Caution", "色，戒", "kanji", PERIOD_LATE20,
     "1979年発表中編。抗日期上海女スパイの欲望と裏切りを描く張愛玲晩年の代表作。", 5),
    ("郁達夫『沈淪』", "Yu Dafu Sinking", "沈淪", "kanji", PERIOD_LATE20,
     "1921年創造社私小説。日本留学中国青年の性的苦悶と祖国愛を告白した自叙伝的短編。", 4),
    ("林語堂『北京好日』", "Lin Yutang Moment in Peking", "京華煙雲", "kanji", PERIOD_LATE20,
     "1939年英語小説。義和団から抗日戦争まで北京三家族を描く海外華人英語文学代表作。", 4),
    ("白先勇『臺北人』短篇集", "Pai Hsien-yung Taipei People", "臺北人", "kanji", PERIOD_LATE20,
     "1971年14短篇集。大陸喪失した外省人の追憶と頽廃を描く台湾現代文学金字塔。", 5),
    ("聶華苓『桑青與桃紅』", "Hualing Nieh Mulberry and Peach", "桑青與桃紅", "kanji", PERIOD_LATE20,
     "1976年離散小説。抗戦から米国までの中国女性流亡を二重人格で描く海外華人代表作。", 4),
    ("張貴興『猴杯』", "Chang Kuei-hsing Monkey Cup", "猴杯", "kanji", PERIOD_21C,
     "2000年馬華熱帯小説。ボルネオ密林とプランテーションを舞台に華人離散と暴力を描く。", 4),

    # Cluster 2: 香港・台湾文学
    ("劉以鬯『酒徒』", "Liu Yichang Drunkard", "酒徒", "kanji", PERIOD_LATE20,
     "1963年香港意識流小説。商業社会で堕する文人の独白で都市疎外を描く中文モダニズム嚆矢。", 5),
    ("西西『我城』", "Xi Xi My City", "我城", "kanji", PERIOD_LATE20,
     "1975年香港都市小説。少年阿果視点で香港日常を魔術的写実で描く本土意識文学起点。", 5),
    ("王文興『家變』", "Wang Wenxing Family Catastrophe", "家變", "kanji", PERIOD_LATE20,
     "1973年台湾実験長編。父出奔をめぐる家族解体を漢字実験で描き言語革命と論争招く。", 4),
    ("朱天心『古都』", "Chu Tien-hsin The Old Capital", "古都", "kanji", PERIOD_21C,
     "1997年中編。台北と京都の重層記憶を彷徨い、外省人二世のアイデンティティ喪失を綴る。", 4),
    ("朱天文『荒人手記』", "Chu Tien-wen Notes of a Desolate Man", "荒人手記", "kanji", PERIOD_LATE20,
     "1994年台湾長編。同性愛者中年男性独白で世紀末頽廃を綴り時報文学賞を受賞した代表作。", 4),
    ("賴香吟", "Lai Hsiang-yin", "賴香吟", "kanji", PERIOD_21C,
     "1969年生台湾女性作家。『其後』『翻譯者』で記憶喪失と歴史創傷を扱う知性派代表。", 3),

    # Cluster 3: ネット文学・ジャンル小説
    ("唐家三少 网络小説", "Tang Jia San Shao web novel", "唐家三少", "kanji", PERIOD_21C,
     "起点中文网代表作家。『斗羅大陸』等で玄幻ジャンルを商業化し网絡文学産業の象徴。", 4),
    ("慕容雪村 ネット文学突破", "Murong Xuecun online breakthrough", "慕容雪村", "kanji", PERIOD_21C,
     "2002年『成都、今夜将我遺忘』で網絡文学を主流文壇に橋渡しした都市虚無小説の旗手。", 4),
    ("安妮宝貝 ネットデビュー", "Anni Baobei online debut", "安妮宝貝", "kanji", PERIOD_21C,
     "1998年BBS発表で台頭。都市女性の感傷文体で網絡文学初期の女性読者層を開拓した。", 4),
    ("麦家『解密』", "Mai Jia Decoded", "解密", "kanji", PERIOD_21C,
     "2002年諜報小説。天才数学者の暗号解読人生を描き諜戦類型と純文学を架橋した代表作。", 4),
    ("劉慈欣『球状閃電』中編版", "Liu Cixin Ball Lightning novella", "球狀閃電", "kanji", PERIOD_LATE20,
     "2001年中編原型。球電量子化現象を硬科幻で展開し『三体』前夜の科幻世界の根を成す。", 4),
    ("劉宇昆『紙の動物園』翻訳", "Ken Liu Paper Menagerie translation", "紙の動物園", "kanji", PERIOD_21C,
     "2011年米国ヒューゴー賞短編。中国SF英訳の橋渡し役で『三体』世界普及の立役者。", 4),

    # Cluster 4: 詩人細部
    ("海子「亜洲銅」", "Hai Zi Asia Bronze", "亞洲銅", "kanji", PERIOD_LATE20,
     "1984年抒情詩。アジアの土地と農耕の根源的イメージを神話化した第三代詩派の代表作。", 5),
    ("欧陽江河「玻璃工廠」", "Ouyang Jianghe Glass Factory", "玻璃工廠", "kanji", PERIOD_LATE20,
     "1987年知識分子写作の代表作。工場と透明性のメタファーで存在論的省察を展開した長詩。", 4),
    ("翟永明「女人」組詩", "Zhai Yongming Woman cycle", "女人", "kanji", PERIOD_LATE20,
     "1984年20首組詩。「黒夜意識」を提唱し中国女性詩の身体経験を確立した嚆矢的作品。", 5),
    ("于堅『0檔案』", "Yu Jian File Zero", "0檔案", "kanji", PERIOD_LATE20,
     "1992年長詩。人事档案の言語を解体し官僚制と個人記録を批判する民間写作代表作。", 4),
    ("西川「致敬」", "Xi Chuan Salute", "致敬", "kanji", PERIOD_LATE20,
     "1992年知識分子写作の散文長詩。歴史と祖先への敬礼で文人伝統と現代詩を接続した代表作。", 4),
    ("韓東「有関大雁塔」", "Han Dong Somebody about Big Wild Goose Pagoda", "有關大雁塔", "kanji", PERIOD_LATE20,
     "1983年第三代詩派宣言詩。崇高な大雁塔を「ある人々」と脱神聖化し日常口語詩を打ち立てた。", 5),

    # Cluster 5: 80后・90后・新世代
    ("韓寒『1988』", "Han Han 1988", "1988", "kanji", PERIOD_21C,
     "2010年公路小説。古いサンタナで旅する青年と娼妓を描き80后世代の虚無を描いた代表作。", 4),
    ("郭敬明『小時代』", "Guo Jingming Tiny Times", "小時代", "kanji", PERIOD_21C,
     "2008年都市青春長編。上海四人の消費生活を描き80后女性読者層と物質主義文学を象徴。", 4),
    ("盛可以『北妹』", "Sheng Keyi Northern Girls", "北妹", "kanji", PERIOD_21C,
     "2004年長編。深圳に出稼ぎする湖南農村出身少女の苦闘を描く新世代労働文学代表作。", 4),
    ("魯敏『六人晩餐』", "Lu Min Dinner for Six", "六人晚餐", "kanji", PERIOD_21C,
     "2012年長編。製鋼工場周辺の二家族六人の食卓で80年代から現代までの中国家族史を描く。", 4),
    ("王梆『不可見的女人』", "Wang Bang Invisible Women", "不可見的女人", "kanji", PERIOD_21C,
     "在英華人作家。労働階級女性の不可視性をルポ的小説で描く新世代海外華人作品。", 3),
    ("張悦然『繭』", "Zhang Yueran Cocoon", "繭", "kanji", PERIOD_21C,
     "2016年長編。文革祖父世代の罪を継承する80后男女二人の対話形式で世代間記憶を描く。", 4),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted, skipped = 0, 0
    for c in CONCEPTS:
        name_ja, name_en, name_orig, script, period_id, definition, importance = c
        try:
            cur.execute("""
                INSERT INTO concepts
                  (name_ja, name_en, name_original, original_script,
                   subfield_id, region, period_id, definition,
                   importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'tier2', 'china')
            """, (name_ja, name_en, name_orig, script,
                  SUBFIELD_ID, REGION, period_id, definition, importance))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    print(f"Inserted: {inserted}, Skipped: {skipped}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    print(f"Total in subfield {SUBFIELD_ID}: {cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
