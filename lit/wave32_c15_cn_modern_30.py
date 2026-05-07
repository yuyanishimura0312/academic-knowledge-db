#!/usr/bin/env python3
"""Wave32 C15: Add 30 new concepts to lit_cn_modern (subfield_id=9).
5 thematic clusters x 6 concepts. Definitions <= 100 chars."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 9
REGION = "東アジア"

# Period mapping (region=東アジア)
P_MAY4 = 24       # 五四運動期
P_REPUB = 25      # 国民革命〜抗戦期
P_MAO = 26        # 毛沢東期
P_REFORM = 27     # 改革開放期
P_MODERN = 12     # 現代

CONCEPTS_REPLACE = [
    # Replacements for duplicates (10)
    ("楊沫『東方欲暁』", "Dawn in the East", "东方欲晓", "kanji", P_MAO,
     "楊沫1980年長編。『青春之歌』の続編、革命知識人の戦時延安経験を描く。", 3, "partial"),
    ("浩然『金光大道』", None, None, None, None, None, None, None),  # already exists, skip duplicate handling
    ("劉心武『鐘鼓楼』", "Bell and Drum Tower", "钟鼓楼", "kanji", P_REFORM,
     "劉心武1984年長編、茅盾文学賞。北京一日の市民群像で社会主義都市生活を記録。", 4, "invariant"),
    ("韓少功『馬橋詞典』", "A Dictionary of Maqiao", "马桥词典", "kanji", P_REFORM,
     "韓少功1996年辞書体長編。湘西馬橋村方言の115語彙で集合記憶を構築。", 5, "rethinking"),
    ("阿城『樹王』", "The King of Trees", "树王", "kanji", P_REFORM,
     "阿城1985年中編。下放青年と古樹守人の相克を通じ自然と革命の対立を描く。", 4, "rethinking"),
    ("莫言『豊乳肥臀』", "Big Breasts and Wide Hips", "丰乳肥臀", "kanji", P_REFORM,
     "莫言1995年長編。母を中心とする20世紀中国家族史を母系視点から描出。", 5, "rethinking"),
    ("余華『許三観売血記』", "Chronicle of a Blood Merchant", "许三观卖血记", "kanji", P_REFORM,
     "余華1995年長編。売血で家族を支える庶民の40年史、生存の倫理を問う。", 5, "invariant"),
    ("劉慈欣『球状閃電』", "Ball Lightning", "球状闪电", "kanji", P_MODERN,
     "劉慈欣2004年長編。球電の科学的探求と軍事応用、ハードSFの先駆作。", 4, "rethinking"),
    ("賈平凹『秦腔』", "Qin Opera", "秦腔", "kanji", P_MODERN,
     "賈平凹2005年長編、茅盾文学賞。陝西農村と地方戯曲の凋落を綿密に記録。", 5, "rethinking"),
    ("麦家『風声』", "The Message", "风声", "kanji", P_MODERN,
     "麦家2007年長編。汪精衛政権下の諜報内通者捜索、密室推理諜報叙事。", 4, "invariant"),
]

CONCEPTS = [
    # Cluster 1: 五四運動 (魯迅野草, 周作人雨天的書, 胡適嘗試集, 郭沫若女神, 茅盾蝕三部, 巴金家)
    # Existing already cover these works → use related/derivative concepts
    ("魯迅『阿Q正伝』", "The True Story of Ah Q", "阿Q正伝", "kanji", P_MAY4,
     "魯迅1921-22年中編小説。精神勝利法で自己慰安する阿Qを描き国民性批判の象徴となった。", 5, "rethinking"),
    ("魯迅『吶喊』", "Call to Arms", "吶喊", "kanji", P_MAY4,
     "魯迅1923年短編集。狂人日記・孔乙己・故郷等収録。中国現代小説の出発点。", 5, "invariant"),
    ("周作人『談龍集』", "Tan Long Ji", "談龍集", "kanji", P_MAY4,
     "周作人1927年雑文集。閑適散文と人道主義論を展開、五四散文の典型。", 4, "partial"),
    ("胡適『文学改良芻議』", "Suggestions for Literary Reform", "文学改良芻議", "kanji", P_MAY4,
     "胡適1917年論文。八不主義を掲げ白話文学運動の理論的礎石となった。", 5, "invariant"),
    ("郭沫若『屈原研究』", "Studies on Qu Yuan", "屈原研究", "kanji", P_MAY4,
     "郭沫若の屈原論考群。古代と現代を橋渡しする民族的浪漫精神の探求。", 4, "partial"),
    ("茅盾『虹』", "Rainbow", "虹", "kanji", P_MAY4,
     "茅盾1929年長編。五四運動から五卅運動への女性知識人の精神遍歴を描く。", 4, "partial"),

    # Cluster 2: 1930s小説
    ("老舎『離婚』", "Divorce", "離婚", "kanji", P_REPUB,
     "老舎1933年長編。北京小役人の凡庸な日常をユーモアで描く都市諷刺小説。", 4, "invariant"),
    ("沈従文『長河』", "Long River", "長河", "kanji", P_REPUB,
     "沈従文1938-43年未完長編。湘西の近代化による牧歌的世界の解体を描く。", 4, "rethinking"),
    ("蕭紅『商市街』", "Market Street", "商市街", "kanji", P_REPUB,
     "蕭紅1936年自伝的散文集。哈爾濱貧困生活の女性視点記録。", 4, "rethinking"),
    ("蕭軍『第三代』", "The Third Generation", "第三代", "kanji", P_REPUB,
     "蕭軍1937-50年大河小説。東北農村三代史を通じ革命と土地の運命を描く。", 3, "partial"),
    ("端木蕻良『鴜鷺湖的憂鬱』", "Melancholy of Cilu Lake", "鴜鷺湖的憂鬱", "kanji", P_REPUB,
     "端木蕻良1936年中編。東北農村の閉塞と若者の苦悶を抒情的に描く。", 3, "invariant"),
    ("駱賓基『北望園的春天』", "Spring of Beiwang Garden", "北望園的春天", "kanji", P_REPUB,
     "駱賓基1944年小説集。抗戦下の知識人群像を抑制された筆致で描く。", 3, "invariant"),

    # Cluster 3: 戦時+建国初期
    ("姚雪垠『李自成』", "Li Zicheng", "李自成", "kanji", P_MAO,
     "姚雪垠1963-99年大河歴史小説。明末農民反乱を共産主義史観で再構成した巨編。", 4, "rethinking"),
    ("趙樹理『三里湾』", "Sanliwan", "三里湾", "kanji", P_MAO,
     "趙樹理1955年長編。農業合作化運動下の村落人間関係を山薬蛋派様式で描く。", 4, "partial"),
    ("周立波『山郷巨変』", "Great Changes in a Mountain Village", "山郷巨変", "kanji", P_MAO,
     "周立波1958-60年長編。湖南農村合作化を抒情的筆致で描いた建国初期傑作。", 4, "partial"),
    ("楊沫『青春之歌』", "Song of Youth", "青春之歌", "kanji", P_MAO,
     "楊沫1958年長編。知識女性林道静が革命に目覚める成長譚、紅色経典の代表。", 4, "rethinking"),
    ("浩然『艷陽天』", "Bright Sunny Day", "艷陽天", "kanji", P_MAO,
     "浩然1964-66年三巻長編。集団化期の階級闘争を理想化、文革直前の代表作。", 3, "rethinking"),
    ("革命様板戯八大", "Eight Model Operas", "革命样板戏八大", "kanji", P_MAO,
     "文革期江青指導下の八大革命模範劇。京劇・バレエ等を社会主義様式に再編。", 4, "rethinking"),

    # Cluster 4: 新時期
    ("劉心武『班主任』", "The Class Teacher", "班主任", "kanji", P_REFORM,
     "劉心武1977年短編。文革被害を受けた青少年を描き傷痕文学の幕を開けた。", 5, "invariant"),
    ("韓少功『爸爸爸』", "Pa Pa Pa", "爸爸爸", "kanji", P_REFORM,
     "韓少功1985年中編。湘西山村の白痴少年を通じ民族文化深層を探る尋根代表作。", 5, "rethinking"),
    ("阿城『棋王』", "The Chess King", "棋王", "kanji", P_REFORM,
     "阿城1984年中編。下放青年王一生の道家的棋道、尋根文学の精神的源流。", 5, "invariant"),
    ("莫言『紅高粱家族』", "Red Sorghum Clan", "红高粱家族", "kanji", P_REFORM,
     "莫言1986-87年連作。山東高密の祖父母世代の生命力を魔幻リアリズムで描出。", 5, "invariant"),
    ("余華『活着』", "To Live", "活着", "kanji", P_REFORM,
     "余華1993年長編。地主息子福貴の20世紀苦難史を通じ生存の意味を問う。", 5, "invariant"),
    ("王安憶『長恨歌』", "Song of Everlasting Sorrow", "长恨歌", "kanji", P_REFORM,
     "王安憶1995年長編。上海女性王琦瑤の40年生涯を通じ都市記憶を再構築。", 5, "invariant"),

    # Cluster 5: 現代21c
    ("劉慈欣『三体』", "The Three-Body Problem", "三体", "kanji", P_MODERN,
     "劉慈欣2006-10年三部作。文革と宇宙文明接触を結ぶハードSF、世界的影響を持つ。", 5, "rethinking"),
    ("残雪『黄泥街』", "Yellow Mud Street", "黄泥街", "kanji", P_MODERN,
     "残雪1987年代表中編。腐敗した街の悪夢的叙述、女性前衛派の到達点。", 4, "rethinking"),
    ("賈平凹『廃都』", "Ruined City", "废都", "kanji", P_MODERN,
     "賈平凹1993年長編。古都西安の知識人荘之蝶の頽廃、90年代精神危機を象徴。", 5, "rethinking"),
    ("閻連科『日光流年』", "Days, Months, Years", "日光流年", "kanji", P_MODERN,
     "閻連科1998年長編。短命村住民が長寿を求める寓話、神実主義の代表作。", 5, "rethinking"),
    ("麦家『暗算』", "Plot Against", "暗算", "kanji", P_MODERN,
     "麦家2003年長編。秘密情報員たちの諜報叙事を通じ天才と運命を描く。", 4, "invariant"),
    ("双雪涛『飛行員』", "The Aviator", "飞行员", "kanji", P_MODERN,
     "双雪涛2017年短編集。東北衰退工業都市を背景にした記憶と幻想の物語。", 4, "rethinking"),
]

def main():
    conn = sqlite3.connect(str(DB))
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    # Use only valid replacement entries (skip placeholder None tuples)
    valid_replacements = [c for c in CONCEPTS_REPLACE if c[1] is not None]
    for name_ja, name_en, name_orig, script, period_id, definition, importance, fourth in valid_replacements:
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id,
                 region, period_id, definition, importance_score,
                 fourth_transform_status, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, script, SUBFIELD_ID,
                  REGION, period_id, definition, importance,
                  fourth, "tier2", "yes" if importance >= 5 else "no"))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=9").fetchone()[0]
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total subfield_id=9: {total}")

if __name__ == "__main__":
    main()
