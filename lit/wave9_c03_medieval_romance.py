"""
LIT-DB Phase 2 — C03: Medieval Romance Europe (中世西欧・ロマンス語圏)
================================================================
Inserts 40 canonical concepts across 5 categories:
  A. Chivalric epic & courtly lyric (8)
  B. Romance & narrative forms (8)
  C. Italian medieval (8)
  D. Major poetics / criticism (8)
  E. Genres / themes (8)

Subfield: lit_eu_medieval (subfield_id=2), region='西欧'.
Romance-language sphere (Old French / Provençal / Italian / Latin):
chanson de geste, troubadour lyric, Arthurian romance, Roman de la Rose,
Dante / Petrarch / Boccaccio, scholastic poetics, dream vision, mystery
plays, etc.

Sources prioritise public-domain primary editions:
  - Bibliotheca Augustana (https://www.hs-augsburg.de/~harsch/Chronologia/)
  - Gallica BnF (https://gallica.bnf.fr/)
  - Internet Archive (https://archive.org/)
  - Project Gutenberg (https://www.gutenberg.org/)
  - Internet Medieval Sourcebook
    (https://sourcebooks.fordham.edu/sbook.asp)
  - Princeton Dante Project (https://dante.princeton.edu/)
  - Petrarch's Canzoniere (Petrarch.dartmouth.edu)
  - Liber Liber (https://www.liberliber.it/) for Italian texts

Pattern: P1 (Canonical Primary Pursuit) + P3 (cross-tradition parallel
between Provençal / Old French / Italian).

Zero overlap with C02 (Roman/Biblical) or C04 (Germanic medieval) or
C05 (Renaissance). Petrarchism / Dante's Vita Nuova legacy already in
C05 are NOT re-added; this file covers the medieval-original works
themselves and earlier reception only.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (medieval Western Europe / Romance)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    # name_ja, name_en, start, end, description
    ("中世初期（カロリング期）", "Carolingian Early Middle Ages", 750, 1000,
     "カロリング・ルネサンスを経て俗語文学の萌芽が現れる時期。"
     "ラテン教会文学が支配的だが、古フランス語・古イタリア語の最古証言が現れる。"),
    ("中世盛期（ロマネスク・初期ゴシック）", "High Middle Ages", 1000, 1200,
     "シャンソン・ド・ジェスト、トルバドゥール抒情詩、初期ロマンの成立期。"
     "騎士道文化と十字軍の時代。フランス文化圏が中世文学の中心となる。"),
    ("中世盛期後期（13世紀）", "Thirteenth Century", 1200, 1300,
     "クレチアン・ド・トロワ以後のアーサー王物語サイクル、ロマン・ド・ラ・ローズ、"
     "イタリアではフランチェスコ会的霊性詩、ドルチェ・スティル・ノーヴォの形成期。"),
    ("トレチェント（14世紀イタリア）", "Trecento", 1300, 1400,
     "ダンテ『神曲』、ペトラルカ『カンツォニエーレ』、ボッカッチョ『デカメロン』が"
     "成立した俗語文学三大祖の世紀。トスカーナ俗語が後世イタリア語の規範を形成。"),
    ("中世晩期（14-15世紀）", "Late Middle Ages", 1300, 1500,
     "ファブリオー・寓意夢物語・神秘劇など多様なジャンルが俗語で展開。"
     "ペトラルキスムの伝播・人文主義の萌芽がルネサンスへの橋渡しとなる。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — Chivalric epic & courtly lyric (8)
# ===============================================================

add({
    "name_ja": "シャンソン・ド・ジェスト",
    "name_en": "chanson de geste",
    "name_original": "chanson de geste",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "11-13世紀の古フランス語による武勲詩ジャンル。"
                  "10音節または12音節の脚韻アサナンスで構成され、シャルルマーニュ、"
                  "ギヨーム・ドランジュ等の英雄をめぐる封建的忠誠と異教徒との戦いを歌う。"
                  "ジョングルールが宮廷・市場で口承伝達した武人的英雄叙事詩。",
    "background": "カロリング帝国崩壊後の封建社会の集団記憶を、聖地巡礼路や"
                  "十字軍熱の文脈で英雄化した口承伝統が9-11世紀に形成された。",
    "development": "ロランの歌からギヨーム・サイクル、十字軍サイクルへ展開。"
                   "イタリアのプルチ『モルガンテ』、ボイアルド・アリオストの騎士物語詩へ"
                   "継承され、近代ではバイロンや20世紀の歴史小説に影響。",
    "historical_context": "封建社会の倫理（忠誠・名誉・親族復讐）の文学的結晶。",
    "primary_source_url": "https://www.hs-augsburg.de/~harsch/gallica/"
                          "Chronologie/11siecle/Roland/rol_intr.html",
    "primary_source_type": "Bibliotheca Augustana — Old French texts",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "シャンソン・ド・ジェストは口承詩人ジョングルールによる集団的・"
                      "再創造的伝承であり、単一作者性を前提としない。"
                      "LLMの多声的テクスト生成と構造的に類比される。",
         "related_ai_phenomenon": "LLMによる集合的テクスト生成・著者同定問題"},
    ],
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "中世英雄叙事詩",
         "description": "神話DBが扱う英雄叙事の中世フランス的展開。"},
    ],
})

add({
    "name_ja": "ロランの歌",
    "name_en": "Chanson de Roland",
    "name_original": "La Chanson de Roland",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "11世紀末頃成立とされる古フランス語による現存最古のシャンソン・ド・ジェスト。"
                  "オックスフォード写本（1140年代）に約4,002行で伝わる。"
                  "778年ロンスヴォーの戦いでのシャルルマーニュ後衛部隊壊滅を、"
                  "ロランとオリヴィエの友愛・封建忠誠・殉教的最期の物語へと変容させた。",
    "background": "778年のバスク族による奇襲を、十字軍期（第1回十字軍1096-1099）の"
                  "イデオロギーで「サラセン人との聖戦」へ書き換える集合的記憶の文学化。",
    "development": "中世全ヨーロッパに翻案（中高ドイツ語『ルオラントの歌』、"
                   "ノルウェー語サガ等）。19世紀にロマン主義の中で再発見され、"
                   "フランス国民文学の起点として正典化された。",
    "historical_context": "封建忠誠・殉教・聖戦が交錯する中世初期の世界観の結晶。",
    "primary_source_url": "https://www.hs-augsburg.de/~harsch/gallica/"
                          "Chronologie/11siecle/Roland/rol_intr.html",
    "primary_source_type": "Bibliotheca Augustana — La Chanson de Roland",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "ロランの歌は19世紀以降フランス国民文学の正典として制度化されたが、"
                      "近年の脱植民地批評では「異教徒との聖戦」イデオロギーの起源として"
                      "再検討対象となる。AI時代の正典再編議論に直結。",
         "related_ai_phenomenon": "AIキュレーションによる正典再評価"},
    ],
})

add({
    "name_ja": "宮廷恋愛（フィナモール）",
    "name_en": "courtly love / fin'amor",
    "name_original": "fin'amor",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "12世紀南フランス・トルバドゥール詩で確立された貴婦人崇拝の愛の理念。"
                  "騎士＝詩人が高貴な貴婦人（domna）を遠くから崇め、奉仕と苦悩を通じて"
                  "精神的高貴さ（cortezia）に到達する非充足的・封建的愛の規範。"
                  "「fin'amor」（純粋な愛）は19世紀ガストン・パリスの造語「amour courtois」で総称された。",
    "background": "アキテーヌ公ギヨーム9世（1071-1126）以降の南仏宮廷文化と、"
                  "12世紀ルネサンスにおけるオウィディウス『恋の技法』再発見が交差した。",
    "development": "北仏トルヴェール・ドイツミンネゼンガー・イタリア・ドルチェ・スティル・"
                   "ノーヴォ（カヴァルカンティ・ダンテ）・ペトラルキスムへ伝播し、"
                   "西欧近代「ロマンチックラブ」概念の祖型となる。",
    "historical_context": "封建ジェンダー秩序と聖母マリア崇敬が交差する中世性愛文化の結晶。",
    "primary_source_url": "https://www.hs-augsburg.de/~harsch/Chronologia/"
                          "Lspost12/GuilelmusPictaviensis/gui_intr.html",
    "primary_source_type": "Bibliotheca Augustana — William IX Aquitaine",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "fin'amorは「奉仕する自己」という近代恋愛主体の祖型を提供したが、"
                      "AI時代の親密性（チャットボット恋愛・パラソーシャル関係）は"
                      "宮廷恋愛的「不在の他者を崇拝する」構造を再演している。",
         "related_ai_phenomenon": "AIコンパニオン・パラソーシャル親密性"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "fin'amorの規範化された愛の表象は儀礼的・反復的であり、"
                      "AI生成ラブレターの「真正性」議論の中世的祖型となる。",
         "related_ai_phenomenon": "AI恋愛生成テクストの真正性"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "宮廷文化と贈与的愛",
         "description": "人類学DBが扱う騎士道文化・贈与論との接点。"},
    ],
})

add({
    "name_ja": "トルバドゥール抒情詩",
    "name_en": "troubadour lyric",
    "name_original": "trobador",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "12-13世紀南フランス・オック語圏で活動した宮廷詩人トルバドゥール"
                  "（trobador、「発見する者」）が創出した俗語抒情詩の総体。"
                  "ギヨーム9世・ベルナール・ド・ヴァンタドゥール・ベルトラン・ド・ボルン・"
                  "アルノー・ダニエル等が活動。canso（恋愛歌）・sirventés（諷刺歌）・"
                  "alba（夜明け歌）など多様なジャンルを開発した。",
    "background": "アキテーヌ・トゥールーズ・プロヴァンス諸侯の宮廷文化、"
                  "アンダルス・アラブ・ヘブライ詩との接触、女性庇護者（エレオノール・"
                  "ダキテーヌ等）の存在が条件となった。",
    "development": "アルビジョア十字軍（1209-1229）以後イタリア（シチリア派・"
                   "ドルチェ・スティル・ノーヴォ）・カタルーニャ・ドイツ（ミンネザング）へ亡命的伝播。"
                   "ダンテ『俗語論』が言語的範例として参照。",
    "historical_context": "封建宮廷を文学的審級として再構築した最初の俗語詩文化。",
    "primary_source_url": "https://www.trobar.org/troubadours/",
    "primary_source_type": "Trobar — Old Occitan troubadour texts",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "トルバドゥール詩はラテン語ではなくオック語俗語で書かれた最初の"
                      "高度文芸であり、「俗語の文芸的尊厳」を西欧で初めて確立。"
                      "LLMの多言語生成における「中心言語/周辺言語」議論の中世的祖型。",
         "related_ai_phenomenon": "多言語LLMにおける言語的尊厳"},
    ],
})

add({
    "name_ja": "トルヴェール",
    "name_en": "trouvère",
    "name_original": "trouvère",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "12-13世紀北フランス・オイル語圏で活動した宮廷詩人。"
                  "トルバドゥールの北方版として宮廷恋愛詩・武勲詩・牧歌・物語歌を制作。"
                  "シャンパーニュ伯ティボー4世、コノン・ド・ベテュヌ、リシュアール獅子心王、"
                  "アダン・ド・ラ・アル等が活動。約2,000曲の旋律付き歌が伝存。",
    "background": "南仏トルバドゥール文化が北仏宮廷（シャンパーニュ・フランドル・"
                  "アラス）に伝播し、北仏オイル語の文化的洗練と並行して発展した。",
    "development": "アダン・ド・ラ・アル『ロバンとマリオンの劇』など世俗劇への展開、"
                   "中世末期にはイタリア・ドイツ宮廷詩文化に影響。"
                   "近代音楽学では旋律譜が現存する貴重な中世音楽資料として研究される。",
    "historical_context": "北フランスを欧州宮廷文化の中心へ押し上げた俗語抒情詩文化。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b8454677g",
    "primary_source_type": "Gallica BnF — Chansonnier de Noailles",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ドルチェ・スティル・ノーヴォ",
    "name_en": "dolce stil nuovo",
    "name_original": "dolce stil novo",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "13世紀後半フィレンツェを中心にグイド・グイニツェッリ・"
                  "グイド・カヴァルカンティ・ダンテ等が形成した抒情詩流派。"
                  "貴婦人を「天使的女性」（donna angelicata）として精神的・神学的に昇華する詩風で、"
                  "プロヴァンス・シチリア派抒情詩を哲学的・神秘主義的に深化させた。"
                  "「貴族性は心にあり」という新たな貴族倫理を打ち出した。",
    "background": "シチリア派抒情詩、トマス・アクィナスのスコラ哲学、"
                  "フランチェスコ会的神秘主義の交差点で形成された。",
    "development": "ダンテ『新生』『神曲』に集約され、ペトラルカへ継承。"
                   "ペトラルキスムを通じて全ヨーロッパ近代抒情詩の祖型となる。",
    "historical_context": "都市新興階級フィレンツェ商人層の文化的自己定義。",
    "primary_source_url": "https://www.liberliber.it/online/autori/autori-d/"
                          "dante-alighieri/",
    "primary_source_type": "Liber Liber — Italian medieval texts",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "ドルチェ・スティル・ノーヴォは「愛する自己」を哲学的内省主体として"
                      "確立した。デカルト的自己以前の内省的主体性のモデル。"
                      "AI時代の自己理解論議の歴史的源泉。",
         "related_ai_phenomenon": "AIにおける内省的主体性のモデル"},
    ],
})

add({
    "name_ja": "プロヴァンス抒情詩",
    "name_en": "Provençal lyric",
    "name_original": "Provensal",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "古プロヴァンス語（オック語）で12-13世紀に書かれたトルバドゥール詩の総体。"
                  "ギヨーム9世以降約450名の詩人による2,500曲以上の歌が伝存。"
                  "trobar leu（明瞭な詩法）／trobar clus（閉ざされた詩法）／"
                  "trobar ric（豊麗な詩法）の3様式を競合させた高度な詩学を発展させた。",
    "background": "ロマンス語族の中で最初に高度文芸を達成した俗語。"
                  "アンダルス・アラブ・モサラベ詩との接触が形式的影響を与えた可能性。",
    "development": "アルビジョア十字軍によるラングドック衰退後、伝統はイタリア・"
                   "カタルーニャに継承される。ダンテ『煉獄篇』26歌でアルノー・ダニエルを"
                   "「より優れた工匠」と称揚することで正典化された。",
    "historical_context": "中世西欧における俗語文芸の最初の自意識的確立。",
    "primary_source_url": "https://www.trobar.org/",
    "primary_source_type": "Trobar — Old Occitan corpus",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シルヴァンテス（諷刺歌）",
    "name_en": "sirventés",
    "name_original": "sirventés",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "トルバドゥール詩の主要ジャンルの一つで、政治・道徳・戦争を主題とする"
                  "諷刺歌・論争歌。canso（恋愛歌）の旋律を借用しつつ歌詞を諷刺的に"
                  "書き換える形式が一般的。ベルトラン・ド・ボルン（c.1140-c.1215）が"
                  "戦争鼓舞のシルヴァンテスで著名で、ダンテ『地獄篇』28歌に登場する。",
    "background": "12世紀の宮廷間政治・教皇権力・十字軍動員の言論空間で発達。",
    "development": "13世紀イタリア俗語政治詩、近代では政治詩・諷刺詩の中世的範例として参照。",
    "historical_context": "中世封建政治の言論メディアとしての俗語詩。",
    "primary_source_url": "https://www.trobar.org/troubadours/bertran_de_born/",
    "primary_source_type": "Trobar — Bertran de Born",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY B — Romance & narrative forms (8)
# ===============================================================

add({
    "name_ja": "ロマン・クルトワ（宮廷ロマン）",
    "name_en": "roman courtois",
    "name_original": "roman courtois",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "12世紀後半に北フランスで成立した古フランス語による韻文長編物語ジャンル。"
                  "シャンソン・ド・ジェストの集団的英雄性に対し、個人化された騎士の冒険・"
                  "宮廷恋愛・霊的探求を主題化する。クレチアン・ド・トロワが完成形を確立し、"
                  "「ロマンス」という近代ジャンル名の語源となった。",
    "background": "12世紀ルネサンスにおけるラテン古典翻訳熱（『テーバイ物語』『トロイア物語』『エネアス物語』）が"
                  "出発点。アンリ2世プランタジネット朝宮廷が制作的中心。",
    "development": "クレチアン以後、散文ロマンスへ移行し『ヴルガータ・サイクル』『ランスロ＝聖杯散文サイクル』を形成。"
                   "マロリー『アーサー王の死』、近代の歴史小説、ファンタジー文学（トールキン）まで継承。",
    "historical_context": "騎士階級の自己意識が文学的内省主体へ深化する転換点。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b6000952t",
    "primary_source_type": "Gallica BnF — French medieval romance manuscripts",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "ロマン・クルトワは「冒険（aventure）」を物語生成原理として確立。"
                      "個別の冒険挿話を連鎖させる構造はAI生成インタラクティブナラティブと類比される。",
         "related_ai_phenomenon": "AI生成インタラクティブ冒険物語"},
    ],
})

add({
    "name_ja": "クレチアン・ド・トロワ『ランスロ』",
    "name_en": "Chrétien de Troyes, Lancelot",
    "name_original": "Le Chevalier de la Charrette",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "クレチアン・ド・トロワ（c.1135-c.1185）が1177-1181頃にシャンパーニュ伯妃マリーの命で執筆した古フランス語韻文ロマン。"
                  "ランスロが王妃グネヴィエールを救出するため騎士の名誉を犠牲にして"
                  "辱めの荷車に乗る逸話を中心に、宮廷恋愛の絶対性を物語化した。"
                  "ランスロ＝グネヴィエール伝承の原典。",
    "background": "シャンパーニュ宮廷を中心とする女性庇護者文学の典型。"
                  "アレクサンドロス物語・テーバイ物語などの古典翻案運動を承けたケルト＝アーサー伝承の文学化。",
    "development": "13世紀散文化サイクル（『ランスロ・プロサ』）を経てマロリー『アーサー王の死』へ。"
                   "近代では脚本・映画・ファンタジーで反復的に再話され続ける。",
    "historical_context": "宮廷恋愛と封建忠誠の倫理的衝突を文学的に主題化した最初の作品。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b8454675b",
    "primary_source_type": "Gallica BnF — Chrétien de Troyes manuscripts",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "クレチアン・ド・トロワ『ペルスヴァル』",
    "name_en": "Chrétien de Troyes, Perceval ou le Conte du Graal",
    "name_original": "Perceval, ou le Conte du Graal",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "クレチアン・ド・トロワが1180-1190頃にフランドル伯フィリップの命で書き始めた未完の韻文ロマン。"
                  "純朴な森の青年ペルスヴァルが騎士となり、「漁夫王」城で謎の聖杯（graal）と血の槍を目撃するが"
                  "問いを発しなかったため王国の荒廃が癒されない、という主題で聖杯文学を創始した。",
    "background": "ケルト・アーサー伝承の素材とキリスト教秘蹟神学が交錯する転換期に成立。",
    "development": "未完を補完する続編群（4 Continuations）が生まれ、"
                   "13世紀には『散文ペルスヴァル』『散文聖杯』へ展開、"
                   "ロベール・ド・ボロン『ジョセフ・ダリマティ』で聖杯がキリストの聖盃と同定される神秘主義化を遂げる。"
                   "ワーグナー『パルジファル』、エリオット『荒地』までの聖杯象徴の祖。",
    "historical_context": "騎士道倫理と修道的探求が融合する13世紀霊性文化の文学的胎動。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b6000951c",
    "primary_source_type": "Gallica BnF — Perceval manuscripts",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "「問いを発しなかったため物語が成就しない」という構造は、"
                      "AIプロンプトにおける「正しい問いを発する技術」の中世的祖型として読み直せる。",
         "related_ai_phenomenon": "プロンプト設計と問いの倫理"},
    ],
})

add({
    "name_ja": "トリスタンとイズー",
    "name_en": "Tristan and Iseult",
    "name_original": "Tristan et Iseut",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "12世紀後半にベルール（北仏）・トマ（アングロ＝ノルマン）が韻文版を書き始めた、"
                  "ケルト由来の悲恋伝承の文学化。"
                  "コーンウォール王マルクの妃となるアイルランド王女イズーが、誤って飲んだ媚薬により"
                  "騎士トリスタンと宿命的恋愛に陥る運命悲劇。"
                  "宮廷恋愛規範（封建的忠誠と愛の対立）の極限的劇化。",
    "background": "ケルト・アイルランド英雄伝承（ディアルムドとグランニアの追跡譚）が"
                  "12世紀のフランス語圏に流入し書記化された。",
    "development": "ゴットフリート・フォン・シュトラスブルクのドイツ語版、"
                   "13世紀フランス語『散文トリスタン』、ワーグナー『トリスタンとイゾルデ』、"
                   "ジョセフ・ベディエの近代再構成版まで連綿たる継承を持つ。",
    "historical_context": "宮廷恋愛と封建秩序の根源的対立を悲劇化した中世西欧の典型物語。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b105389851",
    "primary_source_type": "Gallica BnF — Tristan manuscripts",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "宿命的悲恋の物語型",
         "description": "神話DBが扱う「禁じられた愛」の物語型の中世西欧的展開。"},
    ],
})

add({
    "name_ja": "ロマン・ド・ラ・ローズ",
    "name_en": "Roman de la Rose",
    "name_original": "Roman de la Rose",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "ギヨーム・ド・ロリスが1230年代に書き始め（約4,000行）、ジャン・ド・マンが1270年代に"
                  "拡張した（約18,000行）古フランス語韻文寓意夢物語。"
                  "詩人＝主人公が薔薇園の薔薇（女性／愛）を獲得しようとする寓意的探求を、"
                  "理性・友・嫉妬・自然・天才といった擬人化された存在との対話を通じて描く。",
    "background": "ギヨーム部分はオウィディウス・宮廷恋愛・スコラ哲学の融合。"
                  "ジャン部分はパリ大学的百科全書知の取り込みで作品性格が大きく変容。",
    "development": "中世後期で最も読まれた俗語作品の一つ。"
                   "シャンソン・ド・ファブリオー的要素・百科全書的雑多性を含み、"
                   "ペトラルカ・チョーサー（『薔薇物語』英訳）・C・S・ルイス『愛のアレゴリー』論まで波及。"
                   "「薔薇物語論争」（クリスティーヌ・ド・ピザン対ジャン・ド・モントルイユ）は"
                   "中世フェミニズム論争の起点となった。",
    "historical_context": "13世紀都市知識人文化（パリ大学・宮廷文化）の集大成的作品。",
    "primary_source_url": "https://romandelarose.org/",
    "primary_source_type": "Roman de la Rose Digital Library (Bodleian/Johns Hopkins)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "薔薇物語論争（querelle de la Rose）は中世における女性嫌悪言説への"
                      "最初の組織的批判であり、現代AI生成テクストにおけるバイアス論争の祖型。",
         "related_ai_phenomenon": "AI生成テクストのバイアス批判"},
    ],
})

add({
    "name_ja": "ボッカッチョ『デカメロン』",
    "name_en": "Boccaccio, Decameron",
    "name_original": "Decameron",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "トレチェント（14世紀イタリア）",
    "definition": "ジョヴァンニ・ボッカッチョ（1313-1375）が1349-1353年に執筆した俗語散文物語集。"
                  "1348年フィレンツェの黒死病から逃れて郊外に集まった10人の若者が10日間に1人1話ずつ"
                  "計100話を語る枠物語。恋・智・運命・愚行を主題に、聖俗・貴賤を横断する人間喜劇を描いた。"
                  "イタリア俗語散文の規範を確立し、近代短編小説の祖型となった。",
    "background": "黒死病（1348）による社会崩壊への文学的応答。"
                  "オリエント枠物語（『千夜一夜』『パンチャタントラ』）・ファブリオー・"
                  "ローマ古典・聖人伝の素材を融合。",
    "development": "シャンソン・ド・ファブリオー、チョーサー『カンタベリー物語』、"
                   "マルグリット・ド・ナヴァール『エプタメロン』、シェイクスピア（『シンベリン』『恋の骨折り損』）、"
                   "近代短編小説（ポー・モーパッサン）の祖。",
    "historical_context": "黒死病後の都市市民文化が古典・教会・宮廷の三大権威から自立する転換点。",
    "primary_source_url": "https://www.liberliber.it/online/autori/autori-b/"
                          "giovanni-boccaccio/decameron/",
    "primary_source_type": "Liber Liber — Decameron",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "100話の枠物語構造は、AI生成短編集のキュレーション・"
                      "パラレル生成構造と直接的に類比される。",
         "related_ai_phenomenon": "AI生成短編アンソロジーの構造"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "黒死病後の都市文化",
         "description": "人類学DBが扱う疫病と社会変容の文学的記録。"},
    ],
})

add({
    "name_ja": "ファブリオー",
    "name_en": "fabliau",
    "name_original": "fabliau",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "12-14世紀北フランスで流行した古フランス語による短い韻文滑稽物語ジャンル。"
                  "約150篇が現存し、聖職者・市民・農民の性的冒険・詐欺・愚行を扱う"
                  "粗野で諷刺的な物語を、8音節脚韻対句で語る。"
                  "宮廷恋愛文学の高雅性に対する社会的・文体的反転として機能した。",
    "background": "都市市民文化の興隆と説教師の例話（exemplum）の世俗化が背景。",
    "development": "ボッカッチョ『デカメロン』、チョーサー『カンタベリー物語』粉屋の話・荘園管理人の話、"
                   "ラ・フォンテーヌ『コント』、近代の諷刺短編小説まで継承。",
    "historical_context": "中世都市市民の世俗的笑い文化の文学的結晶。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/bpt6k55400h",
    "primary_source_type": "Gallica BnF — Recueil général et complet des fabliaux",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "物語", "status": "partial",
         "rationale": "ファブリオーは「粗野・滑稽・諷刺」という低俗ジャンルを文学的領域に持ち込んだ。"
                      "AI生成における「高雅／低俗」の規範変容議論に接続する。",
         "related_ai_phenomenon": "AI生成における雅俗の境界"},
    ],
})

add({
    "name_ja": "エクセンプルム（説教例話）",
    "name_en": "exemplum",
    "name_original": "exemplum",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "中世ラテン語・俗語説教で用いられた短い教訓的逸話。"
                  "教義的命題を聴衆に印象づけるため、聖人伝・古典・動物寓話・"
                  "現代逸話を素材に倫理的範例として再構成する。"
                  "ジャック・ド・ヴィトリ、エティエンヌ・ド・ブルボン、"
                  "ヤコブス・デ・ウォラギネ『黄金伝説』が代表的編纂者。",
    "background": "13世紀の説教者修道会（フランチェスコ会・ドミニコ会）の都市説教戦略の中で"
                  "体系化された。",
    "development": "ボッカッチョ・チョーサー・近代短編小説まで物語素材として継承。"
                   "現代の説話論（プロップ・トドロフ）が中世エクセンプルムを構造分析の対象とした。",
    "historical_context": "中世説教文化と俗語物語ジャンルの架橋装置。",
    "primary_source_url": "https://archive.org/details/jacquesdevitryt00jacqgoog",
    "primary_source_type": "Internet Archive — Exempla of Jacques de Vitry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "物語", "status": "partial",
         "rationale": "エクセンプルムは「短い物語＋教訓」の構造を持ち、"
                      "AI生成における「ストーリー＋教訓抽出」の中世的祖型となる。",
         "related_ai_phenomenon": "AI生成寓話の教訓抽出"},
        {"axis": "受容", "status": "partial",
         "rationale": "説教者の教訓的解釈が物語の「正しい意味」を確定する権威構造は、"
                      "AI出力の解釈権限論議の中世的祖型となる。",
         "related_ai_phenomenon": "AIテクストの解釈権限"},
    ],
})

add({
    "name_ja": "ノヴェッラの起源",
    "name_en": "origin of the novella",
    "name_original": "novella",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "トレチェント（14世紀イタリア）",
    "definition": "短い散文物語ジャンル「ノヴェッラ」の中世イタリア起源。"
                  "13世紀末『ノヴェッリーノ』（百話集、c.1281）に始まり、"
                  "ボッカッチョ『デカメロン』が完成形を確立した。"
                  "ファブリオー・エクセンプルム・古典逸話を融合し、"
                  "近代短編小説（ノヴェル）の語源となった独立ジャンル。",
    "background": "13世紀イタリア都市文化の説話需要、写本配布技術、"
                  "ラテン古典・東方枠物語の流入が起源条件となった。",
    "development": "サッケッティ『三百話集』、マズッチョ『ノヴェッリーノ』、"
                   "バンデッロ『短編集』を経てフランス・スペイン・英国に伝播し、"
                   "近代「短編小説」（short story / Novelle）の祖型となる。",
    "historical_context": "都市読書市場の興隆と俗語散文物語の自立。",
    "primary_source_url": "https://www.liberliber.it/online/autori/autori-a/"
                          "anonimo/il-novellino/",
    "primary_source_type": "Liber Liber — Il Novellino",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY C — Italian medieval (8)
# ===============================================================

add({
    "name_ja": "ダンテ『神曲』",
    "name_en": "Dante, Divina Commedia",
    "name_original": "Commedia / Divina Commedia",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "トレチェント（14世紀イタリア）",
    "definition": "ダンテ・アリギエーリ（1265-1321）が1308-1321年に執筆した三部100歌の俗語叙事詩。"
                  "三韻句法（terza rima）でダンテ自身が地獄・煉獄・天国を旅する寓意的巡礼譚を歌う。"
                  "古典（ウェルギリウス）・スコラ哲学（アクィナス）・宮廷恋愛（ベアトリーチェ）を統合し、"
                  "中世西欧キリスト教世界観の総合的文学化を達成した。",
    "background": "1302年フィレンツェ追放後の流謫経験、白派・黒派抗争、"
                  "教皇権・神聖ローマ帝国の対立、トマス・アクィナスの神学的総合が背景。",
    "development": "中世後期のすべての俗語叙事詩の規範となり、ボッカッチョによる注釈で正典化。"
                   "近代ではブレイク・ロセッティ・エリオット『荒地』・ベケットまで影響。"
                   "イタリア標準語形成の起点。",
    "historical_context": "中世ヨーロッパ知の総合と俗語文芸の最高達成。",
    "primary_source_url": "https://dante.princeton.edu/",
    "primary_source_type": "Princeton Dante Project — Commedia full text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "三部・三韻句法・100歌という強固な形式構造は、"
                      "形式制約のもとでの創造というAI生成の構造的問いに直結する。",
         "related_ai_phenomenon": "形式制約下のAI創造性"},
        {"axis": "正典", "status": "rethinking",
         "rationale": "神曲はイタリア国語形成の起点として正典化されたが、"
                      "AI時代の正典再編議論において、形式言語の規範形成のモデルケースとして再検討される。",
         "related_ai_phenomenon": "AIによる言語規範形成"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ダンテのスコラ的世界観",
         "description": "哲学DBが扱う中世スコラ哲学の文学的総合。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "中世詩学の集大成",
         "description": "詩学DBが扱う中世寓意詩学の総合的範例。"},
    ],
})

add({
    "name_ja": "ダンテ『新生』",
    "name_en": "Dante, Vita Nuova",
    "name_original": "Vita Nuova",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "ダンテが1294年頃に編纂した俗語による散文＋詩のプロシメトロン作品。"
                  "ベアトリーチェ・ポルティナーリへの愛と彼女の早逝を、抒情詩31篇とその来歴を解説する散文で語る。"
                  "ドルチェ・スティル・ノーヴォの集大成であり、神曲ベアトリーチェの霊的役割の伏線となる。"
                  "西欧文学最初の自伝的恋愛物語の試み。",
    "background": "グイド・カヴァルカンティとの友情・対話の中で構想された。"
                  "プロヴァンス抒情詩の「vida（伝記）」の形式的影響を受ける。",
    "development": "ペトラルカ『カンツォニエーレ』の伝記的恋愛詩集の祖型。"
                   "ダンテ・ガブリエル・ロセッティの英訳・絵画でラファエル前派に影響。"
                   "近代の伝記的批評・告白文学の遠い先駆。",
    "historical_context": "個人的愛の経験を体系的詩文として構造化した最初の試み。",
    "primary_source_url": "https://www.liberliber.it/online/autori/autori-d/"
                          "dante-alighieri/vita-nuova/",
    "primary_source_type": "Liber Liber — Vita Nuova",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ペトラルカ『カンツォニエーレ』",
    "name_en": "Petrarch, Canzoniere",
    "name_original": "Rerum vulgarium fragmenta",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "トレチェント（14世紀イタリア）",
    "definition": "フランチェスコ・ペトラルカ（1304-1374）が生涯にわたり編纂した俗語抒情詩集。"
                  "ラウラへの愛を主題とする366篇のソネット・カンツォーネ・セスティーナ等で構成され、"
                  "ラウラ生前と死後の二部構成で人間的愛の罪意識と精神的浄化の弁証法を描く。"
                  "ペトラルキスムを通じて全ヨーロッパ近代抒情詩の規範となった。",
    "background": "1327年アヴィニョンでラウラと邂逅したとされる。"
                  "ドルチェ・スティル・ノーヴォと古典ラテン抒情詩（カトゥッルス・プロペルティウス）の融合。",
    "development": "16世紀ペトラルキスム運動を通じ、フランスのプレイヤード派（ロンサール・デュベレー）、"
                   "イングランドのワイアット・サリー・スペンサー・シェイクスピアのソネット連作の祖型となる。",
    "historical_context": "中世宮廷恋愛詩を近代的内省抒情詩へ変容させた決定的作品。",
    "primary_source_url": "https://petrarch.dartmouth.edu/",
    "primary_source_type": "Dartmouth Petrarch Online Concordance",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "ペトラルカ的「分裂する内面の自己」（同名論文Greene）は近代主観性の祖型。"
                      "AI時代の自己分裂・複数主体性の議論の歴史的源泉。",
         "related_ai_phenomenon": "AIアバターと自己の複数化"},
    ],
})

add({
    "name_ja": "カヴァルカンティの抒情詩",
    "name_en": "Cavalcanti lyric (dolce stil nuovo)",
    "name_original": "Guido Cavalcanti, Rime",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "グイド・カヴァルカンティ（c.1255-1300）の抒情詩。"
                  "ドルチェ・スティル・ノーヴォの中心人物として愛を「アヴェロエス的能動知性」"
                  "の哲学的範疇で論じる暗鬱な詩風を確立。"
                  "代表作カンツォーネ『Donna me prega（私に貴女が問うには）』は"
                  "愛の生理学・心理学を哲学詩として論じる中世抒情詩の知的頂点。",
    "background": "アヴェロエス哲学・パドヴァの自然哲学とフィレンツェ宮廷文化の交差点。",
    "development": "ダンテ『新生』での盟友。"
                   "近代ではエズラ・パウンドが翻訳・紹介して20世紀モダニズム詩学に大きな影響。",
    "historical_context": "中世スコラ哲学と俗語抒情詩の最も濃密な交差点。",
    "primary_source_url": "https://www.liberliber.it/online/autori/autori-c/"
                          "guido-cavalcanti/",
    "primary_source_type": "Liber Liber — Cavalcanti Rime",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ボッカッチョ『名婦伝』",
    "name_en": "Boccaccio, De claris mulieribus",
    "name_original": "De mulieribus claris",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "トレチェント（14世紀イタリア）",
    "definition": "ボッカッチョが1361-1362年に執筆したラテン語著作。"
                  "イヴから同時代のヨハンナ・ナポリ女王まで106人の女性の伝記を集める。"
                  "ペトラルカ『有名男子伝』と対をなし、女性個人を歴史的範例として論じた最初の体系的著作。"
                  "中世末期から近代へのジェンダー言説の重要な節点。",
    "background": "ペトラルカとの友情と古典復興運動の中で執筆。"
                  "プルタルコス『対比列伝』の女性版を意図した。",
    "development": "クリスティーヌ・ド・ピザン『淑女の都市』の直接的参照源。"
                   "ルネサンス・近代の女性伝記文学（『ジャン・ダルク』伝記等）の祖型。",
    "historical_context": "中世末期の女性論議の知的中核資料。",
    "primary_source_url": "https://archive.org/details/concerningfamou00boccgoog",
    "primary_source_type": "Internet Archive — De claris mulieribus",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "受容", "status": "partial",
         "rationale": "中世末期の女性表象の枠組みは現代AIの女性表象バイアス議論の歴史的祖型。",
         "related_ai_phenomenon": "AI生成における女性表象バイアス"},
    ],
})

add({
    "name_ja": "ヤコポーネ・ダ・トーディのラウダ",
    "name_en": "Iacopone da Todi, Laude",
    "name_original": "Laude / Laudi spirituali",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "フランチェスコ会霊性派詩人ヤコポーネ・ダ・トーディ（c.1230-1306）が著した俗語宗教詩集。"
                  "イタリア中部ウンブリア方言で書かれた約100篇のラウダ（讃歌）が伝存。"
                  "Stabat Mater（聖母嘆きの歌）の作詩者として知られる。"
                  "アッシジのフランチェスコ『太陽の讃歌』と並び中世イタリア俗語宗教詩の頂点。",
    "background": "フランチェスコ会霊性派（spirituali）の終末論的厳格主義と"
                  "教皇ボニファティウス8世との抗争（投獄経験）が霊的詩想を深化させた。",
    "development": "中世末期のラウダ運動・典礼劇に継承。"
                   "近代ではジョズエ・カルドゥッチ・パスコリらの再評価で正典化。",
    "historical_context": "13世紀フランチェスコ会霊性運動の文学的結晶。",
    "primary_source_url": "https://www.liberliber.it/online/autori/autori-i/"
                          "iacopone-da-todi/",
    "primary_source_type": "Liber Liber — Iacopone Laude",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "シチリア派抒情詩",
    "name_en": "Sicilian School (poetry)",
    "name_original": "Scuola siciliana",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "13世紀前半、神聖ローマ皇帝フェデリーコ2世（在位1220-1250）のパレルモ・フォッジア宮廷で"
                  "活動した抒情詩人集団。ジャコモ・ダ・レンティーニ等が、トルバドゥール詩を"
                  "シチリア俗語で翻案・革新し、ソネット形式を初めて確立した。"
                  "後のドルチェ・スティル・ノーヴォ・ペトラルキスムの直接的祖。",
    "background": "ノルマン・シチリア王国の多文化的（アラブ・ビザンツ・ラテン）宮廷文化と"
                  "皇帝フリードリヒ2世の文芸庇護が母胎。",
    "development": "皇帝家の没落（1266マンフレディ戦死）後、トスカーナ過渡派"
                   "（グイットーネ・ダレッツォ）を経てドルチェ・スティル・ノーヴォへ継承。"
                   "ダンテ『俗語論』でその貢献を高く評価される。",
    "historical_context": "イタリア俗語詩の自立的出発点。",
    "primary_source_url": "https://www.liberliber.it/online/autori/autori-s/"
                          "scuola-siciliana/",
    "primary_source_type": "Liber Liber — Scuola siciliana",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ペトラルキスム前駆",
    "name_en": "Petrarchism precursor (medieval roots)",
    "name_original": "petrarchismo (origini medievali)",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "トレチェント（14世紀イタリア）",
    "definition": "ペトラルカ『カンツォニエーレ』が後世ペトラルキスム運動の祖型となるに至る、"
                  "中世イタリア抒情詩の系譜的前駆条件。"
                  "シチリア派・ドルチェ・スティル・ノーヴォ・ダンテ『新生』を統合的に再編した"
                  "トレチェント抒情詩学の達成として、近代的恋愛抒情詩の規範を確立した。"
                  "（C05ルネサンス期の「ペトラルキスム」とは区別される、その中世的源泉。）",
    "background": "13-14世紀イタリア俗語抒情詩の連続的発展がペトラルカに集約された。",
    "development": "16世紀イタリア（ベンボ・カスティリオーネ）・フランス（プレイヤード派）・"
                   "イングランド（シェイクスピアのソネット連作）の汎ヨーロッパ的展開へ。",
    "historical_context": "中世末期から近代抒情詩への決定的橋渡し。",
    "primary_source_url": "https://petrarch.dartmouth.edu/",
    "primary_source_type": "Dartmouth Petrarch Online — corpus context",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})


# ===============================================================
# CATEGORY D — Major poetics / criticism (8)
# ===============================================================

add({
    "name_ja": "中世寓意解釈（アレゴレシス）",
    "name_en": "medieval allegoresis",
    "name_original": "allegoresis",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "中世西欧で発達したテクストの寓意的解釈方法。"
                  "オリゲネス・アウグスティヌスの聖書解釈学、"
                  "プラトン哲学のキリスト教的読み替え、"
                  "古典神話の道徳的・キリスト教的再解釈を含む。"
                  "テクストの字義的意味を超えた多重的真理層を読み取る方法論として、"
                  "中世詩学の中核を成した。",
    "background": "ヘレニズム期の寓意解釈（フィロン・オリゲネス）の中世継承。"
                  "12世紀ルネサンスでベルナール・シルウェストリス『アエネーイス註解』、"
                  "13世紀でアリストテレス註解運動と統合された。",
    "development": "ダンテ『饗宴』『カングランデ書簡』で詩学的方法として理論化。"
                   "ルネサンスでは批判的に継承され、近代では新批評・脱構築批評と対比的に再評価。",
    "historical_context": "中世における意味の重層性とテクスト権威の理解枠組み。",
    "primary_source_url": "https://sourcebooks.fordham.edu/source/aug-confessions.asp",
    "primary_source_type": "Internet Medieval Sourcebook — Augustine et al.",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "中世寓意解釈はテクストに「複数の正しい解釈」を許容する読みの倫理を確立した。"
                      "LLM出力の多重解釈問題に直結する歴史的範例。",
         "related_ai_phenomenon": "LLM出力の多義性と解釈"},
        {"axis": "言語", "status": "rethinking",
         "rationale": "字義／寓意／道徳／神秘という多層的言語観は、"
                      "プロンプトと出力の意味階層を理解するモデルとして再活用できる。",
         "related_ai_phenomenon": "プロンプトと意味階層"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "中世寓意詩学",
         "description": "詩学DBが扱う中世解釈学の核心。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "アウグスティヌス的記号論",
         "description": "哲学DBが扱う中世記号論・解釈学の文学的応用。"},
    ],
})

add({
    "name_ja": "聖書四義（四重解釈）",
    "name_en": "four senses of scripture",
    "name_original": "quadriga / sensus quattuor",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "中世神学が体系化したテクスト解釈の四層モデル。"
                  "字義（litteralis／historicus）・寓意（allegoricus）・"
                  "道徳（moralis／tropologicus）・神秘（anagogicus）の四義で"
                  "聖書を解釈する方法論。「ニコラオ・デ・リラの公式」"
                  "（Littera gesta docet, quid credas allegoria, moralis quid agas, quo tendas anagogia）が"
                  "標準形を提供する。",
    "background": "オリゲネス三層解釈（字義・道徳・神秘）に寓意層を加えてカッシアヌスが四層化、"
                  "中世盛期に標準化された。",
    "development": "ダンテ『カングランデ書簡』で世俗詩（神曲）にも適用される。"
                   "ルネサンスの古典寓意解釈・近代以降の象徴主義詩学に継承。"
                   "現代の階層的記号論（ジュネット）にも理論的影響。",
    "historical_context": "中世における「正しい読み」の制度的枠組み。",
    "primary_source_url": "https://sourcebooks.fordham.edu/source/dante-letters.asp",
    "primary_source_type": "Internet Medieval Sourcebook — Dante's Letter to Cangrande",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アルス・ディクタミニス（書記技法）",
    "name_en": "ars dictaminis",
    "name_original": "ars dictaminis",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "11-13世紀ボローニャ・モンテカッシーノで発達したラテン語書簡作成の技法書ジャンル。"
                  "アルベリック・モンテカッシーノ、ブオンコンパーニョ・ダ・シーニャ等が体系化。"
                  "salutatio（呼びかけ）・exordium（導入）・narratio・petitio・conclusioの五分構造を持ち、"
                  "教皇庁・諸侯宮廷の公的書簡作成を支えた中世修辞学の応用形。",
    "background": "11世紀の教皇庁・帝国行政文書需要と古典修辞学（キケロ・カッシオドルス）の中世継承。",
    "development": "13-14世紀のフィレンツェ書記局（ブルネット・ラティーニ）でラテン語から俗語へ拡張。"
                   "近代ではビジネス・公文書修辞学の祖型として再評価される。",
    "historical_context": "中世盛期の文書文化の制度的基盤。",
    "primary_source_url": "https://archive.org/details/MN40130ucmf_1",
    "primary_source_type": "Internet Archive — Boncompagno da Signa",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "アルス・ディクタミニスは「公的書簡の標準書式」を体系化した点で、"
                      "AI生成における定型書式生成（ビジネスメール等）の歴史的祖型。",
         "related_ai_phenomenon": "AI生成定型書式"},
    ],
})

add({
    "name_ja": "ダンテ『俗語論』",
    "name_en": "Dante, De Vulgari Eloquentia",
    "name_original": "De vulgari eloquentia",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "トレチェント（14世紀イタリア）",
    "definition": "ダンテが1303-1305年頃にラテン語で執筆した未完の俗語論。"
                  "イタリア半島14方言を比較検討し、文学に値する「光輝ある俗語」（vulgare illustre）を"
                  "理論化した中世最初の俗語言語学的著作。"
                  "詩・形式・主題の三位一体を論じる詩学的考察も含む。",
    "background": "12-13世紀イタリア各都市方言の文学的差異と、ラテン語の独占的権威への問題提起。",
    "development": "ペトラルカ・ボッカッチョ以降のイタリア標準語確立への理論的支柱。"
                   "16世紀ピエトロ・ベンボ『俗語散文論』へ受け継がれ、"
                   "ロマンス諸言語の標準化議論の祖となる。",
    "historical_context": "俗語が文芸的尊厳を確立する転換期の理論的宣言。",
    "primary_source_url": "https://www.liberliber.it/online/autori/autori-d/"
                          "dante-alighieri/de-vulgari-eloquentia/",
    "primary_source_type": "Liber Liber — De vulgari eloquentia",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "「光輝ある俗語」概念は、複数の方言群から文芸的標準を構築する理論的試みであり、"
                      "多言語LLMの言語標準化議論の中世的先駆となる。",
         "related_ai_phenomenon": "多言語LLMの標準化"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "中世詩学・俗語論",
         "description": "詩学DBが扱う俗語文芸の自立論の祖型。"},
    ],
})

add({
    "name_ja": "フィナモールの詩規範",
    "name_en": "fin'amor codex",
    "name_original": "código del fin'amor",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "アンドレアス・カペッラヌス『恋愛論』（De amore, c.1185）に体系化された"
                  "宮廷恋愛の31条の規範。秘密性・忍耐・嫉妬・苦悩・贈与・奉仕等、"
                  "宮廷恋愛の儀礼的規則を詩学的・倫理的法典として理論化した。"
                  "13世紀以降の宮廷恋愛詩のメタ規範として機能した。",
    "background": "シャンパーニュのマリー宮廷（クレチアン・ド・トロワ庇護者）の文化的環境で執筆。",
    "development": "12-13世紀宮廷恋愛文学全体の理論的基盤。"
                   "近代では中世ジェンダー研究・愛の社会史（ドゥニ・ド・ルージュモン『愛と西洋』）"
                   "の中核資料として再活用。",
    "historical_context": "中世宮廷恋愛文化の規範化と理論化。",
    "primary_source_url": "https://archive.org/details/artofcourtlylove00andr",
    "primary_source_type": "Internet Archive — Andreas Capellanus, De Amore",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ジョク・パルティ（恋愛論争詩）",
    "name_en": "joc partit / partimen",
    "name_original": "joc partit / partimen / jeu-parti",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "トルバドゥール／トルヴェール詩のジャンルの一つ。"
                  "二人の詩人が恋愛・倫理に関する論争を交互に詩節で論じる対話詩。"
                  "ジャンルの起源は南仏tensoだが、北仏でjoc partit / jeu-partiとして発達した。"
                  "宮廷的な詩と倫理討論を結合した知的娯楽として宮廷で実演された。",
    "background": "宮廷の知的娯楽としての対論文化と、中世大学のスコラ的討論術（disputatio）の交差点。",
    "development": "中世末期の宮廷文化衰退とともにジャンルとしては消滅するが、"
                   "対論詩の構造はルネサンス・近代の対話詩・劇詩に継承される。",
    "historical_context": "中世宮廷の知的娯楽と詩的形式の融合。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b8454677g",
    "primary_source_type": "Gallica BnF — Trouvère manuscript collections",
    "importance_score": 2,
    "source_tier": "primary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "アクィナスの美学",
    "name_en": "Aquinas aesthetics",
    "name_original": "pulchritudo (Aquinas)",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "トマス・アクィナス（1225-1274）が『神学大全』『真理論』等で展開した美の哲学。"
                  "美の三条件integritas（完全性）・consonantia（調和）・claritas（明晰）と"
                  "「快適に視られるもの」（quod visum placet）という定義は中世美学の最高総合。"
                  "中世詩学・後世美学（ジョイス『若き芸術家の肖像』）に決定的影響。",
    "background": "アリストテレス『詩学』のラテン中世受容、アヴェロエスのアラビア注釈、"
                  "アウグスティヌス美学伝統の総合。",
    "development": "ダンテの世界観の哲学的支柱。"
                   "近代ではマリタン『芸術と詩におけるトマス主義』、"
                   "ジョイスの美学論などで現代美学に再活用される。",
    "historical_context": "中世スコラ哲学による美の体系化の頂点。",
    "primary_source_url": "https://archive.org/details/summatheologicat00thomuoft",
    "primary_source_type": "Internet Archive — Summa Theologiae Latin",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "アクィナスの美の三条件",
         "description": "哲学DBが扱う中世美学の中核概念。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "中世詩学的美論",
         "description": "詩学DBが扱う中世美学の哲学的核。"},
    ],
})

add({
    "name_ja": "ブルネット・ラティーニ",
    "name_en": "Brunetto Latini, Tresor / Tesoretto",
    "name_original": "Li livres dou Tresor / Tesoretto",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "ブルネット・ラティーニ（c.1220-1294）はフィレンツェ書記局長で、"
                  "古フランス語『宝典』（Tresor, c.1265）と俗語イタリア語『小宝典』（Tesoretto）を著した。"
                  "アリストテレス的倫理学・修辞学・百科全書知を俗語に翻訳・体系化した。"
                  "ダンテの師として『神曲・地獄篇』15歌に登場する。",
    "background": "13世紀後半フィレンツェ書記局の俗語政治・文学文化の中核人物。",
    "development": "ダンテ・俗語百科書（『約束された書物』）・近代百科全書の祖型。"
                   "イタリア俗語散文の規範形成への貢献。",
    "historical_context": "中世末期都市知識人の俗語的知の総合化。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b8454678s",
    "primary_source_type": "Gallica BnF — Brunetto Latini Tresor",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY E — Genres / themes (8)
# ===============================================================

add({
    "name_ja": "宮廷恋愛論争",
    "name_en": "courtly love debate",
    "name_original": "querelle de la Rose / querelle des dames",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世晩期（14-15世紀）",
    "definition": "中世末期の宮廷恋愛・女性表象をめぐる論争群。"
                  "クリスティーヌ・ド・ピザン（1364-1430）が『薔薇物語』の女性嫌悪表象を批判した"
                  "「薔薇物語論争」（querelle de la Rose, 1401-1403）と、"
                  "15-16世紀の「女性論争」（querelle des femmes）を含む。"
                  "中世フェミニズム言論の起点。",
    "background": "ジャン・ド・マンの『薔薇物語』後半の女性嫌悪的表象に対する批判。"
                  "中世末期の都市知識人女性（クリスティーヌ・ド・ピザン）の自立的執筆活動。",
    "development": "ルネサンス『淑女の都市』（1405）・近代フェミニズム文学批評の祖型。"
                   "現代のジェンダー批評・AI生成バイアス論議の歴史的源泉。",
    "historical_context": "中世末期の女性主体の知的自立運動。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b520003203",
    "primary_source_type": "Gallica BnF — Christine de Pizan manuscripts",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "宮廷恋愛論争はテクスト中の女性表象の倫理的責任を問うた最初の組織的批評。"
                      "現代AI生成バイアス論争の中世的祖型。",
         "related_ai_phenomenon": "AI生成テクストのジェンダーバイアス批判"},
    ],
})

add({
    "name_ja": "レー（ブルトン・レー）",
    "name_en": "lai / Breton lai",
    "name_original": "lai breton",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期（ロマネスク・初期ゴシック）",
    "definition": "12世紀後半フランスで発達した古フランス語による短い韻文物語ジャンル。"
                  "マリー・ド・フランス（c.1160-1215頃活躍）の12篇のレーが代表的。"
                  "ケルト・ブルターニュ素材を基にした超自然的恋愛物語を、約100-1,000行の8音節脚韻対句で語る。"
                  "「ブルターニュの竪琴詩から派生した」と作中で説明される音楽的物語ジャンル。",
    "background": "ブルターニュ・ノルマンディーのケルト・アングロ＝ノルマン文化交差圏で発達。"
                  "プランタジネット朝アンリ2世宮廷の文学的洗練を反映。",
    "development": "中世末期の英語『サー・ガウェイン』、チョーサー『フランクリンの話』など"
                   "ロマンス諸国に拡散。近代の幻想短編小説（ノディエ・メリメ）の遠い祖型。",
    "historical_context": "中世における短編幻想物語の創出。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b6000952t/f1.item",
    "primary_source_type": "Gallica BnF — Marie de France Lais (BnF MS fr. 2168)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "夢物語（寓意夢）",
    "name_en": "dream vision",
    "name_original": "songe / vision allégorique",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "中世西欧文学の主要枠組みジャンル。"
                  "詩人＝主人公が眠りに落ち、寓意的夢を体験するという設定で、"
                  "宮廷恋愛・霊性的探求・社会風刺など多様な主題を扱う。"
                  "マクロビウス『スキピオの夢註解』が理論的支柱を提供し、"
                  "『薔薇物語』『神曲』『真珠詩』『言葉の館』等で多様に展開された。",
    "background": "聖書（ヨセフ・ダニエル・黙示録）と古典（『スキピオの夢』）の夢物語伝統が"
                  "中世キリスト教的寓意学と融合した。",
    "development": "チョーサー『公爵夫人の書』『言葉の館』『鳥の議会』、"
                   "ラングランド『農夫ピアズの幻』、近代のパスカル・アリエス『時の歴史』、"
                   "シュルレアリスム文学までの夢物語系譜。",
    "historical_context": "中世における主観的体験の形式的器。",
    "primary_source_url": "https://romandelarose.org/",
    "primary_source_type": "Roman de la Rose Digital Library",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アーサー王物語サイクル",
    "name_en": "Arthurian cycle",
    "name_original": "matière de Bretagne",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "ジョフロア・モンマス『ブリタニア列王史』（c.1136）以後展開した、"
                  "アーサー王と円卓の騎士をめぐる物語群の総体。"
                  "ヴァース『ブリュ物語』、クレチアン・ド・トロワ韻文ロマン群、"
                  "13世紀『ヴルガータ・サイクル』『ランスロ＝聖杯散文サイクル』、"
                  "マロリー『アーサー王の死』へと500年にわたり拡張された。"
                  "「ブルターニュ素材」（matière de Bretagne）として中世文学三大素材の一を成す。",
    "background": "ケルト・アイルランド／ウェールズ伝承（『マビノギオン』『カンブリア年代記』）が"
                  "12世紀ノルマン宮廷で文学化された。",
    "development": "中世全ヨーロッパに翻案・拡張。近代ではテニソン『国王牧歌』、"
                   "T・H・ホワイト『永遠の王』、トールキン中つ国神話まで継承。"
                   "現代ファンタジー・映画文化の主要源泉。",
    "historical_context": "中世西欧の集合的物語想像力の最大の達成。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b6000951c",
    "primary_source_type": "Gallica BnF — Lancelot-Grail manuscripts",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "アーサー王神話",
         "description": "神話DBが扱う中世西欧最大の英雄物語サイクル。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "騎士道文化",
         "description": "人類学DBが扱う中世騎士道文化の文学的結晶。"},
    ],
})

add({
    "name_ja": "聖杯ロマンス",
    "name_en": "Grail romance",
    "name_original": "queste del saint graal",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "アーサー王物語サイクル内の聖杯探求物語群。"
                  "クレチアン・ド・トロワ『ペルスヴァル』が起源。"
                  "ロベール・ド・ボロン『ジョセフ・ダリマティ』『メルラン』『ペルスヴァル』が"
                  "聖杯をキリストの聖盃と同定する神秘主義的伝承を確立。"
                  "13世紀『散文聖杯探求』ではガラハドが純潔な完成者として登場する。",
    "background": "ケルト・アイルランド「dagda の大釜」「再生の鍋」伝承と、"
                  "キリスト教の聖体・聖遺物崇敬が13世紀で融合した。",
    "development": "マロリー『アーサー王の死』への中核物語、"
                   "ワーグナー『パルジファル』、テニソン『聖杯』、"
                   "エリオット『荒地』、ジョン・ボーマン『エクスカリバー』まで。",
    "historical_context": "中世神秘主義と騎士道倫理の文学的結晶。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b105389851",
    "primary_source_type": "Gallica BnF — Queste del Saint Graal manuscripts",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "獣寓話の中世復興",
    "name_en": "beast fable revival",
    "name_original": "fabula bestiarum / Roman de Renart",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "中世における動物寓話・諷刺ジャンルの大規模復興。"
                  "古フランス語『狐物語』（Roman de Renart, 12-13世紀）が中核作品で、"
                  "狐ルナールを主役にする30余の枝編が宮廷・教会・封建社会を諷刺。"
                  "イソップ寓話の中世継承（『マリーのイソペット』）、"
                  "中世動物誌（bestiarium）と並行発展した。",
    "background": "古典イソップ寓話・古代インド『パンチャタントラ』伝承の中世西欧での合流。",
    "development": "ゲーテ『狐ライネケ』、ラ・フォンテーヌ『寓話詩』、"
                   "近代児童文学（『狐物語』再話）まで広く継承される。",
    "historical_context": "中世における動物寓話を社会諷刺装置として再活用した文化現象。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b8451626r",
    "primary_source_type": "Gallica BnF — Roman de Renart manuscripts",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "神秘劇（ミステリー・サイクル）",
    "name_en": "mystery cycles",
    "name_original": "mystères / sacre rappresentazioni",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世晩期（14-15世紀）",
    "definition": "中世末期に発達した宗教劇ジャンル。"
                  "聖書物語（創世から最後の審判まで）を都市祭典で連続上演する大規模演劇。"
                  "イタリアの sacre rappresentazioni、フランスの mystères、"
                  "イングランドのコーパス・クリスティ・サイクル（ヨーク・チェスター・"
                  "ウェイクフィールド・Nタウン）等が代表例。",
    "background": "教会典礼劇（典礼諷諭劇）が13-14世紀に都市職能組合主催の大規模俗語劇へ拡張。",
    "development": "宗教改革による禁止後途絶するが、近代に文献研究・再演運動が再興。"
                   "現代のオーバーアマガウ受難劇・ベンジャミン・ブリテンのオペラ化等で継承。",
    "historical_context": "中世末期都市文化と宗教文化の総合的祭典。",
    "primary_source_url": "https://archive.org/details/playsofourforefa00gayl",
    "primary_source_type": "Internet Archive — Plays of Our Forefathers",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "奇蹟劇（ミラクル・プレイ）",
    "name_en": "miracle plays",
    "name_original": "miracles de Notre Dame",
    "original_script": "roman",
    "subfield_code": "lit_eu_medieval",
    "region": "西欧",
    "period_key": "中世盛期後期（13世紀）",
    "definition": "中世末期に発達した宗教劇ジャンルで、聖人・聖母の奇蹟譚を主題とする。"
                  "フランスでは『ノートルダムの奇蹟劇集』（Miracles de Notre Dame, 14世紀）の"
                  "40篇が伝存。聖母マリアが地上の罪人を救済する物語を、"
                  "宗教祭典と都市的娯楽の双方として上演した。",
    "background": "聖母マリア崇敬の高揚、聖遺物巡礼・市場文化の活性化、"
                  "都市職能組合の祭典後援が条件となった。",
    "development": "中世末期から近世への過渡期に世俗劇（モラリテ・farce）への分化。"
                   "シェイクスピア劇への遠い遺産。",
    "historical_context": "中世末期の聖母崇敬文化と都市演劇の交差。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/btv1b8451591x",
    "primary_source_type": "Gallica BnF — Miracles de Notre Dame manuscripts",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ---------------------------------------------------------------
# Relations between concepts (within this batch)
# ---------------------------------------------------------------

RELATIONS: list[tuple[str, str, str, str]] = [
    # A. Chivalric epic / lyric internal lineage
    ("ロランの歌", "シャンソン・ド・ジェスト", "exemplifies",
     "ロランの歌はシャンソン・ド・ジェストの最古かつ範例的作品。"),
    ("トルバドゥール抒情詩", "プロヴァンス抒情詩", "exemplifies",
     "プロヴァンス抒情詩はトルバドゥール詩の言語的総体を指す。"),
    ("トルヴェール", "トルバドゥール抒情詩", "extends",
     "トルヴェールは北仏オイル語圏でのトルバドゥール詩の継承形態。"),
    ("ドルチェ・スティル・ノーヴォ", "宮廷恋愛（フィナモール）", "extends",
     "ドルチェ・スティル・ノーヴォは宮廷恋愛の哲学的・神学的深化。"),
    ("ドルチェ・スティル・ノーヴォ", "プロヴァンス抒情詩", "extends",
     "ドルチェ・スティル・ノーヴォはプロヴァンス・シチリア派抒情詩を哲学化した。"),
    ("シルヴァンテス（諷刺歌）", "トルバドゥール抒情詩", "exemplifies",
     "シルヴァンテスはトルバドゥール詩の主要諷刺ジャンル。"),

    # B. Romance & narrative
    ("クレチアン・ド・トロワ『ランスロ』", "ロマン・クルトワ（宮廷ロマン）", "exemplifies",
     "ランスロはクレチアン作のロマン・クルトワの典型作品。"),
    ("クレチアン・ド・トロワ『ペルスヴァル』", "ロマン・クルトワ（宮廷ロマン）", "exemplifies",
     "ペルスヴァルはクレチアン作のロマン・クルトワで聖杯主題を導入。"),
    ("クレチアン・ド・トロワ『ランスロ』", "宮廷恋愛（フィナモール）", "exemplifies",
     "ランスロは宮廷恋愛規範の物語的極限化。"),
    ("クレチアン・ド・トロワ『ペルスヴァル』", "聖杯ロマンス", "precedes",
     "ペルスヴァルが聖杯ロマンス全体の起点となる。"),
    ("聖杯ロマンス", "アーサー王物語サイクル", "exemplifies",
     "聖杯ロマンスはアーサー王サイクル内の中核物語群。"),
    ("トリスタンとイズー", "ロマン・クルトワ（宮廷ロマン）", "exemplifies",
     "トリスタンとイズーはロマン・クルトワの極限的悲恋作品。"),
    ("ロマン・ド・ラ・ローズ", "夢物語（寓意夢）", "exemplifies",
     "ロマン・ド・ラ・ローズは夢物語形式の最も影響力ある作例。"),
    ("ロマン・ド・ラ・ローズ", "中世寓意解釈（アレゴレシス）", "exemplifies",
     "ロマン・ド・ラ・ローズは中世寓意解釈の文学的応用。"),
    ("ボッカッチョ『デカメロン』", "ノヴェッラの起源", "exemplifies",
     "デカメロンはノヴェッラ・ジャンルの完成形を確立。"),
    ("ボッカッチョ『デカメロン』", "ファブリオー", "extends",
     "デカメロン中の滑稽話はファブリオー伝統の散文化継承。"),
    ("エクセンプルム（説教例話）", "ノヴェッラの起源", "precedes",
     "エクセンプルムは中世説教話の世俗化を経てノヴェッラの素材源となる。"),
    ("ファブリオー", "ノヴェッラの起源", "precedes",
     "ファブリオーは韻文滑稽話としてノヴェッラの直接的祖型。"),

    # C. Italian medieval lineage
    ("シチリア派抒情詩", "ドルチェ・スティル・ノーヴォ", "precedes",
     "シチリア派が13世紀後半のドルチェ・スティル・ノーヴォの直接的祖。"),
    ("カヴァルカンティの抒情詩", "ドルチェ・スティル・ノーヴォ", "exemplifies",
     "カヴァルカンティはドルチェ・スティル・ノーヴォの中心的範例。"),
    ("ダンテ『新生』", "ドルチェ・スティル・ノーヴォ", "exemplifies",
     "新生はドルチェ・スティル・ノーヴォの集大成。"),
    ("ダンテ『新生』", "ダンテ『神曲』", "precedes",
     "新生のベアトリーチェ像が神曲の霊的役割の伏線。"),
    ("ダンテ『神曲』", "中世寓意解釈（アレゴレシス）", "exemplifies",
     "神曲は中世寓意解釈の文学的最高総合。"),
    ("ダンテ『神曲』", "聖書四義（四重解釈）", "exemplifies",
     "神曲は聖書四義を世俗詩に適用した最初の体系例。"),
    ("ペトラルカ『カンツォニエーレ』", "ダンテ『新生』", "extends",
     "カンツォニエーレは新生型の伝記的恋愛詩集を内省的抒情詩へ深化。"),
    ("ペトラルカ『カンツォニエーレ』", "ペトラルキスム前駆", "precedes",
     "カンツォニエーレが後世ペトラルキスム運動の祖型となる。"),
    ("ヤコポーネ・ダ・トーディのラウダ", "ドルチェ・スティル・ノーヴォ", "parallels",
     "13世紀後半のフランチェスコ会霊性詩はドルチェ・スティル・ノーヴォと並行する宗教抒情詩潮流。"),
    ("ボッカッチョ『名婦伝』", "宮廷恋愛論争", "precedes",
     "名婦伝はクリスティーヌ・ド・ピザン『淑女の都市』の直接的参照源。"),

    # D. Poetics
    ("聖書四義（四重解釈）", "中世寓意解釈（アレゴレシス）", "exemplifies",
     "聖書四義は中世寓意解釈の体系化された4層モデル。"),
    ("ダンテ『俗語論』", "ダンテ『神曲』", "precedes",
     "俗語論の理論的探究が神曲の俗語選択を支える。"),
    ("ブルネット・ラティーニ", "ダンテ『神曲』", "influences",
     "ブルネットはダンテの師として俗語的知の総合化を伝授。"),
    ("アクィナスの美学", "ダンテ『神曲』", "influences",
     "アクィナスの美学体系がダンテの世界観の哲学的支柱。"),
    ("フィナモールの詩規範", "宮廷恋愛（フィナモール）", "exemplifies",
     "フィナモールの詩規範はカペッラヌス『恋愛論』に体系化された宮廷恋愛の法典。"),
    ("ジョク・パルティ（恋愛論争詩）", "トルバドゥール抒情詩", "exemplifies",
     "ジョク・パルティはトルバドゥール詩の対論ジャンル。"),
    ("アルス・ディクタミニス（書記技法）", "ダンテ『俗語論』", "precedes",
     "アルス・ディクタミニスの修辞学体系がダンテの俗語論的考察を準備した。"),

    # E. Genres / themes
    ("レー（ブルトン・レー）", "アーサー王物語サイクル", "parallels",
     "ブルトン・レーはアーサー王物語サイクルと並行する中世短編幻想物語。"),
    ("獣寓話の中世復興", "ファブリオー", "parallels",
     "獣寓話とファブリオーは中世盛期の俗語諷刺文学の双子的ジャンル。"),
    ("神秘劇（ミステリー・サイクル）", "奇蹟劇（ミラクル・プレイ）", "parallels",
     "神秘劇と奇蹟劇は中世末期都市宗教劇の二大ジャンル。"),
    ("夢物語（寓意夢）", "中世寓意解釈（アレゴレシス）", "exemplifies",
     "夢物語は中世寓意解釈を物語形式に応用した中核ジャンル。"),
    ("宮廷恋愛論争", "ロマン・ド・ラ・ローズ", "criticizes",
     "宮廷恋愛論争はクリスティーヌ・ド・ピザンによる薔薇物語批判から開始された。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[wave9_c03_medieval_romance] inserting {len(CONCEPTS)} concepts...")
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
                    print(f"  [warn] axis tag failed for "
                          f"{entry['name_ja']}: {e}")

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
                    print(f"  [warn] cross_domain failed for "
                          f"{entry['name_ja']}: {e}")

        # 3) Insert relations
        for src_name, tgt_name, rtype, desc in RELATIONS:
            sid = name_to_id.get(src_name)
            tid = name_to_id.get(tgt_name)
            if not sid or not tid:
                print(f"  [warn] relation skipped: {src_name!r} -> "
                      f"{tgt_name!r} (sid={sid}, tid={tid})")
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
        print("[wave9_c03_medieval_romance] inserted:")
        print(f"  concepts: {summary['concepts']}")
        print(f"  fourth_transform_tags: {summary['fourth_transform_tags']} "
              f"(this run: +{fourth_count})")
        print(f"  cross_domain: {summary['cross_domain']} "
              f"(this run: +{cd_count})")
        print(f"  relations: {summary['relations']} "
              f"(this run: +{relation_count})")
        print(f"  source_tier dist: {db.tier_distribution()}")
        print(f"  coverage (lit_eu_medieval):")
        for r in db.coverage_by_subfield():
            if r["code"] == "lit_eu_medieval":
                print(f"    {r}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
