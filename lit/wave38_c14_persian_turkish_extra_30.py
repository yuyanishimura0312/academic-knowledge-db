#!/usr/bin/env python3
"""Wave 38: add 30 extra niche concepts to lit_persian_turkish."""

from lit_db_helper import LitDB

DB_PATH = "lit.sqlite"
SUBFIELD = "lit_persian_turkish"

P_CLASSIC_EARLY = 46
P_CLASSIC_MID = 47
P_CLASSIC_LATE = 48
P_MODERN = 51

CONCEPTS = [
    # Cluster 1: ペルシア叙事詩細部
    {
        "name_ja": "『ガルシャースプ・ナーマ』竜退治挿話",
        "name_en": "Garshasp-nama dragon-slaying episode",
        "name_original": "گرشاسپ‌نامه",
        "original_script": "arabic",
        "region": "西アジア",
        "period_id": P_CLASSIC_EARLY,
        "definition": "アサディー叙事詩で英雄の怪物退治を示す武勇場面。",
    },
    {
        "name_ja": "グルガーニー『ヴィースとラーミーン』恋文",
        "name_en": "Gorgani Vis and Ramin love letters",
        "name_original": "ویس و رامین",
        "original_script": "arabic",
        "region": "西アジア",
        "period_id": P_CLASSIC_MID,
        "definition": "恋人間の書簡が情念と策略を進めるロマンス技法。",
    },
    {
        "name_ja": "ニザーミー『ホスローとシーリーン』水浴場面",
        "name_en": "Nizami Khusrow and Shirin bathing scene",
        "name_original": "خسرو و شیرین",
        "original_script": "arabic",
        "region": "西アジア",
        "period_id": P_CLASSIC_MID,
        "definition": "シーリーンの身体像と視線をめぐる有名な恋愛叙景。",
    },
    {
        "name_ja": "ニザーミー『七王妃物語』黒の館",
        "name_en": "Nizami Haft Paykar black pavilion",
        "name_original": "هفت پیکر",
        "original_script": "arabic",
        "region": "西アジア",
        "period_id": P_CLASSIC_MID,
        "definition": "七色の館連作で土曜と黒が結ぶ教訓的挿話。",
    },
    {
        "name_ja": "アミール・ホスロー『八つの楽園』模倣構造",
        "name_en": "Amir Khusrow Hasht Bihisht imitative structure",
        "name_original": "هشت بهشت",
        "original_script": "arabic",
        "region": "南アジア",
        "period_id": P_CLASSIC_LATE,
        "definition": "ニザーミー型七館物語を八楽園へ改作した宮廷叙事詩構成。",
    },
    {
        "name_ja": "ジャーミー『サラーマーンとアブサール』寓意",
        "name_en": "Jami Salaman and Absal allegory",
        "name_original": "سلامان و ابسال",
        "original_script": "arabic",
        "region": "西アジア",
        "period_id": P_CLASSIC_LATE,
        "definition": "肉欲と理性の葛藤を恋愛物語に託す哲学的寓意詩。",
    },
    # Cluster 2: ペルシア神秘主義散文
    {
        "name_ja": "スフラワルディー『照明哲学』光の階梯",
        "name_en": "Suhrawardi Hikmat al-Ishraq hierarchy of light",
        "name_original": "حکمة الاشراق",
        "original_script": "arabic",
        "region": "西アジア",
        "period_id": P_CLASSIC_MID,
        "definition": "存在を光の強弱で秩序化する照明学派の中心概念。",
    },
    {
        "name_ja": "ナジュム・ラーズィー『神の僕の道程』魂の旅",
        "name_en": "Najm Razi Mirsad al-Ibad soul journey",
        "name_original": "مرصاد العباد",
        "original_script": "arabic",
        "region": "西アジア",
        "period_id": P_CLASSIC_LATE,
        "definition": "魂の下降と帰還を説く13世紀ペルシア語スーフィー散文。",
    },
    {
        "name_ja": "アズィーズ・ナサフィー『完全人間』人間論",
        "name_en": "Aziz Nasafi Insan-i Kamil anthropology",
        "name_original": "انسان کامل",
        "original_script": "arabic",
        "region": "西アジア",
        "period_id": P_CLASSIC_LATE,
        "definition": "宇宙を映す完全人間像を論じるイルハン朝期神秘主義散文。",
    },
    {
        "name_ja": "ホージャ・アブドゥッラー・アンサーリー『祈祷』",
        "name_en": "Khwaja Abdullah Ansari Munajat",
        "name_original": "مناجات",
        "original_script": "arabic",
        "region": "西アジア",
        "period_id": P_CLASSIC_EARLY,
        "definition": "短い祈りの散文で神への親密な語りを形にしたヘラート文学。",
    },
    {
        "name_ja": "マイブディー『神秘の開示』注釈層",
        "name_en": "Maybudi Kashf al-Asrar commentary layers",
        "name_original": "کشف الاسرار",
        "original_script": "arabic",
        "region": "西アジア",
        "period_id": P_CLASSIC_MID,
        "definition": "逐語・説教・神秘解釈を重ねるペルシア語クルアーン注釈。",
    },
    {
        "name_ja": "『統一の秘密』アブー・サイード聖者伝",
        "name_en": "Asrar al-Tawhid Abu Sa'id hagiography",
        "name_original": "اسرار التوحید",
        "original_script": "arabic",
        "region": "西アジア",
        "period_id": P_CLASSIC_MID,
        "definition": "アブー・サイードの逸話を集成した初期ペルシア語聖者伝。",
    },
    # Cluster 3: タジク・現代タジク
    {
        "name_ja": "アイニー『回想録』ブハラ学校批判",
        "name_en": "Sadriddin Aini Reminiscences Bukhara school critique",
        "name_original": "Ёддоштҳо",
        "original_script": "cyrillic",
        "region": "中央アジア",
        "period_id": P_MODERN,
        "definition": "旧ブハラの教育と社会を記録するタジク近代散文の核。",
    },
    {
        "name_ja": "ミルゾ・トゥルスンゾダ『詩人』",
        "name_en": "Mirzo Tursunzoda Shoir",
        "name_original": "Шоир",
        "original_script": "cyrillic",
        "region": "中央アジア",
        "period_id": P_MODERN,
        "definition": "ソ連期タジク詩で詩人の社会的使命を歌う代表的作品。",
    },
    {
        "name_ja": "ロイク・シェラリー抒情詩",
        "name_en": "Loyiq Sherali lyric poetry",
        "name_original": "Лоиқ Шералӣ",
        "original_script": "cyrillic",
        "region": "中央アジア",
        "period_id": P_MODERN,
        "definition": "母語・故郷・歴史記憶を鋭く歌う20世紀タジク抒情詩。",
    },
    {
        "name_ja": "ボゾル・ソビル亡命詩",
        "name_en": "Bozor Sobir exile poetry",
        "name_original": "Бозор Собир",
        "original_script": "cyrillic",
        "region": "中央アジア",
        "period_id": P_MODERN,
        "definition": "政治批判と亡命経験を重ねる現代タジク詩の一潮流。",
    },
    {
        "name_ja": "グルナザル・ケルディ国歌詩",
        "name_en": "Gulnazar Keldi national anthem lyric",
        "name_original": "Гулназар Келдӣ",
        "original_script": "cyrillic",
        "region": "中央アジア",
        "period_id": P_MODERN,
        "definition": "独立後タジキスタン国歌の詞で知られる詩人の国家的抒情。",
    },
    {
        "name_ja": "ファルゾナ・ホジャンディー女性抒情",
        "name_en": "Farzona Khojandi women's lyric",
        "name_original": "Фарзона",
        "original_script": "cyrillic",
        "region": "中央アジア",
        "period_id": P_MODERN,
        "definition": "女性主体と古典語彙を結ぶ現代タジク詩の重要な声。",
    },
    # Cluster 4: 中央アジア文学
    {
        "name_ja": "ナヴァーイー『ハムサ』ファルハード像",
        "name_en": "Alisher Navoi Khamsa Farhad figure",
        "name_original": "Xamsa",
        "original_script": "latin",
        "region": "中央アジア",
        "period_id": P_CLASSIC_LATE,
        "definition": "チャガタイ語五部作で労働と愛の英雄として造形された人物像。",
    },
    {
        "name_ja": "バーブル『バーブル・ナーマ』庭園描写",
        "name_en": "Babur Baburnama garden description",
        "name_original": "Bāburnāma",
        "original_script": "latin",
        "region": "中央アジア",
        "period_id": P_CLASSIC_LATE,
        "definition": "地誌・植物・造園感覚を結ぶチャガタイ語回想録の細部。",
    },
    {
        "name_ja": "マフトゥムクリ・ピラーギー詩",
        "name_en": "Magtymguly Pyragy Turkmen poetry",
        "name_original": "Magtymguly Pyragy",
        "original_script": "latin",
        "region": "中央アジア",
        "period_id": P_CLASSIC_LATE,
        "definition": "トルクメン民族意識と倫理を歌う18世紀詩人の作品群。",
    },
    {
        "name_ja": "ノディラ女性詩人ディーワーン",
        "name_en": "Nodira Uzbek female poet diwan",
        "name_original": "Nodira",
        "original_script": "latin",
        "region": "中央アジア",
        "period_id": P_CLASSIC_LATE,
        "definition": "コーカンド宮廷で女性の声を刻んだウズベク古典詩集。",
    },
    {
        "name_ja": "マクスート・アタイ チュヴァシ文学",
        "name_en": "Maqsut Atai Chuvash literature",
        "name_original": "Maqsut Atai",
        "original_script": "latin",
        "region": "中央アジア",
        "period_id": P_MODERN,
        "definition": "チュヴァシ語近代文学に連なるトルコ系少数言語文学の論点。",
    },
    {
        "name_ja": "マグジャン・ジュマバエフ象徴主義詩",
        "name_en": "Magjan Zhumabayev Kazakh symbolist poetry",
        "name_original": "Мағжан Жұмабаев",
        "original_script": "cyrillic",
        "region": "中央アジア",
        "period_id": P_MODERN,
        "definition": "カザフ近代詩で民族感情と象徴主義を結合した抒情。",
    },
    # Cluster 5: 現代トルコ女性
    {
        "name_ja": "ハリデ・エディプ『シネクリ・バッカル』",
        "name_en": "Halide Edib Adivar Sinekli Bakkal",
        "name_original": "Sinekli Bakkal",
        "original_script": "latin",
        "region": "西アジア",
        "period_id": P_MODERN,
        "definition": "旧市街の女性歌手を通じて近代化と伝統を問う長編小説。",
    },
    {
        "name_ja": "アダレット・アーオール『死に横たわる』",
        "name_en": "Adalet Agaoglu Olmeye Yatmak",
        "name_original": "Ölmeye Yatmak",
        "original_script": "latin",
        "region": "西アジア",
        "period_id": P_MODERN,
        "definition": "共和国女性知識人の記憶と身体を交錯させる実験小説。",
    },
    {
        "name_ja": "ラティフェ・テキン『愛しい恥知らずの死』",
        "name_en": "Latife Tekin Sevgili Arsiz Olum",
        "name_original": "Sevgili Arsız Ölüm",
        "original_script": "latin",
        "region": "西アジア",
        "period_id": P_MODERN,
        "definition": "村落口承と都市移住を魔術的リアリズムで結ぶトルコ小説。",
    },
    {
        "name_ja": "テゼル・オズリュ『幼年の寒い夜』",
        "name_en": "Tezer Ozlu Cocuklugun Soguk Geceleri",
        "name_original": "Çocukluğun Soğuk Geceleri",
        "original_script": "latin",
        "region": "西アジア",
        "period_id": P_MODERN,
        "definition": "精神病院・家族・女性身体を断片的に描く自伝的小説。",
    },
    {
        "name_ja": "ナズル・エライ『通りすがりの者』",
        "name_en": "Nazli Eray Yoldan Gecen",
        "name_original": "Yoldan Geçen",
        "original_script": "latin",
        "region": "西アジア",
        "period_id": P_MODERN,
        "definition": "日常と幻想の境界を滑らせる現代トルコ女性作家の短編世界。",
    },
    {
        "name_ja": "アスル・エルドアン『奇跡のマンダリン』",
        "name_en": "Asli Erdogan Mucizevi Mandarin",
        "name_original": "Mucizevi Mandarin",
        "original_script": "latin",
        "region": "西アジア",
        "period_id": P_MODERN,
        "definition": "亡命感覚と都市の孤独を凝縮する初期短編小説集。",
    },
]


def main() -> None:
    inserted = 0
    skipped = 0
    with LitDB(DB_PATH) as db:
        for entry in CONCEPTS:
            if len(entry["definition"]) > 100:
                raise ValueError(f"definition too long: {entry['name_ja']}")
            cid = db.insert_concept(
                **entry,
                subfield_code=SUBFIELD,
                importance_score=3,
                fourth_transform_status="partial",
                fourth_transform_note="周縁化された細部の再読対象。",
                source_tier="secondary",
                canonical_in_region="minor",
            )
            if cid:
                inserted += 1
    print(f"Inserted or existing: {inserted}, skipped: {skipped}")


if __name__ == "__main__":
    main()
