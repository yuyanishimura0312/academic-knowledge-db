"""LIT-DB Phase 2 Wave 15 — C16: Japanese Classical Literature ADD 80.

Subfield: lit_jp_classical (id=10), region='東アジア'.
Existing periods (reused): 上代/中古/中世/近世.

Coverage (80 NEW concepts, NON-overlapping with existing 140):
  A: 万葉集詳細 (12) — 巻一/巻二/巻三/巻七/巻十/巻十六/巻十九, 大伴家持秋風の歌, 笠女郎贈答歌,
                       額田王・但馬皇女・湯原王皇族歌人, 大津皇子辞世歌, 万葉集編纂主体論争,
                       万葉仮名表記研究, 訓字訓詠論争
  B: 和漢比較 (6)   — 経國集細目, 都氏文集都良香, 朝野群載文学性, 性霊集空海,
                       文鏡秘府論詩学, 雑談集無住（漢学的側面）
  C: 古今集系譜 (12) — 古今集仮名序紀貫之, 真名序紀淑望, 後撰集源順, 拾遺集藤原公任,
                       後拾遺集藤原通俊, 金葉集源俊頼三奏本, 詞花集藤原顕輔, 千載集藤原俊成,
                       新古今集藤原定家初撰本, 新勅撰集, 八代集論, 二十一代集体系
  D: 私家集 (14)    — 人麻呂集, 赤人集, 家持集, 貫之集, 躬恒集, 業平集, 小町集, 紫式部集,
                       和泉式部集, 長秋詠藻俊成, 拾遺愚草定家, 山家集西行, 拾玉集慈円, 金槐和歌集実朝
  E: 中古日記補完 (3) — 土佐日記原本仮名表記, 和泉式部日記三親王恋愛, 増基法師庵日記
  F: 中世紀行・連歌 (10) — 海道記, 東関紀行, 十六夜日記, 都の苞, 二条良基筑波集編纂,
                            心敬十題, 宗祇水無瀬三吟百韻, 老葉, 守武千句, 連歌之作法書
  G: 軍記補完 (4)   — 将門記, 陸奥話記, 平家物語覚一本/延慶本対比, 吾妻鏡編纂
  H: 能・狂言 (8)   — 風姿花伝七篇別段, 花鏡, 至花道, 三道, 拾玉得花, 申楽談義,
                       禅竹歌舞髄脳記六輪一露, 大蔵流狂言三百番
  I: 近世補完 (11)  — 西鶴本朝二十不孝, 諸艶大鑑, 武家義理物語, 男色大鑑,
                       近松世話浄瑠璃曾根崎心中・心中天網島・冥途の飛脚・女殺油地獄,
                       国性爺合戦, 春雨物語各章, 国学和歌四大人, 桂園派香川景樹
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


NIJL = "https://kokusho.nijl.ac.jp/"
NDL = "https://dl.ndl.go.jp/"
AOZORA = "https://www.aozora.gr.jp/"
JSTAGE = "https://www.jstage.jst.go.jp/"
SAT = "https://21dzk.l.u-tokyo.ac.jp/SAT/"
WASEDA = "https://www.wul.waseda.ac.jp/kotenseki/"
JTI = "https://jti.lib.virginia.edu/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_jp_classical", region="東アジア",
         original_script="kanji_kana")


# ============================================================
# A: 万葉集詳細（12）  period: 上代
# ============================================================
add(**C, name_ja="萬葉集巻一", name_en="Manyoshu Volume 1",
    name_original="萬葉集巻一",
    period_key="上代",
    definition="『萬葉集』巻一は雑歌84首を収録する。仁徳天皇皇后磐姫の歌に始まり、舒明・天智・天武・持統・文武・元明・元正各朝の主要な雑歌を編年的に配列する。萬葉集の冒頭巻として、皇統儀礼歌の正典的選定を示し、巻二（相聞・挽歌）と対をなして上代宮廷歌の二大部立を確立する。",
    background="奈良前期の編纂による皇統儀礼歌の正典化。",
    development="伊藤博・稲岡耕二の巻一研究が現代解釈の基盤を成す。",
    historical_context="天武・持統皇統儀礼歌制度の集約。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻一",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"巻一の皇統儀礼歌正典化は国家的物語編成の作者性を示し、AI時代の国家的物語生成と作者性の問題を再考する古典的参照点となる。",
         "related_ai_phenomenon":"AI時代の国家的物語生成と作者性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"皇統儀礼歌の制度化",
         "description":"巻一の皇統儀礼歌は古代王権の儀礼的正当化過程を文学化し、人類学的王権論の比較対象として中核的位置を占める。"}])

add(**C, name_ja="萬葉集巻二", name_en="Manyoshu Volume 2",
    name_original="萬葉集巻二",
    period_key="上代",
    definition="『萬葉集』巻二は相聞150首・挽歌150首を収録する。磐姫皇后相聞歌に始まり、額田王・天智天皇相聞歌、天武持統相聞歌を経て、有間皇子・大津皇子・草壁皇子・高市皇子等の挽歌に至る。相聞・挽歌の二部立を皇統年代順に並べ、人麻呂挽歌の頂点を含む宮廷歌の精華を集約する。",
    background="人麻呂活躍期の宮廷儀礼挽歌制度成熟。",
    development="人麻呂研究・挽歌研究の中核資料となった。",
    historical_context="天智・天武・持統朝の皇族死とその挽歌儀礼。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻二",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"persistent",
         "rationale":"巻二の挽歌群は皇統儀礼における死者主体の声の代弁を文学化した古代事例で、AI時代における故人の声の生成倫理を再考する参照点となる。",
         "related_ai_phenomenon":"AI生成による故人の声の倫理"}])

add(**C, name_ja="萬葉集巻三", name_en="Manyoshu Volume 3",
    name_original="萬葉集巻三",
    period_key="上代",
    definition="『萬葉集』巻三は雑歌・譬喩歌・挽歌を収録する250余首の巻。山部赤人富士山讃歌（317-318）、笠金村行幸歌、家持初期作等を含む。雑歌の中核に行幸従駕歌を据え、譬喩歌（恋情を物に寄せる歌）を独立部立として配する点で、萬葉部立論上重要な位置を占める。",
    background="奈良前期から中期の宮廷従駕歌制度。",
    development="赤人富士山歌は近世以降日本叙景歌の頂点として再評価された。",
    historical_context="聖武朝行幸文化の隆盛期。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻三",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="萬葉集巻七", name_en="Manyoshu Volume 7",
    name_original="萬葉集巻七",
    period_key="上代",
    definition="『萬葉集』巻七は作者未詳歌約350首を収め、雑歌・譬喩歌・挽歌の三部立を持つ。古歌集・古集・人麻呂歌集等から採録され、定型化された序詞・枕詞を駆使する短歌中心の構成で、宮廷外の歌謡的基層を伝える点で重要。萬葉中期の歌謡定型化過程の証左となる。",
    background="人麻呂歌集等の準匿名歌集の編纂的吸収。",
    development="伊藤博『萬葉集の構造と成立』で巻七の作者未詳歌の起源論が精緻化された。",
    historical_context="奈良前期から中期の歌謡的基層と宮廷歌人の継承関係。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻七",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="萬葉集巻十", name_en="Manyoshu Volume 10",
    name_original="萬葉集巻十",
    period_key="上代",
    definition="『萬葉集』巻十は四季雑歌・四季相聞各約250首を収め、季節分類による編集を採用した最初期の和歌集として極めて重要。後の四季部立による『古今集』編纂の祖型となり、日本和歌史における季節部立の起源を成す。作者未詳歌が大半を占め、人麻呂歌集を主要源泉とする。",
    background="奈良中期の季節歌謡蓄積と季節部立の文学的創発。",
    development="『古今集』四季部立の祖型となり、日本季節歌の制度的起源を成す。",
    historical_context="奈良中期の和歌部立論の成熟期。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻十",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="萬葉集巻十六", name_en="Manyoshu Volume 16",
    name_original="萬葉集巻十六",
    period_key="上代",
    definition="『萬葉集』巻十六「有由縁并雑歌」は104首を収め、各歌に長文の左注または題詞で歌の縁起・伝承を付す独特の巻。竹取翁歌・乞食者歌・遊行女婦歌等、宮廷正統儀礼歌から外れた周縁的歌謡を多く含み、上代日本の口承伝承・芸能・社会層を伝える稀有な記録として民俗学・社会史の第一級資料となる。",
    background="奈良時代周縁芸能・口承伝承の文字化への関心。",
    development="折口信夫・柳田国男以来の民俗学が巻十六を中核資料とした。",
    historical_context="宮廷正統儀礼歌の周縁にある芸能者・遊行者の文化。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻十六",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"周縁的口承伝承の文字化",
         "description":"巻十六の有由縁雑歌は古代日本の周縁芸能者・遊行者の口承を文字化した稀有な事例で、人類学的口承伝承研究の比較対象となる。"}])

add(**C, name_ja="萬葉集巻十九", name_en="Manyoshu Volume 19",
    name_original="萬葉集巻十九",
    period_key="上代",
    definition="『萬葉集』巻十九は天平勝宝期（749-756）の家持私家集化が進んだ巻で、154首を収める。家持の越中守時代から帰京後の作を中心に、家持自作の長歌・短歌、橘諸兄家宴席歌等を集約する。家持萬葉集編纂の最終局面を示す重要な巻として、伊藤博等の家持編纂論の中核資料。",
    background="家持の萬葉集私家集化の最終局面。",
    development="家持編纂論の中核資料となり、家持文学的自意識の発展を示す。",
    historical_context="天平勝宝期の橘諸兄政権下での家持文化的活動。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻十九",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="大伴家持「秋風の歌」",
    name_en="Otomo no Yakamochi: Autumn Wind Verses",
    name_original="秋風の歌",
    period_key="上代",
    definition="大伴家持が天平勝宝5年（753）に詠んだ巻十九所収の三首一連（4290-4292）「春の野に霞たなびきうら悲し…」「我が宿のいささ群竹吹く風の音のかそけきこの夕かも」を含む独詠歌群。家持の内省的孤独感と微細な自然感受を示し、近代以降「日本的抒情の祖型」として高く評価された。家持文学の頂点とされる。",
    background="天平勝宝期の家持中央政界での孤立感と内省的歌風確立。",
    development="近代詩歌（北原白秋・斎藤茂吉）が家持秋風の歌を抒情の祖として再発見した。",
    historical_context="天平勝宝5年（753）2月の春秋三首独詠の文脈。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻十九4290-4292",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="笠女郎大伴家持贈答歌",
    name_en="Kasa no Iratsume and Yakamochi exchange poems",
    name_original="笠女郎・大伴家持贈答歌",
    period_key="上代",
    definition="笠女郎が大伴家持に贈った24首（巻四・587-610）を中核とする贈答歌群。家持からの返歌は2首（巻四・611-612）のみで、笠女郎の片恋的情熱が際立つ。「我が形見見つつ偲はせあらたまの年の緒長く我も思はむ」（587）等、女性歌人の主体的恋愛表現として萬葉相聞歌の精華を成す。",
    background="奈良前期の宮廷女性歌人の活動と相聞歌制度。",
    development="女性主体の恋愛詩として近代以降のフェミニズム文学批評が再評価した。",
    historical_context="家持青年期（740年代）の交流圏。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻四587-612",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"笠女郎贈答歌は片想いの女性主体の声を文学化した古代の事例で、AI時代における一方的・非対称関係の表象問題を再考する参照点となる。",
         "related_ai_phenomenon":"AI関係における非対称性と主体性"}])

add(**C, name_ja="額田王・但馬皇女・湯原王（皇族歌人）",
    name_en="Princess Nukata, Princess Tajima, Prince Yuhara",
    name_original="額田王・但馬皇女・湯原王",
    period_key="上代",
    definition="天智・天武朝の女性歌人額田王（生没年未詳、「あかねさす紫野行き標野行き」が著名）、持統朝の但馬皇女（？-708、穂積皇子との恋）、聖武朝の皇族歌人湯原王（志貴皇子の子、繊細な小品で知られる）の3名。皇族歌人として宮廷歌の知的洗練を担い、人麻呂・赤人ら職業歌人とは異なる皇族的視点の和歌世界を提示した。",
    background="天武・持統・聖武朝の皇族文化的活動。",
    development="近代以降、皇族歌人の独自性が和歌史上に位置づけられた。",
    historical_context="天武皇統の文化的成熟期。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻一・二・三・四・八",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="大津皇子辞世歌",
    name_en="Prince Otsu's Death Verse",
    name_original="大津皇子辞世歌",
    period_key="上代",
    definition="大津皇子（663-686）が686年10月3日謀反の罪で死を賜った際の辞世歌「百伝ふ磐余の池に鳴く鴨を今日のみ見てや雲隠りなむ」（巻三・416）。妃山辺皇女の殉死とともに、天武皇統内政争の悲劇を象徴する作品で、辞世歌の祖型を確立した。日本辞世文学の歴史的起点として位置づけられる。",
    background="天武天皇崩御直後の皇位継承争いと、草壁皇子派による大津皇子排斥。",
    development="日本辞世文学（武士・近世武家・近代）の祖型として継承された。",
    historical_context="686年9月天武崩御直後の宮廷政争。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻三・416",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"辞世詩の死生観",
         "description":"大津皇子辞世歌は東アジア辞世文学の祖型を成し、儒仏混淆的死生観を文学化した古代事例として哲学史に接続する。"}])

add(**C, name_ja="萬葉集編纂主体論争",
    name_en="Debate on Manyoshu compilers",
    name_original="萬葉集編纂主体論争",
    period_key="上代",
    definition="『萬葉集』の最終編纂者をめぐる近現代国文学の論争。家持単独編纂説（伊藤博・稲岡耕二）、家持＋複数編者説（佐佐木信綱）、橘諸兄関与説、巻別異編者説等が並立する。20巻全体の編纂的整合性をどう説明するかをめぐり、現代まで決着していない国文学の中核論題。",
    background="20世紀国文学による萬葉集本文批判の深化。",
    development="伊藤博『萬葉集の構造と成立』『萬葉集の歌人と作品』が現代論争の主軸を提供した。",
    historical_context="奈良末期から平安初期の編纂的最終局面の不透明性。",
    primary_source_url=JSTAGE+"article/jjpoetry/-char/ja/",
    primary_source_type="J-STAGE: 萬葉集編纂論論文群",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"萬葉集編纂主体論争は集合的編纂体の作者性問題を古代から問う論題で、AI時代の集合的著作・分散編纂の作者性問題と理論的に響き合う。",
         "related_ai_phenomenon":"AI時代の集合的・分散的著作の作者性"}])

add(**C, name_ja="萬葉仮名表記研究",
    name_en="Manyogana orthographic studies",
    name_original="萬葉仮名",
    period_key="上代",
    definition="『萬葉集』が用いる漢字の音訓借用による日本語表記体系（萬葉仮名）の研究。橋本進吉「上代特殊仮名遣い」（甲類乙類の区別）の発見以来、20世紀日本語学の中核論題となった。音仮名・訓仮名・略音仮名・略訓仮名の分類、巻別表記特性、人麻呂歌集表記等が精緻化されてきた。",
    background="橋本進吉による上代特殊仮名遣いの発見（1917）。",
    development="稲岡耕二『萬葉表記論』、犬飼隆等が現代研究を精緻化した。",
    historical_context="日本語表記体系成立期の文字運用。",
    primary_source_url=JSTAGE+"article/japanese/-char/ja/",
    primary_source_type="J-STAGE: 萬葉仮名研究",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"萬葉仮名は外国語文字（漢字）の音訓借用による母語表記の創発で、AI時代の多言語・多文字混淆表記の祖型として再考される。",
         "related_ai_phenomenon":"AI時代の多言語混淆表記"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"言語表記の哲学",
         "description":"萬葉仮名研究は文字と音声の関係を問う言語哲学の古典的事例で、デリダ的文字論の東アジア的展開と接続する。"}])

add(**C, name_ja="訓字訓詠論争",
    name_en="Debate on logographic vs phonographic reading",
    name_original="訓字訓詠論争",
    period_key="上代",
    definition="『萬葉集』巻一〜四等の訓字主体表記歌を、原作者がどのように音読したかをめぐる近現代国文学の論争。澤瀉久孝・稲岡耕二らが訓字主体表記から原音への復元可能性を探究し、犬飼隆らが復元の限界と表記独自の意味論を主張した。萬葉本文批判の中核論題で、現代でも決着していない。",
    background="20世紀後半の萬葉本文批判の精緻化。",
    development="稲岡耕二『萬葉表記論』、犬飼隆『木簡から探る和歌の起源』が論争の現代局面を構成する。",
    historical_context="奈良時代の訓読・音読の混在状況。",
    primary_source_url=JSTAGE+"article/japanese/-char/ja/",
    primary_source_type="J-STAGE: 萬葉訓字訓詠論",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# B: 和漢比較（6）  period: 中古
# ============================================================
add(**C, name_ja="経國集細目", name_en="Keikokushu detailed structure",
    name_original="経國集",
    period_key="中古",
    definition="『経國集』(827)は淳和天皇勅撰の最後の勅撰漢詩集で、20巻のうち現存6巻（巻1・10・11・13・14・20）に賦・詩・序・対策文・策問を収める。賦17篇・詩178首・序51篇・対策38を収録し、文選的雅文を志向した『凌雲集』『文華秀麗集』に対し、対策・策問という政治実用文を組み入れた点で独自性を持つ。",
    background="嵯峨・淳和朝の漢詩文国家形成。",
    development="勅撰漢詩集三部作（『凌雲集』『文華秀麗集』『経國集』）の最終作として位置づけられる。",
    historical_context="淳和朝の文章経国思想の集約。",
    primary_source_url=NDL+"info:ndljp/pid/2543380",
    primary_source_type="NDL: 経國集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="都氏文集と都良香",
    name_en="Toshi Bunshu and Miyako no Yoshika",
    name_original="都氏文集",
    period_key="中古",
    definition="都良香（834-879）の漢詩文集『都氏文集』6巻。詩・賦・序・記・銘・碑・賛等を収め、平安中期前半の漢詩文の精華を伝える。良香は菅原是善・道真親子の師として宮廷漢学を支え、富士山記・羅城門記等の名作を残した。文章生試で道真の試官を務め、平安漢学の系譜上重要な位置を占める。",
    background="平安中期前半の宮廷漢学の隆盛期。",
    development="菅原道真『菅家文草』への直接的影響源として位置づけられる。",
    historical_context="清和・陽成朝の漢学興隆。",
    primary_source_url=NDL+"info:ndljp/pid/2543381",
    primary_source_type="NDL: 都氏文集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="朝野群載の文学性",
    name_en="Choya Gunsai: literary aspects",
    name_original="朝野群載",
    period_key="中古",
    definition="三善為康（1049-1139）編『朝野群載』20巻は、平安期の公文書・詩文・記録を集成した類書。詔勅・宣命・奏文・申文・告文・諷詠・書状等27部立を持ち、平安期実用文学・記録文学の博物誌的集成として、文学史上の補完的価値が極めて高い。漢文公文体の様式的多様性を伝える第一級資料。",
    background="平安後期の類書編纂による知識集成熱。",
    development="近現代古文書学・公文体研究の中核資料となった。",
    historical_context="院政期の公文書様式の集大成。",
    primary_source_url=NDL+"info:ndljp/pid/2543382",
    primary_source_type="NDL: 朝野群載",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="性霊集と空海",
    name_en="Shoryoshu by Kukai",
    name_original="性霊集",
    period_key="中古",
    definition="空海（774-835）の漢詩文集『遍照発揮性霊集』10巻（弟子真済編）。詩・銘・碑・表・書状等を収め、平安初期漢詩文の頂点を成す。中国六朝・唐詩文の高度な技巧を駆使しつつ、密教思想を文学化した独自の漢文世界を展開する。「文鏡秘府論」とともに空海文学論の中核を成す。",
    background="平安初期の入唐留学僧による中国文学受容の頂点。",
    development="平安期密教文学・五山漢詩文へ深い影響を残した。",
    historical_context="嵯峨朝の文章経国思想と密教興隆の交錯。",
    primary_source_url=SAT+"satdb2015.php?mode=detail&useid=2426_,55,0001",
    primary_source_type="SAT: 性霊集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"密教詩学",
         "description":"空海性霊集は密教思想を漢詩文で表現した東アジア密教文学の頂点で、宗教哲学と詩学の融合事例として哲学史に接続する。"}])

add(**C, name_ja="文鏡秘府論の詩学",
    name_en="Bunkyo Hifuron poetics",
    name_original="文鏡秘府論",
    period_key="中古",
    definition="空海『文鏡秘府論』6巻（819頃成立）。中国六朝・初唐の詩学書（『文心雕龍』『詩品』『文選』李善注等）を引用統合し、漢詩の音律・体勢・結構・声病・対偶等を体系的に論じた東アジア最大級の詩学書。中国本土ですら散逸した諸論を伝える点で、世界文学史上の貴重な資料となる。",
    background="空海留学期の中国詩学資料の収集。",
    development="近代以降、中国佚書復元の第一級資料として中国学者にも珍重された。",
    historical_context="平安初期の入唐留学による中国文学知識の体系的移入。",
    primary_source_url=SAT+"satdb2015.php?mode=detail&useid=2438_,55,0001",
    primary_source_type="SAT: 文鏡秘府論",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"文鏡秘府論は外国詩学（中国）を体系化した古典で、AI時代の越境的詩学・多言語生成詩学の祖型として再考される。",
         "related_ai_phenomenon":"AI多言語生成と越境的詩学"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"東アジア詩学",
         "description":"文鏡秘府論は中国六朝-唐詩学を体系化した東アジア最大級の詩学書で、東アジア美学・詩学哲学の中核資料となる。"}])

add(**C, name_ja="無住『雑談集』の和漢混淆性",
    name_en="Muju's Zodanshu: Japanese-Chinese learning hybrid",
    name_original="雑談集",
    period_key="中世",
    definition="無住（1227-1312）が1305年頃に著した説話集10巻。仏法・儒教・歌道・連歌・漢学・故事等を縦横に語る博覧強記の随想体で、鎌倉末期僧侶の和漢混淆的教養世界を最も具体的に伝える資料。沙石集・聖財集とともに無住三大著作の一を成し、中世和漢比較文学研究の中核資料となる。",
    background="鎌倉末期の禅宗興隆と漢学興隆。",
    development="中世和漢比較文学・説話文学研究の中核資料となった。",
    historical_context="鎌倉末期から南北朝期の禅宗・五山文学興隆前夜。",
    primary_source_url=NIJL+"biblio/200005001/",
    primary_source_type="NIJL: 雑談集",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# C: 古今集系譜（12）  period: 中古/中世
# ============================================================
add(**C, name_ja="紀貫之と古今集仮名序",
    name_en="Ki no Tsurayuki and Kokinshu kana preface",
    name_original="古今和歌集仮名序",
    period_key="中古",
    definition="紀貫之（872?-945）が『古今和歌集』(905)に附した仮名序。「やまとうたは人の心を種としてよろづの言の葉とぞなれりける」の冒頭で著名。和歌の本質論・歌風史論・六歌仙評価を展開し、日本最初の体系的歌学書・文学論として位置づけられる。日本文学批評史の起点を成す。",
    background="醍醐朝の勅撰和歌集編纂と和歌の体系化要求。",
    development="後の歌論（俊成『古来風躰抄』、定家『近代秀歌』）の祖型となった。",
    historical_context="905年古今集成立直後。",
    primary_source_url=AOZORA+"cards/000035/files/2073_15321.html",
    primary_source_type="青空文庫: 古今和歌集仮名序",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"仮名序は仮名（女手）による文学論執筆の始原で、AI時代の非主流言語による文学批評の祖型として再考される。",
         "related_ai_phenomenon":"AI時代の言語階層と文学批評"}])

add(**C, name_ja="紀淑望と古今集真名序",
    name_en="Ki no Yoshimochi and Kokinshu mana preface",
    name_original="古今和歌集真名序",
    period_key="中古",
    definition="紀淑望（？-919）が『古今和歌集』に附した漢文序（真名序）。仮名序とほぼ同内容を漢文で展開し、漢文世界に和歌を位置づける役割を果たす。仮名序と真名序の対をなす二重序は、平安初期の和漢併存的文学観の制度的表現で、日本古典文学の和漢二重構造の象徴となる。",
    background="平安初期の和漢併存的文学制度。",
    development="近世以降、仮名序・真名序の比較研究が和漢比較文学の中核となった。",
    historical_context="醍醐朝（905）の和歌国家化。",
    primary_source_url=NDL+"info:ndljp/pid/2543400",
    primary_source_type="NDL: 古今集真名序",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="後撰和歌集と源順",
    name_en="Gosenshu and Minamoto no Shitago",
    name_original="後撰和歌集",
    period_key="中古",
    definition="第二勅撰和歌集『後撰和歌集』(951年下命、960年代成立)は村上天皇の勅命により梨壺の五人（源順・大中臣能宣・清原元輔・坂上望城・紀時文）が編纂した20巻1425首。源順（911-983）が中心的役割を果たした。古今集に対し贈答歌・物語的詞書を多く採録し、和歌物語化の傾向を強めた点に独自性を持つ。",
    background="村上朝の文化政策と梨壺学士による編纂。",
    development="後の物語的和歌集編纂（拾遺集等）の祖型となった。",
    historical_context="天暦天徳期の宮廷文化興隆。",
    primary_source_url=NDL+"info:ndljp/pid/2543401",
    primary_source_type="NDL: 後撰和歌集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="拾遺和歌集と藤原公任",
    name_en="Shuishu and Fujiwara no Kinto",
    name_original="拾遺和歌集",
    period_key="中古",
    definition="第三勅撰和歌集『拾遺和歌集』(1005-07頃成立)。花山院主導下、藤原公任（966-1041）撰の『拾遺抄』を母体に増補された20巻1351首。公任は『和漢朗詠集』『新撰髄脳』『三十六人撰』等を著した平安中期歌壇の中心で、拾遺集編纂を通じて和歌の精錬様式を確立した。",
    background="花山院・一条朝の文化的精錬期。",
    development="公任の歌論『新撰髄脳』『和歌九品』が後世歌論の基盤となった。",
    historical_context="長徳・寛弘期の宮廷文化頂点。",
    primary_source_url=NDL+"info:ndljp/pid/2543402",
    primary_source_type="NDL: 拾遺和歌集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="後拾遺和歌集と藤原通俊",
    name_en="Goshuishu and Fujiwara no Michitoshi",
    name_original="後拾遺和歌集",
    period_key="中古",
    definition="第四勅撰和歌集『後拾遺和歌集』(1086)。白河天皇勅命、藤原通俊（1047-1099）撰の20巻1218首。和泉式部・赤染衛門・相模等の女流歌人を多く採録し、平安中期女流和歌の集大成的性格を持つ。源経信『難後拾遺』による批判を受け、後の和歌議論を活性化させた点でも重要。",
    background="白河院政期の文化政策と女流歌人の評価上昇。",
    development="経信『難後拾遺』が後の歌合判詞・歌論の先駆となった。",
    historical_context="応徳期の女流文学最終局面。",
    primary_source_url=NDL+"info:ndljp/pid/2543403",
    primary_source_type="NDL: 後拾遺和歌集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="金葉和歌集と源俊頼三奏本",
    name_en="Kinyoshu and Minamoto no Toshiyori's three drafts",
    name_original="金葉和歌集",
    period_key="中古",
    definition="第五勅撰和歌集『金葉和歌集』(1124-1127)。白河院勅命で源俊頼（1055-1129）が三度上奏した点（初奏本・二度本・三奏本）で著名。最終的な三奏本が10巻665首と勅撰集中最少規模になった。俊頼の革新的歌風（題詠・新古今前史的傾向）が伝統派と衝突した編纂史を持つ。",
    background="白河院政期の和歌革新と保守の対立。",
    development="俊頼『俊頼髄脳』とともに新古今前史の理論的基盤を提供した。",
    historical_context="大治期の白河院政文化。",
    primary_source_url=NDL+"info:ndljp/pid/2543404",
    primary_source_type="NDL: 金葉和歌集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="詞花和歌集と藤原顕輔",
    name_en="Shikashu and Fujiwara no Akisuke",
    name_original="詞花和歌集",
    period_key="中古",
    definition="第六勅撰和歌集『詞花和歌集』(1151-1154)。崇徳上皇勅命で藤原顕輔（1090-1155、六条藤家祖）撰の10巻415首。顕輔の保守的選定基調により伝統的和歌様式を集約したが、勅撰集としては規模が小さく、歌史上やや影が薄い。六条藤家の家学的基盤を整えた意味では重要。",
    background="崇徳院期の伝統派和歌の集約。",
    development="六条藤家歌学の制度的基盤となった。",
    historical_context="保元の乱（1156）前夜の宮廷文化。",
    primary_source_url=NDL+"info:ndljp/pid/2543405",
    primary_source_type="NDL: 詞花和歌集",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="千載和歌集と藤原俊成",
    name_en="Senzaishu and Fujiwara no Shunzei",
    name_original="千載和歌集",
    period_key="中世",
    definition="第七勅撰和歌集『千載和歌集』(1188)。後白河院勅命で藤原俊成（1114-1204）撰の20巻1288首。俊成の幽玄理念を反映する深い情趣の和歌を多く採録し、新古今集（1205）の前駆的作品集となった。源平合戦後の戦乱期に編纂された点で、中世和歌の出発点を画する歴史的意義を持つ。",
    background="俊成の幽玄理念と御子左家歌学の確立。",
    development="新古今集編纂の直接的母体となり、俊成-定家系統の和歌理論を確立した。",
    historical_context="文治・建久期の戦乱直後の宮廷文化再構築。",
    primary_source_url=NDL+"info:ndljp/pid/2543406",
    primary_source_type="NDL: 千載和歌集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="新古今和歌集と藤原定家初撰本",
    name_en="Shinkokinshu and Teika's first compilation",
    name_original="新古今和歌集",
    period_key="中世",
    definition="第八勅撰和歌集『新古今和歌集』(1205)。後鳥羽院勅命で藤原定家・家隆・通具・有家・寂蓮・雅経の6人が編纂した20巻約2000首。新古今美学（幽玄・余情・本歌取・物語性）の頂点を成す。後鳥羽院隠岐配流（1221）後の隠岐本切継本との比較研究が現代研究の中核論題となる。",
    background="後鳥羽院期の文化政策と御子左家歌学の頂点。",
    development="八代集の頂点として近現代和歌史の中核地位を保持した。",
    historical_context="承元・建保期の後鳥羽院文化政策。",
    primary_source_url=NDL+"info:ndljp/pid/2543407",
    primary_source_type="NDL: 新古今和歌集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"新古今集の本歌取・引用詩学は既存テクスト統合による創造を理論化した古典で、AI生成における学習データ統合と新規性の関係を再考する祖型となる。",
         "related_ai_phenomenon":"AI生成における学習データ統合と新規性"}])

add(**C, name_ja="新勅撰和歌集",
    name_en="Shinchokusen Wakashu",
    name_original="新勅撰和歌集",
    period_key="中世",
    definition="第九勅撰和歌集『新勅撰和歌集』(1235)。後堀河天皇勅命で藤原定家単独撰の20巻1374首。定家晩年の保守的・平明志向への転換を反映し、新古今的華麗さを抑え雅正な様式を志向した。武家作（藤原頼経等）を多く採録した点でも、武家政権下の勅撰集の様相変化を示す重要作。",
    background="承久の乱(1221)後の朝廷文化と武家文化の交錯。",
    development="定家晩年の歌風転換を示し、京極派・二条派分裂の前史となった。",
    historical_context="嘉禎期の鎌倉幕府執権政治確立期。",
    primary_source_url=NDL+"info:ndljp/pid/2543408",
    primary_source_type="NDL: 新勅撰和歌集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="八代集論",
    name_en="Hachidaishu (Eight Imperial Anthologies) theory",
    name_original="八代集",
    period_key="中世",
    definition="『古今和歌集』(905)から『新古今和歌集』(1205)までの最初の八つの勅撰和歌集を一群として論じる枠組み。鎌倉中期に二条良基等によって体系化され、平安・鎌倉初期和歌の正典体系として確立した。八代集は和歌の伝統的枠組みの基礎を成し、近世以降の二十一代集体系の中核を担う。",
    background="鎌倉中期の和歌伝統の正典化。",
    development="近世国学（賀茂真淵・本居宣長）が八代集を和歌伝統の精華として再定位した。",
    historical_context="鎌倉中期から南北朝期の和歌伝統意識の体系化。",
    primary_source_url=NIJL+"biblio/200005010/",
    primary_source_type="NIJL: 八代集論関連歌学書",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="二十一代集体系",
    name_en="Nijuichidaishu (Twenty-one Imperial Anthologies) system",
    name_original="二十一代集",
    period_key="中世",
    definition="『古今和歌集』から『新続古今和歌集』(1439)までの21の勅撰和歌集を一群として論じる枠組み。室町期に体系化され、近世以降日本和歌正典の最大単位となった。八代集（905-1205）と十三代集（1206-1439）から成り、二条派・京極派・冷泉派等の中世和歌諸派の総合的舞台となる。",
    background="室町前期の和歌正典体系の最終形成。",
    development="近世国学・近代和歌史記述の中核枠組みとなった。",
    historical_context="室町前期の和歌伝統意識の総合化。",
    primary_source_url=NIJL+"biblio/200005011/",
    primary_source_type="NIJL: 二十一代集",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: 私家集（14）  period: 上代/中古/中世
# ============================================================
add(**C, name_ja="人麻呂集",
    name_en="Hitomaro-shu",
    name_original="柿本人麻呂集",
    period_key="上代",
    definition="柿本人麻呂に擬される歌集の総称。『萬葉集』に「人麻呂歌集」として引用される376首と、平安期成立の『人麻呂集』伝本が存在する。萬葉巻七・十・十一・十二の主要源泉となり、人麻呂単独作と人麻呂時代歌謡の両義性を持つ。日本最古の私家集（仮託集）として位置づけられる。",
    background="奈良時代の人麻呂神格化と私家集化過程。",
    development="平安・中世の人麻呂影供（神格化された歌聖崇拝）の理論的基盤となった。",
    historical_context="奈良中期から平安初期の人麻呂伝承形成。",
    primary_source_url=NIJL+"biblio/200005020/",
    primary_source_type="NIJL: 人麻呂集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="赤人集",
    name_en="Akahito-shu",
    name_original="山部赤人集",
    period_key="上代",
    definition="山部赤人に擬される歌集。萬葉集所収の赤人歌に加え、平安期に擬作・誤伝された歌を含む。三十六人集の一として伝来し、中世以降の和歌の正典的小集として継承された。萬葉時代と平安和歌の橋渡し的役割を果たし、赤人「歌聖」化過程の証拠となる。",
    background="平安初期の赤人神格化と私家集化。",
    development="三十六人集の一として中世和歌教育の中核となった。",
    historical_context="平安中期の歌聖崇拝形成期。",
    primary_source_url=NIJL+"biblio/200005021/",
    primary_source_type="NIJL: 赤人集",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="家持集",
    name_en="Yakamochi-shu",
    name_original="大伴家持集",
    period_key="上代",
    definition="大伴家持の歌を集めた私家集。『萬葉集』巻十七〜二十の家持自身の編纂部分が事実上の家持私家集を成すほか、平安期に独立した『家持集』が編集された。三十六人集の一として伝来し、家持の中世以降の正典的位置を確保する役割を果たした。",
    background="家持の萬葉編纂的私家集化と平安期再編集。",
    development="三十六人集として中世和歌教育に組み込まれた。",
    historical_context="平安中期の三十六人集形成期。",
    primary_source_url=NIJL+"biblio/200005022/",
    primary_source_type="NIJL: 家持集",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="貫之集",
    name_en="Tsurayuki-shu",
    name_original="貫之集",
    period_key="中古",
    definition="紀貫之（872?-945）の私家集。約900首を収め、自撰部分（屏風歌・贈答歌・和歌所執筆時代の作）と他撰部分から成る。古今集編纂の中心人物の私家集として、平安初期和歌の精華を直接伝える第一級資料。三十六人集の一として中世以降も和歌教育の中核となった。",
    background="平安初期和歌の中心人物の作品集成。",
    development="平安中期以降の和歌教育・歌論の中核資料となった。",
    historical_context="醍醐・朱雀朝の宮廷和歌活動。",
    primary_source_url=NIJL+"biblio/200005023/",
    primary_source_type="NIJL: 貫之集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="躬恒集",
    name_en="Mitsune-shu",
    name_original="凡河内躬恒集",
    period_key="中古",
    definition="凡河内躬恒（生没年未詳、9世紀末-10世紀前半）の私家集。約400首を収める。古今集撰者の一人で、貫之・友則・忠岑とともに古今集中核歌人を成した。平安初期和歌の様式（縁語・掛詞・序詞の精緻化）を具現する作品群を残し、三十六人集の一として伝来した。",
    background="古今集編纂期の中核歌人の作品集成。",
    development="三十六人集の一として中世和歌教育に組み込まれた。",
    historical_context="醍醐朝の古今集編纂期。",
    primary_source_url=NIJL+"biblio/200005024/",
    primary_source_type="NIJL: 躬恒集",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="業平集",
    name_en="Narihira-shu",
    name_original="在原業平集",
    period_key="中古",
    definition="在原業平（825-880）の歌を集めた私家集。『古今集』に30首、『伊勢物語』に多数収録される業平歌の集成版。三十六人集の一として伝来し、業平を「みやび」の体現者として神格化する中世以降の業平崇拝の基盤資料となった。『伊勢物語』の歌的核を成す。",
    background="平安中期以降の業平神格化と私家集化。",
    development="伊勢物語と相互参照される正典として、中世和歌教育の中核資料となった。",
    historical_context="平安中期の業平伝承形成期。",
    primary_source_url=NIJL+"biblio/200005025/",
    primary_source_type="NIJL: 業平集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="小町集",
    name_en="Komachi-shu",
    name_original="小野小町集",
    period_key="中古",
    definition="小野小町（生没年未詳、9世紀中頃）の歌を集めた私家集。古今集所収18首と他撰歌を中心に約120首を収める。三十六歌仙・六歌仙の女性代表として、中世以降の小町伝説（深草少将百夜通い・卒塔婆小町・関寺小町等）の文学的源泉となり、能・浄瑠璃・歌舞伎の小町物の中核資料となった。",
    background="平安中期の小町伝説形成と私家集化。",
    development="能（観阿弥・世阿弥『卒塔婆小町』『関寺小町』）の典拠となった。",
    historical_context="平安中期の女性歌人神格化期。",
    primary_source_url=NIJL+"biblio/200005026/",
    primary_source_type="NIJL: 小町集",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"小町集と小町伝説は美貌・才能・老醜を経る女性主体の文学的形象化で、AI時代の女性身体・年齢表象の歴史的祖型として再考される。",
         "related_ai_phenomenon":"AI時代の女性身体・年齢表象"}])

add(**C, name_ja="紫式部集",
    name_en="Murasaki Shikibu-shu",
    name_original="紫式部集",
    period_key="中古",
    definition="紫式部（970?-1019?）の自撰私家集。約128首を収める。父為時越前下向時の作・夫宣孝との贈答歌・道長家女房時代の作・寡居晩年の作等を年代順に配列し、紫式部の人生を辿る自伝的構成を持つ。源氏物語・紫式部日記とともに紫式部三大遺作の一を成す。",
    background="紫式部晩年の自撰による生涯総括。",
    development="近代以降、源氏物語・紫式部日記との相互参照で紫式部研究の中核資料となった。",
    historical_context="一条朝後半から三条朝の紫式部晩年。",
    primary_source_url=NIJL+"biblio/200005027/",
    primary_source_type="NIJL: 紫式部集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="和泉式部集",
    name_en="Izumi Shikibu-shu",
    name_original="和泉式部集",
    period_key="中古",
    definition="和泉式部（生没年未詳、970年代-1030年代）の私家集。和泉式部集（正集）約650首と続和泉式部集約650首から成る計約1300首の大著。情熱的恋愛詠と仏教的寂寥詠を併せ持ち、平安中期最大の女性歌人としての地位を確立する。和泉式部日記と相互参照される。",
    background="一条朝の女流歌人活動の頂点期。",
    development="平安中期女性和歌の頂点として近代以降高く評価された。",
    historical_context="長保・寛弘期の宮廷文化。",
    primary_source_url=NIJL+"biblio/200005028/",
    primary_source_type="NIJL: 和泉式部集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="藤原俊成『長秋詠藻』",
    name_en="Fujiwara no Shunzei, Choshu Eiso",
    name_original="長秋詠藻",
    period_key="中世",
    definition="藤原俊成（1114-1204）の自撰家集『長秋詠藻』（1178頃成立）。約400首を収め、俊成幽玄理念の具現作品集として位置づけられる。題詠・歌合作・季節歌を中心に俊成中年期までの精華を集約し、千載集編纂期の俊成歌学を直接示す第一級資料。御子左家歌学の理論的基盤を成す。",
    background="俊成幽玄理念の確立期の自撰集成。",
    development="千載集（1188）・新古今集（1205）への直接的影響源となった。",
    historical_context="治承期の御子左家歌学確立期。",
    primary_source_url=NIJL+"biblio/200005029/",
    primary_source_type="NIJL: 長秋詠藻",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="藤原定家『拾遺愚草』",
    name_en="Fujiwara no Teika, Shui Guso",
    name_original="拾遺愚草",
    period_key="中世",
    definition="藤原定家（1162-1241）の自撰家集『拾遺愚草』（最終形は1216頃）。員外を含めて約4000首を収める平安末-鎌倉前期最大の私家集。定家の生涯にわたる和歌活動を年代順に編集し、新古今集編纂期の定家歌学を直接伝える。員外（拾遺愚草員外）には定家の実験的・私的歌が多数収録される。",
    background="新古今集編纂期の定家歌学の集大成。",
    development="近世以降の定家研究・新古今研究の中核資料となった。",
    historical_context="承元・建保期の定家歌学頂点期。",
    primary_source_url=NIJL+"biblio/200005030/",
    primary_source_type="NIJL: 拾遺愚草",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"拾遺愚草の本歌取多用は既存テクスト統合の作者性を理論化した古典で、AI生成の学習元統合における作者性問題の祖型となる。",
         "related_ai_phenomenon":"AI生成における学習元統合と作者性"}])

add(**C, name_ja="西行『山家集』『聞書集』",
    name_en="Saigyo, Sanka-shu and Kikigaki-shu",
    name_original="山家集・聞書集",
    period_key="中世",
    definition="西行（1118-1190）の家集『山家集』（自撰、約1500首）と『聞書集』（他撰、約260首）。西行漂泊・隠遁生活と桜・月の自然観照を主題とする独特の歌風を集大成する。新古今集（94首採録）の最大採録歌人として、新古今美学の主要源泉となった。中世以降の漂泊文学・隠遁文学の祖型を成す。",
    background="平安末期の隠遁文化と漂泊歌人の独自スタイル。",
    development="芭蕉『おくのほそ道』を含む近世以降の漂泊文学の祖型となった。",
    historical_context="平安末期から鎌倉初期の動乱期と隠遁。",
    primary_source_url=AOZORA+"cards/000956/files/53129_56063.html",
    primary_source_type="青空文庫: 山家集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"隠遁哲学",
         "description":"西行山家集は東アジア隠遁文学・隠遁哲学の頂点を成し、世捨て・漂泊の哲学的基礎を文学化した中核資料となる。"}])

add(**C, name_ja="慈円『拾玉集』",
    name_en="Jien, Shugyokushu",
    name_original="拾玉集",
    period_key="中世",
    definition="慈円（1155-1225、九条兼実弟、天台座主）の家集『拾玉集』。約6000首の長大な家集で、平安末-鎌倉初期最大級の私家集の一。新古今集（92首採録）に多数採録され、新古今美学形成の主要源泉となった。仏教的諦観と政治的激動の双方を主題化する独特の歌風を集約する。『愚管抄』の著者でもある。",
    background="平安末期の天台仏教興隆と九条家政治。",
    development="新古今集編纂と中世仏教歌・道歌の理論的基盤を提供した。",
    historical_context="承久の乱前夜の慈円政治的活動期。",
    primary_source_url=NIJL+"biblio/200005031/",
    primary_source_type="NIJL: 拾玉集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="源実朝『金槐和歌集』",
    name_en="Minamoto no Sanetomo, Kinkai Wakashu",
    name_original="金槐和歌集",
    period_key="中世",
    definition="鎌倉幕府第3代将軍源実朝（1192-1219）の自撰家集『金槐和歌集』(1213頃)。約700首を収める。藤原定家への私淑により新古今美学を体現しつつ、武家政権首長としての独自の万葉調・骨太な歌風も併せ持つ。「ものいはぬ四方の獣すらだにもあはれなるかなや親の子を思ふ」等の名歌で著名。",
    background="鎌倉初期の武家政権と京都歌壇の交流。",
    development="近代以降、正岡子規が『歌よみに与ふる書』で実朝を再評価し、近代和歌の祖と位置づけた。",
    historical_context="建保期の実朝将軍期と暗殺(1219)直前の歌作。",
    primary_source_url=AOZORA+"cards/001134/files/45903_24094.html",
    primary_source_type="青空文庫: 金槐和歌集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"persistent",
         "rationale":"実朝金槐集は武家政権首長による文学的主体性確立を示し、AI時代の権力者主体による文学創造と作者性の関係を再考する歴史的参照点となる。",
         "related_ai_phenomenon":"AI時代の権力者主体と文学創造"}])


# ============================================================
# E: 中古日記補完（3）  period: 中古
# ============================================================
add(**C, name_ja="土佐日記原本仮名表記",
    name_en="Tosa Nikki original kana orthography",
    name_original="土佐日記",
    period_key="中古",
    definition="紀貫之『土佐日記』(935頃)の原本（藤原為家筆青谿書屋本、定家筆本等）が示す10世紀仮名表記の実態。漢字仮名交り文ではなく、純粋仮名（女手）による日記文学の最初期作で、平仮名表記体系の確立期を直接伝える文字史料。仮名遣い・濁点表記・字母選択等の研究の中核資料となる。",
    background="10世紀の仮名表記体系確立期。",
    development="池田亀鑑・小松英雄等の本文研究が現代研究の基盤を提供した。",
    historical_context="承平期の女手成熟期。",
    primary_source_url=NIJL+"biblio/200005040/",
    primary_source_type="NIJL: 土佐日記諸本",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"土佐日記の女手仮名表記は外来文字（漢字）に対するヴァナキュラ表記の確立で、AI時代の言語多様性・少数言語保存の祖型として再考される。",
         "related_ai_phenomenon":"AI時代の言語多様性と少数言語保存"}])

add(**C, name_ja="和泉式部日記の三親王恋愛",
    name_en="Izumi Shikibu Nikki: love affair with three princes",
    name_original="和泉式部日記",
    period_key="中古",
    definition="『和泉式部日記』(1004頃)が記述する和泉式部と為尊親王（999-1002没）・敦道親王（1002-1007没）兄弟との連続的恋愛、および日記成立後の藤原保昌との結婚を含む和泉式部の生涯における三人の貴族男性との関係構造。情熱的恋愛詠の文学化と、寡婦・愛人・正妻の社会的位置の交錯を文学的に構造化した稀有な作品。",
    background="一条朝の女房文化と皇族との恋愛。",
    development="近代以降、女性主体の恋愛文学の頂点として再評価された。",
    historical_context="長保・寛弘期の和泉式部の最も活発な活動期。",
    primary_source_url=AOZORA+"cards/000051/files/2074_15324.html",
    primary_source_type="青空文庫: 和泉式部日記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"古代恋愛婚姻システム",
         "description":"和泉式部日記の三親王恋愛は平安中期貴族の通い婚・複数関係システムを文学化し、人類学的家族・婚姻論の比較対象となる。"}])

add(**C, name_ja="増基法師庵日記",
    name_en="Zoki Hoshi Iori Nikki",
    name_original="増基法師庵日記",
    period_key="中古",
    definition="増基法師（10世紀末-11世紀初頭活動）が著した隠遁庵生活の日記。「いほぬし」とも呼ばれる。30余首の和歌を含み、京都北山の庵での四季の移ろい・読経・客人来訪等を記録する。隠遁日記文学の最初期作品で、中世隠遁文学（西行・長明・兼好）の祖型を提示した点で文学史的意義を持つ。",
    background="平安中期の僧侶隠遁文化興隆期。",
    development="方丈記等の中世隠遁文学への先駆的位置を占める。",
    historical_context="一条朝期の隠遁文化形成期。",
    primary_source_url=NIJL+"biblio/200005041/",
    primary_source_type="NIJL: 増基法師集",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# F: 中世紀行・連歌（10）  period: 中世
# ============================================================
add(**C, name_ja="海道記",
    name_en="Kaidoki",
    name_original="海道記",
    period_key="中世",
    definition="作者未詳（鴨長明擬作説あり）の紀行文『海道記』(1223頃)。承久の乱(1221)後、京都から鎌倉までの東海道紀行を漢文混淆体で記述する。中世紀行文学の最初期作品として、後の『東関紀行』『十六夜日記』への先駆的役割を果たした。和歌37首を含み、紀行歌の様式を確立した。",
    background="承久の乱後の京都-鎌倉間往来の活発化。",
    development="中世東海道紀行文学伝統の出発点となった。",
    historical_context="貞応期の鎌倉幕府権力確立期。",
    primary_source_url=NIJL+"biblio/200005050/",
    primary_source_type="NIJL: 海道記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="東関紀行",
    name_en="Tokan Kiko",
    name_original="東関紀行",
    period_key="中世",
    definition="作者未詳の紀行文『東関紀行』(1242頃)。京都-鎌倉間の東海道紀行を和漢混淆体で記述し、海道記の系譜を継ぐ。古典文学故事の引用・和歌詠出を多用し、紀行文学の文学的精錬を達成した。後の『十六夜日記』とともに「中世東海道紀行三部作」として位置づけられる。",
    background="鎌倉中期の京都-鎌倉間往来文化の成熟。",
    development="中世紀行文学の文学的精錬の頂点を成した。",
    historical_context="仁治期の鎌倉幕府文化的安定期。",
    primary_source_url=NIJL+"biblio/200005051/",
    primary_source_type="NIJL: 東関紀行",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="十六夜日記",
    name_en="Izayoi Nikki",
    name_original="十六夜日記",
    period_key="中世",
    definition="阿仏尼（1222?-1283）の紀行日記『十六夜日記』(1280頃)。亡夫藤原為家の遺領播磨国細川庄の領有訴訟のため、阿仏尼が京都から鎌倉へ下向する旅と訴訟経過を和歌混じりに記述する。中世女流紀行文学の代表作で、訴訟という実用的目的を文学化した点で独自性を持つ。",
    background="鎌倉幕府訴訟制度と阿仏尼の遺領訴訟。",
    development="中世女流紀行文学・訴訟文学の代表作として位置づけられる。",
    historical_context="弘安期の鎌倉幕府訴訟制度活用期。",
    primary_source_url=AOZORA+"cards/001120/files/45901_24090.html",
    primary_source_type="青空文庫: 十六夜日記",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"阿仏尼十六夜日記は女性主体による法的訴訟と文学化の交錯を示す古典で、AI時代の女性主体の制度的アクセスと文学化を再考する参照点となる。",
         "related_ai_phenomenon":"AI時代の女性主体と制度的アクセス"}])

add(**C, name_ja="都の苞",
    name_en="Miyako no Tsuto",
    name_original="都のつと",
    period_key="中世",
    definition="宗久（生没年未詳、14世紀中頃活動）の紀行文『都のつと』(1350頃)。京都から東国（鎌倉・松島）への紀行を和歌混じりに記述する。南北朝動乱期の紀行文学として、海道記・東関紀行・十六夜日記の系譜を継ぎつつ、戦乱期の紀行という独自の歴史的位置を占める。",
    background="南北朝動乱期の東西往来。",
    development="中世東国紀行文学の最終局面を示す作品となった。",
    historical_context="観応・文和期の南北朝動乱期。",
    primary_source_url=NIJL+"biblio/200005052/",
    primary_source_type="NIJL: 都のつと",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="二条良基『菟玖波集』編纂",
    name_en="Nijo Yoshimoto and the Tsukuba-shu compilation",
    name_original="菟玖波集",
    period_key="中世",
    definition="二条良基（1320-1388）が救済（きゅうぜい）と共撰した連歌集『菟玖波集』(1356)。20巻2190句を収め、北朝後光厳天皇の准勅撰の宣下を受けた連歌史上最初の権威的撰集。連歌の詩的地位を和歌と並ぶものに高め、『応安新式』(1372)とともに連歌制度確立の二大事業を成した。",
    background="南北朝期の連歌興隆と二条良基の制度化努力。",
    development="後の『新撰菟玖波集』(1495宗祇撰)への系譜を確立した。",
    historical_context="延文期の南北朝動乱期文化政策。",
    primary_source_url=NIJL+"biblio/200005053/",
    primary_source_type="NIJL: 菟玖波集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="心敬『ささめごと』十題",
    name_en="Shinkei's Sasamegoto: Ten Topics",
    name_original="ささめごと",
    period_key="中世",
    definition="心敬（1406-1475）『ささめごと』(1463-64成立)の十題構成。和歌の本質・作者の心構え・連歌作法・古今集仮名序の解釈・冷えさび論・本歌取・付合論・歌合判詞論・修行論・誹諧論等を十項目に分けて論じる中世連歌論の頂点。冷えさび美学を理論化し、後の宗祇・芭蕉に直接影響した。",
    background="室町中期の連歌論精緻化と禅的美学の浸透。",
    development="宗祇・芭蕉等の連歌・俳諧論の理論的源泉となった。",
    historical_context="応仁の乱(1467)直前の文化的精錬期。",
    primary_source_url=NIJL+"biblio/200005054/",
    primary_source_type="NIJL: ささめごと",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="宗祇『水無瀬三吟百韻』",
    name_en="Sogi: Minase Sangin Hyakuin",
    name_original="水無瀬三吟百韻",
    period_key="中世",
    definition="宗祇（1421-1502）・肖柏・宗長の三人による連歌百韻『水無瀬三吟百韻』(1488年正月22日、後鳥羽院水無瀬殿御影前で興行)。連歌史上最高傑作とされ、初句「雪ながら山もとかすむ夕かな」が著名。三吟による高度な付合・呼応・展開の理想形を実現し、室町連歌の頂点を画す。",
    background="応仁の乱後の宗祇全盛期と後鳥羽院水無瀬殿への奉納。",
    development="連歌百韻の正典として近世まで継承された。",
    historical_context="長享期の応仁の乱後復興期。",
    primary_source_url=NIJL+"biblio/200005055/",
    primary_source_type="NIJL: 水無瀬三吟百韻",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"集合的創作儀礼",
         "description":"水無瀬三吟百韻は複数主体の協働創作儀礼の文学的頂点を示し、人類学的儀礼論・集合的創造論の比較対象となる。"}])

add(**C, name_ja="宗祇『老葉』",
    name_en="Sogi: Oiha",
    name_original="老葉",
    period_key="中世",
    definition="宗祇の連歌句集『老葉』(1499)。宗祇晩年の自選句集で、約1000句を収める。連歌から独立した発句として優れた句を選定し、後の芭蕉等の発句独立化の先駆的事例となった。連歌史と俳諧史の架け橋を成す重要文献。",
    background="宗祇晩年の自選集成。",
    development="後の発句独立・俳諧形成の先駆となった。",
    historical_context="明応期の宗祇晩年期。",
    primary_source_url=NIJL+"biblio/200005056/",
    primary_source_type="NIJL: 老葉",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="荒木田守武千句",
    name_en="Arakida Moritake's Thousand Verses",
    name_original="守武千句",
    period_key="近世",
    definition="荒木田守武（1473-1549、伊勢神宮神官）の俳諧連歌『守武千句』(1540)。山崎宗鑑『犬筑波集』(1530頃)とともに俳諧連歌の二大祖を成す。連歌の高雅様式から離れ、滑稽・諧謔・卑近を意図的に導入することで、後の貞門俳諧・談林俳諧・芭蕉俳諧へと続く俳諧の出発点を画した。",
    background="室町末期の連歌様式に対する諧謔的反発。",
    development="貞門・談林・芭蕉俳諧の祖型として位置づけられた。",
    historical_context="天文期の伝統的連歌様式への内部的反動。",
    primary_source_url=NIJL+"biblio/200005057/",
    primary_source_type="NIJL: 守武千句",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="連歌之作法書",
    name_en="Renga no Saho-sho (Rules of Renga)",
    name_original="連歌之作法書",
    period_key="中世",
    definition="室町期に編纂された連歌規則集の総称。二条良基『応安新式』(1372)、心敬『ささめごと』(1463-64)、宗祇『連歌新式』(1501)等の連歌規則書群を指す。式目（詠物・付合・去嫌・序破急等）の精緻化を通じて、連歌を高度な制度的文学形式として確立した。中世連歌論の中核ジャンル。",
    background="連歌興隆期の作法・規則体系化の必要。",
    development="近世俳諧式目（『犬筑波集』『毛吹草』『俳諧御傘』）への直接的継承を成した。",
    historical_context="室町期の連歌制度確立。",
    primary_source_url=NIJL+"biblio/200005058/",
    primary_source_type="NIJL: 連歌之作法書類",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# G: 軍記補完（4）  period: 中世
# ============================================================
add(**C, name_ja="将門記",
    name_en="Shomonki",
    name_original="将門記",
    period_key="中世",
    definition="平将門の乱(935-940)を記述する漢文体軍記『将門記』(940年代成立)。日本最初の軍記物語として位置づけられ、地方武士の中央反乱とその鎮圧を記述する。漢文体で書かれ、漢籍故事を多用しつつ、東国武士の実態を伝える点で歴史的価値が高い。後の和漢混淆体軍記物語（保元・平治・平家・太平記）の祖型を成す。",
    background="承平・天慶の乱(935-941)の歴史的衝撃。",
    development="日本軍記物語伝統の出発点となった。",
    historical_context="承平天慶期の地方武士反乱の中央衝撃。",
    primary_source_url=NIJL+"biblio/200005060/",
    primary_source_type="NIJL: 将門記",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="陸奥話記",
    name_en="Mutsu Waki",
    name_original="陸奥話記",
    period_key="中世",
    definition="前九年の役(1051-1062)を記述する漢文体軍記『陸奥話記』(11世紀後半成立)。源頼義・義家による安倍貞任討伐を記述し、武家源氏の東国経略の文学的祖型となった。将門記とともに古代軍記の二大作品を成し、後の保元・平治・平家物語に至る武家文学伝統の出発点に位置する。",
    background="前九年の役による東国武家形成。",
    development="源義家を「武家の棟梁」として神話化する伝承形成の起点となった。",
    historical_context="平安後期の東国経略期。",
    primary_source_url=NIJL+"biblio/200005061/",
    primary_source_type="NIJL: 陸奥話記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="平家物語覚一本・延慶本対比",
    name_en="Heike Monogatari: Kakuichi vs Engyo manuscript comparison",
    name_original="平家物語覚一本・延慶本",
    period_key="中世",
    definition="『平家物語』の二大本文系統である覚一本（語り本系、明石覚一作1370頃）と延慶本（読み本系、延慶2年1309書写本）の本文比較研究。覚一本は琵琶法師による語りの定本として簡潔な文体を持ち、延慶本はより長大で多様な異伝・地方伝承を含む。両系統の成立過程と本文的優劣をめぐる議論は中世軍記研究の中核論題。",
    background="平家物語の口承（語り）と書承（読み物）の二重伝承。",
    development="中世軍記物語本文研究の中核論題となった。",
    historical_context="鎌倉中期から南北朝期の平家物語伝承の多様化。",
    primary_source_url=NIJL+"biblio/200005062/",
    primary_source_type="NIJL: 平家物語諸本",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"平家物語の本文系統論は集合的口承と書承の交錯による多元的作者性を示す古典で、AI時代の分散的著作・バージョン管理問題と理論的に響き合う。",
         "related_ai_phenomenon":"AI時代の分散的著作とバージョン管理"}])

add(**C, name_ja="吾妻鏡編纂",
    name_en="Azuma Kagami compilation",
    name_original="吾妻鏡",
    period_key="中世",
    definition="鎌倉幕府公式編年史『吾妻鏡』(1300頃成立)52巻。源頼朝挙兵(1180)から宗尊親王帰京(1266)までの87年間を編年体で記述する。鎌倉幕府関係者によって編纂され、北条氏正統化の歴史観を含むが、当代記録の集成として鎌倉時代史の第一級史料となる。文学性も高く、軍記物語との相互参照対象となる。",
    background="鎌倉幕府末期の幕府史記述の必要。",
    development="近世徳川家の鎌倉幕府研究・武家政権理論の中核資料となった。",
    historical_context="鎌倉幕府末期の歴史総括期。",
    primary_source_url=NIJL+"biblio/200005063/",
    primary_source_type="NIJL: 吾妻鏡",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# H: 能・狂言（8）  period: 中世
# ============================================================
add(**C, name_ja="世阿弥『風姿花伝』七篇別段",
    name_en="Zeami's Fushikaden: Seven sections detailed structure",
    name_original="風姿花伝",
    period_key="中世",
    definition="世阿弥『風姿花伝』(1400-02頃)の構造論。「年来稽古条々」「物学条々」「問答条々」「神儀云」「奥義云」「花修云」「別紙口伝」の七篇から成る。各篇は能修行の年齢別段階・物まね類型・問答形式の理論・能の起源神話・奥義論・花の本質論・口伝秘伝で構成され、能楽論の体系性を最初に確立した中核文献。",
    background="観阿弥-世阿弥の能楽実践と理論化。",
    development="能楽論の正典として中世以降継承され、近代以降の演劇理論にも影響した。",
    historical_context="室町前期の足利義満庇護下の能楽形成期。",
    primary_source_url=NIJL+"biblio/200005070/",
    primary_source_type="NIJL: 風姿花伝",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="世阿弥『花鏡』",
    name_en="Zeami's Kakyo",
    name_original="花鏡",
    period_key="中世",
    definition="世阿弥『花鏡』(1424)。風姿花伝に続く能楽論で、より成熟した世阿弥晩年の理論を示す。「序破急」「離見の見」「妙花風」等の中核概念を提示し、観客視点と演者視点の二重性、超越的演技境地論を展開した。能楽論の頂点として位置づけられる。",
    background="世阿弥晩年の理論的成熟。",
    development="近代演劇理論（ブレヒト的疎隔・俳優論）との比較対象となった。",
    historical_context="応永末期の世阿弥晩年期。",
    primary_source_url=NIJL+"biblio/200005071/",
    primary_source_type="NIJL: 花鏡",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"世阿弥「離見の見」は演者の自己客観化・観客主体内化を理論化した古典で、AI時代の自己客観化技術・自己モニタリングの祖型として再考される。",
         "related_ai_phenomenon":"AI時代の自己客観化と自己モニタリング"}])

add(**C, name_ja="世阿弥『至花道』",
    name_en="Zeami's Shikado",
    name_original="至花道",
    period_key="中世",
    definition="世阿弥『至花道』(1420)。能楽論の一書で、「二曲三体」（歌舞・物まね・老体・女体・軍体）の体系化を中心とする。能の演技類型を理論的に整理し、修行段階論を精緻化した。風姿花伝と花鏡の中間に位置する重要文献で、世阿弥能楽論の体系化過程を示す。",
    background="世阿弥能楽論の中期成熟期。",
    development="能楽演技類型論の中核資料となった。",
    historical_context="応永後期の世阿弥成熟期。",
    primary_source_url=NIJL+"biblio/200005072/",
    primary_source_type="NIJL: 至花道",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="世阿弥『三道』",
    name_en="Zeami's Sando",
    name_original="三道",
    period_key="中世",
    definition="世阿弥『三道』(1423)。能の作劇法を論じた能楽論で、「種・作・書」の三道（題材選定・作劇構成・執筆）を体系化した。能の本説（典拠）選定論、構成法（序破急の劇的展開）、詞章執筆法（古典引用・本歌取の作劇的活用）を理論化し、能の作劇論を確立した。",
    background="世阿弥の作劇実践の理論化。",
    development="能の作劇論の正典として、後の能作者（観世元雅・禅竹・信光）に継承された。",
    historical_context="応永末期の能楽作劇論成熟期。",
    primary_source_url=NIJL+"biblio/200005073/",
    primary_source_type="NIJL: 三道",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="世阿弥『拾玉得花』",
    name_en="Zeami's Shugyoku Tokka",
    name_original="拾玉得花",
    period_key="中世",
    definition="世阿弥『拾玉得花』(1428)。世阿弥晩年の能楽論で、息子観世元能への伝書として執筆された。「妙所」「闌位」「三体」等の世阿弥独自概念を集約し、修行最終段階・芸術的最高境地論を展開する。世阿弥の最後期理論として、花鏡とともに晩年理論の到達点を示す。",
    background="世阿弥晩年の伝書執筆。",
    development="世阿弥の理論的最終境地を示す資料として位置づけられる。",
    historical_context="正長期の世阿弥晩年期。",
    primary_source_url=NIJL+"biblio/200005074/",
    primary_source_type="NIJL: 拾玉得花",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="世阿弥『申楽談義』",
    name_en="Zeami's Sarugaku Dangi",
    name_original="申楽談義",
    period_key="中世",
    definition="世阿弥晩年の語りを次男観世元能が筆録した能楽談話集『申楽談義』(1430頃)。世阿弥が息子に語る能楽史・観阿弥逸話・能作者論・修行論・演技逸話等を集約する。世阿弥の他の理論書（風姿花伝・花鏡）の補足的資料として極めて価値が高く、能楽史の第一級口伝資料を成す。",
    background="世阿弥晩年の口伝伝授。",
    development="近代以降、世阿弥能楽論研究の補完資料として中核的位置を占めた。",
    historical_context="永享期の世阿弥晩年伝授期。",
    primary_source_url=NIJL+"biblio/200005075/",
    primary_source_type="NIJL: 申楽談義",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="金春禅竹『歌舞髄脳記』『六輪一露之記』",
    name_en="Komparu Zenchiku: Kabu Zuinoki and Rokurin Ichiro no Ki",
    name_original="歌舞髄脳記・六輪一露之記",
    period_key="中世",
    definition="金春禅竹（1405-1468、世阿弥女婿）の能楽論二書。『歌舞髄脳記』(1456)は能の歌舞の本質論、『六輪一露之記』(1455-56)は六つの輪と一つの露で能の修行段階を象徴的に表現した独自理論書。世阿弥能楽論を継承しつつ、和歌・天台密教・禅思想を融合した独自の象徴的理論を展開し、世阿弥以後最大の能楽理論家となった。",
    background="世阿弥の女婿として能楽論を継承し独自展開。",
    development="世阿弥-禅竹系統の能楽論として、観世系統と並ぶ理論的展開を成した。",
    historical_context="室町中期の能楽流派分化期。",
    primary_source_url=NIJL+"biblio/200005076/",
    primary_source_type="NIJL: 歌舞髄脳記・六輪一露之記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"中世象徴哲学",
         "description":"禅竹六輪一露之記は中世日本における和歌・密教・禅の融合的象徴哲学を体系化した古典で、東アジア象徴哲学史の中核資料となる。"}])

add(**C, name_ja="大蔵流狂言三百番",
    name_en="Okura School Three Hundred Kyogen Plays",
    name_original="大蔵流狂言三百番",
    period_key="中世",
    definition="狂言の最古流派大蔵流の伝統演目300番余の総称。大蔵虎明（1597-1662）筆『虎明本狂言集』(1642)が最古の網羅的台本集として知られる。脇狂言・大名狂言・小名狂言・婿狂言・女狂言・鬼狂言・山伏狂言・出家狂言・座頭狂言等の類型に分かれ、中世末-近世初期の社会階層・職業・生活を喜劇的に映す。",
    background="室町期の能楽の間狂言・本狂言の制度化と流派形成。",
    development="近世以降の落語・喜劇の祖型となり、日本喜劇文化の基盤を成した。",
    historical_context="室町末期から江戸初期の狂言制度化期。",
    primary_source_url=NIJL+"biblio/200005077/",
    primary_source_type="NIJL: 虎明本狂言集",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# I: 近世補完（11）  period: 近世
# ============================================================
add(**C, name_ja="井原西鶴『本朝二十不孝』",
    name_en="Ihara Saikaku, Honcho Nijuh Fukou",
    name_original="本朝二十不孝",
    period_key="近世",
    definition="井原西鶴（1642-1693）の浮世草子『本朝二十不孝』(1686)。中国『二十四孝』の反転として、日本各地の不孝者20話を集めた風刺的説話集。元禄前夜の都市庶民の道徳的崩壊を諧謔的に描き、儒教的孝の規範に対する町人的相対化を示す。西鶴町人物の重要作の一。",
    background="元禄前夜の儒教的道徳と町人現実の乖離。",
    development="近世風刺文学の重要先例となった。",
    historical_context="貞享期の元禄文化前夜。",
    primary_source_url=AOZORA+"cards/000206/files/4467_30706.html",
    primary_source_type="青空文庫: 本朝二十不孝",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="井原西鶴『諸艶大鑑』",
    name_en="Ihara Saikaku, Shoen Okagami",
    name_original="諸艶大鑑",
    period_key="近世",
    definition="西鶴の浮世草子『諸艶大鑑』(1684、別名『好色二代男』)。『好色一代男』(1682)の続編で、世之介の遺児世伝の遊里遍歴を描く。京都・大坂・江戸の遊里を網羅的に描写し、元禄遊里文化の集大成的記録となる。風俗誌的価値も高く、近世遊里研究の第一級資料。",
    background="元禄前夜の遊里文化興隆。",
    development="近世遊里文学・風俗誌の中核資料となった。",
    historical_context="貞享期の都市遊里文化頂点期。",
    primary_source_url=AOZORA+"cards/000206/files/4468_30707.html",
    primary_source_type="青空文庫: 諸艶大鑑",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="井原西鶴『武家義理物語』",
    name_en="Ihara Saikaku, Buke Giri Monogatari",
    name_original="武家義理物語",
    period_key="近世",
    definition="西鶴の浮世草子『武家義理物語』(1688)。武士の義理に関わる事件27話を収める武家物の代表作。武家社会の名誉・義務・忠誠の規範を町人作家の視点から相対化的に描き、武家社会の硬直性と矛盾を諧謔的に提示する。武家物として『新可笑記』とともに西鶴の重要作。",
    background="元禄期の武家規範と町人視点の対立。",
    development="近世武士道文学の相対化的視点を提示した。",
    historical_context="元禄期の武家社会硬直化期。",
    primary_source_url=AOZORA+"cards/000206/files/4469_30708.html",
    primary_source_type="青空文庫: 武家義理物語",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="井原西鶴『男色大鑑』",
    name_en="Ihara Saikaku, Nanshoku Okagami",
    name_original="男色大鑑",
    period_key="近世",
    definition="西鶴の浮世草子『男色大鑑』(1687)。武家の若衆道（武士間男色）20話と歌舞伎役者買い20話の計40話を収める日本男色文学の集大成。武家若衆道と都市役者買い文化の両面を網羅的に描き、近世日本セクシュアリティ史・LGBTQ史の第一級資料。",
    background="元禄期の若衆道文化と歌舞伎役者買いの併存。",
    development="近代以降のセクシュアリティ史研究・LGBTQ史研究の中核資料となった。",
    historical_context="貞享期の男色文化集成期。",
    primary_source_url=AOZORA+"cards/000206/files/4470_30709.html",
    primary_source_type="青空文庫: 男色大鑑",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"近世男色文化",
         "description":"男色大鑑は近世日本男色文化の文学的集成で、人類学的セクシュアリティ史・LGBTQ史研究の比較対象として中核的位置を占める。"}],
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"男色大鑑は近世日本における同性愛・両性愛の社会的肯定を文学化した古典で、AI時代のセクシュアリティ表象・多様な主体表現を再考する歴史的参照点となる。",
         "related_ai_phenomenon":"AI時代の多様なセクシュアリティ表象"}])

add(**C, name_ja="近松門左衛門『曾根崎心中』",
    name_en="Chikamatsu, Sonezaki Shinju",
    name_original="曾根崎心中",
    period_key="近世",
    definition="近松門左衛門（1653-1725）の世話浄瑠璃『曾根崎心中』(1703)。元禄16年4月7日大坂北新地遊女お初と醤油商手代徳兵衛の天神森心中事件を即時に劇化した世話浄瑠璃の祖。「この世のなごり夜もなごり」の道行が著名。世話浄瑠璃というジャンルを確立し、近世市民劇の祖型を成した。",
    background="元禄期の都市心中事件多発と即時劇化文化。",
    development="世話浄瑠璃ジャンルを創出し、後の心中物・世話物の祖型となった。",
    historical_context="元禄16年(1703)の同年事件即時劇化。",
    primary_source_url=AOZORA+"cards/000058/files/2079_15334.html",
    primary_source_type="青空文庫: 曾根崎心中",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="近松門左衛門『心中天網島』",
    name_en="Chikamatsu, Shinju Ten no Amijima",
    name_original="心中天網島",
    period_key="近世",
    definition="近松世話浄瑠璃『心中天網島』(1720)。大坂天満紙屋治兵衛と曾根崎新地遊女小春の心中を劇化する。近松世話浄瑠璃の最高傑作の一つで、義理と人情の葛藤、女房おさんの献身、心中道行の極致を描く。「心中天網島」の名は天網恢恢疎にして漏らさずの仏教的世界観を背景に持つ。",
    background="享保期の都市心中事件と近松晩年期の作劇技法成熟。",
    development="世話浄瑠璃の頂点を成し、近代以降の劇作・小説に深い影響を与えた。",
    historical_context="享保5年(1720)の同年事件即時劇化。",
    primary_source_url=AOZORA+"cards/000058/files/2080_15335.html",
    primary_source_type="青空文庫: 心中天網島",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="近松門左衛門『冥途の飛脚』",
    name_en="Chikamatsu, Meido no Hikyaku",
    name_original="冥途の飛脚",
    period_key="近世",
    definition="近松世話浄瑠璃『冥途の飛脚』(1711)。大坂飛脚屋忠兵衛が遊女梅川請出のため公金封印切に至る心中前夜の物語。「封印切」の場面が劇的頂点を成す。義理と人情の葛藤、町人の経済的破滅、心中への必然的展開を描き、近松世話浄瑠璃の中核作品の一を成す。",
    background="正徳期の都市町人経済の不安定化。",
    development="近世市民劇の中核演目として歌舞伎にも翻案され継承された。",
    historical_context="正徳1年(1711)の同年事件即時劇化。",
    primary_source_url=AOZORA+"cards/000058/files/2081_15336.html",
    primary_source_type="青空文庫: 冥途の飛脚",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="近松門左衛門『女殺油地獄』",
    name_en="Chikamatsu, Onna Goroshi Abura no Jigoku",
    name_original="女殺油地獄",
    period_key="近世",
    definition="近松世話浄瑠璃『女殺油地獄』(1721)。大坂河内屋徳兵衛の継子河内屋与兵衛が借金窮迫から豊島屋油屋お吉を殺害する事件を劇化する。近松最晩年の傑作で、油まみれの殺人場面の凄惨さは「油地獄」と称される。心中物とは異なる暴力犯罪の世話浄瑠璃化として独自の地位を占める。",
    background="享保期の都市犯罪多発化と劇化。",
    development="近代以降、谷崎潤一郎・三島由紀夫等が再評価し、近代演劇に強い影響を与えた。",
    historical_context="享保6年(1721)の同年事件即時劇化。",
    primary_source_url=AOZORA+"cards/000058/files/2082_15337.html",
    primary_source_type="青空文庫: 女殺油地獄",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="近松門左衛門『国性爺合戦』",
    name_en="Chikamatsu, Kokusenya Kassen",
    name_original="国性爺合戦",
    period_key="近世",
    definition="近松時代浄瑠璃『国性爺合戦』(1715)。明清交代期の鄭成功（和藤内）の活躍を劇化した時代浄瑠璃の最高傑作。竹本座で17ヶ月続演の大ヒットとなり、近松時代浄瑠璃の最高傑作とされる。中国を舞台にした国際的時代物として、世話浄瑠璃と並ぶ近松の二大ジャンルを完成させた。",
    background="正徳期の中国情報流入と国際的物語への関心。",
    development="近世時代浄瑠璃の頂点として、後の歌舞伎『国性爺合戦』翻案にも継承された。",
    historical_context="正徳5年(1715)の竹本座興行。",
    primary_source_url=AOZORA+"cards/000058/files/2083_15338.html",
    primary_source_type="青空文庫: 国性爺合戦",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"国性爺合戦は外国（中国）を舞台に外国主人公を主役化した稀有な日本古典劇で、AI時代の越境的物語生成・他文化主体化の祖型として再考される。",
         "related_ai_phenomenon":"AI時代の越境的物語生成"}])

add(**C, name_ja="上田秋成『春雨物語』各章",
    name_en="Ueda Akinari, Harusame Monogatari: chapter by chapter",
    name_original="春雨物語",
    period_key="近世",
    definition="上田秋成（1734-1809）晩年の物語集『春雨物語』(1808頃完成、未刊)。「血かたびら」「天津処女」「海賊」「目ひとつの神」「死首の咲顔」「捨石丸」「宮木が塚」「歌のほまれ」「樊噲」の9話（伝本により10話）を収める。雨月物語(1776)の怪異志怪性に対し、歴史的・写実的・倫理的方向への晩年的転換を示す。",
    background="秋成晩年の歴史考証学的関心と物語形式の転換。",
    development="近世物語文学の最終局面を示す重要作として位置づけられた。",
    historical_context="文化期の秋成最晩年期。",
    primary_source_url=AOZORA+"cards/000074/files/2086_15341.html",
    primary_source_type="青空文庫: 春雨物語",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="国学和歌四大人",
    name_en="Four Great Scholars of Kokugaku Waka",
    name_original="国学四大人",
    period_key="近世",
    definition="近世国学を確立した荷田春満（1669-1736）・賀茂真淵（1697-1769）・本居宣長（1730-1801）・平田篤胤（1776-1843）の四人の総称。万葉集等古典研究を通じて日本固有の精神性（古道）を主張し、和歌・古典文学解釈の革新を達成した。万葉調復興（真淵）・もののあはれ論（宣長）・古道神学（篤胤）等で和歌・古典文学解釈に画期をもたらした。",
    background="近世中後期の儒学・仏教に対する国学の興隆。",
    development="近代日本ナショナリズムと近代国文学の理論的源泉となった。",
    historical_context="享保期から天保期の国学興隆期。",
    primary_source_url=AOZORA+"cards/000200/files/4471_30710.html",
    primary_source_type="青空文庫: 国学関連著作",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"近世国学哲学",
         "description":"国学四大人は近世日本独自の言語・精神哲学を確立し、東アジア哲学史において日本固有の哲学的展開の中核を成す。"}])

add(**C, name_ja="香川景樹と桂園派",
    name_en="Kagawa Kageki and the Keien School",
    name_original="香川景樹・桂園派",
    period_key="近世",
    definition="香川景樹（1768-1843）が確立した近世後期最大の和歌流派「桂園派」。古今集の「しらべ」を重視し、賀茂真淵の万葉調・本居宣長のもののあはれ論に対し、平明な日常感受の和歌を主張した。『新学異見』(1815)で真淵を批判し、近世後期から近代和歌へと続く平易な和歌の伝統を確立。明治期の落合直文・正岡子規に至る系譜の起点となる。",
    background="近世後期の万葉調・国学派和歌に対する反動。",
    development="桂園派は明治期の和歌伝統の主要源流となった。",
    historical_context="文化文政期の和歌様式論争期。",
    primary_source_url=AOZORA+"cards/000201/files/4472_30711.html",
    primary_source_type="青空文庫: 香川景樹著作",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj in ["上代", "中古", "中世", "近世"]:
            row = db.conn.execute(
                "SELECT id FROM periods WHERE name_ja=? AND region='東アジア' LIMIT 1",
                (nj,)).fetchone()
            if row is None:
                print(f"  [error] period not found: {nj}")
                return 1
            period_ids[nj] = row[0]

        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            pkey = entry.pop("period_key", None)
            if pkey:
                entry["period_id"] = period_ids[pkey]
            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            name_to_id[entry["name_ja"]] = cid
            for ax in fourth_axes:
                try:
                    db.tag_fourth_transform(cid, **ax)
                    fourth_count += 1
                except LitDBError as e:
                    print(f"  [warn] fourth_transform tag failed for {entry['name_ja']}: {e}")
            for cd in cross_domain:
                try:
                    db.insert_cross_domain(
                        lit_entity_type="concept", lit_entity_id=cid,
                        target_db=cd["target_db"], link_type=cd["link_type"],
                        target_entity_id=cd.get("target_entity_id"),
                        target_entity_name=cd.get("target_entity_name"),
                        description=cd.get("description"))
                    cd_count += 1
                except LitDBError as e:
                    print(f"  [warn] cross_domain failed for {entry['name_ja']}: {e}")

        summary = db.progress_summary()
        print(f"[c16-w15] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c16-w15] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
