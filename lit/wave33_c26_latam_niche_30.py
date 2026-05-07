#!/usr/bin/env python3
"""Wave 33 C26: Latin America niche 30 concepts (subfield_id=16)."""
import sqlite3, sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"

# 5 clusters x 6 concepts. period_id mapping:
# 256=20世紀前半期, 258=Boom補完期, 226=McOndo・Crack世代, 288=21世紀ラテンアメリカ女性期, 281=ブラジル20世紀詩補完期
CONCEPTS = [
    # Cluster 1: Caribbean Spanish
    ("『夜になる前に』（Reinaldo Arenas）", "Antes que anochezca (Reinaldo Arenas)", "Antes que anochezca", "latin",
     258, 226, "アレナスのキューバ亡命自伝、検閲・同性愛・革命幻滅を抉る証言文学。", 5, "rethinking"),
    ("『パラディーソ』（Lezama Lima）", "Paradiso (Lezama Lima)", "Paradiso", "latin",
     256, 256, "レサマ・リマの大著、ネオバロック詩学とエロス・神秘主義の融合体。", 5, "invariant"),
    ("『三匹の悲しい虎』（Cabrera Infante）", "Tres tristes tigres (Cabrera Infante)", "Tres tristes tigres", "latin",
     258, 258, "ハバナの夜と話し言葉の遊戯、キューバン・スペイン語の音響実験小説。", 5, "rethinking"),
    ("『コブラ』（Severo Sarduy）", "Cobra (Severo Sarduy)", "Cobra", "latin",
     258, 258, "サルドゥイのネオバロック前衛、変身・記号・東洋性が交錯する小説。", 4, "rethinking"),
    ("ハバナ四部作（Leonardo Padura）", "Trilogía/Tetralogía de La Habana (Padura)", "Las cuatro estaciones", "latin",
     226, 226, "パドゥラのマリオ・コンデ刑事連作、ポスト革命キューバの幻滅探偵小説。", 4, "rethinking"),
    ("『庭園』（Dulce María Loynaz）", "Jardín (Dulce María Loynaz)", "Jardín", "latin",
     256, 256, "ロイナスの幻想小説、女性主体と植民地キューバの庭園記憶を詩的に描く。", 4, "partial"),

    # Cluster 2: Andean
    ("『アンデスのリトゥーマ』（Vargas Llosa）", "Lituma en los Andes (Vargas Llosa)", "Lituma en los Andes", "latin",
     226, 226, "バルガス・リョサのアンデス山岳小説、センデロ・ルミノソとアンデス神話の交叉。", 4, "rethinking"),
    ("『フリウスの世界』（Bryce Echenique）", "Un mundo para Julius (Bryce Echenique)", "Un mundo para Julius", "latin",
     258, 258, "ブライセ・エチェニケのリマ寡頭制批判、子供視点で描かれる階級・人種小説。", 4, "rethinking"),
    ("『落下する物音』（Vásquez）", "El ruido de las cosas al caer (Vásquez)", "El ruido de las cosas al caer", "latin",
     226, 226, "バスケスのコロンビア小説、麻薬戦争と恐怖の世代記憶を扱う傑作。", 4, "rethinking"),
    ("『ヤワール・フィエスタ』（Arguedas）", "Yawar Fiesta (Arguedas)", "Yawar Fiesta", "latin",
     256, 256, "アルゲダスのケチュア祭儀小説、闘牛祭をめぐる先住民世界観の擁護。", 5, "invariant"),
    ("『ガラバンボ、見えざる男』（Manuel Scorza）", "Garabombo, el invisible (Scorza)", "Garabombo el invisible", "latin",
     258, 258, "スコルサ「沈黙の戦争」連作、アンデス農民闘争のマジックリアリズム。", 4, "rethinking"),
    ("『田舎屋敷』（José Donoso）", "Casa de campo (Donoso)", "Casa de campo", "latin",
     258, 258, "ドノソのチリ・アレゴリー小説、ピノチェト政変を寓話化した家屋の物語。", 4, "rethinking"),

    # Cluster 3: Central American
    ("『トウモロコシの人々』（Asturias）", "Hombres de maíz (Asturias)", "Hombres de maíz", "latin",
     256, 256, "アストゥリアスのマヤ神話小説、トウモロコシ起源神話と先住民近代の交錯。", 5, "invariant"),
    ("『バルン・カナン』深層読解（Castellanos）", "Balún Canán (Castellanos) deep reading", "Balún Canán", "latin",
     256, 256, "ロサリオ・カステリャーノスのチアパス小説、児童視点と先住民・地主階級分析。", 4, "rethinking"),
    ("ロベルト・カスティーリョ（Honduras）", "Roberto Castillo (Honduras)", "Roberto Castillo", "latin",
     226, 226, "ホンジュラス短編作家、中米暴力と日常哲学を描く隠れた中米文学の声。", 3, "rethinking"),
    ("『マルガリータ、海はなんと美しい』（Sergio Ramírez）", "Margarita, está linda la mar (Ramírez)", "Margarita, está linda la mar", "latin",
     226, 226, "セルヒオ・ラミレスのニカラグア小説、ダリオとソモサ暗殺を交錯させる歴史小説。", 4, "rethinking"),
    ("『住まわれた女』（Gioconda Belli）", "La mujer habitada (Belli)", "La mujer habitada", "latin",
     288, 288, "ベリのニカラグア・フェミニスト小説、サンディニスタ革命と先住民霊性の融合。", 4, "rethinking"),
    ("『無分別』（Horacio Castellanos Moya）", "Insensatez (Castellanos Moya)", "Insensatez", "latin",
     226, 226, "カステリャーノス・モヤのグアテマラ虐殺証言記録小説、狂気と歴史の独白。", 4, "rethinking"),

    # Cluster 4: Brazilian補完
    ("『水族館の夏』（Lygia Fagundes Telles）", "Verão no aquário (Telles)", "Verão no aquário", "latin",
     258, 258, "テレスのブラジル女性小説、軍政期サンパウロの女性意識と家族崩壊を描く。", 4, "rethinking"),
    ("『猥褻なD夫人』（Hilda Hilst）", "A obscena senhora D (Hilst)", "A obscena senhora D", "latin",
     258, 258, "ヒルダ・ヒルストの実験詩的散文、エロス・死・神秘主義の極限言語実験。", 4, "rethinking"),
    ("『花火師』（Murilo Rubião）", "O pirotécnico Zacarias (Rubião)", "O pirotécnico Zacarias", "latin",
     256, 256, "ムリロ・ルビアンのブラジル幻想短編、カフカ的不条理を熱帯化した先駆者。", 4, "partial"),
    ("『発明された記憶』（Manoel de Barros）", "Memórias inventadas (Manoel de Barros)", "Memórias inventadas", "latin",
     281, 281, "バロスのパンタナル詩、無用の物への愛と幼年期の言語遊戯。", 4, "invariant"),
    ("『ごみ捨て場の部屋』（Carolina Maria de Jesus）", "Quarto de despejo (Carolina Maria de Jesus)", "Quarto de despejo", "latin",
     256, 256, "カロリーナのファヴェーラ日記、貧困と人種の生証言、サブアルタン文学の金字塔。", 5, "rethinking"),
    ("『幸せな男のマニュアル』（Ferréz）", "Manual prático do ódio (Ferréz)", "Manual prático do ódio", "latin",
     226, 226, "フェレースの「文学辺境（marginal）」、サンパウロ周縁部のヒップホップ的散文。", 4, "rethinking"),

    # Cluster 5: Crónica + Indigenous
    ("『火の記憶』（Eduardo Galeano）", "Memoria del fuego (Galeano)", "Memoria del fuego", "latin",
     258, 258, "ガレアーノのラ米史詩的クロニカ三部作、植民地から現代までの口承的歴史叙述。", 5, "invariant"),
    ("『トラテロルコの夜』（Elena Poniatowska）", "La noche de Tlatelolco (Poniatowska)", "La noche de Tlatelolco", "latin",
     258, 258, "ポニアトフスカの1968年虐殺証言コラージュ、テスティモニオ・ジャンルの代表作。", 5, "invariant"),
    ("ドミティラ・バリオス『私に話させて』", "Domitila Barrios: Si me permiten hablar", "Si me permiten hablar", "latin",
     258, 258, "ボリビア鉱山労働者妻ドミティラの口述自伝、ラ米テスティモニオの古典。", 4, "rethinking"),
    ("リゴベルタ・メンチュー証言", "Rigoberta Menchú: Me llamo Rigoberta Menchú", "Me llamo Rigoberta Menchú", "latin",
     258, 258, "マヤ・キチェ女性メンチューの証言、ノーベル平和賞・先住民テスティモニオの象徴。", 5, "rethinking"),
    ("エリクラ・チワイラフ詩学（Mapuche）", "Elicura Chihuailaf (Mapuche poetry)", "Elicura Chihuailaf", "latin",
     288, 288, "マプチェ詩人チワイラフの「青い口承」詩学、二言語マプドゥングン・スペイン語詩。", 4, "rethinking"),
    ("ウンベルト・アクアバル詩（Maya K'iche')", "Humberto Ak'abal (K'iche' Maya poetry)", "Humberto Ak'abal", "latin",
     288, 288, "グアテマラのキチェ語詩人アクアバル、自然・鳥声・先住民音韻の現代詩。", 4, "rethinking"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for c in CONCEPTS:
        name_ja, name_en, name_orig, region, period_id, _hist_period, definition, importance, fourth = c
        try:
            cur.execute("""
                INSERT INTO concepts (name_ja, name_en, name_original, original_script, subfield_id,
                                       region, period_id, definition, importance_score, fourth_transform_status,
                                       source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, 16, ?, ?, ?, ?, ?, 'A', 'latin')
            """, (name_ja, name_en, name_orig, "latin", region, period_id, definition, importance, fourth))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP: {name_ja} ({e})", file=sys.stderr)
    conn.commit()
    total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=16").fetchone()[0]
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total subfield_id=16: {total}")

if __name__ == "__main__":
    main()
