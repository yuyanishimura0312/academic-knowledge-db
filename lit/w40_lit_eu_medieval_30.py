from lit_db_helper import LitDB


SUBFIELD = "lit_eu_medieval"
REGION = "西欧"

P_LATIN = 219
P_FR = 213
P_OCC = 214
P_EN = 115
P_GER = 216
P_NORTH = 218
P_IB = 215
P_LATE = 114


CONCEPTS = [
    # 1. 中世ラテン小品・韻律叙事
    {
        "name_ja": "『ワルターリウス』",
        "name_en": "Waltharius",
        "name_original": "Waltharius",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "ヘクサメトロスでワルテル伝承を語る中世ラテン英雄叙事詩。",
    },
    {
        "name_ja": "『モデナの見張り歌』",
        "name_en": "Modena Watchmen's Song",
        "name_original": "O tu qui servas armis ista moenia",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "城壁見張りの掛け声を詩化したカロリング期ラテン小詩。",
    },
    {
        "name_ja": "『ケンブリッジ歌集』",
        "name_en": "Cambridge Songs",
        "name_original": "Carmina Cantabrigiensia",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "恋愛・政治・宗教を混在させる11世紀ラテン歌謡集。",
    },
    {
        "name_ja": "『ベネディクトボイレン降誕劇』",
        "name_en": "Benediktbeuern Christmas Play",
        "name_original": "Ludus de Nativitate",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "カルミナ・ブラーナ写本に残るラテン降誕劇断片。",
    },
    {
        "name_ja": "『聖ニコラウス学生劇』",
        "name_en": "St Nicholas Student Play",
        "name_original": "Tres Clerici",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "三人の学生の蘇生奇跡を劇化するラテン典礼劇。",
    },
    {
        "name_ja": "『グロースター年代記韻文序』",
        "name_en": "Gloucester Chronicle Verse Prologue",
        "name_original": "Gloucester Chronicle Verse Prologue",
        "original_script": "latin",
        "period_id": P_LATIN,
        "definition": "地方年代記の権威づけに用いられたラテン韻文序文。",
    },
    # 2. 古仏語辺境ロマンス・写本
    {
        "name_ja": "『トゥーレットのディト』",
        "name_en": "Dit de la tourette",
        "name_original": "Dit de la tourette",
        "original_script": "latin",
        "period_id": P_FR,
        "definition": "幽閉の小塔を恋愛寓意に変える古仏語ディ小品。",
    },
    {
        "name_ja": "『二人の恋人のレー』",
        "name_en": "Les Deus Amanz",
        "name_original": "Les Deus Amanz",
        "original_script": "latin",
        "period_id": P_FR,
        "definition": "山登り試練で恋人の死を語るマリー・ド・フランスの短いレー。",
    },
    {
        "name_ja": "『灰の木のレー』",
        "name_en": "Le Fresne",
        "name_original": "Le Fresne",
        "original_script": "latin",
        "period_id": P_FR,
        "definition": "捨て子認知と双生児の身分回復を扱う古仏語レー。",
    },
    {
        "name_ja": "『ラネヴァル』",
        "name_en": "Lanval",
        "name_original": "Lanval",
        "original_script": "latin",
        "period_id": P_FR,
        "definition": "妖精愛人と宮廷裁判を結ぶマリー・ド・フランスのレー。",
    },
    {
        "name_ja": "『ギヨーム・ド・ドール』",
        "name_en": "Guillaume de Dole",
        "name_original": "Roman de Guillaume de Dole",
        "original_script": "latin",
        "period_id": P_FR,
        "definition": "挿入歌を物語展開に組み込むジャン・ルナールの宮廷ロマンス。",
    },
    {
        "name_ja": "『エルサレム陥落歌』",
        "name_en": "Chanson de Jerusalem",
        "name_original": "Chanson de Jerusalem",
        "original_script": "latin",
        "period_id": P_FR,
        "definition": "第一回十字軍の包囲戦を武勲詩化した古仏語叙事詩。",
    },
    # 3. オック語ミクロ形式・詩論
    {
        "name_ja": "デスコール（オック語不均衡歌）",
        "name_en": "Descort",
        "name_original": "descort",
        "original_script": "latin",
        "period_id": P_OCC,
        "definition": "各連の韻律をずらし恋の不調和を示すトロバール形式。",
    },
    {
        "name_ja": "エスクラチャ（罵倒小詩）",
        "name_en": "Escrache",
        "name_original": "escrache",
        "original_script": "latin",
        "period_id": P_OCC,
        "definition": "敵対者を嘲罵する短いオック語諷刺詩型。",
    },
    {
        "name_ja": "トルナーダ（結尾反歌）",
        "name_en": "Tornada",
        "name_original": "tornada",
        "original_script": "latin",
        "period_id": P_OCC,
        "definition": "献辞や宛先を示すトルバドゥール詩末尾の短連。",
    },
    {
        "name_ja": "『愛の裁定』",
        "name_en": "Las Leys d'Amors",
        "name_original": "Las Leys d'Amors",
        "original_script": "latin",
        "period_id": P_OCC,
        "definition": "トゥールーズ詩院が編んだオック語詩法の大規模規範書。",
    },
    {
        "name_ja": "『ラザルのカンソ』",
        "name_en": "Canso de la Crozada, Laisse Lazar",
        "name_original": "Lazar",
        "original_script": "latin",
        "period_id": P_OCC,
        "definition": "アルビジョワ十字軍歌中のラザル挿話をめぐる叙述単位。",
    },
    {
        "name_ja": "『カニゴーの恋愛論争』",
        "name_en": "Canigo Tenso",
        "name_original": "Tenso del Canigo",
        "original_script": "latin",
        "period_id": P_OCC,
        "definition": "山岳地名を舞台化する後期オック語テンソの局地的作例。",
    },
    # 4. 古英語・中英語写本断片
    {
        "name_ja": "『フィンネスブルフ断片』",
        "name_en": "Finnesburg Fragment",
        "name_original": "The Fight at Finnsburh",
        "original_script": "latin",
        "period_id": P_EN,
        "definition": "ベオウルフ関連のフリジア戦闘を伝える古英語頭韻詩断片。",
    },
    {
        "name_ja": "『ブルナンブルフの戦い』",
        "name_en": "Battle of Brunanburh",
        "name_original": "The Battle of Brunanburh",
        "original_script": "latin",
        "period_id": P_EN,
        "definition": "年代記に挿入された王権勝利を称える古英語戦勝詩。",
    },
    {
        "name_ja": "『エクセター謎詩』",
        "name_en": "Exeter Book Riddles",
        "name_original": "Riddles",
        "original_script": "latin",
        "period_id": P_EN,
        "definition": "物体・自然・書物を声に変えるエクセター写本の謎詩群。",
    },
    {
        "name_ja": "『説教者の魂への語り』",
        "name_en": "Soul and Body",
        "name_original": "Soul and Body",
        "original_script": "latin",
        "period_id": P_EN,
        "definition": "死後の魂が肉体を責める古英語終末論的対話詩。",
    },
    {
        "name_ja": "『ハーレー抒情詩集』",
        "name_en": "Harley Lyrics",
        "name_original": "Harley Lyrics",
        "original_script": "latin",
        "period_id": P_LATE,
        "definition": "写本Harley 2253に残る英仏ラテン混淆の中英語抒情詩群。",
    },
    {
        "name_ja": "『聖エルケンワルド』",
        "name_en": "St Erkenwald",
        "name_original": "Saint Erkenwald",
        "original_script": "latin",
        "period_id": P_LATE,
        "definition": "異教裁判官の遺体発見を描く中英語頭韻復興詩。",
    },
    # 5. ゲルマン・北方・イベリア小伝承
    {
        "name_ja": "『エレーネ』",
        "name_en": "Elene",
        "name_original": "Elene",
        "original_script": "latin",
        "period_id": P_EN,
        "definition": "キュネウルフが聖十字架発見を語る古英語宗教叙事詩。",
    },
    {
        "name_ja": "『メレスブルク呪文』",
        "name_en": "Merseburg Charms",
        "name_original": "Merseburger Zaubersprueche",
        "original_script": "latin",
        "period_id": P_GER,
        "definition": "異教神名を保存する古高ドイツ語の二つの呪文詩。",
    },
    {
        "name_ja": "『ルートヴィヒの歌』",
        "name_en": "Ludwigslied",
        "name_original": "Ludwigslied",
        "original_script": "latin",
        "period_id": P_GER,
        "definition": "ノルマン撃退を王讃美に変えた古高ドイツ語戦勝詩。",
    },
    {
        "name_ja": "『グローアの呪文』",
        "name_en": "Grogaldr",
        "name_original": "Grogaldr",
        "original_script": "latin",
        "period_id": P_NORTH,
        "definition": "母の霊が息子に旅の保護呪文を授けるエッダ風詩。",
    },
    {
        "name_ja": "『フィヨルスヴィーズの歌』",
        "name_en": "Fjolsvinnsmal",
        "name_original": "Fjolsvinnsmal",
        "original_script": "latin",
        "period_id": P_NORTH,
        "definition": "門番との問答で城の知を開示する後期エッダ詩。",
    },
    {
        "name_ja": "『エレナとマリア』",
        "name_en": "Elena y Maria",
        "name_original": "Elena y Maria",
        "original_script": "latin",
        "period_id": P_IB,
        "definition": "騎士と聖職者の価値を女性対話で競わせるカスティーリャ詩。",
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
                importance_score=2,
                source_tier="primary",
                canonical_in_region="minor",
                **entry,
            )
            inserted += 1
            print(f"{inserted:02d}. {entry['name_ja']} -> {cid}")
    print(f"done: {inserted}/30")


if __name__ == "__main__":
    main()
