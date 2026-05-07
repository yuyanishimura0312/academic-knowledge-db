#!/usr/bin/env python3
"""Wave 37: lit_cn_classical (subfield_id=8) - 30 deep niche concepts."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 8
REGION = "東アジア"

# period IDs: 漢=2, 魏晋南北朝=3, 唐=4, 宋=52, 明=54, 清=55
concepts = [
    # Cluster 1: 漢魏晋詩賦細部 (period 2/3)
    ("蔡邕「述行賦」", "Cai Yong: Shuxing Fu", "述行賦", 3, "後漢蔡邕の紀行賦。洛陽から陳留への旅程に時局批判を織り込む長篇抒情賦。"),
    ("王粲「七哀詩」", "Wang Can: Qi'ai Shi", "七哀詩", 3, "建安七子王粲の代表作。長安喪乱・荊州避難の悲哀を詠む五言古詩三首。"),
    ("阮籍「詠懷詩」八十二首", "Ruan Ji: Yonghuai Eighty-two", "詠懷詩八十二首", 3, "竹林七賢阮籍の代表連作。隠喩的政治批判と憂世の情を五言で連ねる。"),
    ("左思「三都賦」", "Zuo Si: Sandu Fu", "三都賦", 3, "西晋左思の蜀都・呉都・魏都三都賦。洛陽紙貴の故事を生む大賦。"),
    ("陸機「文賦」詳解", "Lu Ji: Wen Fu (detailed)", "文賦", 3, "陸機の創作論的賦。構思・遣辭・文体十類を論じる中国最初期の体系的文学論。"),
    ("潘岳「悼亡詩」", "Pan Yue: Daowang Shi", "悼亡詩", 3, "西晋潘岳が亡妻楊氏を悼む三首連作。後世悼亡詩ジャンルの祖型。"),
    # Cluster 2: 唐詩細部 (period 4)
    ("孟郊「寒衣詩」「遊子吟」", "Meng Jiao: Hanyi/Youzi Yin", "寒衣詩・遊子吟", 4, "苦吟派孟郊の母情詩。「慈母手中線、遊子身上衣」で寒微の情を凝縮する。"),
    ("賈島「推敲」典故", "Jia Dao: Tuiqiao Anecdote", "推敲", 4, "賈島「僧推月下門」の字句選択逸話。煉字精神と苦吟詩学の象徴典故。"),
    ("李賀「神弦曲」群", "Li He: Shenxian Qu", "神弦曲", 4, "鬼才李賀の祭祀神霊歌行群。冥界・神異の鬼怪美学と濃艶な意象世界。"),
    ("温庭筠「菩薩蛮」", "Wen Tingyun: Pusa Man", "菩薩蛮", 4, "晩唐花間派温庭筠の代表詞。閨怨と濃彩意象により詞体の文学化を確立。"),
    ("韋応物「寒食寄京師諸弟」", "Wei Yingwu: Hanshi Ji Jingshi", "寒食寄京師諸弟", 4, "中唐韋応物の寒食節郷愁詩。淡遠閑寂の風格で王孟詩派を継承する。"),
    ("韓愈「山石」", "Han Yu: Shanshi", "山石", 4, "韓愈の七言古詩代表作。一日の山寺遊歴を散文的筆致で叙す以文為詩実例。"),
    # Cluster 3: 宋詩・宋詞 (period 52)
    ("黄庭堅「寄黄幾復」", "Huang Tingjian: Ji Huang Jifu", "寄黄幾復", 52, "江西詩派黄庭堅の七律。「桃李春風一杯酒」で点鉄成金の技法を体現する。"),
    ("陳師道「別三子」", "Chen Shidao: Bie Sanzi", "別三子", 52, "後山陳師道が貧で三子を母家に送る別離詩。江西派閉門覓句の典型。"),
    ("楊万里「小池」", "Yang Wanli: Xiaochi", "小池", 52, "誠斎体楊万里の七言絶句。荷尖蜻蜓の小景観察で活法・誠斎体を確立する。"),
    ("范成大「四時田園雑興」", "Fan Chengda: Sishi Tianyuan Zaxing", "四時田園雜興", 52, "范成大の田園六十首連作。農村四季の労苦と風物を写実的に描く。"),
    ("周邦彦「蘭陵王・柳」", "Zhou Bangyan: Lanlingwang Liu", "蘭陵王・柳", 52, "清真詞周邦彦の長調代表作。柳色送別を勾勒し慢詞律呂法度の極致を示す。"),
    ("姜夔「揚州慢」", "Jiang Kui: Yangzhou Man", "揚州慢", 52, "白石道人姜夔の自度曲。金兵後の揚州空城を詠み清空騒雅の詞境を開く。"),
    # Cluster 4: 明清小説詩細部 (period 54/55)
    ("馮夢龍『三言』", "Feng Menglong: Sanyan", "三言（喻世明言・警世通言・醒世恒言）", 54, "晩明馮夢龍の白話短篇集120篇。市民倫理と通俗芸術を融合した擬話本集大成。"),
    ("凌濛初『二拍』", "Ling Mengchu: Erpai", "初刻拍案驚奇・二刻拍案驚奇", 54, "凌濛初の擬話本集80篇。三言と並ぶ「三言二拍」明代白話短篇の双璧。"),
    ("蒲松齡『聊齋誌異』「連瑣」", "Pu Songling: Liaozhai - Liansuo", "聊齋誌異・連瑣", 55, "聊斎志異中の人鬼戀篇。書生楊于畏と幽霊連瑣の詩文唱和譚、文言志怪の精華。"),
    ("紀昀『閱微草堂筆記』分類", "Ji Yun: Yuewei Caotang Biji", "閱微草堂筆記", 55, "紀昀の文言志怪筆記1196則。理学批判と教化論で聊齋に対抗する清代志怪。"),
    ("劉鶚『老殘遊記』黄河治水描写", "Liu E: Laocan Youji - Yellow River", "老殘遊記・黄河", 55, "晩清劉鶚の遊記体小説中、黄河治水と江湖医老残見聞による晩清官場諷刺の核心部。"),
    ("李寶嘉『官場現形記』", "Li Baojia: Guanchang Xianxing Ji", "官場現形記", 55, "晩清李寶嘉の譴責小説。清末官界腐敗を六十回連環短篇で暴露する代表作。"),
    # Cluster 5: 散文・文論細部 (period 3/52/55)
    ("劉勰『文心雕龍』「神思」篇", "Liu Xie: Wenxin - Shensi", "文心雕龍・神思", 3, "文心雕龍創作論の核心篇。想像作用「神与物遊」を論じ中国想像論の基礎を築く。"),
    ("鍾嶸『詩品』上品論", "Zhong Rong: Shipin Shang", "詩品上品", 3, "鍾嶸が漢魏六朝五言詩人122名を三品評価し上品11家を選ぶ最初期詩人品評書。"),
    ("司空圖『二十四詩品』「雄渾」", "Sikong Tu: Ershisi Shipin - Xionghun", "二十四詩品・雄渾", 4, "二十四詩品冒頭風格。「大用外腓、真体内充」と象徴的に詩境雄渾を描く。"),
    ("嚴羽『滄浪詩話』妙悟", "Yan Yu: Canglang Shihua - Miaowu", "滄浪詩話・妙悟", 52, "嚴羽が禅喩で詩学を論じ「妙悟」を最高境地とする宋代詩論最重要文献。"),
    ("王國維『人間詞話』境界説", "Wang Guowei: Renjian Cihua", "人間詞話", 55, "王国維が境界・有我無我・隔不隔を論じ伝統詞話と西洋美学を融合した近代詞論。"),
    ("葉燮『原詩』理事情論", "Ye Xie: Yuanshi", "原詩", 55, "清初葉燮の体系的詩論。理・事・情と才・膽・識・力の四要素で創作論を組織する。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = []
    skipped = []
    for ja, en, orig, pid, defn in concepts:
        try:
            assert len(defn) <= 100, f"def too long ({len(defn)}): {ja}"
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script,
                 subfield_id, region, period_id, definition,
                 importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, 'kanji', ?, ?, ?, ?, 3, 'A', 'yes')
            """, (ja, en, orig, SUBFIELD_ID, REGION, pid, defn))
            inserted.append(ja)
        except sqlite3.IntegrityError as e:
            skipped.append((ja, str(e)))
    conn.commit()
    conn.close()
    print(f"Inserted: {len(inserted)}/30")
    if skipped:
        print(f"Skipped: {len(skipped)}")
        for s in skipped:
            print(" -", s)

if __name__ == "__main__":
    main()
