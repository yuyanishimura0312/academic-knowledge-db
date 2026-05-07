"""LIT-DB Phase 2 Wave 18 — C38 ADD: World Lit / Translation theory (+60).

Subfield: lit_world_translation (id=23). Existing 80. Target 500.
Adds 60 NEW non-overlapping concepts covering:
 A: Classical & pre-modern translation theory (10)
 B: Comparative literature foundations (10)
 C: Polysystem & beyond (8)
 D: Interpretive school & process (5)
 E: Feminist / postcolonial / activist translation (8)
 F: Cultural translation (5)
 G: Machine translation & AI (8)
 H: Literary translation practice (6)

Theory-heavy: ~60% primary (Cicero, Dryden, Schleiermacher 1813, Benjamin,
Berman, Steiner, Vaswani 2017 paper, etc.) + secondary academic.
fourth_transform_tags >= 25, cross_domain to PT/PHIL/AN >= 18.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("古典・前近代翻訳伝統期", "Pre-modern Translation Traditions",
     -300, 1700,
     "ローマ期キケロから中世仏典漢訳・バグダード知恵の館・トレド翻訳学派・江戸期漢文訓読まで、近代以前の主要翻訳伝統。"),
    ("ロマン主義・近代翻訳論期", "Romantic & Modern Translation Theory",
     1700, 1900,
     "ドライデンからシュライアマハー、ゲーテ、フンボルト、ショーペンハウアーまでの近代翻訳論形成期。"),
    ("比較文学形成期", "Formation of Comparative Literature", 1800, 1950, None),
    ("構造主義・記述的翻訳学期", "Structuralist & Descriptive Translation Studies",
     1950, 1990, None),
    ("世界文学・ポストコロニアル翻訳期", "World Literature & Postcolonial Translation",
     1990, 2030, None),
]


GUTEN = "https://www.gutenberg.org/"
ARCHIVE = "https://archive.org/details/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
ARXIV = "https://arxiv.org/abs/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_world_translation", region="理論",
         original_script="roman")


# ============================================================
# A: Classical & pre-modern translation theory (10) — primary heavy
# ============================================================
add(**C, name_ja="キケロ『最善の演説家種について』",
    name_en="Cicero, De optimo genere oratorum",
    name_original="De optimo genere oratorum",
    period_key="古典・前近代翻訳伝統期",
    definition="紀元前46年頃キケロがアイスキネスとデモステネスの演説をラテン語に翻訳した際の序文。「翻訳者ではなく演説家として（non ut interpres sed ut orator）」訳すべきとする原則を提示し、語対語ではなく意味対意味（sense-for-sense）翻訳論の祖とされる。",
    background="ローマ共和制末期のギリシア文化受容と、キケロの修辞学的翻訳実践。",
    development="ヒエロニムスやドライデンに直接影響、西洋翻訳論の出発点。",
    historical_context="ヘレニズム期ローマにおけるギリシア文化吸収の知的運動。",
    primary_source_url=GUTEN+"ebooks/49810",
    primary_source_type="Project Gutenberg: De Optimo Genere Oratorum (Latin)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"キケロの「演説家として訳す」は意味再創造を最優先する立場。LLMの自然性追求型翻訳の古典的原型。",
        "related_ai_phenomenon":"LLM翻訳における自然性優先"}],
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"古代修辞学",
        "description":"キケロ翻訳論は古代修辞学の倫理（decorum）を翻訳に適用した最初期の理論化。"}])

add(**C, name_ja="ホラティウス『詩論』fidus interpres",
    name_en="Horace, Ars Poetica — fidus interpres",
    name_original="Ars Poetica",
    period_key="古典・前近代翻訳伝統期",
    definition="紀元前19年頃ホラティウス『詩論』133-134行「忠実な翻訳者として語を語へと訳すことを求めるな（nec verbo verbum curabis reddere fidus interpres）」が、語対語翻訳への古典的批判として2000年間引用され続ける標語となった。",
    background="アウグストゥス期の文学的成熟とギリシア古典への対峙。",
    development="ヒエロニムス、ドライデン、シュライアマハーすべてが言及する翻訳論の常套句となった。",
    historical_context="ローマ文学黄金期の翻訳/翻案論争。",
    primary_source_url=GUTEN+"ebooks/14020",
    primary_source_type="Project Gutenberg: Ars Poetica (Latin)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"fidus interpres批判は機械的逐語訳を否定する古代の知見。MTの語対語対応を超えた文脈理解の理論的源流。",
        "related_ai_phenomenon":"MT文脈翻訳の理論的根拠"}])

add(**C, name_ja="ヒエロニムス『最善の翻訳法について』",
    name_en="Jerome, De optimo genere interpretandi",
    name_original="Epistula 57 ad Pammachium",
    period_key="古典・前近代翻訳伝統期",
    definition="396年聖ヒエロニムスがパンマキウス宛書簡57で展開した翻訳論。「私はギリシア語からラテン語へ、語を語ではなく意味を意味から訳す（non verbum e verbo, sed sensum exprimere de sensu）」と宣言。聖書（神聖テクスト）と世俗テクストで方針を区別した二層論。",
    background="ウルガタ訳聖書の翻訳実践と、当時の古典文学翻訳論争。",
    development="中世翻訳論の規範となり、宗教改革期の聖書翻訳論争に再活性化された。",
    historical_context="後期ローマ帝国のキリスト教文化形成期。",
    primary_source_url=ARCHIVE+"hieronymi-epistulae",
    primary_source_type="Archive.org: Jerome Epistulae",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"ヒエロニムスの聖典/世俗二層論は、翻訳禁忌領域の存在を示す。AI翻訳における法律・宗教文書の特殊扱いの古典的源流。",
        "related_ai_phenomenon":"AI翻訳の領域別ポリシー"}],
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"聖典解釈学",
        "description":"ヒエロニムス翻訳論は聖書解釈学（hermeneutica sacra）の方法論的基盤を提供した。"}])

add(**C, name_ja="アウグスティヌス『キリスト教の教え』2.16",
    name_en="Augustine, De doctrina christiana 2.16",
    name_original="De doctrina christiana",
    period_key="古典・前近代翻訳伝統期",
    definition="397-426年アウグスティヌス『キリスト教の教え』第2巻16章。聖書翻訳の多様性を擁護し、複数訳の比較が原典理解を深めるとする「複数翻訳並列解釈」の理論を提示。記号論的翻訳観（res/signa）の出発点。",
    background="北アフリカのラテン語聖書諸訳の混乱と、ヒエロニムス新訳への反発。",
    development="中世の註解伝統、ウィクリフ訳論争、現代記号論翻訳論に影響。",
    historical_context="西方教会形成期の聖書テクスト統一問題。",
    primary_source_url=GUTEN+"ebooks/2014",
    primary_source_type="Project Gutenberg: De Doctrina Christiana",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"記号論・解釈学",
        "description":"アウグスティヌスのres/signa理論は中世記号論の基礎で、翻訳論の哲学的母体。"}])

add(**C, name_ja="ロジャー・ベーコン『大著作』言語論",
    name_en="Roger Bacon, Opus Maius — linguistic theory",
    name_original="Opus Maius, Pars III",
    period_key="古典・前近代翻訳伝統期",
    definition="1267年ロジャー・ベーコン『大著作』第3部。原典言語（ヘブライ語・ギリシア語・アラビア語）の習得なしに正しい翻訳は不可能と主張し、中世の三言語主義（trilinguism）を理論化。スコラ翻訳実践の方法論的批判書。",
    background="13世紀パリ大学・オックスフォードでのアラビア哲学受容と、トマス主義の体系化期。",
    development="ルネサンス人文主義の原典回帰運動、宗教改革期の聖書原典主義の遠い起源。",
    historical_context="13世紀知恵の館テクストのラテン語訳の質問題。",
    primary_source_url=ARCHIVE+"opusmajusofroger01baco",
    primary_source_type="Archive.org: Opus Maius (Latin)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="エチエンヌ・ドレ『良き翻訳の方法』1540",
    name_en="Étienne Dolet, La manière de bien traduire (1540)",
    name_original="La manière de bien traduire d'une langue en aultre",
    period_key="古典・前近代翻訳伝統期",
    definition="1540年エチエンヌ・ドレが発表した世界初の体系的翻訳論。翻訳の5原則（原典理解・両言語熟達・逐語主義回避・俗語使用・調和ある文体）を提示。1546年ドレは異端と翻訳の罪で火刑となり、翻訳の政治的危険を象徴する事件となった。",
    background="ルネサンス期フランスの古典語からヴェルナキュラへの翻訳運動。",
    development="ジョアシャン・デュ・ベレ『擁護顕揚』、後の英国翻訳論に影響。",
    historical_context="フランソワ1世期の俗語化政策と宗教改革期の翻訳統制。",
    primary_source_url=ARCHIVE+"lamanieredebien00dole",
    primary_source_type="Archive.org: La manière de bien traduire (1540)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"ドレの5原則は今もMT評価規準の核心。AI翻訳評価指標の遠祖。",
        "related_ai_phenomenon":"AI翻訳の評価フレームワーク"}])

add(**C, name_ja="デュ・ベレ『擁護顕揚』翻訳章",
    name_en="Du Bellay, Défense — translation chapter",
    name_original="La Défense et illustration de la langue française",
    period_key="古典・前近代翻訳伝統期",
    definition="1549年ジョアシャン・デュ・ベレ『フランス語の擁護と顕揚』第1巻第6章。詩の翻訳不可能性を初めて理論化し、「詩の翻訳は無益」と主張、模倣（imitation）と翻案（adaptation）を翻訳に優先させた。フランス・プレイヤード派の宣言書。",
    background="ペトラルカ翻訳の流行への反発と、フランス語の地位確立運動。",
    development="ドライデン三分類、ベンヤミン翻訳不可能性論、アプター untranslatables への系譜。",
    historical_context="16世紀フランス詩のヴェルナキュラ化運動。",
    primary_source_url=GUTEN+"ebooks/27071",
    primary_source_type="Project Gutenberg: Défense et illustration",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"詩の翻訳不可能性論はLLM時代の文学翻訳の限界議論の理論的源流。",
        "related_ai_phenomenon":"AI詩翻訳の限界"}])

add(**C, name_ja="ドライデン metaphrase/paraphrase/imitation",
    name_en="Dryden, metaphrase/paraphrase/imitation",
    name_original="Preface to Ovid's Epistles",
    period_key="ロマン主義・近代翻訳論期",
    definition="1680年ジョン・ドライデン『オウィディウス書簡集』序文。翻訳を3類型に分類した古典的枠組み——逐語訳（metaphrase）・自由訳（paraphrase）・翻案（imitation）。中道のparaphraseを推奨し、近代英語圏翻訳論の出発点となった。",
    background="王政復古期英国の古典翻訳ブームと、フランス美的不実翻訳の影響。",
    development="ポープ、シュライアマハー、ベンヤミン、ヴェヌーティすべてがドライデン3類型を起点に理論化。",
    historical_context="17世紀末英国の古典文学英訳の制度化期。",
    primary_source_url=GUTEN+"ebooks/21765",
    primary_source_type="Project Gutenberg: Dryden, Ovid's Epistles Preface",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"ドライデン3類型は現代MTの literal/free/adaptive モードの原型。",
        "related_ai_phenomenon":"MT翻訳モード設計"}])

add(**C, name_ja="ポープ『イーリアス』『オデュッセイア』序文",
    name_en="Pope, Iliad/Odyssey prefaces",
    name_original="Preface to Pope's Iliad",
    period_key="ロマン主義・近代翻訳論期",
    definition="1715年アレグザンダー・ポープ『イーリアス』英訳序文。ホメロスの「火」と「精神」を保ちつつ英国読者に届く文体を作る原則を提示。詩翻訳における「等価効果」の古典的議論で、後のナイダ機能的等価説の遠祖。",
    background="アウグスタン期英詩の頂点と、古典翻訳の市場成立。",
    development="マシュー・アーノルド『ホメロス翻訳論』、ヴェヌーティ等価批判の前提。",
    historical_context="18世紀英国の古典英訳産業の形成期。",
    primary_source_url=GUTEN+"ebooks/6130",
    primary_source_type="Project Gutenberg: Pope's Iliad",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シュライアマハー『翻訳の方法について』1813詳説",
    name_en="Schleiermacher 1813, Über die verschiedenen Methoden — detail",
    name_original="Ueber die verschiedenen Methoden des Uebersetzens",
    period_key="ロマン主義・近代翻訳論期",
    definition="1813年6月24日ベルリン王立アカデミー講演。翻訳者は「読者を著者の方へ動かす（外国化）」か「著者を読者の方へ動かす（自国化）」の二者択一を迫られるとする決定的二分法。ヴェヌーティ foreignization/domestication の直接の起源。",
    background="ドイツ・ロマン主義の異文化受容論争と、シュライアマハー解釈学の成熟期。",
    development="ベンヤミン、ベルマン、ヴェヌーティが直接継承する翻訳論の理論的核心。",
    historical_context="ナポレオン戦争期ドイツの国民文学形成と外国文学受容。",
    primary_source_url=ARCHIVE+"smtlichewerkedrit03schl",
    primary_source_type="Archive.org: Schleiermacher Sämmtliche Werke III/2",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"二分法は現在のMT/AI翻訳における自国化バイアスとローカリゼーション戦略の理論的フレーム。",
        "related_ai_phenomenon":"MT自国化バイアス"}],
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"解釈学的循環",
        "description":"シュライアマハー翻訳論は彼の解釈学（hermeneutics）の応用であり哲学的翻訳論の頂点。"}])


# ============================================================
# B: Comparative literature foundations (10)
# ============================================================
add(**C, name_ja="フンボルト『アガメムノン』序文",
    name_en="Wilhelm von Humboldt, Preface to Agamemnon",
    name_original="Einleitung zu Aeschylos' Agamemnon",
    period_key="ロマン主義・近代翻訳論期",
    definition="1816年ヴィルヘルム・フォン・フンボルトがアイスキュロス『アガメムノン』独訳の序文。「言語は単なる記号ではなく世界観（Weltansicht）」とする言語哲学を翻訳論に適用、翻訳の根源的不可能性と必要性のパラドックスを定式化。",
    background="ドイツ・ロマン主義の言語哲学とゲーテ世界文学論の同時代的展開。",
    development="ベンヤミン「翻訳者の使命」、サピア=ウォーフ仮説、アプター untranslatables の哲学的源流。",
    historical_context="ベルリン大学創立期の人文主義改革。",
    primary_source_url=ARCHIVE+"aischylosagameno00aescuoft",
    primary_source_type="Archive.org: Aeschylos Agamemnon (Humboldt 1816)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"言語=世界観論はLLMの言語別バイアス・文化的盲点問題の哲学的源流。",
        "related_ai_phenomenon":"LLM言語別世界観バイアス"}],
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"言語相対性原理",
        "description":"フンボルトの言語=世界観論はサピア=ウォーフ仮説、認知言語学の哲学的祖先。"}])

add(**C, name_ja="ゲーテ Naturformen vs Kunstformen",
    name_en="Goethe, Naturformen vs Kunstformen",
    name_original="Noten und Abhandlungen zu West-östlichem Divan",
    period_key="ロマン主義・近代翻訳論期",
    definition="1819年ゲーテ『西東詩集』付録「翻訳の3様式」で展開した翻訳の3段階理論——伝達的（散文的）・翻案的（自国文化様式）・最高段階（原典に同定する逐語的）。第3段階を理想とする翻訳ヒエラルキー論。",
    background="ペルシア詩翻訳とハーフェズ受容、世界文学（Weltliteratur）構想。",
    development="ベンヤミンの翻訳論、ベルマン他者の試練、世界文学論の理論的母体。",
    historical_context="後期ロマン主義の東洋文学受容期。",
    primary_source_url=GUTEN+"ebooks/2319",
    primary_source_type="Project Gutenberg: West-östlicher Divan",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"ゲーテ3段階説は機械翻訳の自然性vs忠実性のトレードオフの古典的定式化。",
        "related_ai_phenomenon":"MT忠実性vs自然性"}])

add(**C, name_ja="ショーペンハウアー『言語と語について』",
    name_en="Schopenhauer, Über Sprache und Worte",
    name_original="Parerga und Paralipomena, §299",
    period_key="ロマン主義・近代翻訳論期",
    definition="1851年ショーペンハウアー『パレルガとパラリポメナ』第299節。各言語に固有の概念があり、完全な対応語は存在しないとする「翻訳不可能語（Untranslatable）」論の哲学的定式化。アプター『翻訳不可能なもの』の19世紀的源流。",
    background="カント認識論とフンボルト言語哲学の継承、東洋哲学受容。",
    development="ヴィトゲンシュタイン、カッサン『翻訳不可能語辞典』、アプター理論の遠祖。",
    historical_context="19世紀ドイツ哲学の言語論的転回前史。",
    primary_source_url=GUTEN+"ebooks/40868",
    primary_source_type="Project Gutenberg: Parerga und Paralipomena",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"言語と思考",
        "description":"ショーペンハウアーの翻訳不可能語論は分析哲学・現象学言語論の源流。"}])

add(**C, name_ja="ベンヤミン『翻訳者の使命』深層読解",
    name_en="Benjamin, Aufgabe des Übersetzers — deeper readings",
    name_original="Die Aufgabe des Übersetzers",
    period_key="比較文学形成期",
    definition="アンドリュー・ベンジャミン『翻訳と哲学』(1989)、ポール・ド・マン『翻訳者の使命の結論』(1986)、ルドルフ・パンヴィッツ引用の起源、スタイナー『バベル以後』のベンヤミン論など、ヴァルター・ベンヤミン1923年序文の20世紀後半デコンストラクション読解の系譜。",
    background="ベンヤミン受容のフランス・北米学術史と、ド・マン脱構築の影響。",
    development="アガンベン、デリダ、アプターのベンヤミン読解へと展開。",
    historical_context="1980年代北米脱構築理論期と、ベンヤミン『使命』の正典化。",
    primary_source_url=ARCHIVE+"resistancetotheo0000mand",
    primary_source_type="Archive.org: de Man, Resistance to Theory",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"ベンヤミン的「純粋言語」概念はLLMの多言語埋め込み空間の哲学的隠喩。",
        "related_ai_phenomenon":"LLM多言語潜在空間"}],
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"脱構築翻訳論",
        "description":"ド・マン読解はベンヤミン論を脱構築哲学の中心テクストに据えた。"}])

add(**C, name_ja="ベルマン『他者の試練』",
    name_en="Berman, L'épreuve de l'étranger",
    name_original="L'épreuve de l'étranger",
    period_key="構造主義・記述的翻訳学期",
    definition="1984年アントワーヌ・ベルマン『他者の試練——ロマン主義ドイツの文化と翻訳』。シュライアマハー、フンボルト、ノヴァーリス、シュレーゲル兄弟らドイツ・ロマン主義の翻訳思想を再構築し、外国化（étranger）翻訳の倫理を理論化。ヴェヌーティに直接影響。",
    background="フランス語圏の翻訳論不在を埋めるドイツ翻訳哲学受容運動。",
    development="ベルマン『翻訳論およびアントワーヌ・ベルマン批判の試論』、ヴェヌーティ外国化論の理論基盤。",
    historical_context="1980年代フランス翻訳学の制度化期。",
    primary_source_url=WIKI_FR+"L'%C3%89preuve_de_l'%C3%A9tranger",
    primary_source_type="Wikipedia FR: L'épreuve de l'étranger",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"ベルマン他者の試練はAI翻訳の文化的他者性消去問題への倫理的批判基盤。",
        "related_ai_phenomenon":"AI翻訳の文化平準化批判"}])

add(**C, name_ja="ポズネット『比較文学』1886",
    name_en="Posnett, Comparative Literature (1886)",
    name_original="Comparative Literature",
    period_key="比較文学形成期",
    definition="1886年ハッチソン・マコーレー・ポズネット著、世界初の体系的比較文学概論書。社会的進化論の枠組みで世界文学を「氏族文学→部族文学→国民文学→世界文学」と発展段階で捉える。比較文学の制度化に決定的影響。",
    background="ヴィクトリア期英国の社会進化論と、ゲーテ世界文学概念の受容。",
    development="20世紀比較文学の出発点として、ヴェセロフスキー、エティアンブル、ダムロッシュらに継承された。",
    historical_context="19世紀末英国の人文学制度化期。",
    primary_source_url=ARCHIVE+"comparativeliter00pos",
    primary_source_type="Archive.org: Posnett, Comparative Literature (1886)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ゲイリー『比較文学の創設』",
    name_en="Gayley, Founding of Comparative Literature",
    name_original="The Society of Comparative Literature",
    period_key="比較文学形成期",
    definition="1894年チャールズ・ミルズ・ゲイリーがカリフォルニア大学に北米最初の比較文学学会を設立、1900年代「比較文学協会」設立論を発表。米国比較文学制度の創設者。",
    background="19世紀末米国の独国型大学制度導入と、世界文学への学術的関心。",
    development="後のレマック「米国学派」、ウェレック「比較文学の危機」へ繋がる北米比較文学の出発点。",
    historical_context="米国大学院制度形成期。",
    primary_source_url=WIKI_EN+"Comparative_literature",
    primary_source_type="Wikipedia: Comparative Literature history",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ブリュヌティエール比較文学",
    name_en="Ferdinand Brunetière, comparative literature",
    name_original="L'évolution des genres dans l'histoire de la littérature",
    period_key="比較文学形成期",
    definition="1890年フェルディナン・ブリュヌティエール『文学史におけるジャンルの進化』。ダーウィン進化論を文学ジャンル発展に応用し、フランス比較文学（影響研究学派）の方法論的祖となった。",
    background="19世紀末フランスの実証主義批評と、テーヌ環境決定論の継承。",
    development="バルダンスペルジェ、グヤール、ヴァン・ティーゲムらフランス学派の理論的源流。",
    historical_context="第三共和制フランス大学の文学史制度化期。",
    primary_source_url=GUTEN+"ebooks/47077",
    primary_source_type="Project Gutenberg: Brunetière, Évolution des genres",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="グヤール『比較文学』",
    name_en="Marius-François Guyard, La littérature comparée",
    name_original="La littérature comparée",
    period_key="比較文学形成期",
    definition="1951年マリウス＝フランソワ・グヤール著、フランス比較文学の標準的入門書。「フランス学派」（影響研究・受容研究）の方法論を体系化し、第二次大戦後の比較文学制度化に決定的役割を果たした。",
    background="戦後フランスの大学制度復興と、ソルボンヌの比較文学講座再編。",
    development="エティアンブル『比較は理由ならず』(1963)による批判の標的となり、比較文学方法論争の起点。",
    historical_context="冷戦初期の欧州人文学制度再建期。",
    primary_source_url=WIKI_FR+"Litt%C3%A9rature_compar%C3%A9e",
    primary_source_type="Wikipedia FR: Littérature comparée",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="レマック「米国学派」定義",
    name_en="Henry Remak, American School definition",
    name_original="Comparative Literature, Its Definition and Function",
    period_key="比較文学形成期",
    definition="1961年ヘンリー・レマック「比較文学——その定義と機能」。「比較文学とは、ある国の文学と他国の文学・芸術・哲学・歴史・社会科学・自然科学・宗教等との比較研究」とする拡張的定義で米国学派を定式化。フランス学派の影響研究中心主義を批判。",
    background="冷戦期米国大学院の比較文学プログラム拡大と、領域横断志向の隆盛。",
    development="ウェレック「比較文学の危機」(1959)、北米比較文学拡張主義の理論基盤。",
    historical_context="1960年代米国学際研究運動。",
    primary_source_url=WIKI_EN+"Comparative_literature#American_school",
    primary_source_type="Wikipedia: American School Comparative Lit",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# C: Polysystem & beyond (8)
# ============================================================
add(**C, name_ja="ウェレック「比較文学の危機」1959",
    name_en="Wellek, Crisis of Comparative Literature (1959)",
    name_original="The Crisis of Comparative Literature",
    period_key="構造主義・記述的翻訳学期",
    definition="1958年チャペルヒル国際比較文学会議でルネ・ウェレックが発表、フランス学派の影響研究実証主義を「文学性の喪失」として批判、比較文学を「文学そのもの」の研究として再定義。北米学派の理論的旗印。",
    background="1950年代米国ニュー・クリティシズムの隆盛と、欧州学派への対抗意識。",
    development="レマック定義、エティアンブル『比較は理由ならず』(1963)反論論争へ。",
    historical_context="冷戦期人文学の方法論論争。",
    primary_source_url=WIKI_EN+"Ren%C3%A9_Wellek",
    primary_source_type="Wikipedia: Wellek, Crisis essay",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="エヴェン=ゾーハー『ポリシステム研究』",
    name_en="Even-Zohar, Polysystem Studies",
    name_original="Polysystem Studies",
    period_key="構造主義・記述的翻訳学期",
    definition="1990年イタマール・エヴェン=ゾーハー『ポリシステム研究』（Poetics Today誌特集号）。文学を中心と周縁が動的に交渉する複数システムの集合（polysystem）として捉える理論で、翻訳文学が国民文学の中心へ侵入する過程を理論化。テルアビブ学派の中核。",
    background="ロシア・フォルマリズムとプラハ構造主義の継承、若いイスラエル国民文学の翻訳依存性。",
    development="トゥーリのDTS、ラムベール、ヘルマンス、バスネット文化的転回への直接影響。",
    historical_context="1970-80年代の翻訳学独立学問化と国際化。",
    primary_source_url=WIKI_EN+"Polysystem_theory",
    primary_source_type="Wikipedia: Polysystem theory",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"ポリシステム理論はLLM時代の言語別データ量非対称性とその文化的影響を分析する基盤理論。",
        "related_ai_phenomenon":"LLMの低リソース言語問題"}])

add(**C, name_ja="トゥーリ『記述翻訳学とその彼方』",
    name_en="Toury, Descriptive Translation Studies and Beyond",
    name_original="Descriptive Translation Studies and Beyond",
    period_key="構造主義・記述的翻訳学期",
    definition="1995年ギデオン・トゥーリ著、DTSの決定版。翻訳「規範（norms）」の経験的記述、「初期規範（initial norm）」「予備規範」「操作規範」の3層モデル、目標文化指向の翻訳概念を体系化。実証的翻訳学の基盤。",
    background="エヴェン=ゾーハー・ポリシステム理論を方法論的に体系化する課題。",
    development="チェスタマン『翻訳のミーム』、現代コーパス翻訳学、機械翻訳評価論の理論基盤。",
    historical_context="1990年代欧州翻訳学の制度化と国際化期。",
    primary_source_url=WIKI_EN+"Gideon_Toury",
    primary_source_type="Wikipedia: Gideon Toury",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"トゥーリ規範論はAI翻訳評価の規範的vs記述的分析の理論的源流。",
        "related_ai_phenomenon":"MT規範分析"}])

add(**C, name_ja="チェスタマン『翻訳のミーム』",
    name_en="Chesterman, Memes of Translation",
    name_original="Memes of Translation",
    period_key="構造主義・記述的翻訳学期",
    definition="1997年アンドリュー・チェスタマン著。翻訳概念・規範・戦略を「ミーム（meme）」として伝達される文化情報単位として理論化、翻訳5規範（期待・関係・コミュニケーション・責任・倫理）を提示。ドーキンス的進化論を翻訳学に応用。",
    background="トゥーリ規範論の発展と、文化進化論の翻訳学への移植。",
    development="翻訳教育、翻訳倫理学、翻訳プロセス研究の理論的基盤。",
    historical_context="1990年代後半翻訳学の哲学的・倫理的転回。",
    primary_source_url=WIKI_EN+"Andrew_Chesterman",
    primary_source_type="Wikipedia: Andrew Chesterman",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ホームズ『翻訳学の地図』",
    name_en="Holmes, Map of Translation Studies",
    name_original="The Name and Nature of Translation Studies",
    period_key="構造主義・記述的翻訳学期",
    definition="1972年ジェイムズ・S・ホームズが第3回応用言語学AILA会議で発表、翻訳学（Translation Studies）を「純粋翻訳学（理論+記述）」と「応用翻訳学（教育+ツール+批評）」に分類した学問地図。翻訳学制度化の出発点文書。",
    background="1960-70年代の翻訳実践の量的拡大と、独立学問化の必要性。",
    development="トゥーリDTS、テルアビブ学派、欧州翻訳学制度化の理論的母体。",
    historical_context="1972年コペンハーゲンAILA会議、翻訳学の独立宣言。",
    primary_source_url=WIKI_EN+"James_S._Holmes",
    primary_source_type="Wikipedia: James S. Holmes",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ピム『翻訳史の方法』",
    name_en="Pym, Method in Translation History",
    name_original="Method in Translation History",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1998年アンソニー・ピム『翻訳史の方法』、2014年改訂版。翻訳史記述の方法論を体系化し、翻訳者個人・社会的場・歴史的因果関係の分析枠組みを提示。社会学的翻訳学の方法論的基盤。",
    background="1990年代翻訳史記述の急増と、方法論の不在。",
    development="翻訳社会学（ヴォルフ・フカリ）、翻訳者ハビトゥス研究、翻訳労働社会学への展開。",
    historical_context="2000年前後の翻訳学の社会学的転回期。",
    primary_source_url=WIKI_EN+"Anthony_Pym",
    primary_source_type="Wikipedia: Anthony Pym",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハーマンス『異文化逸脱』",
    name_en="Hermans, Crosscultural Transgressions",
    name_original="Crosscultural Transgressions",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2002年テオ・ハーマンス編『異文化逸脱——翻訳学の研究モデル・観察II』。翻訳学の認識論的基盤を再考、翻訳者の声・自己反省性・翻訳学のメタ理論を中心に置いた論集。批判的翻訳学の代表的著作。",
    background="ポリシステム後の翻訳学の認識論的混乱と再構築の試み。",
    development="翻訳学の自己反省的展開、社会構築主義的翻訳論の基盤。",
    historical_context="2000年代翻訳学の哲学的成熟期。",
    primary_source_url=WIKI_EN+"Theo_Hermans",
    primary_source_type="Wikipedia: Theo Hermans",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ロビンソン『翻訳者の転回』",
    name_en="Robinson, The Translator's Turn",
    name_original="The Translator's Turn",
    period_key="構造主義・記述的翻訳学期",
    definition="1991年ダグラス・ロビンソン著、翻訳学に翻訳者の身体・感情・倫理的主体性を導入した先駆的著作。1997年『翻訳と帝国』で植民地翻訳の権力分析を展開。北米翻訳学の身体論的転回の起点。",
    background="ポストモダン身体論と、翻訳学の構造主義的脱身体化への反発。",
    development="翻訳プロセス研究、認知翻訳学、翻訳者倫理学の理論的基盤となった。",
    historical_context="1990年代翻訳学の主体・身体への回帰期。",
    primary_source_url=WIKI_EN+"Douglas_Robinson_(academic)",
    primary_source_type="Wikipedia: Douglas Robinson (translator)",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: Interpretive school & process (5)
# ============================================================
add(**C, name_ja="セレスコヴィッチ『意味の理論』",
    name_en="Seleskovitch & Lederer, théorie du sens (ESIT)",
    name_original="Théorie interprétative de la traduction",
    period_key="構造主義・記述的翻訳学期",
    definition="1968年ダニカ・セレスコヴィッチ、1980年代マリアンヌ・ルデレールがパリ高等翻訳通訳学校（ESIT）で確立した「意味の理論（théorie du sens / interpretive theory）」。通訳・翻訳のプロセスを「言語剥奪→意味理解→再表現」の3段階と捉え、語ではなく意味の通訳を重視。",
    background="同時通訳の実務的観察と、構造主義言語学の不十分性。",
    development="通訳学（Interpreting Studies）の独立学問化、ESITモデル、現代AVT・会議通訳教育の基盤。",
    historical_context="1970-80年代EU・国連の同時通訳需要拡大期。",
    primary_source_url=WIKI_FR+"Th%C3%A9orie_interpr%C3%A9tative_de_la_traduction",
    primary_source_type="Wikipedia FR: théorie interprétative",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジル『努力モデル』",
    name_en="Gile, Effort Models in Conference Interpreting",
    name_original="Basic Concepts and Models for Interpreter and Translator Training",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ダニエル・ジル『通訳者・翻訳者教育の基礎概念とモデル』(1995/2009)。同時通訳の認知負荷を「聴解努力＋記憶努力＋産出努力＋協調」の合計モデルとして定式化、通訳者の限界資源理論。認知通訳学の標準モデル。",
    background="同時通訳の認知科学的研究と、通訳教育の科学化要請。",
    development="認知通訳学、通訳者疲労研究、AI通訳支援システム設計の理論基盤。",
    historical_context="1990年代欧州通訳教育の制度化期。",
    primary_source_url=WIKI_EN+"Daniel_Gile",
    primary_source_type="Wikipedia: Daniel Gile",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"努力モデルはAI通訳システムのリアルタイム認知負荷シミュレーションの理論的基盤。",
        "related_ai_phenomenon":"AI通訳システム設計"}])

add(**C, name_ja="ペヒハッカー『通訳学入門』",
    name_en="Pöchhacker, Introducing Interpreting Studies",
    name_original="Introducing Interpreting Studies",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2004/2016年フランツ・ペヒハッカー著、通訳学の標準教科書。会議通訳・コミュニティ通訳・法廷通訳・医療通訳・手話通訳を統合的に扱い、通訳学を独立分野として体系化。",
    background="通訳実務の多様化と、翻訳学からの通訳学独立要請。",
    development="通訳学のグローバル制度化、医療・法廷通訳の専門教育の基盤教科書。",
    historical_context="2000年代通訳学の独立学問化期。",
    primary_source_url=WIKI_EN+"Franz_P%C3%B6chhacker",
    primary_source_type="Wikipedia: Franz Pöchhacker",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴァーデンスヨ『相互作用としての通訳』",
    name_en="Wadensjö, Interpreting as Interaction",
    name_original="Interpreting as Interaction",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1998年セシリア・ヴァーデンスヨ著、コミュニティ通訳を会話分析的に捉え、通訳者を「中立的伝導体」ではなく相互作用の能動的参加者として理論化。コミュニティ通訳学の中核理論。",
    background="スウェーデンの移民コミュニティ通訳実践と、ゴフマン会話分析の応用。",
    development="法廷・医療・難民通訳の倫理学、通訳者役割論の理論基盤。",
    historical_context="1990年代北欧の移民・難民支援と通訳制度整備期。",
    primary_source_url=WIKI_EN+"Cecilia_Wadensj%C3%B6",
    primary_source_type="Wikipedia: Cecilia Wadensjö",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"会話分析・相互行為人類学",
        "description":"通訳の相互作用論はグッドウィン・ゴフマンの会話分析人類学の応用領域。"}])

add(**C, name_ja="アンジェレッリ『異文化社会言語学モデル』",
    name_en="Angelelli, Cross-cultural Sociolinguistic Models",
    name_original="Revisiting the Interpreter's Role",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2004年クラウディア・アンジェレッリ著、医療通訳の社会言語学的モデル。通訳者を中立的「導管」ではなく文化的・言語的・社会的調停者（cultural mediator）として捉える理論。米国医療通訳教育の基盤。",
    background="米国の多言語化と、医療場面での通訳エラー問題の社会的可視化。",
    development="医療通訳認証制度、医療人類学的通訳論、医療翻訳AIシステム設計に影響。",
    historical_context="2000年代米国医療通訳の制度化期。",
    primary_source_url=WIKI_EN+"Claudia_Angelelli",
    primary_source_type="Wikipedia: Claudia Angelelli",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: Feminist / postcolonial / activist translation (8)
# ============================================================
add(**C, name_ja="サイモン『翻訳における性差』",
    name_en="Sherry Simon, Gender in Translation",
    name_original="Gender in Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1996年シェリー・サイモン著、フェミニスト翻訳論の決定的著作。19世紀ヴィクトリア朝女性翻訳者の不可視化、現代フェミニスト翻訳介入戦略、ジェンダー化された言語の翻訳問題を体系化。",
    background="ケベック・フェミニスト文学運動と、英語圏ジェンダー研究の翻訳学への合流。",
    development="フォン・フロトウ、メッシエ、レヴィン等フェミニスト翻訳学の理論的基盤。",
    historical_context="1990年代北米フェミニズム第三波と人文学制度化。",
    primary_source_url=WIKI_EN+"Sherry_Simon",
    primary_source_type="Wikipedia: Sherry Simon",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"ジェンダー","status":"rethinking",
        "rationale":"フェミニスト翻訳論はAI翻訳のジェンダーバイアス（he/sheデフォルト等）の批判的分析の理論的源流。",
        "related_ai_phenomenon":"MTジェンダーバイアス"}])

add(**C, name_ja="フォン・フロトウ『翻訳とジェンダー』",
    name_en="Luise von Flotow, Translation and Gender",
    name_original="Translation and Gender",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1997年ルイーズ・フォン・フロトウ著、フェミニスト翻訳実践の3戦略——「補足（supplementing）」「序文・脚注（prefacing/footnoting）」「ハイジャック（hijacking）」を体系化。ケベック実践の理論化。",
    background="1980-90年代ケベック・フェミニスト作家（ニコル・ブロサール等）の英訳ブーム。",
    development="クィア翻訳、トランス翻訳、AI翻訳ジェンダー批判の理論的基盤。",
    historical_context="1990年代北米フェミニスト翻訳実践の制度化。",
    primary_source_url=WIKI_EN+"Luise_von_Flotow",
    primary_source_type="Wikipedia: Luise von Flotow",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スピヴァク「翻訳の政治学」",
    name_en="Spivak, The Politics of Translation",
    name_original="The Politics of Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1993年ガヤトリ・C・スピヴァク『他なる世界において』所収論文。ベンガル語フェミニスト作品の英訳実践を通じ、第三世界女性作家の英訳における文化的還元主義を批判、「真の翻訳」の三階層（論理的・修辞的・沈黙）を提示。",
    background="サバルタン研究、デリダ脱構築、ベンガル文学英訳実践。",
    development="ポストコロニアル翻訳、トランスナショナル・フェミニズム、惑星性論の理論的核心。",
    historical_context="1990年代ポストコロニアル批評の頂点期。",
    primary_source_url=WIKI_EN+"Gayatri_Chakravorty_Spivak",
    primary_source_type="Wikipedia: Gayatri Spivak",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"サバルタン理論",
        "description":"翻訳の政治学はサバルタン研究の言語論的展開で、ポストコロニアル哲学の中核。"},
        {"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"ポストコロニアル人類学",
        "description":"スピヴァクの翻訳論は人類学的他者表象批判と並行する。"}])

add(**C, name_ja="ニランジャーナ『場の取り戻し』",
    name_en="Tejaswini Niranjana, Siting Translation",
    name_original="Siting Translation: History, Post-Structuralism, and the Colonial Context",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1992年テジャスウィニ・ニランジャーナ著、植民地翻訳のポスト構造主義的批判。英国インド統治下のサンスクリット古典英訳が「東洋」を構築し、植民地知の体制を支えた過程をベンヤミン・デリダ・フーコーで分析。",
    background="サバルタン研究、サイード・オリエンタリズム、デリダ脱構築の融合。",
    development="ポストコロニアル翻訳学の出発点、ヴェヌーティ外国化論との対話。",
    historical_context="1990年代北米ポストコロニアル批評制度化期。",
    primary_source_url=WIKI_EN+"Tejaswini_Niranjana",
    primary_source_type="Wikipedia: Tejaswini Niranjana",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"植民地知の体制",
        "description":"植民地翻訳と知の体制論は人類学のwriting culture論議と並行。"}])

add(**C, name_ja="ベイカー『翻訳と紛争』",
    name_en="Mona Baker, Translation and Conflict",
    name_original="Translation and Conflict: A Narrative Account",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2006年モナ・ベイカー著、紛争状況での翻訳・通訳のナラティヴ理論。9.11以後の戦争翻訳・人権翻訳・抵抗翻訳を分析、翻訳者の「reframing（枠組み再構築）」戦略を中心概念とする。活動家翻訳学の理論的基盤。",
    background="9.11後のイラク戦争翻訳問題と、人権NGO翻訳実践の急増。",
    development="ティモシュコ活動家翻訳論との対話、Translators Without Borders等の理論基盤。",
    historical_context="2000年代「テロとの戦争」期の翻訳の政治化。",
    primary_source_url=WIKI_EN+"Mona_Baker",
    primary_source_type="Wikipedia: Mona Baker",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ハティム&メイソン『翻訳者としてのコミュニケーター』",
    name_en="Hatim & Mason, The Translator as Communicator",
    name_original="The Translator as Communicator",
    period_key="構造主義・記述的翻訳学期",
    definition="1990/1997年バジル・ハティム＆イアン・メイソン『翻訳者としての言説』『翻訳者としてのコミュニケーター』2部作。ハリデー機能言語学を翻訳学に応用、翻訳をテクスト類型・談話・記号論の3層で分析。",
    background="ハリデー体系機能言語学とテクスト言語学の翻訳学への合流。",
    development="談話分析翻訳学、批判的言説分析翻訳論、機能的MT評価の理論的基盤。",
    historical_context="1990年代欧州応用言語学翻訳論の隆盛期。",
    primary_source_url=WIKI_EN+"Basil_Hatim",
    primary_source_type="Wikipedia: Basil Hatim",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ルフェーヴル『翻訳・書き換え・操作』",
    name_en="Lefevere, Translation, Rewriting and Manipulation",
    name_original="Translation, Rewriting, and the Manipulation of Literary Fame",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1992年アンドレ・ルフェーヴル著、文化的転回の代表的著作。翻訳を「書き換え（rewriting）」の一形態として捉え、パトロネージ・詩学・イデオロギーの3要素が文学的名声を操作する過程を理論化。",
    background="バスネット&ルフェーヴル『翻訳・歴史・文化』(1990)文化的転回の体系化。",
    development="ヴェヌーティ、ティモシュコ、社会学的翻訳学の直接基盤。",
    historical_context="1990年代翻訳学の文化的転回期。",
    primary_source_url=WIKI_EN+"Andr%C3%A9_Lefevere",
    primary_source_type="Wikipedia: André Lefevere",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バスネット&トリヴェディ『ポストコロニアル翻訳』",
    name_en="Bassnett & Trivedi, Postcolonial Translation",
    name_original="Post-colonial Translation: Theory and Practice",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1999年スーザン・バスネット＆ハリッシュ・トリヴェディ編『ポストコロニアル翻訳——理論と実践』。文化的転回とポストコロニアル研究の合流点として、植民地翻訳の権力非対称・カニバリズム翻訳・抵抗翻訳を統合的に論じた論集。",
    background="1990年代後半の文化的転回・ポストコロニアル翻訳・世界文学論の収斂。",
    development="アプター翻訳ゾーン論、ダムロッシュ世界文学論の理論的前提。",
    historical_context="1990年代末の翻訳学グローバル化期。",
    primary_source_url=WIKI_EN+"Susan_Bassnett",
    primary_source_type="Wikipedia: Susan Bassnett",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"ポストコロニアル人類学",
        "description":"ポストコロニアル翻訳論は人類学的他者表象批判の言語実践版。"}])


# ============================================================
# F: Cultural translation (5)
# ============================================================
add(**C, name_ja="アサド「文化翻訳の概念」",
    name_en="Asad, The Concept of Cultural Translation",
    name_original="The Concept of Cultural Translation in British Social Anthropology",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1986年タラル・アサド『書くカルチャー』所収論文。英国社会人類学の「文化翻訳」概念を批判的に分析、人類学者の翻訳実践に内在する権力非対称（西洋言語の特権性）を暴露した。文化翻訳論の批判的源泉。",
    background="クリフォード&マーカス『書くカルチャー』(1986)の人類学的反省運動。",
    development="文化人類学の翻訳論的転回、ポストコロニアル翻訳論、文化翻訳概念の哲学的基盤。",
    historical_context="1980年代北米人類学のwriting culture論議。",
    primary_source_url=WIKI_EN+"Talal_Asad",
    primary_source_type="Wikipedia: Talal Asad",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"writing culture論",
        "description":"アサド文化翻訳論はwriting culture論議の翻訳学的核心。"},
        {"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"異文化理解の哲学",
        "description":"文化翻訳概念はガダマー解釈学・テイラー異文化理解論と接続。"}])

add(**C, name_ja="トリヴェディ『現代における文学翻訳』",
    name_en="Harish Trivedi, In Our Time / Translation Culture",
    name_original="Translation Culture and Counter-Culture",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2007年ハリッシュ・トリヴェディ「文化翻訳と翻訳文化」論文。バーバ・スピヴァク等のメタファ的「文化翻訳」概念を批判、実際の言語間翻訳実践への回帰を要請。インドの多言語翻訳文化を理論化。",
    background="ホミ・バーバ『文化の場所』(1994)の文化翻訳概念のメタファ的拡散への反発。",
    development="アプター untranslatables、ダムロッシュ世界文学論との対話を生んだ。",
    historical_context="2000年代インドの多言語文学論の制度化期。",
    primary_source_url=WIKI_EN+"Harish_Trivedi",
    primary_source_type="Wikipedia: Harish Trivedi",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バッハマン=メディック『文化的転回』",
    name_en="Bachmann-Medick, Cultural Turns — deeper",
    name_original="Cultural Turns: Neuorientierungen in den Kulturwissenschaften",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2006年ドリス・バッハマン=メディック『文化的転回——文化学の新方向』。20世紀後半の人文学7つの転回（解釈学的・パフォーマティブ・反省・ポストコロニアル・翻訳的・空間的・図像的）を整理し、「翻訳的転回」を独立カテゴリーとして提示。",
    background="ドイツ語圏文化学（Kulturwissenschaft）の体系化要請。",
    development="翻訳人類学、グローバル文化学、トランスカルチュラル研究の理論基盤。",
    historical_context="2000年代欧州人文学の方法論的成熟期。",
    primary_source_url=WIKI_DE+"Doris_Bachmann-Medick",
    primary_source_type="Wikipedia DE: Doris Bachmann-Medick",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スタイナー『バベル以後』",
    name_en="Steiner, After Babel",
    name_original="After Babel: Aspects of Language and Translation",
    period_key="構造主義・記述的翻訳学期",
    definition="1975年ジョージ・スタイナー著、翻訳論の総合的著作。翻訳を「解釈学的運動（hermeneutic motion）」の4段階——信頼・侵襲・統合・補償——として理論化、翻訳を理解一般のモデルとする壮大な視野を提示。",
    background="ハイデガー・ガダマー解釈学と、戦後ユダヤ・欧州知識人の多言語経験。",
    development="バーマン他者の試練、ヴェヌーティ批判、多くの翻訳論の対話相手となった古典。",
    historical_context="1970年代北米・英国人文学の解釈学受容期。",
    primary_source_url=WIKI_EN+"After_Babel",
    primary_source_type="Wikipedia: After Babel",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"解釈学的循環",
        "description":"スタイナー翻訳論はガダマー解釈学を翻訳実践に最も体系的に適用した著作。"}])

add(**C, name_ja="エーコ『鼠か蝿か』",
    name_en="Eco, Mouse or Rat?",
    name_original="Mouse or Rat? Translation as Negotiation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2003年ウンベルト・エーコ著、翻訳を「交渉（negotiation）」として捉える実践論。自著（『薔薇の名前』『前日島』等）の多言語翻訳経験から、忠実性ではなく等価効果と読者交渉の倫理を提示。",
    background="エーコ自身の作家・翻訳者経験と、彼の記号論の翻訳論への応用。",
    development="現代文学翻訳実践論の代表的著作、AI翻訳評価の理論的参照。",
    historical_context="2000年代欧州知識人翻訳論の総合期。",
    primary_source_url=WIKI_EN+"Mouse_or_Rat%3F",
    primary_source_type="Wikipedia: Mouse or Rat?",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# G: Machine translation & AI (8)
# ============================================================
add(**C, name_ja="ALPACレポート1966",
    name_en="ALPAC Report (1966)",
    name_original="Languages and Machines: Computers in Translation and Linguistics",
    period_key="構造主義・記述的翻訳学期",
    definition="1966年米国科学アカデミー言語自動処理諮問委員会（ALPAC）報告書。当時の機械翻訳の質を厳しく評価し、「実用的MTは存在しない」と結論、米国MT研究予算を大幅削減した。MT「冬の時代」の起点。",
    background="冷戦期米国のロシア語自動翻訳研究投資への評価要請。",
    development="MT研究の20年停滞期を生み、計算言語学の理論研究への転換を促した。",
    historical_context="1960年代米国MTプロジェクト（Georgetown-IBM等）の挫折期。",
    primary_source_url=WIKI_EN+"ALPAC",
    primary_source_type="Wikipedia: ALPAC",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"ALPACは現代AI翻訳の評価基準論争（過大評価/過小評価）の歴史的原型。",
        "related_ai_phenomenon":"AI翻訳評価の歴史的教訓"}])

add(**C, name_ja="ジョージタウン=IBM実験1954",
    name_en="Georgetown-IBM Experiment (1954)",
    name_original="Georgetown-IBM machine translation experiment",
    period_key="構造主義・記述的翻訳学期",
    definition="1954年1月7日ジョージタウン大学とIBMが共同で実施した世界初の公開MT実験。IBM 701計算機がロシア語60文を英語に自動翻訳、メディアに「3-5年で全自動翻訳」と楽観論を生んだ歴史的イベント。",
    background="冷戦期米国のロシア語科学文献翻訳需要と、計算機の応用拡張。",
    development="ALPACレポートで楽観論が打ち砕かれるが、MT研究の制度化の起点となった。",
    historical_context="1950年代計算機科学の応用拡大期。",
    primary_source_url=WIKI_EN+"Georgetown%E2%80%93IBM_experiment",
    primary_source_type="Wikipedia: Georgetown-IBM Experiment",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="IBM Model 1-5（Brown et al.）",
    name_en="Brown et al., IBM Models 1-5",
    name_original="The Mathematics of Statistical Machine Translation",
    period_key="構造主義・記述的翻訳学期",
    definition="1993年ピーター・ブラウン他「統計的機械翻訳の数学——パラメータ推定」(Computational Linguistics誌)。IBM Watsonチームが開発した5段階の統計的MTモデル（語アラインメント・歪曲・繁殖力等）。SMT時代の理論的基盤。",
    background="1990年代初頭IBM Watson研究所のSMTパラダイム確立。",
    development="モーゼス（Moses）SMTシステム、Och&Ney(2003)、現代NMT前史の理論基盤。",
    historical_context="1990年代計算言語学の統計革命期。",
    primary_source_url=WIKI_EN+"IBM_alignment_models",
    primary_source_type="Wikipedia: IBM Alignment Models",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"IBM Modelsは現代LLMの確率的言語モデルの直系祖先で、AI翻訳パラダイムの起点。",
        "related_ai_phenomenon":"LLM確率的言語モデル"}])

add(**C, name_ja="バーダナウ注意機構2014",
    name_en="Bahdanau et al., Attention (2014)",
    name_original="Neural Machine Translation by Jointly Learning to Align and Translate",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2014年ドミトリ・バーダナウ、KyungHyun Cho、Yoshua Bengio論文。NMTに注意機構（attention mechanism）を導入し、入力系列の関連部分にデコーダーが動的に注目する仕組みを提案。Transformerの直接的前駆。",
    background="2013-14年seq2seq encoder-decoderモデルの長文翻訳における情報ボトルネック問題。",
    development="2017年Vaswani et al.「Attention is All You Need」Transformer論文の理論的基盤。",
    historical_context="2010年代深層学習革命期。",
    primary_source_url=ARXIV+"1409.0473",
    primary_source_type="arXiv: Bahdanau et al. 2014 (NMT Attention)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"emerging",
        "rationale":"注意機構はLLM全体の基礎技術。翻訳タスクから生まれて全AI領域を変革した革命的概念。",
        "related_ai_phenomenon":"Transformerの起源"}])

add(**C, name_ja="Vaswani『Attention is All You Need』",
    name_en="Vaswani et al., Attention is All You Need (2017)",
    name_original="Attention Is All You Need",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2017年Google論文（NeurIPS 2017）。RNN・CNNを排除し自己注意機構（self-attention）のみで構成するTransformerアーキテクチャを提案。WMT 2014英独翻訳でSOTA達成、現代LLM・NMT全ての基盤となる革命的論文。",
    background="2014-16年NMTの計算効率と長距離依存問題の限界。",
    development="BERT、GPT、T5、mBART、NLLB等すべての現代LLMの基盤、AI翻訳の質的飛躍を実現。",
    historical_context="2010年代後半のTransformer革命期。",
    primary_source_url=ARXIV+"1706.03762",
    primary_source_type="arXiv: Vaswani et al. 2017 (Transformer)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"emerging",
        "rationale":"Transformerは現代AI翻訳・LLMの絶対的基盤、第四変容（AI時代）を定義する技術論文。",
        "related_ai_phenomenon":"LLM時代の到来"}])

add(**C, name_ja="NLLB-200（Meta）",
    name_en="NLLB-200 (Meta)",
    name_original="No Language Left Behind",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2022年Meta AI「No Language Left Behind」プロジェクト。200言語対応の単一NMTモデルを公開、低リソース言語（スワヒリ語・ベンガル語・ウルドゥー語等）の翻訳品質を大幅改善。AI翻訳の言語平等性への取り組み。",
    background="GPT・GoogleNMTの英語中心バイアス問題と、言語的平等の倫理要請。",
    development="低リソース言語MT研究、デジタル言語格差解消、ポストコロニアル翻訳論との実践的接続。",
    historical_context="2020年代AI倫理と多言語AI研究の隆盛期。",
    primary_source_url=ARXIV+"2207.04672",
    primary_source_type="arXiv: NLLB Team 2022",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"言語","status":"emerging",
        "rationale":"NLLBは低リソース言語のデジタル可視化を実現、ポストコロニアル翻訳論の技術的応答。",
        "related_ai_phenomenon":"低リソース言語MT"}],
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"言語多様性保全",
        "description":"NLLBは言語人類学の言語消滅問題への技術的応答。"}])

add(**C, name_ja="BLEU/METEOR/COMET評価指標",
    name_en="BLEU/METEOR/COMET evaluation metrics",
    name_original="BLEU: a Method for Automatic Evaluation of Machine Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2002年Papineni他BLEU、2005年Banerjee&Lavie METEOR、2020年Rei他COMETなどMT自動評価指標の系譜。n-gramマッチング→意味的類似度→学習済み評価モデルへと進化、現代AI翻訳評価の標準。",
    background="2000年代MT評価の人手依存問題と、自動評価指標の必要性。",
    development="MQMフレームワーク、BLEURT、人間並行評価論争、AI翻訳品質保証の理論基盤。",
    historical_context="2000-20年代MT評価指標の進化史。",
    primary_source_url=WIKI_EN+"BLEU",
    primary_source_type="Wikipedia: BLEU / MT evaluation metrics",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"自動評価指標は人間翻訳者の質判断の数値化試みで、AI時代翻訳評価の認識論的基盤。",
        "related_ai_phenomenon":"AI翻訳品質評価"}])

add(**C, name_ja="ポストエディット理論（MTPE）",
    name_en="Post-editing literacy (MTPE)",
    name_original="Post-editing Machine Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="MT出力を人間翻訳者が修正する実践（MTPE: Machine Translation Post-Editing）の理論。軽編集（light）・全編集（full）の区別、認知負荷研究、翻訳者労働の変容、AI時代の翻訳教育論を統合。",
    background="2010年代SMT・NMT実用化と、翻訳産業のMTPE業務への移行。",
    development="MTPEガイドライン（ISO 18587）、翻訳者労働経済学、翻訳教育のMTPE能力育成の基盤。",
    historical_context="2010-20年代翻訳産業のAI化期。",
    primary_source_url=WIKI_EN+"Postediting",
    primary_source_type="Wikipedia: Postediting",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[{"axis":"労働","status":"rethinking",
        "rationale":"MTPEは翻訳者労働の質的変容を象徴する。AI時代の知識労働全般のモデルケース。",
        "related_ai_phenomenon":"AI時代の知識労働変容"}])


# ============================================================
# H: Literary translation practice (6)
# ============================================================
add(**C, name_ja="グロスマン『なぜ翻訳が必要なのか』",
    name_en="Edith Grossman, Why Translation Matters",
    name_original="Why Translation Matters",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2010年エディス・グロスマン著、文学翻訳家の実践論。ガルシア・マルケス、リョサ等ラテンアメリカ文学英訳経験から、翻訳者の創造性と文化的責任を論じる。Yale University Pressの代表的翻訳論。",
    background="グロスマン自身のセルバンテス『ドン・キホーテ』新訳(2003)経験。",
    development="現代文学翻訳家エッセイの代表作、翻訳者可視化運動の理論基盤。",
    historical_context="2000年代英語圏文学翻訳の制度化期。",
    primary_source_url=WIKI_EN+"Edith_Grossman",
    primary_source_type="Wikipedia: Edith Grossman",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="パークス『文体翻訳』",
    name_en="Tim Parks, Translating Style",
    name_original="Translating Style: A Literary Approach to Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1997/2007年ティム・パークス著、英語からイタリア語への翻訳実践を文体論的に分析。D.H.ロレンス、ヴァージニア・ウルフ、ジョイス等のイタリア語訳の文体的選択を精緻に検討、文学翻訳実践理論の代表作。",
    background="パークス自身のイタリア在住翻訳者経験と、英伊文学翻訳実践。",
    development="現代文学翻訳実践論、翻訳教育のテキスト分析教材として広く使用。",
    historical_context="1990-2000年代文学翻訳実践論の成熟期。",
    primary_source_url=WIKI_EN+"Tim_Parks",
    primary_source_type="Wikipedia: Tim Parks",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ベルノフスキー『外国語』",
    name_en="Susan Bernofsky, Foreign Words",
    name_original="Foreign Words: Translator-Authors in the Age of Goethe",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2005年スーザン・ベルノフスキー著、ゲーテ時代のドイツ翻訳者＝作家の翻訳論を再構築。翻訳者ベルノフスキーは2010年代ローベルト・ヴァルザー全英訳プロジェクトの中心人物として、現代翻訳家可視化運動を牽引。",
    background="ベルノフスキーのコロンビア大学翻訳プログラムと、ヴァルザー作品再評価。",
    development="2020年PEN America Translation Awards、現代英語圏文学翻訳家ネットワークの理論的基盤。",
    historical_context="2010-20年代英語圏文学翻訳家可視化運動。",
    primary_source_url=WIKI_EN+"Susan_Bernofsky",
    primary_source_type="Wikipedia: Susan Bernofsky",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ドン・ミー・チョイ『翻訳・移民・人種』",
    name_en="Don Mee Choi, Translation, Migration, Race",
    name_original="Translation Is a Mode = Translation Is an Anti-neocolonial Mode",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2020年ドン・ミー・チョイ『翻訳は様式である＝翻訳は反新植民地様式である』。韓国詩人キム・ヘスン英訳経験から、翻訳を反植民地・反帝国的実践として理論化、翻訳者の人種化された身体を中心に置く。",
    background="2020年代北米アジア系翻訳家・詩人の可視化運動と、BLM後の人種批評の翻訳学への合流。",
    development="トランスナショナル・フェミニズム翻訳、ディアスポラ翻訳論の現代的展開。",
    historical_context="2020年代英語圏翻訳の脱植民地化運動。",
    primary_source_url=WIKI_EN+"Don_Mee_Choi",
    primary_source_type="Wikipedia: Don Mee Choi",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"人種・植民","status":"emerging",
        "rationale":"チョイ翻訳論はAI時代の人種化された翻訳労働への批判的応答の代表例。",
        "related_ai_phenomenon":"AI翻訳と人種化労働"}],
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"ディアスポラ人類学",
        "description":"チョイの反植民地翻訳論はディアスポラ人類学・人種批評と接続。"}])

add(**C, name_ja="ワインバーガー『王維を読む19の方法』",
    name_en="Eliot Weinberger, 19 Ways of Looking at Wang Wei",
    name_original="19 Ways of Looking at Wang Wei",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1987/2016年エリオット・ワインバーガー著、王維（8世紀唐）の四行詩「鹿柴」の19種類の英訳・仏訳を比較分析。古典中国詩の翻訳不可能性と多様性を実例で示した翻訳論の名著、文学翻訳教育の定番テキスト。",
    background="ワインバーガー自身のオクタビオ・パス英訳実践と、東洋詩学への関心。",
    development="比較翻訳論教育、中国古典詩英訳論、翻訳の多様性理論の標準テクスト。",
    historical_context="1980年代米国の中国古典文学受容期。",
    primary_source_url=WIKI_EN+"Eliot_Weinberger",
    primary_source_type="Wikipedia: Eliot Weinberger",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"19の翻訳の多様性は単一最適翻訳というMTの前提を根本から問い直す古典的思考実験。",
        "related_ai_phenomenon":"AI翻訳の多様性問題"}],
    cross_domain=[{"target_db":"PT","link_type":"shared_concept",
        "target_entity_name":"古典中国詩学",
        "description":"王維詩翻訳論は古典中国詩学（詩格・意境論）と接続する翻訳実践。"}])

add(**C, name_ja="サールス『翻訳の哲学』",
    name_en="Damion Searls, The Philosophy of Translation",
    name_original="The Philosophy of Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2024年デイミオン・サールス著、メルロ＝ポンティ現象学を翻訳実践に適用した哲学的翻訳論。翻訳を「身体化された読み（embodied reading）」として捉え、ハイデガー・フッサール・メルロ＝ポンティ・イェンセン現象学の翻訳論的読み直し。",
    background="サールス自身のドイツ語・ノルウェー語翻訳実践（フォッセ、リルケ等）。",
    development="2020年代英語圏翻訳家エッセイの代表作、現象学的翻訳論の現代的展開。",
    historical_context="2020年代英語圏文学翻訳家の哲学的成熟期。",
    primary_source_url=WIKI_EN+"Damion_Searls",
    primary_source_type="Wikipedia: Damion Searls",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"現象学的言語論",
        "description":"サールス翻訳論はメルロ＝ポンティ現象学の翻訳学的応用。"}])


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
        print(f"[wave18-c38-add60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave18-c38-add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
