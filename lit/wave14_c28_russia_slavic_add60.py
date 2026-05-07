"""LIT-DB Phase 2 Wave 14 — C28: Russian / Slavic Literature (+60).

Subfield: lit_russia_slavic (id=18).
Sources: Project Gutenberg, Wikisource (ru/cs/pl/sr/hu), Russian National Library digital,
Internet Archive Slavic. Aim >= 70% primary tier.
fourth_transform_tags >= 18; cross_domain to PT/PHIL >= 14.

Existing 80 concepts include 19c golden age core (Pushkin/Gogol/Dostoevsky/Tolstoy/Chekhov/Turgenev),
Symbolism (early), Acmeism (basic), OPOJAZ/Formalism (basic), Bakhtin core, Soviet (basic),
post-Soviet (basic), structural poetics. This wave adds 60 NEW covering:
  A: 19c expansion — Karamzin/Zhukovsky/Griboedov + late Dostoevsky/Tolstoy works (14)
  B: Silver Age — Symbolist 2nd gen + Acmeism + Futurism complete (12)
  C: Formalism extensions + Bakhtin extensions (8)
  D: Soviet expansion — Sholokhov/Bulgakov/Platonov/Olesha/Ilf-Petrov/Tsvetaeva/Khodasevich (10)
  E: Post-Soviet — Brodsky/Aksenov/Trifonov/Pelevin/Sorokin/Akunin/Tolstaya/Petrushevskaya/Ulitskaya (8)
  F: Slavic — Czech/Polish/Serbian-Croatian/Bulgarian/Hungarian (8)
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("18世紀末ロシア・センチメンタリズム期", "Russian Sentimentalism (late 18c)", 1780, 1820,
     "カラムジン・ジュコフスキー期。ロシア近代散文と抒情詩の言語的整備期。"),
    ("19世紀ロシア・ロマンチズム黎明期", "Russian Pre-Romantic", 1810, 1840,
     "グリボエードフ、デカブリスト世代から黄金時代への移行期。"),
    ("19世紀後期ロシア・リアリズム成熟期", "Late Russian Realism (mid-late 19c)", 1860, 1910,
     "ドストエフスキー・トルストイ後期の哲学的・宗教的散文成熟期。"),
    ("ロシア銀の時代", "Russian Silver Age", 1890, 1925,
     "象徴主義・アクメイズム・未来派が交錯したロシア・モダニズム黄金期。"),
    ("ロシア・フォルマリズム期", "Russian Formalism", 1915, 1935,
     "OPOJAZ・モスクワ言語学サークル中心の文学理論革命期。"),
    ("バフチン・サークル期", "Bakhtin Circle", 1920, 1975,
     "バフチン、ヴォロシノフ、メドヴェジェフのサークルによる対話論・カーニバル論成立期。"),
    ("ソヴィエト中期", "Soviet Mid Period", 1925, 1965,
     "社会主義リアリズム成立期から雪解け期にかけての公認文学と地下文学の二重構造。"),
    ("ソヴィエト後期・ペレストロイカ期", "Late Soviet & Perestroika", 1965, 1991,
     "停滞期から崩壊期にかけての都市散文・反体制文学・亡命文学の隆盛期。"),
    ("ポスト・ソヴィエト期", "Post-Soviet", 1991, 2025,
     "ソ連崩壊以後のロシア・ポストモダン、政治的アレゴリー、女性作家の台頭期。"),
    ("チェコ近現代文学期", "Czech Modern Literature", 1880, 2025,
     "ハシェク以降のチェコ語近現代文学。"),
    ("ポーランド・ロマン主義および近現代期", "Polish Romanticism & Modern", 1820, 2025,
     "ミツキェヴィチ以降のポーランド近現代文学。"),
    ("南スラヴ・バルカン文学期", "South Slavic & Balkan Literature", 1850, 2025,
     "セルビア・クロアチア・ブルガリア・ハンガリーの近現代文学。"),
]


GUTEN = "https://www.gutenberg.org/"
WIKI_RU = "https://ru.wikipedia.org/wiki/"
WIKI_CS = "https://cs.wikipedia.org/wiki/"
WIKI_PL = "https://pl.wikipedia.org/wiki/"
WIKI_SR = "https://sr.wikipedia.org/wiki/"
WIKI_HU = "https://hu.wikipedia.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WSRC_RU = "https://ru.wikisource.org/wiki/"
WSRC_CS = "https://cs.wikisource.org/wiki/"
WSRC_PL = "https://pl.wikisource.org/wiki/"
WSRC_SR = "https://sr.wikisource.org/wiki/"
WSRC_HU = "https://hu.wikisource.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
RNB = "https://nlr.ru/"
IARCH = "https://archive.org/"
LIB_RU = "https://ilibrary.ru/"
RVB = "https://rvb.ru/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


# Common kwargs by region/script
RUS = dict(subfield_code="lit_russia_slavic", region="東欧・ロシア", original_script="cyrillic")
CZE = dict(subfield_code="lit_russia_slavic", region="東欧・ロシア", original_script="roman")
POL = dict(subfield_code="lit_russia_slavic", region="東欧・ロシア", original_script="roman")
SRB = dict(subfield_code="lit_russia_slavic", region="東欧・ロシア", original_script="cyrillic")
HRV = dict(subfield_code="lit_russia_slavic", region="東欧・ロシア", original_script="roman")
BUL = dict(subfield_code="lit_russia_slavic", region="東欧・ロシア", original_script="cyrillic")
HUN = dict(subfield_code="lit_russia_slavic", region="東欧・ロシア", original_script="roman")


# ============================================================
# A: 19世紀拡張（カラムジン〜後期ドストエフスキー・トルストイ）（14）
# ============================================================
add(**RUS, name_ja="カラムジン『ロシア人旅行者の手紙』",
    name_en="Karamzin's Letters of a Russian Traveller",
    name_original="Письма русского путешественника",
    period_key="18世紀末ロシア・センチメンタリズム期",
    definition="ニコライ・カラムジン（1766-1826）が1791-92年に発表した書簡体旅行記。1789-90年の西欧旅行を素材に、ドイツ・スイス・フランス・英国の見聞を感傷主義的散文で記した。ロシア近代散文の文語規範を確立し、後のプーシキン散文の文体的基盤となった。",
    background="エカチェリーナ二世末期ロシアの西欧文化受容、フランス感傷主義（スターン・ルソー）の影響。",
    development="プーシキン散文、19世紀ロシア小説の文体的祖型となった。",
    historical_context="フランス革命直後の西欧政治情勢を直接観察した第一級史料。",
    primary_source_url=WSRC_RU+"Письма_русского_путешественника_(Карамзин)",
    primary_source_type="Wikisource (ru): Письма русского путешественника",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="カラムジン『哀れなリーザ』",
    name_en="Karamzin's Poor Liza",
    name_original="Бедная Лиза",
    period_key="18世紀末ロシア・センチメンタリズム期",
    definition="カラムジンが1792年に発表した中編小説。モスクワ近郊の農民娘リーザと貴族青年エラストの悲恋を感傷主義的散文で描き、ロシア近代散文の規範例となった。「農民もまた愛することを知る」のテーゼがロシア社会的散文の道徳的基盤を提供した。",
    background="フランス感傷主義（ルソー『新エロイーズ』）のロシア受容、農民文学の祖型化。",
    development="プーシキン『駅長』、ドストエフスキー『貧しき人々』に直接影響。",
    historical_context="エカチェリーナ二世末期ロシアの社会階層意識の変化期。",
    primary_source_url=WSRC_RU+"Бедная_Лиза_(Карамзин)",
    primary_source_type="Wikisource (ru): Бедная Лиза",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="ジュコフスキー・バラード",
    name_en="Zhukovsky's ballads",
    name_original="Баллады Жуковского",
    period_key="19世紀ロシア・ロマンチズム黎明期",
    definition="ヴァシリー・ジュコフスキー（1783-1852）の翻訳・翻案バラード群（『リュドミラ』1808、『スヴェトラーナ』1813、『森の王』1818等）。ドイツ・ロマン派（ビュルガー、ゲーテ）のバラードをロシア語抒情詩の形式に翻案し、ロシア・ロマン派詩の音律・語彙的基盤を確立した。プーシキンの直接の師。",
    background="ナポレオン戦争期ロシアの民族意識台頭、ドイツ・ロマン派の受容。",
    development="プーシキン抒情詩、19世紀ロシア・バラード詩の規範となった。",
    historical_context="アレクサンドル一世期ロシアの民族文学形成期。",
    primary_source_url=WSRC_RU+"Жуковский,_Василий_Андреевич",
    primary_source_type="Wikisource (ru): Жуковский ballads",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="グリボエードフ『知恵の悲しみ』",
    name_en="Griboedov's Woe from Wit",
    name_original="Горе от ума",
    period_key="19世紀ロシア・ロマンチズム黎明期",
    definition="アレクサンドル・グリボエードフ（1795-1829）が1823-24年に書いた韻文喜劇。モスクワ貴族社会の偽善を批判する青年チャーツキーの帰京と挫折を描く。長らく検閲で全文出版が阻まれたが、台詞の多くがロシア語日常表現として定着し、デカブリスト世代の精神を凝縮した古典となった。",
    background="アレクサンドル一世末期の自由主義・反動の対立、デカブリスト運動前夜の文化情勢。",
    development="ドストエフスキー、ゴンチャロフ、20世紀ロシア演劇の中心研究対象。",
    historical_context="1825年デカブリスト蜂起前のロシア知識人精神を凝縮した第一級史料。",
    primary_source_url=WSRC_RU+"Горе_от_ума_(Грибоедов)",
    primary_source_type="Wikisource (ru): Горе от ума",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ドストエフスキー『死の家の記録』",
    name_en="Dostoevsky's House of the Dead",
    name_original="Записки из Мёртвого дома",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="ドストエフスキーが1860-62年に発表した半自伝的小説。シベリア徒刑（1850-54）の経験をもとに、オムスク監獄の囚人共同体を描く。ロシア最初の本格的監獄文学であり、20世紀ソルジェニーツィン、シャラーモフのグラーグ文学の祖型となった。",
    background="ドストエフスキー自身のシベリア徒刑体験、19世紀ロシア司法・刑罰制度の文学化。",
    development="ソルジェニーツィン『収容所群島』、シャラーモフ『コルィマ物語』、20世紀監獄文学全体の祖型。",
    historical_context="アレクサンドル二世大改革前夜のロシア司法制度批判。",
    primary_source_url=GUTEN+"ebooks/37536",
    primary_source_type="Project Gutenberg: The House of the Dead",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ドストエフスキー『地下室の手記』地下生活者の動機",
    name_en="Dostoevsky's Underground Man motif",
    name_original="Записки из подполья — Подпольный человек",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="ドストエフスキー『地下室の手記』(1864)の主人公「地下生活者」の人物動機。合理主義（チェルヌィシェフスキー『何をなすべきか』）を否定し、「2×2=5」を意志の自由として主張する反英雄の原型。20世紀実存主義文学（カミュ『異邦人』、サルトル『嘔吐』）の祖型となった。",
    background="1860年代ロシア急進主義（ニヒリズム）への批判、合理主義倫理学の文学的解体。",
    development="サルトル、カミュ、ベケット、20世紀世界実存主義文学の最重要先行者。",
    historical_context="1860年代ロシアの社会改革論議と合理主義倫理の流行への文学的応答。",
    primary_source_url=GUTEN+"ebooks/600",
    primary_source_type="Project Gutenberg: Notes from the Underground",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"地下生活者の合理性拒絶・自己破壊的自由はAI最適化された生活への抵抗の哲学的祖型として機能する。",
         "related_ai_phenomenon":"AI最適化への非合理的抵抗の主体性"}])

add(**RUS, name_ja="ドストエフスキー『白痴』",
    name_en="Dostoevsky's The Idiot",
    name_original="Идиот",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="ドストエフスキーが1868-69年に発表した長編小説。「絶対的に善き人」ムィシキン公爵をペテルブルク社交界に置き、その悲劇的破綻を描く。キリスト教的人格と近代社会の不可能な共存というドストエフスキー神学の中核作品で、後の『カラマーゾフの兄弟』アリョーシャ像の原型。",
    background="ドストエフスキー帰国後のペテルブルク社会観察、ロシア正教神学的倫理探求。",
    development="20世紀キリスト教文学（フラナリー・オコナー、エンドー）に深い影響。",
    historical_context="アレクサンドル二世大改革期ロシアの社会的混乱と道徳的探求。",
    primary_source_url=GUTEN+"ebooks/2638",
    primary_source_type="Project Gutenberg: The Idiot",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ドストエフスキー『未成年』",
    name_en="Dostoevsky's A Raw Youth",
    name_original="Подросток",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="ドストエフスキーが1875年に発表した長編小説。私生児アルカージーの「ロスチャイルド理念」（金力による独立）と父ヴェルシーロフへの愛憎を描く。後期五大長編の中で最も実験的な一人称形式で、ロシア青年の道徳的形成（Bildung）小説の特異な変奏。",
    background="1870年代ロシアの資本主義浸透と青年世代のニヒリズム的傾向。",
    development="後の『カラマーゾフの兄弟』への構造的橋渡しとなり、ロシア成長小説の祖型。",
    historical_context="アレクサンドル二世期末期のロシア資本主義段階への移行。",
    primary_source_url=GUTEN+"ebooks/40745",
    primary_source_type="Project Gutenberg: A Raw Youth",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="ドストエフスキー『作家の日記』",
    name_en="Dostoevsky's Diary of a Writer",
    name_original="Дневник писателя",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="ドストエフスキーが1873-81年に断続的に刊行した個人雑誌。時事評論・短編小説・宗教的省察・スラヴ派的時代論を一個人で書き継いだ前例のない出版形態。「プーシキン演説」(1880)を含み、ロシア・メシアニズムとスラヴ派思想の文学的綱領となった。",
    background="ロシア・スラヴ派思想の成熟、露土戦争(1877-78)前後のロシア民族主義高揚。",
    development="20世紀ロシア宗教哲学（ベルジャーエフ、ソロヴィヨフ）への直接影響。",
    historical_context="アレクサンドル二世末期のロシア・ナショナリズム・メシアニズム高揚期。",
    primary_source_url=IARCH+"details/diaryofwriter01dost",
    primary_source_type="Internet Archive: Diary of a Writer",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="トルストイ『戦争と平和』構造",
    name_en="Tolstoy's War and Peace structure",
    name_original="Война и мир — структура",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="『戦争と平和』(1865-69)の構造的特徴。歴史叙述と家族小説の二重構造、四家族（ボルコンスキー・ロストフ・ベズーホフ・クラーギン）の交差、ナポレオン戦争を背景とする「歴史哲学エピローグ」を含む全体構成は、19世紀小説形式の限界を押し広げた。バフチンが「叙事詩的全体」と評した規範例。",
    background="クリミア戦争後ロシアの歴史哲学的省察、トルストイ自身のヤースナヤ・ポリャーナ哲学。",
    development="20世紀大河小説（プルースト、マン、ガルシア＝マルケス）の祖型。",
    historical_context="アレクサンドル二世大改革期のロシア国民意識と歴史観の再編。",
    primary_source_url=GUTEN+"ebooks/2600",
    primary_source_type="Project Gutenberg: War and Peace",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"歴史と個人の二重構造はAI生成における大規模物語のスケーリング問題の古典的祖型として機能する。",
         "related_ai_phenomenon":"AI生成における大規模物語の構造化"}])

add(**RUS, name_ja="トルストイ『アンナ・カレーニナ』",
    name_en="Tolstoy's Anna Karenina",
    name_original="Анна Каренина",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トルストイが1875-77年に発表した長編小説。ペテルブルク高級官僚夫人アンナの不倫と自死、地主リョーヴィンの哲学的探求の二重構造で19世紀ロシア社会を描いた。ナボコフがプルーストとともに「19世紀小説の頂点」と評したリアリズム小説の規範例。",
    background="アレクサンドル二世大改革期ロシアの上流社会と地方地主家庭の対比、トルストイ自身の精神的危機。",
    development="20世紀世界小説の規範例として絶えず参照され、ヘンリー・ジェイムズらに直接影響。",
    historical_context="ロシア大改革期の社会階層流動と道徳的混乱。",
    primary_source_url=GUTEN+"ebooks/1399",
    primary_source_type="Project Gutenberg: Anna Karenina",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="トルストイ『イワン・イリイチの死』",
    name_en="Tolstoy's Death of Ivan Ilyich",
    name_original="Смерть Ивана Ильича",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トルストイが1886年に発表した中編小説。ペテルブルクの判事イワン・イリイチの死病と精神的覚醒を描く。トルストイ後期の宗教的回心後の代表作で、20世紀実存哲学（ハイデガー『存在と時間』死の分析）の文学的源泉となった。",
    background="トルストイ自身の精神的危機（『懺悔』1882）後の宗教的・倫理的探求。",
    development="ハイデガー、レヴィナス、20世紀死の哲学・実存主義文学の中心参照点。",
    historical_context="アレクサンドル三世期ロシアの宗教的反動と知識人の精神的危機。",
    primary_source_url=GUTEN+"ebooks/887",
    primary_source_type="Project Gutenberg: Death of Ivan Ilyich",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"死を通じての自己覚醒というトルストイ的構図は、AI環境における有限性・身体性意識の哲学的祖型。",
         "related_ai_phenomenon":"AI環境における有限性・身体性意識"}])

add(**RUS, name_ja="トルストイ『クロイツェル・ソナタ』",
    name_en="Tolstoy's Kreutzer Sonata",
    name_original="Крейцерова соната",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トルストイが1889年に発表した中編小説。ポズドヌィシェフが妻殺害を回想する独白形式で、結婚・性・近代家族の道徳的破綻を批判する。ロシア検閲で発禁となり地下流通したが、トルストイ後期道徳論の核心作品として20世紀フェミニズム研究の参照対象となった。",
    background="トルストイ晩年の禁欲主義（ソフィア・トルストイとの婚姻危機）、近代家族制度批判。",
    development="20世紀フェミニズム文学批評、結婚論の中心参照点。",
    historical_context="アレクサンドル三世期ロシアの家族・性道徳論議。",
    primary_source_url=GUTEN+"ebooks/689",
    primary_source_type="Project Gutenberg: The Kreutzer Sonata",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="トルストイ『復活』",
    name_en="Tolstoy's Resurrection",
    name_original="Воскресение",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トルストイが1899年に発表した最後の長編小説。貴族ネフリュードフが旧愛人マスロワをシベリア送りにした責任を引き受け、彼女と司法制度・社会制度全体を批判していく構造。トルストイ後期の宗教的・社会批判の集大成で、ロシア正教会破門(1901)の直接の契機。",
    background="トルストイ晩年の宗教的・社会批判運動（ドゥホボル教徒援助等）、ロシア司法制度批判。",
    development="20世紀社会批判文学、トルストイズム運動の文学的綱領となった。",
    historical_context="ニコライ二世期初期のロシア司法・社会制度危機。",
    primary_source_url=GUTEN+"ebooks/1938",
    primary_source_type="Project Gutenberg: Resurrection",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="トルストイ『ハジ・ムラート』",
    name_en="Tolstoy's Khadji Murat",
    name_original="Хаджи-Мурат",
    period_key="19世紀後期ロシア・リアリズム成熟期",
    definition="トルストイが1896-1904年に書き、死後1912年に刊行された中編小説。19世紀コーカサス戦争のチェチェン首領ハジ・ムラートのロシア帝国への投降と死を描く。ハロルド・ブルームが「19世紀世界文学の頂点」と評し、ポストコロニアル研究の中心テクストとなった。",
    background="トルストイ自身のコーカサス従軍経験、19世紀ロシア帝国主義への晩年的批判。",
    development="20-21世紀ポストコロニアル文学批評、コーカサス文学研究の中心参照点。",
    historical_context="19世紀ロシア帝国コーカサス戦争（1817-64）の文学的反省。",
    primary_source_url=GUTEN+"ebooks/19534",
    primary_source_type="Project Gutenberg: Hadji Murad",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# B: 銀の時代（象徴主義第二世代・アクメイズム・未来派）（12）
# ============================================================
add(**RUS, name_ja="ブリューソフ『ロシア象徴主義者』詩集",
    name_en="Bryusov's Russian Symbolists anthology",
    name_original="Русские символисты",
    period_key="ロシア銀の時代",
    definition="ヴァレーリー・ブリューソフ（1873-1924）が1894-95年に編纂・出版した三冊本詩集。フランス象徴主義（ヴェルレーヌ・マラルメ）のロシア移植を綱領化し、ロシア象徴主義運動の出発点となった。ブリューソフはロシア象徴主義の「組織者」として運動の制度化を担った。",
    background="1890年代ロシアの世紀末文化、フランス象徴主義のロシア受容。",
    development="メレジコフスキー、ソロヴィヨフを介して20世紀初頭ロシア・モダニズム全体の土台となった。",
    historical_context="アレクサンドル三世末期から世紀転換期の文化的危機と再生。",
    primary_source_url=WSRC_RU+"Русские_символисты",
    primary_source_type="Wikisource (ru): Русские символисты",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="ソログーブ『小悪魔』",
    name_en="Sologub's The Petty Demon",
    name_original="Мелкий бес",
    period_key="ロシア銀の時代",
    definition="フョードル・ソログーブ（1863-1927）が1907年に発表した長編小説。地方都市の中学校教師ペレドーノフの偏執狂的妄想と没落を象徴主義的散文で描く。ロシア象徴主義散文の代表作で、グロテスクとリアリズムの融合は20世紀ナボコフ『ロリータ』、ブルガーコフに直接影響を与えた。",
    background="20世紀初頭ロシア地方都市の停滞文化、ロシア象徴主義散文の成熟期。",
    development="ナボコフ、ブルガーコフ、20世紀ロシア・グロテスク散文の祖型。",
    historical_context="日露戦争・第一次革命(1905)期のロシア社会的閉塞感。",
    primary_source_url=IARCH+"details/melkijbes00solo",
    primary_source_type="Internet Archive: Мелкий бес",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="ベールイ『ペテルブルク』詩学",
    name_en="Bely's Petersburg poetics",
    name_original="Поэтика «Петербурга»",
    period_key="ロシア銀の時代",
    definition="アンドレイ・ベールイ『ペテルブルク』(1913-14)の詩学的革新。アナパエスト的リズム散文、色彩象徴体系、知覚の脳生理学的描写、テロリスト父子の二重像構造により、ロシア象徴主義散文の頂点を示した。ナボコフが「20世紀四大小説の一」と評した。",
    background="第一次革命後ロシアの神秘主義的不安、ベールイのアントロポゾフィー（シュタイナー）受容。",
    development="ジョイス『ユリシーズ』と並ぶモダニズム散文の頂点として20世紀世界文学に影響。",
    historical_context="第一次世界大戦前夜の帝政ロシアの解体感覚。",
    primary_source_url=RVB+"belyi/01text/02prose/04peterburg.htm",
    primary_source_type="Russian Virtual Library: Петербург (Bely)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"ベールイの脳生理学的散文と色彩象徴は、AI生成における知覚の機械的構築可能性を理論化する古典的参照点。",
         "related_ai_phenomenon":"AI生成における知覚の機械的構築"}])

add(**RUS, name_ja="ブローク『十二』",
    name_en="Blok's The Twelve",
    name_original="Двенадцать",
    period_key="ロシア銀の時代",
    definition="アレクサンドル・ブローク（1880-1921）が1918年に発表した長詩。十月革命直後のペトログラードを行進する12人の赤衛兵をキリストが率いる象徴主義的・終末論的詩篇。ロシア象徴主義の革命的爆発として、20世紀ロシア政治詩学の中心作品となった。",
    background="十月革命直後のペトログラード、ブロークの神秘的革命受容。",
    development="20世紀ロシア政治詩学・象徴主義革命詩の規範例となった。",
    historical_context="十月革命直後の混沌期、内戦勃発前夜の文化情勢。",
    primary_source_url=WSRC_RU+"Двенадцать_(Блок)",
    primary_source_type="Wikisource (ru): Двенадцать",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ジナイーダ・ギッピウス詩学",
    name_en="Gippius poetics",
    name_original="Поэтика Гиппиус",
    period_key="ロシア銀の時代",
    definition="ジナイーダ・ギッピウス（1869-1945）の詩学・批評。メレジコフスキーの妻にして象徴主義サロンの中心人物。「神秘主義的形而上学」「両性具有的主体」を象徴主義詩の中核に据え、ロシア宗教哲学運動とロシア象徴主義第一世代の理論的綱領を担った。",
    background="19世紀末ロシア宗教哲学運動、メレジコフスキー＝ギッピウス・サロンの形成。",
    development="20世紀ロシア・フェミニズム文学研究の中心参照点となった。",
    historical_context="ニコライ二世期前半ロシアの宗教的探求と文学運動の交差。",
    primary_source_url=RVB+"gippius/",
    primary_source_type="Russian Virtual Library: Гиппиус",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="グミリョフ詩学",
    name_en="Gumilyov poetics",
    name_original="Поэтика Гумилёва",
    period_key="ロシア銀の時代",
    definition="ニコライ・グミリョフ（1886-1921）の詩学。「アクメイズム宣言」(1913)を執筆し、象徴主義の神秘主義に対抗して「世界の明晰な姿」「事物の重み」を詩の核心とした。アフマートヴァの最初の夫で、1921年タガンツェフ事件で銃殺。20世紀ロシア・モダニズム詩学の中心人物。",
    background="1910年代ロシア銀の時代の運動分化、象徴主義からアクメイズムへの理論的転換。",
    development="マンデリシュタム、アフマートヴァ、20世紀ロシア・アクメイズム派詩人の理論的支柱。",
    historical_context="第一次大戦前夜から内戦期にかけての帝政・革命期文化情勢。",
    primary_source_url=RVB+"gumilev/",
    primary_source_type="Russian Virtual Library: Гумилёв",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="マンデリシュタム『トリスティア』",
    name_en="Mandelstam's Tristia",
    name_original="Tristia",
    period_key="ロシア銀の時代",
    definition="オシップ・マンデリシュタム（1891-1938）が1922年に刊行した第二詩集。ペテルブルクからクリミア・グルジアへの内戦期遍歴を背景に、古代ローマ・ヘレニズム的主題と現代ロシアの危機を融合した。アクメイズムの「世界文化への郷愁」テーゼを最も純粋に体現する詩集として、20世紀ロシア詩の規範例。",
    background="内戦期マンデリシュタムの南ロシア遍歴、アクメイズム成熟期。",
    development="ブロツキー、20世紀ロシア亡命詩、マンデリシュタム再評価運動の中心テクスト。",
    historical_context="ロシア内戦期(1918-22)の文化的離散経験。",
    primary_source_url=RVB+"mandelstam/01text/01versus/01versus.htm",
    primary_source_type="Russian Virtual Library: Tristia (Mandelstam)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"マンデリシュタムの「世界文化への郷愁」と古典的言語層の重ね合わせは、AI生成テキストにおける文化記憶の機械的呼び出しと理論的に共振する。",
         "related_ai_phenomenon":"AI生成における文化記憶・古典層の呼び出し"}])

add(**RUS, name_ja="マンデリシュタム『ヴォロネジ・ノート』",
    name_en="Mandelstam's Voronezh Notebooks",
    name_original="Воронежские тетради",
    period_key="ソヴィエト中期",
    definition="マンデリシュタムが1935-37年のヴォロネジ流刑期に書き残した詩篇群。ナジェージダ・マンデリシュタムが暗記して伝承し、1960年代以降に出版された。スターリン時代の極限状況下で書かれた最後期の詩学的革新（音響・触覚的言語、生物学的隠喩）の集大成として、20世紀ロシア詩の頂点。",
    background="マンデリシュタムのスターリン批判詩(1933)とそれに伴う流刑、ナジェージダの記憶による伝承。",
    development="ブロツキー、ツェラン、20世紀世界詩におけるホロコースト・全体主義詩学の祖型。",
    historical_context="大粛清前夜のソ連の文化的恐怖、極限状況下の詩的抵抗。",
    primary_source_url=RVB+"mandelstam/01text/01versus/03versus.htm",
    primary_source_type="Russian Virtual Library: Воронежские тетради",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"全体主義的監視下で書かれた詩は、AI監視環境下の表現抵抗の哲学的祖型として機能する。",
         "related_ai_phenomenon":"AI監視環境における表現抵抗"}])

add(**RUS, name_ja="アフマートヴァ『北の悲歌』",
    name_en="Akhmatova's Northern Elegies",
    name_original="Северные элегии",
    period_key="ソヴィエト中期",
    definition="アンナ・アフマートヴァ（1889-1966）が1940-64年に断続的に書いた7篇の悲歌詩篇。ペテルブルク幼年期から戦時レニングラード・戦後迫害期までの自伝的回想を凝縮した形而上学的悲歌で、後期アフマートヴァ詩学の頂点を成す。",
    background="戦時アフマートヴァのレニングラード・タシケント疎開、戦後ジダーノフ批判(1946)後の創作復帰。",
    development="20世紀ロシア女性詩、亡命受容のアフマートヴァ復権運動の中心テクスト。",
    historical_context="第二次大戦・スターリン晩年・雪解け期のソ連文化情勢。",
    primary_source_url=RVB+"ahmatova/01text/02versus/03versus.htm",
    primary_source_type="Russian Virtual Library: Северные элегии",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="マヤコフスキー『ズボンをはいた雲』",
    name_en="Mayakovsky's A Cloud in Trousers",
    name_original="Облако в штанах",
    period_key="ロシア銀の時代",
    definition="ウラジーミル・マヤコフスキー（1893-1930）が1915年に発表した長詩。「タチヤーナを愛するなら、母は寝に行け」式の挑発的修辞、階段詩形式（лесенка）、ロシア未来派的言語実験の結晶。ロシア未来派の代表作として20世紀ロシア前衛詩の規範例となった。",
    background="第一次大戦下ロシアの未来派運動、ブルリュク・カメンスキー・フレーブニコフ・マヤコフスキー集団の形成。",
    development="ブレヒト、ネルーダ、20世紀世界政治詩・パフォーマンス詩の祖型。",
    historical_context="第一次大戦と二月・十月革命前夜の文化的爆発期。",
    primary_source_url=WSRC_RU+"Облако_в_штанах",
    primary_source_type="Wikisource (ru): Облако в штанах",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="フレーブニコフ詩学",
    name_en="Khlebnikov poetics",
    name_original="Поэтика Хлебникова",
    period_key="ロシア銀の時代",
    definition="ヴェリミール・フレーブニコフ（1885-1922）の詩学。「ザーウミ（超意味言語）」を理論化し、語根変容・新造語・歴史数学的予言詩を展開した。ロシア未来派の理論的中核で、ヤコブソンが「20世紀最大の詩人の一人」と評した。",
    background="1910年代ロシア未来派運動、フレーブニコフのスラヴ古層への言語学的探究。",
    development="ヤコブソン言語学、20世紀世界前衛詩学の中心研究対象となった。",
    historical_context="ロシア銀の時代末期から内戦期の言語実験文化。",
    primary_source_url=RVB+"hlebnikov/",
    primary_source_type="Russian Virtual Library: Хлебников",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"フレーブニコフのザーウミ・新造語生成は、AI言語モデルにおける形態素操作・語根変容の文学的祖型として機能する。",
         "related_ai_phenomenon":"AI言語モデルにおける形態素・語根操作"}])

add(**RUS, name_ja="クルチョーヌィフ詩学",
    name_en="Kruchenykh poetics",
    name_original="Поэтика Кручёных",
    period_key="ロシア銀の時代",
    definition="アレクセイ・クルチョーヌィフ（1886-1968）の詩学。「ジル・ベ・シュチュル・ウベ・シュチョー」(1913)に代表される純粋音響詩「ザーウミ」の極限的実践者。フレーブニコフと並ぶロシア未来派の理論的中核で、20世紀音響詩・サウンド・ポエトリーの祖型を成した。",
    background="1910年代モスクワ・ロシア未来派の音声詩実験。",
    development="ダダ、レトリスム、20世紀世界音響詩学の祖型となった。",
    historical_context="ロシア銀の時代の言語的爆発期と前衛美術運動の交差。",
    primary_source_url=IARCH+"details/kruchenykh-zaum",
    primary_source_type="Internet Archive: Kruchenykh zaum",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# C: フォルマリズム拡張・バフチン拡張（8）
# ============================================================
add(**RUS, name_ja="シクロフスキー『散文の理論』",
    name_en="Shklovsky's Theory of Prose",
    name_original="Теория прозы",
    period_key="ロシア・フォルマリズム期",
    definition="ヴィクトル・シクロフスキー（1893-1984）が1925年に発表した論文集。「異化（オストラネニエ）」をトリストラム・シャンディ・トルストイ・セルバンテスに適用し、文学性は形式的「装置」に存すると論じた。OPOJAZフォルマリズムの綱領的著作。",
    background="OPOJAZ（詩的言語研究会）の理論的成熟、ロシア・モダニズム前衛芸術との並行。",
    development="20世紀構造主義（ヤコブソン、トドロフ）、ナラトロジー、文学理論の祖型となった。",
    historical_context="新経済政策(NEP)期ソ連の文化的多元性期、形式主義論争前夜。",
    primary_source_url=IARCH+"details/teoriaprozy00shkl",
    primary_source_type="Internet Archive: Теория прозы",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"異化＝形式的装置の理論はAI生成テキストの「機械的装置」との関係を理論化する基盤となる。",
         "related_ai_phenomenon":"AI生成における形式的装置の自動化"}])

add(**RUS, name_ja="シクロフスキー異化のトリストラム・シャンディ適用",
    name_en="Shklovsky's ostranenie applied to Tristram Shandy",
    name_original="«Тристрам Шенди» Стерна и теория романа",
    period_key="ロシア・フォルマリズム期",
    definition="シクロフスキー論文「スターンの『トリストラム・シャンディ』と小説論」(1921)。スターンの脱線・反復・素材露出を「世界文学で最も典型的な小説」と論じ、形式的「装置の露呈」が小説の本質であるとした。フォルマリズム小説論の代表的応用例。",
    background="OPOJAZの英文学への形式分析適用、英国小説起源論の再検討。",
    development="バフチン、20世紀メタフィクション理論（カラー、マチェレイ）の祖型。",
    historical_context="1920年代初頭ソ連の文学理論的活発期。",
    primary_source_url=IARCH+"details/shklovsky-sterne",
    primary_source_type="Internet Archive: Sterne and the theory of novel",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="エイヘンバウム『レールモントフ』",
    name_en="Eikhenbaum's Lermontov",
    name_original="Лермонтов: опыт историко-литературной оценки",
    period_key="ロシア・フォルマリズム期",
    definition="ボリス・エイヘンバウム（1886-1959）が1924年に発表したレールモントフ論。フォルマリズム的「文学事実」概念を歴史小説論に適用し、レールモントフ詩・散文を「文学的環境（литературный быт）」の中で位置づけた。フォルマリズム史的研究の代表例。",
    background="OPOJAZの「内在的研究」から「文学事実」「文学的日常」概念への発展期。",
    development="後期フォルマリズム・トィニャーノフ文学進化論、20世紀社会学的文学研究に継承。",
    historical_context="1920年代ソ連文学界の制度的整備期。",
    primary_source_url=IARCH+"details/lermontov-eikhenbaum",
    primary_source_type="Internet Archive: Лермонтов (Эйхенбаум)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="エイヘンバウム『若きトルストイ』",
    name_en="Eikhenbaum's Young Tolstoy",
    name_original="Молодой Толстой",
    period_key="ロシア・フォルマリズム期",
    definition="エイヘンバウムが1922年に発表したトルストイ初期作研究。トルストイ日記・初期作の「内的独白」「微細分析」技法を形式的に分析し、フォルマリズム的トルストイ研究の規範を確立した。後年大著『トルストイ』(1928, 1931, 1960)に発展。",
    background="OPOJAZのリアリズム小説への形式分析拡張、心理リアリズム再解釈。",
    development="20世紀トルストイ研究、内的独白・自由間接話法研究の中心参照点。",
    historical_context="1920年代ソ連の古典再読運動。",
    primary_source_url=IARCH+"details/molodojtolstoj00ejkh",
    primary_source_type="Internet Archive: Молодой Толстой",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="トィニャーノフ『プーシキン』",
    name_en="Tynyanov's Pushkin",
    name_original="Пушкин (роман)",
    period_key="ロシア・フォルマリズム期",
    definition="ユーリイ・トィニャーノフ（1894-1943）が1935-43年に書いた未完歴史小説『プーシキン』。フォルマリスト理論家による文学的実践として、19世紀文学資料の徹底調査と「文学事実」概念の小説的応用を結合した。フォルマリズム理論と歴史小説の融合形式。",
    background="トィニャーノフの19世紀ロシア文学史研究と、1930年代ソ連歴史小説需要。",
    development="バーンズ、ボラーニョ、20世紀メタヒストリカル小説の祖型。",
    historical_context="スターリン体制下の歴史回顧文学需要期。",
    primary_source_url=LIB_RU+"tynyanov/pushkin/index.html",
    primary_source_type="ilibrary.ru: Тынянов Пушкин",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="OPOJAZ史",
    name_en="OPOJAZ history",
    name_original="История ОПОЯЗа",
    period_key="ロシア・フォルマリズム期",
    definition="OPOJAZ（詩的言語研究会、Общество изучения поэтического языка、1916設立）の組織史。シクロフスキー・エイヘンバウム・トィニャーノフ・ヤクビンスキー・ポリヴァーノフを中心としたペトログラード形式主義集団の活動年表（1916-30）。1930年マルクス主義批判で解体に至る制度史。",
    background="第一次大戦下ペトログラード言語学・詩学集団の形成、ロシア未来派との連携。",
    development="20世紀構造主義言語学（ヤコブソン、プラハ学派）、文学理論制度化の祖型。",
    historical_context="ロシア銀の時代末期から第一次五カ年計画期までの文学制度史。",
    primary_source_url=IARCH+"details/opoyaz-history",
    primary_source_type="Internet Archive: OPOJAZ archival materials",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="バフチン『ドストエフスキーの詩学の諸問題』",
    name_en="Bakhtin's Problems of Dostoevsky's Poetics",
    name_original="Проблемы поэтики Достоевского",
    period_key="バフチン・サークル期",
    definition="ミハイル・バフチン（1895-1975）が1929年に『ドストエフスキー創作の諸問題』として発表し、1963年に増補改訂した著作。「ポリフォニー（多声性）」「対話的小説」「無終結性」を中心概念にドストエフスキー散文を分析し、20世紀文学理論の中心著作となった。",
    background="バフチン・サークル(1920年代レニングラード)、フォルマリズムへの理論的応答。",
    development="クリステヴァ「インターテクスチャル性」、ジュリア・ジャクション、20世紀対話論全体の祖型。",
    historical_context="1920年代末ソ連の理論的多元性期から1960年代雪解け期にかけての復権。",
    primary_source_url=IARCH+"details/problemy-poetiki-dostoevskogo",
    primary_source_type="Internet Archive: Проблемы поэтики Достоевского",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ポリフォニー＝主体の複数性理論はAI生成における複数声・複数視点の機械的構築を理論化する基盤となる。",
         "related_ai_phenomenon":"AI生成における複数視点・複数声の機械的構築"}])

add(**RUS, name_ja="バフチン『ラブレーとカーニバル』",
    name_en="Bakhtin's Rabelais and Carnival",
    name_original="Творчество Франсуа Рабле и народная культура средневековья и Ренессанса",
    period_key="バフチン・サークル期",
    definition="バフチンが1940年に博士論文として完成し、1965年に出版した著作。フランソワ・ラブレー『ガルガンチュアとパンタグリュエル』を中世・ルネサンス民衆文化の「カーニバル的笑い」「グロテスク・リアリズム」「身体下部」の伝統で読み解き、20世紀文化理論の中心テクストとなった。",
    background="バフチンの20-30年代カザフ流刑期執筆、中世・ルネサンス民衆文化研究。",
    development="ル・ロワ・ラデュリ、ギンズブルク、20世紀文化人類学・新歴史主義の中心参照点。",
    historical_context="スターリン体制下の隠れた知的抵抗、1960年代復権による国際的影響。",
    primary_source_url=IARCH+"details/rable-bakhtin",
    primary_source_type="Internet Archive: Рабле (Бахтин)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"カーニバル的反転・身体下部の理論は、AI生成における規範転倒・パロディ生成と理論的に並行する。",
         "related_ai_phenomenon":"AI生成における規範転倒・パロディ"}])


# ============================================================
# D: ソヴィエト拡張（10）
# ============================================================
add(**RUS, name_ja="ショーロホフ『静かなドン』",
    name_en="Sholokhov's Quiet Don",
    name_original="Тихий Дон",
    period_key="ソヴィエト中期",
    definition="ミハイル・ショーロホフ（1905-84）が1928-40年に発表した四部長編小説。第一次大戦・革命・内戦期のドン・コサック共同体の崩壊を、コサック青年グレゴリー・メレホフの遍歴を通じて描く。1965年ノーベル文学賞受賞作で、ソ連公認文学最大の傑作。著者問題は依然として論争中。",
    background="ショーロホフのドン・コサック地域出身という生地条件、内戦期コサック蜂起の文学化。",
    development="20世紀世界大河小説、内戦文学の祖型として絶えず参照される。",
    historical_context="ロシア内戦(1918-22)とコサック共同体解体の歴史的記録。",
    primary_source_url=LIB_RU+"sholohov/tihiy_don/index.html",
    primary_source_type="ilibrary.ru: Тихий Дон",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ブルガーコフ『犬の心臓』",
    name_en="Bulgakov's Heart of a Dog",
    name_original="Собачье сердце",
    period_key="ソヴィエト中期",
    definition="ミハイル・ブルガーコフ（1891-1940）が1925年に書いた中編小説。教授プレオブラジェンスキーが犬に人間下垂体を移植してシャリコフを創出する寓話的SFで、ソ連「新人」イデオロギー批判として検閲され、サミズダート流通を経て1987年にようやく公式刊行された。",
    background="新経済政策(NEP)期ソ連の科学万能主義批判、ブルガーコフの医学的素養。",
    development="20世紀ソ連風刺文学・反ユートピアSFの規範例。1988年映画化で大ブーム。",
    historical_context="新経済政策末期からスターリン体制成立期の文化的緊張。",
    primary_source_url=LIB_RU+"bulgakov/sobache_serdce/index.html",
    primary_source_type="ilibrary.ru: Собачье сердце",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"人為的主体創出の寓話は、AI時代の主体生成（AIエージェント・LLMペルソナ）の哲学的祖型として機能する。",
         "related_ai_phenomenon":"AI時代の人工的主体生成"}])

add(**RUS, name_ja="プラトーノフ『土台穴』",
    name_en="Platonov's Foundation Pit",
    name_original="Котлован",
    period_key="ソヴィエト中期",
    definition="アンドレイ・プラトーノフ（1899-1951）が1929-30年に書いた中編小説。「全プロレタリア共同住宅」の土台穴を掘る労働者共同体の絶望的な作業を、独特の「ソ連的言語」（プラトーノフ語）で描く。ソ連体制下では出版不可能で1988年に初公開され、20世紀世界文学の最重要作品の一とされる。",
    background="第一次五カ年計画期の集団化・工業化の悲惨を、内部からの言語的歪みで描いた。",
    development="ブロツキー、ジェイムソン、20世紀ディストピア・全体主義文学批評の中心参照点。",
    historical_context="集団化・大粛清前夜の社会的恐怖期。",
    primary_source_url=LIB_RU+"platonov/kotlovan/index.html",
    primary_source_type="ilibrary.ru: Котлован",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"プラトーノフ語の歪んだイデオロギー言語は、AI生成における体制・教義言語の機械的再生産の文学的祖型として機能する。",
         "related_ai_phenomenon":"AI生成における体制言語の機械的再生産"}])

add(**RUS, name_ja="プラトーノフ『チェヴェングール』",
    name_en="Platonov's Chevengur",
    name_original="Чевенгур",
    period_key="ソヴィエト中期",
    definition="プラトーノフが1926-29年に書いた長編小説。ロシア南部の架空都市チェヴェングールで「即時共産主義」を樹立する一団の悲喜劇。ソ連体制下では出版不可能で1988年に初公開された。革命ユートピア理念の文学的剖析として20世紀世界文学の頂点の一とされる。",
    background="内戦末期の南ロシア、革命ユートピア実験の歴史的経験。",
    development="20世紀ユートピア文学批評・全体主義研究の中心参照点。",
    historical_context="新経済政策期から第一次五カ年計画期への移行期の革命幻想。",
    primary_source_url=LIB_RU+"platonov/chevengur/index.html",
    primary_source_type="ilibrary.ru: Чевенгур",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="オレーシャ『羨望』",
    name_en="Olesha's Envy",
    name_original="Зависть",
    period_key="ソヴィエト中期",
    definition="ユーリ・オレーシャ（1899-1960）が1927年に発表した中編小説。ソ連経済計画委員アンドレイ・バビーチェフと、彼の家に拾われた「余計な人」ニコライ・カヴァレーロフの対立を描く。新経済政策末期ソ連の旧知識人・新ソビエト人対立の文学化として、20世紀ロシア・モダニズムの代表作。",
    background="新経済政策末期ソ連の社会階層対立、オレーシャの「金細工的」散文文体。",
    development="ナボコフが激賞、20世紀ロシア・モダニズム散文研究の中心テクスト。",
    historical_context="新経済政策末期から第一次五カ年計画期への文化的過渡期。",
    primary_source_url=LIB_RU+"olesha/zavist/index.html",
    primary_source_type="ilibrary.ru: Зависть",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="イリフ・ペトロフ『十二の椅子』",
    name_en="Ilf-Petrov's The Twelve Chairs",
    name_original="Двенадцать стульев",
    period_key="ソヴィエト中期",
    definition="イリヤ・イリフとエヴゲニー・ペトロフが1928年に発表した諷刺長編小説。革命前ロシア貴族夫人の宝石を隠した椅子を、共謀詐欺師オスタープ・ベンデルが追う冒険譚。新経済政策期ソ連社会の生き生きとした諷刺画として、20世紀ロシア大衆文学最大のヒット。",
    background="新経済政策期ソ連の社会的多様性、ロシア・ピカレスク文学伝統の継承。",
    development="続編『黄金の子牛』(1931)とともに20世紀ロシア諷刺文学の規範となった。",
    historical_context="新経済政策期ソ連の文化的多元性最盛期。",
    primary_source_url=LIB_RU+"ilf_petrov/12_stulev/index.html",
    primary_source_type="ilibrary.ru: Двенадцать стульев",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="ツヴェターエワ亡命詩",
    name_en="Tsvetaeva émigré poetry",
    name_original="Эмигрантская поэзия Цветаевой",
    period_key="ソヴィエト中期",
    definition="マリーナ・ツヴェターエワ（1892-1941）の亡命期(1922-39)詩篇群。プラハ・パリでの極貧生活下に書かれた『プラハの騎士』『山の詩』『終りの詩』『鼠捕り』などの長詩は、20世紀ロシア亡命文学の頂点を成し、ロシア銀の時代詩の最終的爆発を体現した。",
    background="内戦後ツヴェターエワのプラハ・パリ亡命、ロシア亡命文化の中心地での創作。",
    development="ブロツキー、リプキンら20世紀ロシア詩人による再評価運動の中心テクスト。",
    historical_context="戦間期ロシア亡命文化（パリ・プラハ・ベルリン）の盛期。",
    primary_source_url=RVB+"tsvetaeva/",
    primary_source_type="Russian Virtual Library: Цветаева",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ホダセーヴィチ亡命詩",
    name_en="Khodasevich émigré poetry",
    name_original="Эмигрантская поэзия Ходасевича",
    period_key="ソヴィエト中期",
    definition="ヴラジスラフ・ホダセーヴィチ（1886-1939）の亡命期詩篇群。『ヨーロッパの夜』(1927)所収。ロシア銀の時代の古典主義的詩風を亡命地パリで継承し、ナボコフが「20世紀最大のロシア詩人」と称えた。亡命ロシア文学最大の批評家としても活動。",
    background="内戦後ホダセーヴィチのベルリン・パリ亡命、亡命ロシア文学の理論化。",
    development="ナボコフによる激賞、20世紀ロシア亡命文学研究の中心参照点。",
    historical_context="戦間期パリ・ロシア亡命文化の中核期。",
    primary_source_url=RVB+"hodasevich/",
    primary_source_type="Russian Virtual Library: Ходасевич",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**RUS, name_ja="ブルガーコフ『巨匠とマルガリータ』詩学",
    name_en="Bulgakov's Master and Margarita poetics",
    name_original="Поэтика «Мастера и Маргариты»",
    period_key="ソヴィエト中期",
    definition="ブルガーコフ『巨匠とマルガリータ』(1928-40執筆、1966-67初刊)の詩学的革新。1930年代モスクワに来訪する悪魔ヴォランドの物語、エルサレムでのピラトとイエスの並行小説、巨匠とマルガリータの恋愛を三層構造で結合。バフチン・カーニバル理論の文学的実例として、20世紀ロシア文学最大の傑作とされる。",
    background="スターリン期モスクワの文化的恐怖と、ブルガーコフ自身の創作禁止。",
    development="20世紀世界マジック・リアリズム（ガルシア＝マルケス、ラシュディ）への影響。",
    historical_context="大粛清期から第二次大戦勃発期にかけての地下執筆。",
    primary_source_url=LIB_RU+"bulgakov/master_i_margarita/index.html",
    primary_source_type="ilibrary.ru: Мастер и Маргарита",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**RUS, name_ja="ソルジェニーツィン『イワン・デニーソヴィチの一日』",
    name_en="Solzhenitsyn's One Day in the Life of Ivan Denisovich",
    name_original="Один день Ивана Денисовича",
    period_key="ソヴィエト中期",
    definition="アレクサンドル・ソルジェニーツィン（1918-2008）が1962年に『新世界』誌に発表した中編小説。シベリア収容所のイワン・デニーソヴィチの一日を描き、フルシチョフ「雪解け」期の最大事件として、20世紀ロシア・グラーグ文学の出発点となった。1970年ノーベル文学賞受賞の記念碑作。",
    background="フルシチョフ脱スターリン化路線(1956)に伴う収容所文学の解禁、ソルジェニーツィン自身のエカチェリンブルク監獄経験。",
    development="シャラーモフ『コルィマ物語』、グーズマン、20世紀ロシア・グラーグ文学全体の祖型。",
    historical_context="フルシチョフ「雪解け」期の文化的解禁。",
    primary_source_url=LIB_RU+"solzhenicyn/odin_den/index.html",
    primary_source_type="ilibrary.ru: Один день Ивана Денисовича",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# E: ポスト・ソヴィエト（8）
# ============================================================
add(**RUS, name_ja="ブロツキー亡命詩",
    name_en="Brodsky exile poetry",
    name_original="Эмигрантская поэзия Бродского",
    period_key="ソヴィエト後期・ペレストロイカ期",
    definition="ヨシフ・ブロツキー（1940-96）の亡命期(1972-96)詩篇群。1972年強制亡命後の米国生活を背景に、英米古典詩・ロシア銀の時代・古代ローマの三層を融合した抒情詩を展開。1987年ノーベル文学賞受賞、1991-92年米国桂冠詩人。20世紀後半ロシア亡命詩学の頂点。",
    background="ブロツキーのレニングラード裁判(1964)・流刑・強制亡命(1972)、亡命後の米国学術活動。",
    development="20世紀後半世界亡命詩学・トランスナショナル文学研究の中心参照点。",
    historical_context="ブレジネフ停滞期から冷戦末期にかけての反体制亡命知識人文化。",
    primary_source_url=RVB+"brodsky/",
    primary_source_type="Russian Virtual Library: Бродский",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ブロツキー亡命詩の言語的・地理的多層性は、AI環境におけるトランスローカル主体の文学的祖型として機能する。",
         "related_ai_phenomenon":"AI環境におけるトランスローカル主体"}])

add(**RUS, name_ja="アクショーノフ『火傷』",
    name_en="Aksenov's The Burn",
    name_original="Ожог",
    period_key="ソヴィエト後期・ペレストロイカ期",
    definition="ヴァシリー・アクショーノフ（1932-2009）が1969-75年に書いた長編小説。ソ連「シックスティーズ（六〇年代世代）」の自伝的群像をジャズ・ロック文化と結合した実験的散文。1980年米国に亡命後ソ連でも発禁となった。ソ連後期世代文学の代表作。",
    background="フルシチョフ「雪解け」世代の文化的経験、ジャズ・西洋ポピュラー音楽のソ連流入。",
    development="20世紀後半ロシア世代論文学、亡命文学研究の中心テクスト。",
    historical_context="ブレジネフ停滞期の若者文化と知識人の精神的疲弊。",
    primary_source_url=LIB_RU+"aksenov/ozhog/index.html",
    primary_source_type="ilibrary.ru: Ожог",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="トリーフォノフ都市散文",
    name_en="Trifonov urban prose",
    name_original="Городская проза Трифонова",
    period_key="ソヴィエト後期・ペレストロイカ期",
    definition="ユーリ・トリーフォノフ（1925-81）の都市散文群（『交換』1969、『その他の生活』1975、『岸辺の家』1976）。モスクワ知識人家庭の日常的・道徳的危機を、ソ連の都市的中産階級の視点から描いた。「都市散文（городская проза）」の代表作家として20世紀後半ソ連リアリズム最高峰。",
    background="ブレジネフ停滞期モスクワ知識人階級の物質的安定と道徳的危機。",
    development="ソ連後期家族小説、都市リアリズム文学の祖型となった。",
    historical_context="停滞期ソ連の都市中産階級文化。",
    primary_source_url=LIB_RU+"trifonov/",
    primary_source_type="ilibrary.ru: Трифонов",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="ペレーヴィン『ジェネレーションP』",
    name_en="Pelevin's Generation P",
    name_original="Generation «П»",
    period_key="ポスト・ソヴィエト期",
    definition="ヴィクトル・ペレーヴィン（1962-）が1999年に発表した長編小説。1990年代ロシアの広告業界を舞台に、ソ連崩壊後ロシア知識人の消費資本主義への適応・幻覚を描く。バーチャル現実・シミュラクラ理論の文学化として、20世紀末ロシア・ポストモダンの代表作。",
    background="1990年代ロシアの新興広告業・ポストソ連消費資本主義文化、ボードリヤール理論のロシア受容。",
    development="20-21世紀ロシア・ポストモダン散文の規範例となった。",
    historical_context="エリツィン期ロシアの社会的混沌と消費文化の急速な浸透。",
    primary_source_url=LIB_RU+"pelevin/generation_p/index.html",
    primary_source_type="ilibrary.ru: Generation П",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"広告言語による現実構築の文学化は、AI生成コンテンツが消費者現実を構築する現代状況と直接的に共振する。",
         "related_ai_phenomenon":"AI生成コンテンツによる消費者現実の構築"}])

add(**RUS, name_ja="ソローキン『親衛隊士の日』",
    name_en="Sorokin's Day of the Oprichnik",
    name_original="День опричника",
    period_key="ポスト・ソヴィエト期",
    definition="ウラジーミル・ソローキン（1955-）が2006年に発表した長編小説。2027年の「新中世ロシア」を、復古した親衛隊（オプリチニーナ）士の一日を通じて描く反ユートピア小説。プーチン時代ロシアの権威主義復古傾向を文学的に予言した作品として国際的に評価。",
    background="プーチン政権下ロシアのナショナリズム復古、ソローキンのスキャンダル・ポストモダン傾向。",
    development="21世紀ロシア政治アレゴリー文学、現代反ユートピアの代表作。",
    historical_context="プーチン第二期(2004-08)ロシアの権威主義的回帰。",
    primary_source_url=LIB_RU+"sorokin/den_oprichnika/index.html",
    primary_source_type="ilibrary.ru: День опричника",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"ソローキン的アレゴリー予言詩学は、AI予測モデルによる未来シナリオ生成の文学的祖型として機能する。",
         "related_ai_phenomenon":"AI予測モデルによる未来シナリオ生成"}])

add(**RUS, name_ja="アクーニン歴史推理",
    name_en="Akunin historical detective fiction",
    name_original="Исторический детектив Акунина",
    period_key="ポスト・ソヴィエト期",
    definition="グリゴリー・チハルチシヴィリ（筆名ボリス・アクーニン、1956-）のエラスト・ファンドーリン・シリーズ（1998-2018、全15巻）。19世紀末から20世紀初頭ロシアを舞台にした歴史推理小説で、20-21世紀ロシア・ジャンル文学の制度的成熟と、ロシア帝政期ノスタルジーの文化的記録。",
    background="1990年代後半ロシアのジャンル文学制度確立、アクーニン自身の翻訳家としての日本文学受容（南北戦争三島由紀夫）。",
    development="21世紀ロシア大衆文学・帝政期ノスタルジー文化の中心テクスト。",
    historical_context="エリツィン期末期からプーチン期にかけてのロシア大衆文化成熟期。",
    primary_source_url=WIKI_RU+"Акунин,_Борис",
    primary_source_type="Wikipedia (ru): Акунин",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**RUS, name_ja="タチヤナ・トルスタヤ『クィシ』",
    name_en="Tatyana Tolstaya's The Slynx",
    name_original="Кысь",
    period_key="ポスト・ソヴィエト期",
    definition="タチヤナ・トルスタヤ（1951-）が2000年に発表した長編小説。核戦争後の200年後ロシアを舞台にした反ユートピア小説で、書物文化の崩壊・政治支配・言語変容を描く。21世紀ロシア女性作家の代表作で、レフ・トルストイの曾孫であるトルスタヤの古典文学伝統への応答。",
    background="ソ連崩壊後ロシアの文化的断絶感、女性作家の地位向上。",
    development="21世紀ロシア・ディストピア文学・女性作家研究の中心テクスト。",
    historical_context="エリツィン期末からプーチン期初期にかけてのロシア知識人の文化的不安。",
    primary_source_url=LIB_RU+"tolstaya/kys/index.html",
    primary_source_type="ilibrary.ru: Кысь",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**RUS, name_ja="ペトルシェフスカヤ短編",
    name_en="Petrushevskaya short stories",
    name_original="Рассказы Петрушевской",
    period_key="ポスト・ソヴィエト期",
    definition="リュドミラ・ペトルシェフスカヤ（1938-）の短編・劇作品群。ソ連後期から現代に至るモスクワ女性の家庭・職場の日常的悲惨を、極度に圧縮された口語的散文で描く。20-21世紀ロシア女性作家の代表的存在で、グロテスク・リアリズムと恐怖譚を結合した独自のスタイルを確立。",
    background="ソ連後期都市女性の社会的実態、ペレストロイカ・崩壊期の女性作家可視化。",
    development="20-21世紀ロシア女性文学・グロテスク短編研究の中心参照点。",
    historical_context="ブレジネフ期から現代までのロシア女性の社会的経験。",
    primary_source_url=WIKI_RU+"Петрушевская,_Людмила_Стефановна",
    primary_source_type="Wikipedia (ru): Петрушевская",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**RUS, name_ja="ウリツカヤ家族小説",
    name_en="Ulitskaya family novels",
    name_original="Семейные романы Улицкой",
    period_key="ポスト・ソヴィエト期",
    definition="リュドミラ・ウリツカヤ（1943-）の家族小説群（『メデア』1996、『クコーツキイ家の人びと』2001、『ダニエル・シュタイン』2006）。20世紀ロシア・ユダヤ人家族の歴史を、女性医師・科学者・宗教者の視点から描く。21世紀ロシア女性文学の代表作家として国際的に高い評価。",
    background="ソ連崩壊後ロシア・ユダヤ人歴史の文学的回復、女性作家世代の制度的成熟。",
    development="21世紀ロシア家族小説・女性作家研究の中心テクスト。",
    historical_context="ポストソ連期ロシアのアイデンティティ再編期。",
    primary_source_url=WIKI_RU+"Улицкая,_Людмила_Евгеньевна",
    primary_source_type="Wikipedia (ru): Улицкая",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# F: スラヴ諸言語（チェコ・ポーランド・南スラヴ・ハンガリー）（8）
# ============================================================
add(**CZE, name_ja="ハシェク『勇敢な兵士シュヴェイク』",
    name_en="Hašek's The Good Soldier Švejk",
    name_original="Osudy dobrého vojáka Švejka za světové války",
    period_key="チェコ近現代文学期",
    definition="ヤロスラフ・ハシェク（1883-1923）が1921-23年に発表した未完長編小説。第一次大戦中のチェコ人兵士シュヴェイクが、オーストリア＝ハンガリー帝国軍の不条理を「愚直な熱狂」で受け流す諷刺小説。ブレヒト「勇敢な母」の直接的祖型で、20世紀世界諷刺文学の頂点。",
    background="第一次大戦下オーストリア＝ハンガリー帝国軍ハシェクの捕虜・脱走・赤軍参加経験。",
    development="ブレヒト、ハインリヒ・ベル、20世紀反戦・反権威文学の祖型。",
    historical_context="第一次大戦末期から第一次チェコスロヴァキア共和国初期。",
    primary_source_url=GUTEN+"ebooks/55695",
    primary_source_type="Project Gutenberg: The Good Soldier Švejk",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CZE, name_ja="フラバル『私はイギリス王に給仕した』",
    name_en="Hrabal's I Served the King of England",
    name_original="Obsluhoval jsem anglického krále",
    period_key="チェコ近現代文学期",
    definition="ボフミル・フラバル（1914-97）が1971年にサミズダート版で発表した長編小説。ボヘミア地方のホテル・ボーイ「ジテーク」が20世紀チェコ史（戦間期・ナチ占領期・社会主義期）を生き延びる物語。「パブリンスキ・テクスト」と呼ばれる口承的散文の代表作。",
    background="社会主義チェコの正常化期、フラバルの労働者階級的散文。",
    development="クンデラ、20世紀チェコ語文学研究の中心テクスト。",
    historical_context="プラハの春(1968)後の正常化期チェコの文化的逃避。",
    primary_source_url=WIKI_CS+"Obsluhoval_jsem_anglického_krále",
    primary_source_type="Wikipedia (cs): Obsluhoval jsem",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**CZE, name_ja="クンデラ『存在の耐えられない軽さ』",
    name_en="Kundera's The Unbearable Lightness of Being",
    name_original="Nesnesitelná lehkost bytí",
    period_key="チェコ近現代文学期",
    definition="ミラン・クンデラ（1929-2023）が1984年にフランス亡命中に発表した長編小説。プラハの春(1968)前後のチェコを舞台に、外科医トマーシュとテレザの愛情・浮気・亡命を、ニーチェ「永劫回帰」の哲学的省察と織り交ぜて描く。20世紀末世界文学の最重要作品の一。",
    background="クンデラのフランス亡命(1975)、東欧ポストモダンの哲学的小説の確立。",
    development="20世紀末世界小説・ヨーロッパ・ポストモダン研究の中心テクスト。",
    historical_context="ベルリン壁崩壊前夜の東欧亡命文化。",
    primary_source_url=WIKI_EN+"The_Unbearable_Lightness_of_Being",
    primary_source_type="Wikipedia: The Unbearable Lightness of Being",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**POL, name_ja="ミツキェヴィチ『パン・タデウシュ』",
    name_en="Mickiewicz's Pan Tadeusz",
    name_original="Pan Tadeusz",
    period_key="ポーランド・ロマン主義および近現代期",
    definition="アダム・ミツキェヴィチ（1798-1855）が1834年にパリ亡命中に発表した叙事詩。リトアニア地方のシュラフタ（小貴族）家庭の対立と和解を、ナポレオン軍ポーランド進撃を背景に描く。ポーランド国民叙事詩として、19世紀ポーランド・ロマン派文学の最高傑作とされる。",
    background="11月蜂起(1830-31)失敗後のポーランド亡命文化、パリにおけるポーランド・ロマン主義運動。",
    development="20世紀ポーランド国民意識の文化的支柱として、絶えず参照される。",
    historical_context="分割ポーランド時代の民族的精神的支柱。",
    primary_source_url=GUTEN+"ebooks/28240",
    primary_source_type="Project Gutenberg: Pan Tadeusz",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**POL, name_ja="シュルツ『シナモン書房』",
    name_en="Schulz's Cinnamon Shops",
    name_original="Sklepy cynamonowe",
    period_key="ポーランド・ロマン主義および近現代期",
    definition="ブルーノ・シュルツ（1892-1942）が1934年に発表した短編集。ガリツィア地方ドロホビチの小都市を、神秘主義的・幻想的散文で描く。ホロコーストでナチに殺害されたシュルツの代表作で、カフカと並ぶ中欧モダニズム散文の最重要作品。",
    background="戦間期ポーランド・ガリツィア地方ユダヤ人町の文化、シュルツの絵画的素養。",
    development="ナボコフ、ロス、20世紀世界モダニズム散文研究の中心テクスト。",
    historical_context="戦間期ガリツィア・ユダヤ人町の文化と、ホロコースト前夜の精神的不安。",
    primary_source_url=WSRC_PL+"Sklepy_cynamonowe",
    primary_source_type="Wikisource (pl): Sklepy cynamonowe",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**POL, name_ja="トカルチュク『逃亡派』",
    name_en="Tokarczuk's Flights",
    name_original="Bieguni",
    period_key="ポーランド・ロマン主義および近現代期",
    definition="オルガ・トカルチュク（1962-）が2007年に発表した長編小説。グローバル化時代の旅・身体・移動をテーマに、断片的・百科全書的散文で構成される。ポーランド「ニケ賞」受賞、英訳版がブッカー国際賞(2018)受賞。2018年トカルチュクのノーベル文学賞受賞の代表作。",
    background="ポーランドのEU加盟(2004)後のグローバル化体験、トカルチュクの心理学的素養。",
    development="21世紀世界文学のグローバル散文の代表作。",
    historical_context="ポーランドのEU統合期、グローバル化の文化的経験。",
    primary_source_url=WIKI_PL+"Bieguni_(powieść)",
    primary_source_type="Wikipedia (pl): Bieguni",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"トカルチュクの分散的・断片的主体造形は、AI環境におけるネットワーク化された主体の文学的祖型として機能する。",
         "related_ai_phenomenon":"AI環境におけるネットワーク化された主体"}])

add(**SRB, name_ja="アンドリッチ『ドリナの橋』",
    name_en="Andrić's The Bridge on the Drina",
    name_original="На Дрини ћуприја",
    period_key="南スラヴ・バルカン文学期",
    definition="イヴォ・アンドリッチ（1892-1975）が1945年に発表した長編小説。ボスニアのヴィシェグラード村を流れるドリナ川の橋を中心に、16世紀から第一次大戦までのバルカン多民族共存と紛争を400年スパンで描く。1961年ノーベル文学賞受賞作で、20世紀世界文学のバルカン代表作。",
    background="第二次大戦末期ベオグラード占領下の執筆、アンドリッチの外交官経験。",
    development="20世紀世界バルカン文学・歴史小説研究の中心参照点。",
    historical_context="第二次大戦末期から戦後ユーゴスラヴィア成立期の文化的展望。",
    primary_source_url=WSRC_SR+"На_Дрини_ћуприја",
    primary_source_type="Wikisource (sr): На Дрини ћуприја",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**HUN, name_ja="クラスナホルカイ『サタンタンゴ』",
    name_en="Krasznahorkai's Satantango",
    name_original="Sátántangó",
    period_key="南スラヴ・バルカン文学期",
    definition="ラースロー・クラスナホルカイ（1954-）が1985年に発表した長編小説。社会主義末期ハンガリー田舎の崩壊した集団農場を舞台に、住民の絶望と詐欺師イリミアーシュの来訪を、長文段落・無段落形式で描く。タル・ベーラ監督による7時間映画化(1994)で国際的に著名。2015年ブッカー国際賞、現代ハンガリー文学の代表作家。",
    background="社会主義末期ハンガリーの農村崩壊、クラスナホルカイの黙示録的散文形式。",
    development="20-21世紀ハンガリー・東欧ポストモダン文学の中心テクスト。",
    historical_context="社会主義末期から体制転換期のハンガリーの精神的崩壊。",
    primary_source_url=WIKI_HU+"Sátántangó_(regény)",
    primary_source_type="Wikipedia (hu): Sátántangó",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


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


# Additional fourth_transform tags (target >= 18)
_attach_axes("ドストエフスキー『死の家の記録』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"監獄共同体での主体経験記述は、AI監視・管理環境における自己観察記録の哲学的祖型。",
     "related_ai_phenomenon":"AI監視環境下の自己記述"}])
_attach_axes("ドストエフスキー『白痴』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"「絶対的善人」の社会的不可能性は、AI生成における理想的人格モデルの構築可能性問題と理論的に対応する。",
     "related_ai_phenomenon":"AI生成における理想的人格モデルの限界"}])
_attach_axes("トルストイ『アンナ・カレーニナ』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"二重物語の並行構造は、AI生成による複数プロットラインの並列管理の古典的祖型。",
     "related_ai_phenomenon":"AI生成における並列プロット管理"}])
_attach_axes("トルストイ『復活』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"司法制度全体への文学的批判は、AI裁定システム・予測警察への批判的審査の祖型として機能する。",
     "related_ai_phenomenon":"AI裁定システムへの批判的審査"}])
_attach_axes("ブローク『十二』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"革命的混沌の中の終末論的隊列は、AI時代の集合的・自動化されたプロセスの神秘化的記述と理論的に対応する。",
     "related_ai_phenomenon":"AI時代の自動化プロセスの神秘化"}])
_attach_axes("グミリョフ詩学", [
    {"axis":"言語","status":"rethinking",
     "rationale":"アクメイズムの「事物の重み」「世界の明晰な姿」理念は、AI生成における物質的指示性の問題と理論的に対応する。",
     "related_ai_phenomenon":"AI生成における物質的指示性"}])
_attach_axes("ショーロホフ『静かなドン』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"著者問題の長期論争は、AI生成テキストの作者性帰属問題と理論的に並行する歴史的祖型。",
     "related_ai_phenomenon":"AI生成テキストの作者性帰属問題"}])
_attach_axes("ハシェク『勇敢な兵士シュヴェイク』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"権威への愚直な従順による不条理露呈は、AI指示への過剰最適化の文学的祖型として機能する。",
     "related_ai_phenomenon":"AI指示への過剰最適化"}])
_attach_axes("クンデラ『存在の耐えられない軽さ』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"永劫回帰なき軽さ・選択不能性は、AI環境における代替可能・置換可能な選択の哲学的祖型。",
     "related_ai_phenomenon":"AI環境における代替可能な選択"}])
_attach_axes("シュルツ『シナモン書房』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"シュルツの神秘主義的散文と「現実の二度読み」は、AI生成における現実の象徴的再構築と理論的に共振する。",
     "related_ai_phenomenon":"AI生成における現実の象徴的再構築"}])
_attach_axes("アンドリッチ『ドリナの橋』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"400年スパンの長期歴史叙述は、AI生成による超長期歴史シミュレーションの文学的祖型として機能する。",
     "related_ai_phenomenon":"AI生成による超長期歴史シミュレーション"}])


# Cross-domain links (target >= 14, mainly to PT and PHIL)
_attach_cross("ドストエフスキー『地下室の手記』地下生活者の動機", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"実存主義・反合理主義",
     "description":"地下生活者の合理性拒絶はキルケゴール、サルトル、カミュ実存主義哲学の文学的祖型。"}])

_attach_cross("ドストエフスキー『白痴』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"キリスト教倫理学・キリスト論",
     "description":"ムィシキン・キリスト像はベルジャーエフ、ソロヴィヨフのロシア宗教哲学の文学的展開。"}])

_attach_cross("ドストエフスキー『作家の日記』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"スラヴ派思想・ロシア・メシアニズム",
     "description":"ドストエフスキー後期スラヴ派思想は19世紀後半ロシア宗教哲学の中心源流。"}])

_attach_cross("トルストイ『戦争と平和』構造", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"歴史哲学・自由意志論",
     "description":"トルストイ歴史哲学エピローグはヘーゲル・マルクス歴史哲学への文学的応答。"}])

_attach_cross("トルストイ『イワン・イリイチの死』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"死の哲学・実存主義",
     "description":"ハイデガー『存在と時間』の死の分析の文学的源泉。"}])

_attach_cross("マンデリシュタム『トリスティア』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"古典詩・アクメイズム詩学",
     "description":"アクメイズムの「世界文化への郷愁」は20世紀ロシア詩学の中心理論。"}])

_attach_cross("マンデリシュタム『ヴォロネジ・ノート』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"全体主義詩学・抵抗詩",
     "description":"極限状況下の詩はツェラン、ホロコースト詩学の中心研究対象。"}])

_attach_cross("シクロフスキー『散文の理論』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"形式主義詩学・ナラトロジー",
     "description":"異化理論はジュネット、トドロフのナラトロジーの直接的祖型。"}])

_attach_cross("バフチン『ドストエフスキーの詩学の諸問題』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"対話論・ポリフォニー詩学",
     "description":"ポリフォニー理論はクリステヴァ、トドロフの対話論の中心源流。"},
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"対話の哲学",
     "description":"バフチン対話論はブーバー、レヴィナス対話哲学と並ぶ20世紀対話思想の中核。"}])

_attach_cross("バフチン『ラブレーとカーニバル』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"民衆文化哲学・身体論",
     "description":"カーニバル理論は20世紀文化人類学・身体論哲学の中心参照点。"}])

_attach_cross("プラトーノフ『土台穴』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"全体主義哲学・ユートピア批判",
     "description":"プラトーノフの言語的歪みはアーレント、レフォール全体主義哲学の文学的並行物。"}])

_attach_cross("ブルガーコフ『巨匠とマルガリータ』詩学", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"マジック・リアリズム詩学",
     "description":"三層物語構造はガルシア＝マルケス、ラシュディに直接影響。"}])

_attach_cross("ソルジェニーツィン『イワン・デニーソヴィチの一日』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"全体主義倫理学・証言哲学",
     "description":"グラーグ証言文学はアーレント、リクール証言哲学の中心源流。"}])

_attach_cross("ブロツキー亡命詩", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"亡命詩学・トランスナショナル詩学",
     "description":"ブロツキー多言語詩学は20世紀後半トランスナショナル詩学研究の中心。"}])

_attach_cross("ペレーヴィン『ジェネレーションP』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"シミュラクラ哲学・ポストモダン",
     "description":"ボードリヤール、ジェイムソン、ジジェク・ポストモダン哲学のロシア的展開。"}])

_attach_cross("ハシェク『勇敢な兵士シュヴェイク』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"権威批判・愚者の哲学",
     "description":"シュヴェイクの愚直性はバフチン愚者論、エラスムス愚者論の20世紀文学的展開。"}])

_attach_cross("ミツキェヴィチ『パン・タデウシュ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"国民叙事詩・ロマン主義詩学",
     "description":"19世紀ヨーロッパ国民叙事詩研究の中心テクスト。"}])

_attach_cross("シュルツ『シナモン書房』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"幻想文学・モダニズム詩学",
     "description":"中欧モダニズム散文（カフカ、ロート）研究の中心参照点。"}])


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
        print(f"[c28-w14] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c28-w14] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c28-w14] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
