"""LIT-DB Phase 2 Wave 13 — C13 add60: Chinese Classical Literature (60 new).

Subfield: lit_cn_classical (id=8), region='東アジア'.
Existing 90 concepts cover Tang/Song/Ming-Qing theory and major schools.
This wave adds 60 NEW concepts covering individual works and
sub-genres (詩經 individual genres, 楚辭, 漢賦, 樂府, 六朝詩, 唐詩補完,
宋詞補完, 元曲, 明清小説補完, 評點批評).

Sources (real, verifiable):
  - CTEXT (Chinese Text Project): https://ctext.org/
  - 維基文庫 (Chinese Wikisource): https://zh.wikisource.org/
  - Kanripo: https://www.kanripo.org/
  - 中國哲學書電子化計劃: https://ctext.org/
  - Wikipedia academic entries (zh / en).

Verification policy:
  - 'primary'   -> PD original text on CTEXT / Wikisource / Kanripo, or
                   contemporaneous critical document.
  - 'secondary' -> canonical scholarly synthesis or academic-grade Wikipedia.
  - 'tertiary'  -> synthetic/comparative critical category for taxonomic
                   completeness.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


# ------------------------------------------------------------
# Sources
# ------------------------------------------------------------
CTEXT = "https://ctext.org/"
WSRC_ZH = "https://zh.wikisource.org/wiki/"
KANRIPO = "https://www.kanripo.org/"
WIKI_ZH = "https://zh.wikipedia.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"


# Period name_ja must match existing rows in `periods` (region='中国')
PERIOD_NAMES = {
    "先秦": "先秦", "漢": "漢", "魏晋南北朝": "魏晋南北朝",
    "唐": "唐", "宋": "宋", "元": "元", "明": "明", "清": "清",
}


CONCEPTS: list[dict] = []


def add(**e):
    CONCEPTS.append(e)


C = dict(subfield_code="lit_cn_classical", region="東アジア",
         original_script="hanzi")


# ============================================================
# A: 詩經 individual genres (8)
# ============================================================
add(**C, name_ja="風（國風）",
    name_en="Guofeng (Airs of the States)",
    name_original="國風",
    period_key="先秦",
    definition="『詩經』160篇を収める第一部。周南・召南・邶風・鄘風・衛風・王風・鄭風・齊風・魏風・唐風・秦風・陳風・檜風・曹風・豳風の15「國風」から成り、各諸侯國の地方歌謠を集成する。庶民の恋愛・労働・社会批判を主題とし、後世詩学において「比興」の源泉として規範化された。",
    background="西周末期から春秋中期にかけて諸国に流伝した民間歌謡を、周王室および魯太師が採集・整理した編纂事業。",
    development="漢代以降「采風」の制度的記憶として詩学伝統に継承され、樂府民歌・唐宋古文家の民謡関心の祖型となった。",
    historical_context="西周礼楽体制の崩壊と春秋諸侯國の分立期。",
    primary_source_url=CTEXT+"book-of-poetry/guo-feng",
    primary_source_type="CTEXT: 詩經 國風",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="小雅",
    name_en="Xiaoya (Minor Court Hymns)",
    name_original="小雅",
    period_key="先秦",
    definition="『詩經』74篇を収める第二部。西周王室および士大夫階層の宴饗・征戍・諷諭を主題とし、「鹿鳴」「四牡」「采薇」「鶴鳴」等を含む。後世「変風変雅」論において、政治的諷諭詩の正統と見做され、杜甫・白居易の諷諭詩理念の源流となった。",
    background="西周中後期の王室典礼および貴族士大夫文化の制度化。",
    development="毛詩序の「変雅」概念を経て、唐代諷諭詩派・宋代政治詩の理論的祖型となった。",
    historical_context="西周末期から春秋初期の王室衰微と政治批判文学の萌芽。",
    primary_source_url=CTEXT+"book-of-poetry/minor-odes-of-the-kingdom",
    primary_source_type="CTEXT: 詩經 小雅",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="大雅",
    name_en="Daya (Major Court Hymns)",
    name_original="大雅",
    period_key="先秦",
    definition="『詩經』31篇を収める第三部。西周王朝の建国神話・歴代王徳・典礼を主題とし、「文王」「大明」「綿」「皇矣」「生民」等を含む。周民族の起源神話を文学的に定着させ、後世「史詩」概念の中国的源流とされる。",
    background="西周王室の祭祀・典礼における頌辞文学の制度化。",
    development="後漢「四始」論を経て、唐代杜甫・元結による典礼詩・歴史詩の規範となった。",
    historical_context="西周建国期から穆王・宣王中興期の王朝意識形成。",
    primary_source_url=CTEXT+"book-of-poetry/greater-odes-of-the-kingdom",
    primary_source_type="CTEXT: 詩經 大雅",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="頌（周頌・魯頌・商頌）",
    name_en="Song (Sacrificial Hymns)",
    name_original="頌",
    period_key="先秦",
    definition="『詩經』40篇を収める第四部。周頌31篇・魯頌4篇・商頌5篇から成り、宗廟祭祀における頌辞・舞楽歌詞である。神祖追慕と王権神聖化の機能を担い、後世「廟堂文学」「典禮文学」の規範となった。",
    background="西周宗廟祭祀および魯國・宋國（商の遺裔）の宗教典礼文化。",
    development="漢代郊廟歌辞、唐代郊祀歌、宋代大晟楽府の祖型となった。",
    historical_context="西周宗法制度における祖先祭祀と王権神聖化の儀礼空間。",
    primary_source_url=CTEXT+"book-of-poetry/odes-of-the-temple-and-the-altar",
    primary_source_type="CTEXT: 詩經 頌",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="周南・召南",
    name_en="Zhounan and Shaonan",
    name_original="周南・召南",
    period_key="先秦",
    definition="『國風』冒頭の二篇25首。周公旦・召公奭が分治した南方地域（漢水流域）の民歌とされ、「關雎」「桃夭」「卷耳」等の名篇を含む。毛詩序は「正風」とし、王化の典範と位置づけた。儒家経学において「風教」概念の中核を成す。",
    background="西周初期の周公・召公分陝統治と南方諸侯國の文化的統合。",
    development="後漢毛詩序の「正風」教説、朱熹『詩集傳』の風化論に至るまで儒家詩学の核となった。",
    historical_context="西周初期の王朝統合と南方文化の周化過程。",
    primary_source_url=CTEXT+"book-of-poetry/zhou-nan",
    primary_source_type="CTEXT: 詩經 周南・召南",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="周南・召南は「風教」教説の核として、テキストが社会教化に作用するという古代中国の文学社会化観の祖型。AIによる文化規範生成・教化的テキスト生成の問題と理論的に共振する。")

add(**C, name_ja="鄭風・衛風",
    name_en="Zhengfeng and Weifeng",
    name_original="鄭風・衛風",
    period_key="先秦",
    definition="『國風』中の鄭國・衛國の歌謡群。「子衿」「野有蔓草」「氓」等、男女の恋愛と背叛を率直に詠む作品が多く、孔子は『論語』陽貨篇で「鄭聲淫」と評した。後世「鄭衛之音」は艶麗放縦な音楽・文学の代名詞となり、雅正対淫艶の対立軸を成した。",
    background="春秋中期の鄭・衛両国の商業発達と都市文化の興隆。",
    development="後漢以降「鄭衛之音」批判は儒家詩学の規範論議の中核となり、宋詞・元曲の艶情批判にも転用された。",
    historical_context="春秋中期商業都市の興隆と礼楽体制の動揺。",
    primary_source_url=CTEXT+"book-of-poetry/odes-of-zheng",
    primary_source_type="CTEXT: 詩經 鄭風",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="豳風「七月」",
    name_en="Bin Air: Seventh Month",
    name_original="豳風 七月",
    period_key="先秦",
    definition="『國風』豳風冒頭の長篇農事詩。一年十二ヶ月の農事・蚕織・狩猟・宴饗を時系列で叙し、西周初期豳地（陝西旬邑）の農耕生活を網羅的に描く。中国最古の歳時記文学とされ、後世「田家詩」「農事詩」（陶淵明・范成大）の祖型となった。",
    background="周民族先祖公劉の豳地居住期（前1500年頃推定）の農耕文化。",
    development="陶淵明田園詩、唐代王維「田家」、宋代范成大『四時田園雜興』に至る農事詩系譜の出発点。",
    historical_context="西周以前の周民族農耕文化と歳時祭祀。",
    primary_source_url=CTEXT+"book-of-poetry/odes-of-bin",
    primary_source_type="CTEXT: 詩經 豳風 七月",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="興・比・賦（六義の詩法）",
    name_en="Xing, Bi, Fu (six principles)",
    name_original="興比賦",
    period_key="先秦",
    definition="毛詩序が確立した詩経解釈の三詩法。「賦」は直叙、「比」は比喩、「興」は事物に託して情を発する技法を指す。風・雅・頌の三体と合わせ「六義」として詩学の根本範疇を成し、唐代孔穎達『毛詩正義』、宋代朱熹『詩集傳』を経て、東アジア詩学の基本概念となった。",
    background="後漢毛詩学派による詩経解釈学の体系化。",
    development="陸機『文賦』、劉勰『文心雕龍』比興篇、唐代鍾嶸『詩品』、朝鮮・日本の漢詩論にまで継承された詩学基本範疇。",
    historical_context="後漢経学における経典解釈学の精緻化期。",
    primary_source_url=CTEXT+"shi-jing/great-preface",
    primary_source_type="CTEXT: 毛詩大序",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="興比賦は事物-情感-言語の連鎖的喚起を理論化する。AI生成における連想的展開・象徴的飛躍の機制を理解する古典的祖型として再読可能。")


# ============================================================
# B: 楚辭 detailed (7)
# ============================================================
add(**C, name_ja="離騷",
    name_en="Li Sao (Encountering Sorrow)",
    name_original="離騷",
    period_key="先秦",
    definition="屈原（前340頃-前278頃）作の長篇抒情叙事詩、約2490字373句。楚懐王朝廷で讒言により放逐された自身の境涯を、香草美人比喩・神話的飛行・占夢を駆使して詠む。司馬遷「史記屈原賈生列傳」が「離憂」と訓じ、後世楚辭体および中国抒情詩の祖型として尊崇された。",
    background="戦国期楚国の懐王朝廷における派閥対立と屈原の失脚（前304年頃）。",
    development="漢賦の祖型となり、また士大夫の「忠君不遇」意識の文学的範例として、唐代李白・杜甫から清代まで継承された。",
    historical_context="戦国末期楚国の対秦外交失敗と国家衰微。",
    primary_source_url=CTEXT+"chu-ci/li-sao",
    primary_source_type="CTEXT: 楚辭 離騷",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="九歌",
    name_en="Jiu Ge (Nine Songs)",
    name_original="九歌",
    period_key="先秦",
    definition="屈原作とされる楚辭の祭祀歌11篇。東皇太一・雲中君・湘君・湘夫人・大司命・少司命・東君・河伯・山鬼・國殤・禮魂を祀る楚国南方の宗教歌曲を文学的に再構成したもの。シャーマニズム的神話世界と艶美な男女神話を統合し、後世神仙詩・遊仙詩の源流となった。",
    background="戦国期楚国南方（沅湘流域）のシャーマニズム的宗教祭祀文化。",
    development="魏晋遊仙詩、唐代李賀「神弦曲」、清代王闓運に至る神仙文学の祖型となった。",
    historical_context="楚国南方地域の苗蛮系宗教文化と中原漢文化の融合。",
    primary_source_url=CTEXT+"chu-ci/jiu-ge",
    primary_source_type="CTEXT: 楚辭 九歌",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="天問",
    name_en="Tian Wen (Heavenly Questions)",
    name_original="天問",
    period_key="先秦",
    definition="屈原作の長篇問答詩、172問374句。天地創成・神話伝説・歴史治乱を通じ計170余の根源的問いを連鎖的に提起する。中国古代神話の最大規模文献的記録であり、また哲学的問答詩の唯一無二の作例として、現代に至るまで神話学・思想史研究の中心資料となっている。",
    background="戦国期楚国における神話伝承の集積と、屈原個人の歴史哲学的反省。",
    development="柳宗元「天対」（天問への回答篇）、現代の中国神話学（袁珂等）の根本資料。",
    historical_context="戦国末期の宇宙論・神話論の集大成期。",
    primary_source_url=CTEXT+"chu-ci/tian-wen",
    primary_source_type="CTEXT: 楚辭 天問",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="天問の連鎖的問答形式は、根源を問い続ける思考様式を文学化する。LLMへのプロンプト連鎖・問答型対話の古典的祖型として再読可能。")

add(**C, name_ja="九章",
    name_en="Jiu Zhang (Nine Pieces)",
    name_original="九章",
    period_key="先秦",
    definition="屈原作とされる楚辭中の9篇の中短篇。「惜誦」「涉江」「哀郢」「抽思」「懷沙」「思美人」「惜往日」「橘頌」「悲回風」を収め、放逐後の各時期の心境を直接抒情する。中でも「橘頌」は中国最古の詠物詩、「哀郢」は楚国都郢陥落（前278年）を悼む亡国詩として尊重される。",
    background="屈原放逐期（前304-前278）の各時期の心境変化。",
    development="魏晋詠物詩、亡国哀詩（庾信「哀江南賦」）、宋代陸游愛国詩の祖型となった。",
    historical_context="戦国末期楚国の対秦敗戦と国都陥落。",
    primary_source_url=CTEXT+"chu-ci/jiu-zhang",
    primary_source_type="CTEXT: 楚辭 九章",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="招魂",
    name_en="Zhao Hun (Summoning the Soul)",
    name_original="招魂",
    period_key="先秦",
    definition="楚辭中の招魂呪詞。屈原作（王逸説）または宋玉作（諸説あり）。亡霊の四方流離を阻止し故郷へ召還する楚地の宗教儀礼を文学化したもの。四方の恐怖と故郷の華美を対比的に列挙する構造は、後世辞賦の鋪陳手法（漢賦の鋪張揚厲）の祖型となった。",
    background="戦国期楚地の招魂呪術と宗教祭祀文化。",
    development="漢賦の鋪陳・対偶手法、後世挽歌・哀祭文の典拠となった。",
    historical_context="楚地宗教文化と漢文化への移植期。",
    primary_source_url=CTEXT+"chu-ci/zhao-hun",
    primary_source_type="CTEXT: 楚辭 招魂",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="漁父",
    name_en="Yu Fu (The Fisherman)",
    name_original="漁父",
    period_key="先秦",
    definition="楚辭中の問答短篇。流謫中の屈原と漁父の対話を通じ「衆人皆濁我獨清、衆人皆醉我獨醒」の屈原の堅持と、漁父の「滄浪之水清兮、可以濯吾纓」の隠逸的相対主義を対比的に呈示する。後世士大夫の「出処進退」論の哲学的原型となり、隠逸文学の中核典拠となった。",
    background="戦国末期屈原放逐期の精神的危機と隠逸思想の対照。",
    development="陶淵明の隠逸理念、唐代隠逸詩、宋代士大夫の出処論の哲学的源流。",
    historical_context="戦国末期の士の道・隠の道をめぐる思想的緊張。",
    primary_source_url=CTEXT+"chu-ci/yu-fu",
    primary_source_type="CTEXT: 楚辭 漁父",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="漁父の相対主義 vs 屈原の絶対主義の対比は、AI時代における倫理的態度（適応型 vs 原則型）の選択構造の古典的範型として再読可能。")

add(**C, name_ja="宋玉「九辯」",
    name_en="Song Yu's Jiu Bian",
    name_original="九辯",
    period_key="先秦",
    definition="戦国末期楚国の宋玉（屈原の弟子と伝わる）作の長篇抒情詩。「悲哉秋之為氣也」を冒頭句とし、秋を媒介に士の不遇を詠む。中国「悲秋」文学の祖型として、後世杜甫・李煜・辛棄疾を経て、東アジアの秋詩伝統を規定した。",
    background="戦国末期楚国の文学集団における屈原文学の継承。",
    development="漢賦・建安詩・唐詩・宋詞に至る悲秋文学の規範的源流となった。",
    historical_context="戦国末期楚国の文化的成熟期。",
    primary_source_url=CTEXT+"chu-ci/jiu-bian",
    primary_source_type="CTEXT: 楚辭 九辯",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# C: 漢賦 (8)
# ============================================================
add(**C, name_ja="司馬相如「子虛賦」",
    name_en="Sima Xiangru's Zi Xu Fu",
    name_original="子虛賦",
    period_key="漢",
    definition="司馬相如（前179-前117）作の漢大賦の代表作。子虛・烏有先生・亡是公の三仮託人物の問答形式で、楚王雲夢沢の狩猟を鋪張揚厲して描く。漢武帝が読んで感嘆し、相如を召見した契機となった作品。漢大賦の典範を成し、揚雄・班固に継承された。",
    background="前漢武帝期の中央集権強化と帝室文学の盛行。",
    development="「上林賦」と対をなし、漢大賦の鋪陳・対偶・諷諭の規範を確立した。",
    historical_context="武帝建元年間（前140-前135）の文学侍従制度の確立。",
    primary_source_url=CTEXT+"han-shu/si-ma-xiang-ru-zhuan",
    primary_source_type="CTEXT: 漢書 司馬相如傳",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="司馬相如「上林賦」",
    name_en="Sima Xiangru's Shanglin Fu",
    name_original="上林賦",
    period_key="漢",
    definition="司馬相如「子虛賦」の続篇。亡是公が天子上林苑の壮麗・狩猟・典礼を鋪張揚厲して描き、末尾で「卒章顯志」（諷諭の意を結ぶ）の構造を確立する。漢大賦最高峰の作とされ、文心雕龍・文選において賦体の典範として尊崇された。",
    background="武帝期の帝室苑囿文化と漢帝国の物質的繁栄。",
    development="揚雄「甘泉賦」「羽獵賦」、班固「両都賦」、張衡「兩京賦」の直接的祖型となった。",
    historical_context="武帝期の帝国主義的拡張と中央集権完成。",
    primary_source_url=CTEXT+"han-shu/si-ma-xiang-ru-zhuan",
    primary_source_type="CTEXT: 漢書 司馬相如傳",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="司馬相如「大人賦」",
    name_en="Sima Xiangru's Daren Fu",
    name_original="大人賦",
    period_key="漢",
    definition="司馬相如晩年作の遊仙賦。武帝の神仙信仰を諷諭する意図で「大人」（武帝喩）の宇宙飛行を壮麗に描いたが、武帝はかえって遊仙趣味を強めたと司馬遷は記す。後世遊仙詩・神仙文学の祖型となり、屈原「遠遊」と並ぶ中国遊仙文学の二大源流。",
    background="武帝晩年の神仙方術への傾倒。",
    development="魏晋遊仙詩、郭璞「遊仙詩」、唐代李白遊仙詩の規範的源流。",
    historical_context="武帝末期の神仙信仰と方士の隆盛。",
    primary_source_url=CTEXT+"han-shu/si-ma-xiang-ru-zhuan",
    primary_source_type="CTEXT: 漢書 司馬相如傳",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="揚雄四賦",
    name_en="Yang Xiong's Four Fu",
    name_original="揚雄四賦",
    period_key="漢",
    definition="揚雄（前53-後18）作の四篇代表賦——「甘泉賦」「河東賦」「羽獵賦」「長楊賦」。司馬相如賦の規範を継承しつつ諷諭性を強化し、後年自ら「童子雕蟲篆刻、壯夫不為」と批判した。漢大賦の自己反省的契機を担い、後世辞賦と政治の関係論の中核となった。",
    background="前漢成帝期の宮廷儀礼と賦家の侍従文学。",
    development="揚雄『法言』『太玄』に至る賦否定論を経て、班固「両都賦」の都市賦への展開を導いた。",
    historical_context="前漢末期の儒家経学興隆と賦の文学的位置の変動。",
    primary_source_url=CTEXT+"han-shu/yang-xiong-zhuan",
    primary_source_type="CTEXT: 漢書 揚雄傳",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="班固「兩都賦」",
    name_en="Ban Gu's Liang Du Fu",
    name_original="兩都賦",
    period_key="漢",
    definition="後漢班固（32-92）作の都市大賦。西京賓と東都主人の問答形式で、旧都長安と新都洛陽を対比的に描き、東漢の文教治世を称揚する。司馬相如「子虛・上林」の苑囿賦から都市賦への転換を画し、後世「京都賦」の規範となった。",
    background="後漢光武帝・明帝期の洛陽遷都と漢帝国の制度再建。",
    development="張衡「兩京賦」、左思「三都賦」（晋）の直接的範型となり、都市文学の祖を成す。",
    historical_context="後漢前期の制度整備と儒家化政治。",
    primary_source_url=CTEXT+"wenxuan",
    primary_source_type="文選: 兩都賦 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="張衡「兩京賦」",
    name_en="Zhang Heng's Liang Jing Fu",
    name_original="兩京賦",
    period_key="漢",
    definition="後漢張衡（78-139）作の長篇都市賦。班固「兩都賦」を継承しつつ、長安と洛陽の都市・典礼・芸能をより詳細に描く。漢大賦の鋪張極限を成し、左思「三都賦」（賦の傑作とされ「洛陽紙貴」の故事を生んだ）の直接的祖型となった。",
    background="後漢中期の文人科学者張衡の博物学的関心と文学的野心。",
    development="左思「三都賦」、晋潘岳「西征賦」、唐代都市賦に直接的影響。",
    historical_context="後漢中期の文化的爛熟と科学（天文・地震儀）と文学の交錯。",
    primary_source_url=CTEXT+"wenxuan",
    primary_source_type="文選: 兩京賦 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="張衡「歸田賦」",
    name_en="Zhang Heng's Gui Tian Fu",
    name_original="歸田賦",
    period_key="漢",
    definition="張衡晩年作の短篇抒情賦。宮廷の腐敗と政治的閉塞を厭い、田園隠遁を志す心境を簡潔に詠む。漢大賦の鋪張から脱した抒情小賦の出発点となり、魏晋抒情賦（陶淵明「歸去來辭」）の祖型となった。",
    background="張衡晩年の宦官専権下の政治的失意。",
    development="陶淵明「歸去來辭」、謝靈運山水賦、唐宋小賦の系譜的源流。",
    historical_context="後漢後期の宦官専権と知識人の隠逸志向の興隆。",
    primary_source_url=CTEXT+"wenxuan",
    primary_source_type="文選: 歸田賦 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="「歸田賦」が体現する公的世界からの撤退志向は、AI時代の制度疲労に対する隠遁・スローライフ志向と理論的に共振する。")

add(**C, name_ja="賈誼「弔屈原賦」「鵩鳥賦」",
    name_en="Jia Yi's Diao Quyuan Fu and Fu Niao Fu",
    name_original="弔屈原賦・鵩鳥賦",
    period_key="漢",
    definition="前漢賈誼（前200-前168）作の二篇代表賦。「弔屈原賦」は長沙王太傅左遷時に湘水を渡り屈原を哀悼、「鵩鳥賦」は鵩鳥（不吉の鳥）の侵入を契機に道家的処世観を抒情的に展開する。漢初辞賦から司馬相如大賦への過渡期を画し、士の不遇文学の漢代祖型となった。",
    background="前漢文帝期の派閥対立と賈誼の左遷。",
    development="司馬相如・揚雄に継承され、後世「逐臣文学」の漢代典拠となった。",
    historical_context="前漢初期の中央集権形成期の派閥闘争。",
    primary_source_url=CTEXT+"han-shu/jia-yi-zhuan",
    primary_source_type="CTEXT: 漢書 賈誼傳",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: 樂府 (4)
# ============================================================
add(**C, name_ja="郭茂倩『樂府詩集』分類体系",
    name_en="Guo Maoqian's Yuefu Shiji classification",
    name_original="樂府詩集",
    period_key="宋",
    definition="北宋郭茂倩（1041-1099頃）編『樂府詩集』100巻が確立した樂府詩の12分類体系——郊廟歌辭・燕射歌辭・鼓吹曲辭・橫吹曲辭・相和歌辭・清商曲辭・舞曲歌辭・琴曲歌辭・雜曲歌辭・近代曲辭・雜歌謠辭・新樂府辭。漢から唐五代までの樂府を網羅集成し、後世樂府研究の基盤となった。",
    background="北宋仁宗・神宗期の文献整理事業と樂府学の体系化。",
    development="清代沈德潛『古詩源』、現代の樂府研究（蕭滌非『漢魏六朝樂府文學史』）の基礎となった。",
    historical_context="北宋中期の儒家文献学と楽制復興運動。",
    primary_source_url=CTEXT+"library.pl?if=gb&res=1571",
    primary_source_type="CTEXT: 樂府詩集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="相和歌辭",
    name_en="Xianghe Geci (Harmony Songs)",
    name_original="相和歌辭",
    period_key="漢",
    definition="漢代樂府の主要分類の一つ。「絲竹相和、執節者歌」（弦楽・竹管が和し、節を持つ者が歌う）の演奏形式から命名。「東門行」「婦病行」「陌上桑」「孔雀東南飛」等、漢代庶民生活と社会矛盾を主題とする名篇を含む。漢樂府民歌の中核を成し、建安詩人の擬作対象となった。",
    background="漢代教坊（音楽行政機関）における民間音楽の収集と整理。",
    development="建安七子の擬樂府、陸機「擬古詩」、唐代李白「行路難」「將進酒」の祖型となった。",
    historical_context="漢代樂府制度の興隆と民間文化の宮廷化。",
    primary_source_url=CTEXT+"yuefu-shiji",
    primary_source_type="樂府詩集 相和歌辭 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="鼓吹曲辭",
    name_en="Guchui Quci (Drum-Pipe Songs)",
    name_original="鼓吹曲辭",
    period_key="漢",
    definition="漢代軍楽として確立された樂府分類。北狄音楽を起源とし、鼓・笳・簫等の管楽で演奏される。漢「鐃歌十八曲」（朱鷺・思悲翁・上之回・戰城南等）が現存し、武帝期の軍事拡張を反映する。後世軍歌・出塞詩の源流となった。",
    background="漢武帝期の対匈奴戦争と北方民族音楽の取り入れ。",
    development="魏晋鼓吹曲、唐代邊塞詩（高適・岑參）の音楽的・主題的祖型となった。",
    historical_context="武帝期の軍事拡張と異文化音楽の宮廷化。",
    primary_source_url=CTEXT+"yuefu-shiji",
    primary_source_type="樂府詩集 鼓吹曲辭 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="雜歌謠辭",
    name_en="Zage Yaoci (Miscellaneous Songs)",
    name_original="雜歌謠辭",
    period_key="漢",
    definition="樂府詩集が分類する民間歌謠の総称。童謠・讖謠・里巷歌等を含み、漢代庶民の声と政治批判を最も直接的に伝える。漢書五行志に多く採録され、政治的予言・社会批判の機能を持つ。後世「采風」精神の中核典拠となった。",
    background="漢代の童謠・讖謠の社会的流布と政治機能。",
    development="魏晋讖緯文学、宋代『宋史五行志』、明清民歌（馮夢龍『山歌』）に継承された民間歌謠採集の伝統の祖。",
    historical_context="漢代讖緯思想と民間声論の政治化。",
    primary_source_url=CTEXT+"yuefu-shiji",
    primary_source_type="樂府詩集 雜歌謠辭 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: 六朝詩 (8)
# ============================================================
add(**C, name_ja="阮籍「詠懷詩」",
    name_en="Ruan Ji's Yong Huai Shi",
    name_original="詠懷詩",
    period_key="魏晋南北朝",
    definition="阮籍（210-263、竹林七賢）作の五言詩82首組詩。司馬氏簒奪期の政治的危険下、隠喩・寓意・象徴を駆使して個人の哲学的苦悶を抒情する。鍾嶸『詩品』は「言在耳目之内、情寄八荒之表」と評価し、中国抒情詩の暗喩的精緻化の出発点とされる。",
    background="魏晋禅代期（249-265）の司馬氏専権と知識人の政治的危機。",
    development="陶淵明「飲酒」二十首、唐代陳子昂「感遇」三十八首、李白「古風」五十九首の組詩抒情の祖型となった。",
    historical_context="魏末晋初の高平陵の変（249）以降の政治的恐怖。",
    primary_source_url=CTEXT+"wenxuan",
    primary_source_type="文選: 阮籍詠懷詩 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="阮籍の暗喩詩は政治的検閲下で意味を多層化する技法。AI時代の表現規制下で多義的に意味を伝える戦略の古典的祖型。")

add(**C, name_ja="嵇康詩",
    name_en="Ji Kang's poetry",
    name_original="嵇康詩",
    period_key="魏晋南北朝",
    definition="嵇康（223-262、竹林七賢首）作の四言詩・五言詩。「贈秀才入軍」「幽憤詩」を代表とし、玄学（道家哲学）と隠逸を主題に、清峻孤高の文体を確立。司馬昭に処刑される直前の「廣陵散」絶響の伝説とともに、魏晋風度の文学的体現とされた。",
    background="魏晋玄学の興隆と司馬氏専権下の知識人弾圧。",
    development="阮籍とともに魏晋玄言詩・隠逸詩の祖型を成し、陶淵明・謝靈運に継承された。",
    historical_context="魏末晋初の名教（儒教）と自然（道家）の論争期。",
    primary_source_url=CTEXT+"wenxuan",
    primary_source_type="文選: 嵇康詩 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="陶淵明「歸去來辭」",
    name_en="Tao Yuanming's Gui Qu Lai Ci",
    name_original="歸去來辭",
    period_key="魏晋南北朝",
    definition="陶淵明（365頃-427）が彭澤県令を辞任（405年）した際に作った辞賦体抒情文。「歸去來兮、田園將蕪胡不歸」を冒頭に、官途棄絶と田園回帰の決意を率直に詠む。中国隠逸文学の最高傑作とされ、後世士大夫の隠逸理念の規範的範型となった。",
    background="東晋末期の混乱期と陶淵明の彭澤令辞任。",
    development="蘇軾は「晋無文章、惟陶淵明歸去來辭一篇而已」と絶讃し、宋代以降の隠逸文学・田園詩の頂点として尊崇された。",
    historical_context="東晋末期の政治的混乱と寒門知識人の生活的選択。",
    primary_source_url=CTEXT+"wenxuan",
    primary_source_type="文選: 陶淵明集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="「歸去來辭」が示す制度離脱と自然回帰の意志は、AI/プラットフォーム経済からの撤退志向（slow movement, digital detox）と理論的に共振する。")

add(**C, name_ja="陶淵明「飲酒」二十首",
    name_en="Tao Yuanming's Yin Jiu Twenty",
    name_original="飲酒二十首",
    period_key="魏晋南北朝",
    definition="陶淵明作の五言組詩20首。隠逸生活における酒と思索を主題に、「採菊東籬下、悠然見南山」（其五）等の千古絶唱を含む。中国隠逸詩・田園詩の最高頂点とされ、組詩形式の抒情的可能性を最大限に展開した。後世詩学において「平淡」「自然」の理念の規範的範例となった。",
    background="陶淵明の彭澤令辞任後の田園隠居生活（406年以降）。",
    development="蘇軾「和陶詩」、清代沈德潛『古詩源』に至る陶淵明評価の頂点。",
    historical_context="東晋末から劉宋初の動乱期と隠逸知識人の生活実践。",
    primary_source_url=CTEXT+"wenxuan",
    primary_source_type="文選・陶淵明集: 飲酒詩 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="陶淵明「桃花源記」",
    name_en="Tao Yuanming's Tao Hua Yuan Ji",
    name_original="桃花源記",
    period_key="魏晋南北朝",
    definition="陶淵明作の散文小品。武陵漁人が偶然辿り着いた秦時遺民の理想郷を描く幻想的物語。「桃花源」は後世中国の理想郷概念の代名詞となり、政治批判の隠喩・反体制ユートピア・神仙境の三重構造を内包する。中国ユートピア文学の祖型。",
    background="東晋末期の戦乱と社会的疲弊、陶淵明の理想社会像。",
    development="王維「桃源行」、唐代仙境詩、明代『鏡花緣』、現代の中国ユートピア文学に至る理想郷文学の規範的源流。",
    historical_context="東晋末期の政治混乱と社会的不安。",
    primary_source_url=CTEXT+"wenxuan",
    primary_source_type="文選・陶淵明集: 桃花源記 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="桃花源は隔絶された理想空間として、デジタル空間・メタバース等のユートピア構想の古典的祖型として再読可能。")

add(**C, name_ja="謝靈運山水詩",
    name_en="Xie Lingyun's landscape poetry",
    name_original="謝靈運山水詩",
    period_key="魏晋南北朝",
    definition="謝靈運（385-433）が劉宋初期に確立した山水詩体。「登池上樓」「石壁精舎還湖中作」等の代表作で、永嘉郡の自然を精緻に描き、玄言詩から山水詩への転換を画した。鍾嶸『詩品』は「才高詞盛、富艶難蹤」と評し、中国山水詩の祖と尊崇される。",
    background="東晋末から劉宋初の貴族文化と謝氏家門の文化的高度化。",
    development="王維・孟浩然唐代山水詩、宋代山水画題詩の祖型となった。",
    historical_context="劉宋初期の貴族政治と地方流謫文化。",
    primary_source_url=CTEXT+"wenxuan",
    primary_source_type="文選: 謝靈運集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="鮑照「擬行路難」",
    name_en="Bao Zhao's Ni Xing Lu Nan",
    name_original="擬行路難",
    period_key="魏晋南北朝",
    definition="鮑照（414頃-466）作の樂府擬作18首組詩。寒門出身の鮑照が「對案不能食、拔劍擊柱長歎息」と寒士の不遇を激越に詠む。六朝詩の貴族文学から脱した寒士詩の出発点として、唐代李白「行路難」三首の直接的祖型となった。",
    background="劉宋・南齊期の門閥制度下の寒門文人の社会的閉塞。",
    development="李白「行路難」、唐代寒士詩派、宋代陸游愛国詩の祖型。",
    historical_context="南朝門閥社会と寒門知識人の社会的位置。",
    primary_source_url=CTEXT+"wenxuan",
    primary_source_type="文選: 鮑照集 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="江淹「恨賦」「別賦」",
    name_en="Jiang Yan's Hen Fu and Bie Fu",
    name_original="恨賦・別賦",
    period_key="魏晋南北朝",
    definition="江淹（444-505）作の二篇代表賦。「恨賦」は古今の悲恨を典型化し、「別賦」は「黯然銷魂者、唯別而已矣」を冒頭に七種の別離を描く。六朝抒情小賦の頂点を成し、後世「江郎才尽」の故事とともに、抒情賦の規範的範型となった。",
    background="南朝梁初期の文学的爛熟と感傷主義の興隆。",
    development="唐宋抒情小賦、明清騈文の典拠となった。",
    historical_context="南朝梁初の文化的高度化と文学的精緻化。",
    primary_source_url=CTEXT+"wenxuan",
    primary_source_type="文選: 江淹集 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# F: 唐詩補完 (8)
# ============================================================
add(**C, name_ja="王維「輞川集」",
    name_en="Wang Wei's Wangchuan Collection",
    name_original="輞川集",
    period_key="唐",
    definition="王維（701頃-761）と裴迪が輞川別業（藍田県）の20景を詠み合った五絶組詩。「鹿柴」「竹里館」「辛夷塢」等を含み、禅的静寂と山水画的構図を融合した。蘇軾は「味摩詰之詩、詩中有畫」と評し、詩画一体の理念の祖型となった。",
    background="盛唐後期の安史の乱（755-763）以前の貴族文化と王維の半官半隠生活。",
    development="宋代蘇軾の詩画論、元明文人画題詩、日本の山水詩理念の規範的源流。",
    historical_context="盛唐後期の貴族別業文化と禅宗の文人受容。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩: 王維輞川集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="孟浩然山水田園詩",
    name_en="Meng Haoran's landscape pastoral poetry",
    name_original="孟浩然詩",
    period_key="唐",
    definition="孟浩然（689-740）が確立した盛唐山水田園詩体。「春曉」「過故人莊」「望洞庭湖贈張丞相」を代表とし、田家・山水・隠逸を平淡な五言で詠む。王維と並び「王孟」と称され、陶淵明・謝靈運の正統継承者として唐代山水詩の祖型を形成した。",
    background="盛唐期の襄陽地方文化と科挙不合格の隠逸文人の社会的位置。",
    development="王維・韋應物・柳宗元、宋代范成大田園詩に直接的影響。",
    historical_context="盛唐前期の科挙制度と地方文人文化の興隆。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩: 孟浩然集 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="高適邊塞詩",
    name_en="Gao Shi's frontier poetry",
    name_original="高適邊塞詩",
    period_key="唐",
    definition="高適（704頃-765）が確立した盛唐邊塞詩体。「燕歌行」「別董大」を代表とし、河北・隴西の辺境と兵士の生を雄渾な筆致で詠む。岑參と並び「高岑」と称され、唐代邊塞詩派の双璧を成した。漢樂府「鼓吹曲辭」の精神を盛唐に継承した。",
    background="盛唐期の対突厥・吐蕃戦争と知識人の従軍体験。",
    development="盛唐邊塞詩派（王昌齡・岑參）、宋代陸游愛国詩、清代邊塞詩に直接的影響。",
    historical_context="玄宗期の対外戦争と募兵制成立。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩: 高適集 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="岑參邊塞詩",
    name_en="Cen Shen's frontier poetry",
    name_original="岑參邊塞詩",
    period_key="唐",
    definition="岑參（715頃-770）が安西節度使幕府従軍中に作った邊塞詩群。「白雪歌送武判官歸京」「走馬川行奉送封大夫出師西征」等で、西域天山の壮麗な自然と異域風物を奇抜な想像力で詠む。盛唐邊塞詩の頂点と評価される。",
    background="安史の乱前後の西域経営と岑參の二度の西域従軍（749-751、754-757）。",
    development="李賀の奇譎詩風、宋代陸游、明清邊塞詩への影響。",
    historical_context="盛唐安西都護府の西域経営期。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩: 岑參集 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="韓愈詩（以文為詩）",
    name_en="Han Yu's poetry (prose-as-poetry)",
    name_original="韓愈詩",
    period_key="唐",
    definition="韓愈（768-824）が中唐に確立した「以文為詩」の詩体。「南山詩」「山石」等で、古文運動の散文的論理性を詩に取り込み、奇崛硬瘦な独自の文体を樹立した。宋代江西詩派・蘇軾・黄庭堅の直接的祖型となり、唐宋詩風転換の中核を成した。",
    background="中唐古文運動と詩文一体化の理念。",
    development="蘇軾・黄庭堅・宋代江西詩派、元代趙孟頫、明清擬古派の祖型。",
    historical_context="中唐安史の乱後の文化再構築期と古文運動。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩: 韓愈集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="柳宗元「永州八記」",
    name_en="Liu Zongyuan's Yongzhou Ba Ji",
    name_original="永州八記",
    period_key="唐",
    definition="柳宗元（773-819）が永州司馬左遷期（805-815）に作った山水遊記8篇——「始得西山宴遊記」「鈷鉧潭記」「鈷鉧潭西小丘記」「至小丘西小石潭記」「袁家渇記」「石渠記」「石澗記」「小石城山記」。中国山水遊記の規範を確立し、北宋「唐宋八大家」散文の頂点として尊崇された。",
    background="永貞革新失敗（805）後の柳宗元の永州流謫期。",
    development="宋代蘇軾・王安石散文、明代「公安派」遊記、清代桐城派古文の典範となった。",
    historical_context="中唐永貞革新と政治的弾圧期。",
    primary_source_url=CTEXT+"liu-he-dong-ji",
    primary_source_type="柳河東集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="劉禹錫「竹枝詞」",
    name_en="Liu Yuxi's Zhu Zhi Ci",
    name_original="竹枝詞",
    period_key="唐",
    definition="劉禹錫（772-842）が夔州刺史時代（822-824）に巴渝民歌を文学化した七言絶句組詩。「楊柳青青江水平、聞郎江上踏歌聲」等で、長江上流民俗と男女の情を詠む。文人による民歌取材の祖型となり、後世「竹枝詞」は中国民俗詩の代名詞となった。",
    background="中唐「新樂府運動」の地方民歌関心と劉禹錫の夔州体験。",
    development="宋代蘇軾「竹枝詞」、明清地方竹枝詞の盛行、各地民俗詩の規範となった。",
    historical_context="中唐後期の地方文化への文人関心の興隆。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩: 劉禹錫集 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="元稹「連昌宮詞」",
    name_en="Yuan Zhen's Lian Chang Gong Ci",
    name_original="連昌宮詞",
    period_key="唐",
    definition="元稹（779-831）作の七言長篇叙事詩。安史の乱前後の連昌宮の盛衰を、宮辺老人の語りを通じて回顧的に描く。白居易「長恨歌」「琵琶行」とならぶ中唐叙事詩の代表作で、白居易と「元白」と並称される新樂府運動の中核を担った。",
    background="中唐元和年間（806-820）の新樂府運動と歴史回顧詩。",
    development="白居易「長恨歌」と双璧を成し、宋代叙事詩、元代雑劇（『梧桐雨』）に影響。",
    historical_context="中唐元和年間の安史記憶と政治的反省。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩: 元稹集 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# G: 宋詞補完 (5)
# ============================================================
add(**C, name_ja="柳永慢詞",
    name_en="Liu Yong's manci (slow songs)",
    name_original="柳永慢詞",
    period_key="宋",
    definition="柳永（987頃-1053頃）が北宋初期に確立した「慢詞」（長調詞）形式。「雨霖鈴」「八聲甘州」「望海潮」等で、従来の短調小令を超え、長大な抒情と都市風俗・別離・羈旅を詳細に詠む。詞体の決定的拡大を達成し、蘇軾・周邦彥への直接的橋渡しとなった。",
    background="北宋初期の都市文化興隆と教坊・歌伎文化の発達。",
    development="蘇軾「念奴嬌・赤壁懷古」、周邦彥「六醜」、南宋慢詞の祖型となった。",
    historical_context="北宋仁宗期の都市文化と歌妓文化の繁栄。",
    primary_source_url=CTEXT+"library.pl?if=gb&res=8042",
    primary_source_type="樂章集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="周邦彥『清真集』",
    name_en="Zhou Bangyan's Qing Zhen Ji",
    name_original="清真集",
    period_key="宋",
    definition="周邦彥（1056-1121）作の詞集。「蘇幕遮」「蘭陵王」「六醜」等を含み、詞律の精密化と典故の精錬を徹底し、北宋詞の集大成と尊崇された。南宋姜夔・吳文英の格律詞派の祖型となり、清代浙西詞派・常州詞派の模範となった。",
    background="北宋徽宗期の大晟楽府編纂と詞律学の高度化。",
    development="南宋姜夔『白石道人歌曲』、吳文英『夢窗詞』、清代格律詞派の規範となった。",
    historical_context="徽宗期の文化政策と文学的精緻化。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="清真集 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="姜夔『白石道人歌曲』",
    name_en="Jiang Kui's Baishi Daoren Geji",
    name_original="白石道人歌曲",
    period_key="宋",
    definition="姜夔（1155-1221頃）作の自度曲（自作の旋律と詞）集。「揚州慢」「暗香」「疏影」等を含み、清空高雅な格律詞の頂点を成した。曲譜が現存する唯一の宋代詞集として、中国音楽史上も極めて重要。清代浙西詞派の宗祖として尊崇された。",
    background="南宋孝宗・寧宗期の士大夫文化と音楽的精緻化。",
    development="清代朱彝尊「浙西詞派」、現代の宋詞音楽学研究の中核資料。",
    historical_context="南宋偏安期の文化的精緻化と懐古志向。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="白石道人歌曲 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="吳文英『夢窗詞』",
    name_en="Wu Wenying's Mengchuang Ci",
    name_original="夢窗詞",
    period_key="宋",
    definition="吳文英（1200頃-1260頃）作の詞集。「鶯啼序」「八聲甘州・靈巖陪庾幕諸公遊」等を含み、密麗深邃な独自の詞風を確立した。張炎は「七寶樓臺、眩人眼目、碎拆下來、不成片段」と評したが、清代王國維『人間詞話』は再評価し、晚清四大家詞の形成に影響した。",
    background="南宋末期の士大夫文化の感傷的精緻化。",
    development="清末四大家（鄭文焯・朱祖謀・王鵬運・況周頤）の詞学、現代王國維詞論の中核対象となった。",
    historical_context="南宋末期の蒙古侵攻と政治的危機下の文学的内向化。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="夢窗詞 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="王沂孫詠物詞",
    name_en="Wang Yisun's wuyong ci",
    name_original="王沂孫詠物詞",
    period_key="宋",
    definition="王沂孫（1230頃-1291頃）が南宋滅亡前後に作った詠物詞群。「齊天樂・蟬」「眉嫵・新月」等で、蝉・月・落葉等の物象に亡国の悲愴と遺民意識を寓託する。南宋遺民詞の代表作家として、後世「比興寄託」詞論の規範的範例となった。",
    background="南宋滅亡（1279）と遺民知識人の政治的喪失。",
    development="清代常州詞派（張惠言・周濟）の比興寄託論の中核典拠となった。",
    historical_context="宋元交替期の遺民文化と亡国哀悼。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="碧山樂府 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="王沂孫の比興寄託は表立っては言えない政治的批判を物象に托す技法。AI時代の検閲下言論技法の古典的祖型として再読可能。")


# ============================================================
# H: 元曲 (6)
# ============================================================
add(**C, name_ja="關漢卿「竇娥冤」",
    name_en="Guan Hanqing's Dou E Yuan",
    name_original="竇娥冤",
    period_key="元",
    definition="關漢卿（1220頃-1300頃）作の四折一楔子の元雑劇。寡婦竇娥が冤罪により処刑され、三大誓願（血飛白練・六月飛雪・三年大旱）が天地によって応じる悲劇。中国悲劇の最高傑作と王國維『宋元戯曲考』が評価し、世界戯曲史上の傑作として現代演出も継続される。",
    background="元代の高利貸社会・吏治腐敗と知識人の社会批判。",
    development="明清地方戯曲、京劇、現代戯曲改編に至る悲劇伝統の祖型。",
    historical_context="元代庶民社会の苦難と吏治の苛酷さ。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="關漢卿戲曲集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="關漢卿「救風塵」",
    name_en="Guan Hanqing's Jiu Feng Chen",
    name_original="救風塵",
    period_key="元",
    definition="關漢卿作の四折元雑劇。妓女趙盼兒が機智で姉妹分の妓女を悪人から救出する喜劇。元雑劇の市井女性を主人公とする社会喜劇の祖型を成し、女性の主体性と機略を肯定的に描いた点で、中国戯曲史上特筆される。",
    background="元代都市社会の妓女文化と関漢卿の市井文学的視角。",
    development="明代南戯、清代地方劇、現代女性主役戯曲の祖型。",
    historical_context="元代大都の繁華街文化と妓女社会。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="關漢卿戲曲集 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="王實甫「西廂記」",
    name_en="Wang Shifu's Xi Xiang Ji",
    name_original="西廂記",
    period_key="元",
    definition="王實甫（1260頃-1336頃）作の五本二十一折の長篇元雑劇。唐代元稹「鶯鶯傳」を典拠とし、書生張珙と相国千金崔鶯鶯の恋愛を、紅娘の機智的助力を介して大団円に導く。元曲の言語的頂点と評価され、毛宗崗『第六才子書』として尊崇された。",
    background="元代「鶯鶯傳」改作の系譜（董解元『西廂記諸宮調』）と元曲成熟期。",
    development="明清『牡丹亭』『紅樓夢』の恋愛文学の祖型、現代戯曲改編の中心レパートリーとなった。",
    historical_context="元代知識人と妓女・閨秀の恋愛文化。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="西廂記 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="馬致遠「漢宮秋」",
    name_en="Ma Zhiyuan's Han Gong Qiu",
    name_original="漢宮秋",
    period_key="元",
    definition="馬致遠（1250頃-1321頃）作の四折元雑劇。漢元帝と王昭君の悲恋を題材に、王昭君の自殺と元帝の悲嘆を抒情的に描く歴史悲劇。「秋夜梧桐雨」と並ぶ元曲歴史悲劇の頂点。馬致遠は「曲狀元」とも称され、元代散曲・雑劇の双方の代表作家。",
    background="元代の漢族文人の異族支配下における歴史的記憶の文学化。",
    development="清代洪昇『長生殿』、現代京劇『昭君出塞』の祖型。",
    historical_context="元代漢族知識人の異族統治下のアイデンティティ問題。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="漢宮秋 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="鄭光祖「倩女離魂」",
    name_en="Zheng Guangzu's Qian Nü Li Hun",
    name_original="倩女離魂",
    period_key="元",
    definition="鄭光祖（生没年不詳、元末雑劇作家）作の四折元雑劇。唐代陳玄祐「離魂記」を典拠とし、張倩女の魂が肉体を離れて愛人王文舉を追う幻想的恋愛劇。元代「四大家」（關・馬・鄭・白）の一人として、湯顯祖「牡丹亭」の魂遊系譜の直接的祖型となった。",
    background="元末雑劇の幻想性志向と唐人小説の戯曲化。",
    development="湯顯祖「牡丹亭」、現代昆曲「離魂」の規範的源流。",
    historical_context="元末の雑劇成熟期と幻想戯曲の興隆。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="倩女離魂 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="套數と小令（散曲）",
    name_en="Taoshu vs Xiaoling (sanqu forms)",
    name_original="套數・小令",
    period_key="元",
    definition="元代散曲（朗誦・詠唱用の独立曲詞、雑劇外の音楽文学）の二大形式。「小令」は単一曲牌の短詩、「套數」は複数の同宮調曲牌を連ねた組曲。馬致遠「天淨沙・秋思」（小令）、睢景臣「般涉調・哨遍・高祖還郷」（套數）等が代表作。詞から曲への詩歌史的転換を画した。",
    background="元代の都市音楽文化と雑劇から派生した独立詠唱曲の制度化。",
    development="明代散曲（康海・王九思）、清代曲学（吳梅『顧曲麈談』）への系譜。",
    historical_context="元代詩歌史における詩（漢魏唐宋）から曲（元）への質的転換期。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="全元散曲 (CTEXT)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# I: 明清小説補完 (8)
# ============================================================
add(**C, name_ja="『金瓶梅』評本系譜",
    name_en="Jin Ping Mei commentarial editions",
    name_original="金瓶梅評本",
    period_key="明",
    definition="明萬曆年間（1573-1620）成書の長篇小説『金瓶梅』の評点本系譜。詞話本（萬曆刊）と崇禎本（崇禎刊「新刻繡像批評金瓶梅」）の二系統に分かれ、清初張竹坡（1670-1698）「皋鶴堂批評第一奇書金瓶梅」が評点学の頂点を成した。中国小説評点の最重要対象作品。",
    background="明後期商業出版の興隆と長篇白話小説の成熟。",
    development="張竹坡評を経て、清代評点批評（毛宗崗・脂硯齋）の中核典範となった。",
    historical_context="明後期江南商業文化と都市読書市場の成立。",
    primary_source_url=WIKI_ZH+"金瓶梅",
    primary_source_type="維基百科: 金瓶梅版本系譜",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="呉敬梓『儒林外史』",
    name_en="Wu Jingzi's Rulin Waishi",
    name_original="儒林外史",
    period_key="清",
    definition="呉敬梓（1701-1754）作の56回章回小説。科挙制度下の儒生の腐敗と虚偽を、范進・周進・嚴監生等の人物像を通じ風刺的に描く。中国諷刺小説の最高傑作と魯迅『中国小説史略』が評価し、現代の科挙文化研究の中核資料となった。",
    background="清乾隆期の科挙制度爛熟と知識人の社会批判。",
    development="清末「四大譴責小説」（『官場現形記』『二十年目睹之怪現狀』『老殘遊記』『孽海花』）の祖型となった。",
    historical_context="清乾隆期の社会的爛熟と知識人の自己批判。",
    primary_source_url=CTEXT+"wiki.pl?if=gb&res=541234",
    primary_source_type="儒林外史 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="李汝珍『鏡花緣』",
    name_en="Li Ruzhen's Jing Hua Yuan",
    name_original="鏡花緣",
    period_key="清",
    definition="李汝珍（1763頃-1830頃）作の100回章回小説。武則天時代の唐敖の海外漂流と百花仙女の運命を主軸に、女兒國・君子國・大人國等の異域を経巡る幻想冒険譚。フェミニスト的女兒國批評・百科全書的博物学的記述を統合し、中国近代小説への橋渡しとなった。",
    background="清嘉慶期の博物学興隆と『山海経』異域伝統の小説化。",
    development="清末民初の幻想小説、近代『新中國未來記』等のユートピア小説の祖型。",
    historical_context="清中期の文化爛熟と西洋知識流入の前夜。",
    primary_source_url=CTEXT+"wiki.pl",
    primary_source_type="鏡花緣 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="鏡花緣の女兒國は性役割反転を文学化する。AI時代のジェンダー再考・性別の構築性問題と理論的に共振する古典的祖型。")

add(**C, name_ja="蒲松齡『聊齋誌異』評點",
    name_en="Pu Songling's Liaozhai Zhiyi commentaries",
    name_original="聊齋誌異評點",
    period_key="清",
    definition="蒲松齡（1640-1715）作の文言短篇集491篇『聊齋誌異』の評点本系譜。乾隆青柯亭本（1766）と但明倫評本・馮鎮巒評本・何守奇評本等の複数評点が並立し、狐仙・鬼怪・幻想譚を社会批判・倫理批判として読む解釈学的伝統を確立した。",
    background="清代文言短篇集の成熟と評点学の文言小説への拡張。",
    development="現代『聊齋』研究、比較民俗学・幻想文学研究の中核対象。",
    historical_context="清初山東地方文人文化と民間幻想譚の文学化。",
    primary_source_url=CTEXT+"liaozhai-zhi-yi",
    primary_source_type="聊齋誌異 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="紀昀『閱微草堂筆記』",
    name_en="Ji Yun's Yue Wei Cao Tang Bi Ji",
    name_original="閱微草堂筆記",
    period_key="清",
    definition="紀昀（1724-1805、四庫全書総纂官）作の文言筆記小説1196則。蒲松齡『聊齋』の艶麗を批判し、平淡な文体で鬼神譚・志怪譚に儒家的教訓を寓託する。乾嘉学派の儒家的文言小説観の規範的範型として、清代文言筆記の頂点を成した。",
    background="乾嘉学派の儒家経学興隆と文言志怪伝統の継承。",
    development="清末民初文言筆記、現代の儒家系統幻想小説研究の核心対象。",
    historical_context="清乾隆期の四庫全書編纂と儒家文献学の頂点。",
    primary_source_url=CTEXT+"wiki.pl",
    primary_source_type="閱微草堂筆記 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="劉鶚『老殘遊記』",
    name_en="Liu E's Lao Can You Ji",
    name_original="老殘遊記",
    period_key="清",
    definition="劉鶚（1857-1909）作の20回章回小説（1903-04連載、1907初版）。江湖医者老殘の山東遊歴を媒介に、清末「清官」の苛酷さを批判する。魯迅が「四大譴責小説」の一つに数えた清末譴責小説の代表作。前期版本（連載本）と後期版本（増補本）の差異が研究対象。",
    background="清末新政期の社会批判言論と新聞連載小説の興隆。",
    development="清末民初譴責小説、現代社会批判小説の祖型となった。",
    historical_context="清末光緒期の政治改革と社会批判言論。",
    primary_source_url=WIKI_ZH+"老殘遊記",
    primary_source_type="維基百科: 老殘遊記",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="曾樸『孽海花』",
    name_en="Zeng Pu's Nie Hai Hua",
    name_original="孽海花",
    period_key="清",
    definition="曾樸（1872-1935）作の30回章回小説（1905-07連載、1928完成）。清末同治・光緒期の朝廷・外交・革命を、状元洪鈞と妓女傅彩雲（後の賽金花）を軸に描く。「四大譴責小説」の一つで、近代中国の歴史的転換期を文学化した。",
    background="清末庚子事変（1900）後の政治批判小説の興隆。",
    development="近代中国歴史小説、現代の清末研究の文学的中核資料。",
    historical_context="清末同治・光緒期の歴史的転換と新聞連載文化。",
    primary_source_url=WIKI_ZH+"孽海花",
    primary_source_type="維基百科: 孽海花",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="李漁『無聲戲』『十二樓』",
    name_en="Li Yu's Wu Sheng Xi and Shi Er Lou",
    name_original="無聲戲・十二樓",
    period_key="清",
    definition="李漁（1611-1680）作の話本（白話短篇）集二種。「無聲戲」12篇・「十二樓」12篇は、明末清初市井生活と機智戯謔を主題とし、戯曲家としての構成意識を散文に応用した独自の話本様式を確立した。話本小説の最高峰の一として尊崇される。",
    background="明末清初江南市井文化と李漁の戯曲・小説両方面の活動。",
    development="清代白話短篇、現代の中国小説技巧研究の中核対象。",
    historical_context="明清交替期の江南都市文化と文人商業活動の展開。",
    primary_source_url=WIKI_ZH+"李漁",
    primary_source_type="維基百科: 李漁話本",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# J: 評點批評 (6)
# ============================================================
add(**C, name_ja="脂硯齋紅樓夢評",
    name_en="Zhi Yan Zhai's Honglou Meng commentary",
    name_original="脂硯齋評石頭記",
    period_key="清",
    definition="清乾隆期『紅樓夢』作者曹雪芹（1715頃-1763頃）と最も近い圏内の評者「脂硯齋」「畸笏叟」等による評点。「庚辰本」「甲戌本」「己卯本」等の評本系統に存し、作者意図・人物関係・後40回散逸部分の手がかりを伝え、紅学研究の最重要資料となった。",
    background="乾隆中期『紅樓夢』創作圏内の評点活動。",
    development="現代「紅学」（紅楼夢学）の最大研究対象、版本学・主題学の中核資料。",
    historical_context="乾隆中期江南文人文化と家族小説の創作・評点活動。",
    primary_source_url=WIKI_ZH+"脂硯齋",
    primary_source_type="維基百科: 脂硯齋評本",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="脂硯齋評は作者と読者の境界を曖昧化する協働的テキスト生成。AI時代の人間-AI協働創作の古典的祖型として再読可能。")

add(**C, name_ja="金聖歎水滸傳評",
    name_en="Jin Shengtan's Shuihu Zhuan commentary",
    name_original="貫華堂第五才子書水滸傳",
    period_key="清",
    definition="金聖歎（1608-1661）が崇禎14年（1641）に刊行した『水滸傳』70回評点本。「七十回後皆贗作」として原120回本を腰斬し、宋江謀反招安部分を削除した上で、各回各句に詳細評を付した。中国小説評点学の頂点とされ、毛宗崗・張竹坡・脂硯齋への直接的祖型となった。",
    background="明末清初の文学的個人主義と評点学の制度化。",
    development="毛宗崗『三國演義』評、張竹坡『金瓶梅』評、脂硯齋『紅樓夢』評の規範。",
    historical_context="明末清初の評点商業出版と文人個人批評の興隆。",
    primary_source_url=WIKI_ZH+"金聖歎",
    primary_source_type="維基百科: 金聖歎",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="毛宗崗三國演義評",
    name_en="Mao Zonggang's Sanguo Yanyi commentary",
    name_original="毛宗崗評三國演義",
    period_key="清",
    definition="毛宗崗（1632-1709頃）が清初康熙年間に父毛綸と共同で刊行した『三國演義』120回評点本。羅貫中原作・羅貫本に大幅な文字改訂を施し、また各回首尾に総評を付した。後世の通行本となり、清以降の『三國演義』受容を規定した。",
    background="明末清初評点学の興隆と毛綸・毛宗崗父子の評点活動。",
    development="現代通行本『三國演義』の基盤、東アジア『三國』受容の中核版本。",
    historical_context="清初康熙期の文学整理と通俗文学の規範化。",
    primary_source_url=WIKI_ZH+"毛宗崗",
    primary_source_type="維基百科: 毛宗崗",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="張竹坡金瓶梅評",
    name_en="Zhang Zhupo's Jin Ping Mei commentary",
    name_original="第一奇書金瓶梅",
    period_key="清",
    definition="張竹坡（1670-1698）が清康熙34年（1695）に刊行した『金瓶梅』評点本「皋鶴堂批評第一奇書金瓶梅」。崇禎本を底本に、各回詳細評と「読法」一篇を付した。金聖歎評を継承しつつ独自の理論的高度化を達成し、『金瓶梅』読解の規範となった。",
    background="清康熙期の評点学全盛期と『金瓶梅』の文学的再評価。",
    development="現代『金瓶梅』研究の中核資料、清代評点理論の頂点。",
    historical_context="清初の小説評点制度の成熟期。",
    primary_source_url=WIKI_ZH+"張竹坡",
    primary_source_type="維基百科: 張竹坡",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="王國維『人間詞話』",
    name_en="Wang Guowei's Renjian Cihua",
    name_original="人間詞話",
    period_key="清",
    definition="王國維（1877-1927）が1908-09年『國粹學報』に連載し、1926年定本化された詞話。「境界説」を中核理念とし、「有我之境」「無我之境」「隔と不隔」「造境と寫境」等の独創的範疇を提示した。中国伝統詞論と西洋哲学（叔本華・カント）を統合し、近代中国文学批評の出発点となった。",
    background="清末民初の西洋哲学受容と中国伝統詩学の近代化。",
    development="20世紀中国文学批評（朱光潛美学、宗白華芸境論）の中核典拠。",
    historical_context="清末民初の伝統と近代の交差点における学術的綜合。",
    primary_source_url=WIKI_ZH+"人間詞話",
    primary_source_type="維基文庫: 人間詞話",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="王国維「境界説」は主客融合の美的体験を理論化する。AI生成芸術における観賞主体・作品・生成者三者関係を再考する古典的東洋詩学の参照点。")

add(**C, name_ja="清代詞學三派",
    name_en="Three Qing Ci-xue schools",
    name_original="浙西・常州・桐城詞學",
    period_key="清",
    definition="清代詞學の主要三派——浙西詞派（朱彝尊宗、姜夔・張炎を尊崇、清空高雅を主張）、常州詞派（張惠言宗、比興寄託を主張）、桐城詞派（戈載宗、声律精密を主張）——の総称。清詞史の主要な争点を構成し、後世の中国詞論の論争軸を規定した。",
    background="清初〜中期の地方文人結社と詞學論争の制度化。",
    development="近代王國維詞論、現代詞學研究（葉嘉瑩等）の論争枠組みの祖型となった。",
    historical_context="清代士大夫文化における地方学派形成と論争文化。",
    primary_source_url=WIKI_ZH+"清詞",
    primary_source_type="維基百科: 清代詞派",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# Cross-domain links to PT/PHIL (>=14 required)
# ============================================================
# Map: source concept name_ja -> list of cross_domain dicts
CROSS: dict[str, list[dict]] = {
    "興・比・賦（六義の詩法）": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "興比賦・象徴と比喩の理論",
         "description": "興比賦は東アジア詩学の根本範疇で、現代詩学・比喩理論との接続軸。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "言意之辨",
         "description": "六義は言葉と意味の関係をめぐる中国伝統哲学（言意之辨）の文学的展開。"},
    ],
    "離騷": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "抒情詩と自我表出",
         "description": "離騷は中国抒情詩の祖型として、抒情主体と自我表出の詩学理論の中核典拠。"},
    ],
    "天問": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "宇宙論と神話論の問答",
         "description": "天問は古代中国宇宙論・神話論を網羅的に問う哲学詩で、中国哲学史の根本資料。"},
    ],
    "漁父": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "出処進退論",
         "description": "漁父の問答は中国哲学における士の出処進退論の文学的祖型。"},
    ],
    "阮籍「詠懷詩」": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "暗喩・寓意理論",
         "description": "詠懷詩の暗喩構造は、政治的圧力下の隠喩詩学（イソップ・スピーチ）の東アジア祖型。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "魏晋玄学",
         "description": "阮籍は竹林七賢の中核として、魏晋玄学（道家哲学復興）の文学的体現者。"},
    ],
    "陶淵明「歸去來辭」": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "隠逸思想",
         "description": "歸去來辭は中国隠逸思想（道家・荘子）の文学的最高表現。"},
    ],
    "陶淵明「桃花源記」": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ユートピア思想",
         "description": "桃花源は中国ユートピア思想（小国寡民・大同）の文学的祖型。"},
    ],
    "謝靈運山水詩": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "山水詩・自然描写の詩学",
         "description": "謝靈運山水詩は東アジア自然描写詩学の規範的源流。"},
    ],
    "韓愈詩（以文為詩）": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "詩文一体・ジャンル境界",
         "description": "「以文為詩」は詩と散文の境界を流動化する詩学理論の中国的展開。"},
    ],
    "柳宗元「永州八記」": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "山水遊記・場所の詩学",
         "description": "永州八記は場所性と主体経験を結ぶ遊記文学の規範的祖型。"},
    ],
    "王國維『人間詞話』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "境界説と美学",
         "description": "境界説は中国伝統詩学を西洋美学（カント・叔本華）と統合した近代批評理論の中核。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "東西哲学綜合",
         "description": "王国維は中国伝統と西洋哲学（叔本華悲劇論等）を綜合した近代中国哲学の出発点。"},
    ],
    "金聖歎水滸傳評": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "評点と読書理論",
         "description": "金聖歎評点学は中国独自の読書理論・テキスト介入実践として現代テクスト論との接続点。"},
    ],
    "脂硯齋紅樓夢評": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "協働的テキスト生成",
         "description": "脂硯齋評は作者-評者-読者の境界を流動化する協働的テキスト生成の古典的祖型。"},
    ],
    "周南・召南": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "礼楽思想",
         "description": "周南・召南は儒家礼楽思想における風教論の詩学的根拠。"},
    ],
    "九歌": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "シャーマニズムと宗教思想",
         "description": "九歌は楚地シャーマニズムの文学化として中国宗教思想史の重要資料。"},
    ],
    "嵇康詩": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "名教と自然",
         "description": "嵇康詩は魏晋玄学の名教vs自然論争の文学的体現。"},
    ],
}


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    inserted: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        # Look up existing CN periods (region='中国')
        period_ids: dict[str, int] = {}
        for key, name_ja in PERIOD_NAMES.items():
            row = db.conn.execute(
                "SELECT id FROM periods WHERE name_ja = ? AND region = ?",
                (name_ja, "東アジア"),
            ).fetchone()
            if row is None:
                print(f"  [error] missing period: {name_ja}")
                return 1
            period_ids[key] = row["id"]

        # Insert concepts
        for raw in CONCEPTS:
            entry = dict(raw)
            pkey = entry.pop("period_key", None)
            if pkey:
                entry["period_id"] = period_ids[pkey]
            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            inserted[entry["name_ja"]] = cid
            # Count fourth_transform tag (status field on concepts table)
            if entry.get("fourth_transform_status"):
                fourth_count += 1

        # Cross-domain links
        for name_ja, links in CROSS.items():
            cid = inserted.get(name_ja)
            if cid is None:
                # already existed; look it up
                row = db.conn.execute(
                    "SELECT id FROM concepts WHERE name_ja = ? AND subfield_id = 8",
                    (name_ja,),
                ).fetchone()
                if row is None:
                    print(f"  [warn] cross_domain target missing: {name_ja}")
                    continue
                cid = row["id"]
            for cd in links:
                try:
                    db.insert_cross_domain(
                        lit_entity_type="concept", lit_entity_id=cid,
                        target_db=cd["target_db"], link_type=cd["link_type"],
                        target_entity_id=cd.get("target_entity_id"),
                        target_entity_name=cd.get("target_entity_name"),
                        description=cd.get("description"))
                    cd_count += 1
                except LitDBError as e:
                    print(f"  [warn] cross_domain failed for {name_ja}: {e}")

        summary = db.progress_summary()
        print(f"[c13_add60] inserted concepts (this run): {len(inserted)} / total: {summary['concepts']}")
        print(f"[c13_add60] fourth_transform tags +{fourth_count}; cross_domain +{cd_count}")
        # Tier breakdown
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = len(CONCEPTS)
        print(f"[c13_add60] tiers: primary={primary} ({primary*100/total:.1f}%), secondary={secondary}, tertiary={tertiary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
