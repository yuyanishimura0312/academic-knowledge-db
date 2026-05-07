"""
LIT-DB Phase 2 — C12: Western Contemporary (西欧現代・21世紀)
=================================================================
Inserts 40 concepts spanning 5 categories of 21st century Western
literature (post-2000):

  A. 21st century novel mainstream (8)
  B. Major author concepts (8)
  C. Contemporary metafiction forms (8)
  D. Major themes / contemporary issues (8)
  E. Form / criticism concepts (8)

subfield_id=7 (lit_eu_postmodern) — contemporary 21c is housed here
alongside C11 postmodern; this batch focuses strictly on post-2000
phenomena to avoid overlap.

Pattern applied: P3 (Contemporary Critical Reception). Sources are
JSTOR/Project MUSE academic articles, major author public-domain
interview/essay archives, and recent (post-2010) literary criticism.

Duplicate check: concepts already present in lit.sqlite (climate
fiction, performativity, distant reading, magical realism, hypertext
fiction) are deliberately not re-inserted; C12 introduces narrower
post-2000 successor concepts (e.g. distant reading post-Moretti,
performativity in 21c literature, climate emergency narrative).
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("21世紀現代", "Contemporary 21st century", 2000, 2026,
     "ポストモダン以降の西欧文学。9/11以後の世界、デジタル飽和、気候危機、AI出現を主要文脈とする。"),
    ("ミレニアム転換期", "Turn of the Millennium", 1995, 2010,
     "ポストモダンの自己消費とデジタル化の本格化が交差する移行期。"),
]


# ---------------------------------------------------------------
# Concept payload
# ---------------------------------------------------------------

CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — 21st century novel mainstream (8)
# ===============================================================

add({
    "name_ja": "ポスト・ポストモダニズム",
    "name_en": "post-postmodernism",
    "name_original": "post-postmodernism",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "1990年代末以降、ポストモダンのアイロニー・自己言及・断片化に対する疲弊から登場した文学傾向の総称。誠実さ・関係性・倫理的応答性を再評価し、皮肉と感情の二項対立を再構築しようとする。Jeffrey Nealonら批評家がポストモダン以後の文化状況として理論化した。",
    "background": "Foster Wallace『無限の戯れ』以降、英米批評で「アイロニー疲労」が議論された。",
    "development": "メタモダニズム、新誠実、autofiction、cli-fiなど多岐の傾向を含む包括語として2010年代に定着。",
    "historical_context": "9/11、リーマンショック、SNS浸透という連続する危機的文脈。",
    "primary_source_url": "https://www.jstor.org/stable/24246802",
    "primary_source_type": "JSTOR — Nealon Post-Postmodernism (2012)",
    "importance_score": 5,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "メタモダニズム",
    "name_en": "metamodernism",
    "name_original": "metamodernism",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Timotheus Vermeulen と Robin van den Akker が2010年論文「Notes on Metamodernism」で提唱した文化感性。モダンの真摯さとポストモダンのアイロニーを「振動（oscillation）」として両立させ、希望と憂鬱、誠実さと懐疑のあいだを揺れ動く。",
    "background": "ポストモダンの行き詰まりに対する若年世代の応答として理論化された。",
    "development": "Notes on Metamodernism オンラインジャーナル創刊、Wes Anderson映画・David Foster Wallace散文を典拠例として展開。",
    "historical_context": "金融危機後の世代的感覚としての「楽観的シニシズム」。",
    "primary_source_url": "https://www.tandfonline.com/doi/full/10.3402/jac.v2i0.5677",
    "primary_source_type": "Journal of Aesthetics & Culture — Vermeulen & van den Akker 2010",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "メタモダンの「振動」感性は、AI生成コンテンツに対する視聴者の半信半疑（信じたいが信じきれない）態度を理論化する枠組みとして再評価されている。",
         "related_ai_phenomenon": "AI生成コンテンツへのアンビバレントな視聴者反応"},
        {"axis": "創造性", "status": "rethinking",
         "rationale": "アイロニーと誠実さの両立を志向する創造性概念は、AIとの協働創作における「機械の真摯さ問題」と接続する。",
         "related_ai_phenomenon": "AI協働創作と真摯性"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "メタモダン感性",
         "description": "哲学DBにおける後ポストモダン文化哲学との共有概念。"},
    ],
})

add({
    "name_ja": "9/11小説",
    "name_en": "9/11 fiction",
    "name_original": "9/11 fiction / post-9/11 novel",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "2001年9月11日同時多発テロを直接・間接の主題とする小説群。トラウマ・記憶・テロリズム・米国アイデンティティ危機を中心軸とする。Don DeLillo『Falling Man』、Jonathan Safran Foer『Extremely Loud and Incredibly Close』、Mohsin Hamid『The Reluctant Fundamentalist』が代表的。",
    "background": "9/11が「歴史の終わり」言説を反転させ、新たなトラウマ叙事を要請した。",
    "development": "テロリスト視点小説（Hamid）、子ども視点小説（Foer）、抽象的アレゴリー（DeLillo）と多様化。Richard Gray、Kristiaan Versluysが理論化。",
    "historical_context": "対テロ戦争、サーベイランス国家化、イスラム恐怖症の台頭。",
    "primary_source_url": "https://www.jstor.org/stable/41349040",
    "primary_source_type": "JSTOR — Versluys Out of the Blue (2009)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "クライメート・フィクション（cli-fi）の現代発展",
    "name_en": "climate fiction (cli-fi) post-2000",
    "name_original": "cli-fi / climate fiction",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "気候危機を主題とする21世紀小説ジャンル。ジャーナリストDan Bloomが造語したcli-fiは、Margaret Atwood『MaddAddam』三部作、Richard Powers『The Overstory』、Kim Stanley Robinson『The Ministry for the Future』などを中核に、人新世・地球規模思考・非人間中心主義を文学化する。Adam Trexlerの『Anthropocene Fictions』が学問的体系化。",
    "background": "IPCC報告書の浸透と気候運動の拡大が文学に反響した。",
    "development": "ディストピアSFとリアリズムの融合、種を超えた語り手、惑星規模の時間スケールが特徴。",
    "historical_context": "人新世概念の普及（Crutzen 2000）、グレタ・トゥーンベリ運動。",
    "primary_source_url": "https://www.jstor.org/stable/j.ctvw1d5h1",
    "primary_source_type": "JSTOR — Trexler Anthropocene Fictions (2015)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "人類規模を超えた地質学的時間スケールの物語は、人間中心の物語論を根本的に再考させ、AI時代の非人間的視点創出の先駆形となる。",
         "related_ai_phenomenon": "非人間視点のAI生成ナラティブ"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "人類種としての集合主体性を物語化する試みは、分散主体論・非人間中心主義のAI論と並行する。",
         "related_ai_phenomenon": "分散主体性とAIエージェント"},
    ],
    "cross_domain": [
        {"target_db": "SignalDB", "link_type": "parallel",
         "target_entity_name": "気候危機シグナル",
         "description": "Signal DBの気候関連シグナルとの直接並行関係。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "人新世人類学",
         "description": "人類学DBの人新世研究との接続。"},
    ],
})

add({
    "name_ja": "ニューロ・ノヴェル",
    "name_en": "neuro-novel",
    "name_original": "neuro-novel",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "認知神経科学の知見を物語構造・人物造形に組み込む21世紀小説の一群。Marco Roth が2009年n+1誌論文で命名。Ian McEwan『Saturday』、Richard Powers『The Echo Maker』、Rivka Galchen『Atmospheric Disturbances』が代表例。脳と意識の関係を主題化することで、心的リアリズムの新形態を模索する。",
    "background": "神経科学の一般化（Antonio Damasio、V.S. Ramachandran等の啓蒙書普及）が背景。",
    "development": "意識の流れ手法を神経学的説明と接続、症例研究的人物造形が広がった。",
    "historical_context": "脳科学ブームと「神経人文学」の興隆。",
    "primary_source_url": "https://www.nplusonemag.com/issue-8/essays/the-rise-of-the-neuronovel/",
    "primary_source_type": "n+1 — Roth The Rise of the Neuronovel (2009)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "オートフィクション（21世紀版）",
    "name_en": "autofiction (21st century)",
    "name_original": "autofiction",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Serge Doubrovskyが1977年に造語したautofictionが2010年代に英語圏で大規模に再流行した現象。自伝と虚構の境界を実名・実体験に密着させつつ意図的に揺るがす形式。Karl Ove Knausgård『My Struggle』6巻（2009-2011）、Rachel Cusk『Outline』三部作、Sheila Heti『How Should a Person Be?』が中核。",
    "background": "ポストモダン虚構主義への疲労と「真正なるもの」への渇望が背景。",
    "development": "SNS時代のセルフ・キュレーションと並行する文学現象として理論化（James Wood、Jonathan Sturgeon）。",
    "historical_context": "ソーシャルメディア飽和とアイデンティティ可視化の時代。",
    "primary_source_url": "https://www.newyorker.com/magazine/2017/02/06/karl-ove-knausgaards-quest-for-the-real",
    "primary_source_type": "New Yorker — James Wood on Knausgård (2017)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "実名の自己を虚構的に再構築するautofictionは、AI生成のデジタル分身・パーソナルチャットボットによる主体の脱構築と同時代的に進行している。",
         "related_ai_phenomenon": "AIパーソナルアバター・デジタル分身"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "真正性が虚構を通して構築されるという逆説は、AI生成コンテンツの「本物らしさ」議論と直結する。",
         "related_ai_phenomenon": "生成AIの真正性問題"},
    ],
})

add({
    "name_ja": "ポスト・トゥルース・フィクション",
    "name_en": "post-truth fiction",
    "name_original": "post-truth fiction",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "2016年トランプ当選・Brexitを契機にOxford Dictionaries が「post-truth」を年間語に選定して以降の、虚偽情報・代替事実・陰謀論を主題化する小説群。Karen Russell、Tom McCarthy、Salvatore Scibona、Olivia Laing らが事実と虚構の崩壊を物語化する。",
    "background": "SNS拡散・フェイクニュース・トランプ政権の現実性危機。",
    "development": "陰謀論小説、メディア環境小説、ジャーナリスト主人公の認識論的危機を核とする。",
    "historical_context": "アルゴリズム的情報環境と政治的二極化。",
    "primary_source_url": "https://muse.jhu.edu/article/690987",
    "primary_source_type": "Project MUSE — Post-Truth Studies (2018)",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "ポスト・トゥルース状況下では真正性の規準そのものが揺らぐ。生成AIによる説得的虚構がこの問題を極限化する。",
         "related_ai_phenomenon": "生成AIによるディープフェイク・偽情報拡散"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "AI生成偽情報",
         "description": "AI開発DBの偽情報・ハルシネーション論との並行。"},
        {"target_db": "SignalDB", "link_type": "parallel",
         "target_entity_name": "ポスト真実シグナル",
         "description": "Signal DBの認識論的危機シグナルとの接続。"},
    ],
})

add({
    "name_ja": "ポスト・インターネット・フィクション",
    "name_en": "post-internet fiction",
    "name_original": "post-internet fiction",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "インターネット文化が日常に完全浸透した世代（ミレニアル後期-Z世代）の経験を内在的に描く小説。Patricia Lockwood『No One Is Talking About This』、Lauren Oyler『Fake Accounts』、Tao Lin『Taipei』が代表。Twitter文体、ミーム、ハイパーテキスト的注意分散を文体に取り込む。",
    "background": "Marisa Olson が美術領域で2008年頃使用したpost-internet概念が文学に拡張された。",
    "development": "オンライン-オフラインの区別が無効化された経験、注意散漫を文体化する試み。",
    "historical_context": "スマートフォン浸透とアテンション・エコノミー。",
    "primary_source_url": "https://www.nytimes.com/2021/02/16/books/review-no-one-is-talking-about-this-patricia-lockwood.html",
    "primary_source_type": "NYT — Lockwood review (2021)",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

# ===============================================================
# CATEGORY B — Major author concepts (8)
# ===============================================================

add({
    "name_ja": "ゼーバルトの記念碑的フィクション",
    "name_en": "Sebald's memorial fiction",
    "name_original": "W.G. Sebald — Austerlitz",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "W.G. Sebald（1944-2001）が『Austerlitz』（2001）等で確立した、写真・建築・記憶・歴史を融合する独自形式。フィクションとエッセイ、伝記、紀行文を境界なく接続し、ホロコースト記憶を間接的に喚起する。長文無段落、白黒写真挿入、語り手の媒介的姿勢が特徴。",
    "background": "ドイツ語圏ホロコースト後文学の延長線上に英語圏で受容された。",
    "development": "Teju Cole『Open City』、Ben Lerner、Olivia Laingらに直接的影響。「Sebaldian」が形容詞として定着。",
    "historical_context": "ホロコースト記憶の世代的継承問題、欧州統合の文化的記憶。",
    "primary_source_url": "https://www.jstor.org/stable/40339692",
    "primary_source_type": "JSTOR — Sebald studies",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ボラーニョ『2666』の暴力詩学",
    "name_en": "Bolaño's poetics of violence (2666)",
    "name_original": "Roberto Bolaño — 2666",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Roberto Bolaño（1953-2003）が遺作『2666』（2004死後刊行）で確立した、メキシコ女性連続殺人を中心に5部構成で展開する叙事詩的暴力探究。サンタテレサ（実在シウダー・フアレス）の犯罪記録を反復的・列挙的に提示し、読者を倫理的疲弊に追い込む独自詩学。",
    "background": "ラテンアメリカ・ブームの遺産とポストモダン断片化の継承上に位置。",
    "development": "Don DeLillo『Underworld』後の最大規模「世界小説」として国際的評価を確立、英語圏現代小説に決定的影響。",
    "historical_context": "ネオリベラリズム下のメキシコ・米国国境暴力。",
    "primary_source_url": "https://www.nybooks.com/articles/2008/12/04/the-departed/",
    "primary_source_type": "NYRB — Bolaño 2666 review",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "国境暴力人類学",
         "description": "人類学DBの国境暴力研究との接続。"},
    ],
})

add({
    "name_ja": "クナウスゴール『わが闘争』の極限autofiction",
    "name_en": "Knausgård's My Struggle",
    "name_original": "Karl Ove Knausgård — Min Kamp",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "ノルウェーの作家Karl Ove Knausgård（1968-）が全6巻3,600頁で展開した『Min Kamp』（My Struggle、2009-2011）。実名の家族・友人・自身の卑近な日常を極端な詳細で記述し、autofictionの極限例として国際的論争を呼んだ。Hitler『Mein Kampf』を意図的に喚起するタイトルが倫理論争となった。",
    "background": "ノルウェー文学賞受賞作家としての地位と私生活暴露の倫理的緊張。",
    "development": "英訳出版（Don Bartlett訳）後、Zadie Smith、Jonathan Lethem、Jeffrey Eugenidesらが熱烈擁護、Joyce Carol Oatesらが批判。",
    "historical_context": "SNS時代の自己暴露文化と文学的暴露の境界問題。",
    "primary_source_url": "https://www.newyorker.com/magazine/2014/08/25/total-recall-3",
    "primary_source_type": "New Yorker — Wood on Knausgård (2014)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ベン・ラーナー『10:04』の予測的フィクション",
    "name_en": "Ben Lerner's 10:04",
    "name_original": "Ben Lerner — 10:04",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "詩人・小説家Ben Lerner（1979-）の『10:04』（2014）。前作『Leaving the Atocha Station』（2011）から続く、autofiction的語り手と未来から振り返る予測的叙述を組み合わせる方法。ハリケーン・サンディ、人工授精、芸術助成金など現代米国を素材に、フィクションの倫理的可能性を探究する。",
    "background": "Sebald、Coetzeeの影響下で英語圏autofictionを精緻化。",
    "development": "『The Topeka School』（2019）でレトリック教育と陰謀論の系譜を主題化。",
    "historical_context": "気候災害、生殖技術、ニューヨーク文化生産の経済的脆弱性。",
    "primary_source_url": "https://www.lrb.co.uk/the-paper/v36/n21/adam-mars-jones/the-second-cousin-once-removed",
    "primary_source_type": "LRB — Mars-Jones on 10:04",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "マギー・ネルソン『アルゴノーツ』のハイブリッド批評",
    "name_en": "Maggie Nelson's The Argonauts",
    "name_original": "Maggie Nelson — The Argonauts",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Maggie Nelson（1973-）の『The Argonauts』（2015）。「自伝理論（autotheory）」と呼ばれる新形式の代表作で、クィア家族形成の実体験とJudith Butler、Eve Sedgwick、Roland Barthes、D.W. Winnicottの理論を断章形式で織り合わせる。理論と回想録の境界を消去する。",
    "background": "Eileen Myles、Anne Carsonの伝統と第三波・第四波フェミニズム理論の交差。",
    "development": "Lauren Fournier『Autotheory as Feminist Practice』（2021）で学問的体系化。多くの後続著作（Olivia Laing、Audrey Wollen等）に影響。",
    "historical_context": "クィア・トランス権利運動、ポスト・第二波フェミニズム理論の臨床的応用。",
    "primary_source_url": "https://www.jstor.org/stable/26926770",
    "primary_source_type": "JSTOR — Fournier autotheory",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "トカルチュク『逃亡派』の星座的小説",
    "name_en": "Tokarczuk's Flights",
    "name_original": "Olga Tokarczuk — Bieguni",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Olga Tokarczuk（1962-、2018ノーベル文学賞）の『Bieguni』（2007、英訳『Flights』2017）。116の断章で旅・身体・解剖学・移動を主題化する「星座的novel（constellation novel）」。本人が「ベルナドフスカ・ノヴェル」と呼ぶ非線形構造の代表例。",
    "background": "ポーランド17世紀分派の旅する苦行者から着想。",
    "development": "Booker International賞受賞、英語圏でのポーランド現代文学受容拡大に決定的役割。",
    "historical_context": "EU移動の自由とグローバル流動性の文化的反響。",
    "primary_source_url": "https://www.themillions.com/2018/08/the-cartography-of-the-world-on-olga-tokarczuks-flights.html",
    "primary_source_type": "The Millions — Flights review (2018)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アリ・スミス『季節四部作』のリアルタイム小説",
    "name_en": "Ali Smith's Seasonal Quartet",
    "name_original": "Ali Smith — Seasonal Quartet",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Ali Smith（1962-）の『Autumn』（2016）、『Winter』（2017）、『Spring』（2019）、『Summer』（2020）からなる四部作。Brexit投票直後から執筆出版までの間隔を極端に短縮し、コロナ禍までを「リアルタイム」で記録する実験的方法。Pauline Boty、Charlotte Mew等の女性芸術家を断章で召喚する。",
    "background": "ヴァージニア・ウルフ伝統の継承と21世紀英国政治への直接的応答。",
    "development": "Booker候補（『Autumn』）、英国Brexit文学の代表的成果として確立。",
    "historical_context": "Brexit、難民危機、コロナ禍という連続的危機。",
    "primary_source_url": "https://www.theguardian.com/books/2016/oct/12/autumn-ali-smith-review-brexit-novel",
    "primary_source_type": "Guardian — Autumn review (2016)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ジェニファー・イーガン『ならず者』のネットワーク小説",
    "name_en": "Egan's A Visit from the Goon Squad",
    "name_original": "Jennifer Egan — A Visit from the Goon Squad",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Jennifer Egan（1962-）の『A Visit from the Goon Squad』（2010、ピューリッツァー賞）。13章が時代と人物を飛躍する短編連結novel-in-stories形式で、第12章「Great Rock and Roll Pauses」全体がPowerPointスライド形式という形式実験。続編『The Candy House』（2022）でデジタル記憶共有技術を主題化。",
    "background": "ポストモダン断片化と短編集の境界実験。",
    "development": "novel-in-storiesの21世紀代表作。Tablet/iPad初代と同時期発表で時代精神を体現。",
    "historical_context": "音楽産業デジタル化と都市文化の世代的変容。",
    "primary_source_url": "https://www.nytimes.com/2010/06/27/books/review/Charles-t.html",
    "primary_source_type": "NYT — Goon Squad review (2010)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

# ===============================================================
# CATEGORY C — Contemporary metafiction forms (8)
# ===============================================================

add({
    "name_ja": "ドキュメンタリー・ノヴェル",
    "name_en": "documentary novel (contemporary)",
    "name_original": "documentary novel",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "実在する文書・記録・証言を直接織り込む21世紀小説の形式。Hervé Le Tellier『L'Anomalie』、Laurent Binet『HHhH』、Javier Cercas『Soldados de Salamina』が代表的。ノンフィクション資料の使用と虚構叙述の境界を意図的に崩す。",
    "background": "Truman Capote『冷血』のニュージャーナリズム伝統と、デジタル時代の文書アクセス容易化が交差。",
    "development": "Svetlana Alexievich『チェルノブイリの祈り』など東欧ジャーナリスト作家との交流で発展。",
    "historical_context": "公文書アーカイブのデジタル化、フェイクニュース時代の事実性への希求。",
    "primary_source_url": "https://muse.jhu.edu/article/645895",
    "primary_source_type": "Project MUSE — Documentary Fiction",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ハイブリッド回想録小説",
    "name_en": "hybrid memoir-novel",
    "name_original": "hybrid memoir-novel",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "回想録（memoir）と小説の境界を意図的に消去する21世紀の形式。Sigrid Nunez『The Friend』、Deborah Levy『Living Autobiography』三部作、Annie Ernaux『Les Années』が代表。第一人称が文学的虚構と実体験の中間領域を漂流する。",
    "background": "Annie Ernaux2022年ノーベル賞受賞で国際的注目。",
    "development": "Levy、Nunez、Cuskら英語圏女性作家による継承。",
    "historical_context": "回想録ブームと「真正な声」への希求。",
    "primary_source_url": "https://www.nybooks.com/articles/2018/04/19/sigrid-nunez-friend-novel/",
    "primary_source_type": "NYRB — Nunez The Friend",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "宛先小説（自伝的呼びかけ）",
    "name_en": "autobiographical novel of address",
    "name_original": "autobiographical novel of address",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "「あなた」と呼びかける形式で、実在の他者（亡き親、子、恋人）に語りかける小説形式。Édouard Louis『En finir avec Eddy Bellegueule』、Annie Ernaux『La Place』（先駆）、Ocean Vuong『On Earth We're Briefly Gorgeous』が代表。書簡体小説の現代的再活性化。",
    "background": "Roland Barthes『恋愛のディスクール』の宛先論的影響。",
    "development": "クィア・トランス文学（Vuong、Louis、Carmen Maria Machado）で特に発展。",
    "historical_context": "親密圏暴力・階級移動・性的少数者経験の文学化。",
    "primary_source_url": "https://muse.jhu.edu/article/762089",
    "primary_source_type": "Project MUSE — Address theory",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "二人称ナラティブの再興",
    "name_en": "second-person narrative revival",
    "name_original": "second-person narrative",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Jay McInerney『Bright Lights, Big City』（1984）が80年代に試みた二人称形式が、21世紀に大幅に再興した現象。Mohsin Hamid『The Reluctant Fundamentalist』、『How to Get Filthy Rich in Rising Asia』、Jennifer Egan『Goon Squad』第10章、Tom Robbins作品が代表。読者と語り手の境界を流動化させる装置。",
    "background": "McInerney以来の二人称小説の批評史的議論。",
    "development": "Monika Fludernik、Brian Richardsonら物語論者が体系化。",
    "historical_context": "デジタル没入体験（VR、二人称ゲーム）と並行する読者主体化。",
    "primary_source_url": "https://www.jstor.org/stable/40345516",
    "primary_source_type": "JSTOR — Richardson Unnatural Voices",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "断片小説の成熟",
    "name_en": "fragmentary novel mature",
    "name_original": "fragmentary novel",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "番号付き断章・空白頁・短い章で構成する小説形式の21世紀的成熟。Jenny Offill『Dept. of Speculation』、David Markson後期作、Sarah Manguso『300 Arguments』、Kate Zambreno『Drifts』が代表例。モダニズム断片化を継承しつつ、SNS時代の注意分散を文体化する。",
    "background": "ヴィトゲンシュタイン哲学・Markson『Wittgenstein's Mistress』からの系譜。",
    "development": "Maggie Nelson、Bhanu Kapilを巻き込んだ「断章批評（criticism in fragments）」の流行と並行。",
    "historical_context": "短文SNS時代の認知・文体への影響。",
    "primary_source_url": "https://www.theatlantic.com/magazine/archive/2014/02/the-novelist-who-reinvented-the-mommy-blog/355807/",
    "primary_source_type": "Atlantic — Offill review",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ノヴェル・イン・ストーリーズ",
    "name_en": "novel-in-stories",
    "name_original": "novel-in-stories",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "短編が連結し全体として小説を構成する形式の21世紀的発展。Elizabeth Strout『Olive Kitteridge』（2008）、Jennifer Egan『Goon Squad』、Phil Klay『Redeployment』、Yiyun Li『A Thousand Years of Good Prayers』が代表。Sherwood Anderson『Winesburg, Ohio』伝統の継承。",
    "background": "創作プログラム（MFA）拡大と短編出版経済の影響。",
    "development": "ピューリッツァー賞、National Book Award受賞作が続出し主流ジャンル化。",
    "historical_context": "雑誌経済の縮小と書籍化の経済的論理。",
    "primary_source_url": "https://www.nytimes.com/2008/04/13/books/review/Eder-t.html",
    "primary_source_type": "NYT — Olive Kitteridge review",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "エッセイ・小説ハイブリッド",
    "name_en": "hybrid essay-novel",
    "name_original": "hybrid essay-novel",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "エッセイ（思弁的散文）と虚構叙述の融合形式。Rachel Cusk『Outline』三部作、Teju Cole『Open City』、Ben Lerner作品、Olivia Laing『Crudo』が代表。語り手が美術評論・哲学考察・政治分析を切れ目なく虚構叙述に織り込む。",
    "background": "Sebald、Coetzee後期、Cyngの影響下で21世紀英米で発展。",
    "development": "MFA創作教育で「Cuskian」が様式名として定着。",
    "historical_context": "学術エッセイの一般読者向け展開（New Yorker、LRB の読者圏）。",
    "primary_source_url": "https://www.newyorker.com/magazine/2014/12/22/i-dont-mind-being-here",
    "primary_source_type": "New Yorker — Cusk Outline review",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "リテラリー・ノンフィクション",
    "name_en": "literary nonfiction (contemporary)",
    "name_original": "literary nonfiction",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "21世紀に小説と並ぶ文学的地位を獲得したノンフィクション形式。Helen MacDonald『H is for Hawk』、Maggie Nelson、Hanif Abdurraqib、Patrick Radden Keefe等が代表。事実性の縛りの中で文学的洗練を達成し、Booker・全米図書批評家協会賞などで小説と同等に評価される。",
    "background": "ニュージャーナリズム伝統とエッセイブームの合流。",
    "development": "Kindle Singlesとロングフォーム雑誌（n+1、Granta、The Believer）の経済的支え。",
    "historical_context": "出版経済の変容とエッセイ・回想録ブーム。",
    "primary_source_url": "https://www.theguardian.com/books/2014/aug/02/h-is-for-hawk-helen-macdonald-review",
    "primary_source_type": "Guardian — H is for Hawk review",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

# ===============================================================
# CATEGORY D — Major themes / contemporary issues (8)
# ===============================================================

add({
    "name_ja": "コンテンポラリー・プレカリティ",
    "name_en": "contemporary precarity",
    "name_original": "contemporary precarity",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "雇用・住居・健康保険の不安定性を主題化する21世紀文学傾向。Sally Rooney『Normal People』、Halle Butler『The New Me』、Ling Ma『Severance』が代表。Lauren Berlant『Cruel Optimism』理論を文学化する。労働-家庭分離が崩壊した「常時不安定」状態の物語化。",
    "background": "Judith Butler、Isabell Lorey、Guy Standingらの「プレカリアート」理論の文学的応用。",
    "development": "ミレニアル小説（Rooney、Tony Tulathimutte、Naoise Dolan）で中核主題化。",
    "historical_context": "リーマンショック後の労働市場、ギグエコノミー化。",
    "primary_source_url": "https://www.dukeupress.edu/cruel-optimism",
    "primary_source_type": "Duke UP — Berlant Cruel Optimism",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "プレカリティ人類学",
         "description": "人類学DBのプレカリアート研究との接続。"},
    ],
})

add({
    "name_ja": "監視小説",
    "name_en": "surveillance fiction",
    "name_original": "surveillance fiction",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "デジタル監視社会を主題化する21世紀小説。Dave Eggers『The Circle』、Jennifer Egan『The Candy House』、Olga Ravn『The Employees』、Hari Kunzru『Red Pill』が代表。Snowden事件以降、Foucault『監獄の誕生』、Shoshana Zuboff『監視資本主義』を理論的背景に発展。",
    "background": "Snowden事件（2013）、Cambridge Analytica事件（2018）が文学的衝撃。",
    "development": "ディストピア・サブジャンルから現実主義へと拡張。",
    "historical_context": "GAFA監視資本主義、中国社会信用システムの可視化。",
    "primary_source_url": "https://www.publicaffairsbooks.com/titles/shoshana-zuboff/the-age-of-surveillance-capitalism/",
    "primary_source_type": "Public Affairs — Zuboff Surveillance Capitalism",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "監視下で自己を構成する主体の文学化は、AI追跡・パーソナライゼーションが日常化した時代の主体性問題と直結する。",
         "related_ai_phenomenon": "AI監視・パーソナライゼーション"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "読者-主人公-監視者の三角構造が読者の受容自体を監視に組み込む。",
         "related_ai_phenomenon": "アテンション・キャプチャアルゴリズム"},
    ],
    "cross_domain": [
        {"target_db": "SignalDB", "link_type": "parallel",
         "target_entity_name": "監視資本主義シグナル",
         "description": "Signal DBの監視資本主義シグナルとの接続。"},
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "AI追跡技術",
         "description": "AI開発DBの監視AI技術との並行。"},
    ],
})

add({
    "name_ja": "ポスト真実ナラティブ",
    "name_en": "post-truth narrative",
    "name_original": "post-truth narrative",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "陰謀論・偽情報・代替事実が物語構造そのものを規定する文学傾向。Ben Lerner『The Topeka School』、Hari Kunzru『White Tears』、Patricia Lockwood『No One Is Talking About This』が代表。語り手や読者の認識論的安定を意図的に崩し、真理判定不能な物語空間を構築する。",
    "background": "2016年トランプ当選とBrexit投票が転換点。",
    "development": "Lee McIntyre『Post-Truth』（2018）、Yascha Mounk批評を理論的支柱として発展。",
    "historical_context": "ソーシャルメディア・アルゴリズム的情報環境。",
    "primary_source_url": "https://muse.jhu.edu/article/690987",
    "primary_source_type": "Project MUSE — post-truth narrative",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "MeToo時代の文学",
    "name_en": "MeToo era literature",
    "name_original": "MeToo era literature",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "2017年MeToo運動以降、性暴力・権力勾配・同意問題を中心化する文学傾向。Kate Manne『Down Girl』理論を背景に、Carmen Maria Machado『In the Dream House』、Mary Gaitskill『This Is Pleasure』、Vanessa Springora『Le Consentement』が代表。被害者証言と虚構叙述の倫理的緊張を主題化。",
    "background": "Tarana Burke運動、Harvey Weinstein告発（2017）、文芸界では Junot Díaz、Sherman Alexie告発が転換点。",
    "development": "Roxane Gay編集『Not That Bad』（2018）等のアンソロジーが体系化。",
    "historical_context": "デジタルプラットフォームによる証言の集合化。",
    "primary_source_url": "https://global.oup.com/academic/product/down-girl-9780190933197",
    "primary_source_type": "Oxford UP — Manne Down Girl",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "AI in fiction",
    "name_en": "AI in fiction",
    "name_original": "AI in fiction",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "人工知能を主題・人物・語り手として直接組み込む21世紀小説。Kazuo Ishiguro『Klara and the Sun』、Ian McEwan『Machines Like Me』、Jeanette Winterson『Frankissstein』、Richard Powers『Galatea 2.2』、Ted Chiang短編が代表。LLM登場（2022-）以降は爆発的に増加し、AI語り手・AI共著作品（Sean Michaels等）も登場。",
    "background": "P.K. Dick伝統に加え、Marvin Minsky、Stuart Russellら認知科学の文学的反響。",
    "development": "GPT-3（2020）、ChatGPT（2022）以降、AIをめぐる文学的言説が飛躍的に拡大。",
    "historical_context": "OpenAI・DeepMind等のLLM開発と社会的議論。",
    "primary_source_url": "https://www.newyorker.com/magazine/2021/03/01/can-a-machine-learn-to-write-for-the-new-yorker",
    "primary_source_type": "New Yorker — Klara and the Sun review",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "AIを語り手・登場人物・共同創作者として扱う作品群は、作者性概念そのものを根本的に再構成する。",
         "related_ai_phenomenon": "AI共著・AI語り手・AI作家像"},
        {"axis": "創造性", "status": "rethinking",
         "rationale": "機械の創造性を文学が表象する行為自体が、創造性概念を文学とAI開発の双方向で再定義する。",
         "related_ai_phenomenon": "LLM創造性論争"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "shared_concept",
         "target_entity_name": "文学的AI表象",
         "description": "AI開発DBの文学的AI表象研究と直接共有。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "AI意識論",
         "description": "哲学DBのAI意識論との接続。"},
    ],
})

add({
    "name_ja": "ポストヒューマニズム文学",
    "name_en": "post-humanism in fiction",
    "name_original": "post-humanism in fiction",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "人間中心主義を根本的に問い直す21世紀小説の傾向。Richard Powers『The Overstory』（樹木の時間）、Karen Joy Fowler『We Are All Completely Beside Ourselves』（チンパンジー姉妹）、Charlotte McConaghy『Migrations』、Han Kang作品が代表。Donna Haraway、Rosi Braidotti、Cary Wolfeを理論的支柱とする。",
    "background": "1990年代Donna Haraway『サイボーグ宣言』以降の継承。",
    "development": "気候危機文学、動物権利運動、種を超えた倫理学の文学化と接続。",
    "historical_context": "種絶滅速度の科学的可視化、動物倫理運動。",
    "primary_source_url": "https://upress.umn.edu/book-division/books/what-is-posthumanism",
    "primary_source_type": "U Minnesota — Wolfe What Is Posthumanism",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ポストヒューマニズム",
         "description": "哲学DBのポストヒューマニズム哲学との接続。"},
    ],
})

add({
    "name_ja": "気候緊急事態ナラティブ",
    "name_en": "climate emergency narrative",
    "name_original": "climate emergency narrative",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "cli-fi一般から区別される、急性危機（IPCC「1.5°C特別報告書」2018年以降）に焦点化する具体的ナラティブ形式。Kim Stanley Robinson『The Ministry for the Future』、Maja Lunde『The History of Bees』、Jenny Offill『Weather』、Lydia Millet『A Children's Bible』が代表。10-30年スケールの近未来を扱い、政策・運動・絶望・希望を物語化する。",
    "background": "グレタ・トゥーンベリ運動、Extinction Rebellion運動の文学的反響。",
    "development": "「Solarpunk」「Hopepunk」など希望志向サブジャンルへの分岐。",
    "historical_context": "IPCC報告書、COP会議、気候訴訟の同時進行。",
    "primary_source_url": "https://orbitbooks.net/book/the-ministry-for-the-future/",
    "primary_source_type": "Orbit — Ministry for the Future",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "物語", "status": "partial",
         "rationale": "急性危機を物語化する形式は、物語の閉鎖性（プロット解決）と未解決の現実性の緊張を主題とし、AI生成シナリオプランニングと並走する。",
         "related_ai_phenomenon": "AIによる気候シナリオ生成"},
    ],
    "cross_domain": [
        {"target_db": "SignalDB", "link_type": "parallel",
         "target_entity_name": "気候緊急事態シグナル",
         "description": "Signal DBの気候緊急シグナルとの並行関係。"},
    ],
})

add({
    "name_ja": "難民・移民ナラティブ",
    "name_en": "refugee/migration narrative",
    "name_original": "refugee/migration narrative",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "21世紀の難民・移民経験を主題化する文学傾向。Mohsin Hamid『Exit West』、Viet Thanh Nguyen『The Refugees』、Behrouz Boochani『No Friend But the Mountains』、Dina Nayeri『The Ungrateful Refugee』が代表。Edwidge Danticat、Jhumpa Lahiriのディアスポラ伝統を継承し、同時代難民危機を扱う。",
    "background": "シリア難民危機（2015）、地中海難民死亡、米墨国境分断政策の反響。",
    "development": "難民自身の英語執筆作家（Boochani、Nayeri、Hala Alyan等）の主流化。",
    "historical_context": "EU難民危機、トランプ移民政策、オーストラリアManus島収容所。",
    "primary_source_url": "https://www.nytimes.com/2017/03/10/books/review/exit-west-mohsin-hamid.html",
    "primary_source_type": "NYT — Exit West review",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

# ===============================================================
# CATEGORY E — Form / criticism concepts (8)
# ===============================================================

add({
    "name_ja": "メタモダニズム理論（van den Akker・Vermeulen）",
    "name_en": "metamodernism theory",
    "name_original": "metamodernism theory",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Robin van den Akker と Timotheus Vermeulen が2010年論文と編著『Metamodernism: Historicity, Affect, and Depth After Postmodernism』（2017）で精緻化した文化理論。「振動（oscillation）」「両極（both-ness）」「希望と憂鬱の同居」を中核概念とし、ポストモダンの後継として21世紀文化を理論化する。",
    "background": "ポストモダン理論（Lyotard、Jameson、Hutcheon）の延長線で、その克服を試みる。",
    "development": "Notes on Metamodernism オンライン誌（2010-）が拠点。Luke Turner Metamodernist Manifesto（2011）も参照される。",
    "historical_context": "金融危機後の文化的気分、SNS時代の真摯さの逆説。",
    "primary_source_url": "https://www.rowmaninternational.com/book/metamodernism/3-156-9c5dc25d-fa92-4395-bce4-6c5378e7ad36",
    "primary_source_type": "Rowman & Littlefield — Metamodernism (2017)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ニュー・シンセリティ",
    "name_en": "new sincerity",
    "name_original": "new sincerity",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "David Foster Wallace論文「E Unibus Pluram」（1993）以降、ポストモダンのアイロニーを克服しようとする文学的姿勢の総称。Adam Kelly批評家が「New Sincerity」概念を体系化。Wallace、Dave Eggers、George Saunders、Miranda July、Tao Linらが代表とされる。",
    "background": "Wallace『無限の戯れ』とアイロニー疲労論が出発点。",
    "development": "Adam Kelly『Sincerity in Contemporary US Fiction』（2013）が学問的体系化を達成。",
    "historical_context": "メディアの皮肉化に対する文学的応答。",
    "primary_source_url": "https://www.tandfonline.com/doi/full/10.1080/09502386.2013.821649",
    "primary_source_type": "Cultural Studies — Adam Kelly New Sincerity",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "アイロニーを通り抜けた誠実さの探究は、AI時代における「機械の真摯さ」「人間性のシグナル」問題と深く接続する。",
         "related_ai_phenomenon": "AI生成コンテンツと真摯性の差異化"},
    ],
})

add({
    "name_ja": "現代文学におけるパフォーマティヴィティ",
    "name_en": "performativity in contemporary literature",
    "name_original": "performativity in literature",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Judith Butler のパフォーマティヴィティ理論を21世紀文学批評が再活性化した動向。アイデンティティ・ジェンダー・人種が反復行為で構成されるという観点を、autofiction・autotheory・回想録などの形式読解に適用する。Sianne Ngai、Lauren Berlant、Maggie Nelson等が文学批評と理論を融合させて発展。",
    "background": "Butler『ジェンダー・トラブル』（1990）の理論的延長を21世紀の作家が直接的に参照。",
    "development": "Lauren Fournier『Autotheory as Feminist Practice』（2021）で文学への適用が体系化。",
    "historical_context": "クィア理論の作家自身による文学的実践化。",
    "primary_source_url": "https://muse.jhu.edu/book/82213",
    "primary_source_type": "Project MUSE — Autotheory book",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "サーフェス・リーディング",
    "name_en": "surface reading",
    "name_original": "surface reading",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Stephen Best と Sharon Marcus が2009年Representations誌特集「The Way We Read Now」で提唱した批評方法。Frederic Jameson 由来の「徴候的読解（symptomatic reading）」を批判し、テクストの表面・形式・記述的特徴の精読を擁護する。「深層」を仮定せずテクストの所与に向き合う姿勢。",
    "background": "ポストクリティーク運動（後述critique vs description）の主要構成要素。",
    "development": "Heather Love『The Hermeneutics of Suspicion』批判、Eve Sedgwick weak theory への接続。",
    "historical_context": "脱構築・カルチュラルスタディーズ後の「読み方の疲弊」議論。",
    "primary_source_url": "https://online.ucpress.edu/representations/article/108/1/1/81097",
    "primary_source_type": "Representations — Best & Marcus (2009)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "クリティーク対ディスクリプション",
    "name_en": "critique vs description",
    "name_original": "critique vs description",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Rita Felski『The Limits of Critique』（2015）が体系化した批評方法論争。Paul Ricoeur『Freud and Philosophy』由来の「疑いの解釈学（hermeneutics of suspicion）」がもはや批評の唯一の方法ではないと主張し、記述・愛着・感情的応答を含む多元的批評方法を擁護する動き。",
    "background": "Bruno Latour「批判は終わったか」論文（2004）が前奏。",
    "development": "「ポスト・クリティーク」運動として2010年代の主要批評論争に。",
    "historical_context": "脱構築・カルチュラルスタディーズの教育機関制度化への自己批評。",
    "primary_source_url": "https://press.uchicago.edu/ucp/books/book/chicago/L/bo20827012.html",
    "primary_source_type": "U Chicago Press — Felski Limits of Critique",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ポストクリティーク",
         "description": "哲学DBの解釈学的方法論論争との接続。"},
    ],
})

add({
    "name_ja": "アテンショナル・リーディング",
    "name_en": "attentional reading",
    "name_original": "attentional reading",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "デジタル注意散漫の時代に対する批評的応答として登場した読書実践概念。N. Katherine Hayles『How We Think』（2012）の「ハイパー注意（hyper-attention）」と「深い注意（deep attention）」の対比を出発点とし、批評行為自体を注意の形式として理論化する。Sianne Ngai、Lauren Berlantらが感情批評に接続。",
    "background": "デジタル人文学の発展と並走する読書論の再定式化。",
    "development": "緩慢読み（slow reading）運動、書籍club復権、SNS時代の長文読書論争として展開。",
    "historical_context": "スマートフォン浸透と読書時間減少の文化的危機感。",
    "primary_source_url": "https://press.uchicago.edu/ucp/books/book/chicago/H/bo13744213.html",
    "primary_source_type": "U Chicago Press — Hayles How We Think",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ウィーク・セオリー（Sedgwick）",
    "name_en": "weak theory",
    "name_original": "weak theory",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "ミレニアム転換期",
    "definition": "Eve Kosofsky Sedgwick が論文「Paranoid Reading and Reparative Reading」（2003、『Touching Feeling』所収）で対比した「強い理論（paranoid）」と「弱い理論（reparative）」の枠組みのうち後者。普遍化・敵対化を避け、局所的・修復的・愛着的読解を擁護する。21世紀の方法論論争の主要参照点。",
    "background": "Sylvan Tomkins情動理論、Melanie Klein精神分析を理論的源泉とする。",
    "development": "Best & Marcus サーフェス・リーディング、Heather Love、Felski ポストクリティークに継承。",
    "historical_context": "クィア理論の方法論的内省。",
    "primary_source_url": "https://www.dukeupress.edu/touching-feeling",
    "primary_source_type": "Duke UP — Sedgwick Touching Feeling",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "モレッティ後の遠読（distant reading post-Moretti）",
    "name_en": "distant reading post-Moretti",
    "name_original": "distant reading post-Moretti",
    "original_script": "roman",
    "subfield_code": "lit_eu_postmodern",
    "region": "西欧",
    "period_key": "21世紀現代",
    "definition": "Franco Moretti『Distant Reading』（2013）以降、計算的方法・大規模コーパス・トピックモデリング・ネットワーク分析を文学研究に適用する潮流の発展形。Andrew Piper『Enumerations』、Ted Underwood『Distant Horizons』、Matthew Jockers『Macroanalysis』が代表的成果。MorettiのStanford Literary Lab以後、機械学習・LLMの本格応用段階へ移行している。",
    "background": "Moretti初期遠読への批判（Da Cunha、Bode）を経て方法論的に精緻化された段階。",
    "development": "2020年代はTransformer モデルとLLM ベースの新たな段階に。Cultural Analytics誌が拠点。",
    "historical_context": "デジタル人文学の機関的拡大と批判（Brennan、McKittrick等）。",
    "primary_source_url": "https://www.versobooks.com/books/2421-distant-reading",
    "primary_source_type": "Verso — Moretti Distant Reading",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "数千冊規模の文学コーパス分析は、人間の読書に基づく批評概念を根本的に変容させ、LLM時代に新段階を迎えている。",
         "related_ai_phenomenon": "LLMによる文学コーパス分析"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "LLM文学分析",
         "description": "AI開発DBのLLM応用研究との並行関係。"},
    ],
})


# ---------------------------------------------------------------
# Relations payload
# ---------------------------------------------------------------

RELATIONS: list[tuple[str, str, str, str]] = [
    ("ポスト・ポストモダニズム", "メタモダニズム", "contains",
     "メタモダニズムはポスト・ポストモダニズムの最も体系化された下位カテゴリ。"),
    ("ポスト・ポストモダニズム", "ニュー・シンセリティ", "contains",
     "ニュー・シンセリティはポスト・ポストモダン文化感性の主要表現。"),
    ("メタモダニズム", "メタモダニズム理論（van den Akker・Vermeulen）", "extends",
     "メタモダニズム文化現象は van den Akker・Vermeulen の理論に基づく。"),
    ("ニュー・シンセリティ", "オートフィクション（21世紀版）", "influences",
     "新誠実の感性が autofiction の真摯さ志向を導いている。"),
    ("9/11小説", "監視小説", "influences",
     "9/11後の対テロ戦争・愛国者法体制が監視小説の前提を形成した。"),
    ("クライメート・フィクション（cli-fi）の現代発展", "気候緊急事態ナラティブ", "contains",
     "気候緊急事態ナラティブは cli-fi の最近10年の急性危機特化形態。"),
    ("クライメート・フィクション（cli-fi）の現代発展", "ポストヒューマニズム文学", "influences",
     "気候フィクションが種を超えた視点を要請しポストヒューマニズム文学を促進。"),
    ("オートフィクション（21世紀版）", "ハイブリッド回想録小説", "extends",
     "ハイブリッド回想録小説は autofiction の隣接形式として並走する。"),
    ("オートフィクション（21世紀版）", "クナウスゴール『わが闘争』の極限autofiction", "contains",
     "クナウスゴール『わが闘争』は autofiction の最大規模の極限例。"),
    ("オートフィクション（21世紀版）", "マギー・ネルソン『アルゴノーツ』のハイブリッド批評", "contains",
     "Nelson『The Argonauts』は autofiction を autotheory に拡張した代表例。"),
    ("マギー・ネルソン『アルゴノーツ』のハイブリッド批評", "現代文学におけるパフォーマティヴィティ", "extends",
     "Nelson は Butler パフォーマティヴィティ理論を文学的実践として応用。"),
    ("ポスト・トゥルース・フィクション", "ポスト真実ナラティブ", "extends",
     "ポスト真実ナラティブはジャンル化された post-truth fiction の批評的命名。"),
    ("ポスト・トゥルース・フィクション", "AI in fiction", "influences",
     "AI生成偽情報の登場が post-truth fiction の対象を拡張している。"),
    ("ポスト・インターネット・フィクション", "断片小説の成熟", "influences",
     "オンライン注意散漫の文体化が断片小説の現代形を促進。"),
    ("ゼーバルトの記念碑的フィクション", "ベン・ラーナー『10:04』の予測的フィクション", "influences",
     "Sebald の写真・記憶融合が Lerner の方法に直接影響。"),
    ("ゼーバルトの記念碑的フィクション", "エッセイ・小説ハイブリッド", "influences",
     "Sebald の散文方法がエッセイ・小説ハイブリッドの模範。"),
    ("ボラーニョ『2666』の暴力詩学", "9/11小説", "extends",
     "Bolaño の暴力詩学は post-9/11 小説の国際的拡張形態として読まれる。"),
    ("クナウスゴール『わが闘争』の極限autofiction", "宛先小説（自伝的呼びかけ）", "influences",
     "Knausgård の家族関係に向けた語りが宛先形式を促進した。"),
    ("ベン・ラーナー『10:04』の予測的フィクション", "気候緊急事態ナラティブ", "contains",
     "Lerner『10:04』のハリケーン・サンディ叙述は気候緊急事態ナラティブの初期例。"),
    ("マギー・ネルソン『アルゴノーツ』のハイブリッド批評", "エッセイ・小説ハイブリッド", "extends",
     "Nelson の autotheory はエッセイ・小説ハイブリッドの極限例。"),
    ("トカルチュク『逃亡派』の星座的小説", "断片小説の成熟", "extends",
     "Tokarczuk の星座的構造は断片小説の国際的範例。"),
    ("アリ・スミス『季節四部作』のリアルタイム小説", "ドキュメンタリー・ノヴェル", "influences",
     "Smith のリアルタイム執筆方法がドキュメンタリー・小説境界を再交渉。"),
    ("ジェニファー・イーガン『ならず者』のネットワーク小説", "ノヴェル・イン・ストーリーズ", "extends",
     "Egan『Goon Squad』はnovel-in-storiesの21世紀代表作。"),
    ("ジェニファー・イーガン『ならず者』のネットワーク小説", "監視小説", "influences",
     "Egan『The Candy House』が記憶共有技術を主題化し監視小説と接続。"),
    ("コンテンポラリー・プレカリティ", "MeToo時代の文学", "influences",
     "プレカリティの権力勾配が MeToo 文学の前提条件を共有する。"),
    ("コンテンポラリー・プレカリティ", "ポスト・インターネット・フィクション", "influences",
     "ギグエコノミー下の不安定性がポスト・インターネット小説の主要主題。"),
    ("AI in fiction", "ポストヒューマニズム文学", "extends",
     "AI in fiction はポストヒューマニズム文学の最も顕著な下位ジャンル。"),
    ("AI in fiction", "ニューロ・ノヴェル", "influences",
     "AI意識論が neuro-novel の認知的問題系を継承・拡張する。"),
    ("監視小説", "ポスト・トゥルース・フィクション", "influences",
     "監視資本主義の認識論的歪曲が post-truth fiction の前提を形成。"),
    ("難民・移民ナラティブ", "気候緊急事態ナラティブ", "influences",
     "気候難民の増加が難民ナラティブと気候ナラティブを接続する。"),
    ("メタモダニズム理論（van den Akker・Vermeulen）", "ニュー・シンセリティ", "extends",
     "メタモダニズム理論は new sincerity を「振動」概念で再解釈する。"),
    ("ウィーク・セオリー（Sedgwick）", "サーフェス・リーディング", "influences",
     "Sedgwick の reparative reading が surface reading を準備した。"),
    ("ウィーク・セオリー（Sedgwick）", "クリティーク対ディスクリプション", "influences",
     "Sedgwick の paranoid 批判が Felski post-critique の起点。"),
    ("サーフェス・リーディング", "クリティーク対ディスクリプション", "extends",
     "surface reading は post-critique 運動の方法論的基盤。"),
    ("クリティーク対ディスクリプション", "アテンショナル・リーディング", "influences",
     "post-critique の感情・愛着への着目がアテンショナル批評を導く。"),
    ("モレッティ後の遠読（distant reading post-Moretti）", "AI in fiction", "influences",
     "LLM ベースの遠読がAI in fictionの分析対象を拡張。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[wave10_c12_contemporary] inserting {len(CONCEPTS)} concepts...")
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
                name_ja=name_ja, region="西欧",
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
                try:
                    db.tag_fourth_transform(cid, **axis_entry)
                    fourth_count += 1
                except LitDBError as e:
                    print(f"  [error fourth] {entry['name_ja']} {axis_entry}: {e}")

            for cd in cross_domain:
                try:
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
                except LitDBError as e:
                    print(f"  [error cd] {entry['name_ja']} {cd}: {e}")

        # 3) Insert relations
        for src_name, tgt_name, rtype, desc in RELATIONS:
            sid = name_to_id.get(src_name)
            tid = name_to_id.get(tgt_name)
            if not sid or not tid:
                print(f"  [warn] relation skipped: {src_name!r} -> {tgt_name!r} "
                      f"(sid={sid}, tid={tid})")
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
        sf7_count = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 7"
        ).fetchone()["c"]
        print()
        print("[wave10_c12_contemporary] inserted:")
        print(f"  concepts (total): {summary['concepts']}")
        print(f"  concepts (subfield_id=7): {sf7_count}")
        print(f"  fourth_transform_tags this run: +{fourth_count}")
        print(f"  cross_domain this run: +{cd_count}")
        print(f"  relations this run: +{relation_count}")
        print(f"  source_tier dist: {db.tier_distribution()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
