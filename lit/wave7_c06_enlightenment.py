"""
LIT-DB Phase 2 — C06: Enlightenment / Western Europe (西欧啓蒙)
====================================================================
Inserts 40 canonical concepts spanning 5 categories:
  A. Major themes & ideals (8)
  B. Major author-concepts (8)
  C. Rise of the novel (8)
  D. Poetics & criticism (8)
  E. Meta-critical concepts (8)

subfield_code='lit_eu_enlightenment' (id=4), region='西欧'
Pattern: P1 (Canonical Primary Pursuit) — anchored to PD (ARTFL Project,
Project Gutenberg, Deutsches Textarchiv, Internet Archive) attestable
references; secondary tier reserved for critically established synthetic
concepts (e.g., 'Republic of Letters', 'public sphere').

This module is part of Wave 7 of the LIT-DB collection, focused on the
European Enlightenment (c.1680–1800) and pre-Romantic literary culture.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding — Enlightenment / Pre-Romantic (Western Europe)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("初期啓蒙期", "Early Enlightenment", 1680, 1730,
     "ベール、ロック、デフォー、スウィフトを中心とする初期啓蒙の理性主義と懐疑論の確立期。"),
    ("盛期啓蒙期", "High Enlightenment", 1730, 1780,
     "ヴォルテール、ディドロ、ルソー、レッシング、フィールディング、リチャードソン全盛の哲学・小説・批評の合流期。"),
    ("感性主義期", "Age of Sensibility", 1740, 1790,
     "リチャードソン、スターン、ルソー『新エロイーズ』を中心とする感性・感傷主義文学興隆期。"),
    ("後期啓蒙・前ロマン主義", "Late Enlightenment / Pre-Romantic",
     1780, 1800,
     "カント『判断力批判』、シラー、バーク『崇高と美の起源』を経て前ロマン主義美学への橋渡し期。"),
]


# ---------------------------------------------------------------
# Concept payload
# ---------------------------------------------------------------

CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


SUB = "lit_eu_enlightenment"
REG = "西欧"


# ===============================================================
# CATEGORY A — Major themes & ideals (8)
# ===============================================================

add({
    "name_ja": "理性対感情",
    "name_en": "reason vs sentiment",
    "name_original": "raison contre sentiment",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "啓蒙期文学を通底する根本的緊張で、デカルト的・ロック的合理主義が要求する理性の主権と、シャフツベリ・ハチスン・ルソーらが主張する道徳感情・共感能力との対立構造。理性の冷徹な解析と感情の温かな共感が相互補完的か、あるいは不可避に対立するかという問いが、啓蒙小説・詩・哲学を貫く動因となった。",
    "background": "デカルト『情念論』とロック『人間知性論』の理性中心主義への反動として、シャフツベリ『道徳家たち』（1709）が道徳感覚論を提起した。",
    "development": "ヒューム『人性論』、スミス『道徳感情論』を経て、ルソー『エミール』『新エロイーズ』が感情の優位を主張、ジェイン・オースティン『分別と多感』（1811）に直接結実する。",
    "historical_context": "宗教戦争後のヨーロッパが新たな道徳的基盤を理性と感情のいずれに求めるかをめぐる文化的問い。",
    "primary_source_url": "https://artfl-project.uchicago.edu/",
    "primary_source_type": "ARTFL Project — Rousseau, Diderot",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "理性と感情の二項対立は、AI が論理的推論を担い人間が感情的判断を担う現代的分業のなかで再活性化されている。",
         "related_ai_phenomenon": "AI と人間の役割分担論争（reasoning vs empathy）"},
    ],
})

add({
    "name_ja": "哲学小説",
    "name_en": "philosophical novel",
    "name_original": "roman philosophique",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "物語の枠組を借りて哲学的・社会的命題を批判的に展開する啓蒙期固有の小説形態。ヴォルテール『カンディード』『ザディーグ』、モンテスキュー『ペルシア人の手紙』、ディドロ『ラモーの甥』『運命論者ジャック』が代表で、登場人物が哲学的立場の体現者として配置され、旅・対話・寓話を通じて時代の偏見・教義を試問する。",
    "background": "リュキアノス『真実の物語』、トマス・モア『ユートピア』の伝統に、デカルト的方法論と新興小説形式を接続する試み。",
    "development": "19 世紀には消滅するが、20 世紀のサルトル『嘔吐』、カミュ『異邦人』、ボルヘス短編、クンデラに継承される。",
    "historical_context": "検閲下の啓蒙思想家が哲学論文を寓話化して流通させる必要性。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/19942",
    "primary_source_type": "Project Gutenberg — Voltaire Candide",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "命題を駆動因とする物語形式は、AI が論証と物語を同時生成する現代において再評価の対象となっている。",
         "related_ai_phenomenon": "LLM による論証的物語生成"},
        {"axis": "受容", "status": "partial",
         "rationale": "風刺と検閲回避を目的とする読者公共圏の前提は、AI 時代のアルゴリズム的検閲環境で部分的に再現される。",
         "related_ai_phenomenon": "AI コンテンツモデレーションと風刺"},
    ],
})

add({
    "name_ja": "ビルドゥング（陶冶）",
    "name_en": "Bildung",
    "name_original": "Bildung",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "後期啓蒙・前ロマン主義",
    "definition": "後期啓蒙期ドイツで結晶する人格陶冶の理念で、個人が古典・芸術・自然・社会経験との交通を通じて全人的に自己形成する過程を指す。ヘルダー『人類の歴史哲学考』、ゲーテ『ヴィルヘルム・マイスター』、フンボルト言語論を中核とし、ドイツ教養市民層 Bildungsbürgertum の自己定義原理となった。",
    "background": "ピエティスムの内面的自己形成と新人文主義のギリシア理想が融合した。",
    "development": "ビルドゥングス・ロマン（教養小説）の成立、19 世紀ドイツ大学制度（フンボルト型大学）、20 世紀人文教育全般の理論的基盤。",
    "historical_context": "プロイセン啓蒙改革と国民国家形成期の教育理念。",
    "primary_source_url": "https://www.deutschestextarchiv.de/",
    "primary_source_type": "Deutsches Textarchiv — Goethe, Herder",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "全人的自己形成の理念は、AI による技能習得短縮化と人間的成熟の意味を問い直す現代的議論のなかで再検討されている。",
         "related_ai_phenomenon": "AI 時代の人間的成熟と教育論"},
    ],
})

add({
    "name_ja": "公共圏（ハーバーマス以前）",
    "name_en": "public sphere (pre-Habermasian)",
    "name_original": "espace public / Öffentlichkeit",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "18 世紀ヨーロッパに形成された、コーヒーハウス・サロン・新聞・定期刊行物・書簡通信を通じて私人が公共的事象について理性的に議論する社会空間。ハーバーマス『公共性の構造転換』（1962）が遡及的に理論化したが、当時の同時代的概念としてはアディソン・スティール『スペクテイター』が「中流階級の道徳教育空間」として実体化した。",
    "background": "印刷市場拡大、コーヒー文化、絶対王政期宮廷文化との対抗的な俗人読者層の形成。",
    "development": "ハーバーマスによる遡及的概念化、20 世紀後半メディア論・民主主義論の理論的中核として再活性化。",
    "historical_context": "絶対王政の宮廷的代表性公共圏に対する市民的論争公共圏の形成期。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/12030",
    "primary_source_type": "Project Gutenberg — Addison & Steele Spectator",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "印刷媒体と対面議論を中心とする 18 世紀公共圏は、AI が議論参加者となるソーシャルメディア時代のなかでその基本前提が再交渉されている。",
         "related_ai_phenomenon": "AI ボットと公論形成"},
    ],
})

add({
    "name_ja": "啓蒙的コスモポリタニズム",
    "name_en": "Enlightenment cosmopolitanism",
    "name_original": "cosmopolitisme des Lumières",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "国境・宗派・身分を超えた「世界市民」の理念を文学・哲学において展開する啓蒙期の思想潮流。ヴォルテール『寛容論』、カント『永遠平和のために』、レッシング『賢者ナータン』を中核とし、文芸共和国（Republic of Letters）の越境的書簡通信が制度的基盤となった。",
    "background": "三十年戦争後の宗教的寛容論の発展と印刷文化の汎ヨーロッパ化。",
    "development": "19 世紀国民主義の興隆により後退するが、20 世紀後半の人権思想・グローバリズム論において再活性化。",
    "historical_context": "絶対王政間の文芸的・哲学的越境ネットワークが国民国家形成期に逆行的に成立した。",
    "primary_source_url": "https://artfl-project.uchicago.edu/",
    "primary_source_type": "ARTFL Project — Voltaire, Diderot",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "感性",
    "name_en": "sensibility",
    "name_original": "sensibility / sensibilité",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "感性主義期",
    "definition": "18 世紀中葉に文学・道徳哲学の中心概念となった、外的刺激・他者の苦悩・自然美に対して鋭敏に感応する精神的能力。リチャードソン『パミラ』『クラリッサ』、スターン『感傷的旅』、ルソー『新エロイーズ』が文学的範型を確立し、涙・赤面・気絶を共感能力の身体的指標として記述化した。",
    "background": "ロック『人間知性論』の感覚論とシャフツベリ・ハチスンの道徳感覚論の合流。",
    "development": "ジェイン・オースティン『分別と多感』が感性過剰を批判的に主題化、ロマン主義抒情詩への直接の連続。",
    "historical_context": "宮廷的礼節文化に対抗する中産階級的内面性の表象戦略。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/4078",
    "primary_source_type": "Project Gutenberg — Sterne Sentimental Journey",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "感傷小説",
    "name_en": "sentimental novel",
    "name_original": "roman sentimental",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "感性主義期",
    "definition": "登場人物の感情的揺動・道徳的苦悩・共感的紐帯を中心主題とし、読者の涙を誘発することを目的とする 18 世紀中葉の小説形式。リチャードソン『パミラ』（1740）『クラリッサ』（1747–48）、スターン『感傷的旅』（1768）、マッケンジー『感じやすき男』（1771）、ゲーテ『若きウェルテルの悩み』（1774）が代表で、涙・気絶・徳の試煉を反復的構造として用いる。",
    "background": "リチャードソンによる書簡形式と感性概念の小説的合流。",
    "development": "前ロマン主義抒情、19 世紀メロドラマ、家庭小説（ガスケル、ストウ）、現代の女性小説に直接連続。",
    "historical_context": "中産階級女性読者の興隆と道徳的読書文化の成立。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/6124",
    "primary_source_type": "Project Gutenberg — Goethe Werther",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "哲学的リベルティナージュ",
    "name_en": "libertinage philosophique",
    "name_original": "libertinage philosophique",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "宗教的・道徳的権威の懐疑、官能的経験の哲学的肯定、合理主義的快楽主義を結合する啓蒙期固有の知的・文学的態度。テオフィル・ド・ヴィオー、ガッサンディ系統の唯物論的快楽主義に発し、クレビヨン・フィス、ラクロ『危険な関係』、サド『ジュスティーヌ』に文学的形象を与えた。",
    "background": "17 世紀ガッサンディのエピクロス主義復興と宮廷的自由思想（libertins érudits）の融合。",
    "development": "19 世紀ボードレール、フローベール『感情教育』、20 世紀バタイユ、現代のクィア理論的読み直しへと連続。",
    "historical_context": "絶対王政後期の貴族的サロン文化と地下出版文化の交差点。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/10979",
    "primary_source_type": "Project Gutenberg — Laclos Liaisons dangereuses",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "宗教的・道徳的権威からの知的解放を媒介に主体を再定義した libertinage は、AI による道徳判断代行が問われる現代において主体の自律性問題を再活性化する。",
         "related_ai_phenomenon": "AI 倫理判断と人間的自律"},
    ],
})


# ===============================================================
# CATEGORY B — Major author-concepts (8)
# ===============================================================

add({
    "name_ja": "ヴォルテール『カンディード』",
    "name_en": "Voltaire's Candide",
    "name_original": "Candide, ou l'Optimisme",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "ヴォルテール（1694–1778）が 1759 年に匿名出版した哲学的コント。ライプニッツ＝ヴォルフ的楽観論（「最善世界論」）をリスボン地震・七年戦争・宗教迫害の現実と対峙させ、パングロス博士の楽観論を反復的に解体する。「自分の畑を耕さねばならない（Il faut cultiver notre jardin）」の結句が啓蒙的実践主義を象徴する。",
    "background": "1755 年リスボン地震とライプニッツ的神義論の信頼失墜、ヴォルテール『リスボン地震に寄せる詩』（1756）の前段。",
    "development": "ロマン主義による反復的読み替え、20 世紀のサルトル・カミュの不条理文学、現代のメタフィクションに継承。",
    "historical_context": "啓蒙期最大のベストセラーとして 18 世紀末まで全ヨーロッパで読まれた。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/19942",
    "primary_source_type": "Project Gutenberg — Voltaire Candide",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ライプニッツ批判",
         "description": "哲学 DB のライプニッツ神義論への啓蒙的批判の文学的形象として共有。"},
    ],
})

add({
    "name_ja": "ディドロ『百科全書』",
    "name_en": "Diderot's Encyclopédie",
    "name_original": "Encyclopédie, ou Dictionnaire raisonné des sciences, des arts et des métiers",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "ディドロ（1713–84）とダランベールが 1751–72 年に編纂・出版した全 28 巻（本巻 17、図版巻 11）の啓蒙の総合事典。約 7 万 2 千の記事を 150 名以上の執筆者で書き分け、知識の体系化・職人技の図解化・伝統権威への批判を通じて、啓蒙の知的プロジェクトを物質的に具現化した最大の出版企画。",
    "background": "チェンバーズ『サイクロペディア』英訳企画から発展、ベーコン的知識分類体系の継承。",
    "development": "後の百科事典伝統（ブリタニカ）、19 世紀実証主義、20 世紀ウィキペディアの理念的祖先、現代 LLM 訓練データの精神的予表。",
    "historical_context": "検閲・出版禁止令と購読者ネットワークの組合わせによる啓蒙的知の流通モデル。",
    "primary_source_url": "https://artfl-project.uchicago.edu/",
    "primary_source_type": "ARTFL Encyclopédie Project",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "知識を体系的に集積し交差参照可能にする百科全書原理は、LLM の訓練データ構造と直接の系譜関係にある。",
         "related_ai_phenomenon": "LLM 訓練コーパスとしての百科事典的知識"},
        {"axis": "正典", "status": "rethinking",
         "rationale": "「何を知識として記録するか」の選別原理は、AI が情報の正典化を担う現代において再交渉される。",
         "related_ai_phenomenon": "AI による知識正典化"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "LLM 訓練データの構造",
         "description": "百科全書の知識集積形式が LLM 訓練コーパスの精神的予表となる。"},
    ],
})

add({
    "name_ja": "ルソー『新エロイーズ』",
    "name_en": "Rousseau's Julie, ou la Nouvelle Héloïse",
    "name_original": "Julie, ou la Nouvelle Héloïse",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "感性主義期",
    "definition": "ルソー（1712–78）が 1761 年に出版した書簡体小説。中世のアベラールとエロイーズの愛を 18 世紀スイスの貴族令嬢ジュリと家庭教師サン＝プルーの恋に翻案し、自然・徳・感情・社会的義務の葛藤を描いた。18 世紀最大のベストセラーとなり、感性主義文学の頂点を画した。",
    "background": "リチャードソン『クラリッサ』の書簡形式とルソー自身の感情教育論の融合。",
    "development": "ゲーテ『ウェルテル』、スタール夫人『コリンヌ』、19 世紀全恋愛小説の感情的祖型。",
    "historical_context": "ヨーロッパ初の現象的ベストセラー（再版数 70 以上）、読者の感情的反応が同時代記録として残る。",
    "primary_source_url": "https://artfl-project.uchicago.edu/",
    "primary_source_type": "ARTFL Project — Rousseau Nouvelle Héloïse",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ルソーの自然概念",
         "description": "哲学 DB のルソー自然・自由概念と直接共有。"},
    ],
})

add({
    "name_ja": "ルソー『告白』",
    "name_en": "Rousseau's Confessions",
    "name_original": "Les Confessions",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "感性主義期",
    "definition": "ルソーが 1764–70 年に執筆し死後 1782/1789 年に出版した自伝。「私は自分自身を私が知るままに、すなわちあるがままに描く」という冒頭で、アウグスティヌス『告白』のキリスト教的伝統を世俗化・心理化し、近代自伝形式の祖型を確立した。幼少期の些末事から内面的羞恥までを率直に開示する独自の自伝原理が、後の心理学的自伝伝統を準備した。",
    "background": "アウグスティヌス・モンテーニュの伝統に、ルソー独自の真正性概念が接続。",
    "development": "ゲーテ『詩と真実』、ワーズワース『プレリュード』、現代の自伝・回想録ジャンル全般、近代精神分析の先駆。",
    "historical_context": "啓蒙期に成立する近代的個人概念の最も極端な文学的具現化。",
    "primary_source_url": "https://artfl-project.uchicago.edu/",
    "primary_source_type": "ARTFL Project — Rousseau Confessions",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "デフォー『ロビンソン・クルーソー』",
    "name_en": "Defoe's Robinson Crusoe",
    "name_original": "Robinson Crusoe",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期啓蒙期",
    "definition": "ダニエル・デフォー（c.1660–1731）が 1719 年に発表した小説で、無人島漂着者ロビンソンが理性と労働を通じて文明的環境を再構築する物語。プロテスタント的勤労倫理、植民地主義的支配、孤立的自我の形成を主題化し、近代的個人主義の文学的祖型として後世に巨大な影響を与えた（ロビンソナード）。",
    "background": "アレクサンダー・セルカーク漂流実記（1709）と清教徒精神的自伝伝統の融合。",
    "development": "ロビンソナード（『スイスのロビンソン』『無人島に生きる十六少年』『蝿の王』）として無数の派生作品を生み、19 世紀に「現代小説の祖」と再定位された。",
    "historical_context": "イギリス植民地拡張と中産階級読者層の同時的興隆。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/521",
    "primary_source_type": "Project Gutenberg — Defoe Robinson Crusoe",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "スウィフト『ガリヴァー旅行記』",
    "name_en": "Swift's Gulliver's Travels",
    "name_original": "Gulliver's Travels",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期啓蒙期",
    "definition": "ジョナサン・スウィフト（1667–1745）が 1726 年に発表した四部構成の風刺旅行記。リリパット人・ブロブディンナグ巨人・ラピュタ空中島・フウイヌム馬族の四つの異郷を通じて、人間理性・科学的探求・政治的腐敗・人間性そのものを段階的に脱中心化する。啓蒙の自己批判的反省の最も鋭利な文学的形象。",
    "background": "ルキアノス『真実の物語』の伝統と、王立協会の自然哲学への懐疑論的応答。",
    "development": "ヴォルテール『カンディード』『ミクロメガス』への直接的影響、現代ディストピア文学（オーウェル）、SF の祖型。",
    "historical_context": "アン女王時代末期のトーリ党知識人によるホイッグ的進歩主義批判。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/829",
    "primary_source_type": "Project Gutenberg — Swift Gulliver",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "レッシング『ラオコーン』",
    "name_en": "Lessing's Laokoon",
    "name_original": "Laokoon, oder Über die Grenzen der Malerei und Poesie",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "ゴットホルト・エフライム・レッシング（1729–81）が 1766 年に発表した美学論。古代彫像「ラオコーン群像」の苦痛表現を起点に、絵画（空間芸術）と詩（時間芸術）の媒体的差異を体系化し、ホラティウス『詩論』以来の ut pictura poesis 原理を批判的に再定義した。近代美学における芸術ジャンル論の基礎テクスト。",
    "background": "ヴィンケルマン『ギリシア美術模倣論』（1755）の受容と批判。",
    "development": "カント美学・ヘーゲル美学・現代の媒体特殊性論（クレメント・グリーンバーグ）に直接的影響。",
    "historical_context": "ドイツ啓蒙期における芸術理論の自立化と国民的批評の形成。",
    "primary_source_url": "https://www.deutschestextarchiv.de/lessing_laokoon_1766",
    "primary_source_type": "Deutsches Textarchiv — Lessing Laokoon",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "レッシング『ハンブルク演劇論』",
    "name_en": "Lessing's Hamburgische Dramaturgie",
    "name_original": "Hamburgische Dramaturgie",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "レッシングが 1767–69 年にハンブルク国民劇場の劇評家として執筆した 104 編の劇評・演劇論。フランス古典主義（コルネイユ・ヴォルテール）の三一致則中心の演劇論を批判し、シェイクスピアとアリストテレス『詩学』本来の解釈に依拠したドイツ国民演劇の理論的基盤を提示した。",
    "background": "ハンブルク国民劇場（1767 年設立）の劇評家としての活動。",
    "development": "ゲーテ・シラーのワイマール古典主義、ドイツ近代演劇全般、20 世紀ブレヒトの叙事的演劇論への系譜。",
    "historical_context": "ドイツ国民演劇形成期における仏文化覇権からの自立要求。",
    "primary_source_url": "https://www.deutschestextarchiv.de/lessing_dramaturgie01_1767",
    "primary_source_type": "Deutsches Textarchiv — Lessing Hamburgische Dramaturgie",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "レッシングの美学",
         "description": "哲学 DB の啓蒙美学の中核として共有。"},
    ],
})


# ===============================================================
# CATEGORY C — Rise of the novel (8)
# ===============================================================

add({
    "name_ja": "書簡体小説",
    "name_en": "epistolary novel",
    "name_original": "roman épistolaire",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "登場人物の往復書簡の連鎖によって物語を構成する 18 世紀の小説形式。リチャードソン『パミラ』『クラリッサ』、ルソー『新エロイーズ』、ラクロ『危険な関係』、ゲーテ『ウェルテル』が代表で、複数視点の同時提示、心理的内面の直接開示、時間性の細密化を可能にし、近代心理小説の前段階として決定的な役割を果たした。",
    "background": "17 世紀ポルトガル『ある尼僧の手紙』とロマン的書簡実用書（lettre galante）の融合。",
    "development": "19 世紀の心理小説（ジェイン・オースティン、スタンダール）に吸収され、20 世紀には間欠的に再活性化（ドストエフスキー『貧しき人々』）。",
    "historical_context": "中産階級的書簡文化の興隆と書簡形式の文学化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/9296",
    "primary_source_type": "Project Gutenberg — Richardson Clarissa",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ピカレスクの継続",
    "name_en": "picaresque continuation",
    "name_original": "continuación picaresca",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期啓蒙期",
    "definition": "黄金世紀スペイン由来のピカレスク（『ラサリーリョ・デ・トルメス』『グスマン・デ・アルファラチェ』）が 18 世紀英仏で批判的に継承された現象。ルサージュ『ジル・ブラース』（1715–35）、デフォー『モル・フランダース』（1722）、フィールディング『ジョナサン・ワイルド』、スモレット『ロデリック・ランダム』に発展し、社会風刺・流浪者一人称・道徳的曖昧性を保持した。",
    "background": "スペイン黄金世紀ピカレスクの仏訳普及。",
    "development": "ディケンズの社会小説、19 世紀メロドラマ、20 世紀ボルヘス・ガルシア＝マルケスのラテンアメリカ小説に間接的継承。",
    "historical_context": "都市化進行下の下層社会描写需要の興隆。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/371",
    "primary_source_type": "Project Gutenberg — Lesage Gil Blas",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "感傷小説（リチャードソン型）",
    "name_en": "sentimental novel (Richardsonian)",
    "name_original": "sentimental novel",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "感性主義期",
    "definition": "サミュエル・リチャードソン（1689–1761）が『パミラ』（1740）『クラリッサ』（1747–48）『チャールズ・グランディソン卿』（1753）で確立した特殊な感傷小説型。徳の試煉を反復構造として、書簡形式による細密な心理描写、女性主人公の道徳的試練、男性貴族による誘惑・暴力を主題化し、中産階級女性読者向けの道徳的読書文化を成立させた。",
    "background": "ピューリタン精神的自伝伝統と新興中産階級女性読者層の合流。",
    "development": "フィールディング『シャメラ』（1741）の風刺的応答、ルソー『新エロイーズ』、ゲーテ『ウェルテル』、19 世紀家庭小説（ガスケル、ストウ）の祖。",
    "historical_context": "ロンドン印刷業者リチャードソン自身の中産階級的世界観の文学的具現化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/9296",
    "primary_source_type": "Project Gutenberg — Richardson Clarissa",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "哲学的コント",
    "name_en": "philosophical conte",
    "name_original": "conte philosophique",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "ヴォルテールが完成させた啓蒙期固有の短編・中編形式で、東洋的・架空的舞台に哲学的命題を仮託して展開する寓話的物語。『ザディーグ』（1747）『カンディード』（1759）『ミクロメガス』（1752）『純朴な男（L'Ingénu）』（1767）が代表で、急速な物語転換・反復的反証・冷淡な語り口によって特徴づけられる。",
    "background": "リュキアノス的風刺対話、東洋的物語伝統（『千一夜物語』ガラン仏訳 1704–17）の啓蒙的翻案。",
    "development": "20 世紀のサルトル『壁』『嘔吐』、カミュ、ボルヘス、クンデラに哲学小説の祖型として継承。",
    "historical_context": "検閲下で哲学的命題を流通させるための形式的戦略。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/4646",
    "primary_source_type": "Project Gutenberg — Voltaire Zadig",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "哲学的命題を駆動因として急速な物語転換を生む形式は、AI 生成物語の論証的構造と親和的であり再評価される。",
         "related_ai_phenomenon": "LLM による哲学的物語生成"},
        {"axis": "受容", "status": "partial",
         "rationale": "検閲下で寓話を媒介に思想を流通させる仕組みは、AI コンテンツモデレーション環境下で部分的に類比的状況が再現される。",
         "related_ai_phenomenon": "AI モデレーション回避としての寓話化"},
    ],
})

add({
    "name_ja": "ロビンソナード",
    "name_en": "Robinsonade",
    "name_original": "Robinsonade",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期啓蒙期",
    "definition": "デフォー『ロビンソン・クルーソー』（1719）の構造（無人島漂着・サバイバル・文明再構築）を反復・変奏する 18・19 世紀の小説サブジャンル。ヨハン・ダーフィット・シュナーベル『フェルゼンブルク島』（1731）、ジャン＝ジャック・ルソーが『エミール』で青少年に推奨、ヨハン・ダーフィット・ヴィース『スイスのロビンソン』（1812）、ヴェルヌ『無人島に生きる十六少年』に発展。",
    "background": "デフォー成功による出版市場での反復的需要、啓蒙期の自然状態論との理論的連動。",
    "development": "ヴェルヌ、ゴールディング『蝿の王』（1954）、現代サバイバル文学・映画ジャンルに継続的継承。",
    "historical_context": "植民地拡張期の冒険的自我形成への文学的需要。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/3836",
    "primary_source_type": "Project Gutenberg — Wyss Swiss Family Robinson",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "教養小説の前駆",
    "name_en": "Bildungsroman precursor",
    "name_original": "Vorläufer des Bildungsromans",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "後期啓蒙・前ロマン主義",
    "definition": "ゲーテ『ヴィルヘルム・マイスターの修業時代』（1795–96）を典型的祖型とする教養小説（Bildungsroman）の啓蒙期前駆形態。ヴィーラント『アガトン物語』（1766–67）、ルソー『エミール』（1762、教育論ながら物語形式）、フィールディング『トム・ジョーンズ』（1749）の青年成長プロットを核とし、後期啓蒙期ドイツの陶冶（Bildung）理念と結合して教養小説に結晶する。",
    "background": "ピエティスムの内面的回心物語と啓蒙的教育論の合流。",
    "development": "ゲーテ『ヴィルヘルム・マイスター』、ノヴァーリス『ハインリヒ・フォン・オフタディンゲン』、19 世紀ドイツ教養小説伝統、20 世紀のジョイス『若き芸術家の肖像』。",
    "historical_context": "ドイツ語圏教養市民層の自己定義と教育理念の文学化。",
    "primary_source_url": "https://www.deutschestextarchiv.de/wieland_agathon_1766",
    "primary_source_type": "Deutsches Textarchiv — Wieland Agathon",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ゴシック小説の興起",
    "name_en": "Gothic novel emergence",
    "name_original": "Gothic novel",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "後期啓蒙・前ロマン主義",
    "definition": "ホレス・ウォルポール『オトラント城奇譚』（1764）に始まり、アン・ラドクリフ『ユードルフォの謎』（1794）、マシュー・ルイス『修道士』（1796）に展開する、中世的城・修道院・廃墟を舞台に超自然・恐怖・抑圧を主題化する 18 世紀後半小説サブジャンル。啓蒙的理性の境界外を探究することで、前ロマン主義の感性的拡張を準備した。",
    "background": "中世復興趣味（オシアン詩偽作 1760、リチャード・ハード『騎士道とロマンス論』1762）と感性主義の合流。",
    "development": "メアリー・シェリー『フランケンシュタイン』（1818）、ポー、ホーソーン、現代ホラー文学・映画の祖型。",
    "historical_context": "啓蒙的合理主義への逆張り的趣味の文学的成立。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/696",
    "primary_source_type": "Project Gutenberg — Walpole Castle of Otranto",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "リベルタン小説",
    "name_en": "libertine novel",
    "name_original": "roman libertin",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "性的征服・道徳的逸脱・社交の戦略を主題化する 18 世紀仏小説サブジャンル。クレビヨン・フィス『ソファ』（1742）、ディドロ『お喋りな宝石』（1748）、ラクロ『危険な関係』（1782）、サド『ジュスティーヌ』（1791）が代表で、書簡形式・回想録形式を駆使し、貴族的サロン文化と地下出版文化の交差点に位置する。",
    "background": "宮廷的 libertinage érudit 文化と啓蒙的快楽主義の合流。",
    "development": "19 世紀ボードレール、フローベール『感情教育』、20 世紀サド再評価（バタイユ、クロソウスキー）、現代のクィア文学的読み直しへ。",
    "historical_context": "アンシャン・レジーム末期の貴族的社交文化と検閲下の地下出版市場の交差。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/10979",
    "primary_source_type": "Project Gutenberg — Laclos Liaisons dangereuses",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY D — Poetics & criticism (8)
# ===============================================================

add({
    "name_ja": "ディドロ『俳優の逆説』",
    "name_en": "Diderot's Paradoxe sur le comédien",
    "name_original": "Paradoxe sur le comédien",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "ディドロが 1773–77 年に執筆し死後 1830 年に出版した演技論。優れた俳優は感情に支配されず冷徹な観察と計算によって演じるという「逆説」を展開し、共感的没入を演技の核とする伝統的見解を覆した。19・20 世紀演劇論（スタニスラフスキー、ブレヒト、ディドロ的疎外）の理論的源泉。",
    "background": "啓蒙的合理主義による感情過剰演劇への批判、英国俳優デヴィッド・ギャリックへの観察。",
    "development": "スタニスラフスキー・システム、ブレヒト叙事的演劇、現代の演技理論全般に基礎的影響。",
    "historical_context": "啓蒙期演劇改革と感性主義文化の同時的緊張のなかで成立。",
    "primary_source_url": "https://artfl-project.uchicago.edu/",
    "primary_source_type": "ARTFL Project — Diderot Paradoxe",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "レッシング『ラオコーン』詩と絵画",
    "name_en": "Lessing's Laocoön (poetry vs painting)",
    "name_original": "Laokoon — Grenzen der Malerei und Poesie",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "レッシング『ラオコーン』（1766）が体系化した、絵画は空間的並列の芸術であり詩は時間的継起の芸術であるとする媒体的差異論。ホラティウス『詩論』以来の ut pictura poesis 原理を媒体特殊性論の立場から批判的に再定義し、近代的芸術ジャンル論の理論的基盤を据えた。",
    "background": "ヴィンケルマン『ギリシア美術模倣論』（1755）の絵画的時間論への応答。",
    "development": "カント美学、ヘーゲル芸術哲学、20 世紀クレメント・グリーンバーグの媒体特殊性論まで継承。",
    "historical_context": "ドイツ啓蒙期美学の自立化と国民的批評の形成。",
    "primary_source_url": "https://www.deutschestextarchiv.de/lessing_laokoon_1766",
    "primary_source_type": "Deutsches Textarchiv — Lessing Laokoon",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ボワロー『詩法』の遺産",
    "name_en": "Boileau's Art Poétique legacy",
    "name_original": "L'Art Poétique",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期啓蒙期",
    "definition": "ボワロー＝デプレオ『詩法』（1674）が確立したフランス古典主義詩学規範の啓蒙期における持続的支配。「自然」と「理性」を最高基準とし、デコルム・三一致則・ジャンル階層・古典模倣を四大規範として、18 世紀末まで仏文学の規範的基盤を提供した。",
    "background": "アリストテレス『詩学』とホラティウス『詩論』の古典主義的統合。",
    "development": "ポープ『批評論』、ヴォルテール、フランス・アカデミー、19 世紀のロマン主義による批判的乗り越えを誘発。",
    "historical_context": "ルイ 14 世時代の文化的覇権と啓蒙期の規範論争の前提。",
    "primary_source_url": "https://artfl-project.uchicago.edu/",
    "primary_source_type": "ARTFL Project — Boileau Art Poétique",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ポープ『批評論』",
    "name_en": "Pope's Essay on Criticism",
    "name_original": "An Essay on Criticism",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期啓蒙期",
    "definition": "アレグザンダー・ポープ（1688–1744）が 1711 年に発表した詩形式の批評論。ホラティウス『詩論』とボワロー『詩法』の英国的統合を、英雄詩体二行連句で達成した。「過つは人の常、ゆるすは神の業（To err is human, to forgive divine）」「中途半端な学識は危険なもの（A little learning is a dangerous thing）」など多数の警句を文化的標語として残した。",
    "background": "ドライデン批評と仏古典主義詩学の英国的統合の試み。",
    "development": "ジョンソン批評、サミュエル・テイラー・コールリッジ、19 世紀英国批評伝統に基礎的影響。",
    "historical_context": "アン女王時代英文学の自己定位と古典主義の英国的受容。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/7409",
    "primary_source_type": "Project Gutenberg — Pope Essay on Criticism",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "新旧論争",
    "name_en": "Querelle des Anciens et des Modernes",
    "name_original": "Querelle des Anciens et des Modernes",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期啓蒙期",
    "definition": "1687–94 年フランス・アカデミーで爆発し 18 世紀英国（ベントリー、テンプル、スウィフト『書物の戦い』）に波及した、古典作家の絶対的権威と近代作家の同等性をめぐる文学論争。ペロー『古代人と近代人の比較』（1688）が近代擁護の綱領、ボワロー・ラ・フォンテーヌが古代擁護の代表で、近代進歩史観の文学的起源となった。",
    "background": "ルネサンス期からの「俗語の高揚」運動と古典絶対主義との潜在的緊張の表面化。",
    "development": "ルソー『学問芸術論』、フランス啓蒙の進歩主義、ハーバーマス的近代性論への遠隔的影響。",
    "historical_context": "ルイ 14 世末期文化政策の自己定義要求と俗語文化の自己肯定の交差。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/623",
    "primary_source_type": "Project Gutenberg — Swift Battle of the Books",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "バーク『崇高』",
    "name_en": "Edmund Burke's Sublime",
    "name_original": "A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "後期啓蒙・前ロマン主義",
    "definition": "エドマンド・バーク（1729–97）が 1757 年に発表した美学論で、崇高（sublime）と美（beautiful）を生理学的・心理的差異において峻別した。崇高は恐怖・暗黒・広大さ・力に由来し自己保存本能に訴え、美は小ささ・滑らかさ・優美さに由来し社会的紐帯に訴える。古典的調和美学を相対化し、ロマン主義美学を準備した。",
    "background": "ロンギノス『崇高について』再受容（ボワロー仏訳 1674）と感覚論心理学の合流。",
    "development": "カント『判断力批判』の「崇高の分析論」（1790）、ロマン主義美学（ワーズワース、フリードリヒ）、現代のリオタール『崇高と前衛』に継承。",
    "historical_context": "啓蒙的調和美学から前ロマン主義感性的拡張への移行の理論的結節点。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/15043",
    "primary_source_type": "Project Gutenberg — Burke Sublime and Beautiful",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "崇高の経験は人間的限界の認識に依拠するが、AI が無限的計算能力を示す現代において人間的崇高の地位が再検討されている。",
         "related_ai_phenomenon": "AI による崇高経験の媒介"},
        {"axis": "主体", "status": "partial",
         "rationale": "崇高経験における主体の自己保存的反応は、AI が脅威主体として現れる現代に部分的類比をもつ。",
         "related_ai_phenomenon": "AI 脅威認識の崇高的構造"},
    ],
})

add({
    "name_ja": "カント『判断力批判』",
    "name_en": "Kant's Critique of Judgment",
    "name_original": "Kritik der Urteilskraft",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "後期啓蒙・前ロマン主義",
    "definition": "イマヌエル・カント（1724–1804）が 1790 年に発表した批判哲学第三部で、美的判断と目的論的判断を体系化した。「無関心的快」「目的なき合目的性」「主観的普遍性」を美の四契機とし、崇高の分析論で量的崇高と力学的崇高を区別した。近代美学の理論的基礎テクストで、ドイツ観念論・ロマン主義・モダニズム美学の共通参照点。",
    "background": "バーク『崇高』、ヒューム『趣味基準論』、レッシング『ラオコーン』の啓蒙美学的伝統の批判的綜合。",
    "development": "シラー『人間の美的教育について』、シェリング、ヘーゲル、ハイデガー、リオタール、現代分析美学全般に基礎的影響。",
    "historical_context": "ドイツ啓蒙の哲学的頂点としての三批判書プロジェクトの完結。",
    "primary_source_url": "https://www.deutschestextarchiv.de/kant_urteilskraft_1790",
    "primary_source_type": "Deutsches Textarchiv — Kant Kritik der Urteilskraft",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "カント美学",
         "description": "哲学 DB のカント美学概念と直接共有、近代美学の基礎テクスト。"},
    ],
})

add({
    "name_ja": "シラー『素朴文学と感傷文学について』",
    "name_en": "Schiller's Naive and Sentimental Poetry",
    "name_original": "Über naive und sentimentalische Dichtung",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "後期啓蒙・前ロマン主義",
    "definition": "フリードリヒ・シラー（1759–1805）が 1795–96 年に発表した詩学論。古代詩人を自然と一体となった「素朴 naiv」、近代詩人を自然から疎外され理想を希求する「感傷 sentimentalisch」と類型化した。近代性概念の文学的自己理解の基礎テクストで、後のロマン主義・モダニズム自己定位の参照点。",
    "background": "ルソー『学問芸術論』の自然喪失論、シラー＝ゲーテの古典＝近代論争。",
    "development": "ドイツ・ロマン主義（シュレーゲル兄弟）、ヘーゲル芸術終焉論、ニーチェ『悲劇の誕生』、20 世紀近代性論の先駆。",
    "historical_context": "ワイマール古典主義における近代芸術の自己定義要求。",
    "primary_source_url": "https://www.deutschestextarchiv.de/schiller_dichtung_1795",
    "primary_source_type": "Deutsches Textarchiv — Schiller Über naive und sentimentalische Dichtung",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY E — Meta-critical concepts (8)
# ===============================================================

add({
    "name_ja": "文芸共和国",
    "name_en": "Republic of Letters",
    "name_original": "Respublica literaria",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "16–18 世紀ヨーロッパで成立した、国境・宗派・身分を超える学者・文人の越境的書簡通信ネットワーク。エラスムス時代に源流をもち、17–18 世紀のベール、ヴォルテール、ディドロ、フランクリン、ライプニッツに頂点を迎え、定期刊行物・書簡通信・学士院を物質的基盤として啓蒙的知の流通を可能にした。",
    "background": "ルネサンス人文主義の越境的書簡文化と印刷文化の合流。",
    "development": "19 世紀の国民国家化により消滅するが、20 世紀後半の Anne Goldgar・Hans Bots らの歴史学的再発見を経て、現代のグローバル学術ネットワーク論の祖型として再評価。",
    "historical_context": "絶対王政間の文芸的越境ネットワークが国民国家形成期に逆行的に機能した。",
    "primary_source_url": "https://artfl-project.uchicago.edu/",
    "primary_source_type": "ARTFL Project — Voltaire Correspondence",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "サロン文化",
    "name_en": "salons literary culture",
    "name_original": "salons littéraires",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "17–18 世紀パリを中心に成立した、貴族・上層中産階級女性の私的サロンを舞台とする文芸的・哲学的会話文化。ランブイエ侯爵夫人サロン（17 世紀前半）に源流をもち、デファン夫人、ジョフラン夫人、レスピナス嬢、ネッケル夫人らのサロンが啓蒙文芸の成立基盤となった。女性の文化的指導性、機智と礼節の融合、口承文化と印刷文化の媒介を特徴とする。",
    "background": "宮廷的礼節文化（プレシオジテ）と中産階級的文芸文化の融合。",
    "development": "フランス革命により消滅するが、19 世紀復古サロン文化、20 世紀文芸サークル、現代の文化的ネットワーク論の祖型。",
    "historical_context": "アンシャン・レジーム期女性の例外的文化的指導性の制度化。",
    "primary_source_url": "https://artfl-project.uchicago.edu/",
    "primary_source_type": "ARTFL Project — French Enlightenment Correspondence",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "サロン文化",
         "description": "人類学 DB のヨーロッパ近世社交文化研究と共有。"},
    ],
})

add({
    "name_ja": "百科全書主義",
    "name_en": "encyclopedism",
    "name_original": "encyclopédisme",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "知識の体系的・網羅的集積と相互参照可能化を文化的プロジェクトとして遂行する啓蒙期固有の知的態度。ディドロ＝ダランベール『百科全書』（1751–72）を頂点に、チェンバーズ『サイクロペディア』、ベール『歴史批評辞典』、ヨハン・ハインリヒ・ツェードラー『大全 Universal-Lexicon』が代表で、知識の世俗化・体系化・伝統権威からの解放を文化的目標とする。",
    "background": "ベーコン『学問の進歩』の知識分類体系、ライプニッツの普遍学構想、印刷市場の拡大の合流。",
    "development": "19 世紀ブリタニカ百科事典、20 世紀ウィキペディア、現代 LLM 訓練データ構造の理念的祖先。",
    "historical_context": "啓蒙の知的プロジェクトの最大の物質的具現化。",
    "primary_source_url": "https://artfl-project.uchicago.edu/",
    "primary_source_type": "ARTFL Encyclopédie Project",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "LLM 訓練コーパス",
         "description": "百科全書主義の知識体系化原理が LLM 訓練データの精神的予表となる。"},
    ],
})

add({
    "name_ja": "フィロゾーフ",
    "name_en": "philosophes",
    "name_original": "philosophes",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "18 世紀フランス啓蒙期に固有の社会的・文化的アイデンティティで、伝統的「哲学者」を超えて社会批判・公共啓蒙・進歩信仰を実践する知識人類型。ヴォルテール、ディドロ、ダランベール、コンドルセ、ドルバック、エルヴェシウスを中核とし、サロン・百科全書・地下出版を通じて公共圏に介入した。",
    "background": "イタリア・ルネサンス人文主義者と英国経験論哲学者の系譜的継承の仏特殊形態。",
    "development": "19 世紀の知識人（intellectuels、ドレフュス事件命名）、20 世紀の公共知識人類型の祖型。",
    "historical_context": "アンシャン・レジーム末期の絶対王政と公共圏の緊張のなかで成立した特殊な知識人類型。",
    "primary_source_url": "https://artfl-project.uchicago.edu/",
    "primary_source_type": "ARTFL Project — Diderot, Voltaire",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "フィロゾーフ・サロン",
         "description": "人類学 DB の啓蒙期知識人サークル研究と共有。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "フィロゾーフ",
         "description": "哲学 DB の啓蒙思想家集団概念と直接共有。"},
    ],
})

add({
    "name_ja": "ジャーナリズムの興隆",
    "name_en": "journalism rise",
    "name_original": "essor du journalisme",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期啓蒙期",
    "definition": "17 世紀末から 18 世紀にかけて成立した定期刊行物文化で、文芸・哲学・政治を公衆向けに論評する新興メディア形態。ベール『文芸共和国便り』（1684–1718）、アディソン＝スティール『スペクテイター』（1711–12）『タトラー』（1709–11）、グリム『文芸通信』（1753–73）が代表で、書籍とは異なる時間性・公共性・批評性を文芸文化に導入した。",
    "background": "印刷市場の拡大、コーヒーハウス文化、文芸共和国の通信ネットワークの合流。",
    "development": "19 世紀の新聞文化、20 世紀のメディア論、現代のデジタル・ジャーナリズムの祖型。",
    "historical_context": "公共圏の形成と書籍以外の文芸的時間性の導入。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/12030",
    "primary_source_type": "Project Gutenberg — Addison & Steele Spectator",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "推測的歴史",
    "name_en": "conjectural history",
    "name_original": "conjectural history / histoire conjecturale",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期啓蒙期",
    "definition": "実証的史料が欠如する人類社会の起源・発展段階を、合理的推測と原始民族・現存非西洋社会の観察から再構築するスコットランド啓蒙固有の歴史記述形式。アダム・スミス『道徳感情論』（1759）、ヒューム『英国史』、ファーガソン『市民社会史論』（1767）、ジョン・ミラー『階級区別の起源』、ルソー『人間不平等起源論』が代表。",
    "background": "ホッブズ・ロックの自然状態論と新世界先住民観察報告の合流。",
    "development": "コンドルセ『人間精神進歩史』、19 世紀進化論的人類学（モルガン、テイラー）、現代の文化人類学の前史。",
    "historical_context": "啓蒙の進歩史観と新世界遭遇の哲学的処理要求の交差。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/2160",
    "primary_source_type": "Project Gutenberg — Rousseau Discourse on Inequality",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "AN", "link_type": "borrowed_from",
         "target_entity_name": "進化論的人類学",
         "description": "推測的歴史が 19 世紀進化論的人類学の方法論的先駆となる。"},
    ],
})

add({
    "name_ja": "小説における徳倫理",
    "name_en": "virtue ethics in fiction",
    "name_original": "virtue ethics in fiction",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "感性主義期",
    "definition": "18 世紀小説に特有の、登場人物の徳の試煉・道徳的成長・読者への倫理的教訓を中心構造とする読書文化。リチャードソン『パミラ』『クラリッサ』、フィールディング『トム・ジョーンズ』『アメリア』が典型で、アリストテレス的徳倫理の啓蒙的世俗化を物語的に具現化する。サミュエル・ジョンソン『ラセラス』、エッジワース教育的小説に継承される。",
    "background": "アリストテレス・キリスト教的徳倫理の啓蒙的世俗化と中産階級的家庭道徳の合流。",
    "development": "ジェイン・オースティン、19 世紀ブロンテ姉妹・エリオット、現代マッキンタイア『美徳なき時代』の徳倫理復興論への系譜。",
    "historical_context": "中産階級女性読者向けの道徳的読書文化の成立。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/6593",
    "primary_source_type": "Project Gutenberg — Fielding Tom Jones",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "感情対理性論争",
    "name_en": "sentiment vs reason debate",
    "name_original": "débat sentiment contre raison",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "感性主義期",
    "definition": "啓蒙期後半に文学・哲学・道徳論を貫いた論争で、道徳判断の基礎を理性に置くか感情に置くかをめぐる。ヒューム『人性論』第三巻「理性は情念の奴隷たるべし」、シャフツベリ＝ハチスンの道徳感覚論、ルソー『エミール』が感情側、カント『実践理性批判』が理性側を代表する。文学的にはオースティン『分別と多感』が直接的形象化。",
    "background": "デカルト合理主義とロック経験論の道徳論的展開の交差。",
    "development": "19 世紀ロマン主義・功利主義の対立、20 世紀分析哲学のヒューム・カント論争として継続。",
    "historical_context": "啓蒙的合理主義から感性主義・前ロマン主義への移行の理論的結節点。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/4705",
    "primary_source_type": "Project Gutenberg — Hume Treatise of Human Nature",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ---------------------------------------------------------------
# Relations payload
# ---------------------------------------------------------------

RELATIONS: list[tuple[str, str, str, str]] = [
    ("理性対感情", "感性", "influences",
     "理性対感情論争の感情側が感性概念に結晶。"),
    ("理性対感情", "感情対理性論争", "extends",
     "感情対理性論争は理性対感情の啓蒙期後半的形態。"),
    ("理性対感情", "感傷小説", "influences",
     "感性主義文学は理性対感情論争の文学的形象化。"),
    ("哲学小説", "哲学的コント", "contains",
     "哲学的コントは哲学小説の短編形態。"),
    ("哲学小説", "ヴォルテール『カンディード』", "contains",
     "『カンディード』は哲学小説の頂点的代表。"),
    ("哲学小説", "スウィフト『ガリヴァー旅行記』", "contains",
     "『ガリヴァー旅行記』は英国側の哲学小説。"),
    ("ビルドゥング（陶冶）", "教養小説の前駆", "influences",
     "ビルドゥング理念が教養小説形式の理念的基盤。"),
    ("ビルドゥング（陶冶）", "シラー『素朴文学と感傷文学について』", "influences",
     "シラー詩学はビルドゥング理念の理論的展開。"),
    ("公共圏（ハーバーマス以前）", "ジャーナリズムの興隆", "contains",
     "定期刊行物が公共圏の物質的基盤を成す。"),
    ("公共圏（ハーバーマス以前）", "サロン文化", "contains",
     "サロン文化は公共圏の対面的形態。"),
    ("公共圏（ハーバーマス以前）", "文芸共和国", "extends",
     "文芸共和国は公共圏の越境的形態。"),
    ("啓蒙的コスモポリタニズム", "文芸共和国", "extends",
     "文芸共和国は啓蒙的コスモポリタニズムの制度的具現化。"),
    ("啓蒙的コスモポリタニズム", "ヴォルテール『カンディード』", "influences",
     "『カンディード』のヨーロッパ・南米遍歴は啓蒙的コスモポリタニズムの文学的具現。"),
    ("感性", "感傷小説", "contains",
     "感性概念が感傷小説の中心主題。"),
    ("感性", "ルソー『新エロイーズ』", "contains",
     "『新エロイーズ』は感性概念の頂点的文学化。"),
    ("感性", "ビルドゥング（陶冶）", "influences",
     "感性的成熟がビルドゥング理念の心理的基礎。"),
    ("感傷小説", "感傷小説（リチャードソン型）", "contains",
     "リチャードソン型は感傷小説の祖型。"),
    ("感傷小説", "ルソー『新エロイーズ』", "contains",
     "『新エロイーズ』は感傷小説のフランス的頂点。"),
    ("感傷小説", "書簡体小説", "extends",
     "書簡形式が感傷小説の典型的形式。"),
    ("哲学的リベルティナージュ", "リベルタン小説", "contains",
     "リベルタン小説は哲学的リベルティナージュの文学的形象。"),
    ("ヴォルテール『カンディード』", "哲学的コント", "contains",
     "『カンディード』は哲学的コントの頂点。"),
    ("ヴォルテール『カンディード』", "スウィフト『ガリヴァー旅行記』", "extends",
     "ヴォルテールはスウィフト風刺の仏的継承者。"),
    ("ディドロ『百科全書』", "百科全書主義", "contains",
     "『百科全書』は百科全書主義の頂点的具現。"),
    ("ディドロ『百科全書』", "フィロゾーフ", "contains",
     "『百科全書』はフィロゾーフ集団の共同事業。"),
    ("ディドロ『百科全書』", "文芸共和国", "extends",
     "『百科全書』は文芸共和国の協働的成果。"),
    ("ルソー『新エロイーズ』", "書簡体小説", "extends",
     "『新エロイーズ』は書簡体小説の仏的頂点。"),
    ("ルソー『新エロイーズ』", "感傷小説", "extends",
     "『新エロイーズ』は感傷小説の仏的頂点。"),
    ("ルソー『告白』", "ルソー『新エロイーズ』", "influences",
     "『告白』は『新エロイーズ』の自伝的延長。"),
    ("ルソー『告白』", "ビルドゥング（陶冶）", "influences",
     "『告白』の自己形成の物語がビルドゥング理念の前駆。"),
    ("デフォー『ロビンソン・クルーソー』", "ロビンソナード", "contains",
     "ロビンソナードは『ロビンソン・クルーソー』の派生ジャンル。"),
    ("デフォー『ロビンソン・クルーソー』", "推測的歴史", "influences",
     "ロビンソン的孤立的個人形成は推測的歴史の自然状態論と並行。"),
    ("スウィフト『ガリヴァー旅行記』", "哲学小説", "contains",
     "『ガリヴァー旅行記』は英国側の哲学小説。"),
    ("スウィフト『ガリヴァー旅行記』", "新旧論争", "influences",
     "『書物の戦い』が新旧論争の英国的形象。"),
    ("レッシング『ラオコーン』", "レッシング『ラオコーン』詩と絵画", "contains",
     "媒体特殊性論は『ラオコーン』の中心命題。"),
    ("レッシング『ラオコーン』", "カント『判断力批判』", "influences",
     "『ラオコーン』の媒体論がカント美学に基礎を提供。"),
    ("レッシング『ハンブルク演劇論』", "ディドロ『俳優の逆説』", "extends",
     "両者ともに啓蒙期演劇論の刷新を担う。"),
    ("書簡体小説", "感傷小説（リチャードソン型）", "contains",
     "リチャードソン型は書簡体小説の英国的頂点。"),
    ("書簡体小説", "リベルタン小説", "extends",
     "ラクロ『危険な関係』は書簡体形式のリベルタン的展開。"),
    ("ピカレスクの継続", "デフォー『ロビンソン・クルーソー』", "influences",
     "ピカレスク的下層描写がデフォー小説の前提。"),
    ("ピカレスクの継続", "教養小説の前駆", "influences",
     "ピカレスク的旅と成長が教養小説の物語構造的祖型。"),
    ("感傷小説（リチャードソン型）", "感性", "contains",
     "リチャードソン型感傷小説は感性の文学的形象化。"),
    ("感傷小説（リチャードソン型）", "ルソー『新エロイーズ』", "influences",
     "リチャードソン感傷小説がルソーへの直接的影響。"),
    ("哲学的コント", "ヴォルテール『カンディード』", "contains",
     "『カンディード』は哲学的コントの頂点。"),
    ("ロビンソナード", "デフォー『ロビンソン・クルーソー』", "extends",
     "ロビンソナードは『ロビンソン・クルーソー』の反復的変奏。"),
    ("教養小説の前駆", "ビルドゥング（陶冶）", "extends",
     "教養小説の前駆はビルドゥング理念の物語的具現の試み。"),
    ("ゴシック小説の興起", "感性", "extends",
     "ゴシック小説は感性の暗黒面への拡張。"),
    ("ゴシック小説の興起", "バーク『崇高』", "influences",
     "バーク的崇高がゴシック小説の美学的基盤。"),
    ("リベルタン小説", "哲学的リベルティナージュ", "contains",
     "リベルタン小説は哲学的リベルティナージュの文学的具現。"),
    ("ディドロ『俳優の逆説』", "理性対感情", "extends",
     "演技論における理性対感情の問題化。"),
    ("レッシング『ラオコーン』詩と絵画", "カント『判断力批判』", "influences",
     "媒体特殊性論がカント芸術論の前提。"),
    ("ボワロー『詩法』の遺産", "ポープ『批評論』", "influences",
     "ポープはボワロー詩学の英国的継承。"),
    ("ボワロー『詩法』の遺産", "新旧論争", "influences",
     "ボワロー古典擁護派が新旧論争の一方を代表。"),
    ("ポープ『批評論』", "ボワロー『詩法』の遺産", "extends",
     "ポープはボワロー詩学の英国的延長。"),
    ("新旧論争", "啓蒙的コスモポリタニズム", "influences",
     "新旧論争の近代擁護派が啓蒙的進歩史観の文学的起源。"),
    ("バーク『崇高』", "カント『判断力批判』", "influences",
     "バーク崇高論がカント崇高分析論の直接的源泉。"),
    ("バーク『崇高』", "ゴシック小説の興起", "influences",
     "バーク的崇高が前ロマン主義感性的拡張の理論基盤。"),
    ("カント『判断力批判』", "シラー『素朴文学と感傷文学について』", "influences",
     "カント美学がシラー詩学の哲学的基盤。"),
    ("シラー『素朴文学と感傷文学について』", "ビルドゥング（陶冶）", "influences",
     "感傷文学の自己反省性がビルドゥングの理論的展開。"),
    ("文芸共和国", "サロン文化", "contains",
     "サロン文化は文芸共和国の都市的形態。"),
    ("文芸共和国", "ジャーナリズムの興隆", "extends",
     "定期刊行物が文芸共和国の媒体的拡張。"),
    ("サロン文化", "フィロゾーフ", "contains",
     "サロン文化はフィロゾーフ集団の社交的基盤。"),
    ("百科全書主義", "ディドロ『百科全書』", "contains",
     "『百科全書』は百科全書主義の頂点的具現。"),
    ("百科全書主義", "啓蒙的コスモポリタニズム", "influences",
     "知識の越境的集積が啓蒙的コスモポリタニズムの理論基盤。"),
    ("フィロゾーフ", "サロン文化", "extends",
     "フィロゾーフはサロン文化の知的核心。"),
    ("フィロゾーフ", "ディドロ『百科全書』", "contains",
     "フィロゾーフは『百科全書』執筆者集団。"),
    ("ジャーナリズムの興隆", "公共圏（ハーバーマス以前）", "contains",
     "定期刊行物は公共圏の媒体的基盤。"),
    ("推測的歴史", "啓蒙的コスモポリタニズム", "influences",
     "推測的歴史の普遍的人類論が啓蒙的コスモポリタニズムの理論基盤。"),
    ("推測的歴史", "デフォー『ロビンソン・クルーソー』", "influences",
     "ロビンソン的個人形成が推測的歴史の自然状態論と並行。"),
    ("小説における徳倫理", "感傷小説（リチャードソン型）", "contains",
     "リチャードソン感傷小説は徳倫理小説の頂点。"),
    ("小説における徳倫理", "ピカレスクの継続", "criticizes",
     "ピカレスク的道徳的曖昧性が徳倫理小説に対立する。"),
    ("感情対理性論争", "感性", "extends",
     "感性概念が感情側の理論的基盤。"),
    ("感情対理性論争", "カント『判断力批判』", "influences",
     "カント美学は感情対理性論争の批判的綜合。"),
    ("感情対理性論争", "感傷小説", "influences",
     "感情対理性論争の文学的形象化が感傷小説。"),
    ("ヴォルテール『カンディード』", "啓蒙的コスモポリタニズム", "extends",
     "『カンディード』の越境的遍歴が啓蒙的コスモポリタニズムの文学的具現。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[wave7_c06_enlightenment] inserting {len(CONCEPTS)} concepts...")
    if len(CONCEPTS) != 40:
        print(f"  WARNING: expected 40 concepts, got {len(CONCEPTS)}")

    name_to_id: dict[str, int] = {}
    fourth_count = 0
    cd_count = 0
    relation_count = 0

    with LitDB() as db:
        # 1) Seed periods
        period_ids: dict[str, int] = {}
        for name_ja, name_en, sy, ey, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(
                name_ja=name_ja, region=REG,
                start_year=sy, end_year=ey,
                name_en=name_en, description=desc,
            )
            period_ids[name_ja] = pid
            print(f"  period: {name_ja!r} -> id={pid}")

        # 2) Insert concepts
        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            period_key = entry.pop("period_key", None)
            if period_key:
                entry["period_id"] = period_ids[period_key]

            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            name_to_id[entry["name_ja"]] = cid

            for axis_entry in fourth_axes:
                db.tag_fourth_transform(cid, **axis_entry)
                fourth_count += 1

            for cd in cross_domain:
                db.insert_cross_domain(
                    lit_entity_type="concept",
                    lit_entity_id=cid,
                    target_db=cd["target_db"],
                    link_type=cd["link_type"],
                    target_entity_id=cd.get("target_entity_id"),
                    target_entity_name=cd.get("target_entity_name"),
                    description=cd.get("description"),
                )
                cd_count += 1

        # 3) Insert relations
        for src_name, tgt_name, rtype, desc in RELATIONS:
            sid = name_to_id.get(src_name)
            tid = name_to_id.get(tgt_name)
            if not sid or not tid:
                print(f"  [warn] relation skipped: {src_name!r} -> {tgt_name!r}"
                      f" (sid={sid}, tid={tid})")
                continue
            db.insert_relation(
                source_type="concept", source_id=sid,
                target_type="concept", target_id=tid,
                relation_type=rtype,
                description=desc,
                confidence=4,
            )
            relation_count += 1

        # 4) Summary
        summary = db.progress_summary()
        print()
        print("[wave7_c06_enlightenment] inserted:")
        print(f"  concepts (total): {summary['concepts']}")
        print(f"  fourth_transform_tags (total): {summary['fourth_transform_tags']} "
              f"(this run: +{fourth_count})")
        print(f"  cross_domain (total): {summary['cross_domain']} "
              f"(this run: +{cd_count})")
        print(f"  relations (total): {summary['relations']} "
              f"(this run: +{relation_count})")

        # Subfield-4 specific count
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 4"
        ).fetchone()
        print(f"  concepts in subfield_id=4 (Enlightenment): {row['c']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
