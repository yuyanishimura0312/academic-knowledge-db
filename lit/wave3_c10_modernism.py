"""LIT-DB Phase 2 Wave 3 — C10: Western Modernism (40 concepts).

Subfield: lit_eu_modernism (id=6), region='西欧'.
Sources: Modernist Journals Project (modjourn.org), Project Gutenberg,
academic-grade Wikipedia (en/ja), and JSTOR-indexed scholarship summaries.
PD primary materials -> 'primary'; canonical scholarly secondary -> 'secondary';
synthetic critical categories -> 'tertiary'.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError

# Modernism is largely a single transnational period (~1890-1945 high modernism,
# with late modernist tail to ~1965). We define one umbrella period and use the
# same period_id for all concepts for consistency.
PERIODS = [
    ("モダニズム期", "Modernist Era", 1890, 1945,
     "ボードレールに連なる19世紀末象徴主義から第二次大戦終結までの、西欧文学・芸術における近代の自己解体的革新期。"),
    ("後期モダニズム期", "Late Modernism", 1945, 1965,
     "戦後ベケット・セレクション以降、ポストモダンへ移行するまでの遅延期。"),
]

# Source URL bases (real, verifiable)
MJP = "https://modjourn.org/"  # Modernist Journals Project (Brown Univ.)
GUTEN = "https://www.gutenberg.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"  # Stanford Encyclopedia of Philosophy
JSTOR = "https://www.jstor.org/"
POETRY_FOUND = "https://www.poetryfoundation.org/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_eu_modernism", region="西欧",
         original_script="roman")

# ============================================================
# A: モダニズムの主要技法（8件）
# ============================================================
add(**C, name_ja="意識の流れ", name_en="stream of consciousness",
    name_original="stream of consciousness", period_key="モダニズム期",
    definition="登場人物の意識内に去来する感覚・記憶・観念・連想を、論理的整理を経ずに連続的な言語の流れとして提示する語りの技法。ウィリアム・ジェイムズの心理学概念から借用され、ジョイス『ユリシーズ』、ヴァージニア・ウルフ『ダロウェイ夫人』、フォークナー『響きと怒り』で結晶化した。",
    background="ベルクソンの持続概念、フロイトの無意識論、ジェイムズの意識心理学が交差する20世紀初頭の主観性再定義の流れを背景とする。",
    development="エドゥアール・デュジャルダン『月桂樹は切られた』(1888)を先駆とし、1920年代に英語圏モダニズムの中心技法として確立。後の自由間接話法・内的独白と隣接して発展した。",
    historical_context="第一次世界大戦後の主体経験の断片化と、心理科学の文学的受容の同時並行。",
    primary_source_url=GUTEN+"ebooks/4300",
    primary_source_type="Project Gutenberg『ユリシーズ』",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"意識の連続的流れとして主体を表象する技法は、LLMのトークン逐次生成における「意識なき流れ」と表面的に酷似し、主体性の指標としての連続性を再定義する。",
         "related_ai_phenomenon":"LLMの逐次生成と意識の流れの構造的類似"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"持続（ベルクソン）",
         "description":"ベルクソンの持続概念と意識の流れ技法の哲学的基盤の共有。"}])

add(**C, name_ja="内的独白", name_en="interior monologue",
    name_original="interior monologue", period_key="モダニズム期",
    definition="登場人物の思考をその人物の声・語彙・統辞のまま地の文に直接提示する技法。意識の流れの一形態であるが、より明確に文法的に「私」の声として組織化される点が特徴。デュジャルダン由来でジョイス『ユリシーズ』モリー・ブルーム独白に頂点を見る。",
    background="フランス自然主義作家デュジャルダンの実験を、ヴァレリー・ラルボーがジョイスに紹介して英語モダニズムに移植された。",
    development="フォークナー、ベケット『モロイ』三部作、ヌーヴォー・ロマンへ展開。",
    historical_context="話法理論（バフチン以前の段階）と心理学的内面性発見の交差。",
    primary_source_url=WIKI_EN+"Interior_monologue",
    primary_source_type="Wikipedia: Interior monologue (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="自由間接話法", name_en="free indirect discourse",
    name_original="free indirect discourse / style indirect libre",
    period_key="モダニズム期",
    definition="登場人物の声・視点と語り手の声を融合させ、引用符や「彼は思った」の挿入なしに人物の意識を地の文として提示する語りの技法。フローベール『ボヴァリー夫人』に範型があり、ウルフ・ジョイス・ジェイムズで深化したモダニズム小説の中心装置。",
    background="フローベールの非人称的客観描写と、19世紀末以降の人物意識への内的接近の方法論的探求。",
    development="言語学（バリー、バフチン）の「二重音声性」概念と接続し、現代物語論の基本概念となった。",
    historical_context="リアリズムの語り手機能の解体と、近代小説の主観／客観境界の流動化。",
    primary_source_url=WIKI_EN+"Free_indirect_speech",
    primary_source_type="Wikipedia: Free indirect speech (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"二重音声性",
         "description":"バフチン物語論の二重音声性概念と自由間接話法の理論的接続。"}])

add(**C, name_ja="文学的モンタージュ", name_en="literary montage",
    name_original="literary montage", period_key="モダニズム期",
    definition="エイゼンシュテイン的映画モンタージュを文学に応用し、断片的場面・声・引用を意味的連結なしに並置することで、読者に新たな全体像を構成させる構成技法。ジョン・ドス・パソス『U.S.A.』三部作、デーブリーン『ベルリン・アレクサンダー広場』が代表例。",
    background="ロシア・フォルマリズム映画理論と、ダダイズムのコラージュ的発想の文学的移植。",
    development="ベンヤミンの『パサージュ論』が批評的・哲学的モンタージュ実践へ拡張し、現代の断片小説まで継承される。",
    historical_context="映画・写真・新聞メディアの並置的視覚経験の文学的内面化。",
    primary_source_url=WIKI_EN+"Montage_(literature)",
    primary_source_type="Wikipedia: Montage in literature",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="断片化", name_en="fragmentation",
    name_original="fragmentation", period_key="モダニズム期",
    definition="統一的物語・主体・世界観を意図的に解体し、不連続な断片の並置として作品を構成するモダニズムの構造原理。エリオット『荒地』の引用断片群、パウンド『キャントーズ』の多言語多時代並置に範型を見る。",
    background="第一次世界大戦による西欧文化の総合的危機認識と、ニーチェ・ベルクソン以降の主体批判の文学的具現化。",
    development="後期モダニズム・ポストモダン文学の基本様式となり、デジタル時代のハイパーテクスト的構造に継承される。",
    historical_context="戦間期の文化的危機意識と科学・哲学の認識論的革新。",
    primary_source_url=POETRY_FOUND+"poems/47311/the-waste-land",
    primary_source_type="Poetry Foundation『荒地』全文",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="神話的方法", name_en="mythical method",
    name_original="mythical method", period_key="モダニズム期",
    definition="T.S.エリオットがジョイス『ユリシーズ』論(1923)で命名した、現代の混沌たる経験を古代神話の構造で組織化する技法。ジョイス（オデュッセイア構造）、エリオット（聖杯神話）、エズラ・パウンドの古典借用に体現される。",
    background="フレイザー『金枝篇』、ジェイン・ハリソンらケンブリッジ古典学派の神話研究の文学的受容。",
    development="ユング元型論と接続し、20世紀の神話批評（ノースロップ・フライ）へ展開。",
    historical_context="人類学的神話研究と西洋文明危機論の文学的合流。",
    primary_source_url=WIKI_EN+"Mythical_method",
    primary_source_type="Wikipedia: Mythical method (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"Myth-Narratives","link_type":"shared_concept",
         "target_entity_name":"近代における神話の再構成",
         "description":"フレイザー以降の神話研究と20世紀文学の神話的方法の交差。"}])

add(**C, name_ja="異化", name_en="defamiliarization",
    name_original="ostranenie / остранение",
    period_key="モダニズム期",
    definition="ヴィクトル・シクロフスキー「方法としての芸術」(1917)が定式化した、見慣れた事物を不慣れに描き直すことで知覚を更新する文学技法。ロシア・フォルマリズムの中核概念であり、20世紀の前衛文学全体の理論的基礎を成す。",
    background="ロシア未来派の言語実験とロシア・フォルマリズム言語学の合流から生まれた理論。",
    development="ブレヒトの「異化効果」(Verfremdungseffekt)、現代物語論、ブリコラージュ的前衛芸術論まで継承。",
    historical_context="ロシア革命前後の言語的・知覚的革新の理論化。",
    primary_source_url=WIKI_EN+"Defamiliarization",
    primary_source_type="Wikipedia: Defamiliarization (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"模倣（imitatio）からの脱却を20世紀芸術の正統性根拠とした異化原理が、確率的に既存パターンを生成するLLMの創造性概念によって相対化される。",
         "related_ai_phenomenon":"LLMの確率的生成と異化的創造性の対立"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"フォルマリズム詩学",
         "description":"異化はロシア・フォルマリズムの中核詩学概念として、PT-DBにも収録される横断概念。"}])

add(**C, name_ja="エピファニー", name_en="epiphany (literary)",
    name_original="epiphany", period_key="モダニズム期",
    definition="日常的事物・状況の中で突然訪れる啓示的瞬間。ジェームズ・ジョイスが『スティーヴン・ヒアロー』『若い芸術家の肖像』で文学概念として確立し、宗教的顕現概念の世俗化として近代文学の認識論的中心瞬間となった。",
    background="カトリック典礼の顕現祭(Epiphany)概念のジョイスによる世俗化と、ワーズワース「自然の啓示」のロマン派的継承。",
    development="ウルフ「存在の瞬間」(moment of being)、プルースト「無意志的記憶」と並ぶモダニズムの認識論的核心瞬間概念群を形成。",
    historical_context="宗教的世界観の世俗化と文学的経験の超越的瞬間化。",
    primary_source_url=GUTEN+"ebooks/4217",
    primary_source_type="Project Gutenberg『若い芸術家の肖像』",
    importance_score=4, source_tier="primary", canonical_in_region="core")

# ============================================================
# B: 主要主題と世界観（8件）
# ============================================================
add(**C, name_ja="近代の危機", name_en="crisis of modernity",
    name_original="crisis of modernity", period_key="モダニズム期",
    definition="第一次世界大戦と工業化・都市化の加速によって西欧近代の進歩主義・合理主義が破綻したという文学的・哲学的認識。エリオット『荒地』、シュペングラー『西洋の没落』、ヴァレリー『精神の危機』が同時並行で表現した。",
    background="19世紀末の文化悲観主義（ニーチェ）と1914-18年大戦の物質的破局の合流。",
    development="戦後モダニズムの基層的世界観となり、フランクフルト学派（アドルノ・ホルクハイマー『啓蒙の弁証法』）の哲学的継承を生んだ。",
    historical_context="第一次大戦後のヨーロッパ精神的・物質的廃墟。",
    primary_source_url=POETRY_FOUND+"poems/47311/the-waste-land",
    primary_source_type="Poetry Foundation『荒地』",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="疎外", name_en="alienation",
    name_original="alienation / Entfremdung", period_key="モダニズム期",
    definition="近代的個人が世界・他者・労働・自己自身から切り離されているという感覚と、それを文学化する主題。マルクス（疎外労働）・ヘーゲル概念に発し、カフカ・カミュ・サルトルにおいて20世紀文学の中心主題となった。",
    background="ヘーゲル疎外論とマルクス『経済学・哲学草稿』の哲学的疎外概念の文学的継承。",
    development="実存主義文学（カミュ『異邦人』、サルトル『嘔吐』）で頂点に達し、戦後の不条理演劇まで延長。",
    historical_context="工業化・官僚制化・大衆社会化に対する個人の応答。",
    primary_source_url=GUTEN+"ebooks/5200",
    primary_source_type="Project Gutenberg『変身』(英訳)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"疎外論",
         "description":"マルクス・ヘーゲル系統の疎外論と20世紀文学的疎外主題の理論的共有。"}])

add(**C, name_ja="都市経験", name_en="urban experience",
    name_original="urban experience", period_key="モダニズム期",
    definition="近代大都市（ロンドン・パリ・ベルリン・ニューヨーク）の群衆・速度・匿名性・分裂的知覚を文学化する主題系。ボードレール『パリの憂鬱』を先駆とし、ジョイス『ダブリン市民』、ウルフ『ダロウェイ夫人』、デーブリーン『ベルリン・アレクサンダー広場』に結晶化。",
    background="ボードレール「遊歩者」(flâneur)、ジンメル「大都市と精神生活」が定式化した近代都市の心的経験。",
    development="ベンヤミン『パサージュ論』が批評的に総合し、ポストモダン都市論まで延長される。",
    historical_context="19世紀末以降の大都市化と中産階級的都市経験の普遍化。",
    primary_source_url=GUTEN+"ebooks/2814",
    primary_source_type="Project Gutenberg『ダブリン市民』",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"都市の人類学",
         "description":"シカゴ学派以降の都市人類学とモダニズム文学的都市経験の交差。"}])

add(**C, name_ja="時間意識", name_en="time consciousness",
    name_original="time consciousness", period_key="モダニズム期",
    definition="客観的・時計的時間ではなく、主観的・体験的に流動する時間（ベルクソン的持続）を文学的に再構築する主題。プルースト『失われた時を求めて』、ウルフ『ダロウェイ夫人』『灯台へ』、マン『魔の山』が範型を成す。",
    background="ベルクソンの持続(durée)概念、フッサール現象学の時間意識分析、アインシュタイン相対性理論の文化的衝撃。",
    development="フォークナー的非線形時間、マグリッチ・リアリズムの円環時間、ポストモダン的時間遊戯まで継承。",
    historical_context="近代物理学・哲学・心理学の時間概念革新と並走する文学実践。",
    primary_source_url=GUTEN+"ebooks/7178",
    primary_source_type="Project Gutenberg『失われた時を求めて』(英訳)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"時間意識（フッサール・ベルクソン）",
         "description":"現象学・生命哲学の時間概念とモダニズム文学的時間意識の理論的共有。"}])

add(**C, name_ja="主体の解体", name_en="dissolution of self",
    name_original="dissolution of self", period_key="モダニズム期",
    definition="統一的・自律的近代主体の解体と、複数化・分裂化された主体経験の文学化。ピランデッロ『一・誰でもない・十万』、ペソア「異名」、ベケット三部作の主体消失過程に体現される。",
    background="フロイトの無意識論、マッハ「自我は救済されない」、ニーチェ「超人」以降の主体批判哲学の文学的具現化。",
    development="ヌーヴォー・ロマン、ポストモダン文学、ポストヒューマニズム的文学批評まで延長される。",
    historical_context="19世紀末以降の主体批判哲学・心理学的革新の総合。",
    primary_source_url=WIKI_EN+"Modernist_literature",
    primary_source_type="Wikipedia: Modernist literature (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"モダニズムが既に解体した近代主体は、生成AIによってさらに非主体的テクスト生成として根本的に問い直される。AIテクストは「主体の解体」の論理的帰結としても、その極限としても解釈可能。",
         "related_ai_phenomenon":"主体なきAIテクスト生成と主体の解体テーマの連続性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"主体批判",
         "description":"ニーチェ・マッハ以降の主体批判哲学と文学的主体解体の交差。"}])

add(**C, name_ja="神話と歴史", name_en="myth and history",
    name_original="myth and history", period_key="モダニズム期",
    definition="直線的進歩史観と神話的循環時間の緊張・重ね合わせを主題化するモダニズムの世界観。エリオット、ジョイス、トマス・マン『ヨセフとその兄弟』、イェイツ『幻想録』に体現される、歴史と神話の往復構造。",
    background="シュペングラー文化循環論、フレイザー神話研究、ニーチェ「永劫回帰」の文学的受容。",
    development="戦後のラテンアメリカ・マジック・リアリズム（ガルシア=マルケス）、現代の神話小説まで継承。",
    historical_context="進歩史観の戦間期的破綻と、神話的時間の文学的回帰。",
    primary_source_url=WIKI_EN+"Mythopoeia",
    primary_source_type="Wikipedia: Mythopoeia",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="不安", name_en="anxiety",
    name_original="anxiety / Angst", period_key="モダニズム期",
    definition="存在の根拠喪失から生じる根源的不安を文学的中心経験とする主題。キェルケゴール『不安の概念』に発し、カフカ・ハイデガー『存在と時間』・サルトル・カミュにおいて20世紀の中核実存的経験となる。",
    background="キェルケゴールの宗教的不安概念、ハイデガー存在論の世俗化、二度の大戦の集合的不安の合流。",
    development="戦後実存主義文学・不条理演劇（イヨネスコ・ベケット）に結晶化。",
    historical_context="戦間期・戦後の集合的不安と個人実存の哲学化。",
    primary_source_url=GUTEN+"ebooks/5200",
    primary_source_type="Project Gutenberg『変身』(英訳)",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"存在論的不安",
         "description":"レイン・ギデンズらの社会人類学的不安研究と文学的不安主題の交差。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"不安（ハイデガー・キェルケゴール）",
         "description":"実存哲学の不安概念と文学的不安主題の理論的共有。"}])

add(**C, name_ja="戦争のトラウマ", name_en="war trauma",
    name_original="war trauma / shell shock",
    period_key="モダニズム期",
    definition="第一次大戦の塹壕戦と精神的傷害(shell shock)を文学化する主題系。レマルク『西部戦線異状なし』、ヘミングウェイ『武器よさらば』、ウルフ『ダロウェイ夫人』のセプティマス・スミス、シーグフリード・サスーン詩で結晶化した。",
    background="塹壕戦の前例なき心的・身体的破壊と、医学的トラウマ概念の文学的形象化。",
    development="第二次大戦・原爆・ホロコースト文学に継承され、20世紀後半のトラウマ理論（カルース、フェルマン）の文学批評的展開を生む。",
    historical_context="第一次大戦の機械化された大量殺戮の文学的応答。",
    primary_source_url=GUTEN+"ebooks/35684",
    primary_source_type="Project Gutenberg『ジェイコブの部屋』(ウルフ)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

# ============================================================
# C: 主要運動・流派（8件）
# ============================================================
add(**C, name_ja="イマジズム", name_en="Imagism",
    name_original="Imagism", period_key="モダニズム期",
    definition="エズラ・パウンドが1912-17年に主導した英米詩運動。①事物を直接的に扱う、②表現に絶対不要な語を使わない、③メトロノームではなく音楽的句法に従う、の三原則を掲げ、簡潔・具体的・正確な詩的言語を追求した。",
    background="フォード・マドックス・フォードのインプレッショニズム、T.E.ヒュームの古典主義詩論、フランス象徴主義の英米受容。",
    development="エイミー・ロウェル、H.D.（ヒルダ・ドゥリトル）、ウィリアム・カーロス・ウィリアムズに継承され、現代英米詩の基層を形成した。",
    historical_context="ヴィクトリア朝後期詩の修辞的過剰への反動として成立。",
    primary_source_url=POETRY_FOUND+"learn/glossary-terms/imagism",
    primary_source_type="Poetry Foundation: Imagism",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ヴォーティシズム", name_en="Vorticism",
    name_original="Vorticism", period_key="モダニズム期",
    definition="ウィンダム・ルイス・エズラ・パウンドが1914年に創始した英国前衛芸術・文学運動。雑誌『BLAST』を機関誌とし、未来派の動と立体派の構造を統合した「渦」(vortex)的形象を志向した。第一次大戦で短命に終わった。",
    background="マリネッティ未来派とキュビスム造形思想の英国的統合要求。",
    development="戦争での主要メンバー戦死により1917年に事実上消滅したが、後の英国モダニズムとパウンドの『キャントーズ』の方法論的源泉となる。",
    historical_context="戦前英国の前衛芸術運動と大戦による断絶。",
    primary_source_url=MJP+"render.php?id=mjp.2005.00.082",
    primary_source_type="Modernist Journals Project: BLAST",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シュルレアリスム", name_en="Surrealism",
    name_original="Surréalisme", period_key="モダニズム期",
    definition="アンドレ・ブルトンが1924年『シュルレアリスム宣言』で創始したフランス前衛運動。フロイト無意識論と自動記述(écriture automatique)を方法論的核とし、夢・偶然・無意識を芸術的真実の源泉とした。",
    background="ダダのニヒリズム的破壊からの転換と、フロイト精神分析のフランス的受容の合流。",
    development="文学（ブルトン、エリュアール、アラゴン）から美術（ダリ、エルンスト、マグリット）に拡張し、戦後ラテンアメリカ・マジック・リアリズムにも影響。",
    historical_context="第一次大戦後のヨーロッパ精神的危機と無意識発見の応答。",
    primary_source_url=WIKI_EN+"Surrealism",
    primary_source_type="Wikipedia: Surrealism (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ダダ", name_en="Dada",
    name_original="Dada", period_key="モダニズム期",
    definition="1916年チューリッヒのキャバレー・ヴォルテールでトリスタン・ツァラ、フーゴ・バル、リヒャルト・ヒュルゼンベックらが創始した、戦争・ブルジョワ文化への徹底的否定運動。意味の解体・偶然・パフォーマンスを武器とした反芸術運動。",
    background="第一次大戦のスイス中立地帯への亡命知識人による反戦運動の文化的形象化。",
    development="ベルリン（グロス、ハートフィールド）、パリ（ピカビア、デュシャン）に拡散し、シュルレアリスムへ継承される。",
    historical_context="第一次大戦中の徹底的なヨーロッパ文化否定。",
    primary_source_url=WIKI_EN+"Dada",
    primary_source_type="Wikipedia: Dada (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="表現主義", name_en="Expressionism",
    name_original="Expressionismus", period_key="モダニズム期",
    definition="20世紀初頭ドイツ語圏で展開した、客観的描写ではなく主観的感情・精神状態の強烈な表出を志向する文学・美術運動。文学ではトラークル、ベン、カイザー、トラー、初期カフカに体現される。",
    background="ニーチェ的生の哲学、ベルクソン直観主義、フロイト無意識論のドイツ的受容と、ヴィルヘルム期社会への精神的反逆。",
    development="ワイマール期の文学・演劇・映画（『カリガリ博士』）に展開し、ナチス政権下で「退廃芸術」とされ抑圧された。",
    historical_context="第一次大戦前後のドイツ社会の精神的動揺。",
    primary_source_url=WIKI_EN+"Expressionism",
    primary_source_type="Wikipedia: Expressionism (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="未来派", name_en="Futurism",
    name_original="Futurismo", period_key="モダニズム期",
    definition="フィリッポ・トンマーゾ・マリネッティが1909年「未来派宣言」(『フィガロ』紙)で創始したイタリア前衛運動。速度・機械・暴力・戦争を称揚し、過去の文化的伝統を徹底拒否する反伝統運動。",
    background="イタリア後発工業化への文化的応答と、ニーチェ的生の高揚思想の機械文明的具現化。",
    development="ロシア未来派（マヤコフスキー、フレーブニコフ）に分岐し、ファシズムへの政治的接続でマリネッティ路線は批判される一方、芸術形式は20世紀前衛の基礎となった。",
    historical_context="工業化・機械化の進展と戦争前の文化的高揚。",
    primary_source_url=WIKI_EN+"Futurism",
    primary_source_type="Wikipedia: Futurism (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハーレム・ルネサンス", name_en="Harlem Renaissance",
    name_original="Harlem Renaissance", period_key="モダニズム期",
    definition="1920年代ニューヨーク・ハーレムを中心に展開したアフリカ系アメリカ人の文学・音楽・美術運動。アラン・ロック『ニュー・ニグロ』、ラングストン・ヒューズ詩、ゾラ・ニール・ハーストン『彼らの目は神を見ていた』が代表する。",
    background="第一次大戦後の黒人北部移住(Great Migration)とハーレムの文化的集積、ジャズ文化の成熟。",
    development="1930年代の世界恐慌で運動は衰退するが、戦後公民権運動期の黒人文学（エリスン、ボールドウィン）の前史となる。",
    historical_context="アメリカ黒人の文化的自己主張と「ジャズ・エイジ」の交差。",
    primary_source_url=WIKI_EN+"Harlem_Renaissance",
    primary_source_type="Wikipedia: Harlem Renaissance (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"人種・エスニシティ研究",
         "description":"フランツ・ボアズ系統の人種人類学とハーレム・ルネサンスの相互影響。"}])

add(**C, name_ja="ブルームズベリー・グループ", name_en="Bloomsbury Group",
    name_original="Bloomsbury Group", period_key="モダニズム期",
    definition="20世紀初頭ロンドン・ブルームズベリー地区に集った知識人・芸術家集団。ヴァージニア・ウルフ、レナード・ウルフ、E.M.フォースター、リットン・ストレイチー、経済学者ケインズ、美術批評ロジャー・フライらが含まれる、英国モダニズムの中核共同体。",
    background="ケンブリッジ大学の哲学者G.E.ムーアの倫理学（『プリンキピア・エシカ』）の倫理的・美学的影響。",
    development="ホガース・プレス出版業を通じて英国モダニズム作品（エリオット、フロイト英訳）の発信拠点となる。",
    historical_context="エドワード朝後期の知的サロン文化と戦間期的解放思潮。",
    primary_source_url=WIKI_EN+"Bloomsbury_Group",
    primary_source_type="Wikipedia: Bloomsbury Group (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

# ============================================================
# D: 主要作家概念・批評概念（8件）
# ============================================================
add(**C, name_ja="客観的相関物", name_en="objective correlative",
    name_original="objective correlative", period_key="モダニズム期",
    definition="T.S.エリオット「ハムレットとその問題」(1919)が定式化した、特定の感情を喚起するため一連の対象・状況・出来事を選び取る詩的方法。感情の直接表出ではなく具体物を介する間接喚起としてモダニズム詩学の中心概念となった。",
    background="フランス象徴主義の暗示詩学とパウンドのイマジズムの理論的整理。",
    development="新批評(New Criticism)の中心概念として制度化され、20世紀詩学全体の基礎概念となる。",
    historical_context="ロマン派的感情吐露への批評的反動。",
    primary_source_url="https://www.bartleby.com/200/sw9.html",
    primary_source_type="Bartleby: Eliot 'Hamlet and His Problems'",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"客観的相関物",
         "description":"エリオット詩学の中心概念として詩学DBにも収録される横断概念。"}])

add(**C, name_ja="新しくせよ", name_en="Make it new",
    name_original="Make it new", period_key="モダニズム期",
    definition="エズラ・パウンドが古代中国の湯王の銘から借用してモダニズムのスローガン化した命題（同名エッセイ集1934）。あらゆる古典的伝統を当代的に新生させることが芸術家の使命であるとする、モダニズム創造論の標語。",
    background="儒教古典『大学』の銘文「苟日新、日日新、又日新」の翻訳的継承と、ヴィクトリア朝詩学への反動。",
    development="モダニズムの普遍的標語として20世紀芸術論全般に拡散し、ポストモダンの「make it old」的反動も生んだ。",
    historical_context="伝統と革新の弁証法的緊張。",
    primary_source_url=WIKI_EN+"Make_It_New",
    primary_source_type="Wikipedia: Make It New (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"模倣脱却を芸術家の使命とした20世紀の宣言が、確率的にパターンを再構成するLLMの「新しさ」によって相対化される。",
         "related_ai_phenomenon":"LLM時代の新規性概念の問い直し"}])

add(**C, name_ja="ジョイスのモノミス的方法", name_en="Joyce's monomyth method",
    name_original="Joyce's monomyth method", period_key="モダニズム期",
    definition="ジェームズ・ジョイスが『ユリシーズ』『フィネガンズ・ウェイク』で展開した、単一の神話原型を全人類的に変奏する方法論。ヴィーコ歴史循環論とジョセフ・キャンベル「英雄の旅」原型の文学的先駆けとして機能した。",
    background="ジャンバッティスタ・ヴィーコ『新科学』の歴史循環論と、フレイザー人類学的神話研究の総合。",
    development="ジョゼフ・キャンベル『千の顔を持つ英雄』(1949)の理論的先取りとして、戦後の神話批評・物語論に継承された。",
    historical_context="モダニズム神話的方法の極限的展開。",
    primary_source_url=GUTEN+"ebooks/4300",
    primary_source_type="Project Gutenberg『ユリシーズ』",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"Myth-Narratives","link_type":"shared_concept",
         "target_entity_name":"モノミス／英雄の旅",
         "description":"キャンベル神話論とジョイス的神話的方法の理論的接続。"}])

add(**C, name_ja="存在の瞬間", name_en="moment of being",
    name_original="moment of being", period_key="モダニズム期",
    definition="ヴァージニア・ウルフが自伝的随筆『過去のスケッチ』(1939執筆)で命名した、日常の「綿のような存在」(non-being)から突然立ち現れる啓示的瞬間。彼女のモダニズム小説の認識論的中心概念で、ジョイスのエピファニーと並ぶ。",
    background="ブルームズベリー・グループのG.E.ムーア倫理学的「内的状態の善」概念の文学的展開。",
    development="モダニズム文学の認識論的核心瞬間概念群（エピファニー、無意志的記憶）と並んで、20世紀小説論の基本概念となった。",
    historical_context="ウルフ晩年の自伝的省察と長年の小説実践の理論化。",
    primary_source_url=WIKI_EN+"Virginia_Woolf",
    primary_source_type="Wikipedia: Virginia Woolf (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"突発的・非反復的・体験的な「存在の瞬間」の真正性が、無限再生産可能なAI生成テクストの瞬間に対する倫理的・美学的対立軸を成す。",
         "related_ai_phenomenon":"AI生成における体験的瞬間の不在"}])

add(**C, name_ja="カフカ的", name_en="Kafkaesque",
    name_original="Kafkaesque / kafkaesk", period_key="モダニズム期",
    definition="フランツ・カフカ作品の特徴的な世界感覚を形容する批評的形容詞。不条理な権力構造・官僚制・規則体系の中で出口なく翻弄される個人の経験を指し、20世紀後半に英語・各国語の一般語彙となった。",
    background="カフカの『審判』『城』『変身』に体現される、近代官僚制と個人的不安の文学的形象化。",
    development="戦後の不条理文学（ベケット、イヨネスコ）、ポストモダン文学、現代の監視社会論まで影響範囲が拡張する形容語。",
    historical_context="ハプスブルク末期から戦間期の中欧官僚社会の文学的記録。",
    primary_source_url=GUTEN+"ebooks/7849",
    primary_source_type="Project Gutenberg『審判』(英訳)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="連続的現在", name_en="continuous present",
    name_original="continuous present", period_key="モダニズム期",
    definition="ガートルード・スタインが『ピカソ』『The Making of Americans』等で展開した、過去・未来を排して現在進行形のみで物事を提示する文体的方法論。反復と微細変奏を通じて時間を平面化する実験的散文技法。",
    background="ウィリアム・ジェイムズ心理学（ハーバード時代の師）の意識理論と、キュビスム同時代性の文学的応答。",
    development="ベケット後期作品、ヌーヴォー・ロマン、現代実験文学（リン・ハジニアン等L=A=N=G=U=A=G=E poets）まで継承。",
    historical_context="アメリカ実験文学の独自モダニズム展開。",
    primary_source_url=GUTEN+"ebooks/15396",
    primary_source_type="Project Gutenberg: Stein 'Tender Buttons'",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヘミングウェイの氷山理論",
    name_en="Hemingway's iceberg theory",
    name_original="iceberg theory", period_key="モダニズム期",
    definition="アーネスト・ヘミングウェイが『午後の死』(1932)で定式化した文体理論。表面的散文の下に作者が知る大量の情報を「水面下」に沈める省略の美学で、簡潔な英語散文がより深い感情・主題を喚起する効果を狙う。",
    background="新聞記者経験の簡潔文体訓練と、エズラ・パウンドの「不要語削除」原理の散文的実装。",
    development="20世紀後半の英米短篇小説の規範文体となり、レイモンド・カーヴァー、現代ミニマリスト散文に継承。",
    historical_context="モダニズム省略美学の散文版。",
    primary_source_url=WIKI_EN+"Iceberg_theory",
    primary_source_type="Wikipedia: Iceberg theory (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="フォークナーの南部意識の流れ",
    name_en="Faulkner's Southern stream of consciousness",
    name_original="Southern stream of consciousness",
    period_key="モダニズム期",
    definition="ウィリアム・フォークナーが『響きと怒り』『八月の光』『アブサロム、アブサロム！』で展開した、アメリカ南部の人種・歴史・敗北意識を多重的意識の流れで表現する独特のモダニズム手法。",
    background="ジョイス・ウルフの英国モダニズム手法の南部歴史的経験への適用。",
    development="戦後ラテンアメリカ・マジック・リアリズム（ガルシア=マルケスはフォークナーから多大な影響）、現代南部文学に継承。",
    historical_context="アメリカ南部の南北戦争敗北・人種問題の文学的内面化。",
    primary_source_url=WIKI_EN+"William_Faulkner",
    primary_source_type="Wikipedia: William Faulkner (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

# ============================================================
# E: メタモダニズム・批評概念（8件）
# ============================================================
add(**C, name_ja="高級／低俗芸術の分割",
    name_en="high vs low art divide",
    name_original="high vs low art divide", period_key="モダニズム期",
    definition="モダニズムが構築した、自律的・難解な高級芸術と大衆的・娯楽的低俗芸術の対立構造。アンドレアス・フイッセン『大いなる分裂』(1986)が批評的に総合し、モダニズムの本質的構造として理論化された。",
    background="19世紀末のブルジョワ的高級文化と都市大衆文化の同時発達と、両者の弁別欲求。",
    development="ポストモダンが意図的に分割を解体し、「大衆文化のモダニズム」（ジャズ、映画、推理小説）の再評価を生んだ。",
    historical_context="近代資本主義文化における階級的文化弁別。",
    primary_source_url=WIKI_EN+"After_the_Great_Divide",
    primary_source_type="Wikipedia: After the Great Divide (Huyssen)",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"高級芸術／低俗芸術の正典的弁別が、AI生成コンテンツの大量化と多様化によって、人間芸術／機械生成という新しい分割線へと再編される可能性。",
         "related_ai_phenomenon":"AI生成と人間芸術の新しい正典的分割"}])

add(**C, name_ja="モダニスト反小説", name_en="modernist anti-novel",
    name_original="modernist anti-novel", period_key="モダニズム期",
    definition="伝統的小説の物語性・人物造形・因果性を意図的に解体する小説形式。プルースト、ジョイス『フィネガンズ・ウェイク』、ベケット三部作、ヌーヴォー・ロマン（ロブ=グリエ）に体現される、小説の自己批判的形態。",
    background="19世紀リアリズム小説規範への反動と、内面性・言語自体の小説的探究の極限化。",
    development="戦後ヌーヴォー・ロマン、ポストモダン実験小説、現代のメタフィクションへ継承。",
    historical_context="小説形式自体の自己反省的探究。",
    primary_source_url=WIKI_EN+"Anti-novel",
    primary_source_type="Wikipedia: Anti-novel (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"伝統的物語性を解体する反小説の方法論が、生成AIの非人間的・非物語的テクスト生成と構造的に類比される。物語の人間中心性が改めて問われる。",
         "related_ai_phenomenon":"AI生成テクストの非物語的特性"}])

add(**C, name_ja="モダニズム雑誌",
    name_en="modernist periodicals",
    name_original="Little Review, BLAST, transition",
    period_key="モダニズム期",
    definition="モダニズム文学の発表・流通を担った小冊子的雑誌群。『The Little Review』（1914-29、ジョイス『ユリシーズ』連載）、『BLAST』（1914-15、ヴォーティシズム機関誌）、『transition』（1927-38、パリ前衛誌）を代表とする、運動の物質的基盤。",
    background="商業出版に拒絶された前衛作品の流通基盤として、エディター主導の小規模高度雑誌形態が必要とされた。",
    development="Modernist Journals Project（ブラウン大学）が2000年代以降全文デジタル化し、研究基盤を再構築している。",
    historical_context="モダニズムの制度的・物質的条件としての小冊子文化。",
    primary_source_url=MJP,
    primary_source_type="Modernist Journals Project (Brown University)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="モダニスト亡命", name_en="modernist exile",
    name_original="modernist exile", period_key="モダニズム期",
    definition="多くのモダニズム作家が政治的・文化的・自発的に祖国から離れた状態で創作したという、モダニズムの構造的特徴。ジョイス（アイルランド→イタリア・スイス）、エリオット（米→英）、パウンド（米→英・伊）、コンラッド（ポーランド→英）、ナボコフ（露→米）、ベケット（愛→仏）に体現。",
    background="近代国民国家システムと、戦争・革命による人的移動の常態化。",
    development="戦後ポストコロニアル文学、現代ディアスポラ文学（W.G.ゼーバルトら）に継承。",
    historical_context="20世紀の戦争・革命・全体主義による人的離散の文学化。",
    primary_source_url=WIKI_EN+"Exile_in_literature",
    primary_source_type="Wikipedia: Exile in literature",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"亡命作家の多言語的・翻訳的創作実践（ナボコフ、ベケットの仏英自己翻訳）が、AI多言語生成の文学的位置を考える上で重要な前史となる。",
         "related_ai_phenomenon":"AI多言語生成と多言語的創作の系譜"}])

add(**C, name_ja="アンチミメシス", name_en="antimimesis",
    name_original="antimimesis", period_key="モダニズム期",
    definition="アリストテレス的模倣（ミメシス）詩学への反動として、芸術が現実を模倣するのではなく、現実が芸術を模倣するというオスカー・ワイルド「虚言の衰退」(1889)由来の芸術観。モダニズム自律美学の理論的基盤の一つ。",
    background="19世紀末唯美主義（ワイルド、ペイター）の芸術自律論。",
    development="モダニズムの芸術自律論、戦後の構築主義美学（ヴィルヘルム・ヴォリンガー）まで継承。",
    historical_context="リアリズム規範からの離脱と芸術自律性の確立。",
    primary_source_url=GUTEN+"ebooks/887",
    primary_source_type="Project Gutenberg: Wilde 'Intentions'",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="自己目的的芸術", name_en="autotelic art",
    name_original="autotelic art", period_key="モダニズム期",
    definition="芸術作品がそれ自体を目的とし、外的（道徳的・実用的・政治的）目的に従属しないとするモダニズム美学の中核命題。「芸術のための芸術」(l'art pour l'art)を継承し、新批評の「言語的構築物としてのテクスト」概念に結実。",
    background="カント『判断力批判』の無関心的快の伝統と、19世紀フランスのテオフィル・ゴーティエ・パルナシアンの「芸術のための芸術」運動。",
    development="新批評・形式主義詩学・脱構築まで延長される、モダニズム美学の根幹概念。",
    historical_context="芸術の社会的有用性論への対抗的自律論。",
    primary_source_url=WIKI_EN+"Art_for_art%27s_sake",
    primary_source_type="Wikipedia: Art for art's sake",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="モダニスト崇高", name_en="modernist sublime",
    name_original="modernist sublime", period_key="モダニズム期",
    definition="ロンギノス・カント・バーク以来の伝統的崇高概念をモダニズム的に変容させ、断片化・解体・空虚・トラウマの中に立ち現れる新しい崇高経験。エリオット『荒地』、ベケット晩年作品、戦後アンセルム・キーファー絵画に体現される。",
    background="第一次大戦後の伝統的美的範疇の破綻と、否定的崇高（negative sublime）の必要。",
    development="ジャン=フランソワ・リオタール『崇高と前衛』(1991)が哲学的に総合し、ポストモダン崇高論として継承。",
    historical_context="20世紀の集合的トラウマ経験の美学化。",
    primary_source_url=SEP+"sublime/",
    primary_source_type="Stanford Encyclopedia: Sublime",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"モダニスト崇高がトラウマや空虚という体験の真正性を要件とするのに対し、AI生成テクストの「崇高」は体験的真正性を欠いた構文的崇高として位置付けられ、両者の差異が美学的問いを生む。",
         "related_ai_phenomenon":"AI生成と体験的真正性の問題"}])

add(**C, name_ja="後期モダニズム", name_en="late modernism",
    name_original="late modernism", period_key="後期モダニズム期",
    definition="第二次大戦後（1945-65頃）に高モダニズムを継承しつつポストモダンへと移行する過渡期の文学。ベケット三部作、ナボコフ『ロリータ』、ヌーヴォー・ロマン、戦後ニューヨーク派詩を含む、モダニズムの最終的展開期。",
    background="高モダニズムの主要作家の戦後活動継続と、新世代によるモダニズム継承。",
    development="1960年代後半以降ポストモダン文学（ピンチョン、バース）に明確に変態し、モダニズムの歴史化が進む。",
    historical_context="戦後の冷戦下文化と消費社会化の文学的応答。",
    primary_source_url=WIKI_EN+"Late_modernism",
    primary_source_type="Wikipedia: Late modernism (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")


def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="西欧",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid
        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            pkey = entry.pop("period_key", None)
            if pkey:
                entry["period_id"] = period_ids[pkey]
            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            name_to_id[entry["name_ja"]] = cid
            for ax in fourth_axes:
                try:
                    db.tag_fourth_transform(cid, **ax)
                    fourth_count += 1
                except LitDBError as e:
                    print(f"  [warn] fourth_transform tag failed for {entry['name_ja']}: {e}")
            for cd in cross_domain:
                try:
                    db.insert_cross_domain(
                        lit_entity_type="concept", lit_entity_id=cid,
                        target_db=cd["target_db"], link_type=cd["link_type"],
                        target_entity_id=cd.get("target_entity_id"),
                        target_entity_name=cd.get("target_entity_name"),
                        description=cd.get("description"))
                    cd_count += 1
                except LitDBError as e:
                    print(f"  [warn] cross_domain failed for {entry['name_ja']}: {e}")
        summary = db.progress_summary()
        print(f"[c10] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c10] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
