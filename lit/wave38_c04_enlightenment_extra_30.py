#!/usr/bin/env python3
"""Wave 38: add 30 extra niche concepts to lit_eu_enlightenment."""

from lit_db_helper import LitDB

SUBFIELD = "lit_eu_enlightenment"
REGION = "西欧"

# Five thematic clusters x six concepts. Period ids are 西欧 periods.
CONCEPTS = [
    # Cluster 1: French clandestine and para-Enlightenment prose
    ("アナ『テレーズ哲学者』", "Therese Philosophe", "Therese philosophe", 100,
     "地下出版のリベルタン小説。唯物論と性愛論を対話体で結ぶ。"),
    ("ティフェーニュ『ギフアンティ』", "Tiphaigne de la Roche Giphantie", "Giphantie", 100,
     "写真を予見する幻想旅行譚。技術的幻視と風刺を交差させる。"),
    ("メルシエ『二四四〇年』", "Mercier L'An 2440", "L'An 2440", 102,
     "未来パリを舞台にした啓蒙的ユートピア小説。改革願望を都市像に託す。"),
    ("ムーイ『成り上がり農婦』", "Mouhy La Paysanne parvenue", "La Paysanne parvenue", 100,
     "女性版成り上がり小説。奉公・誘惑・社交上昇を連載形式で描く。"),
    ("デュクロ『コンフェッション』", "Duclos Confessions du comte de ***", "Confessions du comte de ***", 100,
     "貴族的放蕩の回想小説。社交界の心理観察を告白形式に収める。"),
    ("マルモンテル『道徳物語』", "Marmontel Contes moraux", "Contes moraux", 100,
     "短篇教訓譚集。社交的感性と穏健な道徳判断を物語化する。"),

    # Cluster 2: British women's fiction and sensibility margins
    ("ヘイウッド『過剰な恋』", "Eliza Haywood Love in Excess", "Love in Excess", 99,
     "情念過多の恋愛小説。女性欲望とスキャンダル出版の境界を示す。"),
    ("レノックス『女キホーテ』", "Charlotte Lennox The Female Quixote", "The Female Quixote", 100,
     "ロマンス読書を風刺する小説。女性読者とジャンル錯誤を主題化。"),
    ("スコット『ミレニアム・ホール』", "Sarah Scott Millenium Hall", "A Description of Millenium Hall", 101,
     "女性共同体ユートピア小説。慈善・教育・独身生活を制度化する。"),
    ("マッケンジー『感情の人』", "Mackenzie The Man of Feeling", "The Man of Feeling", 101,
     "断片形式の感傷小説。涙と徳の過剰が男性主体を解体する。"),
    ("シャーロット・スミス『エメリン』", "Charlotte Smith Emmeline", "Emmeline", 102,
     "女性の経済的不安を描く小説。感傷と社会批判を接続する。"),
    ("ブルック『エミリー・モンタギュー』", "Frances Brooke The History of Emily Montague", "The History of Emily Montague", 101,
     "カナダ植民地を舞台にした書簡体小説。感傷と帝国観察を結ぶ。"),

    # Cluster 3: German-Swiss poetics and minor prose
    ("ボードマー『ノアキーデ』", "Bodmer Die Noachide", "Die Noachide", 99,
     "ノア洪水を扱う宗教叙事詩。ミルトン受容と独語叙事詩実験。"),
    ("ブライティンガー『批判詩学』", "Breitinger Critische Dichtkunst", "Critische Dichtkunst", 99,
     "可能世界論を詩学化した書。想像力の規則性を擁護する。"),
    ("ゲラート『スウェーデン伯爵夫人』", "Gellert Swedish Countess", "Leben der schwedischen Grafin von G***", 100,
     "ドイツ初期家庭小説。徳・友情・結婚を平明散文で調停する。"),
    ("ニコライ『ゼーバルトゥス』", "Nicolai Sebaldus Nothanker", "Sebaldus Nothanker", 102,
     "啓蒙派の反敬虔主義小説。出版界と神学論争を風刺する。"),
    ("ムゼーウス『ドイツ民話集』", "Musaus Volksmarchen der Deutschen", "Volksmarchen der Deutschen", 102,
     "民話素材の文人風再話集。啓蒙的機知で怪異を処理する。"),
    ("ヒッペル『結婚について』", "Hippel Uber die Ehe", "Uber die Ehe", 102,
     "結婚制度を諧謔的に論じる散文。市民的親密圏を解剖する。"),

    # Cluster 4: Gothic and antiquarian byways
    ("アイクン夫妻『散文雑篇』", "Aikin Miscellaneous Pieces in Prose", "Miscellaneous Pieces in Prose", 101,
     "初期ゴシック短篇を含む散文集。恐怖美学を実験的に提示する。"),
    ("リー『休息所』", "Sophia Lee The Recess", "The Recess", 292,
     "歴史ゴシック小説。エリザベス朝陰謀譚を女性幽閉の物語に変える。"),
    ("パーソンズ『ヴォルフェンバッハ城』", "Eliza Parsons Castle of Wolfenbach", "The Castle of Wolfenbach", 292,
     "ミネルヴァ・プレス系ゴシック。追跡と出生秘密を通俗化する。"),
    ("ロシュ『クレルモン』", "Regina Maria Roche Clermont", "Clermont", 292,
     "女性ゴシック小説。父娘関係と城館陰謀を感傷的に編む。"),
    ("スミス『古い館』", "Charlotte Smith The Old Manor House", "The Old Manor House", 292,
     "相続と戦争を絡める小説。ゴシック空間を社会批判に転用する。"),
    ("ベックフォード『ヴァテック』", "Beckford Vathek", "Vathek", 102,
     "東方幻想ゴシック。欲望と異教的地獄を豪奢な散文で描く。"),

    # Cluster 5: Italian and Iberian Enlightenment forms
    ("ヴェッリ兄弟『カッフェ』", "Il Caffe periodical", "Il Caffe", 100,
     "ミラノ啓蒙の定期刊行物。経済・言語・風俗改革を散文で進める。"),
    ("ゴッツィ『三つのオレンジへの恋』", "Gozzi Love for Three Oranges", "L'amore delle tre melarance", 102,
     "即興喜劇を寓話劇化した作品。啓蒙喜劇改革への反発を示す。"),
    ("ゴッツィ『トゥーランドット』", "Gozzi Turandot", "Turandot", 102,
     "東方姫君の謎解き劇。仮面喜劇と幻想演劇を結合する。"),
    ("メタスタージオ『見捨てられたディドーネ』", "Metastasio Didone abbandonata", "Didone abbandonata", 99,
     "オペラ・セリア台本の典型。情念と義務の葛藤を整序する。"),
    ("カダルソ『モロッコ書簡』", "Cadalso Moroccan Letters", "Cartas marruecas", 102,
     "異邦人書簡体のスペイン批判。国民性と後進性を相対化する。"),
    ("イリアルテ『文学寓話集』", "Iriarte Literary Fables", "Fabulas literarias", 102,
     "文学論争を寓話化した詩集。作家気質と詩法の欠陥を諷刺する。"),
]


def main() -> None:
    inserted = skipped = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            before = db.find_concept(name_ja, REGION, period_id)
            cid = db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script="latin",
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            if before:
                skipped += 1
            elif cid:
                inserted += 1
        total = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id = 4"
        ).fetchone()[0]
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total: {total}")


if __name__ == "__main__":
    main()
