"""Wave 41: add 30 hyper-niche concepts to lit_india."""

from lit_db_helper import LitDB

SUBFIELD = "lit_india"
REGION = "南アジア"


CONCEPTS = [
    # Himalayan and northeastern minor oral/manuscript traditions
    {
        "name_ja": "リンブー語ムンドゥム口誦",
        "name_en": "Limbu Mundhum oral recitation",
        "name_original": "Mundhum",
        "original_script": "limbu",
        "period_id": 138,
        "definition": "リンブーの宇宙論と祖先譚を伝える祭儀的口誦群。",
    },
    {
        "name_ja": "ガロ・カッタ叙事歌",
        "name_en": "Garo katta epic song",
        "name_original": "katta",
        "original_script": "roman",
        "period_id": 138,
        "definition": "ガロ社会で英雄譚や移住記憶を歌う長篇口承歌。",
    },
    {
        "name_ja": "ディマサ・ハチャリ歌謡",
        "name_en": "Dimasa Hachari songs",
        "name_original": "Hachari",
        "original_script": "roman",
        "period_id": 138,
        "definition": "ディマサの儀礼と氏族記憶を結ぶ短詩的歌謡。",
    },
    {
        "name_ja": "ミシン・オイニトム恋歌",
        "name_en": "Mising Oinitom love songs",
        "name_original": "Oinitom",
        "original_script": "roman",
        "period_id": 138,
        "definition": "アッサムのミシン人に伝わる掛け合い型恋愛歌。",
    },
    {
        "name_ja": "ボド・バガルンバ歌詞",
        "name_en": "Bodo Bagurumba lyrics",
        "name_original": "Bagurumba",
        "original_script": "devanagari",
        "period_id": 138,
        "definition": "ボドの蝶舞踊に伴う季節儀礼の歌詞群。",
    },
    {
        "name_ja": "ネパール・バンサーワリー写本",
        "name_en": "Nepalese vamsavali manuscripts",
        "name_original": "vaṃśāvalī",
        "original_script": "devanagari",
        "period_id": 138,
        "definition": "王統と聖地由来を記すネパール系年代記写本。",
    },
    # Kashmiri, Sindhi, and Punjabi micro-genres
    {
        "name_ja": "ヌンド・リシ『シュルク』",
        "name_en": "Nund Rishi shruks",
        "name_original": "śrukh",
        "original_script": "sharada",
        "period_id": 267,
        "definition": "カシミールのリシ聖者が残した短い教訓詩。",
    },
    {
        "name_ja": "ハッバ・ハートゥーン『ロル』",
        "name_en": "Habba Khatun lol songs",
        "name_original": "lol",
        "original_script": "sharada",
        "period_id": 267,
        "definition": "カシミール女性詩人に帰される抒情的恋歌形式。",
    },
    {
        "name_ja": "スィンディー・カーフィー",
        "name_en": "Sindhi kafi",
        "name_original": "kafi",
        "original_script": "arabic",
        "period_id": 267,
        "definition": "スーフィー思想を民謡旋律で歌うスィンディー詩型。",
    },
    {
        "name_ja": "『シャー・ジョー・リサーロ』異本",
        "name_en": "Shah Jo Risalo recensions",
        "name_original": "Shah Jo Risalo",
        "original_script": "arabic",
        "period_id": 267,
        "definition": "シャー・ラティーフ詩集の写本・口承差を示す諸本。",
    },
    {
        "name_ja": "パンジャーブ語ヴァール詩",
        "name_en": "Punjabi vaar poetry",
        "name_original": "vaar",
        "original_script": "gurmukhi",
        "period_id": 266,
        "definition": "戦闘や聖者行状を語るパンジャーブ語英雄歌。",
    },
    {
        "name_ja": "ワーリス・シャー『ヒール』諸本",
        "name_en": "Waris Shah Heer recensions",
        "name_original": "Hir",
        "original_script": "gurmukhi",
        "period_id": 267,
        "definition": "恋愛キッサ『ヒール』の写本・印刷本の異本群。",
    },
    # Dravidian subgenre variants and performance texts
    {
        "name_ja": "マラヤーラム・ヴァダッカンパットゥ",
        "name_en": "Malayalam Vadakkan Pattukal",
        "name_original": "Vadakkan Pattukal",
        "original_script": "malayalam",
        "period_id": 243,
        "definition": "北ケーララの武芸氏族を歌う英雄バラッド群。",
    },
    {
        "name_ja": "クンチャン・ナンビヤール『トゥッラル』",
        "name_en": "Kunchan Nambiar Tullal",
        "name_original": "Tullal",
        "original_script": "malayalam",
        "period_id": 243,
        "definition": "風刺と舞踊を結ぶマラヤーラム語劇詩形式。",
    },
    {
        "name_ja": "マッピラ・パットゥ歌本",
        "name_en": "Mappila pattu songbooks",
        "name_original": "Mappila pattu",
        "original_script": "arabic_malayalam",
        "period_id": 243,
        "definition": "アラビ・マラヤーラムで流通したムスリム歌謡本。",
    },
    {
        "name_ja": "タミル・パッル詩",
        "name_en": "Tamil pallu poetry",
        "name_original": "pallu",
        "original_script": "tamil",
        "period_id": 237,
        "definition": "農夫像を風刺的に描く近世タミル小詩型。",
    },
    {
        "name_ja": "タミル・クラヴァンジ劇",
        "name_en": "Tamil kuravanji drama",
        "name_original": "kuravanji",
        "original_script": "tamil",
        "period_id": 237,
        "definition": "占い女と恋慕を軸にしたタミル舞踊劇形式。",
    },
    {
        "name_ja": "テルグ・シャタカム詩",
        "name_en": "Telugu satakam poetry",
        "name_original": "śatakam",
        "original_script": "telugu",
        "period_id": 137,
        "definition": "百詩前後の連作で倫理や信仰を述べる詩型。",
    },
    # Jain, Buddhist, and scholastic manuscript niches
    {
        "name_ja": "ジャイナ・ニルユクティ注釈",
        "name_en": "Jain niryukti commentaries",
        "name_original": "niryukti",
        "original_script": "prakrit",
        "period_id": 265,
        "definition": "聖典語句を韻文で解くジャイナ最古層注釈。",
    },
    {
        "name_ja": "アーヴァシュヤカ・チュールニ",
        "name_en": "Avasyaka curni",
        "name_original": "Āvaśyaka-cūrṇi",
        "original_script": "prakrit",
        "period_id": 265,
        "definition": "ジャイナ日課聖典を散文で詳解する注釈伝統。",
    },
    {
        "name_ja": "ネワール仏教チャチャー歌",
        "name_en": "Newar Buddhist caca songs",
        "name_original": "caca",
        "original_script": "newa",
        "period_id": 264,
        "definition": "儀礼舞踊と結びつくネワール密教の歌謡。",
    },
    {
        "name_ja": "ネパール・アヴァダーナ写本",
        "name_en": "Nepalese avadana manuscripts",
        "name_original": "avadāna",
        "original_script": "sanskrit",
        "period_id": 264,
        "definition": "功徳譚を集めたネパール伝来サンスクリット写本。",
    },
    {
        "name_ja": "アヴァダーナシャタカ伝本",
        "name_en": "Avadanasataka recensions",
        "name_original": "Avadānaśataka",
        "original_script": "sanskrit",
        "period_id": 264,
        "definition": "百話構成の仏教功徳譚集に残る伝本差。",
    },
    {
        "name_ja": "プラークリット・ガーター注疏",
        "name_en": "Prakrit gatha glosses",
        "name_original": "gāthā",
        "original_script": "prakrit",
        "period_id": 265,
        "definition": "短詩ガーターを語釈する僧院系注疏の伝統。",
    },
    # Classical poetics micro-debates
    {
        "name_ja": "サーデャ・ラサ論",
        "name_en": "Sadhya rasa debate",
        "name_original": "sādhya rasa",
        "original_script": "sanskrit",
        "period_id": 236,
        "definition": "ラサを到達対象と見る詩論上の微細な立場。",
    },
    {
        "name_ja": "ボージャ『シュリンガーラ・プラカーシャ』",
        "name_en": "Bhoja's Srngara Prakasa",
        "name_original": "Śṛṅgāra-prakāśa",
        "original_script": "sanskrit",
        "period_id": 236,
        "definition": "恋愛ラサ中心に演劇と詩を統合する大部詩論。",
    },
    {
        "name_ja": "クシェーメーンドラ『カヴィカンターバラナ』",
        "name_en": "Ksemendra's Kavikanthabharana",
        "name_original": "Kavikaṇṭhābharaṇa",
        "original_script": "sanskrit",
        "period_id": 236,
        "definition": "詩人修練の欠点と技巧を列挙するカシミール詩論。",
    },
    {
        "name_ja": "プラティーバー詩才論",
        "name_en": "Pratibha theory of poetic genius",
        "name_original": "pratibhā",
        "original_script": "sanskrit",
        "period_id": 236,
        "definition": "詩作能力を天賦の閃きとして論じる詩学概念。",
    },
    {
        "name_ja": "サハリダヤ受容論",
        "name_en": "Sahrdaya reception theory",
        "name_original": "sahṛdaya",
        "original_script": "sanskrit",
        "period_id": 236,
        "definition": "理想的鑑賞者の感受性を問うサンスクリット詩論。",
    },
    {
        "name_ja": "ラサ・ニシュパッティ論争",
        "name_en": "Rasa nispatti debate",
        "name_original": "rasa-niṣpatti",
        "original_script": "sanskrit",
        "period_id": 236,
        "definition": "ラサが発生か推認か顕現かをめぐる解釈論争。",
    },
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id=12"
            ).fetchall()
        }
        dupes = [concept["name_ja"] for concept in CONCEPTS if concept["name_ja"] in existing]
        if dupes:
            raise SystemExit(f"duplicates in lit_india: {dupes}")

        for concept in CONCEPTS:
            if len(concept["definition"]) > 100:
                raise ValueError(f"definition too long: {concept['name_ja']}")
            db.insert_concept(
                **concept,
                subfield_code=SUBFIELD,
                region=REGION,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )

        print(f"added={len(CONCEPTS)}")


if __name__ == "__main__":
    main()
