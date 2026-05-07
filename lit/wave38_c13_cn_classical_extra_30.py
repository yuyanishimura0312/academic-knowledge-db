#!/usr/bin/env python3
"""Wave 38 C13: lit_cn_classical extra 30 niche concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_cn_classical"
REGION = "東アジア"

P_XIANQIN = 1
P_HAN = 2
P_WEIJIN = 3
P_TANG = 4
P_SONG = 52
P_MING = 54
P_QING = 55

CONCEPTS = [
    # 1. 経書・漢代注釈系譜
    ("魯詩学派", "Lu-school Poetry exegesis", "魯詩", P_HAN, "魯申培系の今文詩経学。礼義解釈を重んじた漢代三家詩の一。"),
    ("斉詩翼氏学", "Qi-school Wing lineage", "齊詩翼氏學", P_HAN, "翼奉らに伝わる斉詩の一支流。災異と詩義を結ぶ今文注釈。"),
    ("韓詩内伝", "Han Poetry Inner Tradition", "韓詩内傳", P_HAN, "韓嬰系詩経解釈の失伝部門。外伝と対になる説話的詩義の源流。"),
    ("毛詩小序弁体", "Mao Poetry minor prefaces", "毛詩小序", P_HAN, "各篇冒頭の短序で詩旨を定める毛詩注釈の微細な解題形式。"),
    ("焦氏易林", "Jiao's Forest of Changes", "焦氏易林", P_HAN, "易占辞を四言韻語で展開した漢代占筮文学の特異な韻文集。"),
    ("劉向『列女伝』叙伝体", "Liu Xiang Lienu zhuan narrative", "列女傳", P_HAN, "女性範例を類型化し讃で締める、漢代伝記散文の教訓的形式。"),
    # 2. 魏晋南北朝の小流派・小品
    ("永明体八病回避", "Yongming avoidance of eight faults", "永明體八病", P_WEIJIN, "沈約らの声律詩学で、平頭・上尾など八病を避ける作詩規範。"),
    ("謝朓宣城詩", "Xie Tiao Xuancheng poems", "謝朓宣城詩", P_WEIJIN, "宣城太守期の清麗な山水詩。大謝から唐近体詩へ橋渡しする詩風。"),
    ("何遜宮体前夜詩", "He Xun pre-palace-style poetry", "何遜詩", P_WEIJIN, "斉梁の繊細な五言詩。宮体詩以前の清婉な情景描写を示す。"),
    ("陰鏗新体詩", "Yin Keng new-style verse", "陰鏗新體詩", P_WEIJIN, "梁陳期の声律化された五言詩。初唐律詩形成の隠れた前段階。"),
    ("庾信『哀江南賦』", "Yu Xin Lament for the South", "哀江南賦", P_WEIJIN, "亡国と北遷の痛みを駢儷体で刻む、南北朝末の自伝的長賦。"),
    ("顔之推文章観", "Yan Zhitui view of writing", "顔氏家訓文章篇", P_WEIJIN, "実用と教養を両立させる家訓中の文章論。六朝文風批判を含む。"),
    # 3. 唐代周縁詩歌・敦煌文献
    ("王梵志詩", "Wang Fanzhi poems", "王梵志詩", P_TANG, "俗語と仏教教訓で世態を諷す、敦煌写本に残る白話的唐詩。"),
    ("寒山拾得詩群", "Hanshan and Shide poems", "寒山拾得詩", P_TANG, "禅・隠逸・俗語を混ぜる天台山伝承の周縁詩群。"),
    ("敦煌変文講唱体", "Dunhuang transformation-text prosimetrum", "敦煌變文", P_TANG, "仏伝や史譚を散韻交替で語る、講唱文学の初期形態。"),
    ("敦煌俗賦", "Dunhuang popular fu", "敦煌俗賦", P_TANG, "口語・滑稽・問答を用いる敦煌写本系の通俗賦。"),
    ("敦煌曲子詞", "Dunhuang quzi ci", "敦煌曲子詞", P_TANG, "民間歌謡の調べを残す初期詞資料。文人詞成立前の詞体を示す。"),
    ("皮陸唱和", "Pi-Lu poetic exchange", "皮陸唱和", P_TANG, "皮日休と陸龜蒙の大量唱和。晩唐江南文人の遊戯的詩社実践。"),
    # 4. 宋金詞話・詩話の細部
    ("呂本中活法説", "Lu Benzhong living method", "活法", P_SONG, "江西詩派内部から固定句法を越える生成的作詩法を説いた概念。"),
    ("惠洪『冷斎夜話』", "Huihong Lengzhai Yehua", "冷齋夜話", P_SONG, "禅僧惠洪の詩話筆記。詩僧文化と宋代逸話批評を伝える。"),
    ("葉夢得『石林詩話』", "Ye Mengde Shilin Shihua", "石林詩話", P_SONG, "北宋詩壇の掌故と作法を記す、士大夫詩話の代表的初期資料。"),
    ("江湖詩派", "Rivers and Lakes poetry school", "江湖詩派", P_SONG, "南宋末の下層文人詩派。江湖集刊行で地方詩人を束ねた。"),
    ("元好問『中州集』", "Yuan Haowen Zhongzhou ji", "中州集", P_SONG, "金代詩人を編み亡国記憶を保存した、北方詩史の重要総集。"),
    ("吳激蔡松年詞", "Wu Ji and Cai Songnian ci", "吳激蔡松年詞", P_SONG, "金代前期の詞人二家。宋詞の余韻を北方宮廷文化へ移した。"),
    # 5. 明清地域派・女性文芸
    ("呉江派曲学", "Wujiang school drama theory", "吳江派", P_MING, "沈璟を中心に音律と本色を重視した明代曲学の地域派。"),
    ("臨川派戯曲", "Linchuan school drama", "臨川派", P_MING, "湯顕祖系の文采と情を重んじる戯曲潮流。呉江派と対立した。"),
    ("嘉靖八才子", "Eight Talents of Jiajing", "嘉靖八才子", P_MING, "李攀龍以前の明中期詩文集団。復古詩学の過渡的結社。"),
    ("陽羨詞派", "Yangxian ci school", "陽羨詞派", P_QING, "陳維崧を中心に豪放な長調を得意とした清初詞派。"),
    ("常州詞派比興説", "Changzhou ci allegorical poetics", "常州詞派比興説", P_QING, "張惠言らが詞に寄托と比興を読む清代詞学の核心説。"),
    ("随園女弟子詩", "Suiyuan women disciples' poetry", "隨園女弟子詩", P_QING, "袁枚門下女性詩人の作品群。清代女性詩社文化の可視的成果。"),
]


def main() -> None:
    inserted = 0
    skipped = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, f"definition too long: {name_ja}"
            before = db.find_concept(name_ja, REGION, period_id)
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script="kanji",
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            if before:
                skipped += 1
            else:
                inserted += 1
        total = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=8"
        ).fetchone()[0]
    print(f"Inserted={inserted}, skipped={skipped}, subfield_id=8 total={total}")


if __name__ == "__main__":
    main()
