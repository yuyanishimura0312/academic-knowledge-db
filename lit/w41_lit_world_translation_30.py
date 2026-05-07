#!/usr/bin/env python3
from lit_db_helper import LitDB

DB = "lit.sqlite"
SUBFIELD = "lit_world_translation"

CONCEPTS = [
    # Cluster 1: manuscript and missionary translation micro-traditions
    ("ソグド語マニ教讃歌の漢語傍訳", "Chinese glosses on Sogdian Manichaean hymns", "Sogdian Manichaean hymns", "ソグド語讃歌に添う漢語傍訳が教義語を橋渡しする写本層。", "中央アジア"),
    ("トカラ語仏典断片の梵語復元訳", "Sanskrit back-rendering of Tocharian Buddhist fragments", "Tocharian fragments", "トカラ語断片から失われた梵語原典を推定する逆翻訳実践。", "中央アジア"),
    ("古ウイグル語マニ教説話の重訳", "Relay translation of Old Uyghur Manichaean tales", "Old Uyghur tales", "中世イラン語素材が古ウイグル語へ移る重訳説話群。", "中央アジア"),
    ("アルメニア語エフレム讃歌のギリシア語逆流", "Greek reflow of Armenian Ephrem hymns", "Ephrem hymns", "シリア語讃歌がアルメニア語を経てギリシア語圏へ戻る回路。", "コーカサス"),
    ("マロン派ガルシューニー説教訳", "Maronite Garshuni sermon translation", "Garshuni sermons", "アラビア語説教をシリア文字で書く越境的な翻訳書記。", "レバント"),
    ("コンゴ王国カテキズム葡語訳", "Kongo catechism in Portuguese translation", "Kongo catechism", "キコンゴ教理問答が葡語布教語彙と交差した初期訳例。", "アフリカ"),

    # Cluster 2: minor-language relay and bilingual edition niches
    ("リヴォニア語詩のラトビア語窓口", "Livonian-Latvian poetry mediation", "Livonian poetry", "リヴォニア語詩がラトビア語対訳で可読圏を得る出版形式。", "バルト"),
    ("アロマン語民謡のルーマニア語編訳", "Aromanian-Romanian folksong adaptation", "Aromanian folksongs", "アロマン語歌謡がルーマニア語で国民民俗へ編入される訳。", "バルカン"),
    ("コーンウォール語復興劇の英語併記", "Cornish revival drama with English facing text", "Cornish drama", "復興コーンウォール語劇が英語併記で上演性を確保する型。", "西欧"),
    ("サルデーニャ語詩の伊語自己対訳", "Sardinian-Italian poetic self-translation", "Sardinian poetry", "島嶼語詩人が伊語自己対訳で読者圏を二重化する実践。", "地中海"),
    ("ヴェプス語童話の露語ピボット", "Veps-Russian fairy-tale pivot translation", "Veps tales", "ヴェプス語童話がロシア語を経て研究・児童書化される経路。", "北東欧"),
    ("ラトガレ語小説の標準ラトビア語橋渡し", "Latgalian fiction via standard Latvian", "Latgalian fiction", "ラトガレ語小説が標準ラトビア語版で国内正典へ接続する。", "バルト"),

    # Cluster 3: forgotten works and local genres in translation
    ("パンジャーブ語キッサー英訳抄本", "English abridgements of Punjabi qissa", "Punjabi qissa", "恋愛叙事キッサーを英訳抄本が民俗資料化する翻訳編集。", "南アジア"),
    ("シンド語シャー・ジョ・リサーロ部分訳", "Partial translations of Shah Jo Risalo", "Shah Jo Risalo", "シンド語詩集の選択訳が神秘主義像を作る受容単位。", "南アジア"),
    ("マダガスカル語ハインテニー仏訳", "French translation of Malagasy hain-teny", "hain-teny", "謎掛け恋歌ハインテニーの比喩連鎖を仏語へ移す試み。", "インド洋"),
    ("ハウサ語ソヤイヤ小説の英語要約訳", "English summaries of Hausa soyayya novels", "soyayya fiction", "恋愛大衆小説が英語要約で研究市場へ入る縮約翻訳。", "西アフリカ"),
    ("ウォロフ語タース詩の仏語散文化", "French prose rendering of Wolof taas poetry", "taas poetry", "タースの即興韻律が仏語散文で説明化される翻訳課題。", "西アフリカ"),
    ("ミシュテカ語絵文書の西語読解訳", "Spanish reading translation of Mixtec codices", "Mixtec codices", "絵文書の図像列を西語叙述へ変換する読解翻訳。", "メソアメリカ"),

    # Cluster 4: censorship, exile, and paratextual translation circuits
    ("ハンガリー亡命詩の独語小雑誌訳", "German little-magazine translations of Hungarian exile poetry", "exile poetry", "亡命詩が独語小雑誌で冷戦的証言として流通する回路。", "中欧"),
    ("ユーゴ内戦証言文学の仏語抄訳", "French abridged translations of Yugoslav war testimony", "war testimony", "証言文学が仏語抄訳で人権言説に接続される編集訳。", "バルカン"),
    ("台湾白色テロ獄中詩の英訳パラテクスト", "English paratexts of White Terror prison poetry", "prison poetry", "獄中詩英訳の序文・注が政治記憶を方向づける形式。", "東アジア"),
    ("エリトリア独立詩のティグリニャ英訳", "Tigrinya-English translations of Eritrean liberation poetry", "liberation poetry", "解放闘争詩が英訳で亡命共同体の記憶媒体となる。", "アフリカ"),
    ("クルド語地下詩集のトルコ語偽装訳", "Disguised Turkish translations of Kurdish underground poetry", "Kurdish poetry", "クルド語詩が検閲回避のためトルコ語訳名義で流通する。", "西アジア"),
    ("チカーノ小出版社の二言語詩編集", "Bilingual poetry editing in Chicano small presses", "Chicano poetry", "英西二言語詩を小出版社が運動的に編集・翻訳する場。", "北米"),

    # Cluster 5: theoretical and digital micro-debates
    ("有生性階層の翻訳損失", "Animacy hierarchy loss in translation", "animacy hierarchy", "有生性を文法化する言語の関係性が訳文で平坦化する問題。", "理論"),
    ("証拠性接辞の訳注化", "Evidential suffix annotation in translation", "evidential suffixes", "伝聞・推量を示す接辞を訳注で補うか本文化するかの論点。", "理論"),
    ("敬語シフトの時系列アライメント", "Temporal alignment of honorific shifts", "honorific shifts", "会話内の敬語変化を訳文で同じ時点に置けるかの分析。", "理論"),
    ("多字体固有名の翻字揺れ", "Variant transliteration of multi-script proper names", "proper names", "複数文字圏を渡る固有名の綴り揺れが索引性を乱す問題。", "理論"),
    ("OCR汚染コーパスの訳文文体歪み", "Style distortion from OCR-contaminated translation corpora", "OCR noise", "OCR誤りを含む対訳データが訳文文体を歪める現象。", "デジタル"),
    ("低資源詩翻訳の参照訳過学習", "Reference overfitting in low-resource poetry MT", "reference overfitting", "少数参照訳への過適合が詩の別解を過小評価する問題。", "デジタル"),
]


def main():
    with LitDB(DB) as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=23"
        ).fetchone()[0]
        existing = {row["name_ja"] for row in db.conn.execute("SELECT name_ja FROM concepts")}

        if len(CONCEPTS) != 30:
            raise SystemExit(f"expected 30 concepts, got {len(CONCEPTS)}")

        seen = set()
        for name_ja, _, _, definition, _ in CONCEPTS:
            if name_ja in seen:
                raise SystemExit(f"duplicate in script: {name_ja}")
            seen.add(name_ja)
            if name_ja in existing:
                raise SystemExit(f"duplicate in DB: {name_ja}")
            if len(definition) > 100:
                raise SystemExit(f"definition too long: {name_ja} ({len(definition)})")

        for name_ja, name_en, name_original, definition, region in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                subfield_code=SUBFIELD,
                region=region,
                period_id=None,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )

        db.conn.commit()
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=23"
        ).fetchone()[0]
        print(f"Inserted {after - before}; total {after}")


if __name__ == "__main__":
    main()
