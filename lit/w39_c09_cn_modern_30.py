#!/usr/bin/env python3
"""Wave 39: add 30 ultra-niche concepts to lit_cn_modern."""

from lit_db_helper import LitDB

REGION = "東アジア"
SUBFIELD = "lit_cn_modern"

P_WUSI = 24
P_WAR = 25
P_MAO = 26
P_REFORM = 27


CONCEPTS = [
    # 1. 晩清・民初の小雑誌と忘れられた作品
    ("『月月小説』", "All-Story Monthly", "月月小説", P_WUSI, "1906年創刊の晩清小説月刊。新小説の連載場。"),
    ("『繍像小説』", "Illustrated Fiction", "繡像小說", P_WUSI, "1903年創刊の図像入り小説誌。譴責小説を普及。"),
    ("呉趼人『新石頭記』", "New Story of the Stone", "新石頭記", P_WUSI, "1908年連載のSF的続紅楼夢。近代文明批評を展開。"),
    ("徐念慈『新法螺先生譚』", "New Mr Braggadocio", "新法螺先生譚", P_WUSI, "1905年の科学幻想小説。月世界旅行で文明を諷刺。"),
    ("陳天華『獅子吼』", "Lion's Roar", "獅子吼", P_WUSI, "1905年革命小説。民族覚醒を寓言的英雄譚に託す。"),
    ("蘇曼殊『断鴻零雁記』", "Broken Swan Notes", "斷鴻零雁記", P_WUSI, "1912年の哀感小説。僧と孤児の恋を文言白話混淆で描く。"),
    # 2. 1930年代小流派・小媒体
    ("『無軌列車』新感覚派誌", "Trackless Train", "無軌列車", P_WAR, "1928年上海の新感覚派同人誌。都市速度感を実験。"),
    ("『水星』京派小誌", "Mercury Beijing School", "水星", P_WAR, "1934年創刊の京派文芸誌。沈従文らの純文学拠点。"),
    ("東北作家群『科爾沁旗草原』", "Horqin Grassland", "科爾沁旗草原", P_WAR, "端木蕻良の1939年長編。満洲草原の植民地暴力を描く。"),
    ("中国詩歌会", "Chinese Poetry Society", "中國詩歌會", P_WAR, "1932年上海結成の左翼詩歌団体。街頭朗誦を重視。"),
    ("『七月』詩派", "July Poetry School", "七月", P_WAR, "胡風周辺の抗戦詩派。主観戦闘精神を掲げた。"),
    ("九葉派『中国新詩』", "Nine Leaves Chinese New Poetry", "中國新詩", P_WAR, "1940年代後半のモダニズム詩誌。都市知性を追求。"),
    # 3. 抗戦・左翼演劇と小説
    ("夏衍『上海屋檐下』", "Under Shanghai Eaves", "上海屋簷下", P_WAR, "1937年話劇。上海長屋の群像で戦前市民生活を描く。"),
    ("夏衍『法西斯細菌』", "Fascist Bacillus", "法西斯細菌", P_WAR, "1942年話劇。日中戦争下の知識人と疫病隠喩を扱う。"),
    ("路翎『財主底兒女們』", "Children of the Rich", "財主底兒女們", P_WAR, "1945年長編。地主家庭崩壊を心理リアリズムで描く。"),
    ("沙汀『淘金記』", "Gold Rush", "淘金記", P_WAR, "1943年長編。四川鉱区の利権と地方社会を風刺。"),
    ("張天翼『華威先生』", "Mr Hua Wei", "華威先生", P_WAR, "1938年短編。抗戦期の空疎な会議政治家を諷刺。"),
    ("艾蕪『南行記』", "Journey South", "南行記", P_WAR, "1935年短編集。雲南辺境の流浪者と少数民族地帯を描く。"),
    # 4. 1950-70年代の周辺的紅色叙事
    ("曲波『林海雪原』", "Tracks in the Snowy Forest", "林海雪原", P_MAO, "1957年長編。東北匪賊討伐を冒険活劇化した紅色小説。"),
    ("杜鵬程『保衛延安』", "Defend Yan'an", "保衛延安", P_MAO, "1954年長編。国共内戦の延安防衛を集団英雄で描く。"),
    ("李英儒『野火春風斗古城』", "Wildfire Spring Wind", "野火春風斗古城", P_MAO, "1958年長編。地下抗日組織の都市潜入戦を描く。"),
    ("馮徳英『苦菜花』", "Bitter Cauliflower", "苦菜花", P_MAO, "1958年長編。山東農村女性の抗日参加を紅色家族史化。"),
    ("金敬邁『欧陽海之歌』", "Song of Ouyang Hai", "歐陽海之歌", P_MAO, "1965年長編。兵士殉難を雷鋒式英雄譚にしたベストセラー。"),
    ("張揚『第二次握手』", "Second Handshake", "第二次握手", P_MAO, "文革期手稿小説。科学者恋愛物語として地下流通した。"),
    # 5. 改革開放期の地方・短篇・変種
    ("莫言『透明的紅蘿蔔』", "Transparent Red Radish", "透明的紅蘿蔔", P_REFORM, "1985年中篇。少年労働者の感覚世界を高密度比喩で描く。"),
    ("王安憶『小鮑荘』", "Xiaobao Village", "小鮑莊", P_REFORM, "1985年中篇。村落共同体の倫理を尋根文学として再構成。"),
    ("張煒『古船』", "Ancient Ship", "古船", P_REFORM, "1986年長編。膠東の町史から革命と家族暴力を掘る。"),
    ("格非『迷舟』", "Lost Boat", "迷舟", P_REFORM, "1987年短編。歴史叙述の迷路化で先鋒小説を代表。"),
    ("劉恒『伏羲伏羲』", "Fuxi Fuxi", "伏羲伏羲", P_REFORM, "1987年中篇。農村欲望と家族禁忌を寓話的に描く。"),
    ("馬原『岡底斯的誘惑』", "Temptation of Gangdise", "岡底斯的誘惑", P_REFORM, "1985年短編。チベット旅行譚で叙述の真偽を撹乱。"),
]


def main():
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, original, period_id, definition in CONCEPTS:
            before = db.find_concept(name_ja, REGION, period_id)
            cid = db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=original,
                original_script="kanji",
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            if before is None and cid:
                inserted += 1
    print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
