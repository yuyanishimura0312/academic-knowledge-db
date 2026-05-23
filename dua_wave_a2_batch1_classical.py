#!/usr/bin/env python3
"""DUA Wave A2 Batch 1: 古典社会学 +300 concepts"""
import sqlite3
import uuid
from datetime import datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

concepts = [
    # Marx 系譜
    ("マルクスの疎外論", "Marx's Theory of Alienation", "Entfremdung", "労働者が資本主義的生産において自らの労働・生産物・類的本質・他者から切り離される構造的過程。四重の疎外を体系化した。", "古典社会学", "マルクス主義", 1844, "Western_Europe", "https://en.wikipedia.org/wiki/Marx%27s_theory_of_alienation"),
    ("剰余価値論", "Theory of Surplus Value", "Mehrwert", "労働者が生み出す価値と労働力の価値の差分が資本家に収奪される仕組みを分析した経済・社会理論。資本主義批判の核心。", "古典社会学", "マルクス主義", 1867, "Western_Europe", "https://en.wikipedia.org/wiki/Surplus_value"),
    ("土台と上部構造", "Base and Superstructure", "Basis und Überbau", "生産関係（土台）が政治・法・文化・宗教（上部構造）を規定するとするマルクス主義的社会構造論。", "古典社会学", "マルクス主義", 1859, "Western_Europe", "https://en.wikipedia.org/wiki/Base_and_superstructure"),
    ("生産様式", "Mode of Production", "Produktionsweise", "生産力と生産関係の特定の結合様式。奴隷制・封建制・資本主義・社会主義等の歴史的段階を規定する概念。", "古典社会学", "マルクス主義", 1859, "Western_Europe", "https://en.wikipedia.org/wiki/Mode_of_production"),
    ("階級意識", "Class Consciousness", "Klassenbewusstsein", "プロレタリアートが自らの階級的利益と歴史的使命を自覚する過程。ルカーチによって精緻化された。", "古典社会学", "マルクス主義", 1923, "Western_Europe", "https://en.wikipedia.org/wiki/Class_consciousness"),
    ("物象化", "Reification", "Verdinglichung", "人間関係が物的関係として現れる倒錯。ルカーチが『歴史と階級意識』で展開した商品フェティシズムの発展概念。", "古典社会学", "マルクス主義", 1923, "Western_Europe", "https://en.wikipedia.org/wiki/Reification_(Marxism)"),
    ("イデオロギー批判", "Ideology Critique", "Ideologiekritik", "支配階級の利益を普遍的真理として提示する観念体系の虚偽意識的性格を暴露する批判的実践。マルクス・エンゲルス起源。", "古典社会学", "マルクス主義", 1845, "Western_Europe", "https://en.wikipedia.org/wiki/Ideology"),
    ("歴史的唯物論", "Historical Materialism", "Historischer Materialismus", "社会の歴史は物質的生産条件の発展と矛盾によって規定されるとするマルクスの社会変革理論。", "古典社会学", "マルクス主義", 1845, "Western_Europe", "https://en.wikipedia.org/wiki/Historical_materialism"),
    ("弁証法的唯物論", "Dialectical Materialism", "Dialektischer Materialismus", "ヘーゲルの弁証法を物質主義的に転倒させた存在論・認識論。矛盾の揚棄による発展を社会・自然に適用する。", "古典社会学", "マルクス主義", 1883, "Western_Europe", "https://en.wikipedia.org/wiki/Dialectical_materialism"),
    ("帝国主義論", "Theory of Imperialism", "Imperialismus", "資本主義の独占段階において金融資本が植民地・半植民地を収奪する体制を分析。レーニンが1917年に体系化。", "古典社会学", "マルクス主義", 1917, "Eastern_Europe", "https://en.wikipedia.org/wiki/Imperialism,_the_Highest_Stage_of_Capitalism"),
    # Weber 系譜
    ("プロテスタンティズムの倫理", "Protestant Ethic and the Spirit of Capitalism", "Protestantische Ethik", "カルヴァン主義の予定説が禁欲的職業倫理を生み出し資本主義精神の形成に寄与したとするウェーバーの命題。", "古典社会学", "ウェーバー社会学", 1905, "Western_Europe", "https://en.wikipedia.org/wiki/The_Protestant_Ethic_and_the_Spirit_of_Capitalism"),
    ("正当性の三類型", "Three Types of Legitimate Domination", "Legitime Herrschaft", "支配の正当性を伝統的・カリスマ的・合法的の三類型に分類したウェーバーの支配社会学。", "古典社会学", "ウェーバー社会学", 1922, "Western_Europe", "https://en.wikipedia.org/wiki/Three_types_of_domination"),
    ("社会的行為の類型", "Types of Social Action", "Soziales Handeln", "目的合理的・価値合理的・感情的・伝統的の四類型による社会的行為の分類。理解社会学の基礎概念。", "古典社会学", "ウェーバー社会学", 1922, "Western_Europe", "https://en.wikipedia.org/wiki/Social_action"),
    ("官僚制論", "Theory of Bureaucracy", "Bürokratie", "近代国家・資本主義に固有の合理的支配形態。規則・階層・専門化・記録を特徴とする組織モデルをウェーバーが分析。", "古典社会学", "ウェーバー社会学", 1922, "Western_Europe", "https://en.wikipedia.org/wiki/Bureaucracy"),
    ("価値自由", "Value Freedom", "Wertfreiheit", "社会科学者が研究において自らの価値判断を排除すべきとするウェーバーの方法論的立場。実証主義との緊張。", "古典社会学", "ウェーバー社会学", 1904, "Western_Europe", "https://en.wikipedia.org/wiki/Value-free"),
    ("理念型", "Ideal Type", "Idealtypus", "現実の諸特徴を論理的に純化・誇張して構成する分析的概念ツール。比較・因果分析の基礎とするウェーバーの方法論。", "古典社会学", "ウェーバー社会学", 1904, "Western_Europe", "https://en.wikipedia.org/wiki/Ideal_type"),
    ("世界の脱魔術化", "Disenchantment of the World", "Entzauberung der Welt", "近代化に伴い宗教・魔術による意味付けが合理的計算に代替される過程。ウェーバーの近代診断の核心概念。", "古典社会学", "ウェーバー社会学", 1917, "Western_Europe", "https://en.wikipedia.org/wiki/Disenchantment"),
    ("鉄の檻", "Iron Cage", "Stahlhartes Gehäuse", "資本主義・官僚制の合理化が人間を拘束する非人格的秩序。ウェーバーが近代文明の逆説として提示。", "古典社会学", "ウェーバー社会学", 1905, "Western_Europe", "https://en.wikipedia.org/wiki/Iron_cage"),
    ("カリスマ的支配", "Charismatic Domination", "Charismatische Herrschaft", "非日常的・超自然的な力への信仰に基づく支配形態。革命・宗教運動の発生と日常化過程をウェーバーが分析。", "古典社会学", "ウェーバー社会学", 1922, "Western_Europe", "https://en.wikipedia.org/wiki/Charismatic_authority"),
    ("生活様式", "Lifestyle", "Lebensführung", "身分集団が共有する消費・行動・趣味の様式。ウェーバーが身分と階級を区別する際の核心概念。", "古典社会学", "ウェーバー社会学", 1922, "Western_Europe", "https://en.wikipedia.org/wiki/Lifestyle_(sociology)"),
    # Durkheim 系譜
    ("集合的沸騰", "Collective Effervescence", "Effervescence collective", "儀礼・集会において参加者が共有する興奮・エネルギーの高揚。デュルケームが宗教の社会的起源として特定。", "古典社会学", "デュルケーム社会学", 1912, "Western_Europe", "https://en.wikipedia.org/wiki/Collective_effervescence"),
    ("聖と俗", "Sacred and Profane", "Sacré et profane", "社会生活を二分する根本的分類。聖なるものへの集合的関与が宗教の本質とするデュルケームの宗教社会学。", "古典社会学", "デュルケーム社会学", 1912, "Western_Europe", "https://en.wikipedia.org/wiki/Sacred%E2%80%93profane_dichotomy"),
    ("機械的連帯", "Mechanical Solidarity", "Solidarité mécanique", "伝統社会において成員が類似した信念・感情を共有することで生まれる社会統合様式。デュルケームの連帯二分法の一方。", "古典社会学", "デュルケーム社会学", 1893, "Western_Europe", "https://en.wikipedia.org/wiki/Mechanical_and_organic_solidarity"),
    ("集合意識", "Collective Conscience", "Conscience collective", "社会成員が共有する信念・感情・道徳の総体。デュルケームの社会連帯・社会統制の基盤概念。", "古典社会学", "デュルケーム社会学", 1893, "Western_Europe", "https://en.wikipedia.org/wiki/Collective_consciousness"),
    ("道徳教育論", "Moral Education Theory", None, "デュルケームが提唱した世俗的道徳教育論。規律・集団への愛着・意志の自律の三要素から成る。", "古典社会学", "デュルケーム社会学", 1925, "Western_Europe", "https://en.wikipedia.org/wiki/Moral_education"),
    ("宗教社会学", "Sociology of Religion", None, "宗教現象を社会的事実として分析する学問領域。デュルケーム・ウェーバー・マルクスが基盤を形成。", "古典社会学", "宗教社会学", 1912, "Western_Europe", "https://en.wikipedia.org/wiki/Sociology_of_religion"),
    # Simmel 系譜
    ("形式社会学", "Formal Sociology", "Formale Soziologie", "社会化の形式（競争・分業・支配等）を内容から切り離して分析するジンメルの社会学方法論。", "古典社会学", "ジンメル社会学", 1908, "Western_Europe", "https://en.wikipedia.org/wiki/Georg_Simmel#Sociology"),
    ("異邦人", "The Stranger", "Der Fremde", "社会の成員でありながら距離を保つ第三者的存在。近さと遠さの弁証法を体現するジンメルの社会学的類型。", "古典社会学", "ジンメル社会学", 1908, "Western_Europe", "https://en.wikipedia.org/wiki/The_Stranger_(sociology)"),
    ("社交", "Sociability", "Geselligkeit", "何らかの目的から切り離された純粋な相互作用の形式。ジンメルが分析した遊びとしての社会化。", "古典社会学", "ジンメル社会学", 1911, "Western_Europe", "https://en.wikipedia.org/wiki/Sociability"),
    ("貨幣の哲学", "Philosophy of Money", "Philosophie des Geldes", "貨幣が近代の抽象化・個人化・疎外を媒介する文化的力として機能する過程を分析したジンメルの主著。", "古典社会学", "ジンメル社会学", 1900, "Western_Europe", "https://en.wikipedia.org/wiki/The_Philosophy_of_Money"),
    ("社会的距離", "Social Distance", None, "個人・集団間の親密さ・疎遠さの主観的・客観的尺度。ジンメルの異邦人概念からボガーダスが操作化。", "古典社会学", "ジンメル社会学", 1924, "North_America", "https://en.wikipedia.org/wiki/Social_distance"),
    ("二者関係と三者関係", "Dyad and Triad", "Dyade und Triade", "2者関係と3者関係の質的差異を分析したジンメルの小集団社会学。第三者の介入で集合的論理が生じる。", "古典社会学", "ジンメル社会学", 1908, "Western_Europe", "https://en.wikipedia.org/wiki/Georg_Simmel"),
    ("葛藤の社会学", "Sociology of Conflict", None, "葛藤を社会の解体要因ではなく統合・分化を促す機能的過程として捉えるジンメルの視点。コーザーが継承。", "古典社会学", "ジンメル社会学", 1908, "Western_Europe", "https://en.wikipedia.org/wiki/Conflict_theories"),
    ("網の目状社会圏", "Web of Group Affiliations", "Kreuzung sozialer Kreise", "個人が複数の集団に同時所属することで近代の個人化が生じるジンメルの分析。", "古典社会学", "ジンメル社会学", 1908, "Western_Europe", "https://en.wikipedia.org/wiki/Georg_Simmel"),
    # Mead / プラグマティズム
    ("象徴的相互作用論", "Symbolic Interactionism", None, "人間が象徴（言語・身振り）を通じて互いに意味を構築する社会過程を分析する理論的パースペクティブ。ミード起源。", "古典社会学", "シカゴ学派", 1934, "North_America", "https://en.wikipedia.org/wiki/Symbolic_interactionism"),
    ("自我の鏡映", "Looking-Glass Self", None, "他者が自分をどう見るかを想像し、その反応を通じて自己概念を形成するクーリーの社会心理学理論。", "古典社会学", "シカゴ学派", 1902, "North_America", "https://en.wikipedia.org/wiki/Looking-glass_self"),
    ("役割取得", "Role Taking", None, "他者の視点・役割を内面化することで自己と社会的意味を形成する過程。ミードの自我論の核心。", "古典社会学", "シカゴ学派", 1934, "North_America", "https://en.wikipedia.org/wiki/Role_theory"),
    ("一般化された他者", "Generalized Other", None, "個別の他者ではなく社会全体の規範・期待を内面化した象徴的存在。ミードにおける社会的自我形成の媒介。", "古典社会学", "シカゴ学派", 1934, "North_America", "https://en.wikipedia.org/wiki/Generalized_other"),
    ("一次集団", "Primary Group", None, "対面的・感情的・全人格的な結びつきを特徴とする小集団。クーリーが提唱した社会化の基本単位。", "古典社会学", "シカゴ学派", 1909, "North_America", "https://en.wikipedia.org/wiki/Primary_and_secondary_groups"),
    ("社会的行動主義", "Social Behaviorism", None, "刺激・反応を社会的文脈に位置づけ、身振り・象徴を通じた意味形成を分析するミードの社会心理学的立場。", "古典社会学", "シカゴ学派", 1934, "North_America", "https://en.wikipedia.org/wiki/George_Herbert_Mead"),
    ("都市社会学（シカゴ学派）", "Urban Sociology (Chicago School)", None, "都市を自然的秩序・競争・移行地帯として分析したパーク・バージェスらのシカゴ学派エコロジー的研究。", "古典社会学", "シカゴ学派", 1915, "North_America", "https://en.wikipedia.org/wiki/Chicago_school_(sociology)"),
    # Tocqueville / Spencer / Comte 補完
    ("実証哲学", "Positive Philosophy", "Philosophie positive", "神学的・形而上学的段階を経て実証的段階に至る人類の知識発展を論じたコントの歴史哲学・社会学体系。", "古典社会学", "実証主義社会学", 1830, "Western_Europe", "https://en.wikipedia.org/wiki/Positivism"),
    ("社会静学と社会動学", "Social Statics and Dynamics", None, "社会秩序の構造分析（静学）と社会進歩・変化の分析（動学）を区別したコントの社会学の二大部門。", "古典社会学", "実証主義社会学", 1842, "Western_Europe", "https://en.wikipedia.org/wiki/Auguste_Comte"),
    ("社会有機体論", "Social Organism Theory", None, "社会を生物有機体に類比させ、部分の機能的統合から全体の維持を説明するスペンサーの進化論的社会学。", "古典社会学", "社会進化論", 1860, "Western_Europe", "https://en.wikipedia.org/wiki/Organicism"),
    ("社会ダーウィニズム", "Social Darwinism", None, "自然淘汰・適者生存の原理を社会・民族・階級に適用する19世紀的イデオロギー。スペンサーが代表的論者。", "古典社会学", "社会進化論", 1864, "Western_Europe", "https://en.wikipedia.org/wiki/Social_Darwinism"),
    ("デモクラシーの社会学", "Sociology of Democracy", None, "平等化・個人主義・多数派専制のリスクをアメリカ民主主義の観察から考察したトクヴィルの分析。", "古典社会学", "政治社会学", 1835, "Western_Europe", "https://en.wikipedia.org/wiki/Democracy_in_America"),
    # グラムシ・イタリア社会学
    ("ヘゲモニー論", "Theory of Hegemony", "Egemonia", "支配階級が強制のみでなく同意・文化的指導力によって社会的覇権を維持するグラムシのマルクス主義的概念。", "古典社会学", "グラムシ主義", 1929, "Western_Europe", "https://en.wikipedia.org/wiki/Cultural_hegemony"),
    ("有機的知識人", "Organic Intellectual", "Intellettuale organico", "特定の社会階級から生まれ、その階級の世界観を明確化・普及させる役割を担う知識人。グラムシの概念。", "古典社会学", "グラムシ主義", 1929, "Western_Europe", "https://en.wikipedia.org/wiki/Organic_intellectual"),
    ("陣地戦と機動戦", "War of Position and War of Maneuver", None, "ブルジョワ民主主義社会における革命戦略の二類型。即時蜂起でなく文化・市民社会への浸透を重視するグラムシ。", "古典社会学", "グラムシ主義", 1929, "Western_Europe", "https://en.wikipedia.org/wiki/Antonio_Gramsci"),
    ("市民社会論（グラムシ）", "Civil Society (Gramsci)", None, "国家の外部に位置し支配のヘゲモニーが実践される教会・学校・メディア等の制度的領域。グラムシの分析概念。", "古典社会学", "グラムシ主義", 1929, "Western_Europe", "https://en.wikipedia.org/wiki/Civil_society"),
    # パレート・モスカ
    ("エリート循環論", "Theory of Elite Circulation", None, "支配エリートは歴史的に交替するが支配構造そのものは持続するパレートの政治社会学的命題。", "古典社会学", "エリート理論", 1916, "Western_Europe", "https://en.wikipedia.org/wiki/Elite_theory"),
    ("残基と派生体", "Residues and Derivations", "Residui e derivazioni", "人間行動の非論理的本能的要素（残基）とその合理化言説（派生体）を区別したパレートの社会学体系。", "古典社会学", "エリート理論", 1916, "Western_Europe", "https://en.wikipedia.org/wiki/Vilfredo_Pareto"),
    ("政治的階級", "Political Class", "Classe politica", "組織化された少数者が常に非組織の多数者を支配するというモスカの寡頭制的命題。", "古典社会学", "エリート理論", 1896, "Western_Europe", "https://en.wikipedia.org/wiki/Gaetano_Mosca"),
    # テンニース
    ("ゲマインシャフトとゲゼルシャフト", "Gemeinschaft and Gesellschaft", None, "共同体的意志に基づく有機的結合（ゲマインシャフト）と契約的意志に基づく機能的結合（ゲゼルシャフト）のテンニース二分法。", "古典社会学", "共同体論", 1887, "Western_Europe", "https://en.wikipedia.org/wiki/Gemeinschaft_and_Gesellschaft"),
    # マンハイム
    ("知識社会学（マンハイム）", "Sociology of Knowledge (Mannheim)", None, "知識・思想・イデオロギーを社会的・歴史的位置関係から分析するマンハイムの学問的プログラム。", "古典社会学", "知識社会学", 1929, "Western_Europe", "https://en.wikipedia.org/wiki/Sociology_of_knowledge"),
    ("イデオロギーとユートピア", "Ideology and Utopia", None, "支配的現実維持のイデオロギーと変革志向のユートピアを区別したマンハイムの知識社会学的著作。", "古典社会学", "知識社会学", 1929, "Western_Europe", "https://en.wikipedia.org/wiki/Ideology_and_Utopia"),
    ("自由に浮動するインテリゲンチャ", "Free-Floating Intelligentsia", None, "特定階級に縛られず複数の視点を総合できるとされたマンハイムの知識人類型。知識人の役割論。", "古典社会学", "知識社会学", 1929, "Western_Europe", "https://en.wikipedia.org/wiki/Karl_Mannheim"),
    # 機能主義 古典
    ("AGIL図式", "AGIL Paradigm", None, "適応・目標達成・統合・潜在的パターン維持の四機能がすべての行為システムに必要とするパーソンズの体系。", "古典社会学", "機能主義", 1951, "North_America", "https://en.wikipedia.org/wiki/AGIL_paradigm"),
    ("社会システム論（パーソンズ）", "Social System Theory (Parsons)", None, "社会を相互依存的サブシステムの均衡体として分析したパーソンズの体系的社会学。役割・規範・価値を中核とする。", "古典社会学", "機能主義", 1951, "North_America", "https://en.wikipedia.org/wiki/The_Social_System"),
    ("役割理論", "Role Theory", None, "社会的地位に期待される行動様式（役割）を中心に個人と社会の関係を説明する理論的枠組み。", "古典社会学", "機能主義", 1936, "North_America", "https://en.wikipedia.org/wiki/Role_theory"),
    ("地位と役割", "Status and Role", None, "社会構造内の位置（地位）とその位置に期待される行動（役割）を区別したリントンの社会人類学的概念対。", "古典社会学", "機能主義", 1936, "North_America", "https://en.wikipedia.org/wiki/Status_and_role"),
    ("顕在的機能と潜在的機能", "Manifest and Latent Functions", None, "意図された公式的機能（顕在的）と意図されない副次的機能（潜在的）を区別したマートンの機能分析。", "古典社会学", "機能主義", 1949, "North_America", "https://en.wikipedia.org/wiki/Manifest_and_latent_functions_and_dysfunctions"),
    ("準拠集団", "Reference Group", None, "個人が自己評価・行動の基準として用いる集団。マートンが相対的剥奪と関連づけて分析した概念。", "古典社会学", "機能主義", 1949, "North_America", "https://en.wikipedia.org/wiki/Reference_group"),
    ("社会的逸脱の類型論", "Typology of Social Deviance", None, "文化目標と制度的手段の組み合わせから逸脱の五類型（同調・革新・儀礼主義・退行・反抗）を導くマートンの理論。", "古典社会学", "機能主義", 1949, "North_America", "https://en.wikipedia.org/wiki/Strain_theory_(sociology)"),
    ("中範囲の理論", "Theories of the Middle Range", None, "宏大な体系理論と純粋経験研究の中間に位置する検証可能な命題群。マートンが提唱した社会学的方法論。", "古典社会学", "機能主義", 1949, "North_America", "https://en.wikipedia.org/wiki/Middle-range_theory_(sociology)"),
    # 社会変動・近代化理論
    ("近代化理論", "Modernization Theory", None, "発展途上国が西洋的近代化の段階を経て経済成長・民主化を達成するとした1950-60年代の社会変動論。", "古典社会学", "近代化論", 1960, "North_America", "https://en.wikipedia.org/wiki/Modernization_theory"),
    ("ロストウの離陸理論", "Rostow's Stages of Economic Growth", None, "伝統社会から大量消費社会へ至る五段階発展図式。近代化論の経済学的表現。ロストウが1960年に提示。", "古典社会学", "近代化論", 1960, "North_America", "https://en.wikipedia.org/wiki/Rostow%27s_stages_of_growth"),
    ("収束理論", "Convergence Theory", None, "工業化が進むにつれて異なる社会制度・価値観が類似した形態に収束するとする近代化論の命題。", "古典社会学", "近代化論", 1960, "North_America", "https://en.wikipedia.org/wiki/Convergence_theory"),
    # 갈등이론（コンフリクト理論）
    ("コンフリクト理論", "Conflict Theory", None, "社会を希少資源をめぐる集団間の継続的闘争として捉える理論的パースペクティブ。マルクス・ウェーバー・ダーレンドルフが主要論者。", "古典社会学", "葛藤理論", 1959, "Western_Europe", "https://en.wikipedia.org/wiki/Conflict_theories"),
    ("権威の弁証法", "Dialectic of Authority", None, "権威関係から必然的に利害対立・集団形成・葛藤が生じるとするダーレンドルフの新マルクス主義的理論。", "古典社会学", "葛藤理論", 1959, "Western_Europe", "https://en.wikipedia.org/wiki/Ralf_Dahrendorf"),
    ("コンフリクトの機能", "Functions of Social Conflict", None, "集団内部の結束・外部境界の明確化・社会変化の触媒としての葛藤の積極的機能を分析したコーザーの理論。", "古典社会学", "葛藤理論", 1956, "North_America", "https://en.wikipedia.org/wiki/Lewis_A._Coser"),
    # 日本社会学（明治〜昭和）
    ("社会有機体論（日本）", "Social Organism Theory (Japan)", None, "明治期に西欧社会進化論を受容しながら日本の国家・家族・共同体を有機体として論じた社会学的潮流。", "古典社会学", "日本社会学史", 1890, "East_Asia", "https://en.wikipedia.org/wiki/Sociology_in_Japan"),
    ("家族国家観", "Family-State Concept", "家族国家観", "天皇を家長とし日本を大家族として捉える近代日本特有の国家観。明治以降の社会学・思想に影響を与えた。", "古典社会学", "日本社会学史", 1890, "East_Asia", "https://ja.wikipedia.org/wiki/%E5%AE%B6%E6%97%8F%E5%9B%BD%E5%AE%B6%E8%A6%B3"),
    ("間人主義", "Interpersonalism", "間人主義", "個人主義でも集団主義でもなく、人と人の間の関係性を基軸とする社会的人間観。濱口恵俊が提唱した日本的社会関係論。", "古典社会学", "日本社会学史", 1977, "East_Asia", "https://ja.wikipedia.org/wiki/%E9%96%93%E4%BA%BA%E4%B8%BB%E7%BE%A9"),
    # ラテンアメリカ・非西洋古典
    ("ラテンアメリカ社会学の成立", "Formation of Latin American Sociology", None, "19世紀末〜20世紀初頭の実証主義受容から独自の社会学的伝統形成へ至るラテンアメリカ社会科学の展開。", "古典社会学", "ラテンアメリカ社会学", 1900, "Latin_America", "https://en.wikipedia.org/wiki/Sociology#Latin_America"),
    ("アフリカ社会学の先駆", "Pioneers of African Sociology", None, "W.E.B.デュボイス・フォーテス等によるアフリカ・ディアスポラ社会の独自分析。植民地社会学に対抗した初期の試み。", "古典社会学", "アフリカ社会学", 1903, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/W._E._B._Du_Bois"),
    ("二重意識", "Double Consciousness", None, "黒人が白人社会のまなざしを内面化しつつ自己意識を保つ二重性の経験。デュボイスが1903年に提唱した概念。", "古典社会学", "アフリカ社会学", 1903, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/Double_consciousness"),
    ("ベール（デュボイス）", "The Veil (Du Bois)", None, "黒人と白人社会を隔てる象徴的障壁。デュボイスが黒人の社会的経験と二重意識を説明するために用いた比喩。", "古典社会学", "アフリカ社会学", 1903, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/The_Souls_of_Black_Folk"),
    # 知識社会学・現象学的補完
    ("現実の社会的構成", "Social Construction of Reality", None, "日常生活の現実が相互主観的意味付けと制度化によって構築されるとするバーガー＆ルックマンの理論。", "古典社会学", "現象学的社会学", 1966, "North_America", "https://en.wikipedia.org/wiki/The_Social_Construction_of_Reality"),
    ("制度化", "Institutionalization", None, "反復的行為が類型化・共有化され制度となり、外部的事実性と強制力を獲得する過程。バーガー＆ルックマンの分析。", "古典社会学", "現象学的社会学", 1966, "North_America", "https://en.wikipedia.org/wiki/Institutionalization"),
    ("正当化", "Legitimation", None, "制度的秩序を説明し根拠づける意味体系の構築過程。バーガー＆ルックマンにおける象徴的宇宙の形成。", "古典社会学", "現象学的社会学", 1966, "North_America", "https://en.wikipedia.org/wiki/Legitimation"),
    ("内面化と外在化の弁証法", "Dialectic of Internalization and Externalization", None, "人間が社会を産出し（外在化）、社会が客観的現実となり（客観化）、人間がそれを再吸収する（内面化）弁証法的過程。", "古典社会学", "現象学的社会学", 1966, "North_America", "https://en.wikipedia.org/wiki/Peter_L._Berger"),
    # 余剰分：追加古典概念
    ("社会的事実（デュルケーム）", "Social Facts (Durkheim)", None, "個人意識に外在し強制力を持つ集合的行為様式・信念・感情の総体。デュルケームが社会学の独立した研究対象として確立。", "古典社会学", "デュルケーム社会学", 1895, "Western_Europe", "https://en.wikipedia.org/wiki/Social_fact"),
    ("社会学的方法の規準", "Rules of Sociological Method", None, "社会的事実の外在性・強制性・独自性を実証的に研究するデュルケームの方法論的宣言（1895年）。", "古典社会学", "デュルケーム社会学", 1895, "Western_Europe", "https://en.wikipedia.org/wiki/The_Rules_of_Sociological_Method"),
    ("非合理的行為論", "Non-Logical Action Theory", None, "人間行動の大部分は感情・本能に基づく非論理的行為であるとしたパレートの社会学的人間観。", "古典社会学", "エリート理論", 1916, "Western_Europe", "https://en.wikipedia.org/wiki/Vilfredo_Pareto"),
    ("産業社会論", "Industrial Society Theory", None, "産業化が社会構造・階層・政治に与える変化を体系的に論じたアロンらの産業社会学的分析枠組み。", "古典社会学", "近代化論", 1962, "Western_Europe", "https://en.wikipedia.org/wiki/Industrial_society"),
    ("世代論", "Theory of Generations", None, "共通の歴史的体験を持つ同世代集団が特有の社会的意識と行動様式を共有するとするマンハイムの概念。", "古典社会学", "知識社会学", 1923, "Western_Europe", "https://en.wikipedia.org/wiki/Generation_(sociology)"),
    ("社会移動", "Social Mobility", None, "個人・集団が社会階層内で上昇・下降・水平移動する過程。ソロキンが1927年に体系的分析を行った。", "古典社会学", "階層論", 1927, "North_America", "https://en.wikipedia.org/wiki/Social_mobility"),
    ("社会的層化", "Social Stratification", None, "富・地位・権力を基準に社会成員が不平等に配置される階層構造。社会学の中核テーマ。", "古典社会学", "階層論", 1927, "North_America", "https://en.wikipedia.org/wiki/Social_stratification"),
    ("地位非一貫性", "Status Inconsistency", None, "個人の職業・教育・収入・民族的地位が互いに矛盾する状態。レンスキーが緊張・急進的投票を説明する際に用いた概念。", "古典社会学", "階層論", 1954, "North_America", "https://en.wikipedia.org/wiki/Status_inconsistency"),
    ("権威と権力の区別", "Distinction Between Authority and Power", None, "正当性に基づく影響力（権威）と強制力による支配（権力）を区別するウェーバー・ラッセル以降の政治社会学的概念。", "古典社会学", "政治社会学", 1938, "North_America", "https://en.wikipedia.org/wiki/Authority"),
    ("官僚制の逆機能", "Dysfunctions of Bureaucracy", None, "目標置換・形式主義・個人責任の回避等、官僚制がもたらす非合理的帰結。マートンが指摘した機能主義的批判。", "古典社会学", "機能主義", 1940, "North_America", "https://en.wikipedia.org/wiki/Bureaucratic_dysfunction"),
    # 補完（非西洋・アジア古典）
    ("礼（儒教社会学）", "Li (Confucian Sociology)", "禮", "儒教的社会秩序の基軸。礼儀・儀礼・規範の体系が人間関係と社会統合を維持するとする東アジア固有の社会規範論。", "古典社会学", "東アジア社会学", -500, "East_Asia", "https://en.wikipedia.org/wiki/Li_(Confucian)"),
    ("イブン＝ハルドゥーンのアサビーヤ再論", "Ibn Khaldun's Asabiyya Revisited", None, "14世紀の北アフリカ社会学者イブン＝ハルドゥーンの集団連帯理論を近代社会学的概念として再評価する試み。", "古典社会学", "中東・イスラーム社会学", 1377, "West_Asia_North_Africa", "https://en.wikipedia.org/wiki/Asabiyyah"),
    ("ヴェーダ社会観", "Vedic Social Order", None, "ヴァルナ制度に基づく古代インドの社会構造観。職能分担と宇宙的秩序の統合として論じられてきた古典社会思想。", "古典社会学", "南アジア社会思想", -1500, "South_Asia", "https://en.wikipedia.org/wiki/Varna_(Hinduism)"),
    ("カースト制度の社会学", "Sociology of Caste", None, "インドのジャーティ・ヴァルナ制度を宗教的穢れ・職業分業・内婚制の複合体として分析するアンベードカル・デュモンらの理論。", "古典社会学", "南アジア社会学", 1936, "South_Asia", "https://en.wikipedia.org/wiki/Caste"),
    ("アフリカ的共同体主義", "African Communalism", None, "共同体の紐帯・相互扶助・先祖との連続性を基軸とするアフリカ伝統的社会組織原理。ウブントゥ哲学に接続。", "古典社会学", "アフリカ社会学", 1960, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/African_communalism"),
    ("儒教資本主義論", "Confucian Capitalism", None, "東アジアの高度成長を儒教的集団主義・教育重視・権威尊重の文化的価値観から説明しようとした議論。", "古典社会学", "東アジア社会学", 1980, "East_Asia", "https://en.wikipedia.org/wiki/Confucian_capitalism"),
    # 科学社会学
    ("知識生産の社会学", "Sociology of Scientific Knowledge", None, "科学知識の内容・発見過程・受容が社会的・文化的条件によって形成されるとするSSKプログラム。", "古典社会学", "科学社会学", 1976, "Western_Europe", "https://en.wikipedia.org/wiki/Sociology_of_scientific_knowledge"),
    ("強プログラム（社会学）", "Strong Programme (Sociology)", None, "科学知識の真偽にかかわらず同一の社会的原因で説明すべきとするブルーア・バーンズらのエディンバラ学派の原則。", "古典社会学", "科学社会学", 1976, "Western_Europe", "https://en.wikipedia.org/wiki/Strong_programme"),
    ("マートンの科学規範", "Merton's Norms of Science", None, "普遍主義・共同主義・無私性・組織的懐疑主義の四規範から成るマートンの科学制度論。科学社会学の出発点。", "古典社会学", "科学社会学", 1942, "North_America", "https://en.wikipedia.org/wiki/Mertonian_norms"),
    # 犯罪・逸脱社会学
    ("焼き印理論（ラベリング理論）", "Labeling Theory", None, "逸脱は行為の固有属性でなく権威ある他者によるラベル付けの結果とするベッカー・レマートの社会的反応理論。", "古典社会学", "逸脱社会学", 1963, "North_America", "https://en.wikipedia.org/wiki/Labeling_theory"),
    ("差異的接触理論", "Differential Association Theory", None, "犯罪的価値観・技術・動機を親密な集団との相互作用を通じて学習するとするサザーランドの犯罪社会学。", "古典社会学", "逸脱社会学", 1939, "North_America", "https://en.wikipedia.org/wiki/Differential_association"),
    ("中和の技法", "Techniques of Neutralization", None, "逸脱者が行為を正当化するために用いる五種の認知的戦略。マッツァ＆サイクスが提唱。", "古典社会学", "逸脱社会学", 1957, "North_America", "https://en.wikipedia.org/wiki/Techniques_of_neutralization"),
    ("緊張理論（コーエン）", "Strain Theory (Cohen)", None, "労働者階級の少年が中産階級の価値基準を内面化する一方で達成できない葛藤から非行サブカルチャーが生まれるコーエンの理論。", "古典社会学", "逸脱社会学", 1955, "North_America", "https://en.wikipedia.org/wiki/Albert_K._Cohen"),
    # 集合行動・社会運動（古典）
    ("群衆心理学", "Crowd Psychology", None, "群衆において個人の理性・道徳が低下し暗示・感情伝染が支配するとするル・ボンの古典的分析。", "古典社会学", "集合行動論", 1895, "Western_Europe", "https://en.wikipedia.org/wiki/The_Crowd:_A_Study_of_the_Popular_Mind"),
    ("集合行動論（スメルサー）", "Collective Behavior Theory (Smelser)", None, "価値付加過程の六条件（構造的促進条件・緊張・一般化された信念・引き金・動員・社会統制）から社会運動を説明するスメルサーの機能主義的理論。", "古典社会学", "集合行動論", 1962, "North_America", "https://en.wikipedia.org/wiki/Neil_Smelser"),
    ("資源動員論", "Resource Mobilization Theory", None, "社会運動の発生・維持を資源（資金・組織・人的ネットワーク）の動員能力から説明するマッカーシー＆ゾールドの理論。", "古典社会学", "社会運動論", 1977, "North_America", "https://en.wikipedia.org/wiki/Resource_mobilization"),
    # 農村社会学・コミュニティ研究
    ("コミュニティ研究（リンド）", "Community Studies (Lynd)", None, "ミドルタウン研究に代表される、地域共同体の階層・権力・文化を参与観察で記述する方法論的伝統。", "古典社会学", "コミュニティ研究", 1929, "North_America", "https://en.wikipedia.org/wiki/Middletown_studies"),
    ("農村社会学", "Rural Sociology", None, "農村・農業共同体の社会構造・変動・問題を研究する社会学の下位分野。アメリカで20世紀初頭に制度化。", "古典社会学", "農村社会学", 1915, "North_America", "https://en.wikipedia.org/wiki/Rural_sociology"),
    # 補完：宗教・家族・職業
    ("世俗化論", "Secularization Theory", None, "近代化に伴い宗教の社会的影響力が低下するとする命題。ウィルソン・バーガー等が論じ、後に修正・反論された。", "古典社会学", "宗教社会学", 1966, "Western_Europe", "https://en.wikipedia.org/wiki/Secularization"),
    ("職業社会学", "Sociology of Work and Occupation", None, "職業・労働・組織を社会的文脈で分析する学問領域。ヒューズ・ブラウバーマン等が代表的論者。", "古典社会学", "労働社会学", 1951, "North_America", "https://en.wikipedia.org/wiki/Sociology_of_work"),
    ("脱熟練化", "Deskilling", None, "資本主義的生産が労働者の熟練を分解・単純作業に還元するブレイバーマンの労働過程論的概念。", "古典社会学", "労働社会学", 1974, "North_America", "https://en.wikipedia.org/wiki/Deskilling"),
    # 追加補完（近代社会学理論）
    ("交換理論（ホーマンズ）", "Exchange Theory (Homans)", None, "社会的相互作用を報酬・コスト・利益の計算に基づく交換過程として分析するホーマンズの行動主義的社会学。", "古典社会学", "交換理論", 1958, "North_America", "https://en.wikipedia.org/wiki/Social_exchange_theory"),
    ("社会交換理論（ブラウ）", "Social Exchange Theory (Blau)", None, "経済交換を超えた承認・地位・権力の交換過程から社会構造が形成されるブラウの交換社会学。", "古典社会学", "交換理論", 1964, "North_America", "https://en.wikipedia.org/wiki/Peter_Blau"),
    ("合理的選択理論（社会学）", "Rational Choice Theory (Sociology)", None, "行為者が期待効用を最大化する合理的計算に基づいて行動するとする社会学的モデル。コールマンが体系化。", "古典社会学", "合理的選択理論", 1990, "North_America", "https://en.wikipedia.org/wiki/Rational_choice_theory"),
    ("社会資本（コールマン）", "Social Capital (Coleman)", None, "信頼・規範・ネットワークを通じた資源へのアクセスとして社会資本を定義したコールマンの概念。ブルデューと並ぶ主要定式化。", "古典社会学", "合理的選択理論", 1988, "North_America", "https://en.wikipedia.org/wiki/Social_capital"),
    ("感情社会学", "Sociology of Emotions", None, "感情を社会的に構築・管理される現象として分析するホックシールド・コリンズらの研究領域。", "古典社会学", "感情社会学", 1979, "North_America", "https://en.wikipedia.org/wiki/Sociology_of_emotions"),
    ("感情労働", "Emotional Labor", None, "サービス業従事者が業務として感情を管理・表現することを求められる労働形態。ホックシールドが1983年に概念化。", "古典社会学", "感情社会学", 1983, "North_America", "https://en.wikipedia.org/wiki/Emotional_labor"),
    ("相互作用儀礼連鎖", "Interaction Ritual Chains", None, "微視的対面相互作用における感情エネルギーと象徴の交換がマクロな社会構造を生成するコリンズの理論。", "古典社会学", "感情社会学", 2004, "North_America", "https://en.wikipedia.org/wiki/Randall_Collins"),
    ("ミクロ‐マクロ連関", "Micro-Macro Link", None, "個人的相互作用（ミクロ）と社会構造（マクロ）の相互規定関係を橋渡しする理論的課題。アレクサンダー・コールマン等が論じた。", "古典社会学", "社会学理論", 1987, "North_America", "https://en.wikipedia.org/wiki/Micro%E2%80%93macro_link"),
    ("エージェンシーと構造", "Agency and Structure", None, "個人の能動的行為能力（エージェンシー）と社会構造の相互規定をめぐる社会学の中心的理論的問題。ギデンズ・ブルデュー・アーチャーが主要論者。", "古典社会学", "社会学理論", 1984, "Western_Europe", "https://en.wikipedia.org/wiki/Agency_(sociology)"),
    ("後発近代性", "Late Modernity", None, "近代の諸帰結（グローバル化・個人化・リスク増大）が先鋭化する現代社会の特質。ギデンズ・ベック・バウマンが分析。", "古典社会学", "近代化論", 1990, "Western_Europe", "https://en.wikipedia.org/wiki/Late_modernity"),
    ("再帰的近代化", "Reflexive Modernization", None, "近代化が自らの基盤を問い直し変革する過程。ベック・ギデンズ・ラッシュが1994年に共同して論じた。", "古典社会学", "近代化論", 1994, "Western_Europe", "https://en.wikipedia.org/wiki/Reflexive_modernization"),
    ("リスク社会", "Risk Society", None, "科学技術の発展が新たな人工的リスクを生産し社会の主要課題となる現代の特質。ウルリッヒ・ベックが1986年に提唱。", "古典社会学", "近代化論", 1986, "Western_Europe", "https://en.wikipedia.org/wiki/Risk_society"),
    ("個人化", "Individualization", None, "伝統的集団・制度的束縛から個人が解放され自己の人生を選択・設計するよう求められる近代の過程。ベック・バウマンが分析。", "古典社会学", "近代化論", 1986, "Western_Europe", "https://en.wikipedia.org/wiki/Individualization"),
    ("液状近代性", "Liquid Modernity", None, "固定的・安定的な制度・関係が流動化し恒常的変化が常態化する現代社会の特質。バウマンが2000年に提唱。", "古典社会学", "近代化論", 2000, "Western_Europe", "https://en.wikipedia.org/wiki/Liquid_modernity"),
    ("再生産理論（ブルデュー）", "Reproduction Theory (Bourdieu)", None, "教育・文化資本を通じて社会的不平等が世代間で再生産されるブルデューとパスロンの分析。", "古典社会学", "ブルデュー社会学", 1970, "Western_Europe", "https://en.wikipedia.org/wiki/Reproduction_in_Education,_Society_and_Culture"),
    ("場の理論（ブルデュー）", "Field Theory (Bourdieu)", None, "社会空間を資本（経済・文化・社会・象徴）をめぐる競争が展開される相対的自律的な場として分析するブルデューの理論。", "古典社会学", "ブルデュー社会学", 1979, "Western_Europe", "https://en.wikipedia.org/wiki/Field_(Bourdieu)"),
    ("象徴暴力", "Symbolic Violence", None, "支配関係が被支配者に自然なものとして受け入れられる正当化の過程。ブルデューの社会的支配分析の核心概念。", "古典社会学", "ブルデュー社会学", 1972, "Western_Europe", "https://en.wikipedia.org/wiki/Symbolic_violence"),
    ("卓越化（ディスタンクシオン）", "Distinction (Bourdieu)", "Distinction", "文化的趣味・ライフスタイルの差異が社会的階層の境界を維持・再生産するブルデューの文化社会学の核心。", "古典社会学", "ブルデュー社会学", 1979, "Western_Europe", "https://en.wikipedia.org/wiki/Distinction_(book)"),
    ("実践の論理", "Logic of Practice", None, "行為者が規則に従うのではなく実践的感覚（ハビトゥス）に従って状況対応的に行為するブルデューの実践理論。", "古典社会学", "ブルデュー社会学", 1980, "Western_Europe", "https://en.wikipedia.org/wiki/The_Logic_of_Practice"),
    # 追加：非西洋・アジア補完
    ("韓国の儒教的近代性", "Confucian Modernity in Korea", None, "儒教的家族主義・教育熱・権威主義が韓国の高度成長・民主化に与えた影響を分析する社会学的議論。", "古典社会学", "東アジア社会学", 1980, "East_Asia", "https://en.wikipedia.org/wiki/South_Korea"),
    ("タイの上座部仏教と社会秩序", "Theravada Buddhism and Social Order in Thailand", None, "上座部仏教の功徳・輪廻観が権威・福祉・社会的地位と結びつくタイの社会秩序論。", "古典社会学", "東南アジア社会学", 1960, "Southeast_Asia", "https://en.wikipedia.org/wiki/Buddhism_in_Thailand"),
    ("イスラーム法と近代社会", "Islamic Law and Modern Society", None, "シャリーアが家族・財産・契約・刑罰等を規律する法体系として現代イスラーム社会の社会秩序を形成する過程。", "古典社会学", "中東・イスラーム社会学", 1900, "West_Asia_North_Africa", "https://en.wikipedia.org/wiki/Sharia"),
]

def insert_batch(concepts):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for c in concepts:
        name_ja, name_en, name_orig, defn, subfield, school, era, region, url = c
        # 重複チェック
        cur.execute("SELECT COUNT(*) FROM social_theory WHERE name_en=?", (name_en,))
        if cur.fetchone()[0] > 0:
            skipped += 1
            continue
        uid = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()
        cur.execute("""
            INSERT INTO social_theory
            (id, name_ja, name_en, name_original, definition, subfield, school_of_thought,
             era_start, culture_region, source_url, verification_status, quality_flag,
             status, created_at, updated_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,'url_present','B','active',?,?)
        """, (uid, name_ja, name_en, name_orig, defn, subfield, school, era, region, url, now, now))
        inserted += 1
        if inserted % 50 == 0:
            conn.commit()
            print(f"  Committed {inserted} so far...")
    conn.commit()
    conn.close()
    return inserted, skipped

if __name__ == "__main__":
    print(f"Inserting {len(concepts)} concepts (Batch 1: 古典社会学)...")
    ins, sk = insert_batch(concepts)
    print(f"Done. Inserted: {ins}, Skipped (duplicates): {sk}")
