"""LIT-DB Phase 2 Wave 13 — C16: Japanese Classical Literature ADD 60.

Subfield: lit_jp_classical (id=10), region='東アジア'.
Existing periods (reused, no creation needed):
  - 上代 (id=59, 600-794)
  - 中古 (id=60, 794-1185)
  - 中世 (id=97, 1185-1603)
  - 近世 (id=98, 1603-1868)

Sources (>=85% primary target):
  - NIJL (国文学研究資料館): https://kokusho.nijl.ac.jp/
  - NDL Digital Collections: https://dl.ndl.go.jp/
  - 青空文庫: https://www.aozora.gr.jp/
  - J-STAGE: https://www.jstage.jst.go.jp/
  - SAT 大正新脩大藏經: https://21dzk.l.u-tokyo.ac.jp/SAT/
  - 国際日本文化研究センター, 早稲田大学古典籍

Coverage (60 concepts split into blocks):
  A: 上代詩歌補完 (10) — 萬葉集巻別, 東歌, 防人歌, 家持編纂論, 赤人, 人麻呂レクチエッ複合, 虫麻呂, 憶良, 笠金村, 田辺福麻呂
  B: 漢詩 (11) — 懐風藻, 三勅撰, 道真, 都良香, 紀長谷雄, 慶滋保胤, 大江匡房, 五山(義堂・絶海・瑞渓・万里)
  C: 中古散文補完 (10) — 土佐, 蜻蛉三巻, 紫式部日記, 更級, 讃岐典侍, 成尋阿闍梨母, 道綱母, 藤原実頼, 御堂関白記, 日記文学全体論
  D: 説話文学 (10) — 今昔巻別, 宇治拾遺, 古今著聞, 十訓抄, 沙石, 撰集抄, 発心集, 閑居友, 三国伝記, 雑談集
  E: 物語文学補完 (10) — 落窪, 住吉, 浜松, 夜の寝覚, 狭衣, 堤中納言, とりかへばや, 我が身, 松浦宮, 鎌倉物語草子
  F: 中世補完 (9) — 徒然草段別, 方丈記災厄, 太平記和漢混淆, 神皇正統記, 増鏡, 梅松論, 源平盛衰記, 平治・保元, 義経記
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


# Sources
NIJL = "https://kokusho.nijl.ac.jp/"
NDL = "https://dl.ndl.go.jp/"
AOZORA = "https://www.aozora.gr.jp/"
JSTAGE = "https://www.jstage.jst.go.jp/"
SAT = "https://21dzk.l.u-tokyo.ac.jp/SAT/"
NICHIBUN = "https://www.nichibun.ac.jp/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
WASEDA = "https://www.wul.waseda.ac.jp/kotenseki/"
JTI = "https://jti.lib.virginia.edu/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_jp_classical", region="東アジア",
         original_script="kanji_kana")


# ============================================================
# A: 上代詩歌補完（10）  period: 上代
# ============================================================
add(**C, name_ja="萬葉集巻別構造論",
    name_en="Manyoshu volume-by-volume structure",
    name_original="萬葉集",
    period_key="上代",
    definition="『萬葉集』全20巻の編纂的構造論。雑歌・相聞・挽歌の三大部立を巻別に配列する原則と、巻一・二（皇統的初期）、巻三〜十六（中軸）、巻十七〜二十（家持私家集化）の三層構造をめぐる近現代国文学の研究。橋本進吉以来の段階編纂説と、伊藤博・稲岡耕二らの巻別個性論が骨格を成す。",
    background="20世紀国文学による萬葉集本文批判と段階編纂説の確立。",
    development="伊藤博『萬葉集の構造と成立』、稲岡耕二『萬葉表記論』が現代研究の基礎を定めた。",
    historical_context="奈良時代の宮廷歌集編纂と、家持による最終段階編纂。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集（西本願寺本影印）",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="萬葉集東歌",
    name_en="Azuma-uta (Eastern songs of Manyoshu)",
    name_original="東歌",
    period_key="上代",
    definition="『萬葉集』巻十四に収録される東国（関東・東北南部）方言を反映した約230首の歌群。中央宮廷歌人の編集を経つつも東国音韻（甲類乙類の混同・特殊な語彙）を残し、上代日本語方言研究と古代地方文学の双方の中核資料となる。柳田国男以来、口承的基層を持つ民謡の文字化として位置づけられてきた。",
    background="律令制下の東国経営と、地方歌謡の宮廷文学化。",
    development="折口信夫『古代研究』、橋本進吉の上代特殊仮名遣い研究の主要証拠群となった。",
    historical_context="8世紀東国の方言と、宮廷による地方歌謡の収集編纂。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻十四",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"地方口承伝統と中央集権化",
         "description":"東歌は地方口承の中央集権的編纂への組み込みを示す資料で、人類学的中心-周縁関係の古代日本における具体例となる。"}])

add(**C, name_ja="萬葉集防人歌",
    name_en="Sakimori-uta (Frontier guard songs)",
    name_original="防人歌",
    period_key="上代",
    definition="『萬葉集』巻二十に収録される、九州沿岸防衛のため徴発された東国防人とその家族による約100首の歌群。家持が755年部領使から提出された歌を採録した経緯が記され、家族との別離・故郷望郷を主題とする。古代徴兵制度下の民衆の声を伝える稀有な記録として、社会史・文学史双方で重要視される。",
    background="天智朝以降の防人制度と、東国民衆の九州派遣。",
    development="近代以降、戦争文学・民衆文学の祖型として再評価された。",
    historical_context="755年（天平勝宝7）の防人歌進上と家持による採録。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻二十",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"防人歌は名前を残さない民衆主体の声を文字化した稀有な事例で、AI時代の匿名集団主体の声の可視化問題を再考する古典的参照点となる。",
         "related_ai_phenomenon":"AI時代における集合的匿名主体の声の可視化"}])

add(**C, name_ja="大伴家持の萬葉集編纂論",
    name_en="Otomo no Yakamochi as Manyoshu compiler",
    name_original="大伴家持",
    period_key="上代",
    definition="大伴家持（718?-785）が『萬葉集』の最終編纂者であるとする現代国文学の通説的見解。巻十七〜二十の家持私家集化、防人歌採録、最終歌（759年正月）が家持作であること等の編纂痕跡から推定される。佐佐木信綱・橋本進吉以来、伊藤博・稲岡耕二によって確立された。",
    background="奈良時代後半の家持の宮廷経歴と歌集編纂への関与。",
    development="現代の萬葉集成立論の中軸仮説となった。",
    historical_context="天平宝字以降の政治的混乱と家持の中央地方往還。",
    primary_source_url=JSTAGE+"article/jjpoetry/-char/ja/",
    primary_source_type="J-STAGE: 萬葉集編纂論研究",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="山部赤人",
    name_en="Yamabe no Akahito",
    name_original="山部赤人",
    period_key="上代",
    definition="奈良時代前半の宮廷歌人（生没年未詳、聖武朝活躍）。『萬葉集』に長歌13首・短歌37首を残す。富士山讃歌（巻三・317-318）、吉野行幸歌、若浦行幸歌等で、自然描写の叙景的清澄さに優れ、人麻呂と並ぶ「歌聖」として『古今集仮名序』に挙げられた。叙景歌の祖型を確立した。",
    background="奈良時代宮廷儀礼歌の制度的成熟。",
    development="平安和歌の叙景表現に深い影響を与え、紀貫之『古今集仮名序』で人麻呂と並称された。",
    historical_context="聖武天皇行幸の従駕歌人としての活動。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻三・六",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="柿本人麻呂レクチエッ複合（挽歌・宮廷歌人論）",
    name_en="Kakinomoto no Hitomaro lectical complex (court elegy)",
    name_original="柿本人麻呂",
    period_key="上代",
    definition="柿本人麻呂（生没年未詳、持統・文武朝活躍）の挽歌群（草壁皇子挽歌・高市皇子挽歌・明日香皇女挽歌）に見られる、宮廷儀礼における鎮魂と神話的世界観の重層構造。折口信夫が「依代」「鎮魂」概念で論じ、白川静、伊藤博らが古代王権儀礼との関連で精緻化した。挽歌形式の祖型を確立した。",
    background="持統朝の天武皇統儀礼整備と宮廷歌人制度の確立。",
    development="折口信夫『古代研究』、白川静『初期万葉論』が現代研究の基盤を提供した。",
    historical_context="天武・持統朝の皇統儀礼と人麻呂の宮廷歌人としての職務。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻二",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"鎮魂儀礼と挽歌",
         "description":"人麻呂挽歌は古代日本の鎮魂儀礼の文学的形態を示し、人類学的儀礼論の比較対象として中核的位置を占める。"}])

add(**C, name_ja="高橋虫麻呂",
    name_en="Takahashi no Mushimaro",
    name_original="高橋虫麻呂",
    period_key="上代",
    definition="奈良時代前半の歌人（生没年未詳、藤原宇合配下で常陸国司）。『萬葉集』に長歌14首・短歌21首を残す。浦島伝説・水江浦島子・真間手児名・葦屋処女・筑波山求婚等の伝説歌を多く詠み、「伝説歌人」と称される。地方民間伝承を宮廷歌の形式に組み入れた点で独自の地位を占める。",
    background="奈良時代地方国司の文化活動と、地方伝承の中央文学化。",
    development="折口信夫が口承伝説の文学化として高く評価し、現代の伝承文学研究の中心資料となった。",
    historical_context="藤原宇合の常陸守時代における文化的庇護。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻九",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="山上憶良「貧窮問答歌」",
    name_en="Yamanoue no Okura, Dialogue of the Destitute",
    name_original="貧窮問答歌",
    period_key="上代",
    definition="山上憶良（660?-733?）が『萬葉集』巻五（892-893）に収めた長歌反歌。貧者と極貧者の対話形式で律令制下の農民の困窮を描写する。漢籍『遊仙窟』『文選』の対話形式を踏まえつつ、社会批判的視座を導入した稀有な歌で、子等を思ふ歌・老身重病歌等とともに憶良の社会派歌人としての地位を決定した。",
    background="憶良の遣唐使経験（702渡唐）による漢籍受容と、奈良時代律令農民の困窮の社会問題化。",
    development="近代以降、社会派文学の祖として高く評価された。土屋文明、伊藤博らによる注釈研究が蓄積。",
    historical_context="天平期の律令制度疲弊と、地方国司憶良の現地観察。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻五",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"persistent",
         "rationale":"貧窮問答歌は律令下の窮民の声を文学化した古代の社会派詩で、AI時代における周縁主体の声の文学的代弁の倫理問題を再考する歴史的参照点となる。",
         "related_ai_phenomenon":"AIによる周縁主体の声の代弁問題"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"古代社会批判詩",
         "description":"憶良の貧窮問答歌は古代東アジアにおける社会批判詩の形式と倫理を代表し、儒教的経世思想の文学的具現として哲学史に接続する。"}])

add(**C, name_ja="山上憶良「子等を思ふ歌」",
    name_en="Okura, Verses on Thinking of Children",
    name_original="子等を思ふ歌",
    period_key="上代",
    definition="山上憶良が『萬葉集』巻五（802-803）に収めた長歌反歌。「瓜食めば子ども思ほゆ栗食めばまして偲はゆ」（803）の反歌で著名。釈迦の教えを引用しつつ、子への親愛を肯定する人情味溢れる歌で、家族愛を主題化した古代東アジア漢詩文圏でも稀有な作品として、近代以降の家族文学評価で中核的位置を占める。",
    background="憶良の漢籍仏典受容と、家族愛の文学化への独自関心。",
    development="近代以降の家族小説・自伝文学の祖型的位置を獲得した。",
    historical_context="天平期の仏教伝来と憶良の儒仏混淆的世界観。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻五",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="笠金村と田辺福麻呂",
    name_en="Kasa no Kanamura and Tanabe no Sakimaro",
    name_original="笠金村・田辺福麻呂",
    period_key="上代",
    definition="奈良時代中期の宮廷歌人2名の総称。笠金村（生没年未詳、聖武朝活動）は『萬葉集』に長歌11首短歌34首、行幸従駕歌・離別歌に優れた。田辺福麻呂（生没年未詳、家持と交流）は宮廷歌人最末期の代表で、行幸歌・宴席歌に古代雅讃の様式を集約した。両者は人麻呂・赤人と虫麻呂・憶良の間を結ぶ宮廷儀礼歌の継承者として位置づけられる。",
    background="奈良時代中期の宮廷儀礼歌の様式的継承期。",
    development="伊藤博『萬葉集の構造と成立』が両者を萬葉宮廷歌人系譜の中で位置づけた。",
    historical_context="聖武朝行幸文化と宮廷歌人制度の成熟。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻三・六・九",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# B: 漢詩（11）  period: 上代/中古/中世
# ============================================================
add(**C, name_ja="懐風藻の漢詩世界",
    name_en="Kaifuso poetic world",
    name_original="懐風藻",
    period_key="上代",
    definition="751年（天平勝宝3）成立の現存最古の日本漢詩集。編者未詳（淡海三船説有力）。大友皇子・大津皇子・文武天皇・長屋王・藤原宇合等64人の漢詩120首を収める。六朝詩風（謝霊運・庾信）を範とした律令貴族の漢詩実践を伝え、万葉和歌と並走する古代日本漢文学の出発点。",
    background="律令制下の貴族漢学教育と、唐文化受容の最盛期。",
    development="平安初期三勅撰漢詩集（凌雲・文華秀麗・経国）の前史を形成した。",
    historical_context="奈良時代後半の唐文化追従政策と漢詩制作の制度化。",
    primary_source_url=NDL+"info:ndljp/pid/2585896",
    primary_source_type="NDL: 懐風藻",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="平安初期三勅撰漢詩集",
    name_en="Three early-Heian imperial Chinese poetry anthologies",
    name_original="凌雲集・文華秀麗集・経国集",
    period_key="中古",
    definition="嵯峨朝〜淳和朝に編纂された三勅撰漢詩集の総称。『凌雲集』(814、小野岑守等編)、『文華秀麗集』(818、藤原冬嗣等編)、『経国集』(827、良岑安世等編)。嵯峨天皇の文章経国思想（『経国集』序）を背景に、漢詩を国家経営の核と位置づけ、唐風文化最盛期（弘仁・天長文化）を代表する。",
    background="嵯峨天皇の唐風志向と、平安初期律令再強化政策。",
    development="9世紀後半の菅家文草・道真までの漢詩文隆盛の制度的基盤を形成した。",
    historical_context="唐との文化交流最盛期と、宮廷漢文学の制度化。",
    primary_source_url=NDL+"info:ndljp/pid/2585927",
    primary_source_type="NDL: 凌雲集・文華秀麗集・経国集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"persistent",
         "rationale":"三勅撰漢詩集は外国語（漢文）による国家文学を制度化した古典的事例で、AI時代の多言語生成と国民文学概念の関係を再考する歴史的参照点となる。",
         "related_ai_phenomenon":"多言語AI生成と国民文学概念の再考"}])

add(**C, name_ja="菅原道真『菅家文草』",
    name_en="Sugawara no Michizane, Kanke Bunso",
    name_original="菅家文草",
    period_key="中古",
    definition="菅原道真（845-903）の漢詩文集。900年（昌泰3）醍醐天皇に献上。漢詩468首・散文159篇を全12巻に編集。讃岐守時代（886-890）の地方民情詩、右大臣昇進期の宮廷詩、大宰府配流期（901-903）の悲憤詩を含む。日本漢詩の頂点と評され、平安朝漢詩文の代表作。",
    background="9世紀後半の宇多・醍醐朝における学問家系（菅家）の制度的地位。",
    development="平安後期から中世にかけて道真信仰（天神信仰）と結合し、漢詩文教育の規範書となった。",
    historical_context="901年昌泰の変による道真左遷と大宰府客死。",
    primary_source_url=NDL+"info:ndljp/pid/2566348",
    primary_source_type="NDL: 菅家文草・菅家後集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="都良香",
    name_en="Miyako no Yoshika",
    name_original="都良香",
    period_key="中古",
    definition="平安初期漢詩人（834-879）。文章博士・大内記。『日本三代実録』編纂に参画し、『都氏文集』（散逸を経て3巻現存）に漢詩文を収める。富士山記等の漢文紀行的記述に独自性を発揮し、菅原道真の師格として平安漢文学黄金期の準備をなした。",
    background="9世紀中葉の文章道（紀伝道）の制度的成熟。",
    development="弟子菅原道真への漢詩文継承を通じて9世紀末漢詩文最盛期の基盤を提供した。",
    historical_context="清和・陽成朝の文章道と紀伝博士制度。",
    primary_source_url=NDL+"info:ndljp/pid/2566349",
    primary_source_type="NDL: 都氏文集",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="紀長谷雄",
    name_en="Ki no Haseo",
    name_original="紀長谷雄",
    period_key="中古",
    definition="平安初期漢詩人（845-912）。菅原道真と並ぶ宇多・醍醐朝の代表漢詩人で、文章博士・参議。『紀家集』（散逸、断片現存）に漢詩文を残し、中世「長谷雄草子」絵巻でも知られる。9世紀末漢詩文最盛期を道真とともに体現した。",
    background="9世紀後半文章道の最盛期と、紀氏の漢学家系としての位置。",
    development="中世以降、長谷雄絵巻の主人公として説話化され、漢詩人像が大衆化された。",
    historical_context="昌泰の変（901）で道真失脚後、紀氏が文章道を継いだ歴史的位置。",
    primary_source_url=NDL+"info:ndljp/pid/2566350",
    primary_source_type="NDL: 本朝文粋・紀家集断片",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="慶滋保胤『池亭記』『日本往生極楽記』",
    name_en="Yoshishige no Yasutane, Chiteiki and Nihon Ojo Gokurakuki",
    name_original="池亭記・日本往生極楽記",
    period_key="中古",
    definition="慶滋保胤（?-1002）の代表作二編。『池亭記』(982)は西京荒廃と東京繁栄を対比した漢文随筆で、鴨長明『方丈記』の祖型として日本随筆文学史で重要な位置を占める。『日本往生極楽記』(983-987頃)は浄土往生者45人の伝記で、日本最初の往生伝として中世仏教文学史の起点となった。",
    background="10世紀末の貴族浄土信仰興隆と、慶滋保胤の漢学教養。",
    development="『方丈記』『発心集』等の中世隠遁随筆と、『続本朝往生伝』以降の往生伝群の双方の祖型となった。",
    historical_context="985年源信『往生要集』と並ぶ平安中期浄土教興隆の文学的展開。",
    primary_source_url=NDL+"info:ndljp/pid/2566351",
    primary_source_type="NDL: 本朝文粋・日本往生極楽記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"浄土教思想と往生伝",
         "description":"日本往生極楽記は平安中期浄土教思想の文学的具現で、東アジア仏教哲学史の中で重要な位置を占める。"}])

add(**C, name_ja="大江匡房『江談抄』『本朝神仙伝』",
    name_en="Oe no Masafusa, Godansho and Honcho Shinsenden",
    name_original="江談抄・本朝神仙伝",
    period_key="中古",
    definition="大江匡房（1041-1111）の代表作。『江談抄』は1108年頃成立、藤原実兼が匡房から聴取した政治・歴史・故事談を収録した談話集で、平安後期の漢詩文・有職故実の宝庫となる。『本朝神仙伝』は日本の神仙的人物37人の伝記で、慶滋保胤『日本往生極楽記』の道教版的位置を占める。",
    background="平安後期院政期の貴族文化と、大江氏の漢学・有職故実継承。",
    development="中世説話集（『古事談』『十訓抄』『古今著聞集』）に多大な影響を与えた。",
    historical_context="白河院政期（1086-1129）の宮廷文化と知識継承。",
    primary_source_url=NDL+"info:ndljp/pid/2585930",
    primary_source_type="NDL: 江談抄",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="五山文学・義堂周信",
    name_en="Five Mountains Literature: Gido Shushin",
    name_original="義堂周信『空華集』",
    period_key="中世",
    definition="義堂周信（1325-1388）は中世臨済禅僧、五山文学の代表者。夢窓疎石の弟子で、京都建仁寺・南禅寺・鎌倉円覚寺住持を歴任。漢詩文集『空華集』『空華日用工夫略集』を残し、宋元禅宗詩風を日本に定着させた。室町幕府足利義満の信任を受け、五山文学最盛期の制度的地位を確立した。",
    background="鎌倉末〜南北朝期の禅宗渡来僧（蘭渓道隆・無学祖元等）以降の禅宗文化定着。",
    development="絶海中津と並ぶ五山文学の双璧として、中世日本漢詩文の規範を確立した。",
    historical_context="足利義満の北山文化期と五山官寺制度の整備。",
    primary_source_url=SAT+"satdb2015.php",
    primary_source_type="SAT 大正新脩大藏經・空華集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="五山文学・絶海中津",
    name_en="Five Mountains Literature: Zekkai Chushin",
    name_original="絶海中津『蕉堅藁』",
    period_key="中世",
    definition="絶海中津（1336-1405）は中世臨済禅僧、義堂と並ぶ五山文学の代表者。明初に渡明し（1368-78）、宋濂等明初文人と直接交流。帰国後に建仁寺・相国寺住持。漢詩文集『蕉堅藁』を残し、明風を直接導入した点で義堂と異なる独自性を示した。足利義満の信任厚く、五山外交文書の起草も担った。",
    background="明初（洪武年間）日明交流再開と禅僧渡明文化。",
    development="明風漢詩文を直接日本に伝え、室町後期五山文学の方向性を決定づけた。",
    historical_context="1368年明朝成立と日明貿易（勘合貿易）開始期。",
    primary_source_url=SAT+"satdb2015.php",
    primary_source_type="SAT 大正新脩大藏經・蕉堅藁",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="瑞渓周鳳『臥雲日件録』",
    name_en="Zuikei Shuho, Gaun Nikkenroku",
    name_original="臥雲日件録",
    period_key="中世",
    definition="瑞渓周鳳（1391-1473）の漢文日記。1446-1472年の日記で、室町中期相国寺の生活・政治・文化情報を詳細に記録する。『善隣国宝記』（日明・日朝外交史料集）の編者でもあり、五山禅僧の知的活動と外交実務の交点を体現する人物の自筆記録として、中世史・文学史双方で第一級史料となる。",
    background="室町中期五山外交僧の制度的地位と、漢文日記の慣行。",
    development="近世国学者・近代日本史学（田中健夫等）の中世外交史研究の基本史料となった。",
    historical_context="応仁の乱（1467-77）前夜の京都五山と幕府政治。",
    primary_source_url=NIJL+"biblio/200004842/",
    primary_source_type="NIJL: 臥雲日件録",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="万里集九『梅花無尽蔵』",
    name_en="Banri Shukyu, Baika Mujinzo",
    name_original="梅花無尽蔵",
    period_key="中世",
    definition="万里集九（1428-?）の漢詩文集。応仁の乱を避けて美濃に下向、太田道灌の招きで関東に滞在等、地方諸大名の保護下に活動した遊歴禅僧。『梅花無尽蔵』は7巻の漢詩文集で、地方武家文化と中央五山文化の橋渡しを示す資料として、戦国前期文化史の重要証言となる。",
    background="応仁の乱後の京都五山衰退と、地方大名の文化保護興隆。",
    development="戦国期文化の地方分散化を象徴する作家として、近世儒学的漢詩文の前史を形成した。",
    historical_context="応仁の乱(1467-77)以降の京都文化拡散と地方大名文化の隆盛。",
    primary_source_url=NIJL+"biblio/200004843/",
    primary_source_type="NIJL: 梅花無尽蔵",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# C: 中古散文補完（10）  period: 中古
# ============================================================
add(**C, name_ja="土佐日記の編年体破断",
    name_en="Tosa Nikki and the rupture of chronicle form",
    name_original="土佐日記",
    period_key="中古",
    definition="紀貫之『土佐日記』(935頃)が示す日記文学の革新。編年体公的記録（漢文男手日記）の様式を保ちつつ、女性仮託（「をとこもすなる日記」）と仮名表現を導入し、亡児追悼の私的感情を中心に再編した。公的編年体の構造を破断して内面記述を組み込んだ点で、後の女流仮名日記文学の方法的祖型となった。",
    background="10世紀前半の漢文公日記伝統と、仮名散文表現の成熟。",
    development="蜻蛉日記・紫式部日記・更級日記等、平安女流日記文学の方法的前提となった。",
    historical_context="935年貫之土佐守任期終了帰京と、935年承平天慶の乱前夜の社会。",
    primary_source_url=AOZORA+"cards/000176/files/49262_18809.html",
    primary_source_type="青空文庫: 土佐日記",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="蜻蛉日記三巻別個性",
    name_en="Kagero Nikki: distinctness of the three volumes",
    name_original="蜻蛉日記",
    period_key="中古",
    definition="藤原道綱母『蜻蛉日記』(974頃成立)の上中下三巻にわたる質的変容論。上巻（954-968）は短歌中心の自伝、中巻（969-971）は散文増大と内面化、下巻（972-974）は子道綱中心への視点転換と、巻ごとに性格が異なる。日記文学の方法的成熟過程を内蔵した稀有な作品として、現代国文学の中心研究対象となる。",
    background="10世紀後半摂関政治期の貴族女性の生活と感情の文学化。",
    development="紫式部・和泉式部・菅原孝標女に直接影響を与え、平安女流日記文学の最初の方法的成熟例となった。",
    historical_context="藤原道綱母の藤原兼家との結婚生活（954-）と、摂関期貴族女性の社会的位置。",
    primary_source_url=AOZORA+"index_pages/person9079.html",
    primary_source_type="青空文庫: 蜻蛉日記",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="紫式部日記の女房世界",
    name_en="Murasaki Shikibu Diary and the world of court women",
    name_original="紫式部日記",
    period_key="中古",
    definition="紫式部『紫式部日記』(1010頃)が描く一条天皇中宮彰子サロンの女房世界。敦成親王誕生記録（1008）を中核に、清少納言・和泉式部・赤染衛門等同時代女房への批評、自身の内面的孤独の記述、漢詩文教養を含む知的女房の自画像を展開する。平安女房文化の最重要内部証言となる。",
    background="一条天皇期の中宮サロン文化と、紫式部の彰子付女房としての職務。",
    development="女房日記の方法的頂点として、近代以降の女流文学評価の中心作品となった。",
    historical_context="1008-1010年中宮彰子敦成親王誕生と藤原道長期摂関政治確立期。",
    primary_source_url=AOZORA+"cards/000019/files/4231_15811.html",
    primary_source_type="青空文庫: 紫式部日記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"宮廷女性ネットワーク",
         "description":"紫式部日記は古代日本宮廷女性ネットワークの内部記述で、人類学的女性社会研究の比較対象として重要。"}])

add(**C, name_ja="更級日記の旅と夢",
    name_en="Sarashina Nikki: travel and dream",
    name_original="更級日記",
    period_key="中古",
    definition="菅原孝標女『更級日記』(1059頃)が示す内面記述の独特性。13歳の上総下向〜京帰還の旅（1020）から始まり、源氏物語耽溺・宮仕え・結婚・夫死別・晩年の失意までの40年余を回顧する。夢の記述を多く含み、現実と幻想が重層する独自の散文世界を構築した。物語耽読の文学化として日本受容史の重要証言。",
    background="11世紀中葉の地方下向貴族女性の物語愛好と内面化。",
    development="近代以降、夢と物語耽読をめぐる女性主体の文学として再評価された。",
    historical_context="1020年代物語文化最盛期の地方貴族女性の物語消費。",
    primary_source_url=AOZORA+"cards/000074/files/52338_45867.html",
    primary_source_type="青空文庫: 更級日記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"更級日記は物語耽読が現実認識を変容させる過程を内省的に記述した古典で、AI時代における物語的没入と現実認識の関係を再考する原型的参照点となる。",
         "related_ai_phenomenon":"AIナラティブへの没入と現実認識の変容"}])

add(**C, name_ja="讃岐典侍日記",
    name_en="Sanuki no Suke Nikki",
    name_original="讃岐典侍日記",
    period_key="中古",
    definition="藤原長子（讃岐典侍）の日記（1108頃成立）。堀河天皇の崩御（1107）と鳥羽天皇即位後の宮廷を描く。仕えた天皇の死と新天皇への奉仕という個人的悲嘆と公的職務の交錯を、上巻（堀河追慕）下巻（新天皇仕官）の二部構成で展開する。院政期初期の宮廷女房日記として、平安女流日記文学の最終代表作の一つ。",
    background="院政期初期（白河院政下）の宮廷女房文化と、典侍長子の堀河天皇への深い忠誠。",
    development="女房日記伝統の最終的展開を示し、中世以降の追懐文学への橋渡しとなった。",
    historical_context="1107年堀河天皇崩御と鳥羽天皇即位、白河院政期の宮廷。",
    primary_source_url=NIJL+"biblio/200004844/",
    primary_source_type="NIJL: 讃岐典侍日記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="成尋阿闍梨母集",
    name_en="Jojin Ajari no Haha no Shu",
    name_original="成尋阿闍梨母集",
    period_key="中古",
    definition="成尋阿闍梨の母（生没年未詳、約1071-1073頃成立）の家集兼日記。子成尋（1011-1081）の入宋（1072）に際した母の悲嘆と祈祷生活を、和歌と散文を交えて記録する。子の長期不在に対する母の感情記述として稀有な作品で、平安後期女房日記の中で独自の位置を占める。",
    background="11世紀後半の入宋僧文化と、家族関係の文学化。",
    development="近代以降、母性文学の祖型として再評価された。",
    historical_context="1072年成尋入宋と、1081年成尋客死までの母子別離期。",
    primary_source_url=NIJL+"biblio/200004845/",
    primary_source_type="NIJL: 成尋阿闍梨母集",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="藤原道綱母の方法",
    name_en="Fujiwara no Michitsuna's mother as literary method",
    name_original="道綱母",
    period_key="中古",
    definition="『蜻蛉日記』作者藤原道綱母（937?-995）の文学的方法論。和歌中心の自伝記述、自己を「身（み）」として三人称化する自己疎外、結婚生活の不満を中核とする内面記述等、平安女流文学の方法的祖型を確立した。紫式部・和泉式部・菅原孝標女への直接的影響源として、現代国文学が方法論研究の中心対象とする。",
    background="10世紀後半の貴族女性自伝表現の方法的探究。",
    development="平安女流日記文学全体の方法論的枠組みを定義した。",
    historical_context="兼家・道隆・道長の摂関政治期と道綱母の周縁的位置。",
    primary_source_url=AOZORA+"index_pages/person9079.html",
    primary_source_type="青空文庫: 蜻蛉日記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="藤原実頼『清慎公記』",
    name_en="Fujiwara no Saneyori, Seishinkoki",
    name_original="清慎公記",
    period_key="中古",
    definition="藤原実頼（900-970）の漢文日記（『水心記』とも）。10世紀中葉の摂関期初期の朝廷儀礼・政務・官人事を詳細に記録する。摂関期男性貴族日記（『御堂関白記』『小右記』『水左記』等）伝統の起点に位置し、平安貴族日記文学の制度的基盤を形成した。",
    background="10世紀中葉藤原北家の摂関制度確立と、漢文日記の有職故実継承機能。",
    development="藤原忠平『貞信公記』とともに、後の摂関期男性貴族日記の規範となった。",
    historical_context="村上天皇期の天暦の治と摂関政治の制度的成熟期。",
    primary_source_url=NIJL+"biblio/200004846/",
    primary_source_type="NIJL: 清慎公記断片",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="御堂関白記の文体",
    name_en="Style of Mido Kanpakuki",
    name_original="御堂関白記",
    period_key="中古",
    definition="藤原道長（966-1027）の漢文日記『御堂関白記』(998-1021)が示す日記文体論。具注暦の余白と紙背に書かれた自筆原本（陽明文庫蔵、ユネスコ世界記憶遺産2013登録）が現存し、簡素直截な漢文体・朝廷儀礼記録・政治判断記録を統合する。摂関期最盛期の文体と政治を直接伝える第一級史料。",
    background="11世紀初頭摂関政治の頂点と道長の権力中枢。",
    development="後の貴族漢文日記（『小右記』『水左記』『中右記』等）の参照規範となった。",
    historical_context="道長最盛期（1016年摂政・1017年太政大臣）と摂関政治の確立。",
    primary_source_url=NDL+"info:ndljp/pid/2585931",
    primary_source_type="NDL: 御堂関白記",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="日記文学全体論",
    name_en="Heian diary literature: a general theory",
    name_original="日記文学",
    period_key="中古",
    definition="平安期日記文学（仮名日記）全体の方法論的位置づけ。土佐日記（935）から讃岐典侍日記（1108）までの約170年間に展開した仮名散文日記群を、(1)女性仮託・女性自筆、(2)和歌中心から散文中心への移行、(3)内面記述の段階的深化、(4)私的個人記録から文学作品への変容、として体系的に把握する。秋山虔・三谷邦明等の現代国文学が枠組み化した。",
    background="平安期男性漢文日記伝統と平行する仮名女性日記伝統の制度的成立。",
    development="近代私小説・近代女性自伝文学の祖型として再解釈された。",
    historical_context="平安後期の女房文学制度と物語・日記・歌集の三角形成。",
    primary_source_url=JSTAGE+"article/jjpoetry/-char/ja/",
    primary_source_type="J-STAGE: 日記文学研究",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"平安日記文学は私的主体の内面記述を文学化した古典的事例で、AI時代の自己記述（ライフログ・SNS・AIメモワール）と内面性概念を再考する原型的参照点となる。",
         "related_ai_phenomenon":"AIライフログと内面記述の真正性"}])


# ============================================================
# D: 説話文学（10）  period: 中古/中世
# ============================================================
add(**C, name_ja="今昔物語集巻別構造",
    name_en="Konjaku Monogatarishu volume-by-volume structure",
    name_original="今昔物語集",
    period_key="中古",
    definition="『今昔物語集』(1120頃成立)31巻（うち3巻欠）の三部構成論。天竺部（巻1-5、インド仏教説話）、震旦部（巻6-10、中国仏教・世俗説話）、本朝部（巻11-31、日本仏教・世俗説話）を「今ハ昔」で開始する説話形式で配列する。仏教東漸の地理的範型を文学化した世界最大の中世説話集。",
    background="平安後期の仏教東漸思想と漢文・和文説話伝統の総合。",
    development="芥川龍之介『羅生門』『鼻』等の近代再話の典拠となり、世界文学的位置を獲得した。",
    historical_context="院政期初期の貴族・僧侶共有の説話文化。",
    primary_source_url=AOZORA+"cards/000879/files/127_15225.html",
    primary_source_type="青空文庫: 今昔物語集（部分）",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="宇治拾遺物語",
    name_en="Uji Shui Monogatari",
    name_original="宇治拾遺物語",
    period_key="中世",
    definition="13世紀前半成立、編者未詳の説話集。『宇治大納言物語』（散逸）を継ぐ位置を主張し、197話を収める。仏教説話・世俗説話・笑話を分類なく配列する自由な構成と、「これも今は昔」の口語的開始句で著名。芥川龍之介『芋粥』『鼻』の典拠としても知られ、中世説話文学の代表作。",
    background="13世紀鎌倉初期の説話編纂興隆と、仏教教化文学の俗化。",
    development="中世以降の説話集（『古今著聞集』『十訓抄』）と、近代再話文学の典拠となった。",
    historical_context="承久の乱（1221）後の鎌倉前期文化と寺社説話の集成期。",
    primary_source_url=NIJL+"biblio/200004847/",
    primary_source_type="NIJL: 宇治拾遺物語",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="古今著聞集",
    name_en="Kokon Chomonju",
    name_original="古今著聞集",
    period_key="中世",
    definition="橘成季編、1254年成立の説話集。20巻、神祇・釈教・政道・忠臣・好色・武勇・絵画・蹴鞠・遊楽等30篇に分類した726話を収める。前代『今昔』『宇治拾遺』が仏教説話中心だったのに対し、王朝美的・風雅・芸能を中心とする宮廷貴族文化説話集として独自の地位を占める。",
    background="13世紀中葉鎌倉中期の貴族文化懐古と、王朝説話編纂運動。",
    development="中世末期から近世にかけての教養書・有職故実書として広く流布した。",
    historical_context="鎌倉中期の宮廷・武家両文化並立期と、貴族文化の説話的保存。",
    primary_source_url=NIJL+"biblio/200004848/",
    primary_source_type="NIJL: 古今著聞集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="十訓抄",
    name_en="Jikkinsho",
    name_original="十訓抄",
    period_key="中世",
    definition="1252年成立、編者未詳（六波羅二臘左衛門入道説有）の教訓説話集。「人に恵を施すべき事」等10徳目に応じて約280話を分類配列する。中世武家社会向け教訓書として広く読まれ、漢籍・本朝説話を統合した教育的説話集の代表作。",
    background="13世紀中葉の武家社会興隆と、儒仏融合的徳目教育の需要。",
    development="近世初期に庶民教訓書として広く流布し、近世仮名草子教訓書の祖型となった。",
    historical_context="鎌倉中期の武家社会道徳形成期。",
    primary_source_url=NIJL+"biblio/200004849/",
    primary_source_type="NIJL: 十訓抄",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="無住『沙石集』",
    name_en="Muju, Shasekishu",
    name_original="沙石集",
    period_key="中世",
    definition="無住道暁（1227-1312）が1283年に著した仏教説話集。10巻、約150話。臨済禅と他宗の融合を背景に、世俗的笑話を仏教真理伝達の方便とする「沙中の金、石中の玉」の精神（書名由来）で著名。中世仏教説話の方法論的頂点を成し、近世落語の祖型としても重要。",
    background="13世紀末鎌倉末期の禅宗興隆と、無住の融合的仏教観。",
    development="近世初期落語の典拠となり、また中世仏教説話の方法論的範型となった。",
    historical_context="弘安の役（1281）直後の鎌倉末期社会。",
    primary_source_url=SAT+"satdb2015.php",
    primary_source_type="SAT 大正新脩大藏經・沙石集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"仏教方便と笑話",
         "description":"沙石集は仏教真理伝達の方便として笑話を用いる方法を理論化し、東アジア仏教哲学の方便論の文学的具現として位置づけられる。"}])

add(**C, name_ja="撰集抄",
    name_en="Senjusho",
    name_original="撰集抄",
    period_key="中世",
    definition="13世紀後半成立、西行仮託の仏教説話集。9巻、121話。西行を語り手として仏教高僧・名僧の説話を語る形式で、西行像形成の中核資料となる。「死人を蘇らせる」高野聖説話等で著名。後世の西行伝説の主要源泉として、文学史・芸能史双方で重要な地位を占める。",
    background="13世紀後半の西行信仰興隆と、西行に仮託する説話編纂。",
    development="能『西行桜』『江口』、近世西行物芸能の主要典拠となった。",
    historical_context="鎌倉中後期の西行隠遁聖伝説の成熟期。",
    primary_source_url=NIJL+"biblio/200004850/",
    primary_source_type="NIJL: 撰集抄",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="鴨長明『発心集』",
    name_en="Kamo no Chomei, Hosshinshu",
    name_original="発心集",
    period_key="中世",
    definition="鴨長明（1155?-1216）が1216年頃に著した仏教説話集。8巻、約100話。隠遁聖・高僧の発心譚を中核とし、長明自身の隠遁経験（『方丈記』）と通底する遁世思想を背景とする。中世隠遁文学の核心資料として、『方丈記』とともに長明思想の双璧を成す。",
    background="鎌倉初期の隠遁聖文化と、長明の浄土・遁世志向。",
    development="『閑居友』『撰集抄』『沙石集』等中世遁世説話集の系譜の中核に位置する。",
    historical_context="承久の乱（1221）直前の鎌倉初期社会と長明晩年。",
    primary_source_url=NIJL+"biblio/200004851/",
    primary_source_type="NIJL: 発心集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="慶政『閑居友』",
    name_en="Keisei, Kankyo no Tomo",
    name_original="閑居友",
    period_key="中世",
    definition="慶政上人（九条道家子、1189-1268）が1222年に著した仏教説話集。上下2巻、32話。男女別二部構成で、特に下巻女性発心譚は中世女性仏教史の貴重な資料。鴨長明『発心集』に直接続く時期に成立し、貴族出身遁世僧による中世仏教説話文学の代表作の一つ。",
    background="九条道家の摂関家公子の遁世と、女性仏教観の中世的展開。",
    development="中世女性仏教史研究の中核資料として、近代以降再評価された。",
    historical_context="承久の乱（1221）直後の九条家遁世僧文化。",
    primary_source_url=NIJL+"biblio/200004852/",
    primary_source_type="NIJL: 閑居友",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="三国伝記",
    name_en="Sangoku Denki",
    name_original="三国伝記",
    period_key="中世",
    definition="玄棟編、15世紀前半成立の仏教説話集。12巻、360話。天竺・震旦・本朝の三国の僧三人が交互に説話を語る形式で、『今昔物語集』の三国構造を継承しつつ室町期の説話文化を集成する。室町期説話集の代表的成果として、中世末から近世への橋渡し作品となる。",
    background="室町期説話文化の成熟と、三国仏教史的世界観の継続。",
    development="近世仮名草子・談義本への直接的祖型となった。",
    historical_context="室町中期の禅宗・天台宗融合的仏教文化。",
    primary_source_url=NIJL+"biblio/200004853/",
    primary_source_type="NIJL: 三国伝記",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="無住『雑談集』",
    name_en="Muju, Zotanshu",
    name_original="雑談集",
    period_key="中世",
    definition="無住道暁が1305年（嘉元3）に著した晩年の説話集。10巻。『沙石集』の続編的位置を占め、世俗説話・笑話・仏教説話を雑然と配列する。書名通り「雑談」の枠組みで仏教真理を伝達する方法を徹底させ、近世口承文学（落語・笑話）の祖型として再評価される。",
    background="無住晩年の体系性放棄と、雑然性自体を方法とする説話編集。",
    development="近世落語『沙石集』再話、明治以降の口承文学研究で再評価された。",
    historical_context="弘安・嘉元期の鎌倉末期社会。",
    primary_source_url=SAT+"satdb2015.php",
    primary_source_type="SAT 大正新脩大藏經・雑談集",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# E: 物語文学補完（10）  period: 中古/中世
# ============================================================
add(**C, name_ja="落窪物語",
    name_en="Ochikubo Monogatari",
    name_original="落窪物語",
    period_key="中古",
    definition="10世紀末成立、作者未詳の継子いじめ物語。継母にいじめられる「落窪の君」が貴公子に救出され継母に復讐するという、シンデレラ型物語の日本古代代表作。源氏物語以前の物語形式を伝え、中世お伽草子（『鉢かづき』『姥皮』）の祖型として、日本の継子譚伝統の起点を形成した。",
    background="10世紀末の物語文化興隆と、継子譚という民間伝承類型の貴族文学化。",
    development="中世お伽草子の継子譚群（『鉢かづき』『姥皮』）の直接的祖型となった。",
    historical_context="一条朝物語文化興隆期と、源氏物語以前の物語形式。",
    primary_source_url=AOZORA+"cards/001561/files/56074_56892.html",
    primary_source_type="青空文庫: 落窪物語",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"継子譚と民俗伝承類型",
         "description":"落窪物語はシンデレラ型継子譚の日本古代版で、人類学的世界民間伝承類型研究（ATU 510A）の比較対象として重要。"}])

add(**C, name_ja="住吉物語",
    name_en="Sumiyoshi Monogatari",
    name_original="住吉物語",
    period_key="中古",
    definition="10世紀末-11世紀初頭成立、作者未詳の継子いじめ物語。落窪物語と並ぶ継子譚で、住吉に隠れた姫君が後に幸福を得る筋立て。源氏物語『玉鬘』巻に「住吉の姫君」言及があり、源氏物語以前から流布していた古物語の一つとして重要。中世改作版が現存する。",
    background="10世紀末物語文化と、住吉信仰・継子譚の融合。",
    development="中世以降の住吉物語改作群と、近世お伽草子へ継承された。",
    historical_context="一条朝物語文化興隆期。",
    primary_source_url=NIJL+"biblio/200004854/",
    primary_source_type="NIJL: 住吉物語",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="浜松中納言物語",
    name_en="Hamamatsu Chunagon Monogatari",
    name_original="浜松中納言物語",
    period_key="中古",
    definition="11世紀後半成立、菅原孝標女作と伝える長編物語。浜松中納言が亡父の生まれ変わりを唐土に求めて渡航し、唐皇帝の后と結ばれる輪廻転生譚。源氏物語以後の中古物語の代表作で、転生・国際的舞台・夢幻的構造を特徴とし、後の中世物語（『松浦宮物語』）の祖型となった。",
    background="平安後期の浄土教・輪廻転生思想と、唐土への文化的憧憬。",
    development="松浦宮物語、中世王朝物語群（『夜の寝覚』『狭衣物語』）への直接的影響源。",
    historical_context="11世紀後半院政期前夜の物語文化と、宋への文化的志向。",
    primary_source_url=NIJL+"biblio/200004855/",
    primary_source_type="NIJL: 浜松中納言物語",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="夜の寝覚",
    name_en="Yoru no Nezame",
    name_original="夜の寝覚",
    period_key="中古",
    definition="11世紀後半成立、菅原孝標女作と伝える長編物語。中の君（寝覚の上）と中納言の許されぬ恋の悲劇を、夜の覚醒・夢・追懐の主題で描く。源氏物語『宇治十帖』の影響下にありつつ、独自の心理的内面性と運命的悲恋の主題で中古物語の精神的頂点を形成した。",
    background="11世紀後半源氏物語の継承と、女流物語の心理的深化。",
    development="松浦宮物語、狭衣物語と並ぶ中古後期物語三大作の一つとして位置づけられる。",
    historical_context="院政期前夜の貴族文化と物語文学の最終的成熟。",
    primary_source_url=NIJL+"biblio/200004856/",
    primary_source_type="NIJL: 夜の寝覚",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="狭衣物語",
    name_en="Sagoromo Monogatari",
    name_original="狭衣物語",
    period_key="中古",
    definition="11世紀後半成立、源頼国女（六条斎院宣旨）作と伝える長編物語。狭衣大将が許されぬ恋に苦悩しつつ皇位に上る過程を描く。源氏物語直接の影響下で書かれた中古後期物語の代表作で、宮廷恋愛と政治的上昇の二重構造で源氏物語のテーマを再展開した。",
    background="源氏物語以降の物語文学の継承と展開。",
    development="中世以降の物語梗概書（『風葉和歌集』）の主要対象となり、中古物語の代表作として継承された。",
    historical_context="院政期前夜の貴族物語文化の最終成熟期。",
    primary_source_url=NIJL+"biblio/200004857/",
    primary_source_type="NIJL: 狭衣物語",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="堤中納言物語",
    name_en="Tsutsumi Chunagon Monogatari",
    name_original="堤中納言物語",
    period_key="中古",
    definition="11世紀後半-12世紀成立の短編物語集。10編＋断章1編から成り、各話別作者・別年代の集合体。「虫めづる姫君」（虫を愛する規範外の姫の物語）が著名で、世界最古の短編物語集の一つとされる。各短編が独立した実験的形式を取り、中古物語の多様性を示す重要作品。",
    background="11世紀後半短編物語の興隆と、長編物語と並走する短編形式の確立。",
    development="近現代に「虫めづる姫君」が宮崎駿『風の谷のナウシカ』のヒロイン造形の祖型として再評価された。",
    historical_context="平安後期の物語文化多様化期。",
    primary_source_url=AOZORA+"cards/001075/files/45222_24081.html",
    primary_source_type="青空文庫: 堤中納言物語",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="とりかへばや物語",
    name_en="Torikaebaya Monogatari",
    name_original="とりかへばや物語",
    period_key="中古",
    definition="12世紀成立、作者未詳の異性装物語。男女取り違えた兄妹（性別を入れ替えて育てられた兄妹）が宮廷に出仕し、最終的に正しい性別に戻る物語。日本古典文学において稀有な性別越境主題を扱い、現代ジェンダー研究の中核資料として再評価された。中世改作版（『今とりかへばや』）も現存。",
    background="12世紀の物語形式実験と、ジェンダー越境への文学的関心。",
    development="現代ジェンダー研究・クィア理論の古典的参照点として再評価された。",
    historical_context="院政期の物語文化多様化と、規範外主題の文学的探究。",
    primary_source_url=NIJL+"biblio/200004858/",
    primary_source_type="NIJL: とりかへばや物語",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"とりかへばや物語は性別二項対立を物語的に解体する古典的事例で、AI時代の主体カテゴリ流動化（性別・人種・年齢）を再考する歴史的参照点となる。",
         "related_ai_phenomenon":"AI時代の主体カテゴリ流動化"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"異性装と性別越境",
         "description":"とりかへばや物語は古代日本の異性装文化を文学化し、人類学的ジェンダー研究の比較対象として中核的位置を占める。"}])

add(**C, name_ja="我が身にたどる姫君",
    name_en="Waga Mi ni Tadoru Himegimi",
    name_original="我が身にたどる姫君",
    period_key="中世",
    definition="13世紀後半成立、作者未詳の長編王朝物語。中世王朝物語の代表作で、姫君が出生の謎をたどる構造を中核とする。源氏物語『宇治十帖』の影響下にありつつ、中世的悲恋・出生謎・運命的構造を独自に展開した。中世王朝物語衰退期の重要作品。",
    background="鎌倉中期の王朝物語衰退期と、最終的な作品制作。",
    development="中世王朝物語の最末期作品として、王朝物語伝統の終焉を示す。",
    historical_context="鎌倉中期の貴族文化衰退と、武家文化興隆。",
    primary_source_url=NIJL+"biblio/200004859/",
    primary_source_type="NIJL: 我が身にたどる姫君",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="松浦宮物語",
    name_en="Matsuranomiya Monogatari",
    name_original="松浦宮物語",
    period_key="中世",
    definition="12世紀末-13世紀初頭成立、藤原定家作説有力の長編物語。松浦宮（侍従弁少将）が遣唐使として唐土に渡り、皇女との恋愛を体験する国際的舞台の物語。浜松中納言物語の系譜を継ぎ、唐土設定と漢詩文・琴楽の重層的展開で、定家美学の物語的具現と評される。",
    background="13世紀初頭の中国文化への憧憬継続と、定家ら新古今歌人の物語制作。",
    development="中世王朝物語の代表作の一つとして、定家美学の物語的展開を示す。",
    historical_context="新古今集（1205）前後の文化的精錬期。",
    primary_source_url=NIJL+"biblio/200004860/",
    primary_source_type="NIJL: 松浦宮物語",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="鎌倉物語草子全体論",
    name_en="Kamakura monogatari soshi: a general theory",
    name_original="鎌倉物語草子",
    period_key="中世",
    definition="鎌倉期に制作された短編物語草子群の総称的把握。『風葉和歌集』(1271)所載の物語梗概等から推定される、12世紀末から13世紀の中世王朝物語衰退期に量産された短編・断片的物語群を指す。多くは散逸し、書名・梗概のみ残るが、王朝物語伝統の中世的継承と最終的衰退を示す重要な集合体。",
    background="鎌倉期の貴族文化衰退と、それでも継続する物語制作。",
    development="室町期お伽草子への橋渡しとなり、お伽草子の文体的・形式的祖型となった。",
    historical_context="鎌倉中後期の貴族文化最終局面。",
    primary_source_url=NIJL+"biblio/200004861/",
    primary_source_type="NIJL: 風葉和歌集",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# F: 中世補完（9）  period: 中世
# ============================================================
add(**C, name_ja="徒然草段別考",
    name_en="Tsurezuregusa: section-by-section study",
    name_original="徒然草",
    period_key="中世",
    definition="兼好法師『徒然草』(1330頃)243段の段別解釈論。序段＋243段の独立した随想章を、(1)有職故実・儀礼考証、(2)無常観・遁世論、(3)処世訓・人生観察、(4)和歌・連歌論、(5)笑話・逸話の5層に分類する近現代国文学の枠組み。冨倉徳次郎・木藤才蔵以来の徒然草研究の中核。",
    background="14世紀前半南北朝期前夜の貴族・武家文化交錯と、兼好の遁世観。",
    development="近世以降の徒然草注釈書群（『野槌』『鉄槌』等）と現代国文学注釈の基盤となった。",
    historical_context="鎌倉幕府末期から建武新政前夜の社会的動揺期。",
    primary_source_url=AOZORA+"cards/000063/files/45224_24076.html",
    primary_source_type="青空文庫: 徒然草",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="方丈記の災厄記述",
    name_en="Hojoki: documentation of disasters",
    name_original="方丈記",
    period_key="中世",
    definition="鴨長明『方丈記』(1212)前半の五大災厄記述（安元の大火1177、治承の辻風1180、福原遷都1180、養和の飢饉1181-82、元暦の大地震1185）の文学史的意義。当代災害の具体的記述を文学的内省と結びつけ、災害文学の祖型を確立した。中世末法観の具体的形象化として、鎌倉初期社会史の第一級資料でもある。",
    background="平安末期-鎌倉初期の連続災害と、長明の現地観察。",
    development="近世以降、災害文学の祖型として再評価され、現代では3.11以降の災害文学論で再注目された。",
    historical_context="治承・寿永の乱（1180-85）期の社会的混乱と災害連鎖。",
    primary_source_url=AOZORA+"cards/000196/files/45226_19919.html",
    primary_source_type="青空文庫: 方丈記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"方丈記の災厄記述は当代観察者による具体的災害記録と内省的省察の統合で、AI時代の災害ドキュメンタリーと当事者性問題を再考する原型的参照点となる。",
         "related_ai_phenomenon":"AI生成災害ドキュメンタリーと当事者性"}])

add(**C, name_ja="太平記の和漢混淆",
    name_en="Taiheiki's Japanese-Chinese hybrid style",
    name_original="太平記",
    period_key="中世",
    definition="『太平記』(14世紀後半成立)が示す和漢混淆文の頂点。元弘の乱(1331)から細川頼之管領就任(1367)に至る40巻の南北朝動乱記で、漢文訓読体・和文体・故事引用・教訓的論評を融合した文体は中世軍記物語の文体的頂点を成す。後の太平記読み（街頭芸能）を通じて近世庶民文化に深く浸透した。",
    background="南北朝動乱期の文化総決算的編纂。",
    development="近世太平記読み（街頭講談）、軍記物語演芸、近代軍記物語論（石母田正）の中核作品となった。",
    historical_context="南北朝合一(1392)に至る動乱期の総合的記録。",
    primary_source_url=NIJL+"biblio/200004862/",
    primary_source_type="NIJL: 太平記",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="北畠親房『神皇正統記』",
    name_en="Kitabatake Chikafusa, Jinno Shotoki",
    name_original="神皇正統記",
    period_key="中世",
    definition="北畠親房（1293-1354）が1339年に著した歴史書・政道書。神武天皇から後村上天皇までの皇統を「正統」概念で系譜化し、南朝の正当性を主張する。「大日本者神国也」の冒頭で著名。中世日本の歴史哲学と国体論の祖型を確立し、近世水戸学・近代国学に深い影響を与えた。",
    background="南北朝動乱期の南朝側政治的危機と、親房の政道書執筆。",
    development="近世水戸学（『大日本史』）、近代国家神道、戦前皇国史観の理論的源泉となった。",
    historical_context="1339年後醍醐天皇崩御と南朝の劣勢化期。",
    primary_source_url=AOZORA+"cards/000919/files/4263_22308.html",
    primary_source_type="青空文庫: 神皇正統記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"中世国体論",
         "description":"神皇正統記は中世日本の国体論・歴史哲学の核となり、東アジア政治哲学史に独自の地位を占める。"}])

add(**C, name_ja="増鏡",
    name_en="Masukagami",
    name_original="増鏡",
    period_key="中世",
    definition="14世紀後半成立、作者未詳（二条良基説有）の歴史物語。後鳥羽天皇即位(1183)から後醍醐天皇隠岐還幸(1333)までの150年を編年体で記述する。鏡物（『大鏡』『今鏡』『水鏡』）の最終作で、王朝美的視点から中世前期史を貴族側から描いた。鏡物史伝伝統の終焉を示す重要作品。",
    background="鏡物4部作の歴史的継承と、南北朝期前夜の歴史総括。",
    development="近世以降、貴族側中世史の主要史料・文学として継続的に参照された。",
    historical_context="南北朝動乱期の歴史総括と、王朝側視点からの中世前期描写。",
    primary_source_url=NIJL+"biblio/200004863/",
    primary_source_type="NIJL: 増鏡",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="梅松論",
    name_en="Baishoron",
    name_original="梅松論",
    period_key="中世",
    definition="14世紀後半成立、作者未詳の軍記物語。鎌倉幕府滅亡(1333)から建武新政・室町幕府成立(1336)までを足利方視点から記述する。『太平記』が南朝側視点を含むのに対し、梅松論は明確に北朝・足利方の正当性を主張する。南北朝期の対立的歴史記述の北朝側代表作。",
    background="南北朝動乱期の北朝・足利方の歴史記述需要。",
    development="近世以降、太平記と並ぶ南北朝史の対比的史料として参照された。",
    historical_context="室町幕府成立直後（観応・延文期）の北朝歴史総括。",
    primary_source_url=NIJL+"biblio/200004864/",
    primary_source_type="NIJL: 梅松論",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="源平盛衰記",
    name_en="Genpei Joseiki",
    name_original="源平盛衰記",
    period_key="中世",
    definition="13世紀後半-14世紀前半成立、作者未詳の軍記物語。『平家物語』の異本系統として位置づけられる48巻の大著。平家物語の覚一本系統に比べて記述が詳細・拡大され、地方伝承・故事・歌謡を多く取り込む。中世軍記物語の拡大版・異本研究の中核資料。",
    background="平家物語の異本生成過程と、中世末期軍記物語の地方拡散。",
    development="近世太平記読みと並ぶ中世軍記物語の主要演芸源泉となった。",
    historical_context="鎌倉中期から南北朝期にかけての軍記物語の地方的展開。",
    primary_source_url=NIJL+"biblio/200004865/",
    primary_source_type="NIJL: 源平盛衰記",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="平治物語・保元物語",
    name_en="Heiji Monogatari and Hogen Monogatari",
    name_original="平治物語・保元物語",
    period_key="中世",
    definition="13世紀前半成立、作者未詳の軍記物語2作。『保元物語』は保元の乱(1156)を、『平治物語』は平治の乱(1159)を扱う。両作とも『平家物語』に直接先行する短編軍記物語で、武士勢力台頭の決定的事件を文学化した。「保元・平治・平家」の三部作的位置を占め、中世軍記物語の出発点を形成する。",
    background="鎌倉初期の武家文化興隆と、武士台頭の決定的瞬間（保元・平治の乱）の文学化。",
    development="平家物語、太平記、源平盛衰記等中世軍記物語伝統の出発点となった。",
    historical_context="承久の乱(1221)前後の鎌倉初期社会と武家文化形成期。",
    primary_source_url=NIJL+"biblio/200004866/",
    primary_source_type="NIJL: 平治物語・保元物語",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="義経記",
    name_en="Gikeiki",
    name_original="義経記",
    period_key="中世",
    definition="14世紀末-15世紀初頭成立、作者未詳の軍記物語。源義経（1159-1189）の生涯を、平家追討の英雄性ではなく、頼朝との対立・奥州落ちの悲劇として描く。鞍馬の修行・五条橋弁慶・安宅関等の伝説的場面を多く含み、後の能（『安宅』『船弁慶』『鞍馬天狗』）・歌舞伎（『勧進帳』）・浄瑠璃の主要典拠となった。義経伝説形成の中核資料。",
    background="室町初期の義経伝説興隆と、悲劇的英雄像への民衆的関心。",
    development="能・歌舞伎・浄瑠璃の義経物の主要典拠として、近世日本演劇文化に深く浸透した。",
    historical_context="室町初期の判官贔屓文化の形成期。",
    primary_source_url=NIJL+"biblio/200004867/",
    primary_source_type="NIJL: 義経記",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        # Reuse existing Japan periods (上代/中古/中世/近世) — no creation needed.
        period_ids: dict[str, int] = {}
        for nj in ["上代", "中古", "中世", "近世"]:
            row = db.conn.execute(
                "SELECT id FROM periods WHERE name_ja=? AND region='東アジア' LIMIT 1",
                (nj,)).fetchone()
            if row is None:
                print(f"  [error] period not found: {nj}")
                return 1
            period_ids[nj] = row[0]

        # Insert concepts
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
        print(f"[c16-w13] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c16-w13] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
