"""LIT-DB Phase 2 Wave 12 — C38 ADD: World Lit / Translation theory (+40 concepts).

Subfield: lit_world_translation (id=23), region='理論'.
Existing 40 covers Goethe, Casanova, polysystem, etc.
This wave ADDS 40 new concepts focused on:
  A: Translation theory schools (8) — Skopos, DTS, Cultural Turn, Postcolonial,
     Feminist, Sociological, Activist, Eco-translation
  B: Specific translation approaches (8) — relay, retranslation, indirect/pivot,
     MT/AI translation, post-editing, fan translation, scanlation, fansub
  C: World-lit theoretical frames (8) — Damrosch readings, Apter Untranslatables,
     Walkowitz Born Translated, Cheah What is World Lit, Mufti Forget English,
     Helgesson/Vermeulen Institutions, Moretti world-system, Spivak planetarity
  D: Translation history & key texts (8) — Belles Infidèles, Schleiermacher 1813,
     Benjamin Aufgabe full reading, Borges on translation, Venuti Invisibility,
     comparative methodology (typological/genetic/contact)
  E: Specific traditions (8) — Buddhist sutra (Dao'an, Xuanzang), Bayt al-Hikma,
     Toledo school, Kanbun-yomikudashi, Jeromean/Cicero, Indian translation,
     Russian translation school, Latin American translation thought

Sources: Project Gutenberg, archive.org, SEP, EncyclopediaBritannica, academic
Wikipedia (en/fr/de/zh/ja), CTEXT, CBETA. Theory-heavy → mix primary (Benjamin
Aufgabe, Schleiermacher 1813, Cicero, Borges essays) + secondary academic.

Targets: fourth_transform_tags >= 18 (translation/language axes are core),
cross_domain to PT/PHIL/AN >= 12.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("比較文学形成期", "Formation of Comparative Literature", 1800, 1950, None),
    ("構造主義・記述的翻訳学期", "Structuralist & Descriptive Translation Studies",
     1950, 1990, None),
    ("世界文学・ポストコロニアル翻訳期", "World Literature & Postcolonial Translation",
     1990, 2030, None),
    ("古典・前近代翻訳伝統期", "Pre-modern Translation Traditions",
     -300, 1700,
     "ローマ期キケロから中世仏典漢訳・バグダード知恵の館・トレド翻訳学派・江戸期漢文訓読まで、近代以前の主要翻訳伝統。"),
]


GUTEN = "https://www.gutenberg.org/"
ARCHIVE = "https://archive.org/details/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
WIKI_ZH = "https://zh.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
BRITT = "https://www.britannica.com/"
CBETA = "https://cbetaonline.dila.edu.tw/"
CTEXT = "https://ctext.org/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_world_translation", region="理論",
         original_script="roman")


# ============================================================
# A: Translation theory schools (8)
# ============================================================
add(**C, name_ja="スコポス理論（フェアメーア）",
    name_en="Skopos theory (Vermeer)",
    name_original="Skopostheorie",
    period_key="構造主義・記述的翻訳学期",
    definition="ハンス・J・フェアメーアが1978年に提唱、カタリーナ・ライスとの共著『一般翻訳理論の基礎』(1984)で体系化された翻訳理論。翻訳行為の中心は原文ではなく目標テクストの「目的（Skopos）」であり、翻訳の妥当性は等価性ではなく目的達成度（adequacy）で評価されるとする機能主義パラダイム。ドイツ語圏応用翻訳学の中心理論となった。",
    background="1970年代ドイツ語圏の応用言語学・翻訳学が、ナイダ的等価性パラダイムから機能主義への転換を模索した文脈。",
    development="ノードの「翻訳指示（translation brief）」論、産業翻訳・ローカリゼーション理論の基盤となった。",
    historical_context="EC統合前夜の欧州における産業翻訳需要の急増と、応用翻訳学の制度化期。",
    primary_source_url=WIKI_EN+"Skopos_theory",
    primary_source_type="Wikipedia: Skopos theory (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"スコポス理論は翻訳目的が原文に優越するという立場。AI翻訳・ローカリゼーションでユースケースに応じて出力を最適化する設計と理論的に共振する。",
         "related_ai_phenomenon":"AI翻訳における目的別最適化"}])

add(**C, name_ja="記述的翻訳学（Holmes/Toury）",
    name_en="Descriptive Translation Studies (Holmes/Toury)",
    name_original="Descriptive Translation Studies",
    period_key="構造主義・記述的翻訳学期",
    definition="ジェイムズ・S・ホームズ「翻訳学の名と性質」(1972)が学問領域として翻訳学（Translation Studies）を制度化し、ギデオン・トゥーリ『記述翻訳学とその彼方』(1995)が体系化した実証的・記述的アプローチ。規範的「べき論」を排し、実際の翻訳現象を経験的・体系的に記述することを目指す。テルアビブ学派の中核理論。",
    background="1972年AILAコペンハーゲン会議でのホームズ提案と、1970-80年代エヴェン=ゾーハー・ポリシステム理論との連動。",
    development="バスネット&ルフェーヴル『翻訳・歴史・文化』(1990)の「文化的転回」へと発展した。",
    historical_context="1970年代末から1980年代の翻訳学の独立学問化期。",
    primary_source_url=WIKI_EN+"Descriptive_translation_studies",
    primary_source_type="Wikipedia: Descriptive Translation Studies",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"DTSの記述的・実証的アプローチは、AI翻訳の大規模コーパス分析と方法論的に共鳴し、現代翻訳学のデータ駆動的展開の理論的基盤となる。",
         "related_ai_phenomenon":"AI翻訳のコーパス基盤分析"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"記述詩学・実証的方法論",
         "description":"DTSは規範批判から記述へという20世紀人文学全般の方法論的転換を翻訳学で実現した。"}])

add(**C, name_ja="文化的転回（Bassnett/Lefevere）",
    name_en="Cultural Turn (Bassnett & Lefevere)",
    name_original="Cultural Turn in Translation Studies",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="スーザン・バスネットとアンドレ・ルフェーヴル編『翻訳・歴史・文化』(1990)が宣言した翻訳学のパラダイム転換。翻訳を言語的等価性ではなく文化間交渉・書き換え（rewriting）・パトロネージとして捉え直し、イデオロギー・権力・規範を中心に置く。ルフェーヴル『翻訳・書き換え・文学的名声の操作』(1992)が代表的著作。",
    background="ポリシステム理論、フーコー的権力分析、カルチュラル・スタディーズの翻訳学への合流。",
    development="ポストコロニアル翻訳論、フェミニスト翻訳論、社会学的翻訳学の理論的母体となった。",
    historical_context="冷戦終結後の文化研究的展開と、英語圏翻訳学の主流化期。",
    primary_source_url=WIKI_EN+"Translation_studies#Cultural_translation",
    primary_source_type="Wikipedia: Translation Studies / Cultural Turn",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"文化的転回は翻訳をイデオロギー・権力交渉として捉える。AI翻訳に内在する訓練データのイデオロギー的バイアスを分析する理論的基盤。",
         "related_ai_phenomenon":"AI翻訳のイデオロギー的バイアス"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"文化人類学的翻訳論",
         "description":"文化的転回は人類学のwriting culture論議と並行的に翻訳概念を文化間交渉として再定式化した。"}])

add(**C, name_ja="ポストコロニアル翻訳（Niranjana/Spivak）",
    name_en="Postcolonial translation (Niranjana/Spivak)",
    name_original="postcolonial translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="テジャスウィニ・ニランジャーナ『場の取り戻し（Siting Translation）』(1992)とガヤトリ・C・スピヴァク「翻訳の政治学」(1993)が定式化した、翻訳を植民地権力の機構として批判的に分析する理論。英国インド統治下のサンスクリット翻訳が「東洋」表象を構築した過程の批判から、現代英語訳の権力非対称までを射程とする。",
    background="エドワード・サイード『オリエンタリズム』(1978)、サバルタン研究、ホミ・バーバ『文化の場所』(1994)。",
    development="ハリッシュ・トリヴェディ、マリア・ティモシュコ、ローレンス・ヴェヌーティの「外国化（foreignization）」論との対話を通じて発展。",
    historical_context="1990年代英語圏文学批評におけるポストコロニアル研究の制度化期。",
    primary_source_url=WIKI_EN+"Postcolonial_translation",
    primary_source_type="Wikipedia: Postcolonial Translation Studies",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ポストコロニアル翻訳論は翻訳における権力非対称を中心化する。AI翻訳がリソース豊富な英語中心に偏向する構造的問題を理論化する基礎となる。",
         "related_ai_phenomenon":"AI翻訳の英語中心バイアス"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ポストコロニアル理論",
         "description":"ポストコロニアル翻訳論はポストコロニアル哲学の言語実践論として位置づけられる。"},
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"文化的他者表象",
         "description":"植民地翻訳が「東洋」を構築した過程は人類学的他者表象批判と並行する。"}])

add(**C, name_ja="フェミニスト翻訳（Simon/von Flotow）",
    name_en="Feminist translation (Simon/von Flotow)",
    name_original="feminist translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="シェリー・サイモン『翻訳における性差（Gender in Translation）』(1996)とルイーズ・フォン・フロトウ『翻訳とジェンダー』(1997)が体系化した、ジェンダー視点からの翻訳理論。ケベックのフェミニスト作家（ニコル・ブロサール等）の英訳実践に始まり、女性翻訳者の不可視化、性差別的言語の翻訳的処理、原文「介入」戦略を理論化した。",
    background="1980年代ケベック・フェミニスト文学運動と、フェミニズム第二波の言語批判。",
    development="クィア翻訳論、トランス翻訳論、ジェンダー多様性翻訳論へと展開。",
    historical_context="1990年代北米翻訳学のフェミニズム的展開期。",
    primary_source_url=WIKI_EN+"Translation#Feminist_translation",
    primary_source_type="Wikipedia: Feminist Translation",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="社会学的翻訳学（Wolf/Pym）",
    name_en="Sociological turn (Wolf/Pym)",
    name_original="sociology of translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ミシェラ・ヴォルフ&アレクサンドラ・フカリ編『翻訳の社会学を構築する』(2007)、アンソニー・ピム『翻訳学の探究』(2010)が体系化した、翻訳行為を翻訳者・出版者・読者・制度を含む社会的場（ブルデュー的champ）として分析する理論。翻訳者ハビトゥス、翻訳市場、翻訳者ネットワーク分析を中心とする。",
    background="ピエール・ブルデュー社会学の翻訳学への移植、翻訳者の労働条件・経済的地位への関心。",
    development="翻訳者のエージェンシー研究、ボランティア翻訳・コミュニティ翻訳研究、翻訳産業研究の基盤となった。",
    historical_context="2000年代欧州翻訳学のブルデュー受容期と、翻訳産業のグローバル化。",
    primary_source_url=WIKI_EN+"Sociology_of_translation",
    primary_source_type="Wikipedia: Sociology of Translation",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ブルデュー社会学の応用",
         "description":"社会学的翻訳学はブルデュー的場・ハビトゥス概念を翻訳実践に応用した、社会科学と文学研究の橋渡し領域。"}])

add(**C, name_ja="活動家翻訳（Tymoczko）",
    name_en="Activist translation (Tymoczko)",
    name_original="activist translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="マリア・ティモシュコ『翻訳・抵抗・活動』(2010)、『翻訳学の拡張・再分節化』(2007)が定式化した、翻訳者を社会変革の能動的エージェントとして捉える理論。アイルランド独立運動期のゲール語翻訳から現代の人権翻訳・抵抗翻訳までを射程とし、翻訳者の倫理的・政治的選択を中心に置く。",
    background="ティモシュコのアイルランド古ゲール語『タン・ボー・クアルンゲ』翻訳実践と、ポストコロニアル翻訳論の発展。",
    development="モナ・ベイカー『翻訳と紛争』(2006)の物語論的アプローチ、ボランティア翻訳ネットワーク（Translators Without Borders等）研究と接続。",
    historical_context="2000年代以降の翻訳の政治化・社会運動化（NGO翻訳・市民メディア翻訳）。",
    primary_source_url=WIKI_EN+"Maria_Tymoczko",
    primary_source_type="Wikipedia: Maria Tymoczko",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エコ翻訳論（Cronin）",
    name_en="Eco-translation (Cronin)",
    name_original="eco-translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="マイケル・クローニン『翻訳と人新世（Eco-Translation）』(2017)が提唱した、翻訳を生態学的視点から再概念化する理論。言語多様性と生物多様性の並行、翻訳の物質的・エネルギー的コスト、人新世における種間翻訳の倫理を扱う。中国の胡庚申「生態翻訳学」(2008)とも独立に並行的に発展した。",
    background="2010年代の人新世論議、環境人文学の興隆、言語消滅と生物多様性危機の並行的問題化。",
    development="多種翻訳論（multispecies translation）、機械翻訳のエネルギー消費批判、デジタル翻訳の生態学的監査論へと展開中。",
    historical_context="2010年代後半の気候変動危機の文化的論議と、人文学のエコロジー的転回。",
    primary_source_url=WIKI_EN+"Eco-translatology",
    primary_source_type="Wikipedia: Eco-translatology",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"エコ翻訳論は言語多様性を生物多様性と並行的に捉える。AI翻訳が大規模言語モデル訓練のエネルギー消費・少数言語消失を加速する構造的問題の理論的基盤。",
         "related_ai_phenomenon":"AI翻訳の生態的コストと言語多様性"}])


# ============================================================
# B: Specific translation approaches (8)
# ============================================================
add(**C, name_ja="リレー翻訳",
    name_en="relay translation",
    name_original="relay translation",
    period_key="構造主義・記述的翻訳学期",
    definition="原文から第一の翻訳者が中間言語に翻訳し、別の翻訳者がその中間訳から目標言語に翻訳する二段階以上の翻訳。文学翻訳・通訳（特に多言語会議通訳）・聖典翻訳に広く見られる。マーティン・リングマー「リレー翻訳」(2007)、ピム『翻訳学の探究』(2010)が方法論的に整理した。",
    background="多言語的世界における直接翻訳者不在の構造的問題と、希少言語ペアの翻訳実務的解決。",
    development="EU多言語通訳のリレー方式、文学翻訳における重訳問題（中国文学英訳経由の日本語訳等）、機械翻訳のピボット方式へと連結。",
    historical_context="20世紀後半以降の国際機関多言語化と、希少言語文学の重訳経由グローバル化。",
    primary_source_url=WIKI_EN+"Relay_translation",
    primary_source_type="Wikipedia: Relay translation",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="再翻訳（retranslation）",
    name_en="retranslation",
    name_original="retraduction",
    period_key="構造主義・記述的翻訳学期",
    definition="同一原文の新たな翻訳行為。アントワーヌ・ベルマンの「再翻訳の時間」(1990)が古典的論文。ベルマンは初訳が「同化的・帰化的」、再訳が原文の他者性を回復する「外国化的」傾向を持つという「再翻訳仮説」を提示した。古典文学翻訳の世代的更新を理論化する中心概念となった。",
    background="ベルマン『他者の試練』のフランス古典翻訳論、フローベール・ドストエフスキー等の英訳更新史。",
    development="シャンタル・ガニエ『再翻訳のもう一つの研究』(2012)等が再翻訳仮説を実証的に検証。AI翻訳時代の自動再翻訳論議へと接続。",
    historical_context="1990年代仏語圏翻訳学の理論的展開と、英米古典文学翻訳の世代的更新（ペーヴェア&ヴォロホンスキー訳ロシア文学等）。",
    primary_source_url=WIKI_EN+"Retranslation",
    primary_source_type="Wikipedia: Retranslation",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"再翻訳仮説（初訳の同化的→再訳の外国化的傾向）は、AI自動再翻訳が世代的に出力を更新していく将来構造を理論化する基盤となる。",
         "related_ai_phenomenon":"AI翻訳の世代的更新と再翻訳仮説"}])

add(**C, name_ja="間接翻訳・ピボット翻訳",
    name_en="indirect translation / pivot translation",
    name_original="indirect translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="原文ではなく中間言語の翻訳から目標言語へ訳す方式。文学では重訳と呼ばれ、機械翻訳では英語経由の「ピボット翻訳」として実装される。アレクサンドラ・アシス・ローザ等編『間接翻訳：理論的・方法論的・歴史的考察』(2017)が体系化。",
    background="翻訳資源の非対称性（英語中心構造）と、希少言語ペアにおける直接翻訳者不在。",
    development="ニューラル機械翻訳の多言語モデル（Google Multilingual NMT 2016、M2M-100 2020）が英語中継を経由しない直接翻訳を実装し、ピボット翻訳の構造を変化させつつある。",
    historical_context="20世紀後半グローバル文学市場の英語経由構造と、機械翻訳の多言語化。",
    primary_source_url=WIKI_EN+"Indirect_translation",
    primary_source_type="Wikipedia: Indirect translation",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ピボット翻訳は機械翻訳の構造的特徴であり、英語中心ピボットから多言語直接翻訳への転換は AI翻訳の理論的中心問題。",
         "related_ai_phenomenon":"NMT多言語モデルのピボット脱却"}])

add(**C, name_ja="機械翻訳・AI翻訳の理論",
    name_en="Machine/AI translation theory",
    name_original="machine translation theory",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="統計的機械翻訳（SMT, 1990s）からニューラル機械翻訳（NMT, 2014-）、トランスフォーマーベースの大規模言語モデル翻訳（2017-）に至る計算機翻訳の理論的基盤。ドロシー・ケニー編『人間にとっての機械翻訳』(2017)、シャロン・オブライエン等の翻訳テクノロジー研究が、理論と実践の接点を整理してきた。",
    background="ウィーバー覚書(1949)以来のMT研究、Google翻訳(2006)、TransformerアーキテクチャとGPT/BERT系モデルの台頭。",
    development="ChatGPT/LLM時代の翻訳論議は、文脈理解・スタイル転写・文学翻訳の質を中心に進展中。",
    historical_context="2010年代以降のAI翻訳の質的転換と、人間翻訳者の労働条件・職業的アイデンティティの再編。",
    primary_source_url=WIKI_EN+"Machine_translation",
    primary_source_type="Wikipedia: Machine translation",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"AI翻訳は翻訳行為の物質的基盤を根本から再編した。翻訳者・原文・目標文・読者の関係構造そのものが再構築されつつある。",
         "related_ai_phenomenon":"LLMによる文学翻訳の質的飛躍"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"AI翻訳は翻訳者の作者性・著作権・倫理的責任を根本的に問い直す。",
         "related_ai_phenomenon":"AI翻訳の著作権と翻訳者の責任"}])

add(**C, name_ja="ポストエディット",
    name_en="post-editing (MT post-editing)",
    name_original="post-editing",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="機械翻訳出力を人間翻訳者が編集する翻訳実践。ライトポストエディット（最低限の修正）とフルポストエディット（出版品質）に分類される。ISO 18587(2017)が国際標準化し、シャロン・オブライエンらが認知負荷研究を進めた。AI翻訳時代の翻訳産業の中心実践となった。",
    background="2000年代統計的機械翻訳の品質向上と、翻訳産業のコスト削減圧力。",
    development="NMT・LLM時代の「AI支援翻訳」「ヒューマン・イン・ザ・ループ」へと展開。文学翻訳への適用可能性は議論中。",
    historical_context="2010年代以降の翻訳産業のテクノロジー化と、翻訳者の役割再定義期。",
    primary_source_url=WIKI_EN+"Postediting",
    primary_source_type="Wikipedia: Post-editing",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ポストエディットは人間翻訳者を「編集者」に変容させ、翻訳者の作者性・専門性・労働条件を再定義する。",
         "related_ai_phenomenon":"AI支援翻訳における人間の役割"}])

add(**C, name_ja="ファン翻訳",
    name_en="fan translation",
    name_original="fan translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ファンコミュニティが商業的回路を経由せず無償・自発的に行う翻訳実践。マンガ・アニメ・ゲーム・ライトノベル・ファンフィクションの翻訳が中心。ミニ・ラ・コマップ＆ラリッサ・ラブレ＝コルテス『ファン翻訳における新たな関係性』(2023)等が研究を体系化。",
    background="2000年代以降のインターネット普及と、日本ポップカルチャーのグローバル化、商業翻訳の遅延・不在。",
    development="プラットフォーム翻訳（Wattpad、AO3）、クラウドソーシング翻訳、AI支援ファン翻訳へと展開。",
    historical_context="グローバル・ファンコミュニティの形成と、知的財産権・著作権との緊張関係。",
    primary_source_url=WIKI_EN+"Fan_translation",
    primary_source_type="Wikipedia: Fan translation",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="スキャンレーション",
    name_en="scanlation",
    name_original="scanlation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="マンガを原本スキャン→ファン翻訳→画像合成→オンライン公開する一連のファン実践。1990年代の英語マンガファンコミュニティに起源を持ち、2000年代以降のマンガグローバル化を駆動した。スキャンレーション・グループの分業・倫理規範・商業出版との緊張関係をめぐる研究が蓄積。",
    background="日本マンガの英語翻訳遅延・絶版問題と、デジタル画像処理技術の普及。",
    development="商業マンガアプリ（MangaPlus 2019）、AI翻訳マンガサービスへと展開し、スキャンレーションの位置づけが変容中。",
    historical_context="2000-10年代の日本マンガ・グローバル化と、ファン文化の制度化。",
    primary_source_url=WIKI_EN+"Scanlation",
    primary_source_type="Wikipedia: Scanlation",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ファンサブ理論",
    name_en="fansub theory",
    name_original="fansub",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="アニメ・実写映像のファン字幕翻訳実践。1980年代のVHS時代に始まり、2000年代以降ストリーミング時代に拡大。ホルヘ・ディアス・シンタス&パブロ・ムニョス・サンチェス「ファンサブ：オーディオビジュアル翻訳の代替モデル」(2006)が学術的に位置づけた。「逐語的注釈」「文化注」「タイポグラフィ的演出」など商業字幕と異なる規範を持つ。",
    background="1980年代日本アニメの北米VHSファンコミュニティ、商業字幕の不在・遅延。",
    development="ストリーミング時代の公式同時配信（クランチロール等）が変えた市場構造と、ファンサブの規範的位置の変化。",
    historical_context="グローバル映像消費の同時性化と、字幕翻訳の専門化。",
    primary_source_url=WIKI_EN+"Fansub",
    primary_source_type="Wikipedia: Fansub",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# C: World-lit theoretical frames (8)
# ============================================================
add(**C, name_ja="ダムロッシュ『世界文学の読み方』",
    name_en="Damrosch How to Read World Literature",
    name_original="How to Read World Literature",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="デイヴィッド・ダムロッシュ『世界文学の読み方』(2009、2nd ed. 2017)。世界文学を「翻訳から得られる楕円形の屈折」(elliptical refraction)として捉え、ギルガメシュ叙事詩から現代まで読解実践を提示。前著『世界文学とは何か』(2003)の理論的命題を、教育的・実践的に展開した世界文学入門の規範書。",
    background="2000年代の世界文学論の制度化と、米国大学における世界文学コースの拡大。",
    development="ダムロッシュ編『プリンストン世界文学百科事典』(2020)、ハーヴァード「文学研究所」を通じた世界文学教育の制度化。",
    historical_context="ポスト9.11期米国における比較文学の世界文学への移行期。",
    primary_source_url=WIKI_EN+"David_Damrosch",
    primary_source_type="Wikipedia: David Damrosch",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アプター『翻訳不可能なもの』",
    name_en="Apter Against World Literature: On the Politics of Untranslatability",
    name_original="Against World Literature",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="エミリー・アプター『世界文学に抗して：翻訳不可能性の政治学』(2013)。バーバラ・カサン編『欧州哲学語彙集（Vocabulaire européen des philosophies）』(2004)を英訳した経験から、世界文学言説の英語中心性・翻訳前提を批判し、翻訳不可能性（untranslatables）を文学的・哲学的概念として理論化した。",
    background="2010年代世界文学論への批判的応答と、欧州哲学語彙集の英訳プロジェクト。",
    development="ダムロッシュ的世界文学論議への対抗的立場として、世界文学論争の中心的論点を提示。",
    historical_context="2010年代英語圏比較文学のグローバル化批判期。",
    primary_source_url=WIKI_EN+"Emily_Apter",
    primary_source_type="Wikipedia: Emily Apter",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"翻訳不可能性は AI翻訳が「すべてを訳せる」と前提することへの根本的批判。LLM時代の翻訳論の中心論点。",
         "related_ai_phenomenon":"LLMの翻訳前提と翻訳不可能性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"翻訳不可能性・哲学的語彙",
         "description":"アプターの議論はカサン哲学語彙集の翻訳実践に基づき、哲学的概念の翻訳不可能性を中心化する。"}])

add(**C, name_ja="ウォルコウィッツ『翻訳のために生まれた』",
    name_en="Walkowitz Born Translated",
    name_original="Born Translated",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="レベッカ・L・ウォルコウィッツ『翻訳のために生まれた：現代小説の世界文学的形式』(2015)が提唱した概念。グローバル流通を前提に書かれる現代小説（J.M.クッツェー、村上春樹、カズオ・イシグロ等）を、原語と翻訳の境界を曖昧化する「翻訳的形式」として分析。世界文学の生産的位相を理論化した。",
    background="2000年代以降のグローバル文学市場の制度化と、英語圏作家の世界文学的自意識。",
    development="ジン・ツァン『シノフォン世界文学』、シャオロウ・ヤン等の言語横断的世界文学論と接続。",
    historical_context="2010年代世界文学論の生産論的展開期。",
    primary_source_url=WIKI_EN+"Rebecca_Walkowitz",
    primary_source_type="Wikipedia: Rebecca Walkowitz",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"「翻訳のために生まれた」作品概念は、AI翻訳前提で書かれる将来の文学への理論的伏線として再読可能。",
         "related_ai_phenomenon":"AI翻訳前提の文学創作"}])

add(**C, name_ja="チア『世界文学とは何か』",
    name_en="Cheah What Is a World",
    name_original="What Is a World? On Postcolonial Literature as World Literature",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ペン・チア『世界とは何か：世界文学としてのポストコロニアル文学』(2016)。ハイデガー・デリダの世界概念哲学を踏まえ、世界文学を市場流通ではなく「世界化（worlding）の規範的・倫理的力」として再概念化。グローバル資本に対抗する世界文学の解放的可能性を理論化した。",
    background="ポストコロニアル理論、現象学的世界概念、グローバル資本主義批判の合流。",
    development="マッダレナ・パラディ等の批判的世界文学論、エコクリティシズムとの対話を通じて発展。",
    historical_context="2010年代後半世界文学論の規範的・倫理的転回期。",
    primary_source_url=WIKI_EN+"World_literature#Theoretical_debates",
    primary_source_type="Wikipedia: World literature / theoretical debates",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ハイデガー世界概念",
         "description":"チアの世界文学論はハイデガー『存在と時間』の世界概念を文学理論に応用したもの。"}])

add(**C, name_ja="ムフティ『英語を忘れよ』",
    name_en="Mufti Forget English!",
    name_original="Forget English! Orientalisms and World Literatures",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="アーミル・R・ムフティ『英語を忘れよ：オリエンタリズムと世界文学』(2016)。世界文学の英語中心構造を、ヨーロッパ・オリエンタリズムが東洋文学を「翻訳可能な他者」として制作した歴史的過程に遡って批判。19世紀ドイツ・インド学から現代南アジア英語文学までを射程とする。",
    background="サイード『オリエンタリズム』(1978)の世界文学論への適用、南アジア英語文学の世界文学化への批判。",
    development="ジェイミー・スター、ガヤトリ・スピヴァク等のポストコロニアル比較文学論と接続。",
    historical_context="2010年代後半グローバル英語批判と、世界文学のオリエンタリズム的構造の問題化期。",
    primary_source_url=WIKI_EN+"Aamir_Mufti",
    primary_source_type="Wikipedia: Aamir Mufti",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"英語中心主義批判は、AI翻訳・LLMが英語中心訓練データに依存する構造的問題と直結する。",
         "related_ai_phenomenon":"LLMの英語中心訓練データバイアス"}])

add(**C, name_ja="ヘルゲソン&ヴァーミューレン『世界文学の制度』",
    name_en="Helgesson & Vermeulen Institutions of World Literature",
    name_original="Institutions of World Literature",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ステファン・ヘルゲソン&ピーター・ヴァーミューレン編『世界文学の制度：文学市場・翻訳・批評』(2015)。世界文学を抽象的範疇ではなく具体的制度（出版社・翻訳助成・文学賞・大学・批評誌）の集合として分析する社会学的世界文学論を体系化した論集。",
    background="カサノヴァ『文学の世界共和国』の制度論的展開と、ブルデュー社会学の文学研究への適用。",
    development="文学賞研究（ノーベル賞・ブッカー賞）、翻訳助成研究、文学エージェント研究へと展開。",
    historical_context="2010年代世界文学論の制度社会学的転回期。",
    primary_source_url=WIKI_EN+"World_literature",
    primary_source_type="Wikipedia: World literature (institutions)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="モレッティ世界システム論",
    name_en="Moretti's world-systems literary theory",
    name_original="world-systems literary theory",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="フランコ・モレッティ「世界文学への試論」(2000)、『近代叙事詩』(1996)が、ウォーラーステインの世界システム論を文学に適用した理論。世界文学を中心・準周縁・周縁の不平等な階層構造として把握し、形式の伝播を中心から周縁への単方向的流動として説明する仮説を提示した。",
    background="ウォーラーステイン世界システム分析、エヴェン=ゾーハー・ポリシステム理論の世界規模化。",
    development="エミリー・アプター、ペンドルトン的批判（中心-周縁モデルの単純化批判）と論争を引き起こした。",
    historical_context="2000年代世界文学論の社会学的・量的転回期。",
    primary_source_url=WIKI_EN+"Franco_Moretti",
    primary_source_type="Wikipedia: Franco Moretti",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="スピヴァク惑星性",
    name_en="Spivak's planetarity",
    name_original="planetarity",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ガヤトリ・C・スピヴァク『学問領域の死』(2003)で提唱された概念。グローバリゼーションが世界を均質的「グローブ」として把握するのに対し、不可知の他者性を含意する「惑星（planet）」概念を対置する。世界文学・比較文学の倫理的・哲学的基盤として、グローバル資本主義言説への批判的代替を提供する。",
    background="ハイデガー的世界概念、デリダ的他者性、ポストコロニアル理論の総合。",
    development="ペン・チア『世界とは何か』(2016)等の世界文学倫理論議の中心参照点となった。",
    historical_context="ポスト9.11期米国比較文学の倫理的転回期。",
    primary_source_url=WIKI_EN+"Gayatri_Chakravorty_Spivak",
    primary_source_type="Wikipedia: Gayatri Spivak",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"惑星性・他者性の哲学",
         "description":"スピヴァクの惑星性概念はデリダ・レヴィナス的他者性の哲学を文学理論に展開した。"}])


# ============================================================
# D: Translation history & key texts (8)
# ============================================================
add(**C, name_ja="美しい不実な翻訳（Belles Infidèles）",
    name_en="Belles Infidèles",
    name_original="Belles Infidèles",
    period_key="古典・前近代翻訳伝統期",
    definition="17世紀フランス、ニコラ・ペロ・ダブランクール（1606-64）らによるギリシャ・ラテン古典の意訳的翻訳様式。「美しいが不実」とのジル・メナージュの揶揄に由来する命名。原文を当時のフランス語的優雅さに同化させる「帰化的翻訳」の歴史的範例として、後のヴェヌーティ「外国化／帰化」論議の歴史的前提となった。",
    background="17世紀フランス古典主義の言語規範主義、サロン文化、フランス語の古典としての確立論議。",
    development="シュライアマハー1813年講演における「読者を著者へ」型翻訳の歴史的範例として位置づけられた。",
    historical_context="ルイ14世期フランス絶対王政期の言語規範化と、古典の国民文学化過程。",
    primary_source_url=WIKI_FR+"Belles_infid%C3%A8les",
    primary_source_type="Wikipedia (FR): Belles infidèles",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="シュライアマハー1813年講演",
    name_en="Schleiermacher 1813 lecture On the Different Methods of Translating",
    name_original="Über die verschiedenen Methoden des Übersetzens",
    period_key="比較文学形成期",
    definition="フリードリヒ・シュライアマハー（1768-1834）が1813年6月24日にベルリン王立科学アカデミーで行った講演。「翻訳者は読者を著者の元へ向かわせるか、著者を読者の元へ向かわせるか」の二者択一を定式化し、近代翻訳理論の基本対立軸を確立した。ヴェヌーティ「外国化／帰化」論の直接の歴史的源流。",
    background="ナポレオン戦争期ベルリンの民族文学論議、ヘルダー言語哲学、ロマン派翻訳論（A.W.シュレーゲル等）の文脈。",
    development="アントワーヌ・ベルマン『他者の試練』(1984)、ヴェヌーティ『翻訳者の不可視性』(1995)の理論的中心参照点となった。",
    historical_context="プロイセン国民国家形成期の言語ナショナリズムと、翻訳の哲学的位置づけ。",
    primary_source_url=ARCHIVE+"smtlichewerkeau03schluoft",
    primary_source_type="archive.org: Schleiermacher Sämtliche Werke",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"シュライアマハー二者択一は AI翻訳における「自然な目標言語化」vs「原文の他者性保持」の設計選択と直接共鳴する。",
         "related_ai_phenomenon":"AI翻訳の同化的vs外国化的設計"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"シュライアマハー解釈学",
         "description":"シュライアマハーは近代解釈学の創始者であり、翻訳論はその解釈学的言語哲学の応用。"}])

add(**C, name_ja="ベンヤミン「翻訳者の使命」精読",
    name_en="Benjamin's Die Aufgabe des Übersetzers — close reading",
    name_original="Die Aufgabe des Übersetzers",
    period_key="比較文学形成期",
    definition="ヴァルター・ベンヤミン『翻訳者の使命』(1923、ボードレール『パリ風景』独訳序文)の理論的読解。ベンヤミンは翻訳を原文への「忠実」ではなく、純粋言語（reine Sprache）の彼方への暗示として理論化。デリダ『バベルの塔』(1985)、ポール・ド・マン「ベンヤミン『翻訳者の使命』論」(1985)が脱構築的に再読し、20世紀後半翻訳論の哲学的中核となった。",
    background="ベンヤミンのカバラ的言語神学、ボードレール翻訳実践、ロマン派翻訳論（ヘルダリン・ピンダロス訳）の継承。",
    development="デリダ・ド・マンの読解は20世紀後半翻訳論を哲学的・脱構築的水準で更新した。",
    historical_context="ヴァイマル期ドイツ知識人の翻訳実践と、近代翻訳論の哲学化。",
    primary_source_url=ARCHIVE+"benjamin-walter-die-aufgabe-des-uebersetzers",
    primary_source_type="archive.org: Benjamin Aufgabe (German original)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ベンヤミンの「純粋言語」概念は AI翻訳が示唆する「言語間共通の意味空間」（多言語埋め込み空間）と理論的に響き合い、再読が進む。",
         "related_ai_phenomenon":"多言語埋め込み空間と純粋言語"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ベンヤミン言語哲学",
         "description":"ベンヤミン翻訳論は彼のカバラ的言語神学（『言語一般について、また人間の言語について』1916）の応用。"},
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"翻訳の詩学",
         "description":"ベンヤミン翻訳論は20世紀詩学の哲学的中心テクストの一つ。"}])

add(**C, name_ja="ボルヘス翻訳論",
    name_en="Borges on translation",
    name_original="Borges sobre la traducción",
    period_key="比較文学形成期",
    definition="ホルヘ・ルイス・ボルヘス「ホメロス翻訳について」(1932)、「『千一夜物語』翻訳者たち」(1936)、「ウォーリー版『源氏物語』」(1938)等のエッセイ群。原文と翻訳の階層を逆転させ、翻訳を独立した文学的営為として位置づける独自の翻訳論。「原文は翻訳に対して不忠実である」のパラドックスで知られる。",
    background="ブエノスアイレス文学雑誌『スール』活動期、20世紀ラテンアメリカ文学のヨーロッパ翻訳経由受容の自己反省。",
    development="エフライン・クリスタル『翻訳者ボルヘス』(2002)等が体系化。スザンヌ・ジル・レヴィン等のラテンアメリカ翻訳論に継承された。",
    historical_context="20世紀前半ラテンアメリカの世界文学的自意識と、翻訳実践の文学化。",
    primary_source_url=WIKI_EN+"Jorge_Luis_Borges#Translation",
    primary_source_type="Wikipedia: Borges and translation",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヴェヌーティ『翻訳者の不可視性』精読",
    name_en="Venuti Translator's Invisibility — close reading",
    name_original="The Translator's Invisibility",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ローレンス・ヴェヌーティ『翻訳者の不可視性：翻訳の歴史』(1995、2nd ed. 2008)。シュライアマハー1813年講演を理論的中軸に、英語圏翻訳市場における「流暢な翻訳」規範が翻訳者を不可視化する政治構造を批判。「外国化（foreignization）」を抵抗的翻訳実践として提唱した。20世紀末翻訳論の中心テクスト。",
    background="ベルマン『他者の試練』のフランス翻訳論伝統、英語圏翻訳市場の英米中心主義批判。",
    development="ベイカー、ティモシュコ、ピムらとの論争を通じて、21世紀翻訳論の主要論点を形成。",
    historical_context="1990年代英語圏翻訳学の批判的・政治的転回期。",
    primary_source_url=WIKI_EN+"Lawrence_Venuti",
    primary_source_type="Wikipedia: Lawrence Venuti",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"翻訳者の不可視性論は、AI翻訳における「翻訳者の消失」を歴史的・構造的に位置づけ直す批判的枠組みを提供する。",
         "related_ai_phenomenon":"AI翻訳における翻訳者主体の消失"}])

add(**C, name_ja="類型論的vs系譜論的比較",
    name_en="typological vs genetic comparison",
    name_original="typological vs genetic comparison",
    period_key="比較文学形成期",
    definition="比較文学の方法論的二類型。系譜論的（genetic）比較は歴史的影響関係に基づく比較（仏派の影響研究）、類型論的（typological）比較は歴史的接触のない並行的類似に基づく比較（米派の並行研究）。ヴィクトル・ジルムンスキー『歴史比較文学論』(1979)、ディオニス・デュリシン『比較文学的研究』(1984)が体系化した東欧比較文学方法論。",
    background="エティアンブル『比較文学反論』(1963)以降の比較文学方法論論争、東欧マルクス主義比較文学の伝統。",
    development="現代比較文学の量的方法論（モレッティ）、世界文学論議における方法論的反省の基盤。",
    historical_context="20世紀後半東欧・ソ連比較文学の理論的成熟期。",
    primary_source_url=WIKI_EN+"Comparative_literature#Methodology",
    primary_source_type="Wikipedia: Comparative literature methodology",
    importance_score=4, source_tier="tertiary", canonical_in_region="major")

add(**C, name_ja="接触関係（contact relations）",
    name_en="contact relations in comparative literature",
    name_original="contact relations",
    period_key="比較文学形成期",
    definition="デュリシン比較文学方法論の中核概念。文学現象間の関係を「接触なし型類似（typological affinities）」と「接触あり型関係（contact relations）」に区別し、後者をさらに直接接触・媒介接触に細分する分析枠組み。スロヴァキア比較文学派の方法論的精緻化として、現代世界文学論議に継承される。",
    background="ディオニス・デュリシン（1929-97）スロヴァキア比較文学派、東欧構造主義文学論。",
    development="現代世界文学論における「文学的接触」分析（パスカル・カサノヴァ、デイヴィッド・ダムロッシュ）の方法論的源流の一つ。",
    historical_context="20世紀後半東欧比較文学の独自方法論確立期。",
    primary_source_url=WIKI_EN+"Dion%C3%BDz_%C4%8Euri%C5%A1in",
    primary_source_type="Wikipedia: Dionýz Ďurišin",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="キケロ・ホラティウスの翻訳論",
    name_en="Cicero & Horace on translation",
    name_original="De optimo genere oratorum / Ars Poetica",
    period_key="古典・前近代翻訳伝統期",
    definition="マルクス・トゥッリウス・キケロ『最良の弁論家種について』(46 BCE)とホラティウス『詩論』(c. 19 BCE)に見られる翻訳論。キケロは「言葉ではなく意味を（non verbum pro verbo, sed sensum pro sensu）」、ホラティウスは「忠実な翻訳者（fidus interpres）」たることを否定する立場を表明。西洋翻訳論の歴史的源流として、ヒエロニムス『パンマキウスへの書簡』(395)以来繰り返し参照されてきた。",
    background="ヘレニズム期ギリシャ文化のローマ受容、ローマ修辞学伝統の翻訳実践化。",
    development="ヒエロニムス翻訳論、中世スコラ翻訳論、近代欧州翻訳論議全体の歴史的前提となった。",
    historical_context="共和制末期ローマの文化的ギリシャ化期。",
    primary_source_url=GUTEN+"ebooks/47843",
    primary_source_type="Project Gutenberg: Cicero / Horace classical works",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: Specific traditions of translation (8)
# ============================================================
add(**C, name_ja="道安の仏典漢訳論「五失本三不易」",
    name_en="Dao'an's Five Losses and Three Difficulties",
    name_original="五失本三不易",
    period_key="古典・前近代翻訳伝統期",
    definition="道安（312-385）が4世紀後半に提示した中国仏典漢訳の理論的綱領。「五失本（原典の五つの失われ方）」と「三不易（三つの困難）」を定式化し、サンスクリット原典の漢語化における不可避的損失を体系化した中国最古の翻訳論。後の鳩摩羅什・玄奘翻訳論の理論的前提となった。",
    background="後秦期長安における仏典翻訳事業の制度化、サンスクリット・パーリ語仏典の漢訳需要拡大。",
    development="鳩摩羅什（343-413）の意訳的翻訳実践、玄奘（602-664）の「五種不翻」論へと継承。中国翻訳論の歴史的中核理論として現代に至るまで参照される。",
    historical_context="4世紀末中国華北の仏教受容期、長安仏典翻訳センターの形成。",
    primary_source_url=CBETA,
    primary_source_type="CBETA: Dao'an translation prefaces",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"仏教哲学の漢訳",
         "description":"道安の翻訳論は仏教哲学概念の漢語化という哲学的・言語的転換の理論的基盤。"}])

add(**C, name_ja="玄奘「五種不翻」",
    name_en="Xuanzang's Five Untranslatables",
    name_original="五種不翻",
    period_key="古典・前近代翻訳伝統期",
    definition="玄奘（602-664）が7世紀に定式化した仏典翻訳における音訳保持原則。「秘密故」「含多義故」「此無故」「順古故」「生善故」の五条件下では翻訳せず音訳すべきとした。アプター「翻訳不可能性」論の歴史的先駆として、現代翻訳論議でも参照される。玄奘訳『大唐西域記』『大般若経』等の理論的基盤。",
    background="唐代初期長安における大規模翻訳事業（玄奘訳経院）と、サンスクリット原典への直接接触。",
    development="後世の中国仏教翻訳実践全般、東アジア仏教文化圏の音訳語彙形成（菩薩・般若・三昧等）の理論的基盤となった。",
    historical_context="唐太宗・高宗期の文化国際化期、玄奘西域・インド求法旅行(629-645)の帰還後翻訳事業。",
    primary_source_url=CBETA,
    primary_source_type="CBETA: Xuanzang translation prefaces",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"玄奘の音訳保持原則は、翻訳不可能性の歴史的範例。AI翻訳における専門用語・固有名詞・概念語の処理戦略の理論的祖型。",
         "related_ai_phenomenon":"AI翻訳における専門用語の音訳保持"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"仏教哲学概念の保持",
         "description":"玄奘の翻訳論は仏教哲学概念（般若・菩提・涅槃等）の意味的不可訳性を体系化した。"}])

add(**C, name_ja="バグダード「知恵の館」翻訳運動",
    name_en="Bayt al-Hikma translation movement",
    name_original="بيت الحكمة",
    period_key="古典・前近代翻訳伝統期",
    definition="アッバース朝バグダードで8-9世紀に展開された大規模翻訳運動。カリフ・マームーン（在位813-833）が制度化した「知恵の館（Bayt al-Hikma）」を中心に、ギリシャ・シリア・ペルシャ・サンスクリット文献をアラビア語に翻訳。フナイン・イブン・イスハーク（809-873）等が主導し、アリストテレス・ガレノス等のアラビア語化を達成した。",
    background="アッバース朝の文化的・科学的国際化政策、シリアキリスト教徒・ペルシャ人翻訳者ネットワーク。",
    development="12世紀トレド翻訳学派を経由してアリストテレス哲学が西欧に再伝播し、欧州スコラ哲学・大学文化の基盤となった。",
    historical_context="9世紀アッバース朝黄金期、バグダードのグローバル知識中心化。",
    primary_source_url=WIKI_EN+"House_of_Wisdom",
    primary_source_type="Wikipedia: House of Wisdom",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"アリストテレス哲学のアラビア語化",
         "description":"知恵の館はアリストテレス哲学のアラビア語化（イブン・スィーナ・イブン・ルシュド）の制度的基盤。"},
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"翻訳と文化的伝播",
         "description":"知恵の館はギリシャ・ペルシャ・インドの知識のイスラーム文化圏への伝播を媒介した文化人類学的事例。"}])

add(**C, name_ja="トレド翻訳学派",
    name_en="Toledo School of Translators",
    name_original="Escuela de Traductores de Toledo",
    period_key="古典・前近代翻訳伝統期",
    definition="12-13世紀イベリア半島トレドで展開されたアラビア語からラテン語・カスティーリャ語への大規模翻訳事業。レコンキスタ後のキリスト教領内に残存したムスリム学者・ユダヤ人翻訳者を活用し、ジェラルド・オブ・クレモナ（1114-87）、マイケル・スコット等がアリストテレス・ガレノス・アルキンディー・アル＝ファーラビー・イブン・スィーナを欧州に再導入した。",
    background="11世紀末トレド再征服(1085)、イベリア半島の三宗教共存（コンビベンシア）、欧州スコラ哲学のアリストテレス再受容需要。",
    development="13世紀パリ大学・オックスフォード大学のスコラ哲学興隆の基盤となり、トマス・アクィナス『神学大全』のアリストテレス受容を可能にした。",
    historical_context="12世紀ルネサンス（チャールズ・ハスキンズの命名する文化的興隆期）。",
    primary_source_url=WIKI_EN+"Toledo_School_of_Translators",
    primary_source_type="Wikipedia: Toledo School of Translators",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"スコラ哲学とアリストテレス再受容",
         "description":"トレド翻訳学派は欧州スコラ哲学のアリストテレス再導入の制度的基盤を提供した。"}])

add(**C, name_ja="漢文訓読法",
    name_en="Kanbun-yomikudashi method",
    name_original="漢文訓読",
    period_key="古典・前近代翻訳伝統期",
    definition="日本古来の漢文読解・翻訳方法。返り点・送り仮名・乎古止点等の補助記号を漢文原文に付加し、漢文を日本語語順・文法に再構成して読み下す独自の翻訳実践。8世紀奈良時代に成立、平安・鎌倉・江戸期に体系化され、近世日本の漢学・洋学翻訳の方法論的基盤を提供した。",
    background="古代日本の漢字文化受容、奈良仏教の経典漢訳受容と日本的読解需要。",
    development="江戸期漢学塾・蘭学翻訳・明治期欧文翻訳の方法論に応用され、現代日本の漢文教育に継承される。",
    historical_context="奈良-平安期の漢字文化受容期から、明治期の翻訳近代化までの長期的伝統。",
    primary_source_url=WIKI_JA+"%E6%BC%A2%E6%96%87%E8%A8%93%E8%AA%AD",
    primary_source_type="Wikipedia (JA): 漢文訓読",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"訓読は原文を保持したまま別言語化する独自方式。AI翻訳における原文-訳文の重畳表示・並列読解インターフェースの理論的祖型として再評価可能。",
         "related_ai_phenomenon":"AI翻訳の原文・訳文並列インターフェース"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"日本の翻訳人類学",
         "description":"訓読は日本独自の翻訳実践として、文化人類学的言語接触研究の重要事例。"}])

add(**C, name_ja="ヒエロニムス翻訳論",
    name_en="Jerome's translation theory",
    name_original="Epistula 57: De optimo genere interpretandi",
    period_key="古典・前近代翻訳伝統期",
    definition="ヒエロニムス（c.347-420）が395年にパンマキウスに送った書簡『最良の翻訳法について（書簡第57号）』に展開した翻訳論。聖書翻訳における「逐語訳」と聖典以外の「意訳」を区別し、キケロの「意味を意味で（sensum de sensu）」原則を踏襲。ヴルガータ訳聖書(382-405)の翻訳実践と理論を統合した。",
    background="4世紀末ローマ帝国のキリスト教国教化、聖書ラテン語訳統一の必要性、教皇ダマスス1世の依頼。",
    development="中世スコラ翻訳論、近代欧州翻訳論議全般の歴史的前提となり、現代まで西洋翻訳論の中心参照点。",
    historical_context="4世紀末古代末期、キリスト教文化と古典文化の総合期。",
    primary_source_url=ARCHIVE+"texts",
    primary_source_type="archive.org: Jerome Letters / Vulgate",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"聖書翻訳の哲学",
         "description":"ヒエロニムス翻訳論は聖典翻訳における意味と言葉の関係を体系化した最初期の翻訳哲学。"}])

add(**C, name_ja="ロシア翻訳学派",
    name_en="Russian translation school",
    name_original="русская школа перевода",
    period_key="構造主義・記述的翻訳学期",
    definition="20世紀ソ連・ロシアで発達した独自の翻訳理論。アンドレイ・フェドロフ『翻訳理論の基礎』(1953、ソ連最初の体系的翻訳学書)、ヴィレン・コミッサーロフ『翻訳の言語学』(1980)、レオニード・バルフダーロフ『言語と翻訳』(1975)が代表的著作。翻訳の言語学的厳密化を進め、ソ連大規模翻訳事業（外国文学全集刊行）を理論的に支えた。",
    background="ソ連の文化政策的翻訳事業（『外国文学』誌、各国文学全集）、構造言語学の翻訳論への適用。",
    development="ソ連崩壊後はコミッサーロフ等の弟子たちが現代ロシア翻訳学の中核を担い、エヴェン=ゾーハー的ポリシステム論との対話を進めた。",
    historical_context="20世紀ソ連の文化的国際化政策と、ロシア翻訳実践の体系化期。",
    primary_source_url=WIKI_EN+"Translation_studies#Russia",
    primary_source_type="Wikipedia: Translation Studies / Russia",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ラテンアメリカ翻訳思想",
    name_en="Latin American translation thought",
    name_original="pensamiento de la traducción latinoamericano",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="20世紀ラテンアメリカ文学者・思想家による独自の翻訳論伝統。アロイジオ・デ・カンポス『カニバル翻訳』、オスワルド・デ・アンドラーヂ『カニバル宣言』(1928)の食人主義的翻訳論、オクタビオ・パス『翻訳：言葉とその意味について』(1971)、ボルヘスのエッセイ群を中核とする。原文-翻訳の階層を逆転させ、翻訳を創造的同化として捉える思想。",
    background="20世紀ラテンアメリカ文学のヨーロッパ中心経由グローバル化と、それに対する文化的自律志向。",
    development="ヴェヌーティ「外国化」論、ヘロイザ・ゴンサロ・バルボーザ等の現代ラテンアメリカ翻訳論に継承された。",
    historical_context="20世紀ラテンアメリカ文学のブーム期(1960s-)とその理論的自己省察。",
    primary_source_url=WIKI_EN+"Cannibalist_Manifesto",
    primary_source_type="Wikipedia: Cannibalist Manifesto",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"カニバリズム的文化論",
         "description":"オスワルド・デ・アンドラーヂのカニバル宣言はラテンアメリカ文化人類学・文学論の中心テクスト。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="理論",
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
        print(f"[c38-add40] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c38-add40] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
