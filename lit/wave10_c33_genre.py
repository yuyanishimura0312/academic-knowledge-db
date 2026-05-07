"""
LIT-DB Phase 2 — C33 Wave 10: Children / Mass / Genre Literature
================================================================
40 concepts spanning 5 categories of genre / popular / children's literature:
  A. Children's literature (8)
  B. Science fiction / fantasy (8)
  C. Mystery / hardboiled / thriller (8)
  D. Graphic novel / comics (8)
  E. Mass literature / genre theory (8)

Sources:
  - International Children's Digital Library (ICDL): http://en.childrenslibrary.org/
  - Internet Speculative Fiction Database (ISFDB): http://www.isfdb.org/
  - Pulp Magazines Project: https://www.pulpmags.org/
  - Children's Literature Association journal (Project MUSE)
  - Science Fiction Studies (DePauw / JSTOR)
  - Modern Fiction Studies, Journal of Popular Culture
  - Comics Studies journals (ImageTexT, Comics Grid, Inks)
  - Author canonical editions / publisher pages

source_tier='primary' — author's canonical text or peer-reviewed canonical
  scholarly journal article directly cited.
source_tier='secondary' — encyclopedic / reference work synthesis (ISFDB,
  Encyclopedia of SF, Britannica, ICDL synthesis).
source_tier='tertiary' — synthetic genre-name level definitions resting on
  multiple secondary expositions.

subfield_id=21, region='周縁横断' (peripheral / cross-cutting genre region).

Pattern: P3 (Theory-driven concept cartography) + P5 (Genre canon mapping).
"""
from __future__ import annotations

import sys

from lit_db_helper import LitDB, LitDBError


SUBFIELD_CODE = "lit_genre"
REGION = "周縁横断"


# ---------------------------------------------------------------
# Period seeding (genre/popular literature waves, 1697-present)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    # name_ja, name_en, start, end, description
    ("民話・初期児童文学期", "Folk-Tale & Early Children's Literature",
     1697, 1899,
     "ペロー童話集（1697）からグリム・アンデルセン・キャロル・ルイスを経て"
     "19世紀末ビアトリクス・ポターまで、児童文学が独立ジャンルとして制度化された時期。"),
    ("初期SF・パルプ期", "Early SF & Pulp Era", 1864, 1939,
     "ヴェルヌ・H.G.ウェルズの科学ロマンスと、20世紀前半のパルプマガジン時代。"
     "Poe探偵小説起源も含む大衆ジャンル成立期。"),
    ("黄金時代・古典化期", "Golden Age & Classical Era",
     1920, 1959,
     "Christie黄金時代ミステリ、Asimov・Heinlein系黄金時代SF、"
     "Hammett/Chandlerハードボイルド、ハードSF確立期。マスマーケット・ペーパーバック誕生。"),
    ("ジャンル多様化期", "Genre Diversification", 1960, 1989,
     "Tolkien後のセカンダリーワールド・ファンタジー、Le Guin社会派SF、"
     "Dahl・Sendak絵本革新、サイバーパンクの誕生（Gibson 1984）、"
     "graphic novel概念の確立（Eisner 1978）期。"),
    ("ポップ・グローバル化期", "Pop Globalization & Convergence",
     1990, 2025,
     "Rowling『Harry Potter』のグローバル現象、Maus/Watchmen以降のグラフィック"
     "ノベル文学化、young adultジャンル確立、cli-fi誕生、"
     "ファンフィクション・コミュニティの大規模化期。"),
]


# ---------------------------------------------------------------
# Concept payload
# ---------------------------------------------------------------

CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — Children's literature (8)
# ===============================================================

add({
    "name_ja": "ペロー・グリム童話伝統",
    "name_en": "fairy tale traditions (Perrault, Grimm)",
    "name_original": "Histoires ou contes du temps passé / Kinder- und Hausmärchen",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "民話・初期児童文学期",
    "definition": "シャルル・ペロー『過ぎし時代の物語』（1697）とグリム兄弟"
        "『子供と家庭の童話集』（KHM, 1812-1857）が確立した文学的童話伝統。"
        "口承民話を文字化・編集して児童・家庭読者向けに供給する形式が、"
        "のちの児童文学・ジャンル文学の基層を成した。",
    "background": "17世紀フランス宮廷サロン文化と、19世紀ドイツ・ロマン主義的"
        "国民文化収集運動の二系譜。",
    "development": "アンデルセン創作童話、絵本産業、ディズニーアニメ、"
        "ファンタジー文学全般の基礎テクスト群となる。",
    "historical_context": "近世絶対王政期と19世紀国民国家形成期。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/2591",
    "primary_source_type": "Project Gutenberg — Grimm KHM full text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アンデルセン文学童話",
    "name_en": "Andersen literary fairy tale",
    "name_original": "Eventyr",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "民話・初期児童文学期",
    "definition": "ハンス・クリスチャン・アンデルセン（1805-1875）が1835年から"
        "発表した『おとぎ話集』（Eventyr）。民話の口承的素材を出発点に"
        "しつつ、近代的個人作家による創作童話として独立させ、"
        "「人魚姫」「みにくいアヒルの子」「裸の王様」など世界文学の"
        "基層を構成する物語群を生んだ。",
    "background": "デンマーク・ロマン主義と作家自身の社会的疎外経験。",
    "development": "ワイルド、宮沢賢治、現代文学童話の直接の源流。",
    "historical_context": "19世紀ヨーロッパ国民文化運動と児童書市場の成立。",
    "primary_source_url": "https://andersen.sdu.dk/vaerk/hersholt/",
    "primary_source_type": "Hans Christian Andersen Centre — Hersholt translations",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ルイス・キャロル『不思議の国のアリス』",
    "name_en": "Lewis Carroll: Alice's Adventures in Wonderland",
    "name_original": "Alice's Adventures in Wonderland",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "民話・初期児童文学期",
    "definition": "ルイス・キャロル（チャールズ・ドジソン）が1865年に出版した"
        "児童文学・ナンセンス文学の古典。論理学者として言語遊戯・論理パズル"
        "を物語に組み込み、教訓主義から離脱した遊戯的児童文学を確立した。"
        "近代児童文学の出発点とされる。",
    "background": "ヴィクトリア朝の道徳主義的児童書への暗黙の対抗。",
    "development": "20世紀ナンセンス文学、ファンタジー、サブカルチャーの源泉。",
    "historical_context": "ヴィクトリア朝中期の児童文学市場拡大期。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/11",
    "primary_source_type": "Project Gutenberg — Carroll full text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ビアトリクス・ポター絵本",
    "name_en": "Beatrix Potter picture books",
    "name_original": "The Tale of Peter Rabbit",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "民話・初期児童文学期",
    "definition": "ビアトリクス・ポター（1866-1943）が1902年『ピーターラビットの"
        "おはなし』（自費出版1901、Frederick Warne商業版1902）から発表した"
        "絵本シリーズ。著者自身の精緻な水彩画と簡潔な物語の統合により、"
        "近代絵本（picture book）の基本形式を確立した。",
    "background": "ヴィクトリア朝末期の自然観察文化と独学博物学。",
    "development": "20世紀絵本産業・絵本理論、Sendak以後の絵本革新の前提となる。",
    "historical_context": "20世紀初頭の児童書出版産業化期。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/14838",
    "primary_source_type": "Project Gutenberg — Potter Peter Rabbit full text",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ロアルド・ダール児童文学",
    "name_en": "Roald Dahl children's literature",
    "name_original": "Charlie and the Chocolate Factory / Matilda",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "ロアルド・ダール（1916-1990）が『チャーリーとチョコレート工場』"
        "（1964）『マチルダ』（1988）等で確立した、ブラックユーモアと反権威"
        "主義を特徴とする20世紀後半の児童文学スタイル。大人世界の偽善・"
        "残酷を子供視点から脱構築する語りで、後続の児童文学を方向づけた。",
    "background": "戦後英国の児童書ブームと、教訓主義への暗黙の批判。",
    "development": "現代の批判的児童文学・YA文学のアイロニカルな語りの源流。",
    "historical_context": "戦後英国・米国の児童書市場拡大期。",
    "primary_source_url": "https://www.roalddahl.com/roald-dahl/about",
    "primary_source_type": "Roald Dahl Story Company — official biography",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "J.K.ローリング『ハリー・ポッター』",
    "name_en": "J.K. Rowling: Harry Potter",
    "name_original": "Harry Potter and the Philosopher's Stone",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ポップ・グローバル化期",
    "definition": "J.K.ローリングが1997-2007年に発表した7巻のファンタジー連作。"
        "魔法学校という擬制の教育空間を舞台に成長物語と善悪闘争を統合した"
        "形式により、グローバル児童文学市場を再定義した。映画・テーマパーク・"
        "巨大ファンダム形成によりトランスメディア・フランチャイズの典型例となる。",
    "background": "1990年代後半の児童書出版業界とグローバル翻訳ネットワーク。",
    "development": "YA文学市場の確立、ファンフィクション現象の大規模化、"
        "現代ファンタジーの基準作。",
    "historical_context": "ポスト冷戦のグローバル化と児童文化の市場化。",
    "primary_source_url": "https://www.bloomsbury.com/uk/harry-potter-and-the-philosophers-stone-9781408855652/",
    "primary_source_type": "Bloomsbury — UK first publisher canonical edition",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "グローバル巨大ファンダムが生んだ参加型文化は、AI時代の"
            "創作・解釈の集合的生産モデルを先取りする。",
         "related_ai_phenomenon": "AI生成コンテンツの集合的受容コミュニティ"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "ファンダム文化",
         "description": "Rowlingファンダムは人類学DBの大衆文化研究と直結する。"},
    ],
})

add({
    "name_ja": "モーリス・センダック絵本",
    "name_en": "Maurice Sendak picture book",
    "name_original": "Where the Wild Things Are",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "モーリス・センダック（1928-2012）が『かいじゅうたちのいるところ』"
        "（1963）等で確立した絵本表現。子供の怒り・暴力性・孤独などの感情を"
        "正面から描き、絵本を「子供のため」に純化された道徳教材から"
        "心的経験の文学装置へと転換した。",
    "background": "戦後アメリカ児童書黄金期とポスト精神分析的子供観。",
    "development": "Carle・Browne以降の現代絵本表現と絵本理論の出発点。",
    "historical_context": "1960年代米国の児童文化革新期。",
    "primary_source_url": "https://www.harpercollins.com/products/where-the-wild-things-are-maurice-sendak",
    "primary_source_type": "HarperCollins — canonical publisher edition",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "エリック・カール絵本",
    "name_en": "Eric Carle picture books",
    "name_original": "The Very Hungry Caterpillar",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "エリック・カール（1929-2021）が『はらぺこあおむし』（1969）等"
        "で確立した絵本様式。コラージュによる原色彩色と、穴あきページなど"
        "造本上のインタラクティブ仕掛けにより、絵本を「読む対象」から"
        "「触り操作する対象」へ拡張した先駆。",
    "background": "戦後アメリカの教育心理学（ピアジェ等）と造本技術革新。",
    "development": "現代の仕掛け絵本・知育絵本・乳幼児絵本市場の方向づけ。",
    "historical_context": "1960-70年代米国の幼児教育産業拡大期。",
    "primary_source_url": "https://www.eric-carle.com/the-very-hungry-caterpillar/",
    "primary_source_type": "Eric Carle Studio — official canonical page",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY B — Science fiction / fantasy (8)
# ===============================================================

add({
    "name_ja": "H.G.ウェルズの科学ロマンス",
    "name_en": "H.G. Wells scientific romance",
    "name_original": "scientific romance",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "初期SF・パルプ期",
    "definition": "H.G.ウェルズが『タイムマシン』（1895）『宇宙戦争』（1898）等"
        "で確立した近代SFの祖型。同時代に「scientific romance」と呼ばれた"
        "形式は、科学的仮説（時間旅行、異星侵略、進化的他者）を文学的"
        "思考実験に変換し、社会批評と結合した近代SFの方法論を方向づけた。",
    "background": "19世紀末英国の進化論論争（ハクスリーら）と社会改革思想。",
    "development": "20世紀ディストピア文学、宇宙SF、思考実験SFの直接の祖。",
    "historical_context": "ヴィクトリア末期からエドワード朝の科学普及期。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/35",
    "primary_source_type": "Project Gutenberg — Wells Time Machine full text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ジュール・ヴェルヌ「驚異の旅」",
    "name_en": "Jules Verne: Voyages extraordinaires",
    "name_original": "Voyages extraordinaires",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "初期SF・パルプ期",
    "definition": "ジュール・ヴェルヌ（1828-1905）が出版社エッツェルとともに"
        "1864年から展開した連作シリーズ。『地底旅行』『海底二万里』"
        "『八十日間世界一周』等64編を含み、地理学・科学・技術への教養的"
        "情熱を冒険物語と結合させた。近代SFのもうひとつの祖。",
    "background": "第二帝政期フランスの科学万博文化と地理学的探検熱。",
    "development": "20世紀冒険SF、ハードSF的科学主義の系譜の起源。",
    "historical_context": "第二帝政・第三共和政期の科学普及運動。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/164",
    "primary_source_type": "Project Gutenberg — Verne Twenty Thousand Leagues",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "トールキンのセカンダリーワールド",
    "name_en": "Tolkien secondary world",
    "name_original": "Secondary World",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "黄金時代・古典化期",
    "definition": "J.R.R.トールキンが論文「妖精物語について」（On Fairy-Stories, "
        "1947初出講演1939）で理論化した概念。一次世界（現実世界）に対し、"
        "作家が独自の言語・歴史・地理を持つ自律的な「二次世界」を創造する"
        "ファンタジー方法論を指す。『指輪物語』（1954-1955）がその実践。",
    "background": "オックスフォードの言語学・古英語文学研究を背景。",
    "development": "戦後ファンタジー全般、ル・グウィン・マーティン等の世界構築"
        "ファンタジーの理論的基盤。",
    "historical_context": "戦間期オックスフォード・インクリングス文学共同体。",
    "primary_source_url": "https://archive.org/details/tolkien-on-fairy-stories",
    "primary_source_type": "Internet Archive — Tolkien 'On Fairy-Stories' essay",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "セカンダリーワールド構築",
         "description": "トールキンの世界構築論は神話DBの神話構築論と接続。"},
    ],
})

add({
    "name_ja": "ル=グウィン『所有せざる人々』",
    "name_en": "Le Guin: The Dispossessed",
    "name_original": "The Dispossessed: An Ambiguous Utopia",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "アーシュラ・K・ル=グウィンが1974年に発表したSF長篇。"
        "副題「曖昧なユートピア」が示す通り、アナーキズム的惑星アナレスと"
        "資本主義的双子惑星ウラスを並置し、ユートピア的政治思想実験を"
        "SFの形式で展開した。ヒューゴ・ネビュラ両賞を受賞しSFの社会派"
        "潮流を代表する。",
    "background": "1960-70年代のニューウェーブSFと反戦・第二波フェミニズム運動。",
    "development": "現代の社会派SF、フェミニストSF、cli-fiまでの理論的源流。",
    "historical_context": "1970年代米国の反体制思想と科学技術批判の高揚期。",
    "primary_source_url": "http://www.isfdb.org/cgi-bin/title.cgi?1819",
    "primary_source_type": "ISFDB — canonical bibliographic record",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アシモフ『ファウンデーション』",
    "name_en": "Asimov: Foundation",
    "name_original": "Foundation",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "黄金時代・古典化期",
    "definition": "アイザック・アシモフが1942-1953年に発表した連作"
        "（1951年に長篇化）。「心理歴史学（psychohistory）」という架空学問"
        "を中軸に、銀河帝国の崩壊と再建千年計画を描く壮大な歴史的SF。"
        "黄金時代SFの代表作で、後続のスペースオペラ・社会SFの基準点となる。",
    "background": "1940年代米国パルプマガジン文化（特にAstounding誌）と"
        "編集者ジョン・キャンベルの方向づけ。",
    "development": "アシモフのロボット三原則体系と統合され、現代AI倫理議論にも影響。",
    "historical_context": "戦時・戦後の米国大衆文学産業期。",
    "primary_source_url": "http://www.isfdb.org/cgi-bin/title.cgi?22942",
    "primary_source_type": "ISFDB — Foundation series canonical record",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "サイバーパンク（Gibson『ニューロマンサー』）",
    "name_en": "cyberpunk (Gibson: Neuromancer)",
    "name_original": "Neuromancer / cyberpunk",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "ウィリアム・ギブスン『ニューロマンサー』（1984）が結晶化した"
        "SFサブジャンル。電脳空間（cyberspace）・人工知能・低層ハッカー文化を"
        "中核モチーフとし、企業国家化したディストピア都市を舞台に高度技術と"
        "社会的辺境者の交差を描く。Bruce Sterlingらが『Mirrorshades』（1986）"
        "で運動化した。",
    "background": "1980年代の情報技術台頭と新自由主義経済再編。",
    "development": "現代のpost-cyberpunk・solarpunk、AI文学・vaporwave等"
        "ポップカルチャー全般の母型。",
    "historical_context": "1980年代米国レーガン期の技術-経済転換。",
    "primary_source_url": "http://www.isfdb.org/cgi-bin/title.cgi?2289",
    "primary_source_type": "ISFDB — Neuromancer canonical record",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "サイバーパンクの「人間/機械境界の溶解」テーゼは、"
            "現在のAI主体性論争を先取りする文学的予示として再活性化する。",
         "related_ai_phenomenon": "AI主体性・人間機械境界論争"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "電脳空間内の自己と現実身体の真正性問題は、"
            "AI生成ペルソナの真正性問題と直結する。",
         "related_ai_phenomenon": "AIアバター・生成ペルソナの真正性"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "shared_concept",
         "target_entity_name": "サイバースペース／AI主体",
         "description": "サイバーパンクのAI想像力はAI発展DBの主体性論議と接続。"},
        {"target_db": "PHIL", "link_type": "parallel",
         "target_entity_name": "ポストヒューマン主体",
         "description": "哲学DBのポストヒューマン主体性論と並行展開。"},
    ],
})

add({
    "name_ja": "ハードSFとソフトSFの区別",
    "name_en": "hard SF vs soft SF",
    "name_original": "hard SF / soft SF",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "P. Schuyler Millerが1957年Astounding誌書評で導入した"
        "「ハードSF」と、対比語として用いられた「ソフトSF」の区別。"
        "前者は物理学・天文学・工学等「硬い」科学への忠実度を重視する作品"
        "（Clarke・Niven等）、後者は心理学・社会学・人類学等「柔らかい」"
        "科学に基づく作品（Le Guin等）を指す。SF内部のジャンル自己理解の"
        "中心軸。",
    "background": "1950-60年代米国SF批評の自己定義運動。",
    "development": "1980-90年代に学術的SF研究（Science Fiction Studies誌）が"
        "より精緻に再定式化。",
    "historical_context": "黄金時代SFからニューウェーブへの移行期。",
    "primary_source_url": "https://www.depauw.edu/sfs/",
    "primary_source_type": "Science Fiction Studies (DePauw) — academic journal",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "クライ・フィ（気候フィクション）",
    "name_en": "climate fiction (cli-fi)",
    "name_original": "cli-fi",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ポップ・グローバル化期",
    "definition": "ジャーナリスト／作家ダン・ブルームが2007-2008年頃に造語した"
        "ジャンル名。気候変動を中核主題とする小説（K.S.Robinson『2312』、"
        "M.Atwood『MaddAddam』三部作、R.Powers『Overstory』等）を指し、"
        "2010年代にAdam Trexler『Anthropocene Fictions』（2015）等が"
        "学術ジャンルとして制度化した。",
    "background": "2000年代の気候危機認識と文学的応答。",
    "development": "現代の人新世文学・環境人文学の中核ジャンルに。",
    "historical_context": "2010年代の気候危機文化的可視化期。",
    "primary_source_url": "http://www.isfdb.org/cgi-bin/pl.cgi?529620",
    "primary_source_type": "ISFDB — climate fiction bibliographic listing",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "気候という非人間的時間スケールの叙述化は、"
            "AIによる大規模スケール叙述生成と並行して再考される。",
         "related_ai_phenomenon": "AIによる非人間スケール叙述"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "人類規模の集合的主体を物語化する試みは、"
            "AI時代の人間/種スケールの主体性問題と接続する。",
         "related_ai_phenomenon": "種スケールの主体性とAI"},
    ],
})


# ===============================================================
# CATEGORY C — Mystery / hardboiled / thriller (8)
# ===============================================================

add({
    "name_ja": "ポー「モルグ街の殺人」（探偵小説起源）",
    "name_en": "Poe: The Murders in the Rue Morgue",
    "name_original": "The Murders in the Rue Morgue",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "初期SF・パルプ期",
    "definition": "エドガー・アラン・ポーが1841年Graham's Magazineに発表した"
        "短篇。素人探偵デュパンが論理的「分析」によって犯罪を解決する形式を"
        "確立し、近代探偵小説（detective fiction）の原型テクストとして"
        "コナン・ドイル以下すべてのミステリの起源とされる。",
    "background": "19世紀前半の都市犯罪報道とポーの分析的批評精神。",
    "development": "ドイル・クリスティ・ハードボイルドまで全ミステリの祖。",
    "historical_context": "19世紀米国の雑誌文芸産業期。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/2148",
    "primary_source_type": "Project Gutenberg — Poe Works full text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "コナン・ドイル『シャーロック・ホームズ』",
    "name_en": "Conan Doyle: Sherlock Holmes",
    "name_original": "The Adventures of Sherlock Holmes",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "初期SF・パルプ期",
    "definition": "アーサー・コナン・ドイルが1887-1927年に発表したシャーロック・"
        "ホームズ・シリーズ（4長篇＋56短篇）。観察と演繹推理に基づく"
        "「コンサルティング探偵」の形式を確立し、探偵小説をジャンル文学"
        "市場の中核に押し上げた。後の黄金時代ミステリ全般の規範となる。",
    "background": "ヴィクトリア末期の科学的合理性信仰と都市犯罪報道。",
    "development": "黄金時代ミステリ・現代刑事ドラマ・各種パスティーシュの直接の祖。",
    "historical_context": "ヴィクトリア朝末からエドワード朝の雑誌文化期。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/1661",
    "primary_source_type": "Project Gutenberg — Adventures of Sherlock Holmes",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "クリスティと黄金時代ミステリ",
    "name_en": "Christie golden age mystery",
    "name_original": "Golden Age detective fiction",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "黄金時代・古典化期",
    "definition": "アガサ・クリスティ（1890-1976）を代表とする1920-30年代英米の"
        "ミステリ運動。ポアロ・ミス・マープル等の名探偵、フェアプレイ原則、"
        "クローズドサークル形式を方法論的に洗練し、Detection Club（1930年"
        "創設）を制度的中心とする。S.S.ヴァン・ダイン20則・ノックス10戒"
        "等の規約により形式化した。",
    "background": "戦間期英国中流階級の余暇読書市場。",
    "development": "現代の本格ミステリ・パズラー系全般の規範起点。",
    "historical_context": "両大戦間期の出版産業安定成長期。",
    "primary_source_url": "https://www.agathachristie.com/about/the-detection-club",
    "primary_source_type": "Agatha Christie Estate — official Detection Club",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ハードボイルド（HammettとChandler）",
    "name_en": "hardboiled (Hammett, Chandler)",
    "name_original": "hardboiled detective fiction",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "黄金時代・古典化期",
    "definition": "ダシール・ハメットが『ブラック・マスク』誌（1920年代）で"
        "確立し、レイモンド・チャンドラー『大いなる眠り』（1939）等が深化"
        "させた米国ミステリ様式。私立探偵を主人公とし、簡潔で口語的な"
        "一人称描写、都市の腐敗、暴力の実在的描写を特徴とする。"
        "Chandlerエッセイ「Simple Art of Murder」（1944）が様式論の古典。",
    "background": "禁酒法時代の米国都市犯罪と男性労働者大衆雑誌文化。",
    "development": "戦後米国ノワール、現代私立探偵小説の様式的基盤。",
    "historical_context": "1920-40年代米国大都市の社会的混乱期。",
    "primary_source_url": "https://www.theatlantic.com/magazine/archive/1944/12/the-simple-art-of-murder/656179/",
    "primary_source_type": "The Atlantic archive — Chandler 'Simple Art of Murder'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ノワール",
    "name_en": "noir",
    "name_original": "roman noir / film noir",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "黄金時代・古典化期",
    "definition": "1940-50年代に確立した暗鬱・宿命的・道徳的曖昧さを特徴と"
        "する物語様式。フランス批評家がアメリカ犯罪映画群に「film noir」"
        "の名を与え（Nino Frank 1946、Borde & Chaumeton 1955）、それが"
        "文学的源流（ハードボイルド・パルプ犯罪小説）に遡及的に適用された。"
        "Cain・Goodisらが文学的中核。",
    "background": "戦間期から戦後の米国都市の社会不安と実存主義的気分。",
    "development": "現代のネオノワール（Ellroy、ポラニスキ）まで継承。",
    "historical_context": "戦中・戦後の米国大衆心性と仏文学批評の合流。",
    "primary_source_url": "https://www.jstor.org/journal/journpopcult",
    "primary_source_type": "Journal of Popular Culture — noir studies archive",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "警察小説（police procedural）",
    "name_en": "police procedural",
    "name_original": "police procedural",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "黄金時代・古典化期",
    "definition": "1940-50年代に確立したミステリのサブジャンル。私立探偵や"
        "アマチュア探偵ではなく警察組織の捜査手続を主軸とする物語形式で、"
        "Lawrence Treat『V as in Victim』（1945）、Hillary Waugh『Last "
        "Seen Wearing』（1952）、Ed McBain（87分署シリーズ）等が祖型。"
        "現代の刑事ドラマ全般の基盤。",
    "background": "戦後米国の都市警察制度の文化的可視化と取材ジャーナリズム。",
    "development": "現代のEd McBain・松本清張系警察小説、TV刑事ドラマ全般の母型。",
    "historical_context": "戦後米国の都市行政・警察改革期。",
    "primary_source_url": "https://www.britannica.com/art/police-procedural",
    "primary_source_type": "Encyclopedia Britannica — police procedural entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "スリラー",
    "name_en": "thriller",
    "name_original": "thriller",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "黄金時代・古典化期",
    "definition": "サスペンス・緊張・脅威を中核効果とするジャンル。20世紀初頭の"
        "John Buchan『三十九階段』（1915）、戦後のIan Fleming『007』、"
        "Frederick Forsyth『ジャッカルの日』、現代のLee Child・Gillian "
        "Flynnまで連続する。心理スリラー・政治スリラー・テクノスリラー等"
        "のサブジャンル群を含む大ジャンル。",
    "background": "20世紀地政学的冷戦・テロリズム・国際諜報の文化的可視化。",
    "development": "現代ベストセラー市場の中核ジャンル、映画・TV連動の典型。",
    "historical_context": "20世紀後半の冷戦・対テロ戦争文化期。",
    "primary_source_url": "https://www.britannica.com/art/thriller",
    "primary_source_type": "Encyclopedia Britannica — thriller entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "密室ミステリ（locked room mystery）",
    "name_en": "locked room mystery",
    "name_original": "locked room mystery",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "黄金時代・古典化期",
    "definition": "Poe「モルグ街の殺人」（1841）に起源を持ち、Gaston Leroux"
        "『黄色い部屋の謎』（1907）、John Dickson Carr『三つの棺』（1935）"
        "が古典化した不可能犯罪サブジャンル。物理的に密閉された空間で"
        "生じる犯罪を論理的に解決する形式で、Carr『三つの棺』第17章の"
        "「密室講義」が様式論の古典。",
    "background": "19世紀ゴシック・密室小説の論理化への希求。",
    "development": "現代日本の本格ミステリ（綾辻・島田・有栖川等）まで連続的展開。",
    "historical_context": "黄金時代ミステリの形式実験期。",
    "primary_source_url": "https://www.locusmag.com/Reviews/2014/09/lila-cox-reviews-the-three-coffins/",
    "primary_source_type": "Locus Magazine — Carr canonical reception",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY D — Graphic novel / comics (8)
# ===============================================================

add({
    "name_ja": "マンガの文学運動化",
    "name_en": "manga literary movement",
    "name_original": "劇画 / 文学的マンガ",
    "original_script": "japanese",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "1950-60年代の辰巳ヨシヒロ「劇画」運動以降、手塚治虫の"
        "ストーリーマンガ確立、つげ義春・白土三平らの貸本マンガを経て、"
        "マンガが児童向け娯楽から成人向け文学的表現として制度化された"
        "潮流。ガロ・COM等の雑誌が制度的中軸となり、20世紀後半に"
        "国際的「manga」概念として再輸出された。",
    "background": "戦後日本の出版産業再編と貸本文化。",
    "development": "現代世界マンガ市場・グローバル文化現象の基盤。",
    "historical_context": "戦後日本の大衆文化革新期。",
    "primary_source_url": "https://www.jstor.org/journal/mechademia",
    "primary_source_type": "Mechademia (U. Minnesota Press) — academic journal",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "manga大衆文化",
         "description": "マンガ文学化は人類学DBの大衆文化グローバル化研究と接続。"},
    ],
})

add({
    "name_ja": "グラフィックノベルの文学化",
    "name_en": "graphic novel literary",
    "name_original": "graphic novel",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "Will Eisner『A Contract with God』（1978）の表題で広く"
        "流通した「graphic novel」概念。コミックブックを「ノベル」と"
        "等価な長篇文学形式として位置づけ、書店流通・書評対象・図書館"
        "蔵書化への道を開いた。1980年代後半のMaus・Watchmen・Dark "
        "Knight Returnsで決定的に成立した文学カテゴリ。",
    "background": "1970年代米国コミック産業のサブカルチャー化と成人読者拡大。",
    "development": "現代のグラフィックノベル市場・コミックスタディーズの基盤。",
    "historical_context": "1970-80年代米国コミック産業再編期。",
    "primary_source_url": "https://www.willeisner.com/library/a-contract-with-god/",
    "primary_source_type": "Will Eisner Studios — canonical publisher record",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シュピーゲルマン『マウス』",
    "name_en": "Spiegelman: Maus",
    "name_original": "Maus: A Survivor's Tale",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "アート・シュピーゲルマンが雑誌RAWに連載（1980-1991）し、"
        "1986/1991年に2巻として刊行したグラフィックノベル。父親のホロコースト"
        "体験を、ユダヤ人を鼠、ナチスを猫として描く動物寓話形式で証言した。"
        "1992年特別ピューリッツァー賞を受賞し、グラフィックノベルが文学的"
        "正統性を獲得する分水嶺となった。",
    "background": "戦後ホロコースト第二世代の証言文学運動。",
    "development": "Persepolis・FunHome等の自伝的グラフィックノベルの祖型。",
    "historical_context": "1980-90年代の記憶・証言文学の制度化期。",
    "primary_source_url": "https://www.penguinrandomhouse.com/books/8796/the-complete-maus-by-art-spiegelman/",
    "primary_source_type": "Penguin Random House — canonical edition",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "『ウォッチメン』の文学的手法",
    "name_en": "Watchmen literary moves",
    "name_original": "Watchmen",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "アラン・ムーア（脚本）とデイヴ・ギボンズ（作画）が"
        "1986-1987年にDCコミックスから連載した12号構成のグラフィックノベル。"
        "9パネル・グリッド構造、章末の散文挿入、左右ページの図像対応など、"
        "コミックス固有の文学的方法を体系的に展開し、スーパーヒーロー"
        "ジャンルを脱構築した。Time誌「100 best novels since 1923」"
        "に唯一選出されたグラフィックノベル（2005）。",
    "background": "1980年代英米コミックの「British Invasion」とムーアの脱構築的詩学。",
    "development": "現代のスーパーヒーロー再解釈・批評的グラフィックノベルの規範。",
    "historical_context": "1980年代後半の冷戦終末期と核不安の文化的可視化。",
    "primary_source_url": "https://www.dccomics.com/graphic-novels/watchmen-1986/watchmen",
    "primary_source_type": "DC Comics — canonical publisher record",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "サトラピ『ペルセポリス』",
    "name_en": "Satrapi: Persepolis",
    "name_original": "Persepolis",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ポップ・グローバル化期",
    "definition": "マルジャン・サトラピが2000-2003年にフランスで発表した"
        "自伝的グラフィックノベル4巻。イラン革命下のテヘランで育った著者の"
        "少女期から青年期を、白黒のミニマルな線画で描き、グラフィックノベル"
        "がトランスナショナル女性自伝の有力な形式となることを示した。"
        "2007年映画化。",
    "background": "イラン革命亡命者の集合的記憶文学運動。",
    "development": "現代のディアスポラ・グラフィックノベル、女性自伝的"
        "コミックの基準作。",
    "historical_context": "ポスト9.11の文化的中東表象再考期。",
    "primary_source_url": "https://www.penguinrandomhouse.com/books/14067/persepolis-by-marjane-satrapi/",
    "primary_source_type": "Pantheon / Random House — canonical English edition",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "ディアスポラ自伝",
         "description": "サトラピの自伝は人類学DBのディアスポラ研究と直結。"},
    ],
})

add({
    "name_ja": "コミックス研究（comics studies）",
    "name_en": "comics studies",
    "name_original": "comics studies",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ポップ・グローバル化期",
    "definition": "1990-2000年代に学術領域として制度化したコミックス・"
        "グラフィックノベル研究。International Journal of Comic Art（1999-）、"
        "ImageTexT（2004-）、Comics Studies Society（2014-）等が機関的中軸。"
        "視覚-言語混合メディアの理論化を、Hatfield・Chute・Hortonら学者が"
        "推進している。",
    "background": "1990年代以降のグラフィックノベル正統化と大学院プログラム創設。",
    "development": "現代のメディアスタディーズ・視覚文化論の重要分野。",
    "historical_context": "1990-2010年代のメディア・カルチュラル・スタディーズ拡張期。",
    "primary_source_url": "https://www.imagetextjournal.com/",
    "primary_source_type": "ImageTexT (U. Florida) — open access journal",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "シーケンシャル・アート理論",
    "name_en": "sequential art theory",
    "name_original": "sequential art",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "Will Eisner『Comics and Sequential Art』（1985）と"
        "Scott McCloud『Understanding Comics』（1993）が体系化した、"
        "「並置された絵画的・他の像を意図的シーケンスで配置するもの」"
        "（McCloud）としてコミックスを定義する理論枠組み。コマ・"
        "溝（gutter）・パネル間閉合（closure）等の概念がコミックス"
        "形式論の中核装置となった。",
    "background": "Eisner自身のコミック制作経験と教育者としての方法論的整理。",
    "development": "現代コミックス研究の方法論的基盤。Hatfield、Groensteen等"
        "の理論家が継承・批判。",
    "historical_context": "1980-90年代の北米コミックス自己理論化期。",
    "primary_source_url": "https://www.harpercollins.com/products/understanding-comics-scott-mccloud",
    "primary_source_type": "HarperCollins — McCloud canonical edition",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "マンガとコミックの区別",
    "name_en": "manga vs comic distinctions",
    "name_original": "manga / comics distinction",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ポップ・グローバル化期",
    "definition": "日本のマンガと欧米コミックスの様式的・産業的・読書文化的"
        "差異をめぐる比較研究領域。右綴じvs左綴じ、白黒主体vsカラー主体、"
        "雑誌連載・単行本流通モデル、コマ密度と視線誘導、ジャンル多様性等を"
        "Frederik Schodt『Manga! Manga!』（1983）、Jaqueline Berndt等が"
        "理論化した。",
    "background": "1980-90年代以降のマンガのグローバル流通拡大。",
    "development": "現代のグローバル・マンガ研究、トランスナショナル・コミック"
        "比較研究の基盤。",
    "historical_context": "1990-2000年代の日本マンガ世界市場拡大期。",
    "primary_source_url": "https://www.jstor.org/journal/intejcomicart",
    "primary_source_type": "International Journal of Comic Art (JSTOR) — academic journal",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY E — Mass literature / genre theory (8)
# ===============================================================

add({
    "name_ja": "ヤングアダルト文学の出現",
    "name_en": "young adult literature emergence",
    "name_original": "young adult literature",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "1960年代後半〜70年代に米国出版業界・図書館界で制度化した"
        "「young adult」ジャンル。S.E. Hinton『The Outsiders』（1967）"
        "が祖型作とされ、1970年代米国図書館協会のYALSA設立とMargaret A. "
        "Edwards Award創設（1988）で制度的に確立した。「子供」と「大人」の"
        "間の独自の読者層・主題系を制度化した。",
    "background": "戦後ベビーブーマー世代の青少年文化の市場化。",
    "development": "Rowling・Collins・Greenら現代YA文学市場の基盤。",
    "historical_context": "1960-70年代米国の青少年文化革命期。",
    "primary_source_url": "https://www.ala.org/yalsa/",
    "primary_source_type": "ALA / YALSA — Young Adult Library Services Association",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "「特定読者層の制度化」というYAジャンル形成は、"
            "AI時代の読者セグメント生成・パーソナライゼーションと接続する。",
         "related_ai_phenomenon": "AIによる読者セグメント生成"},
    ],
})

add({
    "name_ja": "ジャンル文学vs文学小説論争",
    "name_en": "genre fiction vs literary fiction debate",
    "name_original": "genre vs literary fiction",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ポップ・グローバル化期",
    "definition": "20世紀後半から現代まで継続する、ジャンル文学（SF・"
        "ミステリ・ロマンス等）と「文学的」小説の階層的二分法をめぐる"
        "論争。Ursula K. Le Guin、Margaret Atwood、Michael Chabon等の"
        "作家自身が境界批判を展開し、現代の批評（John Frow『Genre』2006、"
        "Theodore Martin『Contemporary Drift』2017）が学術的に再整理した。",
    "background": "ニュー・クリティシズム以降の正典/通俗の階層的整序への批判。",
    "development": "現代のpost-genre / interstitial fiction議論まで継続。",
    "historical_context": "1990-2020年代の出版マーケティングと文学批評の再交渉期。",
    "primary_source_url": "https://www.routledge.com/Genre/Frow/p/book/9781138937758",
    "primary_source_type": "Routledge — Frow Genre canonical edition",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "「正典/通俗」二分法はAI訓練データの正典バイアス問題と"
            "直結し、ジャンル境界の歴史性を再考させる。",
         "related_ai_phenomenon": "AI訓練データの正典/通俗バイアス"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "ジャンル理論",
         "description": "詩学DBのジャンル理論と直結する大論争。"},
    ],
})

add({
    "name_ja": "マスマーケット・ペーパーバック",
    "name_en": "mass market paperback",
    "name_original": "mass market paperback",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "黄金時代・古典化期",
    "definition": "1935年Allen LaneのPenguin Books創設、1939年米国Pocket "
        "Books創設に始まる、低価格・大量流通の文庫形式。書店・新聞スタンド・"
        "ドラッグストアでの流通を可能にし、20世紀後半の大衆文学市場の物質的"
        "基盤を成した。装丁・価格・流通モデルが内容（ジャンル文学）と相互"
        "規定的に発展した。",
    "background": "大恐慌期の出版産業再編と中産階級読書習慣変化。",
    "development": "現代の電子書籍・サブスクリプション読書サービスまでの"
        "大衆出版モデルの源流。",
    "historical_context": "1930-50年代の米英出版革命期。",
    "primary_source_url": "https://www.pulpmags.org/",
    "primary_source_type": "Pulp Magazines Project — historical context archive",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "partial",
         "rationale": "物質的書物の安価大量流通モデルは、AI時代の"
            "デジタル無限複製・サブスクリプションへ部分的に移行している。",
         "related_ai_phenomenon": "AI生成コンテンツの大量複製可能性"},
        {"axis": "正典", "status": "rethinking",
         "rationale": "ペーパーバック流通は「通俗」の正典化を可能にしたが、"
            "AI時代には正典/通俗の境界自体が再交渉される。",
         "related_ai_phenomenon": "AIによる正典再編成"},
    ],
})

add({
    "name_ja": "ロマンス小説（ジャンル）",
    "name_en": "romance novel as genre",
    "name_original": "romance novel",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ジャンル多様化期",
    "definition": "20世紀ハーレクイン社（カナダ）の世界的拡大（1957年Mills & Boon"
        "提携）とともに大衆ジャンルとして制度化された恋愛小説形式。"
        "Romance Writers of America（RWA, 1980年創設）が「中心的恋愛"
        "ストーリー」「感情的に満足する楽観的結末」をジャンル定義としている。"
        "Janice Radway『Reading the Romance』（1984）が学術的読者研究を"
        "確立した。",
    "background": "戦後英米女性読者市場の制度化と出版マーケティング革新。",
    "development": "現代のロマンスサブジャンル多様化（パラノーマル・"
        "ヒストリカル・LGBTQ+ロマンス等）の基盤。",
    "historical_context": "1950-80年代の女性読書文化の市場化。",
    "primary_source_url": "https://www.uncpress.org/book/9780807841495/reading-the-romance/",
    "primary_source_type": "U. North Carolina Press — Radway canonical edition",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ウェスタン（ジャンル）",
    "name_en": "western genre",
    "name_original": "western",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "初期SF・パルプ期",
    "definition": "Owen Wister『The Virginian』（1902）を祖型として、"
        "19世紀末-20世紀米国西部辺境を舞台とするジャンル文学。"
        "Zane Grey、Louis L'Amour等のパルプ・大衆作家を経て、"
        "Cormac McCarthy『血と暴力の国』（2005）等の文学的再解釈に至る。"
        "米国国民神話の中核ジャンル。",
    "background": "19世紀末「フロンティアの消滅」言説（Turner 1893）と西部開拓神話。",
    "development": "現代のRevisionist Western、SFウェスタン融合（Firefly等）まで展開。",
    "historical_context": "20世紀米国国民神話形成期。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/1298",
    "primary_source_type": "Project Gutenberg — Wister The Virginian full text",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ホラー（ジャンル）",
    "name_en": "horror as genre",
    "name_original": "horror fiction",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "黄金時代・古典化期",
    "definition": "ゴシック小説（Walpole・Radcliffe）、Poe・Stoker・Lovecraftを"
        "経て20世紀後半に独立ジャンルとして制度化された恐怖文学。"
        "Stephen King（『キャリー』1974〜）の商業的成功とWorld Horror "
        "Convention・Bram Stoker Award（1987-）の制度化により定着した。"
        "Noel Carroll『The Philosophy of Horror』（1990）が学術的フレーム化。",
    "background": "ゴシック・パルプ系譜と戦後米国大衆出版産業の合流。",
    "development": "現代のpost-horror（Aster・Peele）、cosmic horror再評価まで展開。",
    "historical_context": "1970-90年代米国大衆ジャンル文学の頂点期。",
    "primary_source_url": "https://www.routledge.com/The-Philosophy-of-Horror/Carroll/p/book/9780415902168",
    "primary_source_type": "Routledge — Carroll canonical edition",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ディストピア小説（Orwell・Huxley・Atwood）",
    "name_en": "dystopian fiction (Orwell, Huxley, Atwood)",
    "name_original": "dystopian fiction",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "黄金時代・古典化期",
    "definition": "Huxley『すばらしい新世界』（1932）、Orwell『1984年』（1949）、"
        "Atwood『侍女の物語』（1985）を中軸とする、抑圧的近未来社会を描く"
        "サブジャンル。「ユートピア」（More 1516）の反転として、20世紀"
        "全体主義・消費社会・宗教国家・監視社会への文学的批判を展開する。"
        "近年はYA向け（Collins『Hunger Games』2008-）にまで拡張された。",
    "background": "20世紀全体主義（ナチズム・スターリニズム）と消費社会への批判。",
    "development": "現代AI監視社会論・気候ディストピアの理論的源流。",
    "historical_context": "20世紀後半の冷戦・対テロ戦争・新自由主義監視社会期。",
    "primary_source_url": "https://www.britannica.com/art/dystopia",
    "primary_source_type": "Encyclopedia Britannica — dystopia entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "AI監視社会・予測社会への警告物語としてのディストピアは、"
            "現実の生成AI・予測AI技術が登場した時代に再活性化する。",
         "related_ai_phenomenon": "AI監視社会・予測社会"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ディストピア社会哲学",
         "description": "哲学DBの政治哲学（全体主義論・監視社会論）と直結する。"},
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "AI監視社会の警告",
         "description": "AI発展DBにおけるAIガバナンス・倫理議論の文学的予示。"},
    ],
})

add({
    "name_ja": "ファンフィクション現象",
    "name_en": "fan fiction phenomenon",
    "name_original": "fan fiction",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ポップ・グローバル化期",
    "definition": "1960年代Star Trekファンジン文化に起源し、1990-2000年代"
        "FanFiction.net・Archive of Our Own（AO3, 2008-）等のオンライン"
        "プラットフォームで爆発的拡大した、ファンによる既存作品世界の"
        "二次創作実践。Henry Jenkins『Textual Poachers』（1992）が"
        "学術的フレーム化、Karen Hellekson・Kristina Busseらが現代研究を"
        "展開する。",
    "background": "1960-70年代米国SF・テレビファンダム文化と、2000年代の"
        "デジタルプラットフォーム革新。",
    "development": "現代のtransformative works概念、AI生成創作との連続性議論まで展開。",
    "historical_context": "1990-2020年代のデジタルプラットフォーム時代の参加型文化期。",
    "primary_source_url": "https://journal.transformativeworks.org/index.php/twc",
    "primary_source_type": "Transformative Works and Cultures — open access journal",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "ファンフィクションの集合的・派生的著者性は、AI生成"
            "創作の著者性問題と構造的に並列し、近代的単一著者性概念を"
            "再考させる。",
         "related_ai_phenomenon": "AI生成創作の著者性問題"},
        {"axis": "創造性", "status": "rethinking",
         "rationale": "「既存作品からの創発的派生」というファンフィクション"
            "モデルは、AIの訓練データからの生成と並行する創造性概念を"
            "提示する。",
         "related_ai_phenomenon": "AI生成における創造性の再定義"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "派生的創造性",
         "description": "AI発展DBの生成AI創造性論と並行する文学的先駆。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "ファンダム参加型文化",
         "description": "人類学DBの参加型文化研究と直結する。"},
    ],
})

add({
    "name_ja": "読書共同体としてのジャンル",
    "name_en": "genre as reading community",
    "name_original": "genre as reading community",
    "original_script": "roman",
    "subfield_code": SUBFIELD_CODE,
    "region": REGION,
    "period_key": "ポップ・グローバル化期",
    "definition": "ジャンルを単なる形式分類ではなく、特定の読書実践を"
        "共有する「解釈共同体」（Stanley Fish）として捉える理論枠組み。"
        "Janice Radway『Reading the Romance』（1984）の民族誌的読者研究、"
        "Henry Jenkins『Textual Poachers』（1992）のファンダム研究、"
        "John Frow『Genre』（2006）の理論的整理によって体系化された。",
    "background": "1980年代の受容理論・カルチュラル・スタディーズと"
        "民族誌的読者研究の合流。",
    "development": "現代のオンライン読書共同体・Goodreads・BookTok研究まで展開。",
    "historical_context": "1980-2000年代の文学研究の文化研究的転回。",
    "primary_source_url": "https://www.routledge.com/Textual-Poachers/Jenkins/p/book/9780415533294",
    "primary_source_type": "Routledge — Jenkins Textual Poachers canonical edition",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "ジャンル理論",
         "description": "詩学DBのジャンル理論を読者共同体論として拡張。"},
    ],
})


# ---------------------------------------------------------------
# Relations payload (sequential after concepts inserted)
# ---------------------------------------------------------------

RELATIONS: list[tuple[str, str, str, str]] = [
    # A. Children's literature internal
    ("ペロー・グリム童話伝統", "アンデルセン文学童話", "influences",
     "ペロー・グリムの民話編集伝統がアンデルセンの創作童話の前提となる。"),
    ("アンデルセン文学童話", "ルイス・キャロル『不思議の国のアリス』", "influences",
     "アンデルセンの近代文学童話がキャロルのナンセンス文学の前提となる。"),
    ("ルイス・キャロル『不思議の国のアリス』", "ロアルド・ダール児童文学", "influences",
     "キャロルの遊戯的反教訓主義がダールのブラックユーモアに継承される。"),
    ("ビアトリクス・ポター絵本", "モーリス・センダック絵本", "influences",
     "ポターが確立した近代絵本形式が後続のセンダック以降の絵本表現の基盤。"),
    ("モーリス・センダック絵本", "エリック・カール絵本", "influences",
     "センダックの絵本革新がカールらの幼児絵本拡張の前提となる。"),
    ("ロアルド・ダール児童文学", "J.K.ローリング『ハリー・ポッター』", "influences",
     "ダールの寄宿学校・反権威主義モチーフがローリング作品の素地となる。"),
    ("J.K.ローリング『ハリー・ポッター』", "ヤングアダルト文学の出現", "extends",
     "ローリングの世界的成功がYAジャンル市場の決定的拡大を促した。"),

    # B. SF / Fantasy internal
    ("H.G.ウェルズの科学ロマンス", "アシモフ『ファウンデーション』", "influences",
     "ウェルズの社会批評的SFが黄金時代SF全般の前提となる。"),
    ("ジュール・ヴェルヌ「驚異の旅」", "ハードSFとソフトSFの区別", "influences",
     "ヴェルヌの科学的厳密主義がハードSFの理念的源流を成す。"),
    ("H.G.ウェルズの科学ロマンス", "ディストピア小説（Orwell・Huxley・Atwood）", "influences",
     "ウェルズの『タイム・マシン』『モロー博士の島』が20世紀ディストピアの直接の祖。"),
    ("トールキンのセカンダリーワールド", "J.K.ローリング『ハリー・ポッター』", "influences",
     "トールキンの世界構築論がローリングのファンタジー世界の方法的前提。"),
    ("アシモフ『ファウンデーション』", "ル=グウィン『所有せざる人々』", "influences",
     "アシモフの社会的SFがル=グウィン社会派SFの方法的前提。"),
    ("ル=グウィン『所有せざる人々』", "クライ・フィ（気候フィクション）", "influences",
     "ル=グウィンの社会派SFがcli-fiの政治批評的SF系譜の中心。"),
    ("サイバーパンク（Gibson『ニューロマンサー』）", "クライ・フィ（気候フィクション）", "influences",
     "サイバーパンクの近未来批評的様式がcli-fiに方法論的に継承される。"),
    ("ハードSFとソフトSFの区別", "サイバーパンク（Gibson『ニューロマンサー』）", "influences",
     "ハード/ソフト区別をめぐる議論がサイバーパンクの自己定義を方向づけた。"),

    # C. Mystery / Thriller internal
    ("ポー「モルグ街の殺人」（探偵小説起源）", "コナン・ドイル『シャーロック・ホームズ』", "influences",
     "ポーのデュパン物語がドイルのホームズ造型の直接の祖。"),
    ("コナン・ドイル『シャーロック・ホームズ』", "クリスティと黄金時代ミステリ", "influences",
     "ドイルの方法主義的探偵物語が黄金時代ミステリの前提となる。"),
    ("クリスティと黄金時代ミステリ", "密室ミステリ（locked room mystery）", "contains",
     "黄金時代ミステリは密室ミステリを中核形式の一つとして包含する。"),
    ("コナン・ドイル『シャーロック・ホームズ』", "ハードボイルド（HammettとChandler）", "influences",
     "ドイル系古典探偵への対抗様式としてハードボイルドが成立した。"),
    ("ハードボイルド（HammettとChandler）", "ノワール", "extends",
     "ハードボイルドがノワール様式の文学的核を成す。"),
    ("ハードボイルド（HammettとChandler）", "警察小説（police procedural）", "influences",
     "ハードボイルドの都市犯罪リアリズムが警察小説の前提となる。"),
    ("クリスティと黄金時代ミステリ", "スリラー", "influences",
     "黄金時代ミステリの緊張形式がスリラージャンルの方法的源泉を成す。"),
    ("ポー「モルグ街の殺人」（探偵小説起源）", "密室ミステリ（locked room mystery）", "influences",
     "ポーは密室ミステリの起源テクストを提供した。"),

    # D. Graphic novel / comics internal
    ("マンガの文学運動化", "グラフィックノベルの文学化", "parallel",
     "日本のマンガ文学化と欧米グラフィックノベル化は1960-70年代に並行展開。"),
    ("グラフィックノベルの文学化", "シュピーゲルマン『マウス』", "contains",
     "Maus はグラフィックノベル文学化の決定的画期作品。"),
    ("グラフィックノベルの文学化", "『ウォッチメン』の文学的手法", "contains",
     "Watchmen はグラフィックノベル文学化のもう一つの画期作品。"),
    ("シュピーゲルマン『マウス』", "サトラピ『ペルセポリス』", "influences",
     "Maus の自伝的グラフィックノベル形式がPersepolisの方法的前提。"),
    ("シーケンシャル・アート理論", "コミックス研究（comics studies）", "influences",
     "Eisner・McCloudの理論がコミックス研究領域の方法論的中軸を成す。"),
    ("マンガとコミックの区別", "コミックス研究（comics studies）", "contains",
     "マンガ/コミックス比較は現代コミックス研究の中核領域。"),
    ("『ウォッチメン』の文学的手法", "シーケンシャル・アート理論", "extends",
     "Watchmen はEisner理論を実践的に最も高度に展開した作例。"),
    ("マンガの文学運動化", "マンガとコミックの区別", "extends",
     "日本マンガ文学化の進展が国際比較研究を促した。"),

    # E. Mass / genre theory internal
    ("マスマーケット・ペーパーバック", "ロマンス小説（ジャンル）", "influences",
     "ペーパーバック流通モデルがロマンスの大衆ジャンル化を可能にした。"),
    ("マスマーケット・ペーパーバック", "ウェスタン（ジャンル）", "influences",
     "ペーパーバック流通がウェスタンの大衆ジャンル定着を可能にした。"),
    ("マスマーケット・ペーパーバック", "ホラー（ジャンル）", "influences",
     "ペーパーバック流通が戦後ホラーの大衆ジャンル化を可能にした。"),
    ("ジャンル文学vs文学小説論争", "読書共同体としてのジャンル", "extends",
     "二分法批判が「読書共同体としてのジャンル」概念へと展開する。"),
    ("ロマンス小説（ジャンル）", "読書共同体としてのジャンル", "influences",
     "Radway のロマンス読者民族誌が読書共同体ジャンル論の出発点。"),
    ("ファンフィクション現象", "読書共同体としてのジャンル", "extends",
     "ファンフィクション研究がジャンル＝共同体論を最も先鋭に展開する。"),
    ("ヤングアダルト文学の出現", "ジャンル文学vs文学小説論争", "extends",
     "YAジャンルの制度化が「文学性」の正典/通俗階層を再交渉した。"),
    ("ディストピア小説（Orwell・Huxley・Atwood）", "ヤングアダルト文学の出現", "influences",
     "Atwood以降のディストピアがCollins等YAディストピアの直接の前提。"),

    # Cross-category bridges (children × SF × mystery × graphic × theory)
    ("J.K.ローリング『ハリー・ポッター』", "ファンフィクション現象", "influences",
     "Harry Potterファンダムが現代ファンフィクション・コミュニティ拡大の決定的契機。"),
    ("サイバーパンク（Gibson『ニューロマンサー』）", "ディストピア小説（Orwell・Huxley・Atwood）", "extends",
     "サイバーパンクは20世紀ディストピアの技術論的展開。"),
    ("『ウォッチメン』の文学的手法", "ジャンル文学vs文学小説論争", "extends",
     "Watchmenはコミックスを「文学」として再定位することで境界論争を再活性化した。"),
    ("マンガの文学運動化", "ヤングアダルト文学の出現", "parallel",
     "マンガの青少年読者ジャンル化はYA形成と並行する東アジア事例。"),
    ("シュピーゲルマン『マウス』", "ジャンル文学vs文学小説論争", "extends",
     "Mausのピューリッツァー受賞は「文学」の境界拡張の決定的画期。"),
    ("ハードボイルド（HammettとChandler）", "サイバーパンク（Gibson『ニューロマンサー』）", "influences",
     "Chandlerの第一人称都市犯罪様式がGibsonサイバーパンクの語りの祖型。"),
    ("ジュール・ヴェルヌ「驚異の旅」", "ヤングアダルト文学の出現", "influences",
     "ヴェルヌの青少年向け冒険SFは20世紀YA SFの直接の祖。"),
    ("ロマンス小説（ジャンル）", "ファンフィクション現象", "influences",
     "ロマンス読者共同体がファンフィクション・コミュニティの組織形態の祖型を提供した。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[wave10_c33_genre] inserting {len(CONCEPTS)} concepts...")
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
                name_ja=name_ja, region=REGION,
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
        print("[wave10_c33_genre] inserted:")
        print(f"  concepts (total): {summary['concepts']}")
        print(f"  fourth_transform_tags: {summary['fourth_transform_tags']} "
              f"(this run: +{fourth_count})")
        print(f"  cross_domain: {summary['cross_domain']} "
              f"(this run: +{cd_count})")
        print(f"  relations: {summary['relations']} "
              f"(this run: +{relation_count})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
