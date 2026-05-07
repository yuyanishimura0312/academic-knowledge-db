"""LIT-DB Phase 2 Wave 22 — C28: Russian / Slavic Literature (+80).

Subfield: lit_russia_slavic (id=18). Existing 142, target 400.
Sources: Project Gutenberg, Wikisource (ru/cs/pl/sr/hu), Russian Virtual Library,
ilibrary.ru, Internet Archive. Aim >= 70% primary tier.
fourth_transform_tags >= 24; cross_domain to PT/PHIL >= 18.

Coverage groups (all NEW, non-overlapping):
  A: 19c expansion — Karamzin History/Krylov/Pushkin minor works/Lermontov Demon (10)
  B: Gogol/Tyutchev/Fet/Maykov/Polonsky (10)
  C: Late 19c novelists — Saltykov/Leskov/Korolenko/Garshin/Uspensky/Turgenev (10)
  D: Silver Age — Sologub/Bely/Briusov/Annensky/Ivanov/Merezhkovsky/Kuzmin (10)
  E: Acmeism deep — Akhmatova/Mandelstam/Gumilev volumes (8)
  F: Futurism deep — Mayakovsky/Khlebnikov/Kruchenykh/Severyanin (8)
  G: Soviet — Babel/Pilnyak/Furmanov/Sholokhov/Kataev/Fadeev/Erenburg/Zabolotsky (10)
  H: Dissident & contemporary — Shalamov/Dombrovski/Marchenko/Sinyavsky/Andreev/Bitov/Pelevin/Sorokin/Makanin/Ulitskaya (8)
  I: Slavic — Hašek/Hrabal/Kundera/Havel/Čapek/Słowacki/Sienkiewicz/Reymont/Gombrowicz/Miłosz/Szymborska/Tokarczuk (10)
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("18世紀末ロシア・センチメンタリズム期", "Russian Sentimentalism (late 18c)", 1780, 1820,
     "カラムジン・ジュコフスキー期。"),
    ("19世紀ロシア・ロマンチズム黎明期", "Russian Pre-Romantic", 1810, 1840,
     "デカブリスト世代から黄金時代への移行期。"),
    ("19世紀ロシア黄金時代", "Russian Golden Age 19c", 1820, 1860,
     "プーシキン・ゴーゴリ・レールモントフ・チュッチェフ・フェート期。"),
    ("19世紀後期ロシア・リアリズム成熟期", "Late Russian Realism (mid-late 19c)", 1860, 1910,
     "ドストエフスキー・トルストイ後期、サルトィコフ、レスコフ、コロレンコ等。"),
    ("ロシア銀の時代", "Russian Silver Age", 1890, 1925,
     "象徴主義・アクメイズム・未来派が交錯したロシア・モダニズム黄金期。"),
    ("ソヴィエト中期", "Soviet Mid Period", 1925, 1965,
     "社会主義リアリズム成立期から雪解け期。"),
    ("ソヴィエト後期・ペレストロイカ期", "Late Soviet & Perestroika", 1965, 1991,
     "停滞期から崩壊期にかけての反体制・地下文学期。"),
    ("ポスト・ソヴィエト期", "Post-Soviet", 1991, 2025,
     "ソ連崩壊以後のロシア・ポストモダン期。"),
    ("チェコ近現代文学期", "Czech Modern Literature", 1880, 2025,
     "ハシェク以降のチェコ語近現代文学。"),
    ("ポーランド・ロマン主義および近現代期", "Polish Romanticism & Modern", 1820, 2025,
     "ミツキェヴィチ以降のポーランド近現代文学。"),
]


GUTEN = "https://www.gutenberg.org/"
WIKI_RU = "https://ru.wikipedia.org/wiki/"
WIKI_CS = "https://cs.wikipedia.org/wiki/"
WIKI_PL = "https://pl.wikipedia.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WSRC_RU = "https://ru.wikisource.org/wiki/"
WSRC_CS = "https://cs.wikisource.org/wiki/"
WSRC_PL = "https://pl.wikisource.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
IARCH = "https://archive.org/"
LIB_RU = "https://ilibrary.ru/"
RVB = "https://rvb.ru/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


RUS = dict(subfield_code="lit_russia_slavic", region="東欧・ロシア", original_script="cyrillic")
CZE = dict(subfield_code="lit_russia_slavic", region="東欧・ロシア", original_script="roman")
POL = dict(subfield_code="lit_russia_slavic", region="東欧・ロシア", original_script="roman")


# ============================================================
# A: 19c Russian expansion (10)
# ============================================================
add(**RUS, name_ja="カラムジン『ロシア国家史』",
    name_en="Karamzin's History of the Russian State",
    name_original="История государства Российского",
    period_key="18世紀末ロシア・センチメンタリズム期",
    definition="カラムジンが1816-26年に刊行した全12巻のロシア通史。古代ルーシから17世紀初頭までを感傷主義的散文で叙述し、19世紀ロシア歴史小説（プーシキン・トルストイ）の素材庫となった。",
    background="アレクサンドル一世期ロシアの民族史意識台頭。",
    development="プーシキン『ボリス・ゴドゥノフ』、トルストイ『戦争と平和』に直接影響。",
    historical_context="ナポレオン戦争後のロシア・ナショナリズム成熟期。",
    primary_source_url=WSRC_RU+"История_государства_Российского_(Карамзин)",
    primary_source_type="Wikisource (ru): История государства Российского",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="クルィロフ『寓話集』",
    name_en="Krylov's Fables",
    name_original="Басни Крылова",
    period_key="19世紀ロシア・ロマンチズム黎明期",
    definition="イワン・クルィロフ（1769-1844）の寓話群（1809-43、9巻200篇余）。ラ・フォンテーヌ翻案と独自寓話を融合し、ロシア口語の規範を確立。多くの台詞がロシア語諺として定着。",
    background="ナポレオン戦争期ロシアの民族文学形成。",
    development="プーシキン以前のロシア口語的詩語の確立者。",
    historical_context="アレクサンドル一世期ロシアの民族意識。",
    primary_source_url=WSRC_RU+"Иван_Андреевич_Крылов",
    primary_source_type="Wikisource (ru): Крылов Басни",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="プーシキン『ベールキン物語』",
    name_en="Pushkin's Tales of Belkin",
    name_original="Повести покойного Ивана Петровича Белкина",
    period_key="19世紀ロシア黄金時代",
    definition="プーシキンが1830年ボルジノ村で書いた5編の連作短編集（『射撃』『吹雪』『葬儀屋』『駅長』『令嬢百姓娘』）。架空編者ベールキンを介した枠物語形式で、ロシア近代散文の規範を確立した。",
    background="ボルジノの秋(1830)、コレラ隔離下の創作。",
    development="ロシア近代短編小説の祖型、ゴーゴリ・チェーホフへの直接影響。",
    historical_context="ニコライ一世期ロシアの散文文学開花期。",
    primary_source_url=GUTEN+"ebooks/13437",
    primary_source_type="Project Gutenberg: Tales of Belkin",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="プーシキン『青銅の騎士』",
    name_en="Pushkin's Bronze Horseman",
    name_original="Медный всадник",
    period_key="19世紀ロシア黄金時代",
    definition="プーシキンが1833年に書いたペテルブルク叙事詩。1824年大洪水で恋人を失った小役人エヴゲーニイが、ピョートル大帝銅像に呪詛を投げかけ追われる幻想譚。国家と個人の永遠の対立を主題化したロシア文学最重要作品。",
    background="ピョートル大帝とニコライ一世の権力国家像、ペテルブルク神話の文学化。",
    development="ベールイ『ペテルブルク』、20世紀ペテルブルク・テクスト研究の祖型。",
    historical_context="ニコライ一世期ロシアの専制国家批判の暗喩。",
    primary_source_url=GUTEN+"ebooks/22094",
    primary_source_type="Project Gutenberg: The Bronze Horseman",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="プーシキン『エヴゲーニイ・オネーギン』",
    name_en="Pushkin's Eugene Onegin",
    name_original="Евгений Онегин",
    period_key="19世紀ロシア黄金時代",
    definition="プーシキンが1823-31年に執筆した韻文小説（全8章）。退屈な貴族青年オネーギンとタチヤーナの不成就の恋を描き、「オネーギン詩節」と呼ばれる独自の14行ソネット形式で、ロシア近代詩・小説の規範を確立した。",
    background="アレクサンドル一世末期ロシア貴族文化、バイロン『ドン・ジュアン』の影響。",
    development="チャイコフスキー歌劇化(1879)、20世紀ロシア小説論（バフチン・ロトマン）の中心テクスト。",
    historical_context="デカブリスト蜂起前後のロシア貴族青年文化。",
    primary_source_url=GUTEN+"ebooks/23997",
    primary_source_type="Project Gutenberg: Eugene Onegin",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="プーシキン『ボリス・ゴドゥノフ』",
    name_en="Pushkin's Boris Godunov",
    name_original="Борис Годунов",
    period_key="19世紀ロシア黄金時代",
    definition="プーシキンが1825年ミハイロフスコエ流刑中に書いた歴史劇。動乱時代のボリス・ゴドゥノフ（1598-1605治世）と僭称ドミトリーの抗争を描く。シェイクスピア史劇の影響下にロシア国民演劇の規範を確立した。",
    background="ニコライ一世期ロシアの権力批判、シェイクスピア史劇受容。",
    development="ムソルグスキー歌劇化(1869)、20世紀ロシア演劇研究の中心テクスト。",
    historical_context="ニコライ一世即位直後の専制批判の暗喩。",
    primary_source_url=GUTEN+"ebooks/4929",
    primary_source_type="Project Gutenberg: Boris Godunov",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="プーシキン『モーツァルトとサリエリ』",
    name_en="Pushkin's Mozart and Salieri",
    name_original="Моцарт и Сальери",
    period_key="19世紀ロシア黄金時代",
    definition="プーシキンが1830年ボルジノで書いた小悲劇連作の一編。サリエリによるモーツァルト毒殺伝説を素材に、天才と才能の永遠の対立を描く。リムスキー＝コルサコフ歌劇化(1898)で世界的に知られる。",
    background="ボルジノの秋(1830)、プーシキンの「小悲劇」連作（4編）の一。",
    development="20世紀ロシア・ヨーロッパ天才論の文学的祖型。",
    historical_context="ニコライ一世期ロシア知識人の天才論。",
    primary_source_url=GUTEN+"ebooks/13522",
    primary_source_type="Project Gutenberg: Little Tragedies",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="プーシキン『大尉の娘』",
    name_en="Pushkin's Captain's Daughter",
    name_original="Капитанская дочка",
    period_key="19世紀ロシア黄金時代",
    definition="プーシキンが1836年に発表した歴史中編小説。プガチョフ反乱(1773-75)を背景に、若い将校ピョートル・グリニョフの恋愛と忠誠を描く。ロシア歴史小説の祖型として、トルストイ・ショーロホフへの直接影響。",
    background="プーシキンによるプガチョフ史料調査(1833)、ロシア歴史小説の規範化。",
    development="トルストイ『戦争と平和』、ショーロホフ『静かなドン』の祖型。",
    historical_context="ニコライ一世期ロシアの民衆反乱史への関心。",
    primary_source_url=GUTEN+"ebooks/13511",
    primary_source_type="Project Gutenberg: The Captain's Daughter",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="レールモントフ『ペチョーリンの日記』",
    name_en="Lermontov's Pechorin's Journal",
    name_original="Журнал Печорина",
    period_key="19世紀ロシア黄金時代",
    definition="レールモントフ『現代の英雄』(1840)後半部の主人公ペチョーリンの日記。「タマーニ」「メリー姫」「運命論者」の3章で構成され、近代ロシア心理小説の祖型を確立。一人称分析的散文の規範作。",
    background="ニコライ一世期ロシア青年層のバイロン的虚無、コーカサス戦争体験。",
    development="ドストエフスキー、トルストイ近代心理小説への直接影響。",
    historical_context="ニコライ一世期ロシアの「余計な人」文化。",
    primary_source_url=GUTEN+"ebooks/913",
    primary_source_type="Project Gutenberg: A Hero of Our Time",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="レールモントフ『デーモン』",
    name_en="Lermontov's Demon",
    name_original="Демон",
    period_key="19世紀ロシア黄金時代",
    definition="レールモントフが1829-39年に書き続けた長編詩（8稿）。コーカサス・グルジアを舞台に、堕天使デーモンと修道女タマーラの不可能な恋を描く。ロシア・ロマン派詩の頂点で、ヴルーベリの絵画化(1890)、ルビンシテイン歌劇化(1875)で象徴主義に深い影響。",
    background="バイロン・ヴィニー『悪魔の試練』のロシア・ロマン派的展開、コーカサス神話。",
    development="ロシア象徴主義の中心モチーフ、20世紀デーモン論の文学的源泉。",
    historical_context="ニコライ一世期ロシアのバイロン主義最盛期。",
    primary_source_url=WSRC_RU+"Демон_(Лермонтов)",
    primary_source_type="Wikisource (ru): Демон",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# B: Gogol/Tyutchev/Fet/Maykov/Polonsky (10)
# ============================================================
add(**RUS, name_ja="ゴーゴリ『鼻』",
    name_en="Gogol's Nose",
    name_original="Нос",
    period_key="19世紀ロシア黄金時代",
    definition="ゴーゴリが1836年に発表したペテルブルク連作の幻想短編。ペテルブルク役人コワリョフの鼻が独立して街を歩き回る不条理譚。ナンセンス・グロテスク文学の祖型として、20世紀カフカ・ベケットへの直接的先行作。",
    background="ニコライ一世期ペテルブルク官僚社会の風刺、ホフマン的幻想散文の継承。",
    development="20世紀世界不条理文学（カフカ、ベケット）の祖型。",
    historical_context="ペテルブルク官僚社会の階級的格差。",
    primary_source_url=GUTEN+"ebooks/36238",
    primary_source_type="Project Gutenberg: The Nose",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ゴーゴリ『外套』",
    name_en="Gogol's Overcoat",
    name_original="Шинель",
    period_key="19世紀ロシア黄金時代",
    definition="ゴーゴリが1842年に発表したペテルブルク連作の中編。九等官アカーキー・アカーキエヴィチが新しい外套を作り盗まれて死に、亡霊として現れる悲劇譚。「我々はみなゴーゴリの外套から出てきた」と言われ、ロシア・リアリズム小説の祖型。",
    background="ニコライ一世期ペテルブルク下級役人の社会的悲惨、自然派散文の確立。",
    development="ドストエフスキー『貧しき人々』、20世紀ロシア小役人文学の祖型。",
    historical_context="ニコライ一世期ペテルブルクの官僚機構。",
    primary_source_url=GUTEN+"ebooks/36034",
    primary_source_type="Project Gutenberg: The Cloak (Overcoat)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ゴーゴリ『死せる魂』",
    name_en="Gogol's Dead Souls",
    name_original="Мёртвые души",
    period_key="19世紀ロシア黄金時代",
    definition="ゴーゴリが1842年に発表した長編「ポエマ」（第一部）。詐欺師チチコフがロシア地方を巡り、死亡農奴の名簿を買い集める旅を通じてロシア地主階級の諷刺画廊を構築。ロシア地方リアリズムの祖型で、第二部は1852年焼却された。",
    background="ニコライ一世期ロシア農奴制社会の諷刺、ダンテ『神曲』の世俗化。",
    development="チェーホフ・ブルガーコフ・ナボコフへの直接的影響。",
    historical_context="農奴解放(1861)以前のロシア地方社会。",
    primary_source_url=GUTEN+"ebooks/1081",
    primary_source_type="Project Gutenberg: Dead Souls",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ゴーゴリ『検察官』",
    name_en="Gogol's Government Inspector",
    name_original="Ревизор",
    period_key="19世紀ロシア黄金時代",
    definition="ゴーゴリが1836年に発表した5幕喜劇。地方都市の役人たちが通りすがりの青年フレスタコフを偽の検察官と誤認し賄賂を捧げる諷刺劇。ニコライ一世も観劇し笑った傑作で、ロシア国民演劇の規範作。",
    background="ニコライ一世期ロシア地方官僚機構の腐敗、プーシキンが題材を提供。",
    development="チェーホフ、ブルガーコフ、20世紀ロシア演劇の祖型。",
    historical_context="ニコライ一世期ロシア地方官僚社会の風刺。",
    primary_source_url=GUTEN+"ebooks/19960",
    primary_source_type="Project Gutenberg: The Inspector-General",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ゴーゴリ『友人との往復書簡選』",
    name_en="Gogol's Selected Passages from Correspondence with Friends",
    name_original="Выбранные места из переписки с друзьями",
    period_key="19世紀ロシア黄金時代",
    definition="ゴーゴリが1847年に発表した宗教思想随筆集。後期ゴーゴリの保守的・宗教的思想を表明し、ベリンスキー激烈批判書簡を引き起こした。19世紀ロシア知識人内戦（西欧派 vs スラヴ派）の中心争点。",
    background="ゴーゴリ後期の宗教的危機、ローマ滞在期の保守主義化。",
    development="ベリンスキー・ザルツブルク書簡(1847)・19世紀ロシア知識人論争の決定的瞬間。",
    historical_context="ニコライ一世末期ロシア思想史の分水嶺。",
    primary_source_url=WSRC_RU+"Выбранные_места_из_переписки_с_друзьями",
    primary_source_type="Wikisource (ru): Выбранные места",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="チュッチェフ『沈黙』",
    name_en="Tyutchev's Silentium",
    name_original="Silentium!",
    period_key="19世紀ロシア黄金時代",
    definition="フョードル・チュッチェフ（1803-73）が1830年に書いた哲学詩。「思想は言語化されると虚偽となる」と歌い、ロシア哲学詩の祖型を確立。20世紀ロシア象徴主義（メレジコフスキー・ヴャチェスラフ・イワノフ）の中心参照詩。",
    background="ドイツ・ロマン派哲学（シェリング・F.シュレーゲル）のロシア受容。",
    development="ロシア象徴主義詩学・20世紀沈黙論詩学の祖型。",
    historical_context="ニコライ一世期ロシア哲学詩の確立。",
    primary_source_url=WSRC_RU+"Silentium!_(Тютчев)",
    primary_source_type="Wikisource (ru): Silentium",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="チュッチェフ自然抒情詩",
    name_en="Tyutchev's nature lyrics",
    name_original="Природная лирика Тютчева",
    period_key="19世紀ロシア黄金時代",
    definition="チュッチェフの自然・宇宙抒情詩群（『春の雷雨』1828、『海の波には旋律がある』1865等）。シェリング自然哲学の影響下にロシア自然詩の規範を確立。チュッチェフの自然詩はロシア宇宙論的詩学の中心。",
    background="ドイツ自然哲学のロシア受容、19世紀後半ロシア自然詩の成熟。",
    development="ブロック・パステルナーク自然詩への直接影響。",
    historical_context="19世紀後半ロシアの自然哲学・宇宙論の文化的台頭。",
    primary_source_url=RVB+"tyutchev/",
    primary_source_type="Russian Virtual Library: Тютчев",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="チュッチェフ『最後の愛』",
    name_en="Tyutchev's Last Love",
    name_original="Последняя любовь",
    period_key="19世紀ロシア黄金時代",
    definition="チュッチェフが1851-54年に書いた「デニシエフ・サイクル」の代表詩。晩年の愛人エレーナ・デニシエワへの愛と罪意識を描く悲劇的抒情詩群。19世紀ロシア愛情詩の頂点として、20世紀アフマートヴァ・ツヴェターエワへの直接影響。",
    background="チュッチェフ晩年のデニシエワとの15年に及ぶ不倫関係。",
    development="アフマートヴァ・ツヴェターエワ愛情詩学の祖型。",
    historical_context="アレクサンドル二世初期ロシア社交界の道徳危機。",
    primary_source_url=RVB+"tyutchev/01text/01versus/",
    primary_source_type="Russian Virtual Library: Денисьевский цикл",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="フェート抒情詩",
    name_en="Fet's lyrical poetry",
    name_original="Лирика Фета",
    period_key="19世紀ロシア黄金時代",
    definition="アファナーシー・フェート（1820-92）の抒情詩群（『夕べの灯』1883-91、4部、200篇余）。「シューマン的」音楽性で純粋抒情を追求し、ショーペンハウアー哲学の翻訳者でもあった。ロシア「純粋芸術派」の代表で、象徴主義詩への直接的祖型。",
    background="19世紀後半ロシアの「純粋芸術派 vs 民衆派」論争、ショーペンハウアー哲学受容。",
    development="ロシア象徴主義詩（バリモント・ベリイ）への直接影響。",
    historical_context="アレクサンドル二世期ロシア知識人の芸術論争。",
    primary_source_url=RVB+"fet/",
    primary_source_type="Russian Virtual Library: Фет",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="アポロン・マイコフ詩集",
    name_en="Apollon Maykov poetry",
    name_original="Стихотворения Аполлона Майкова",
    period_key="19世紀ロシア黄金時代",
    definition="アポロン・マイコフ（1821-97）の古典派詩集群（『ローマ詩集』1847、『おとぎの国』1879）。ギリシア・ローマ古典の翻案と、ロシア宗教史叙事詩を融合。19世紀後半ロシア古典派詩の代表で、『イーゴリ軍記』翻訳者としても重要。",
    background="19世紀後半ロシアの古典学受容、スラヴ派思想の文学化。",
    development="20世紀ロシア・アクメイズム（グミリョフ）の古典派的傾向の祖型。",
    historical_context="アレクサンドル二世期ロシア古典派文化。",
    primary_source_url=RVB+"19vek/maykov/",
    primary_source_type="Russian Virtual Library: А.Н. Майков",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# C: Late 19c novelists (10)
# ============================================================
add(**RUS, name_ja="ポロンスキー詩集",
    name_en="Polonsky poetry",
    name_original="Стихотворения Полонского",
    period_key="19世紀ロシア黄金時代",
    definition="ヤコフ・ポロンスキー（1819-98）の抒情詩集群（『ジプシー女』『鈴』等）。フェート・チュッチェフと並ぶ19世紀後半ロシア「純粋芸術派」の代表で、ロマン主義抒情と都市散文詩の融合を試みた。20世紀ブロック詩学への先行。",
    background="19世紀後半ロシア純粋芸術派、フェート・マイコフと並ぶ三大抒情詩人。",
    development="20世紀初頭ブロック・象徴主義詩への直接影響。",
    historical_context="アレクサンドル二世期ロシア知識人の抒情詩文化。",
    primary_source_url=RVB+"19vek/polonsky/",
    primary_source_type="Russian Virtual Library: Я.П. Полонский",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="トルストイ『セヴァストポリ物語』",
    name_en="Tolstoy's Sevastopol Sketches",
    name_original="Севастопольские рассказы",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トルストイが1855-56年に発表したクリミア戦争従軍記三部作。セヴァストポリ攻囲戦(1854-55)を兵士の視点から描く即時的リポルタージュで、「真実こそ私の英雄」のテーゼがトルストイ後期リアリズムの倫理的基盤を形成。",
    background="トルストイ自身のクリミア戦争従軍体験(1854-55)。",
    development="『戦争と平和』への直接的予兆、20世紀戦争文学の祖型。",
    historical_context="クリミア戦争敗北後のロシア社会改革機運。",
    primary_source_url=GUTEN+"ebooks/22996",
    primary_source_type="Project Gutenberg: Sevastopol Sketches",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="トルストイ『懺悔』",
    name_en="Tolstoy's Confession",
    name_original="Исповедь",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トルストイが1882年に書いた宗教的告白記。50歳での精神的危機と、教会権威への懐疑を経た独自のキリスト教信仰確立を記す。後期トルストイ宗教思想の出発点で、20世紀世界宗教思想（ガンジー・ベルジャーエフ）への直接影響。",
    background="トルストイ50歳の精神的危機(1879-82)、教会から破門の起源。",
    development="ガンジー非暴力主義、20世紀キリスト教アナキズムの直接的源流。",
    historical_context="アレクサンドル三世期ロシアの宗教思想再編。",
    primary_source_url=GUTEN+"ebooks/43794",
    primary_source_type="Project Gutenberg: A Confession",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="トルストイ『神の国は汝らの内にあり』",
    name_en="Tolstoy's The Kingdom of God Is Within You",
    name_original="Царство Божие внутри вас",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トルストイが1893年にドイツで初刊した宗教思想書。「無抵抗」「非戦」を中心とするキリスト教アナキズム綱領で、ロシアでは禁書。ガンジーが1894年に読み感銘し、後の非暴力主義運動の理論的源泉となった。",
    background="トルストイ後期キリスト教アナキズム思想の体系化。",
    development="ガンジー、キング牧師、20世紀世界非暴力主義の中心源流。",
    historical_context="アレクサンドル三世期ロシアの宗教検閲・トルストイ破門への抵抗。",
    primary_source_url=GUTEN+"ebooks/43302",
    primary_source_type="Project Gutenberg: The Kingdom of God Is Within You",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="トルストイ『芸術とは何か』",
    name_en="Tolstoy's What Is Art?",
    name_original="Что такое искусство?",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トルストイが1897-98年に発表した美学論。芸術の本質を「感情の伝達」と定義し、シェイクスピア・ベートーヴェン・ワーグナーを「人民から離れた芸術」と批判。19世紀末ロシア・ヨーロッパ美学論の最大スキャンダル書。",
    background="トルストイ後期宗教思想の美学への適用、フランス象徴主義への批判。",
    development="20世紀芸術社会学・芸術定義論の中心参照点。",
    historical_context="19世紀末ヨーロッパ世紀末美学への倫理的反論。",
    primary_source_url=GUTEN+"ebooks/64908",
    primary_source_type="Project Gutenberg: What Is Art?",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="トゥルゲーネフ『ルージン』",
    name_en="Turgenev's Rudin",
    name_original="Рудин",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トゥルゲーネフが1856年に発表した第一長編。雄弁ながら行動できない知識人ルージンを通じて、1840年代ロシア「余計な人」の典型を造形。トゥルゲーネフ社会小説連作の出発点で、ロシア知識人小説の規範。",
    background="ニコライ一世期ロシア・ヘーゲル派青年（バクーニン世代）の文学化。",
    development="ドストエフスキー『悪霊』、20世紀ロシア知識人論小説の祖型。",
    historical_context="クリミア戦争敗北後のロシア知識人の自己批判機運。",
    primary_source_url=GUTEN+"ebooks/6900",
    primary_source_type="Project Gutenberg: Rudin",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="トゥルゲーネフ『その前夜』",
    name_en="Turgenev's On the Eve",
    name_original="Накануне",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トゥルゲーネフが1860年に発表した長編小説。ロシア娘エレーナがブルガリア人革命家インサーロフを愛し共に祖国解放戦争に身を投じる物語。1860年代ロシア社会改革機運下の英雄探求を文学化した。",
    background="アレクサンドル二世大改革前夜のロシア社会改革機運、バルカン民族解放運動。",
    development="ロシア社会派小説、19世紀末バルカン解放戦争文学への影響。",
    historical_context="農奴解放(1861)前夜のロシア社会変革期。",
    primary_source_url=GUTEN+"ebooks/8649",
    primary_source_type="Project Gutenberg: On the Eve",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="トゥルゲーネフ『猟人日記』",
    name_en="Turgenev's A Sportsman's Sketches",
    name_original="Записки охотника",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トゥルゲーネフが1847-52年に『現代人』誌に発表した短編連作（25編）。ロシア地方の農民・地主の風俗をスケッチ的散文で描き、農奴制批判の社会的効果を発揮。アレクサンドル二世が「農奴解放決断の一因」と回顧した文学史的事件。",
    background="ニコライ一世期ロシア農奴制下の地方社会、自然派散文の確立。",
    development="ロシア・リアリズム短編、19世紀ヨーロッパ社会派文学の祖型。",
    historical_context="ニコライ一世末期から農奴解放(1861)前夜のロシア改革機運。",
    primary_source_url=GUTEN+"ebooks/8597",
    primary_source_type="Project Gutenberg: A Sportsman's Sketches",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="サルトィコフ＝シチェドリン『ある町の歴史』",
    name_en="Saltykov-Shchedrin's History of a Town",
    name_original="История одного города",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="サルトィコフ＝シチェドリン（1826-89）が1869-70年に発表した諷刺的擬似歴史。架空都市グルポフの歴代「市長」たちの愚行を「史料」風に綴り、ロシア専制政治の本質を諷刺。20世紀全体主義文学（オーウェル・ハクスリー）の祖型。",
    background="アレクサンドル二世期ロシアの官僚専制への文学的批判。",
    development="ザミャーチン『われら』、20世紀ディストピア文学の祖型。",
    historical_context="アレクサンドル二世期ロシア改革停滞期。",
    primary_source_url=LIB_RU+"saltykov/istoriya_odnogo_goroda/index.html",
    primary_source_type="ilibrary.ru: История одного города",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="サルトィコフ＝シチェドリン『大人のためのお伽話』",
    name_en="Saltykov-Shchedrin's Fairy Tales for Grown-ups",
    name_original="Сказки для детей изрядного возраста",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="サルトィコフ＝シチェドリンが1869-86年に書いた32編の諷刺寓話集。動物寓話形式でロシア専制・知識人・庶民を諷刺し、19世紀後半ロシア検閲下の社会批判の規範を確立した。",
    background="アレクサンドル二世末期から三世期にかけてのロシア検閲強化への対応。",
    development="20世紀ロシア・ソ連諷刺文学（イリフ＝ペトロフ・ブルガーコフ）の祖型。",
    historical_context="アレクサンドル三世期ロシアの反動的政治情勢。",
    primary_source_url=LIB_RU+"saltykov/skazki/index.html",
    primary_source_type="ilibrary.ru: Сказки",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: Silver Age expansion (10)
# ============================================================
add(**RUS, name_ja="レスコフ『左利き』",
    name_en="Leskov's Lefty",
    name_original="Левша",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="ニコライ・レスコフ（1831-95）が1881年に発表した短編。トゥーラの鍛冶屋「左利き」が英国製の鋼鉄の蚤に蹄鉄を打つ物語を、ロシア民衆の口語的「スカーズ」形式で語る。ロシア・スカーズ散文の規範作。",
    background="アレクサンドル三世期ロシア民衆主義の文化的台頭、レスコフのスカーズ散文確立。",
    development="20世紀ロシア・スカーズ散文（ゾーシチェンコ・バーベリ）の祖型。",
    historical_context="アレクサンドル三世期ロシアの民衆主義文化。",
    primary_source_url=LIB_RU+"leskov/levsha/index.html",
    primary_source_type="ilibrary.ru: Левша",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="レスコフ『魅せられた旅人』",
    name_en="Leskov's Enchanted Wanderer",
    name_original="Очарованный странник",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="レスコフが1873年に発表した中編小説。元農奴イワン・フリャーギンが波乱の人生を語る半自伝風スカーズ。ロシア聖愚者・放浪者類型の文学的集大成で、19世紀後半ロシア宗教的散文の傑作。",
    background="アレクサンドル二世期ロシア宗教的民衆主義、レスコフの聖人伝関心。",
    development="20世紀ロシア宗教的散文・放浪者文学の祖型。",
    historical_context="アレクサンドル二世期ロシア民衆宗教文化。",
    primary_source_url=LIB_RU+"leskov/ocharovanyj_strannik/index.html",
    primary_source_type="ilibrary.ru: Очарованный странник",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="コロレンコ『マカルの夢』",
    name_en="Korolenko's Makar's Dream",
    name_original="Сон Макара",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="ウラジーミル・コロレンコ（1853-1921）が1885年に発表したシベリア中編。ヤクート流刑中に書かれた農民マカルの夢幻譚で、神の前で自己弁護する民衆の罪を描く。19世紀後半ロシア・シベリア文学の代表作。",
    background="コロレンコ自身のヤクート流刑(1881-84)体験、シベリア民族誌的関心。",
    development="20世紀ロシア・シベリア文学・民衆主義文学の祖型。",
    historical_context="アレクサンドル三世期ロシア政治流刑制度。",
    primary_source_url=WSRC_RU+"Сон_Макара_(Короленко)",
    primary_source_type="Wikisource (ru): Сон Макара",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="コロレンコ『盲目の音楽家』",
    name_en="Korolenko's Blind Musician",
    name_original="Слепой музыкант",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="コロレンコが1886年に発表した中編小説。生まれつき盲目の貴族青年ペトロが音楽を通じて世界と関係を結ぶ過程を描く心理的成長譚。19世紀末ロシア民衆主義文学と心理小説の融合作。",
    background="アレクサンドル三世期ロシアの民衆主義と心理小説の合流。",
    development="20世紀ロシア障害者文学・教育心理小説の先駆。",
    historical_context="19世紀末ロシア教育思想・身体障害観の変化。",
    primary_source_url=WSRC_RU+"Слепой_музыкант_(Короленко)",
    primary_source_type="Wikisource (ru): Слепой музыкант",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="ガールシン『赤い花』",
    name_en="Garshin's Red Flower",
    name_original="Красный цветок",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="フセヴォロド・ガールシン（1855-88）が1883年に発表した精神病院短編。狂人の主人公が世界の悪を体現する庭の赤い花を倒す使命に取り憑かれる物語。19世紀末ロシア狂気文学の祖型で、チェーホフ『六号室』への直接影響。",
    background="ガールシン自身の精神疾患・露土戦争従軍体験(1877-78)。",
    development="チェーホフ『六号室』、20世紀ロシア狂気文学の祖型。",
    historical_context="アレクサンドル三世期ロシア医学的・心理学的言説の発展。",
    primary_source_url=WSRC_RU+"Красный_цветок_(Гаршин)",
    primary_source_type="Wikisource (ru): Красный цветок",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="ガールシン『四日間』",
    name_en="Garshin's Four Days",
    name_original="Четыре дня",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="ガールシンが1877年に発表した露土戦争短編。負傷した兵士イワノフがブルガリア戦場に4日間放置され、敵兵の腐乱死体と対話する物語。19世紀末ロシア反戦文学の祖型で、20世紀世界戦争文学への影響大。",
    background="ガールシン自身の露土戦争従軍・負傷体験。",
    development="20世紀ロシア・ヨーロッパ反戦文学（レマルク・バルビュス）の祖型。",
    historical_context="露土戦争(1877-78)とロシア知識人の戦争観。",
    primary_source_url=WSRC_RU+"Четыре_дня_(Гаршин)",
    primary_source_type="Wikisource (ru): Четыре дня",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="ソログーブ『小悪魔』ペレドノフ像",
    name_en="Sologub's Petty Demon — Peredonov",
    name_original="Мелкий бес — Передонов",
    period_key="ロシア銀の時代",
    definition="フョードル・ソログーブ（1863-1927）が1907年に発表した『小悪魔』(1892-1902執筆)の主人公ペレドノフ像。地方教師ペレドノフが「ネドトゥィコムカ（捉えがたきもの）」幻覚に取り憑かれる物語は、ロシア・デカダンス散文の頂点で、20世紀世紀末文学の規範作。",
    background="19世紀末ロシア地方知識人の精神的崩壊、デカダンス散文の確立。",
    development="ナボコフ・ベケット世紀末散文の祖型として国際的影響大。",
    historical_context="ニコライ二世期ロシア地方教育界の精神的疲弊。",
    primary_source_url=LIB_RU+"sologub/melkij_bes/index.html",
    primary_source_type="ilibrary.ru: Мелкий бес",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ベールイ『銀の鳩』",
    name_en="Bely's Silver Dove",
    name_original="Серебряный голубь",
    period_key="ロシア銀の時代",
    definition="アンドレイ・ベールイ（1880-1934）が1909年に発表した長編小説。神学校生ダリャリスキーがロシア地方の鞭身派(ホルィスト)宗派に取り憑かれる物語。後の『ペテルブルク』への祖型で、20世紀ロシア・モダニズム散文の重要作。",
    background="20世紀初頭ロシアの民衆宗派研究、ベールイの象徴主義散文実験。",
    development="ベールイ『ペテルブルク』(1913-14)への直接的祖型。",
    historical_context="第一次ロシア革命(1905)後のロシア宗教文化的混乱。",
    primary_source_url=LIB_RU+"bely/serebryanyj_golub/index.html",
    primary_source_type="ilibrary.ru: Серебряный голубь",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="ブリューソフ『火の天使』",
    name_en="Briusov's Fiery Angel",
    name_original="Огненный ангел",
    period_key="ロシア銀の時代",
    definition="ヴァレリー・ブリューソフ（1873-1924）が1907-08年に発表した歴史長編小説。16世紀ドイツのケルンを舞台にした魔女狩り・神秘主義小説で、ロシア象徴主義の歴史散文の代表作。プロコフィエフ歌劇化(1927)で世界的に著名。",
    background="ブリューソフのニーナ・ペトロフスカヤ恋愛、ロシア象徴主義オカルト関心。",
    development="プロコフィエフ歌劇化、20世紀ロシア歴史小説の祖型。",
    historical_context="第一次ロシア革命(1905)後のロシア象徴主義成熟期。",
    primary_source_url=LIB_RU+"brusov/ognennyj_angel/index.html",
    primary_source_type="ilibrary.ru: Огненный ангел",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="アンネンスキー『糸杉の小箱』",
    name_en="Annensky's Cypress Casket",
    name_original="Кипарисовый ларец",
    period_key="ロシア銀の時代",
    definition="インノケンチー・アンネンスキー（1855-1909）が死後1910年に発表された詩集。ペテルブルクのデカダンス・印象主義詩で、後のアクメイズム（アフマートヴァ・グミリョフ）に直接影響。「ロシア20世紀詩の隠れた父」と呼ばれる。",
    background="19世紀末ロシア・デカダンス詩、フランス象徴主義（マラルメ・ヴェルレーヌ）の翻訳者。",
    development="アクメイズム詩学・20世紀ロシア詩研究の中心参照点。",
    historical_context="第一次ロシア革命(1905)後のロシア・デカダンス詩。",
    primary_source_url=RVB+"annenskij/",
    primary_source_type="Russian Virtual Library: Анненский",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# E: Acmeism deep (8)
# ============================================================
add(**RUS, name_ja="メレジコフスキー『キリストと反キリスト』三部作",
    name_en="Merezhkovsky's Christ and Antichrist trilogy",
    name_original="Христос и Антихрист",
    period_key="ロシア銀の時代",
    definition="ドミトリー・メレジコフスキー（1865-1941）が1895-1905年に発表した歴史長編三部作（『神々の死』『神々の復活』『反キリスト』）。背教者ユリアヌス・レオナルド・ピョートル大帝を題材に、二神論的歴史哲学を展開。ロシア象徴主義第一世代の哲学的代表作。",
    background="19世紀末ロシア宗教思想（ソロヴィヨフ・ロザノフ）の文学化。",
    development="20世紀ロシア宗教哲学・象徴主義散文の中心参照点。",
    historical_context="第一次ロシア革命(1905)前後のロシア宗教ルネサンス。",
    primary_source_url=LIB_RU+"merezhkovsky/",
    primary_source_type="ilibrary.ru: Мережковский",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="ヴャチェスラフ・イワノフ『コル・アルデンス』",
    name_en="Vyacheslav Ivanov's Cor Ardens",
    name_original="Cor Ardens",
    period_key="ロシア銀の時代",
    definition="ヴャチェスラフ・イワノフ（1866-1949）が1911年に発表した詩集。「燃える心」を意味し、古代ギリシア・ディオニュソス神秘主義の文学化。ロシア象徴主義第二世代の哲学的・神秘主義的詩学の頂点。",
    background="イワノフのディオニュソス研究、ニーチェ『悲劇の誕生』のロシア受容。",
    development="20世紀ロシア新異教主義・神秘主義詩学の中心テクスト。",
    historical_context="第一次ロシア革命(1905)後のロシア宗教ルネサンス。",
    primary_source_url=RVB+"ivanov/",
    primary_source_type="Russian Virtual Library: Вяч. Иванов",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="クズミーン『翼』",
    name_en="Kuzmin's Wings",
    name_original="Крылья",
    period_key="ロシア銀の時代",
    definition="ミハイル・クズミーン（1872-1936）が1906年に発表した中編小説。青年ヴァーニャの同性愛的精神的成長を描く。ロシア初の公然たる同性愛文学で、20世紀ロシアLGBT文学の祖型として国際的に重要。",
    background="20世紀初頭ロシアの「性の革命」、クズミーン自身の同性愛者としての立場。",
    development="20世紀ロシア・ヨーロッパLGBT文学研究の中心テクスト。",
    historical_context="第一次ロシア革命(1905)後の社会的タブー解体期。",
    primary_source_url=WIKI_RU+"Крылья_(повесть_Кузмина)",
    primary_source_type="Wikipedia (ru): Крылья",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**RUS, name_ja="アフマートヴァ『夕べ』",
    name_en="Akhmatova's Evening",
    name_original="Вечер",
    period_key="ロシア銀の時代",
    definition="アンナ・アフマートヴァ（1889-1966）が1912年に発表したデビュー詩集。アクメイズム派の感覚的具体性と、女性の愛の心理を圧縮された短詩で表現。20世紀ロシア詩の女性的視点の規範を確立した。",
    background="アクメイズム結社「詩人組合」(1911)結成、グミリョフとの結婚(1910)。",
    development="20世紀ロシア女性詩の規範、後のツヴェターエワ・パルヌィへの影響。",
    historical_context="ニコライ二世期ロシア銀の時代女性詩の確立。",
    primary_source_url=RVB+"akhmatova/",
    primary_source_type="Russian Virtual Library: Ахматова",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="アフマートヴァ『数珠』",
    name_en="Akhmatova's Rosary",
    name_original="Чётки",
    period_key="ロシア銀の時代",
    definition="アフマートヴァが1914年に発表した第二詩集。第一次大戦勃発前夜のペテルブルクを背景に、女性の愛と祈りを結合した抒情詩集。アクメイズム女性詩の規範作で、革命前ロシア最後の純粋抒情詩集の一。",
    background="アクメイズム成熟期、グミリョフ結婚生活の破綻過程。",
    development="20世紀ロシア女性愛情詩・宗教抒情詩の規範。",
    historical_context="第一次大戦勃発直前のロシア銀の時代終末期。",
    primary_source_url=RVB+"akhmatova/",
    primary_source_type="Russian Virtual Library: Чётки",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="アフマートヴァ『英雄なき詩』",
    name_en="Akhmatova's Poem Without a Hero",
    name_original="Поэма без героя",
    period_key="ソヴィエト中期",
    definition="アフマートヴァが1940-65年に書き続けた長詩。1913年ペテルブルクの仮装舞踏会から始まり、革命・粛清・戦争を経た「世紀の鏡」として20世紀ロシア史を凝縮。アフマートヴァ晩年の最高傑作で、20世紀ロシア詩の最終的成果。",
    background="アクメイズム世代の歴史的記憶、スターリン期粛清の集合的経験。",
    development="20世紀ロシア記憶詩学・歴史叙事詩研究の中心テクスト。",
    historical_context="スターリン期粛清から雪解け期にかけての文化的記憶。",
    primary_source_url=RVB+"akhmatova/",
    primary_source_type="Russian Virtual Library: Поэма без героя",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="マンデリシュタム『石』",
    name_en="Mandelstam's Stone",
    name_original="Камень",
    period_key="ロシア銀の時代",
    definition="オシップ・マンデリシュタム（1891-1938）が1913年に発表したデビュー詩集。「石」「建築」「ペテルブルク」をモチーフに、アクメイズム派の「事物の重み」詩学を確立。20世紀ロシア詩の建築的・古典的潮流の出発点。",
    background="アクメイズム結社「詩人組合」加入、マンデリシュタム哲学・古典学習。",
    development="20世紀ロシア・古典派詩学・建築詩学の規範作。",
    historical_context="第一次大戦勃発直前のロシア銀の時代成熟期。",
    primary_source_url=RVB+"mandelshtam/",
    primary_source_type="Russian Virtual Library: Мандельштам Камень",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="マンデリシュタム『ダンテについての対話』",
    name_en="Mandelstam's Conversation about Dante",
    name_original="Разговор о Данте",
    period_key="ソヴィエト中期",
    definition="マンデリシュタムが1933年に書いた詩学エッセイ。ダンテ『神曲』を「詩的物質性」「速度」「ダイナミック・ストラクチャー」の観点から再解釈する20世紀詩学最重要文書の一。生前未刊、1967年初刊。",
    background="マンデリシュタム1930年代地下執筆期、ヴォロネジ流刑前の哲学的省察。",
    development="20世紀ロシア・ヨーロッパ詩学（ヘイニー、ブロツキー）の中心参照点。",
    historical_context="スターリン期マンデリシュタム迫害期。",
    primary_source_url=RVB+"mandelshtam/",
    primary_source_type="Russian Virtual Library: Разговор о Данте",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# F: Futurism deep + Esenin/Pasternak/Tsvetaeva (8)
# ============================================================
add(**RUS, name_ja="グミリョフ『火の柱』",
    name_en="Gumilev's Pillar of Fire",
    name_original="Огненный столп",
    period_key="ロシア銀の時代",
    definition="ニコライ・グミリョフ（1886-1921）が1921年に発表した遺作詩集。銃殺(1921)直前に刊行された詩集で、「迷子の電車」「第六感」等を収録。ロシア・アクメイズム最後の最高傑作で、20世紀ロシア詩の冒険主義的潮流の頂点。",
    background="グミリョフのアフリカ探検・第一次大戦従軍・反革命陰謀容疑(1921)。",
    development="ブロツキー・タルコフスキーら20世紀後半ロシア詩への直接影響。",
    historical_context="ロシア内戦期から赤色テロ期にかけての知識人迫害。",
    primary_source_url=RVB+"gumilev/",
    primary_source_type="Russian Virtual Library: Огненный столп",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="マヤコフスキー『南京虫』",
    name_en="Mayakovsky's Bedbug",
    name_original="Клоп",
    period_key="ソヴィエト中期",
    definition="ウラジーミル・マヤコフスキー（1893-1930）が1929年に発表した諷刺喜劇。元革命家プリースィプキンが冷凍され50年後の共産主義未来で「ホモ・サピエンス・ブルジュアシス」として展示される反ユートピア劇。マヤコフスキー晩年の体制批判の頂点。",
    background="新経済政策末期ソ連の小ブルジョワ復活への批判、マヤコフスキー晩年の体制懐疑。",
    development="20世紀世界反ユートピア演劇（ブレヒト、イヨネスコ）の祖型。",
    historical_context="第一次五カ年計画期(1928-32)ソ連の文化的緊張。",
    primary_source_url=LIB_RU+"mayakovskij/klop/index.html",
    primary_source_type="ilibrary.ru: Клоп",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="フレーブニコフ『ザンゲジ』",
    name_en="Khlebnikov's Zangezi",
    name_original="Зангези",
    period_key="ロシア銀の時代",
    definition="ヴェリミル・フレーブニコフ（1885-1922）が1920-22年に書いた「超詩」（スヴェルクポエマ）。20の「平面」で構成され、神々・鳥・人間・数字の言語が混ざり合う前代未聞の言語実験詩。ロシア未来派の言語革命の頂点。",
    background="ロシア内戦期フレーブニコフの放浪生活、「数の宇宙論」探求。",
    development="20世紀世界実験詩・コンクリート詩への直接影響。",
    historical_context="ロシア内戦期文化的混乱の中の言語実験。",
    primary_source_url=RVB+"hlebnikov/",
    primary_source_type="Russian Virtual Library: Зангези",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="クルチョーヌィフ『太陽への勝利』",
    name_en="Kruchenykh's Victory over the Sun",
    name_original="Победа над Солнцем",
    period_key="ロシア銀の時代",
    definition="アレクセイ・クルチョーヌィフ（1886-1968）が1913年に発表した未来派オペラ・リブレット。マレーヴィチ舞台美術、マチューシン作曲。「太陽の捕獲」と新しい未来の宣言を「ザーウミ（超意味言語）」で表現。ロシア未来派の総合芸術の頂点。",
    background="ロシア未来派の総合芸術運動、サンクト・ペテルブルク初演(1913.12)。",
    development="マレーヴィチ「黒の四角」(1915)、20世紀世界アヴァンギャルドの祖型。",
    historical_context="第一次大戦勃発直前のロシア銀の時代アヴァンギャルド爆発期。",
    primary_source_url=WIKI_RU+"Победа_над_Солнцем",
    primary_source_type="Wikipedia (ru): Победа над Солнцем",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**RUS, name_ja="セヴェリャーニン『シャンパンのパイナップル』",
    name_en="Severyanin's Pineapples in Champagne",
    name_original="Ананасы в шампанском",
    period_key="ロシア銀の時代",
    definition="イーゴリ・セヴェリャーニン（1887-1941）が1915年に発表した詩集。エゴ未来派の創始者として、装飾的・甘美な都市詩で1910年代ロシア詩の流行を作った。1918年「詩王」選出後、エストニアに亡命。",
    background="1911年のエゴ未来派宣言、ロシア未来派内部の派閥抗争。",
    development="20世紀ロシア大衆詩・キャバレー詩学の祖型。",
    historical_context="第一次大戦下ロシアの都市文化最盛期。",
    primary_source_url=WSRC_RU+"Игорь_Северянин",
    primary_source_type="Wikisource (ru): Северянин",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="エセーニン『黒い男』",
    name_en="Esenin's Black Man",
    name_original="Чёрный человек",
    period_key="ソヴィエト中期",
    definition="セルゲイ・エセーニン（1895-1925）が1925年自殺直前に完成した長詩。鏡の中の「黒い男」と語り合う自己分裂の悲劇詩で、エセーニン晩年の精神的危機を凝縮。20世紀ロシア自殺詩学の頂点。",
    background="エセーニンの精神疾患・アルコール依存・1925年自殺。",
    development="マヤコフスキー自殺(1930)、20世紀ロシア自殺詩学の中心テクスト。",
    historical_context="新経済政策末期ソ連知識人の精神的疲弊。",
    primary_source_url=LIB_RU+"esenin/chernyj_chelovek/index.html",
    primary_source_type="ilibrary.ru: Чёрный человек",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="パステルナーク『わが妹なる人生』",
    name_en="Pasternak's My Sister Life",
    name_original="Сестра моя — жизнь",
    period_key="ロシア銀の時代",
    definition="ボリス・パステルナーク（1890-1960）が1922年に発表した第三詩集。1917年夏（二月革命と十月革命の間）の自然と愛を、革命的高揚と一体化させて描く。20世紀ロシア・モダニズム詩の頂点で、パステルナーク詩学の出発点。",
    background="ロシア二月・十月革命の間の精神的高揚、パステルナークの音楽・哲学的素養。",
    development="20世紀ロシア・モダニズム詩研究の中心参照点。",
    historical_context="ロシア革命期の精神的・文化的高揚期。",
    primary_source_url=RVB+"pasternak/",
    primary_source_type="Russian Virtual Library: Сестра моя — жизнь",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ツヴェターエワ『終りの詩』",
    name_en="Tsvetaeva's Poem of the End",
    name_original="Поэма Конца",
    period_key="ソヴィエト中期",
    definition="マリーナ・ツヴェターエワが1924年プラハで書いた長詩。亡命中の恋愛破綻を「別離」「終り」のテーマで描き、ツヴェターエワ亡命詩の頂点。20世紀ロシア女性詩・別離詩学の規範作。",
    background="ツヴェターエワのプラハ亡命期、コンスタンチン・ロドゼーヴィチとの恋愛破綻。",
    development="20世紀ロシア女性詩・別離詩学の中心参照点。",
    historical_context="戦間期プラハ・ロシア亡命文化の盛期。",
    primary_source_url=RVB+"tsvetaeva/",
    primary_source_type="Russian Virtual Library: Поэма Конца",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# G: Soviet prose (10)
# ============================================================
add(**RUS, name_ja="バーベリ『騎兵隊』",
    name_en="Babel's Red Cavalry",
    name_original="Конармия",
    period_key="ソヴィエト中期",
    definition="イサーク・バーベリ（1894-1940）が1926年に発表した連作短編集。ポーランド・ソヴィエト戦争(1920)に従軍したユダヤ人記者の視点から、コサック兵の暴力と詩的イメージを並置。20世紀ロシア戦争文学・短編散文の頂点。",
    background="バーベリ自身のブジョーンヌィ第一騎兵軍従軍(1920)、ユダヤ人インテリの視点。",
    development="20世紀世界戦争文学・短編散文の祖型として国際的影響大。",
    historical_context="ロシア内戦期最終局面のポーランド・ソヴィエト戦争。",
    primary_source_url=LIB_RU+"babel/konarmiya/index.html",
    primary_source_type="ilibrary.ru: Конармия",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="バーベリ『オデッサ物語』",
    name_en="Babel's Odessa Stories",
    name_original="Одесские рассказы",
    period_key="ソヴィエト中期",
    definition="バーベリが1923-24年に発表した短編集。革命前後のオデッサ・モルダヴァンカ地区のユダヤ人ギャング王ベーニャ・クリーク（モルデハイ・ヤフナリエルの息子）を主人公にした連作。20世紀ロシア・ユダヤ人地方文学の頂点。",
    background="バーベリ自身のオデッサ出身、革命前後のオデッサ・ユダヤ人犯罪文化。",
    development="20世紀ロシア・ユダヤ人文学・地方語散文の祖型。",
    historical_context="新経済政策期ソ連のユダヤ人文化最盛期。",
    primary_source_url=LIB_RU+"babel/odesskie_rasskazy/index.html",
    primary_source_type="ilibrary.ru: Одесские рассказы",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="ピリニャーク『裸の年』",
    name_en="Pilnyak's Naked Year",
    name_original="Голый год",
    period_key="ソヴィエト中期",
    definition="ボリス・ピリニャーク（1894-1938）が1922年に発表した最初のソ連内戦長編小説。1919年ロシア地方都市オルデュンの革命的混沌を断片的・モンタージュ的散文で描く。1920年代ソ連実験的散文の祖型。",
    background="ロシア内戦期(1918-22)の文化的混乱、ピリニャークのモダニズム的散文実験。",
    development="20世紀ソ連実験的散文（プラトーノフ・ブルガーコフ）の祖型。",
    historical_context="ロシア内戦末期から新経済政策初期の文化的過渡期。",
    primary_source_url=LIB_RU+"pilnyak/golyj_god/index.html",
    primary_source_type="ilibrary.ru: Голый год",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="フルマーノフ『チャパーエフ』",
    name_en="Furmanov's Chapaev",
    name_original="Чапаев",
    period_key="ソヴィエト中期",
    definition="ドミトリー・フルマーノフ（1891-1926）が1923年に発表した内戦小説。ウラル戦線で戦死したチャパーエフ師団長(1887-1919)を主人公にした半自伝的英雄譚。後の社会主義リアリズム小説の祖型として、ヴァシリエフ兄弟映画化(1934)で国民的英雄像に。",
    background="フルマーノフ自身のチャパーエフ師団政治委員経験(1919)。",
    development="社会主義リアリズム英雄小説の規範、ペレーヴィン『チャパーエフと空虚』への祖型。",
    historical_context="ロシア内戦期赤軍英雄崇拝の文学的構築。",
    primary_source_url=LIB_RU+"furmanov/chapaev/index.html",
    primary_source_type="ilibrary.ru: Чапаев",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="ショーロホフ『開かれた処女地』",
    name_en="Sholokhov's Virgin Soil Upturned",
    name_original="Поднятая целина",
    period_key="ソヴィエト中期",
    definition="ミハイル・ショーロホフ（1905-84）が1932-60年に発表した長編二巻。コサック村グレミャーチイ・ロークの集団化(1930)の悲劇と勝利を描く社会主義リアリズム集団化小説の規範作。1965年ノーベル文学賞受賞作家の代表作。",
    background="第一次五カ年計画期コサック地域の集団化体験。",
    development="社会主義リアリズム集団化小説の規範、戦後ソ連農村文学への影響大。",
    historical_context="第一次五カ年計画期(1928-32)から後期ソ連の集団化総括。",
    primary_source_url=LIB_RU+"sholohov/podnjataja_celina/index.html",
    primary_source_type="ilibrary.ru: Поднятая целина",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="カターエフ『遠ざかる白い帆』",
    name_en="Kataev's Lonely Sail Whitens",
    name_original="Белеет парус одинокий",
    period_key="ソヴィエト中期",
    definition="ヴァレンチン・カターエフ（1897-1986）が1936年に発表した青少年向け歴史小説。1905年革命下のオデッサで、少年ペーチャと水兵ガヴリークの冒険を描く。20世紀ソ連青少年文学の規範作で、革命前史の郷愁的描写。",
    background="1905年第一次ロシア革命のオデッサ・潜在記憶、カターエフ自身の少年期。",
    development="ソ連青少年文学・歴史小説の規範作として継続再版。",
    historical_context="スターリン期ソ連の革命前史の文化的回想。",
    primary_source_url=LIB_RU+"kataev/beleet_parus/index.html",
    primary_source_type="ilibrary.ru: Белеет парус одинокий",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="ファジェーエフ『若き親衛隊』",
    name_en="Fadeev's Young Guard",
    name_original="Молодая гвардия",
    period_key="ソヴィエト中期",
    definition="アレクサンドル・ファジェーエフ（1901-56）が1945年に発表した独ソ戦小説。クラスノドン青年地下組織「若き親衛隊」(1942-43)を題材にした社会主義リアリズム英雄小説。1948年スターリンの指示で改稿させられ、後にファジェーエフ自殺(1956)の遠因。",
    background="独ソ戦下クラスノドン青年地下組織の実話、戦後スターリン文化政策。",
    development="社会主義リアリズム英雄小説の典型、ソ連青少年文学規範作。",
    historical_context="第二次大戦末期から戦後スターリン期の文化政策。",
    primary_source_url=LIB_RU+"fadeev/molodaya_gvardiya/index.html",
    primary_source_type="ilibrary.ru: Молодая гвардия",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="エレンブルク『雪解け』",
    name_en="Erenburg's Thaw",
    name_original="Оттепель",
    period_key="ソヴィエト中期",
    definition="イリヤ・エレンブルク（1891-1967）が1954-56年に発表した中編二部作。スターリン死(1953)後のソ連知識人の精神的解放を描き、「雪解け」期(オッテペリ)の名称の由来となった作品。フルシチョフ脱スターリン化期文学の象徴。",
    background="スターリン死(1953)直後のソ連知識人の精神的解放。",
    development="フルシチョフ「雪解け」期文化の名称由来、ソ連改革文学の出発点。",
    historical_context="スターリン死直後から第20回党大会(1956)にかけての文化的解凍期。",
    primary_source_url=LIB_RU+"ehrenburg/ottepel/index.html",
    primary_source_type="ilibrary.ru: Оттепель",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="エレンブルク『人々・歳月・人生』",
    name_en="Erenburg's People, Years, Life",
    name_original="Люди, годы, жизнь",
    period_key="ソヴィエト中期",
    definition="エレンブルクが1961-65年に発表した6巻の自伝的回想録。20世紀前半ロシア・ヨーロッパ知識人（マンデリシュタム・ピカソ・モディリアーニ・ヘミングウェイ等）の交友記。雪解け期最大の文化的事件で、ソ連知識人の歴史的記憶回復の中心テクスト。",
    background="フルシチョフ「雪解け」期の歴史的記憶回復機運。",
    development="20世紀ロシア・ヨーロッパ知識人交流史の中心参照点。",
    historical_context="フルシチョフ後期から停滞期初期のソ連文化記憶。",
    primary_source_url=LIB_RU+"ehrenburg/lyudi_gody_zhizn/index.html",
    primary_source_type="ilibrary.ru: Люди, годы, жизнь",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="ザボロツキー『コルムヌィ』",
    name_en="Zabolotsky's Columns",
    name_original="Столбцы",
    period_key="ソヴィエト中期",
    definition="ニコライ・ザボロツキー（1903-58）が1929年に発表したデビュー詩集。ペテルブルクのネップ期都市風景を、グロテスク・原始的視覚で描く実験詩集。OBERIU派の代表作で、20世紀ロシア・アヴァンギャルド詩の重要作。",
    background="OBERIU結社(1928)、ハルムス・ヴヴェジェンスキーらの実験的詩運動。",
    development="20世紀ロシア・アヴァンギャルド詩・哲学詩学の中心テクスト。",
    historical_context="新経済政策末期レニングラードの実験的文化期。",
    primary_source_url=RVB+"zabolotsky/",
    primary_source_type="Russian Virtual Library: Столбцы",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# H: Dissident & contemporary (8)
# ============================================================
add(**RUS, name_ja="ソルジェニーツィン『ガン病棟』",
    name_en="Solzhenitsyn's Cancer Ward",
    name_original="Раковый корпус",
    period_key="ソヴィエト後期・ペレストロイカ期",
    definition="ソルジェニーツィンが1963-67年に書き、1968年に国外で発表した長編小説。ウズベキスタンのガン病棟を舞台に、元政治囚オレグ・コストグロートフを中心とする多視点小説。ソ連体制の道徳的疾患の暗喩で、ソルジェニーツィン中期代表作。",
    background="ソルジェニーツィン自身のガン治療体験(1954)、ブレジネフ期の出版禁止。",
    development="20世紀ロシア反体制文学・病院小説の規範作。",
    historical_context="ブレジネフ初期ソ連の文化的締め付け。",
    primary_source_url=IARCH+"details/cancerward",
    primary_source_type="Internet Archive: Cancer Ward",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="ソルジェニーツィン『マトリョーナの家』",
    name_en="Solzhenitsyn's Matryona's Place",
    name_original="Матрёнин двор",
    period_key="ソヴィエト後期・ペレストロイカ期",
    definition="ソルジェニーツィンが1959年に書き、1963年に『新世界』誌で発表した中編。ロシア地方の老婦人マトリョーナの素朴な聖性を描く農村散文の傑作。「ロシアの土地は義人なくしては成り立たない」のテーゼで、20世紀ロシア宗教的散文の中心テクスト。",
    background="ソルジェニーツィン1956年からのロシア地方教師生活、ロシア聖人伝伝統の継承。",
    development="20世紀ロシア農村散文（ラスプーチン・ベローフ）の祖型。",
    historical_context="フルシチョフ「雪解け」期の地方文学開花。",
    primary_source_url=LIB_RU+"solzhenicyn/matrenin_dvor/index.html",
    primary_source_type="ilibrary.ru: Матрёнин двор",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="シニャフスキー『プーシキンとの散歩』",
    name_en="Sinyavsky's Strolls with Pushkin",
    name_original="Прогулки с Пушкиным",
    period_key="ソヴィエト後期・ペレストロイカ期",
    definition="アンドレイ・シニャフスキー（筆名アブラム・テルツ、1925-97）が労働収容所で書き、1975年パリで発表した文学批評・エッセイ集。プーシキンを「軽さ」「演技性」の詩人として再解釈し、ロシア知識人の偶像破壊と評された。亡命知識人文学批評の代表作。",
    background="シニャフスキー裁判(1965)・収容所体験(1966-71)、亡命後の批評活動。",
    development="20世紀後半ロシア亡命批評・偶像破壊的文学論の中心テクスト。",
    historical_context="ブレジネフ停滞期から亡命期にかけてのソ連知識人運動。",
    primary_source_url=WIKI_RU+"Прогулки_с_Пушкиным",
    primary_source_type="Wikipedia (ru): Прогулки с Пушкиным",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**RUS, name_ja="ビートフ『プーシキン館』",
    name_en="Bitov's Pushkin House",
    name_original="Пушкинский дом",
    period_key="ソヴィエト後期・ペレストロイカ期",
    definition="アンドレイ・ビートフ（1937-2018）が1964-71年に書き、1978年米国で発表した長編小説。レニングラード・プーシキン館研究員リョーヴァ・オドエフツェフの精神的遍歴を、ロシア古典文学への絶え間ない言及と共に描くポストモダン小説の祖型。",
    background="ブレジネフ停滞期レニングラード知識人の精神的疲弊、ビートフのメタフィクション実験。",
    development="20世紀後半ロシア・ポストモダン小説（ペレーヴィン・ソローキン）の祖型。",
    historical_context="ブレジネフ停滞期の知識人地下文学。",
    primary_source_url=WIKI_RU+"Пушкинский_дом_(роман)",
    primary_source_type="Wikipedia (ru): Пушкинский дом",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**RUS, name_ja="ペレーヴィン『チャパーエフと空虚』",
    name_en="Pelevin's Buddha's Little Finger",
    name_original="Чапаев и Пустота",
    period_key="ポスト・ソヴィエト期",
    definition="ヴィクトル・ペレーヴィン（1962-）が1996年に発表した長編小説。1919年内戦期のチャパーエフ師団と1990年代モスクワ精神病院の二重物語を、仏教的「空虚」哲学で結合。20世紀末ロシア・ポストモダン小説の代表作。",
    background="ソ連崩壊後ロシアの仏教・東洋思想ブーム、ペレーヴィン自身の禅仏教関心。",
    development="21世紀ロシア・ポストモダン小説・仏教文学の中心テクスト。",
    historical_context="エリツィン期ロシアの精神的混沌と東洋宗教ブーム。",
    primary_source_url=LIB_RU+"pelevin/chapaev_i_pustota/index.html",
    primary_source_type="ilibrary.ru: Чапаев и Пустота",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ソローキン『青脂』",
    name_en="Sorokin's Blue Lard",
    name_original="Голубое сало",
    period_key="ポスト・ソヴィエト期",
    definition="ウラジーミル・ソローキン（1955-）が1999年に発表した長編小説。クローン・ロシア古典作家(トルストイ-4等)が分泌する神秘的物質「青脂」を中心とする実験的・スキャンダル的散文。ポストソ連ロシア文学界最大の検閲・告発スキャンダルの中心作。",
    background="ソローキンの古典文学パロディ実践、1990年代後半ロシア・ポストモダン爆発期。",
    development="21世紀ロシア・ポストモダン小説・パロディ文学の頂点的中心テクスト。",
    historical_context="エリツィン期末期ロシアの文化的多元性最盛期。",
    primary_source_url=WIKI_RU+"Голубое_сало",
    primary_source_type="Wikipedia (ru): Голубое сало",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# I: Slavic — Czech/Polish (10)
# ============================================================
add(**CZE, name_ja="チャペック『ロボット (R.U.R.)』",
    name_en="Čapek's R.U.R.",
    name_original="R.U.R. (Rossumovi Univerzální Roboti)",
    period_key="チェコ近現代文学期",
    definition="カレル・チャペック（1890-1938）が1920年に発表したSF戯曲。「ロボット」(robota=賦役)の語をチェコ語から世界に広めた作品。人造労働者の反乱を通じて産業文明・人間性を問う20世紀SF文学の祖型作。",
    background="第一次大戦後のチェコスロヴァキア独立、産業化への文学的応答。",
    development="20世紀世界SF文学（アシモフ・レム）の祖型として国際的影響甚大。",
    historical_context="第一次チェコスロヴァキア共和国初期(1918-)のモダニズム文化。",
    primary_source_url=GUTEN+"ebooks/59112",
    primary_source_type="Project Gutenberg: R.U.R.",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CZE, name_ja="チャペック『山椒魚戦争』",
    name_en="Čapek's War with the Newts",
    name_original="Válka s mloky",
    period_key="チェコ近現代文学期",
    definition="チャペックが1936年に発表した諷刺SF長編小説。深海から発見された知性ある山椒魚と人類の協力・対立をモック・ドキュメンタリー形式で描く反ファシズム・反植民地主義諷刺。第二次大戦前夜の戦間期欧州危機の文学的予言。",
    background="戦間期欧州ファシズム勃興、チャペックの民主主義的人道主義。",
    development="20世紀世界SF諷刺文学の規範作、戦間期民主主義文学の頂点。",
    historical_context="ヒトラー台頭(1933)、ミュンヘン協定(1938)前のチェコスロヴァキア文化。",
    primary_source_url=WIKI_CS+"Válka_s_mloky",
    primary_source_type="Wikipedia (cs): Válka s mloky",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**CZE, name_ja="ハヴェル『力なき者の力』",
    name_en="Havel's Power of the Powerless",
    name_original="Moc bezmocných",
    period_key="チェコ近現代文学期",
    definition="ヴァーツラフ・ハヴェル（1936-2011）が1978年に発表した政治哲学エッセイ。「ポスト全体主義」社会における日常的順応の構造を分析し、「真実の生」を反体制実践の核心に据えた。20世紀後半東欧反体制思想の中心テクスト。",
    background="憲章77(1977)起草、正常化期チェコの反体制運動。",
    development="20世紀後半世界反体制思想・市民社会論の中心参照点。",
    historical_context="正常化期チェコスロヴァキア(1968-89)の地下知識人文化。",
    primary_source_url=IARCH+"details/PowerOfPowerlessHavel",
    primary_source_type="Internet Archive: Power of the Powerless",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**CZE, name_ja="ハヴェル『ガーデン・パーティー』",
    name_en="Havel's Garden Party",
    name_original="Zahradní slavnost",
    period_key="チェコ近現代文学期",
    definition="ハヴェルが1963年に発表した不条理戯曲。社会主義チェコの中産階級青年フーゴ・プルディヒが官僚機構に飲み込まれていく不条理喜劇。1960年代チェコ「不条理演劇」の代表作で、ハヴェルの戯曲家としての出発点。",
    background="プラハの春前夜(1960年代)チェコの文化的解凍、ベケット・イヨネスコ受容。",
    development="20世紀後半東欧不条理演劇の規範作。",
    historical_context="ノヴォトニー期末期チェコスロヴァキアの文化的解凍。",
    primary_source_url=WIKI_CS+"Zahradní_slavnost",
    primary_source_type="Wikipedia (cs): Zahradní slavnost",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**POL, name_ja="スウォヴァツキ『バラディナ』",
    name_en="Słowacki's Balladyna",
    name_original="Balladyna",
    period_key="ポーランド・ロマン主義および近現代期",
    definition="ユリウシュ・スウォヴァツキ（1809-49）が1834年に書き1839年に発表した5幕韻文劇。ポーランド神話的過去を舞台に、姉妹バラディナとアリーナの王位簒奪悲劇を描く。シェイクスピア『マクベス』のポーランド・ロマン派的展開で、19世紀ポーランド演劇の規範作。",
    background="11月蜂起(1830-31)失敗後の亡命、シェイクスピア史劇のロマン派的展開。",
    development="20世紀ポーランド演劇・神話的悲劇研究の中心テクスト。",
    historical_context="分割ポーランド時代の亡命ロマン派文化。",
    primary_source_url=WSRC_PL+"Balladyna",
    primary_source_type="Wikisource (pl): Balladyna",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**POL, name_ja="センキェヴィチ『クォ・ヴァディス』",
    name_en="Sienkiewicz's Quo Vadis",
    name_original="Quo Vadis",
    period_key="ポーランド・ロマン主義および近現代期",
    definition="ヘンリク・センキェヴィチ（1846-1916）が1895-96年に発表した歴史長編小説。ネロ帝期ローマ(64-68年)を舞台に、ローマ貴族ヴィニツィウスとキリスト教徒少女リギアの恋愛を描く。1905年ノーベル文学賞受賞作家の代表作で、20世紀世界キリスト教歴史小説の規範。",
    background="19世紀末ヨーロッパ歴史小説ブーム、センキェヴィチの古代史研究。",
    development="20世紀ハリウッド映画化(1951)、世界歴史小説の規範作。",
    historical_context="分割ポーランド時代後期のポーランド・ナショナリズム文化。",
    primary_source_url=GUTEN+"ebooks/2853",
    primary_source_type="Project Gutenberg: Quo Vadis",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**POL, name_ja="センキェヴィチ『火と剣をもって』",
    name_en="Sienkiewicz's With Fire and Sword",
    name_original="Ogniem i mieczem",
    period_key="ポーランド・ロマン主義および近現代期",
    definition="センキェヴィチが1884年に発表した「三部作」第一巻。17世紀ポーランド・ウクライナ・コサック戦争(フメリニツキー反乱、1648-57)を題材にした歴史長編小説。19世紀末ポーランド・ナショナリズム文学の頂点で、ポーランド国民歴史小説の規範。",
    background="19世紀末ポーランド・ナショナリズム文化、フメリニツキー反乱の歴史的記憶。",
    development="ポーランド国民歴史小説の規範、20世紀映画化(1999)で大衆文化化。",
    historical_context="分割ポーランド時代後期の民族意識高揚。",
    primary_source_url=GUTEN+"ebooks/30287",
    primary_source_type="Project Gutenberg: With Fire and Sword",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**POL, name_ja="レイモント『農民』",
    name_en="Reymont's Peasants",
    name_original="Chłopi",
    period_key="ポーランド・ロマン主義および近現代期",
    definition="ヴワディスワフ・レイモント（1867-1925）が1904-09年に発表した4巻長編小説（『秋』『冬』『春』『夏』）。ポーランド中部リプツェ村の四季を通じて農民共同体の生活を描く。1924年ノーベル文学賞受賞作で、20世紀ポーランド農村文学の頂点。",
    background="19世紀末ポーランド農村社会の変化、自然主義散文の影響。",
    development="20世紀ポーランド・ヨーロッパ農村文学の規範作。",
    historical_context="分割ポーランド時代末期の農村社会。",
    primary_source_url=WSRC_PL+"Chłopi",
    primary_source_type="Wikisource (pl): Chłopi",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**POL, name_ja="ゴンブローヴィチ『フェルディドゥルケ』",
    name_en="Gombrowicz's Ferdydurke",
    name_original="Ferdydurke",
    period_key="ポーランド・ロマン主義および近現代期",
    definition="ヴィトルド・ゴンブローヴィチ（1904-69）が1937年に発表した長編小説。30歳の作家ジョーゼフが小学校に再入学させられる不条理譚を通じて、社会的「形式（forma）」の暴力性を諷刺。20世紀ポーランド・モダニズム散文の頂点で、ベケット・カフカと並ぶ中欧不条理文学の傑作。",
    background="戦間期ポーランドの社会的「形式」批判、ニーチェ・カフカの影響。",
    development="20世紀世界モダニズム散文・不条理文学の中心テクスト。",
    historical_context="第二次共和国期ポーランドの文化的成熟期。",
    primary_source_url=WSRC_PL+"Ferdydurke",
    primary_source_type="Wikisource (pl): Ferdydurke",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**POL, name_ja="ミウォシュ『囚われの魂』",
    name_en="Milosz's Captive Mind",
    name_original="Zniewolony umysł",
    period_key="ポーランド・ロマン主義および近現代期",
    definition="チェスワフ・ミウォシュ（1911-2004）が1953年にパリで発表した政治哲学エッセイ。社会主義ポーランドの知識人4類型（アルファ・ベータ・ガンマ・デルタ）の精神的屈従を分析。20世紀後半東欧反体制思想の出発点で、ミウォシュ亡命の最初の主要作。",
    background="ミウォシュ自身のポーランド外交官亡命(1951)、戦後東欧知識人体験。",
    development="20世紀後半東欧反体制思想・全体主義研究の中心参照点。",
    historical_context="戦後ポーランド人民共和国成立期(1945-56)の知識人迫害。",
    primary_source_url=IARCH+"details/captivemind00milo",
    primary_source_type="Internet Archive: The Captive Mind",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# Cross-domain attachment helper
# ============================================================
def _attach_cross(concept_name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


def _attach_axes(concept_name: str, ax_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("fourth_axes", [])
            c["fourth_axes"] = existing + ax_list
            return


# Fourth-transform tags (target >= 24)
_attach_axes("カラムジン『ロシア国家史』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"単独著者による国民史の構築は、AI生成による国家ナラティブ自動生成の歴史的祖型として機能する。",
     "related_ai_phenomenon":"AI生成による国家ナラティブの自動構築"}])
_attach_axes("プーシキン『青銅の騎士』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"国家権力と個人の対立はAI監視社会における主体性問題の文学的祖型。",
     "related_ai_phenomenon":"AI監視社会における個人と国家"}])
_attach_axes("プーシキン『エヴゲーニイ・オネーギン』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"オネーギン詩節の自動詩生成可能性は、AIによる定型詩生成の文学的祖型として機能する。",
     "related_ai_phenomenon":"AIによる定型詩生成"}])
_attach_axes("プーシキン『大尉の娘』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"歴史と虚構の融合手法は、AIによる歴史シミュレーション生成の祖型として機能する。",
     "related_ai_phenomenon":"AIによる歴史シミュレーション生成"}])
_attach_axes("レールモントフ『ペチョーリンの日記』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"近代心理小説の自己分析的形式は、AIによる人格モデリングの祖型として機能する。",
     "related_ai_phenomenon":"AIによる人格・心理モデリング"}])
_attach_axes("ゴーゴリ『鼻』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"身体部位の独立した主体化はAIアバター・ポストヒューマン主体論の文学的祖型。",
     "related_ai_phenomenon":"AIアバター・ポストヒューマン主体"}])
_attach_axes("ゴーゴリ『外套』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"小役人の物質的同一化（外套=自己）は、AI環境におけるオブジェクトとしての自己の文学的祖型。",
     "related_ai_phenomenon":"AI環境におけるオブジェクト化された自己"}])
_attach_axes("ゴーゴリ『死せる魂』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"死亡者名簿の流通による経済的価値創出は、AI生成データの所有・経済化問題の文学的祖型。",
     "related_ai_phenomenon":"AI生成データの所有・経済化問題"}])
_attach_axes("チュッチェフ『沈黙』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"「言語化された思想は虚偽」のテーゼはAI生成における言語と意味の根本的断絶の哲学的祖型。",
     "related_ai_phenomenon":"AI生成における言語と意味の断絶"}])
_attach_axes("チュッチェフ自然抒情詩", [
    {"axis":"創造性","status":"rethinking",
     "rationale":"自然詩学の宇宙論的視点はAI生成における人間中心主義を超えた創造論の祖型。",
     "related_ai_phenomenon":"AI生成における脱人間中心的創造性"}])
_attach_axes("フェート抒情詩", [
    {"axis":"創造性","status":"rethinking",
     "rationale":"純粋抒情の音楽性追求はAI生成詩のリズム・音響的最適化の文学的祖型。",
     "related_ai_phenomenon":"AI生成詩の音響最適化"}])
_attach_axes("トルストイ『懺悔』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"中年期の精神的危機の自己記録はAI環境における主体的危機の文学的祖型。",
     "related_ai_phenomenon":"AI環境における主体的危機の自己記述"}])
_attach_axes("トルストイ『芸術とは何か』", [
    {"axis":"創造性","status":"rethinking",
     "rationale":"芸術=感情伝達のテーゼはAI生成芸術の感情シミュレーション問題の祖型。",
     "related_ai_phenomenon":"AI生成芸術の感情シミュレーション"}])
_attach_axes("サルトィコフ＝シチェドリン『ある町の歴史』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"擬似歴史的諷刺はAIによる歴史的偽史生成の批判的祖型として機能する。",
     "related_ai_phenomenon":"AIによる歴史的偽史生成"}])
_attach_axes("レスコフ『左利き』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"スカーズ口語形式はAI生成音声・話者シミュレーションの文学的祖型。",
     "related_ai_phenomenon":"AI生成における話者シミュレーション"}])
_attach_axes("ソログーブ『小悪魔』ペレドノフ像", [
    {"axis":"主体","status":"rethinking",
     "rationale":"幻覚に取り憑かれた主体の解体はAI生成環境における主体の幻覚的崩壊の文学的祖型。",
     "related_ai_phenomenon":"AI環境における主体の幻覚的崩壊"}])
_attach_axes("ベールイ『銀の鳩』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"知識人の民衆宗派への取り込みはAIアルゴリズムによる主体の取り込み構造の文学的祖型。",
     "related_ai_phenomenon":"AIアルゴリズムへの主体の取り込み"}])
_attach_axes("アンネンスキー『糸杉の小箱』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"印象主義詩の感覚的曖昧性はAI生成における感覚モデリングの祖型として機能する。",
     "related_ai_phenomenon":"AI生成における感覚モデリング"}])
_attach_axes("クズミーン『翼』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"非規範的セクシュアリティの文学的可視化はAI環境におけるアイデンティティ多様化の祖型。",
     "related_ai_phenomenon":"AI環境におけるアイデンティティ多様化"}])
_attach_axes("アフマートヴァ『英雄なき詩』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"世紀の集合的記憶の凝縮はAI生成における歴史的記憶の超圧縮表現の祖型。",
     "related_ai_phenomenon":"AI生成における歴史的記憶の圧縮表現"}])
_attach_axes("マンデリシュタム『ダンテについての対話』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"詩的物質性・速度・ダイナミック構造の理論はAI生成詩の構造分析の祖型として機能する。",
     "related_ai_phenomenon":"AI生成詩の構造的物質性"}])
_attach_axes("フレーブニコフ『ザンゲジ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"ザーウミ・数字言語実験はAIモデルの非自然言語生成・数学的言語の文学的祖型。",
     "related_ai_phenomenon":"AIによる非自然言語生成"}])
_attach_axes("クルチョーヌィフ『太陽への勝利』", [
    {"axis":"創造性","status":"rethinking",
     "rationale":"総合芸術・ザーウミ実験はAIマルチモーダル生成・統合的創造の文学的祖型。",
     "related_ai_phenomenon":"AIマルチモーダル統合的創造"}])
_attach_axes("バーベリ『騎兵隊』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"インテリの暴力的他者観察はAI観察データの倫理的問題の文学的祖型。",
     "related_ai_phenomenon":"AI観察データの倫理的問題"}])
_attach_axes("ピリニャーク『裸の年』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"モンタージュ的断片散文はAI生成のセグメント結合・断片化生成の文学的祖型。",
     "related_ai_phenomenon":"AI生成における断片結合"}])
_attach_axes("ザボロツキー『コルムヌィ』", [
    {"axis":"創造性","status":"rethinking",
     "rationale":"OBERIU派の原始的視覚はAI生成における脱人間的視覚の文学的祖型。",
     "related_ai_phenomenon":"AI生成における脱人間的視覚"}])
_attach_axes("シャラーモフ『コルィマ物語』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"極限環境での無感情証言はAI証言データの感情中立化問題の文学的祖型。",
     "related_ai_phenomenon":"AI証言データの感情中立化"}])
_attach_axes("ペレーヴィン『チャパーエフと空虚』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"二重物語の仏教的「空虚」哲学はAI環境における二重・並列現実の文学的祖型。",
     "related_ai_phenomenon":"AI生成における並列現実"}])
_attach_axes("ソローキン『青脂』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"クローン古典作家の生成物概念はAI生成文学・クローン著者性問題の文学的祖型。",
     "related_ai_phenomenon":"AI生成によるクローン著者性"}])
_attach_axes("チャペック『ロボット (R.U.R.)』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"「ロボット」概念創出はAI主体問題・人工労働者倫理の起源的文学的祖型。",
     "related_ai_phenomenon":"AI主体・人工労働者倫理"}])
_attach_axes("チャペック『山椒魚戦争』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"非人間知性との共存・対立はAGI時代における人間-AI関係の文学的祖型。",
     "related_ai_phenomenon":"人間-AGI共存の倫理"}])
_attach_axes("ハヴェル『力なき者の力』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"日常的順応の構造分析はAI生成環境における無意識的順応の文学的祖型。",
     "related_ai_phenomenon":"AI環境における無意識的順応"}])
_attach_axes("ゴンブローヴィチ『フェルディドゥルケ』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"社会的「形式」の暴力性分析はAIテンプレート・形式による主体形成の文学的祖型。",
     "related_ai_phenomenon":"AIテンプレートによる主体形成"}])
_attach_axes("ミウォシュ『囚われの魂』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"知識人の精神的屈従の類型化はAI環境における知識人主体の屈従類型の祖型。",
     "related_ai_phenomenon":"AI環境における知識人の屈従類型"}])


# Cross-domain links (target >= 18)
_attach_cross("カラムジン『ロシア国家史』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"歴史哲学・国民史叙述",
     "description":"カラムジン国民史叙述は19世紀ヨーロッパ歴史哲学の重要源流。"}])
_attach_cross("プーシキン『エヴゲーニイ・オネーギン』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"韻文小説・オネーギン詩節",
     "description":"オネーギン詩節は19世紀ロシア・ヨーロッパ韻文小説の規範形式。"}])
_attach_cross("プーシキン『青銅の騎士』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"ペテルブルク・テクスト",
     "description":"ペテルブルク神話の文学的祖型として20世紀ロシア・テクスト論の中心参照点。"}])
_attach_cross("プーシキン『ボリス・ゴドゥノフ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"歴史劇・国民演劇",
     "description":"シェイクスピア史劇のロシア・ロマン派的展開で、19世紀ロシア演劇の規範。"}])
_attach_cross("レールモントフ『デーモン』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"バイロン的反英雄・デーモン文学",
     "description":"バイロン詩のロシア・ロマン派的展開で、20世紀象徴主義の中心モチーフ。"}])
_attach_cross("ゴーゴリ『死せる魂』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"地方リアリズム・諷刺文学",
     "description":"19世紀ロシア地方リアリズムの祖型、ヨーロッパ諷刺文学の中心参照点。"}])
_attach_cross("ゴーゴリ『友人との往復書簡選』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"ロシア宗教思想・スラヴ派",
     "description":"19世紀ロシア宗教保守思想の文学的綱領、スラヴ派の中心テクスト。"}])
_attach_cross("チュッチェフ『沈黙』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"沈黙の哲学・言語限界論",
     "description":"沈黙論詩学はヴィトゲンシュタイン・ハイデガー言語哲学への文学的先行。"}])
_attach_cross("トルストイ『懺悔』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"宗教的告白・実存的懺悔",
     "description":"アウグスティヌス『告白』の19世紀ロシア的展開、実存哲学の重要源流。"}])
_attach_cross("トルストイ『神の国は汝らの内にあり』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"非暴力主義・キリスト教アナキズム",
     "description":"ガンジー非暴力主義・20世紀世界平和思想の中心源流。"}])
_attach_cross("トルストイ『芸術とは何か』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"芸術哲学・芸術社会学",
     "description":"19世紀末芸術哲学・芸術社会学の中心参照点、20世紀美学論の出発点。"}])
_attach_cross("サルトィコフ＝シチェドリン『ある町の歴史』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"諷刺擬似歴史・反ユートピア",
     "description":"20世紀ディストピア文学（ザミャーチン・オーウェル）の祖型。"}])
_attach_cross("レスコフ『魅せられた旅人』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"ロシア聖愚者文学・スカーズ散文",
     "description":"ロシア聖愚者類型・スカーズ散文研究の中心テクスト。"}])
_attach_cross("ソログーブ『小悪魔』ペレドノフ像", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"デカダンス散文・心理的グロテスク",
     "description":"19世紀末ロシア・ヨーロッパ・デカダンス散文研究の頂点。"}])
_attach_cross("アンネンスキー『糸杉の小箱』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"印象主義詩・象徴主義からアクメイズムへの架橋",
     "description":"19世紀末から20世紀初頭ロシア詩学転換期の中心テクスト。"}])
_attach_cross("ヴャチェスラフ・イワノフ『コル・アルデンス』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"新異教主義・ディオニュソス神秘主義",
     "description":"ニーチェ『悲劇の誕生』のロシア哲学的展開、20世紀新異教主義の中心源流。"}])
_attach_cross("メレジコフスキー『キリストと反キリスト』三部作", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"ロシア宗教ルネサンス・二神論",
     "description":"ベルジャーエフ・フロレンスキー20世紀ロシア宗教哲学の文学的源流。"}])
_attach_cross("マンデリシュタム『石』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"アクメイズム詩学・建築詩学",
     "description":"アクメイズム派の「事物の重み」「世界文化への郷愁」詩学の出発点。"}])
_attach_cross("マンデリシュタム『ダンテについての対話』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"詩的物質性・ダイナミック構造",
     "description":"20世紀ロシア・ヨーロッパ詩学（ヘイニー・ブロツキー）の中心参照テクスト。"}])
_attach_cross("グミリョフ『火の柱』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"アクメイズム冒険主義詩学",
     "description":"20世紀ロシア冒険主義詩学・遺作詩研究の中心テクスト。"}])
_attach_cross("バーベリ『騎兵隊』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"暴力詩学・短編散文革新",
     "description":"20世紀世界短編散文・戦争文学・暴力詩学研究の中心テクスト。"}])
_attach_cross("ソルジェニーツィン『収容所群島』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"全体主義研究・証言哲学",
     "description":"アーレント・リクール証言哲学・全体主義研究の中心参照テクスト。"}])
_attach_cross("シャラーモフ『コルィマ物語』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"極限環境証言・無感情記述",
     "description":"アガンベン『アウシュヴィッツの残りもの』証言哲学の中心源流。"}])
_attach_cross("ビートフ『プーシキン館』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"メタフィクション・ポストモダン小説",
     "description":"20世紀後半ロシア・ポストモダン小説（ペレーヴィン・ソローキン）の祖型。"}])
_attach_cross("ペレーヴィン『チャパーエフと空虚』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"仏教哲学・空虚論",
     "description":"20世紀末ロシア・仏教哲学・東洋思想ブームの代表的文学化。"}])
_attach_cross("ソローキン『青脂』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"パロディ・スキャンダル文学",
     "description":"21世紀ロシア・ポストモダン・パロディ文学の頂点的中心テクスト。"}])
_attach_cross("チャペック『ロボット (R.U.R.)』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"人工知能哲学・労働者倫理",
     "description":"20世紀世界AI哲学・人工労働者倫理研究の起源的源流。"},
    {"target_db":"AI-Development","link_type":"shared_concept",
     "target_entity_name":"ロボット概念の文化的起源",
     "description":"「ロボット」概念のチェコ文化的起源・AI研究史の文学的源流。"}])
_attach_cross("チャペック『山椒魚戦争』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"非人間知性・反植民地主義",
     "description":"非人間知性論・反植民地主義・反ファシズム文学研究の中心テクスト。"}])
_attach_cross("ハヴェル『力なき者の力』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"反体制思想・市民社会論",
     "description":"20世紀後半東欧反体制思想・市民社会論の中心参照テクスト。"}])
_attach_cross("センキェヴィチ『クォ・ヴァディス』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"歴史小説・キリスト教文学",
     "description":"19世紀末世界歴史小説・キリスト教文学の規範作。"}])
_attach_cross("レイモント『農民』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"農村文学・自然主義散文",
     "description":"20世紀ヨーロッパ農村文学・自然主義散文研究の中心テクスト。"}])
_attach_cross("ゴンブローヴィチ『フェルディドゥルケ』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"形式の哲学・社会的役割論",
     "description":"20世紀ヨーロッパ・モダニズム哲学・社会的役割論の中心参照点。"}])
_attach_cross("ミウォシュ『囚われの魂』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"全体主義知識人類型論",
     "description":"20世紀後半東欧反体制思想・全体主義知識人研究の中心源流。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="東欧・ロシア",
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
        print(f"[c28-w22] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c28-w22] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c28-w22] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
