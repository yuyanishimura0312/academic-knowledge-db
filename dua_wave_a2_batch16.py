"""DUA Wave A2 Batch 16 — 残り491件到達用 新規概念大量投入 (~600 entries)"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def uid():
    return "dua_" + uuid.uuid4().hex[:12]

now = datetime.datetime.now(datetime.timezone.utc).isoformat()

records = [
    # ===== 哲学・倫理学 新規 (~80) =====
    ("スピノザ倫理学", "Spinoza's Ethics", "バルーフ・スピノザの主著『エチカ』（1677年）で展開される汎神論的倫理学体系。神即自然（Deus sive Natura）、感情の幾何学的分析、自由は必然性の認識であるという洞察が中核。", "哲学・倫理学", "Western_Europe", 1677, "https://en.wikipedia.org/wiki/Ethics_(Spinoza)"),
    ("ライプニッツの哲学", "Leibniz's Philosophy", "ゴットフリート・ライプニッツの形而上学・論理学・科学哲学。モナドロジー（単純実体の理論）、予定調和説、最善世界論、微積分の独立発見が代表的業績。", "哲学・倫理学", "Western_Europe", 1714, "https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz"),
    ("バークリーの観念論", "Berkeley's Idealism", "ジョージ・バークリーの哲学。存在することは知覚されることである（esse est percipi）という原理から物質的実体を否定し、精神と観念のみを実在とする。", "哲学・倫理学", "Western_Europe", 1710, "https://en.wikipedia.org/wiki/George_Berkeley"),
    ("ヒュームの哲学", "Hume's Philosophy", "デイヴィッド・ヒュームの経験論・懐疑論・道徳論。因果関係の習慣論、自己同一性否定、感情に基づく道徳論、宗教的奇跡批判が代表的立場。人間本性論が主著。", "哲学・倫理学", "Western_Europe", 1739, "https://en.wikipedia.org/wiki/David_Hume"),
    ("カントの道徳哲学", "Kant's Moral Philosophy", "イマヌエル・カントの実践理性批判と道徳形而上学の基礎づけ。定言命法・義務・意志の自律・人格の尊厳が中核概念。行為の道徳的価値を意志の動機（善意志）に求める。", "哲学・倫理学", "Western_Europe", 1785, "https://en.wikipedia.org/wiki/Kantian_ethics"),
    ("ヘーゲルの弁証法", "Hegel's Dialectic", "ゲオルク・ヴィルヘルム・フリードリヒ・ヘーゲルが展開した弁証法的思惟。正・反・合（テーゼ・アンチテーゼ・ジンテーゼ）の運動による絶対精神の自己展開。歴史・精神・論理の全領域を包括する体系。", "哲学・倫理学", "Western_Europe", 1807, "https://en.wikipedia.org/wiki/Dialectic"),
    ("ショーペンハウアーの哲学", "Schopenhauer's Philosophy", "アルトゥール・ショーペンハウアーの意志と表象の世界。世界の根底に盲目的な意志（Wille）を見る悲観主義哲学。仏教との親和性、芸術による意志の否定、禁欲主義的救済論が特徴。", "哲学・倫理学", "Western_Europe", 1819, "https://en.wikipedia.org/wiki/Arthur_Schopenhauer"),
    ("ニーチェの哲学", "Nietzsche's Philosophy", "フリードリヒ・ニーチェの哲学。神の死・ニヒリズム批判・力への意志・永劫回帰・超人（Übermensch）が中核概念。道徳の系譜学によるキリスト教道徳批判が代表的著作。", "哲学・倫理学", "Western_Europe", 1883, "https://en.wikipedia.org/wiki/Friedrich_Nietzsche"),
    ("マルクスの哲学", "Marx's Philosophy", "カール・マルクスの史的唯物論・疎外論・資本主義批判。土台（経済的生産関係）と上部構造（法・政治・文化）の弁証法的関係、階級闘争による歴史発展が基本テーゼ。", "哲学・倫理学", "Western_Europe", 1867, "https://en.wikipedia.org/wiki/Marxist_philosophy"),
    ("ウィトゲンシュタインの前期哲学", "Early Wittgenstein's Philosophy", "論理哲学論考（1921年）で展開された言語の写像理論。語られうることと語られえないことの区別、論理と言語の限界を論じる。意味は言語と世界の等形性（Abbildung）に依存する。", "哲学・倫理学", "Western_Europe", 1921, "https://en.wikipedia.org/wiki/Tractatus_Logico-Philosophicus"),
    ("分析哲学の起源", "Origins of Analytic Philosophy", "フレーゲ・ラッセル・ムーアの概念分析と論理分析に始まる哲学的伝統の形成史。観念論批判・論理的分析の方法・記号論理の哲学への適用が出発点。ダメットが起源研究を主導。", "哲学・倫理学", "Western_Europe", 1879, "https://en.wikipedia.org/wiki/Analytic_philosophy"),
    ("オックスフォード日常言語哲学", "Oxford Ordinary Language Philosophy", "ライル、オースティン、ストローソンらオックスフォード哲学者が発展させた方法論。日常言語の文法的分析によって哲学的混乱を診断・解消しようとする。", "哲学・倫理学", "Western_Europe", 1945, "https://en.wikipedia.org/wiki/Ordinary_language_philosophy"),
    ("クワインの哲学", "Quine's Philosophy", "W.V.O.クワインの分析哲学・認識論・存在論。分析と総合の区別批判（経験主義の二つのドグマ）、認識論の自然化、オントロジーの相対性が代表的立場。", "哲学・倫理学", "North_America", 1953, "https://en.wikipedia.org/wiki/Willard_Van_Orman_Quine"),
    ("デイヴィドソンの哲学", "Davidson's Philosophy", "ドナルド・デイヴィドソンの言語哲学・心の哲学・行為論。根本的解釈、異則的一元論（非法則的モニズム）、コミュニケーション的三角形が代表的理論。", "哲学・倫理学", "North_America", 1963, "https://en.wikipedia.org/wiki/Donald_Davidson_(philosopher)"),
    ("キプリングの問題", "Kripke's Philosophy", "ソール・クリプキの哲学。固定指示子（proper name）の意味論、後験的必然性、規則遵守のパラドクス（クリプキンシュタイン）、真理論（グラウンデッドネス）が代表的貢献。", "哲学・倫理学", "North_America", 1972, "https://en.wikipedia.org/wiki/Saul_Kripke"),
    ("デリダの脱構築", "Derrida's Deconstruction", "ジャック・デリダが展開した哲学的読解実践。ロゴス中心主義・音声中心主義批判、差延（différance）、テクストの外はない、亡霊論（hauntology）が代表的概念。", "哲学・倫理学", "Western_Europe", 1967, "https://en.wikipedia.org/wiki/Deconstruction"),
    ("フーコーの権力論", "Foucault's Theory of Power", "ミシェル・フーコーが展開した権力・知識・主体の関係論。規律権力（一望監視装置パノプティコン）、生権力・生政治、系譜学的方法が代表的概念。", "哲学・倫理学", "Western_Europe", 1975, "https://en.wikipedia.org/wiki/Michel_Foucault"),
    ("ブルデューの哲学", "Bourdieu's Philosophy", "ピエール・ブルデューの社会哲学。ハビトゥス・場（フィールド）・文化資本・象徴暴力が中核概念。社会学的実践理論として構造主義と実践論の統合を図る。", "哲学・倫理学", "Western_Europe", 1972, "https://en.wikipedia.org/wiki/Pierre_Bourdieu"),
    ("バトラーのパフォーマティヴィティ", "Butler's Performativity", "ジュディス・バトラーのジェンダー・パフォーマティヴィティ理論。ジェンダーは生来のものでなく反復的実践によって構成・再構成されるという理論。オースティンの発語行為論から着想を得る。", "哲学・倫理学", "North_America", 1990, "https://en.wikipedia.org/wiki/Judith_Butler"),
    ("ネグリとハートの帝国論", "Negri and Hardt's Empire", "アントニオ・ネグリとマイケル・ハートが共著した『帝国』（2000年）。グローバル主権の新しい形態としての「帝国」と、それへの対抗力としての「マルチチュード」を論じる。", "哲学・倫理学", "Western_Europe", 2000, "https://en.wikipedia.org/wiki/Empire_(Hardt_and_Negri)"),
    ("スラヴォイ・ジジェクの哲学", "Slavoj Zizek's Philosophy", "ラカンの精神分析とヘーゲル弁証法をマルクス主義的イデオロギー批判に接続するスロベニア出身の哲学者の理論。イデオロギーの幻想的構造、崇高なる対象、欲動の倫理が代表概念。", "哲学・倫理学", "Western_Europe", 1989, "https://en.wikipedia.org/wiki/Slavoj_%C5%BDi%C5%BEek"),
    ("アレントの政治哲学", "Arendt's Political Philosophy", "ハンナ・アレントの公私区分論、全体主義の起源分析、権力と暴力の区別、活動的生活（vita activa）の三形態（労働・仕事・活動）が代表的概念。悪の凡庸性の分析で知られる。", "哲学・倫理学", "Western_Europe", 1951, "https://en.wikipedia.org/wiki/Hannah_Arendt"),
    ("ロールズの正義論", "Rawls's Theory of Justice", "ジョン・ロールズの政治哲学。無知のヴェール・元の立場・正義の二原理（平等な基本的自由・格差原理）が基礎概念。リベラリズムの代表的理論として倫理学・政治学に多大な影響。", "哲学・倫理学", "North_America", 1971, "https://en.wikipedia.org/wiki/A_Theory_of_Justice"),
    ("コミュニタリアニズム", "Communitarianism", "ロールズ流のリベラリズムへの批判として登場した政治哲学的立場。テイラー、サンデル、マッキンタイア、ウォルツァーが代表。共同体の文化・価値・伝統の優先を主張する。", "哲学・倫理学", "North_America", 1982, "https://en.wikipedia.org/wiki/Communitarianism"),
    ("リバタリアニズム", "Libertarianism", "個人の自由と財産権を最高価値とする政治哲学。ノージック（アナーキー・国家・ユートピア）が代表的論者。最小国家論、市場自由主義、自己所有権テーゼが中核。", "哲学・倫理学", "North_America", 1974, "https://en.wikipedia.org/wiki/Libertarianism"),
    ("共和主義（政治哲学）", "Republicanism", "自由を支配の不在（non-domination）として定義する政治哲学的立場。ペティット（非支配の自由）、スキナー（ネオ・ローマ的自由）が代表的論者。ハリントン、マキャヴェリに源泉を持つ。", "哲学・倫理学", "Western_Europe", 1997, "https://en.wikipedia.org/wiki/Republicanism"),
    ("多文化主義の哲学", "Philosophy of Multiculturalism", "文化的少数派・先住民族・移民集団の集団的権利と文化的認定を論じる政治哲学。キムリッカの自由主義的多文化主義、パレクの多文化主義の再考が代表的立場。", "哲学・倫理学", "North_America", 1995, "https://en.wikipedia.org/wiki/Multiculturalism"),
    ("フェミニスト哲学", "Feminist Philosophy", "女性の視点と経験から哲学的問いを再構成する理論的実践。平等・差異・ケア・権力・身体の概念を問い直す。ボーヴォワール（第二の性）、バトラー、フリーダン、ウルストンクラフトが代表。", "哲学・倫理学", "Western_Europe", 1949, "https://en.wikipedia.org/wiki/Feminist_philosophy"),
    ("脱植民地哲学", "Decolonial Philosophy", "ヨーロッパ中心的な哲学の地理的・歴史的偏向を批判し代替的知識体系を探求する哲学的立場。ミニョロ（局所的知識）、ケイハル（エピステーミック・デコロナイゼーション）が代表。", "哲学・倫理学", "Latin_America", 2000, "https://en.wikipedia.org/wiki/Decolonial_theory"),
    ("黒人哲学", "African American Philosophy", "アフリカ系アメリカ人の哲学的伝統。デュボイス（ダブル・コンシャスネス）、コーネル・ウェスト（実用主義的プロフェシー）、パトリシア・ヒル・コリンズが代表的論者。人種・自由・アイデンティティを中核とする。", "哲学・倫理学", "North_America", 1903, "https://en.wikipedia.org/wiki/African-American_philosophy"),
    ("アフリカ哲学（現代）", "Contemporary African Philosophy", "ポスト独立期のアフリカ哲学者による哲学的探求。エタ・エバン（民族哲学批判）、オゴン（エスノフィロソフィー批判）、ギラコ（フィロソフィー・ポリティーク）が代表的論者。", "哲学・倫理学", "Sub_Saharan_Africa", 1976, "https://en.wikipedia.org/wiki/African_philosophy"),
    # ===== 歴史学 新規 (~60) =====
    ("古代ギリシアの歴史", "History of Ancient Greece", "ミノア文明・ミケーネ文明から古典期・ヘレニズム期に至るギリシアの歴史。ポリス形成、ペルシア戦争、ペロポネソス戦争、アレクサンドロス大王の征服が主要事件。", "歴史学", "Western_Europe", -3000, "https://en.wikipedia.org/wiki/Ancient_Greece"),
    ("ローマ帝国史", "History of the Roman Empire", "紀元前27年のアウグストゥス即位から西ローマ帝国滅亡（476年）に至るローマ帝国の政治・軍事・文化史。パクス・ロマーナ・専制政治・三世紀の危機・キリスト教国教化が主要テーマ。", "歴史学", "Western_Europe", -27, "https://en.wikipedia.org/wiki/Roman_Empire"),
    ("中世ヨーロッパ史", "History of Medieval Europe", "5〜15世紀のヨーロッパの政治・社会・宗教・文化史。封建制度・十字軍・カトリック教会の権威・百年戦争・黒死病が主要テーマ。ル・ゴフ、ブロックが代表的研究者。", "歴史学", "Western_Europe", 476, "https://en.wikipedia.org/wiki/Middle_Ages"),
    ("ルネサンス史", "History of the Renaissance", "14〜17世紀イタリアを中心に展開した文化・思想・芸術の変革期の歴史。人文主義、ダ・ヴィンチ、ミケランジェロ、マキャヴェリ、コペルニクスが代表的人物・業績。", "歴史学", "Western_Europe", 1300, "https://en.wikipedia.org/wiki/Renaissance"),
    ("大航海時代史", "History of the Age of Exploration", "15〜17世紀のヨーロッパ人による世界探検・植民地化の歴史。ヴァスコ・ダ・ガマ、コロンブス、マゼランが代表的探検家。新大陸発見・香料貿易・植民地帝国形成が主要テーマ。", "歴史学", "Western_Europe", 1415, "https://en.wikipedia.org/wiki/Age_of_Discovery"),
    ("産業革命史", "History of the Industrial Revolution", "18世紀後半〜19世紀のイギリスから始まった工業化の歴史。蒸気機関・紡績機械・鉄道・都市化・労働運動が主要テーマ。アシュトン、ランデスが代表的研究者。", "歴史学", "Western_Europe", 1760, "https://en.wikipedia.org/wiki/Industrial_Revolution"),
    ("世界大戦の歴史", "History of World Wars", "第一次世界大戦（1914〜1918年）と第二次世界大戦（1939〜1945年）の歴史的研究。ケーガン、キーガン、エヴァンスが代表的論者。帝国主義・ナショナリズム・全体主義が主要因。", "歴史学", "Western_Europe", 1914, "https://en.wikipedia.org/wiki/World_War_I"),
    ("脱植民地化の歴史", "History of Decolonization", "20世紀中葉のアジア・アフリカ諸国の植民地からの独立運動と国民国家形成の歴史。ガンジー（インド）、ンクルマ（ガーナ）、スカルノ（インドネシア）が代表的指導者。", "歴史学", "Global_Synthesis", 1945, "https://en.wikipedia.org/wiki/Decolonization"),
    ("イスラーム文明の歴史", "History of Islamic Civilization", "7世紀のムハンマド以降のイスラーム帝国（ウマイヤ・アッバース・ファーティマ）の政治・科学・芸術・哲学の発展史。黄金時代の科学革命、モンゴルの侵略、オスマン帝国が主要テーマ。", "歴史学", "West_Asia_North_Africa", 622, "https://en.wikipedia.org/wiki/History_of_Islam"),
    ("中国史（清朝・近代）", "History of Qing China and Modern China", "1644〜1912年の清朝史と1912年以降の中華民国・中華人民共和国の歴史。アヘン戦争・太平天国の乱・辛亥革命・五四運動・文化大革命が主要事件。スペンスが代表的研究者。", "歴史学", "East_Asia", 1644, "https://en.wikipedia.org/wiki/Qing_dynasty"),
    ("インド史（近代）", "History of Modern India", "ムガル帝国衰退から英領インド・独立・分離独立（1947年）に至るインドの近現代史。英国東インド会社・セポイの反乱・国民会議派・マハトマ・ガンジーが主要テーマ。", "歴史学", "South_Asia", 1757, "https://en.wikipedia.org/wiki/History_of_India"),
    ("日本近現代史", "Modern Japanese History", "明治維新（1868年）から現代に至る日本の政治・社会・経済・文化史。近代化・帝国主義・太平洋戦争・占領期・高度経済成長が主要テーマ。", "歴史学", "East_Asia", 1868, "https://en.wikipedia.org/wiki/History_of_Japan"),
    ("アフリカ前植民地史", "Pre-Colonial African History", "植民地化以前のアフリカの文明・王国・国家の歴史。マリ帝国・ソンガイ帝国・アクスム王国・コンゴ王国・グレート・ジンバブエが主要研究対象。", "歴史学", "Sub_Saharan_Africa", 300, "https://en.wikipedia.org/wiki/Pre-colonial_Africa"),
    ("ラテンアメリカ独立史", "History of Latin American Independence", "19世紀初頭のスペイン・ポルトガル植民地からのラテンアメリカ諸国の独立運動史。シモン・ボリバル、サン・マルティン、オイギンス、ミランダが代表的人物。", "歴史学", "Latin_America", 1810, "https://en.wikipedia.org/wiki/Spanish_American_wars_of_independence"),
    ("ジェノサイドの歴史と研究", "Genocide History and Studies", "20世紀以降の集団的虐殺（アルメニア人虐殺・ホロコースト・カンボジア・ルワンダ）の歴史的・政治学的研究。レムキン（ジェノサイド概念の創出）、パワーが代表的論者。", "歴史学", "Global_Synthesis", 1915, "https://en.wikipedia.org/wiki/Genocide"),
    ("記憶と歴史論", "Memory and History", "集合的記憶・歴史意識・記念行為の理論的研究。ハルヴァックスの集合的記憶概念、ノラの場所の記憶、リクールの記憶・歴史・忘却が代表的理論。", "歴史学", "Western_Europe", 1925, "https://en.wikipedia.org/wiki/Collective_memory"),
    ("経済史の方法論", "Methodology of Economic History", "歴史研究に計量的・統計的手法を適用する計量経済史（クリオメトリクス）の発展。フォゲル（奴隷制の効率性研究）、ノース（制度と経済変化）が代表的論者。", "歴史学", "North_America", 1958, "https://en.wikipedia.org/wiki/Cliometrics"),
    ("社会史の方法論", "Methodology of Social History", "通常の政治史を超えて庶民・労働者・農民・女性の歴史を描く方法論。アナール学派（フェーブル・ブローデル）、イギリス社会史学派（トンプソン）が代表的アプローチ。", "歴史学", "Western_Europe", 1929, "https://en.wikipedia.org/wiki/Social_history"),
    ("歴史の因果性論", "Historical Causation", "歴史的出来事の原因と結果の関係を分析する歴史哲学の問い。決定論的・偶然論的・構造論的・エージェント中心的因果モデルが対立する。ダントーの分析哲学的アプローチが代表。", "歴史学", "Western_Europe", 1965, "https://en.wikipedia.org/wiki/Causality"),
    ("歴史と物語の関係", "History and Narrative", "歴史記述における物語形式の認識論的地位を問う。ホワイト（メタヒストリー）の歴史のトロポロジー、リクールの物語的アイデンティティ、アンカースミットの歴史表象論が代表的立場。", "歴史学", "North_America", 1973, "https://en.wikipedia.org/wiki/Historiography"),
    # ===== 宗教学 新規 (~30) =====
    ("ユダヤ教の歴史", "History of Judaism", "古代イスラエルから現代に至るユダヤ教の発展史。モーセ五書・タルムード・カバラー・ハスカラー（ユダヤ啓蒙）・シオニズム・ホロコーストが主要テーマ。", "宗教学", "West_Asia_North_Africa", -2000, "https://en.wikipedia.org/wiki/Judaism"),
    ("イスラーム神学（カラーム）", "Islamic Theology (Kalam)", "イスラームの神学的論争と体系の研究。ムウタジラ派（理性主義）・アシュアリー派（正統神学）・マートゥリーディー派が主要学派。神の属性・人間の自由意志・創造論が主要論争点。", "宗教学", "West_Asia_North_Africa", 750, "https://en.wikipedia.org/wiki/Kalam"),
    ("キリスト教神学の歴史", "History of Christian Theology", "初期教会から現代に至るキリスト教神学の発展。三位一体論争（ニカイア公会議）・キリスト論論争・アウグスティヌスの恩寵論・スコラ神学・宗教改革神学が主要テーマ。", "宗教学", "Western_Europe", 100, "https://en.wikipedia.org/wiki/Christian_theology"),
    ("神学的実存主義", "Theological Existentialism", "キルケゴール・バルト・ブルトマンが展開した実存主義的神学。個人的信仰の絶対的選択、神の言葉（Word of God）の啓示、非神話化（entmythologisierung）が代表的概念。", "宗教学", "Western_Europe", 1843, "https://en.wikipedia.org/wiki/Christian_existentialism"),
    ("解放の神学（アフリカ）", "African Liberation Theology", "アフリカのキリスト教神学者による黒人解放の文脈での神学的探求。アラン・ブーサック、デズモンド・ツツ、タラロ・ベウラが代表。アパルトヘイト反対と黒人アイデンティティの肯定が中核。", "宗教学", "Sub_Saharan_Africa", 1972, "https://en.wikipedia.org/wiki/Black_theology"),
    ("アジア神学", "Asian Theology", "アジアの文化的・宗教的文脈からキリスト教神学を再解釈する試み。ツヌー・スン、クワメ・ベクー、チェン・フォン・チョンが代表的論者。アジアの貧困・多宗教状況が主要文脈。", "宗教学", "East_Asia", 1975, "https://en.wikipedia.org/wiki/Contextual_theology"),
    ("仏教経済学", "Buddhist Economics", "シューマッハー（スモール・イズ・ビューティフル）が提唱した仏教的価値観に基づく経済思想。欲望の制御・正しい生活・共同体的生産様式・非暴力が中核。タイの仏教経済学にも発展。", "宗教学", "South_Asia", 1973, "https://en.wikipedia.org/wiki/Buddhist_economics"),
    ("ネオ・コンフュシアニズム", "Neo-Confucianism", "宋代（960〜1279年）に展開した儒教の哲学的・形而上学的刷新。朱熹（朱子）の理気論が代表的体系。仏教・道家との対話を経て宇宙論・心性論を発展させた。", "宗教学", "East_Asia", 1000, "https://en.wikipedia.org/wiki/Neo-Confucianism"),
    ("ゾロアスター教の研究", "Zoroastrian Studies", "古代ペルシアのゾロアスター教（マズダー教）の歴史・神学・儀礼の研究。アフラ・マズダーとアンラ・マインユの善悪二元論、アヴェスター文書、パルシー共同体が研究対象。", "宗教学", "West_Asia_North_Africa", -1500, "https://en.wikipedia.org/wiki/Zoroastrianism"),
    ("神話の構造論", "Structural Analysis of Myth", "レヴィ＝ストロースが発展させた神話の構造的分析法。神話素（mytheme）の対立と媒介のパターンによって神話の深層構造を解明する。オイディプス神話・ボロロ神話の分析が代表。", "宗教学", "Western_Europe", 1955, "https://en.wikipedia.org/wiki/Structural_anthropology"),
    # ===== 古典学 新規 (~30) =====
    ("ストア哲学", "Stoic Philosophy", "ゼノン・クリュシッポス・マルクス・アウレリウスが展開した古代哲学の学派。自然に従った生、徳のみが善、情念（パトス）への超然が中核的主張。ローマ時代に倫理哲学として隆盛した。", "古典学", "Western_Europe", -300, "https://en.wikipedia.org/wiki/Stoicism"),
    ("エピクロス哲学", "Epicurean Philosophy", "エピクロスが創始した古代哲学の学派。快楽（特にアタラクシア＝平静心）が最高善、死の恐怖の解消、隠棲して友と過ごす生活が理想とされる。原子論的物理学を基盤とする。", "古典学", "Western_Europe", -307, "https://en.wikipedia.org/wiki/Epicureanism"),
    ("プラトンのイデア論", "Plato's Theory of Forms", "プラトンの形而上学の核心。感覚的世界の背後に完全・永遠なるイデア（形相）の領域があり、知識はイデアの想起（アナムネーシス）であるという理論。洞窟の比喩が代表的説明。", "古典学", "Western_Europe", -370, "https://en.wikipedia.org/wiki/Theory_of_forms"),
    ("アリストテレスの形而上学", "Aristotle's Metaphysics", "アリストテレスの存在論。形相と質料、可能態と現実態、実体と属性、四原因説（質料因・形相因・動力因・目的因）が中核概念。プラトンのイデア論批判から出発する。", "古典学", "Western_Europe", -350, "https://en.wikipedia.org/wiki/Aristotle%27s_Metaphysics"),
    ("新プラトン主義", "Neoplatonism", "プロティノスが創始したプラトン哲学の神秘主義的展開（3世紀）。一者（to hen）からの流出（emanation）論、魂の上昇と観照（theoria）が中核。中世キリスト教・イスラーム神学に影響。", "古典学", "Western_Europe", 245, "https://en.wikipedia.org/wiki/Neoplatonism"),
    ("ソクラテス的対話法", "Socratic Method", "ソクラテスが実践した哲学的対話の方法。問答（エレンコス）を通じて相手の無知を自覚させ（産婆術・マイエウティケー）真の知識を探求する。プラトンの対話篇に記録される。", "古典学", "Western_Europe", -399, "https://en.wikipedia.org/wiki/Socratic_method"),
    ("キケロとローマ哲学", "Cicero and Roman Philosophy", "マルクス・トゥッリウス・キケロのローマへのギリシア哲学の翻訳と独自展開。弁論術・政治哲学・友情論・義務論（De Officiis）が代表的著作。共和政理念の哲学的擁護が特徴。", "古典学", "Western_Europe", -106, "https://en.wikipedia.org/wiki/Cicero"),
    ("ローマの詩人と詩学", "Roman Poets and Poetics", "古代ローマの詩の理論と主要詩人の研究。ウェルギリウス（アエネイス・農耕詩）・ホラティウス（頌歌・諷刺詩）・オウィディウス（変身物語・愛の技法）・ルクレティウス（物の本性について）が代表。", "古典学", "Western_Europe", -70, "https://en.wikipedia.org/wiki/Latin_poetry"),
    ("古代インド哲学（ニヤーヤ学派）", "Nyaya School of Indian Philosophy", "古代インドのニヤーヤ学派（正しい論理の学派）。ゴータマの哲学綱要（ニヤーヤ・スートラ）が基本テキスト。四つの知識源泉（知覚・推論・類比・証言）と十六カテゴリーが体系の基礎。", "古典学", "South_Asia", 200, "https://en.wikipedia.org/wiki/Ny%C4%81ya"),
    ("古代インド哲学（ヴァイシェーシカ学派）", "Vaisheshika School of Indian Philosophy", "古代インドの原子論的自然哲学の学派。カナーダの哲学綱要（ヴァイシェーシカ・スートラ）が基本テキスト。実体・性質・運動・普遍・特殊・内属の六カテゴリーによる実在分析が特徴。", "古典学", "South_Asia", 200, "https://en.wikipedia.org/wiki/Vaisheshika"),
    # ===== 美学・芸術理論 新規 (~40) =====
    ("芸術の本質と定義", "Nature and Definition of Art", "芸術とは何かという美学の根本的問い。模倣説・表現説・形式説・制度論・クラスター概念説・家族的類似説が主要アプローチ。定義不可能説（ウィーツ）も重要な立場。", "美学・芸術理論", "Western_Europe", 1956, "https://en.wikipedia.org/wiki/Aesthetics"),
    ("美的判断力批判", "Critique of Aesthetic Judgment", "カントの第三批判（判断力批判）における美的判断の分析。美は利害関心なき満足・普遍的必然性・目的なき合目的性・共通感覚への訴えかけという四契機で規定される。", "美学・芸術理論", "Western_Europe", 1790, "https://en.wikipedia.org/wiki/Critique_of_Judgment"),
    ("ベネデット・クローチェの表現論", "Croce's Expressionism", "イタリアの哲学者クローチェの芸術哲学。芸術は直観の表現であり、表現は同時に言語であるとする。精神の哲学の一部として美学を位置づけ、技術と芸術を厳しく区別する。", "美学・芸術理論", "Western_Europe", 1902, "https://en.wikipedia.org/wiki/Benedetto_croce"),
    ("クライブ・ベルの形式主義美学", "Bell's Formalist Aesthetics", "クライブ・ベルが提唱した「有意味な形式（significant form）」の美学。芸術の本質は特定の形式的関係にあり、その知覚が美的感動（aesthetic emotion）を引き起こすとする。", "美学・芸術理論", "Western_Europe", 1914, "https://en.wikipedia.org/wiki/Significant_form"),
    ("グッドマンの記号論的美学", "Goodman's Semiotic Aesthetics", "ネルソン・グッドマンの「芸術の言語」（1968年）。芸術を記号体系として分析し、密 度・飽和・例示・多重参照・相対的充填性という記号論的基準を提示する。", "美学・芸術理論", "North_America", 1968, "https://en.wikipedia.org/wiki/Nelson_Goodman"),
    ("リシャール・シャーハン美学", "Shusterman's Somaesthetics", "リチャード・シュスターマンが提唱した身体美学（ソマ・エスセティクス）。デューイのプラグマティスト美学を身体的実践へ拡張し、身体的意識の訓練を生の向上として論じる。", "美学・芸術理論", "North_America", 2000, "https://en.wikipedia.org/wiki/Somaesthetics"),
    ("ダントーの芸術界論", "Danto's Artworld Theory", "アーサー・ダントーが提唱した芸術界（artworld）の概念。芸術作品をそれとして見るためには芸術の歴史と理論という「雰囲気」（atmosphere）が必要だとする。芸術の歴史の終わりも提唱。", "美学・芸術理論", "North_America", 1964, "https://en.wikipedia.org/wiki/Arthur_Danto"),
    ("マーセル・デュシャンとコンセプチュアル・アート", "Duchamp and Conceptual Art", "デュシャンのレディメイド（1917年の泉）がコンセプチュアル・アートの先駆けとなった経緯。芸術の意図・制度・コンセプトの優位性、「芸術とは何か」への根本的挑戦を論じる。", "美学・芸術理論", "Western_Europe", 1917, "https://en.wikipedia.org/wiki/Conceptual_art"),
    ("アドルノの美学", "Adorno's Aesthetics", "テオドール・アドルノの美学理論。芸術の否定弁証法的性格、文化産業批判、前衛音楽（シェーンベルク）への支持、美的外観（Schein）と真理内実（Wahrheitsgehalt）の緊張が代表的概念。", "美学・芸術理論", "Western_Europe", 1970, "https://en.wikipedia.org/wiki/Theodor_W._Adorno"),
    ("ランシエールの美学", "Rancière's Aesthetics", "ジャック・ランシエールの政治的美学論。芸術の感性的分割（le partage du sensible）の概念、美学的体制と倫理的・表象的体制の区別、美学の民主主義的可能性が代表的論点。", "美学・芸術理論", "Western_Europe", 2000, "https://en.wikipedia.org/wiki/Jacques_Ranci%C3%A8re"),
    ("イスラーム美術と美学", "Islamic Art and Aesthetics", "イスラームの芸術的伝統における美学的原理の研究。偶像崇拝禁止とアラビア書道・幾何学模様の発展、アラベスク、建築的象徴性、スーフィー詩の美学が代表的論点。", "美学・芸術理論", "West_Asia_North_Africa", 650, "https://en.wikipedia.org/wiki/Islamic_art"),
    ("アフリカ美術と美学", "African Art and Aesthetics", "サハラ以南のアフリカ諸文化の芸術的伝統と美的概念の研究。ヨルバ美学（アセ・美的力）、グレート・ジンバブエの建築、ベナン王国ブロンズが代表的研究対象。", "美学・芸術理論", "Sub_Saharan_Africa", 1000, "https://en.wikipedia.org/wiki/African_art"),
    ("ラテンアメリカ美術と美学", "Latin American Art and Aesthetics", "メソアメリカ古代美術から近代ムラリズム（ディエゴ・リベラ）、マジック・リアリズムの視覚芸術（フリーダ・カーロ）、ラテンアメリカのコンセプチュアル・アートまでを対象とする。", "美学・芸術理論", "Latin_America", -1500, "https://en.wikipedia.org/wiki/Latin_American_art"),
    ("身体芸術とパフォーマンス", "Body Art and Performance", "身体そのものを媒体とする芸術実践と理論。ヘルマン・ニッチュ、クリス・バーデン、シナ・アーペル、マリーナ・アブラモヴィッチが代表的アーティスト。恒久性・リスク・現前性が主要論点。", "美学・芸術理論", "Western_Europe", 1960, "https://en.wikipedia.org/wiki/Body_art"),
    # ===== 言語学 (新規専門) (~40) =====
    ("スタンスと主観性", "Stance and Subjectivity in Language", "話者が命題内容への態度・コミットメント・感情を言語的に表明する現象の語用論・文法論的研究。評価表現・認識的モダリティ・主観性マーカーが主要研究対象。", "言語学", "North_America", 2002, "https://en.wikipedia.org/wiki/Evidentiality"),
    ("メタ言語意識", "Metalinguistic Awareness", "言語そのものを対象として意識的に省察する能力の研究。音韻意識・形態意識・統語意識・語用意識の発達と読み書き能力との関連が主要論点。", "言語学", "North_America", 1980, "https://en.wikipedia.org/wiki/Metalinguistic_awareness"),
    ("語彙化パターン", "Lexicalization Patterns", "言語が意味的内容（運動・経路・様態・因果性等）を語彙形態にどのように符号化するかを研究する認知言語学的分野。タルミーの運動イベント類型論が代表的理論。", "言語学", "North_America", 1985, "https://en.wikipedia.org/wiki/Lexicalization"),
    ("言語の色彩語彙", "Color Terminology in Language", "世界の言語における色彩語彙の普遍的パターンと文化的変異を研究する分野。バーリン＆ケイの基本色彩語研究（1969年）が基盤。言語相対性との関連も論じられる。", "言語学", "North_America", 1969, "https://en.wikipedia.org/wiki/Basic_color_terms"),
    ("依存文法", "Dependency Grammar", "文の構造を支配関係（依存関係）のネットワークとして記述する文法理論。テスニエール（文の要素）が創始。プロジェクション文法、依存構造文法（ハドソン）が現代の主要形態。", "言語学", "Western_Europe", 1959, "https://en.wikipedia.org/wiki/Dependency_grammar"),
    ("レキシカル・フォノロジー", "Lexical Phonology", "音韻変化を語彙部門に内在する階層的規則として分析する生成音韻論の枠組み。キパルスキーとモーバーグが提唱。屈折接辞・派生接辞・複合語の音韻挙動を説明する。", "言語学", "North_America", 1982, "https://en.wikipedia.org/wiki/Lexical_phonology"),
    ("パラ言語", "Paralanguage", "言語的コミュニケーションに随伴する音声的・非音声的側面の研究。声量・声調・速度・間・沈黙・呼吸・笑い・泣きが含まれる。言語的メッセージを修正・強調・矛盾させる機能を持つ。", "言語学", "North_America", 1956, "https://en.wikipedia.org/wiki/Paralanguage"),
    ("言語と認知の関係", "Language-Cognition Interface", "言語構造が思考・認知・概念形成に影響するかを問う認知言語学・心理学の中心的問い。新ウォーフ仮説（ボロディツキー）、言語相対性の実証研究、普遍的概念基盤論が対立する。", "言語学", "North_America", 1990, "https://en.wikipedia.org/wiki/Linguistic_relativity"),
    ("語用論的失敗", "Pragmatic Failure", "異文化間コミュニケーションにおける語用論的知識の不足・誤用が引き起こすコミュニケーション障害を研究する分野。トーマスが概念を定式化。語用論的転移、文化的スクリプトとの衝突が主要論点。", "言語学", "Western_Europe", 1983, "https://en.wikipedia.org/wiki/Pragmatics"),
    ("文法化論", "Grammaticalization Theory", "語彙的意味を持つ要素が文法的機能語・接辞等へ変化する歴史的過程を研究する歴史言語学の分野。ホッパー＆トラウゴットが体系化。脱範疇化・音声的縮小・意味の脱色が主要メカニズム。", "言語学", "Western_Europe", 1912, "https://en.wikipedia.org/wiki/Grammaticalization"),
]

print(f"レコード総数: {len(records)}")

con = sqlite3.connect(DB)
con.execute("PRAGMA journal_mode=WAL")
cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM humanities_concept")
before = cur.fetchone()[0]
print(f"既存件数: {before}")

existing = set(r[0] for r in cur.execute("SELECT name_en FROM humanities_concept"))

batch = []
inserted = 0
skipped = 0

for r in records:
    name_en = r[1]
    if name_en in existing:
        skipped += 1
        continue
    existing.add(name_en)
    uid_val = uid()
    batch.append((uid_val, r[0], r[1], r[2], r[3], r[4], r[5], r[6], 'url_present', 'dua_wave_a2', 'active', now, now))
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

cur.execute("SELECT COUNT(*) FROM humanities_concept")
after = cur.fetchone()[0]
con.close()
print(f"inserted={inserted}, skipped={skipped}")
print(f"総件数: {after} (目標5500)")
