#!/usr/bin/env python3
"""Wave40: add 30 hyper-niche concepts to lit_latin_america."""

from lit_db_helper import LitDB

SUBFIELD = "lit_latin_america"
REGION = "ラテンアメリカ"

P_COLONIAL = 254
P_VANG = 284
P_POSTDICT = 260
P_INDIG = 231
P_WOMEN = 288

ROWS = [
    # Cluster 1: colonial archive micro-forms
    ("プロバンサ・デ・メリトス", "probanza de meritos", "probanza de meritos", P_COLONIAL, "征服者が功績を王権へ申告する証言文書ジャンル。"),
    ("レラシオン・ヘオグラフィカ応答", "relacion geografica response", "relacion geografica", P_COLONIAL, "植民地質問状への地域記述回答を読む文書形式。"),
    ("アルファベット化ナワトル告解書", "alphabetized Nahuatl confessional", "confesionario nahuatl", P_COLONIAL, "ナワトル語をローマ字化し布教告解へ組み込む植民地文体。"),
    ("アンデス・キープ書記残響", "Andean khipu scriptural residue", "khipu residue", P_COLONIAL, "キープ記憶術が年代記叙述に残す数的・索引的痕跡。"),
    ("カビルド嘆願文レトリック", "cabildo petition rhetoric", "peticion de cabildo", P_COLONIAL, "都市参事会名義で王権へ訴える集団的請願の修辞。"),
    ("聖人伝的クリオージャ自己像", "hagiographic criolla self-fashioning", "autoimagen criolla hagiografica", P_COLONIAL, "修道女・聖女伝がクリオージャ権威を作る自己演出。"),

    # Cluster 2: vanguard little-magazine poetics
    ("壁新聞アフィッシュ詩学", "wall-newspaper affiche poetics", "poetica de afiche mural", P_VANG, "街頭貼紙と詩誌を接続する前衛の即時メディア詩学。"),
    ("エストリデンティスタ機械擬声", "estridentista machine onomatopoeia", "onomatopeya estridentista", P_VANG, "機械音・都市騒音を詩行へ移すメキシコ前衛技法。"),
    ("マルティンフィエリスタ誌面冗談", "martinfierrista page joke", "chiste martinfierrista", P_VANG, "『Martin Fierro』誌上の広告風冗談と文学的内輪批評。"),
    ("クリオージョ未来派パロディ", "criollo futurist parody", "parodia futurista criolla", P_VANG, "欧州未来派語彙をブエノスアイレス俗語でずらす前衛戦略。"),
    ("アンデス・インディヘニスタ表紙詩学", "Andean indigenista cover poetics", "cubierta indigenista", P_VANG, "前衛誌の表紙図像が先住民性を構成する視覚詩学。"),
    ("ブラジル木輸出語彙", "pau-brasil export vocabulary", "vocabulario pau-brasil", P_VANG, "輸出品目の語彙で詩を国際商品化するモダニズモ技法。"),

    # Cluster 3: post-dictatorship forensic forms
    ("消失者索引詩", "desaparecido index poem", "poema indice de desaparecidos", P_POSTDICT, "失踪者名簿の索引性を詩の構造に転用する追悼形式。"),
    ("証言脚注ノワール", "testimonial footnote noir", "noir de nota testimonial", P_POSTDICT, "犯罪小説に証言脚注を埋め込み国家暴力を参照化する技法。"),
    ("軍政検閲余白", "dictatorship censorship margin", "margen censurado", P_POSTDICT, "削除・伏字・空白を軍政期読解の証拠として扱う概念。"),
    ("人権法廷モノローグ", "human-rights tribunal monologue", "monologo de tribunal", P_POSTDICT, "法廷証言の一人語りを演劇・小説へ移す記憶形式。"),
    ("遺骨鑑定エレジー", "forensic bone elegy", "elegia forense", P_POSTDICT, "発掘遺骨とDNA鑑定を弔いの詩的装置にする表現。"),
    ("秘密警察ファイル小説", "secret-police dossier novel", "novela de archivo policial", P_POSTDICT, "諜報記録の断片性を筋立てにするポスト独裁小説。"),

    # Cluster 4: Indigenous language mediation
    ("二言語自己翻訳詩", "bilingual self-translation poem", "poema autotraducido", P_INDIG, "先住民語とスペイン語間で作者が自己翻訳する詩形式。"),
    ("マプチェ・ウルトゥン転写", "Mapuche ulkantun transcription", "transcripcion ulkantun", P_INDIG, "マプチェ歌謡ulkantunを活字詩へ移す転写実践。"),
    ("キチェ語反復パラレリズム", "K'iche' repetitive parallelism", "paralelismo k'iche'", P_INDIG, "キチェ語詩で意味を増幅する反復対句構造。"),
    ("ケチュア証言の逐語異化", "Quechua testimonial literalism", "literalismo testimonial quechua", P_INDIG, "ケチュア語順をスペイン語証言文に残す翻訳異化。"),
    ("アイマラ時間逆行比喩", "Aymara reverse-time metaphor", "metafora temporal aymara", P_INDIG, "未来を背後、過去を前方とするアイマラ的時間比喩の文学化。"),
    ("ミスキート沿岸口承地図", "Miskito coastal oral map", "mapa oral miskito", P_INDIG, "海岸地名と航路記憶で物語空間を組む口承地図。"),

    # Cluster 5: 21st-century eco/body microgenres
    ("農薬母性スリラー", "agrotoxic maternity thriller", "thriller materno agrotoxico", P_WOMEN, "農薬汚染と母子不安を結ぶ現代南米スリラー形式。"),
    ("胎内独白ディストピア", "intrauterine monologue dystopia", "distopia intrauterina", P_WOMEN, "胎児・胎内視点で国家や家族の暴力を語る実験小説形式。"),
    ("フェミサイド合唱語り", "femicide choral narration", "narracion coral de feminicidio", P_WOMEN, "女性殺害事件を共同体の複数声で再構成する語り。"),
    ("クィア・サンテリアSF", "queer Santeria SF", "ciencia ficcion santera queer", P_WOMEN, "サンテリア神霊とクィア身体を未来都市SFへ接続する形式。"),
    ("国境児童アーカイブ小説", "border-child archive novel", "novela archivo de ninos frontera", P_WOMEN, "移民児童の音声・書類・写真を小説構造にする形式。"),
    ("気候葬送クロニカ", "climate funeral cronica", "cronica funebre climatica", P_WOMEN, "洪水・旱魃・森林火災を死者儀礼として記録するクロニカ。"),
]


def main() -> None:
    if len(ROWS) != 30:
        raise SystemExit(f"expected 30 rows, got {len(ROWS)}")
    too_long = [(name, len(defn)) for name, *_rest, defn in ROWS if len(defn) > 100]
    if too_long:
        raise SystemExit(f"definitions too long: {too_long}")
    with LitDB() as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=16"
        ).fetchone()[0]
        ids = []
        for name_ja, name_en, name_original, period_id, definition in ROWS:
            ids.append(db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script="latin",
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="marginal",
            ))
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=16"
        ).fetchone()[0]
    print(f"inserted={after - before} touched={len(ids)} total={after}")


if __name__ == "__main__":
    main()
