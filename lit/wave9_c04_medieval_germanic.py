"""
LIT-DB Phase 2 — C04: Medieval Germanic & British Isles Literature
=====================================================================
Inserts 40 canonical concepts spanning 5 categories:
  A. Old English (8)
  B. Middle English (8)
  C. Old Norse / Icelandic / Skaldic (8)
  D. Middle High German / Old German (8)
  E. Major poetics & forms (8)

Subfield: lit_eu_medieval (subfield_id=2), region=西欧.
This file covers the Germanic & British Isles medieval canon.
Zero overlap with C03 (Romance: French/Italian/Iberian medieval).

Primary sources:
  - Bibliotheca Augustana (Old/Middle High German, Old Norse)
  - TEAMS Middle English Texts (https://d.lib.rochester.edu/teams)
  - Internet Archive (Beowulf manuscript / Heimskringla / Eddas)
  - Project Gutenberg (Malory, Chaucer, sagas in PD translation)
  - Heimskringla.no (Old Norse canonical edition)

Pattern: P1 (Canonical Primary Pursuit) + P2 (Form-poetics chains).
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (Germanic + British Isles medieval)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    # name_ja, name_en, start, end, description
    ("古英語期", "Old English Period", 700, 1100,
     "アングロ・サクソン期。叙事詩『ベオウルフ』、エレジー、"
     "ベーダの教会史、アングロ・サクソン年代記の時代。"
     "頭韻詩（alliterative verse）が中核形式。"),
    ("中英語期", "Middle English Period", 1100, 1500,
     "ノルマン征服後から印刷術導入直前まで。チョーサー、"
     "ガウェイン詩人、ラングランド、神秘主義者（マージェリー・"
     "ケンプ、ノリッジのジュリアン）、マロリーが活動。"),
    ("古ノルド期", "Old Norse / Saga Age", 800, 1300,
     "ヴァイキング時代から13世紀までのアイスランド・ノルウェー。"
     "エッダ詩、スカルド詩、家族サガが書写された写本文化期。"),
    ("中高ドイツ期", "Middle High German Period", 1050, 1350,
     "宮廷文学黄金期。『ニーベルンゲンの歌』、ヴォルフラム、"
     "ゴットフリート、ヴァルター・フォン・デア・フォーゲルヴァイデが活動。"
     "ミンネザング（宮廷恋愛抒情詩）が興隆。"),
    ("中世末期ゲルマン圏", "Late Medieval Germanic", 1300, 1500,
     "マイスタージンガー成立、ドイツ語都市の聖史劇興隆、"
     "獣譚（Reynard）の各国語版流布、寓話文学定着の時代。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — Old English (8)
# ===============================================================

add({
    "name_ja": "ベオウルフ",
    "name_en": "Beowulf",
    "name_original": "Bēowulf",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古英語期",
    "definition": "8-11世紀に成立したと推定される古英語頭韻詩の長編英雄叙事詩。"
                  "全3,182行。スウェーデンのギート族の英雄ベオウルフが、デンマーク王フローズガールの"
                  "館を襲う怪物グレンデル、その母、そして晩年に故郷で龍を退治して死ぬまでを描く。"
                  "唯一の写本（ノウェル写本、大英図書館Cotton Vitellius A.xv）に現存。",
    "background": "ゲルマン諸部族の口承英雄詩がキリスト教化された写本文化のなかで定着した稀少例。"
                  "詩人は無名で、北欧・大陸の伝承を熟知したアングロ・サクソンの聖職者と推定される。",
    "development": "1815年Thorkelin初版、19世紀以降の文献学的整備、"
                   "1936年トールキン論文「Beowulf: The Monsters and the Critics」が現代批評の起点。"
                   "シェイマス・ヒーニーの2000年新訳、ザメツキスの映画化（2007）等で大衆化。",
    "historical_context": "ヴァイキング侵攻期の英国で、異教的英雄観とキリスト教世界観が共存する。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/16328",
    "primary_source_type": "Project Gutenberg — Beowulf (Gummere translation, PD)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "口承伝承から無名の写字生による写本化を経た作品で、近代的「作者」概念以前の"
                      "集合的著作モデルの典型。AI生成テクストにおける「作者なき作品」議論と"
                      "構造的類比を持つ。",
         "related_ai_phenomenon": "AI協働による匿名・集合的著作モデル"},
    ],
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "ゲルマン英雄神話",
         "description": "ゲルマン神話DBが扱う英雄譚・怪物退治モチーフの最古層西欧記録。"},
        {"target_db": "AN", "link_type": "parallel",
         "target_entity_name": "ヴァイキング文化",
         "description": "アングロ・サクソンとスカンジナビアの文化交渉を示す一次資料。"},
    ],
})

add({
    "name_ja": "古英語悲歌『さすらい人』",
    "name_en": "The Wanderer",
    "name_original": "The Wanderer",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古英語期",
    "definition": "10世紀のエクセター本（Exeter Book）に収められた115行の古英語悲歌（エレジー）。"
                  "主君を失い海上を流浪する戦士の独白を通して、現世の儚さ（ubi sunt主題）と"
                  "神への帰依を語る。アングロ・サクソン的英雄道徳と修道院的キリスト教内省が融合。",
    "background": "エクセター大聖堂図書館に伝来した10世紀末写本に収録。詩人不詳。",
    "development": "20世紀以降、トールキン『指輪物語』ローハン詩篇（"
                   "「Where now the horse and the rider?」）が直接的引用で大衆化。"
                   "現代英語詩の喪失と回想の主題系譜の祖型。",
    "historical_context": "ヴァイキング侵攻期の不安と修道院文化が交錯する精神状況を反映。",
    "primary_source_url": "https://oldenglishpoetry.camden.rutgers.edu/the-wanderer/",
    "primary_source_type": "Old English Poetry Project (Rutgers, edition + translation)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "古英語悲歌『海の旅人』",
    "name_en": "The Seafarer",
    "name_original": "The Seafarer",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古英語期",
    "definition": "エクセター本収録の124行の古英語悲歌。北海の冬の航海の苦しみを"
                  "現実的描写で語った前半と、地上の富の儚さと天上の故郷への憧れを語る"
                  "宗教的後半とからなる。海洋の試練を魂の修行として読み替える二重構造を持つ。",
    "background": "エクセター本（10世紀末）所収。詩人不詳。",
    "development": "エズラ・パウンド1911年訳が現代主義詩の重要範例となり、"
                   "20世紀英米詩で「海・流浪・苦行」主題系譜の源流に位置づけられる。",
    "historical_context": "海上交易と修道生活が並立するアングロ・サクソン社会の精神性。",
    "primary_source_url": "https://oldenglishpoetry.camden.rutgers.edu/the-seafarer/",
    "primary_source_type": "Old English Poetry Project (Rutgers, edition + translation)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "キャドモンの賛歌",
    "name_en": "Caedmon's Hymn",
    "name_original": "Cædmon's Hymn",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古英語期",
    "definition": "7世紀後半（680年頃）に成立した9行の古英語頭韻詩で、現存最古の"
                  "古英語キリスト教詩。ベーダ『教会史』第4巻第24章により伝来。"
                  "読み書きできない牧夫キャドモンが夢で詩を授けられ、創造主を讃える"
                  "賛歌を口にしたという起源譚を伴う。",
    "background": "ノーサンブリア地方ウィットビー修道院で記録。"
                  "ベーダの記述により「英語詩の起源」として神話化。",
    "development": "古英語キリスト教詩の祖型として、後の『創世記』『出エジプト記』"
                   "『ユディト』等の聖書詩群への道を開いた。",
    "historical_context": "アングロ・サクソンの異教的口承詩がキリスト教主題に転用された画期。",
    "primary_source_url": "https://oldenglishpoetry.camden.rutgers.edu/caedmons-hymn/",
    "primary_source_type": "Old English Poetry Project (Rutgers, edition + translation)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ベーダ『英国教会史』",
    "name_en": "Bede, Ecclesiastical History of the English People",
    "name_original": "Historia Ecclesiastica Gentis Anglorum",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古英語期",
    "definition": "ノーサンブリアの修道士ベーダ（673頃-735）が731年に完成させた"
                  "ラテン語5巻の英国教会史。アングロ・サクソンのキリスト教化を物語形式で記述し、"
                  "キャドモン伝、エドウィン王の改宗、ホイットビー教会会議等の挿話により"
                  "中世英文学の歴史的記憶の基盤を築いた。",
    "background": "ジャロー修道院で執筆。古代地中海歴史記述（エウセビオス）の英国適用。",
    "development": "9世紀のアルフレッド大王治世期に古英語訳が成立。"
                   "中世英文学の歴史記述・聖人伝の祖型として作用。",
    "historical_context": "ローマ的キリスト教普遍主義とアングロ・サクソン地方主義の総合。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/38326",
    "primary_source_type": "Project Gutenberg — Bede Ecclesiastical History (PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アングロ・サクソン年代記",
    "name_en": "Anglo-Saxon Chronicle",
    "name_original": "Anglo-Saxon Chronicle",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古英語期",
    "definition": "9世紀末アルフレッド大王の主導下に編纂が始まり、12世紀まで複数写本で"
                  "継続された古英語年代記。年次形式で英国史を記録し、しばしば頭韻詩"
                  "（『ブルナンブルクの戦い』937年項等）を年次記事内に挿入する。"
                  "古英語散文の最重要モニュメント。",
    "background": "ウェセックス王権の歴史的正統性確保のための編纂事業として開始。"
                  "ピーターバラ写本など7写本系統で伝来。",
    "development": "古英語散文発達の基盤。中世英国史記述の祖型として、"
                   "ジェフリー・オブ・モンマス以降の英国史叙述に影響。",
    "historical_context": "ヴァイキング侵攻期にウェセックス中心的英国意識を構築。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/657",
    "primary_source_type": "Project Gutenberg — Anglo-Saxon Chronicle (PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "頭韻詩（古英語）",
    "name_en": "Old English alliterative verse",
    "name_original": "alliterative verse",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古英語期",
    "definition": "古英語詩の基本韻律。1行を中央のカエスーラで2半行（ヘミスティク）に分け、"
                  "各半行に2強拍を置き、半行間で頭韻（同じ子音の繰り返し）によって結ぶ。"
                  "脚韻ではなく頭子音の反復が韻律的接合原理を担うゲルマン共通の詩法。",
    "background": "ゲルマン諸語に共通する古層詩法。シーヴァース（Sievers）の5パターン"
                   "分類（A-E type）が現代でも基準的記述法。",
    "development": "ノルマン征服以降、フランス系脚韻詩が主流化するなかで一旦衰退するが、"
                   "14世紀後半の頭韻復興（alliterative revival、ガウェイン詩人）で再興。",
    "historical_context": "ゲルマン口承詩の音韻記憶装置。スコップ（口誦詩人）の即興作詩を可能にした。",
    "primary_source_url": "https://oldenglishpoetry.camden.rutgers.edu/",
    "primary_source_type": "Old English Poetry Project (Rutgers)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "頭韻詩は意味より音響構造を優先する韻律で、AIによる音響的言語生成・"
                      "TTS韻律設計と直接的に関わる。AI時代に音響的詩学の再発見を促す。",
         "related_ai_phenomenon": "音響重視のAI詩生成・音声合成韻律設計"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "頭韻法・韻律論",
         "description": "詩学DBの韻律理論にゲルマン語族の代表的範例を提供。"},
    ],
})

add({
    "name_ja": "ケニング（古英語）",
    "name_en": "kenning (Old English)",
    "name_original": "kenning",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古英語期",
    "definition": "古英語・古ノルド詩で用いられた圧縮的隠喩表現。"
                  "「鯨の道（hron-rād）」＝海、「戦の蛇（bēado-leoma）」＝剣のように、"
                  "通常2語の合成語または属格構文で具象を抽象的・装飾的に置換する。"
                  "頭韻詩の語彙的拡張装置として機能した。",
    "background": "ゲルマン詩語彙の伝統。古英語『ベオウルフ』では海・船・剣・戦士に"
                  "数十種のケニングが用いられる。",
    "development": "古ノルド・スカルド詩で極度に発達し、ケニングの内部にケニングを"
                   "入れ子化する複合ケニングが芸術的頂点を迎える（後述参照）。",
    "historical_context": "頭韻詩に必要な語数を確保する詩法的必要から発達した装置。",
    "primary_source_url": "https://oldenglishpoetry.camden.rutgers.edu/",
    "primary_source_type": "Old English Poetry Project (Rutgers)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "ケニングは少数の素材語から無限の組み合わせを生成する圧縮的隠喩生成法で、"
                      "現代のプロンプトエンジニアリング・潜在空間操作と構造的に類比される。"
                      "AI時代における「圧縮による創造」の中世先行事例。",
         "related_ai_phenomenon": "プロンプトエンジニアリング・潜在空間隠喩生成"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "隠喩理論・圧縮表現",
         "description": "詩学DBの隠喩論に中世ゲルマン圏の極限的範例を提供。"},
    ],
})


# ===============================================================
# CATEGORY B — Middle English (8)
# ===============================================================

add({
    "name_ja": "チョーサー『カンタベリー物語』",
    "name_en": "Chaucer, The Canterbury Tales",
    "name_original": "The Canterbury Tales",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "ジェフリー・チョーサー（1343-1400）が1387年頃から死去まで執筆した"
                  "中英語長編枠物語集。カンタベリー大聖堂への巡礼者29名が語る24篇の物語"
                  "（未完）からなり、騎士・粉屋・バース夫人など各身分のヴォイスを"
                  "リアリスティックに描き分け、英国近代物語文学の起源となった。",
    "background": "ボッカッチョ『デカメロン』の枠物語形式を英国に移植。"
                  "プランタジネット朝末期の社会階層を文学的に網羅。",
    "development": "15世紀の写本流布、1476年カクストン初版（英国最初の印刷書籍の一つ）、"
                   "ドライデン『古今寓話集』（1700）以降の近代化、"
                   "現代では脱植民地化批評・ジェンダー批評の対象として継続的再評価。",
    "historical_context": "黒死病後の英国社会の流動化と中産階級興隆を文学的に体現。",
    "primary_source_url": "https://d.lib.rochester.edu/teams/text/benson-and-andersson-the-literary-context-of-chaucers-fabliaux",
    "primary_source_type": "TEAMS Middle English Texts (Rochester)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "「英文学の父」としてチョーサーは正典中の正典だが、"
                      "中産階級的視点・男性中心性・ユダヤ人描写等で現代批評は再検討中。",
         "related_ai_phenomenon": "AIによる正典解体・脱中心化キュレーション"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "枠物語・声の多重化",
         "description": "詩学DBの枠物語論・多声理論（バフチン）の英国的範例。"},
    ],
})

add({
    "name_ja": "チョーサー『トロイラスとクリセイデ』",
    "name_en": "Chaucer, Troilus and Criseyde",
    "name_original": "Troilus and Criseyde",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "チョーサーが1380年代に完成させた5巻8,239行の中英語ロマンス。"
                  "ボッカッチョ『フィローストラト』を原典に、トロイア戦争を背景とする"
                  "トロイラスとクリセイデの恋愛悲劇を描く。"
                  "ライム・ロイヤル詩節（七行詩節）を確立し、英国心理小説の祖型を成す。",
    "background": "リチャード2世宮廷期の宮廷ロマンス需要に応えた円熟期作品。",
    "development": "シェイクスピア『トロイラスとクレシダ』、ヘンリーソン『クレシードの遺言』、"
                   "C.S.ルイス『愛のアレゴリー』の宮廷愛分析の中核例として批評史で重視。",
    "historical_context": "百年戦争中期の英仏文化交渉を背景に、宮廷愛伝統を英語で内面化。",
    "primary_source_url": "https://d.lib.rochester.edu/teams/text/windeatt-troilus-and-criseyde-introduction",
    "primary_source_type": "TEAMS Middle English Texts (Rochester)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "サー・ガウェインと緑の騎士",
    "name_en": "Sir Gawain and the Green Knight",
    "name_original": "Sir Gawain and the Green Knight",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "14世紀後半（1380年頃）に成立した北西部中英語頭韻詩ロマンス。"
                  "全2,530行。アーサー王宮廷でガウェイン卿が首切り遊戯の挑戦を受け、"
                  "1年後に緑の騎士の館で誠実さの試練を経る物語。"
                  "頭韻復興（alliterative revival）の最高傑作。",
    "background": "唯一の写本コットン・ネロA.x（大英図書館）に同詩人の『真珠』『清浄』『忍耐』と"
                  "ともに収録。詩人は無名（Pearl Poet/Gawain Poet）。",
    "development": "20世紀のトールキン編集（1925）で再評価、ヒーニー新訳（2007）、"
                   "デヴィッド・ロウェリー監督映画『グリーン・ナイト』（2021）で大衆化。",
    "historical_context": "中英語頭韻復興の詩学的頂点。アーサー王伝統と英国西部地方意識の融合。",
    "primary_source_url": "https://d.lib.rochester.edu/teams/text/sir-gawain-and-the-green-knight",
    "primary_source_type": "TEAMS Middle English Texts (Rochester)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "partial",
         "rationale": "中世ロマンスの試練構造（quest narrative）はAI生成物語の構造的"
                      "範例として参照されるが、人間的「誠実さ（trawthe）」の倫理的核心は"
                      "AIには移植困難で、部分的にのみ再考される。",
         "related_ai_phenomenon": "AI物語生成における倫理的試練構造の限界"},
    ],
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "首切り遊戯モチーフ",
         "description": "ケルト神話起源の首切り遊戯モチーフの中世英国的展開。"},
    ],
})

add({
    "name_ja": "真珠（パール）",
    "name_en": "Pearl",
    "name_original": "Pearl",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "ガウェイン詩人（同一著者）による14世紀後半の中英語夢詩・哀悼詩。"
                  "全1,212行、101詩節（5行＋12行から成る複雑な12行詩節）。"
                  "夭折した「真珠」（おそらく娘）を悼む夢想者が、夢のなかで天上の少女と"
                  "対話し神学的慰めを得る。中世夢ヴィジョン文学の頂点。",
    "background": "コットン・ネロA.x写本所収。神学的精緻さと頭韻・脚韻併用の絢爛な"
                  "詩節構造で、中英語詩の技巧的頂点とされる。",
    "development": "T.S.エリオット、トールキンが影響を受け、現代では喪失と慰めの"
                   "詩学的範例として継続的に再読される。",
    "historical_context": "黒死病後の死別経験の文学的昇華。",
    "primary_source_url": "https://d.lib.rochester.edu/teams/text/stanbury-pearl",
    "primary_source_type": "TEAMS Middle English Texts (Rochester)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ラングランド『農夫ピアズの夢』",
    "name_en": "Langland, Piers Plowman",
    "name_original": "Piers Plowman",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "ウィリアム・ラングランド（1330頃-1387頃）が三度の改稿を経て"
                  "（A本1370頃・B本1378頃・C本1380年代）執筆した中英語頭韻詩夢ヴィジョン。"
                  "夢想者ウィルが農夫ピアズを案内者に、真理（Truth）の探究と教会・社会の"
                  "腐敗を寓意的に描く。社会批判詩・神学的アレゴリーの集大成。",
    "background": "1381年ワット・タイラーの乱の社会的背景と、ロラード派改革運動と関連深い。"
                  "50以上の写本で伝来し、中世末期英国で広く読まれた。",
    "development": "16世紀の宗教改革派が「先行的改革者」として再発見。"
                   "現代では中世社会経済史・労働倫理研究の中核資料。",
    "historical_context": "黒死病後の労働・社会階層・教会改革論争を文学的に総合。",
    "primary_source_url": "https://d.lib.rochester.edu/teams/text/schmidt-piers-plowman-the-b-version",
    "primary_source_type": "TEAMS Middle English Texts (Rochester)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "マージェリー・ケンプ『マージェリー・ケンプの書』",
    "name_en": "The Book of Margery Kempe",
    "name_original": "The Book of Margery Kempe",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "マージェリー・ケンプ（1373頃-1438以後）が1430年代に書記に口述筆記させた"
                  "中英語自伝的霊性記録。英文学最初の自伝的散文と評される。"
                  "出産の危機を経た神秘体験、エルサレム・ローマ・サンティアゴ巡礼、"
                  "教会との緊張関係を一人称で語る。",
    "background": "ノリッジのジュリアンとも面会。識字能力なき女性が口述で書を残した稀有例。"
                  "唯一の写本（大英図書館Add. MS 61823）が1934年に発見された。",
    "development": "20世紀フェミニスト批評・中世女性霊性研究で再発見・再評価。"
                   "中世女性のエージェンシーと声の問題系の中核資料。",
    "historical_context": "中世末期のロラード派改革論争・女性神秘主義の時代背景。",
    "primary_source_url": "https://d.lib.rochester.edu/teams/text/staley-book-of-margery-kempe",
    "primary_source_type": "TEAMS Middle English Texts (Rochester)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ノリッジのジュリアン『神の愛の啓示』",
    "name_en": "Julian of Norwich, Revelations of Divine Love",
    "name_original": "Revelations of Divine Love",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "ノリッジのジュリアン（1342頃-1416以後）が1373年5月8日に受けた16の"
                  "幻視を、長年の黙想を経て中英語散文で記録した神秘主義神学書。"
                  "短篇本（1373）と長篇本（1393頃以降）の二版が存在。"
                  "「すべては善きものとなる（All shall be well）」の言葉で知られる。",
    "background": "アンカレス（隠修女）として教会脇の小室に生涯隠住。"
                  "英文学最初の女性著作として確認される散文書。",
    "development": "T.S.エリオット『リトル・ギディング』（『四つの四重奏』）が"
                   "「すべては善きものとなる」を引用し、20世紀以降の神秘主義復興で再評価。",
    "historical_context": "黒死病後・百年戦争期の集合的死別経験を女性的視点で神学化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/52958",
    "primary_source_type": "Project Gutenberg — Revelations of Divine Love (PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "中世女性神秘主義神学",
         "description": "哲学DBにおける中世神秘主義（エックハルト等）の英国的並行事例。"},
    ],
})

add({
    "name_ja": "マロリー『アーサー王の死』",
    "name_en": "Malory, Le Morte d'Arthur",
    "name_original": "Le Morte d'Arthur",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "サー・トマス・マロリー（1415頃-1471）が獄中で1469-70年頃に"
                  "完成させた中英語散文によるアーサー王物語集大成。"
                  "ヴァルゲート連作・ポスト=ヴァルゲート連作などフランス語ロマンスを"
                  "英語散文に翻案・統合し、アーサー誕生から円卓崩壊までを単一の叙述に纏めた。",
    "background": "1485年のカクストン版印刷で広く普及。1934年ウィンチェスター写本が"
                  "発見され、原テクスト復元が進んだ。",
    "development": "テニソン『国王牧歌』、T.H.ホワイト『永遠の王』、"
                   "現代ではアーサー王映像化（モンティ・パイソン、エクスカリバー等）の祖型。",
    "historical_context": "薔薇戦争期の英国貴族崩壊を背景に、騎士道理想の終焉を文学化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/1251",
    "primary_source_type": "Project Gutenberg — Le Morte d'Arthur (PD)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "アーサー王伝説の正典化",
         "description": "ケルト・フランス起源のアーサー王伝説を英語散文で正典化した決定版。"},
    ],
})


# ===============================================================
# CATEGORY C — Old Norse / Icelandic / Skaldic (8)
# ===============================================================

add({
    "name_ja": "エッダ（古エッダ・新エッダ）",
    "name_en": "The Eddas (Poetic and Prose)",
    "name_original": "Eddur (Sæmundar Edda / Snorra Edda)",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古ノルド期",
    "definition": "古ノルド神話・英雄伝承の二大文献。"
                  "『古エッダ』（Poetic Edda）は13世紀写本コーデックス・レギウス所収の29篇の詩で、"
                  "『巫女の予言』（Vǫluspá）等のオージン神話・英雄伝承を含む。"
                  "『新エッダ』（Prose Edda）はスノッリ・ストルルソンが13世紀前半に"
                  "スカルド詩作詩法のために編んだ散文神話便覧。",
    "background": "キリスト教化後のアイスランドで異教神話を文学・詩学的遺産として保存した稀有例。"
                  "スノッリは詩法の手引きとして神話を体系化した。",
    "development": "リヒャルト・ワーグナー『ニーベルングの指環』、トールキン中つ国神話、"
                   "現代北欧神話再話文学（ニール・ゲイマン等）まで継続的に源泉となる。",
    "historical_context": "ヴァイキング時代の神話を文字文化期に保存した記憶装置。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/14726",
    "primary_source_type": "Project Gutenberg — Poetic Edda (Bellows translation, PD)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "口承神話を13世紀写本で書き留めたエッダは「真正な異教神話」の地位を"
                      "巡って近代以降論争の対象。AI時代の文化遺産の真正性議論と直結する。",
         "related_ai_phenomenon": "AI生成神話・伝統再話と真正性議論"},
    ],
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "北欧神話正典",
         "description": "神話DBが扱う北欧神話の最古層一次資料。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "ヴァイキング異教文化",
         "description": "人類学DBが扱うヴァイキング異教世界観の一次資料。"},
    ],
})

add({
    "name_ja": "スノッリ・ストルルソン『ヘイムスクリングラ』",
    "name_en": "Snorri Sturluson, Heimskringla",
    "name_original": "Heimskringla",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古ノルド期",
    "definition": "アイスランドの首長スノッリ・ストルルソン（1179-1241）が1220年代に"
                  "執筆した古ノルド散文によるノルウェー王朝史。神話的祖先イングリンガ家から"
                  "12世紀のマグヌス・エルリングソンまで16のサガに分けて叙述する。"
                  "古ノルド散文歴史記述の最高峰。",
    "background": "アイスランド首長層の知的遺産として、王権神話と歴史的事実を融合する独自の"
                  "歴史哲学を展開。スカルド詩を歴史的証言として組み込む方法論を確立。",
    "development": "近代北欧国民意識形成の文学的基盤、19世紀ナショナリズムでの再発見、"
                   "現代では初期国家形成研究の中核資料。",
    "historical_context": "アイスランド共和国末期の政治的動乱期の知的総括。",
    "primary_source_url": "https://heimskringla.no/wiki/Heimskringla",
    "primary_source_type": "Heimskringla.no — canonical Old Norse text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "スカルド詩",
    "name_en": "skaldic poetry",
    "name_original": "skáldskapr",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古ノルド期",
    "definition": "9-13世紀のノルウェー・アイスランドの宮廷詩人（スカルド）が王侯への"
                  "讃詩・嘲詩・追悼詩として作詩した古ノルド詩。"
                  "ドロットクヴェット（dróttkvætt）等の極度に複雑な韻律と、入れ子状の"
                  "ケニング、内韻・頭韻・脚韻の複合的使用が特徴。即興性と技巧的精緻さの極限。",
    "background": "宮廷文化と贈答経済に組み込まれた職業詩人制度。"
                  "詩は王の名声の永続化装置として高い経済的価値を持った。",
    "development": "スノッリ『新エッダ』のスカルド詩法解説で体系化される。"
                   "現代北欧詩学・口承詩学研究の中核対象。",
    "historical_context": "ヴァイキング社会の名声経済と詩的記憶装置。",
    "primary_source_url": "https://www.hi.is/~eybjorn/ugm/skindex/skindex.html",
    "primary_source_type": "Skaldic Poetry of the Scandinavian Middle Ages (open access)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "スカルド詩の極度に圧縮・倒置された統語構造はAI構文解析の限界事例として"
                      "言語学的に再検討される。複層ケニングは生成AIの隠喩生成と直接比較可能。",
         "related_ai_phenomenon": "AI構文解析・隠喩生成における高度圧縮表現の処理"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "スカルド詩は写本伝承の途中で改変・誤伝承の可能性が高く、"
                      "「原作者の真正な作品」という近代的概念で扱えない。AI時代の真正性議論と接続。",
         "related_ai_phenomenon": "AI改変テクストと真正性議論"},
    ],
})

add({
    "name_ja": "ケニング（古ノルド・スカルド詩）",
    "name_en": "kenning (Old Norse skaldic)",
    "name_original": "kenning (skaldic)",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古ノルド期",
    "definition": "古ノルド・スカルド詩で芸術的頂点に達した圧縮的隠喩装置。"
                  "「波の馬の道（hesta unnar leið）」＝海、「戦の鯨（vals val）」＝剣の"
                  "ように、ケニングの内部に別のケニングを入れ子化（複合ケニング）して"
                  "意味を多層化する。スノッリ『新エッダ』が体系的解説を提供。",
    "background": "ドロットクヴェット詩節の複雑な韻律的制約のなかで、必要な音節数を"
                  "確保する詩法的必要から極端に発達。",
    "development": "近代北欧詩・現代詩・現代芸術の隠喩理論で再評価。"
                   "アイスランド現代詩でも継承・変奏される。",
    "historical_context": "宮廷詩人の技巧的競争のなかで圧縮表現が極限化。",
    "primary_source_url": "https://www.hi.is/~eybjorn/ugm/skindex/skindex.html",
    "primary_source_type": "Skaldic Poetry of the Scandinavian Middle Ages (open access)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アイスランド家族サガ",
    "name_en": "Icelandic family sagas (Íslendingasögur)",
    "name_original": "Íslendingasögur",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古ノルド期",
    "definition": "13-14世紀のアイスランドで成立した約40篇の散文サガ群。"
                  "9-11世紀の入植期アイスランド人入植者・首長家族の確執・血讐・婚姻・訴訟を"
                  "客観的な叙述スタイルで描く。中世西欧の散文小説的成熟の最高到達点。",
    "background": "アイスランド共和国期の首長層が口承伝承を散文化した。"
                  "署名なき集合的著作が大半で、近代的著作概念以前の物語生産形態。",
    "development": "19世紀ナショナリズムでの再発見、20世紀のラクスネス『独立の民』、"
                   "現代北欧文学・北欧クライム小説に継承。",
    "historical_context": "氷島民の自治社会の倫理規範を物語形式で記録した法的・文化的記憶。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/606",
    "primary_source_type": "Project Gutenberg — Icelandic sagas (PD translations)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "サガの「客観的・無解説の叙述」は近代小説の心理描写と対極にあり、"
                      "AI生成テクストの没主観的叙述スタイルと類比される。",
         "related_ai_phenomenon": "AIによる客観的・無解説叙述の生成"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "家族サガの「家系誌的真正性」は、家族の口承記憶として真実とされてきたが、"
                      "現代ではフィクション性が強調される。AI時代の家族史・系譜の真正性議論と接続。",
         "related_ai_phenomenon": "AI生成家系・伝記と真正性議論"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "アイスランド共和国期の親族・血讐",
         "description": "人類学DBが扱う北欧親族構造・血讐システムの文学的記録。"},
    ],
})

add({
    "name_ja": "エギルのサガ",
    "name_en": "Egil's Saga",
    "name_original": "Egils saga Skallagrímssonar",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古ノルド期",
    "definition": "13世紀前半（おそらくスノッリ・ストルルソン作）に成立した古ノルド散文サガ。"
                  "10世紀の歴史的詩人エギル・スカラグリムソン（910頃-990頃）の生涯を、"
                  "彼の現存スカルド詩を組み込みつつ三世代の家族史として叙述する。"
                  "詩人サガ（skáldsögur）の代表例。",
    "background": "ミルスサルル写本（13世紀後半）等で伝来。"
                  "エギルの『頭の身代金』『息子の喪失』等のスカルド詩を本文に組み込む独自構造。",
    "development": "20世紀の北欧文学批評・古英詩比較研究で重要参照。"
                   "現代では詩人の自己性・名声経済の研究素材として中核的。",
    "historical_context": "ヴァイキング時代の詩人と王権の緊張関係を物語化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/4655",
    "primary_source_type": "Project Gutenberg — Egil's Saga (PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ニャールのサガ",
    "name_en": "Njál's Saga",
    "name_original": "Brennu-Njáls saga",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古ノルド期",
    "definition": "13世紀末（1280年代）成立の古ノルド散文サガ。最長・最重要の家族サガ。"
                  "賢者ニャールとその一族が血讐の連鎖の末に焼き討ちで滅亡する物語を、"
                  "アイスランド全島規模の訴訟・政治を背景に叙述する。"
                  "中世散文芸術の最高峰の一つ。",
    "background": "60以上の写本で伝来。集合的口承の散文化と思われ、特定著者は不明。",
    "development": "19-20世紀北欧文学批評の中核対象。"
                   "現代北欧文学・国際的な中世文学研究の正典作品。",
    "historical_context": "アイスランド共和国の法制度と血讐制度の緊張を物語化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/17919",
    "primary_source_type": "Project Gutenberg — Njál's Saga (Dasent translation, PD)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "フラフンケルのサガ",
    "name_en": "Hrafnkel's Saga",
    "name_original": "Hrafnkels saga Freysgoða",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "古ノルド期",
    "definition": "13世紀後半成立の比較的短いアイスランド家族サガ。"
                  "首長フラフンケルが従者を殺害し失脚するも復讐し権力を回復する物語を、"
                  "凝縮された散文で描く。家族サガのなかで最も整った構成と緻密な心理描写を持ち、"
                  "サガ研究の方法論的試金石。",
    "background": "シーグルズル・ノルダル（1940）が「フィクション説」を提唱し、"
                  "「歴史的伝承」対「文学的構築」のサガ論争の中心に位置する。",
    "development": "サガの歴史性・文学性論争の中核対象。"
                   "現代の物語論・歴史叙述論で広く参照。",
    "historical_context": "アイスランド共和国期の権力闘争を理念型的に提示。",
    "primary_source_url": "https://www.heimskringla.no/wiki/Hrafnkels_saga_Freysgo%C3%B0a",
    "primary_source_type": "Heimskringla.no — Old Norse canonical text",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY D — Middle High German / Old German (8)
# ===============================================================

add({
    "name_ja": "ヒルデブラントの歌",
    "name_en": "Hildebrandslied",
    "name_original": "Hildebrandslied",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中高ドイツ期",
    "definition": "830年頃成立の現存最古の古高ドイツ語頭韻詩。68行（断片）。"
                  "東ゴート王テオドリックの戦士ヒルデブラントが30年ぶりに故郷に戻り、"
                  "息子ハドゥブラントと不和の対決をする悲劇的英雄歌。"
                  "ゲルマン共通の英雄伝承の散文化以前の段階を示す稀有資料。",
    "background": "フルダ修道院でラテン神学書の余白に書写された。"
                  "詩自体はおそらくロンゴバルド王国起源で、フランク王国に伝来。",
    "development": "19世紀ドイツ国民文学運動で「ドイツ最古の詩」として神話化。"
                   "ヴァーグナーやドイツ・ロマン主義詩人に影響。",
    "historical_context": "民族大移動期の英雄伝承がカロリング朝期の写本文化で固定化された希少例。",
    "primary_source_url": "https://www.hs-augsburg.de/~harsch/germanica/Chronologie/09Jh/Hildebrand/hil_lied.html",
    "primary_source_type": "Bibliotheca Augustana — Hildebrandslied (canonical Old High German edition)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ニーベルンゲンの歌",
    "name_en": "Nibelungenlied",
    "name_original": "Das Nibelungenlied",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中高ドイツ期",
    "definition": "1200年頃にオーストリア・パッサウ近辺で無名詩人によって完成された"
                  "中高ドイツ語英雄叙事詩。全39章2,379詩節（4行詩節、ニーベルンゲン詩節）。"
                  "ジークフリートの裏切り殺害と未亡人クリームヒルトの復讐による"
                  "ブルグント王朝滅亡を描く。ドイツ国民叙事詩。",
    "background": "民族大移動期（5世紀）のフン族・ブルグント族の歴史的記憶を、"
                  "宮廷ロマンス様式で再構成。30以上の写本で伝来。",
    "development": "1755年Bodmerの再発見、19世紀ドイツ国民文学運動の中核作品、"
                   "ヴァーグナー『ニーベルングの指環』（1876）、フリッツ・ラング映画化（1924）。",
    "historical_context": "ドイツ民族意識形成期の文学的核として近代ナショナリズムに利用された。",
    "primary_source_url": "https://www.hs-augsburg.de/~harsch/germanica/Chronologie/13Jh/Nibelungen/nib_n_00.html",
    "primary_source_type": "Bibliotheca Augustana — Nibelungenlied (canonical MHG edition)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "ジークフリート神話・ドラゴン退治",
         "description": "神話DBが扱うゲルマン英雄神話・ドラゴン退治神話の中世正典化。"},
    ],
})

add({
    "name_ja": "ヴォルフラム『パルチヴァール』",
    "name_en": "Wolfram, Parzival",
    "name_original": "Parzival",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中高ドイツ期",
    "definition": "ヴォルフラム・フォン・エッシェンバッハ（1170頃-1220頃）が1200-10年頃に"
                  "完成させた中高ドイツ語宮廷叙事詩。全16巻24,810行。"
                  "クレチアン・ド・トロワ『ペルスヴァル』を基に、騎士パルチヴァールの"
                  "聖杯探求と精神的成長を描く。中世ドイツ宮廷文学の最高峰。",
    "background": "アーサー王伝統と聖杯モチーフをドイツ語圏で独自に発展させた。"
                  "聖杯（Gral）を石（lapis exillis）として描く独自設定が特徴。",
    "development": "ワーグナー『パルジファル』（1882）の原典。"
                   "20世紀のユング派心理学・神話学で英雄成長物語の範例として再評価。",
    "historical_context": "シュタウフェン朝期ドイツの宮廷文化的成熟期の象徴。",
    "primary_source_url": "https://www.hs-augsburg.de/~harsch/germanica/Chronologie/13Jh/Wolfram/wol_pa00.html",
    "primary_source_type": "Bibliotheca Augustana — Parzival (canonical MHG edition)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ゴットフリート『トリスタン』",
    "name_en": "Gottfried, Tristan",
    "name_original": "Tristan",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中高ドイツ期",
    "definition": "ゴットフリート・フォン・シュトラースブルク（生没年不詳、1210年頃没）が"
                  "1210年頃まで執筆した中高ドイツ語宮廷叙事詩。"
                  "未完で19,548行。トマス・オブ・ブリテン版を基に、トリスタンとイゾルデの"
                  "不倫の恋を絶対愛として精緻に内面化。中世西欧愛文学の頂点。",
    "background": "クレチアン的アーサー王ロマンスとは異なる「個人の絶対愛」を主題化し、"
                  "ヴォルフラム『パルチヴァール』の宗教的探求と対極をなす。",
    "development": "ワーグナー『トリスタンとイゾルデ』（1865）が原典。"
                   "20世紀のドゥニ・ド・ルージュモン『愛と西欧』が西欧愛の祖型として分析。",
    "historical_context": "宮廷愛伝統の絶対化と教会的婚姻倫理の緊張を文学化。",
    "primary_source_url": "https://www.hs-augsburg.de/~harsch/germanica/Chronologie/13Jh/Gottfried/got_tr00.html",
    "primary_source_type": "Bibliotheca Augustana — Tristan (canonical MHG edition)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ヴァルター・フォン・デア・フォーゲルヴァイデ",
    "name_en": "Walther von der Vogelweide",
    "name_original": "Walther von der Vogelweide",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中高ドイツ期",
    "definition": "中高ドイツ語抒情詩最大の詩人（1170頃-1230頃）。ミンネザング（宮廷恋愛詩）と"
                  "シュプルッフ（教訓・政治詩）の双方で頂点に達した。"
                  "「Under der linden（菩提樹の下で）」「Ich saz uf einem steine（石の上に座して）」"
                  "等の詩で、宮廷愛と政治批判の双方の範例を確立。",
    "background": "ヴァルチブルクのコンクール、ホーエンシュタウフェン朝期の宮廷流浪詩人として"
                  "皇帝・諸侯への讃詩・諷刺詩を残した。",
    "development": "近代ドイツ抒情詩の祖。"
                   "19世紀ドイツ・ロマン主義での再発見、現代でも独詩教育の中核。",
    "historical_context": "シュタウフェン朝皇帝権・教皇権闘争期の政治抒情詩。",
    "primary_source_url": "https://www.hs-augsburg.de/~harsch/germanica/Chronologie/13Jh/Walther/wal_intr.html",
    "primary_source_type": "Bibliotheca Augustana — Walther von der Vogelweide (canonical MHG edition)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ミンネザング（宮廷恋愛抒情詩）",
    "name_en": "Minnesang",
    "name_original": "Minnesang",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中高ドイツ期",
    "definition": "12-14世紀の中高ドイツ語圏宮廷抒情詩運動。"
                  "プロヴァンスのトルバドゥール詩学を範例に、騎士の高貴な貴婦人への"
                  "片思い的奉仕愛（hôhe minne）を抒情詩化する。"
                  "クレタス・ヴァルター・ハインリヒ・フォン・モルンゲン等が代表詩人。",
    "background": "シュタウフェン朝期の宮廷文化のなかで、教会婚姻倫理とは異なる"
                  "婚外恋愛の抒情的・倫理的様式として制度化。",
    "development": "マイスタージンガーへの通俗化、近代ドイツ・ロマン主義抒情詩への影響、"
                   "現代研究では女性的観点からの再考が進む。",
    "historical_context": "宮廷愛伝統がプロヴァンスからドイツ語圏に移植された文化的転移。",
    "primary_source_url": "https://www.hs-augsburg.de/~harsch/germanica/Chronologie/13Jh/Minnesang/min_intr.html",
    "primary_source_type": "Bibliotheca Augustana — Minnesang anthology (canonical MHG)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "宮廷愛抒情詩・トルバドゥール並行",
         "description": "詩学DBの宮廷愛抒情詩理論にドイツ語圏の代表的並行事例を提供。"},
    ],
})

add({
    "name_ja": "マイスタージンガー",
    "name_en": "Meistersinger",
    "name_original": "Meistersinger",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世末期ゲルマン圏",
    "definition": "14-16世紀のドイツ都市市民階級の職能詩人組合。"
                  "ミンネザングの貴族的伝統を都市職人階級が継承し、"
                  "ニュルンベルク・マインツ・シュトラースブルク等で詩学規則（Tabulatur）に基づく"
                  "歌唱コンクールを実施。ハンス・ザックス（1494-1576）が頂点。",
    "background": "活字印刷期に向けて宮廷文化が都市市民文化に転換する文化的画期。",
    "development": "ワーグナー『ニュルンベルクのマイスタージンガー』（1868）で大衆化。"
                   "ドイツ市民階級の文化的自立の象徴として近代ドイツで再評価。",
    "historical_context": "中世末期ドイツ都市の経済的繁栄と知的市民層の台頭を文学化。",
    "primary_source_url": "https://www.hs-augsburg.de/~harsch/germanica/Chronologie/16Jh/Sachs/sac_intr.html",
    "primary_source_type": "Bibliotheca Augustana — Hans Sachs (canonical edition)",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ドイツ語圏聖史劇",
    "name_en": "German mystery cycles",
    "name_original": "Mysterienspiel / Passionsspiel",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世末期ゲルマン圏",
    "definition": "13-16世紀のドイツ語圏で発達した聖書劇・聖史劇。"
                  "オーバーアマガウ受難劇、フランクフルト受難劇、アルスフェルト受難劇等、"
                  "都市の市民組合（Zünfte）が共同制作・上演する大規模屋外劇として発達。"
                  "ラテン典礼劇から土着言語演劇への移行を体現。",
    "background": "13世紀の聖体祭（コルプス・クリスティ）祭礼との結合で大規模化。"
                  "市民の宗教教育・社会統合装置として機能。",
    "development": "宗教改革で多くが廃絶。オーバーアマガウは1634年のペスト誓願以降10年毎に上演継続。"
                   "20世紀のドイツ演劇史で土着演劇伝統として再評価。",
    "historical_context": "中世末期都市市民の宗教生活と演劇文化の融合。",
    "primary_source_url": "https://www.hs-augsburg.de/~harsch/germanica/Chronologie/15Jh/Passion/pas_intr.html",
    "primary_source_type": "Bibliotheca Augustana — German Passion plays",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY E — Major poetics & forms (8)
# ===============================================================

add({
    "name_ja": "頭韻復興（中英語）",
    "name_en": "alliterative revival",
    "name_original": "alliterative revival",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "14世紀後半の英国西部・北西部で起きた頭韻詩の文学的復興運動。"
                  "ノルマン征服後の脚韻詩主流のなかで、古英語頭韻詩伝統を"
                  "新たな宗教詩・ロマンス・社会批判詩として再生させた。"
                  "代表作は『サー・ガウェインと緑の騎士』『農夫ピアズの夢』『真珠』。",
    "background": "ロンドン中心の宮廷文化（チョーサー）に対する西部地方の文化的自立の表現。"
                  "古英語伝統への意識的回帰。",
    "development": "16世紀の宗教改革期に消滅。20世紀のトールキン・ヒーニーが現代英詩に復活させる。",
    "historical_context": "百年戦争期の英国西部地方の文化的アイデンティティ表現。",
    "primary_source_url": "https://d.lib.rochester.edu/teams/text/sir-gawain-and-the-green-knight",
    "primary_source_type": "TEAMS Middle English Texts (Rochester)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "夢ヴィジョン詩・夢アレゴリー",
    "name_en": "dream allegory / dream vision",
    "name_original": "dream vision",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "中世末期に成立した文学形式。詩人＝夢想者が眠りに落ち、"
                  "夢の中で寓意的人物・案内者と対話して神学・倫理的真理に至る、という枠組みを持つ。"
                  "『薔薇物語』を範例に、ラングランド『農夫ピアズ』、チョーサー『公爵夫人の書』、"
                  "ガウェイン詩人『真珠』などが英国で発展させた。",
    "background": "聖アウグスティヌスの夢解釈論、マクロビウスの夢分類論を理論的基盤とする。"
                  "古典ラテン詩（キケロ『スキーピオーの夢』）の中世的展開。",
    "development": "近代ロマン主義の夢詩（コールリッジ『クーブラ・カーン』）、"
                   "現代の幻想文学（ボルヘス）まで継承される文学形式。",
    "historical_context": "中世末期の内省的霊性と寓意的世界観の文学的統合。",
    "primary_source_url": "https://d.lib.rochester.edu/teams",
    "primary_source_type": "TEAMS Middle English Texts (Rochester)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "アレゴリー詩学・夢の枠組み",
         "description": "詩学DBが扱う中世アレゴリー理論の中核形式。"},
    ],
})

add({
    "name_ja": "聖人伝（ハギオグラフィー）",
    "name_en": "hagiography",
    "name_original": "hagiography",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "聖人の生涯・殉教・奇跡を物語化する中世の重要文学ジャンル。"
                  "ヤコブス・デ・ウォラギネ『黄金伝説』（1260頃）が中世末期の決定版。"
                  "古英語『聖人列伝』（エルフリック）、中英語『南方聖人列伝』など"
                  "土着言語版が広く流布した。",
    "background": "ローマ帝国期の殉教録・修道院伝記の中世的拡張。"
                  "民衆教化と教会的範例提示の二重機能を持つ。",
    "development": "宗教改革で聖人崇敬批判に晒されるが、近代の中世史・民俗学・物語論で"
                   "範例物語の祖型として再評価。",
    "historical_context": "中世キリスト教社会の集合的記憶を聖人を媒介に組織化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/45389",
    "primary_source_type": "Project Gutenberg — The Golden Legend (Caxton, PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "範例文学（エクセンプラ）",
    "name_en": "exemplary literature / exempla",
    "name_original": "exempla",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "説教者が聴衆教化のために用いた短い道徳的物語の文学集成。"
                  "『ローマ人行伝』（Gesta Romanorum、13世紀末）が代表的アンソロジー。"
                  "シェイクスピア・チョーサー・ボッカッチョ等近世文学の物語素材庫として作用。",
    "background": "中世の説教文化のなかで、ラテン・俗語両方で蓄積された物語データベース。"
                  "ドミニコ会・フランシスコ会托鉢修道士の説教実践と結合。",
    "development": "近世の物語短編集（ボッカッチョ、チョーサー）の物語供給源。"
                   "近代の物語論（プロップ、トドロフ）で範例的物語型として研究。",
    "historical_context": "中世説教文化と物語文化の融合の所産。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/26782",
    "primary_source_type": "Project Gutenberg — Gesta Romanorum (PD)",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "聖史劇・道徳劇",
    "name_en": "mystery and morality plays",
    "name_original": "mystery / morality plays",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "中世末期の英国・ドイツ語圏で発達した宗教劇の二大形式。"
                  "聖史劇（mystery plays）はヨーク・チェスター・ウェイクフィールド劇集成のように"
                  "聖書物語を職人組合が連作上演。"
                  "道徳劇（morality plays）は『誰でも人（Everyman）』を典型に、抽象徳目を"
                  "擬人化して人間の魂の救済を描く。",
    "background": "13世紀以降の聖体祭祭礼と都市市民組合の結合で発達。"
                  "ラテン典礼劇から土着言語劇への移行段階。",
    "development": "シェイクスピア・マーロウら近世ドラマの直接的前身。"
                   "20世紀の英国伝統劇復興（T.S.エリオット『大聖堂の殺人』）の祖型。",
    "historical_context": "中世末期の都市市民文化と宗教劇の融合。",
    "primary_source_url": "https://d.lib.rochester.edu/teams/text/davidson-and-oconnell-everyman-and-its-dutch-original-elckerlijc",
    "primary_source_type": "TEAMS Middle English Texts (Rochester)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "バラッド（民衆口承詩）の生成",
    "name_en": "ballad emergence",
    "name_original": "ballad",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "13-15世紀の英国・スコットランド・スカンジナビアで成立した民衆口承詩形式。"
                  "4行詩節（ABCB脚韻）のシンプルな形式に物語的内容を盛り、"
                  "口承伝承で多変種を生成する。"
                  "後の『チャイルド・バラッド』（F.J.チャイルド編、1882-98）が代表的集成。",
    "background": "宮廷詩・教会詩から独立した民衆文芸として中世末期に成熟。"
                  "ロビン・フッド伝説、悲恋・殺人・歴史事件等を主題化。",
    "development": "近世の俗謡として継続。19世紀ロマン主義（ヘルダー、グリム兄弟、"
                   "ウォルター・スコット）が国民詩として再発見。",
    "historical_context": "中世末期の民衆文芸の自立的発達。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/44968",
    "primary_source_type": "Project Gutenberg — Child's English and Scottish Ballads (PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "獣譚（レイナード狐物語）",
    "name_en": "beast epic (Reynard the Fox)",
    "name_original": "Reynard / Reineke / Renart",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世末期ゲルマン圏",
    "definition": "12世紀末から各地のヨーロッパ言語で展開された狐レイナードを主人公とする"
                  "風刺的獣寓話叙事詩。フランス語『ロマン・ド・ルナール』、"
                  "中低ドイツ語『ライネケ・フォス』（1498）、英語版（カクストン1481訳）が代表作。"
                  "封建社会・教会の偽善を諷刺する。",
    "background": "中世ラテン獣寓話（『イーゾップ寓話』ラテン版、『ニウァルディス』）を基に、"
                  "土着言語の社会批判文学として展開。",
    "development": "ゲーテ『ライネケ狐』（1794）が近代化、現代児童文学（ロアルド・ダール"
                   "『すばらしき父さん狐』）まで影響。",
    "historical_context": "中世末期社会の階層的腐敗を獣譚で婉曲批判。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/642",
    "primary_source_type": "Project Gutenberg — Reynard the Fox (Caxton/Goethe, PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "土着言語の文学的高揚論争",
    "name_en": "vernacular elevation debate",
    "name_original": "vernacular elevation",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中英語期",
    "definition": "中世末期から近世初頭にかけて、ラテン語に代えて土着言語"
                  "（英語・ドイツ語・古ノルド語等）を文学・神学・学術言語として"
                  "正統化しようとする議論と実践。"
                  "ジョン・ウィクリフ英訳聖書、マルティン・ルター独訳聖書、"
                  "アイスランドにおける土着サガ書記事業がそれぞれ画期。",
    "background": "ローマ・カトリック普遍ラテン語に対するゲルマン語圏の文化的自立要求。"
                  "印刷術発明（1450頃）が土着言語標準化を加速。",
    "development": "宗教改革・近代国民国家形成の言語的基盤。"
                   "現代では言語政策論・脱植民地論で再評価。",
    "historical_context": "中世末期教会権威の動揺と国民文化形成期の文学言語論争。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/42477",
    "primary_source_type": "Project Gutenberg — Wycliffe Bible / Luther Bible (PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "土着言語の文学的高揚は、ラテン語ヘゲモニーへの翻訳的抵抗として実現された。"
                      "AI時代の機械翻訳・多言語LLM普及は、新たな言語ヘゲモニー（英語）への抵抗運動と"
                      "並行する。",
         "related_ai_phenomenon": "AI多言語モデルと言語的少数派の文学的自立運動"},
    ],
})


# ---------------------------------------------------------------
# Relations between concepts (in this wave)
# ---------------------------------------------------------------

RELATIONS: list[tuple[str, str, str, str]] = [
    # Old English internal
    ("頭韻詩（古英語）", "ベオウルフ", "embodied_in",
     "ベオウルフは古英語頭韻詩の最高傑作。"),
    ("頭韻詩（古英語）", "古英語悲歌『さすらい人』", "embodied_in",
     "さすらい人は古英語頭韻詩エレジーの代表例。"),
    ("頭韻詩（古英語）", "古英語悲歌『海の旅人』", "embodied_in",
     "海の旅人は古英語頭韻詩エレジーの代表例。"),
    ("頭韻詩（古英語）", "キャドモンの賛歌", "embodied_in",
     "キャドモンの賛歌は古英語頭韻詩キリスト教詩の祖型。"),
    ("ケニング（古英語）", "ベオウルフ", "embodied_in",
     "ベオウルフは古英語ケニングの宝庫。"),
    ("ベーダ『英国教会史』", "キャドモンの賛歌", "transmits",
     "ベーダの教会史がキャドモンの賛歌を伝来させた。"),

    # Old English → Middle English
    ("頭韻詩（古英語）", "頭韻復興（中英語）", "extends",
     "頭韻復興はノルマン征服後、頭韻詩伝統を14世紀に再生させた運動。"),
    ("頭韻復興（中英語）", "サー・ガウェインと緑の騎士", "embodied_in",
     "ガウェインは頭韻復興の最高傑作。"),
    ("頭韻復興（中英語）", "ラングランド『農夫ピアズの夢』", "embodied_in",
     "農夫ピアズは頭韻復興の社会批判的代表作。"),
    ("頭韻復興（中英語）", "真珠（パール）", "embodied_in",
     "真珠は頭韻復興の宗教詩的頂点。"),

    # Middle English internal
    ("夢ヴィジョン詩・夢アレゴリー", "ラングランド『農夫ピアズの夢』", "embodied_in",
     "農夫ピアズは中英語夢ヴィジョン詩の代表作。"),
    ("夢ヴィジョン詩・夢アレゴリー", "真珠（パール）", "embodied_in",
     "真珠は中英語夢ヴィジョン詩の宗教的頂点。"),
    ("チョーサー『カンタベリー物語』", "範例文学（エクセンプラ）", "draws_from",
     "カンタベリー物語の各物語は中世範例文学を素材とする。"),
    ("チョーサー『トロイラスとクリセイデ』", "チョーサー『カンタベリー物語』", "predates",
     "トロイラスはチョーサーの円熟期作品でカンタベリー物語に先立つ。"),

    # Old Norse internal
    ("ケニング（古ノルド・スカルド詩）", "スカルド詩", "embodied_in",
     "スカルド詩はケニングの芸術的頂点を示す。"),
    ("スカルド詩", "エギルのサガ", "embedded_in",
     "エギルのサガはスカルド詩を本文に組み込む詩人サガ。"),
    ("ケニング（古英語）", "ケニング（古ノルド・スカルド詩）", "extends",
     "ケニングは古英語からスカルド詩で芸術的頂点に達した。"),
    ("エッダ（古エッダ・新エッダ）", "スノッリ・ストルルソン『ヘイムスクリングラ』", "predates",
     "スノッリの新エッダがスカルド詩法を体系化し、ヘイムスクリングラに先立つ。"),
    ("エッダ（古エッダ・新エッダ）", "アイスランド家族サガ", "predates",
     "エッダ神話世界が家族サガの背景神話を提供する。"),
    ("アイスランド家族サガ", "ニャールのサガ", "embodied_in",
     "ニャールのサガは家族サガの最高峰。"),
    ("アイスランド家族サガ", "エギルのサガ", "embodied_in",
     "エギルのサガは詩人サガ系の代表的家族サガ。"),
    ("アイスランド家族サガ", "フラフンケルのサガ", "embodied_in",
     "フラフンケルのサガは凝縮型家族サガの代表。"),

    # MHG internal
    ("ヒルデブラントの歌", "ニーベルンゲンの歌", "predates",
     "古高ドイツ語ヒルデブラントの歌が、中高ドイツ語ニーベルンゲンの歌に先立つゲルマン英雄詩。"),
    ("ミンネザング（宮廷恋愛抒情詩）", "ヴァルター・フォン・デア・フォーゲルヴァイデ", "embodied_in",
     "ヴァルターはミンネザングの最高峰詩人。"),
    ("ミンネザング（宮廷恋愛抒情詩）", "マイスタージンガー", "extends",
     "マイスタージンガーはミンネザングの市民階級的継承形態。"),
    ("ヴォルフラム『パルチヴァール』", "ゴットフリート『トリスタン』", "contemporaneous",
     "ヴォルフラムとゴットフリートはともに1210年頃の中高ドイツ宮廷叙事詩双璧。"),
    ("ドイツ語圏聖史劇", "聖史劇・道徳劇", "parallel",
     "ドイツ語圏聖史劇と英国聖史劇・道徳劇は中世末期土着言語劇の並行発達。"),

    # Cross-tradition (Germanic ↔ British Isles)
    ("頭韻詩（古英語）", "ヒルデブラントの歌", "parallel",
     "古英語頭韻詩と古高ドイツ語ヒルデブラントの歌は西ゲルマン頭韻伝統の並行。"),
    ("ベオウルフ", "エッダ（古エッダ・新エッダ）", "parallel",
     "ベオウルフとエッダは英・北欧におけるゲルマン英雄神話の並行記録。"),
    ("ニーベルンゲンの歌", "エッダ（古エッダ・新エッダ）", "shares_material",
     "ニーベルンゲンの歌のジークフリート伝承はエッダ系北欧伝承と共通源泉。"),
    ("ベオウルフ", "アイスランド家族サガ", "parallel",
     "ベオウルフの英雄詩世界は家族サガの英雄観の文学的並行。"),

    # Forms cross-cutting
    ("聖人伝（ハギオグラフィー）", "ノリッジのジュリアン『神の愛の啓示』", "extends",
     "ジュリアンの啓示は聖人伝伝統の女性神秘主義的展開。"),
    ("聖人伝（ハギオグラフィー）", "マージェリー・ケンプ『マージェリー・ケンプの書』", "extends",
     "マージェリー・ケンプの書は聖人伝伝統を世俗女性の自伝に拡張。"),
    ("範例文学（エクセンプラ）", "獣譚（レイナード狐物語）", "extends",
     "獣譚は範例文学の動物寓話的展開。"),
    ("聖史劇・道徳劇", "ドイツ語圏聖史劇", "parallel",
     "英国聖史劇・道徳劇とドイツ語圏聖史劇は中世末期都市劇の並行。"),

    # Vernacular debate spans all
    ("土着言語の文学的高揚論争", "チョーサー『カンタベリー物語』", "embodied_in",
     "チョーサーは英語の文学的高揚の決定的画期。"),
    ("土着言語の文学的高揚論争", "ヴォルフラム『パルチヴァール』", "embodied_in",
     "ヴォルフラムはドイツ語の宮廷文学的高揚の代表。"),
    ("土着言語の文学的高揚論争", "アイスランド家族サガ", "embodied_in",
     "家族サガはアイスランド土着語散文の自立的成熟。"),
    ("土着言語の文学的高揚論争", "マロリー『アーサー王の死』", "embodied_in",
     "マロリーは英語散文ロマンスの完成形。"),

    # Ballad / vernacular emergence
    ("バラッド（民衆口承詩）の生成", "獣譚（レイナード狐物語）", "parallel",
     "バラッドと獣譚は中世末期の民衆語文芸の並行発達。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[wave9_c04_medieval_germanic] inserting {len(CONCEPTS)} concepts...")
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
        print("[wave9_c04_medieval_germanic] inserted:")
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
        print(f"  coverage (medieval):")
        for r in db.coverage_by_subfield():
            if r["code"] == "lit_eu_medieval":
                print(f"    {r}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
