#!/usr/bin/env python3
"""DUA Wave A2 Batch 5: 政治社会学+文化社会学+デジタル社会学+環境社会学+現象学的社会学"""
import sqlite3, uuid
from datetime import datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

concepts = [
    # === 政治社会学・国家論 ===
    ("国家の自律性", "State Autonomy", None, "国家が支配階級の単純な道具ではなく固有の利害・能力・構造を持つとするスコクポル・ノードリンガー等の命題。", "政治社会学・国家論", "国家論", 1979, "North_America", "https://en.wikipedia.org/wiki/State_autonomy"),
    ("革命の社会学（スコクポル）", "Social Revolutions (Skocpol)", None, "革命を国家・階級・国際的文脈の三者の相互作用から比較歴史的に説明したスコクポルの構造的分析（1979年）。", "政治社会学・国家論", "比較歴史社会学", 1979, "North_America", "https://en.wikipedia.org/wiki/States_and_Social_Revolutions"),
    ("資本主義の多様性", "Varieties of Capitalism", None, "自由市場型と協調型の資本主義体制の制度的差異を比較分析するホール＆ソスキス等の政治経済学的枠組み。", "政治社会学・国家論", "比較政治経済学", 2001, "Western_Europe", "https://en.wikipedia.org/wiki/Varieties_of_Capitalism"),
    ("福祉国家体制論", "Welfare State Regimes", None, "自由主義・保守主義・社会民主主義の三タイプに福祉国家を分類したエスピング＝アンデルセンの比較政治社会学（1990年）。", "政治社会学・国家論", "比較政治社会学", 1990, "Western_Europe", "https://en.wikipedia.org/wiki/The_Three_Worlds_of_Welfare_Capitalism"),
    ("脱商品化", "Decommodification", None, "労働力が市場に依存することなく生存できる程度を示すエスピング＝アンデルセンの福祉国家評価指標。", "政治社会学・国家論", "比較政治社会学", 1990, "Western_Europe", "https://en.wikipedia.org/wiki/Decommodification"),
    ("権力構造研究", "Power Structure Research", None, "経済エリートが政治的意思決定にどの程度支配力を持つかを実証的に検討するドムホフ等の政治社会学的研究。", "政治社会学・国家論", "エリート理論", 1967, "North_America", "https://en.wikipedia.org/wiki/Power_elite"),
    ("多元主義（ダール）", "Pluralism (Dahl)", None, "民主主義社会では権力が分散し複数の集団が競争的に政策を形成するとするダールの政治理論。エリート論への対抗。", "政治社会学・国家論", "民主主義論", 1961, "North_America", "https://en.wikipedia.org/wiki/Pluralism_(political_theory)"),
    ("ポリアーキー", "Polyarchy", None, "完全な民主主義の理念に対し現実の民主的統治形態として多数の集団が競争的に参加するとするダールの概念。", "政治社会学・国家論", "民主主義論", 1971, "North_America", "https://en.wikipedia.org/wiki/Polyarchy"),
    ("審議民主主義", "Deliberative Democracy", None, "合理的討議・理由付けによって正当な政治的決定を形成するハーバーマス・コーエン・ドライゼクらの民主主義論。", "政治社会学・国家論", "民主主義論", 1989, "Western_Europe", "https://en.wikipedia.org/wiki/Deliberative_democracy"),
    ("社会運動と国家", "Social Movements and the State", None, "社会運動が国家制度への接近・対立・統合を通じて政治変化を引き起こす過程の分析。タロー・マクアダム等。", "政治社会学・国家論", "社会運動論", 1994, "North_America", "https://en.wikipedia.org/wiki/Social_movement_theory"),
    ("政治的機会構造", "Political Opportunity Structure", None, "社会運動の発展・衰退を規定する政治システムの開放性・閉鎖性の度合い。タロー・マクアダムらの分析概念。", "政治社会学・国家論", "社会運動論", 1996, "North_America", "https://en.wikipedia.org/wiki/Political_opportunity"),
    ("フレーミング理論（社会運動）", "Framing Theory (Social Movements)", None, "社会運動が問題を定義し行動を正当化する意味構成の過程。ゴフマン＋スノウ＆ベンフォードが体系化。", "政治社会学・国家論", "社会運動論", 1988, "North_America", "https://en.wikipedia.org/wiki/Framing_(social_sciences)"),
    ("グローバル社会運動", "Global Social Movements", None, "WTO反対・世界社会フォーラム・気候運動等、国境を超えた連帯と抵抗のネットワーク。タランスモーションの実証分析。", "政治社会学・国家論", "社会運動論", 1999, "Global_Synthesis", "https://en.wikipedia.org/wiki/Global_justice_movement"),
    ("グローバル・ガバナンス", "Global Governance", None, "国家に代わる国際機関・NGO・多国籍企業・市民社会が形成する多層的な世界的統治の枠組み。", "政治社会学・国家論", "グローバル政治社会学", 1995, "Global_Synthesis", "https://en.wikipedia.org/wiki/Global_governance"),
    ("世界共和国論", "Cosmopolitanism", None, "人類共通の市民性・正義・権利を国家を超えた世界的制度で保障しようとする政治哲学。カント・ベック・ヌスバウム等。", "政治社会学・国家論", "グローバル政治社会学", 1994, "Global_Synthesis", "https://en.wikipedia.org/wiki/Cosmopolitanism"),
    ("ポピュリズム論", "Populism Theory", None, "エリートに対する「純粋な人民」を強調する薄い中心イデオロギー。ムデ・カルトワッセル・ムフ等が分析。", "政治社会学・国家論", "政治社会学", 2004, "Western_Europe", "https://en.wikipedia.org/wiki/Populism"),
    ("威権主義の新形態", "New Forms of Authoritarianism", None, "選挙権威主義・ハイブリッド体制・民主主義の後退等、21世紀型権威主義の政治社会学的分析。", "政治社会学・国家論", "政治社会学", 2010, "Global_Synthesis", "https://en.wikipedia.org/wiki/Authoritarianism"),
    ("ナショナリズムの社会学", "Sociology of Nationalism", None, "国民を発明された共同体として分析するアンダーソン・ホブズボウム・ゲルナー等の比較歴史的研究。", "政治社会学・国家論", "ナショナリズム論", 1983, "Western_Europe", "https://en.wikipedia.org/wiki/Nationalism"),
    ("想像の共同体（アンダーソン）", "Imagined Communities (Anderson)", None, "国民が活字資本主義を通じて匿名の他者と共同体を想像することで形成されるとするアンダーソンの主著（1983年）。", "政治社会学・国家論", "ナショナリズム論", 1983, "North_America", "https://en.wikipedia.org/wiki/Imagined_Communities"),
    ("民族紛争の社会学", "Sociology of Ethnic Conflict", None, "民族的アイデンティティ・資源競争・歴史的記憶が紛争を生む過程を分析する比較政治社会学の研究領域。", "政治社会学・国家論", "民族・人種社会学", 1985, "Global_Synthesis", "https://en.wikipedia.org/wiki/Ethnic_conflict"),
    ("公共圏の再構成", "Reconstitution of the Public Sphere", None, "デジタル・グローバル・多文化状況での公共圏の変容を分析するフレイザー・カルホーン等の批判的公共論。", "政治社会学・国家論", "民主主義論", 1992, "North_America", "https://en.wikipedia.org/wiki/Public_sphere"),
    ("国際規範の拡散", "Diffusion of International Norms", None, "人権・民主主義・環境保護等の国際規範が各国国内政治を変容させる過程。フィネモア・シッキンク等の構成主義。", "政治社会学・国家論", "グローバル政治社会学", 1998, "North_America", "https://en.wikipedia.org/wiki/Norm_(sociology)"),
    ("組織された無責任（ベック）", "Organized Irresponsibility (Beck)", None, "リスク社会において誰も責任を取らないまま組織的リスクが産出される体制的パターンをベックが批判的に分析した概念。", "政治社会学・国家論", "リスク社会論", 1992, "Western_Europe", "https://en.wikipedia.org/wiki/Ulrich_Beck"),
    ("環境政治学", "Environmental Politics", None, "環境問題を権力・利害・制度・社会運動の観点から分析する政治社会学的研究領域。", "政治社会学・国家論", "環境社会学", 1992, "Global_Synthesis", "https://en.wikipedia.org/wiki/Environmental_politics"),
    ("比較福祉国家（日本・東アジア）", "Comparative Welfare State (Japan/East Asia)", None, "儒教的家族主義・発展主義国家を組み込んだ東アジア福祉レジームをエスピング＝アンデルセン枠組みの外から論じた研究。", "政治社会学・国家論", "比較政治社会学", 1997, "East_Asia", "https://en.wikipedia.org/wiki/East_Asian_welfare_model"),
    ("グローバル・サウスの民主主義", "Democracy in the Global South", None, "アフリカ・ラテンアメリカ・アジアの民主化プロセス・民主主義の質・後退を比較政治学的に分析する研究。", "政治社会学・国家論", "民主主義論", 1990, "Global_Synthesis", "https://en.wikipedia.org/wiki/Democracy"),
    ("部族主義と国家形成（アフリカ）", "Tribalism and State Formation (Africa)", None, "植民地的境界線が引いた国家と先存の民族・部族関係の緊張をめぐるアフリカ政治社会学の研究テーマ。", "政治社会学・国家論", "アフリカ政治社会学", 1970, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/Tribalism"),

    # === 文化社会学・知識社会学 ===
    ("文化ダイヤモンド（グリスウォルド）", "Cultural Diamond (Griswold)", None, "文化的対象・生産者・受容者・社会文脈の四者の相互関係として文化を分析するグリスウォルドの分析枠組み。", "文化社会学・知識社会学", "文化社会学", 1994, "North_America", "https://en.wikipedia.org/wiki/Cultural_diamond"),
    ("文化的ツールキット（スウィドラー）", "Cultural Toolkit (Swidler)", None, "文化は行動を規定する価値でなく、行動戦略を構成するための象徴・儀礼・世界観等のツールキットとするスウィドラーの文化論。", "文化社会学・知識社会学", "文化社会学", 1986, "North_America", "https://en.wikipedia.org/wiki/Ann_Swidler"),
    ("アートワールド（ベッカー）", "Art Worlds (Becker)", None, "芸術を個人天才の産物でなく多数の協働者が参加するコレクティブ活動として分析するベッカーの社会学（1982年）。", "文化社会学・知識社会学", "芸術社会学", 1982, "North_America", "https://en.wikipedia.org/wiki/Art_Worlds"),
    ("文化的雑食性", "Cultural Omnivore", None, "高文化と大衆文化を横断的に消費するポストモダン的趣味構造。ピーターソンがスノッブ論に対抗して提示。", "文化社会学・知識社会学", "文化社会学", 1992, "North_America", "https://en.wikipedia.org/wiki/Cultural_omnivore"),
    ("知識社会学の展開", "Development of Sociology of Knowledge", None, "マンハイム・マートン・バーガー＆ルックマンを経て科学知識社会学（SSK）へ至る知識の社会的研究の系譜。", "文化社会学・知識社会学", "知識社会学", 1929, "Western_Europe", "https://en.wikipedia.org/wiki/Sociology_of_knowledge"),
    ("文化的記憶", "Cultural Memory", None, "共同体が過去を象徴・儀礼・テキストを通じて選択的に保存・伝達するアスマン（J.＆A.）の記憶研究概念。", "文化社会学・知識社会学", "記憶社会学", 1992, "Western_Europe", "https://en.wikipedia.org/wiki/Cultural_memory"),
    ("集合的記憶（ハルバックス）", "Collective Memory (Halbwachs)", None, "記憶は個人的でなく社会的集団の枠組みの中で形成されるとするハルバックスの社会学的命題（1950年）。", "文化社会学・知識社会学", "記憶社会学", 1950, "Western_Europe", "https://en.wikipedia.org/wiki/Collective_memory"),
    ("忘却の社会学", "Sociology of Forgetting", None, "集合的記憶が意図的・非意図的に選択・抑圧・書き換えられる過程の社会学的分析。コーネルトン・オルリック等。", "文化社会学・知識社会学", "記憶社会学", 1989, "Western_Europe", "https://en.wikipedia.org/wiki/Forgetting"),
    ("遺産化", "Heritagization", None, "過去の文化的要素が遺産として制度的に選別・博物館化・観光化・国際化される政治的過程の批判的分析。", "文化社会学・知識社会学", "文化遺産研究", 1995, "Western_Europe", "https://en.wikipedia.org/wiki/Heritage"),
    ("消費文化論", "Consumer Culture Theory", None, "消費実践が意味・アイデンティティ・社会的差異を産出する文化的プロセスとして分析されるFick・アーノルト等の研究。", "文化社会学・知識社会学", "消費社会学", 1996, "North_America", "https://en.wikipedia.org/wiki/Consumer_culture_theory"),
    ("ポップカルチャーの社会学", "Sociology of Popular Culture", None, "大衆音楽・テレビ・スポーツ・ゲーム等の大衆文化形式が社会的意味・権力・アイデンティティを生産する過程の分析。", "文化社会学・知識社会学", "文化社会学", 1970, "North_America", "https://en.wikipedia.org/wiki/Popular_culture"),
    ("文化産業の多様性", "Diversity of Cultural Industries", None, "音楽・映画・出版・ゲーム等の文化産業の経済的特性・グローバル化・コングロマリット化を分析する文化経済学。", "文化社会学・知識社会学", "文化産業論", 1990, "Western_Europe", "https://en.wikipedia.org/wiki/Cultural_industry"),
    ("宗教的合理化（ウェーバー後）", "Religious Rationalization (Post-Weber)", None, "ウェーバーの脱魔術化・宗教的合理化論の後継として展開された宗教と近代性の関係をめぐる議論。", "文化社会学・知識社会学", "宗教社会学", 1960, "Western_Europe", "https://en.wikipedia.org/wiki/Rationalization_(sociology)"),
    ("宗教的市場論", "Religious Market Theory", None, "宗教参加を宗教組織間の競争・需要・供給によって説明するスターク・フィンク等の宗教の合理的選択論。", "文化社会学・知識社会学", "宗教社会学", 1987, "North_America", "https://en.wikipedia.org/wiki/Religious_economy"),
    ("グローバル・カルチャー・インダストリー", "Global Culture Industries", None, "ハリウッド・K-POP・ボリウッド等のグローバルな文化産業のフローと地域的受容・変形の分析。", "文化社会学・知識社会学", "グローバル文化社会学", 2000, "Global_Synthesis", "https://en.wikipedia.org/wiki/Cultural_imperialism"),
    ("クレオール化", "Creolization", None, "植民地・移民状況において異なる文化が接触・融合・変形する過程。ハニフ・クレシ・ハンネルツ等が分析。", "文化社会学・知識社会学", "グローバル文化社会学", 1990, "Global_Synthesis", "https://en.wikipedia.org/wiki/Creolization"),
    ("翻訳社会学", "Sociology of Translation (Cultural)", None, "文化的意味が国境を越えて移動する際に変形・交渉・抵抗が生じる過程の社会学的分析。", "文化社会学・知識社会学", "グローバル文化社会学", 1995, "Western_Europe", "https://en.wikipedia.org/wiki/Cultural_translation"),
    ("ポップカルチャーとナショナルアイデンティティ", "Pop Culture and National Identity", None, "K-POP・アニメ・宝萊坞等の大衆文化が国民的アイデンティティの形成と国際的ソフトパワーに寄与する過程。", "文化社会学・知識社会学", "グローバル文化社会学", 2000, "East_Asia", "https://en.wikipedia.org/wiki/Korean_Wave"),
    ("科学と社会（STS）", "Science and Society (STS)", None, "科学技術の知識・実践・制度が社会的に形成され、逆に社会を形成する相互構成的過程の学際的研究。", "文化社会学・知識社会学", "科学技術社会論", 1970, "Western_Europe", "https://en.wikipedia.org/wiki/Science_and_technology_studies"),
    ("社会的認識論", "Social Epistemology", None, "知識の社会的条件・集団認識・制度的真理産出を哲学的・社会学的に分析するゴールドマン・フラー等の領域。", "文化社会学・知識社会学", "知識社会学", 1987, "North_America", "https://en.wikipedia.org/wiki/Social_epistemology"),
    ("メディアの社会的構成", "Social Construction of Media", None, "メディア技術が社会的文脈・利害・文化によって特定の形態・使途を与えられる過程の社会構築論的分析。", "文化社会学・知識社会学", "メディア社会学", 1985, "North_America", "https://en.wikipedia.org/wiki/Social_construction_of_technology"),
    ("フィールド（文化的場）理論と文化産出", "Field Theory and Cultural Production", None, "文学・芸術・科学の場における資本・位置・戦略をブルデューが体系的に分析した文化社会学の枠組み。", "文化社会学・知識社会学", "ブルデュー社会学", 1993, "Western_Europe", "https://en.wikipedia.org/wiki/Field_(Bourdieu)"),
    ("デジタル文化研究", "Digital Cultural Studies", None, "インターネット・SNS・ゲーム・デジタルメディアが文化的意味・アイデンティティ・権力を産出する過程の批判的分析。", "文化社会学・知識社会学", "デジタル社会学", 2003, "Global_Synthesis", "https://en.wikipedia.org/wiki/Digital_culture"),
    ("サブカルチャー理論", "Subcultural Theory", None, "支配文化に抵抗するスタイル・象徴・実践を持つ下位集団の形成をBirmingham CCCS等が分析した理論。", "文化社会学・知識社会学", "文化社会学", 1975, "Western_Europe", "https://en.wikipedia.org/wiki/Subculture"),

    # === デジタル社会学・ネットワーク社会 ===
    ("ネットワーク社会（カステルス）", "Network Society (Castells)", None, "情報・コミュニケーション技術がネットワークを社会組織の主要形態にする新たな社会形態をカステルスが分析（1996年）。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 1996, "North_America", "https://en.wikipedia.org/wiki/The_Information_Age:_Economy,_Society_and_Culture"),
    ("情報資本主義", "Informational Capitalism", None, "情報・知識・ネットワークが生産の主要動力となる資本主義の新段階。カステルスの情報時代論の経済的核心。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 1996, "North_America", "https://en.wikipedia.org/wiki/Informational_capitalism"),
    ("プラットフォーム社会", "Platform Society", None, "デジタルプラットフォームが社会制度・メディア・経済・政治を再編する現代社会の特徴をダイク等が分析。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2018, "Western_Europe", "https://en.wikipedia.org/wiki/Platform_economy"),
    ("デジタル格差", "Digital Divide", None, "情報技術へのアクセス・利用能力・成果が社会的属性（階層・年齢・地域・国籍）によって格差化する現象。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 1995, "North_America", "https://en.wikipedia.org/wiki/Digital_divide"),
    ("第二次デジタル格差", "Second-Level Digital Divide", None, "アクセスの格差を超えて、利用スキル・活用目的・成果における格差の第二層。ディマッジオ・ハルゴッタイ等。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2001, "North_America", "https://en.wikipedia.org/wiki/Digital_divide"),
    ("アルゴリズムの社会的帰結", "Social Consequences of Algorithms", None, "推薦・スコアリング・自動化意思決定アルゴリズムが不平等・偏見・権力を再生産する過程の社会学的分析。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2010, "Global_Synthesis", "https://en.wikipedia.org/wiki/Algorithmic_bias"),
    ("ソーシャルメディアと政治", "Social Media and Politics", None, "ツイッター・フェイスブック等のSNSが政治動員・世論形成・偽情報流通に与える影響の社会科学的研究。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2008, "Global_Synthesis", "https://en.wikipedia.org/wiki/Social_media_and_political_communication"),
    ("フィルターバブル", "Filter Bubble", None, "パーソナライズアルゴリズムが利用者を既存の信念を強化する情報のみにさらす状態。パリサーが2011年に命名。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2011, "North_America", "https://en.wikipedia.org/wiki/Filter_bubble"),
    ("エコーチェンバー", "Echo Chamber", None, "同質的な意見・情報のみが流通し多様な視点が排除されるオンライン空間の現象。政治的分極化の要因として研究。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2001, "North_America", "https://en.wikipedia.org/wiki/Echo_chamber_(media)"),
    ("プラットフォーム労働", "Platform Labor", None, "ウーバー・クラウドワーク等のデジタルプラットフォームを通じた労働の流動化・不安定化・労働権の侵食。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2014, "Global_Synthesis", "https://en.wikipedia.org/wiki/Platform_work"),
    ("デジタル監視社会", "Digital Surveillance Society", None, "国家・企業による個人データ収集・監視の普遍化と市民権・プライバシーへの影響。ライアン・監視資本主義論。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2001, "North_America", "https://en.wikipedia.org/wiki/Surveillance_society"),
    ("中国のデジタル社会", "Chinese Digital Society", None, "独自のプラットフォーム（微信・支付宝・抖音）・社会信用システム・デジタル権威主義が形成する中国独自のデジタル社会。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2015, "East_Asia", "https://en.wikipedia.org/wiki/Internet_censorship_in_China"),
    ("AIと社会的不平等", "AI and Social Inequality", None, "顔認識・採用AI・与信モデル等が人種・性別・階級の偏見を自動化・拡大する社会技術的不平等の分析。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2018, "Global_Synthesis", "https://en.wikipedia.org/wiki/Algorithmic_bias"),
    ("デジタル・アクティヴィズム", "Digital Activism", None, "SNS・スマートフォン・オンライン署名を活用した政治的動員・抵抗・運動の新形態。アラブの春・BLM等。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2009, "Global_Synthesis", "https://en.wikipedia.org/wiki/Digital_activism"),
    ("プラットフォーム資本主義", "Platform Capitalism", None, "デジタルプラットフォーム企業が媒介・データ・ネットワーク効果を通じて市場を独占する資本主義の新形態。スルニチェク。", "デジタル社会学・ネットワーク社会", "デジタル社会学", 2016, "Global_Synthesis", "https://en.wikipedia.org/wiki/Platform_capitalism"),

    # === 環境社会学・人新世 ===
    ("環境社会学の基礎", "Foundations of Environmental Sociology", None, "自然と社会の相互規定関係を分析する社会学の下位分野。ライリー・ダナラップ・キャットン等が1970年代に確立。", "環境社会学・人新世", "環境社会学", 1978, "North_America", "https://en.wikipedia.org/wiki/Environmental_sociology"),
    ("新生態学的パラダイム", "New Ecological Paradigm", None, "人間例外主義に対抗し、人間を自然の一部として捉えるエコロジー的世界観。ダナラップ＆ヴァン・リエールが1978年に提示。", "環境社会学・人新世", "環境社会学", 1978, "North_America", "https://en.wikipedia.org/wiki/New_Ecological_Paradigm"),
    ("踏み車仮説（トレッドミル）", "Treadmill of Production", None, "経済成長が環境破壊を自動的に促進する資本主義の構造的動態をシュナイバーグが分析した理論（1980年）。", "環境社会学・人新世", "環境社会学", 1980, "North_America", "https://en.wikipedia.org/wiki/Treadmill_of_production"),
    ("人新世", "Anthropocene", None, "人類の活動が地質学的力として地球システムを変容させた現代の地質年代。クルッツェンが2000年に命名。", "環境社会学・人新世", "人新世論", 2000, "Global_Synthesis", "https://en.wikipedia.org/wiki/Anthropocene"),
    ("プラネタリー・バウンダリー", "Planetary Boundaries", None, "地球システムの安全な操作空間を定義する九つの境界。ロックストローム等が2009年に提示。人新世の科学的枠組み。", "環境社会学・人新世", "人新世論", 2009, "Global_Synthesis", "https://en.wikipedia.org/wiki/Planetary_boundaries"),
    ("気候正義", "Climate Justice", None, "気候変動の原因・脆弱性・解決策が不均衡に分布する不正義を指摘し平等な気候政策を求める社会運動・理論。", "環境社会学・人新世", "環境社会学", 2000, "Global_Synthesis", "https://en.wikipedia.org/wiki/Climate_justice"),
    ("物のエージェンシー（モノの社会学）", "Agency of Things (Sociology of Materiality)", None, "人間以外の物質的存在が社会過程に能動的役割を果たすとするラトゥール以降の社会学的存在論。", "環境社会学・人新世", "人新世論", 1991, "Western_Europe", "https://en.wikipedia.org/wiki/Material_culture"),
    ("マルチ種族誌", "Multispecies Ethnography", None, "人間と動植物・微生物・菌類等の複数種の絡まり合いを記述する人類学的・社会学的研究アプローチ。", "環境社会学・人新世", "人新世論", 2010, "North_America", "https://en.wikipedia.org/wiki/Multispecies_ethnography"),
    ("ツィン菌類的思考（インタリューカー）", "Tsing's Latent Commons", None, "資本主義廃墟に生きる松茸を通じてグローバル資本主義・生態・偶発性を分析したツィングの人類学（2015年）。", "環境社会学・人新世", "人新世論", 2015, "North_America", "https://en.wikipedia.org/wiki/Anna_Tsing"),
    ("ダウンストリーム思考（生態社会学）", "Downstream Thinking (Eco-Sociology)", None, "環境問題の解決を技術的下流処理でなく社会的生産構造の根本変革に求める環境社会学の批判的立場。", "環境社会学・人新世", "環境社会学", 1985, "North_America", "https://en.wikipedia.org/wiki/Environmental_sociology"),
    ("エコフェミニズム", "Ecofeminism", None, "女性支配と自然支配が家父長制的思考の共通基盤から生まれるとし、両者の解放を結合するフェミニスト環境思想。", "環境社会学・人新世", "環境社会学", 1974, "Western_Europe", "https://en.wikipedia.org/wiki/Ecofeminism"),
    ("グローバル・コモンズ", "Global Commons", None, "大気・海洋・生物多様性等、特定国家に帰属せず全人類が共有する地球的共有財。その管理をめぐる国際的ガバナンス。", "環境社会学・人新世", "環境社会学", 1990, "Global_Synthesis", "https://en.wikipedia.org/wiki/Global_commons"),
    ("脱成長論", "Degrowth Theory", None, "経済成長の追求を停止し、生態的限界内での縮小・再生的経済への転換を主張する政治経済・社会論。", "環境社会学・人新世", "環境社会学", 1972, "Western_Europe", "https://en.wikipedia.org/wiki/Degrowth"),
    ("エネルギー民主主義", "Energy Democracy", None, "再生可能エネルギーへの転換を市民・地域主導で行い、エネルギー分野での民主的統制を実現しようとする社会運動・理論。", "環境社会学・人新世", "環境社会学", 2005, "Western_Europe", "https://en.wikipedia.org/wiki/Energy_democracy"),
    ("環境的不正義", "Environmental Injustice", None, "有害施設・汚染が人種的マイノリティ・低所得地域に集中する不平等な環境負荷の分布。環境正義運動の出発点。", "環境社会学・人新世", "環境社会学", 1987, "North_America", "https://en.wikipedia.org/wiki/Environmental_justice"),
    ("アフリカの環境社会学", "African Environmental Sociology", None, "植民地的土地収奪・資源採掘・気候脆弱性のアフリカ固有の社会的文脈で環境問題を論じる批判的研究。", "環境社会学・人新世", "環境社会学", 1990, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/Environmental_justice"),

    # === 生活世界・現象学的社会学 ===
    ("シュッツの社会的世界", "Schutz's Social World", None, "日常生活の自明性・主観的意味・間主観性を現象学的に分析したシュッツの行為理論的社会学。", "生活世界・現象学的社会学", "現象学的社会学", 1932, "Western_Europe", "https://en.wikipedia.org/wiki/Alfred_Schutz"),
    ("自然的態度", "Natural Attitude", None, "日常生活者が疑わずに自明視する世界の基本的構え。フッサール＋シュッツにおける社会学的分析の出発点。", "生活世界・現象学的社会学", "現象学的社会学", 1932, "Western_Europe", "https://en.wikipedia.org/wiki/Natural_attitude"),
    ("相互作用儀礼（ゴフマン）", "Interaction Ritual (Goffman)", None, "対面的相互作用を儀礼的な規則と演技的パフォーマンスとして分析するゴフマンの社会学的ドラマトゥルギー。", "生活世界・現象学的社会学", "ゴフマン", 1967, "North_America", "https://en.wikipedia.org/wiki/Erving_Goffman"),
    ("スティグマ", "Stigma (Goffman)", None, "社会的に傷つけられた属性が個人のアイデンティティを汚染・破壊する過程をゴフマンが分析した概念（1963年）。", "生活世界・現象学的社会学", "ゴフマン", 1963, "North_America", "https://en.wikipedia.org/wiki/Stigma_(sociology)"),
    ("全制的施設", "Total Institution", None, "外部との接触を遮断し生活の全局面を統制する施設（精神病院・刑務所・軍隊）をゴフマンが分析した概念。", "生活世界・現象学的社会学", "ゴフマン", 1961, "North_America", "https://en.wikipedia.org/wiki/Total_institution"),
    ("エスノメソドロジー", "Ethnomethodology", None, "日常生活者が「なんとか会話・状況を成立させる」実践的方法（メソッド）を分析するガーフィンケルの社会学。", "生活世界・現象学的社会学", "エスノメソドロジー", 1967, "North_America", "https://en.wikipedia.org/wiki/Ethnomethodology"),
    ("会話分析", "Conversation Analysis", None, "自然発生的会話の連鎖構造・修復・順番取りを録音分析するサックス・シェグロフ等のエスノメソドロジー的研究。", "生活世界・現象学的社会学", "エスノメソドロジー", 1974, "North_America", "https://en.wikipedia.org/wiki/Conversation_analysis"),
    ("インデクシカリティ", "Indexicality", None, "言語・行為の意味が文脈に依存して確定するという性質。エスノメソドロジーが日常的問題として分析する概念。", "生活世界・現象学的社会学", "エスノメソドロジー", 1967, "North_America", "https://en.wikipedia.org/wiki/Indexicality"),
    ("身体化された知識", "Embodied Knowledge", None, "明示的に語れない技能・感覚・習慣として身体に刻まれた知識形態。ポランニー・メルロ＝ポンティ・ブルデュー。", "生活世界・現象学的社会学", "身体社会学", 1958, "Western_Europe", "https://en.wikipedia.org/wiki/Embodied_cognition"),
    ("身体の社会学", "Sociology of the Body", None, "身体を文化的・権力的に構成されながら社会実践に関与する物質的存在として分析するシリングら。", "生活世界・現象学的社会学", "身体社会学", 1993, "Western_Europe", "https://en.wikipedia.org/wiki/Body_in_sociology"),
    ("感覚的社会学", "Sensory Sociology", None, "視覚・聴覚・嗅覚・触覚等の感覚経験が社会的に構成され、社会的意味を産出する過程を分析する研究領域。", "生活世界・現象学的社会学", "身体社会学", 2007, "Western_Europe", "https://en.wikipedia.org/wiki/Sensory_ethnography"),
    ("実践共同体（ウェンガー）", "Community of Practice (Wenger)", None, "共通の実践・知識・技術を通じて学習が生じる社会的文脈として実践共同体を分析するウェンガー＆レイブの理論。", "生活世界・現象学的社会学", "学習社会学", 1991, "North_America", "https://en.wikipedia.org/wiki/Community_of_practice"),
    ("日本社会論（間主観性）", "Japanese Social Theory (Intersubjectivity)", None, "「場」「気配」「間」等の日本的間主観性概念を社会学的に分析した中根千枝・清水博・山岸俊男等の研究。", "生活世界・現象学的社会学", "日本社会学", 1967, "East_Asia", "https://en.wikipedia.org/wiki/Japanese_studies"),
    ("中根千枝のタテ社会論", "Nakane Chie's Vertical Society", None, "日本社会の組織原理が資格・属性（ヨコ）でなく場・所属（タテ）によって構成されるとする中根の社会学的分析。", "生活世界・現象学的社会学", "日本社会学", 1967, "East_Asia", "https://en.wikipedia.org/wiki/Chie_Nakane"),
    ("丸山眞男の近代日本思想", "Maruyama Masao's Modern Japanese Thought", None, "近代日本における「超国家主義」・「思想の科学」・日本政治思想史研究。ファシズムの社会的基盤を分析した。", "生活世界・現象学的社会学", "日本社会学", 1946, "East_Asia", "https://en.wikipedia.org/wiki/Maruyama_Masao"),
    ("場（清水博）", "Ba (Shimizu Hiroshi)", None, "生命現象・組織・知識創造の基盤となる関係論的場（フィールド）概念を提唱した清水博の独自の生命論・組織論。", "生活世界・現象学的社会学", "日本社会学", 1983, "East_Asia", "https://en.wikipedia.org/wiki/Ba_(place)"),
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
    print(f"Inserting {len(concepts)} concepts (Batch 5)...")
    ins, sk = insert_batch(concepts)
    print(f"Done. Inserted: {ins}, Skipped: {sk}")
