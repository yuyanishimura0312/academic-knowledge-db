#!/usr/bin/env python3
"""Wave 43: add 30 ultra-niche concepts to lit_russia_slavic."""

from lit_db_helper import LitDB

SUBFIELD = "lit_russia_slavic"
REGION = "東欧・ロシア"

P_GOLDEN = 291
P_REAL = 202
P_SILVER = 203
P_FORM = 204
P_BAKH = 205
P_SOV_MID = 206
P_SOV_LATE = 207
P_POST = 208
P_CZECH = 209
P_POLISH = 210
P_SOUTH = 211

CONCEPTS = [
    # Cluster 1: early East Slavic textual microgenres
    ("『モノマフ訓戒』統治父性", "Monomakh Instruction paternal rule", None, "公子への倫理訓戒を父権的統治理念へ結ぶキエフ期教訓文。"),
    ("キリク問答の暦法細目", "Kirik Questions calendrical minutiae", None, "復活祭計算と典礼実務を問答化するノヴゴロド聖職者文献。"),
    ("『ダニイル巡礼記』聖地測量", "Daniel Pilgrim holy-land measurement", None, "聖地の距離と祭儀場所を実測風に記すルーシ巡礼記の記述法。"),
    ("『サヴァ・グルツィン物語』悪魔契約譚", "Savva Grudtsyn devil pact tale", None, "若者の放蕩と悪魔契約を世俗小説的筋で描く17世紀物語。"),
    ("『フロルとラヴル物語』馬医聖人譚", "Flor and Lavr horse-healer saints", None, "馬の治癒奇跡を職能信仰と結ぶ民衆的聖人説話。"),
    ("『シェミャーカ裁判』逆転笑話", "Shemyaka Judgment reversal tale", None, "不条理判決が弱者の利得へ転じる17世紀風刺笑話。"),

    # Cluster 2: nineteenth-century Russian marginal prose and criticism
    ("ナデージジン『モルヴァ』新聞批評圏", "Nadezhdin Molva newspaper criticism", P_GOLDEN, "週刊紙の短評で文学市場と哲学批評を接続した1830年代誌面。"),
    ("ドルージニン美的批評の余暇論", "Druzhinin aesthetic criticism leisure", P_REAL, "功利主義批評に抗し読書の自由と芸術的快を擁護した批評語彙。"),
    ("ピセムスキー『千の魂』官僚心理", "Pisemsky Thousand Souls bureaucracy", P_REAL, "昇進欲と地方行政の腐敗を心理リアリズムで描く官僚小説。"),
    ("スレプツォフ『困難な時代』急進サロン", "Sleptsov Hard Times radical salon", P_REAL, "女性解放と急進思想の生活実験を小説内サロンで試す1860年代散文。"),
    ("マルコ・ヴォフチョク農奴女性語り", "Marko Vovchok serf-woman narration", P_REAL, "ウクライナ農奴女性の声を口承調でロシア語圏へ媒介した散文。"),
    ("ボボルイキン『キタイ・ゴロド』都市記録", "Boborykin Kitai-Gorod urban chronicle", P_REAL, "商業街区の会話と消費を連載小説的に記録するモスクワ都市散文。"),

    # Cluster 3: Silver Age little journals, performance, and occult craft
    ("『ミール・イスクーストヴァ』誌面エクフラシス", "Mir iskusstva ekphrastic pages", P_SILVER, "美術批評と詩的散文を図版配置で交差させる雑誌文体。"),
    ("バルモント音韻過剰詩学", "Balmont sonic excess poetics", P_SILVER, "頭韻・母音反復で意味を溶かす象徴主義の音楽化技法。"),
    ("アンネンスキー悲劇翻訳の仮面", "Annensky tragic translation mask", P_SILVER, "ギリシア悲劇翻訳を自己の叙情的仮面として用いる詩的実践。"),
    ("サバシニコフ出版社古典叢書", "Sabashnikov classical series", P_SILVER, "校訂・装丁・注釈で古典受容を近代出版文化へ組み替えた叢書。"),
    ("『コメディアンの休憩所』カバレット戯文", "Comedians' Halt cabaret prose", P_SILVER, "前衛俳優と詩人が即興寸劇を雑誌的戯文へ変える小劇場文化。"),
    ("フョードル・ソログーブ小悪魔的短章", "Sologub petty-demonic miniature", P_SILVER, "日常の悪意を短い寓話的散文へ凝縮するデカダンス小品。"),

    # Cluster 4: formalist, Bakhtinian, and Soviet micro-poetics
    ("ヴォロシノフ『フロイト主義』批判文体", "Voloshinov Freudianism polemic", P_BAKH, "精神分析を社会的記号論から批判するバフチン圏の論争文体。"),
    ("メドヴェージェフ『形式的方法』社会詩学", "Medvedev formal method social poetics", P_BAKH, "フォルマリズムを社会的評価の場へ置き直すバフチン圏の詩学。"),
    ("『リテラトゥルナヤ・ウチョーバ』工房批評", "Literaturnaya ucheba workshop criticism", P_FORM, "若手作家教育を誌面添削と創作講座で制度化した批評形式。"),
    ("チュコフスキー『チュコッカラ』家庭アルバム文体", "Chukovsky Chukokkala album style", P_SOV_MID, "作家の落書き・献辞・似顔絵を家庭的文学資料へ束ねるアルバム。"),
    ("ハルムス事件散文の反因果", "Kharms incident prose anti-causality", P_SOV_MID, "出来事が理由なく発生し途切れるオベリウ系短散文の構成法。"),
    ("ヴヴェデンスキー時間崩壊詩劇", "Vvedensky time-collapse verse drama", P_SOV_MID, "会話と時間概念を破綻させ存在論的不安を舞台化する詩劇。"),

    # Cluster 5: late Soviet, post-Soviet, West and South Slavic niches
    ("ユジンスキー・サークル秘教読解", "Yuzhinsky circle esoteric reading", P_SOV_LATE, "地下読書会で神秘思想と前衛文学を重ねるモスクワ非公式知。"),
    ("ネクロリアリズム散文映像圏", "Necrorealist prose-film milieu", P_POST, "死体喜劇と粗い映像感覚を散文にも移すペテルブルク地下美学。"),
    ("ルビンシュテインカード詩", "Rubinstein card-catalog poem", P_POST, "図書カード形式で発話断片を並べるモスクワ・コンセプチュアリズム詩。"),
    ("クラクフ・アヴァンガルダ三M標語", "Krakow Avant-Garde three M slogan", P_POLISH, "都市・大衆・機械を掲げ詩の圧縮構成を求めたポーランド前衛標語。"),
    ("スロヴァキア・ナドレアリスム詩", "Slovak Nadrealism poetry", P_CZECH, "シュルレアリスムをスロヴァキア語抒情へ移植した戦間期前衛詩。"),
    ("スロヴェニア『ノヴァ・レヴィヤ』反体制文芸", "Nova revija dissident literature", P_SOUTH, "文芸誌を通じ民族論と民主化言説を育てたスロヴェニア知識人圏。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    assert len(CONCEPTS) == 5 * 6
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 18"
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
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            inserted += 1
    print(f"Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
