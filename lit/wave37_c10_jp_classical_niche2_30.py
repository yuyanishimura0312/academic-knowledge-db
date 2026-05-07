#!/usr/bin/env python3
"""Wave 37: subfield 10 (lit_jp_classical) deep-niche 30 concepts."""
import sqlite3, os
DB = os.path.join(os.path.dirname(__file__), "lit.sqlite")

# (name_ja, name_en, name_original, original_script, region, period_id, definition, importance)
ROWS = [
    # Cluster 1: 平安和歌私家集 (period_id=60 中古)
    ("中務集", "Nakatsukasa-shu", "中務集", "kanji", "東アジア", 60, "平安中期女流歌人中務の私家集。屏風歌・贈答歌を多く収め優艶な歌風。", 3),
    ("元輔集", "Motosuke-shu", "元輔集", "kanji", "東アジア", 60, "清原元輔の私家集。梨壺の五人として後撰集編纂に携わった歌人の歌業。", 3),
    ("道綱母集", "Michitsuna-no-Haha-shu", "道綱母集", "kanji", "東アジア", 60, "藤原道綱母の私家集。蜻蛉日記とは別に編まれた贈答・嘆きの歌群。", 3),
    ("西行山家集雑歌", "Sankashu Zoka", "山家集 雑歌", "kanji", "東アジア", 60, "西行私家集『山家集』の雑歌部。漂泊・自然・仏教観念を融合した抒情歌群。", 4),
    ("寂蓮法師集", "Jakuren-Hoshi-shu", "寂蓮法師集", "kanji", "東アジア", 60, "新古今歌人寂蓮の私家集。幽玄・余情を体現する自然詠と仏教詠を収める。", 3),
    ("慈円拾玉集", "Jien Shugyokushu", "拾玉集", "kanji", "東アジア", 60, "天台座主慈円の私家集。約六千首を擁する大部の自撰集で愚管抄思想と通底。", 4),

    # Cluster 2: 漢文学・国史 (period_id=60 中古)
    ("本朝文粋", "Honcho Monzui", "本朝文粋", "kanji", "東アジア", 60, "藤原明衡編の平安漢詩文選集。十四巻・四百余編で和臭漢文の精華を集成。", 4),
    ("江談抄", "Godansho", "江談抄", "kanji", "東アジア", 60, "大江匡房の談話を藤原実兼が筆録した説話集。詩文・有職故実逸話を収める。", 4),
    ("朝野群載", "Choya Gunsai", "朝野群載", "kanji", "東アジア", 60, "三善為康編の平安公私文書類聚。詩賦・官符・書状など二十巻の文書集成。", 3),
    ("続日本後紀", "Shoku Nihon Koki", "続日本後紀", "kanji", "東アジア", 60, "六国史第四。仁明天皇朝十七年を編年体で記す勅撰漢文国史。", 3),
    ("類聚国史", "Ruiju Kokushi", "類聚国史", "kanji", "東アジア", 60, "菅原道真編の分類国史。六国史記事を神祇・帝王等項目別に再編した史料集。", 4),
    ("古事談", "Kojidan", "古事談", "kanji", "東アジア", 60, "源顕兼編の鎌倉初期説話集。王道・臣節・僧行ほか六部門の宮廷古事を録す。", 3),

    # Cluster 3: 中世物語・連歌 (period_id=97 中世)
    ("海人の刈藻", "Ama no Karumo", "海人の刈藻", "kanji", "東アジア", 97, "鎌倉期の擬古物語。源氏物語の影響下で恋愛と出家を描く佚名作。", 3),
    ("苔の衣", "Koke no Koromo", "苔の衣", "kanji", "東アジア", 97, "中世擬古物語。仏道求道と恋愛葛藤を絡める四巻構成の女流系物語。", 3),
    ("風につれなき物語", "Kaze ni Tsurenaki Monogatari", "風につれなき物語", "kanji", "東アジア", 97, "中世擬古物語の佚名作。源氏摂取の恋愛遍歴譚で零本のみ伝存。", 3),
    ("心敬ささめごと", "Shinkei Sasamegoto", "ささめごと", "kanji", "東アジア", 97, "心敬の連歌論書。冷え寂び・心の艶を理論化し連歌美学の頂点を示す。", 4),
    ("宗祇老葉", "Sogi Wakuraba", "老葉", "kanji", "東アジア", 97, "連歌師宗祇晩年の自撰句集。三巻構成で枯淡幽玄の連歌句を集成。", 3),
    ("宗長日記", "Socho Nikki", "宗長日記", "kanji", "東アジア", 97, "連歌師宗長の旅日記。今川氏ら諸国大名歴訪と連歌興行を記録。", 3),

    # Cluster 4: 近世和文・俳論 (period_id=98 近世)
    ("本居宣長玉勝間", "Motoori Norinaga Tamakatsuma", "玉勝間", "kanji", "東アジア", 98, "宣長随筆。十五巻千余条の学問雑録で古道論・もののあはれ補論を含む。", 4),
    ("上田秋成浅茅が宿", "Asaji ga Yado", "浅茅が宿", "kanji", "東アジア", 98, "雨月物語第三話。戦乱で離別した夫婦の再会を幽霊譚として描く名編。", 4),
    ("賀茂真淵万葉考", "Kamo no Mabuchi Manyoko", "万葉考", "kanji", "東アジア", 98, "真淵の万葉集注釈書。ますらをぶり論を打ち立てた国学的注釈の金字塔。", 4),
    ("与謝蕪村春風馬堤曲", "Shunpu Batei Kyoku", "春風馬堤曲", "kanji", "東アジア", 98, "蕪村の俳詩。漢詩・俳句・和文を融合した実験的離郷叙情詩十八首。", 4),
    ("横井也有鶉衣", "Yokoi Yayu Uzuragoromo", "鶉衣", "kanji", "東アジア", 98, "尾張俳人也有の俳文集。軽妙洒脱な漢和混淆文体で日常を諷詠する。", 3),
    ("大田南畝半日閑話", "Ota Nanpo Hannichi Kanwa", "半日閑話", "kanji", "東アジア", 98, "蜀山人の随筆。江戸の世相・狂歌・風俗を軽妙に記録した随想集。", 3),

    # Cluster 5: 江戸戯作・遊里文学 (period_id=98 近世)
    ("山東京伝通言総籬", "Tsugen Somagaki", "通言総籬", "kanji", "東アジア", 98, "山東京伝の洒落本。吉原大籬の通言を写実的会話で活写した代表作。", 4),
    ("唐来三和莫切自根金生木", "Kirakire Kanenaruki", "莫切自根金生木", "kanji", "東アジア", 98, "唐来三和の黄表紙。富裕譚を逆転発想で諷した黄表紙黄金期の代表作。", 3),
    ("為永春水春色梅児誉美", "Shunshoku Umegoyomi", "春色梅児誉美", "kanji", "東アジア", 98, "為永春水の人情本。深川芸者世界の三角関係を情緒的に描いた天保期名作。", 4),
    ("柳亭種彦偐紫田舎源氏", "Nise Murasaki Inaka Genji", "偐紫田舎源氏", "kanji", "東アジア", 98, "柳亭種彦の合巻。源氏物語を室町世界に翻案した三十八編の長編絵入り小説。", 4),
    ("十返舎一九東海道中膝栗毛", "Tokaidochu Hizakurige", "東海道中膝栗毛", "kanji", "東アジア", 98, "弥次郎兵衛・喜多八の道中滑稽本。化政期庶民文学を代表する旅譚。", 5),
    ("滝沢馬琴椿説弓張月", "Chinsetsu Yumiharizuki", "椿説弓張月", "kanji", "東アジア", 98, "馬琴の読本。源為朝の琉球渡海伝奇を北斎挿絵と共に展開した壮大伝奇譚。", 4),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = skipped = 0
    for r in ROWS:
        name_ja, name_en, name_original, script, region, pid, definition, importance = r
        try:
            cur.execute("""INSERT INTO concepts
                (name_ja, name_en, name_original, original_script,
                 subfield_id, region, period_id, definition, importance_score,
                 source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, 10, ?, ?, ?, ?, 'tier1', 'canonical')""",
                (name_ja, name_en, name_original, script, region, pid, definition, importance))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    conn.close()
    print(f"Wave 37 c10 niche2: inserted={inserted} skipped={skipped} target=30")

if __name__ == "__main__":
    main()
