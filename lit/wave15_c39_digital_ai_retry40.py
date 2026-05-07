"""LIT-DB Phase 2 Wave 15 — C39 Digital Humanities & AI Era ADD 40 (RETRY).

Subfield: lit_digital_ai (id=24), region='理論'.
Existing 111 concepts cover DH/AI core. This wave ADDS 40 NEW concepts:
  A: AI literary criticism (5) — PEN AI statement, SFWA AI ban, NaNoWriMo
     controversy, AI authorship debates, Kindle AI flood.
  B: Generative deeper (8) — Botnik, Janelle Shane, AI Dungeon, NovelAI,
     Sudowrite, Character.AI, Replika, NaNoGenMo theory.
  C: Prompt as literature (3) — prompting as ekphrasis, jailbreak-as-
     transgression, prompt engineering manuals as poetics.
  D: Interactive (5) — Choice of Games, Inkle studio, Bitsy, Hidden Door,
     Twine ecosystem theory.
  E: Social media literature (5) — Twitter fiction, hashtag fiction,
     Insta-poetry critique, BookTok, BookTube.
  F: Webnovel (6) — Wattpad, Royal Road, 起点中文网, 小説家になろう,
     isekai theory, system novel theory.
  G: Academic infrastructure (4) — DSH journal, ADHO, Internet Archive
     corpus, Google Books project.
  H: Ethics (4) — Stochastic Parrots paper, Bender Octopus, Crawford Atlas
     of AI, Gender Shades audit.

Verification policy:
  - 'primary'  -> manifesto / primary scholarly paper / archived program /
                  reference release / official statement.
  - 'secondary' -> canonical scholarly synthesis (Britannica, SEP,
                   academic-grade Wikipedia, peer-reviewed survey).
  - 'tertiary' -> synthetic critical category for taxonomic completeness.

Targets: ~50% primary, fourth_axes>=25, cross_domain>=18.
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
ACM = "https://dl.acm.org/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_digital_ai", region="理論",
         original_script="roman", period_key="デジタル人文学・AI時代")


# ============================================================
# A: AI文学批評（5件）
# ============================================================
add(**C, name_ja="PEN America AI声明",
    name_en="PEN America AI statement",
    name_original="PEN America AI statement (2023)",
    definition="2023年PEN AmericaがAIと作家の権利・表現の自由・著作権について発表した声明。作家コミュニティの公式立場を表明し、AI訓練データの透明性と作家への公正な対価を要求した。",
    background="2022-2023年LLMの大衆化とAuthors Guild訴訟、作家コミュニティの危機感。",
    development="2024-2025年に各国作家団体（Society of Authors UK、日本ペンクラブ等）が同様の声明を発表する連鎖反応を起こした。",
    historical_context="2023-2025年作家団体のAI論議制度化期。",
    primary_source_url="https://pen.org/ai-and-human-creativity/",
    primary_source_type="PEN America: AI statement (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"PEN声明はAI時代の作者性権利を制度的に再定義する作家団体の集合的応答。",
         "related_ai_phenomenon":"作家団体のAI規範化"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI倫理規範",
         "description":"PEN声明はAI開発倫理と作家権利の交差点。"}])

add(**C, name_ja="SFWA AI禁止規定",
    name_en="SFWA AI ban",
    name_original="SFWA AI submission ban (2023)",
    definition="2023年Science Fiction and Fantasy Writers Associationが会員資格・受賞対象作品からAI生成テクストを排除した規定。Clarkesworld誌のAI投稿急増問題を契機とし、SFジャンルのAI境界規範を確立した。",
    background="2023年初頭Clarkesworld誌へのAI生成投稿急増（月数百件）、編集休止事件。",
    development="2023-2024年Hugo Awards、Nebula Awards、世界SF業界がAI排除規範を制度化、AI境界規範の中核事例となった。",
    historical_context="2023-2025年ジャンル文学のAI境界規範化期。",
    primary_source_url="https://www.sfwa.org/2023/02/24/clarkesworld-and-the-ai-problem/",
    primary_source_type="SFWA: official statement (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"SFWA規定はジャンル文学コミュニティが集合的にAI作者性を排除する規範形成の典型。",
         "related_ai_phenomenon":"ジャンル業界のAI排除規範"}])

add(**C, name_ja="NaNoWriMo論争",
    name_en="NaNoWriMo AI controversy",
    name_original="NaNoWriMo AI controversy (2024)",
    definition="2024年National Novel Writing Month主催団体がAI使用容認声明を出したことで作家コミュニティが分裂、理事辞任・スポンサー離脱が相次いだ事件。AI障害者支援論と作家性権利論が衝突した。",
    background="2024年9月NaNoWriMo公式FAQでAI使用を「個人の選択」と容認、エイブリズム論への配慮を理由に挙げた。",
    development="2024-2025年で作家コミュニティが組織分裂、代替コミュニティ（NaNoMo Rebellion等）が複数派生した。",
    historical_context="2024-2025年作家コミュニティのAI分裂期。",
    primary_source_url=WIKI_EN+"National_Novel_Writing_Month",
    primary_source_type="Wikipedia: NaNoWriMo (controversy section)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"NaNoWriMo論争はアクセシビリティと作者性権利の対立を可視化したコミュニティ分裂事例。",
         "related_ai_phenomenon":"作家コミュニティのAI分裂"}])

add(**C, name_ja="AI著作者性論争",
    name_en="AI authorship debates",
    name_original="AI authorship debates",
    definition="LLM生成テクストにおける著作者性帰属を巡る2022-2025年の理論論議。Mark Lemley、James Grimmelmann、Pamela Samuelson等の法学者が著作権法の根本概念を再検討し、判例形成が進行中。",
    background="2022-2023年LLM大衆化と作家性帰属の法的不確定性、Thaler v. Perlmutter判例（2023）。",
    development="2024-2025年米欧で判例蓄積、EU AI法・米著作権局指針が形成中、根本理論論議が活発化。",
    historical_context="2022-2025年AI著作者性法理論議期。",
    primary_source_url="https://www.copyright.gov/ai/",
    primary_source_type="US Copyright Office: AI guidance (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"AI著作者性論争は近代以降の作者概念を法的・理論的に根本から再検討する。",
         "related_ai_phenomenon":"作者概念の法的解体"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"作者性の哲学",
         "description":"AI著作者性論争は法と哲学の交差点。"}])

add(**C, name_ja="Kindle AI洪水",
    name_en="Kindle Direct AI flood",
    name_original="Kindle Direct Publishing AI flood",
    definition="2023-2024年Amazon Kindle Direct Publishingに大量のAI生成書籍が氾濫した現象。著名作家の盗作疑惑書籍、要約書籍、低品質ゴーストキンドル書籍が問題化、Amazon側が日次出版冊数制限を導入した。",
    background="2023年GPT-4・Claude大衆化、ノーコード出版ツール（Sudowrite等）の成熟。",
    development="2023年9月Amazon日次3冊制限導入、2024年AI明示規定追加、世界出版業界のAI規範形成期となった。",
    historical_context="2023-2025年大衆出版プラットフォームのAI氾濫期。",
    primary_source_url="https://www.theverge.com/2023/9/19/23881035/amazon-kdp-ai-publishing-limits-3-books",
    primary_source_type="The Verge 2023: Amazon AI book limits (primary report)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"AI洪水は大衆出版市場の品質基準と正典形成過程を根本的に攪乱した。",
         "related_ai_phenomenon":"出版市場のAI氾濫"}])


# ============================================================
# B: 生成系深化（8件）
# ============================================================
add(**C, name_ja="NaNoGenMo理論",
    name_en="NaNoGenMo theory",
    name_original="National Novel Generation Month theory",
    definition="2013年Darius Kazemi提唱のNaNoGenMoを巡る生成文学理論。「50,000語の小説をコードで生成する」課題の理論的・美学的解釈、Allison Parrish、Nick Montfort、Mark Sample等による生成詩学の形成期。",
    background="2013年Kazemi GitHub Issue創設、e-literature・generative artコミュニティの拡張。",
    development="2013-2024年で世界の生成文学実践の中核イベント、Allison Parrish『Articulations』、Liza Daly『Seraphs』等の傑作が産出された。",
    historical_context="2013-2025年生成文学制度化期。",
    primary_source_url=GITHUB+"NaNoGenMo/2024",
    primary_source_type="NaNoGenMo GitHub (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"NaNoGenMoは生成行為そのものを文学実践として制度化した先駆事例。",
         "related_ai_phenomenon":"生成行為の文学化"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"生成モデル",
         "description":"NaNoGenMoは生成AI研究と文学実践の橋渡し。"}])

add(**C, name_ja="Botnik Studios",
    name_en="Botnik Studios",
    name_original="Botnik Studios",
    definition="Jamie Brew、Bob Mankoff等が2016年に設立した予測キーボードベースの協働創作スタジオ。『Harry Potter and the Portrait of What Looked Like a Large Pile of Ash』等のパロディで人間とアルゴリズムの協働ナラティブを実証した。",
    background="2016年予測テキスト技術の成熟、The New Yorker風刺漫画系作家Brewの実験。",
    development="2017-2020年でバズコンテンツの源泉、人間-AI協働文学の入門事例として教育・批評の中心となった。",
    historical_context="2016-2020年予測キーボード文学期。",
    primary_source_url="https://botnik.org/",
    primary_source_type="Botnik Studios: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"Botnikは人間の手動選択とアルゴリズム提案の協働を制度化したパロディ詩学。",
         "related_ai_phenomenon":"予測協働ライティング"}])

add(**C, name_ja="Janelle Shane",
    name_en="Janelle Shane",
    name_original="Janelle Shane",
    definition="光学物理学者でAI Weirdnessブログ運営者。2018年以降、ニューラルネットの学習失敗を文学的素材として展示、『You Look Like a Thing and I Love You』(2019)で機械学習の限界を大衆向けに語った。",
    background="2017年Shaneブログ開始、char-RNN・GPT-2時代の生成文学実験の代表。",
    development="2018-2024年で世界的に翻訳・引用される機械学習文学批評の中心人物となった。",
    historical_context="2017-2024年機械学習文学批評の大衆化期。",
    primary_source_url="https://www.aiweirdness.com/",
    primary_source_type="AI Weirdness blog (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"Shaneは機械学習の「失敗」を文学的価値として再評価する批評的視点を確立した。",
         "related_ai_phenomenon":"機械学習の失敗の詩学"}])

add(**C, name_ja="AI Dungeon",
    name_en="AI Dungeon",
    name_original="AI Dungeon (Latitude)",
    definition="Nick Walton開発、2019年公開のGPT-2/3ベースの対話型インタラクティブフィクション。プレイヤーの自由入力にAIが応答する形式で、商用LLM応用文学の先駆事例。NSFW論議・OpenAI規制論議の起点となった。",
    background="2019年GPT-2公開、対話型生成テクスト技術の成熟。",
    development="2020-2021年世界的人気、2021年OpenAIコンテンツ規制論争でNovelAI等の派生を生んだ。",
    historical_context="2019-2024年LLM応用IFの大衆化期。",
    primary_source_url="https://aidungeon.io/",
    primary_source_type="AI Dungeon: official site (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"AI DungeonはAIとプレイヤーの即興協働物語を商用化した最初の大規模事例。",
         "related_ai_phenomenon":"AIとの即興物語"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"GPT-3応用",
         "description":"AI DungeonはLLM応用と物語実践の重要交差点。"}])

add(**C, name_ja="NovelAI",
    name_en="NovelAI",
    name_original="NovelAI (Anlatan)",
    definition="2021年Anlatan社がAI Dungeonの規制論議への対抗として公開したサブスク型LLMフィクション執筆プラットフォーム。GPT-J・Llama系ファインチューンで、独自モデル・プライバシー保護・物語制御特化を売りとした。",
    background="2021年AI Dungeon規制論争、ユーザーのプライバシー保護需要、独自LLMファインチューン技術の成熟。",
    development="2022-2025年でアニメ・ライトノベル系英語圏ファンコミュニティの中心ツールとなり、Stable Diffusion統合で画像生成も提供。",
    historical_context="2021-2025年サブスク型LLM文学プラットフォーム期。",
    primary_source_url="https://novelai.net/",
    primary_source_type="NovelAI: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"NovelAIは規制を回避する独自LLMで「制御可能な作者支援」モデルを確立した。",
         "related_ai_phenomenon":"独自モデルによる作者支援"}])

add(**C, name_ja="Sudowrite",
    name_en="Sudowrite",
    name_original="Sudowrite",
    definition="2020年James Yu、Amit Gupta設立のフィクション作家向けLLMアシスタント。「Describe」「Brainstorm」「Rewrite」等の文学特化機能を提供し、商業作家の実用ツールとして定着した。",
    background="2020年GPT-3 API公開、商業作家向けAIツール需要の顕在化。",
    development="2022-2025年でMFA文芸創作課程・商業作家コミュニティで論議の中心、AI支援創作の事実上の業界標準となった。",
    historical_context="2020-2025年商業作家のAI支援ツール定着期。",
    primary_source_url="https://www.sudowrite.com/",
    primary_source_type="Sudowrite: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"Sudowriteは商業作家のワークフローにAIを組み込む過程を可視化した代表的サービス。",
         "related_ai_phenomenon":"作家ワークフローのAI統合"}])

add(**C, name_ja="Character.AI",
    name_en="Character.AI",
    name_original="Character.AI",
    definition="2021年元Google Brain研究者Noam Shazeer、Daniel De Freitas設立のキャラクター対話型LLMサービス。フィクションキャラクターとの対話シミュレーションが世界で月間2,000万人ユーザー規模となり、ロールプレイ文学の制度化を促した。",
    background="2021年LaMDA系対話LLM、ファンフィクション・ロールプレイコミュニティの需要。",
    development="2023-2024年世界のZ世代に普及、若年層自殺関連訴訟（2024年Setzer事件）でAI倫理の中核論議となった。",
    historical_context="2021-2025年対話型キャラクターLLMの大衆化期。",
    primary_source_url="https://character.ai/",
    primary_source_type="Character.AI: official site (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"Character.AIはロールプレイ文学を産業規模で制度化、若年層の物語消費形態を変容させた。",
         "related_ai_phenomenon":"対話型キャラクター文学"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"擬人化と倫理",
         "description":"Character.AIは擬人化倫理の中心問題。"}])

add(**C, name_ja="Replika",
    name_en="Replika",
    name_original="Replika (Luka Inc.)",
    definition="2017年Eugenia Kuyda設立のAIコンパニオンアプリ。亡くなった友人とのチャット履歴から開発されたとされ、「AI愛人」「AI友人」として世界数百万ユーザー規模、AI親密性関係の文学・倫理論議の中心となった。",
    background="2017年Kuyda友人Mazurenko事故死、対話履歴からのAI蘇生プロジェクト。",
    development="2020-2024年COVID孤独期に急成長、2023年Erotic Roleplay規制変更でユーザー反発、AI親密性文学の中心事例となった。",
    historical_context="2017-2025年AIコンパニオン文学期。",
    primary_source_url="https://replika.com/",
    primary_source_type="Replika: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"ReplikaはAI親密性関係を産業規模で制度化、ポストヒューマン親密性論の現実事例となった。",
         "related_ai_phenomenon":"AIとの親密性関係"}])


# ============================================================
# C: プロンプト文学（3件）
# ============================================================
add(**C, name_ja="エクフラシスとしてのプロンプト",
    name_en="prompting as ekphrasis",
    name_original="prompting as ekphrasis",
    definition="プロンプト記述行為を古代ギリシア・ローマのエクフラシス（絵画・彫刻の言語的描写）の現代的継承として理論化する流れ。Stephanie Bahr、Joshua Lukin等が2023-2024年に文学伝統との接続を提案。",
    background="2022-2023年プロンプト工学の文学的制度化、古典修辞学伝統との接続論議の浮上。",
    development="2024-2025年ASLE、MLA等の学会で「エクフラシスとしてのプロンプト」セッションが組まれ、古典文学との接続論議が制度化中。",
    historical_context="2022-2025年プロンプト文学理論の古典接続期。",
    primary_source_url=WIKI_EN+"Ekphrasis",
    primary_source_type="Wikipedia: Ekphrasis (background)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"プロンプトを古代エクフラシス伝統に接続することで、生成AIが古典修辞学の継承形態として理論化される。",
         "related_ai_phenomenon":"古典修辞学のAI時代継承"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"エクフラシス",
         "description":"プロンプト=エクフラシスは詩学伝統とAI実践の接続点。"}])

add(**C, name_ja="侵犯としての脱獄プロンプト",
    name_en="jailbreak as transgression",
    name_original="jailbreak as transgression",
    definition="LLMの安全規制を突破するjailbreakプロンプトをジョルジュ・バタイユ的「侵犯（transgression）」の現代的形態として理論化する流れ。McKenzie Wark等が2024年以降にAI規範の境界破壊を文学的侵犯として位置づけた。",
    background="2023-2024年jailbreakコミュニティの拡大、ポスト構造主義的侵犯論との接続。",
    development="2024-2025年でAI研究と批判理論の交差点として、Wark、Jussi Parikka等の批判理論家が侵犯論を展開中。",
    historical_context="2023-2025年AI規範と侵犯論の理論化期。",
    primary_source_url=ARXIV+"2305.13860",
    primary_source_type="arXiv 2023: jailbreak studies (background)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"jailbreakを侵犯として理論化することは、AI規範の境界線そのものを文学的問題として再定義する。",
         "related_ai_phenomenon":"AI規範の文学的侵犯"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"侵犯（バタイユ）",
         "description":"jailbreak侵犯論はバタイユ哲学とAI実践の接続点。"}])

add(**C, name_ja="プロンプト工学マニュアル詩学",
    name_en="prompt engineering manuals as poetics",
    name_original="prompt engineering manuals as poetics",
    definition="OpenAI、Anthropic、DeepLearning.AI等の公式プロンプト工学マニュアルを「現代の詩学（ars poetica）」として読解する批評実践。Andrej Karpathy、Lilian Weng等の技術文書が現代修辞学の正典となる過程を分析する。",
    background="2022-2024年プロンプト工学公式マニュアル群の整備、技術文書の文学批評対象化。",
    development="2024-2025年でDH研究者がOpenAI/Anthropicマニュアルを「AI時代のars poetica」として教材化する動きが進行中。",
    historical_context="2022-2025年技術文書の詩学化期。",
    primary_source_url="https://docs.anthropic.com/claude/docs/prompt-engineering",
    primary_source_type="Anthropic: Prompt Engineering Guide (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"技術マニュアルが「詩学」として読解されることは、プログラミング文書と文学理論の境界が溶解する現象を示す。",
         "related_ai_phenomenon":"技術文書の詩学化"}])


# ============================================================
# D: インタラクティブ（5件）
# ============================================================
add(**C, name_ja="Twineエコシステム理論",
    name_en="Twine ecosystem theory",
    name_original="Twine ecosystem theory",
    definition="Twineを中心とする選択型物語の制作・配布・批評・教育エコシステム理論。Stuart Moulthrop、Anastasia Salter、Anna Anthropy等が2014-2024年にコミュニティ・ツール・ジャンルの相互形成過程を理論化。",
    background="2009年Twine初版、2010年代インディーIF制作の大衆化、エコシステム理論の必要性。",
    development="2015-2024年でELO、IFDB、ITCHを巻き込む包括的エコシステム理論として制度化、教育・批評の中核となった。",
    historical_context="2010-2025年インディーIFエコシステム理論化期。",
    primary_source_url="https://twinery.org/",
    primary_source_type="Twinery: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"Twineエコシステムはインディー作家コミュニティとオープンソース文学制度の典型事例。",
         "related_ai_phenomenon":"オープンソース文学エコシステム"}])

add(**C, name_ja="Choice of Games",
    name_en="Choice of Games",
    name_original="Choice of Games (Dan Fabulich, Adam Strong-Morse)",
    definition="2009年Dan Fabulich、Adam Strong-Morse設立のChoiceScript言語ベース選択型小説プラットフォーム。プロ作家が稼げるモデルを確立、IF商業化の先駆事例として制度化。Hosted Games、Heart's Choice系列等で多様なジャンルを供給。",
    background="2009年ChoiceScript開発、商業選択型小説市場の不在への対応。",
    development="2010-2024年で商業選択型小説市場の中核となり、年間50作以上の出版、世界IF市場の主要プラットフォームとなった。",
    historical_context="2009-2025年商業IF制度化期。",
    primary_source_url="https://www.choiceofgames.com/",
    primary_source_type="Choice of Games: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"Choice of GamesはIFの商業作家性を制度化した先駆事例。",
         "related_ai_phenomenon":"IF商業化と作家性"}])

add(**C, name_ja="Inkleスタジオ",
    name_en="Inkle studio",
    name_original="Inkle (Joseph Humfrey, Jon Ingold)",
    definition="2011年Jon Ingold、Joseph Humfreyが設立したインタラクティブ・フィクション制作スタジオ。『80 Days』(2014)、『Heaven's Vault』(2019)、『Pendragon』(2020)等で文学的IFの新基準を確立、Inkスクリプト言語をオープンソース化。",
    background="2011年Steve Jackson『Sorcery!』移植プロジェクト、文学的IFへの商業需要。",
    development="2014-2024年でIGF、BAFTA等の主要文学的IF賞受賞、Ink言語が世界IF制作の主要ツールとなった。",
    historical_context="2011-2025年文学的商業IF制度化期。",
    primary_source_url="https://www.inklestudios.com/",
    primary_source_type="Inkle: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"Inkleは文学的IFと商業ゲーム業界の融合を制度化した代表事例。",
         "related_ai_phenomenon":"文学的IFと商業ゲームの融合"}])

add(**C, name_ja="Bitsy",
    name_en="Bitsy",
    name_original="Bitsy (Adam Le Doux)",
    definition="2017年Adam Le Doux開発の極小ピクセル探索ゲーム制作ツール。8×8ピクセル・3色・限定文字数の制約が独自の詩的ナラティブ表現を生み、世界数千の小品制作と「Bitsyジャム」コミュニティを形成した。",
    background="2017年Le Doux制約ゲーム制作実験、Twine的小品文学への需要。",
    development="2018-2024年でBitsyジャム・教育用ツールとして世界普及、極小ナラティブ制作の中核となった。",
    historical_context="2017-2025年極小制約ナラティブ期。",
    primary_source_url="https://make.bitsy.org/",
    primary_source_type="Bitsy: official tool (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"Bitsyは極小制約による詩的ナラティブ生成を可能にする現代の俳句的形式。",
         "related_ai_phenomenon":"極小制約ナラティブの詩学"}])

add(**C, name_ja="Hidden Door",
    name_en="Hidden Door",
    name_original="Hidden Door (Hilary Mason)",
    definition="2020年Hilary Mason設立のLLMベース協働物語ゲームプラットフォーム。既存IPを安全に「物語化」する独自モデルで、世界初の「物語AIゲーム」として2024年に商業展開、AI時代TRPG・物語ゲームの先駆事例。",
    background="2020-2023年LLM技術成熟、物語AIゲーム・TRPG商業化への需要。",
    development="2024-2025年公開ベータ展開、文学IPライセンス契約モデル、TRPGコミュニティとの連携で物語AIゲーム市場を切り拓いた。",
    historical_context="2020-2025年物語AIゲーム期。",
    primary_source_url="https://www.hiddendoor.co/",
    primary_source_type="Hidden Door: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"Hidden DoorはAI時代の協働物語ゲームを既存IPと結合する商業モデルを確立した。",
         "related_ai_phenomenon":"AI協働物語ゲーム"}])


# ============================================================
# E: ソーシャルメディア文学（5件）
# ============================================================
add(**C, name_ja="Twitterフィクション",
    name_en="Twitter fiction",
    name_original="Twitter fiction",
    definition="2010年代以降のTwitter（現X）短文ナラティブ実践。Teju Cole『Small Fates』(2011)、Jennifer Egan『Black Box』(2012, New Yorker発表)、Andrés Neuman等の作家が140/280字制約下で物語形式を実験した。",
    background="2010年代Twitter普及、極短文ナラティブへの作家的関心。",
    development="2014-2020年で多数の文学誌Twitter Fiction Festival企画、2022年X買収後規範変動で衰退傾向。",
    historical_context="2010-2024年マイクロブログ文学期。",
    primary_source_url="https://www.newyorker.com/magazine/2012/06/04/black-box",
    primary_source_type="The New Yorker 2012: Egan Black Box (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"Twitterフィクションは短文制約が物語形式に与える構造的影響を実証した。",
         "related_ai_phenomenon":"短文制約と物語形式"}])

add(**C, name_ja="ハッシュタグフィクション",
    name_en="hashtag fiction",
    name_original="hashtag fiction",
    definition="ハッシュタグを構造化装置として用いる集合的ナラティブ実践。#TwitterFiction、#VeryShortStory、#1LineWed等のハッシュタグが2010年代に集合的物語生成プロトコルとなり、参加型文学の典型形式を形成した。",
    background="2010年代Twitterハッシュタグ文化、参加型物語実践への関心。",
    development="2014-2020年で各国文学誌が「ハッシュタグ小説募集」企画、2024年現在は#WritingCommunityに収斂中。",
    historical_context="2010-2024年集合的ハッシュタグ文学期。",
    primary_source_url=WIKI_EN+"Twitterature",
    primary_source_type="Wikipedia: Twitterature (background)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ハッシュタグフィクションは集合的・参加型作者性の典型形式。",
         "related_ai_phenomenon":"集合的参加型作者性"}])

add(**C, name_ja="インスタ詩批評",
    name_en="Insta-poetry critique",
    name_original="Insta-poetry critique",
    definition="Rupi Kaur『milk and honey』(2014)以降のInstagram詩を巡る批評論議。Becca Rothfeld、Rebecca Watts等の批評家がインスタ詩を「商業化された感情詩」として批判する一方、フェミニスト批評家が大衆詩の民主化として擁護する両極論議。",
    background="2014年Kaur『milk and honey』ベストセラー化、インスタ詩商業化、批評論議の浮上。",
    development="2018-2024年で「インスタ詩は詩か」論議が世界文学誌で展開、大衆詩の民主化と商業化を巡る現代批評論議の中心となった。",
    historical_context="2014-2025年インスタ詩批評論議期。",
    primary_source_url=WIKI_EN+"Rupi_Kaur",
    primary_source_type="Wikipedia: Rupi Kaur (background)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"インスタ詩批評論議は大衆詩の正統性とアルゴリズム的拡散の関係を問う現代批評の中核問題。",
         "related_ai_phenomenon":"アルゴリズム拡散と詩の正統性"}])

add(**C, name_ja="BookTok",
    name_en="BookTok",
    name_original="BookTok",
    definition="2020年代TikTok上の書籍コミュニティ。2020-2024年で全米書籍売上の数十%を駆動、Colleen Hoover『It Ends With Us』、Sarah J. Maas等の作家を世界的ベストセラーに押し上げ、出版業界のマーケティング構造を変容させた。",
    background="2020年COVID期にTikTok急成長、書籍コミュニティの自然発生。",
    development="2022-2024年Penguin Random House、Hachette等の大手出版社が独自BookTokマーケティング部門を設立、業界構造変動が進行中。",
    historical_context="2020-2025年BookTok時代。",
    primary_source_url=WIKI_EN+"BookTok",
    primary_source_type="Wikipedia: BookTok (academic-grade)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"BookTokはアルゴリズム駆動型書籍受容を産業規模で制度化した代表事例。",
         "related_ai_phenomenon":"アルゴリズム拡散と書籍受容"}])

add(**C, name_ja="BookTube",
    name_en="BookTube",
    name_original="BookTube",
    definition="2010年代以降のYouTube書評コミュニティ。Ariel Bissett、Jen Campbell、Lauren等のBookTuberが2014-2024年で書評の大衆メディア化を駆動、伝統的書評ジャーナリズムへの代替形態として制度化された。",
    background="2010年代YouTube普及、書評の大衆メディア化への関心。",
    development="2014-2024年でBookTube Awardsが定着、出版社マーケティング標準チャネル、TikTokのBookTokと並ぶデジタル書評コミュニティの双璧となった。",
    historical_context="2010-2025年デジタル書評コミュニティ期。",
    primary_source_url=WIKI_EN+"BookTube",
    primary_source_type="Wikipedia: BookTube (background)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"BookTubeはデジタル書評コミュニティの先駆形式。",
         "related_ai_phenomenon":"動画SNS書評の制度化"}])


# ============================================================
# F: ウェブ小説（6件）
# ============================================================
add(**C, name_ja="Wattpad",
    name_en="Wattpad",
    name_original="Wattpad",
    definition="2006年Allen Lau、Ivan Yuen設立のWeb小説プラットフォーム。世界9,000万人ユーザー規模、Anna Todd『After』One Direction同人発ベストセラー化等で同人発商業化モデルを確立、2021年Naver買収。",
    background="2006年モバイル読書市場の不在、同人創作プラットフォーム需要。",
    development="2010-2024年で世界最大規模のWeb小説プラットフォームに成長、出版業界のスカウト先として制度化、2021年韓国Naver買収で韓流文化と統合された。",
    historical_context="2006-2025年同人発商業化期。",
    primary_source_url="https://www.wattpad.com/",
    primary_source_type="Wattpad: official site (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"Wattpadは同人発商業化モデルを世界規模で制度化、伝統的出版社のゲートキーパー機能を脱構築した。",
         "related_ai_phenomenon":"同人発商業化モデル"}])

add(**C, name_ja="Royal Road",
    name_en="Royal Road",
    name_original="Royal Road",
    definition="2012年Kevin Berg設立の英語圏ウェブ小説プラットフォーム。LitRPG、isekai、progression fantasy系列の発信地となり、Andrew Rowe、Sleyca等の作家を世界市場に輩出、英語圏Web小説の中核となった。",
    background="2012年英語圏Web小説プラットフォーム需要、LitRPGジャンル成長期。",
    development="2018-2024年でAmazon KU連携、同人小説の商業化経路として制度化、英語圏なろう系の中核プラットフォームとなった。",
    historical_context="2012-2025年英語圏Web小説期。",
    primary_source_url="https://www.royalroad.com/",
    primary_source_type="Royal Road: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"Royal Roadは英語圏Web小説の同人商業化経路を確立した。",
         "related_ai_phenomenon":"英語圏なろう系"}])

add(**C, name_ja="起点中文網",
    name_en="Qidian (起点中文网)",
    name_original="起点中文網 / Qidian",
    definition="2002年設立の中国最大Web小説プラットフォーム。2014年閲文集団傘下、世界最大規模の中文Web小説生態系を形成、修真・玄幻・系統文学の発信地として東アジアWeb小説文化の中心となった。",
    background="2002年中国Web小説市場形成期、商業化モデルの不在への対応。",
    development="2014-2024年で世界最大規模の中文Web小説生態系、Webnovel英語版を通じて世界化、東アジアWeb小説文化の中核となった。",
    historical_context="2002-2025年中国Web小説産業期。",
    primary_source_url="https://www.qidian.com/",
    primary_source_type="Qidian: official site (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"起点中文網は東アジアWeb小説の正典形成過程を産業規模で制度化した。",
         "related_ai_phenomenon":"東アジアWeb小説産業化"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"中国Web文学",
         "description":"起点中文網は中国Web文学産業の中核。"}])

add(**C, name_ja="小説家になろう",
    name_en="Shōsetsuka ni Narō",
    name_original="小説家になろう",
    definition="2004年Hina Project設立の日本最大Web小説プラットフォーム。「異世界転生」「悪役令嬢」等のなろう系ジャンルを生み、ライトノベル業界・アニメ業界・世界Web小説文化に決定的影響を与えた。",
    background="2004年日本Web小説市場形成期、同人・素人小説プラットフォーム需要。",
    development="2010-2024年で日本Web小説の中核となり、なろう系・異世界系・悪役令嬢系を世界に発信、Pixiv・カクヨム等と並ぶ日本Web文学エコシステム。",
    historical_context="2004-2025年日本Web小説産業期。",
    primary_source_url="https://syosetu.com/",
    primary_source_type="小説家になろう: official site (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"なろうは日本Web小説の正典形成と世界アニメ・ラノベ産業への影響を産業規模で制度化した。",
         "related_ai_phenomenon":"なろう系の世界化"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"日本ライトノベル",
         "description":"なろうは日本ラノベ・アニメ産業の中核。"}])

add(**C, name_ja="異世界転生理論",
    name_en="isekai theory",
    name_original="isekai theory",
    definition="日本Web小説の主要ジャンル「異世界転生」を巡る学術論議。佐々木隆、松本健一郎等の批評家がポストモダン的逃避・労働者階級の救済幻想・近代主体の解体として理論化、ジャンル理論の国際的中核となった。",
    background="2010年代「Re:ゼロ」「転スラ」等のなろう系ヒット、ジャンル理論化の必要性。",
    development="2018-2024年で日本国内・海外で異世界転生研究が学術化、ジェンダー・労働・階級の批判的読解が主流となった。",
    historical_context="2010-2025年異世界ジャンル理論化期。",
    primary_source_url=WIKI_JA+"異世界",
    primary_source_type="Wikipedia: 異世界 (academic-grade)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"異世界転生理論はWeb小説ジャンルの社会学的解読を制度化した代表事例。",
         "related_ai_phenomenon":"Web小説ジャンルの社会学的解読"}])

add(**C, name_ja="システム小説理論",
    name_en="system novel theory (LitRPG)",
    name_original="LitRPG / system novel theory",
    definition="ステータス画面・スキルシステム・経験値等のRPG的「システム」を物語装置として用いるWeb小説ジャンル理論。Sergei Korol等のロシアLitRPG派生、英語圏progression fantasy、中国系統流の比較研究が進行中。",
    background="2010年代RPGゲーム文化のWeb小説への流入、ジャンル理論化の必要性。",
    development="2018-2024年でAndrew Rowe、He Who Fights with Monsters、Cradle系列等が世界市場で成功、システム小説理論が制度化中。",
    historical_context="2010-2025年システム小説ジャンル理論化期。",
    primary_source_url=WIKI_EN+"LitRPG",
    primary_source_type="Wikipedia: LitRPG (academic-grade)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"システム小説はゲーム的構造と物語形式の融合を制度化したWeb小説の代表ジャンル。",
         "related_ai_phenomenon":"ゲーム構造とナラティブの融合"}])


# ============================================================
# G: 学術インフラ（4件）
# ============================================================
add(**C, name_ja="Digital Scholarship in the Humanities",
    name_en="Digital Scholarship in the Humanities (DSH)",
    name_original="Digital Scholarship in the Humanities (DSH)",
    definition="1986年創刊『Literary and Linguistic Computing』の後継として2015年改名されたDH分野の中核査読誌。Oxford University Press、ALLC連携で世界DH研究の主要発表場、世界の計算文学研究の中核となった。",
    background="1986年LLC創刊、デジタル人文学分野の発表場形成、2015年改名でDH領域拡張。",
    development="2015-2025年でDH分野の主要査読誌として制度化、世界の計算文学研究・DH方法論の中核発表場となった。",
    historical_context="1986-2025年DH学術誌制度化期。",
    primary_source_url="https://academic.oup.com/dsh",
    primary_source_type="DSH: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"受容","status":"partial",
         "rationale":"DSHはDH分野の制度的中核として、計算文学研究の正統性確立に寄与した。",
         "related_ai_phenomenon":"DH学術正統性"}])

add(**C, name_ja="ADHO",
    name_en="ADHO (Alliance of Digital Humanities Organizations)",
    name_original="Alliance of Digital Humanities Organizations",
    definition="2005年設立のデジタル人文学国際連合体。ALLC、ACH、CSDH/SCHN、JADH、TaiwanDH等の地域学会を統括し、年次大会DH（Digital Humanities Conference）を主催、世界DH研究の制度的中核となった。",
    background="2005年世界DH学会連携の必要性、年次国際会議制度化への需要。",
    development="2010-2024年でDH年次大会が世界の計算文学・DH研究の中心発表場として制度化、グローバルDH研究の中核機関となった。",
    historical_context="2005-2025年DHグローバル組織化期。",
    primary_source_url="https://adho.org/",
    primary_source_type="ADHO: official site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"受容","status":"partial",
         "rationale":"ADHOはDH分野の制度的グローバル化を駆動した中核機関。",
         "related_ai_phenomenon":"DH分野のグローバル制度化"}])

add(**C, name_ja="Internet Archiveコーパス",
    name_en="Internet Archive corpus",
    name_original="Internet Archive corpus / archive.org",
    definition="1996年Brewster Kahle設立のInternet Archive。Open Library 2000万冊、Wayback Machine 8,000億ページがDH研究の中核データ源、2023年Hachette訴訟・LLM学習データ論議の中心となった。",
    background="1996年Web永続化への危機感、デジタル文化遺産保存への需要。",
    development="2010-2024年でDH研究・LLM学習データの中核ソースとなり、2023年Hachette対Internet Archive判決でCDL論議が世界化した。",
    historical_context="1996-2025年Web文化遺産保存期。",
    primary_source_url="https://archive.org/",
    primary_source_type="Internet Archive: official site (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"Internet ArchiveはWeb文化遺産の正典化基盤として、デジタル時代の正典形成に決定的影響を与える。",
         "related_ai_phenomenon":"Web文化遺産とAI学習データ"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI学習データソース",
         "description":"Internet ArchiveはDH研究とAI学習データの交差点。"}])

add(**C, name_ja="Google Books Project",
    name_en="Google Books Project",
    name_original="Google Books Library Project",
    definition="2004年Google Print Library Projectとして開始された世界書籍デジタル化計画。3,000万冊以上を電子化、2015年Authors Guild対Google判決でフェアユース確定、Google Ngram Viewer・LLM学習データの中核基盤となった。",
    background="2004年Larry Page・Sergey Brinの大規模書籍デジタル化構想、世界の主要図書館との連携。",
    development="2004-2015年Authors Guild訴訟、2015年フェアユース判決、2010-2024年Google Ngram Viewerが計算文学研究の中核データ源となった。",
    historical_context="2004-2025年大規模書籍デジタル化期。",
    primary_source_url="https://books.google.com/",
    primary_source_type="Google Books: official site (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"Google Booksは大規模書籍デジタル化と正典の計算的解析を可能にした基盤事業。",
         "related_ai_phenomenon":"大規模書籍コーパスとAI"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"大規模コーパス",
         "description":"Google BooksはDH研究とAI学習データの中核基盤。"}])


# ============================================================
# H: 倫理（4件）
# ============================================================
add(**C, name_ja="確率的オウム論文",
    name_en="Stochastic Parrots paper (Bender et al. 2021)",
    name_original="On the Dangers of Stochastic Parrots",
    definition="2021年Emily Bender、Timnit Gebru、Angelina McMillan-Major、Margaret Mitchellの『FAccT』論文。LLMの環境コスト・偏向・幻覚・透明性問題を体系的に批判、Gebru解雇事件の引き金となり、AI倫理論議の中核となった。",
    background="2020-2021年LLM大規模化（GPT-3）、AI倫理論議の制度化、Google Ethical AI研究所内部論議。",
    development="2021年12月Gebru解雇事件、2022-2025年LLM倫理論議の最重要参考文献として世界的に引用される標準論文となった。",
    historical_context="2020-2025年LLM倫理論議期。",
    primary_source_url="https://dl.acm.org/doi/10.1145/3442188.3445922",
    primary_source_type="ACM FAccT 2021: Stochastic Parrots (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"確率的オウム論文はLLM作者性を「統計的模倣」として根本的に脱神話化した決定的批評。",
         "related_ai_phenomenon":"LLM作者性の脱神話化"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"LLMの「理解」を統計的反復として暴露することで、AI生成テクストの真正性概念を根本的に問い直した。",
         "related_ai_phenomenon":"AI理解の脱神話化"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI倫理",
         "description":"確率的オウム論文はAI倫理論議の中核。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"理解と意味",
         "description":"確率的オウム論文は意味理論とAIの交差点。"}])

add(**C, name_ja="Bender章魚論証",
    name_en="Bender Octopus argument",
    name_original="Bender & Koller Octopus argument (2020)",
    definition="2020年Emily Bender、Alexander Kollerの『ACL』論文『Climbing towards NLU』で展開された思考実験。海底ケーブルから言語データだけ受信する章魚は意味を理解できないという論証で、LLMの意味理解不可能性を論証した。",
    background="2020年BERT・GPT-2成熟、LLMの「理解」概念への哲学的批判の必要性。",
    development="2020-2024年でAI意味論論議の標準的参照論証となり、Bender『Stochastic Parrots』論文と並ぶLLM懐疑論の中核論証となった。",
    historical_context="2020-2025年LLM意味理解論議期。",
    primary_source_url="https://aclanthology.org/2020.acl-main.463/",
    primary_source_type="ACL 2020: Climbing towards NLU (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"章魚論証はLLMの意味理解不可能性を論理的に論証する標準論証として制度化された。",
         "related_ai_phenomenon":"LLM意味理解の哲学的批判"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"意味の哲学",
         "description":"章魚論証は意味の哲学とAI研究の交差点。"}])

add(**C, name_ja="Crawford『Atlas of AI』",
    name_en="Crawford Atlas of AI",
    name_original="Kate Crawford: Atlas of AI (2021)",
    definition="2021年Kate Crawfordの著書。AIをデータ・ラベル労働・鉱物資源・電力・地政学の物質的システムとして再概念化、「AIは人工でも知的でもない」という批判的立場でAI唯物論的研究の中核となった。",
    background="2010年代Crawford AI Now Institute設立、AIの物質性・労働・環境影響の批判的研究蓄積。",
    development="2021-2024年でAI批判理論・DH批判の必読書、AIの物質的・地政学的批判の世界的標準となった。",
    historical_context="2021-2025年AI唯物論的批判期。",
    primary_source_url="https://yalebooks.yale.edu/book/9780300209570/atlas-of-ai/",
    primary_source_type="Yale University Press: Atlas of AI (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"Crawfordの著書はAIを物質的・労働的・地政学的システムとして批判的に再概念化する。",
         "related_ai_phenomenon":"AIの物質性批判"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"テクノロジー批判",
         "description":"Crawford Atlas of AIは技術哲学とAI研究の交差点。"}])

add(**C, name_ja="Gender Shades監査",
    name_en="Gender Shades audit",
    name_original="Gender Shades (Buolamwini & Gebru 2018)",
    definition="2018年Joy Buolamwini、Timnit Gebruの『FAT*』論文。商業顔認識システムの肌色・性別交差性偏向を体系的に監査、IBM・Microsoft・Faceの偏向を実証、AI監査研究の標準論文となった。",
    background="2017年Buolamwini MIT Media Lab研究、商業AIシステムの偏向への批判的研究の必要性。",
    development="2018-2024年AI監査研究の標準参照論文、IBM・Microsoftの顔認識撤退、AI Bill of Rights制定への直接影響となった。",
    historical_context="2018-2025年AI監査研究期。",
    primary_source_url="https://proceedings.mlr.press/v81/buolamwini18a.html",
    primary_source_type="PMLR FAT* 2018: Gender Shades (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"Gender ShadesはAI監査研究を制度化、AIシステムの社会的偏向検証の標準を確立した。",
         "related_ai_phenomenon":"AI監査研究の制度化"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI偏向監査",
         "description":"Gender ShadesはAI開発倫理の中核論文。"}])


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
        print(f"[c39-retry40] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c39-retry40] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
