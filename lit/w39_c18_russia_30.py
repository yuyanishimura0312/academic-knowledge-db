#!/usr/bin/env python3
"""Wave 39: add 30 ultra-niche concepts to lit_russia_slavic."""

from lit_db_helper import LitDB

SUBFIELD = "lit_russia_slavic"
REGION = "東欧・ロシア"

P_SENT = 200
P_ROM = 201
P_REAL = 202
P_SILVER = 203
P_SOV_MID = 206
P_SOV_LATE = 207
P_CZECH = 209
P_POLISH = 210
P_SOUTH = 211
P_MED = 220

CONCEPTS = [
    # Cluster 1: medieval and early East Slavic textuality
    ("キリル・トゥロフスキー説教装飾文体", "Kirill Turovsky ornate sermons", P_MED, "12世紀ルーシ説教で比喩連鎖と典礼語を密に重ねる装飾散文。"),
    ("ダニイル隠者『祈願』二重声", "Daniel the Immured Supplication", P_MED, "卑下する請願と鋭い政治助言が同居する中世ルーシの宮廷散文。"),
    ("『ステファン・ペルム伝』文字創成譚", "Life of Stephen of Perm alphabet myth", P_MED, "コミ人宣教と文字発明を聖人伝へ組み込む北東ルーシの宣教文学。"),
    ("『カザン史』征服叙事", "History of Kazan conquest narrative", P_MED, "イヴァン四世のカザン征服を聖戦と帝国拡張の語りで正当化する史書。"),
    ("『ピョートルとフェヴロニヤ物語』聖婚譚", "Peter and Fevronia sacred marriage", P_MED, "知恵ある農民女性と公の結婚を聖性へ転じるムーロム伝説物語。"),
    ("シメオン・ポロツキー宮廷音節詩", "Simeon Polotsky syllabic court verse", P_MED, "モスクワ宮廷でポーランド風音節詩を導入した17世紀教養詩。"),

    # Cluster 2: obscure nineteenth-century Russian prose and criticism
    ("ヴェルトマン『不死身コシチェイ』時空戯画", "Veltman Koshchei time-space burlesque", P_ROM, "古代ロシア風冒険を時代錯誤と語りの脱線で崩す初期歴史小説。"),
    ("センコフスキー東方奇譚", "Senkovsky oriental tales", P_ROM, "アラビア趣味と学識冗談を混ぜたベストゥージェフ＝マルリンスキー周辺の奇譚。"),
    ("オドエフスキー『ロシアの夜』断章哲学", "Odoevsky Russian Nights fragments", P_ROM, "対話と幻想短編を交互に置き芸術・科学・信仰を論じる哲学小説。"),
    ("マルリンスキー高加索冒険譚", "Marlinsky Caucasus adventure tales", P_ROM, "流刑将校の高加索経験を決闘・名誉・異国趣味へ変えたロマン派散文。"),
    ("ダール民衆語彙スケッチ", "Dal folk lexicon sketches", P_REAL, "方言語彙と職人観察を小品へ織り込む辞書編纂者ダールの民俗散文。"),
    ("ナジェージジン『テレスコープ』批評圏", "Nadezhdin Teleskop critical circle", P_REAL, "チャアダーエフ掲載前後に哲学批評と検閲衝突を抱えた1830年代誌面。"),

    # Cluster 3: marginal Silver Age formations
    ("ニコライ・ミンスキーのメオニズム", "Nikolai Minsky meonism", P_SILVER, "非存在への意志を宗教哲学化した初期ロシア象徴主義の周縁思想。"),
    ("エリス象徴主義翻訳圏", "Ellis symbolist translation milieu", P_SILVER, "ボードレール受容と神智学的注釈を結ぶ若象徴派周辺の翻訳実践。"),
    ("ボリス・サドフスコイ擬古詩", "Boris Sadovskoy archaizing verse", P_SILVER, "18世紀風語彙と貴族趣味で銀の時代の反近代姿勢を詩化した作風。"),
    ("セルゲイ・ソロヴィヨフ若象徴派詩", "Sergei Solovyov junior symbolist verse", P_SILVER, "宗教的エロスと古典神話を薄明の抒情へ寄せる若象徴派の小詩圏。"),
    ("ヴォローシン『燃える茨』クリミア神話", "Voloshin Burning Bush Crimea myth", P_SILVER, "コクテベリ風景を黙示録的ロシア像へ重ねるヴォローシン詩集の核。"),
    ("チェルビナ・デ・ガブリアク仮面詩", "Cherubina de Gabriak mask poetry", P_SILVER, "架空スペイン貴婦人の仮名で雑誌界を揺らした女性詩人の仮面戦略。"),

    # Cluster 4: Soviet micro-movements and unofficial genres
    ("イマジニズム『宣言』", "Russian Imaginist Declaration", P_SOV_MID, "比喩イメージの自律を掲げエセーニン周辺が出した短命前衛詩の綱領。"),
    ("プロレトクリト工場抒情", "Proletkult factory lyric", P_SOV_MID, "機械・集団労働・新語を称揚する初期ソ連労働者詩の実験。"),
    ("生産小説コンヴェイヤー詩学", "Production novel conveyor poetics", P_SOV_MID, "工場工程と五カ年計画を人物造形より優先する1930年前後の小説技法。"),
    ("チュヴァシ詩ナロード語彙", "Chuvash poetry narod vocabulary", P_SOV_MID, "チュヴァシ語民謡語彙を革命詩へ接続したヴォルガ少数民族文学の手法。"),
    ("アブラム・テルツ寓話的密輸", "Abram Tertz allegorical smuggling", P_SOV_LATE, "シニャフスキーが筆名で国外へ出した幻想寓話による検閲回避の文体。"),
    ("マニエリスト派オルデンブルク会", "Order of Courtly Mannerists", P_SOV_LATE, "中世騎士団を戯画化し儀礼化した1980年代モスクワ地下詩グループ。"),

    # Cluster 5: West and South Slavic regional niches
    ("ムウォダ・ポルスカ農民神秘主義", "Young Poland peasant mysticism", P_POLISH, "農村儀礼とカトリック象徴を混ぜる若きポーランド期の地方幻想。"),
    ("ブルーノ・ヤシェンスキ未来派綴字", "Bruno Jasieński futurist orthography", P_POLISH, "音声化綴字と都市速度で標準ポーランド語を揺さぶる未来派詩法。"),
    ("ヴィチエズスラフ・ネズヴァル夢幻連作", "Vitezslav Nezval dream cycles", P_CZECH, "ポエティスムからシュルレアリスムへ移る夢と映画的連想の詩連作。"),
    ("ラジスラフ・クリーマ哲学幻想", "Ladislav Klima philosophical grotesque", P_CZECH, "極端な主観哲学を怪奇小説と黒い笑いへ注ぐチェコ散文の異端。"),
    ("スロヴェニア・モデルナ抒情", "Slovene Moderna lyric", P_SOUTH, "ツァンカル周辺が都市不安と象徴主義をスロヴェニア語詩へ導入した潮流。"),
    ("マケドニア民謡採録詩学", "Macedonian folk-song collection poetics", P_SOUTH, "口承民謡の採録と標準語形成が結びつくマケドニア近代文学の基層。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
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
        total = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 18"
        ).fetchone()["c"]
    print(f"Inserted: {inserted}, Skipped: {skipped}, Subfield 18 total: {total}")


if __name__ == "__main__":
    main()
