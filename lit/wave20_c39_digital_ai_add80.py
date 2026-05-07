"""LIT-DB Phase 2 Wave 20 — C39 Digital Humanities & AI Era ADD 80 (NEW).

Subfield: lit_digital_ai (id=24), region='理論'.
Existing 211 concepts. This wave adds 80 NEW non-overlapping concepts.
Targets: ~50% primary, fourth_axes>=50, cross_domain>=35.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("デジタル人文学・AI時代", "Digital Humanities & AI Era",
     1990, 2030,
     "1990年代のTEIとデジタルテクスト批評の制度化から、2010年代の遠読・トピックモデリング、2020年代のLLM以降にいたる、計算的人文学とAI生成文学の理論期。"),
]

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
# A: AI著作権訴訟詳細（13件）
# ============================================================
add(**C, name_ja="Authors Guild対OpenAI訴訟詳細",
    name_en="Authors Guild v. OpenAI 2023 detail",
    name_original="Authors Guild v. OpenAI (S.D.N.Y. 2023)",
    definition="2023年9月Authors Guildほか17作家がOpenAI/Microsoftを提訴した集団訴訟。GRRマーティン・グリシャム等が著作権侵害を主張、Books3への依存を主要争点としたAI訴訟の旗艦事例。",
    background="2023年Books3データセット暴露、ChatGPTの著作権作品学習が判明。",
    development="2024-2025年でNYT v OpenAI等と統合審理、判決は2025年以降に持ち越され、米AI著作権法形成の中心事案となった。",
    historical_context="2023-2025年AI著作権訴訟期。",
    primary_source_url="https://authorsguild.org/news/ag-and-authors-file-class-action-suit-against-openai/",
    primary_source_type="Authors Guild filing (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Authors Guild訴訟はAI著作権訴訟の旗艦事例。"),
                 fa_canon("Books3依存により正典の構成過程がAI訓練に介入された。")],
    cross_domain=[cd("AI-Development","AI訴訟","Authors Guild訴訟はAI法形成の中核。")])

add(**C, name_ja="NYT対OpenAI訴訟詳細",
    name_en="NYT v. OpenAI/Microsoft 2023 detail",
    name_original="The New York Times Co. v. Microsoft Corp. (S.D.N.Y. 2023)",
    definition="2023年12月NYTがOpenAI/Microsoftを提訴。GPT-4が記事をほぼ逐語再生する100例を証拠提示、報道機関のAI訓練対抗訴訟の代表事例として2024-2025年米AI法形成を主導。",
    background="2023年NYT交渉決裂、ChatGPTの逐語再生問題化。",
    development="2024-2025年でDaily News等が同様訴訟を提起、報道×AI法形成の中心事案となった。",
    historical_context="2023-2025年報道機関AI訴訟期。",
    primary_source_url="https://nytco-assets.nytimes.com/2023/12/NYT_Complaint_Dec2023.pdf",
    primary_source_type="NYT complaint filing (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("NYT訴訟は逐語再生による記者作者性侵害を可視化した。")],
    cross_domain=[cd("AI-Development","記憶化","NYT訴訟は記憶化問題の代表事例。")])

add(**C, name_ja="Sarah Silverman対Meta訴訟",
    name_en="Sarah Silverman v. Meta+OpenAI 2023",
    name_original="Silverman v. OpenAI / Silverman v. Meta (N.D. Cal. 2023)",
    definition="2023年7月コメディアン Sarah Silverman、Richard Kadrey、Christopher Goldenがメタ・OpenAIを提訴。Books3経由の著作物学習を争点とし、AI訓練データの違法性論議を加速させた。",
    background="2023年Books3問題化、コメディ・小説作家の集団訴訟組織化。",
    development="2023-2024年で部分却下後再構築、AI訓練データ法の判例形成を駆動した。",
    historical_context="2023-2025年Books3関連訴訟期。",
    primary_source_url="https://llmlitigation.com/pdf/03416/silverman-openai-complaint.pdf",
    primary_source_type="Silverman complaint (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Silverman訴訟はAI訓練データの違法性論議を加速。")])

add(**C, name_ja="Concord Music対Anthropic訴訟",
    name_en="Concord Music v. Anthropic 2023",
    name_original="Concord Music Group v. Anthropic PBC (M.D. Tenn. 2023)",
    definition="2023年10月Concord・Universal・ABKCO音楽出版社がAnthropicを提訴。Claude が著作権楽曲歌詞を出力した事例を争点とし、音楽×AI訴訟の旗艦事例となった。",
    background="2023年Claude 2公開後、歌詞出力問題が表面化。",
    development="2024年部分差止判決、音楽出版社×AI法形成の代表事例となり業界対応を駆動した。",
    historical_context="2023-2025年音楽×AI訴訟期。",
    primary_source_url="https://www.courtlistener.com/docket/67830231/concord-music-group-inc-v-anthropic-pbc/",
    primary_source_type="Court filing (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Concord訴訟は歌詞×AI著作権の代表事例。")])

add(**C, name_ja="Suno/Udio音楽訴訟2024",
    name_en="Music labels v. Suno+Udio 2024",
    name_original="UMG/Sony/Warner v. Suno (D. Mass.) and v. Udio (S.D.N.Y.) 2024",
    definition="2024年6月メジャーレーベル3社がSuno・Udioを提訴。AI音楽生成プラットフォームの訓練データに著作権楽曲が含まれると主張、音楽×AI生成の旗艦訴訟となった。",
    background="2024年Suno/Udio商用化、AI音楽生成市場の急成長。",
    development="2024-2025年で生成音楽法形成の中心事案、フェアユース論議の現代版焦点となった。",
    historical_context="2024-2025年AI音楽生成訴訟期。",
    primary_source_url="https://www.riaa.com/wp-content/uploads/2024/06/Suno-Complaint.pdf",
    primary_source_type="RIAA filing (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Suno/Udio訴訟は生成音楽法形成の中心事案。")])

add(**C, name_ja="Doe対GitHub Copilot訴訟",
    name_en="Doe 1 v. GitHub Copilot litigation",
    name_original="Doe 1 v. GitHub, Inc. (N.D. Cal. 2022)",
    definition="2022年11月匿名開発者がGitHub・OpenAI・MicrosoftをCopilotコード生成で提訴。オープンソースライセンス違反を争点とし、コード×AI訴訟の旗艦事例となった。",
    background="2022年Copilot公開、GPL違反論議の浮上。",
    development="2023-2024年で部分却下、ソフトウェア×AI法形成の代表事例として現在進行中。",
    historical_context="2022-2025年コード×AI訴訟期。",
    primary_source_url="https://githubcopilotlitigation.com/",
    primary_source_type="Plaintiff site (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Copilot訴訟はコード作者性論議の代表事例。")],
    cross_domain=[cd("AI-Development","Copilot","Copilot訴訟はコード生成法の中核。")])

add(**C, name_ja="Andersen対Stability AI訴訟",
    name_en="Andersen v. Stability AI 2023",
    name_original="Andersen v. Stability AI Ltd. (N.D. Cal. 2023)",
    definition="2023年1月アーティスト Sarah Andersen ほかがStability AI・Midjourney・DeviantArtを提訴。画像生成AIの訓練データ著作権侵害を争点とし、視覚×AI訴訟の旗艦事例。",
    background="2022年Stable Diffusion公開、アーティスト共同体の対抗運動。",
    development="2023-2024年で原告主張の一部認容、視覚×AI法形成の代表事例となった。",
    historical_context="2023-2025年視覚AI訴訟期。",
    primary_source_url="https://stablediffusionlitigation.com/",
    primary_source_type="Plaintiff site (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Andersen訴訟は視覚×AI著作権法形成の中核。")])

add(**C, name_ja="Tremblay対OpenAI訴訟",
    name_en="Tremblay v. OpenAI 2023",
    name_original="Tremblay v. OpenAI, Inc. (N.D. Cal. 2023)",
    definition="2023年6月小説家 Paul Tremblay・Mona Awad が OpenAI を提訴。ChatGPT が著作物の正確な要約を生成する点を証拠としたAI著作権訴訟の初期代表事例。",
    background="2023年ChatGPT-4公開、小説要約生成能力の問題化。",
    development="2023-2024年でSilverman訴訟と統合審理、初期AI訴訟の判例形成を駆動した。",
    historical_context="2023-2024年初期AI訴訟期。",
    primary_source_url="https://llmlitigation.com/pdf/03223/tremblay-openai-complaint.pdf",
    primary_source_type="Tremblay complaint (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Tremblay訴訟はAI著作権訴訟の初期代表事例。")])

add(**C, name_ja="Chabon対OpenAI訴訟",
    name_en="Chabon v. OpenAI 2023",
    name_original="Chabon v. OpenAI, Inc. (N.D. Cal. 2023)",
    definition="2023年9月Pulitzer賞作家 Michael Chabon ほかが OpenAI を提訴。ChatGPT が著作物のスタイル模倣を行う点を争点とし、文学的スタイル×AI法の代表事例となった。",
    background="2023年Chabon等の作家共同体組織化、AI訓練対抗運動の隆盛。",
    development="2023-2024年で他訴訟と統合、文学スタイル×AI法形成の代表事例。",
    historical_context="2023-2025年作家AI訴訟期。",
    primary_source_url="https://llmlitigation.com/pdf/03223/chabon-openai-complaint.pdf",
    primary_source_type="Chabon complaint (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Chabon訴訟は文学スタイル×AI法の代表事例。")])

add(**C, name_ja="JKローリングAI論争",
    name_en="J.K. Rowling AI controversy",
    name_original="J.K. Rowling on AI authorship (2023-2024)",
    definition="2023-2024年J.K.RowlingがAIによるHarry Potterスタイル模倣・トランス論争でのAI画像悪用に関する一連の発言。世界規模の作家×AI論議を駆動した代表的著名作家言及。",
    background="2023年AIスタイル模倣の社会問題化、Rowlingの作家×AI論議への参与。",
    development="2024-2025年でRowling発言が世界的なAI論議を駆動、著名作家×AI論議の代表事例となった。",
    historical_context="2023-2025年著名作家AI論議期。",
    primary_source_url="https://twitter.com/jk_rowling",
    primary_source_type="Rowling X account (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Rowling論争は著名作家×AI論議の代表事例。")])

add(**C, name_ja="マーガレット・アトウッドAI論",
    name_en="Margaret Atwood AI commentary",
    name_original="Margaret Atwood on AI (2023-2024)",
    definition="2023-2024年Margaret AtwoodのAI論評。『ハンドメイズ・テイル』等のAI訓練無断利用に対する批判で、世界的SF作家のAI批評の代表事例となった。",
    background="2023年Books3問題、Atwood作品のAI訓練利用判明。",
    development="2024-2025年でAtwoodがAuthors Guild訴訟参加、世界SF作家×AI論議を主導した。",
    historical_context="2023-2025年SF作家AI論議期。",
    primary_source_url="https://www.theatlantic.com/technology/archive/2023/09/books3-database-generative-ai-training-copyright-infringement/675363/",
    primary_source_type="Atlantic interview (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Atwood AI論はSF作家×AI批判の代表事例。")])

add(**C, name_ja="スティーヴン・キングAI論",
    name_en="Stephen King on AI",
    name_original="Stephen King on AI training (2023)",
    definition="2023年8月Stephen Kingの『The Atlantic』寄稿。自著がAI訓練に使用されたことを「歓迎しないが避けられない」と論じた著名作家のAI論議代表事例。",
    background="2023年Books3問題化、King作品のAI訓練利用判明。",
    development="2023-2024年でKingの寄稿が作家×AI論議の言説標準となった。",
    historical_context="2023-2025年作家論評期。",
    primary_source_url="https://www.theatlantic.com/books/archive/2023/08/stephen-king-books-ai-writing/675103/",
    primary_source_type="The Atlantic essay (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("King論はベストセラー作家×AI論議の代表事例。")])

add(**C, name_ja="Walters対OpenAI誹謗訴訟",
    name_en="Walters v. OpenAI defamation",
    name_original="Walters v. OpenAI L.L.C. (N.D. Ga. 2023)",
    definition="2023年6月ラジオパーソナリティ Mark Walters が OpenAI を誹謗で提訴。ChatGPT が虚偽事実を生成した世界初のAI誹謗訴訟として注目を集めた事例。",
    background="2023年ChatGPT幻覚問題の社会化、誹謗領域への波及。",
    development="2024年原告敗訴判決、AI誹謗法形成の代表事例として判例化された。",
    historical_context="2023-2024年AI誹謗訴訟期。",
    primary_source_url="https://www.courtlistener.com/docket/67484097/walters-v-openai-llc/",
    primary_source_type="Court filing (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_auth("Walters訴訟はAI幻覚×誹謗法の代表事例。")])


# ============================================================
# B: AI規制（11件）
# ============================================================
add(**C, name_ja="伊Garante GDPRブロック",
    name_en="Italian Garante GDPR ChatGPT block",
    name_original="Garante per la protezione dei dati personali order 2023",
    definition="2023年3月伊データ保護当局GarantéがChatGPTを一時禁止した世界初の国家規模ChatGPT規制。GDPR違反を理由とし、欧州AI規制形成の起点となった。",
    background="2023年GDPR×AI整合性問題、Garante先行規制決定。",
    development="2023-2024年でEU AI法形成への影響、GDPR×AIの代表規制事例として確立した。",
    historical_context="2023-2024年GDPR×AI規制期。",
    primary_source_url="https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9870832",
    primary_source_type="Garante official order (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Garanteブロックは国家AI規制の起点。")])

add(**C, name_ja="EU AI法文学条項詳細",
    name_en="EU AI Act literary provisions detail",
    name_original="EU AI Act Articles 53, 50 (2024)",
    definition="2024年5月成立のEU AI法の文学関連条項。第53条訓練データ要約公開義務、第50条AI生成コンテンツ識別表示義務など、文学×AI法の世界基準を定めた。",
    background="2021年提案以降の議論、2023-2024年の急速合意形成。",
    development="2024-2026年で段階的施行、世界AI法のテンプレートとして他国規制に影響した。",
    historical_context="2024-2026年EU AI法施行期。",
    primary_source_url="https://eur-lex.europa.eu/eli/reg/2024/1689/oj",
    primary_source_type="EU Official Journal (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("EU AI法は世界AI規制の標準。"),
                 fa_canon("第53条要約公開義務はAI訓練データの可視化を制度化。")],
    cross_domain=[cd("AI-Development","AI規制","EU AI法はAI規制の世界基準。")])

add(**C, name_ja="米著作権局2023ガイダンス",
    name_en="US Copyright Office 2023 guidance",
    name_original="USCO Generative AI Statement of Policy (2023)",
    definition="2023年3月米著作権局が公開したAI生成著作物ガイダンス。「人間の創造的寄与」を著作権要件とし、Zarya of the Dawn事件を契機にAI×著作権法を米法体系で整備した。",
    background="2022年Kashtanova事件、AI著作物の登録問題化。",
    development="2023-2025年で世界の著作権局が同様ガイダンス発表、AI著作権法の国際標準形成を主導した。",
    historical_context="2023-2025年AI著作権法形成期。",
    primary_source_url="https://www.copyright.gov/ai/Copyright-Registration-Guidance-Works-Containing-Material-Generated-by-Artificial-Intelligence.pdf",
    primary_source_type="USCO official guidance (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("USCO 2023ガイダンスはAI著作権法の世界基準。")],
    cross_domain=[cd("PHIL","作者性","USCOガイダンスはAI×作者性の法的判断。")])

add(**C, name_ja="日本著作権法30条の4詳細",
    name_en="Japan AI training Article 30-4 detail",
    name_original="日本著作権法第30条の4（2018年改正）",
    definition="2018年改正日本著作権法第30条の4。情報解析目的の著作物利用を著作権者の許諾なしに認める世界最寛容なAI訓練条項として、日本のAI開発立地優位性を法的に確立した。",
    background="2018年改正、機械学習研究促進の法整備。",
    development="2023-2025年で日本がAI開発の法的優遇地として国際的に再評価、AI×著作権法の比較研究の中心事例となった。",
    historical_context="2018-2025年日本AI法形成期。",
    primary_source_url="https://www.bunka.go.jp/seisaku/chosakuken/aiandcopyright.html",
    primary_source_type="文化庁公式 (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("日本30条の4は世界最寛容のAI訓練法条項。")])

add(**C, name_ja="中国生成AI規制2023",
    name_en="China generative AI rules 2023",
    name_original="生成式人工智能服务管理暂行办法（2023年8月）",
    definition="2023年8月施行の中国生成AI暫定管理規則。社会主義核心価値観順守・実名登録・データ出所証明等を義務化し、世界初の包括的生成AI規制として国際的に注目された。",
    background="2023年中国AI急成長、政府規制需要の急増。",
    development="2023-2025年で中国AI法のテンプレートとなり、グローバルAI法形成の比較対象として確立した。",
    historical_context="2023-2025年中国AI規制期。",
    primary_source_url="http://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm",
    primary_source_type="国家网信办 (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("中国生成AI規則は包括的AI規制の代表事例。")])

add(**C, name_ja="韓国AI著作物指針",
    name_en="Korea AI works guidance",
    name_original="韓国文化体育観光部AI著作物利用ガイドライン2023",
    definition="2023年12月韓国文化体育観光部が公開したAI著作物利用ガイドライン。AI訓練データの著作権処理・AI生成著作物の権利帰属を整備し、東アジアAI法の代表事例となった。",
    background="2023年韓国AI政策推進、生成AI急成長への対応。",
    development="2024-2025年で韓国AI法のテンプレート化、東アジアAI法形成を主導した。",
    historical_context="2023-2025年韓国AI法期。",
    primary_source_url="https://www.mcst.go.kr/",
    primary_source_type="MCST official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("韓国AIガイドラインは東アジアAI法の代表事例。")])

add(**C, name_ja="米AI大統領令2023",
    name_en="Biden AI Executive Order 2023",
    name_original="Executive Order 14110 on Safe, Secure, and Trustworthy AI (2023)",
    definition="2023年10月Biden大統領が署名したAI大統領令第14110号。基盤モデル開発者の安全性報告義務・連邦機関のAI政策統一等を定め、米AI政策の中心枠組みとなった。",
    background="2023年AI Safety Summit、米AI政策需要の急増。",
    development="2023-2025年で米連邦AI政策の指針、Trump政権下での廃止議論を経て政策論議の焦点となった。",
    historical_context="2023-2025年米AI政策期。",
    primary_source_url="https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/",
    primary_source_type="White House EO (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("AI大統領令は米AI政策の中心枠組み。")])

add(**C, name_ja="英国AI規制白書2023",
    name_en="UK AI Regulation White Paper 2023",
    name_original="UK Pro-Innovation Approach to AI Regulation (2023)",
    definition="2023年3月英国政府公表のAI規制白書。EU硬規制と異なる「イノベーション促進型」分散規制アプローチを提唱し、英国AI政策の独自路線を示した代表文書。",
    background="2023年Brexit後のAI政策独自化、EU AI法対抗構築。",
    development="2024-2025年で英国AI政策の中心文書、世界のAI規制モデル多様化に寄与した。",
    historical_context="2023-2025年英国AI政策期。",
    primary_source_url="https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach",
    primary_source_type="UK Government White Paper (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("英国白書は分散型AI規制の代表事例。")])

add(**C, name_ja="ブレッチリー宣言2023",
    name_en="Bletchley Declaration 2023",
    name_original="The Bletchley Declaration (2023)",
    definition="2023年11月英国Bletchley Park開催のAI安全サミットで採択された国際宣言。28カ国がフロンティアAI安全性を協調する世界初のAI国際宣言として注目された。",
    background="2023年フロンティアAI急成長、国際協調需要の急増。",
    development="2024-2025年でソウル・パリAIサミットへの継続、AI国際協調の起点となった。",
    historical_context="2023-2025年AI国際協調期。",
    primary_source_url="https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration",
    primary_source_type="UK Government (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("ブレッチリー宣言はAI国際協調の起点。")])

add(**C, name_ja="広島AIプロセス2023",
    name_en="Hiroshima AI Process 2023",
    name_original="G7広島AIプロセス（2023）",
    definition="2023年5月G7広島サミット発のAI国際協調枠組み。生成AIガイドラインを含む包括的AI国際指針を整備し、日本主導のAI国際協調の代表事例となった。",
    background="2023年G7議長国日本のAI政策推進、生成AI急成長への国際対応。",
    development="2023-2024年でG7諸国の生成AIガイドライン採択、日本主導のAI外交の代表事例。",
    historical_context="2023-2024年広島AIプロセス期。",
    primary_source_url="https://www.mofa.go.jp/ecm/ec/page5_000483.html",
    primary_source_type="外務省公式 (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("広島AIプロセスは日本主導AI協調の代表事例。")])


# ============================================================
# C: 生成詩・LLM創造性研究（11件）
# ============================================================
add(**C, name_ja="確率的オウム論文詳細",
    name_en="Stochastic Parrots paper Bender 2021 detail",
    name_original="Bender, Gebru et al. 'On the Dangers of Stochastic Parrots' (FAccT 2021)",
    definition="2021年Emily Bender・Timnit Gebruら共著のFAccT論文。LLMを「確率的オウム」と批判し、Gebru解雇事件を契機にAI批判言説の旗艦文献となった理論的中核。",
    background="2020年GPT-3公開、Bender-Gebru倫理研究の累積。",
    development="2021-2025年でAI批判言説の標準引用、Gebru解雇事件で世界的注目を獲得した。",
    historical_context="2021-2025年AI批判理論期。",
    primary_source_url="https://dl.acm.org/doi/10.1145/3442188.3445922",
    primary_source_type="ACM FAccT proceedings (primary)",
    importance_score=5, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("確率的オウム論文はAI批判言説の旗艦文献。")],
    cross_domain=[cd("PHIL","意味論","Bender論はLLM意味理解の哲学批判。"),
                  cd("AI-Development","LLM批判","確率的オウム論はLLM批判の中核。")])

add(**C, name_ja="ベンダー章魚論証詳細",
    name_en="Bender Octopus argument detail",
    name_original="Bender & Koller 'Climbing Towards NLU' (ACL 2020)",
    definition="2020年Bender・Kollerの章魚思考実験。海底ケーブル傍受で人間言語を学習する章魚は意味理解できないとし、LLM意味理解不可能論の代表的論証を確立した。",
    background="2020年GPT-3前夜、Symbol Grounding問題の再浮上。",
    development="2020-2025年でLLM意味論議の標準引用、AI哲学の中心議論となった。",
    historical_context="2020-2025年LLM意味論議期。",
    primary_source_url="https://aclanthology.org/2020.acl-main.463/",
    primary_source_type="ACL Anthology (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("章魚論証はLLM意味理解論議の中核。")],
    cross_domain=[cd("PHIL","意味論","章魚論証は意味論哲学の現代議論。")])

add(**C, name_ja="イェジン・チョイLLM常識",
    name_en="Yejin Choi commonsense LLM",
    name_original="Yejin Choi (UW/AI2) commonsense reasoning research",
    definition="ワシントン大学/AI2のYejin Choi研究室によるLLM常識推論研究。COMET・ATOMIC・Defeasible NLI等のベンチマークを通じてLLMの常識限界を可視化、AI×常識論議の中核研究を主導。",
    background="2010年代中盤Choi常識推論研究の累積。",
    development="2020-2025年でChoi研究がLLM常識論議の標準、世界AI×常識研究の中核となった。",
    historical_context="2020-2025年LLM常識研究期。",
    primary_source_url="https://homes.cs.washington.edu/~yejin/",
    primary_source_type="UW research page (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Choi常識研究はLLM常識論議の中核。")])

add(**C, name_ja="Branwen GPT-4文学評価",
    name_en="Branwen GPT-4 creative writing evaluation",
    name_original="Gwern Branwen 'GPT-3 Creative Fiction' (2020-)",
    definition="Gwern Branwen による2020年以降のGPT系創作評価集成。詩・散文・SF生成の網羅的事例を蓄積し、AI×創作研究の代表的個人サイト・批評参照源となった。",
    background="2020年GPT-3公開、独立研究者Branwenの早期評価活動。",
    development="2020-2025年でBranwen評価集成がAI創作研究の世界標準参照、AI×文学批評の中核資料となった。",
    historical_context="2020-2025年Branwen評価期。",
    primary_source_url="https://gwern.net/gpt-3",
    primary_source_type="Gwern.net (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Branwen評価はAI創作批評の代表参照源。")])

add(**C, name_ja="Constitutional AI Anthropic",
    name_en="Constitutional AI Anthropic",
    name_original="Bai et al. 'Constitutional AI' (Anthropic 2022)",
    definition="2022年Anthropic公開の Constitutional AI 論文。AIに憲法的原則を学習させて自律的に倫理判断する手法を提唱、Claude設計の中核技術として世界AI倫理論議を主導した。",
    background="2022年RLHF限界と倫理AI需要、Anthropic安全研究の集大成。",
    development="2022-2025年でClaude基盤技術となり、AI倫理×LLM技術の中核となった。",
    historical_context="2022-2025年Constitutional AI期。",
    primary_source_url="https://arxiv.org/abs/2212.08073",
    primary_source_type="arXiv (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Constitutional AIはAI倫理×技術の代表事例。")],
    cross_domain=[cd("AI-Development","RLHF","Constitutional AIはRLHFの代表応用。")])

add(**C, name_ja="RLHF創造性影響研究",
    name_en="RLHF impact on LLM creativity",
    name_original="Kirk et al. 'Understanding the Effects of RLHF on LLM Generalisation and Diversity' (ICLR 2024)",
    definition="2024年Kirkらの研究。人間フィードバック強化学習がLLM出力の多様性を低下させる現象を実証し、RLHF×創造性論議の代表研究となった。",
    background="2023年RLHF普及、創造性低下の経験的観察。",
    development="2024-2025年でRLHF×創造性研究の標準引用、AI創作研究の中核となった。",
    historical_context="2023-2025年RLHF創造性研究期。",
    primary_source_url="https://arxiv.org/abs/2310.06452",
    primary_source_type="arXiv (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("RLHF研究はAI創造性論議の代表研究。")])

add(**C, name_ja="Park生成エージェント",
    name_en="Park 2023 generative agents",
    name_original="Park et al. 'Generative Agents: Interactive Simulacra of Human Behavior' (UIST 2023)",
    definition="2023年Stanford Joon Park らの生成エージェント論文。25体のLLMエージェントが村で生活する Smallville シミュレーションで、マルチエージェント物語生成の代表事例となった。",
    background="2023年LLM大衆化、エージェント研究の浮上。",
    development="2023-2025年で生成エージェント研究の標準引用、AI×物語シミュレーションの中核となった。",
    historical_context="2023-2025年生成エージェント期。",
    primary_source_url="https://arxiv.org/abs/2304.03442",
    primary_source_type="arXiv (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Park生成エージェントはAI×物語シミュレーションの代表事例。")],
    cross_domain=[cd("AI-Development","エージェント","Park生成エージェントは複数エージェント研究の中核。")])

add(**C, name_ja="LLMキャラクター一貫性",
    name_en="LLM character consistency research",
    name_original="Wang et al. 'RoleLLM' (ACL 2024) and related",
    definition="2023-2024年LLMキャラクター一貫性研究の集成。RoleLLM・CharacterChat等のベンチマークでLLMの長対話キャラクター維持能力を評価、AI×キャラクター研究の代表領域となった。",
    background="2023年Character.AI普及、キャラクター一貫性需要の浮上。",
    development="2024-2025年でキャラクター一貫性研究が学術領域として確立、AI物語論の中核となった。",
    historical_context="2023-2025年キャラクター一貫性研究期。",
    primary_source_url="https://arxiv.org/abs/2310.00746",
    primary_source_type="arXiv (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("キャラクター一貫性研究はAI物語論の代表領域。")])

add(**C, name_ja="マルチエージェント物語",
    name_en="Multi-agent narrative generation",
    name_original="MetaGPT, AutoGen, ChatDev, Camel-AI multi-agent narrative",
    definition="2023年以降のマルチエージェント物語生成研究。MetaGPT・AutoGen・ChatDev等が複数LLMエージェントの協働物語生成を実装、AI×集合的物語の代表事例となった。",
    background="2023年LLMエージェント研究の急成長、マルチエージェント物語需要。",
    development="2023-2025年でマルチエージェント物語が研究領域として確立、AI集合創造性の中核となった。",
    historical_context="2023-2025年マルチエージェント物語期。",
    primary_source_url="https://github.com/geekan/MetaGPT",
    primary_source_type="MetaGPT GitHub (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("マルチエージェント物語はAI集合創造性の代表事例。")])

add(**C, name_ja="Voyager Minecraftナラティブ",
    name_en="Voyager Minecraft narrative",
    name_original="Wang et al. 'Voyager: An Open-Ended Embodied Agent' (NeurIPS 2023)",
    definition="2023年NVIDIA・Caltech Wang らのVoyager論文。GPT-4駆動のMinecraftエージェントが自律的目標生成と物語的経験を蓄積し、AI×ゲーム物語の代表研究となった。",
    background="2023年Minecraft×AIエージェント研究、自律的物語需要。",
    development="2023-2025年でVoyagerが具現化AI研究の標準、AI×ゲーム物語の中核となった。",
    historical_context="2023-2025年具現化AI研究期。",
    primary_source_url="https://voyager.minedojo.org/",
    primary_source_type="Voyager project site (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("VoyagerはAI×ゲーム物語の代表研究。")],
    cross_domain=[cd("AI-Development","具現化AI","Voyagerは具現化AI研究の代表事例。")])

add(**C, name_ja="Pi Inflectionパーソナ",
    name_en="Pi Inflection AI persona",
    name_original="Inflection AI 'Pi' personal AI (2023)",
    definition="2023年Mustafa Suleyman創業のInflection AI開発の対話AI Pi。共感的パーソナリティを軸に設計され、AI×パーソナリティ設計の代表事例となった対話AIプロダクト。",
    background="2023年Inflection AI創業、対話AI差別化戦略。",
    development="2023-2024年でPiが世界規模の対話AI事例、Microsoft買収後にAI×パーソナリティ研究の代表事例となった。",
    historical_context="2023-2024年対話AIパーソナ期。",
    primary_source_url="https://pi.ai/",
    primary_source_type="Pi.ai official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("PiはAI×パーソナリティ設計の代表事例。")])


# ============================================================
# D: プロンプト工学批評（10件）
# ============================================================
add(**C, name_ja="Riley Goodsideプロンプト",
    name_en="Riley Goodside prompt engineering",
    name_original="Riley Goodside (Scale AI prompt engineer)",
    definition="2022年Scale AI入社のRiley Goodsideによる先駆的プロンプト工学。Twitter上で蓄積したプロンプト技法集成が世界プロンプト工学の標準実践となった代表的個人実践者。",
    background="2022年GPT-3普及、プロンプト工学の領域形成。",
    development="2022-2025年でGoodsideがプロンプト工学の世界標準実践者、AI批評の代表参照源となった。",
    historical_context="2022-2025年プロンプト工学期。",
    primary_source_url="https://twitter.com/goodside",
    primary_source_type="Riley Goodside X account (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Goodsideはプロンプト工学の世界標準実践者。")])

add(**C, name_ja="Simon Willisonプロンプト批評",
    name_en="Simon Willison prompt practice",
    name_original="Simon Willison's Weblog (2022-)",
    definition="2022年以降のSimon Willison によるLLM批評ブログ。プロンプトインジェクション概念の確立等、AI批評ジャーナリズムの代表的個人実践者として世界AI批評を主導した。",
    background="2022年Willisonブログ更新、AI批評需要の急増。",
    development="2022-2025年でWillisonブログがAI批評ジャーナリズムの世界標準参照源となった。",
    historical_context="2022-2025年AI批評ジャーナリズム期。",
    primary_source_url="https://simonwillison.net/",
    primary_source_type="Simon Willison's Weblog (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("WillisonブログはAI批評ジャーナリズムの代表事例。")])

add(**C, name_ja="Karpathyソフトウェア論",
    name_en="Karpathy Software 2.0/3.0",
    name_original="Andrej Karpathy 'Software 2.0' (2017) / 'Software 3.0' (2024)",
    definition="2017年Andrej Karpathy 'Software 2.0'論文と2024年 'Software 3.0' エッセイ。ニューラルネット・LLMが従来コードを置換する潮流を理論化、AI開発思想の代表的論考。",
    background="2017年深層学習急成長、Karpathyのテスラ-OpenAI経験。",
    development="2017-2025年でSoftware 2.0/3.0論がAI開発思想の世界標準引用、AI×ソフトウェア哲学の中核となった。",
    historical_context="2017-2025年Software 2.0/3.0期。",
    primary_source_url="https://karpathy.medium.com/software-2-0-a64152b37c35",
    primary_source_type="Karpathy Medium (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Karpathyソフトウェア論はAI×開発哲学の中核。")],
    cross_domain=[cd("PHIL","技術哲学","Software 2.0論は技術哲学の代表概念。")])

add(**C, name_ja="Janusシミュレータ論",
    name_en="Janus simulators essay",
    name_original="janus 'Simulators' (LessWrong 2022)",
    definition="2022年janusのLessWrong投稿『Simulators』。LLMをエージェントではなく「シミュレータ」として再定義し、Waluigi効果等の概念を生み出したAI批評代表エッセイ。",
    background="2022年GPT-3拡張、LLM性質論議の浮上。",
    development="2022-2025年でJanusエッセイがAI批評の代表論考、LessWrong×AI批評の中核となった。",
    historical_context="2022-2025年AI批評理論期。",
    primary_source_url="https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators",
    primary_source_type="LessWrong post (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("JanusシミュレータはLLM性質論議の代表概念。")],
    cross_domain=[cd("PHIL","存在論","Janusシミュレータ論はAI存在論の代表概念。")])

add(**C, name_ja="Mollick One Useful Thing",
    name_en="Ethan Mollick One Useful Thing",
    name_original="Ethan Mollick 'One Useful Thing' Substack (2022-)",
    definition="2022年Wharton教授Ethan Mollick開設のSubstack『One Useful Thing』。教育×AI実践の代表的論者として世界規模で読まれ、AI教育論議の中核言説となった。",
    background="2022年ChatGPT教育応用、Mollickの早期実践研究。",
    development="2022-2025年でMollickニュースレターがAI教育論議の世界標準、書籍『Co-Intelligence』(2024)も出版された。",
    historical_context="2022-2025年AI教育論議期。",
    primary_source_url="https://www.oneusefulthing.org/",
    primary_source_type="Substack (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Mollickニュースレターはこの分野の代表論者。")])

add(**C, name_ja="Maggie Appletonヴィンテージ",
    name_en="Maggie Appleton vintage internet AI",
    name_original="Maggie Appleton 'The Expanding Dark Forest' (2022)",
    definition="2022年Maggie Appleton『The Expanding Dark Forest and Generative AI』エッセイ。生成AIによる「ヴィンテージ・インターネット」消失論を提唱し、AI×文化批評の代表エッセイとなった。",
    background="2022年生成AI急成長、人間文化×AI論議の浮上。",
    development="2022-2025年でAppleton エッセイがAI×文化批評の世界標準参照、AI批評の中核となった。",
    historical_context="2022-2025年AI×文化批評期。",
    primary_source_url="https://maggieappleton.com/dark-forest",
    primary_source_type="Maggie Appleton blog (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Appleton ヴィンテージ論はAI×文化批評の代表エッセイ。")])

add(**C, name_ja="James Yu Sudowriteエッセイ",
    name_en="James Yu Sudowrite essays",
    name_original="James Yu (Sudowrite cofounder) writings",
    definition="Sudowrite創業者James YuのAI×創作エッセイ集。SF作家でもあるYu によるAI執筆ツール思想の代表的論考で、AI×創作実践の中核言説となった。",
    background="2021年Sudowrite創業、Yu のSF作家×AI起業家経験。",
    development="2021-2025年でYuエッセイがAI執筆ツール思想の世界標準参照、AI×創作実践の中核となった。",
    historical_context="2021-2025年AI創作思想期。",
    primary_source_url="https://www.sudowrite.com/blog",
    primary_source_type="Sudowrite blog (primary)",
    importance_score=2, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Yu エッセイはAI×創作実践の中核言説。")])

add(**C, name_ja="プロンプト工学指針詩学",
    name_en="Prompt engineering guides as poetics",
    name_original="OpenAI/Anthropic prompt engineering guides",
    definition="OpenAI・Anthropic等が公開する公式プロンプト工学指針。モデル提供企業による標準的プロンプト技法集成が、AI×文体論の中核資料として研究対象となった。",
    background="2023年プロンプト工学標準化、企業公式指針の普及。",
    development="2023-2025年で公式指針がAI×文体論研究の中核資料、プロンプト詩学の標準参照源となった。",
    historical_context="2023-2025年プロンプト指針期。",
    primary_source_url="https://platform.openai.com/docs/guides/prompt-engineering",
    primary_source_type="OpenAI official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("企業プロンプト指針はAI×文体論の中核資料。")])

add(**C, name_ja="脱獄プロンプト類型論",
    name_en="Jailbreak prompt typology",
    name_original="Wei et al. 'Jailbroken: How Does LLM Safety Training Fail?' (NeurIPS 2023)",
    definition="2023年Alexander Wei らのNeurIPS論文。脱獄プロンプトを類型化し、DAN・grandma exploit・Sydney等の代表事例を学術整理、AI×レトリック研究の代表論文となった。",
    background="2023年脱獄プロンプト現象の社会化、学術整理需要。",
    development="2023-2025年でWei論文が脱獄研究の世界標準引用、AI×レトリック研究の中核となった。",
    historical_context="2023-2025年脱獄研究期。",
    primary_source_url="https://arxiv.org/abs/2307.02483",
    primary_source_type="arXiv NeurIPS (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Wei脱獄類型論はAI×レトリック研究の代表論文。")],
    cross_domain=[cd("AI-Development","脱獄","Wei脱獄類型論は脱獄研究の中核。")])

add(**C, name_ja="システムプロンプト作者声",
    name_en="System prompt as authorial voice",
    name_original="Anthropic Claude system prompt disclosures (2024)",
    definition="2024年Anthropic公開のClaude システムプロンプト全文。AIアシスタントの『声』を構築する作者的テクストとして公開され、AI×声論研究の代表事例となった。",
    background="2024年AI透明性需要、システムプロンプト公開議論。",
    development="2024-2025年でAnthropicがシステムプロンプト公開を制度化、AI×声論議の標準事例となった。",
    historical_context="2024-2025年システムプロンプト透明性期。",
    primary_source_url="https://docs.anthropic.com/en/release-notes/system-prompts",
    primary_source_type="Anthropic docs (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Claudeシステムプロンプト公開はAI×声論議の標準事例。")])


# ============================================================
# E: マルチモーダル文学（11件）
# ============================================================
add(**C, name_ja="DALL-E 3プロンプト詩学",
    name_en="DALL-E 3 prompt poetics",
    name_original="OpenAI DALL-E 3 system / GPT-4V (2023)",
    definition="2023年OpenAI公開のDALL-E 3。ChatGPT統合でプロンプトをLLMが詳細化する設計を採用、テクスト×画像生成プロンプトの詩学研究の代表事例となった。",
    background="2023年DALL-E 3公開、LLM-画像生成統合の急成長。",
    development="2023-2025年でDALL-E 3プロンプトがマルチモーダル詩学研究の標準対象、AI×エクフラシスの中核となった。",
    historical_context="2023-2025年マルチモーダル詩学期。",
    primary_source_url="https://openai.com/index/dall-e-3/",
    primary_source_type="OpenAI announcement (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("DALL-E 3はマルチモーダル詩学の代表事例。")],
    cross_domain=[cd("PT","エクフラシス","DALL-E 3はAI×エクフラシスの代表事例。")])

add(**C, name_ja="Midjourneyキャプション詩学",
    name_en="Midjourney captions as ekphrasis",
    name_original="Midjourney v6 prompts (2024)",
    definition="2024年Midjourney v6普及によるプロンプト詩学。世界規模で集積されたMidjourneyプロンプトがエクフラシス（画像描写詩）の現代版として研究対象となり、AI×詩学の代表領域となった。",
    background="2022年Midjourney公開、2024年v6でプロンプト詩学の成熟。",
    development="2022-2025年でMidjourneyプロンプトがAI×エクフラシス研究の中核資料、詩学領域として確立した。",
    historical_context="2022-2025年Midjourney詩学期。",
    primary_source_url="https://docs.midjourney.com/",
    primary_source_type="Midjourney docs (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Midjourneyプロンプトは現代エクフラシスの代表事例。")],
    cross_domain=[cd("PT","エクフラシス","Midjourneyプロンプトはエクフラシス詩学の現代継承。")])

add(**C, name_ja="Sora物語生成詳細",
    name_en="Sora narrative implications detail",
    name_original="OpenAI Sora technical report (2024)",
    definition="2024年OpenAI公開のSora動画生成モデル詳細。世界モデル仮説と物語生成能力を主張し、AI×映像物語の旗艦研究としてマルチモーダル文学の代表事例となった。",
    background="2024年Sora公開、世界モデル論議の急成長。",
    development="2024-2025年でSora がAI×映像物語の世界標準参照、マルチモーダル文学研究の中核となった。",
    historical_context="2024-2025年Sora物語期。",
    primary_source_url="https://openai.com/research/video-generation-models-as-world-simulators",
    primary_source_type="OpenAI research (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("SoraはAI×映像物語の旗艦研究。")],
    cross_domain=[cd("AI-Development","世界モデル","Soraは世界モデル研究の代表事例。")])

add(**C, name_ja="Runway Gen-3物語",
    name_en="Runway Gen-3 narrative",
    name_original="Runway Gen-3 Alpha (2024)",
    definition="2024年Runway公開のGen-3 Alpha動画生成モデル。映画作家・映像作家にAI動画生成を本格的に提供し、AI×映画製作の代表プラットフォームとなった。",
    background="2024年Runway×映画業界連携、商用AI動画生成需要。",
    development="2024-2025年でRunwayが映画AIツールの世界標準、AI×映像物語の中核プラットフォームとなった。",
    historical_context="2024-2025年Runway期。",
    primary_source_url="https://runwayml.com/research/introducing-gen-3-alpha",
    primary_source_type="Runway research (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Runway Gen-3はAI×映画製作の代表事例。")])

add(**C, name_ja="Stable Video Diffusion",
    name_en="Stable Video Diffusion",
    name_original="Stability AI 'Stable Video Diffusion' (2023)",
    definition="2023年11月Stability AI公開のStable Video Diffusion。オープンソース動画生成モデルとして公開され、AI×映像生成の民主化を駆動した代表モデル。",
    background="2023年動画生成需要、Stability AIオープンソース戦略。",
    development="2023-2024年でSVDがオープン動画生成の世界標準、コミュニティ動画AI生態系を形成した。",
    historical_context="2023-2024年オープン動画AI期。",
    primary_source_url="https://stability.ai/news/stable-video-diffusion-open-ai-video-model",
    primary_source_type="Stability AI announcement (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("SVDはオープン動画生成の民主化代表事例。")])

add(**C, name_ja="Eleven Labs声クローン",
    name_en="Eleven Labs voice cloning narration",
    name_original="ElevenLabs voice cloning platform (2022-)",
    definition="2022年Eleven Labs創業の声クローン・ナレーションプラットフォーム。10秒音声で個人の声を再現する技術を商用化し、AI×ナレーション・オーディオブック市場を駆動した。",
    background="2022年Eleven Labs創業、声クローン技術の商用化。",
    development="2022-2025年でEleven Labsが声クローン×ナレーションの世界標準、オーディオブック×AI市場の中核となった。",
    historical_context="2022-2025年声クローン期。",
    primary_source_url="https://elevenlabs.io/",
    primary_source_type="ElevenLabs official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_auth("Eleven Labs声クローンは音声真正性論議の代表事例。")])

add(**C, name_ja="OpenAI Voice Engine",
    name_en="OpenAI Voice Engine",
    name_original="OpenAI Voice Engine (2024)",
    definition="2024年OpenAI公開のVoice Engineモデル。15秒音声で個人の声を再現する技術を限定公開し、声クローン×AI倫理論議の代表事例となったAI音声プラットフォーム。",
    background="2024年OpenAI音声AI戦略、Eleven Labs対抗。",
    development="2024-2025年でVoice Engineが限定公開のままだが、声クローン×倫理議論の標準事例となった。",
    historical_context="2024-2025年OpenAI音声AI期。",
    primary_source_url="https://openai.com/index/navigating-the-challenges-and-opportunities-of-synthetic-voices/",
    primary_source_type="OpenAI announcement (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_auth("Voice Engineは声クローン×倫理議論の代表事例。")])

add(**C, name_ja="Apple Intelligenceナレーション",
    name_en="Apple Intelligence narration",
    name_original="Apple Intelligence (2024)",
    definition="2024年Apple公開のApple Intelligence。デバイス内AI処理によるナレーション・要約機能で、世界規模の消費者AI体験を駆動するマルチモーダルAIプラットフォーム。",
    background="2024年Apple AI戦略、デバイス内AI処理の確立。",
    development="2024-2025年でApple IntelligenceがマルチモーダルAIの大衆化を駆動、世界規模のAI体験を変革した。",
    historical_context="2024-2025年Apple AI期。",
    primary_source_url="https://www.apple.com/apple-intelligence/",
    primary_source_type="Apple official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Apple IntelligenceはマルチモーダルAI大衆化の代表事例。")])

add(**C, name_ja="NotebookLM Audio Overview",
    name_en="Google NotebookLM Audio Overview",
    name_original="Google NotebookLM Audio Overview (2024)",
    definition="2024年Google公開のNotebookLM Audio Overview機能。アップロード文書から二人ホスト形式のポッドキャストを自動生成し、AI×音声物語の代表事例となった機能。",
    background="2024年Google AI推進、ポッドキャスト×AI需要。",
    development="2024-2025年でAudio Overview機能がポッドキャスト×AIの世界標準、知識×音声生成の代表事例となった。",
    historical_context="2024-2025年Audio Overview期。",
    primary_source_url="https://blog.google/technology/ai/notebooklm-audio-overviews/",
    primary_source_type="Google blog (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Audio OverviewはAI×音声物語の代表事例。"),
                 fa_recv("Audio Overviewは知識受容形式を再構成する。")])

add(**C, name_ja="AIカバーソング",
    name_en="AI cover songs as derivative literature",
    name_original="So-Vits-SVC voice conversion AI covers (2023-)",
    definition="2023年以降のSo-Vits-SVCベースAIカバーソング現象。Drake×Weeknd『Heart on My Sleeve』等の事例で派生文学×AI論議を駆動、AI×音楽派生創作の代表事例となった。",
    background="2023年So-Vits-SVC普及、AIカバーソング急成長。",
    development="2023-2025年でAIカバーソングがAI派生創作の代表事例、音楽×AI法形成の中核となった。",
    historical_context="2023-2025年AIカバーソング期。",
    primary_source_url="https://github.com/svc-develop-team/so-vits-svc",
    primary_source_type="So-Vits-SVC GitHub (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_auth("AIカバーソングは派生創作×真正性論議の代表事例。")])

add(**C, name_ja="GPT-4Vマルチモーダル批評",
    name_en="GPT-4V multimodal criticism",
    name_original="OpenAI GPT-4V(ision) (2023)",
    definition="2023年9月OpenAI公開のGPT-4 Vision。テクスト×画像理解を統合し、文学批評・エクフラシス・視覚詩学のAI実践を可能にした代表的マルチモーダルLLM。",
    background="2023年マルチモーダルLLM急成長、視覚理解需要。",
    development="2023-2025年でGPT-4VがマルチモーダルAI批評の世界標準、AI×視覚詩学の中核となった。",
    historical_context="2023-2025年マルチモーダルLLM期。",
    primary_source_url="https://openai.com/index/gpt-4v-system-card/",
    primary_source_type="OpenAI system card (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("GPT-4VはマルチモーダルAI批評の代表事例。")])


# ============================================================
# F: HCI×文学・インタラクティブ（10件）
# ============================================================
add(**C, name_ja="Eastgate Storyspace",
    name_en="Eastgate Storyspace",
    name_original="Eastgate Systems Storyspace (1987-)",
    definition="1987年Eastgate Systems開発のハイパーテクスト執筆ソフトウェア。Michael Joyce『afternoon, a story』等の古典ハイパーフィクションを生み、デジタル文学黎明期の中核ツールとなった。",
    background="1980年代後半ハイパーテクスト研究、Joyce-Bolter共同開発。",
    development="1987-2010年代でStoryspaceがハイパーフィクションの世界標準、デジタル文学史の中核ツールとなった。",
    historical_context="1987-2010年代ハイパーフィクション期。",
    primary_source_url="https://www.eastgate.com/storyspace/",
    primary_source_type="Eastgate official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Storyspaceはハイパーフィクションの世界標準ツール。")])

add(**C, name_ja="Inanimate Alice",
    name_en="Inanimate Alice",
    name_original="Pullinger & Joseph 'Inanimate Alice' (2005-)",
    definition="2005年Kate Pullinger・Chris Joseph 創作のデジタル多話小説『Inanimate Alice』。10エピソードの世界横断的物語で、教育×デジタル文学の代表事例として世界規模で読まれた。",
    background="2005年Pullinger-Joseph 共同創作、教育市場参入。",
    development="2005-2024年でInanimate Aliceが教育×デジタル文学の世界標準、デジタル文学教育の代表事例となった。",
    historical_context="2005-2025年デジタル文学教育期。",
    primary_source_url="https://inanimatealice.com/",
    primary_source_type="Inanimate Alice official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Inanimate Aliceは教育×デジタル文学の代表事例。")])

add(**C, name_ja="Pry app回顧",
    name_en="Pry app retrospective",
    name_original="Tender Claws 'Pry' (2014) retrospective",
    definition="2014年Tender Claws開発のiPad小説『Pry』。タッチ操作で意識の流れを表現する革新的UI で第13回USC ガドフリー賞を受賞、モバイル×デジタル文学の代表作として確立した。",
    background="2014年Tender Claws創業、モバイル×文学需要。",
    development="2014-2024年でPryがモバイル×デジタル文学の代表作、回顧的批評の中核作品となった。",
    historical_context="2014-2024年モバイル×文学期。",
    primary_source_url="https://prynovella.com/",
    primary_source_type="Pry official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Pryはモバイル×デジタル文学の代表作。")])

add(**C, name_ja="80 Daysナラティブ",
    name_en="80 Days narrative",
    name_original="Inkle '80 Days' (2014)",
    definition="2014年Inkle開発のVerne原作×Meg Jayanth脚本『80 Days』。750,000語のインタラクティブ・フィクションで、Time誌2014年ベストゲーム選定、ゲーム×文学の代表作となった。",
    background="2014年Inkle×Jayanth共同制作、ナラティブゲーム需要。",
    development="2014-2024年で80 Daysがゲーム×文学の世界標準、ナラティブゲーム研究の中核作品となった。",
    historical_context="2014-2024年ナラティブゲーム期。",
    primary_source_url="https://www.inklestudios.com/80days/",
    primary_source_type="Inkle official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("80 Daysはゲーム×文学の代表作。")])

add(**C, name_ja="Florenceゲーム文学",
    name_en="Florence game-as-literature",
    name_original="Mountains 'Florence' (2018)",
    definition="2018年Mountains開発のモバイル恋愛ゲーム『Florence』。30分の感情的物語をUI操作で表現し、Apple Design賞・BAFTAゲーム部門を受賞、ゲーム×文学の代表作となった。",
    background="2018年Mountains（元Monument Valley開発者）創業、感情的UI需要。",
    development="2018-2024年でFlorenceが感情的ゲーム×文学の世界標準、UI×物語研究の中核となった。",
    historical_context="2018-2024年感情ゲーム期。",
    primary_source_url="https://mountains.studio/florence/",
    primary_source_type="Mountains official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("FlorenceはUI×物語の代表事例。")])

add(**C, name_ja="Heaven's Vault",
    name_en="Heaven's Vault",
    name_original="Inkle 'Heaven's Vault' (2019)",
    definition="2019年Inkle開発の考古学SF『Heaven's Vault』。プレイヤーが古代言語を解読する革新的物語で、言語学×物語ゲームの代表作として評価された。",
    background="2019年Inkle×Jon Ingold共同制作、言語学×物語需要。",
    development="2019-2024年でHeaven's Vaultが言語学×物語ゲームの世界標準、AI×言語学物語の参照源となった。",
    historical_context="2019-2024年言語ゲーム期。",
    primary_source_url="https://www.inklestudios.com/heavensvault/",
    primary_source_type="Inkle official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Heaven's Vaultは言語学×物語ゲームの代表作。")])

add(**C, name_ja="Citizen Sleeper",
    name_en="Citizen Sleeper",
    name_original="Jump Over the Age 'Citizen Sleeper' (2022)",
    definition="2022年Gareth Damian Martin 単独開発の TTRPG ベース SF小説ゲーム『Citizen Sleeper』。BAFTA Best Narrative ノミネート、TTRPG×文学×ゲームの代表作として評価された。",
    background="2022年Martin単独制作、TTRPG×物語需要。",
    development="2022-2024年でCitizen Sleeperが個人作家×ナラティブゲームの代表作、続編も2024年に発表された。",
    historical_context="2022-2024年TTRPG物語期。",
    primary_source_url="https://www.citizensleeper.com/",
    primary_source_type="Jump Over the Age (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Citizen Sleeperは個人作家×ナラティブゲームの代表作。")])

add(**C, name_ja="Disco Elysium文学",
    name_en="Disco Elysium as literature",
    name_original="ZA/UM 'Disco Elysium' (2019)",
    definition="2019年ZA/UM開発のRPG『Disco Elysium』。文学的高密度脚本で BAFTA・GDC ナラティブ賞を受賞、ゲーム×文学の頂点作として21世紀文学批評で議論された代表作。",
    background="2019年ZA/UM × Robert Kurvitz 文学コレクティブ、エストニア発文学RPG。",
    development="2019-2024年でDisco Elysiumがゲーム×文学批評の中核作品、Booker賞級文学批評で議論された。",
    historical_context="2019-2024年文学RPG期。",
    primary_source_url="https://discoelysium.com/",
    primary_source_type="ZA/UM official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Disco Elysiumはゲーム×文学批評の頂点作。"),
                 fa_canon("Disco Elysiumは21世紀文学批評の正典化議論を引き起こした。")])

add(**C, name_ja="Twineエコシステム回顧",
    name_en="Twine ecosystem retrospective",
    name_original="Anna Anthropy 'Rise of the Videogame Zinesters' (2012)",
    definition="2012年Anna Anthropy 著書を中心とするTwine批評集成。Twineを「ビデオゲーム自費出版」として理論化し、酷詩・クィア・周縁声のデジタル文学プラットフォームとして批評領域を確立した。",
    background="2009年Twine公開、Anthropy ら独立開発者運動の隆盛。",
    development="2012-2024年でTwine批評がデジタル文学批評の中核領域、AnthropyらのTwine文学批評が確立された。",
    historical_context="2012-2024年Twine批評期。",
    primary_source_url="https://www.sevenstories.com/books/3702-rise-of-the-videogame-zinesters",
    primary_source_type="Seven Stories Press (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Twine批評はデジタル文学批評の代表領域。")])

add(**C, name_ja="ELO Electronic Literature Org",
    name_en="ELO Electronic Literature Organization",
    name_original="Electronic Literature Organization (1999-)",
    definition="1999年設立の電子文学組織。Electronic Literature Collection の3巻刊行・年次大会開催を通じてデジタル文学のアーカイブ・批評・教育を主導、世界デジタル文学研究の中核機関。",
    background="1999年MIT-UCLA共同設立、デジタル文学制度化需要。",
    development="1999-2025年でELOがデジタル文学研究の世界標準、ELC1-3刊行で正典化を主導した。",
    historical_context="1999-2025年デジタル文学制度化期。",
    primary_source_url="https://eliterature.org/",
    primary_source_type="ELO official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("ELOはデジタル文学正典化の中核機関。")])


# ============================================================
# G: DH ベンチマーク（7件）
# ============================================================
add(**C, name_ja="BookCorpus論争詳細",
    name_en="BookCorpus controversy detail",
    name_original="Bandy & Vincent 'Addressing Documentation Debt for BookCorpus' (2021)",
    definition="2021年Jack Bandy・Nicholas Vincent論文。BookCorpus（無料電子書籍7,185冊）の著作権・倫理問題を学術的に検証し、AI訓練データの倫理批判の代表研究となった。",
    background="2015年BookCorpus公開、2021年倫理論議の本格化。",
    development="2021-2025年でBandy-Vincent論文がAI訓練データ批判の標準引用、データ倫理研究の中核となった。",
    historical_context="2021-2025年データ倫理研究期。",
    primary_source_url="https://arxiv.org/abs/2105.05241",
    primary_source_type="arXiv (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("BookCorpus論争は訓練データ倫理の代表研究。")])

add(**C, name_ja="Project Gutenbergコーパス",
    name_en="Project Gutenberg as corpus",
    name_original="Project Gutenberg (1971-) as NLP corpus",
    definition="1971年Michael Hart創設のProject Gutenberg。70,000冊以上のPDテクストがNLP・LLM研究の標準コーパスとして利用され、デジタル文学研究の中核資料となった。",
    background="1971年Gutenberg創設、デジタル化PDテクスト需要。",
    development="1971-2025年でGutenbergがNLP研究の世界標準コーパス、AI訓練データの中核資料となった。",
    historical_context="1971-2025年Gutenberg期。",
    primary_source_url="https://www.gutenberg.org/",
    primary_source_type="Project Gutenberg (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("GutenbergはAI訓練データの中核資料。")])

add(**C, name_ja="HathiTrust Research Center",
    name_en="HathiTrust Research Center",
    name_original="HathiTrust Research Center (HTRC, 2011-)",
    definition="2011年Indiana・Illinois共同設立のHTRC。HathiTrust約2,000万冊のテクストデータマイニング基盤として、計算的文学研究の世界標準インフラとなった。",
    background="2011年Google Books和解後、研究用テクスト基盤需要。",
    development="2011-2025年でHTRCが計算的文学研究の世界標準、Capsule・Workset Builder等のツール展開された。",
    historical_context="2011-2025年HTRC期。",
    primary_source_url="https://www.hathitrust.org/htrc",
    primary_source_type="HTRC official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_canon("HTRCは計算的文学研究の世界標準インフラ。")])

add(**C, name_ja="JSTOR Constellate",
    name_en="JSTOR Constellate",
    name_original="ITHAKA JSTOR Constellate (2020-2024)",
    definition="2020年JSTOR-Portico-ITHAKA連携公開のテクストマイニング基盤Constellate。学術論文・新聞のNLP研究を可能にし、人文学計算研究の代表プラットフォームとなった。",
    background="2020年JSTOR×データ研究需要、ITHAKA戦略。",
    development="2020-2024年でConstellateが計算人文学の代表基盤、2024年7月サービス終了で研究生態系の課題を露呈した。",
    historical_context="2020-2024年Constellate期。",
    primary_source_url="https://constellate.org/",
    primary_source_type="JSTOR Constellate (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_canon("Constellate終了は研究基盤持続性の代表事例。")])

add(**C, name_ja="BookSumベンチマーク",
    name_en="BookSum benchmark",
    name_original="Kryscinski et al. 'BookSum' (2021)",
    definition="2021年Salesforce研究Kryscinskiらの長文要約ベンチマーク BookSum。書籍規模テクストの要約評価で、長文LLM研究の代表ベンチマークとして確立した。",
    background="2021年長文LLM需要、Salesforce研究の集大成。",
    development="2021-2025年でBookSumが長文要約研究の世界標準、書籍×LLM評価の中核となった。",
    historical_context="2021-2025年長文要約期。",
    primary_source_url="https://arxiv.org/abs/2105.08209",
    primary_source_type="arXiv (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("BookSumは長文要約研究の標準。")])

add(**C, name_ja="ROCStoriesベンチマーク",
    name_en="ROCStories benchmark",
    name_original="Mostafazadeh et al. 'ROCStories' (NAACL 2016)",
    definition="2016年Nasrin Mostafazadeh らのROCStories。常識的物語完成タスクの代表ベンチマークで、AI×物語理解研究の世界標準となった。",
    background="2016年物語AI研究需要、Cloze Story Completion確立。",
    development="2016-2025年でROCStoriesがAI物語研究の世界標準、LLM評価の中核ベンチマークとなった。",
    historical_context="2016-2025年ROCStories期。",
    primary_source_url="https://aclanthology.org/N16-1098/",
    primary_source_type="ACL Anthology (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("ROCStoriesはAI物語研究の世界標準。")])

add(**C, name_ja="MMLU文学サブセット",
    name_en="MMLU literature subset",
    name_original="Hendrycks et al. 'MMLU' (ICLR 2021)",
    definition="2021年Dan Hendrycksらの MMLU ベンチマーク内の文学サブセット。米国高校・大学レベルの文学知識テストで、LLM文学知識評価の世界標準となった。",
    background="2021年MMLU公開、LLM評価標準化需要。",
    development="2021-2025年でMMLUがLLM評価の世界標準、文学サブセットがAI文学知識研究の参照源となった。",
    historical_context="2021-2025年MMLU期。",
    primary_source_url="https://arxiv.org/abs/2009.03300",
    primary_source_type="arXiv (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_canon("MMLU文学サブセットはLLM文学知識評価の標準。")])


# ============================================================
# H: AI×日本文学（5件）
# ============================================================
add(**C, name_ja="一茶くんAI俳句",
    name_en="Issa-kun AI haiku project",
    name_original="北海道大学一茶くんプロジェクト（2017-）",
    definition="2017年北海道大学川村秀憲研究室のAI俳句生成プロジェクト『一茶くん』。深層学習で俳句生成を行い、AI×伝統詩の代表的日本研究として国際的注目を集めた。",
    background="2017年北大深層学習研究、AI×俳句需要。",
    development="2017-2024年で一茶くんが世界AI俳句研究の代表事例、AI×日本伝統詩の中核プロジェクトとなった。",
    historical_context="2017-2024年AI俳句期。",
    primary_source_url="https://aihaiku.github.io/",
    primary_source_type="一茶くんプロジェクト公式 (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("一茶くんはAI×日本伝統詩の代表事例。")],
    cross_domain=[cd("AI-Development","深層学習詩生成","一茶くんはAI生成詩の代表事例。")])

add(**C, name_ja="AI源氏物語英訳",
    name_en="AI Genji Monogatari translation project",
    name_original="AI源氏物語英訳プロジェクト（2020s）",
    definition="2020年代の複数機関によるAI古典日本語英訳プロジェクト。源氏物語の機械翻訳研究で、AI×日本古典の代表事例として国際DH研究で議論された。",
    background="2020年代古典日本語NLP研究の隆盛、機械翻訳需要。",
    development="2020-2025年でAI源氏物語研究が日本古典×AI翻訳の代表事例、国際DH研究の中核となった。",
    historical_context="2020-2025年古典日本語AI期。",
    primary_source_url="https://www.nii.ac.jp/research/projects/",
    primary_source_type="NII research (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("AI源氏物語研究は古典×AI翻訳の代表事例。")])

add(**C, name_ja="ELYZA日本語LLM",
    name_en="ELYZA Japanese LLM",
    name_original="ELYZA Japanese Llama 2 (2023-)",
    definition="2023年ELYZA社公開の日本語特化LLM。Llama 2ベースの ELYZA-japanese-Llama-2-7b で日本語LLM研究を主導し、日本AI×日本語処理の代表モデルとなった。",
    background="2023年ELYZA創業、日本語LLM需要の急増。",
    development="2023-2025年でELYZA LLMが日本語LLMの代表モデル、KDDI買収で日本AI企業の代表事例となった。",
    historical_context="2023-2025年日本語LLM期。",
    primary_source_url="https://elyza.ai/",
    primary_source_type="ELYZA official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("ELYZA LLMは日本語LLMの代表モデル。")])

add(**C, name_ja="Sakana AI進化的モデル",
    name_en="Sakana AI evolutionary models",
    name_original="Sakana AI Evolutionary Model Merge (2024)",
    definition="2024年David Ha・Llion Jones創業のSakana AI。進化的モデル統合手法で日本語×多言語LLMを開発し、日本発AI研究の代表事例となった東京拠点AIスタートアップ。",
    background="2024年Sakana AI創業、Google Brain出身者集結。",
    development="2024-2025年でSakana AIが日本発AI研究の代表事例、Google Brainレベルの研究を東京で展開した。",
    historical_context="2024-2025年Sakana AI期。",
    primary_source_url="https://sakana.ai/",
    primary_source_type="Sakana AI official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Sakana AIは日本発AI研究の代表事例。")])

add(**C, name_ja="青空文庫AI訓練問題",
    name_en="Aozora Bunko AI training",
    name_original="青空文庫×AI訓練データ問題（2023-）",
    definition="2023年以降の青空文庫テクストAI訓練利用問題。日本古典・近代文学の主要PDコーパスがAI訓練データとして利用され、日本AI×著作権論議の代表事例となった。",
    background="2023年AI訓練データ問題化、青空文庫の主要コーパス化。",
    development="2023-2025年で青空文庫×AI論議が日本AI法形成の代表事例、PD×AI訓練の中核議論となった。",
    historical_context="2023-2025年青空文庫AI期。",
    primary_source_url="https://www.aozora.gr.jp/",
    primary_source_type="青空文庫公式 (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("青空文庫AI論議は日本PD×AI訓練の代表事例。")])


# ============================================================
# I: AI×非西欧文学（5件）
# ============================================================
add(**C, name_ja="AI4Bharat IndicLLM",
    name_en="AI4Bharat IndicLLM",
    name_original="AI4Bharat IndicTrans2, IndicLLM (IIT Madras 2023-)",
    definition="2023年IIT Madras × Nilekaniセンターの AI4Bharat プロジェクト。22インド公式言語のLLM・翻訳モデル開発で、非西欧×多言語AI研究の代表事例となった。",
    background="2020年代インドAI政策推進、Nilekani寄付による研究基盤確立。",
    development="2023-2025年でAI4Bharatがインド多言語AIの世界代表事例、非西欧多言語AI研究の中核となった。",
    historical_context="2023-2025年インドAI期。",
    primary_source_url="https://ai4bharat.org/",
    primary_source_type="AI4Bharat official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("AI4Bharatはインド多言語AIの代表事例。"),
                 fa_canon("AI4Bharatは非西欧多言語AI研究の中核。")],
    cross_domain=[cd("AI-Development","多言語LLM","AI4Bharatは多言語AI研究の代表事例。")])

add(**C, name_ja="Aya Cohere多言語",
    name_en="Aya Cohere multilingual",
    name_original="Cohere For AI 'Aya' multilingual project (2024)",
    definition="2024年Cohere For AI 公開のAya多言語モデル。119言語対応の多言語LLMで、3,000人世界研究者が参与する代表的グローバル多言語AI研究プロジェクトとなった。",
    background="2024年Cohere AI推進、多言語AI需要の急増。",
    development="2024-2025年でAyaがグローバル多言語AIの代表事例、世界協働AI研究の中核となった。",
    historical_context="2024-2025年Aya期。",
    primary_source_url="https://cohere.com/research/aya",
    primary_source_type="Cohere For AI (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Ayaはグローバル多言語AIの代表事例。")])

add(**C, name_ja="Jais Falcon Arabic LLM",
    name_en="Arabic Jais and Falcon Arabic",
    name_original="G42 Jais (2023) / TII Falcon Arabic (2024)",
    definition="2023年UAE G42×Cerebras公開のJaisアラビア語LLMと2024年TII Falcon Arabic。アラビア語LLM研究の代表事例で、湾岸諸国主導の非西欧AI研究の中核となった。",
    background="2023-2024年湾岸AI政策推進、アラビア語AI需要。",
    development="2023-2025年でJais・Falcon Arabicがアラビア語LLMの代表事例、湾岸×AI研究の中核となった。",
    historical_context="2023-2025年湾岸AI期。",
    primary_source_url="https://huggingface.co/inceptionai/jais-13b",
    primary_source_type="Hugging Face (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Jais・Falcon Arabicはアラビア語LLMの代表事例。")])

add(**C, name_ja="HyperCLOVA韓国語",
    name_en="HyperCLOVA Korean LLM",
    name_original="Naver HyperCLOVA / HyperCLOVA X (2021-)",
    definition="2021年Naver公開のHyperCLOVA。韓国語特化LLMで、2023年HyperCLOVA Xに進化し韓国語×AI研究の代表事例となった東アジア主導LLMプロジェクト。",
    background="2021年Naver AI推進、韓国語LLM需要の浮上。",
    development="2021-2025年でHyperCLOVAが韓国語LLMの代表事例、東アジアAI研究の中核となった。",
    historical_context="2021-2025年HyperCLOVA期。",
    primary_source_url="https://clova.ai/hyperclova",
    primary_source_type="Naver CLOVA (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("HyperCLOVAは韓国語LLMの代表事例。")])

add(**C, name_ja="Wenxin Qwen中国語LLM",
    name_en="Chinese Wenxin and Qwen LLM",
    name_original="Baidu 文心 / Alibaba 通义千问 (2023-)",
    definition="2023年Baidu文心一言・Alibaba通義千問の中国語LLM群。中国生成AI規制下で発展し、中国語×AI研究の代表事例として世界AI市場を二極化した。",
    background="2023年中国AI政策推進、中国語LLM需要の急増。",
    development="2023-2025年で中国LLMが世界AI市場を二極化、Qwenオープンソース化で世界AI研究に影響した。",
    historical_context="2023-2025年中国LLM期。",
    primary_source_url="https://qwenlm.github.io/",
    primary_source_type="Qwen GitHub (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("中国LLMは世界AI市場二極化の代表事例。")])


# ============================================================
# J: 倫理・公正・著作者性論争（10件）
# ============================================================
add(**C, name_ja="Buolamwini Algorithmic Justice",
    name_en="Joy Buolamwini Algorithmic Justice League",
    name_original="Joy Buolamwini Algorithmic Justice League (2016-)",
    definition="2016年MIT Media Lab Joy Buolamwini設立のAlgorithmic Justice League。Gender Shades監査・コーディング詩で AI公正性運動を主導した代表的AI批判活動家・組織。",
    background="2016年Buolamwini顔認識バイアス研究の集大成。",
    development="2016-2025年でAJLがAI公正性運動の世界中核、書籍・映画・詩で社会×AI批評を展開した。",
    historical_context="2016-2025年AI公正性運動期。",
    primary_source_url="https://www.ajl.org/",
    primary_source_type="AJL official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("AJLはAI公正性運動の世界中核。")],
    cross_domain=[cd("AI-Development","AI倫理","AJLはAI倫理運動の代表組織。")])

add(**C, name_ja="DAIRゲブル研究所",
    name_en="Gebru Distributed AI Research",
    name_original="Distributed AI Research Institute (DAIR, 2021-)",
    definition="2021年Timnit Gebru創設のDistributed AI Research Institute。Google解雇後の独立研究機関として、AI倫理・労働・植民地主義批判の代表的研究組織となった。",
    background="2020年Gebru解雇事件、独立研究機関設立需要。",
    development="2021-2025年でDAIRがAI倫理研究の世界中核、グローバル多元的AI批判の代表機関となった。",
    historical_context="2021-2025年DAIR期。",
    primary_source_url="https://www.dair-institute.org/",
    primary_source_type="DAIR official (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("DAIRはAI倫理研究の世界中核。")])

add(**C, name_ja="Mitchell Model Cards詳細",
    name_en="Margaret Mitchell model cards detail",
    name_original="Mitchell et al. 'Model Cards for Model Reporting' (FAT* 2019)",
    definition="2019年Margaret MitchellらのFAT*論文。AIモデルの倫理的文書化標準『Model Cards』を提唱し、AI透明性研究の世界標準を確立した代表的論考。",
    background="2019年AI透明性需要、Mitchell Google倫理研究の集大成。",
    development="2019-2025年でModel CardsがAI透明性の世界標準、Hugging Face等で標準実装された。",
    historical_context="2019-2025年Model Cards期。",
    primary_source_url="https://arxiv.org/abs/1810.03993",
    primary_source_type="arXiv (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Model CardsはAI透明性の世界標準。")])

add(**C, name_ja="Alondra Nelson AI権利章典",
    name_en="Alondra Nelson AI Bill of Rights",
    name_original="Nelson et al. 'Blueprint for an AI Bill of Rights' (OSTP 2022)",
    definition="2022年Alondra Nelson主導の米OSTP公開『AI Bill of Rights青写真』。AI×市民権の代表政策文書として、世界AI政策論議に影響した。",
    background="2022年Biden政権AI政策推進、Nelson OSTP副長官時代。",
    development="2022-2025年でAI Bill of Rightsが米AI政策の中心枠組み、世界AI×市民権論議の中核となった。",
    historical_context="2022-2025年AI権利期。",
    primary_source_url="https://www.whitehouse.gov/ostp/ai-bill-of-rights/",
    primary_source_type="White House OSTP (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("AI Bill of RightsはAI×市民権の代表政策文書。")])

add(**C, name_ja="DiResta AI偽情報",
    name_en="DiResta AI/disinformation",
    name_original="Renée DiResta 'Invisible Rulers' (2024)",
    definition="2024年Stanford Internet Observatory元代表Renée DiResta著『Invisible Rulers』。AI×偽情報研究の代表書籍として世界AI批判言説を主導した。",
    background="2024年DiResta SIO退職、AI×偽情報問題の深刻化。",
    development="2024-2025年でDiResta書籍がAI×偽情報研究の標準引用、世界AI批判の中核となった。",
    historical_context="2024-2025年AI偽情報期。",
    primary_source_url="https://reneediresta.com/",
    primary_source_type="DiResta official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_auth("DiResta研究はAI×偽情報研究の代表事例。")])

add(**C, name_ja="Crawford Atlas of AI",
    name_en="Crawford Anatomy of AI System",
    name_original="Kate Crawford 'Atlas of AI' (Yale UP 2021)",
    definition="2021年Kate Crawford著『Atlas of AI』。AIの物質的・労働的・地政学的基盤を解剖した代表的批判書として、AI批判言説の中核文献となった。",
    background="2018年Anatomy of AI System視覚化、書籍化準備。",
    development="2021-2025年でCrawford書籍がAI批判言説の世界標準、AI×政治経済研究の中核となった。",
    historical_context="2021-2025年Crawford批判期。",
    primary_source_url="https://yalebooks.yale.edu/book/9780300264630/atlas-of-ai/",
    primary_source_type="Yale UP (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Crawford Atlas of AIはAI批判言説の中核文献。")],
    cross_domain=[cd("PHIL","技術哲学","Crawford研究はAI技術哲学の代表書籍。")])

add(**C, name_ja="Marietje Schaake AI政策",
    name_en="Marietje Schaake AI policy",
    name_original="Marietje Schaake 'The Tech Coup' (Princeton UP 2024)",
    definition="2024年元欧州議員Marietje Schaake著『The Tech Coup』。AI×民主主義論議の代表書籍として、AI企業統治の批判言説を主導した。",
    background="2024年Schaake Stanford Cyber Policy Center退職、書籍出版。",
    development="2024-2025年でSchaake書籍がAI×民主主義論議の標準引用、世界AI政策論議の中核となった。",
    historical_context="2024-2025年AI政策論議期。",
    primary_source_url="https://press.princeton.edu/books/hardcover/9780691241173/the-tech-coup",
    primary_source_type="Princeton UP (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Schaake書籍はAI×民主主義論議の代表事例。")])

add(**C, name_ja="Authors Guild AI政策",
    name_en="Authors Guild AI policy",
    name_original="Authors Guild AI Best Practices (2023-)",
    definition="2023年以降のAuthors Guild AI政策声明集。AI×契約条項標準・AI訓練opt-out要請等を発表し、米作家×AI政策の代表機関として世界規模で影響した。",
    background="2023年生成AI急成長、Authors Guild対AI政策需要。",
    development="2023-2025年でAuthors Guild政策が世界作家×AI政策の標準モデル、AI出版契約論議の中核となった。",
    historical_context="2023-2025年Authors Guild政策期。",
    primary_source_url="https://authorsguild.org/advocacy/artificial-intelligence/",
    primary_source_type="Authors Guild (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Authors Guild政策は世界作家×AI政策の標準。")])

add(**C, name_ja="Society of Authors AI",
    name_en="UK Society of Authors AI position",
    name_original="UK Society of Authors AI statement (2023-)",
    definition="2023年以降の英国Society of Authors AI政策声明。英作家×AI政策の代表機関として、欧州作家AI論議を主導した。",
    background="2023年英国生成AI論議、SoA対AI政策需要。",
    development="2023-2025年でSoA政策が英国作家×AI政策の中心、欧州作家AI論議の中核となった。",
    historical_context="2023-2025年SoA政策期。",
    primary_source_url="https://societyofauthors.org/",
    primary_source_type="Society of Authors (primary)",
    importance_score=2, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("SoA政策は英国作家×AI政策の代表事例。")])

add(**C, name_ja="JBPA日本出版AI政策",
    name_en="JBPA Japan publishers AI policy",
    name_original="日本書籍出版協会AI政策声明（2023-）",
    definition="2023年以降の日本書籍出版協会(JBPA)AI政策声明集。日本出版業×AI政策の代表機関として、日本独自の30条の4論議に対応した出版業界声明を発表した。",
    background="2023年日本生成AI急成長、出版業×AI政策需要。",
    development="2023-2025年でJBPA政策が日本出版業×AI政策の中心、日本独自AI論議の代表事例となった。",
    historical_context="2023-2025年JBPA政策期。",
    primary_source_url="https://www.jbpa.or.jp/",
    primary_source_type="JBPA official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("JBPA政策は日本出版業×AI政策の代表事例。")])


# ============================================================
# K: AI×アーカイブ・教育・即興（13件）— 残り
# ============================================================
add(**C, name_ja="Internet Archive AI",
    name_en="Internet Archive AI Initiative",
    name_original="Internet Archive AI initiatives (2023-)",
    definition="2023年以降のInternet Archive AI関連活動集成。Wayback MachineへのAI訓練利用論議、Open Library訴訟等で、アーカイブ×AIの代表事例となった。",
    background="2023年Internet Archive対Hachette判決、AI訓練利用論議。",
    development="2023-2025年でInternet ArchiveがアーカイブAI論議の世界中核、AI×アーカイブ法形成の代表事例となった。",
    historical_context="2023-2025年アーカイブAI期。",
    primary_source_url="https://archive.org/",
    primary_source_type="Internet Archive (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_canon("Internet ArchiveはアーカイブAI論議の中核。")])

add(**C, name_ja="Library of Congress AI戦略",
    name_en="Library of Congress AI strategy",
    name_original="Library of Congress AI Strategy (2024)",
    definition="2024年米議会図書館公開のAI戦略文書。世界最大の図書館によるAI×アーカイブ統合戦略として、世界図書館AI政策の代表事例となった。",
    background="2024年LoC AI政策推進、米連邦図書館戦略。",
    development="2024-2025年でLoC AI戦略が世界図書館AI政策の標準モデル、AI×公共アーカイブの代表事例となった。",
    historical_context="2024-2025年LoC AI期。",
    primary_source_url="https://www.loc.gov/programs/digital-collections/digital-strategy-2024-2028/",
    primary_source_type="LoC official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_canon("LoC AI戦略は世界図書館AI政策の標準。")])

add(**C, name_ja="Europeana AI政策",
    name_en="EU Europeana AI policy",
    name_original="Europeana AI policy framework (2023-)",
    definition="2023年以降のEuropeana AI政策枠組み。欧州5,000万件文化遺産デジタルアーカイブのAI戦略として、欧州AI×文化遺産の代表事例となった。",
    background="2023年Europeana AI推進、EU AI法×文化遺産需要。",
    development="2023-2025年でEuropeana AI政策が欧州AI×文化遺産の中核、世界文化遺産AI論議の代表事例となった。",
    historical_context="2023-2025年Europeana AI期。",
    primary_source_url="https://www.europeana.eu/en/professional/ai",
    primary_source_type="Europeana official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_canon("Europeana AI政策は欧州文化遺産AIの代表事例。")])

add(**C, name_ja="Google Books訴訟回顧",
    name_en="Google Books lawsuit retrospective",
    name_original="Authors Guild v. Google retrospective (2005-2016)",
    definition="2005-2016年Authors Guild対Google Books訴訟の回顧的研究。Fair Useでの和解が現代AI訓練データ法形成の前史として再評価された代表的法的先例。",
    background="2005年Google Books開始、2013年Fair Use判決、2016年確定。",
    development="2016-2025年でGoogle Books和解判例がAI訓練データ法の前史として再評価、回顧的研究の代表事例となった。",
    historical_context="2005-2025年Google Books期。",
    primary_source_url="https://www.publishers.org/news/authors-guild-v-google-supreme-court-denies-cert/",
    primary_source_type="AAP retrospective (primary)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[fa_authorship("Google Books判例はAI訓練データ法の前史。")])

add(**C, name_ja="HathiTrust孤児作品",
    name_en="HathiTrust orphan works",
    name_original="Authors Guild v. HathiTrust (2014)",
    definition="2014年Authors Guild対HathiTrust訴訟。孤児作品×フェアユース判決で、AI訓練データ法形成の前史として再評価された代表的判例。",
    background="2008年HathiTrust設立、2014年Fair Use判決確定。",
    development="2014-2025年でHathiTrust判例がAI訓練データ法の前史として再評価、孤児作品×AI法の代表事例となった。",
    historical_context="2014-2025年HathiTrust判例期。",
    primary_source_url="https://www.hathitrust.org/about/court-decisions/",
    primary_source_type="HathiTrust legal (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("HathiTrust判例はAI訓練データ法の前史。")])

add(**C, name_ja="Khan Academy AI教育",
    name_en="Khan Academy AI tutoring",
    name_original="Khan Academy×OpenAI partnership (2023-)",
    definition="2023年Khan Academy×OpenAI公式提携。Khanmigo・GPT-4ベース教育AI開発で、世界規模の教育AI統合の代表事例となったエドテック×AI連携。",
    background="2023年OpenAI×教育連携戦略、Khan Academy先行採用。",
    development="2023-2025年でKhanmigoが世界教育AI統合の代表事例、AI×無料教育の中核となった。",
    historical_context="2023-2025年教育AI連携期。",
    primary_source_url="https://blog.khanacademy.org/khan-labs/",
    primary_source_type="Khan Academy blog (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Khan AcademyはAI×無料教育の代表事例。")])

add(**C, name_ja="Duolingo AI統合",
    name_en="Duolingo AI integration",
    name_original="Duolingo Max with GPT-4 (2023)",
    definition="2023年Duolingo×OpenAI連携公開のDuolingo Max。GPT-4ベース言語学習AI機能で、世界規模の言語学習×AI統合の代表事例となった。",
    background="2023年Duolingo×OpenAI連携、言語学習AI需要。",
    development="2023-2025年でDuolingo MaxがAI×言語学習の代表事例、世界規模のAI教育統合を駆動した。",
    historical_context="2023-2025年Duolingo AI期。",
    primary_source_url="https://blog.duolingo.com/duolingo-max/",
    primary_source_type="Duolingo blog (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Duolingo MaxはAI×言語学習の代表事例。")])

add(**C, name_ja="ChatGPT Edu",
    name_en="OpenAI ChatGPT Edu",
    name_original="OpenAI ChatGPT Edu (2024)",
    definition="2024年OpenAI公開のChatGPT Edu。大学向け特化版ChatGPTとしてArizona State大等の世界トップ大学に普及し、高等教育×AI統合の代表事例となった。",
    background="2024年OpenAI教育市場展開、大学AI需要。",
    development="2024-2025年でChatGPT Eduが世界高等教育×AIの代表事例、大学AI統合の中核となった。",
    historical_context="2024-2025年高等教育AI期。",
    primary_source_url="https://openai.com/index/introducing-chatgpt-edu/",
    primary_source_type="OpenAI announcement (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("ChatGPT Eduは高等教育×AIの代表事例。")])

add(**C, name_ja="Stuart Russell AI教育論",
    name_en="Stuart Russell AI education",
    name_original="Stuart Russell 'Human Compatible' (2019) and AI education writings",
    definition="2019年UC Berkeley Stuart Russell著『Human Compatible』とAI×教育論。世界AI教科書著者によるAI×教育論議の代表的論考として、教育者×AI論議を主導した。",
    background="2019年Russell書籍出版、世界AI教科書改訂運動。",
    development="2019-2025年でRussell論議がAI×教育論議の中核、世界AI教育の代表的論者となった。",
    historical_context="2019-2025年Russell論議期。",
    primary_source_url="https://people.eecs.berkeley.edu/~russell/",
    primary_source_type="Russell UCB page (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Russell論はAI×教育論議の代表事例。")],
    cross_domain=[cd("AI-Development","AI教科書","Russellは世界AI教科書の著者。")])

add(**C, name_ja="Microsoft Reading Coach",
    name_en="Microsoft Reading Coach",
    name_original="Microsoft Reading Coach (2022-)",
    definition="2022年Microsoft公開のReading Coach。AIによる音読練習支援機能で、世界教育市場でAI×読書教育の代表事例となった教育AIプロダクト。",
    background="2022年Microsoft教育AI戦略、読書練習需要。",
    development="2022-2025年でReading CoachがAI×読書教育の代表事例、世界教育AI市場の中核となった。",
    historical_context="2022-2025年Reading Coach期。",
    primary_source_url="https://www.microsoft.com/en-us/education/reading-coach",
    primary_source_type="Microsoft Education (primary)",
    importance_score=2, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Reading CoachはAI×読書教育の代表事例。")])

add(**C, name_ja="Speak.io会話AI",
    name_en="Speak.io AI conversation",
    name_original="Speak app (2016-)",
    definition="2016年Speak創業のAI会話練習プラットフォーム。OpenAI出資の英会話AI として、世界規模で言語学習×会話AIの代表事例となったエドテック。",
    background="2016年Speak創業、2022年OpenAI Startup Fund出資。",
    development="2016-2025年でSpeakが会話AI×言語学習の代表事例、世界言語教育AI市場で評価された。",
    historical_context="2016-2025年Speak期。",
    primary_source_url="https://www.speak.com/",
    primary_source_type="Speak official (primary)",
    importance_score=2, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Speakは会話AI×言語学習の代表事例。")])

add(**C, name_ja="NaNoWriMo AI論争",
    name_en="NaNoWriMo livestreaming AI controversy",
    name_original="NaNoWriMo 2024 AI policy controversy",
    definition="2024年NaNoWriMo組織がAI執筆を「中立的」とした声明発表後の作家共同体離反事件。世界規模の作家×AI論議の代表事例として注目された。",
    background="2024年NaNoWriMo AI政策発表、作家共同体反発。",
    development="2024年でNaNoWriMo論争が世界作家×AI論議の代表事例、AI×創作共同体論議の中核となった。",
    historical_context="2024年NaNoWriMo論争期。",
    primary_source_url="https://nanowrimo.org/",
    primary_source_type="NaNoWriMo official (primary)",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("NaNoWriMo論争はAI×創作共同体論議の代表事例。")])

add(**C, name_ja="Edinburgh Fringe AIショー",
    name_en="Edinburgh Fringe AI shows",
    name_original="Edinburgh Fringe Festival AI shows (2023-)",
    definition="2023-2024年Edinburgh Fringe Festivalで上演されたAI即興公演群。『Improbotics』『AI: When a Robot Writes a Play』等が世界規模の即興×AIの代表事例となった。",
    background="2023年Edinburgh Fringe×AI受容、即興×AI実験隆盛。",
    development="2023-2024年でEdinburgh Fringe AIショーが世界即興×AI公演の代表事例、ライブ×AI論議の中核となった。",
    historical_context="2023-2024年Edinburgh AI期。",
    primary_source_url="https://www.edfringe.com/",
    primary_source_type="Edinburgh Fringe (primary)",
    importance_score=2, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[fa_authorship("Edinburgh Fringe AIは即興×AIの代表事例。")])


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
        print(f"[wave20-c39-add80] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave20-c39-add80] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
