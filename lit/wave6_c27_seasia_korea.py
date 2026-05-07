"""
LIT-DB Phase 2 — C27 Wave6: Southeast Asian and Korean Literature
====================================================================
Inserts 40 representative concepts spanning 5 categories:
  A. 韓国古典・近代 (10)
  B. 韓国現代 (8)
  C. ベトナム文学 (8)
  D. フィリピン・インドネシア・タイ (8)
  E. その他東南アジア・比較 (6)

subfield_id=17, code='lit_se_asia_korea', region='グローバルサウス'

Sources: National Library of Korea (NLK), Literature Translation Institute
of Korea (LTI Korea), Nôm Foundation (Vietnamese Hán-Nôm), SEAlang Library
(Southeast Asian languages), Wikipedia canonical entries where primary
critical editions are not online.
"""
from __future__ import annotations

from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    # Korea
    ("統一新羅期", "Unified Silla", 668, 935,
     "新羅の朝鮮半島統一期。郷歌（ヒャンガ）が記録された朝鮮文学の初期。"),
    ("高麗期", "Goryeo Period", 918, 1392,
     "高麗王朝期。漢文学と固有歌謡が並行し、後の時調の基盤が形成された。"),
    ("朝鮮王朝期", "Joseon Dynasty", 1392, 1910,
     "ハングル創製（1443年訓民正音）以降、時調・歌辞・パンソリ・国文小説が発達した時代。"),
    ("韓国近代期", "Korean Modern", 1894, 1945,
     "甲午改革から日帝強占期にかけて、近代小説・自由詩・現代散文が確立した時代。"),
    ("韓国現代期", "Korean Contemporary", 1945, 2025,
     "解放後の南北分断、戦後文学から現代K-novelグローバル流通までを含む現代期。"),
    # Vietnam
    ("ベトナム古典期", "Vietnamese Classical", 938, 1858,
     "李朝・陳朝・後黎朝・阮朝の漢文・字喃（チュノム）文学が発達した時代。"),
    ("ベトナム近代期", "Vietnamese Modern", 1858, 1945,
     "フランス植民地化以降、クオック・グー（国語表記）による近代文学が形成された時代。"),
    ("ベトナム現代期", "Vietnamese Contemporary", 1945, 2025,
     "独立戦争・南北分断・統一・ドイモイ改革を経た現代ベトナム文学の展開期。"),
    # Indonesia / Philippines / Thailand
    ("東南アジア植民地・独立期", "SEA Colonial-Independence", 1850, 1965,
     "オランダ・スペイン・米国・フランス植民地下から独立に至る東南アジア近代文学の形成期。"),
    ("東南アジア現代期", "SEA Contemporary", 1965, 2025,
     "独立後ナショナル文学・抵抗文学・グローバル英訳期。"),
    # Other SEA
    ("東南アジア古典期", "SEA Classical", 800, 1850,
     "クメール・ビルマ・ラオ・マレー古典文学が宮廷・宗教的語りとして栄えた時代。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — 韓国古典・近代 (10)
# ===============================================================

add({
    "name_ja": "郷歌（ヒャンガ）",
    "name_en": "hyangga",
    "name_original": "향가",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "統一新羅期",
    "definition": "新羅・高麗初期に郷札（ヒャンチャル）と呼ばれる漢字音訓借用法で表記された朝鮮固有の歌謡。『三国遺事』に14首、『均如伝』に11首の計25首が現存し、朝鮮文学最古の韻文記念碑として朝鮮詩歌史の出発点となった。",
    "background": "新羅人が漢字を借用して固有語を音訓表記する独自的書記法を発達させた。",
    "development": "高麗末期以降衰退したが、20世紀の小倉進平・梁柱東による解読で再評価された。",
    "historical_context": "東アジア漢字文化圏における固有語表記の独立的伝統。",
    "primary_source_url": "https://www.nl.go.kr/",
    "primary_source_type": "National Library of Korea reference",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "時調（シジョ）",
    "name_en": "sijo",
    "name_original": "시조",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "朝鮮王朝期",
    "definition": "高麗末期に成立し朝鮮王朝期に隆盛した三章六句45字内外の朝鮮固有定型詩。初章・中章・終章という三段構成と終章冒頭の三字句転換が特徴で、士大夫の儒教的教養から妓生（キーセン）の恋情まで広範に扱った。朝鮮詩歌の中核形式。",
    "background": "高麗末期の士大夫層が固有語による短歌形式を求めて成立した。",
    "development": "尹善道、黄真伊、李退溪らの作を経て、現代詩調までその系譜が続く。",
    "historical_context": "和歌・絶句と並ぶ東アジア固有定型詩の三大形式の一つ。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "歌辞（ガサ）",
    "name_en": "gasa",
    "name_original": "가사",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "朝鮮王朝期",
    "definition": "朝鮮王朝期に発達した4音4歩格の長編韻文形式。鄭澈『関東別曲』『思美人曲』、許蘭雪軒『閨怨歌』等が代表作で、紀行・抒情・教訓・閨怨等多様な主題を扱った。時調が短詩を担うのに対し、歌辞は叙事的・教訓的長歌を担う相補的形式。",
    "background": "朝鮮王朝の士大夫層と女性作者層が長編語りを必要とする中で発達した。",
    "development": "後期には庶民歌辞・東学歌辞へと展開し、近代以降は失われた。",
    "historical_context": "ハングル創製後の女性文学の主要装置の一つ。",
    "primary_source_url": "https://www.nl.go.kr/",
    "primary_source_type": "National Library of Korea reference",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "パンソリ",
    "name_en": "pansori",
    "name_original": "판소리",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "朝鮮王朝期",
    "definition": "朝鮮王朝後期（17-19世紀）に庶民層から発達した一人語り音楽劇。ソリックン（唱者）が太鼓の打ち手（コス）を伴って数時間にわたり物語を語り歌う。『春香歌』『沈清歌』『興夫歌』『水宮歌』『赤壁歌』が五大マダンとして現存し、2003年ユネスコ無形文化遺産に登録された。",
    "background": "朝鮮王朝後期の庶民文化興隆の中、巫俗音楽と説唱伝統が融合して成立した。",
    "development": "申在孝（19世紀）の整理により五大マダンが定型化し、現代も継承されている。",
    "historical_context": "東アジア口承パフォーマンスの代表的事例。",
    "primary_source_url": "https://ich.unesco.org/en/RL/pansori-epic-chant-00070",
    "primary_source_type": "UNESCO ICH official entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "春香伝（春香歌）",
    "name_en": "Chunhyangga",
    "name_original": "춘향전",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "朝鮮王朝期",
    "definition": "朝鮮王朝後期に成立した代表的国文小説兼パンソリ。妓生の娘春香と両班の息子李夢龍の愛と階級を超えた婚姻、貪官への抵抗を描く。パンソリ五大マダンの一つとして音楽的にも文学的にも朝鮮古典文学の頂点を成し、現代まで映画・舞台・小説に翻案され続ける。",
    "background": "朝鮮王朝後期の身分制動揺と庶民文化興隆が物語を生んだ。",
    "development": "現代韓国でも繰り返し映画化・舞台化され、国民的物語として機能する。",
    "historical_context": "東アジア恋愛物語の独自的代表作。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "沈清伝（沈清歌）",
    "name_en": "Shimcheongga",
    "name_original": "심청전",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "朝鮮王朝期",
    "definition": "朝鮮王朝後期の国文小説兼パンソリ。盲目の父の眼を開かせるため海神への供犠として身を投げ、龍宮を経て王妃となり父を再会させる孝女沈清の物語。儒教的孝の理想と仏教的因縁・転生観が融合し、『春香伝』と並ぶ朝鮮国文物語の代表作となる。",
    "background": "儒教的孝の理想と巫俗・仏教的世界観の融合の中で物語が成立した。",
    "development": "パンソリ・小説・現代映画（『沈清』など）を通じて継承された。",
    "historical_context": "朝鮮国文物語の儒・仏・巫融合的世界観の代表的体現。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "李光洙『無情』",
    "name_en": "Yi Kwang-su's Mujeong (The Heartless)",
    "name_original": "무정",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国近代期",
    "definition": "李光洙（1892-1950）が1917年『毎日申報』に連載した朝鮮初の本格的近代長編小説。教師李亨植と妓生英采、富豪令嬢善馨の三角関係を通じて、近代的自我・自由恋愛・民族啓蒙を主題化した。朝鮮文学近代化の出発点と位置づけられる。",
    "background": "東京留学組による近代日本文学経由の西欧近代小説受容が背景となった。",
    "development": "李光洙は後に親日的立場をとり評価が両義的だが、近代朝鮮小説の起点としての地位は不変である。",
    "historical_context": "朝鮮文学の近代化の象徴的契機。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "金素月の詩",
    "name_en": "Kim So-wol's poetry",
    "name_original": "김소월",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国近代期",
    "definition": "金素月（1902-1934）は朝鮮固有の七五調・民謡的リズムを近代自由詩に取り込み、朝鮮的「恨（ハン）」の情感を抒情詩で結晶化した近代朝鮮抒情詩の代表者。代表作『つつじの花（진달래꽃、1925）』は別離の情景を朝鮮的美意識で描き、現代韓国でも国民的愛唱詩として機能する。",
    "background": "金億・主要文学雑誌『創造』『廃墟』を経由する近代朝鮮詩の伝統に立った。",
    "development": "近代朝鮮詩の民族的・民衆的可能性を示し、後の韓国抒情詩の規範を形成した。",
    "historical_context": "朝鮮的抒情の近代詩への結晶化。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "金東仁の近代主義小説",
    "name_en": "Kim Tong-in's modernist fiction",
    "name_original": "김동인",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国近代期",
    "definition": "金東仁（1900-1951）は雑誌『創造』（1919）創刊メンバーとして朝鮮近代短編小説の確立に寄与した作家。『鑑じゃがいも』『狂炎ソナタ』等で写実主義・耽美主義・自然主義を試み、李光洙の啓蒙主義に対して芸術至上主義を主張した。短編小説の文体的・技巧的近代化を主導した。",
    "background": "東京留学組として大正期日本文学から近代主義美学を吸収した。",
    "development": "後の韓国短編小説の文体的洗練の基盤を築いた。",
    "historical_context": "朝鮮文学の啓蒙主義から芸術主義への展開。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "崔南善『海から少年へ』",
    "name_en": "Choe Nam-son's 'From the Sea to the Boys'",
    "name_original": "해에게서 소년에게",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国近代期",
    "definition": "崔南善（1890-1957）が1908年『少年』創刊号に発表した朝鮮初の近代自由詩。海の擬人化を通じて青年世代に対する民族的覚醒を呼びかけた。定型詩から自由詩への移行を象徴する作品で、朝鮮近代詩の出発点として位置づけられる。",
    "background": "啓蒙運動と日本明治詩・西欧近代詩の影響下で成立した。",
    "development": "「新体詩」運動の起点となり、近代朝鮮詩の自由詩化を導いた。",
    "historical_context": "朝鮮詩の近代化転換点。",
    "primary_source_url": "https://www.nl.go.kr/",
    "primary_source_type": "National Library of Korea reference",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY B — 韓国現代 (8)
# ===============================================================

add({
    "name_ja": "韓国分断文学",
    "name_en": "Korean division literature",
    "name_original": "분단문학",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国現代期",
    "definition": "1945年解放と1950-53年朝鮮戦争に起因する朝鮮半島分断を主題とする韓国現代文学の中核領域。崔仁勲『広場』（1960）、黄晳暎『懐かしき庭』、林哲祐『太白山脈』等が代表作。離散家族・イデオロギー対立・脱北者経験を扱い、韓国現代文学の倫理的核を成す。",
    "background": "解放と戦争の歴史的トラウマが文学的表象として継続する韓国独自的主題系である。",
    "development": "21世紀には脱北者文学・南北対話文学にまで拡張している。",
    "historical_context": "朝鮮半島の冷戦的分断の文学的応答。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "朴景利『土地（トジ）』",
    "name_en": "Park Kyung-ni's Toji (The Land)",
    "name_original": "토지",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国現代期",
    "definition": "朴景利（1926-2008）が1969年から25年かけて執筆した全16巻5部の大河小説。慶尚南道河東の崔参判家三代を軸に、東学農民戦争から日帝強占期・解放までの朝鮮民衆の苦難と再生を描く。韓国現代文学最大規模の歴史叙事として国民的古典の地位にある。",
    "background": "朝鮮現代史を女性家長を中心に再構築する野心が物語を生んだ。",
    "development": "TV連続ドラマ・記念館建設等を通じて国民的記憶として機能する。",
    "historical_context": "韓国現代文学の歴史的・大河的代表作。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "黄晳暎の社会派小説",
    "name_en": "Hwang Sok-yong's social fiction",
    "name_original": "황석영",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国現代期",
    "definition": "黄晳暎（1943-）はベトナム戦争従軍経験、光州民主化運動、訪朝事件を背景に『客地』『張吉山』『懐かしき庭』『パリデギ』『日没』等を著した韓国社会派小説の代表者。労働者・難民・脱北者等の周縁的主体の経験を描き、東アジア現代史の文学的証言者として国際的評価を獲得した。",
    "background": "1980年代民主化運動と分断・離散経験が作家活動の背景となった。",
    "development": "『パリデギ』など東アジア神話を現代難民物語に翻案する手法で世界文学に連結した。",
    "historical_context": "東アジア現代史の文学的証言。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "韓江『菜食主義者』",
    "name_en": "Han Kang's The Vegetarian",
    "name_original": "채식주의자",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国現代期",
    "definition": "韓江（1970-）が2007年に発表した三部構成の長編小説。突如肉食を拒否する女性ヨンへとその家族の崩壊を、夫・義兄・姉の三視点から描く。デボラ・スミスによる英訳で2016年国際ブッカー賞、2024年韓国人初のノーベル文学賞受賞の決定的作品となった。",
    "background": "韓国父権制社会への身体的・存在論的拒否を女性身体を通じて表象する試みから生まれた。",
    "development": "国際ブッカー賞・ノーベル賞を経て韓国文学の世界文学進入の象徴となった。",
    "historical_context": "韓国文学のグローバル受容の決定的契機。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "現代韓国詩",
    "name_en": "contemporary Korean poetry",
    "name_original": "한국 현대시",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国現代期",
    "definition": "1945年解放後の韓国詩。徐廷柱の生命詩、金洙暎の参与詩、申庚林の民衆詩、高銀の禅的抒情、崔勝鎬・金惠順の現代女性詩等多様な系譜が展開する。1980年代民主化運動詩、2000年代「未来派」実験詩、現代の英訳詩人（金惠順等）が世界詩壇で評価されている。",
    "background": "解放と分断と民主化の歴史が詩的言語の倫理的緊張を持続させた。",
    "development": "金惠順の英訳がグリフィン詩賞を受賞する等、世界詩壇への進出が続く。",
    "historical_context": "東アジア現代詩の主要系譜の一つ。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "印章（インジャン）文学",
    "name_en": "in-jang literature (signature literature)",
    "name_original": "인장문학",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国現代期",
    "definition": "韓国現代文学において作家固有の文体的・主題的「印章（署名）」を特徴づける批評概念。李清俊、金承鈺、朴婉緒、申京淑等の作家論において、作品全体を貫く独自的痕跡（印章）の分析装置として用いられる。日本語「作家の極印」、仏語「signature」と類比される批評概念。",
    "background": "西欧作家性論と韓国独自の手工芸的「印章」概念の融合から発達した。",
    "development": "現代韓国文学批評の独自的分析装置として定着しつつある。",
    "historical_context": "韓国文学批評における作家性論の独自的展開。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "K-novelグローバル波",
    "name_en": "K-novel global wave",
    "name_original": "K-소설 글로벌 웨이브",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国現代期",
    "definition": "2010年代以降、K-pop・K-drama・K-cinemaに続いて韓国小説が世界市場で急速に受容される現象。申京淑『母をお願い』、韓江『菜食主義者』、チョン・セラン、チョ・ナムジュ『82年生まれ、キム・ジヨン』等の英訳・多言語訳が世界的ベストセラーとなり、2024年韓江ノーベル賞で頂点を迎えた。LTI Koreaによる組織的翻訳支援が基盤となる。",
    "background": "1996年設立のLTI Koreaによる翻訳支援政策と韓国大衆文化の世界的台頭が背景となった。",
    "development": "ノーベル賞・国際ブッカー賞・全米批評家協会賞等の主要文学賞獲得が続く。",
    "historical_context": "21世紀世界文学市場における韓国文学の主要勢力化。",
    "primary_source_url": "https://www.ltikorea.or.kr/",
    "primary_source_type": "LTI Korea reference",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "北朝鮮文学",
    "name_en": "North Korean literature",
    "name_original": "북조선문학",
    "original_script": "hangul",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "韓国現代期",
    "definition": "1945年以降の朝鮮民主主義人民共和国の文学。社会主義リアリズム・主体（チュチェ）思想に基づく党的文学の制度化を特徴とし、洪命憙『林巨正』を起点に、朝鮮戦争文学・首領形象創造文学・帰還文学等の独自的領域を形成した。脱北者文学（金英玲『朝鮮民主主義人民共和国の現実』等）が並行する。",
    "background": "ソ連社会主義リアリズム理論の朝鮮への移植と主体思想化が制度的基盤となった。",
    "development": "1990年代以降、脱北者文学・体制内文学の双方が国際的研究対象となった。",
    "historical_context": "朝鮮半島分断の文学的二重展開。",
    "primary_source_url": "https://www.nl.go.kr/",
    "primary_source_type": "National Library of Korea reference",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY C — ベトナム文学 (8)
# ===============================================================

add({
    "name_ja": "阮攸『金雲翹』",
    "name_en": "Nguyen Du's Tale of Kieu (Truyen Kieu)",
    "name_original": "Truyện Kiều",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "ベトナム古典期",
    "definition": "阮朝の阮攸（1766-1820）が中国明代の小説を翻案し、字喃（チュノム）で著した3,254行の韻文長編物語。父の救出のため自己を犠牲にする美女王翠翹の運命を描き、ベトナム文学の最高峰として国民的古典化されている。1965年世界平和評議会により世界文化記念人物に選定された。",
    "background": "中国明代の青心才人の小説をベトナム六八体（lục bát）の韻文に翻案した。",
    "development": "20世紀に入りクオック・グー（ローマ字表記）化され、ベトナム国民的アイデンティティの象徴となった。",
    "historical_context": "ベトナム字喃文学の頂点・国民文学の中核。",
    "primary_source_url": "http://nomfoundation.org/nom-project/tale-of-kieu",
    "primary_source_type": "Nom Foundation critical edition",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "字喃（チュノム）漢喃文学",
    "name_en": "Han-Nom literature (Vietnamese Sino-Vietnamese)",
    "name_original": "Hán Nôm",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "ベトナム古典期",
    "definition": "13世紀から19世紀のベトナムで発達した漢字派生の固有表記法字喃（チュノム）と漢文で書かれた古典文学群の総称。阮廌『国音詩集』、胡春香の俳諧詩、阮攸『金雲翹』、阮甸『征婦吟』等が代表作。20世紀ローマ字化により断絶したが、Nôm Foundationのデジタル化で再アクセス可能となっている。",
    "background": "中国漢字を借用した独自的書記法とベトナム民族意識の結合から発達した。",
    "development": "20世紀のローマ字化（クオック・グー）で日常的読みは失われたが、研究・継承は続く。",
    "historical_context": "東アジア漢字文化圏における独立的書記伝統の代表例。",
    "primary_source_url": "http://nomfoundation.org/",
    "primary_source_type": "Nom Foundation digital library",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "自力文団（Tự lực văn đoàn）",
    "name_en": "Tu Luc Van Doan (Self-Strength Literary Group)",
    "name_original": "Tự lực văn đoàn",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "ベトナム近代期",
    "definition": "1932年に作家グエン・トゥオン・タム（一林）が設立したベトナム近代文学の主要文学集団。雑誌『風化（Phong Hóa）』『今日（Ngày Nay）』を媒体に、儒教的旧家族制度批判・近代的恋愛・個人主義を主題とする小説（『二人の恋』『風と影』等）を発表し、ベトナム文学の近代化を主導した。",
    "background": "フランス植民地下の都市知識人層が西欧近代文学を吸収して形成された。",
    "development": "ベトナム近代小説の規範を確立し、後の社会主義リアリズム文学にも影響した。",
    "historical_context": "ベトナム文学近代化の中核運動。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Self-Reliant_Literary_Group",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ナム・カオの写実主義",
    "name_en": "Nam Cao's realism",
    "name_original": "Nam Cao",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "ベトナム近代期",
    "definition": "ナム・カオ（1915-1951）はベトナム近代写実主義の代表作家。短編『チ・フェオ』（1941）で農村の貧困・暴力・人間性疎外を冷徹に描き、長編『生い立ち（Sống mòn）』で植民地下知識人の精神的衰退を表現した。フランス植民地下ベトナム民衆の生を最も鋭く文学化した作家とされる。",
    "background": "フランス植民地統治下の極貧農村社会への文学的応答として作品が書かれた。",
    "development": "1951年抗仏戦線で戦死したが、後の社会主義リアリズム文学・現代ベトナム文学の規範となった。",
    "historical_context": "ベトナム植民地下民衆文学の頂点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Nam_Cao",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "バオ・ニン『戦争の悲しみ』",
    "name_en": "Bao Ninh's The Sorrow of War",
    "name_original": "Nỗi buồn chiến tranh",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "ベトナム現代期",
    "definition": "バオ・ニン（1952-）が1990年に発表した自伝的長編小説。北ベトナム軍兵士キエンの視点からベトナム戦争のトラウマと無意味性を非線形的時間構成で描き、勝利物語の公式的言説に対する内的崩壊の証言を提示した。1994年英訳でThe Independent外国小説賞、後にベトナム現代文学の世界的代表作となった。",
    "background": "ドイモイ改革下の表現自由化と従軍経験の文学化が出版を可能にした。",
    "development": "ベトナム戦争文学の世界的経典の一つに加わった。",
    "historical_context": "ベトナム戦争の被害者側からの最重要文学的応答。",
    "primary_source_url": "https://en.wikipedia.org/wiki/The_Sorrow_of_War",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "グエン・フイ・ティエップ短編",
    "name_en": "Nguyen Huy Thiep's short stories",
    "name_original": "Nguyễn Huy Thiệp",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "ベトナム現代期",
    "definition": "グエン・フイ・ティエップ（1950-2021）は1986年ドイモイ改革直後に短編『山林の塩』『退役した将軍』等で登場し、社会主義リアリズムの公式言説を脱構築した現代ベトナム文学の革命者。歴史的物語と現代社会のシニカルな並置を通じて公式記憶への反論を提起した。",
    "background": "ドイモイ改革下の文学的自由化が新表現を可能にした。",
    "development": "現代ベトナム短編小説の規範転換を主導し、英訳でも国際的評価を獲得した。",
    "historical_context": "ドイモイ期ベトナム文学の文学的革命。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Nguy%E1%BB%85n_Huy_Thi%E1%BB%87p",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ベトナム英訳文学",
    "name_en": "Vietnamese literature in English translation",
    "name_original": "Vietnamese literature in English",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "ベトナム現代期",
    "definition": "21世紀以降のベトナム作家の英訳・英語執筆作品の世界的台頭。ヴィエト・タン・ウェン『The Sympathizer』（2015、ピュリッツァー賞）、オーシャン・ヴオン『On Earth We're Briefly Gorgeous』、グエン・ファン・クェ・マイ等が代表的存在で、ベトナム戦争・難民・ディアスポラ経験を世界文学の主流に提示した。",
    "background": "ベトナム戦争難民の第二世代がアメリカ・カナダで作家化したことが基盤となった。",
    "development": "ピュリッツァー賞等主要文学賞での評価獲得が続く。",
    "historical_context": "ベトナム文学のディアスポラ的・グローバル的展開。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Vietnamese_American_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ドイモイ期文学",
    "name_en": "doi moi literature",
    "name_original": "văn học đổi mới",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "ベトナム現代期",
    "definition": "1986年ドイモイ（刷新）改革以降のベトナム文学。社会主義リアリズム公式言説からの離脱と表現自由化の中で、グエン・フイ・ティエップ、バオ・ニン、ズオン・トゥ・フォン等が戦争批判・社会批判・個人内面探求の作品を発表した。ベトナム文学の現代的多様化の出発点。",
    "background": "経済改革に伴う検閲緩和と知的自由化が背景となった。",
    "development": "現代ベトナム文学の主要作家層を生み、世界文学への接続を可能にした。",
    "historical_context": "ベトナム文学の脱社会主義的近代化。",
    "primary_source_url": "https://en.wikipedia.org/wiki/%C4%90%E1%BB%95i_M%E1%BB%9Bi",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY D — フィリピン・インドネシア・タイ (8)
# ===============================================================

add({
    "name_ja": "ホセ・リサール『ノリ・メ・タンヘレ』",
    "name_en": "Jose Rizal's Noli Me Tangere",
    "name_original": "Noli Me Tangere",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア植民地・独立期",
    "definition": "フィリピン国民英雄ホセ・リサール（1861-1896）が1887年にスペイン語で発表した長編小説。スペイン植民地下マニラ社会の植民地主義・教会権力・人種差別を批判し、フィリピン民族意識覚醒の文学的契機となった。1896年リサール処刑がフィリピン革命の直接的契機となり、以後フィリピン国民文学の起点として位置づけられる。",
    "background": "ベルリン・スペイン留学中のリサールがフィリピン社会改革の必要性を文学的に表象した。",
    "development": "続編『エル・フィリブステリスモ』（1891）と共に現代もフィリピン高校必修教材。",
    "historical_context": "東南アジア反植民地文学の象徴的起点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Noli_Me_T%C3%A1ngere_(novel)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "フィリピン・タガログ・ディアスポラ文学",
    "name_en": "Filipino diasporic Tagalog literature",
    "name_original": "Panitikang Filipino sa diaspora",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア現代期",
    "definition": "フィリピン国外労働移民（OFW）・移民第二世代によるタガログ語・英語・両語混合の文学。ジェシカ・ハジドク、ミゲル・シフコ等が代表的存在で、移民労働・家族離散・ハイブリッド・アイデンティティを主題化する。フィリピン現代文学の世界文学的展開の中核を成す。",
    "background": "フィリピン国外労働移民1,000万人規模が文学的主体を生んだ。",
    "development": "英訳・タガログ語混合表現等、独自的多言語的詩学を発達させている。",
    "historical_context": "東南アジア・ディアスポラ文学の代表的事例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Philippine_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "サストラ・アンカタン45（45年世代文学）",
    "name_en": "Sastra Angkatan 45 (Generation '45)",
    "name_original": "Sastra Angkatan 45",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア植民地・独立期",
    "definition": "1945年インドネシア独立宣言前後の世代によるインドネシア独立文学運動。チャイリル・アンワル（1922-1949）の自由詩、イドルス、アスルル・サニ等の散文が代表的で、独立への戦闘的呼びかけと近代的個人意識の確立を主題化した。インドネシア近代文学の出発点。",
    "background": "日本軍政・蘭領東インド独立闘争の世代的経験が文学的爆発を生んだ。",
    "development": "プラムディヤ等の次世代作家へ独立後文学を継承した。",
    "historical_context": "インドネシア国民文学の創成的契機。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Angkatan_45",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "プラムディヤ『ブル四部作』",
    "name_en": "Pramoedya Ananta Toer's Buru Quartet",
    "name_original": "Tetralogi Buru",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア現代期",
    "definition": "プラムディヤ・アナンタ・トゥール（1925-2006）がスハルト政権下ブル島流刑中に口承で構想し1980-88年に出版した『人間の大地』『すべての民族の子』『足跡』『ガラスの家』からなる四部作長編小説。20世紀初頭オランダ植民地下のジャワ知識人ミンケのジャーナリスト・闘士としての成長を通じて、インドネシア民族意識の形成を描いた。インドネシア・東南アジア文学の世界的代表作。",
    "background": "12年に及ぶブル島政治流刑経験下、紙ペンを奪われた状況下で口承で構想された。",
    "development": "ノーベル文学賞候補となり、東南アジアの世界文学的代表作の地位を獲得した。",
    "historical_context": "東南アジア反植民地・反独裁文学の頂点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Buru_Quartet",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "プジャンガ・バル",
    "name_en": "Pujangga Baru (New Writers)",
    "name_original": "Pujangga Baru",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア植民地・独立期",
    "definition": "1933年に詩人ストモ・ジャウハル・アリーフィン、サヌシー・パネ、アルミン・パネが創刊した文芸雑誌『プジャンガ・バル（新文学者）』を中心に展開した蘭領東インド時代のインドネシア近代文学運動。マレー語近代化と西欧近代受容によりインドネシア国民言語の文学的基盤を築いた。",
    "background": "蘭領東インド統治下の近代教育を受けたマレー語知識人層が運動を担った。",
    "development": "1945年世代文学運動への直接的先駆をなした。",
    "historical_context": "インドネシア国民言語文学の制度的形成。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Pujangga_Baru",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "スントーン・プー",
    "name_en": "Sunthorn Phu",
    "name_original": "สุนทรภู่",
    "original_script": "thai",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア古典期",
    "definition": "スントーン・プー（1786-1855）はラッタナーコーシン王朝期タイ最大の詩人で、ラーマ2世期の宮廷詩人として活動した。代表作『プラ・アパイ・マニー』（25,000行以上の長編幻想叙事詩）と多数の旅行詩（ニラート）が知られ、タイ語六八体（クローン）の規範を確立した。1986年ユネスコ世界文化記念人物に選定された。",
    "background": "ラーマ2世王の文学愛好と宮廷詩人制度がスントーン・プーの活動を可能にした。",
    "development": "現代タイの詩教育の中核教材となり、6月26日「スントーン・プーの日」として記念される。",
    "historical_context": "タイ古典文学の頂点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Sunthorn_Phu",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ククリット・プラーモート",
    "name_en": "Kukrit Pramoj",
    "name_original": "คึกฤทธิ์ ปราโมช",
    "original_script": "thai",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア現代期",
    "definition": "ククリット・プラーモート（1911-1995）はタイ近代の作家・政治家・首相（1975-76）。長編小説『四つの治世（Si Phaen Din）』『多くの人生（Lai Chiwit）』等で1932年立憲革命以降のタイ社会変動を描き、現代タイ散文文学の規範を確立した。タイ国民文学の代表作家として国民芸術家に認定された。",
    "background": "タイ王族出身の知的・政治的指導者として近代タイ社会変動を多角的に経験した。",
    "development": "現代タイ歴史小説の規範を確立し、タイ・ナショナル・アイデンティティの文学的基盤となった。",
    "historical_context": "タイ近代国民文学の中心人物。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Kukrit_Pramoj",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "現代タイ小説",
    "name_en": "contemporary Thai novel",
    "name_original": "นวนิยายไทยร่วมสมัย",
    "original_script": "thai",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア現代期",
    "definition": "20世紀後半以降のタイ語小説。シーブーラパー（クラープ・サパサーディー）の社会派、チャート・コープチッティーの『判決（Kham Phiphaksa）』、ピラ・スドゥムらの現代政治小説、プラブダ・ユン等の都市実験文学が代表的展開を成す。検閲・社会批判・グローバル化の交差を映す。",
    "background": "1932年立憲革命以降のタイ社会変動と冷戦・現代政治の文学的応答。",
    "development": "21世紀には英訳・国際文学賞での評価獲得が続いている。",
    "historical_context": "東南アジア大陸部現代文学の代表的展開の一つ。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Thai_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})


# ===============================================================
# CATEGORY E — その他東南アジアと比較 (6)
# ===============================================================

add({
    "name_ja": "ビルマ古典・近代文学",
    "name_en": "Burmese literature classical and modern",
    "name_original": "မြန်မာစာပေ",
    "original_script": "burmese",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア古典期",
    "definition": "11世紀パガン王朝以降のビルマ文学。古典期の宮廷詩・仏教注釈・年代記（ヤサウィン）から、コンバウン王朝期のリッタ・ペズィンや王女ヒンニュンタウの詩、植民地下のテッパン・マウン・ワらの近代散文、独立後のシュエ・ウー・ダウン・ニョー等の社会派文学までを含む。仏教伝統と植民地経験の交差が中核を成す。",
    "background": "上座部仏教の正典伝承と王朝記録文学の伝統が古典文学の基盤となった。",
    "development": "1948年独立後のミャンマー国民文学・現代亡命作家文学への系譜が続く。",
    "historical_context": "東南アジア大陸部仏教文化圏の独立的文学伝統。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Burmese_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "カンボジア『リアムケー』",
    "name_en": "Cambodian Reamker (Khmer Ramayana)",
    "name_original": "រាមកេរ្តិ៍",
    "original_script": "khmer",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア古典期",
    "definition": "クメール語によるラーマーヤナ翻案叙事詩で、カンボジア宮廷文学・宮廷舞踊・影絵芝居（スバエク・トム）の中核台本。インド古典叙事詩を上座部仏教世界観で再解釈し、カンボジア国民的物語として継承される。アンコール時代以降の浮き彫り装飾でも視覚的に表象されている。",
    "background": "インド・サンスクリット叙事詩のカンボジア仏教文化への翻案として成立した。",
    "development": "クメール・ルージュ期に多くの伝承者を失ったが、現代カンボジア文化復興の中核として再生中。",
    "historical_context": "東南アジア大陸部のラーマーヤナ翻案叙事詩の代表例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Reamker",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ラオ古典文学",
    "name_en": "Lao literature",
    "name_original": "ວັນນະຄະດີລາວ",
    "original_script": "lao",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア古典期",
    "definition": "ラーンサーン王国期以降のラオス文学。仏教ジャータカに基づく『シン・サイ』『パ・ラム・パ・ラム』等の長編叙事詩、本生譚物語、宮廷詩が中核を成す。フランス植民地下では発展が抑制されたが、独立後・近年は現代ラオ語小説（タオン・チャンタヴォン等）が展開している。",
    "background": "上座部仏教・タイ系言語文化の影響下で古典文学が発達した。",
    "development": "1975年人民民主共和国成立以降、社会主義文学として再編されつつある。",
    "historical_context": "東南アジア大陸部上座部仏教文化圏の小国文学。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Lao_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "シンガポール多言語文学",
    "name_en": "Singapore multilingual literature",
    "name_original": "Singapore literature",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア現代期",
    "definition": "英語・中国語・マレー語・タミル語の四公用語による多言語的文学を特徴とするシンガポール現代文学。エドウィン・タムブー、キリン・ナー、ジュロン王、英語詩人のアルフィアン・サアトらが代表的存在で、多民族・多言語都市国家のハイブリッド文学的アイデンティティを表象する。",
    "background": "1965年独立以降の多言語政策と多民族社会が文学的多元性の基盤となった。",
    "development": "シンガポール文学賞・SEA Write Award等を通じて制度的に支援されている。",
    "historical_context": "東南アジア多言語都市国家文学の代表例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Singapore_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "マレーシア華人文学（馬華文学）",
    "name_en": "Malaysian Chinese literature (Mahua)",
    "name_original": "馬華文學",
    "original_script": "kanji",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア現代期",
    "definition": "マレーシアにおける中国語使用者による文学。1920-30年代の南来作家から、1970-80年代の李永平、張貴興、黎紫書等の現代作家までを含む。台湾・中華圏文学市場と連動しつつ、東南アジアの熱帯的風土・多民族経験・中華アイデンティティを独自的に表現する。",
    "background": "華人移民コミュニティと中国語教育・出版が文学の言語的基盤を維持した。",
    "development": "21世紀には台湾・中国本土の文学賞での評価獲得が続いている。",
    "historical_context": "東南アジア中華圏文学の代表例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mahua_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "インドネシア・マジック・リアリズム",
    "name_en": "Indonesian magic realism",
    "name_original": "Realisme magis Indonesia",
    "original_script": "roman",
    "subfield_code": "lit_se_asia_korea",
    "region": "グローバルサウス",
    "period_key": "東南アジア現代期",
    "definition": "21世紀インドネシア文学に顕著な現実と神秘・神話・精霊世界の融合的記述。エカ・クルニアワン『美は傷なり（Cantik Itu Luka）』（2002）、レイラ・S・チュドリ『プラン・ジャワ』、デウィ・レスタリ等が代表的。インドネシア群島の口承・神話伝統と世界文学的マジック・リアリズムの独自的接続を示す。",
    "background": "インドネシア多島嶼神話・精霊信仰伝統とラテンアメリカ・マジック・リアリズム受容の融合から発達した。",
    "development": "エカ・クルニアワンの英訳が2016年マン・ブッカー国際賞候補となる等、国際的展開が続く。",
    "historical_context": "東南アジア・グローバル文学の独自的潮流。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Eka_Kurniawan",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ---------------------------------------------------------------
# Fourth-transform tagging
# ---------------------------------------------------------------
FOURTH_TRANSFORM_TAGS = {
    "パンソリ": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "唱者の声・身体・即興と観衆の合いの手によって毎回再生される口承パフォーマンス言語は、AI生成テクストの一回性・身体性欠如への原理的対比を提供する。",
         "ai_phenomenon": "AI生成テクストにおける口承的身体性の不在"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "固定テキストではなく毎回の語りで再構成される物語形式は、AI物語生成における可変性・反復性の理論的源泉を提供する。",
         "ai_phenomenon": "AI物語生成の可変性・即興性"},
    ],
    "K-novelグローバル波": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "翻訳・組織的支援・グローバル文化現象の連動による韓国文学の世界的受容は、AI翻訳時代の世界文学受容の制度的可能性を実証する。",
         "ai_phenomenon": "AI翻訳による非西洋文学のグローバル受容拡大"},
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "デボラ・スミス英訳『菜食主義者』の論争は翻訳者の創造的役割の再考を促し、AI翻訳時代の翻訳論の核心的問題を先取りする。",
         "ai_phenomenon": "AI翻訳における創造的介入の倫理"},
    ],
    "韓国分断文学": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "離散家族・脱北者の経験的真正性を文学的真理の核に据える分断文学は、AI生成証言の真正性論争と直接対応する。",
         "ai_phenomenon": "AI生成証言テクストの真正性問題"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "分断主体の文学的形象化はAI時代における歴史的主体性・代表性の問題と構造的に類比される。",
         "ai_phenomenon": "AI時代の歴史的主体性・代表性"},
    ],
    "阮攸『金雲翹』": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "中国小説の字喃詩への翻案、20世紀のクオック・グー化、現代英訳への多層的翻訳経路は、AI翻訳時代の文化間翻訳の歴史的モデルを提供する。",
         "ai_phenomenon": "AI翻訳における多層的文化間翻訳"},
    ],
    "プラムディヤ『ブル四部作』": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "植民地から独立への民族主体形成を一個人ミンケの成長物語で結晶化する手法は、AI時代の主体形成理論の文学的源泉となる。",
         "ai_phenomenon": "AI仲介下の主体形成過程の理論化"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "口承で構想され記録された四部作の生成過程は、テキストの物質的真正性の問題に新たな視点を提供する。",
         "ai_phenomenon": "AI生成テクストの物質的・経験的真正性"},
    ],
    "字喃（チュノム）漢喃文学": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "漢字派生の固有表記法と漢文を併用する多重的書記実践は、AI多言語生成における書記システム間翻訳の理論的源泉となる。",
         "ai_phenomenon": "AI多言語・多書記システム生成"},
    ],
    "ホセ・リサール『ノリ・メ・タンヘレ』": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "スペイン語で書かれた反植民地小説が母国フィリピン民族意識を覚醒させる現象は、宗主国言語による被植民者主体形成の文学的事例として、AI英語ヘゲモニー下の主体形成問題と並行する。",
         "ai_phenomenon": "AI英語ヘゲモニー下の非英語主体形成"},
    ],
    "韓江『菜食主義者』": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "国際ブッカー賞・ノーベル賞という制度的受容を通じて韓国文学の世界文学進入が確立される過程は、AI翻訳時代の世界文学制度的受容の事例となる。",
         "ai_phenomenon": "AI翻訳時代の世界文学制度的受容"},
    ],
    "ベトナム英訳文学": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "ベトナム第二世代作家の英語直接執筆は翻訳を経ないグローバル文学の形式を実証し、AI言語生成時代の言語選択戦略を予示する。",
         "ai_phenomenon": "AI生成時代の言語選択戦略"},
    ],
    "サストラ・アンカタン45（45年世代文学）": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "独立闘争世代の集団的主体性が文学的生産の母体となる現象は、AI時代の集団的・歴史的主体性の問題に文学的源泉を提供する。",
         "ai_phenomenon": "AI時代の集団的・世代的主体性"},
    ],
}


# ---------------------------------------------------------------
# Cross-domain links
# ---------------------------------------------------------------
CROSS_DOMAIN_LINKS = [
    ("パンソリ", "AN", "shared_concept", "oral performance / embodied transmission",
     "パンソリの口承パフォーマンスは人類学の口承文化・身体的伝承研究と直接共有される。"),
    ("プラムディヤ『ブル四部作』", "PHIL", "shared_concept", "anti-colonial subject / ethnophilosophy",
     "プラムディヤの民族意識形成論はインドネシア民族哲学・反植民地哲学と一体に発展した。"),
    ("ホセ・リサール『ノリ・メ・タンヘレ』", "PHIL", "shared_concept", "Filipino national consciousness / Rizalism",
     "リサールはフィリピン民族哲学・リサリスモ思想の文学的・哲学的源泉を成す。"),
    ("阮攸『金雲翹』", "PT", "shared_concept", "translation / adaptation theory",
     "中国小説の字喃詩翻案は翻訳・翻案理論研究の中核的事例として詩学DBと共有される。"),
    ("K-novelグローバル波", "AI-Development", "parallel", "translation / global circulation",
     "デボラ・スミス英訳論争はAI翻訳時代の翻訳論議に直接接続する事例である。"),
    ("ベトナム英訳文学", "AI-Development", "parallel", "diasporic English writing / language choice",
     "ベトナム系作家の英語直接執筆はAI時代の言語選択戦略と並行する。"),
    ("カンボジア『リアムケー』", "Myth-Narratives", "shared_concept", "Ramayana adaptation / national myth",
     "クメール版ラーマーヤナは神話・物語DBと完全共有される世界叙事詩翻案素材。"),
    ("沈清伝（沈清歌）", "Myth-Narratives", "shared_concept", "filial piety narrative / sacrifice myth",
     "孝女犠牲・龍宮再生の物語構造は神話・物語DBの東アジア物語素材として共有される。"),
    ("韓国分断文学", "AN", "shared_concept", "displacement / divided memory",
     "離散家族・脱北者経験は人類学的離散・記憶研究と直接接続する。"),
    ("郷歌（ヒャンガ）", "PT", "parallel", "indigenous script / vernacular poetics",
     "郷札による固有語表記は周縁的書記実践として詩学DBの周縁文学装置研究と並行する。"),
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
                name_ja=nj, region="グローバルサウス",
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

        print(f"\n=== C27 SE Asia + Korea completed ===")
        print(f"  concepts inserted: {inserted} (skipped: {skipped})")
        print(f"  fourth-transform tags: {ft_count}")
        print(f"  cross-domain links: {cd_count}")
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 17"
        ).fetchone()
        print(f"  total concepts in subfield 17: {row['c']}")


if __name__ == "__main__":
    main()
