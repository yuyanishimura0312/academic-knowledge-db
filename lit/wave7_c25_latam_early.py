"""
LIT-DB Phase 2 — C25 Wave7: Latin American Literature, Colonial through 19c
============================================================================
Inserts 40 representative concepts spanning 5 categories:
  A. 植民地期 (8) — Crónicas de Indias, Las Casas, Bernal Díaz, Sor Juana,
                     Inca Garcilaso, Ercilla, Bartolomé Hidalgo
  B. 独立期・19世紀前半 (8) — gauchesco, Martín Fierro, Sarmiento Facundo,
                              Echeverría, Mármol, Bello, costumbrismo, romanticismo
  C. 19世紀後半・モデルニスモ前夜 (8) — realismo, naturalismo, indianismo,
                                          Martí, Palma, novela de la tierra precursors,
                                          Hostos, Acevedo Díaz
  D. 主要主題 (8) — civilización vs barbarie, indigenismo precursor (19c sense),
                    gaucho 民俗主体, criollismo (19c sense), mestizaje thematics,
                    espacio americano, frontera (19c gauchesco), hispanidad debate
  E. 形式・批評概念 (8) — crónica genre, ensayo americano, novela folletín,
                          costumbrismo descripción, lengua americana 議論,
                          américa as utopia, criollo voice, lo real vs lo maravilloso 前史

subfield_id=16, code='lit_latin_america', region='グローバルサウス'
Coverage: 植民地期 (~1492-1808) ~ 19世紀末 (~1880, モデルニスモ直前)

Sources: Biblioteca Virtual Miguel de Cervantes, Memoria Chilena,
Biblioteca Nacional Argentina (BNA), Brown University John Carter Brown Library
digital archives, Wikipedia academic-grade entries.
"""
from __future__ import annotations

from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (7 periods spanning colonial through 19c)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("植民地初期", "Early Colonial Period (Lat-Am)", 1492, 1600,
     "コロンブス以降の征服期。crónicas de Indiasが主要文学形式となり、"
     "征服者・宣教師・先住民系記録者がアメリカ大陸の現実を初めて文字化した。"),
    ("植民地盛期", "High Colonial / Baroque Period", 1600, 1750,
     "植民地行政の安定化とバロック文学の隆盛。"
     "Sor Juana・Inca Garcilaso・Carrió de la Vandera等、"
     "植民地クリオージョ知識人の文学的主体形成期。"),
    ("植民地後期・独立直前", "Late Colonial / Pre-Independence", 1750, 1810,
     "啓蒙思想流入と独立運動勃興期。"
     "Bartolomé Hidalgoらgauchesco先駆者がpopularな声を文学化。"),
    ("独立期", "Independence Period", 1810, 1830,
     "ボリーバル・サン=マルティン主導の独立戦争期。"
     "Andrés Bello・Olmedoらの新古典主義詩と独立イデオロギーの結合。"),
    ("ラテンアメリカ・ロマン主義期", "Latin American Romanticism", 1830, 1870,
     "Echeverría『El matadero』『La cautiva』を起点とするロマン主義的国民文学期。"
     "Sarmiento『Facundo』『Amalia』など独裁者批判の政治文学が同時並行。"),
    ("19世紀後半・モデルニスモ前夜", "Late 19c / Pre-Modernismo", 1870, 1888,
     "リアリズム・ナチュラリズム・コスチュンブリスモの成熟期。"
     "Martí・Palma・Hostosが地域横断的な散文文化を確立。"
     "1888年Darío『Azul...』直前まで。"),
    ("ラテンアメリカ通史的・主題期", "Lat-Am Thematic / Cross-Period", 1492, 1900,
     "植民地期から19世紀末までを通底する主題群"
     "（civilización vs barbarie、mestizaje、frontera等）の括り。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — 植民地期 (8)
# ===============================================================

add({
    "name_ja": "クロニカス・デ・インディアス（インディアスの記録）",
    "name_en": "Chronicles of the Indies",
    "name_original": "crónicas de Indias",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "植民地初期",
    "definition": "16-17世紀の征服者・宣教師・先住民系記録者がアメリカ大陸での"
                  "発見・征服・伝道経験を記述した第一次史料群。"
                  "Cortés『Cartas de relación』(1519-26)、Cabeza de Vaca『Naufragios』(1542)、"
                  "Bernal Díaz、Las Casas、Sahagún、Inca Garcilasoらの作品がこの範疇に属し、"
                  "ラテンアメリカ文学の出発点を構成する。",
    "background": "1492年以降の征服活動を法的・歴史的に正当化する必要から制度的に書かれた記録。",
    "development": "目撃証言から先住民史への移行、征服者と宣教師の対立的視点も内包。",
    "historical_context": "「ラテンアメリカ文学」の起点と認知される第一次資料群、「他者」表象の起源。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/cronistas_de_indias/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "バルトロメ・デ・ラス・カサス『インディアスの破壊についての簡潔な報告』",
    "name_en": "Bartolomé de Las Casas, A Short Account of the Destruction of the Indies",
    "name_original": "Brevísima relación de la destrucción de las Indias",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "植民地初期",
    "definition": "ドミニコ会士ラス・カサス(1484-1566)が1542年に執筆、1552年に出版した"
                  "スペイン人によるアメリカ先住民虐殺の告発文書。カール5世への請願として書かれ、"
                  "後の「ニューラサ伝説(leyenda negra)」の源泉となった。"
                  "人権言説と先住民擁護の起源として近代政治思想にも巨大な影響を残す。",
    "background": "Encomienda制下の先住民虐待の現場経験と、Vitoria自然法学派との連動。",
    "development": "1550年Valladolid論争でSepúlvedaと対決、欧州諸言語に翻訳され流通。",
    "historical_context": "近代人権思想・反植民地批評の遠源として常に再読される正典文書。",
    "primary_source_url": "https://www.cervantesvirtual.com/obra/brevsima-relacin-de-la-destruccin-de-las-indias-0/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 全文",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ベルナル・ディアス・デル・カスティーリョ『新スペイン征服の真実の歴史』",
    "name_en": "Bernal Díaz del Castillo, True History of the Conquest of New Spain",
    "name_original": "Historia verdadera de la conquista de la Nueva España",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "植民地初期",
    "definition": "コルテス遠征の従軍兵士ベルナル・ディアス(1496頃-1584)が老年期に執筆、"
                  "1632年に死後出版された征服記。López de Gómaraの公式史を批判し、"
                  "兵士の目線から証言性と細部の具象性に依拠した「下からの歴史記述」を展開、"
                  "近代的記録文学・回想録の先駆として位置づけられる。",
    "background": "公式史家Gómaraによる征服美化への現場兵士からの反論として執筆された。",
    "development": "未刊状態で長く流通、1632年初版以降近代批評に再発見された。",
    "historical_context": "下からの証言文学の原型、近代回想録ジャンルの先駆。",
    "primary_source_url": "https://www.cervantesvirtual.com/obra/historia-verdadera-de-la-conquista-de-la-nueva-espaa-0/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 全文",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ソル・フアナ・イネス・デ・ラ・クルス",
    "name_en": "Sor Juana Inés de la Cruz",
    "name_original": "Sor Juana Inés de la Cruz",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "植民地盛期",
    "definition": "ヌエバ・エスパーニャ(現メキシコ)生まれの修道女詩人(1648/51-1695)、本名"
                  "Juana Ramírez de Asbaje。バロック詩・劇・哲学的散文の全領域で頂点を極め、"
                  "『Respuesta a Sor Filotea』(1691)で女性の知的権利を擁護した"
                  "ラテンアメリカ最初のフェミニスト的知識人として位置づけられる。",
    "background": "ヒエロニムス会修道女として活動、副王宮廷と接点を持ちつつ自学した百科全書的知性。",
    "development": "晩年に教会権力との衝突から書斎を放棄、ペスト看病中に死去。",
    "historical_context": "植民地クリオージョ女性が世界文学規範に到達した最初の事例として再評価。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/sor_juana_ines_de_la_cruz/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ソル・フアナ『プリメロ・スエニョ（最初の夢）』",
    "name_en": "Sor Juana, Primero Sueño (First Dream)",
    "name_original": "Primero Sueño",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "植民地盛期",
    "definition": "ソル・フアナの最高傑作とされる975行の哲学詩(1692出版)。"
                  "ゴンゴラ的バロック様式で「魂の夜の飛翔」「宇宙的認識への上昇と挫折」"
                  "を主題化、Ovidius・Hermes・新プラトン主義を統合した知的飛翔の叙述、"
                  "近代以前ラテンアメリカ詩の到達点として正典化される。",
    "background": "ゴンゴラ『Soledades』への応答であり、植民地知識人による欧州バロック更新の試み。",
    "development": "Octavio Paz『Sor Juana』(1982)による徹底的な再解釈で20世紀正典化された。",
    "historical_context": "認識・夢・限界を主題化した近代以前の世界文学的正典。",
    "primary_source_url": "https://www.cervantesvirtual.com/obra-visor/primero-sueno--0/html/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 全文",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "インカ・ガルシラソ『インカ皇統記（コメンタリオス・レアレス）』",
    "name_en": "El Inca Garcilaso de la Vega, Royal Commentaries of the Incas",
    "name_original": "Comentarios reales de los Incas",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "植民地盛期",
    "definition": "Garcilaso de la Vega Inca(1539-1616、クスコ生まれ、母方インカ王族・"
                  "父方スペイン征服者)が1609-17年に出版したインカ帝国通史。"
                  "ケチュア語と先住民口頭伝承を引用しつつスペイン語ヒューマニズムの"
                  "様式で書かれた、メスティーソ知識人の最初の主要文学的成果。",
    "background": "母方ロイヤルファミリーから聞いた口頭伝承を成人後にスペインで再構成。",
    "development": "啓蒙期のインカ復古主義、Túpac Amaru反乱の知的源泉となった。",
    "historical_context": "メスティサヘ意識・先住民文献学の起点、ラテンアメリカ歴史記述の起源的テクスト。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/inca_garcilaso/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アロンソ・デ・エルシーリャ『ラ・アラウカーナ』",
    "name_en": "Alonso de Ercilla, La Araucana",
    "name_original": "La Araucana",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "植民地初期",
    "definition": "スペイン人軍人エルシーリャ(1533-1594)がチリ征服戦争(対マプチェ族)に"
                  "従軍した経験を基に1569-89年に三部公刊した叙事詩。"
                  "古典叙事詩(Ariosto・Tasso)の様式を踏まえつつ、"
                  "「敵」マプチェ族の英雄カウポリカン・ラウタロらを尊厳ある人物として描いたことで、"
                  "ラテンアメリカ最初の「土着英雄叙事詩」と位置づけられる。",
    "background": "García Hurtado de Mendoza総督下のArauco戦争従軍経験。",
    "development": "後にチリ国民叙事詩として正典化、19世紀以降のチリ・ナショナリズムの基層。",
    "historical_context": "先住民英雄を文学的に尊厳化した最初の例、植民地叙事詩ジャンルの確立。",
    "primary_source_url": "https://www.memoriachilena.gob.cl/602/w3-article-7794.html",
    "primary_source_type": "Memoria Chilena 専用ページ",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "バルトロメ・イダルゴ（gauchesco先駆）",
    "name_en": "Bartolomé Hidalgo (gauchesque precursor)",
    "name_original": "Bartolomé Hidalgo",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "植民地後期・独立直前",
    "definition": "ウルグアイ生まれの詩人(1788-1822)、リオ・デ・ラ・プラタ独立戦争に従軍。"
                  "『Cielitos patrióticos』『Diálogos patrióticos』など、"
                  "実在のガウチョの口語(habla gauchesca)を文学言語として最初に体系的に用い、"
                  "後のgauchesco文学(Hernández『Martín Fierro』へ至る)の祖と位置づけられる。",
    "background": "独立戦争中の民兵動員と、ガウチョの政治的主体化を背景に成立。",
    "development": "後にAscasubi・del Campo・Hernándezへとgauchesco系譜が継承された。",
    "historical_context": "口語的・民衆的詩の文学化の起点、リオ・プラタ国民文学の準備段階。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/bartolome_hidalgo/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY B — 独立期・19世紀前半 (8)
# ===============================================================

add({
    "name_ja": "ガウチェスコ文学（gauchesco genre）",
    "name_en": "gauchesque literature",
    "name_original": "literatura gauchesca",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ・ロマン主義期",
    "definition": "19世紀リオ・デ・ラ・プラタ地域(アルゼンチン・ウルグアイ)で発達した、"
                  "ガウチョ(パンパの牧畜民)の口語・生活・倫理を主題とする詩・物語の総体。"
                  "Bartolomé Hidalgo→Hilario Ascasubi→Estanislao del Campo→José Hernández"
                  "という系譜で結晶化し、リオ・プラタ国民文学の中核を構成した。",
    "background": "独立戦争・連邦/中央集権抗争でガウチョが政治主体化した社会史的背景。",
    "development": "Hernández『Martín Fierro』(1872)で頂点に達し、Borges・Lugonesによって正典化された。",
    "historical_context": "口語的ポピュラー文学の正典化、ラテンアメリカ初の民衆基盤詩ジャンル。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/literatura_gauchesca/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ホセ・エルナンデス『マルティン・フィエロ』",
    "name_en": "José Hernández, Martín Fierro",
    "name_original": "El gaucho Martín Fierro / La vuelta de Martín Fierro",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ・ロマン主義期",
    "definition": "アルゼンチン詩人エルナンデス(1834-1886)が1872年(第一部『出立』)・"
                  "1879年(第二部『帰還』)に出版したガウチョ叙事詩。"
                  "サルミエント『Facundo』のbarbarie観に対抗して、"
                  "近代国家による辺境征服に追われるガウチョの声を一人称で書くことで、"
                  "アルゼンチン国民文学の正典・ラテンアメリカ20世紀詩の起点と位置づけられる。",
    "background": "ロカ将軍主導の「砂漠征服」によるガウチョの社会的駆逐への抵抗が背景。",
    "development": "20世紀にLugones『El payador』(1916)が国民詩として正典化、Borgesが繰り返し論じた。",
    "historical_context": "近代化・国民形成・周縁化の同時的描出、ラテンアメリカ抒情の源泉。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/jose_hernandez/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ドミンゴ・サルミエント『ファクンド —— 文明と野蛮』",
    "name_en": "Domingo Sarmiento, Facundo: Civilization and Barbarism",
    "name_original": "Facundo: Civilización y Barbarie",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ・ロマン主義期",
    "definition": "アルゼンチン政治家・教育者サルミエント(1811-1888)が1845年チリ亡命中に"
                  "出版した思想書。地方カウディーリョ Juan Facundo Quirogaを題材に、"
                  "「文明(都市・欧州・教育)」対「野蛮(田園・アメリカ・カウディーリョ)」"
                  "の二項対立を立てた。Rosas独裁批判であると同時に、"
                  "ラテンアメリカ・エッセイ文学の原型を確立した記念碑的著作。",
    "background": "Rosas独裁による知識人弾圧、サルミエント自身の亡命経験が直接的契機。",
    "development": "20世紀にMartínez Estrada『Radiografía de la pampa』らで反復・再批判された。",
    "historical_context": "ラテンアメリカ思想史で最も影響力のある二項対立フレーム、論争永続。",
    "primary_source_url": "https://www.cervantesvirtual.com/obra/facundo-civilizacion-y-barbarie--0/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 全文",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "エステバン・エチェベリーア『と畜場（El matadero）』",
    "name_en": "Esteban Echeverría, The Slaughterhouse",
    "name_original": "El matadero",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ・ロマン主義期",
    "definition": "アルゼンチン・ロマン主義詩人エチェベリーア(1805-1851)が1838-40年頃執筆、"
                  "1871年死後出版された短編。Rosas独裁下のブエノスアイレスのと畜場を舞台に、"
                  "暴徒化したFederalesが反対派青年を惨殺する場面を生々しく描いた、"
                  "ラテンアメリカ最初の本格的短編小説・暴力文学・政治寓話の起源。",
    "background": "Echeverríaが「世代1837」(Asociación de Mayo)主導期に執筆。",
    "development": "Borges・Cortázarらが20世紀短編伝統の起点と位置づけ、批評的再評価を受けた。",
    "historical_context": "短編ジャンル・暴力描写の先駆、独裁下の文学的抵抗の典型。",
    "primary_source_url": "https://www.cervantesvirtual.com/obra-visor/el-matadero--1/html/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 全文",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ホセ・マルモル『アマリア』",
    "name_en": "José Mármol, Amalia",
    "name_original": "Amalia",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ・ロマン主義期",
    "definition": "アルゼンチン詩人マルモル(1817-1871)がモンテビデオ亡命中の"
                  "1851-55年に新聞連載、1855年単行本化したロマン主義小説。"
                  "Rosas独裁下のブエノスアイレスを舞台にした政治的恋愛悲劇で、"
                  "ラテンアメリカ最初の主要な国民的恋愛小説・政治小説の融合体として、"
                  "後の独裁者文学・歴史小説伝統に基層を提供する。",
    "background": "Rosas体制下亡命者ジャーナリズムの中心人物としての著者の立場が反映される。",
    "development": "アルゼンチン国民読書教材として長く流通、ヨーロッパ・ロマン主義小説形式の翻案実例。",
    "historical_context": "新聞連載小説(folletín)・政治批判・恋愛物語の融合の先駆。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/jose_marmol/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アンドレス・ベリョ（ベネズエラ／チリ）",
    "name_en": "Andrés Bello",
    "name_original": "Andrés Bello",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "独立期",
    "definition": "ベネズエラ生まれの言語学者・詩人・教育者・法学者(1781-1865)、"
                  "後年チリに移住しチリ大学初代学長。『Silvas americanas』(1826/1828)で"
                  "アメリカ大陸の自然と労働を新古典主義的に詠み、"
                  "『Gramática de la lengua castellana destinada al uso de los americanos』(1847)"
                  "でアメリカ独自のスペイン語規範論を確立、ラテンアメリカ独立期の知的支柱。",
    "background": "ボリーバル英語家庭教師としてロンドン亡命を経験、ヒューマニスト的実践を展開。",
    "development": "チリ大学創設・民法典編纂(1855)・教育制度設計を主導。",
    "historical_context": "ラテンアメリカ独立期文化制度設計の中核人物、規範文法の標準を作った。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/andres_bello/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "コスチュンブリスモ（風俗描写）",
    "name_en": "costumbrismo",
    "name_original": "costumbrismo",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ・ロマン主義期",
    "definition": "19世紀のスペイン語圏で発達した「風俗(costumbres)」を観察・描写する"
                  "短いエッセイ・スケッチ系ジャンル。Mariano José de Larraら"
                  "スペイン本国に始まりラテンアメリカでは独立後の国民形成期に展開、"
                  "Ricardo Palma『Tradiciones peruanas』、José Milla(グアテマラ)、"
                  "Jotabeche(チリ)らが各国の地域性を文学化、ロマン主義とリアリズムの橋渡しを担った。",
    "background": "新興国民国家の文化的自己定義要請の中で、地域の特殊性表象が制度化された。",
    "development": "後の地域主義・リアリズム文学の素材源として継承、新聞連載文化と一体化。",
    "historical_context": "短篇散文ジャンルの確立、観察的記述の文学化、地域文学の準備。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Costumbrismo",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ラテンアメリカ・ロマン主義（romanticismo lat-am）",
    "name_en": "Latin American Romanticism",
    "name_original": "romanticismo hispanoamericano",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ・ロマン主義期",
    "definition": "1830-70年代のラテンアメリカで、欧州ロマン主義(特にユゴー・バイロン)を"
                  "受容しつつ、独立後の国民国家形成・自然・カウディーリョ批判・先住民表象等の"
                  "ローカル課題に応答した文学運動。Echeverría・Sarmiento・Mármol・Isaacs"
                  "(コロンビア『María』)・Zorrilla de San Martín(ウルグアイ『Tabaré』)らが代表者。",
    "background": "独立後の国民文化定義要請と、欧州ロマン派文学翻訳・流通の同時進行が背景。",
    "development": "国別に多様な変奏(アルゼンチン政治派・コロンビア恋愛派・ウルグアイ先住民派)を展開。",
    "historical_context": "国民文学制度化の中核、後のリアリズム・モデルニスモへ橋渡し。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Latin_American_literature#Romanticism",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY C — 19世紀後半・モデルニスモ前夜 (8)
# ===============================================================

add({
    "name_ja": "ラテンアメリカ・リアリズム（realismo lat-am）",
    "name_en": "Latin American Realism",
    "name_original": "realismo hispanoamericano",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "19世紀後半・モデルニスモ前夜",
    "definition": "1860-90年代に欧州リアリズム(Balzac・Flaubert・Galdós)を"
                  "受容したラテンアメリカ小説運動。Alberto Blest Gana(チリ"
                  "『Martín Rivas』1862)・Eugenio Cambaceres(アルゼンチン)・"
                  "Tomás Carrasquilla(コロンビア)らが、近代化する都市・地方の社会矛盾を"
                  "客観描写の枠組みで描き、20世紀小説への発展段階を構成した。",
    "background": "近代化・都市化・産業化の進展と、欧州リアリズム小説の翻訳流通が背景。",
    "development": "後にナチュラリズム・地域主義(criollismo・regionalismo)へ展開。",
    "historical_context": "ロマン主義からモデルニスモ・地域主義への過渡、社会描写の小説化。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Latin_American_literature#Realism",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ラテンアメリカ・ナチュラリズム（naturalismo lat-am）",
    "name_en": "Latin American Naturalism",
    "name_original": "naturalismo hispanoamericano",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "19世紀後半・モデルニスモ前夜",
    "definition": "1880-1900年頃、Émile Zolaの自然主義小説をラテンアメリカ的に翻案した小説運動。"
                  "Eugenio Cambaceres『Sin rumbo』(1885)『En la sangre』(1887)、"
                  "Federico Gamboa(メキシコ『Santa』1903)、Aluísio Azevedo(ブラジル"
                  "『O cortiço』1890)らが、遺伝・環境決定論・移民・売春・社会階級を主題化、"
                  "近代化の社会病理を文学化した。",
    "background": "近代都市化・移民流入・社会問題の顕在化と、Zolaの理論的影響。",
    "development": "20世紀地域主義(novela de la tierra)とインディヘニスモへの素材継承。",
    "historical_context": "社会病理・階級問題の小説化、近代化批判の最初の文学的言語化。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Naturalism_(literature)#In_Latin_America",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "インディアニスモ（19世紀ロマン派的先住民表象）",
    "name_en": "indianismo (19th-century Romantic Indianism)",
    "name_original": "indianismo",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ・ロマン主義期",
    "definition": "19世紀のラテンアメリカ・ロマン主義文脈で発達した、先住民を"
                  "「気高い野蛮人(noble savage)」として理想化・神話化する表象様式。"
                  "ブラジルではJosé de Alencar『Iracema』(1865)『O Guarani』(1857)、"
                  "ウルグアイではZorrilla de San Martín『Tabaré』(1888)が代表作。"
                  "20世紀の社会派インディヘニスモとは区別される、観念的・美的先住民像。",
    "background": "独立後の国民起源神話形成要請と、欧州ロマン派の「高貴な野蛮人」観の融合。",
    "development": "20世紀にMariátegui・Arguedas系のリアリズム的indigenismoによって批判的に乗り越えられた。",
    "historical_context": "先住民表象の最初の文学的様式、後のインディヘニスモ論争の起点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Indianism_(arts)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ホセ・マルティ",
    "name_en": "José Martí",
    "name_original": "José Martí",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "19世紀後半・モデルニスモ前夜",
    "definition": "キューバの詩人・思想家・革命家(1853-1895)。"
                  "『Ismaelillo』(1882)『Versos sencillos』(1891)で詩を、"
                  "『Nuestra América』(1891)で散文エッセイを革新し、"
                  "モデルニスモ詩の先駆かつラテンアメリカ統一思想の代表者。"
                  "1895年キューバ独立戦争で戦死、20世紀ラテンアメリカ思想の中核的アイコン。",
    "background": "キューバ独立運動の組織者として米国・中南米・欧州を移動、ジャーナリストとして活動。",
    "development": "Casa de las Américasがマルティ研究の制度的中心、革命キューバ思想の正典。",
    "historical_context": "詩人・思想家・革命家の三位一体的アイコン、ラテンアメリカ統合思想の起点。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/jose_marti/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "リカルド・パルマ『ペルーの伝承（Tradiciones peruanas）』",
    "name_en": "Ricardo Palma, Peruvian Traditions",
    "name_original": "Tradiciones peruanas",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "19世紀後半・モデルニスモ前夜",
    "definition": "ペルー作家パルマ(1833-1919)が1872-1910年に十巻にわたり刊行した"
                  "「tradición(伝承)」と呼ぶ独創的短編散文集。植民地期リマの逸話・"
                  "風俗・伝説を歴史と虚構を混淆させて綴り、「tradición」という新ジャンルを"
                  "確立した。コスチュンブリスモとリアリズムの融合、"
                  "ラテンアメリカ短編散文の重要な源泉。",
    "background": "リマ国立図書館長として植民地史料に深く接し、それを語り直す形式を発見。",
    "development": "「tradición」は他国にも模倣者を生み、ラテンアメリカ独自の短編散文ジャンルとして定着。",
    "historical_context": "歴史と虚構の境界を遊戯化、後のBorges『Historia universal de la infamia』にも影響。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/ricardo_palma/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "大地小説の先駆者群（novela de la tierra precursors）",
    "name_en": "novel of the land — precursors",
    "name_original": "precursores de la novela de la tierra",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "19世紀後半・モデルニスモ前夜",
    "definition": "20世紀初頭に結晶化する「大地小説(novela de la tierra)」の19世紀における"
                  "先駆作品群。Jorge Isaacs『María』(1867、コロンビア)・"
                  "Eustasio Rivera以前の地域描写、Eduardo Acevedo Díaz(ウルグアイ)、"
                  "Alberto Blest Gana(チリ)らが、ラテンアメリカの自然・農村・地方を"
                  "前景化する小説伝統の基層を作った。",
    "background": "地域固有の自然・風土を国民文学の核に置く要請が独立後に持続的に存在。",
    "development": "20世紀初頭にGallegos『Doña Bárbara』・Güiraldes『Don Segundo Sombra』として結晶化。",
    "historical_context": "ラテンアメリカ小説における自然と土地の中心性、地域主義の系譜的源泉。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Novel_of_the_land",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "エウヘニオ・マリア・デ・オストス",
    "name_en": "Eugenio María de Hostos",
    "name_original": "Eugenio María de Hostos",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "19世紀後半・モデルニスモ前夜",
    "definition": "プエルトリコ生まれの思想家・教育者・作家(1839-1903)。"
                  "『La peregrinación de Bayoán』(1863)などで自伝的旅行記小説を、"
                  "『Tratado de moral』『Lecciones de derecho constitucional』で"
                  "ラテンアメリカ実証主義教育思想を確立。プエルトリコ・ドミニカ共和国・"
                  "チリ・ベネズエラを移動した汎ラテンアメリカ的知識人。",
    "background": "プエルトリコ独立運動の知的指導者として欧州・南米・カリブを横断的に活動。",
    "development": "ドミニカ共和国師範学校創設・チリ大学法学部刷新等、教育制度設計を実践。",
    "historical_context": "汎カリブ・汎ラテンアメリカ的知識人の典型、エッセイと教育論の連動。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/eugenio_maria_de_hostos/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "エドゥアルド・アセベド・ディアス",
    "name_en": "Eduardo Acevedo Díaz",
    "name_original": "Eduardo Acevedo Díaz",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "19世紀後半・モデルニスモ前夜",
    "definition": "ウルグアイ作家・政治家(1851-1921)、ウルグアイ歴史小説の創始者。"
                  "『Ismael』(1888)『Nativa』(1890)『Grito de gloria』(1893)『Lanza y sable』(1914)"
                  "の四部作でウルグアイ独立から内戦までを叙事的に描き、ガウチョと国民形成を"
                  "リアリズム的に主題化、20世紀リオ・プラタ歴史小説伝統の起点となった。",
    "background": "ブランコ党政治家としての亡命経験を背景に歴史小説を執筆。",
    "development": "後継のEnrique Amorim・Juan Carlos Onettiらウルグアイ近代小説伝統の基層を準備。",
    "historical_context": "ラテンアメリカ歴史小説の確立、ガウチョ表象のリアリズム的更新。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/eduardo_acevedo_diaz/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY D — 主要主題 (8)
# ===============================================================

add({
    "name_ja": "文明 vs 野蛮（civilización vs barbarie）",
    "name_en": "civilization vs barbarism",
    "name_original": "civilización vs barbarie",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ通史的・主題期",
    "definition": "サルミエント『Facundo』(1845)が定式化し、その後ラテンアメリカ思想史で"
                  "最も支配的かつ論争的なフレームとなった二項対立。"
                  "「文明=都市・欧州・教育」/「野蛮=パンパ・カウディーリョ・先住民」という"
                  "ヒエラルキー的対比が、後の進歩主義・近代化政策・地域主義反論等の前提となり、"
                  "20世紀全体にわたって繰り返し批判・反転された。",
    "background": "Rosas独裁批判と欧州啓蒙的進歩主義の融合的論理として19世紀半ばに成立。",
    "development": "Hernández『Martín Fierro』が「野蛮側」から反論、20世紀には脱植民地批評で全面解体。",
    "historical_context": "ラテンアメリカ自己理解の支配的構図、政策・教育・文化全般を規定し続けた論争。",
    "primary_source_url": "https://www.cervantesvirtual.com/obra/facundo-civilizacion-y-barbarie--0/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "先住民問題の先駆的問題化（19世紀）",
    "name_en": "indigenismo precursor (19c thematic problem)",
    "name_original": "indigenismo precursor (siglo XIX)",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "19世紀後半・モデルニスモ前夜",
    "definition": "19世紀ラテンアメリカ文学が先住民を主題化する際の「先住民問題」"
                  "(土地収奪・ラテン語化・社会的従属)の先駆的問題化。"
                  "Clorinda Matto de Turner『Aves sin nido』(1889)が代表的な"
                  "リアリズム的先住民問題小説であり、後の20世紀社会派インディヘニスモ"
                  "(Icaza・Alegría・Arguedas)の直接的先駆として位置づけられる。"
                  "20世紀のregionalist indigenismoとは区別される19c枠の表象問題。",
    "background": "アンデス諸国の先住民系農民をめぐる土地・労働問題が知識人に意識化され始めた。",
    "development": "20世紀のMariátegui社会主義的インディヘニスモへの理論的橋渡しを担った。",
    "historical_context": "先住民を観念化(indianismo)から社会問題化(indigenismo)へ移す転換点。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/clorinda_matto_de_turner/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ガウチョ —— 民俗的主体",
    "name_en": "gaucho as popular subject",
    "name_original": "el gaucho como sujeto popular",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ通史的・主題期",
    "definition": "リオ・デ・ラ・プラタ平原(パンパ)の牧畜民ガウチョが、"
                  "19世紀ラテンアメリカ文学において獲得した「民俗的主体」としての位置。"
                  "独立戦争従軍と内戦動員を経て政治化されたガウチョは、"
                  "Hidalgo→Hernándezのgauchesco系譜で文学的主体として定着し、"
                  "サルミエント的「野蛮」表象との対峙の中で国民文学の中心的形象となった。",
    "background": "リオ・プラタ平原の牧畜経済と独立戦争での民兵動員が社会的基盤。",
    "development": "20世紀初頭Lugones『El payador』により国民詩的形象として正典化。",
    "historical_context": "民衆主体の文学化の典型、欧州的「市民」とは別の主体形象の創出。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/literatura_gauchesca/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "クリオージョ意識（19世紀的criollismo）",
    "name_en": "criollismo (19c criollo consciousness)",
    "name_original": "criollismo (siglo XIX)",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "19世紀後半・モデルニスモ前夜",
    "definition": "19世紀ラテンアメリカで、植民地生まれの白人系(criollo)知識人が"
                  "自らの場所(América)・言語・風俗をスペイン本国とは区別された"
                  "独自的存在として主題化した文学的意識形態。"
                  "20世紀の地域主義としてのcriollismo(Gallegos等)とは区別される、"
                  "独立期~19世紀末のクリオージョ自意識の文学的形成過程。",
    "background": "独立後の国民形成期に、クリオージョ知識人が「アメリカ的」自己定義を求めた。",
    "development": "20世紀初頭の地域主義(criollismo regionalista)へと制度的に発展。",
    "historical_context": "クリオージョ・ナショナリズムの文学的核、後の地域主義への前史。",
    "primary_source_url": "https://es.wikipedia.org/wiki/Criollismo",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "メスティサヘ主題（19世紀的）",
    "name_en": "mestizaje thematics (19c)",
    "name_original": "temática del mestizaje (siglo XIX)",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ通史的・主題期",
    "definition": "Inca Garcilasoの混血的自己提示を起源とし、19世紀の独立期~"
                  "国民形成期において文学的主題として浮上した「混血(mestizaje)」言説。"
                  "ロマン主義のindianismo・ガウチョ表象・アロンソ・デ・エルシーリャの"
                  "土着英雄表象等が、20世紀のVasconcelos『La raza cósmica』(1925)へ至る"
                  "メスティサヘ・イデオロギーの19世紀的前段階を構成した。",
    "background": "クリオージョ・先住民・アフリカ系・移民系の混在社会を国民として包摂する要請。",
    "development": "20世紀にVasconcelos宇宙的人種論として理論化、後にメスティサヘ批判へと反転。",
    "historical_context": "ラテンアメリカ国民形成イデオロギーの基層、混血・統合言説の19c起源。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mestizaje",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アメリカ的空間（espacio americano）",
    "name_en": "American Space",
    "name_original": "espacio americano",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ通史的・主題期",
    "definition": "ラテンアメリカ文学が独自の文学的主題として確立してきた"
                  "「アメリカ大陸の空間」概念。植民地期の発見・征服空間、"
                  "Bello『Silva a la agricultura de la zona tórrida』(1826)の熱帯自然、"
                  "サルミエントのパンパ、Isaacs『María』のカウカ渓谷、"
                  "novela de la tierra系の地域空間など、ラテンアメリカ的存在の根源的"
                  "規定としての地理・自然の文学化。",
    "background": "欧州から見た「異質な空間」を文学的に肯定的価値として再構成する要請。",
    "development": "20世紀の魔術的リアリズムに至る空間的想像力の系譜の起点。",
    "historical_context": "ラテンアメリカ存在論の中核としての空間性、地理と文学の連動。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/andres_bello/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "境界（frontera —— gauchesco的境界線概念）",
    "name_en": "frontera (gauchesque frontier concept)",
    "name_original": "frontera (concepto gauchesco)",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ・ロマン主義期",
    "definition": "19世紀ラテンアメリカ文学、特にgauchesco・サルミエント系の"
                  "テクストにおける「文明」と「野蛮」、「白人入植」と「先住民」、"
                  "「中央国家」と「辺境」を分ける境界線の概念。"
                  "Echeverría『La cautiva』(1837)、Hernández『Martín Fierro』が"
                  "もっとも鋭くこの境界線を主題化、ラテンアメリカ近代化過程の暴力性を象徴する場。",
    "background": "アルゼンチンの「砂漠征服」など先住民領域への国家拡張が直接的歴史背景。",
    "development": "後の地域主義・脱植民地批評に至る「frontera」言説の起点。",
    "historical_context": "近代国民国家形成の暴力性が文学的に可視化される最重要トポス。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/jose_hernandez/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "イスパニダー論争（hispanidad debate）",
    "name_en": "hispanidad debate",
    "name_original": "debate sobre la hispanidad",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "19世紀後半・モデルニスモ前夜",
    "definition": "独立後のラテンアメリカ知識人が、スペイン本国との文化的・"
                  "言語的・歴史的紐帯(hispanidad)をどう評価するかをめぐる持続的論争。"
                  "Bello・サルミエント・マルティ・ロドーらが各自の立場で関与し、"
                  "「ラテンアメリカは欧州=スペインの延長か、独自的存在か」"
                  "という中核的アイデンティティ問題を文学・思想に持ち込んだ。",
    "background": "1898年米西戦争前後にスペインの没落と汎ヒスパニズム再興要請が論争を激化させた。",
    "development": "Rodó『Ariel』(1900)で結晶化、20世紀の汎ヒスパニズム論争・反米論と継承される。",
    "historical_context": "ラテンアメリカ自己定義の中核問題、スペイン語圏文学共同体観念の起源。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Hispanidad",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY E — 形式・批評概念 (8)
# ===============================================================

add({
    "name_ja": "クロニカ（crónica genre）",
    "name_en": "crónica (chronicle as genre)",
    "name_original": "crónica",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ通史的・主題期",
    "definition": "ラテンアメリカで植民地期のcrónicas de Indiasから始まり、"
                  "19世紀末モデルニスモ期にマルティ・ダリオらが新聞コラム形式で更新し、"
                  "20世紀以降にCarlos Monsiváis等が更に文学化した、"
                  "「現実観察+文学的記述」を特徴とする独特の散文ジャンル。"
                  "ジャーナリズムと文学の境界を遊戯化するラテンアメリカ的散文形式の核。",
    "background": "植民地期の征服記録を起点とし、近代化期に新聞文化と接続して再生した。",
    "development": "20世紀のMonsiváis・Pedro Lemebel(チリ)らクロニスタへ継承。",
    "historical_context": "ラテンアメリカ散文文学の固有性を象徴するジャンル、ジャーナリズムと文学の融合形式。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Cr%C3%B3nica",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アメリカ・エッセイ（ensayo americano）",
    "name_en": "American essay (Latin American essay tradition)",
    "name_original": "ensayo americano / ensayo hispanoamericano",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ通史的・主題期",
    "definition": "ラテンアメリカ独自のアイデンティティ・歴史・運命を主題化する"
                  "エッセイ伝統。サルミエント『Facundo』(1845)を起点に、"
                  "マルティ『Nuestra América』(1891)・ロドー『Ariel』(1900)へと継承され、"
                  "20世紀のMartínez Estrada・Octavio Paz・Edmundo O'Gormanへ至る、"
                  "ラテンアメリカ思想散文の中核ジャンル。",
    "background": "独立後の自己定義要請とエッセイという柔軟な形式の親和性が成立条件。",
    "development": "20世紀のPaz『El laberinto de la soledad』(1950)でメキシコ・アイデンティティ論として頂点。",
    "historical_context": "ラテンアメリカ思想散文の中核形式、アイデンティティ思考の主要言語。",
    "primary_source_url": "https://www.cervantesvirtual.com/obras/autor/marti-jose-1853-1895-1085",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "新聞連載小説（novela folletín）",
    "name_en": "serialized novel (folletín)",
    "name_original": "novela folletín / folletín literario",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ・ロマン主義期",
    "definition": "19世紀ラテンアメリカ各国の新聞・雑誌で連載された長編小説形式。"
                  "Mármol『Amalia』を典型に、ロマン主義小説の流通様式として確立し、"
                  "都市読者層の形成・大衆的文学市場の成立・新聞ジャーナリズムと"
                  "小説の連動を担った、ラテンアメリカ近代小説の流通基盤。",
    "background": "フランスのfeuilleton(Sue・Dumas)型の翻案、印刷文化と新聞ジャーナリズム発展。",
    "development": "20世紀のラジオ・テレビ・ノベラ伝統(telenovela)の遠源として継承される。",
    "historical_context": "近代小説の大衆化基盤、後のラテンアメリカ大衆文化(telenovela等)の起源。",
    "primary_source_url": "https://es.wikipedia.org/wiki/Folletín",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "コスチュンブリスモ的描写（costumbrismo descripción）",
    "name_en": "costumbrismo descriptive technique",
    "name_original": "descripción costumbrista",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ・ロマン主義期",
    "definition": "コスチュンブリスモ・ジャンル特有の描写技法。"
                  "観察者(narrator)が地域の風俗・服装・食物・話し方・儀礼等を"
                  "細密に描写・列挙する記述様式で、Larra→Palma→Acevedo Díaz→"
                  "20世紀地域主義小説へと継承された。読者の風俗的好奇心と国民的"
                  "教育要請を同時に満たす機能を持ち、リアリズム描写技法の先駆。",
    "background": "新興読者層の地域知識への需要と、国民形成期の文化整序要請の交差。",
    "development": "後にリアリズム・ナチュラリズム小説の精密描写技法に統合された。",
    "historical_context": "ラテンアメリカ散文描写技法の準拠点、観察的記述の文学化。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Costumbrismo",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アメリカ語論争（lengua americana 議論）",
    "name_en": "American Spanish debate",
    "name_original": "debate sobre la lengua americana",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "独立期",
    "definition": "独立後のラテンアメリカで、スペイン語をスペイン本国規範に従わせるか、"
                  "アメリカ独自の規範を立てるかをめぐる持続的論争。"
                  "Andrés Bello『Gramática』(1847)が「アメリカ人のための」スペイン語を"
                  "標榜し、サルミエントは正書法改革を提唱、Cuervo(コロンビア)は"
                  "ラテンアメリカ各国スペイン語の分岐を懸念する立場をとった。",
    "background": "独立後の文化的自立要請と、スペイン語圏の言語的統一性維持要請の緊張。",
    "development": "20世紀のRoyal Academyとの諸国語アカデミー連合体制で論争は制度化された。",
    "historical_context": "ラテンアメリカ言語アイデンティティ形成の核、規範文法の地域的多元化問題。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/andres_bello/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アメリカ＝ユートピア（américa as utopia）",
    "name_en": "America as utopia",
    "name_original": "América como utopía",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ通史的・主題期",
    "definition": "コロンブス以来、欧州の側からも19世紀以降ラテンアメリカ自身の側からも"
                  "繰り返し投影された「アメリカ大陸=新しい人類の場」というユートピア言説。"
                  "Vasco de Quiroga(16世紀)のミチョアカン・ユートピア計画、"
                  "Bello・マルティ・Rodóの汎アメリカ的未来構想等を含む、"
                  "ラテンアメリカ歴史哲学の中核的言説形象。",
    "background": "Thomas More『Utopia』のアメリカ的読み替えに始まる長期持続的言説。",
    "development": "20世紀のEdmundo O'Gorman『La invención de América』(1958)で批判的に再考された。",
    "historical_context": "ラテンアメリカ自己理解の最古の言説層、欧州近代の他者投影と自己投影の交差点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Utopia",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "クリオージョの声（criollo voice）",
    "name_en": "criollo voice",
    "name_original": "voz criolla",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "植民地後期・独立直前",
    "definition": "植民地期後期から独立期にかけて、植民地生まれ白人系(criollo)知識人が"
                  "スペイン本国エリートとは区別された独自的話者位置を文学的に確立した過程。"
                  "Sor Juana・Inca Garcilasoの先駆を経て、独立期のBello・Olmedoらの"
                  "新古典主義詩、19世紀ロマン主義小説に至るクリオージョの一人称的"
                  "話者位置の獲得。",
    "background": "植民地後期にクリオージョ層が経済・知的に成熟し独自意識を持ち始めた。",
    "development": "後にgauchesco的民衆声・先住民系声との緊張関係に置かれる。",
    "historical_context": "ラテンアメリカ作家性の制度的起源、後の主体多元化への前提。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Criollo_people",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "驚異的現実の前史（lo real vs lo maravilloso 前史）",
    "name_en": "lo real vs lo maravilloso — pre-history",
    "name_original": "prehistoria de lo real vs lo maravilloso",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ラテンアメリカ通史的・主題期",
    "definition": "20世紀のCarpentier『lo real maravilloso』(1949)・García Márquez的"
                  "魔術的リアリズムに先行する、ラテンアメリカ文学における"
                  "「現実そのものの驚異性」の言説的前史。"
                  "コロンブス『Diario』、Cabeza de Vaca『Naufragios』、Inca Garcilasoの"
                  "驚異記述、Palma『Tradiciones peruanas』の歴史と虚構の混淆等、"
                  "20世紀以前から繰り返し現れる現実-驚異の融合的記述伝統。",
    "background": "コロンブス以来「アメリカ=驚異の場」とする欧州投影と、植民地知識人の"
                  "自地域驚異性主張の重ね合わせとして成立した記述様式。",
    "development": "20世紀にCarpentierにより理論化され、ブーム期魔術的リアリズムの基層となる。",
    "historical_context": "魔術的リアリズムの長期的前史、ラテンアメリカ文学の現実観の特異性の起源。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/cronistas_de_indias/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# Fourth-transformation tags (10 entries — at least 10 required)
# ===============================================================

FOURTH_TRANSFORM_TAGS: dict[str, list[dict]] = {
    "クロニカス・デ・インディアス（インディアスの記録）": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "目撃証言性に依拠するcrónicaの真正性概念は、AI生成テクストが"
                      "「観察されざる現実」を記述しうる時代に根本的に問い直される。"
                      "誰が誰の経験を保証するかという問題はLLM時代に再浮上する。",
         "ai_phenomenon": "LLM hallucination, synthetic eyewitness narratives, "
                          "AI-fabricated 'discoveries'"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "crónicaは観察者の経験順序を物語に転換する形式だが、"
                      "AIによる時系列再構成・複数視点合成が、観察者-物語の固有結合を解体しうる。",
         "ai_phenomenon": "AI narrative reconstruction, multi-perspective synthesis"},
    ],
    "文明 vs 野蛮（civilización vs barbarie）": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "サルミエント二項対立は欧州近代を「文明」の絶対基準とするが、"
                      "AI時代の知の再分配・グローバルサウスからのAI批評の興隆は、"
                      "この基準の絶対性を解体する。",
         "ai_phenomenon": "decolonial AI ethics, Global South AI critique, "
                          "challenges to Eurocentric AI training data"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "「文明」と「野蛮」を分ける主体定義は、"
                      "AIが「主体」概念自体を揺さぶる時代に再考を迫られる。"
                      "誰がどの立場から「文明」を定義するかの問いは AI時代に深化する。",
         "ai_phenomenon": "AI agency, post-human subject debates"},
    ],
    "先住民問題の先駆的問題化（19世紀）": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "19世紀のindigenismo precursor は先住民を「代弁」する非先住民知識人の"
                      "立場から書かれたが、AI時代の言語モデルは先住民言語の"
                      "「自己代弁」可能性を技術的に変容させる。"
                      "誰が代弁するかの倫理問題は AI時代に再構成される。",
         "ai_phenomenon": "indigenous-language LLMs, AI translation of low-resource languages, "
                          "epistemic representation in AI systems"},
    ],
    "ガウチェスコ文学（gauchesco genre）": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "gauchescoの独自性はパンパのガウチョ口語(habla gauchesca)の"
                      "詩的文学化にあるが、LLM時代に「マイナー言語変種」を"
                      "AIが「再生産」する可能性は、gauchesco的口語的真正性の"
                      "概念を根本から揺さぶる。",
         "ai_phenomenon": "LLM regeneration of dialect varieties, AI-synthesized vernacular voices"},
    ],
    "アメリカ・エッセイ（ensayo americano）": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "ensayo americanoは「ラテンアメリカ的我々」を主体として"
                      "アイデンティティを思考する形式だが、AI時代に「我々」と"
                      "「機械」の境界が揺らぐ中で、集合的主体定義の前提が再考される。",
         "ai_phenomenon": "collective AI agents, post-anthropic subject formation"},
        {"axis": "言語", "status": "rethinking",
         "rationale": "ensayo americanoは「アメリカ的スペイン語」での思考を要件とするが、"
                      "AIによる多言語等価生成は地域的言語アイデンティティの"
                      "中核前提を変容させる。",
         "ai_phenomenon": "multilingual LLMs, AI translation as default language modality"},
    ],
    "クロニカ（crónica genre）": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "crónicaのジャンル成立は「観察者-記述者の経験的関与」に基づくが、"
                      "AIによる現実観察・記述生成が普遍化する時代に、"
                      "観察関与の真正性概念は根本から再構築される。",
         "ai_phenomenon": "AI journalistic chronicle generation, synthetic on-the-ground reporting"},
    ],
    "メスティサヘ主題（19世紀的）": [
        {"axis": "主体", "status": "partial",
         "rationale": "メスティサヘ言説は「混血を通じた国民統合」を理想化するが、"
                      "AI時代には「人間-機械混合主体(hybrid subject)」という新たな"
                      "混合性が前景化する。19c メスティサヘ言説は人間集団内の混合に"
                      "限定される点で AI時代の混合性論には部分的な前史しか提供しない。",
         "ai_phenomenon": "human-AI hybrid subjects, post-human mestizaje debates"},
    ],
    "驚異的現実の前史（lo real vs lo maravilloso 前史）": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "「現実そのものが驚異的である」という19世紀以前の表現は、"
                      "AI生成画像・テクストが「驚異の現実」を任意に生成する時代に、"
                      "驚異の真正性根拠そのものを問い直される。",
         "ai_phenomenon": "AI image generation as everyday reality, synthetic 'wondrous' content"},
    ],
}


# ===============================================================
# Cross-domain links (10 entries — at least 8 required)
# ===============================================================

# Tuple format: (concept_name_ja, target_db, link_type, target_entity_name, description)
CROSS_DOMAIN_LINKS: list[tuple] = [
    ("バルトロメ・デ・ラス・カサス『インディアスの破壊についての簡潔な報告』", "PHIL",
     "shared_concept", "natural law / human rights",
     "Vitoria自然法学派と連動し、近代人権思想の起源として哲学DBの権利論伝統と直接共有される。"),
    ("ソル・フアナ・イネス・デ・ラ・クルス", "PHIL",
     "shared_concept", "feminist epistemology / women's right to learn",
     "『Respuesta a Sor Filotea』は女性の知的権利を哲学的に論証し、"
     "近代フェミニスト認識論の植民地期前史として哲学DBと共有される。"),
    ("アンドレス・ベリョ（ベネズエラ／チリ）", "PHIL",
     "shared_concept", "Latin American Enlightenment, juridical philosophy",
     "Bello『Gramática』『民法典』はラテンアメリカ啓蒙思想・法哲学の中核業績であり、"
     "哲学DBの近代法哲学・教育思想と共有される。"),
    ("ドミンゴ・サルミエント『ファクンド —— 文明と野蛮』", "PHIL",
     "shared_concept", "civilization-barbarism dichotomy / philosophy of history",
     "Facundoの civilización vs barbarie 二項対立はラテンアメリカ歴史哲学の"
     "中核フレームとして哲学DBの歴史哲学・教育思想と直接共有される。"),
    ("メスティサヘ主題（19世紀的）", "AN",
     "shared_concept", "mestizaje as anthropological category",
     "メスティサヘ言説は人類学DBの混血・人種・民族カテゴリ理論と直接共有され、"
     "Vasconcelos『La raza cósmica』前史として人類学的人種言説と一体的に展開する。"),
    ("ガウチョ —— 民俗的主体", "AN",
     "shared_concept", "popular subject / pastoral subjectivity",
     "ガウチョの民俗的主体性は人類学DBの牧畜民・周縁集団主体性研究と並行的に成立、"
     "民衆主体研究の典型ケースとして共有される。"),
    ("クロニカス・デ・インディアス（インディアスの記録）", "AN",
     "shared_concept", "early ethnography / proto-anthropological writing",
     "Sahagún『Historia general de las cosas de la Nueva España』等のcrónicaは"
     "近代人類学のプロト・エスノグラフィーであり、人類学DBの記述伝統の起源と共有される。"),
    ("インカ・ガルシラソ『インカ皇統記（コメンタリオス・レアレス）』", "AN",
     "shared_concept", "indigenous historiography / native informant",
     "Inca Garcilasoはケチュア口頭伝承を文献化したメスティーソ知識人として、"
     "人類学DBのnative informant・先住民歴史記述伝統の起源として共有される。"),
    ("ホセ・マルティ", "PT",
     "shared_concept", "modernist poetics / political poetry",
     "マルティ『Versos sencillos』はモデルニスモ詩の先駆として詩学DBと直接共有され、"
     "政治詩と象徴詩の融合の典型例。"),
    ("先住民問題の先駆的問題化（19世紀）", "AN",
     "shared_concept", "indigenismo as social-scientific category",
     "indigenismoの19世紀的問題化は人類学DBの先住民研究・文化人類学の"
     "ラテンアメリカ的起源として直接共有される。"),
]


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

def main() -> None:
    with LitDB() as db:
        # Seed periods
        period_id_by_key: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(
                name_ja=nj, region="グローバルサウス",
                start_year=sy, end_year=ey,
                name_en=ne, description=desc,
            )
            period_id_by_key[nj] = pid

        # Insert concepts
        name_to_id: dict[str, int] = {}
        inserted = 0
        skipped = 0
        for entry in CONCEPTS:
            ent = dict(entry)
            period_key = ent.pop("period_key", None)
            if period_key:
                ent["period_id"] = period_id_by_key.get(period_key)
            try:
                cid = db.insert_concept(**ent)
                name_to_id[ent["name_ja"]] = cid
                inserted += 1
            except LitDBError as e:
                print(f"[error] insert failed for {ent.get('name_ja')!r}: {e}")
                skipped += 1

        # Fourth-transform tags
        ft_count = 0
        for name_ja, tags in FOURTH_TRANSFORM_TAGS.items():
            cid = name_to_id.get(name_ja)
            if not cid:
                print(f"[warn] no concept id for fourth-transform: {name_ja!r}")
                continue
            for tag in tags:
                try:
                    db.tag_fourth_transform(
                        cid,
                        axis=tag["axis"],
                        status=tag["status"],
                        rationale=tag.get("rationale"),
                        related_ai_phenomenon=tag.get("ai_phenomenon"),
                    )
                    ft_count += 1
                except LitDBError as e:
                    print(f"[error] tag failed for {name_ja!r}/{tag['axis']}: {e}")

        # Cross-domain links
        cd_count = 0
        for name_ja, target_db, link_type, target_name, desc in CROSS_DOMAIN_LINKS:
            cid = name_to_id.get(name_ja)
            if not cid:
                print(f"[warn] no concept id for cross-domain: {name_ja!r}")
                continue
            try:
                db.insert_cross_domain(
                    lit_entity_type="concept",
                    lit_entity_id=cid,
                    target_db=target_db,
                    link_type=link_type,
                    target_entity_name=target_name,
                    description=desc,
                )
                cd_count += 1
            except LitDBError as e:
                print(f"[error] cross-domain failed for {name_ja!r}: {e}")

        print(f"\n=== C25 Latin American Early (Colonial-19c) completed ===")
        print(f"  concepts inserted: {inserted} (skipped: {skipped})")
        print(f"  fourth-transform tags: {ft_count}")
        print(f"  cross-domain links: {cd_count}")
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 16"
        ).fetchone()
        print(f"  total concepts in subfield 16: {row['c']}")


if __name__ == "__main__":
    main()
