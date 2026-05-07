#!/usr/bin/env python3
"""Wave 40: add 30 hyper-niche lit_eu_modernism concepts."""

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_eu_modernism"
REGION = "西欧"
PERIOD_ID = 22

CONCEPTS = [
    # Cluster 1: ケルト・島嶼モダニズム
    ("ヒュー・マクディアミッド『酔漢、薊を見る』", "MacDiarmid, A Drunk Man Looks at the Thistle", "A Drunk Man Looks at the Thistle", "latin", "スコットランド語復興を宇宙的独白へ拡張した長詩。"),
    ("ミナ・ロイ『愛の歌』", "Mina Loy, Songs to Joannes", "Songs to Joannes", "latin", "恋愛抒情を解剖学的断片へ変える英語前衛連作。"),
    ("ナンシー・キュナード『パーラー』", "Nancy Cunard, Parallax", "Parallax", "latin", "亡命社交圏の断片視差を刻む小部数モダニズム詩集。"),
    ("デイヴィッド・ジョーンズ『括弧内にて』", "David Jones, In Parenthesis", "In Parenthesis", "latin", "塹壕記憶とウェールズ叙事伝統を重ねる戦争長詩。"),
    ("リン・リグズ『緑の月』", "Lynn Riggs, Green Grow the Lilacs", "Green Grow the Lilacs", "latin", "民謡劇を境界的モダニズムに接続する地方戯曲。"),
    ("ケイト・オブライエン『国境』", "Kate O'Brien, Without My Cloak", "Without My Cloak", "latin", "アイルランド地方家族史を女性主体で組み替える長篇。"),
    # Cluster 2: 低地諸国・フラマン前衛
    ("ファン・オスタイエン『占領された都市』", "Paul van Ostaijen, Occupied City", "Bezette Stad", "latin", "活字配置で戦時アントワープを分解するフラマン詩集。"),
    ("ボルヘルス『拡声器』", "Hendrik de Vries, Luidsprekers", "Luidsprekers", "latin", "夢と音響を断片化するオランダ前衛詩の小実験。"),
    ("エディ・デュペロン『起源の国』", "E. du Perron, Land van herkomst", "Land van herkomst", "latin", "植民地記憶と欧州知識人自我を往復させる小説。"),
    ("ヘルマン・ファン・デン・ベルフの新即物詩", "Herman van den Bergh, New Objectivist verse", "Nieuwe zakelijkheid", "latin", "機械時代の硬質な像を短詩に圧縮する蘭語詩法。"),
    ("マルス文学誌『ヘット・オーフェルジヒト』", "Het Overzicht", "Het Overzicht", "latin", "構成主義詩画を媒介したアントワープ国際前衛誌。"),
    ("テオ・ファン・ドゥースブルフのメカノ詩", "Theo van Doesburg, Mecano poems", "Mécano", "latin", "デ・ステイルの匿名誌面で展開した機械的詩実験。"),
    # Cluster 3: バルカン・南東欧小前衛
    ("トリスタン・ツァラ『アンチピリン氏の初の天上冒険』", "Tzara, La première aventure céleste", "La première aventure céleste de M. Antipyrine", "latin", "ダダ以前の音声断片を舞台化したルーマニア系小品。"),
    ("ウルムズ『漏斗とスタマーテ』", "Urmuz, The Funnel and Stamate", "Pâlnia și Stamate", "latin", "官僚的論理を奇怪な物体譚へ崩すルーマニア散文。"),
    ("ゲオ・ボグザのルポルタージュ詩", "Geo Bogza, reportage poetry", "poezia reportaj", "latin", "犯罪・労働現場を前衛詩の記録形式へ移す実験。"),
    ("ラディスラフ・クリーマ『栄光あるネメシス』", "Ladislav Klíma, Glorious Nemesis", "Slavná Nemesis", "latin", "唯我論哲学をグロテスク幻想小説に変えるチェコ作品。"),
    ("ミロシュ・ツルニャンスキ『移民』", "Miloš Crnjanski, Migrations", "Seobe", "latin", "セルビア離散史を叙情的断片で組む歴史小説。"),
    ("リュボミル・ミチッチのゼニティズム", "Ljublomir Micić, Zenitism", "zenitizam", "latin", "バルカン野蛮を欧州前衛の再起動原理にした運動。"),
    # Cluster 4: ユダヤ・イディッシュ欧州前衛
    ("ペレツ・マルキシュ『堆』", "Peretz Markish, Di kupe", "די קופּע", "hebrew", "ポグロム死者の山を表現主義的長詩にしたイディッシュ作品。"),
    ("ウリ・ツヴィ・グリンベルグ『路上のメフィスト』", "Uri Zvi Greenberg, Mephisto", "מעפיסטא", "hebrew", "戦後都市を黙示録的語りで歪めるヘブライ・イディッシュ詩。"),
    ("モイシェ・クルバク『ゼリグマンの町』", "Moyshe Kulbak, Zelmenyaner", "זעלמעניאַנער", "hebrew", "ミンスク中庭を共同体崩壊の喜劇として描く連作小説。"),
    ("レイブ・クヴィトコの児童前衛詩", "Leyb Kvitko, children's avant-garde verse", "לייב קוויטקאָ", "hebrew", "児童詩に音響反復と革命的都市感覚を入れた実験。"),
    ("メレフ・ラヴィチ『孔雀』誌圏", "Melech Ravitch, Di Khalyastre", "די כאַליאַסטרע", "hebrew", "ワルシャワ前衛集団の反写実的イディッシュ詩圏。"),
    ("イツィク・マンゲル『フメシュの歌』", "Itzik Manger, Khumesh-lider", "חומש לידער", "hebrew", "聖書人物を東欧民衆劇へ移すイディッシュ詩連作。"),
    # Cluster 5: 写本・校訂・理論ミクロ論争
    ("『荒地』ポンド削除稿", "The Waste Land Pound deletions", "Waste Land drafts", "latin", "エリオット草稿で可視化される編集による断片化過程。"),
    ("ジョイス『ユリシーズ』ローゼンバック手稿", "Ulysses Rosenbach manuscript", "Rosenbach manuscript", "latin", "印刷本文以前の加筆層を残すジョイス自筆清書稿。"),
    ("カフカ遺稿束ノート番号問題", "Kafka manuscript bundle numbering", "Oktavhefte", "latin", "八折判ノート配列が作品境界を左右する校訂論点。"),
    ("プルースト貼紙カイエ", "Proust paperoles", "paperoles", "latin", "貼紙増補が生成する『失われた時』の可変的本文層。"),
    ("ベンヤミン『パサージュ論』コンヴォリュート配列", "Benjamin Arcades convolute order", "Konvolute", "latin", "引用束の順序が論証性を決める未完草稿編集問題。"),
    ("ムージル遺稿章配列論争", "Musil Nachlass chapter ordering", "Nachlasskapitel", "latin", "『特性のない男』未完部の章順をめぐる校訂上の争点。"),
]


def main() -> None:
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            before = db.find_concept(name_ja, REGION, PERIOD_ID)
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                period_id=PERIOD_ID,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            if before is None and db.find_concept(name_ja, REGION, PERIOD_ID) is not None:
                inserted += 1
    print(f"INSERTED={inserted}")


if __name__ == "__main__":
    main()
