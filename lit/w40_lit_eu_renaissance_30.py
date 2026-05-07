#!/usr/bin/env python3
"""Wave 40: 30 hyper-niche European Renaissance concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD = "lit_eu_renaissance"
REGION = "西欧"

P_IT = 144
P_IB = 145
P_FR = 146
P_EN = 147
P_NO = 148

CONCEPTS = [
    # Italian tragedy, prose, and genre microforms
    ("トリッシノ『ソフォニスバ』", "Trissino Sophonisba", "Sofonisba", P_IT, "古典則で構成された最初期のイタリア語悲劇。"),
    ("トリッシノ無韻十一音節詩", "Trissino versi sciolti", "versi sciolti", P_IT, "押韻を避ける十一音節詩で叙事・悲劇を古典化する技法。"),
    ("ルチェッライ『ロズムンダ』", "Rucellai Rosmunda", "Rosmunda", P_IT, "セネカ悲劇を俗語宮廷劇へ移した初期悲劇。"),
    ("アレティーノ『宮廷女』", "Aretino La cortigiana", "La cortigiana", P_IT, "ローマ宮廷の職業的虚飾を暴く散文喜劇。"),
    ("スペローネ『言語対話』", "Speroni Dialogue on Languages", "Dialogo delle lingue", P_IT, "俗語の権威を対話形式で争う言語論。"),
    ("チンツィオ『ヘカトンミティ』", "Giraldi Cinthio Hecatommithi", "Hecatommithi", P_IT, "残酷譚と劇材を集めた百物語型ノヴェッラ集。"),

    # French poetics, tragedy, and courtly pastoral margins
    ("ペルチエ『詩法』", "Peletier Art poetique", "Art poetique", P_FR, "綴字改革と詩形論を結ぶプレイヤード周辺詩法。"),
    ("ポンチュス・ド・ティヤール『誤謬恋愛詩集』", "Pontus de Tyard Erreurs amoureuses", "Erreurs amoureuses", P_FR, "宇宙論的比喩を恋愛詩へ注ぐリヨン派連作。"),
    ("ジャン・ド・ラ・タイユ『悲劇作法』", "Jean de La Taille Art de la tragedie", "Art de la tragedie", P_FR, "仏語悲劇の三一致と格調を説く短い劇論。"),
    ("ジョデル『ディドンの犠牲』", "Jodelle Didon se sacrifiant", "Didon se sacrifiant", P_FR, "ウェルギリウス材を仏人文主義悲劇化した作品。"),
    ("モンクレティアン『スコットランド女王』", "Montchrestien La Reine d'Escosse", "La Reine d'Escosse", P_FR, "メアリ処刑を時事悲劇へ変えた政治劇。"),
    ("ニコラ・ド・モントルー『ベルジュリー』", "Nicolas de Montreux Bergeries", "Bergeries", P_FR, "宮廷恋愛を長大化した仏牧歌ロマンス。"),

    # Iberian songbooks, theatre, pastoral, and morisco prose
    ("エンシーナ『カンシオネーロ』", "Juan del Encina Cancionero", "Cancionero", P_IB, "抒情詩と牧人劇を束ねた初期スペイン印刷詩集。"),
    ("ルーカス・フェルナンデス『ファルサとエグログ集』", "Lucas Fernandez Farsas y eglogas", "Farsas y eglogas", P_IB, "聖俗の寸劇を集めるサラマンカ演劇本。"),
    ("ペレス・デ・オリバ『アンフィトリオン』", "Perez de Oliva Amphitrion", "Amphitrion", P_IB, "プラウトゥス喜劇をカスティーリャ語散文へ移した翻案。"),
    ("ヒル・ポロ『恋するディアナ』", "Gil Polo Diana enamorada", "Diana enamorada", P_IB, "モンテマヨール牧歌を続編化したバレンシア作品。"),
    ("ペレス・デ・イタ『グラナダ内戦史』", "Perez de Hita Civil Wars of Granada", "Guerras civiles de Granada", P_IB, "ムーア趣味を歴史ロマンス化した擬史散文。"),
    ("サラス・バルバディーリョ『機知あるエレーナ』", "Salas Barbadillo La ingeniosa Elena", "La ingeniosa Elena", P_IB, "女性ピカラの策略を描く都市的短編小説。"),

    # English commercial theatre side channels
    ("リリー『カンパスペ』", "Lyly Campaspe", "Campaspe", P_EN, "宮廷機知と古代逸話を合わせたユーフュイズム喜劇。"),
    ("ピール『老妻物語』", "Peele The Old Wives' Tale", "The Old Wives' Tale", P_EN, "口承昔話を舞台上で継ぎ合わせる幻想喜劇。"),
    ("グリーン『修道士ベーコンと修道士バンゲイ』", "Greene Friar Bacon and Friar Bungay", "Friar Bacon and Friar Bungay", P_EN, "魔術師伝説を学園喜劇化した人気劇。"),
    ("デッカー『靴屋の祭日』", "Dekker Shoemaker's Holiday", "The Shoemaker's Holiday", P_EN, "職人共同体を祝祭喜劇として描く市民劇。"),
    ("チャップマン『ビュシー・ダンボワ』", "Chapman Bussy D'Ambois", "Bussy D'Ambois", P_EN, "仏宮廷決闘譚を硬質な英悲劇へ変えた作品。"),
    ("ダニエル『クレオパトラ』", "Samuel Daniel Cleopatra", "Cleopatra", P_EN, "上演より読書を想定したセネカ風押韻悲劇。"),

    # Northern Neo-Latin and school drama microcanon
    ("グナフェウス『アコラストゥス』", "Gnapheus Acolastus", "Acolastus", P_NO, "放蕩息子譚を人文主義学校劇にしたラテン喜劇。"),
    ("ビーダーマン『ケノドクスス』", "Bidermann Cenodoxus", "Cenodoxus", P_NO, "虚栄の学者を地獄へ落とすイエズス会ラテン劇。"),
    ("ブキャナン『洗礼者ヨハネ』", "Buchanan Baptistes", "Baptistes", P_NO, "暴君論を聖書悲劇に託したスコットランド人文主義劇。"),
    ("レウクリン『セルギウス』", "Reuchlin Sergius", "Sergius", P_NO, "教会腐敗を諷刺するドイツ初期人文主義喜劇。"),
    ("スホナエウス『ヨセフ』", "Schonaeus Joseph", "Josephus", P_NO, "聖書物語を教室上演用に整えたラテン学校劇。"),
    ("シクスト・ビルク『スザンナ』", "Sixt Birck Susanna", "Susanna", P_NO, "貞女受難を宗教改革期の学校劇へ翻案した作。"),
]


def main() -> None:
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            before = db.find_concept(name_ja, REGION, period_id)
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script="latin",
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            if before is None:
                inserted += 1
    print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
