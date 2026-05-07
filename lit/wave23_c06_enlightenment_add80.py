"""LIT-DB Phase 2 Wave 23 — C06: Enlightenment / Romanticism ADD 80.

Subfield: lit_eu_enlightenment (id=4).
Existing: 141 concepts. Target 500. This wave adds 80 NEW non-overlapping
covering: French Enlightenment expanded, British 18c expanded, Gothic
deeper, German Sturm und Drang/Klassik expanded, British Romantic
poetry expanded, German Romanticism expanded, Russian Romanticism
expanded, American Romanticism expanded.

Sources: Project Gutenberg, Wikisource (en/fr/de/it/es/ru), Frantext,
BVMC, archive.org. Primary >= 85%.
Targets: fourth_transform_tags >= 24, cross_domain >= 18.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("18世紀フランス啓蒙拡張期", "French Enlightenment Expanded (18th c.)",
     1715, 1789,
     "ディドロ・ヴォルテール・ルソー・マリヴォー・プレヴォ・ボーマルシェ・ラクロ・サド・レチフ・クレビヨン・シャンフォール・リヴァロルを擁する啓蒙散文・劇・モラリストの成熟期。"),
    ("18世紀英国小説興隆期", "British 18th-century Novel",
     1700, 1800,
     "デフォー・リチャードソン・フィールディング・スターン・スモレット・バーニー・ジョンソン・ボズウェル・ギボンを擁する英国小説・批評・伝記の興隆期。"),
    ("ゴシック小説深化期", "Gothic Novel Deeper",
     1764, 1830,
     "ウォルポール・リーヴ・ラドクリフ・ルイス・マチューリン・ホッグを擁するゴシック小説の深化と多様化期。"),
    ("ドイツ・シュトゥルム・ウント・ドラング期", "German Sturm und Drang / Klassik",
     1760, 1830,
     "クロップシュトック・レッシング・ヴィーラント・ヘルダー・ゲーテ・シラー・ヘルダーリン・ジャン・パウル・モーリッツ・ヴァッケンローダー・クライストを擁する疾風怒濤期からヴァイマル古典主義・初期ロマン派。"),
    ("英国ロマン主義詩期", "British Romantic Poetry",
     1780, 1840,
     "ワーズワース・コールリッジ・ブレイク・キーツ・シェリー・バイロン・ラム・ハズリット・ド・クィンシーを擁する英国ロマン主義詩・散文の中核期。"),
    ("ドイツ・ロマン派期", "German Romanticism",
     1795, 1840,
     "シュレーゲル兄弟・ノヴァーリス・ティーク・ブレンターノ・アイヒェンドルフ・E.T.A.ホフマン・ヴァッケンローダーを擁するイエナ・ハイデルベルク・ベルリン・ロマン派の連続期。"),
    ("ロシア・ロマン主義期", "Russian Romanticism",
     1815, 1845,
     "プーシキン・レールモントフ・ゴーゴリ・ジュコフスキー・バラトィンスキー・チュッチェフ・フェートを中心とするロシア近代文学黄金期初頭。"),
    ("米国ロマン主義期", "American Romanticism",
     1820, 1865,
     "ホーソーン・メルヴィル・ポー・エマソン・ソロー・ホイットマン・ディキンソン・フラーを擁するアメリカン・ルネサンス期。"),
]


GUTEN = "https://www.gutenberg.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WIKI_RU = "https://ru.wikipedia.org/wiki/"
WSRC_FR = "https://fr.wikisource.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
WSRC_DE = "https://de.wikisource.org/wiki/"
WSRC_RU = "https://ru.wikisource.org/wiki/"
ARCH = "https://archive.org/details/"
FRANTEXT = "https://www.frantext.fr/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_eu_enlightenment", region="西欧",
         original_script="roman")
CRU = dict(subfield_code="lit_eu_enlightenment", region="ロシア",
           original_script="cyrillic")
CAM = dict(subfield_code="lit_eu_enlightenment", region="米国",
           original_script="roman")


# ============================================================
# A: French Enlightenment Expanded (12 NEW)
# ============================================================
add(**C, name_ja="ディドロ『盲人書簡』",
    name_en="Diderot's Lettre sur les aveugles",
    name_original="Lettre sur les aveugles à l'usage de ceux qui voient",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ディドロが1749年に発表した哲学書簡。盲人の知覚から唯物論的認識論を展開し、ヴァンセンヌ投獄の直接原因となった啓蒙期感覚論文学の起点。",
    background="ロック・コンディヤック感覚論の継承、モリヌー問題の哲学的応用。",
    development="後の『百科全書』『ダランベールの夢』へ連続する唯物論散文の祖型。",
    historical_context="1749年フランス王権下の検閲・投獄事件。",
    primary_source_url=WSRC_FR+"Lettre_sur_les_aveugles",
    primary_source_type="Wikisource FR: Lettre sur les aveugles",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"盲人の知覚論はマルチモーダル知覚理論の祖型。AIの感覚モダリティ統合と理論的に共振。",
        "related_ai_phenomenon":"マルチモーダルAI・知覚的差異"}],
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"感覚論",
        "description":"『盲人書簡』はロック・コンディヤック感覚論の文学的具体化。"}])

add(**C, name_ja="ディドロ『ラモーの甥』",
    name_en="Diderot's Le Neveu de Rameau",
    name_original="Le Neveu de Rameau",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ディドロが1761-74年頃執筆した対話篇。哲学者「私」と作曲家ラモーの甥との皮肉な対話で、社会的偽善・芸術・道徳を解体的に検討する。ゲーテ独訳(1805)で発見され、ヘーゲル『精神現象学』が引用したことで近代哲学の中心テクストとなった。",
    background="リバティナージュ思想と18世紀対話篇形式の独自統合、生前未刊。",
    development="ゲーテ訳(1805)、ヘーゲル『精神現象学』B章自己疎外論の中心参照、フロイト・ラカンによる再読。",
    historical_context="七年戦争後のパリ・カフェ文化と新興音楽論争。",
    primary_source_url=GUTEN+"ebooks/2092",
    primary_source_type="Project Gutenberg: Le Neveu de Rameau",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"主体","status":"rethinking",
        "rationale":"ラモーの甥の自己疎外的多声性は、AI時代の主体分裂・複数自己と理論的に共振。",
        "related_ai_phenomenon":"AI多声主体の祖型"}],
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"自己疎外（ヘーゲル）",
        "description":"ヘーゲル『精神現象学』の自己疎外論の中心参照テクスト。"}])

add(**C, name_ja="ディドロ『運命論者ジャック』",
    name_en="Diderot's Jacques le fataliste",
    name_original="Jacques le fataliste et son maître",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ディドロが1771-78年頃執筆した小説。スターン『トリストラム・シャンディ』に倣う自意識的脱線形式で、ジャックと主人の旅を語る。決定論と自由意志の哲学的論争を散文形式で展開し、20世紀メタフィクション論の重要な祖型となった。",
    background="スターン受容、ライプニッツ・スピノザ決定論の文学化。",
    development="クンデラ『不滅』『笑いと忘却の書』の直接的源泉、20世紀メタフィクション論の祖型。",
    historical_context="ルイ16世期パリ・サロンと出版検閲。",
    primary_source_url=GUTEN+"ebooks/16921",
    primary_source_type="Project Gutenberg: Jacques le fataliste",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"物語","status":"rethinking",
        "rationale":"自意識的脱線・決定論論議はAI生成の経路依存性と理論的に共振。",
        "related_ai_phenomenon":"AI生成の確率的決定論"}])

add(**C, name_ja="ディドロ『ブーガンヴィル航海記補遺』",
    name_en="Diderot's Supplément au voyage de Bougainville",
    name_original="Supplément au voyage de Bougainville",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ディドロが1772年執筆の対話篇。ブーガンヴィルのタヒチ航海記への文学的補遺として、自然状態と西洋文明の対比を通じ植民地批判・性倫理批判を展開。18世紀末異文化遭遇文学の最高水準。",
    background="ブーガンヴィル『世界周航記』(1771)、ルソー自然状態論の小説化。",
    development="19-20世紀のオリエンタリズム批判、ポストコロニアル文学論の祖型。",
    historical_context="七年戦争敗北後のフランス植民地政策再考期。",
    primary_source_url=WSRC_FR+"Suppl%C3%A9ment_au_voyage_de_Bougainville",
    primary_source_type="Wikisource FR: Supplément",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"異文化遭遇・自然状態",
        "description":"人類学DB側の自然状態・タヒチ研究と直接接続する文学的祖型。"}])

add(**C, name_ja="ヴォルテール『哲学辞典』",
    name_en="Voltaire's Dictionnaire philosophique",
    name_original="Dictionnaire philosophique portatif",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ヴォルテールが1764年に発表した哲学辞典。アルファベット順の項目で宗教・形而上学・政治を風刺的に解説する。18世紀フランス啓蒙批評形式の代表作で、現代百科批評・短文批評の祖型となった。",
    background="ベール『歴史批評辞典』の継承、百科全書派との連携と独自路線。",
    development="19世紀フローベール『紋切型辞典』、20世紀バルト『批評と真実』の祖型。",
    historical_context="七年戦争後のフェルネー隠棲期、宗教的不寛容批判運動。",
    primary_source_url=GUTEN+"ebooks/18569",
    primary_source_type="Project Gutenberg: Dictionnaire philosophique",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴォルテール『哲学書簡』",
    name_en="Voltaire's Lettres philosophiques",
    name_original="Lettres philosophiques (Lettres anglaises)",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ヴォルテールが1734年に発表した英国観察記。ロンドン亡命中(1726-29)の経験を25通の書簡形式で構成し、ニュートン物理学・ロック哲学・英国議会政治を仏に紹介。フランス啓蒙運動の起点とされる。",
    background="ロンドン亡命体験、ベイユ書簡形式の継承。",
    development="百科全書派・モンテスキュー『法の精神』への直接的影響、英仏文化交流の起点。",
    historical_context="1734年フランス王権下の検閲・焚書事件。",
    primary_source_url=GUTEN+"ebooks/2708",
    primary_source_type="Project Gutenberg: Lettres philosophiques",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴォルテール『ミクロメガス』",
    name_en="Voltaire's Micromégas",
    name_original="Micromégas",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ヴォルテールが1752年発表の哲学コント。シリウス星人と土星人が地球を訪問し、人類の小ささを観察する短編。18世紀SF文学の祖型で、スウィフト『ガリヴァー旅行記』の仏応答として近代SFの出発点となった。",
    background="スウィフト・キルヒャー宇宙論受容、ニュートン物理学普及運動。",
    development="ジュール・ヴェルヌ・H.G.ウェルズに先駆ける近代SFの祖型。",
    historical_context="1750年代パリ・宮廷からベルリン宮廷までの移動期。",
    primary_source_url=GUTEN+"ebooks/30123",
    primary_source_type="Project Gutenberg: Micromégas",
    importance_score=3, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"主体","status":"rethinking",
        "rationale":"異星的視点による人類相対化はAI視点の人間観察と理論的に共振。",
        "related_ai_phenomenon":"AI外部視点による人類相対化"}])

add(**C, name_ja="ヴォルテール『ザディーグ』",
    name_en="Voltaire's Zadig",
    name_original="Zadig ou la Destinée",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ヴォルテールが1747年発表の東洋風哲学コント。バビロンの賢者ザディーグの遍歴を通じ、運命と摂理の問題を諷刺的に検討する。『カンディード』前駆作として啓蒙オリエンタリズム文学の代表作。",
    background="『千夜一夜物語』ガラン仏訳(1704-17)以後のオリエンタリズム流行。",
    development="『カンディード』(1759)に直結する哲学コント形式の確立。",
    historical_context="1740年代後半のシレジー戦争期パリ・宮廷文化。",
    primary_source_url=GUTEN+"ebooks/4647",
    primary_source_type="Project Gutenberg: Zadig",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ルソー『学問芸術論』",
    name_en="Rousseau's Discourse on Sciences and Arts",
    name_original="Discours sur les sciences et les arts",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ルソーが1750年ディジョン・アカデミー懸賞で受賞した論考。「学問・芸術の復興は風俗の純化に貢献したか」に否と答え、文明批判思想を初めて公表した。ルソー思想体系の出発点で、18世紀啓蒙との緊張を体現する文学的論争作。",
    background="ディジョン・アカデミー懸賞論文形式、ルソーの思想的転換期。",
    development="『人間不平等起源論』(1755)、『社会契約論』(1762)へ連なるルソー思想体系の起点。",
    historical_context="1750年代啓蒙ペシミズムの最初期表現。",
    primary_source_url=GUTEN+"ebooks/40233",
    primary_source_type="Project Gutenberg: Discours sur les sciences",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ルソー『人間不平等起源論』",
    name_en="Rousseau's Discourse on Inequality",
    name_original="Discours sur l'origine et les fondements de l'inégalité",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ルソーが1755年に発表した社会哲学論考。自然状態における人間の善性と、私有財産発生による不平等の歴史を散文叙事詩風に語る。18世紀文学的哲学論考の最高峰で、近代社会理論の起点。",
    background="ホッブズ・ロック自然状態論への対抗、推測的歴史叙述の文学化。",
    development="マルクス『資本論』『経済学・哲学草稿』、レヴィ＝ストロース『悲しき熱帯』の中心参照点。",
    historical_context="百科全書派全盛期、啓蒙的進歩観への根底批判。",
    primary_source_url=GUTEN+"ebooks/11136",
    primary_source_type="Project Gutenberg: Discours sur l'inégalité",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"自然状態論",
        "description":"近代社会理論の出発点として哲学DBの社会契約論項目と直接接続。"},
        {"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"レヴィ＝ストロース・推測的歴史",
        "description":"レヴィ＝ストロースの推測的人類学の文学的祖型。"}])

add(**C, name_ja="ボーマルシェ『セビリアの理髪師』",
    name_en="Beaumarchais's Le Barbier de Séville",
    name_original="Le Barbier de Séville",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ボーマルシェが1775年に上演した喜劇。フィガロ三部作の第一作で、機知に富む下僕フィガロが伯爵の恋を助ける筋書き。革命前夜の身分風刺の起点で、ロッシーニ・オペラ(1816)化により世界的古典となった。",
    background="モリエール喜劇伝統の継承、第三身分台頭期のサロン文化。",
    development="『フィガロの結婚』(1784)、『罪深き母』(1792)に続く三部作の起点、ロッシーニ・オペラ。",
    historical_context="アメリカ独立戦争期前夜のフランス社会的緊張。",
    primary_source_url=GUTEN+"ebooks/20581",
    primary_source_type="Project Gutenberg: Le Barbier de Séville",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クレビヨン・フィス『ソファ』",
    name_en="Crébillon fils's Le Sopha",
    name_original="Le Sopha, conte moral",
    period_key="18世紀フランス啓蒙拡張期",
    definition="クロード・プロスペル・ジョリオ・ド・クレビヨン（1707-1777、息子）が1742年発表のオリエンタル風小説。前世がソファだった語り手が、その上で起こった恋愛を語る枠物語。18世紀リバティナージュ文学・ロココ小説の代表作で、後のディドロ『おしゃべりな宝石』に直接連なる。",
    background="ガラン『千夜一夜』仏訳以後のオリエンタリズム流行と、レジャンス期リバティナージュ文学。",
    development="ディドロ『おしゃべりな宝石』(1748)、19世紀末デカダン文学の祖型。",
    historical_context="1740年代パリ・宮廷文化のロココ的耽美期。",
    primary_source_url=GUTEN+"ebooks/30923",
    primary_source_type="Project Gutenberg: Le Sopha",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# B: British 18c Expanded (10 NEW)
# ============================================================
add(**C, name_ja="リチャードソン『チャールズ・グランディソン卿』",
    name_en="Richardson's Sir Charles Grandison",
    name_original="The History of Sir Charles Grandison",
    period_key="18世紀英国小説興隆期",
    definition="リチャードソンが1753-54年に発表した7巻書簡体小説。理想的紳士チャールズ・グランディソン卿を中心に、英国紳士道徳の典範を提示。リチャードソン三部作の最終巻で、19世紀英国紳士小説の祖型となった。",
    background="『パメラ』『クラリッサ』後の理想化路線、英国ジェントルマン理念の文学化。",
    development="ジェイン・オースティン『マンスフィールド・パーク』への直接的影響、19世紀英国ジェントルマン小説の祖型。",
    historical_context="1750年代英国の紳士階級拡大とマナー論議。",
    primary_source_url=GUTEN+"ebooks/55459",
    primary_source_type="Project Gutenberg: Sir Charles Grandison",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フィールディング『アミリア』",
    name_en="Fielding's Amelia",
    name_original="Amelia",
    period_key="18世紀英国小説興隆期",
    definition="フィールディングが1751年発表の最後の長編小説。貧困・不貞・債務に苦しむブース夫妻を描き、初期社会問題小説の祖型を成した。ウェルギリウス『アエネイス』を構造的範に、フィールディング小説論の到達点を示す。",
    background="ロンドン治安判事としての社会観察、ウェルギリウス模範の継続。",
    development="ディケンズ社会問題小説、19世紀英国家庭小説の祖型。",
    historical_context="1750年代ロンドン都市犯罪・貧困問題期。",
    primary_source_url=GUTEN+"ebooks/6098",
    primary_source_type="Project Gutenberg: Amelia",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="スモレット『ハンフリー・クリンカー』",
    name_en="Smollett's Humphry Clinker",
    name_original="The Expedition of Humphry Clinker",
    period_key="18世紀英国小説興隆期",
    definition="トバイアス・スモレット（1721-1771）が1771年発表の最後の小説。書簡体形式で英国・スコットランド旅行を多視点で描き、18世紀英国旅行小説・地方主義文学の頂点を成した。",
    background="リチャードソン書簡体とフィールディング社会観察の総合、18世紀英国旅行文学の流行。",
    development="ジェイン・オースティン旅行描写、19世紀英国地方主義小説の祖型。",
    historical_context="1770年代英国・スコットランド統合後の文化的交流。",
    primary_source_url=GUTEN+"ebooks/2160",
    primary_source_type="Project Gutenberg: Humphry Clinker",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スモレット『ロデリック・ランダム』",
    name_en="Smollett's Roderick Random",
    name_original="The Adventures of Roderick Random",
    period_key="18世紀英国小説興隆期",
    definition="スモレットが1748年発表のピカレスク小説。スコットランド出身青年ロデリックの遍歴・海軍体験・不正告発を一人称で描く。英国海軍・植民地経験の文学化として、19世紀英国海洋小説の祖型となった。",
    background="ル・サージュ『ジル・ブラース』翻訳経験、スモレット自身の海軍軍医体験。",
    development="マリアットの海洋小説、19世紀英国冒険小説の祖型。",
    historical_context="オーストリア継承戦争期(1740-48)英国海軍経験。",
    primary_source_url=GUTEN+"ebooks/4085",
    primary_source_type="Project Gutenberg: Roderick Random",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="スターン『センチメンタル・ジャーニー』",
    name_en="Sterne's A Sentimental Journey",
    name_original="A Sentimental Journey Through France and Italy",
    period_key="18世紀英国小説興隆期",
    definition="スターンが1768年発表の旅行記風小説。語り手ヨリック牧師のフランス旅行を、感受性と機知で描く断片的形式。「センチメンタル」の語を文学的に確立し、18世紀後半感傷文学の起点となった。",
    background="『トリストラム・シャンディ』成功後の旅行体験、ロック『感性論』受容。",
    development="ゲーテ『ウェルテル』、ロシア（カラムジン『露国旅行記』）、19世紀感傷文学の祖型。",
    historical_context="1768年英国大陸旅行（グランド・ツアー）文化期。",
    primary_source_url=GUTEN+"ebooks/804",
    primary_source_type="Project Gutenberg: A Sentimental Journey",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョンソン『英語辞典』序文",
    name_en="Johnson's Preface to the Dictionary",
    name_original="Preface to A Dictionary of the English Language",
    period_key="18世紀英国小説興隆期",
    definition="サミュエル・ジョンソン（1709-1784）が1755年に発表した『英語辞典』序文。9年間の単独編纂事業の理論的総括として、英語の歴史性・規範性・変化を論じる18世紀英国散文の最高水準。英語学・辞書学の祖型。",
    background="アカデミー・フランセーズ『辞典』への英国的応答、ジョンソン9年間の単独編纂作業。",
    development="近代英語辞書編纂の起点、20世紀OED編纂の理論的祖型。",
    historical_context="1755年英国の言語的国民意識形成期。",
    primary_source_url=GUTEN+"ebooks/29765",
    primary_source_type="Project Gutenberg: Johnson Dictionary Preface",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"単独編纂による言語規範化はAI言語モデルの言語規範形成と理論的に共振。",
        "related_ai_phenomenon":"AI言語モデルの規範化機能"}])

add(**C, name_ja="ジョンソン『詩人列伝』",
    name_en="Johnson's Lives of the Poets",
    name_original="The Lives of the Most Eminent English Poets",
    period_key="18世紀英国小説興隆期",
    definition="ジョンソンが1779-81年に発表した英国詩人52名の伝記批評集。ミルトン・ドライデン・ポープ等の生涯と作品を、新古典主義的批評基準で評価する。英国近代文学批評・伝記批評の祖型。",
    background="ミルトン以降英国詩史の総括、新古典主義批評基準の体系化。",
    development="19-20世紀英国文学史叙述、ハロルド・ブルーム『西欧正典』の祖型。",
    historical_context="1780年前後英国の国民文学正典形成期。",
    primary_source_url=GUTEN+"ebooks/4673",
    primary_source_type="Project Gutenberg: Lives of the Poets",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"正典","status":"rethinking",
        "rationale":"ジョンソン詩人列伝は英国正典の形成的編纂であり、AIによる正典再編・推薦機能と理論的に共振。",
        "related_ai_phenomenon":"AIによる正典編纂・推薦"}])

add(**C, name_ja="ジョンソン『ラセラス』",
    name_en="Johnson's Rasselas",
    name_original="The History of Rasselas, Prince of Abissinia",
    period_key="18世紀英国小説興隆期",
    definition="ジョンソンが1759年に1週間で執筆した東洋風哲学コント。アビシニア王子ラセラスが幸福の本質を求めて世界遍歴する筋書き。母の葬儀費用捻出のため執筆され、ヴォルテール『カンディード』と同年発表のため対照的読解の対象となった。",
    background="母の死、ガラン『千夜一夜』翻訳以後の東洋風哲学コント流行。",
    development="ヴォルテール『カンディード』との並行、19世紀英国哲学小説の祖型。",
    historical_context="1759年七年戦争期英国の哲学的悲観主義論議。",
    primary_source_url=GUTEN+"ebooks/652",
    primary_source_type="Project Gutenberg: Rasselas",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ボズウェル『ジョンソン伝』",
    name_en="Boswell's Life of Johnson",
    name_original="The Life of Samuel Johnson, LL.D.",
    period_key="18世紀英国小説興隆期",
    definition="ジェイムズ・ボズウェル（1740-1795）が1791年発表の伝記。20年余のジョンソンとの交流に基づく綿密な日常会話・観察記録で、近代伝記文学の決定的傑作となった。「ボズウェル的」が綿密記録の代名詞となるほど影響を残した。",
    background="20年以上のボズウェル日記実践、ジョンソン晩年の親密な交流期。",
    development="近代伝記文学の祖型、20世紀リットン・ストレイチー『ヴィクトリア朝偉人伝』への系譜。",
    historical_context="ジョージ朝後期英国・スコットランド文人交流期。",
    primary_source_url=GUTEN+"ebooks/1564",
    primary_source_type="Project Gutenberg: Life of Johnson",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ギボン『ローマ帝国衰亡史』",
    name_en="Gibbon's Decline and Fall",
    name_original="The History of the Decline and Fall of the Roman Empire",
    period_key="18世紀英国小説興隆期",
    definition="エドワード・ギボン（1737-1794）が1776-89年に発表した6巻歴史書。1500年にわたるローマ帝国衰亡を、啓蒙的合理主義と懐疑的諷刺で叙述。歴史叙述としても文学としても18世紀英国散文の最高峰で、近代歴史叙述の祖型。",
    background="ローマ・カピトル丘での着想、啓蒙的合理主義と古典学的綿密性の統合。",
    development="19-20世紀近代歴史叙述の祖型、文体としても英国散文の規範。",
    historical_context="1770-80年代英国・スコットランド啓蒙期、フランス革命直前。",
    primary_source_url=GUTEN+"ebooks/731",
    primary_source_type="Project Gutenberg: Decline and Fall",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"啓蒙的歴史哲学",
        "description":"18世紀啓蒙的歴史叙述の文学的頂点として哲学DB歴史哲学項目と接続。"}])


# ============================================================
# C: Gothic Deeper (8 NEW)
# ============================================================
add(**C, name_ja="リーヴ『古英国男爵』",
    name_en="Reeve's The Old English Baron",
    name_original="The Old English Baron",
    period_key="ゴシック小説深化期",
    definition="クララ・リーヴ（1729-1807）が1778年発表のゴシック小説。ウォルポール『オトラント城』への意識的応答として、超自然事象を抑制した「リアル・ゴシック」を提唱。ラドクリフ的「説明されたゴシック」の祖型となった。",
    background="ウォルポール『オトラント城』批判と、女性読者層を意識した穏健化路線。",
    development="ラドクリフ『ユードルフォの謎』への直接的影響、英国ゴシック女性化の起点。",
    historical_context="1770年代英国の女性読書市場拡大期。",
    primary_source_url=GUTEN+"ebooks/13911",
    primary_source_type="Project Gutenberg: The Old English Baron",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ラドクリフ『イタリアン』",
    name_en="Radcliffe's The Italian",
    name_original="The Italian, or the Confessional of the Black Penitents",
    period_key="ゴシック小説深化期",
    definition="ラドクリフが1797年発表の最後の主要作。ナポリ・ローマを舞台に修道士スケドーニの陰謀と異端審問の恐怖を描く。ルイス『修道士』への応答として、女性的ゴシックの方法的成熟を示した。19世紀後期ゴシックへの直接的影響。",
    background="ルイス『修道士』(1796)への応答、フランス革命期の反カトリック感情。",
    development="ヴィクトリア朝ゴシック復興、ヘンリー・ジェイムズ・ホーソーンへの影響。",
    historical_context="1797年仏伊カトリック制度と英国プロテスタント感情。",
    primary_source_url=GUTEN+"ebooks/3094",
    primary_source_type="Project Gutenberg: The Italian",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ラドクリフ『森のロマンス』",
    name_en="Radcliffe's The Romance of the Forest",
    name_original="The Romance of the Forest",
    period_key="ゴシック小説深化期",
    definition="ラドクリフが1791年発表のゴシック小説。フランスの修道院廃墟で孤児アデリーンが直面する陰謀と恐怖を描く。『ユードルフォの謎』前駆作で、ラドクリフ的ゴシックの方法を確立した中期傑作。",
    background="ラドクリフ初期短編からの飛躍、フランス革命期の英国仏崇拝・恐怖混合心理。",
    development="『ユードルフォの謎』(1794)へ直結、ジェイン・オースティン『ノーサンガー・アビー』風刺対象。",
    historical_context="1791年フランス革命進行期の英国仏感情。",
    primary_source_url=GUTEN+"ebooks/4280",
    primary_source_type="Project Gutenberg: Romance of the Forest",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ルイス『修道士』",
    name_en="Lewis's The Monk",
    name_original="The Monk, A Romance",
    period_key="ゴシック小説深化期",
    definition="マシュー・グレゴリー・ルイス（1775-1818）が1796年に20歳で発表したゴシック小説。マドリードの修道士アンブロシオの堕落・近親相姦・悪魔契約を露骨に描く「男性ゴシック」「黒色ゴシック」の代表作。バイロン的英雄・19世紀デカダン文学の祖型。",
    background="ドイツ・シャウアーロマン受容、ラドクリフ的「説明されたゴシック」への対抗路線。",
    development="バイロン、ホフマン、ポー、ホーソーン、19世紀デカダン文学への直接的影響。",
    historical_context="1796年フランス革命進行期英国の道徳的反動。",
    primary_source_url=GUTEN+"ebooks/601",
    primary_source_type="Project Gutenberg: The Monk",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"主体","status":"rethinking",
        "rationale":"修道士の堕落構造はAI時代の倫理的境界侵犯シナリオと理論的に共振。",
        "related_ai_phenomenon":"AI生成における倫理的境界の侵犯"}])

add(**C, name_ja="マチューリン『放浪者メルモス』",
    name_en="Maturin's Melmoth the Wanderer",
    name_original="Melmoth the Wanderer",
    period_key="ゴシック小説深化期",
    definition="チャールズ・ロバート・マチューリン（1780-1824）が1820年発表のゴシック小説。150年の寿命と引き換えに魂を売ったメルモスの放浪を、入れ子構造の物語で描く。ゴシック小説の最高峰の一つで、19世紀デカダン文学・実存主義的恐怖の祖型。",
    background="アイルランド・プロテスタント牧師の異端的想像力、後期ゴシックの形而上学化。",
    development="バルザック『追放者』、ボードレール、ワイルド『ドリアン・グレイの肖像』、20世紀ボルヘスへの直接的影響。",
    historical_context="1820年アイルランド・プロテスタント教会期。",
    primary_source_url=GUTEN+"ebooks/41950",
    primary_source_type="Project Gutenberg: Melmoth the Wanderer",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"実存的恐怖・有限性",
        "description":"メルモスの不死性は実存哲学の有限性問題の文学的祖型。"}])

add(**C, name_ja="ホッグ『義とされた罪人の懺悔』",
    name_en="Hogg's Confessions of a Justified Sinner",
    name_original="The Private Memoirs and Confessions of a Justified Sinner",
    period_key="ゴシック小説深化期",
    definition="ジェイムズ・ホッグ（1770-1835）が1824年発表のスコットランド・ゴシック小説。極端カルヴァン主義者ロバートの分身体験と殺人を、二重叙述で描く。ドッペルゲンガー文学・心理ゴシックの祖型で、20世紀A.アンドレ・ジッド再評価以降世界古典化した。",
    background="スコットランド・カルヴァン主義神学批判、シュトゥルム・ウント・ドラング受容。",
    development="ドストエフスキー『二重人格』、スティーヴンソン『ジキル博士とハイド氏』、20世紀心理ゴシックの祖型。",
    historical_context="1820年代スコットランド宗教論争期。",
    primary_source_url=GUTEN+"ebooks/2276",
    primary_source_type="Project Gutenberg: Confessions of a Justified Sinner",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"主体","status":"rethinking",
        "rationale":"ドッペルゲンガー・分身体験はAI生成における複数自己・分身生成と理論的に共振。",
        "related_ai_phenomenon":"AIによる分身・複数自己生成"}])

add(**C, name_ja="ウォルポール『神秘の母』",
    name_en="Walpole's The Mysterious Mother",
    name_original="The Mysterious Mother",
    period_key="ゴシック小説深化期",
    definition="ウォルポールが1768年に私家版印刷した戯曲。近親相姦のテーマを扱う5幕悲劇で、生前は公演を拒否された。『オトラント城』に続くウォルポール・ゴシック実験で、19世紀バイロン『マンフレッド』の禁忌主題の祖型となった。",
    background="ストロベリー・ヒルでの私家版印刷実践、ウォルポールのゴシック多媒体実験。",
    development="バイロン『マンフレッド』『カイン』、19世紀禁忌主題ロマン主義劇の祖型。",
    historical_context="1768年英国の私家版印刷文化期。",
    primary_source_url=GUTEN+"ebooks/47028",
    primary_source_type="Project Gutenberg: The Mysterious Mother",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="マチューリン『ベルトラム』",
    name_en="Maturin's Bertram",
    name_original="Bertram, or The Castle of St. Aldobrand",
    period_key="ゴシック小説深化期",
    definition="マチューリンが1816年発表したゴシック悲劇。バイロン推奨でドルーリー・レーン上演に至り、ロマン派演劇の主要作となった。コールリッジ『文学的自伝』第23章でゴシック演劇批判の中心対象となった。",
    background="バイロン・ロマン派演劇支援、ドルーリー・レーン劇場のゴシック劇流行。",
    development="コールリッジ批判、19世紀ロマン派演劇論議の中心テクスト。",
    historical_context="1816年英国ナポレオン戦後のロマン派文化期。",
    primary_source_url=GUTEN+"ebooks/14660",
    primary_source_type="Project Gutenberg: Bertram",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# D: German Sturm und Drang / Klassik Expanded (10 NEW)
# ============================================================
add(**C, name_ja="レッシング『賢者ナータン』",
    name_en="Lessing's Nathan der Weise",
    name_original="Nathan der Weise",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="ゴットホルト・エフライム・レッシング（1729-1781）が1779年発表の宗教寛容劇。十字軍時代エルサレムを舞台に、ユダヤ人ナータン・キリスト教徒・ムスリムの三宗教対話を描く。三つの指輪の寓話を中心に、啓蒙的宗教寛容思想の劇的頂点を成した。",
    background="ゲッツェ正統派論争(1778)、レッシング・スピノザ論争期。",
    development="ハーバーマス『公共圏』、ハンス・コック『寛容論』、現代多文化主義の祖型。",
    historical_context="フリードリヒ大王期プロイセン啓蒙の宗教寛容論争期。",
    primary_source_url=GUTEN+"ebooks/3820",
    primary_source_type="Project Gutenberg: Nathan der Weise",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"啓蒙的寛容論",
        "description":"啓蒙的宗教寛容思想の劇的中心テクスト。"}])

add(**C, name_ja="レッシング『エミーリア・ガロッティ』",
    name_en="Lessing's Emilia Galotti",
    name_original="Emilia Galotti",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="レッシングが1772年発表の市民悲劇。古代ヴィルギニア説話を翻案し、君主の専横に対する市民娘エミーリアの自死で抗議させる。ドイツ市民悲劇形式の頂点で、ゲーテ『ウェルテル』『ヴィルヘルム・マイスター』へ直接的影響。",
    background="ディドロ市民劇論受容、絶対主義への市民層批判。",
    development="シラー『たくらみと恋』、19世紀ドイツ市民劇、ヘッベル悲劇への祖型。",
    historical_context="1772年プロイセン・小邦国家の絶対主義期。",
    primary_source_url=GUTEN+"ebooks/2447",
    primary_source_type="Project Gutenberg: Emilia Galotti",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クロップシュトック『メシアス』",
    name_en="Klopstock's Der Messias",
    name_original="Der Messias",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="フリードリヒ・ゴットリープ・クロップシュトック（1724-1803）が1748-73年に発表した20歌の宗教叙事詩。ミルトン『失楽園』に倣いキリスト受難を六歩格で歌う。18世紀ドイツ詩の劇的更新で、シュトゥルム・ウント・ドラング・ヘルダーリンの宗教詩学の祖型。",
    background="ミルトン受容、ピエティスムス神学、六歩格ドイツ詩の確立。",
    development="ヘルダーリン宗教詩、19世紀ドイツ宗教叙事詩、20世紀宗教詩学。",
    historical_context="プロイセン啓蒙期の宗教詩学運動。",
    primary_source_url=GUTEN+"ebooks/14237",
    primary_source_type="Project Gutenberg: Der Messias",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ゲーテ『ゲッツ・フォン・ベルリヒンゲン』",
    name_en="Goethe's Götz von Berlichingen",
    name_original="Götz von Berlichingen mit der eisernen Hand",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="ゲーテが1773年発表のシェイクスピア風歴史劇。16世紀ドイツの鉄手騎士ゲッツの自由・没落を描き、シュトゥルム・ウント・ドラング演劇形式の起点となった。当時23歳のゲーテの劇作家としての登場作。",
    background="シェイクスピア独受容、ヘルダーとのシュトラスブルク交友、ドイツ国民劇の追求。",
    development="シラー『群盗』、シュトゥルム・ウント・ドラング劇、19世紀ドイツ歴史劇。",
    historical_context="1770年代ドイツ青年知識人の国民意識形成期。",
    primary_source_url=GUTEN+"ebooks/2321",
    primary_source_type="Project Gutenberg: Götz von Berlichingen",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ゲーテ『エグモント』",
    name_en="Goethe's Egmont",
    name_original="Egmont",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="ゲーテが1788年発表の歴史悲劇。16世紀ネーデルラント解放戦争のエグモント伯の悲劇を描く。ベートーヴェン序曲(1810)で世界古典化し、ヴァイマル古典主義劇の代表作。",
    background="ヴァイマル滞在期の歴史劇構想、シラーとの古典主義劇論議。",
    development="ベートーヴェン序曲、19世紀ドイツ国民劇、ヴァイマル古典主義劇の祖型。",
    historical_context="フランス革命直前のヨーロッパ自由論議期。",
    primary_source_url=GUTEN+"ebooks/1945",
    primary_source_type="Project Gutenberg: Egmont",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ゲーテ『タウリスのイフィゲーニエ』",
    name_en="Goethe's Iphigenie auf Tauris",
    name_original="Iphigenie auf Tauris",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="ゲーテが1779年散文版・1787年韻文版を発表した古典悲劇。エウリピデス『タウリケのイピゲネイア』を翻案し、女性の倫理的力で蛮族・血の呪詛を超越させる。ヴァイマル古典主義人道主義の頂点。",
    background="エウリピデス古典学受容、シャルロッテ・フォン・シュタインへの献呈。",
    development="シラー『ヴァレンシュタイン』、19世紀ドイツ古典劇、ヴァイマル人道主義の規範。",
    historical_context="1780年代前半ヴァイマル古典主義成熟期。",
    primary_source_url=GUTEN+"ebooks/2054",
    primary_source_type="Project Gutenberg: Iphigenie auf Tauris",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ゲーテ『親和力』",
    name_en="Goethe's Elective Affinities",
    name_original="Die Wahlverwandtschaften",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="ゲーテが1809年発表の長編小説。化学的「親和力」概念を結婚・恋愛関係に類比し、四人の人物の運命的引力・破局を描く。ヴァルター・ベンヤミン『ゲーテの親和力』(1922)が現代批評の中心テクストとして再評価。",
    background="化学的親和力概念の文学的応用、ナポレオン期ヨーロッパ社会変動。",
    development="ベンヤミン『ゲーテの親和力』、20世紀心理小説、現代結婚論小説の祖型。",
    historical_context="1809年ナポレオン戦争期ドイツの社会変動。",
    primary_source_url=GUTEN+"ebooks/2034",
    primary_source_type="Project Gutenberg: Die Wahlverwandtschaften",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"主体","status":"rethinking",
        "rationale":"親和力概念は人間関係の自然法則化を試み、AI推薦アルゴリズムの人間関係予測と理論的に共振。",
        "related_ai_phenomenon":"AI推薦・親和性アルゴリズム"}])

add(**C, name_ja="シラー『美的教育論』",
    name_en="Schiller's Aesthetic Education",
    name_original="Über die ästhetische Erziehung des Menschen",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="シラーが1795年発表の27通の哲学的書簡。フランス革命の挫折を受け、政治的解放の前提として美的経験による人間教育を論じる。カント『判断力批判』の文学的発展で、現代美学・批判理論の中心テクスト。",
    background="フランス革命挫折(1793-94)、カント『判断力批判』(1790)受容。",
    development="ヘーゲル美学、マルクーゼ『美的次元』、20世紀批判理論の中心源泉。",
    historical_context="1795年フランス革命挫折直後のドイツ知識人の政治的反省期。",
    primary_source_url=GUTEN+"ebooks/6798",
    primary_source_type="Project Gutenberg: Aesthetic Education",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"美的教育・批判理論",
        "description":"カント美学からマルクーゼ批判理論へ連なる中心テクスト。"}])

add(**C, name_ja="クライスト『マルキーゼ・フォン・O』",
    name_en="Kleist's The Marquise of O",
    name_original="Die Marquise von O....",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="ハインリヒ・フォン・クライスト（1777-1811）が1808年発表の中編小説。意識を失っている間に妊娠した寡婦の謎を、密度の高い独自構文で描く。20世紀ロメール映画化を経て、近代小説の凝縮形式の祖型として再評価された。",
    background="カント認識危機、独自の精神病理的散文構文の開発。",
    development="20世紀カフカ、ロメール映画化、現代凝縮型小説の祖型。",
    historical_context="ナポレオン戦争期プロイセンの政治的危機。",
    primary_source_url=GUTEN+"ebooks/3263",
    primary_source_type="Project Gutenberg: Die Marquise von O",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"物語","status":"rethinking",
        "rationale":"無意識的妊娠の謎は、AI生成における意識/無意識境界の問題と理論的に共振。",
        "related_ai_phenomenon":"AI生成における意識的/無意識的領域"}])

add(**C, name_ja="クライスト『ミヒャエル・コールハース』",
    name_en="Kleist's Michael Kohlhaas",
    name_original="Michael Kohlhaas",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="クライストが1810年発表した中編小説。16世紀の馬商人コールハースが法的不正義に対し私的戦争を起こす実話翻案で、近代法と個人的正義の衝突を高密度に描く。20世紀カフカ・ドクトロウ『ラグタイム』への直接的祖型。",
    background="ナポレオン期プロイセン法改革、グリム民俗説話との接続。",
    development="カフカ『城』『審判』、ドクトロウ『ラグタイム』、20世紀法と暴力の文学の祖型。",
    historical_context="1810年プロイセン改革期の法と暴力論議。",
    primary_source_url=GUTEN+"ebooks/12111",
    primary_source_type="Project Gutenberg: Michael Kohlhaas",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"法と暴力（ベンヤミン）",
        "description":"ベンヤミン『暴力批判論』の法・正義問題の文学的祖型。"}])


# ============================================================
# E: British Romantic 補完 (10 NEW)
# ============================================================
add(**C, name_ja="コールリッジ『老水夫の歌』",
    name_en="Coleridge's The Rime of the Ancient Mariner",
    name_original="The Rime of the Ancient Mariner",
    period_key="英国ロマン主義詩期",
    definition="サミュエル・テイラー・コールリッジ（1772-1834）が1798年『リリカル・バラッズ』所収の長詩。アホウドリ殺害の罪と贖罪の航海譚を、古英語風バラッド形式で描く。英国ロマン主義詩の最高峰の一つで、現代環境批評・象徴主義詩学の祖型。",
    background="ワーズワースとの『リリカル・バラッズ』(1798)共同企画、海事日記研究。",
    development="ボードレール『信天翁』、20世紀環境批評、現代エコクリティシズムの祖型。",
    historical_context="1798年英仏戦争期英国の海事文化。",
    primary_source_url=GUTEN+"ebooks/151",
    primary_source_type="Project Gutenberg: Ancient Mariner",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"正典","status":"rethinking",
        "rationale":"アホウドリ殺害の罪概念は、AI時代の環境倫理・生命倫理を再考する古典的祖型。",
        "related_ai_phenomenon":"AI時代の環境倫理・生命倫理"}])

add(**C, name_ja="コールリッジ『クリスタベル』",
    name_en="Coleridge's Christabel",
    name_original="Christabel",
    period_key="英国ロマン主義詩期",
    definition="コールリッジが1797-1800年執筆・1816年発表の未完の長詩。神秘的ジェラルディーンに魅入られた処女クリスタベルの物語で、ヴァンパイア文学・サフィック詩学の祖型を成した。バイロン称賛により遅れて発表された。",
    background="ゴシック・ヴァンパイア伝承の独自詩化、未完性自体の詩学。",
    development="バイロン『海賊』、シェリー『ザストロッツィ』、19世紀末ヴァンパイア文学の祖型。",
    historical_context="1810年代英国ロマン派の新古典主義との緊張期。",
    primary_source_url=GUTEN+"ebooks/12671",
    primary_source_type="Project Gutenberg: Christabel",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ブレイク『天国と地獄の結婚』",
    name_en="Blake's Marriage of Heaven and Hell",
    name_original="The Marriage of Heaven and Hell",
    period_key="英国ロマン主義詩期",
    definition="ブレイクが1790-93年に制作した自著彫版による予言書。「悪の格言」「地獄の格言」で道徳的二元論を解体し、エネルギーと肉体の肯定を主張する。スウェーデンボリ批判を経た独自神秘主義の起点で、20世紀対抗文化の聖典化した。",
    background="スウェーデンボリ受容と批判、ミルトン『失楽園』再読。",
    development="20世紀ハクスリー『知覚の扉』、ビート世代、対抗文化の聖典として再生。",
    historical_context="フランス革命期英国の急進思想・神秘主義系譜。",
    primary_source_url=GUTEN+"ebooks/45315",
    primary_source_type="Project Gutenberg: Marriage of Heaven and Hell",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="キーツ『エンディミオン』",
    name_en="Keats's Endymion",
    name_original="Endymion: A Poetic Romance",
    period_key="英国ロマン主義詩期",
    definition="ジョン・キーツ（1795-1821）が1818年発表の長詩。羊飼いエンディミオンと月女神シンシアの恋を4巻で歌う神話的長詩。冒頭「美しきものは永遠の喜び」で知られ、キーツ詩学の出発宣言となった。",
    background="シェリー助言、ハント・サークルでの古典神話受容。",
    development="キーツ晩年大頌歌群へ直結、19世紀英国神話的長詩の祖型。",
    historical_context="1818年英国ロマン派第二世代の興隆期。",
    primary_source_url=GUTEN+"ebooks/24280",
    primary_source_type="Project Gutenberg: Endymion",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シェリー『縛を解かれたプロメテウス』",
    name_en="Shelley's Prometheus Unbound",
    name_original="Prometheus Unbound",
    period_key="英国ロマン主義詩期",
    definition="パーシー・ビッシュ・シェリー（1792-1822）が1820年発表のリリカル・ドラマ。アイスキュロス散逸続編を再構築し、プロメテウスの解放を通じ革命的解放を歌う。シェリー詩学の頂点で、19-20世紀政治的詩学の中心テクスト。",
    background="アイスキュロス古典学受容、フランス革命挫折後の急進主義持続。",
    development="マルクス・エンゲルス称賛、19-20世紀解放詩学の祖型。",
    historical_context="1820年英国・イタリア反動期に対する詩的抵抗。",
    primary_source_url=GUTEN+"ebooks/4800",
    primary_source_type="Project Gutenberg: Prometheus Unbound",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="シェリー『無秩序の仮面舞踏会』",
    name_en="Shelley's The Mask of Anarchy",
    name_original="The Mask of Anarchy",
    period_key="英国ロマン主義詩期",
    definition="シェリーが1819年ピータールー虐殺事件を受けて執筆した政治詩。当時発表禁止され1832年に発表された。「眠りから目覚めよ獅子のように」のリフレインで、英国労働運動・ガンディー非暴力抵抗運動の聖典化した。",
    background="ピータールー虐殺事件(1819)、シェリー急進主義の頂点。",
    development="チャーティスト運動、ガンディー、20世紀世界非暴力抵抗運動の祖型。",
    historical_context="1819年マンチェスター・ピータールー虐殺事件期。",
    primary_source_url=GUTEN+"ebooks/4799",
    primary_source_type="Project Gutenberg: The Mask of Anarchy",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バイロン『マンフレッド』",
    name_en="Byron's Manfred",
    name_original="Manfred",
    period_key="英国ロマン主義詩期",
    definition="ジョージ・ゴードン・バイロン（1788-1824）が1817年発表の劇詩。アルプス山中の孤独な貴族マンフレッドが死霊・神霊と対峙する3幕劇。バイロン的英雄類型の頂点で、シューマン序曲(1849)・ニーチェ『ツァラトゥストラ』への直接的影響。",
    background="スイス亡命期、ゲーテ『ファウスト』第一部独受容。",
    development="シューマン序曲、ニーチェ『ツァラトゥストラ』、19世紀世紀末文学の祖型。",
    historical_context="1817年バイロン亡命直後のスイス・アルプス滞在期。",
    primary_source_url=GUTEN+"ebooks/8711",
    primary_source_type="Project Gutenberg: Manfred",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"主体","status":"rethinking",
        "rationale":"マンフレッドの自律的拒絶（神霊への屈服を拒む）は、AI時代の自律的主体・拒絶権を理論化する祖型。",
        "related_ai_phenomenon":"AIと自律的主体性・拒絶権"}])

add(**C, name_ja="チャールズ・ラム『エリア随筆』",
    name_en="Charles Lamb's Essays of Elia",
    name_original="Essays of Elia",
    period_key="英国ロマン主義詩期",
    definition="チャールズ・ラム（1775-1834）が1820-23年『ロンドン・マガジン』連載・1823年単行本化のエッセー集。エリアの仮名で日常生活・記憶・友情を綿密に観察する独自の散文形式を確立。19世紀英国エッセー文学の頂点で、20世紀英国エッセー伝統の祖型。",
    background="モンテーニュ・ハズリット系譜の英国エッセー伝統、ロマン派散文の独自路線。",
    development="ヴァージニア・ウルフ、ジョージ・オーウェル、20世紀英国エッセー伝統の祖型。",
    historical_context="1820年代ロンドン文人サークル文化期。",
    primary_source_url=GUTEN+"ebooks/10125",
    primary_source_type="Project Gutenberg: Essays of Elia",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハズリット『時代精神』",
    name_en="Hazlitt's The Spirit of the Age",
    name_original="The Spirit of the Age",
    period_key="英国ロマン主義詩期",
    definition="ウィリアム・ハズリット（1778-1830）が1825年発表の同時代肖像集。ベンサム・ゴドウィン・コールリッジ・ワーズワース・スコット・バイロン等25人の肖像批評で、ロマン派世代の自己理解の決定的記録となった。",
    background="ロマン派終期の世代論議、ハズリット急進派批評の集大成。",
    development="ヴィクトリア朝伝記批評、20世紀英国批評史の中心テクスト。",
    historical_context="1820年代英国ロマン派終焉期。",
    primary_source_url=GUTEN+"ebooks/12224",
    primary_source_type="Project Gutenberg: Spirit of the Age",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ド・クィンシー『阿片常用者の告白』",
    name_en="De Quincey's Confessions of an Opium-Eater",
    name_original="Confessions of an English Opium-Eater",
    period_key="英国ロマン主義詩期",
    definition="トマス・ド・クィンシー（1785-1859）が1821年『ロンドン・マガジン』連載・1822年単行本化の自伝的エッセー。阿片摂取の快楽と恐怖、夢の構造を散文詩的に描く。ボードレール『人工楽園』、20世紀薬物文学・夢散文の祖型。",
    background="阿片チンキの19世紀英国流通、ロマン派の意識変容実験。",
    development="ボードレール『人工楽園』、ポー、ハクスリー、ビート世代、20世紀薬物・意識変容文学の祖型。",
    historical_context="1820年代英国阿片貿易・医療使用文化期。",
    primary_source_url=GUTEN+"ebooks/2040",
    primary_source_type="Project Gutenberg: Confessions of an Opium-Eater",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"主体","status":"rethinking",
        "rationale":"阿片による意識変容・夢構造はAI生成の幻覚・ハルシネーション現象と理論的に共振。",
        "related_ai_phenomenon":"AIハルシネーションと意識変容"}])


# ============================================================
# F: German Romanticism Expanded (8 NEW)
# ============================================================
add(**C, name_ja="シュレーゲル兄弟『アテネーウム断片』",
    name_en="Schlegels' Athenaeum Fragments",
    name_original="Athenaeums-Fragmente",
    period_key="ドイツ・ロマン派期",
    definition="フリードリヒ・シュレーゲル（1772-1829）とアウグスト・ヴィルヘルム・シュレーゲル（1767-1845）兄弟がノヴァーリス等と1798-1800年『アテネーウム』誌に発表した断片集。「進歩的普遍詩」概念とロマン派理論の初期定式化。20世紀ベンヤミン『ドイツ・ロマン派の批評概念』(1920)が中心研究対象化した。",
    background="イエナ・ロマン派サークル形成、フィヒテ哲学受容。",
    development="ベンヤミン『ドイツ・ロマン派の批評概念』、20世紀現代批評の中心テクスト。",
    historical_context="1798-1800年イエナ・ロマン派形成期。",
    primary_source_url=WSRC_DE+"Athen%C3%A4ums-Fragmente",
    primary_source_type="Wikisource DE: Athenaeums-Fragmente",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"作者性","status":"rethinking",
        "rationale":"断片形式・共同執筆実践は、AI時代の集合的・断片的著作と理論的に共振。",
        "related_ai_phenomenon":"AI集合的・断片的著作"}],
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"初期ロマン派批評",
        "description":"ベンヤミン経由で現代批評理論の中心源泉。"}])

add(**C, name_ja="フリードリヒ・シュレーゲル『ルツィンデ』",
    name_en="F. Schlegel's Lucinde",
    name_original="Lucinde",
    period_key="ドイツ・ロマン派期",
    definition="フリードリヒ・シュレーゲルが1799年発表の自伝的小説。ドロテーア・メンデルスゾーンとの恋愛を、断片・書簡・寓意・幻想の混合形式で描く。当時スキャンダルとなり、20世紀キルケゴール『あれか、これか』批判対象となるなど、ロマン派恋愛小説の代表作。",
    background="ドロテーア・メンデルスゾーンとの恋愛、ロマン派理論の小説的具体化。",
    development="キルケゴール『あれか、これか』批判、20世紀フェミニズム批評再評価。",
    historical_context="1799年イエナ・ロマン派サークル形成期。",
    primary_source_url=GUTEN+"ebooks/57921",
    primary_source_type="Project Gutenberg: Lucinde",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ノヴァーリス『キリスト教世界またはヨーロッパ』",
    name_en="Novalis's Christianity or Europe",
    name_original="Die Christenheit oder Europa",
    period_key="ドイツ・ロマン派期",
    definition="ノヴァーリス（フリードリヒ・フォン・ハルデンベルク、1772-1801）が1799年執筆・1826年発表のエッセー。中世カトリック・ヨーロッパ統一を理想化し、宗教改革・啓蒙を文化的分裂とする独自の歴史哲学を提示。20世紀カール・シュミット『中世ヨーロッパ』論議の中心参照点。",
    background="フランス革命戦争期のヨーロッパ統一論議、独自神秘主義キリスト教観。",
    development="カール・シュミット、現代欧州統合思想の祖型、ベネディクト16世引用。",
    historical_context="1799年フランス革命戦争期のヨーロッパ統一論議。",
    primary_source_url=WSRC_DE+"Die_Christenheit_oder_Europa",
    primary_source_type="Wikisource DE: Christenheit oder Europa",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ノヴァーリス『花粉』",
    name_en="Novalis's Pollen",
    name_original="Blütenstaub",
    period_key="ドイツ・ロマン派期",
    definition="ノヴァーリスが1798年『アテネーウム』誌掲載の断片集。「我々はいつも家路にある」「哲学とは郷愁である」等の名句で、ロマン派思想の核を断片形式で表現した。アテネーウム断片と並ぶ初期ロマン派思想の中核テクスト。",
    background="シュレーゲル兄弟との『アテネーウム』共同企画、断片形式の自覚的選択。",
    development="20世紀アフォリズム文学（ベンヤミン、アドルノ）、現代断片形式批評の祖型。",
    historical_context="1798年イエナ・ロマン派形成期。",
    primary_source_url=WSRC_DE+"Bl%C3%BCtenstaub",
    primary_source_type="Wikisource DE: Blütenstaub",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="E.T.A.ホフマン『黄金の壺』",
    name_en="Hoffmann's The Golden Pot",
    name_original="Der goldne Topf",
    period_key="ドイツ・ロマン派期",
    definition="エルンスト・テオドール・アマデウス・ホフマン（1776-1822）が1814年発表のロマン派幻想物語。学生アンゼルムスが現実のドレスデン世界とアトランティス神話世界を二重に生きる物語。後期ドイツ・ロマン派幻想文学の頂点で、20世紀フロイト「不気味なもの」論の中心テクスト。",
    background="ジャン・パウル受容、ホフマン自身の音楽家・法律家・作家三重生活。",
    development="フロイト『不気味なもの』、20世紀ファンタスティック文学（トドロフ）、現代マジックリアリズムの祖型。",
    historical_context="ナポレオン戦争後のドレスデン文化期。",
    primary_source_url=GUTEN+"ebooks/30894",
    primary_source_type="Project Gutenberg: Der goldne Topf",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"物語","status":"rethinking",
        "rationale":"二重世界構造（現実と神話）は、AI生成の重層的世界モデリングと理論的に共振。",
        "related_ai_phenomenon":"AI多世界モデル・並行物語"}])

add(**C, name_ja="E.T.A.ホフマン『牡猫ムルの人生観』",
    name_en="Hoffmann's Life and Opinions of the Tomcat Murr",
    name_original="Lebensansichten des Katers Murr",
    period_key="ドイツ・ロマン派期",
    definition="ホフマンが1819-21年発表の二重小説。教養を備えた牡猫ムルの自伝と、楽長クライスラーの伝記が偶然印刷紛れに混合された形式の前衛作。20世紀ナラトロジー・メタフィクション論の中心研究対象。",
    background="スターン『トリストラム・シャンディ』受容、ホフマン晩年の方法的実験。",
    development="20世紀メタフィクション、ボルヘス、カルヴィーノ、現代ナラトロジーの祖型。",
    historical_context="1820年前後ベルリン・後期ロマン派期。",
    primary_source_url=GUTEN+"ebooks/14916",
    primary_source_type="Project Gutenberg: Lebensansichten des Katers Murr",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ティーク『ゲノフェーファ』",
    name_en="Tieck's Genoveva",
    name_original="Leben und Tod der heiligen Genoveva",
    period_key="ドイツ・ロマン派期",
    definition="ルートヴィヒ・ティーク（1773-1853）が1799年発表の中世聖人伝劇。中世風アレマン語を用いた独自の韻文劇で、ドイツ・ロマン派中世復興の起点となった。シューマン序曲(1850)で世界古典化した。",
    background="中世復興運動、ロマン派の中世憧憬。",
    development="シューマン序曲、19世紀ドイツ中世復興運動、ナザレ派絵画への影響。",
    historical_context="1799年イエナ・ロマン派形成期の中世復興運動。",
    primary_source_url=GUTEN+"ebooks/27066",
    primary_source_type="Project Gutenberg: Genoveva",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ヴァッケンローダー『芸術愛好の修道士の心情吐露』",
    name_en="Wackenroder's Outpourings of an Art-Loving Friar",
    name_original="Herzensergießungen eines kunstliebenden Klosterbruders",
    period_key="ドイツ・ロマン派期",
    definition="ヴィルヘルム・ハインリヒ・ヴァッケンローダー（1773-1798）がティークの協力で1797年発表のエッセー集。中世イタリア・ドイツの宗教画家ラファエロ・デューラー等を熱狂的に讃える独自の宗教的芸術観で、ドイツ・ロマン派の中世憧憬・宗教画家崇拝の起点となった。",
    background="ベルリン・ロマン派サークル形成、ヴァッケンローダーの早世(25歳)。",
    development="ナザレ派絵画運動、19世紀ドイツ中世画家崇拝、現代宗教美学の祖型。",
    historical_context="1797年ベルリン・ロマン派形成期。",
    primary_source_url=GUTEN+"ebooks/30355",
    primary_source_type="Project Gutenberg: Herzensergießungen",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# G: Russian Romanticism Expanded (10 NEW)
# ============================================================
add(**CRU, name_ja="プーシキン『青銅の騎士』",
    name_en="Pushkin's The Bronze Horseman",
    name_original="Медный всадник",
    period_key="ロシア・ロマン主義期",
    definition="アレクサンドル・プーシキン（1799-1837）が1833年執筆・1837年没後発表の長詩。1824年ペテルブルク大洪水に翻弄される下級官吏エフゲーニーと、ピョートル大帝銅像の対峙を描く。ロシア帝都ペテルブルクの神話化の頂点で、ロシア文学帝都主題の祖型。",
    background="1824年ペテルブルク大洪水、プーシキン晩年のロシア国家論議。",
    development="ゴーゴリ『ペテルブルグ物語』、ドストエフスキー『罪と罰』、20世紀ペテルブルク文学の祖型。",
    historical_context="1830年代ニコライ1世期ロシアの国家・個人論議。",
    primary_source_url=WSRC_RU+"%D0%9C%D0%B5%D0%B4%D0%BD%D1%8B%D0%B9_%D0%B2%D1%81%D0%B0%D0%B4%D0%BD%D0%B8%D0%BA",
    primary_source_type="Wikisource RU: Медный всадник",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CRU, name_ja="プーシキン『大尉の娘』",
    name_en="Pushkin's The Captain's Daughter",
    name_original="Капитанская дочка",
    period_key="ロシア・ロマン主義期",
    definition="プーシキンが1836年発表の歴史小説。プガチョフ反乱(1773-75)期の若き士官ピョートルと大尉の娘マーシャの物語を、回想録形式で描く。ウォルター・スコット歴史小説をロシア独自に展開し、19世紀ロシア歴史小説の祖型。",
    background="プガチョフ反乱史料調査、スコット歴史小説のロシア独自展開。",
    development="トルストイ『戦争と平和』、19-20世紀ロシア歴史小説の祖型。",
    historical_context="1830年代ロシアの民衆反乱史再評価期。",
    primary_source_url=GUTEN+"ebooks/13511",
    primary_source_type="Project Gutenberg: Captain's Daughter",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CRU, name_ja="プーシキン『ボリス・ゴドゥノフ』",
    name_en="Pushkin's Boris Godunov",
    name_original="Борис Годунов",
    period_key="ロシア・ロマン主義期",
    definition="プーシキンが1825年執筆・1831年発表のシェイクスピア風歴史劇。16世紀末「動乱時代」のボリス・ゴドゥノフ皇帝の即位と没落を描く。ムソルグスキー・オペラ(1869)でロシア国民劇となり、19-20世紀ロシア歴史劇の祖型。",
    background="シェイクスピア・ロシア受容、カラムジン『ロシア国家史』再評価期。",
    development="ムソルグスキー・オペラ、19-20世紀ロシア国民劇、現代ロシア歴史劇の祖型。",
    historical_context="デカブリスト乱(1825)前後のロシア政治論議期。",
    primary_source_url=GUTEN+"ebooks/19640",
    primary_source_type="Project Gutenberg: Boris Godunov",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CRU, name_ja="プーシキン『スペードの女王』",
    name_en="Pushkin's The Queen of Spades",
    name_original="Пиковая дама",
    period_key="ロシア・ロマン主義期",
    definition="プーシキンが1834年発表の中編小説。ペテルブルク社交界でカード・ゲームに執着する将校ゲルマンの破滅譚。ホフマン的幻想とリアリズムの統合で、チャイコフスキー・オペラ(1890)化を経て20世紀ロシア・モダニズムの祖型となった。",
    background="ホフマン受容、ペテルブルク社交界カード文化観察。",
    development="チャイコフスキー・オペラ、20世紀ロシア・モダニズム、現代心理サスペンスの祖型。",
    historical_context="1830年代ペテルブルク社交界文化期。",
    primary_source_url=GUTEN+"ebooks/23058",
    primary_source_type="Project Gutenberg: Queen of Spades",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CRU, name_ja="レールモントフ『悪魔』",
    name_en="Lermontov's The Demon",
    name_original="Демон",
    period_key="ロシア・ロマン主義期",
    definition="ミハイル・レールモントフ（1814-1841）が1829-39年に改訂を重ねた長詩。コーカサスを舞台に堕天使悪魔と修道女タマーラの恋を描く。ロシア・ロマン主義叙事詩の頂点で、ヴルーベリ絵画(1890年代)・ルビンシュテイン・オペラ(1875)で世界化した。",
    background="バイロン受容、コーカサス勤務体験、ロシア・ロマン派悪魔学。",
    development="ヴルーベリ絵画、ルビンシュテイン・オペラ、19世紀末ロシア悪魔学の祖型。",
    historical_context="1830年代ロシアのコーカサス戦争期。",
    primary_source_url=WSRC_RU+"%D0%94%D0%B5%D0%BC%D0%BE%D0%BD_(%D0%9B%D0%B5%D1%80%D0%BC%D0%BE%D0%BD%D1%82%D0%BE%D0%B2)",
    primary_source_type="Wikisource RU: Демон",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CRU, name_ja="レールモントフ『ムツィリ』",
    name_en="Lermontov's Mtsyri",
    name_original="Мцыри",
    period_key="ロシア・ロマン主義期",
    definition="レールモントフが1839年発表のコーカサス長詩。修道院に捕らわれた山岳民族の青年ムツィリが脱走し、自由と帰郷を求めて死ぬ物語。レールモントフ自由詩学の頂点で、19世紀ロシア・コーカサス詩学の中核。",
    background="レールモントフ自身のコーカサス追放(1837)、バイロン的自由理念の独自展開。",
    development="19世紀ロシア・コーカサス文学伝統、ソ連期民族文学への影響。",
    historical_context="1830年代後半ロシア・コーカサス戦争期。",
    primary_source_url=WSRC_RU+"%D0%9C%D1%86%D1%8B%D1%80%D0%B8",
    primary_source_type="Wikisource RU: Мцыри",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CRU, name_ja="ゴーゴリ『検察官』",
    name_en="Gogol's The Government Inspector",
    name_original="Ревизор",
    period_key="ロシア・ロマン主義期",
    definition="ニコライ・ゴーゴリ（1809-1852）が1836年発表の喜劇。地方都市の役人たちが偽の検察官を本物と誤認する筋書きで、ロシア官僚制を諷刺した。ニコライ1世自身が許可した上演で、19-20世紀ロシア社会風刺劇の祖型。",
    background="プーシキンからの題材提供、ロシア地方官僚制観察。",
    development="チェーホフ、ブルガーコフ、20世紀ロシア・ソ連風刺劇の祖型。",
    historical_context="1836年ニコライ1世期ロシア官僚制全盛期。",
    primary_source_url=GUTEN+"ebooks/47431",
    primary_source_type="Project Gutenberg: The Inspector-General",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CRU, name_ja="ジュコフスキー『バラード』",
    name_en="Zhukovsky's ballads",
    name_original="Баллады В. Жуковского",
    period_key="ロシア・ロマン主義期",
    definition="ヴァシーリー・ジュコフスキー（1783-1852）が1808-30年代に発表したバラード群。ビュルガー『レノーレ』、シラー『手套』『鐘の歌』、サウジー、ゴールドスミス等の独・英ロマン派バラードを翻案・翻訳した、ロシア・ロマン主義詩の出発点。",
    background="ドイツ・英国ロマン派バラード受容、カラムジン感傷主義の継承。",
    development="プーシキン以降ロシア・ロマン主義詩の出発点、現代ロシア翻訳詩学の祖型。",
    historical_context="1810-30年代ロシアのドイツ・英国ロマン派受容期。",
    primary_source_url=WSRC_RU+"%D0%96%D1%83%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9,_%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9_%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B5%D0%B2%D0%B8%D1%87",
    primary_source_type="Wikisource RU: Жуковский",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"翻訳","status":"rethinking",
        "rationale":"翻案・翻訳によるロシア詩の創出は、AI翻訳・適応の文化転移と理論的に共振。",
        "related_ai_phenomenon":"AI翻訳と文化的翻案"}])

add(**CRU, name_ja="チュッチェフ抒情詩",
    name_en="Tyutchev's lyrics",
    name_original="Лирика Ф. Тютчева",
    period_key="ロシア・ロマン主義期",
    definition="フョードル・チュッチェフ（1803-1873）が1830-70年代に発表した自然・夜・形而上学的抒情詩。「ロシアは知性で理解できない」「沈黙！」等の名句で、19世紀ロシア哲学詩の頂点を成した。20世紀シンボリズム（イワノフ、ブローク）の中心源泉。",
    background="ミュンヘン外交官時代のシェリング・ロマン派受容、ロシア国家論議。",
    development="20世紀シンボリズム、現代ロシア哲学詩の祖型。",
    historical_context="1830-70年代ロシア・ヨーロッパ知識人交流期。",
    primary_source_url=WSRC_RU+"%D0%A2%D1%8E%D1%82%D1%87%D0%B5%D0%B2,_%D0%A4%D1%91%D0%B4%D0%BE%D1%80_%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87",
    primary_source_type="Wikisource RU: Тютчев",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CRU, name_ja="バラトィンスキー抒情詩",
    name_en="Baratynsky's lyrics",
    name_original="Лирика Е. Баратынского",
    period_key="ロシア・ロマン主義期",
    definition="エヴゲーニー・バラトィンスキー（1800-1844）が1820-40年代に発表した哲学抒情詩。プーシキン世代の詩人として、形而上学的省察と簡潔な詩形を統合した。20世紀以降ブロツキー・マンデリシュタームらに再評価された、ロシア哲学詩の祖型。",
    background="プーシキン・ロマン主義サークル、レルモントフ・チュッチェフと並ぶ哲学詩系譜。",
    development="20世紀マンデリシュターム、ブロツキー、現代ロシア哲学詩の祖型。",
    historical_context="1820-40年代ロシア・ロマン主義詩黄金期。",
    primary_source_url=WSRC_RU+"%D0%91%D0%B0%D1%80%D0%B0%D1%82%D1%8B%D0%BD%D1%81%D0%BA%D0%B8%D0%B9,_%D0%95%D0%B2%D0%B3%D0%B5%D0%BD%D0%B8%D0%B9_%D0%90%D0%B1%D1%80%D0%B0%D0%BC%D0%BE%D0%B2%D0%B8%D1%87",
    primary_source_type="Wikisource RU: Баратынский",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# H: American Romanticism Expanded (12 NEW)
# ============================================================
add(**CAM, name_ja="ホーソーン『トワイス・トールド・テイルズ』",
    name_en="Hawthorne's Twice-Told Tales",
    name_original="Twice-Told Tales",
    period_key="米国ロマン主義期",
    definition="ナサニエル・ホーソーン（1804-1864）が1837年初版・1842年増補版を発表した短編集。「牧師の黒いヴェール」「マイ・キンズマン少佐モリヌー」「若いグッドマン・ブラウン」等を含む。アメリカ短編小説形式の確立で、ポー絶賛により米国短編美学の祖型となった。",
    background="ボウディン大学卒業後セーラム隠棲期(1825-37)の文学修業。",
    development="ポー短編論の中心評価対象、メルヴィル『書記バートルビー』、20世紀アメリカ短編小説の祖型。",
    historical_context="1830年代ニューイングランド・ピューリタン伝統再評価期。",
    primary_source_url=GUTEN+"ebooks/13707",
    primary_source_type="Project Gutenberg: Twice-Told Tales",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CAM, name_ja="ホーソーン『古い牧師館の苔』",
    name_en="Hawthorne's Mosses from an Old Manse",
    name_original="Mosses from an Old Manse",
    period_key="米国ロマン主義期",
    definition="ホーソーンが1846年発表の短編集。コンコルドの旧牧師館滞在期(1842-45)の作品を収録し、「ラパチーニの娘」「美の芸術家」「若いグッドマン・ブラウン」を含む。メルヴィル『ホーソーンとその苔』(1850)書評で米国国民文学論議の中心テクストとなった。",
    background="コンコルド・エマソン・ソローとの交流、超越主義サークル経験。",
    development="メルヴィル『ホーソーンとその苔』、米国国民文学論議の起点、20世紀米国短編論。",
    historical_context="1840年代コンコルド超越主義運動期。",
    primary_source_url=GUTEN+"ebooks/9241",
    primary_source_type="Project Gutenberg: Mosses from an Old Manse",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CAM, name_ja="メルヴィル『タイピー』",
    name_en="Melville's Typee",
    name_original="Typee: A Peep at Polynesian Life",
    period_key="米国ロマン主義期",
    definition="ハーマン・メルヴィル（1819-1891）が1846年発表のデビュー作。ポリネシア・マルキーズ諸島タイピー渓谷での捕鯨船離脱体験を、半自伝半フィクションで描く。19世紀米国太平洋文学の起点で、20世紀ポストコロニアル文学論の祖型。",
    background="1842年捕鯨船アクシュネット号離脱、ポリネシア体験。",
    development="メルヴィル後期作品、20世紀ポストコロニアル文学、ハワイ・太平洋研究の祖型。",
    historical_context="1840年代米国太平洋進出期。",
    primary_source_url=GUTEN+"ebooks/1900",
    primary_source_type="Project Gutenberg: Typee",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CAM, name_ja="メルヴィル『ピエール』",
    name_en="Melville's Pierre",
    name_original="Pierre, or The Ambiguities",
    period_key="米国ロマン主義期",
    definition="メルヴィルが1852年発表の長編小説。『白鯨』直後の野心的作品で、近親相姦・自殺を含む心理悲劇。同時代に酷評されたが、20世紀メルヴィル復興期に再評価され、現代心理小説・モダニズムの祖型として位置づけられた。",
    background="『白鯨』失敗後の絶望期、ホーソーンとの交流。",
    development="20世紀メルヴィル復興、現代心理小説、モダニズムの祖型。",
    historical_context="1850年代米国南北戦争前夜の社会的緊張期。",
    primary_source_url=GUTEN+"ebooks/34970",
    primary_source_type="Project Gutenberg: Pierre",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CAM, name_ja="メルヴィル『信用詐欺師』",
    name_en="Melville's The Confidence-Man",
    name_original="The Confidence-Man: His Masquerade",
    period_key="米国ロマン主義期",
    definition="メルヴィルが1857年発表の最後の長編小説。ミシシッピ蒸気船を舞台に、姿を変える信用詐欺師が乗客の信頼を試す筋書き。20世紀ポストモダニズム・解釈学の中心研究対象として再評価された、メルヴィル最も難解な作品。",
    background="『ピエール』失敗後の経済的困窮、米国民主主義への懐疑。",
    development="20世紀ポストモダニズム、解釈学、現代米国小説の祖型。",
    historical_context="1857年金融恐慌期米国の信用問題。",
    primary_source_url=GUTEN+"ebooks/21816",
    primary_source_type="Project Gutenberg: The Confidence-Man",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"主体","status":"rethinking",
        "rationale":"信用詐欺師の変装・偽装は、AI生成における信頼性・偽情報問題と理論的に共振。",
        "related_ai_phenomenon":"AI偽情報・なりすまし"}])

add(**CAM, name_ja="メルヴィル『ビリー・バッド』",
    name_en="Melville's Billy Budd",
    name_original="Billy Budd, Sailor",
    period_key="米国ロマン主義期",
    definition="メルヴィルが1888-91年執筆・1924年遺作刊行の中編小説。英国海軍水兵ビリー・バッドの無垢と司法的処刑を、海事法と道徳の悲劇として描く。ベンジャミン・ブリテン・オペラ(1951)で世界古典化、20世紀メルヴィル復興期の中心テクスト。",
    background="メルヴィル晩年の海軍記憶、19世紀末米国近代化への省察。",
    development="ブリテン・オペラ、20世紀法と文学論議、現代海事文学の祖型。",
    historical_context="メルヴィル晩年(1888-91)ニューヨーク隠棲期。",
    primary_source_url=GUTEN+"ebooks/5300",
    primary_source_type="Project Gutenberg: Billy Budd",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CAM, name_ja="メルヴィル『ベニト・セレノ』",
    name_en="Melville's Benito Cereno",
    name_original="Benito Cereno",
    period_key="米国ロマン主義期",
    definition="メルヴィルが1855年発表の中編小説。スペイン奴隷船での反乱を米国船長デラノが見抜けない物語で、奴隷制・人種・認識の盲点を緻密に描く。1960年代米国公民権運動期に再評価され、20世紀人種文学批評の中心テクスト。",
    background="ヘリン船長『航海日誌』(1817)題材、米国南北戦争前夜の奴隷制論議。",
    development="20世紀後半人種批評、ポール・ジル・ロイ『黒い大西洋』、現代奴隷制文学批評の祖型。",
    historical_context="1855年米国南北戦争前夜の奴隷制度危機期。",
    primary_source_url=GUTEN+"ebooks/15859",
    primary_source_type="Project Gutenberg: Benito Cereno",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"奴隷制と人種認識",
        "description":"人類学DB側の奴隷制・人種研究と直接接続する文学的祖型。"}])

add(**CAM, name_ja="ポー『ユリイカ』",
    name_en="Poe's Eureka",
    name_original="Eureka: A Prose Poem",
    period_key="米国ロマン主義期",
    definition="エドガー・アラン・ポー（1809-1849）が1848年発表した宇宙論散文詩。宇宙の起源・膨張・収縮を、当時の天文学を独自に詩的に統合して論じる。同時代に無視されたが、20世紀ボードレール訳・ヴァレリー再評価で、現代SF・宇宙論文学の祖型として復権。",
    background="ポー晩年の科学受容、ニュートン・ラプラス天文学の独自詩化。",
    development="ボードレール訳、ヴァレリー、20世紀SF・宇宙論文学の祖型。",
    historical_context="1848年ポー晩年の経済的困窮期。",
    primary_source_url=GUTEN+"ebooks/32037",
    primary_source_type="Project Gutenberg: Eureka",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CAM, name_ja="ポー『構成の哲学』",
    name_en="Poe's The Philosophy of Composition",
    name_original="The Philosophy of Composition",
    period_key="米国ロマン主義期",
    definition="ポーが1846年発表の批評論文。『大鴉』(1845)の制作過程を理性的計算として再構成し、霊感論を否定する近代詩学の出発点となった。ボードレール・マラルメ経由でフランス象徴主義詩学・現代批評理論の中心テクストとなった。",
    background="ロマン派霊感論への反発、ポー独自の理性的詩学。",
    development="ボードレール・マラルメ・ヴァレリー、20世紀新批評、現代制作論の祖型。",
    historical_context="1846年米国ロマン主義成熟期。",
    primary_source_url=GUTEN+"ebooks/55749",
    primary_source_type="Project Gutenberg: Philosophy of Composition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"創造性","status":"rethinking",
        "rationale":"ポー『構成の哲学』の理性的計算的詩作は、AI生成の計算的詩作と理論的に共振する祖型。",
        "related_ai_phenomenon":"AI生成と計算的詩作"}])

add(**CAM, name_ja="エマソン『自然論』",
    name_en="Emerson's Nature",
    name_original="Nature",
    period_key="米国ロマン主義期",
    definition="エマソンが1836年匿名発表のエッセー。米国超越主義の出発宣言で、自然を「現在のシンボル」「精神の発現」と定義し、独自の汎神論的自然観を提示。ニューイングランド超越主義クラブ(1836-)の理論的支柱となった。",
    background="ユニタリアニズム聖職辞職(1832)、ヨーロッパ旅行体験、独逸観念論受容。",
    development="ソロー『ウォルデン』、ニーチェ受容、20世紀米国環境思想の祖型。",
    historical_context="1836年米国超越主義クラブ形成期。",
    primary_source_url=GUTEN+"ebooks/29433",
    primary_source_type="Project Gutenberg: Nature (Emerson)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"米国超越主義",
        "description":"米国超越主義の出発宣言として哲学DB項目と接続。"}])

add(**CAM, name_ja="エマソン『アメリカの学者』",
    name_en="Emerson's The American Scholar",
    name_original="The American Scholar",
    period_key="米国ロマン主義期",
    definition="エマソンが1837年ハーバード・ファイ・ベータ・カッパ協会講演として発表の記念碑的演説。米国知識人の文化的独立を宣言し、ヨーロッパ模倣からの離脱を訴える。オリヴァー・ホームズ評「米国知識人独立宣言」として、米国国民文学論の起点。",
    background="ジャクソン民主主義期、米国国民文化形成論議。",
    development="米国国民文学論、20世紀米国スタディーズの起点。",
    historical_context="1837年米国独立60年期の文化的独立論議。",
    primary_source_url=GUTEN+"ebooks/16643",
    primary_source_type="Project Gutenberg: American Scholar",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CAM, name_ja="ソロー『市民の不服従』",
    name_en="Thoreau's Civil Disobedience",
    name_original="Resistance to Civil Government / Civil Disobedience",
    period_key="米国ロマン主義期",
    definition="ヘンリー・デイヴィッド・ソローが1849年発表のエッセー。米墨戦争・奴隷制への反対として人頭税納付を拒否し獄中体験した経験から、不正義法への市民的不服従を論じる。ガンディー非暴力抵抗運動・キング牧師公民権運動の理論的源泉となった。",
    background="米墨戦争(1846-48)・米国奴隷制への抗議、コンコルド超越主義の政治化。",
    development="ガンディー非暴力抵抗運動、マーティン・ルーサー・キング、20世紀世界市民運動の祖型。",
    historical_context="1849年米墨戦争・奴隷制論議期。",
    primary_source_url=GUTEN+"ebooks/71",
    primary_source_type="Project Gutenberg: Civil Disobedience",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"市民的不服従論",
        "description":"アーレント・ロールズ市民的不服従論の中心源泉。"}])

add(**CAM, name_ja="マーガレット・フラー『19世紀の女性』",
    name_en="Fuller's Woman in the Nineteenth Century",
    name_original="Woman in the Nineteenth Century",
    period_key="米国ロマン主義期",
    definition="マーガレット・フラー（1810-1850）が1845年発表のフェミニズム論考。米国超越主義の女性論として、女性の知的・政治的解放を論じる。米国フェミニズム文学の出発点で、20世紀後半フェミニズム第二波の中心源泉。",
    background="超越主義クラブ参加、エマソンとの『ダイアル』編集経験。",
    development="米国フェミニズム文学伝統の起点、20世紀後半フェミニズム第二波の中心源泉。",
    historical_context="1845年米国セネカフォールズ会議(1848)前夜のフェミニズム形成期。",
    primary_source_url=GUTEN+"ebooks/8642",
    primary_source_type="Project Gutenberg: Woman in the Nineteenth Century",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"主体","status":"rethinking",
        "rationale":"フラー女性論は主体の社会的構成を理論化し、AI時代のジェンダー・主体性論議の祖型。",
        "related_ai_phenomenon":"AI生成における主体・ジェンダー"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="西欧",
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
        print(f"[c06-add80 wave23] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c06-add80 wave23] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
