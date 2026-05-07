"""LIT-DB Phase 2 Wave 10 — C09: European Symbolism / fin-de-siècle (40 concepts).

Subfield: lit_eu_realism (id=5), region='西欧'.
象徴主義・世紀末担当（C08 リアリズム・自然主義と同 subfield、重複ゼロを厳守）。
Sources: Project Gutenberg (PD primary texts of Baudelaire, Verlaine, Rimbaud,
Mallarmé, Huysmans, Wilde, Yeats, etc.), Gallica (BnF), ARTFL Project (U Chicago),
Poetry Foundation (academic), Stanford Encyclopedia of Philosophy, and
academic-grade Wikipedia (en/fr/ja).
PD primary materials -> 'primary'; canonical scholarly secondary -> 'secondary';
synthetic critical categories -> 'tertiary'.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError

# ============================================================
# Periods (one umbrella + national/late-stage variants)
# ============================================================
PERIODS = [
    ("象徴主義期", "Symbolist Era", 1857, 1900,
     "ボードレール『悪の華』(1857)からマラルメ没後（1898）までの、フランスを中核としつつ汎ヨーロッパに伝播した象徴主義詩学・美学の中心期。"),
    ("世紀末", "fin de siècle", 1880, 1914,
     "1880年代から第一次大戦勃発までの、デカダンス・唯美主義・象徴主義・初期モダニズムが交錯する西欧文化の過渡期。"),
    ("ラファエル前派期", "Pre-Raphaelite Era", 1848, 1900,
     "ラファエル前派兄弟団結成（1848）から世紀末までの、英国における象徴主義の先駆としての中世主義的・唯美主義的運動期。"),
]

# Source URL bases (real, verifiable)
GUTEN = "https://www.gutenberg.org/"
GALLICA = "https://gallica.bnf.fr/"
ARTFL = "https://artfl-project.uchicago.edu/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
POETRY_FOUND = "https://www.poetryfoundation.org/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_eu_realism", region="西欧",
         original_script="roman")

# ============================================================
# A: フランス象徴主義（8件）
# ============================================================
add(**C, name_ja="『悪の華』", name_en="The Flowers of Evil",
    name_original="Les Fleurs du mal", period_key="象徴主義期",
    definition="シャルル・ボードレール（1821-67）が1857年に発表した詩集。都市の倦怠（spleen）、官能、悪、美の中の腐敗を主題に近代詩の出発点を画した。出版直後に風俗紊乱で禁書6篇の判決を受けつつ、後の象徴主義・モダニズム詩の母胎となった。",
    background="1840-50年代パリの近代化と、ロマン主義の終焉、近代都市生活の不安・倦怠・群衆経験。",
    development="1861年第二版で構成を再編し、死後1868年版で完成形に。マラルメ、ヴェルレーヌ、ランボー、T.S.エリオット、ベンヤミンに直接的影響。",
    historical_context="第二帝政期パリの近代化と道徳統制、新しい都市美学の必要性。",
    primary_source_url=GUTEN+"ebooks/36286",
    primary_source_type="Project Gutenberg: Les Fleurs du mal (FR original)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"ボードレールの「悪」「腐敗」「都市倦怠」の真正性は具体的な近代都市経験に根差すのに対し、AI生成詩はそうした体験的真正性を欠く。世紀末美学の真正性問題が再浮上する。",
         "related_ai_phenomenon":"AI生成詩と都市経験の真正性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"フィン・ド・シエクル文化",
         "description":"世紀末文化人類学（モースら）が論じる近代都市経験の象徴主義的形象化。"}])

add(**C, name_ja="万物照応", name_en="correspondences",
    name_original="correspondances", period_key="象徴主義期",
    definition="ボードレールが詩「Correspondances」（『悪の華』所収）で定式化した、自然界の諸感覚（色・香・音）相互、および可視世界と精神的世界が秘密の象徴的対応関係で結ばれているという象徴主義の中核教義。スウェーデンボリ神秘主義に由来し、象徴主義詩学の存在論的基盤となった。",
    background="スウェーデンボリ『天界と地獄』、ドイツロマン主義（ノヴァーリス）の世界象徴論。",
    development="マラルメの「象徴」概念、ヴェルレーヌの音楽性、ランボーの色彩共感覚（「母音」）に展開。",
    historical_context="科学的唯物論への対抗としての象徴的世界観の再構築。",
    primary_source_url=GUTEN+"ebooks/36286",
    primary_source_type="Project Gutenberg: Les Fleurs du mal (Correspondances)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"万物照応の読解には読者の象徴的・神秘的解釈能力が前提とされるが、AI読解はパターン認識として「対応」を扱う。象徴の解釈学的次元が再考される。",
         "related_ai_phenomenon":"AI読解における象徴解釈の限界"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"スウェーデンボリ照応説",
         "description":"スウェーデンボリの神学的照応説の詩学への移植。"}])

add(**C, name_ja="何より音楽を", name_en="Music above all things",
    name_original="De la musique avant toute chose", period_key="象徴主義期",
    definition="ポール・ヴェルレーヌ（1844-96）の詩「詩法」(Art poétique, 1882)冒頭の宣言。詩は意味よりも音楽的響きを第一とし、奇数音節（impair）と曖昧さ（nuance）を尊ぶべきとする象徴主義詩学の中心テーゼ。詩を絵画・修辞から解放し、音楽芸術に近づける綱領となった。",
    background="ワーグナーのGesamtkunstwerk思想と、フランス詩の韻律的固定性への反動。",
    development="マラルメの「純粋詩」「韻文の危機」概念、ベルレーヌ自身の『言葉なきロマンス』(1874)に展開。後の自由詩運動の理論的支柱となる。",
    historical_context="近代芸術における音楽の特権化（パターのいう「音楽の状態」）。",
    primary_source_url=GUTEN+"ebooks/14700",
    primary_source_type="Project Gutenberg: Verlaine 'Jadis et Naguère' (Art poétique収録)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="見者の手紙", name_en="Letter of the Seer",
    name_original="Lettre du voyant", period_key="象徴主義期",
    definition="アルチュール・ランボー（1854-91）が1871年5月にポール・ドメニとジョルジュ・イザンバールに送った2通の手紙の総称。「私は他者である」(Je est un autre)の宣言と、「あらゆる感覚の長期的・大規模・理性的錯乱」によって詩人を「見者」(voyant)に仕立てるとする詩論を含む、近代詩学の革命的文書。",
    background="ロマン主義の天才詩人観の継承と、近代主体の解体への先駆的洞察。",
    development="ランボー自身の『地獄の季節』『イリュミナシオン』に実践され、20世紀シュルレアリスム（ブルトンが「私は他者である」を中心テーゼ化）へ継承。",
    historical_context="パリ・コミューン直後の社会的・精神的混乱の中での詩人の使命の再定義。",
    primary_source_url=WIKI_FR+"Lettre_du_voyant",
    primary_source_type="Wikipedia FR: Lettre du voyant (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ランボーの「私は他者である」(Je est un autre)は近代主体の自己同一性を揺るがした。LLMが「他者の声」を生成する現代において、詩人＝見者という非人称的詩作主体のモデルが再考される。",
         "related_ai_phenomenon":"LLMの非人称的生成と『私は他者である』"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"主体の解体",
         "description":"近代主体批判の系譜にランボー詩学を位置付ける哲学的接続。"}])

add(**C, name_ja="純粋詩", name_en="pure poetry",
    name_original="poésie pure", period_key="象徴主義期",
    definition="ステファヌ・マラルメ（1842-98）が定式化し、後にポール・ヴァレリー、アンリ・ブレモンが継承した、物語・教訓・感傷を排し、言語の音楽性と暗示性のみで成り立つべき詩の理想。「詩人は自分の主導権を語に委ねる」（『書物について』）に集約される、自律的言語芸術としての詩観。",
    background="エドガー・アラン・ポー「詩作の哲学」の翻訳・受容、ヴァーグナー音楽の自律性、唯物論への対抗。",
    development="ヴァレリーの「詩学」、新批評の「言語的構築物」概念、20世紀構造主義詩学までの長期的影響。",
    historical_context="近代芸術の自律化と、商業的・教化的文学への対抗としての詩の特権化。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k71326n",
    primary_source_type="Gallica BnF: Mallarmé 'Divagations' (1897)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"マラルメ「詩人は語に主導権を委ねる」というテーゼは、LLMが言語自身に生成を委ねる現代の言語芸術の先駆と読み替えうる。純粋詩の音楽的理想が機械的生成の文脈で再評価される。",
         "related_ai_phenomenon":"LLMの言語自律的生成と純粋詩の理想"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"言語自律生成",
         "description":"純粋詩の言語自律理念とLLMの自律的言語生成の構造的並行。"}])

add(**C, name_ja="『骰子一擲』", name_en="A Throw of the Dice",
    name_original="Un coup de dés jamais n'abolira le hasard",
    period_key="象徴主義期",
    definition="マラルメが1897年『コスモポリス』誌に発表し1914年に決定版が刊行された、近代詩史を画する空間的構成詩。ページ全体を画布として、活字の大小・配置・余白を意味要素とし、「思考はサイコロ投げ」という哲学的命題と詩のタイポグラフィ的革新を結合した。",
    background="マラルメ後期の言語・書物理論（『書物について』）、ワーグナー総合芸術論、印刷技術の象徴化。",
    development="20世紀具体詩、視覚詩、エズラ・パウンド『キャントーズ』、デリダ『プレイヤード論』のタイポグラフィ的読解、現代デジタル詩まで継承。",
    historical_context="近代書物文化の頂点とその自己反省的解体。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k1071316",
    primary_source_type="Gallica BnF: Mallarmé 'Un coup de dés' (NRF 1914)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"『骰子一擲』のタイポグラフィ的詩は線形的物語性を解体し、空間的・同時的読解を要求する。デジタル時代の非線形テクスト（ハイパーテクスト、AI生成可変テクスト）の先駆として再評価される。",
         "related_ai_phenomenon":"非線形テクストとAI生成の可変構造"}])

add(**C, name_ja="メーテルランク象徴主義劇", name_en="Maeterlinck symbolist drama",
    name_original="théâtre symboliste",
    period_key="象徴主義期",
    definition="モーリス・メーテルランク（1862-1949、1911年ノーベル賞）が確立した象徴主義演劇形式。『ペレアスとメリザンド』(1892)、『青い鳥』(1908)に代表され、心理リアリズムを排し、沈黙・暗示・寓意・運命の感覚を中心とする「静的演劇」(théâtre statique)を提唱した。",
    background="自然主義演劇（ゾラ、アントワーヌ）への反動と、ワーグナー的総合芸術観の演劇への適用。",
    development="ドビュッシーがオペラ化（1902年『ペレアスとメリザンド』）し、20世紀不条理演劇（ベケット、イヨネスコ）の前史となる。",
    historical_context="世紀末ベルギーにおけるフランス語文化と、北方神秘主義の融合。",
    primary_source_url=GUTEN+"ebooks/8214",
    primary_source_type="Project Gutenberg: Maeterlinck 'Pelléas et Mélisande'",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="『さかしま』", name_en="Against Nature",
    name_original="À rebours", period_key="世紀末",
    definition="ジョリス=カルル・ユイスマンス（1848-1907）が1884年に発表したデカダンス文学の聖典。貴族デ・ゼッサントが世俗を断ち隠遁邸宅で人工的・倒錯的快楽を追求する物語。自然主義から象徴主義・カトリック神秘主義への転換点を画し、ワイルド『ドリアン・グレイの肖像』に直接的影響を与えた。",
    background="ゾラ自然主義への反動と、世紀末の精神的疲弊・逃避願望。",
    development="ワイルド、ダヌンツィオ、ジョン・グレイ、Yellow Bookサークルへ波及。批評ではバルベ・ドールヴィイ、レミ・ド・グールモンが評価。",
    historical_context="第三共和制下フランスにおける産業主義への美学的反逆。",
    primary_source_url=GUTEN+"ebooks/12341",
    primary_source_type="Project Gutenberg: Huysmans 'À rebours'",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"デ・ゼッサントの人工的・反自然的美学は、自然なき芸術の真正性を問う。AI生成芸術が「自然」「体験」を経由しない芸術の極限であるとき、ユイスマンス的「人工楽園」が新しい意味で再来する。",
         "related_ai_phenomenon":"AI生成と人工的美学の系譜"}])

# ============================================================
# B: 主要主題と象徴（8件）
# ============================================================
add(**C, name_ja="共感覚", name_en="synesthesia",
    name_original="synesthésie", period_key="象徴主義期",
    definition="複数の感覚（色彩・音響・香気・触感）が交差する知覚現象、およびそれを詩的原理として用いる象徴主義詩学。ボードレール「万物照応」、ランボー「母音」(1871、A=黒、E=白、I=赤、U=緑、O=青)、ユイスマンス『さかしま』の「香水交響楽」「リキュール・オーケストラ」に体現される。",
    background="近代生理学の感覚研究（ヘルムホルツ、フェヒナー）と、ロマン主義の総合的世界象徴論。",
    development="20世紀のスクリャービン共感覚的音楽、カンディンスキー絵画、現代神経科学の共感覚研究まで継承。",
    historical_context="近代における感覚の科学化と、感覚の詩的再統合の試み。",
    primary_source_url=WIKI_EN+"Synesthesia_in_art",
    primary_source_type="Wikipedia: Synesthesia in art (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"共感覚は感覚間の越境的言語化を要求する。マルチモーダルAIが画像・音・テクストを横断的に処理する現代、共感覚詩学が新しい言語論的射程を獲得する。",
         "related_ai_phenomenon":"マルチモーダルAIと共感覚的表現"},
        {"axis":"受容","status":"partial",
         "rationale":"共感覚的読解は読者の感覚的想像力を要請するが、AIによる感覚記号の対応学習は別種の「読み」を構成する。",
         "related_ai_phenomenon":"AI読解における感覚連合"}])

add(**C, name_ja="ダンディ", name_en="the dandy",
    name_original="dandy", period_key="世紀末",
    definition="ジョージ・ブラメル（1778-1840）に範を取り、ボードレール『現代生活の画家』(1863)が「英雄的近代主体」として理論化した、洗練された装い・冷静な無関心・芸術化された生活様式を本質とする美学的人格類型。世紀末デカダンスの理想的人物像となった。",
    background="リージェンシー期英国の社交文化と、産業ブルジョワへの貴族的反逆。",
    development="バルベ・ドールヴィイ『ダンディズムについて』(1845)、ワイルド、ダヌンツィオ、芥川龍之介の自己造形まで波及。",
    historical_context="19世紀ブルジョワ社会の画一化への美学的個人主義の対抗。",
    primary_source_url=GUTEN+"ebooks/45713",
    primary_source_type="Project Gutenberg: Baudelaire 'Le Peintre de la vie moderne' 由来資料",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="憂愁", name_en="spleen",
    name_original="le spleen", period_key="象徴主義期",
    definition="ボードレールが『悪の華』第一部「Spleen et Idéal」で中心化した、近代都市人の慢性的倦怠・形而上的不安・時間の重圧を表す感情語。ギリシア医学の「黒胆汁」(spleen)に由来し、英ロマン派の「英国病」(English malady)経由で受容され、近代詩の中心情緒となった。",
    background="ロマン主義のメランコリー伝統と、近代都市生活の精神病理学的経験。",
    development="ヴェルレーヌ、ラフォルグ、ボー・ブランマー、エリオット『荒地』のmodernist ennuiまで継承。",
    historical_context="近代産業都市における時間感覚と精神生活の質的変化。",
    primary_source_url=GUTEN+"ebooks/36286",
    primary_source_type="Project Gutenberg: Baudelaire 'Spleen' 群",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アンニュイ", name_en="ennui",
    name_original="ennui", period_key="世紀末",
    definition="フランス語で「倦怠」「無聊」を意味し、世紀末文学において、近代人が経験する形而上的退屈・存在の無意味感・刺激への渇望が混合した精神状態を指す中心概念。ボードレール「読者へ」(Au lecteur)で「最も醜悪な怪物」と呼ばれ、ユイスマンス、ラフォルグ、フローベール『感情教育』に共通する世紀末の通奏低音。",
    background="パスカルのdivertissement論、ロマン主義の世界苦(Weltschmerz)伝統。",
    development="20世紀実存主義（サルトル『嘔吐』）、不条理文学、現代の「実存的退屈」論まで継承。",
    historical_context="近代における時間の空虚化と意味の喪失経験。",
    primary_source_url=GUTEN+"ebooks/36286",
    primary_source_type="Project Gutenberg: Baudelaire 'Au lecteur'",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="デカダンス", name_en="decadence",
    name_original="décadence", period_key="世紀末",
    definition="文明・芸術が爛熟期を過ぎ衰退期に入った状態、およびその衰退に美的価値を見出す世紀末文学運動。テオフィル・ゴーティエ『悪の華』序文(1868)、ポール・ブールジェ『現代心理研究』(1883)、アナトール・バジュ雑誌『ル・デカダン』(1886-89)を通じて運動化し、ヨーロッパ全域に波及した。",
    background="ローマ帝国衰退期文学（ペトロニウス、アプレイウス）の世紀末的再評価。",
    development="フランス→英国（ワイルド、ビアズリー、Yellow Book）、イタリア（ダヌンツィオ）、ロシア（メレシュコフスキー）へ拡散。",
    historical_context="第三共和制安定期フランスの文化的自己疲労意識と、近代進歩史観への倒錯的反逆。",
    primary_source_url=WIKI_EN+"Decadent_movement",
    primary_source_type="Wikipedia: Decadent movement (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="象牙の塔", name_en="ivory tower",
    name_original="tour d'ivoire", period_key="象徴主義期",
    definition="シャルル=オーギュスタン・サント=ブーヴが詩人アルフレッド・ド・ヴィニーを評して「象牙の塔」(tour d'ivoire)に閉じこもると批判的に述べた(1837)ことを起源とし、世紀末以降は象徴主義詩人・芸術家が世俗から隔絶した自律的美的空間に立てこもることを肯定的に表す象徴語となった。",
    background="ロマン主義天才詩人観と、社会的批判詩学（ユゴー）への対抗としての美的隔絶論。",
    development="20世紀芸術自律論（モダニズム）、戦後アカデミズム批判（学者の象牙の塔批判）まで意味を変えつつ継承。",
    historical_context="近代における芸術と社会の分化と、芸術自律性の象徴化。",
    primary_source_url=WIKI_EN+"Ivory_tower",
    primary_source_type="Wikipedia: Ivory tower (academic)",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="芸術のための芸術", name_en="art for art's sake",
    name_original="l'art pour l'art", period_key="象徴主義期",
    definition="芸術は道徳・宗教・実用・政治から独立し、芸術それ自体を目的とすべきとする美学的綱領。テオフィル・ゴーティエ『モーパン嬢』序文(1835)で定式化し、パルナシアン詩派、象徴主義、英国唯美主義（ペイター、ワイルド）、20世紀モダニズム自律美学の根幹をなす。",
    background="カント『判断力批判』の無関心的快、ヴィクトル・クザン哲学美学の系譜。",
    development="フランス→英国唯美主義→モダニズム→新批評→20世紀芸術自律論の根幹概念として継承。",
    historical_context="近代における芸術・社会の分化と、ブルジョワ的有用性論への抵抗。",
    primary_source_url=WIKI_EN+"Art_for_art%27s_sake",
    primary_source_type="Wikipedia: Art for art's sake (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"「芸術のための芸術」は芸術の自律性を真正性の根拠としたが、AI生成芸術は「誰のための」「何のための」自律かを再問する。芸術自律論の前提が再考される。",
         "related_ai_phenomenon":"AI生成芸術と芸術自律論の再考"},
        {"axis":"主体","status":"rethinking",
         "rationale":"芸術自律論は芸術家の主体的選択を前提とするが、AI生成において「主体」は分散し、自律性の主体的根拠が不明瞭になる。",
         "related_ai_phenomenon":"AIにおける芸術主体の分散"}])

add(**C, name_ja="衰退の美", name_en="beauty in decay",
    name_original="beauté de la décadence", period_key="世紀末",
    definition="衰退・崩壊・腐敗・病・死の中に独特の美を見出す世紀末美学的態度。ボードレール「腐肉」(Une charogne)に範型を見、ユイスマンス『さかしま』の人工的衰退美、ダヌンツィオ『死の勝利』、ワイルド『ドリアン・グレイの肖像』に展開。健康・進歩・調和という古典美学の前提への倒錯的反逆。",
    background="ロマン主義の廃墟趣味、ゴシック小説の死の美学、19世紀末の文化的衰退意識。",
    development="20世紀ホラー文学、ゴス美学、現代の廃墟美学（ruin lust）まで継承。",
    historical_context="近代進歩史観への美学的反逆。",
    primary_source_url=GUTEN+"ebooks/36286",
    primary_source_type="Project Gutenberg: Baudelaire 'Une charogne'",
    importance_score=3, source_tier="primary", canonical_in_region="major")

# ============================================================
# C: 各国象徴主義（8件）
# ============================================================
add(**C, name_ja="イェイツのアイルランド象徴主義",
    name_en="Yeats's Irish Symbolism",
    name_original="Yeats Irish symbolism", period_key="世紀末",
    definition="ウィリアム・バトラー・イェイツ（1865-1939、1923年ノーベル賞）が1890-1900年代に確立した、フランス象徴主義（マラルメ、ヴィリエ）と、ケルト神話・神秘主義（黄金の夜明け団）、アイルランド民族復興運動を統合した独自の象徴詩学。詩集『葦間の風』(1899)、『塔』(1928)に体現。",
    background="アイルランド民族主義文化復興（ゲール文芸協会、アベイ劇場）と、フランス象徴主義の英訳受容（アーサー・シモンズ『文学における象徴主義運動』1899）。",
    development="後期は『幻想録』(1925)の私的神秘主義体系に発展し、英語圏モダニズム詩への直接的橋渡しとなった。",
    historical_context="世紀末アイルランドの文化的・政治的覚醒と、英国象徴主義の受容。",
    primary_source_url=GUTEN+"ebooks/49608",
    primary_source_type="Project Gutenberg: Yeats 'The Wind Among the Reeds'",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="シュテファン・ゲオルゲ", name_en="Stefan George",
    name_original="Stefan George", period_key="世紀末",
    definition="シュテファン・ゲオルゲ（1868-1933）はドイツ象徴主義を代表する詩人。マラルメに直接師事し帰国後『芸術草紙』(Blätter für die Kunst, 1892-1919)を主宰、貴族的・儀礼的・カリスマ的言語芸術観を展開した。詩集『魂の年』(1897)、『七つの環』(1907)、ゲオルゲ・サークルが彼を中心に形成された。",
    background="マラルメ象徴主義のドイツへの直接移植と、ヴィルヘルム時代ドイツの文化的閉塞への美学的反逆。",
    development="フリードリヒ・グンドルフ、エルンスト・カントーロヴィチらゲオルゲ・サークル知識人を介して、ヴァイマル文化・リルケ・ハイデガー後期詩観に影響。",
    historical_context="ヴィルヘルム期ドイツのブルジョワ文化への貴族的・美学的反逆。",
    primary_source_url=WIKI_EN+"Stefan_George",
    primary_source_type="Wikipedia: Stefan George (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="マラルメの国際的影響",
    name_en="Mallarmé's international influence",
    name_original="influence internationale de Mallarmé",
    period_key="象徴主義期",
    definition="ステファヌ・マラルメが1884年以降パリ・ローム街の自宅で開いた「火曜会」(les Mardis)を介して、ヨーロッパ全域に象徴主義詩学を伝播した文化現象。シュテファン・ゲオルゲ（独）、W.B.イェイツ・アーサー・シモンズ（英）、エミール・ヴェルハーレン（白）、メーテルランク（白）、ダリオ（中南米モデルニスモ）が直接・間接に影響を受け、汎ヨーロッパ象徴主義のハブとなった。",
    background="第三共和制パリの文化的中心性と、マラルメの個人的求心力。",
    development="アーサー・シモンズ『文学における象徴主義運動』(1899)が英語圏に総合的紹介を提供し、エリオット・パウンドのモダニズムへ橋渡し。",
    historical_context="19世紀末のパリの国際的文化中心としての役割。",
    primary_source_url=ARTFL,
    primary_source_type="ARTFL Project (U Chicago) Mallarmé corpus",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ロシア象徴主義", name_en="Russian Symbolism",
    name_original="Русский символизм / Russkii simvolizm",
    period_key="世紀末",
    definition="1890年代-1910年代のロシアにおける象徴主義文学運動。第一世代（старшие символисты、ヴァレリー・ブリューソフ、ジナイーダ・ギッピウス、ドミトリー・メレシュコフスキー）と第二世代（младшие символисты、アンドレイ・ベールイ、アレクサンドル・ブローク、ヴャチェスラフ・イワノフ）に分かれ、フランス象徴主義とロシア宗教哲学（ソロヴィヨフ）を融合した独自の宗教的・終末論的色彩を帯びる。",
    background="フランス象徴主義の翻訳受容（ブリューソフ訳ヴェルレーヌ等）と、ウラジーミル・ソロヴィヨフ宗教哲学の影響。",
    development="ベールイ『ペテルブルグ』(1913)、ブローク『十二』(1918)に頂点。アクメイズム（グミリョフ、アフマートワ、マンデリシュターム）・未来派（マヤコフスキー、フレーブニコフ）への対抗として乗り越えられる。",
    historical_context="ロシア帝政末期の宗教的・革命的緊張と、銀の時代(серебряный век)文化の中核。",
    primary_source_url=WIKI_EN+"Russian_symbolism",
    primary_source_type="Wikipedia: Russian symbolism (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ベルギー象徴主義", name_en="Belgian Symbolism",
    name_original="symbolisme belge", period_key="象徴主義期",
    definition="フランス語圏ベルギーを中心とした象徴主義文学運動。エミール・ヴェルハーレン（1855-1916、『触手のある町』1895）、モーリス・メーテルランク（1862-1949）、ジョルジュ・ローデンバック（『死都ブリュージュ』1892）、シャルル・ヴァン・レルベルクが代表。フランス象徴主義の中核地帯のひとつであり、フランドル神秘主義との融合を特徴とする。",
    background="ベルギー独立(1830)後のフランス語文化と、北方カトリック神秘主義（リュースブルック等）の伝統。",
    development="メーテルランクの劇は世界的に普及（ドビュッシー『ペレアスとメリザンド』）し、ベルギー象徴主義は欧州象徴主義の中核に位置付けられた。",
    historical_context="世紀末ベルギーの文化的多元性と、フランス文化への近接性。",
    primary_source_url=WIKI_FR+"Symbolisme_belge",
    primary_source_type="Wikipedia FR: Symbolisme belge",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="クレプスコラーリ", name_en="Crepuscolari",
    name_original="Crepuscolari", period_key="世紀末",
    definition="20世紀初頭イタリアの象徴主義系詩派。「黄昏の詩人たち」(Crepuscolari)の名は批評家ジュゼッペ・アントニオ・ボルジェーゼが1910年に名付けた。グイード・ゴッツァーノ、セルジョ・コラッツィーニ、マリーノ・モレッティが代表。象徴主義的雰囲気と日常的・地方的・抑制された倦怠感を特徴とし、ダヌンツィオの英雄的修辞への反逆として位置付けられる。",
    background="ダヌンツィオの英雄的・装飾的詩風への反動と、フランス世紀末詩（ラフォルグ、サマン）の影響。",
    development="モンターレを介して20世紀イタリア・エルメティスモ（hermetic poetry）詩人ウンガレッティ・モンターレ・クアジモードに継承。",
    historical_context="統一後イタリアの文化的省察期と、ヨーロッパ世紀末文化への参与。",
    primary_source_url=WIKI_EN+"Crepuscolari",
    primary_source_type="Wikipedia: Crepuscolari (academic)",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="カタルーニャ・モデルニズム",
    name_en="Catalan Modernisme",
    name_original="Modernisme català", period_key="世紀末",
    definition="1880年代-1910年代カタルーニャ（バルセロナ中心）の文化運動。ドイツ語「Modernismus」、英語「Aestheticism」、フランス「Art Nouveau」の地域的変奏で、文学（ジョアン・マラガル、サンティアゴ・ルシニョール）・美術（ラモン・カザス、アントニ・ガウディ）・建築・グラフィックを横断した。象徴主義的詩学とカタルーニャ民族復興（Renaixença）が融合する。",
    background="フランス象徴主義・英国唯美主義の地中海的受容と、カタルーニャ民族文化復興運動。",
    development="後の「ノウセンティズム」(Noucentisme, 1906-)に乗り越えられるが、ガウディ建築・カタルーニャ文化アイデンティティの源泉となる。",
    historical_context="スペイン王政復古期(Restauración)におけるカタルーニャ自立志向。",
    primary_source_url=WIKI_EN+"Modernisme",
    primary_source_type="Wikipedia: Modernisme (Catalan, academic)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="世紀末", name_en="fin de siècle",
    name_original="fin de siècle", period_key="世紀末",
    definition="フランス語で「世紀の終わり」を意味し、特に1880-1914年の西欧文化全般の精神的・美学的・社会的雰囲気を指す総合概念。デカダンス、象徴主義、唯美主義、初期モダニズム、文化的疲労感、新しい不安、性別・階級・国家の境界の動揺が複合した、文化史的局面の総称。",
    background="第三共和制安定期フランスの文化的爛熟と、第一次大戦前夜の不安。",
    development="第一次大戦勃発(1914)で終結し、戦後文化（モダニズム高揚期）に乗り越えられる。後の文化史で「ベル・エポック」と並列・対比される鍵概念。",
    historical_context="近代西欧文化の終焉感と新時代待望の交錯期。",
    primary_source_url=WIKI_EN+"Fin_de_si%C3%A8cle",
    primary_source_type="Wikipedia: Fin de siècle (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"フィン・ド・シエクル文化史",
         "description":"カール・ショースキー『世紀末ウィーン』に代表される文化人類学・文化史の対象としての世紀末。"}])

# ============================================================
# D: 主要詩学・批評（8件）
# ============================================================
add(**C, name_ja="象徴主義宣言", name_en="Symbolist Manifesto",
    name_original="Le Symbolisme (Moréas)", period_key="象徴主義期",
    definition="ジャン・モレアス（1856-1910、ギリシア出身パリ在住詩人）が1886年9月18日『フィガロ』紙文芸付録に発表した宣言文「Le Symbolisme」。「象徴主義」(symbolisme)という運動名を初めて公式化し、デカダンスからの分離、原型(prototype)・先験的(primordiale)・暗示(suggestion)を重視する詩学綱領を提示した、運動の自己定義文書。",
    background="1880年代パリの文学雑誌乱立とデカダンス／象徴主義の名称争い。",
    development="モレアス自身は1891年「ロマン派学派」(École romane)を創設し象徴主義から離脱したが、宣言は運動の出発点として残る。",
    historical_context="19世紀末文学運動の自己組織化と命名政治。",
    primary_source_url=WIKI_FR+"Manifeste_du_symbolisme",
    primary_source_type="Wikipedia FR: Manifeste du symbolisme",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="名指さぬ暗示", name_en="suggestion not naming",
    name_original="suggérer, non nommer", period_key="象徴主義期",
    definition="マラルメが「文学の謎について」(1896, 『パン』誌インタビュー)で定式化した象徴主義詩学の中心テーゼ：「対象を指名するのは詩を享受することの四分の三を奪うことだ。それを暗示するのが詩の夢である」(Nommer un objet, c'est supprimer les trois quarts de la jouissance du poème...; le suggérer, voilà le rêve)。詩は対象を直接命名せず、暗示によって読者の想像力を喚起する原理。",
    background="ボードレール照応詩学の継承と、リアリズム的命名詩学への反動。",
    development="20世紀詩学（ヴァレリー、新批評の意味の遅延理論、現代記号学）に継承。",
    historical_context="近代詩における意味伝達モデルの根本的転換。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k71326n",
    primary_source_type="Gallica BnF: Mallarmé 'Divagations' 関連",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="韻文の音楽性", name_en="musicality of verse",
    name_original="musicalité du vers", period_key="象徴主義期",
    definition="詩を意味伝達ではなく音響的・音楽的経験として捉える象徴主義詩学の中心原理。ヴェルレーヌ「詩法」「何より音楽を」、マラルメの「韻文の危機」、ペイターの「すべての芸術は音楽の状態に憧れる」(All art constantly aspires towards the condition of music, 『ルネサンス』1873)を共通の地盤とする。",
    background="ワーグナーのGesamtkunstwerk理論と、19世紀後半の音楽の特権化。",
    development="20世紀現代音楽（ドビュッシー、ラヴェル）と協働し、戦間期モダニズム詩（パウンド、エリオット）の音響的詩観へ継承。",
    historical_context="近代芸術における音楽の最高芸術化。",
    primary_source_url=WIKI_EN+"Symbolism_(arts)",
    primary_source_type="Wikipedia: Symbolism in the arts (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="自由詩の発明", name_en="invention of free verse",
    name_original="invention du vers libre", period_key="象徴主義期",
    definition="フランス語詩における音節定数・押韻規則を破棄し、リズムと長短の自由化を達成した詩形革命。ギュスターヴ・カーン『パレ・ノマード』(1887)序文で公式に「vers libre」(自由詩)の理論を提唱。ジュール・ラフォルグ、エミール・ヴェルハーレンも同時期に独立に実践し、20世紀世界詩の標準形式を準備した。",
    background="ロマン派以降のアレクサンドラン批判と、ホイットマン『草の葉』(1855)の英語圏自由詩の影響。",
    development="エズラ・パウンドのイマジズム、T.S.エリオット、20世紀世界詩の標準形式へ展開。",
    historical_context="近代詩における伝統形式の解体と新形式の創出。",
    primary_source_url=WIKI_EN+"Vers_libre",
    primary_source_type="Wikipedia: Vers libre (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"自由詩の発明は19世紀末の詩的言語の解放であった。AI生成詩が古典韻律を学習・模倣・再構成する現代において、自由詩の「自由」の意味が再考される。AIには「規則の重力」が異なる仕方で働く。",
         "related_ai_phenomenon":"AIによる詩的形式の再構成と自由詩の歴史的意義"}])

add(**C, name_ja="エルメティスモ", name_en="hermetic poetry",
    name_original="ermetismo", period_key="世紀末",
    definition="文字通りには「ヘルメス的詩」、世紀末象徴主義に発し20世紀イタリアで結実する難解・密教的・暗示的詩学。マラルメに源を持ち、フランチェスコ・フローラが1936年の論評でジュゼッペ・ウンガレッティ、エウジェーニオ・モンターレ、サルヴァトーレ・クアジモードの詩を「ermetico」と批判的に呼んだことで運動名となった。",
    background="マラルメ象徴主義の難解性継承と、ファシズム期イタリアの公式雄弁修辞への抵抗。",
    development="モンターレ『骨のセピア』(1925)、ウンガレッティ『悲しみ』(1947)、クアジモード（1959年ノーベル賞）に頂点。",
    historical_context="戦間期イタリアの政治的抑圧下の暗号的詩作。",
    primary_source_url=WIKI_EN+"Hermeticism_(poetry)",
    primary_source_type="Wikipedia: Hermeticism in poetry (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="散文詩", name_en="prose poem",
    name_original="poème en prose", period_key="象徴主義期",
    definition="詩形（行分け・韻律）を放棄しつつ詩的密度を保つ短い散文形式。アロイジウス・ベルトラン『夜のガスパール』(1842、死後出版)が嚆矢。ボードレール『パリの憂愁』(1869、死後出版)で確立し、ランボー『イリュミナシオン』『地獄の季節』、マラルメ『散文詩』、ロートレアモン『マルドロールの歌』に至る象徴主義の中心形式となった。",
    background="ロマン派の長編詩への反動と、近代都市散文経験の詩化。",
    development="20世紀世界詩（フランシス・ポンジュ、シュペルヴィエル、フリオ・コルタサル、ボルヘス）の中心形式の一つとなる。",
    historical_context="散文／韻文の伝統的二分法の解体。",
    primary_source_url=GUTEN+"ebooks/36247",
    primary_source_type="Project Gutenberg: Baudelaire 'Le Spleen de Paris'",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="韻文の危機", name_en="Crisis of Verse",
    name_original="Crise de vers", period_key="象徴主義期",
    definition="マラルメが1895年『ルヴュ・ブランシュ』に発表し『ディヴァガシオン』(1897)に収録した詩学エッセイ。フランス古典韻律の破綻と自由詩の到来を「最近の詩の歴史的危機」として総括し、詩語を日常語の対極に置く「分割としての詩」の理論を提示した、19世紀末詩学最重要文書。",
    background="1880年代以降の自由詩運動（カーン、ラフォルグ）への理論的応答必要性。",
    development="ヴァレリー詩学、新批評の言語論的詩観、20世紀フランス詩学（ボヌフォワ、メショニック）まで継承。",
    historical_context="フランス韻律システムの300年継続後の根本的破綻期。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k71326n",
    primary_source_type="Gallica BnF: Mallarmé 'Divagations' (Crise de vers)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"マラルメが診断した「韻文の危機」は伝統形式の解体だった。AIが大量の韻文を再生成・再構成する現代、第二の「韻文の危機」（生成的危機）が到来しうる。",
         "related_ai_phenomenon":"AI生成詩と詩的形式の第二の危機"}])

add(**C, name_ja="照応の理論", name_en="theory of correspondence",
    name_original="théorie des correspondances", period_key="象徴主義期",
    definition="ボードレール「Correspondances」を出発点として、19世紀末-20世紀初頭に展開された象徴主義詩学・哲学的理論枠組。物質と精神、感覚と意味、ミクロコスモスとマクロコスモスの間に秘密の対応関係があり、詩人はその対応を発見・暗示する者であるとする世界観。スウェーデンボリ、フーリエ、ピエール・ルルーの神秘主義的伝統を継承。",
    background="スウェーデンボリ『天界の秘儀』『天界と地獄』のフランス受容（バルザック、ジェラール・ド・ネルヴァル）。",
    development="20世紀解釈学（ガダマー）、構造主義人類学（レヴィ=ストロースの「冷たい思考」）、エコ詩学まで部分的に継承。",
    historical_context="近代世俗化の中での神秘主義的世界観の文学的延命。",
    primary_source_url=SEP+"swedenborg/",
    primary_source_type="Stanford Encyclopedia: Swedenborg",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

# ============================================================
# E: 隣接運動と継承（8件）
# ============================================================
add(**C, name_ja="ラファエル前派", name_en="Pre-Raphaelitism",
    name_original="Pre-Raphaelite Brotherhood", period_key="ラファエル前派期",
    definition="1848年、ダンテ・ガブリエル・ロセッティ、ウィリアム・ホルマン・ハント、ジョン・エヴァレット・ミレイらがロンドンで結成した英国唯美主義の先駆運動。ラファエロ以前の中世イタリア絵画の精神を範とし、文学（ロセッティ詩、クリスティーナ・ロセッティ、ウィリアム・モリス）と美術を統合した。象徴主義の英語圏先行運動。",
    background="ヴィクトリア朝産業文化への美学的反逆と、中世主義リバイバル（ピュージン、ラスキン）。",
    development="1860年代以降ロセッティ・スウィンバーンを介して唯美主義(Aestheticism)へ展開、ウィリアム・モリスのアーツ・アンド・クラフツ運動、世紀末英国象徴主義に継承。",
    historical_context="ヴィクトリア朝中期英国の文化的自己批判運動。",
    primary_source_url=GUTEN+"ebooks/4011",
    primary_source_type="Project Gutenberg: Rossetti poems / Pre-Raphaelite texts",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ワイルド唯美主義", name_en="Wilde's Aestheticism",
    name_original="Wilde's Aestheticism", period_key="世紀末",
    definition="オスカー・ワイルド（1854-1900）を中心人物とする英国世紀末美学運動。ウォルター・ペイター『ルネサンス』(1873)結語の「経験そのものを目的に燃える」を綱領的根拠とし、「芸術のための芸術」、生の芸術化、人工の自然超越を中心テーゼとした。著作『意向集』(1891)、『ドリアン・グレイの肖像』(1890)、『獄中記』(1905)。",
    background="ペイターのオックスフォード美学、ラファエル前派の延長、フランス唯美主義(ゴーティエ、フロベール)の英国受容。",
    development="ワイルドの裁判(1895)で社会的に挫折するが、世紀末英国象徴主義（イェイツ、シモンズ）、20世紀ブルームズベリー・グループ、現代クィア理論まで継承。",
    historical_context="ヴィクトリア朝末期英国の道徳主義への美学的・性的反逆。",
    primary_source_url=GUTEN+"ebooks/887",
    primary_source_type="Project Gutenberg: Wilde 'Intentions'",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"生の美学",
         "description":"ニーチェ以降の生の美学的肯定の哲学的系譜とワイルド唯美主義の接続。"}])

add(**C, name_ja="デカダンス運動", name_en="Decadence Movement",
    name_original="Decadent Movement", period_key="世紀末",
    definition="1880年代-1900年代に欧米で展開した文学・美術運動で、文明衰退の中の美、人工の自然超越、倒錯的快楽、過剰な装飾性を特徴とする。フランス（ボードレール、ヴェルレーヌ、ユイスマンス、ラフォルグ）に発し、英国（ワイルド、ビアズリー、ダウソン、ライオネル・ジョンソン）、イタリア（ダヌンツィオ）、ロシア（メレシュコフスキー）に拡散。象徴主義と重なるがより自己破壊的・倒錯的。",
    background="第三共和制安定期の文化的疲労意識と、進歩史観への美学的反逆。",
    development="第一次大戦で衰退するが、20世紀のキャンプ美学、ゴス文化、現代クィア・デカダンス（ハーヴェイ・フィースタイン、デレク・ジャーマン）まで継承。",
    historical_context="近代文化の絶頂期の自己疲弊意識。",
    primary_source_url=WIKI_EN+"Decadent_movement",
    primary_source_type="Wikipedia: Decadent movement (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="イエローブック・サークル",
    name_en="Yellow Book circle",
    name_original="The Yellow Book circle", period_key="世紀末",
    definition="1894-97年ロンドンで刊行された季刊文芸誌『ザ・イエロー・ブック』(The Yellow Book)を中心に集まった英国世紀末作家・芸術家集団。編集者ヘンリー・ハーランド、美術編集オーブリー・ビアズリー、寄稿者にマックス・ビアボーム、アーネスト・ダウソン、ライオネル・ジョンソン、ジョン・デイヴィッドソンを含む。フランス世紀末小説『黄表紙本』(yellow book)に題名を取る挑発的色彩。",
    background="ワイルドの『リッピンコッツ』『ペル・メル・マガジン』掲載と、ボドリー・ヘッド出版社（ジョン・レイン）の出版戦略。",
    development="ワイルド裁判(1895)後の保守的反動でビアズリー解任、運動失速。後継誌『サヴォイ』(1896、シモンズ編集)に継承。",
    historical_context="世紀末英国の出版文化と公的道徳の対立。",
    primary_source_url=WIKI_EN+"The_Yellow_Book",
    primary_source_type="Wikipedia: The Yellow Book (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="世紀末演劇", name_en="fin-de-siècle theatre",
    name_original="théâtre fin-de-siècle", period_key="世紀末",
    definition="1880-1914年の世紀末演劇運動の総称。象徴主義劇（メーテルランク、ヴィリエ・ド・リラダン『アクセル』）、自然主義超克（ストリンドベリ後期、イプセン後期『ボルクマン』『建築師ソルネス』）、唯美主義劇（ワイルド『サロメ』1893）、表現主義先駆を含む、近代演劇の象徴主義的革新期。",
    background="自然主義演劇（アントワーヌ自由劇場）への反動と、ワーグナー総合芸術論の演劇化。",
    development="リュニェ=ポー『芸術座』(Théâtre de l'Œuvre, 1893)が象徴主義劇上演拠点となり、後の前衛演劇（アルトー、ベケット、不条理劇）の前史となる。",
    historical_context="近代演劇のリアリズム規範からの離脱期。",
    primary_source_url=WIKI_EN+"Symbolism_(arts)",
    primary_source_type="Wikipedia: Symbolism in the arts (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="モダニズムへの遺産",
    name_en="Symbolist legacy to Modernism",
    name_original="héritage symboliste au modernisme",
    period_key="世紀末",
    definition="象徴主義詩学（暗示、自由詩、純粋詩、共感覚、神話的世界観）が20世紀英米モダニズム（パウンド、エリオット、イェイツ、ジョイス、ヴァレリー）に継承された文化的伝達系譜。アーサー・シモンズ『文学における象徴主義運動』(1899)が直接的橋渡しとなり、エリオットが「私はヴェルレーヌやラフォルグを読まずには詩人になれなかった」と公言する関係。",
    background="マラルメ火曜会のロンドン経由伝播と、世紀末・20世紀初頭の英米作家のパリ留学経験。",
    development="20世紀世界詩学の象徴主義的基盤として、戦間期モダニズム、戦後ニュー・クリティシズム、現代詩理論まで継承。",
    historical_context="フランス象徴主義の英語圏伝達と、20世紀モダニズムの誕生。",
    primary_source_url=GUTEN+"ebooks/55142",
    primary_source_type="Project Gutenberg: Symons 'The Symbolist Movement in Literature'",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"暗示の詩学",
         "description":"詩学DB（PT）の暗示・象徴の詩学概念と象徴主義詩学の系譜的接続。"}])

add(**C, name_ja="イマジズム前史", name_en="Imagism precursor",
    name_original="Imagism precursor", period_key="世紀末",
    definition="1912-17年エズラ・パウンドが主導した英米詩運動「イマジズム」の象徴主義的前史。ヴェルレーヌの音楽的詩観、マラルメの暗示詩学、ラフォルグの自由詩、T.E.ヒュームの「乾いた精緻さ」(dry hardness)詩論を介して、象徴主義の暗示性が「直接的提示」(direct treatment of the thing)に変換される連続性。F.S.フリント、エイミー・ローウェル、H.D.が代表詩人。",
    background="アーサー・シモンズ『文学における象徴主義運動』(1899)とパウンドのロンドン到着(1908)、ヴェルレーヌ・ラフォルグ翻訳活動。",
    development="イマジズムは1917年に運動として終結するが、20世紀英米モダニズム詩、客観派詩、戦後ニュー・アメリカン・ポエトリーまで継承。",
    historical_context="フランス世紀末詩学の英米詩への移植期。",
    primary_source_url=POETRY_FOUND+"learn/glossary-terms/imagism",
    primary_source_type="Poetry Foundation: Imagism (academic glossary)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="オカルト象徴主義", name_en="occult symbolism",
    name_original="symbolisme occulte", period_key="世紀末",
    definition="世紀末象徴主義文学・芸術における神秘主義・神智学・薔薇十字思想・カバラ・タロー・心霊主義の系譜的影響。スウェーデンボリ→エリファス・レヴィ→ヘレナ・ブラヴァツキー神智学(1875-)→黄金の夜明け団(Order of the Golden Dawn, 1888-)→イェイツ・アーサー・マッケン・アレイスター・クロウリーの実践。象徴主義の宗教哲学的基盤。",
    background="19世紀後半の科学的唯物論への対抗としての秘教復興と、東洋宗教の西欧受容。",
    development="20世紀神秘主義文学（イェイツ後期、ジョイス『フィネガンズ・ウェイク』神秘主義要素）、戦後ニュー・エイジ、現代秘教文化に継承。",
    historical_context="近代世俗化の文化的反動としての秘教復興。",
    primary_source_url=WIKI_EN+"Occultism_in_modern_culture",
    primary_source_type="Wikipedia: Occultism in modern culture (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"近代秘教復興",
         "description":"近代宗教人類学（オカルト復興、神智学）と象徴主義の文化的接続。"}])


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
        sf5_count = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id=5"
        ).fetchone()["c"]
        print(f"[c09] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c09] subfield_id=5 cumulative: {sf5_count}")
        print(f"[c09] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
