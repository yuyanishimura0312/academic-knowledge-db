"""
LIT-DB Phase 2 — C26 Wave3: Latin American Literature (ラテンアメリカ文学)
==========================================================================
Inserts 40 representative concepts spanning 5 categories:
  A. モデルニスモ (8)
  B. ブーム期主要作家概念 (8)
  C. 主要主題 (8)
  D. ポスト・ブーム (8)
  E. 理論・批評概念 (8)

subfield_id=16, code='lit_latin_america', region='グローバルサウス'

Sources: Cervantes Virtual (Biblioteca Virtual Miguel de Cervantes),
Memoria Chilena, Casa de las Américas, JSTOR-listed canonical entries,
Wikipedia (Spanish/English/Portuguese) for canonical concept entries.
"""
from __future__ import annotations

from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("モデルニスモ期", "Modernismo (Spanish American)", 1880, 1916,
     "ルベン・ダリオ『Azul...』(1888)を起点とするスペイン語圏中南米のモデルニスモ。"
     "パルナシスム・サンボリスム影響下、独自の美学を確立。"),
    ("ブラジル・モデルニスモ期", "Brazilian Modernismo", 1922, 1945,
     "1922年サンパウロ近代芸術週間を起点とするブラジル独自のモデルニスモ。"
     "Mário/Oswald de Andradeらが主導しブラジル性の探求と前衛的形式実験を結合。"),
    ("リージョナリスモ・先駆期", "Regionalist / Pre-Boom", 1920, 1949,
     "クリオジスモ・先駆的インディヘニスモ・大地小説の時代。アストゥリアス・カルペンティエルら。"),
    ("ブーム期", "Boom Period", 1960, 1975,
     "García Márquez・Cortázar・Vargas Llosa・Fuentesらによる小説革新の黄金期。"
     "魔術的リアリズム・全体小説・開放小説の概念が成立。"),
    ("ポスト・ブーム期", "Post-Boom", 1975, 2000,
     "ブーム期の継承と批判から派生する複数潮流。"
     "女性作家の台頭、testimonio、neopolicial、McOndoなどの諸運動。"),
    ("現代ラテンアメリカ文学期", "Contemporary Latin American", 2000, 2025,
     "Bolaño以後のグローバル化文学。先住民系・メスティーソ作家の国際的展開。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — モデルニスモ (8)
# ===============================================================

add({
    "name_ja": "モデルニスモ（イスパノアメリカ）",
    "name_en": "modernismo hispánico",
    "name_original": "modernismo hispanoamericano",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "モデルニスモ期",
    "definition": "ルベン・ダリオ『Azul...』(1888)を起点とする19世紀末から20世紀初頭の"
                  "スペイン語圏中南米における詩・散文の革新運動。フランス・パルナシスム"
                  "とサンボリスムを摂取しつつ、コスモポリタンな美学とラテンアメリカの自"
                  "立的文学アイデンティティを同時に追求した、ラテンアメリカ発の最初の世界的文学運動。",
    "background": "19世紀末のラテンアメリカ独立国家形成・近代化と、フランス文学受容を背景に成立。",
    "development": "ホセ・マルティ・グティエレス・ナヘラの先駆を経てダリオに結実、"
                   "ロドー『Ariel』など散文にも展開、98年世代スペイン文学にも逆流的影響を与えた。",
    "historical_context": "ラテンアメリカが文学的に「中心」へと能動的に介入した最初の運動。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/modernismo_hispanoamericano/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 専用ポータル",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ルベン・ダリオ",
    "name_en": "Rubén Darío",
    "name_original": "Rubén Darío",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "モデルニスモ期",
    "definition": "ニカラグア生まれの詩人(1867-1916)、本名Félix Rubén García Sarmiento。"
                  "『Azul...』(1888)『Prosas profanas』(1896)『Cantos de vida y esperanza』(1905)"
                  "によりスペイン語詩を根底から刷新し、モデルニスモの中心人物として"
                  "「padre del modernismo」と称される。",
    "background": "中米・チリ・アルゼンチン・スペインを移動する離散的詩人として国境横断的活動を展開。",
    "development": "外交官として欧州駐在、ヴェルレーヌ・ユゴーらと交流、後期は反米的政治詩を執筆。",
    "historical_context": "ラテンアメリカ詩人がスペイン語圏全体の規範形成主体となった最初の事例。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/ruben_dario/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "『Azul...』（青...）",
    "name_en": "Azul...",
    "name_original": "Azul...",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "モデルニスモ期",
    "definition": "ルベン・ダリオがチリ・バルパライソで1888年に出版した詩・散文集。"
                  "詩篇と短編散文を組み合わせる構成と、青色を象徴とする"
                  "コスモポリタン的・夢想的美学により、モデルニスモの開幕を告げた金字塔。"
                  "スペインの批評家フアン・バレラの賛辞によりスペイン本国にも逆輸入された。",
    "background": "ダリオがチリ滞在時に執筆、ヴィクトル・ユゴーらフランス文学の影響を強く受ける。",
    "development": "1890年第二版でさらに詩篇追加、スペイン本国の批評家を通じて欧州に逆流。",
    "historical_context": "ラテンアメリカ発の文学革新がスペイン本国を変革した象徴的事件。",
    "primary_source_url": "https://www.cervantesvirtual.com/obra/azul--0/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes 全文",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "パルナシスム・サンボリスム影響",
    "name_en": "Parnassian and Symbolist influence",
    "name_original": "influencia parnasiana y simbolista",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "モデルニスモ期",
    "definition": "モデルニスモを規定するフランス詩二大潮流の影響関係。"
                  "テオフィル・ゴーティエ・ルコント・ド・リール由来の彫琢された形式美と、"
                  "ヴェルレーヌ・マラルメ由来の音楽性・象徴性を、モデルニスモ詩人たちは"
                  "創造的にアメリカ的素材へと接続し、独自の融合美学を生んだ。",
    "background": "1880年代末のフランス文学雑誌のラテンアメリカ流通が直接影響経路を作った。",
    "development": "Casal・Silva・Lugonesらが各自の方向で受容を展開した。",
    "historical_context": "影響受容の主体性をめぐるラテンアメリカ批評の出発点。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/modernismo_hispanoamericano/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "シンボリスモ・ラテンアメリカ版",
    "name_en": "Latin American Symbolism",
    "name_original": "simbolismo latinoamericano",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "モデルニスモ期",
    "definition": "フランス象徴主義をモデルニスモの核として消化したラテンアメリカ独自の象徴詩。"
                  "ホセ・アスンシオン・シルバ(コロンビア)の『Nocturno』、"
                  "フリアン・デル・カサル(キューバ)の青ざめた美意識など、"
                  "音楽性・神秘・暗示を核としつつ熱帯やカリブ的素材と結合した。",
    "background": "ヴェルレーヌ・マラルメへの直接的傾倒と独自的解釈の融合。",
    "development": "後期モデルニスモのHerrera y Reissig(ウルグアイ)が極限的に展開。",
    "historical_context": "ラテンアメリカ詩の音楽性追求の起源として後続詩人にも継承された。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/jose_asuncion_silva/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "Casa de las Américas（アメリカの家）",
    "name_en": "Casa de las Américas",
    "name_original": "Casa de las Américas",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "1959年キューバ革命直後にハバナで設立されたラテンアメリカ文化機関。"
                  "Haydée Santamaríaが初代館長を務め、年次のCasa de las Américas賞"
                  "(1960-)はラテンアメリカ全域の作家を発掘し、ブーム期作家ネットワーク"
                  "形成の中心装置となった。同名雑誌は批評の主要場でもある。",
    "background": "革命キューバの文化外交として、汎ラテンアメリカ的連帯を制度化した。",
    "development": "1971年Padilla事件でブーム作家の一部と決別、後も主要文学賞として存続。",
    "historical_context": "ブーム期文学制度化の決定的拠点であり政治と文学の交差点。",
    "primary_source_url": "https://www.casadelasamericas.org/",
    "primary_source_type": "Casa de las Américas 公式",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ブラジル・モデルニズモ",
    "name_en": "Brazilian Modernismo",
    "name_original": "Modernismo brasileiro",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブラジル・モデルニスモ期",
    "definition": "1922年サンパウロ近代芸術週間(Semana de Arte Moderna)を起点とする"
                  "ブラジル独自のモデルニズモ運動。スペイン語圏のモデルニスモとは異質で、"
                  "むしろ前衛(モダニズム)に近く、Mário de Andrade・Oswald de Andrade・"
                  "Manuel Bandeiraらがブラジル性の探求と形式革新を結合した。",
    "background": "20世紀初頭の欧州前衛(キュビスム・未来派)受容と国民文化形成要請の交差。",
    "development": "Antropofagia宣言(1928)・Mário『Macunaíma』(1928)など多様な展開。",
    "historical_context": "ブラジル20世紀文学の出発点であり後続全潮流の原点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Modernismo_(Brazilian_literary_movement)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "クリオジスモ",
    "name_en": "criollismo",
    "name_original": "criollismo",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "リージョナリスモ・先駆期",
    "definition": "20世紀前半のラテンアメリカで、土着のクリオージョ(植民地生まれ白人系)文化・"
                  "風土・人々を中心に描いた地域主義文学運動。Rómulo Gallegos『Doña Bárbara』"
                  "(1929)・Ricardo Güiraldes『Don Segundo Sombra』(1926)など、"
                  "大地小説(novela de la tierra)を通じてラテンアメリカ的本質の表象を試みた。",
    "background": "モデルニスモのコスモポリタニズムへの反動として土着志向が強まった。",
    "development": "ブーム期作家により批判的に乗り越えられたが、地域性表象の伝統を残した。",
    "historical_context": "国民文学形成の中核となった先住民・農村・カウボーイ表象の制度化。",
    "primary_source_url": "https://es.wikipedia.org/wiki/Criollismo",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "先駆的インディヘニスモ",
    "name_en": "indigenismo (precursor)",
    "name_original": "indigenismo precursor",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "リージョナリスモ・先駆期",
    "definition": "20世紀前半のアンデス諸国(ペルー・エクアドル・ボリビア)を中心とする"
                  "先住民問題を主題化した文学運動。Clorinda Matto de Turner『Aves sin nido』"
                  "(1889)を先駆としJorge Icaza『Huasipungo』(1934)・Ciro Alegría"
                  "『El mundo es ancho y ajeno』(1941)が代表作。"
                  "Mariáteguiの社会主義的解釈と結合し、先住民復権の文学的基盤を築いた。",
    "background": "19世紀末から20世紀初頭の先住民系農民革命運動と知識人の連帯を背景にする。",
    "development": "後にArguedasのネオ・インディヘニスモへ進化、現代の先住民系作家による"
                   "「自己代弁」の段階へと展開した。",
    "historical_context": "ラテンアメリカ文学が「他者代弁」の倫理問題を最初に提起した運動。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Indigenismo",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY B — ブーム期主要作家概念 (8)
# ===============================================================

add({
    "name_ja": "魔術的リアリズム",
    "name_en": "magical realism",
    "name_original": "realismo mágico",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "ラテンアメリカ・ブーム期文学を世界的に定義した文学的手法・概念。"
                  "García Márquez『Cien años de soledad』(1967)が最も普及した代表作で、"
                  "日常的現実のなかに不思議・超自然・神話的要素を違和感なく統合する。"
                  "用語は1925年Franz Roh(独)の絵画論に由来し、Ángel Floresが1955年に文学批評に転用、"
                  "ブーム期にラテンアメリカ的様式として国際的ブランドとなった。",
    "background": "ヨーロッパ的リアリズムでは捉えきれないラテンアメリカの混淆的現実を表象する必要から発達。",
    "development": "Allende・Rushdieらラテンアメリカ外作家にも継承されグローバルな様式となった。",
    "historical_context": "ラテンアメリカが世界文学の規範形成主体となった画期的事象。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Magic_realism",
    "primary_source_type": "Wikipedia canonical entry / 学術書誌",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "lo real maravilloso（驚異的現実）",
    "name_en": "the marvelous real",
    "name_original": "lo real maravilloso",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "アレホ・カルペンティエル(キューバ)が1949年小説『El reino de este mundo』"
                  "の序文で提唱した概念。シュルレアリスムの「人為的驚異」と対比的に、"
                  "アメリカ大陸そのものに内在する地理・歴史・文化的混淆性が産む"
                  "「現実そのものの驚異」を文学化する立場。魔術的リアリズムと近接するが"
                  "存在論的差異を主張する点で区別される。",
    "background": "ハイチ訪問時にカルペンティエルが感じた歴史的・自然的驚異が出発点。",
    "development": "魔術的リアリズム概念と混同・対立しつつカリブ・中米作家に継承された。",
    "historical_context": "ヨーロッパ前衛(シュルレアリスム)に対抗するラテンアメリカ独自の存在論宣言。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Lo_real_maravilloso",
    "primary_source_type": "Wikipedia canonical entry / 序文一次資料",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ボルヘス的迷宮",
    "name_en": "Borgesian labyrinth",
    "name_original": "el laberinto borgeano",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "リージョナリスモ・先駆期",
    "definition": "ホルヘ・ルイス・ボルヘス(アルゼンチン1899-1986)の"
                  "短編集『Ficciones』(1944)『El Aleph』(1949)に頻出するモチーフ概念。"
                  "迷宮・無限図書館(『La biblioteca de Babel』)・分岐する庭・"
                  "鏡・地図など、無限と再帰の構造を通じて現実・虚構・知識の境界を撹乱する。"
                  "ポストモダン文学の先駆として世界文学に決定的影響を与えた。",
    "background": "アルゼンチン国立図書館長としての書物世界への内在と独自の哲学的読書から生成。",
    "development": "Foucault・Eco・Calvinoらヨーロッパ思想家・作家に直接影響、ハイパーテクスト理論の先駆。",
    "historical_context": "ラテンアメリカが20世紀世界文学の最深部に達した到達点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Jorge_Luis_Borges",
    "primary_source_type": "Wikipedia canonical entry / 全集",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "Rayuela（石蹴り遊び）／開放小説",
    "name_en": "Hopscotch / open novel",
    "name_original": "Rayuela",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "フリオ・コルタサル(アルゼンチン)が1963年に発表した小説。"
                  "通常順読み(1-56章)と作者提示の「跳躍」順(73章から始まる別順序)の"
                  "二通りの読みを許容する開放的構造を持ち、読者を能動的協働者とする"
                  "「開放小説(novela abierta)」の代表例。"
                  "後のハイパーテクスト・インタラクティブフィクション理論の先駆。",
    "background": "パリ亡命中のコルタサルがシュルレアリスム・ジャズ即興と影響交差させて構想。",
    "development": "ブーム期の小説形式革新の頂点として国際的に受容された。",
    "historical_context": "読者の能動性を作品成立条件に組み込む読書理論の文学的実践。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Hopscotch_(Cort%C3%A1zar_novel)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "全体小説（novela total）",
    "name_en": "total novel",
    "name_original": "novela total",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "マリオ・バルガス・リョサ(ペルー)が提唱した小説概念。"
                  "社会・歴史・心理・神話・形式実験の全層を一つの小説に統合する野心的構想で、"
                  "Vargas Llosa『La casa verde』(1966)『Conversación en La Catedral』(1969)"
                  "が代表的実践。フローベール論『La orgía perpetua』(1975)で理論化された。",
    "background": "19世紀写実主義の野心(バルザック・トルストイ)を20世紀的形式革新で更新する企図。",
    "development": "Fuentes『Terra Nostra』Lezama『Paradiso』など同時代他作家にも構造類似が見られる。",
    "historical_context": "ブーム期の野心の象徴的概念であり後続作家からの批判の主要対象でもある。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mario_Vargas_Llosa",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "サンタ・マリア（Onetti架空都市）",
    "name_en": "Santa María (Onetti's fictional city)",
    "name_original": "Santa María",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "フアン・カルロス・オネッティ(ウルグアイ)が複数小説で展開した架空都市。"
                  "『La vida breve』(1950)で創造され『El astillero』(1961)"
                  "『Juntacadáveres』(1964)など連作的に展開。閉塞・退廃・絶望を"
                  "実存主義的文学空間として構築し、ラテンアメリカ文学の暗部を代表する。"
                  "García Márquezのマコンドの先駆と位置づけられる。",
    "background": "ファウルキナーのヨクナパトーファ郡から学んだ架空地誌の手法。",
    "development": "後続作家の架空都市創造(マコンド・コマラ等)の規範となった。",
    "historical_context": "ラテンアメリカ・モダニズム小説の到達点として再評価された。",
    "primary_source_url": "https://es.wikipedia.org/wiki/Juan_Carlos_Onetti",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "Terra Nostra（テラ・ノストラ）",
    "name_en": "Terra Nostra",
    "name_original": "Terra Nostra",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "カルロス・フエンテス(メキシコ)が1975年に発表した大著小説。"
                  "16世紀スペイン・フェリペ2世のエル・エスコリアル建設を中核に、"
                  "古代ローマから20世紀末パリまでをスペイン・ヨーロッパ・新大陸を貫く"
                  "壮大な歴史的・神話的網目として再構築。Romulo Gallegos賞受賞。"
                  "全体小説の野心の極限的事例。",
    "background": "メキシコ・スペイン・ヨーロッパ複層的アイデンティティ探求の集大成。",
    "development": "ハロルド・ブルーム『The Western Canon』にも収録された世界文学正典。",
    "historical_context": "ブーム期最大野心作の一つでスペイン語圏百年戦争的歴史小説の頂点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Terra_Nostra_(novel)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ネオ・バロック（Lezama Lima）",
    "name_en": "neo-baroque",
    "name_original": "neobarroco",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "ホセ・レサマ・リマ(キューバ1910-76)が雑誌『Orígenes』を中心に展開した"
                  "ラテンアメリカ独自のバロック詩学。17世紀スペイン・バロック(Góngora)を"
                  "アメリカ大陸の混淆性へと変換し、過剰な比喩・蛇行する構文・百科全書的引用を特徴とする。"
                  "代表作『Paradiso』(1966)。Severo Sarduyらにより理論化された。",
    "background": "アメリカ的混血性をバロック的「不均衡な隆起」として理論化する企図。",
    "development": "Sarduy『Barroco』(1974)で理論化、ポストモダニズムの先駆として再評価された。",
    "historical_context": "ヨーロッパ的「明晰さ」とは異質なラテンアメリカ的詩学の宣言。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Jos%C3%A9_Lezama_Lima",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY C — 主要主題 (8)
# ===============================================================

add({
    "name_ja": "孤独（soledad）",
    "name_en": "solitude",
    "name_original": "soledad",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "ガブリエル・ガルシア・マルケスのノーベル賞受賞講演"
                  "『La soledad de América Latina』(1982)で集大成された主題。"
                  "『Cien años de soledad』(1967)を頂点に、植民地化・独裁・貧困・"
                  "西欧的眼差しからの疎外として「ラテンアメリカ的孤独」を意味する。"
                  "個人的・歴史的・地政学的孤独が重層的に表象される。",
    "background": "コロンビアの内戦・千日戦争・暴力期(La Violencia)の集合的経験から発生。",
    "development": "Octavio Paz『El laberinto de la soledad』(1950)など他作家にも変奏。",
    "historical_context": "ラテンアメリカ文学を世界的に特徴づけた主要トポス。",
    "primary_source_url": "https://www.nobelprize.org/prizes/literature/1982/marquez/lecture/",
    "primary_source_type": "Nobel Prize 公式 (一次資料)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ラテンアメリカ的アイデンティティ",
    "name_en": "Latin American identity",
    "name_original": "identidad latinoamericana",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "ラテンアメリカ文学の根本主題で、独立(19世紀初頭)以後の"
                  "「我々は何者か」をめぐる連続的問い。Sarmiento『Facundo』(1845)の"
                  "「文明か野蛮か」二項対立から、Paz『El laberinto de la soledad』(1950)の"
                  "メキシコ性論、Fuentes『La nueva novela hispanoamericana』(1969)の"
                  "ブーム期文学的アイデンティティ論まで継続する主題系。",
    "background": "脱植民地後の国民国家形成と西欧中心主義への抵抗の二重要請。",
    "development": "現代ではグローバル化・移動性の中で再構築されている。",
    "historical_context": "ラテンアメリカ知識人の200年的問題系。",
    "primary_source_url": "https://www.cervantesvirtual.com/portales/octavio_paz/",
    "primary_source_type": "Biblioteca Virtual Miguel de Cervantes",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "メスティサヘ（混血性）",
    "name_en": "mestizaje",
    "name_original": "mestizaje",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "リージョナリスモ・先駆期",
    "definition": "ラテンアメリカ・カリブにおける人種・文化混淆過程および理論概念。"
                  "José Vasconcelos『La raza cósmica』(1925)が美学的に肯定、"
                  "Inca Garcilaso de la Vega(17世紀)を先駆とする系譜を持つ。"
                  "現代ではAnzaldúa『Borderlands』のmestiza consciousness、"
                  "Glissantのcréolizationなど批判的再構築が進む。",
    "background": "植民地期の人種カテゴリ(casta)体系から脱植民地的に転回した概念。",
    "development": "白人支配的バイアスを批判するdecolonial理論で再検討される。",
    "historical_context": "ラテンアメリカ存在論の核心概念であり論争の中心。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mestizaje",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "独裁者文学",
    "name_en": "dictator novel",
    "name_original": "novela del dictador",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "ラテンアメリカの独裁政権を主題化したサブジャンル。"
                  "Asturias『El Señor Presidente』(1946)を先駆とし、"
                  "Carpentier『El recurso del método』(1974)、"
                  "García Márquez『El otoño del patriarca』(1975)、"
                  "Roa Bastos『Yo el Supremo』(1974)、Vargas Llosa『La fiesta del Chivo』(2000)"
                  "など多数作品を含む。権力・暴力・神格化を文学的に解剖する。",
    "background": "20世紀ラテンアメリカの軍事独裁・カウディジョ政治の社会的経験。",
    "development": "1970年代に集中的に展開、ポスト・ブームでも継承される。",
    "historical_context": "ラテンアメリカ政治史と文学創造の最深の絡みつき。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Dictator_novel",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "亡命（exilio）",
    "name_en": "exile",
    "name_original": "exilio",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "ラテンアメリカ20世紀史を貫く根本主題。"
                  "Cortázarのパリ亡命、García Márquezのメキシコ滞在、"
                  "南米軍政期(1970-80年代)のチリ・アルゼンチン・ウルグアイ作家亡命、"
                  "ベネズエラ近年の大量出国まで連続する。"
                  "亡命作家の身体的離散と作品内表象が複雑に絡む文学現象。",
    "background": "独裁・革命・経済危機が連鎖する20世紀ラテンアメリカの政治的不安定。",
    "development": "Bolaño・Skármetaらポスト・ブーム作家の主要主題となった。",
    "historical_context": "ラテンアメリカ文学を本質的にトランスナショナルなものにする条件。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Latin_American_exile_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "歴史的記憶（memoria histórica）",
    "name_en": "historical memory",
    "name_original": "memoria histórica",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "南米軍政期(チリ・アルゼンチン・ウルグアイ)の人権侵害・失踪者問題に対する"
                  "文学的・社会的応答として発達した主題系。"
                  "Diamela Eltit・Roberto Bolaño・Carlos Liscanoらの作品で前景化。"
                  "公式記憶と対抗記憶の闘争、子供から見た独裁の経験(Alejandro Zambra)など"
                  "新たな主題的展開を見せ続けている。",
    "background": "1980-90年代の民主化過程と人権運動が文学的に応答した結果として発達。",
    "development": "現代スペイン語圏文学の主要関心の一つとして継続。",
    "historical_context": "国家暴力の文学的処理という普遍的問題のラテンアメリカ的実装。",
    "primary_source_url": "https://www.memoriachilena.gob.cl/",
    "primary_source_type": "Memoria Chilena (国立図書館 公式)",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "暴力小説（novela de la violencia）",
    "name_en": "novel of violence",
    "name_original": "novela de la violencia",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "コロンビアのLa Violencia(1948-58)以後を主題化する小説群を起点とし、"
                  "現代では麻薬戦争・武装紛争・都市暴力を扱うジャンル全般を指す。"
                  "Fernando Vallejo『La virgen de los sicarios』(1994)、"
                  "Yuri Herrera『Trabajos del reino』(2004)、"
                  "Fernanda Melchor『Temporada de huracanes』(2017)など継承する。",
    "background": "コロンビア両党派暴力期La Violenciaの集合的トラウマと現代暴力の連続。",
    "development": "narcoliteratura(麻薬文学)というサブジャンルへ展開した。",
    "historical_context": "ラテンアメリカ社会暴力の文学的解剖の伝統。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Narcoliterature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "コレラの時代の愛",
    "name_en": "Love in the Time of Cholera",
    "name_original": "El amor en los tiempos del cólera",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "ガブリエル・ガルシア・マルケス(コロンビア)が1985年に発表した小説。"
                  "カリブ海岸都市での50年以上にわたる愛の物語を、"
                  "コレラ流行と老いと記憶を絡めて描く。"
                  "ノーベル賞受賞(1982)後のマルケスの代表作で、"
                  "ブーム期の魔術的リアリズムから抒情的・現実主義的方向への転換を示す。",
    "background": "両親の恋愛史を素材に、晩年期の愛と時間の主題を探求した。",
    "development": "マイク・ニューウェル監督の映画化(2007)で世界的普及。",
    "historical_context": "晩期マルケス文学の代表作として正典化された。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Love_in_the_Time_of_Cholera",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY D — ポスト・ブーム (8)
# ===============================================================

add({
    "name_ja": "ポスト・ブーム",
    "name_en": "post-Boom",
    "name_original": "post-Boom",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "1975年頃以後のブーム後ラテンアメリカ文学の総称的批評概念。"
                  "Donald Shawらが理論化、ブーム期の野心的形式実験から"
                  "「読みやすさ」「ポピュラー文化への接近」「女性作家の台頭」"
                  "「政治的より個人的主題への移行」「メロドラマの再評価」などを特徴とする。"
                  "Allende・Skármeta・Puigらが代表作家。",
    "background": "ブーム期実験への読者反発と新世代作家の独自性追求の合流。",
    "development": "1990年代以降McOndo・Crackなど新たな反動運動を生み出した。",
    "historical_context": "ブームの「父殺し」と新世代の自己定立の試み。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Post-Boom",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "McOndo運動",
    "name_en": "McOndo movement",
    "name_original": "McOndo",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "1996年Alberto Fuguet(チリ)・Sergio Gómez編の短編集"
                  "『McOndo』に由来する文学運動。マコンド(García Márquez的魔術的村)を"
                  "Mac+condoとして都市・グローバル・消費文化的に書き換える命名。"
                  "魔術的リアリズムの呪縛を断ち、グローバル消費都市文化を等身大に描く"
                  "新世代作家の宣言として機能した。",
    "background": "ブーム期魔術的リアリズムの世界的ステレオタイプ化への反発。",
    "development": "Fuguet・Edmundo Paz Soldán・Rodrigo Fresánらが展開した。",
    "historical_context": "ラテンアメリカ文学のグローバル化への自覚的応答。",
    "primary_source_url": "https://en.wikipedia.org/wiki/McOndo",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "Crack世代",
    "name_en": "Generación del Crack",
    "name_original": "Generación del Crack",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "1996年メキシコシティの作家集団による文学運動。"
                  "Jorge Volpi・Ignacio Padilla・Eloy Urroz・Pedro Ángel Palou・"
                  "Ricardo Chávez Castañedaらが同時に「Crack宣言」を発表。"
                  "ブーム期の野心的全体小説的小説への回帰を主張し、"
                  "ローカル主義(criollismo)・魔術的リアリズム双方への対抗を企図した。",
    "background": "メキシコ文学の世界化への自覚と地域主義への反発。",
    "development": "Volpi『En busca de Klingsor』(1999)が国際的成功を収めた。",
    "historical_context": "McOndoとともに1990年代後半の世代的自己定立を象徴する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Crack_Movement",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "Roberto Bolaño『2666』",
    "name_en": "Roberto Bolaño's 2666",
    "name_original": "2666",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "現代ラテンアメリカ文学期",
    "definition": "ロベルト・ボラーニョ(チリ1953-2003)が遺作として2004年に出版した5部構成の大作。"
                  "メキシコ国境都市Santa Teresa(実在のCiudad Juárezをモデル)での"
                  "女性連続殺人事件を中核に、文学批評家・哲学者・ジャーナリスト・ナチス時代の作家を"
                  "結ぶ網目を描く。21世紀ラテンアメリカ文学の最高峰として国際的正典に登録された。",
    "background": "Bolaño晩年の癌闘病中に書かれた死との競争の作品。",
    "development": "英訳出版(2008)後、世界文学の頂点と認定された。",
    "historical_context": "ブーム以後のラテンアメリカ文学の世界的再正典化を象徴する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/2666",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ネオポリシアル",
    "name_en": "Latin American neopolicial",
    "name_original": "neopolicial latinoamericano",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "1970-80年代に北米ハードボイルド推理小説の影響を受けつつ、"
                  "ラテンアメリカ社会の腐敗・暴力・権力構造を解剖する独自の犯罪小説潮流。"
                  "Paco Ignacio Taibo II(メキシコ)『Sombra de la sombra』、"
                  "Leonardo Padura(キューバ)Mario Conde 4部作、"
                  "Ricardo Piglia(アルゼンチン)『Plata quemada』らが代表作家。",
    "background": "アメリカ・ハードボイルドの社会批判精神とラテンアメリカ独裁経験の接合。",
    "development": "Bolaño『Estrella distante』も同潮流の影響を受ける。",
    "historical_context": "ジャンル文学が社会批判的高文学と接続した革新的事例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Neopolicial",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "テスティモニオ文学",
    "name_en": "testimonio literature",
    "name_original": "testimonio",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "1960-80年代のラテンアメリカで発達した、"
                  "周縁化された人物(先住民・農民・革命家・受刑者)の口述証言を"
                  "知識人・編者が書き起こす文学ジャンル。"
                  "Miguel Barnet『Biografía de un cimarrón』(1966)が先駆、"
                  "Rigoberta Menchú/Elisabeth Burgos『Me llamo Rigoberta Menchú』(1983)が代表作。"
                  "1986年Casa de las Américas賞にtestimonio部門が新設された。",
    "background": "キューバ革命以後の左派文化運動と人類学・民族誌的方法の交差で発達。",
    "development": "1990年代Rigoberta Menchú論争(David Stoll)で真正性問題に直面した。",
    "historical_context": "他者代弁の倫理問題を最も先鋭的に提起したジャンル。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Testimonio",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "女性作家の台頭",
    "name_en": "rise of women writers",
    "name_original": "auge de las escritoras",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "1980年代以後のラテンアメリカ女性作家の決定的台頭。"
                  "Isabel Allende『La casa de los espíritus』(1982)を世界的成功の起点とし、"
                  "Ángeles Mastretta(メキシコ)『Arráncame la vida』(1985)、"
                  "Laura Restrepo(コロンビア)『Delirio』、"
                  "Diamela Eltit(チリ)、Cristina Peri Rossi(ウルグアイ)らが多様な声を確立。"
                  "ブーム期男性中心正典への重要な修正となった。",
    "background": "第二波フェミニズムと民主化過程が交差した1980年代の社会変動。",
    "development": "21世紀のValeria Luiselli・Samanta Schweblin・Mariana Enríquezらに継承された。",
    "historical_context": "ラテンアメリカ正典のジェンダー的再構築の決定的契機。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Latin_American_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "先住民・メスティーソ文学",
    "name_en": "indigenous-mestizo literature",
    "name_original": "literatura indígena-mestiza",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "20世紀後半以後の、先住民系・メスティーソ作家による自己代弁的文学運動。"
                  "José María Arguedas(ペルー)『Los ríos profundos』(1958)を先駆として、"
                  "Humberto Ak'abalマヤ・キチェ詩、Natalio Hernández・"
                  "Briceida Cuevasナワトル・マヤ詩、Luis de Lión(グアテマラ)など、"
                  "二言語(先住民語+スペイン語)実践と独自の文学性を確立する。",
    "background": "20世紀インディヘニスモが代弁構造を批判される過程で内発的代弁が興隆。",
    "development": "21世紀には国際的な先住民文学ネットワークと連動した。",
    "historical_context": "ラテンアメリカ文学の存在論的境界の根本的拡大。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Indigenous_literatures_in_the_Americas",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY E — 理論・批評概念 (8)
# ===============================================================

add({
    "name_ja": "コミットメント文学（literatura comprometida）",
    "name_en": "committed literature",
    "name_original": "literatura comprometida",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "サルトルの「engagement」をラテンアメリカ的に翻訳・実装した文学倫理概念。"
                  "1960年代キューバ革命以後のラテンアメリカ知識人にとって、"
                  "文学創造は政治的責任と不可分とされた。"
                  "Roque Dalton・Mario Benedetti・Eduardo Galeanoらが代表する立場で、"
                  "Casa de las Américas等を制度的拠点として展開した。",
    "background": "サルトル『文学とは何か』(1947)受容と冷戦下ラテンアメリカ革命運動の交差。",
    "development": "1971年Padilla事件以後の知識人分裂を契機に多元化した。",
    "historical_context": "ラテンアメリカ文学の倫理的・政治的最高水準の議論。",
    "primary_source_url": "https://www.casadelasamericas.org/",
    "primary_source_type": "Casa de las Américas 公式",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "transculturación（文化越境化）",
    "name_en": "transculturation",
    "name_original": "transculturación",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "Fernando Ortiz(キューバ)が『Contrapunteo cubano del tabaco y el azúcar』"
                  "(1940)で提唱、Ángel Rama(ウルグアイ)が『Transculturación narrativa en "
                  "América Latina』(1982)で文学批評概念へ拡張。"
                  "「acculturation(同化)」を批判し、文化接触における能動的変容と新生を強調する。"
                  "Arguedasらの「文化越境的物語作家」概念で実装される。",
    "background": "西欧中心主義的文化変容論を脱植民地視点から批判する企図。",
    "development": "ポストコロニアル理論と接続し国際的に流通した。",
    "historical_context": "ラテンアメリカ発の世界的影響力を持つ批評概念。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Transculturation",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "文化的異質性（heterogeneidad cultural）",
    "name_en": "cultural heterogeneity",
    "name_original": "heterogeneidad cultural",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "アントニオ・コルネホ・ポラール(ペルー1936-97)が提唱した批評概念。"
                  "transculturaciónの「融合」志向への批判として、"
                  "ラテンアメリカ社会に複数の生産主体・受容主体・社会的指示が"
                  "非対称的に併存する状況を強調する。"
                  "『Escribir en el aire』(1994)で集大成された。",
    "background": "アンデス諸国の口承文化と都市知識人文化の根本的非対称性が出発点。",
    "development": "Mignoloの「border thinking」など脱植民地思考に継承された。",
    "historical_context": "ラテンアメリカ批評理論の脱植民地的転回の中心概念。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Antonio_Cornejo_Polar",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "脱植民地批評",
    "name_en": "decolonial criticism",
    "name_original": "crítica decolonial",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "現代ラテンアメリカ文学期",
    "definition": "Aníbal Quijano(ペルー)『Colonialidad del poder』(2000)を起点に、"
                  "Walter Mignolo・Enrique Dussel・Catherine Walshらが構築した"
                  "ラテンアメリカ独自の批判理論。"
                  "ポストコロニアル批評(英語圏)を超えて、"
                  "近代/植民地性のmatriz(母型)そのものを問題化する。"
                  "文学批評ではEpistemic disobedience概念で正典問題を再構築する。",
    "background": "modernity/coloniality研究グループの汎ラテンアメリカ的協働で発達。",
    "development": "21世紀に英語圏アカデミアにも逆流的影響を持つようになった。",
    "historical_context": "ラテンアメリカ思想の世界批評理論への独自貢献。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Decoloniality",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "魔術的リアリズム論争",
    "name_en": "magic realism debate",
    "name_original": "debate del realismo mágico",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "1980年代以後の魔術的リアリズム概念をめぐる激しい批評論争。"
                  "(1)概念の理論的曖昧性、(2)国際市場が要求するエキゾチシズムへの還元、"
                  "(3)ラテンアメリカ文学の多様性の単一概念への矮小化、"
                  "を主要争点とする。McOndo・Crack世代の宣言は本論争の文学的応答である。",
    "background": "ブーム作品の世界的成功が産んだステレオタイプ化への批判的応答として発達。",
    "development": "Roberto González Echevarría・Erna Pfeifferら多数の批評家が参戦。",
    "historical_context": "ラテンアメリカ文学の自己定義をめぐる持続的論争。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Magic_realism",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アントロポファジア（人食いブラジル）",
    "name_en": "anthropophagy",
    "name_original": "antropofagia",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブラジル・モデルニスモ期",
    "definition": "オズワルド・デ・アンドラーデ(ブラジル)が1928年『Manifesto Antropófago』"
                  "で発表した文化理論。トゥピ族の人食い儀礼をメタファーとして、"
                  "ヨーロッパ文化を批判的に「食べ尽くし」ブラジル独自に再生成する文化戦略を主張。"
                  "「Tupi or not Tupi, that is the question」が代表表現。"
                  "Tropicália運動・現代ブラジル文化の根本理論となった。",
    "background": "1920年代の汎欧州前衛運動とブラジル国民文化形成要請の創造的合流。",
    "development": "1960年代Tropicália、現代ブラジル映画・音楽の理論的基礎を提供する。",
    "historical_context": "ラテンアメリカ独自の影響受容理論として世界的影響を持つ。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Anthropophagic_Movement",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "辺境（frontera）",
    "name_en": "border / borderlands",
    "name_original": "frontera",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ポスト・ブーム期",
    "definition": "Gloria Anzaldúa『Borderlands/La Frontera』(1987)を中心とする批評概念。"
                  "メキシコ-米国国境を物理的・象徴的・心理的・言語的境界の重層体として理論化し、"
                  "「mestiza consciousness」「nepantla(中間状態)」など"
                  "境界に住む主体の独自認識様式を概念化した。"
                  "チカーノ文学の理論的基礎であり、ラテンアメリカ批評理論にも逆流影響した。",
    "background": "20世紀後半メキシコ系移民の経験と第三波フェミニズムの交差で発達。",
    "development": "Néstor García Canclini『Culturas híbridas』(1990)など接続概念群を生成。",
    "historical_context": "ラテンアメリカ文学の地理的・言語的境界の根本的再定義。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Borderlands/La_Frontera:_The_New_Mestiza",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "the marvelous real（驚異的現実 批評概念）",
    "name_en": "the marvelous real (critical concept)",
    "name_original": "lo real maravilloso (concepto crítico)",
    "original_script": "roman",
    "subfield_code": "lit_latin_america",
    "region": "グローバルサウス",
    "period_key": "ブーム期",
    "definition": "lo real maravilloso(驚異的現実)を批評概念として理論化したIrlemar Chiampi"
                  "『O realismo maravilhoso』(1980)・Roberto González Echevarría"
                  "『The Voice of the Masters』(1985)等の批評的展開。"
                  "魔術的リアリズム概念との相互関係・差異・系譜を厳密に論究する潮流で、"
                  "現代ラテンアメリカ批評の基礎概念枠組みの一つとなった。",
    "background": "Carpentier序文(1949)を出発点に、ブーム後批評が概念精緻化を進めた。",
    "development": "現代ラテンアメリカ文学批評の標準概念対として確立した。",
    "historical_context": "ラテンアメリカ批評理論の概念精緻化の代表事例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Lo_real_maravilloso",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ---------------------------------------------------------------
# Fourth-transform tagging (12 entries)
# ---------------------------------------------------------------
FOURTH_TRANSFORM_TAGS = {
    "魔術的リアリズム": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "西欧的リアリズムの「事実=現実」基準を脱構築し"
                       "「現実そのものに内在する驚異」を文学的真正性として再定立した魔術的リアリズムは、"
                       "AI生成テクストにおける真実性・事実性の境界変容と構造的に類比される。",
         "ai_phenomenon": "AI生成コンテンツが揺るがす事実/虚構の境界"},
    ],
    "テスティモニオ文学": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "周縁化された他者の声を編者が書き起こすtestimonioの主体構造は、"
                       "AI生成テクストにおける作者主体の分散・代弁構造と直接的に類比される。",
         "ai_phenomenon": "AI生成テクストにおける作者主体の分散と代弁構造"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "Rigoberta Menchú論争が提起した証言の真正性問題は、"
                       "AI生成証言・偽記憶・ディープフェイクの真正性危機と直接的に対応する。",
         "ai_phenomenon": "AI生成テクストの証言価値・真正性危機"},
    ],
    "transculturación（文化越境化）": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "文化接触における能動的変容を理論化したtransculturaciónは、"
                       "AI翻訳が産む文化変容の規模拡大とプロセス変質に直接適用される批評概念となる。",
         "ai_phenomenon": "AI翻訳がもたらす大規模文化越境化"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "文化越境的受容主体の能動性概念は、AI媒介受容における主体性の再構築に"
                       "再帰的に応用される。",
         "ai_phenomenon": "AI媒介文化受容における主体性の再構築"},
    ],
    "ボルヘス的迷宮": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "『La biblioteca de Babel』(1941)が予表する全ての可能なテクストを"
                       "含む無限図書館は、LLMの潜在テクスト空間と直接的に類比される"
                       "「LLMの予表」として再評価される。",
         "ai_phenomenon": "LLMの潜在テクスト空間としての無限図書館"},
        {"axis": "作者性", "status": "rethinking",
         "rationale": "『Pierre Menard』(1939)が示すテクストの再現と作者性の独立可能性は、"
                       "AI生成テクストの作者性問題の哲学的先駆として再評価される。",
         "ai_phenomenon": "AI生成テクストにおける作者性概念の脱構築"},
    ],
    "脱植民地批評": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "近代/植民地性の母型(matriz)を問題化する脱植民地批評は、"
                       "AI訓練データの植民地的偏向(英語・西欧中心主義)を批判的に照射する枠組みとなる。",
         "ai_phenomenon": "AI訓練データの植民地的偏向と知識生産の脱植民地化"},
    ],
    "アントロポファジア（人食いブラジル）": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "ヨーロッパ文化を「食べて」独自に再生成するantropofagiaは、"
                       "AI生成における学習データ消化と再生成プロセスの先駆的理論として再評価される。",
         "ai_phenomenon": "AI学習における学習データ消化と再生成"},
        {"axis": "翻訳", "status": "partial",
         "rationale": "アントロポファジア的「批判的食人」は影響受容を主体的変容過程として捉え、"
                       "AI翻訳が単純な等価変換ではなく文化的消化過程である点と部分的に対応する。",
         "ai_phenomenon": "AI翻訳の文化的消化過程"},
    ],
    "ネオ・バロック（Lezama Lima）": [
        {"axis": "創造性", "status": "partial",
         "rationale": "過剰な比喩・蛇行する構文・百科全書的引用を特徴とするneobarrocoの美学は、"
                       "LLMの語彙過剰生成・連鎖的引用生成の傾向と部分的に類比される。",
         "ai_phenomenon": "LLMの過剰生成傾向との類比"},
    ],
    "Roberto Bolaño『2666』": [
        {"axis": "物語", "status": "partial",
         "rationale": "5部構成の網目状物語が複数の主体・場所・時代を結合する構造は、"
                       "AI生成テクストにおける主体非中心的物語の先駆と部分的に対応する。",
         "ai_phenomenon": "AI生成における主体非中心的物語構造"},
    ],
    "辺境（frontera）": [
        {"axis": "言語", "status": "partial",
         "rationale": "境界に住む主体の二言語(Spanglish)・複言語的実践は、"
                       "AI生成多言語テクストの混淆性・コードスイッチングと部分的に類比される。",
         "ai_phenomenon": "AI生成における多言語混淆・コードスイッチング"},
    ],
    "メスティサヘ（混血性）": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "純粋性ではなく混淆を価値とするmestizaje概念は、"
                       "AI訓練データの混合的性格と正典の純粋性概念の崩壊に直接適用される。",
         "ai_phenomenon": "AI訓練における正典純粋性の崩壊と混淆的知識"},
    ],
    "Casa de las Américas（アメリカの家）": [
        {"axis": "正典", "status": "partial",
         "rationale": "文学賞による正典形成装置としてのCasa de las Américasは、"
                       "AI訓練データのキュレーション(=新たな正典化装置)と部分的に対応する。",
         "ai_phenomenon": "AI訓練データキュレーションによる正典形成"},
    ],
}


# ---------------------------------------------------------------
# Cross-domain links (>= 8)
# ---------------------------------------------------------------
CROSS_DOMAIN_LINKS = [
    ("モデルニスモ（イスパノアメリカ）", "PT", "shared_concept", "modernismo poetics",
     "ルベン・ダリオを中心とするモデルニスモは詩学・修辞論の独自体系を構築し"
     "Poetics DBの近代詩学理論と直接共有される。"),
    ("ネオ・バロック（Lezama Lima）", "PT", "shared_concept", "baroque poetics",
     "Lezama-Sarduy系譜のneobarrocoは17世紀バロック詩学を現代に再活性化し、"
     "Poetics DBのバロック理論と直接共有される。"),
    ("ボルヘス的迷宮", "PHIL", "shared_concept", "Borges philosophical influence",
     "ボルヘスの形而上的虚構はFoucault・Derridaらに直接影響し、"
     "20世紀哲学の重要なリソースとなった。"),
    ("ボルヘス的迷宮", "AI-Development", "parallel", "infinite library and LLM latent space",
     "『La biblioteca de Babel』(1941)が予表する無限図書館はLLMの潜在テクスト空間と"
     "直接的に類比され、AI開発の文学的先駆として位置づけられる。"),
    ("メスティサヘ（混血性）", "AN", "shared_concept", "mestizaje and racial mixing",
     "ラテンアメリカ人類学の中核概念であり人類学DBの民族・人種理論と直接共有される。"),
    ("先駆的インディヘニスモ", "AN", "shared_concept", "indigenous representation",
     "先住民表象をめぐる文学運動は人類学的他者代弁問題と直接接続し、"
     "人類学DBの民族誌的代弁論と共有される。"),
    ("transculturación（文化越境化）", "AN", "shared_concept", "transculturation theory",
     "Fernando Ortizによるtransculturación概念は人類学・文学の境界横断的概念で、"
     "人類学DBの文化変容理論と直接共有される。"),
    ("脱植民地批評", "PHIL", "shared_concept", "decolonial philosophy",
     "Quijano・Mignolo・Dusselらの脱植民地批評は哲学・社会理論との一体的展開で、"
     "Philosophy DBの脱植民地哲学と直接共有される。"),
    ("アントロポファジア（人食いブラジル）", "AN", "shared_concept", "anthropophagy and ritual",
     "Tupi族の儀礼をメタファー化したantropofagiaは人類学的実体研究と接続し、"
     "人類学DBの儀礼・身体性理論と共有される。"),
    ("テスティモニオ文学", "AN", "shared_concept", "ethnographic testimony",
     "testimonio の他者代弁構造は民族誌的代弁論と直接共有され、"
     "Rigoberta Menchú論争は人類学的真正性議論と一体である。"),
    ("コミットメント文学（literatura comprometida）", "PHIL", "shared_concept", "Sartrean engagement",
     "サルトル『文学とは何か』のengagement概念をラテンアメリカ的に翻訳した概念で、"
     "20世紀実存主義哲学と一体的展開を持つ。"),
    ("Casa de las Américas（アメリカの家）", "AN", "parallel", "cultural institution",
     "革命キューバの文化外交装置として汎ラテンアメリカ的連帯を制度化、"
     "人類学的文化制度研究と並行的事象。"),
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

        print(f"\n=== C26 Latin American Boom completed ===")
        print(f"  concepts inserted: {inserted} (skipped: {skipped})")
        print(f"  fourth-transform tags: {ft_count}")
        print(f"  cross-domain links: {cd_count}")
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 16"
        ).fetchone()
        print(f"  total concepts in subfield 16: {row['c']}")


if __name__ == "__main__":
    main()
