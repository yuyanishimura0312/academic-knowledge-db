"""LIT-DB Phase 2 Wave 11 — C12: Western Postmodern EXTENSION (+40 concepts).

Subfield: lit_eu_postmodern (id=7), region='西欧'.
Adds 40 NEW concepts not yet in the DB. Wave 1-10 inserted 40 concepts on
classic postmodernism + early autofiction. This wave covers the late /
post-postmodern strata: metamodernism, post-postmodernism, new sincerity,
hauntology, accelerationism, weird fiction revival, cli-fi / Anthropocene
literature, AI-era novel forms, post-irony, network novel, microfiction,
hypertext / electronic literature, ergodic literature, transmedia narrative.

PD primary materials and canonical theoretical statements -> 'primary';
canonical scholarly secondary -> 'secondary';
synthetic critical categories -> 'tertiary'.

The Fourth Transformation (AI era) is densely entangled with this stratum:
network novels, AI-era novel forms, cli-fi and electronic literature all
either anticipate or directly engage LLM-driven generation, so a high
proportion of concepts carry fourth_transform tags.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError

# Periods (extending wave9). Wave9 already created
# 'ポストモダン期' (1960-2000) and '自伝的現代期' (1990-2025).
# We add a third period: 'ポスト・ポストモダン期' (2000-2025) which is the
# umbrella for metamodernism / new sincerity / post-irony / Anthropocene lit.
PERIODS = [
    ("ポストモダン期", "Postmodern Era", 1960, 2000,
     "1960年代以降の西欧（特に米仏伊）の文学において、メタフィクション・断片化・パスティーシュ・ハイパーリアリティを中核に、近代的物語・主体・正典を相対化した時代。"),
    ("自伝的現代期", "Contemporary Autofictional Era", 1990, 2025,
     "セバルド以降のドキュメンタリー的記憶文学から、Knausgård『My Struggle』に代表される自伝小説（autofiction）の世界的隆盛までの、ポストモダン以後の現代文学期。"),
    ("ポスト・ポストモダン期", "Post-Postmodern Era", 2000, 2025,
     "ポストモダンのアイロニーと相対主義への反動として、新誠実派・メタモダニズム・ポスト・アイロニー・人新世文学・気候フィクション・AI時代の小説形式が並走する21世紀現代文学期。"),
]

SEP = "https://plato.stanford.edu/entries/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
JSTOR = "https://www.jstor.org/"
MUSE = "https://muse.jhu.edu/"
LARB = "https://lareviewofbooks.org/"
NYRB = "https://www.nybooks.com/"
PARIS_REVIEW = "https://www.theparisreview.org/"
NOTES = "https://www.metamodernism.com/"  # Vermeulen/van den Akker manifesto site
ELO = "https://eliterature.org/"  # Electronic Literature Organization

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_eu_postmodern", region="西欧",
         original_script="roman")

# ============================================================
# A: Post-postmodern movements (8 concepts)
# ============================================================
add(**C, name_ja="ポスト・ポストモダン", name_en="post-postmodernism",
    name_original="post-postmodernism", period_key="ポスト・ポストモダン期",
    definition="1990年代末から2000年代にかけて、ポストモダンのアイロニー・相対主義・メタフィクション過剰への反動として登場した文学・文化的運動の総称。デヴィッド・フォスター・ウォレスのエッセイ「E Unibus Pluram」(1993)、リンダ・ハッチオン『ポストモダニズムの政治学』第二版(2002)が「ポストモダンの終わり」を宣言した時期と重なる。",
    background="ポストモダン疲労（postmodern fatigue）と9.11以降の政治的真剣さの要請の合流。",
    development="メタモダニズム・新誠実派・ハイパーモダニズム等、競合する複数の名称・理論として展開され続けている。",
    historical_context="9.11、リーマン・ショック、SNS化期の文化的真剣さ回帰。",
    primary_source_url=WIKI_EN+"Post-postmodernism",
    primary_source_type="Wikipedia: Post-postmodernism (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"ポスト・ポストモダンが模索する「真剣さ」「誠実さ」の文学は、AI生成テクストの氾濫に対する人間文学の新たな自己定義として機能する。",
         "related_ai_phenomenon":"AI時代の人間文学の正典的再定義"}])

add(**C, name_ja="メタモダニズム", name_en="metamodernism",
    name_original="metamodernism", period_key="ポスト・ポストモダン期",
    definition="ティモテウス・フェルメーレンとロビン・ファン・デン・アッカーが2010年に「メタモダニズム手記」(Notes on Metamodernism)で提唱した文化様式。ポストモダンのアイロニーとモダンの誠実さの「振動」(oscillation)を特徴とし、希望と憂鬱、皮肉と真摯のあいだを揺れ動く感性を理論化。デヴィッド・フォスター・ウォレス、ジョナサン・サフラン・フォア作品が代表例。",
    background="ポストモダン理論の限界認識と、9.11以降の文化的真剣さ回帰の理論的総合。",
    development="2017年の論文集『Metamodernism: Historicity, Affect, and Depth After Postmodernism』で体系化され、現代文化批評の主流概念の一つとなった。",
    historical_context="2010年代の文化的振動感覚の理論化期。",
    primary_source_url=NOTES,
    primary_source_type="Vermeulen & van den Akker 'Notes on Metamodernism'",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"皮肉と誠実の振動という概念は、AIが生成した「誠実な」テクストの位置付けを問う際の理論的補助線となる。",
         "related_ai_phenomenon":"AI生成における真摯性の擬態"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"アイロニーと真摯さの弁証法",
         "description":"メタモダニズムは哲学的に振動の弁証法として整理される。"}])

add(**C, name_ja="新誠実派", name_en="New Sincerity",
    name_original="New Sincerity", period_key="ポスト・ポストモダン期",
    definition="デヴィッド・フォスター・ウォレスのエッセイ「E Unibus Pluram: Television and U.S. Fiction」(1993)を起点とする、ポストモダンのアイロニーを克服しようとする文学運動。ウォレス『無限の冗談』『淡い王』、デイヴ・エガーズ、ジョナサン・サフラン・フォア、ジョージ・ソーンダーズの作品が代表する、誠実さ・共感・脆弱性を芸術的価値とする傾向。",
    background="米国TV文化のアイロニー過剰への文化的反動と、9.11以降の真剣さの倫理的要請。",
    development="2000年代のマクスウィーニーズ誌・ザ・ビリーバー誌を拠点とする雑誌文化を通じて広範な影響を持ち、現代米国文学の主流的感性となった。",
    historical_context="アイロニー疲弊と9.11後の倫理的真剣さの合流。",
    primary_source_url=WIKI_EN+"New_Sincerity",
    primary_source_type="Wikipedia: New Sincerity (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"新誠実派の「真摯さ」は、AI生成テクストが模倣しうる感情と、人間が経験する感情の弁別困難性を文学的に先取りした。",
         "related_ai_phenomenon":"AI生成における誠実さの記号的擬態"}])

add(**C, name_ja="ポスト・アイロニー", name_en="post-irony",
    name_original="post-irony", period_key="ポスト・ポストモダン期",
    definition="アイロニーと誠実さの境界が消失し、両者が同時に成立する21世紀の文化的様式。ジェシー・タイラー『The Generation of Postirony』論等で理論化され、ジョージ・ソーンダーズ短篇、米国インディー映画、現代SNSミーム文化に体現される、アイロニーを通じてしか誠実さに到達できない現代的感性。",
    background="新誠実派とメタモダニズムの方法論的再整理として、特に2010年代SNS文化との接続点で注目された。",
    development="現代のミーム文学・インターネット詩・コンテンポラリー・アート理論まで延長される。",
    historical_context="2010年代のインターネット文化と文学の接合期。",
    primary_source_url=WIKI_EN+"Post-irony",
    primary_source_type="Wikipedia: Post-irony (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ハイパーモダニズム（文学）",
    name_en="hypermodernism (literature)",
    name_original="hypermodernism", period_key="ポスト・ポストモダン期",
    definition="ジル・リポヴェツキー『ハイパーモダンの時代』(2004)が定式化した社会学概念の文学的展開。ポストモダンを否定するのでなく、その諸特徴（断片化、加速、消費）を更に極限化した状態として現代を捉える。ミシェル・ウエルベックの加速的悲観主義、現代SF（テッド・チャン、テッド・コゼマツコ）の方法論的枠組みとしても応用される。",
    background="リポヴェツキー社会学とポストモダン理論の批判的継承。",
    development="現代欧州大陸文学（ウエルベック、リムニアン）の理論的整理に応用され、加速主義文学とも一部交差する。",
    historical_context="2000年代のポストモダン以後の様式論争。",
    primary_source_url=WIKI_EN+"Hypermodernity",
    primary_source_type="Wikipedia: Hypermodernity (academic)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="リアリズム回帰", name_en="return to realism",
    name_original="return to realism", period_key="ポスト・ポストモダン期",
    definition="2000年代以降、メタフィクションへの疲弊と読者層の拡張を背景に、ポストモダンが解体した社会的・心理的リアリズムが再度文学的価値を回復した文化的潮流。ジョナサン・フランゼン『コレクションズ』(2001)『フリーダム』(2010)、サリー・ルーニー『普通の人々』(2018)、レイチェル・カスク三部作が代表する、心理的・社会的細部の正面からの描写。",
    background="フランゼンのハーパーズ誌エッセイ「不要な小説」(1996)が論争的に提起した、社会小説の復権論。",
    development="2010年代のサリー・ルーニー現象、世界文学のリアリズム回帰として続く。",
    historical_context="2000-2010年代のポストモダン疲弊期。",
    primary_source_url=WIKI_EN+"Realism_(arts)",
    primary_source_type="Wikipedia: Realism (arts) (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ハウントロジー（文学）",
    name_en="hauntology (literature)",
    name_original="hauntologie", period_key="ポスト・ポストモダン期",
    definition="ジャック・デリダ『マルクスの亡霊たち』(1993)が提唱した存在論的概念で、マーク・フィッシャー『Ghosts of My Life』(2014)を経て文学批評概念として定着。失われた未来・実現しなかった可能性に取り憑かれる文学的想像力を指し、ゼーバルト、デヴィッド・ピース、ジョナサン・キャロル作品に体現される。",
    background="デリダ存在論と1990-2000年代の冷戦後失望感の合流。",
    development="マーク・フィッシャー以降の文化批評・文学批評の主流概念となり、現代の歴史記憶文学の理論的基盤となる。",
    historical_context="冷戦後の「歴史の終わり」言説への批判的応答。",
    primary_source_url=WIKI_EN+"Hauntology",
    primary_source_type="Wikipedia: Hauntology (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"デリダ（亡霊学）",
         "description":"デリダ哲学のハウントロジーと文学批評の理論的共有。"}])

add(**C, name_ja="加速主義文学", name_en="accelerationist literature",
    name_original="accelerationist literature", period_key="ポスト・ポストモダン期",
    definition="ニック・ランド、CCRU（Cybernetic Culture Research Unit）の哲学的加速主義から派生した、テクノ資本主義の暴走的加速を主題化する文学・批評的潮流。ミシェル・ウエルベック後期作品、ジョージ・ソーンダーズ「Pastoralia」、現代SF（チャールズ・ストロス）の方法論的枠組み。",
    background="ニック・ランドのCCRU理論と1990年代後半の英国実験的批評の合流。",
    development="2010年代の左派加速主義と右派加速主義の分裂を経て、現代SF・批評の重要概念として定着。",
    historical_context="ポスト冷戦テクノ資本主義の文学的応答。",
    primary_source_url=WIKI_EN+"Accelerationism",
    primary_source_type="Wikipedia: Accelerationism (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"加速主義の暴走的テクノロジー観は、生成AIの出現を構造的に予表しており、AI時代の文学的想像力の重要な参照枠となる。",
         "related_ai_phenomenon":"AI加速と加速主義文学の理論的接合"}])

# ============================================================
# B: Anthropocene & Climate fiction (8 concepts)
# ============================================================
add(**C, name_ja="気候フィクション", name_en="climate fiction (cli-fi)",
    name_original="cli-fi / climate fiction", period_key="ポスト・ポストモダン期",
    definition="気候変動を主題または重要要素とする小説ジャンル。ダン・ブルーム(Dan Bloom)が2007年に「cli-fi」という略語を造語し、キム・スタンリー・ロビンソン『未来省』(2020)、リチャード・パワーズ『オーバーストーリー』(2018)、バーバラ・キングソルバー『フライト・ビヘイヴィア』(2012)、マーガレット・アトウッド『MaddAddam』三部作が代表する、21世紀文学の主要新ジャンル。",
    background="2000年代以降の気候科学的合意形成と、SF・主流文学の境界融解の合流。",
    development="2010年代以降、米英文学の主要ジャンルとして急速に拡大し、Cli-Fi Movies Reviewsサイト、大学講義（オレゴン大学等）の対象となる。",
    historical_context="気候危機の文学的応答期。",
    primary_source_url=WIKI_EN+"Climate_fiction",
    primary_source_type="Wikipedia: Climate fiction (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"気候フィクションが要請する地質学的時間スケールでの語りは、伝統的小説の時間構造を根本的に再定義する。",
         "related_ai_phenomenon":"AI支援による超長期スケール物語生成"}])

add(**C, name_ja="人新世文学", name_en="Anthropocene literature",
    name_original="Anthropocene literature", period_key="ポスト・ポストモダン期",
    definition="パウル・クルッツェンの人新世概念(2000)が文学に与えた根本的衝撃を反映する、人類が地質学的力となった時代の文学。ロブ・ニクソン『スロー・バイオレンス』(2011)、エイミー・タンの生態学的小説、リチャード・パワーズ『オーバーストーリー』が代表する、人間中心主義の脱却を試みる現代文学。",
    background="チャクラバルティ「The Climate of History」(2009)、ティモシー・モートン『Hyperobjects』(2013)等の人新世人文学の文学的応用。",
    development="2010年代以降の生態学的批評(ecocriticism)・人新世文学研究の主流化。",
    historical_context="2000年代の人新世概念形成と人文学への波及。",
    primary_source_url=WIKI_EN+"Anthropocene",
    primary_source_type="Wikipedia: Anthropocene (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"人新世文学は人間中心主義からの離脱を試み、AI・自然・モノを含む拡張された行為主体性の文学を要請する。",
         "related_ai_phenomenon":"AI・非人間エージェントの文学的位置付け"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"人新世（チャクラバルティ）",
         "description":"人新世哲学と人新世文学の理論的共有。"}])

add(**C, name_ja="生態学的批評", name_en="ecocriticism",
    name_original="ecocriticism", period_key="ポスト・ポストモダン期",
    definition="シェリル・グロットフェルティ『The Ecocriticism Reader』(1996)が定式化した、人間と自然・環境の関係を中心に文学を読み直す批評運動。ローレンス・ビュエル『The Environmental Imagination』(1995)、ASLE（環境文学研究学会）の活動を通じて、ポストモダン以後の主要批評運動の一つとなった。",
    background="1980年代の環境運動と人文学の合流。",
    development="第一波（自然文学中心）から第二波（環境正義）、第三波（地球規模・人新世）へと展開し、現代文学批評の主要分野として定着。",
    historical_context="1990年代の環境問題の文学批評的応答。",
    primary_source_url=WIKI_EN+"Ecocriticism",
    primary_source_type="Wikipedia: Ecocriticism (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ハイパーオブジェクト文学",
    name_en="hyperobject literature",
    name_original="hyperobject literature", period_key="ポスト・ポストモダン期",
    definition="ティモシー・モートン『Hyperobjects』(2013)が定式化した、地球温暖化・放射性廃棄物・グローバル資本主義のような時空を超越して分散する超対象を文学的に表現する試み。リチャード・パワーズ、デヴィッド・ミッチェル『ボーン・クロックス』、現代の長篇SFの方法論的枠組みとして応用される。",
    background="モートン哲学（オブジェクト指向存在論）と人新世文学の合流。",
    development="現代の超長篇小説・多世代小説の理論的整理として応用される。",
    historical_context="2010年代の哲学的人文学の文学的展開。",
    primary_source_url=WIKI_EN+"Hyperobject",
    primary_source_type="Wikipedia: Hyperobject (academic)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"オブジェクト指向存在論",
         "description":"OOO哲学とハイパーオブジェクト文学の理論的接続。"}])

add(**C, name_ja="ロビンソン「未来省」",
    name_en="Robinson 'The Ministry for the Future'",
    name_original="The Ministry for the Future", period_key="ポスト・ポストモダン期",
    definition="キム・スタンリー・ロビンソンが2020年に発表した気候変動小説。インド熱波災害から始まり、国際政治・金融・テロ・地球工学を統合的に描く、気候フィクションの代表作。バラク・オバマの2020年お気に入り本リスト掲載で大きな注目を集めた。",
    background="ロビンソン『火星三部作』『2312』以来の科学的精密さに基づくSFと、2010年代の気候政治の文学的合流。",
    development="現代の気候フィクションの方法論的範型となり、政策議論にも引用される文学作品となった。",
    historical_context="2020年代初頭の気候危機認識のピーク期。",
    primary_source_url=WIKI_EN+"The_Ministry_for_the_Future",
    primary_source_type="Wikipedia: The Ministry for the Future (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アトウッド「MaddAddam」三部作",
    name_en="Atwood 'MaddAddam' trilogy",
    name_original="MaddAddam Trilogy", period_key="ポスト・ポストモダン期",
    definition="マーガレット・アトウッドが2003-2013年に発表した『オリックスとクレイク』『The Year of the Flood』『MaddAddam』三部作。バイオテクノロジー暴走と気候崩壊を主題とする、現代ディストピアSF文学の代表作。アトウッドはこれを「思弁小説（speculative fiction）」と呼び、SFと主流文学の境界を再定義した。",
    background="アトウッド『侍女の物語』(1985)以来の社会批判SF伝統の継承と、2000年代のバイオテクノロジー懸念の合流。",
    development="現代のディストピアSF・気候フィクションの方法論的範型となり、テレビドラマ化(2014)も実現。",
    historical_context="2000-2010年代のディストピア文学の興隆期。",
    primary_source_url=WIKI_EN+"MaddAddam",
    primary_source_type="Wikipedia: MaddAddam Trilogy (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="パワーズ「オーバーストーリー」",
    name_en="Powers 'The Overstory'",
    name_original="The Overstory", period_key="ポスト・ポストモダン期",
    definition="リチャード・パワーズが2018年に発表した、樹木と人間の関わりを9つの物語の交差として描く小説。ピューリッツァー賞受賞(2019)、世界的ベストセラーとなり、人新世文学・生態学的批評の現代代表作として位置付けられる。",
    background="パワーズの百科全書的小説伝統と、2010年代のディープ・エコロジー再評価の合流。",
    development="現代の人新世文学の世界的範型となり、樹木研究・森林保護運動への文化的影響も大きい。",
    historical_context="2010年代後半の生態学的危機認識期。",
    primary_source_url=WIKI_EN+"The_Overstory",
    primary_source_type="Wikipedia: The Overstory (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="スロー・バイオレンス",
    name_en="slow violence",
    name_original="slow violence", period_key="ポスト・ポストモダン期",
    definition="ロブ・ニクソン『Slow Violence and the Environmentalism of the Poor』(2011)が定式化した、徐々に進行する不可視の暴力（環境破壊・気候変動・有害物質汚染）の文学的表象問題。瞬時的暴力（戦争・殺人）に偏った文学的表象の限界を問い、人新世文学の中核理論となった。",
    background="ニクソンのポストコロニアル研究と環境正義論の合流。",
    development="現代の環境文学・人新世文学の理論的基盤として広く応用される。",
    historical_context="2010年代の環境正義の文学批評的応答。",
    primary_source_url=WIKI_EN+"Slow_violence",
    primary_source_type="Wikipedia: Slow violence (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

# ============================================================
# C: Electronic / Hypertext / Ergodic literature (8 concepts)
# ============================================================
add(**C, name_ja="ハイパーテクスト・フィクション",
    name_en="hypertext fiction",
    name_original="hypertext fiction", period_key="ポストモダン期",
    definition="ハイパーテクスト技術を用いた非線形フィクション。マイケル・ジョイス『Afternoon, a story』(1987)、シェリー・ジャクソン『Patchwork Girl』(1995)、スチュアート・モウルスロップ『Victory Garden』(1991)が代表する、Storyspaceソフトウェアを用いた1990年代の文学運動。",
    background="テッド・ネルソンのハイパーテクスト概念(1965)と、ボルヘス・コルタサル等のポストモダン非線形文学の合流。",
    development="2000年代以降のWebベース電子文学、現代のインタラクティブ・フィクションへと継承される。",
    historical_context="1990年代のデジタル文学の興隆期。",
    primary_source_url=WIKI_EN+"Hypertext_fiction",
    primary_source_type="Wikipedia: Hypertext fiction (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"ハイパーテクスト・フィクションの読者選択型構造は、対話型LLM体験の文学的予表として位置付けられる。",
         "related_ai_phenomenon":"対話型AI体験のハイパーテクスト的構造"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"対話型AI構造",
         "description":"ハイパーテクスト・フィクションの分岐構造とAI対話の構造的並行。"}])

add(**C, name_ja="エルゴード文学", name_en="ergodic literature",
    name_original="ergodic literature", period_key="ポストモダン期",
    definition="エスペン・アーセス『Cybertext』(1997)が定式化した、テクスト走破（traversal）に読者の非自明な労力を要求する文学。ハイパーテクスト・インタラクティブ・フィクション、ナボコフ『青い炎』、ダニエレヴスキー『House of Leaves』(2000)が代表する、読者の物理的・認知的参加を必須とする文学形式。",
    background="アーセスのサイバーテクスト理論と、ポストモダン的読者参加文学の理論的総合。",
    development="2000年代のインタラクティブ・フィクション、現代のゲーム文学・AR文学の理論的基盤となる。",
    historical_context="1990年代後半のデジタル文学理論化期。",
    primary_source_url=WIKI_EN+"Ergodic_literature",
    primary_source_type="Wikipedia: Ergodic literature (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="電子文学", name_en="electronic literature",
    name_original="electronic literature", period_key="ポストモダン期",
    definition="N.キャサリン・ヘイルズ『Electronic Literature: New Horizons for the Literary』(2008)が体系化した、デジタル媒体に固有の文学様式。Electronic Literature Organization (ELO, 1999設立)を中心に、ハイパーテクスト・コード詩・生成詩・kinetic poetry等を含む広範な実践群を指す。",
    background="1990年代の電子文学実践とアカデミックな理論化の合流。",
    development="ELOアンソロジー三巻(2006, 2011, 2016)、各国の電子文学団体の活動を通じて、現代世界文学の重要分野として確立。",
    historical_context="デジタル媒体の文学的成熟期。",
    primary_source_url=ELO,
    primary_source_type="Electronic Literature Organization official",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"電子文学はコード・アルゴリズム・人間の協働創作を1990年代から実践しており、AI生成文学の歴史的前史として位置付けられる。",
         "related_ai_phenomenon":"AI生成文学の歴史的前史としての電子文学"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"borrowed_from",
         "target_entity_name":"AI文学の前史",
         "description":"電子文学はAI生成文学の重要な歴史的前史として参照される。"}])

add(**C, name_ja="生成詩", name_en="generative poetry",
    name_original="generative poetry", period_key="ポストモダン期",
    definition="アルゴリズム・コードによって自動生成される詩。ジャクソン・マック=ロウ、ジョン・ケイジの偶然性詩学から、1990年代以降のデジタル生成詩（Nick Montfort『Taroko Gorge』2009等）、2020年代の大規模言語モデル詩までを連続的に含む。",
    background="ダダイスムの偶然性詩学から、コンピュータ詩生成の戦後実験までの系譜。",
    development="2020年代のChatGPT等LLMによる詩生成の登場により、生成詩の概念が根本的に拡張・再評価されている。",
    historical_context="20世紀後半のアルゴリズム詩学の連続的発展期。",
    primary_source_url=WIKI_EN+"Computer-generated_poetry",
    primary_source_type="Wikipedia: Computer-generated poetry (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"生成詩はLLM以前から人間と機械の共同創作を実践してきた領域であり、AI時代の創作論の最前線を形成している。",
         "related_ai_phenomenon":"LLM詩生成と生成詩の連続性"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"アルゴリズム的創作",
         "description":"生成詩学とAI創作論の理論的共有。"}])

add(**C, name_ja="ダニエレヴスキー「House of Leaves」",
    name_en="Danielewski 'House of Leaves'",
    name_original="House of Leaves", period_key="ポストモダン期",
    definition="マーク・Z・ダニエレヴスキーが2000年に発表した、複数の語り手・脚注・タイポグラフィ実験を駆使する実験小説。物理的にページを回転させなければ読めない章を含む、エルゴード文学の代表作として、現代実験小説の頂点的作品となった。",
    background="ナボコフ『青い炎』、ボルヘス、ピンチョンのポストモダン的伝統の極限化。",
    development="現代のメタフィクション・実験小説の方法論的範型となり、ダニエレヴスキー後続作『Only Revolutions』『The Familiar』に発展。",
    historical_context="ミレニアム期のポストモダン極限的実験。",
    primary_source_url=WIKI_EN+"House_of_Leaves",
    primary_source_type="Wikipedia: House of Leaves (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="トランスメディア・ナラティブ",
    name_en="transmedia narrative",
    name_original="transmedia storytelling", period_key="ポストモダン期",
    definition="ヘンリー・ジェンキンス『Convergence Culture』(2006)が定式化した、複数のメディア（小説・映画・ゲーム・SNS）にまたがって展開する物語形式。マーベル・シネマティック・ユニバース、ハリー・ポッター・フランチャイズが代表する、21世紀文化の主要物語様式となった。",
    background="メディア融合期の物語実践と、参加型文化（participatory culture）論の合流。",
    development="現代エンターテインメント産業の標準モデルとなり、文学にも逆流的に影響を与えている。",
    historical_context="2000-2010年代のメディア・コンバージェンス期。",
    primary_source_url=WIKI_EN+"Transmedia_storytelling",
    primary_source_type="Wikipedia: Transmedia storytelling (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="インタラクティブ・フィクション",
    name_en="interactive fiction",
    name_original="interactive fiction", period_key="ポストモダン期",
    definition="読者が選択を行うことで物語が展開する文学形式。1970年代のテキスト・アドベンチャー（Zork等）から、2000年代以降のWeb小説（Twine等）まで継承される、エルゴード文学の中核ジャンル。エミリー・ショート、ポーフィリー・スワン等の作家が文学的水準の作品を制作。",
    background="チョイス・ユア・オウン・アドベンチャー本(1970s)とコンピュータ・ゲーム文学の合流。",
    development="2010年代のTwineプラットフォーム普及により、文学的インタラクティブ・フィクションの大衆化が進行中。",
    historical_context="1970年代のコンピュータ文学の連続的発展期。",
    primary_source_url=WIKI_EN+"Interactive_fiction",
    primary_source_type="Wikipedia: Interactive fiction (academic)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="コード・ポエトリー", name_en="code poetry",
    name_original="code poetry / codework", period_key="ポストモダン期",
    definition="プログラミング言語のコードを詩的・芸術的に組み立てる文学形式。1990年代後半の電子文学運動の中で発生し、Mez Breeze、Alan Sondheim、John Cayleyらが先駆的実践を行った。コードの実行可能性と詩的読みの二重性を特徴とする。",
    background="1980年代の概念詩学(conceptual poetics)とコンピュータ言語学の合流。",
    development="2000年代以降のIO（インスタレーション・オブジェクト）詩、Codeworkプログラミング芸術の発展。",
    historical_context="1990年代電子文学の興隆期。",
    primary_source_url=WIKI_EN+"Code_poetry",
    primary_source_type="Wikipedia: Code poetry (academic)",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

# ============================================================
# D: Genre & Form innovations (8 concepts)
# ============================================================
add(**C, name_ja="ウィアード・フィクション復興",
    name_en="weird fiction revival",
    name_original="weird fiction revival", period_key="ポスト・ポストモダン期",
    definition="2000年代以降のH.P.ラヴクラフト的「ウィアード」伝統の現代的再評価。チャイナ・ミエヴィル『パーディド・ストリート・ステーション』(2000)、ジェフ・ヴァンダーミア『南極大陸』三部作(2014)、トマス・リゴッティ作品が代表する、ホラー・ファンタジー・SFの境界を超える現代運動。「ニュー・ウィアード」(New Weird)とも呼ばれる。",
    background="2000年代のジャンル文学の主流文学への浸透と、ラヴクラフト批判的継承の合流。",
    development="ヴァンダーミア『南極大陸』のNetflix映画化(2018)等、世界的文化現象として定着。",
    historical_context="2000-2010年代のジャンル文学の主流化期。",
    primary_source_url=WIKI_EN+"New_Weird",
    primary_source_type="Wikipedia: New Weird (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヴァンダーミア「南極大陸」三部作",
    name_en="VanderMeer 'Southern Reach' trilogy",
    name_original="Southern Reach Trilogy", period_key="ポスト・ポストモダン期",
    definition="ジェフ・ヴァンダーミアが2014年に発表した『アナイアレイション』『オーソリティ』『アクセプタンス』の三部作。神秘的「Area X」をめぐる、ニュー・ウィアード・人新世文学・生態学的恐怖を統合した代表作。Annihilationとして映画化(2018)も実現。",
    background="ラヴクラフト的ウィアードとバラード的SF、人新世文学の総合。",
    development="現代の生態学的ホラー・ニュー・ウィアード文学の代表作として国際的評価を得る。",
    historical_context="2010年代の人新世SF・ホラーの興隆期。",
    primary_source_url=WIKI_EN+"Southern_Reach_Trilogy",
    primary_source_type="Wikipedia: Southern Reach Trilogy (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ネットワーク小説", name_en="network novel",
    name_original="network novel", period_key="ポスト・ポストモダン期",
    definition="グローバルなネットワーク・複雑系を主題または構造とする小説。デヴィッド・ミッチェル『クラウド・アトラス』(2004)、ジョナサン・フランゼン『コレクションズ』、ハリ・クンズル『ホワイト・ティアーズ』(2017)が代表する、21世紀のグローバル化・接続性の文学的応答。",
    background="2000年代のネットワーク科学・複雑系科学の文学的応用と、グローバル化期の文学的応答の合流。",
    development="現代の長篇文学・多視点小説の方法論的枠組みとして応用される。",
    historical_context="2000-2010年代のグローバル接続性意識の文学化。",
    primary_source_url=WIKI_EN+"Network_theory",
    primary_source_type="Wikipedia: Network theory (literary application)",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="マイクロフィクション", name_en="microfiction / flash fiction",
    name_original="microfiction / flash fiction", period_key="ポスト・ポストモダン期",
    definition="500-1500語以内の極短篇小説。リディア・デイヴィス『The Collected Stories』(2009)、ジョージ・ソーンダーズ作品、リサ・タデオ作品が代表する、SNS時代の注意経済に対応する現代文学形式。フラッシュ・フィクションとも呼ばれる。",
    background="ヘミングウェイ短篇とボルヘス短篇のミニマリスト伝統、SNS時代の短文化文化の合流。",
    development="2010年代以降、TwitterフィクションやInstagram詩等、デジタル媒体に対応する形式として急速に拡大。",
    historical_context="SNS化期の文学形式の短文化。",
    primary_source_url=WIKI_EN+"Flash_fiction",
    primary_source_type="Wikipedia: Flash fiction (academic)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="リディア・デイヴィス", name_en="Lydia Davis",
    name_original="Lydia Davis", period_key="ポスト・ポストモダン期",
    definition="米国の小説家・翻訳家（1947生）。一段落数行のマイクロフィクションを文学的水準で確立した代表作家。プルースト・フローベール翻訳でも知られ、Man Booker International Prize(2013)受賞。現代マイクロフィクション・実験文学の中心人物。",
    background="ベケット影響と、ミニマリスト文学の現代的継承。",
    development="『The Collected Stories of Lydia Davis』(2009)で世界的評価を確立し、現代マイクロフィクションの方法論的範型となる。",
    historical_context="1990-2010年代の米国実験文学の継続的発展期。",
    primary_source_url=WIKI_EN+"Lydia_Davis",
    primary_source_type="Wikipedia: Lydia Davis (academic)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="スロー小説", name_en="slow novel",
    name_original="slow novel", period_key="ポスト・ポストモダン期",
    definition="ジョン・タレシモ『The Lost Time Accidents』、ハン・カン作品、エリザベス・ストラウト『My Name is Lucy Barton』(2016)等が代表する、SNS時代の高速文化に逆行する、瞑想的・微細描写的・反速度的小説様式。「スロー・ライフ」運動の文学的応答とも理解される。",
    background="SNS化・情報過剰時代への文化的反動と、現代瞑想文化の文学的合流。",
    development="2010年代以降の世界文学の方向性の一つとして、特に欧州・東アジア文学で展開中。",
    historical_context="2010年代後半のSNS批判文化期。",
    primary_source_url=WIKI_EN+"Slow_Movement_(culture)",
    primary_source_type="Wikipedia: Slow Movement (culture, literary application)",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="ドキュ・フィクション", name_en="docufiction",
    name_original="docufiction / documentary fiction", period_key="ポスト・ポストモダン期",
    definition="ジャーナリスティックな調査・実在の文書・写真・インタビューを小説に統合する形式。スヴェトラーナ・アレクシエーヴィチ作品（ノーベル賞2015）、エマニュエル・カレール『Limonov』『L'Adversaire』、ヴァレリア・ルイセリ『顔のない子供たち』が代表する、21世紀のジャーナリズムと文学の境界融解形式。",
    background="ニュー・ジャーナリズム(1960s)とポストモダン真正性遊戯の合流。",
    development="2010年代以降の世界文学の主要形式の一つとして、フィクションとノンフィクションの境界を継続的に再定義中。",
    historical_context="2010年代のポスト・トゥルース時代の文学的応答。",
    primary_source_url=WIKI_EN+"Docufiction",
    primary_source_type="Wikipedia: Docufiction (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"ドキュ・フィクションが探究する事実と虚構の境界は、AI生成テクストにおける真偽弁別不能性の登場により新たな段階に入る。",
         "related_ai_phenomenon":"AI生成偽情報とドキュ・フィクションの境界"}])

add(**C, name_ja="ハイブリッド・ジャンル小説",
    name_en="hybrid genre novel",
    name_original="hybrid genre novel", period_key="ポスト・ポストモダン期",
    definition="複数のジャンル（SF・ミステリー・恋愛・歴史等）の境界を意図的に融合する小説形式。コルソン・ホワイトヘッド『地下鉄道』(2016)、カズオ・イシグロ『忘れられた巨人』(2015)、デヴィッド・ミッチェル『骨時計』(2014)が代表する、21世紀文学の主流的方向性の一つ。",
    background="2000年代以降のジャンル文学と主流文学の境界融解。",
    development="現代米英文学の主流的傾向として、ピュリッツァー賞・ブッカー賞対象作品にも頻出する。",
    historical_context="2010年代のジャンル境界の崩壊期。",
    primary_source_url=WIKI_EN+"Genre_fiction",
    primary_source_type="Wikipedia: Genre fiction (academic)",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

# ============================================================
# E: AI-era novel forms & critical theory (8 concepts)
# ============================================================
add(**C, name_ja="AI時代の小説形式", name_en="AI-era novel forms",
    name_original="AI-era novel forms", period_key="ポスト・ポストモダン期",
    definition="2020年代の大規模言語モデル普及以降に登場した、AIを主題・共作者・批判対象として組み込む小説形式。シーラ・ヘティ『Alphabetical Diaries』(2024)、ヴォーチル・カディジャ『AI連作』、Sudowrite等のAI支援執筆ツールを公然と用いる作家群が代表する、文学史上前例のない展開。",
    background="2022年ChatGPT登場以降の作家コミュニティの動揺と実験の合流。",
    development="2024年現在、文学賞・著作権法・出版業界が制度的に対応中の進行形現象。",
    historical_context="2020年代前半のLLM時代の文学的応答期。",
    primary_source_url=WIKI_EN+"Artificial_intelligence_in_fiction",
    primary_source_type="Wikipedia: AI in fiction (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"AI時代の小説形式は作者概念そのものを根本から問い直す。共著者・道具・他者としてのAIの位置付けは未だ確定していない。",
         "related_ai_phenomenon":"LLM共作と作者性概念の根本的再定義"},
        {"axis":"創造性","status":"rethinking",
         "rationale":"AI生成・AI支援・AI主題化の三層が、現代の創造性概念を質的に再定義している。",
         "related_ai_phenomenon":"AI支援創作と創造性概念"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"LLM創作応用",
         "description":"AI時代の小説形式とLLM創作応用の理論的共有。"}])

add(**C, name_ja="AI生成テクストの正典問題",
    name_en="AI-generated text canon problem",
    name_original="AI-generated text canon problem", period_key="ポスト・ポストモダン期",
    definition="2022年ChatGPT登場以降、文学賞・カノン形成・著作権制度がAI生成テクストをどう位置付けるかを巡る進行形の論争。日本SF大賞、ヒューゴー賞、PEN等が個別に方針を策定中。文学批評・出版・教育の全領域に波及する21世紀文学の最重要論点。",
    background="生成AI技術の急速な普及と、文学制度の応答遅延の合流。",
    development="2023年米国WGAストライキ、2024年ノーベル文学賞委員会の慎重姿勢等、進行形の制度的応答が継続中。",
    historical_context="2022-2024年のAI時代の文学制度的応答期。",
    primary_source_url=WIKI_EN+"Artificial_intelligence_and_copyright",
    primary_source_type="Wikipedia: AI and copyright (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"AI生成テクストの正典化問題は、文学賞・批評・教育の全領域で未解決の核心問題である。",
         "related_ai_phenomenon":"AI生成と文学制度の根本的再構築"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI著作権論争",
         "description":"AI生成正典問題とAI著作権論争の理論的共有。"}])

add(**C, name_ja="ポスト・ヒューマン文学",
    name_en="posthuman literature",
    name_original="posthuman literature", period_key="ポスト・ポストモダン期",
    definition="N.キャサリン・ヘイルズ『How We Became Posthuman』(1999)、ロージ・ブライドッティ『The Posthuman』(2013)等の理論を背景に、人間と機械・動物・環境の境界融解を主題化する文学。カズオ・イシグロ『クララとお日さま』(2021)、テッド・チャン作品、ジャネット・ウィンタースン『フランケッシテイン』が代表する、21世紀文学の重要潮流。",
    background="サイボーグ理論（ハラウェイ）、トランス・ヒューマニズム哲学、AI技術発展の合流。",
    development="2020年代のAI時代に決定的重要性を獲得し、現代世界文学の中核主題となる。",
    historical_context="人間概念の文化的解体期。",
    primary_source_url=WIKI_EN+"Posthumanism",
    primary_source_type="Wikipedia: Posthumanism (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ポスト・ヒューマン文学は、人間と非人間の境界を文学的に解体し、AI時代の主体概念を直接的に問う。",
         "related_ai_phenomenon":"AI主体性と人間主体性の関係"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ポスト・ヒューマニズム",
         "description":"ポスト・ヒューマニズム哲学とポスト・ヒューマン文学の理論的共有。"},
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AIと人間性",
         "description":"AI技術発展とポスト・ヒューマン文学の理論的相互作用。"}])

add(**C, name_ja="イシグロ「クララとお日さま」",
    name_en="Ishiguro 'Klara and the Sun'",
    name_original="Klara and the Sun", period_key="ポスト・ポストモダン期",
    definition="カズオ・イシグロが2021年に発表した、人工的友達(Artificial Friend)ロボットのクララを語り手とする小説。AI時代の人間とAIの関係を、ノーベル文学賞作家が正面から扱った代表作として国際的評価を獲得。",
    background="イシグロ『わたしを離さないで』(2005)以来の生命倫理的SF伝統の継承と、2010年代後半のAI技術発展への文学的応答。",
    development="現代のAI時代文学の方法論的範型となり、テレビ・映画化も検討中。",
    historical_context="2020年代初頭のAI時代の文学的応答期。",
    primary_source_url=WIKI_EN+"Klara_and_the_Sun",
    primary_source_type="Wikipedia: Klara and the Sun (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"AIロボットを語り手とする小説形式は、AI主体性の文学的探究の最前線を形成する。",
         "related_ai_phenomenon":"AI語り手と人間語り手の文学的関係"}])

add(**C, name_ja="テッド・チャン", name_en="Ted Chiang",
    name_original="Ted Chiang", period_key="ポスト・ポストモダン期",
    definition="米国のSF作家（1967生）。短篇集『あなたの人生の物語』(2002)、『息吹』(2019)で哲学的・科学的精密さを持つSF短篇を確立。映画『メッセージ』(2016)原作となり、AI・言語・自由意志を主題とする21世紀SF文学の代表作家。AI批判エッセイ「ChatGPTはWebのぼやけたJPEGである」(2023)でも著名。",
    background="アジア系米国人SF作家の現代的継承と、哲学的SF伝統の発展。",
    development="ヒューゴー賞・ネビュラ賞複数受賞し、現代SF文学の中心作家となる。AI時代の批評的思考者として影響力を持つ。",
    historical_context="2000-2020年代の哲学的SF文学の興隆期。",
    primary_source_url=WIKI_EN+"Ted_Chiang",
    primary_source_type="Wikipedia: Ted Chiang (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"テッド・チャンのAI批判エッセイは、LLM時代の創造性概念の最も影響力ある批判的議論の一つとなった。",
         "related_ai_phenomenon":"LLMと人間創造性の批判的議論"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI批評",
         "description":"テッド・チャンのAI批評はAI開発論議に直接的影響を与える。"}])

add(**C, name_ja="批判的ポストヒューマニズム",
    name_en="critical posthumanism",
    name_original="critical posthumanism", period_key="ポスト・ポストモダン期",
    definition="ロージ・ブライドッティ『The Posthuman』(2013)、ステファン・ハーブレヒター『Posthumanism: A Critical Analysis』(2013)等が定式化した、トランスヒューマニズムの技術楽観主義に対する批判的人文学運動。人間中心主義・男性中心主義・西欧中心主義を同時に解体し、AI時代の人文学を再構築する試み。",
    background="フェミニズム・ポストコロニアリズム・動物研究・環境人文学の合流。",
    development="2020年代のAI時代の人文学的応答の理論的中核として機能している。",
    historical_context="2010年代の人文学の理論的再構築期。",
    primary_source_url=WIKI_EN+"Posthumanism",
    primary_source_type="Wikipedia: Posthumanism (academic, critical strand)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"批判的ポストヒューマニズム",
         "description":"批判的ポストヒューマニズム哲学と文学批評の理論的共有。"}])

add(**C, name_ja="アルゴリズム的読解", name_en="algorithmic reading",
    name_original="algorithmic reading / distant reading",
    period_key="ポスト・ポストモダン期",
    definition="フランコ・モレッティ『Distant Reading』(2013)が定式化した、コンピュータ的・統計的手法による文学テクストの大規模解析。クローズ・リーディング（精読）と対比されるディスタント・リーディング（遠読）として、デジタル人文学(Digital Humanities)の中核方法論となった。",
    background="モレッティの世界文学論と、2000年代のデジタル人文学の興隆の合流。",
    development="2010年代のText Mining、2020年代のLLM分析の登場により、文学研究方法論として継続的拡張中。",
    historical_context="2000-2010年代のデジタル人文学の興隆期。",
    primary_source_url=WIKI_EN+"Distant_reading",
    primary_source_type="Wikipedia: Distant reading (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"アルゴリズム的読解は、人間読者と機械読者の関係を文学研究の方法論的中心に据える。",
         "related_ai_phenomenon":"LLMによる文学解析と人間解釈の関係"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"テクスト解析AI",
         "description":"アルゴリズム的読解とAIテクスト解析の方法論的共有。"}])

add(**C, name_ja="サリー・ルーニー", name_en="Sally Rooney",
    name_original="Sally Rooney", period_key="ポスト・ポストモダン期",
    definition="アイルランドの小説家（1991生）。『Conversations with Friends』(2017)、『普通の人々』(2018)、『美しい世界、どこにあるの』(2021)で、SNS時代のミレニアル世代の心理的リアリズムを確立。21世紀文学のリアリズム回帰を象徴する作家として国際的評価を獲得。",
    background="2010年代のアイルランド文学の世代交代と、SNS時代の現代心理小説の合流。",
    development="『普通の人々』BBC・Hulu共同テレビ化(2020)が世界的成功を収め、現代世界文学の中心作家の一人となる。",
    historical_context="2010-2020年代のリアリズム回帰文学の興隆期。",
    primary_source_url=WIKI_EN+"Sally_Rooney",
    primary_source_type="Wikipedia: Sally Rooney (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="major")


def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    skipped: list[str] = []
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="西欧",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid
        sf_id = db.subfield_id("lit_eu_postmodern")
        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            pkey = entry.pop("period_key", None)
            if pkey:
                entry["period_id"] = period_ids[pkey]
            # Pre-skip exact duplicates by (name_ja, region, subfield_id)
            existing = db.find_concept(entry["name_ja"], entry["region"], sf_id)
            if existing:
                skipped.append(entry["name_ja"])
                continue
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
        print(f"[c12] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c12] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        if skipped:
            print(f"[c12] skipped duplicates ({len(skipped)}): {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
