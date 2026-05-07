from lit_db_helper import LitDB


CONCEPTS = [
    # Latin clerical and school genres
    ("オルド・ラケーリス", "Ordo Rachelis", "ラケルの嘆きを劇化するラテン聖史劇台本。"),
    ("『ダニエル劇』ボーヴェ写本", "Ludus Danielis", "ダニエル書を歌唱劇化したボーヴェ大聖堂系ラテン劇。"),
    ("ゴリアルド詩のコンダクトゥス化", "Goliardic conductus", "放浪学生詩が多声・単声歌へ転用される現象。"),
    ("アクセスス・アド・アウクトーレス", "Accessus ad auctores", "学校で古典著者を読むための定型序論。"),
    ("マテリア・トロヤナ", "Matter of Troy", "トロイア伝承を中世ロマンスへ再編する題材群。"),
    ("ディスタ・カトニス中世受容", "Disticha Catonis reception", "ラテン格言詩を学校道徳教材化した受容。"),
    # Anglo-Saxon and Middle English manuscript culture
    ("ノウェル写本怪物譚群", "Nowell Codex monster narratives", "ベオウルフ周辺の怪物・驚異譚を含む写本群。"),
    ("ヴェルチェリ書『魂と身体』", "Soul and Body", "死後の魂が朽ちる身体を責める古英語説教詩。"),
    ("エクセター書『廃墟』", "The Ruin", "崩壊したローマ都市を悼む古英語断片詩。"),
    ("アニクリン・ウィス", "Ancrene Wisse", "女性隠修者向けに書かれた中英語の生活規則書。"),
    ("キャサリン・グループ", "Katherine Group", "西ミッドランド方言の女性聖人伝・教訓散文群。"),
    ("オルムルム", "Ormulum", "福音朗読を独自綴字で注解した中英語韻文説教。"),
    # Occitan and Old French microforms
    ("プラン（トルバドゥール哀悼歌）", "Planh", "死者を悼むオック語宮廷抒情の定型詩。"),
    ("テンソ（オック語論争詩）", "Tenso", "二人以上の詩人が応答する恋愛・倫理論争詩。"),
    ("パルトゥール・ド・ジュー", "Parture de jeu", "北仏トルヴェールの二択型恋愛問答詩。"),
    ("レヴェルディ（春の発端句）", "Reverdie", "春の自然描写から恋愛詩を開く定型導入。"),
    ("ディ・アムルー", "Dit amoureux", "一人称恋愛語りを展開する古仏語ディ形式。"),
    ("コンジェ（告別詩）", "Congé", "作者が友人や都市へ別れを告げる古仏語詩型。"),
    # Iberian medieval lyric and narrative
    ("カンティガ・デ・アミーゴ", "Cantiga de amigo", "女性の声で恋人不在を歌うガリシア語抒情詩。"),
    ("カンティガ・デ・エスカルニオ", "Cantiga de escarnio", "曖昧な暗示で相手を嘲るガリシア語諷刺歌。"),
    ("ハルチャ（モサラベ語折返し）", "Kharja", "ムワッシャハ末尾に置かれる俗語の恋愛短句。"),
    ("セッラニージャ", "Serranilla", "山地の女との遭遇を歌うイベリア小抒情詩。"),
    ("ロマンス・フロンテリーソ", "Romance fronterizo", "国境戦争を題材にするスペイン古ロマンセ。"),
    ("カント・デ・シビラ", "Cant de la Sibil-la", "終末預言を歌うカタルーニャ系典礼劇歌。"),
    # Norse, Germanic, and Celtic peripheries
    ("リームル", "Rimur", "サガ題材を連作韻文にした後期アイスランド詩。"),
    ("フォルナルダルサガ", "Fornaldarsaga", "北欧古代を舞台にする伝奇的サガ群。"),
    ("サットル（アイスランド小話）", "Thattr", "王や詩人をめぐる短いアイスランド散文挿話。"),
    ("ドロットクヴェット", "Drottkvaett", "宮廷スカルド詩で用いられる複雑な韻律。"),
    ("プリデインのアルマス", "Armes Prydein", "ブリテン諸族の反サクソン同盟を預言するウェールズ詩。"),
    ("アイルランド航海譚イムラム", "Immram", "海上遍歴と異界訪問を語るアイルランド物語型。"),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        for name_ja, name_en, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_eu_medieval",
                region="西欧",
                period_id=None,
                definition=definition,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )
    print(f"inserted_or_existing={len(CONCEPTS)}")


if __name__ == "__main__":
    main()
