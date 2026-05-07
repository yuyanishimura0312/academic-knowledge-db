"""
LIT-DB Phase 2 — C05: Renaissance / Early Modern Western Europe (ルネサンス・近世西欧)
======================================================================================
Inserts 40 canonical concepts spanning 5 categories:
  A. Major movements / schools (8)
  B. Major genres / forms (8)
  C. Major themes / concepts (8)
  D. Major author-concepts / techniques (8)
  E. Critical / meta concepts (8)

subfield_code='lit_eu_renaissance' (id=3), region='西欧'
Primary sources: Folger Shakespeare, Project Gutenberg, Internet Archive,
EEBO bibliographic citations, Perseus (PD).

Pattern: P1 (Canonical Primary Pursuit) — anchored to PD or critical-edition
attestable references; secondary tier reserved for critically established
synthetic concepts (e.g., 'Petrarchan conceit' as critical category).
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding — Renaissance / Early Modern (Western Europe)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("初期ルネサンス（イタリア）", "Early Italian Renaissance", 1300, 1450,
     "ペトラルカ・ボッカッチョによる古典復興とトスカーナ俗語文学の確立期。"),
    ("盛期・後期ルネサンス（伊・西・仏）", "High and Late Renaissance",
     1450, 1580,
     "印刷術普及・人文主義の汎ヨーロッパ展開、プレイヤード派、カスティーリャ黄金時代の前段。"),
    ("エリザベス朝・ジャコビアン期（英）", "Elizabethan and Jacobean England",
     1558, 1625,
     "シェイクスピア・シドニー・スペンサー・ベン・ジョンソンら英詩・英演劇の頂点期。"),
    ("黄金世紀（西）", "Spanish Golden Age", 1492, 1681,
     "セルバンテス、ロペ・デ・ベガ、ゴンゴラ、カルデロン・デ・ラ・バルカらによるカスティーリャ語文学の黄金期。"),
]


# ---------------------------------------------------------------
# Concept payload
# ---------------------------------------------------------------

CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


SUB = "lit_eu_renaissance"
REG = "西欧"


# ===============================================================
# CATEGORY A — Major movements / schools (8)
# ===============================================================

add({
    "name_ja": "人文主義",
    "name_en": "Renaissance humanism",
    "name_original": "studia humanitatis",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ルネサンス（イタリア）",
    "definition": "古典ラテン・ギリシア語文献の発掘・校訂・模倣を通じて人間性（humanitas）の陶冶を目指した知的運動。文法・修辞・詩学・歴史・道徳哲学の五科目（studia humanitatis）を中核とし、ペトラルカに始まりエラスムスで頂点を迎え、近世全ヨーロッパの教育・文芸の枠組みを規定した。",
    "background": "中世スコラ哲学の論理学優位への反動として、ペトラルカがキケロ書簡を写本探索により再発見した1345年が転機。",
    "development": "ヴァッラ『ラテン語の優美について』、ピコ『人間の尊厳について』、エラスムス『痴愚神礼讃』を経て、北方人文主義として宗教改革と結びつく。",
    "historical_context": "イタリア都市国家の俗人エリート階層が古典模倣を通じて新たな自己定義を行った。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/1399",
    "primary_source_type": "Project Gutenberg — Petrarch Letters",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "「人間の尊厳」を中心に据えた近世主体観は、AIが言語生産の主体となり得る現代において再検討の必要に迫られている。",
         "related_ai_phenomenon": "AI時代の人間主体性論争"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ルネサンス人文主義",
         "description": "哲学DBの近世前期人間論の中核概念と直接共有。"},
    ],
})

add({
    "name_ja": "プレイヤード派",
    "name_en": "La Pléiade",
    "name_original": "La Pléiade",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "1549年デュ・ベレー『フランス語の擁護と顕揚』を綱領とする七人の詩人グループ（ロンサール、デュ・ベレー他）による詩革新運動。フランス語による高雅な詩を打ち立てるべく、ギリシア・ラテン詩とイタリアのペトラルキスムを翻案・模倣した。",
    "background": "宮廷詩人マロら旧世代の中世詩形を超克し、フランス語の詩的威信を国民的課題として確立しようとした。",
    "development": "ロンサール『恋愛詩集』、デュ・ベレー『オリーヴ』『悔恨詩集』として結実し、フランス古典主義詩学（マレルブ、ボワロー）への直接の前段階を成す。",
    "historical_context": "ヴァロワ宮廷の文化政策と俗語詩の威信競争。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/14128",
    "primary_source_type": "Project Gutenberg — Du Bellay Défense",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "俗語の「擁護と顕揚」によって国民言語を構築する企図は、AIによる多言語等価生成という現代的状況のなかで言語の優劣・正統性の問題を再活性化させる。",
         "related_ai_phenomenon": "LLMにおける多言語コーパスの不均衡と国民語"},
    ],
})

add({
    "name_ja": "ペトラルキスム",
    "name_en": "Petrarchism",
    "name_original": "Petrarchismo",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "ペトラルカ『カンツォニエーレ』を範とする恋愛抒情詩の汎ヨーロッパ的模倣現象。理想化された女性ラウラへの届かぬ恋、対立物の修辞（火と氷、甘苦）、ソネット連作の集成形式が定型化し、16世紀ヨーロッパ抒情詩の共通言語となった。",
    "background": "ベンボ『俗語論』（1525）によりトスカーナ語ペトラルカ詩が範例として制度化された。",
    "development": "ロンサール、シドニー、スペンサー、ガルシラーソ・デ・ラ・ベガらが各国語版ペトラルキスムを展開し、後にバロックの「反ペトラルキスム」を生む。",
    "historical_context": "印刷本によるペトラルカ普及と宮廷恋愛詩の制度化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/41085",
    "primary_source_type": "Project Gutenberg — Petrarch Sonnets (English)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "カスティーリャ黄金時代",
    "name_en": "Castilian Golden Age (Siglo de Oro)",
    "name_original": "Siglo de Oro",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "黄金世紀（西）",
    "definition": "16世紀末から17世紀後半にかけてのカスティーリャ語文学の隆盛期。セルバンテス、ロペ・デ・ベガ、ゴンゴラ、ケベード、カルデロンが活躍し、ピカレスク小説・コメディア・ゴンゴリスモ詩・宗教劇を発達させ、スペインの世界帝国期と並行する文化的爆発を成した。",
    "background": "アメリカ植民・ハプスブルク家統治・反宗教改革を背景とする。",
    "development": "セルバンテス『ドン・キホーテ』が近代小説の祖となり、コメディアはフランス古典主義劇に影響、ゴンゴラの culteranismo は20世紀「27年世代」に再評価される。",
    "historical_context": "帝国の絶頂と衰退の同時進行が「不安と栄光」の文学を生んだ。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/996",
    "primary_source_type": "Project Gutenberg — Cervantes Don Quijote",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "エリザベス朝演劇",
    "name_en": "Elizabethan stage",
    "name_original": "Elizabethan stage",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "エリザベス朝・ジャコビアン期（英）",
    "definition": "1576年The Theatre開設から1642年清教徒革命の劇場閉鎖までのロンドン公衆劇場文化。マーロウ、シェイクスピア、ジョンソン、ウェブスターらが、貴族のパトロン制と公衆観客の経済性、円形舞台と無装幀の上演条件を組み合わせ、近世西欧最大の演劇的爆発を生んだ。",
    "background": "中世受難劇・道徳劇から発展し、宮廷祝祭と公衆娯楽が交差する独自空間として制度化。",
    "development": "シェイクスピア『ハムレット』『リア王』、ジョンソン『ヴォルポーネ』、ウェブスター『マルフィ公爵夫人』など。後の英演劇とドイツ・ロマン派のシェイクスピア受容の母胎。",
    "historical_context": "テューダー・スチュアート期の都市化と宮廷文化の交差。",
    "primary_source_url": "https://shakespeare.folger.edu/",
    "primary_source_type": "Folger Shakespeare Library",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "形而上派詩人",
    "name_en": "Metaphysical poets",
    "name_original": "Metaphysical poets",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "エリザベス朝・ジャコビアン期（英）",
    "definition": "ジョン・ダン、ジョージ・ハーバート、アンドリュー・マーヴェル、リチャード・クラショーらの17世紀英詩人群。突飛な比喩（conceit）、論理的議論の劇的展開、神学的・哲学的主題への鋭い知的接近を特徴とし、サミュエル・ジョンソンが命名したことで批評概念として固定された。",
    "background": "ペトラルキスムの慣習的恋愛詩への反動と、宗教改革後の個人的霊性の問いの結合。",
    "development": "20世紀T.S.エリオット「形而上派詩人論」（1921）により再評価され、モダニズム詩学の祖型となった。",
    "historical_context": "宗教戦争期の信仰と懐疑の鋭い葛藤。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/23838",
    "primary_source_type": "Project Gutenberg — Donne Poems",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "スプレッツァトゥーラ",
    "name_en": "sprezzatura",
    "name_original": "sprezzatura",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "カスティリオーネ『宮廷人』（1528）が定義した宮廷人の理想的態度で、技巧的な振舞いをあたかも自然・無造作であるかのように見せる「努力の隠蔽」。文学・修辞・恋愛・処世のあらゆる場面を貫く近世エリートの美的規範となり、ヨーロッパ宮廷文化に普遍化した。",
    "background": "ウルビーノ宮廷の理想的廷臣像の探求として論じられた。",
    "development": "シェイクスピア演劇、シドニー『アーケイディア』の貴族像、後のフランス古典主義の bonheur d’expression に間接的に継承。",
    "historical_context": "イタリア小宮廷文化が汎ヨーロッパの貴族モデルとして輸出された時代。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/29429",
    "primary_source_type": "Project Gutenberg — Castiglione Courtier",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "エラスミアニズム",
    "name_en": "Erasmianism",
    "name_original": "Erasmianismus",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "エラスムス・ロッテルダム（c.1466–1536）の思想と文体を範とする北方人文主義の流派。原典批判（『校訂版ギリシア語新約聖書』1516）、平和主義、寛容、聖書源泉主義（philosophia Christi）を文体的優美と結合し、宗教改革と対抗改革双方に深い影響を与えた。",
    "background": "ヴァッラの文献学的批判精神を北方ヨーロッパに移植する試み。",
    "development": "『痴愚神礼讃』（1511）、『キリスト教兵士提要』、『格言集』を経て、モンテーニュ、ラブレー、シェイクスピアの寛容主義・笑い・人文主義へと連続する。",
    "historical_context": "宗教戦争前夜の調停的人文主義の極限的形態。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/9371",
    "primary_source_type": "Project Gutenberg — Erasmus Praise of Folly",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "エラスムス的人文主義",
         "description": "哲学DBの近世前期寛容論・人間論の起点として共有。"},
    ],
})


# ===============================================================
# CATEGORY B — Major genres / forms (8)
# ===============================================================

add({
    "name_ja": "ソネット",
    "name_en": "sonnet",
    "name_original": "sonetto",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ルネサンス（イタリア）",
    "definition": "14行・抑揚整った韻律・閉じた論理構造を持つ短詩形。13世紀シチリア派ジャコモ・ダ・レンティーニが原型を示し、ペトラルカが恋愛抒情詩の標準形式に定着、シェイクスピアが英国型（4・4・4・2）に変奏した。近世ヨーロッパ抒情詩の最大公約数的形式となる。",
    "background": "中世イタリア宮廷詩の短歌形式から発展。",
    "development": "ペトラルカ → ペトラルキスム → シドニー『アストロフェルとステラ』 → シェイクスピア・ソネット集 → ミルトン・ワーズワース・キーツ・リルケへと連続。",
    "historical_context": "印刷本による標準形式の流通と多言語伝播。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/41085",
    "primary_source_type": "Project Gutenberg — Petrarch Sonnets",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "牧歌劇／パストラル",
    "name_en": "pastoral (Renaissance)",
    "name_original": "pastorale",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "ヘレニズム期テオクリトス・ウェルギリウスを範に、理想化された田園空間で羊飼い達の恋愛と詩を演じる文学形式。サンナザーロ『アルカディア』（1504）が散文と詩の混成形式として確立し、タッソ『アミンタ』、シドニー『アーケイディア』、スペンサー『羊飼いの暦』へと展開した。",
    "background": "都市化した宮廷文化の田園郷愁とウェルギリウス受容の合流。",
    "development": "シェイクスピア『お気に召すまま』、ミルトン『リシダス』、後のロマン派田園詩へと連続する。",
    "historical_context": "宮廷的閑暇と古典模倣の理想空間として機能。",
    "primary_source_url": "https://archive.org/details/sannazaroarcadia00sann",
    "primary_source_type": "Internet Archive — Sannazaro Arcadia",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ピカレスク小説",
    "name_en": "picaresque novel",
    "name_original": "novela picaresca",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "黄金世紀（西）",
    "definition": "下層社会出身の悪漢（pícaro）が一人称で自伝的に語るエピソディック小説。匿名『ラサリーリョ・デ・トルメスの生涯』（1554）が原型を確立し、アレマン『グスマン・デ・アルファラチェ』（1599）、ケベード『ぺてん師』により黄金時代を成した。社会風刺と内省の結合が近代小説の重要源流となる。",
    "background": "16世紀スペインの貧困・移民・階層流動性の経験を文学化。",
    "development": "グリンメルスハウゼン『阿呆物語』、ルサージュ『ジル・ブラース』、デフォー『モル・フランダース』、ディケンズ『デイヴィッド・コパフィールド』、20世紀のソール・ベローへと連続。",
    "historical_context": "帝国期スペインの社会的不安と神学的悲観論。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/320",
    "primary_source_type": "Project Gutenberg — Lazarillo de Tormes",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "エセー（モンテーニュ）",
    "name_en": "essai (Montaigne)",
    "name_original": "essai",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "モンテーニュが『エセー』（1580–88）で創出したジャンルで、特定主題への試論・自己観察・古典引用が縦横に絡む散文形式。「私自身が私の書物の素材である」と宣言し、確定した結論を拒む試行的（en essayant）思考を文体化、近世散文の自伝的・懐疑論的支柱となった。",
    "background": "ボルドー高等法院議員引退後、自宅塔の書斎で着手された。",
    "development": "ベーコン『随想集』、パスカル『パンセ』、ハズリット、エマソン、現代エッセイ全般の祖型。",
    "historical_context": "宗教戦争の暴力に対する個人的距離化の手段。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/3600",
    "primary_source_type": "Project Gutenberg — Montaigne Essais",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "「自己を素材とする」モンテーニュ的試論は近世主体性の文学的実装であり、AIが自己を参照する書記形式（self-referential generation）の先行例として再読される。",
         "related_ai_phenomenon": "AIによる自己観察的テクスト生成"},
    ],
})

add({
    "name_ja": "シェイクスピア演劇",
    "name_en": "Shakespearean drama",
    "name_original": "Shakespearean drama",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "エリザベス朝・ジャコビアン期（英）",
    "definition": "ウィリアム・シェイクスピア（1564–1616）が確立した英演劇形式。歴史劇・悲劇・喜劇・ロマンス劇の四ジャンル横断、無韻詩（blank verse）と散文の交差、複数プロット並列構造、心理的に流動的な登場人物造形によって、西洋演劇の基準点となった。",
    "background": "公衆劇場の経済性・宮廷祝祭・テューダー史劇受容の結合。",
    "development": "後の英演劇のみならず、独ロマン派、フランス・ユゴー、現代映画化、ポストコロニアル『テンペスト』読解にまで連続する。",
    "historical_context": "テューダー終焉とスチュアート初期の政治的不安定。",
    "primary_source_url": "https://shakespeare.folger.edu/",
    "primary_source_type": "Folger Shakespeare — Folger Editions",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "Cultural-Intelligence", "link_type": "shared_concept",
         "target_entity_name": "シェイクスピアの世界正典化",
         "description": "文化情報DBの「世界文化資源」概念とリンク。"},
    ],
})

add({
    "name_ja": "マスク（仮面劇）",
    "name_en": "masque",
    "name_original": "masque",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "エリザベス朝・ジャコビアン期（英）",
    "definition": "宮廷で上演された詩・音楽・舞踊・舞台美術が融合する祝祭劇。ベン・ジョンソンとイニゴ・ジョーンズの共作（1605以降）が頂点で、王権賛美の寓意とアンチマスクの混乱対比を構造とする。後の英オペラ・ハイ・ロマンス劇に続く総合芸術の前駆。",
    "background": "宮廷祝祭文化と人文主義的寓意伝統の結合。",
    "development": "ミルトン『コーマス』が文学的マスクの傑作。ヘンデル英オペラ、ロマン派詩劇に間接的影響。",
    "historical_context": "スチュアート初期の絶対王政賛美装置として機能。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/19909",
    "primary_source_type": "Project Gutenberg — Milton Comus / Ben Jonson Masques",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "エンブレム本",
    "name_en": "emblem book",
    "name_original": "emblemata",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "図像（pictura）・標題（motto）・詩文（subscriptio）の三部構成で道徳的・寓意的真理を提示する近世の複合書物形式。アンドレア・アルチャート『エンブレム集』（1531）が祖で、500冊以上が16–17世紀ヨーロッパで流通、視覚と言語の結合詩学を制度化した。",
    "background": "象形文字解読熱・印刷木版術・寓意伝統の合流。",
    "development": "シェイクスピア・スペンサー・ジョージ・ハーバートの詩想に深く浸透し、現代の視覚文化研究（W.J.T.ミッチェル）の一次史料となる。",
    "historical_context": "絵画と書物の境界における近世視覚文化の制度化。",
    "primary_source_url": "https://archive.org/details/alciatusemblemat00alci",
    "primary_source_type": "Internet Archive — Alciato Emblemata",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ノヴェッラ",
    "name_en": "novella",
    "name_original": "novella",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ルネサンス（イタリア）",
    "definition": "短編散文物語のイタリア起源形式。ボッカッチョ『デカメロン』（1353）が枠物語形式（黒死病避難中の十日間百話）で完成し、機智・情欲・運命の急転を中核主題とする。後のヨーロッパ短編・近代novel語源となる。",
    "background": "中世フランス韻文短編（fabliau）と東方枠物語の合流。",
    "development": "バンデッロ『ノヴェッラ集』、マルグリット・ド・ナヴァール『エプタメロン』、シェイクスピアの『ロミオとジュリエット』『ヴェニスの商人』源泉となり、近代短編小説とロマン主義Novelle（ゲーテ）の祖型。",
    "historical_context": "中世末期都市市民層の物語消費の制度化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/23700",
    "primary_source_type": "Project Gutenberg — Boccaccio Decameron",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY C — Major themes / concepts (8)
# ===============================================================

add({
    "name_ja": "イミタチオ（模倣）",
    "name_en": "imitatio",
    "name_original": "imitatio",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "古代古典作家を範例として模倣することで自己の文体を陶冶する近世文学創作の根本原理。ペトラルカが「蜜蜂の比喩」（複数の花から蜜を集めて自分の蜜にする）として理論化、ベンボがキケロ・ペトラルカ単一模範を主張、エラスムス『キケロニアヌス』が複数模範を擁護して近世文学の中心論争となった。",
    "background": "古代修辞学（クインティリアヌス）の模倣論を近世創作論に接続。",
    "development": "ロンサールの「自然な模倣」、シドニー『詩の擁護』、後のドライデン・ポープの新古典主義詩学に直接連続。",
    "historical_context": "古典再発見と俗語文学創出の同時進行が要請した詩学的調整。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/14128",
    "primary_source_type": "Project Gutenberg — Du Bellay Défense",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "「複数源泉からの模倣による独自性」を要求するイミタチオは、AIが大規模コーパスから生成する詩的テクストの創造性論争と直接対応する。中国文芸理論の「点鉄成金」と並列して再読されるべき近世詩学の中核。",
         "related_ai_phenomenon": "LLMにおけるコーパスからの「学習」と独創性論争"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "イミタチオ詩学",
         "description": "Poetics DBの近世詩学の根本原理として共有。"},
    ],
})

add({
    "name_ja": "コピア（豊穣）",
    "name_en": "copia",
    "name_original": "copia (rerum ac verborum)",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "「事物と言葉の豊穣」を意味する近世修辞学の中核概念。エラスムス『コピア論』（1512）が同じ事柄を200通り以上の言い回しで表現する訓練書として体系化し、ヨーロッパ全土の人文主義教育の標準教材となった。語彙的・修辞的多様性を文体的優美の必須条件とする。",
    "background": "クインティリアヌスの copia 論を北方人文主義教育に再構築。",
    "development": "ラテン文法学校の必須訓練として浸透し、シェイクスピア劇の語彙の豊かさ、ラブレーの饒舌、ジョンソンの修辞密度の制度的基盤となった。",
    "historical_context": "印刷本時代の語彙拡張への教育的対応。",
    "primary_source_url": "https://archive.org/details/eraserridoublec00eras",
    "primary_source_type": "Internet Archive — Erasmus De Copia",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "「無限の言い換え」を訓練するコピアは、LLMの言い換え（paraphrase）生成能力の人文主義的先行例として再評価できる。",
         "related_ai_phenomenon": "LLMによる言い換え生成（paraphrase）"},
        {"axis": "創造性", "status": "rethinking",
         "rationale": "コピアが教える「同一事象の多言語化」は、AI時代の創造性論争において「冗長と豊穣の差」を再考させる。",
         "related_ai_phenomenon": "AI生成テクストの冗長性／創造性論争"},
    ],
})

add({
    "name_ja": "デコルム（適切さ）",
    "name_en": "decorum",
    "name_original": "decorum",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "話者・聴衆・主題に応じて文体・語彙・形式を「適切に」整える近世修辞学の規範原理。キケロの decorum を近世が再発見し、シドニー『詩の擁護』、ジョンソン『木材』、後のフランス新古典主義の bienséance（礼節）にまで体系化された。文学的階層秩序の中核を成す。",
    "background": "古代キケロ・クインティリアヌス修辞学の近世受容。",
    "development": "ボワロー『詩法』、ドライデン批評を経て、19世紀以降のリアリズム詩学が破壊的に乗り越える対象となる。",
    "historical_context": "宮廷文化と階層秩序の文学的反映。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/1962",
    "primary_source_type": "Project Gutenberg — Sidney Defence of Poesy",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "デコルム",
         "description": "Poetics DBの近世詩学規範として共有。"},
    ],
})

add({
    "name_ja": "ウト・ピクトゥラ・ポエシス",
    "name_en": "ut pictura poesis",
    "name_original": "ut pictura poesis",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "ホラティウス『詩論』の「絵画のように詩もまた」の句を起点とする、詩と絵画の姉妹芸術論。近世はこの一句を絵画と詩の本質的等価性を主張する標語として絶対化し、エンブレム本・寓意絵画・エクフラシス的詩を生む詩学的根拠となった。",
    "background": "ホラティウス受容と人文主義者の絵画擁護論の合流。",
    "development": "レッシング『ラオコオン』（1766）が詩と絵画の本質的差異を論じて批判するまで、二世紀以上の規範性を保った。",
    "historical_context": "印刷木版・宮廷絵画・人文主義教育の交差。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/14020",
    "primary_source_type": "Project Gutenberg — Horace Ars Poetica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "テアトルム・ムンディ（世界劇場）",
    "name_en": "theatrum mundi",
    "name_original": "theatrum mundi",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "エリザベス朝・ジャコビアン期（英）",
    "definition": "「世界は舞台、人はみな役者」の比喩で、人生を演劇として、神を観客として捉える近世形而上学的世界観。シェイクスピア『お気に召すまま』の「全世界が舞台」、カルデロン『世界という大劇場』（El gran teatro del mundo）が文学的頂点を成し、ストア派・キリスト教思想の近世的再活性化を体現する。",
    "background": "後期古代のエピクテトス・古ストア派の比喩と中世キリスト教の終末論的視点の融合。",
    "development": "バロック演劇の自意識的形式、近代フィクションの自己反映性、現代パフォーマンス・スタディーズへ連続。",
    "historical_context": "宗教戦争の流動性と近世宮廷演劇の隆盛が共鳴。",
    "primary_source_url": "https://shakespeare.folger.edu/shakespeares-works/as-you-like-it/",
    "primary_source_type": "Folger Shakespeare — As You Like It",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "「自我は演じられた役柄である」というテアトルム・ムンディの近世主体観は、AIアバターやデジタルペルソナの可塑性論議と構造的に重なり、近代主体性以前の演劇的自我観を再活性化する。",
         "related_ai_phenomenon": "AIアバター・SNSペルソナ・デジタル自我"},
    ],
})

add({
    "name_ja": "メランコリー",
    "name_en": "melancholy",
    "name_original": "melancholia",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "エリザベス朝・ジャコビアン期（英）",
    "definition": "黒胆汁過剰によって生じる憂鬱と知性の特質を結ぶ古典医学＝心理学的概念。フィチーノ『生について』が天才の必要条件と理論化、デューラー版画『メレンコリアI』（1514）に視覚的範例化、バートン『憂鬱の解剖』（1621）が百科全書的に集大成した。シェイクスピア『ハムレット』の中核主題。",
    "background": "ガレノス医学の四体液説と新プラトン主義の天才論の融合。",
    "development": "ロマン主義の天才・憂鬱論、ベンヤミン『ドイツ悲哀劇の根源』、現代の鬱病文化論まで連続。",
    "historical_context": "近世主体性の内面化と医学的自己理解の制度化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/10800",
    "primary_source_type": "Project Gutenberg — Burton Anatomy of Melancholy",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "宮廷恋愛の再考",
    "name_en": "courtly love revisited",
    "name_original": "amour courtois rivisitato",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "中世トルバドゥール／フィン・アモール（fin’amor）の届かぬ恋の枠組みを、近世ペトラルキスム・宮廷恋愛詩・カスティリオーネ宮廷論が再解釈し、新プラトン主義的精神化（ベンボ『アゾラーニ』）と俗化（シェイクスピア『恋の骨折り損』）の二極で展開した近世恋愛詩学。",
    "background": "中世宮廷詩の継承とプラトン『饗宴』再発見の合流。",
    "development": "ペトラルキスム全般、シドニー『アストロフェルとステラ』、ロンサール、後の17世紀précieuses文学にまで連続。",
    "historical_context": "宮廷文化の汎ヨーロッパ化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/29429",
    "primary_source_type": "Project Gutenberg — Castiglione Courtier",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "宮廷恋愛",
         "description": "人類学DBの恋愛文化研究と共有される歴史的範例。"},
    ],
})

add({
    "name_ja": "可滅的肉体（メメント・モリ）",
    "name_en": "mortal flesh / memento mori",
    "name_original": "memento mori",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "エリザベス朝・ジャコビアン期（英）",
    "definition": "「死を覚えよ」の警句に集約される、肉体の可滅性と魂の不滅性をめぐる近世詩学的主題。ペスト・宗教戦争・改革論争を背景に、ジョン・ダンの説教『緊急時の祈り』『死よ、誇るなかれ』、シェイクスピア『ハムレット』墓場場面が頂点を成す。",
    "background": "中世末期の死の舞踏（danse macabre）伝統の近世個人主義的内面化。",
    "development": "バロック宗教詩、近代の存在論的詩（ハイデガー、リルケ）まで連続。",
    "historical_context": "宗教戦争と疫病が連続する近世初期の死の遍在性。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/23838",
    "primary_source_type": "Project Gutenberg — Donne Holy Sonnets",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY D — Major author-concepts / techniques (8)
# ===============================================================

add({
    "name_ja": "ペトラルカ的コンチェット",
    "name_en": "Petrarchan conceit",
    "name_original": "concetto petrarchesco",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ルネサンス（イタリア）",
    "definition": "ペトラルカ『カンツォニエーレ』に範を取る恋愛詩の修辞的装置。「火と氷」「甘い苦しみ」「歩く死人」など対立物の融合、誇張的比喩、抽象と感覚の交差を組み合わせて愛の矛盾を表現する。近世ヨーロッパ恋愛詩の標準的修辞語彙となった。",
    "background": "プロヴァンス trobar clus と中世ストイル・ノヴォの遺産の集成。",
    "development": "ペトラルキスム全般を貫き、形而上派詩人のメタフィジカル・コンチェット（ダン、マーヴェル）として知的劇化、後にエリオットが再評価。",
    "historical_context": "宮廷恋愛詩学のヨーロッパ的標準化期。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/41085",
    "primary_source_type": "Project Gutenberg — Petrarch Sonnets",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シェイクスピア的無韻詩",
    "name_en": "Shakespearean blank verse",
    "name_original": "blank verse",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "エリザベス朝・ジャコビアン期（英）",
    "definition": "弱強五歩格（iambic pentameter）の押韻なし詩行で、サリー伯ハワードがウェルギリウス英訳に導入、マーロウが劇詩に応用、シェイクスピアが思考の自然な流動性を表す柔軟な韻律に成熟させた。英演劇・英叙事詩（ミルトン『失楽園』）の標準形式。",
    "background": "イタリア verso sciolto の英語移植としてサリーが導入。",
    "development": "ミルトン『失楽園』、ワーズワース『序曲』、テニソン、フロスト、現代の英語詩劇まで継続使用される。",
    "historical_context": "印刷文化と公衆劇場の融合した英文学固有の韻律進化。",
    "primary_source_url": "https://shakespeare.folger.edu/",
    "primary_source_type": "Folger Shakespeare — Folger Editions",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "セルバンテス的対話主義",
    "name_en": "Cervantes dialogism",
    "name_original": "dialogismo cervantino",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "黄金世紀（西）",
    "definition": "セルバンテス『ドン・キホーテ』（1605/1615）が確立した複数声部の同時進行的小説技法。理想主義的キホーテと現実主義的サンチョの永続的対話、語り手の入れ子、本物・偽物の続編問題が、20世紀バフチンによって「対話的小説」原理として理論化された近代小説の祖型。",
    "background": "騎士道物語パロディとピカレスク的下層描写の融合。",
    "development": "スターン『トリストラム・シャンディ』、フィールディング、ドストエフスキー、ボルヘスの再書き、20世紀メタフィクションへ直接連続。",
    "historical_context": "騎士道理想と帝国衰退期の現実の落差。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/996",
    "primary_source_type": "Project Gutenberg — Cervantes Don Quijote",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ラブレー的カーニヴァル",
    "name_en": "Rabelaisian carnival",
    "name_original": "carnaval rabelaisien",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "ラブレー『ガルガンチュアとパンタグリュエル』（1532–64）に体現される民衆的笑い、身体性（食・性・排泄）の称揚、公的言説の脱中心化を特徴とする近世文学的形式。バフチン『フランソワ・ラブレーの作品と中世・ルネサンスの民衆文化』が「カーニヴァル化された文学」原理として理論化した。",
    "background": "中世末期の民衆祝祭文化と人文主義古典学の異種接合。",
    "development": "スウィフト『ガリヴァー旅行記』、ジョイス『ユリシーズ』、ガルシア＝マルケス、近現代のグロテスク・リアリズム全般に連続。",
    "historical_context": "宗教戦争前夜の民衆文化と知識文化の最後の融合期。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/1200",
    "primary_source_type": "Project Gutenberg — Rabelais Gargantua",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "モンテーニュ的試行",
    "name_en": "Montaigne's essai-method",
    "name_original": "essai (méthode montaignienne)",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "モンテーニュが固有の文体として実践した、確定的結論を求めず思考を試行（en essayant）し続ける書記方法。「私は何を知るか（Que sais-je?）」を旗印に、自己観察・古典引用・経験的逸話を縦横に編む方法は、近世懐疑論文学と近代エッセイの基盤となった。",
    "background": "ピュロン主義復興（セクストス・エンペイリコス再発見）と個人的書斎文化の融合。",
    "development": "パスカル、ベーコン、ヒューム、エマソン、ヴァレリー、現代の批評的エッセイ全般。",
    "historical_context": "宗教戦争期の絶対的真理主張への懐疑論的応答。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/3600",
    "primary_source_type": "Project Gutenberg — Montaigne Essais",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "タッソの英雄叙事詩",
    "name_en": "Tasso's heroic epic",
    "name_original": "poema eroico tassiano",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "トルクァート・タッソ『エルサレム解放』（1581）が確立した近世英雄叙事詩の規範。第一回十字軍を題材に、ホメロス・ウェルギリウスの古典構造、アリオスト的恋愛・魔術エピソード、対抗改革の宗教的真摯さを統合し、『英雄詩論』（1594）で詩学的に自己理論化した。",
    "background": "アリオスト『狂えるオルランド』の影響と対抗改革の倫理的厳格化。",
    "development": "スペンサー『妖精女王』、ミルトン『失楽園』、後のフランス古典主義叙事詩試行、19世紀イタリア統一期文学的記憶として再活性化。",
    "historical_context": "対抗改革期の文学と宗教的真理要求の調停。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/392",
    "primary_source_type": "Project Gutenberg — Tasso Jerusalem Delivered",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シドニー『詩の擁護』",
    "name_en": "Sidney's Defence of Poesy",
    "name_original": "The Defence of Poesy",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "エリザベス朝・ジャコビアン期（英）",
    "definition": "フィリップ・シドニー（1554–86）による英語最初期の体系的詩学論（c.1581執筆、1595出版）。ピューリタン的詩攻撃（スティーブン・ゴッソン）への応答として、アリストテレス・ホラティウス・スカリゲルを統合し、「詩は教えると同時に喜ばせる」ホラティウス的二目的論を英国に確立した。",
    "background": "ピューリタン『悪用の学校』（1579）の詩・劇場攻撃に対する貴族的応答。",
    "development": "ジョンソン批評、ドライデン『劇詩論』、後のイギリス批評伝統の起点。",
    "historical_context": "宗教改革後の英国における詩の正当性論争。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/1962",
    "primary_source_type": "Project Gutenberg — Sidney Defence of Poesy",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "「詩は嘘をつかぬ、なぜなら何も主張しないから」というシドニーの詩学的擁護論は、AIが生成するフィクションの真理問題（「ハルシネーション」）と直接対応する。",
         "related_ai_phenomenon": "生成AIにおけるハルシネーションと虚構の真理性"},
    ],
})

add({
    "name_ja": "ダンテ『新生』の遺産",
    "name_en": "Dante's Vita Nuova legacy",
    "name_original": "Vita Nuova / la nuova vita",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ルネサンス（イタリア）",
    "definition": "ダンテ・アリギエーリ『新生』（c.1294）が確立した、詩と散文を交互に編む「自伝的詩集」形式。理想化された女性ベアトリーチェへの愛を新プラトン主義的精神化と詩学的自己解説で結ぶ枠組みは、ペトラルカ『カンツォニエーレ』を経て近世恋愛詩集全般の基本枠組みとなった。",
    "background": "プロヴァンス・シチリア派抒情詩と中世神秘主義神学の融合。",
    "development": "ペトラルキスム、シドニー『アストロフェルとステラ』、ロセッティ訳によるラファエル前派受容、現代の批評的自伝にまで連続。",
    "historical_context": "中世末期トスカーナ俗語詩文化の自己定義期。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/41085",
    "primary_source_type": "Project Gutenberg — Dante Vita Nuova / Petrarch Sonnets",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY E — Critical / meta concepts (8)
# ===============================================================

add({
    "name_ja": "詩の擁護（ジャンルとして）",
    "name_en": "Defence of Poesy (as genre)",
    "name_original": "apologia / defensio poesis",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "ピューリタン・神学的詩攻撃に対し、詩の倫理的・教育的価値を擁護する近世批評ジャンル。ボッカッチョ『神々の系譜』第14・15巻、シドニー『詩の擁護』、後のジョンソン『木材』を中核とし、後の英・仏批評伝統全体の起点となった。",
    "background": "プラトン詩人追放論の中世的継承への近世人文主義的応答。",
    "development": "シェリー『詩の擁護』（1821）に直接連続し、現代の文学擁護論（マーサ・ヌスバウム等）へ。",
    "historical_context": "宗教改革と人文主義の交差点における詩の社会的位置の再交渉。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/1962",
    "primary_source_type": "Project Gutenberg — Sidney Defence of Poesy",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "AI時代の「文学の必要性」論争はDefence of Poesyジャンルの近世的成立条件を再活性化する。「詩は何の役に立つか」の問いが古代以来のリトルニューロを生んでいる。",
         "related_ai_phenomenon": "AI時代の文学・人文学の社会的価値論争"},
    ],
})

add({
    "name_ja": "詩論（アルス・ポエティカ）の復興",
    "name_en": "ars poetica revival",
    "name_original": "ars poetica",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "ホラティウス『詩論』とアリストテレス『詩学』のラテン訳普及（1498アヴェロエス経由、1536アレッサンドロ・パッツィ）による近世詩学論の体系化現象。スカリゲル『詩学七書』（1561）が古典詩学を百科全書化し、ロンサール『フランス詩芸術略』、シドニー、後のフランス古典主義詩学の規範を準備した。",
    "background": "印刷術による古典詩学テクストの普及と俗語詩規範化要求の合流。",
    "development": "ボワロー『詩法』（1674）、ポープ『批評論』を経て新古典主義詩学の基盤となる。",
    "historical_context": "古典詩学受容と俗語詩規範化の同時進行。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/14020",
    "primary_source_type": "Project Gutenberg — Horace Ars Poetica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "新旧論争前夜",
    "name_en": "Querelle des Anciens et des Modernes (eve of)",
    "name_original": "Querelle des Anciens et des Modernes",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "近世ヨーロッパで継続した古典の絶対的権威と近代詩人の同等性を争う論争で、後のフランス・アカデミーでの「新旧論争」（1687–94）に結晶する前段。タッソ＝アリオスト論争、シドニー的擁護、ジョルダーノ・ブルーノの近代擁護は、近世ルネサンスにおける古典模倣と独自性の緊張を体現した。",
    "background": "古典再発見の絶頂と俗語文学自己定義要求の交差。",
    "development": "ペロー『古代人と近代人の比較』（1688）、ジャン・ジャック・ルソーを経て、近代進歩史観の文学的起源となる。",
    "historical_context": "イタリア・ルネサンス遅期から北方人文主義への移行期。",
    "primary_source_url": "https://archive.org/details/scaliger-poetices-libri-septem",
    "primary_source_type": "Internet Archive — Scaliger Poetices",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "俗語の高揚",
    "name_en": "vulgar tongue elevation",
    "name_original": "elevatio linguae vulgaris",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ルネサンス（イタリア）",
    "definition": "ラテン語の独占的詩的威信に対抗し、各国俗語（イタリア語・フランス語・スペイン語・英語）を詩・散文の高雅な媒体に高める近世運動。ダンテ『俗語論（De vulgari eloquentia）』（c.1304–07）が原理を示し、デュ・ベレー『フランス語擁護』、ベンボ『俗語論』、ネブリハ『カスティーリャ語文法』が国民言語化を推進した。",
    "background": "宮廷文化の各国化と印刷市場の俗語需要拡大。",
    "development": "シェイクスピア英語、セルバンテスのカスティーリャ語、近代国民言語の文学的基盤として継続。",
    "historical_context": "近世国家形成と国民言語の同時成立。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/14128",
    "primary_source_type": "Project Gutenberg — Du Bellay Défense",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "「俗語＝近隣の周縁言語を高雅な媒体に高める」近世の運動は、低リソース言語への AI による高品質生成・翻訳が同様の威信再配分を起こす現代的事象と対応する。",
         "related_ai_phenomenon": "AIによる低リソース言語の文学的高雅化"},
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "ラテン語からの翻訳を通じて俗語が高雅化したように、AIによる多言語間の高速翻訳は言語間威信秩序の再編をもたらしている。",
         "related_ai_phenomenon": "AI翻訳による言語間威信秩序の再編"},
    ],
})

add({
    "name_ja": "劇場の比喩",
    "name_en": "theatrum metaphor",
    "name_original": "theatrum metaphor",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "エリザベス朝・ジャコビアン期（英）",
    "definition": "近世が世界・自然・記憶・知識を「劇場（theatrum）」として比喩化した知のメタファー群。クスマンスカ・ジョンストン、ジュリオ・カミーロの「記憶劇場」、テオドロス・ツヴィンガー『人間生活の劇場』、ベーコン『学問の進歩』、シェイクスピアの自己反映劇まで、近世知識編成の中心メタファー。",
    "background": "印刷本による知識集成と古代記憶術の合流。",
    "development": "後の百科全書、博物館、近代の知識可視化、現代のデータ可視化文化に継続。",
    "historical_context": "情報過多時代に知識を演出可能な空間として組織する欲求。",
    "primary_source_url": "https://archive.org/details/theatrumvitaehum01zwin",
    "primary_source_type": "Internet Archive — Zwinger Theatrum Vitae Humanae",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "コモンプレイス・ブック",
    "name_en": "Renaissance commonplace book",
    "name_original": "liber locorum communium",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "古典・聖書・現代著作からの引用を主題別（loci communes）に整理した近世の知識集成書記。エラスムス『格言集』、メランヒトン『神学要綱』が範を示し、人文主義教育の必須訓練となり、シェイクスピアら近世著者の創作の知的基盤となった。引用と独創の境界を流動化させた書記文化。",
    "background": "古代修辞学の loci 概念と中世スコラ学の sententiae 集成の融合。",
    "development": "ロック『教育論』、近代の備忘録文化、現代のデジタル・ノートテイキングに連続。",
    "historical_context": "印刷本時代の情報過多に対する個人的知識管理の制度化。",
    "primary_source_url": "https://archive.org/details/erasmusadagia00eras",
    "primary_source_type": "Internet Archive — Erasmus Adagia",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "コモンプレイス・ブックは「他者の言葉の集成から自己の創作を生む」近世実践であり、LLMの大規模コーパス→生成という構造の近世史的先行例として再読できる。",
         "related_ai_phenomenon": "LLM訓練コーパスと生成テクストの関係"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "LLM訓練コーパス",
         "description": "コモンプレイス・ブックの「集成→生成」構造とLLMの「コーパス→生成」構造の構造的類比。AI開発DBにおけるコーパス論議の歴史的前駆。"},
    ],
})

add({
    "name_ja": "イミタチオ・ウェテルム",
    "name_en": "imitatio veterum",
    "name_original": "imitatio veterum",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期・後期ルネサンス（伊・西・仏）",
    "definition": "「古代人の模倣」を意味する近世詩学の基底原理で、imitatio一般のなかで特に古代古典作家を範例とする規範的側面を指す。ベンボのキケロ／ペトラルカ単一模倣論争、エラスムス『キケロニアヌス』の批判、後の新古典主義の規範化を貫く近世人文主義の中核論題。",
    "background": "古代修辞学の模倣論とキリスト教模範論（imitatio Christi）の世俗的世俗化の合流。",
    "development": "ボワロー、ポープ、ジョンソン批評を経て、19世紀ロマン派による「独創性」概念の発明によって相対化される。",
    "historical_context": "古典再発見と俗語詩規範化の交差。",
    "primary_source_url": "https://archive.org/details/eraserridoublec00eras",
    "primary_source_type": "Internet Archive — Erasmus Ciceronianus",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "学識ある無知（ドクタ・イグノランチア）",
    "name_en": "learned ignorance",
    "name_original": "docta ignorantia",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ルネサンス（イタリア）",
    "definition": "ニコラウス・クザーヌス『学識ある無知について』（De docta ignorantia, 1440）が体系化した、有限知性が無限神を直接認識し得ぬことを最高知識として承認する近世神秘主義的・哲学的詩学。後のジョルダーノ・ブルーノ、モンテーニュの「Que sais-je」、シェイクスピアの懐疑論的瞬間に思想的水脈を提供した。",
    "background": "中世神秘神学（マイスター・エックハルト）と新プラトン主義の合流。",
    "development": "モンテーニュ的試行、デカルト方法的懐疑、近代懐疑論の文学的伝統に継承。",
    "historical_context": "中世末期の知の限界の発見と人文主義の自己定義。",
    "primary_source_url": "https://archive.org/details/learnedignoranc00cusa",
    "primary_source_type": "Internet Archive — Cusanus De Docta Ignorantia",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "学識ある無知",
         "description": "哲学DBの近世初期形而上学の起点として共有される。"},
    ],
})


# ---------------------------------------------------------------
# Relations payload
# ---------------------------------------------------------------

RELATIONS: list[tuple[str, str, str, str]] = [
    ("人文主義", "イミタチオ（模倣）", "contains",
     "人文主義教育はイミタチオを実践原理として組み込んだ。"),
    ("人文主義", "コピア（豊穣）", "contains",
     "コピアは人文主義ラテン教育の中核訓練。"),
    ("人文主義", "俗語の高揚", "influences",
     "古典学習が俗語の文学的高雅化要求を生んだ。"),
    ("人文主義", "コモンプレイス・ブック", "contains",
     "コモンプレイス・ブックは人文主義的知識編成の制度的形態。"),
    ("エラスミアニズム", "人文主義", "extends",
     "エラスミアニズムは北方人文主義の極限的発展形。"),
    ("エラスミアニズム", "コピア（豊穣）", "contains",
     "エラスムス『コピア論』は北方人文主義教育の中核教材。"),
    ("プレイヤード派", "ペトラルキスム", "extends",
     "プレイヤード派はフランス語ペトラルキスムの推進者。"),
    ("プレイヤード派", "俗語の高揚", "extends",
     "デュ・ベレー『擁護と顕揚』は俗語高揚運動の綱領。"),
    ("プレイヤード派", "イミタチオ（模倣）", "contains",
     "プレイヤード派は古典・伊詩の模倣を国民詩構築の原理とした。"),
    ("ペトラルキスム", "ソネット", "contains",
     "ペトラルキスムはソネット連作を中心形式とする。"),
    ("ペトラルキスム", "ペトラルカ的コンチェット", "contains",
     "ペトラルキスムの修辞語彙の中核がペトラルカ的コンチェット。"),
    ("ペトラルキスム", "宮廷恋愛の再考", "extends",
     "ペトラルキスムは中世宮廷恋愛の近世的再構成。"),
    ("ペトラルキスム", "ダンテ『新生』の遺産", "extends",
     "ペトラルカ『カンツォニエーレ』は『新生』形式の継承的展開。"),
    ("カスティーリャ黄金時代", "ピカレスク小説", "contains",
     "ピカレスク小説は黄金世紀スペインの代表的散文形式。"),
    ("カスティーリャ黄金時代", "セルバンテス的対話主義", "contains",
     "セルバンテス対話主義は黄金世紀の最大成果。"),
    ("エリザベス朝演劇", "シェイクスピア演劇", "contains",
     "シェイクスピア演劇はエリザベス朝演劇の頂点。"),
    ("エリザベス朝演劇", "シェイクスピア的無韻詩", "contains",
     "無韻詩はエリザベス朝演劇の中核的韻律。"),
    ("エリザベス朝演劇", "テアトルム・ムンディ（世界劇場）", "contains",
     "テアトルム・ムンディはエリザベス朝演劇の自己反映的中心比喩。"),
    ("エリザベス朝演劇", "マスク（仮面劇）", "contains",
     "マスクはエリザベス朝・ジャコビアン期の宮廷劇形式。"),
    ("形而上派詩人", "ペトラルカ的コンチェット", "criticizes",
     "形而上派詩人はペトラルキスムの陳腐化に反発し、知的劇化されたコンチェットを発展させた。"),
    ("形而上派詩人", "可滅的肉体（メメント・モリ）", "contains",
     "ジョン・ダンらは肉体可滅性の主題を詩的に深化させた。"),
    ("スプレッツァトゥーラ", "宮廷恋愛の再考", "influences",
     "宮廷人理想としてのスプレッツァトゥーラは恋愛詩の流麗さ規範に連続。"),
    ("スプレッツァトゥーラ", "デコルム（適切さ）", "extends",
     "スプレッツァトゥーラはデコルムの宮廷的特殊化。"),
    ("ソネット", "ペトラルカ的コンチェット", "contains",
     "ソネット形式はペトラルカ的コンチェットの収納器。"),
    ("ソネット", "シェイクスピア的無韻詩", "influences",
     "ソネットの弱強五歩格は無韻詩の韻律基盤。"),
    ("牧歌劇／パストラル", "シェイクスピア演劇", "influences",
     "『お気に召すまま』はパストラルの劇形式化。"),
    ("ピカレスク小説", "セルバンテス的対話主義", "influences",
     "ピカレスクの一人称下層描写がセルバンテス対話主義の素材を準備。"),
    ("エセー（モンテーニュ）", "モンテーニュ的試行", "contains",
     "モンテーニュ的試行はエセーの方法的核心。"),
    ("エセー（モンテーニュ）", "学識ある無知（ドクタ・イグノランチア）", "extends",
     "「Que sais-je」は学識ある無知の近世的継承。"),
    ("シェイクスピア演劇", "テアトルム・ムンディ（世界劇場）", "contains",
     "シェイクスピア劇の自己反映性は世界劇場比喩の文学的頂点。"),
    ("シェイクスピア演劇", "メランコリー", "contains",
     "ハムレットはメランコリー主題の悲劇的形象化。"),
    ("シェイクスピア演劇", "可滅的肉体（メメント・モリ）", "contains",
     "ハムレット墓場場面は可滅性主題の劇的提示。"),
    ("マスク（仮面劇）", "ウト・ピクトゥラ・ポエシス", "extends",
     "マスクは詩・絵画・音楽の総合実践として ut pictura poesis を体現。"),
    ("エンブレム本", "ウト・ピクトゥラ・ポエシス", "extends",
     "エンブレム本は ut pictura poesis 原理の制度的具現化。"),
    ("ノヴェッラ", "シェイクスピア演劇", "influences",
     "シェイクスピアは『ロミオとジュリエット』等で伊ノヴェッラを劇化した。"),
    ("ノヴェッラ", "ピカレスク小説", "influences",
     "ノヴェッラの世俗的物語伝統がピカレスク小説の前提を成す。"),
    ("イミタチオ（模倣）", "イミタチオ・ウェテルム", "contains",
     "イミタチオ・ウェテルムはイミタチオの古典範例特化形態。"),
    ("イミタチオ（模倣）", "コピア（豊穣）", "influences",
     "複数源泉模倣がコピア訓練を要求する。"),
    ("イミタチオ（模倣）", "コモンプレイス・ブック", "influences",
     "イミタチオはコモンプレイス・ブックを実践基盤とする。"),
    ("デコルム（適切さ）", "詩論（アルス・ポエティカ）の復興", "extends",
     "デコルムは古典詩学復興の中心規範。"),
    ("ウト・ピクトゥラ・ポエシス", "詩論（アルス・ポエティカ）の復興", "contains",
     "ut pictura poesis はホラティウス『詩論』再受容の標語。"),
    ("テアトルム・ムンディ（世界劇場）", "劇場の比喩", "extends",
     "テアトルム・ムンディは劇場メタファーの形而上学的拡張。"),
    ("メランコリー", "可滅的肉体（メメント・モリ）", "influences",
     "メランコリーは可滅性主題の心理化。"),
    ("宮廷恋愛の再考", "ダンテ『新生』の遺産", "extends",
     "近世宮廷恋愛詩は『新生』形式に直接連続する。"),
    ("ペトラルカ的コンチェット", "シドニー『詩の擁護』", "influences",
     "シドニーはペトラルカ的修辞を英国に擁護的に紹介した。"),
    ("シェイクスピア的無韻詩", "タッソの英雄叙事詩", "extends",
     "ミルトン経由でタッソ英雄詩構造が無韻詩英語叙事詩に継承される。"),
    ("セルバンテス的対話主義", "ピカレスク小説", "extends",
     "セルバンテスはピカレスク小説の枠組みを対話主義に発展させた。"),
    ("ラブレー的カーニヴァル", "コピア（豊穣）", "extends",
     "ラブレーの饒舌は人文主義コピアの民衆的爆発。"),
    ("モンテーニュ的試行", "エセー（モンテーニュ）", "contains",
     "モンテーニュ的試行はエセーの構成原理。"),
    ("タッソの英雄叙事詩", "イミタチオ（模倣）", "extends",
     "タッソは古代叙事詩のイミタチオを近世化した。"),
    ("シドニー『詩の擁護』", "詩の擁護（ジャンルとして）", "contains",
     "シドニー著作は『詩の擁護』ジャンルの英国的成立。"),
    ("ダンテ『新生』の遺産", "ソネット", "influences",
     "『新生』形式がソネット連作伝統の基盤を成す。"),
    ("詩の擁護（ジャンルとして）", "詩論（アルス・ポエティカ）の復興", "contains",
     "詩の擁護は古典詩学復興の批評的応用。"),
    ("詩論（アルス・ポエティカ）の復興", "デコルム（適切さ）", "contains",
     "デコルムは古典詩学復興の中核規範概念。"),
    ("新旧論争前夜", "イミタチオ・ウェテルム", "criticizes",
     "近代擁護派は古典絶対化のイミタチオ・ウェテルムを批判。"),
    ("俗語の高揚", "プレイヤード派", "influences",
     "俗語高揚運動の綱領的実践がプレイヤード派。"),
    ("俗語の高揚", "ダンテ『新生』の遺産", "extends",
     "ダンテ『俗語論』および『新生』が俗語高揚運動の起点。"),
    ("劇場の比喩", "コモンプレイス・ブック", "influences",
     "「記憶劇場」（カミーロ）はコモンプレイス的知識集成の空間化。"),
    ("コモンプレイス・ブック", "イミタチオ・ウェテルム", "extends",
     "コモンプレイス書記は古代範例模倣の実践的形態。"),
    ("学識ある無知（ドクタ・イグノランチア）", "モンテーニュ的試行", "influences",
     "クザーヌスの学識ある無知が「Que sais-je」の思想的水脈。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[wave4_c05_renaissance] inserting {len(CONCEPTS)} concepts...")
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
        print("[wave4_c05_renaissance] inserted:")
        print(f"  concepts (total): {summary['concepts']}")
        print(f"  fourth_transform_tags (total): {summary['fourth_transform_tags']} "
              f"(this run: +{fourth_count})")
        print(f"  cross_domain (total): {summary['cross_domain']} "
              f"(this run: +{cd_count})")
        print(f"  relations (total): {summary['relations']} "
              f"(this run: +{relation_count})")

        # Subfield-3 specific count
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 3"
        ).fetchone()
        print(f"  concepts in subfield_id=3 (Renaissance): {row['c']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
