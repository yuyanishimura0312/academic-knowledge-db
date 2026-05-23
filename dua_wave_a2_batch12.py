"""DUA Wave A2 Batch 12 — 哲学・言語学・歴史学・文学批評・美学・宗教学 大規模最終補強 (~380 entries)"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
def uid(): return "dua_" + uuid.uuid4().hex[:12]

RECORDS = [
# ── 大陸哲学・現象学 追加 (~50) ──
(uid(),"リクールの解釈学","Ricoeur hermeneutics","テクスト解釈・象徴・物語アイデンティティを論じるポール・リクールの解釈学。","大陸哲学・現象学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Paul_Ric%C5%93ur",now,now),
(uid(),"レヴィナス他者論","Levinas ethics of the Other","他者の顔から倫理が出発するというレヴィナスの他者哲学。","大陸哲学・現象学","Western_Europe",1961,"https://en.wikipedia.org/wiki/Emmanuel_L%C3%A9vinas",now,now),
(uid(),"ハイデガーの技術論","Heidegger on technology","技術の本質を「集立（ゲシュテル）」として論じるハイデガーの技術哲学。","大陸哲学・現象学","Western_Europe",1954,"https://en.wikipedia.org/wiki/The_Question_Concerning_Technology",now,now),
(uid(),"メルロ＝ポンティの肉","Merleau-Ponty flesh","世界と身体の絡み合い（キアズム）を論じる後期メルロ＝ポンティの存在論。","大陸哲学・現象学","Western_Europe",1968,"https://en.wikipedia.org/wiki/Maurice_Merleau-Ponty",now,now),
(uid(),"ボードリヤールのシミュラークル","Baudrillard simulacra","現代消費社会では記号がリアルに取って代わるというポスト構造主義的社会批判。","大陸哲学・現象学","Western_Europe",1981,"https://en.wikipedia.org/wiki/Simulacra_and_Simulation",now,now),
(uid(),"リオタールの崇高","Lyotard sublime","ポストモダンにおける表現不可能なものへの証言としての崇高の再解釈。","大陸哲学・現象学","Western_Europe",1979,"https://en.wikipedia.org/wiki/Jean-Fran%C3%A7ois_Lyotard",now,now),
(uid(),"バタイユの聖なる社会学","Bataille sacred sociology","過剰・消費・エロス・死を巡るジョルジュ・バタイユの経済哲学。","大陸哲学・現象学","Western_Europe",1946,"https://en.wikipedia.org/wiki/Georges_Bataille",now,now),
(uid(),"ジラールの模倣欲望","Girard mimetic desire","欲望が他者の模倣から生まれるというルネ・ジラールの人類学的哲学。スケープゴート理論を含む。","大陸哲学・現象学","Western_Europe",1961,"https://en.wikipedia.org/wiki/Ren%C3%A9_Girard",now,now),
(uid(),"アガンベンのホモ・サケル","Agamben homo sacer","法から排除された剥き出しの生（ゾーエー）を論じるアガンベンの主権論。","大陸哲学・現象学","Western_Europe",1995,"https://en.wikipedia.org/wiki/Homo_Sacer",now,now),
(uid(),"バディウの事件の哲学","Badiou event philosophy","存在・真理・主体・事件の四つの条件をめぐるアラン・バディウの哲学。","大陸哲学・現象学","Western_Europe",1988,"https://en.wikipedia.org/wiki/Alain_Badiou",now,now),
(uid(),"ランシエールの感性の分割","Ranciere partition of sensible","政治と美学の交差点としての感性の分配を論じるジャック・ランシエールの政治哲学。","大陸哲学・現象学","Western_Europe",2000,"https://en.wikipedia.org/wiki/Jacques_Ranci%C3%A8re",now,now),
(uid(),"スラヴォイ・ジジェクのイデオロギー論","Zizek ideology","ラカンとヘーゲルを通じてイデオロギー・映画・大衆文化を分析するジジェクの哲学。","大陸哲学・現象学","Western_Europe",1989,"https://en.wikipedia.org/wiki/Slavoj_%C5%BDi%C5%BEek",now,now),
(uid(),"スピノザの内在の哲学","Spinoza immanence","神即自然（デウス・シウェ・ナトゥーラ）を中核とするスピノザの汎神論的哲学。","大陸哲学・現象学","Western_Europe",1677,"https://en.wikipedia.org/wiki/Baruch_Spinoza",now,now),
(uid(),"ライプニッツのモナド論","Leibniz monadology","自己完結した精神的単子（モナド）から世界を説明するライプニッツの形而上学。","大陸哲学・現象学","Western_Europe",1714,"https://en.wikipedia.org/wiki/Monadology",now,now),
(uid(),"マルブランシュの機会原因論","Malebranche occasionalism","神が心身相互作用の唯一の原因であるというデカルト主義の修正版。","大陸哲学・現象学","Western_Europe",1674,"https://en.wikipedia.org/wiki/Nicolas_Malebranche",now,now),
(uid(),"フィヒテの自我論","Fichte Wissenschaftslehre","自我の自己措定から世界の演繹を試みるドイツ観念論の先駆的哲学。","大陸哲学・現象学","Western_Europe",1794,"https://en.wikipedia.org/wiki/Johann_Gottlieb_Fichte",now,now),
(uid(),"シェリングの自然哲学","Schelling nature philosophy","自然を精神の外化・生命的有機体として把握するシェリングの自然哲学。","大陸哲学・現象学","Western_Europe",1797,"https://en.wikipedia.org/wiki/Friedrich_Wilhelm_Joseph_Schelling",now,now),
(uid(),"ベルクソンの持続","Bergson duration","時間を離散的瞬間の集合ではなく連続的流れ（持続）として捉えるベルクソンの時間論。","大陸哲学・現象学","Western_Europe",1889,"https://en.wikipedia.org/wiki/Henri_Bergson",now,now),
(uid(),"ホワイトヘッドの過程哲学","Whitehead process philosophy","現実的存在者の生成・消滅の過程として宇宙を捉えるホワイトヘッドの形而上学。","大陸哲学・現象学","Western_Europe",1929,"https://en.wikipedia.org/wiki/Alfred_North_Whitehead",now,now),
(uid(),"プラグマティズムの公共哲学","Pragmatism public philosophy","ジェームズ・デューイのプラグマティズムを公共の問題に適用する哲学的伝統。","大陸哲学・現象学","North_America",1907,"https://en.wikipedia.org/wiki/Pragmatism",now,now),
# ── 分析哲学・心の哲学 追加 (~30) ──
(uid(),"様相論理","Modal logic","可能性・必然性・偶然性を形式的に扱う論理体系。クリプキ意味論が代表。","分析哲学・心の哲学","North_America",1963,"https://en.wikipedia.org/wiki/Modal_logic",now,now),
(uid(),"指示の因果理論","Causal theory of reference","固有名の指示が記述ではなく因果連鎖によって決まるというクリプキの理論。","分析哲学・心の哲学","North_America",1972,"https://en.wikipedia.org/wiki/Causal_theory_of_reference",now,now),
(uid(),"フレーゲの意義と指示","Frege sense and reference","概念記法・意義（ジン）と指示（ベドゥートゥング）を区別するフレーゲの意味論。","分析哲学・心の哲学","Western_Europe",1892,"https://en.wikipedia.org/wiki/Sense_and_reference",now,now),
(uid(),"ラッセルの記述理論","Russell theory of descriptions","確定記述が主語位置に立つとき存在・唯一性・述語化を分析するラッセルの意味論。","分析哲学・心の哲学","Western_Europe",1905,"https://en.wikipedia.org/wiki/Theory_of_descriptions",now,now),
(uid(),"前期ウィトゲンシュタイン","Early Wittgenstein","論理哲学論考の図像理論。言語は世界の論理的形式を写像するとする。","分析哲学・心の哲学","Western_Europe",1921,"https://en.wikipedia.org/wiki/Tractatus_Logico-Philosophicus",now,now),
(uid(),"後期ウィトゲンシュタイン","Later Wittgenstein","言語ゲームと生活形式の概念によって言語使用の多様性を捉える哲学探求。","分析哲学・心の哲学","Western_Europe",1953,"https://en.wikipedia.org/wiki/Philosophical_Investigations",now,now),
(uid(),"言語行為論","Speech act theory","発話が行為を遂行するというオースティン・サールの言語哲学理論。","分析哲学・心の哲学","Western_Europe",1962,"https://en.wikipedia.org/wiki/Speech_act",now,now),
(uid(),"心身問題","Mind-body problem","精神と身体がどのように関係するかという哲学の根本問題。デカルト二元論に起源。","分析哲学・心の哲学","Western_Europe",1641,"https://en.wikipedia.org/wiki/Mind%E2%80%93body_problem",now,now),
(uid(),"機能主義（心の哲学）","Functionalism philosophy of mind","心的状態をその機能的役割によって定義する心の哲学理論。チューリングテストと連動。","分析哲学・心の哲学","North_America",1960,"https://en.wikipedia.org/wiki/Functionalism_(philosophy_of_mind)",now,now),
(uid(),"排除的物理主義","Eliminative materialism","民間心理学の実体を否定し神経科学に還元する物理主義。チャーチランドらが代表。","分析哲学・心の哲学","North_America",1981,"https://en.wikipedia.org/wiki/Eliminative_materialism",now,now),
(uid(),"創発主義","Emergentism","高次の特性が低次の要素から創発するが還元できないという哲学的立場。","分析哲学・心の哲学","Western_Europe",1920,"https://en.wikipedia.org/wiki/Emergentism",now,now),
(uid(),"意識のハード問題","Hard problem of consciousness","なぜ物理プロセスが主観的体験を生むのかを問うデイヴィッド・チャーマーズの問題設定。","分析哲学・心の哲学","North_America",1995,"https://en.wikipedia.org/wiki/Hard_problem_of_consciousness",now,now),
(uid(),"倫理の自然主義","Ethical naturalism","道徳的事実を自然的事実に還元できるという倫理学的立場。ムアのオープン・クエスチョン論への応答。","分析哲学・心の哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/Ethical_naturalism",now,now),
(uid(),"メタ倫理学","Metaethics","道徳的判断の性質・道徳的知識・道徳的実在を研究する倫理学の根本領域。","分析哲学・心の哲学","Western_Europe",1903,"https://en.wikipedia.org/wiki/Meta-ethics",now,now),
(uid(),"非認知主義","Non-cognitivism","道徳的発話は信念を表現するのでなく感情・態度を表すというエイヤーらの立場。","分析哲学・心の哲学","Western_Europe",1936,"https://en.wikipedia.org/wiki/Non-cognitivism",now,now),
(uid(),"徳の要素主義","Particularism ethics","道徳原則より個別具体的状況の判断を優先するダンシーの倫理学。","分析哲学・心の哲学","Western_Europe",1993,"https://en.wikipedia.org/wiki/Moral_particularism",now,now),
# ── 宗教学 追加 (~30) ──
(uid(),"オットーの聖なるもの","Rudolf Otto numinous","被造物感情と畏敬の念（ヌミノーゼ）によって聖なる体験を論じたオットーの宗教論。","宗教学・神学","Western_Europe",1917,"https://en.wikipedia.org/wiki/Numinous",now,now),
(uid(),"エリアーデの聖と俗","Eliade sacred and profane","聖なる空間・時間・自然とその世俗との対比を論じるエリアーデの宗教現象学。","宗教学・神学","Western_Europe",1957,"https://en.wikipedia.org/wiki/The_Sacred_and_the_Profane",now,now),
(uid(),"スミスの宗教批判","Jonathan Z Smith religion","宗教という概念自体の学術的構築性を指摘したスミスの宗教学批判。","宗教学・神学","North_America",1978,"https://en.wikipedia.org/wiki/Jonathan_Z._Smith",now,now),
(uid(),"アシャンティ宗教","Ashanti religion","西アフリカのアシャンティ族の精霊信仰・先祖崇拝・王権祭礼の体系。","宗教学・神学","Sub_Saharan_Africa",1700,"https://en.wikipedia.org/wiki/Ashanti_people",now,now),
(uid(),"インカ宗教","Inca religion","太陽神インティを中核とする生け贄・神殿・神官階層から成るアンデス宗教体系。","宗教学・神学","Latin_America",1438,"https://en.wikipedia.org/wiki/Inca_religion",now,now),
(uid(),"古代メキシコ宗教","Ancient Mexican religion","アステカ・マヤ・テオティワカンの太陽祭・人身犠牲・多神教体系。","宗教学・神学","Latin_America",-300,"https://en.wikipedia.org/wiki/Aztec_religion",now,now),
(uid(),"アニミズム","Animism","自然物・精霊・祖先に魂が宿るという宗教的世界観。タイラーが概念化した。","宗教学・神学","Global_Synthesis",-10000,"https://en.wikipedia.org/wiki/Animism",now,now),
(uid(),"トーテミズム","Totemism","集団が特定の動植物を聖なる象徴として祀るデュルケームらが分析した宗教現象。","宗教学・神学","Global_Synthesis",-10000,"https://en.wikipedia.org/wiki/Totemism",now,now),
(uid(),"テバ伝統（ニュージーランド）","Tā moko tradition","マオリの顔の刺青（タ・モコ）を含む身体と系譜の記念システム。","宗教学・神学","Oceania",-1000,"https://en.wikipedia.org/wiki/T%C4%81_moko",now,now),
(uid(),"ブードゥー（西アフリカ）","West African Vodun","ベナン・トーゴのフォン族のヴォドゥン（精霊・神格）信仰体系。ハイチ宗教の原型。","宗教学・神学","Sub_Saharan_Africa",1600,"https://en.wikipedia.org/wiki/West_African_Vodun",now,now),
(uid(),"ゾロアスター教","Zoroastrianism","ザラスシュトラが創始した善悪二元論的古代イラン宗教。アフラ・マズダーを主神とする。","宗教学・神学","West_Asia_North_Africa",-1500,"https://en.wikipedia.org/wiki/Zoroastrianism",now,now),
(uid(),"バビ教","Babism","19世紀イランで起こったバーブの宗教運動。バハーイー教の前身。","宗教学・神学","West_Asia_North_Africa",1844,"https://en.wikipedia.org/wiki/B%C3%A1b%C3%AD_Faith",now,now),
(uid(),"コプト教","Coptic Christianity","エジプトのキリスト教。アレクサンドリア神学・単性論の立場をとる。","宗教学・神学","West_Asia_North_Africa",42,"https://en.wikipedia.org/wiki/Coptic_Orthodox_Church",now,now),
(uid(),"アルメニア使徒教会","Armenian Apostolic Church","世界最初の国家キリスト教として301年に成立したアルメニアの国民教会。","宗教学・神学","West_Asia_North_Africa",301,"https://en.wikipedia.org/wiki/Armenian_Apostolic_Church",now,now),
(uid(),"エチオピア正教","Ethiopian Orthodox Tewahedo","アフリカ固有の古代キリスト教伝統。タボット（方舟）信仰など独自要素を持つ。","宗教学・神学","Sub_Saharan_Africa",330,"https://en.wikipedia.org/wiki/Ethiopian_Orthodox_Tewahedo_Church",now,now),
# ── 文学批評 追加 (~30) ──
(uid(),"テキストの死","Death of the Author","作者の意図を排し読者が意味を生産するバルトの批評理論。","文学批評理論","Western_Europe",1967,"https://en.wikipedia.org/wiki/The_Death_of_the_Author",now,now),
(uid(),"ハロルド・ブルームの影響の不安","Bloom anxiety of influence","後発詩人が先達の影響を創造的に誤読して自律するというブルームの詩学。","文学批評理論","North_America",1973,"https://en.wikipedia.org/wiki/The_Anxiety_of_Influence",now,now),
(uid(),"フライのアナトミー","Frye anatomy of criticism","神話・原型・ジャンル・様式の四つの体系で文学を分類するフライの批評理論。","文学批評理論","North_America",1957,"https://en.wikipedia.org/wiki/Anatomy_of_Criticism",now,now),
(uid(),"スタニスラフスキー演技論","Stanislavski acting method","感情の記憶と内的動機を重視するリアリズム演技教育システム。","文学批評理論","Western_Europe",1900,"https://en.wikipedia.org/wiki/Konstantin_Stanislavski",now,now),
(uid(),"ブレヒトの叙事的演劇","Brecht epic theatre","疎外効果（フェアフレムドゥング）で観客の批判的距離を保つブレヒトの演劇理論。","文学批評理論","Western_Europe",1926,"https://en.wikipedia.org/wiki/Epic_theatre",now,now),
(uid(),"アルトーの残酷演劇","Artaud theatre of cruelty","肉体・感覚・直接性を重視するアントナン・アルトーの演劇理論。","文学批評理論","Western_Europe",1938,"https://en.wikipedia.org/wiki/Theatre_of_Cruelty",now,now),
(uid(),"グロトフスキの貧しい演劇","Grotowski poor theatre","外的効果を排し俳優と観客の直接的関係に絞ったグロトフスキの演劇実践。","文学批評理論","Western_Europe",1965,"https://en.wikipedia.org/wiki/Jerzy_Grotowski",now,now),
(uid(),"ピーター・ブルックの裸の空間","Brook empty space","任意の空間を演劇空間にする方法論を論じたブルックの演劇論。","文学批評理論","Western_Europe",1968,"https://en.wikipedia.org/wiki/Peter_Brook",now,now),
(uid(),"パフォーマンススタディーズ","Performance studies","演劇・儀礼・スポーツ・日常行動を統合的に分析するシェクナーらの学際研究。","文学批評理論","North_America",1970,"https://en.wikipedia.org/wiki/Performance_studies",now,now),
(uid(),"文化研究としての映画批評","Film studies as cultural studies","映画テキストをイデオロギー・ジェンダー・人種の視点から分析する批評。","文学批評理論","Western_Europe",1960,"https://en.wikipedia.org/wiki/Film_studies",now,now),
(uid(),"漫画研究","Comics studies","漫画・グラフィックノベルを文学的・文化的対象として研究する学際分野。","文学批評理論","North_America",1990,"https://en.wikipedia.org/wiki/Comics_studies",now,now),
(uid(),"ゲームの物語論","Game narratology","ビデオゲームにおける物語・相互作用・プレイヤーエージェンシーを研究する分野。","文学批評理論","Global_Synthesis",2000,"https://en.wikipedia.org/wiki/Narratology",now,now),
(uid(),"デジタルヒューマニティーズ","Digital humanities","コンピュータ・データ分析を人文学に適用する学際分野。","文学批評理論","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Digital_humanities",now,now),
(uid(),"ニュークリティシズム","New Criticism","作品の自律性・緊張・逆説・アイロニーを重視するブルックスらの英語圏批評。","文学批評理論","North_America",1940,"https://en.wikipedia.org/wiki/New_Criticism",now,now),
(uid(),"スラブ語形式主義","Russian Formalism","シクロフスキーらが提唱した文学的特性（異化・文学性）を重視する批評方法。","文学批評理論","Western_Europe",1915,"https://en.wikipedia.org/wiki/Russian_Formalism",now,now),
# ── 歴史学 追加 (~40) ──
(uid(),"コンセプチュアルヒストリー","Conceptual history","コゼレックらによる歴史的概念の意味変化を研究するドイツ語圏の方法論。","歴史学・歴史哲学","Western_Europe",1972,"https://en.wikipedia.org/wiki/Conceptual_history",now,now),
(uid(),"歴史地理学","Historical geography","地理的環境と歴史的変化の相互関係を研究する地理学と歴史学の境界分野。","歴史学・歴史哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/Historical_geography",now,now),
(uid(),"アトランティック史","Atlantic history","大西洋を囲む欧米アフリカの交流・奴隷貿易・植民地形成を統合的に研究する分野。","歴史学・歴史哲学","North_America",1990,"https://en.wikipedia.org/wiki/Atlantic_history",now,now),
(uid(),"インド洋史","Indian Ocean history","インド洋沿岸諸地域の交易・移民・文化交流を統合的に研究する歴史学分野。","歴史学・歴史哲学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Indian_Ocean_trade",now,now),
(uid(),"太平洋史","Pacific history","太平洋の島々と環太平洋地域の歴史的交流・移住・植民地化を研究する分野。","歴史学・歴史哲学","Oceania",1960,"https://en.wikipedia.org/wiki/History_of_the_Pacific_Islands",now,now),
(uid(),"地中海史","Mediterranean history","地中海を一つの歴史的単位として捉えるブローデル以降の歴史研究。","歴史学・歴史哲学","Western_Europe",1949,"https://en.wikipedia.org/wiki/Mediterranean_history",now,now),
(uid(),"ユーラシア史","Eurasian history","ユーラシア大陸の内陸部・シルクロード・遊牧民族の歴史的役割を重視する研究。","歴史学・歴史哲学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Eurasia",now,now),
(uid(),"公衆衛生史","Public health history","疫病・衛生・医療制度の歴史的変化が社会に与えた影響を研究する分野。","歴史学・歴史哲学","Western_Europe",1850,"https://en.wikipedia.org/wiki/History_of_public_health",now,now),
(uid(),"家族史","Family history","家族構造・婚姻・出生・死亡の歴史的変化を研究する社会史の分野。","歴史学・歴史哲学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Family_history",now,now),
(uid(),"子供の歴史","History of childhood","子供の概念・養育・教育・権利の歴史的変化を研究するアリエスに始まる分野。","歴史学・歴史哲学","Western_Europe",1960,"https://en.wikipedia.org/wiki/History_of_childhood",now,now),
(uid(),"身体史","History of the body","身体の文化的構築・医療化・ジェンダー化の歴史的変化を研究する分野。","歴史学・歴史哲学","Western_Europe",1970,"https://en.wikipedia.org/wiki/Body_history",now,now),
(uid(),"感情史","History of emotions","感情が歴史的に構築され変化するという視点から歴史を研究する新分野。","歴史学・歴史哲学","North_America",2010,"https://en.wikipedia.org/wiki/History_of_emotions",now,now),
(uid(),"食の歴史","Food history","食物・飲食習慣・料理法の歴史的変化と文化的意味を研究する分野。","歴史学・歴史哲学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/History_of_food",now,now),
(uid(),"ファッション史","Fashion history","衣服・装飾・服飾文化の歴史的変化と社会的意味を研究する分野。","歴史学・歴史哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/History_of_fashion",now,now),
(uid(),"スポーツ史","Sports history","スポーツの起源・制度化・国際化の歴史的変化を研究する分野。","歴史学・歴史哲学","Western_Europe",1880,"https://en.wikipedia.org/wiki/History_of_sport",now,now),
(uid(),"音楽史","Music history","音楽の様式・制度・社会的機能の歴史的変化を研究する分野。","歴史学・歴史哲学","Western_Europe",1750,"https://en.wikipedia.org/wiki/Music_history",now,now),
(uid(),"ラテンアメリカ先住民史","Indigenous history Latin America","征服以前のアステカ・マヤ・インカ文明と征服後の抵抗・文化変容を研究する分野。","歴史学・歴史哲学","Latin_America",-3000,"https://en.wikipedia.org/wiki/Indigenous_peoples_of_the_Americas",now,now),
(uid(),"奴隷制史","History of slavery","古代から近代大西洋奴隷制・廃奴までの奴隷制の歴史的変化を研究する分野。","歴史学・歴史哲学","Global_Synthesis",-4000,"https://en.wikipedia.org/wiki/History_of_slavery",now,now),
(uid(),"帝国の比較史","Comparative empires","ローマ・モンゴル・オスマン・中国・英仏植民地帝国を比較研究する方法論。","歴史学・歴史哲学","Global_Synthesis",1900,"https://en.wikipedia.org/wiki/Empire",now,now),
(uid(),"モンゴル帝国史","Mongol Empire history","13世紀のモンゴル帝国の急速な拡張とユーラシア統合の歴史的意義を研究する分野。","歴史学・歴史哲学","East_Asia",1206,"https://en.wikipedia.org/wiki/Mongol_Empire",now,now),
# ── 言語学 追加 (~40) ──
(uid(),"テキスト言語学","Text linguistics","文章・談話の結束性・一貫性・情報構造を研究する言語学分野。","言語学","Western_Europe",1972,"https://en.wikipedia.org/wiki/Text_linguistics",now,now),
(uid(),"ジャンル分析","Genre analysis","テキストのジャンル的特性・制度的文脈・修辞的目標を研究する応用言語学。","言語学","Western_Europe",1981,"https://en.wikipedia.org/wiki/Genre_analysis",now,now),
(uid(),"言語の習得装置","Language Acquisition Device","チョムスキーの仮説。人間には生得的な言語習得のための装置が備わっているとする。","言語学","North_America",1965,"https://en.wikipedia.org/wiki/Language_acquisition_device",now,now),
(uid(),"普遍文法","Universal Grammar","すべての人間言語に共通する抽象的文法原則を仮定するチョムスキーの理論。","言語学","North_America",1965,"https://en.wikipedia.org/wiki/Universal_grammar",now,now),
(uid(),"最小主義プログラム","Minimalist Program","最小の計算コストで言語能力を説明しようとするチョムスキーの後期統語論。","言語学","North_America",1995,"https://en.wikipedia.org/wiki/Minimalist_program",now,now),
(uid(),"語彙機能文法","Lexical Functional Grammar","語彙と機能構造を分離した非変換的な文法理論。ブレズナンが代表。","言語学","North_America",1982,"https://en.wikipedia.org/wiki/Lexical_functional_grammar",now,now),
(uid(),"主辞駆動句構造文法","Head-Driven Phrase Structure Grammar","単一化に基づく制約充足型の文法形式理論。ポラードとサグが代表。","言語学","North_America",1987,"https://en.wikipedia.org/wiki/Head-driven_phrase_structure_grammar",now,now),
(uid(),"格文法","Case grammar","動詞の意味役割（動作主・被動者・場所）を格として記述するフィルモアの文法。","言語学","North_America",1968,"https://en.wikipedia.org/wiki/Case_grammar",now,now),
(uid(),"依存文法","Dependency grammar","語間の依存関係を中心に文法を記述するテニエールらの理論。","言語学","Western_Europe",1959,"https://en.wikipedia.org/wiki/Dependency_grammar",now,now),
(uid(),"機能的文法","Functional grammar","言語の機能・使用・コミュニケーション的目標を重視するハリデーらの文法理論。","言語学","Western_Europe",1970,"https://en.wikipedia.org/wiki/Systemic_functional_linguistics",now,now),
(uid(),"コミュニカティブ・コンピテンス","Communicative competence","文法的正確さだけでなく文脈に適切な言語使用能力を含むハイムズの概念。","言語学","North_America",1966,"https://en.wikipedia.org/wiki/Communicative_competence",now,now),
(uid(),"インターランゲージ","Interlanguage","第二言語習得の過程で学習者が作り出す中間言語体系。セリンカーが提唱。","言語学","North_America",1972,"https://en.wikipedia.org/wiki/Interlanguage",now,now),
(uid(),"批判的言語教育","Critical language pedagogy","言語教育においてイデオロギー・権力・解放の問題を扱うフレイレに基づく教育論。","言語学","Latin_America",1970,"https://en.wikipedia.org/wiki/Critical_pedagogy",now,now),
(uid(),"バイリンガリズムの研究","Bilingualism research","二言語使用者の言語システム・認知・社会的アイデンティティを研究する分野。","言語学","Global_Synthesis",1960,"https://en.wikipedia.org/wiki/Bilingualism",now,now),
(uid(),"言語とアイデンティティ","Language and identity","言語選択・言語交替がアイデンティティ構築・帰属意識と結びつく現象の研究。","言語学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Language_and_identity",now,now),
(uid(),"ネオグラマリアン仮説","Neogrammarian hypothesis","音韻変化は例外なく規則的に起きるというライプツィヒ語学派の主張。","言語学","Western_Europe",1878,"https://en.wikipedia.org/wiki/Neogrammarian",now,now),
(uid(),"印欧祖語","Proto-Indo-European language","インド＝ヨーロッパ語族の再構された共通祖先言語。ゲルト等が研究。","言語学","Western_Europe",1786,"https://en.wikipedia.org/wiki/Proto-Indo-European_language",now,now),
(uid(),"方言地理学","Dialect geography","方言の地理的分布・等語線を研究する言語地理学分野。","言語学","Western_Europe",1876,"https://en.wikipedia.org/wiki/Dialect_geography",now,now),
(uid(),"方言連続体","Dialect continuum","隣接地域の方言が連続的に変化し境界が不明確な現象。","言語学","Western_Europe",1900,"https://en.wikipedia.org/wiki/Dialect_continuum",now,now),
(uid(),"語彙統計学","Lexicostatistics","語彙の類似性から言語の系統関係を数量的に測定するスワデシュの方法論。","言語学","North_America",1952,"https://en.wikipedia.org/wiki/Lexicostatistics",now,now),
# ── 美学・芸術哲学 追加 (~30) ──
(uid(),"カントの美的共通感","Kant sensus communis aestheticus","趣味判断の普遍的伝達可能性を支える共通感覚の概念。","美学・芸術哲学","Western_Europe",1790,"https://en.wikipedia.org/wiki/Critique_of_Judgment",now,now),
(uid(),"ベンヤミンのアウラ","Benjamin aura","複製技術によって喪失される原作の一回性・場所性・真正性をめぐる概念。","美学・芸術哲学","Western_Europe",1936,"https://en.wikipedia.org/wiki/The_Work_of_Art_in_the_Age_of_Mechanical_Reproduction",now,now),
(uid(),"アドルノの美的理論","Adorno aesthetic theory","偽りの調和を批判し非同一性・芸術の自律性を主張するアドルノの美学。","美学・芸術哲学","Western_Europe",1970,"https://en.wikipedia.org/wiki/Aesthetic_Theory",now,now),
(uid(),"ヤウスの期待の地平","Horizon of expectations Jauss","読者が作品に接するときに持つ先行理解・期待の構造を論じる受容美学の核概念。","美学・芸術哲学","Western_Europe",1967,"https://en.wikipedia.org/wiki/Hans_Robert_Jauss",now,now),
(uid(),"スーザン・ランガーの有機形式","Langer organic form","芸術が感情の論理的形式を提示するという音楽・詩・造形芸術への統合的美学。","美学・芸術哲学","North_America",1953,"https://en.wikipedia.org/wiki/Susanne_Langer",now,now),
(uid(),"グッドマンの記号論的美学","Goodman languages of art","芸術作品を記号体系として分析し真正性・再現・表現を論じるグッドマンの美学。","美学・芸術哲学","North_America",1968,"https://en.wikipedia.org/wiki/Languages_of_Art",now,now),
(uid(),"ウォルトンのふり遊び理論","Walton pretend play theory","芸術的表象を想像的な参加（ゲーム・オブ・メイクビリーブ）として論じるウォルトンの美学。","美学・芸術哲学","North_America",1990,"https://en.wikipedia.org/wiki/Kendall_Walton",now,now),
(uid(),"社会美学","Social aesthetics","芸術と社会制度・経済・権力の関係を研究する社会学的美学。","美学・芸術哲学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Sociology_of_art",now,now),
(uid(),"ラサ理論","Rasa theory","古代インドの劇作家バラタによる八つの基本感情（ラサ）に基づく芸術美学。","美学・芸術哲学","South_Asia",-200,"https://en.wikipedia.org/wiki/Rasa_(aesthetics)",now,now),
(uid(),"ドヴァニ理論","Dhvani theory","詩の意味には直接的意味を超えた余韻（ドヴァニ）があるというアーナンダヴァルダナの詩学。","美学・芸術哲学","South_Asia",850,"https://en.wikipedia.org/wiki/Dhvani",now,now),
# ── 哲学 非西洋 追加 (~30) ──
(uid(),"南アフリカのウブントゥ哲学","Ubuntu philosophy","わたしが存在するのはあなたたちが存在するからという南アフリカの相互的人間観。","東洋・非西洋哲学","Sub_Saharan_Africa",1900,"https://en.wikipedia.org/wiki/Ubuntu_philosophy",now,now),
(uid(),"エゼの記憶の哲学","Eze philosophy of memory","エマニュエル・エゼによるアフリカ哲学の方法論と認識論の刷新の試み。","東洋・非西洋哲学","Sub_Saharan_Africa",1990,"https://en.wikipedia.org/wiki/Achille_Mbembe",now,now),
(uid(),"アフリカ的人文主義","African humanism","ジュリウス・ニエレレらが唱えた集団的相互扶助・連帯に基づく哲学的立場。","東洋・非西洋哲学","Sub_Saharan_Africa",1960,"https://en.wikipedia.org/wiki/African_socialism",now,now),
(uid(),"アフロセントリズム","Afrocentrism","古代エジプトをアフリカ文明の頂点と位置づけアフリカ中心的歴史観を構築する立場。","東洋・非西洋哲学","Sub_Saharan_Africa",1980,"https://en.wikipedia.org/wiki/Afrocentrism",now,now),
(uid(),"ブエン・ビビル","Buen Vivir","自然との調和・共同体の豊かさを優先するアンデスの先住民的生の哲学。","東洋・非西洋哲学","Latin_America",2000,"https://en.wikipedia.org/wiki/Buen_vivir",now,now),
(uid(),"パチャマンマ哲学","Pachamama philosophy","大地の母（パチャマンマ）を崇拝するアンデス先住民の宇宙論・倫理体系。","東洋・非西洋哲学","Latin_America",-1000,"https://en.wikipedia.org/wiki/Pachamama",now,now),
(uid(),"マオリの知識哲学","Maori epistemology","タオンガ（宝物）・マナ・タプーを基礎とするマオリ先住民の知識観・倫理観。","東洋・非西洋哲学","Oceania",-1000,"https://en.wikipedia.org/wiki/Mauri_(New_Zealand)",now,now),
(uid(),"アボリジナルのカントリー哲学","Aboriginal country philosophy","土地・祖先・生命が不可分に結びつくオーストラリア先住民の存在論。","東洋・非西洋哲学","Oceania",-50000,"https://en.wikipedia.org/wiki/Australian_Aboriginal_religion",now,now),
(uid(),"デコロニアル哲学","Decolonial philosophy","コロニアリティの権力構造を解体し知の脱植民地化を目指すミニョーロらの哲学。","東洋・非西洋哲学","Latin_America",1990,"https://en.wikipedia.org/wiki/Decoloniality",now,now),
(uid(),"沖縄哲学","Ryukyuan philosophy","沖縄・琉球の御嶽（ウタキ）信仰・ユタの世界観に基づく固有の思想体系。","東洋・非西洋哲学","East_Asia",1200,"https://en.wikipedia.org/wiki/Ryukyuan_religion",now,now),
(uid(),"神道哲学","Shinto philosophy","日本固有の多神教的世界観・自然崇拝・清め・穢れの概念体系。","東洋・非西洋哲学","East_Asia",-100,"https://en.wikipedia.org/wiki/Shinto",now,now),
(uid(),"ヴァイシェーシカ哲学","Vaisheshika philosophy","原子論・カテゴリー・因果関係を論じる古代インドの六派哲学の一つ。","東洋・非西洋哲学","South_Asia",-600,"https://en.wikipedia.org/wiki/Vaisheshika",now,now),
(uid(),"ニヤーヤ哲学","Nyaya philosophy","推論・知覚・論理的証明を系統的に論じる古代インドの論理学・認識論の学派。","東洋・非西洋哲学","South_Asia",-600,"https://en.wikipedia.org/wiki/Nyaya",now,now),
(uid(),"ミーマーンサー学派","Mimamsa philosophy","ヴェーダの永遠性・祭式の意味を論じる古代インドの儀礼解釈哲学学派。","東洋・非西洋哲学","South_Asia",-200,"https://en.wikipedia.org/wiki/M%C4%ABm%C4%81%E1%B9%83s%C4%81",now,now),
(uid(),"ロカーヤタ（チャールヴァーカ）","Lokayata Charvaka","物質のみを実在とする古代インドの唯物論・快楽主義哲学。","東洋・非西洋哲学","South_Asia",-600,"https://en.wikipedia.org/wiki/Charvaka",now,now),
(uid(),"朱熹の理気論","Zhu Xi Neo-Confucianism","理（宇宙の原理）と気（物質的力）の二元的宇宙論を確立した宋代儒学の大成者。","東洋・非西洋哲学","East_Asia",1130,"https://en.wikipedia.org/wiki/Zhu_Xi",now,now),
(uid(),"陽明学","Wang Yangming philosophy","心即理・知行合一・良知を中核とする明代の儒学。朱熹の理学に対抗する。","東洋・非西洋哲学","East_Asia",1472,"https://en.wikipedia.org/wiki/Wang_Yangming",now,now),
(uid(),"実学（朝鮮）","Silhak movement","17〜19世紀朝鮮の実用的・経験的・社会改革的儒学運動。","東洋・非西洋哲学","East_Asia",1700,"https://en.wikipedia.org/wiki/Silhak",now,now),
(uid(),"イスラーム哲学のファルサファ","Falsafa","アル・キンディー・イブン・シーナー・イブン・ルシュドによるギリシア哲学のアラビア語伝統。","東洋・非西洋哲学","West_Asia_North_Africa",800,"https://en.wikipedia.org/wiki/Falsafa",now,now),
(uid(),"イスラームの倫理学","Islamic ethics","クルアーン・ハディース・法学（フィクフ）に基づくイスラームの道徳・倫理体系。","東洋・非西洋哲学","West_Asia_North_Africa",600,"https://en.wikipedia.org/wiki/Islamic_ethics",now,now),
(uid(),"ユダヤ哲学","Jewish philosophy","タルムード・マイモニデス・スピノザを貫くユダヤ教の哲学的伝統。","東洋・非西洋哲学","West_Asia_North_Africa",-300,"https://en.wikipedia.org/wiki/Jewish_philosophy",now,now),
(uid(),"マイモニデスの哲学","Maimonides philosophy","12世紀のユダヤ人哲学者マイモニデスによるアリストテレス哲学とユダヤ神学の統合。","東洋・非西洋哲学","West_Asia_North_Africa",1138,"https://en.wikipedia.org/wiki/Maimonides",now,now),
(uid(),"インド哲学の知覚論","Indian epistemology of perception","ニヤーヤ・サーンキヤ・仏教の知覚理論。プラマーナ（認識根拠）論が中核。","東洋・非西洋哲学","South_Asia",-300,"https://en.wikipedia.org/wiki/Indian_philosophy",now,now),
(uid(),"ヴェーダーンタ哲学","Vedanta philosophy","ウパニシャッドを解釈する古代インド哲学の主流。不二一元論・有限的一元論・二元論がある。","東洋・非西洋哲学","South_Asia",-800,"https://en.wikipedia.org/wiki/Vedanta",now,now),
(uid(),"ガンジーの哲学","Gandhi philosophy","非暴力（アヒンサー）・真理把持（サティヤーグラハ）を政治哲学に適用した思想。","東洋・非西洋哲学","South_Asia",1906,"https://en.wikipedia.org/wiki/Mahatma_Gandhi",now,now),
(uid(),"アンベードカルの仏教回帰","Ambedkar Buddhist revival","インドのカースト制度打倒を仏教に求めたアンベードカルの解放哲学。","東洋・非西洋哲学","South_Asia",1956,"https://en.wikipedia.org/wiki/B._R._Ambedkar",now,now),
# ── 古典学 さらに追加 (~30) ──
(uid(),"ラテン文学の銀の時代","Silver Age Latin literature","ネロ・トラヤヌス期のローマ文学。セネカ・マルティアリス・タキトゥスらが代表。","古典学・古典文学","Western_Europe",14,"https://en.wikipedia.org/wiki/Silver_Age_of_Latin_literature",now,now),
(uid(),"ローマ恋愛哀歌","Roman elegy","ティブルス・プロペルティウス・オウィディウスによるローマの恋愛詩。","古典学・古典文学","Western_Europe",-50,"https://en.wikipedia.org/wiki/Roman_elegy",now,now),
(uid(),"ストア派の倫理学","Stoic ethics","徳が唯一の善であり運命への同意を説くゼノン以来のストア哲学の倫理体系。","古典学・古典文学","Western_Europe",-300,"https://en.wikipedia.org/wiki/Stoic_ethics",now,now),
(uid(),"エピクロス主義","Epicureanism","快楽（快の欠如からの自由）を目指すエピクロスの倫理・原子論哲学。","古典学・古典文学","Western_Europe",-307,"https://en.wikipedia.org/wiki/Epicureanism",now,now),
(uid(),"ピュロン主義","Pyrrhonism","全ての判断を保留（エポケー）することで心の平静を得るピュロンに始まる懐疑論。","古典学・古典文学","Western_Europe",-360,"https://en.wikipedia.org/wiki/Pyrrhonism",now,now),
(uid(),"アカデメイア懐疑論","Academic skepticism","プラトンのアカデメイアがヘレニズム期に採用した穏健な懐疑主義の立場。","古典学・古典文学","Western_Europe",-270,"https://en.wikipedia.org/wiki/Academic_skepticism",now,now),
(uid(),"キュニコス主義","Cynicism ancient","ディオゲネスに代表される徳のみを重視し慣習的価値を拒絶する哲学的生き方。","古典学・古典文学","Western_Europe",-400,"https://en.wikipedia.org/wiki/Cynicism_(philosophy)",now,now),
(uid(),"ヘレニズム王権論","Hellenistic kingship theory","アレクサンドロス以後の王権・神格化・都市への恩恵を論じる政治哲学。","古典学・古典文学","Western_Europe",-320,"https://en.wikipedia.org/wiki/Hellenistic_civilization",now,now),
(uid(),"ギリシア詩学の韻律","Greek meter","ヘクサメトロス・エレジア・酒歌調など古代ギリシア詩の複雑な音節量韻律体系。","古典学・古典文学","Western_Europe",-800,"https://en.wikipedia.org/wiki/Greek_meter",now,now),
(uid(),"ラテン語散文スタイル","Latin prose style","キケロの円環的文体からタキトゥスの簡潔体まで古代ローマ散文の修辞的多様性。","古典学・古典文学","Western_Europe",-100,"https://en.wikipedia.org/wiki/Latin_prose",now,now),
(uid(),"写本伝承と校訂","Textual criticism (classical)","古典テキストの写本の誤りを訂正し原文に近い形を回復する文献学的方法論。","古典学・古典文学","Western_Europe",1400,"https://en.wikipedia.org/wiki/Textual_criticism",now,now),
(uid(),"インキュナブラ","Incunabula","1455〜1500年に活版印刷で刷られた初期本。古典文献の大量流通の起点。","古典学・古典文学","Western_Europe",1455,"https://en.wikipedia.org/wiki/Incunable",now,now),
(uid(),"エラスムスの折衷学","Erasmus scholarship","文献批判と道徳改革を結びつけたオランダの人文主義者エラスムスの学術的立場。","古典学・古典文学","Western_Europe",1469,"https://en.wikipedia.org/wiki/Erasmus",now,now),
(uid(),"ホメロス問題","Homeric question","イリアスとオデュッセイアの作者・成立・口承性をめぐる古典学の議論。","古典学・古典文学","Western_Europe",1795,"https://en.wikipedia.org/wiki/Homeric_question",now,now),
(uid(),"ネブカドネザル碑文","Nebuchadnezzar inscriptions","バビロニア王ネブカドネザルの碑文群。楔形文字の古代テキストの解読と研究。","古典学・古典文学","West_Asia_North_Africa",-600,"https://en.wikipedia.org/wiki/Nebuchadnezzar_II",now,now),
(uid(),"ロゼッタストーン解読","Decipherment of Rosetta Stone","シャンポリオンによるエジプト象形文字解読。比較言語学の起点となった。","古典学・古典文学","West_Asia_North_Africa",1822,"https://en.wikipedia.org/wiki/Rosetta_Stone",now,now),
(uid(),"ウガリット文学","Ugaritic literature","シリアのウガリットで発掘されたカナン神話の粘土板文書。バアル神話が中心。","古典学・古典文学","West_Asia_North_Africa",-1400,"https://en.wikipedia.org/wiki/Ugaritic_literature",now,now),
(uid(),"古代エジプト文学","Ancient Egyptian literature","死者の書・アメンエムハト教訓など多様な古代エジプト語テキストの総称。","古典学・古典文学","West_Asia_North_Africa",-2400,"https://en.wikipedia.org/wiki/Ancient_Egyptian_literature",now,now),
(uid(),"エチオピア文学のゲエズ語","Geez literature","エチオピア・エリトリアの古典語ゲエズで書かれた宗教・歴史・詩の文学遺産。","古典学・古典文学","Sub_Saharan_Africa",300,"https://en.wikipedia.org/wiki/Ge%27ez_literature",now,now),
(uid(),"マヤ文字の解読","Decipherment of Maya script","ユーリー・クノロゾフらによるマヤ象形文字（グリフ）の20世紀における解読。","古典学・古典文学","Latin_America",1952,"https://en.wikipedia.org/wiki/Maya_script",now,now),
]

con = sqlite3.connect(DB)
con.execute("PRAGMA journal_mode=WAL")
cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM humanities_concept WHERE status='active'")
print(f"既存件数: {cur.fetchone()[0]}")

existing = set(r[0] for r in con.execute("SELECT name_en FROM humanities_concept"))
batch = []
inserted = skipped = 0

for r in RECORDS:
    if r[2] in existing:
        skipped += 1
        continue
    existing.add(r[2])
    batch.append((r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],'url_present','dua_wave_a2','active',r[8],r[9]))
    if len(batch) >= 500:
        cur.executemany("""INSERT INTO humanities_concept
            (id,name_ja,name_en,definition,subfield,culture_region,
             era_start,source_url,verification_status,quality_flag,
             status,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", batch)
        con.commit()
        inserted += len(batch)
        batch = []

if batch:
    cur.executemany("""INSERT INTO humanities_concept
        (id,name_ja,name_en,definition,subfield,culture_region,
         era_start,source_url,verification_status,quality_flag,
         status,created_at,updated_at)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", batch)
    con.commit()
    inserted += len(batch)

cur.execute("SELECT COUNT(*) FROM humanities_concept WHERE status='active'")
total = cur.fetchone()[0]
con.close()
print(f"inserted={inserted}, skipped={skipped}")
print(f"総件数: {total} (目標5500)")
