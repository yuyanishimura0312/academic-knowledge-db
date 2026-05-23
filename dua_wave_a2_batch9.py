#!/usr/bin/env python3
"""DUA Wave A2 Batch 9 — 認識論+形而上学+論理学+古典学+宗教学+美学補強"""
import sqlite3, uuid, datetime, os

DB_PATH = os.path.expanduser("~/projects/research/academic-knowledge-db/academic.db")

def uid(): return "dua_" + uuid.uuid4().hex[:12]
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()

CONCEPTS = [
    # 認識論・形而上学・論理学 (大陸哲学・現象学 / 分析哲学サブフィールド補強) +120
    (uid(),"知識の定義","Definition of Knowledge","プラトン以来「真の信念に正当化が加わったもの」として定義される知識の概念","大陸哲学・現象学","Western_Europe",-380,"https://en.wikipedia.org/wiki/Epistemology",now(),now()),
    (uid(),"ゲティア問題","Gettier Problem","知識の伝統的定義に反例を与えたゲティアの1963年論文が提起した問題","分析哲学・心の哲学","Western_Europe",1963,"https://en.wikipedia.org/wiki/Gettier_problem",now(),now()),
    (uid(),"インターナリズムとエクスターナリズム","Internalism and Externalism Epistemology","正当化の根拠が認識者の内的状態にあるか外的世界にあるかをめぐる認識論の論争","分析哲学・心の哲学","North_America",1980,"https://en.wikipedia.org/wiki/Epistemological_internalism_and_externalism",now(),now()),
    (uid(),"信頼性主義","Reliabilism","信念が信頼できるプロセスによって形成されることを正当化条件とする認識論","分析哲学・心の哲学","North_America",1979,"https://en.wikipedia.org/wiki/Reliabilism",now(),now()),
    (uid(),"基礎主義","Foundationalism","知識体系は疑いえない基礎的信念から演繹的に構築されるという認識論","分析哲学・心の哲学","Western_Europe",1641,"https://en.wikipedia.org/wiki/Foundationalism",now(),now()),
    (uid(),"コヒーレンティズム","Coherentism","信念の正当化は体系全体の整合性によるという認識論","分析哲学・心の哲学","Western_Europe",1978,"https://en.wikipedia.org/wiki/Coherentism",now(),now()),
    (uid(),"徳認識論","Virtue Epistemology","知的徳（開放性・謙虚さ等）を中心に認識的成就を評価する認識論","分析哲学・心の哲学","North_America",1980,"https://en.wikipedia.org/wiki/Virtue_epistemology",now(),now()),
    (uid(),"社会認識論","Social Epistemology","共同体・制度・権力の文脈で知識の形成・評価を分析する認識論","分析哲学・心の哲学","North_America",1987,"https://en.wikipedia.org/wiki/Social_epistemology",now(),now()),
    (uid(),"実体の形而上学","Substance Metaphysics","存在の根底に変化を通じて同一であり続ける実体があるというアリストテレス以来の形而上学","大陸哲学・現象学","Western_Europe",-350,"https://en.wikipedia.org/wiki/Substance_theory",now(),now()),
    (uid(),"本質と偶有性","Essence and Accident","存在者が必然的に持つ本質と偶然的に持つ偶有性の区別","大陸哲学・現象学","Western_Europe",-350,"https://en.wikipedia.org/wiki/Essence",now(),now()),
    (uid(),"因果性の形而上学","Metaphysics of Causation","原因と結果の関係の性質を論じるヒューム以来の形而上学","分析哲学・心の哲学","Western_Europe",1739,"https://en.wikipedia.org/wiki/Causality",now(),now()),
    (uid(),"物理主義","Physicalism","存在するすべては物理的であるという形而上学的立場","分析哲学・心の哲学","North_America",1970,"https://en.wikipedia.org/wiki/Physicalism",now(),now()),
    (uid(),"二元論","Dualism (philosophy)","心と身体は異なる実体であるというデカルト以来の形而上学","大陸哲学・現象学","Western_Europe",1641,"https://en.wikipedia.org/wiki/Dualism_(philosophy_of_mind)",now(),now()),
    (uid(),"汎心論","Panpsychism","意識は物質の基本的性質として宇宙に遍在するという立場","分析哲学・心の哲学","Global_Synthesis",2006,"https://en.wikipedia.org/wiki/Panpsychism",now(),now()),
    (uid(),"観念論","Idealism","実在は精神・観念・経験に依存するというバークリー・カント以来の立場","大陸哲学・現象学","Western_Europe",1710,"https://en.wikipedia.org/wiki/Idealism",now(),now()),
    (uid(),"実在論","Realism (philosophy)","心から独立した外的世界が実在するという立場","分析哲学・心の哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/Philosophical_realism",now(),now()),
    (uid(),"アンチ実在論","Anti-Realism","外的世界や抽象的対象の独立した実在を否定するダミットらの立場","分析哲学・心の哲学","Western_Europe",1978,"https://en.wikipedia.org/wiki/Anti-realism",now(),now()),
    (uid(),"普遍論争","Problem of Universals","普遍概念が実在するか（実在論）名称に過ぎないか（唯名論）をめぐる中世哲学の論争","大陸哲学・現象学","Western_Europe",1100,"https://en.wikipedia.org/wiki/Problem_of_universals",now(),now()),
    (uid(),"唯名論","Nominalism","普遍は名称に過ぎず個別的事物のみが実在するという立場","大陸哲学・現象学","Western_Europe",1300,"https://en.wikipedia.org/wiki/Nominalism",now(),now()),
    (uid(),"プラトン主義","Platonism","数学的・抽象的対象が物理世界から独立して実在するという立場","大陸哲学・現象学","Western_Europe",-385,"https://en.wikipedia.org/wiki/Platonism",now(),now()),
    (uid(),"数学の哲学","Philosophy of Mathematics","数学的対象の存在・真理・認識を論じる哲学の分野","分析哲学・心の哲学","Western_Europe",1879,"https://en.wikipedia.org/wiki/Philosophy_of_mathematics",now(),now()),
    (uid(),"論理実証主義","Logical Positivism","ウィーン学団が提唱した意味の検証可能性原理に基づく哲学","分析哲学・心の哲学","Western_Europe",1922,"https://en.wikipedia.org/wiki/Logical_positivism",now(),now()),
    (uid(),"反証主義","Falsificationism","科学理論は検証ではなく反証可能性によって特徴づけられるポパーの科学哲学","分析哲学・心の哲学","Western_Europe",1934,"https://en.wikipedia.org/wiki/Falsifiability",now(),now()),
    (uid(),"科学的実在論","Scientific Realism","成熟した科学理論の理論的存在者が実在するという立場","分析哲学・心の哲学","North_America",1975,"https://en.wikipedia.org/wiki/Scientific_realism",now(),now()),
    (uid(),"パラダイム論","Paradigm Theory","科学革命は通常科学から革命的転換として起きるというクーンの科学史観","分析哲学・心の哲学","North_America",1962,"https://en.wikipedia.org/wiki/The_Structure_of_Scientific_Revolutions",now(),now()),
    (uid(),"科学と価値","Science and Values","科学的探求は価値中立でなく価値が埋め込まれているというロングーノらの論","分析哲学・心の哲学","North_America",1990,"https://en.wikipedia.org/wiki/Value-free_science",now(),now()),
    (uid(),"命題論理","Propositional Logic","命題の真偽と論理結合子の形式的体系","分析哲学・心の哲学","Western_Europe",1879,"https://en.wikipedia.org/wiki/Propositional_calculus",now(),now()),
    (uid(),"述語論理","Predicate Logic","個体・述語・量化子を含む一階述語論理の形式体系","分析哲学・心の哲学","Western_Europe",1879,"https://en.wikipedia.org/wiki/First-order_logic",now(),now()),
    (uid(),"モーダル論理","Modal Logic","必然性と可能性の演算子を含む論理体系","分析哲学・心の哲学","North_America",1963,"https://en.wikipedia.org/wiki/Modal_logic",now(),now()),
    (uid(),"認識論的論理","Epistemic Logic","知識・信念・共有知識を形式化した論理体系","分析哲学・心の哲学","Western_Europe",1962,"https://en.wikipedia.org/wiki/Epistemic_modal_logic",now(),now()),
    (uid(),"義務論理","Deontic Logic","義務・許可・禁止を形式化した論理体系","分析哲学・心の哲学","Western_Europe",1951,"https://en.wikipedia.org/wiki/Deontic_logic",now(),now()),
    (uid(),"時制論理","Temporal Logic","過去・現在・未来の時間的関係を形式化した論理体系","分析哲学・心の哲学","North_America",1977,"https://en.wikipedia.org/wiki/Temporal_logic",now(),now()),
    (uid(),"非単調論理","Non-Monotonic Logic","新情報によって結論が取り消される推論を形式化する論理","分析哲学・心の哲学","North_America",1980,"https://en.wikipedia.org/wiki/Non-monotonic_logic",now(),now()),
    (uid(),"確率論的論理","Probabilistic Logic","不確実性下の推論に確率を組み込んだ論理体系","分析哲学・心の哲学","North_America",1986,"https://en.wikipedia.org/wiki/Probabilistic_logic",now(),now()),
    (uid(),"ゲーデルの不完全性定理","Godel Incompleteness Theorems","任意の無矛盾な形式的算術体系には証明も反証もできない命題があるという定理","分析哲学・心の哲学","Western_Europe",1931,"https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems",now(),now()),
    (uid(),"チューリングテスト","Turing Test","機械が人間と区別できない応答をできれば知性があると判定するアラン・チューリングの提案","分析哲学・心の哲学","Western_Europe",1950,"https://en.wikipedia.org/wiki/Turing_test",now(),now()),
    (uid(),"中国語の部屋","Chinese Room","コンピュータは構文を処理するが意味を理解しないというサールの思考実験","分析哲学・心の哲学","North_America",1980,"https://en.wikipedia.org/wiki/Chinese_room",now(),now()),
    (uid(),"フレーム問題","Frame Problem","変化しない事実の推論を効率化する問題として人工知能哲学で提起された問題","分析哲学・心の哲学","North_America",1969,"https://en.wikipedia.org/wiki/Frame_problem",now(),now()),
    (uid(),"記号接地問題","Symbol Grounding Problem","記号システムが意味を持つための条件を問うハルナードの問題","分析哲学・心の哲学","North_America",1990,"https://en.wikipedia.org/wiki/Symbol_grounding_problem",now(),now()),
    (uid(),"クオリア","Qualia","痛みや赤の見えなど主観的経験の感覚的性質","分析哲学・心の哲学","North_America",1982,"https://en.wikipedia.org/wiki/Qualia",now(),now()),
    (uid(),"意識の流れ","Stream of Consciousness","ウィリアム・ジェームズが記述した意識経験の連続的かつ変化する流れ","大陸哲学・現象学","North_America",1890,"https://en.wikipedia.org/wiki/Stream_of_consciousness",now(),now()),
    (uid(),"デネットのヘテロ現象学","Heterophenomenology","デネットが提唱する意識研究の三人称的方法論","分析哲学・心の哲学","North_America",1991,"https://en.wikipedia.org/wiki/Heterophenomenology",now(),now()),
    (uid(),"メタ倫理学","Metaethics","道徳的言語・事実・知識の性質を問うカント・ムーア以来の哲学の分野","倫理学・政治哲学","Western_Europe",1903,"https://en.wikipedia.org/wiki/Meta-ethics",now(),now()),
    (uid(),"規範倫理学","Normative Ethics","行為の正しさの基準を定める功利主義・義務論・徳倫理学の分野","倫理学・政治哲学","Western_Europe",1789,"https://en.wikipedia.org/wiki/Normative_ethics",now(),now()),
    (uid(),"応用倫理学","Applied Ethics","現実の倫理的問題（AI・医療・環境・ビジネス等）に倫理理論を適用する分野","倫理学・政治哲学","North_America",1971,"https://en.wikipedia.org/wiki/Applied_ethics",now(),now()),
    (uid(),"法哲学","Philosophy of Law","法の性質・権威・正当性を論じる哲学の分野","分析哲学・心の哲学","Western_Europe",1690,"https://en.wikipedia.org/wiki/Philosophy_of_law",now(),now()),
    (uid(),"言語の意味論的三角形","Semiotic Triangle","記号・意味・指示対象の三者関係を示すオグデン＝リチャーズの図式","分析哲学・心の哲学","Western_Europe",1923,"https://en.wikipedia.org/wiki/Triangle_of_reference",now(),now()),
    (uid(),"ラッセルのパラドックス","Russell's Paradox","集合論の素朴な公理から生じる「自己を含まない集合の集合」の矛盾","分析哲学・心の哲学","Western_Europe",1901,"https://en.wikipedia.org/wiki/Russell%27s_paradox",now(),now()),
    (uid(),"ヴィトゲンシュタインの後期哲学","Later Wittgenstein","意味は使用であり言語ゲームで構成されるとする後期ウィトゲンシュタインの哲学","分析哲学・心の哲学","Western_Europe",1953,"https://en.wikipedia.org/wiki/Ludwig_Wittgenstein",now(),now()),
    (uid(),"プラグマティズムの真理観","Pragmatist Theory of Truth","真理は探求の最終的合意であるパース・デューイのプラグマティスト的真理論","分析哲学・心の哲学","North_America",1878,"https://en.wikipedia.org/wiki/Pragmatic_theory_of_truth",now(),now()),
    (uid(),"整合説","Coherence Theory of Truth","真理はすべての信念の整合的体系への合致によって成立するという立場","分析哲学・心の哲学","Western_Europe",1906,"https://en.wikipedia.org/wiki/Coherence_theory_of_truth",now(),now()),
    (uid(),"対応説","Correspondence Theory of Truth","命題が事実と対応するときに真であるという古典的真理論","分析哲学・心の哲学","Western_Europe",1912,"https://en.wikipedia.org/wiki/Correspondence_theory_of_truth",now(),now()),
    (uid(),"消去主義的真理論","Deflationary Theory of Truth","真理の概念には実質的内容がなく述語の機能的役割に還元されるという立場","分析哲学・心の哲学","North_America",1970,"https://en.wikipedia.org/wiki/Deflationary_theory_of_truth",now(),now()),
    (uid(),"分析と総合","Analytic and Synthetic","分析判断（概念の展開）と総合判断（経験的内容付加）のカントの区別","分析哲学・心の哲学","Western_Europe",1781,"https://en.wikipedia.org/wiki/Analytic%E2%80%93synthetic_distinction",now(),now()),
    (uid(),"アプリオリとアポステリオリ","A Priori and A Posteriori","経験に先立つ認識と経験から得られる認識のカントの区別","大陸哲学・現象学","Western_Europe",1781,"https://en.wikipedia.org/wiki/A_priori_and_a_posteriori",now(),now()),
    (uid(),"超越論的観念論","Transcendental Idealism","空間・時間・カテゴリーは主観の形式であるというカントの認識論的立場","大陸哲学・現象学","Western_Europe",1781,"https://en.wikipedia.org/wiki/Transcendental_idealism",now(),now()),
    (uid(),"弁証法","Dialectic","ヘーゲルにおける正・反・合の対立と止揚による概念の自己展開","大陸哲学・現象学","Western_Europe",1807,"https://en.wikipedia.org/wiki/Dialectic",now(),now()),
    (uid(),"精神現象学","Phenomenology of Spirit","ヘーゲルが意識・自己意識・精神の発展を弁証法的に叙述した主著","大陸哲学・現象学","Western_Europe",1807,"https://en.wikipedia.org/wiki/Phenomenology_of_Spirit",now(),now()),
    (uid(),"疎外","Alienation","マルクスが論じる労働過程での人間の自己喪失・対象化の概念","大陸哲学・現象学","Western_Europe",1844,"https://en.wikipedia.org/wiki/Marx%27s_theory_of_alienation",now(),now()),
    (uid(),"実践哲学","Practical Philosophy","行為・道徳・政治に関わる哲学的問いを扱うカント以来の哲学の領域","大陸哲学・現象学","Western_Europe",1785,"https://en.wikipedia.org/wiki/Practical_philosophy",now(),now()),
    (uid(),"プラグマティズム","Pragmatism","パース・ジェームズ・デューイが確立した真理と意味を実践的結果で評価する哲学","分析哲学・心の哲学","North_America",1878,"https://en.wikipedia.org/wiki/Pragmatism",now(),now()),
    (uid(),"新プラグマティズム","Neopragmatism","ローティが提唱した反基礎主義・会話的合理性に基づく現代プラグマティズム","分析哲学・心の哲学","North_America",1979,"https://en.wikipedia.org/wiki/Neopragmatism",now(),now()),
    (uid(),"プロセス哲学","Process Philosophy","実体ではなく出来事・過程を存在の基本単位とするホワイトヘッドの形而上学","大陸哲学・現象学","Western_Europe",1929,"https://en.wikipedia.org/wiki/Process_philosophy",now(),now()),
    (uid(),"記号論","Semiotics","記号・意味・コミュニケーションの体系的理論","大陸哲学・現象学","Global_Synthesis",1960,"https://en.wikipedia.org/wiki/Semiotics",now(),now()),
    (uid(),"フィクションの哲学","Philosophy of Fiction","虚構的存在者の存在論・虚構的真理・感情のパラドックスを論じる哲学","分析哲学・心の哲学","North_America",1975,"https://en.wikipedia.org/wiki/Philosophy_of_fiction",now(),now()),
    (uid(),"時間の哲学","Philosophy of Time","時間の実在性・方向性・経験を論じる形而上学","分析哲学・心の哲学","Western_Europe",1908,"https://en.wikipedia.org/wiki/Philosophy_of_time",now(),now()),
    (uid(),"同一性の形而上学","Metaphysics of Identity","ライプニッツの法則・時間を通じた同一性・人格の同一性を論じる形而上学","分析哲学・心の哲学","Western_Europe",1975,"https://en.wikipedia.org/wiki/Personal_identity",now(),now()),
    (uid(),"スコラ哲学","Scholasticism","中世キリスト教神学とアリストテレス哲学を統合したトマス・アクィナスらの哲学","大陸哲学・現象学","Western_Europe",1100,"https://en.wikipedia.org/wiki/Scholasticism",now(),now()),
    (uid(),"新プラトン主義","Neoplatonism","プロティノスが確立した一者・知性・魂の三原理からなるプラトン主義の発展","大陸哲学・現象学","Western_Europe",250,"https://en.wikipedia.org/wiki/Neoplatonism",now(),now()),
    (uid(),"イスラーム哲学","Islamic Philosophy","アル＝キンディー・イブン・シーナーらがギリシア哲学とイスラーム神学を統合した哲学","大陸哲学・現象学","West_Asia_North_Africa",850,"https://en.wikipedia.org/wiki/Islamic_philosophy",now(),now()),
    (uid(),"ユダヤ哲学","Jewish Philosophy","マイモニデスらがユダヤ教神学とギリシア哲学を統合した哲学伝統","大陸哲学・現象学","West_Asia_North_Africa",1190,"https://en.wikipedia.org/wiki/Jewish_philosophy",now(),now()),
    (uid(),"新儒学","Neo-Confucianism","宋・明代に朱熹らが仏教・道教を取り込んで発展させた儒学の刷新","大陸哲学・現象学","East_Asia",1100,"https://en.wikipedia.org/wiki/Neo-Confucianism",now(),now()),
    (uid(),"道家哲学","Taoist Philosophy","老子・荘子を源泉とする自然・無為・道を中心とする中国の哲学思想","大陸哲学・現象学","East_Asia",-500,"https://en.wikipedia.org/wiki/Taoism",now(),now()),
    (uid(),"インド認識論","Indian Epistemology","ニヤーヤ学派を中心とする知覚・推論・比喩・言語証言の四種知識源論","大陸哲学・現象学","South_Asia",-200,"https://en.wikipedia.org/wiki/Indian_logic",now(),now()),
    (uid(),"アフリカ哲学","African Philosophy","ウンコロやオルカによる口承・共同体・存在論を中心とするアフリカの哲学","大陸哲学・現象学","Sub_Saharan_Africa",1970,"https://en.wikipedia.org/wiki/African_philosophy",now(),now()),
    (uid(),"批判理論","Critical Theory","ホルクハイマー・アドルノが提唱した啓蒙理性批判と解放志向の社会哲学","大陸哲学・現象学","Western_Europe",1937,"https://en.wikipedia.org/wiki/Critical_theory",now(),now()),
    (uid(),"フランクフルト学派","Frankfurt School","ホルクハイマー・アドルノ・ハーバーマスらの批判理論の研究集団","大陸哲学・現象学","Western_Europe",1923,"https://en.wikipedia.org/wiki/Frankfurt_School",now(),now()),
    (uid(),"コミュニケーション的行為","Communicative Action","ハーバーマスが提唱する相互理解を目指す言語行為を社会理論の基礎とする概念","大陸哲学・現象学","Western_Europe",1981,"https://en.wikipedia.org/wiki/Communicative_action",now(),now()),
    (uid(),"解釈学的循環","Hermeneutic Circle","部分は全体の理解を、全体は部分の理解を前提とする解釈の循環","大陸哲学・現象学","Western_Europe",1819,"https://en.wikipedia.org/wiki/Hermeneutic_circle",now(),now()),
    (uid(),"脱近代哲学","Postmodern Philosophy","大文字の理性・普遍的真理・基礎付けを批判するリオタールらの哲学","大陸哲学・現象学","Western_Europe",1979,"https://en.wikipedia.org/wiki/Postmodern_philosophy",now(),now()),
    (uid(),"現代フランス哲学","Contemporary French Philosophy","デリダ・フーコー・ドゥルーズ・バディウらの1960年代以降のフランス哲学","大陸哲学・現象学","Western_Europe",1960,"https://en.wikipedia.org/wiki/French_philosophy",now(),now()),
    (uid(),"構造主義哲学","Structuralist Philosophy","言語・社会・文化の構造を前面に出すソシュール・レヴィ＝ストロース以来の哲学","大陸哲学・現象学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Structuralism",now(),now()),
    (uid(),"環境哲学","Environmental Philosophy","自然の価値・人間と自然の関係・持続可能性を論じる哲学の分野","倫理学・政治哲学","North_America",1971,"https://en.wikipedia.org/wiki/Environmental_philosophy",now(),now()),
    (uid(),"スピノザの汎神論","Spinoza's Pantheism","神と自然は同一の唯一実体の二つの属性であるというスピノザの形而上学","大陸哲学・現象学","Western_Europe",1677,"https://en.wikipedia.org/wiki/Baruch_Spinoza",now(),now()),
    (uid(),"ライプニッツのモナド論","Leibniz Monadology","単純で分割不能な精神的実体「モナド」が宇宙を構成するという形而上学","大陸哲学・現象学","Western_Europe",1714,"https://en.wikipedia.org/wiki/Monadology",now(),now()),
    (uid(),"経験主義","Empiricism","すべての知識は感覚経験に由来するロック・ヒューム以来の認識論","大陸哲学・現象学","Western_Europe",1689,"https://en.wikipedia.org/wiki/Empiricism",now(),now()),
    (uid(),"理性主義","Rationalism","理性と生得観念が確実な知識の基礎であるデカルト・ライプニッツの認識論","大陸哲学・現象学","Western_Europe",1637,"https://en.wikipedia.org/wiki/Rationalism",now(),now()),
    (uid(),"懐疑主義","Skepticism","知識の確実性を疑問視するピュロン・デカルト以来の哲学的立場","大陸哲学・現象学","Western_Europe",-300,"https://en.wikipedia.org/wiki/Philosophical_skepticism",now(),now()),
    (uid(),"デカルトの方法的懐疑","Cartesian Method of Doubt","確実な知識の基礎を求めて疑いえるすべてを疑うデカルトの認識論的方法","大陸哲学・現象学","Western_Europe",1641,"https://en.wikipedia.org/wiki/Cartesian_doubt",now(),now()),
    (uid(),"我思う","Cogito ergo sum","「我思う、ゆえに我あり」というデカルトの哲学の第一原理","大陸哲学・現象学","Western_Europe",1637,"https://en.wikipedia.org/wiki/Cogito,_ergo_sum",now(),now()),
    (uid(),"ヒュームの問題","Hume's Problem of Induction","過去の観察から将来についての普遍的結論を正当化できるかという問題","分析哲学・心の哲学","Western_Europe",1739,"https://en.wikipedia.org/wiki/Problem_of_induction",now(),now()),
    (uid(),"カントの定言命法","Categorical Imperative","「あなたの行為の格率が普遍的法則となるよう行為せよ」というカントの道徳原理","倫理学・政治哲学","Western_Europe",1785,"https://en.wikipedia.org/wiki/Categorical_imperative",now(),now()),
    (uid(),"目的の王国","Kingdom of Ends","すべての理性的存在者が互いを目的として扱う倫理的理想共同体のカントの概念","倫理学・政治哲学","Western_Europe",1785,"https://en.wikipedia.org/wiki/Kingdom_of_Ends",now(),now()),
    (uid(),"シュライアーマッハーの解釈学","Schleiermacher Hermeneutics","テクストの理解は著者の心理的再構築を含むというロマン主義的解釈学","大陸哲学・現象学","Western_Europe",1819,"https://en.wikipedia.org/wiki/Friedrich_Schleiermacher",now(),now()),
    (uid(),"ディルタイの精神科学","Dilthey Geistswissenschaften","自然科学の説明に対して精神科学は理解を方法とするというディルタイの区別","大陸哲学・現象学","Western_Europe",1883,"https://en.wikipedia.org/wiki/Wilhelm_Dilthey",now(),now()),
    (uid(),"新カント主義","Neo-Kantianism","19世紀後半のカント哲学への回帰を軸としたマールブルク学派・西南ドイツ学派の哲学","大陸哲学・現象学","Western_Europe",1860,"https://en.wikipedia.org/wiki/Neo-Kantianism",now(),now()),
    (uid(),"ウィリアム・ジェームズの根本的経験主義","Radical Empiricism","純粋経験を哲学の出発点とするジェームズの意識と世界の連続性の思想","大陸哲学・現象学","North_America",1912,"https://en.wikipedia.org/wiki/Radical_empiricism",now(),now()),
    (uid(),"哲学的人間学","Philosophical Anthropology","シェーラー・プレスナーらによる人間の固有な存在様式を探る哲学","大陸哲学・現象学","Western_Europe",1928,"https://en.wikipedia.org/wiki/Philosophical_anthropology",now(),now()),
    (uid(),"象徴形式の哲学","Philosophy of Symbolic Forms","カッシーラーが提唱する人間は象徴を通じて世界を理解する文化哲学","大陸哲学・現象学","Western_Europe",1923,"https://en.wikipedia.org/wiki/Ernst_Cassirer",now(),now()),
    (uid(),"意味の哲学","Philosophy of Meaning","フレーゲ・ラッセル以来の言語表現の意味・指示・真理条件を論じる哲学","分析哲学・心の哲学","Western_Europe",1892,"https://en.wikipedia.org/wiki/Philosophy_of_language",now(),now()),
    (uid(),"専門知の哲学","Philosophy of Expertise","専門知識の性質・習得・権威を論じる認識論の分野","分析哲学・心の哲学","North_America",2001,"https://en.wikipedia.org/wiki/Tacit_knowledge",now(),now()),

    # 古典学・古典文学補強 +60
    (uid(),"ソポクレスの悲劇","Sophoclean Tragedy","オイディプス王・アンティゴネーに見るソポクレスの悲劇的宿命と自由意志","古典学・古典文学","Western_Europe",-450,"https://en.wikipedia.org/wiki/Sophocles",now(),now()),
    (uid(),"アイスキュロスの三部作","Aeschylean Trilogy","オレステイア等の三部作でアイスキュロスが展開した神の正義と人間の苦悩","古典学・古典文学","Western_Europe",-525,"https://en.wikipedia.org/wiki/Aeschylus",now(),now()),
    (uid(),"エウリピデスの革新","Euripidean Innovation","神話の合理化・女性の心理・社会批判に特徴づけられるエウリピデスの悲劇","古典学・古典文学","Western_Europe",-484,"https://en.wikipedia.org/wiki/Euripides",now(),now()),
    (uid(),"アリストパネスの喜劇","Aristophanic Comedy","戦争批判・政治風刺・哲学批評を含む古代ギリシア喜劇の傑作群","古典学・古典文学","Western_Europe",-450,"https://en.wikipedia.org/wiki/Aristophanes",now(),now()),
    (uid(),"テオクリトスの牧歌","Theocritean Pastoral","田園の理想化を詩の主題とするテオクリトスのギリシア語牧歌詩","古典学・古典文学","Western_Europe",-270,"https://en.wikipedia.org/wiki/Theocritus",now(),now()),
    (uid(),"プラトンの対話篇","Platonic Dialogues","ソクラテスを主役に哲学的問いを劇的対話で探求するプラトンの著作群","古典学・古典文学","Western_Europe",-387,"https://en.wikipedia.org/wiki/Platonic_dialogues",now(),now()),
    (uid(),"カトゥルスの愛の詩","Catullan Poetry","ローマ帝政前期の詩人カトゥルスの恋愛・友情・政治を詠んだ抒情詩","古典学・古典文学","Western_Europe",-84,"https://en.wikipedia.org/wiki/Catullus",now(),now()),
    (uid(),"ホラティウスの詩学","Horatian Poetics","「詩の技法」で古代ローマ最高の詩人論・ジャンル論を確立したホラティウス","古典学・古典文学","Western_Europe",-65,"https://en.wikipedia.org/wiki/Horace",now(),now()),
    (uid(),"プロペルティウスの哀歌","Propertian Elegy","愛の苦悩と詩の自律を主題とするプロペルティウスのラテン語哀歌","古典学・古典文学","Western_Europe",-50,"https://en.wikipedia.org/wiki/Propertius",now(),now()),
    (uid(),"ユウェナリスの風刺詩","Juvenalian Satire","ローマ帝政期の腐敗・堕落を激烈に風刺するユウェナリスの詩集","古典学・古典文学","Western_Europe",100,"https://en.wikipedia.org/wiki/Juvenal",now(),now()),
    (uid(),"プリニウスの書簡","Pliny's Letters","ローマ帝政期の社会・文化を生き生きと伝える小プリニウスの書簡集","古典学・古典文学","Western_Europe",100,"https://en.wikipedia.org/wiki/Pliny_the_Younger",now(),now()),
    (uid(),"マルクス・アウレリウスの瞑想録","Meditations of Marcus Aurelius","ローマ皇帝が自己修養のために書いたストア哲学の実践的日記","古典学・古典文学","Western_Europe",165,"https://en.wikipedia.org/wiki/Meditations",now(),now()),
    (uid(),"アウグスティヌスの告白","Confessions of Augustine","回心の経験と神への探求を叙述するアウグスティヌスの自伝的神学著作","古典学・古典文学","Western_Europe",397,"https://en.wikipedia.org/wiki/Confessions_(Augustine)",now(),now()),
    (uid(),"ボエティウスの哲学の慰め","Consolation of Philosophy","処刑を待つボエティウスが書いた哲学と運命について対話形式で論じた著作","古典学・古典文学","Western_Europe",524,"https://en.wikipedia.org/wiki/Consolation_of_Philosophy",now(),now()),
    (uid(),"ベオウルフ","Beowulf","英語最古の英雄叙事詩で古英語文学の最高傑作","古典学・古典文学","Western_Europe",900,"https://en.wikipedia.org/wiki/Beowulf",now(),now()),
    (uid(),"アラビア語古典詩","Classical Arabic Poetry","ムアッラカート等のジャーヒリーヤ時代のアラビア語詩の伝統","古典学・古典文学","West_Asia_North_Africa",500,"https://en.wikipedia.org/wiki/Arabic_poetry",now(),now()),
    (uid(),"ペルシア語古典詩","Classical Persian Poetry","ルーダキー・フィルドウスィー・ハーフェズらのペルシア語詩の豊かな伝統","古典学・古典文学","West_Asia_North_Africa",900,"https://en.wikipedia.org/wiki/Persian_literature",now(),now()),
    (uid(),"タミル古典文学","Tamil Classical Literature","サンガム文学を核とする世界最古の文学伝統の一つ","古典学・古典文学","South_Asia",-200,"https://en.wikipedia.org/wiki/Tamil_literature",now(),now()),
    (uid(),"パーリ語文学","Pali Literature","テーラワーダ仏教の聖典と注釈文学の伝統","古典学・古典文学","South_Asia",-300,"https://en.wikipedia.org/wiki/Pali_literature",now(),now()),
    (uid(),"漢詩の詩学","Classical Chinese Poetics","詩経・楚辞から唐詩宋詞まで続く中国詩学の理論と実践","古典学・古典文学","East_Asia",-600,"https://en.wikipedia.org/wiki/Chinese_poetry",now(),now()),
    (uid(),"万葉集","Man'yoshu","8世紀に成立した日本最古の和歌集","古典学・古典文学","East_Asia",759,"https://en.wikipedia.org/wiki/Man%27y%C5%8Dsh%C5%AB",now(),now()),
    (uid(),"枕草子","The Pillow Book","清少納言による平安時代の随筆文学の傑作","古典学・古典文学","East_Asia",1002,"https://en.wikipedia.org/wiki/The_Pillow_Book",now(),now()),
    (uid(),"平家物語","The Tale of the Heike","平家の盛衰を描く中世日本の軍記文学の代表作","古典学・古典文学","East_Asia",1330,"https://en.wikipedia.org/wiki/The_Tale_of_the_Heike",now(),now()),
    (uid(),"奥の細道","Oku no Hosomichi","松尾芭蕉による俳諧紀行文学の傑作","古典学・古典文学","East_Asia",1702,"https://en.wikipedia.org/wiki/Oku_no_Hosomichi",now(),now()),
    (uid(),"三国志演義","Romance of the Three Kingdoms","後漢末の三国時代を描く中国四大名著の一つ","古典学・古典文学","East_Asia",1321,"https://en.wikipedia.org/wiki/Romance_of_the_Three_Kingdoms",now(),now()),
    (uid(),"紅楼夢","Dream of the Red Chamber","清代の曹雪芹が著した中国古典小説の最高傑作","古典学・古典文学","East_Asia",1791,"https://en.wikipedia.org/wiki/Dream_of_the_Red_Chamber",now(),now()),
    (uid(),"チョーサーのカンタベリー物語","Canterbury Tales","14世紀英語文学の傑作でイングランドの社会を巡礼者の語りで描く","古典学・古典文学","Western_Europe",1400,"https://en.wikipedia.org/wiki/The_Canterbury_Tales",now(),now()),
    (uid(),"シェイクスピアの悲劇","Shakespearean Tragedy","ハムレット・オセロ・リア王・マクベスに代表されるシェイクスピアの四大悲劇","古典学・古典文学","Western_Europe",1600,"https://en.wikipedia.org/wiki/Shakespeare%27s_tragedies",now(),now()),
    (uid(),"ミルトンの失楽園","Paradise Lost","清教徒革命期のミルトンが書いた壮大な聖書叙事詩","古典学・古典文学","Western_Europe",1667,"https://en.wikipedia.org/wiki/Paradise_Lost",now(),now()),
    (uid(),"モリエールの喜劇","Moliere's Comedy","宗教的偽善・医師・守銭奴を風刺するフランス古典主義喜劇の傑作群","古典学・古典文学","Western_Europe",1666,"https://en.wikipedia.org/wiki/Moli%C3%A8re",now(),now()),
    (uid(),"ラシーヌの悲劇","Racine's Tragedy","フランス古典主義悲劇の最高峰フェードルを生んだラシーヌの作品群","古典学・古典文学","Western_Europe",1677,"https://en.wikipedia.org/wiki/Jean_Racine",now(),now()),
    (uid(),"グリム童話","Brothers Grimm Fairy Tales","ドイツ口承民話を収集・再話したグリム兄弟の童話集","古典学・古典文学","Western_Europe",1812,"https://en.wikipedia.org/wiki/Grimm%27s_Fairy_Tales",now(),now()),
    (uid(),"セルバンテスの短篇集","Cervantes Novelas Ejemplares","スペインの模範小説集でセルバンテスの社会批評と人間観察が光る作品","古典学・古典文学","Western_Europe",1613,"https://en.wikipedia.org/wiki/Novelas_Ejemplares",now(),now()),
    (uid(),"トルストイの長編小説","Tolstoy Epic Novels","戦争と平和・アンナ・カレーニナに代表するロシア文学の巨匠の作品","古典学・古典文学","Western_Europe",1869,"https://en.wikipedia.org/wiki/Leo_Tolstoy",now(),now()),
    (uid(),"ドストエフスキーの心理小説","Dostoevsky Psychological Novel","罪と罰・カラマーゾフの兄弟に代表する実存的心理描写の深みある小説","古典学・古典文学","Western_Europe",1866,"https://en.wikipedia.org/wiki/Fyodor_Dostoevsky",now(),now()),
    (uid(),"チョーサー以前の中英語文学","Middle English Literature","パール・サー・ガウェイン等の中英語時代の文学","古典学・古典文学","Western_Europe",1300,"https://en.wikipedia.org/wiki/Middle_English_literature",now(),now()),
    (uid(),"ルネサンス文学","Renaissance Literature","人文主義・古典回帰・個人の発見を特徴とするヨーロッパ・ルネサンスの文学","古典学・古典文学","Western_Europe",1400,"https://en.wikipedia.org/wiki/Renaissance_literature",now(),now()),
    (uid(),"バロック文学","Baroque Literature","華麗・複雑・感情的強度を特徴とする17世紀ヨーロッパのバロック文学","古典学・古典文学","Western_Europe",1600,"https://en.wikipedia.org/wiki/Baroque_literature",now(),now()),
    (uid(),"古典主義文学","Neoclassical Literature","理性・均衡・古代の規範を重視する17〜18世紀ヨーロッパの文学","古典学・古典文学","Western_Europe",1660,"https://en.wikipedia.org/wiki/Neoclassicism",now(),now()),
    (uid(),"スワヒリ語文学","Swahili Literature","東アフリカの共通語スワヒリ語で書かれた詩・物語・現代文学","古典学・古典文学","Sub_Saharan_Africa",1700,"https://en.wikipedia.org/wiki/Swahili_literature",now(),now()),
    (uid(),"ヨルバ口承文学","Yoruba Oral Literature","西アフリカのヨルバ族の神話・ことわざ・歌の豊かな口承文学伝統","古典学・古典文学","Sub_Saharan_Africa",1000,"https://en.wikipedia.org/wiki/Yoruba_literature",now(),now()),
    (uid(),"ウパニシャッド","Upanishads","ヴェーダの最後の部分でブラフマンとアートマンの同一性を論じる哲学的聖典","古典学・古典文学","South_Asia",-700,"https://en.wikipedia.org/wiki/Upanishads",now(),now()),
    (uid(),"バガヴァッド・ギーター","Bhagavad Gita","マハーバーラタに含まれクリシュナとアルジュナの対話で倫理・宗教を論じる聖典","古典学・古典文学","South_Asia",-200,"https://en.wikipedia.org/wiki/Bhagavad_Gita",now(),now()),
    (uid(),"パンチャタントラ","Panchatantra","動物寓話を通じて政治・倫理・知恵を教えるインド古典の知恵文学","古典学・古典文学","South_Asia",-200,"https://en.wikipedia.org/wiki/Panchatantra",now(),now()),
    (uid(),"テヴァーラム","Tevaram","シヴァ神への敬虔を歌い上げるタミル語シヴァ派の聖者詩集","古典学・古典文学","South_Asia",700,"https://en.wikipedia.org/wiki/Tevaram",now(),now()),
    (uid(),"モルドゥン・キルギス叙事詩","Epic of Manas","キルギスの英雄マナスを主人公とする世界最長の口承叙事詩","古典学・古典文学","Global_Synthesis",1000,"https://en.wikipedia.org/wiki/Epic_of_Manas",now(),now()),
    (uid(),"コーカサスの叙事詩","Caucasian Epics","ナルト叙事詩等コーカサス地域の英雄的口承文学の伝統","古典学・古典文学","Global_Synthesis",1000,"https://en.wikipedia.org/wiki/Nart_saga",now(),now()),
    (uid(),"フィンランドのカレワラ","Kalevala","フィンランドの民族叙事詩でロンロットが口承詩を収集・編纂した国民文学","古典学・古典文学","Western_Europe",1849,"https://en.wikipedia.org/wiki/Kalevala",now(),now()),
    (uid(),"西アフリカのグリオ伝統","Griot Tradition","西アフリカの語り部グリオによる歴史・系譜・音楽の口承保存と伝達","古典学・古典文学","Sub_Saharan_Africa",1200,"https://en.wikipedia.org/wiki/Griot",now(),now()),
    (uid(),"スカルド詩","Skaldic Poetry","古ノルド語の複雑な韻律と詩人名を持つ中世北欧の宮廷詩","古典学・古典文学","Western_Europe",800,"https://en.wikipedia.org/wiki/Skaldic_poetry",now(),now()),
    (uid(),"サガ文学","Icelandic Sagas","中世アイスランドのノルウェー・アイスランド人を描く散文の物語","古典学・古典文学","Western_Europe",1200,"https://en.wikipedia.org/wiki/Sagas_of_Icelanders",now(),now()),
    (uid(),"アパルトヘイト文学","Apartheid Literature","南アフリカのアパルトヘイト体制に抵抗・証言する文学","古典学・古典文学","Sub_Saharan_Africa",1960,"https://en.wikipedia.org/wiki/Literature_of_South_Africa",now(),now()),
    (uid(),"マオリの口承文学","Maori Oral Literature","ニュージーランドのマオリ民族の神話・歌・諺の豊かな口承文学","古典学・古典文学","Oceania",1000,"https://en.wikipedia.org/wiki/Maori_literature",now(),now()),
    (uid(),"アボリジナル口承","Aboriginal Australian Oral Tradition","ドリームタイム神話を含むオーストラリア先住民の世界最古の口承文化","古典学・古典文学","Oceania",-40000,"https://en.wikipedia.org/wiki/Australian_Aboriginal_mythology",now(),now()),
    (uid(),"コーランの文学性","Literary Qualities of Quran","アラビア語の最高の文学的達成とされるクルアーンの修辞・音楽性・意味の多層性","古典学・古典文学","West_Asia_North_Africa",632,"https://en.wikipedia.org/wiki/Quranic_Arabic",now(),now()),

    # 宗教学・神学補強 +40
    (uid(),"宗教の定義","Definition of Religion","宗教を普遍的に定義しようとするデュルケーム・スマート・ティリッヒらの試み","宗教学・神学","Global_Synthesis",1912,"https://en.wikipedia.org/wiki/Religion",now(),now()),
    (uid(),"儀礼理論","Ritual Theory","礼儀・儀式の構造・意味・社会機能を分析するターナー・ベルらの理論","宗教学・神学","Global_Synthesis",1966,"https://en.wikipedia.org/wiki/Ritual",now(),now()),
    (uid(),"タントラ哲学","Tantra Philosophy","身体・性・宇宙のエネルギーを変容の手段とするヒンドゥー・仏教密教の哲学","宗教学・神学","South_Asia",600,"https://en.wikipedia.org/wiki/Tantra",now(),now()),
    (uid(),"密教","Vajrayana Buddhism","儀礼・マントラ・マンダラを用いる急速な悟りを目指す大乗仏教の秘密乗","宗教学・神学","East_Asia",700,"https://en.wikipedia.org/wiki/Vajrayana",now(),now()),
    (uid(),"禅宗","Zen Buddhism","坐禅・公案・師弟伝達を通じて直接の悟りを目指す中国・日本の仏教宗派","宗教学・神学","East_Asia",700,"https://en.wikipedia.org/wiki/Zen",now(),now()),
    (uid(),"浄土教","Pure Land Buddhism","阿弥陀仏への信仰と念仏により浄土への往生を目指す仏教の一流","宗教学・神学","East_Asia",200,"https://en.wikipedia.org/wiki/Pure_Land_Buddhism",now(),now()),
    (uid(),"上座部仏教","Theravada Buddhism","古い仏教を保存するとされるスリランカ・東南アジアの仏教伝統","宗教学・神学","South_Asia",-200,"https://en.wikipedia.org/wiki/Theravada",now(),now()),
    (uid(),"ジャイナ教","Jainism","不殺生・非所有・多面的真理（アネーカーンタ）を核とするインドの宗教","宗教学・神学","South_Asia",-600,"https://en.wikipedia.org/wiki/Jainism",now(),now()),
    (uid(),"シク教","Sikhism","一神教・平等主義・奉仕を強調するパンジャーブ発祥の宗教","宗教学・神学","South_Asia",1469,"https://en.wikipedia.org/wiki/Sikhism",now(),now()),
    (uid(),"ゾロアスター教","Zoroastrianism","善と悪の宇宙的闘争をテーマとするイラン発祥の古代一神教","宗教学・神学","West_Asia_North_Africa",-600,"https://en.wikipedia.org/wiki/Zoroastrianism",now(),now()),
    (uid(),"マニ教","Manichaeism","善悪二元論を基盤とするマニが創始した世界宗教","宗教学・神学","West_Asia_North_Africa",250,"https://en.wikipedia.org/wiki/Manichaeism",now(),now()),
    (uid(),"グノーシス主義","Gnosticism","物質世界を悪しき創造神の作とし精神的知識（グノーシス）による救済を説く運動","宗教学・神学","West_Asia_North_Africa",100,"https://en.wikipedia.org/wiki/Gnosticism",now(),now()),
    (uid(),"東方正教会神学","Eastern Orthodox Theology","ビザンツ神学・神化・聖像崇敬を特徴とするギリシア正教の神学伝統","宗教学・神学","Western_Europe",800,"https://en.wikipedia.org/wiki/Eastern_Orthodox_theology",now(),now()),
    (uid(),"プロテスタント神学","Protestant Theology","聖書のみ・信仰のみ・万人祭司を原理とするルター以来の神学伝統","宗教学・神学","Western_Europe",1517,"https://en.wikipedia.org/wiki/Protestantism",now(),now()),
    (uid(),"カトリック神学","Catholic Theology","ローマ教皇の権威・聖伝・秘跡論を核とするローマカトリック教会の神学","宗教学・神学","Western_Europe",500,"https://en.wikipedia.org/wiki/Catholic_theology",now(),now()),
    (uid(),"イスラーム神学カラーム","Kalam Islamic Theology","アシュアリー学派等のイスラーム合理的神学の伝統","宗教学・神学","West_Asia_North_Africa",850,"https://en.wikipedia.org/wiki/Kalam",now(),now()),
    (uid(),"ユダヤ教律法","Halakha","ユダヤ教の宗教法の総体とその解釈・適用の伝統","宗教学・神学","West_Asia_North_Africa",-200,"https://en.wikipedia.org/wiki/Halakha",now(),now()),
    (uid(),"宗教倫理学","Religious Ethics","各宗教伝統の道徳規範・美徳論・社会倫理を比較研究する学問","宗教学・神学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Religious_ethics",now(),now()),
    (uid(),"ダニエル・デネットの宗教批判","Dennett Religion Breaking the Spell","宗教を自然淘汰の副産物として分析するデネットの進化論的宗教批判","宗教学・神学","North_America",2006,"https://en.wikipedia.org/wiki/Breaking_the_Spell_(book)",now(),now()),
    (uid(),"宗教的ファンダメンタリズム","Religious Fundamentalism","聖典の字義通り解釈と近代主義への対抗を特徴とする宗教復古運動","宗教学・神学","Global_Synthesis",1920,"https://en.wikipedia.org/wiki/Fundamentalism",now(),now()),
    (uid(),"エキュメニズム","Ecumenism","キリスト教諸宗派の対話・協力・統一を目指す運動","宗教学・神学","Global_Synthesis",1910,"https://en.wikipedia.org/wiki/Ecumenism",now(),now()),
    (uid(),"インターフェイス対話","Interfaith Dialogue","異なる宗教伝統間の理解・協力を目指す対話の実践","宗教学・神学","Global_Synthesis",1965,"https://en.wikipedia.org/wiki/Interfaith_dialogue",now(),now()),
    (uid(),"宗教と科学の関係","Religion and Science","創造論・進化論・神学と科学哲学の関係をめぐる対話と論争","宗教学・神学","Global_Synthesis",1860,"https://en.wikipedia.org/wiki/Relationship_between_religion_and_science",now(),now()),
    (uid(),"宗教的暴力","Religious Violence","宗教的動機・正当化・制度化による暴力の社会学的・神学的分析","宗教学・神学","Global_Synthesis",2003,"https://en.wikipedia.org/wiki/Religious_violence",now(),now()),
    (uid(),"宗教的ナショナリズム","Religious Nationalism","宗教的アイデンティティと国民国家を結合させる政治的運動","宗教学・神学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Religious_nationalism",now(),now()),
    (uid(),"アフリカ伝統宗教","African Traditional Religion","精霊・祖先・自然力を中心とするサブサハラアフリカの宗教実践の総称","宗教学・神学","Sub_Saharan_Africa",1000,"https://en.wikipedia.org/wiki/African_traditional_religion",now(),now()),
    (uid(),"オリシャ信仰","Orisha Worship","西アフリカのヨルバ族の神々（オリシャ）崇拝とその新大陸への拡散","宗教学・神学","Sub_Saharan_Africa",1000,"https://en.wikipedia.org/wiki/Orisha",now(),now()),
    (uid(),"先住民宗教","Indigenous Religion","世界各地の先住民の宗教的実践・世界観・儀礼の多様性","宗教学・神学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Indigenous_religion",now(),now()),
    (uid(),"カルマ論","Karma Theory","行為の因果的結果として来世の状態が決まるというインド諸宗教の概念","宗教学・神学","South_Asia",-600,"https://en.wikipedia.org/wiki/Karma",now(),now()),
    (uid(),"輪廻転生","Reincarnation","霊魂が死後新たな身体に生まれ変わるとするインド・古代ギリシア等の信仰","宗教学・神学","Global_Synthesis",-600,"https://en.wikipedia.org/wiki/Reincarnation",now(),now()),
    (uid(),"ニルヴァーナ","Nirvana","仏教において欲望・苦しみの消滅による完全な解脱の状態","宗教学・神学","South_Asia",-500,"https://en.wikipedia.org/wiki/Nirvana",now(),now()),
    (uid(),"宗教的回心","Religious Conversion","ある宗教から他の宗教への信仰の転換のプロセスと心理","宗教学・神学","Global_Synthesis",1902,"https://en.wikipedia.org/wiki/Religious_conversion",now(),now()),
    (uid(),"スピリチュアリティ","Spirituality","制度的宗教を超えた個人的な超越・内的変容・意味追求の次元","宗教学・神学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Spirituality",now(),now()),
    (uid(),"宗教心理学","Psychology of Religion","宗教的経験・信仰・実践の心理的メカニズムを研究する学際分野","宗教学・神学","North_America",1902,"https://en.wikipedia.org/wiki/Psychology_of_religion",now(),now()),
    (uid(),"宗教人類学","Anthropology of Religion","宗教の文化的多様性・機能・象徴を比較人類学的に研究する分野","宗教学・神学","Global_Synthesis",1871,"https://en.wikipedia.org/wiki/Anthropology_of_religion",now(),now()),
    (uid(),"聖書解釈学","Biblical Hermeneutics","聖書テクストの意味を歴史・文学・神学的に解釈する方法論","宗教学・神学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Biblical_hermeneutics",now(),now()),
    (uid(),"死後生の信仰","Belief in Afterlife","天国・地獄・天国・輪廻等の死後の存在への信仰の比較宗教学","宗教学・神学","Global_Synthesis",1871,"https://en.wikipedia.org/wiki/Afterlife",now(),now()),
    (uid(),"神秘主義比較研究","Comparative Mysticism","異なる宗教伝統の神秘的経験の共通性と相違を研究する比較宗教学","宗教学・神学","Global_Synthesis",1960,"https://en.wikipedia.org/wiki/Mysticism",now(),now()),
    (uid(),"祈りの宗教学","Study of Prayer","祈りの形態・心理・社会的機能を比較宗教学的に分析する研究","宗教学・神学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Prayer",now(),now()),
    (uid(),"聖地巡礼","Pilgrimage","世界各地の宗教伝統における聖地への旅の意味・実践・社会的機能","宗教学・神学","Global_Synthesis",1978,"https://en.wikipedia.org/wiki/Pilgrimage",now(),now()),
]

def main():
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA journal_mode=WAL")
    cur = con.cursor()

    existing = set(r[0] for r in cur.execute("SELECT name_en FROM humanities_concept"))
    print(f"既存件数: {len(existing)}")

    inserted = skipped = 0
    batch = []

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
