"""
LIT-DB Phase 2 Wave 11 — C22 ADD: Persian & Turkish Literature (40 new concepts).

Subfield: lit_persian_turkish (id=14), region='南西アジア'.
Sources: Ganjoor (https://ganjoor.net/), Encyclopaedia Iranica
(https://iranicaonline.org/), OpenITI, Tashlh corpus, Ottoman Diwan archives,
academic-grade Wikipedia (en/tr/fa).

40 NEW concepts split into five blocks of 8 (avoiding existing ids 522-561):
  A: ペルシア・スーフィー詩拡張（ルーミー弟子・サアディー教説・ビーデル・サブク・ヒンディー） 8
  B: ペルシア古典散文（ターリーフ・タズキラ・スィヤーサトナーマ等） 8
  C: 古典トルコ拡張（ディーワーン形式・テズキレ・シェイヒ・ガーリブ・アハメディー） 8
  D: 近代トルコ（タンプナル、パムク補充、ヒサール、アハメト・ハムディ） 8
  E: 近代イラン・アフガン・タジク・アゼリ・ウズベク 8

source_tier classical >= 75% primary, fourth_transform >= 12, cross_domain >= 8.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


PERIODS_TO_SEED = [
    ("ペルシア古典中期（セルジューク・ホラズム）", "Middle Classical Persian",
     1037, 1258,
     "セルジューク朝・モンゴル前夜のペルシア古典詩学黄金期。"),
    ("ペルシア古典後期（イルハン・ティムール）", "Late Classical Persian",
     1258, 1500,
     "モンゴル期からティムール朝。古典完成期。"),
    ("ペルシア古典散文期", "Persian Classical Prose",
     950, 1500,
     "ペルシア散文の歴史叙述・聖人伝・統治論・倫理書の確立期。バイハキー、アッタール、ニザームルムルクら。"),
    ("サブク・ヒンディー期", "Sabk-e Hindi (Indian Style)",
     1500, 1750,
     "ムガル朝期インド・ペルシア詩学。サーイブ、カリーム、ビーデルらによるイメージ過剰主義と意味の繊細化。"),
    ("オスマン古典期（ディーワーン文学）", "Ottoman Classical (Diwan)",
     1300, 1839,
     "オスマン宮廷詩文化。アフメディー、フズーリー、バーキー、ネフィー、ナービー、ガーリブら。"),
    ("近現代ペルシア・トルコ", "Modern Persian / Turkish",
     1900, 2025,
     "ニーマー以後のペルシア新詩、トルコ共和国期の散文。ヘダーヤト、タンプナル、パムク、ファッロホザード、シャーミルー他。"),
    ("中央アジア近現代", "Modern Central Asia",
     1900, 2025,
     "タジク・ウズベク・アゼリ近代文学。アイニー、チョルパン、カディリ、サービル、シャフリヤール他。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


GANJOOR = "https://ganjoor.net/"
IRANICA = "https://iranicaonline.org/articles/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_TR = "https://tr.wikipedia.org/wiki/"
WIKI_FA = "https://fa.wikipedia.org/wiki/"
OPENITI = "https://openiti.org/"


# ===============================================================
# A. ペルシア・スーフィー詩拡張（8）
# ===============================================================

add({
    "name_ja": "サナーイー『真理の園』",
    "name_en": "Sana'i / Hadiqat al-Haqiqa",
    "name_original": "حدیقة الحقیقه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "ハキーム・サナーイー・ガズナヴィー（c.1080-c.1131）が1131年頃完成した教訓的マスナヴィー『真理の園と道法の真理（Ḥadīqat al-Ḥaqīqa wa Sharīʿat al-Ṭarīqa）』。約11,000ベイトに及ぶ最古の体系的スーフィー教説詩で、コーラン解釈・寓話・神秘体験・倫理を統合した。アッタール・ルーミーの直接の祖型となり、ペルシア神秘詩学の規範を確立した。",
    "background": "ガズナヴィー朝宮廷詩人としての出発から神秘主義への転回を経て成立した。",
    "development": "アッタール『神秘哲学』、ルーミー『マスナヴィー』の方法論的祖型として継承された。",
    "historical_context": "セルジューク朝期スーフィー思想の文学的体系化を担った。",
    "primary_source_url": GANJOOR + "sanaee/hadighe/",
    "primary_source_type": "Ganjoor: Hadiqat al-Haqiqa",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アッタール『鳥の言葉』",
    "name_en": "Attar / Mantiq al-Tayr",
    "name_original": "منطق الطیر",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "ファリードゥッディーン・アッタール（c.1145-c.1221）の代表作『鳥の言葉（Manṭiq al-Ṭayr）』。1177年頃成立、約4,500ベイトのマスナヴィー。三十羽の鳥（si murgh）が王シームルグを求めて七つの谷を越える寓話を通じ、スーフィー道行（ṭarīqa）の七階梯を体系化した。スーフィー寓話文学の最高峰。",
    "background": "ニーシャープール薬剤師として聖人伝『アウリヤーの伝記』も著した。",
    "development": "ルーミー『マスナヴィー』、ジャーミー『七つの王座』の直接の祖型となり、近代欧米にも翻訳された。",
    "historical_context": "モンゴル侵入直前のホラサーン・スーフィー文化の頂点を示す作品。",
    "primary_source_url": GANJOOR + "attar/manteghotteyr/",
    "primary_source_type": "Ganjoor: Mantiq al-Tayr",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アッタール『聖者列伝』",
    "name_en": "Attar / Tazkirat al-Awliya",
    "name_original": "تذکرة الاولیاء",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "アッタールが1220年頃完成した散文聖人伝集成『タズキラトゥ・アウリヤー』。ラービア、バーヤズィード、ハッラージュ、ジュナイドら72人のスーフィー聖者の言行録を集成し、ペルシア散文聖人伝（タズキラ）ジャンルの規範を確立した。R.A.ニコルソンによる校訂版（1905-07）が学術基準。",
    "background": "アラビア語スーフィー伝記伝統（スラミー、クシャイリー）のペルシア語による集大成。",
    "development": "ジャーミー『親愛者の息吹（Nafaḥāt al-Uns）』等のペルシア聖人伝の祖型となった。",
    "historical_context": "13世紀ペルシア散文の聖人伝ジャンル成立期。",
    "primary_source_url": IRANICA + "attar-farid-al-din-poet",
    "primary_source_type": "Encyclopaedia Iranica: Attar",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シャムス・タブリーズィー",
    "name_en": "Shams-i Tabrizi",
    "name_original": "شمس تبریزی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "シャムスッディーン・ムハンマド・タブリーズィー（c.1185-1248）はルーミーの精神的師にして変容の触媒。1244年コニヤでルーミーと邂逅し、その内的革命を引き起こした。『マカーラート（Maqālāt-i Shams）』はシャムス自身の言葉を記録した散文集で、ルーミーの『シャムス詩集（Dīvān-i Shams-i Tabrīzī）』はシャムスへの献呈詩集として成立した。",
    "background": "イスマーイール派・スンニー諸派を遍歴するスーフィー巡歴者として活動した。",
    "development": "ルーミー詩学・マウラヴィー教団の精神的源泉として正典化された。",
    "historical_context": "13世紀アナトリア・スーフィー思想の極点を象徴する人物。",
    "primary_source_url": IRANICA + "sams-e-tabrizi",
    "primary_source_type": "Encyclopaedia Iranica: Shams-e Tabrizi",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ジャーミー『七つの王座』",
    "name_en": "Jami / Haft Awrang",
    "name_original": "هفت اورنگ",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "アブドゥッラフマーン・ジャーミー（1414-1492）の七編から成るマスナヴィー集『七つの王座（Haft Awrang）』。『ユースフとズライハー』『ライラーとマジュヌーン』『サラーマンとアブサール』等を含み、ニザーミー『五詩集』伝統を継承しつつスーフィー神秘主義を全面化した。ヘラート・ティムール朝宮廷文化の頂点を示す。",
    "background": "ナクシュバンディー教団の指導者として神秘思想と詩を統合した。",
    "development": "古典ペルシア詩の最後の巨匠として、後の中央アジア・インド・トルコ詩に深く影響した。",
    "historical_context": "ティムール朝末期ヘラート文芸サークルの集大成的存在。",
    "primary_source_url": GANJOOR + "jami/7owrang/",
    "primary_source_type": "Ganjoor: Haft Awrang",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ビーデル・デフラヴィー",
    "name_en": "Bidel Dehlavi",
    "name_original": "میرزا عبدالقادر بیدل",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "サブク・ヒンディー期",
    "definition": "ミールザー・アブドゥルカーディル・ビーデル・デフラヴィー（1642-1720）はムガル朝末期インド・ペルシア詩の最高峰で、サブク・ヒンディー（インド様式）の頂点を成した詩人。極度に凝縮された比喩・抽象的形而上学イメージ・統語上の難解さで知られ、タジク・アフガン・中央アジア詩で「ビーデルハーニー（ビーデル朗誦）」の伝統を生んだ。",
    "background": "ムガル朝アウラングゼーブ期インドのペルシア語詩文化の頂点を担った。",
    "development": "20世紀タジク・アフガン詩人（ヘドリー・モハッマディー、ハリーリー）に再発見され、現代中央アジア詩の精神的源泉となった。",
    "historical_context": "イラン本土ではバーザガシュト運動により低評価を受けたが、インド・中央アジアでは正典化された。",
    "primary_source_url": IRANICA + "bidel-dehlavi-abd-al-qader",
    "primary_source_type": "Encyclopaedia Iranica: Bidel",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "サブク・ヒンディー（インド様式）",
    "name_en": "Sabk-e Hindi (Indian Style)",
    "name_original": "سبک هندی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "サブク・ヒンディー期",
    "definition": "16-18世紀ムガル朝インドおよびサファヴィー朝期に成立したペルシア詩の様式。意味の繊細化（mażmūn-tarāshī：意味の彫琢）、新奇な比喩、抽象性を追求し、サーイブ・タブリーズィー、カリーム・カーシャーニー、ビーデルらが代表する。20世紀イラン・モダニズム詩の理論家ニーマーらにより再評価された。",
    "background": "サファヴィー朝の宮廷後援衰退によるペルシア詩人のムガル朝移動という社会的条件下で成立した。",
    "development": "イラン本土では18世紀バーザガシュト（回帰）運動で否定されたが、20世紀以降再評価された。",
    "historical_context": "ペルシア詩の地理的中心がインドへ移動した近世の文化現象。",
    "primary_source_url": IRANICA + "indian-style",
    "primary_source_type": "Encyclopaedia Iranica: Indian style",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "サアディー教説詩学",
    "name_en": "Sa'di's pedagogical poetics",
    "name_original": "تعلیم سعدی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "サアディー・シーラーズィー（c.1210-c.1291）が『ブースターン（果樹園、1257）』『グリスタン（薔薇園、1258）』に確立した倫理教育詩学。物語と教訓・散文と韻文・聖と俗を交互に配置することで、世俗倫理（adab）と神秘思想を統合した。ペルシア語圏で千年以上「初等教科書」として機能し続けた。",
    "background": "中央アジア・地中海・インドへの旅と多文化体験を背景に成立した。",
    "development": "ペルシア語・ウルドゥー語・トルコ語・タジク語圏での標準教材となり、ゲーテ・エマーソンも翻訳から学んだ。",
    "historical_context": "モンゴル征服直後のシーラーズで成立し、ペルシア倫理教育の規範となった。",
    "primary_source_url": GANJOOR + "saadi/golestan/",
    "primary_source_type": "Ganjoor: Golestan + Bustan",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# B. ペルシア古典散文（8）
# ===============================================================

add({
    "name_ja": "バイハキー『歴史』",
    "name_en": "Bayhaqi / Tarikh-e Bayhaqi",
    "name_original": "تاریخ بیهقی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "アブー・ファドル・バイハキー（995-1077）が著したガズナヴィー朝史書『ターリーフ・バイハキー』。原30巻のうち6巻が現存し、特にスルターン・マスウード一世（在位1030-40）治世を中心に詳述する。文学的記述・心理描写・対話再現を駆使したペルシア散文の最高傑作で、ペルシア語歴史叙述の規範を確立した。",
    "background": "ガズナヴィー朝宮廷書記として実務記録に基づき執筆した。",
    "development": "ジュヴァイニー、ラシードゥッディーンらモンゴル期歴史書の方法的祖型となった。",
    "historical_context": "11世紀ペルシア散文文学的成熟期の頂点を示す。",
    "primary_source_url": IRANICA + "bayhaqi-abul-fazl",
    "primary_source_type": "Encyclopaedia Iranica: Bayhaqi",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ニザームルムルク『スィヤーサトナーマ』",
    "name_en": "Nizam al-Mulk / Siyasatnama",
    "name_original": "سیاست‌نامه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "セルジューク朝宰相ニザームルムルク（1018-1092）が1086-91年頃に著した統治論『スィヤーサトナーマ（統治の書）』。50章構成で、君主・宰相・軍隊・徴税・諜報・宗教政策を歴史逸話と統合して論じる。ペルシア「君主論（mirror for princes、andarznāma）」ジャンルの規範作。",
    "background": "セルジューク朝の制度設計者としての実務経験を基盤に成立した。",
    "development": "ペルシア・オスマン両圏の統治論書の祖型となり、19世紀ヨーロッパ東洋学にも翻訳された。",
    "historical_context": "セルジューク朝行政・軍事制度の理論化を担った。",
    "primary_source_url": IRANICA + "nezam-al-molk",
    "primary_source_type": "Encyclopaedia Iranica: Nezam al-Molk",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "カイ・カーウース『カーブースナーマ』",
    "name_en": "Kay Ka'us / Qabusnama",
    "name_original": "قابوس‌نامه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "ジヤール朝の君主アンスィルマアーリー・カイ・カーウース（在位1049-87）が1082年に息子ギーラーンシャーに与えた教訓書『カーブースナーマ』。44章構成で、宗教・倫理・実用知識・処世訓を子向けに体系化した。ペルシア教訓散文（andarz）ジャンルの代表作。",
    "background": "イラン土着貴族層の文化的伝統に基づいて成立した。",
    "development": "ペルシア教訓書の典型として近代まで筆写・教材化された。",
    "historical_context": "11世紀イラン在地貴族文化の文学的結晶。",
    "primary_source_url": IRANICA + "kay-kavus-b-eskandar",
    "primary_source_type": "Encyclopaedia Iranica: Kay Ka'us",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ジュヴァイニー『世界征服者の歴史』",
    "name_en": "Juvayni / Tarikh-e Jahangushay",
    "name_original": "تاریخ جهانگشای",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "アター・マリク・ジュヴァイニー（1226-1283）の歴史書『世界征服者の歴史（Tārīkh-i Jahāngushāy）』。3巻構成でチンギス・ハン・モンゴル諸王・ホラズムシャー朝・イスマーイール派の歴史を記述し、モンゴル征服史の主要史料となった。修辞的に高度な散文と、目撃者証言を統合した方法論で知られる。",
    "background": "イルハン朝バグダード総督として実地観察と公文書を活用した。",
    "development": "ラシードゥッディーン『集史』、ヴァッサーフ『歴史』のモンゴル期史学の起点。",
    "historical_context": "モンゴル支配期ペルシア・イスラーム文明の歴史的自己理解の中核。",
    "primary_source_url": IRANICA + "jovayni-ata-malek",
    "primary_source_type": "Encyclopaedia Iranica: Juvayni",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ラシードゥッディーン『集史』",
    "name_en": "Rashid al-Din / Jami al-Tawarikh",
    "name_original": "جامع التواریخ",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "イルハン朝宰相ラシードゥッディーン・ファドルッラー・ハマダーニー（1247-1318）が編纂した『集史（Jāmiʿ al-Tawārīkh）』。1300年頃ガザン・ハン勅命で開始、1310年完成。モンゴル史・イラン史・トルコ史・中国史・インド史・フランク史を統合した世界初の世界史的著作で、ペルシア散文学術最高峰。",
    "background": "宮廷医・宰相としての立場で多言語史料・諸民族証言を集成した。",
    "development": "ペルシア・アラビア・トルコ語圏の歴史叙述に決定的影響を与えた。",
    "historical_context": "モンゴル世界帝国期の文化総合の文学的結晶。",
    "primary_source_url": IRANICA + "jame-al-tawarik",
    "primary_source_type": "Encyclopaedia Iranica: Jame al-Tawarik",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ナーセル・ホスロウ『旅行記』",
    "name_en": "Nasir Khusraw / Safarnama",
    "name_original": "سفرنامه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "ナーセル・ホスロウ・クバーディヤーニー（1004-c.1088）が1052年頃完成した旅行記『サファルナーマ』。1046-52年の七年間の中近東・エジプト・メッカ巡礼旅行を記録し、明晰簡潔なペルシア散文の規範を確立した。ファーティマ朝下カイロのイスマーイール派精神受容過程も記す貴重な一次史料。",
    "background": "セルジューク朝行政官からの劇的転回後のイスマーイール派宣教師としての旅。",
    "development": "ペルシア旅行記文学の起点として後の旅行記類の規範となった。",
    "historical_context": "11世紀イスラーム世界の文化地理を伝える稀有な目撃証言。",
    "primary_source_url": IRANICA + "naser-e-khosrow",
    "primary_source_type": "Encyclopaedia Iranica: Naser-e Khosrow",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ガザーリー『幸福の錬金術』",
    "name_en": "Ghazali / Kimiya-ye Sa'adat",
    "name_original": "کیمیای سعادت",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "アブー・ハーミド・ムハンマド・ガザーリー（1058-1111）が1106年頃ペルシア語で著した『幸福の錬金術（Kīmiyā-yi Saʿādat）』。アラビア語『宗教諸学の再生（Iḥyāʾ ʿUlūm al-Dīn）』のペルシア語自家編訳版で、ペルシア教義・倫理・神秘主義散文の規範作。読者層の俗人化を意識したペルシア語による知識民主化を象徴する。",
    "background": "ニザーミーヤ学院教授職放棄後の精神的危機・遍歴経験を基盤に成立。",
    "development": "ペルシア教義散文の規範として千年にわたり読み継がれた。",
    "historical_context": "11世紀イスラーム正統スンニー神学とスーフィズムの統合期を象徴する。",
    "primary_source_url": IRANICA + "gazali-iv-",
    "primary_source_type": "Encyclopaedia Iranica: Ghazali",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ヘダーヤト『鎖』（ペルシア小品集）",
    "name_en": "Hedayat / Sag-e Velgard (short fiction)",
    "name_original": "سگ ولگرد",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "サーデク・ヘダーヤト『野良犬（Sag-e Velgard、1942）』および短編集『生き埋め（Zende be Gur、1930）』に代表されるペルシア近代短編小説。フランス自然主義・カフカ的不安・ペルシア民俗を統合した方法で、ペルシア小説形式の制度化を担った。『盲目の梟』と並ぶヘダーヤト散文の代表領域。",
    "background": "テヘラン上層知識人家庭出身、パリ留学経験を基盤とした。",
    "development": "ペルシア近代短編小説形式の規範として、20世紀後半作家（チューバク、ゴルシーリー）への祖型となった。",
    "historical_context": "1930-40年代テヘラン文学界の小説形式定着期を代表する。",
    "primary_source_url": IRANICA + "hedayat-sadeq-i-life",
    "primary_source_type": "Encyclopaedia Iranica: Hedayat",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# C. 古典トルコ拡張（8）
# ===============================================================

add({
    "name_ja": "アフメディー『イスケンデルナーメ』",
    "name_en": "Ahmedi / Iskendername",
    "name_original": "İskendernâme",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "アフメディー（c.1334-1413）の長編マスナヴィー『イスケンデルナーメ（アレクサンドル王物語）』。1390年頃完成、約8,000ベイト。ニザーミー『イスカンダル・ナーマ』のトルコ語翻案で、宇宙論・歴史・倫理を統合したオスマン文学最初期の主要作品。オスマン古典文学の起点を画す。",
    "background": "ゲルミヤン朝・オスマン朝双方に仕えた宮廷詩人として活動した。",
    "development": "オスマン宮廷マスナヴィー伝統の祖型として、後のシェイヒ・ハタイー・ガーリブに継承された。",
    "historical_context": "14世紀末アナトリアにおけるオスマン文学の制度的成立を象徴する。",
    "primary_source_url": WIKI_TR + "Ahmedi",
    "primary_source_type": "Wikipedia (TR): Ahmedi",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "シェイヒ『フスレヴ・ヴ・シーリーン』",
    "name_en": "Sheyhi / Husrev u Sirin",
    "name_original": "Hüsrev ü Şirin",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "シェイヒ（c.1371-c.1431）のマスナヴィー『フスレヴ・ヴ・シーリーン』。ニザーミー原作のトルコ語翻案で、サーサーン朝王ホスローとアルメニア王女シーリーンの恋愛を描く。15世紀前半オスマン宮廷文学の代表作の一つ。",
    "background": "オスマン宮廷医・詩人として活動した。",
    "development": "オスマン恋愛マスナヴィー伝統の規範作となった。",
    "historical_context": "ニザーミー『五詩集』のトルコ語翻案運動の中核。",
    "primary_source_url": WIKI_TR + "%C5%9Eeyhi",
    "primary_source_type": "Wikipedia (TR): Sheyhi",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "シェイヒ・ガーリブ『フスン・ヴ・アシュク』",
    "name_en": "Sheikh Galib / Hüsn ü Aşk",
    "name_original": "Hüsn ü Aşk",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "シェイヒ・ガーリブ（メフメト・エセド、1757-1799）が1782-83年完成したマスナヴィー『美と愛（Ḥüsn ü ʿAşḳ）』。約2,100ベイトで、寓意的に「美（Hüsn）」と「愛（Aşk）」の探求物語をスーフィー道行（タリーカ）として展開。オスマン古典詩の最後にして最高の総合と位置付けられる。",
    "background": "メヴレヴィー教団修道僧（ガラタ・メヴレヴィーハーネ僧院長）としての神秘主義的素養を基盤とした。",
    "development": "オスマン古典詩の頂点として近代以降も継続的に解釈・上演された。",
    "historical_context": "セリム三世期オスマン宮廷文学の頂点を画す。",
    "primary_source_url": WIKI_TR + "%C5%9Eeyh_Galib",
    "primary_source_type": "Wikipedia (TR): Sheikh Galib",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ネフィー（オスマン風刺詩）",
    "name_en": "Nef'i (Ottoman satirist)",
    "name_original": "Nef'î",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "オメル・ネフィー（c.1572-1635）はオスマン古典期最大のカスィーダ詩人にして風刺詩集『シハーム・カザー（運命の矢）』の作者。スルタン・ムラト四世期に活動し、激越な風刺で諸王侯を攻撃した結果1635年処刑された。オスマン詩における風刺（hicv）と頌詩（kaside）双方の頂点を画す。",
    "background": "エルズルム出身、オスマン宮廷詩人として活動した。",
    "development": "オスマン宮廷詩における政治的緊張と詩的力量の極限を体現した。",
    "historical_context": "17世紀オスマン宮廷文化の頂点と、詩人の政治的危険性を象徴する。",
    "primary_source_url": WIKI_TR + "Nef%27%C3%AE",
    "primary_source_type": "Wikipedia (TR): Nef'i",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ナービー（オスマン教訓詩）",
    "name_en": "Nabi (Ottoman didactic poetry)",
    "name_original": "Nâbî",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "ユースフ・ナービー（1642-1712）はオスマン古典詩における「ヒクメト派（hikmet ekolü：知恵詩学）」の創始者。マスナヴィー『ハイリーイェ』（息子へ与えた教訓書）と『ハイラーバード』が代表作で、社会風刺・倫理教説・実践的知恵を詩化した「思想詩（fikir şiiri）」を確立した。",
    "background": "ウルファ出身、オスマン官僚・詩人として活動した。",
    "development": "オスマン詩の知性主義的傾向の理論的祖型として後継者を生んだ。",
    "historical_context": "17世紀末オスマン古典詩の方法論的転換期を代表する。",
    "primary_source_url": WIKI_TR + "N%C3%A2b%C3%AE",
    "primary_source_type": "Wikipedia (TR): Nabi",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "オスマン・テズキレ（詩人列伝）",
    "name_en": "Ottoman tezkire (biographical anthology)",
    "name_original": "tezkire-i şuara",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "オスマン古典期に発達した詩人伝記集成（tezkire-i şuʿarāʾ）。サーヒー・ベイ『シャーイル・テズキレスィ』（1538）、ラティーフィー（1546）、アーシュク・チェレビー（1568）、キナルザーデ・ハサン・チェレビー（1586）等を代表とし、詩人の伝記情報・選詩・批評を統合した。オスマン文学批評の主要ジャンル。",
    "background": "ペルシア・タズキラ伝統（ダウラトシャー、ジャーミー）のオスマン語適応。",
    "development": "オスマン文学批評・正典化・文学史叙述の主要装置として19世紀末まで継続した。",
    "historical_context": "オスマン宮廷文学の自己理論化と詩人ネットワークの可視化機構。",
    "primary_source_url": WIKI_EN + "Tezkire",
    "primary_source_type": "Wikipedia: Tezkire",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "メスィヒー（オスマン抒情）",
    "name_en": "Mesihi (Ottoman lyric)",
    "name_original": "Mesihî",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "メスィヒー・プリシュティナヴィー（c.1470-1512）はバヤズィト二世期の主要オスマン詩人。『春のカスィーダ（Bahariyye）』が代表作で、18世紀英国詩人ウィリアム・ジョーンズ卿による英訳を通じヨーロッパに紹介された最初のオスマン詩人として知られる。",
    "background": "コソヴォ出身、オスマン宮廷詩人として活動した。",
    "development": "オスマン詩のヨーロッパ受容の起点を提供した。",
    "historical_context": "16世紀初頭オスマン宮廷詩の代表的詩人。",
    "primary_source_url": WIKI_EN + "Mesihi_of_Pristina",
    "primary_source_type": "Wikipedia: Mesihi",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "オスマン・メスネヴィー伝統",
    "name_en": "Ottoman mesnevi tradition",
    "name_original": "mesnevî",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "オスマン古典期に発達した二行連句叙事詩形式（mesnevî）の総体。ペルシア・マスナヴィー伝統を継承し、アフメディー『イスケンデルナーメ』からシェイヒ・ガーリブ『フスン・ヴ・アシュク』に至る五百年間にわたり、宗教教説・恋愛物語・歴史叙事・教訓を担う主要長編形式となった。各種スルタンを主題とするガザヴァートナーマ（戦記物）も含む。",
    "background": "ペルシア・マスナヴィー形式のトルコ語適応・発展として成立。",
    "development": "近代以降の長編詩・物語詩の形式的祖型として継承された。",
    "historical_context": "オスマン古典宮廷文学の長編叙事の主要装置。",
    "primary_source_url": WIKI_EN + "Mathnawi_(poetic_form)",
    "primary_source_type": "Wikipedia: Mathnawi",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# D. 近代トルコ（8）
# ===============================================================

add({
    "name_ja": "アハメト・ハムディ・タンプナル『静寂』",
    "name_en": "Ahmet Hamdi Tanpınar / Huzur",
    "name_original": "Huzur",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "アハメト・ハムディ・タンプナル（1901-1962）の長編小説『静寂（Huzur）』（1949）。第二次大戦前夜のイスタンブルを舞台に音楽家ムムタズと女性ヌーランの恋愛を中心に、伝統的オスマン文化と近代化の緊張・記憶・時間意識を内省的散文で展開した。オルハン・パムクが「我が師」と公言した近代トルコ小説の規範作。",
    "background": "イスタンブル大学トルコ文学教授として古典詩学・近代小説を架橋した。",
    "development": "パムクら現代トルコ作家の方法的源泉として正典化された。",
    "historical_context": "戦後トルコ知識人の文化的アイデンティティ問題を結晶化した。",
    "primary_source_url": WIKI_EN + "Ahmet_Hamdi_Tanp%C4%B1nar",
    "primary_source_type": "Wikipedia: Ahmet Hamdi Tanpınar",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "タンプナル『時間調整研究所』",
    "name_en": "Tanpınar / The Time Regulation Institute",
    "name_original": "Saatleri Ayarlama Enstitüsü",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "タンプナルの長編小説『時間調整研究所（Sa'atleri Ayarlama Enstitüsü）』（1962）。共和国期トルコの近代化・官僚制・伝統との関係を、架空の「時間調整研究所」を舞台に風刺的・寓話的に描く。20世紀トルコ文学の最重要小説の一つとして国際的評価を獲得した。",
    "background": "オスマン時間意識と西欧的近代時間の衝突を主題化した晩年の代表作。",
    "development": "21世紀英訳（2013）により世界文学正典に組み込まれた。",
    "historical_context": "トルコ共和国期近代化政策への文学的応答の頂点を画した。",
    "primary_source_url": WIKI_EN + "The_Time_Regulation_Institute",
    "primary_source_type": "Wikipedia: Time Regulation Institute",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アブデュルハック・シナーシ・ヒサール",
    "name_en": "Abdülhak Şinasi Hisar",
    "name_original": "Abdülhak Şinasi Hisar",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "アブデュルハック・シナーシ・ヒサール（1888-1963）はオスマン末期・共和国期トルコの記憶文学者。『ボアズィチ・メフタプラル（ボスポラスの月明かり）』（1942）、『ボアズィチ・ヨルラル（ボスポラスの古き屋敷）』（1954）等で、19世紀末オスマン上流社会の生活・建築・季節を緻密な散文で記録した。プルースト的記憶散文のトルコ的展開。",
    "background": "オスマン高官家庭出身、パリ滞在経験を持つ。",
    "development": "オスマン文化記憶のアーカイブ的散文の規範として継承された。",
    "historical_context": "共和国期に消滅したオスマン都市文化の文学的保存を担った。",
    "primary_source_url": WIKI_TR + "Abd%C3%BClhak_%C5%9Einasi_Hisar",
    "primary_source_type": "Wikipedia (TR): Hisar",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "オルハン・パムク『私の名は紅』",
    "name_en": "Orhan Pamuk / My Name Is Red",
    "name_original": "Benim Adım Kırmızı",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "オルハン・パムクの長編小説『私の名は紅（Benim Adım Kırmızı）』（1998）。16世紀末オスマン宮廷細密画家集団の殺人事件を多重話法（人物・物・色・死者の語り）で展開し、オスマン伝統絵画と西欧透視図法・宗教と表象の衝突を主題化した。2003年IMPACダブリン文学賞、ノーベル賞受賞（2006）の主要作。",
    "background": "オスマン細密画研究と多視点ポストモダン技法を統合した。",
    "development": "21世紀世界文学・歴史小説の規範作として国際的に正典化された。",
    "historical_context": "イスラーム表象論争・トルコ文化アイデンティティ論議の文学的結晶。",
    "primary_source_url": WIKI_EN + "My_Name_Is_Red",
    "primary_source_type": "Wikipedia: My Name Is Red",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ナーズム・ヒクメト",
    "name_en": "Nâzım Hikmet",
    "name_original": "Nâzım Hikmet Ran",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ナーズム・ヒクメト（1902-1963）は20世紀トルコ詩を代表する革新者。マヤコフスキー・ロシア未来派の影響下に自由詩形式と政治的・社会的主題を統合し、トルコ近代詩の構造変革を達成した。長編詩『人々の風景』（1941-1950）、『ジェコンド・ジョコンダの物語』（1936）が代表作。トルコ国籍剥奪・モスクワ亡命を経験した。",
    "background": "モスクワ留学（1922-1924）でロシア・アヴァンギャルドを摂取した。",
    "development": "トルコ自由詩運動の祖として、ベディル・タランジ・ファズル・ヒュスニュ・ダーラルジャらに継承された。",
    "historical_context": "20世紀トルコ詩の構造的革新と政治的迫害の象徴。",
    "primary_source_url": WIKI_EN + "N%C3%A2z%C4%B1m_Hikmet",
    "primary_source_type": "Wikipedia: Nazim Hikmet",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "サイト・ファーイク・アバスヤヌク",
    "name_en": "Sait Faik Abasıyanık",
    "name_original": "Sait Faik Abasıyanık",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "サイト・ファーイク・アバスヤヌク（1906-1954）は20世紀トルコ短編小説の代表作家。イスタンブル・ブユックアダ島およびマルマラ漁師・移民・周縁的人物を題材に、チェーホフ的観察と内省的抒情を統合した。トルコ短編小説の現代的規範を確立し、毎年「サイト・ファーイク短編賞」が授与される。",
    "background": "ブルサ・スイス・パリ留学経験を持ち、マルマラ社会の周縁観察を継続した。",
    "development": "トルコ近代短編小説形式の規範として後継作家に継承された。",
    "historical_context": "1940-50年代トルコ社会の文化的多様性の文学的記録。",
    "primary_source_url": WIKI_EN + "Sait_Faik_Abas%C4%B1yan%C4%B1k",
    "primary_source_type": "Wikipedia: Sait Faik",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ベディル・タランジ",
    "name_en": "Cahit Sıtkı Tarancı",
    "name_original": "Cahit Sıtkı Tarancı",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ジャヒト・スィトクィ・タランジ（1910-1956）は共和国期トルコ叙情詩を代表する詩人。詩集『時間以後（Ömrümde Sükût）』（1933）、『三十五歳（Otuz Beş Yaş）』（1946）が代表作。死・時間・存在不安を簡潔な近代トルコ語で結晶化し、トルコ抒情詩の近代的規範を確立した。",
    "background": "パリ・ソルボンヌ留学経験を経て、フランス象徴派・近代抒情詩を摂取した。",
    "development": "戦後トルコ抒情詩の主要源泉として後継詩人に影響した。",
    "historical_context": "共和国期トルコ詩のフランス象徴派受容の頂点を担った。",
    "primary_source_url": WIKI_TR + "Cahit_S%C4%B1tk%C4%B1_Taranc%C4%B1",
    "primary_source_type": "Wikipedia (TR): Tarancı",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ヤフヤ・ケマル・ベヤトル",
    "name_en": "Yahya Kemal Beyatlı",
    "name_original": "Yahya Kemal Beyatlı",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ヤフヤ・ケマル・ベヤトル（1884-1958）はオスマン古典詩学と近代トルコ詩を架橋した詩人。古典アルーズ韻律を保持しながら近代トルコ語で詩作し、歴史意識・イスタンブル・オスマン文化記憶を主題化した。詩集『古き詩の風（Eski Şiirin Rüzgârıyle）』（1962）が代表作。",
    "background": "パリ滞在（1903-1912）でアンリ・ベルクソンに学び、近代詩学を摂取した。",
    "development": "タンプナルとともに「保守近代主義」的詩学の理論的源泉として機能した。",
    "historical_context": "オスマン文化記憶を共和国期に継承する文化保守主義的詩学を担った。",
    "primary_source_url": WIKI_EN + "Yahya_Kemal_Beyatl%C4%B1",
    "primary_source_type": "Wikipedia: Yahya Kemal",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# E. 近代イラン・アフガン・タジク・アゼリ・ウズベク（8）
# ===============================================================

add({
    "name_ja": "アフマド・シャーミルー",
    "name_en": "Ahmad Shamlou",
    "name_original": "احمد شاملو",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "アフマド・シャーミルー（1925-2000）はニーマー以後最も重要な現代ペルシア詩人で、白詩（she'r-e sefid：自由詩）の創始者。詩集『新たな空気の鮮度（Hava-ye Taze）』（1957）、『花崗岩と挑戦（Mar'asi）』（1986）等で、社会的抒情と政治的告発を結合した詩学を確立した。",
    "background": "テヘラン労働者運動・左翼知識人圏内で詩人活動を行った。",
    "development": "20世紀後半ペルシア自由詩の主要規範として、現代まで読み継がれている。",
    "historical_context": "革命前後イラン社会と詩人の政治的位置の象徴。",
    "primary_source_url": IRANICA + "shamlu-ahmad",
    "primary_source_type": "Encyclopaedia Iranica: Shamlu",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ハリール・アッラー・ハリーリー",
    "name_en": "Khalilullah Khalili",
    "name_original": "خلیل‌الله خلیلی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ハリール・アッラー・ハリーリー（1907-1987）はアフガニスタン・ペルシア詩を代表する詩人・歴史家。古典韻律を保持しつつ近代主題を導入し、特にビーデル研究の20世紀的復興を主導した。著書『ビーデルとそのスーフィズム（Faiz-i Qudsī）』はサブク・ヒンディー再評価の基盤となった。",
    "background": "アフガニスタン王室との緊張関係を経て、晩年は米国・パキスタンに亡命した。",
    "development": "20世紀アフガン・ペルシア詩文化の中核的存在として規範化された。",
    "historical_context": "アフガン文学のペルシア圏内自律性確立に寄与した。",
    "primary_source_url": IRANICA + "khalili-khalilullah",
    "primary_source_type": "Encyclopaedia Iranica: Khalili",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "サドリッディーン・アイニー",
    "name_en": "Sadriddin Ayni",
    "name_original": "Садриддин Айнӣ",
    "original_script": "cyrillic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "中央アジア近現代",
    "definition": "サドリッディーン・アイニー（1878-1954）は近代タジク文学の祖。回想録『回想（Yoddoshtho）』（1948-54）、長編『奴隷たち（Ghulomon）』（1934）が代表作で、ブハラ社会の伝統的教育・革命的変革を散文化した。タジク文学のペルシア古典から近代社会主義リアリズムへの転換を主導した。",
    "background": "ブハラ伝統的教育を経てジャディード（改革派）運動に参加、その後ソヴィエト・タジク文学制度創設者となった。",
    "development": "近代タジク散文小説・回想録形式の規範を確立した。",
    "historical_context": "ペルシア圏東部における近代国民文学制度成立の中核。",
    "primary_source_url": WIKI_EN + "Sadriddin_Ayni",
    "primary_source_type": "Wikipedia: Sadriddin Ayni",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ロイク・シェラリ",
    "name_en": "Loiq Sherali",
    "name_original": "Лоиқ Шералӣ",
    "original_script": "cyrillic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "中央アジア近現代",
    "definition": "ロイク・シェラリ（1941-2000）は20世紀後半タジク詩を代表する詩人。古典ペルシア韻律と近代抒情を統合し、タジク民族意識・ペルシア文学伝統への回帰・ソヴィエト後期の社会的緊張を主題化した。詩集『ロザン（窓）』『ホクル（叫び）』が代表作。",
    "background": "ソ連時代後期タジキスタン文学界の中心的詩人として活動した。",
    "development": "現代タジク詩の主要規範として現在まで広く朗誦されている。",
    "historical_context": "ソヴィエト末期タジク民族意識の文学的再構築を担った。",
    "primary_source_url": WIKI_EN + "Loiq_Sherali",
    "primary_source_type": "Wikipedia: Loiq Sherali",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ミルザ・アラクバル・サービル",
    "name_en": "Mirza Alakbar Sabir",
    "name_original": "Mirzə Ələkbər Sabir",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "中央アジア近現代",
    "definition": "ミルザ・アラクバル・サービル（1862-1911）は近代アゼルバイジャン詩の祖。風刺雑誌『モッラー・ナスレッディン（Molla Nasraddin）』（1906-1931）の中心詩人として、伝統的ムスリム社会の保守性・植民地状況・社会改革を風刺した。詩集『ホップ・ホップナーマ』（1912）が代表作。",
    "background": "シャマフ出身、近代アゼルバイジャン啓蒙運動の中心人物として活動した。",
    "development": "近代アゼルバイジャン文学・トルコ系諸言語風刺詩の規範を確立した。",
    "historical_context": "ロシア領アゼルバイジャンの社会改革運動と文学的近代化の合流点。",
    "primary_source_url": WIKI_EN + "Mirza_Alakbar_Sabir",
    "primary_source_type": "Wikipedia: Sabir",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ムハンマドフセイン・シャフリヤール",
    "name_en": "Mohammad-Hossein Shahriar",
    "name_original": "محمدحسین شهریار",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "中央アジア近現代",
    "definition": "ムハンマドフセイン・ベフジャト・タブリーズィー（1906-1988、雅号シャフリヤール）はペルシア語・アゼルバイジャン語両方で書いた20世紀イラン最大の詩人の一人。アゼリ語長編詩『ハイダル・ババへの挨拶（Heydar Babaya Salam）』（1954）はアゼリ近代詩の最高傑作とされ、ペルシア語のガザル・カスィーダ群もハーフェズ伝統の20世紀的継承として高く評価される。",
    "background": "イラン領アゼルバイジャン・タブリーズ出身、医学を修めた後詩人として活動した。",
    "development": "アゼリ・ペルシア両言語圏で正典化され、毎年9月18日「シャフリヤールの日（イラン詩の日）」が制定されている。",
    "historical_context": "20世紀イラン多言語文学の象徴的人物。",
    "primary_source_url": IRANICA + "shahriar-mohammad-hosayn",
    "primary_source_type": "Encyclopaedia Iranica: Shahriar",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アブドゥッラフ・カディリー",
    "name_en": "Abdulla Qodiriy",
    "name_original": "Abdulla Qodiriy",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "中央アジア近現代",
    "definition": "アブドゥッラフ・カディリー（1894-1938）は近代ウズベク小説の祖。長編歴史小説『過ぎし日々（Oʻtkan kunlar）』（1922-26）、『サソリの巣窟より（Mehrobdan chayon）』（1929）で、19世紀コーカンド・ハン国を舞台にウズベク社会の近代化・伝統と恋愛を描いた。スターリン期粛清で1938年処刑、1956年復権。",
    "background": "ジャディード改革運動の文化的継承者として活動した。",
    "development": "近代ウズベク小説形式の規範として、現代まで読み継がれている。",
    "historical_context": "中央アジア近代化と社会主義粛清の双方を象徴する作家。",
    "primary_source_url": WIKI_EN + "Abdulla_Qodiriy",
    "primary_source_type": "Wikipedia: Abdulla Qodiriy",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "チョルパン",
    "name_en": "Cho'lpon",
    "name_original": "Choʻlpon",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "中央アジア近現代",
    "definition": "アブドゥルハミド・スレイマーン・ユヌスオグリ（1897-1938、雅号チョルパン：明けの明星）は近代ウズベク詩・劇文学の祖。詩集『朝（Tong sirlari）』（1926）、長編小説『夜と昼（Kecha va kunduz）』（1936）で、ウズベク社会の近代化・植民地状況・女性解放を主題化した。1938年スターリン期粛清で処刑、1989年復権。",
    "background": "ジャディード運動とロシア革命後の中央アジア近代化運動の中心人物の一人。",
    "development": "近代ウズベク自由詩・近代散文の起点として正典化された。",
    "historical_context": "中央アジア近代文学運動の悲劇的象徴。",
    "primary_source_url": WIKI_EN + "Cho%CA%BClpon",
    "primary_source_type": "Wikipedia: Cho'lpon",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ---------------------------------------------------------------
# Fourth-transform tagging (>=12)
# ---------------------------------------------------------------
FOURTH_TRANSFORM_TAGS = {
    "サナーイー『真理の園』": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "コーラン解釈・寓話・神秘体験を統合した教説詩学は、AIによる多層テキスト統合生成の歴史的祖型。",
         "ai_phenomenon": "AI生成テキストの多層統合構造"},
    ],
    "アッタール『鳥の言葉』": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "三十羽の鳥がシームルグへ至る七谷物語は、複数主体の集合的探究という構造で、AI生成における「群知能（swarm intelligence）」物語論と類比される。",
         "ai_phenomenon": "AI生成における群知能・集合的物語"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "三十羽の鳥（si murgh）が王シームルグ自身であるという結末は、主体の集合性・分散性を提示し、AI主体論の祖型。",
         "ai_phenomenon": "AI生成における集合的・分散的主体"},
    ],
    "アッタール『聖者列伝』": [
        {"axis": "正典", "status": "partial",
         "rationale": "72聖者の体系的伝記集成は、LLMの人物プロフィール生成・検索の歴史的祖型として位置付けられる。",
         "ai_phenomenon": "LLMの人物プロファイル生成・整理"},
    ],
    "ビーデル・デフラヴィー": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "極度に凝縮された比喩・抽象的形而上学イメージ・統語上の難解さは、AI解釈の限界事例として注目される。",
         "ai_phenomenon": "LLMによる難解詩の解釈限界"},
        {"axis": "正典", "status": "rethinking",
         "rationale": "イラン本土での低評価とインド・中央アジアでの正典化の地理的分裂は、AI翻訳による地域別正典の動態を予示する。",
         "ai_phenomenon": "AI翻訳による地域別正典の動態"},
    ],
    "サブク・ヒンディー（インド様式）": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "意味の繊細化（mażmūn-tarāshī：意味の彫琢）は、LLMによる微細な意味選択・新奇な比喩生成の歴史的祖型。",
         "ai_phenomenon": "LLMの微細な意味選択・新奇比喩生成"},
    ],
    "オスマン・テズキレ（詩人列伝）": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "詩人伝記集成・批評・選詩の統合形式は、LLMによる文学正典の集約・要約・推薦機能の祖型として再評価される。",
         "ai_phenomenon": "LLMによる文学正典の集約・推薦"},
    ],
    "シェイヒ・ガーリブ『フスン・ヴ・アシュク』": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "美と愛の擬人化による寓意的探求物語は、AI生成における抽象概念の擬人化・物語化の祖型。",
         "ai_phenomenon": "AI生成における抽象概念の擬人化・物語化"},
    ],
    "オスマン・メスネヴィー伝統": [
        {"axis": "正典", "status": "invariant"},
    ],
    "アハメト・ハムディ・タンプナル『静寂』": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "オスマン文化と近代化の緊張・記憶を内省的散文で展開した方法は、AI時代の文化的ハイブリッド性の再考枠組みとなる。",
         "ai_phenomenon": "AI時代の文化的ハイブリッド表現"},
    ],
    "タンプナル『時間調整研究所』": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "オスマン時間意識と近代時間の衝突を風刺した寓話は、AI時代の時間性・同時性の再考枠組みを提供する。",
         "ai_phenomenon": "AI時代の時間性・同期性の再考"},
    ],
    "オルハン・パムク『私の名は紅』": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "細密画の匿名性と西欧透視図法の作者主体の対照は、AI生成における作者性問題の歴史的祖型として再評価される。",
         "ai_phenomenon": "AI生成における作者性・匿名性問題"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "人物・物・色・死者が次々と語る多重話法は、LLMによる多視点ナラティブ生成の文学的祖型。",
         "ai_phenomenon": "LLMによる多視点ナラティブ生成"},
    ],
    "ナーズム・ヒクメト": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "古典アルーズ韻律を解体し自由詩形式と政治的主題を統合した運動は、AI生成における形式自由化の歴史的祖型。",
         "ai_phenomenon": "AI生成における形式拘束の解体"},
    ],
    "アフマド・シャーミルー": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "白詩（she'r-e sefid）の創始は、ニーマーに続くペルシア詩の形式革新で、AI生成の自由形式詩学の祖型として継承される。",
         "ai_phenomenon": "AI自由形式詩学の歴史的祖型"},
    ],
    "ムハンマドフセイン・シャフリヤール": [
        {"axis": "言語", "status": "partial",
         "rationale": "ペルシア語とアゼリ語両方で書く二言語詩学は、AI多言語生成の歴史的祖型として位置付けられる。",
         "ai_phenomenon": "AI多言語生成・コードスイッチング"},
    ],
    "サドリッディーン・アイニー": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "古典ペルシアから近代社会主義リアリズムへの言語・文学制度転換を主導した方法は、AI時代の文学正典再編の歴史的祖型。",
         "ai_phenomenon": "AI時代の文学正典再編"},
    ],
    "アブドゥッラフ・カディリー": [
        {"axis": "受容", "status": "partial",
         "rationale": "粛清・処刑後の復権・再評価過程は、AI翻訳・分析による失われた作家の復権可能性と類比される。",
         "ai_phenomenon": "AI分析による失われた作家の復権"},
    ],
}


# ---------------------------------------------------------------
# Cross-domain links (>=8)
# ---------------------------------------------------------------
CROSS_DOMAIN_LINKS = [
    ("アッタール『鳥の言葉』", "PHIL", "shared_concept", "Sufi seven valleys / mystic ascent",
     "七谷の体系はスーフィー神秘主義道行論の核心で、哲学DBのスーフィズム認識論と直接共有される。"),
    ("ニザームルムルク『スィヤーサトナーマ』", "PHIL", "shared_concept", "mirror for princes / political philosophy",
     "君主論ジャンルはイスラーム政治哲学の中核で、哲学DBの政治哲学項目と接続する。"),
    ("ガザーリー『幸福の錬金術』", "PHIL", "shared_concept", "Ghazali / Sunni mysticism integration",
     "スンニー神学とスーフィズムの統合は哲学DBの中核項目として共有される。"),
    ("ビーデル・デフラヴィー", "AI-Development", "parallel", "LLM interpretive limit",
     "ビーデルの極度に凝縮された比喩・抽象性は、LLMの詩解釈限界事例として理論的に重要である。"),
    ("オスマン・テズキレ（詩人列伝）", "AI-Development", "parallel", "LLM canonical curation",
     "詩人伝記集成・批評・選詩統合形式は、LLMの正典集約・推薦機能の文学的祖型として再評価される。"),
    ("オルハン・パムク『私の名は紅』", "AI-Development", "parallel", "LLM multi-perspective generation",
     "細密画家・物・色・死者の多重話法はLLMの多視点ナラティブ生成と直接接続する。"),
    ("ナーズム・ヒクメト", "AI-Development", "parallel", "AI free-verse generation",
     "アルーズ韻律解体と自由詩確立は、AI生成における形式拘束の解体と歴史的に並行する。"),
    ("アッタール『聖者列伝』", "AN", "shared_concept", "hagiography / oral memory tradition",
     "聖者言行録ジャンルは人類学的口承・聖人崇拝研究の対象で、人類学DBと共有される。"),
    ("オスマン・メスネヴィー伝統", "PT", "shared_concept", "long narrative verse / world poetics",
     "二行連句長編叙事形式は世界詩学の主要形式の一つで、詩学DBと共有される。"),
    ("ムハンマドフセイン・シャフリヤール", "PT", "shared_concept", "bilingual poetics",
     "ペルシア語・アゼリ語の二言語詩学は世界二言語詩学研究の主要事例として詩学DBと共有される。"),
    ("ジュヴァイニー『世界征服者の歴史』", "AN", "shared_concept", "Mongol historiography / cross-cultural witness",
     "モンゴル征服史叙述は人類学的他者証言研究の主要対象で、人類学DBと共有される。"),
    ("ラシードゥッディーン『集史』", "AN", "shared_concept", "world history / cross-cultural ethnography",
     "世界初の世界史的著作は人類学的多文化総合の文学的祖型として人類学DBと共有される。"),
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

        print(f"\n=== Wave11 C22 Persian-Turkish ADD40 completed ===")
        print(f"  concepts inserted: {inserted} (skipped: {skipped})")
        print(f"  fourth-transform tags: {ft_count}")
        print(f"  cross-domain links: {cd_count}")
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 14"
        ).fetchone()
        print(f"  total concepts in subfield 14: {row['c']}")


if __name__ == "__main__":
    main()
