"""LIT-DB Phase 2 Wave 15 — C10: European Modernism (+40 retry).

Subfield: lit_eu_modernism (id=6), region='西欧'.
Adds 40 new concepts on top of existing 80, focusing on:
  A: Joyce deepening (Dubliners stories, Portrait, Ulysses episodes, Wake) — 14
  B: Proust deepening (7 volumes, episodes) — 9
  C: Mann (5)
  D: Kafka (5)
  E: Woolf (4)
  F: Faulkner (3)
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("モダニズム期", "Modernism", 1890, 1945,
     "ジョイス、プルースト、マン、カフカ、ウルフらヨーロッパ高地モダニズム期。"),
    ("後期モダニズム期", "Late Modernism", 1945, 1965,
     "戦後モダニズム後期。"),
]


GUTEN = "https://www.gutenberg.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WSRC_FR = "https://fr.wikisource.org/wiki/"
WSRC_DE = "https://de.wikisource.org/wiki/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_eu_modernism", region="西欧", original_script="roman")


# ============================================================
# A: Joyce deepening (14)
# ============================================================
add(**C, name_ja="ジョイス『ダブリン市民』「姉妹」",
    name_en="Joyce's Dubliners: The Sisters",
    name_original="The Sisters",
    period_key="モダニズム期",
    definition="ジェイムズ・ジョイス（1882-1941）が1914年刊『ダブリン市民』冒頭に置いた短編。少年が司祭フリン神父の死を告げられる物語で、麻痺(paralysis)・霊性的腐敗のテーマを冒頭に提示し、ダブリン民衆の心理的閉塞のジョイス的診断を開く。",
    background="20世紀初頭ダブリンのカトリック社会と少年期視点の文学化。",
    development="モダニズム短編形式・エピファニー詩学の出発点として20世紀短編研究の中心となった。",
    historical_context="1900年代アイルランドの文化的閉塞期。",
    primary_source_url=GUTEN+"ebooks/2814",
    primary_source_type="Project Gutenberg: Dubliners",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョイス『ダブリン市民』「アラビー」",
    name_en="Joyce's Dubliners: Araby",
    name_original="Araby",
    period_key="モダニズム期",
    definition="『ダブリン市民』第3短編。少年がマンガン姉への憧れからアラビー市場へ向かうが、世俗的失望に至る物語。少年期の幻想と幻滅のエピファニー構造を確立し、20世紀短編形式の規範例として広く教材化された。",
    background="19世紀末ダブリンの東方主義的バザール文化、少年期心理の文学化。",
    development="エピファニー短編形式の祖型、20世紀英米短編教育の中核作品。",
    historical_context="1894年ダブリン・アラビー慈善市の文化的記憶。",
    primary_source_url=GUTEN+"ebooks/2814",
    primary_source_type="Project Gutenberg: Dubliners",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジョイス『ダブリン市民』「エヴリン」",
    name_en="Joyce's Dubliners: Eveline",
    name_original="Eveline",
    period_key="モダニズム期",
    definition="『ダブリン市民』第4短編。19歳の娘エヴリンが恋人フランクとブエノスアイレスへ駆け落ちしようとするが、最後の瞬間に動けなくなる物語。麻痺の主題を女性主体において結晶化し、ジョイス的決断不能のエピファニーを示す。",
    background="20世紀初頭アイルランド女性の社会的閉塞、家父長制下の主体形成。",
    development="ジェンダー研究、ポストコロニアル批評の中心テクストとなった。",
    historical_context="20世紀初頭アイルランド・ナショナリズム期の女性問題。",
    primary_source_url=GUTEN+"ebooks/2814",
    primary_source_type="Project Gutenberg: Dubliners",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョイス『ダブリン市民』「死せる人々」",
    name_en="Joyce's Dubliners: The Dead",
    name_original="The Dead",
    period_key="モダニズム期",
    definition="『ダブリン市民』終結の中編（1914）。クリスマス会後、ゲイブリエル・コンロイが妻グレタの過去の恋人マイケル・フューリーの死を知り、生者と死者の境界が溶ける雪景色のエピファニーで終わる。20世紀英文学短編の最高峰の一つとされ、エリオット、フォークナーらに深い影響を与えた。",
    background="20世紀初頭ダブリン中産階級の文化儀礼と過去の文学化。",
    development="ジョン・ヒューストン映画化(1987)等を経て20世紀文化の古典となった。",
    historical_context="エドワード朝期アイルランドの文化的記憶。",
    primary_source_url=GUTEN+"ebooks/2814",
    primary_source_type="Project Gutenberg: Dubliners",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"生者と死者の境界が溶融する終結エピファニーは、AI環境における過去・記憶・死者の再構成可能性と理論的に共振する。",
         "related_ai_phenomenon":"AI環境における死者・過去の記憶再構成"}])

add(**C, name_ja="ジョイス『若き芸術家の肖像』",
    name_en="Joyce's A Portrait of the Artist as a Young Man",
    name_original="A Portrait of the Artist as a Young Man",
    period_key="モダニズム期",
    definition="ジョイスが1916年に発表した長編小説。スティーヴン・ディーダラスの幼少期から大学卒業までの精神的形成（Bildung）を、各年齢段階の言語意識で記述する自伝的成長小説。自由間接話法と意識の流れの実験で、20世紀モダニズム成長小説の祖型を成した。",
    background="ジョイス自身のダブリン青年期、20世紀初頭アイルランド・カトリック教育・大学制度。",
    development="ペーター『マリウス』を継承し、ウルフ、フォークナー、20世紀世界の自伝的小説の規範となった。",
    historical_context="20世紀初頭アイルランド・ナショナリズム・カトリック文化の文学的批判期。",
    primary_source_url=GUTEN+"ebooks/4217",
    primary_source_type="Project Gutenberg: Portrait",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジョイス『ユリシーズ』テレマコス挿話",
    name_en="Joyce's Ulysses: Telemachus",
    name_original="Telemachus (Ulysses Episode 1)",
    period_key="モダニズム期",
    definition="『ユリシーズ』第1挿話（1922）。マーテロ塔でのスティーヴン・ディーダラスとマリガン、ハインズの朝の場面。ホメロス『オデュッセイア』テレマコスに対応し、子の父探しの主題を提示する。文体「物語的（若き）」、舞台時刻午前8時。",
    background="1904年6月16日ダブリンの実時間構造、ホメロス対応の構築原理。",
    development="20世紀世界文学の最重要古典の冒頭として、無数の批評・注解が蓄積した。",
    historical_context="20世紀初頭ダブリンの植民地的文化情勢。",
    primary_source_url=GUTEN+"ebooks/4300",
    primary_source_type="Project Gutenberg: Ulysses",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジョイス『ユリシーズ』カリュプソ挿話",
    name_en="Joyce's Ulysses: Calypso",
    name_original="Calypso (Ulysses Episode 4)",
    period_key="モダニズム期",
    definition="『ユリシーズ』第4挿話。レオポルド・ブルームの最初の登場場面。エクルズ街7番地で妻モリーへの朝食準備、屋外での腎臓買い物等を描く。ホメロス対応はカリュプソ島、文体「物語的（成熟）」、時刻午前8時。ブルームの日常的身体性のジョイス的肖像化。",
    background="20世紀初頭ダブリンのユダヤ系市民生活、家庭的身体性の文学化。",
    development="モダニズム小説における日常的身体性記述の規範例となった。",
    historical_context="20世紀初頭ダブリンの多文化的市民社会。",
    primary_source_url=GUTEN+"ebooks/4300",
    primary_source_type="Project Gutenberg: Ulysses",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョイス『ユリシーズ』ハデス挿話",
    name_en="Joyce's Ulysses: Hades",
    name_original="Hades (Ulysses Episode 6)",
    period_key="モダニズム期",
    definition="『ユリシーズ』第6挿話。ブルームら4人がパディ・ディグナムの葬儀のためグラスネヴィン墓地へ向かう。ホメロス対応は冥界下り、文体「内臓的（incubism）」、時刻午前11時。ブルームの父の自殺記憶・息子ルーディの死など死の主題が交差する。",
    background="ダブリンの葬儀文化、ブルーム家の喪失体験の文学化。",
    development="20世紀文学における死・喪・葬礼描写の規範的長編場面となった。",
    historical_context="20世紀初頭ダブリンのカトリック・ユダヤ的死生観交差。",
    primary_source_url=GUTEN+"ebooks/4300",
    primary_source_type="Project Gutenberg: Ulysses",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョイス『ユリシーズ』食人鬼挿話",
    name_en="Joyce's Ulysses: Lestrygonians",
    name_original="Lestrygonians (Ulysses Episode 8)",
    period_key="モダニズム期",
    definition="『ユリシーズ』第8挿話。ブルームの昼食場面。バートン・レストランの食事光景に嫌悪し、デイヴィ・バーン酒場でゴルゴンゾーラ・サンドイッチとブルゴーニュを摂る。ホメロス対応は食人巨人、文体「蠕動的（peristaltic）」、時刻午後1時。食欲・身体性のモダニスト記述の規範例。",
    background="20世紀初頭ダブリンの飲食文化、身体的時間性の文学化。",
    development="モダニズム小説における身体的時間記述の規範例となった。",
    historical_context="20世紀初頭ダブリンの市民的食文化。",
    primary_source_url=GUTEN+"ebooks/4300",
    primary_source_type="Project Gutenberg: Ulysses",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ジョイス『ユリシーズ』セイレーン挿話",
    name_en="Joyce's Ulysses: Sirens",
    name_original="Sirens (Ulysses Episode 11)",
    period_key="モダニズム期",
    definition="『ユリシーズ』第11挿話。オーモンド・ホテル酒場での音楽場面。ブルームが妻モリーと愛人ボイランの密会時刻を意識しつつ食事する。ホメロス対応はセイレーン、文体「フーガ風（fuga per canonem）」、時刻午後4時。文学言語の音楽化のジョイス的実験の頂点。",
    background="20世紀初頭ダブリンのアイルランド民謡・サロン音楽文化。",
    development="モダニズム文学言語の音楽性の規範例となった。",
    historical_context="20世紀初頭ダブリンの音楽文化。",
    primary_source_url=GUTEN+"ebooks/4300",
    primary_source_type="Project Gutenberg: Ulysses",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"言語の音楽化・フーガ的構造化の実験は、AI生成における言語の構造的・音楽的生成可能性と理論的に共振する。",
         "related_ai_phenomenon":"AI生成における言語の音楽的・構造的生成"}])

add(**C, name_ja="ジョイス『ユリシーズ』キュクロプス挿話",
    name_en="Joyce's Ulysses: Cyclops",
    name_original="Cyclops (Ulysses Episode 12)",
    period_key="モダニズム期",
    definition="『ユリシーズ』第12挿話。バーニー・キアナン酒場での「市民」(the Citizen)とブルームの対立場面。アイルランド・ナショナリズムと反ユダヤ主義の文学的批判。ホメロス対応は単眼巨人、文体「巨大化的(gigantism)」の連続パロディ。20世紀ナショナリズム批評の文学的範型。",
    background="20世紀初頭アイルランド・ナショナリズム運動の排他的側面、ヨーロッパ反ユダヤ主義。",
    development="ポストコロニアル批評・ナショナリズム研究の中心テクストとなった。",
    historical_context="20世紀初頭アイルランド・ゲール語復興運動期。",
    primary_source_url=GUTEN+"ebooks/4300",
    primary_source_type="Project Gutenberg: Ulysses",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"ナショナリズム的単眼性の文学的批判は、AI時代のフィルターバブル・偏向情報環境批判の祖型として理論的に再読される。",
         "related_ai_phenomenon":"AI環境におけるフィルターバブル・単眼性"}])

add(**C, name_ja="ジョイス『ユリシーズ』ロータスの実挿話",
    name_en="Joyce's Ulysses: Lotus Eaters",
    name_original="Lotus Eaters (Ulysses Episode 5)",
    period_key="モダニズム期",
    definition="『ユリシーズ』第5挿話。ブルームが郵便局で愛人マーサからの手紙を受け取り、教会に立ち寄り、トルコ風呂に向かう場面。ホメロス対応は忘却の蓮の実、文体「麻薬的(narcissism)」、時刻午前10時。日常的逃避と忘却の主題のジョイス的記述。",
    background="20世紀初頭ダブリンの郵便文化・宗教儀礼・浴場文化。",
    development="モダニズム文学における日常的逃避・薬物的状態記述の規範例となった。",
    historical_context="20世紀初頭ダブリンの市民的儀礼文化。",
    primary_source_url=GUTEN+"ebooks/4300",
    primary_source_type="Project Gutenberg: Ulysses",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ジョイス『フィネガンズ・ウェイク』構造",
    name_en="Joyce's Finnegans Wake structure",
    name_original="Finnegans Wake structure",
    period_key="モダニズム期",
    definition="ジョイス最後の作品（1939）の構造原理。ヴィーコ歴史循環論（神時代→英雄時代→人間時代→ricorso）の4部構造、HCEとALPの家族構造、夢言語による多言語ポートマント語の重層化。20世紀文学の最も実験的テクストとして言語学・文化研究の中心研究対象。",
    background="ジョイスの晩年17年の創作集中、ヴィーコ歴史哲学・ブルーノ対立的同一性哲学の継承。",
    development="ポスト構造主義（デリダ、ラカン、エコ）、計算機文学研究、AI言語研究の中心研究対象となった。",
    historical_context="第一次大戦後ヨーロッパの言語・歴史哲学的危機期。",
    primary_source_url=WIKI_EN+"Finnegans_Wake",
    primary_source_type="Wikipedia: Finnegans Wake",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"多言語ポートマント語による夢言語実験は、多言語LLMの言語混合的生成と理論的に共振する20世紀文学の極限点。",
         "related_ai_phenomenon":"多言語LLMにおける言語混合的生成"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"集合的夢の語り構造は、AI生成における集合的・非人称的著作の祖型として理論化されうる。",
         "related_ai_phenomenon":"AI生成における集合的・非人称的著作"}])

add(**C, name_ja="ジョイス『ダブリン市民』「出会い」",
    name_en="Joyce's Dubliners: An Encounter",
    name_original="An Encounter",
    period_key="モダニズム期",
    definition="『ダブリン市民』第2短編。少年二人が学校をさぼってダブリン東部を放浪し、奇妙な老人と出会う物語。少年期の冒険的逃走と性的脅威の遭遇、麻痺の継承的構造をエピファニー形式で結晶化する。",
    background="20世紀初頭ダブリンの少年文化、児童期の性的危機の文学化。",
    development="20世紀児童期文学・心理小説研究の中心テクストとなった。",
    historical_context="20世紀初頭ダブリン市民社会の少年文化。",
    primary_source_url=GUTEN+"ebooks/2814",
    primary_source_type="Project Gutenberg: Dubliners",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# B: Proust deepening (9)
# ============================================================
add(**C, name_ja="プルースト『スワン家の方へ』",
    name_en="Proust's Du côté de chez Swann",
    name_original="Du côté de chez Swann",
    period_key="モダニズム期",
    definition="マルセル・プルースト（1871-1922）『失われた時を求めて』第1巻（1913）。コンブレー幼少期、スワンの恋（オデット）、ジルベルトへの少年期愛を描く。マドレーヌ挿話・無意識的記憶論・ヴィントゥイユのソナタを導入し、20世紀回想小説の祖型を確立した。",
    background="ベル・エポック期パリのサロン文化、ベルクソン哲学的記憶論の文学化。",
    development="20世紀世界の回想小説・心理小説の最重要規範となった。",
    historical_context="第三共和制期フランスの社会的記憶文化。",
    primary_source_url=WSRC_FR+"Du_côté_de_chez_Swann",
    primary_source_type="Wikisource: Du côté de chez Swann",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="プルースト『花咲く乙女たちのかげに』",
    name_en="Proust's À l'ombre des jeunes filles en fleurs",
    name_original="À l'ombre des jeunes filles en fleurs",
    period_key="モダニズム期",
    definition="『失われた時を求めて』第2巻（1919、ゴンクール賞受賞）。バルベック海岸でのアルベルティーヌら少女集団との出会い、エルスティールとの邂逅。少年期から青年期への精神的移行と、芸術家エルスティールを介した美的覚醒の主題を展開する。",
    background="ノルマンディー海岸リゾート文化、ベル・エポック期青少年文化。",
    development="20世紀青年期成長小説・芸術家小説の規範作品となった。",
    historical_context="第三共和制期フランスのリゾート文化。",
    primary_source_url=WSRC_FR+"À_l’ombre_des_jeunes_filles_en_fleurs",
    primary_source_type="Wikisource: A l'ombre",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="プルースト『ゲルマントの方』",
    name_en="Proust's Le Côté de Guermantes",
    name_original="Le Côté de Guermantes",
    period_key="モダニズム期",
    definition="『失われた時を求めて』第3巻（1920-21）。語り手のパリ・ゲルマント公爵夫妻邸への社交的進入と、祖母の死を描く。フランス貴族サロンの精緻な社会学的観察と、ドレフュス事件期の社会的亀裂をモダニスト的フォーマットで描出する。",
    background="ベル・エポック期パリ貴族サロン文化、ドレフュス事件の社会的記憶。",
    development="20世紀貴族サロン研究・社会学的小説研究の中心テクスト。",
    historical_context="ドレフュス事件後フランス第三共和制期の社会的緊張。",
    primary_source_url=WSRC_FR+"Le_Côté_de_Guermantes",
    primary_source_type="Wikisource: Côté de Guermantes",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="プルースト『ソドムとゴモラ』",
    name_en="Proust's Sodome et Gomorrhe",
    name_original="Sodome et Gomorrhe",
    period_key="モダニズム期",
    definition="『失われた時を求めて』第4巻（1921-22）。シャルリュス男爵とジュピアン仕立屋のホモセクシュアル的邂逅冒頭、アルベルティーヌの同性愛疑惑、ヴェルデュラン・サロンの社会動学を描く。20世紀同性愛文学の最重要古典として、クィア研究の中心テクストとなった。",
    background="ベル・エポック期フランスの同性愛文化と社会的隠蔽。",
    development="20世紀クィア批評・ジェンダー研究の中心研究対象。",
    historical_context="第三共和制期フランスのジェンダー・性的規範論議。",
    primary_source_url=WSRC_FR+"Sodome_et_Gomorrhe",
    primary_source_type="Wikisource: Sodome et Gomorrhe",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"性的アイデンティティの隠蔽・複数性の文学化は、AI時代のアイデンティティの可塑性・複数主体問題と理論的に響き合う。",
         "related_ai_phenomenon":"AI環境におけるアイデンティティの複数性・可塑性"}])

add(**C, name_ja="プルースト『囚われの女』",
    name_en="Proust's La Prisonnière",
    name_original="La Prisonnière",
    period_key="モダニズム期",
    definition="『失われた時を求めて』第5巻（1923死後出版）。語り手のパリ・アパルトマン内へのアルベルティーヌ監禁同居生活と、嫉妬と所有欲の精神病理学的解剖。20世紀嫉妬文学・恋愛心理学の最重要文献。",
    background="ベル・エポック期パリのブルジョワ家庭文化、嫉妬と監禁愛の文学化。",
    development="20世紀心理小説、ジェンダー研究の中心テクスト。",
    historical_context="第一次大戦期フランスの心理学的危機表現。",
    primary_source_url=WSRC_FR+"La_Prisonnière",
    primary_source_type="Wikisource: La Prisonnière",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="プルースト『消え去ったアルベルティーヌ』",
    name_en="Proust's Albertine disparue",
    name_original="Albertine disparue",
    period_key="モダニズム期",
    definition="『失われた時を求めて』第6巻（1925死後出版）。アルベルティーヌの逃亡・死と、語り手の喪と忘却の心理学。最も実験的な記憶・喪心理学的章として、20世紀喪研究（フロイト『喪とメランコリー』）と並行する文学的探究を提示する。",
    background="第一次大戦期フランスの喪文化、フロイト喪理論の文学的並行。",
    development="20世紀喪研究・心理小説の中心テクストとなった。",
    historical_context="第一次大戦後フランスの大量喪文化。",
    primary_source_url=WSRC_FR+"Albertine_disparue",
    primary_source_type="Wikisource: Albertine disparue",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="プルースト『見出された時』",
    name_en="Proust's Le Temps retrouvé",
    name_original="Le Temps retrouvé",
    period_key="モダニズム期",
    definition="『失われた時を求めて』終巻（1927死後出版）。第一次大戦中のパリと、ゲルマント大公邸での「マチネ」場面で、不揃いな敷石・スプーンの音などからの無意識的記憶連鎖が記憶の救済をもたらし、語り手が小説執筆の決意に至る。20世紀文学最大の終結章。",
    background="第一次大戦後フランスの記憶文化、プルースト晩年の総合化意識。",
    development="20世紀文学・哲学（ベルクソン、ドゥルーズ）の最重要研究対象。",
    historical_context="第一次大戦後フランスの記憶・救済論議。",
    primary_source_url=WSRC_FR+"Le_Temps_retrouvé",
    primary_source_type="Wikisource: Le Temps retrouvé",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"無意識的記憶による主体の時間横断的統合は、AI環境における記憶の機械的再構成・主体的連続性問題と理論的に共振する。",
         "related_ai_phenomenon":"AI環境における記憶再構成と主体連続性"}])

add(**C, name_ja="プルーストのコンブレー",
    name_en="Proust's Combray section",
    name_original="Combray",
    period_key="モダニズム期",
    definition="『スワン家の方へ』第1部「コンブレー」。語り手の幼少期の田舎町コンブレーでの記憶世界。マドレーヌ挿話による無意識的記憶の発動、スワン家の方とゲルマントの方の二つの散歩道、母の就寝の口づけの主題を導入する。プルースト世界の祖型構造。",
    background="プルースト自身のイリエ＝コンブレー幼少期の記憶。",
    development="20世紀回想小説・幼少期記憶文学の規範例として、ベルクソン記憶哲学の文学的典型。",
    historical_context="第三共和制期フランス田舎町文化。",
    primary_source_url=WSRC_FR+"Du_côté_de_chez_Swann/Combray",
    primary_source_type="Wikisource: Combray",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="プルーストのプチット・マドレーヌ",
    name_en="Proust's petite madeleine",
    name_original="petite madeleine",
    period_key="モダニズム期",
    definition="『スワン家の方へ』「コンブレー」中の有名な挿話。紅茶に浸したマドレーヌ菓子の味から無意識的記憶（mémoire involontaire）が発動し、コンブレー幼少期世界が全面的に蘇生する。20世紀無意識的記憶論・感覚的記憶研究の最重要文学的範型。",
    background="ベルクソン的時間哲学の文学化、プルースト自身の感覚的記憶体験。",
    development="20世紀記憶哲学（ベルクソン、リクール）、神経科学（プルースト効果）の中心参照点。",
    historical_context="第三共和制期フランスの感覚論・記憶論議。",
    primary_source_url=WSRC_FR+"Du_côté_de_chez_Swann/Combray",
    primary_source_type="Wikisource: Combray (madeleine)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"感覚的契機からの記憶蘇生メカニズムは、AI記憶検索・関連連鎖との対比で読み直されるべき近代主体記憶の祖型。",
         "related_ai_phenomenon":"AI記憶検索における感覚的・連鎖的想起"}])


# ============================================================
# C: Mann (5)
# ============================================================
add(**C, name_ja="マン『ブッデンブローク家の人々』",
    name_en="Mann's Buddenbrooks",
    name_original="Buddenbrooks: Verfall einer Familie",
    period_key="モダニズム期",
    definition="トーマス・マン（1875-1955）が1901年に発表した長編小説。北ドイツ・リューベックの商家ブッデンブローク家四世代の没落を描く。19世紀リアリズムの遺産とモダニズム的精神病理学（ニーチェ、ショーペンハウアー、ヴァーグナー受容）を融合し、1929年マンのノーベル賞受賞理由となった。",
    background="ハンザ都市ブルジョワジーの没落、世紀転換期ドイツ家族文化の文学化。",
    development="20世紀家族小説・没落小説の規範作品となった。",
    historical_context="ヴィルヘルム期ドイツのブルジョワ文化危機。",
    primary_source_url=GUTEN+"ebooks/27059",
    primary_source_type="Project Gutenberg: Buddenbrooks",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マン『魔の山』",
    name_en="Mann's Der Zauberberg",
    name_original="Der Zauberberg",
    period_key="モダニズム期",
    definition="トーマス・マンが1924年に発表した長編小説。スイス・ダボスのサナトリウムで7年間過ごす青年ハンス・カストルプを主人公に、第一次大戦前夜ヨーロッパの精神的閉塞をセテムブリーニ・ナフタら教師人物の論争で象徴的に縮図化する。20世紀教養小説の頂点。",
    background="マン自身の妻のサナトリウム滞在、第一次大戦前夜ヨーロッパの精神文化。",
    development="20世紀ドイツ教養小説・観念小説の頂点として20世紀世界文学の規範となった。",
    historical_context="第一次大戦前夜ヨーロッパの精神的危機。",
    primary_source_url=WIKI_DE+"Der_Zauberberg",
    primary_source_type="Wikipedia: Der Zauberberg",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"サナトリウムにおける時間感覚の解体・教育的論争による主体形成は、AI環境における教育的論争・主体形成のモデルとして理論的に再読される。",
         "related_ai_phenomenon":"AI環境における対話的・論争的主体形成"}])

add(**C, name_ja="マン『ファウスト博士』",
    name_en="Mann's Doktor Faustus",
    name_original="Doktor Faustus",
    period_key="後期モダニズム期",
    definition="トーマス・マンが1947年に発表した長編小説。ドイツ作曲家アドリアン・レーヴァーキューンの伝記形式で、シェーンベルク十二音技法を踏まえた音楽的悪魔契約を、ナチ・ドイツ崩壊と並行的に語る。20世紀ドイツ精神史総括的作品として戦後ヨーロッパ精神史研究の中心。",
    background="マンの米国亡命期、シェーンベルク・アドルノとの音楽論議、戦後ドイツ精神史総括。",
    development="戦後ドイツ精神史・音楽史研究の中心テクストとなった。",
    historical_context="戦後ドイツ精神史総括期。",
    primary_source_url=WIKI_DE+"Doktor_Faustus",
    primary_source_type="Wikipedia: Doktor Faustus",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="マン『トニオ・クレーガー』",
    name_en="Mann's Tonio Kröger",
    name_original="Tonio Kröger",
    period_key="モダニズム期",
    definition="トーマス・マンが1903年に発表した中編小説。北ドイツ商家の息子で芸術家トニオ・クレーガーが、市民的世界と芸術家的世界の間に立つ精神的二重性を独白する。ニーチェ、ショーペンハウアー受容と「芸術家小説」の20世紀ドイツ的範型を確立した。",
    background="ニーチェ・ショーペンハウアー受容、マン自身の精神的二重性の文学化。",
    development="20世紀ドイツ芸術家小説の規範作品となった。",
    historical_context="世紀転換期ドイツの芸術家・市民論議。",
    primary_source_url=WIKI_DE+"Tonio_Kröger",
    primary_source_type="Wikipedia: Tonio Kröger",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マン『ヨゼフとその兄弟』",
    name_en="Mann's Joseph und seine Brüder",
    name_original="Joseph und seine Brüder",
    period_key="モダニズム期",
    definition="トーマス・マンが1933-43年に発表した4部作大長編。旧約聖書創世記のヨセフ物語を、近代的心理学（フロイト）・文化人類学（フレイザー）的視点で再話する。亡命期のマンが10年以上をかけて完成させた、20世紀最大の神話再話文学。",
    background="マンの亡命期創作集中、フロイト・フレイザー人類学の文学化。",
    development="20世紀神話再話文学の最大作品となった。",
    historical_context="ナチ期マンの亡命と文化的抵抗期。",
    primary_source_url=WIKI_DE+"Joseph_und_seine_Brüder",
    primary_source_type="Wikipedia: Joseph und seine Brüder",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# D: Kafka (5)
# ============================================================
add(**C, name_ja="カフカ『変身』",
    name_en="Kafka's Die Verwandlung",
    name_original="Die Verwandlung",
    period_key="モダニズム期",
    definition="フランツ・カフカ（1883-1924）が1915年に発表した中編小説。ある朝、グレゴール・ザムザが巨大な毒虫(Ungeziefer)に変身していることに気づく冒頭で始まり、家族・職場・社会との断絶を描く。20世紀近代不条理文学の最重要古典。",
    background="ハプスブルク末期プラハのユダヤ系ドイツ語作家文化、近代官僚制下の主体疎外。",
    development="20世紀世界文学の最重要古典として無数の批評・哲学的読解（ドゥルーズ／ガタリ）が蓄積。",
    historical_context="ハプスブルク末期プラハの多文化的疎外文化。",
    primary_source_url=GUTEN+"ebooks/5200",
    primary_source_type="Project Gutenberg: The Metamorphosis",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"主体の異質的他者への変身は、AI環境における主体性の変質・非人間化問題の根源的祖型。",
         "related_ai_phenomenon":"AI環境における主体の非人間化・他者化"}])

add(**C, name_ja="カフカ『審判』",
    name_en="Kafka's Der Process",
    name_original="Der Process",
    period_key="モダニズム期",
    definition="カフカが1914-15年執筆、1925年死後出版の長編小説。銀行員ヨーゼフ・Kがある朝、罪状不明のまま逮捕され、不可解な裁判過程を経て処刑される物語。近代官僚制・法制度の不条理性を究極的に文学化し、20世紀全体主義論・法哲学の中心テクスト。",
    background="ハプスブルク末期プラハの官僚制下、カフカ自身の保険局勤務経験。",
    development="ベンヤミン、アドルノら20世紀批判理論、デリダ法哲学の中心研究対象となった。",
    historical_context="ハプスブルク末期から第一次大戦期の官僚制・法制度危機。",
    primary_source_url=WIKI_DE+"Der_Process",
    primary_source_type="Wikipedia: Der Process",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"罪状不明の自動的訴追構造は、AI判定システム・アルゴリズム的訴追の文学的祖型として理論的に再読される。",
         "related_ai_phenomenon":"AI判定システム・アルゴリズム的訴追"}])

add(**C, name_ja="カフカ『城』",
    name_en="Kafka's Das Schloss",
    name_original="Das Schloss",
    period_key="モダニズム期",
    definition="カフカが1922年執筆、1926年死後出版の長編小説（未完）。測量士Kが城に呼ばれて村に到着するが、城の権力中枢に決して接近できない物語。官僚制の到達不可能性と、共同体での不在的同化の主題を究極的に文学化した。",
    background="ハプスブルク末期プラハの官僚制と、カフカ晩年の精神的危機。",
    development="20世紀官僚制論・権力論（フーコー、アガンベン）の中心テクスト。",
    historical_context="ハプスブルク末期から第一次大戦後の官僚制危機。",
    primary_source_url=WIKI_DE+"Das_Schloß",
    primary_source_type="Wikipedia: Das Schloss",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="カフカ『流刑地にて』",
    name_en="Kafka's In der Strafkolonie",
    name_original="In der Strafkolonie",
    period_key="モダニズム期",
    definition="カフカが1914年執筆、1919年に発表した中編小説。流刑地で罪状を被告の身体に刻みつける処刑機械を描く。近代刑罰制度の身体性・テクノロジー性を究極的に象徴化し、フーコー『監獄の誕生』(1975)等20世紀身体・刑罰論の中心テクストとなった。",
    background="第一次大戦期ヨーロッパの植民地・処刑制度、近代刑罰の身体的書き込み技法。",
    development="フーコー、アガンベン、20世紀身体・刑罰論の中心研究対象。",
    historical_context="第一次大戦期植民地刑罰制度の文化的批判期。",
    primary_source_url=WIKI_DE+"In_der_Strafkolonie",
    primary_source_type="Wikipedia: In der Strafkolonie",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"罪状を身体に刻む処刑機械は、AI判定の身体的書き込み・量化されたモニタリングの文学的祖型として理論的に再読される。",
         "related_ai_phenomenon":"AI判定の身体的書き込み・モニタリング"}])

add(**C, name_ja="カフカ『断食芸人』",
    name_en="Kafka's Ein Hungerkünstler",
    name_original="Ein Hungerkünstler",
    period_key="モダニズム期",
    definition="カフカが1922年に発表した短編小説。サーカスで断食を見世物にする芸人が、誰にも理解されないまま死ぬ物語。近代芸術家の社会的疎外と、芸術の見世物化批判をモダニズム的寓話形式で究極的に結晶化した、カフカ晩年の傑作。",
    background="第一次大戦後中欧の見世物文化、芸術家の社会的疎外の文学化。",
    development="20世紀芸術家論・寓話文学の規範作品となった。",
    historical_context="第一次大戦後中欧の見世物文化。",
    primary_source_url=WIKI_DE+"Ein_Hungerkünstler",
    primary_source_type="Wikipedia: Ein Hungerkünstler",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# E: Woolf (4)
# ============================================================
add(**C, name_ja="ウルフ『ダロウェイ夫人』",
    name_en="Woolf's Mrs Dalloway",
    name_original="Mrs Dalloway",
    period_key="モダニズム期",
    definition="ヴァージニア・ウルフ（1882-1941）が1925年に発表した長編小説。ロンドンの一日を通して、政治家夫人クラリッサ・ダロウェイの夜会準備と、戦争神経症退役兵セプティマス・スミスの自殺を平行的に描く。意識の流れと自由間接話法のウルフ的方法の頂点。",
    background="第一次大戦後ロンドンの都市文化、戦争神経症の社会問題化。",
    development="20世紀世界の意識の流れ小説・女性作家研究の中心テクストとなった。",
    historical_context="第一次大戦後英国の都市・戦争記憶文化。",
    primary_source_url=GUTEN+"ebooks/63107",
    primary_source_type="Project Gutenberg: Mrs Dalloway",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ウルフ『灯台へ』",
    name_en="Woolf's To the Lighthouse",
    name_original="To the Lighthouse",
    period_key="モダニズム期",
    definition="ウルフが1927年に発表した長編小説。スコットランド・ヘブリディーズ諸島でのラムジー家の二度の夏（1910と1920）を描く三部構成（窓・時の流れ・灯台）。母の喪失・芸術家リリー・ブリスコウの絵画的探求・第一次大戦の記憶を統合的に文学化した、ウルフ最高傑作の一つ。",
    background="ウルフ自身の両親喪失体験、第一次大戦後の喪文化。",
    development="20世紀モダニズム小説・喪文学・女性芸術家小説の規範作品。",
    historical_context="第一次大戦後英国の喪文化。",
    primary_source_url=GUTEN+"ebooks/144",
    primary_source_type="Project Gutenberg: To the Lighthouse",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ウルフ『波』",
    name_en="Woolf's The Waves",
    name_original="The Waves",
    period_key="モダニズム期",
    definition="ウルフが1931年に発表した実験的長編小説。6人の友人（バーナード、ネヴィル、ルイ、ジニー、スーザン、ロウダ）の幼少から老年までの内的独白を、潮の章間奏曲で区切る形式。ウルフ最も実験的なモダニズム小説として、抒情詩的散文の極限を示した。",
    background="ウルフ晩年の創作実験、第一次大戦後英国の世代論。",
    development="20世紀実験的モダニズム小説の最重要範型となった。",
    historical_context="第一次大戦後英国の世代意識文化。",
    primary_source_url=WIKI_EN+"The_Waves",
    primary_source_type="Wikipedia: The Waves",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"6声部の内的独白を編成する形式は、AI環境における複数主体の並列的声部生成と理論的に共振する。",
         "related_ai_phenomenon":"AI環境における複数主体の並列的声部生成"}])

add(**C, name_ja="ウルフ『自分ひとりの部屋』",
    name_en="Woolf's A Room of One's Own",
    name_original="A Room of One's Own",
    period_key="モダニズム期",
    definition="ウルフが1929年に発表した長文評論。ケンブリッジでの講演を基に、女性が小説を書くためには「年500ポンドと自分ひとりの部屋」が必要であると論じ、シェイクスピアの妹（Judith）を仮構して女性作家の歴史的不在を文学社会学的に解析する。20世紀フェミニズム批評の祖型。",
    background="第一次大戦後英国の女性参政権運動、ウルフ自身のヴィクトリア朝期女性家庭文化批判。",
    development="20世紀フェミニズム批評・女性文学史研究の最重要起点となった。",
    historical_context="戦間期英国の女性権利運動期。",
    primary_source_url=WIKI_EN+"A_Room_of_One%27s_Own",
    primary_source_type="Wikipedia: A Room of One's Own",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"執筆条件としての社会的・経済的基盤論は、AI時代の生成基盤・計算資源と作者性の関係を理論化する古典的参照点。",
         "related_ai_phenomenon":"AI時代の生成基盤・計算資源と作者性"}])


# ============================================================
# F: Faulkner (3)
# ============================================================
add(**C, name_ja="フォークナー『響きと怒り』",
    name_en="Faulkner's The Sound and the Fury",
    name_original="The Sound and the Fury",
    period_key="モダニズム期",
    definition="ウィリアム・フォークナー（1897-1962）が1929年に発表した長編小説。米国南部ミシシッピ州ジェファソンのコンプソン家の没落を、知的障害のベンジー、自殺するクェンティン、皮肉なジェイソン、客観的ディルジーの4視点で語る。20世紀米国南部モダニズムの最高峰。",
    background="米国南部の没落、フォークナー自身のオックスフォード（ミシシッピ州）体験。",
    development="20世紀米国南部文学・意識の流れ小説の規範作品となった。",
    historical_context="戦間期米国南部の文化的危機。",
    primary_source_url=WIKI_EN+"The_Sound_and_the_Fury",
    primary_source_type="Wikipedia: The Sound and the Fury",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"知的障害者の主体視点を中心に据える形式は、AI環境における非標準的主体・多様な認知形態の文学化として理論的に再読される。",
         "related_ai_phenomenon":"AI環境における非標準的・多様認知主体"}])

add(**C, name_ja="フォークナー『死の床に横たわりて』",
    name_en="Faulkner's As I Lay Dying",
    name_original="As I Lay Dying",
    period_key="モダニズム期",
    definition="フォークナーが1930年に発表した長編小説。死にゆく母アディ・バンドレンの遺体を埋葬地ジェファソンへ運ぶ旅を、家族と隣人15人の59個の独白章で描く。フォークナー意識の流れ実験の頂点として、20世紀米国南部モダニズム小説の規範作品。",
    background="米国南部貧農階級の文化、フォークナー意識の流れ実験の発展。",
    development="20世紀世界文学の意識の流れ・多視点小説の規範作品となった。",
    historical_context="大恐慌期米国南部貧農階級文化。",
    primary_source_url=WIKI_EN+"As_I_Lay_Dying",
    primary_source_type="Wikipedia: As I Lay Dying",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="フォークナー『アブサロム、アブサロム!』",
    name_en="Faulkner's Absalom, Absalom!",
    name_original="Absalom, Absalom!",
    period_key="モダニズム期",
    definition="フォークナーが1936年に発表した長編小説。米国南部のトマス・サトペンの興亡を、ハーバード大学のクェンティン・コンプソンと友人シュリーヴが回顧的に再構築する形式。米国南部の人種・歴史的罪と、歴史叙述の構築性をモダニズム的に究極的に文学化した。",
    background="米国南部の奴隷制歴史的記憶、フォークナーのヨクナパトーファ・サーガ。",
    development="20世紀米国南部文学・歴史叙述論の中心テクストとなった。",
    historical_context="戦間期米国南部の人種・歴史記憶文化。",
    primary_source_url=WIKI_EN+"Absalom,_Absalom!",
    primary_source_type="Wikipedia: Absalom, Absalom!",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"複数語り手による歴史的事実の再構築は、AI生成における歴史叙述の多重的構築性問題と理論的に共振する。",
         "related_ai_phenomenon":"AI生成における歴史叙述の多重構築性"}])


# ============================================================
# Cross-domain attachments (>= 10)
# ============================================================
def _attach_cross(name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


_attach_cross("ジョイス『ダブリン市民』「死せる人々」", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"エピファニー詩学",
     "description":"終結雪景場面はモダニズム短編詩学（エピファニー）の規範例として20世紀短編詩学に影響。"}])

_attach_cross("ジョイス『若き芸術家の肖像』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"教養小説の詩学",
     "description":"言語意識の段階的発展による主体形成は、20世紀教養小説詩学の規範例。"}])

_attach_cross("ジョイス『ユリシーズ』テレマコス挿話", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"ホメロス対応の構築原理",
     "description":"古典神話との対応構築は、20世紀モダニスト構築原理の典型例。"}])

_attach_cross("ジョイス『フィネガンズ・ウェイク』構造", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"ヴィーコ歴史哲学",
     "description":"ヴィーコ4段階歴史循環論の文学的構築化は、20世紀歴史哲学受容史の中心。"}])

_attach_cross("プルースト『スワン家の方へ』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"ベルクソン記憶哲学",
     "description":"無意識的記憶論はベルクソン『物質と記憶』(1896)の哲学的記憶論の文学的典型。"}])

_attach_cross("プルーストのプチット・マドレーヌ", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"感覚的記憶の人類学",
     "description":"感覚的契機からの記憶蘇生メカニズムは、20世紀記憶人類学・感覚人類学の中心参照点。"}])

_attach_cross("マン『魔の山』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"ヨーロッパ精神史総括論",
     "description":"セテムブリーニとナフタの教育的論争は、20世紀ヨーロッパ精神史総括論議の文学的縮図。"}])

_attach_cross("カフカ『審判』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"近代官僚制・法批判論",
     "description":"罪状不明の訴追構造は、ベンヤミン、アガンベン、デリダの法哲学批判の中心研究対象。"}])

_attach_cross("カフカ『流刑地にて』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"身体的刑罰の人類学",
     "description":"身体への罪状刻印機械はフーコー『監獄の誕生』身体的刑罰論の文学的祖型。"}])

_attach_cross("ウルフ『自分ひとりの部屋』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"フェミニスト人類学",
     "description":"女性執筆条件論は20世紀フェミニスト人類学・ジェンダー研究の最重要起点。"}])

_attach_cross("ウルフ『ダロウェイ夫人』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"意識の流れ詩学",
     "description":"自由間接話法と意識の流れの統合形式は、20世紀小説詩学の規範研究対象。"}])

_attach_cross("フォークナー『アブサロム、アブサロム!』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"歴史叙述の構築性",
     "description":"複数語り手による歴史再構築は、ヘイドン・ホワイト『メタヒストリー』(1973)等の歴史叙述論の文学的祖型。"}])


# ============================================================
# Main runner
# ============================================================
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
        print(f"[c10-w15] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c10-w15] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c10-w15] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
