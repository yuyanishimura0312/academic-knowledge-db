"""
LIT-DB Phase 2 — C22 Wave4: Persian & Turkish Literature
============================================================
Inserts 40 concepts spanning 5 categories:
  A. ペルシア古典詩学 (8)
  B. 主要詩人と概念 (8)
  C. スーフィー詩学・神秘主義 (8)
  D. オスマン古典文学 (8)
  E. 近代と現代 (8)

subfield_id=14, code='lit_persian_turkish', region='南西アジア'

Sources: Ganjoor (https://ganjoor.net/), Encyclopaedia Iranica
(https://iranicaonline.org/), OpenITI, Wikipedia canonical entries.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("ペルシア古典初期（サーマーン朝）", "Early Classical Persian (Samanid)",
     875, 1037,
     "ニューペルシア語（ファールシー）の文学的確立期。ルーダキー・フェルドウスィーが活躍し、シャー・ナーメによる民族叙事詩の定礎。"),
    ("ペルシア古典中期（セルジューク・ホラズム）", "Middle Classical Persian",
     1037, 1258,
     "セルジューク朝・モンゴル前夜。ニザーミー・アッタール・ハイヤームらによりロマンス叙事詩・スーフィー詩学が確立。"),
    ("ペルシア古典後期（イルハン・ティムール）", "Late Classical Persian",
     1258, 1500,
     "モンゴル期からティムール朝。ルーミー・サアディー・ハーフェズ・ジャーミーらの古典完成期。"),
    ("オスマン古典期（ディーワーン文学）", "Ottoman Classical (Diwan)",
     1300, 1839,
     "オスマン宮廷詩文化。フズーリー・バーキー・シェイヒ・ガーリブらディーワーン詩人と民俗文学の二層構造。"),
    ("タンジマート期（オスマン近代化）", "Tanzimat (Ottoman Modernization)",
     1839, 1908,
     "タンジマート改革（1839）以降の西欧化。ナマーク・ケマルら新世代がジャンル・主題を刷新。"),
    ("近現代ペルシア・トルコ", "Modern Persian / Turkish",
     1900, 2025,
     "ニーマー・ユーシージュによるシェエル・ノウ（新詩）、トルコ共和国成立後の言語改革、ヘダーヤト・パムクら現代作家の登場。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — ペルシア古典詩学 (8)
# ===============================================================

add({
    "name_ja": "ガザル（ペルシア版）",
    "name_en": "ghazal (Persian)",
    "name_original": "غزل",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "5から15ベイト程度の単韻短詩で、各ベイトが独立した意味単位をなしながら全体として恋愛・神秘・倫理を主題とするペルシア叙情詩の代表形式。最終ベイトに詩人の雅号（タハッルス）を織り込むのが慣例で、ハーフェズによって完成形を取った。",
    "background": "アラブ詩のカスィーダから恋愛部分（ナスィーブ）が独立して成立した抒情形式である。",
    "development": "サナーイー・サアディー・ハーフェズを経て成熟し、ウルドゥー語・トルコ語・スワヒリ語詩に伝播した。",
    "historical_context": "ペルシア宮廷文化と商人・スーフィー集会の双方で享受された汎域形式。",
    "primary_source_url": "https://iranicaonline.org/articles/gazal-1",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "カスィーダ（ペルシア版）",
    "name_en": "qasida (Persian)",
    "name_original": "قصیده",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン朝）",
    "definition": "アラブ詩から継承された長編単韻頌詩で、サーマーン朝以降のペルシア宮廷で君主賛歌・哲学詩・宗教詩の主要形式となった。ルーダキー・アンヴァリー・ハーカーニーらがペルシア固有の修辞・隠喩体系で再構築し、ガザルとは異なる重厚な公的文体を担った。",
    "background": "アラビア語カスィーダ形式をペルシア宮廷詩人が翻案・継承したものである。",
    "development": "ホラズム期に頂点を迎え、ペルシア宮廷文化の権威表象として機能した。",
    "historical_context": "宮廷経済と詩人パトロネージの中核装置となった。",
    "primary_source_url": "https://iranicaonline.org/articles/qasida-1",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "マスナヴィー（叙事詩形式）",
    "name_en": "masnavi / mathnawi",
    "name_original": "مثنوی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "二行連句（各ベイトが独立して脚韻するaa/bb/cc型）の長編詩形式で、叙事・教訓・神秘哲学を語る大規模物語に適する。ペルシア固有の発明とされ、フェルドウスィーの『シャー・ナーメ』、ニザーミーの『五詩集』、ルーミーの『精神的マスナヴィー』により世界文学史的地位を獲得した。",
    "background": "アラブ詩の単韻拘束を緩和し物語文学に適合させるべく考案された脚韻革新である。",
    "development": "民族叙事・恋愛ロマンス・神秘哲学の三系統に分岐し、トルコ語・ウルドゥー語に伝播した。",
    "historical_context": "ペルシア語圏全域の物語文学基盤となった。",
    "primary_source_url": "https://iranicaonline.org/articles/matnawi",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ルバーイー（四行詩）",
    "name_en": "ruba'i",
    "name_original": "رباعی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "aaba（または aaaa）の脚韻を持つ四行詩形式で、特定のホラサーニー韻律で書かれる短詩。哲学的省察・神秘的瞑想・人生の無常を凝縮的に表現するのに用いられ、ウマル・ハイヤーム『ルバイヤート』により世界文学的に著名となった。",
    "background": "ペルシア固有の短詩形式として古典初期に確立した。",
    "development": "ハイヤームの懐疑詩、サナーイー・アッタール・ルーミーの神秘ルバーイーへと多様化した。",
    "historical_context": "口承・即興詩としても広く用いられた。",
    "primary_source_url": "https://iranicaonline.org/articles/robai",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "キトア（断章）",
    "name_en": "qit'a",
    "name_original": "قطعه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン朝）",
    "definition": "ガザルと同形式の単韻短詩だが、冒頭ベイトの両半句が韻を踏まない（マトラを欠く）形式で、機会詩・諷刺・墓碑銘・哲学的箴言に用いられる。アラブ詩のキトアをペルシア詩が定着化させた断章形式で、宮廷の政治詩・社会批評を担った。",
    "background": "ガザルから儀礼性を除いた実用的短詩形式として分化した。",
    "development": "アンヴァリー・サアディーらの社会批評詩で発達した。",
    "historical_context": "宮廷の派閥抗争・社会風刺の媒体となった。",
    "primary_source_url": "https://iranicaonline.org/articles/qeta",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "ディーワーン（ペルシア版）",
    "name_en": "divan (Persian)",
    "name_original": "دیوان",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "個々の詩人の作品をジャンル別（カスィーダ・ガザル・キトア・ルバーイー）かつアルファベット順（脚韻字）に編纂する標準的詩集形式。ペルシア詩人の正典化装置として機能し、ハーフェズのディーワーンは占い書（ファール）として今日も用いられるなど特異な受容史を持つ。",
    "background": "アラブ詩のディーワーン編纂慣行をペルシア詩が継承・体系化したものである。",
    "development": "ハーフェズのディーワーン、サアディーの『クッリヤート』により編纂規範が確立した。",
    "historical_context": "ペルシア文学正典の物質的基盤を提供した。",
    "primary_source_url": "https://iranicaonline.org/articles/divan",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ヘカーヤト（説話）",
    "name_en": "hekayat",
    "name_original": "حکایت",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "教訓的・寓意的短編説話のジャンルで、サアディーの『グリスタン』『ブースターン』に典型を見る。散文と詩を交互に配し、王・賢者・スーフィー・庶民の逸話を通じて倫理・処世訓を伝える。コーラン的・スーフィー的世界観を物語化する装置として機能した。",
    "background": "アラブのアダブ文学・スーフィー教団の口承説話伝統が結合して成立した。",
    "development": "サアディーにより倫理的散文ジャンルとして確立し、トルコ語・ウルドゥー語に翻訳された。",
    "historical_context": "宮廷・マドラサ・キャラバンサライで広く享受された。",
    "primary_source_url": "https://iranicaonline.org/articles/hekayat",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "タハッルス（雅号）",
    "name_en": "takhallus",
    "name_original": "تخلص",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "ガザルの最終ベイトに詩人自身の雅号を織り込む慣習。ハーフェズ・サアディー・ルーミーらは本名と異なる詩号を用い、それが詩のシグネチャー機能と同時に詩的主体の自己呈示装置として機能した。詩人と詩中話者の同一性・差異を構造化する重要な詩学装置である。",
    "background": "ペルシア詩固有の作者性表象装置として確立した。",
    "development": "ガザル形式のジャンル境界標識として規範化された。",
    "historical_context": "詩集編纂の検索キーとしても機能した。",
    "primary_source_url": "https://iranicaonline.org/articles/takhallos",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY B — 主要詩人と概念 (8)
# ===============================================================

add({
    "name_ja": "シャー・ナーメ（フェルドウスィー）",
    "name_en": "Shahnameh (Ferdowsi)",
    "name_original": "شاهنامه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン朝）",
    "definition": "フェルドウスィー（940年頃-1020年頃）が30年余をかけて完成させた約5万ベイトのペルシア民族叙事詩。神話・伝説・歴史の三部からなり、イラン王朝史を統合的に物語化することでアラブ征服後のペルシア言語・民族アイデンティティの再構築を担った。マスナヴィー形式の頂点。",
    "background": "アラブ征服後のニューペルシア語成立期に、サーマーン朝の民族意識回復事業の文脈で構想された。",
    "development": "原典自体が正典化し、写本伝統・細密画装飾・パフォーマンス（ナッカーリー）を生み出した。",
    "historical_context": "ペルシア言語圏全域の民族的記憶装置となった。",
    "primary_source_url": "https://ganjoor.net/ferdousi/shahname",
    "primary_source_type": "Ganjoor PD text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ルーダキー（ペルシア詩の父）",
    "name_en": "Rudaki",
    "name_original": "رودکی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン朝）",
    "definition": "859年頃-941年。サーマーン朝の宮廷詩人で、ニューペルシア語による文学的詩作の創始者として「ペルシア詩の父」と称される。ガザル・カスィーダ・マスナヴィー・ルバーイーのすべてのジャンル基盤を確立し、現存する千ベイト余の詩はペルシア叙情詩の原型となった。",
    "background": "アラブ征服後のペルシア語復興運動の最初の主要詩人である。",
    "development": "後代のペルシア詩人すべての規範的祖型として機能した。",
    "historical_context": "サーマーン朝のブハラ宮廷を文化的中心に押し上げた。",
    "primary_source_url": "https://ganjoor.net/roodaki",
    "primary_source_type": "Ganjoor PD text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ニザーミーの五詩集（ハムセ）",
    "name_en": "Khamsa of Nizami",
    "name_original": "خمسه نظامی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "ニザーミー・ガンジャヴィー（1141-1209）による五編のマスナヴィー長編ロマンスの集成（『秘密の宝庫』『ホスローとシーリーン』『ライラとマジュヌーン』『七つの肖像』『イスカンダル・ナーメ』）。ペルシア・ロマンス叙事詩の正典を形成し、ジャーミー・アミール・ホスローらによる連作（ハムセ）模倣の標準を定めた。",
    "background": "コーカサスのアゼルバイジャン地域でセルジューク文化と接触する文脈に成立した。",
    "development": "オスマン語・チャガタイ語・ウルドゥー語に翻案され、細密画主題の供給源となった。",
    "historical_context": "ペルシア語圏のロマンス文学正典として機能した。",
    "primary_source_url": "https://ganjoor.net/nezami",
    "primary_source_type": "Ganjoor PD text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ハイヤームのルバイヤート",
    "name_en": "Rubaiyat of Omar Khayyam",
    "name_original": "رباعیات خیام",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "ウマル・ハイヤーム（1048-1131）に帰される千余の四行詩。生の無常・死の必然・神学的懐疑・刹那的享楽を凝縮的に表現し、エドワード・フィッツジェラルドの英訳（1859）を経て19世紀英語圏に巨大な影響を与えた。作者帰属の真正性問題と翻訳経由の世界文学化の典型例である。",
    "background": "数学者・天文学者ハイヤームの哲学的省察が四行詩に結晶化したものとされる。",
    "development": "フィッツジェラルド訳経由でヴィクトリア朝詩・モダニズム詩に深く影響した。",
    "historical_context": "ペルシア詩の世界文学化の象徴的事例となった。",
    "primary_source_url": "https://ganjoor.net/khayyam",
    "primary_source_type": "Ganjoor PD text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ルーミーのマスナヴィー",
    "name_en": "Masnavi-i Ma'navi (Rumi)",
    "name_original": "مثنوی معنوی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ジャラール・アッディーン・ルーミー（1207-1273）による約25,000ベイトの神秘哲学叙事詩で、メヴレヴィー教団の精神的経典として「ペルシア語のクルアーン」とも称される。寓話・逸話・コーラン解釈を織り交ぜ、神秘的合一・愛・主体消失（ファナー）の哲学を物語形式で展開する。",
    "background": "コンヤに移住したルーミーがメヴレヴィー旋舞教団を形成する文脈で口述・記録された。",
    "development": "オスマン期のテッケ（修道場）で典礼的に朗誦され、20世紀以降英訳経由で世界的受容を獲得した。",
    "historical_context": "スーフィー神秘哲学の最高峰文学的表現となった。",
    "primary_source_url": "https://ganjoor.net/moulavi/masnavi",
    "primary_source_type": "Ganjoor PD text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "サアディーの『グリスタン』『ブースターン』",
    "name_en": "Gulistan and Bustan of Sa'di",
    "name_original": "گلستان و بوستان",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "サアディー・シーラーズィー（1210頃-1291頃）による倫理文学の二大古典。『ブースターン』（1257）はマスナヴィー形式の徳論詩、『グリスタン』（1258）は散文と詩を交互に配する説話集。「アダム子はみな一身の肢体」の人類普遍主義句で名高く、ペルシア語圏の倫理的規範書として千年機能した。",
    "background": "モンゴル侵入期の流浪と巡礼経験を倫理的省察に結晶化したものである。",
    "development": "オスマン宮廷・ムガル宮廷で標準教科書となり、19世紀以降エマソン・ヴォルテール・ゲーテに影響した。",
    "historical_context": "ペルシア語圏の道徳教育の核となった。",
    "primary_source_url": "https://ganjoor.net/saadi",
    "primary_source_type": "Ganjoor PD text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ハーフェズのガザル",
    "name_en": "Ghazals of Hafez",
    "name_original": "غزلیات حافظ",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ハーフェズ・シーラーズィー（1325頃-1390頃）による約500のガザルで、ペルシア叙情詩の最高峰とされる。ワイン・愛・神秘的合一・偽善批判が多義的に重なり合う「リンディー（道楽者）」の語りを通じ、聖俗の境界を意図的に攪乱する詩学を展開した。ファール（占い）として今も用いられるなど特異な受容を持つ。",
    "background": "シーラーズのムザッファル朝・ティムール朝の動乱期に成立した。",
    "development": "ゲーテの『西東詩集』を介して西欧文学に深く影響し、20世紀ペルシア文学の規範を形成した。",
    "historical_context": "ペルシア語圏全域で家庭的・占い的に享受された。",
    "primary_source_url": "https://ganjoor.net/hafez",
    "primary_source_type": "Ganjoor PD text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_transform_status": "rethinking",
    "fourth_transform_note": "多義性の極致としてLLM時代の言語解釈論で再評価される。",
})

add({
    "name_ja": "ジャーミー（古典最後の巨匠）",
    "name_en": "Jami",
    "name_original": "جامی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ヌールッディーン・アブドゥッラフマーン・ジャーミー（1414-1492）はティムール朝末期ヘラート宮廷の詩人・スーフィー・学者で、「ペルシア古典詩最後の巨匠」と称される。『ハフト・アウラング（七つの王座）』はニザーミー連作模倣の標準ハムセを構成し、彼以降の古典詩の創造性は減退するとされる。",
    "background": "ナクシュバンディー教団のスーフィーとして活動しヘラート宮廷で重んじられた。",
    "development": "オスマン・ムガル両宮廷の規範作家となり、ペルシア古典の正典閉鎖の標識となった。",
    "historical_context": "ペルシア古典詩の終焉を象徴する人物となった。",
    "primary_source_url": "https://ganjoor.net/jami",
    "primary_source_type": "Ganjoor PD text",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY C — スーフィー詩学・神秘主義 (8)
# ===============================================================

add({
    "name_ja": "ファナー（消滅）",
    "name_en": "fana",
    "name_original": "فناء",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "スーフィズムにおける主体消失の概念で、修行者の自我（ナフス）が神性のうちに溶解する神秘的状態を指す。アッタール・ルーミー詩学の中核をなし、ペルシア神秘詩における主体・声・話者の境界を意図的に流動化させる詩学装置として機能する。仏教の無我・道教の忘我との比較研究の対象でもある。",
    "background": "9世紀バグダードのジュナイドらの神秘体験論を起点として教義化された。",
    "development": "ペルシア神秘詩・スーフィー教団の修行論の中核概念として展開した。",
    "historical_context": "イスラーム神秘主義の主体論の核心となった。",
    "primary_source_url": "https://iranicaonline.org/articles/fana",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "バカー（持続）",
    "name_en": "baqa",
    "name_original": "بقاء",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "ファナー（自我消滅）の後に到達する「神における持続」の状態。自我が消滅した後に神性のなかで再構成された主体が世界に立ち戻る神秘的段階を指し、ファナーと対をなしてスーフィー修行論の終局を構成する。ルーミー・イブン・アラビーの詩学・哲学で核心的概念となる。",
    "background": "ファナー教義の必然的補完として神秘主義教団で体系化された。",
    "development": "ファナー単独では世俗的活動の根拠が消失するため、行為主体の再構築原理として精緻化された。",
    "historical_context": "スーフィー教団の倫理的活動論の根拠となった。",
    "primary_source_url": "https://iranicaonline.org/articles/baqa-and-fana",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "マアリファ（叡智）",
    "name_en": "ma'rifa",
    "name_original": "معرفت",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "理性的知識（イルム）と区別される神秘的・直観的叡智で、神を直接体験的に知る認識様態を指す。スーフィー認識論の頂点をなし、アッタール『鳥の言葉』の七つの谷の終局に位置する。ペルシア神秘詩においては言語化不可能性をめぐる詩学的課題として展開される。",
    "background": "ハッラージュらの初期神秘体験論を起点として認識論として精緻化された。",
    "development": "イブン・アラビーの『フスース』とペルシア詩学の統合により思想と詩学が一体化した。",
    "historical_context": "スーフィー認識論の中核となった。",
    "primary_source_url": "https://iranicaonline.org/articles/marifa",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ハール（神秘的状態）",
    "name_en": "hal",
    "name_original": "حال",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "スーフィー修行者に神から一時的に与えられる神秘的状態を指す。マカーム（自力で達成する位階）と対をなし、恵贈的・突発的に訪れる体験で、ペルシア神秘詩における陶酔・狂喜・涙といった情動表現の理論的根拠となる。一時性ゆえに記述は困難で、詩的隠喩を必要とする。",
    "background": "9世紀以降のスーフィー教団で修行体験を分節化する語彙として確立した。",
    "development": "マカームとの対概念として体系化され、ペルシア神秘詩の情動描写の枠組みを提供した。",
    "historical_context": "スーフィー修行体験論の中核概念となった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Hal_(Sufism)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "マカーム（位階）",
    "name_en": "maqam",
    "name_original": "مقام",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "スーフィー修行者が自力で到達する精神的位階の概念で、悔悟・忍耐・信頼・服従などの段階を順序的に構成する。ハール（恵贈的状態）と対をなす自力的・段階的概念で、修行論の体系化と詩的物語化（七つの谷の旅）の双方を可能にした構造的概念である。",
    "background": "ジュナイドら初期スーフィーの修行論を起点として段階論として整備された。",
    "development": "アッタール『鳥の言葉』の七つの谷の構造的基盤となった。",
    "historical_context": "スーフィー修行論の組織原理となった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Maqaam",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "スーフィー象徴体系（ワイン・薔薇・ナイチンゲール）",
    "name_en": "Sufi symbolism (wine, rose, nightingale)",
    "name_original": "رمز صوفیانه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "ペルシア神秘詩で体系化された二重隠喩の象徴コードで、ワイン（神的陶酔）・薔薇（神的美）・ナイチンゲール（求道者の魂）・酌人（霊的師）・酒場（修道場）といった対応関係を通じ、表層の世俗的恋愛詩と深層の神秘哲学詩を同一テクストに重ねる詩学を確立した。",
    "background": "シャリーア法学者の検閲を回避するための隠喩的装置として発達した。",
    "development": "ハーフェズ詩で完成された二重読解可能性のシステムとなった。",
    "historical_context": "ペルシア詩の多義性詩学の核となった。",
    "primary_source_url": "https://iranicaonline.org/articles/sufi-symbolism",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_transform_status": "rethinking",
    "fourth_transform_note": "二重隠喩の体系はAI意味解析の隠喩多義性問題と直接接続する。",
})

add({
    "name_ja": "マスナヴィーの霊的物語",
    "name_en": "spiritual mathnawi",
    "name_original": "مثنوی معنوی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "マスナヴィー形式を神秘哲学の物語化に転用したジャンル概念で、サナーイー『真理の園』、アッタール『鳥の言葉』、ルーミー『精神的マスナヴィー』が代表する。寓話・逸話を連鎖させながらコーラン解釈・神秘哲学を物語的に展開し、教義書とは異なる詩的神学を成立させた。",
    "background": "サナーイーの『真理の園』を起点として神秘叙事詩ジャンルが分化した。",
    "development": "ルーミーの『精神的マスナヴィー』により最高峰に達した。",
    "historical_context": "ペルシア神秘文学の主要ジャンルとなった。",
    "primary_source_url": "https://iranicaonline.org/articles/mathnawi",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "リンド（道楽者の人物像）",
    "name_en": "rind",
    "name_original": "رند",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ハーフェズ詩学の中核をなす逆説的人物像で、表面的には酒場に通う放蕩者でありながら内面的には偽善的法学者を超える真の信仰者という二重構造を持つ。シャリーア順守を装う「ザーヘド（敬虔者）」との対立構図でペルシア神秘詩の偽善批判を担い、聖俗境界の攪乱者として機能する。",
    "background": "アッタール期にすでに萌芽するが、ハーフェズで詩学的中心人物となった。",
    "development": "ペルシア叙情詩における皮肉・諷刺・神秘の重層構造を体現する人物類型となった。",
    "historical_context": "ペルシア詩の聖俗統合詩学の象徴となった。",
    "primary_source_url": "https://iranicaonline.org/articles/rend",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY D — オスマン古典文学 (8)
# ===============================================================

add({
    "name_ja": "ディーワーン文学（オスマン版）",
    "name_en": "Diwan poetry (Ottoman)",
    "name_original": "Divan edebiyatı",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "13世紀から19世紀のオスマン宮廷詩文化で、ペルシア詩の形式（ガザル・カスィーダ・マスナヴィー）と修辞体系を全面的に継承しつつ、オスマン・トルコ語独自の語彙（アラビア語・ペルシア語・トルコ語の三層融合）で展開された。フズーリー・バーキー・ナーブィー・ネディムらが代表し、民俗文学（ハルク文学）と並行する二層構造を形成した。",
    "background": "セルジューク朝以来のアナトリア宮廷文化がオスマン宮廷で制度化された。",
    "development": "16世紀バーキーから18世紀ネディムへと洗練が進み、19世紀タンジマート期に近代化批判の対象となった。",
    "historical_context": "オスマン宮廷文化の中核を担った。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Ottoman_Divan_poetry",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "フズーリー",
    "name_en": "Fuzuli",
    "name_original": "Fuzûlî / فضولی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "ムハンマド・ビン・スレイマン・フズーリー（1483頃-1556）はバグダード周辺で活動した詩人で、アゼルバイジャン・トルコ語、ペルシア語、アラビア語の三言語で詩を残した。マスナヴィー『ライラとマジュヌーン』（トルコ語）とディーワーンが代表作で、オスマン古典文学の精神的祖型として後代に巨大な影響を残した。",
    "background": "サファヴィー・オスマン両帝国の境界地域で活動し、両宮廷文化に通じた。",
    "development": "オスマン詩人の祖型として規範化され、20世紀アゼルバイジャンでは民族詩人として再評価された。",
    "historical_context": "テュルク語圏全域の詩的規範を提供した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Fuzuli_(poet)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "バーキー",
    "name_en": "Baki",
    "name_original": "Bâkî / باقی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "マフムード・アブドゥルバーキー（1526-1600）はスレイマン大帝期のオスマン宮廷詩人で「詩のスルタン（スルタヌッシュアラー）」と称された。ガザルの形式的洗練を頂点に押し上げ、特にスレイマン大帝への悲歌（メルスィエ）はオスマン古典詩の代表作となった。",
    "background": "イスタンブルの貧しい家庭から学者・詩人として出世しスレイマン大帝の寵を得た。",
    "development": "オスマン古典詩の頂点を象徴する詩人として標準化された。",
    "historical_context": "オスマン宮廷詩の制度的中心を担った。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Baki_(poet)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "シェイヒ・ガーリブ",
    "name_en": "Sheikh Galib",
    "name_original": "Şeyh Gâlib / شیخ غالب",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "メフメト・エサド・ガーリブ・デデ（1757-1799）はメヴレヴィー教団の長老（シェイヒ）にしてオスマン古典詩最後の巨匠。マスナヴィー『フスン・ウ・アシュク（美と愛）』はスーフィー的寓意叙事詩の頂点とされ、オスマン古典文学の終焉と19世紀近代への橋渡しを象徴する詩人となった。",
    "background": "メヴレヴィー教団ガラタ修道場の長老として活動した。",
    "development": "オスマン古典詩の自己反省的完結と新時代への移行を体現した。",
    "historical_context": "古典詩終焉期の象徴的人物となった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Sheikh_Ghalib",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "メスネヴィー（トルコ版）",
    "name_en": "mesnevi (Turkish)",
    "name_original": "mesnevi",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "ペルシア・マスナヴィー形式のトルコ語版で、二行連句脚韻形式による長編叙事詩・教訓詩・神秘詩のジャンル。フズーリーの『ライラとマジュヌーン』、シェイヒ・ガーリブの『フスン・ウ・アシュク』が代表する。ペルシア・マスナヴィー伝統の翻案・継承を通じてオスマン文学の物語形式を提供した。",
    "background": "ペルシア・マスナヴィー形式の翻案がアナトリアで定着した。",
    "development": "オスマン宮廷文学の主要物語形式となった。",
    "historical_context": "ペルシア・トルコ文学の連続性を示すジャンルとなった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mesnevi",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "カスィーデ（トルコ版）",
    "name_en": "kaside (Turkish)",
    "name_original": "kaside",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "アラブ・ペルシアのカスィーダ形式のオスマン・トルコ語版で、スルタン・大宰相・諸侯への賛歌、スルタンの即位・遠征記念詩、預言者賛詩などを担う長編単韻頌詩。ナフ（預言者賛歌）・メディフ（賛歌）・ヒジヴ（諷刺）といった主題サブジャンルを発達させた。",
    "background": "アラブ・ペルシア・カスィーダ伝統の翻案として定着した。",
    "development": "オスマン宮廷の儀礼詩として制度化された。",
    "historical_context": "オスマン宮廷の権威表象装置となった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Kaside",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "ハルク・エデビヤトゥ（民俗文学）",
    "name_en": "halk edebiyati",
    "name_original": "halk edebiyatı",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "オスマン古典のディーワーン文学（宮廷文学）と並行して発達したトルコ民俗文学の総称で、アシュク（吟遊詩人）の口承詩、コシュマ（叙情民謡）、デスタン（民族叙事詩）、トルコ式トルコ語の使用を特徴とする。ユヌス・エムレ、カラージャオウラン、ピル・スルタン・アブダルらが代表する。",
    "background": "中央アジア・テュルク系の口承詩伝統が宮廷文化と並行して継承された。",
    "development": "20世紀の言語改革・国民国家形成期にトルコ・アイデンティティの基盤として再評価された。",
    "historical_context": "オスマン文学の二層構造の片翼を担った。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Turkish_folk_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "カラギョズ（影絵芝居）",
    "name_en": "Karagoz shadow theatre",
    "name_original": "Karagöz",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "オスマン期に確立した伝統影絵芝居で、主人公カラギョズ（庶民）とハジヴァト（教養人）の対話を中心に、社会風刺・言語遊戯・滑稽劇を展開する。ラマダン期の祝祭娯楽として制度化され、口承喜劇文学のオスマン的形式を提供した。2009年にユネスコ無形文化遺産に登録された。",
    "background": "中世東地中海の影絵芝居伝統がオスマン宮廷・コーヒーハウス文化で定着した。",
    "development": "ラマダン娯楽として民衆文化の中核を担い、20世紀以降演劇研究の対象となった。",
    "historical_context": "オスマン都市文化の口承喜劇基盤となった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Karag%C3%B6z_and_Hacivat",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "minor",
})


# ===============================================================
# CATEGORY E — 近代と現代 (8)
# ===============================================================

add({
    "name_ja": "ナマーク・ケマル（タンジマート改革）",
    "name_en": "Namik Kemal",
    "name_original": "Namık Kemal",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "タンジマート期（オスマン近代化）",
    "definition": "ナマーク・ケマル（1840-1888）はタンジマート期の詩人・劇作家・政治思想家で、近代オスマン文学の祖型。戯曲『祖国またはシリストレ』（1873）でオスマン演劇に祖国・自由・立憲主義の主題を導入し、ヨーロッパ近代文学の枠組みでオスマン文学を再構築する道を開いた。",
    "background": "若きオスマン人運動の指導者として近代化と立憲主義を推進した。",
    "development": "オスマン文学の近代化・西欧化の象徴的人物として規範化された。",
    "historical_context": "近代トルコ文学の起点を提供した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Nam%C4%B1k_Kemal",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "テヴフィク・フィクレト（西欧化詩）",
    "name_en": "Tevfik Fikret",
    "name_original": "Tevfik Fikret",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "タンジマート期（オスマン近代化）",
    "definition": "テヴフィク・フィクレト（1867-1915）はセルヴェティ・フュヌーン（富の知識）誌の中心詩人で、フランス・パルナス派・象徴派を範に取りオスマン詩のヨーロッパ化を推進した。社会批判詩・人類普遍主義・反専制主義を主題とし、近代トルコ詩の文学言語を創出した。",
    "background": "ガラタサライ高校の文学教師としてフランス文学を媒介した。",
    "development": "セルヴェティ・フュヌーン運動を通じてトルコ詩の近代化を主導した。",
    "historical_context": "トルコ詩の西欧化の決定的局面を担った。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Tevfik_Fikret",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "サーデク・ヘダーヤト『盲目の梟』",
    "name_en": "Sadeq Hedayat / The Blind Owl",
    "name_original": "صادق هدایت / بوف کور",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "サーデク・ヘダーヤト（1903-1951）の小説『盲目の梟』（1936）はペルシア近代散文の最高峰とされ、カフカ・ポー・フランス象徴主義の影響下に幻想・狂気・反復・死を主題とする実験的内的独白を展開した。近代ペルシア小説の起点を画し、ヘダーヤトの自殺と相俟って20世紀ペルシア文学の象徴となった。",
    "background": "パリ留学経験とフランス・ヨーロッパ近代文学の摂取を背景に成立した。",
    "development": "ペルシア小説の近代化の決定的作品として正典化された。",
    "historical_context": "20世紀ペルシア文学の頂点を象徴する作品となった。",
    "primary_source_url": "https://iranicaonline.org/articles/hedayat-sadeq-i-life",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ニーマー・ユーシージュ（ペルシア新詩）",
    "name_en": "Nima Yushij / sher-e now",
    "name_original": "نیما یوشیج / شعر نو",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "アリー・エスファンディヤーリー（1897-1960、雅号ニーマー・ユーシージュ）は古典ペルシア韻律の固定的構造を打破し、行長・脚韻配置を内容に応じて自由化する「シェエル・ノウ（新詩）」を創始した。詩『アフサーネ（伝説、1922）』『フェネク（ファネク、1948）』が代表作で、現代ペルシア詩の祖と位置付けられる。",
    "background": "千年続いた古典韻律の絶対性に対する内側からの構造的批判として登場した。",
    "development": "シャーミルー、フォルーグ・ファッロホザード、セペフリーら次世代詩人の言語的基盤となった。",
    "historical_context": "ペルシア詩の千年に一度の構造変革を担った。",
    "primary_source_url": "https://iranicaonline.org/articles/nima-yushij",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_transform_status": "rethinking",
    "fourth_transform_note": "古典韻律の解体と自由詩の創始は、AI時代の形式拘束再考と類比される。",
})

add({
    "name_ja": "フォルーグ・ファッロホザード（女性詩）",
    "name_en": "Forough Farrokhzad",
    "name_original": "فروغ فرخزاد",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "フォルーグ・ファッロホザード（1934-1967）は20世紀ペルシア詩を代表する女性詩人で、女性主体・身体・欲望を一人称で語る革新的詩学を確立した。詩集『反逆』（1958）『再生』（1964）『信じよう、寒い季節の始まりを』（1974）が代表作で、ペルシア詩におけるジェンダー主体の問題を本格的に開いた。",
    "background": "ニーマー・ユーシージュの新詩運動の継承者として登場した。",
    "development": "ペルシア詩のジェンダー主体革命を担い、世界詩史にも影響した。",
    "historical_context": "20世紀ペルシア女性文学の象徴となった。",
    "primary_source_url": "https://iranicaonline.org/articles/farrokhzad-forug-poet",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "オルハン・パムク『無垢の博物館』",
    "name_en": "Orhan Pamuk / The Museum of Innocence",
    "name_original": "Masumiyet Müzesi",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "オルハン・パムク（1952-）はトルコ初のノーベル文学賞受賞者（2006）で、長編小説『無垢の博物館』（2008）は1970年代イスタンブルを舞台に喪失と記憶の博物館化を主題とする。実物の博物館（Masumiyet Müzesi、2012年開館）と小説の相互参照が、小説形式の物質化という前例のない実験を達成した。",
    "background": "イスタンブルの中産階級知識人家庭に育ちアメリカ滞在経験を持つ。",
    "development": "小説と博物館の融合実験により21世紀小説の形式革新を達成した。",
    "historical_context": "現代トルコ文学の世界文学化を象徴する作家となった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/The_Museum_of_Innocence",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ソフラブ・セペフリー",
    "name_en": "Sohrab Sepehri",
    "name_original": "سهراب سپهری",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ソフラブ・セペフリー（1928-1980）はペルシア現代詩・絵画の双方で活躍した詩人画家で、仏教・道教・スーフィズムを統合した東洋的精神性を新詩形式で表現した。長詩『水の足音』（1965）『緑の容積』（1967）が代表作で、自然・水・色彩・透明性を主題化したペルシア生態詩の先駆となった。",
    "background": "京都・インドへの旅を通じて東アジア精神性を摂取した。",
    "development": "ペルシア現代詩に東洋的・生態的次元を導入した。",
    "historical_context": "ニーマー以後のペルシア新詩多様化の代表的展開を担った。",
    "primary_source_url": "https://iranicaonline.org/articles/sepehri-sohrab",
    "primary_source_type": "Encyclopaedia Iranica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ヤシャル・ケマル『インス・メメド』",
    "name_en": "Yasar Kemal / Memed, My Hawk",
    "name_original": "İnce Memed",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ヤシャル・ケマル（1923-2015）の長編小説『インス・メメド（やせっぽちのメメド）』（1955）はトルコ・チュクロワ地方を舞台に圧政に抗うアウトロー（エシュキヤ）を主人公とする社会派小説。トルコ民俗叙事の伝統と社会主義リアリズムを統合し、戦後トルコ文学の世界化を牽引した。",
    "background": "クルド系・チュクロワ地方の口承文化的素養を背景に成立した。",
    "development": "40カ国語以上に翻訳されトルコ文学の国際的代表作となった。",
    "historical_context": "戦後トルコ社会派文学の頂点を画した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Yasar_Kemal",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ---------------------------------------------------------------
# Fourth-transform tagging (12+ entries)
# ---------------------------------------------------------------
FOURTH_TRANSFORM_TAGS = {
    "ハーフェズのガザル": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "ハーフェズのガザルは聖俗・恋愛/神秘の二重読解を意図的に成立させる多義性詩学の極致で、AI言語モデルによる多義性解析・隠喩展開と直接接続する。",
         "ai_phenomenon": "LLMによる多義性解釈・複数読解可能性の同時保持"},
        {"axis": "作者性", "status": "partial",
         "rationale": "タハッルス（雅号）による詩人主体の自己呈示と、写本伝承の偽作問題は、AI生成詩におけるシグネチャー・作者推定の問題と部分的に対応する。",
         "ai_phenomenon": "AI生成詩のスタイロメトリー的作者推定"},
    ],
    "スーフィー象徴体系（ワイン・薔薇・ナイチンゲール）": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "ワイン・薔薇等の二重隠喩体系は表層と深層の意味の真正性を意図的に分裂させる詩学で、AI生成テクストの真正性問題（表面的人間性と内部メカニズムの分裂）と構造的に類比される。",
         "ai_phenomenon": "AI生成テクストの表層的真正性と内部メカニズムの乖離"},
        {"axis": "言語", "status": "rethinking",
         "rationale": "二重隠喩のシステマティックな運用はLLMの隠喩解析・意味の重ね合わせ生成の理論的先駆として再評価される。",
         "ai_phenomenon": "LLMの隠喩多義性の意味解析"},
    ],
    "ルーミーのマスナヴィー": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "寓話・逸話・コーラン解釈を多層的に連鎖する物語構造は、AI生成の連鎖的・拡張的物語生成と類比される。",
         "ai_phenomenon": "AI生成の連鎖的・寓話的物語拡張"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "ファナー（自我消滅）を物語の核に据えたマスナヴィーは、AI生成における話者主体の溶解・拡散と存在論的に類比される。",
         "ai_phenomenon": "AI生成テクストにおける話者主体の溶解"},
    ],
    "ニーマー・ユーシージュ（ペルシア新詩）": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "千年続いた古典韻律の絶対性を内側から解体しシェエル・ノウを創始した運動は、AI時代の形式拘束再考・自由詩生成と直接接続する。",
         "ai_phenomenon": "AI生成詩における形式拘束の解体・自由化"},
    ],
    "ナマーク・ケマル（タンジマート改革）": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "西欧文学受容を通じてオスマン文学の正典・ジャンル体系を再構築したタンジマート文学は、グローバルAI翻訳が進める現代の文学受容再編と構造的に類比される。",
         "ai_phenomenon": "AI翻訳によるグローバル文学受容の再編"},
    ],
    "ファナー（消滅）": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "スーフィー的主体消失の概念は、AI生成テクストにおける主体性の希薄化・分散化と存在論的に類比される。",
         "ai_phenomenon": "AI生成における主体性の分散・消失"},
    ],
    "サアディーの『グリスタン』『ブースターン』": [
        {"axis": "正典", "status": "partial",
         "rationale": "ペルシア語圏千年の標準教科書として機能したサアディーの倫理文学は、LLMの教科書的知識集成機能と部分的に類比される。",
         "ai_phenomenon": "LLMの規範的・倫理的知識集成"},
    ],
    "シャー・ナーメ（フェルドウスィー）": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "アラブ征服後のペルシア民族正典を再構築した叙事詩事業は、AI翻訳・生成による地域文学正典の再構築と構造的に類比される。",
         "ai_phenomenon": "AI翻訳・生成による地域・少数言語文学の正典化"},
    ],
    "オルハン・パムク『無垢の博物館』": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "小説と物質的博物館の相互参照という形式実験は、AIマルチモーダル生成の物語と物質性の融合と直接接続する。",
         "ai_phenomenon": "AIマルチモーダル生成における物語と物質性の融合"},
    ],
    "ハイヤームのルバイヤート": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "フィッツジェラルド英訳が原典を上回る世界的影響を獲得した受容史は、AI翻訳が原典を超える受容を生む可能性と直接対応する。",
         "ai_phenomenon": "AI翻訳が原典を超える受容を生む現象"},
    ],
    "サーデク・ヘダーヤト『盲目の梟』": [
        {"axis": "受容", "status": "partial",
         "rationale": "ペルシア小説の世界化を成立させた受容構造は、現代AI時代の周縁言語文学のグローバル化と部分的に類比される。",
         "ai_phenomenon": "AI翻訳による周縁言語文学のグローバル化"},
    ],
    "ディーワーン文学（オスマン版）": [
        {"axis": "正典", "status": "invariant"},
    ],
}


# ---------------------------------------------------------------
# Cross-domain links (>= 8)
# ---------------------------------------------------------------
CROSS_DOMAIN_LINKS = [
    ("ガザル（ペルシア版）", "PT", "shared_concept", "lyric poetry / poetics",
     "ペルシア・ガザルは世界叙情詩学における短詩独立形式の代表事例で、詩学DBの抒情詩研究と直接接続する。"),
    ("マスナヴィー（叙事詩形式）", "PT", "shared_concept", "narrative verse form",
     "二行連句叙事形式は世界叙事詩学における脚韻配置論の主要事例で、詩学DBと共有される。"),
    ("ファナー（消滅）", "PHIL", "shared_concept", "Sufi philosophy / annihilation of self",
     "ファナーはイスラーム神秘哲学・主体論の中核概念で、哲学DBのスーフィズム項目と直接共有される。"),
    ("マアリファ（叡智）", "PHIL", "shared_concept", "mystical epistemology",
     "ma'rifaは神秘的認識論として哲学DBの認識論項目と直接接続する。"),
    ("バカー（持続）", "PHIL", "shared_concept", "Sufi metaphysics",
     "ファナー後の主体再構築原理は哲学DBの主体論・形而上学と共有される。"),
    ("スーフィー象徴体系（ワイン・薔薇・ナイチンゲール）", "PHIL", "shared_concept", "Ibn Arabi / wahdat al-wujud",
     "スーフィー象徴の二重構造は存在の単一性論（ワフダトゥル・ウジュード）哲学と一体に発展した。"),
    ("ハルク・エデビヤトゥ（民俗文学）", "AN", "shared_concept", "oral folk tradition / Anatolia",
     "アシュク吟遊詩・口承民謡は人類学的口承文学研究の主要対象であり、人類学DBと共有される。"),
    ("カラギョズ（影絵芝居）", "AN", "shared_concept", "shadow theatre / performance ethnography",
     "オスマン影絵芝居は人類学的パフォーマンス研究・無形文化遺産研究の典型事例として共有される。"),
    ("ハーフェズのガザル", "AI-Development", "parallel", "LLM polysemy interpretation",
     "ハーフェズの聖俗二重読解詩学は、LLMの多義性解釈・複数読解可能性保持の理論的先駆として位置付けられる。"),
    ("ニーマー・ユーシージュ（ペルシア新詩）", "AI-Development", "parallel", "LLM free-form generation",
     "古典韻律解体によるシェエル・ノウ運動は、LLMによる形式拘束を超えた自由詩生成と歴史的に類比される。"),
    ("スーフィー象徴体系（ワイン・薔薇・ナイチンゲール）", "AI-Development", "parallel", "metaphor processing in LLMs",
     "二重隠喩のシステマティックな運用はLLMの隠喩処理・意味多重化の理論的先駆として再評価される。"),
    ("シャー・ナーメ（フェルドウスィー）", "Myth-Narratives", "shared_concept", "national epic / mythological cycle",
     "民族叙事詩シャー・ナーメは神話・物語DBにおける国民叙事詩の代表事例として共有される。"),
]


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

def main() -> None:
    with LitDB() as db:
        # Seed periods
        period_id_by_key: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(
                name_ja=nj, region="南西アジア",
                start_year=sy, end_year=ey,
                name_en=ne, description=desc,
            )
            period_id_by_key[nj] = pid

        # Insert concepts
        name_to_id: dict[str, int] = {}
        inserted = 0
        skipped = 0
        for entry in CONCEPTS:
            ent = dict(entry)
            period_key = ent.pop("period_key", None)
            if period_key:
                ent["period_id"] = period_id_by_key.get(period_key)
            try:
                cid = db.insert_concept(**ent)
                name_to_id[ent["name_ja"]] = cid
                inserted += 1
            except LitDBError as e:
                print(f"[error] insert failed for {ent.get('name_ja')!r}: {e}")
                skipped += 1

        # Fourth-transform tags
        ft_count = 0
        for name_ja, tags in FOURTH_TRANSFORM_TAGS.items():
            cid = name_to_id.get(name_ja)
            if not cid:
                print(f"[warn] no concept id for fourth-transform: {name_ja!r}")
                continue
            for tag in tags:
                try:
                    db.tag_fourth_transform(
                        cid,
                        axis=tag["axis"],
                        status=tag["status"],
                        rationale=tag.get("rationale"),
                        related_ai_phenomenon=tag.get("ai_phenomenon"),
                    )
                    ft_count += 1
                except LitDBError as e:
                    print(f"[error] tag failed for {name_ja!r}/{tag['axis']}: {e}")

        # Cross-domain links
        cd_count = 0
        for name_ja, target_db, link_type, target_name, desc in CROSS_DOMAIN_LINKS:
            cid = name_to_id.get(name_ja)
            if not cid:
                print(f"[warn] no concept id for cross-domain: {name_ja!r}")
                continue
            try:
                db.insert_cross_domain(
                    lit_entity_type="concept",
                    lit_entity_id=cid,
                    target_db=target_db,
                    link_type=link_type,
                    target_entity_name=target_name,
                    description=desc,
                )
                cd_count += 1
            except LitDBError as e:
                print(f"[error] cross-domain failed for {name_ja!r}: {e}")

        print(f"\n=== C22 Persian-Turkish completed ===")
        print(f"  concepts inserted: {inserted} (skipped: {skipped})")
        print(f"  fourth-transform tags: {ft_count}")
        print(f"  cross-domain links: {cd_count}")
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 14"
        ).fetchone()
        print(f"  total concepts in subfield 14: {row['c']}")


if __name__ == "__main__":
    main()
