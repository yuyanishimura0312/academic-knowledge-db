from lit_db_helper import LitDB


SUBFIELD = "lit_eu_classical"
REGION = "西欧"


ROWS = [
    # Cluster 1: archaic lyric and fragmentary performance
    ("プラティナス『ヒュポルケーマ』断片", "Pratinas hyporchema fragment", "Pratinas Hyporchema", 5, "サテュロス劇詩人に帰される舞踊歌断片。"),
    ("プラクシラ『アドニス歌』断片", "Praxilla Adonis fragment", "Praxilla Adonis song", 5, "死にゆくアドニスの逆説的遺言を伝える抒情詩断片。"),
    ("コリンナ『アソポスの娘たち』", "Corinna, Daughters of Asopus", "Korinna Asopou korai", 5, "ボイオティア神話を地方語で競演化した合唱詩断片。"),
    ("テレス『ディオニュソス讃歌』断片", "Telesilla Dionysus hymn fragment", "Telesilla Dionysus hymn", 5, "アルゴス女性詩人に帰される神歌断片。"),
    ("ラススのディテュランボス改革", "Lasus dithyrambic reform", "Lasus of Hermione", 5, "ディテュランボスの旋律と競演形式を洗練した革新。"),
    ("ティモテオス『ペルシア人』ノモス", "Timotheus, Persians nome", "Timotheos Persai", 5, "新音楽の技巧でサラミス海戦を歌うノモス詩。"),
    # Cluster 2: Hellenistic micro-forms and scholarly poetry
    ("アスクレピアデスの饗宴エピグラム", "Asclepiades sympotic epigram", "Asklepiades epigrams", 7, "酒宴と恋を短章化したサモス系エピグラム群。"),
    ("アニテの動物墓碑銘", "Anyte animal epitaphs", "Anyte animal epitaphs", 7, "小動物の死を悼むヘレニズム女性詩人の墓碑銘群。"),
    ("ノッシスの女性エピグラム", "Nossis female epigrams", "Nossis epigrams", 7, "ロクリス女性詩人がサッポー的系譜を刻む短詩群。"),
    ("リュコプロン『カッサンドラ』語彙難解性", "Lycophron Cassandra obscurity", "Alexandra obscuritas", 7, "神話異名と迂言で構成される極端な難解詩法。"),
    ("エラトステネス『ヘルメス』断片", "Eratosthenes Hermes fragments", "Eratosthenes Hermes", 7, "神話と天文学を結ぶ学匠詩の散逸断片。"),
    ("エウポリオン『トラクス』断片", "Euphorion Thrax fragments", "Euphorion Thrax", 7, "希少神話を凝縮するカルキス派小叙事詩断片。"),
    # Cluster 3: Roman Republican and Augustan marginal texts
    ("ラエウィウス『エロトパイグニア』", "Laevius Erotopaegnia", "Laevius Erotopaegnia", 73, "技巧的恋愛小詩を集めた共和政末期の断片詩集。"),
    ("ウァロ『メニッポス風諷刺』", "Varro Menippean Satires", "Saturae Menippeae", 73, "散文と韻文を混ぜた博識な哲学諷刺断片。"),
    ("カルウスのイオー哀歌", "Calvus Io elegy", "Calvus Io", 73, "カトゥッルス同時代詩人の神話的エピュリオン断片。"),
    ("キンナ『スミュルナ』", "Cinna Smyrna", "Cinna Smyrna", 73, "九年推敲の逸話で知られる新詩人派小叙事詩。"),
    ("マエケナス散文断片", "Maecenas prose fragments", "Maecenas fragments", 74, "アウグストゥス側近に帰される装飾的散文断片。"),
    ("コルネリウス・ガッルス詩断片", "Cornelius Gallus fragments", "Gallus fragments", 74, "ラテン恋愛悲歌創始者のパピルス伝存断片。"),
    # Cluster 4: technical rhetoric, grammar, and scholia
    ("アエリウス・テオン『予備訓練』", "Aelius Theon Progymnasmata", "Progymnasmata", 75, "寓話・比較などを教える最古級の修辞訓練書。"),
    ("アプトニオス『予備訓練』", "Aphthonius Progymnasmata", "Progymnasmata", 198, "ビザンツ学校で標準化した短作文課題集。"),
    ("ヘシュキオス辞典", "Hesychius Lexicon", "Lexicon", 198, "希語難語と方言語彙を保存する後期古代辞書。"),
    ("エウスタティオス『イリアス注解』", "Eustathius Commentary on Iliad", "Parekbole", 199, "ホメロス本文を博引旁証で読むビザンツ注釈。"),
    ("ツェツェス『千行詩』", "Tzetzes Chiliades", "Chiliades", 199, "逸話と古典知識を政治詩で配列する注釈的長詩。"),
    ("ホメロス小辞典『デ・シグニフィカートゥ』", "Homeric D-scholia", "D-scholia", 198, "語釈中心の初学者向けホメロス注釈群。"),
    # Cluster 5: late antique Christian and cento microgenres
    ("プロバ『ウェルギリウス百行詩』", "Proba Virgilian cento", "Cento Vergilianus", 198, "ウェルギリウス句だけで聖書物語を再構成する百行詩。"),
    ("ファルコニア・プロバの創世記再話", "Faltonia Proba Genesis retelling", "Genesis cento", 198, "創世記をラテン叙事詩句で編み直す女性作家の試み。"),
    ("アヴィトゥス『霊的歴史』", "Avitus Spiritual History", "De spiritalis historiae gestis", 198, "創世記主題を叙事詩化したガリア司教の六歩格詩。"),
    ("アルキムス・アウィトゥス楽園詩", "Avitus paradise poetry", "De origine mundi", 198, "楽園と堕罪を古典叙事詩語法で描く聖書詩。"),
    ("キプリアヌス・ガルス『ヘプタテウコス』", "Cyprianus Gallus Heptateuchos", "Heptateuchos", 198, "モーセ五書ほかをラテン六歩格に移す聖書叙事詩。"),
    ("オリエンティウス『勧告詩』", "Orientius Commonitorium", "Commonitorium", 198, "俗世批判と悔悛を二行詩で説くガリア教訓詩。"),
]


def main() -> None:
    if len(ROWS) != 30:
        raise SystemExit(f"expected 30 rows, got {len(ROWS)}")
    too_long = [name for name, *_rest, definition in ROWS if len(definition) > 100]
    if too_long:
        raise SystemExit(f"definition too long: {too_long}")

    with LitDB() as db:
        existing = [
            name for name, _en, _orig, period_id, _definition in ROWS
            if db.find_concept(name, REGION, period_id)
        ]
        if existing:
            raise SystemExit(f"already exists: {existing}")

        inserted = 0
        for name_ja, name_en, name_original, period_id, definition in ROWS:
            before = db.conn.total_changes
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=1,
                source_tier="secondary",
                canonical_in_region="marginal",
                skip_duplicates=False,
            )
            inserted += db.conn.total_changes - before
        print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
