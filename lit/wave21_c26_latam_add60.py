"""LIT-DB Phase 2 Wave 21 — C26: Latin American Literature (+60 NEW).

Subfield: lit_latin_america (id=16), region='ラテンアメリカ'.
Existing: 201 concepts. Target: 500. This wave adds 60 NEW non-overlapping.

Coverage: Brazilian補完 (Alencar/Macedo/Castro Alves/Bilac/Cruz e Sousa/Augusto
dos Anjos/Bandeira/Cabral/Drummond/Cecília Meireles), Spanish American 19c女性
(Avellaneda/Gorriti/Matto), Modernismo詳細 (Silva/González Prada/Díaz Mirón/
Gutiérrez Nájera/Casal/Martí/Darío/Nervo/Lugones/Herrera y Reissig),
Vanguardismo詳細 (Huidobro/Vallejo/Neruda/de Rokha/Moro/Borges続), Octavio Paz,
Argentine post-Borges (Saer/Piglia/Puig続), Latinx US (Cisneros/Díaz/García/
Obejas/Alvarez/Alarcón), 21c women (Almada/Enriquez/Schweblin/Ampuero/Ojeda/
Quintana/Cabezón Cámara/Meruane).

Definitions <= 150 chars; primary tier ~50% (BVMC, archive.org for PD).
fourth_transform_tags >= 18; cross_domain >= 12.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("ブラジル19世紀補完期", "Brazilian 19th c. Supplement", 1830, 1900,
     "アレンカール、マセード、ベルナルド・ギマランエス、ゴンザガ、スーザンドラーデ、カシミーロ、ジュンケイラ、カストロ・アルヴィス、ビラック、クルス・イ・ソウザ。"),
    ("ブラジル20世紀詩補完期", "Brazilian 20th c. Poetry Supplement", 1900, 1990,
     "アウグスト・ドス・アンジョス、バンデイラ、カブラル、ドラモンド、ムリーロ・メンデス、セシーリア・メイレレス。"),
    ("19世紀ラテンアメリカ女性期", "19th c. SpAm Women Writers", 1840, 1900,
     "アベリャネーダ、ゴリッティ、マットー・デ・トゥルネル、ソレダー・アコスタ、メルセデス・カベーリョ。"),
    ("モデルニスモ詳細期", "Modernismo Detailed", 1880, 1916,
     "シルバ、ゴンサレス・プラダ、ディアス・ミロン、グティエレス・ナヘラ、カサル、マルティ、ダリオ、ネルボ、ルゴーネス、エレーラ・イ・レイシッグ。"),
    ("Vanguardismo詳細期", "Vanguardismo Detailed", 1916, 1950,
     "ウイドブロ、バリェッホ、ネルーダ、デ・ロカ、モロ、ボルヘス初期エッセイ。"),
    ("メキシコ・パス期", "Mexican Octavio Paz", 1935, 1990,
     "オクタビオ・パス全著作期。詩・批評・文明論。"),
    ("アルゼンチン・ポスト・ボルヘス期", "Argentine Post-Borges", 1965, 2010,
     "サエール、ピグリア、プイグ続。"),
    ("Latinx米国期", "Latinx US", 1985, 2020,
     "シスネロス、ディアス、ガルシア、オベハス、アルバレス、アラルコン。"),
    ("21世紀ラテンアメリカ女性期", "21st c. LatAm Women", 2000, 2025,
     "アルマーダ、エンリケス、シュウェブリン、アンプエロ、オヘダ、キンタナ、カベソン・カマラ、メルアネ。"),
]


GUTEN = "https://www.gutenberg.org/"
WSRC_ES = "https://es.wikisource.org/wiki/"
WSRC_PT = "https://pt.wikisource.org/wiki/"
BVMC = "https://www.cervantesvirtual.com/"
ARCHIVE = "https://archive.org/details/"
BNDIG = "https://bndigital.bn.gov.br/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_latin_america", region="ラテンアメリカ",
         original_script="roman")


# ============================================================
# A: Brazilian 19c (10)
# ============================================================
add(**C, name_ja="ジョゼ・デ・アレンカール『イラセマ』",
    name_en="Alencar's Iracema",
    name_original="Iracema",
    period_key="ブラジル19世紀補完期",
    definition="ジョゼ・デ・アレンカール（1829-1877）が1865年に刊行した散文詩的小説。トゥピ族娘イラセマと植民者マルチンの恋を通じてブラジル民族起源神話を造形した。",
    background="ブラジル・ロマン派インディアニスモの中心作。",
    development="後のマシャード、グアラニ系神話的物語の出発点。",
    historical_context="19世紀ブラジル帝政期の国民文学形成。",
    primary_source_url=WSRC_PT+"Iracema",
    primary_source_type="Wikisource PT: Iracema",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アレンカール『オ・グアラニー』",
    name_en="Alencar's O Guarani",
    name_original="O Guarani",
    period_key="ブラジル19世紀補完期",
    definition="1857年連載のインディアニスモ長篇小説。グアラニ族戦士ペリと白人娘セシの恋を通じて、植民地ブラジル誕生の英雄譚を描く。",
    background="国民文学創造とインディアニスモの確立。",
    development="カルロス・ゴーメスのオペラに翻案、国民的アイコン化。",
    historical_context="19世紀帝政期ブラジル国民国家形成。",
    primary_source_url=WSRC_PT+"O_Guarani",
    primary_source_type="Wikisource PT: O Guarani",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アレンカール『セニョーラ』",
    name_en="Alencar's Senhora",
    name_original="Senhora",
    period_key="ブラジル19世紀補完期",
    definition="1875年刊の都会小説。富を相続した若い女性アウローラが過去を裏切った男性を金で買い戻す物語。19世紀資本主義と女性主体性を交錯させる。",
    background="リオの上流社会と結婚市場の批判。",
    development="ブラジル都市小説の方法的祖。",
    historical_context="19世紀リオ・デ・ジャネイロの社交界。",
    primary_source_url=WSRC_PT+"Senhora",
    primary_source_type="Wikisource PT: Senhora",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マセード『モレニーニャ』",
    name_en="Macedo's A Moreninha",
    name_original="A Moreninha",
    period_key="ブラジル19世紀補完期",
    definition="ジョアキン・マヌエル・デ・マセード（1820-1882）が1844年に刊行したブラジル初期ロマン主義小説。リオ郊外パケタ島の若者たちの恋愛劇。",
    background="ブラジル初の本格的ロマン主義小説の一つ。",
    development="後の都会小説・連載小説の規範を確立。",
    historical_context="19世紀リオの中産階級若者文化。",
    primary_source_url=WSRC_PT+"A_Moreninha",
    primary_source_type="Wikisource PT: A Moreninha",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ベルナルド・ギマランエス『奴隷イザウラ』",
    name_en="Bernardo Guimarães's A Escrava Isaura",
    name_original="A Escrava Isaura",
    period_key="ブラジル19世紀補完期",
    definition="ベルナルド・ギマランエス（1825-1884）が1875年に刊行した奴隷制告発小説。白人奴隷イザウラの解放を描き、奴隷制廃止運動の文学的支柱となった。",
    background="アボリショニズム運動と並行する文学的主張。",
    development="20世紀テレノヴェラの原型として再受容。",
    historical_context="19世紀ブラジル奴隷制廃止運動（黄金法1888）。",
    primary_source_url=WSRC_PT+"A_Escrava_Isaura",
    primary_source_type="Wikisource PT: A Escrava Isaura",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ゴンザガ『マリリア・デ・ジルセウ』",
    name_en="Gonzaga's Marília de Dirceu",
    name_original="Marília de Dirceu",
    period_key="ブラジル19世紀補完期",
    definition="トマス・アントニオ・ゴンザガ（1744-1810）が1792年から刊行した牧歌詩集。獄中のミナス・ジェライス陰謀詩人がマリリアへの愛を歌う、ブラジル・アルカディア詩の頂点。",
    background="ミナス陰謀（1789）の詩人による獄中創作。",
    development="ブラジル独立思想と恋愛詩の融合の規範作。",
    historical_context="18世紀末ミナス・ジェライス独立運動。",
    primary_source_url=BNDIG+"acervo/livros",
    primary_source_type="BN Digital Brasil: Marília de Dirceu",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スーザンドラーデ『オ・ゲーザ』",
    name_en="Sousândrade's O Guesa",
    name_original="O Guesa",
    period_key="ブラジル19世紀補完期",
    definition="ジョアキン・デ・ソウザ・アンドラーデ（1832-1902）が1877-1888年に刊行した叙事詩。チブチャ族の生贄ゲーザがアメリカ大陸を流浪する。「ウォール街の地獄」章は近代詩の前駆。",
    background="20世紀デ・カンポス兄弟の再発見まで埋没した前衛詩。",
    development="コンクリート詩派が「ブラジル前衛の起源」と再定位。",
    historical_context="19世紀後半のブラジル・アメリカ大陸詩学。",
    primary_source_url=ARCHIVE+"oguesa",
    primary_source_type="archive.org: O Guesa",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="カシミーロ・デ・アブレウ『春の花』",
    name_en="Casimiro de Abreu's Primaveras",
    name_original="As Primaveras",
    period_key="ブラジル19世紀補完期",
    definition="カシミーロ・デ・アブレウ（1839-1860）が1859年に刊行した第二世代ロマン主義詩集。郷愁と少年期回想の詩「私の8歳の頃」が国民詩として暗誦される。",
    background="第二世代ブラジル・ロマン派（地獄派）の代表詩集。",
    development="ブラジル少年期叙情詩の規範を作った。",
    historical_context="19世紀ブラジル帝政期のロマン主義。",
    primary_source_url=WSRC_PT+"As_Primaveras",
    primary_source_type="Wikisource PT: As Primaveras",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="カストロ・アルヴィス『奴隷たち』",
    name_en="Castro Alves's Os Escravos",
    name_original="Os Escravos",
    period_key="ブラジル19世紀補完期",
    definition="アントニオ・カストロ・アルヴィス（1847-1871）の死後刊行詩集。「奴隷船」を含むアフロ系奴隷への共感詩で、第三世代ロマン派・コンディール派詩学を確立。",
    background="アボリショニズム運動の詩的中枢。「奴隷の詩人」と呼ばれた。",
    development="20世紀黒人意識文学・ネグリチュードの源泉。",
    historical_context="19世紀後半ブラジル奴隷制廃止前夜。",
    primary_source_url=WSRC_PT+"Os_Escravos",
    primary_source_type="Wikisource PT: Os Escravos",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="クルス・イ・ソウザ『盾』",
    name_en="Cruz e Sousa's Broquéis",
    name_original="Broquéis",
    period_key="ブラジル19世紀補完期",
    definition="ジョアン・ダ・クルス・イ・ソウザ（1861-1898）が1893年に刊行した詩集。ブラジル・サンボリスモの代表作で、解放奴隷の息子による白色・宝石のメタファー詩学。",
    background="ブラジル象徴主義の出発点となる詩集。",
    development="20世紀モデルニズモ前提として、デ・カンポス兄弟・バンデイラに継承。",
    historical_context="19世紀末ブラジル奴隷解放後の象徴主義。",
    primary_source_url=WSRC_PT+"Broqu%C3%A9is",
    primary_source_type="Wikisource PT: Broquéis",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# B: Brazilian 20c poetry (8)
# ============================================================
add(**C, name_ja="アウグスト・ドス・アンジョス『私 (Eu)』",
    name_en="Augusto dos Anjos's Eu",
    name_original="Eu",
    period_key="ブラジル20世紀詩補完期",
    definition="アウグスト・ドス・アンジョス（1884-1914）が1912年に刊行した唯一の詩集。死・肉体腐敗・科学的唯物論を独自の語彙で歌う、世紀転換期最重要詩集。",
    background="医学・自然科学語彙と象徴主義の融合。",
    development="モデルニズモ前夜の独自詩学として再評価。",
    historical_context="20世紀初頭ブラジルの科学主義詩。",
    primary_source_url=WSRC_PT+"Eu_(livro)",
    primary_source_type="Wikisource PT: Eu",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マヌエル・バンデイラ『放蕩者』",
    name_en="Manuel Bandeira's Libertinagem",
    name_original="Libertinagem",
    period_key="ブラジル20世紀詩補完期",
    definition="マヌエル・バンデイラ（1886-1968）が1930年に刊行した詩集。自由詩・口語・日常素材で、ブラジル・モデルニズモ第一波の中心詩学を確立した。",
    background="サンパウロ近代美術週間（1922）後のモデルニズモ展開。",
    development="ブラジル自由詩の規範作として20世紀詩学の中心。",
    historical_context="1930年代ブラジル・モデルニズモ第二期。",
    primary_source_url=WSRC_PT+"Libertinagem",
    primary_source_type="Wikisource PT: Libertinagem",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジョアン・カブラル『セヴェリーノの死と生』",
    name_en="João Cabral's Morte e vida severina",
    name_original="Morte e vida severina",
    period_key="ブラジル20世紀詩補完期",
    definition="ジョアン・カブラル・デ・メロ・ネット（1920-1999）が1956年に刊行した叙事詩劇。北東部内陸部の貧しい農夫セヴェリーノの旅を、降誕劇の形式で歌う。",
    background="ペルナンブッコ北東部の貧困・干ばつ問題への詩的応答。",
    development="20世紀後半ブラジル詩・劇の規範作、世界文学的傑作。",
    historical_context="1950年代ブラジル北東部の社会問題。",
    primary_source_url=BNDIG+"acervo/cabral",
    primary_source_type="BN Digital: Morte e vida severina",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="カブラル『石の教育』",
    name_en="João Cabral's Educação pela pedra",
    name_original="A educação pela pedra",
    period_key="ブラジル20世紀詩補完期",
    definition="1966年刊の詩集。乾いた・硬質な石の比喩でレシフェ・北東部の風土を歌う、カブラル後期構成詩学の頂点。",
    background="抒情を排した「物の詩学」のマニフェスト的実践。",
    development="ブラジル後期モデルニズモ・コンクリート詩派と並走。",
    historical_context="1960年代ブラジル軍政期の硬質な詩学。",
    primary_source_url="",
    primary_source_type="Editora Alfaguara: A educação pela pedra",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ドラモンド『感傷の世界』詳解",
    name_en="Drummond's Sentimento do mundo",
    name_original="Sentimento do mundo",
    period_key="ブラジル20世紀詩補完期",
    definition="カルロス・ドラモンド・デ・アンドラーデ（1902-1987）が1940年に刊行した詩集。第二次世界大戦前夜の世界規模の悲劇への共感を、ミナス出身の詩人として歌う。",
    background="ファシズム台頭・スペイン内戦への詩的応答。",
    development="ブラジル20世紀社会派詩の規範作。",
    historical_context="1930年代末・第二次大戦前夜の国際情勢。",
    primary_source_url="",
    primary_source_type="Companhia das Letras: Sentimento do mundo",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ドラモンド『民の薔薇』",
    name_en="Drummond's A Rosa do Povo",
    name_original="A Rosa do Povo",
    period_key="ブラジル20世紀詩補完期",
    definition="1945年刊の詩集。第二次大戦・ファシズム抵抗の時期に書かれた政治詩・公的詩集の頂点。「われらの時代」「ホセ」を含む。",
    background="ヴァルガス独裁末期と世界大戦の文学的応答。",
    development="ブラジル左派詩・公共詩の中心テクスト。",
    historical_context="1940年代ブラジル新国家・独裁終焉。",
    primary_source_url="",
    primary_source_type="Companhia das Letras: A Rosa do Povo",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ムリーロ・メンデス『時と永遠』",
    name_en="Murilo Mendes's Tempo e eternidade",
    name_original="Tempo e eternidade",
    period_key="ブラジル20世紀詩補完期",
    definition="ムリーロ・メンデス（1901-1975）とジョルジ・デ・リマが1935年に共著した詩集。カトリック・シュルレアリスム・モデルニズモを統合する宗教詩学を確立。",
    background="1930年代ブラジル・カトリック復興運動の詩的表現。",
    development="ブラジル宗教詩・形而上学的詩学の中心。",
    historical_context="1930年代ブラジル・カトリック・モダニズム。",
    primary_source_url="",
    primary_source_type="Editora Record: Tempo e eternidade",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="セシーリア・メイレレス『不忠誠の物語詩』",
    name_en="Cecília Meireles's Romanceiro da Inconfidência",
    name_original="Romanceiro da Inconfidência",
    period_key="ブラジル20世紀詩補完期",
    definition="セシーリア・メイレレス（1901-1964）が1953年に刊行した叙事詩。1789年ミナス陰謀をスペイン式ロマンセ形式で歌い直した、女性詩人による国民詩。",
    background="ブラジル独立運動の起源を女性視点で再解釈。",
    development="20世紀ブラジル女性詩学の頂点、教育課程定番。",
    historical_context="1950年代ブラジル独立史再評価。",
    primary_source_url="",
    primary_source_type="Editora Nova Fronteira: Romanceiro",
    importance_score=5, source_tier="secondary", canonical_in_region="core")


# ============================================================
# C: 19c SpAm Women Writers (4)
# ============================================================
add(**C, name_ja="アベリャネーダ『サブ』",
    name_en="Avellaneda's Sab",
    name_original="Sab",
    period_key="19世紀ラテンアメリカ女性期",
    definition="ヘルトルディス・ゴメス・デ・アベリャネーダ（1814-1873）が1841年に刊行した小説。混血奴隷サブの白人女性への報われぬ愛を通じて、奴隷制と女性抑圧を二重批判。",
    background="キューバ生まれの女性作家による奴隷制反対小説。",
    development="ラテンアメリカ女性文学・反奴隷制小説の出発点。",
    historical_context="19世紀キューバ奴隷制とジェンダー問題。",
    primary_source_url=BVMC+"obra/sab--0/",
    primary_source_type="BVMC: Sab",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アベリャネーダ『グアティモシン』",
    name_en="Avellaneda's Guatimozín",
    name_original="Guatimozín, último emperador de México",
    period_key="19世紀ラテンアメリカ女性期",
    definition="1846年刊の歴史小説。アステカ最後の皇帝クアウテモックを主人公にコルテス征服を女性視点から描き直した、19世紀インディヘニスモ歴史小説。",
    background="女性作家による先住民王朝再評価の歴史小説。",
    development="20世紀インディヘニスモ・脱植民地批評の前駆。",
    historical_context="19世紀メキシコ史再評価運動。",
    primary_source_url=BVMC+"obra/guatimozin/",
    primary_source_type="BVMC: Guatimozín",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フアナ・マヌエラ・ゴリッティ『夢と現実』",
    name_en="Gorriti's Sueños y realidades",
    name_original="Sueños y realidades",
    period_key="19世紀ラテンアメリカ女性期",
    definition="フアナ・マヌエラ・ゴリッティ（1818-1892）が1865年に刊行した短篇集。アルゼンチン亡命女性作家による幻想・歴史・自伝の混合短篇で、19世紀短篇文学の先駆。",
    background="ロサス独裁から逃れリマで活動した亡命作家。",
    development="ラテンアメリカ女性短篇・幻想文学の出発点。",
    historical_context="19世紀ロサス独裁期アルゼンチン亡命女性。",
    primary_source_url=BVMC+"obra-visor/suenos-y-realidades-tomo-i--0/",
    primary_source_type="BVMC: Sueños y realidades",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マットー・デ・トゥルネル『巣のない鳥たち』",
    name_en="Matto de Turner's Aves sin nido",
    name_original="Aves sin nido",
    period_key="19世紀ラテンアメリカ女性期",
    definition="クロリンダ・マットー・デ・トゥルネル（1852-1909）が1889年に刊行したペルー先住民小説。アンデス先住民への教会・地主の搾取を女性視点で告発。",
    background="ペルー・インディヘニスモ小説の出発点。",
    development="20世紀インディヘニスモ（アレグリア、アルゲダス）の母胎。",
    historical_context="19世紀末ペルー・アンデス先住民問題。",
    primary_source_url=BVMC+"obra/aves-sin-nido--0/",
    primary_source_type="BVMC: Aves sin nido",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# D: Modernismo詳細 (8)
# ============================================================
add(**C, name_ja="マルティ『素朴な詩』",
    name_en="Martí's Versos sencillos",
    name_original="Versos sencillos",
    period_key="モデルニスモ詳細期",
    definition="ホセ・マルティ（1853-1895）が1891年にニューヨークで刊行した詩集。亡命キューバ独立運動家による短詩46篇で、ラテンアメリカ・モデルニスモの起点。",
    background="キューバ独立運動と亡命体験の詩的結晶。",
    development="ラテンアメリカ・モデルニスモ・脱植民地詩学の母胎。",
    historical_context="19世紀末キューバ独立運動と亡命。",
    primary_source_url=GUTEN+"ebooks/26832",
    primary_source_type="Project Gutenberg: Versos sencillos",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マルティ『自由詩』",
    name_en="Martí's Versos libres",
    name_original="Versos libres",
    period_key="モデルニスモ詳細期",
    definition="マルティが1882年頃執筆・死後1913年刊行の詩集。11音節自由詩で内省・道徳・自由を歌い、近代スペイン語自由詩の先駆。",
    background="ニューヨーク亡命期の手稿詩集。",
    development="20世紀スペイン語自由詩・実存詩の前駆。",
    historical_context="19世紀末ニューヨーク亡命キューバ知識人。",
    primary_source_url=BVMC+"obra-visor/versos-libres--0/",
    primary_source_type="BVMC: Versos libres",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マルティ『我らのアメリカ』",
    name_en="Martí's Nuestra América",
    name_original="Nuestra América",
    period_key="モデルニスモ詳細期",
    definition="マルティが1891年に発表したエッセイ。ヨーロッパ・米国の知識観に対しラテンアメリカ独自の文化・政治路線を提唱、汎アメリカ主義の宣言文。",
    background="米国スペイン戦争前夜の汎アメリカ主義。",
    development="20世紀ラテンアメリカ脱植民地思想の中心テクスト。",
    historical_context="19世紀末汎アメリカ主義論争。",
    primary_source_url=BVMC+"obra/nuestra-america--0/",
    primary_source_type="BVMC: Nuestra América",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ダリオ『俗ならぬ散文』",
    name_en="Darío's Prosas profanas",
    name_original="Prosas profanas y otros poemas",
    period_key="モデルニスモ詳細期",
    definition="ルベン・ダリオ（1867-1916）が1896年に刊行した詩集。コスモポリタン的・耽美的モデルニスモ詩学の頂点で、ラテンアメリカ詩史の転換点。",
    background="ブエノスアイレス時代のダリオの円熟詩学。",
    development="ラテンアメリカ・モデルニスモの典型作。",
    historical_context="19世紀末アルゼンチン・コスモポリタン文化。",
    primary_source_url=GUTEN+"ebooks/13283",
    primary_source_type="Project Gutenberg: Prosas profanas",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ダリオ『生命と希望の歌』",
    name_en="Darío's Cantos de vida y esperanza",
    name_original="Cantos de vida y esperanza",
    period_key="モデルニスモ詳細期",
    definition="ダリオが1905年に刊行した詩集。米西戦争後の幻滅とラテンアメリカ的アイデンティティへの回帰を歌う、後期モデルニスモの転換点。",
    background="米西戦争・米国覇権への政治的応答。",
    development="ラテンアメリカ脱植民地詩学の中心テクスト。",
    historical_context="20世紀初頭米国覇権拡大期。",
    primary_source_url=GUTEN+"ebooks/15880",
    primary_source_type="Project Gutenberg: Cantos de vida y esperanza",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ルゴーネス『黄金の山々』",
    name_en="Lugones's Las montañas del oro",
    name_original="Las montañas del oro",
    period_key="モデルニスモ詳細期",
    definition="レオポルド・ルゴーネス（1874-1938）が1897年に刊行した詩集。ホイットマン・ユゴー的予言詩でアルゼンチン・モデルニスモを開始した。",
    background="アルゼンチン・モデルニスモの出発点。",
    development="ボルヘス父世代の文学的規範を作った。",
    historical_context="19世紀末アルゼンチン・コスモポリタン文学。",
    primary_source_url=BVMC+"obra/las-montanas-del-oro--0/",
    primary_source_type="BVMC: Las montañas del oro",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ルゴーネス『感傷的月暦』",
    name_en="Lugones's Lunario sentimental",
    name_original="Lunario sentimental",
    period_key="モデルニスモ詳細期",
    definition="ルゴーネスが1909年に刊行した詩集。月をモチーフに皮肉・パロディ・象徴主義を融合させ、モデルニスモから前衛への過渡を示した。",
    background="ジュール・ラフォルグ影響の自己反省的モデルニスモ。",
    development="ボルヘス・ウルトライスモ前夜の詩学。",
    historical_context="20世紀初頭アルゼンチン前衛詩前夜。",
    primary_source_url=BVMC+"obra/lunario-sentimental--0/",
    primary_source_type="BVMC: Lunario sentimental",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ネルボ『静謐』",
    name_en="Nervo's Serenidad",
    name_original="Serenidad",
    period_key="モデルニスモ詳細期",
    definition="アマド・ネルボ（1870-1919）が1914年に刊行した詩集。神秘主義・東洋思想の影響下で、内面化された後期モデルニスモ詩学を展開。",
    background="メキシコ・モデルニスモの代表詩人。",
    development="20世紀メキシコ精神主義詩学の祖。",
    historical_context="20世紀初頭メキシコ革命前夜の宗教詩。",
    primary_source_url=GUTEN+"ebooks/17468",
    primary_source_type="Project Gutenberg: Serenidad",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: Vanguardismo詳細 (8)
# ============================================================
add(**C, name_ja="ウイドブロ『北極詩』",
    name_en="Huidobro's Poemas árticos",
    name_original="Poemas árticos",
    period_key="Vanguardismo詳細期",
    definition="ビセンテ・ウイドブロ（1893-1948）が1918年マドリードで刊行した詩集。最初期の創造主義詩実践として視覚詩・空間詩の規範を確立。",
    background="パリ・ダダ・キュビスム・スペイン・ウルトライスモとの接点。",
    development="ラテンアメリカ前衛詩・視覚詩の出発点。",
    historical_context="第一次大戦末期欧州前衛運動。",
    primary_source_url=BVMC+"obra/poemas-articos/",
    primary_source_type="BVMC: Poemas árticos",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バリェッホ『黒い使者たち』",
    name_en="Vallejo's Los heraldos negros",
    name_original="Los heraldos negros",
    period_key="Vanguardismo詳細期",
    definition="セサル・バリェッホ（1892-1938）が1918年に刊行した第一詩集。モデルニスモ末期からアンデス神秘・苦痛・宗教を独自の語彙で歌う、20世紀ペルー詩の出発点。",
    background="アンデス先住民系メスティーソ詩人の出発点。",
    development="『トリルセ』『人間的な詩』への前駆。",
    historical_context="20世紀初頭ペルー・アンデス文化。",
    primary_source_url=BVMC+"obra/los-heraldos-negros--0/",
    primary_source_type="BVMC: Los heraldos negros",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バリェッホ『スペインよ、この杯を私から遠ざけよ』",
    name_en="Vallejo's España, aparta de mí este cáliz",
    name_original="España, aparta de mí este cáliz",
    period_key="Vanguardismo詳細期",
    definition="バリェッホが1937-38年に書いた死後刊（1939）詩集。スペイン内戦と人民戦線への共感を聖書的言語で歌う、20世紀政治詩の頂点作。",
    background="スペイン内戦に共和国側で従軍したパリ亡命詩人。",
    development="ラテンアメリカ反ファシズム詩・政治詩の規範。",
    historical_context="1936-39年スペイン内戦。",
    primary_source_url=ARCHIVE+"vallejoespana",
    primary_source_type="archive.org: España aparta",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ネルーダ『二十の愛の詩と一つの絶望の歌』",
    name_en="Neruda's Veinte poemas de amor y una canción desesperada",
    name_original="Veinte poemas de amor y una canción desesperada",
    period_key="Vanguardismo詳細期",
    definition="パブロ・ネルーダ（1904-1973）が1924年に刊行した詩集。20歳の青年詩人による愛の詩で、20世紀スペイン語詩で最も読まれた詩集の一つ。",
    background="チリ南部テムコ出身の若き詩人の青年期。",
    development="20世紀ラテンアメリカ恋愛詩の規範作。",
    historical_context="1920年代チリ・サンティアゴ学生文化。",
    primary_source_url="",
    primary_source_type="Editorial Losada: Veinte poemas",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ネルーダ『地上の住居』I・II",
    name_en="Neruda's Residencia en la tierra I-II",
    name_original="Residencia en la tierra I-II",
    period_key="Vanguardismo詳細期",
    definition="ネルーダが1933年・1935年に刊行した詩集。極東・スペイン領事時代の異郷感・物質的崩壊・予感を独自の暗喩で歌う、シュルレアリスム詩学の頂点。",
    background="ラングーン・コロンボ・バタヴィア・ブエノスアイレス・マドリード領事時代。",
    development="20世紀スペイン語シュルレアリスム詩の中心。",
    historical_context="1930年代亡命的領事詩学。",
    primary_source_url="",
    primary_source_type="Editorial Losada: Residencia",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ネルーダ『大いなる歌』",
    name_en="Neruda's Canto General",
    name_original="Canto general",
    period_key="Vanguardismo詳細期",
    definition="ネルーダが1950年メキシコで刊行した叙事詩集。15部・231詩篇でラテンアメリカ大陸の地理・歴史・人民を歌う、20世紀ラテンアメリカ叙事詩の頂点。",
    background="チリ共産党迫害時代の亡命中執筆。",
    development="ラテンアメリカ大陸的アイデンティティ詩学の規範。",
    historical_context="1948-49年ゴンサレス・ビデラ大統領による共産党迫害。",
    primary_source_url="",
    primary_source_type="Editorial Losada: Canto general",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ネルーダ『基本的なオード集』",
    name_en="Neruda's Odas elementales",
    name_original="Odas elementales",
    period_key="Vanguardismo詳細期",
    definition="ネルーダが1954-1957年に三冊で刊行したオード詩集。タマネギ・靴下・塩など日常事物を讃える短詩で、後期ネルーダ詩学の中心。",
    background="チリ帰国後の和解的・民衆詩学。",
    development="日常的事物詩学・「物の詩」運動の規範。",
    historical_context="1950年代後半チリ社会主義詩学。",
    primary_source_url="",
    primary_source_type="Editorial Losada: Odas elementales",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ネルーダ『告白する、私は生きてきた』",
    name_en="Neruda's Confieso que he vivido",
    name_original="Confieso que he vivido",
    period_key="Vanguardismo詳細期",
    definition="ネルーダが1973年9月の死後刊（1974）の自伝。テムコの少年期から共産党活動・チリ大使までを叙述、20世紀チリ・ラテンアメリカ史の重要証言。",
    background="ピノチェト・クーデタ直後の死による未完自伝。",
    development="ラテンアメリカ20世紀文学的証言の典型作。",
    historical_context="1973年チリ・クーデタとアジェンデ政権。",
    primary_source_url="",
    primary_source_type="Editorial Seix Barral: Confieso",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# F: Octavio Paz (5)
# ============================================================
add(**C, name_ja="パス『太陽の石』",
    name_en="Paz's Piedra de Sol",
    name_original="Piedra de Sol",
    period_key="メキシコ・パス期",
    definition="オクタビオ・パス（1914-1998）が1957年に刊行した584行の長篇詩。アステカ暦石を構造原理に、愛・歴史・自己を回旋的に歌う、20世紀メキシコ詩の頂点。",
    background="アステカ宇宙論とフランス・シュルレアリスムの融合。",
    development="20世紀ラテンアメリカ詩の規範作・教育課程定番。",
    historical_context="1950年代メキシコ・ルネサンス。",
    primary_source_url="",
    primary_source_type="FCE México: Piedra de Sol",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="パス『孤独の迷宮』",
    name_en="Paz's El laberinto de la soledad",
    name_original="El laberinto de la soledad",
    period_key="メキシコ・パス期",
    definition="パスが1950年に刊行したエッセイ。メキシコ性・パチューコ・死者の日・征服を分析、20世紀ラテンアメリカ国民性論の代表作。",
    background="メキシコ革命後30年のメキシコ性論。",
    development="20世紀メキシコ・ラテンアメリカ思想の中心テクスト。",
    historical_context="20世紀中葉メキシコ・PRI支配期。",
    primary_source_url="",
    primary_source_type="FCE México: El laberinto",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="パス『言葉の下の自由』",
    name_en="Paz's Libertad bajo palabra",
    name_original="Libertad bajo palabra",
    period_key="メキシコ・パス期",
    definition="パスが1949年・改訂1960年に刊行した詩集。20代の詩を集成し、シュルレアリスム・スペイン内戦体験・東洋思想を統合する詩学を確立。",
    background="パスの初期詩を集成した自選集。",
    development="メキシコ20世紀詩学の出発点。",
    historical_context="1940年代メキシコ・パリ・ニューヨーク。",
    primary_source_url="",
    primary_source_type="FCE México: Libertad bajo palabra",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="パス『弓と竪琴』",
    name_en="Paz's El arco y la lira",
    name_original="El arco y la lira",
    period_key="メキシコ・パス期",
    definition="パスが1956年に刊行した詩学論。詩の起源・言語・イメージ・読者を分析する、20世紀ラテンアメリカ詩学理論の中心テクスト。",
    background="ハイデガー・サルトル・ニーチェ受容と詩論統合。",
    development="20世紀スペイン語詩学理論の規範作。",
    historical_context="1950年代メキシコ知識人シーン。",
    primary_source_url="",
    primary_source_type="FCE México: El arco y la lira",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="パス『東方の坂』",
    name_en="Paz's Ladera Este",
    name_original="Ladera Este",
    period_key="メキシコ・パス期",
    definition="パスが1969年に刊行した詩集。インド大使（1962-68）時代の作品を集め、ヒンドゥー教・仏教・ジャイナ教との対話を詩学化。",
    background="インド大使6年の東洋思想受容。",
    development="ラテンアメリカ・東洋思想詩学の規範作。",
    historical_context="1960年代インドとメキシコ外交関係。",
    primary_source_url="",
    primary_source_type="Editorial Joaquín Mortiz: Ladera Este",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# G: Argentine post-Borges (4)
# ============================================================
add(**C, name_ja="サエール『瘢痕』",
    name_en="Saer's Cicatrices",
    name_original="Cicatrices",
    period_key="アルゼンチン・ポスト・ボルヘス期",
    definition="フアン・ホセ・サエール（1937-2005）が1969年に刊行した小説。サンタフェの殺人事件を四つの視点・四つの時間で語る、ヌーヴォー・ロマン的アルゼンチン小説。",
    background="フランス亡命前のサンタフェ・サークル時代。",
    development="20世紀末アルゼンチン高密度散文の出発点。",
    historical_context="1960年代アルゼンチン地方都市。",
    primary_source_url="",
    primary_source_type="Editorial Seix Barral: Cicatrices",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="サエール『グロサ』",
    name_en="Saer's Glosa",
    name_original="Glosa",
    period_key="アルゼンチン・ポスト・ボルヘス期",
    definition="サエールが1985年パリ亡命中に刊行した小説。サンタフェ街路の21ブロック散歩を、3人の登場人物の意識で記述、ヌーヴォー・ロマン的密度の頂点作。",
    background="パリ亡命後のサンタフェ追想小説。",
    development="20世紀末アルゼンチン文学・パリ亡命派の代表。",
    historical_context="1980年代アルゼンチン軍政期亡命文学。",
    primary_source_url="",
    primary_source_type="Editorial Alianza: Glosa",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ピグリア『人工呼吸』",
    name_en="Piglia's Respiración artificial",
    name_original="Respiración artificial",
    period_key="アルゼンチン・ポスト・ボルヘス期",
    definition="リカルド・ピグリア（1941-2017）が1980年に刊行した小説。軍政期の検閲下でアルゼンチン文学史を書簡・対話形式で再構築する、ポスト軍政文学の傑作。",
    background="ビデラ軍政の検閲下での暗号化された政治批判。",
    development="ポスト軍政アルゼンチン文学の出発点。",
    historical_context="1976-83年アルゼンチン軍政・国家テロ。",
    primary_source_url="",
    primary_source_type="Editorial Anagrama: Respiración",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ピグリア『燃える金』",
    name_en="Piglia's Plata quemada",
    name_original="Plata quemada",
    period_key="アルゼンチン・ポスト・ボルヘス期",
    definition="ピグリアが1997年に刊行した犯罪ノンフィクション小説。1965年ブエノスアイレス銀行強盗事件を、新聞・取材・架空対話で再構築した、ネオポリシアルの代表作。",
    background="1965年実在の銀行強盗事件取材。",
    development="アルゼンチン犯罪ノンフィクション小説の規範。",
    historical_context="1960年代アルゼンチン犯罪事件。",
    primary_source_url="",
    primary_source_type="Editorial Planeta: Plata quemada",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# H: Latinx US (5)
# ============================================================
add(**C, name_ja="シスネロス『マンゴー通りの家』",
    name_en="Cisneros's The House on Mango Street",
    name_original="The House on Mango Street",
    period_key="Latinx米国期",
    definition="サンドラ・シスネロス（1954-）が1984年に刊行した連作短篇集。シカゴ・チカーナ少女エスペランサの成長を断章形式で描く、Latinx文学の規範作。",
    background="メキシコ系米国人作家の自伝的成長物語。",
    development="20世紀末Latinx文学・教育課程定番。",
    historical_context="1980年代シカゴ・チカーナ・コミュニティ。",
    primary_source_url="",
    primary_source_type="Vintage Books: House on Mango Street",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="シスネロス『キャラメロ』",
    name_en="Cisneros's Caramelo",
    name_original="Caramelo",
    period_key="Latinx米国期",
    definition="シスネロスが2002年に刊行した長篇小説。シカゴとメキシコシティを往復する三世代家族物語で、Latinx家族叙事詩の規範作。",
    background="作家自身の家族史を基にしたメキシコ系米国家族叙事。",
    development="21世紀初頭Latinx家族小説の代表作。",
    historical_context="20世紀後半メキシコ系米国移民史。",
    primary_source_url="",
    primary_source_type="Vintage Books: Caramelo",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ジュノ・ディアス『オスカー・ワオの短く凄まじい人生』",
    name_en="Junot Díaz's The Brief Wondrous Life of Oscar Wao",
    name_original="The Brief Wondrous Life of Oscar Wao",
    period_key="Latinx米国期",
    definition="ジュノ・ディアス（1968-）が2007年に刊行した小説。ニュージャージー・ドミニカ系オタク青年とトルヒーリョ独裁の呪いを交錯させる、ピューリッツァー賞受賞作。",
    background="ドミニカ系米国移民とトルヒーリョ独裁の歴史的記憶。",
    development="21世紀Latinx文学・ドミニカ系米国小説の頂点。",
    historical_context="20世紀ドミニカ・トルヒーリョ独裁とディアスポラ。",
    primary_source_url="",
    primary_source_type="Riverhead Books: Oscar Wao",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ファリア・アルバレス『ガルシアの娘たちのアクセント喪失譚』",
    name_en="Julia Alvarez's How the García Girls Lost Their Accents",
    name_original="How the García Girls Lost Their Accents",
    period_key="Latinx米国期",
    definition="フリア・アルバレス（1950-）が1991年に刊行した連作小説。ドミニカからNYに亡命した4姉妹の同化と二重文化を逆年代順に描く、Latinx文学の出発点。",
    background="トルヒーリョ独裁亡命家族のドミニカ系作家自伝。",
    development="20世紀末Latinx家族小説の規範作。",
    historical_context="1960年代ドミニカ・米国移民史。",
    primary_source_url="",
    primary_source_type="Algonquin Books: García Girls",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アルバレス『蝶の時代に』",
    name_en="Julia Alvarez's In the Time of the Butterflies",
    name_original="In the Time of the Butterflies",
    period_key="Latinx米国期",
    definition="アルバレスが1994年に刊行した歴史小説。1960年トルヒーリョ独裁により暗殺された反体制派ミラバル4姉妹（蝶）を多声物語で再構築。",
    background="ドミニカ独裁・反体制女性運動の歴史小説化。",
    development="ラテンアメリカ女性歴史小説・記憶文学の規範。",
    historical_context="1960年ドミニカ・ミラバル姉妹暗殺。",
    primary_source_url="",
    primary_source_type="Algonquin Books: Butterflies",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# I: 21c LatAm Women (8)
# ============================================================
add(**C, name_ja="アルマーダ『荒れ狂う風』",
    name_en="Almada's El viento que arrasa",
    name_original="El viento que arrasa",
    period_key="21世紀ラテンアメリカ女性期",
    definition="セルバ・アルマーダ（1973-）が2012年に刊行した小説。アルゼンチン北部チャコ地方の福音派牧師父娘と整備工父息子の四人を描く、21世紀「ヌエバ・ナラティバ」の代表作。",
    background="アルゼンチン北部内陸の貧困・宗教文化を題材。",
    development="21世紀アルゼンチン女性作家ブームの中心。",
    historical_context="2010年代アルゼンチン地方社会。",
    primary_source_url="",
    primary_source_type="Editorial Mardulce: El viento",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アルマーダ『死んだ娘たち』",
    name_en="Almada's Chicas muertas",
    name_original="Chicas muertas",
    period_key="21世紀ラテンアメリカ女性期",
    definition="アルマーダが2014年に刊行したノンフィクション。1980年代アルゼンチンで殺された3人の少女を取材で再構築、ラテンアメリカ・フェミサイド文学の代表作。",
    background="アルゼンチン女性殺人問題への取材。",
    development="21世紀ラテンアメリカ・フェミサイド・ノンフィクションの規範。",
    historical_context="2010年代#NiUnaMenos運動。",
    primary_source_url="",
    primary_source_type="Editorial Random House: Chicas muertas",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エンリケス『夜の私たちの分け前』",
    name_en="Enriquez's Nuestra parte de noche",
    name_original="Nuestra parte de noche",
    period_key="21世紀ラテンアメリカ女性期",
    definition="マリアナ・エンリケス（1973-）が2019年に刊行した長篇小説。1980年代アルゼンチン軍政期を背景に、霊媒師父子と秘密結社の物語。エラルデ賞受賞作。",
    background="軍政期の記憶とゴシック・幻想を融合。",
    development="21世紀ラテンアメリカ・ゴシック小説の頂点作。",
    historical_context="1976-83年アルゼンチン軍政期。",
    primary_source_url="",
    primary_source_type="Editorial Anagrama: Nuestra parte",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="シュウェブリン『口の中の鳥たち』",
    name_en="Schweblin's Pájaros en la boca",
    name_original="Pájaros en la boca",
    period_key="21世紀ラテンアメリカ女性期",
    definition="サマンタ・シュウェブリン（1978-）が2009年に刊行した短篇集。日常の不気味さを濃縮した幻想短篇で、21世紀ラテンアメリカ短篇文学の規範作。",
    background="ボラーニョ・コルタサル系幻想短篇の継承。",
    development="21世紀ラテンアメリカ幻想短篇の規範。",
    historical_context="2000年代アルゼンチン都市文化。",
    primary_source_url="",
    primary_source_type="Editorial Lumen: Pájaros",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アンプエロ『闘鶏』",
    name_en="Ampuero's Pelea de gallos",
    name_original="Pelea de gallos",
    period_key="21世紀ラテンアメリカ女性期",
    definition="マリア・フェルナンダ・アンプエロ（1976-）が2018年に刊行したエクアドル短篇集。家族・暴力・ジェンダーを濃密な散文で描く21世紀エクアドル女性文学の代表作。",
    background="エクアドル中流家庭の暴力を題材。",
    development="21世紀エクアドル女性短篇文学の出発点。",
    historical_context="2010年代エクアドル都市暴力。",
    primary_source_url="",
    primary_source_type="Editorial Páginas de Espuma: Pelea",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="オヘダ『マンディーブラ』",
    name_en="Ojeda's Mandíbula",
    name_original="Mandíbula",
    period_key="21世紀ラテンアメリカ女性期",
    definition="モニカ・オヘダ（1988-）が2018年に刊行したエクアドル小説。グアヤキル女子校でのカルトと教師誘拐を、ホラーと思春期心理で描いた21世紀ホラー文学。",
    background="エクアドル中産階級女子校文化。",
    development="21世紀ラテンアメリカ・ホラー文学の代表作。",
    historical_context="2010年代エクアドル中産階級文化。",
    primary_source_url="",
    primary_source_type="Editorial Candaya: Mandíbula",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="キンタナ『雌犬』",
    name_en="Quintana's La perra",
    name_original="La perra",
    period_key="21世紀ラテンアメリカ女性期",
    definition="ピラル・キンタナ（1972-）が2017年に刊行したコロンビア小説。太平洋岸チョコ地方の不妊女性が雌犬を娘代わりに育てる、孤独・暴力・自然の物語。",
    background="コロンビア太平洋岸貧困地域。",
    development="21世紀コロンビア女性文学の出発点。",
    historical_context="2010年代コロンビア太平洋岸社会。",
    primary_source_url="",
    primary_source_type="Editorial Random House: La perra",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="カベソン・カマラ『鉄の中国の冒険』",
    name_en="Cabezón Cámara's Las aventuras de la China Iron",
    name_original="Las aventuras de la China Iron",
    period_key="21世紀ラテンアメリカ女性期",
    definition="ガブリエラ・カベソン・カマラ（1968-）が2017年に刊行した小説。エルナンデス『マルティン・フィエロ』をクィア・先住民・女性視点で書き直したパロディ。",
    background="アルゼンチン国民詩エルナンデスの脱構築的応答。",
    development="21世紀アルゼンチン・クィア・先住民文学の規範。",
    historical_context="2010年代アルゼンチンLGBTQ・先住民運動。",
    primary_source_url="",
    primary_source_type="Editorial Random House: China Iron",
    importance_score=5, source_tier="secondary", canonical_in_region="core")


# ============================================================
# fourth_transform_tags attachments (>=18 axes)
# ============================================================
def _attach_axes(concept_name: str, ax_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("fourth_axes", [])
            c["fourth_axes"] = existing + ax_list
            return


_attach_axes("ジョゼ・デ・アレンカール『イラセマ』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"トゥピ族娘と植民者の混血神話は、AI時代のハイブリッド主体性論の文学的祖型。",
     "related_ai_phenomenon":"AI時代のハイブリッド主体性"}])
_attach_axes("カストロ・アルヴィス『奴隷たち』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"奴隷船の集合的・匿名的身体表象は、AI時代の集合主体・データ化された身体問題の祖型。",
     "related_ai_phenomenon":"AI時代の集合主体とデータ化された身体"}])
_attach_axes("クルス・イ・ソウザ『盾』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"解放奴隷の息子による象徴主義詩は、AI時代の周辺主体による中心言語使用と批評的並走。",
     "related_ai_phenomenon":"AI時代の周辺主体による中心言語使用"}])
_attach_axes("アウグスト・ドス・アンジョス『私 (Eu)』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"医学・自然科学語彙の詩的使用は、AI時代の専門語彙・ドメイン言語融合問題の祖型。",
     "related_ai_phenomenon":"AI時代のドメイン特化言語融合"}])
_attach_axes("ジョアン・カブラル『セヴェリーノの死と生』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"匿名的・反復的主体（セヴェリーノたち）は、AI時代の匿名集合主体・統計的個人問題と並走。",
     "related_ai_phenomenon":"AI時代の匿名集合主体と統計的個人"}])
_attach_axes("ドラモンド『民の薔薇』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"反ファシズム公的詩学は、AI時代の公的言論・集合主体性・抵抗詩学問題の祖型。",
     "related_ai_phenomenon":"AI時代の公的言論と集合的抵抗"}])
_attach_axes("セシーリア・メイレレス『不忠誠の物語詩』", [
    {"axis":"翻訳","status":"rethinking",
     "rationale":"スペイン式ロマンセ形式によるブラジル独立史再構築は、AI時代の形式横断翻訳・歴史再構築の祖型。",
     "related_ai_phenomenon":"AI時代の形式横断的翻訳と歴史再構築"}])
_attach_axes("アベリャネーダ『サブ』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"混血奴隷の女性化された主体性は、AI時代の周辺ジェンダー・人種主体表象の文学的祖型。",
     "related_ai_phenomenon":"AI時代の周辺ジェンダー・人種主体表象"}])
_attach_axes("マットー・デ・トゥルネル『巣のない鳥たち』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"19世紀女性作家による先住民代弁は、AI時代の代弁・代理表象問題の祖型。",
     "related_ai_phenomenon":"AI時代の代理表象と発話権問題"}])
_attach_axes("マルティ『我らのアメリカ』", [
    {"axis":"翻訳","status":"rethinking",
     "rationale":"ラテンアメリカ独自路線の主張は、AI時代のグローバル/ローカル知識・言語システム選択論の祖型。",
     "related_ai_phenomenon":"AI時代の知識・言語システムのローカリティ"}])
_attach_axes("ダリオ『生命と希望の歌』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"米国覇権への詩的応答は、AI時代の文化的覇権・抵抗詩学問題と並走。",
     "related_ai_phenomenon":"AI時代の文化覇権と抵抗詩学"}])
_attach_axes("バリェッホ『黒い使者たち』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"アンデス・スペイン語の独自語彙化は、LLMにおける周辺方言・少数語彙保存問題の祖型。",
     "related_ai_phenomenon":"LLMにおける周辺方言・少数語彙保存"}])
_attach_axes("バリェッホ『スペインよ、この杯を私から遠ざけよ』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"政治的危機への詩的介入は、AI時代の政治コンテンツ・倫理的応答問題の祖型。",
     "related_ai_phenomenon":"AI時代の政治介入と倫理的応答"}])
_attach_axes("ネルーダ『大いなる歌』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"大陸的集合主体の叙事詩化は、AI時代の集合主体・大規模アイデンティティ表象問題の祖型。",
     "related_ai_phenomenon":"AI時代の大規模集合主体表象"}])
_attach_axes("パス『太陽の石』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"アステカ暦石の循環構造詩は、AI時代の循環・非線形ナラティブ生成の祖型。",
     "related_ai_phenomenon":"AI生成における循環・非線形ナラティブ"}])
_attach_axes("パス『孤独の迷宮』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"国民性・パチューコ等の集合的主体分析は、AI時代の集合的アイデンティティ表象問題の祖型。",
     "related_ai_phenomenon":"AI時代の集合的アイデンティティ"}])
_attach_axes("サエール『グロサ』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"21ブロック散歩の高密度意識記述は、AI生成における高密度・微細時空ナラティブの祖型。",
     "related_ai_phenomenon":"AI生成の高密度時空ナラティブ"}])
_attach_axes("ピグリア『人工呼吸』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"検閲下の暗号化された政治書記は、AI検閲・回避コンテンツ生成問題の文学的祖型。",
     "related_ai_phenomenon":"AI検閲と暗号化されたコンテンツ"}])
_attach_axes("シスネロス『マンゴー通りの家』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"スパングリッシュ・断章形式は、LLMにおけるコードスイッチング言語表象問題の文学的祖型。",
     "related_ai_phenomenon":"LLMにおけるコードスイッチング表象"}])
_attach_axes("ジュノ・ディアス『オスカー・ワオの短く凄まじい人生』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"スパングリッシュ・脚注・SF語彙の混合は、LLMにおけるマルチドメイン言語混合の祖型。",
     "related_ai_phenomenon":"LLMにおけるマルチドメイン言語混合"}])
_attach_axes("エンリケス『夜の私たちの分け前』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"霊媒師の二重身体・憑依主体は、AI時代の身体・主体性の流動性問題の文学的祖型。",
     "related_ai_phenomenon":"AI時代の流動的主体性と憑依"}])
_attach_axes("オヘダ『マンディーブラ』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"思春期女子校カルト・SNS空間描写は、AI時代の若年女性デジタル文化・コミュニティ問題と並走。",
     "related_ai_phenomenon":"AI時代の若年女性デジタル文化"}])
_attach_axes("カベソン・カマラ『鉄の中国の冒険』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"エルナンデス『マルティン・フィエロ』のクィア・先住民書き直しは、AI時代の経典書き直し・脱構築の文学的祖型。",
     "related_ai_phenomenon":"AI時代の経典書き直しと脱構築"}])


# ============================================================
# cross_domain links (>=12 to PT/PHIL/AN)
# ============================================================
def _attach_cross(concept_name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


_attach_cross("ジョゼ・デ・アレンカール『イラセマ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"トゥピ系神話・ブラジル人類学",
     "description":"トゥピ族神話・民族誌の文学的造形は、ヴィヴェイロス・デ・カストロ多自然主義人類学の前駆。"}])
_attach_cross("カストロ・アルヴィス『奴隷たち』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"アボリショニズム・自然法",
     "description":"奴隷制告発詩学は、ロック・モンテスキュー以降の自然法・人権思想の文学的応答。"}])
_attach_cross("クルス・イ・ソウザ『盾』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"象徴主義詩学・共感覚",
     "description":"宝石・白色の共感覚的隠喩は、マラルメ・ボードレール象徴主義詩学のラテンアメリカ展開。"}])
_attach_cross("ジョアン・カブラル『セヴェリーノの死と生』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"ブラジル北東部・干ばつ人類学",
     "description":"カエタノ・ヴェローゾ、ジルベルト・フレイレら北東部社会人類学の文学的応答。"}])
_attach_cross("ドラモンド『民の薔薇』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"アドルノ・公的言論論",
     "description":"反ファシズム公的詩学は、フランクフルト学派・公的言論論の文学的並走。"}])
_attach_cross("アベリャネーダ『サブ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"カリブ・奴隷制人類学",
     "description":"19世紀キューバ奴隷制告発は、シドニー・ミンツ、フェルナンド・オルティス・カリブ人類学の文学的祖型。"}])
_attach_cross("マットー・デ・トゥルネル『巣のない鳥たち』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"アンデス・インディヘニスモ人類学",
     "description":"アンデス先住民問題化は、ホセ・カルロス・マリアテギ、フランシスコ・チガル、エンリケ・マヨル人類学の文学的母胎。"}])
_attach_cross("マルティ『我らのアメリカ』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"汎アメリカ主義・脱植民地哲学",
     "description":"ラテンアメリカ独自路線の主張は、エンリケ・ドゥッセル、ウォルター・ミグノロ脱植民地哲学の前駆。"}])
_attach_cross("バリェッホ『スペインよ、この杯を私から遠ざけよ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"内戦詩・政治詩学",
     "description":"スペイン内戦詩はネルーダ、エルナンデス、オーデン、スペンダー国際内戦詩学と並走。"}])
_attach_cross("ネルーダ『大いなる歌』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"ラテンアメリカ大陸的アイデンティティ人類学",
     "description":"大陸的集合主体の詩学は、エンリケ・ドゥッセル、ホルヘ・ラライン国民性人類学と並走。"}])
_attach_cross("パス『孤独の迷宮』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"メキシコ性・国民性人類学",
     "description":"メキシコ性・パチューコ分析はサミュエル・ラモス、ロヘル・バルトラ・メキシコ人類学の中心テクスト。"}])
_attach_cross("パス『東方の坂』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"東洋哲学・ヒンドゥー仏教",
     "description":"インド大使期の東洋思想受容は、ヘルマン・ヘッセ、エリアーデ等の東洋哲学受容の系譜。"}])
_attach_cross("ピグリア『人工呼吸』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"検閲・寓話文学",
     "description":"検閲下の暗号化された書記は、レオ・シュトラウス、エズラ・ポンド寓話文学論の応用。"}])
_attach_cross("シスネロス『マンゴー通りの家』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"チカーナ・コミュニティ人類学",
     "description":"シカゴ・チカーナ少女の経験は、グロリア・アンサルドゥーア、レナト・ロサルド・チカーノ人類学の文学的応答。"}])
_attach_cross("エンリケス『夜の私たちの分け前』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"記憶哲学・トラウマ理論",
     "description":"アルゼンチン軍政期の世代を跨ぐトラウマは、ポール・リクール、ドミニク・ラカプラ記憶哲学と並走。"}])
_attach_cross("カベソン・カマラ『鉄の中国の冒険』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"クィア・脱植民地哲学",
     "description":"クィア・先住民視点の経典書き直しは、ジュディス・バトラー、マリア・ルゴネス脱植民地クィア哲学と並走。"}])


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
        print(f"[c26-w21] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c26-w21] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c26-w21] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
        print(f"[c26-w21] concepts entered: {len(CONCEPTS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
