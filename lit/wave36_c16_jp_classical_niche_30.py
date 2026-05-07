#!/usr/bin/env python3
"""Wave 36 cluster 16: lit_jp_classical NICHE +30 concepts (5 thematic clusters)."""
import sqlite3, sys
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"

# period_id reference (East Asia): 上代=59, 中古=60, 中世=97, 近世=98
P_KODAI = 59
P_CHUKO = 60
P_CHUSEI = 97
P_KINSEI = 98

CONCEPTS = [
    # === Cluster 1: 漢詩詳細 (kanshi anthologies) ===
    ("懐風藻序","Kaifuso Jo","懐風藻序","kanji",P_KODAI,
     "751年懐風藻の序文。日本最古の漢詩文論として中国詩学受容の出発点を示す。",4),
    ("凌雲集","Ryounshu","凌雲集","kanji",P_CHUKO,
     "814年小野岑守ら撰の最初の勅撰漢詩集。嵯峨朝の漢風謳歌を象徴する24人90余首。",4),
    ("文華秀麗集","Bunka Shureishu","文華秀麗集","kanji",P_CHUKO,
     "818年藤原冬嗣ら撰の第二勅撰漢詩集。賦・雑詠・贈答など七部構成、約140首。",4),
    ("経国集","Keikokushu","經國集","kanji",P_CHUKO,
     "827年良岑安世ら撰の第三勅撰漢詩集。本来20巻、賦・詩・序・対策収録。",4),
    ("菅家文草","Kanke Bunso","菅家文草","kanji",P_CHUKO,
     "900年菅原道真自撰の漢詩文集12巻。漢詩468首と散文を収め個人別集の白眉。",5),
    ("都氏文集","Toshi Bunshu","都氏文集","kanji",P_CHUKO,
     "都良香の漢詩文集6巻。9世紀後半の文章博士による賦・詩・序・銘を集成。",3),

    # === Cluster 2: 中世紀行 (medieval travel diaries) ===
    ("海道記注釈","Kaidoki Chushaku","海道記注釋","kanji",P_CHUSEI,
     "中世紀行海道記の本文諸本と注釈伝統。歌枕と漢文典拠を解読する研究系譜。",3),
    ("東関紀行注釈","Tokan Kiko Chushaku","東關紀行注釋","kanji",P_CHUSEI,
     "中世紀行東関紀行の諸本と注釈系譜。和漢混淆体の典拠探索を行う注釈研究。",3),
    ("阿仏尼東下り","Abutsuni Azuma Kudari","阿佛尼東下り","kanji",P_CHUSEI,
     "1279年阿仏尼鎌倉下向の和歌記録。十六夜日記とは別の紀行的歌群を含む補完資料。",3),
    ("宗久都の苞","Sokyu Miyako no Tsuto","宗久都の苞","kanji",P_CHUSEI,
     "宗久作中世紀行都の苞の作者考証。隠遁僧の歌枕巡礼観を読む方法論。",3),
    ("増基庵日記","Zoki An Nikki","增基庵日記","kanji",P_CHUSEI,
     "増基法師の中世庵居日記。隠遁生活と和歌詠草を結合した中世隠者文学の一形態。",3),
    ("飛鳥井雅有歌集","Asukai Masaari Kashu","飛鳥井雅有歌集","kanji",P_CHUSEI,
     "鎌倉中期飛鳥井雅有の私家集。京鎌倉往還を含む紀行的歌群を含み中世紀行と接続。",3),

    # === Cluster 3: 軍記三系統 (military tale variants) ===
    ("覚一本平家物語","Kakuichi-bon Heike Monogatari","覺一本平家物語","kanji",P_CHUSEI,
     "1371年明石覚一による語り本系平家物語12巻。琵琶法師の語り台本として正典化。",5),
    ("延慶本平家物語","Engyo-bon Heike Monogatari","延慶本平家物語","kanji",P_CHUSEI,
     "1309-10年書写の読み本系平家物語。語り本に比べ史伝的記述と漢文体が濃厚。",4),
    ("源平闘諍録","Genpei Tojoroku","源平鬪諍錄","kanji",P_CHUSEI,
     "鎌倉中期成立の平家物語異本系。千葉氏関連記事を増補した東国読み本系統。",3),
    ("太平記古態本","Taiheiki Kotai-bon","太平記古態本","kanji",P_CHUSEI,
     "現行40巻太平記の最古態を残す諸本。神田本・西源院本など本文研究の基礎。",4),
    ("義経記諸本系統","Gikeiki Shohon Keito","義經記諸本系統","kanji",P_CHUSEI,
     "義経記の流布本・古活字本・絵入本諸系統。判官物語形成過程を本文系統で追跡。",3),
    ("曾我物語真名本","Soga Monogatari Manabon","曾我物語眞名本","kanji",P_CHUSEI,
     "1300年前後成立の漢字専用表記曾我物語。仮名本に先行する古態を残す諸本。",4),

    # === Cluster 4: 説話文学 (setsuwa anthologies) ===
    ("今昔物語集本朝部","Konjaku Monogatarishu Honchobu","今昔物語集本朝部","kanji",P_CHUKO,
     "1120年頃成立の今昔物語集巻21-31の日本説話部分。仏法部と世俗部に二分される。",5),
    ("今昔物語集天竺震旦部","Konjaku Monogatarishu Tenjiku Shintan-bu","今昔物語集天竺震旦部","kanji",P_CHUKO,
     "今昔物語集巻1-10。インド・中国の仏教説話を時系列で配し三国伝来史観を構築。",4),
    ("宇治拾遺物語序","Uji Shui Monogatari Jo","宇治拾遺物語序","kanji",P_CHUSEI,
     "宇治拾遺物語冒頭の序文。古本説話集系統との関係を示す中世説話書誌の鍵資料。",3),
    ("古今著聞集分類論","Kokon Chomonju Bunrui Ron","古今著聞集分類論","kanji",P_CHUSEI,
     "1254年古今著聞集の30篇分類体系。中世類書化の方法論として説話分類学を提示。",3),
    ("沙石集","Shasekishu","沙石集","kanji",P_CHUSEI,
     "1283年無住道暁編の仏教説話集10巻。和漢混淆体で禅宗的世俗化を進めた説話論。",5),
    ("玄棟三国伝記論","Genbo Sangoku Denki Ron","玄棟三國傳記論","kanji",P_CHUSEI,
     "玄棟編三国伝記の編纂方法論。天竺・震旦・本朝三国順循環という構造論研究。",3),

    # === Cluster 5: 近世国学 (Edo nativist learning) ===
    ("賀茂真淵歌意考","Kamo no Mabuchi Kaiko","歌意考","kanji",P_KINSEI,
     "1764年賀茂真淵の歌論書。万葉の高く直き調を理想とし古今以後の優美風を批判。",5),
    ("本居宣長石上私淑言","Motoori Norinaga Isonokami Sasamegoto","石上私淑言","kanji",P_KINSEI,
     "1763年本居宣長の歌論書。和歌の本質を「もののあはれ」とする本居美学の原型。",5),
    ("本居宣長玉勝間","Motoori Norinaga Tamakatsuma","玉勝間","kanji",P_KINSEI,
     "1795-1812年本居宣長の随筆14巻1003条。古学・文献考証・国語論を集成した晩年学術ノート。",5),
    ("平田篤胤霊能真柱","Hirata Atsutane Tama no Mihashira","靈能眞柱","kanji",P_KINSEI,
     "1813年平田篤胤の宇宙論的国学書。古事記神話を体系化し復古神道の教義を確立。",4),
    ("香川景樹桂園一枝","Kagawa Kageki Keien Isshi","桂園一枝","kanji",P_KINSEI,
     "1828年香川景樹自選の家集。古今集を理想とする桂園派歌風を集成、調べの説を展開。",4),
    ("大田南畝狂歌集","Ota Nanpo Kyokashu","大田南畝狂歌集","kanji",P_KINSEI,
     "天明狂歌の中心大田南畝(蜀山人)の狂歌集成。江戸後期町人文芸の知的諧謔を代表。",4),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = skipped = 0
    for name_ja, name_en, name_orig, script, period_id, definition, importance in CONCEPTS:
        if len(definition) > 100:
            print(f"SKIP (def>100): {name_ja} ({len(definition)})", file=sys.stderr)
            skipped += 1
            continue
        try:
            cur.execute("""
                INSERT INTO concepts (name_ja, name_en, name_original, original_script,
                    subfield_id, region, period_id, definition, importance_score,
                    source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, 10, '東アジア', ?, ?, ?, 'A', 'Y')
            """, (name_ja, name_en, name_orig, script, period_id, definition, importance))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP (dup): {name_ja} - {e}", file=sys.stderr)
            skipped += 1
    conn.commit()
    print(f"Inserted: {inserted}, Skipped: {skipped}")
    conn.close()

if __name__ == "__main__":
    main()
