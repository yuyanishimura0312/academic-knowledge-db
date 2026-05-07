"""
LIT-DB Phase 2 — C34 Wave 10: Theory Classical (Antiquity through 19th Century)
================================================================================
Classical, medieval, Renaissance, 17-18c, and 19c literary theory / criticism
(40 concepts).

Categories (8 each):
  A. 古代詩学 / Ancient poetics & rhetoric
  B. 中世・ルネサンス批評 / Medieval & Renaissance criticism
  C. 17-18世紀批評 / 17-18c criticism (Neoclassical / Enlightenment)
  D. 19世紀ロマン主義・理想主義批評 / 19c Romantic & Idealist criticism
  E. 19世紀後半批評 / Late-19c criticism (Arnold, Pater, Taine, etc.)

Sources (primary > secondary > tertiary):
  - Perseus Digital Library (Greek/Latin originals)
  - Project Gutenberg (English/French/German translations and originals)
  - Stanford Encyclopedia of Philosophy (SEP) for theoretical positions
  - JSTOR canonical articles for key works
  - Internet Archive scholarly editions
  - Bibliotheca Augustana for Latin/medieval texts

C34 covers 古代〜19世紀末. C35 (Russian Formalism onward) / C36 (Anglo-American
New Criticism+) / C37 (Gender/Postcolonial/Eco) handle 20-21c theory.

Pattern: P3 (Theory-driven Concept Cartography).
"""
from __future__ import annotations

import sys

from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (theory-region anchored to periods of theory)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    # name_ja, name_en, start, end, description
    ("古代詩学・修辞学期", "Ancient Poetics & Rhetoric", -400, 500,
     "プラトン、アリストテレスからローマ期の修辞学伝統、教父学までを含む古代の文学理論期。"),
    ("中世・ルネサンス批評期", "Medieval & Renaissance Criticism", 1200, 1600,
     "アクィナス、ダンテから16世紀イタリア・フランス・英国のルネサンス批評論を含む。"),
    ("17-18世紀新古典主義・啓蒙批評期", "Neoclassical & Enlightenment Criticism",
     1660, 1800,
     "ボワロー、ドライデン、ポープ、レッシング、バーク、カント、ヘルダー、ヴィーコらが詩学・美学・修辞学を制度化した時期。"),
    ("19世紀ロマン主義・理想主義批評期", "Romantic & Idealist Criticism",
     1798, 1860,
     "コールリッジ、ワーズワース、ヘーゲル、ショーペンハウアー、シラー、シュレーゲル、カーライル、サント＝ブーヴらが活躍した時期。"),
    ("19世紀後半批評期", "Late-19th-Century Criticism", 1860, 1900,
     "アーノルド、ペイター、テーヌ、ベリンスキー、シモンズ、ブリュンチエールらの批評期。"),
]


# ---------------------------------------------------------------
# Concept payload
# ---------------------------------------------------------------

CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — 古代詩学 / Ancient Poetics & Rhetoric (8)
# ===============================================================

add({
    "name_ja": "詩人追放論（『国家』第十巻）",
    "name_en": "Banishment of the Poets (Republic Book X)",
    "name_original": "Πολιτεία Ι",
    "original_script": "greek",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "古代詩学・修辞学期",
    "definition": "プラトン『国家』第十巻に展開された詩人批判論。詩はイデアの三段の隔たり（ミメーシス）に立つ模倣の模倣であり、魂の劣った部分に訴え情念を養うため、理想国家から叙事詩人・悲劇詩人を追放すべきだとされる。詩と哲学の「太古からの争い」を定式化し、虚構の倫理的・存在論的位置を西洋思想史において根本問題として打ち立てた。",
    "background": "プラトンのイデア論、魂の三分説、古代ギリシアの教育における詩人（ホメロス）の権威への対抗。",
    "development": "アリストテレス『詩学』が直接の応答。シドニー『詩の弁護』、シェリー『詩の弁護』ら詩擁護論の系譜を生み続ける。",
    "historical_context": "前4世紀アテナイ。ホメロスを「ヘラスの教師」とする伝統的教養観への哲学的挑戦。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0168%3Abook%3D10",
    "primary_source_type": "Perseus Digital Library — Plato Republic Book X (Greek)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "「模倣の模倣」というプラトンの虚構批判は、AI生成コンテンツが原物から二重三重に隔てられている現代の問題を予表する。何が真正な制作で、何が単なる影かという問いがAI時代に再活性化する。",
         "related_ai_phenomenon": "AI生成コンテンツの真正性論争・派生コンテンツの倫理"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "詩が魂の劣った部分（情念）を喚起するというプラトンの懸念は、AI生成物が人間の感情を操作するリスクへの倫理的議論と並行する。",
         "related_ai_phenomenon": "AI感情操作・パーソナライズドコンテンツの倫理"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "プラトンのミメーシス論",
         "description": "哲学DBのプラトン形而上学・芸術論と直接共有。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "ミメーシス（詩学）",
         "description": "詩学DBの古代ミメーシス概念の起点。"},
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "AI生成物の存在論的地位",
         "description": "AI生成物の真正性・派生性論争の古代的予表。"},
    ],
})

add({
    "name_ja": "アリストテレス詩学（理論側面）",
    "name_en": "Aristotle's Poetics (theoretical aspects)",
    "name_original": "Περὶ ποιητικῆς",
    "original_script": "greek",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "古代詩学・修辞学期",
    "definition": "アリストテレス『詩学』の理論的核心。詩を「行為のミメーシス（再現／模倣）」と定義し、悲劇を「ある一定の大きさを備えた完結した行為の模倣」と規定する。プラトンの詩人追放論への哲学的応答として、詩の認識論的価値（普遍を語る点で歴史より哲学的）を擁護した。カタルシス、ペリペテイア、アナグノリシスなど後代の批評の基本概念を提供。",
    "background": "前4世紀リュケイオンでの講義原稿。プラトンの『国家』への応答として、詩の自律的価値を論証する。",
    "development": "ルネサンス期に再発見され、カステルヴェトロらによる注釈伝統が三一致則など新古典主義詩学を生む。20世紀にはフライ、リクールらに継承される。",
    "historical_context": "アテナイ古典悲劇（ソフォクレス、エウリピデス）の鑑賞経験を理論化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0056",
    "primary_source_type": "Perseus Digital Library — Aristotle Poetics (Greek/English)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "アリストテレスは詩の創造性を「ミメーシス」として定式化し、無からの創造ではなく既存の世界の再構成として位置づけた。AI生成が学習データの再構成として機能するメカニズムは、このミメーシス論の現代的反復に近い。",
         "related_ai_phenomenon": "AI生成のミメーシス的構造（学習データ再組成）"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "「行為の模倣」「始まり・中・終わり」の物語構造論は、AIが物語を生成する際に基盤として参照される普遍的物語文法の理論的源泉。",
         "related_ai_phenomenon": "AIナラティブ生成の構造的限界とアリストテレス的形式"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "アリストテレスの形而上学・倫理学",
         "description": "哲学DBのアリストテレス哲学と詩学は連続的体系を成す。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "ミメーシス・カタルシス",
         "description": "詩学DBの根幹概念群を提供。"},
        {"target_db": "Myth-Narratives", "link_type": "parallel",
         "target_entity_name": "プロット構造論",
         "description": "神話分析DBの物語構造論の古代的源泉。"},
    ],
})

add({
    "name_ja": "ホラティウス『詩論』（理論側面）",
    "name_en": "Horace's Ars Poetica (theoretical aspects)",
    "name_original": "Ars Poetica",
    "original_script": "latin",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "古代詩学・修辞学期",
    "definition": "ホラティウス（前65-前8）が前1世紀末にピソ家に宛てた書簡形式の詩論（『書簡集』第二書第三書簡）。詩は「楽しませかつ教える」（dulce et utile）べきだと定式化し、適合（decorum）、自然と技巧の調和、「9年間の彫琢」など創作上の規準を提示。「ut pictura poesis（絵画のように詩は）」など後代の批評を導く格言を多数生む。",
    "background": "アウグストゥス時代のローマ。ギリシア詩学の伝統をローマの詩作実践と融合させる試み。",
    "development": "ルネサンスから18世紀新古典主義詩学（ボワロー、ポープ）まで批評の規範書として絶大な影響を及ぼす。",
    "historical_context": "アウグストゥス朝の詩人サークル（マエケナス・ホラティウス・ウェルギリウス）。",
    "primary_source_url": "https://www.thelatinlibrary.com/horace/arspoet.shtml",
    "primary_source_type": "The Latin Library — Horace Ars Poetica (Latin)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "parallel",
         "target_entity_name": "ストア派・エピクロス派の倫理",
         "description": "ホラティウスの「楽しませかつ教える」倫理は古代倫理学の文学的応用。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "decorum（適合）",
         "description": "詩学DBの古代修辞学・詩学の中核概念。"},
    ],
})

add({
    "name_ja": "ロンギノス『崇高について』（理論側面）",
    "name_en": "Longinus On the Sublime (theoretical aspects)",
    "name_original": "Περὶ ὕψους",
    "original_script": "greek",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "古代詩学・修辞学期",
    "definition": "1世紀頃の作とされる修辞学・詩学論文。崇高（hypsous）を「言葉の卓越」と定義し、それが読者を「説得」ではなく「忘我（ekstasis）」に至らしめる効果を論じる。崇高の五つの源泉として、偉大な思想の構想力、強烈な情念、適切な比喩、高貴な語法、荘厳な語法を挙げる。",
    "background": "ローマ帝政初期の修辞学伝統に位置づく。著者は「ロンギノス」と伝えられるが特定不能。",
    "development": "ボワローによる17世紀仏訳が西欧での再発見の契機。バーク、カントらの18世紀崇高論の源泉となる。",
    "historical_context": "ローマ帝政期ギリシア語修辞学の文脈で執筆。",
    "primary_source_url": "https://www.gutenberg.org/files/17957/17957-h/17957-h.htm",
    "primary_source_type": "Project Gutenberg — Longinus On the Sublime (English translation)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "崇高がもたらす「忘我（ekstasis）」という圧倒的読者体験のモデルは、AIが生成する大規模・高密度コンテンツへの読者反応を再考する基盤。AI生成の「崇高さ」あるいは情報過多による圧倒は、ロンギノスの問題系を新たな技術的環境で再活性化する。",
         "related_ai_phenomenon": "AI生成テキストにおける崇高・圧倒的体験"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "崇高（aesthetics）",
         "description": "哲学DBのカント・バークの崇高論の古代的源泉。"},
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "AI生成と崇高経験",
         "description": "AI発展DBの大規模生成体験論への古代的予表。"},
    ],
})

add({
    "name_ja": "キケロ修辞学",
    "name_en": "Cicero's rhetorical theory",
    "name_original": "De Oratore / Orator",
    "original_script": "latin",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "古代詩学・修辞学期",
    "definition": "キケロ（前106-前43）が『弁論家について』『弁論家』『発想論』などで展開した修辞学体系。ギリシア弁論術（特にアリストテレス、イソクラテス）をローマ的実践と融合させ、弁論家を「徳・知識・弁舌」を備えた完成された人間（orator perfectus）として理想化した。発想・配列・修辞・記憶・発音の五段階や、教える・楽しませる・動かす（docere/delectare/movere）の三機能を定式化。",
    "background": "共和制末期ローマの政治弁論実践。アカデメイア懐疑派とストア派の倫理的折衷。",
    "development": "クインティリアヌスへ直接継承。ルネサンスのキケロ主義（cicéronisme）として人文主義の中核となる。",
    "historical_context": "前1世紀ローマ。共和制崩壊期の政治的弁論文化。",
    "primary_source_url": "https://www.thelatinlibrary.com/cic.html",
    "primary_source_type": "The Latin Library — Cicero rhetorical works (Latin)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "キケロ哲学",
         "description": "哲学DBのキケロ折衷主義・倫理学と修辞学は連続体。"},
    ],
})

add({
    "name_ja": "クインティリアヌス『弁論家の教育』",
    "name_en": "Quintilian's Institutio Oratoria",
    "name_original": "Institutio Oratoria",
    "original_script": "latin",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "古代詩学・修辞学期",
    "definition": "クインティリアヌス（35頃-100頃）の修辞学全書（12巻）。弁論家の幼児教育から完成された徳の境地までを体系化し、「善き人にして弁論に巧みなる者」（vir bonus dicendi peritus）を弁論家像の理想とする。修辞論の伝統的五段階を網羅的に教説化し、ローマ古典作家の批評的概観（第10巻）も含む。中世から近代までの修辞学・教育論の標準書として機能。",
    "background": "ウェスパシアヌス帝下、ローマ初の国費教師に任命される。20年の教育実践の結晶。",
    "development": "1416年ポッジョ・ブラッチョリーニによるザンクト・ガレン修道院での全写本発見が人文主義教育論の起爆剤となる。",
    "historical_context": "ローマ帝政初期。第二次詭弁術期に対する古典主義的教育理念の擁護。",
    "primary_source_url": "https://www.thelatinlibrary.com/quintilian.html",
    "primary_source_type": "The Latin Library — Quintilian Institutio (Latin)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アウグスティヌス『キリスト教の教えについて』",
    "name_en": "Augustine's De Doctrina Christiana",
    "name_original": "De Doctrina Christiana",
    "original_script": "latin",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "古代詩学・修辞学期",
    "definition": "アウグスティヌス（354-430）が396-426年に執筆した4巻の教義論・解釈学・修辞学書。聖書解釈の方法（記号論・寓意的解釈・語学的素養）と、説教における古典修辞学の応用を論じる。記号（signum）と物（res）の区別を導入し、後代の記号論・解釈学（ヘルメネウティクス）の古代的源泉となった。古典修辞学を「キリスト教化」する歴史的画期。",
    "background": "古代修辞学の異教的伝統とキリスト教信仰の関係をめぐる教父神学の問題。",
    "development": "中世スコラ学の解釈学的伝統、ルネサンス聖書文献学、近代記号論（パース・ソシュール）の遠い源流。",
    "historical_context": "ローマ帝国末期の北アフリカ。古典文化からキリスト教文化への移行期。",
    "primary_source_url": "https://www.augustinus.it/latino/dottrina_cristiana/index.htm",
    "primary_source_type": "Augustinus.it — De Doctrina Christiana (Latin critical text)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "アウグスティヌスの言語論・記号論",
         "description": "哲学DBのアウグスティヌス神学・解釈学と直接共有。"},
    ],
})

add({
    "name_ja": "プルタルコス『若き者は詩をいかに聞くべきか』",
    "name_en": "Plutarch's How the Young Should Read Poetry",
    "name_original": "Πῶς δεῖ τὸν νέον ποιημάτων ἀκούειν",
    "original_script": "greek",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "古代詩学・修辞学期",
    "definition": "プルタルコス（46頃-120頃）の『モラリア』中の論考。若者がホメロスら古代詩人を読む際の倫理的・教育的指針を示し、詩の虚構性を認めつつそれを徳育に資する読み方の技術を論じる。プラトンの詩人追放に対する妥協的応答として、批判的読解（philological-ethical reading）の伝統を確立。古代における読者反応理論の重要文献。",
    "background": "プラトン主義者プルタルコスの教養論。前期ストア派・中期プラトン主義の融合。",
    "development": "中世から近代の道徳的詩学（moral poetics）、近代の児童文学論まで影響を及ぼす。",
    "historical_context": "ローマ帝政期ギリシア。第二次詭弁術期の文化的洗練。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2008.01.0140",
    "primary_source_type": "Perseus Digital Library — Plutarch Moralia (How to Study Poetry)",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY B — 中世・ルネサンス批評 / Medieval & Renaissance (8)
# ===============================================================

add({
    "name_ja": "アクィナスの美学",
    "name_en": "Aquinas's aesthetics",
    "name_original": "Summa Theologiae (selected articles)",
    "original_script": "latin",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "中世・ルネサンス批評期",
    "definition": "トマス・アクィナス（1225頃-1274）の『神学大全』I.39.8、II-II.180.2bほかに散在する美論。美（pulchrum）の三条件として「完全性（integritas）」「均衡（proportio／consonantia）」「明晰さ（claritas）」を提示し、美と善の存在論的同一性、感覚と知性の協働的把握を論じた。アリストテレス＝アヴィセンナ系統の存在論を聖書的創造論と統合する中世美学の頂点。",
    "background": "13世紀パリのアリストテレス受容、アラビア哲学（特にアヴィセンナ）の影響。",
    "development": "ジャック・マリタンの新トマス主義美学、ジェイムズ・ジョイス『若き芸術家の肖像』の理論的中軸となる。エーコ『中世の美学』の主題。",
    "historical_context": "13世紀パリ大学のスコラ哲学全盛期。神学的体系の中での美の位置づけ。",
    "primary_source_url": "https://www.corpusthomisticum.org/sth0000.html",
    "primary_source_type": "Corpus Thomisticum — Summa Theologiae (Latin)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "トマス・アクィナスの形而上学",
         "description": "哲学DBのスコラ哲学と直接共有される。"},
    ],
})

add({
    "name_ja": "ダンテ『俗語論』",
    "name_en": "Dante's De Vulgari Eloquentia",
    "name_original": "De Vulgari Eloquentia",
    "original_script": "latin",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "中世・ルネサンス批評期",
    "definition": "ダンテ・アリギエーリ（1265-1321）が1303-1305年頃にラテン語で執筆した未完の論考（2巻）。俗語（イタリア諸方言）の文学的尊厳を論証し、「光輝ある俗語（volgare illustre）」という超方言的詩語の理念を提示する。バベル神話を起点に言語の起源と方言分裂の歴史を語り、文学言語と政治的統一の関係を西欧で初めて理論化した記念碑的著作。",
    "background": "中世末イタリアにおける俗語文学（プロヴァンス詩、シチリア派、ストルノヴィスティ）の隆盛。",
    "development": "ベンボら16世紀イタリア言語論争の起点。19世紀ナショナリズム的言語論の先駆。",
    "historical_context": "13-14世紀イタリア。ラテン語普遍主義から俗語自覚への転換期。",
    "primary_source_url": "https://www.danteonline.it/italiano/opere.asp?idope=3",
    "primary_source_type": "Dante Online — De Vulgari Eloquentia (Latin critical text)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "中世言語哲学",
         "description": "哲学DBの中世言語論との接続。"},
    ],
})

add({
    "name_ja": "シドニー『詩の弁護』（理論側面）",
    "name_en": "Sidney's Defence of Poesy (theoretical aspects)",
    "name_original": "An Apology for Poetry / The Defence of Poesy",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "中世・ルネサンス批評期",
    "definition": "フィリップ・シドニー（1554-1586）が1579-1581年頃に執筆し1595年に出版された英国ルネサンス詩学の代表作。ステフェン・ガッソンの清教徒的詩攻撃への応答として、詩を「有徳の像を示す動的な絵画」と定義し、歴史と哲学の中間にあって両者を超える教育的価値を持つと擁護。「詩人の零落のないエデンの庭」など印象的修辞で詩擁護論の決定版を成す。",
    "background": "16世紀後半英国の清教徒的反演劇・反詩運動への対抗。スカリゲル、ミントゥルノ、フラカストロらイタリア・ルネサンス詩学の英国受容。",
    "development": "ベン・ジョンソン、ドライデン、シェリー『詩の弁護』を経て近代英文学批評の起点となる。",
    "historical_context": "エリザベス朝英国。宮廷詩人と清教徒の文化抗争。",
    "primary_source_url": "https://www.gutenberg.org/files/1962/1962-h/1962-h.htm",
    "primary_source_type": "Project Gutenberg — Sidney Defence of Poesy",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "カスティリオーネ『宮廷人の書』",
    "name_en": "Castiglione's Book of the Courtier",
    "name_original": "Il Libro del Cortegiano",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "中世・ルネサンス批評期",
    "definition": "バルダッサーレ・カスティリオーネ（1478-1529）が1528年に出版した4巻の対話篇。理想の宮廷人像を提示する過程で、文学・芸術・言語論を展開し、特に「スプレッツァトゥーラ（sprezzatura、努力を見せない優雅）」概念を芸術的振舞いの中核として定式化。プラトン主義的恋愛論を結末に置き、ルネサンス的全人教育（uomo universale）の文学的理想像を構築。",
    "background": "ウルビーノ宮廷（モンテフェルトロ家）での実体験。プラトン主義的フィレンツェ・ヒューマニズム。",
    "development": "16-17世紀全欧州の宮廷文化・礼儀作法書の規範。シェイクスピア、コルネイユらに影響。",
    "historical_context": "イタリア戦争期、宮廷文化が貴族倫理の中軸となる時期。",
    "primary_source_url": "https://www.liberliber.it/online/autori/autori-c/baldassarre-castiglione/il-libro-del-cortegiano/",
    "primary_source_type": "Liber Liber — Il Cortegiano (Italian critical text)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "タッソ『英雄詩論』",
    "name_en": "Tasso's Discourses on the Heroic Poem",
    "name_original": "Discorsi del poema eroico",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "中世・ルネサンス批評期",
    "definition": "トルクァート・タッソ（1544-1595）が1594年に出版した6巻の英雄詩論。アリストテレス『詩学』の三一致則・行為の単一性論をキリスト教時代の英雄詩（『解放されたエルサレム』）に応用する理論を展開。「驚異と真実」「歴史と虚構」「単一性と多様性」の調停を論じ、新古典主義詩学の代表的体系を樹立。",
    "background": "16世紀後半イタリアの反宗教改革期、トリエント公会議後のカトリック詩学の整備。",
    "development": "17世紀フランス新古典主義（ボワロー、ラシーヌ）の英雄詩論の理論的源泉。",
    "historical_context": "フェラーラ宮廷からローマへの移動期。詩人の内面的危機と教義的厳格化。",
    "primary_source_url": "https://www.bibliotecaitaliana.it/indice/visualizza_scheda/bibit000180",
    "primary_source_type": "Biblioteca Italiana — Discorsi del poema eroico (Italian)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "マッツォーニ『ダンテ詩学擁護』",
    "name_en": "Mazzoni's Defence of Dante",
    "name_original": "Della difesa della Commedia di Dante",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "中世・ルネサンス批評期",
    "definition": "ジャコモ・マッツォーニ（1548-1598）が1587-1688年に出版した『神曲』擁護論。アリストテレス『詩学』の枠組みを用いて、寓意的詩学の擁護と、詩を「想像可能な事物の模倣（imitazione delle cose imaginabili）」として再定義する。詩を哲学・歴史と区別する境界画定の理論として、後の幻想・フィクション論の先駆をなす。",
    "background": "16世紀イタリアのアリストテレス『詩学』注釈伝統。リドルフィーらの『神曲』批判への応答。",
    "development": "シドニーが直接参照、フィリップ・シドニー『詩の弁護』の理論的補強となる。バロック期幻想理論の先駆。",
    "historical_context": "16世紀後半イタリア。ダンテ復権運動と古典主義詩学の両立試み。",
    "primary_source_url": "https://archive.org/details/delladifesadella00mazz",
    "primary_source_type": "Internet Archive — Mazzoni Della difesa (1587 ed.)",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "デュ・ベレー『フランス語の擁護と顕揚』",
    "name_en": "Du Bellay's Defence and Illustration of French Language",
    "name_original": "Défense et illustration de la langue française",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "中世・ルネサンス批評期",
    "definition": "ジョアシャン・デュ・ベレー（1522頃-1560）が1549年に出版したプレイヤード派の宣言書。フランス語をギリシア・ラテンに比肩する文学言語として顕揚することを目指し、古典作家の「改造的模倣（innutrition）」「翻案・翻訳論」を展開。フランス国民文学の自己意識的形成の基礎文書として、近代の言語ナショナリズム文学論の出発点となる。",
    "background": "ロンサールを中心とするプレイヤード詩派の理論的綱領。スペローニ『言語論』のフランス的応用。",
    "development": "17世紀のマレルブ、ボワローを経て、19世紀ロマン派の言語論まで継承される。",
    "historical_context": "1549年フランス。ヴァロワ朝下、ラテン語からフランス語への文化的移行期。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b8602787r",
    "primary_source_type": "Gallica BnF — Défense et illustration (1549 ed.)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "スカリゲル『詩学』",
    "name_en": "Scaliger's Poetics",
    "name_original": "Poetices libri septem",
    "original_script": "latin",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "中世・ルネサンス批評期",
    "definition": "ユリウス・カエサル・スカリゲル（1484-1558）が1561年に出版した7巻の詩学論文。アリストテレス『詩学』を体系的に拡張し、ジャンル論・修辞学・古代詩人比較論・詩作技法論を網羅する。ホメロスよりウェルギリウスを上位に置く判断、悲劇の三一致則の厳格定式化など、ルネサンス末期のラテン語詩学の決定版を成し、近代新古典主義の理論的基盤となった。",
    "background": "16世紀イタリア＝フランスのアリストテレス注釈伝統。カステルヴェトロ、ロボルテッロらに次ぐ集大成。",
    "development": "17世紀フランス新古典主義（コルネイユ、ボワロー）の三一致則体系の直接的源泉。",
    "historical_context": "16世紀フランスのラテン語人文主義。アジャン在住期に執筆。",
    "primary_source_url": "https://archive.org/details/poeticeslibrise00scal",
    "primary_source_type": "Internet Archive — Scaliger Poetices (1561 ed.)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY C — 17-18世紀批評 / 17-18c Criticism (8)
# ===============================================================

add({
    "name_ja": "ボワロー『詩法』（理論側面）",
    "name_en": "Boileau's L'Art Poétique (theoretical aspects)",
    "name_original": "L'Art poétique",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "17-18世紀新古典主義・啓蒙批評期",
    "definition": "ニコラ・ボワロー＝デプレオー（1636-1711）が1674年に出版した4歌の韻文詩論。ホラティウス『詩論』をモデルに、フランス新古典主義の規則体系（理性、自然、bon sens、ジャンル区分、三一致則）を韻文で定式化。「正しく考えてからのみ正しく書ける」（Avant donc que d'écrire, apprenez à penser）など多数の格言を生み、17-18世紀全欧州の詩学規範書として機能した。",
    "background": "ルイ14世時代フランス古典主義の最盛期。ラシーヌ、モリエールらと並ぶ批評的代弁者の役割。",
    "development": "ポープ『批評論』、レッシング、英国新古典主義に直接影響。19世紀ロマン主義はその規則主義への反発として展開。",
    "historical_context": "ヴェルサイユ宮廷文化、王立アカデミーによる文学規範化の時期。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/bpt6k1042204j",
    "primary_source_type": "Gallica BnF — L'Art poétique (1674)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ドライデン『劇詩論』",
    "name_en": "Dryden's An Essay of Dramatic Poesy",
    "name_original": "An Essay of Dramatick Poesie",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "17-18世紀新古典主義・啓蒙批評期",
    "definition": "ジョン・ドライデン（1631-1700）が1668年に出版した対話篇形式の劇論。古代と近代、フランス古典主義と英国劇（特にシェイクスピア）の優劣を四人の対話者（ニアンダー＝ドライデン、ユージニウス、クリテス、リシディウス）を通じて検討。三一致則、押韻劇の妥当性、シェイクスピアの「最大の包括的魂」評価などを論じ、英国近代批評の創始的著作とされる。",
    "background": "王政復古期英国。フランス新古典主義の影響と、シェイクスピア＝英国劇場伝統との緊張。",
    "development": "サミュエル・ジョンソン『シェイクスピア序文』を経て、英国批評の対話的・歴史相対的伝統を確立。",
    "historical_context": "1660年代ロンドン、王政復古劇場の再開期。",
    "primary_source_url": "https://www.gutenberg.org/files/15349/15349-h/15349-h.htm",
    "primary_source_type": "Project Gutenberg — Dryden Essays",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ポープ『批評論』（理論側面）",
    "name_en": "Pope's Essay on Criticism (theoretical aspects)",
    "name_original": "An Essay on Criticism",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "17-18世紀新古典主義・啓蒙批評期",
    "definition": "アレクサンダー・ポープ（1688-1744）が1711年に出版した英雄連句体の批評論。ホラティウス、ボワローを範に、批評家の徳と陥穽、自然と古代、機知（wit）と判断（judgement）の関係を論じる。「致命的なのは少しの学問」（A little learning is a dangerous thing）、「人間に犯すは普通／神に許すは神の業」（To err is human, to forgive divine）など格言を多産。",
    "background": "アウグスタン期英文学の中軸詩人。アディソン『スペクテイター』の批評文化の中で執筆。",
    "development": "ジョンソン『英国詩人列伝』、ロマン派詩学と並びアウグスタン批評の代表として後代に影響。",
    "historical_context": "アン女王時代英国、新古典主義の頂点期。",
    "primary_source_url": "https://www.gutenberg.org/files/7409/7409-h/7409-h.htm",
    "primary_source_type": "Project Gutenberg — Pope Essay on Criticism",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "レッシング『ラオコオン』（理論側面）",
    "name_en": "Lessing's Laocoön (theoretical aspects)",
    "name_original": "Laokoon: oder über die Grenzen der Malerei und Poesie",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "17-18世紀新古典主義・啓蒙批評期",
    "definition": "ゴットホルト・エフライム・レッシング（1729-1781）が1766年に出版した美学論。古代彫刻ラオコオン群像とウェルギリウスの叙述を比較し、絵画は「空間における物体」、詩は「時間における行為」を媒体とすると論じる。「ut pictura poesis」を批判し、各芸術ジャンルの媒体特性に即した美学を確立。媒体特異性（medium-specificity）論の起点として近代美学の画期となった。",
    "background": "ヴィンケルマン『古代芸術史』への応答。ベルリン啓蒙主義の批評文化。",
    "development": "ヘーゲル美学、グリーンバーグのモダニズム媒体特異性論まで影響を及ぼす。",
    "historical_context": "ドイツ啓蒙期、ハンブルク劇場の批評家として執筆。",
    "primary_source_url": "https://www.projekt-gutenberg.org/lessing/laokoon/laokoon.html",
    "primary_source_type": "Projekt Gutenberg-DE — Lessing Laokoon",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "啓蒙美学",
         "description": "哲学DBのドイツ啓蒙美学（バウムガルテン・カント）への接続。"},
    ],
})

add({
    "name_ja": "バーク『崇高と美の起源』",
    "name_en": "Burke's Philosophical Enquiry into the Sublime and Beautiful",
    "name_original": "A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "17-18世紀新古典主義・啓蒙批評期",
    "definition": "エドマンド・バーク（1729-1797）が1757年に出版した美学論。崇高と美を心理学的・経験論的に区別し、崇高は「自己保存」に関わる恐怖・畏怖の感情に、美は「社会」に関わる愛・優しさの感情に根拠づけられると論じる。ロンギノス『崇高について』の近代的再解釈を実現し、ロマン主義美学の基礎を準備した。",
    "background": "ロック経験論、シャフツベリの徳論、英国感覚論的美学の伝統。",
    "development": "カント『判断力批判』の崇高論に直接影響。ワーズワース、ターナー、シェリー、ゴシック小説に波及。",
    "historical_context": "1750年代英国。啓蒙的美学の成熟期。",
    "primary_source_url": "https://www.gutenberg.org/files/15043/15043-h/15043-h.htm",
    "primary_source_type": "Project Gutenberg — Burke Sublime and Beautiful",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "崇高（aesthetics）",
         "description": "哲学DBの近代美学（カント崇高論への直接影響）。"},
    ],
})

add({
    "name_ja": "カント『判断力批判』（美学的側面）",
    "name_en": "Kant's Critique of Judgment (aesthetic aspects)",
    "name_original": "Kritik der Urteilskraft",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "17-18世紀新古典主義・啓蒙批評期",
    "definition": "イマヌエル・カント（1724-1804）が1790年に出版した第三批判書。趣味判断を「概念なしに普遍的に好まれる」「目的なき合目的性」として規定し、美の主観的妥当性論を確立。崇高の数学的・力学的区別、天才（Genie）論、芸術の自律性などを定式化し、近代美学・芸術哲学の枠組みを画定した。",
    "background": "シャフツベリ、バウムガルテン、バークの英国＝ドイツ美学伝統の批判的統合。",
    "development": "シラー、シェリング、ヘーゲルの観念論美学、19世紀芸術自律性論、20世紀フォルマリズムまで決定的影響。",
    "historical_context": "1790年ケーニヒスベルク。フランス革命期、啓蒙の頂点で執筆。",
    "primary_source_url": "https://www.projekt-gutenberg.org/kant/kuk/kuk.html",
    "primary_source_type": "Projekt Gutenberg-DE — Kant Kritik der Urteilskraft",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "カント美学・判断力批判",
         "description": "哲学DBのカント批判哲学の核心。"},
    ],
})

add({
    "name_ja": "ヘルダーの民族精神（フォルクスガイスト）",
    "name_en": "Herder's Volksgeist",
    "name_original": "Volksgeist",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "17-18世紀新古典主義・啓蒙批評期",
    "definition": "ヨハン・ゴットフリート・ヘルダー（1744-1803）が『言語起源論』（1772）、『人類歴史哲学考』（1784-1791）などで展開した概念。各民族はそれぞれ固有の「民族精神（Volksgeist）」を持ち、それが言語・文学・芸術・慣習に表現されると主張。普遍主義的啓蒙批評（ヴォルテール、レッシング）に対抗し、文学の歴史的・文化的相対性論を確立した。比較文学・国民文学概念の理論的源泉。",
    "background": "ハーマン、シャフツベリの影響下でのドイツ初期ロマン主義の準備期。古代フォークソング・聖書文学への注目。",
    "development": "グリム兄弟、ロマン主義国民文学論、19世紀ナショナリズム的文学史記述、20世紀フォークロア研究の根。",
    "historical_context": "プロイセン・ザクセン期、リガ・ヴァイマルでの執筆。",
    "primary_source_url": "https://www.projekt-gutenberg.org/herder/sprspr/sprspr.html",
    "primary_source_type": "Projekt Gutenberg-DE — Herder Über den Ursprung der Sprache",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "「民族精神」という集合的主体概念は、AI（特にLLM）が訓練データに内在するcultural biasを通じて特定の民族・言語の「精神」を増幅・固定化するメカニズムと並行する。AI時代の文化的代表性問題はヘルダー的問題系の再活性化。",
         "related_ai_phenomenon": "LLMにおけるcultural bias、訓練データの民族言語的偏向"},
        {"axis": "言語", "status": "rethinking",
         "rationale": "言語と民族精神の同一性論は、英語中心のLLMが他言語民族の「精神」を翻訳・再構成する現代的問題と直結する。",
         "related_ai_phenomenon": "AIによる言語間翻訳と文化的均質化"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ヘルダーの歴史哲学",
         "description": "哲学DBのヘルダー歴史哲学・言語哲学と直接共有。"},
        {"target_db": "AN", "link_type": "borrowed_from",
         "target_entity_name": "民族・文化概念",
         "description": "人類学DBの民族・文化概念の前史的源泉。"},
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "LLM cultural bias",
         "description": "AI発展DBの文化バイアス問題への概念的予表。"},
    ],
})

add({
    "name_ja": "ヴィーコ『新しい学』",
    "name_en": "Vico's New Science",
    "name_original": "Scienza Nuova",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "17-18世紀新古典主義・啓蒙批評期",
    "definition": "ジャンバッティスタ・ヴィーコ（1668-1744）が1725-1744年に三版にわたり出版した歴史哲学・文学起源論。「人間史」を神々の時代・英雄の時代・人間の時代の循環的展開として描き、初期人類が「詩的知恵（sapienza poetica）」によって世界を理解したとする。神話・隠喩・象徴を歴史認識の根源的様態として位置づけ、デカルト的合理主義に対抗する人文学的認識論を樹立した。",
    "background": "ナポリの古典学者・修辞学教授。デカルト主義への対抗、ホメロス問題への独自的応答。",
    "development": "ミシュレ、コールリッジ、ジョイス『フィネガンズ・ウェイク』、20世紀のクローチェ、ベンヤミン、ノースロップ・フライらに影響。",
    "historical_context": "18世紀前半ナポリ。スペイン＝オーストリア継承戦争期。",
    "primary_source_url": "https://www.bibliotecaitaliana.it/indice/visualizza_scheda/bibit000209",
    "primary_source_type": "Biblioteca Italiana — Scienza Nuova (1744 ed.)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ヴィーコの歴史哲学",
         "description": "哲学DBのヴィーコ哲学と直接共有。"},
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "詩的知恵・神話的思考",
         "description": "神話分析DBの神話的思考論への古典的源泉。"},
    ],
})


# ===============================================================
# CATEGORY D — 19世紀ロマン主義・理想主義 (8)
# ===============================================================

add({
    "name_ja": "コールリッジ『文学的自伝』（理論側面）",
    "name_en": "Coleridge's Biographia Literaria (theoretical aspects)",
    "name_original": "Biographia Literaria",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀ロマン主義・理想主義批評期",
    "definition": "サミュエル・テイラー・コールリッジ（1772-1834）が1817年に出版した自伝兼批評論。「想像力（Imagination）」と「空想力（Fancy）」の有名な区別、第一次想像力（一切の人間知覚の生命力）と第二次想像力（詩的創造）の階層、「不信の自発的停止（willing suspension of disbelief）」概念を提示。ドイツ観念論（特にシェリング）の英国受容を実現し、英国ロマン主義批評の理論的基盤を樹立した。",
    "background": "シェリング、フィヒテのドイツ観念論を英国ロマン主義詩学に統合。ワーズワースとの友情と決裂期に執筆。",
    "development": "I.A.リチャーズ『コールリッジによる想像力論』を経て20世紀英米ニュー・クリティシズムに継承。",
    "historical_context": "1810年代後半英国、ロマン主義の成熟期。",
    "primary_source_url": "https://www.gutenberg.org/files/6081/6081-h/6081-h.htm",
    "primary_source_type": "Project Gutenberg — Coleridge Biographia Literaria",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "borrowed_from",
         "target_entity_name": "シェリング観念論",
         "description": "哲学DBのドイツ観念論を英国批評に橋渡し。"},
    ],
})

add({
    "name_ja": "ワーズワース『抒情民謡集』序文（理論版）",
    "name_en": "Wordsworth's Preface to Lyrical Ballads (theoretical version)",
    "name_original": "Preface to Lyrical Ballads",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀ロマン主義・理想主義批評期",
    "definition": "ウィリアム・ワーズワース（1770-1850）が1800年（拡張版1802年）に『抒情民謡集』第二版に付した序文。詩を「強い感情の自発的な溢出（spontaneous overflow of powerful feelings）が静謐に再想起されたもの」と定義し、詩語と「人間が普通に話す言葉」の連続性を擁護。新古典主義的詩語（poetic diction）を批判し、英国ロマン主義詩学の宣言文として機能した。",
    "background": "コールリッジとの共著『抒情民謡集』（1798）の理論的補足。フランス革命の幻滅期。",
    "development": "コールリッジ『文学的自伝』が直接の応答・批判。19-20世紀の口語性・日常言語の詩学全般の出発点。",
    "historical_context": "1800年前後英国湖水地方、フランス革命後の保守化期。",
    "primary_source_url": "https://www.bartleby.com/39/36.html",
    "primary_source_type": "Bartleby — Wordsworth Preface to Lyrical Ballads",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ヘーゲル『美学講義』",
    "name_en": "Hegel's Lectures on Aesthetics",
    "name_original": "Vorlesungen über die Ästhetik",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀ロマン主義・理想主義批評期",
    "definition": "G.W.F.ヘーゲル（1770-1831）が1820-1829年にベルリン大学で行った美学講義（H.ホトーの編集により1835-1838年公刊）。芸術を「絶対精神の感性的顕現」と規定し、象徴的芸術（古代オリエント）・古典的芸術（古代ギリシア）・ロマン的芸術（キリスト教時代）の三段階弁証法を展開。「芸術の終焉（Ende der Kunst）」テーゼで近代における芸術の哲学的地位を問題化し、芸術史哲学の頂点を成した。",
    "background": "ベルリン大学哲学教授時代。シェリング、シラー、F.シュレーゲルらドイツ観念論美学の集大成。",
    "development": "20世紀のルカーチ、アドルノ、フライらの歴史的形式論、現代の「芸術の終焉」論（ダントー）まで継承。",
    "historical_context": "1820年代ベルリン、復古期プロイセン。",
    "primary_source_url": "https://www.projekt-gutenberg.org/hegel/aestheti/aestheti.html",
    "primary_source_type": "Projekt Gutenberg-DE — Hegel Vorlesungen über die Ästhetik",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ヘーゲル絶対精神論",
         "description": "哲学DBのヘーゲル弁証法・歴史哲学と直接共有。"},
    ],
})

add({
    "name_ja": "ショーペンハウアーの芸術論",
    "name_en": "Schopenhauer on art",
    "name_original": "Die Welt als Wille und Vorstellung (Buch III)",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀ロマン主義・理想主義批評期",
    "definition": "アルトゥール・ショーペンハウアー（1788-1860）が『意志と表象としての世界』（1819）第三巻で展開した芸術論。芸術を「イデアの観想」とし、意志による生の苦悩からの一時的解放と位置づける。芸術ジャンルを建築・彫刻・絵画・詩・音楽の階層的順序で配し、特に音楽を「意志そのものの直接的客体化」として最高位に置く。文学では悲劇を最高ジャンルとする悲劇論を展開した。",
    "background": "プラトンのイデア論、カント物自体論、ヒンドゥー・仏教思想の融合的形而上学。",
    "development": "ワーグナー、ニーチェ初期、トーマス・マン、プルースト、ベケットら近代芸術理論・実践への深甚な影響。",
    "historical_context": "1810-1850年代ドイツ。観念論凋落期、「悲観主義哲学」の登場。",
    "primary_source_url": "https://www.projekt-gutenberg.org/schopenh/wille1/wille1.html",
    "primary_source_type": "Projekt Gutenberg-DE — Schopenhauer Welt als Wille und Vorstellung",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ショーペンハウアー意志論",
         "description": "哲学DBのショーペンハウアー形而上学と直接共有。"},
    ],
})

add({
    "name_ja": "シラー『人間の美的教育について』",
    "name_en": "Schiller's On the Aesthetic Education of Man",
    "name_original": "Über die ästhetische Erziehung des Menschen",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀ロマン主義・理想主義批評期",
    "definition": "フリードリヒ・シラー（1759-1805）が1795年に出版した27通の書簡。フランス革命の挫折を踏まえ、政治的自由の前提として「美的状態（ästhetischer Zustand）」を介する人間の全人的教育を説く。「形式衝動」と「素材衝動」を媒介する「遊戯衝動（Spieltrieb）」を芸術の本質とし、「人間は遊戯するときにのみ完全に人間である」と論じた。",
    "background": "イェナでのカント批判哲学受容、フランス革命の暴力化への応答。",
    "development": "ドイツ観念論美学・教育論の中核、20世紀のホイジンガ『ホモ・ルーデンス』、マルクーゼまで継承。",
    "historical_context": "1790年代後半イェナ、ヴァイマル古典主義の理論的中心期。",
    "primary_source_url": "https://www.projekt-gutenberg.org/schiller/aesterz/aesterz.html",
    "primary_source_type": "Projekt Gutenberg-DE — Schiller Ästhetische Erziehung",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シュレーゲル『アテネーウム断片集』",
    "name_en": "Schlegel's Athenaeum Fragments",
    "name_original": "Athenäums-Fragmente",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀ロマン主義・理想主義批評期",
    "definition": "フリードリヒ・シュレーゲル（1772-1829）が兄アウグスト・ヴィルヘルムと共に1798-1800年に発行した雑誌『アテネーウム』に発表した断章群。「ロマン的詩は進歩的普遍詩（progressive Universalpoesie）」、ロマン的アイロニー、批評と詩の不可分性、ジャンル混淆の理念を断片形式で提示。イェナ・ロマン派の理論的綱領であり、断片自体が新たな批評形式として模範を示した。",
    "background": "ノヴァーリス、シェリング、ティーク、シュライアーマッハーらイェナ・サークル。",
    "development": "20世紀のベンヤミン『ドイツ・ロマン主義における芸術批評の概念』、デコンストラクション批評、ブランショの断片論まで継承。",
    "historical_context": "1798-1800年イェナ、ドイツ初期ロマン主義の最盛期。",
    "primary_source_url": "https://www.zeno.org/Literatur/M/Schlegel,+Friedrich/Theoretische+Schriften/Athen%C3%A4ums-Fragmente",
    "primary_source_type": "Zeno.org — Schlegel Athenäums-Fragmente",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "カーライル英雄論",
    "name_en": "Carlyle's hero theory",
    "name_original": "On Heroes, Hero-Worship, and the Heroic in History",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀ロマン主義・理想主義批評期",
    "definition": "トマス・カーライル（1795-1881）が1840年の連続講演を1841年に出版した英雄論。「歴史は偉大な人物の伝記の合計」と論じ、「神性としての英雄」「予言者としての英雄」「詩人としての英雄」「教師としての英雄」「文人としての英雄」「王としての英雄」の六類型を提示。文学を歴史的・道徳的に読む英雄主義的批評（特に詩人の予言者的役割）を確立した。",
    "background": "ドイツ観念論（フィヒテ、シラー、ゲーテ）の英国受容。産業革命期の精神的危機への応答。",
    "development": "ヴィクトリア朝批評、ニーチェ超人論、20世紀偉人史観への直接的影響、後にマルクス主義からの強烈な批判対象。",
    "historical_context": "1830-40年代ロンドン、産業革命と社会変革期。",
    "primary_source_url": "https://www.gutenberg.org/files/1091/1091-h/1091-h.htm",
    "primary_source_type": "Project Gutenberg — Carlyle On Heroes",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "サント＝ブーヴ伝記批評",
    "name_en": "Sainte-Beuve's biographical criticism",
    "name_original": "critique biographique",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀ロマン主義・理想主義批評期",
    "definition": "シャルル＝オーギュスタン・サント＝ブーヴ（1804-1869）が『月曜閑談（Causeries du lundi）』など1840-1860年代の連載で確立した批評方法。文学作品を作家の生涯・気質・社会環境から説明する伝記＝心理学的批評を体系化した。「樹木の認識は果実から得られる」というモデルで、テクストを作家人格の徴表として読む方法論を実定し、19世紀フランス批評の主流を成した。",
    "background": "ロマン主義の自我中心的詩学、イポリット・テーヌの実証主義との交錯。",
    "development": "プルースト『サント＝ブーヴに反対して』が直接的批判、20世紀ロシア・フォルマリズム、ニュー・クリティシズム、構造主義（バルト「作者の死」）の主たる批判対象として位置づく。",
    "historical_context": "1840-1860年代フランス第二帝政期、新聞批評文化の最盛期。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/bpt6k207242m",
    "primary_source_type": "Gallica BnF — Causeries du Lundi",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "「作品を作家の生涯・人格から説明する」というサント＝ブーヴの方法論は、AI生成物に「作者」を見出そうとする現代の試みと反転的に対応する。AI時代における「作者なきテクスト」の問題は、サント＝ブーヴ的伝記批評の前提（作品＝作者人格の徴表）を根底から揺るがす。",
         "related_ai_phenomenon": "AI生成テクストの作者性問題、伝記批評の現代的限界"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "AI生成と作者性",
         "description": "AI発展DBの作者性論議への概念的反転。"},
    ],
})


# ===============================================================
# CATEGORY E — 19世紀後半批評 / Late-19c Criticism (8)
# ===============================================================

add({
    "name_ja": "アーノルド「批評の機能」",
    "name_en": "Arnold's Function of Criticism",
    "name_original": "The Function of Criticism at the Present Time",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀後半批評期",
    "definition": "マシュー・アーノルド（1822-1888）が1864年に発表した批評論文。批評を「世界で考えられ語られた最善のものを学び広める無私の努力（disinterested endeavour to learn and propagate the best）」と定義し、「物事をあるがままに見る」批評の自律性と教養（culture）の社会的役割を主張。英国功利主義的・党派的批評を批判し、欧州的視野からの批評的高度化を呼びかけた。",
    "background": "ヴィクトリア朝中期の宗教的・社会的危機、フランス批評（サント＝ブーヴ、ルナン）への応答。",
    "development": "T.S.エリオット『伝統と個人的才能』、F.R.リーヴィス、ニュー・クリティシズムを経て20世紀英米批評の理論的基礎の一つ。",
    "historical_context": "1860年代英国、ヴィクトリア朝中期の文化論争期。",
    "primary_source_url": "https://www.gutenberg.org/files/12628/12628-h/12628-h.htm",
    "primary_source_type": "Project Gutenberg — Arnold Essays in Criticism",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アーノルド試金石批評",
    "name_en": "Arnold's touchstones",
    "name_original": "touchstones",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀後半批評期",
    "definition": "マシュー・アーノルドが「詩の研究（The Study of Poetry, 1880）」で提示した批評方法。ホメロス、ダンテ、シェイクスピア、ミルトンらの「最高の卓越」を持つ短い詩行を「試金石（touchstones）」とし、新たな詩を評価する基準とする手法。歴史的相対主義（historic estimate）と個人的偏愛（personal estimate）を超えた「真の評価（real estimate）」を可能にする道具として提示された。",
    "background": "1879年T.H.ウォードのアンソロジー序文として執筆。アーノルドの批評的成熟期。",
    "development": "T.S.エリオットの「歴史的感覚」、リーヴィス「偉大な伝統」など20世紀英米キャノン論の方法的源泉。",
    "historical_context": "1880年代英国、ヴィクトリア朝後期の批評文化。",
    "primary_source_url": "https://www.gutenberg.org/files/12628/12628-h/12628-h.htm",
    "primary_source_type": "Project Gutenberg — Arnold Essays in Criticism (Second Series)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ペイター『ルネサンス』",
    "name_en": "Pater's The Renaissance",
    "name_original": "Studies in the History of the Renaissance",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀後半批評期",
    "definition": "ウォルター・ペイター（1839-1894）が1873年に出版した美術・文学批評集。結論章（Conclusion）で「すべての芸術は音楽の状態を絶えず希求する」「この硬く宝石のような炎で常に燃え続けること、この恍惚を保つこと、こそが人生における成功」と論じ、印象主義的批評と唯美主義（aestheticism）の理論的綱領を提示。芸術を経験の濃密化として捉える「芸術のための芸術」運動の中核文書。",
    "background": "ラファエル前派、ラスキン批評の発展形。オックスフォード美学運動の理論的指導。",
    "development": "ワイルド、シモンズらデカダン派批評、初期モダニズム（ジョイス、エリオット、ウルフ）に深甚な影響。",
    "historical_context": "1870-90年代英国、ヴィクトリア朝後期の美学運動全盛期。",
    "primary_source_url": "https://www.gutenberg.org/files/2398/2398-h/2398-h.htm",
    "primary_source_type": "Project Gutenberg — Pater The Renaissance",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "テーヌ三要素批評（人種・環境・時代）",
    "name_en": "Taine's race-milieu-moment criticism",
    "name_original": "race, milieu, moment",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀後半批評期",
    "definition": "イポリット・テーヌ（1828-1893）が『英文学史』（1864）序論ほかで定式化した実証主義的文学史論。文学作品を「人種（race）・環境（milieu）・時代（moment）」の三要素の合力として説明する決定論的方法。コント実証主義、ダーウィン進化論の影響下に、文学を自然科学的因果連鎖の対象とする19世紀後半最も影響力のある批評方法を樹立した。",
    "background": "オーギュスト・コント実証主義、ダーウィン進化論の文学史への応用。",
    "development": "ブリュンチエール、19世紀後半フランス文学史記述の標準枠組み。20世紀のロシア・フォルマリズム、ニュー・クリティシズムの主たる批判対象。",
    "historical_context": "1860-80年代フランス第二帝政・第三共和制初期、実証主義の全盛期。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/bpt6k29659v",
    "primary_source_type": "Gallica BnF — Taine Histoire de la littérature anglaise",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ベリンスキーのリアリズム批評",
    "name_en": "Belinsky's realist criticism",
    "name_original": "реалистическая критика",
    "original_script": "cyrillic",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀後半批評期",
    "definition": "ヴィッサリオン・ベリンスキー（1811-1848）が『祖国雑記』『現代人』誌の年次概観などで展開した社会意識的リアリズム批評。文学を「社会の鏡」「時代精神の表現」と捉え、ゴーゴリ、レールモントフ、初期ドストエフスキーの社会批判性を高く評価した。「自然派（natural school）」概念を提唱し、ロシア19世紀リアリズム文学とその批評の理論的基盤を樹立。後のチェルヌィシェフスキー、ドブロリューボフら革命的民主主義批評の祖となる。",
    "background": "ヘーゲル左派、フィヒテ実践哲学のロシア受容、農奴制ロシアの社会的危機。",
    "development": "チェルヌィシェフスキー『現実に対する芸術の美学的諸関係』、20世紀ソヴィエト社会主義リアリズム批評の前史。",
    "historical_context": "1830-40年代モスクワ・ペテルブルク、ニコライ1世期。",
    "primary_source_url": "https://az.lib.ru/b/belinskij_w_g/",
    "primary_source_type": "Lib.ru — Belinsky collected works (Russian)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ペイターの印象主義批評",
    "name_en": "Pater's impressionist criticism",
    "name_original": "impressionist criticism",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀後半批評期",
    "definition": "ウォルター・ペイターが『ルネサンス』序文（1873）で定式化した批評方法。「批評の対象は、それが私にとって何であるか、それが私にどのような印象を生むかを知ること」と主張し、批評家の主観的印象を批評の中核に据える。アーノルドの「物事をあるがままに見る」客観主義への対抗的位置を取り、「すべての芸術批評は、ある意味では作家自身の自伝の一部である」（ワイルドが継承する命題）の源泉となる。",
    "background": "ラスキン批評からの脱出、唯美主義運動の理論的核。",
    "development": "オスカー・ワイルド「批評家としての芸術家」（1891）、シモンズ『象徴主義文学運動』（1899）に直接継承。",
    "historical_context": "1870-90年代英国、ヴィクトリア朝後期。",
    "primary_source_url": "https://www.gutenberg.org/files/2398/2398-h/2398-h.htm",
    "primary_source_type": "Project Gutenberg — Pater The Renaissance Preface",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "「印象」を批評の中核とするペイターの方法は、AI読書補助・パーソナライズド批評が個人の「印象」を計算する現代と直結する。批評の主観性をどう機械的に再構築するかという問題系の出発点。",
         "related_ai_phenomenon": "AIによるパーソナライズド批評・読書印象の計算的生成"},
    ],
})

add({
    "name_ja": "シモンズ『象徴主義文学運動』",
    "name_en": "Symons's Symbolist Movement in Literature",
    "name_original": "The Symbolist Movement in Literature",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀後半批評期",
    "definition": "アーサー・シモンズ（1865-1945）が1899年に出版した批評書。ネルヴァル、ヴィリエ、ランボー、ヴェルレーヌ、ラフォルグ、マラルメ、メーテルランクら19世紀フランス・ベルギー詩人を「象徴主義（Symbolism）」として体系化し、英語圏に紹介。「象徴主義文学は、夢の文学である。それは形式の暴政から解放され、超越的なものへと向かう」とし、英米モダニズム（イェイツ、エリオット、ジョイス、パウンド）の理論的予告となった。",
    "background": "ペイター唯美主義の延長、フランス象徴主義詩学の英国紹介。",
    "development": "イェイツの神秘主義詩学、エリオット『荒地』、英米モダニズム批評の理論的橋渡し。",
    "historical_context": "1890年代末ロンドン、世紀末（fin de siècle）の文化的雰囲気。",
    "primary_source_url": "https://www.gutenberg.org/files/35861/35861-h/35861-h.htm",
    "primary_source_type": "Project Gutenberg — Symons The Symbolist Movement",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ブリュンチエール歴史的批評",
    "name_en": "Brunetière's historical criticism",
    "name_original": "critique historique",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "19世紀後半批評期",
    "definition": "フェルディナン・ブリュンチエール（1849-1906）が『フランス文学における諸ジャンルの進化』（1890）などで定式化した実証主義的批評論。テーヌの三要素批評にダーウィン進化論を加え、文学ジャンルが生物種のように発生・成熟・衰退・絶滅の進化過程をたどると主張。19世紀末フランス文学史記述の主流方法を確立し、印象主義批評（フランス、ルメートル）に対抗する科学的批評の旗手となった。",
    "background": "テーヌ実証主義、ダーウィン進化論の文学史への徹底的応用。",
    "development": "20世紀のロシア・フォルマリズム、ジャンル理論（フライ、トドロフ）が継承的に批判的に発展。",
    "historical_context": "1880-1900年代フランス第三共和制、実証主義の最盛期から凋落期。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/bpt6k207216v",
    "primary_source_type": "Gallica BnF — Brunetière L'évolution des genres",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ---------------------------------------------------------------
# Relations payload (sequential after concepts inserted)
# ---------------------------------------------------------------
RELATIONS: list[tuple[str, str, str, str]] = [
    # A. Ancient internal
    ("詩人追放論（『国家』第十巻）", "アリストテレス詩学（理論側面）", "influences",
     "プラトンの詩人批判への直接的応答としてアリストテレスの『詩学』が位置づく。"),
    ("アリストテレス詩学（理論側面）", "ホラティウス『詩論』（理論側面）", "influences",
     "アリストテレス詩学のローマ的応用としてのホラティウス。"),
    ("アリストテレス詩学（理論側面)", "ロンギノス『崇高について』（理論側面）", "influences",
     "詩学の枠組みの中でロンギノスが崇高論を独立的に展開（影響関係は緩やか）。"),
    ("キケロ修辞学", "クインティリアヌス『弁論家の教育』", "influences",
     "クインティリアヌスはキケロ修辞学の体系的継承者。"),
    ("キケロ修辞学", "アウグスティヌス『キリスト教の教えについて』", "influences",
     "アウグスティヌスは古典修辞学（特にキケロ）をキリスト教化する。"),
    ("アリストテレス詩学（理論側面）", "プルタルコス『若き者は詩をいかに聞くべきか』", "influences",
     "プルタルコスはアリストテレス的詩学を倫理教育的に応用する。"),

    # B. Medieval/Renaissance internal
    ("アリストテレス詩学（理論側面）", "アクィナスの美学", "influences",
     "アクィナスはアリストテレス美学をスコラ学的に展開する。"),
    ("アリストテレス詩学（理論側面）", "スカリゲル『詩学』", "extends",
     "スカリゲル『詩学』はアリストテレス『詩学』のルネサンス的拡張。"),
    ("アリストテレス詩学（理論側面）", "タッソ『英雄詩論』", "extends",
     "タッソはアリストテレス詩学を英雄詩に応用する。"),
    ("ホラティウス『詩論』（理論側面）", "シドニー『詩の弁護』（理論側面）", "influences",
     "シドニーはホラティウスの「楽しませかつ教える」を中軸に据える。"),
    ("ホラティウス『詩論』（理論側面）", "スカリゲル『詩学』", "influences",
     "スカリゲルはホラティウスの規範を体系化する。"),
    ("詩人追放論（『国家』第十巻）", "シドニー『詩の弁護』（理論側面）", "criticizes",
     "シドニーはプラトンの詩人追放論への古典的応答として弁護論を展開する。"),
    ("ダンテ『俗語論』", "デュ・ベレー『フランス語の擁護と顕揚』", "influences",
     "ダンテの俗語顕揚論はデュ・ベレーのフランス語論の遠源となる。"),
    ("マッツォーニ『ダンテ詩学擁護』", "シドニー『詩の弁護』（理論側面）", "influences",
     "マッツォーニのダンテ擁護論はシドニーの詩擁護論の理論的補強となる。"),

    # C. 17-18c internal
    ("ホラティウス『詩論』（理論側面）", "ボワロー『詩法』（理論側面）", "influences",
     "ボワローはホラティウス『詩論』をモデルに新古典主義詩学を韻文化する。"),
    ("スカリゲル『詩学』", "ボワロー『詩法』（理論側面）", "influences",
     "スカリゲルの三一致則体系がボワローの規則主義の前提となる。"),
    ("ボワロー『詩法』（理論側面）", "ポープ『批評論』（理論側面）", "influences",
     "ポープはボワロー詩法の英語的継承者。"),
    ("ホラティウス『詩論』（理論側面）", "ポープ『批評論』（理論側面）", "influences",
     "ポープはホラティウスを直接的範とする。"),
    ("ボワロー『詩法』（理論側面）", "ドライデン『劇詩論』", "criticizes",
     "ドライデンはフランス新古典主義（ボワロー）に対しシェイクスピア＝英国劇場の独自性を擁護する。"),
    ("ロンギノス『崇高について』（理論側面）", "バーク『崇高と美の起源』", "influences",
     "ロンギノスの崇高論がバークの近代的崇高心理学の源泉。"),
    ("バーク『崇高と美の起源』", "カント『判断力批判』（美学的側面）", "influences",
     "カントの崇高論はバークから直接的影響を受けつつ理論化される。"),
    ("カント『判断力批判』（美学的側面）", "シラー『人間の美的教育について』", "influences",
     "シラーはカント美学を実践的・教育的に展開する。"),
    ("ヘルダーの民族精神（フォルクスガイスト）", "シュレーゲル『アテネーウム断片集』", "influences",
     "ヘルダーの民族精神論がドイツ・ロマン派の国民文学観の前提。"),
    ("ヴィーコ『新しい学』", "ヘルダーの民族精神（フォルクスガイスト）", "influences",
     "ヴィーコの詩的知恵論がヘルダーの民族精神論の遠源となる。"),
    ("レッシング『ラオコオン』（理論側面）", "カント『判断力批判』（美学的側面）", "influences",
     "レッシングの媒体特異性論がカント美学のジャンル論的前提。"),

    # D. 19c Romantic/Idealist internal
    ("カント『判断力批判』（美学的側面）", "シュレーゲル『アテネーウム断片集』", "influences",
     "カント美学がイェナ・ロマン派の理論的前提。"),
    ("カント『判断力批判』（美学的側面）", "ヘーゲル『美学講義』", "influences",
     "ヘーゲル美学はカント美学の弁証法的拡張。"),
    ("シラー『人間の美的教育について』", "シュレーゲル『アテネーウム断片集』", "influences",
     "シラーの美的状態論がイェナ・ロマン派理論の直接的源泉。"),
    ("シュレーゲル『アテネーウム断片集』", "コールリッジ『文学的自伝』（理論側面）", "influences",
     "シュレーゲルのドイツ・ロマン派理論がコールリッジ批評の源泉。"),
    ("シェリング哲学（外部）", "コールリッジ『文学的自伝』（理論側面）", "influences",
     "コールリッジはシェリング想像力論を直接英訳的に流用する（外部リレーション）。"),
    ("コールリッジ『文学的自伝』（理論側面）", "ワーズワース『抒情民謡集』序文（理論版）", "criticizes",
     "コールリッジは『文学的自伝』後半でワーズワース序文の詩語論を批判的に再考する。"),
    ("ヘーゲル『美学講義』", "ショーペンハウアーの芸術論", "criticizes",
     "ショーペンハウアーはヘーゲル芸術終焉論への対抗として意志の客体化論を展開する。"),
    ("カーライル英雄論", "サント＝ブーヴ伝記批評", "parallel",
     "カーライルとサント＝ブーヴは作家＝偉人の人格中心批評を並行的に展開する。"),

    # E. Late-19c internal
    ("サント＝ブーヴ伝記批評", "テーヌ三要素批評（人種・環境・時代）", "influences",
     "サント＝ブーヴの伝記批評がテーヌの実証主義的拡張の前提となる。"),
    ("テーヌ三要素批評（人種・環境・時代）", "ブリュンチエール歴史的批評", "influences",
     "ブリュンチエールはテーヌ三要素批評にダーウィン進化論を加える。"),
    ("アーノルド「批評の機能」", "アーノルド試金石批評", "extends",
     "アーノルドは「批評の機能」の理論を「試金石」批評の方法論として実装する。"),
    ("ペイター『ルネサンス』", "ペイターの印象主義批評", "contains",
     "『ルネサンス』序文がペイター印象主義批評の方法的綱領。"),
    ("ペイター『ルネサンス』", "シモンズ『象徴主義文学運動』", "influences",
     "ペイターの唯美主義がシモンズの象徴主義紹介の理論的基盤。"),
    ("アーノルド「批評の機能」", "ペイターの印象主義批評", "criticizes",
     "ペイター印象主義批評はアーノルド客観主義への対抗として展開する。"),
    ("ヘーゲル『美学講義』", "ベリンスキーのリアリズム批評", "influences",
     "ベリンスキーはヘーゲル左派の芸術論をリアリズム批評に転化する。"),
    ("カーライル英雄論", "アーノルド「批評の機能」", "influences",
     "カーライルの文化論がアーノルド教養論の英国的前提となる。"),

    # Cross-period bridges
    ("詩人追放論（『国家』第十巻）", "ヴィーコ『新しい学』", "criticizes",
     "ヴィーコは詩的知恵論によりプラトンの詩排除論への根本的応答を提示する。"),
    ("ロンギノス『崇高について』（理論側面）", "シュレーゲル『アテネーウム断片集』", "influences",
     "ロンギノス崇高論はドイツ・ロマン派の超越的詩学の古典的源泉。"),
    ("アクィナスの美学", "カント『判断力批判』（美学的側面）", "influences",
     "アクィナスの美の三条件（特にclaritas）はカント美学の前史的原型を成す。"),
    ("カスティリオーネ『宮廷人の書』", "シラー『人間の美的教育について』", "influences",
     "宮廷人の優雅（sprezzatura）はシラーの美的状態論の遠源となる。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[wave10_c34_theory_classical] inserting {len(CONCEPTS)} concepts...")
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
                name_ja=name_ja, region="理論",
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
        print("[wave10_c34_theory_classical] inserted:")
        print(f"  concepts: {summary['concepts']}")
        print(f"  fourth_transform_tags: {summary['fourth_transform_tags']} "
              f"(this run: +{fourth_count})")
        print(f"  cross_domain: {summary['cross_domain']} "
              f"(this run: +{cd_count})")
        print(f"  relations: {summary['relations']} "
              f"(this run: +{relation_count})")

        # Subfield 22 cumulative
        cur = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 22"
        ).fetchone()
        print(f"  subfield_id=22 cumulative concepts: {cur['c']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
