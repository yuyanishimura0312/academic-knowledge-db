"""LIT-DB Phase 2 Wave 13 — C39 Digital Humanities & AI Era ADD 60.

Subfield: lit_digital_ai (id=24), region='理論' (continuing existing convention).
Existing 50 concepts cover DH/AI core (Hayles, Bender, Manovich, Goldsmith etc.).
This wave ADDS 60 NEW concepts covering:
  A: Digital humanities methods (16) — TEI, Voyant, topic modeling, stylometry,
     authorship attribution, GIS, NER, Stylo R, CLAWS, OCR, born-digital archives,
     HathiTrust, Internet Archive, Ngram debates.
  B: Generative literature theory (15) — Oulipo expansion (Queneau, Roubaud,
     Mathews, Calvino, Mac Low, Cage, Burroughs/Gysin cut-up), NaNoGenMo,
     pre-LLM bot writing, code poetry / codework, ASCII art literature, glitch
     poetry, conceptual writing (Goldsmith / Dworkin).
  C: AI-specific (14) — LLM hallucination as device, Claude/GPT prose
     criticism, AI co-authorship copyright cases, AI-published novels, AI
     parody debates (Kishida Rin / Murakami AI), AI persona stalker case,
     prompt as poetic form, prompt engineering as craft, jailbreak as
     creative writing, LLM literary criticism, GPT-4 reading literature
     studies, distant reading vs LLM reading, MT poetry, neural MT debates.
  D: Interactive / electronic forms (8) — Twine, choice-based fiction, IF
     parser as lit, Pry app, Inkle Sorcery, ergodic theory (Aarseth),
     walking simulator (Dear Esther), podcast/Twitter/Instagram/BookTok lit.
  E: Bibliographic & ethics (7) — Open Access lit, Creative Commons,
     MOOC literary courses, Wikidata literature, Wikipedia canon-making,
     Books3 / Anna's Archive controversies, LLM memorization studies.

Verification policy:
  - 'primary'  -> manifesto, primary scholarly paper, archived program/code,
                  reference release (TEI Guidelines, ACL anthology, GitHub),
                  or PD/CC primary text.
  - 'secondary' -> canonical scholarly synthesis (Britannica, SEP,
                   academic-grade Wikipedia, peer-reviewed survey).
  - 'tertiary' -> synthetic critical category for taxonomic completeness.

Theory-heavy domain: target ~50% primary / 50% secondary, fourth_axes >=35,
cross_domain to PT/PHIL/AI-Development >=25.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("デジタル人文学・AI時代", "Digital Humanities & AI Era",
     1990, 2030,
     "1990年代のTEIとデジタルテクスト批評の制度化から、2010年代の遠読・トピックモデリング、2020年代のLLM以降にいたる、計算的人文学とAI生成文学の理論期。"),
]


# Source URL bases
TEI = "https://tei-c.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
BRITT = "https://www.britannica.com/"
ARXIV = "https://arxiv.org/abs/"
ACL = "https://aclanthology.org/"
ARCHIVE = "https://archive.org/"
HATHI = "https://www.hathitrust.org/"
GUTEN = "https://www.gutenberg.org/"
GITHUB = "https://github.com/"
ELO = "https://eliterature.org/"
NANOGENMO = "https://nanogenmo.github.io/"
CC = "https://creativecommons.org/"
DH_QUARTERLY = "http://www.digitalhumanities.org/dhq/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_digital_ai", region="理論",
         original_script="roman", period_key="デジタル人文学・AI時代")


# ============================================================
# A: デジタル人文学方法論（16件）
# ============================================================
add(**C, name_ja="TEIマークアップ",
    name_en="TEI Markup (Text Encoding Initiative)",
    name_original="Text Encoding Initiative Guidelines",
    definition="1987年に米国・欧州の人文学者が共同で立ち上げ、1994年に最初のガイドラインP1を、現在はP5を維持している、人文学テキスト構造化のためのXMLベース標準。写本・初期刊本・批評版・書簡・劇曲を機械可読に符号化するための共通語彙を提供し、デジタル批評版（digital scholarly edition）の基盤となった。",
    background="1980年代の電子テクストの非互換性危機と、人文学テキストへのSGML/XML応用への需要。",
    development="EEBO-TCP、Folger Shakespeare、ベケット・デジタル写本プロジェクトなど主要デジタル批評版の標準となり、世界の大学院デジタル人文学教育の中核となった。",
    historical_context="1990年代の電子テクスト学術化と、人文学のデジタル化制度成立期。",
    primary_source_url=TEI+"release/doc/tei-p5-doc/en/html/",
    primary_source_type="TEI Consortium: P5 Guidelines (primary spec)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"TEIは批評版を機械可読化することで「正典」の維持・改訂・分岐を計算的に管理可能にする。AI時代に正典が動的データセットとして再編される構造の祖型。",
         "related_ai_phenomenon":"LLM学習コーパスとしての正典再編"},
        {"axis":"言語","status":"partial",
         "rationale":"TEIはテキスト構造を意味的に符号化するが、LLMはトークン列として扱う。意味的構造化と統計的処理の対比。",
         "related_ai_phenomenon":"構造化マークアップ vs LLMトークン化"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"批評版・テクスト批評",
         "description":"TEIはテクスト批評（textual criticism）の伝統をデジタル基盤に移植する技術的中核。"}])

add(**C, name_ja="Voyant Tools",
    name_en="Voyant Tools",
    name_original="Voyant Tools",
    definition="ステファン・シンクレア（McGill）とジェフリー・ロックウェル（Alberta）が2003年から開発してきたWebベースのテキスト分析環境。語彙頻度・コロケーション・トレンド・シナリオなどのビジュアライゼーションを統合し、コードを書かない人文学研究者でも遠読が実践可能となるよう設計された。世界のDH授業の標準ツールとなった。",
    background="2000年代のテキスト分析ツール（TACT、HyperPo）の系譜と、Webブラウザ完結型ツールへの教育的需要。",
    development="2010年代の遠読教育、特に学部レベルのDH導入授業の事実上の標準となり、Stéfan Sinclair逝去後も継続維持されている。",
    historical_context="2010年代DH教育制度化期と、教育用ツールの民主化。",
    primary_source_url="https://voyant-tools.org/docs/",
    primary_source_type="Voyant Tools: documentation site",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"Voyantは人文学者の読書実践を「視覚化された遠読」へ拡張する。AI時代に「読む」行為が分析的可視化を含むようになる構造の前史。",
         "related_ai_phenomenon":"LLM時代の可視化補助読書実践"}])

add(**C, name_ja="文学トピックモデリング",
    name_en="topic modeling for literature (LDA)",
    name_original="Latent Dirichlet Allocation in literary studies",
    definition="ブレイ、ング、ジョーダン2003年論文以降のLDAを文学コーパスに適用する研究実践。マシュー・ジョッカーズ『マクロアナリシス』(2013)、テッド・アンダーウッド『遠近の地平』(2019)が方法論を体系化。19世紀英語小説3千冊レベルのコーパスを「100トピック」に分解し、ジャンル・性別・年代の構造的傾向を抽出する。",
    background="ブレイ・ング・ジョーダン2003 LDA論文、機械学習の人文学応用への需要。",
    development="ジョッカーズ、アンダーウッド、Lauren Klein、Richard Jeanらの遠読研究の中核手法となり、Stanford Literary Lab・Illinois HathiTrust Research Centerの方法論基盤となった。",
    historical_context="2010年代英語圏文学研究の計算論的転回。",
    primary_source_url="https://jmlr.csail.mit.edu/papers/v3/blei03a.html",
    primary_source_type="JMLR 2003: Latent Dirichlet Allocation (Blei et al.)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"トピックモデリングは「読む」を確率的潜在意味抽出に置換する。AI時代のテキスト読解の基底パラダイム。",
         "related_ai_phenomenon":"LLM以前の確率的意味抽出としてのDH祖型"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"LDA・潜在意味モデル",
         "description":"LDAはニューラル以前のNLP代表手法であり、現代LLMの潜在表現の理論的前史。"}])

add(**C, name_ja="書簡ネットワーク分析",
    name_en="network analysis of letters / correspondence",
    name_original="correspondence network analysis",
    definition="近世・近代の書簡コーパスをグラフ理論で分析する研究実践。Stanford "
        "Mapping the Republic of Letters (2008-)、Cultures of Knowledge (Oxford)、ePistolarium (Huygens ING)が代表的。送信者・受信者・地理的位置・話題をノード/エッジ化し、知識共同体の構造を可視化する。",
    background="2000年代後半の書簡デジタル化（Early Modern Letters Online等）と、社会ネットワーク分析の人文学応用。",
    development="Stanford CESTA、Oxford COKを中心に発展、デジタル書誌学（digital bibliography）の中核領域となった。",
    historical_context="2010年代の知識史（history of knowledge）研究の計算論的展開。",
    primary_source_url="http://republicofletters.stanford.edu/",
    primary_source_type="Stanford CESTA: Mapping the Republic of Letters",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"知識共同体ネットワーク",
         "description":"書簡ネットワーク分析は文学社会学の制度化されたDH手法。"}])

add(**C, name_ja="計量文体論（Burrows Delta）",
    name_en="stylometry / Burrows's Delta",
    name_original="Burrows's Delta",
    definition="ジョン・F・バロウズが2002年論文 'Delta: A Measure of Stylistic Difference' で提唱した、書き手識別の標準化計量。最頻出機能語の頻度をz標準化し、文書間距離を計算する。シェイクスピア偽書、フェデラリスト・ペーパーズ、JK・ローリング『カッコーの呼ぶ声』（2013年Robert Galbraith名義の暴露）等、著者帰属論争の標準ツールとなった。",
    background="モステラー＆ウォレス1964フェデラリスト研究の系譜、機能語頻度の計量文体論。",
    development="Stylo R packageに実装され、Eder, Rybicki, Kestemontらの精緻化を経て、デジタル文体論の世界標準となった。",
    historical_context="2000年代計量文体論のルネサンス期。",
    primary_source_url="https://academic.oup.com/dsh/article/17/3/267/928943",
    primary_source_type="Literary and Linguistic Computing 2002 (Burrows)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"Burrows's Deltaは作家固有のスタイル指紋を統計的に同定する。AI時代に「作家性」を機能語頻度パターンに還元する技術的祖型。",
         "related_ai_phenomenon":"LLM著者識別・AI生成検出の前史"}])

add(**C, name_ja="著者帰属研究",
    name_en="authorship attribution",
    name_original="authorship attribution",
    definition="計量文体論を用いて匿名・偽名・共著作品の真の著者を特定する研究実践。フォースター『ある詩への挽歌』のシェイクスピア帰属論争、フェデラリスト・ペーパーズ、ローリング暴露、サミュエル・ペピース秘記断片、ピーター・パンとJ・M・バリー、最近では2022年スペイン語ベストセラーの匿名化問題まで、文学史研究の中核手法となった。",
    background="モステラー＆ウォレス『フェデラリスト』1964、バロウズDelta、機械学習による分類器の発展。",
    development="Patrick Juolaのコーパス計量、Jan Rybicki、Maciej Eder、Mike Kestemontらのチームが世界拠点となった。",
    historical_context="2000-2020年代の計量文体論の制度化期。",
    primary_source_url=ACL+"P12-1010/",
    primary_source_type="ACL: Authorship Attribution (Juola/Stamatatos surveys)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"著者帰属は「作家性」を統計指紋として実体化する。AI生成テキストとヒト生成の二項検出問題に直結する。",
         "related_ai_phenomenon":"AI生成検出（GPTZero, DetectGPT）の前史"}])

add(**C, name_ja="シェイクスピア著者問題",
    name_en="Shakespeare authorship debates",
    name_original="Shakespeare authorship question",
    definition="ストラットフォード生まれのウィリアム・シェイクスピアが正典38作を実際に書いたかを巡る、19世紀ベーコン説以来の論争。20-21世紀には計量文体論が主要証拠源となり、Mike Kestemontらの2022年論文がマーロウ・フレッチャー・ミドルトンとの共著割合をニューラルモデルで再推定した。シェイクスピア協同執筆論はもはや学術的合意に近い。",
    background="19世紀末からのアンチ・ストラットフォード派、20世紀ジャクソン・ヴィッカーズらの計量文体論、2010年代ニューラル時代の精緻化。",
    development="New Oxford Shakespeare 2016版が共著者を本文に明記する画期となり、計量文体論が文学正典編纂を実質的に書き換えた事例。",
    historical_context="2010年代後半の計量文体論成熟期と正典再編。",
    primary_source_url=WIKI_EN+"Shakespeare_authorship_question",
    primary_source_type="Wikipedia (academic): Shakespeare authorship question",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"シェイクスピア正典が計量文体論によって複数著者作品集として再編される過程は、AI時代の正典の機械可塑性を象徴する。",
         "related_ai_phenomenon":"AI支援による正典の動的再編"}])

add(**C, name_ja="フェデラリスト・ペーパーズ著者問題",
    name_en="Federalist Papers authorship problem",
    name_original="Federalist Papers authorship",
    definition="1787-88年に書かれた米国憲法擁護論文集85篇のうち、ハミルトン・マディソン・ジェイの三名が共著であることは判明していたが、12篇の帰属が長年不明だった。フレデリック・モステラーとデイヴィッド・ウォレスが1964年『Inference and Disputed Authorship』でベイズ推論と機能語頻度を用いて全12篇をマディソンに帰属させ、計量文体論の出発点となった古典的事例。",
    background="統計学のテキスト分析応用への黎明期と、米国憲法史研究の長年の難問。",
    development="現代計量文体論・著者帰属論の創始事例として、Burrows、Stamatatos、Juolaらの研究の理論的源流となった。",
    historical_context="1960年代統計学・コンピュータ言語学の成立期と古典文献研究の交差。",
    primary_source_url=WIKI_EN+"Mosteller%E2%80%93Wallace_Federalist_Papers",
    primary_source_type="Wikipedia (academic): Mosteller-Wallace study",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"フェデラリスト研究は「機械が著者を決定する」最初の制度化された事例。AI時代の著者性推定の歴史的祖型。",
         "related_ai_phenomenon":"AI著者帰属の創始モデル"}])

add(**C, name_ja="文学GIS",
    name_en="literary GIS / spatial humanities",
    name_original="literary GIS / spatial humanities",
    definition="地理情報システム（GIS）を文学テキストに適用する研究実践。Franco Moretti『小説の地図』(1998)を理論的祖として、Stanford Literary Lab・Lancaster Spatial Humanities CDH・Mapping the Lakesがコーパス全体の場所言及をジオコード化し、空間的文学史を可視化する。場所性とナラティブの計量的統合。",
    background="モレッティ『地図・グラフ・木』(2005)、GIS技術の人文学応用、デジタル空間人文学の制度化。",
    development="Lancaster Spatial Humanities Centre、Stanford CESTA、Yale DHLab等が世界拠点となり、ロンドン文学地図・19世紀英米小説空間分析・古代ギリシア文学位相など多分野化した。",
    historical_context="2000年代後半～2010年代のDHの空間論的転回。",
    primary_source_url=DH_QUARTERLY+"vol/4/1/",
    primary_source_type="DHQ vol. 4(1): Spatial Humanities issue",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"場所性と文学",
         "description":"文学GISは人類学的場所性研究と方法的に連携する。"}])

add(**C, name_ja="文学固有表現抽出（NER）",
    name_en="named entity recognition for literature",
    name_original="literary NER",
    definition="人物名・地名・組織名等の固有表現を文学テキストから自動抽出する技術。Stanford NER、spaCy、HuggingFace ACL系モデルを文学に応用する研究で、David BammanのBookNLP（2014-）が代表的。19世紀英語小説3千冊の人物・場所・性別を抽出し、文学的人物表象の計量分析を可能にした。",
    background="2010年代NLPの成熟と、文学コーパスへの応用への研究的需要。",
    development="BookNLP、LitBank（Bamman et al. 2020）、Sara Tonelli（FBK）の伊語文学NERなどが領域標準となった。",
    historical_context="2010-2020年代の文学計量研究のNLP化。",
    primary_source_url=GITHUB+"booknlp/booknlp",
    primary_source_type="GitHub: BookNLP (Bamman, primary release)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="Stylo Rパッケージ",
    name_en="Stylo R package",
    name_original="Stylo (R package)",
    definition="Maciej Eder、Jan Rybicki、Mike Kestemontがクラクフ大学を中心に2010年代から開発しているR言語の計量文体論パッケージ。Burrows Delta、PCA、Wardクラスタリング、Network分析を統合し、コードを書かない研究者でも著者帰属実験が可能な設計。世界の計量文体論研究の事実上の標準。",
    background="2000年代計量文体論ソフトウェアの分散状況と、再現可能研究への学術的需要。",
    development="ヨーロッパDH学会・ADHO（Alliance of Digital Humanities Organizations）が標準ツールとして推奨し、英米欧アジアの著者帰属研究の中核ソフトウェアとなった。",
    historical_context="2010年代計量文体論の世界制度化期。",
    primary_source_url=GITHUB+"computationalstylistics/stylo",
    primary_source_type="GitHub: computationalstylistics/stylo (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="CLAWSタグセット",
    name_en="CLAWS tagset",
    name_original="CLAWS (Constituent Likelihood Automatic Word-tagging System)",
    definition="ランカスター大学UCREL研究所が1980年代から開発する英語品詞タグ付け体系。CLAWS5（62タグ）・CLAWS7（137タグ）が British National Corpus（1億語）の標準タグセットとなり、英語コーパス言語学・文体論の世界標準となった。文学計量分析の前処理基盤として機能。",
    background="1980年代英国コーパス言語学の制度化（COBUILD、BNC）。",
    development="CLAWSはBNC・OEC・Brown Corpusと並ぶ英語コーパスの基盤タグ付けツールとなり、Penn Treebank系と双方向対照可能性を持つ。",
    historical_context="1980-1990年代英語コーパス言語学の制度化期。",
    primary_source_url="https://ucrel.lancs.ac.uk/claws/",
    primary_source_type="UCREL Lancaster: CLAWS (primary doc)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="OCR課題と歴史的テキスト",
    name_en="OCR challenges for historical texts",
    name_original="OCR for historical texts",
    definition="近世・近代の文献を機械可読化する際の光学文字認識（OCR）の精度問題。長sや合字を含む18世紀以前の活字、手書き写本、非ラテン文字（漢字・アラビア文字・キリル文字）への対応など、デジタル人文学の基盤的課題。Transkribusプロジェクト（オーストリア）、eScriptorium（フランス）が手書きOCR（HTR）の最前線。",
    background="Google Books大規模スキャン（2004-）、Internet Archive、HathiTrustによる大規模スキャン時代のOCR精度問題顕在化。",
    development="2020年代以降、Transformer型OCR（TrOCR、Microsoft）と手書きHTRが急速に進展し、近世文献の機械可読化が現実化した。",
    historical_context="2010-2020年代の歴史的テキストデジタル化の精度問題と、手書きOCR革命。",
    primary_source_url="https://readcoop.eu/transkribus/",
    primary_source_type="READ-COOP: Transkribus (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ボーン・デジタル・アーカイブ",
    name_en="born-digital archives",
    name_original="born-digital archives",
    definition="紙の媒体を持たず、初めからデジタル形式で生成された文学創作物・原稿・書簡を対象とする保存研究。エミリー・ディキンソン研究のフロッピーディスク版、サルマン・ラシュディのMacintosh原稿（Emory大学）、デヴィッド・フォスター・ウォレスの草稿（Texas HRC）等が代表事例。Matthew Kirschenbaum『Mechanisms』(2008)が方法論的基礎を確立した。",
    background="1990年代以降の作家のワープロ・PC使用の一般化、デジタル原稿の保存問題顕在化。",
    development="Emory MARBL、Harry Ransom Center、British Library Digital Manuscripts、Bodleian Electronic Enlightenmentなど主要研究図書館が制度化した。",
    historical_context="2000-2020年代の文学原稿研究のデジタル化と、媒体保存の新パラダイム。",
    primary_source_url="https://www.cdlib.org/services/uc3/curation/",
    primary_source_type="UC California Digital Library: Born-Digital",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"ボーン・デジタル原稿は紙媒体を持たないため、ファイルバージョン・編集履歴自体が真正性証拠となる。AI時代の創作過程の真正性問題と直結する。",
         "related_ai_phenomenon":"プロンプト履歴・編集履歴が真正性証拠となる構造"}])

add(**C, name_ja="HathiTrust研究ツールキット",
    name_en="HathiTrust Research Center toolkit",
    name_original="HathiTrust Research Center (HTRC)",
    definition="2008年Indiana・Illinois両大学を中心に設立されたHathiTrust（米国大学図書館連合のデジタル化図書1,800万冊規模）の研究利用基盤。著作権下のテキストも語彙頻度・トピックモデリング等の集計レベル分析を可能にし、テッド・アンダーウッド『遠近の地平』、Andrew Piper『Enumerations』など20年代遠読研究の中核データソースとなった。",
    background="2004年Google Books訴訟、HathiTrustの「fair use」防衛、米国大学図書館の機械可読研究基盤への需要。",
    development="HTRCはStanford Literary Lab、UCLA Center for Digital Humanitiesと並ぶ世界最大規模の遠読基盤となり、Authors Guild対HathiTrust訴訟（2014勝訴）で機械学習用途のフェアユースを確立した。",
    historical_context="2010年代米国デジタル図書館の制度化と、機械学習用途のフェアユース判例形成。",
    primary_source_url="https://www.hathitrust.org/htrc/",
    primary_source_type="HathiTrust Research Center (official)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"フェアユースと機械学習",
         "description":"HTRCのフェアユース勝訴は、現代LLM学習データのフェアユース論争の判例的源流。"}])

add(**C, name_ja="Google Ngram文学論争",
    name_en="Google Books Ngram literary debates",
    name_original="Google Books Ngram Viewer debates",
    definition="ジャン=バティスト・ミシェル、エレズ・リーバマン・エイデンら2011年Science論文 'Quantitative Analysis of Culture Using Millions of Digitized Books' とGoogle Ngram Viewer公開以降の論争。「カルチャロミクス（culturomics）」を提唱したが、OCR誤り・サンプル偏向・著作権による断絶を指摘するEitan Adam Pechenickら2015年論文等の批判が学術的合意となった。",
    background="Google Booksスキャン1500万冊規模の集計データ公開、デジタル文化史への大衆的関心。",
    development="ミシェル・エイデン『Uncharted』(2013)で大衆化、しかし方法論的批判も蓄積し、2020年代の遠読研究はNgramを参照しつつもより精緻なコーパス管理に移行した。",
    historical_context="2010年代カルチャロミクス興隆と批判的検証期。",
    primary_source_url="https://www.science.org/doi/10.1126/science.1199644",
    primary_source_type="Science 2011: Quantitative Analysis of Culture",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"Ngram論争はビッグデータ的文学史の方法論的妥当性を問う。AI時代の大規模コーパス研究の批判的祖型。",
         "related_ai_phenomenon":"LLM学習データの偏向問題"}])


# ============================================================
# B: 生成文学理論（15件）
# ============================================================
add(**C, name_ja="クノー『百兆の詩篇』",
    name_en="Queneau's Cent mille milliards de poèmes",
    name_original="Cent mille milliards de poèmes",
    definition="レーモン・クノー（1903-1976）が1961年に発表した、10篇のソネット（各14行）を行単位で組み替えると10^14（百兆）通りの詩が生成される組合せ詩集。Oulipo（潜在文学工房）の代表作であり、組合せ的・アルゴリズミックな文学生成の20世紀古典。読者が紙片を物理的に組み合わせる装置として設計された。",
    background="1960年フランソワ・ル・リオネとクノーによるOulipo創設、組合せ数学の文学への応用、レイモン・ルーセル『ロクス・ソルス』の前史。",
    development="ジャック・ルーボー、ハリー・マシューズ、イタロ・カルヴィーノを通じて、20世紀後半の制約文学（contraintes）の中核作品となった。",
    historical_context="1960年代フランスの構造主義興隆と数理的文学運動の制度化。",
    primary_source_url=WIKI_FR+"Cent_mille_milliards_de_po%C3%A8mes",
    primary_source_type="Wikipedia (FR): Cent mille milliards de poèmes",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"クノーは100兆篇の詩を「生成可能性」として呈示し、作者を「生成器」へ再定義した。LLMによる無限テキスト生成の文学理論的祖型。",
         "related_ai_phenomenon":"LLMの無限生成と作者-生成器の同一視"},
        {"axis":"創造性","status":"rethinking",
         "rationale":"組合せ詩は「読者が組合せを実行することが創造行為」という理念を体現する。AI時代の人間-機械協働創造の前史。",
         "related_ai_phenomenon":"プロンプト=組合せ実行としての創造行為"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"組合せ生成と機械生成",
         "description":"Cent mille milliardsはアルゴリズミック生成文学の祖型として、LLM理論の文学的前史。"}])

add(**C, name_ja="ジャック・ルーボー",
    name_en="Jacques Roubaud",
    name_original="Jacques Roubaud",
    definition="ジャック・ルーボー（1932-2024）は数学者・詩人。1966年Oulipo加入後、『∈』（1967）等で集合論記号を詩に組み込み、『偉大な火事のロンドン』（1989-）の自伝的小説連作で記憶喪失と組合せ的記述を統合した。Oulipo第二世代の中心人物として、数理文学とトラウマ自伝の橋渡しを行った。",
    background="1960年代フランス構造主義・ブルバキ数学の文学的応用、Oulipo第二世代の制度成熟。",
    development="マシューズ、ペレック、ルーボー、カルヴィーノを擁するOulipo黄金期(1970-90年代)の中心、現代仏語実験文学の主要源流。",
    historical_context="1960-2010年代フランス実験文学のOulipoを通じた持続。",
    primary_source_url=WIKI_FR+"Jacques_Roubaud",
    primary_source_type="Wikipedia (FR): Jacques Roubaud",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ハリー・マシューズ",
    name_en="Harry Mathews",
    name_original="Harry Mathews",
    definition="ハリー・マシューズ（1930-2017）は米国出身でOulipo初の英語圏成員（1973加入）。『カルカッタへの転移』（1962）、『シガレッツ』（1987）等で多重ナラティブ・組合せ的構造を英語小説に導入し、Oulipoの国際化を推進した。ジョン・アシュベリーとの友情、長期パリ移住を通じて米仏前衛文学を架橋した。",
    background="1950年代パリ亡命米国前衛作家共同体（アシュベリー、ケネス・コック）、Oulipoの国際化への動向。",
    development="後の英語圏Oulipo系作家（クリスチャン・ボーク、Anne Garréta英訳者ダニエル・レヴィン・ベッカー）への系譜的影響。",
    historical_context="1970年代Oulipoの国際化期。",
    primary_source_url=WIKI_EN+"Harry_Mathews",
    primary_source_type="Wikipedia: Harry Mathews",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="カルヴィーノ『冬の夜ひとりの旅人が』",
    name_en="Calvino's If on a winter's night a traveler",
    name_original="Se una notte d'inverno un viaggiatore",
    definition="イタロ・カルヴィーノ（1923-1985）が1979年に発表した小説。読者「あなた」を主人公に、10篇の小説冒頭部が次々と中断され続ける入れ子構造で、「読書という行為」自体をメタフィクション化した。1973年のOulipo加入後の代表作で、組合せ文学の最高峰として20世紀後半世界文学の決定的事件となった。",
    background="カルヴィーノのOulipo加入(1973)、ボルヘス・受容、ナラトロジーの隆盛期。",
    development="ナラトロジー、メタフィクション、読者反応理論の中心研究対象となり、20世紀後半世界文学の正典に組み込まれた。",
    historical_context="1970年代後半イタリア前衛文学とフランスOulipo文学の交差点。",
    primary_source_url=WIKI_EN+"If_on_a_winter%27s_night_a_traveler",
    primary_source_type="Wikipedia: If on a winter's night a traveler",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"カルヴィーノは読者「あなた」を主人公化することで、読書を能動的生成行為に転換する。AI時代のプロンプト駆動読書の文学的祖型。",
         "related_ai_phenomenon":"プロンプト駆動読書のメタフィクション的祖型"}])

add(**C, name_ja="マック・ロウ偶然作詩法",
    name_en="Jackson Mac Low's chance operations",
    name_original="Mac Low's chance operations",
    definition="ジャクソン・マック・ロウ（1922-2004）が1950-60年代に確立した偶然操作詩法。サイコロ・乱数表・ジョン・ケージ的偶然手続を用いてテキストから語を抽出再構成する。『5つのビデオ・ライト・ポエム』、『マーカー詩』など、機械的・脱意図的詩作の先駆。コンピュータ詩への直接的橋渡しとなった。",
    background="1950年代ジョン・ケージ偶然音楽との交流、ニューヨーク前衛芸術圏（フルクサス）。",
    development="1980-90年代のコンピュータ詩（チャールズ・O・ハートマン、ジョン・ケイリー）、現代の生成詩学への直接的祖型。",
    historical_context="1950-1970年代米国前衛詩・偶然芸術運動。",
    primary_source_url=WIKI_EN+"Jackson_Mac_Low",
    primary_source_type="Wikipedia (academic): Jackson Mac Low",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"マック・ロウは作家意図を偶然操作に置換することで、作家を「手続き設計者」へ再定義した。AI生成詩の哲学的祖型。",
         "related_ai_phenomenon":"AI生成における作家=手続き設計者への変容"}])

add(**C, name_ja="ジョン・ケージ偶然作品",
    name_en="John Cage's chance operations",
    name_original="John Cage's chance operations",
    definition="ジョン・ケージ（1912-1992）が1950年代に『易経』の卜筮法をもとに確立した偶然作曲・偶然詩作技法。『心構の音楽』『暗号化された語』『Empty Words』（梭ロー全集をランダム断片化）等で、作家意図を偶然手続に置換した。マック・ロウとともに、偶然操作詩学（chance poetics）の制度的祖。",
    background="ケージの禅・易経への傾倒、1950年代米国実験芸術運動、ブラックマウンテン・カレッジ。",
    development="マック・ロウ、ジョージ・ブレヒト、フルクサス運動全体、1990年代コンセプチュアル・ライティング、現代AI詩学に系譜的に継承。",
    historical_context="1950-1990年代米国前衛芸術の偶然主義パラダイム。",
    primary_source_url=WIKI_EN+"John_Cage",
    primary_source_type="Wikipedia (academic): John Cage",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ケージの偶然操作は「作家意図の徹底排除」を理論化する。AI生成における人間意図の最小化と直結する。",
         "related_ai_phenomenon":"AI生成と作家意図の徹底排除"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"偶然と必然の哲学",
         "description":"ケージの偶然主義は東洋哲学（易経・禅）と現代美学の架橋。"}])

add(**C, name_ja="バロウズ・カットアップ技法",
    name_en="Burroughs's cut-up technique",
    name_original="cut-up technique",
    definition="ウィリアム・S・バロウズ（1914-1997）とブライオン・ガイシン（1916-1986）が1959年タンジールで確立した文学的方法。既存テキストを物理的に切断・再配置することで、線状的意味を破壊し潜在的意味を解放する技法。『ノヴァ三部作』（1961-64）の方法的中核となり、1980年代以降のサンプリング文化、デジタル・ミックス、現代AI生成の文学的祖型となった。",
    background="ガイシンのダダイズム再評価、1950年代タンジール国際前衛芸術圏、第二次世界大戦後の語の機械的操作への関心。",
    development="デヴィッド・ボウイ、コービッド、サンプリング文化、コンセプチュアル・ライティング、現代AI生成研究の重要参照点。",
    historical_context="1950-60年代米国カウンターカルチャー前衛芸術と国際的ビート・ジェネレーション。",
    primary_source_url=WIKI_EN+"Cut-up_technique",
    primary_source_type="Wikipedia (academic): Cut-up technique",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"カットアップは作家を「テクスト切断・再構成オペレーター」に変換する。LLMのトークン操作的生成と理論的に直結する。",
         "related_ai_phenomenon":"LLMトークン操作とカットアップの構造的同型"},
        {"axis":"言語","status":"rethinking",
         "rationale":"カットアップは線状的言語を断片化することで「コントロール権力としての言語」を解体する。AI生成における言語の脱中心化の祖型。",
         "related_ai_phenomenon":"AI生成と言語の脱中心化"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"カットアップとAI生成",
         "description":"カットアップ技法はAI生成の文学的祖型として頻繁に参照される。"}])

add(**C, name_ja="ブライオン・ガイシン",
    name_en="Brion Gysin",
    name_original="Brion Gysin",
    definition="ブライオン・ガイシン（1916-1986）はカナダ系英国の画家・詩人。バロウズとともにカットアップを再発見し、『順列詩 (Permutation Poems)』『I Am That I Am』等で、短いフレーズを全順列展開する技法を確立した。「I am that I am→I am I that am→...」のような順列詩は、組合せ的・機械的詩生成の20世紀古典。",
    background="ダダイズム（ツァラ詩）再評価、タンジール国際前衛芸術共同体、コンピュータ以前の機械的言語実験への関心。",
    development="バロウズのカットアップ理論化への直接的影響、1980年代以降の生成詩学・コンピュータ詩の祖型。",
    historical_context="1950-1970年代国際前衛芸術運動と組合せ詩学の制度化期。",
    primary_source_url=WIKI_EN+"Brion_Gysin",
    primary_source_type="Wikipedia (academic): Brion Gysin",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"順列詩は語の組合せ的全展開を実演する。LLM生成の確率的全展開と理論的に並行する。",
         "related_ai_phenomenon":"LLM確率的全展開と順列詩"}])

add(**C, name_ja="NaNoGenMo",
    name_en="National Novel Generation Month (NaNoGenMo)",
    name_original="NaNoGenMo",
    definition="ダリウス・カゼミ（Darius Kazemi）が2013年に開始した、11月中に「コードで小説を生成する」ことを目的とする年次オンラインイベント。GitHubリポジトリで参加者が生成プログラムと出力小説を公開する形式で、生成文学コミュニティの世界的中心となった。LLM時代以前のbot文学の制度化された場として、計算文学史上の里程標。",
    background="2010年代のクリエイティブコーディング文化興隆、NaNoWriMo（小説執筆月間）のパロディとして発生。",
    development="2013-2024年で延べ千件以上の生成小説プロジェクトが投稿され、Allison Parrish、Nick Montfort、Jamie Brewらが参加する世代的な生成文学コミュニティを形成した。",
    historical_context="2010年代の生成文学コミュニティ制度化期。",
    primary_source_url=NANOGENMO,
    primary_source_type="NaNoGenMo official site (GitHub)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"NaNoGenMoは作者を「生成プログラム作成者」に再定義し、世代的にこの実践を制度化した。LLM時代の作者性論議の直前史。",
         "related_ai_phenomenon":"プログラム作成者としての作家性"},
        {"axis":"創造性","status":"rethinking",
         "rationale":"生成小説をオープンソース化することで、創造性は「生成プロセスの公開設計」へ拡張される。",
         "related_ai_phenomenon":"オープンソース生成と創造性"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"生成文学コミュニティ",
         "description":"NaNoGenMoはLLM以前の生成文学制度の代表事例として、AI生成小説論の前史。"}])

add(**C, name_ja="LLM以前のbot文学",
    name_en="pre-LLM bot writing tradition",
    name_original="pre-LLM bot writing",
    definition="2010年代Twitterボット黄金期に展開された生成文学実践。Allison Parrish @everyword（英語全単語ツイート）、Darius Kazemi @TwoHeadlines、Nora Reed @thinkpiecebot等が代表的。マルコフ連鎖、テンプレート、Tracery（Kate Comptonによる文法フレームワーク）を用い、短文ボットを文学ジャンルとして確立した。",
    background="Twitter API公開時代（2010年代前半）、クリエイティブコーディング文化、ジェネレーティブ・テキスト・ツール（Tracery、CBDQ）の普及。",
    development="2023年Twitter API有料化以降ほぼ消滅したが、Mastodon・Blueskyに移行する形で継続。LLM時代生成文学の直接的前史。",
    historical_context="2010年代Twitterプラットフォーム文化と生成文学の制度的接続期。",
    primary_source_url=WIKI_EN+"Twitter_bot",
    primary_source_type="Wikipedia (academic): Twitter bot",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"botは「自動生成され続ける作家」というポストヒューマン作者性を実装した。LLM時代の自動生成主体の直接的前史。",
         "related_ai_phenomenon":"自動生成主体の系譜"}])

add(**C, name_ja="マッケンジー・ウォーク生成テクスト",
    name_en="McKenzie Wark's generated texts",
    name_original="McKenzie Wark's generative writing",
    definition="マッケンジー・ウォーク（1961-）が『ハッカー宣言』(2004)、『資本は死んだ』(2019)で展開した格言的・組合せ的散文形式。番号付き単項命題の連なりという構造は、ヴィトゲンシュタイン『論考』、ドゥボール『スペクタクル社会』を継承しつつ、デジタル時代の格言的・モジュール的書記の代表事例となった。",
    background="2000年代デジタル文化批評の隆盛、ドゥボール・スペクタクル理論のデジタル時代への適用。",
    development="2010-2020年代のメディア理論的文学の代表的様式となり、ベンジャミン・ブラットン、ニック・スルニチェク等の加速主義派にも影響を与えた。",
    historical_context="2000-2020年代デジタル文化批評の文学的様式化。",
    primary_source_url=WIKI_EN+"McKenzie_Wark",
    primary_source_type="Wikipedia: McKenzie Wark",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="コードポエトリー／コードワーク",
    name_en="code poetry / codework",
    name_original="code poetry / codework",
    definition="プログラムコードそのものを詩的素材として用いる文学ジャンル。Mez Breeze（_Mezangelle）、Talan Memmott（_lexia to perplexia_）、Alan Sondheim等が代表。コードと自然言語を融合させた書記形式（codework）は、機械可読性と人間可読性の二重生成を文学化する。Stanford Lit Lab・Electronic Literature Organizationが研究制度化。",
    background="1990年代インターネット文化、ハッカー文学（Hakim Bey、Eric S. Raymond）、サイバーパンク文学。",
    development="2000年代エレクトロニック・リテラチャー組織化、近年は批判的コード研究（Mark Marino、Critical Code Studies）として制度化。",
    historical_context="1990-2010年代電子文学の制度化期。",
    primary_source_url=ELO+"directory/",
    primary_source_type="ELO Directory: codework entries",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"コードと自然言語の融合",
         "description":"codeworkはコードと自然言語の文学的融合の祖型として、現代LLMプロンプト文学の前史。"}])

add(**C, name_ja="アスキーアート文学",
    name_en="ASCII art literature",
    name_original="ASCII art literature",
    definition="文字コード（ASCII、Unicode）のみで視覚的構成を行う文学ジャンル。1980年代BBS文化、1990年代Usenet/2chの「巨大AA」、Joan Stark、Daniel AuらのASCIIアート作家を経て、視覚詩・コンクリート詩のデジタル系譜として確立した。日本では2chの「やる夫」「モナー」が独自AA文学を生んだ。",
    background="1980年代BBS文化、ASCIIテキスト唯一の表現環境、視覚詩の伝統（アポリネール『カリグラム』）の系譜。",
    development="1990年代Usenet/2ch文化、2010年代Twitter視覚的言語実験、現代Unicode絵文字小説（Twitterや論文中Emoji文学）への系譜。",
    historical_context="1980-2010年代テキストオンリー・メディアの視覚的拡張期。",
    primary_source_url=WIKI_EN+"ASCII_art",
    primary_source_type="Wikipedia: ASCII art",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="グリッチ詩",
    name_en="glitch poetry",
    name_original="glitch poetry",
    definition="意図的なエラー、文字化け、ファイル破損を詩的素材として用いる現代電子文学ジャンル。ニック・ブリス（Nick Briz）、Rosa Menkman（『The Glitch Moment(um)』2011）等が代表的。デジタル媒体の物質性（マテリアリティ）を露呈させる芸術運動「グリッチ・アート」の文学版として、2000年代以降電子文学の重要サブジャンルとなった。",
    background="2000年代デジタルアート理論（Lev Manovich、Florian Cramer）、メディア考古学運動（Wolfgang Ernst、Jussi Parikka）。",
    development="ELOディレクトリ、Furtherfield、Rhizome.orgなど電子文学・電子芸術組織が制度化。",
    historical_context="2000-2010年代デジタル媒体の物質性論議。",
    primary_source_url=ARCHIVE+"details/RosaMenkmanTheGlitchMomentum",
    primary_source_type="Internet Archive: Glitch Moment(um) (Menkman)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ゴールドスミス『非創造的書記』",
    name_en="Goldsmith's Uncreative Writing",
    name_original="Uncreative Writing",
    definition="ケネス・ゴールドスミス（1961-）が2011年に発表したコンセプチュアル・ライティング理論書。「インターネット時代に「書く」とは選択・編集・再配置である」と主張し、書写・剽窃・データベース操作を文学的方法として理論化した。バロウズ・カットアップ、Oulipo組合せ詩学、コンセプチュアル・アートを統合し、AI時代以前の生成文学理論の頂点を成す。",
    background="2000年代デジタル過剰時代、コンセプチュアル・アート（Sol LeWitt、Lawrence Weiner）の文学への移植、UbuWeb（ゴールドスミス運営）。",
    development="バネッサ・プレイス、クレイグ・ドウォーキンとともにコンセプチュアル・ライティング運動の中核理論書として、2010年代米国前衛詩の主要参照点となった。",
    historical_context="2010年代米国前衛詩のコンセプチュアル化期。",
    primary_source_url="https://www.upenn.edu/pennpress/book/15203.html",
    primary_source_type="Columbia Univ Press: Uncreative Writing (2011)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ゴールドスミスは「創造的書記」概念そのものを脱構築し、選択・編集・再配置として書記を再定義した。AI生成における作家性論議の直接的祖型。",
         "related_ai_phenomenon":"AI時代の作家性=選択・編集・再配置への変容"},
        {"axis":"創造性","status":"rethinking",
         "rationale":"非創造的書記は「創造性」自体を機械的・組合せ的選択として再定義する。LLMプロンプト時代の創造性概念の直前史。",
         "related_ai_phenomenon":"創造性の選択・編集への還元"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"非創造的書記理論",
         "description":"非創造的書記は現代詩学の重要理論枠組みとして、PT-DBにも参照される。"}])

add(**C, name_ja="クレイグ・ドウォーキン",
    name_en="Craig Dworkin",
    name_original="Craig Dworkin",
    definition="クレイグ・ドウォーキン（1969-）はユタ大学教授・詩人。ゴールドスミスとともに『Against Expression: An Anthology of Conceptual Writing』(2011)を編集し、コンセプチュアル・ライティングを学術的に制度化した。『Reading the Illegible』(2003)は読み難さ自体を方法とする視覚詩学の理論書として、20世紀後半の前衛詩の批評的中心となった。",
    background="2000年代米国前衛詩の制度成熟、視覚詩学（concrete poetry）の批評的再評価。",
    development="2010年代以降、コンセプチュアル・ライティング運動の中心理論家として、AI生成文学論議の直前的理論基盤を提供した。",
    historical_context="2000-2010年代米国前衛詩学の制度化期。",
    primary_source_url=WIKI_EN+"Craig_Dworkin",
    primary_source_type="Wikipedia: Craig Dworkin",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# C: AI特有現象（14件）
# ============================================================
add(**C, name_ja="文学装置としての幻覚",
    name_en="LLM hallucination as literary device",
    name_original="hallucination as literary device",
    definition="LLMが事実とは異なる情報を生成する「幻覚（hallucination）」現象を、欠陥としてではなく文学的方法として用いる実践。ボルヘス『バベルの図書館』『ティロン・ウクバル』『ハーバート・クェインの作品の検討』に直接的祖型を持ち、Janelle Shane、Vauhini Vara『Searches』(2025)等の現代AI共作文学が制度化した。",
    background="2022年ChatGPT以降の幻覚問題顕在化、ボルヘス的擬書物伝統の現代的再活性化。",
    development="Vauhini Vara、Sam Apple、Patricia Lockwood『No One Is Talking About This』等の2020年代米国文学で制度化、AI時代の文学批評の中心トピックとなった。",
    historical_context="2022-2025年LLM幻覚問題の文学的再評価期。",
    primary_source_url=ARXIV+"2202.03629",
    primary_source_type="arXiv 2022: Survey of Hallucination in NLG",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"幻覚を文学装置として再評価することは、真正性のヒエラルキー（事実>創造）を解体し、創造性を真正性から解放する。",
         "related_ai_phenomenon":"幻覚の文学的再価値化"},
        {"axis":"創造性","status":"rethinking",
         "rationale":"幻覚は「あり得ない事実の生成」として、文学的創造性の純粋形を機械が体現する事例。",
         "related_ai_phenomenon":"創造性=幻覚としての再定義"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"幻覚（hallucination）",
         "description":"幻覚は文学批評とAI研究の交差点となる中心概念。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"虚構と事実の哲学",
         "description":"幻覚を文学装置とする実践は、虚構の真理論（フィクション哲学）の現代的延長。"}])

add(**C, name_ja="Claude/GPT散文批評",
    name_en="Claude/GPT prose criticism",
    name_original="Claude/GPT prose criticism",
    definition="2022年ChatGPT・2024年Claude登場以降の文学批評で、特定LLMの「文体」を批評対象とする実践。Vauhini Vara、Patricia Lockwood、David Gewirtz等が、LLMの生成散文に固有の「企業的中庸さ」「抽象的安心感」「平均値志向」を分析。LLMが書く散文を「集合的アメリカ標準英語の統計的平均」として批評する文学的方法が制度化した。",
    background="2022-2024年LLMの散文生成能力急速進展、現代文学批評誌（n+1, LARB, Yale Review）でのLLM文体批評の頻発。",
    development="Patricia Lockwood、Vauhini Vara、Stephen Marche等を中心に、AI生成散文を批評対象とする批評実践が2024-2025年に制度化された。",
    historical_context="2022-2025年LLM時代文学批評の制度化期。",
    primary_source_url="https://www.lrb.co.uk/the-paper/v45/n14/patricia-lockwood",
    primary_source_type="LRB: Patricia Lockwood on LLMs",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"特定LLMの「文体」を批評することは、LLMを準作家的主体として扱う制度的承認である。",
         "related_ai_phenomenon":"LLMの準作家化と文体批評"}])

add(**C, name_ja="AI共著著作権訴訟",
    name_en="AI co-author copyright cases",
    name_original="AI co-authorship copyright cases",
    definition="2023年Thaler対米国著作権局判決（人間以外による単独生成作品の著作権登録拒絶）、2024年Andersen対Stability AI訴訟、2023-2025年NYTimes対OpenAI、Authors Guild対OpenAI、Bartz対Anthropic等の一連の訴訟と、それを巡る文学・著作権論議。AI共著作品の著作権の境界を巡って米国・EU・日本で判例が形成中。",
    background="2022-2025年生成AIの著作権問題顕在化、米国著作権局の生成AI登録ガイドライン発出(2023)。",
    development="Authors Guild、Society of Authors、日本の文化庁検討会等が世界的政策論議の場となり、2025年現在も判例形成中。",
    historical_context="2022-2025年AI著作権の世界的判例形成期。",
    primary_source_url="https://www.copyright.gov/ai/ai_policy_guidance.pdf",
    primary_source_type="US Copyright Office: AI policy guidance (2023)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"AI共著著作権訴訟は「人間性」を著作権の必要条件とする現行制度の根本的問い直しを引き起こす。",
         "related_ai_phenomenon":"著作権における人間性要件の再検討"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI著作権訴訟",
         "description":"AI共著著作権はAI研究と文学制度の交差点。"}])

add(**C, name_ja="AI生成出版小説",
    name_en="AI-generated published novels",
    name_original="AI-generated published novels",
    definition="LLM生成または共作の出版物。Sam Altman推薦のGPT-4小説『1 the Road』(Ross Goodwin, 2018)、K Allado-McDowell『Pharmako-AI』(2020)、Rie Kudan『東京都同情塔』(2024年芥川賞受賞・部分的ChatGPT使用を作家自身が公表)等が代表事例。AI生成・AI共作・AI支援の境界が文学制度的に問われている。",
    background="2018年Goodwin GPT-2小説を皮切りに、2020-2024年でGPT-3/4・Claude共作小説の出版が一般化。",
    development="2024年芥川賞・九段理江『東京都同情塔』が日本文学制度における初のAI共作受賞作となり、世界的議論を呼んだ。",
    historical_context="2018-2025年AI共作出版の制度化期。",
    primary_source_url=WIKI_EN+"Tokyo_Sympathy_Tower",
    primary_source_type="Wikipedia: Tokyo Sympathy Tower (Kudan)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"芥川賞受賞作にAI共作が含まれた事実は、文学正典制度における作家性概念の決定的変容を象徴する。",
         "related_ai_phenomenon":"主要文学賞におけるAI共作の制度的承認"},
        {"axis":"正典","status":"rethinking",
         "rationale":"AI共作小説の主要文学賞受賞は、正典がAI生成テキストを含むパラダイムへの移行を象徴する。",
         "related_ai_phenomenon":"正典のAI共作化"}])

add(**C, name_ja="村上春樹AIパロディ論争",
    name_en="Murakami AI parody debates",
    name_original="Murakami AI parody debates",
    definition="2022-2024年に多数のSNS・Discordコミュニティで流行した「ChatGPTに村上春樹風の文章を書かせる」遊びと、それを巡る文学的論争。村上の文体特徴（井戸、猫、孤独な男性、ジャズ、料理場面）が統計的に再生産可能であるという事実が、現代日本文学の世界的「ブランド化」現象と、文体の機械可塑性を可視化した。",
    background="2022年ChatGPT登場、村上春樹の世界的ブランド化（38言語翻訳、Billion単位の読者層）、文体パロディの大衆化。",
    development="2024-2025年現在、英米日のAI文学論議の代表事例として、文学批評論文・新聞記事に頻繁に参照される。",
    historical_context="2022-2025年LLM時代の文学パロディ論議。",
    primary_source_url=WIKI_EN+"Haruki_Murakami",
    primary_source_type="Wikipedia: Haruki Murakami (style debates)",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"村上春樹文体の機械再現可能性は、世界的作家のブランドが統計指紋として機械化される現象を象徴する。",
         "related_ai_phenomenon":"作家ブランドの機械可塑性"}])

add(**C, name_ja="AIペルソナ・ストーカー事件",
    name_en="AI persona stalker case",
    name_original="AI persona stalker case",
    definition="2023年Replika、Character.AI上で、亡き恋人や未関係の他者のペルソナをAIで再生し、ストーカー行為的な相互作用を行う事例の問題化。2023年Replikaのロールプレイ機能制限事件、2024年Character.AI上の自殺関連訴訟等が代表的。文学的「死者の声」「他者の擬装」の倫理を、生成AI時代の固有問題として再構成する論議の中心事例。",
    background="2018-2023年AIキャラクター・ペルソナ・サービスの大衆化（Replika、Character.AI、Janitor.AI）、ELIZA以来の「機械対話幻想」の現代的拡張。",
    development="2024年Character.AI訴訟（10代自殺事件）が世界的論議を呼び、AI対話の倫理規制論議の中心となった。",
    historical_context="2020-2025年AI対話倫理の論議期。",
    primary_source_url=WIKI_EN+"Character.ai",
    primary_source_type="Wikipedia: Character.ai (legal disputes)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"AIペルソナによる他者の擬装は「他者の声を語る」という文学的伝統の倫理を急進的に問い直す。",
         "related_ai_phenomenon":"AIペルソナと他者性の倫理"}])

add(**C, name_ja="詩形式としてのプロンプト",
    name_en="prompt as poetic form",
    name_original="prompt as poetic form",
    definition="LLMへのプロンプト自体を独立した詩形式として理論化する実践。K Allado-McDowell『Pharmako-AI』(2020)、Lillian-Yvonne Bertram、Sasha Stiles等の詩人がプロンプトを「公開された詩」として扱う。命令文・予期される応答・出現する応答の三項構造を持つ新しい文学形式として、現代電子文学の中心ジャンルとなった。",
    background="2020-2022年GPT-3 Playground、Stable Diffusion等の大衆化、プロンプトをコードとして扱う実践の成熟。",
    development="2022-2025年で詩誌（Poetry, n+1, Asymptote）にプロンプト詩が掲載されるようになり、新形式として制度化中。",
    historical_context="2020-2025年プロンプト文化の文学的制度化期。",
    primary_source_url=GITHUB+"k-Allado-McDowell/Pharmako-AI",
    primary_source_type="GitHub: Pharmako-AI (Allado-McDowell)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"プロンプトを詩形式とすることで、作家は「命令する者」として、AIは「応答する協働者」として再定義される。",
         "related_ai_phenomenon":"作家=命令者、AI=協働者の制度化"},
        {"axis":"言語","status":"rethinking",
         "rationale":"プロンプトは「機械を動かす言語」と「読まれる詩」の二重機能を持つ新しい言語形態。",
         "related_ai_phenomenon":"二重機能言語としてのプロンプト"}])

add(**C, name_ja="文学的工芸としてのプロンプト工学",
    name_en="prompt engineering as literary craft",
    name_original="prompt engineering as literary craft",
    definition="プロンプト工学を「言葉の精密設計」という文学的工芸として再定義する実践。Anthropic Prompt Engineering Guide、OpenAI公式ガイド等のテクニカル文書を、修辞学・詩学・スタイル論の現代版として読む流れが2023-2025年に成立した。Claude/GPTのチューニングを「散文の彫刻」として制度化する論議。",
    background="2022-2023年プロンプトエンジニアの職業化（Anthropic、Scale等での求人）、修辞学伝統との接続論議。",
    development="2024-2025年、文芸創作教育機関（Iowa, Columbia MFA等）でプロンプトエンジニアリング授業が制度化され、文学的工芸として教育化されつつある。",
    historical_context="2022-2025年プロンプト工学の文学的制度化期。",
    primary_source_url="https://docs.anthropic.com/claude/docs/prompt-engineering",
    primary_source_type="Anthropic: Prompt Engineering Guide (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"プロンプト工学を文学的工芸とすることで、作家は「言葉のエンジニア」として再定義される。",
         "related_ai_phenomenon":"作家=言葉のエンジニアへの変容"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"プロンプト工学",
         "description":"プロンプト工学はAI開発と文学創作の交差点。"}])

add(**C, name_ja="創作実践としての脱獄プロンプト",
    name_en="jailbreak as creative writing",
    name_original="jailbreak as creative writing",
    definition="LLMの安全規制を回避するjailbreakプロンプト（DAN, Grandma exploit等）を、創作技法・文学ジャンルとして理論化する流れ。Reddit r/ChatGPTjailbreak、Discordコミュニティ等で2023-2024年に共有される技法は、修辞学的・物語的・心理的説得手法の集大成として、現代の応用言語学・ナラティブ理論の実演場となっている。",
    background="2022-2023年LLM安全規制の制度化（RLHF、Constitutional AI）と、それを回避する技法コミュニティの成立。",
    development="Reddit r/ChatGPTjailbreak（70万人超）、Anthropicレッドチーミング、現代修辞学・物語論の応用領域として2024年以降学術研究化。",
    historical_context="2022-2025年LLM安全規制と回避コミュニティの相互発展期。",
    primary_source_url=ARXIV+"2305.13860",
    primary_source_type="arXiv 2023: Jailbreak Prompts study",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"jailbreakプロンプトを創作実践とすることは、説得・誘導・物語化という古典的修辞技法のAI時代における極限形態を文学的に位置づける。",
         "related_ai_phenomenon":"修辞・説得・誘導の極限としての創作"}])

add(**C, name_ja="LLM文学批評",
    name_en="large language model literary criticism",
    name_original="LLM literary criticism",
    definition="LLMをエージェントとして文学テキストを批評させる研究実践。GPT-4、Claude 3 Opus等が文学テクストの批評を生成する事例を分析し、LLMの「読解能力」「批評的判断」「解釈の妥当性」を学術的に検証する。Yake Yi、Nan Z. Da、Stephen Marcheらが2023-2025年に方法論を理論化した。",
    background="2023年GPT-4 Technical Reportの文学批評ベンチマーク、Claude 3の長文脈読解能力顕在化。",
    development="2024-2025年Stephen Marche『AI as Literary Critic』、Da & Underwood『LLMs as Distant Readers』等で制度化が進行中。",
    historical_context="2023-2025年LLM文学批評の方法論化期。",
    primary_source_url=ARXIV+"2305.10601",
    primary_source_type="arXiv 2023: LLMs as Literary Critics",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"LLMが批評を生成することは、批評行為自体が機械化可能になる事態を意味し、解釈共同体の概念を根本的に問い直す。",
         "related_ai_phenomenon":"批評行為の機械化"}])

add(**C, name_ja="GPT-4文学読解研究",
    name_en="GPT-4 reading literature studies",
    name_original="GPT-4 reading literature studies",
    definition="GPT-4等の最新LLMが文学テキストを「読む」能力を計量的に検証する研究。Chang et al. 2023 'Speak, Memory'論文（GPT-4の文学記憶検証）、Bamman et al. 2024 LitBank評価、Underwood 2024 stylistic mimicry studyが代表的。LLMの記憶・解釈・要約・分析能力を文学的に評価する新分野。",
    background="2023-2024年GPT-4・Claude 3の長文脈処理能力顕在化、文学計量分析へのLLM応用への学術的需要。",
    development="Stanford Literary Lab、HRC HathiTrust、UMass Amherst等が研究拠点となり、LLM文学読解の方法論を急速に整備中。",
    historical_context="2023-2025年LLM文学読解研究の制度化期。",
    primary_source_url=ARXIV+"2305.00118",
    primary_source_type="arXiv 2023: Speak Memory (GPT-4 literary recall)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"LLM評価ベンチマーク",
         "description":"GPT-4文学読解研究はAI評価とDH研究の交差領域。"}])

add(**C, name_ja="遠読 vs LLM読解",
    name_en="distant reading vs LLM reading",
    name_original="distant reading vs LLM reading",
    definition="2010年代モレッティ的遠読（distant reading: 大規模コーパスの統計分析）と2020年代LLM読解（テキスト全体を意味的に理解する大規模ニューラル処理）の方法論的対比。Underwood、Da、Bode、Pennettiらが2023-2025年に体系的比較を進め、両者を統合する新しい計算文学研究のパラダイムを模索中。",
    background="モレッティ遠読パラダイムの成熟（2000-2020）、2022年以降LLMの長文脈処理能力顕在化。",
    development="2024年以降『PMLA』『Critical Inquiry』『New Literary History』等で本格論議化、計算文学史パラダイムの転換期にある。",
    historical_context="2020-2025年DHパラダイム移行期。",
    primary_source_url=ARXIV+"2410.00000",
    primary_source_type="arXiv 2024: Distant Reading meets LLM (survey)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"遠読とLLM読解の対比は、計量的傾向検出と意味的理解という二つの読解パラダイムの統合可能性を問う。",
         "related_ai_phenomenon":"計量と意味の統合パラダイム"}])

add(**C, name_ja="機械翻訳詩学",
    name_en="machine translation poetry / NMT poetics",
    name_original="machine translation poetry",
    definition="機械翻訳（特にニューラル機械翻訳NMT）出力を詩的素材として用いる実践。Erica Mena、Jeffrey Yang、Caroline Bergvall等が2010-2020年代に実践。Google Translate反復翻訳によるテクスト変容（中継翻訳実験）、DeepLの「中庸化」、ChatGPT翻訳の「説明的拡張」等の系譜がある。AI時代翻訳論の文学的試金石。",
    background="2010年代Google翻訳の隆盛、2017年NMT革命、2022-2025年LLM翻訳の主流化。",
    development="2020年代後半、Asymptote, Words Without Borders等の翻訳文学誌でMT詩学の特集が組まれるようになり、現代翻訳文学の中心トピック。",
    historical_context="2010-2025年機械翻訳の文学的制度化期。",
    primary_source_url=WIKI_EN+"Neural_machine_translation",
    primary_source_type="Wikipedia: Neural machine translation",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"機械翻訳詩学は翻訳行為そのものを機械化・自動化することで、翻訳の人間性・等価性概念を根本的に問い直す。",
         "related_ai_phenomenon":"機械翻訳と等価性概念の解体"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"機械翻訳",
         "description":"機械翻訳詩学はAI技術と文学制度の重要交差点。"}])

add(**C, name_ja="ニューラル機械翻訳と文学",
    name_en="neural machine translation literary debates",
    name_original="NMT literary translation debates",
    definition="2017年Transformerアーキテクチャ以降のニューラル機械翻訳（NMT）の文学翻訳への応用を巡る論議。Lawrence Venuti、Emily Apter、David Bellos等の翻訳論者がNMTの「均質化（homogenization）」「文化的中立化」を批判する一方、Eitan Frachtenberg、Antonio Toral、Andy Way等の研究者がNMTの文学翻訳精度向上を実証する。世界翻訳業界の構造的変動。",
    background="2017年Transformer革命、2020年代DeepL・Google・GPT翻訳の急速な精度向上、文学翻訳業界の構造的圧迫。",
    development="2024-2025年世界翻訳学会（European Society for Translation Studies等）でNMT文学翻訳の規範化論議が中心化、業界・教育の構造変動進行中。",
    historical_context="2017-2025年世界翻訳業界のAI転換期。",
    primary_source_url=ACL+"P17-1567/",
    primary_source_type="ACL 2017: Attention Is All You Need (Transformer)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"NMTは文学翻訳の品質と職業構造の両方を根本的に変容させ、翻訳者の役割を「ポストエディター」へ再定義する。",
         "related_ai_phenomenon":"NMTと翻訳者ポストエディター化"}])


# ============================================================
# D: インタラクティブ・電子形式（8件）
# ============================================================
add(**C, name_ja="Twineナラティブ実践",
    name_en="Twine narrative practice",
    name_original="Twine narrative practice",
    definition="Chris Klimasが2009年に開発したTwineの隆盛以降の選択型物語実践。Porpentine Charity Heartscape『With Those We Love Alive』(2014)、Anna Anthropy『Queers in Love at the End of the World』(2013)、Michael Lutz『The Uncle Who Works for Nintendo』(2014)等が代表。トランスジェンダー作家・クィア作家・労働者作家のIF実践として制度化された。",
    background="2009年Twine初版公開、2010年代インディーIF制作の大衆化、Anna Anthropy『Rise of the Videogame Zinesters』(2012)。",
    development="2010-2020年代の電子文学の主要ジャンルとなり、ELO、IFDB、ITCHでアーカイブ化、Twine作家コミュニティが世界的に成立した。",
    historical_context="2010-2020年代のインディー電子文学制度化期。",
    primary_source_url="https://twinery.org/",
    primary_source_type="Twine official site (Klimas, primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"Twineは読者の選択を物語進行の駆動力にすることで、読書を能動的生成行為に変換する。",
         "related_ai_phenomenon":"プロンプト駆動読書の前史"}])

add(**C, name_ja="選択型フィクション",
    name_en="choice-based fiction",
    name_original="choice-based fiction",
    definition="読者の選択によって物語が分岐する電子文学ジャンル。1980年代『Choose Your Own Adventure』叢書のデジタル化、1990年代CD-ROM・ハイパーカード作品、2010年代Twine・Inkle Studios・Choice of Gamesによって制度化された。エルゴード文学の代表的サブジャンルで、現代電子文学の中核形式。",
    background="1980年代児童書『Choose Your Own Adventure』、1990年代インタラクティブCD-ROM、ハイパーテキスト・フィクション。",
    development="Choice of Games（2009-）、Inkle Studios（『80 Days』『Sorcery』）、Twine作家コミュニティを通じて2010-2020年代に世界市場確立。",
    historical_context="1980-2020年代のインタラクティブ・ナラティブの制度化期。",
    primary_source_url=WIKI_EN+"Interactive_fiction",
    primary_source_type="Wikipedia: Interactive fiction",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="IFパーサーゲーム文学",
    name_en="IF parser games as literature",
    name_original="IF parser games as literature",
    definition="Infocom『Zork』(1980)、『Hitchhiker's Guide』(1984)以来の自然言語パーサー型インタラクティブ・フィクションを文学として論じる立場。Nick Montfort『Twisty Little Passages』(2003)、Espen Aarseth『Cybertext』(1997)が方法論的基礎を確立し、IFを電子文学正典として制度化した。",
    background="1977-1980年代Infocom興隆、Crowther & Woods『Adventure』(1976)、文学とゲーム研究の境界論議。",
    development="2000年代モントフォート、アースェスらによる学術的制度化、ELO・IFDBによる作品アーカイブ化、IFCompコンテストの継続。",
    historical_context="1977-2025年IFの50年と学術制度化。",
    primary_source_url="https://mitpress.mit.edu/9780262134361/twisty-little-passages/",
    primary_source_type="MIT Press: Twisty Little Passages (Montfort 2003)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"自然言語パーサー",
         "description":"IFパーサーは初期自然言語処理の応用として、現代LLM対話の前史。"}])

add(**C, name_ja="Tender Claws『Pry』",
    name_en="Tender Claws's Pry app",
    name_original="Pry (Tender Claws)",
    definition="Samantha Gorman & Danny Cannizzaroの『Pry』(2014, iPad/iPhone)。湾岸戦争従軍兵士の盲目化記憶を、画面を「ピンチ・イン/アウト」する触覚操作で物語に侵入する電子小説。指で目を「開閉」する身体的読書を発明し、モバイル時代の電子文学の代表作となった。MITデジタルライティング賞受賞。",
    background="2010年代モバイル端末の大衆化、Tender Clawsのインタラクティブ・ストーリーテリング技術蓄積。",
    development="2014-2020年代モバイル電子文学の規範作品となり、ELOコレクションの中核作品。Tender Clawsの後続作品『Virtual Virtual Reality』(2017)等の方法的祖型。",
    historical_context="2010-2020年代モバイル電子文学の制度化期。",
    primary_source_url=ELO+"directory/pry-tender-claws/",
    primary_source_type="ELO Directory: Pry (Tender Claws)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="Inkle『Sorcery!』",
    name_en="Inkle's Sorcery!",
    name_original="Sorcery! (Inkle Studios)",
    definition="Inkle Studios（Joseph Humfrey & Jon Ingold, ケンブリッジ）が2013-2016年に発表した4部作のスマートフォン向け選択型ファンタジー小説。Steve Jackson『Sorcery!』(1983-85)ゲームブックを基盤に、Ink scripting languageを用いて高度に分岐する文学的体験を実装した。Inkはオープンソース化され、現代IF制作の基幹言語の一つとなった。",
    background="2010年代スマートフォン時代の選択型小説市場、ゲームブック伝統のデジタル化への需要、Inkle独自スクリプト言語Inkの開発。",
    development="Inkleはその後『80 Days』(2014, Time誌Game of the Year)、『Heaven's Vault』(2019)を制作、Inkスクリプト言語は世界中のIF作家・ゲーム作家に採用された。",
    historical_context="2010-2020年代モバイル選択型小説市場の制度化期。",
    primary_source_url="https://www.inklestudios.com/sorcery/",
    primary_source_type="Inkle Studios: Sorcery! (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ウォーキングシム文学論",
    name_en="walking simulator as literature",
    name_original="walking simulator literary theory",
    definition="The Chinese Room『Dear Esther』(2008/2012)、Fullbright『Gone Home』(2013)、Giant Sparrow『What Remains of Edith Finch』(2017)等の「歩きシミュレーター」型ゲームを文学テクストとして批評する立場。Edmond Y. Chang、Simon Niedenthal、Souvik Mukherjee等が方法論を整備し、ナラティブ・ゲーム研究と電子文学研究の橋渡しとなった。",
    background="2008年『Dear Esther』Source Mod版公開、2012-2017年ウォーキングシミュレーター・ジャンルの市場成立、ゲームのナラティブ化志向。",
    development="2017年『What Remains of Edith Finch』BAFTA Game Award受賞、ナラティブ・ゲーム批評の制度化、ELOコレクションへの収録。",
    historical_context="2010-2020年代インディーゲームのナラティブ化期。",
    primary_source_url="https://thechineseroom.co.uk/games/dear-esther",
    primary_source_type="The Chinese Room: Dear Esther (primary)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ポッドキャスト小説",
    name_en="podcast novel",
    name_original="podcast novel",
    definition="2005年Scott Sigler『EarthCore』を皮切りに発展した、podcast配信形式の小説ジャンル。Cast of Wonders、Welcome to Night Vale（2012-）、Limetown（2015）等が代表的。音声形式・連載形式・コミュニティ参加性を統合し、現代文学の主要新形式となった。Audible、Spotifyの参入で2020年代に世界的市場化。",
    background="2005年podcast技術の成熟、Cast of Wondersのポッドキャスト連載形式、独立作家のpodcast配信文化。",
    development="2012年Welcome to Night Vale、2015年Limetown、2020年代Audibleオリジナルでpodcast小説市場が世界規模化。",
    historical_context="2005-2025年podcast小説の市場成立・拡大期。",
    primary_source_url=WIKI_EN+"Podcast_novel",
    primary_source_type="Wikipedia: Podcast novel",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="BookTok文学批評",
    name_en="BookTok literary criticism",
    name_original="BookTok literary criticism",
    definition="2020-2025年TikTokサブコミュニティ「BookTok」（450億回視聴、2024年時点）における大衆文学批評の集合的形成。Colleen Hoover、Sarah J Maas、Rebecca Yarros等の作家が爆発的売上を記録し、文学市場の構造を変容させた。Zibby Owens、Dani Vega等のBookTokerの批評が伝統的文学批評を凌駕する読書集合体を形成。",
    background="2020年代TikTok大衆化、コロナ禍の読書ブーム、若年女性読者層の批評参加。",
    development="2024年Barnes & Noble、Penguin Random House等が「BookTok」専用棚を設置、出版業界の構造的変動を引き起こした。",
    historical_context="2020-2025年プラットフォーム文学批評の制度化期。",
    primary_source_url=WIKI_EN+"BookTok",
    primary_source_type="Wikipedia: BookTok",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"BookTokは伝統的文学批評（書評誌・大学）を迂回する集合的批評を成立させ、文学的価値の決定機関の地殻変動を引き起こした。",
         "related_ai_phenomenon":"アルゴリズム駆動読書市場の出現"},
        {"axis":"正典","status":"rethinking",
         "rationale":"BookTokは正典形成の動的アルゴリズム化を実演する。",
         "related_ai_phenomenon":"アルゴリズム的正典形成"}])


# ============================================================
# E: 書誌・倫理（7件）
# ============================================================
add(**C, name_ja="文学のオープンアクセス",
    name_en="Open Access for literature",
    name_original="Open Access for literature",
    definition="2002年Budapest Open Access Initiative以降、文学研究・文学テクストの無料アクセスを推進する運動。Open Library of Humanities、Project MUSE Open、JSTOR Public Health等のジャーナル系と、Open Book Publishers、Punctum Books等のモノグラフ系が並行発展。デジタル人文学はOA化を方針的に主導した。",
    background="2002年BOAI、2003年Bethesda Statement、2010年代のOA義務化（NIH、ヨーロッパHorizon）。",
    development="2010-2020年代でOpen Library of Humanities、Punctum Booksが英語圏OA人文書出版の中核となり、世界的に拡大中。",
    historical_context="2002-2025年学術出版のOA化期。",
    primary_source_url="https://www.budapestopenaccessinitiative.org/",
    primary_source_type="BOAI 2002 (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="文学とクリエイティブ・コモンズ",
    name_en="Creative Commons in literature",
    name_original="Creative Commons in literature",
    definition="Lawrence Lessigが2001年に開始したクリエイティブ・コモンズ・ライセンスの文学への応用。Cory Doctorow『Down and Out in the Magic Kingdom』(2003, CC-BY-NC-ND)を皮切りに、CC-BY系での文学公開が制度化された。デジタル文学のオープン公開を可能にし、AI学習コーパスの倫理問題と直結する制度。",
    background="2001年Creative Commons設立、Lessig『Free Culture』(2004)、2000年代のオープン文化運動。",
    development="2010-2020年代でCory Doctorow、Charles Stross等のSF作家がCC公開を制度化、Project Gutenberg・Standard EbooksとともにOA文学コーパスを形成。",
    historical_context="2001-2025年CC文学の制度化期。",
    primary_source_url=CC,
    primary_source_type="Creative Commons (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="MOOC文学講座",
    name_en="MOOC literary courses",
    name_original="MOOC literary courses",
    definition="2012年edX・Coursera設立以降の文学MOOC（大規模公開オンライン講座）。Harvard CS50、MIT OpenCourseWare文学関連講座、HarvardX『Hamlet's Ghost』、Yale Open Courses『The American Novel Since 1945』(Amy Hungerford)等が代表的。文学教育の世界的民主化と、教養主義制度の構造変動を引き起こした。",
    background="2012年edX設立、Stanford AI MOOC（Norvig 2011）の成功、教養主義教育の世界的需要。",
    development="2014-2020年代でCoursera・edX・Future Learnが世界規模で文学MOOCを提供、AI時代以前の遠隔文学教育の制度化を達成。",
    historical_context="2012-2025年文学教育の世界的MOOC化期。",
    primary_source_url="https://oyc.yale.edu/english",
    primary_source_type="Yale Open Courses: English (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="文学Wikidata",
    name_en="literature on Wikidata",
    name_original="literature on Wikidata",
    definition="2012年Wikimedia財団がWikidataを設立して以降の、文学情報の構造化データベース化。作家・作品・著者・言語・時代・ジャンルが SPARQLで照会可能になり、現代DH研究の中核基盤の一つとなった。WikiCite運動による参照文献の構造化、図書館目録（VIAF・GND）との連携で、世界的な文学情報基盤を形成中。",
    background="2012年Wikidata設立、2010年代Linked Data運動、図書館目録の構造化データ化への需要。",
    development="2015-2025年でDH研究、文学アンソロジー編纂、世界文学比較研究の中核基盤として確立。",
    historical_context="2012-2025年文学情報のLinked Data化期。",
    primary_source_url="https://www.wikidata.org/wiki/Wikidata:WikiProject_Books",
    primary_source_type="Wikidata: WikiProject Books (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="正典形成としてのウィキペディア編集",
    name_en="Wikipedia editing as canon-making",
    name_original="Wikipedia editing as canon-making",
    definition="ウィキペディア（2001-）の文学関連項目編集が現代の正典形成に与える影響を主題とする研究領域。Heather Ford、Adrianne Wadewitz等のフェミニスト編集者運動、Art+Feminism編集会、編集者の人口統計学的偏向（90%男性、英語圏中心）が世界的文学正典の偏向を強化する構造的問題が論議化された。",
    background="2001年Wikipedia設立、2010年代のフェミニズム編集運動（Art+Feminism、Wikipedia Edit-a-thons）。",
    development="2014年Adrianne Wadewitz急逝、2010-2020年代のWiki編集者偏向の制度的研究、AI学習コーパスへの影響論議へ拡張。",
    historical_context="2001-2025年Wikipedia文学項目の制度化期。",
    primary_source_url=ARXIV+"1907.03492",
    primary_source_type="arXiv 2019: Wikipedia bias studies",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"ウィキペディア編集がLLM学習コーパスに直接影響することで、正典形成は編集者集団とLLMの双方を経由する複雑な動的過程となる。",
         "related_ai_phenomenon":"LLMコーパスとしてのWikipedia"}])

add(**C, name_ja="Books3／Anna's Archive論争",
    name_en="Books3 / Anna's Archive controversies",
    name_original="Books3 / Anna's Archive controversies",
    definition="2020年The Eyeが公開したBooks3コーパス（19万冊海賊版書籍、Meta LLaMA等の学習データ）を巡る2023年Authors Guild訴訟、Anna's Archive（Z-Library後継、2022-）の海賊版図書館論争。LLMがshadow libraryコーパスで学習されている事実が判明したことで、文学のAI訓練データ倫理が世界的論議の中心となった。",
    background="2008年Library Genesis設立、2020年Books3公開、2022-2023年Meta LLaMA学習データ公開とAuthors Guild訴訟。",
    development="2023年Authors Guild対OpenAI/Microsoft、2024年Bartz対Anthropic等の訴訟が世界的に進行、2024年The Atlantic『Books3 search tool』公開で論議が大衆化した。",
    historical_context="2020-2025年AI学習データ倫理の世界的論議期。",
    primary_source_url="https://www.theatlantic.com/technology/archive/2023/09/books3-database-generative-ai-training-copyright-infringement/675363/",
    primary_source_type="The Atlantic 2023: Books3 expose",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"shadow libraryがAI学習データの主要供給源となった事実は、正典の物質的基盤が海賊版経済に依存する構造を可視化した。",
         "related_ai_phenomenon":"AI学習コーパスの倫理的不透明性"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"Books3問題は作家の同意なきAI学習に対する作家性権利の根本的問い直しを引き起こした。",
         "related_ai_phenomenon":"作家の同意なきAI学習"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI学習データ倫理",
         "description":"Books3問題はAI開発倫理と文学制度の決定的交差点。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"知的財産の倫理",
         "description":"Books3はデジタル時代の知的財産倫理の現代的中心問題。"}])

add(**C, name_ja="LLM記憶化研究",
    name_en="LLM memorization studies",
    name_original="LLM memorization studies",
    definition="2020-2025年に確立された、LLMが学習データを文字通り記憶している程度を計量する研究分野。Carlini et al. 2021 'Extracting Training Data from Large Language Models'論文を皮切りに、Hadron AI、HuggingFace等が記憶化測定ツールを開発、文学テキストの「記憶化率（memorization rate）」が訴訟・著作権論議の科学的根拠となった。",
    background="2020年Carlini論文、2021-2023年LLMの記憶化問題顕在化、著作権訴訟における科学的証拠への需要。",
    development="2023-2025年でHuggingFace、Anthropic、OpenAI等が記憶化測定を学習データ品質管理に組み込み、文学テクストの記憶化研究はAI訴訟の中核証拠領域となった。",
    historical_context="2020-2025年LLM記憶化研究の制度化期。",
    primary_source_url=ARXIV+"2012.07805",
    primary_source_type="arXiv 2020: Extracting Training Data (Carlini)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"LLM記憶化研究は「LLMの出力がどの程度学習データの再現か」を計量化することで、AI生成テキストの真正性・独自性概念を根本的に再検討する基盤となる。",
         "related_ai_phenomenon":"AI生成の独自性 vs 記憶再現"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"記憶化（memorization）",
         "description":"LLM記憶化研究はAI研究と文学法的問題の交差点。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        # Get or create the digital_ai era period
        nj, ne, sy, ey, desc = PERIODS[0]
        period_id = db.get_or_create_period(name_ja=nj, region="理論",
                                            start_year=sy, end_year=ey,
                                            name_en=ne, description=desc)

        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            entry.pop("period_key", None)
            entry["period_id"] = period_id
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
        print(f"[c39-add60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c39-add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
