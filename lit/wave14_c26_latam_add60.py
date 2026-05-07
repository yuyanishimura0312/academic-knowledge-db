"""LIT-DB Phase 2 Wave 14 — C26: Latin American Literature (+60).

Subfield: lit_latin_america (id=16), region='ラテンアメリカ'.
Sources: Project Gutenberg, Wikisource es/pt, BVMC (Biblioteca Virtual Miguel
de Cervantes), archive.org, BNDigital Brasil.
Living-author works -> secondary acceptable. Aim ~60% primary tier.
fourth_transform_tags >= 18; cross_domain (PT/PHIL/AN) >= 12.

Adds 60 new concepts on top of the existing 81 (Wave 3 Boom + Wave 7 colonial),
covering: pre-Boom indigenismo, Mexican Revolution novel, Argentina expanded,
Brazil expanded (19c-20c-21c), post-Boom + McOndo + Crack, Caribbean Spanish,
Andean, Southern Cone testimonio, Indigenous LatAm, women writers expanded,
Brazilian post-modern.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("プレ・ブーム期", "Pre-Boom (early-mid 20th c.)", 1900, 1955,
     "ラテンアメリカ地域小説・インディヘニスモ・メキシコ革命小説の隆盛期。"),
    ("メキシコ革命期文学", "Mexican Revolution Literature", 1910, 1955,
     "1910年メキシコ革命を文学化したアスエラ、グスマン、ヤニェス、ルルフォらの時代。"),
    ("インディヘニスモ期", "Indigenismo (Andean)", 1920, 1965,
     "アレグリア、アルゲダス、ロペス・イ・フエンテスらアンデス先住民問題の文学化期。"),
    ("ラテンアメリカ・ブーム期拡張", "LatAm Boom Expanded", 1955, 1975,
     "コルタサル、フエンテス、バルガス・リョサ、ガルシア・マルケスら個別作品。"),
    ("ポスト・ブーム期", "Post-Boom (1970s-90s)", 1970, 1995,
     "ドノソ、プイグ、後期ガルシア・マルケスら、ブーム後のラテンアメリカ小説。"),
    ("McOndo・Crack世代", "McOndo & Crack Generation", 1990, 2010,
     "フゲ、フレサン、ボラーニョ、ボルピ、パディーリャらラテンアメリカ脱魔術リアリズム世代。"),
    ("カリブ・スペイン語文学期", "Caribbean Spanish Literature (20th c.)", 1930, 2000,
     "カルペンティエル、レサマ・リマ、カブレラ・インファンテ、サルドゥイ、アレナス、パドゥラ。"),
    ("ブラジル近代文学期", "Brazilian Modern Literature", 1880, 1960,
     "マシャード・デ・アシスから1922年モデルニズモを経てロサ・リスペクトルへ。"),
    ("ブラジル現代文学期", "Brazilian Contemporary Literature", 1960, 2025,
     "ロサ後期、リスペクトル後期、テレス、ヒルダ・イルスト、ハトゥム、エヴァリスト、フェレス、ヴィエイラ・ジュニオール。"),
    ("テスティモニオ期", "Testimonio (Southern Cone)", 1955, 1995,
     "ウォルシュ『オペラシオン・マサクレ』、ガレアーノら証言文学・歴史エッセイ期。"),
    ("先住民口承・現代インディヘナ", "Indigenous Oral & Modern Indigenous Lit",
     1500, 2025,
     "マヤ『ラビナル・アチ』、ケチュア『アプ・インカ・アタワルパマン』、マプチェ詩、ヤギャン／セルクナム保存口承、現代インディヘナ小説。"),
    ("21世紀女性作家期", "21st-c. LatAm Women Writers", 1995, 2025,
     "シュウェブリン、エンリケス、オヘダ、カベソン・カマラら現代女性作家。"),
]


GUTEN = "https://www.gutenberg.org/"
WIKI_ES = "https://es.wikipedia.org/wiki/"
WIKI_PT = "https://pt.wikipedia.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WSRC_ES = "https://es.wikisource.org/wiki/"
WSRC_PT = "https://pt.wikisource.org/wiki/"
BVMC = "https://www.cervantesvirtual.com/"
ARCHIVE = "https://archive.org/details/"
BNDIG = "https://bndigital.bn.gov.br/"
BRITT = "https://www.britannica.com/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_latin_america", region="ラテンアメリカ",
         original_script="roman")


# ============================================================
# A: インディヘニスモ／プレ・ブーム期 (8)
# ============================================================
add(**C, name_ja="シロ・アレグリア『広く異郷なる世界』",
    name_en="Ciro Alegría's El mundo es ancho y ajeno",
    name_original="El mundo es ancho y ajeno",
    period_key="インディヘニスモ期",
    definition="ペルー作家シロ・アレグリア（1909-1967）が1941年に発表した長編小説。アンデス先住民共同体ルミの土地収奪と消滅を描き、ラテンアメリカ・インディヘニスモ小説の頂点として汎アメリカ文学賞を受賞した。",
    background="ペルー1920-30年代のインディヘニスモ運動と、ハシエンダ制下の先住民土地問題。",
    development="アルゲダスを経てボリビア、エクアドル、ラテンアメリカ全域のインディヘニスモ文学に継承された。",
    historical_context="ペルー・オリゴガルキア体制下の先住民共同体破壊。",
    primary_source_url=BVMC+"obra/el-mundo-es-ancho-y-ajeno/",
    primary_source_type="BVMC: El mundo es ancho y ajeno",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="シロ・アレグリア『黄金の蛇』",
    name_en="Ciro Alegría's La serpiente de oro",
    name_original="La serpiente de oro",
    period_key="インディヘニスモ期",
    definition="シロ・アレグリアが1935年に発表した長編小説。ペルー北部マラニョン河流域のチョロ（メスティーソ）筏師の生活を詩的に描き、地域小説とインディヘニスモを橋渡しした。ラテンアメリカ小説賞を受賞。",
    background="マラニョン河流域の先住民・メスティーソ船頭文化、1930年代APRA党のインディヘニスモ。",
    development="アルゲダス、サモラ・サクラメンタらアンデス文学に継承された。",
    historical_context="ペルー1930年代の地域小説的潮流。",
    primary_source_url=BVMC+"obra/la-serpiente-de-oro/",
    primary_source_type="BVMC: La serpiente de oro",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ホセ・マリア・アルゲダス『ヤワル・フィエスタ』",
    name_en="Arguedas's Yawar Fiesta",
    name_original="Yawar Fiesta",
    period_key="インディヘニスモ期",
    definition="ペルー作家ホセ・マリア・アルゲダス（1911-1969）が1941年に発表した長編小説。アンデス山地の先住民共同体「コミュニダー」が祝う「血の祭」（ヤワル・フィエスタ）と、リマ中央政府の禁止令の衝突を描く。タイトルがケチュア語のままなのは新インディヘニスモの言語政治の象徴。",
    background="ペルー高地共同体の闘牛祭祀、1910-30年代の中央集権化と先住民文化抑圧。",
    development="『深い川』『すべての血』『キツネ』と進む五部作の出発点。",
    historical_context="ペルー山地の祭祀人類学とインディヘニスモ文学化。",
    primary_source_url=ARCHIVE+"yawarfiestajose0000argu",
    primary_source_type="archive.org: Yawar Fiesta (Arguedas, 1941 ed.)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アルゲダス『深い川』",
    name_en="Arguedas's Los ríos profundos",
    name_original="Los ríos profundos",
    period_key="インディヘニスモ期",
    definition="アルゲダスが1958年に発表した長編小説。少年エルネストが寄宿学校で先住民文化と白人支配の間に引き裂かれる過程を描き、ケチュア語の音韻リズムをスペイン語散文に組み込んだ。ペルー国民文学賞受賞。",
    background="クスコ・アバンカイ地方の寄宿学校、ケチュア語と西語のバイリンガル現実。",
    development="ラテンアメリカ・新インディヘニスモの代表作として、アンヘル・ラマ『移動する都市の周辺』理論の基礎テクスト。",
    historical_context="1950年代ペルーの教育・地方・先住民問題。",
    primary_source_url=ARCHIVE+"losriosprofundos0000argu",
    primary_source_type="archive.org: Los ríos profundos (1958)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アルゲダス『キツネ ——上のキツネと下のキツネ』",
    name_en="Arguedas's El zorro de arriba y el zorro de abajo",
    name_original="El zorro de arriba y el zorro de abajo",
    period_key="インディヘニスモ期",
    definition="アルゲダス遺作（1971年没後刊行）の長編。ペルー漁港チンボテを舞台に、自殺直前の作家自身の日記断章と漁民・売春婦・移民の物語が交錯する。アンデス神話「上のキツネと下のキツネ」を構造原理とし、近代ラテンアメリカ・メタフィクションの先駆。",
    background="ペルー60年代の沿岸工業化と山地→沿岸の大規模移民、アルゲダスの精神的危機。",
    development="アンヘル・ラマ批評で「文化越境化（transculturación）」の中心テクストとされ、ラテンアメリカ批評理論の核となった。",
    historical_context="ペルー1960年代の都市化・産業化危機、ベラスコ革命前夜。",
    primary_source_url=ARCHIVE+"elzorrodearriba0000argu",
    primary_source_type="archive.org: El zorro de arriba (1971)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アスエラ『虐げられた人々』",
    name_en="Mariano Azuela's Los de abajo",
    name_original="Los de abajo",
    period_key="メキシコ革命期文学",
    definition="マリアノ・アスエラ（1873-1952）が1915年に新聞連載で発表した革命小説。北部メキシコのデメトリオ・マシアス率いる農民革命兵団の盛衰を断片的場面の連鎖で描き、メキシコ革命小説の祖型を確立した。",
    background="1910-1920年メキシコ革命下の北部戦線、アスエラ自身の革命軍従軍経験。",
    development="グスマン、ヤニェス、ルルフォを経てメキシコ近代小説全体の出発点となった。",
    historical_context="メキシコ革命の社会的渦中。",
    primary_source_url=GUTEN+"ebooks/24693",
    primary_source_type="Project Gutenberg: Los de abajo",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="グスマン『鷲と蛇』",
    name_en="Martín Luis Guzmán's El águila y la serpiente",
    name_original="El águila y la serpiente",
    period_key="メキシコ革命期文学",
    definition="マルティン・ルイス・グスマン（1887-1976）が1928年に発表した小説的回想録。革命派指導者ビリャ、カランサ、オブレゴンらを身近に観察した経験を、自伝的章と革命史断章として再構成した作品。メキシコ革命「証言小説」の基準作。",
    background="グスマンの革命派ジャーナリスト経験とビリャ陣営観察。",
    development="ヤニェス、ルルフォ、フエンテスのメキシコ歴史小説に継承された。",
    historical_context="メキシコ革命指導者層の内部権力闘争。",
    primary_source_url=BVMC+"obra/el-aguila-y-la-serpiente/",
    primary_source_type="BVMC: El águila y la serpiente",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヤニェス『嵐のとき』",
    name_en="Agustín Yáñez's Al filo del agua",
    name_original="Al filo del agua",
    period_key="メキシコ革命期文学",
    definition="アグスティン・ヤニェス（1904-1980）が1947年に発表した長編。ハリスコ州小村の革命前夜（1909-1910）の精神的閉塞をフォークナー的多視点で描き、メキシコ近代小説（ルルフォ、フエンテス）の前提を準備した。",
    background="ハリスコ州メキシコ・カトリック小社会の革命前夜の心理人類学。",
    development="ルルフォ『ペドロ・パラモ』、フエンテス『澄みわたる大地』への直接の橋渡し。",
    historical_context="1910年メキシコ革命前夜の地方カトリック社会。",
    primary_source_url=BVMC+"obra/al-filo-del-agua/",
    primary_source_type="BVMC: Al filo del agua",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# B: メキシコ革命後・ルルフォ／フエンテス／パチェコ拡張 (8)
# ============================================================
add(**C, name_ja="ルルフォ『燃える平原』",
    name_en="Juan Rulfo's El llano en llamas",
    name_original="El llano en llamas",
    period_key="メキシコ革命期文学",
    definition="フアン・ルルフォ（1917-1986）が1953年に刊行した短編集（17篇）。革命後ハリスコ州の貧農共同体を、最小限の口語と省略で描く。「ルビーナ」「ペドロ・パラモに告げてくれ」等を含み、ラテンアメリカ短編の最高峰。",
    background="ハリスコ農村のクリステロ戦争後の精神的廃墟、ルルフォ自身の孤児体験。",
    development="ガルシア・マルケスが「これを読まなければ作家にはなれなかった」と評し、『百年の孤独』マコンドの祖型。",
    historical_context="メキシコ革命後の農地改革挫折とクリステロ戦争（1926-1929）。",
    primary_source_url=ARCHIVE+"elllanoenllamas0000rulf",
    primary_source_type="archive.org: El llano en llamas (1953)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ルルフォ『ペドロ・パラモ』詳解",
    name_en="Rulfo's Pedro Páramo (close reading)",
    name_original="Pedro Páramo",
    period_key="メキシコ革命期文学",
    definition="ルルフォが1955年に発表した長編。死者と生者が混在する村コマラを舞台に、息子フアン・プレシアドの父探しを断片化した時間と話者の交替で語る。68の断章でラテンアメリカ・モダニズムの頂点を成し、フアン・プレシアド本人も死者であることが明らかになる構造で、魔術的リアリズムの先駆。",
    background="ハリスコ州コマラのカシケ（地方ボス）社会、ルルフォの実家衰亡経験。",
    development="ガルシア・マルケス、フエンテス、ボラーニョの直接的祖型。",
    historical_context="メキシコ革命後の地方権力構造の崩壊。",
    primary_source_url=ARCHIVE+"pedroparamo0000rulf",
    primary_source_type="archive.org: Pedro Páramo (1955)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="フエンテス『澄みわたる大地』",
    name_en="Fuentes's La región más transparente",
    name_original="La región más transparente",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="カルロス・フエンテス（1928-2012）が1958年に発表した長編。メキシコ・シティを多視点・多話者で描く都市総合小説。ジョイス『ユリシーズ』、ドス・パソス『U.S.A.』を範に革命後メキシコ・シティの階級構造を解剖し、メキシコ近代都市小説の出発点。",
    background="1950年代メキシコ・シティの都市化、PRI体制下の階級再編。",
    development="ボルヘス、コルタサル、ガルシア・マルケスのブーム小説の前提を作った。",
    historical_context="PRI体制下メキシコ・シティの近代化と階級緊張。",
    primary_source_url=ARCHIVE+"laregionmastrans0000fuen",
    primary_source_type="archive.org: La región más transparente (1958)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="フエンテス『アウラ』",
    name_en="Fuentes's Aura",
    name_original="Aura",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="フエンテスが1962年に発表した短編小説（中編）。二人称現在形「君は…する」で語られ、青年史家フェリペが老婦人コンスエロの邸で若い姪アウラと出会い、二人が同一存在であることを発見する幻想小説。日本江戸怪談（円朝『真景累ヶ淵』類縁）への言及があり、ラテンアメリカ幻想短編の代表作。",
    background="1960年代メキシコ・シティの幻想短編潮流、フエンテスの欧州・日本怪談渉猟。",
    development="ボラーニョ、エンリケスの幻想・怪奇路線に継承。",
    historical_context="1960年代メキシコ知識人による文学的実験。",
    primary_source_url=ARCHIVE+"aura0000fuen",
    primary_source_type="archive.org: Aura (1962)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フエンテス『アルテミオ・クルスの死』",
    name_en="Fuentes's La muerte de Artemio Cruz",
    name_original="La muerte de Artemio Cruz",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="フエンテスが1962年に発表した長編。革命を生き延び腐敗した寡頭資本家アルテミオ・クルスの臨終意識を、一人称・二人称・三人称の三声で交差させ、メキシコ革命の理想と裏切りを総括する。ブーム期メキシコ小説の頂点。",
    background="1962年フエンテスの革命幻滅とPRI体制批判の結晶。",
    development="バルガス・リョサ『緑の家』『カテドラルでの対話』の多声構造に直接影響。",
    historical_context="メキシコ革命50年の総括的問い直し。",
    primary_source_url=ARCHIVE+"lamuertedeartemio0000fuen",
    primary_source_type="archive.org: La muerte de Artemio Cruz (1962)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="フエンテス『テラ・ノストラ』詳解",
    name_en="Fuentes's Terra Nostra (close reading)",
    name_original="Terra Nostra",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="フエンテスが1975年に発表した1000頁超の歴史総合小説。フェリペ二世のエル・エスコリアル、コロンブス到達、未来2000年パリを縦横に往還し、ヒスパニック世界の起源と未来を構造的に問う。ロムロ・ガリェゴス賞、ハベリエール・ビリャウルティア賞受賞。",
    background="フエンテスの1970年代ヨーロッパ・歴史哲学渉猟。",
    development="ピエール・メナール的歴史メタフィクション、ボルピらクラック世代の歴史小説の祖型。",
    historical_context="1970年代ラテンアメリカ知識人の起源論的問い直し。",
    primary_source_url=BVMC+"obra/terra-nostra/",
    primary_source_type="BVMC: Terra Nostra",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ホセ・エミリオ・パチェコ『君は遠くで死ぬだろう』",
    name_en="José Emilio Pacheco's Morirás lejos",
    name_original="Morirás lejos",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="ホセ・エミリオ・パチェコ（1939-2014）が1967年に発表した中編。エルサレム神殿陥落（70年）、スペイン異端審問、ナチス・ホロコースト、現代メキシコ・シティを連結し、迫害の循環を構造的に描く。メキシコ「中間世代」の代表作。",
    background="1968年トラテロルコ事件前夜のメキシコ知識人の歴史的不安。",
    development="ボルピ、パディーリャらクラック世代の歴史小説に直接継承。",
    historical_context="1960年代後半メキシコの政治不安定。",
    primary_source_url=BVMC+"obra/moriras-lejos/",
    primary_source_type="BVMC: Morirás lejos",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ロサリオ・カステリャーノス『バルン・カナン』",
    name_en="Rosario Castellanos's Balún Canán",
    name_original="Balún Canán",
    period_key="メキシコ革命期文学",
    definition="ロサリオ・カステリャーノス（1925-1974）が1957年に発表した長編。チアパス州ツェルタル先住民地域の少女視点で土地改革と先住民・白人ファミリーの関係を描く。メキシコ・インディヘニスモのフェミニスト的更新。",
    background="チアパス州の植民地的ハシエンダ制とカルデナス土地改革（1934-40）の先住民への影響。",
    development="エレナ・ポニャトウスカ、エレナ・ガロ、現代メキシコ女性作家の祖型。",
    historical_context="メキシコ南部の先住民問題と土地改革。",
    primary_source_url=ARCHIVE+"baluncanan0000cast",
    primary_source_type="archive.org: Balún Canán (1957)",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# C: アルゼンチン拡張：ボルヘス／ビオイ／コルタサル／サバト個別作品 (8)
# ============================================================
add(**C, name_ja="ボルヘス『フィクションズ』詳解",
    name_en="Borges's Ficciones (close reading)",
    name_original="Ficciones",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="ホルヘ・ルイス・ボルヘス（1899-1986）が1944年に編んだ短編集。「トレーン、ウクバール、オルビス・テルティウス」「八岐の園」「バビロンのくじ」「ピエール・メナール」を含む。架空の書物・無限図書館・幾何学的時間の構造を確立し、20世紀世界文学の古典。",
    background="1940年代ブエノスアイレスの文学誌「Sur」周辺、形而上学・神秘主義・推理小説の総合。",
    development="フーコー『言葉と物』冒頭、エコ『薔薇の名前』、現代メタフィクション全体の祖型。",
    historical_context="1940年代アルゼンチン都市知識人文化。",
    primary_source_url=ARCHIVE+"ficciones0000borg",
    primary_source_type="archive.org: Ficciones (1944)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ボルヘス『八岐の園』",
    name_en="Borges's El jardín de senderos que se bifurcan",
    name_original="El jardín de senderos que se bifurcan",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="ボルヘスが1941年に発表した短編。中国スパイ余尊が祖先の迷宮的小説を解読する物語で、すべての可能な未来が同時に存在する「分岐する時間」を提示する。多世界解釈・ハイパーテクスト理論の前駆として現代情報理論で頻繁に参照される。",
    background="第二次大戦中アルゼンチンでの東洋学読書、量子力学普及前の論理的多世界。",
    development="ヘンリー・エヴェレット多世界解釈、デリダ脱構築、ハイパーテクスト理論の参照点。",
    historical_context="第二次大戦中の中立アルゼンチン知識人。",
    primary_source_url=ARCHIVE+"jardinsenderos0000borg",
    primary_source_type="archive.org: Ficciones所収",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ボルヘス『アレフ』詳解",
    name_en="Borges's El Aleph (close reading)",
    name_original="El Aleph",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="ボルヘスが1949年に編んだ短編集。表題作「アレフ」では地下室で全宇宙を同時に見る一点が提示され、「不死の人」「神学者」を含む。空間・時間・自己同一性の幾何学的限界を扱う形而上学的短編集。",
    background="1949年ブエノスアイレス、ペロン政権下のボルヘスの図書館員時代。",
    development="サブァト、コルタサル、ボラーニョ、ピンチョン全体への影響。",
    historical_context="ペロン政権下アルゼンチン文学界。",
    primary_source_url=ARCHIVE+"elaleph0000borg",
    primary_source_type="archive.org: El Aleph (1949)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ボルヘス『他者の異端審問』",
    name_en="Borges's Otras inquisiciones",
    name_original="Otras inquisiciones",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="ボルヘスが1952年に刊行したエッセイ集。「カフカとその先駆者たち」「『キホーテ』の隠れた魔術」「ホーソーン」「壁と書物」を含み、文学史を作家相互の遡及的影響として理論化する。文学批評理論への決定的貢献。",
    background="1950年代初頭ボルヘスのエッセイ集大成。",
    development="T.S.エリオット影響論との対比、現代受容理論・系譜批評の前駆。",
    historical_context="ペロン体制下の批評的退避としてのエッセイ。",
    primary_source_url=ARCHIVE+"otrasinquisicio0000borg",
    primary_source_type="archive.org: Otras inquisiciones (1952)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ビオイ・カサーレス『モレルの発明』",
    name_en="Bioy Casares's La invención de Morel",
    name_original="La invención de Morel",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="アドルフォ・ビオイ・カサーレス（1914-1999）が1940年に発表した中編。無人島の逃亡者が出会う人々が、実は機械装置で永遠再生される死者の映像であると判明する幻想小説。ボルヘスは序文で「完璧な小説」と評した。仮想現実・シミュレーションの祖型。",
    background="1930年代末ブエノスアイレス、ボルヘス／ビオイ協働期。",
    development="アラン・ロブ＝グリエ『去年マリエンバートで』、リン『マトリックス』理論的祖型。",
    historical_context="第二次大戦前夜の南米モダニズム。",
    primary_source_url=ARCHIVE+"lainvenciondemorel0000bioy",
    primary_source_type="archive.org: La invención de Morel (1940)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="コルタサル『石蹴り遊び』構造",
    name_en="Cortázar's Rayuela (structural analysis)",
    name_original="Rayuela",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="フリオ・コルタサル（1914-1984）が1963年に発表した長編。155章を、線形読み（1-56章）／指示順読み（73章から表に従う）／自由読みの三通りで読むよう指示する構造で、開放小説（novela abierta）概念を確立した。パリのオラシオとブエノスアイレスのオラシオの二都市構造で文学的越境を主題化。",
    background="1950-60年代パリの亡命アルゼンチン文学コミュニティ、ジャズ・即興・サルトル実存主義。",
    development="エコ『開かれた作品』理論の文学的実装、ハイパーテクスト・ナラトロジーの前駆。",
    historical_context="1960年代パリ知識人のラテンアメリカ・コスモポリタニズム。",
    primary_source_url=ARCHIVE+"rayuela0000cort",
    primary_source_type="archive.org: Rayuela (1963)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="コルタサル『動物寓意譚（Bestiario）』",
    name_en="Cortázar's Bestiario",
    name_original="Bestiario",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="コルタサルが1951年に発表した第一短編集（8篇）。「占拠された家」「片頭痛」「動物寓意譚」を含み、日常空間に幻想が侵入する「新幻想（nuevo fantástico）」の祖型を作った。",
    background="1950年代初頭ブエノスアイレス、ボルヘス影響下の幻想短編潮流。",
    development="サムエル・ベケット、エンリケス、シュウェブリンの現代不安幻想に継承。",
    historical_context="ペロン政権下アルゼンチンの不安。",
    primary_source_url=BVMC+"obra/bestiario/",
    primary_source_type="BVMC: Bestiario",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="サバト『英雄たちと墓について』",
    name_en="Sábato's Sobre héroes y tumbas",
    name_original="Sobre héroes y tumbas",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="エルネスト・サバト（1911-2011）が1961年に発表した長編。ブエノスアイレスを舞台に、若い建築家マルティンと精神不安定なアレハンドラの恋愛、その父フェルナンドの「盲人についての報告」（地下盲人組織の妄想）を組み合わせる。20世紀ラテンアメリカ実存主義小説の頂点。",
    background="1950年代アルゼンチンの政治・経済不安、サバト自身の物理学者→作家の転身。",
    development="ピグリア、コーン、現代アルゼンチン心理小説に継承。",
    historical_context="ペロン後アルゼンチンの実存的不安。",
    primary_source_url=ARCHIVE+"sobreheroesytumbas0000saba",
    primary_source_type="archive.org: Sobre héroes y tumbas (1961)",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: ブラジル19-20世紀拡張 (10)
# ============================================================
add(**C, name_ja="マシャード・デ・アシス『ブラス・クーバスの死後の回想』",
    name_en="Machado de Assis's Memórias Póstumas de Brás Cubas",
    name_original="Memórias Póstumas de Brás Cubas",
    period_key="ブラジル近代文学期",
    definition="マシャード・デ・アシス（1839-1908）が1881年に発表した長編。死者ブラス・クーバスが書いた回想という設定で、19世紀リオの上層ブルジョワ社会を皮肉とメタフィクションで描く。ブラジル近代文学の出発点で、スーザン・ソンタグ、ハロルド・ブルームが20世紀以前最高の小説の一つと評価。",
    background="第二帝政期リオ社会、奴隷制末期の支配階級内部観察。",
    development="ボルヘス、カルヴィーノ、ロベルト・ロサーニのメタフィクションに継承。",
    historical_context="19世紀末ブラジル奴隷制末期。",
    primary_source_url=GUTEN+"ebooks/54829",
    primary_source_type="Project Gutenberg: Memórias Póstumas",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マシャード・デ・アシス『キンカス・ボルバ』",
    name_en="Machado de Assis's Quincas Borba",
    name_original="Quincas Borba",
    period_key="ブラジル近代文学期",
    definition="マシャード・デ・アシスが1891年に発表した長編。狂気の哲学者キンカス・ボルバから遺産を相続したルバンが社会的破滅へ向かう過程を描き、独自の哲学「ヒューマニティスム（Humanitismo）」を風刺する。ブラジル・リアリズム三部作の中作。",
    background="第二帝政末期リオ、奴隷制廃止（1888）と共和制移行（1889）期の社会動揺。",
    development="エサ・デ・ケイロス、20世紀ブラジル風刺小説の祖型。",
    historical_context="ブラジル奴隷制廃止と共和制移行期。",
    primary_source_url=GUTEN+"ebooks/55752",
    primary_source_type="Project Gutenberg: Quincas Borba",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マシャード・デ・アシス『ドン・カズムッホ』",
    name_en="Machado de Assis's Dom Casmurro",
    name_original="Dom Casmurro",
    period_key="ブラジル近代文学期",
    definition="マシャード・デ・アシスが1899年に発表した長編。一人称話者ベント・サンチャゴが妻カピトゥの不貞を疑い、その確信を読者に納得させようとする物語。語り手の信頼性問題を軸に、ヘレン・カルダウェル『The Brazilian Othello』(1960)以来、文学批評最大の作品の一つとして読まれる。",
    background="19世紀末リオ・ブルジョワ社会の家庭・倫理規範。",
    development="ヘンリー・ジェイムズ、ナボコフ的不信頼話者文学全体に並行。",
    historical_context="ブラジル共和制初期の社会文化。",
    primary_source_url=GUTEN+"ebooks/55752",
    primary_source_type="Project Gutenberg: Dom Casmurro",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="エウクリーデス・ダ・クーニャ『奥地』",
    name_en="Euclides da Cunha's Os sertões",
    name_original="Os sertões",
    period_key="ブラジル近代文学期",
    definition="エウクリーデス・ダ・クーニャ（1866-1909）が1902年に発表したカヌードス戦争（1893-1897）報告書。バイーア州奥地の宗教指導者アントニオ・コンセイレイロの神権共同体を、地理・人類学・軍事報告として記述する。ブラジル文学・社会科学の祖型。",
    background="19世紀末バイーア州奥地の宗教共同体カヌードスと連邦軍の戦争。",
    development="ヴァルガス・リョサ『世界終末戦争』、ロサ『大いなる奥地』の直接の祖型。",
    historical_context="ブラジル共和制成立直後の連邦／奥地対立。",
    primary_source_url=GUTEN+"ebooks/30661",
    primary_source_type="Project Gutenberg: Os sertões",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="リマ・バレット『ポリカルポ・クアレズマの悲しき結末』",
    name_en="Lima Barreto's Triste fim de Policarpo Quaresma",
    name_original="Triste fim de Policarpo Quaresma",
    period_key="ブラジル近代文学期",
    definition="リマ・バレット（1881-1922）が1911年に発表した長編。リオの愛国的官吏ポリカルポ・クアレズマがブラジル国民国家形成の挫折に逢着する物語。ブラジル共和制初期の人種差別と国家神話を批判的に描く。",
    background="共和制初期リオの人種・階級構造。リマ・バレット自身の混血・貧困経験。",
    development="マリオ・デ・アンドラーデ、コンセイサオン・エヴァリスト等の人種批判文学の前駆。",
    historical_context="共和制初期ブラジルの国家形成。",
    primary_source_url=GUTEN+"ebooks/45881",
    primary_source_type="Project Gutenberg: Triste fim de Policarpo Quaresma",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マリオ・デ・アンドラーデ『マクナイマ』",
    name_en="Mário de Andrade's Macunaíma",
    name_original="Macunaíma: o herói sem nenhum caráter",
    period_key="ブラジル近代文学期",
    definition="マリオ・デ・アンドラーデ（1893-1945）が1928年に発表した長編。アマゾン先住民の英雄マクナイマがリオ・サンパウロを横断する物語で、ブラジル諸地域の民俗・神話・口承を融合する「ラプソディア（狂詩曲）」。1922年「現代芸術週」とアントロポファジア宣言の文学的結実。",
    background="1920年代サンパウロ・モデルニズモ、オズワルド・デ・アンドラーデ「アントロポファジア宣言」(1928)。",
    development="ロサ『大いなる奥地』、現代ブラジル先住民文学の前提。",
    historical_context="1920年代ブラジル文化民族主義。",
    primary_source_url=BNDIG+"acervodigital/livros/macunaima",
    primary_source_type="BNDigital: Macunaíma (1928)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="カルロス・ドラモンド・デ・アンドラーデ『世界の感情』",
    name_en="Carlos Drummond de Andrade's Sentimento do mundo",
    name_original="Sentimento do mundo",
    period_key="ブラジル近代文学期",
    definition="カルロス・ドラモンド・デ・アンドラーデ（1902-1987）が1940年に発表した第三詩集。「七つの顔の詩」「肩がこる、生は重い」を含み、ブラジル・モデルニズモの第二世代を代表する。社会的不安と個人的孤独の交差を口語自由詩で表現。",
    background="第二次大戦勃発期ブラジル、ヴァルガス独裁下の知識人。",
    development="ジョアン・カブラル・デ・メロ・ネトら20世紀ブラジル詩全体の規範。",
    historical_context="ヴァルガス・エスタード・ノーヴォ期(1937-45)。",
    primary_source_url=ARCHIVE+"sentimentodomundo0000drum",
    primary_source_type="archive.org: Sentimento do mundo (1940)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ロサ『大いなる奥地：諸小道』",
    name_en="Guimarães Rosa's Grande Sertão: Veredas",
    name_original="Grande Sertão: Veredas",
    period_key="ブラジル現代文学期",
    definition="ジョアン・ギマランエス・ロサ（1908-1967）が1956年に発表した長編。ミナス・ジェライス州奥地の傭兵リオバルドの語りを、500頁以上の独白として展開。ポルトガル語をネオロジズム・口語・古語で再構築し、20世紀ラテンアメリカ最高峰の言語実験小説。",
    background="ミナス州奥地のジャグンソ（傭兵）文化、ロサ自身の医師・外交官経験。",
    development="ボラーニョ、ハトゥム、現代ブラジル文学全体への決定的影響。",
    historical_context="ブラジル奥地（セルタオン）の社会人類学。",
    primary_source_url=ARCHIVE+"grandesertaoveredas0000rosa",
    primary_source_type="archive.org: Grande Sertão (1956)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ロサ『最初の物語』",
    name_en="Guimarães Rosa's Primeiras estórias",
    name_original="Primeiras estórias",
    period_key="ブラジル現代文学期",
    definition="ロサが1962年に発表した21篇短編集。「川の三番目の岸」「ミグエリン少年」を含み、奥地の少年・狂人・神秘的体験者の声を最小限の言葉で立ち上げる。ブラジル短編の最高峰の一つ。",
    background="1960年代ブラジルのセルタオン民俗観察と精神主義の融合。",
    development="リスペクトル後期、現代ブラジル短編全体に継承。",
    historical_context="1960年代ブラジル現代文学成熟期。",
    primary_source_url=ARCHIVE+"primeirasestorias0000rosa",
    primary_source_type="archive.org: Primeiras estórias (1962)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="リスペクトル『G・H・の受難』",
    name_en="Lispector's A paixão segundo G.H.",
    name_original="A paixão segundo G.H.",
    period_key="ブラジル現代文学期",
    definition="クラリッセ・リスペクトル（1920-1977）が1964年に発表した長編。リオのアパートメイドの部屋でゴキブリと対面した上流ブルジョワ女性G.H.の意識変容を、宗教的告白の形で記述する。ラテンアメリカ女性実存哲学小説の頂点。",
    background="1960年代リオのブルジョワ女性社会、エレーヌ・シクスー後年の理論化。",
    development="シクスー、デリダによる読解で世界フェミニスト批評の中心テクスト化。",
    historical_context="1960年代ブラジル軍政前夜の知的緊張。",
    primary_source_url=ARCHIVE+"apaixaosegundogh0000lisp",
    primary_source_type="archive.org: A paixão segundo G.H. (1964)",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# E: ポスト・ブーム＋McOndo＋Crack (8)
# ============================================================
add(**C, name_ja="ドノソ『卑猥な夜の鳥』",
    name_en="Donoso's El obsceno pájaro de la noche",
    name_original="El obsceno pájaro de la noche",
    period_key="ポスト・ブーム期",
    definition="ホセ・ドノソ（1924-1996）が1970年に発表した長編。チリの没落貴族家系の屋敷を舞台に、奇形収集家族と変身する盲老女の世界を、解体された語りで描く。ラテンアメリカ・ゴシック小説の頂点。",
    background="1960年代末ドノソのバルセロナ亡命と精神的危機。",
    development="ボラーニョ、エンリケスのラテンアメリカ・ゴシックに継承。",
    historical_context="チリ・ピノチェト・クーデター直前の社会的不安。",
    primary_source_url=ARCHIVE+"elobscenopajaro0000dono",
    primary_source_type="archive.org: El obsceno pájaro (1970)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="プイグ『リタ・ヘイワースの裏切り』",
    name_en="Puig's La traición de Rita Hayworth",
    name_original="La traición de Rita Hayworth",
    period_key="ポスト・ブーム期",
    definition="マヌエル・プイグ（1932-1990）が1968年に発表した長編。アルゼンチン地方町の少年トトの周囲を、内的独白・手紙・日記・新聞記事で多声的に再構築する。ハリウッド映画消費がアイデンティティを構築する戦後ラテンアメリカ庶民文化を主題化。",
    background="1960年代アルゼンチンの大衆メディア・ハリウッド受容。",
    development="ポスト・ブーム大衆文化志向の出発点、現代カルチュラル・スタディーズの祖型。",
    historical_context="ペロン後アルゼンチン地方文化。",
    primary_source_url=ARCHIVE+"latraicionderita0000puig",
    primary_source_type="archive.org: La traición de Rita Hayworth (1968)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="プイグ『蜘蛛女のキス』",
    name_en="Puig's El beso de la mujer araña",
    name_original="El beso de la mujer araña",
    period_key="ポスト・ブーム期",
    definition="プイグが1976年に発表した長編。ブエノスアイレス監獄の同房者、政治犯バレンティンと同性愛者モリナの会話だけで構成される。モリナが語るB級映画と二人の関係が交錯し、独裁政権下の連帯と裏切りを描く。1985年映画化（バベンコ監督）。",
    background="1976年アルゼンチン軍事独裁、性的少数者・政治犯への弾圧。",
    development="クィア批評、ラテンアメリカ・ジェンダー研究の中心テクスト。",
    historical_context="アルゼンチン軍事独裁下「汚い戦争」初期。",
    primary_source_url=ARCHIVE+"elbesodelamujer0000puig",
    primary_source_type="archive.org: El beso de la mujer araña (1976)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バルガス・リョサ『カテドラルでの対話』",
    name_en="Vargas Llosa's Conversación en La Catedral",
    name_original="Conversación en La Catedral",
    period_key="ラテンアメリカ・ブーム期拡張",
    definition="マリオ・バルガス・リョサ（1936-2025）が1969年に発表した長編。リマのバル「ラ・カテドラル」での4時間の対話を出発点に、オドリア独裁政権下ペルー（1948-56）の腐敗を多時間・多視点で描く総合小説。「ペルーはいつ駄目になったのか」という冒頭の問いが代表する政治小説。",
    background="オドリア独裁下ペルー、バルガス・リョサ自身のジャーナリスト経験。",
    development="ガルシア・マルケス『族長の秋』、フエンテス『アルテミオ・クルスの死』と並ぶブーム期独裁小説の頂点。",
    historical_context="オドリア独裁(1948-1956)とペルー1960年代の総括。",
    primary_source_url=ARCHIVE+"conversacionenlacatedral0000varg",
    primary_source_type="archive.org: Conversación en La Catedral (1969)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ガルシア・マルケス『族長の秋』",
    name_en="García Márquez's El otoño del patriarca",
    name_original="El otoño del patriarca",
    period_key="ポスト・ブーム期",
    definition="ガブリエル・ガルシア・マルケス（1927-2014）が1975年に発表した長編。架空のカリブ独裁者の200歳超の人生を、極端に長い文と話者の集合的「私たち」で語る。ブーム期独裁者文学（カルペンティエル『方法異論』、アストゥリアス『大統領閣下』、ロア・バストス『至上のわれ』）の頂点。",
    background="ラテンアメリカ20世紀独裁者群像、ガルシア・マルケスの権力分析。",
    development="ボラーニョの現代独裁観察に継承。",
    historical_context="1970年代ラテンアメリカ独裁政権群（ピノチェト、ビデラ、ストロエスナー）。",
    primary_source_url=BVMC+"obra/el-otono-del-patriarca/",
    primary_source_type="BVMC: El otoño del patriarca",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ガルシア・マルケス『予告された殺人の記録』",
    name_en="García Márquez's Crónica de una muerte anunciada",
    name_original="Crónica de una muerte anunciada",
    period_key="ポスト・ブーム期",
    definition="ガルシア・マルケスが1981年に発表した中編。1951年コロンビアの実際の名誉殺人事件を、27年後の聞き書きという形で再構成し、村全員が殺人を予知しながら止めなかった集団的責任を分析する。ラテンアメリカ・ナラティブ・ジャーナリズムの古典。",
    background="1951年スクレ州の実際の事件、ガルシア・マルケス自身の記者経験。",
    development="ハベル『真実の小説』、現代ラテンアメリカ・ナラティブ・ジャーナリズム全体の規範。",
    historical_context="ラテンアメリカ村落の名誉殺人慣習。",
    primary_source_url=ARCHIVE+"cronicademuerteanunciada0000garc",
    primary_source_type="archive.org: Crónica (1981)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ボラーニョ『野生の探偵たち』",
    name_en="Bolaño's Los detectives salvajes",
    name_original="Los detectives salvajes",
    period_key="McOndo・Crack世代",
    definition="ロベルト・ボラーニョ（1953-2003）が1998年に発表した長編。1976年メキシコ・シティの「インフラリアリスタ」詩運動から、ソノラ砂漠での女性詩人セサリア・ティナヘロ探索、ヨーロッパ・アフリカ・イスラエルへの放浪を、52人の証言で20年にわたり辿る。エレラ賞・ロムロ・ガリェゴス賞受賞。",
    background="ボラーニョ自身の70年代メキシコ「インフラリアリスタ」運動経験と亡命。",
    development="現代世界文学・ロード小説の規範、ポスト・ブーム終焉と新世代の出発。",
    historical_context="1970年代メキシコ知識人の左翼挫折と亡命。",
    primary_source_url=BVMC+"obra/los-detectives-salvajes/",
    primary_source_type="BVMC: Los detectives salvajes",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ボラーニョ『2666』詳解",
    name_en="Bolaño's 2666 (close reading)",
    name_original="2666",
    period_key="McOndo・Crack世代",
    definition="ボラーニョが2004年に没後刊行した1100頁超の遺作長編。五部構成で、ベンノ・フォン・アーチンボルディ研究、メキシコ・シウダー・フアレスのフェミサイド、ナチス文学批判、20世紀世界の暴力の総体を扱う。21世紀世界文学の頂点として国際的評価を受けた。",
    background="シウダー・フアレスのフェミサイド（1993-2003、500人以上）、ボラーニョ晩年の死病。",
    development="ハトゥム、ヴォルピ、シュウェブリンら21世紀ラテンアメリカ作家の前提。",
    historical_context="2000年代メキシコ国境の組織犯罪・女性殺害。",
    primary_source_url=ARCHIVE+"2666robertobolano",
    primary_source_type="archive.org: 2666 (2004)",
    importance_score=5, source_tier="secondary", canonical_in_region="core")


# ============================================================
# F: カリブ・スペイン語＋アンデス＋テスティモニオ (8)
# ============================================================
add(**C, name_ja="カルペンティエル『この世の王国』",
    name_en="Carpentier's El reino de este mundo",
    name_original="El reino de este mundo",
    period_key="カリブ・スペイン語文学期",
    definition="アレホ・カルペンティエル（1904-1980）が1949年に発表した中編。ハイチ革命（1791-1804）の黒人指導者マッカンダル、トゥーサン、デサリーヌを描く。序文で「lo real maravilloso（驚異的現実）」を宣言し、ラテンアメリカ魔術的リアリズム理論の出発点となった。",
    background="1943-44年カルペンティエルのハイチ訪問、ヴードゥー文化体験。",
    development="ガルシア・マルケスの魔術的リアリズム、ポスト植民地文学全体への決定的影響。",
    historical_context="ハイチ革命とフランス革命のグローバル史的関連。",
    primary_source_url=ARCHIVE+"elreinodeestemu0000carp",
    primary_source_type="archive.org: El reino de este mundo (1949)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="カルペンティエル『失われた足跡』",
    name_en="Carpentier's Los pasos perdidos",
    name_original="Los pasos perdidos",
    period_key="カリブ・スペイン語文学期",
    definition="カルペンティエルが1953年に発表した長編。ニューヨークの音楽学者がオリノコ川源流の先住民共同体に楽器調査で赴き、近代から先史時代へ時間遡行する物語。ラテンアメリカ・コスモロジー小説の規範。",
    background="1947-48年カルペンティエルのオリノコ川調査旅行。",
    development="ガルシア・マルケス『百年の孤独』、ロサ『大いなる奥地』の地理的・神話的祖型。",
    historical_context="冷戦初期ラテンアメリカ知識人の文化的回帰。",
    primary_source_url=ARCHIVE+"lospasosperdidos0000carp",
    primary_source_type="archive.org: Los pasos perdidos (1953)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="レサマ・リマ『パラディーソ』",
    name_en="Lezama Lima's Paradiso",
    name_original="Paradiso",
    period_key="カリブ・スペイン語文学期",
    definition="ホセ・レサマ・リマ（1910-1976）が1966年に発表した長編。ハバナの少年ホセ・セミの成長を、ネオバロック詩的散文（極度に密度高く比喩的）で描く。同性愛描写でキューバ革命政府の検閲対象となった。ラテンアメリカ・ネオバロックの頂点。",
    background="20世紀前半ハバナのカトリック・ブルジョワ文化、レサマの「Orígenes」誌グループ。",
    development="サルドゥイ、アレナス、現代ラテンアメリカ・ネオバロック詩学全体の起源。",
    historical_context="キューバ革命下の文化検閲。",
    primary_source_url=BVMC+"obra/paradiso/",
    primary_source_type="BVMC: Paradiso",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="カブレラ・インファンテ『三匹の悲しい虎たち』",
    name_en="Cabrera Infante's Tres tristes tigres",
    name_original="Tres tristes tigres",
    period_key="カリブ・スペイン語文学期",
    definition="ギジェルモ・カブレラ・インファンテ（1929-2005）が1967年に発表した長編。革命前夜（1958）のハバナの夜を、口語キューバ語・言葉遊び・パロディで再構築する。タイトル自体が早口言葉。ラテンアメリカ言語実験小説の代表作。",
    background="革命前ハバナの夜のキャバレー文化、カブレラ・インファンテの亡命前経験。",
    development="サルドゥイ、ラテンアメリカ・ネオバロックの理論化に貢献。",
    historical_context="1958年ハバナの最後の自由な夜。",
    primary_source_url=BVMC+"obra/tres-tristes-tigres/",
    primary_source_type="BVMC: Tres tristes tigres",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="サルドゥイ『歌い手たちの故郷』",
    name_en="Sarduy's De donde son los cantantes",
    name_original="De donde son los cantantes",
    period_key="カリブ・スペイン語文学期",
    definition="セベロ・サルドゥイ（1937-1993）が1967年に発表した中編。キューバの三重起源（中国・アフリカ・スペイン）を三章で構成し、神学・記号論・パロディを融合する。ラテンアメリカ・ネオバロック理論の宣言的小説。",
    background="1960年代パリのテル・ケル誌・ラカン精神分析周辺、サルドゥイのキューバ亡命知識人圏。",
    development="ネオバロック・クィア・脱構築批評の交差点。",
    historical_context="1960年代パリ知識人圏とラテンアメリカ亡命。",
    primary_source_url=BVMC+"obra/de-donde-son-los-cantantes/",
    primary_source_type="BVMC: De donde son los cantantes",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アレナス『夜になるまえに』",
    name_en="Reinaldo Arenas's Antes que anochezca",
    name_original="Antes que anochezca",
    period_key="カリブ・スペイン語文学期",
    definition="レイナルド・アレナス（1943-1990）が1992年に没後刊行した自伝。革命前後キューバの貧困・同性愛・政治弾圧・収容所・マリエル亡命・ニューヨーク・エイズ自殺を、急速な口語で記述する。ラテンアメリカ・クィア証言文学の金字塔。",
    background="1960-70年代キューバ革命下の同性愛弾圧、アレナスのUMAP収容所体験。",
    development="現代ラテンアメリカ・クィア批評の中心テクスト、シュナーベル映画化（2000）。",
    historical_context="キューバ革命下の同性愛者迫害（UMAP収容所、1965-68）。",
    primary_source_url=ARCHIVE+"antesqueanochezca0000aren",
    primary_source_type="archive.org: Antes que anochezca (1992)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="バリェッホ『トリルセ』",
    name_en="César Vallejo's Trilce",
    name_original="Trilce",
    period_key="プレ・ブーム期",
    definition="セサル・バリェッホ（1892-1938）が1922年に発表した77詩篇集。ペルーの新造語・誤植・タイポグラフィー実験を駆使し、20世紀スペイン語詩で最も先鋭的な前衛詩集。エリオット『荒地』、ジョイス『ユリシーズ』と並ぶ1922年世界文学の革新点。",
    background="1920年代ペルーのアバンギャルド、バリェッホのトルヒーリョ収監体験(1920)。",
    development="ネルーダ、パス、20世紀スペイン語詩全体の規範。",
    historical_context="1920年代ペルー北部アバンギャルド運動。",
    primary_source_url=ARCHIVE+"trilce0000vall",
    primary_source_type="archive.org: Trilce (1922)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バリェッホ『人間的な詩』",
    name_en="César Vallejo's Poemas humanos",
    name_original="Poemas humanos",
    period_key="プレ・ブーム期",
    definition="バリェッホが1939年没後刊行された詩集。パリ亡命期（1923-1938）の詩を集め、「黒い石の上の白い石」「私はパリで死ぬだろう」を含む。20世紀ラテンアメリカ実存的詩の頂点。",
    background="バリェッホのパリ亡命と貧困、スペイン内戦体験。",
    development="ネルーダ、パスから現代ラテンアメリカ詩への決定的影響。",
    historical_context="スペイン内戦と第二次大戦前夜。",
    primary_source_url=ARCHIVE+"poemashumanos0000vall",
    primary_source_type="archive.org: Poemas humanos (1939)",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# G: テスティモニオ＋先住民＋現代女性作家 (10)
# ============================================================
add(**C, name_ja="ロドルフォ・ウォルシュ『オペラシオン・マサクレ』",
    name_en="Walsh's Operación masacre",
    name_original="Operación masacre",
    period_key="テスティモニオ期",
    definition="ロドルフォ・ウォルシュ（1927-1977）が1957年に発表した調査報告書。1956年アルゼンチン軍政のホセ・レオン・スアレス処刑事件を再構成し、9年前のカポーティ『冷血』(1965)を先取りした「ノンフィクション・ノベル」のラテンアメリカ起源。著者自身は1977年軍政下に殺害された。",
    background="1956年6月アラムブル政権による違法処刑、ウォルシュのジャーナリスト調査。",
    development="ガルシア・マルケス『予告された殺人の記録』、ラテンアメリカ・ナラティブ・ジャーナリズムの祖型。",
    historical_context="アルゼンチン1955-58年軍政期。",
    primary_source_url=ARCHIVE+"operacionmasacre0000wals",
    primary_source_type="archive.org: Operación masacre (1957)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ガレアーノ『収奪された大地——ラテンアメリカ五百年』",
    name_en="Galeano's Las venas abiertas de América Latina",
    name_original="Las venas abiertas de América Latina",
    period_key="テスティモニオ期",
    definition="エドゥアルド・ガレアーノ（1940-2015）が1971年に発表した歴史エッセイ。コロンブス到達から1970年までのラテンアメリカ被搾取史を、植民地経済・モノカルチャー・帝国主義の連鎖として叙述する。ラテンアメリカ被抑圧アイデンティティの基本書。",
    background="1960年代南米左翼の反帝国主義言説、従属論派経済学。",
    development="チャベス、エボ・モラレス等21世紀左翼政権のイデオロギー的源泉。",
    historical_context="南米軍政期前夜の左翼知識人運動。",
    primary_source_url=ARCHIVE+"lasvenasabiertasdeamerica0000gale",
    primary_source_type="archive.org: Las venas abiertas (1971)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ガレアーノ『火の記憶』三部作",
    name_en="Galeano's Memoria del fuego trilogy",
    name_original="Memoria del fuego (I-III)",
    period_key="テスティモニオ期",
    definition="ガレアーノが1982-86年に発表した三部作（『誕生』『顔と仮面』『風の世紀』）。コロンブス以前から1984年までのラテンアメリカを、断片化された歴史的場面の連鎖として再構築する。ラテンアメリカ集合的記憶の文学的記述。",
    background="1980年代ガレアーノのモンテビデオ亡命。",
    development="ロベルト・サヴィアーノら21世紀ナラティブ・ジャーナリズムの祖型。",
    historical_context="南米軍政期からの民主化過程。",
    primary_source_url=ARCHIVE+"memoriadelfuego0000gale",
    primary_source_type="archive.org: Memoria del fuego (1982-86)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マヤ・キチェ語劇『ラビナル・アチ』",
    name_en="K'iche'/Maya Drama Rabinal Achi",
    name_original="Rabinal Achí (Xajoj Tun)",
    period_key="先住民口承・現代インディヘナ",
    definition="グアテマラ・キチェ族のプレ・コロンビア期（15世紀以前推定）の儀式劇。ラビナルとキチェの戦士が捕虜の尊厳ある処刑を演じる。植民地化後も口承で保存され、19世紀ブラスール・ド・ブルブール神父が記録、2005年UNESCO無形文化遺産。アメリカ大陸唯一のプレ・コロンビア期演劇。",
    background="マヤ古典期後期キチェ族の儀礼演劇、植民地後の口承保存。",
    development="20世紀グアテマラ先住民演劇復興、アングル・アストゥリアスの神話学的源泉。",
    historical_context="プレ・コロンビア期マヤ高地社会。",
    primary_source_url=ARCHIVE+"rabinalachi0000bras",
    primary_source_type="archive.org: Brasseur de Bourbourg ed.",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ケチュア語悲歌『アプ・インカ・アタワルパマン』",
    name_en="Quechua Elegy Apu Inca Atawallpaman",
    name_original="Apu Inka Atawallpaman",
    period_key="先住民口承・現代インディヘナ",
    definition="16世紀カハマルカでスペイン軍によりインカ最後の皇帝アタワルパが処刑された(1533)後に作られたケチュア語哀歌。インカ崩壊の集合的悲嘆を表現し、20世紀アルゲダスがスペイン語に翻訳。アンデス先住民文学保存の象徴。",
    background="インカ帝国崩壊直後のケチュア社会の集合的喪失。",
    development="アルゲダス翻訳(1955)で20世紀インディヘニスモ文学の基礎テクスト化。",
    historical_context="インカ征服(1532-33)直後の先住民集団。",
    primary_source_url=ARCHIVE+"apuincaatawallpaman0000argu",
    primary_source_type="archive.org: Arguedas trans. (1955)",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エリクラ・チワイラフ（マプチェ詩）",
    name_en="Elicura Chihuailaf (Mapuche poetry)",
    name_original="Mapudungun-Spanish bilingual poetry",
    period_key="先住民口承・現代インディヘナ",
    definition="エリクラ・チワイラフ（1952-）はチリ・マプチェ族の二言語詩人。マプチェ語（マプドゥングン）とスペイン語の対訳形式で詩集『青い夢』(1995)他を発表し、2020年チリ国民文学賞を先住民として初受賞。現代インディヘナ詩の代表。",
    background="チリ南部マプチェ族の口承詩学、ポスト・ピノチェト先住民復権運動。",
    development="ラテンアメリカ・先住民バイリンガル詩運動の先駆。",
    historical_context="ポスト軍政チリの先住民権利運動。",
    primary_source_url=ARCHIVE+"sueoazul0000chih",
    primary_source_type="archive.org: De sueños azules y contrasueños",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="サマンタ・シュウェブリン『救援距離』",
    name_en="Samanta Schweblin's Distancia de rescate",
    name_original="Distancia de rescate",
    period_key="21世紀女性作家期",
    definition="サマンタ・シュウェブリン（1978-）が2014年に発表した中編。アルゼンチン田舎の母娘が農薬汚染で死に瀕し、瀕死の母と隣家の少年の対話で語られる。2017年ブッカー国際賞最終候補、2021年Netflix映画化。21世紀ラテンアメリカ・エコ・フェミニスト・ホラーの代表作。",
    background="アルゼンチン・パンパスのモンサント大豆汚染、21世紀環境正義運動。",
    development="エンリケス、オヘダ、カベソン・カマラとともにラテンアメリカ「新ゴシック」女性作家世代を形成。",
    historical_context="2010年代アルゼンチン環境危機・遺伝子組換え農業。",
    primary_source_url=BRITT+"topic/Distancia-de-rescate",
    primary_source_type="Britannica: Distancia de rescate",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マリアナ・エンリケス『焚き火で失ったもの』",
    name_en="Mariana Enríquez's Las cosas que perdimos en el fuego",
    name_original="Las cosas que perdimos en el fuego",
    period_key="21世紀女性作家期",
    definition="マリアナ・エンリケス（1973-）が2016年に発表した短編集（12篇）。アルゼンチン軍政の失踪者、貧困、ジェンダー暴力を、ホラー・ゴシックの形式で再構築する。21世紀ラテンアメリカ女性ゴシックの代表作で、24か国に翻訳。",
    background="アルゼンチン軍政「汚い戦争」(1976-83)の集合的トラウマ、2010年代フェミサイド危機。",
    development="シュウェブリン、オヘダ、カベソン・カマラと女性ゴシックの新世代を形成。",
    historical_context="2010年代アルゼンチンのジェンダー暴力危機（Ni Una Menos運動）。",
    primary_source_url=BRITT+"biography/Mariana-Enriquez",
    primary_source_type="Britannica: Mariana Enríquez",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ガブリエラ・カベソン・カマラ『中国少女』",
    name_en="Cabezón Cámara's Las aventuras de la China Iron",
    name_original="Las aventuras de la China Iron",
    period_key="21世紀女性作家期",
    definition="ガブリエラ・カベソン・カマラ（1968-）が2017年に発表した長編。エルナンデス『マルティン・フィエロ』(1872)の捨てられた妻「中国（La China）」を主人公に据え、19世紀パンパスをクィア・先住民連帯のロード小説として再構築。2020年ブッカー国際賞最終候補。",
    background="19世紀ガウチェスコ古典の脱植民地・脱家父長的書き換え。",
    development="エルナンデス古典をクィア・先住民視点で再読する21世紀ラテンアメリカ女性文学の代表例。",
    historical_context="2010年代アルゼンチン・フェミニスト・先住民権利運動。",
    primary_source_url=BRITT+"biography/Gabriela-Cabezon-Camara",
    primary_source_type="Britannica: Gabriela Cabezón Cámara",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="コンセイサオン・エヴァリスト『ブィチェーロのしずく』",
    name_en="Conceição Evaristo's Olhos d'água",
    name_original="Olhos d'água",
    period_key="ブラジル現代文学期",
    definition="コンセイサオン・エヴァリスト（1946-）が2014年に発表した短編集（15篇）。ブラジル黒人女性貧困層の声を、自伝的短編の形で記録する。彼女の概念「エスクレヴィヴェンシア（escrevivência＝書く＋生きる）」はブラジル黒人フェミニズム文学理論の中心概念。2015年ジャブティ賞受賞。",
    background="サンパウロ・ファヴェーラ出身のエヴァリストの自伝的位置取り、20世紀ブラジル黒人運動。",
    development="フェレス、イタマール・ヴィエイラ・ジュニオールらブラジル黒人文学の理論的中心。",
    historical_context="2010年代ブラジル人種・ジェンダー運動。",
    primary_source_url=BRITT+"biography/Conceicao-Evaristo",
    primary_source_type="Britannica: Conceição Evaristo",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# fourth_transform_tags attachments (>=18 axes)
# ============================================================
def _attach_axes(concept_name: str, ax_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("fourth_axes", [])
            c["fourth_axes"] = existing + ax_list
            return


_attach_axes("シロ・アレグリア『広く異郷なる世界』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"先住民共同体の集合的主体性は、AI時代に消失する個人主義主体に対する代替モデル。",
     "related_ai_phenomenon":"AI環境における共同体的主体造形の理論的可能性"}])
_attach_axes("アルゲダス『ヤワル・フィエスタ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"ケチュア語と西語のバイリンガル構築は、多言語LLMにおける周辺言語表象問題の理論的祖型。",
     "related_ai_phenomenon":"多言語LLMにおける少数言語表象"}])
_attach_axes("アルゲダス『深い川』", [
    {"axis":"翻訳","status":"rethinking",
     "rationale":"ケチュア音韻リズムを西語散文に組み込む技法は、AI翻訳における音韻・リズム再現問題と理論的に並行。",
     "related_ai_phenomenon":"AI翻訳における詩的リズム再現問題"}])
_attach_axes("アルゲダス『キツネ ——上のキツネと下のキツネ』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"作家自殺直前の日記を小説に組み込む構造は、AI時代の作家性・伝記的真実性の境界を理論化する基準点。",
     "related_ai_phenomenon":"AI時代の伝記的真実と作家性の境界"}])
_attach_axes("ルルフォ『ペドロ・パラモ』詳解", [
    {"axis":"物語","status":"rethinking",
     "rationale":"死者と生者が混在する非線形時間構造は、AI生成物語における時間構造の機械的構築可能性を理論化する。",
     "related_ai_phenomenon":"AI生成における非線形時間構造"}])
_attach_axes("フエンテス『アウラ』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"二人称現在形による読者の物語内主体化は、AI対話エージェントの二人称呼びかけと理論的に並行。",
     "related_ai_phenomenon":"AIエージェントによる二人称的主体構築"}])
_attach_axes("ボルヘス『フィクションズ』詳解", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"「ピエール・メナール」が同じテキストの異なる作者性を提起し、AI生成と人間執筆の同一テキスト問題を半世紀先取り。",
     "related_ai_phenomenon":"AI生成テキストと人間執筆の同一性問題"}])
_attach_axes("ボルヘス『八岐の園』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"分岐する時間の物語構造は、AI物語生成における枝分かれ確率木の文学的祖型。",
     "related_ai_phenomenon":"AI生成における物語の確率的分岐"}])
_attach_axes("ビオイ・カサーレス『モレルの発明』", [
    {"axis":"真正性","status":"rethinking",
     "rationale":"機械装置で永遠再生される人物像は、AI生成・ディープフェイクによる死者再生と理論的に並行する祖型。",
     "related_ai_phenomenon":"AI生成によるディープフェイク・死者再生"}])
_attach_axes("コルタサル『石蹴り遊び』構造", [
    {"axis":"受容","status":"rethinking",
     "rationale":"複数読み順を許容する開放小説の構造は、AI生成インタラクティブ・ナラティブの祖型。",
     "related_ai_phenomenon":"AI駆動インタラクティブ・ナラティブ"}])
_attach_axes("マシャード・デ・アシス『ドン・カズムッホ』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"信頼できない一人称話者の極限は、AIエージェントの語りの真偽判定問題と理論的に共振する古典的参照点。",
     "related_ai_phenomenon":"AIエージェントの語りの真偽判定"}])
_attach_axes("マリオ・デ・アンドラーデ『マクナイマ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"ブラジル諸地方口承を標準語小説に融合する技法は、多方言LLMにおける文化的混淆表象の理論的祖型。",
     "related_ai_phenomenon":"多言語・多方言LLMにおける文化的混淆"}])
_attach_axes("ロサ『大いなる奥地：諸小道』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"ネオロジズム・古語・口語による言語再構築は、LLMが標準語に同質化する世界での言語的多様性の参照点。",
     "related_ai_phenomenon":"LLMによる言語標準化と多様性の喪失"}])
_attach_axes("リスペクトル『G・H・の受難』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"ブルジョワ女性とゴキブリの「他者」遭遇による主体解体は、AI環境における人間中心主義解体の哲学的祖型。",
     "related_ai_phenomenon":"AI環境における人間中心主義の解体"}])
_attach_axes("プイグ『蜘蛛女のキス』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"ハリウッド映画消費がアイデンティティを構築する設定は、AI推奨アルゴリズムによるアイデンティティ形成と理論的に並行。",
     "related_ai_phenomenon":"AI推奨アルゴリズムによるアイデンティティ形成"}])
_attach_axes("ボラーニョ『野生の探偵たち』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"52人の証言の多声構造は、AI生成における集合的・分散的作者性の文学的祖型。",
     "related_ai_phenomenon":"AI生成における分散的作者性"}])
_attach_axes("ボラーニョ『2666』詳解", [
    {"axis":"正典","status":"rethinking",
     "rationale":"5部構成の遺作の正典化過程は、AI生成テキストの正典化基準問題を理論化する21世紀的参照点。",
     "related_ai_phenomenon":"AI生成テキストの正典化基準"}])
_attach_axes("カルペンティエル『この世の王国』", [
    {"axis":"真正性","status":"rethinking",
     "rationale":"「驚異的現実（lo real maravilloso）」概念は、AI生成における「驚異」と「現実」の境界問題の半世紀前の祖型。",
     "related_ai_phenomenon":"AI生成における驚異と現実の境界"}])
_attach_axes("バリェッホ『トリルセ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"新造語・誤植・タイポグラフィー実験は、AI生成における言語規範違反・創発的言語の理論的祖型。",
     "related_ai_phenomenon":"AI生成における言語規範違反と創発"}])
_attach_axes("シュウェブリン『救援距離』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"瀕死の母と少年の意識の融合は、AI環境における主体融合・分散主体の文学的探究。",
     "related_ai_phenomenon":"AI環境における意識融合・分散主体"}])
_attach_axes("コンセイサオン・エヴァリスト『ブィチェーロのしずく』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"「エスクレヴィヴェンシア（書く＋生きる）」概念は、AI執筆と生身の経験の不可分性を理論化する21世紀的参照点。",
     "related_ai_phenomenon":"AI執筆と生身の経験の不可分性"}])


# ============================================================
# cross_domain links (>=12 to PT/PHIL/AN)
# ============================================================
def _attach_cross(concept_name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


_attach_cross("シロ・アレグリア『広く異郷なる世界』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"アンデス先住民共同体・土地問題",
     "description":"アンデス先住民共同体（ayllu）の文学的記述はホセ・カルロス・マリアテギ、ジョン・ムラの先住民人類学と並行。"}])
_attach_cross("アルゲダス『ヤワル・フィエスタ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"祭祀人類学・闘牛儀礼",
     "description":"アンデス血の祭儀礼の文学的記述は20世紀後半アンデス祭祀人類学（Allen, Rasnake）の中心研究対象と並行。"}])
_attach_cross("アルゲダス『キツネ ——上のキツネと下のキツネ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"文化越境化（transculturación）",
     "description":"アンヘル・ラマ『移動する都市の周辺』(1982)による「文化越境化」概念の主たる文学的論証テクスト。"}])
_attach_cross("ルルフォ『ペドロ・パラモ』詳解", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"非線形時間ナラトロジー",
     "description":"68断章による非線形時間構造はジュネット・ナラトロジーの典型例。"}])
_attach_cross("ボルヘス『フィクションズ』詳解", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"形而上学的迷宮・無限論",
     "description":"ボルヘスの無限・分岐・反復はスピノザ、ライプニッツ、ショーペンハウアーの形而上学的読解と直接接続。"}])
_attach_cross("ボルヘス『八岐の園』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"多世界形而上学",
     "description":"分岐時間の形而上学はエヴェレット多世界解釈の哲学的読解と並行。"}])
_attach_cross("ボルヘス『他者の異端審問』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"系譜批評・遡及的影響理論",
     "description":"「カフカとその先駆者たち」のテーゼは現代受容理論・系譜批評の出発点。"}])
_attach_cross("ビオイ・カサーレス『モレルの発明』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"シミュレーション形而上学",
     "description":"機械再生による永遠の現存在は、ボストロムのシミュレーション論の哲学的祖型。"}])
_attach_cross("コルタサル『石蹴り遊び』構造", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"開放作品・読者参与",
     "description":"エコ『開かれた作品』(1962)理論の文学的実装としてイタリア記号論で頻繁に参照。"}])
_attach_cross("マシャード・デ・アシス『ドン・カズムッホ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"信頼できない一人称話者",
     "description":"ブース『フィクションのレトリック』(1961)、現代ナラトロジー全体の参照テクスト。"}])
_attach_cross("マリオ・デ・アンドラーデ『マクナイマ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"アントロポファジア・人類学的混淆論",
     "description":"オズワルド・デ・アンドラーデ「アントロポファジア宣言」(1928)はヴィヴェイロス・デ・カストロのパースペクティヴィズム人類学の前駆。"}])
_attach_cross("リスペクトル『G・H・の受難』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"他者・現象学的経験",
     "description":"ゴキブリとの遭遇によるG.H.の主体解体はエレーヌ・シクスー、デリダ、レヴィナス的他者哲学と並行。"}])
_attach_cross("カルペンティエル『この世の王国』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"カリブ・ヴードゥー文化人類学",
     "description":"ハイチ革命のヴードゥー的霊性記述は20世紀後半カリブ宗教人類学（メルヴィル・ハースコヴィッツ、アルフレッド・メトロー）と並行。"}])
_attach_cross("ガレアーノ『収奪された大地——ラテンアメリカ五百年』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"従属論・植民地経済人類学",
     "description":"ガレアーノの被搾取史は従属論派（カルドソ、フランク）経済社会人類学の文学的並行。"}])
_attach_cross("ロサ『大いなる奥地：諸小道』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"言語実験・新造語詩学",
     "description":"ロサのネオロジズムは現代スタイリスティクス・言語詩学の中心研究対象。"}])
_attach_cross("プイグ『蜘蛛女のキス』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"クィア批評・大衆文化人類学",
     "description":"監獄での同性愛・大衆映画消費はラテンアメリカ・クィア批評（モリ、リベラ）の中心テクスト。"}])
_attach_cross("ボラーニョ『2666』詳解", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"フェミサイド人類学",
     "description":"シウダー・フアレス殺害事件の文学的記述はメリッサ・ライト、ロサ・リンダ・フレゴソらフェミサイド人類学と並行。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="ラテンアメリカ",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid

        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            pkey = entry.pop("period_key", None)
            if pkey:
                entry["period_id"] = period_ids[pkey]
            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            name_to_id[entry["name_ja"]] = cid
            for ax in fourth_axes:
                try:
                    db.tag_fourth_transform(cid, **ax)
                    fourth_count += 1
                except LitDBError as e:
                    print(f"  [warn] fourth_transform tag failed for {entry['name_ja']}: {e}")
            for cd in cross_domain:
                try:
                    db.insert_cross_domain(
                        lit_entity_type="concept", lit_entity_id=cid,
                        target_db=cd["target_db"], link_type=cd["link_type"],
                        target_entity_id=cd.get("target_entity_id"),
                        target_entity_name=cd.get("target_entity_name"),
                        description=cd.get("description"))
                    cd_count += 1
                except LitDBError as e:
                    print(f"  [warn] cross_domain failed for {entry['name_ja']}: {e}")

        summary = db.progress_summary()
        print(f"[c26-w14] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c26-w14] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c26-w14] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
        print(f"[c26-w14] concepts entered: {len(CONCEPTS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
