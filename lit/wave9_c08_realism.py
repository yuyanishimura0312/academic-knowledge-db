"""LIT-DB Phase 2 Wave 9 — C08: European Realism / Naturalism (40 concepts).

Subfield: lit_eu_realism (id=5), region='西欧'.
Sources: Project Gutenberg, HathiTrust, ARTFL/FRANTEXT (where applicable),
plato.stanford.edu, britannica.com, academic-grade Wikipedia (en/fr/de).

Verification policy:
  - 'primary'  -> PD literary text or contemporaneous critical document available online
                  (Project Gutenberg, ARTFL, Wikisource original).
  - 'secondary' -> canonical scholarly synthesis or encyclopedia entry (Britannica,
                   SEP, academic-grade Wikipedia).
  - 'tertiary' -> synthetic/comparative critical category constructed by the
                  contributor for taxonomic completeness.

40 concepts split into five blocks of 8:
  A: French realism (Stendhal, Balzac, Flaubert, Maupassant) — 8
  B: English / American / Northern European realism — 8
  C: Naturalism (French + Anglo-American + German) — 8
  D: Major poetics & critical concepts of realism — 8
  E: Related schools and sub-genres — 8
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


# Periods used by C08. region='西欧' for all.
PERIODS = [
    ("19世紀フランス・リアリズム期", "French Realism (19th c.)", 1830, 1880,
     "ルイ・フィリップ王政期から第三共和制初期にかけてのフランス文学。スタンダール、バルザックを起点に、フローベール、モーパッサンに至るリアリズムの古典的成熟期。"),
    ("19世紀英米・北欧リアリズム期", "British/American/Nordic Realism (19th c.)",
     1840, 1900,
     "ヴィクトリア朝中期以降の英米と北欧におけるリアリズム小説・社会劇の隆盛期。ディケンズ、エリオット、ジェイムズ、ハウエルズ、トウェイン、イプセンを擁する。"),
    ("自然主義期", "Naturalism (late 19th c.)", 1865, 1910,
     "ゾラを中心とするフランス自然主義と、その英米・独語圏への波及期。実験医学・進化論・遺伝決定論を文学に統合した時代。"),
    ("リアリズム理論成熟期", "Mature Realist Poetics", 1850, 1900,
     "リアリズム・自然主義の自己理論化期。ハウエルズ、ジェイムズ、ゾラらによる小説論の確立。"),
]


# Source URL bases (real, verifiable)
GUTEN = "https://www.gutenberg.org/"
HATHI = "https://catalog.hathitrust.org/"
ARTFL = "https://artfl-project.uchicago.edu/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
BRITT = "https://www.britannica.com/"
WSRC_FR = "https://fr.wikisource.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_eu_realism", region="西欧",
         original_script="roman")


# ============================================================
# A: フランス・リアリズム（8件）
# ============================================================
add(**C, name_ja="スタンダール『赤と黒』",
    name_en="Stendhal's Le Rouge et le Noir",
    name_original="Le Rouge et le Noir",
    period_key="19世紀フランス・リアリズム期",
    definition="スタンダール（1783-1842）が1830年に発表した長編小説。王政復古期フランスの社会を背景に、平民出身の青年ジュリアン・ソレルの野心と没落を描く。心理分析と社会観察を統合した方法によって、19世紀フランス・リアリズム小説の出発点を成した作品とされる。",
    background="ナポレオン没落後の王政復古期社会と、平民青年の社会上昇路途断絶という歴史的条件。",
    development="バルザック『人間喜劇』、フローベール『感情教育』に直接先行する心理-社会リアリズムの祖型となった。",
    historical_context="シャルル十世期反動と1830年7月革命前夜の社会的緊張。",
    primary_source_url=GUTEN+"ebooks/798",
    primary_source_type="Project Gutenberg: Le Rouge et le Noir",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バルザック『人間喜劇』",
    name_en="Balzac's La Comédie humaine",
    name_original="La Comédie humaine",
    period_key="19世紀フランス・リアリズム期",
    definition="オノレ・ド・バルザック（1799-1850）が1842年以降統一的構想として組織した、約90編の長編・中編・短編から成る小説連環。同時代フランス社会を「私的生活」「地方生活」「パリ生活」「政治生活」「軍隊生活」「田園生活」の各場面に分類し、社会全体の文学的全集化を試みた。19世紀リアリズム長編形式の規範となった。",
    background="王政復古期・七月王政期フランスの急速な社会変動と、文学による社会総体把握の野心。",
    development="ゾラ『ルーゴン=マッカール叢書』、プルースト『失われた時を求めて』、その他20世紀小説連環の祖型となった。",
    historical_context="七月王政期の産業化・都市化・ブルジョワジー台頭という社会的文脈。",
    primary_source_url=GUTEN+"author/64",
    primary_source_type="Project Gutenberg: Balzac collection",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"社会全体記述",
         "description":"バルザックの社会全集化構想は、19世紀社会観察と人類学的全体記述（ethnography）の文学的並行物として位置づけられる。"}])

add(**C, name_ja="バルザック「人間類型」",
    name_en="Balzac's type humain",
    name_original="type humain",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが『人間喜劇』前書（1842）で表明した文学的方法論。動物学者ジョフロワ・サン=ティレールの「単一構造平面」を範に、社会の中の人間を職業・階層・気質によって分類可能な「類型」として把握する。個別人物造形と社会類型学を統合する19世紀リアリズム人物論の理論的核となった。",
    background="ジョフロワ・サン=ティレール、ビュフォン以来のフランス自然史学的分類思考の文学への移植。",
    development="ゾラ自然主義の遺伝決定論的人物論、ルカーチ『歴史小説論』『リアリズム研究』のリアリズム理論に継承された。",
    historical_context="19世紀前半フランスの社会階層流動化と、社会観察言説の発達。",
    primary_source_url=ARTFL+"databases/efts/PUBLIC/",
    primary_source_type="ARTFL: Avant-propos to La Comédie humaine",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"バルザックの「人間類型」は個別主体を社会的類型に還元する方法論であり、AI時代におけるペルソナ生成・キャラクタープロンプトと理論的に響き合う。生成AIによる類型ベースの人物設定は、バルザック類型論の機械化として再読可能。",
         "related_ai_phenomenon":"LLMによるペルソナ生成・類型ベースキャラクター設計"},
        {"axis":"物語","status":"rethinking",
         "rationale":"類型を物語駆動装置として用いる19世紀リアリズム手法は、AI生成における物語キャラクターの定型化問題と並行する。",
         "related_ai_phenomenon":"AI生成物語のキャラクター類型化"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"人類学的類型論",
         "description":"バルザックの社会類型概念は、19世紀社会観察と人類学的類型論（モーガン、テイラー）と並行する文化分類思考の文学的形式。"}])

add(**C, name_ja="フローベール『ボヴァリー夫人』",
    name_en="Flaubert's Madame Bovary",
    name_original="Madame Bovary",
    period_key="19世紀フランス・リアリズム期",
    definition="ギュスターヴ・フローベール（1821-1880）が1856-57年に発表した長編小説。地方医師夫人エンマ・ボヴァリーの欲望・幻滅・自殺を、徹底した文体的精錬と「非個人性（impassibilité）」を以て描く。リアリズム小説の方法的範型として、19世紀世界文学の決定的事件となった。1857年の風俗紊乱裁判で起訴され、無罪判決を獲得した。",
    background="第二帝政期フランスの地方ブルジョワ社会と、ロマン主義的感性の文学的批判。",
    development="モーパッサン、ゾラ、ジェイムズ、プルースト、ジョイスに直接的影響を与え、20世紀モダニズム小説の文体論的基盤となった。",
    historical_context="第二帝政期の検閲・道徳裁判文化と、文学の自律性論議の歴史的瞬間。",
    primary_source_url=GUTEN+"ebooks/14155",
    primary_source_type="Project Gutenberg: Madame Bovary (FR)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="フローベール「正確な言葉（le mot juste）」",
    name_en="Flaubert's le mot juste",
    name_original="le mot juste",
    period_key="19世紀フランス・リアリズム期",
    definition="フローベールが書簡（特にルイーズ・コレ宛）で繰り返し主張した文体論的理念。ある内容を表現するのに「正確な唯一の言葉」が存在するという信念で、文体的選択の極限的精錬を要求する。19世紀リアリズム文体論の頂点を成し、20世紀モダニズム作家（ジェイムズ、ジョイス、パウンド、ヘミングウェイ）に継承された。",
    background="フローベールの修道院的執筆実践（『ボヴァリー夫人』に5年）と、19世紀フランス文体論の精緻化。",
    development="ヘンリー・ジェイムズの文体論、エズラ・パウンドのイマジズム、ヘミングウェイの「氷山理論」に直接影響を与えた。",
    historical_context="19世紀フランス文学言語の規範化と、文体的自意識の高度化。",
    primary_source_url=GUTEN+"ebooks/28178",
    primary_source_type="Project Gutenberg: Flaubert Correspondance",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"「正確な唯一の言葉」というフローベール的理念は、LLMが確率的に「次の言葉」を選択する生成原理と根本的に対立する。AI生成の確率的多義性と、リアリズム的精確性理念の緊張関係を理論化する古典的参照点として再読される。",
         "related_ai_phenomenon":"LLMの確率的生成 vs 精確言語理念の緊張"}])

add(**C, name_ja="フローベール「非個人性（impassibilité）」",
    name_en="Flaubert's impassibilité",
    name_original="impassibilité",
    period_key="19世紀フランス・リアリズム期",
    definition="フローベールが提唱した小説作家の方法論的態度。「作家は自身の作品の中に、宇宙における神のように、いたるところに在りつつどこにも姿を見せてはならない」（書簡 1852年12月）に集約される、感情的同一化・道徳的判断を排した観察的記述の理念。リアリズム作家の客観的距離概念の祖型。",
    background="19世紀科学的観察精神（クロード・ベルナール実験医学等）の文学への浸透。",
    development="モーパッサン、ゾラ、フランス自然主義に継承され、ジェイムズ「点視野（point of view）」論の前提条件となった。",
    historical_context="19世紀フランスにおける文学の自律性主張と、作家の制度的位置の確立。",
    primary_source_url=GUTEN+"ebooks/28178",
    primary_source_type="Project Gutenberg: Flaubert Correspondance",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"フローベールの非個人性理念は、作家主体の意図・感情を作品から消去する技法を理論化する。これは作家主体不在で生成されるAIテキストの構造と類比的であり、AI時代の作家性を再考する古典的参照点。",
         "related_ai_phenomenon":"AI生成における作家主体不在の構造"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"非個人性が獲得する「客観的真正性」は、AI生成テキストが模倣する「中立的観察」の文学的祖型。AI時代における客観性の真正性問題を再検討する基準。",
         "related_ai_phenomenon":"AI生成テキストの中立性・客観性主張"}])

add(**C, name_ja="フローベールの自由間接話法",
    name_en="free indirect discourse in Flaubert",
    name_original="style indirect libre",
    period_key="19世紀フランス・リアリズム期",
    definition="『ボヴァリー夫人』を通じてフローベールが体系的に展開した語りの技法。三人称の地の文に登場人物の意識・声を直接話法の引用符号なく溶け込ませる方法で、語り手と人物意識の境界を意図的に曖昧化する。19世紀リアリズム小説の方法的革新の中心であり、20世紀モダニズム小説（ジェイムズ、ジョイス、ウルフ）の心理表現の祖型となった。",
    background="19世紀フランス散文における語りの技法の精緻化と、心理リアリズムへの志向。",
    development="ジェイムズ点視野論、ジョイス『ユリシーズ』、ウルフ意識流に直接展開し、20世紀ナラトロジー（バンフィルド、コーン）の中心研究対象となった。",
    historical_context="19世紀後半の文学的自意識の高度化と、語りの技法的革新期。",
    primary_source_url=WIKI_EN+"Free_indirect_speech",
    primary_source_type="Wikipedia: Free indirect speech",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"自由間接話法は語り手の声と人物の声の融合を技法化する。LLMの生成において複数の声・観点が混淆する現象は、自由間接話法の機械化として理論化可能。",
         "related_ai_phenomenon":"LLM生成における複数視点の混淆"},
        {"axis":"主体","status":"rethinking",
         "rationale":"自由間接話法は語り主体と人物主体の境界の解体を文学的に達成する技法。AI生成における主体境界の流動化を理論化する古典的祖型。",
         "related_ai_phenomenon":"AI生成における主体境界の流動化"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"自由間接話法・物語論",
         "description":"自由間接話法はナラトロジー（バンフィルド、コーン、ジュネット）の中心研究対象であり、リアリズム詩学の方法的核を成す。"}])

add(**C, name_ja="モーパッサン短編形式",
    name_en="Maupassant short story form",
    name_original="conte / nouvelle",
    period_key="19世紀フランス・リアリズム期",
    definition="ギ・ド・モーパッサン（1850-1893）が1880年代に確立したフランス短編小説の規範形式。フローベールに師事した文体的精錬を基盤に、簡潔な観察、効果的な結末、抑制された道徳判断を統合し、19世紀フランス短編小説の頂点を成した。300編余りの短編で、リアリズムの精密さと自然主義的観察を融合した。",
    background="フローベール直系の文体修練と、1880年代フランス雑誌文化（『ル・ゴーロワ』『ジル・ブラース』）における短編需要。",
    development="チェーホフ、O・ヘンリー、サマセット・モームを経て、20世紀世界短編小説の規範形式となった。",
    historical_context="第三共和制初期の出版文化と、雑誌・新聞媒体における短編形式の経済的成熟。",
    primary_source_url=GUTEN+"author/119",
    primary_source_type="Project Gutenberg: Maupassant collection",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# B: 英米・北欧リアリズム（8件）
# ============================================================
add(**C, name_ja="ディケンズ『荒涼館』",
    name_en="Dickens's Bleak House",
    name_original="Bleak House",
    period_key="19世紀英米・北欧リアリズム期",
    definition="チャールズ・ディケンズ（1812-1870）が1852-53年に発表した長編小説。チャンスリー裁判所の永続的訴訟を中核に、ヴィクトリア朝ロンドンの法・階級・貧困・伝染病を描き出す。複数の語り（三人称現在形と一人称回顧）の併用、社会全体の網状的把握、霧の象徴主義によって、19世紀英国リアリズムの頂点を成した。",
    background="ヴィクトリア朝中期の都市化・産業化と、法制度・公衆衛生改革論議。",
    development="ジョージ・エリオット、トーマス・ハーディ、後の英米モダニズム長編形式（ジョイス、ウルフ）に深い影響を与えた。",
    historical_context="1850年代英国の社会改革論議（公衆衛生法1848、衡平法改革）。",
    primary_source_url=GUTEN+"ebooks/1023",
    primary_source_type="Project Gutenberg: Bleak House",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジョージ・エリオット『ミドルマーチ』",
    name_en="George Eliot's Middlemarch",
    name_original="Middlemarch",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ジョージ・エリオット（メアリー・アン・エヴァンズ、1819-1880）が1871-72年に発表した長編小説。1830年前後のイングランド地方都市を舞台に、ドロシア・ブルックを中心とする複数の人物の生・思想・結婚を、心理的精緻さと社会的分析を統合して描く。F・R・リーヴィスは『偉大な伝統』(1948)で「英国小説中最高峰」と評価した。",
    background="ヴィクトリア朝中期の女性教育論・宗教論・科学論の総合的反映。",
    development="ヘンリー・ジェイムズ、ヴァージニア・ウルフ、F・R・リーヴィスのリアリズム評価軸の中心作品となった。",
    historical_context="1832年第一次選挙法改正前夜の社会と、1870年代の女性高等教育問題（ガートン・カレッジ設立1869）。",
    primary_source_url=GUTEN+"ebooks/145",
    primary_source_type="Project Gutenberg: Middlemarch",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="トルストイ的リアリズム",
    name_en="Tolstoyan realism",
    name_original="толстовский реализм",
    period_key="19世紀英米・北欧リアリズム期",
    definition="レフ・トルストイ（1828-1910）が『戦争と平和』『アンナ・カレーニナ』に確立したリアリズムの様式。心理的内面描写・社会的全体把握・歴史哲学的思索を統合し、独白的（ホモフォニック）統一視点のもとに巨大な世界像を構築する。フローベール的非個人性とは対極の、作者道徳的判断を内蔵したリアリズムとして、19世紀世界リアリズムの一極を成す。",
    background="ロシア19世紀リアリズムの伝統と、トルストイ独自の歴史哲学・宗教思想。",
    development="ヘンリー・ジェイムズ「ゆるい大袋（loose baggy monsters）」批評、バフチン独白的小説論、20世紀世界文学への深い影響。",
    historical_context="ロシア大改革期と、世界文学的承認の獲得期。",
    primary_source_url=GUTEN+"ebooks/2600",
    primary_source_type="Project Gutenberg: War and Peace",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"独白的小説とリアリズム",
         "description":"トルストイ的独白型リアリズムはバフチンによってドストエフスキー的ポリフォニーの対比軸として理論化された。"}])

add(**C, name_ja="ヘンリー・ジェイムズ「小説の技法」",
    name_en="Henry James's The Art of Fiction",
    name_original="The Art of Fiction",
    period_key="リアリズム理論成熟期",
    definition="ヘンリー・ジェイムズ（1843-1916）が1884年に発表したエッセイ。ウォルター・ベザント講演への応答として書かれ、小説を芸術として理論化した英語圏初期の体系的小説論。「小説は人生の直接的印象（direct impression of life）」「経験は無限に大きな感受性」と説き、英語圏小説論の出発点となった。",
    background="フローベールおよびフランス・リアリズムの英米受容、19世紀末英語圏文学批評の専門化。",
    development="後の小説論（パーシー・ラボック『小説の技術』1921、ウェイン・ブース『小説の修辞学』1961）に継承された。",
    historical_context="19世紀末英米における大衆小説と「芸術小説」の分離、文学批評の専門学術化。",
    primary_source_url=GUTEN+"ebooks/41719",
    primary_source_type="Project Gutenberg: The Art of Fiction",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ヘンリー・ジェイムズ「視点（point of view）」",
    name_en="Henry James's point of view",
    name_original="point of view",
    period_key="リアリズム理論成熟期",
    definition="ヘンリー・ジェイムズが小説論および後年の『ニューヨーク版』序文（1907-09）で展開した語りの技法理論。物語を特定の中心意識（central consciousness）の限定的視野から提示する技法を意味し、フローベール的非個人性を英語圏小説に適用した。20世紀英米小説論の中心概念となった。",
    background="フローベール非個人性理念のジェイムズによる吸収・体系化と、19世紀末英米小説の方法的洗練。",
    development="パーシー・ラボック『小説の技術』(1921)が体系化し、ウェイン・ブース、ジェラール・ジュネット、20世紀ナラトロジーの基本枠組みとなった。",
    historical_context="19世紀末から20世紀初頭の小説論の専門学術化期。",
    primary_source_url=GUTEN+"author/113",
    primary_source_type="Project Gutenberg: Henry James prefaces",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ジェイムズの中心意識・限定視点の理論は、神視点と対照的な「制限された主体的視点」を技法化する。AI生成テキストにおける視点設定（system promptによる視点制御）の文学理論的祖型として再読される。",
         "related_ai_phenomenon":"LLMによる視点制御・パースペクティブ設定"},
        {"axis":"主体","status":"rethinking",
         "rationale":"特定の意識を介在させる語りの技法は、AI生成における擬似的主体の構築と理論的に共振する。",
         "related_ai_phenomenon":"AI生成における擬似的中心意識の構築"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"焦点化・視点理論",
         "description":"ジェイムズの視点論はジュネットの焦点化（focalisation）理論の歴史的祖型をなす、現代物語論の中心源流。"}])

add(**C, name_ja="トウェイン口語的リアリズム",
    name_en="Twain's vernacular realism",
    name_original="vernacular realism",
    period_key="19世紀英米・北欧リアリズム期",
    definition="マーク・トウェイン（サミュエル・クレメンス、1835-1910）が『ハックルベリー・フィンの冒険』(1884-85)に確立した、米国南部・中西部口語を地の文に取り込むリアリズム様式。アーネスト・ヘミングウェイは「すべての近代米国文学はマーク・トウェイン『ハック・フィン』に始まる」と述べた。米国文学のヨーロッパ伝統からの分離と、口語ナラティブの規範確立を意味する。",
    background="米国南部・中西部の口語伝統、19世紀末米国文学の独立志向。",
    development="ヘミングウェイ、フォークナー、サリンジャー、20世紀米国口語ナラティブの祖型となった。",
    historical_context="再建期(Reconstruction)後の米国における人種・地域・口語をめぐる文学的論議。",
    primary_source_url=GUTEN+"ebooks/76",
    primary_source_type="Project Gutenberg: Adventures of Huckleberry Finn",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ハウエルズ・リアリズム原理",
    name_en="Howells's realist principles",
    name_original="Howells's realism",
    period_key="リアリズム理論成熟期",
    definition="ウィリアム・ディーン・ハウエルズ（1837-1920）が『ハーパーズ・マンスリー』連載コラム「Editor's Study」(1886-92)および『批評と小説』(1891)に展開した米国リアリズム理論。「正直で公平な真実の表現」を中心理念に、ロマン主義的虚飾・センセーショナリズムを批判し、米国中産階級日常生活の倫理的描写を提唱した。米国リアリズム運動の制度的中心。",
    background="米国南北戦争後の出版文化興隆と、ヨーロッパ・リアリズムの選択的受容。",
    development="ヘンリー・ジェイムズ、フランク・ノリス、後の米国自然主義への橋渡しとなった。",
    historical_context="再建期からアメリカン・センチュリー初頭にかけての米国文学制度確立期。",
    primary_source_url=GUTEN+"ebooks/3377",
    primary_source_type="Project Gutenberg: Criticism and Fiction",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イプセン社会劇",
    name_en="Ibsen's social drama",
    name_original="samtidsdrama",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ヘンリック・イプセン（1828-1906）が1877年『社会の柱』以降確立した近代社会問題劇。『人形の家』(1879)、『幽霊』(1881)、『民衆の敵』(1882)等で、女性解放・遺伝・公共良心・科学的真実といった同時代社会問題を、緻密な現実主義的舞台空間と「過去の漸次的暴露」構造で展開し、近代演劇の方法的革新を達成した。",
    background="北欧の自由主義・女性解放運動、ダーヴィン進化論受容、ノルウェー国民国家形成。",
    development="ジョージ・バーナード・ショウ『イプセン主義の本質』(1891)以降、英国・米国・ドイツの近代演劇に決定的影響を与えた。",
    historical_context="1879年『人形の家』結末（ノラの家出）が引き起こした全欧的社会論議と、女性解放問題の文学化。",
    primary_source_url=GUTEN+"author/124",
    primary_source_type="Project Gutenberg: Ibsen collection",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# C: 自然主義（8件）
# ============================================================
add(**C, name_ja="ゾラ「実験小説論」",
    name_en="Zola's Le Roman expérimental",
    name_original="Le Roman expérimental",
    period_key="自然主義期",
    definition="エミール・ゾラ（1840-1902）が1880年に発表した自然主義文学綱領。クロード・ベルナール『実験医学序説』(1865)を直接の範として、小説を「実験的観察」「決定論的法則の検証装置」と理論化した。文学を実験科学的方法に近づけることで、ロマン主義的想像力・主観性を排する自然主義の方法論的支柱となった。",
    background="ベルナール実験医学、テーヌ環境決定論、ダーウィン進化論の文学への統合。",
    development="フランス自然主義（モーパッサン、ユイスマンス、セアール、メダンの夕べ）、英米自然主義（ノリス、ドライサー、クレイン）、ドイツ自然主義（ハウプトマン、ホルツ）の理論的基盤となった。",
    historical_context="第三共和制期フランスの世俗化・科学主義興隆と、文学の自律的方法論確立期。",
    primary_source_url=GUTEN+"ebooks/16793",
    primary_source_type="Project Gutenberg: Le Roman expérimental",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ゾラ『ルーゴン=マッカール叢書』",
    name_en="Zola's Les Rougon-Macquart",
    name_original="Les Rougon-Macquart",
    period_key="自然主義期",
    definition="ゾラが1871-93年に発表した20巻の小説連環。「第二帝政下のある一族の自然と社会の歴史」を副題とし、ルーゴン家とマッカール家の遺伝形質が世代を超えて社会階層を貫通していく構造を、決定論的フレームの中で展開した。バルザック『人間喜劇』に対する自然主義的応答であり、フランス自然主義の中心作品。",
    background="バルザック『人間喜劇』への意識、テーヌの「人種・環境・時代」三要因論、メンデル遺伝法則以前の遺伝決定論。",
    development="20世紀の家族長編連環（マン『ブッデンブローク家』、ガルシア・マルケス『百年の孤独』、フォークナー・ヨクナパトーファ・サーガ）に深い影響を与えた。",
    historical_context="第二帝政期フランス社会の文学的全体像化と、第三共和制初期の社会批判。",
    primary_source_url=GUTEN+"author/26",
    primary_source_type="Project Gutenberg: Émile Zola collection",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="自然主義的遺伝決定論",
    name_en="naturalist genetic determinism",
    name_original="naturalisme génétique",
    period_key="自然主義期",
    definition="フランス自然主義（特にゾラ）の中核教説。人間性格・運命を遺伝形質と環境による決定論的産物として把握する文学的立場。プロスペル・リュカ『自然遺伝についての哲学的・生理学的論』(1847-50)等の19世紀医学的遺伝論を文学に統合し、自由意志・道徳判断を背後に退かせるリアリズムの極限形態を成した。",
    background="19世紀フランス医学（ベルナール、リュカ）の遺伝・神経・気質論と、テーヌ批評理論。",
    development="ノリス『マクティーグ』、ドライサー、ハーディ後期長編、20世紀英米自然主義の中心教説となった。",
    historical_context="19世紀後半ヨーロッパにおける生物学的決定論思考の社会科学・人文学への浸透。",
    primary_source_url=WIKI_EN+"Naturalism_(literature)",
    primary_source_type="Wikipedia: Naturalism (literature)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"自然主義的遺伝決定論は人間主体を生物学的・環境的決定の産物として把握する。AI時代において、主体を学習データとアルゴリズムの決定論的産物と見る視座と理論的に並行する。",
         "related_ai_phenomenon":"AIにおける主体性のアルゴリズム的決定論"}])

add(**C, name_ja="フランク・ノリス",
    name_en="Frank Norris",
    name_original="Frank Norris",
    period_key="自然主義期",
    definition="フランク・ノリス（1870-1902）は米国自然主義の代表的作家。『マクティーグ』(1899)、『オクトパス』(1901)、『穴（The Pit）』(1903、遺作)で、サンフランシスコ移民労働者の没落・カリフォルニア小麦農家と鉄道資本の闘争・シカゴ穀物投機を、ゾラ的決定論フレームで描いた。米国自然主義の制度的成立を象徴する。",
    background="ゾラ・自然主義の米国受容と、19世紀末米国の経済資本主義・労働問題の文学化。",
    development="ドライサー、シンクレア、ロンドンを経て、1930年代米国社会派長編小説（スタインベック『怒りの葡萄』）に継承された。",
    historical_context="米国「金ぴか時代」末期から「進歩主義時代」初期の社会変動と、独占資本主義批判文学。",
    primary_source_url=GUTEN+"author/39",
    primary_source_type="Project Gutenberg: Frank Norris collection",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シオドア・ドライサー",
    name_en="Theodore Dreiser",
    name_original="Theodore Dreiser",
    period_key="自然主義期",
    definition="シオドア・ドライサー（1871-1945）は米国自然主義の代表的長編作家。『シスター・キャリー』(1900)、『ジェニー・ガーハート』(1911)、『アメリカの悲劇』(1925)で、米国都市中下層の人物が社会的・経済的力に翻弄される様を、装飾を排した重厚な散文で描いた。米国リアリズム・自然主義の頂点として20世紀米国文学に深い影響を与えた。",
    background="米国移民第二世代の経済的苦難体験、19世紀末米国都市社会のジャーナリスティック観察、ハーバート・スペンサー社会進化論受容。",
    development="シンクレア・ルイス、フィッツジェラルド、ジョン・ドス・パソスの方法的祖型となり、1930年米国人初のノーベル文学賞受賞者ルイスは受賞演説でドライサーを最重要先行者と讃えた。",
    historical_context="進歩主義時代から狂騒の20年代、大恐慌期の米国社会の文学的反映。",
    primary_source_url=GUTEN+"ebooks/233",
    primary_source_type="Project Gutenberg: Sister Carrie",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スティーヴン・クレイン『赤い武勲章』",
    name_en="Stephen Crane's The Red Badge of Courage",
    name_original="The Red Badge of Courage",
    period_key="自然主義期",
    definition="スティーヴン・クレイン（1871-1900）が1895年に発表した長編小説。米国南北戦争を、戦闘経験のない若い兵士ヘンリー・フレミングの限定的意識から描き、戦争英雄主義を解体した。印象主義的描写・心理的内省・限定視点を統合した方法は、フランス自然主義と並行しつつ、米国モダニズムへの橋渡しとなった。",
    background="米国南北戦争30年後の歴史的距離、フランス自然主義および印象主義絵画の受容、米国ジャーナリズム文化。",
    development="ヘミングウェイ『武器よさらば』、フォークナー、20世紀米国戦争文学の方法的祖型となった。",
    historical_context="1890年代米国における南北戦争記憶の文学的再構成と、ヴェテラン世代の死を見越したジャーナリスティック歴史化。",
    primary_source_url=GUTEN+"ebooks/73",
    primary_source_type="Project Gutenberg: The Red Badge of Courage",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハウプトマン自然主義劇",
    name_en="Hauptmann's naturalist drama",
    name_original="naturalistisches Drama",
    period_key="自然主義期",
    definition="ゲルハルト・ハウプトマン（1862-1946）が『日の出前』(1889)、『織工』(1892)で確立したドイツ自然主義劇。ホルツ・シュラフ「秒様式（Sekundenstil）」（時間の精密記述）、方言の舞台導入、社会階層の決定論的描写によって、ドイツ近代演劇の方法的革新を達成した。1912年ノーベル文学賞受賞。",
    background="ベルリン「自由舞台（Freie Bühne）」設立(1889)、フランス自然主義およびイプセン受容、シレジア織工蜂起(1844)の歴史的記憶。",
    development="ブレヒト叙事的演劇への系譜的影響、20世紀ドイツ社会派演劇の祖型となった。",
    historical_context="ヴィルヘルム期ドイツの社会民主主義興隆、1890年「社会主義者鎮圧法」失効後の左派文化高揚期。",
    primary_source_url=GUTEN+"author/445",
    primary_source_type="Project Gutenberg: Hauptmann collection",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="モーパッサンの自然主義",
    name_en="Maupassant's naturalism",
    name_original="naturalisme de Maupassant",
    period_key="自然主義期",
    definition="モーパッサンがゾラ編『メダンの夕べ』(1880)所収「脂肪の塊」以降に展開した自然主義的方法。フローベール直系の文体精錬を保持しつつ、ゾラの遺伝・環境決定論を取り込んだ。ノルマンディー農民・パリ官吏・娼婦の生を、感情的同一化を排した観察的散文で描き、フランス自然主義短編の規範となった。",
    background="フローベール文体修練とゾラ自然主義綱領の総合、メダン文学集団の活動。",
    development="チェーホフ短編、20世紀世界短編小説の決定的範型となった。",
    historical_context="第三共和制初期フランスの自然主義論争期と、雑誌・新聞媒体の短編需要興隆。",
    primary_source_url=GUTEN+"ebooks/3090",
    primary_source_type="Project Gutenberg: Boule de Suif",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: 主要詩学・批評概念（8件）
# ============================================================
add(**C, name_ja="リアリズム教説（19世紀中葉）",
    name_en="realism doctrine (mid-19th c.)",
    name_original="réalisme",
    period_key="リアリズム理論成熟期",
    definition="1850年代フランスにおいて、シャンフルーリ（ジュール・フルーリ=ユッソン）、デュランティ、画家クールベを中心に体系化された文学的・芸術的教説。雑誌『レアリスム』(1856-57)を機関紙とし、同時代の物質的・社会的現実の正確な観察的記述を芸術の中心使命と主張した。19世紀中葉の文学・美術リアリズム運動の理論的中核。",
    background="1855年クールベ「リアリズム宣言」展、1850年代フランス第二帝政期の社会変動と芸術論争。",
    development="フローベール、ゾラ、自然主義への橋渡しとなり、世界各国のリアリズム運動の理論的源流となった。",
    historical_context="第二帝政期フランスの芸術論争と、ロマン主義・新古典主義への対抗運動として成立。",
    primary_source_url=BRITT+"art/Realism-art",
    primary_source_type="Britannica: Realism (art)",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="生活の一断面（tranche de vie）",
    name_en="slice of life / tranche de vie",
    name_original="tranche de vie",
    period_key="自然主義期",
    definition="ジャン・ジュリアン（劇作家）が1888年に提唱したフランス自然主義劇の中心理念。劇作品を「生活から切り取られた一片」として呈示すべきとし、伝統的劇構成（発端・展開・葛藤・解決）を排する。19世紀末フランス自由舞台運動（アントワーヌ）の方法的支柱となり、20世紀演劇・映画・小説の構成論に深い影響を与えた。",
    background="自由舞台（Théâtre Libre, 1887）設立とフランス自然主義劇の制度的興隆。",
    development="チェーホフ後期戯曲、20世紀リアリズム劇・モダニズム劇の構成原理に継承された。映画における「ヌーヴェル・ヴァーグ」の脱劇構成にも継承。",
    historical_context="19世紀末パリ実験劇場運動と、伝統的劇構造への対抗。",
    primary_source_url=WIKI_EN+"Slice_of_life",
    primary_source_type="Wikipedia: Slice of life",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI生成リアリズムの構成論",
         "description":"「生活の一断面」概念は、AI生成テキスト・映像が伝統的物語構成を欠いたまま「現実断片」として呈示される現象を理論化する古典的参照点となる。"}])

add(**C, name_ja="観察方法",
    name_en="observation method",
    name_original="méthode d'observation",
    period_key="リアリズム理論成熟期",
    definition="19世紀リアリズム・自然主義作家が共有した方法論的核。ゾラの実験医学的観察、フローベールの取材ノート、モーパッサンのノルマンディー観察記録、バルザックの社会類型観察に代表される、現実への直接的観察を文学の前提とする態度。リアリズム作家を以前のロマン主義作家と区別する制度的方法論となった。",
    background="19世紀フランス科学的観察精神（ベルナール、テーヌ）の文学への浸透。",
    development="20世紀ジャーナリスティック・ノンフィクション（ヘミングウェイ、トルーマン・カポーティ『冷血』）、ニュージャーナリズム、ドキュメンタリー文学の方法的祖型となった。",
    historical_context="19世紀フランス・ヨーロッパにおける文学の自律的方法論確立期。",
    primary_source_url=GUTEN+"ebooks/16793",
    primary_source_type="Project Gutenberg: Le Roman expérimental",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="類型と人物（type vs character）",
    name_en="type vs character",
    name_original="type contre caractère",
    period_key="リアリズム理論成熟期",
    definition="リアリズム文学批評の中心論争。人物造形が社会的・歴史的「類型（type）」として機能する側面と、個別具体的「人物（character）」として機能する側面の関係を巡る議論。ルカーチ『歴史小説論』(1937)、『リアリズム研究』(1948)で理論化され、リアリズム評価の中心軸（バルザック・トルストイ vs ゾラ自然主義）となった。",
    background="バルザック類型論、19世紀ドイツ・ヘーゲル左派の社会論、20世紀ルカーチ・マルクス主義文学理論。",
    development="ルカーチ的「典型（typische Figur）」概念は20世紀社会主義リアリズム理論の中心となり、また英米『新批評』の人物論（フォースター『小説の側面』ラウンド／フラット人物論）と対比的に展開した。",
    historical_context="19世紀リアリズム作品評価の理論的整理と、20世紀マルクス主義文学理論の成立。",
    primary_source_url=WIKI_EN+"György_Lukács",
    primary_source_type="Wikipedia: Lukács / typical character",
    importance_score=4, source_tier="tertiary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"類型・典型と人物造形",
         "description":"類型／人物の対比は、リアリズム詩学の中心的人物論枠組みであり、現代物語論にも継承される。"}])

add(**C, name_ja="社会的記録としての小説",
    name_en="novel as social document",
    name_original="le roman comme document social",
    period_key="リアリズム理論成熟期",
    definition="19世紀リアリズム・自然主義の中核理念。小説を同時代社会の正確な記録・証言・分析として位置づけ、文学に社会学的・歴史的・人類学的価値を要求する立場。バルザック『人間喜劇』前書、ゾラ序文、ハウエルズ批評に通底する理念で、文学と社会科学の境界が未分化であった19世紀の文学観を象徴する。",
    background="19世紀社会観察文学（パリ生理学的スケッチ、ロンドン都市探訪記等）と、社会科学黎明期の文学への影響。",
    development="20世紀ドキュメンタリー文学、社会派ジャーナリズム、ノンフィクション小説、現代の社会派長編小説に継承された。",
    historical_context="19世紀における社会学・人類学・歴史学の制度化以前の、文学による社会総体把握への文化的需要。",
    primary_source_url=BRITT+"art/realism-literature",
    primary_source_type="Britannica: Realism (literature)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"小説が社会記録として機能するという理念は、AIが生成可能になった「事実っぽいフィクション」「擬似的ドキュメンタリー」と緊張関係に立つ。AI時代における社会的記録性の真正性を再考する古典的参照点。",
         "related_ai_phenomenon":"AI生成擬似ドキュメンタリーと真正性問題"},
        {"axis":"受容","status":"rethinking",
         "rationale":"小説を社会記録として受容する読者契約は、AI生成テキストの社会的記録としての受容可能性を理論的に問い直す枠組み。",
         "related_ai_phenomenon":"AI生成テキストの社会記録としての受容"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"民族誌と文学",
         "description":"小説の社会記録機能は人類学的民族誌（ethnography）の文学的並行物であり、19世紀社会観察言説の双子をなす。"}])

add(**C, name_ja="成熟した全知の語り手",
    name_en="omniscient narrator (mature)",
    name_original="narrateur omniscient",
    period_key="リアリズム理論成熟期",
    definition="19世紀リアリズム小説（バルザック、ディケンズ、エリオット、トルストイ）に共有された、社会・歴史・心理の全領域を見通す全知的語り手。神視点として小説世界を統御し、人物・社会・思想に対し権威的判断を下す。フローベール非個人性以降のリアリズム諸方法とともに、リアリズム期の語りの主要形式の一極を成した。",
    background="18世紀小説（フィールディング、ディドロ）からの継承と、19世紀リアリズムによる体系的精緻化。",
    development="フローベール非個人性、ジェイムズ点視点論によって相対化され、20世紀モダニズム小説で意識流・自由間接話法に置換された。",
    historical_context="19世紀の「神は死んだ」(ニーチェ1882)以前の世界観と、文学的全知視点との一致。",
    primary_source_url=WIKI_EN+"Narration#Omniscient",
    primary_source_type="Wikipedia: Narration / omniscient",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"19世紀リアリズムの全知の語り手は神的・統一的視点を文学的に体現する。LLMが「全データから生成する」擬似全知性と、19世紀全知性の歴史的構造を比較理論化する基準点。",
         "related_ai_phenomenon":"LLMの擬似全知性と神視点の歴史的比較"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"焦点化ゼロ・全知視点",
         "description":"全知の語り手はジュネット焦点化理論の「焦点化ゼロ（focalisation zéro）」に対応し、ナラトロジーの基本範疇となる。"}])

add(**C, name_ja="自由間接話法の理論化",
    name_en="free indirect style theorized",
    name_original="style indirect libre théorisé",
    period_key="リアリズム理論成熟期",
    definition="シャルル・バイイ（言語学者）が1912年論文「フランス語における自由間接話法」で命名・分析し、20世紀ナラトロジー（バンフィルド『話されざる文章』1982、ドリット・コーン『透明な精神』1978、ジュネット『物語のディスクール』1972）が体系化した、19世紀リアリズム小説の語りの技法理論。フローベール『ボヴァリー夫人』を主要範例とする。",
    background="19世紀リアリズム小説の語り技法を、20世紀言語学・ナラトロジーが遡及的に理論化した過程。",
    development="20世紀後半のナラトロジー、認知物語論、現代英米小説論の中心研究対象となった。",
    historical_context="19世紀リアリズム実践と20世紀文学理論の理論的接続点。",
    primary_source_url=WIKI_EN+"Free_indirect_speech",
    primary_source_type="Wikipedia: Free indirect speech (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"自由間接話法・物語論",
         "description":"自由間接話法理論はナラトロジーの中心研究対象であり、リアリズム詩学と現代物語論の接続点。"}])

add(**C, name_ja="物語的共感",
    name_en="narrative empathy",
    name_original="empathie narrative",
    period_key="リアリズム理論成熟期",
    definition="19世紀リアリズム小説が読者と人物の間に組織する感情的同一化の構造。ジョージ・エリオット『アダム・ビード』エッセイ、ヘンリー・ジェイムズ『小説の技法』、後にスーザン・キーン『共感とノヴェル』(2007)などで理論化された。リアリズムの倫理的機能（他者理解の拡大）を支える方法論的基盤として、リアリズム評価の中心軸の一つとなった。",
    background="18世紀ヒューム道徳哲学の同情論、19世紀ロマン主義感情論のリアリズムへの統合。",
    development="20世紀英米『道徳的批評』(F.R.リーヴィス、ライオネル・トリリング)、現代の認知文学研究、共感のニューロサイエンス研究と接続した。",
    historical_context="19世紀ヴィクトリア朝の道徳的市民社会形成と、文学による道徳的想像力涵養の理念。",
    primary_source_url=WIKI_EN+"Narrative_empathy",
    primary_source_type="Wikipedia: Narrative empathy",
    importance_score=3, source_tier="tertiary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"物語的共感はリアリズム小説の倫理的中核機能であり、AI生成テキストが「人物への共感」を呼び起こせるか、その共感に倫理的価値があるかという、AI時代の文学倫理問題の理論的基盤となる。",
         "related_ai_phenomenon":"AI生成キャラクターへの共感の倫理性"}])


# ============================================================
# E: 関連流派・運動（8件）
# ============================================================
add(**C, name_ja="フランス・リアリズム派",
    name_en="French realism school",
    name_original="école réaliste",
    period_key="19世紀フランス・リアリズム期",
    definition="1850年代パリにおいて、シャンフルーリ、デュランティ、画家クールベを中心に結集した文学・芸術運動。雑誌『レアリスム』(1856-57)を機関紙とし、ロマン主義・新古典主義への対抗として、同時代の物質的・社会的現実の観察的描写を綱領とした。フローベール・ゾラ以前のリアリズム運動の制度的中核を成す。",
    background="1855年クールベ独立展示（パリ万国博覧会脇でのリアリズム宣言展）、第二帝政期の芸術論争。",
    development="フローベール、ゾラ、自然主義に橋渡しされ、19世紀後半の世界的リアリズム運動の理論的源流となった。",
    historical_context="第二帝政期のサロン芸術・アカデミー権威への反抗と、芸術の現代化論議。",
    primary_source_url=BRITT+"art/Realism-art",
    primary_source_type="Britannica: Realism (art)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="米国地方主義（リージョナリズム）",
    name_en="American regionalism",
    name_original="American regionalism",
    period_key="19世紀英米・北欧リアリズム期",
    definition="米国南北戦争後に隆盛した、特定地方の風土・習俗・口語を中核とする文学運動。ニューイングランドのサラ・オーン・ジュエット『深い樅の村』(1896)、南部のチャールズ・チェスナット、メアリー・N・マーフリー、西部のブレット・ハートを代表的作家とする。「ローカル・カラー（local color）」運動とも呼ばれ、米国国民国家形成期の文学的多様化を象徴する。",
    background="再建期米国の地域的アイデンティティの再編、雑誌文化の興隆と地域取材文学への需要。",
    development="ウィラ・キャザー、フォークナー、20世紀米国南部・西部小説に継承された。",
    historical_context="再建期から進歩主義時代の米国における、国家統合と地域多様化の緊張関係。",
    primary_source_url=WIKI_EN+"Regionalism_(art)#Regionalism_in_literature",
    primary_source_type="Wikipedia: Regionalism (literature)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="社会小説",
    name_en="social novel",
    name_original="social novel",
    period_key="19世紀英米・北欧リアリズム期",
    definition="同時代社会の階層問題・労働問題・都市問題を中心テーマとする19世紀小説サブジャンル。エリザベス・ガスケル『メアリー・バートン』(1848)、ディケンズ『ハード・タイムズ』(1854)、ディズレーリ『シビル』(1845)、フランスのウジェーヌ・スー『パリの秘密』(1842-43)を代表とする。リアリズム文学の社会批判機能の集約形態。",
    background="1830-40年代英国・フランスの産業化進展と、労働運動・社会主義運動の興隆。",
    development="ゾラ自然主義、ロシア・ナロードニチェストヴォ文学、20世紀社会派長編小説への系譜的橋渡しとなった。",
    historical_context="チャーチスト運動(1838-58)、フランス1848年革命前夜の社会的緊張。",
    primary_source_url=WIKI_EN+"Social_novel",
    primary_source_type="Wikipedia: Social novel",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="問題小説",
    name_en="problem novel",
    name_original="Tendenzroman",
    period_key="19世紀英米・北欧リアリズム期",
    definition="特定の社会問題（女性の地位、結婚制度、宗教の権威、労働、人種等）を中心テーマとして焦点化する19世紀末リアリズム小説サブジャンル。トマス・ハーディ『ジュード・オブスキュア』(1895)、メレディス『エゴイスト』(1879)、グラント・アレン『無罪の女』(1895)等を代表とする。後期ヴィクトリア朝の社会改革論議の文学的形式。",
    background="後期ヴィクトリア朝の女性問題・結婚問題・宗教論議、フェミニスト運動初期の興隆。",
    development="20世紀の社会派長編、フェミニズム小説、現代の「主題小説」への祖型となった。",
    historical_context="1870-90年代英国の社会改革立法（既婚女性財産法1882等）と、文学による社会問題化。",
    primary_source_url=WIKI_EN+"Problem_novel",
    primary_source_type="Wikipedia: Problem novel",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="英国状況小説（condition-of-England novel）",
    name_en="condition-of-England novel",
    name_original="condition-of-England novel",
    period_key="19世紀英米・北欧リアリズム期",
    definition="トマス・カーライル『チャーティズム』(1839)が提起した「英国状況の問題」に応答した1840-50年代英国小説のサブジャンル。ディズレーリ『シビル、または二つの国民』(1845)、ガスケル『メアリー・バートン』(1848)、『北と南』(1854-55)、ディケンズ『ハード・タイムズ』(1854)、キングズリー『酵母』(1848)を代表とする。産業化下の英国社会の階層分裂を主題化した。",
    background="1830-40年代英国産業化進展、チャーチスト運動、1840年代「飢餓の40年代（hungry forties）」。",
    development="後期ヴィクトリア朝社会小説、20世紀英国社会派長編（オーウェル）に継承された。",
    historical_context="1832年第一次選挙法改正後の社会的緊張と、産業資本主義への文学的応答。",
    primary_source_url=WIKI_EN+"Condition_of_England_question",
    primary_source_type="Wikipedia: Condition-of-England question",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="マックレイキング文学",
    name_en="muckraking literature",
    name_original="muckraking",
    period_key="自然主義期",
    definition="米国進歩主義時代(1900-1914頃)に隆盛した、独占企業・政治腐敗・社会問題を暴露する調査ジャーナリズム文学。アプトン・シンクレア『ジャングル』(1906、シカゴ食肉産業の暴露)、アイダ・ターベル『スタンダード・オイル史』(1904)、リンカーン・ステフェンズ『都市の恥辱』(1904)を代表とする。米国自然主義の社会派的延長として位置づけられる。",
    background="米国「金ぴか時代」の独占資本主義批判、進歩主義運動の高揚、雑誌『マクルアーズ』『コリアーズ』のジャーナリスティック機能拡大。",
    development="シンクレア『ジャングル』が連邦食品医薬品法(1906)制定の契機となり、20世紀調査ジャーナリズムと社会派文学の祖型となった。",
    historical_context="セオドア・ローズベルト大統領期(1901-1909)の改革政治、独占禁止法強化期。",
    primary_source_url=GUTEN+"ebooks/140",
    primary_source_type="Project Gutenberg: The Jungle (Sinclair)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="姦通小説",
    name_en="novel of adultery",
    name_original="novel of adultery",
    period_key="19世紀英米・北欧リアリズム期",
    definition="フローベール『ボヴァリー夫人』(1856-57)、トルストイ『アンナ・カレーニナ』(1873-77)、フォンターネ『エフィ・ブリースト』(1894-95)、エサ・デ・ケイロス『バジリオの従兄』(1878)、レオポルド・アラス『ラ・レヘンタ』(1884-85)を中核とする19世紀リアリズム小説のサブジャンル。ブルジョワ結婚制度と女性の欲望の衝突を、ヒロインの社会的破滅として展開する物語類型。",
    background="19世紀ヨーロッパのブルジョワ結婚制度確立と、それと衝突する女性の欲望・社会的孤立の文学的問題化。",
    development="トニー・タナー『姦通と小説』(1979)、レイチェル・ブラウンスタイン『ヒロインを読む』等の比較文学研究の中心対象となった。",
    historical_context="19世紀ヨーロッパ各国のブルジョワ家族制度確立期、女性財産法・離婚法論議。",
    primary_source_url=WIKI_EN+"Adultery_in_fiction",
    primary_source_type="Wikipedia: Adultery in fiction (academic)",
    importance_score=4, source_tier="tertiary", canonical_in_region="major")

add(**C, name_ja="幻滅の小説",
    name_en="novel of disillusionment",
    name_original="Desillusionsroman",
    period_key="19世紀英米・北欧リアリズム期",
    definition="主人公の青年期理想・希望が社会的経験を通じて段階的に解体されていく構造を持つ19世紀リアリズム小説のサブジャンル。フローベール『感情教育』(1869)、バルザック『幻滅』(1837-43)、ハーディ『ジュード・オブスキュア』(1895)、ゴンチャロフ『オブローモフ』(1859)を代表とする。ルカーチ『小説の理論』(1916)が「幻滅の小説（Roman der Desillusion）」として理論化した。",
    background="19世紀ヨーロッパ・ブルジョワ社会における青年知識人の社会的位置喪失と、ロマン主義的理想主義への文学的反省。",
    development="20世紀モダニズム長編（プルースト、マン『魔の山』）、戦後米国小説（フィッツジェラルド『グレート・ギャツビー』）の物語構造に継承された。",
    historical_context="19世紀ヨーロッパの世代論的社会変動と、青年期文学テーマの哲学的深化。",
    primary_source_url=WIKI_EN+"György_Lukács#The_Theory_of_the_Novel",
    primary_source_type="Wikipedia: Lukács Theory of the Novel",
    importance_score=4, source_tier="tertiary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"幻滅の小説・教養小説論",
         "description":"幻滅の小説はルカーチ『小説の理論』の中心類型であり、教養小説（Bildungsroman）論と並ぶ19世紀小説論の中核枠組み。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        # Create periods
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="西欧",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid

        # Insert concepts
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
        print(f"[c08] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c08] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
