"""LIT-DB Phase 2 Wave 19 — C26: Latin American Literature (+60 NEW).

Subfield: lit_latin_america (id=16), region='ラテンアメリカ'.
Existing: 141 concepts. Target: 500. This wave adds 60 NEW non-overlapping.

Coverage: コロニアル詳細, 19世紀補完, 20世紀前半, Vanguardismo,
Boom補完, Brazilian深掘り, Postdictadura.

Definitions <= 150 chars; primary tier >= 60% (BVMC, Project Gutenberg, BNDigital).
fourth_transform_tags >= 18; cross_domain >= 12.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("コロニアル詳細期", "Colonial Detail (16-18c)", 1500, 1800,
     "サアグン、ラス・カサス、ガルシラソ、グアマン・ポマ、バルブエナ、シグエンサ、フレイレら植民地年代記・詩・歴史。"),
    ("19世紀補完期", "19th c. Supplement", 1810, 1900,
     "ガウチェスコ、ロマン主義、コスチュンブリスモ、初期モデルニスモを補完。"),
    ("20世紀前半期", "Early 20th c. (Pre-Vanguard)", 1900, 1945,
     "バスコンセロス、エンリケス・ウレーニャ、アルト、キローガ、リベラ、ガジェゴス、グイラルデス、マリアテギ。"),
    ("Vanguardismo期", "Vanguardismo (1920s-30s)", 1916, 1945,
     "ウイドブロ、ヒロンド、デ・ロハ、マリオ／オズワルド・デ・アンドラーデ、ムリーロ・メンデス、ジョルジ・デ・リマ。"),
    ("Boom補完期", "Boom Supplement", 1955, 1985,
     "ドノソ、フエンテス後期、バルガス・リョサ後期、ガルシア・マルケス後期、コルタサル後期、サバト、オネッティ追加作。"),
    ("ブラジル深掘り期", "Brazilian Deep Dive", 1880, 2000,
     "マシャード後期、リマ・バレット、グラシリアーノ・ラモス、ジョルジ・アマード、ヴェリッシモ、テレス、ヒルスト、リスペクトル後期、フォンセカ、ウバルド・リベイロ。"),
    ("ポスト独裁期", "Postdictadura (1980s-2010s)", 1980, 2015,
     "ボラーニョ後期、エルティト、サンブラ、メルアネ、ジェフタノヴィッチ、フランス、リベラ・レテリエル、スカルメタ。"),
]


GUTEN = "https://www.gutenberg.org/"
WIKI_ES = "https://es.wikipedia.org/wiki/"
WIKI_PT = "https://pt.wikipedia.org/wiki/"
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
# A: コロニアル詳細 (10)
# ============================================================
add(**C, name_ja="サアグン『新スペイン全史』",
    name_en="Sahagún's Historia general de las cosas de Nueva España",
    name_original="Historia general de las cosas de Nueva España",
    period_key="コロニアル詳細期",
    definition="フランシスコ会修道士サアグン（1499-1590）が16世紀後半にナワトル語と西語の対訳で編んだ12巻の民族誌。フィレンツェ写本が代表的伝本でアステカ人類学の基礎。",
    background="フランシスコ会の先住民教化のためのナワ族文化体系的調査。",
    development="近代民族誌・人類学の祖型として20世紀メキシコ人類学で再評価。",
    historical_context="16世紀後半の植民地メキシコ・先住民文化記録。",
    primary_source_url=BVMC+"obra/historia-general-de-las-cosas-de-nueva-espana/",
    primary_source_type="BVMC: Historia general (Sahagún)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ラス・カサス『インディアスの破壊についての簡潔な報告』詳解",
    name_en="Las Casas's Brevísima relación (close reading)",
    name_original="Brevísima relación de la destrucción de las Indias",
    period_key="コロニアル詳細期",
    definition="ドミニコ会士ラス・カサス（1484-1566）が1552年に刊行した告発書。スペイン征服者の先住民虐殺を地域別に列挙し、後の「黒い伝説」の基底となった。",
    background="新世界での征服者の暴虐を国王カルロス一世に告発する目的で執筆。",
    development="近代人権思想・脱植民地批評・現代インディヘニスモの基礎。",
    historical_context="16世紀バリャドリッド論争（先住民の合理性をめぐる論争）。",
    primary_source_url=GUTEN+"ebooks/20321",
    primary_source_type="Project Gutenberg: Brevísima relación",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="インカ・ガルシラソ『フロリダ誌』",
    name_en="Inca Garcilaso's La Florida del Inca",
    name_original="La Florida del Inca",
    period_key="コロニアル詳細期",
    definition="インカ・ガルシラソ・デ・ラ・ベガ（1539-1616）が1605年に刊行した北米遠征記。エルナンド・デ・ソトのフロリダ遠征を、メスティーソの視点で再構成した最初期の植民地史書。",
    background="ガルシラソの母方インカ系譜と、父方スペイン系譜の二重視点。",
    development="『コメンタリオス・レアレス』の前駆的方法論として読まれる。",
    historical_context="16世紀北米植民地化の初期記録。",
    primary_source_url=BVMC+"obra/la-florida-del-inca--0/",
    primary_source_type="BVMC: La Florida del Inca",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="グアマン・ポマ『新しい記録と良き統治』",
    name_en="Guaman Poma's Nueva crónica y buen gobierno",
    name_original="Nueva corónica y buen gobierno",
    period_key="コロニアル詳細期",
    definition="アンデス先住民フェリペ・グアマン・ポマ・デ・アヤラ（c.1535-c.1616）が1615年頃に著した1200頁・398図版の年代記。インカ史と植民地批判をスペイン王に直訴する形式。",
    background="アンデス先住民エリートの植民地体験と統治改革要求。",
    development="20世紀発見以降、脱植民地批評・先住民史学の中心テクスト。",
    historical_context="17世紀初頭ペルー副王領下の先住民エリート。",
    primary_source_url="https://poma.kb.dk/",
    primary_source_type="Royal Library Copenhagen digital ms.",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バルブエナ『メキシコの偉大さ』",
    name_en="Bernardo de Balbuena's Grandeza mexicana",
    name_original="Grandeza mexicana",
    period_key="コロニアル詳細期",
    definition="ベルナルド・デ・バルブエナ（1562-1627）が1604年に刊行した詩。メキシコ・シティの賛美をテルセート連で歌い、植民地バロック都市詩の規範を確立した。",
    background="17世紀初頭メキシコ・シティの植民地都市文化。",
    development="ソル・フアナ、シグエンサらメキシコ・バロックの前提を作った。",
    historical_context="17世紀初頭ヌエバ・エスパーニャ副王領の都市文化。",
    primary_source_url=BVMC+"obra/grandeza-mexicana--0/",
    primary_source_type="BVMC: Grandeza mexicana",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バルブエナ『エル・ベルナルド』",
    name_en="Balbuena's El Bernardo",
    name_original="El Bernardo, o victoria de Roncesvalles",
    period_key="コロニアル詳細期",
    definition="バルブエナが1624年に刊行した24歌の壮大叙事詩。スペイン英雄ベルナルド・デル・カルピオを主人公に、ロンセスバーリェスの戦いを再構築する植民地スペイン語叙事詩の頂点。",
    background="ヌエバ・エスパーニャ副王領で書かれたスペイン国民英雄叙事詩。",
    development="アメリカ大陸初の本格的英雄叙事詩として植民地詩の規範。",
    historical_context="17世紀植民地詩学のヨーロッパ古典模倣。",
    primary_source_url=BVMC+"obra/el-bernardo-o-victoria-de-roncesvalles/",
    primary_source_type="BVMC: El Bernardo",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="シグエンサ・イ・ゴンゴラ『パルテニコの勝利』",
    name_en="Sigüenza y Góngora's Triunfo parténico",
    name_original="Triunfo parténico",
    period_key="コロニアル詳細期",
    definition="カルロス・デ・シグエンサ・イ・ゴンゴラ（1645-1700）が1683年に刊行した詩学論集。メキシコ大学の聖母無原罪詩賛コンクール記録。植民地クリオージョ知識人ネットワークの記録。",
    background="17世紀メキシコ・シティのクリオージョ知識人サークル。",
    development="メキシコ・クリオージョ意識・地域アイデンティティの先駆的記録。",
    historical_context="ヌエバ・エスパーニャ副王領の文芸サロン文化。",
    primary_source_url=BVMC+"obra/triunfo-partenico/",
    primary_source_type="BVMC: Triunfo parténico",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="フレイレ『エル・カルネロ』",
    name_en="Juan Rodríguez Freyle's El carnero",
    name_original="El carnero",
    period_key="コロニアル詳細期",
    definition="フアン・ロドリゲス・フレイレ（1566-c.1640）が1638年頃に著したヌエバ・グラナダ年代記。歴史記述に逸話・スキャンダル・口承を織り交ぜ、植民地クリオージョ語りの祖型を作った。",
    background="17世紀前半ボゴタ・サンタフェの植民地社会観察。",
    development="現代コロンビア小説の祖として再評価され、ガルシア・マルケスへの間接的影響。",
    historical_context="ヌエバ・グラナダ副王領の植民地社会。",
    primary_source_url=BVMC+"obra/el-carnero/",
    primary_source_type="BVMC: El carnero",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="オーニャ『手なずけられたアラウコ』",
    name_en="Pedro de Oña's Arauco domado",
    name_original="Arauco domado",
    period_key="コロニアル詳細期",
    definition="ペドロ・デ・オーニャ（1570-1643）が1596年に刊行した叙事詩。エルシーリャ『ラ・アラウカーナ』への返答として、スペイン征服者ガルシア・ウルタド・デ・メンドーサを称揚する。",
    background="エルシーリャ叙事詩への政治的対抗としてのチリ植民地詩。",
    development="チリ最初のクリオージョ詩人作品としてチリ国民文学の起源。",
    historical_context="16世紀末チリ・アラウコ戦争の植民地視点。",
    primary_source_url=BVMC+"obra/arauco-domado--0/",
    primary_source_type="BVMC: Arauco domado",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="アンドレス・ベリョ『アメリカの森への祈り』",
    name_en="Andrés Bello's Silvas americanas",
    name_original="Silvas americanas",
    period_key="コロニアル詳細期",
    definition="アンドレス・ベリョ（1781-1865）が1823-26年に発表した二編の詩（『アメリカの詩への招待』『熱帯の農業』）。新生独立アメリカの自然・労働を古典的シルバ詩形で歌う独立期文化宣言。",
    background="独立期ベネズエラ・コロンビアの新国民文化形成。",
    development="ラテンアメリカ独立後文化の文学的礎石。",
    historical_context="1810-30年代ラテンアメリカ独立戦争期。",
    primary_source_url=BVMC+"obra/silvas-americanas/",
    primary_source_type="BVMC: Silvas americanas",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# B: 19世紀補完 (10)
# ============================================================
add(**C, name_ja="バルトロメ・イダルゴ『シエリトス』",
    name_en="Bartolomé Hidalgo's Cielitos",
    name_original="Cielitos y Diálogos patrióticos",
    period_key="19世紀補完期",
    definition="バルトロメ・イダルゴ（1788-1822）がアルゼンチン独立戦争期に作ったガウチョ口語詩。ガウチェスコ・ジャンルの最初期作品で、後のアスカスビ・エルナンデスの祖型。",
    background="リオ・デ・ラ・プラタ独立戦争期のガウチョ兵士口語文化。",
    development="アスカスビ、デル・カンポ、エルナンデス『マルティン・フィエロ』の起源。",
    historical_context="1810-20年代ラ・プラタ独立戦争。",
    primary_source_url=BVMC+"obra/cielitos-y-dialogos-patrioticos/",
    primary_source_type="BVMC: Cielitos y Diálogos",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="エチェベリーア『囚われの女』",
    name_en="Echeverría's La cautiva",
    name_original="La cautiva",
    period_key="19世紀補完期",
    definition="エステバン・エチェベリーア（1805-1851）が1837年に発表した叙事詩。先住民に拉致された白人女性マリアと夫ブリアンのパンパスでの逃避行を歌い、アルゼンチン・ロマン主義の出発点。",
    background="1830年代アルゼンチンのロサス独裁体制とパンパス先住民問題。",
    development="アルゼンチン国民ロマン主義詩の規範。",
    historical_context="ロサス独裁期のフロンティア戦争。",
    primary_source_url=BVMC+"obra/la-cautiva--0/",
    primary_source_type="BVMC: La cautiva",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="サルミエント『地方の思い出』",
    name_en="Sarmiento's Recuerdos de provincia",
    name_original="Recuerdos de provincia",
    period_key="19世紀補完期",
    definition="ドミンゴ・F・サルミエント（1811-1888）が1850年に発表した自伝的回想録。サンフアン州の幼少期と教育者としての形成を記し、ラテンアメリカ近代自伝の規範。",
    background="サルミエントのチリ亡命中の自己形成記述。",
    development="ラテンアメリカ自伝・教育エッセイの祖型。",
    historical_context="ロサス独裁下の亡命知識人。",
    primary_source_url=BVMC+"obra/recuerdos-de-provincia--0/",
    primary_source_type="BVMC: Recuerdos de provincia",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="エスタニスラオ・デル・カンポ『ファウスト』",
    name_en="Estanislao del Campo's Fausto",
    name_original="Fausto: Impresiones del gaucho Anastasio el Pollo",
    period_key="19世紀補完期",
    definition="エスタニスラオ・デル・カンポ（1834-1880）が1866年に発表したガウチェスコ詩。ガウチョのアナスタシオがブエノスアイレスでグノー・オペラ『ファウスト』を見た感想を語る、ガウチェスコのパロディ的頂点。",
    background="1860年代ブエノスアイレスのオペラ受容とガウチョ文化対比。",
    development="エルナンデス『マルティン・フィエロ』と並ぶガウチェスコ古典。",
    historical_context="ブエノスアイレス都市化と地方文化の対比。",
    primary_source_url=BVMC+"obra/fausto--impresiones-del-gaucho-anastasio-el-pollo/",
    primary_source_type="BVMC: Fausto",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アスカスビ『サントス・ベガ』",
    name_en="Hilario Ascasubi's Santos Vega",
    name_original="Santos Vega o Los mellizos de la flor",
    period_key="19世紀補完期",
    definition="イラリオ・アスカスビ（1807-1875）が1872年に発表した13,000行のガウチェスコ叙事詩。伝説的パイヤドール（即興詩人）サントス・ベガを主人公に、パンパス文化を百科全書的に記述。",
    background="アスカスビのフランス亡命中、パンパス民俗の集合的記憶化。",
    development="エルナンデス『マルティン・フィエロ』への直接の前駆。",
    historical_context="19世紀後半パンパス文化の文学的記録化。",
    primary_source_url=BVMC+"obra/santos-vega-o-los-mellizos-de-la-flor/",
    primary_source_type="BVMC: Santos Vega",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="マンシーリャ『ランケル先住民地への遠足』",
    name_en="Mansilla's Una excursión a los indios ranqueles",
    name_original="Una excursión a los indios ranqueles",
    period_key="19世紀補完期",
    definition="ルシオ・V・マンシーリャ（1831-1913）が1870年に発表した先住民地探訪記。ランケル族との外交使節としての18日間を、人類学的観察と政治的考察で記す。アルゼンチン・ノンフィクションの規範。",
    background="1870年マンシーリャのコルドバ・パンパス国境軍司令官時代。",
    development="ガウチェスコと近代人類学の橋渡し。",
    historical_context="アルゼンチン砂漠征服戦争前夜の先住民政策。",
    primary_source_url=BVMC+"obra/una-excursion-a-los-indios-ranqueles--0/",
    primary_source_type="BVMC: Una excursión a los indios ranqueles",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フアン・マリア・グティエレス『アメリカ詩集』",
    name_en="Juan María Gutiérrez's América poética",
    name_original="América poética",
    period_key="19世紀補完期",
    definition="フアン・マリア・グティエレス（1809-1878）が1846年に編纂したラテンアメリカ初の地域詩アンソロジー。15か国の詩人を集め、汎アメリカ的文学アイデンティティの構築を試みた。",
    background="1840年代アルゼンチン亡命知識人による汎アメリカ文学運動。",
    development="ラテンアメリカ文学概念の制度化の起点。",
    historical_context="独立後ラテンアメリカ国民文学形成期。",
    primary_source_url=BVMC+"obra/america-poetica/",
    primary_source_type="BVMC: América poética",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="オストス『バヨアンの巡礼』",
    name_en="Hostos's La peregrinación de Bayoán",
    name_original="La peregrinación de Bayoán",
    period_key="19世紀補完期",
    definition="エウヘニオ・マリア・デ・オストス（1839-1903）が1863年に発表した思想小説。タイノ族首長バヨアンの架空巡礼を通じてプエルトリコ・キューバの独立とアンティル連合を提唱した。",
    background="1860年代スペイン領アンティル諸島独立運動。",
    development="マルティ、ルベン・ダリオに先立つアンティル独立思想の文学化。",
    historical_context="19世紀後半スペイン領カリブ独立運動。",
    primary_source_url=BVMC+"obra/la-peregrinacion-de-bayoan--0/",
    primary_source_type="BVMC: La peregrinación de Bayoán",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ゴンサレス・プラダ『自由のページ』",
    name_en="González Prada's Páginas libres",
    name_original="Páginas libres",
    period_key="19世紀補完期",
    definition="マヌエル・ゴンサレス・プラダ（1844-1918）が1894年にパリで刊行したエッセイ集。ペルー・アリストクラシーと教会への急進的批判で、20世紀ペルー左翼思想（マリアテギ）の起源。",
    background="ペルー太平洋戦争敗北(1879-83)後の知識人危機。",
    development="マリアテギ、アヤ・デ・ラ・トーレ（APRA党）の理論的源泉。",
    historical_context="19世紀末ペルー寡頭制支配の危機。",
    primary_source_url=BVMC+"obra/paginas-libres--0/",
    primary_source_type="BVMC: Páginas libres",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ホセ・アスンシオン・シルバ『食卓の後で』",
    name_en="José Asunción Silva's De sobremesa",
    name_original="De sobremesa",
    period_key="19世紀補完期",
    definition="コロンビア詩人ホセ・アスンシオン・シルバ（1865-1896）が1896年没後に発見された日記体小説。デカダン主義の知識人ホセ・フェルナンデスの欧州遍歴を描き、ラテンアメリカ世紀末小説の祖型。",
    background="1890年代ボゴタの世紀末文化、シルバの欧州体験と早世。",
    development="モデルニスモ小説の起点としてダリオ、グティエレス・ナヘラと並ぶ。",
    historical_context="19世紀末ラテンアメリカ・モデルニスモ。",
    primary_source_url=BVMC+"obra/de-sobremesa--0/",
    primary_source_type="BVMC: De sobremesa",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# C: 20世紀前半 (10)
# ============================================================
add(**C, name_ja="バスコンセロス『宇宙的人種』",
    name_en="Vasconcelos's La raza cósmica",
    name_original="La raza cósmica",
    period_key="20世紀前半期",
    definition="ホセ・バスコンセロス（1882-1959）が1925年に発表した文化哲学エッセイ。ラテンアメリカ・メスティーソを五大人種混合の「第五の宇宙的人種」として未来的に位置づける。",
    background="メキシコ革命後の文化政策（バスコンセロスは公教育長官）。",
    development="メキシコ国民アイデンティティ言説の中軸として20世紀全体に影響。",
    historical_context="1920年代メキシコ革命後の文化国家建設。",
    primary_source_url=ARCHIVE+"larazacosmica00vasc",
    primary_source_type="archive.org: La raza cósmica (1925)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ペドロ・エンリケス・ウレーニャ『六つのエッセイ』",
    name_en="Henríquez Ureña's Seis ensayos en busca de nuestra expresión",
    name_original="Seis ensayos en busca de nuestra expresión",
    period_key="20世紀前半期",
    definition="ペドロ・エンリケス・ウレーニャ（1884-1946）が1928年に発表したエッセイ集。ラテンアメリカ文学の固有表現を探求し、20世紀ラテンアメリカ批評の基礎を確立した。",
    background="ドミニカ共和国出身のエンリケス・ウレーニャの汎アメリカ批評構想。",
    development="アンヘル・ラマ、ロベルト・フェルナンデス・レタマールら現代ラテンアメリカ批評の祖。",
    historical_context="1920年代ラテンアメリカ文化的自立運動。",
    primary_source_url=BVMC+"obra/seis-ensayos-en-busca-de-nuestra-expresion/",
    primary_source_type="BVMC: Seis ensayos",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="エンリケス・ウレーニャ『現代史的潮流』",
    name_en="Henríquez Ureña's Las corrientes literarias",
    name_original="Las corrientes literarias en la América Hispánica",
    period_key="20世紀前半期",
    definition="エンリケス・ウレーニャが1949年に没後刊行されたハーバード・ノートン講義（1940-41）。植民地から20世紀までのスペイン語アメリカ文学史を初めて体系化した。",
    background="ハーバード大学チャールズ・ノートン詩学講義。",
    development="ラテンアメリカ文学史記述の出発点として現代まで参照される。",
    historical_context="1940年代米国アカデミアでのラテンアメリカ研究興隆。",
    primary_source_url=ARCHIVE+"corrienteslitera0000henr",
    primary_source_type="archive.org: Las corrientes literarias (1949)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="グスマン『カウディーリョの影』",
    name_en="Guzmán's La sombra del caudillo",
    name_original="La sombra del caudillo",
    period_key="20世紀前半期",
    definition="マルティン・ルイス・グスマン（1887-1976）が1929年に発表した政治小説。革命後メキシコのカウディーリョ（軍事指導者）権力闘争を内幕として描き、ラテンアメリカ独裁者文学の祖。",
    background="1920年代メキシコ革命後のオブレゴン・カリェス権力構造。",
    development="アストゥリアス『大統領閣下』、ガルシア・マルケス『族長の秋』の前駆。",
    historical_context="メキシコ革命後の軍事カウディーリョ体制。",
    primary_source_url=BVMC+"obra/la-sombra-del-caudillo/",
    primary_source_type="BVMC: La sombra del caudillo",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マセドニオ・フェルナンデス『永遠の女の小説博物館』",
    name_en="Macedonio Fernández's Museo de la Novela de la Eterna",
    name_original="Museo de la Novela de la Eterna",
    period_key="20世紀前半期",
    definition="マセドニオ・フェルナンデス（1874-1952）が1967年没後刊行した実験小説。56の序文と本編からなり、ボルヘス・コルタサルに先立つアルゼンチン・メタフィクションの起源。",
    background="ブエノスアイレス20世紀前半の哲学的文人サークル、若きボルヘスの師。",
    development="ボルヘス、コルタサル、アイラ、ピグリアら現代アルゼンチン文学の隠れた起源。",
    historical_context="ブエノスアイレス1920-50年代の前衛文学圏。",
    primary_source_url=ARCHIVE+"museodelanovelade0000mace",
    primary_source_type="archive.org: Museo de la Novela (1967)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ロベルト・アルト『七人の狂人』",
    name_en="Roberto Arlt's Los siete locos",
    name_original="Los siete locos",
    period_key="20世紀前半期",
    definition="ロベルト・アルト（1900-1942）が1929年に発表した長編小説。ブエノスアイレス下層知識人レムロ・エルドサインの陰謀と妄想を、卑俗な口語と異常心理で描く。アルゼンチン都市小説の祖。",
    background="1920年代ブエノスアイレスの移民下層・無政府主義圏。",
    development="続編『火炎放射器』(1931)とともに、コルタサル、サバト、ピグリアの起源。",
    historical_context="1920年代末アルゼンチン経済危機。",
    primary_source_url=BVMC+"obra/los-siete-locos--0/",
    primary_source_type="BVMC: Los siete locos",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アルト『ブエノスアイレス水彩画』",
    name_en="Arlt's Aguafuertes porteñas",
    name_original="Aguafuertes porteñas",
    period_key="20世紀前半期",
    definition="アルトが1928-33年に新聞『エル・ムンド』に連載した日刊コラム集。ブエノスアイレス下層民の口語・風景を「水彩画（aguafuerte）」として記録し、現代クロニカ・ジャンルの起源。",
    background="1928年以降のブエノスアイレス都市変容を毎日記録するジャーナリズム。",
    development="ガルシア・マルケス、モンシバイス、アロイラら現代クロニカ作家の祖型。",
    historical_context="1930年代ブエノスアイレスの都市変容。",
    primary_source_url=BVMC+"obra/aguafuertes-portenas/",
    primary_source_type="BVMC: Aguafuertes porteñas",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="キローガ『愛と狂気と死の物語』",
    name_en="Quiroga's Cuentos de amor de locura y de muerte",
    name_original="Cuentos de amor de locura y de muerte",
    period_key="20世紀前半期",
    definition="ウルグアイ作家オラシオ・キローガ（1878-1937）が1917年に発表した短編集。ミシオネス密林の自然と人間の闘争を、ポー・モーパッサン的圧縮で描く。ラテンアメリカ近代短編の規範。",
    background="アルゼンチン・ミシオネス州ジャングルでの開拓体験。",
    development="ボルヘス、コルタサルら20世紀ラテンアメリカ短編全体への祖。",
    historical_context="1910年代ラテンアメリカ熱帯辺境開拓。",
    primary_source_url=BVMC+"obra/cuentos-de-amor-de-locura-y-de-muerte/",
    primary_source_type="BVMC: Cuentos de amor de locura y de muerte",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="リベラ『渦』",
    name_en="José Eustasio Rivera's La vorágine",
    name_original="La vorágine",
    period_key="20世紀前半期",
    definition="ホセ・エウスタシオ・リベラ（1888-1928）が1924年に発表したコロンビア長編。アマゾン熱帯雨林のゴム採取労働の地獄を、詩的散文で描く「ジャングル小説」の規範。",
    background="1920年代コロンビア・アマゾン国境調査委員リベラの実体験。",
    development="ガジェゴス『ドニャ・バルバラ』、グイラルデス『ドン・セグンド・ソンブラ』とともに大地小説三大作。",
    historical_context="20世紀初頭ラテンアメリカ熱帯辺境のゴム・ブーム搾取。",
    primary_source_url=GUTEN+"ebooks/22388",
    primary_source_type="Project Gutenberg: La vorágine",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マリアテギ『ペルー現実解釈の七つのエッセイ』",
    name_en="Mariátegui's Siete ensayos de interpretación de la realidad peruana",
    name_original="Siete ensayos de interpretación de la realidad peruana",
    period_key="20世紀前半期",
    definition="ホセ・カルロス・マリアテギ（1894-1930）が1928年に発表したマルクス主義エッセイ。ペルーの土地・先住民・教育問題を分析し、ラテンアメリカ・マルクス主義の出発点を確立した。",
    background="1920年代ペルー・アマウタ誌、ペルー社会党結成（1928）。",
    development="フランクフルト学派、従属論、サパティスタ運動の理論的祖型。",
    historical_context="1920年代ラテンアメリカ革命左翼思想形成期。",
    primary_source_url=ARCHIVE+"sieteensayosdein0000mari",
    primary_source_type="archive.org: 7 ensayos (1928)",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# D: Vanguardismo (8)
# ============================================================
add(**C, name_ja="ウイドブロ『アルタソル』",
    name_en="Vicente Huidobro's Altazor",
    name_original="Altazor o el viaje en paracaídas",
    period_key="Vanguardismo期",
    definition="ビセンテ・ウイドブロ（1893-1948）が1931年に発表した7歌の長詩。空中落下する詩人アルタソルの墜落を、最終歌で全言語の解体に至る音声詩で描く。ラテンアメリカ前衛詩の頂点。",
    background="1920年代パリ・ダダ・シュルレアリスム圏でのチリ詩人ウイドブロ。",
    development="ラテンアメリカ・コンクリート詩、ニカノル・パラ反詩の祖型。",
    historical_context="1920-30年代パリ前衛芸術圏。",
    primary_source_url=ARCHIVE+"altazoroelviajeen0000huid",
    primary_source_type="archive.org: Altazor (1931)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ウイドブロ『創造主義宣言』",
    name_en="Huidobro's Manifiesto Creacionismo",
    name_original="Non serviam / Manifestes",
    period_key="Vanguardismo期",
    definition="ウイドブロが1914-25年に各地で発表した詩論宣言群（「Non serviam」1914、『マニフェスト集』1925）。詩人を「小さな神」と定義し「創造主義（creacionismo）」を提唱、ラテンアメリカ前衛詩理論を開いた。",
    background="ウイドブロのチリ・パリ・マドリード前衛圏渡航。",
    development="ボルヘス・ウルトライスモ、デ・ロハ、ヒロンドら同時代前衛運動の理論的源。",
    historical_context="第一次大戦前後のヨーロッパ・ラテンアメリカ前衛運動。",
    primary_source_url=BVMC+"obra/manifiestos/",
    primary_source_type="BVMC: Manifiestos",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヒロンド『路面電車詩集』",
    name_en="Oliverio Girondo's Veinte poemas para ser leídos en el tranvía",
    name_original="Veinte poemas para ser leídos en el tranvía",
    period_key="Vanguardismo期",
    definition="オリベリオ・ヒロンド（1891-1967）が1922年に発表した詩集。ブエノスアイレス都市風景を都市的フラヌール視点で描き、アルゼンチン前衛詩の出発点となった。",
    background="1920年代ブエノスアイレスのマルティン・フィエロ誌前衛圏。",
    development="ボルヘス・ウルトライスモと並走するアルゼンチン前衛詩の規範。",
    historical_context="1920年代ブエノスアイレス都市文化最盛期。",
    primary_source_url=BVMC+"obra/veinte-poemas-para-ser-leidos-en-el-tranvia/",
    primary_source_type="BVMC: Veinte poemas",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヒロンド『骨髄の中で』",
    name_en="Girondo's En la masmédula",
    name_original="En la masmédula",
    period_key="Vanguardismo期",
    definition="ヒロンドが1954年に発表した晩年詩集。新造語・音声実験で言語の物質性を極限化し、コンクリート詩・パラ反詩の前駆となった。",
    background="アルゼンチン前衛詩の戦後継続、ヒロンドとノラー・ラング夫妻のサロン。",
    development="ニカノル・パラ反詩、レオニダス・ラムボーグニーニ詩学の祖。",
    historical_context="1950年代アルゼンチン詩の言語物質化。",
    primary_source_url=BVMC+"obra/en-la-masmedula/",
    primary_source_type="BVMC: En la masmédula",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="マリオ・デ・アンドラーデ『パウリセイア・デスヴァイラーダ』",
    name_en="Mário de Andrade's Pauliceia desvairada",
    name_original="Pauliceia desvairada",
    period_key="Vanguardismo期",
    definition="マリオ・デ・アンドラーデ（1893-1945）が1922年に発表した詩集。サンパウロ近代化の都市的妄想（pauliceia）を自由韻律で歌い、ブラジル・モデルニズモの宣言的詩集となった。",
    background="1922年サンパウロ近代芸術週間（Semana de 22）の中核。",
    development="ブラジル・モデルニズモ全体の出発点として現代まで参照。",
    historical_context="1920年代サンパウロ工業都市化。",
    primary_source_url=BNDIG+"acervodigital",
    primary_source_type="BNDigital: Pauliceia desvairada",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="オズワルド・デ・アンドラーデ『食人宣言』",
    name_en="Oswald de Andrade's Manifesto antropófago",
    name_original="Manifesto antropófago",
    period_key="Vanguardismo期",
    definition="オズワルド・デ・アンドラーデ（1890-1954）が1928年に『アントロポファジア誌』に発表した詩的宣言。「Tupi or not tupi」のフレーズで欧州文化の選択的食人を提唱、ブラジル文化批評の中軸概念。",
    background="1920年代ブラジル・モデルニズモの第二段階としての人類学的文化論。",
    development="ヴィヴェイロス・デ・カストロ・パースペクティヴィズム人類学の文学的祖。",
    historical_context="1920年代後半ブラジル国民アイデンティティ論争。",
    primary_source_url=ARCHIVE+"manifestoantropofago",
    primary_source_type="archive.org: Manifesto antropófago",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="オズワルド・デ・アンドラーデ『ブラジル木の詩』",
    name_en="Oswald de Andrade's Pau-Brasil",
    name_original="Pau-Brasil",
    period_key="Vanguardismo期",
    definition="オズワルド・デ・アンドラーデが1925年に発表した詩集。植民地報告書テクストを引用・再構成し、ブラジル一次産品（パウブラジル材）的詩学を提唱した。",
    background="1924年パリでセンドラルらと交流、植民地史料への関心。",
    development="ブラジル・モデルニズモ第一段階の理論的・実践的代表作。",
    historical_context="1920年代ブラジル文化国民化運動。",
    primary_source_url=ARCHIVE+"paubrasil0000andr",
    primary_source_type="archive.org: Pau-Brasil (1925)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョルジ・デ・リマ『オルフェウスの発明』",
    name_en="Jorge de Lima's Invenção de Orfeu",
    name_original="Invenção de Orfeu",
    period_key="Vanguardismo期",
    definition="ジョルジ・デ・リマ（1893-1953）が1952年に発表した10歌・5000行の叙事詩。カモンイス『ウズ・ルジアダス』を範に、ブラジルの神話的・カトリック的・アフロ系起源を統合する。",
    background="北東部アラゴアス州のカトリック・アフロ系融合文化。",
    development="ブラジル現代叙事詩の頂点として参照される。",
    historical_context="20世紀中葉ブラジル神話的国民詩。",
    primary_source_url=ARCHIVE+"invencaodeorfeu0000lima",
    primary_source_type="archive.org: Invenção de Orfeu",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# E: Boom補完 (8)
# ============================================================
add(**C, name_ja="ドノソ『田舎の家』",
    name_en="José Donoso's Casa de campo",
    name_original="Casa de campo",
    period_key="Boom補完期",
    definition="ホセ・ドノソ（1924-1996）が1978年に発表した長編。架空のベンタラ家の田舎屋敷で起きる子供たちの叛乱を、ピノチェト軍政のアレゴリーとして描く。ポスト・ブーム小説の代表作。",
    background="1973年チリ・ピノチェト・クーデター後の亡命中執筆。",
    development="バルガス・リョサ『山羊の祝祭』ら独裁者寓話小説に直接影響。",
    historical_context="1970年代南米軍政期。",
    primary_source_url=BVMC+"obra/casa-de-campo/",
    primary_source_type="BVMC: Casa de campo",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バルガス・リョサ『緑の家』",
    name_en="Vargas Llosa's La casa verde",
    name_original="La casa verde",
    period_key="Boom補完期",
    definition="マリオ・バルガス・リョサ（1936-）が1966年に発表した長編。ペルー・ピウラの売春宿「緑の家」と密林ノヴァト要塞を、5本の物語線を時空交錯で編む。Rómulo Gallegos賞受賞、ブーム期構造的実験の頂点。",
    background="1950年代バルガス・リョサのアマゾン調査体験。",
    development="ガルシア・マルケス『族長の秋』の構造的祖型。",
    historical_context="1960年代ラテンアメリカ・ブーム期。",
    primary_source_url=BVMC+"obra/la-casa-verde--0/",
    primary_source_type="BVMC: La casa verde",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バルガス・リョサ『パンタレオン大尉と女たち』",
    name_en="Vargas Llosa's Pantaleón y las visitadoras",
    name_original="Pantaleón y las visitadoras",
    period_key="Boom補完期",
    definition="バルガス・リョサが1973年に発表した諷刺長編。アマゾン駐屯軍のための公娼サービス組織化を、軍報告書・新聞記事の混淆で描き、軍隊官僚のグロテスクをユーモラスに描く。",
    background="1970年代ペルー軍事政権下の風刺小説。",
    development="ラテンアメリカ・諷刺軍事小説の規範。",
    historical_context="1970年代ペルー・ベラスコ軍政期。",
    primary_source_url=BVMC+"obra/pantaleon-y-las-visitadoras--0/",
    primary_source_type="BVMC: Pantaleón y las visitadoras",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バルガス・リョサ『世界終末戦争』",
    name_en="Vargas Llosa's La guerra del fin del mundo",
    name_original="La guerra del fin del mundo",
    period_key="Boom補完期",
    definition="バルガス・リョサが1981年に発表した700頁長編。1896-97年ブラジル・カヌードス農民千年王国反乱を、エウクリーデス・ダ・クーニャ『奥地』を典拠に再構築する。",
    background="ブラジル北東部カヌードス史実とユークリデス・ダ・クーニャ『奥地』の継承。",
    development="ガルシア・マルケス『族長の秋』、ボラーニョ『2666』へのスケール的影響。",
    historical_context="ブラジル第一共和制初期の千年王国反乱。",
    primary_source_url=BVMC+"obra/la-guerra-del-fin-del-mundo--0/",
    primary_source_type="BVMC: La guerra del fin del mundo",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ガルシア・マルケス『コレラの時代の愛』",
    name_en="García Márquez's El amor en los tiempos del cólera",
    name_original="El amor en los tiempos del cólera",
    period_key="Boom補完期",
    definition="ガルシア・マルケス（1927-2014）が1985年に発表した長編。フェルミナとフロレンティーノの50年越しの愛を、コロンビア・カリブ世紀末から現代までの社会変容を背景に描く。",
    background="ノーベル賞受賞(1982)後の代表作、両親の恋愛史を典拠。",
    development="ポスト・ブーム期魔術リアリズムの円熟。",
    historical_context="20世紀コロンビア・カリブ社会変容。",
    primary_source_url=BVMC+"obra/el-amor-en-los-tiempos-del-colera--0/",
    primary_source_type="BVMC: El amor en los tiempos del cólera",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ガルシア・マルケス『迷宮の将軍』",
    name_en="García Márquez's El general en su laberinto",
    name_original="El general en su laberinto",
    period_key="Boom補完期",
    definition="ガルシア・マルケスが1989年に発表した歴史小説。シモン・ボリーバル最後の航海（1830年マグダレナ川下り）を、独立後幻滅と病死の14日として描き、独立神話を脱神話化する。",
    background="ボリーバル没後160周年の記念執筆。",
    development="ポスト・ブーム歴史小説の規範、ボリーバル像脱神話化。",
    historical_context="ラテンアメリカ独立後の英雄神話批判。",
    primary_source_url=BVMC+"obra/el-general-en-su-laberinto--0/",
    primary_source_type="BVMC: El general en su laberinto",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="コルタサル『62 / 模型キット』",
    name_en="Cortázar's 62 / Modelo para armar",
    name_original="62 / Modelo para armar",
    period_key="Boom補完期",
    definition="フリオ・コルタサル（1914-1984）が1968年に発表した長編。『石蹴り遊び』第62章のプログラムを実装する形式で、パリ・ロンドン・ウィーンを移動する人物群の関係を組み立てる。",
    background="『石蹴り遊び』(1963)の理論的続編。",
    development="ヌーヴォーロマン・実験小説のラテンアメリカ的展開。",
    historical_context="1960年代後半パリ亡命知識人圏。",
    primary_source_url=BVMC+"obra/62-modelo-para-armar/",
    primary_source_type="BVMC: 62 / Modelo para armar",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="オネッティ『造船所』",
    name_en="Onetti's El astillero",
    name_original="El astillero",
    period_key="Boom補完期",
    definition="ホアン・カルロス・オネッティ（1909-1994）が1961年に発表した長編。架空の街サンタ・マリアの廃れた造船所支配人ラルセンの幻想的支配劇を描く。ラテンアメリカ・モダニズム頂点。",
    background="1950年代モンテビデオの倦怠と、フォークナー的架空都市の継承。",
    development="ボラーニョ『チリの夜』、サエル『リオの孤児』に直接影響。",
    historical_context="1960年代ウルグアイ社会停滞期。",
    primary_source_url=BVMC+"obra/el-astillero/",
    primary_source_type="BVMC: El astillero",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# F: Brazilian深掘り (8)
# ============================================================
add(**C, name_ja="マシャード・デ・アシス『記念のアイレス』",
    name_en="Machado de Assis's Memorial de Aires",
    name_original="Memorial de Aires",
    period_key="ブラジル深掘り期",
    definition="マシャード・デ・アシス（1839-1908）が1908年に発表した遺作。引退外交官アイレスの日記体で、リオの寡婦フィデリアと若者トリスタンの関係を観察する。マシャード晩年の静謐な傑作。",
    background="マシャード晩年、奴隷解放(1888)・帝政崩壊(1889)後のリオ。",
    development="マシャード五大長編の最終作として現代まで参照。",
    historical_context="第一共和制初期リオデジャネイロ。",
    primary_source_url=GUTEN+"ebooks/55727",
    primary_source_type="Project Gutenberg: Memorial de Aires",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="リマ・バレット『書記イザイアスの回想』",
    name_en="Lima Barreto's Recordações do escrivão Isaías Caminha",
    name_original="Recordações do escrivão Isaías Caminha",
    period_key="ブラジル深掘り期",
    definition="リマ・バレット（1881-1922）が1909年に発表した自伝的長編。混血知識人イザイアスのリオでの社会的挫折を描き、ブラジル最初の本格的人種問題小説。",
    background="第一共和制リオの人種・階級差別、リマ・バレット自身の混血知識人体験。",
    development="マシャード後のブラジル現実主義小説の中軸として再評価。",
    historical_context="20世紀初頭リオの人種・階級差別。",
    primary_source_url=ARCHIVE+"recordacoesdoescrivao0000lima",
    primary_source_type="archive.org: Recordações (1909)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="グラシリアーノ・ラモス『不毛の人生』",
    name_en="Graciliano Ramos's Vidas secas",
    name_original="Vidas secas",
    period_key="ブラジル深掘り期",
    definition="グラシリアーノ・ラモス（1892-1953）が1938年に発表した北東部小説。干魃に追われる小作人ファビアーノ家族と犬バレイアの放浪を、極度に削ぎ落とした散文で描く。ブラジル北東部小説の頂点。",
    background="1930年代ブラジル北東部干魃地帯（sertão）の社会調査小説潮流。",
    development="ジョルジ・アマード、ロサ、ヴィエイラ・ジュニオールら北東部文学の規範。",
    historical_context="1930年代ブラジル北東部経済危機。",
    primary_source_url=ARCHIVE+"vidassecas0000ramo",
    primary_source_type="archive.org: Vidas secas (1938)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジョルジ・アマード『砂浜の船長たち』",
    name_en="Jorge Amado's Capitães da Areia",
    name_original="Capitães da Areia",
    period_key="ブラジル深掘り期",
    definition="ジョルジ・アマード（1912-2001）が1937年に発表した長編。サルバドール港の浮浪児集団「砂浜の船長たち」の生を、共産主義者作家の社会的視点で描く。",
    background="1930年代エスタード・ノヴォ独裁期、アマードの共産党活動期。",
    development="20世紀ブラジル児童労働・浮浪児文学の起源。",
    historical_context="1930年代バイーア州都市貧困。",
    primary_source_url=ARCHIVE+"capitaesdaareia0000amad",
    primary_source_type="archive.org: Capitães da Areia (1937)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョルジ・アマード『ガブリエラ、丁子と肉桂』",
    name_en="Amado's Gabriela, cravo e canela",
    name_original="Gabriela, cravo e canela",
    period_key="ブラジル深掘り期",
    definition="アマードが1958年に発表した代表作。バイーア・イレウスのカカオ町で、混血娘ガブリエラとアラブ系移民バーオーナー・ナシブの恋愛を中心に町の近代化を描く。",
    background="1920年代バイーア・イレウスのカカオ・ブーム。",
    development="アマード後期民俗・恋愛小説の規範、世界的ベストセラー。",
    historical_context="20世紀前半バイーア州カカオ経済。",
    primary_source_url=BRITT+"topic/Gabriela-Cravo-e-Canela",
    primary_source_type="Britannica: Gabriela",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エリコ・ヴェリッシモ『時と風』三部作",
    name_en="Érico Veríssimo's O Tempo e o Vento trilogy",
    name_original="O Tempo e o Vento (I-III)",
    period_key="ブラジル深掘り期",
    definition="エリコ・ヴェリッシモ（1905-1975）が1949-61年に発表した三部作（『大陸』『肖像』『群島』）。リオ・グランデ・ド・スル州の200年史をテルヘ家系を通じて描く。ブラジル南部国民叙事詩。",
    background="1940-60年代ブラジル南部地域史小説潮流。",
    development="ブラジル地域大河小説の代表作。",
    historical_context="リオ・グランデ・ド・スル州200年史。",
    primary_source_url=ARCHIVE+"otempoevento0000veri",
    primary_source_type="archive.org: O Tempo e o Vento",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="リジア・ファグンデス・テレス『少女たち』",
    name_en="Lygia Fagundes Telles's As Meninas",
    name_original="As Meninas",
    period_key="ブラジル深掘り期",
    definition="リジア・ファグンデス・テレス（1923-2022）が1973年に発表した長編。サンパウロの女子寄宿舎の三人の女学生の意識を、軍政期の政治的不安を背景に内的独白で描く。",
    background="1970年代ブラジル軍政期サンパウロ女子学生文化。",
    development="ブラジル女性文学・軍政期内的独白小説の規範、ジャブティ賞受賞。",
    historical_context="1970年代ブラジル軍政期。",
    primary_source_url=BRITT+"biography/Lygia-Fagundes-Telles",
    primary_source_type="Britannica: Telles",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヒルダ・イルスト『卑猥な貴婦人D』",
    name_en="Hilda Hilst's A Obscena Senhora D",
    name_original="A Obscena Senhora D",
    period_key="ブラジル深掘り期",
    definition="ヒルダ・イルスト（1930-2004）が1982年に発表した中編。60歳の女性ヒラエの形而上学的・性的独白を高密度で展開し、ブラジル実験文学・女性身体エロス書記の頂点。",
    background="1980年代ブラジル女性実験文学。",
    development="リスペクトル後継として21世紀イルスト再評価。",
    historical_context="1980年代ブラジル軍政後期。",
    primary_source_url=BRITT+"biography/Hilda-Hilst",
    primary_source_type="Britannica: Hilda Hilst",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# G: Postdictadura (6)
# ============================================================
add(**C, name_ja="ボラーニョ『遠い星』",
    name_en="Bolaño's Estrella distante",
    name_original="Estrella distante",
    period_key="ポスト独裁期",
    definition="ロベルト・ボラーニョ（1953-2003）が1996年に発表した中編。ピノチェト軍政の詩人・空軍パイロット・連続殺人鬼カルロス・ビーデルを追跡する語り手の物語。軍政の文化的暴力を描く。",
    background="1973年チリ・ピノチェト・クーデターのトラウマ、ボラーニョの収監体験。",
    development="ボラーニョ『チリの夜』『2666』への直接の前駆。",
    historical_context="1970-90年代チリ・ピノチェト軍政。",
    primary_source_url=BRITT+"biography/Roberto-Bolano",
    primary_source_type="Britannica: Bolaño",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ボラーニョ『チリの夜』",
    name_en="Bolaño's Nocturno de Chile",
    name_original="Nocturno de Chile",
    period_key="ポスト独裁期",
    definition="ボラーニョが2000年に発表した中編。死の床のオプスデイ司祭セバスティアン・ウルティアの一夜の独白で、ピノチェト軍政期チリ知識人の共犯を告発する。一段落構成の修辞的傑作。",
    background="ピノチェト時代チリ・カトリック保守知識人圏の批判。",
    development="ラテンアメリカ・ポスト独裁文学の代表作。",
    historical_context="1990年代末チリ・ポスト軍政期記憶論争。",
    primary_source_url=BRITT+"topic/By-Night-in-Chile",
    primary_source_type="Britannica: Nocturno de Chile",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ディアメラ・エルティト『ルンペリカ』",
    name_en="Diamela Eltit's Lumpérica",
    name_original="Lumpérica",
    period_key="ポスト独裁期",
    definition="ディアメラ・エルティト（1949-）が1983年に発表した実験的処女作。サンティアゴ広場の浮浪女L.イルマンディの夜を、断片的散文・写真で構成し、ピノチェト軍政下の身体抵抗を描く。",
    background="1980年代ピノチェト軍政下チリ・前衛芸術集団CADA。",
    development="チリ・ポスト軍政女性実験文学・脱植民地批評の祖。",
    historical_context="1980年代チリ軍政期文化的抵抗。",
    primary_source_url=BRITT+"biography/Diamela-Eltit",
    primary_source_type="Britannica: Eltit",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アレハンドロ・サンブラ『盆栽』",
    name_en="Alejandro Zambra's Bonsái",
    name_original="Bonsái",
    period_key="ポスト独裁期",
    definition="アレハンドロ・サンブラ（1975-）が2006年に発表した極小長編（94頁）。サンティアゴの大学生フリオとエミリアの恋と読書の生を、自己反省的な細密散文で描く。ポスト独裁世代代表作。",
    background="2000年代後半ポスト軍政チリ若手作家ミニマリズム。",
    development="ラテンアメリカ「新ナラティブ」極小小説の規範。",
    historical_context="2000年代ポスト軍政チリ世代。",
    primary_source_url=BRITT+"biography/Alejandro-Zambra",
    primary_source_type="Britannica: Zambra",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="リナ・メルアネ『眼の中の血』",
    name_en="Lina Meruane's Sangre en el ojo",
    name_original="Sangre en el ojo",
    period_key="ポスト独裁期",
    definition="リナ・メルアネ（1970-）が2012年に発表した自伝的長編。チリ系作家リナのニューヨークで網膜出血で失明する身体的危機を、医療と移住の二重体験として記述する。",
    background="メルアネのニューヨーク移住生活と糖尿病合併症体験。",
    development="ラテンアメリカ女性身体・移住文学の規範。",
    historical_context="2010年代ラテンアメリカ女性ディアスポラ文学。",
    primary_source_url=BRITT+"biography/Lina-Meruane",
    primary_source_type="Britannica: Meruane",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="スカルメタ『ネルーダの郵便配達人』",
    name_en="Skármeta's El cartero de Neruda",
    name_original="El cartero de Neruda (Ardiente paciencia)",
    period_key="ポスト独裁期",
    definition="アントニオ・スカルメタ（1940-）が1985年に発表した中編。1969-73年イスラ・ネグラのネルーダの郵便配達人マリオの詩的成長を、ピノチェト・クーデター悲劇まで描く。1994年映画『イル・ポスティーノ』原作。",
    background="アジェンデ期チリのネルーダ晩年とクーデターの記憶。",
    development="ラテンアメリカ・大衆文学とポリティカル・メモリーの架橋。",
    historical_context="1969-73年アジェンデ期チリ。",
    primary_source_url=BRITT+"biography/Antonio-Skarmeta",
    primary_source_type="Britannica: Skármeta",
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


_attach_axes("サアグン『新スペイン全史』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"ナワトル語と西語の並列対訳は、多言語LLMにおける文化的並置と保存問題の前駆。",
     "related_ai_phenomenon":"AI多言語並列処理における少数言語保存"}])
_attach_axes("ラス・カサス『インディアスの破壊についての簡潔な報告』詳解", [
    {"axis":"主体","status":"rethinking",
     "rationale":"先住民を理性的主体とする論証は、AI主体性論争・人間性の境界問題の倫理的祖型。",
     "related_ai_phenomenon":"AI時代の主体性・人格定義の倫理問題"}])
_attach_axes("グアマン・ポマ『新しい記録と良き統治』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"先住民エリートが征服者言語で征服を批判する書記は、AI時代の被支配的主体の表象問題と理論的並行。",
     "related_ai_phenomenon":"AI環境における周辺的主体の表象"}])
_attach_axes("インカ・ガルシラソ『フロリダ誌』", [
    {"axis":"翻訳","status":"rethinking",
     "rationale":"メスティーソ二重視点の歴史記述は、AI時代の文化間翻訳・ハイブリッド主体の祖型。",
     "related_ai_phenomenon":"AI時代の文化間翻訳とハイブリッド主体"}])
_attach_axes("バスコンセロス『宇宙的人種』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"五人種混合の「宇宙的人種」言説は、AI時代のハイブリッド・アイデンティティ論の20世紀的祖型。",
     "related_ai_phenomenon":"AI時代のハイブリッド・アイデンティティ"}])
_attach_axes("マセドニオ・フェルナンデス『永遠の女の小説博物館』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"56序文・本編の自己反省構造は、AI生成における自己言及・メタ・テキストの祖型。",
     "related_ai_phenomenon":"AI生成における自己言及メタテキスト"}])
_attach_axes("ロベルト・アルト『七人の狂人』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"ブエノスアイレス下層口語ルンファルドの文学化は、LLMにおける非標準口語表象問題の祖型。",
     "related_ai_phenomenon":"LLMにおける非標準口語の表象"}])
_attach_axes("アルト『ブエノスアイレス水彩画』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"日刊新聞コラムの即時性は、AI時代のリアルタイム生成コンテンツの祖型。",
     "related_ai_phenomenon":"AI生成によるリアルタイム都市記録"}])
_attach_axes("マリアテギ『ペルー現実解釈の七つのエッセイ』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"先住民共同体的社会主義の構想は、AI時代の集合的所有・分散主体論と理論的並行。",
     "related_ai_phenomenon":"AI時代の集合的所有・分散主体"}])
_attach_axes("ウイドブロ『アルタソル』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"音声詩で全言語を解体する第七歌は、AI生成における言語規範解体・創発的言語の祖型。",
     "related_ai_phenomenon":"AI生成における言語規範解体と創発"}])
_attach_axes("ウイドブロ『創造主義宣言』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"詩人を「小さな神」「創造主」と定義する詩学は、AI生成における創造主体性問題の20世紀的祖型。",
     "related_ai_phenomenon":"AI生成と創造主体性の哲学的問い直し"}])
_attach_axes("オズワルド・デ・アンドラーデ『食人宣言』", [
    {"axis":"翻訳","status":"rethinking",
     "rationale":"欧州文化の選択的食人による文化的混淆論は、AI時代のデータ・スクレイピングと文化的所有問題の理論的祖型。",
     "related_ai_phenomenon":"AIデータ・スクレイピングと文化的所有"}])
_attach_axes("マリオ・デ・アンドラーデ『パウリセイア・デスヴァイラーダ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"標準ポルトガル語に対する都市口語の組織的混入は、LLMにおける都市方言表象問題と並行。",
     "related_ai_phenomenon":"LLMにおける都市方言表象"}])
_attach_axes("バルガス・リョサ『緑の家』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"5本の物語線の時空交錯構造は、AI生成マルチストランド・ナラティブの構造的祖型。",
     "related_ai_phenomenon":"AI生成マルチストランド・ナラティブ"}])
_attach_axes("バルガス・リョサ『世界終末戦争』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"ダ・クーニャ『奥地』を典拠とする百科全書的小説は、AI時代の典拠統合・大規模再構築の祖型。",
     "related_ai_phenomenon":"AI時代の大規模典拠統合と再構築"}])
_attach_axes("コルタサル『62 / 模型キット』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"プログラム的指示にもとづく組立小説は、AIインタラクティブ・組立小説の理論的祖型。",
     "related_ai_phenomenon":"AI駆動インタラクティブ組立小説"}])
_attach_axes("オネッティ『造船所』", [
    {"axis":"真正性","status":"rethinking",
     "rationale":"架空都市サンタ・マリアでの幻想的支配劇は、AI生成における架空空間・架空現実の祖型。",
     "related_ai_phenomenon":"AI生成における架空空間と架空現実"}])
_attach_axes("グラシリアーノ・ラモス『不毛の人生』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"極度に削ぎ落とした北東部口語散文は、LLMにおける極小言語・周辺方言の表象問題と並行。",
     "related_ai_phenomenon":"LLMにおける極小言語・周辺方言の表象"}])
_attach_axes("ヒルダ・イルスト『卑猥な貴婦人D』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"60歳女性身体の形而上学的独白は、AI時代の老齢・女性身体表象問題の文学的祖型。",
     "related_ai_phenomenon":"AI時代の老齢身体・女性身体の表象"}])
_attach_axes("ボラーニョ『遠い星』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"連続殺人鬼が詩人でもある二重作者性は、AI生成における作者性・倫理性の分離問題と理論的並行。",
     "related_ai_phenomenon":"AI生成における作者性と倫理性の分離"}])
_attach_axes("ボラーニョ『チリの夜』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"一段落構成の修辞的独白は、AI生成における長文連続生成・段落構造解体の祖型。",
     "related_ai_phenomenon":"AI生成における長文連続生成"}])
_attach_axes("ディアメラ・エルティト『ルンペリカ』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"浮浪女L.イルマンディの身体抵抗は、AI監視社会における身体の周辺性・抵抗の祖型。",
     "related_ai_phenomenon":"AI監視社会における身体の周辺性"}])
_attach_axes("アレハンドロ・サンブラ『盆栽』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"自己反省的な細密散文・極小小説は、AI時代の極小・自己言及テキスト形式の文学的探究。",
     "related_ai_phenomenon":"AI時代の極小・自己言及形式"}])
_attach_axes("リナ・メルアネ『眼の中の血』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"失明する身体・移住者の二重周辺性は、AIアクセシビリティ・身体多様性論の文学的祖型。",
     "related_ai_phenomenon":"AIアクセシビリティと身体多様性"}])


# ============================================================
# cross_domain links (>=12 to PT/PHIL/AN)
# ============================================================
def _attach_cross(concept_name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


_attach_cross("サアグン『新スペイン全史』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"民族誌・ナワ族人類学",
     "description":"フィレンツェ写本は近代民族誌の祖型として、ボアズ・マリノフスキー以前の人類学的記述方法の起源と接続。"}])
_attach_cross("ラス・カサス『インディアスの破壊についての簡潔な報告』詳解", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"近代人権思想・自然法",
     "description":"ビトリア、スアレスのサラマンカ学派自然法論と接続し、近代人権思想の出発点。"}])
_attach_cross("グアマン・ポマ『新しい記録と良き統治』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"アンデス先住民人類学",
     "description":"アンデス・トコイカマヨック制度・キープ記憶術の記録は、ホセ・カルロス・マリアテギ、トム・サモラ、ジョン・ムラ人類学の典拠。"}])
_attach_cross("インカ・ガルシラソ『フロリダ誌』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"メスティーソ・ハイブリッド人類学",
     "description":"メスティーソ二重視点の歴史記述はガルシア・カンクリーニ、ホミ・バーバのハイブリディティ論の祖型。"}])
_attach_cross("バスコンセロス『宇宙的人種』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"人種混合・進化的存在論",
     "description":"五人種混合の進化哲学はピエール・テイヤール・ド・シャルダンら20世紀進化哲学と並走。"}])
_attach_cross("マリアテギ『ペルー現実解釈の七つのエッセイ』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"ラテンアメリカ・マルクス主義",
     "description":"先住民共同体的社会主義の構想はグラムシ、フランクフルト学派、従属論派の理論的祖。"}])
_attach_cross("ウイドブロ『アルタソル』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"音声詩・コンクリート詩学",
     "description":"第七歌の音声詩は20世紀コンクリート詩・サウンド・ポエトリー研究の中心テクスト。"}])
_attach_cross("オズワルド・デ・アンドラーデ『食人宣言』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"ヴィヴェイロス・デ・カストロ・パースペクティヴィズム",
     "description":"ブラジル先住民食人観の人類学的継承として、ヴィヴェイロス・デ・カストロ多自然主義の文学的源。"}])
_attach_cross("ジョルジ・アマード『ガブリエラ、丁子と肉桂』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"バイーア・アフロ系シンクレティズム",
     "description":"カンドンブレ宗教文化の文学化はヴェルジェ、ピエール・サンソンら宗教人類学と並走。"}])
_attach_cross("バルガス・リョサ『世界終末戦争』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"歴史小説論・典拠批評",
     "description":"ダ・クーニャ『奥地』を典拠とする再構築は、リンダ・ハッチオン歴史メタフィクション論の典型例。"}])
_attach_cross("グアマン・ポマ『新しい記録と良き統治』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"絵画・テクスト混合書記",
     "description":"398図版とテクストの混合書記はW・J・T・ミッチェル画像理論・絵画記号学の前駆。"}])
_attach_cross("ボラーニョ『遠い星』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"独裁・暴力人類学",
     "description":"ピノチェト軍政の文化的暴力描写はネリー・リチャード、エリザベス・ジェリン記憶人類学と並走。"}])
_attach_cross("ディアメラ・エルティト『ルンペリカ』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"フェミニスト身体論・抵抗哲学",
     "description":"浮浪女の身体抵抗はジュディス・バトラー身体論、ネリー・リチャード批評と並走。"}])
_attach_cross("ヒルダ・イルスト『卑猥な貴婦人D』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"女性身体・形而上学",
     "description":"60歳女性の形而上学的独白はリュス・イリガライ、エレーヌ・シクスー女性身体哲学と並走。"}])


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
        print(f"[c26-w19] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c26-w19] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c26-w19] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
        print(f"[c26-w19] concepts entered: {len(CONCEPTS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
