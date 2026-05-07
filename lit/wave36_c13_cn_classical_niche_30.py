#!/usr/bin/env python3
"""Wave36 C13: lit_cn_classical NICHE 30 concepts (5 clusters x 6)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 8
REGION = "東アジア"

# period_id mapping
P_TANG, P_SONG, P_YUAN, P_MING, P_QING = 4, 52, 53, 54, 55

CONCEPTS = [
    # === 1. 唐傳奇詳細 (period=唐) ===
    ("沈既濟『枕中記』黄粱夢譚型", "Shen Jiji 'Pillow Record' yellow-millet dream type", "枕中記",
     P_TANG, "盧生が呂翁の枕で一生の栄華を夢見、黄粱未熟の刹那と悟る道家寓意の傳奇代表作。"),
    ("李朝威『柳毅傳』龍女譚モチーフ", "Li Chaowei 'Liu Yi' dragon-maiden motif", "柳毅傳",
     P_TANG, "落第書生柳毅が涇川龍女の苦境を救い洞庭龍宮で婚を結ぶ、人神交婚譚の典型。"),
    ("蔣防『霍小玉傳』棄妾悲劇型", "Jiang Fang 'Huo Xiaoyu' abandoned-courtesan tragedy", "霍小玉傳",
     P_TANG, "李益と娼女霍小玉の盟約破棄譚。男主の薄情と女鬼の祟りを描く悲劇的傳奇。"),
    ("元稹『鶯鶯傳』張生棄鶯モデル", "Yuan Zhen 'Yingying Zhuan' Zhang Sheng abandonment", "鶯鶯傳",
     P_TANG, "張生と崔鶯鶯の私通と離別。後の『西廂記』源流をなす才子佳人薄情譚。"),
    ("白行簡『李娃傳』妓女義行譚", "Bai Xingjian 'Li Wa Zhuan' courtesan virtue tale", "李娃傳",
     P_TANG, "妓女李娃が滎陽生を救済し科挙合格に導く、娼婦の義を顕揚する傳奇。"),
    ("段成式『酉陽雜俎』志怪百科型", "Duan Chengshi 'Youyang Zazu' miscellany encyclopedism", "酉陽雜俎",
     P_TANG, "鬼神・異物・風俗・博物を網羅する晩唐筆記の集大成。後世志怪の典拠。"),

    # === 2. 宋代散文 (period=宋) ===
    ("歐陽修「秋聲賦」声を聞く文", "Ouyang Xiu 'Autumn Sounds Rhapsody'", "秋聲賦",
     P_SONG, "秋風の音を聴覚から起筆し人事の盛衰へ転ずる、宋代俳賦の到達点。"),
    ("蘇軾「前赤壁賦」水月主客問答", "Su Shi 'Former Red Cliff Rhapsody' host-guest dialogue", "前赤壁賦",
     P_SONG, "客の悲嘆と主の達観を水と月の比喩で説き、変と不変の哲理を導く名賦。"),
    ("蘇軾「後赤壁賦」鶴夢道士譚", "Su Shi 'Latter Red Cliff Rhapsody' crane-Daoist", "後赤壁賦",
     P_SONG, "再遊の夜に孤鶴と道士の夢を綴り、前篇の理趣から幻奇境へ転ずる続篇。"),
    ("王安石「遊褒禪山記」志力物三因論", "Wang Anshi 'Bao Chan Mountain' three-factor theory", "遊褒禪山記",
     P_SONG, "洞穴探訪を経て志・力・物の三条件を論ずる、議論性に富む宋代遊記。"),
    ("范仲淹「岳陽樓記」先憂後樂論", "Fan Zhongyan 'Yueyang Tower' worry-first joy-after", "岳陽樓記",
     P_SONG, "天下の憂を先んじ天下の楽を後にすと宣する士大夫倫理の宣言文。"),
    ("周敦頤「愛蓮說」君子蓮花譬喩", "Zhou Dunyi 'On Loving the Lotus' gentleman-lotus", "愛蓮說",
     P_SONG, "蓮を泥中不染の君子に喩え、菊・牡丹と対比する理学的小品の典範。"),

    # === 3. 元曲深掘り (period=元) ===
    ("白樸『梧桐雨』玄宗楊妃悲歌", "Bai Pu 'Rain on Wutong Tree' Xuanzong-Yang lament", "梧桐雨",
     P_YUAN, "馬嵬坡後の玄宗が梧桐の雨音に楊貴妃を偲ぶ、抒情性高い元雑劇四大悲劇の一。"),
    ("鄭光祖『倩女離魂』魂体離合譚", "Zheng Guangzu 'Soul Departed' soul-body separation", "倩女離魂",
     P_YUAN, "張倩女の魂が肉体を離れ恋人を追う愛情劇。離魂モチーフの代表作。"),
    ("紀君祥『趙氏孤兒』復讐悲劇型", "Ji Junxiang 'Orphan of Zhao' revenge tragedy", "趙氏孤兒",
     P_YUAN, "屠岸賈の趙氏滅族と孤児の復讐を描く、ヴォルテール翻案の元代悲劇。"),
    ("喬吉散曲鬼簿評価", "Qiao Ji sanqu and Lugui Bu evaluation", "喬吉散曲",
     P_YUAN, "豪放清麗を兼ねる散曲の名手。鍾嗣成『録鬼簿』で高評を受ける元代曲家。"),
    ("馬致遠「秋思」天淨沙小令", "Ma Zhiyuan 'Autumn Thoughts' Tianjingsha xiaoling", "天淨沙·秋思",
     P_YUAN, "枯藤老樹昏鴉の名句で知られる、漂泊の哀愁を凝縮した散曲小令の絶唱。"),
    ("關漢卿「單刀會」関羽英雄劇", "Guan Hanqing 'Single Sword Meeting' Guan Yu drama", "單刀會",
     P_YUAN, "関羽が単刀で魯粛の宴に赴く三国題材の英雄劇。豪放派関漢卿の代表作。"),

    # === 4. 明代戯曲 (period=明) ===
    ("湯顯祖『牡丹亭』情至論実演", "Tang Xianzu 'Peony Pavilion' supremacy-of-feeling", "牡丹亭",
     P_MING, "杜麗娘の生死を超える愛を描き、情至論を体現する玉茗堂四夢の白眉。"),
    ("湯顯祖『南柯記』槐安国寓意", "Tang Xianzu 'Nanke Ji' Huai'an kingdom allegory", "南柯記",
     P_MING, "蟻穴の槐安国で栄華を極め覚醒する淳于棼譚。仏教的虚妄観を伝奇化。"),
    ("湯顯祖『邯鄲記』黄粱夢戯曲化", "Tang Xianzu 'Handan Ji' yellow-millet dramatization", "邯鄲記",
     P_MING, "枕中記を翻案、盧生の一生を四十二齣に展開する仏道悟道劇。"),
    ("沈璟詞律本色派音律論", "Shen Jing lülü orthodox-school prosody", "沈璟詞律",
     P_MING, "音律厳守の本色派を率い湯顯祖の文采派と「湯沈論争」を演じた曲律家。"),
    ("王驥德『曲律』曲学体系書", "Wang Jide 'Qulü' systematic theory of qu", "曲律",
     P_MING, "明代南北曲の音律・文辞・結構を網羅的に論じた最重要曲学理論書。"),
    ("李漁『閒情偶寄』詞曲部演劇論", "Li Yu 'Xianqing Ouji' Ciqu section drama theory", "閒情偶寄·詞曲部",
     P_MING, "戯曲創作・演出・賓白・科諢を体系化した、東洋初の総合演劇理論書。"),

    # === 5. 清代散文 (period=清) ===
    ("袁枚『隨園詩話』性靈派詩話", "Yuan Mei 'Suiyuan Shihua' xingling-school poetics", "隨園詩話",
     P_QING, "性霊説を掲げ、真情と独創を重んじる清中期最大の詩話集。格調説に対抗。"),
    ("趙翼『陔餘叢考』考証随筆", "Zhao Yi 'Gaiyu Congkao' evidential miscellany", "陔餘叢考",
     P_QING, "経史子集を博捜し疑義を考証する、乾嘉学派代表の博学随筆。"),
    ("紀昀『閱微草堂筆記』理学志怪", "Ji Yun 'Yuewei Caotang Biji' rationalist zhiguai", "閱微草堂筆記",
     P_QING, "聊斎誌異と並ぶ清代志怪の双璧。理学的訓戒を志怪体に込める紀昀の代表筆記。"),
    ("章學誠『文史通義』六経皆史論", "Zhang Xuecheng 'Wenshi Tongyi' six-classics-all-history", "文史通義",
     P_QING, "六経皆史の命題で経学を史学に統合する、清代史論の画期的著作。"),
    ("顧炎武『日知錄』経世実学随筆", "Gu Yanwu 'Rizhi Lu' practical-statecraft notes", "日知錄",
     P_QING, "経義・政事・風俗を考証し経世致用を説く、清初実学の金字塔的札記。"),
    ("黃宗羲『明夷待訪錄』政論散文", "Huang Zongxi 'Mingyi Daifang Lu' political treatise prose", "明夷待訪錄",
     P_QING, "君主専制を批判し民本思想を説く、清初啓蒙的政論散文の代表作。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted, skipped = 0, 0
    for name_ja, name_en, name_orig, period_id, definition in CONCEPTS:
        assert len(definition) <= 100, f"DEF too long ({len(definition)}): {name_ja}"
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script,
                 subfield_id, region, period_id, definition,
                 importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, 'kanji', ?, ?, ?, ?, 3, 'B', 'east_asia')
            """, (name_ja, name_en, name_orig, SUBFIELD_ID, REGION, period_id, definition))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP {name_ja}: {e}")
            skipped += 1
    conn.commit()
    total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)).fetchone()[0]
    conn.close()
    print(f"Inserted: {inserted} / Skipped: {skipped} / Total lit_cn_classical: {total}")

if __name__ == "__main__":
    main()
