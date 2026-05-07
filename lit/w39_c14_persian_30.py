#!/usr/bin/env python3
"""Wave 39: add 30 ultra-niche concepts to lit_persian_turkish."""

from lit_db_helper import LitDB

SUBFIELD = "lit_persian_turkish"
REGION = "南西アジア"

P_EARLY = 250
P_MID = 47
P_PROSE = 141
P_LATE = 48
P_HINDI = 142
P_OTTOMAN = 49
P_TANZ = 50
P_MODERN = 51
P_CENTRAL = 143
P_MINOR = 252

CONCEPTS = [
    # Cluster 1: early Persian court and regional lyric microforms
    ("ムンジーク・テルメズィー風刺断片", "Munjik Tirmidhi satirical fragments", P_EARLY, "サーマーン朝周辺の辛辣な宮廷風刺を伝える断片詩群。"),
    ("キサーイー・マルヴァズィー悔悟詩", "Kisai Marvazi penitential poetry", P_EARLY, "称賛詩から宗教的悔悟へ転じた初期ペルシア詩の小系譜。"),
    ("アブー・シュクール『アーファリーン・ナーメ』", "Abu Shakur's Afarin-nameh", P_EARLY, "格言と教訓を短句で連ねるサーマーン朝期の失われた教訓詩。"),
    ("ダキーキーのゾロアスター挿話", "Daqiqi Zoroaster episode", P_EARLY, "『シャー・ナーメ』に残るグシュタースプ改宗物語の先行詩片。"),
    ("アブー・サイード四行詩帰属伝承", "Abu Sa'id quatrain attribution", P_EARLY, "聖者名に後世の神秘主義ルバーイーが集積する帰属伝承。"),
    ("ラビア・バルヒー恋愛詩伝説", "Rabi'a Balkhi love-lyric legend", P_EARLY, "初期女性詩人像を殉愛物語と断片詩で伝えるバルフ伝承。"),

    # Cluster 2: Persian prose, adab, and minor mirror texts
    ("『ムジュマル・アルタワーリーフ』無名史書", "Mujmal al-tawarikh anonymous chronicle", P_PROSE, "神話王朝から同時代までを簡潔に配列する12世紀ペルシア語史書。"),
    ("『ファールス・ナーマ』地方史叙述", "Fars-nameh regional historiography", P_PROSE, "ファールス地方の王統・地理・逸話を束ねる地域史散文。"),
    ("『サマク・アイヤール』アイヤール語り", "Samak-e Ayyar chivalric prose", P_PROSE, "義侠的盗賊の変装と策謀を連ねる長大な口承系ロマンス。"),
    ("『マルズバーン・ナーメ』動物寓話", "Marzban-nameh animal fables", P_PROSE, "タバリスターン系素材を宮廷的教訓寓話へ改作した散文集。"),
    ("アウフィー『逸話集』詩人小伝", "Awfi anecdotal biographies", P_PROSE, "詩人列伝と逸話を混ぜる初期ペルシア文学史資料。"),
    ("『シンドバード・ナーメ』枠物語", "Sindbad-nameh frame tale", P_PROSE, "王子沈黙譚を女性悪知恵説話群で囲むペルシア語枠物語。"),

    # Cluster 3: post-Mongol, Timurid, and Indo-Persian obscurities
    ("ヴァッサーフ華麗体史書", "Vassaf ornate historiography", P_LATE, "誇張された修辞でイルハン朝史を飾る難解散文の代表例。"),
    ("ハージュー『フマイとフマーユーン』", "Khwaju's Humay u Humayun", P_LATE, "ニザーミー模倣をケルマーン詩人が宮廷恋愛譚へ変えたマスナヴィー。"),
    ("ウバイド・ザーカーニー『猫と鼠』", "Ubayd Zakani's Cat and Mouse", P_LATE, "捕食寓話で宗教権威と政治権力を風刺する短編詩物語。"),
    ("イブン・ヤミーン断章詩", "Ibn Yamin qit'a poetry", P_LATE, "日常倫理と社会観察を短いキトアに凝縮したホラーサーン詩。"),
    ("ファッルヒー・ヤズディー獄中詩", "Farrukhi Yazdi prison poetry", P_MODERN, "口を縫われた革命詩人像と結びつく立憲期ペルシア抵抗詩。"),
    ("ガーニー・カシュミーリー詩", "Ghani Kashmiri poetry", P_HINDI, "カシミールの感覚的比喩でサブク・ヒンディーを細密化した詩。"),

    # Cluster 4: Ottoman marginal forms, periodicals, and manuscript culture
    ("ルズナーメ宮廷日誌文学", "Ottoman ruzname court diaries", P_OTTOMAN, "宮廷日誌の定型記録が逸話的散文へにじむオスマン文書文化。"),
    ("セルギュゼシュト自伝的捕囚譚", "Serguzest captivity narrative", P_OTTOMAN, "遍歴・捕囚・改宗体験を一人称で語るオスマン散文小ジャンル。"),
    ("エヴリヤー『夢の序』", "Evliya Celebi dream prologue", P_OTTOMAN, "旅の使命を預言者夢で正当化する『旅行記』冒頭の自己神話化。"),
    ("ランプルル・ファーイズ雑録", "Lemprulu Faiz miscellany", P_OTTOMAN, "詩・逸話・宮廷情報を雑多に集める写本メジュムア文化の一例。"),
    ("エンデルンル・ファーズル『女性の書』", "Enderunlu Fazil's Book of Women", P_OTTOMAN, "帝都と諸民族の女性像を風俗分類する後期ディーワーン詩。"),
    ("ミフリ・ハトゥン女性ディーワーン", "Mihri Hatun's divan", P_OTTOMAN, "アマスヤ宮廷で女性詩人が恋愛ガゼルを競作した希少なディーワーン。"),

    # Cluster 5: Turkic, Kurdish, Pashto, and modern peripheral print cultures
    ("カラカルパク『キルク・クズ』叙事詩", "Karakalpak Qirq Qiz epic", P_CENTRAL, "四十人の娘戦士を語るカラカルパク英雄叙事詩。"),
    ("チャガタイ『ラターファト・ナーメ』", "Latafat-nameh Chagatai lyric", P_CENTRAL, "恋人の美を部位ごとに讃えるチャガタイ語の細密恋愛詩。"),
    ("アブドゥルカーディル・ベーディル中央アジア受容", "Bedil Central Asian reception", P_CENTRAL, "ブハラ・ヒヴァのマドラサで難解詩を注釈したベーディル崇拝。"),
    ("バローチ『ハーニーとシェー・ムリード』", "Balochi Hani and Sheh Mureed", P_MINOR, "部族名誉と禁欲的恋を結びつけるバローチ語恋愛叙事詩。"),
    ("パシュトー・ランダイ女性短詩", "Pashto landay women's couplets", P_MINOR, "二行で恋・戦争・家父長制を刺す女性口承短詩。"),
    ("クルド・ゴーラーン語ヤールサーン詩", "Gorani Yarsan sacred verse", P_MINOR, "ヤールサーン信仰の秘教語りをゴーラーン語詩で伝える周縁伝統。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 14"
            )
        }
        for name_ja, name_en, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, f"{name_ja}: {len(definition)}"
            if name_ja in existing:
                skipped += 1
                print(f"[skip-name] {name_ja}")
                continue
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
        total = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 14"
        ).fetchone()["c"]
    print(f"Inserted: {inserted}, Skipped: {skipped}, Subfield 14 total: {total}")


if __name__ == "__main__":
    main()
