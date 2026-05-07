#!/usr/bin/env python3
"""Wave 37 C02: lit_eu_medieval niche concepts (30) - 5 clusters x 6."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 2
REGION = "西欧"

# period mapping by cluster
PERIODS = {
    "AS": 110,    # 中世初期（カロリング期）-> Anglo-Saxon early
    "FR": 213,    # 中世フランス古典期
    "DE": 111,    # 中世盛期（ロマネスク・初期ゴシック） -> 独・蘭 high
    "DE2": 119,   # 中世末期ゲルマン圏
    "SCAN": 218,  # 北方中世
    "IT": 212,    # 中世盛期イタリア
    "ES": 215,    # イベリア中世
}

CONCEPTS = [
    # Cluster 1: アングロサクソン (period 110)
    ("ベオウルフ・グレンデル戦闘場面", "Beowulf Grendel Episode", "Bēowulf, ll.710-836", "latin", 110,
     "古英語叙事詩『ベオウルフ』第711-836行、英雄とグレンデルの夜戦を描く中核場面。"),
    ("古英語悲歌『さすらい人』詳論", "The Wanderer (detailed)", "Eardstapa", "latin", 110,
     "エクセター写本所収の古英語悲歌、流謫者の独白と運命観・ウビ・スント主題を表現。"),
    ("古英語悲歌『海の旅人』詳論", "The Seafarer (detailed)", "Sēofarend", "latin", 110,
     "エクセター写本の古英語悲歌、海上の苦難と来世志向を結ぶ瞑想的構造を持つ。"),
    ("十字架の夢", "The Dream of the Rood", "Dryht-cyninges rōd", "latin", 110,
     "古英語キリスト教詩、磔刑の十字架自身が語る夢幻的視覚詩、ヴェルチェッリ写本所収。"),
    ("マルドンの戦い", "The Battle of Maldon", "Beadu Maldūne", "latin", 110,
     "991年マルドン会戦を描く古英語戦闘詩、英雄エセルレッドの忠誠心と敗北の倫理。"),
    ("キャドモンの賛歌詳論", "Caedmon's Hymn (detailed)", "Cædmones Hymn", "latin", 110,
     "ベーダ伝に伝わる最古の古英語キリスト教詩、9行の創造主賛歌、口頭詩から記録への移行。"),

    # Cluster 2: 中世仏ロマンス (period 213)
    ("クレチアン・ド・トロワ『エレックとエニード』", "Chrétien Erec et Enide", "Erec et Enide", "latin", 213,
     "クレチアン最初期のアーサー王ロマン、騎士道と結婚愛の調和を主題化。"),
    ("クレチアン『クリジェス』詳論", "Chrétien Cligès (detailed)", "Cligès", "latin", 213,
     "ビザンツ・アーサー王世界を結ぶロマン、トリスタン主題への対抗的応答を含む。"),
    ("クレチアン『イヴァン（獅子の騎士）』詳論", "Chrétien Yvain (detailed)", "Yvain ou le Chevalier au Lion", "latin", 213,
     "クレチアン円熟期の作、騎士の名誉と妻への義務の葛藤と獅子の助力者主題。"),
    ("マリー・ド・フランス『レー集』", "Marie de France Lais", "Lais de Marie de France", "latin", 213,
     "アングロ・ノルマン詩人マリーの十二編のブルトン・レー、超自然と恋愛の短篇集。"),
    ("ベルール『トリスタン』詳論", "Béroul Tristan", "Tristan de Béroul", "latin", 213,
     "12世紀ノルマン詩人ベルールの『トリスタン』、共通版（version commune）系の代表。"),
    ("ロベール・ド・ボロン『聖杯物語』", "Robert de Boron Estoire du Graal", "Estoire dou Graal", "latin", 213,
     "聖杯起源をキリスト教神学化した散文ロマンの基礎、聖杯=最後の晩餐の聖杯。"),

    # Cluster 3: 中世独・蘭 (period 111 / 119)
    ("ヴォルフラム『パルチヴァール』詳論", "Wolfram Parzival (detailed)", "Parzival", "latin", 111,
     "ヴォルフラム・フォン・エッシェンバッハの中高ドイツ語騎士叙事詩、聖杯探求の心理ロマン。"),
    ("ハルトマン・フォン・アウエ『エレック』", "Hartmann Erec", "Erec", "latin", 111,
     "クレチアン『エレックとエニード』のドイツ語翻案、宮廷叙事詩のドイツ的展開の起点。"),
    ("ゴットフリート『トリスタンとイゾルデ』詳論", "Gottfried Tristan und Isolde", "Tristan und Isolde", "latin", 111,
     "ゴットフリート・フォン・シュトラスブルクの中高ドイツ語『トリスタン』、洗練された愛の神秘論。"),
    ("ヴァルター・フォン・デア・フォーゲルヴァイデ詳論", "Walther von der Vogelweide (detailed)", "Walther von der Vogelweide", "latin", 111,
     "ミンネザング最大の詩人、宮廷恋愛詩・政治シュプルッフ詩を統合した中高ドイツ語抒情の頂点。"),
    ("ニーベルンゲンの歌詳論", "Nibelungenlied (detailed)", "Nibelungenliet", "latin", 111,
     "中高ドイツ語英雄叙事詩、ジークフリートの死とブルグント族滅亡を描く写本ABCの異本群。"),
    ("クードルーン", "Kudrun", "Kūdrūn", "latin", 119,
     "13世紀中高ドイツ語英雄叙事詩、北海伝承を背景に女性主人公の忍耐と救出を描く。"),

    # Cluster 4: 中世スカンジナビア (period 218)
    ("スノッリ『ヘイムスクリングラ』詳論", "Snorri Heimskringla", "Heimskringla", "latin", 218,
     "スノッリ・ストルルソンによるノルウェー王列伝、サガ史学の代表作で17王の生涯を編年。"),
    ("『エギルのサガ』詳論", "Egils saga (detailed)", "Egils saga Skalla-Grímssonar", "latin", 218,
     "10世紀スカルド詩人エギル・スカラグリムスソンの生涯を描く家族サガ、詩人サガの典型。"),
    ("『ニャールのサガ』詳論", "Njáls saga (detailed)", "Brennu-Njáls saga", "latin", 218,
     "アイスランド家族サガ最長作、ニャールとグンナルの友情と血讐連鎖、焼討事件を描く。"),
    ("『ラックスデーラ・サガ』", "Laxdæla saga", "Laxdæla saga", "latin", 218,
     "アイスランド家族サガ、グズルーンとキャルタンの三角関係を中心とする西部ラックス谷の年代記。"),
    ("『ヴォルスンガ・サガ』", "Volsunga saga", "Vǫlsunga saga", "latin", 218,
     "13世紀古ノルド散文サガ、シグルズとブリュンヒルドの伝説を集大成した英雄サガの祖型。"),
    ("『ハーヴァマール』", "Hávamál", "Hávamál", "latin", 218,
     "古エッダ所収の教訓詩、オーディン仮託の処世訓・ルーン秘儀を含む北欧知恵文学。"),

    # Cluster 5: 中世伊・西 (period 212 / 215)
    ("チーノ・ダ・ピストイア詳論", "Cino da Pistoia (detailed)", "Cino da Pistoia", "latin", 212,
     "ドルチェ・スティル・ノーヴォ詩人で法学者、ダンテとペトラルカを橋渡しする抒情の中継点。"),
    ("グイットーネ・ダレッツォ", "Guittone d'Arezzo", "Guittone d'Arezzo", "latin", 212,
     "13世紀トスカーナ詩人、シチリア派とドルチェ・スティル・ノーヴォを繋ぐ説教的・政治的詩風。"),
    ("グイド・カヴァルカンティ詳論", "Guido Cavalcanti (detailed)", "Guido Cavalcanti", "latin", 212,
     "ドルチェ・スティル・ノーヴォの哲学的詩人、愛の自然学的考察と『ドンナ・ミ・プレガ』。"),
    ("ヤコポーネ・ダ・トーディ詳論", "Iacopone da Todi (detailed)", "Iacopone da Todi", "latin", 212,
     "フランチェスコ会霊性詩人、俗語ラウダとラテン語『スタバト・マーテル』の作者とされる。"),
    ("ベルセオ『聖母奇蹟譚』詳論", "Berceo Milagros de Nuestra Señora", "Milagros de Nuestra Señora", "latin", 215,
     "ゴンサロ・デ・ベルセオの聖母奇蹟譚、メステル・デ・クレレシーアの代表作・四行定型詩。"),
    ("フアン・ルイス『良き愛の書』詳論", "Juan Ruiz Libro de Buen Amor", "Libro de Buen Amor", "latin", 215,
     "イータの司祭フアン・ルイスのカスティーリャ語詩物語、聖俗の愛を二重に語るパロディ的傑作。"),
]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted, skipped = 0, 0
    for name_ja, name_en, name_orig, script, period_id, definition in CONCEPTS:
        assert len(definition) <= 100, f"def too long ({len(definition)}): {name_ja}"
        try:
            cur.execute("""
                INSERT INTO concepts (name_ja, name_en, name_original, original_script,
                    subfield_id, region, period_id, definition, importance_score)
                VALUES (?,?,?,?,?,?,?,?,3)
            """, (name_ja, name_en, name_orig, script, SUBFIELD_ID, REGION, period_id, definition))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    conn.close()
    print(f"inserted={inserted} skipped={skipped} total={len(CONCEPTS)}")


if __name__ == "__main__":
    main()
