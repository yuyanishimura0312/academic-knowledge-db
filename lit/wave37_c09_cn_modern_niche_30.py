#!/usr/bin/env python3
"""Wave 37: lit_cn_modern (subfield_id=9) +30 niche concepts, 5 thematic clusters."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 9
REGION = "東アジア"

# period mapping
P_WUSI = 24       # 五四運動期 1915-1927
P_KANGSEN = 25    # 国民革命〜抗戦期 1927-1949
P_MAO = 26        # 毛沢東期 1949-1976
P_REFORM = 27     # 改革開放期 1976-1989
P_GENDAI = 12     # 現代 1970-2025

CONCEPTS = [
    # Cluster 1: 五四運動細部 (period 24, some 25)
    ("魯迅『野草』散文詩集", "Lu Xun Wild Grass", "野草", "kanji", P_WUSI,
     "魯迅1927年散文詩集、夢と象徴で内面の絶望と抗争を凝縮した実験的小品集。"),
    ("老舎『駱駝祥子』人力車夫悲劇", "Lao She Camel Xiangzi", "駱駝祥子", "kanji", P_KANGSEN,
     "老舎1936年長編、北平人力車夫祥子の没落を通じ都市底辺と個人理想の崩壊を描く。"),
    ("茅盾『子夜』金融資本叙事", "Mao Dun Midnight", "子夜", "kanji", P_KANGSEN,
     "茅盾1933年長編、上海金融資本家呉蓀甫の崩壊で半植民地中国経済を社会全景的に描く。"),
    ("巴金『家』封建家族解体", "Ba Jin Family", "家", "kanji", P_WUSI,
     "巴金1933年長編、四川高家三兄弟を通じ封建家族制度の抑圧と若者の覚醒を描く。"),
    ("冰心『寄小読者』児童散文", "Bing Xin To Young Readers", "寄小読者", "kanji", P_WUSI,
     "冰心1923-26年書簡体散文、母性愛・自然・童心の三主題で現代児童文学の起点を成す。"),
    ("徐志摩『再別康橋』新月派抒情", "Xu Zhimo Cambridge", "再別康橋", "kanji", P_WUSI,
     "徐志摩1928年自由詩、ケンブリッジ離別を音楽的格律で歌い新月派抒情詩の代表作となる。"),

    # Cluster 2: 抗戦期 (period 25)
    ("艾青『北方』抗戦詩", "Ai Qing Northland", "北方", "kanji", P_KANGSEN,
     "艾青1939年長詩集、土地と農民への深い愛と抗日戦の悲愴を散文的自由律で結晶化。"),
    ("丁玲『太陽照在桑乾河上』土改文学", "Ding Ling Sun Sanggan", "太陽照在桑乾河上", "kanji", P_KANGSEN,
     "丁玲1948年長編、華北土地改革の階級闘争を描きスターリン文学賞受賞、解放区典範化。"),
    ("孫犁「荷花淀」白洋淀詩派", "Sun Li Lotus Lake", "荷花淀", "kanji", P_KANGSEN,
     "孫犁1945年短編、白洋淀の女性たちの抗日活動を抒情的清新文体で描き荷花淀派を創始。"),
    ("趙樹理『李家荘的変遷』農民叙事", "Zhao Shuli Lijiazhuang", "李家荘的変遷", "kanji", P_KANGSEN,
     "趙樹理1946年長編、山西農村李家荘の十数年変遷を通俗講談体で描き工農兵文芸を確立。"),
    ("田漢『関漢卿』歴史劇", "Tian Han Guan Hanqing", "関漢卿", "kanji", P_MAO,
     "田漢1958年話劇、元代劇作家関漢卿の創作と抵抗を描き新中国歴史劇の代表作となる。"),
    ("曹禺『雷雨』家庭悲劇", "Cao Yu Thunderstorm", "雷雨", "kanji", P_KANGSEN,
     "曹禺1934年四幕劇、周家三十年の秘密と階級・血縁の網が雷雨の夜に崩壊する古典話劇。"),

    # Cluster 3: 文革・新時期 (periods 26, 27)
    ("王蒙『布礼』意識流", "Wang Meng Bolshevik Salute", "布礼", "kanji", P_REFORM,
     "王蒙1979年中編、革命幹部の意識流回想で反右派から文革までの理想と苦難を再構成。"),
    ("北島『回答』朦朧詩宣言", "Bei Dao Answer", "回答", "kanji", P_REFORM,
     "北島1976年詩、「卑劣は卑劣者の通行証」で始まり朦朧詩運動と個人の覚醒を象徴する。"),
    ("芒克『陽光中的向日葵』地下詩", "Mang Ke Sunflower Sun", "陽光中的向日葵", "kanji", P_MAO,
     "芒克1970年代詩、太陽に従わない向日葵で文革時代の精神的反逆を白洋淀詩群として歌う。"),
    ("顧城「一代人」朦朧詩", "Gu Cheng Generation", "一代人", "kanji", P_REFORM,
     "顧城1979年二行詩、「黒夜は私に黒い瞳を与えた」で文革世代の喪失と希求を凝縮する。"),
    ("韓少功『爸爸爸』尋根文学", "Han Shaogong Daddy Daddy", "爸爸爸", "kanji", P_REFORM,
     "韓少功1985年中編、湖南山村の白痴丙崽を通じ楚文化の原始性と中国民族劣根性を尋根。"),
    ("莫言『紅高粱』新歴史小説", "Mo Yan Red Sorghum", "紅高粱", "kanji", P_REFORM,
     "莫言1986年中編、山東高密の祖父母世代の抗日と恋愛を野性的感覚で語る新歴史叙事。"),

    # Cluster 4: 90年代以降 (period 12)
    ("余華『活着』苦難叙事", "Yu Hua To Live", "活着", "kanji", P_GENDAI,
     "余華1993年長編、福貴一人の数十年を通じ国共内戦から文革までの苦難と生存力を描く。"),
    ("蘇童『妻妾成群』新歴史小説", "Su Tong Wives Concubines", "妻妾成群", "kanji", P_GENDAI,
     "蘇童1989年中編、民国期陳家四夫人の妻妾闘争を通じ封建家族の腐敗と女性の悲劇を描く。"),
    ("王安憶『長恨歌』上海叙事", "Wang Anyi Song Everlasting Sorrow", "長恨歌", "kanji", P_GENDAI,
     "王安憶1995年長編、上海女王琦瑶の四十年運命で都市記憶と海派文化の終焉を描く。"),
    ("鉄凝『大浴女』女性身体叙事", "Tie Ning Bathing Women", "大浴女", "kanji", P_GENDAI,
     "鉄凝2000年長編、姉妹三人の身体と記憶を通じ文革後女性の罪責と自己救済を探求。"),
    ("畢飛宇『青衣』戯曲世界", "Bi Feiyu Moon Opera", "青衣", "kanji", P_GENDAI,
     "畢飛宇2000年中編、京劇女優筱燕秋の嫦娥役執念を通じ芸術と現実の裂け目を描く心理小説。"),
    ("劉震雲『手機』風俗小説", "Liu Zhenyun Cellphone", "手機", "kanji", P_GENDAI,
     "劉震雲2003年長編、TV司会者の携帯通信を通じ現代中国の言語・嘘・婚姻倫理を諷刺する。"),

    # Cluster 5: 現代中国 (period 12)
    ("閻連科『丁庄夢』神実主義", "Yan Lianke Dream Ding Village", "丁庄夢", "kanji", P_GENDAI,
     "閻連科2006年長編、河南売血エイズ村を死者の語りで描き神実主義による中国現実批判。"),
    ("劉慈欣『三体』中国SF", "Liu Cixin Three Body", "三体", "kanji", P_GENDAI,
     "劉慈欣2008年三部作、文革から宇宙終末まで黒暗森林理論で展開しヒューゴー賞受賞。"),
    ("韓寒『三重門』80後文学", "Han Han Triple Door", "三重門", "kanji", P_GENDAI,
     "韓寒2000年長編、高校生林雨翔の挫折を通じ中国教育制度を諷刺し80後世代の旗手となる。"),
    ("慕容雪村『成都、今夜請将我遺忘』網絡文学", "Murong Xuecun Chengdu", "成都、今夜請将我遺忘", "kanji", P_GENDAI,
     "慕容雪村2002年網絡小説、成都ホワイトカラーの堕落と虚無を描き網絡文学商業化の起点。"),
    ("安妮宝貝『告別薇安』女性網絡文学", "Anni Baobei Goodbye Vivian", "告別薇安", "kanji", P_GENDAI,
     "安妮宝貝1999年短編、都市女性の虚無と疎外を網絡発表し女性向け網絡文学のブームを創出。"),
    ("劉震雲『一句頂一万句』喧鬧叙事", "Liu Zhenyun One Sentence", "一句頂一万句", "kanji", P_GENDAI,
     "劉震雲2009年長編、河南楊百順の言葉を求める百年放浪で中国人の孤独と話相手を探求。"),
]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # existing names check
    existing = {r[0] for r in cur.execute(
        "SELECT name_ja FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)
    )}

    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, period_id, definition in CONCEPTS:
        if name_ja in existing:
            print(f"  SKIP exists: {name_ja}")
            skipped += 1
            continue
        if len(definition) > 100:
            print(f"  WARN definition too long ({len(definition)}): {name_ja}")
        try:
            cur.execute(
                """INSERT INTO concepts
                   (name_ja, name_en, name_original, original_script,
                    subfield_id, region, period_id, definition,
                    importance_score, source_tier, canonical_in_region)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, 3, 'A', 'CN')""",
                (name_ja, name_en, name_orig, script,
                 SUBFIELD_ID, REGION, period_id, definition),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"  INTEGRITY {name_ja}: {e}")
            skipped += 1

    conn.commit()
    total = cur.execute(
        "SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)
    ).fetchone()[0]
    conn.close()
    print(f"Wave37 lit_cn_modern: inserted={inserted} skipped={skipped} total_in_subfield={total}")


if __name__ == "__main__":
    main()
