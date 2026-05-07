"""LIT-DB Phase 2 Wave 18 — C22 ADD60 Persian & Turkish Literature.

Adds 60 new non-overlapping concepts to subfield_id=14 (lit_persian_turkish).
Sources: Ganjoor, Encyclopaedia Iranica, Wikisource, Tashlh, academic Wikipedia.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


PERIODS_TO_SEED = [
    ("ペルシア古典初期（サーマーン・ガズナ）", "Early Classical Persian", 900, 1100,
     "サーマーン朝・ガズナ朝期、ペルシア新詩誕生期。"),
    ("ペルシア古典中期（セルジューク・ホラズム）", "Middle Classical Persian", 1037, 1258,
     "セルジューク朝・モンゴル前夜のペルシア古典詩学黄金期。"),
    ("ペルシア古典後期（イルハン・ティムール）", "Late Classical Persian", 1258, 1500,
     "モンゴル期からティムール朝。古典完成期。"),
    ("ペルシア古典散文期", "Persian Classical Prose", 950, 1500,
     "ペルシア散文の歴史叙述・聖人伝・統治論・倫理書の確立期。"),
    ("サブク・ヒンディー期", "Sabk-e Hindi (Indian Style)", 1500, 1750,
     "ムガル朝期インド・ペルシア詩学。"),
    ("オスマン古典期（ディーワーン文学）", "Ottoman Classical (Diwan)", 1300, 1839,
     "オスマン宮廷詩文化。"),
    ("オスマン民俗・テッケ詩", "Ottoman Folk / Tekke Poetry", 1240, 1900,
     "ユヌス・エムレからアシュク詩人までの民俗・神秘詩。"),
    ("近現代ペルシア・トルコ", "Modern Persian / Turkish", 1900, 2025,
     "ニーマー以後・共和国期散文。"),
    ("中央アジア近現代", "Modern Central Asia", 1900, 2025,
     "タジク・ウズベク近代文学。"),
    ("クルド・パシュトー・バローチ・スィンディー文学", "Kurdish/Pashto/Balochi/Sindhi Lit", 1500, 2025,
     "周辺イラン語派・南アジア・スーフィー詩学圏。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


GANJOOR = "https://ganjoor.net/"
IRANICA = "https://iranicaonline.org/articles/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_TR = "https://tr.wikipedia.org/wiki/"
WIKI_FA = "https://fa.wikipedia.org/wiki/"
WIKISOURCE = "https://en.wikisource.org/wiki/"


# =====================================================
# A. ペルシア古典補完（Rudaki/Daqiqi/Shahnameh sections）10
# =====================================================

add({
    "name_ja": "ルーダキー『ディーワーン』",
    "name_en": "Rudaki / Divan",
    "name_original": "دیوان رودکی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン・ガズナ）",
    "definition": "ペルシア詩の父ルーダキー（c.858-941）の散逸・断片詩集。カスィーダ・ガザル・ルバーイー約1,000ベイトが現存し、新ペルシア語詩の規範を確立した。",
    "background": "サーマーン朝宮廷詩人の頂点として活動。",
    "development": "ガズナ朝ウンスリー・ファッルヒーらに継承された。",
    "historical_context": "10世紀ペルシア新詩誕生期の中核。",
    "primary_source_url": GANJOOR + "roodaki/",
    "primary_source_type": "Ganjoor: Rudaki Divan",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ダキーキー『シャー・ナーメ断片』",
    "name_en": "Daqiqi / Shahnameh Fragment",
    "name_original": "شاهنامه دقیقی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン・ガズナ）",
    "definition": "ダキーキー・トゥースィー（d.c.977）が着手し未完で殺害されたシャー・ナーメ草稿の千ベイト断片。ザラスシュトラ宗教導入部を扱い、フェルドウスィーが自作に組み入れた。",
    "background": "サーマーン朝宮廷詩人として活動。",
    "development": "フェルドウスィーがダキーキー作と明示して継承した。",
    "historical_context": "ペルシア民族叙事詩の前史。",
    "primary_source_url": IRANICA + "daqiqi-abu-mansur",
    "primary_source_type": "Encyclopaedia Iranica: Daqiqi",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "シャー・ナーメ『ロスタムとソフラーブ』",
    "name_en": "Shahnameh / Rostam and Sohrab",
    "name_original": "رستم و سهراب",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン・ガズナ）",
    "definition": "フェルドウスィー『シャー・ナーメ』中最も悲劇的な父子相剋物語。ロスタムが我が子ソフラーブと知らずに殺す悲劇で、世界文学の運命悲劇典型として正典化された。",
    "background": "古代イラン英雄叙事の伝承を文字化したもの。",
    "development": "アーノルド英訳『Sohrab and Rustum』（1853）等で世界文学化した。",
    "historical_context": "ペルシア民族叙事の悲劇構造の中核。",
    "primary_source_url": GANJOOR + "ferdousi/shahname/",
    "primary_source_type": "Ganjoor: Shahnameh",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "シャー・ナーメ『スィヤーヴァシュ』",
    "name_en": "Shahnameh / Siavash",
    "name_original": "سیاوش",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン・ガズナ）",
    "definition": "シャー・ナーメ中の純潔王子スィヤーヴァシュの悲劇。継母の讒言、火の試練、トゥラン亡命と殉教で構成され、ペルシア純潔・無垢殉難物語の祖型。",
    "background": "古代イラン儀礼伝承（スィヤーヴァシャーン）を文学化。",
    "development": "中央アジアスィヤーヴァシュ哀悼儀礼として民俗的に継承された。",
    "historical_context": "ペルシア悲劇英雄主題の基盤。",
    "primary_source_url": GANJOOR + "ferdousi/shahname/siavash/",
    "primary_source_type": "Ganjoor: Siavash",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "シャー・ナーメ『ビージャンとマニージェ』",
    "name_en": "Shahnameh / Bizhan and Manijeh",
    "name_original": "بیژن و منیژه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン・ガズナ）",
    "definition": "シャー・ナーメ中の恋愛叙事。イラン勇士ビージャンとトゥラン王女マニージェの悲恋・幽閉・救出を描き、ペルシア恋愛叙事の祖型を提示した。",
    "background": "夜の枕物語形式で導入される独立性の高い物語単位。",
    "development": "ニザーミー恋愛叙事五詩集の祖型として継承された。",
    "historical_context": "ペルシア叙事詩内恋愛挿話の典型。",
    "primary_source_url": GANJOOR + "ferdousi/shahname/bizhanmanizhe/",
    "primary_source_type": "Ganjoor: Bizhan-Manizhe",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "シャー・ナーメ『エスファンディヤール』",
    "name_en": "Shahnameh / Esfandiyar",
    "name_original": "اسفندیار",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン・ガズナ）",
    "definition": "シャー・ナーメ中、ゾロアスター教擁護者王子エスファンディヤールとロスタムの宿命的決闘物語。「七つの試練（haft khwan）」と父王ゴシュターサプの陰謀を含む宗教・政治叙事。",
    "background": "アヴェスタ伝承の英雄サイクルをペルシア化。",
    "development": "ペルシア宗教・政治劇の祖型として正典化された。",
    "historical_context": "ペルシア古代英雄期最終局面を象徴。",
    "primary_source_url": GANJOOR + "ferdousi/shahname/",
    "primary_source_type": "Ganjoor: Shahnameh / Esfandiyar",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "シャー・ナーメ『カイ・カーウースのマーザンダラーン遠征』",
    "name_en": "Shahnameh / Kavus Mazandaran Expedition",
    "name_original": "هفت‌خوان رستم",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン・ガズナ）",
    "definition": "カイ・カーウース王のマーザンダラーン遠征とロスタムの七つの試練（haft khwan）。盲目化した王を救出するロスタムの冒険でペルシア英雄ケルティケの祖型。",
    "background": "古代イラン王権・英雄関係の典型構造を提示。",
    "development": "イスラーム期ペルシア冒険物語の規範となった。",
    "historical_context": "ペルシア英雄叙事の冒険構造の起源。",
    "primary_source_url": GANJOOR + "ferdousi/shahname/",
    "primary_source_type": "Ganjoor: Shahnameh / Haft Khwan",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "シャー・ナーメ『ホスロウ・パルヴィーズ』",
    "name_en": "Shahnameh / Khosrow Parviz",
    "name_original": "خسرو پرویز",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン・ガズナ）",
    "definition": "シャー・ナーメ末尾サーサーン朝サイクル中、ホスロウ二世パルヴィーズと美姫シーリーンの恋愛・宮廷劇・対ローマ遠征・転落史。ニザーミー『ホスロウとシーリーン』の物語源泉。",
    "background": "サーサーン朝史実とパフラヴィー物語伝承の融合。",
    "development": "ニザーミー、デフラヴィー、ナヴァーイーの五詩集中核物語として継承された。",
    "historical_context": "ペルシア宮廷恋愛叙事の正典源泉。",
    "primary_source_url": GANJOOR + "ferdousi/shahname/khosrop/",
    "primary_source_type": "Ganjoor: Khosrow Parviz",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "シャー・ナーメ『アヌーシルヴァーン』",
    "name_en": "Shahnameh / Anushirvan",
    "name_original": "انوشیروان",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典初期（サーマーン・ガズナ）",
    "definition": "シャー・ナーメ中サーサーン朝ホスロウ一世アヌーシルヴァーンの治世。賢相ボゾルグメフルとの問答・公正裁判・カリーラとディムナ翻訳挿話を含む統治理想叙事。",
    "background": "イスラーム期ペルシア『正義の王』言説の源泉。",
    "development": "ニザームルムルク『スィヤーサトナーマ』等の鏡論祖型となった。",
    "historical_context": "ペルシア政治理想叙事の中核。",
    "primary_source_url": GANJOOR + "ferdousi/shahname/",
    "primary_source_type": "Ganjoor: Anushirvan",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ハーフェズ『ディーワーン』体系的注釈伝統",
    "name_en": "Hafez Divan / Commentary Tradition",
    "name_original": "شرح دیوان حافظ",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ハーフェズ約500ガザル群の体系的読解伝統。ホッラムシャーヒー、フォルーザーンファル、シメル等の詩節別注釈で、神秘的・恋愛的・政治風刺的多層解釈が確立された。",
    "background": "ハーフェズ詩のイハーム（多義性）が多重注釈伝統を生んだ。",
    "development": "20世紀以降学術的校訂・西欧学者翻訳で世界文学化した。",
    "historical_context": "ペルシア注釈学の最高度発展形態。",
    "primary_source_url": GANJOOR + "hafez/",
    "primary_source_type": "Ganjoor: Hafez Divan",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})


# =====================================================
# B. ペルシア・スーフィー詩深耕（10）
# =====================================================

add({
    "name_ja": "アッタール『神秘哲学の書（アスラール・ナーメ）』",
    "name_en": "Attar / Asrar Nama",
    "name_original": "اسرارنامه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "アッタール初期のスーフィー教説マスナヴィー『秘密の書』。22章構成で神秘体験・霊魂論・道行段階を寓話化。ルーミー幼年期にアッタールから贈呈された逸話で知られる。",
    "background": "アッタール体系の青年期作品とされる。",
    "development": "ルーミー『マスナヴィー』形式の祖型の一つ。",
    "historical_context": "12世紀ホラサーン・スーフィー文学の核心。",
    "primary_source_url": GANJOOR + "attar/asrarname/",
    "primary_source_type": "Ganjoor: Asrar Nama",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "アッタール『苦難の書（ムシーバト・ナーメ）』",
    "name_en": "Attar / Musibat Nama",
    "name_original": "مصیبت‌نامه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "アッタールの長編教説マスナヴィー『苦難の書』。サーリク（求道者）が40日の心の旅で諸界・諸存在を巡り神秘的真理に至る寓話で、内的旅程の体系化。",
    "background": "アッタール晩年の総合的教説詩。",
    "development": "ルーミー神秘旅程詩学の直接の祖型となった。",
    "historical_context": "ペルシア・スーフィー教説詩の体系的完成形。",
    "primary_source_url": GANJOOR + "attar/mosibatname/",
    "primary_source_type": "Ganjoor: Musibat Nama",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "アッタール『神の書（イラーヒー・ナーメ）』",
    "name_en": "Attar / Ilahi Nama",
    "name_original": "الهی‌نامه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典中期（セルジューク・ホラズム）",
    "definition": "アッタール『神の書（イラーヒー・ナーメ）』。父王と六王子の対話形式で世俗的欲望と霊的真理の対比を体系化したマスナヴィー教説詩。",
    "background": "対話形式マスナヴィーの規範例。",
    "development": "後世スーフィー対話詩の祖型となった。",
    "historical_context": "12世紀末ペルシア対話詩学の核心。",
    "primary_source_url": GANJOOR + "attar/elahiname/",
    "primary_source_type": "Ganjoor: Ilahi Nama",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ルーミー『マスナヴィー第一巻』",
    "name_en": "Rumi / Masnavi Book I",
    "name_original": "مثنوی دفتر اول",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ルーミー『マスナヴィー・マアナヴィー』第一巻（約4,000ベイト）。冒頭「葦笛の歌」で別離と帰還の神秘哲学を提示し、マスナヴィー全体の主題的設計図を確立した。",
    "background": "弟子フサームッディーン・チャラビーの請いで開始。",
    "development": "ニコルソン校訂英訳が世界基準を提供した。",
    "historical_context": "13世紀ペルシア・スーフィー詩の頂点。",
    "primary_source_url": GANJOOR + "moulavi/masnavi/daftar1/",
    "primary_source_type": "Ganjoor: Masnavi I",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ルーミー『マスナヴィー第三巻』",
    "name_en": "Rumi / Masnavi Book III",
    "name_original": "مثنوی دفتر سوم",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ルーミー『マスナヴィー』第三巻。預言者言行録解釈と寓話を密に編んだ巻で、エゴ（nafs）と神聖（rūḥ）の対立を最も深く展開した。",
    "background": "中期マスナヴィー思索の頂点。",
    "development": "近代欧米スーフィー研究で集中的に注釈された。",
    "historical_context": "13世紀後半コニヤのスーフィー教育中核。",
    "primary_source_url": GANJOOR + "moulavi/masnavi/daftar3/",
    "primary_source_type": "Ganjoor: Masnavi III",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ルーミー『ディーワーン・シャムス』",
    "name_en": "Rumi / Divan-e Shams",
    "name_original": "دیوان شمس",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ルーミーが師シャムス・タブリーズィーの名で編んだ約3,500ガザル・1,983ルバーイーから成る抒情詩集。陶酔的愛と一体化を激烈な詩語で表現し、ペルシア神秘抒情の頂点。",
    "background": "シャムスとの邂逅・別離が創作の根源。",
    "development": "コールマン・バークス英訳で世界的人気を獲得。",
    "historical_context": "13世紀コニヤのスーフィー抒情の核心。",
    "primary_source_url": GANJOOR + "moulavi/shams/",
    "primary_source_type": "Ganjoor: Divan-e Shams",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ルーミー『フィーヒ・マー・フィーヒ』",
    "name_en": "Rumi / Fihi ma Fihi",
    "name_original": "فیه ما فیه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ルーミーの講話集『その中にあるもの』。71章のスーフィー教育談話を弟子が記録した散文集で、マスナヴィー詩学の散文的基盤を提示する。",
    "background": "弟子集会の口述教育記録。",
    "development": "アーバリー英訳で西欧スーフィー研究の基礎資料となった。",
    "historical_context": "13世紀スーフィー散文教育の典型。",
    "primary_source_url": IRANICA + "fihi-ma-fihi",
    "primary_source_type": "Encyclopaedia Iranica: Fihi ma Fihi",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "サアディー『ブースターン』教訓構造",
    "name_en": "Sa'di / Bustan Didactic Structure",
    "name_original": "بوستان",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "サアディー『ブースターン』（1257）の10巻分構成。正義・恩恵・愛・謙譲・足ること・満足・教育・感謝・悔悟・神への祈祷の教訓体系で、ペルシア倫理叙事詩の規範。",
    "background": "サアディーが30年放浪後シーラーズで編纂。",
    "development": "イスラーム圏全域で道徳教育教材として正典化された。",
    "historical_context": "ペルシア教訓詩学の体系的完成。",
    "primary_source_url": GANJOOR + "saadi/boostan/",
    "primary_source_type": "Ganjoor: Bustan",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ジャーミー『ユースフとズライハー』",
    "name_en": "Jami / Yusuf wa Zulaykha",
    "name_original": "یوسف و زلیخا",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ジャーミー七詩集中の恋愛叙事『ユースフとズライハー』（1483）。コーランのユースフ物語をスーフィー恋愛として再構築し、約4,000ベイトで魂と神の合一を寓意化した。",
    "background": "イブン・アラビー存在一性論をペルシア恋愛叙事に翻訳。",
    "development": "ムガル朝・オスマン朝で度々翻案された。",
    "historical_context": "ペルシア古典最後の恋愛叙事の規範。",
    "primary_source_url": GANJOOR + "jami/3-haftowrang2/",
    "primary_source_type": "Ganjoor: Yusuf-Zulaykha",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ジャーミー『サラマーンとアブサール』",
    "name_en": "Jami / Salaman wa Absal",
    "name_original": "سلامان و ابسال",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ジャーミー七詩集中のヘルメス的寓話マスナヴィー『サラマーンとアブサール』。プトレマイオス系ヘレニズム恋愛寓話をスーフィー化したもので、知性と感性の合一を主題化。",
    "background": "ヘレニズム伝承のペルシア・スーフィー化。",
    "development": "フィッツジェラルド英訳（1856）で西欧紹介。",
    "historical_context": "ペルシア寓意詩のヘルメス的延長。",
    "primary_source_url": GANJOOR + "jami/7-haftowrang2/",
    "primary_source_type": "Ganjoor: Salaman-Absal",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})


# =====================================================
# C. ペルシア散文・歴史（5）
# =====================================================

add({
    "name_ja": "ジュヴァイニー『世界征服者の歴史』詳論",
    "name_en": "Juvayni / Tarikh-i Jahangushay",
    "name_original": "تاریخ جهانگشای",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "アタ・マリク・ジュヴァイニー（1226-1283）著『世界征服者の歴史』全三巻（1252-1260）。チンギス・ハーン以降のモンゴル征服を目撃証言として記録、ペルシア装飾散文の頂点。",
    "background": "イルハン朝官僚として現地調査。",
    "development": "ボイル英訳（1958）が世界基準。",
    "historical_context": "13世紀ペルシア散文歴史記述の核心。",
    "primary_source_url": IRANICA + "jovayni-ata-malek",
    "primary_source_type": "Encyclopaedia Iranica: Juvayni",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ラシードゥッディーン『集史』詳論",
    "name_en": "Rashid al-Din / Jami al-Tawarikh",
    "name_original": "جامع التواریخ",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "ラシードゥッディーン・ハマダーニー（1247-1318）著『集史』。世界初の世界史的著作で、モンゴル・中国・インド・フランク・トルコ・ユダヤ史を統合的に編纂、複数言語証言を駆使。",
    "background": "イルハン朝宰相として国際情報網を活用。",
    "development": "近代世界史学・人類学的他者表象論の祖型。",
    "historical_context": "14世紀世界史叙述の最高峰。",
    "primary_source_url": IRANICA + "jame-al-tawarikh",
    "primary_source_type": "Encyclopaedia Iranica: Jami al-Tawarikh",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "カリーラとディムナ（ペルシア版）",
    "name_en": "Kalila wa Dimna (Persian)",
    "name_original": "کلیله و دمنه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "サンスクリット『パンチャタントラ』のパフラヴィー経由アラビア語版を、ナスルッラー・モンシー（12世紀）がペルシア装飾散文化した寓話集。動物寓話による政治・倫理教育の規範。",
    "background": "ササン朝・アッバース朝経由でペルシア化。",
    "development": "オスマン版『フマーユーン・ナーメ』、ヴァーエズ・カーシェフィー『アンワーリ・スハイリー』へ展開。",
    "historical_context": "汎ユーラシア寓話伝承の中核ハブ。",
    "primary_source_url": IRANICA + "kalila-wa-demna-i",
    "primary_source_type": "Encyclopaedia Iranica: Kalila wa Demna",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ヴァーエズ・カーシェフィー『アンワーリ・スハイリー』",
    "name_en": "Va'ez Kashifi / Anwar-i Suhayli",
    "name_original": "انوار سهیلی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典後期（イルハン・ティムール）",
    "definition": "ホセイン・ヴァーエズ・カーシェフィー（d.1504）著『カノープスの光』。『カリーラとディムナ』をティムール朝後期ペルシア装飾散文で再構築した寓話集で、ムガル朝で標準教科書化。",
    "background": "ヘラート文化サークルの中心人物。",
    "development": "ムガル朝経由で英領インド翻訳基盤となった。",
    "historical_context": "ティムール朝後期ペルシア寓話散文の頂点。",
    "primary_source_url": IRANICA + "anwar-e-sohayli",
    "primary_source_type": "Encyclopaedia Iranica: Anwar-e Sohayli",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "トゥーティー・ナーメ（ペルシア・オウムの書）",
    "name_en": "Tutinama (Persian)",
    "name_original": "طوطی‌نامه",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "ペルシア古典散文期",
    "definition": "ジヤー・ナフシャビー（d.1350）著『トゥーティー・ナーメ』。賢いオウムが旅人妻に52夜物語る枠物語形式の寓話集で、サンスクリット『シュカサプタティ』のペルシア化。",
    "background": "ティムール朝期ペルシア枠物語形式の典型。",
    "development": "ムガル朝期豪華絵入り写本の主要対象となった。",
    "historical_context": "汎ユーラシア枠物語伝承のペルシア結節点。",
    "primary_source_url": IRANICA + "tuti-nama",
    "primary_source_type": "Encyclopaedia Iranica: Tutinama",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})


# =====================================================
# D. サブク・ヒンディー詳細（5）
# =====================================================

add({
    "name_ja": "サーイブ・タブリーズィー",
    "name_en": "Sa'eb Tabrizi",
    "name_original": "صائب تبریزی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "サブク・ヒンディー期",
    "definition": "サーイブ・タブリーズィー（c.1592-1676）はサブク・ヒンディー最大のガザル詩人で、約12万ベイトを残した。マズムーン・タラーシー（意味の彫琢）と新奇比喩で17世紀ペルシア詩学を主導した。",
    "background": "イスファハーン・ムガル宮廷で活動、後シャー・アッバース二世桂冠詩人。",
    "development": "現代イラン・タジク・アフガンで再評価が進む。",
    "historical_context": "17世紀汎ペルシア詩文化のハブ。",
    "primary_source_url": GANJOOR + "saeb/",
    "primary_source_type": "Ganjoor: Saeb Divan",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "カリーム・カーシャーニー",
    "name_en": "Kalim Kashani",
    "name_original": "کلیم کاشانی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "サブク・ヒンディー期",
    "definition": "アブー・タリーブ・カリーム・カーシャーニー（c.1581-1651）はムガル朝シャー・ジャハーン桂冠詩人。サブク・ヒンディーのガザル・カスィーダで知られ、社会観察的アフォリズム性と凝縮的比喩を統合した。",
    "background": "イスファハーン出身、デリー・カシミール宮廷で活動。",
    "development": "アフガン・タジク詩文化で広く朗誦される。",
    "historical_context": "ムガル朝ペルシア宮廷詩文化の頂点の一人。",
    "primary_source_url": GANJOOR + "kalim/",
    "primary_source_type": "Ganjoor: Kalim Kashani",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ナズィーリー・ニーシャープーリー",
    "name_en": "Naziri Nishapuri",
    "name_original": "نظیری نیشابوری",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "サブク・ヒンディー期",
    "definition": "ナズィーリー・ニーシャープーリー（d.1612）はムガル朝アクバル期の主要ペルシア詩人。サブク・ヒンディー初期形成期のガザルで、形而上学的繊細さと哲学的省察を特徴とした。",
    "background": "ニーシャープールからインドへ移住、ジャイプールで活動。",
    "development": "サーイブ等後継サブク・ヒンディー詩人に深く影響。",
    "historical_context": "16-17世紀ムガル朝ペルシア詩学の中核。",
    "primary_source_url": IRANICA + "naziri-nishapuri",
    "primary_source_type": "Encyclopaedia Iranica: Naziri",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ファイズィー・アクバル宮廷詩人",
    "name_en": "Faizi (Akbar Court)",
    "name_original": "فیضی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "サブク・ヒンディー期",
    "definition": "アブー・ル・ファイズ・ファイズィー（1547-1595）はムガル朝アクバル宮廷桂冠詩人で、宰相アブー・ル・ファズルの兄。ペルシア語五詩集（ハムセ）構想と、サンスクリット『リーラーヴァティー』翻訳で知られる。",
    "background": "アクバル「Din-e Ilahi」プロジェクトの文化中核。",
    "development": "ムガル多宗教統合文化の象徴的詩人。",
    "historical_context": "16世紀末ムガル朝ペルシア宮廷文化の頂点。",
    "primary_source_url": IRANICA + "fayzi-faizi",
    "primary_source_type": "Encyclopaedia Iranica: Faizi",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ガザーリー・マシュハディー",
    "name_en": "Ghazali Mashhadi",
    "name_original": "غزالی مشهدی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "サブク・ヒンディー期",
    "definition": "ガザーリー・マシュハディー（c.1526-1572）はムガル朝アクバル初代マレク・アル＝シュアラー（桂冠詩人）。サブク・ヒンディー初期形式形成に寄与、神秘的・哲学的省察と詩的革新を結合した。",
    "background": "マシュハドからインドへ移住、後アクバル宮廷詩人。",
    "development": "サブク・ヒンディー先駆として影響を残した。",
    "historical_context": "16世紀ムガル朝ペルシア詩学の起点。",
    "primary_source_url": IRANICA + "gazali-mashhadi",
    "primary_source_type": "Encyclopaedia Iranica: Ghazali Mashhadi",
    "importance_score": 3, "source_tier": "primary", "canonical_in_region": "regional",
})


# =====================================================
# E. オスマン古典補完（6）
# =====================================================

add({
    "name_ja": "ユヌス・エムレ",
    "name_en": "Yunus Emre",
    "name_original": "Yunus Emre",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン民俗・テッケ詩",
    "definition": "ユヌス・エムレ（c.1240-c.1321）は中世アナトリア・トルコ語スーフィー詩の祖。シラブ韻律のイラーヒー（神讃歌）でアナトリア・トルコ語による神秘詩を確立、トルコ民俗・テッケ詩学の規範。",
    "background": "ハジ・ベクタシュ系・メウラーナ系神秘主義圏で活動。",
    "development": "20世紀トルコ民俗・近代詩双方で広く受容。",
    "historical_context": "アナトリア・トルコ語文学の起点。",
    "primary_source_url": WIKI_TR + "Yunus_Emre",
    "primary_source_type": "Wikipedia (TR): Yunus Emre",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "フズーリー『レイラとメジュヌーン』",
    "name_en": "Fuzuli / Leyla vu Mecnun",
    "name_original": "Leylâ vü Mecnûn",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "ムハンマド・フズーリー（1494-1556）著オスマン・トルコ語マスナヴィー『レイラとメジュヌーン』（1535）。アラブ・ペルシア伝承をオスマン語スーフィー恋愛叙事に再構築、トルコ古典恋愛叙事の頂点。",
    "background": "イラク（バグダード）出身、三言語（アゼリ・アラビア・ペルシア）で創作。",
    "development": "後世オスマン恋愛叙事の規範として正典化。",
    "historical_context": "16世紀オスマン語スーフィー恋愛叙事の頂点。",
    "primary_source_url": WIKI_TR + "Leyl%C3%A2_v%C3%BC_Mecn%C3%BBn_(Fuzul%C3%AE)",
    "primary_source_type": "Wikipedia (TR): Fuzuli Leyla Mecnun",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "バーキー（オスマン・スルターン詩人）",
    "name_en": "Baki",
    "name_original": "Bâkî",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "マフムード・アブドゥルバーキー（1526-1600）はスュレイマン大帝期オスマン・ディーワーン詩の頂点。ガザル・カスィーデで知られ、特にスュレイマン死を悼む『カヌーニー追悼詩』が古典化。",
    "background": "オスマン・ウルマー階級出身、シャイヒュル・イスラム職を歴任。",
    "development": "古典オスマン抒情詩の規範として継承された。",
    "historical_context": "16世紀後半オスマン宮廷詩学の頂点。",
    "primary_source_url": WIKI_TR + "B%C3%A2k%C3%AE",
    "primary_source_type": "Wikipedia (TR): Baki",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ネディーム（チューリップ時代詩人）",
    "name_en": "Nedim",
    "name_original": "Nedim",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン古典期（ディーワーン文学）",
    "definition": "アフメト・ネディーム（c.1681-1730）は『チューリップ時代』（Lale Devri）の代表詩人。シャルクィ（オスマン・トルコ語形式歌謡）と都市享楽詩を確立し、イスタンブル日常生活を典雅な詩語で表現した。",
    "background": "アフメト三世大宰相ネヴシェヒルリ・ダーマト・イブラヒム・パシャの庇護下で活動。",
    "development": "オスマン後期都市抒情詩の規範となった。",
    "historical_context": "18世紀初頭オスマン都市文化の文学的結晶。",
    "primary_source_url": WIKI_TR + "Nedim_(divan_%C5%9Fairi)",
    "primary_source_type": "Wikipedia (TR): Nedim",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "カラジャオウラン",
    "name_en": "Karacaoğlan",
    "name_original": "Karacaoğlan",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン民俗・テッケ詩",
    "definition": "カラジャオウラン（17世紀）はアナトリア南部チュクロヴァ地方のアシュク（吟遊詩人）。シラブ韻律の民俗叙情詩で、自然・恋愛・遊牧民生活を平易なトルコ語で歌い、アシュク詩学の規範。",
    "background": "テュルクメン遊牧民圏出身の吟遊詩人。",
    "development": "近代トルコ民俗詩学・民族主義詩学の源泉として再評価。",
    "historical_context": "17世紀アナトリア民俗抒情の頂点。",
    "primary_source_url": WIKI_TR + "Karacao%C4%9Flan",
    "primary_source_type": "Wikipedia (TR): Karacaoğlan",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ピール・スルタン・アブダル",
    "name_en": "Pir Sultan Abdal",
    "name_original": "Pir Sultan Abdal",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "オスマン民俗・テッケ詩",
    "definition": "ピール・スルタン・アブダル（16世紀）はアレヴィー・ベクタシ詩学の中心詩人。シラブ韻律のネフェス（神霊歌）でシーア派的神秘主義と社会的反抗を結合し、現代トルコ抵抗詩の象徴となった。",
    "background": "シヴァス・バナズ出身、オスマン総督への反抗で処刑伝承。",
    "development": "20世紀左翼・社会民主主義運動の文化的アイコンとなった。",
    "historical_context": "オスマン期アレヴィー詩学の頂点。",
    "primary_source_url": WIKI_TR + "Pir_Sultan_Abdal",
    "primary_source_type": "Wikipedia (TR): Pir Sultan Abdal",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})


# =====================================================
# F. 近代トルコ深掘り（9）
# =====================================================

add({
    "name_ja": "ハーリデ・エディプ『シネクリ・バッカル』",
    "name_en": "Halide Edip / Sinekli Bakkal",
    "name_original": "Sinekli Bakkal",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ハーリデ・エディプ・アドゥヴァル（1884-1964）著小説『蝿どまりの食料品店』（1936）。アブデュルハミト二世期イスタンブル下町を舞台に、女性主体の宗教・西欧化対立を描き共和国期写実小説の頂点。",
    "background": "独立戦争従軍経験を持つ女性知識人。",
    "development": "20世紀トルコ女性文学の規範として正典化。",
    "historical_context": "共和国期写実主義の頂点の一つ。",
    "primary_source_url": WIKI_TR + "Sinekli_Bakkal",
    "primary_source_type": "Wikipedia (TR): Sinekli Bakkal",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "レシャト・ヌリ・ギュンテキン『チャル・クシュ』",
    "name_en": "Reşat Nuri / Çalıkuşu",
    "name_original": "Çalıkuşu",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "レシャト・ヌリ・ギュンテキン（1889-1956）著『ミソサザイ』（1922）。若い女性教師フェリーデのアナトリア奉職を通じ、共和国期女性主体・地方教育・近代国民意識を描き国民的小説となった。",
    "background": "教師としての経験を作品化。",
    "development": "ラジオ・映画・テレビで何度も翻案された国民的物語。",
    "historical_context": "共和国期国民教育・女性主体形成の文学的結晶。",
    "primary_source_url": WIKI_TR + "%C3%87al%C4%B1ku%C5%9Fu",
    "primary_source_type": "Wikipedia (TR): Çalıkuşu",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ヤクプ・カドリ『ヤバン』",
    "name_en": "Yakup Kadri / Yaban",
    "name_original": "Yaban",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ヤクプ・カドリ・カラオスマンオール（1889-1974）著『よそ者』（1932）。独立戦争期アナトリア村に避難した知識人将校の視点で、都市知識人と地方民の文化的断絶を描いた共和国期主要小説。",
    "background": "カダロ運動知識人として共和国文化政策に関与。",
    "development": "共和国期都市・地方分断議論の文学的源泉。",
    "historical_context": "1930年代トルコ知識人問題の文学的告白。",
    "primary_source_url": WIKI_TR + "Yaban_(roman)",
    "primary_source_type": "Wikipedia (TR): Yaban",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "サバハッティン・アリ『毛皮のマドンナ』",
    "name_en": "Sabahattin Ali / Madonna in a Fur Coat",
    "name_original": "Kürk Mantolu Madonna",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "サバハッティン・アリ（1907-1948）著小説『毛皮のマドンナ』（1943）。1920年代ベルリンを舞台にトルコ青年ライフとユダヤ系画家マリアの恋愛を描き、内省的男性主体・近代喪失・トランスナショナル恋愛を主題化。",
    "background": "ベルリン留学経験を背景化。",
    "development": "21世紀トルコで再発見され大ベストセラーとなった。",
    "historical_context": "戦間期トルコ・ヨーロッパ知識人交流の文学的結晶。",
    "primary_source_url": WIKI_TR + "K%C3%BCrk_Mantolu_Madonna",
    "primary_source_type": "Wikipedia (TR): Kürk Mantolu Madonna",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ヤシャル・ケマル『鷹のメメッド』",
    "name_en": "Yaşar Kemal / Memed My Hawk",
    "name_original": "İnce Memed",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ヤシャル・ケマル（1923-2015）四部作『鷹のメメッド』（1955-1987）。チュクロヴァ平原の山賊メメッドを通じ、地主搾取・農民反抗・アナトリア神話世界を叙事詩的散文で描いたトルコ農村文学の頂点。",
    "background": "クルド系出身、チュクロヴァ調査をベース化。",
    "development": "40言語以上に翻訳、ノーベル賞候補。",
    "historical_context": "20世紀後半トルコ社会派叙事散文の頂点。",
    "primary_source_url": WIKI_TR + "%C4%B0nce_Memed",
    "primary_source_type": "Wikipedia (TR): İnce Memed",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ラティフェ・テキン『愛しい無頼の死』",
    "name_en": "Latife Tekin / Dear Shameless Death",
    "name_original": "Sevgili Arsız Ölüm",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ラティフェ・テキン（1957-）著小説『愛しい無頼の死』（1983）。アナトリア村からイスタンブル都市スラムへの移住家族を、口承伝承・魔術的リアリズム・女性語りで描いたトルコ・マジックリアリズムの代表作。",
    "background": "東部アナトリア村出身、自身の家族経験を素材化。",
    "development": "トルコ女性・ポストモダン・口承統合文学の規範となった。",
    "historical_context": "1980年代トルコ社会変動の文学的結晶。",
    "primary_source_url": WIKI_TR + "Sevgili_Ars%C4%B1z_%C3%96l%C3%BCm",
    "primary_source_type": "Wikipedia (TR): Sevgili Arsız Ölüm",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "アダレト・アアオール『死ぬために横たわる』",
    "name_en": "Adalet Ağaoğlu / Lying Down to Die",
    "name_original": "Ölmeye Yatmak",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "アダレト・アアオール（1929-2020）著三部作冒頭小説（1973）。共和国期女性大学教員アイセルの内的独白で、共和国近代化・女性主体・1968年世代を意識流技法で描いた。",
    "background": "ラジオ放送局勤務後作家活動。",
    "development": "トルコ女性意識流小説の規範として正典化。",
    "historical_context": "1970年代トルコ女性主体問題の文学的結晶。",
    "primary_source_url": WIKI_TR + "%C3%96lmeye_Yatmak",
    "primary_source_type": "Wikipedia (TR): Ölmeye Yatmak",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "オルハン・ヴェリ『ガリプ』",
    "name_en": "Orhan Veli / Garip",
    "name_original": "Garip",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "オルハン・ヴェリ・カヌク（1914-1950）他三人共著詩集『奇妙』（1941）。日常言語・口語・庶民生活を主題化し、オスマン古典詩学の徹底的解体を達成、近代トルコ詩の方向転換。",
    "background": "オクタイ・ルファト・メリチ・ジェヴデト・アンダイとの三人運動。",
    "development": "戦後トルコ詩学の主要源泉となった。",
    "historical_context": "1940年代トルコ詩革命の起点。",
    "primary_source_url": WIKI_TR + "Garip_(kitap)",
    "primary_source_type": "Wikipedia (TR): Garip",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "イフサン・オクタイ・アナル『霧の大陸地図』",
    "name_en": "İhsan Oktay Anar / Atlas of Misty Continents",
    "name_original": "Puslu Kıtalar Atlası",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "イフサン・オクタイ・アナル（1960-）著小説『霧の大陸地図』（1995）。17世紀イスタンブルを舞台に、アラビアン・ナイト風寓話・ボルヘス的迷宮性・オスマン秘教を融合した21世紀トルコポストモダン代表作。",
    "background": "エーゲ大学哲学者として活動。",
    "development": "21世紀トルコポストモダン・歴史小説の規範。",
    "historical_context": "1990年代トルコ文学新世代の象徴。",
    "primary_source_url": WIKI_TR + "Puslu_K%C4%B1talar_Atlas%C4%B1",
    "primary_source_type": "Wikipedia (TR): Puslu Kıtalar Atlası",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})


# =====================================================
# G. 近代イラン深掘り（8）
# =====================================================

add({
    "name_ja": "ヘダーヤト『盲目の梟』詳論",
    "name_en": "Hedayat / Buf-e Kur",
    "name_original": "بوف کور",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "サーデク・ヘダーヤト（1903-1951）著『盲目の梟』（1937）。アヘン中毒画家の悪夢的独白で、ペルシア近代散文の心理小説・モダニズムを完成させた20世紀イラン散文の頂点。",
    "background": "パリ留学・カフカ受容を反映。",
    "development": "20世紀ペルシア小説の規範として世界的に翻訳。",
    "historical_context": "20世紀イラン・モダニズムの頂点。",
    "primary_source_url": IRANICA + "buf-e-kur",
    "primary_source_type": "Encyclopaedia Iranica: Buf-e Kur",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "アル・アフマド『西洋中毒』",
    "name_en": "Al-e Ahmad / Gharbzadegi",
    "name_original": "غرب‌زدگی",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ジャラール・アル・アフマド（1923-1969）著評論『西洋中毒』（1962）。イラン社会の西欧近代主義依存を「病」として診断、革命前イラン知識人言説の核心となったエッセイ。",
    "background": "シーア派伝統・近代化緊張の知識人として活動。",
    "development": "イラン革命前後の文化政策論議の核心テクストとなった。",
    "historical_context": "1960-70年代イラン知識人論議の起点。",
    "primary_source_url": IRANICA + "garbzadegi",
    "primary_source_type": "Encyclopaedia Iranica: Gharbzadegi",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ダーネシュヴァル『スーヴァシューン』",
    "name_en": "Daneshvar / Suvashun",
    "name_original": "سووشون",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "シミーン・ダーネシュヴァル（1921-2012）著『スーヴァシューン』（1969）。第二次大戦期シーラーズを舞台に、英国占領・地主階級・女性主体を統合的に描いたイラン女性作家初の長編小説の規範。",
    "background": "夫アル・アフマドと並ぶ近代イラン文学夫婦の一翼。",
    "development": "イラン女性文学の規範として正典化された。",
    "historical_context": "20世紀後半イラン女性主体文学の起点。",
    "primary_source_url": IRANICA + "savushun",
    "primary_source_type": "Encyclopaedia Iranica: Savushun",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "フォルーグ・ファッロホザード『新たに誕生する』",
    "name_en": "Forough Farrokhzad / Tavalludi Digar",
    "name_original": "تولدی دیگر",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "フォルーグ・ファッロホザード（1934-1967）詩集『新たに誕生する』（1964）。女性自我の革命的告白と社会批判を結合した代表作で、イラン女性詩学の頂点を確立した。",
    "background": "離婚・映画監督・短い生涯を通じ詩人として急成長。",
    "development": "20世紀後半イラン女性詩・自由詩の規範として継承。",
    "historical_context": "1960年代イラン女性主体革命の文学的結晶。",
    "primary_source_url": IRANICA + "farrokhzad-forough",
    "primary_source_type": "Encyclopaedia Iranica: Farrokhzad",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ソフラブ・セペフリー『ハシュト・キターブ』",
    "name_en": "Sohrab Sepehri / Hasht Ketab",
    "name_original": "هشت کتاب",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ソフラブ・セペフリー（1928-1980）詩集『八つの書』（1977）。仏教・スーフィー・自然詩学を統合したペルシア・モダニズム詩の集大成で、長編詩『水の足音』が代表作。",
    "background": "画家としても活動、東洋・仏教旅行を素材化。",
    "development": "20世紀後半イラン精神詩学の規範として継承。",
    "historical_context": "1970年代イラン精神詩学の頂点。",
    "primary_source_url": IRANICA + "sepehri-sohrab",
    "primary_source_type": "Encyclopaedia Iranica: Sepehri",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "アフヴァン・サーレス『冬』",
    "name_en": "Akhavan-Sales / Zemestan",
    "name_original": "زمستان",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "メフディー・アフヴァン・サーレス（1929-1990）詩集『冬』（1956）。1953年クーデター後のイラン政治的失意を、ニーマー新詩形式とペルシア古典叙事的格調で結合した代表作。",
    "background": "モサッデク政権崩壊後の政治的幻滅を背景化。",
    "development": "ニーマー以後ペルシア社会派詩学の規範として継承。",
    "historical_context": "1950-60年代イラン政治失意の詩的結晶。",
    "primary_source_url": IRANICA + "akhavan-thaleth-mehdi",
    "primary_source_type": "Encyclopaedia Iranica: Akhavan-Sales",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "マフムード・ドウラトアバーディー『キレダル』",
    "name_en": "Mahmoud Dowlatabadi / Kelidar",
    "name_original": "کلیدر",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "マフムード・ドウラトアバーディー（1940-）著大長編小説『キレダル』全10巻（1977-1984）。ホラサーン地方クルド系遊牧民を描いた約3,000頁のペルシア叙事散文の頂点。",
    "background": "故郷ホラサーン社会調査を素材化。",
    "development": "現代ペルシア叙事散文最大の達成として正典化。",
    "historical_context": "20世紀後半イラン地方文学の頂点。",
    "primary_source_url": IRANICA + "dowlatabadi-mahmud",
    "primary_source_type": "Encyclopaedia Iranica: Dowlatabadi",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "サーエディー『恐怖と震え』",
    "name_en": "Saedi / Tars o Larz",
    "name_original": "ترس و لرز",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "近現代ペルシア・トルコ",
    "definition": "ゴラームホセイン・サーエディー（1936-1985）著短編集『恐怖と震え』（1968）。ペルシア湾岸漁村を舞台に、悪霊・地霊伝承と政治寓話を結合したペルシア・マジックリアリズムの代表作。",
    "background": "精神科医として地域調査を素材化。",
    "development": "イラン地域文化伝承を文学化する規範となった。",
    "historical_context": "1960年代イラン社会派寓話文学の頂点。",
    "primary_source_url": IRANICA + "saedi-gholam-hosayn",
    "primary_source_type": "Encyclopaedia Iranica: Saedi",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})


# =====================================================
# H. クルド・パシュトー・バローチ・スィンディー（7）
# =====================================================

add({
    "name_ja": "エフメデー・ハーニー『メムーとズィーン』",
    "name_en": "Ehmedê Xanî / Mem û Zîn",
    "name_original": "Mem û Zîn",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "クルド・パシュトー・バローチ・スィンディー文学",
    "definition": "エフメデー・ハーニー（1651-1707）著クルド語マスナヴィー『メムとズィーン』（1692）。クルド民族叙事恋愛詩で、悲恋を通じクルド民族意識を提示し、近代クルド文学の祖型となった。",
    "background": "ハッカリ地方ボタン・クルド神学者として活動。",
    "development": "20世紀クルド民族運動の文化的シンボルとなった。",
    "historical_context": "近代クルド民族意識の文学的起点。",
    "primary_source_url": WIKI_EN + "Mem_and_Zin",
    "primary_source_type": "Wikipedia: Mem and Zin",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ジゲルフィン",
    "name_en": "Cigerxwîn",
    "name_original": "Cigerxwîn",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "クルド・パシュトー・バローチ・スィンディー文学",
    "definition": "シェイフムス・ハサン（1903-1984、雅号ジゲルフィン：燃える肝）は20世紀クルド・クルマンジー方言詩の祖。社会主義的政治詩と古典韻律を結合し、近代クルド民族・社会意識を体系化した。",
    "background": "シリア・レバノン・スウェーデン亡命を経て活動。",
    "development": "20世紀後半クルド民族運動の文化的中核となった。",
    "historical_context": "20世紀クルド近代詩学の起点。",
    "primary_source_url": WIKI_EN + "Cegerxw%C3%AEn",
    "primary_source_type": "Wikipedia: Cigerxwin",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "シェルコ・ベカス",
    "name_en": "Sherko Bekas",
    "name_original": "Şêrko Bêkes",
    "original_script": "roman",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "クルド・パシュトー・バローチ・スィンディー文学",
    "definition": "シェルコ・ベカス（1940-2013）はイラク・クルド・ソラニー方言を代表する20世紀後半詩人。「ルワンゲ運動」（1971）で自由詩革命を主導、近代クルド詩学の主流を形成した。",
    "background": "クルド民族運動家家系出身、亡命・帰還を経て活動。",
    "development": "ソラニー・クルド詩学の20世紀後半規範として継承。",
    "historical_context": "イラク・クルド近代詩運動の頂点。",
    "primary_source_url": WIKI_EN + "Sherko_Bekas",
    "primary_source_type": "Wikipedia: Sherko Bekas",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ホシャール・ハン・ハッタク",
    "name_en": "Khushal Khan Khattak",
    "name_original": "خوشحال خان خټک",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "クルド・パシュトー・バローチ・スィンディー文学",
    "definition": "ホシャール・ハン・ハッタク（1613-1689）はパシュトー詩文の祖。ムガル朝アウラングゼーブへの抵抗運動を主導しつつ約45,000ベイトを残し、戦争・愛・パシュトン名誉を統合した近代パシュトー文学の規範。",
    "background": "ハッタク部族長として政治・軍事・詩作を兼ねた。",
    "development": "20世紀パシュトーン民族意識の文化的中核となった。",
    "historical_context": "近世南アジア・パシュトー文学の頂点。",
    "primary_source_url": WIKI_EN + "Khushal_Khan_Khattak",
    "primary_source_type": "Wikipedia: Khushal Khan Khattak",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ラフマーン・ババー",
    "name_en": "Rahman Baba",
    "name_original": "رحمان بابا",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "クルド・パシュトー・バローチ・スィンディー文学",
    "definition": "アブドゥッラフマーン・モフマンド（c.1632-c.1706）はパシュトー神秘詩学の祖。ペシャーワル近郊で活動し、スーフィー神秘主義と平易なパシュトー語を結合した詩集が現代まで深い宗教的権威を持つ。",
    "background": "モフマンド部族出身、スーフィー道師として活動。",
    "development": "現代パシュトーン文化圏で「パシュトーンのハーフェズ」と呼ばれる。",
    "historical_context": "17世紀パシュトー神秘詩学の頂点。",
    "primary_source_url": WIKI_EN + "Rahman_Baba",
    "primary_source_type": "Wikipedia: Rahman Baba",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "シャー・アブドゥル・ラティーフ・ビッタイ『シャー・ジョー・リサーロ』",
    "name_en": "Shah Abdul Latif Bhittai / Shah Jo Risalo",
    "name_original": "شاه جو رسالو",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "クルド・パシュトー・バローチ・スィンディー文学",
    "definition": "シャー・アブドゥル・ラティーフ・ビッタイ（1689-1752）著スィンディー語詩集『シャー・ジョー・リサーロ』。30章構成のスーフィー詩集成で、スィンド民俗ロマンスをスーフィー神秘主義化、近代スィンディー文学の規範。",
    "background": "ビット・シャー・ジョーで活動するスーフィー詩人。",
    "development": "現代スィンド文化圏で最高権威の詩人として正典化。",
    "historical_context": "18世紀スィンディー・スーフィー詩学の頂点。",
    "primary_source_url": WIKI_EN + "Shah_Jo_Risalo",
    "primary_source_type": "Wikipedia: Shah Jo Risalo",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "サチャル・サルマスト",
    "name_en": "Sachal Sarmast",
    "name_original": "سچل سرمست",
    "original_script": "arabic",
    "subfield_code": "lit_persian_turkish",
    "region": "南西アジア",
    "period_key": "クルド・パシュトー・バローチ・スィンディー文学",
    "definition": "サチャル・サルマスト（1739-1827）はスィンド・パンジャブ国境地域の七言語スーフィー詩人。スィンディー・サライキー・パンジャービー・ペルシア・アラビア・ウルドゥー・バローチ語で詩作し、汎南アジア・スーフィー詩学を象徴する。",
    "background": "ダラージャ・スィンド出身、巡礼放浪詩人として活動。",
    "development": "現代パキスタン多言語スーフィー詩学の規範。",
    "historical_context": "18-19世紀南アジア多言語スーフィー詩学の頂点。",
    "primary_source_url": WIKI_EN + "Sachal_Sarmast",
    "primary_source_type": "Wikipedia: Sachal Sarmast",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})


# =====================================================
# Fourth-transform tags (target >=18)
# =====================================================
FOURTH_TRANSFORM_TAGS = {
    "ルーダキー『ディーワーン』": [
        {"axis": "正典", "status": "invariant",
         "rationale": "ペルシア新詩規範を確立した断片詩集はAI時代でも歴史的起点として不動。",
         "ai_phenomenon": "AIによるペルシア起源詩学の規範化"},
    ],
    "シャー・ナーメ『ロスタムとソフラーブ』": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "父子相剋悲劇はAI生成における運命構造・倫理的選択生成の祖型として再評価される。",
         "ai_phenomenon": "AI生成における運命悲劇構造"},
    ],
    "シャー・ナーメ『スィヤーヴァシュ』": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "純潔殉難物語はAI物語生成における「無垢の主体」生成パターンの祖型。",
         "ai_phenomenon": "AI生成における純潔主体構造"},
    ],
    "ハーフェズ『ディーワーン』体系的注釈伝統": [
        {"axis": "解釈", "status": "rethinking",
         "rationale": "イハーム（多義性）に対する複層注釈伝統はLLM多解釈生成の歴史的祖型。",
         "ai_phenomenon": "LLMによる多義テクスト解釈"},
        {"axis": "正典", "status": "rethinking",
         "rationale": "詩節別多重注釈伝統はAI注釈・解釈生成の祖型として再評価される。",
         "ai_phenomenon": "AI注釈生成のモデル"},
    ],
    "アッタール『神秘哲学の書（アスラール・ナーメ）』": [
        {"axis": "正典", "status": "partial",
         "rationale": "22章スーフィー教説の体系化はAI時代の知識体系化の歴史的祖型。",
         "ai_phenomenon": "AI知識体系化の祖型"},
    ],
    "ルーミー『マスナヴィー第一巻』": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "葦笛の別離哲学は分離・帰還構造でAI主体論の祖型として再考される。",
         "ai_phenomenon": "AI主体性における分離・帰還"},
    ],
    "ルーミー『ディーワーン・シャムス』": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "他者（シャムス）名義での創作は作者性の分散・複数性として、AI共著・代理生成の祖型。",
         "ai_phenomenon": "AI共著・名義代理生成"},
    ],
    "サアディー『ブースターン』教訓構造": [
        {"axis": "正典", "status": "invariant",
         "rationale": "10巻倫理体系はAI時代でも教訓詩学の規範として不動。",
         "ai_phenomenon": "AI倫理生成の歴史的源泉"},
    ],
    "ジャーミー『ユースフとズライハー』": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "コーラン物語のスーフィー詩化はAI多層テクスト変換の歴史的祖型。",
         "ai_phenomenon": "AI多層テクスト変換"},
    ],
    "ジュヴァイニー『世界征服者の歴史』詳論": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "目撃証言型歴史記述はAI証言データ生成・歴史記述の祖型として再評価。",
         "ai_phenomenon": "AI歴史記述・証言生成"},
    ],
    "ラシードゥッディーン『集史』詳論": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "世界初の世界史的著作は多文化総合的AI知識統合の祖型として再評価。",
         "ai_phenomenon": "AI多文化知識統合"},
    ],
    "カリーラとディムナ（ペルシア版）": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "汎ユーラシア寓話伝承は、AI物語多言語翻訳・伝承生成の祖型。",
         "ai_phenomenon": "AI寓話多言語生成"},
    ],
    "サーイブ・タブリーズィー": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "意味の彫琢（mazmun-tarashi）は、AI生成における新奇比喩・凝縮表現の祖型。",
         "ai_phenomenon": "AI生成における凝縮的比喩"},
    ],
    "ユヌス・エムレ": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "口語アナトリア・トルコ語による神秘詩は、AI多方言生成の祖型として再評価。",
         "ai_phenomenon": "AI民俗言語・口語生成"},
    ],
    "フズーリー『レイラとメジュヌーン』": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "アラブ起源恋愛伝承のオスマン語スーフィー化は、AI物語ローカライゼーション祖型。",
         "ai_phenomenon": "AI物語の文化的翻訳"},
    ],
    "ハーリデ・エディプ『シネクリ・バッカル』": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "女性主体・宗教近代化対立はAI時代のジェンダー・近代再考の祖型。",
         "ai_phenomenon": "AI時代のジェンダー再考"},
    ],
    "ヤシャル・ケマル『鷹のメメッド』": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "アナトリア叙事詩散文化は、AI地方文学正典化の祖型。",
         "ai_phenomenon": "AI地方文学正典化"},
    ],
    "ラティフェ・テキン『愛しい無頼の死』": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "口承伝承・女性語りの統合は、AI生成における口承・多重声の歴史的祖型。",
         "ai_phenomenon": "AI口承・多重声生成"},
    ],
    "オルハン・ヴェリ『ガリプ』": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "古典詩学解体・日常言語化は、AI生成における口語・日常生成の祖型。",
         "ai_phenomenon": "AI日常言語詩学"},
    ],
    "ヘダーヤト『盲目の梟』詳論": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "悪夢的独白・不安定主体は、AI生成における不安定主体・幻覚（hallucination）構造の祖型。",
         "ai_phenomenon": "AI不安定主体・幻覚構造"},
    ],
    "フォルーグ・ファッロホザード『新たに誕生する』": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "女性自我の革命的告白は、AI時代のジェンダー詩学再考の祖型。",
         "ai_phenomenon": "AI時代の女性主体詩学"},
    ],
    "マフムード・ドウラトアバーディー『キレダル』": [
        {"axis": "受容", "status": "partial",
         "rationale": "10巻3,000頁の長大叙事は、AI長文生成・記憶保持の限界事例として参照される。",
         "ai_phenomenon": "AI長文生成限界"},
    ],
    "エフメデー・ハーニー『メムーとズィーン』": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "クルド民族意識文学起点は、AI少数言語文学正典化の祖型。",
         "ai_phenomenon": "AI少数言語文学正典化"},
    ],
    "シャー・アブドゥル・ラティーフ・ビッタイ『シャー・ジョー・リサーロ』": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "民俗ロマンスのスーフィー化はAI民俗-神秘伝承統合生成の祖型。",
         "ai_phenomenon": "AI民俗・神秘伝承統合"},
    ],
    "サチャル・サルマスト": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "七言語並行詩作は、AI多言語生成・コードスイッチングの歴史的祖型として再評価。",
         "ai_phenomenon": "AI多言語コードスイッチング"},
    ],
}


# =====================================================
# Cross-domain links (target >=14)
# =====================================================
CROSS_DOMAIN_LINKS = [
    ("シャー・ナーメ『ロスタムとソフラーブ』", "AN", "shared_concept", "father-son tragedy / kinship anthropology",
     "父子相剋悲劇は人類学的親族構造研究と接続する。"),
    ("シャー・ナーメ『スィヤーヴァシュ』", "AN", "shared_concept", "ritual mourning / Siavashan ceremony",
     "中央アジアのスィヤーヴァシュ哀悼儀礼は人類学儀礼研究と共有される。"),
    ("シャー・ナーメ『アヌーシルヴァーン』", "PHIL", "shared_concept", "Persian mirror for princes",
     "賢相ボゾルグメフルとの問答は政治哲学・統治論として哲学DBと共有。"),
    ("ハーフェズ『ディーワーン』体系的注釈伝統", "AI-Development", "parallel", "LLM multi-interpretation",
     "イハーム多義性への複層注釈はLLM多解釈生成と直接接続する。"),
    ("アッタール『神秘哲学の書（アスラール・ナーメ）』", "PHIL", "shared_concept", "Sufi metaphysics",
     "スーフィー存在論・霊魂論として哲学DBと共有される。"),
    ("ルーミー『マスナヴィー第一巻』", "PHIL", "shared_concept", "Sufi separation/return philosophy",
     "葦笛の別離哲学は哲学DB存在論と共有される。"),
    ("ルーミー『ディーワーン・シャムス』", "PT", "shared_concept", "ecstatic mystical lyric",
     "陶酔抒情詩学は世界詩学の主要形式として詩学DBと共有。"),
    ("ジュヴァイニー『世界征服者の歴史』詳論", "AN", "shared_concept", "Mongol cross-cultural ethnography",
     "モンゴル征服史叙述は人類学的他者証言として共有される。"),
    ("ラシードゥッディーン『集史』詳論", "AN", "shared_concept", "world history / ethnography",
     "世界初の世界史は人類学的多文化総合の祖型として共有。"),
    ("カリーラとディムナ（ペルシア版）", "PT", "shared_concept", "trans-Eurasian fable",
     "汎ユーラシア寓話伝承は世界詩学の主要形式として共有。"),
    ("ヴァーエズ・カーシェフィー『アンワーリ・スハイリー』", "PT", "shared_concept", "Mughal Persian fable",
     "ムガル朝寓話散文は世界詩学装飾散文研究として共有。"),
    ("サーイブ・タブリーズィー", "AI-Development", "parallel", "LLM concise metaphor generation",
     "意味の彫琢はLLMの新奇比喩生成と歴史的に並行する。"),
    ("ユヌス・エムレ", "PHIL", "shared_concept", "Sufi vernacular spirituality",
     "口語スーフィー神秘主義は哲学DBスーフィズム項目と共有。"),
    ("フズーリー『レイラとメジュヌーン』", "PT", "shared_concept", "transregional love narrative",
     "アラブ・ペルシア・トルコ恋愛伝承の翻訳は世界詩学と共有。"),
    ("ハーリデ・エディプ『シネクリ・バッカル』", "AN", "shared_concept", "gender / modernization anthropology",
     "女性主体・近代化対立は人類学ジェンダー研究と共有される。"),
    ("ヘダーヤト『盲目の梟』詳論", "AI-Development", "parallel", "LLM hallucination structure",
     "悪夢的不安定主体はAI幻覚（hallucination）構造の歴史的祖型。"),
    ("ラティフェ・テキン『愛しい無頼の死』", "AN", "shared_concept", "rural-urban migration narrative",
     "農村-都市移住物語は人類学移住研究の対象として共有。"),
    ("エフメデー・ハーニー『メムーとズィーン』", "AN", "shared_concept", "Kurdish ethno-literature",
     "クルド民族叙事は人類学的民族文学研究と共有される。"),
    ("シャー・アブドゥル・ラティーフ・ビッタイ『シャー・ジョー・リサーロ』", "AN", "shared_concept", "Sindhi Sufi folklore",
     "スィンド民俗ロマンスのスーフィー化は人類学民俗研究と共有。"),
    ("サチャル・サルマスト", "PT", "shared_concept", "multilingual mystic poetics",
     "七言語並行詩学は世界多言語詩学研究と共有される。"),
]


# =====================================================
# Main
# =====================================================
def main() -> None:
    with LitDB() as db:
        period_id_by_key: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(
                name_ja=nj, region="南西アジア",
                start_year=sy, end_year=ey,
                name_en=ne, description=desc,
            )
            period_id_by_key[nj] = pid

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

        print(f"\n=== Wave18 C22 Persian-Turkish ADD60 completed ===")
        print(f"  concepts inserted: {inserted} (skipped: {skipped})")
        print(f"  total concepts attempted: {len(CONCEPTS)}")
        print(f"  fourth-transform tags: {ft_count}")
        print(f"  cross-domain links: {cd_count}")
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 14"
        ).fetchone()
        print(f"  total concepts in subfield 14: {row['c']}")


if __name__ == "__main__":
    main()
