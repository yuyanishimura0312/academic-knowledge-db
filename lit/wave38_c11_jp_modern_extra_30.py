#!/usr/bin/env python3
"""Wave 38: lit_jp_modern (id=11) +30 deep niche concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD = "lit_jp_modern"
REGION = "東アジア"

# period IDs: 8 明治期, 9 大正期, 10 昭和戦前期, 11 戦後期, 12 現代
CONCEPTS = [
    # 明治周縁作家・小説
    ("饗庭篁村『むら竹』", "Muratake (Aeba Koson)", "むら竹", 8, "根岸派の洒脱な写実を示す明治初期小説。"),
    ("川上眉山『大盃』", "Great Cup (Kawakami Bizan)", "大盃", 8, "硯友社周辺の情緒過多な美文小説。"),
    ("巌谷小波『こがね丸』", "Koganemaru (Iwaya Sazanami)", "こがね丸", 8, "近代児童文学成立期の冒険的動物譚。"),
    ("宮崎湖処子『帰省』", "Homecoming (Miyazaki Koshoshi)", "帰省", 8, "民友社系青年の倫理的煩悶を描く明治小説。"),
    ("木下尚江『火の柱』", "Pillar of Fire (Kinoshita Naoe)", "火の柱", 8, "社会主義思想を小説化した明治政治文学。"),
    ("小栗風葉『青春』", "Youth (Oguri Fuyo)", "青春", 8, "硯友社末期の学生風俗と恋愛を描く長編。"),
    # 大正・私小説周辺
    ("島村抱月『囚はれたる文芸』", "Captive Literature", "囚はれたる文芸", 9, "自然主義受容を理論化した大正批評文脈。"),
    ("長谷川時雨『旧聞日本橋』", "Old Tales of Nihonbashi", "旧聞日本橋", 9, "女性の都市記憶で江戸東京移行を語る随筆。"),
    ("近松秋江『疑惑』", "Suspicion (Chikamatsu Shuko)", "疑惑", 9, "破滅型私小説の嫉妬と執着を示す短編。"),
    ("葛西善蔵『子をつれて』", "With a Child", "子をつれて", 9, "貧困と父子関係を露呈する破滅型私小説。"),
    ("嘉村礒多『業苦』", "Karmic Suffering", "業苦", 9, "罪責感と信仰葛藤を凝縮した私小説短編。"),
    ("久米正雄『破船』", "Shipwreck (Kume Masao)", "破船", 9, "新思潮派周辺の恋愛心理と挫折を描く小説。"),
    # 植民地・外地・地方変奏
    ("佐藤春夫『霧社』", "Musha (Sato Haruo)", "霧社", 10, "台湾霧社事件を素材化した植民地幻想譚。"),
    ("佐藤春夫『女誡扇綺譚』", "The Strange Tale of Fan", "女誡扇綺譚", 10, "台南廃屋を舞台にした植民地ゴシック小説。"),
    ("龍瑛宗『パパイヤのある街』", "Town with Papayas", "パパイヤのある街", 10, "日本語台湾文学の都市下層を描く短編。"),
    ("呂赫若『清秋』", "Clear Autumn (Lu Heruo)", "清秋", 10, "台湾知識人の閉塞感を日本語で描く短編。"),
    ("西川満『赤嵌記』", "Record of Chikan", "赤嵌記", 10, "台湾郷土を耽美的に再構成した外地文学。"),
    ("火野葦平『糞尿譚』", "Dung Tale (Hino Ashihei)", "糞尿譚", 10, "北九州の労働と滑稽を描く芥川賞作。"),
    # 戦後小雑誌・前衛・占領期
    ("花田清輝『復興期の精神』", "Spirit of Reconstruction", "復興期の精神", 11, "戦後前衛批評の方法意識を示す評論集。"),
    ("埴谷雄高『死霊』", "Dead Souls (Haniya Yutaka)", "死霊", 11, "形而上学的対話で構成された未完の長編。"),
    ("島尾敏雄『出孤島記』", "Leaving the Solitary Island", "出孤島記", 11, "特攻待機体験を内面化した戦後短編。"),
    ("原民喜『夏の花』", "Summer Flowers (Hara Tamiki)", "夏の花", 11, "被爆直後の広島を静謐に記録した短編。"),
    ("金達寿『玄海灘』", "Genkai Sea (Kim Tal-su)", "玄海灘", 11, "在日朝鮮人文学初期の民族移動小説。"),
    ("富士正晴『贋・久坂葉子伝』", "Fake Biography of Kusaka Yoko", "贋・久坂葉子伝", 11, "夭折作家像を虚実混淆で描く伝記小説。"),
    # 現代辺境・実験小説
    ("目取真俊『水滴』", "Droplets (Medoruma Shun)", "水滴", 12, "沖縄戦の記憶を身体寓話化した芥川賞作。"),
    ("崎山多美『くりかえしがえし』", "Repeating Back", "くりかえしがえし", 12, "沖縄語の反復で標準語小説を揺さぶる実験作。"),
    ("李良枝『由熙』", "Yuhi (Yi Yang-ji)", "由熙", 12, "在日女性の言語喪失と韓国体験を描く小説。"),
    ("リービ英雄『星条旗の聞こえない部屋』", "Room Where the Star-Spangled Banner Cannot Be Heard", "星条旗の聞こえない部屋", 12, "非母語日本語で書く越境作家の初期長編。"),
    ("笙野頼子『タイムスリップ・コンビナート』", "Time Slip Kombinat", "タイムスリップ・コンビナート", 12, "湾岸地帯を幻視化する反リアリズム小説。"),
    ("松浦理英子『親指Pの修業時代』", "Apprenticeship of Big Toe P", "親指Pの修業時代", 12, "身体変容と性愛を寓話化した実験長編。"),
]


def main() -> None:
    if len(CONCEPTS) != 30:
        raise SystemExit(f"expected 30 concepts, got {len(CONCEPTS)}")
    if any(len(c[4]) > 100 for c in CONCEPTS):
        raise SystemExit("definition over 100 chars")

    with LitDB() as db:
        existing = {
            r["name_ja"]
            for r in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 11"
            )
        }
        dupes = [c[0] for c in CONCEPTS if c[0] in existing]
        if dupes:
            raise SystemExit(f"duplicates in subfield 11: {dupes}")

        inserted = 0
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script="kanji",
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            inserted += 1

        total = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 11"
        ).fetchone()["c"]
        print(f"Inserted {inserted}; total subfield 11: {total}")


if __name__ == "__main__":
    main()
