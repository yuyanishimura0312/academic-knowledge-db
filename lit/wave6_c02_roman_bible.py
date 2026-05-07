"""
LIT-DB Phase 2 — C02: Classical Roman & Biblical Literature
================================================================
Inserts 40 canonical concepts spanning 5 categories:
  A. Roman epic / major poets (8)
  B. Roman lyric / satire (8)
  C. Roman prose (8)
  D. Biblical literature (8)
  E. Criticism / rhetoric / major themes (8)

All entries are sourced from public-domain primary sources:
  - Perseus Digital Library (Latin authors, esp. Vergil, Ovid, Cicero, Tacitus, Livy)
  - Project Gutenberg (Loeb-style PD translations, English KJV)
  - Sefaria (Tanakh — Psalms, Song of Songs, Job, prophets — open license)
  - Bible Hub / Bible Gateway / Greek New Testament (parables, beatitudes, gospels)

Pattern: P1 (Canonical Primary Pursuit) extended with P3 (Cross-tradition
parallel) for biblical material. Subfield: lit_eu_classical (subfield_id=1)
for both Roman and biblical literature, region=西欧.

Zero overlap with C01 Greek (Homer/Sappho/tragedy/Aristotle Poetics etc.).
This file covers the LATIN and BIBLICAL canon only.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (Roman + biblical)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    # name_ja, name_en, start, end, description
    ("ローマ共和政後期", "Late Roman Republic", -100, -27,
     "キケロ、カトゥッルス、ルクレーティウスが活動した内戦期。"
     "ギリシャ詩学・哲学のラテン化が進み、ラテン散文・抒情詩が確立。"),
    ("アウグストゥス時代", "Augustan Age", -27, 14,
     "ウェルギリウス・ホラティウス・オウィディウス・ティブッルス・"
     "プロペルティウスが活動したラテン詩黄金期。帝政の樹立とともに国民叙事詩が成立。"),
    ("帝政ローマ時代（白銀期）", "Silver Age of Latin", 14, 200,
     "セネカ・ルカヌス・ペトロニウス・ユウェナリス・タキトゥス・"
     "アプレイウスらが活動。修辞学化と政治的諷刺の時代。"),
    ("旧約聖書時代", "Hebrew Bible Period", -1200, -200,
     "ヘブライ語聖書（タナハ）の編纂期。詩篇・雅歌・ヨブ記・預言書文学が成立。"),
    ("新約聖書時代", "New Testament Period", 30, 110,
     "コイネ・ギリシャ語による福音書・書簡・黙示録の成立期。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — Roman epic / major poets (8)
# ===============================================================

add({
    "name_ja": "ウェルギリウス『アエネーイス』",
    "name_en": "Vergil, Aeneid",
    "name_original": "Aeneis",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "ウェルギリウス（前70-19）が前29-19年にかけて執筆したラテン国民叙事詩。"
                  "12巻・約9,896行のヘクサメター詩で、トロイア陥落後のアエネーアスがイタリアに"
                  "渡りローマ建国の祖となる経緯を歌う。ホメロス『イリアス』『オデュッセイア』"
                  "を統合的に再構成し、運命（fatum）と義務（pietas）の主題を中核に据える。",
    "background": "前27年のオクタウィアヌスによる元首政樹立を文学的に基礎づけるため、"
                  "アウグストゥス自身の支援を受けて執筆。詩人は完成前に死去し未完のまま伝来。",
    "development": "中世ではキリスト教的アレゴリーで読まれ（フルゲンティウス、ベルナール）、"
                   "ダンテ『神曲』の案内人ウェルギリウスとして登場。"
                   "ルネサンス国民叙事詩（カモンイス、タッソ）、ミルトン『失楽園』、"
                   "近代ではエリオット「ウェルギリウスとは何か」が古典的範例性を再定義。",
    "historical_context": "アウグストゥス帝政の文化的正統化装置として機能した。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0055",
    "primary_source_type": "Perseus — Vergil Aeneid",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "アエネーイスは2000年にわたり西欧国民叙事詩の正典範例として君臨してきたが、"
                      "ポストコロニアル批評（クィント『叙事詩と帝国』）以降、帝国主義的物語の"
                      "範例として批判的再検討の対象となっている。AI時代の正典再編成議論に直結する。",
         "related_ai_phenomenon": "AIによる正典再編・脱植民地化キュレーション"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "国民叙事詩の範例",
         "description": "詩学DBが扱う「叙事詩の正統性」議論の中核作品。"},
    ],
})

add({
    "name_ja": "ウェルギリウス『牧歌』",
    "name_en": "Vergil, Eclogues",
    "name_original": "Eclogae / Bucolica",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "ローマ共和政後期",
    "definition": "ウェルギリウスが前42-37年に執筆した10篇の田園詩集。"
                  "テオクリトスの牧歌を範例としつつ、内戦期イタリアの土地没収・追放という"
                  "歴史的現実を背景に、羊飼いの対話・歌合わせ・予言を交えた田園世界を描く。"
                  "第4牧歌は「処女が新時代の子を生む」という予言的詩でキリスト教的解釈を受けた。",
    "background": "フィリッピの戦い（前42）後の退役兵への土地分配でウェルギリウス自身が"
                  "土地を失った経験が反映される。",
    "development": "ルネサンスのパストラル劇（サナザロ『アルカディア』、シドニー）、"
                   "ミルトン『リシダス』、ペトラルカの牧歌書簡など、田園文学の祖型として継承。",
    "historical_context": "内戦期の社会的混乱を詩的田園で象徴的に解決する文学装置。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0056",
    "primary_source_type": "Perseus — Vergil Eclogues",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ウェルギリウス『農耕詩』",
    "name_en": "Vergil, Georgics",
    "name_original": "Georgica",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "ローマ共和政後期",
    "definition": "ウェルギリウスが前37-29年に執筆した4巻の教訓詩。"
                  "穀物耕作・果樹・家畜・養蜂を主題に、ヘシオドス『労働と日々』を範例としつつ、"
                  "農村労働の倫理的尊厳と内戦による農村疲弊からの再建を主題化する。"
                  "結尾のオルペウス・エウリュディケー神話挿話で詩人と詩作の意味を内省する。",
    "background": "アクティウムの海戦（前31）前後の執筆。マエケーナースの庇護下に成立。",
    "development": "近代では農村労働の理想化・反工業化文学（ヴァージル復興）、"
                   "現代エコクリティシズム（ジェイ・パリーニ等）が再評価。",
    "historical_context": "アウグストゥス的「ローマ復興」イデオロギーへの詩的応答。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0058",
    "primary_source_type": "Perseus — Vergil Georgics",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "オウィディウス『変身物語』",
    "name_en": "Ovid, Metamorphoses",
    "name_original": "Metamorphoses",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "オウィディウス（前43-後17）が後8年ごろに完成させた15巻のヘクサメター叙事詩。"
                  "宇宙創成から自身の時代までの神話を「変身（metamorphosis）」を主題に約250篇繋ぎ、"
                  "ナルキッソス・ピュグマリオーン・ピュラモスとティスベー・ダフネ・"
                  "アクタイオーン・ピュロムネーラ等、後世西欧文化の神話的辞典となった。",
    "background": "アウグストゥスによる流刑直前の執筆。詩人は完成と同時に黒海沿岸に追放された。",
    "development": "中世のオウィディウス・モラリゼ、ボッカッチョ、シェイクスピア（『ヴィーナスと"
                   "アドニス』『夏の夜の夢』）、テッド・ヒューズ『オウィディウスからの物語』、"
                   "現代の作家マリ・テリオが再話文学の祖型として活用。",
    "historical_context": "アウグストゥス帝政の道徳改革と詩的官能性の緊張を体現。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0028",
    "primary_source_type": "Perseus — Ovid Metamorphoses",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "「変身」を物語生成原理に据えた構造は、AI生成テクストの可塑性・流動性"
                      "（テクスト＝シェイプシフター）と構造的に類比される。",
         "related_ai_phenomenon": "AI生成における人物・場面の連続変容"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "変身譚（metamorphosis）",
         "description": "人類学DBが扱う変身譚・人獣変容神話の西欧古典的源泉。"},
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "ローマ神話アンソロジー",
         "description": "西欧神話DBの中核ソース。約250篇の神話を結節する辞典として機能。"},
    ],
})

add({
    "name_ja": "オウィディウス『名婦の手紙』",
    "name_en": "Ovid, Heroides",
    "name_original": "Heroides / Epistulae Heroidum",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "オウィディウスが神話の女性英雄たち（ペーネロペー、ディードー、メーディア、"
                  "サッポー等）が不在の男に宛てて書いたという設定の擬書簡詩集。"
                  "21篇のエレギーア・ディスティコンで、女性視点の独白を独立詩ジャンルとして確立した。",
    "background": "ヘレニズム期の擬書簡修辞演習を文学的ジャンルに昇華させた。",
    "development": "中世の女性嘆き詩、ルネサンスのペトラルカ風書簡詩、ポープ『エロイーザから"
                   "アベラールへ』、リルケ『ドゥイノの悲歌』までの「女性独白」系譜の祖。",
    "historical_context": "ローマ的男性英雄叙事詩への女性視点による応答。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0085",
    "primary_source_type": "Perseus — Ovid Heroides",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ルカヌス『内乱記（ファルサーリア）』",
    "name_en": "Lucan, Pharsalia (Bellum Civile)",
    "name_original": "Bellum Civile / Pharsalia",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "ルカヌス（後39-65）の未完叙事詩10巻。カエサルとポンペイウスの内戦を主題とし、"
                  "ウェルギリウス『アエネーイス』の楽観的国民叙事詩に対し、神々を排し人間的"
                  "悲劇として共和政の崩壊を歌う「反叙事詩」。ストア哲学的英雄カトーが道徳的中心。",
    "background": "ネロー帝の宮廷詩人だったが、ピーソー陰謀事件に連座し25歳で自殺命令を受け死去。",
    "development": "ダンテ『神曲』、シェイクスピア『ジュリアス・シーザー』への影響、"
                   "近代では英雄主義への懐疑詩の祖として再評価（マサーズ、フランケル）。",
    "historical_context": "ネロー帝期の専制への詩的抵抗としての反帝政叙事詩。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0134",
    "primary_source_type": "Perseus — Lucan Pharsalia",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "スタティウス『テーバイス』",
    "name_en": "Statius, Thebaid",
    "name_original": "Thebais",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "スタティウス（後45-96）が後80-92年に完成させた12巻のヘクサメター叙事詩。"
                  "オイディプスの息子エテオクレースとポリュネイケースの兄弟相剋とテーバイ攻めの七将を歌う。"
                  "ウェルギリウスを範例としつつ、ストア哲学的内面化と修辞的技巧を強化した白銀期の代表作。",
    "background": "ドミティアーヌス帝期の宮廷文化のもとで執筆。",
    "development": "ダンテ『神曲』煉獄篇でスタティウス自身が登場し、改宗詩人として再話される。"
                   "中世ロマンス『テーバイ物語』、チョーサー『騎士物語』に接続。",
    "historical_context": "白銀期ラテン詩の修辞的洗練と心理主義の極致。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0136",
    "primary_source_type": "Perseus — Statius Thebaid",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "シリウス・イタリクス『プニカ』",
    "name_en": "Silius Italicus, Punica",
    "name_original": "Punica",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "シリウス・イタリクス（後26-101）が著した17巻・12,200行に及ぶ古代ラテン文学最長の"
                  "叙事詩。第二次ポエニ戦争（前218-201）を主題とし、ハンニバルとスキピオ・"
                  "アフリカヌスの対決を歌う。ウェルギリウスを忠実に範例とした歴史叙事詩の白銀期代表作。",
    "background": "元老院議員から退いて文学に専念。リウィウス『ローマ建国史』を主要素材源とした。",
    "development": "中世にはほぼ忘却されたが、1417年ポッジョ・ブラッチョリーニによって写本が"
                   "再発見され、ルネサンス国民叙事詩の重要参照点となった。",
    "historical_context": "ドミティアヌス帝期の歴史回顧的文化の代表的成果。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/47559",
    "primary_source_type": "Gutenberg — Punica (Loeb edition derivative)",
    "importance_score": 2,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})


# ===============================================================
# CATEGORY B — Roman lyric / satire (8)
# ===============================================================

add({
    "name_ja": "ホラティウス『歌章（カルミナ）』",
    "name_en": "Horace, Odes (Carmina)",
    "name_original": "Carmina",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "ホラティウス（前65-8）の4巻103篇からなる抒情詩集。"
                  "アルカイオス・サッポー・アナクレオン等のギリシャ抒情詩韻律をラテン語で再現し、"
                  "carpe diem（今を摘め）、aurea mediocritas（黄金の中庸）、"
                  "exegi monumentum（私は記念碑を建てた）等、西欧文学の不朽の標語を生んだ。",
    "background": "前23年に巻1-3、後13年に巻4を発表。アウグストゥス・マエケーナースの庇護下。",
    "development": "ペトラルカ、ロンサール、ホプキンズ、オーデン、近代では「ホラティウス的中庸」"
                   "として人生哲学のシンボルとなる。日本では森鴎外がカルミナを訳出。",
    "historical_context": "アウグストゥス的市民倫理と詩的個人性の調和の頂点。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0024",
    "primary_source_type": "Perseus — Horace Odes",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "カトゥッルス抒情詩集",
    "name_en": "Catullus, Carmina",
    "name_original": "Catulli Veronensis Liber",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "ローマ共和政後期",
    "definition": "カトゥッルス（前84-54）の現存116篇からなる詩集。"
                  "アレクサンドリア新詩派（neoteroi）の指導者として、レスビアへの愛と憎しみ、"
                  "友情、政敵への諷刺、神話的小叙事詩を多様な韻律で歌う。"
                  "「odi et amo（愛と憎しみ）」（85番）が個人的情念詩の祖型を確立した。",
    "background": "ヴェローナの裕福な家系出身。キケロ世代のローマ知識人サークルで活動。",
    "development": "中世ではほぼ忘却されたが、1300年頃ヴェローナで写本再発見。"
                   "ペトラルカ、シェイクスピアのソネット、ロマン派、エズラ・パウンドが"
                   "個人的情熱詩の範例として継承。",
    "historical_context": "ヘレニズム的個人主義詩学のラテン化の先駆。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0003",
    "primary_source_type": "Perseus — Catullus Carmina",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "プロペルティウス恋愛悲歌",
    "name_en": "Propertius, Elegies",
    "name_original": "Elegiae",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "プロペルティウス（前50-15）が前28-16年に発表した4巻の恋愛悲歌集。"
                  "キュンティアという詩的女主人公への激しい愛と苦悩を、神話的範例で装飾しつつ"
                  "歌う。難解で錯綜した修辞と熱情的告白の独自性で、後世の悲歌詩学に強い影響を与えた。",
    "background": "ウンブリア出身、マエケーナース・サークルに参加。",
    "development": "ペトラルカ、英国メタフィジカル詩、エズラ・パウンド『プロペルティウスへの"
                   "オマージュ』が直接的継承。",
    "historical_context": "ローマ恋愛悲歌（elegia amatoria）ジャンルの確立期。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0028",
    "primary_source_type": "Perseus — Propertius Elegies",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ティブッルス恋愛悲歌",
    "name_en": "Tibullus, Elegies",
    "name_original": "Elegiae",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "ティブッルス（前55-19）の2巻16篇の悲歌集。"
                  "デリアおよびネメシスへの愛、田園回帰の理想、戦争への嫌悪を、清澄で抑制された"
                  "ラテン語で歌う。クインティリアヌスはローマ悲歌詩人の最良としてティブッルスを挙げた。",
    "background": "騎士階級の詩人。マッサーラ・コルウィーヌス・サークルに参加。",
    "development": "ルネサンス田園詩、ゲーテ『ローマ悲歌』、近代の田園回帰詩学に影響。",
    "historical_context": "アウグストゥス期の田園的理想化と恋愛悲歌の融合。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0078",
    "primary_source_type": "Perseus — Tibullus Elegies",
    "importance_score": 2,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "マルティアリス『エピグランマタ』",
    "name_en": "Martial, Epigrams",
    "name_original": "Epigrammata",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "マルティアリス（後38-104）の12巻約1,500篇のエピグラム集。"
                  "短く鋭い諷刺・卑猥詩・追悼詩を集成し、「pointed wit（要点を突く機知）」を"
                  "特徴とする近代エピグラムの祖。ローマ社会の悪徳・偽善を瞬間的に切り取る。",
    "background": "スペイン出身、ローマで活動。ドミティアヌス・トラヤヌス両帝に詩を献じた。",
    "development": "ルネサンスの新ラテン語エピグラム、英国18世紀の風刺詩、現代の警句文学に直結。",
    "historical_context": "白銀期ローマの過剰社会への諷刺的鏡像。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0506",
    "primary_source_type": "Perseus — Martial Epigrams",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ユウェナリス諷刺詩",
    "name_en": "Juvenal, Satires",
    "name_original": "Saturae",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "ユウェナリス（後60-130頃）の16篇からなる諷刺詩集。"
                  "ローマ帝政期の腐敗・偽善・浪費・女性の堕落を「saeva indignatio（激しい義憤）」で"
                  "鞭打つ。「panem et circenses（パンとサーカス）」「quis custodiet ipsos custodes"
                  "（番人を誰が見張るか）」等、政治批判の不朽の格言を生んだ。",
    "background": "ドミティアヌス帝期に追放された経験を背景とする推測。",
    "development": "ジョンソン『ロンドン』、ドライデン『ジュヴェナル諷刺詩集』英訳、"
                   "近代社会諷刺の範例。",
    "historical_context": "帝政ローマの社会的不安と道徳的批判精神の頂点。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a2008.01.0498",
    "primary_source_type": "Perseus — Juvenal Satires",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ペルシウス諷刺詩",
    "name_en": "Persius, Satires",
    "name_original": "Saturae",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "ペルシウス（後34-62）の6篇からなる短い諷刺詩集。"
                  "ストア哲学的厳格さと密度の高い暗示的言語で、自己認識・徳・詩の頽廃を批判する。"
                  "ホラティウスの寛容な諷刺とユウェナリスの激しい批判の中間に位置する独自の知的諷刺。",
    "background": "ストア哲学者コルヌートゥスに師事。28歳で病没し詩集は遺稿として刊行。",
    "development": "中世にはホラティウスより人気を博し、ジョン・ダンの諷刺詩、エリオットの"
                   "知的密度の高い詩学に間接的影響。",
    "historical_context": "ネロー帝期のストア哲学的反逆精神の文学的表現。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a2008.01.0500",
    "primary_source_type": "Perseus — Persius Satires",
    "importance_score": 2,
    "source_tier": "primary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "ホラティウス『詩論』",
    "name_en": "Horace, Ars Poetica",
    "name_original": "Ars Poetica / Epistula ad Pisones",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "ホラティウスが後期に書いた476行の詩体書簡で、後の文芸批評の根本テクスト。"
                  "詩の統一性（unitas）、適切性（decorum）、教えと愉しみ（prodesse et delectare）、"
                  "ut pictura poesis（詩は絵のごとく）等、西欧詩学の根本概念を体系化した。",
    "background": "ピーソー父子に宛てた書簡形式。アリストテレス『詩学』のローマ的継承を意図。",
    "development": "中世は失われていたが、ルネサンスで再発見されてヴィーダ、スカリゲル、"
                   "ボワロー『詩論』、ポープ『批評論』など近代詩学の規範書として支配的影響力を持った。",
    "historical_context": "ギリシャ詩学のラテン化と教育的体系化の頂点。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0064",
    "primary_source_type": "Perseus — Horace Ars Poetica",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "詩学規範書",
         "description": "詩学DBが扱う規範批評の起源テクスト。"},
    ],
})


# ===============================================================
# CATEGORY C — Roman prose (8)
# ===============================================================

add({
    "name_ja": "キケロ修辞学（弁論術）",
    "name_en": "Cicero, rhetoric",
    "name_original": "rhetorica",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "ローマ共和政後期",
    "definition": "キケロ（前106-43）が確立したラテン修辞学の体系。"
                  "ギリシャの弁論術理論をラテン語化し、inventio（題材発見）・dispositio（配置）・"
                  "elocutio（措辞）・memoria（記憶）・actio（演技）の五段階、"
                  "三文体（plain/middle/grand）など修辞学の基本枠組みを定式化した。",
    "background": "アテネ・ロドスでギリシャ修辞学を学んだ後、ローマ法廷弁論で活躍。",
    "development": "中世のtrivium（文法・論理・修辞）の中核教材、ルネサンス・ヒューマニズムの"
                   "教育的中核（エラスムス、メランヒトン）として支配的影響を保った。",
    "historical_context": "共和政末期の政治的弁論文化の集大成。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0011",
    "primary_source_type": "Perseus — Cicero rhetorical works",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "古典修辞学",
         "description": "哲学DBが扱う修辞学・論理学・倫理学の交差点。"},
    ],
})

add({
    "name_ja": "キケロ『弁論家論』",
    "name_en": "Cicero, De Oratore",
    "name_original": "De Oratore",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "ローマ共和政後期",
    "definition": "キケロが前55年に著した3巻の対話篇形式の弁論術論。"
                  "理想的弁論家（vir bonus dicendi peritus＝語ることに長けた善き人）が、"
                  "哲学・歴史・法学を統合した教養ある全人格者であるべきとする「ヒューマニズム的"
                  "弁論観」を提示し、後世の文芸教育観の根幹を形成した。",
    "background": "クラッスス・アントニウスらローマ大物弁論家の対話として構成。",
    "development": "ペトラルカ、ブルーニ、ヴィットリーノら15世紀ヒューマニストが教養理想として"
                   "再発見。近代リベラル・アーツ教育の思想的源泉。",
    "historical_context": "ローマ共和政エリート教養理想の体系化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0120",
    "primary_source_type": "Perseus — Cicero De Oratore",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "borrowed_from",
         "target_entity_name": "ヒューマニズム的教養理念",
         "description": "哲学DBの教養理念・liberal arts論の起点。"},
    ],
})

add({
    "name_ja": "クインティリアヌス『弁論家の教育』",
    "name_en": "Quintilian, Institutio Oratoria",
    "name_original": "Institutio Oratoria",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "クインティリアヌス（後35-100）が後95年頃に完成させた12巻の修辞学・教育論大全。"
                  "幼児期からの全人的教育プログラム（書字・文法・修辞）を体系化し、"
                  "「vir bonus dicendi peritus（語る術に長けた善き人）」をキケロ以上に明示的に"
                  "教育目標として定式化した。",
    "background": "ウェスパシアヌス帝期に公費修辞学教師として20年活動した経験を集成。",
    "development": "中世前半は失われていたが、1416年ポッジョが完全本を再発見。"
                   "ルネサンス・ヒューマニズム教育（エラスムス、ヴィーヴェス）の規範書として"
                   "支配的影響、近代教育学の祖。",
    "historical_context": "帝政期の修辞学校制度の体系化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a2007.01.0059",
    "primary_source_type": "Perseus — Quintilian Institutio Oratoria",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "修辞学体系",
         "description": "詩学・修辞学DBの体系教材としての中核ソース。"},
    ],
})

add({
    "name_ja": "タキトゥス歴史叙述",
    "name_en": "Tacitus, historiography",
    "name_original": "Annales / Historiae",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "タキトゥス（後56-120）の『年代記（Annales）』『同時代史（Historiae）』『ゲルマーニア』"
                  "『アグリコラ』に代表される歴史叙述。簡潔・凝縮・反語的な「タキトゥス的文体」と、"
                  "皇帝政の暴政を解剖する道徳的鋭さで、政治史叙述の最高峰とされる。",
    "background": "元老院議員・属州総督。アグリコラの婿として帝政期上層の内幕を知悉。",
    "development": "ルネサンス『タキトゥス主義』（リプシウス、マキャヴェッリ）、"
                   "近代政治思想（モンテスキュー、ギボン）の根本的範例。",
    "historical_context": "帝政期言論の自由喪失への文学的応答。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0078",
    "primary_source_type": "Perseus — Tacitus Annals/Histories",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "リウィウス『ローマ建国史』",
    "name_en": "Livy, Ab Urbe Condita",
    "name_original": "Ab Urbe Condita Libri",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "リウィウス（前59-後17）が約40年かけて執筆した142巻のローマ通史（35巻が現存）。"
                  "都市建国（前753）から前9年までを物語的に叙述し、ロームルス・"
                  "ホラティウス兄弟・ルクレティア・キンキナトゥス等、ローマ的徳の範例的物語を確立した。",
    "background": "アウグストゥス帝の親しい交友のもと、共和政的徳の称揚を通じて新体制の道徳的"
                  "正統化を図った。",
    "development": "マキャヴェッリ『ディスコルシ・ソプラ・リヴィオ』、シェイクスピア『ルクレティア凌辱』、"
                   "近代国民史叙述の規範。",
    "historical_context": "アウグストゥス的『ローマ復興』の歴史的バックボーン。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0144",
    "primary_source_type": "Perseus — Livy Ab Urbe Condita",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アプレイウス『黄金のロバ』",
    "name_en": "Apuleius, Metamorphoses (Golden Ass)",
    "name_original": "Metamorphoses / Asinus Aureus",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "アプレイウス（後125-180）が後160年頃に著した11巻のラテン語小説。"
                  "好奇心からロバに変身した主人公ルキウスの遍歴と最終的なイシス女神への帰依を描く。"
                  "「クピド（アモル）とプシュケー」の挿話を含む、ラテン語で完全現存する唯一の小説。",
    "background": "北アフリカ・マダウラ出身のプラトン主義哲学者・修辞家。",
    "development": "ボッカッチョ『デカメロン』、セルバンテス、ラ・フォンテーヌが「クピドとプシュケー」"
                   "を再話。ピカレスク小説、近代魔術リアリズムの祖型。",
    "historical_context": "帝政期地中海世界の宗教的混淆（イシス信仰）の文学的記録。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/1666",
    "primary_source_type": "Gutenberg — Apuleius Golden Ass",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ペトロニウス『サテュリコン』",
    "name_en": "Petronius, Satyricon",
    "name_original": "Satyricon",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "ペトロニウス（後27-66）が著したと伝わる断片的小説。"
                  "南イタリアを舞台に、エンコルピウス・アスキュルトス・ギトーンらの遍歴を諷刺的に描く。"
                  "「トリマルキオの饗宴」場面が特に有名で、解放奴隷の暴富社会の戯画として古典的。",
    "background": "ネロー帝の「優雅の判定者（arbiter elegantiae）」と伝わる人物。"
                  "ピーソー陰謀事件で自殺。",
    "development": "T.S.エリオット『荒地』エピグラフ、フェリーニ映画『サテリコン』、"
                   "近代「メニッペア小説」（バフチン）論の中核例。",
    "historical_context": "ネロー帝期の道徳的退廃を諷刺した最高峰のラテン語小説。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/5225",
    "primary_source_type": "Gutenberg — Petronius Satyricon",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "セネカ悲劇",
    "name_en": "Seneca, tragedy",
    "name_original": "Tragoediae",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "セネカ（前4-後65）が著したと伝わる10篇のラテン悲劇（『トロイアの女』『メーディア』"
                  "『パエドラ』『ヘラクレス』『テュエステス』等）。ギリシャ悲劇を継承しつつ、"
                  "極端な情念表現・修辞的独白・残虐場面・幽霊登場を特徴とし、ストア哲学的"
                  "情念批判を背景に置く。",
    "background": "ストア哲学者・ネロー帝の家庭教師。皇帝の自殺命令を受けて死去。"
                  "上演用ではなく朗読用とする説が有力。",
    "development": "ルネサンスのチンツィオ、シェイクスピア（『リチャード三世』『ハムレット』『マクベス』"
                   "の幽霊・流血場面）、フランス古典悲劇（コルネイユ、ラシーヌ）の祖型。",
    "historical_context": "帝政期の修辞学化された悲劇とストア哲学的内省の融合。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a2007.01.0035",
    "primary_source_type": "Perseus — Seneca Tragedies",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ストア哲学的悲劇観",
         "description": "哲学DBが扱うストア派情念論の文学的応用。"},
    ],
})


# ===============================================================
# CATEGORY D — Biblical literature (8)
# ===============================================================

add({
    "name_ja": "詩篇",
    "name_en": "Psalms",
    "name_original": "תְּהִלִּים (Tehillim)",
    "original_script": "hebrew",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "旧約聖書時代",
    "definition": "ヘブライ語聖書（タナハ）「ケトゥヴィーム」の冒頭に置かれる150篇の宗教詩集。"
                  "ダビデ作とされる多くを含み、賛歌・嘆き・感謝・知恵・王の詩篇・預言詩篇等の"
                  "ジャンルを擁する。並行法（parallelismus membrorum）を構造原理とし、"
                  "西欧抒情詩・賛美歌・典礼の祖型となった。",
    "background": "前10世紀から前3世紀にかけて編纂。ダビデ・アーサフ・コラの子等の名が冠される。",
    "development": "ラテン語ウルガータ・聖書、シェイクスピア英訳聖書（KJV）、"
                   "ルター「神はわがやぐら」（詩篇46番）、ホプキンズの宗教詩、"
                   "現代のメシアン宗教音楽まで、西欧抒情詩・宗教音楽の中核源泉。",
    "historical_context": "イスラエル王国・第二神殿期の典礼文化の文学的結晶。",
    "primary_source_url": "https://www.sefaria.org/Psalms.1",
    "primary_source_type": "Sefaria — Tehillim (Hebrew + JPS translation)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "宗教抒情の典礼形式",
         "description": "哲学DB（神学・ユダヤ教学）が扱う祈りの言語的形式の核心。"},
    ],
})

add({
    "name_ja": "雅歌",
    "name_en": "Song of Songs / Song of Solomon",
    "name_original": "שִׁיר הַשִּׁירִים (Shir ha-Shirim)",
    "original_script": "hebrew",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "旧約聖書時代",
    "definition": "ヘブライ語聖書「ケトゥヴィーム」中の8章からなる愛情詩。"
                  "若い男女（伝統的にソロモンとシュラミの女）の対話的恋歌で、"
                  "官能的描写と田園的イメージに満ちる。ユダヤ教ではイスラエル民と神の関係、"
                  "キリスト教ではキリストと教会のアレゴリーとして解釈された。",
    "background": "前6-3世紀の編纂と推定。ソロモン作の伝承は外的帰属。",
    "development": "ベルナルドゥス（クレルヴォーの）の説教、十字架のヨハネ『霊の歌』、"
                   "ハーバート、ロバート・グレイヴズ、トニ・モリスン『ソロモンの歌』など"
                   "宗教的・世俗的恋愛詩の絶えざる源泉。",
    "historical_context": "古代イスラエル世俗詩の聖書正典化の独特の事例。",
    "primary_source_url": "https://www.sefaria.org/Song_of_Songs.1",
    "primary_source_type": "Sefaria — Shir ha-Shirim (Hebrew + JPS)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "雅歌の「世俗恋歌か神への愛か」というアレゴリー解釈の二重性は、"
                      "AI時代における「テクストの多重解釈」「読み手の意図介入」の根本問題に直結する。",
         "related_ai_phenomenon": "AIによるテクスト解釈の多重性提示"},
    ],
})

add({
    "name_ja": "ヨブ記",
    "name_en": "Book of Job",
    "name_original": "אִיּוֹב (Iyyov)",
    "original_script": "hebrew",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "旧約聖書時代",
    "definition": "ヘブライ語聖書「ケトゥヴィーム」の知恵文学。"
                  "義人ヨブが理由なき苦難に襲われ、三人の友人と神義論（神はなぜ義人を苦しめるか）を"
                  "詩的対話で論じる劇詩。最終的に神が嵐の中から答え、人間の理解を超えた創造の壮大さを示す。"
                  "苦難・神義論・知恵の限界を主題とする世界文学屈指の詩劇。",
    "background": "前6-4世紀の編纂と推定。古代近東の知恵文学伝統と接続。",
    "development": "聖アウグスティヌス、ルター、キェルケゴール『反復』、ジュング『ヨブへの応答』、"
                   "アーチボルド・マクリーシュ『J.B.』、エリ・ヴィーゼル等、神義論の根本テクスト。",
    "historical_context": "バビロン捕囚後のイスラエル神学的危機への応答。",
    "primary_source_url": "https://www.sefaria.org/Job.1",
    "primary_source_type": "Sefaria — Iyyov (Hebrew + JPS)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "神義論",
         "description": "哲学DB（宗教哲学）の中核問題「悪の問題」の起点テクスト。"},
    ],
})

add({
    "name_ja": "預言書文学",
    "name_en": "prophetic literature",
    "name_original": "נְבִיאִים (Nevi'im)",
    "original_script": "hebrew",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "旧約聖書時代",
    "definition": "ヘブライ語聖書の第二部「預言書（ネヴィイーム）」を構成する文学ジャンル。"
                  "イザヤ・エレミア・エゼキエル・小預言書12巻に代表される、神の代弁者としての"
                  "預言者が王と民を批判し悔い改めを促す文学。詩と散文の混合、夢・幻視・象徴行為等を含む。",
    "background": "イスラエル・ユダ王国の存続危機（前9-6世紀）と捕囚期の歴史的状況に応答。",
    "development": "新約聖書の福音書・黙示録の母胎、中世のヒルデガルト・フォン・ビンゲン、"
                   "ブレイク『予言詩』、現代のヴァルター・ベンヤミン『歴史哲学テーゼ』まで"
                   "預言的言説の祖型として機能。",
    "historical_context": "古代近東王制への内在的批判の文学装置。",
    "primary_source_url": "https://www.sefaria.org/Isaiah.1",
    "primary_source_type": "Sefaria — Isaiah (Hebrew + JPS)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "譬え話（パラブル）",
    "name_en": "parable",
    "name_original": "παραβολή (parabolē)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "新約聖書時代",
    "definition": "イエスが教えに用いた短い比喩物語の文学形式。"
                  "「種まきのたとえ」「善きサマリア人」「放蕩息子」「失われた羊」等の代表例で、"
                  "日常的場面を通じて天国・救い・倫理を説く。表面的物語と深層的意味の二重性、"
                  "解釈の開放性を特徴とする。",
    "background": "古代近東のヘブライ語マシャル（mashal）伝統に源を持ち、コイネ・ギリシャ語の"
                  "福音書記述で確立。",
    "development": "キェルケゴール『恐れとおののき』の哲学的物語法、カフカの寓話、"
                   "現代の象徴主義小説（ボルヘス、ル・グィン）に直結する短編形式の祖型。",
    "historical_context": "1世紀ユダヤ教ラビ的教授法とヘレニズム的修辞の融合。",
    "primary_source_url": "https://www.biblegateway.com/passage/?search=Luke+15&version=NRSVUE",
    "primary_source_type": "Bible Gateway — Luke 15 (parables)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "譬え話は表層と深層の二重性、解釈の開放性を本質とする。"
                      "AIによるテクスト解釈・意味生成において、譬え話は「単一意味への還元抵抗」の"
                      "範例として再評価されている。",
         "related_ai_phenomenon": "LLMによる多義テクストの単一化への警戒"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "譬え話の解釈は受容者の状況に開かれているため、AIによる「正解」生成と"
                      "原理的に対立する文学形式。",
         "related_ai_phenomenon": "AI解答の単一化バイアスへの古典的対抗例"},
    ],
})

add({
    "name_ja": "山上の垂訓（八福）",
    "name_en": "beatitudes",
    "name_original": "μακάριοι (makarioi)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "新約聖書時代",
    "definition": "マタイ福音書5-7章（並行ルカ6章）でイエスが語る教訓的説教の冒頭部。"
                  "「心の貧しい者は幸いである」等、9つの「幸いなるかな（makarios）」で始まる"
                  "祝福定式が並行構造を成し、価値の逆転（権力・富ではなく謙遜・憐れみが祝福される）"
                  "を宣言する。古代地中海世界の祝福詩定型を再構成した。",
    "background": "古代ヘブライ語の祝福詩（ašrê定型）とギリシャの祝福詩を結合。",
    "development": "アウグスティヌス『山上の垂訓』、トルストイ『神の国は汝の内にあり』、"
                   "ガンディーの非暴力思想、キング牧師の公民権説教まで、抵抗倫理の祖型として機能。",
    "historical_context": "ローマ帝政期パレスチナの社会的不平等への倫理的応答。",
    "primary_source_url": "https://www.biblegateway.com/passage/?search=Matthew+5&version=NRSVUE",
    "primary_source_type": "Bible Gateway — Matthew 5 (NRSVUE)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "福音書ナラティブ",
    "name_en": "gospel narrative",
    "name_original": "εὐαγγέλιον (euangelion)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "新約聖書時代",
    "definition": "マタイ・マルコ・ルカ・ヨハネの4福音書が確立した「神人イエスの生涯」を伝記的に"
                  "叙述する文学ジャンル。ヘレニズム的伝記（bios）とヘブライ的預言書を融合した独自形式。"
                  "受難・死・復活を中心軸に置き、複数視点による真理証言という構造を持つ。",
    "background": "1世紀後半のコイネ・ギリシャ語による編纂。マルコが最古とされる二資料説が支配的。",
    "development": "中世聖人伝、ダンテ『神曲』、ミルトン『失楽園』『復楽園』、"
                   "現代のニコス・カザンザキス『最後の誘惑』、サラマーゴ『イエス・キリストによる"
                   "福音書』まで、伝記文学・救済物語の祖型。",
    "historical_context": "1-2世紀地中海世界のキリスト教共同体形成の文学装置。",
    "primary_source_url": "https://www.biblegateway.com/passage/?search=Mark+1&version=NRSVUE",
    "primary_source_type": "Bible Gateway — Gospel of Mark (NRSVUE)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "4福音書の異なる「真理証言」の並置は、複数視点による真正性の構築という"
                      "古代的範例であり、AI時代の「複数AIによる真理生成」議論と構造的に類比される。",
         "related_ai_phenomenon": "複数LLMによる真理判定・コンセンサス形成"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "受難-死-復活という基本物語型は、現代物語論（フライ『偉大なコード』、"
                      "ジョセフ・キャンベル）の中核モデルとなり、AI生成物語の典型構造としても機能する。",
         "related_ai_phenomenon": "AI物語生成の典型構造としての受難-復活パターン"},
    ],
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "受難-復活神話",
         "description": "神話DBの英雄の旅・死と再生サイクルの聖書的範例。"},
    ],
})

add({
    "name_ja": "黙示文学",
    "name_en": "apocalyptic literature",
    "name_original": "ἀποκάλυψις (apokalypsis)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "新約聖書時代",
    "definition": "ダニエル書・ヨハネ黙示録に代表される、世界の終末と神の最終的勝利を象徴的幻視で"
                  "啓示する文学ジャンル。獣・数字（666）・玉座・天使長等の濃密な象徴体系で、"
                  "迫害下の信者に終末論的希望を与える。歴史を周期から終末へ向かう線形時間として構造化した。",
    "background": "前2世紀のマカバイ革命期から後1世紀のローマ迫害期にかけて発展。"
                  "イラン的二元論、ヘブライ預言書、ヘレニズム的幻視文学が融合。",
    "development": "ヨアキム・ダ・フィオーレの千年王国論、ブレイク『ヨーロッパ』、"
                   "T.S.エリオット『荒地』、コーマック・マッカーシー『ザ・ロード』、"
                   "現代SFの破滅小説まで、終末論的想像力の祖型。",
    "historical_context": "古代近東・地中海世界の被抑圧者の歴史哲学的応答。",
    "primary_source_url": "https://www.biblegateway.com/passage/?search=Revelation+1&version=NRSVUE",
    "primary_source_type": "Bible Gateway — Revelation (NRSVUE)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "黙示文学は「未来の終末を象徴的に描く」という独特の物語形式で、"
                      "現代AIによる予測的物語生成・シナリオプランニングの祖型として再評価される。",
         "related_ai_phenomenon": "AIによる未来シナリオ生成・終末論的想像"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "黙示文学の象徴解読は読者共同体の解釈実践を前提とし、"
                      "AI支援テクスト解読における共同的意味生成の古典的範例。",
         "related_ai_phenomenon": "AI支援による象徴テクスト解読の協調実践"},
    ],
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "終末神話",
         "description": "神話DBが扱う終末論・千年王国主題の起点テクスト。"},
    ],
})


# ===============================================================
# CATEGORY E — Criticism / rhetoric / major themes (8)
# ===============================================================

add({
    "name_ja": "ut pictura poesis（詩は絵のごとく）",
    "name_en": "ut pictura poesis",
    "name_original": "ut pictura poesis",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "ホラティウス『詩論』361行に登場する有名な格言「詩は絵のごとし（"
                  "ut pictura poesis erit）」。詩と絵画の姉妹芸術論の根本テクストとして、"
                  "ルネサンス以降の文芸批評・芸術論で「視覚芸術と言語芸術の比較可能性」の"
                  "規範的根拠となった。",
    "background": "アリストテレスの「人間は模倣する動物」、シモニデスの「絵は無言の詩、詩は語る絵」"
                  "の伝統を継承。",
    "development": "アルベルティ『絵画論』、ダ・ヴィンチ『パラゴーネ』（諸芸術比較論）、"
                   "レッシング『ラオコオン』（姉妹芸術論批判）、現代のエクフラシス研究まで"
                   "メディア横断比較芸術論の根本概念。",
    "historical_context": "アウグストゥス期の修辞学的詩学の体系化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0064",
    "primary_source_type": "Perseus — Horace Ars Poetica line 361",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "視覚芸術と言語芸術の等価論は、テキスト-画像マルチモーダルAIの"
                      "創造的等価性議論の古典的源泉として再活性化している。",
         "related_ai_phenomenon": "マルチモーダルAI（テキスト-画像生成）の理論的源泉"},
        {"axis": "言語", "status": "rethinking",
         "rationale": "言語と視覚記号の翻訳可能性を前提とする本格言は、"
                      "Stable Diffusion・DALL-E等の言語→画像生成の理論的祖型として再読される。",
         "related_ai_phenomenon": "テキスト-to-イメージ生成の理論基盤"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "詩画論",
         "description": "詩学DBが扱う姉妹芸術論の中核テクスト。"},
    ],
})

add({
    "name_ja": "デコールム（適切性）",
    "name_en": "decorum",
    "name_original": "decorum / aptum",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "ローマ共和政後期",
    "definition": "キケロ『弁論家論』『義務論』、ホラティウス『詩論』が体系化した、"
                  "「言葉・文体・主題が場面・人物・聴衆に適合すべし」という規範。"
                  "三文体（plain/middle/grand）の使い分け、悲劇・喜劇の人物造形の適合性等を含む。"
                  "西欧古典主義詩学の規範的中核。",
    "background": "ギリシャの prepon（適切性）概念のラテン化。アリストテレス的中庸の修辞学化。",
    "development": "ルネサンス・古典主義（カステルヴェトロ、ボワロー）の規範的詩学を支配し、"
                   "19世紀ロマン主義による反規範運動の主要な攻撃対象となった。",
    "historical_context": "ローマ共和政エリート文化の言語的儀礼の理論化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0119",
    "primary_source_type": "Perseus — Cicero De Officiis / Horace Ars Poetica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "崇高（ロンギノス）",
    "name_en": "sublime (Longinus)",
    "name_original": "ὕψος (hypsos)",
    "original_script": "greek",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "帝政ローマ時代（白銀期）",
    "definition": "1世紀のギリシャ語批評書『崇高について（Peri Hypsous）』が定式化した美学概念。"
                  "「思想の高貴さ」「強い情熱」「修辞的形象」「気高い措辞」「全体的構成」の"
                  "5源泉から生まれる、聴衆を「我を忘れさせる」言語効果を指す。",
    "background": "ヘレニズム期の修辞学批評の延長で、作者問題（「ロンギノス」と推定）は未解決。",
    "development": "1674年ボワローのフランス語訳で復活し、バーク『崇高と美』、カント"
                   "『判断力批判』、近代美学の中核概念となる。リオタールがポストモダンの"
                   "崇高として再活性化。",
    "historical_context": "ローマ帝政期のギリシャ語批評文化の到達点。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/17957",
    "primary_source_type": "Gutenberg — Longinus On the Sublime",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "崇高は受容者の「我を忘れる」体験を前提とし、AI生成テクストへの"
                      "美的応答の評価軸として再注目されている。",
         "related_ai_phenomenon": "AI生成テクストへの美的崇高体験の可能性"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "崇高は主体の自己超越体験を前提とし、AI時代の「拡張された主体性」議論に直結する。",
         "related_ai_phenomenon": "人間-AI協働における拡張された美的主体性"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "崇高美学",
         "description": "詩学DBが扱う崇高概念の起点テクスト。"},
    ],
})

add({
    "name_ja": "コピア（豊穣性）",
    "name_en": "copia",
    "name_original": "copia",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "ローマ共和政後期",
    "definition": "キケロ・クインティリアヌス修辞学が中核に据えた「言語的豊穣性」の理念。"
                  "同一の主題・思想を多様な言葉・形象・修辞で言い換える能力で、修辞的創造性の根本。"
                  "エラスムス『言語と思想の豊穣について』（De Copia, 1512）が体系化した。",
    "background": "ギリシャ語plēthos（豊富）のラテン化。アクィラ・ローマナ等の修辞学教程で詳述。",
    "development": "ルネサンス・ヒューマニズム教育の中核訓練法（バリエーション練習）、"
                   "シェイクスピア・モンテーニュの修辞的多様性の理論的根拠。",
    "historical_context": "古代修辞学の創造性訓練の中核装置。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a2007.01.0059",
    "primary_source_type": "Perseus — Quintilian Institutio Oratoria",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "コピア（同一主題の多様な表現）はLLMの「同一プロンプトに対する多様生成」と"
                      "構造的に類比される、言語的創造性の古典的範例。",
         "related_ai_phenomenon": "LLMによる多様表現生成（temperature制御）"},
        {"axis": "創造性", "status": "rethinking",
         "rationale": "「同じ思想を別の言葉で」を創造性の本質とする古典的観念は、"
                      "現代AI創造性の理論的祖型。",
         "related_ai_phenomenon": "AI創造性の中核としてのバリエーション生成"},
    ],
})

add({
    "name_ja": "敬虔なるアエネーアス（pius Aeneas）",
    "name_en": "pius Aeneas",
    "name_original": "pius Aeneas",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "ウェルギリウス『アエネーイス』の主人公アエネーアスを修飾する形容辞「pius」"
                  "（敬虔・義務に忠実）が指す英雄類型。"
                  "アキレウスの個人的栄誉、オデュッセウスの智略に対し、"
                  "家族（父アンキセースを背負う）・神々・運命（fatum）への義務を中核に据える"
                  "ローマ的英雄の祖型。",
    "background": "ローマ的pietas（家族・国家・神々への義務）概念のホメロス英雄に対する逆転。",
    "development": "中世のキリスト教的徳の英雄（聖人伝）、近代の責任ある国家指導者像、"
                   "現代のリーダーシップ論（責任倫理）まで、義務型英雄類型の祖。",
    "historical_context": "アウグストゥス的『ローマ的徳』のイデオロギー的核。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0055",
    "primary_source_type": "Perseus — Vergil Aeneid Bk 1-12",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "黄金の中庸（aurea mediocritas）",
    "name_en": "golden mean (aurea mediocritas)",
    "name_original": "aurea mediocritas",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "ホラティウス『歌章』2巻10番が提唱した「黄金の中庸」の理念。"
                  "極端を避け、中庸の生・適度な富・節度ある情熱を理想とする生き方。"
                  "ピンダロスの『中庸を愛する者』、アリストテレスの倫理学的中庸を結合した"
                  "ローマ的・実践哲学的生活美学の標語。",
    "background": "ストア・エピクロス・アリストテレスの倫理思想を結節するローマ的人生哲学。",
    "development": "ルネサンスの「sprezzatura（さりげなさ）」、近代のミドル・ウェイ思想、"
                   "現代の「ライフバランス」論の遠い起源。",
    "historical_context": "アウグストゥス期の私的生活美学の規範化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0024",
    "primary_source_type": "Perseus — Horace Odes Bk 2.10",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "festina lente（ゆっくり急げ）",
    "name_en": "festina lente",
    "name_original": "festina lente / σπεῦδε βραδέως",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "アウグストゥス帝の好んだ標語で「ゆっくり急げ」（ギリシャ語speude bradeōs）。"
                  "スエートーニウス『皇帝伝』が伝える。逆説的・矛盾的命題（オクシモロン）の"
                  "代表例として、慎重さと迅速性の弁証的調和を表す。エラスムス『格言集』が"
                  "ルネサンス標語として復活させた。",
    "background": "アウグストゥス的統治哲学の標語。古代修辞学の「contraries（対立）」の手法と接続。",
    "development": "ルネサンス印刷業者アルドゥス・マヌティウスの紋章、メディチ家の標語、"
                   "現代では「拙速より巧遅」「考えてから行動」のビジネス標語として活用。",
    "historical_context": "アウグストゥス帝の慎重な統治理念の格言化。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0061%3alife%3daug.%3achapter%3d25",
    "primary_source_type": "Perseus — Suetonius Augustus 25",
    "importance_score": 2,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ヘクサメター叙事詩規約",
    "name_en": "hexameter epic convention",
    "name_original": "hexameter dactylicus",
    "original_script": "latin",
    "subfield_code": "lit_eu_classical",
    "region": "西欧",
    "period_key": "アウグストゥス時代",
    "definition": "ホメロスから受け継がれ、エンニウス・ウェルギリウス・オウィディウス・ルカヌス・"
                  "スタティウス・シリウス・イタリクスを通じてラテン叙事詩の標準韻律として確立した"
                  "六脚律（dactylic hexameter）の詩形規約。"
                  "5つのダクテュロス（長短短）と1つのスポンデー（長長）を基本構成とする。",
    "background": "ホメロス叙事詩の口承定型句生成の韻律的基盤がラテン詩に移植された。"
                  "エンニウス『年代記』が前2世紀にラテン語ヘクサメターを確立。",
    "development": "ミルトン『失楽園』の英雄詩無韻詩、ロングフェロー『エヴァンジェリン』の"
                   "英語ヘクサメター実験、近代叙事詩の韻律的標準。",
    "historical_context": "ローマ詩のギリシャ韻律継承の中核装置。",
    "primary_source_url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.02.0055",
    "primary_source_type": "Perseus — Vergil Aeneid (canonical hexameter exemplar)",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "古典韻律論",
         "description": "詩学DBが扱う韻律体系の中核ジャンル規約。"},
    ],
})


# ---------------------------------------------------------------
# Relations
# ---------------------------------------------------------------

RELATIONS: list[tuple[str, str, str, str]] = [
    # Roman epic interconnections
    ("ウェルギリウス『アエネーイス』", "敬虔なるアエネーアス（pius Aeneas）", "contains",
     "アエネーイスの主人公pius Aeneasがローマ的英雄類型を体現する。"),
    ("ウェルギリウス『アエネーイス』", "ヘクサメター叙事詩規約", "contains",
     "アエネーイスはラテン・ヘクサメター叙事詩の正典範例。"),
    ("ウェルギリウス『牧歌』", "ウェルギリウス『農耕詩』", "extends",
     "牧歌の田園世界が農耕詩の労働の倫理へ展開する詩的進化。"),
    ("オウィディウス『変身物語』", "ヘクサメター叙事詩規約", "contains",
     "変身物語はラテン・ヘクサメターの叙事詩規約に従う。"),
    ("ルカヌス『内乱記（ファルサーリア）』", "ウェルギリウス『アエネーイス』", "criticizes",
     "ルカヌスは神々を排しアエネーイス的国民叙事詩を逆転的に批判する反叙事詩。"),
    ("スタティウス『テーバイス』", "ウェルギリウス『アエネーイス』", "extends",
     "スタティウスはウェルギリウスを忠実に範例とした白銀期の継承叙事詩。"),
    ("シリウス・イタリクス『プニカ』", "ウェルギリウス『アエネーイス』", "extends",
     "プニカはアエネーイスの韻律と構成を歴史叙事詩に応用。"),
    ("オウィディウス『名婦の手紙』", "オウィディウス『変身物語』", "extends",
     "両者は神話素材の再話と女性視点の独立を共有する関連作品。"),

    # Roman lyric / satire interconnections
    ("ホラティウス『歌章（カルミナ）』", "黄金の中庸（aurea mediocritas）", "contains",
     "ホラティウス歌章2巻10番がaurea mediocritasの語源テクスト。"),
    ("ホラティウス『詩論』", "デコールム（適切性）", "contains",
     "ホラティウス詩論はデコールムを詩学規範の中核として体系化。"),
    ("ホラティウス『詩論』", "ut pictura poesis（詩は絵のごとく）", "contains",
     "ut pictura poesisはホラティウス詩論361行に登場する。"),
    ("カトゥッルス抒情詩集", "プロペルティウス恋愛悲歌", "influences",
     "カトゥッルスの個人的情念詩がローマ恋愛悲歌の祖型を準備した。"),
    ("プロペルティウス恋愛悲歌", "ティブッルス恋愛悲歌", "extends",
     "両者はアウグストゥス期ローマ恋愛悲歌の双璧を成す。"),
    ("マルティアリス『エピグランマタ』", "ユウェナリス諷刺詩", "influences",
     "マルティアリスの諷刺的機知がユウェナリスの激しい諷刺へと展開。"),
    ("ペルシウス諷刺詩", "ユウェナリス諷刺詩", "influences",
     "ペルシウスの知的厳格諷刺がユウェナリスの社会諷刺の先駆となった。"),

    # Roman prose interconnections
    ("キケロ修辞学（弁論術）", "キケロ『弁論家論』", "contains",
     "弁論家論はキケロ修辞学の最高の理論的結晶。"),
    ("キケロ修辞学（弁論術）", "クインティリアヌス『弁論家の教育』", "influences",
     "キケロの修辞学体系がクインティリアヌスの教育論大全の基礎。"),
    ("キケロ『弁論家論』", "クインティリアヌス『弁論家の教育』", "extends",
     "クインティリアヌスはキケロのvir bonus理念を教育論として展開。"),
    ("クインティリアヌス『弁論家の教育』", "コピア（豊穣性）", "contains",
     "クインティリアヌス教育論はコピアを修辞訓練の中核として体系化。"),
    ("タキトゥス歴史叙述", "リウィウス『ローマ建国史』", "criticizes",
     "タキトゥスの帝政期暴政叙述はリウィウスの共和政賛美を悲観的に逆転する。"),
    ("セネカ悲劇", "ルカヌス『内乱記（ファルサーリア）』", "influences",
     "セネカ悲劇のストア哲学的英雄像が叔父甥の関係を超えて内乱記の英雄カトーへ継承。"),
    ("アプレイウス『黄金のロバ』", "ペトロニウス『サテュリコン』", "extends",
     "ローマ語ピカレスク小説の二大代表作を成し、近代小説ジャンルの祖型。"),

    # Biblical interconnections
    ("詩篇", "雅歌", "extends",
     "両者ともケトゥヴィーム所収のヘブライ詩文学で、抒情・恋歌・神秘の系譜を成す。"),
    ("ヨブ記", "詩篇", "extends",
     "ヨブ記の苦難詩は詩篇の嘆きの詩篇ジャンルと深く接続する。"),
    ("預言書文学", "黙示文学", "influences",
     "ヘブライ預言書の終末論的言説が黙示文学の祖型を準備した。"),
    ("譬え話（パラブル）", "福音書ナラティブ", "contains",
     "譬え話は福音書ナラティブの教訓的中核ジャンル。"),
    ("山上の垂訓（八福）", "福音書ナラティブ", "contains",
     "八福はマタイ福音書5章の山上の垂訓の冒頭部を構成する。"),
    ("黙示文学", "福音書ナラティブ", "extends",
     "黙示文学はヨハネ黙示録として新約聖書ナラティブの完結を成す。"),

    # Cross-category (Roman ↔ Biblical ↔ Theory)
    ("ホラティウス『詩論』", "崇高（ロンギノス）", "influences",
     "ホラティウスの詩学規範に対し、ロンギノス『崇高について』が情念的逸脱の美学として補完。"),
    ("デコールム（適切性）", "ut pictura poesis（詩は絵のごとく）", "extends",
     "デコールムの規範はut pictura poesisと併せて古典主義詩学の中核を成す。"),
    ("コピア（豊穣性）", "崇高（ロンギノス）", "influences",
     "コピアの言語的豊穣性が崇高の修辞的高揚の基盤を成す。"),
    ("ヘクサメター叙事詩規約", "ホラティウス『詩論』", "extends",
     "ホラティウス詩論はヘクサメター規約のラテン化された詩学規範を体系化。"),
    ("ウェルギリウス『アエネーイス』", "ヘクサメター叙事詩規約", "contains",
     "アエネーイスはラテン・ヘクサメター叙事詩規約の規範的範例。"),
    ("敬虔なるアエネーアス（pius Aeneas）", "黄金の中庸（aurea mediocritas）", "extends",
     "両者ともアウグストゥス期ローマ的徳の中核理念を成す。"),
    ("黙示文学", "預言書文学", "extends",
     "黙示文学はヘブライ預言書文学の終末論的継承形態。"),
    ("セネカ悲劇", "崇高（ロンギノス）", "influences",
     "セネカ悲劇の極端な情念表現が崇高美学の感性的範例となる。"),

    # festina lente connections
    ("festina lente（ゆっくり急げ）", "黄金の中庸（aurea mediocritas）", "extends",
     "festina lenteは黄金の中庸の処世訓的具体化。"),

    # Cicero rhetoric to philosophy bridge
    ("キケロ『弁論家論』", "キケロ修辞学（弁論術）", "contains",
     "弁論家論はキケロ修辞学の理論的完成形。"),

    # Apuleius / Ovid metamorphosis link
    ("アプレイウス『黄金のロバ』", "オウィディウス『変身物語』", "extends",
     "アプレイウスはオウィディウス的変身モチーフを散文小説に応用した継承作品。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[wave6_c02_roman_bible] inserting {len(CONCEPTS)} concepts...")
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
        print("[wave6_c02_roman_bible] inserted:")
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
        print(f"  coverage:")
        for r in db.coverage_by_subfield():
            if r["code"] == "lit_eu_classical":
                print(f"    {r}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
