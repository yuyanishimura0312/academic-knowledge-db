#!/usr/bin/env python3
"""Wave26 C16: 30 concepts for lit_jp_classical (subfield_id=10)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"

# period_ids: 上代=59, 中古=60, 中世=97
CONCEPTS = [
    # Cluster 1: 万葉集深掘り (上代=59)
    ("大伴旅人讃酒歌", "Otomo no Tabito's Sake Praising Poems", "讃酒歌十三首", 59,
     "万葉集巻三338-350、老荘・仏典を引きつつ酒讃の漢学的アイロニーを展開する家持父の連作。"),
    ("大伴坂上郎女歌群論", "Otomo no Sakanoue no Iratsume Poetic Corpus Studies", "大伴坂上郎女歌群論", 59,
     "万葉集女性歌人最多の84首。氏族祭祀・恋情・贈答を統べる女性家長歌の規範を確立。"),
    ("高橋虫麻呂伝説歌", "Takahashi no Mushimaro Legend Poems", "高橋虫麻呂歌集", 59,
     "浦島・真間手児奈・水江浦島など伝承を物語的長歌に再構築した民俗説話の歌化。"),
    ("笠女郎相聞歌", "Kasa no Iratsume Love Poems", "笠女郎相聞", 59,
     "万葉集巻四・巻八の大伴家持宛29首、片恋の心象を凝縮した女流相聞歌の頂点。"),
    ("中臣宅守贈答歌", "Nakatomi no Yakamori Exchange Poems", "中臣宅守狭野茅上娘子贈答", 59,
     "流罪となった宅守と狭野茅上娘子の63首贈答、別離の極限情況を歌で記した稀少例。"),
    ("防人歌集成", "Sakimori Poems Compilation", "防人歌", 59,
     "万葉集巻十四・二十、東国徴兵兵士と妻子の別離を口承伝来した辺境の声の集成。"),
    # Cluster 2: 古今集系譜 (中古=60, 中世=97)
    ("古今集仮名序紀貫之論", "Kokinshu Kana Preface by Ki no Tsurayuki Studies", "古今和歌集仮名序紀貫之", 60,
     "紀貫之による初の本格和歌論、「やまとうたは人の心を種として」の和歌本質定義書。"),
    ("古今集真名序紀淑望", "Kokinshu Mana Preface by Ki no Yoshimochi", "古今和歌集真名序", 60,
     "紀淑望による漢文序、六義論を漢詩学から借用し和歌の正典性を体系化した理論書。"),
    ("後撰集源順", "Gosenshu and Minamoto no Shitago", "後撰和歌集梨壺五人", 60,
     "梨壺の五人の中心源順による第二勅撰集、贈答歌主体で物語的読みを開拓。"),
    ("拾遺集藤原公任", "Shuishu and Fujiwara no Kinto", "拾遺和歌集藤原公任", 60,
     "三十六歌仙撰者公任の選歌眼、和漢朗詠集と並ぶ平安中期歌学の規範形成。"),
    ("新古今集藤原定家", "Shinkokinshu and Fujiwara no Teika", "新古今和歌集藤原定家", 97,
     "定家撰、有心・余情・本歌取を統合し中世幽玄美学の到達点を示す第八代勅撰集。"),
    ("玉葉集京極為兼", "Gyokuyoshu and Kyogoku Tamekane", "玉葉和歌集京極為兼", 97,
     "為兼撰の十四代集、二条派旧套を破り感覚的写生・主観性を打ち出した革新派歌集。"),
    # Cluster 3: 私家集
    ("柿本人麻呂集私家集", "Kakinomoto no Hitomaro Personal Collection", "柿本人麻呂集私家集", 59,
     "万葉時代から平安に伝来した柿本人麻呂仮託の私家集、後世の歌聖像形成基盤。"),
    ("在原業平集私家集", "Ariwara no Narihira Personal Collection", "在原業平集私家集", 60,
     "在原業平の私家集、伊勢物語の素材歌群を含み歌物語形成の母胎となった歌集。"),
    ("紀貫之集", "Ki no Tsurayuki Collection", "貫之集", 60,
     "紀貫之自撰の屏風歌・贈答歌を編む私家集、宮廷儀礼歌の典型と古今集理念の実践。"),
    ("西行山家集", "Saigyo's Sankashu", "山家集", 97,
     "西行の私家集、出家遁世の旅と自然観照を詠み中世隠遁文学・本歌取の源泉となる。"),
    ("藤原定家拾遺愚草", "Fujiwara no Teika's Shui Guso", "拾遺愚草", 97,
     "定家自撰私家集、青年期から晩年までの3,500首余、有心体・余情体の試行軌跡。"),
    ("実朝金槐和歌集", "Sanetomo's Kinkai Wakashu", "金槐和歌集", 97,
     "源実朝の私家集、万葉調の力強さと定家門風を融合した武家歌人の独自境地。"),
    # Cluster 4: 中古日記文学 (中古=60, 中世=97)
    ("土佐日記紀貫之", "Tosa Nikki by Ki no Tsurayuki", "土佐日記", 60,
     "紀貫之が女性に仮託し仮名で記した土佐帰京日記、仮名日記文学の創始。"),
    ("蜻蛉日記藤原道綱母", "Kagero Nikki by Mother of Michitsuna", "蜻蛉日記", 60,
     "藤原道綱母による21年自伝的回想、結婚生活の苦悩を内省的散文で描く。"),
    ("紫式部日記", "Murasaki Shikibu Nikki", "紫式部日記", 60,
     "紫式部が中宮彰子出産記録と女房評を記した宮廷観察記、源氏物語成立期の証言。"),
    ("和泉式部日記", "Izumi Shikibu Nikki", "和泉式部日記", 60,
     "敦道親王との恋愛を歌物語的構成で記した三人称的恋愛日記、贈答歌140余首収録。"),
    ("更級日記菅原孝標女", "Sarashina Nikki by Sugawara no Takasue's Daughter", "更級日記", 60,
     "菅原孝標女の40年回想、源氏物語憧憬から夢・信仰・後悔へ至る精神遍歴記。"),
    ("讃岐典侍日記藤原長子", "Sanuki no Suke Nikki by Fujiwara no Nagako", "讃岐典侍日記藤原長子", 60,
     "藤原長子による堀河天皇崩御と鳥羽朝出仕の記、女房日記末期の追悼的回想。"),
    # Cluster 5: 中世和歌・連歌 (中世=97)
    ("心敬ささめごと十題論", "Shinkei's Sasamegoto Ten Topics Studies", "ささめごと十題論", 97,
     "心敬の連歌論書、冷え寂びの美学と禅的観想を融合した中世詩論の到達点。"),
    ("宗祇水無瀬三吟", "Sogi's Minase Sangin", "水無瀬三吟百韻", 97,
     "宗祇・肖柏・宗長による1488年百韻、後鳥羽院追善の正風連歌典型作。"),
    ("二条良基筑波集", "Nijo Yoshimoto's Tsukubashu", "菟玖波集", 97,
     "二条良基撰、勅撰に准じた最初の連歌集、連歌を和歌と並ぶ正典に押し上げた。"),
    ("飛鳥井雅経", "Asukai Masatsune", "飛鳥井雅経", 97,
     "新古今集撰者の一人、蹴鞠と和歌の家元飛鳥井家の祖、明月記等にも頻出。"),
    ("京極派和歌", "Kyogoku School Waka", "京極派", 97,
     "京極為兼を中心とする革新派、感覚的描写・写生・主観表現で二条派旧套に対抗。"),
    ("二条派和歌", "Nijo School Waka", "二条派", 97,
     "二条為氏以降の保守正統派、定家風を厳守し中世和歌の主流として室町期まで継承。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted, skipped = 0, []
    for name_ja, name_en, name_orig, period_id, definition in CONCEPTS:
        if len(definition) > 100:
            skipped.append((name_ja, "def>100"))
            continue
        try:
            cur.execute(
                """INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id,
                 region, period_id, definition, importance_score, source_tier,
                 canonical_in_region)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                (name_ja, name_en, name_orig, "kanji", 10, "東アジア",
                 period_id, definition, 4, "tier1", "yes"),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped.append((name_ja, str(e)))
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}/30")
    if skipped:
        print("Skipped:")
        for n, r in skipped:
            print(f"  {n}: {r}")

if __name__ == "__main__":
    main()
