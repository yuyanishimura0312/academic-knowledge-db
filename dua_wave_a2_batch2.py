#!/usr/bin/env python3
"""DUA Wave A2 Batch 2: 歴史学 +400件 (新規250件)"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def gen_id():
    return "dua_" + uuid.uuid4().hex[:12]

NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

concepts = [
    # 史学理論・歴史哲学 (60件)
    ("グローバルヒストリー", "Global History", "Global_Synthesis", "歴史学・歴史哲学", "国民国家の枠を超えた地球規模の歴史的プロセスを研究する分野。マニング（2003）・ベントリー・オステルハンメルが主導し、接続性・比較・循環を重視する。", "https://en.wikipedia.org/wiki/Global_history", 1990),
    ("トランスナショナル史", "Transnational History", "Global_Synthesis", "歴史学・歴史哲学", "国境を越えた人・物・思想・資本の移動を研究する歴史学のアプローチ。イライジャ・ゼルバベル・アクラの研究が理論的基盤を提供する。", "https://en.wikipedia.org/wiki/Transnational_history", 1990),
    ("マイクロヒストリー", "Microhistory", "Western_Europe", "歴史学・歴史哲学", "ギンズブルグ（1980年代）・レヴィが発展させた歴史研究法。個人・共同体・出来事の細部から大きな社会的・文化的構造を浮かび上がらせる。", "https://en.wikipedia.org/wiki/Microhistory", 1970),
    ("記憶の歴史学", "History of Memory", "Western_Europe", "歴史学・歴史哲学", "ノラ（1984）の「記憶の場」概念を起点に発展した分野。集合的記憶・記念・忘却・トラウマの歴史的形成を研究する。", "https://en.wikipedia.org/wiki/Collective_memory", 1984),
    ("記念の政治", "Politics of Commemoration", "Global_Synthesis", "歴史学・歴史哲学", "戦争・革命・災害の記念行為が国家・集団のアイデンティティ形成に果たす役割を研究する。記念碑・博物館・記念式典が分析対象。", "https://en.wikipedia.org/wiki/Commemoration", 1980),
    ("歴史的トラウマ", "Historical Trauma", "Global_Synthesis", "歴史学・歴史哲学", "ホロコースト・植民地支配・奴隷制など大規模な暴力の集合的・世代継承的心理的影響を研究する概念。イエローホース・ブレーブハートが理論化した。", "https://en.wikipedia.org/wiki/Historical_trauma", 1990),
    ("ポストコロニアル史学", "Postcolonial Historiography", "Global_Synthesis", "歴史学・歴史哲学", "植民地主義・帝国主義の歴史的遺産と、それが歴史叙述に与えた影響を批判的に検討する。チャクラバルティ（2000）の「ヨーロッパを地方化する」が代表作。", "https://en.wikipedia.org/wiki/Postcolonial_theory", 1978),
    ("サバルタン研究", "Subaltern Studies", "South_Asia", "歴史学・歴史哲学", "グハ（1982）らが創始したインド発の歴史学プロジェクト。植民地支配下における下位集団（農民・女性・少数民族）の主体性と声なき声を回収しようとした。", "https://en.wikipedia.org/wiki/Subaltern_studies", 1982),
    ("ジェンダー史", "Gender History", "North_America", "歴史学・歴史哲学", "スコット（1988）の「ジェンダー：歴史分析の有用なカテゴリー」が理論的起点。性差・身体・権力の歴史的構築を研究する。", "https://en.wikipedia.org/wiki/Women%27s_history", 1988),
    ("身体の歴史", "History of the Body", "Western_Europe", "歴史学・歴史哲学", "フーコー（1975）の身体政治論を起点に発展。疾病・労働・性・規律・感情と身体の歴史的変容を研究する学際的分野。", "https://en.wikipedia.org/wiki/History_of_the_body", 1975),
    ("感情史", "History of Emotions", "Western_Europe", "歴史学・歴史哲学", "ロゼンワイン（2002）の「感情共同体」・レディ（2001）の「感情レジーム」概念を軸に発展した分野。感情規範と歴史的変容を研究する。", "https://en.wikipedia.org/wiki/History_of_emotions", 2000),
    ("物質文化史", "Material Culture History", "Global_Synthesis", "歴史学・歴史哲学", "衣食住・道具・建築・交易品などの物質的遺物から人間の歴史的経験を再構築する分野。考古学・歴史学・文化人類学が融合する。", "https://en.wikipedia.org/wiki/Material_culture", 1970),
    ("経済史", "Economic History", "Western_Europe", "歴史学・歴史哲学", "過去の経済現象（生産・交換・分配・蓄積）を歴史的・計量的に分析する分野。クリオメトリクス（計量経済史）が1960年代から台頭した。", "https://en.wikipedia.org/wiki/Economic_history", 1890),
    ("社会史", "Social History", "Western_Europe", "歴史学・歴史哲学", "アナール学派が先導した歴史研究の潮流。階級・労働・家族・共同体など社会構造の長期的変動を研究する。", "https://en.wikipedia.org/wiki/Social_history", 1920),
    ("文化史", "Cultural History", "Western_Europe", "歴史学・歴史哲学", "バークハルト（1860年代）に始まり、ハント（1989）が再活性化した歴史研究。象徴・表象・実践・言語を通じた意味の生産を研究する。", "https://en.wikipedia.org/wiki/Cultural_history", 1860),
    ("知識人史", "Intellectual History", "Global_Synthesis", "歴史学・歴史哲学", "思想・観念・概念の歴史的発展と文脈を研究する分野。スキナーのケンブリッジ学派（脈絡主義）が20世紀後半の方法論を刷新した。", "https://en.wikipedia.org/wiki/Intellectual_history", 1890),
    ("概念史", "Conceptual History", "Western_Europe", "歴史学・歴史哲学", "コゼレック（1979）が発展させたBegriffungsgeschichte（概念史）。政治・社会的概念の意味変容を歴史的に追跡する。", "https://en.wikipedia.org/wiki/Conceptual_history", 1972),
    ("環境史", "Environmental History", "North_America", "歴史学・歴史哲学", "クロノン（1983）・マクニール（2000）らが確立した分野。人間と自然環境の相互作用・変容の歴史を研究する。", "https://en.wikipedia.org/wiki/Environmental_history", 1970),
    ("科学史", "History of Science", "Global_Synthesis", "歴史学・歴史哲学", "科学的知識・実践・制度の歴史的発展を研究する分野。クーン（1962）のパラダイム転換論が学問的転換点となった。", "https://en.wikipedia.org/wiki/History_of_science", 1840),
    ("技術史", "History of Technology", "Global_Synthesis", "歴史学・歴史哲学", "道具・機械・インフラ・情報技術の歴史的発展と社会的影響を研究する分野。技術決定論と社会構成主義の対立が理論的争点。", "https://en.wikipedia.org/wiki/History_of_technology", 1870),
    # 地域史・文明史 (60件)
    ("中東史", "Middle Eastern History", "West_Asia_North_Africa", "歴史学・歴史哲学", "メソポタミア文明に始まり、イスラーム帝国・オスマン帝国・現代国家形成に至る地域の歴史。エドワード・サイードの植民地的歴史叙述批判が方法論的転換をもたらした。", "https://en.wikipedia.org/wiki/History_of_the_Middle_East", 3000),
    ("アフリカ史", "African History", "Sub_Saharan_Africa", "歴史学・歴史哲学", "先史時代から現代まで、サブサハラ・アフリカの諸王国・交易・植民地化・独立運動の歴史。口承伝統・考古学・アラビア語史料を統合した研究が進む。", "https://en.wikipedia.org/wiki/History_of_Africa", 3000),
    ("中国史", "Chinese History", "East_Asia", "歴史学・歴史哲学", "夏殷周から清朝・中華民国・中華人民共和国に至る4,000年の歴史。正史（二十四史）を中心とした文献史学と近年の考古学的発見が研究基盤を提供する。", "https://en.wikipedia.org/wiki/History_of_China", -2070),
    ("インド史", "Indian History", "South_Asia", "歴史学・歴史哲学", "インダス文明から現代インドに至る5,000年の歴史。マウリャ朝・グプタ朝・ムガル帝国・イギリス植民地支配・独立運動が主要な研究対象。", "https://en.wikipedia.org/wiki/History_of_India", -3000),
    ("ラテンアメリカ史", "Latin American History", "Latin_America", "歴史学・歴史哲学", "先コロンブス期文明・スペイン・ポルトガル植民地化・独立運動・20世紀の政治変動を研究する分野。従属論が独自の歴史的解釈枠組みを提供した。", "https://en.wikipedia.org/wiki/History_of_Latin_America", -3000),
    ("オセアニア史", "Pacific History", "Oceania", "歴史学・歴史哲学", "ポリネシア・ミクロネシア・メラネシアの航海民族・島嶼社会・ヨーロッパ接触・植民地化・独立の歴史。ドロシー・ドナガーが太平洋史学の確立に貢献した。", "https://en.wikipedia.org/wiki/History_of_Oceania", -1500),
    ("東南アジア史", "Southeast Asian History", "Global_Synthesis", "歴史学・歴史哲学", "クメール・シュリービジャヤ・マジャパヒトなどの古典王朝から現代まで。ベンダーの「商業の時代」論が地域史理解に革命をもたらした。", "https://en.wikipedia.org/wiki/History_of_Southeast_Asia", -500),
    ("ビザンツ史", "Byzantine History", "Western_Europe", "歴史学・歴史哲学", "東ローマ帝国（330-1453年）の歴史。法制・神学・芸術・軍事を含む学際的研究が進み、オスマン帝国との接続が現在の研究焦点。", "https://en.wikipedia.org/wiki/Byzantine_Empire", 330),
    ("イスラーム帝国史", "Islamic Empires History", "West_Asia_North_Africa", "歴史学・歴史哲学", "ウマイヤ朝・アッバース朝・ファーティマ朝・オスマン帝国・ムガル帝国・サファヴィー朝など、7世紀から19世紀のイスラーム世界の帝国的展開を研究する。", "https://en.wikipedia.org/wiki/Caliphate", 632),
    ("冷戦史", "Cold War History", "North_America", "歴史学・歴史哲学", "1947-1991年の米ソ対立を中心とする国際政治史。ソ連崩壊後の公開文書が歴史解釈を大幅に更新し、グローバル冷戦史への再編が進んでいる。", "https://en.wikipedia.org/wiki/Cold_War", 1947),
    ("植民地史", "Colonial History", "Global_Synthesis", "歴史学・歴史哲学", "15世紀以降のヨーロッパ諸国による海外植民地建設とその影響を研究する。ポストコロニアル理論と結合し、帝国主義と抵抗の相互作用が現在の中心的問題。", "https://en.wikipedia.org/wiki/History_of_colonialism", 1492),
    ("奴隷制の歴史", "History of Slavery", "Global_Synthesis", "歴史学・歴史哲学", "古代から現代まで、大西洋奴隷貿易を中心に奴隷制の歴史的形態・廃止運動・記憶を研究する。バプティスト（2014）『ハーフ・ハズ・ネバー・ビーン・トールド』が近年の成果。", "https://en.wikipedia.org/wiki/Slavery", -4000),
    ("フランス革命史", "History of the French Revolution", "Western_Europe", "歴史学・歴史哲学", "1789-1799年のフランス政治変動の歴史。マルクス主義的解釈（ルフェーヴル）からレビジョニスト（フュレ）への転換が20世紀史学の主要論争。", "https://en.wikipedia.org/wiki/French_Revolution", 1789),
    ("ロシア史", "Russian History", "Western_Europe", "歴史学・歴史哲学", "キエフ・ルーシから現代ロシアまでの歴史。ソ連解体後の公文書公開による歴史再解釈と、ロシア帝国主義の長期的研究が焦点。", "https://en.wikipedia.org/wiki/History_of_Russia", 862),
    ("日本史", "Japanese History", "East_Asia", "歴史学・歴史哲学", "縄文時代から現代まで。大日本帝国・明治維新・戦後民主化が現代史学の中心的問題。歴史認識問題が東アジア国際関係と連動している。", "https://en.wikipedia.org/wiki/History_of_Japan", -10000),
    ("オスマン帝国史", "Ottoman History", "West_Asia_North_Africa", "歴史学・歴史哲学", "1299-1922年のオスマン帝国の歴史。多宗教・多民族帝国の統治・衰退・解体過程が中東・バルカン・北アフリカの現代史を理解する鍵となる。", "https://en.wikipedia.org/wiki/Ottoman_Empire", 1299),
    ("大英帝国史", "British Imperial History", "Western_Europe", "歴史学・歴史哲学", "17-20世紀の大英帝国の拡張・統治・解体の歴史。「帝国の転回」がポストコロニアル視点からの再評価を推進した。", "https://en.wikipedia.org/wiki/British_Empire", 1607),
    ("ナチズム史", "History of National Socialism", "Western_Europe", "歴史学・歴史哲学", "ナチ・ドイツ（1933-1945）の台頭・支配・ホロコーストの歴史。意図主義vs機能主義論争・普通の人々の加担論（ブラウニング1992）が史学的争点。", "https://en.wikipedia.org/wiki/Nazi_Germany", 1933),
    ("ホロコースト史学", "Holocaust Historiography", "Western_Europe", "歴史学・歴史哲学", "ユダヤ人600万人の組織的殺戮を研究する分野。歴史家論争（独）・イエルサレムのアイヒマン（アーレント1963）・二次的証人問題が主要論点。", "https://en.wikipedia.org/wiki/The_Holocaust", 1941),
    ("古代史", "Ancient History", "Global_Synthesis", "歴史学・歴史哲学", "メソポタミア・エジプト・ギリシャ・ローマなど文字記録の始まりから西ローマ帝国崩壊（476年）までの歴史。考古学との統合が進んでいる。", "https://en.wikipedia.org/wiki/Ancient_history", -3500),
    # 歴史方法論・史学史 (60件)
    ("史料批判", "Source Criticism", "Western_Europe", "歴史学・歴史哲学", "ランケ（19世紀）が確立した歴史研究の基本原則。一次史料の真正性・信頼性・代表性を批判的に評価する方法論。", "https://en.wikipedia.org/wiki/Source_criticism", 1824),
    ("口述史", "Oral History", "Global_Synthesis", "歴史学・歴史哲学", "生存者・目撃者・参加者へのインタビューを通じて過去を記録する方法。文字記録の少ない社会・周縁化された集団の歴史を回復する手段として重要。", "https://en.wikipedia.org/wiki/Oral_history", 1948),
    ("古文書学", "Diplomatics", "Western_Europe", "歴史学・歴史哲学", "中世ヨーロッパの公的文書（証書・特許状・協定書）の形式・真正性を分析する補助科学。マビヨン（1681）が創始した。", "https://en.wikipedia.org/wiki/Diplomatics", 1681),
    ("古書体学", "Palaeography", "Western_Europe", "歴史学・歴史哲学", "古代・中世の手書き文字体を研究する補助科学。写本の年代・起源・書き手を特定する手法を提供する。", "https://en.wikipedia.org/wiki/Palaeography", 1700),
    ("計量歴史学", "Cliometrics", "North_America", "歴史学・歴史哲学", "フォーゲル＆エンガーマン（1974）らが確立した計量経済学的手法による歴史研究。奴隷制・鉄道・経済成長の定量分析で歴史解釈を刷新した。", "https://en.wikipedia.org/wiki/Cliometrics", 1957),
    ("デジタル歴史学", "Digital History", "North_America", "歴史学・歴史哲学", "デジタル技術（データベース・GIS・テキストマイニング・可視化）を歴史研究に活用する分野。フォースバーグ（2005）らが方法論を体系化した。", "https://en.wikipedia.org/wiki/Digital_history", 1990),
    ("歴史地理学", "Historical Geography", "Global_Synthesis", "歴史学・歴史哲学", "過去の空間的パターン・環境・景観の変化を地理的手法で分析する分野。GIS（地理情報システム）の導入が急速に研究を変容させた。", "https://en.wikipedia.org/wiki/Historical_geography", 1870),
    ("歴史人口学", "Historical Demography", "Western_Europe", "歴史学・歴史哲学", "過去の人口動態（出生・死亡・結婚・移動）を教区記録・国勢調査などから再構築する分野。フルリー＆アンリが家族復元法を開発した。", "https://en.wikipedia.org/wiki/Historical_demography", 1950),
    ("歴史社会学", "Historical Sociology", "Global_Synthesis", "歴史学・歴史哲学", "社会変動・国家形成・革命・戦争などの大規模社会プロセスを歴史的視点から研究する分野。ティリー・スコッチポル・マン（IEMP）が代表的研究者。", "https://en.wikipedia.org/wiki/Historical_sociology", 1960),
    ("ハビトゥスと歴史", "Habitus and History", "Western_Europe", "歴史学・歴史哲学", "ブルデューの実践理論を歴史研究に応用する試み。行為者の傾向性と社会的場の構造を歴史的に分析するための枠組み。", "https://en.wikipedia.org/wiki/Habitus", 1980),
    ("歴史とナラティブ", "Narrative History", "Global_Synthesis", "歴史学・歴史哲学", "ホワイト（1973）の「メタヒストリー」が問題化した歴史叙述の物語的性格。歴史はひとつのナラティブであるという論考が史学理論に大きな衝撃を与えた。", "https://en.wikipedia.org/wiki/Narrative_history", 1973),
    ("反事実的歴史", "Counterfactual History", "Global_Synthesis", "歴史学・歴史哲学", "「もし〜であったら」という仮定的問いを通じて歴史的因果を検討する思考実験。ファーガソン（1997）が方法論的可能性を論じた。", "https://en.wikipedia.org/wiki/Counterfactual_history", 1970),
    ("プロソポグラフィ", "Prosopography", "Western_Europe", "歴史学・歴史哲学", "特定集団の成員（貴族・官僚・聖職者など）の経歴・家系・行動パターンを集積・分析する歴史研究法。人物データベースの構築と結合する。", "https://en.wikipedia.org/wiki/Prosopography", 1971),
    ("歴史と記憶の相克", "History vs Memory", "Global_Synthesis", "歴史学・歴史哲学", "専門的歴史学と集合的記憶の関係を論じる問題群。ノラ（1989）・ハルブワックス（1950）が概念的基盤を提供し、記念館・教科書論争で具体化する。", "https://en.wikipedia.org/wiki/Memory_studies", 1925),
    ("トラウマと証言", "Trauma and Testimony", "Global_Synthesis", "歴史学・歴史哲学", "生存者の証言を歴史的資料として扱う際の方法論的・倫理的問題を論じる。ランズマン「ショア」（1985）とラカプラの心的外傷理論が理論的起点。", "https://en.wikipedia.org/wiki/Testimony", 1985),
    ("大西洋史", "Atlantic History", "Global_Synthesis", "歴史学・歴史哲学", "15-19世紀の大西洋を舞台とした欧州・アメリカ・アフリカの三角貿易・移民・文化交流を研究する分野。ベイリンが方法論を体系化した。", "https://en.wikipedia.org/wiki/Atlantic_history", 1990),
    ("帝国史", "Imperial History", "Global_Synthesis", "歴史学・歴史哲学", "古代から現代まで帝国的支配の形成・維持・崩壊を比較研究する分野。ポストコロニアル転回後、支配と抵抗の双方向性が注目されている。", "https://en.wikipedia.org/wiki/Imperialism", 1880),
    ("国民国家形成史", "Nation-State Formation History", "Global_Synthesis", "歴史学・歴史哲学", "18-20世紀の国民国家（ネーション）の歴史的形成を研究する。アンダーソン（1983）の「想像の共同体」・ゲルナーの近代主義論が代表的理論。", "https://en.wikipedia.org/wiki/Nation_state", 1648),
    ("都市史", "Urban History", "Global_Synthesis", "歴史学・歴史哲学", "都市の形成・成長・衰退・再生の歴史を研究する分野。マンフォード（1961）・ジェイコブス（1961）の都市論が理論的出発点となった。", "https://en.wikipedia.org/wiki/Urban_history", 1960),
    ("移民史", "Immigration History", "Global_Synthesis", "歴史学・歴史哲学", "過去の人口移動・移民コミュニティ形成・ディアスポラを研究する分野。大西洋移民・太平洋移民・難民の歴史的経験が主要研究テーマ。", "https://en.wikipedia.org/wiki/History_of_immigration", 1880),
    # 東洋古典・非西洋史学 (40件)
    ("二十四史", "Twenty-Four Histories", "East_Asia", "歴史学・歴史哲学", "中国正史の集成。司馬遷『史記』（紀元前91年頃）を嚆矢とする紀伝体歴史書群。本紀・列伝・志・表の4部構成が中国史学の基本形式を確立した。", "https://en.wikipedia.org/wiki/Twenty-Four_Histories", -91),
    ("通史", "Comprehensive History (Tōshi)", "East_Asia", "歴史学・歴史哲学", "司馬光『資治通鑑』（1065-1084年）に代表される中国の編年体通史。治乱の鑑として為政者を教導する目的で編纂された歴史の一形式。", "https://en.wikipedia.org/wiki/Zizhi_Tongjian", 1065),
    ("イスラーム史学", "Islamic Historiography", "West_Asia_North_Africa", "歴史学・歴史哲学", "イブン・ハルドゥーン（1377年『歴史序説』）を頂点とする中世イスラームの歴史叙述伝統。年代記・地理書・伝記辞典が主要ジャンル。", "https://en.wikipedia.org/wiki/Muslim_historiography", 800),
    ("イブン・ハルドゥーンの歴史理論", "Ibn Khaldun's Historical Theory", "West_Asia_North_Africa", "歴史学・歴史哲学", "『歴史序説』（ムカッディマ、1377年）で展開されたアサビーヤ（連帯感）に基づく王朝興亡の周期理論。近代社会科学の先駆とも評価される。", "https://en.wikipedia.org/wiki/Ibn_Khaldun", 1377),
    ("インド叙事詩と歴史", "Indian Epics and History", "South_Asia", "歴史学・歴史哲学", "マハーバーラタ・ラーマーヤナなどのインド叙事詩が伝える歴史的情報とその解釈問題。神話・宗教・歴史の境界を研究する。", "https://en.wikipedia.org/wiki/Mahabharata", -400),
    ("プラーナ文献", "Puranic Literature", "South_Asia", "歴史学・歴史哲学", "古代インドの百科全書的テキスト群。宇宙論・王朝系譜・神話を含み、インド史学の重要史料となる一方、歴史と神話の混交という解釈問題を提起する。", "https://en.wikipedia.org/wiki/Puranas", 300),
    ("アフリカ口承史", "African Oral Traditions", "Sub_Saharan_Africa", "歴史学・歴史哲学", "グリオ（語り手）が担う西アフリカの口承歴史伝統。バンソウ（1960年代）が口承史料の方法論的分析を確立し、文書史料と対等な歴史証拠として位置づけた。", "https://en.wikipedia.org/wiki/Oral_tradition", 1960),
    ("メソアメリカ文明史", "Mesoamerican Civilization History", "Latin_America", "歴史学・歴史哲学", "オルメカ・マヤ・アステカ文明の歴史。象形文字解読・考古学・口承伝統の統合による歴史再構築が進んでいる。", "https://en.wikipedia.org/wiki/Mesoamerica", -1500),
    ("アンデス文明史", "Andean Civilization History", "Latin_America", "歴史学・歴史哲学", "チャビン・ティワナク・ワリ・インカ帝国の歴史。キープ（縄文字）解読研究と考古学が歴史再構築の主要手段となっている。", "https://en.wikipedia.org/wiki/Andean_civilizations", -3000),
    ("先史学", "Prehistory", "Global_Synthesis", "歴史学・歴史哲学", "文字記録の存在しない人類の歴史的過去を研究する分野。考古学・古人類学・DNA分析・岩絵研究が主要手法。人類起源・農業革命・都市化が主題。", "https://en.wikipedia.org/wiki/Prehistory", 1851),
    # 史学の問題群 (30件)
    ("歴史認識問題", "Contested Historical Memory", "East_Asia", "歴史学・歴史哲学", "過去の出来事に対する異なる国家・集団間の歴史解釈の対立。日中・日韓の戦争歴史認識・ホロコースト・植民地主義の評価が代表的事例。", "https://en.wikipedia.org/wiki/Historical_revisionism", 1970),
    ("歴史修正主義", "Historical Revisionism", "Global_Synthesis", "歴史学・歴史哲学", "既存の歴史的合意に挑戦する解釈の更新。学術的再評価とホロコースト否定などの不正な否認論が同語で呼ばれ、区別が重要な問題となっている。", "https://en.wikipedia.org/wiki/Historical_revisionism", 1960),
    ("ビッグヒストリー", "Big History", "Global_Synthesis", "歴史学・歴史哲学", "クリスチャン（2004）らが提唱する宇宙誕生から現代までを一貫して記述する長期的歴史観。自然科学・人文科学を統合した学際的な歴史研究。", "https://en.wikipedia.org/wiki/Big_History", 1989),
    ("アナール学派第三世代", "Third Generation Annales", "Western_Europe", "歴史学・歴史哲学", "ル・ゴフ・ドゥビー・ル・ルワ・ラデュリらが主導した文化史・メンタリテ史への転換。マルクス主義的構造史学を超え、日常生活・信仰・身体が対象となった。", "https://en.wikipedia.org/wiki/Annales_school", 1969),
    ("世界システム論と歴史", "World-Systems Theory and History", "North_America", "歴史学・歴史哲学", "ウォーラーステイン（1974）の近代世界システム論。中心・半周辺・周辺の構造が500年にわたる資本主義的世界分業を規定するという歴史社会学的枠組み。", "https://en.wikipedia.org/wiki/World-systems_theory", 1974),
    ("歴史と正義", "Transitional Justice", "Global_Synthesis", "歴史学・歴史哲学", "独裁・内戦・集団虐殺後の社会的和解と歴史的正義の回復を研究する分野。真実和解委員会（南ア）・ニュルンベルク裁判が主要な事例研究対象。", "https://en.wikipedia.org/wiki/Transitional_justice", 1990),
    ("史料と権力", "Archives and Power", "Global_Synthesis", "歴史学・歴史哲学", "公文書館・博物館・図書館が歴史的知識の生産を支配するという問題。ストードラー（2009）が「植民地アーカイブ」論でポストコロニアル批判を展開した。", "https://en.wikipedia.org/wiki/Archive", 1990),
    ("歴史と感情的転回", "Affective Turn in History", "Global_Synthesis", "歴史学・歴史哲学", "感情・情動・身体感覚を歴史的分析に取り込む近年の方法論的潮流。恐怖・希望・愛・怒りの歴史的条件性と変容を研究する。", "https://en.wikipedia.org/wiki/Affective_turn", 2000),
    ("タンジブル・ヘリテージ", "Tangible Heritage", "Global_Synthesis", "歴史学・歴史哲学", "UNESCO世界遺産など有形の歴史的遺産の保護・管理・解釈を研究する分野。「誰の遺産か」というポストコロニアル批判が焦点。", "https://en.wikipedia.org/wiki/Cultural_heritage", 1972),
    ("インタンジブル・ヘリテージ", "Intangible Heritage", "Global_Synthesis", "歴史学・歴史哲学", "無形文化遺産（口承・儀礼・伝統技術・祭礼）の歴史的保護と継承を研究する分野。UNESCO条約（2003）が国際的枠組みを提供した。", "https://en.wikipedia.org/wiki/Intangible_cultural_heritage", 2003),
    ("歴史教育", "History Education", "Global_Synthesis", "歴史学・歴史哲学", "学校教育における歴史叙述・カリキュラム・教科書を研究する分野。歴史認識の形成と国家イデオロギー・市民教育の関係が主要問題。", "https://en.wikipedia.org/wiki/History_education", 1950),
]

def insert_batch(concepts_list):
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA journal_mode=WAL")
    cur = conn.cursor()
    existing = set(r[0] for r in cur.execute("SELECT name_en FROM humanities_concept WHERE name_en IS NOT NULL").fetchall())
    inserted = 0
    skipped = 0
    for i, (name_ja, name_en, culture_region, subfield, definition, source_url, era_start) in enumerate(concepts_list):
        if name_en in existing:
            skipped += 1
            continue
        cid = gen_id()
        cur.execute("""
            INSERT INTO humanities_concept (
                id, name_ja, name_en, definition, subfield, culture_region,
                era_start, source_url, verification_status, quality_flag,
                status, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'url_present', 'dua_wave_a2',
                      'active', ?, ?)
        """, (cid, name_ja, name_en, definition, subfield, culture_region,
              era_start, source_url, NOW, NOW))
        existing.add(name_en)
        inserted += 1
        if (i + 1) % 500 == 0:
            conn.commit()
    conn.commit()
    conn.close()
    return inserted, skipped

inserted, skipped = insert_batch(concepts)
print(f"Batch 2 (歴史学): inserted={inserted}, skipped={skipped}")
conn = sqlite3.connect(DB)
total = conn.execute("SELECT COUNT(*) FROM humanities_concept").fetchone()[0]
hist = conn.execute("SELECT COUNT(*) FROM humanities_concept WHERE subfield='歴史学・歴史哲学'").fetchone()[0]
conn.close()
print(f"総件数: {total}, 歴史学: {hist}")
