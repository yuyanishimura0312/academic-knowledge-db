"""DUA Wave A2 Batch 13 — 倫理・哲学・言語学・文学批評・美学・歴史学・古典学 追加補強 (~350 entries)"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
def uid(): return "dua_" + uuid.uuid4().hex[:12]

RECORDS = [
# ── 倫理学・政治哲学 新規追加 (~50) ──
(uid(),"フランクファートの意志自由論","Frankfurt free will","一階の欲求と二階の欲求を区別する意志自由論。決定論と両立する自由意志の分析。","倫理学・政治哲学","North_America",1971,"https://en.wikipedia.org/wiki/Harry_Frankfurt",now,now),
(uid(),"ウィリアムズの道徳的運","Williams moral luck","道徳的評価において運が重要な役割を果たすというバーナード・ウィリアムズの主張。","倫理学・政治哲学","Western_Europe",1976,"https://en.wikipedia.org/wiki/Moral_luck",now,now),
(uid(),"ネーゲルの見方なき視点","Nagel view from nowhere","客観的視点の可能性と限界を論じるトーマス・ネーゲルの認識論・倫理学。","倫理学・政治哲学","North_America",1986,"https://en.wikipedia.org/wiki/The_View_from_Nowhere",now,now),
(uid(),"パーフィットの個人同一性","Parfit personal identity","個人同一性は程度の問題であり功利主義に含意するという議論。","倫理学・政治哲学","Western_Europe",1984,"https://en.wikipedia.org/wiki/Reasons_and_Persons",now,now),
(uid(),"ノージックの権原論","Nozick entitlement theory","取得・移転・矯正の正義による財産権の道徳的根拠を論じる最小国家論。","倫理学・政治哲学","North_America",1974,"https://en.wikipedia.org/wiki/Anarchy,_State,_and_Utopia",now,now),
(uid(),"ドウォーキンの資源の平等","Dworkin equality of resources","資源の平等（羨望テスト）を正義の基準とするロナルド・ドウォーキンの平等論。","倫理学・政治哲学","North_America",1981,"https://en.wikipedia.org/wiki/Ronald_Dworkin",now,now),
(uid(),"センの潜在能力アプローチ","Sen capability approach","物質的資源ではなく人が何をできるか（潜在能力）を福祉・正義の基準とするセンの理論。","倫理学・政治哲学","South_Asia",1979,"https://en.wikipedia.org/wiki/Capability_approach",now,now),
(uid(),"ヌスバウムの潜在能力リスト","Nussbaum capabilities list","人間的尊厳のために必要な10の中心的潜在能力を具体的にリストするヌスバウムの理論。","倫理学・政治哲学","North_America",1990,"https://en.wikipedia.org/wiki/Capabilities_approach",now,now),
(uid(),"ハーバーマスの討議倫理","Habermas discourse ethics","コミュニケーション的行為の理論から導かれる手続き的・普遍主義的倫理学。","倫理学・政治哲学","Western_Europe",1983,"https://en.wikipedia.org/wiki/Discourse_ethics",now,now),
(uid(),"マッキンタイアの徳倫理復興","MacIntyre after virtue","現代道徳の危機を診断しアリストテレス的徳倫理の復興を訴えるマッキンタイアの論著。","倫理学・政治哲学","North_America",1981,"https://en.wikipedia.org/wiki/Alasdair_MacIntyre",now,now),
(uid(),"宗教と政治の分離","Separation of church and state","政教分離の原則。ロック・ジェファーソンに始まる自由民主主義の根幹的原則。","倫理学・政治哲学","Western_Europe",1689,"https://en.wikipedia.org/wiki/Separation_of_church_and_state",now,now),
(uid(),"正義戦争論","Just war theory","戦争の道徳的正当化条件を論じる倫理学。アウグスティヌス・アクィナスに始まる。","倫理学・政治哲学","Western_Europe",400,"https://en.wikipedia.org/wiki/Just_war_theory",now,now),
(uid(),"ホッブズの社会契約","Hobbes social contract","自然状態の万人の万人に対する戦争からリヴァイアサン（主権者）への服従を導く社会契約論。","倫理学・政治哲学","Western_Europe",1651,"https://en.wikipedia.org/wiki/Leviathan_(Hobbes)",now,now),
(uid(),"ルソーの一般意志","Rousseau general will","共同体全体の利益を体現する一般意志を主権の根拠とするルソーの政治哲学。","倫理学・政治哲学","Western_Europe",1762,"https://en.wikipedia.org/wiki/Jean-Jacques_Rousseau",now,now),
(uid(),"ミルの自由論","Mill on liberty","他者危害原理を根拠に個人の自由の範囲を画定するジョン・スチュアート・ミルの政治哲学。","倫理学・政治哲学","Western_Europe",1859,"https://en.wikipedia.org/wiki/On_Liberty",now,now),
(uid(),"バーリンの二つの自由","Berlin two concepts of liberty","積極的自由と消極的自由を区別するアイザイア・バーリンの自由概念分析。","倫理学・政治哲学","Western_Europe",1958,"https://en.wikipedia.org/wiki/Two_Concepts_of_Liberty",now,now),
(uid(),"フェミニズムの波","Waves of feminism","第一波・第二波・第三波・第四波という時期区分によるフェミニズム運動の歴史的分析。","倫理学・政治哲学","North_America",1960,"https://en.wikipedia.org/wiki/Waves_of_feminism",now,now),
(uid(),"インターセクショナリティ","Intersectionality","人種・ジェンダー・階級・セクシュアリティが交差する複合的抑圧を論じるクレンショウの概念。","倫理学・政治哲学","North_America",1989,"https://en.wikipedia.org/wiki/Intersectionality",now,now),
(uid(),"ポスト植民地フェミニズム","Postcolonial feminism","西洋フェミニズムの普遍化を批判し植民地化された女性の特殊な経験を論じる立場。","倫理学・政治哲学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Postcolonial_feminism",now,now),
(uid(),"エコフェミニズム","Ecofeminism","女性支配と自然支配の構造的類似を論じ両者の解放を結びつけるフェミニズムの立場。","倫理学・政治哲学","North_America",1974,"https://en.wikipedia.org/wiki/Ecofeminism",now,now),
# ── 言語学 大量追加 (~70) ──
(uid(),"ジェスチャー研究","Gesture studies","発話と同期するジェスチャーが言語プロセスの一部であることを論じるマクニールらの研究。","言語学","North_America",1992,"https://en.wikipedia.org/wiki/Gesture",now,now),
(uid(),"マルチモーダル談話","Multimodal discourse","言語・視覚・音声・身体が統合された意味生成を研究する談話分析の拡張。","言語学","Western_Europe",2000,"https://en.wikipedia.org/wiki/Multimodality",now,now),
(uid(),"政治言語学","Political linguistics","政治的言語使用・プロパガンダ・フレーミングを研究する言語学と政治学の境界分野。","言語学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Political_linguistics",now,now),
(uid(),"メディア言語分析","Media language analysis","ニュース・広告・ソーシャルメディアの言語的特性を研究する応用言語学。","言語学","Western_Europe",1970,"https://en.wikipedia.org/wiki/Media_language",now,now),
(uid(),"語彙的語用論","Lexical pragmatics","語彙の意味と文脈的解釈の相互作用を研究する語用論と意味論の境界分野。","言語学","Western_Europe",1990,"https://en.wikipedia.org/wiki/Lexical_pragmatics",now,now),
(uid(),"ポライトネス理論","Politeness theory","フェイス（面子）の維持・侵害を通じた礼儀の語用論。ブラウンとレビンソンが代表。","言語学","Western_Europe",1978,"https://en.wikipedia.org/wiki/Politeness_theory",now,now),
(uid(),"インポリトネス研究","Impoliteness research","失礼・敵意ある言語行動を研究する語用論の新分野。カルパーシーが先駆け。","言語学","Western_Europe",1996,"https://en.wikipedia.org/wiki/Impoliteness",now,now),
(uid(),"スタンスとシフティング","Stance and footing","話者が発話内で採る認識的・評価的態度の変化を研究する相互作用言語学。","言語学","North_America",1979,"https://en.wikipedia.org/wiki/Footing_(linguistics)",now,now),
(uid(),"メタファーのマッピング","Metaphor mapping","概念メタファー理論における源泉領域から目標領域への構造写像の分析。","言語学","North_America",1980,"https://en.wikipedia.org/wiki/Conceptual_metaphor",now,now),
(uid(),"フレーム意味論","Frame semantics","概念フレームを語の意味の基盤とするフィルモアの意味論。FrameNetに発展。","言語学","North_America",1976,"https://en.wikipedia.org/wiki/Frame_semantics_(linguistics)",now,now),
(uid(),"原型意味論","Prototype semantics","典型例（プロトタイプ）とカテゴリー境界の曖昧性を中心とする意味理論。","言語学","North_America",1973,"https://en.wikipedia.org/wiki/Prototype_theory",now,now),
(uid(),"経路・着点・源泉","Path goal source schema","レイコフらの画像スキーマ論における空間的経験の基本構造。","言語学","North_America",1987,"https://en.wikipedia.org/wiki/Image_schema",now,now),
(uid(),"語用論的強化","Pragmatic enrichment","語の字義的意味が文脈によって強化・絞り込みされるプロセスの語用論的研究。","言語学","Western_Europe",1995,"https://en.wikipedia.org/wiki/Explicature",now,now),
(uid(),"語彙的連帯","Lexical solidarity","特定の語が意味的に関連する語と選択的に共起するウリエルらの意味関係理論。","言語学","Western_Europe",1964,"https://en.wikipedia.org/wiki/Lexical_solidarities",now,now),
(uid(),"ハワード・ガイルの配慮理論","Accommodation theory Giles","話者が相手に合わせて言語を調整する収束・発散の社会的動機を説明する理論。","言語学","Western_Europe",1973,"https://en.wikipedia.org/wiki/Communication_accommodation_theory",now,now),
(uid(),"都市方言変異","Urban dialect variation","都市部での言語変異・スタイルシフト・言語変化の社会言語学的研究。","言語学","North_America",1966,"https://en.wikipedia.org/wiki/Variationist_sociolinguistics",now,now),
(uid(),"言語接触と収束","Language convergence","異なる言語が接触により互いに類似していく現象。バルカン語連合が典型例。","言語学","Western_Europe",1930,"https://en.wikipedia.org/wiki/Language_convergence",now,now),
(uid(),"語彙拡散","Lexical diffusion","音声変化が語彙単位で徐々に広がるというウォン・ウォンらの変化モデル。","言語学","North_America",1969,"https://en.wikipedia.org/wiki/Lexical_diffusion",now,now),
(uid(),"方言連続体のインビジブル変化","Invisible change in dialect continuum","気付かれないうちに進行する音声・語彙変化の社会言語学的研究。","言語学","North_America",1972,"https://en.wikipedia.org/wiki/Language_change",now,now),
(uid(),"コードスイッチング","Code-switching","多言語話者が会話中に言語を切り替える現象の社会言語学・文法的研究。","言語学","North_America",1967,"https://en.wikipedia.org/wiki/Code-switching",now,now),
(uid(),"トランスランゲージング","Translanguaging","多言語資源を動的に活用する言語実践の概念。ウェールズ語教育から発展。","言語学","Western_Europe",1994,"https://en.wikipedia.org/wiki/Translanguaging",now,now),
(uid(),"エンドリンガ","Endangered language documentation","消滅危機言語のフィールド調査・記録・保存を行う言語学の緊急課題。","言語学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Language_documentation",now,now),
(uid(),"ランゲージ・ネスト","Language nest","幼児が少数言語のみで養育されるイマージョン言語復興プログラム。マオリが先駆け。","言語学","Oceania",1982,"https://en.wikipedia.org/wiki/Language_revitalization",now,now),
(uid(),"人工言語","Constructed language","エスペラント・クリンゴン語などの人工的に設計された言語体系の研究。","言語学","Global_Synthesis",1887,"https://en.wikipedia.org/wiki/Constructed_language",now,now),
(uid(),"ピジン語形成","Pidgin formation","異なる言語背景を持つ話者間の接触から生まれる簡略化された補助言語の形成過程。","言語学","Global_Synthesis",1700,"https://en.wikipedia.org/wiki/Pidgin",now,now),
(uid(),"音声言語学","Phonetics and linguistics","IPA（国際音声字母）体系と音声の物理的・生理的分析を組み合わせた言語研究。","言語学","Western_Europe",1886,"https://en.wikipedia.org/wiki/International_Phonetic_Alphabet",now,now),
(uid(),"音節の普遍性","Syllable universals","CV型を基本とする音節構造の普遍性と言語間の多様性を研究する音韻論。","言語学","Western_Europe",1930,"https://en.wikipedia.org/wiki/Syllable",now,now),
(uid(),"音調言語","Tone language","音の高低が語彙的意味を区別する機能を持つ言語（中国語・ヨルバ語など）の研究。","言語学","Global_Synthesis",1900,"https://en.wikipedia.org/wiki/Tone_language",now,now),
(uid(),"ピッチアクセント","Pitch accent","特定の音節に高低アクセントが付く日本語・スウェーデン語などの音調体系。","言語学","Global_Synthesis",1900,"https://en.wikipedia.org/wiki/Pitch-accent_language",now,now),
(uid(),"言語的相対主義","Linguistic relativity","言語構造が話者の認知・世界観を形作る程度に関する研究。サピア＝ウォーフ仮説を含む。","言語学","North_America",1929,"https://en.wikipedia.org/wiki/Linguistic_relativity",now,now),
(uid(),"顔文字とネット言語","Internet language","ソーシャルメディア・チャット・顔文字などデジタル環境固有の言語変化の研究。","言語学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Internet_linguistics",now,now),
(uid(),"認知詩学","Cognitive poetics","認知科学の枠組みで詩・物語の読みを研究するツァーとスティーンらの分野。","言語学","Western_Europe",1990,"https://en.wikipedia.org/wiki/Cognitive_poetics",now,now),
(uid(),"文学言語学","Literary linguistics","文学テキストを言語学的方法で分析するショートらの分野。文体論に近い。","言語学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Literary_linguistics",now,now),
(uid(),"読み書き能力","Literacy","読み書き能力の歴史的発展・社会的機能・認知的影響を研究する学際分野。","言語学","Global_Synthesis",1970,"https://en.wikipedia.org/wiki/Literacy",now,now),
(uid(),"批判的リテラシー","Critical literacy","テキストを批判的に読み権力関係を問い直す能力を育てる教育実践。","言語学","North_America",1980,"https://en.wikipedia.org/wiki/Critical_literacy",now,now),
# ── 文学批評 追加 (~40) ──
(uid(),"感情読者論","Emotional reader theory","読書体験における感情的反応の役割を論じる批評理論。ブースの「内包された著者」も含む。","文学批評理論","North_America",1961,"https://en.wikipedia.org/wiki/Implied_author",now,now),
(uid(),"倫理批評","Ethical criticism","文学テキストの道徳的・倫理的含意を批評する方法。ブースのレトリック批評に始まる。","文学批評理論","North_America",1988,"https://en.wikipedia.org/wiki/Ethical_criticism",now,now),
(uid(),"認知物語論","Cognitive narratology","物語の理解・産出における読者の認知プロセスを研究するゼルナン・フリードマンらの方法。","文学批評理論","North_America",1996,"https://en.wikipedia.org/wiki/Cognitive_narratology",now,now),
(uid(),"空間的物語論","Spatial narratology","物語における空間・場所・地理的移動の意味を研究する物語論の分野。","文学批評理論","North_America",2000,"https://en.wikipedia.org/wiki/Storyworld",now,now),
(uid(),"トランスメディア物語論","Transmedia narratology","複数のメディアにまたがる物語世界の構築とナビゲーションを研究する分野。","文学批評理論","North_America",2003,"https://en.wikipedia.org/wiki/Transmedia_storytelling",now,now),
(uid(),"クリオール文学","Creole literature","混血・文化混交・クレオール化を主題とするカリブ海・インド洋の文学伝統。","文学批評理論","Latin_America",1950,"https://en.wikipedia.org/wiki/Caribbean_literature",now,now),
(uid(),"マジック・ネグリチュード","Negritude and magic realism","黒人性の回復とマジックリアリズムが交差するアフロ・カリブ海文学。エメ・セゼールが代表。","文学批評理論","Sub_Saharan_Africa",1940,"https://en.wikipedia.org/wiki/%C3%89aim%C3%A9_C%C3%A9saire",now,now),
(uid(),"難民文学","Refugee literature","難民・망mig망・強制移住の体験を描く現代文学。テヴィタ・ヴァセイらが代表。","文学批評理論","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Refugee",now,now),
(uid(),"記憶文学","Memory literature","個人・集合的記憶の語り直しをテーマとする現代文学の潮流。","文学批評理論","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Memory_in_literature",now,now),
(uid(),"病い文学","Literature of illness","病気・障害・死を主題として個人の体験を描く文学ジャンル。ソンタグが先駆的分析。","文学批評理論","North_America",1978,"https://en.wikipedia.org/wiki/Illness_narrative",now,now),
(uid(),"自伝的批評","Autofiction criticism","フィクションと自伝の境界を曖昧にするドゥブロフスキー以来の自己叙述の批評研究。","文学批評理論","Western_Europe",1977,"https://en.wikipedia.org/wiki/Autofiction",now,now),
(uid(),"国際児童文学","International children's literature","世界各地の子ども向け文学の文化的特性・翻訳・教育的機能を研究する分野。","文学批評理論","Global_Synthesis",1900,"https://en.wikipedia.org/wiki/Children%27s_literature",now,now),
(uid(),"SFの詩学","Poetics of science fiction","科学小説の認知的疎外・ノヴァム・諸世界の規則を論じるスヴィン・ダルコらの理論。","文学批評理論","North_America",1972,"https://en.wikipedia.org/wiki/Science_fiction_studies",now,now),
(uid(),"探偵小説論","Detective fiction theory","ポオ・コナン・ドイル以来の探偵小説のジャンル的慣習・読者との契約を論じる批評。","文学批評理論","North_America",1975,"https://en.wikipedia.org/wiki/Detective_fiction",now,now),
(uid(),"不気味なもの","Uncanny Freud","フロイトの概念「ウンハイムリッヒ」。日常的なものが突然異質に感じられる体験。","文学批評理論","Western_Europe",1919,"https://en.wikipedia.org/wiki/The_Uncanny",now,now),
(uid(),"ジャンル理論","Genre theory","文学ジャンルの慣習・変形・相互引用を論じるデリダ・アルテーリらの批評理論。","文学批評理論","Western_Europe",1980,"https://en.wikipedia.org/wiki/Genre",now,now),
# ── 美学 追加 (~30) ──
(uid(),"快楽主義美学","Hedonic aesthetics","美的経験を快楽・不快の感覚として捉える感覚主義的美学の立場。","美学・芸術哲学","Western_Europe",1700,"https://en.wikipedia.org/wiki/Pleasure",now,now),
(uid(),"共感の美学","Empathy aesthetics","ヴォリンガーやリップスが提唱した芸術鑑賞における感情移入（エインフュールング）の理論。","美学・芸術哲学","Western_Europe",1903,"https://en.wikipedia.org/wiki/Empathy",now,now),
(uid(),"フォーム主義美学","Formalism aesthetics","クライヴ・ベルの有意味な形式や内容より形式的特性を重視する美学の立場。","美学・芸術哲学","Western_Europe",1914,"https://en.wikipedia.org/wiki/Clive_Bell",now,now),
(uid(),"前衛芸術論","Avant-garde theory","ビュルガーによる前衛芸術の制度批判・自律性の攻撃という歴史的プロジェクトの分析。","美学・芸術哲学","Western_Europe",1974,"https://en.wikipedia.org/wiki/Avant-garde",now,now),
(uid(),"キッチュの美学","Kitsch aesthetics","グリーンバーグらによるキッチュ（趣味の悪さ）の美学的分析と文化批判。","美学・芸術哲学","North_America",1939,"https://en.wikipedia.org/wiki/Kitsch",now,now),
(uid(),"オランダ黄金時代絵画論","Dutch Golden Age painting theory","17世紀オランダ絵画の市民的主題・写実主義・光の技法をめぐる美術史的美学。","美学・芸術哲学","Western_Europe",1610,"https://en.wikipedia.org/wiki/Dutch_Golden_Age_painting",now,now),
(uid(),"点字芸術","Braille art","視覚障害者が触覚で鑑賞する芸術形式と障害者の美的経験の哲学。","美学・芸術哲学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Inclusive_art",now,now),
(uid(),"コミュニティアート","Community art","市民参加・地域活性化・社会変革を目指す芸術実践とその美学的評価。","美学・芸術哲学","North_America",1960,"https://en.wikipedia.org/wiki/Community_art",now,now),
(uid(),"音楽の認知科学","Cognitive science of music","音楽知覚・音楽感情・音楽記憶の認知的メカニズムを研究する学際分野。","美学・芸術哲学","North_America",1990,"https://en.wikipedia.org/wiki/Cognitive_musicology",now,now),
(uid(),"絵画の見方","Pictorial representation theory","絵画がいかに世界を表象するかをウォルハイム・ゴンブリッチが論じた知覚的美学。","美学・芸術哲学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Pictorial_representation",now,now),
# ── 歴史学 追加 (~30) ──
(uid(),"シルクロード史","Silk Road history","中央アジアを通じた交易・宗教・文化の伝播を研究する地域横断的歴史学。","歴史学・歴史哲学","Global_Synthesis",130,"https://en.wikipedia.org/wiki/Silk_Road",now,now),
(uid(),"ティムール帝国史","Timurid history","14〜16世紀中央アジアのティムール帝国の歴史と文化的繁栄の研究。","歴史学・歴史哲学","West_Asia_North_Africa",1370,"https://en.wikipedia.org/wiki/Timurid_dynasty",now,now),
(uid(),"サファヴィー朝史","Safavid history","16〜18世紀イランのシーア派イスラーム王朝。ペルシア文化・芸術の復興期。","歴史学・歴史哲学","West_Asia_North_Africa",1501,"https://en.wikipedia.org/wiki/Safavid_dynasty",now,now),
(uid(),"ムガル帝国史","Mughal history","16〜19世紀インド亜大陸のイスラーム帝国。ヒンドゥー・イスラーム文化融合の時代。","歴史学・歴史哲学","South_Asia",1526,"https://en.wikipedia.org/wiki/Mughal_Empire",now,now),
(uid(),"朝鮮王朝史","Joseon history","14〜19世紀の朝鮮王朝。儒教的官僚制・身分制・書院文化が特徴。","歴史学・歴史哲学","East_Asia",1392,"https://en.wikipedia.org/wiki/Joseon",now,now),
(uid(),"ベトナム抵抗史","Vietnamese resistance history","中国・モンゴル・フランス・アメリカに対するベトナムの長期的抵抗の歴史。","歴史学・歴史哲学","South_Asia",200,"https://en.wikipedia.org/wiki/History_of_Vietnam",now,now),
(uid(),"マリ帝国史","Mali Empire history","13〜14世紀西アフリカのマリ帝国。マンサ・ムーサの黄金伝説で知られる。","歴史学・歴史哲学","Sub_Saharan_Africa",1235,"https://en.wikipedia.org/wiki/Mali_Empire",now,now),
(uid(),"大津波と歴史","Tsunami and history","自然災害（地震・津波）が歴史・文明・人口移動に与えた影響を研究する環境史分野。","歴史学・歴史哲学","Global_Synthesis",1900,"https://en.wikipedia.org/wiki/Historical_disaster",now,now),
(uid(),"帝国主義とナショナリズム","Imperialism and nationalism","19〜20世紀の帝国主義とナショナリズムの相互作用を研究する歴史学・政治学の議論。","歴史学・歴史哲学","Global_Synthesis",1870,"https://en.wikipedia.org/wiki/Imperialism",now,now),
(uid(),"冷戦史","Cold War history","アメリカとソ連を中心とした1947〜1991年の地政学的対立とその世界的影響。","歴史学・歴史哲学","Global_Synthesis",1947,"https://en.wikipedia.org/wiki/Cold_War",now,now),
(uid(),"脱植民地化","Decolonization history","第二次世界大戦後の植民地独立運動とその政治的・社会的プロセスの歴史学。","歴史学・歴史哲学","Global_Synthesis",1945,"https://en.wikipedia.org/wiki/Decolonization",now,now),
(uid(),"公衆史","Public history","歴史知識を博物館・メモリアル・ドキュメンタリーなど公共の場で活用する実践。","歴史学・歴史哲学","North_America",1970,"https://en.wikipedia.org/wiki/Public_history",now,now),
(uid(),"地域史","Local history","特定の地域・都市・村落の歴史的発展を研究する局所的歴史学の実践。","歴史学・歴史哲学","Western_Europe",1850,"https://en.wikipedia.org/wiki/Local_history",now,now),
# ── 古典学 追加 (~40) ──
(uid(),"古代神殿建築","Ancient temple architecture","ギリシア・ローマ・エジプト・インド・メソアメリカの神殿建築様式の比較研究。","古典学・古典文学","Global_Synthesis",-3000,"https://en.wikipedia.org/wiki/Temple",now,now),
(uid(),"古代演劇空間","Ancient theatre","ディオニュソス劇場からローマのコロッセウムまで古代の上演空間の考古学的・文学的研究。","古典学・古典文学","Western_Europe",-500,"https://en.wikipedia.org/wiki/Ancient_Greek_theatre",now,now),
(uid(),"パピルス文書","Papyrus documents","古代エジプト・ギリシアのパピルスに書かれた文書の発見・解読・研究。","古典学・古典文学","West_Asia_North_Africa",-3000,"https://en.wikipedia.org/wiki/Papyrus",now,now),
(uid(),"粘土板文書","Clay tablet","メソポタミアの楔形文字を刻んだ粘土板の文書群。法律・神話・商業記録を含む。","古典学・古典文学","West_Asia_North_Africa",-3200,"https://en.wikipedia.org/wiki/Clay_tablet",now,now),
(uid(),"ハンムラビ法典","Code of Hammurabi","バビロニア王ハンムラビの法典。282条の法律を刻んだ柱。古代法の記念碑的資料。","古典学・古典文学","West_Asia_North_Africa",-1754,"https://en.wikipedia.org/wiki/Code_of_Hammurabi",now,now),
(uid(),"ウパニシャッド注釈伝統","Upanishad commentary tradition","シャンカラ・ラーマーヌジャ・マドヴァによるウパニシャッドの三大注釈派の伝統。","古典学・古典文学","South_Asia",800,"https://en.wikipedia.org/wiki/Vedanta",now,now),
(uid(),"仏教論書","Buddhist Abhidharma","上座部・説一切有部などの仏教哲学論書の伝統。法（ダルマ）の体系的分析。","古典学・古典文学","South_Asia",-200,"https://en.wikipedia.org/wiki/Abhidharma",now,now),
(uid(),"ジャイナ教文献","Jain literature","ジャイナ教の聖典アーガマと哲学論書の伝統。不殺生と多面的真理（アネーカーンタヴァーダ）を説く。","古典学・古典文学","South_Asia",-500,"https://en.wikipedia.org/wiki/Jain_literature",now,now),
(uid(),"中国医学古典","Chinese medical classics","黄帝内経・傷寒論など古代中国医学の根本典籍群の研究。","古典学・古典文学","East_Asia",-200,"https://en.wikipedia.org/wiki/Traditional_Chinese_medicine",now,now),
(uid(),"道徳経注釈","Tao Te Ching commentary","老子の道徳経に対する王弼・郭象ら古代から現代まで続く解釈の伝統。","古典学・古典文学","East_Asia",-300,"https://en.wikipedia.org/wiki/Tao_Te_Ching",now,now),
(uid(),"論語注釈史","Analects commentary history","孔子の言行録『論語』に対する漢代から清代まで続く儒学的注釈の歴史。","古典学・古典文学","East_Asia",-400,"https://en.wikipedia.org/wiki/Analects",now,now),
(uid(),"史記","Records of the Grand Historian","司馬遷による中国最初の本格的通史。帝王本紀・列伝の形式を確立した。","古典学・古典文学","East_Asia",-109,"https://en.wikipedia.org/wiki/Records_of_the_Grand_Historian",now,now),
(uid(),"清代考証学","Qing dynasty evidential scholarship","清代の漢学・考証学の方法論。文献の厳密な実証的研究を重視した。","古典学・古典文学","East_Asia",1644,"https://en.wikipedia.org/wiki/Kaozheng",now,now),
(uid(),"コーラン注釈","Quran tafsir","イスラームの聖典クルアーンに対する古典的・現代的注釈の伝統（タフスィール）。","古典学・古典文学","West_Asia_North_Africa",600,"https://en.wikipedia.org/wiki/Tafsir",now,now),
(uid(),"ハディース学","Hadith scholarship","預言者ムハンマドの言行録（ハディース）の真偽判定・収集・分類の学問。","古典学・古典文学","West_Asia_North_Africa",700,"https://en.wikipedia.org/wiki/Hadith",now,now),
(uid(),"ヘブライ語聖書注釈","Hebrew Bible commentary","ラビ文学・マソラ学者・中世ユダヤ哲学者によるタナフへの注釈伝統。","古典学・古典文学","West_Asia_North_Africa",-500,"https://en.wikipedia.org/wiki/Biblical_hermeneutics",now,now),
(uid(),"マプングブウェ文明","Mapungubwe civilization","南アフリカの中世国家。金細工・交易ネットワークで栄えたアフリカ初期国家の考古学的研究。","古典学・古典文学","Sub_Saharan_Africa",900,"https://en.wikipedia.org/wiki/Mapungubwe",now,now),
(uid(),"グレートジンバブウェ","Great Zimbabwe","石造建築で知られる14世紀の南アフリカ王国。サブサハラ文明の高水準を示す。","古典学・古典文学","Sub_Saharan_Africa",1100,"https://en.wikipedia.org/wiki/Great_Zimbabwe",now,now),
(uid(),"ティカル遺跡","Tikal Maya site","グアテマラの古典期マヤ最大都市遺跡。神殿・広場・碑文の考古学的研究。","古典学・古典文学","Latin_America",100,"https://en.wikipedia.org/wiki/Tikal",now,now),
(uid(),"テオティワカン文明","Teotihuacan civilization","メキシコの古典期都市国家。太陽・月・死のピラミッドで知られる。","古典学・古典文学","Latin_America",100,"https://en.wikipedia.org/wiki/Teotihuacan",now,now),
(uid(),"チャビン文化","Chavin culture","ペルーのアンデス最古の宗教的中心地。各地の文化を統合する中心的影響を持った。","古典学・古典文学","Latin_America",-900,"https://en.wikipedia.org/wiki/Chav%C3%ADn_culture",now,now),
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
