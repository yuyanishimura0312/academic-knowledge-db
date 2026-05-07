"""LIT-DB Phase 2 Wave 16 — C18: Japanese Modern Literature ADD 50 concepts.

Subfield: lit_jp_modern (id=11), region='日本'.
Existing 110 → target 500. Adds 50 NEW non-overlapping concepts covering:
  A: 詩歌補完 (近代詩・短歌・俳句) — 15
  B: 戦後詩 — 9
  C: 評論 — 7
  D: 戯曲 — 10
  E: 児童文学 — 9
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("明治文学期", "Meiji Literature", 1868, 1912,
     "明治維新から大正改元までの近代日本文学形成期。"),
    ("大正文学期", "Taishō Literature", 1912, 1926,
     "大正改元から昭和改元までの文学期。白樺派、新思潮派、耽美派、新感覚派が並行展開した。"),
    ("昭和戦前戦中期", "Early Shōwa & Wartime", 1926, 1945,
     "昭和改元から敗戦までの文学期。プロレタリア文学、モダニズム、戦時文学。"),
    ("戦後文学期", "Postwar Literature", 1945, 1970,
     "敗戦後の文学的再出発期。戦後派、第三の新人、内向の世代。"),
    ("現代文学期", "Contemporary Japanese Literature", 1970, 2026,
     "高度経済成長後期から平成・令和に至る現代日本文学期。"),
]


AOZORA = "https://www.aozora.gr.jp/"
NDL = "https://dl.ndl.go.jp/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
BRITT = "https://www.britannica.com/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_jp_modern", region="日本",
         original_script="japanese")


# ============================================================
# A: 詩歌補完 — 近代詩・短歌・俳句（15件）
# ============================================================
add(**C, name_ja="北原白秋『邪宗門』",
    name_en="Kitahara Hakushū's Jashūmon",
    name_original="邪宗門",
    period_key="明治文学期",
    definition="北原白秋（1885-1942）が1909年に刊行した第一詩集。キリシタン異国情緒と南蛮文化を主題に、官能的・象徴主義的詩風を確立した。明治末期象徴詩の頂点的成果。",
    background="フランス象徴詩・パンの会の活動と九州柳川出身の異国趣味。",
    development="後の『思ひ出』『東京景物詩』を含む白秋詩業の出発点。三木露風と並ぶ白露時代を成した。",
    historical_context="明治40年代の象徴主義詩運動と耽美派文学の興隆期。",
    primary_source_url=AOZORA+"index_pages/person106.html",
    primary_source_type="青空文庫: 北原白秋",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="北原白秋『桐の花』",
    name_en="Kitahara Hakushū's Kiri no Hana",
    name_original="桐の花",
    period_key="大正文学期",
    definition="北原白秋が1913年に刊行した第一歌集。近代叙情を口語的感覚で表現し、「冬の朝」「酒場」など都会的な近代短歌を確立。明星派以後の新風を切り拓いた。",
    background="俊子事件（姦通罪）を経た情念の詩的昇華。",
    development="近代短歌の口語化・近代化の先駆として、後の短歌革新に道を開いた。",
    historical_context="大正初期の短歌革新運動と、西欧近代詩の影響下にある詩歌再編期。",
    primary_source_url=AOZORA+"index_pages/person106.html",
    primary_source_type="青空文庫: 北原白秋",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="萩原朔太郎『月に吠える』",
    name_en="Hagiwara Sakutarō's Tsuki ni Hoeru",
    name_original="月に吠える",
    period_key="大正文学期",
    definition="萩原朔太郎（1886-1942）が1917年に刊行した第一詩集。神経症的不安と近代的孤独を口語自由詩で表現し、「日本近代詩の確立者」と位置づけられる画期的詩集。",
    background="室生犀星との交流、詩誌『感情』創刊、ポー・ボードレール受容。",
    development="日本近代詩の決定的転換点となり、後の昭和詩のすべての出発点となった。",
    historical_context="大正中期の口語自由詩運動と、近代主体の不安の文学的問題化。",
    primary_source_url=AOZORA+"cards/000067/card832.html",
    primary_source_type="青空文庫: 月に吠える",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"朔太郎の神経症的主体表現は、AI時代の不安・心的状態の言語化を再考する祖型となる。",
         "related_ai_phenomenon":"AI時代の主体的情動の言語化"}])

add(**C, name_ja="萩原朔太郎『青猫』",
    name_en="Hagiwara Sakutarō's Aoneko",
    name_original="青猫",
    period_key="大正文学期",
    definition="萩原朔太郎が1923年に刊行した第二詩集。倦怠・憂鬱・幻想的虚無を彷徨する都市的近代精神を、流麗な口語自由詩で表現。『月に吠える』と並ぶ朔太郎の代表作。",
    background="関東大震災前後の都市的不安と西欧モダニズムの吸収。",
    development="昭和モダニズム詩への直接的橋渡しとして、戦後詩までの系譜を形成した。",
    historical_context="大正末期の都市文化成熟と、近代精神の倦怠の表現問題化。",
    primary_source_url=AOZORA+"cards/000067/card1853.html",
    primary_source_type="青空文庫: 青猫",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="室生犀星『抒情小曲集』",
    name_en="Murō Saisei's Jojō Shōkyokushū",
    name_original="抒情小曲集",
    period_key="大正文学期",
    definition="室生犀星（1889-1962）が1918年に刊行した第一詩集。「ふるさとは遠きにありて思ふもの」で知られる望郷詩を含み、口語自由詩による近代叙情の規範を確立した。",
    background="金沢の貧困な養家での少年期体験と、萩原朔太郎との詩的交流。",
    development="近代叙情詩の規範として、戦後の谷川俊太郎・茨木のり子に至る系譜を形成した。",
    historical_context="大正中期の口語自由詩確立期と、地方出身詩人の文学的台頭。",
    primary_source_url=AOZORA+"cards/001579/card53202.html",
    primary_source_type="青空文庫: 抒情小曲集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="高村光太郎『道程』",
    name_en="Takamura Kōtarō's Dōtei",
    name_original="道程",
    period_key="大正文学期",
    definition="高村光太郎（1883-1956）が1914年に刊行した第一詩集。「僕の前に道はない／僕の後ろに道は出来る」で知られる表題作を含み、近代主体の自我宣言を口語詩で表現した。",
    background="欧米留学体験（1906-09）と「パンの会」「白樺」誌での活動。",
    development="近代日本詩における自立的主体の宣言として、戦後詩まで影響を与え続けた。",
    historical_context="大正初期の自我意識の文学的確立と、口語自由詩運動の本格化。",
    primary_source_url=AOZORA+"cards/000050/card1718.html",
    primary_source_type="青空文庫: 道程",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="高村光太_郎『智恵子抄』",
    name_en="Takamura Kōtarō's Chieko-shō",
    name_original="智恵子抄",
    period_key="昭和戦前戦中期",
    definition="高村光太郎が1941年に刊行した詩集。精神を病み1938年に亡くなった妻智恵子への愛情と挽歌を収め、近代日本詩における夫婦愛の最も純粋な表現として読み継がれる。",
    background="妻長沼智恵子の精神病罹患（1931頃）と死、戦時下の精神的支柱としての回想。",
    development="戦後も広く読まれ続け、近代抒情詩の到達点として教科書的地位を獲得した。",
    historical_context="戦時下の文学統制期に、私的愛情を主題とした詩集が広く受容された特異な事例。",
    primary_source_url=AOZORA+"cards/000050/card51687.html",
    primary_source_type="青空文庫: 智恵子抄",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="三好達治『測量船』",
    name_en="Miyoshi Tatsuji's Sokuryōsen",
    name_original="測量船",
    period_key="昭和戦前戦中期",
    definition="三好達治（1900-1964）が1930年に刊行した第一詩集。「太郎を眠らせ、太郎の屋根に雪ふりつむ」で知られ、文語と口語、伝統的叙情と近代的感覚を融合した昭和詩の規範作。",
    background="第三高等学校・東京帝大仏文科でのフランス詩学吸収、『四季』派の中核。",
    development="戦前戦後を通じて広く読まれ、戦後の中野重治・伊東静雄らとの『四季』派抒情の核となった。",
    historical_context="昭和初期のモダニズムと伝統回帰が交錯した詩運動の中核期。",
    primary_source_url=AOZORA+"cards/001872/card57822.html",
    primary_source_type="青空文庫: 三好達治",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="中原中也『山羊の歌』",
    name_en="Nakahara Chūya's Yagi no Uta",
    name_original="山羊の歌",
    period_key="昭和戦前戦中期",
    definition="中原中也（1907-1937）が1934年に刊行した第一詩集。「汚れつちまつた悲しみに」など内省的悲哀のリリシズムを口語七五調で表現し、青年的孤独の象徴的詩人像を確立した。",
    background="ダダ・ランボー受容、長男文也の死、小林秀雄・大岡昇平との交友。",
    development="夭逝詩人の伝説とともに戦後広く愛され、現代まで青年読者層の支持を集める。",
    historical_context="昭和初期の都市青年の精神的不安と、文壇外の独自詩風の台頭。",
    primary_source_url=AOZORA+"cards/000026/card3491.html",
    primary_source_type="青空文庫: 山羊の歌",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="草野心平『第百階級』",
    name_en="Kusano Shinpei's Daihyaku Kaikyū",
    name_original="第百階級",
    period_key="昭和戦前戦中期",
    definition="草野心平（1903-1988）が1928年に刊行した第二詩集。蛙を詩的主題とする独自の世界を切り拓き、生命賛歌と擬声語表現で近代詩に新領域を開いた。",
    background="中国留学体験と『銅鑼』『歴程』創刊を通じた文学的国際性。",
    development="蛙の詩人として戦後も活躍し、宮沢賢治発掘・顕彰にも貢献した。",
    historical_context="昭和初期のプロレタリア文学とモダニズムの間で独自路線を歩んだ詩人の登場。",
    primary_source_url=WIKI_JA+"%E8%8D%89%E9%87%8E%E5%BF%83%E5%B9%B3",
    primary_source_type="Wikipedia: 草野心平",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="西脇順三郎『AMBARVALIA』",
    name_en="Nishiwaki Junzaburō's Ambarvalia",
    name_original="アムバルワリア",
    period_key="昭和戦前戦中期",
    definition="西脇順三郎（1894-1982）が1933年に刊行した第一詩集。古代ローマの祭祀名を表題とし、シュルレアリスム・モダニズムと古典学知を融合した知性的詩風を確立した。",
    background="オックスフォード留学（1922-25）でのモダニズム詩学吸収と古典文献学研究。",
    development="日本モダニズム詩の頂点として、戦後の鮎川信夫・吉岡実ら『荒地』派に影響を与えた。",
    historical_context="昭和初期のモダニズム運動と西欧前衛詩学の本格的受容期。",
    primary_source_url=WIKI_JA+"%E8%A5%BF%E8%84%87%E9%A0%86%E4%B8%89%E9%83%8E",
    primary_source_type="Wikipedia: 西脇順三郎",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="宮沢賢治『春と修羅』",
    name_en="Miyazawa Kenji's Haru to Shura",
    name_original="春と修羅",
    period_key="大正文学期",
    definition="宮沢賢治（1896-1933）が1924年に自費出版した唯一の生前刊行詩集。「心象スケッチ」と称する独自の宇宙論的詩世界を展開し、近代詩史上類例のない神秘的・科学的・宗教的統合を成した。",
    background="法華経への帰依、岩手県花巻の自然・農業体験、近代科学知識の吸収。",
    development="生前は無名のまま没後発見され、戦後広範な読者を獲得し続ける国民詩人となった。",
    historical_context="大正末期の宗教的精神主義と科学的世界観が並存した知的環境。",
    primary_source_url=AOZORA+"cards/000081/card1058.html",
    primary_source_type="青空文庫: 春と修羅",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"宇宙論的精神世界",
         "description":"賢治の「心象スケッチ」は、人類学的世界観研究における日本近代の宇宙論的想像力の中核事例。"}])

add(**C, name_ja="宮沢賢治『銀河鉄道の夜』",
    name_en="Miyazawa Kenji's Ginga Tetsudō no Yoru",
    name_original="銀河鉄道の夜",
    period_key="昭和戦前戦中期",
    definition="宮沢賢治が1924-31年頃に書き継いだ未完の長編童話。少年ジョバンニとカムパネルラの銀河旅行を通じて、自己犠牲・友情・宗教的救済の主題を象徴的に展開した賢治童話の最高峰。",
    background="妹トシの死(1922)による弔慰の文学的昇華と法華経思想。",
    development="戦後アニメ化・映像化を経て、日本児童文学・幻想文学の規範作品として広く受容された。",
    historical_context="昭和初期の童話・児童文学と宗教的想像力の融合期。",
    primary_source_url=AOZORA+"cards/000081/card456.html",
    primary_source_type="青空文庫: 銀河鉄道の夜",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="石川啄木『一握の砂』",
    name_en="Ishikawa Takuboku's Ichiaku no Suna",
    name_original="一握の砂",
    period_key="明治文学期",
    definition="石川啄木（1886-1912）が1910年に刊行した歌集。三行書き短歌551首を収め、生活実感と社会意識を口語的に詠み込み、近代短歌の革新者として位置づけられる。",
    background="盛岡中学退学・北海道流転・東京での貧困生活、社会主義思想接近。",
    development="近代短歌の口語化・社会派化の起点となり、戦後の現代短歌に至る系譜を切り拓いた。",
    historical_context="明治末期の社会主義運動勃興（大逆事件1910）と歌壇革新の同時進行期。",
    primary_source_url=AOZORA+"cards/000153/card815.html",
    primary_source_type="青空文庫: 一握の砂",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"啄木の生活実感短歌は、近代主体の経済的・社会的位相を歌に内在化した。AI時代の主体性の社会的位相再考の祖型。",
         "related_ai_phenomenon":"AI時代の主体性の社会的位相"}])

add(**C, name_ja="石川啄木『悲しき玩具』",
    name_en="Ishikawa Takuboku's Kanashiki Gangu",
    name_original="悲しき玩具",
    period_key="明治文学期",
    definition="石川啄木の死後1912年に刊行された遺稿歌集。病臥中の生活と死の自覚を詠んだ194首を収録。『一握の砂』を継ぎ、より内省的・社会的な近代短歌の到達を示した。",
    background="肺結核との闘病、母・妻の発病、貧困と社会主義への共感。",
    development="近代短歌の最深部として後世に決定的影響を与え、土岐善麿・茂吉らへの橋渡しとなった。",
    historical_context="明治末期の社会主義弾圧期と、短歌における社会意識の文学的問題化。",
    primary_source_url=AOZORA+"cards/000153/card816.html",
    primary_source_type="青空文庫: 悲しき玩具",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="与謝野晶子『みだれ髪』",
    name_en="Yosano Akiko's Midaregami",
    name_original="みだれ髪",
    period_key="明治文学期",
    definition="与謝野晶子（1878-1942）が1901年に刊行した第一歌集。官能と情熱を奔放に詠う399首を収め、「やは肌のあつき血汐にふれも見でさびしからずや道を説く君」など近代女性歌の出発点を成した。",
    background="鉄幹との恋愛と新詩社結成、西欧ロマン主義の受容。",
    development="明治女性表現の文学的解放として、後の女性短歌・女性文学全体に決定的影響を与えた。",
    historical_context="明治30年代の浪漫主義運動と、女性主体の文学的成立期。",
    primary_source_url=AOZORA+"cards/000885/card3268.html",
    primary_source_type="青空文庫: みだれ髪",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"近代女性主体",
         "description":"晶子のみだれ髪は近代日本における女性主体の文学的成立を示す中核事例。"}])

add(**C, name_ja="斎藤茂吉『赤光』",
    name_en="Saitō Mokichi's Shakkō",
    name_original="赤光",
    period_key="大正文学期",
    definition="斎藤茂吉（1882-1953）が1913年に刊行した第一歌集。「死にたまふ母」連作で知られる近代写生短歌の頂点。アララギ派の中心として伊藤左千夫の写生説を深化させた。",
    background="伊藤左千夫門下入門、医学修業、母の死(1913)体験。",
    development="アララギ派写生短歌の規範として戦後まで圧倒的影響力を持ち続けた。",
    historical_context="大正初期の短歌におけるアララギ派と新詩社の対立構図の中で写生派の確立期。",
    primary_source_url=AOZORA+"cards/001225/card46451.html",
    primary_source_type="青空文庫: 赤光",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# B: 戦後詩（9件）
# ============================================================
add(**C, name_ja="鮎川信夫『戦中手記』",
    name_en="Ayukawa Nobuo's Senchū Shuki",
    name_original="戦中手記",
    period_key="戦後文学期",
    definition="鮎川信夫（1920-1986）の戦中・戦後の詩的思索を集成したテクスト群。『荒地』派の中心人物として、戦争体験の精神史を詩と批評の両面で展開した。「死んだ男」など戦後詩の規範作を含む。",
    background="戦中の従軍体験、田村隆一・北村太郎ら『荒地』同人との結成。",
    development="戦後詩『荒地』派の理論的指導者として、現代詩の方向を決定づけた。",
    historical_context="敗戦直後の精神的廃墟と、詩による戦後再出発の試行期。",
    primary_source_url=WIKI_JA+"%E9%AE%8E%E5%B7%9D%E4%BF%A1%E5%A4%AB",
    primary_source_type="Wikipedia: 鮎川信夫",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="田村隆一『四千の日と夜』",
    name_en="Tamura Ryūichi's Shisen no Hi to Yoru",
    name_original="四千の日と夜",
    period_key="戦後文学期",
    definition="田村隆一（1923-1998）が1956年に刊行した第一詩集。戦後10年の沈黙を経て発表された、戦争体験と虚無の詩的形象化として、『荒地』派戦後詩の象徴的成果。",
    background="戦中徴兵・敗戦体験と、鮎川信夫らとの『荒地』創刊（1947）。",
    development="戦後詩の倫理的標準として、谷川俊太郎以降の現代詩全体に基準を提供した。",
    historical_context="高度経済成長前夜、戦後文化的再編期の詩的応答。",
    primary_source_url=WIKI_JA+"%E7%94%B0%E6%9D%91%E9%9A%86%E4%B8%80",
    primary_source_type="Wikipedia: 田村隆一",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="黒田三郎『ひとりの女に』",
    name_en="Kuroda Saburō's Hitori no Onna ni",
    name_original="ひとりの女に",
    period_key="戦後文学期",
    definition="黒田三郎（1919-1980）が1954年に刊行した詩集。日常言語と戦後生活意識を密着させ、『荒地』派の中で最も平明な抒情を展開した代表作。",
    background="『荒地』同人としての活動と、戦後の市民生活体験。",
    development="戦後詩の平明化路線として、谷川俊太郎・茨木のり子の市民派抒情に道を開いた。",
    historical_context="戦後復興期の市民意識の文学的形成期。",
    primary_source_url=WIKI_JA+"%E9%BB%92%E7%94%B0%E4%B8%89%E9%83%8E",
    primary_source_type="Wikipedia: 黒田三郎",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="石原吉郎『サンチョ・パンサの帰郷』",
    name_en="Ishihara Yoshirō's Sancho Pansa no Kikyō",
    name_original="サンチョ・パンサの帰郷",
    period_key="戦後文学期",
    definition="石原吉郎（1915-1977）が1963年に刊行した第一詩集。シベリア抑留8年の極限体験を凝縮した詩語で、戦後詩のもう一つの頂点を成した。沈黙と抑制の詩学を確立。",
    background="シベリア抑留体験(1945-53)と帰国後の長い沈黙期。",
    development="戦後詩における極限体験の文学的形象化として、現代詩の方法論的基準となった。",
    historical_context="高度経済成長期の繁栄と影で進行した戦争体験の文学的問い直し。",
    primary_source_url=WIKI_JA+"%E7%9F%B3%E5%8E%9F%E5%90%89%E9%83%8E",
    primary_source_type="Wikipedia: 石原吉郎",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"石原の沈黙の詩学は、極限体験における主体の言語的限界を問う。AI時代の主体表現の限界と関連する。",
         "related_ai_phenomenon":"AI時代の主体表現の限界"}])

add(**C, name_ja="吉岡実『紡錘形』",
    name_en="Yoshioka Minoru's Bōsuikei",
    name_original="紡錘形",
    period_key="戦後文学期",
    definition="吉岡実（1919-1990）が1962年に刊行した詩集。シュルレアリスム的イメージと身体性を融合した独自の前衛詩風を確立し、戦後現代詩のもう一つの到達点を成した。",
    background="西脇順三郎の影響と『鰐』同人としての前衛活動。",
    development="戦後前衛詩の頂点として、現代詩・実験詩の系譜に決定的影響を与えた。",
    historical_context="戦後高度経済成長期の前衛芸術運動と詩の実験的展開期。",
    primary_source_url=WIKI_JA+"%E5%90%89%E5%B2%A1%E5%AE%9F",
    primary_source_type="Wikipedia: 吉岡実",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="大岡信『記号の森』",
    name_en="Ōoka Makoto's Kigō no Mori",
    name_original="記号の森",
    period_key="現代文学期",
    definition="大岡信（1931-2017）が1976年頃発表した詩的・批評的展開。連歌・連句と現代詩を結ぶ「うたげと孤心」の詩学を実践し、戦後詩から現代詩への橋渡しを成した。",
    background="戦後派詩運動と古典文学への回帰志向の融合。",
    development="戦後詩の古典統合という独自路線で、現代詩の方法的選択肢を拡げた。",
    historical_context="1970年代の高度経済成長後期、伝統文化の再評価期。",
    primary_source_url=WIKI_JA+"%E5%A4%A7%E5%B2%A1%E4%BF%A1",
    primary_source_type="Wikipedia: 大岡信",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="谷川俊太郎『二十億光年の孤独』",
    name_en="Tanikawa Shuntarō's Nijūoku Kōnen no Kodoku",
    name_original="二十億光年の孤独",
    period_key="戦後文学期",
    definition="谷川俊太郎（1931-2024）が1952年に刊行した第一詩集。21歳でのデビュー作にして、宇宙的スケールと日常的孤独を融合した戦後現代詩の出発点。父谷川徹三の知人三好達治の序文付き。",
    background="父・哲学者谷川徹三の知的環境と、戦後新世代の精神的出発。",
    development="戦後最も広く読まれた詩人として、現代日本の市民的詩文化を確立した。",
    historical_context="戦後復興期の若い世代による平明な詩語による近代精神の継承期。",
    primary_source_url=WIKI_JA+"%E8%B0%B7%E5%B7%9D%E4%BF%8A%E5%A4%AA%E9%83%8E",
    primary_source_type="Wikipedia: 谷川俊太郎",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="茨木のり子『わたしが一番きれいだったとき』",
    name_en="Ibaragi Noriko's Watashi ga Ichiban Kirei Datta Toki",
    name_original="わたしが一番きれいだったとき",
    period_key="戦後文学期",
    definition="茨木のり子（1926-2006）が1958年詩集『見えない配達夫』に収めた代表詩。戦争に青春を奪われた女性世代の経験を、平明な口語で結晶化した戦後詩の規範作。",
    background="戦中の女学生体験、川崎洋らとの『櫂』創刊(1953)。",
    development="戦後女性詩の象徴的成果として、教科書教材を通じて広く読まれ続けている。",
    historical_context="戦後10年代の女性表現の本格的台頭期。",
    primary_source_url=WIKI_JA+"%E8%8C%A8%E6%9C%A8%E3%81%AE%E3%82%8A%E5%AD%90",
    primary_source_type="Wikipedia: 茨木のり子",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"戦後女性主体",
         "description":"茨木の戦後女性詩は、戦争体験における女性主体の文学的形象化として人類学的価値を持つ。"}])

add(**C, name_ja="高橋睦郎の現代詩",
    name_en="Takahashi Mutsuo's Contemporary Poetry",
    name_original="高橋睦郎",
    period_key="現代文学期",
    definition="高橋睦郎（1937-）の戦後・現代を貫く詩業。古典和歌の教養と男色文学の伝統を結び、独自の同性愛詩学・古典詩学融合を展開し、現代詩の境界を拡げた。",
    background="三島由紀夫の知遇、古典和歌・連歌・俳諧研究、ギリシア古典への傾倒。",
    development="現代日本詩におけるセクシュアリティと古典の主題化として、独自の詩的位相を確立した。",
    historical_context="1960年代以降の性的少数派表現の文学的可視化期。",
    primary_source_url=WIKI_JA+"%E9%AB%98%E6%A9%8B%E7%9D%A6%E9%83%8E",
    primary_source_type="Wikipedia: 高橋睦郎",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# C: 評論（7件）
# ============================================================
add(**C, name_ja="江藤淳『成熟と喪失』",
    name_en="Etō Jun's Seijuku to Sōshitsu",
    name_original="成熟と喪失",
    period_key="戦後文学期",
    definition="江藤淳（1932-1999）が1967年に刊行した文芸評論。安岡章太郎・小島信夫ら「第三の新人」を「母性喪失」の主題で読み解き、戦後日本の精神史的転換を文学批評として提示した名著。",
    background="アメリカ留学体験(1962-64)と戦後文学の総括的考察の必要性。",
    development="戦後日本論・近代化論として、文学批評を超えて社会思想の領域へ波及した。",
    historical_context="高度経済成長期の伝統的家族・共同体の崩壊と、その文学的問題化。",
    primary_source_url=WIKI_JA+"%E6%88%90%E7%86%9F%E3%81%A8%E5%96%AA%E5%A4%B1",
    primary_source_type="Wikipedia: 成熟と喪失",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"母性喪失と近代化",
         "description":"江藤の母性喪失論は、人類学的家族研究と並行する戦後日本の精神史的考察。"}])

add(**C, name_ja="加藤周一『日本文学史序説』",
    name_en="Katō Shūichi's Nihon Bungaku-shi Josetsu",
    name_original="日本文学史序説",
    period_key="現代文学期",
    definition="加藤周一（1919-2008）が1975-80年に刊行した二巻本の体系的日本文学史。古代から現代までを「土着の世界観と外来の世界観」の交錯として論じ、戦後日本文学史記述の最高峰。",
    background="戦後雑種文化論（1955）以来の日本文化総合視座の集大成。",
    development="日本文学史の標準的参照書として、英訳・仏訳されて国際的にも普及した。",
    historical_context="戦後30年を経た高度経済成長後期、日本文化の自己像確立期。",
    primary_source_url=WIKI_JA+"%E6%97%A5%E6%9C%AC%E6%96%87%E5%AD%A6%E5%8F%B2%E5%BA%8F%E8%AA%AC",
    primary_source_type="Wikipedia: 日本文学史序説",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="吉本隆明『言語にとって美とはなにか』",
    name_en="Yoshimoto Takaaki's Gengo ni Totte Bi towa Nani ka",
    name_original="言語にとって美とはなにか",
    period_key="戦後文学期",
    definition="吉本隆明（1924-2012）が1965年に刊行した文学言語論の主著。「自己表出」と「指示表出」の対概念で言語芸術を分析し、戦後日本最も影響力ある文学理論を提供した。",
    background="戦後マルクス主義言語論への批判的乗り越えと、独自の言語論構築の必要性。",
    development="現代詩・散文の理論的基礎として、長く文芸批評に影響を与え続けた。",
    historical_context="60年安保闘争後の知的再編期、独自の戦後思想の形成期。",
    primary_source_url=WIKI_JA+"%E8%A8%80%E8%AA%9E%E3%81%AB%E3%81%A8%E3%81%A3%E3%81%A6%E7%BE%8E%E3%81%A8%E3%81%AF%E3%81%AA%E3%81%AB%E3%81%8B",
    primary_source_type="Wikipedia: 言語にとって美とはなにか",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="吉本隆明『共同幻想論』",
    name_en="Yoshimoto Takaaki's Kyōdō Gensō-ron",
    name_original="共同幻想論",
    period_key="戦後文学期",
    definition="吉本隆明が1968年に刊行した思想書。『古事記』『遠野物語』を主資料に、国家を「共同幻想」として概念化し、自己幻想・対幻想・共同幻想の三層構造論を展開した戦後思想の到達点。",
    background="60年代後半の国家論再考と、構造主義・人類学の知的潮流の吸収。",
    development="戦後思想の中核概念として、文学批評・社会学・人類学の領域横断的影響を持続している。",
    historical_context="68年学生運動期の国家・共同体への根源的問い直し。",
    primary_source_url=WIKI_JA+"%E5%85%B1%E5%90%8C%E5%B9%BB%E6%83%B3%E8%AB%96",
    primary_source_type="Wikipedia: 共同幻想論",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"共同幻想と国家",
         "description":"吉本の共同幻想論は、人類学的国家・共同体研究と同期する戦後思想の中核理論。"}])

add(**C, name_ja="蓮實重彦『反=日本語論』",
    name_en="Hasumi Shigehiko's Han-Nihongo-ron",
    name_original="反=日本語論",
    period_key="現代文学期",
    definition="蓮實重彦（1936-）が1977年に刊行した評論。日本語の特殊性を強調する「日本語論」の言説を解体し、フランス現代思想の方法論を文芸批評に応用した。日本ポスト構造主義批評の出発点。",
    background="フランス留学(1962-65)、フーコー・ロラン・バルトの吸収。",
    development="ポスト構造主義的文芸批評の道を開き、柄谷行人・浅田彰らとの共同戦線で1980年代批評を主導した。",
    historical_context="1970年代後半の構造主義・ポスト構造主義の日本受容期。",
    primary_source_url=WIKI_JA+"%E8%93%AE%E5%AE%9F%E9%87%8D%E5%BD%A6",
    primary_source_type="Wikipedia: 蓮實重彦",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="柄谷行人『日本近代文学の起源』",
    name_en="Karatani Kōjin's Nihon Kindai Bungaku no Kigen",
    name_original="日本近代文学の起源",
    period_key="現代文学期",
    definition="柄谷行人（1941-）が1980年に刊行した評論。「風景」「内面」「告白」「病」「子供」の制度を解体し、近代文学の起源そのものを問い直した戦後批評の最大の達成。",
    background="アメリカ滞在(1975-77)、フーコーの考古学的方法の文学批評への応用。",
    development="日本近代文学研究の方法論的革命として、英訳・中訳されて国際的に流通した。",
    historical_context="1980年代知的状況、ポスト構造主義の本格的展開期。",
    primary_source_url=WIKI_JA+"%E6%97%A5%E6%9C%AC%E8%BF%91%E4%BB%A3%E6%96%87%E5%AD%A6%E3%81%AE%E8%B5%B7%E6%BA%90",
    primary_source_type="Wikipedia: 日本近代文学の起源",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"柄谷の「内面」「風景」の制度論は、AI時代における主体・内面の制度的構築を再考する基準点となる。",
         "related_ai_phenomenon":"AI時代の内面・主体の制度的構築"}])

add(**C, name_ja="福田恆存『私の幸福論』",
    name_en="Fukuda Tsuneari's Watashi no Kōfukuron",
    name_original="私の幸福論",
    period_key="戦後文学期",
    definition="福田恆存（1912-1994）が1956年に刊行した随筆評論。戦後民主主義の俗流化を批判し、保守的・伝統的価値観に基づく個人の幸福論を平明な散文で展開した。",
    background="シェイクスピア翻訳・劇作活動と、戦後思想潮流への保守的応答。",
    development="戦後保守思想の文学的代表として、後の小林秀雄・江藤淳らに継承された。",
    historical_context="戦後復興期の左右イデオロギー対立と、保守思想の文芸的形成期。",
    primary_source_url=WIKI_JA+"%E7%A6%8F%E7%94%B0%E6%81%92%E5%AD%98",
    primary_source_type="Wikipedia: 福田恆存",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# D: 戯曲（10件）
# ============================================================
add(**C, name_ja="岸田國士『紙風船』",
    name_en="Kishida Kunio's Kamifūsen",
    name_original="紙風船",
    period_key="大正文学期",
    definition="岸田國士（1890-1954）が1925年に発表した一幕戯曲。日曜日を持て余す若夫婦の対話劇で、近代日本における会話劇の規範を確立した。新劇運動初期の代表作。",
    background="フランス留学(1919-23)と築地小劇場での新劇運動。",
    development="日本近代戯曲の出発点として、戦後の木下順二・別役実らに会話劇の規範を提供した。",
    historical_context="大正末期の新劇運動と、近代演劇制度の確立期。",
    primary_source_url=AOZORA+"cards/001154/card44882.html",
    primary_source_type="青空文庫: 紙風船",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="岸田國士『古い玩具』",
    name_en="Kishida Kunio's Furui Omocha",
    name_original="古い玩具",
    period_key="大正文学期",
    definition="岸田國士が1924年に発表した一幕戯曲。日常生活の細部に潜む心理を、簡潔な対話で表現した近代日本会話劇の出発点。フランス近代劇の影響下に書かれた。",
    background="フランス近代劇（コポー、ジャック・コポー）の方法論吸収。",
    development="後の岸田戯曲全体の出発点として、近代日本戯曲の方法的基準を提供した。",
    historical_context="大正末期の新劇運動初期、西欧近代劇の翻訳・受容期。",
    primary_source_url=AOZORA+"cards/001154/card46911.html",
    primary_source_type="青空文庫: 古い玩具",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="久保田万太郎『短夜』",
    name_en="Kubota Mantarō's Mijikayo",
    name_original="短夜",
    period_key="大正文学期",
    definition="久保田万太郎（1889-1963）が大正期に発表した戯曲。下町情緒と俳諧的詩情を融合した独自の作風で、大正期の市井生活劇の規範を確立した。",
    background="泉鏡花・永井荷風らとの交友、俳諧と新劇運動の融合。",
    development="戦前戦後を貫く下町情緒劇の系譜を確立し、後の新派・新劇に影響を残した。",
    historical_context="大正期の都市生活意識と伝統的下町文化の文学的問題化。",
    primary_source_url=WIKI_JA+"%E4%B9%85%E4%BF%9D%E7%94%B0%E4%B8%87%E5%A4%AA%E9%83%8E",
    primary_source_type="Wikipedia: 久保田万太郎",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="三好十郎『廃墟』",
    name_en="Miyoshi Jūrō's Haikyo",
    name_original="廃墟",
    period_key="戦後文学期",
    definition="三好十郎（1902-1958）が1947年に発表した戦後戯曲。戦後の精神的廃墟と再生を主題に、戦後新劇運動の出発点を成した代表作の一つ。",
    background="戦中の従軍体験と、敗戦後の演劇による精神的再建の試み。",
    development="戦後新劇運動の出発作として、木下順二・宇野信夫らとともに戦後演劇の方向を示した。",
    historical_context="敗戦直後の文化的廃墟期、演劇による戦後再生の試行。",
    primary_source_url=WIKI_JA+"%E4%B8%89%E5%A5%BD%E5%8D%81%E9%83%8E",
    primary_source_type="Wikipedia: 三好十郎",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="木下順二『夕鶴』",
    name_en="Kinoshita Junji's Yūzuru",
    name_original="夕鶴",
    period_key="戦後文学期",
    definition="木下順二（1914-2006）が1949年に発表した代表戯曲。「鶴の恩返し」民話を題材に、貨幣経済による純粋な愛の破壊を主題化した戦後民話劇の頂点。山本安英主演で長期上演された。",
    background="柳田國男民俗学への傾倒と、戦後民話運動の中での創作。",
    development="戦後新劇の規範作として、民話劇という独自ジャンルを確立し、戦後民俗学劇運動を主導した。",
    historical_context="戦後復興期の民俗的記憶の文学的再生運動。",
    primary_source_url=WIKI_JA+"%E5%A4%95%E9%B6%B4",
    primary_source_type="Wikipedia: 夕鶴",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"民話と貨幣経済",
         "description":"『夕鶴』は人類学的民話研究と経済人類学を結ぶ戦後文学の中核事例。"}])

add(**C, name_ja="安部公房『友達』",
    name_en="Abe Kōbō's Tomodachi",
    name_original="友達",
    period_key="戦後文学期",
    definition="安部公房（1924-1993）が1967年に発表した戯曲。突然押しかけてくる「友達」一家の不条理を通じて、現代社会の集団主義と個人の解体を寓話化した代表的不条理劇。",
    background="安部公房スタジオ設立(1973)以前の演劇活動と、ベケット・カフカの吸収。",
    development="戦後不条理演劇の到達点として、現代日本演劇に決定的影響を与えた。",
    historical_context="高度経済成長後期の都市的疎外と集団主義への批判的応答。",
    primary_source_url=WIKI_JA+"%E5%8F%8B%E9%81%94_(%E6%88%AF%E6%9B%B2)",
    primary_source_type="Wikipedia: 友達(戯曲)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="別役実『マッチ売りの少女』",
    name_en="Betsuyaku Minoru's Macchi-uri no Shōjo",
    name_original="マッチ売りの少女",
    period_key="戦後文学期",
    definition="別役実（1937-2020）が1966年に発表した代表戯曲。アンデルセン童話を翻案し、戦後日本の集団的記憶の不確かさを不条理劇として展開した戦後不条理演劇の象徴的成果。",
    background="早稲田小劇場・自由舞台等の小劇場運動と、ベケット影響下の不条理劇の創造。",
    development="戦後不条理演劇の規範作として、唐十郎・寺山修司の小劇場運動と並走した。",
    historical_context="1960年代後半の小劇場運動勃興期、戦後の集合的記憶の問い直し。",
    primary_source_url=WIKI_JA+"%E5%88%A5%E5%BD%B9%E5%AE%9F",
    primary_source_type="Wikipedia: 別役実",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="唐十郎『特権的肉体論』",
    name_en="Kara Jūrō's Tokken-teki Nikutairon",
    name_original="特権的肉体論",
    period_key="戦後文学期",
    definition="唐十郎（1940-2024）が1968年に発表した演劇論。役者の身体を「特権的肉体」と概念化し、近代演劇のテキスト中心主義を批判して身体性に基づく演劇を主張した。アングラ演劇の理論的支柱。",
    background="状況劇場結成(1963)と、新宿花園神社紅テント公演による小劇場運動。",
    development="戦後アングラ演劇の理論的基盤として、寺山修司・鈴木忠志らと並ぶ60年代演劇革命の中核を成した。",
    historical_context="1960年代後半の文化的ラジカリズム期、身体性復権運動。",
    primary_source_url=WIKI_JA+"%E7%89%B9%E6%A8%A9%E7%9A%84%E8%82%89%E4%BD%93%E8%AB%96",
    primary_source_type="Wikipedia: 特権的肉体論",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"唐の身体性論は、AI時代におけるテキスト中心と身体的主体の関係再考の祖型。",
         "related_ai_phenomenon":"AI時代の身体性と主体"}])

add(**C, name_ja="寺山修司『田園に死す』",
    name_en="Terayama Shūji's Den'en ni Shisu",
    name_original="田園に死す",
    period_key="戦後文学期",
    definition="寺山修司（1935-1983）が1965年に短歌集として刊行、後に1974年映画化した代表作。少年期の青森原風景と母性的記憶を、シュルレアリスム的手法で再構成した。",
    background="天井桟敷主宰、短歌・映画・演劇の領域横断的活動。",
    development="戦後アングラ運動の代表として、短歌・映画・演劇の境界横断的表現の規範を提供した。",
    historical_context="1960年代後半の文化的境界横断期、地方/中央の文化的緊張の問題化。",
    primary_source_url=WIKI_JA+"%E7%94%B0%E5%9C%92%E3%81%AB%E6%AD%BB%E3%81%99",
    primary_source_type="Wikipedia: 田園に死す",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="鈴木忠志『トロイアの女』",
    name_en="Suzuki Tadashi's Toroia no Onna",
    name_original="トロイアの女",
    period_key="現代文学期",
    definition="鈴木忠志（1939-）が1974年に演出したエウリピデス翻案。日本伝統演劇の身体技法（鈴木メソッド）でギリシア悲劇を上演し、戦後日本演劇の国際的基準を確立した。",
    background="早稲田小劇場・SCOT結成、利賀村拠点の演劇国際化活動。",
    development="戦後日本演劇の国際的代表として、鈴木メソッドが世界の演劇教育に普及した。",
    historical_context="1970年代の文化的グローバル化期と、伝統と前衛の融合運動。",
    primary_source_url=WIKI_JA+"%E9%88%B4%E6%9C%A8%E5%BF%A0%E5%BF%97_(%E6%BC%94%E5%87%BA%E5%AE%B6)",
    primary_source_type="Wikipedia: 鈴木忠志",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# E: 児童文学（9件）
# ============================================================
add(**C, name_ja="新美南吉『ごん狐』",
    name_en="Niimi Nankichi's Gongitsune",
    name_original="ごん狐",
    period_key="昭和戦前戦中期",
    definition="新美南吉（1913-1943）が1932年に発表した児童文学短編。母を亡くしたいたずら狐ごんと兵十の悲しい交流を描き、近代日本児童文学の最高傑作の一つとして教科書定番教材化された。",
    background="鈴木三重吉『赤い鳥』伝統と地域民話の融合的創作。",
    development="国民的児童文学作品として、戦後の小学校国語教科書に採録され続けている。",
    historical_context="昭和初期の児童文学黄金期、地方児童文学の興隆期。",
    primary_source_url=AOZORA+"cards/000121/card628.html",
    primary_source_type="青空文庫: ごん狐",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="椋鳩十『大造じいさんとガン』",
    name_en="Mukū Hatojū's Daizō Jiisan to Gan",
    name_original="大造じいさんとガン",
    period_key="昭和戦前戦中期",
    definition="椋鳩十（1905-1987）が1941年に発表した動物児童文学。猟師大造とガンの群れの頭領との知略の対決を通じて、自然と人間の倫理的関係を描いた近代動物文学の代表作。",
    background="鹿児島県山村教師経験と、動物観察に基づく動物文学の創出。",
    development="戦後小学校国語教科書定番として、長く読み継がれる動物文学の規範作品。",
    historical_context="昭和戦前期の自然主義的児童文学運動と動物文学の興隆期。",
    primary_source_url=WIKI_JA+"%E6%A4%8B%E9%B3%A9%E5%8D%81",
    primary_source_type="Wikipedia: 椋鳩十",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="壺井栄『二十四の瞳』",
    name_en="Tsuboi Sakae's Nijūshi no Hitomi",
    name_original="二十四の瞳",
    period_key="戦後文学期",
    definition="壺井栄（1899-1967）が1952年に刊行した長編小説。瀬戸内海小豆島の女教師と12人の教え子の戦中戦後を描き、戦争による庶民の悲劇を象徴化した戦後ベストセラー。木下惠介監督で映画化(1954)。",
    background="小豆島での生活体験と、戦後の反戦平和文学運動。",
    development="戦後反戦文学・教育文学の規範として、映画・テレビドラマ化を通じて国民的記憶となった。",
    historical_context="戦後復興期の反戦平和文化運動と庶民史の文学的問題化。",
    primary_source_url=WIKI_JA+"%E4%BA%8C%E5%8D%81%E5%9B%9B%E3%81%AE%E7%9E%B3",
    primary_source_type="Wikipedia: 二十四の瞳",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"戦争と庶民の記憶",
         "description":"『二十四の瞳』は人類学的記憶研究における戦後日本の集合的記憶形成の中核事例。"}])

add(**C, name_ja="いぬいとみこ『木かげの家の小人たち』",
    name_en="Inui Tomiko's Kokage no Ie no Kobitotachi",
    name_original="木かげの家の小人たち",
    period_key="戦後文学期",
    definition="いぬいとみこ（1924-2002）が1959年に刊行した児童文学。英国小人伝説を日本に翻案し、戦時下の家族と小人たちの友情を描いた戦後児童文学の代表作。",
    background="戦中戦後の少女期体験と英国児童文学の翻訳経験。",
    development="戦後児童文学の本格化を象徴する作品として、現代日本児童文学の出発点を成した。",
    historical_context="戦後10年代の児童文学新運動期、近代児童文学の本格化期。",
    primary_source_url=WIKI_JA+"%E3%81%84%E3%81%AC%E3%81%84%E3%81%A8%E3%81%BF%E3%81%93",
    primary_source_type="Wikipedia: いぬいとみこ",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="灰谷健次郎『兎の眼』",
    name_en="Haitani Kenjirō's Usagi no Me",
    name_original="兎の眼",
    period_key="現代文学期",
    definition="灰谷健次郎（1934-2006）が1974年に刊行した児童文学。新任女教師と問題児童の交流を通じて、教育・差別・貧困の問題を真正面から描いた現代児童文学の代表作。",
    background="神戸市の小学校教師経験と、被差別部落・障害児教育問題への関与。",
    development="現代児童文学の社会派路線を確立し、教師・親世代に広く読まれる教育文学の規範となった。",
    historical_context="1970年代の高度経済成長後期、教育・差別問題の社会的問題化期。",
    primary_source_url=WIKI_JA+"%E5%85%8E%E3%81%AE%E7%9C%BC",
    primary_source_type="Wikipedia: 兎の眼",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="那須正幹『ズッコケ三人組』シリーズ",
    name_en="Nasu Masayuki's Zukkoke Sannin-gumi Series",
    name_original="ズッコケ三人組",
    period_key="現代文学期",
    definition="那須正幹（1942-2021）が1978-2004年に発表した50巻のロングセラー児童文学シリーズ。小学6年生の三人組の冒険を通じて、現代日本の児童文化を描き、戦後最大の児童文学シリーズとなった。",
    background="広島の児童文学運動と、ベビーブーム世代の児童読者層の拡大。",
    development="現代日本児童文学のロングセラー規範として、テレビアニメ化を含めて国民的記憶となった。",
    historical_context="1980-90年代の児童文化大衆化期と、シリーズ児童文学の成熟期。",
    primary_source_url=WIKI_JA+"%E3%81%9A%E3%81%A3%E3%81%93%E3%81%91%E4%B8%89%E4%BA%BA%E7%B5%84",
    primary_source_type="Wikipedia: ズッコケ三人組",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="角田光代『対岸の彼女』",
    name_en="Kakuta Mitsuyo's Taigan no Kanojo",
    name_original="対岸の彼女",
    period_key="現代文学期",
    definition="角田光代（1967-）が2004年に刊行した長編小説。第132回直木賞受賞作。30代女性二人の友情と過去の少女期を交錯させ、現代日本女性の人生選択を描いた現代女性文学の代表作。",
    background="女性ライフスタイルの多様化と、現代女性作家の本格的台頭。",
    development="現代女性文学の規範作として、平成期女性読者層に広く受容された。",
    historical_context="平成中期(2000年代)の女性ライフスタイル変容期と女性文学の成熟。",
    primary_source_url=WIKI_JA+"%E5%AF%BE%E5%B2%B8%E3%81%AE%E5%BD%BC%E5%A5%B3",
    primary_source_type="Wikipedia: 対岸の彼女",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="折口信夫『死者の書』",
    name_en="Orikuchi Shinobu's Shisha no Sho",
    name_original="死者の書",
    period_key="昭和戦前戦中期",
    definition="折口信夫（1887-1953、釈迢空）が1939年に発表した古代奈良を舞台とする幻想小説。古代信仰と万葉的世界観を独自の散文で再構築し、近代日本古代文学小説の最高峰の一つ。",
    background="国学・民俗学研究と独自の古代精神史構想。",
    development="古代と近代を結ぶ独自の幻想文学として、戦後三島由紀夫・中上健次に影響を与えた。",
    historical_context="昭和戦前期の国学・古代研究と古典文学創造の最盛期。",
    primary_source_url=AOZORA+"cards/000933/card46591.html",
    primary_source_type="青空文庫: 死者の書",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"古代信仰と民俗学",
         "description":"折口『死者の書』は人類学的古代信仰研究と文学的想像力を結ぶ近代日本の中核事例。"}])

add(**C, name_ja="釈迢空『海やまのあひだ』",
    name_en="Shaku Chōkū's Umi Yama no Aida",
    name_original="海やまのあひだ",
    period_key="大正文学期",
    definition="折口信夫（釈迢空名）が1925年に刊行した第一歌集。古代万葉的な調べを近代短歌に取り込み、独自の幻視的詩境を切り拓いた近代短歌の特異な達成。",
    background="国文学者・民俗学者としての古代研究と短歌革新の融合。",
    development="近代短歌における古代回帰の独自系譜を確立し、戦後現代短歌に独自の影響を残した。",
    historical_context="大正期の短歌革新運動における古典回帰と近代化の交錯。",
    primary_source_url=AOZORA+"index_pages/person933.html",
    primary_source_type="青空文庫: 折口信夫",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# Main runner
# ============================================================
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
        print(f"[c18 wave16 add50] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c18 wave16 add50] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
