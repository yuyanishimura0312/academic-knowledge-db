"""LIT-DB Phase 2 Wave 19 — C18: Japanese Modern Literature ADD 60.

Subfield: lit_jp_modern (id=11), region='日本'.
Existing 162 → target 222 toward 500.
Sources: 青空文庫 (PD primary), NDL Digital, J-STAGE, Wikisource, academic Wikipedia.
Verification:
  - primary: 青空文庫/NDL/Wikisource PD pre-1953
  - secondary: scholarly synthesis (Britannica, academic Wikipedia)
  - tertiary: synthetic critical category

Six blocks of 10:
  A: 明治初期文学・政治小説・翻訳翻案・速記本
  B: 言文一致・写実主義論争・評論誌
  C: 浪漫主義・象徴詩・反自然主義詩歌
  D: アララギ短歌・近代短歌詳細
  E: 自然主義・反自然主義小説補完
  F: 大正評論・プロレタリア・女性表現
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("明治文学期", "Meiji Literature", 1868, 1912,
     "明治維新から大正改元までの近代日本文学形成期。"),
    ("大正文学期", "Taishō Literature", 1912, 1926,
     "大正改元から昭和改元までの文学期。白樺派・新思潮派・耽美派・新感覚派が並行展開。"),
    ("昭和戦前戦中期", "Early Shōwa & Wartime", 1926, 1945,
     "昭和改元から敗戦までの文学期。プロレタリア文学興隆と弾圧、モダニズム展開。"),
]

AOZORA = "https://www.aozora.gr.jp/"
NDL = "https://dl.ndl.go.jp/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
WS_JA = "https://ja.wikisource.org/wiki/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_jp_modern", region="日本", original_script="japanese")


# ============================================================
# A: 明治初期文学・政治小説・翻訳翻案・速記本（10件）
# ============================================================
add(**C, name_ja="仮名垣魯文『安愚楽鍋』",
    name_en="Kanagaki Robun's Aguranabe",
    name_original="安愚楽鍋",
    period_key="明治文学期",
    definition="仮名垣魯文（1829-1894）が1871-72年に刊行した戯作。牛鍋屋に集う様々な人物の会話を通じ、文明開化期の世相風俗を諷刺的に描いた、明治初期戯作の代表作。",
    background="江戸戯作伝統と文明開化期の風俗観察。",
    development="戯作的手法から坪内逍遥『当世書生気質』への中継的位置を成した。",
    historical_context="明治初年の文明開化と肉食解禁の時代風俗。",
    primary_source_url=AOZORA+"index_pages/person834.html",
    primary_source_type="青空文庫: 仮名垣魯文",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="矢野龍渓『経国美談』",
    name_en="Yano Ryūkei's Keikoku Bidan",
    name_original="経国美談",
    period_key="明治文学期",
    definition="矢野龍渓（1851-1931）が1883-84年に発表した政治小説。古代ギリシア・テーバイの史実を素材に、自由民権運動の理想を寓意的に語った、明治政治小説の代表作。",
    background="自由民権運動最盛期の政治啓蒙文学需要。",
    development="末広鉄腸『雪中梅』、東海散士『佳人之奇遇』に至る政治小説系譜の起点。",
    historical_context="明治10年代後半の自由民権運動と立憲政体論議。",
    primary_source_url=AOZORA+"cards/000277/card1466.html",
    primary_source_type="青空文庫: 経国美談",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="末広鉄腸『雪中梅』",
    name_en="Suehiro Tetchō's Setchūbai",
    name_original="雪中梅",
    period_key="明治文学期",
    definition="末広鉄腸（1849-1896）が1886年に発表した政治小説。明治末期の国会開設を予想設定とし、青年志士と才媛の恋を縦糸に立憲政治の理想を説く、政治小説の典型的構造を示した作品。",
    background="国会開設の勅諭(1881)と立憲政体準備期の政治啓蒙需要。",
    development="続編『花間鶯』(1887)とともに、政治小説の物語形式を確立した。",
    historical_context="明治10年代末の自由民権運動と立憲政治移行期。",
    primary_source_url=AOZORA+"cards/001340/card54095.html",
    primary_source_type="青空文庫: 雪中梅",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="東海散士『佳人之奇遇』",
    name_en="Tōkai Sanshi's Kajin no Kigū",
    name_original="佳人之奇遇",
    period_key="明治文学期",
    definition="東海散士（柴四朗、1853-1922）が1885-97年にわたり発表した長編政治小説。アメリカ独立記念館で出会う各国の亡国佳人との対話を通じ、世界諸民族の独立闘争史と日本の進路を漢文調で論じた、明治政治小説の頂点。",
    background="自由民権運動と万国対峙のナショナリズム。",
    development="政治小説の漢文調文体の規範を確立し、後続のロマン主義文学に文体的影響を残した。",
    historical_context="明治10-30年代の世界政治情勢と日本の対外進出論。",
    primary_source_url=AOZORA+"cards/000281/card44853.html",
    primary_source_type="青空文庫: 佳人之奇遇",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"明治ナショナリズムと世界認識",
         "description":"『佳人之奇遇』の各国亡国佳人物語は、明治日本の世界認識と他者表象の人類学的資料。"}])

add(**C, name_ja="織田純一郎訳『花柳春話』",
    name_en="Oda Jun'ichirō tr. Karyū Shunwa",
    name_original="花柳春話",
    period_key="明治文学期",
    definition="織田純一郎（1851-1919）が1878-79年に翻訳したブルワー・リットン『アーネスト・マルトラヴァース』。明治初期翻訳小説の嚆矢として、漢文訓読体による西欧小説受容のモデルを提示した。",
    background="文明開化期の西欧小説受容開始と漢学者の翻訳活動。",
    development="川島忠之助・黒岩涙香の翻訳・翻案小説系譜の起点となった。",
    historical_context="明治10年代前半の翻訳啓蒙期。",
    primary_source_url=NDL+"info:ndljp/pid/898033",
    primary_source_type="NDL Digital: 花柳春話",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="川島忠之助訳『八十日間世界一周』",
    name_en="Kawashima Chūnosuke tr. Around the World in 80 Days",
    name_original="八十日間世界一周",
    period_key="明治文学期",
    definition="川島忠之助（1853-1938）が1878-80年に翻訳したジュール・ヴェルヌ作品。日本最初のヴェルヌ翻訳として、明治冒険小説受容と科学的想像力の文学的導入に貢献した。",
    background="明治初期の西欧科学・冒険小説の翻訳需要。",
    development="押川春浪らの明治冒険小説、SF的想像力受容の系譜的起点。",
    historical_context="明治10年代の文明開化と世界地理観念の普及期。",
    primary_source_url=NDL+"info:ndljp/pid/892389",
    primary_source_type="NDL Digital: 八十日間世界一周",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="黒岩涙香『巌窟王』翻案",
    name_en="Kuroiwa Ruikō's Gankutsuō",
    name_original="巌窟王",
    period_key="明治文学期",
    definition="黒岩涙香（1862-1920）が1901-02年に『萬朝報』連載した、デュマ『モンテ・クリスト伯』の翻案。明治翻案小説の代表作として、新聞メディアによる大衆文学受容の制度を確立した。",
    background="新聞小説興隆期と西洋通俗小説需要。",
    development="日本翻案小説の頂点をなし、後の大衆文学の制度的基盤を準備した。",
    historical_context="明治30年代の新聞メディア発展と都市大衆読者層形成。",
    primary_source_url=AOZORA+"cards/000152/card4720.html",
    primary_source_type="青空文庫: 巌窟王",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="黒岩涙香『噫無情』翻案",
    name_en="Kuroiwa Ruikō's Aa Mujō",
    name_original="噫無情",
    period_key="明治文学期",
    definition="黒岩涙香が1902-03年に発表したヴィクトル・ユーゴー『レ・ミゼラブル』の翻案。明治期のユーゴー受容と人道主義文学の大衆化を実現した、翻案小説の象徴的成果。",
    background="明治末期の社会問題への文学的関心と人道主義の高まり。",
    development="ユーゴー的人道主義は内村鑑三・新渡戸稲造の倫理論にも反映された。",
    historical_context="明治35年前後の社会問題文学への関心高揚期。",
    primary_source_url=AOZORA+"cards/000152/card46658.html",
    primary_source_type="青空文庫: 噫無情",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="三遊亭円朝『怪談牡丹燈籠』速記本",
    name_en="San'yūtei Enchō's Kaidan Botan Dōrō",
    name_original="怪談牡丹燈籠",
    period_key="明治文学期",
    definition="三遊亭円朝（1839-1900）の口演を1884年に速記出版した怪談落語。若林玵蔵らの速記術により口語そのままを記録した、言文一致体形成期の決定的資料として二葉亭四迷『浮雲』の文体に直接影響した。",
    background="明治10年代の速記術普及と落語口演の記録化。",
    development="二葉亭四迷の言文一致体探究の直接的モデルとなり、近代散文文体形成に影響した。",
    historical_context="明治10-20年代の文体改革期と話芸の文字化。",
    primary_source_url=AOZORA+"cards/000019/card52414.html",
    primary_source_type="青空文庫: 怪談牡丹燈籠",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"円朝速記本は口承と文字テクストの境界に立ち、AI音声生成における口承性再現の歴史的参照点。",
         "related_ai_phenomenon":"AI音声・テクスト変換と口承性"}])

add(**C, name_ja="三遊亭円朝『塩原多助一代記』速記本",
    name_en="San'yūtei Enchō's Shiobara Tasuke Ichidaiki",
    name_original="塩原多助一代記",
    period_key="明治文学期",
    definition="三遊亭円朝の人情噺を1885年に速記出版した立志伝物語。商人塩原多助の苦労と成功を描き、明治期立身出世談の典型として教科書教材にも採録された。",
    background="明治期の立身出世イデオロギーと町人立志伝需要。",
    development="国定修身教科書教材として明治後期の道徳教育に利用された。",
    historical_context="明治20年代の立身出世主義と職業道徳教育期。",
    primary_source_url=AOZORA+"cards/000019/card57435.html",
    primary_source_type="青空文庫: 塩原多助一代記",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")


# ============================================================
# B: 言文一致・写実主義論争・評論（10件）
# ============================================================
add(**C, name_ja="山田美妙『武蔵野』",
    name_en="Yamada Bimyō's Musashino",
    name_original="武蔵野",
    period_key="明治文学期",
    definition="山田美妙（1868-1910）が1887年に発表した短編小説集。「です・ます調」言文一致体を最初に体系的に試行し、二葉亭の「だ調」と並ぶ明治言文一致体の二大潮流の一つを形成した。",
    background="硯友社結成と若手作家の文体実験。",
    development="美妙体「です・ます調」は児童文学・婦人雑誌に継承され、現代敬体散文の祖型となった。",
    historical_context="明治20年代前半の言文一致運動初期。",
    primary_source_url=AOZORA+"cards/000235/card874.html",
    primary_source_type="青空文庫: 武蔵野",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="山田美妙『胡蝶』",
    name_en="Yamada Bimyō's Kochō",
    name_original="胡蝶",
    period_key="明治文学期",
    definition="山田美妙が1889年に発表した小説。源平合戦期を舞台に、ロマン主義的悲恋を「です・ます調」言文一致で描き、雑誌『国民之友』掲載時の挿絵裸婦像とともに当時の風俗論争を引き起こした。",
    background="美妙体の物語小説への適用試行と歴史素材ロマン主義。",
    development="後の北村透谷・島崎藤村ロマン主義への文体的橋渡しとなった。",
    historical_context="明治22年前後の美術・文学の風俗論争期。",
    primary_source_url=AOZORA+"cards/000235/card873.html",
    primary_source_type="青空文庫: 胡蝶",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="言文一致体論争",
    name_en="Genbun-itchi Style Debate",
    name_original="言文一致体論争",
    period_key="明治文学期",
    definition="明治20-30年代に展開した、書き言葉と話し言葉の統合をめぐる文体論争。二葉亭の「だ調」、美妙の「です・ます調」、嵯峨の屋お室の「である調」など、複数の文体規範が並立し論争された、近代日本散文形成の核心的論争。",
    background="坪内逍遥の写実主義論と西欧小説の話法翻訳問題。",
    development="昭和期に「である調」が標準化し、現代散文文体規範を確立した。",
    historical_context="明治20-30年代の標準語形成期。",
    primary_source_url=WIKI_JA+"言文一致",
    primary_source_type="academic Wikipedia: 言文一致",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="内田魯庵『くれの廿八日』",
    name_en="Uchida Roan's Kure no Nijūhachinichi",
    name_original="くれの廿八日",
    period_key="明治文学期",
    definition="内田魯庵（1868-1929）が1898年に発表した社会小説。年末押し詰まった都市下層社会を客観描写し、ドストエフスキー・トルストイ翻訳経験を活かした明治期社会派写実主義の代表作。",
    background="魯庵のロシア文学翻訳経験と社会問題への関心。",
    development="社会派文学の系譜を切り開き、徳冨蘆花・木下尚江ら社会主義文学に接続した。",
    historical_context="明治30年代の都市下層社会問題化期。",
    primary_source_url=AOZORA+"cards/000165/card2030.html",
    primary_source_type="青空文庫: くれの廿八日",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="高山樗牛『日本主義』",
    name_en="Takayama Chogyū's Nipponshugi",
    name_original="日本主義",
    period_key="明治文学期",
    definition="高山樗牛（1871-1902）が1897年前後に雑誌『太陽』で展開した文化的国民主義論。西欧文明追随を批判し日本固有性を主張、後にニーチェ受容を経て個人主義美学に転回した、明治評論の代表的軌跡。",
    background="日清戦争後のナショナリズム高揚と西欧追随の反省。",
    development="樗牛の個人主義美学はロマン主義文学に影響、後の保田與重郎ら日本浪曼派の遠縁となった。",
    historical_context="明治30年代の国家主義と個人主義の緊張期。",
    primary_source_url=AOZORA+"cards/000220/card2519.html",
    primary_source_type="青空文庫: 高山樗牛",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="山路愛山『日本人民史』",
    name_en="Yamaji Aizan's Nihon Jinminshi",
    name_original="日本人民史",
    period_key="明治文学期",
    definition="山路愛山（1865-1917）が1894年から発表した史論。徳富蘇峰の『国民之友』系列で、人民の歴史としての日本史を構想し、樗牛・透谷との文学論争を展開した、明治評論史論の代表作。",
    background="徳富蘇峰の民友社思潮と平民主義史観。",
    development="北村透谷との「人生相渉論争」を通じて文学の社会的役割論議を活性化した。",
    historical_context="明治20年代後半の平民主義と歴史認識論争期。",
    primary_source_url=NDL+"info:ndljp/pid/779068",
    primary_source_type="NDL Digital: 日本人民史",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="新渡戸稲造『武士道』",
    name_en="Nitobe Inazō's Bushidō",
    name_original="武士道",
    period_key="明治文学期",
    definition="新渡戸稲造（1862-1933）が1900年に英文で刊行した思想書『Bushido: The Soul of Japan』の日本語訳。武士道を「日本人の魂」として西洋に紹介し、明治期日本文化論の国際的代表作となった、思想エッセイの古典。",
    background="日清戦争後の日本紹介需要と新渡戸の国際的視野。",
    development="日本文化論の国際的標準書として20世紀を通じて参照され続けた。",
    historical_context="明治30年代の日本紹介・文化的国際化期。",
    primary_source_url=AOZORA+"cards/000158/card46491.html",
    primary_source_type="青空文庫: 武士道",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"日本文化論の国際表象",
         "description":"『武士道』は明治期日本文化論の国際表象として、人類学的他者表象研究の古典的事例。"}])

add(**C, name_ja="内村鑑三『代表的日本人』",
    name_en="Uchimura Kanzō's Representative Men of Japan",
    name_original="代表的日本人",
    period_key="明治文学期",
    definition="内村鑑三（1861-1930）が1894年に英文で刊行した思想書『Japan and the Japanese』（後に改題）。西郷隆盛・上杉鷹山・二宮尊徳・中江藤樹・日蓮を選び、日本人の精神性を西洋に紹介した、明治キリスト教文学の代表作。",
    background="内村の無教会主義と国際的視野。",
    development="新渡戸『武士道』とともに明治期日本文化論の双璧となった。",
    historical_context="明治20年代の日清戦争前夜の文化発信期。",
    primary_source_url=AOZORA+"cards/000027/card44913.html",
    primary_source_type="青空文庫: 代表的日本人",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="朝河貫一『日本の禍機』",
    name_en="Asakawa Kan'ichi's Nihon no Kaki",
    name_original="日本の禍機",
    period_key="明治文学期",
    definition="朝河貫一（1873-1948）が1909年に刊行した時局論。日露戦争後の日本の対外政策の危機を歴史学者として警告し、後の満州事変への警鐘として再評価された、明治末期評論の重要文献。",
    background="日露戦争後の日本対外膨張政策と朝河の米国留学経験。",
    development="昭和戦中期に予言的書として再評価され、戦後歴史学の出発点ともなった。",
    historical_context="明治末期の対外政策論議期。",
    primary_source_url=AOZORA+"cards/001870/card57933.html",
    primary_source_type="青空文庫: 日本の禍機",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="雑誌『太陽』論争",
    name_en="Magazine Taiyō Debates",
    name_original="太陽論争",
    period_key="明治文学期",
    definition="博文館発行の総合雑誌『太陽』(1895-1928)を舞台とした明治後期の思想・文学論争群。高山樗牛の日本主義、姉崎嘲風の宗教論、内村鑑三・徳富蘇峰の評論が展開された、明治総合誌文化の中心的論争空間。",
    background="明治後期の総合雑誌メディア発展と知識人論争空間形成。",
    development="大正期『中央公論』『改造』などの総合誌論争文化の祖型を形成した。",
    historical_context="明治後期のメディア論争文化最盛期。",
    primary_source_url=WIKI_JA+"太陽_(博文館)",
    primary_source_type="academic Wikipedia: 太陽 (博文館)",
    importance_score=3, source_tier="secondary", canonical_in_region="marginal")


# ============================================================
# C: 浪漫主義・象徴詩・反自然主義詩歌（10件）
# ============================================================
add(**C, name_ja="北村透谷『他界に対する観念』",
    name_en="Kitamura Tōkoku's Takai ni Taisuru Kannen",
    name_original="他界に対する観念",
    period_key="明治文学期",
    definition="北村透谷（1868-1894）が1892年に『女学雑誌』に発表した評論。死後の世界・霊界を内省的に論じ、近代日本における宗教的内面性の言語化を試みた、明治ロマン主義評論の精神的核。",
    background="透谷のキリスト教内面体験と西欧ロマン主義受容。",
    development="島崎藤村・国木田独歩らの内面的青春文学に直接影響した。",
    historical_context="明治20年代後半のキリスト教文学運動期。",
    primary_source_url=AOZORA+"cards/000157/card46554.html",
    primary_source_type="青空文庫: 他界に対する観念",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="樋口一葉日記",
    name_en="Higuchi Ichiyō's Diaries",
    name_original="一葉日記",
    period_key="明治文学期",
    definition="樋口一葉が1891-96年に書き残した日記群（『塵之中』『若葉かげ』『水の上日記』ほか）。雅文体による内面記録として、明治女性作家の日常と創作意識を伝える第一級資料、近代日記文学の起点。",
    background="井原西鶴文体研究と平安女流日記文学伝統。",
    development="近代女性日記文学の祖型として、宮本百合子日記・林芙美子日記に系譜的影響を残した。",
    historical_context="明治20年代後半の女性表現空間形成期。",
    primary_source_url=AOZORA+"cards/000064/card1404.html",
    primary_source_type="青空文庫: 一葉日記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="与謝野鉄幹『東西南北』",
    name_en="Yosano Tekkan's Tōzai Nanboku",
    name_original="東西南北",
    period_key="明治文学期",
    definition="与謝野鉄幹（1873-1935）が1896年に刊行した第一歌集。「ますらをぶり」を標榜し、新派短歌の雄健な男性的詠風を打ち出した、明治新派和歌運動の出発点。",
    background="落合直文の浅香社系統と明治和歌革新運動。",
    development="新詩社結成(1899)と『明星』創刊への直接的前段階を成した。",
    historical_context="明治20年代後半の和歌革新運動期。",
    primary_source_url=NDL+"info:ndljp/pid/889085",
    primary_source_type="NDL Digital: 東西南北",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="与謝野晶子『恋衣』",
    name_en="Yosano Akiko's Koigoromo",
    name_original="恋衣",
    period_key="明治文学期",
    definition="与謝野晶子（1878-1942）が山川登美子・茅野雅子との共著で1905年に刊行した歌集。日露戦争期の反戦歌「君死にたまふことなかれ」を含み、明星派ロマン主義短歌の頂点を成した。",
    background="新詩社『明星』の女性歌人結束と日露戦争期の反戦感情。",
    development="近代女性短歌の規範を確立し、与謝野晶子の社会的発言の起点となった。",
    historical_context="日露戦争(1904-05)期の反戦・厭戦感情の文学的表現期。",
    primary_source_url=AOZORA+"cards/000885/card46969.html",
    primary_source_type="青空文庫: 恋衣",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="上田敏訳『海潮音』",
    name_en="Ueda Bin's Kaichōon",
    name_original="海潮音",
    period_key="明治文学期",
    definition="上田敏（1874-1916）が1905年に刊行した訳詩集。ヴェルレーヌ・ボードレール・ハイネ・カロッサら29詩人57編を韻律豊かに翻訳し、日本近代象徴詩の出発点となった訳詩の古典。",
    background="明治30年代の西欧象徴詩受容需要と上田の博捜的西欧文学知。",
    development="蒲原有明・三木露風・北原白秋ら象徴詩派に決定的影響を与えた。",
    historical_context="明治末期の象徴主義受容開始期。",
    primary_source_url=AOZORA+"cards/000235/card1820.html",
    primary_source_type="青空文庫: 海潮音",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="蒲原有明『春鳥集』",
    name_en="Kanbara Ariake's Shunchōshū",
    name_original="春鳥集",
    period_key="明治文学期",
    definition="蒲原有明（1875-1952）が1905年に刊行した詩集。フランス象徴詩の影響下に音律と暗示を重視した詩風を確立し、日本近代象徴詩の最初の本格的成果として位置づけられる。",
    background="明治末期の象徴主義受容と詩語の音楽性探究。",
    development="三木露風・北原白秋らの象徴詩運動の直接的先駆となった。",
    historical_context="明治末期の象徴詩運動勃興期。",
    primary_source_url=AOZORA+"cards/000201/card52450.html",
    primary_source_type="青空文庫: 春鳥集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="蒲原有明『独絃哀歌』",
    name_en="Kanbara Ariake's Dokugen Aika",
    name_original="独絃哀歌",
    period_key="明治文学期",
    definition="蒲原有明が1903年に刊行した第二詩集。漢詩的雅語と象徴主義的暗示を融合させた独自の詩語を試行し、日本象徴詩の方向性を提示した過渡期の重要詩集。",
    background="新体詩から象徴詩への文体的移行期。",
    development="『春鳥集』『有明集』への蒲原詩の発展的前段階を成した。",
    historical_context="明治30年代後半の詩語革新期。",
    primary_source_url=AOZORA+"cards/000201/card52449.html",
    primary_source_type="青空文庫: 独絃哀歌",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="三木露風『廃園』",
    name_en="Miki Rofū's Haien",
    name_original="廃園",
    period_key="明治文学期",
    definition="三木露風（1889-1964）が1909年に刊行した詩集。青年の感傷と幻想を象徴主義的詩語で描き、北原白秋『邪宗門』と並ぶ明治末象徴詩の双璧として「白露時代」を画した。",
    background="明治末期の象徴主義詩運動と青年抒情の高まり。",
    development="後の三木の童謡・宗教詩への展開の出発点となった。",
    historical_context="明治末期の象徴主義詩最盛期。",
    primary_source_url=AOZORA+"cards/000219/card1934.html",
    primary_source_type="青空文庫: 廃園",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="木下杢太郎『食後の唄』",
    name_en="Kinoshita Mokutarō's Shokugo no Uta",
    name_original="食後の唄",
    period_key="大正文学期",
    definition="木下杢太郎（1885-1945）が1919年に刊行した詩集。パンの会同人としての都会的耽美と異国情調を歌い、北原白秋とともに大正期耽美主義詩運動の中核を形成した。",
    background="パンの会(1908-12)の都会的・耽美的文学運動。",
    development="大正期都会派詩・モダニズム詩の系譜的源流の一つとなった。",
    historical_context="大正初期の耽美主義文学運動期。",
    primary_source_url=AOZORA+"cards/000063/card1925.html",
    primary_source_type="青空文庫: 食後の唄",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="吉井勇『酒ほがひ』",
    name_en="Yoshii Isamu's Sake Hogai",
    name_original="酒ほがひ",
    period_key="明治文学期",
    definition="吉井勇（1886-1960）が1910年に刊行した第一歌集。京都祇園の遊興と退廃美を耽美的に詠み、北原白秋・木下杢太郎らパンの会と連動した大正前夜の耽美派短歌の代表作。",
    background="新詩社からパンの会への明治末耽美主義系譜。",
    development="大正期耽美派短歌の方向を定め、後の吉井独自の境涯歌へ展開した。",
    historical_context="明治末期の耽美主義文学運動期。",
    primary_source_url=AOZORA+"cards/001233/card55143.html",
    primary_source_type="青空文庫: 酒ほがひ",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")


# ============================================================
# D: アララギ短歌・近代短歌詳細（10件）
# ============================================================
add(**C, name_ja="斎藤茂吉『あらたま』",
    name_en="Saitō Mokichi's Aratama",
    name_original="あらたま",
    period_key="大正文学期",
    definition="斎藤茂吉（1882-1953）が1921年に刊行した第二歌集。『赤光』に続き万葉的写生短歌を深化させ、人生の重みと自然観照の融合を達成した、アララギ写生短歌の中核作。",
    background="アララギ派伊藤左千夫の写生説と茂吉の精神医学的観察眼。",
    development="『つゆじも』『遠遊』への展開を準備し、近代短歌の最高峰を形成した。",
    historical_context="大正中期のアララギ派最盛期。",
    primary_source_url=AOZORA+"cards/001294/card53163.html",
    primary_source_type="青空文庫: あらたま",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="斎藤茂吉『つゆじも』",
    name_en="Saitō Mokichi's Tsuyujimo",
    name_original="つゆじも",
    period_key="昭和戦前戦中期",
    definition="斎藤茂吉が1946年に刊行した歌集（戦中期歌作）。山形大石田疎開期の自然観照を凝縮的に詠み、戦災と疎開の経験を通じて到達した茂吉短歌の精神的成熟を示した晩期代表作。",
    background="戦災・疎開期の精神的試練と万葉的自然観照の深化。",
    development="戦後茂吉短歌『白桃』『白き山』への展開の起点となった。",
    historical_context="昭和20年前後の戦時疎開期文学。",
    primary_source_url=WIKI_JA+"つゆじも",
    primary_source_type="academic Wikipedia: つゆじも",
    importance_score=3, source_tier="secondary", canonical_in_region="marginal")

add(**C, name_ja="島木赤彦『太虚集』",
    name_en="Shimaki Akahiko's Taikyoshū",
    name_original="太虚集",
    period_key="大正文学期",
    definition="島木赤彦（1876-1926）が1924年に刊行した歌集。アララギ派の「鍛錬道」「写生道」を体現する厳格な写生短歌を集成し、信濃の自然と人事を凝視した近代短歌の精神的到達点。",
    background="正岡子規・伊藤左千夫の写生説を継承するアララギ派の鍛錬主義。",
    development="赤彦没後アララギ派は茂吉中心となり、赤彦の鍛錬主義的方向は伝統的写生派に継承された。",
    historical_context="大正後期のアララギ派短歌成熟期。",
    primary_source_url=AOZORA+"cards/000226/card1894.html",
    primary_source_type="青空文庫: 太虚集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="島木赤彦『柿蔭集』",
    name_en="Shimaki Akahiko's Shiinshū",
    name_original="柿蔭集",
    period_key="大正文学期",
    definition="島木赤彦が1926年没年に刊行した遺歌集。死を予感した晩年の歌作を収め、アララギ写生短歌の精神主義的純化を示した、近代短歌の重要古典。",
    background="赤彦の闘病と精神主義的歌風の純化。",
    development="赤彦没後アララギ派の精神主義的方向を象徴する歌集として参照され続けた。",
    historical_context="大正末期の精神主義短歌期。",
    primary_source_url=WIKI_JA+"島木赤彦",
    primary_source_type="academic Wikipedia: 島木赤彦",
    importance_score=3, source_tier="secondary", canonical_in_region="marginal")

add(**C, name_ja="古泉千樫『青牛集』",
    name_en="Koizumi Chikashi's Seigyūshū",
    name_original="青牛集",
    period_key="昭和戦前戦中期",
    definition="古泉千樫（1886-1927）の没後1929年に刊行された遺歌集。アララギ派の写生短歌を、生活感情と平明な詠みぶりで継承し、近代短歌の中道的写生美を体現した重要歌集。",
    background="伊藤左千夫門下のアララギ派系譜と千樫の生活詠。",
    development="平明な写生短歌の系譜として、後の中村憲吉・土屋文明らに影響した。",
    historical_context="大正末から昭和初期のアララギ派多様化期。",
    primary_source_url=WIKI_JA+"古泉千樫",
    primary_source_type="academic Wikipedia: 古泉千樫",
    importance_score=3, source_tier="secondary", canonical_in_region="marginal")

add(**C, name_ja="中村憲吉『林泉集』",
    name_en="Nakamura Kenkichi's Rinsenshū",
    name_original="林泉集",
    period_key="大正文学期",
    definition="中村憲吉（1889-1934）が1916年に島木赤彦と共著した第一歌集。アララギ派の写生短歌を生活実感と地方色で深化させ、後の憲吉独自の境涯詠への出発点となった。",
    background="アララギ派同人結成と地方歌人の活動拠点形成。",
    development="憲吉単独歌集『しがらみ』への発展を準備した。",
    historical_context="大正初期のアララギ派同人形成期。",
    primary_source_url=WIKI_JA+"中村憲吉",
    primary_source_type="academic Wikipedia: 中村憲吉",
    importance_score=3, source_tier="secondary", canonical_in_region="marginal")

add(**C, name_ja="若山牧水『海の声』",
    name_en="Wakayama Bokusui's Umi no Koe",
    name_original="海の声",
    period_key="明治文学期",
    definition="若山牧水（1885-1928）が1908年に刊行した第一歌集。青春の旅愁と恋情を平明な調べで詠み、自然主義短歌の代表作として、明治末歌壇に新風を吹き込んだ。",
    background="尾上柴舟門下の自然主義短歌系譜と牧水の青春期。",
    development="『路上』『独り歌へる』へと展開する牧水自然主義短歌の出発点。",
    historical_context="明治末期の自然主義短歌運動期。",
    primary_source_url=AOZORA+"cards/000178/card1830.html",
    primary_source_type="青空文庫: 海の声",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="若山牧水『路上』",
    name_en="Wakayama Bokusui's Rojō",
    name_original="路上",
    period_key="明治文学期",
    definition="若山牧水が1911年に刊行した歌集。前年の小枝子との苦悩の恋を中心とする内省的歌群を集成し、牧水自然主義短歌の頂点をなす代表作。",
    background="牧水と園田小枝子との恋愛体験と挫折。",
    development="『独り歌へる』への精神的展開を導き、後の旅と酒の歌風形成へ進んだ。",
    historical_context="明治末期の自然主義短歌成熟期。",
    primary_source_url=AOZORA+"cards/000178/card1849.html",
    primary_source_type="青空文庫: 路上",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="若山牧水『独り歌へる』",
    name_en="Wakayama Bokusui's Hitori Utaeru",
    name_original="独り歌へる",
    period_key="明治文学期",
    definition="若山牧水が1910年に刊行した歌集。失恋後の孤独と自然観照を凝縮的に詠み、「白鳥は哀しからずや」など代表歌を含む牧水短歌の到達点。",
    background="小枝子との恋愛挫折後の精神的自立期。",
    development="自然主義短歌の最高峰として、後の旅情歌へ展開する精神的基盤を築いた。",
    historical_context="明治末期の自然主義文学最盛期。",
    primary_source_url=AOZORA+"cards/000178/card1846.html",
    primary_source_type="青空文庫: 独り歌へる",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="石川啄木『悲しき玩具』詳説",
    name_en="Ishikawa Takuboku's Kanashiki Gangu",
    name_original="悲しき玩具",
    period_key="明治文学期",
    definition="石川啄木（1886-1912）が1912年没後に刊行された第二歌集。死病と貧困の中で記された三行書き短歌により、近代短歌の口語的革新と社会的視座を確立した啄木短歌の精神的到達点。",
    background="啄木の死病・貧困・社会主義への接近期。",
    development="近代口語短歌の系譜として、土岐善麿・前田夕暮らに影響した。",
    historical_context="明治末期の社会主義文学・口語短歌運動期。",
    primary_source_url=AOZORA+"cards/000153/card815.html",
    primary_source_type="青空文庫: 悲しき玩具",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: 自然主義・反自然主義小説補完（10件）
# ============================================================
add(**C, name_ja="国木田独歩『欺かざるの記』",
    name_en="Kunikida Doppo's Azamukazaru no Ki",
    name_original="欺かざるの記",
    period_key="明治文学期",
    definition="国木田独歩（1871-1908）の青年期日記（1893-97）で1908-09年に刊行。青年知識人の内面的真実探究の記録として、後の私小説的告白文学の重要な源泉となった、近代自我形成記録の古典。",
    background="独歩のキリスト教体験と青年期苦悩の自己記録。",
    development="田山花袋『蒲団』に始まる私小説的告白文学の精神的源流の一つを成した。",
    historical_context="明治20-30年代のキリスト教文学・自我形成期。",
    primary_source_url=AOZORA+"cards/000038/card44650.html",
    primary_source_type="青空文庫: 欺かざるの記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="国木田独歩『運命論者』",
    name_en="Kunikida Doppo's Unmeironja",
    name_original="運命論者",
    period_key="明治文学期",
    definition="国木田独歩が1903年に発表した短編小説。運命の偶然性と人間の宿命的関係を描き、自然主義以前の神秘的人生観を示した、独歩短編の代表作。",
    background="独歩の自然観・運命観と西欧文学の影響。",
    development="後の自然主義文学の人間観との対比的位置にある作品として参照された。",
    historical_context="明治30年代の人生観・運命論議期。",
    primary_source_url=AOZORA+"cards/000038/card1101.html",
    primary_source_type="青空文庫: 運命論者",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="田山花袋『生』",
    name_en="Tayama Katai's Sei",
    name_original="生",
    period_key="明治文学期",
    definition="田山花袋（1871-1930）が1908年に発表した家族小説三部作の第一作。家族の死と生を平淡な観察で描き、『蒲団』後の花袋自然主義の方法的展開を示した、自然主義家族小説の代表作。",
    background="『蒲団』(1907)後の花袋自然主義の組織的展開期。",
    development="続く『妻』『縁』とともに花袋自然主義家族三部作を構成した。",
    historical_context="明治末期の自然主義文学最盛期。",
    primary_source_url=AOZORA+"cards/001148/card54497.html",
    primary_source_type="青空文庫: 生",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="正宗白鳥『何処へ』",
    name_en="Masamune Hakuchō's Doko e",
    name_original="何処へ",
    period_key="明治文学期",
    definition="正宗白鳥（1879-1962）が1908年に発表した長編小説。青年知識人の人生方向探究と虚無感を冷徹な観察で描き、自然主義文学の代表作の一つとして評価された、白鳥自然主義の到達点。",
    background="日露戦争後の青年知識人の精神的閉塞と白鳥のキリスト教体験。",
    development="白鳥自然主義の方法を確立し、後の『泥人形』『土の香』へ展開した。",
    historical_context="明治末期の自然主義文学最盛期。",
    primary_source_url=AOZORA+"cards/001151/card46606.html",
    primary_source_type="青空文庫: 何処へ",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="徳田秋声『黴』",
    name_en="Tokuda Shūsei's Kabi",
    name_original="黴",
    period_key="明治文学期",
    definition="徳田秋声（1872-1943）が1911年に発表した長編小説。下層知識人の家庭生活を平淡に描き、自然主義の客観的観察を徹底した秋声リアリズムの代表作として、後年まで規範的位置を占めた。",
    background="尾崎紅葉門下から自然主義への秋声の方法的転換。",
    development="『あらくれ』『縮図』『仮装人物』へと展開する秋声リアリズムの起点。",
    historical_context="明治末期の自然主義成熟期。",
    primary_source_url=AOZORA+"cards/000161/card4727.html",
    primary_source_type="青空文庫: 黴",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="徳田秋声『あらくれ』",
    name_en="Tokuda Shūsei's Arakure",
    name_original="あらくれ",
    period_key="大正文学期",
    definition="徳田秋声が1915年に発表した長編小説。激しい性格の女主人公お島の生活変転を描き、自然主義リアリズムの女性主体把握において到達点を示した、大正初期秋声の代表作。",
    background="秋声リアリズムの方法的成熟と女性主体への関心深化。",
    development="後の『縮図』『仮装人物』への秋声リアリズム展開を準備した。",
    historical_context="大正初期のリアリズム文学成熟期。",
    primary_source_url=AOZORA+"cards/000161/card4759.html",
    primary_source_type="青空文庫: あらくれ",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="近松秋江『黒髪』",
    name_en="Chikamatsu Shūkō's Kurokami",
    name_original="黒髪",
    period_key="大正文学期",
    definition="近松秋江（1876-1944）が1922年から発表した短編連作。京都の女性との執着的恋愛を私小説的告白で描き、大正後期私小説の代表作の一つとして、執着の文学の極北を示した。",
    background="秋江の私的恋愛体験と私小説的告白方法の徹底。",
    development="私小説の執着系譜として、後の岩野泡鳴・葛西善蔵らに連なる位置を占めた。",
    historical_context="大正後期の私小説最盛期。",
    primary_source_url=AOZORA+"cards/000228/card53132.html",
    primary_source_type="青空文庫: 黒髪",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="岩野泡鳴『耽溺』",
    name_en="Iwano Hōmei's Tandeki",
    name_original="耽溺",
    period_key="明治文学期",
    definition="岩野泡鳴（1873-1920）が1909年に発表した短編小説。芸者との恋愛体験を一元描写法で描き、泡鳴流自然主義の方法的宣言となった、明治末私小説の代表作。",
    background="泡鳴の一元描写論と自然主義私小説の方法的徹底。",
    development="続く五部作『発展』『毒薬を飲む女』『放浪』『断橋』『憑き物』への展開を導いた。",
    historical_context="明治末期の自然主義最盛期。",
    primary_source_url=AOZORA+"cards/001242/card55125.html",
    primary_source_type="青空文庫: 耽溺",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="永井荷風『日和下駄』",
    name_en="Nagai Kafū's Hiyori Geta",
    name_original="日和下駄",
    period_key="大正文学期",
    definition="永井荷風（1879-1959）が1915年に刊行した東京散策エッセイ集。失われゆく江戸風俗と近代化東京の対比を散文で描き、荷風的東京美学の中核を成した、大正期都市散策文学の古典。",
    background="荷風の江戸文化への愛着と近代化批判的視座。",
    development="『断腸亭日乗』『江戸藝術論』へ連なる荷風東京美学の中軸を形成した。",
    historical_context="大正初期の東京近代化批判文学期。",
    primary_source_url=AOZORA+"cards/001341/card54100.html",
    primary_source_type="青空文庫: 日和下駄",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"都市風景の人類学",
         "description":"荷風『日和下駄』の都市散策は、人類学的都市観察と物質文化記録の文学的並行物。"}])

add(**C, name_ja="谷崎潤一郎『盲目物語』",
    name_en="Tanizaki Jun'ichirō's Mōmoku Monogatari",
    name_original="盲目物語",
    period_key="昭和戦前戦中期",
    definition="谷崎潤一郎（1886-1965）が1931年に発表した『盲目物語』は、お市の方に仕えた盲目の按摩の回想形式で戦国期女性美を語り、谷崎古典回帰期の女性美学を凝縮した中編。",
    background="谷崎関西移住後の古典回帰と女性美学の深化。",
    development="『春琴抄』『細雪』への谷崎古典美学の展開を準備した。",
    historical_context="昭和初期の谷崎古典回帰期。",
    primary_source_url=AOZORA+"cards/001383/card57052.html",
    primary_source_type="青空文庫: 盲目物語",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")


# ============================================================
# F: 大正評論・プロレタリア・女性表現（10件）
# ============================================================
add(**C, name_ja="平塚らいてう『元始女性は太陽であった』",
    name_en="Hiratsuka Raichō's In the Beginning Woman Was the Sun",
    name_original="元始、女性は太陽であった",
    period_key="大正文学期",
    definition="平塚らいてう（1886-1971）が1911年『青鞜』創刊号に発表した宣言文。女性の主体性回復を高唱し、近代日本女性解放運動と女性文学の出発点を画した、フェミニズム評論の古典。",
    background="青鞜社結成と明治末期女性解放運動の高揚。",
    development="与謝野晶子・伊藤野枝・山川菊栄ら大正期女性論者に直接影響した。",
    historical_context="明治末・大正初期の女性解放運動勃興期。",
    primary_source_url=AOZORA+"cards/000058/card46479.html",
    primary_source_type="青空文庫: 元始、女性は太陽であった",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"平塚の女性主体宣言は、AI時代の主体性概念再考の歴史的参照点となる。",
         "related_ai_phenomenon":"AIと主体性の歴史的構築"}])

add(**C, name_ja="与謝野晶子『一隅より』",
    name_en="Yosano Akiko's Ichigū yori",
    name_original="一隅より",
    period_key="大正文学期",
    definition="与謝野晶子が1911年に刊行した最初の評論集。女性論・教育論・社会論を縦横に展開し、平塚らいてう『青鞜』と並ぶ大正期女性評論の双璧を成した、晶子社会評論の代表作。",
    background="与謝野晶子の創作から評論への活動拡大期。",
    development="後の『若き友へ』『人間礼拝』への晶子社会評論の展開を準備した。",
    historical_context="大正初期の女性社会評論勃興期。",
    primary_source_url=AOZORA+"cards/000885/card3270.html",
    primary_source_type="青空文庫: 一隅より",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="福田英子『妾の半生涯』",
    name_en="Fukuda Hideko's Warawa no Hanseigai",
    name_original="妾の半生涯",
    period_key="明治文学期",
    definition="福田英子（1865-1927）が1904年に刊行した自伝。自由民権運動から大阪事件、社会主義運動への半生を女性の視点で記録した、明治期女性自伝の代表作。",
    background="自由民権運動と明治社会主義運動の女性経験。",
    development="後の女性自伝・回想記の祖型として、平塚らいてう自伝などに影響した。",
    historical_context="明治末期の女性社会運動回顧期。",
    primary_source_url=AOZORA+"cards/000156/card46556.html",
    primary_source_type="青空文庫: 妾の半生涯",
    importance_score=3, source_tier="primary", canonical_in_region="marginal")

add(**C, name_ja="小林多喜二『蟹工船』",
    name_en="Kobayashi Takiji's Kanikōsen",
    name_original="蟹工船",
    period_key="昭和戦前戦中期",
    definition="小林多喜二（1903-1933）が1929年に発表した中編小説。北洋蟹工船での労働者搾取と階級闘争意識覚醒を描き、日本プロレタリア文学の最高傑作として国際的に翻訳された。",
    background="昭和初期の労働運動激化と日本プロレタリア文学運動の興隆。",
    development="多喜二の代表作として戦後・21世紀にも繰り返し読み継がれた。",
    historical_context="昭和初期の労働運動・治安維持法体制下のプロレタリア文学。",
    primary_source_url=AOZORA+"cards/000156/card1465.html",
    primary_source_type="青空文庫: 蟹工船",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"MG","link_type":"shared_concept",
         "target_entity_name":"資本主義労働搾取批判",
         "description":"『蟹工船』の労働搾取描写は、経営学的労働関係論の文学的並行物として参照される。"}])

add(**C, name_ja="小林多喜二『党生活者』",
    name_en="Kobayashi Takiji's Tōseikatsusha",
    name_original="党生活者",
    period_key="昭和戦前戦中期",
    definition="小林多喜二が1932-33年に執筆した中編小説（没後刊行）。非合法共産党員の地下生活を描き、検挙・拷問死直前の多喜二プロレタリア文学の精神的遺書となった、戦前左翼文学の頂点。",
    background="特高警察による共産党弾圧と多喜二の地下活動期。",
    development="戦後プロレタリア文学再評価の中核作品となった。",
    historical_context="昭和初期の治安維持法体制下の地下活動期。",
    primary_source_url=AOZORA+"cards/000156/card1652.html",
    primary_source_type="青空文庫: 党生活者",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="葉山嘉樹『海に生くる人々』",
    name_en="Hayama Yoshiki's Umi ni Ikuru Hitobito",
    name_original="海に生くる人々",
    period_key="大正文学期",
    definition="葉山嘉樹（1894-1945）が1926年に発表した長編小説。石炭運搬船の過酷な労働とストライキを描き、日本プロレタリア文学初期の代表作として、多喜二『蟹工船』に先行する位置を占めた。",
    background="大正後期の労働運動とプロレタリア文芸雑誌『文芸戦線』活動。",
    development="日本プロレタリア文学の方向性を確立し、小林多喜二へ継承された。",
    historical_context="大正末期のプロレタリア文学運動勃興期。",
    primary_source_url=AOZORA+"cards/001220/card55092.html",
    primary_source_type="青空文庫: 海に生くる人々",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="徳永直『太陽のない街』",
    name_en="Tokunaga Sunao's Taiyō no nai Machi",
    name_original="太陽のない街",
    period_key="昭和戦前戦中期",
    definition="徳永直（1899-1958）が1929年に発表した長編小説。共同印刷争議を題材に労働者集団の闘争を描き、日本プロレタリア文学の代表作の一つとなった、労働者文学の典型的成果。",
    background="昭和初期の労働争議激化とプロレタリア作家自身の労働者出自。",
    development="戦前プロレタリア文学の成果として戦後も繰り返し読み継がれた。",
    historical_context="昭和初期の労働運動最盛期。",
    primary_source_url=AOZORA+"cards/000051/card4760.html",
    primary_source_type="青空文庫: 太陽のない街",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="中野重治『村の家』",
    name_en="Nakano Shigeharu's Mura no Ie",
    name_original="村の家",
    period_key="昭和戦前戦中期",
    definition="中野重治（1902-1979）が1935年に発表した中編小説。獄中転向後に帰郷した青年と父との対話を通じ、転向問題を内省的に描いた、転向文学の最高峰。",
    background="昭和8年の中野転向と転向文学運動の発生。",
    development="戦後民主主義文学・新日本文学運動の精神的礎石となった。",
    historical_context="昭和初期の転向問題と思想的試練期。",
    primary_source_url=AOZORA+"cards/000158/card46494.html",
    primary_source_type="青空文庫: 村の家",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="林芙美子『放浪記』",
    name_en="Hayashi Fumiko's Hōrōki",
    name_original="放浪記",
    period_key="昭和戦前戦中期",
    definition="林芙美子（1903-1951）が1928-30年に発表した自伝的小説。下層女性の貧困と放浪生活を口語的日記体で描き、昭和初期女性文学のベストセラーとして商業的・文学的成功を収めた、女性私小説の古典。",
    background="林芙美子の貧困・放浪体験と都市下層女性の文学的表現。",
    development="芙美子の出世作となり、戦後『晩菊』『浮雲』へ続く女性文学の起点となった。",
    historical_context="昭和初期の都市下層女性文学勃興期。",
    primary_source_url=AOZORA+"cards/000291/card2354.html",
    primary_source_type="青空文庫: 放浪記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"芙美子の下層女性主体表現は、AI時代の周縁的主体表象の歴史的参照点。",
         "related_ai_phenomenon":"AIと女性的主体表象の系譜"}])

add(**C, name_ja="林芙美子『晩菊』",
    name_en="Hayashi Fumiko's Bangiku",
    name_original="晩菊",
    period_key="昭和戦前戦中期",
    definition="林芙美子が1948年に発表した短編小説（女性文学賞受賞作）。元芸者の老女と元恋人の再会を描き、戦後芙美子文学の精神的成熟を示した、戦後女性文学の代表作。",
    background="戦後の芙美子の精神的成熟と短編美学の深化。",
    development="『浮雲』への戦後芙美子文学の展開を準備した。",
    historical_context="戦後初期の女性文学再生期。",
    primary_source_url=AOZORA+"cards/000291/card4683.html",
    primary_source_type="青空文庫: 晩菊",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# Cross-domain bridges (additional, ensure >= 12)
# ============================================================
def attach_cross(name, target_db, link_type, target_name, desc):
    for c in CONCEPTS:
        if c["name_ja"] == name:
            c.setdefault("cross_domain", []).append(
                {"target_db": target_db, "link_type": link_type,
                 "target_entity_name": target_name, "description": desc})
            return

attach_cross("矢野龍渓『経国美談』", "AN", "shared_concept",
             "明治民権運動と古代史寓意",
             "古代テーバイ史に民権理想を寓意化する手法は、人類学的歴史記憶の政治的活用の事例。")
attach_cross("黒岩涙香『巌窟王』翻案", "MG", "shared_concept",
             "翻案出版と新聞メディア経済",
             "涙香翻案の新聞連載は近代出版経済とメディア企業経営の文学的接点。")
attach_cross("内村鑑三『代表的日本人』", "AN", "shared_concept",
             "明治日本の文化的他者表象",
             "代表的日本人の選定は文化的アイデンティティ構築の人類学的事例。")
attach_cross("上田敏訳『海潮音』", "AN", "shared_concept",
             "翻訳と詩的言語の通文化形成",
             "西欧象徴詩翻訳は、人類学的言語接触と詩語の通文化形成過程の文学的記録。")
attach_cross("小林多喜二『党生活者』", "MG", "shared_concept",
             "資本主義と労働者組織化",
             "党生活者描写は経営学的労働組織論の戦前期文学的鏡像。")
attach_cross("徳永直『太陽のない街』", "MG", "shared_concept",
             "労働争議と企業経営",
             "共同印刷争議題材は経営学的労使関係論の文学的並行記録。")
attach_cross("平塚らいてう『元始女性は太陽であった』", "MG", "shared_concept",
             "ジェンダーと組織主体",
             "女性主体宣言は経営学的ジェンダー論の歴史的源流の一つ。")
attach_cross("林芙美子『放浪記』", "AN", "shared_concept",
             "下層女性のライフコース",
             "放浪体験記は人類学的下層女性ライフコース研究の文学的並行物。")
attach_cross("田山花袋『生』", "AN", "shared_concept",
             "近代家族の解体観察",
             "家族三部作は人類学的近代家族変容の文学的観察記録。")
attach_cross("永井荷風『日和下駄』", "MG", "shared_concept",
             "近代化都市と消費景観",
             "東京散策記は経営学的都市消費景観論の文学的先駆。")
attach_cross("葉山嘉樹『海に生くる人々』", "MG", "shared_concept",
             "海洋労働と資本搾取",
             "石炭運搬船描写は経営学的海洋労働組織論の文学的並行物。")
attach_cross("中野重治『村の家』", "AN", "shared_concept",
             "転向と地域共同体回帰",
             "転向後帰郷は人類学的地域共同体と個人の再接合の文学的事例。")


# ============================================================
# fourth_transform additional tags
# ============================================================
def attach_fourth(name, axis, status, rationale, ai_phen):
    for c in CONCEPTS:
        if c["name_ja"] == name:
            c.setdefault("fourth_axes", []).append(
                {"axis": axis, "status": status,
                 "rationale": rationale, "related_ai_phenomenon": ai_phen})
            return

attach_fourth("仮名垣魯文『安愚楽鍋』", "言語", "rethinking",
              "戯作的口語の風俗観察記録は、AIによる時代風俗テキスト生成の歴史的参照点。",
              "AI生成と時代風俗テクスト")
attach_fourth("矢野龍渓『経国美談』", "作者性", "rethinking",
              "政治啓蒙小説の作者性は、AI生成政治テクストの作者責任問題の歴史的源流。",
              "AI政治テクストの作者性")
attach_fourth("末広鉄腸『雪中梅』", "創造性", "rethinking",
              "政治小説ジャンルは、AI時代の政治的物語生成の歴史的祖型。",
              "AI政治物語ジャンル")
attach_fourth("東海散士『佳人之奇遇』", "言語", "rethinking",
              "漢文調テクストは、AI多言語生成における文体史の参照点。",
              "AI多文体生成")
attach_fourth("黒岩涙香『噫無情』翻案", "翻訳", "rethinking",
              "翻案小説は、AI翻訳と翻案の歴史的参照点となる。",
              "AI翻訳・翻案の歴史性")
attach_fourth("三遊亭円朝『塩原多助一代記』", "言語", "rethinking",
              "速記本口承テクストは、AI音声テキスト変換の歴史的参照点。",
              "AI音声テクスト変換")
attach_fourth("山田美妙『武蔵野』", "言語", "rethinking",
              "敬体言文一致体は、AI敬語生成の歴史的源流。",
              "AI敬語生成")
attach_fourth("言文一致体論争", "言語", "rethinking",
              "文体規範論争は、AI生成テクストの文体規範問題の歴史的鏡像。",
              "AI文体規範")
attach_fourth("高山樗牛『日本主義』", "作者性", "rethinking",
              "ナショナリズム評論は、AI生成評論の文化的偏向問題の歴史的源流。",
              "AI評論の文化的偏向")
attach_fourth("新渡戸稲造『武士道』", "翻訳", "rethinking",
              "英文文化論は、AIによる文化翻訳の歴史的参照点。",
              "AI文化翻訳")
attach_fourth("与謝野晶子『恋衣』", "主体", "rethinking",
              "反戦女性主体は、AI時代の主体的反戦表現の歴史的源流。",
              "AI時代の反戦主体")
attach_fourth("斎藤茂吉『あらたま』", "言語", "rethinking",
              "写生短歌は、AI生成短歌の規範性問題の歴史的参照点。",
              "AI生成短歌の規範性")
attach_fourth("石川啄木『悲しき玩具』詳説", "創造性", "rethinking",
              "口語三行短歌は、AI形式実験生成の歴史的源流。",
              "AI形式実験生成")
attach_fourth("徳田秋声『あらくれ』", "主体", "rethinking",
              "強い女性主体描写は、AI生成女性主体の歴史的参照点。",
              "AI女性主体表象")
attach_fourth("永井荷風『日和下駄』", "言語", "rethinking",
              "都市散策エッセイは、AI都市記述生成の歴史的源流。",
              "AI都市記述生成")
attach_fourth("小林多喜二『蟹工船』", "創造性", "rethinking",
              "プロレタリア文学は、AI時代の階級表現再考の歴史的参照点。",
              "AI時代の階級表現")
attach_fourth("中野重治『村の家』", "主体", "rethinking",
              "転向主体描写は、AI生成における信念変動の主体性問題の歴史的源流。",
              "AI主体の信念変動")
attach_fourth("林芙美子『晩菊』", "主体", "rethinking",
              "晩年女性主体は、AI生成における年齢表象問題の歴史的参照点。",
              "AI生成と高齢女性表象")


def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="日本",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid

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
                    print(f"  [warn] fourth tag {entry['name_ja']}: {e}")
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
                    print(f"  [warn] cross_domain {entry['name_ja']}: {e}")

        summary = db.progress_summary()
        print(f"[wave19 c18 add60] inserted: {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave19 c18 add60] fourth +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
