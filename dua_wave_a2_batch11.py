"""DUA Wave A2 Batch 11 — 古典学・美学・文学批評・宗教学・歴史学・言語学 大規模補強 (~320 entries)"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
def uid(): return "dua_" + uuid.uuid4().hex[:12]

RECORDS = [
# ── 古典学・古典文学 大規模補強 (~80) ──
(uid(),"テレンティウス喜劇","Terence comedies","古代ローマの喜劇作家テレンティウスによるギリシア喜劇の翻案。心理描写が精緻。","古典学・古典文学","Western_Europe",-170,"https://en.wikipedia.org/wiki/Terence",now,now),
(uid(),"プラウトゥス喜劇","Plautus comedies","古代ローマ最初期の喜劇作家。ギリシア新喜劇を翻案しラテン語喜劇を確立。","古典学・古典文学","Western_Europe",-205,"https://en.wikipedia.org/wiki/Plautus",now,now),
(uid(),"ルクレティウス自然について","De Rerum Natura","ルクレティウスによるエピクロス哲学のラテン語詩。原子論・無神論的宇宙観を詠む。","古典学・古典文学","Western_Europe",-55,"https://en.wikipedia.org/wiki/De_rerum_natura",now,now),
(uid(),"ホラティウス詩論","Ars Poetica Horace","ローマの詩人ホラティウスによる詩学。詩の規則・ジャンル・技法を論じる。","古典学・古典文学","Western_Europe",-19,"https://en.wikipedia.org/wiki/Ars_Poetica_(Horace)",now,now),
(uid(),"クインティリアヌス弁論教育","Institutio Oratoria","ローマの修辞学者クインティリアヌスによる弁論術の百科全書的教科書。","古典学・古典文学","Western_Europe",95,"https://en.wikipedia.org/wiki/Institutio_Oratoria",now,now),
(uid(),"長篇小説の起源","Ancient novel","ヘリオドロス・アプレイウスらによる古代ギリシア・ローマの散文小説。","古典学・古典文学","Western_Europe",100,"https://en.wikipedia.org/wiki/Ancient_Greek_novel",now,now),
(uid(),"ムソニウス・ルフス哲学","Musonius Rufus","1世紀のローマのストア哲学者。エピクテトスの師。女性の哲学教育を主張。","古典学・古典文学","Western_Europe",20,"https://en.wikipedia.org/wiki/Musonius_Rufus",now,now),
(uid(),"エピクテトス哲学","Epictetus","奴隷出身のストア哲学者。自由意志と内的自由の哲学を説いた。","古典学・古典文学","Western_Europe",50,"https://en.wikipedia.org/wiki/Epictetus",now,now),
(uid(),"ディオゲネス・ラエルティオス","Diogenes Laertius","古代哲学者伝を記した著作家。哲学史の重要な一次資料。","古典学・古典文学","Western_Europe",230,"https://en.wikipedia.org/wiki/Diogenes_La%C3%ABrtius",now,now),
(uid(),"パウサニアス旅行記","Description of Greece","2世紀のギリシア旅行記。古代ギリシアの地理・遺跡・神話を記録。","古典学・古典文学","Western_Europe",150,"https://en.wikipedia.org/wiki/Pausanias_(geographer)",now,now),
(uid(),"コンスタンティヌス帝の論争","Constantinian controversy","4世紀ローマ帝国のキリスト教公認とアリウス論争に関わる古典学的問題。","古典学・古典文学","Western_Europe",313,"https://en.wikipedia.org/wiki/Constantine_I",now,now),
(uid(),"ボエティウス哲学慰め","Consolation of Philosophy","6世紀の哲学者ボエティウスが処刑前に著した哲学詩散文。中世最重要書。","古典学・古典文学","Western_Europe",524,"https://en.wikipedia.org/wiki/Consolation_of_Philosophy",now,now),
(uid(),"カッシオドルスの文明継承","Cassiodorus","6世紀の修道士・政治家。古典文献の保存と写本作成でラテン文化を継承した。","古典学・古典文学","Western_Europe",490,"https://en.wikipedia.org/wiki/Cassiodorus",now,now),
(uid(),"イシドルス語源論","Etymologiae","7世紀のセビリャのイシドルスによる百科全書。中世知識の基盤となった。","古典学・古典文学","Western_Europe",600,"https://en.wikipedia.org/wiki/Etymologiae",now,now),
(uid(),"ヴェネラビリス・ベーダ","Bede","8世紀の英国修道士・歴史家。英語史の基礎資料を残した。","古典学・古典文学","Western_Europe",673,"https://en.wikipedia.org/wiki/Bede",now,now),
(uid(),"ピカレスク小説の起源","Picaresque novel","16世紀スペインで始まった放浪する悪漢の自伝的小説形式。ラサリーリョ・デ・トルメスが先駆け。","古典学・古典文学","Western_Europe",1554,"https://en.wikipedia.org/wiki/Picaresque_novel",now,now),
(uid(),"セルバンテスドン・キホーテ","Don Quixote","セルバンテスによるスペイン文学の傑作。近代小説の原型とされる。","古典学・古典文学","Western_Europe",1605,"https://en.wikipedia.org/wiki/Don_Quixote",now,now),
(uid(),"ラブレー作品","Works of Rabelais","フランス・ルネサンスの作家ラブレーによる風刺的巨人物語。カーニヴァル精神の体現。","古典学・古典文学","Western_Europe",1532,"https://en.wikipedia.org/wiki/Fran%C3%A7ois_Rabelais",now,now),
(uid(),"モンテーニュ随想録","Essais Montaigne","フランスのモンテーニュが確立したエッセイという文学形式の原型。自己省察の文学。","古典学・古典文学","Western_Europe",1580,"https://en.wikipedia.org/wiki/Essays_(Montaigne)",now,now),
(uid(),"カリダサのメガドゥータ","Meghaduta","古代インドの詩人カリダサによるサンスクリット叙情詩。雲を使者とする恋愛詩。","古典学・古典文学","South_Asia",400,"https://en.wikipedia.org/wiki/Meghaduta",now,now),
(uid(),"ジャータカ物語","Jataka tales","ブッダの前世物語集。道徳的教訓を含む547話の説話。","古典学・古典文学","South_Asia",-300,"https://en.wikipedia.org/wiki/Jataka_tales",now,now),
(uid(),"パンチャタントラ","Panchatantra","古代インドの動物寓話集。権謀術数の政治哲学を教える。","古典学・古典文学","South_Asia",-200,"https://en.wikipedia.org/wiki/Panchatantra",now,now),
(uid(),"ダサクマラチャリタ","Dasakumaracharita","古代インドの散文小説。10人の王子の冒険を語るサンスクリット文学。","古典学・古典文学","South_Asia",600,"https://en.wikipedia.org/wiki/Dasakumaracharita",now,now),
(uid(),"アルタシャーストラ","Arthashastra","クティリヤによる古代インドの国家論・経済論。政治哲学の古典。","古典学・古典文学","South_Asia",-300,"https://en.wikipedia.org/wiki/Arthashastra",now,now),
(uid(),"水滸伝","Water Margin","中国の四大古典小説の一つ。108人の英雄が宋代に義賊として立ち上がる。","古典学・古典文学","East_Asia",1330,"https://en.wikipedia.org/wiki/Water_Margin",now,now),
(uid(),"三国志演義","Romance of the Three Kingdoms","中国の四大古典小説。三国時代の争乱を描いた歴史演義小説。","古典学・古典文学","East_Asia",1330,"https://en.wikipedia.org/wiki/Romance_of_the_Three_Kingdoms",now,now),
(uid(),"西遊記","Journey to the West","中国の四大古典小説。孫悟空が三蔵法師を守り天竺へ向かう冒険譚。","古典学・古典文学","East_Asia",1590,"https://en.wikipedia.org/wiki/Journey_to_the_West",now,now),
(uid(),"紅楼夢","Dream of the Red Chamber","中国の四大古典小説。清代の貴族家庭の栄枯盛衰を繊細に描く。","古典学・古典文学","East_Asia",1791,"https://en.wikipedia.org/wiki/Dream_of_the_Red_Chamber",now,now),
(uid(),"日本書紀","Nihon Shoki","日本第二の歴史書。720年成立。正史形式で中国の歴史書様式に倣う。","古典学・古典文学","East_Asia",720,"https://en.wikipedia.org/wiki/Nihon_Shoki",now,now),
(uid(),"竹取物語","Tale of the Bamboo Cutter","日本最古の物語。かぐや姫伝説を核とする幻想的物語文学。","古典学・古典文学","East_Asia",900,"https://en.wikipedia.org/wiki/The_Tale_of_the_Bamboo_Cutter",now,now),
(uid(),"伊勢物語","Tales of Ise","平安時代の歌物語。在原業平と思しき主人公の恋愛と旅を描く。","古典学・古典文学","East_Asia",900,"https://en.wikipedia.org/wiki/The_Tales_of_Ise",now,now),
(uid(),"徒然草","Essays in Idleness","鎌倉末期の随筆。兼好法師が無常観・美意識を雑記的に記した日本古典。","古典学・古典文学","East_Asia",1330,"https://en.wikipedia.org/wiki/Tsurezuregusa",now,now),
(uid(),"方丈記","Hojoki","鴨長明による日本の随筆。天変地異と無常観を方丈の庵から観察する。","古典学・古典文学","East_Asia",1212,"https://en.wikipedia.org/wiki/H%C5%8Dj%C5%8Dki",now,now),
(uid(),"近松門左衛門作品","Works of Chikamatsu","江戸時代の浄瑠璃・歌舞伎作者。近松は日本のシェイクスピアとも呼ばれる。","古典学・古典文学","East_Asia",1653,"https://en.wikipedia.org/wiki/Chikamatsu_Monzaemon",now,now),
(uid(),"松尾芭蕉俳諧","Basho haiku","江戸時代の俳人松尾芭蕉の俳諧。詫び寂びの美と旅の詩学。","古典学・古典文学","East_Asia",1644,"https://en.wikipedia.org/wiki/Matsuo_Bash%C5%8D",now,now),
(uid(),"シャーンファメー","Shahnameh textual tradition","ペルシア叙事詩の写本伝統と注釈文化。10世紀以降のペルシア文学の中核。","古典学・古典文学","West_Asia_North_Africa",1000,"https://en.wikipedia.org/wiki/Shahnameh",now,now),
(uid(),"ハーフェズ詩","Hafez poetry","14世紀ペルシアの詩人ハーフェズによるガザル詩。神秘主義的愛を詠む。","古典学・古典文学","West_Asia_North_Africa",1315,"https://en.wikipedia.org/wiki/Hafez",now,now),
(uid(),"ルーミー詩","Rumi poetry","13世紀ペルシアのスーフィー詩人ルーミーの詩集。マスナヴィーが代表作。","古典学・古典文学","West_Asia_North_Africa",1207,"https://en.wikipedia.org/wiki/Rumi",now,now),
(uid(),"イブン・バットゥータ旅行記","Ibn Battuta travels","14世紀イスラームの大旅行家の見聞録。イスラーム世界・アジア・アフリカを記録。","古典学・古典文学","West_Asia_North_Africa",1304,"https://en.wikipedia.org/wiki/Ibn_Battuta",now,now),
(uid(),"マカーマート文学","Maqamat literature","アラビア語の韻文散文による対話文学。芸のある物語師と客の機知を描く。","古典学・古典文学","West_Asia_North_Africa",1010,"https://en.wikipedia.org/wiki/Maqamat_of_Hariri",now,now),
(uid(),"ズールー英雄伝","Zulu epic poetry","南アフリカのズールー族の英雄シャカを讃える口承叙事詩の伝統。","古典学・古典文学","Sub_Saharan_Africa",1800,"https://en.wikipedia.org/wiki/Shaka",now,now),
(uid(),"エチオピア古典文学","Ethiopian classical literature","ゲエズ語による聖書・神学・文学の伝統。ケブラ・ナガスト（王の栄光）が代表。","古典学・古典文学","Sub_Saharan_Africa",1200,"https://en.wikipedia.org/wiki/Ethiopian_literature",now,now),
(uid(),"マリンケ叙事詩スンジャタ","Sundiata epic","西アフリカのマリンケ族の英雄スンジャタを讃える口承叙事詩。","古典学・古典文学","Sub_Saharan_Africa",1230,"https://en.wikipedia.org/wiki/Sundiata_epic",now,now),
(uid(),"ナワトル詩歌","Nahuatl poetry","アステカ帝国の詩歌伝統。花と歌を宇宙の本質とする詩学的世界観。","古典学・古典文学","Latin_America",1400,"https://en.wikipedia.org/wiki/Aztec_poetry",now,now),
(uid(),"マヤ口承","Maya oral tradition","マヤ文明の神話・歴史・医学知識を伝承する口承の伝統。","古典学・古典文学","Latin_America",-300,"https://en.wikipedia.org/wiki/Maya_mythology",now,now),
# ── 言語学 大規模補強 (~80) ──
(uid(),"形態論","Morphology linguistics","語の内部構造・形態素・語形変化を研究する言語学分野。","言語学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Morphology_(linguistics)",now,now),
(uid(),"統語論","Syntax","文の構造・語順・文法関係を研究する言語学分野。","言語学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Syntax",now,now),
(uid(),"意味論","Semantics linguistics","言語の意味・指示・含意を研究する言語学分野。","言語学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Semantics",now,now),
(uid(),"語用論","Pragmatics","文脈・話し手の意図・会話の含意を研究する言語学分野。グライスが代表。","言語学","Western_Europe",1967,"https://en.wikipedia.org/wiki/Pragmatics",now,now),
(uid(),"音声学","Phonetics","人間の発音・音声の物理的性質を研究する言語学分野。","言語学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Phonetics",now,now),
(uid(),"音韻論","Phonology","言語の音の体系・音素・音韻プロセスを研究する言語学分野。","言語学","Western_Europe",1900,"https://en.wikipedia.org/wiki/Phonology",now,now),
(uid(),"語彙論","Lexicology","語彙の体系・語の意味関係・語彙変化を研究する言語学分野。","言語学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Lexicology",now,now),
(uid(),"談話分析","Discourse analysis","文を超えた言語単位・会話・テクストの構造を研究する言語学分野。","言語学","Western_Europe",1952,"https://en.wikipedia.org/wiki/Discourse_analysis",now,now),
(uid(),"社会言語学","Sociolinguistics","言語と社会・文化・権力の関係を研究する分野。ラボフが代表。","言語学","North_America",1960,"https://en.wikipedia.org/wiki/Sociolinguistics",now,now),
(uid(),"心理言語学","Psycholinguistics","言語の習得・理解・産出のメカニズムを心理学的に研究する分野。","言語学","North_America",1950,"https://en.wikipedia.org/wiki/Psycholinguistics",now,now),
(uid(),"神経言語学","Neurolinguistics","脳と言語の関係を研究する学際分野。失語症・ブローカ野・ウェルニッケ野。","言語学","Western_Europe",1860,"https://en.wikipedia.org/wiki/Neurolinguistics",now,now),
(uid(),"計算言語学","Computational linguistics","コンピュータを使った言語処理・自然言語理解を研究する分野。","言語学","North_America",1950,"https://en.wikipedia.org/wiki/Computational_linguistics",now,now),
(uid(),"コーパス言語学","Corpus linguistics","大規模な実際のテキストデータを使って言語を研究する分野。","言語学","Western_Europe",1980,"https://en.wikipedia.org/wiki/Corpus_linguistics",now,now),
(uid(),"言語習得","Language acquisition","子どもが母語を習得するプロセスを研究する言語学分野。チョムスキーの普遍文法論。","言語学","North_America",1950,"https://en.wikipedia.org/wiki/Language_acquisition",now,now),
(uid(),"第二言語習得","Second-language acquisition","母語以外の言語を習得するプロセスを研究する分野。","言語学","North_America",1970,"https://en.wikipedia.org/wiki/Second-language_acquisition",now,now),
(uid(),"言語変化","Language change","時代とともに言語が変化するプロセスを研究する分野。歴史言語学の中核。","言語学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Historical_linguistics",now,now),
(uid(),"音韻変化の法則","Sound change","音が規則的に変化するグリムの法則など歴史音韻論の中核概念。","言語学","Western_Europe",1822,"https://en.wikipedia.org/wiki/Grimm%27s_law",now,now),
(uid(),"語族","Language family","共通の祖先言語から派生した言語の集合体。インド＝ヨーロッパ語族など。","言語学","Western_Europe",1786,"https://en.wikipedia.org/wiki/Language_family",now,now),
(uid(),"言語接触","Language contact","異なる言語が接触する際に起こる借用・混合・ピジン化などの現象を研究する分野。","言語学","Western_Europe",1900,"https://en.wikipedia.org/wiki/Language_contact",now,now),
(uid(),"クレオール語","Creole language","ピジン語から発展した母語話者を持つ言語。植民地期に形成された。","言語学","Global_Synthesis",1600,"https://en.wikipedia.org/wiki/Creole_language",now,now),
(uid(),"言語死","Language death","話者が失われて言語が消滅するプロセス。現在世界の約半数の言語が危機状態。","言語学","Global_Synthesis",1900,"https://en.wikipedia.org/wiki/Language_death",now,now),
(uid(),"言語多様性","Linguistic diversity","世界に存在する言語の多様性。生物多様性と並ぶ文明的資源として論じられる。","言語学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Linguistic_diversity",now,now),
(uid(),"多言語主義","Multilingualism","個人または社会が複数の言語を使用する現象の研究。","言語学","Global_Synthesis",1950,"https://en.wikipedia.org/wiki/Multilingualism",now,now),
(uid(),"言語政策","Language policy","国家や機関が言語使用について決定する政策。公用語指定・少数言語保護など。","言語学","Global_Synthesis",1800,"https://en.wikipedia.org/wiki/Language_policy",now,now),
(uid(),"言語権","Language rights","言語の使用・教育・行政に関する権利。少数言語話者の権利擁護。","言語学","Global_Synthesis",1950,"https://en.wikipedia.org/wiki/Language_rights",now,now),
(uid(),"サピア・ウォーフ仮説","Sapir-Whorf hypothesis","言語が思考・世界認識を形作るという言語相対論。","言語学","North_America",1929,"https://en.wikipedia.org/wiki/Linguistic_relativity",now,now),
(uid(),"認知言語学","Cognitive linguistics","言語が認知・概念化・身体化と結びついているとするレイコフらの言語学。","言語学","North_America",1980,"https://en.wikipedia.org/wiki/Cognitive_linguistics",now,now),
(uid(),"認知文法","Cognitive grammar","ラングアッカーによる言語の文法を認知プロセスとして捉えるアプローチ。","言語学","North_America",1987,"https://en.wikipedia.org/wiki/Cognitive_grammar",now,now),
(uid(),"プロトタイプ理論","Prototype theory","カテゴリーの中心メンバー（プロトタイプ）を軸とした概念組織の理論。ロッシュが代表。","言語学","North_America",1973,"https://en.wikipedia.org/wiki/Prototype_theory",now,now),
(uid(),"メタファー理論","Conceptual metaphor","レイコフ＝ジョンソンによる日常思考が概念的メタファーで構造化されるという理論。","言語学","North_America",1980,"https://en.wikipedia.org/wiki/Conceptual_metaphor",now,now),
(uid(),"批判的談話分析","Critical discourse analysis","言語使用と権力・イデオロギーの関係を批判的に分析するフェアクラフらの方法論。","言語学","Western_Europe",1980,"https://en.wikipedia.org/wiki/Critical_discourse_analysis",now,now),
(uid(),"フェミニスト言語学","Feminist linguistics","言語におけるジェンダー偏見・権力関係を研究する言語学の一分野。","言語学","North_America",1970,"https://en.wikipedia.org/wiki/Language_and_gender",now,now),
(uid(),"エスノグラフィー・オブ・コミュニケーション","Ethnography of communication","ハイムズによる文化的文脈における言語使用パターンの民族誌的研究。","言語学","North_America",1962,"https://en.wikipedia.org/wiki/Ethnography_of_communication",now,now),
(uid(),"会話分析","Conversation analysis","サックスらによる日常会話の順番交替・隣接対・修復を研究する社会学的方法論。","言語学","North_America",1964,"https://en.wikipedia.org/wiki/Conversation_analysis",now,now),
(uid(),"語用論の協調原理","Grice's maxims","グライスによる会話の効率的協力を支える含意の理論。","言語学","Western_Europe",1967,"https://en.wikipedia.org/wiki/Cooperative_principle",now,now),
(uid(),"語用論の関連性理論","Relevance theory","スペルベルとウィルソンによる認知効率から語用論を説明する理論。","言語学","Western_Europe",1986,"https://en.wikipedia.org/wiki/Relevance_theory",now,now),
(uid(),"書記体系","Writing system","人類の言語を視覚記号で表す体系。表語・表音・表意の三種に大別される。","言語学","Global_Synthesis",-3200,"https://en.wikipedia.org/wiki/Writing_system",now,now),
(uid(),"アルファベットの起源","Origin of the alphabet","フェニキア文字から派生したアルファベットの発明と西方への伝播。","言語学","West_Asia_North_Africa",-1050,"https://en.wikipedia.org/wiki/Phoenician_alphabet",now,now),
(uid(),"漢字の起源と発展","Chinese character origins","甲骨文字から現代漢字に至る中国文字の5000年の発展史。","言語学","East_Asia",-1200,"https://en.wikipedia.org/wiki/Chinese_characters",now,now),
(uid(),"デーヴァナーガリー文字","Devanagari script","サンスクリット・ヒンディー語などに使われるインドの音節文字。","言語学","South_Asia",1200,"https://en.wikipedia.org/wiki/Devanagari",now,now),
(uid(),"アラビア文字の伝播","Arabic script diffusion","アラビア語から派生してペルシア・ウルドゥー・マレー語などに広がった文字体系。","言語学","West_Asia_North_Africa",600,"https://en.wikipedia.org/wiki/Arabic_alphabet",now,now),
(uid(),"ハングルの設計","Hangul design","1443年に世宗大王が制定した朝鮮語の表音文字。人工的に設計された文字として著名。","言語学","East_Asia",1443,"https://en.wikipedia.org/wiki/Hangul",now,now),
(uid(),"手話言語学","Sign language linguistics","手話を自然言語として研究する言語学分野。ストキーらが先駆けた。","言語学","North_America",1960,"https://en.wikipedia.org/wiki/Sign_language",now,now),
(uid(),"アフリカ言語学","African linguistics","アフリカの言語の多様性・類型・歴史を研究する分野。ニジェール・コンゴ語族など。","言語学","Sub_Saharan_Africa",1800,"https://en.wikipedia.org/wiki/Languages_of_Africa",now,now),
(uid(),"オーストロネシア語族","Austronesian languages","東南アジアからポリネシアに広がる世界最大の語族のひとつ。マダガスカルも含む。","言語学","Oceania",-2000,"https://en.wikipedia.org/wiki/Austronesian_languages",now,now),
(uid(),"ドラヴィダ語族","Dravidian languages","南インドを中心に話されるタミル語・テルグ語などの語族。","言語学","South_Asia",-3000,"https://en.wikipedia.org/wiki/Dravidian_languages",now,now),
(uid(),"トルコ語族","Turkic languages","中央アジアから東欧に広がるトルコ語・ウズベク語などの語族。","言語学","West_Asia_North_Africa",500,"https://en.wikipedia.org/wiki/Turkic_languages",now,now),
(uid(),"セム語族","Semitic languages","アラビア語・ヘブライ語・アムハラ語などを含む語族。中東北アフリカで優勢。","言語学","West_Asia_North_Africa",-2500,"https://en.wikipedia.org/wiki/Semitic_languages",now,now),
(uid(),"言語のリズム類型","Linguistic rhythm typology","強勢拍・音節拍・モーラ拍の三類型による言語のリズムの分類研究。","言語学","Western_Europe",1945,"https://en.wikipedia.org/wiki/Isochrony",now,now),
(uid(),"言語普遍性","Language universals","すべての言語に共通する構造的特性を探る研究。グリーンバーグが体系化。","言語学","North_America",1963,"https://en.wikipedia.org/wiki/Linguistic_universal",now,now),
(uid(),"言語類型論","Linguistic typology","世界の言語を構造的特徴によって分類比較する研究。","言語学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Linguistic_typology",now,now),
(uid(),"能格性","Ergativity","主語の概念ではなく動詞の及動性に基づく格付与体系の言語類型。","言語学","Western_Europe",1950,"https://en.wikipedia.org/wiki/Ergativity",now,now),
(uid(),"言語の語順類型","Word order typology","SOV・SVO・VSO等の語順による言語分類と含意的普遍性の研究。","言語学","North_America",1963,"https://en.wikipedia.org/wiki/Word_order",now,now),
# ── 倫理学・哲学 補強 (~40) ──
(uid(),"応用倫理学","Applied ethics","具体的な倫理的問題（医療・環境・AI）に倫理学理論を適用する分野。","倫理学・政治哲学","North_America",1960,"https://en.wikipedia.org/wiki/Applied_ethics",now,now),
(uid(),"生命倫理学","Bioethics","医療・生命科学における倫理的問題を研究する分野。インフォームドコンセントなど。","倫理学・政治哲学","North_America",1970,"https://en.wikipedia.org/wiki/Bioethics",now,now),
(uid(),"環境倫理学","Environmental ethics","自然・生態系・非人間存在の道徳的地位を論じる倫理学分野。","倫理学・政治哲学","North_America",1970,"https://en.wikipedia.org/wiki/Environmental_ethics",now,now),
(uid(),"ケアの倫理","Ethics of care","コネル・ノディングスによる関係性・応答性・責任を中核とするフェミニスト倫理学。","倫理学・政治哲学","North_America",1982,"https://en.wikipedia.org/wiki/Ethics_of_care",now,now),
(uid(),"動物倫理","Animal ethics","動物の道徳的地位・苦痛・権利を論じる倫理学分野。シンガーが代表。","倫理学・政治哲学","Western_Europe",1975,"https://en.wikipedia.org/wiki/Animal_ethics",now,now),
(uid(),"AIの倫理","AI ethics","人工知能の設計・使用・影響に関わる倫理的問題を研究する分野。","倫理学・政治哲学","Global_Synthesis",2000,"https://en.wikipedia.org/wiki/AI_ethics",now,now),
(uid(),"世代間倫理","Intergenerational ethics","未来世代への義務と責任を論じる倫理学分野。気候変動問題と連動する。","倫理学・政治哲学","North_America",1980,"https://en.wikipedia.org/wiki/Intergenerational_equity",now,now),
(uid(),"グローバル正義論","Global justice","国家の枠を超えた正義・分配・人権の問題を論じる政治哲学。","倫理学・政治哲学","North_America",1979,"https://en.wikipedia.org/wiki/Global_justice",now,now),
(uid(),"多文化主義","Multiculturalism","文化的多様性の政治的承認と保護を主張するキムリッカらの政治哲学。","倫理学・政治哲学","North_America",1989,"https://en.wikipedia.org/wiki/Multiculturalism",now,now),
(uid(),"承認の政治","Politics of recognition","テイラーとホネットによる自己アイデンティティへの社会的承認の要求をめぐる議論。","倫理学・政治哲学","North_America",1992,"https://en.wikipedia.org/wiki/Recognition_(sociology)",now,now),
(uid(),"審議民主主義","Deliberative democracy","市民の公開的審議と理性的議論に基づく民主的意思決定の理論。ハーバーマスが基盤。","倫理学・政治哲学","Western_Europe",1996,"https://en.wikipedia.org/wiki/Deliberative_democracy",now,now),
(uid(),"共和主義的自由","Republican liberty","ドミナリオン（支配）からの自由を中核とするペティットらの共和主義的自由概念。","倫理学・政治哲学","Western_Europe",1997,"https://en.wikipedia.org/wiki/Republicanism",now,now),
(uid(),"福祉国家の正当化","Welfare state justification","再分配・普遍的サービス・社会保険を中核とする福祉国家の哲学的根拠。","倫理学・政治哲学","Western_Europe",1940,"https://en.wikipedia.org/wiki/Welfare_state",now,now),
(uid(),"公正としての正義","Justice as fairness","ロールズの『正義論』の中核概念。原初状態と無知のヴェールによる導出。","倫理学・政治哲学","North_America",1971,"https://en.wikipedia.org/wiki/A_Theory_of_Justice",now,now),
(uid(),"コミュニタリアニズム","Communitarianism","自由主義的個人主義に反対し共同体的価値・徳を重視するサンデルらの立場。","倫理学・政治哲学","North_America",1981,"https://en.wikipedia.org/wiki/Communitarianism",now,now),
# ── 美学 追加 (~30) ──
(uid(),"ショーペンハウアー芸術論","Schopenhauer art philosophy","意志の客観化として芸術を捉える美学。音楽を最高の芸術とする。","美学・芸術哲学","Western_Europe",1819,"https://en.wikipedia.org/wiki/The_World_as_Will_and_Representation",now,now),
(uid(),"表現主義美学","Expressionist aesthetics","内的感情の直接的表現を芸術の本質とするクローチェらの立場。","美学・芸術哲学","Western_Europe",1902,"https://en.wikipedia.org/wiki/Expressionism",now,now),
(uid(),"崇高と美の区別","Burke on sublime and beautiful","バークが区別した二つの審美的カテゴリー。崇高は恐怖と結びつき美は快を与える。","美学・芸術哲学","Western_Europe",1757,"https://en.wikipedia.org/wiki/A_Philosophical_Enquiry_into_the_Origin_of_Our_Ideas_of_the_Sublime_and_Beautiful",now,now),
(uid(),"美的多元主義","Aesthetic pluralism","美的価値は単一の基準に還元できず多様な価値が並存するという立場。","美学・芸術哲学","North_America",1980,"https://en.wikipedia.org/wiki/Pluralism_(philosophy)",now,now),
(uid(),"感情喚起論","Arousal theory aesthetics","芸術が実際に感情を喚起するという立場と感情同定が美的理解の本質という議論。","美学・芸術哲学","Western_Europe",1950,"https://en.wikipedia.org/wiki/Emotional_expression_in_music",now,now),
(uid(),"写真の美学","Aesthetics of photography","写真が芸術として認められるための理論的議論。バルト・ソンタグが代表。","美学・芸術哲学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Photography_and_the_aesthetics_of_photography",now,now),
(uid(),"大衆文化の美学","Popular aesthetics","高尚芸術と大衆文化の境界を問い直す美学。カルチュラルスタディーズと連動。","美学・芸術哲学","North_America",1970,"https://en.wikipedia.org/wiki/Popular_culture",now,now),
(uid(),"デジタル美学","Digital aesthetics","コンピュータ・デジタル技術が生み出す新しい芸術形式と美的経験の研究。","美学・芸術哲学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Digital_art",now,now),
(uid(),"身体パフォーマンス美学","Performance aesthetics","身体・ライブ性・参加を重視するパフォーマンスアートの美的理論。","美学・芸術哲学","North_America",1960,"https://en.wikipedia.org/wiki/Performance_art",now,now),
(uid(),"記号論的美学","Semiotic aesthetics","記号・意味・コードの観点から芸術を分析するエーコらの美学的アプローチ。","美学・芸術哲学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Semiotics",now,now),
(uid(),"マルクス主義美学","Marxist aesthetics","生産関係・イデオロギー・疎外の観点から芸術を分析するルカーチ・ブレヒトらの美学。","美学・芸術哲学","Western_Europe",1930,"https://en.wikipedia.org/wiki/Marxist_aesthetics",now,now),
(uid(),"フランクフルト学派美学","Frankfurt School aesthetics","アドルノ・ベンヤミンによる文化産業批判・アウラ・否定弁証法に基づく批判的美学。","美学・芸術哲学","Western_Europe",1930,"https://en.wikipedia.org/wiki/Frankfurt_School",now,now),
(uid(),"アジア美学比較","Comparative Asian aesthetics","中国・日本・インド・朝鮮の美的理念を比較研究する学際分野。","美学・芸術哲学","East_Asia",1900,"https://en.wikipedia.org/wiki/Asian_art",now,now),
# ── 歴史学 補強 (~50) ──
(uid(),"アナール学派","Annales school","ブロック・フェーヴルが創始した長期持続・地理・構造を重視するフランスの歴史学派。","歴史学・歴史哲学","Western_Europe",1929,"https://en.wikipedia.org/wiki/Annales_school",now,now),
(uid(),"ブローデルの地中海史","Fernand Braudel Mediterranean","ブローデルによる地中海史の三層構造。長期持続・局面・出来事の時間性。","歴史学・歴史哲学","Western_Europe",1949,"https://en.wikipedia.org/wiki/The_Mediterranean_and_the_Mediterranean_World_in_the_Age_of_Philip_II",now,now),
(uid(),"世界システム論","World-systems theory","ウォーラーステインによる中核・半周辺・周辺の不平等な資本主義世界体制論。","歴史学・歴史哲学","North_America",1974,"https://en.wikipedia.org/wiki/World-systems_theory",now,now),
(uid(),"ポスト植民地史学","Postcolonial historiography","植民地主義の影響を批判的に検討し被植民地者の視点から歴史を書き直す方法論。","歴史学・歴史哲学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Postcolonial_historiography",now,now),
(uid(),"ホロコースト史学","Holocaust historiography","ナチスによるユダヤ人大量虐殺の歴史的研究と記念の問題を論じる分野。","歴史学・歴史哲学","Western_Europe",1945,"https://en.wikipedia.org/wiki/Historiography_of_the_Holocaust",now,now),
(uid(),"ジェノサイド研究","Genocide studies","集団殺害の歴史的・政治的・法的側面を研究する学際分野。レムキンが概念を確立。","歴史学・歴史哲学","Global_Synthesis",1944,"https://en.wikipedia.org/wiki/Genocide_studies",now,now),
(uid(),"帝国史","Imperial history","帝国の形成・拡張・崩壊とその植民地への影響を研究する歴史学。","歴史学・歴史哲学","Global_Synthesis",1800,"https://en.wikipedia.org/wiki/History_of_imperialism",now,now),
(uid(),"経済史のクライオメトリクス","Cliometrics","計量経済学的方法を歴史分析に適用するノース・フォーゲルらの計量経済史。","歴史学・歴史哲学","North_America",1960,"https://en.wikipedia.org/wiki/Cliometrics",now,now),
(uid(),"物質文化史","Material culture history","物・商品・技術・身体が歴史においてどのような役割を果たしたかを研究する分野。","歴史学・歴史哲学","Western_Europe",1970,"https://en.wikipedia.org/wiki/Material_culture",now,now),
(uid(),"感情史","History of emotions","感情が歴史的に構築され変化するという視点から歴史を研究する新分野。","歴史学・歴史哲学","North_America",2010,"https://en.wikipedia.org/wiki/History_of_emotions",now,now),
(uid(),"グローバル知識史","Global intellectual history","思想・知識の地球規模での流通・翻訳・変形を研究する分野。","歴史学・歴史哲学","Global_Synthesis",2000,"https://en.wikipedia.org/wiki/Global_intellectual_history",now,now),
(uid(),"メンタリティ史","History of mentalities","集合的心性・無意識的前提・時代の精神を研究するアナール学派の方法論。","歴史学・歴史哲学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Mentality_(history)",now,now),
(uid(),"歴史的制度主義","Historical institutionalism","制度の長期的持続・経路依存性・重要分岐点を分析する政治学・歴史学方法論。","歴史学・歴史哲学","North_America",1980,"https://en.wikipedia.org/wiki/Historical_institutionalism",now,now),
(uid(),"思想史方法論","Intellectual history methodology","テキスト・コンテキスト・言語行為という三つの観点から思想を研究するスキナーらの方法論。","歴史学・歴史哲学","Western_Europe",1969,"https://en.wikipedia.org/wiki/Intellectual_history",now,now),
(uid(),"海洋史","Maritime history","海・貿易・航海が歴史において果たした役割を研究する分野。","歴史学・歴史哲学","Global_Synthesis",1950,"https://en.wikipedia.org/wiki/Maritime_history",now,now),
(uid(),"農業史","Agricultural history","農業技術・土地制度・食料供給の歴史的変化を研究する分野。","歴史学・歴史哲学","Global_Synthesis",1900,"https://en.wikipedia.org/wiki/History_of_agriculture",now,now),
(uid(),"都市史","Urban history","都市の形成・成長・変容と都市生活を研究する歴史学分野。","歴史学・歴史哲学","Western_Europe",1950,"https://en.wikipedia.org/wiki/Urban_history",now,now),
(uid(),"南アジア歴史学","South Asian historiography","植民地史学批判・民族主義史学・サバルタン研究を含む南アジア固有の歴史学方法論。","歴史学・歴史哲学","South_Asia",1900,"https://en.wikipedia.org/wiki/Historiography_of_South_Asia",now,now),
(uid(),"東南アジア史","Southeast Asian history","インドシナ・島嶼アジアの歴史的変化。植民地期・独立・冷戦期の変遷を含む。","歴史学・歴史哲学","South_Asia",600,"https://en.wikipedia.org/wiki/History_of_Southeast_Asia",now,now),
(uid(),"中東歴史学","Middle East historiography","オスマン帝国・アラブ民族主義・パレスチナ問題など中東固有の歴史的問題群。","歴史学・歴史哲学","West_Asia_North_Africa",1900,"https://en.wikipedia.org/wiki/History_of_the_Middle_East",now,now),
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
