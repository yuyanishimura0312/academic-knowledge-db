#!/usr/bin/env python3
"""Wave 34: Add 30 niche concepts to lit_indigenous_oral (subfield_id=19)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 19

# 5 thematic clusters x 6 concepts. Definitions <= 100 chars.
CONCEPTS = [
    # Cluster 1: 中南米先住民
    ("ポポル・ヴフ・キチェ創世詩", "Popol Vuh K'iche", "Popol Wuj", "latin",
     "ラテンアメリカ", 13, "マヤ・キチェ族の創世神話。双子英雄譚と人類創造を含む口承神聖書。"),
    ("チラム・バラム書", "Chilam Balam", "Chilam Balam", "latin",
     "ラテンアメリカ", 13, "ユカテコ・マヤの予言・歴史・暦法を記録した口承起源の写本群。"),
    ("ナワトル・クイカトル詩学", "Nahuatl Cuicatl", "Cuicatl", "latin",
     "ラテンアメリカ", 13, "アステカの花歌・戦士歌の韻律的詩形式。並行対句と散花喩を特徴とする。"),
    ("ケチュア哀歌アプ・インカ・アタワルパマン", "Quechua Apu Inka Atawallpaman", "Apu Inka Atawallpaman", "latin",
     "ラテンアメリカ", 13, "インカ皇帝アタワルパ処刑を悼むケチュア語哀歌。征服期の口承抒情詩。"),
    ("アイマラ・ワラキ口承", "Aymara walaki", "walaki", "latin",
     "ラテンアメリカ", 13, "アイマラ族の集合歌唱・儀礼語り。アンデス互酬性とパチャを語る。"),
    ("マプチェ・マリチウェウ詠唱", "Mapuche Marichiweu", "Marichiweu", "latin",
     "ラテンアメリカ", 13, "マプチェ抵抗詠唱「十回勝つ」。先住民主権と歴史記憶の口承表現。"),
    # Cluster 2: 北米詳細
    ("チェロキー・セコイア音節文字文学", "Cherokee Sequoyah syllabary literature", "ᏣᎳᎩ", "cherokee",
     "北米", 13, "セコイアが1821年に考案したチェロキー音節文字による先住民書記文学伝統。"),
    ("ラコタ『ブラック・エルク・スピークス』", "Lakota Black Elk Speaks", "Hehaka Sapa", "latin",
     "北米", 15, "ラコタ聖人の幻視と歴史を口述した1932年の証言文学。先住民霊性の古典。"),
    ("イロコイ大平和の法", "Iroquois Great Law of Peace", "Kaianerekowa", "latin",
     "北米", 13, "ハウデノショニー連邦の口承憲法。合議制と平和原則を規定する政治叙事。"),
    ("アニシナーベ・ミデ治療歌", "Anishinaabeg Mide healing songs", "Midewiwin", "latin",
     "北米", 13, "ミデウィウィン秘儀結社の治療詠唱。樺皮巻物に象形記録された薬歌。"),
    ("イヌイト・ウニプカートゥ語り", "Inuit unipkaaq", "unipkaaq", "latin",
     "北米", 13, "イヌイトの伝統的語り物形式。シャーマン譚と動物変身譚を含む冬期口承。"),
    ("ユピック仮面詩学", "Yup'ik mask poetics", "kegginaquq", "latin",
     "北米", 13, "ユピック族の儀礼仮面と付随する歌語り。動物霊との交渉的詩学を体現する。"),
    # Cluster 3: 太平洋諸島
    ("ハワイ・クムリポ創世詠唱", "Hawaiian Kumulipo", "Kumulipo", "latin",
     "オセアニア", 13, "2102行のハワイ王統創世詠唱。宇宙発生から王族系譜までを韻律で記述する。"),
    ("トンガ・ファカハー詩学", "Tongan fakahā", "fakahā", "latin",
     "オセアニア", 13, "トンガの叙事的明示詩形式。系譜と王権の正統性を韻律で語る口承伝統。"),
    ("サモア・タラ物語", "Samoan tala", "tala", "latin",
     "オセアニア", 13, "サモアの伝説・歴史口承形式。マタイ制度と土地権原を物語化して伝える。"),
    ("マルケサス・カイオイ詠唱", "Marquesan ka'ioi", "ka'ioi", "latin",
     "オセアニア", 13, "マルケサスの若者祭典詠唱。身体装飾と詩的競演を結ぶ青年期通過儀礼。"),
    ("マオリ・ファカイロ・カラキア", "Maori whakairo karakia", "whakairo karakia", "latin",
     "オセアニア", 13, "マオリ彫刻に付随する詠唱。彫刻家の手と祖先霊を結ぶ呪詩的口承。"),
    ("ヨルング・マニカイ歌循環", "Yolŋu manikay", "manikay", "latin",
     "オセアニア", 13, "ヨルング族の氏族歌循環。土地・祖先・トーテムを結ぶ多声口承詩形式。"),
    # Cluster 4: アフリカ口承詳細
    ("マンデ・グリオ・スンジャタ叙事詩", "Mande griot Sundiata epic", "Sunjata", "latin",
     "アフリカ", 61, "マリ帝国建国王スンジャタを称えるマンデ語叙事詩。グリオ世襲が伝承する。"),
    ("ヨルバ・イファ・オドゥ詩", "Yoruba Ifa odu", "Odù Ifá", "latin",
     "アフリカ", 61, "イファ占いの256章詩集。神話・倫理・処方を韻律で結ぶ口承哲学体系。"),
    ("アカン・アナンセセム蜘蛛譚", "Akan Anansesem", "Anansesem", "latin",
     "アフリカ", 61, "アカン族の蜘蛛アナンシ譚。トリックスター譚で社会知を伝える口承形式。"),
    ("マサイ・エンキテング牛歌", "Maasai enkiteng songs", "enkiteng", "latin",
     "アフリカ", 61, "マサイの牛をめぐる歌唱群。牧畜倫理と男性年齢階梯を結ぶ口承詩。"),
    ("コイサン・|Xam詠唱", "Khoisan |Xam chants", "|Xam", "khoisan",
     "アフリカ", 61, "南部アフリカ|Xam族のクリック音詠唱。月・雨・狩猟霊を呼ぶ最古層口承。"),
    ("ハッザ・ンオ歌", "Hadza n!ow songs", "n!ow", "khoisan",
     "アフリカ", 61, "ハッザ族の狩猟成功歌。動物霊との交渉と男女別歌唱規範を含む口承。"),
    # Cluster 5: アイヌ詳細補完
    ("ユーカラ・ポン・オタサムンクル", "Yukar Pon Otasamunkur", "Pon Otasamunkur", "latin",
     "東アジア", 13, "若き勇者オタサムンクルを主人公とするアイヌ英雄ユーカラの代表曲。"),
    ("トゥイタク継承歌", "Tuytak inheritance song", "tuytak", "latin",
     "東アジア", 13, "アイヌの世代継承儀礼歌。父祖の徳と家系の物語を継ぐ口承形式。"),
    ("サコルペ・カヤック歌", "Sakorpe kayak song", "sakorpe", "latin",
     "東アジア", 13, "アイヌ海猟用カヤックに伴う詠唱。海神への祈りと航海技術を結ぶ。"),
    ("オトンペ・トリックスター譚", "Otonpe trickster tale", "otonpe", "latin",
     "東アジア", 13, "アイヌ口承の道化譚群。社会規範違反を笑話化する教訓的トリックスター。"),
    ("イウォルペ・シャーマン儀礼歌", "Iworpe shamanic chant", "iworpe", "latin",
     "東アジア", 13, "アイヌ・トゥスクル（シャーマン）が病霊と交渉する憑依詠唱。"),
    ("ウェニプル児戯歌", "Wenipuru child play song", "wenipuru", "latin",
     "東アジア", 13, "アイヌ子ども遊戯歌。自然観察と倫理を遊びで伝える幼児期口承教育。"),
]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, region, period_id, definition in CONCEPTS:
        try:
            cur.execute("""
                INSERT INTO concepts (name_ja, name_en, name_original, original_script,
                    subfield_id, region, period_id, definition, importance_score,
                    fourth_transform_status, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 3, 'partial', 'tier2', 'yes')
            """, (name_ja, name_en, name_orig, script, SUBFIELD_ID, region, period_id, definition))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP: {name_ja} - {e}")
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
