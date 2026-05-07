from lit_db_helper import LitDB


SUBFIELD = "lit_persian_turkish"
REGION = "西アジア"


CONCEPTS = [
    # 1. Caspian and Iranian minor-language lyric traditions
    {
        "name_ja": "マーザンダラーニー・アミーリー詩",
        "name_en": "Mazandarani Amiri verse",
        "definition": "タバリー系方言で伝わる即興叙情詩型。",
        "period_id": 51,
    },
    {
        "name_ja": "ギーラキー・ドゥベイティー詠唱",
        "name_en": "Gilaki do-bayti singing",
        "definition": "ギーラーン方言四行詩の口承歌唱。",
        "period_id": 51,
    },
    {
        "name_ja": "ターリシュ語デフトル歌謡",
        "name_en": "Talysh daftar songs",
        "definition": "ターリシュ語宗教歌を手控え帳で伝える伝統。",
        "period_id": 51,
    },
    {
        "name_ja": "ラーズィー方言ファフラヴィーヤート",
        "name_en": "Razi dialect fahlaviyyat",
        "definition": "レイ周辺方言で残る古層抒情詩群。",
        "period_id": 47,
    },
    {
        "name_ja": "タバリー語マルズバーン写本層",
        "name_en": "Tabari Marzban manuscript layer",
        "definition": "タバリー語寓話写本に残る地方語散文層。",
        "period_id": 141,
    },
    {
        "name_ja": "シーラーズ系ユダヤ・ペルシア詩",
        "name_en": "Shirazi Judeo-Persian verse",
        "definition": "ヘブライ文字で写されたシーラーズ系ペルシア詩。",
        "period_id": 48,
    },
    # 2. Persian manuscript micro-practices
    {
        "name_ja": "バヤーズ手控え詩帖",
        "name_en": "Bayaz poetry notebook",
        "definition": "読者が抜粋詩を集めた私的横長詩帖。",
        "period_id": 48,
    },
    {
        "name_ja": "ジョング雑纂詩集",
        "name_en": "Jong miscellany",
        "definition": "船形判に詩歌・書簡・謎を混載する写本。",
        "period_id": 48,
    },
    {
        "name_ja": "サフィーナ詩華写本",
        "name_en": "Safina anthology manuscript",
        "definition": "舟名を持つ小型詩華集写本の編集形式。",
        "period_id": 48,
    },
    {
        "name_ja": "ファール・ハーフェズ余白注記",
        "name_en": "Fal-e Hafez marginalia",
        "definition": "ハーフェズ占いで読者が残した吉凶注記。",
        "period_id": 51,
    },
    {
        "name_ja": "ムラッカア詩画アルバム",
        "name_en": "Muraqqa poetry album",
        "definition": "書画断片と詩句を貼り込む宮廷アルバム。",
        "period_id": 48,
    },
    {
        "name_ja": "タズキラ欄外補筆伝統",
        "name_en": "Tazkira marginal additions",
        "definition": "詩人列伝写本の余白に小伝を増補する慣行。",
        "period_id": 48,
    },
    # 3. Ottoman sub-genres and lodge literature
    {
        "name_ja": "メナークブナーメ聖者伝",
        "name_en": "Menakibname hagiography",
        "definition": "オスマン修道会聖者の奇跡譚を集める散文。",
        "period_id": 49,
    },
    {
        "name_ja": "フトゥッヴェトナーメ職人倫理書",
        "name_en": "Futuvvetname guild ethics",
        "definition": "職人結社の作法を韻文散文で説く教訓書。",
        "period_id": 49,
    },
    {
        "name_ja": "ヴィラーヤトナーメ・ベクタシュ",
        "name_en": "Vilayetname of Haci Bektas",
        "definition": "ハジュ・ベクタシュ伝説を語るベクタシ聖者伝。",
        "period_id": 251,
    },
    {
        "name_ja": "デスタン・イ・ゲイクリ・ババ",
        "name_en": "Destan of Geyikli Baba",
        "definition": "鹿を伴う聖者を歌う初期オスマン伝説詩。",
        "period_id": 251,
    },
    {
        "name_ja": "地方メヴリド写本",
        "name_en": "Provincial mevlid manuscripts",
        "definition": "預言者生誕詩を地方発音で写す写本群。",
        "period_id": 49,
    },
    {
        "name_ja": "マクトゥル・イ・ヒュセイン哀悼詩",
        "name_en": "Maktul-i Huseyin elegy",
        "definition": "カルバラー殉難をトルコ語で悼む長詩群。",
        "period_id": 49,
    },
    # 4. Chagatai, Khwarezmian, and Kipchak textual niches
    {
        "name_ja": "ホラズム『ムハッバトナーメ』写本",
        "name_en": "Khwarazmian Muhabbatname manuscripts",
        "definition": "ホラズム・トルコ語恋愛書簡詩の写本伝承。",
        "period_id": 48,
    },
    {
        "name_ja": "クトゥブ版『ホスローとシーリーン』",
        "name_en": "Qutb's Khusraw u Shirin",
        "definition": "ニザーミー物語をキプチャク語へ移した宮廷詩。",
        "period_id": 48,
    },
    {
        "name_ja": "サイフィ・サライ版『グリスタン』",
        "name_en": "Sayfi Sarayi Gulistan translation",
        "definition": "サアディー散文をキプチャク語で翻案した作品。",
        "period_id": 48,
    },
    {
        "name_ja": "『アタベトゥル・ハカイク』写本系統",
        "name_en": "Atabetul Hakayik manuscript families",
        "definition": "カラハン朝教訓詩の異本分岐をめぐる系統。",
        "period_id": 47,
    },
    {
        "name_ja": "東トルキ『キサス・アルアンビヤー』",
        "name_en": "Eastern Turkic Qisas al-Anbiya",
        "definition": "預言者物語を東トルキ語で語る写本群。",
        "period_id": 48,
    },
    {
        "name_ja": "チャガタイ・ムアンマ詩謎",
        "name_en": "Chagatai muamma riddles",
        "definition": "文字計算で名を隠すチャガタイ語謎詩。",
        "period_id": 48,
    },
    # 5. Kurdish, Pashto, Balochi, and Sindhi micro-traditions
    {
        "name_ja": "ザザキ語デーワーン断片",
        "name_en": "Zazaki divan fragments",
        "definition": "ザザキ語で写された少数派クルド詩断片。",
        "period_id": 252,
    },
    {
        "name_ja": "ソラニー・ナーリ詩派",
        "name_en": "Sorani Nali school",
        "definition": "ナーリ周辺で成立したソラニー抒情詩の小圏。",
        "period_id": 252,
    },
    {
        "name_ja": "パシュトー・チャルベイタ民謡",
        "name_en": "Pashto charbeta songs",
        "definition": "四分割構成で歌われるパシュトー長民謡。",
        "period_id": 252,
    },
    {
        "name_ja": "バローチ・ドムキー叙事歌",
        "name_en": "Balochi Domki epic songs",
        "definition": "ドムキー系吟遊が伝える部族英雄歌。",
        "period_id": 252,
    },
    {
        "name_ja": "スィンディー・ベイト韻律論",
        "name_en": "Sindhi bait prosody",
        "definition": "ビッタイ詩を支える短詩ベイトの韻律規則。",
        "period_id": 252,
    },
    {
        "name_ja": "ゴーラーン語カラム写本",
        "name_en": "Gorani kalam manuscripts",
        "definition": "ヤールサーン聖歌をゴーラーン語で写す写本。",
        "period_id": 252,
    },
]


def main() -> None:
    assert len(CONCEPTS) == 30
    with LitDB("lit.sqlite") as db:
        for concept in CONCEPTS:
            assert len(concept["definition"]) <= 100, concept["name_ja"]
            db.insert_concept(
                subfield_code=SUBFIELD,
                region=REGION,
                importance_score=2,
                **concept,
            )


if __name__ == "__main__":
    main()
