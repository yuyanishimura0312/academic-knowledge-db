"""
LIT-DB Phase 2 — C01 Pilot: Classical Greek (古典古代ギリシャ)
================================================================
Inserts 50 canonical concepts spanning 5 categories:
  1. Genres / forms (10)
  2. Poetic / rhetorical concepts (10)
  3. Major themes / motifs (10)
  4. Heroic / mythic archetypes (10)
  5. Meta-literary concepts (10)

All entries are sourced from public-domain primary sources (Perseus
Digital Library, Project Gutenberg). source_tier='primary' is reserved
for entries directly traceable to Perseus/Gutenberg PD texts;
'secondary' for those grounded in critical editions widely cited;
'tertiary' for synthetic concept names whose attestation rests on
multiple secondary sources.

Pattern applied: P1 (Canonical Primary Pursuit).
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    # name_ja, name_en, start, end, description
    ("古拙期（アルカイック）", "Archaic Greek", -800, -480,
     "ホメロス・ヘシオドス・抒情詩人の時代。叙事詩と抒情詩の口承伝統が文字化される。"),
    ("古典期（クラシック）", "Classical Greek", -480, -323,
     "ペルシア戦争後のアテネ民主政期。三大悲劇詩人・アリストファネス・歴史家・哲学者の活動期。"),
    ("ヘレニズム期", "Hellenistic Greek", -323, -31,
     "アレクサンドロス没後、アレクサンドリア図書館を中心とする学問・詩学の体系化期。"),
]


# ---------------------------------------------------------------
# Concept payload
# ---------------------------------------------------------------
# Each entry is a dict consumed by db.insert_concept(**entry).
# Additional keys 'fourth_axes' (list of dicts) and 'cross_domain'
# (list of dicts) are popped before insertion and applied afterwards.
# 'period_key' resolves to a period_id at insertion time.

CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY 1 — Genres / forms (10)
# ===============================================================

add({
    "name_ja": "叙事詩",
    "name_en": "epic poetry",
    "name_original": "ἔπος (epos)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "口承の英雄詩を起源とする長編詩形式。ヘクサメター（六脚律）で歌われ、戦争・帰還・神々の介入を題材とする。ホメロス『イリアス』『オデュッセイア』が西洋叙事詩の正典を確立し、後世のラテン詩・ヨーロッパ国民叙事詩の祖型となった。",
    "background": "ミュケナイ文明の崩壊後、口承詩人（aoidoi）が英雄譚を伝承し、前8世紀ごろアルファベット文字化された。",
    "development": "ウェルギリウス『アエネーイス』、ダンテ、ミルトンを経て、近代ではジェイムズ・ジョイス『ユリシーズ』が叙事詩を内面化された都市散文へと変容させた。",
    "historical_context": "ポリス成立期のギリシャ社会の英雄倫理を反映する。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0133",
    "primary_source_type": "Perseus PD edition",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "「ホメロス問題」が示す通り、叙事詩は単一作者性に収斂しない口承共同制作の産物であり、生成AIによる多声的テクスト生成と構造的に類比される。",
         "related_ai_phenomenon": "LLMによる多声的テクスト生成・著者同定問題"},
    ],
})

add({
    "name_ja": "悲劇",
    "name_en": "tragedy",
    "name_original": "τραγῳδία (tragōidia)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "アテネのディオニュソス祭で上演された劇形式で、英雄が運命と性格的欠陥（hamartia）の交錯のなかで破滅へ向かう過程を描く。アリストテレス『詩学』が「真面目で完結した一定の大きさを持つ行為の模倣」と定義した。",
    "background": "前6世紀末、テスピスがディテュランボスから役者を分離し成立。前5世紀のアテネ民主政下で公的祭典演劇となった。",
    "development": "セネカ、シェイクスピア、ラシーヌ、近代ではイプセン・チェーホフへと継承され、現代演劇理論まで影響を与え続ける。",
    "historical_context": "ペルシア戦争後のアテネが市民教育装置として制度化した。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0056",
    "primary_source_type": "Perseus — Aristotle Poetics",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "partial",
         "rationale": "舞台共同体での集合的浄化（catharsis）を前提とする悲劇が、AI生成インタラクティブナラティブの個別最適化された情動誘発と対比される。",
         "related_ai_phenomenon": "AI生成インタラクティブドラマ"},
    ],
})

add({
    "name_ja": "喜劇",
    "name_en": "comedy",
    "name_original": "κωμῳδία (kōmōidia)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "ディオニュソス祭の喜歌（kōmos）から発展した劇形式。低俗・滑稽な人物の行為を模倣し、社会風刺と機知を駆使する。アリストファネスの「古喜劇」、メナンドロスの「新喜劇」に大別される。",
    "background": "アルキロコスの嘲笑詩や祝祭の即興劇が源流。前486年に正式にアテネ大ディオニュソス祭の競演に組み込まれた。",
    "development": "プラウトゥス・テレンティウスのローマ喜劇、コンメディア・デッラルテ、モリエール、現代のシットコムまで連なる。",
    "historical_context": "民主政アテネの公的言論空間における権力風刺の制度化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0027",
    "primary_source_type": "Perseus — Aristophanes",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "対話篇",
    "name_en": "philosophical dialogue",
    "name_original": "διάλογος (dialogos)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "対話形式で哲学的探究を演劇的に再構成する文学ジャンル。プラトンが完成させた形式で、ソクラテス的問答法が論理と人物造形の両面で機能する。文学と哲学のあわいに位置する独自のジャンルを成す。",
    "background": "ソクラテスの口頭問答を弟子たちが書き留めた「ソクラテス伝承」（logoi sōkratikoi）が母胎となった。",
    "development": "キケロ、ルキアノス、ガリレオ、ディドロ、ヴァレリーへと継承され、近代では学問的散文と文学的フィクションの境界を揺るがすジャンルとして再評価される。",
    "historical_context": "アテネの言論文化において対話＝民主的探究の象徴。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0166",
    "primary_source_type": "Perseus — Plato Republic",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "対話篇は複数主体間の問答を通じた知の生成を演じるが、ChatGPT等のAI対話は人間-機械の非対称対話として古典的ダイアロゴスの前提を揺るがす。",
         "related_ai_phenomenon": "LLMチャットインターフェース"},
    ],
})

add({
    "name_ja": "抒情詩",
    "name_en": "lyric poetry",
    "name_original": "μέλος (melos)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "リラ（lyra）の伴奏で歌われる短詩形式の総称。叙事詩の客観的英雄叙述に対し、個人の感情・愛・喪失・祝祭を主観的に詠う。サッポー、アルカイオス、ピンダロスらが主要な担い手となった。",
    "background": "祝祭・酒宴・宗教儀礼で歌われた共同体的歌謡から、前7世紀ごろ個人的声を持つ詩へと変貌した。",
    "development": "カトゥッルス、ホラティウス、ペトラルカ、ロマン派詩、モダニズムの内面詩学へと継承される。",
    "historical_context": "ポリス共同体の祝祭文化と個人の感情表現が緊張関係にあった時期。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0479",
    "primary_source_type": "Perseus — Greek Lyric",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "牧歌",
    "name_en": "pastoral / bucolic",
    "name_original": "βουκολικά (boukolika)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "ヘレニズム期",
    "definition": "羊飼い・牛飼いの理想化された田園生活を描く詩ジャンル。テオクリトスの『牧歌（Idylls）』が祖形を確立し、ウェルギリウス『牧歌』を経てヨーロッパ全土の田園文学伝統を生んだ。",
    "background": "ヘレニズム期アレクサンドリアの都市知識人が、シケリアの民俗歌謡を文学的に再構成した。",
    "development": "ルネサンスのパストラル劇（『アルカディア』『アミンタ』）、英国詩のスペンサー・ミルトン・シェリーへと展開し、近代では反田園詩としての都市文学を生み出す対照軸となる。",
    "historical_context": "都市化したヘレニズム王国の知識人の田園郷愁を反映。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a2008.01.0496",
    "primary_source_type": "Perseus — Theocritus Idylls",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "頌歌",
    "name_en": "ode (epinikion)",
    "name_original": "ἐπινίκιον (epinikion)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "競技勝利者を讃える儀礼的合唱抒情詩。ピンダロスが完成させた形式で、勝者の功績・神話的範例・道徳的教訓を三部構成（ストロペー・アンティストロペー・エポードス）で連結する。",
    "background": "オリンピア・ピューティアなど汎ギリシャ競技祭の勝利祝賀に詠まれた。",
    "development": "ホラティウス、ロンサール、キーツ「ギリシャの壺の頌歌」など近代抒情詩の高踏的形式の祖となった。",
    "historical_context": "貴族的競技文化と都市祝賀儀礼の交差点に位置する。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0162",
    "primary_source_type": "Perseus — Pindar Odes",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "歴史記述",
    "name_en": "historiography",
    "name_original": "ἱστορίη (historiē)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "事件・戦争を体系的調査と語りに基づき記録する散文ジャンル。ヘロドトス『歴史』が「物語的歴史」、トゥキュディデス『戦史』が「批判的歴史」のモデルを確立し、文学と史学の交差点となった。",
    "background": "イオニアの自然哲学的探究心（historiē=探究）を出自に持ち、口承叙事詩からの離陸として成立。",
    "development": "ポリュビオス、リウィウス、タキトゥス、ギボンへと連なり、ヘイドン・ホワイトの「メタヒストリー」論で文学性が再評価された。",
    "historical_context": "ペルシア戦争・ペロポネソス戦争という大事件の集合的記憶化の必要から発展。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0125",
    "primary_source_type": "Perseus — Herodotus Histories",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "ヘロドトス／トゥキュディデスの違いが示す「事実と物語」の境界問題は、AI生成歴史記述・ディープフェイク・合成証言と連続する課題系を形成する。",
         "related_ai_phenomenon": "AI生成史料・合成歴史テクスト"},
    ],
})

add({
    "name_ja": "弁論術（演説文）",
    "name_en": "oratory / rhetorical speech",
    "name_original": "ῥητορική (rhētorikē)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "公的場で説得を目的に構成される散文ジャンル。法廷弁論・政治演説・式典演説の三類型に分類され、デモステネス・イソクラテスが完成形を示し、アリストテレス『弁論術』が理論化した。",
    "background": "ソフィストの修辞教育と民主政アテネの法廷・民会制度が結合して制度化。",
    "development": "キケロを通じてラテン世界へ、ルネサンス人文主義、現代の政治コミュニケーション論まで連続する。",
    "historical_context": "民主政の言論市場という制度的基盤が前提。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0073",
    "primary_source_type": "Perseus — Demosthenes",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "悲喜劇／サテュロス劇",
    "name_en": "satyr play",
    "name_original": "δρᾶμα σατυρικόν (drama satyrikon)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "悲劇三部作のあとに上演された短い喜劇的劇形式。サテュロス（半人半獣の精霊）の合唱団を特徴とし、英雄神話を滑稽化する。エウリピデス『キュクロプス』のみが完全な形で現存する。",
    "background": "ディオニュソス祭の儀礼構造に組み込まれた、悲劇の重圧を解放する装置。",
    "development": "中世のミステリ劇間奏、シェイクスピアのコミック・リリーフ、現代のメタ演劇まで影響が指摘される。",
    "historical_context": "ディオニュソス祭の宗教的・娯楽的両面の調停。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0091",
    "primary_source_type": "Perseus — Euripides Cyclops",
    "importance_score": 2,
    "source_tier": "primary",
    "canonical_in_region": "minor",
})

# ===============================================================
# CATEGORY 2 — Poetic / rhetorical concepts (10)
# ===============================================================

add({
    "name_ja": "ミメーシス（模倣）",
    "name_en": "mimesis",
    "name_original": "μίμησις",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "現実・行為・性格を芸術が模倣・再現する原理。プラトンが理想形相からの二重の隔たりとして批判する一方、アリストテレス『詩学』が人間の自然な認知活動かつ詩の本質と肯定した、西洋詩学の中核概念。",
    "background": "ピュタゴラス派の数的模倣概念、初期哲学の自然と技術の関係論を背景に展開。",
    "development": "ホラティウス『詩論』、ルネサンスの自然模倣論、エーリッヒ・アウエルバッハ『ミメーシス』、ラクー＝ラバルトの解体的読解を経て現代まで議論が続く。",
    "historical_context": "イデア論と自然主義詩学の対立を生んだ思想的舞台。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0056",
    "primary_source_type": "Perseus — Aristotle Poetics",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "「模倣／オリジナリティ」の境界が、訓練データを統計的に模倣する生成AIの出力をどう位置づけるかという問題で再燃している。",
         "related_ai_phenomenon": "生成AIの統計的模倣・スタイル転移"},
        {"axis": "正典", "status": "partial",
         "rationale": "ミメーシスは正典的範例の模倣を芸術教育の核に据えてきたが、AIによる正典スタイル無限再生産が正典性の意味を変質させる。",
         "related_ai_phenomenon": "AIによる古典スタイル模倣"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "mimesis",
         "description": "Poetics DB（PT）でアリストテレスのmimesis概念として登録される中核項目との直接連結。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ミメーシス",
         "description": "プラトン-アリストテレス芸術哲学論争の核として哲学DBにも登録予定の概念。"},
    ],
})

add({
    "name_ja": "カタルシス（浄化）",
    "name_en": "catharsis",
    "name_original": "κάθαρσις",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "アリストテレス『詩学』が悲劇の効用として提示した概念で、憐れみ（eleos）と恐れ（phobos）の感情を喚起しつつそれらを浄化する作用を指す。医学的浄化・宗教的浄化のいずれを基底に置くかで解釈論争が続く。",
    "background": "ピュタゴラス派の音楽療法、ヒポクラテス医学の体液浄化論を含む文化的文脈で形成された。",
    "development": "ルネサンス古典主義、ブレヒトの叙事演劇による批判、フロイト精神分析の昇華概念、現代のメディア感情論まで派生する。",
    "historical_context": "悲劇祭の宗教祭儀的起源と哲学的弁証の交差点。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0056",
    "primary_source_type": "Perseus — Aristotle Poetics",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "悲劇の集合的カタルシスが、AI生成パーソナライズドナラティブによる「個別化された情動消費」へと変質する可能性が論点となる。",
         "related_ai_phenomenon": "AIパーソナライズコンテンツの情動最適化"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "catharsis",
         "description": "Poetics DB（PT）の中核概念として cross-link。"},
    ],
})

add({
    "name_ja": "ヒュブリス（傲慢）",
    "name_en": "hubris",
    "name_original": "ὕβρις",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "神々の領分を侵犯する人間の過剰な自負・暴慢。法的には侮辱的暴力を指したが、悲劇詩学では英雄の没落を導く倫理的・形而上学的越権として中心概念化された。",
    "background": "古代ギリシャの宗教的観念「nemesis（神の報復）」と表裏一体で発達。",
    "development": "シェイクスピア悲劇、ロマン派のプロメテウス受容、現代の技術倫理論（プロメテウス的傲慢）まで再活性化される概念。",
    "historical_context": "ポリス的節度倫理（sophrosyne）への対概念として成立。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0185",
    "primary_source_type": "Perseus — Sophocles",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "partial",
         "rationale": "AI開発における「神の領域への越権」言説（プロメテウス的ヒュブリス）として技術倫理論に直接転用されている。",
         "related_ai_phenomenon": "AGI開発をめぐるプロメテウス的言説"},
    ],
})

add({
    "name_ja": "ハマルティア（過誤）",
    "name_en": "hamartia",
    "name_original": "ἁμαρτία",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "悲劇主人公の没落を引き起こす判断の過ち・性格的欠陥。アリストテレス『詩学』13章が「卓越した人物が悪徳ではなくハマルティアによって不運に陥る」構造を悲劇の最善形態とした。",
    "background": "ホメロス的英雄倫理の延長線上で、悲劇の人間的責任論を支える。",
    "development": "新約聖書の「罪（hamartia）」概念へのキリスト教的転用、近代の「悲劇的欠陥（tragic flaw）」論として継承された。",
    "historical_context": "アテネ法廷文化における意図的悪事と過失の区別意識。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0056",
    "primary_source_type": "Perseus — Aristotle Poetics ch.13",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "hamartia",
         "description": "Poetics DBに登録されるべき悲劇構造の中核要素。"},
    ],
})

add({
    "name_ja": "アナグノーリシス（認知）",
    "name_en": "anagnorisis",
    "name_original": "ἀναγνώρισις",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "登場人物が自身・他者・状況の真相を認知する転換点。アリストテレス『詩学』では悲劇プロットの最良の構成要素として、ペリペテイア（逆転）と同時に発生することが理想とされる。『オイディプス王』が範例。",
    "background": "口承叙事詩の「再認」場面（オデュッセウスの帰還認知等）が理論化された。",
    "development": "ロマンス文学の出生秘密、推理小説の解明、現代の自己認識テーマへと拡張する基本構造として残存する。",
    "historical_context": "アテネ悲劇の倫理的・認識論的仕掛け。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0056",
    "primary_source_type": "Perseus — Aristotle Poetics ch.11",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "anagnorisis",
         "description": "Poetics DBの中核項目との連結。"},
    ],
})

add({
    "name_ja": "ペリペテイア（逆転）",
    "name_en": "peripeteia",
    "name_original": "περιπέτεια",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "プロットにおける状況の急激な逆転。アリストテレスは「行為が反対の方向へ転じること」と定義し、悲劇の感情喚起力を最大化する構造的契機とした。",
    "background": "アテネ悲劇の典型構造（運命の急転）の理論化。",
    "development": "アリストテレス的プロット論を継承するルネサンス劇論、近代物語論（プロップ・ブレモン）まで構造分析の出発点となる。",
    "historical_context": "アテネ的運命観（テュケー）と悲劇詩学の結合。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0056",
    "primary_source_type": "Perseus — Aristotle Poetics ch.11",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "peripeteia",
         "description": "Poetics DBの中核項目との連結。"},
    ],
})

add({
    "name_ja": "エートス／パトス／ロゴス",
    "name_en": "ethos, pathos, logos",
    "name_original": "ἦθος / πάθος / λόγος",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "アリストテレス『弁論術』が提示した説得の三様式。話者の人格的信頼（ethos）、聴衆の感情喚起（pathos）、論理による論証（logos）を統合的に運用することが説得の技術とされる。",
    "background": "ソフィストの説得術を哲学的に再編する試みの帰結。",
    "development": "キケロ修辞論、ペレルマンの新修辞学、現代の議論理論・コミュニケーションデザインに受け継がれる基本枠組み。",
    "historical_context": "民主政アテネにおける説得装置の規範化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0060",
    "primary_source_type": "Perseus — Aristotle Rhetoric",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "AIエージェントが「ethos（人格的信頼）」を擬制的に構築する現象が、古典的説得の倫理的前提を問い直す。",
         "related_ai_phenomenon": "AIエージェントの人格化された説得"},
    ],
})

add({
    "name_ja": "デウス・エクス・マキナ",
    "name_en": "deus ex machina",
    "name_original": "ἀπὸ μηχανῆς θεός (apo mēchanēs theos)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "プロットを解決するために神格を機械装置で舞台に登場させる演出技法。エウリピデスが多用し、アリストテレスは「内在的解決」が望ましいとして批判した。",
    "background": "アテネ劇場のメカネー（クレーン装置）という物理的舞台技術が概念の母体。",
    "development": "近代以降「外的・恣意的解決」の比喩として一般化し、文学批評の標準語彙となった。",
    "historical_context": "アテネ劇場の物理的装置と神話的世界観の交差。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0091",
    "primary_source_type": "Perseus — Euripides",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "コーラス（合唱団）",
    "name_en": "chorus",
    "name_original": "χορός",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "古代ギリシャ劇における集団的歌唱・舞踏の合唱団。劇行為に対する共同体的論評・倫理的解釈を担い、観客と俳優を媒介する第三の声として機能する。",
    "background": "ディオニュソス祭儀のディテュランボス合唱から劇形式が分化した名残。",
    "development": "ブレヒトの叙事演劇、ミュージカルのアンサンブル、現代政治劇のドキュメンタリー合唱として再活性化されている。",
    "historical_context": "ポリス共同体の集合的声の演劇的具現化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0010",
    "primary_source_type": "Perseus — Aeschylus",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ストロペー／アンティストロペー／エポードス",
    "name_en": "strophe / antistrophe / epode",
    "name_original": "στροφή / ἀντιστροφή / ἐπῳδός",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "合唱抒情詩の三部構造。ストロペー（左舞い）に対しアンティストロペー（右舞い）が同形式で応答し、エポードス（後歌）が異形式で締めくくる。ピンダロスの頌歌に典型的に現れる。",
    "background": "祭儀的舞踏の左右対称運動を詩的形式に固定したもの。",
    "development": "近代英語詩のキーツ・グレイの頌歌に踏襲され、形式論的詩学の重要参照点となる。",
    "historical_context": "祭儀的身体運動と詩形式の同形性。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0162",
    "primary_source_type": "Perseus — Pindar",
    "importance_score": 2,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

# ===============================================================
# CATEGORY 3 — Major themes / motifs (10)
# ===============================================================

add({
    "name_ja": "クレオス（不滅の名声）",
    "name_en": "kleos",
    "name_original": "κλέος",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "英雄の死後も歌に詠まれ続ける「不滅の名声」。ホメロス的英雄倫理の中核動機で、アキレウスは長命の凡庸さよりも短命のクレオスを選択する。詩人（aoidos）はクレオスの担い手として権威を持つ。",
    "background": "口承詩文化における記憶＝詩の社会的機能を反映。",
    "development": "ローマ詩のfama、中世騎士道のhonor、近代の作家的不死（immortality through art）へと連続する系譜の起点。",
    "historical_context": "戦士貴族社会における名誉経済（gift-economy of fame）。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0133",
    "primary_source_type": "Perseus — Homer Iliad",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "詩人が英雄のクレオスを保証する古典構造に対し、AI時代は「機械が記憶を担う」非人格的記憶経済へ移行する。",
         "related_ai_phenomenon": "AIアーカイブ・記憶の機械化"},
    ],
})

add({
    "name_ja": "ノストス（帰還）",
    "name_en": "nostos",
    "name_original": "νόστος",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "戦争・冒険ののちの英雄の故郷への帰還を意味する叙事詩的主題。『オデュッセイア』が原型を確立し、帰還の困難・帰還後のアイデンティティ確認・家族との再会を物語の中核に据える。",
    "background": "ミュケナイ崩壊後の集団移動経験が文学化された層を含む。",
    "development": "ウェルギリウス『アエネーイス』、ジョイス『ユリシーズ』、ウォルコット『オメロス』など、世界文学の帰還ナラティブの祖型。「ノスタルジア」の語源。",
    "historical_context": "海洋ポリス世界の遠隔交易・植民活動が文学的経験基盤。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0135",
    "primary_source_type": "Perseus — Homer Odyssey",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "invariant",
         "rationale": "「離郷-冒険-帰還」の三幕構造はAI時代でも物語の基本骨格として持続する不変要素である。",
         "related_ai_phenomenon": "AIストーリージェネレーターの定型構造依存"},
    ],
})

add({
    "name_ja": "クセニアー（客人歓待）",
    "name_en": "xenia",
    "name_original": "ξενία",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "見知らぬ客（xenos）への歓待を神聖な義務とする倫理的-宗教的制度。ゼウスが「客人ゼウス」として保護する。『オデュッセイア』ではxenia違反が物語の善悪判別軸となる。",
    "background": "ポリス間ネットワークが未成熟な時代の貴族間紐帯機能。",
    "development": "ローマのhospitium、中世修道院の客人接遇、近代の「もてなし」倫理（デリダのhospitalité論）まで連続する。",
    "historical_context": "貴族間贈与経済と神々の倫理的監視の結合。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0135",
    "primary_source_type": "Perseus — Homer Odyssey",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "ホスピタリティ／贈与",
         "description": "人類学DBの贈与論・歓待制度との接続点。"},
    ],
})

add({
    "name_ja": "モイラ（運命）",
    "name_en": "moira",
    "name_original": "μοῖρα",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "個々人に「割り当てられた持ち分」を意味する運命概念。ゼウスをも超える非人格的秩序として、悲劇の不可避性を支える。複数化されてモイライ三女神（運命の糸を紡ぐ・測る・断つ）として擬人化される。",
    "background": "ホメロス以前のインド-ヨーロッパ的運命観（ノルン等と類縁）。",
    "development": "ストア派の宿命論、キリスト教の摂理論との交渉を経て、近代悲劇の運命vs自由意志テーマの源泉となる。",
    "historical_context": "口承詩文化の運命論的世界観の言語化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0133",
    "primary_source_type": "Perseus — Homer Iliad",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アゴーン（競合）",
    "name_en": "agon",
    "name_original": "ἀγών",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "競技・競演・論争を包括する競合の場。スポーツ祭典、悲劇祭、法廷弁論まで貫く文化的原理で、ニーチェがギリシャ文化の根本動因として称揚した。劇中ではアゴーン場面が議論の高潮点を成す。",
    "background": "ホメロス的英雄競争（aristeia）の制度化として発展。",
    "development": "ニーチェ「ホメロスの競合心」、ハロルド・ブルームの「影響の不安」（poetic agon）、現代の批評理論まで再帰的に活用される。",
    "historical_context": "貴族文化と民主政の双方を貫く競合主義。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0027",
    "primary_source_type": "Perseus — Aristophanes Frogs",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "フィリア（友愛）",
    "name_en": "philia",
    "name_original": "φιλία",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "愛の三概念（eros, philia, agape）の中で最も社会的紐帯を意味する友愛・親愛。アリストテレス『ニコマコス倫理学』第8-9巻が体系化し、悲劇でも英雄関係（アキレウス-パトロクロス、オレステス-ピュラデス）の核となる。",
    "background": "ポリス的市民紐帯と家族紐帯の双方を支える観念。",
    "development": "キケロ『友情論』、モンテーニュの友情論、現代のケア倫理まで継承される。",
    "historical_context": "民主政アテネの市民共同体倫理の中核。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0054",
    "primary_source_type": "Perseus — Aristotle NE",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ティーモス（気概）",
    "name_en": "thumos / spiritedness",
    "name_original": "θυμός",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "胸中に宿る気概・激情・自己尊厳の感情。ホメロスでは怒り・勇気・決意の発生源とされ、プラトン『国家』では魂の三部分の一つ（理性と欲望の中間）として体系化された。",
    "background": "心身一元論的なホメロス的人間観における主要な内的動因の一つ。",
    "development": "プラトン心理学、ストア派情念論、近代ではフランシス・フクヤマ『歴史の終わり』の「承認欲求」論として再評価。",
    "historical_context": "戦士貴族文化の自己尊厳倫理の心的基盤。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0133",
    "primary_source_type": "Perseus — Homer Iliad",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アレテー（卓越）",
    "name_en": "arete",
    "name_original": "ἀρετή",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "事物・人格が固有の機能を最良に発揮する卓越性・徳。ホメロス的英雄では戦闘的卓越、古典期では市民的・倫理的卓越へと意味を拡張し、アリストテレス徳倫理学の中核となる。",
    "background": "貴族倫理の競合的卓越主義（aristos=最良）と語源を共有する。",
    "development": "ローマのvirtus、中世騎士道、現代の徳倫理学（マッキンタイア、ヌスバウム）に継承される。",
    "historical_context": "戦士貴族から市民倫理への徳概念の変質。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0054",
    "primary_source_type": "Perseus — Aristotle NE",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "エロース（情熱的愛）",
    "name_en": "eros",
    "name_original": "ἔρως",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "対象への欠如に駆動された情熱的・身体的愛。サッポー抒情詩、プラトン『饗宴』『パイドロス』が哲学的に深化させ、欠如を充足へと向かわせる魂の上昇運動として描く。",
    "background": "アルカイック抒情詩の主題から、古典期哲学の心的動力学概念へ昇華。",
    "development": "オウィディウス、トルバドゥール詩、ロマン主義、フロイトのリビドー論まで連続する。",
    "historical_context": "アテネ的pederasty文化と哲学的昇華論の交差。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0174",
    "primary_source_type": "Perseus — Plato Symposium",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ヘマルティア的家系の呪い",
    "name_en": "ancestral curse",
    "name_original": "ἀρά (ara) / curse of the house",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "祖先の罪が世代を越えて子孫に降りかかる呪いの主題。アトレウス家・ラブダコス家（オイディプス-アンティゴネー）の悲劇連作で構造化され、個人責任と家系運命の緊張を中心軸とする。",
    "background": "氏族（genos）単位の倫理的連帯責任観の物語化。",
    "development": "シェイクスピア『マクベス』、フォークナー、ガルシア＝マルケスの一族物語まで「呪われた家系」の祖型として継承される。",
    "historical_context": "前近代的家系責任観と個人化されたポリス市民倫理の緊張。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0010",
    "primary_source_type": "Perseus — Aeschylus Oresteia",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

# ===============================================================
# CATEGORY 4 — Heroic / mythic archetypes (10)
# ===============================================================

add({
    "name_ja": "アキレウス的英雄",
    "name_en": "Achillean hero",
    "name_original": "Ἀχιλλεύς",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "短命だが不滅の名声を選び取る、激情と倫理的純粋さを併せ持つ英雄類型。『イリアス』のアキレウスが原型で、菲怒（mēnis）・友（パトロクロス）の死・自身の必滅性の認知という三契機を構造とする。",
    "background": "ミュケナイ的戦士貴族倫理の極限的形象。",
    "development": "ウェルギリウス・アエネーアスとの対比、シモーヌ・ヴェイユ『イリアス——あるいは力の詩篇』、現代戦争文学に至るまで参照され続ける。",
    "historical_context": "戦士共同体倫理と個人的尊厳要求の悲劇的衝突。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0133",
    "primary_source_type": "Perseus — Homer Iliad",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "オデュッセウス的英雄",
    "name_en": "Odyssean hero",
    "name_original": "Ὀδυσσεύς",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "智略（mētis）と忍耐で困難を乗り越え帰還する英雄類型。アキレウスの直情径行と対極をなし、変装・嘘・忍耐の倫理的曖昧さを引き受ける近代的主体の祖型。",
    "background": "海洋交易世界の知略型人間像が叙事詩化された形象。",
    "development": "ジョイス『ユリシーズ』が現代化したほか、ホルクハイマー＆アドルノ『啓蒙の弁証法』が啓蒙的主体の起源として分析した。",
    "historical_context": "アルカイック期の海洋ポリス世界の智略文化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0135",
    "primary_source_type": "Perseus — Homer Odyssey",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "智略と変装で生き延びるオデュッセウス的主体は、AI時代における「ペルソナの可塑性」「アバター主体性」と構造的に類比される。",
         "related_ai_phenomenon": "AIアバター・デジタルペルソナ"},
    ],
})

add({
    "name_ja": "プロメテウス的反逆者",
    "name_en": "Promethean rebel",
    "name_original": "Προμηθεύς",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "神々から火＝技術と知を盗み人類に与え、罰として永久責苦を負う反逆者像。ヘシオドス『神統記』『労働と日々』、アイスキュロス『縛られたプロメテウス』が古典形を確立した。",
    "background": "ティターン世代と新世代の宇宙論的闘争を背景に置く神話素。",
    "development": "シェリー『鎖を解かれたプロメテウス』、メアリ・シェリー『フランケンシュタイン――現代のプロメテウス』、現代AI言説の「プロメテウス的傲慢」まで再活性化が続く。",
    "historical_context": "技術（technē）への両義的態度（恩恵と侵犯）の神話化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0010",
    "primary_source_type": "Perseus — Aeschylus Prometheus Bound",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "AI開発を「現代のプロメテウス的火盗み」と表象する言説が技術倫理の論争で支配的であり、神話的形象がAI時代に再活性化している。",
         "related_ai_phenomenon": "AGI論争におけるプロメテウス／フランケンシュタイン言説"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "borrowed_from",
         "target_entity_name": "プロメテウス的AI言説",
         "description": "AI開発DBが扱う「現代のプロメテウス」「フランケンシュタイン恐怖」言説の神話的源泉。"},
    ],
})

add({
    "name_ja": "悲劇的英雄（オイディプス型）",
    "name_en": "Oedipal tragic hero",
    "name_original": "Οἰδίπους",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "知ろうとする意志がそのまま破滅へ通じる悲劇的英雄類型。ソフォクレス『オイディプス王』が典型を提示し、認知（anagnorisis）と没落（peripeteia）の同時発生を構造的に体現する。",
    "background": "ラブダコス家の呪い神話を素材に、テーバイ三部作として展開。",
    "development": "アリストテレス詩学の悲劇プロット範例、フロイト精神分析の「エディプス・コンプレックス」、レヴィ＝ストロースの神話分析を経て、近代主体性の根本神話となる。",
    "historical_context": "アテネ古典期の知と運命の哲学的問題化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0191",
    "primary_source_type": "Perseus — Sophocles Oedipus Rex",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "嘆きの女性（カッサンドラ／アンティゴネー）",
    "name_en": "lamenting heroine",
    "name_original": "Κασσάνδρα / Ἀντιγόνη",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "公的権力に対し家族の絆・宗教的義務・予知を盾に抗議する女性英雄類型。アンティゴネーは国法と神律の対立を、カッサンドラは聞き入れられない真理の予言者性を体現する。",
    "background": "ホメロス女性嘆きの伝統と悲劇祭の女性役割再構築の交差点。",
    "development": "ヘーゲル『精神現象学』のアンティゴネー解釈、現代フェミニズム批評（バトラー『アンティゴネーの主張』）、政治的抵抗のシンボルとして再活性化。",
    "historical_context": "アテネ的男性中心政治と女性の儀礼的役割の緊張。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0185",
    "primary_source_type": "Perseus — Sophocles Antigone",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "復讐する女性（メーディア／クリュタイメストラ）",
    "name_en": "vengeful woman",
    "name_original": "Μήδεια / Κλυταιμνήστρα",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "夫の裏切り・娘の犠牲に対し家族秩序を超える形で復讐を遂げる女性類型。エウリピデス『メーディア』、アイスキュロス『アガメムノーン』が原型で、ジェンダー秩序の暴力的反転を演じる。",
    "background": "アテネ家父長制の不安と異邦女性恐怖の劇的形象化。",
    "development": "セネカ『メーディア』、ハイナー・ミュラーの再書、フェミニズム批評の中心題目として現代まで再演される。",
    "historical_context": "アテネ家父長制の構造的不安。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0113",
    "primary_source_type": "Perseus — Euripides Medea",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "賢者王／哲人王",
    "name_en": "philosopher-king",
    "name_original": "βασιλεὺς φιλόσοφος (basileus philosophos)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "哲学的真理認識と政治的統治を統合する理想的支配者像。プラトン『国家』第5-7巻が定式化し、文学的にも理想統治者の祖型として後世に強い影響を及ぼした。",
    "background": "ソクラテス処刑後のプラトンによる政治哲学的応答。",
    "development": "ローマ皇帝マルクス・アウレリウスの自己提示、ルネサンス君主論、近代テクノクラート論まで間接的に影響。",
    "historical_context": "民主政の失敗と知識統治への憧憬。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0166",
    "primary_source_type": "Perseus — Plato Republic",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "MG", "link_type": "borrowed_from",
         "target_entity_name": "哲人王",
         "description": "経営学DBの理想的リーダー論との接続。"},
    ],
})

add({
    "name_ja": "詩人＝予言者（vates型）",
    "name_en": "poet-prophet",
    "name_original": "ἀοιδός / μάντις (aoidos / mantis)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "ムーサイの霊感を受け真理を歌う詩人と神託を語る予言者を結ぶ詩人形象。ホメロス・ヘシオドスが詩人の権威の源泉として神的霊感を主張し、プラトン『イオン』が批判的に検討した。",
    "background": "口承詩文化の詩人＝記憶の番人としての宗教的位置づけ。",
    "development": "ローマのvates、中世のbard、ロマン派の「予言者詩人」（シェリー、ホイットマン）に直接連続する。",
    "historical_context": "口承詩文化の宗教的権威構造。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0124",
    "primary_source_type": "Perseus — Hesiod Theogony proem",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "知略のトリックスター（ヘルメース／オデュッセウス）",
    "name_en": "trickster figure",
    "name_original": "Ἑρμῆς (Hermes)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "境界・移動・盗み・嘘を司る神格／英雄類型。ヘルメースは生まれ落ちた直後にアポロンの牛を盗む「ホメロス讃歌・ヘルメース讃歌」で原型を示し、知略的英雄オデュッセウスと類縁関係にある。",
    "background": "境界神の人格化が文学的キャラクターとして発展した形象。",
    "development": "ローマのメルクリウス、近世ピカレスク小説、現代のアンチヒーローまで連続する系譜の起点。",
    "historical_context": "境界・交易・盗みを倫理的両義性のなかで肯定する古代社会の心性。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0137",
    "primary_source_type": "Perseus — Homeric Hymn to Hermes",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "怪物的他者（キュクロプス／メドゥーサ）",
    "name_en": "monstrous Other",
    "name_original": "Κύκλωψ / Μέδουσα",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "ポリス的人間性の境界外に置かれる怪物形象。キュクロプスは家父長的自給自足の野蛮、メドゥーサは女性的他者性の極限を象徴し、英雄の確認的他者として機能する。",
    "background": "ポリス＝人間性／非ポリス＝非人間という二分法の神話化。",
    "development": "中世の異界譚、エキゾティシズム、現代のクィア・モンスター理論（ハラウェイ、コーエン）に連続する。",
    "historical_context": "植民・交易における異邦人遭遇の神話的処理。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0135",
    "primary_source_type": "Perseus — Homer Odyssey Bk 9",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

# ===============================================================
# CATEGORY 5 — Meta-literary concepts (10)
# ===============================================================

add({
    "name_ja": "ムーサイの霊感",
    "name_en": "Muses' inspiration",
    "name_original": "Μοῦσαι",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "ムーサ女神たちが詩人に詩・記憶・真理を授ける制度的詩学。叙事詩・抒情詩は冒頭でムーサに呼びかけることで、詩人を「神的霊感の媒体」として位置づける枠組みを示す。",
    "background": "口承詩人の記憶能力の神格化。記憶（ムネーモシュネー）がムーサの母とされる。",
    "development": "プラトン『イオン』『パイドロス』の「神的狂気」論、ロマン派のジニアス論、現代のクリエイティビティ研究まで続く。",
    "historical_context": "口承詩文化の権威付け装置。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0124",
    "primary_source_type": "Perseus — Hesiod Theogony",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "詩人を「外部からの霊感の受容器」とする古典的詩学は、AIを「外部からの言語生成装置」として捉える現代的状況と構造的に類比され、創造性の所在を再考させる。",
         "related_ai_phenomenon": "生成AIを「現代のムーサ」と捉える言説"},
        {"axis": "作者性", "status": "rethinking",
         "rationale": "霊感詩学は単一作者性に解消されない「詩人＋神」の共同制作を前提としており、人間＋AI共同制作の先例として再読される。",
         "related_ai_phenomenon": "Human-AI共同執筆"},
    ],
})

add({
    "name_ja": "口承伝承（オーラル・トラディション）",
    "name_en": "oral tradition",
    "name_original": "προφορικὴ παράδοσις",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古拙期（アルカイック）",
    "definition": "文字以前の口頭による詩・神話・歴史伝承の体系。パリー＝ロード仮説が示したように、定型句（formula）と類型場面（type-scene）の組み合わせによって即興的に詩を生成する詩学を備える。",
    "background": "ミュケナイ崩壊後の文字喪失期から前8世紀ごろの再文字化までの時代の詩生成技術。",
    "development": "ミルマン・パリーの実証研究（南スラヴ叙事詩との比較）、現代のデジタル人文学・AI生成詩との比較研究へ展開。",
    "historical_context": "前文字社会から文字社会への移行期の詩学。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0133",
    "primary_source_type": "Perseus — Homer (Parry-Lord formula analysis)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "口承伝承の定型句結合型生成は、LLMの確率的トークン生成と構造的に類比され、「作者なき言語生成」の最古の事例として再読される。",
         "related_ai_phenomenon": "LLMの確率的言語生成"},
        {"axis": "言語", "status": "rethinking",
         "rationale": "口承詩の集合的・流動的言語使用が、AI時代の集団的言語生成と通底する。",
         "related_ai_phenomenon": "AIによる集合的言語生成"},
    ],
})

add({
    "name_ja": "詩人間アゴーン",
    "name_en": "agon between poets",
    "name_original": "ἀγὼν ποιητῶν",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "詩人同士が公的場で技を競う制度的競演。ヘシオドス『労働と日々』が「ホメロスとの詩合戦」伝説を語り、アリストファネス『蛙』ではアイスキュロスとエウリピデスがハーデスで詩劇の優劣を争う。",
    "background": "祭典競演（agōn）の制度的中核としての詩人競演。",
    "development": "ハロルド・ブルーム『影響の不安』として理論化され、詩史を世代間アゴーンとして読む方法論を確立した。",
    "historical_context": "祭典文化と詩史の制度的結合。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0032",
    "primary_source_type": "Perseus — Aristophanes Frogs",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "正典（カノン）形成",
    "name_en": "canon formation",
    "name_original": "κανών",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "ヘレニズム期",
    "definition": "アレクサンドリア図書館の文献学者たち（アリスタルコス、アリストファネス・ビザンティオス）が古典作家を選別・序列化した制度的営為。後世の「古典」概念の起源で、保存・教育・批判校訂の三機能を統合する。",
    "background": "ヘレニズム期の膨大な文献蓄積に対する選別・整理の必要。",
    "development": "ローマ期のラテン正典、中世写本伝承、近代国民文学正典、現代のポストコロニアル正典批判まで連続する。",
    "historical_context": "ヘレニズム期の図書館制度と文献学の確立。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a2008.01.0540",
    "primary_source_type": "Perseus — Alexandrian scholia tradition",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "AI時代の「全テクスト等価アクセス」がアレクサンドリア以来の正典形成原理（選別・序列）の前提を揺るがす。",
         "related_ai_phenomenon": "LLM訓練コーパスにおける正典／周縁の平準化"},
    ],
})

add({
    "name_ja": "祭典上演（劇場性）",
    "name_en": "festival performance / theatricality",
    "name_original": "θέατρον (theatron)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "ディオニュソス祭の競演として制度化された劇場文化。詩テクストと身体・音楽・空間が統合された総合芸術であり、「テクストとしての文学」と「上演としての文学」の両義性の起源を成す。",
    "background": "宗教祭儀から劇形式への発展。",
    "development": "中世受難劇、能、グランド・オペラ、現代のパフォーマンス・スタディーズ（シェクナー）まで「上演性」概念を支える。",
    "historical_context": "アテネ民主政の市民教育＝祭典文化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0010",
    "primary_source_type": "Perseus — Aeschylus performances",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アレゴリー的解釈",
    "name_en": "allegorical interpretation",
    "name_original": "ἀλληγορία",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "ホメロス・ヘシオドスの神話的字義を哲学的・道徳的真理の比喩として読む解釈技法。テオゲネス・メトロドロス・ストア派が体系化し、後の聖書解釈・中世寓意詩に決定的影響を与えた。",
    "background": "プラトンの詩人追放論への反駁としての神話救済戦略。",
    "development": "フィロン・オリゲネスの聖書四重解釈、中世寓意詩、現代の比喩理論（ポール・ド・マン）まで連続する。",
    "historical_context": "詩と哲学の対立に対する解釈学的調停。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0179",
    "primary_source_type": "Perseus — Plato Republic Bk 2",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "アレゴレーシス",
         "description": "哲学的解釈学の起源として哲学DBと共有。"},
    ],
})

add({
    "name_ja": "テクネー／詩の技法",
    "name_en": "techne (poetic craft)",
    "name_original": "τέχνη",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "詩作・修辞・建築等を貫く「学習可能な技術知」。ピンダロスの「天賦の才（physis）」と対照を成し、アリストテレス『詩学』が詩を体系的technēとして記述しうる対象として確立した。",
    "background": "前5-4世紀のソフィスト的technē論（弁論術・詩作術）の隆盛。",
    "development": "ホラティウス『詩論』、ルネサンスの詩学論、現代の創作技法書まで連続する「技法としての文学」観の起源。",
    "historical_context": "天才主義／技術主義の対立の古代的起源。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0056",
    "primary_source_type": "Perseus — Aristotle Poetics",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "「technēとしての詩」は学習可能性を強調し、AIの統計的学習による詩的生成と構造的に親和する。逆にロマン派的天才論は対立軸として浮上する。",
         "related_ai_phenomenon": "AIによる詩的技法の学習・再生産"},
    ],
})

add({
    "name_ja": "詩と哲学の古い争い",
    "name_en": "ancient quarrel between poetry and philosophy",
    "name_original": "παλαιὰ διαφορὰ φιλοσοφίᾳ τε καὶ ποιητικῇ",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "プラトン『国家』第10巻が言及する詩と哲学の根本的対立。詩の感情喚起力と哲学の真理探究を緊張関係に置き、西洋詩学・哲学双方の自己定義の起点となった主題。",
    "background": "ソクラテス処刑後のプラトンによる詩人追放論として現れた。",
    "development": "アリストテレス詩学の擁護、ロマン派の詩優位論、ハイデガー後期の詩と思考、現代の文学哲学論争まで一貫して参照される。",
    "historical_context": "アテネ古典期の知のヘゲモニー争い。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0166",
    "primary_source_type": "Perseus — Plato Republic Bk 10",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "詩と哲学の争い",
         "description": "哲学DBの根本主題との直接共有概念。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "詩と哲学の関係",
         "description": "Poetics DBの中核論点。"},
    ],
})

add({
    "name_ja": "プロソポポイア（人格付与・代弁）",
    "name_en": "prosopopoeia",
    "name_original": "προσωποποιία",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "ヘレニズム期",
    "definition": "不在者・死者・抽象概念・無生物に声と人格を付与し代弁させる修辞技法。ヘレニズム期の修辞学校で訓練科目（progymnasmata）として制度化され、文学・哲学・修辞を貫く基盤的技法となった。",
    "background": "弁論教育の体系化過程で技法として独立。",
    "development": "ローマ修辞学、中世のアレゴリー文学、ポール・ド・マンの自伝論、現代のヴォイス理論まで継続する。",
    "historical_context": "ヘレニズム期の修辞学教育制度。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0060",
    "primary_source_type": "Perseus — Aristotle Rhetoric",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "AIが歴史人物・架空人物に「声」を与える現象（生成AIアバター、死者復活コンテンツ）はプロソポポイアの極限化として古典修辞学と直結する。",
         "related_ai_phenomenon": "生成AIによる死者・歴史人物の声の合成"},
    ],
})

add({
    "name_ja": "エクフラシス（描写描写）",
    "name_en": "ekphrasis",
    "name_original": "ἔκφρασις",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "古典期（クラシック）",
    "definition": "視覚芸術作品を言語で生き生きと描写する修辞技法。『イリアス』第18巻のアキレウスの楯描写が古典範例で、後にヘレニズム期に独立ジャンル（fillostratus『絵画について』）として発展した。",
    "background": "口承詩文化の視覚的喚起力（enargeia）の理論化。",
    "development": "ウェルギリウス、キーツ「ギリシャの壺の頌歌」、レッシング『ラオコオン』、現代のイメージ＆テクスト論（W・J・T・ミッチェル）まで連続する。",
    "historical_context": "視覚と言語の関係の古代的問題化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0133",
    "primary_source_type": "Perseus — Homer Iliad Bk 18 (Shield of Achilles)",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "視覚から言語への古典的「翻訳」技法は、マルチモーダルAIによる画像→テキスト変換と構造的に直結し、エクフラシスの再活性化が起きている。",
         "related_ai_phenomenon": "マルチモーダルAIの画像キャプション生成"},
    ],
})


# ---------------------------------------------------------------
# Relations payload (sequential after concepts inserted)
# ---------------------------------------------------------------
# Each tuple: (source_name_ja, target_name_ja, relation_type, description)
RELATIONS: list[tuple[str, str, str, str]] = [
    ("叙事詩", "ノストス（帰還）", "contains",
     "『オデュッセイア』に代表される叙事詩はノストス（帰還）主題を中心構造として含む。"),
    ("叙事詩", "クレオス（不滅の名声）", "contains",
     "『イリアス』に代表される叙事詩はクレオス（不滅の名声）主題を駆動原理とする。"),
    ("叙事詩", "口承伝承（オーラル・トラディション）", "extends",
     "叙事詩は口承伝承の定型句生成詩学から書記叙事詩へと延長された形式。"),
    ("悲劇", "カタルシス（浄化）", "contains",
     "アリストテレスは悲劇の機能をカタルシスとして定義した。"),
    ("悲劇", "ハマルティア（過誤）", "contains",
     "悲劇の構造はハマルティアによる英雄の没落を中核とする。"),
    ("悲劇", "アナグノーリシス（認知）", "contains",
     "悲劇プロットはアナグノーリシスを最良の構成要素として含む。"),
    ("悲劇", "ペリペテイア（逆転）", "contains",
     "悲劇プロットはペリペテイアを最良の構成要素として含む。"),
    ("悲劇", "コーラス（合唱団）", "contains",
     "古代ギリシャ悲劇はコーラスを構造要素として含む。"),
    ("悲劇", "ヒュブリス（傲慢）", "contains",
     "悲劇英雄の没落はしばしばヒュブリスによって動機づけられる。"),
    ("対話篇", "詩と哲学の古い争い", "extends",
     "プラトン対話篇は詩と哲学の古い争いを内部化し、新たな知の文学形式として詩を批判的に取り込む。"),
    ("抒情詩", "エロース（情熱的愛）", "contains",
     "サッポーら抒情詩人はエロースを中核主題として詠った。"),
    ("頌歌", "ストロペー／アンティストロペー／エポードス", "contains",
     "頌歌は三部構造（ストロペー／アンティストロペー／エポードス）を形式とする。"),
    ("ミメーシス（模倣）", "カタルシス（浄化）", "influences",
     "アリストテレス詩学において、ミメーシスがカタルシスを成立させる前提構造となる。"),
    ("ミメーシス（模倣）", "詩と哲学の古い争い", "extends",
     "プラトン-アリストテレスの対立はミメーシス概念をめぐる詩と哲学の争いとして展開した。"),
    ("ハマルティア（過誤）", "ペリペテイア（逆転）", "influences",
     "ハマルティアが状況の逆転（ペリペテイア）を引き起こす因果連関を成す。"),
    ("ペリペテイア（逆転）", "アナグノーリシス（認知）", "influences",
     "アリストテレスは逆転と認知の同時発生を最良のプロットとした。"),
    ("ヒュブリス（傲慢）", "ハマルティア（過誤）", "influences",
     "ヒュブリス的越権がハマルティアの典型形態となる。"),
    ("クレオス（不滅の名声）", "アキレウス的英雄", "contains",
     "アキレウスの選択（短命×不滅の名声）はクレオス概念の極限的形象化。"),
    ("ノストス（帰還）", "オデュッセウス的英雄", "contains",
     "オデュッセウスはノストス主題を体現する英雄類型。"),
    ("クセニアー（客人歓待）", "オデュッセウス的英雄", "influences",
     "『オデュッセイア』のクセニアー違反／遵守が英雄の善悪判別軸を構成する。"),
    ("モイラ（運命）", "悲劇的英雄（オイディプス型）", "influences",
     "モイラの不可避性がオイディプス的悲劇英雄の存在条件を成す。"),
    ("アゴーン（競合）", "詩人間アゴーン", "extends",
     "詩人間アゴーンは祭典文化の競合原理（アゴーン）の制度的特殊化。"),
    ("アレテー（卓越）", "アキレウス的英雄", "contains",
     "ホメロス的英雄倫理におけるアレテーは戦闘的卓越として体現される。"),
    ("プロメテウス的反逆者", "ヒュブリス（傲慢）", "extends",
     "プロメテウスのヒュブリスは技術知（technē）への両義的態度の神話化。"),
    ("怪物的他者（キュクロプス／メドゥーサ）", "クセニアー（客人歓待）", "criticizes",
     "キュクロプスのクセニアー違反は人間性の境界画定装置として機能する。"),
    ("詩人＝予言者（vates型）", "ムーサイの霊感", "extends",
     "詩人＝予言者像はムーサイの霊感を媒介する詩学的権威の人格化。"),
    ("ムーサイの霊感", "口承伝承（オーラル・トラディション）", "extends",
     "ムーサイ呼びかけは口承詩生成の詩学的儀礼を制度化したもの。"),
    ("正典（カノン）形成", "ミメーシス（模倣）", "influences",
     "正典形成は範例模倣（ミメーシス）の教育論を制度化する。"),
    ("詩と哲学の古い争い", "アレゴリー的解釈", "influences",
     "アレゴリー的解釈は詩と哲学の対立に対する解釈学的調停として現れた。"),
    ("テクネー／詩の技法", "ミメーシス（模倣）", "extends",
     "詩のtechnē論はミメーシスの技術的体系化として機能する。"),
    ("エクフラシス（描写描写）", "ミメーシス（模倣）", "extends",
     "エクフラシスは視覚芸術のミメーシスを言語で再ミメーシスする入れ子構造。"),
    ("プロソポポイア（人格付与・代弁）", "ムーサイの霊感", "extends",
     "プロソポポイアは詩人が他者の声を代弁する技法で、霊感詩学の修辞的継承形態。"),
    ("頌歌", "アゴーン（競合）", "contains",
     "頌歌（エピニキオン）は競技勝利を祝う詩で、アゴーン文化を直接前提とする。"),
    ("弁論術（演説文）", "エートス／パトス／ロゴス", "contains",
     "弁論術はエートス／パトス／ロゴスの三様式を体系として含む。"),
    ("歴史記述", "弁論術（演説文）", "influences",
     "トゥキュディデス『戦史』は劇中演説の構成において弁論術と相互作用する。"),
    ("悲劇", "嘆きの女性（カッサンドラ／アンティゴネー）", "contains",
     "悲劇は嘆きの女性類型を主要キャラクター類型として含む。"),
    ("悲劇", "復讐する女性（メーディア／クリュタイメストラ）", "contains",
     "悲劇は復讐する女性類型を主要キャラクター類型として含む。"),
    ("対話篇", "賢者王／哲人王", "contains",
     "プラトン『国家』対話篇は哲人王の理想を主題化する。"),
    ("デウス・エクス・マキナ", "悲劇", "criticizes",
     "アリストテレスはデウス・エクス・マキナを悲劇プロットの劣位的解決として批判した。"),
    ("悲喜劇／サテュロス劇", "悲劇", "extends",
     "サテュロス劇は悲劇三部作の儀礼的解放装置として悲劇形式に付随する。"),
    ("ヘマルティア的家系の呪い", "悲劇的英雄（オイディプス型）", "contains",
     "オイディプス悲劇はラブダコス家の家系呪いを構造的前提とする。"),
    ("知略のトリックスター（ヘルメース／オデュッセウス）", "オデュッセウス的英雄", "extends",
     "オデュッセウス的英雄はトリックスター類型の英雄叙事詩的特殊化。"),
    ("ティーモス（気概）", "アキレウス的英雄", "contains",
     "アキレウスの怒り（mēnis）はティーモス概念の典型的発現。"),
    ("フィリア（友愛）", "アキレウス的英雄", "contains",
     "アキレウスとパトロクロスのフィリアが『イリアス』後半の動因となる。"),
    ("牧歌", "抒情詩", "extends",
     "牧歌はヘレニズム期に抒情詩・叙事詩の要素を再編成した派生ジャンル。"),
    ("祭典上演（劇場性）", "悲劇", "contains",
     "悲劇は祭典上演の制度的中核ジャンル。"),
    ("祭典上演（劇場性）", "喜劇", "contains",
     "喜劇は祭典上演の制度的中核ジャンル。"),
    ("コーラス（合唱団）", "祭典上演（劇場性）", "extends",
     "コーラスは祭典上演における共同体的声の演劇的具現化。"),
    ("叙事詩", "詩人＝予言者（vates型）", "contains",
     "叙事詩は詩人＝予言者像を冒頭のムーサ呼びかけで自己定義する。"),
    ("プロメテウス的反逆者", "テクネー／詩の技法", "influences",
     "プロメテウスがもたらした火＝技術知が技術一般（technē）の文化的位置づけを規定する。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[pilot_c01_greek] inserting {len(CONCEPTS)} concepts...")
    if len(CONCEPTS) != 50:
        print(f"  WARNING: expected 50 concepts, got {len(CONCEPTS)}")

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
            entry = dict(raw)  # shallow copy so we can pop
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
        print("[pilot_c01_greek] inserted:")
        print(f"  concepts: {summary['concepts']}")
        print(f"  fourth_transform_tags: {summary['fourth_transform_tags']} "
              f"(this run: +{fourth_count})")
        print(f"  cross_domain: {summary['cross_domain']} "
              f"(this run: +{cd_count})")
        print(f"  relations: {summary['relations']} "
              f"(this run: +{relation_count})")
        print(f"  source_tier dist: {db.tier_distribution()}")
        print(f"  fourth_transform dist:")
        for r in db.fourth_transform_distribution():
            print(f"    {r}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
