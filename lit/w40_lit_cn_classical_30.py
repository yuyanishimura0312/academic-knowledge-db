#!/usr/bin/env python3
"""Wave 40: add 30 hyper-niche concepts to lit_cn_classical (subfield_id=8)."""

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_cn_classical"
REGION = "東アジア"

P_HAN = 2
P_WEIJIN = 3
P_TANG = 4
P_SONG = 52
P_MING = 54
P_QING = 55

CONCEPTS = [
    # 1. 漢代詩経・経学注釈の逸文系
    ("斉詩匡衡章句", "Kuang Heng Qi Poetry exegesis", "齊詩匡衡章句", P_HAN, "匡衡系斉詩解釈の章句伝承。漢代今文詩学の政治的読法を示す。"),
    ("魯詩韋賢父子学", "Wei family Lu Poetry learning", "魯詩韋賢父子學", P_HAN, "韋賢・韋玄成父子に伝わる魯詩学。官学化した詩経注釈の一脈。"),
    ("韓詩薛氏章句", "Xue lineage Han Poetry chapters", "韓詩薛氏章句", P_HAN, "薛氏が伝えた韓詩章句。韓嬰以後の失伝注釈を復元する手がかり。"),
    ("陸璣『毛詩草木鳥獸蟲魚疏』", "Lu Ji Mao Poetry flora-fauna glosses", "毛詩草木鳥獸蟲魚疏", P_WEIJIN, "詩経名物を動植物別に注す呉陸璣の博物学的毛詩注釈。"),
    ("鄭箋異文校勘", "Zheng Xuan jian variant collation", "鄭箋異文", P_HAN, "鄭玄毛詩箋の字句異同を比べ、経文解釈の揺れを読む校勘作業。"),
    ("三家詩遺説輯佚", "recovered sayings of Three Schools Poetry", "三家詩遺説", P_QING, "魯・斉・韓三家詩の散逸説を清代考証で輯録する注釈復元。"),
    # 2. 六朝宮体・小賦・文選周辺
    ("蕭綱『詠内人晝眠』", "Xiao Gang Yong Neiren Zhoumian", "詠内人晝眠", P_WEIJIN, "梁簡文帝の宮体艶詩。室内視線と女性身体描写の細密化を示す。"),
    ("徐摛宮体唱和", "Xu Chi palace-style exchanges", "徐摛宮體唱和", P_WEIJIN, "徐摛を中心とする梁宮廷の艶詩唱和。宮体詩の実作圏を示す。"),
    ("庾信『小園賦』", "Yu Xin Xiao Yuan Fu", "小園賦", P_WEIJIN, "北周庾信の小品賦。流寓文人の私園感覚と南朝追憶を凝縮する。"),
    ("江總陳宮詩", "Jiang Zong Chen palace poems", "江總陳宮詩", P_WEIJIN, "陳後主宮廷で作られた江総の艶麗詩。亡国前夜の宮廷詩風を伝える。"),
    ("蕭統『文選』序体裁", "Wenxuan preface genre criteria", "文選序", P_WEIJIN, "文選序に示された文類配列と選録基準。六朝文体分類の要点。"),
    ("徐陵『玉台新詠』序辞", "Yutai Xinyong preface rhetoric", "玉臺新詠序", P_WEIJIN, "玉台新詠序の艶情正当化 rhetoric。宮体詩集の読法を誘導する。"),
    # 3. 敦煌講唱・俗文学細部
    ("敦煌押座文", "Dunhuang yaza performance openings", "押座文", P_TANG, "講唱の場を整える敦煌写本の開場文。聴衆統御の定型句を持つ。"),
    ("悉曇字母讃", "Siddham alphabet hymn", "悉曇字母讃", P_TANG, "悉曇字母を韻文で讃える仏教歌讃。文字学と唱導が交差する。"),
    ("伍子胥変文", "Wu Zixu transformation text", "伍子胥變文", P_TANG, "伍子胥復讐譚を散韻交替で語る敦煌変文。史伝の講唱化を示す。"),
    ("降魔変文", "Demon-subduing transformation text", "降魔變文", P_TANG, "仏の降魔場面を劇的に語る変文。説法儀礼と物語演出が結ぶ。"),
    ("維摩詰経講経文", "Vimalakirti sutra lecture text", "維摩詰經講經文", P_TANG, "維摩経を俗講用に展開した講経文。問答と韻文で教義を通俗化する。"),
    ("季布詩詠", "Jibu shiyong ballad narrative", "季布詩詠", P_TANG, "季布故事を詩詠化した敦煌系俗文学。史譚の歌謡的受容を示す。"),
    # 4. 宋代詩話・詞話の小系
    ("王灼『碧雞漫志』", "Wang Zhuo Biji Manzhi", "碧雞漫志", P_SONG, "宋代詞楽の源流と曲調を論じる詞話。詞体史研究の早期資料。"),
    ("胡仔『苕溪漁隱叢話』", "Hu Zai Tiaoxi Yuyin Conghua", "苕溪漁隱叢話", P_SONG, "前後集に詩話を集成した宋代詩論資料。唐宋詩評の宝庫。"),
    ("魏慶之『詩人玉屑』", "Wei Qingzhi Shiren Yuxie", "詩人玉屑", P_SONG, "作詩法と詩評を門類別に編む南宋詩話総集。句法論を整理する。"),
    ("陳善『捫蝨新話』", "Chen Shan Menshi Xinhua", "捫蝨新話", P_SONG, "詩文掌故と読書評を雑録する南宋筆記。士大夫批評の断片を残す。"),
    ("周密『絶妙好詞』", "Zhou Mi Jue Miao Hao Ci", "絶妙好詞", P_SONG, "南宋周密の詞選集。姜夔以後の雅詞を精選し清空趣味を伝える。"),
    ("晁補之評蘇詞", "Chao Buzhi on Su Shi's ci", "晁補之評蘇詞", P_SONG, "晁補之による蘇軾詞評価。詩化した詞への宋人同時代批評を示す。"),
    # 5. 明清評点・版本の微細系譜
    ("葉昼『水滸伝』評点", "Ye Zhou Shuihu commentary", "葉晝評點水滸傳", P_MING, "金聖歎以前の水滸評点。人物評と章法批評の早い層を示す。"),
    ("李卓吾本『西廂記』", "Li Zhi edition Xixiangji", "李卓吾本西廂記", P_MING, "李贄名義で流通した西廂記評本。情と才子佳人読法を強調する。"),
    ("汪象旭『西遊證道書』", "Wang Xiangxu Xiyou Zhengdao Shu", "西遊證道書", P_QING, "西遊記を三教修行譚として読む清初評本。寓意的読解を徹底する。"),
    ("閑斎老人『儒林外史』評", "Xianzhai Laoren Rulin waishi commentary", "閑齋老人評儒林外史", P_QING, "儒林外史の早期評点。諷刺人物の品評と章回構成を読む。"),
    ("蒙府本『石頭記』", "Mongol prince mansion Shitouji manuscript", "蒙府本石頭記", P_QING, "紅楼夢八十回系写本の一種。脂評と本文異同の研究対象。"),
    ("戚蓼生『石頭記序』", "Qi Liaosheng preface to Shitouji", "石頭記序", P_QING, "戚蓼生が紅楼夢の草蛇灰線的構成を称えた著名序文。"),
]


def main() -> None:
    inserted = 0
    skipped = 0
    with LitDB() as db:
        existing_names = {
            row["name_ja"]
            for row in db.conn.execute("SELECT name_ja FROM concepts")
        }
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, (name_ja, len(definition))
            if name_ja in existing_names:
                skipped += 1
                continue
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
            inserted += 1
        total = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id = 8"
        ).fetchone()[0]
    print(f"inserted={inserted} skipped={skipped} total={total}")


if __name__ == "__main__":
    main()
