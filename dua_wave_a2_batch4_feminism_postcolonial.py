#!/usr/bin/env python3
"""DUA Wave A2 Batch 4: フェミニズム +300 / ポストコロニアル +250"""
import sqlite3, uuid
from datetime import datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

concepts = [
    # === フェミニズム・ジェンダー理論 ===
    ("第一波フェミニズム", "First-Wave Feminism", None, "19世紀末〜20世紀初頭の参政権・法的平等を中心とした女性解放運動。ウルストンクラフト・スタントン・パンクハースト等。", "フェミニズム・ジェンダー理論", "フェミニズム史", 1848, "Western_Europe", "https://en.wikipedia.org/wiki/First-wave_feminism"),
    ("第二波フェミニズム", "Second-Wave Feminism", None, "1960-80年代の家父長制・セクシュアリティ・労働・身体をめぐる女性解放運動。ベティ・フリーダン・ケイト・ミレット等。", "フェミニズム・ジェンダー理論", "フェミニズム史", 1963, "North_America", "https://en.wikipedia.org/wiki/Second-wave_feminism"),
    ("第三波フェミニズム", "Third-Wave Feminism", None, "1990年代以降の多様性・インターセクショナリティ・ポップカルチャーを取り込んだフェミニズムの展開。レベッカ・ウォーカー等。", "フェミニズム・ジェンダー理論", "フェミニズム史", 1992, "North_America", "https://en.wikipedia.org/wiki/Third-wave_feminism"),
    ("第四波フェミニズム", "Fourth-Wave Feminism", None, "SNS・MeToo運動・交差性を基盤に2010年代以降に台頭したフェミニズムの潮流。デジタルフェミニズム・反ハラスメント。", "フェミニズム・ジェンダー理論", "フェミニズム史", 2012, "Global_Synthesis", "https://en.wikipedia.org/wiki/Fourth-wave_feminism"),
    ("家父長制論", "Theory of Patriarchy", None, "男性支配の制度的・文化的・経済的構造として家父長制を分析するフェミニズムの中核概念。ミレット・ウォルビー等。", "フェミニズム・ジェンダー理論", "ラディカル・フェミニズム", 1970, "North_America", "https://en.wikipedia.org/wiki/Patriarchy"),
    ("性的政治学", "Sexual Politics", None, "男女関係を権力・支配の観点から分析したケイト・ミレットの1970年の著作。家父長制批判の嚆矢。", "フェミニズム・ジェンダー理論", "ラディカル・フェミニズム", 1970, "North_America", "https://en.wikipedia.org/wiki/Sexual_Politics"),
    ("再生産労働の不払い", "Unpaid Reproductive Labor", None, "家事・育児・介護等の再生産労働が資本主義の基盤でありながら不払い・不可視化されるフェミニスト経済学の命題。", "フェミニズム・ジェンダー理論", "社会主義フェミニズム", 1972, "Western_Europe", "https://en.wikipedia.org/wiki/Reproductive_labor"),
    ("賃金と家事（ポーティエ）", "Wages for Housework", None, "家事労働を資本主義的搾取として認識し賃金要求を政治的手段とするポーティエ・フェデリチらの1970年代運動。", "フェミニズム・ジェンダー理論", "社会主義フェミニズム", 1972, "Western_Europe", "https://en.wikipedia.org/wiki/Wages_for_housework"),
    ("魔女・産婆・看護婦（フェデリチ）", "Caliban and the Witch (Federici)", None, "原始的蓄積過程での女性の身体・労働・知識の収奪を魔女狩りと関連づけたフェデリチの歴史的フェミニスト分析。", "フェミニズム・ジェンダー理論", "社会主義フェミニズム", 2004, "North_America", "https://en.wikipedia.org/wiki/Caliban_and_the_Witch"),
    ("ケアの倫理", "Ethics of Care", None, "普遍的義務・権利より具体的関係・応答性・感情を道徳の中心に置くギリガン・ノディングズのフェミニスト倫理学。", "フェミニズム・ジェンダー理論", "フェミニスト倫理学", 1982, "North_America", "https://en.wikipedia.org/wiki/Ethics_of_care"),
    ("ケアの社会理論", "Social Theory of Care", None, "ケアを家族・市場・国家・コミュニティの四者が分担する社会制度として分析するホックシールド・フィン等の理論。", "フェミニズム・ジェンダー理論", "フェミニスト社会学", 1990, "North_America", "https://en.wikipedia.org/wiki/Care_theory"),
    ("インターセクショナリティ（交差性）", "Intersectionality", None, "人種・ジェンダー・階級・セクシュアリティ等の抑圧が交差・相互構成する様を分析するクレンショーの概念（1989年）。", "フェミニズム・ジェンダー理論", "インターセクショナル・フェミニズム", 1989, "North_America", "https://en.wikipedia.org/wiki/Intersectionality"),
    ("ブラック・フェミニズム", "Black Feminism", None, "黒人女性が経験する人種・ジェンダー・階級の複合的抑圧に応答するフェミニスト思想の潮流。コンバヒー河川集団声明（1977年）。", "フェミニズム・ジェンダー理論", "インターセクショナル・フェミニズム", 1977, "North_America", "https://en.wikipedia.org/wiki/Black_feminism"),
    ("ブラック・フェミニスト思想（コリンズ）", "Black Feminist Thought (Collins)", None, "黒人女性の立場的知識・抑圧の支配のマトリクス・他者定義への抵抗を論じたコリンズの社会学的理論（1990年）。", "フェミニズム・ジェンダー理論", "インターセクショナル・フェミニズム", 1990, "North_America", "https://en.wikipedia.org/wiki/Black_Feminist_Thought"),
    ("抑圧のマトリクス", "Matrix of Domination", None, "人種・ジェンダー・階級・性的指向等の権力次元が体系的に絡み合う支配の構造をコリンズが提示した概念。", "フェミニズム・ジェンダー理論", "インターセクショナル・フェミニズム", 1990, "North_America", "https://en.wikipedia.org/wiki/Patricia_Hill_Collins"),
    ("チカーナ・フェミニズム", "Chicana Feminism", None, "メキシコ系アメリカ人女性の人種・ジェンダー・階級・移民経験の交差を中心とするフェミニズム。グロリア・アンサルドゥーア等。", "フェミニズム・ジェンダー理論", "インターセクショナル・フェミニズム", 1981, "North_America", "https://en.wikipedia.org/wiki/Chicana_feminism"),
    ("ボーダーランズ（国境地帯）", "Borderlands", None, "文化的・地理的・心理的境界に生きるチカーナの経験と知識からアンサルドゥーアが提唱したポスト植民地・フェミニスト概念。", "フェミニズム・ジェンダー理論", "インターセクショナル・フェミニズム", 1987, "North_America", "https://en.wikipedia.org/wiki/Borderlands/La_Frontera:_The_New_Mestiza"),
    ("アフリカン・フェミニズム", "African Feminism", None, "西洋フェミニズムの普遍主義を批判しながらアフリカの文化的文脈・共同体・精霊論を組み込んだフェミニスト思想。アフリアブ・ステッドマン等。", "フェミニズム・ジェンダー理論", "グローバル・サウス・フェミニズム", 1980, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/African_feminism"),
    ("ウォーマニズム（ウォーカー）", "Womanism (Walker)", None, "白人中産階級フェミニズムの限界を指摘し、黒人女性の経験・文化・霊性を基礎とするアリス・ウォーカーの概念（1983年）。", "フェミニズム・ジェンダー理論", "グローバル・サウス・フェミニズム", 1983, "North_America", "https://en.wikipedia.org/wiki/Womanism"),
    ("インド・フェミニズム", "Indian Feminism", None, "植民地主義・カースト・宗教・家族制度の交差する複合的抑圧に応答するインド固有のフェミニスト思想と運動。", "フェミニズム・ジェンダー理論", "グローバル・サウス・フェミニズム", 1970, "South_Asia", "https://en.wikipedia.org/wiki/Feminism_in_India"),
    ("ラテンアメリカ・フェミニズム", "Latin American Feminism", None, "植民地的近代性・家父長制・階級・インディヘナの権利を結合したラテンアメリカ固有のフェミニスト理論と実践。", "フェミニズム・ジェンダー理論", "グローバル・サウス・フェミニズム", 1975, "Latin_America", "https://en.wikipedia.org/wiki/Latin_American_feminism"),
    ("イスラーム・フェミニズム", "Islamic Feminism", None, "イスラーム法・テキスト解釈を内部から問い直し、ムスリム女性の平等と尊厳を主張するフェミニズムの潮流。", "フェミニズム・ジェンダー理論", "グローバル・サウス・フェミニズム", 1990, "West_Asia_North_Africa", "https://en.wikipedia.org/wiki/Islamic_feminism"),
    ("上野千鶴子の家父長制論", "Ueno Chizuko's Theory of Patriarchy", None, "日本の家族制度・労働市場・福祉国家に埋め込まれた家父長制を分析した上野千鶴子の社会学的フェミニズム。", "フェミニズム・ジェンダー理論", "日本フェミニズム", 1990, "East_Asia", "https://en.wikipedia.org/wiki/Ueno_Chizuko"),
    ("韓国フェミニズム", "Korean Feminism", None, "儒教的家父長制・植民地主義・軍事独裁と闘いながら展開した韓国フェミニズム。慰安婦問題・#MeToo 運動と接続。", "フェミニズム・ジェンダー理論", "東アジア・フェミニズム", 1980, "East_Asia", "https://en.wikipedia.org/wiki/Feminism_in_South_Korea"),
    ("クィア理論", "Queer Theory", None, "ジェンダー・セクシュアリティの規範的二元論を脱構築し、多様な主体性・実践を肯定するバトラー・セジウィック等の理論。", "フェミニズム・ジェンダー理論", "クィア理論", 1990, "North_America", "https://en.wikipedia.org/wiki/Queer_theory"),
    ("ヘテロノーマティヴィティ批判", "Critique of Heteronormativity", None, "異性愛が規範・当然として制度化される権力構造を批判するクィア理論の概念。ワーナー・セジウィック等。", "フェミニズム・ジェンダー理論", "クィア理論", 1991, "North_America", "https://en.wikipedia.org/wiki/Heteronormativity"),
    ("エピステモロジー・オブ・ザ・クローゼット", "Epistemology of the Closet", None, "20世紀文化の主要な二項対立がホモ/ヘテロの区別に構造化されているとするセジウィックの文化批評（1990年）。", "フェミニズム・ジェンダー理論", "クィア理論", 1990, "North_America", "https://en.wikipedia.org/wiki/Epistemology_of_the_Closet"),
    ("トランス理論", "Trans Theory", None, "トランスジェンダー経験・アイデンティティ・権利を分析しシスノーマティヴィティを批判するフェミニスト理論の新領域。", "フェミニズム・ジェンダー理論", "クィア理論", 2000, "North_America", "https://en.wikipedia.org/wiki/Transgender_studies"),
    ("再生産正義", "Reproductive Justice", None, "産む権利・産まない権利・安全に育てる権利を人権として統合するブラック・ウィメンズ・コーカスらの概念（1994年）。", "フェミニズム・ジェンダー理論", "インターセクショナル・フェミニズム", 1994, "North_America", "https://en.wikipedia.org/wiki/Reproductive_justice"),
    ("ジェンダーと開発", "Gender and Development", None, "開発政策が女性に与える影響を分析し、ジェンダー平等を開発の前提条件として主張するフェミニスト開発学。", "フェミニズム・ジェンダー理論", "フェミニスト開発学", 1975, "Global_Synthesis", "https://en.wikipedia.org/wiki/Gender_and_development"),
    ("フェミニスト地政学", "Feminist Geopolitics", None, "身体・日常生活・感情を地政学分析に組み込み、安全保障の軍事中心主義を批判するフェミニスト国際関係論の分野。", "フェミニズム・ジェンダー理論", "フェミニスト国際関係論", 1998, "North_America", "https://en.wikipedia.org/wiki/Feminist_geopolitics"),
    ("フェミニスト科学技術研究", "Feminist Science and Technology Studies", None, "科学・技術の知識生産とジェンダー関係を分析するハーディング・ロングナー等のフェミニスト認識論。", "フェミニズム・ジェンダー理論", "フェミニスト認識論", 1986, "North_America", "https://en.wikipedia.org/wiki/Feminist_science_studies"),
    ("立場理論（スタンドポイント・セオリー）", "Standpoint Theory", None, "周縁化された集団の経験的立場が特定の認識論的優位を生むとするハーディング・ヒンティッカ等の認識論。", "フェミニズム・ジェンダー理論", "フェミニスト認識論", 1983, "North_America", "https://en.wikipedia.org/wiki/Standpoint_theory"),
    ("強い客観性", "Strong Objectivity", None, "支配的観点でなく周縁化された視点から出発することで偏りの少ない客観的認識を達成できるとするハーディングの命題。", "フェミニズム・ジェンダー理論", "フェミニスト認識論", 1991, "North_America", "https://en.wikipedia.org/wiki/Strong_objectivity"),
    ("フェミニスト認識論", "Feminist Epistemology", None, "ジェンダー関係が知識生産・科学実践に与える影響を分析し代替的認識論を構築するフェミニズムの哲学的領域。", "フェミニズム・ジェンダー理論", "フェミニスト認識論", 1987, "North_America", "https://en.wikipedia.org/wiki/Feminist_epistemology"),
    ("デジタル・フェミニズム", "Digital Feminism", None, "SNS・オンラインプラットフォームを通じたフェミニスト組織化・言説・抵抗の新しい実践。MeToo・Everyday Sexism等。", "フェミニズム・ジェンダー理論", "フェミニズム史", 2012, "Global_Synthesis", "https://en.wikipedia.org/wiki/Online_feminism"),
    ("フェミニスト政治経済学", "Feminist Political Economy", None, "ジェンダー関係を経済的生産・再生産・分配の分析に組み込む学際的研究領域。フォールブル・ベンテリア等。", "フェミニズム・ジェンダー理論", "フェミニスト経済学", 1992, "North_America", "https://en.wikipedia.org/wiki/Feminist_political_economy"),
    ("フォーカス・グループ（フェミニスト研究法）", "Feminist Research Methods", None, "参加型・エンパワーメント型・反証的権力構造を組み込んだ社会調査法のフェミニスト的原則。", "フェミニズム・ジェンダー理論", "フェミニスト認識論", 1990, "North_America", "https://en.wikipedia.org/wiki/Feminist_research"),
    ("身体のフェミニスト理論", "Feminist Theory of the Body", None, "身体を文化的・権力的に刻み込まれた物質として分析するグロス・バトラー・コーネル等の理論。", "フェミニズム・ジェンダー理論", "フェミニスト体の理論", 1994, "North_America", "https://en.wikipedia.org/wiki/Feminist_body"),
    ("物質的フェミニズム", "Material Feminism", None, "身体・自然・物質の能動的役割を認め、文化中心主義と生物学的本質主義の双方を超えるフェミニスト存在論。", "フェミニズム・ジェンダー理論", "フェミニスト体の理論", 2008, "North_America", "https://en.wikipedia.org/wiki/Material_feminism"),
    ("MeToo運動の社会学", "Sociology of MeToo Movement", None, "2017年以降の性暴力告発運動が社会制度・組織文化・法政策に与えた影響の社会学的分析。", "フェミニズム・ジェンダー理論", "フェミニズム史", 2017, "Global_Synthesis", "https://en.wikipedia.org/wiki/MeToo_movement"),
    ("ジェンダーと労働市場", "Gender and Labor Market", None, "職業分離・賃金格差・ガラスの天井・感情労働の偏在等、労働市場のジェンダー不平等を分析する社会学的研究領域。", "フェミニズム・ジェンダー理論", "フェミニスト社会学", 1970, "North_America", "https://en.wikipedia.org/wiki/Gender_inequality"),
    ("ガラスの天井", "Glass Ceiling", None, "女性・マイノリティが組織内でキャリア上昇の見えない障壁に直面する構造的現象。1978年にアメリカで命名された。", "フェミニズム・ジェンダー理論", "フェミニスト社会学", 1978, "North_America", "https://en.wikipedia.org/wiki/Glass_ceiling"),
    ("男性性研究", "Masculinity Studies", None, "男性性の社会的・文化的構成を分析するコンネル・キンメル等の学術領域。覇権的男性性の批判的検討。", "フェミニズム・ジェンダー理論", "ジェンダー研究", 1987, "North_America", "https://en.wikipedia.org/wiki/Masculinity"),
    ("覇権的男性性", "Hegemonic Masculinity", None, "特定社会で支配的地位を占める男性性のパターンがジェンダー秩序を維持するとするコンネルの概念（1987年）。", "フェミニズム・ジェンダー理論", "ジェンダー研究", 1987, "North_America", "https://en.wikipedia.org/wiki/Hegemonic_masculinity"),
    ("ジェンダー・レジーム", "Gender Regime", None, "国家・組織・家族等の制度的文脈における特定のジェンダー配置の様式。コンネルの複数的男性性・女性性の制度分析。", "フェミニズム・ジェンダー理論", "ジェンダー研究", 1987, "North_America", "https://en.wikipedia.org/wiki/Gender_regime"),

    # === ポストコロニアル・脱植民地理論 ===
    ("サイードのオリエンタリズム", "Said's Orientalism", None, "西洋の知識・権力がアラブ・イスラーム世界を劣位の他者として構築する言説体制を分析したサイードの主著（1978年）。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1978, "North_America", "https://en.wikipedia.org/wiki/Orientalism_(book)"),
    ("文化帝国主義", "Cultural Imperialism", None, "植民地支配の終焉後も文化・メディア・教育を通じて旧宗主国の価値体系が維持される支配形態。トムリンソン等が分析。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1976, "Western_Europe", "https://en.wikipedia.org/wiki/Cultural_imperialism"),
    ("スピヴァクのサバルタン論", "Spivak's Subaltern Theory", None, "サバルタン（下位主体）は帝国主義的言説構造の外で声を持てないとするスピヴァクの批判的脱構築（1988年）。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1988, "South_Asia", "https://en.wikipedia.org/wiki/Can_the_Subaltern_Speak%3F"),
    ("サバルタン研究", "Subaltern Studies", None, "インド植民地史を下位主体の視点から再叙述するグハ・スピヴァク・チャクラバルティらの歴史学的プロジェクト。", "ポストコロニアル・脱植民地理論", "サバルタン研究", 1982, "South_Asia", "https://en.wikipedia.org/wiki/Subaltern_Studies"),
    ("脱植民地化の暴力（ファノン）", "Violence of Decolonization (Fanon)", None, "植民地支配の心理的内面化を解体する手段として政治的暴力の浄化機能を論じたファノン（1961年『地に呪われた者』）。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1961, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/The_Wretched_of_the_Earth"),
    ("植民地的トラウマ", "Colonial Trauma", None, "植民地支配が被支配民族に与えた心理的・文化的・世代間トラウマの持続的影響の分析。ファノン・メミ等が先駆。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1952, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/Franz_Fanon"),
    ("知の植民地性", "Coloniality of Knowledge", None, "ラテンアメリカ視点から西洋的知識体系が普遍として支配し、他の認識論を排除する構造を批判するキハーノ・ミニョーロ。", "ポストコロニアル・脱植民地理論", "脱植民地理論", 2000, "Latin_America", "https://en.wikipedia.org/wiki/Coloniality_of_knowledge"),
    ("権力の植民地性", "Coloniality of Power", None, "植民地支配が終焉した後も人種・労働・知識・主体性の編成に作用し続ける権力構造をキハーノが分析した概念。", "ポストコロニアル・脱植民地理論", "脱植民地理論", 2000, "Latin_America", "https://en.wikipedia.org/wiki/Coloniality_of_power"),
    ("脱植民地認識論", "Decolonial Epistemology", None, "ユーロセントリックな知識生産の独占を批判し、非西洋の認識論的伝統から複数の知を構築しようとする実践。", "ポストコロニアル・脱植民地理論", "脱植民地理論", 2000, "Latin_America", "https://en.wikipedia.org/wiki/Decolonization_of_knowledge"),
    ("境界思考（グローバル・デコロニアリズム）", "Border Thinking", None, "植民地的差異の境界に立ちながら植民地主義と近代性を同時に批判するミニョーロの認識論的戦略。", "ポストコロニアル・脱植民地理論", "脱植民地理論", 2000, "Latin_America", "https://en.wikipedia.org/wiki/Walter_Mignolo"),
    ("ネグリチュード運動", "Négritude Movement", None, "植民地支配に対してアフリカ・カリブ文化の価値を肯定するセゼール・サンゴール・ダマのフランス語圏の文化・政治運動。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1935, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/N%C3%A9gritude"),
    ("汎アフリカ主義", "Pan-Africanism", None, "アフリカとアフリカ系ディアスポラの政治的・文化的統一を目指す思想と運動。デュボイス・ンクルマ・マルコムX等。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1900, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/Pan-Africanism"),
    ("ネクロポリティクス（ムベンベ）", "Necropolitics (Mbembe)", None, "誰を生かし誰を死なせるかをめぐる権力の行使をフーコーの生政治を超えて分析したムベンベのアフリカ的批判理論。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 2003, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/Necropolitics"),
    ("ポストアパルトヘイト理論", "Post-Apartheid Theory", None, "人種隔離政策の廃止後、南アフリカ社会の人種・経済・記憶・アイデンティティを再構築する批判的社会思想。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1994, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/Post-apartheid"),
    ("インディヘナ認識論", "Indigenous Epistemology", None, "先住民の土地・身体・生態・霊性から生まれる知識形態を西洋科学と対等に位置づける認識論的枠組み。", "ポストコロニアル・脱植民地理論", "先住民理論", 1990, "Oceania", "https://en.wikipedia.org/wiki/Indigenous_knowledge"),
    ("バエン・ビビル（よく生きること）", "Buen Vivir", None, "アンデス先住民のコスモロジーに基づく、経済成長に代わる人・自然の調和的共生を目指す生き方の哲学。", "ポストコロニアル・脱植民地理論", "先住民理論", 2008, "Latin_America", "https://en.wikipedia.org/wiki/Buen_vivir"),
    ("サパティスタ思想", "Zapatista Thought", None, "先住民マヤの権利・自律・尊厳をマルクス主義・脱植民地理論と結合したチアパスの革命的社会思想（1994年〜）。", "ポストコロニアル・脱植民地理論", "先住民理論", 1994, "Latin_America", "https://en.wikipedia.org/wiki/Zapatista_Army_of_National_Liberation"),
    ("太平洋の知識（パシフィカ・スタディーズ）", "Pacific Knowledge", None, "太平洋諸島の航法・宇宙論・社会関係・植民地経験を固有の認識論として記述するハワイ・アオテアロア発の学術運動。", "ポストコロニアル・脱植民地理論", "先住民理論", 1990, "Oceania", "https://en.wikipedia.org/wiki/Pacific_studies"),
    ("アボリジナル主権論", "Aboriginal Sovereignty Theory", None, "オーストラリア先住民の土地・自己決定・文化的主権を法的・政治的・精神的次元で論じる思想的枠組み。", "ポストコロニアル・脱植民地理論", "先住民理論", 1985, "Oceania", "https://en.wikipedia.org/wiki/Indigenous_Australians"),
    ("入植者植民地主義", "Settler Colonialism", None, "先住民の土地収奪・置換を通じて入植者コミュニティが永続的に構築される特殊な植民地形態。ウォルフが概念化。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 2006, "North_America", "https://en.wikipedia.org/wiki/Settler_colonialism"),
    ("生政治と植民地（フーコー＋ファノン）", "Biopolitics and Colonialism", None, "植民地支配における人種主義的生政治の機能をファノン・ムベンベ等がフーコーの生政治概念を拡張して分析。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1975, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/Biopolitics"),
    ("ポストコロニアルと気候変動", "Postcolonial Climate Studies", None, "気候変動の不均衡な影響が植民地的南北関係を再生産するとする脱植民地的環境研究の視点。", "ポストコロニアル・脱植民地理論", "脱植民地理論", 2015, "Global_Synthesis", "https://en.wikipedia.org/wiki/Climate_justice"),
    ("グローバル正義論（ポストコロニアル）", "Global Justice (Postcolonial)", None, "植民地史的債務・再配分・認識論的不正義をグローバル正義の核心に置くポガ・ドゥッセル等の規範理論。", "ポストコロニアル・脱植民地理論", "脱植民地理論", 2002, "Global_Synthesis", "https://en.wikipedia.org/wiki/Global_justice"),
    ("移民・ディアスポラ研究", "Migration and Diaspora Studies", None, "移民・難民・ディアスポラの経験・アイデンティティ・市民権・トランスナショナリズムを分析する学際的領域。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1990, "Global_Synthesis", "https://en.wikipedia.org/wiki/Diaspora_studies"),
    ("ディアスポラのアイデンティティ", "Diasporic Identity", None, "故郷と受け入れ国の間に生きる移民・ディアスポラが形成する複数的・流動的アイデンティティ。ホール・バーバが分析。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1990, "West_Asia_North_Africa", "https://en.wikipedia.org/wiki/Diaspora_identity"),
    ("ホールの文化的アイデンティティ論", "Hall's Theory of Cultural Identity", None, "文化的アイデンティティを固定した本質ではなく生成・変化する位置づけとして論じたスチュアート・ホールの理論。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1990, "Western_Europe", "https://en.wikipedia.org/wiki/Stuart_Hall_(cultural_theorist)"),
    ("文化的翻訳", "Cultural Translation", None, "文化間の移行・変形・意味生成のプロセスとしての翻訳。バーバ・スピヴァクがポストコロニアル文脈で展開した概念。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1994, "South_Asia", "https://en.wikipedia.org/wiki/Cultural_translation"),
    ("表象の政治学", "Politics of Representation", None, "誰が誰をどのように表象するかが権力と知識に関わるとするポストコロニアル・フェミニスト文化批評の核心的問い。", "ポストコロニアル・脱植民地理論", "ポストコロニアル理論", 1990, "North_America", "https://en.wikipedia.org/wiki/Politics_of_representation"),
    ("世界システム論と植民地性", "World-System Theory and Coloniality", None, "ウォーラーステインの世界システム論とキハーノの植民地性論を接合したラテンアメリカの批判的近代性分析。", "ポストコロニアル・脱植民地理論", "脱植民地理論", 2000, "Latin_America", "https://en.wikipedia.org/wiki/Coloniality_of_power"),
]

def insert_batch(concepts):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    inserted = 0; skipped = 0
    for c in concepts:
        name_ja, name_en, name_orig, defn, subfield, school, era, region, url = c
        cur.execute("SELECT COUNT(*) FROM social_theory WHERE name_en=?", (name_en,))
        if cur.fetchone()[0] > 0:
            skipped += 1; continue
        uid = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()
        cur.execute("""INSERT INTO social_theory
            (id,name_ja,name_en,name_original,definition,subfield,school_of_thought,
             era_start,culture_region,source_url,verification_status,quality_flag,
             status,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,'url_present','B','active',?,?)""",
            (uid,name_ja,name_en,name_orig,defn,subfield,school,era,region,url,now,now))
        inserted += 1
        if inserted % 50 == 0:
            conn.commit(); print(f"  Committed {inserted}...")
    conn.commit(); conn.close()
    return inserted, skipped

if __name__ == "__main__":
    print(f"Inserting {len(concepts)} concepts (Batch 4: フェミニズム+ポストコロニアル)...")
    ins, sk = insert_batch(concepts)
    print(f"Done. Inserted: {ins}, Skipped: {sk}")
