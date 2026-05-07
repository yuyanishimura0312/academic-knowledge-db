#!/usr/bin/env python3
"""Wave 38 C02: lit_eu_medieval extra niche concepts (30) - 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD = "lit_eu_medieval"
REGION = "西欧"

P_LATIN = 219
P_EARLY = 110
P_GERMAN_LATE = 119
P_FR = 213
P_LATE = 114
P_ES = 215

CONCEPTS = [
    # 1: ラテン中世詩
    {
        "name_ja": "フゴ・プリマス詩群",
        "name_en": "Hugo Primas poems",
        "name_original": "Carmina Hugonis Primas",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "12世紀オルレアンの放浪学僧詩人による風刺的ラテン語詩群。",
    },
    {
        "name_ja": "シャティヨン『アレクサンドレイス』",
        "name_en": "Walter of Chatillon Alexandreis",
        "name_original": "Alexandreis",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "アレクサンドロス大王伝を古典叙事詩風に再構成した12世紀ラテン叙事詩。",
    },
    {
        "name_ja": "アラヌス『アンティクラウディアヌス』",
        "name_en": "Alanus Anticlaudianus",
        "name_original": "Anticlaudianus",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "完全人の創造を寓意的に描くアラヌス・アブ・インスリスのラテン詩。",
    },
    {
        "name_ja": "ベルナルドゥス『コスモグラフィア』",
        "name_en": "Bernardus Silvestris Cosmographia",
        "name_original": "Cosmographia",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "宇宙生成を女神的寓意で語るベルナルドゥス・シルウェストリスの韻散文作。",
    },
    {
        "name_ja": "ゴーティエ・ド・シャティヨン詩集",
        "name_en": "Gautier de Chatillon Carmina",
        "name_original": "Carmina",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "宮廷・教会・学僧文化を横断するゴーティエのラテン語抒情詩集。",
    },
    {
        "name_ja": "ジョゼフ・オブ・エクセター『ユリアドス』",
        "name_en": "Joseph of Exeter Yliados",
        "name_original": "Ylias Daretis Phrygii",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "ダレス偽史に基づきトロイア戦争を語る12世紀末ラテン叙事詩。",
    },
    # 2: 古英語以外古ゲルマン
    {
        "name_ja": "古ザクセン語『ヘーリアント』",
        "name_en": "Old Saxon Heliand",
        "name_original": "Heliand",
        "original_script": "latin",
        "period_id": P_EARLY,
        "definition": "福音書物語をゲルマン英雄詩の語法で翻案した古ザクセン語叙事詩。",
    },
    {
        "name_ja": "オトフリート『福音書』",
        "name_en": "Otfrid Evangelienbuch",
        "name_original": "Evangelienbuch",
        "original_script": "latin",
        "period_id": P_EARLY,
        "definition": "福音書調和を脚韻詩で綴ったオトフリートの古高ドイツ語作品。",
    },
    {
        "name_ja": "古高ドイツ語『ヒルデブラントの歌』",
        "name_en": "Old High German Hildebrandslied",
        "name_original": "Hildebrandslied",
        "original_script": "latin",
        "period_id": P_EARLY,
        "definition": "父子対決を断片で伝える古高ドイツ語英雄詩、頭韻詩法の遺例。",
    },
    {
        "name_ja": "ムールバッハ賛歌",
        "name_en": "Murbach Hymns",
        "name_original": "Murbacher Hymnen",
        "original_script": "latin",
        "period_id": P_EARLY,
        "definition": "ラテン賛歌への古高ドイツ語逐語訳を含む初期修道院詩資料。",
    },
    {
        "name_ja": "古フリジア語第一リウストリンゲン写本",
        "name_en": "Old Frisian First Riustringen Codex",
        "name_original": "First Riustringen Codex",
        "original_script": "latin",
        "period_id": P_GERMAN_LATE,
        "definition": "古フリジア語法文と韻文を収めるリウストリンゲン伝承の主要写本。",
    },
    {
        "name_ja": "古ザクセン語『創世記』",
        "name_en": "Old Saxon Genesis",
        "name_original": "Genesis",
        "original_script": "latin",
        "period_id": P_EARLY,
        "definition": "聖書創世記を古ザクセン語頭韻詩で語る断片的キリスト教叙事詩。",
    },
    # 3: 中世仏抒情・寓意
    {
        "name_ja": "ギヨーム・ド・ロリス『薔薇物語』",
        "name_en": "Guillaume de Lorris Roman de la Rose",
        "name_original": "Roman de la Rose",
        "original_script": "latin",
        "period_id": P_FR,
        "definition": "恋愛の夢幻探索を宮廷的寓意で描く『薔薇物語』前半部。",
    },
    {
        "name_ja": "ジャン・ド・マン『薔薇物語』続編",
        "name_en": "Jean de Meun Roman de la Rose continuation",
        "name_original": "Roman de la Rose continuation",
        "original_script": "latin",
        "period_id": P_FR,
        "definition": "百科全書的諷刺と自然哲学を拡張した『薔薇物語』後半部。",
    },
    {
        "name_ja": "リュトブフ詩群",
        "name_en": "Rutebeuf poems",
        "name_original": "Poemes de Rutebeuf",
        "original_script": "latin",
        "period_id": P_FR,
        "definition": "貧困・宗教・時事を鋭く歌う13世紀パリ詩人リュトブフの詩群。",
    },
    {
        "name_ja": "マショー『真実の物語』",
        "name_en": "Guillaume de Machaut Voir Dit",
        "name_original": "Le Voir Dit",
        "original_script": "latin",
        "period_id": P_LATE,
        "definition": "恋文と抒情詩を散文物語に編み込むマショー晩年の恋愛作品。",
    },
    {
        "name_ja": "ユスターシュ・デシャン『バラード集』",
        "name_en": "Eustache Deschamps Balades",
        "name_original": "Balades",
        "original_script": "latin",
        "period_id": P_LATE,
        "definition": "政治・道徳・日常を定型詩で扱うデシャンの大規模バラード群。",
    },
    {
        "name_ja": "クリスティーヌ『女たちの都』",
        "name_en": "Christine de Pizan Cite des Dames",
        "name_original": "Le Livre de la Cite des Dames",
        "original_script": "latin",
        "period_id": P_LATE,
        "definition": "女性の徳と知を寓意都市に集めるクリスティーヌ・ド・ピザンの擁護論。",
    },
    # 4: 中世英文学
    {
        "name_ja": "パール詩人『真珠』",
        "name_en": "Pearl Poet Pearl",
        "name_original": "Pearl",
        "original_script": "latin",
        "period_id": P_LATE,
        "definition": "夢幻形式で喪失と救済を精緻な頭韻韻律に結ぶ中英語宗教詩。",
    },
    {
        "name_ja": "『ガウェイン卿と緑の騎士』",
        "name_en": "Sir Gawain and the Green Knight",
        "name_original": "Sir Gawain and the Green Knight",
        "original_script": "latin",
        "period_id": P_LATE,
        "definition": "斬首試合と誘惑試練を通じ騎士道倫理を問う中英語頭韻ロマンス。",
    },
    {
        "name_ja": "パール詩人『清浄』",
        "name_en": "Cleanness",
        "name_original": "Cleanness",
        "original_script": "latin",
        "period_id": P_LATE,
        "definition": "聖書説話で純潔と穢れを説くパール詩人圏の中英語頭韻詩。",
    },
    {
        "name_ja": "パール詩人『忍耐』",
        "name_en": "Patience",
        "name_original": "Patience",
        "original_script": "latin",
        "period_id": P_LATE,
        "definition": "ヨナ書を素材に忍耐の徳を説く短い中英語頭韻宗教詩。",
    },
    {
        "name_ja": "ラングランド『農夫ピアズ』Bテキスト",
        "name_en": "Piers Plowman B-text",
        "name_original": "Piers Plowman B-text",
        "original_script": "latin",
        "period_id": P_LATE,
        "definition": "社会批判と救済探求を夢幻で連ねるラングランド『農夫ピアズ』主要版。",
    },
    {
        "name_ja": "ガワー『恋する者の告解』",
        "name_en": "Gower Confessio Amantis",
        "name_original": "Confessio Amantis",
        "original_script": "latin",
        "period_id": P_LATE,
        "definition": "恋愛告解の枠で古今説話を集成するジョン・ガワーの中英語長詩。",
    },
    # 5: スペイン中世
    {
        "name_ja": "『わがシッドの歌』ペロ・アバット写本",
        "name_en": "Cantar de Mio Cid",
        "name_original": "Cantar de mio Cid",
        "original_script": "latin",
        "period_id": P_ES,
        "definition": "ペロ・アバット写本で伝わる『わがシッドの歌』本文伝承の中核。",
    },
    {
        "name_ja": "『良き愛の書』クアデルナ・ビア",
        "name_en": "Libro de Buen Amor",
        "name_original": "Libro de buen amor",
        "original_script": "latin",
        "period_id": P_ES,
        "definition": "『良き愛の書』で聖俗恋愛を支える四行定型詩クアデルナ・ビア。",
    },
    {
        "name_ja": "『東方三博士劇』",
        "name_en": "Auto de los Reyes Magos",
        "name_original": "Auto de los Reyes Magos",
        "original_script": "latin",
        "period_id": P_ES,
        "definition": "東方三博士の礼拝を扱う初期カスティーリャ語宗教劇断片。",
    },
    {
        "name_ja": "『愛の理』",
        "name_en": "Razon de amor",
        "name_original": "Razon de amor",
        "original_script": "latin",
        "period_id": P_ES,
        "definition": "恋愛対話と水酒論争を結ぶ13世紀カスティーリャ語抒情物語。",
    },
    {
        "name_ja": "マンリケ『父の死に寄せる詩』",
        "name_en": "Jorge Manrique Coplas",
        "name_original": "Coplas por la muerte de su padre",
        "original_script": "latin",
        "period_id": P_ES,
        "definition": "無常観と名誉記憶を結ぶホルヘ・マンリケの哀悼詩。",
    },
    {
        "name_ja": "ベルセオ『聖ミリャン伝』",
        "name_en": "Berceo Vida de San Millan",
        "name_original": "Vida de San Millan de la Cogolla",
        "original_script": "latin",
        "period_id": P_ES,
        "definition": "メステル・デ・クレレシーア詩法で聖ミリャンの生涯を語るベルセオ作品。",
    },
]


def main() -> None:
    assert len(CONCEPTS) == 30
    for entry in CONCEPTS:
        assert len(entry["definition"]) <= 100, entry["name_ja"]

    inserted = 0
    with LitDB() as db:
        for entry in CONCEPTS:
            cid = db.insert_concept(
                subfield_code=SUBFIELD,
                region=REGION,
                importance_score=3,
                source_tier="primary",
                canonical_in_region="minor",
                **entry,
            )
            inserted += 1
            print(f"{inserted:02d}. {entry['name_ja']} -> {cid}")
    print(f"done: {inserted}/30")


if __name__ == "__main__":
    main()
