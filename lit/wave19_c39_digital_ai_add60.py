"""LIT-DB Phase 2 Wave 19 — C39 Digital Humanities & AI Era ADD 60 (NEW).

Subfield: lit_digital_ai (id=24), region='理論'.
Existing 151 concepts. This wave adds 60 NEW non-overlapping concepts.
Targets: ~50% primary, fourth_axes>=35, cross_domain>=25.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("デジタル人文学・AI時代", "Digital Humanities & AI Era",
     1990, 2030,
     "1990年代のTEIとデジタルテクスト批評の制度化から、2010年代の遠読・トピックモデリング、2020年代のLLM以降にいたる、計算的人文学とAI生成文学の理論期。"),
]

WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
ARXIV = "https://arxiv.org/abs/"
GITHUB = "https://github.com/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_digital_ai", region="理論",
         original_script="roman", period_key="デジタル人文学・AI時代")


def fa_authorship(reason, phenom="AI作者性再考"):
    return {"axis":"作者性","status":"rethinking","rationale":reason,
            "related_ai_phenomenon":phenom}

def fa_canon(reason, phenom="正典再考"):
    return {"axis":"正典","status":"rethinking","rationale":reason,
            "related_ai_phenomenon":phenom}

def fa_auth(reason, phenom="真正性再考"):
    return {"axis":"真正性","status":"rethinking","rationale":reason,
            "related_ai_phenomenon":phenom}

def fa_recv(reason, phenom="受容再考"):
    return {"axis":"受容","status":"rethinking","rationale":reason,
            "related_ai_phenomenon":phenom}

def cd(target_db, name, desc):
    return {"target_db":target_db, "link_type":"shared_concept",
            "target_entity_name":name, "description":desc}


# ============================================================
# A: AI生成文学の実例（11件）
# ============================================================
add(**C, name_ja="Wattpad AI Story Tools",
    name_en="Wattpad AI authoring tools",
    name_original="Wattpad AI tools",
    definition="2023年以降Wattpadが導入したAI支援執筆機能。アイデア生成・タグ提案・あらすじ要約をAIが補助し、9,000万人ユーザー規模の同人創作プラットフォームに生成AIを統合した。",
    background="2021年Naver買収後のテック投資、2023年生成AI大衆化への対応。",
    development="2024-2025年でAI支援機能の全面展開、同人創作と生成AIの統合モデルの代表事例となった。",
    historical_context="2023-2025年Web小説プラットフォームのAI統合期。",
    primary_source_url="https://company.wattpad.com/",
    primary_source_type="Wattpad: corporate site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Wattpad AI機能は同人創作と生成AIを統合した産業規模の事例。", "同人×AI統合")],
    cross_domain=[cd("AI-Development","生成AI応用","Wattpad AIはエンタメ系AI応用の代表事例。")])

add(**C, name_ja="ProWritingAid",
    name_en="ProWritingAid",
    name_original="ProWritingAid",
    definition="2012年設立のAI支援文章校正ツール。文体分析・冗長性検出・ペース解析等25種類のレポートを提供、NaNoWriMoとの公式提携で創作支援ツールの標準となった。",
    background="2012年Orpheus Technology設立、文章解析ツールの市場形成。",
    development="2018-2024年でNaNoWriMo公認ツール化、Grammarlyと並ぶ創作支援ツール双璧となった。",
    historical_context="2012-2025年AI文章校正期。",
    primary_source_url="https://prowritingaid.com/",
    primary_source_type="ProWritingAid: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("ProWritingAidはAI校正と人間執筆の協働を制度化した。")])

add(**C, name_ja="ChatGPT共著事例",
    name_en="ChatGPT-as-coauthor cases",
    name_original="ChatGPT coauthorship cases",
    definition="2022-2025年ChatGPTを共著者として明示した出版書籍群。Iain Thomas『What Makes Us Human』(2022)、Reid Hoffman『Impromptu』(2023)等、共著者表記をめぐる出版倫理論議の事例。",
    background="2022年11月ChatGPT公開、共著者帰属の規範未確立。",
    development="2023-2025年で出版業界が共著者表記ガイドラインを整備、AI共著の制度化が進行中。",
    historical_context="2022-2025年AI共著規範形成期。",
    primary_source_url="https://www.impromptubook.com/",
    primary_source_type="Impromptu: official site (primary case)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("ChatGPT共著事例は共著者帰属の制度的不確定性を可視化した。")],
    cross_domain=[cd("PHIL","作者性","AI共著は作者概念の哲学的再検討を要請する。")])

add(**C, name_ja="Sudowrite Story Engine",
    name_en="Sudowrite Story Engine",
    name_original="Sudowrite Story Engine",
    definition="2023年Sudowriteが公開した長編生成支援機能。ビート構造・キャラクター一貫性・章生成を統合し、長編小説生成を構造的に支援する代表的AI執筆ツール。",
    background="2021年Sudowrite創業、2022-2023年LLM大衆化と長編生成需要。",
    development="2023-2025年でAmazon KDPベストセラー作家層に普及、AI執筆ツールの主流化を駆動した。",
    historical_context="2023-2025年AI長編生成ツール期。",
    primary_source_url="https://www.sudowrite.com/",
    primary_source_type="Sudowrite: official site (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Story EngineはAI長編生成を構造的に制度化した。")])

add(**C, name_ja="NovelAI Aetherroom",
    name_en="NovelAI Aetherroom",
    name_original="NovelAI Aetherroom",
    definition="NovelAIのプロンプト共有プラットフォーム。生成キャラクター設定・物語シナリオ・スタイルプリセットを共有し、生成文学コミュニティの集合知形成インフラとなった。",
    background="2021年NovelAI創業、2022-2023年プロンプト共有需要の浮上。",
    development="2023-2025年でアニメ・ライトノベル系生成コミュニティの中核プラットフォームとなった。",
    historical_context="2021-2025年プロンプト共有期。",
    primary_source_url="https://aetherroom.club/",
    primary_source_type="Aetherroom: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Aetherroomはプロンプト共有による集合的作者性を制度化した。")])

add(**C, name_ja="Writesonic",
    name_en="Writesonic",
    name_original="Writesonic",
    definition="2020年設立のAI執筆プラットフォーム。マーケティング文・記事・小説を自動生成するSaaSとして500万ユーザー規模に成長、Y Combinator出身のAI執筆ツール代表事例。",
    background="2020年GPT-3 API公開、AI執筆SaaS市場形成期。",
    development="2022-2024年で世界規模のAI執筆SaaSとなり、ChatGPTとの差別化で文学・マーケティング応用を展開した。",
    historical_context="2020-2025年AI執筆SaaS期。",
    primary_source_url="https://writesonic.com/",
    primary_source_type="Writesonic: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="Rytr",
    name_en="Rytr",
    name_original="Rytr",
    definition="2021年設立の低価格AI執筆SaaS。月額9ドルで40言語対応のテキスト生成を提供、新興市場のAI執筆ツール代表として大衆化を駆動した。",
    background="2021年GPT-3普及、低価格AI執筆ツール需要。",
    development="2022-2025年で世界500万ユーザーに到達、新興市場のAI執筆大衆化の代表事例となった。",
    historical_context="2021-2025年AI執筆大衆化期。",
    primary_source_url="https://rytr.me/",
    primary_source_type="Rytr: official site (primary)",
    importance_score=2, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="AI Dungeon同人小説",
    name_en="AI Dungeon community fiction",
    name_original="AI Dungeon community fiction",
    definition="2019年Nick Walton開発のAI Dungeonユーザーコミュニティが生成した同人小説群。AIテキストアドベンチャーから派生した協働生成文学の代表事例で、生成AI文学の草分けとなった。",
    background="2019年GPT-2版AI Dungeon公開、ユーザー生成コンテンツの蓄積。",
    development="2020-2023年GPT-3版で世界規模のコミュニティ形成、生成AI同人文化の原型となった。",
    historical_context="2019-2024年生成AI同人期。",
    primary_source_url="https://aidungeon.io/",
    primary_source_type="AI Dungeon: official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("AI Dungeon同人は協働生成文学の草分け事例。")])

add(**C, name_ja="Hidden Door個別物語",
    name_en="Hidden Door personalized narratives",
    name_original="Hidden Door personalized narratives",
    definition="2020年Hilary Mason、Matt Brewer設立のAIナラティブプラットフォーム。既存IP（オズの魔法使い等）を素材に個別化された物語体験を生成、版権文学のAI拡張モデルを開拓した。",
    background="2020年Hilary Mason（Cloudera元CSO）創業、生成ナラティブ研究の系譜。",
    development="2024年正式公開、IPとAI生成の統合モデルとして注目を集めた。",
    historical_context="2020-2025年版権AI拡張期。",
    primary_source_url="https://www.hiddendoor.co/",
    primary_source_type="Hidden Door: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_canon("Hidden Doorは既存正典のAI拡張モデルを開拓した。")])

add(**C, name_ja="AI児童書洪水",
    name_en="AI-generated children's books",
    name_original="AI-generated children's books phenomenon",
    definition="2023年以降Amazon KDPで急増したAI生成児童書群。低品質ストック画像と生成テクストを組み合わせた書籍が氾濫、児童文学の質と作者性を巡る論議を引き起こした。",
    background="2023年DALL-E、Midjourney、ChatGPT普及、児童書低参入障壁市場。",
    development="2023-2025年でAmazon・出版業界がAI児童書ガイドラインを整備、児童文学の質的境界の論議が進行中。",
    historical_context="2023-2025年AI児童書氾濫期。",
    primary_source_url="https://www.theverge.com/2023/9/19/23881035/amazon-kdp-ai-publishing-limits-3-books",
    primary_source_type="The Verge 2023 (primary report)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[fa_recv("AI児童書洪水は児童文学の質と作者性の境界を揺るがした。")])

add(**C, name_ja="Claude/GPT文体比較研究",
    name_en="Claude vs GPT prose style comparison",
    name_original="Claude vs GPT prose comparative studies",
    definition="2023-2025年LLM間文体差を体系的に比較する研究群。AnthropicのClaudeとOpenAIのGPTの語彙頻度・統語構造・トピック分布の差異を計量文体論的手法で検証する文体研究。",
    background="2023年Claude公開、複数LLM比較研究の必要性。",
    development="2024-2025年計量文体論コミュニティでLLM文体比較研究が確立、AI文体論の新領域を形成した。",
    historical_context="2023-2025年LLM文体論期。",
    primary_source_url=ARXIV+"2310.13800",
    primary_source_type="arXiv 2023: stylometric LLM comparison (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_auth("LLM文体比較は機械生成テクストの真正性検証の基盤研究。")],
    cross_domain=[cd("AI-Development","LLM評価","文体比較はLLM評価研究の文学的応用。")])


# ============================================================
# B: 生成詩・形式実験（10件）
# ============================================================
add(**C, name_ja="@magicrealismbot",
    name_en="@magicrealismbot",
    name_original="@magicrealismbot (Twitter bot)",
    definition="2015年Chris Rodley作の自動生成Twitterボット。マジックリアリズム風のミニ物語を毎時生成、botフィクションの代表事例として20万人フォロワーを獲得し、生成詩学の大衆化を駆動した。",
    background="2014年NaNoGenMo文化、bot文学の制度化期。",
    development="2015-2024年でbot文学の最有名事例、出版書籍化（『The Deep Sea』2018）も実現、生成詩学の大衆事例となった。",
    historical_context="2015-2025年Twitterボット文学期。",
    primary_source_url="https://twitter.com/magicrealismbot",
    primary_source_type="Twitter (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("@magicrealismbotはbot生成詩学の大衆化を駆動した。")])

add(**C, name_ja="@deepdrumpf",
    name_en="@deepdrumpf",
    name_original="@deepdrumpf (Trump LSTM bot)",
    definition="2016年Bradley Hayes（MIT CSAIL）作のドナルド・トランプ風文体生成LSTMボット。LSTMベース文体模倣の代表事例として政治風刺×生成AIの草分けとなった。",
    background="2016年米大統領選、LSTM文体模倣技術の成熟。",
    development="2016-2018年で政治風刺×生成AI実験の中核事例、Hayes論文（MIT 2017）でも理論化された。",
    historical_context="2016-2018年LSTM政治ボット期。",
    primary_source_url="https://twitter.com/deepdrumpf",
    primary_source_type="Twitter / MIT (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("@deepdrumpfは政治文体生成のLSTM応用先駆事例。")])

add(**C, name_ja="AI俳句生成",
    name_en="AI haiku generation",
    name_original="AI haiku generation research",
    definition="2017年以降の俳句生成研究群。Hitsuwari et al.(2022)『Computers in Human Behavior』、北海道大学等の研究機関でGPT/BERTベースの俳句生成と人間評価実験が進展、東洋詩学とAIの交差研究の中核となった。",
    background="2017年Recurrent NN詩学研究、2020年GPT-3俳句生成実験。",
    development="2022-2024年で日本詩学×AI研究が国際的に展開、AI俳句の人間判別不能性が実証された。",
    historical_context="2017-2025年AI俳句研究期。",
    primary_source_url="https://www.sciencedirect.com/science/article/pii/S0747563222002977",
    primary_source_type="Computers in Human Behavior 2022 (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_auth("AI俳句研究は東洋詩形のAI生成可能性を実証した。"),
                 fa_authorship("AI俳句は東洋詩学の作者性概念を再検討する実証基盤。")],
    cross_domain=[cd("PT","俳句","AI俳句は詩学とAI研究の交差点。")])

add(**C, name_ja="AIソネット生成",
    name_en="AI sonnet generators",
    name_original="AI sonnet generators with rhyme constraints",
    definition="押韻制約下のソネット生成研究。Lau et al.(2018)『Deep-speare』、Ghazvininejad et al.(2017)『Hafez』等が押韻・韻律制約付きの形式詩生成を実装、形式詩学のAI再構築の中核研究となった。",
    background="2017年Hafez（USC ISI）、Deep-speare（Melbourne）等の制約詩生成研究。",
    development="2018-2024年でTransformerベースの押韻制御研究が成熟、英詩形式詩生成の標準ベンチマークとなった。",
    historical_context="2017-2025年制約詩生成期。",
    primary_source_url="https://aclanthology.org/P18-1181/",
    primary_source_type="ACL 2018: Deep-speare (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("ソネット生成研究は形式詩学のAI再構築を実現した。")],
    cross_domain=[cd("PT","ソネット","AIソネット生成は詩学形式論とAIの交差点。")])

add(**C, name_ja="Cento生成",
    name_en="Cento generators",
    name_original="Cento generators (digital pastiche)",
    definition="既存テクストの断片を組み合わせてセント（つぎはぎ詩）を生成するアルゴリズム的詩学。Allison Parrish『Articulations』(2018)、Stephanie Strickland等のデジタルセント実践群。",
    background="ローマ詩学のセント（Ausonius等）伝統、デジタル時代のテクスト操作技術。",
    development="2014-2024年で大規模コーパス埋め込みベースのセント生成が成熟、Parrish実践が世代を代表する事例となった。",
    historical_context="2014-2025年デジタルセント期。",
    primary_source_url="https://counterpathpress.org/articulations-allison-parrish",
    primary_source_type="Counterpath Press: Articulations (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("デジタルセントはコーパスベース作者性の代表的形式。")])

add(**C, name_ja="OuLiPo×LLM制約",
    name_en="OuLiPo + LLM constraints",
    name_original="OuLiPo + LLM constraint experiments",
    definition="ウリポ的形式制約とLLMを組み合わせる2023年以降の実験群。リポグラム、s+7、欠字法等の制約をLLMプロンプトに埋め込み、潜在的可能性の文学を計算的に拡張する詩学運動。",
    background="ウリポ伝統（1960-）、2023年LLM大衆化と制約プロンプト研究。",
    development="2023-2025年でウリポメンバー（Hervé Le Tellier等）がLLM実験を始動、現代制約詩学の最先端領域となった。",
    historical_context="2023-2025年ウリポ×AI期。",
    primary_source_url="https://oulipo.net/",
    primary_source_type="Oulipo: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("ウリポ×LLMは制約詩学のAI拡張を実現する。")],
    cross_domain=[cd("PHIL","形式と偶然","ウリポ×AIは形式制約の哲学とAIの交差点。")])

add(**C, name_ja="生成タイポグラフィ詩",
    name_en="Generative typography poetry",
    name_original="Generative typography poetry",
    definition="ProcessingやP5.js等の生成プログラミング環境で実装されるタイポグラフィ詩。Casey Reas、John Maeda等のデザイン研究系生成詩学の代表領域、視覚詩学とコードアートの交差点。",
    background="1990年代Maeda『Design By Numbers』、2001年Processing創設の系譜。",
    development="2010-2024年で生成タイポグラフィが視覚詩学・コードアートの中核領域として制度化された。",
    historical_context="1990-2025年生成タイポ詩学期。",
    primary_source_url="https://processing.org/",
    primary_source_type="Processing Foundation (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("生成タイポは視覚詩学とコード作者性の交差領域。")])

add(**C, name_ja="ASCIIアートLLM",
    name_en="ASCII art via LLM",
    name_original="ASCII art generation via LLM",
    definition="LLMによるASCIIアート生成研究と実践。2023年以降GPT-4・Claudeによる文字絵生成が研究対象化、視覚的記号と言語生成の交差領域として注目を集める。",
    background="ASCIIアートの古典的伝統、2023年マルチモーダルLLM時代。",
    development="2023-2025年でASCII LLM研究が学術論文化、視覚詩学とLLMの交差研究領域を形成した。",
    historical_context="2023-2025年LLM視覚詩学期。",
    primary_source_url=ARXIV+"2402.11753",
    primary_source_type="arXiv 2024: ASCII art LLM (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("LLM ASCII生成は視覚×言語の作者性交差領域。")])

add(**C, name_ja="Sora物語生成",
    name_en="Sora storytelling",
    name_original="OpenAI Sora storytelling",
    definition="2024年OpenAI公開の動画生成モデルSoraを使った物語生成実践。プロンプトから60秒動画を生成し、視覚物語と言語物語の融合領域を形成、映像文学のAI拡張領域の代表事例となった。",
    background="2024年2月Sora公開、動画生成モデルの成熟。",
    development="2024-2025年で短編動画文学・広告映像の制作実践が普及、視覚物語のAI生成研究の中核となった。",
    historical_context="2024-2025年動画生成物語期。",
    primary_source_url="https://openai.com/sora",
    primary_source_type="OpenAI: Sora (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Soraは視覚物語のAI生成を制度化した代表事例。")],
    cross_domain=[cd("AI-Development","動画生成モデル","Soraはマルチモーダル生成研究の中核。")])

add(**C, name_ja="Suno/Udio歌詞生成",
    name_en="Suno/Udio music+lyrics generation",
    name_original="Suno and Udio music+lyrics generation",
    definition="2023-2024年公開のAI楽曲生成サービスSunoとUdio。プロンプトから歌詞付き楽曲を生成し、音楽×言語生成の代表事例となり、2024年RIAA訴訟の対象となった。",
    background="2023年Suno（Cambridge MA）創業、2024年Udio公開。",
    development="2024年6月RIAA訴訟、AI楽曲・歌詞生成の著作権論議の中核事例となった。",
    historical_context="2023-2025年AI楽曲生成期。",
    primary_source_url="https://suno.com/",
    primary_source_type="Suno: official site (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Suno/Udioは音楽×歌詞生成のAI作者性論議の中核事例。")],
    cross_domain=[cd("AI-Development","マルチモーダル生成","音楽生成AIはマルチモーダル研究の代表事例。")])


# ============================================================
# C: 著作権・倫理深掘り（11件）
# ============================================================
add(**C, name_ja="NYT対OpenAI訴訟",
    name_en="NYT vs OpenAI lawsuit",
    name_original="The New York Times v. OpenAI (2023)",
    definition="2023年12月New York TimesがOpenAI・Microsoftを著作権侵害で提訴した訴訟。LLM学習データへのNYT記事の無許諾使用を巡り、訓練データのフェアユース論争の中核訴訟となった。",
    background="2023年LLM訓練データ論議の浮上、NYT記事のChatGPT再現実証。",
    development="2024-2025年で米著作権法のフェアユース範囲とAI訓練データの境界を確定する標準訴訟となった。",
    historical_context="2023-2025年訓練データ訴訟期。",
    primary_source_url="https://www.nytimes.com/2023/12/27/business/media/new-york-times-open-ai-microsoft-lawsuit.html",
    primary_source_type="NYT 2023 (primary report)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[fa_canon("NYT訴訟は訓練データの法的境界を確定する標準訴訟。")],
    cross_domain=[cd("AI-Development","訓練データ法","NYT訴訟はAI法理論議の中核事例。")])

add(**C, name_ja="Authors Guild集団訴訟2024",
    name_en="Authors Guild Class Action 2024",
    name_original="Authors Guild Class Action v. OpenAI (2023-2024)",
    definition="2023年9月Authors Guildが17人の著名作家（John Grisham、George R.R. Martin等）を代表してOpenAIを集団提訴した著作権訴訟。LLM学習データの作家著作権侵害を巡る代表訴訟。",
    background="2023年Authors Guild AI声明、Sarah Silverman訴訟との連鎖。",
    development="2024-2025年で米作家団体のAI法理論議の代表事例として展開中。",
    historical_context="2023-2025年作家団体集団訴訟期。",
    primary_source_url="https://authorsguild.org/news/authors-guild-john-grisham-jodi-picoult-david-baldacci-george-rr-martin-and-13-other-authors-file-class-action-suit-against-openai/",
    primary_source_type="Authors Guild 2023 (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[fa_authorship("Authors Guild訴訟は作家集団のAI法的反撃の代表事例。")])

add(**C, name_ja="GitHub Copilot訴訟",
    name_en="GitHub Copilot lawsuit",
    name_original="Doe v. GitHub (Copilot lawsuit, 2022)",
    definition="2022年11月Matthew Butterick等がGitHub・OpenAI・MicrosoftをCopilotのコード学習で集団提訴した訴訟。コードを著作物として保護する訓練データ訴訟の先駆事例で、後のNYT訴訟等への影響を与えた。",
    background="2021年GitHub Copilot公開、コードの著作権論議の浮上。",
    development="2023-2024年で部分的却下後継続、AI訓練データ訴訟の先駆判例となった。",
    historical_context="2022-2025年コード学習訴訟期。",
    primary_source_url="https://githubcopilotlitigation.com/",
    primary_source_type="Copilot Litigation: official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Copilot訴訟は訓練データ訴訟の先駆判例。")],
    cross_domain=[cd("AI-Development","コード生成AI","Copilot訴訟はコード×AIの法理論議の中核。")])

add(**C, name_ja="Getty対Stability AI訴訟",
    name_en="Getty Images v. Stability AI",
    name_original="Getty Images v. Stability AI (2023)",
    definition="2023年1月Getty ImagesがStability AIを画像著作権侵害で英米同時提訴した訴訟。Stable Diffusion訓練データへのGetty画像の無許諾使用を巡り、画像生成AIの著作権論議の中核訴訟となった。",
    background="2022年Stable Diffusion公開、画像訓練データの法的不確定性。",
    development="2023-2025年英国・米国両裁判所で進行中、画像生成AIの法的境界確定の代表訴訟となった。",
    historical_context="2023-2025年画像生成AI訴訟期。",
    primary_source_url="https://newsroom.gettyimages.com/en/getty-images/getty-images-statement",
    primary_source_type="Getty Images 2023 (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Getty訴訟は画像生成AIの法的境界を確定する代表事例。")])

add(**C, name_ja="Sarah Silverman対Meta",
    name_en="Sarah Silverman v. Meta",
    name_original="Silverman v. Meta (2023)",
    definition="2023年7月Sarah Silverman、Christopher Golden、Richard Kadrey等がMetaのLLaMA訓練データへのBooks3使用を巡って提訴した訴訟。Books3訴訟群の代表事例で、海賊版書籍コーパスの法的問題を可視化した。",
    background="2023年Books3コーパス（Bibliotik由来）のLLM訓練使用、海賊版書籍データ論議。",
    development="2023-2024年で関連訴訟群（Tremblay、Chabon、Awad等）と連動、Books3訴訟群の中核となった。",
    historical_context="2023-2025年Books3訴訟期。",
    primary_source_url="https://llmlitigation.com/",
    primary_source_type="LLM Litigation Hub (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Silverman訴訟は海賊版書籍コーパスの法的問題を可視化した。")])

add(**C, name_ja="Andersen対Stability AI",
    name_en="Andersen v. Stability AI",
    name_original="Andersen v. Stability AI (2023)",
    definition="2023年1月Sarah Andersen、Kelly McKernan、Karla Ortiz等のアーティストがStability AIを著作権侵害で提訴した集団訴訟。芸術家集団のAI訴訟代表事例で、画像生成AIの作者権論議の中核となった。",
    background="2022年Stable Diffusion公開、芸術家コミュニティのAI懸念。",
    development="2023-2025年で部分却下・修正後継続、芸術家集団のAI法的反撃の代表事例となった。",
    historical_context="2023-2025年芸術家集団訴訟期。",
    primary_source_url="https://stablediffusionlitigation.com/",
    primary_source_type="Stable Diffusion Litigation (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Andersen訴訟は芸術家集団のAI法的反撃の代表事例。")])

add(**C, name_ja="RIAA Suno/Udio訴訟",
    name_en="RIAA v. Suno and Udio",
    name_original="RIAA v. Suno and Udio (2024)",
    definition="2024年6月RIAAがSunoとUdioを著作権侵害で提訴した楽曲生成訴訟。Sony Music、Universal Music、Warner Recordsが原告、楽曲生成AIの訓練データ法理論議の中核訴訟となった。",
    background="2024年Suno・Udio普及、楽曲生成AIの著作権論議の浮上。",
    development="2024-2025年で楽曲訓練データ訴訟の代表事例として展開中、画像・テクストに続く第三領域の法理形成中。",
    historical_context="2024-2025年楽曲AI訴訟期。",
    primary_source_url="https://www.riaa.com/record-companies-bring-landmark-cases-for-responsible-ai-against-suno-and-udio-in-boston-and-new-york-federal-courts-respectively/",
    primary_source_type="RIAA 2024 (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("RIAA訴訟は楽曲AI訓練データ法理の代表事例。")])

add(**C, name_ja="WGA AIストライキ2023",
    name_en="WGA AI strike 2023",
    name_original="Writers Guild of America AI strike 2023",
    definition="2023年5-9月Writers Guild of America 148日間ストライキ。脚本家のAI使用規制を中心要求とし、最終合意でAI脚本の正式制限が獲得された、労働運動×AIの代表事例。",
    background="2023年LLM脚本生成普及、ハリウッド脚本家コミュニティの危機感。",
    development="2023年9月合意、AI脚本使用の正式制限獲得、SAG-AFTRA連動ストライキへの先駆となった。",
    historical_context="2023-2024年労働×AI規範形成期。",
    primary_source_url="https://www.wgacontract2023.org/",
    primary_source_type="WGA: official site (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[fa_authorship("WGAストはAI規制を労働運動として制度化した代表事例。")],
    cross_domain=[cd("AI-Development","AI労働規範","WGAストはAI労働規範の代表事例。")])

add(**C, name_ja="SAG-AFTRA AIスト",
    name_en="SAG-AFTRA AI strike",
    name_original="SAG-AFTRA AI strike (2023)",
    definition="2023年7-11月SAG-AFTRA俳優組合の118日間ストライキ。俳優のデジタルレプリカ・AI演技規制を中心要求、最終合意で俳優のAI同意権・対価権が獲得された。",
    background="2023年WGAスト連動、俳優のAI複製技術への危機感。",
    development="2023年11月合意、俳優AI同意権の正式獲得、芸能労働×AIの代表事例となった。",
    historical_context="2023-2024年芸能労働×AI期。",
    primary_source_url="https://www.sagaftra.org/",
    primary_source_type="SAG-AFTRA: official (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[fa_authorship("SAG-AFTRAストは俳優のAI同意権を制度化した。")])

add(**C, name_ja="EU AI法文学条項",
    name_en="EU AI Act literary provisions",
    name_original="EU AI Act (2024) Article 53 literary provisions",
    definition="2024年5月EU理事会採択のAI法（Regulation 2024/1689）第53条等の文学関連条項。汎用AI提供者に訓練データの著作権遵守と公開を義務付け、EUのAI法的枠組みの中核条項となった。",
    background="2021年AI法草案、EU議会・理事会の3年議論、2024年5月最終採択。",
    development="2024-2026年で段階適用、世界AI規制の標準モデルとして影響を拡大中。",
    historical_context="2021-2026年EU AI法形成期。",
    primary_source_url="https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689",
    primary_source_type="EUR-Lex: AI Act 2024 (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[fa_canon("EU AI法は訓練データ法的枠組みの世界標準を形成した。")],
    cross_domain=[cd("AI-Development","AI規制","EU AI法はAI法的枠組みの世界標準。")])

add(**C, name_ja="日本AI著作権30条の4",
    name_en="Japan AI fair use article 30-4",
    name_original="Japan Copyright Act Article 30-4",
    definition="2018年改正日本著作権法第30条の4。AI訓練データのための著作物利用を原則自由化する条文で、世界最先進的なAI訓練データ条項として国際的に注目を集める。",
    background="2018年日本著作権法改正、TPP対応とAI政策の連動。",
    development="2023年文化庁検討会指針、2024年AI×著作権の論点整理が世界的議論の中核となった。",
    historical_context="2018-2025年日本AI著作権制度期。",
    primary_source_url="https://www.bunka.go.jp/seisaku/chosakuken/aiandcopyright.html",
    primary_source_type="文化庁: AIと著作権 (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[fa_canon("30条の4は日本のAI訓練データ法制の世界先進事例。")],
    cross_domain=[cd("AI-Development","AI法制","30条の4は日本AI法制の中核条項。")])


# ============================================================
# D: デジタル人文学深掘り（10件）
# ============================================================
add(**C, name_ja="DARIAH-EU",
    name_en="DARIAH-EU",
    name_original="Digital Research Infrastructure for the Arts and Humanities",
    definition="2014年設立のEUデジタル人文学研究インフラ。21カ国・90機関を統合し、欧州DH研究の連携基盤として制度化、世界最大規模のDH研究インフラとなった。",
    background="2008年DARIAH準備期、欧州研究インフラ戦略フォーラム（ESFRI）採択。",
    development="2014-2024年で欧州DH研究の中核インフラとなり、CLARINと並ぶ欧州DH双璧となった。",
    historical_context="2008-2025年欧州DHインフラ期。",
    primary_source_url="https://www.dariah.eu/",
    primary_source_type="DARIAH-EU: official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("DARIAH-EUは欧州DH研究の制度化基盤。")])

add(**C, name_ja="CLARIN",
    name_en="CLARIN",
    name_original="Common Language Resources and Technology Infrastructure",
    definition="2012年設立の欧州言語資源インフラ。22カ国の言語コーパス・ツールを統合、計算言語学とDH研究の欧州標準インフラとして制度化された。",
    background="2008年CLARIN準備期、欧州言語技術戦略との連動。",
    development="2012-2024年でDARIAH-EUと並ぶ欧州DH双璧、計算文学研究の言語資源基盤として機能。",
    historical_context="2008-2025年欧州言語インフラ期。",
    primary_source_url="https://www.clarin.eu/",
    primary_source_type="CLARIN: official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("CLARINは計算文学の言語資源基盤を制度化。")])

add(**C, name_ja="Open Greek and Latin",
    name_en="Open Greek and Latin",
    name_original="Open Greek and Latin Project",
    definition="Leipzig大学Gregory Crane主導の古典ギリシア語・ラテン語デジタル化プロジェクト。古典文献全2,000万語を構造化XMLで提供し、古典研究のDH中核インフラとなった。",
    background="2014年Crane Leipzig移籍、Perseus Project系譜の拡張。",
    development="2014-2024年で古典文献のオープンデジタル化を推進、古典DH研究の世界標準データ源となった。",
    historical_context="2014-2025年古典オープンデジタル化期。",
    primary_source_url="https://www.dh.uni-leipzig.de/wo/projects/open-greek-and-latin/",
    primary_source_type="Leipzig DH: OGL (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("OGLは古典文献のオープンデジタル化を制度化した。")],
    cross_domain=[cd("PHIL","古典文献","OGLは哲学古典研究の基盤データ。")])

add(**C, name_ja="Perseus Catalog",
    name_en="Perseus Catalog",
    name_original="Perseus Digital Library Catalog",
    definition="1985年設立のTufts大学Perseus Digital Libraryのカタログシステム。古典文献の権威的書誌記述（CTS URN）を提供し、古典DHの中核基盤となり、世界の古典研究の標準書誌枠組みとなった。",
    background="1985年Crane Perseus創設、古典文献のデジタル化先駆。",
    development="1995-2024年でCTS（Canonical Text Services）プロトコルが古典DHの世界標準書誌規格となった。",
    historical_context="1985-2025年Perseus基盤期。",
    primary_source_url="http://catalog.perseus.org/",
    primary_source_type="Perseus: official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("PerseusはDH古典書誌の世界標準を確立した。")])

add(**C, name_ja="Homer Multitext Project",
    name_en="Homer Multitext Project",
    name_original="Homer Multitext Project",
    definition="2000年Casey Dué、Mary Ebbott主導のホメロス写本デジタル化プロジェクト。Venetus A等の写本を高解像度デジタル化し、ホメロスの口承伝承を多元的版本として可視化する代表DHプロジェクト。",
    background="2000年Center for Hellenic Studies創設、口承伝統研究の系譜。",
    development="2000-2024年でホメロス研究のDH標準モデル、写本ベース古典研究の世界先駆事例となった。",
    historical_context="2000-2025年ホメロス多版本期。",
    primary_source_url="https://www.homermultitext.org/",
    primary_source_type="HMT: official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("HMTは口承伝統の多元的写本DHを制度化した。")])

add(**C, name_ja="EVT XMLエディタ",
    name_en="EVT (Edition Visualization Technology)",
    name_original="Edition Visualization Technology",
    definition="ピサ大学開発のTEI XMLベース版本可視化ツール。デジタル批評版の表示・比較を実現し、欧州DH研究の中核ツールとして広く採用された。",
    background="2010年代ピサ大学DH研究、TEI版本可視化需要。",
    development="2014-2024年で欧州デジタル批評版の標準ツール、Edirom等と並ぶ版本DH双璧となった。",
    historical_context="2010-2025年デジタル批評版期。",
    primary_source_url="http://evt.labcd.unipi.it/",
    primary_source_type="EVT Pisa (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_canon("EVTはデジタル批評版の標準ツールを実現した。")])

add(**C, name_ja="Edirom",
    name_en="Edirom",
    name_original="Edirom",
    definition="Detmold音楽大学開発のデジタル音楽批評版基盤。MEI（Music Encoding Initiative）と連動し、音楽×文学のDH研究領域の中核基盤となった。",
    background="2006年Edirom研究プロジェクト開始、音楽デジタル批評版需要。",
    development="2010-2024年で音楽DH研究の世界標準基盤、文学×音楽研究の交差領域基盤となった。",
    historical_context="2006-2025年音楽DH期。",
    primary_source_url="https://www.edirom.de/",
    primary_source_type="Edirom (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="MEI音楽エンコーディング",
    name_en="MEI (Music Encoding Initiative)",
    name_original="Music Encoding Initiative",
    definition="2003年設立のXMLベース音楽記譜エンコーディング国際標準。TEIの音楽版として、楽譜のデジタル批評版・歌曲文学研究のDH基盤となった。",
    background="2003年MEI Council設立、TEI音楽版需要。",
    development="2010-2024年で音楽DH研究の世界標準、歌曲・オペラの言語×音楽分析の基盤となった。",
    historical_context="2003-2025年音楽エンコーディング期。",
    primary_source_url="https://music-encoding.org/",
    primary_source_type="MEI: official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_canon("MEIは音楽×文学DH研究の基盤標準。")])

add(**C, name_ja="IIIF",
    name_en="IIIF (International Image Interoperability Framework)",
    name_original="International Image Interoperability Framework",
    definition="2011年設立のデジタル画像相互運用標準。世界の図書館・美術館の画像コレクション統合を実現、DH研究の画像基盤として制度化された。",
    background="2011年Stanford、Oxford、BNF等の主要機関連携、画像相互運用需要。",
    development="2015-2024年で世界の主要図書館・美術館がIIIF採用、Mirador・Universal Viewer等のビューアが標準化された。",
    historical_context="2011-2025年画像相互運用期。",
    primary_source_url="https://iiif.io/",
    primary_source_type="IIIF Consortium (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("IIIFはDH画像研究の世界標準基盤。")])

add(**C, name_ja="Miradorビューア",
    name_en="Mirador viewer",
    name_original="Mirador (IIIF image viewer)",
    definition="Stanford大学主導のIIIFベース画像ビューア。複数機関の画像コレクションを統合表示し、DH画像研究の世界標準ビューアとなった。",
    background="2014年Stanford SUL開発、IIIF採用拡大。",
    development="2018-2024年でMirador 3公開、世界の主要図書館・美術館の標準ビューアとして制度化された。",
    historical_context="2014-2025年IIIFビューア期。",
    primary_source_url="https://projectmirador.org/",
    primary_source_type="Mirador: official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# E: 機械学習×文学研究（8件）
# ============================================================
add(**C, name_ja="BookNLP",
    name_en="BookNLP",
    name_original="BookNLP (Bamman et al.)",
    definition="David Bamman主導の長編小説向けNLPパイプライン。キャラクター・場所・出来事の抽出を実装し、文学的NLP研究の標準ツールとして世界的に普及した。",
    background="2014年Bamman博士研究、長編小説NLPの研究需要。",
    development="2017-2024年でPython BookNLP（GitHub）として再実装、世界の計算文学研究の標準ツールとなった。",
    historical_context="2014-2025年長編NLP期。",
    primary_source_url=GITHUB+"booknlp/booknlp",
    primary_source_type="BookNLP GitHub (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("BookNLPは長編小説NLP研究の世界標準。")],
    cross_domain=[cd("AI-Development","NLP","BookNLPはNLP研究の文学応用代表事例。")])

add(**C, name_ja="キャラクターネットワーク分析",
    name_en="Character network analysis",
    name_original="Character network analysis (Elson, Grayson, etc.)",
    definition="小説のキャラクター間関係を社会ネットワーク分析で可視化する研究。Elson et al.(2010)、Grayson et al.(2016)等で確立、計算文学研究の中核手法となった。",
    background="2010年Elson『Extracting social networks from literary fiction』、社会ネットワーク分析の文学応用。",
    development="2010-2024年でキャラネットワーク分析が計算文学研究の標準手法、シェイクスピア・ヴィクトリア朝文学等で応用された。",
    historical_context="2010-2025年キャラネット研究期。",
    primary_source_url="https://aclanthology.org/P10-1015/",
    primary_source_type="ACL 2010: Elson (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("キャラネットワーク分析は計算文学の標準手法。")])

add(**C, name_ja="センチメントアーク",
    name_en="Sentiment arc analysis",
    name_original="Reagan et al. emotional arcs (2016)",
    definition="Andy Reagan、Lewis Mitchell等(2016)の『EPJ Data Science』論文。1,327作品のセンチメントアーク分析で6つの感情アークパターン（『Rags to Riches』『Icarus』等）を実証、計算文学のランドマーク研究となった。",
    background="2015-2016年Vermont Computational Story Lab、Vonnegutの感情曲線理論の計算検証。",
    development="2016-2024年でVonnegutストーリーアーク仮説の計算的実証として広く引用、計算文学研究の代表事例となった。",
    historical_context="2016-2025年センチメントアーク期。",
    primary_source_url="https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-016-0093-1",
    primary_source_type="EPJ Data Science 2016 (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("センチメントアークはVonnegut仮説を計算的に実証した代表研究。")],
    cross_domain=[cd("AI-Development","感情分析","センチメントアークはNLP感情分析の文学応用。")])

add(**C, name_ja="NarrativeQAデータセット",
    name_en="NarrativeQA dataset",
    name_original="NarrativeQA Reading Comprehension dataset (Kočiský et al. 2018)",
    definition="2018年DeepMindのKočiský et al.が公開した長編物語読解QAデータセット。1,567作品の脚本・小説からの質問応答データで、長編物語AI読解研究の標準ベンチマークとなった。",
    background="2017-2018年DeepMind読解研究、長編物語AI読解需要。",
    development="2018-2024年で長編物語AI研究の標準ベンチマーク、BookSum等の後継データセットへの基盤となった。",
    historical_context="2018-2025年長編物語AI期。",
    primary_source_url=ARXIV+"1712.07040",
    primary_source_type="arXiv 2018: NarrativeQA (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("NarrativeQAは長編物語AI研究の標準ベンチマーク。")],
    cross_domain=[cd("AI-Development","読解QA","NarrativeQAはNLP研究の文学応用。")])

add(**C, name_ja="Toronto BookCorpus論争",
    name_en="Toronto BookCorpus controversy",
    name_original="Toronto BookCorpus controversy",
    definition="2015年Zhu et al.公開のBookCorpus（11,000冊書籍）を巡る著作権論議。BERT等の主要LLMの訓練データとなったが2021年Bandyらが指摘した著作権侵害問題で、訓練データ倫理論議の代表事例となった。",
    background="2015年BookCorpus公開、BERT・GPT-2等の標準訓練データ化。",
    development="2021年Bandy & Vincent批評論文公開、世界の主要LLM訓練データの倫理問題が可視化された。",
    historical_context="2015-2025年訓練データ倫理期。",
    primary_source_url=ARXIV+"2105.05241",
    primary_source_type="arXiv 2021: Bandy & Vincent (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("BookCorpus論争はLLM訓練データ倫理の代表事例。")])

add(**C, name_ja="FLORES翻訳ベンチマーク",
    name_en="FLORES translation benchmark",
    name_original="FLORES-200 (Meta AI 2022)",
    definition="2022年Meta AI公開の200言語機械翻訳ベンチマーク。文学的テクストを含む3,001文で多言語翻訳評価を実装、機械翻訳研究の世界標準となった。",
    background="2019年FLORES-101、2022年FLORES-200拡張、低資源言語翻訳需要。",
    development="2022-2024年で世界の機械翻訳研究の標準ベンチマーク、文学翻訳AI研究の評価基盤となった。",
    historical_context="2022-2025年200言語MT期。",
    primary_source_url=GITHUB+"facebookresearch/flores",
    primary_source_type="FLORES GitHub (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("FLORESは文学翻訳AI評価の世界標準。")],
    cross_domain=[cd("AI-Development","機械翻訳","FLORESはMT研究の標準ベンチマーク。")])

add(**C, name_ja="BookSum要約データセット",
    name_en="BookSum summarization dataset",
    name_original="BookSum (Kryściński et al. 2021)",
    definition="2021年Salesforce Research公開の長編書籍要約データセット。チャプター・セクション・全書籍の3レベル要約を実装し、長編要約AI研究の標準ベンチマークとなった。",
    background="2021年GPT-3普及、長編要約AI研究需要。",
    development="2021-2024年で長編要約研究の標準ベンチマーク、BookCorpus等とともに文学AI研究の中核データとなった。",
    historical_context="2021-2025年長編要約AI期。",
    primary_source_url=ARXIV+"2105.08209",
    primary_source_type="arXiv 2021: BookSum (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("BookSumは長編要約AI研究の標準ベンチマーク。")],
    cross_domain=[cd("AI-Development","要約","BookSumはNLP要約研究の文学応用。")])

add(**C, name_ja="ジェンダー検出物語分析",
    name_en="Gender detection in narrative",
    name_original="Gender detection in literary narrative (Underwood et al. 2018)",
    definition="Ted Underwood、David Bamman等(2018)の計算文学研究。1880-2007年米英小説におけるキャラクター・ジェンダー表現の計量的変化を実証、計算文学のジェンダー研究代表事例となった。",
    background="2017年Underwood『Distant Horizons』、ジェンダー計算文学研究の系譜。",
    development="2018-2024年でジェンダー計算文学研究の標準参照、Underwood等の代表研究として制度化された。",
    historical_context="2018-2025年ジェンダー計算文学期。",
    primary_source_url="https://culturalanalytics.org/article/13145",
    primary_source_type="JCA 2018: Underwood (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("ジェンダー計算文学研究は計量文学の代表事例。")])


# ============================================================
# F: プラットフォーム文学（5件）
# ============================================================
add(**C, name_ja="Substack文学プラットフォーム",
    name_en="Substack as literary platform",
    name_original="Substack literary platform",
    definition="2017年設立のニュースレター配信サービス。George Saunders、Roxane Gay、Salman Rushdie等の作家が利用し、サブスクリプション型文学発表プラットフォームとして文学経済を変容させた。",
    background="2017年Chris Best、Hamish McKenzie創業、サブスクニュースレター市場形成。",
    development="2020-2024年で文学者・批評家のサブスク発表が定着、伝統的文芸誌経済を脱構築する代表事例となった。",
    historical_context="2017-2025年サブスク文学期。",
    primary_source_url="https://substack.com/",
    primary_source_type="Substack: official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_recv("Substackはサブスク文学経済を制度化した代表事例。")])

add(**C, name_ja="NotebookLM研究者ツール",
    name_en="NotebookLM as research-author tool",
    name_original="Google NotebookLM",
    definition="2023年Google公開のAI研究ノートブック。Gemini基盤で文書群を要約・統合し、研究者・作家のリサーチ補助ツールとして急速に普及、知識生産の代表的AI事例となった。",
    background="2023年Google AI推進、研究者向けAI需要。",
    development="2023-2024年でAudio Overview機能追加、研究者・作家・教育者の世界標準ツールとなった。",
    historical_context="2023-2025年AI研究ノート期。",
    primary_source_url="https://notebooklm.google.com/",
    primary_source_type="Google NotebookLM (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("NotebookLMは研究者×AIの協働ツール代表事例。")],
    cross_domain=[cd("AI-Development","RAG","NotebookLMはRAG技術の代表応用事例。")])

add(**C, name_ja="Obsidian執筆コミュニティ",
    name_en="Obsidian writing community",
    name_original="Obsidian writing community",
    definition="2020年公開のObsidianを中心とする執筆コミュニティ。Markdownベースのナレッジ管理ツールが作家・研究者に普及し、Roam Researchと並ぶ思考執筆ツールの双璧となった。",
    background="2020年Obsidian公開、Roam Research競合、Markdown執筆需要。",
    development="2021-2024年で世界規模の執筆コミュニティ形成、作家・学者の標準ツールとして制度化された。",
    historical_context="2020-2025年Markdown執筆期。",
    primary_source_url="https://obsidian.md/",
    primary_source_type="Obsidian: official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="Scrivener執筆環境",
    name_en="Scrivener legacy",
    name_original="Scrivener (Literature & Latte)",
    definition="2007年Keith Blount開発のプロ作家向け執筆環境。長編小説・脚本・論文の構造的執筆を支援し、20年に渡って世界の作家コミュニティで標準化された執筆ソフトウェアとなった。",
    background="2007年Literature & Latte創業、長編執筆ツール需要。",
    development="2007-2024年で世界の作家コミュニティの標準ツール、ScrivenerからNotion・Obsidianへの世代交代の起点。",
    historical_context="2007-2025年長編執筆環境期。",
    primary_source_url="https://www.literatureandlatte.com/scrivener/",
    primary_source_type="L&L: Scrivener (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Scrivenerは長編執筆環境の世界標準。")])

add(**C, name_ja="iA Writer文学",
    name_en="iA Writer minimalism",
    name_original="iA Writer (Information Architects)",
    definition="2010年Information Architects開発のミニマル執筆ソフト。Markdown・モノスペースフォント・タイプライターモードで執筆環境のミニマリズム潮流を確立、執筆ツール思想の代表事例となった。",
    background="2010年iPad執筆需要、ミニマル執筆潮流。",
    development="2010-2024年で執筆ミニマリズムの代表ツール、Ulysses等と並ぶApple系執筆ツールの双璧となった。",
    historical_context="2010-2025年執筆ミニマリズム期。",
    primary_source_url="https://ia.net/writer",
    primary_source_type="iA Writer: official (primary)",
    importance_score=2, source_tier="primary", canonical_in_region="minor")


# ============================================================
# G: 即興・パフォーマンス・教育・アクセシビリティ（5件）
# ============================================================
add(**C, name_ja="ラブレース・テスト",
    name_en="Lovelace Test for AI creativity",
    name_original="Lovelace Test (Bringsjord et al. 2003)",
    definition="2003年Selmer Bringsjord、Paul Bello、David Ferrucci提唱のAI創造性テスト。チューリングテストの代替として、AI創造性を作者の意図的予期不能性で評価する哲学的枠組み。",
    background="2003年Bringsjord論文、チューリングテストの限界批判。",
    development="2003-2024年でAI創造性論議の標準枠組み、生成AI時代に再注目される代表的創造性テストとなった。",
    historical_context="2003-2025年AI創造性論議期。",
    primary_source_url="https://philpapers.org/rec/BRICAA",
    primary_source_type="Bringsjord 2003 (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("ラブレース・テストはAI創造性論議の標準枠組み。"),
                 fa_auth("ラブレース・テストはAI創造性の真正性検証枠組み。")],
    cross_domain=[cd("PHIL","創造性","ラブレース・テストは創造性哲学の代表概念。"),
                  cd("AI-Development","AI創造性","ラブレース・テストはAI創造性研究の中核。")])

add(**C, name_ja="Khanmigo執筆指導",
    name_en="Khanmigo writing coaching",
    name_original="Khanmigo (Khan Academy AI tutor)",
    definition="2023年Khan Academy公開のGPT-4ベースAI家庭教師。執筆指導機能で教育的AI活用の代表事例となり、世界規模で創作教育のAI統合モデルを形成した。",
    background="2023年OpenAI×Khan Academy提携、教育AI需要。",
    development="2023-2024年で世界規模の教育AI事例、執筆指導機能で創作教育の代表モデルとなった。",
    historical_context="2023-2025年教育AI執筆期。",
    primary_source_url="https://www.khanmigo.ai/",
    primary_source_type="Khanmigo: official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Khanmigoは教育AI×創作の代表事例。")],
    cross_domain=[cd("AI-Development","教育AI","Khanmigoは教育AIの代表事例。")])

add(**C, name_ja="Microsoft Copilot小説執筆",
    name_en="Microsoft Copilot in Word for fiction",
    name_original="Microsoft 365 Copilot for fiction",
    definition="2023年Microsoft公開のCopilot in Word機能。GPT-4ベースで小説執筆支援を実装し、Word文書の標準執筆AIとして世界規模の作家コミュニティに普及した。",
    background="2023年Microsoft×OpenAI提携、Office AI統合戦略。",
    development="2023-2024年で世界Office利用者へのAI執筆機能展開、AI執筆の大衆化を駆動した。",
    historical_context="2023-2025年Office AI執筆期。",
    primary_source_url="https://www.microsoft.com/en-us/microsoft-365/copilot",
    primary_source_type="Microsoft 365 Copilot (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Office Copilotは大衆AI執筆の代表事例。")])

add(**C, name_ja="AIオーディオブック",
    name_en="AI-generated audiobooks",
    name_original="Apple Books / Audible AI narration",
    definition="2023年Apple Books、2024年Audibleが導入したAI朗読オーディオブック。人間ナレーターを代替するAI音声合成技術で、オーディオブック市場のAI拡張を駆動、SAG-AFTRAストの主要争点ともなった。",
    background="2023年Apple Books AI朗読公開、音声合成技術の成熟。",
    development="2023-2025年でAmazon Audible・Spotify等の主要プラットフォームがAI朗読導入、市場構造変動が進行中。",
    historical_context="2023-2025年AIオーディオ期。",
    primary_source_url="https://authors.apple.com/support/4519-digital-narration-audiobooks",
    primary_source_type="Apple Books (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_recv("AIオーディオブックは聴覚文学のAI拡張代表事例。")],
    cross_domain=[cd("AI-Development","音声合成","AIオーディオブックは音声合成の代表応用。")])

add(**C, name_ja="エクフラシスとしての代替テクスト",
    name_en="Alt-text as ekphrasis",
    name_original="Alt-text as ekphrasis (Kleege 2018)",
    definition="2018年Georgina Kleege『More than Meets the Eye』提唱のアクセシビリティ詩学。スクリーンリーダー向け代替テクスト（alt text）を古代エクフラシス伝統の現代的継承として再定位する詩学理論。",
    background="2010年代Kleege盲目研究、アクセシビリティ詩学の系譜。",
    development="2018-2024年で代替テクスト詩学が学術領域として確立、アクセシビリティ×詩学の代表事例となった。",
    historical_context="2018-2025年アクセシビリティ詩学期。",
    primary_source_url="https://academic.oup.com/book/27660",
    primary_source_type="OUP: Kleege 2018 (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("代替テクスト詩学はアクセシビリティ×文学の代表事例。"),
                 fa_recv("代替テクストは新しい文学受容形式を制度化する。")],
    cross_domain=[cd("PT","エクフラシス","代替テクストはエクフラシス詩学の現代継承。")])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
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
            for cdi in cross_domain:
                try:
                    db.insert_cross_domain(
                        lit_entity_type="concept", lit_entity_id=cid,
                        target_db=cdi["target_db"], link_type=cdi["link_type"],
                        target_entity_id=cdi.get("target_entity_id"),
                        target_entity_name=cdi.get("target_entity_name"),
                        description=cdi.get("description"))
                    cd_count += 1
                except LitDBError as e:
                    print(f"  [warn] cross_domain failed for {entry['name_ja']}: {e}")

        summary = db.progress_summary()
        print(f"[wave19-c39-add60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave19-c39-add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
