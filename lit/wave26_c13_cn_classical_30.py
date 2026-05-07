#!/usr/bin/env python3
"""Wave26 C13: Add 30 concepts to lit_cn_classical (subfield_id=8)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"

# period_id mapping (region='東アジア')
P_TANG = 4
P_SONG = 52
P_MING = 54
P_QING = 55

CONCEPTS = [
    # Cluster 1: 詩學
    ("王國維『人間詞話』補完論", "Wang Guowei Renjian Cihua Supplement", "王國維《人間詞話》補論", "kanji", P_QING,
     "境界説の補論。造境/写境・有我/無我境を中核とする近代詞論の総合。"),
    ("司空圖『二十四詩品』", "Sikong Tu Twenty-Four Categories of Poetry", "司空圖《二十四詩品》", "kanji", P_TANG,
     "雄渾・冲淡など24品で詩境を象徴的に分類した晩唐の詩品論。"),
    ("嚴羽『滄浪詩話』詩辨", "Yan Yu Canglang Shihua Shibian", "嚴羽《滄浪詩話・詩辨》", "kanji", P_SONG,
     "妙悟・興趣・別材別趣を説き、盛唐を典範とする禅喩詩論。"),
    ("葉燮『原詩』", "Ye Xie Yuan Shi", "葉燮《原詩》", "kanji", P_QING,
     "理事情・才膽識力で詩の本源と作者条件を体系化した清代詩学論著。"),
    ("王夫之『姜齋詩話』", "Wang Fuzhi Jiangzhai Shihua", "王夫之《薑齋詩話》", "kanji", P_QING,
     "情景交融・現量説を提示し、即景而生を重視する明末清初の詩話。"),
    ("沈德潛『說詩晬語』", "Shen Deqian Shuoshi Cuiyu", "沈德潛《說詩晬語》", "kanji", P_QING,
     "格調説の代表詩話。温柔敦厚を旨とし、唐音復古を主張する。"),
    # Cluster 2: 散文派
    ("桐城派 姚鼐「義理・考據・辭章」", "Yao Nai Yili-Kaoju-Cizhang", "姚鼐〈義理考據辭章〉", "kanji", P_QING,
     "義理・考據・辭章の三者統合を説き桐城派古文を集大成した姚鼐の文論。"),
    ("古文義法（方苞）", "Fang Bao Yifa", "方苞〈古文義法〉", "kanji", P_QING,
     "言有物言有序の義法説を立て桐城派の方法論を確立した古文理論。"),
    ("桐城三祖", "Three Patriarchs of Tongcheng School", "桐城三祖", "kanji", P_QING,
     "方苞・劉大櫆・姚鼐を指す桐城派三祖。清代古文の正統と称される。"),
    ("唐宋八大家論", "Discourse on the Eight Masters of Tang-Song", "唐宋八大家論", "kanji", P_MING,
     "韓柳欧曾王三蘇の八家を古文模範とする批評体系。茅坤『唐宋八大家文鈔』に確立。"),
    ("文以載道（周敦頤）", "Wen yi zai Dao", "周敦頤〈文以載道〉", "kanji", P_SONG,
     "文章は道を載せる器とする宋学的文論。古文の倫理機能を規定する。"),
    ("陽湖派 惲敬", "Yun Jing Yanghu School", "惲敬・陽湖派", "kanji", P_QING,
     "桐城派の偏狭を補い、子史百家を取り入れた清代古文派。惲敬・張惠言が中心。"),
    # Cluster 3: 戲曲詳細
    ("王實甫『西廂記』第四本", "Wang Shifu Xixiang Ji Book IV", "王實甫《西廂記》第四本", "kanji", 53,
     "張生鶯鶯の幽期密約を描く第四本。元雜劇五本二十一折構成の頂点。"),
    ("湯顯祖『牡丹亭』驚夢", "Tang Xianzu Mudan Ting Jingmeng", "湯顯祖《牡丹亭・驚夢》", "kanji", P_MING,
     "杜麗娘が夢中で柳夢梅と契る至情論の核心場面。情の超越性を象徴する。"),
    ("孔尚任『桃花扇』", "Kong Shangren Taohua Shan", "孔尚任《桃花扇》", "kanji", P_QING,
     "侯方域と李香君の悲恋を通じ南明興亡を描く清初伝奇の代表作。"),
    ("洪昇『長生殿』", "Hong Sheng Changsheng Dian", "洪昇《長生殿》", "kanji", P_QING,
     "玄宗楊貴妃の愛と安史の乱を描き情と政を交錯させた清初伝奇の傑作。"),
    ("李漁『閒情偶寄』詞曲部", "Li Yu Xianqing Ouji Ciqu", "李漁《閒情偶寄・詞曲部》", "kanji", P_QING,
     "立主脳・脱窠臼など戯曲創作論を体系化した中国最初の劇作技法書。"),
    ("高明『琵琶記』", "Gao Ming Pipa Ji", "高明《琵琶記》", "kanji", 53,
     "趙五娘・蔡伯喈の物語で南戯を文人劇に昇華させた元末南戯の傑作。"),
    # Cluster 4: 小說批評
    ("金聖歎『水滸傳』評本", "Jin Shengtan Shuihu Zhuan Pingben", "金聖歎評《水滸傳》", "kanji", P_QING,
     "七十回本に評点を付し小説評点学を確立した。文法・章法を精細に解読。"),
    ("毛宗崗『三國演義』評本", "Mao Zonggang Sanguo Yanyi Pingben", "毛宗崗評《三國演義》", "kanji", P_QING,
     "毛綸・宗崗父子の評点本。蜀漢正統論で改訂し読法二十則を付す。"),
    ("脂硯齋『紅樓夢』評", "Zhiyanzhai Honglou Meng Ping", "脂硯齋評《紅樓夢》", "kanji", P_QING,
     "甲戌・庚辰本等に付された脂批。曹雪芹の創作意図を直接伝える評語群。"),
    ("張竹坡『金瓶梅』評", "Zhang Zhupo Jin Ping Mei Ping", "張竹坡評《金瓶梅》", "kanji", P_QING,
     "第一奇書本評点。冷熱対照・苦孝説で世情小説の構造を読み解く。"),
    ("馮夢龍『三言』序", "Feng Menglong Sanyan Prefaces", "馮夢龍《三言》序", "kanji", P_MING,
     "喻世明言・警世通言・醒世恒言の三序。情教論と通俗教化機能を主張する。"),
    ("凌濛初『二拍』序", "Ling Mengchu Erpai Prefaces", "凌濛初《二拍》序", "kanji", P_MING,
     "初刻・二刻拍案驚奇の序。耳目之内日用起居の題材論で擬話本を理論化。"),
    # Cluster 5: 詞學
    ("李清照『詞論』", "Li Qingzhao Cilun", "李清照《詞論》", "kanji", P_SONG,
     "詞別是一家を主張し、音律・典重・故実を重んじる婉約派詞論の原点。"),
    ("周濟『介存齋論詞雜著』", "Zhou Ji Jiecunzhai Lunci Zazhu", "周濟《介存齋論詞雜著》", "kanji", P_QING,
     "常州詞派の理論書。寄託説・有寄託入・無寄託出の弁証を提示する。"),
    ("陳廷焯『白雨齋詞話』", "Chen Tingzhuo Baiyuzhai Cihua", "陳廷焯《白雨齋詞話》", "kanji", P_QING,
     "沈鬱説で常州派詞論を集大成し、温柔敦厚と寄託を統合する清末詞話。"),
    ("況周頤『蕙風詞話』", "Kuang Zhouyi Huifeng Cihua", "況周頤《蕙風詞話》", "kanji", P_QING,
     "重・拙・大の三境説で詞境を論じた清末四大詞話の一。"),
    ("譚獻『復堂詞話』", "Tan Xian Futang Cihua", "譚獻《復堂詞話》", "kanji", P_QING,
     "作者未必然読者何必不然説で受容理論を先取した常州派後期詞論。"),
    ("王國維 詞論（境界説）", "Wang Guowei Cilun Jingjie", "王國維 詞論〈境界說〉", "kanji", P_QING,
     "造境/写境・有我/無我・隔/不隔の対立軸で近代的詞美学を樹立。"),
]

def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, period_id, definition in CONCEPTS:
        assert len(definition) <= 100, f"defn too long: {name_ja} ({len(definition)})"
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script,
                 subfield_id, region, period_id, definition,
                 importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, 8, '東アジア', ?, ?, 4, 'A', 'cn')
            """, (name_ja, name_en, name_orig, script, period_id, definition))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    con.commit()
    con.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
