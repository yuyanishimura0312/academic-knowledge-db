#!/usr/bin/env python3
"""DUA Wave A2 Batch 7 — 倫理学+大陸哲学+分析哲学+宗教学+美学+古典学"""
import sqlite3, uuid, datetime, os

DB_PATH = os.path.expanduser("~/projects/research/academic-knowledge-db/academic.db")

def uid(): return "dua_" + uuid.uuid4().hex[:12]
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()

CONCEPTS = [
    # 倫理学・政治哲学 +80
    (uid(),"行為功利主義","Act Utilitarianism","個々の行為がもたらす帰結の効用を基準に道徳的正しさを判断する功利主義の一形態","倫理学・政治哲学","Western_Europe",1863,"https://en.wikipedia.org/wiki/Act_utilitarianism",now(),now()),
    (uid(),"規則功利主義","Rule Utilitarianism","行為の正しさを直接ではなく規則への準拠を通じて帰結主義的に評価する立場","倫理学・政治哲学","Western_Europe",1953,"https://en.wikipedia.org/wiki/Rule_utilitarianism",now(),now()),
    (uid(),"選好功利主義","Preference Utilitarianism","快楽ではなく選好の充足を効用の基準とするピーター・シンガーらの功利主義","倫理学・政治哲学","Western_Europe",1979,"https://en.wikipedia.org/wiki/Preference_utilitarianism",now(),now()),
    (uid(),"完全義務","Perfect Duty","カントの義務論において例外なく遵守が求められる義務（嘘をつかない等）","倫理学・政治哲学","Western_Europe",1785,"https://en.wikipedia.org/wiki/Perfect_and_imperfect_duties",now(),now()),
    (uid(),"不完全義務","Imperfect Duty","カントの義務論において状況に応じて履行方法を選択できる義務（慈善等）","倫理学・政治哲学","Western_Europe",1785,"https://en.wikipedia.org/wiki/Perfect_and_imperfect_duties",now(),now()),
    (uid(),"功績原理","Principle of Desert","道徳的功績や業績に応じた分配が正義にかなうとする原理","倫理学・政治哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/Desert_(philosophy)",now(),now()),
    (uid(),"相互性原理","Principle of Reciprocity","協力や互恵関係を正義・倫理の基礎とする原理","倫理学・政治哲学","Global_Synthesis",1971,"https://en.wikipedia.org/wiki/Reciprocity_(social_psychology)",now(),now()),
    (uid(),"ネガティブ義務","Negative Duty","他者に危害を加えないという不作為を求める義務","倫理学・政治哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/Negative_and_positive_rights",now(),now()),
    (uid(),"ポジティブ義務","Positive Duty","他者を支援するための積極的行為を求める義務","倫理学・政治哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/Negative_and_positive_rights",now(),now()),
    (uid(),"コントラクタリズム","Contractualism","道徳的規範は合理的な人々が合意できる原理から導かれるとするスキャンロンらの立場","倫理学・政治哲学","North_America",1998,"https://en.wikipedia.org/wiki/Contractualism",now(),now()),
    (uid(),"ホッブズ的自然状態","Hobbesian State of Nature","政治権力以前の人間の状態を「万人の万人に対する闘争」と特徴づけるホッブズの概念","倫理学・政治哲学","Western_Europe",1651,"https://en.wikipedia.org/wiki/State_of_nature",now(),now()),
    (uid(),"ロック的財産権論","Lockean Property Rights","自己所有と労働混入を根拠とする財産権の正当化論","倫理学・政治哲学","Western_Europe",1689,"https://en.wikipedia.org/wiki/Labor_theory_of_property",now(),now()),
    (uid(),"ルソーの一般意志","General Will","個別意志の集合ではなく共同体全体の善を目指す意志というルソーの概念","倫理学・政治哲学","Western_Europe",1762,"https://en.wikipedia.org/wiki/General_will",now(),now()),
    (uid(),"公正としての正義","Justice as Fairness","ロールズが提唱する無知のヴェールに基づく正義の構想","倫理学・政治哲学","North_America",1971,"https://en.wikipedia.org/wiki/Justice_as_Fairness",now(),now()),
    (uid(),"差異原理","Difference Principle","社会的経済的不平等は最も不利な人々の利益を最大化する場合にのみ正当化されるというロールズの原理","倫理学・政治哲学","North_America",1971,"https://en.wikipedia.org/wiki/Difference_principle",now(),now()),
    (uid(),"反照的均衡","Reflective Equilibrium","道徳的直観と原理を相互調整して整合性を求める方法論","倫理学・政治哲学","North_America",1971,"https://en.wikipedia.org/wiki/Reflective_equilibrium",now(),now()),
    (uid(),"ケア倫理","Ethics of Care","ネル・ノディングズやキャロル・ギリガンが提唱する関係性と配慮を中心とする倫理","倫理学・政治哲学","North_America",1982,"https://en.wikipedia.org/wiki/Ethics_of_care",now(),now()),
    (uid(),"徳倫理学","Virtue Ethics","人格の卓越性（徳）を中心に置き行為よりも行為者に注目するアリストテレス由来の倫理学","倫理学・政治哲学","Western_Europe",-350,"https://en.wikipedia.org/wiki/Virtue_ethics",now(),now()),
    (uid(),"コミュニタリアニズム","Communitarianism","個人よりも共同体・伝統・共有価値を優先するサンデルやマッキンタイアの立場","倫理学・政治哲学","North_America",1982,"https://en.wikipedia.org/wiki/Communitarianism",now(),now()),
    (uid(),"共和主義","Republicanism","支配からの自由（非支配）を中心に置くフィリップ・ペティットらの政治哲学","倫理学・政治哲学","Western_Europe",1997,"https://en.wikipedia.org/wiki/Republicanism",now(),now()),
    (uid(),"コスモポリタニズム","Cosmopolitanism","すべての人間が一つの道徳的共同体に属するとする世界市民主義的立場","倫理学・政治哲学","Global_Synthesis",2006,"https://en.wikipedia.org/wiki/Cosmopolitanism",now(),now()),
    (uid(),"承認の政治","Politics of Recognition","テイラーやホネットが論じる文化的アイデンティティの承認を求める政治","倫理学・政治哲学","North_America",1992,"https://en.wikipedia.org/wiki/Recognition_(sociology)",now(),now()),
    (uid(),"再分配的正義","Redistributive Justice","資源や機会を社会的に再分配することで不平等を是正する正義論","倫理学・政治哲学","Global_Synthesis",1971,"https://en.wikipedia.org/wiki/Distributive_justice",now(),now()),
    (uid(),"グローバル正義","Global Justice","国境を超えた正義の要請を論じる政治哲学の分野","倫理学・政治哲学","Global_Synthesis",1999,"https://en.wikipedia.org/wiki/Global_justice",now(),now()),
    (uid(),"環境倫理学","Environmental Ethics","自然・生態系・動物への道徳的義務を論じる倫理学の分野","倫理学・政治哲学","North_America",1973,"https://en.wikipedia.org/wiki/Environmental_ethics",now(),now()),
    (uid(),"深層生態学","Deep Ecology","自然の内在的価値を認め人間中心主義を批判するアルネ・ネスの思想","倫理学・政治哲学","Western_Europe",1973,"https://en.wikipedia.org/wiki/Deep_ecology",now(),now()),
    (uid(),"エコフェミニズム","Ecofeminism","女性支配と自然支配の構造的連関を批判する思想・運動","倫理学・政治哲学","North_America",1974,"https://en.wikipedia.org/wiki/Ecofeminism",now(),now()),
    (uid(),"動物の権利","Animal Rights","ピーター・シンガーやトム・レーガンが論じる動物の道徳的地位","倫理学・政治哲学","North_America",1975,"https://en.wikipedia.org/wiki/Animal_rights",now(),now()),
    (uid(),"AIの倫理","AI Ethics","人工知能の開発・利用における倫理的問題を扱う応用倫理学","倫理学・政治哲学","Global_Synthesis",2010,"https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence",now(),now()),
    (uid(),"テクノロジー倫理","Technology Ethics","科学技術の設計・利用・影響を倫理的に評価する分野","倫理学・政治哲学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Ethics_of_technology",now(),now()),
    (uid(),"バイオエシックス","Bioethics","医療・生命科学に関わる倫理的問題を扱う応用倫理学","倫理学・政治哲学","North_America",1971,"https://en.wikipedia.org/wiki/Bioethics",now(),now()),
    (uid(),"インフォームドコンセント","Informed Consent","医療行為や研究参加に際し十分な説明に基づく同意を求める原則","倫理学・政治哲学","North_America",1957,"https://en.wikipedia.org/wiki/Informed_consent",now(),now()),
    (uid(),"自律原理","Principle of Autonomy","個人の自己決定権を道徳の基礎に置く原理","倫理学・政治哲学","Western_Europe",1785,"https://en.wikipedia.org/wiki/Autonomy",now(),now()),
    (uid(),"無危害原理","Principle of Non-Maleficence","他者に危害を加えないという義務を倫理の基本に置く原理","倫理学・政治哲学","North_America",1979,"https://en.wikipedia.org/wiki/Primum_non_nocere",now(),now()),
    (uid(),"ubuntu倫理","Ubuntu Ethics","「人は他者を通じて人になる」というアフリカの共同体的人間観に基づく倫理","倫理学・政治哲学","Sub_Saharan_Africa",2000,"https://en.wikipedia.org/wiki/Ubuntu_philosophy",now(),now()),
    (uid(),"先住民倫理","Indigenous Ethics","先住民の伝統的知識・関係的世界観に根ざした倫理体系","倫理学・政治哲学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Indigenous_ethics",now(),now()),
    (uid(),"仏教倫理","Buddhist Ethics","不殺生・慈悲・中道を中心とする仏教の道徳体系","倫理学・政治哲学","East_Asia",500,"https://en.wikipedia.org/wiki/Buddhist_ethics",now(),now()),
    (uid(),"儒家倫理","Confucian Ethics","仁・義・礼・智を中心とする儒教の道徳体系","倫理学・政治哲学","East_Asia",-500,"https://en.wikipedia.org/wiki/Confucian_ethics",now(),now()),
    (uid(),"イスラーム倫理","Islamic Ethics","クルアーンとスンナに基づくイスラームの道徳体系","倫理学・政治哲学","West_Asia_North_Africa",700,"https://en.wikipedia.org/wiki/Islamic_ethics",now(),now()),
    (uid(),"政治的リベラリズム","Political Liberalism","包括的教義ではなく政治的価値のみに基づく正義の構想というロールズの後期思想","倫理学・政治哲学","North_America",1993,"https://en.wikipedia.org/wiki/Political_liberalism_(Rawls)",now(),now()),
    (uid(),"熟議民主主義","Deliberative Democracy","理性的討議を通じた合意形成を民主主義の核に置くハーバーマスらの立場","倫理学・政治哲学","Western_Europe",1994,"https://en.wikipedia.org/wiki/Deliberative_democracy",now(),now()),
    (uid(),"参加民主主義","Participatory Democracy","市民の直接的政治参加を重視する民主主義論","倫理学・政治哲学","Global_Synthesis",1970,"https://en.wikipedia.org/wiki/Participatory_democracy",now(),now()),
    (uid(),"アナーキズム","Anarchism","国家権威を否定し自発的協力に基づく社会を目指す政治思想","倫理学・政治哲学","Western_Europe",1840,"https://en.wikipedia.org/wiki/Anarchism",now(),now()),
    (uid(),"マルクス主義政治哲学","Marxist Political Philosophy","生産様式・階級闘争・疎外を中心概念とするマルクスの政治哲学","倫理学・政治哲学","Western_Europe",1848,"https://en.wikipedia.org/wiki/Marxist_philosophy",now(),now()),
    (uid(),"フェミニスト政治哲学","Feminist Political Philosophy","ジェンダー不平等の構造を批判し解放を目指す政治哲学","倫理学・政治哲学","Global_Synthesis",1970,"https://en.wikipedia.org/wiki/Feminist_political_philosophy",now(),now()),
    (uid(),"ポストコロニアル政治","Postcolonial Politics","植民地主義の遺産と権力構造を批判的に分析する政治思想","倫理学・政治哲学","Global_Synthesis",1978,"https://en.wikipedia.org/wiki/Postcolonialism",now(),now()),
    (uid(),"批判的人種理論","Critical Race Theory","人種と権力の法的・社会的構造を批判的に分析する理論","倫理学・政治哲学","North_America",1989,"https://en.wikipedia.org/wiki/Critical_race_theory",now(),now()),
    (uid(),"インターセクショナリティ","Intersectionality","人種・ジェンダー・階級等の複合的差別構造を分析する概念","倫理学・政治哲学","North_America",1989,"https://en.wikipedia.org/wiki/Intersectionality",now(),now()),
    (uid(),"ケイパビリティ・アプローチ","Capability Approach","アマルティア・センとマーサ・ヌスバウムが提唱する潜在能力を福祉の基軸とする枠組","倫理学・政治哲学","Global_Synthesis",1985,"https://en.wikipedia.org/wiki/Capability_approach",now(),now()),
    (uid(),"普遍的基本所得","Universal Basic Income","すべての市民に無条件に支給される基本所得の政治哲学的根拠","倫理学・政治哲学","Global_Synthesis",2017,"https://en.wikipedia.org/wiki/Universal_basic_income",now(),now()),
    (uid(),"ビーガン倫理","Vegan Ethics","動物搾取を拒否しすべての感覚を持つ存在への配慮を求める倫理的立場","倫理学・政治哲学","Global_Synthesis",1944,"https://en.wikipedia.org/wiki/Veganism",now(),now()),
    (uid(),"超人","Übermensch","ニーチェが提唱する既存の道徳を超えて価値を創造する人間像","倫理学・政治哲学","Western_Europe",1883,"https://en.wikipedia.org/wiki/%C3%9Cbermensch",now(),now()),
    (uid(),"権力への意志","Will to Power","ニーチェの哲学における自己超克と価値創造を促す根本的衝動","倫理学・政治哲学","Western_Europe",1886,"https://en.wikipedia.org/wiki/Will_to_power",now(),now()),
    (uid(),"ニヒリズム","Nihilism","価値・意味・知識などの客観的根拠を否定する哲学的立場","倫理学・政治哲学","Western_Europe",1860,"https://en.wikipedia.org/wiki/Nihilism",now(),now()),
    (uid(),"道徳実在論","Moral Realism","道徳的事実が客観的に存在するという立場","倫理学・政治哲学","Western_Europe",1975,"https://en.wikipedia.org/wiki/Moral_realism",now(),now()),
    (uid(),"道徳反実在論","Moral Anti-Realism","客観的道徳的事実の存在を否定する立場の総称","倫理学・政治哲学","Western_Europe",1977,"https://en.wikipedia.org/wiki/Moral_anti-realism",now(),now()),
    (uid(),"情動主義","Emotivism","道徳判断は事実記述ではなく感情表明であるというエイヤーらの立場","倫理学・政治哲学","Western_Europe",1936,"https://en.wikipedia.org/wiki/Emotivism",now(),now()),
    (uid(),"プレスクリプティビズム","Prescriptivism","道徳判断は普遍的行為指令であるというヘアの立場","倫理学・政治哲学","Western_Europe",1952,"https://en.wikipedia.org/wiki/Prescriptivism_(philosophy)",now(),now()),
    (uid(),"自然主義的誤謬","Naturalistic Fallacy","G.E.ムーアが指摘した「善」を自然的性質に還元しようとする誤り","倫理学・政治哲学","Western_Europe",1903,"https://en.wikipedia.org/wiki/Naturalistic_fallacy",now(),now()),
    (uid(),"倫理的直観主義","Ethical Intuitionism","道徳的真理は理性的直観によって認識されるムーアやプリチャードの立場","倫理学・政治哲学","Western_Europe",1903,"https://en.wikipedia.org/wiki/Ethical_intuitionism",now(),now()),
    (uid(),"実存主義倫理","Existentialist Ethics","真正性・自由・責任を中心とするサルトルらの倫理","倫理学・政治哲学","Western_Europe",1946,"https://en.wikipedia.org/wiki/Existentialist_ethics",now(),now()),
    (uid(),"他者の倫理","Ethics of the Other","レヴィナスが提唱する他者の顔を通じた倫理的要請","倫理学・政治哲学","Western_Europe",1961,"https://en.wikipedia.org/wiki/Emmanuel_L%C3%A9vinas",now(),now()),
    (uid(),"ソクラテス的問答法","Socratic Method","問いと対話を通じて知を探求するソクラテスの哲学的方法","倫理学・政治哲学","Western_Europe",-399,"https://en.wikipedia.org/wiki/Socratic_method",now(),now()),
    (uid(),"エピクロス主義","Epicureanism","穏やかな快楽と友情・平静を善とするエピクロスの倫理思想","倫理学・政治哲学","Western_Europe",-307,"https://en.wikipedia.org/wiki/Epicureanism",now(),now()),
    (uid(),"ストア倫理学","Stoic Ethics","理性に従って生き、情念を克服することを善とするストア派の倫理","倫理学・政治哲学","Western_Europe",-300,"https://en.wikipedia.org/wiki/Stoicism",now(),now()),
    (uid(),"パターナリズム","Paternalism","本人の利益のために本人の意思に反して介入することの正当性をめぐる倫理的問題","倫理学・政治哲学","North_America",1971,"https://en.wikipedia.org/wiki/Paternalism",now(),now()),
    (uid(),"害原理","Harm Principle","他者への危害防止以外に個人の自由を制限する正当な理由はないというミルの原理","倫理学・政治哲学","Western_Europe",1859,"https://en.wikipedia.org/wiki/Harm_principle",now(),now()),
    (uid(),"応報的正義","Retributive Justice","犯罪は応分の刑罰を受けるべきとする報復的正義論","倫理学・政治哲学","Western_Europe",1970,"https://en.wikipedia.org/wiki/Retributive_justice",now(),now()),
    (uid(),"修復的正義","Restorative Justice","犯罪被害者・加害者・共同体の関係修復を目指す正義の実践","倫理学・政治哲学","Global_Synthesis",1977,"https://en.wikipedia.org/wiki/Restorative_justice",now(),now()),
    (uid(),"移行期正義","Transitional Justice","紛争・権威主義体制後に過去の人権侵害に対応する正義の機構","倫理学・政治哲学","Global_Synthesis",1995,"https://en.wikipedia.org/wiki/Transitional_justice",now(),now()),
    (uid(),"義務論的制約","Deontological Constraints","帰結にかかわらず守るべき道徳的禁止を設けるネーゲルらの義務論的概念","倫理学・政治哲学","North_America",1979,"https://en.wikipedia.org/wiki/Deontological_ethics",now(),now()),
    (uid(),"トロッコ問題","Trolley Problem","フィリッパ・フットが提起した功利主義と義務論を対比する思考実験","倫理学・政治哲学","Western_Europe",1967,"https://en.wikipedia.org/wiki/Trolley_problem",now(),now()),
    (uid(),"経済的正義","Economic Justice","経済資源の分配と格差を正義の観点から評価する枠組","倫理学・政治哲学","Global_Synthesis",1974,"https://en.wikipedia.org/wiki/Economic_justice",now(),now()),
    (uid(),"市民的不服従","Civil Disobedience","不正義な法に対して非暴力的に抵抗する道徳的権利","倫理学・政治哲学","North_America",1849,"https://en.wikipedia.org/wiki/Civil_disobedience",now(),now()),
    (uid(),"義務に基づく権利論","Rights-Based Theory","道徳的権利を義務の根拠とするロナルド・ドウォーキンらの立場","倫理学・政治哲学","North_America",1977,"https://en.wikipedia.org/wiki/Rights",now(),now()),
    (uid(),"プロスペクト理論と倫理","Prospect Theory and Ethics","カーネマンらの損失回避バイアスが道徳的判断に与える影響の研究","倫理学・政治哲学","North_America",1979,"https://en.wikipedia.org/wiki/Prospect_theory",now(),now()),
    (uid(),"倫理的利己主義","Ethical Egoism","自己利益の最大化が道徳的に正しいとする立場","倫理学・政治哲学","Western_Europe",1874,"https://en.wikipedia.org/wiki/Ethical_egoism",now(),now()),
    (uid(),"道徳心理学","Moral Psychology","道徳的判断・動機・感情を経験的に研究する学際的分野","倫理学・政治哲学","North_America",1980,"https://en.wikipedia.org/wiki/Moral_psychology",now(),now()),

    # 大陸哲学・現象学 +41
    (uid(),"時間意識","Time-Consciousness","フッサールが分析した過去把持・原印象・予持からなる内的時間経験の構造","大陸哲学・現象学","Western_Europe",1905,"https://en.wikipedia.org/wiki/Internal_time-consciousness",now(),now()),
    (uid(),"現象学的還元","Phenomenological Reduction","自然的態度を括弧に入れ意識の構造を記述するフッサールの方法論的手続き","大陸哲学・現象学","Western_Europe",1913,"https://en.wikipedia.org/wiki/Bracketing_(phenomenology)",now(),now()),
    (uid(),"生活世界","Lifeworld","理論以前の直接的経験の場としてフッサールが記述した日常的世界","大陸哲学・現象学","Western_Europe",1936,"https://en.wikipedia.org/wiki/Lifeworld",now(),now()),
    (uid(),"配慮","Care (Sorge)","ハイデガーが現存在の根本的存在様式として分析した気遣いと配慮の構造","大陸哲学・現象学","Western_Europe",1927,"https://en.wikipedia.org/wiki/Sorge",now(),now()),
    (uid(),"現存在分析","Dasein Analysis","ハイデガーが展開した人間の存在様式を世界内存在として分析する手法","大陸哲学・現象学","Western_Europe",1927,"https://en.wikipedia.org/wiki/Dasein",now(),now()),
    (uid(),"頽落","Thrownness and Fallenness","ハイデガーにおける現存在が世間に埋没し自己を喪失する在り方","大陸哲学・現象学","Western_Europe",1927,"https://en.wikipedia.org/wiki/Thrownness",now(),now()),
    (uid(),"非本来性","Inauthenticity","ハイデガーにおける「ひと」への埋没による自己喪失の存在様式","大陸哲学・現象学","Western_Europe",1927,"https://en.wikipedia.org/wiki/Authenticity_(philosophy)",now(),now()),
    (uid(),"情状性","Mood (Stimmung)","ハイデガーが世界との根本的関与として分析した気分の存在論的性格","大陸哲学・現象学","Western_Europe",1927,"https://en.wikipedia.org/wiki/Stimmung",now(),now()),
    (uid(),"アンガージュマン","Engagement (Sartre)","サルトルが提唱する実存主義的政治・社会参加の概念","大陸哲学・現象学","Western_Europe",1945,"https://en.wikipedia.org/wiki/Engagement_(political)",now(),now()),
    (uid(),"状況","Situation (Beauvoir)","ボーヴォワールが分析する自由の行使を条件づける具体的な社会的状況","大陸哲学・現象学","Western_Europe",1949,"https://en.wikipedia.org/wiki/Simone_de_Beauvoir",now(),now()),
    (uid(),"反抗する人間","Rebel (Camus)","カミュが描く不条理に抗い反抗することで意味を創造する人間像","大陸哲学・現象学","Western_Europe",1951,"https://en.wikipedia.org/wiki/The_Rebel_(book)",now(),now()),
    (uid(),"地平融合","Fusion of Horizons","ガダマーが提唱する解釈において過去と現在の意味地平が融合する過程","大陸哲学・現象学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Fusion_of_horizons",now(),now()),
    (uid(),"作動的歴史","Effective History","ガダマーにおける過去の伝統が現在の解釈に無意識に作用する概念","大陸哲学・現象学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Wirkungsgeschichte",now(),now()),
    (uid(),"テクスト自律性","Autonomy of the Text","リクールが論じる著者意図から切り離されたテクスト固有の意味の次元","大陸哲学・現象学","Western_Europe",1973,"https://en.wikipedia.org/wiki/Paul_Ric%C5%93ur",now(),now()),
    (uid(),"物語的自己同一性","Narrative Identity","リクールが論じる自己は語りによって構成されるという自己理解の枠組","大陸哲学・現象学","Western_Europe",1990,"https://en.wikipedia.org/wiki/Narrative_identity",now(),now()),
    (uid(),"生権力","Biopower","フーコーが論じる近代国家による人口・身体・生命の管理・規律化の権力","大陸哲学・現象学","Western_Europe",1976,"https://en.wikipedia.org/wiki/Biopower",now(),now()),
    (uid(),"統治性","Governmentality","フーコーが提唱する人口を対象とした合理的な統治の技法と知","大陸哲学・現象学","Western_Europe",1978,"https://en.wikipedia.org/wiki/Governmentality",now(),now()),
    (uid(),"リゾーム","Rhizome (philosophy)","ドゥルーズ＝ガタリが提唱する根茎型の非階層的思考・存在のモデル","大陸哲学・現象学","Western_Europe",1980,"https://en.wikipedia.org/wiki/Rhizome_(philosophy)",now(),now()),
    (uid(),"器官なき身体","Body without Organs","ドゥルーズ＝ガタリにおける組織化・層化に抵抗する欲望の平面","大陸哲学・現象学","Western_Europe",1980,"https://en.wikipedia.org/wiki/Body_without_organs",now(),now()),
    (uid(),"例外状態","State of Exception","アガンベンが論じる法秩序が停止された主権的決断の空間","大陸哲学・現象学","Western_Europe",2003,"https://en.wikipedia.org/wiki/State_of_exception",now(),now()),
    (uid(),"ホモ・サケル","Homo Sacer","アガンベンが論じる法的保護を剥奪された「剥き出しの生」を生きる者","大陸哲学・現象学","Western_Europe",1995,"https://en.wikipedia.org/wiki/Homo_Sacer",now(),now()),
    (uid(),"消尽","Exhaustion (Deleuze)","ドゥルーズが可能性そのものを使い果たした状態として分析する概念","大陸哲学・現象学","Western_Europe",1992,"https://en.wikipedia.org/wiki/Gilles_Deleuze",now(),now()),
    (uid(),"エクリチュール","Écriture","デリダが提唱する音声中心主義を脱構築する痕跡としての書き言葉の概念","大陸哲学・現象学","Western_Europe",1967,"https://en.wikipedia.org/wiki/%C3%89criture",now(),now()),
    (uid(),"パロール","Parole (Saussure)","ソシュールが区別する言語体系（ラング）に対する個別の発話行為","大陸哲学・現象学","Western_Europe",1916,"https://en.wikipedia.org/wiki/Langue_and_parole",now(),now()),
    (uid(),"過剰","Excess (Bataille)","バタイユが論じる生産・蓄積の経済に対する蕩尽・消費の過剰の哲学","大陸哲学・現象学","Western_Europe",1949,"https://en.wikipedia.org/wiki/Georges_Bataille",now(),now()),
    (uid(),"真理事件","Truth Event","バディウが論じる既存の知識秩序を断絶させる偶発的な真理の出現","大陸哲学・現象学","Western_Europe",1988,"https://en.wikipedia.org/wiki/Alain_Badiou",now(),now()),
    (uid(),"感性の分割","Distribution of the Sensible","ランシエールが論じる何が可視・可聴とされるかを規定する政治的秩序","大陸哲学・現象学","Western_Europe",2000,"https://en.wikipedia.org/wiki/Jacques_Ranci%C3%A8re",now(),now()),
    (uid(),"イデオロギー批判","Ideology Critique","マルクス以来のジジェクらによる社会的幻想としてのイデオロギー分析","大陸哲学・現象学","Western_Europe",1989,"https://en.wikipedia.org/wiki/Slavoj_%C5%BDi%C5%BEek",now(),now()),
    (uid(),"否定弁証法","Negative Dialectics","アドルノが提唱する同一性思考を批判し非同一的なものを保持する弁証法","大陸哲学・現象学","Western_Europe",1966,"https://en.wikipedia.org/wiki/Negative_dialectics",now(),now()),
    (uid(),"アウラ","Aura (Benjamin)","ベンヤミンが論じる芸術作品の今ここにしか宿らない真正な存在感","大陸哲学・現象学","Western_Europe",1935,"https://en.wikipedia.org/wiki/Aura_(Walter_Benjamin)",now(),now()),
    (uid(),"ハビトゥス","Habitus","ブルデューが提唱する社会的位置によって形成された行動・認識の傾向性","大陸哲学・現象学","Western_Europe",1972,"https://en.wikipedia.org/wiki/Habitus_(sociology)",now(),now()),
    (uid(),"持続","Duration (Bergson)","ベルクソンが論じる空間化・数量化に還元できない内的時間経験の質的流れ","大陸哲学・現象学","Western_Europe",1889,"https://en.wikipedia.org/wiki/Duration_(Bergson)",now(),now()),
    (uid(),"純粋記憶","Pure Memory (Bergson)","ベルクソンにおける身体とは独立した過去そのものの虚在的保存","大陸哲学・現象学","Western_Europe",1896,"https://en.wikipedia.org/wiki/Matter_and_Memory",now(),now()),
    (uid(),"西田哲学","Nishida Philosophy","西田幾多郎が提唱する「純粋経験」「絶対無の場所」を核とする独自の哲学体系","大陸哲学・現象学","East_Asia",1911,"https://en.wikipedia.org/wiki/Kitaro_Nishida",now(),now()),
    (uid(),"絶対矛盾的自己同一","Absolute Contradictory Self-Identity","西田哲学において対立するものが統一される弁証法的論理","大陸哲学・現象学","East_Asia",1939,"https://en.wikipedia.org/wiki/Kitaro_Nishida",now(),now()),
    (uid(),"悪の陳腐さ","Banality of Evil","ハンナ・アーレントがアイヒマン裁判を通じて論じた無思考による悪の平凡性","大陸哲学・現象学","North_America",1963,"https://en.wikipedia.org/wiki/Banality_of_evil",now(),now()),
    (uid(),"公共性","Public Realm (Arendt)","アーレントが複数の人間の行為と言論の空間として描く政治的領域","大陸哲学・現象学","North_America",1958,"https://en.wikipedia.org/wiki/Hannah_Arendt",now(),now()),
    (uid(),"レヴィナスの顔","Face of the Other (Levinas)","レヴィナスが倫理の根源として位置づける他者の顔の呼びかけ","大陸哲学・現象学","Western_Europe",1961,"https://en.wikipedia.org/wiki/Face_of_the_Other",now(),now()),
    (uid(),"身体図式","Body Schema","メルロ＝ポンティが分析する身体が空間を無意識に組織化する知覚的能力","大陸哲学・現象学","Western_Europe",1945,"https://en.wikipedia.org/wiki/Body_schema",now(),now()),
    (uid(),"間身体性","Intercorporeality","メルロ＝ポンティが論じる複数の身体が共有する知覚的・運動的次元","大陸哲学・現象学","Western_Europe",1945,"https://en.wikipedia.org/wiki/Maurice_Merleau-Ponty",now(),now()),
    (uid(),"現象的場","Phenomenal Field","心理学・現象学において経験者の視点から記述される経験の全体的布置","大陸哲学・現象学","Western_Europe",1945,"https://en.wikipedia.org/wiki/Phenomenology_(philosophy)",now(),now()),

    # 分析哲学・心の哲学 +31
    (uid(),"固定指示子","Rigid Designator","クリプキが提唱するすべての可能世界で同一の対象を指示する表現","分析哲学・心の哲学","North_America",1980,"https://en.wikipedia.org/wiki/Rigid_designator",now(),now()),
    (uid(),"様相実在論","Modal Realism","デイヴィッド・ルイスが提唱するすべての可能世界が同等に実在するという立場","分析哲学・心の哲学","North_America",1986,"https://en.wikipedia.org/wiki/Modal_realism",now(),now()),
    (uid(),"意味の外在主義","Semantic Externalism","語の意味は話者の心的状態ではなく外部環境によって決定されるパトナムらの立場","分析哲学・心の哲学","North_America",1975,"https://en.wikipedia.org/wiki/Semantic_externalism",now(),now()),
    (uid(),"双子地球","Twin Earth","パトナムが意味の外在主義を論じるための思考実験","分析哲学・心の哲学","North_America",1975,"https://en.wikipedia.org/wiki/Twin_Earth_thought_experiment",now(),now()),
    (uid(),"行為の因果説","Causal Theory of Action","行為は欲求と信念の因果的連鎖によって生じるとするデイヴィッドソンらの立場","分析哲学・心の哲学","North_America",1963,"https://en.wikipedia.org/wiki/Causal_theory_of_action",now(),now()),
    (uid(),"証言的認識論","Testimony Epistemology","他者からの証言を知識の正当な源泉として分析する認識論の分野","分析哲学・心の哲学","Western_Europe",1987,"https://en.wikipedia.org/wiki/Testimony_(epistemology)",now(),now()),
    (uid(),"認識的不正義","Epistemic Injustice","ミランダ・フリッカーが論じる証言的・解釈的不正義による知的排除","分析哲学・心の哲学","Western_Europe",2007,"https://en.wikipedia.org/wiki/Epistemic_injustice",now(),now()),
    (uid(),"証言的不正義","Testimonial Injustice","話者が信用毀損により証言者として認められない不正義の形態","分析哲学・心の哲学","Western_Europe",2007,"https://en.wikipedia.org/wiki/Epistemic_injustice",now(),now()),
    (uid(),"解釈的不正義","Hermeneutical Injustice","集団的意味資源の欠如により自分の経験を理解・表現できない不正義","分析哲学・心の哲学","Western_Europe",2007,"https://en.wikipedia.org/wiki/Epistemic_injustice",now(),now()),
    (uid(),"法の概念","Concept of Law","H.L.A.ハートが法を一次的・二次的ルールの結合として分析した著作・概念","分析哲学・心の哲学","Western_Europe",1961,"https://en.wikipedia.org/wiki/The_Concept_of_Law",now(),now()),
    (uid(),"計算機能主義","Computational Functionalism","心的状態はプログラムのように計算的に機能的役割で定義されるという立場","分析哲学・心の哲学","North_America",1960,"https://en.wikipedia.org/wiki/Functionalism_(philosophy_of_mind)",now(),now()),
    (uid(),"拡張された心","Extended Mind","クラーク＝チャーマーズが提唱する認知過程が頭蓋外環境まで拡張するという論","分析哲学・心の哲学","Western_Europe",1998,"https://en.wikipedia.org/wiki/Extended_mind_thesis",now(),now()),
    (uid(),"体化認知","Embodied Cognition","認知は身体と環境との動的相互作用に根ざすという認知科学・哲学の立場","分析哲学・心の哲学","North_America",1991,"https://en.wikipedia.org/wiki/Embodied_cognition",now(),now()),
    (uid(),"マリーの部屋","Mary's Room","フランク・ジャクソンが提唱するクオリアと物理的知識の関係を問う思考実験","分析哲学・心の哲学","North_America",1982,"https://en.wikipedia.org/wiki/Mary%27s_room",now(),now()),
    (uid(),"哲学的ゾンビ","Philosophical Zombie","クオリアを欠いた行動的に同一な存在の概念的可能性を問う思考実験","分析哲学・心の哲学","North_America",1996,"https://en.wikipedia.org/wiki/Philosophical_zombie",now(),now()),
    (uid(),"情報統合理論","Integrated Information Theory","トノーニが提唱する意識の度合いを情報統合量Φで測定する意識理論","分析哲学・心の哲学","North_America",2004,"https://en.wikipedia.org/wiki/Integrated_information_theory",now(),now()),
    (uid(),"グローバルワークスペース理論","Global Workspace Theory","バーズが提唱する意識を情報を大域的に共有するワークスペースとして捉える理論","分析哲学・心の哲学","North_America",1988,"https://en.wikipedia.org/wiki/Global_workspace_theory",now(),now()),
    (uid(),"意識の難問","Hard Problem of Consciousness","チャーマーズが定式化する物理過程がなぜ主観的経験を生むかという問い","分析哲学・心の哲学","North_America",1995,"https://en.wikipedia.org/wiki/Hard_problem_of_consciousness",now(),now()),
    (uid(),"自由間接話法の哲学","Free Indirect Discourse Philosophy","小説的視点の哲学的分析として意識と語りの関係を論じる","分析哲学・心の哲学","Western_Europe",1990,"https://en.wikipedia.org/wiki/Free_indirect_speech",now(),now()),
    (uid(),"スーパーヴィニアンス","Supervenience","心的性質は物理的性質に伴随し独立変化しないという関係","分析哲学・心の哲学","North_America",1970,"https://en.wikipedia.org/wiki/Supervenience",now(),now()),
    (uid(),"二次元意味論","Two-Dimensional Semantics","チャーマーズらが提唱する語に二つの意味次元を与える意味論","分析哲学・心の哲学","North_America",2006,"https://en.wikipedia.org/wiki/Two-dimensional_semantics",now(),now()),
    (uid(),"言語行為理論","Speech Act Theory","オースティン＝サールによる発話が世界に何かをなすという語用論の理論","分析哲学・心の哲学","Western_Europe",1962,"https://en.wikipedia.org/wiki/Speech_act_theory",now(),now()),
    (uid(),"命題的態度","Propositional Attitude","信念・欲求・恐れなど命題内容に向けられた心的状態の総称","分析哲学・心の哲学","Western_Europe",1905,"https://en.wikipedia.org/wiki/Propositional_attitude",now(),now()),
    (uid(),"指向性","Intentionality","心的状態が対象に向けられているという意識の根本的性格","分析哲学・心の哲学","Western_Europe",1874,"https://en.wikipedia.org/wiki/Intentionality",now(),now()),
    (uid(),"解消主義","Eliminativism","民俗心理学の概念（信念・欲求）を科学的に排除すべきとするチャーチランドらの立場","分析哲学・心の哲学","North_America",1981,"https://en.wikipedia.org/wiki/Eliminative_materialism",now(),now()),
    (uid(),"非還元的物理主義","Non-Reductive Physicalism","心的状態は物理的だが物理概念に還元できないという立場","分析哲学・心の哲学","North_America",1970,"https://en.wikipedia.org/wiki/Non-reductive_physicalism",now(),now()),
    (uid(),"随伴現象説","Epiphenomenalism","意識的経験は物理過程の副産物で因果的役割を持たないという立場","分析哲学・心の哲学","Western_Europe",1879,"https://en.wikipedia.org/wiki/Epiphenomenalism",now(),now()),
    (uid(),"自由意志と決定論","Free Will and Determinism","意志の自由と自然法則の因果的決定論の両立可能性を問う古典的問題","分析哲学・心の哲学","Western_Europe",1700,"https://en.wikipedia.org/wiki/Free_will",now(),now()),
    (uid(),"反事実的条件文","Counterfactual Conditional","「もし〜ならば〜だったであろう」という仮定法的命題の論理的分析","分析哲学・心の哲学","North_America",1973,"https://en.wikipedia.org/wiki/Counterfactual_conditional",now(),now()),
    (uid(),"解釈的慈善原理","Principle of Charity","他者の発言を最も合理的に解釈することを認識論・言語哲学の方法とする原理","分析哲学・心の哲学","North_America",1960,"https://en.wikipedia.org/wiki/Principle_of_charity",now(),now()),
    (uid(),"認識論的謙虚さ","Epistemic Humility","自分の認知限界を自覚し過剰な確信を慎む認識論的徳","分析哲学・心の哲学","North_America",2001,"https://en.wikipedia.org/wiki/Epistemic_humility",now(),now()),

    # 宗教学・神学 +30
    (uid(),"宗教現象学","Phenomenology of Religion","ファン・デル・レーウらが確立した宗教経験の意味構造を記述する学問","宗教学・神学","Global_Synthesis",1933,"https://en.wikipedia.org/wiki/Phenomenology_of_religion",now(),now()),
    (uid(),"解放の神学","Liberation Theology","ラテンアメリカで発展した貧者の視点から聖書を読む神学的運動","宗教学・神学","Latin_America",1968,"https://en.wikipedia.org/wiki/Liberation_theology",now(),now()),
    (uid(),"フェミニスト神学","Feminist Theology","ジェンダー平等の視点から神学的伝統を再解釈する神学","宗教学・神学","North_America",1970,"https://en.wikipedia.org/wiki/Feminist_theology",now(),now()),
    (uid(),"黒人神学","Black Theology","ジェームズ・コーンが提唱するアフリカ系アメリカ人の解放を中心とする神学","宗教学・神学","North_America",1969,"https://en.wikipedia.org/wiki/Black_theology",now(),now()),
    (uid(),"悪の問題","Problem of Evil","全能・全善の神の存在と悪の存在の両立可能性を問う神学・哲学の問題","宗教学・神学","Western_Europe",1710,"https://en.wikipedia.org/wiki/Problem_of_evil",now(),now()),
    (uid(),"カラーム宇宙論的論証","Kalam Cosmological Argument","宇宙の始まりから創造者の存在を論じるイスラーム由来の哲学的論証","宗教学・神学","West_Asia_North_Africa",900,"https://en.wikipedia.org/wiki/Kalam_cosmological_argument",now(),now()),
    (uid(),"ヴェーダーンタ哲学","Vedanta Philosophy","ウパニシャッドを基盤としブラフマン＝アートマン同一性を論じるヒンドゥー哲学","宗教学・神学","South_Asia",-700,"https://en.wikipedia.org/wiki/Vedanta",now(),now()),
    (uid(),"アドヴァイタ・ヴェーダーンタ","Advaita Vedanta","シャンカラが確立したブラフマンと個我の不二一元論を説くヒンドゥー哲学","宗教学・神学","South_Asia",800,"https://en.wikipedia.org/wiki/Advaita_Vedanta",now(),now()),
    (uid(),"仏教認識論","Buddhist Epistemology","ディグナーガ・ダルマキールティらが展開した知覚・推論の厳密な分析","宗教学・神学","South_Asia",500,"https://en.wikipedia.org/wiki/Buddhist_epistemology",now(),now()),
    (uid(),"空観","Śūnyatā","龍樹が体系化した自性の欠如・空を説く大乗仏教の中心概念","宗教学・神学","South_Asia",200,"https://en.wikipedia.org/wiki/%C5%9A%C5%ABnyat%C4%81",now(),now()),
    (uid(),"エンゲイジド・ブッディズム","Engaged Buddhism","ティク・ナット・ハンらが提唱する社会変革へのコミットを含む現代仏教","宗教学・神学","East_Asia",1963,"https://en.wikipedia.org/wiki/Engaged_Buddhism",now(),now()),
    (uid(),"新宗教運動","New Religious Movements","既成宗教と区別される現代の新たな宗教集団・信仰運動の総称","宗教学・神学","Global_Synthesis",1970,"https://en.wikipedia.org/wiki/New_religious_movement",now(),now()),
    (uid(),"世俗化理論","Secularization Theory","近代化とともに宗教が衰退するというウェーバー・バーガーらの理論","宗教学・神学","Global_Synthesis",1967,"https://en.wikipedia.org/wiki/Secularization",now(),now()),
    (uid(),"宗教多元主義","Religious Pluralism","ジョン・ヒックらが提唱する複数の宗教が同等に真理に接近するという立場","宗教学・神学","Global_Synthesis",1973,"https://en.wikipedia.org/wiki/Religious_pluralism",now(),now()),
    (uid(),"宗教的排他主義","Religious Exclusivism","唯一の宗教のみが真理や救済の道を持つとする立場","宗教学・神学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Exclusivism",now(),now()),
    (uid(),"宗教包括主義","Religious Inclusivism","自宗教が真理だが他宗教も部分的に真理を含むとする立場","宗教学・神学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Inclusivism",now(),now()),
    (uid(),"スーフィズム","Sufism","神との神秘的合一を目指すイスラームの神秘主義思想と実践","宗教学・神学","West_Asia_North_Africa",900,"https://en.wikipedia.org/wiki/Sufism",now(),now()),
    (uid(),"カバラー","Kabbalah","ユダヤ教の神秘主義的伝統で神の本性と宇宙の構造を解読しようとする思想","宗教学・神学","West_Asia_North_Africa",1200,"https://en.wikipedia.org/wiki/Kabbalah",now(),now()),
    (uid(),"神秘体験","Mystical Experience","神・宇宙・超越的実在との合一感を伴う宗教的・精神的経験","宗教学・神学","Global_Synthesis",1902,"https://en.wikipedia.org/wiki/Mystical_experience",now(),now()),
    (uid(),"タブー","Taboo","特定の行為・対象・語への宗教的・文化的禁忌とその機能","宗教学・神学","Global_Synthesis",1871,"https://en.wikipedia.org/wiki/Taboo",now(),now()),
    (uid(),"儀礼の通過理論","Rites of Passage","アルノルト・ファン・ヘネップが提唱する分離・過渡・統合の三段階からなる通過儀礼","宗教学・神学","Western_Europe",1909,"https://en.wikipedia.org/wiki/Rites_of_passage",now(),now()),
    (uid(),"コミュニタス","Communitas","ヴィクター・ターナーが論じる通過儀礼の過渡期に生じる平等的共同性","宗教学・神学","Western_Europe",1969,"https://en.wikipedia.org/wiki/Communitas",now(),now()),
    (uid(),"神道の概念","Shinto Concepts","清め・ケガレ・ムスビ・マツリ等の神道の核心的宗教概念","宗教学・神学","East_Asia",700,"https://en.wikipedia.org/wiki/Shinto",now(),now()),
    (uid(),"アニミズム","Animism","自然物・現象に精霊・魂が宿るとする世界観","宗教学・神学","Global_Synthesis",1871,"https://en.wikipedia.org/wiki/Animism",now(),now()),
    (uid(),"シャーマニズム","Shamanism","トランス状態で精霊界と交信し治癒・占いを行う宗教的実践","宗教学・神学","Global_Synthesis",1700,"https://en.wikipedia.org/wiki/Shamanism",now(),now()),
    (uid(),"宗教的経験の多様性","Varieties of Religious Experience","ウィリアム・ジェームズによる宗教的経験の心理学的・哲学的分析","宗教学・神学","North_America",1902,"https://en.wikipedia.org/wiki/The_Varieties_of_Religious_Experience",now(),now()),
    (uid(),"ヌミノーゼ","Numinous","ルドルフ・オットーが論じる畏怖と魅惑を同時に呼び起こす聖なるものの経験","宗教学・神学","Western_Europe",1917,"https://en.wikipedia.org/wiki/Numinous",now(),now()),
    (uid(),"宗教社会学","Sociology of Religion","デュルケーム・ウェーバーらが確立した宗教の社会的機能を分析する学問","宗教学・神学","Global_Synthesis",1912,"https://en.wikipedia.org/wiki/Sociology_of_religion",now(),now()),
    (uid(),"無神論","Atheism","神や超自然的存在の実在を否定する立場","宗教学・神学","Global_Synthesis",1770,"https://en.wikipedia.org/wiki/Atheism",now(),now()),
    (uid(),"不可知論","Agnosticism","神の存在は知ることができないとするT.H.ハクスリーの立場","宗教学・神学","Western_Europe",1869,"https://en.wikipedia.org/wiki/Agnosticism",now(),now()),

    # 美学・芸術哲学 +22
    (uid(),"写真の美学","Photography Aesthetics","写真の芸術的地位・現実との関係・インデックス性を論じる美学","美学・芸術哲学","Western_Europe",1980,"https://en.wikipedia.org/wiki/Photography_and_the_theory_of_art",now(),now()),
    (uid(),"映画の美学","Film Aesthetics","映画を芸術として分析するアンドレ・バザン・マルコム・タービーらの美学","美学・芸術哲学","Western_Europe",1945,"https://en.wikipedia.org/wiki/Film_theory",now(),now()),
    (uid(),"デジタルアートの哲学","Philosophy of Digital Art","デジタル技術が芸術の性質・オリジナリティ・身体性に与える影響の哲学的分析","美学・芸術哲学","Global_Synthesis",1995,"https://en.wikipedia.org/wiki/Digital_art",now(),now()),
    (uid(),"AIと創造性","AI and Creativity","人工知能が生成する作品の美的価値・創造性・著作権を論じる美学の問題","美学・芸術哲学","Global_Synthesis",2017,"https://en.wikipedia.org/wiki/Computational_creativity",now(),now()),
    (uid(),"パフォーマンスアート理論","Performance Art Theory","パフォーマンスアートの身体性・時間性・観客との関係を論じる芸術理論","美学・芸術哲学","North_America",1970,"https://en.wikipedia.org/wiki/Performance_art",now(),now()),
    (uid(),"音楽の存在論","Ontology of Music","音楽作品の同一性・抽象性・実例化の問題を論じるグッドマンらの哲学","美学・芸術哲学","North_America",1968,"https://en.wikipedia.org/wiki/Philosophy_of_music",now(),now()),
    (uid(),"ソマエステティクス","Somaesthetics","リチャード・シュスターマンが提唱する身体経験を美的探求の中心とする理論","美学・芸術哲学","North_America",1992,"https://en.wikipedia.org/wiki/Somaesthetics",now(),now()),
    (uid(),"中国美学","Chinese Aesthetics","意境・写意・禅の美意識等の中国芸術の美的理念と理論","美学・芸術哲学","East_Asia",300,"https://en.wikipedia.org/wiki/Chinese_aesthetics",now(),now()),
    (uid(),"ラサ理論","Rasa Theory","バラタ・ムニが確立したインド古典芸術における9種の感情と美的体験の理論","美学・芸術哲学","South_Asia",-200,"https://en.wikipedia.org/wiki/Rasa_(aesthetics)",now(),now()),
    (uid(),"アフリカの美学","African Aesthetics","アフリカの芸術実践における美・機能・共同体的意味の理論","美学・芸術哲学","Sub_Saharan_Africa",1990,"https://en.wikipedia.org/wiki/African_art",now(),now()),
    (uid(),"マンガ・アニメの美学","Manga and Anime Aesthetics","日本のマンガとアニメの独自の視覚表現・物語構造・キャラクター美学","美学・芸術哲学","East_Asia",1960,"https://en.wikipedia.org/wiki/Manga",now(),now()),
    (uid(),"ミニマリズム","Minimalism","芸術・音楽・デザインにおける素材と形式の徹底的な削減を特徴とする運動","美学・芸術哲学","North_America",1960,"https://en.wikipedia.org/wiki/Minimalism",now(),now()),
    (uid(),"コンセプチュアルアート","Conceptual Art","概念やアイデアを素材とし伝統的なオブジェを超えた芸術形式","美学・芸術哲学","North_America",1967,"https://en.wikipedia.org/wiki/Conceptual_art",now(),now()),
    (uid(),"制度的芸術定義","Institutional Theory of Art","アーサー・ダントーとジョージ・ディッキーが提唱する芸術界による芸術の制度的定義","美学・芸術哲学","North_America",1974,"https://en.wikipedia.org/wiki/Institutional_theory_of_art",now(),now()),
    (uid(),"表現主義の美学","Expressionist Aesthetics","クローチェらによる芸術を内的表現の外化として捉える美学","美学・芸術哲学","Western_Europe",1902,"https://en.wikipedia.org/wiki/Expressionism",now(),now()),
    (uid(),"崇高の概念","Concept of the Sublime","カントが分析する数学的・力学的崇高としての圧倒的・測定不能な美的体験","美学・芸術哲学","Western_Europe",1790,"https://en.wikipedia.org/wiki/Sublime_(philosophy)",now(),now()),
    (uid(),"芸術としての自然","Nature as Art","自然美を芸術と同等に扱うカントやアドルノの自然美学","美学・芸術哲学","Western_Europe",1790,"https://en.wikipedia.org/wiki/Natural_beauty",now(),now()),
    (uid(),"参加型美学","Participatory Aesthetics","芸術作品への観客・市民の積極的参加を重視する現代芸術理論","美学・芸術哲学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Relational_art",now(),now()),
    (uid(),"美的多元主義","Aesthetic Pluralism","唯一の美的基準を否定し複数の美的価値基準の共存を認める立場","美学・芸術哲学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Aesthetic_pluralism",now(),now()),
    (uid(),"模倣と表象","Mimesis and Representation","アリストテレス由来の芸術が現実を模倣・表象するという理論の系譜","美学・芸術哲学","Western_Europe",-350,"https://en.wikipedia.org/wiki/Mimesis",now(),now()),
    (uid(),"間テクスト性の美学","Intertextuality in Aesthetics","クリステヴァらが論じる芸術作品が他の作品・テクストを引用・変容する構造","美学・芸術哲学","Western_Europe",1967,"https://en.wikipedia.org/wiki/Intertextuality",now(),now()),
    (uid(),"美的経験","Aesthetic Experience","デューイ・グッドマンらが分析する日常とは質的に異なる集中した美的鑑賞の体験","美学・芸術哲学","North_America",1934,"https://en.wikipedia.org/wiki/Aesthetic_experience",now(),now()),

    # 古典学・古典文学 +30
    (uid(),"ホメロス問題","Homeric Question","イリアスとオデュッセイアが単独作者による作品かを問う古典学の論争","古典学・古典文学","Western_Europe",1795,"https://en.wikipedia.org/wiki/Homeric_question",now(),now()),
    (uid(),"口承詩学","Oral-Formulaic Theory","ミルマン・パリーとアルバート・ロードが確立した口承詩の定型句・即興性の理論","古典学・古典文学","North_America",1930,"https://en.wikipedia.org/wiki/Oral-formulaic_composition",now(),now()),
    (uid(),"ギリシア悲劇詩学","Poetics of Greek Tragedy","アリストテレスが「詩学」で分析したハマルティア・カタルシス・ミュトスの構造","古典学・古典文学","Western_Europe",-335,"https://en.wikipedia.org/wiki/Poetics_(Aristotle)",now(),now()),
    (uid(),"ウェルギリウスの農耕詩","Georgics (Virgil)","農業・自然・ローマの運命を詠ったウェルギリウスの教訓叙事詩","古典学・古典文学","Western_Europe",-29,"https://en.wikipedia.org/wiki/Georgics",now(),now()),
    (uid(),"オウィディウスの変身物語","Metamorphoses (Ovid)","変身をテーマに神話を集大成したオウィディウスのラテン語叙事詩","古典学・古典文学","Western_Europe",8,"https://en.wikipedia.org/wiki/Metamorphoses",now(),now()),
    (uid(),"キケロの修辞学","Ciceronian Rhetoric","弁論術を道徳・市民的美徳と結びつけたキケロの修辞学的思想","古典学・古典文学","Western_Europe",-55,"https://en.wikipedia.org/wiki/Cicero",now(),now()),
    (uid(),"タキトゥスの歴史叙述","Tacitean Historiography","帝政ローマの政治的腐敗を鋭い心理分析で描いたタキトゥスの歴史記述","古典学・古典文学","Western_Europe",98,"https://en.wikipedia.org/wiki/Tacitus",now(),now()),
    (uid(),"プルタルコスの英雄伝","Plutarch's Lives","ギリシア・ローマの偉人を対比させた伝記集で後世の人物伝の規範となった著作","古典学・古典文学","Western_Europe",100,"https://en.wikipedia.org/wiki/Parallel_Lives",now(),now()),
    (uid(),"写本伝承研究","Manuscript Transmission","古典テクストが中世を通じて筆写・保存・変容してきた過程の研究","古典学・古典文学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Textual_criticism",now(),now()),
    (uid(),"碑文学","Epigraphy","石・金属等に刻まれた碑文を解読・分析する古典学の補助学","古典学・古典文学","Western_Europe",1700,"https://en.wikipedia.org/wiki/Epigraphy",now(),now()),
    (uid(),"ダンテの神曲","Divine Comedy (Dante)","地獄・煉獄・天国を旅するダンテの中世イタリア語叙事詩","古典学・古典文学","Western_Europe",1320,"https://en.wikipedia.org/wiki/Divine_Comedy",now(),now()),
    (uid(),"ドン・キホーテ","Don Quixote","セルバンテスが著した最初の近代小説とされるスペイン語の大作","古典学・古典文学","Western_Europe",1605,"https://en.wikipedia.org/wiki/Don_Quixote",now(),now()),
    (uid(),"マハーバーラタ","Mahabharata","インド二大叙事詩の一つで哲学・法・倫理を含む膨大な古典文学","古典学・古典文学","South_Asia",-400,"https://en.wikipedia.org/wiki/Mahabharata",now(),now()),
    (uid(),"ラーマーヤナ","Ramayana","ヴァールミーキが著したとされるインドの聖王ラーマの物語叙事詩","古典学・古典文学","South_Asia",-200,"https://en.wikipedia.org/wiki/Ramayana",now(),now()),
    (uid(),"ギルガメシュ叙事詩","Epic of Gilgamesh","現存最古の文学作品とされるメソポタミアの英雄叙事詩","古典学・古典文学","West_Asia_North_Africa",-2100,"https://en.wikipedia.org/wiki/Epic_of_Gilgamesh",now(),now()),
    (uid(),"千夜一夜物語","One Thousand and One Nights","アラビア語の説話集で世界文学に多大な影響を与えた中東古典文学","古典学・古典文学","West_Asia_North_Africa",800,"https://en.wikipedia.org/wiki/One_Thousand_and_One_Nights",now(),now()),
    (uid(),"ルーミーのマスナヴィー","Rumi's Masnavi","ジャラールッディーン・ルーミーが著したペルシア語神秘主義詩の最高傑作","古典学・古典文学","West_Asia_North_Africa",1258,"https://en.wikipedia.org/wiki/Masnavi",now(),now()),
    (uid(),"シャーナーメ","Shahnameh","フェルドウスィーがペルシアの神話・英雄・王朝史を詠った叙事詩","古典学・古典文学","West_Asia_North_Africa",1010,"https://en.wikipedia.org/wiki/Shahnameh",now(),now()),
    (uid(),"スンジャータ叙事詩","Epic of Sundiata","マリ帝国の創始者スンジャータを讃えるマンデ族の口承叙事詩","古典学・古典文学","Sub_Saharan_Africa",1235,"https://en.wikipedia.org/wiki/Epic_of_Sundiata",now(),now()),
    (uid(),"ポポル・ヴフ","Popol Vuh","マヤ・キチェ族の創世神話と歴史を記録したメソアメリカの聖典","古典学・古典文学","Latin_America",1701,"https://en.wikipedia.org/wiki/Popol_Vuh",now(),now()),
    (uid(),"古事記","Kojiki","712年に成立した日本最古の歴史書・神話集","古典学・古典文学","East_Asia",712,"https://en.wikipedia.org/wiki/Kojiki",now(),now()),
    (uid(),"カーリダーサ","Kalidasa","「メーガドゥータ」「シャクンタラー」等を著したサンスクリット文学最高の詩人","古典学・古典文学","South_Asia",400,"https://en.wikipedia.org/wiki/Kalidasa",now(),now()),
    (uid(),"ボッカッチョのデカメロン","Decameron (Boccaccio)","ペストを逃れた人々が語る100話の物語集でルネサンス文学の先駆","古典学・古典文学","Western_Europe",1353,"https://en.wikipedia.org/wiki/The_Decameron",now(),now()),
    (uid(),"ゲーテのファウスト","Faust (Goethe)","近代的人間の知識欲・悪との契約を描くゲーテの生涯の大作","古典学・古典文学","Western_Europe",1808,"https://en.wikipedia.org/wiki/Faust_(Goethe)",now(),now()),
    (uid(),"古典学の方法論","Methodology of Classical Scholarship","版本比較・語学分析・歴史文脈化からなる古典文献研究の手法","古典学・古典文学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Classical_philology",now(),now()),
    (uid(),"ナワトル語文学","Nahuatl Literature","アステカの言語ナワトル語で書かれた詩・年代記・神話等の文学","古典学・古典文学","Latin_America",1500,"https://en.wikipedia.org/wiki/Nahuatl_literature",now(),now()),
    (uid(),"史記","Shiji","司馬遷が著した中国初の紀伝体正史で中国史学の規範となった古典","古典学・古典文学","East_Asia",-91,"https://en.wikipedia.org/wiki/Shiji",now(),now()),
    (uid(),"詩経","Book of Songs (Shijing)","孔子が編纂したとされる中国最古の詩集","古典学・古典文学","East_Asia",-600,"https://en.wikipedia.org/wiki/Classic_of_Poetry",now(),now()),
    (uid(),"源氏物語の研究","Scholarship on The Tale of Genji","紫式部の源氏物語に関する注釈・翻訳・比較文学的研究","古典学・古典文学","East_Asia",1008,"https://en.wikipedia.org/wiki/The_Tale_of_Genji",now(),now()),
    (uid(),"ヴェーダ文学","Vedic Literature","リグ・ヴェーダ等の最古のインド文学で宗教・哲学・詩の源泉","古典学・古典文学","South_Asia",-1500,"https://en.wikipedia.org/wiki/Vedas",now(),now()),
]

def main():
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA journal_mode=WAL")
    cur = con.cursor()

    existing = set(r[0] for r in cur.execute("SELECT name_en FROM humanities_concept"))
    print(f"既存件数: {len(existing)}")

    inserted = skipped = 0
    batch = []
    ts = now()

    for r in CONCEPTS:
        name_en = r[2]
        if name_en in existing:
            skipped += 1
            continue
        existing.add(name_en)
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

    total = cur.execute("SELECT COUNT(*) FROM humanities_concept").fetchone()[0]
    print(f"inserted={inserted}, skipped={skipped}")
    print(f"総件数: {total} (目標5500)")
    con.close()

if __name__ == "__main__":
    main()
