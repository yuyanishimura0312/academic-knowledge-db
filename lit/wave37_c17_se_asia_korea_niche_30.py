#!/usr/bin/env python3
"""Wave 37 - subfield 17 (lit_se_asia_korea) niche 30 concepts."""
import sqlite3
import os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lit.sqlite")
SUBFIELD_ID = 17
REGION = "グローバルサウス"

# period mapping
P_KOR_CLASSIC = 153   # 韓国古典文学期 600-1900
P_KOR_MODERN = 154    # 韓国近現代文学期 1894-2030
P_VN_CLASSIC = 155    # ベトナム古典・近世 1000-1900
P_VN_MODERN = 156     # ベトナム近現代 1900-2030
P_TH_CLASSIC = 157    # タイ古典・宮廷文学期 1350-1900
P_TH_MODERN = 158     # タイ近現代 1900-2030
P_KH_LA_CLASSIC = 163 # カンボジア・ラオス古典期
P_PH_CLASSIC = 161    # フィリピン古典・スペイン期
P_PH_MODERN = 162     # フィリピン近現代
P_MAL_CLASSIC = 159   # マレー・インドネシア古典口承期
P_INDO_MODERN = 160   # インドネシア・マレーシア近現代

# 30 concepts × 5 clusters
concepts = [
    # Cluster 1: 韓国古典 (6)
    {
        "name_ja": "郷歌（ヒャンガ）詳説",
        "name_en": "Hyangga (Old Korean vernacular poetry)",
        "name_original": "鄉歌",
        "original_script": "hanja",
        "period_id": P_KOR_CLASSIC,
        "definition": "新羅・高麗初期の郷札表記による土着詩歌。『三国遺事』14首・『均如伝』11首が現存。",
    },
    {
        "name_ja": "高麗歌謡",
        "name_en": "Goryeo gayo",
        "name_original": "高麗歌謠",
        "original_script": "hanja",
        "period_id": P_KOR_CLASSIC,
        "definition": "高麗朝の口承叙情歌謡群。『青山別曲』『動動』等。男女相悦の俗謡として朝鮮朝に記録。",
    },
    {
        "name_ja": "時調（シジョ）古典形式",
        "name_en": "Sijo (classical Korean verse)",
        "name_original": "時調",
        "original_script": "hanja",
        "period_id": P_KOR_CLASSIC,
        "definition": "三章四十五字内外の朝鮮固有定型詩。平時調・辞説時調等の派生形を持つ士大夫文芸。",
    },
    {
        "name_ja": "歌辞（ガサ）",
        "name_en": "Gasa (Korean narrative verse)",
        "name_original": "歌辭",
        "original_script": "hanja",
        "period_id": P_KOR_CLASSIC,
        "definition": "四・四調を基調とする長歌的韻文形式。鄭澈『関東別曲』等の士大夫紀行・教訓詩を含む。",
    },
    {
        "name_ja": "訓民正音",
        "name_en": "Hunminjeongeum",
        "name_original": "訓民正音",
        "original_script": "hanja",
        "period_id": P_KOR_CLASSIC,
        "definition": "1446年世宗公布のハングル創製文書。母音・子音の音韻論的設計と民衆教化思想を提示。",
    },
    {
        "name_ja": "春香伝（チュニャンジョン）詳説",
        "name_en": "Chunhyangjeon",
        "name_original": "春香傳",
        "original_script": "hanja",
        "period_id": P_KOR_CLASSIC,
        "definition": "朝鮮後期パンソリ系小説。妓生春香と両班子弟李夢龍の貞節譚で身分制批判を含む国民物語。",
    },

    # Cluster 2: 韓国近現代 (6)
    {
        "name_ja": "李光洙『無情』詳説",
        "name_en": "Yi Kwang-su Mujeong",
        "name_original": "無情",
        "original_script": "hanja",
        "period_id": P_KOR_MODERN,
        "definition": "1917年連載の韓国最初の近代長編小説。啓蒙主義と自由恋愛・民族再生の三角関係を描く。",
    },
    {
        "name_ja": "金東仁『灼熱』",
        "name_en": "Kim Tong-in Jakyeol",
        "name_original": "灼熱",
        "original_script": "hanja",
        "period_id": P_KOR_MODERN,
        "definition": "金東仁の自然主義短編。芸術至上主義と運命の残酷を簡潔な文体で抉る初期近代小説の代表。",
    },
    {
        "name_ja": "廉想涉『三代』",
        "name_en": "Yeom Sang-seop Samdae",
        "name_original": "三代",
        "original_script": "hanja",
        "period_id": P_KOR_MODERN,
        "definition": "1931年連載長編。京城の趙家三世代を通じ植民地下のブルジョア家族と思想対立を描いた。",
    },
    {
        "name_ja": "蔡萬植『太平天下』",
        "name_en": "Chae Man-sik Taepyeong cheonha",
        "name_original": "太平天下",
        "original_script": "hanja",
        "period_id": P_KOR_MODERN,
        "definition": "1938年発表の風刺長編。植民地期に栄える地主尹直元一家を皮肉な語りで戯画化した傑作。",
    },
    {
        "name_ja": "李箱『翼』",
        "name_en": "Yi Sang Nalgae",
        "name_original": "翼",
        "original_script": "hanja",
        "period_id": P_KOR_MODERN,
        "definition": "1936年発表のモダニズム短編。妓生の夫である語り手の意識の流れで都市と自我崩壊を描く。",
    },
    {
        "name_ja": "韓龍雲『君の沈黙』詳説",
        "name_en": "Han Yong-un Nimui chimmuk",
        "name_original": "님의 沈默",
        "original_script": "hangul",
        "period_id": P_KOR_MODERN,
        "definition": "1926年詩集。仏教・恋愛・民族独立を多義的「君」に重ね朝鮮近代詩の象徴主義を確立した。",
    },

    # Cluster 3: ベトナム文学 (6)
    {
        "name_ja": "阮攸『金雲翹（チュエン・キエウ）』詳説",
        "name_en": "Nguyễn Du Truyện Kiều",
        "name_original": "Truyện Kiều",
        "original_script": "chu_nom",
        "period_id": P_VN_CLASSIC,
        "definition": "3,254行の六八体字喃叙事詩。翠翹の流転を通じ才命相妬の運命観を展開した国民叙事詩。",
    },
    {
        "name_ja": "胡春香の艶詩",
        "name_en": "Hồ Xuân Hương poetry",
        "name_original": "Hồ Xuân Hương",
        "original_script": "chu_nom",
        "period_id": P_VN_CLASSIC,
        "definition": "18-19世紀女性詩人の字喃詩。二重意味と性的隠喩で儒教社会の偽善を風刺した諧謔詩学。",
    },
    {
        "name_ja": "阮丙の民謡詩",
        "name_en": "Nguyễn Bính folk poetry",
        "name_original": "Nguyễn Bính",
        "original_script": "quoc_ngu",
        "period_id": P_VN_MODERN,
        "definition": "1930-40年代詩人。ロマン派『新詩』運動下で農村と恋愛を六八体民謡調で歌った叙情詩。",
    },
    {
        "name_ja": "ヴー・チョン・フン『紅運（ソー・ドー）』",
        "name_en": "Vũ Trọng Phụng Số Đỏ",
        "name_original": "Số Đỏ",
        "original_script": "quoc_ngu",
        "period_id": P_VN_MODERN,
        "definition": "1936年連載の風刺長編。投機家紅毛の出世譚で植民地ハノイの欧化と偽近代を笑殺した。",
    },
    {
        "name_ja": "ナム・カオ『チ・フェオ』",
        "name_en": "Nam Cao Chí Phèo",
        "name_original": "Chí Phèo",
        "original_script": "quoc_ngu",
        "period_id": P_VN_MODERN,
        "definition": "1941年短編。村の浮浪者チー・フェーオの転落と尊厳の渇望でベトナム社会主義リアリズム源流。",
    },
    {
        "name_ja": "バオ・ニン『戦争の悲しみ』詳説",
        "name_en": "Bảo Ninh The Sorrow of War",
        "name_original": "Nỗi buồn chiến tranh",
        "original_script": "quoc_ngu",
        "period_id": P_VN_MODERN,
        "definition": "1990年長編。北兵キエンの記憶錯綜でベトナム戦争を勝者神話から脱構築したドイモイ期傑作。",
    },

    # Cluster 4: タイ・カンボジア・ラオス (6)
    {
        "name_ja": "スントーン・プー『プラ・アパイ・マニ』詳説",
        "name_en": "Sunthorn Phu Phra Aphai Mani",
        "name_original": "พระอภัยมณี",
        "original_script": "thai",
        "period_id": P_TH_CLASSIC,
        "definition": "19世紀タイの長編叙事詩。笛吹き王子の海洋冒険でクローン詩形を国民文学に押し上げた。",
    },
    {
        "name_ja": "クンチャン・クンペーン詳説",
        "name_en": "Khun Chang Khun Phaen",
        "name_original": "ขุนช้างขุนแผน",
        "original_script": "thai",
        "period_id": P_TH_CLASSIC,
        "definition": "アユタヤ起源・ラタナコーシン期完成の口承叙事詩。三角関係と戦闘でタイ社会全体を映す。",
    },
    {
        "name_ja": "リアムケー（カンボジア・ラーマーヤナ）詳説",
        "name_en": "Reamker",
        "name_original": "រាមកេរ្តិ៍",
        "original_script": "khmer",
        "period_id": P_KH_LA_CLASSIC,
        "definition": "クメール版ラーマーヤナ。仏教世界観で再話され王宮舞踊・影絵に転生した国民的叙事詩。",
    },
    {
        "name_ja": "プラ・ラック・プラ・ラム（ラオ・ラーマーヤナ）",
        "name_en": "Phra Lak Phra Lam",
        "name_original": "ພະລັກພະລາມ",
        "original_script": "lao",
        "period_id": P_KH_LA_CLASSIC,
        "definition": "ラオス版ラーマーヤナ叙事詩。仏教ジャータカ化されメコン流域の宮廷・寺院文芸を担った。",
    },
    {
        "name_ja": "チャート・コープチッティ『判決』詳説",
        "name_en": "Chart Korbjitti The Judgement",
        "name_original": "คำพิพากษา",
        "original_script": "thai",
        "period_id": P_TH_MODERN,
        "definition": "1981年長編。村人の冤罪と差別を冷徹に描きSEAライト賞受賞、現代タイ文学を代表する作品。",
    },
    {
        "name_ja": "シーダーオルアン",
        "name_en": "Sidaoruang",
        "name_original": "ศรีดาวเรือง",
        "original_script": "thai",
        "period_id": P_TH_MODERN,
        "definition": "労働者出身の女性短編作家。70年代以降の貧困・女性労働を平易な口語で描く社会派文学。",
    },

    # Cluster 5: フィリピン・マレー・インドネシア (6)
    {
        "name_ja": "ホセ・リサール『ノリ・メ・タンヘレ』詳説",
        "name_en": "José Rizal Noli Me Tangere",
        "name_original": "Noli Me Tangere",
        "original_script": "latin",
        "period_id": P_PH_CLASSIC,
        "definition": "1887年スペイン語長編。聖職者の腐敗と植民地搾取を暴き比島革命の精神的起爆剤となった。",
    },
    {
        "name_ja": "バラグタス『フロランテとラウラ』詳説",
        "name_en": "Balagtas Florante at Laura",
        "name_original": "Florante at Laura",
        "original_script": "latin",
        "period_id": P_PH_CLASSIC,
        "definition": "1838年タガログ語アウィット叙事詩。アルバニア舞台の寓意でスペイン圧政を批判した古典。",
    },
    {
        "name_ja": "ヒカヤット・ハン・トゥア",
        "name_en": "Hikayat Hang Tuah",
        "name_original": "Hikayat Hang Tuah",
        "original_script": "jawi",
        "period_id": P_MAL_CLASSIC,
        "definition": "17世紀マラッカ提督の英雄ヒカヤット。忠誠と武勇でマレー世界の理想戦士像を確立した。",
    },
    {
        "name_ja": "プラムディヤ『ブル四部作』詳説",
        "name_en": "Pramoedya Buru Quartet",
        "name_original": "Tetralogi Buru",
        "original_script": "latin",
        "period_id": P_INDO_MODERN,
        "definition": "ブル島流刑中口述の四部作。ミンケを通じ蘭領東インド民族意識の覚醒を描いた歴史長編。",
    },
    {
        "name_ja": "チャイリル・アンワル『俺』",
        "name_en": "Chairil Anwar Aku",
        "name_original": "Aku",
        "original_script": "latin",
        "period_id": P_INDO_MODERN,
        "definition": "1943年詩。「俺は野獣のごとく」との自己宣言で45年世代インドネシア近代詩を切り開いた。",
    },
    {
        "name_ja": "F・シオニル・ホセ『ロサーレス・サーガ』詳説",
        "name_en": "F. Sionil José Rosales Saga",
        "name_original": "Rosales Saga",
        "original_script": "latin",
        "period_id": P_PH_MODERN,
        "definition": "五部作英語長編。ルソン島ロサーレス村のサンフアン家百年史で比島階級・植民地を貫く。",
    },
]

assert len(concepts) == 30, len(concepts)
for c in concepts:
    assert len(c["definition"]) <= 100, (len(c["definition"]), c["name_ja"])

conn = sqlite3.connect(DB)
cur = conn.cursor()

inserted = 0
skipped = 0
for c in concepts:
    try:
        cur.execute(
            """INSERT INTO concepts
               (name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition, importance_score)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                c["name_ja"],
                c["name_en"],
                c["name_original"],
                c["original_script"],
                SUBFIELD_ID,
                REGION,
                c["period_id"],
                c["definition"],
                3,
            ),
        )
        inserted += 1
    except sqlite3.IntegrityError as e:
        skipped += 1
        print(f"SKIP: {c['name_ja']} ({e})")

conn.commit()
total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)).fetchone()[0]
conn.close()
print(f"inserted={inserted} skipped={skipped} subfield17_total={total}")
