"""LIT-DB Phase 2 Wave 11 — C27 add: SE Asian & Korean Literature (+40 concepts).

Subfield: lit_se_asia_korea (id=17), macro_region='グローバルサウス'.
This is an ADDITIVE wave: 40 concepts already exist (id=912-951). Adds 40 NEW
concepts covering Korean classical/modern, Vietnamese (Nôm tradition, modern),
Thai (royal court / modern), Indonesian (pantun, Pramoedya, contemporary),
Filipino (corrido, Rizal, modern, oral), Cambodian, Laotian, Burmese, Malay.

Sources:
  - 'primary'   -> Wikisource (Korean / Vietnamese / Thai / Indonesian),
                   KRpia (Korean classical archive), Project Gutenberg
                   (Rizal, public-domain SE Asian texts), Internet Archive,
                   Sacred-Texts (Ramakien etc).
  - 'secondary' -> Britannica, academic Wikipedia (en/ko/vi/th/id/fil),
                   journal entries, university repositories.

40 concepts split into eight blocks:
  A: Korean classical (5)         — hyangga, sijo, kasa, pansori, kobun novel
  B: Korean modern/contemporary (6)
  C: Vietnamese (5)               — Nôm tradition, Tale of Kieu, modern
  D: Thai (5)                     — royal court, Ramakien, modern Thai
  E: Indonesian / Malay (5)       — pantun, Pramoedya, sastra
  F: Filipino (5)                 — corrido, Rizal, oral, modern
  G: Cambodian / Laotian (4)      — Reamker, Sang Sinxay, Buddhist tales
  H: Burmese / cross-regional (5) — yadu/yagan, Hla Stin, Buddhist verse
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


# Periods used by this wave (region='グローバルサウス').
PERIODS = [
    ("韓国古典文学期", "Korean Classical Literature",
     600, 1900,
     "新羅統一以降の郷歌（ヒャンガ）から、高麗時調・歌辞、朝鮮王朝の古文小説（古典小説）、口承パンソリに至る、19世紀末以前の韓国古典文学期。漢文・吏読・ハングル混用の言語多層性が特徴。"),
    ("韓国近現代文学期", "Korean Modern & Contemporary Literature",
     1894, 2030,
     "甲午改革以降、開化期啓蒙文学・植民地期近代主義文学・分断期民族文学を経て、21世紀K-novelグローバル化に至る韓国近現代文学期。"),
    ("ベトナム古典・近世文学期", "Vietnamese Classical & Early-Modern Literature",
     1000, 1900,
     "李朝・陳朝以降の漢文文学と字喃（チュノム）文学の併存期。阮朝期の阮攸『金雲翹』を頂点とする字喃文学の成熟と、19世紀末仏領インドシナ成立直前期。"),
    ("ベトナム近現代文学期", "Vietnamese Modern Literature",
     1900, 2030,
     "国語ローマ字（クォック・グー）普及以降のベトナム近代文学。仏領期自力文団・写実主義から、抗仏・抗米戦争文学、ドイモイ期、現代ディアスポラ文学に至る。"),
    ("タイ古典・宮廷文学期", "Thai Classical & Court Literature",
     1350, 1900,
     "アユタヤ朝以降のタイ宮廷文学。クロンサーン・ニラート（紀行詩）・チャン詩形・ラーマキエン王権叙事詩を中核とし、ラタナコーシン朝期に文学的精緻化が頂点に達した宮廷文学期。"),
    ("タイ近現代文学期", "Thai Modern Literature",
     1900, 2030,
     "ラーマ六世王期の文学近代化以降のタイ文学。スントーン・プー以来の宮廷詩伝統と、20世紀社会派小説・現代タイ短編・グローバル受容期文学。"),
    ("マレー・インドネシア古典口承期", "Malay & Indonesian Classical-Oral Literature",
     1300, 1900,
     "マレー世界（ヌサンタラ）の口承詩・パントゥン・ヒカヤット（物語詩文）・スジャラ（年代記）伝統。マラッカ王国・アチェ王国・ジャワ王国の宮廷文学を含む、口承・写本併存期。"),
    ("インドネシア・マレーシア近現代期", "Indonesian & Malaysian Modern Literature",
     1900, 2030,
     "プジャンガ・バル世代以降のインドネシア・マレーシア近代文学。プラムディヤ・アナンタ・トゥール、サストラ・アンカタン45、現代マジック・リアリズム、馬華文学を含む。"),
    ("フィリピン古典・スペイン期", "Philippine Classical & Spanish Era",
     1565, 1898,
     "スペイン植民地期のフィリピン文学。コリード（口承叙事詩）・パシオン（受難譚）・タガログ・セブアノ口承、そしてホセ・リサール『ノリ・メ・タンヘレ』『エル・フィリブステリスモ』に至る民族意識覚醒期。"),
    ("フィリピン近現代文学期", "Philippine Modern Literature",
     1900, 2030,
     "米国植民地期英語文学導入以降のフィリピン近現代文学。タガログ・英語・セブアノ・イロカノの多言語並存と、ディアスポラ文学の興隆を特徴とする。"),
    ("カンボジア・ラオス古典期", "Cambodian & Laotian Classical Period",
     1200, 1900,
     "アンコール期以降のクメール文学とラーンサーン王国期以降のラオ文学。仏典・ジャータカ・王権叙事（リアムケー、サン・シンサイ）を中核とする、上座部仏教と王権の文学的形式期。"),
    ("ビルマ（ミャンマー）古典・近代期", "Burmese Classical & Modern Period",
     1200, 2030,
     "パガン王朝以降のビルマ古典文学（ヤドゥ・ヤガン詩形）と、19世紀末以降の近代小説の成立期。植民地期から軍政期を経て現代に至る。"),
    ("東南アジア横断的・地域比較期", "Cross-regional SE Asian Literary Period",
     1900, 2030,
     "東南アジアおよび環南シナ海・島嶼世界における、複数言語・複数植民地経験を横断する文学的傾向の比較研究期。"),
]


# Source URL bases (real, verifiable)
WSRC_KO = "https://ko.wikisource.org/wiki/"
WSRC_VI = "https://vi.wikisource.org/wiki/"
WSRC_TH = "https://th.wikisource.org/wiki/"
WSRC_ID = "https://id.wikisource.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
KRPIA = "https://www.krpia.co.kr/"
GUTEN = "https://www.gutenberg.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_KO = "https://ko.wikipedia.org/wiki/"
WIKI_VI = "https://vi.wikipedia.org/wiki/"
WIKI_TH = "https://th.wikipedia.org/wiki/"
WIKI_ID = "https://id.wikipedia.org/wiki/"
WIKI_FIL = "https://tl.wikipedia.org/wiki/"
BRITT = "https://www.britannica.com/"
SACRED = "https://www.sacred-texts.com/"
ARCHIVE = "https://archive.org/details/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_se_asia_korea", region="グローバルサウス",
         original_script="vernacular")


# ============================================================
# A: 韓国古典文学（5件）
# ============================================================
add(**C, name_ja="均如『普賢十願歌』",
    name_en="Gyunyeo's Eleven Bodhisattva Songs",
    name_original="普賢十願歌",
    period_key="韓国古典文学期",
    definition="高麗初期の華厳宗僧均如（923-973）が作った11首の郷歌作品群。『華厳経』普賢菩薩の十大願を韓国語固有の郷歌形式に翻訳したもので、『均如伝』(1075)所収。新羅郷歌25首と並ぶ韓国最古層詩歌の核心資料であり、仏教教義を母語詩形に統合した東アジア宗教詩の代表例。",
    background="新羅統一期の郷歌伝統と、高麗初期の華厳宗仏教教団による民衆教化志向。",
    development="朝鮮王朝期の歌辞・時調へ受け継がれる韓国母語詩形の起点となり、20世紀の梁柱東による郷歌解読を経て近代国文学の核心資料となった。",
    historical_context="光宗代（949-975）の科挙制定と仏教教団改革期。",
    primary_source_url=WSRC_KO+"%EB%B3%B4%ED%98%84%EC%8B%AD%EC%9B%90%EA%B0%80",
    primary_source_type="Wikisource Korean: 普賢十願歌",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="尹善道『漁夫四時詞』",
    name_en="Yun Seon-do's Eobu Sasi Sa",
    name_original="漁夫四時詞",
    period_key="韓国古典文学期",
    definition="朝鮮中期の士大夫尹善道（1587-1671）が1651年に著した時調連作。春夏秋冬各10首・計40首の連時調で、全羅南道・甫吉島の漁村生活を四季の流れに即して詠む。朝鮮時調文学の頂点を成し、士大夫詩歌における自然観・隠逸思想の集大成として評価される。",
    background="李朝中期の党争と尹善道自身の度重なる流配・隠居体験。",
    development="李珥・宋時烈らの士大夫詩歌伝統を継ぎつつ、近代以降の韓国古典文学正典化において時調の代表作と位置づけられた。",
    historical_context="孝宗代の党争と地方士族の隠逸文化。",
    primary_source_url=WSRC_KO+"%EC%96%B4%EB%B6%80%EC%82%AC%EC%8B%9C%EC%82%AC",
    primary_source_type="Wikisource Korean: 漁夫四時詞",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="鄭澈『松江歌辞』",
    name_en="Jeong Cheol's Songgang Gasa",
    name_original="松江歌辞",
    period_key="韓国古典文学期",
    definition="朝鮮中期士大夫鄭澈（号：松江、1536-1593）が著した歌辞作品群。代表作「関東別曲」（金剛山・関東八景紀行）、「思美人曲」「続美人曲」（女性話者による君主への忠情）、「星山別曲」を含む。歌辞の規範形式を確立し、宮廷的・士大夫的歌辞文学の頂点をなす。",
    background="宣祖代（1567-1608）の党争と鄭澈の度重なる流配・復権、および朝鮮歌辞形式の宮廷的精緻化。",
    development="女性話者による忠情表出（「思美人曲」）は朝鮮歌辞の規範修辞となり、後代の朴仁老・許蘭雪軒・近代国文学にまで継承された。",
    historical_context="壬辰倭乱直前の朝鮮王朝中期、士林派内党争激化期。",
    primary_source_url=WSRC_KO+"%EC%86%A1%EA%B0%95%EA%B0%80%EC%82%AC",
    primary_source_type="Wikisource Korean: 松江歌辞",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="申潤福のパンソリ六歌",
    name_en="Pansori six madang",
    name_original="판소리 여섯 마당",
    period_key="韓国古典文学期",
    definition="朝鮮後期に成立したパンソリ十二歌のうち、19世紀末申在孝（1812-1884）が整理・正典化した6作品（春香歌・沈清歌・興夫歌・水宮歌・赤壁歌・薔花紅蓮歌）。「マダン（場）」と呼ばれる構造単位で口承され、ソリクン（歌い手）とコス（鼓手）の二人組で演じられる総合芸能。2003年UNESCO人類無形文化遺産。",
    background="朝鮮後期の庶民文化興隆と、申在孝による口承伝統の文字化・規範化作業。",
    development="20世紀朴東鎮ら名唱の継承と、UNESCO登録による現代芸能としての制度化。林権澤映画『シバジ』『風の丘を越えて』が広く国際的に紹介。",
    historical_context="19世紀朝鮮王朝末期の庶民文化興隆と、開港期(1876-)以降の伝統芸能再編。",
    primary_source_url=WSRC_KO+"%ED%8C%90%EC%86%8C%EB%A6%AC",
    primary_source_type="Wikisource Korean: 판소리",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"パンソリは口承・即興・観客介入を含む生身のパフォーマンス芸術であり、AI生成テキストが原理的に欠く即興性・身体性を理論化する古典的参照点となる。",
         "related_ai_phenomenon":"AI生成テキストの非身体性 vs 口承芸術の即興身体性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"口承文芸と無形文化遺産",
         "description":"パンソリは口承伝承と即興身体性を中核とし、人類学的口承文芸研究（パリー＝ロード理論）の東アジア事例として位置づけられる。"}])

add(**C, name_ja="金万重『九雲夢』",
    name_en="Kim Manjung's Kuun-mong",
    name_original="九雲夢",
    period_key="韓国古典文学期",
    definition="朝鮮後期士大夫金万重（1637-1692）が流配地で1687-89年頃に著した古典小説。仏弟子性真が夢の中で楊少游として八仙女との縁を遍歴する筋立てで、朝鮮古文小説中、最も完成度の高い作品とされる。漢文版とハングル版が並存し、朝鮮ハングル小説の正典化に寄与した。",
    background="金万重の流配体験と、朝鮮王朝後期の士大夫小説執筆文化、および中国伝奇小説受容。",
    development="許筠『洪吉童伝』、朴趾源漢文小説、19世紀庶民古典小説への系譜的影響を持ち、近代以降は韓国古典小説研究の中心対象となった。",
    historical_context="粛宗代（1674-1720）の党争と士大夫流配文化、女性読者層の形成期。",
    primary_source_url=KRPIA+"viewer/?prdId=KP01&did=GS_001",
    primary_source_type="KRpia: 九雲夢 (古典DB)",
    importance_score=4, source_tier="primary", canonical_in_region="core")


# ============================================================
# B: 韓国近現代（6件）
# ============================================================
add(**C, name_ja="廉想渉『三代』",
    name_en="Yom Sang-seop's Three Generations",
    name_original="三代",
    period_key="韓国近現代文学期",
    definition="廉想渉（1897-1963）が1931年に新聞連載した長編小説。植民地期ソウルの両班家系・趙家三代（祖父・父・息子）の世代葛藤を通じて、儒教的家父長制と植民地近代の衝突、思想的迷走を描く。植民地期韓国近代リアリズム長編の最高峰として評価される。",
    background="1930年代植民地朝鮮の都市化進展と、両班家庭の経済的没落、社会主義思想流入。",
    development="李泰俊・朴泰遠ら同世代モダニズム作家との対比軸を成し、解放後の韓国リアリズム長編の規範となった。",
    historical_context="満州事変直前の植民地朝鮮社会と、京城（ソウル）市民社会の階層分裂。",
    primary_source_url=WIKI_KO+"%EC%82%BC%EB%8C%80_(%EC%86%8C%EC%84%A4)",
    primary_source_type="Wikipedia Korean: 三代 (소설)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="李箱『翼』",
    name_en="Yi Sang's Wings",
    name_original="날개",
    period_key="韓国近現代文学期",
    definition="李箱（1910-1937）が1936年に発表した中編小説。京城・遊郭街を舞台に、無職の知識人「私」と娼婦の妻との倒錯的関係を、断章的・モダニズム的散文で描く。植民地期朝鮮モダニズム文学の頂点とされ、ジョイス・カフカと並び論じられる東アジア・モダニズムの代表作。",
    background="1930年代京城のモダニズム文芸誌『朝鮮中央日報』『朝光』と九人会の活動、李箱の建築技師・喫茶店主としての生活体験。",
    development="戦後韓国モダニズム文学の起点とされ、金洙暎・崔仁勲・李清俊の系譜的源泉となった。",
    historical_context="日中戦争前夜の植民地朝鮮、知識人の自閉と社会的位置喪失。",
    primary_source_url=WSRC_KO+"%EB%82%A0%EA%B0%9C",
    primary_source_type="Wikisource Korean: 날개",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"李箱『翼』の自閉的・断章的主体は、植民地的近代における自我解体を文学化する。AI時代の自我構成（生成AIによる多重ペルソナ・自己叙述支援）と歴史的に並行するモダニズム的主体喪失の祖型。",
         "related_ai_phenomenon":"AI時代の自我構成・ペルソナ多重化"}])

add(**C, name_ja="趙世煕『こびとが打ち上げた小さなボール』",
    name_en="Cho Se-hui's The Dwarf",
    name_original="난장이가 쏘아올린 작은 공",
    period_key="韓国近現代文学期",
    definition="趙世煕（1942-2022）が1975-78年に連作発表した短編連作小説。ソウル都市再開発に伴い住居を追われる「こびと」家族の悲劇を中核とし、12編の連作で1970年代開発独裁期の構造的暴力を描く。1978年単行本刊行後、韓国民衆文学の代表作として2010年代まで100万部を突破した。",
    background="朴正熙開発独裁期(1961-1979)の経済成長と都市再開発、構造的階層分裂。",
    development="韓国民衆文学運動の文学的核となり、80年代労働文学・90年代以降の社会派長編に継承された。",
    historical_context="1970年代後半の都市スラム強制撤去と、維新体制下の言論統制。",
    primary_source_url=WIKI_KO+"%EB%82%9C%EC%9E%A5%EC%9D%B4%EA%B0%80_%EC%8F%98%EC%95%84%EC%98%AC%EB%A6%B0_%EC%9E%91%EC%9D%80_%EA%B3%B5",
    primary_source_type="Wikipedia Korean: 난장이가 쏘아올린 작은 공",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="申京淑『母をお願い』",
    name_en="Shin Kyung-sook's Please Look After Mom",
    name_original="엄마를 부탁해",
    period_key="韓国近現代文学期",
    definition="申京淑（1963-）が2008年に発表した長編小説。ソウル駅で消えた母を子と夫が探す多重視点で、農村出身母世代の自己犠牲と都市化世代の罪悪感を描く。韓国国内200万部超、英訳版（2011, Knopf）が34カ国で翻訳されるなど、K-novelグローバル化の先駆作品となった。2012年マン・アジア文学賞受賞。",
    background="2000年代韓国の高齢化進展、都市化世代の母世代に対する集団的罪意識。",
    development="韓江『菜食主義者』、孫元平（ソン・ウォンピョン）『アーモンド』、ファン・ボルム『朝になったら別人』に至るK-novelグローバル波の起点となった。",
    historical_context="2000年代後半の韓国高齢化社会化、都市・農村格差顕在化期。",
    primary_source_url=WIKI_KO+"%EC%97%84%EB%A7%88%EB%A5%BC_%EB%B6%80%ED%83%81%ED%95%B4",
    primary_source_type="Wikipedia Korean: 엄마를 부탁해",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="趙南柱『82年生まれ、キム・ジヨン』",
    name_en="Cho Nam-joo's Kim Jiyoung, Born 1982",
    name_original="82년생 김지영",
    period_key="韓国近現代文学期",
    definition="趙南柱（1978-）が2016年に発表した長編小説。1982年生まれの主人公キム・ジヨンの幼少期から育児期までを統計的記述様式で描き、韓国社会のジェンダー差別の構造を可視化した。韓国国内130万部超、25カ国翻訳。2019年映画化、2020年代韓国フェミニズム文学の象徴的作品となった。",
    background="2010年代韓国の#MeToo運動と江南駅女性殺害事件(2016)、ミレニアル世代女性のジェンダー意識覚醒。",
    development="韓国フェミニズム文学（鄭世朗、崔恩栄、ファン・ジョンウン）の興隆を牽引し、東アジア・フェミニズム文学の参照点となった。",
    historical_context="朴槿恵政権末期から文在寅政権初期にかけてのジェンダー政治化期。",
    primary_source_url=WIKI_KO+"82%EB%85%84%EC%83%9D_%EA%B9%80%EC%A7%80%EC%98%81",
    primary_source_type="Wikipedia Korean: 82년생 김지영",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"統計データ的記述様式と物語性の融合は、AI生成可能な「データドリブン物語」の祖型として機能する。AI時代におけるデータ・ナラティヴ融合形式の文学理論的参照点。",
         "related_ai_phenomenon":"AI時代のデータ駆動型ナラティヴ生成"}])

add(**C, name_ja="韓国ウェブ小説（ウェブトゥーン）",
    name_en="Korean web novels and webtoons",
    name_original="웹소설・웹툰",
    period_key="韓国近現代文学期",
    definition="2010年代以降韓国で急成長した連載型ウェブ小説およびウェブトゥーン（縦スクロール漫画）の文学現象。Naver・KakaoPage・MunPiaを主要プラットフォームとし、ロマンス・ファンタジー・武侠・転生・系統作品を中心に、2023年市場規模1兆ウォン超。Netflix『キングダム』『地獄が呼んでいる』ら映像化原作の主要供給源。",
    background="2010年代韓国スマートフォン普及と縦スクロール漫画形式の発明、サブスクリプション課金モデルの確立。",
    development="K-novel・K-comicsとしてグローバル展開され、Netflix・Disney+を経由した世界的IP供給源となった。",
    historical_context="2010-2020年代の韓国コンテンツ産業のグローバル化（K-pop・K-drama・K-novel連動）。",
    primary_source_url=WIKI_KO+"%EC%9B%B9%EC%86%8C%EC%84%A4",
    primary_source_type="Wikipedia Korean: 웹소설",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ウェブ小説・ウェブトゥーンはスクロール・モバイル・連載課金を前提とした新しい文学形式であり、AI翻訳・AI作画支援との結合で第四変容期の文学媒体を象徴する。",
         "related_ai_phenomenon":"AI翻訳・AIイラスト連載とプラットフォーム文学"},
        {"axis":"受容","status":"rethinking",
         "rationale":"ウェブ小説の連載・課金・コメント・人気投票は、読者反応をリアルタイムに作品に取り込む生産形式であり、AI生成と参加型受容を統合する第四変容期文学の典型。",
         "related_ai_phenomenon":"参加型読者フィードバック+AI連載生成"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"プラットフォーム連載文学とAI",
         "description":"ウェブ小説プラットフォームはAI翻訳・AI推薦・AIアシスト執筆の主要実装現場であり、AI時代文学媒体の代表事例。"}])


# ============================================================
# C: ベトナム文学（5件）
# ============================================================
add(**C, name_ja="阮廌『国音詩集』",
    name_en="Nguyễn Trãi's Quốc Âm Thi Tập",
    name_original="國音詩集",
    period_key="ベトナム古典・近世文学期",
    definition="黎朝開国功臣阮廌（グエン・チャイ、1380-1442）が編んだ字喃（チュノム）詩集254首。ベトナム最古の体系的字喃詩集として、漢詩伝統からベトナム母語詩への転換を象徴する。阮廌は1980年UNESCO「世界文化偉人」に登録され、ベトナム民族文学の祖と位置づけられる。",
    background="明朝支配（1407-1427）からの解放戦争と黎朝（1428-1788）成立期、字喃文字の宮廷的承認。",
    development="字喃詩は阮攸『金雲翹』(19世紀初)に至るベトナム母語詩伝統の起点となり、近代国語ローマ字化以降も民族文学の核として研究され続ける。",
    historical_context="15世紀前半の黎朝建国期、阮廌の冤罪刑死(1442)と18世紀名誉回復。",
    primary_source_url=WSRC_VI+"Qu%E1%BB%91c_%C3%A2m_thi_t%E1%BA%ADp",
    primary_source_type="Wikisource Vietnamese: Quốc Âm Thi Tập",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="胡春香の字喃詩",
    name_en="Hồ Xuân Hương's Nôm poetry",
    name_original="Hồ Xuân Hương",
    period_key="ベトナム古典・近世文学期",
    definition="胡春香（ホー・スアン・フオン、1772頃-1822頃）はベトナム後期黎朝・阮朝期の女性詩人。約60首の字喃詩を残し、性的隠喩と社会批判を結合した強烈な女性詩を展開した。「ベトナム詩の女王」と称され、20世紀以降のベトナム民族文学および世界フェミニズム文学研究の主要対象となった。",
    background="18世紀末ベトナム封建体制末期、女性の知識人としての困難な社会的位置、字喃詩の口承的普及。",
    development="20世紀ホアイ・タイン編『ベトナム詩人』(1942)で正典化され、英訳（John Balaban, 2000）を経てグローバルに流通した。",
    historical_context="阮朝建国期(1802-)の社会変動と、儒教的女性規範下の女性詩人の特異な地位。",
    primary_source_url=WSRC_VI+"T%C3%A1c_gia:H%E1%BB%93_Xu%C3%A2n_H%C6%B0%C6%A1ng",
    primary_source_type="Wikisource Vietnamese: 胡春香",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"胡春香の女性主体詩は、東アジア儒教世界における女性詩主体の例外的存立を示す。AI時代の多様な主体生成（女性視点・マイノリティ視点）の歴史的祖型として再読される。",
         "related_ai_phenomenon":"AI生成における周縁主体視点の構築"}])

add(**C, name_ja="ベトナム漢喃文学",
    name_en="Vietnamese Han-Nôm literature",
    name_original="văn học Hán-Nôm",
    period_key="ベトナム古典・近世文学期",
    definition="11世紀李朝以降19世紀末まで、漢文と字喃（チュノム）の二言語体系で展開されたベトナム古典文学の総称。漢喃研究院（Viện Nghiên cứu Hán Nôm）が約4万件の写本・拓本を保管。仏教経典・儒教経典・民間仏典・宮廷詩・口承文学が並存する東アジア漢字文化圏のベトナム的形態を成す。",
    background="李朝（1009-1225）以降の科挙制度と漢字文化、字喃文字の段階的発達。",
    development="20世紀仏領期に国語ローマ字（クォック・グー）に置換されるが、現代ベトナムの古典文学研究は漢喃研究院を中心に継続する。",
    historical_context="東アジア漢字文化圏の南方周縁形成、ベトナム独立期の母語文字発明。",
    primary_source_url="http://www.hannom.org.vn/",
    primary_source_type="Vietnam Han-Nôm Research Institute",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"漢字文化圏",
         "description":"ベトナム漢喃文学は中国・朝鮮・日本・琉球と並ぶ漢字文化圏の文学伝統の南方周縁を成し、人類学的言語接触研究の重要対象。"}])

add(**C, name_ja="トー・ホアイ『デ・メン冒険記』",
    name_en="Tô Hoài's Adventures of a Cricket",
    name_original="Dế Mèn phiêu lưu ký",
    period_key="ベトナム近現代文学期",
    definition="トー・ホアイ（1920-2014）が1941年に発表した長編動物寓話。コオロギのデ・メンが旅を通じて成長する物語で、20世紀ベトナム児童文学の正典となり、英訳・露訳・仏訳含む40言語以上に翻訳された。1996年ホー・チ・ミン文学芸術賞受賞。ベトナム文学のグローバル受容の先駆例。",
    background="1940年代仏領インドシナ末期のハノイ文壇、児童文学・教化文学への需要。",
    development="戦後ベトナムの教育課程に組み込まれ、20世紀東南アジア児童文学の代表作として国際的に承認された。",
    historical_context="日仏共同統治期(1940-1945)直前のハノイ知識人活動、抗仏運動高揚前夜。",
    primary_source_url=WIKI_VI+"D%E1%BA%BF_M%C3%A8n_phi%C3%AAu_l%C6%B0u_k%C3%BD",
    primary_source_type="Wikipedia Vietnamese: Dế Mèn phiêu lưu ký",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ズオン・トゥー・フオン『盲目の楽園』",
    name_en="Dương Thu Hương's Paradise of the Blind",
    name_original="Những thiên đường mù",
    period_key="ベトナム近現代文学期",
    definition="ズオン・トゥー・フオン（1947-）が1988年に発表した長編小説。1950年代北ベトナムの土地改革と1980年代の幻滅を、女性主人公ハンの視点から描く。1991年仏訳でフェミナ賞外国部門候補、ベトナム国内発禁。1994年仏亡命後、ベトナム異論文学の代表的作家としてグローバル受容を獲得した。",
    background="ドイモイ政策（1986-）開始期の言論的相対自由と、土地改革記憶の文学的再検討。",
    development="バオ・ニン『戦争の悲しみ』、グエン・フイ・ティエップと並ぶドイモイ期文学の代表作となり、海外亡命知識人文学の系譜を形成した。",
    historical_context="1986年ドイモイ政策とベトナム共産党文芸統制、1989年ベルリンの壁崩壊期の社会主義文学再編。",
    primary_source_url=WIKI_EN+"D%C6%B0%C6%A1ng_Thu_H%C6%B0%C6%A1ng",
    primary_source_type="Wikipedia: Dương Thu Hương",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# D: タイ文学（5件）
# ============================================================
add(**C, name_ja="ラーマキエン",
    name_en="Ramakien",
    name_original="รามเกียรติ์",
    period_key="タイ古典・宮廷文学期",
    definition="タイ王権叙事詩。インド『ラーマーヤナ』のタイ的翻案で、ラーマ一世王（在位1782-1809）が1797年に詔勅で編纂、ラーマ六世王が改訂。バンコク王宮ワット・プラケーオ（エメラルド寺院）回廊壁画の主題となり、コーン仮面舞踊劇の中核脚本。タイ王権イデオロギーの文学的中核を成す。",
    background="アユタヤ朝期のラーマーヤナ受容、ラタナコーシン朝建国期の王権イデオロギー再編。",
    development="コーン仮面舞踊劇・人形劇・現代タイ文学・映画にまで継承され、東南アジア・ラーマーヤナ伝統の中で最も精緻な王権叙事化を果たした。",
    historical_context="1782年ラタナコーシン朝建国とバンコク遷都、王権再正統化期。",
    primary_source_url=WSRC_TH+"%E0%B8%A3%E0%B8%B2%E0%B8%A1%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B8%A2%E0%B8%A3%E0%B8%95%E0%B8%B4%E0%B9%8C",
    primary_source_type="Wikisource Thai: รามเกียรติ์",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ラーマーヤナ伝統と東南アジア王権",
         "description":"ラーマキエンはインド・ラーマーヤナの東南アジア的王権叙事化として、人類学的王権論・物語伝播研究の中心対象。"}])

add(**C, name_ja="クンチャン・クンペーン",
    name_en="Khun Chang Khun Phaen",
    name_original="ขุนช้างขุนแผน",
    period_key="タイ古典・宮廷文学期",
    definition="アユタヤ期に成立し19世紀ラーマ二世王代に正典化されたタイ口承叙事詩。豪商クンチャンと武将クンペーンの女性ワンタオンを巡る三角関係を、約2万行のセープハー（朗唱詩形）で展開する。タイ庶民文化と宮廷文化の融合作品で、英訳（Baker & Phongpaichit, 2010）以後グローバル受容を獲得した。",
    background="アユタヤ期(1351-1767)の口承伝統、ラタナコーシン朝期の宮廷的整理・出版。",
    development="現代タイ国民教育課程の正典作品となり、ベイカー＝ポンパイチット英訳によりタイ古典文学のグローバル代表作となった。",
    historical_context="アユタヤ朝末期の社会変動とラタナコーシン朝期の文学正典化。",
    primary_source_url=WSRC_TH+"%E0%B8%82%E0%B8%B8%E0%B8%99%E0%B8%8A%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%82%E0%B8%B8%E0%B8%99%E0%B9%81%E0%B8%9C%E0%B8%99",
    primary_source_type="Wikisource Thai: ขุนช้างขุนแผน",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="シーブーラパー『絵画の背景』",
    name_en="Siburapha's Behind the Painting",
    name_original="ข้างหลังภาพ",
    period_key="タイ近現代文学期",
    definition="シーブーラパー（クラープ・サーイプラディット、1905-1974）が1937年に発表した中編小説。日本留学中のタイ人青年と既婚伯爵夫人の恋愛悲劇を描き、近代タイ短編小説の方法的革新を達成した。1980-90年代に2度映画化され、20世紀タイ近代文学の正典となった。",
    background="1930年代立憲革命期(1932)のタイ知識人の近代化志向、シーブーラパー自身の日本訪問体験。",
    development="後の社会派タイ小説（ククリット、シーダーオルアン）に直結する、タイ近代心理小説の規範作品となった。",
    historical_context="1932年立憲革命と1930年代タイの近代化加速、日タイ友好関係深化期。",
    primary_source_url=WIKI_TH+"%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%A0%E0%B8%B2%E0%B8%9E",
    primary_source_type="Wikipedia Thai: ข้างหลังภาพ",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="チャート・コープチッティ『判決』",
    name_en="Chart Korbjitti's The Judgement",
    name_original="คำพิพากษา",
    period_key="タイ近現代文学期",
    definition="チャート・コープチッティ（1954-）が1981年に発表した長編小説。タイ農村の青年ファークが共同体の冤罪的判決により破滅していく構造を描き、1982年タイ国家文学賞、1983年第1回東南アジア文学賞（S.E.A. Write Award）を受賞。タイ社会派文学の頂点とされる。",
    background="1970年代タイ学生運動の挫折(1973-76)と、農村社会の構造的暴力への文学的応答。",
    development="プラパッサーン・セーウィークン、ウィン・ラオワーリン、現代タイ社会派長編の規範作品となった。",
    historical_context="1980年代プレム政権下のタイ社会、農村開発と都市化の緊張期。",
    primary_source_url=WIKI_TH+"%E0%B8%84%E0%B8%B3%E0%B8%9E%E0%B8%B4%E0%B8%9E%E0%B8%B2%E0%B8%81%E0%B8%A9%E0%B8%B2",
    primary_source_type="Wikipedia Thai: คำพิพากษา",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="プラープダー・ユン",
    name_en="Prabda Yoon",
    name_original="ปราบดา หยุ่น",
    period_key="タイ近現代文学期",
    definition="プラープダー・ユン（1973-）はタイの作家・映画製作者・グラフィックデザイナー。短編集『可能性（Probability）』(2000)で東南アジア文学賞受賞、米国留学を経たポストモダン散文・実験的短編で2000年代タイ文学の新世代を代表する。アピチャートポン・ウィーラセータクン映画への参加もあり、タイ現代芸術圏の中心人物。",
    background="2000年代タイのグローバル化加速、米国留学世代知識人の帰還、コンテンポラリー・アート文化興隆。",
    development="ウタイラオン、リンチー・ウィーラパッタナーリンら現代タイ実験文学世代の起点となり、東南アジア現代文学のグローバル受容を牽引した。",
    historical_context="2000年代タクシン政権期のタイ社会変動と、グローバル化下の都市知識人文化。",
    primary_source_url=WIKI_EN+"Prabda_Yoon",
    primary_source_type="Wikipedia: Prabda Yoon",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# E: インドネシア・マレー（5件）
# ============================================================
add(**C, name_ja="マレー・パントゥン",
    name_en="Malay pantun",
    name_original="pantun",
    period_key="マレー・インドネシア古典口承期",
    definition="マレー世界（現在のマレーシア・インドネシア・シンガポール・ブルネイ）の口承伝統的詩形式。4行を基本とし、前半2行（プンバヤン、自然・風景）と後半2行（マクスッド、教訓・恋愛・哲学）の対応構造を持つ。2020年UNESCO人類無形文化遺産。500年以上の口承継承を持つマレー世界の文学的核。",
    background="14-15世紀マラッカ王国期以降のマレー口承伝統、海域交流による形式の広範な拡散。",
    development="近代インドネシア新詩運動（プジャンガ・バル）、マレーシア国民文学、シンガポール多言語文学に継承され、現代もマレー語圏文学アイデンティティの核を成す。",
    historical_context="マラッカ王国期(1400-1511)以降の海域マレー世界における口承文芸ネットワーク。",
    primary_source_url=WSRC_ID+"Pantun",
    primary_source_type="Wikisource Indonesian: Pantun",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"invariant",
         "rationale":"パントゥンは口承・即興・多話者対話を含む生身の詩形式であり、AI生成リズム詩との対比軸として、口承詩形式の身体性・社会性を理論化する。",
         "related_ai_phenomenon":"AI生成詩の音律性 vs 口承詩の対話的即興性"}])

add(**C, name_ja="シャイル詩形",
    name_en="syair",
    name_original="syair",
    period_key="マレー・インドネシア古典口承期",
    definition="マレー世界の伝統的長編叙事詩形式。aaaa脚韻を持つ4行連作で、宗教的物語・歴史・恋愛・教訓を扱う。ハムザ・ファンスーリ（16世紀末アチェ）以降の体系化を経て、19世紀末まで写本形式で広範に流通。アブドゥラ・アブドゥルカディール・ムンシ『アブドゥラ物語』(1849)などを含む、マレー古典文学の主要形式。",
    background="アチェ・スルタン国期のスーフィー詩学受容と、マレー世界の写本文化興隆。",
    development="19世紀末マレー新聞・書籍出版文化への移行で衰退するが、現代マレーシア・インドネシアでは伝統文学保存対象として研究・教育される。",
    historical_context="16-19世紀マレー世界のスーフィー伝統と海域交流期。",
    primary_source_url=WIKI_ID+"Syair",
    primary_source_type="Wikipedia Indonesian: Syair",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="プラムディヤ・アナンタ・トゥール『人間の大地』",
    name_en="Pramoedya Ananta Toer's This Earth of Mankind",
    name_original="Bumi Manusia",
    period_key="インドネシア・マレーシア近現代期",
    definition="プラムディヤ・アナンタ・トゥール（1925-2006）が1980年に発表した『ブル四部作』第一作。蘭印支配末期のジャワ青年ミンケと混血女性アンネリースの恋愛を通じて、植民地的近代と民族意識覚醒を描く。プラムディヤがブル島流刑中に口述で構想・執筆。1981年禁書指定、現代インドネシア文学の正典作品。",
    background="スハルト体制下(1966-1998)のインドネシア政治犯としてのプラムディヤのブル島流刑(1969-1979)体験、20世紀初頭インドネシア民族運動の歴史的記憶。",
    development="国際的に37言語翻訳、ノーベル文学賞最有力候補と長年見なされ、ポストコロニアル文学・第三世界文学研究の中心対象となった。",
    historical_context="1880-1900年代蘭印植民地体制の文学的再構成と、スハルト期反共体制下の発禁文学。",
    primary_source_url=WIKI_ID+"Bumi_Manusia",
    primary_source_type="Wikipedia Indonesian: Bumi Manusia",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"植民地的近代と民族意識",
         "description":"プラムディヤ・ブル四部作は、植民地的近代主体の形成を文学化する典型として、ポストコロニアル人類学（ベネディクト・アンダーソン、ジョン・ペンバートン）と密接に対応する。"}])

add(**C, name_ja="アユ・ウタミ『サマン』",
    name_en="Ayu Utami's Saman",
    name_original="Saman",
    period_key="インドネシア・マレーシア近現代期",
    definition="アユ・ウタミ（1968-）が1998年に発表した長編小説。スハルト体制末期に出版され、女性4人の友情・性・宗教・政治を断章的構造で描く。スハルト体制崩壊直後のインドネシア「サストラ・ワンギ（香りある文学）」と呼ばれる女性作家世代を象徴する作品となった。1998年ジャカルタ芸術評議会賞、英訳（Pamela Allen, 2005）。",
    background="1998年スハルト退陣前後のインドネシア社会変動、女性知識人世代のフェミニズム的覚醒。",
    development="後のレイラ・チュドリ、デウィ・レスタリら「サストラ・ワンギ」世代女性文学を牽引し、現代インドネシア文学のグローバル受容を加速した。",
    historical_context="1998年スハルト体制崩壊と「レフォルマシ（改革）」期のインドネシア社会。",
    primary_source_url=WIKI_EN+"Saman_(novel)",
    primary_source_type="Wikipedia: Saman (novel)",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エカ・クルニアワン『美はそこにある傷』",
    name_en="Eka Kurniawan's Beauty Is a Wound",
    name_original="Cantik itu Luka",
    period_key="インドネシア・マレーシア近現代期",
    definition="エカ・クルニアワン（1975-）が2002年に発表した長編小説。20世紀インドネシアの蘭印末期・日本占領期・独立戦争・1965年共産党虐殺・スハルト期を、ジャワ娼婦デウィ・アユとその子孫の四世代史で描く。マジック・リアリズム的手法でガルシア・マルケスのインドネシア的応答と評され、英訳（New Directions, 2015）でManを獲得。",
    background="2000年代レフォルマシ期のインドネシアで初めて公然と論じられた1965年虐殺記憶、世界文学・ラテンアメリカ文学受容。",
    development="インドネシア・ポスト・スハルト期文学のグローバル代表作となり、ポストコロニアル・マジックリアリズム理論の東南アジア事例として研究された。",
    historical_context="2000年代インドネシア民主化と1965年虐殺記憶の文学化解禁期。",
    primary_source_url=WIKI_ID+"Cantik_Itu_Luka",
    primary_source_type="Wikipedia Indonesian: Cantik Itu Luka",
    importance_score=3, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"マジック・リアリズム手法の東南アジア展開は、AIによる「事実と幻想の融合」生成の文学的祖型として再読可能。",
         "related_ai_phenomenon":"AI生成における事実-幻想境界の流動化"}])


# ============================================================
# F: フィリピン文学（5件）
# ============================================================
add(**C, name_ja="フランシスコ・バラグタス『フロランテとラウラ』",
    name_en="Francisco Balagtas's Florante at Laura",
    name_original="Florante at Laura",
    period_key="フィリピン古典・スペイン期",
    definition="フランシスコ・バラグタス（1788-1862）が1838年に発表したタガログ語ロマン叙事詩。アヴァジニア王国の貴族フロランテと姫ラウラの愛と試練を、12音節4行のアウィット詩形で描く。スペイン植民地期最高のタガログ詩文学とされ、リサールが少年期に深く影響を受けた、フィリピン民族文学の起点作品。",
    background="19世紀前半フィリピン・スペイン植民地期の口承詩・印刷文化興隆、タガログ語文学的精緻化。",
    development="リサール『ノリ・メ・タンヘレ』『エル・フィリブステリスモ』、20世紀タガログ詩、アマド・ヘルナンデス、現代フィリピン民族文学の祖型となった。",
    historical_context="19世紀前半マニラのスペイン語・タガログ語混在文化、独立運動前夜の社会的緊張。",
    primary_source_url=WSRC_EN+"Florante_at_Laura",
    primary_source_type="Wikisource: Florante at Laura",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="リサール『エル・フィリブステリスモ』",
    name_en="Rizal's El Filibusterismo",
    name_original="El Filibusterismo",
    period_key="フィリピン古典・スペイン期",
    definition="ホセ・リサール（1861-1896）が1891年にゲント（ベルギー）で発表したスペイン語長編小説、『ノリ・メ・タンヘレ』(1887)の続編。革命家シモウン（イバラの偽名）がスペイン植民地体制への武装蜂起を企てる構造を通じて、植民地体制の構造的不正義を批判した。1896年リサール処刑の直接的契機となり、フィリピン革命の文学的源泉となった。",
    background="1890年代スペイン植民地体制末期のフィリピン民族運動、リサール自身のヨーロッパ亡命体験と植民地批判。",
    development="フィリピン独立革命(1896-)の精神的基盤となり、20世紀フィリピン民族文学の正典作品となった。1956年「リサール法」で全大学必修教材に指定。",
    historical_context="1872年カビテ事件以降の植民地体制矛盾激化、1896年フィリピン革命勃発前夜。",
    primary_source_url=GUTEN+"ebooks/10676",
    primary_source_type="Project Gutenberg: El Filibusterismo",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="フランシスコ・シオニル・ホセ『ロサーレス五部作』",
    name_en="F. Sionil José's Rosales Saga",
    name_original="Rosales Saga",
    period_key="フィリピン近現代文学期",
    definition="フランシスコ・シオニル・ホセ（1924-2022）が1973-2000年に発表した5巻の長編連作。『木』『仮面の舞踏者』『私の兄、私の処刑人』『プエルト』『マサ』を含み、ルソン島ロサーレス村を起点に、19世紀末スペイン期から1980年代マルコス独裁期までのフィリピン現代史を描く。1980年マグサイサイ賞（文学）、ノーベル文学賞候補とされた。",
    background="フィリピン20世紀社会変動と、シオニル・ホセ自身のロサーレス村出身体験。",
    development="ニック・ホアキン、ジョセ・ガルシア・ヴィラと並ぶフィリピン20世紀英語文学三巨匠の一人として、東南アジア英語文学の代表作となった。",
    historical_context="マルコス戒厳令期(1972-1981)のフィリピン政治状況と、海外読者向け英語文学の戦略的選択。",
    primary_source_url=WIKI_EN+"F._Sionil_Jos%C3%A9",
    primary_source_type="Wikipedia: F. Sionil José",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ニック・ホアキン",
    name_en="Nick Joaquin",
    name_original="Nick Joaquin",
    period_key="フィリピン近現代文学期",
    definition="ニック・ホアキン（1917-2004）はフィリピンを代表する英語作家。短編集『熱帯の真夏の女』(1972)、戯曲『フィリピンの芸術家としての肖像』(1966)、歴史評論『フィリピン・スペイン裏面史』(1966)で、スペイン的・カトリック的フィリピン文化の複雑な遺産を主題化した。1976年フィリピン国民芸術家（文学）。",
    background="20世紀前半フィリピン・スペイン語=英語転換期、米国植民地期(1898-1946)のフィリピン英語文学制度確立。",
    development="フランシスコ・シオニル・ホセ、後の世代のレッセイ・カモテス、現代フィリピン英語文学の正典的源流となった。",
    historical_context="米国植民地期のフィリピン英語化政策と、1946年独立後の文学的アイデンティティ模索期。",
    primary_source_url=WIKI_EN+"Nick_Joaquin",
    primary_source_type="Wikipedia: Nick Joaquin",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C,
    name_ja="フィリピン口承叙事詩（フダ・フダ・イバロイ等）",
    name_en="Philippine oral epics",
    name_original="oral epics (Hudhud, Ibalon, Darangen)",
    period_key="フィリピン古典・スペイン期",
    definition="スペイン植民地化以前から伝承されたフィリピン諸民族の口承叙事詩群。ルソン島イフガオ族「フダ・フダ」（2001年UNESCO人類無形文化遺産）、ビコール「イバロン」、ミンダナオ・マラナオ「ダランゲン」（2005年UNESCO登録）が代表的。先住民族の宇宙論・歴史・倫理を伝える、植民地化以前のフィリピン文学的核。",
    background="紀元前千年紀以降のフィリピン諸島先住民族文化、口承伝統の千年級継承。",
    development="20世紀E・アルセニオ・マヌエル等の人類学的記録活動、UNESCO登録による現代的保護、先住民族文学運動への組込。",
    historical_context="スペイン植民地化(1565-)以前の千年規模の口承文化と、20世紀以降の文献化運動。",
    primary_source_url=WIKI_EN+"Hudhud",
    primary_source_type="Wikipedia: Hudhud (UNESCO ICH)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"口承叙事詩と先住民知識",
         "description":"フィリピン口承叙事詩は人類学的口承文芸研究および先住民族知識保存運動の中核対象であり、UNESCO人類無形文化遺産制度の主要事例。"}])


# ============================================================
# G: カンボジア・ラオス（4件）
# ============================================================
add(**C, name_ja="リアムケー（カンボジア・ラーマーヤナ）",
    name_en="Reamker (Cambodian Ramayana)",
    name_original="រាមកេរ្តិ៍",
    period_key="カンボジア・ラオス古典期",
    definition="カンボジアにおけるラーマーヤナの翻案叙事詩。16-17世紀の詩形整理を経て、19世紀アンドゥオン王代に体系化された。アンコール・ワット回廊レリーフ（12世紀）にも描かれ、王宮古典舞踊（ロバム）・影絵劇（スバエック・トム）の中核脚本。タイ「ラーマキエン」と並ぶ東南アジア・ラーマーヤナ伝統の代表的形態。",
    background="アンコール期(802-1431)のヒンドゥー教受容と、後期クメール文学の整理期。",
    development="ポル・ポト体制(1975-1979)による文化破壊から、戦後ロバム古典舞踊復興と共に再構築され、現代カンボジア文化アイデンティティの核となった。",
    historical_context="アンコール期から19世紀フランス保護領化(1863)直前までのクメール宮廷文化。",
    primary_source_url=WIKI_EN+"Reamker",
    primary_source_type="Wikipedia: Reamker",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="クメール文学とポル・ポト後の再生",
    name_en="Khmer literature after Pol Pot",
    name_original="អក្សរសិល្ប៍ខ្មែរ",
    period_key="カンボジア・ラオス古典期",
    definition="1975-79年のポル・ポト体制下、推定9割の知識人が殺害され、写本・印刷物が大規模破壊されたクメール文学の壊滅と、1979年以降の再生過程。プレア・タット・コーゴン王女、ピチ・タダ、グエック・ヘー・カモル等の戦後作家群が、虐殺記憶と古典伝統の再接続を試みている。21世紀ディアスポラ作家（米国・仏のカンボジア系）の活動を含む。",
    background="20世紀クメール民族主義文学（プレア・タット・ノク等）の戦前蓄積と、1975-79年の総体的破壊。",
    development="DC-Cam（カンボジア虐殺記録センター）等によるアーカイブ再構築、ディアスポラ作家（ブッダ・ボープ等）の英仏語文学活動の興隆。",
    historical_context="ポル・ポト体制の文化破壊と、戦後カンボジアにおける記憶・正義の文学化。",
    primary_source_url=WIKI_EN+"Cambodian_literature",
    primary_source_type="Wikipedia: Cambodian literature",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"クメール文学のポル・ポト後再生は、文学伝統の物理的断絶からの再構築を象徴する。AI時代における失われた文化資料のデジタル/AI復元と理論的に並行する事例。",
         "related_ai_phenomenon":"AI支援による失われた文化資料の復元・再構築"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"文化的ジェノサイドと記憶",
         "description":"クメール文学の戦後再生は、文化的ジェノサイドと記憶の人類学（アラン・ハインドマン他）の中心事例として位置づけられる。"}])

add(**C, name_ja="サン・シンサイ",
    name_en="Sang Sinxay",
    name_original="ສັງສິນໄຊ",
    period_key="カンボジア・ラオス古典期",
    definition="ラオスを代表する古典叙事詩。17-18世紀ラーンサーン王国期の詩人パンヤー・パングカム（伝承）が著したとされ、王子シンサイの英雄譚を約2万行のクロン・サット詩形で描く。仏教ジャータカ伝統と王権叙事の融合作品で、ラオス国民文学の核心であり、隣接タイ東北イサーン地方でも広く流通した。",
    background="ラーンサーン王国期(1353-1707)のラオス宮廷文化と、上座部仏教ジャータカ伝統。",
    development="20世紀ラオス国民国家形成期に正典化され、現代ラオス文学教育の中核教材となった。タイ・イサーン地方ではモーラム（伝統歌謡）の重要レパートリー。",
    historical_context="ラーンサーン王国分裂期(1707)以前のラオス宮廷文学最盛期。",
    primary_source_url=WIKI_EN+"Sang_Sinxay",
    primary_source_type="Wikipedia: Sang Sinxay",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ラオス・ジャータカ文学伝統",
    name_en="Lao Jataka tradition",
    name_original="ຊາດົກລາວ",
    period_key="カンボジア・ラオス古典期",
    definition="ラオスにおける仏典ジャータカ（仏陀前生譚）の口承・写本伝統。パーリ語仏典の正統547話に加え、地域固有の「外典ジャータカ（パンニャーサ・ジャータカ、50話）」が広範に流通した。ヤシ葉写本（バイ・ラーン）形式で寺院（ワット）に保管され、パンサー（雨安居）期の説法文学として伝承される、ラオス上座部仏教文化の文学的核。",
    background="14世紀以降のラーンサーン王国期上座部仏教国教化、寺院教育における写本文化興隆。",
    development="現代ラオス国立図書館・東洋写本研究所（フランス極東学院）のヤシ葉写本デジタル化プロジェクトを経て、グローバル仏教文学研究の重要対象となった。",
    historical_context="14-19世紀ラオス上座部仏教文化圏の形成と、寺院教育制度の確立。",
    primary_source_url=WIKI_EN+"Pa%C3%B1%C3%B1%C4%81sa_J%C4%81taka",
    primary_source_type="Wikipedia: Paññāsa Jātaka",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ジャータカ伝統と仏教文学圏",
         "description":"ラオス・ジャータカ文学はタイ・カンボジア・ミャンマー・スリランカと連動する上座部仏教文学圏の地域形態として、宗教人類学・仏教学の対象。"}])


# ============================================================
# H: ビルマ＆東南アジア横断（5件）
# ============================================================
add(**C, name_ja="ビルマ古典詩形（ヤドゥ・ヤガン）",
    name_en="Burmese classical verse forms (yadu, yagan)",
    name_original="ရတု・ရကန်",
    period_key="ビルマ（ミャンマー）古典・近代期",
    definition="ビルマ古典文学の主要詩形群。「ヤドゥ（ratu）」は4-7音節の三節構造で季節・自然詠を中核とし、「ヤガン（rakan）」は教訓的長編叙事詩形。15世紀第一トングー朝期から19世紀コンバウン朝末期まで、ビルマ宮廷文学の中核形式として精緻化された。シン・マハー・ラッタタラ、シン・ウッタマジョー等の著名詩人を輩出。",
    background="14-15世紀ビルマ古典詩学の成立と、上座部仏教・宮廷文化の融合。",
    development="19世紀末英領期(1886-1948)に近代散文・小説に置換されるが、現代ミャンマーでも国民教育の古典教材として継承される。",
    historical_context="第一・第二トングー朝、コンバウン朝（1752-1885）のビルマ古典文学最盛期。",
    primary_source_url=WIKI_EN+"Burmese_literature",
    primary_source_type="Wikipedia: Burmese literature",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ジャー『カム・スゥエ・ミィン』",
    name_en="Journal Kyaw Ma Ma Lay's Not Out of Hate",
    name_original="မုန်းတီးခြင်းကြောင့်မဟုတ်ပါ",
    period_key="ビルマ（ミャンマー）古典・近代期",
    definition="ビルマの女性作家ジャーナル・チョー・マ・マ・レー（1917-1982）が1955年に発表した長編小説。1930年代英領ビルマの伝統的ビルマ女性プェ・ピューと英国式生活を志向するビルマ人男性ウ・ソウ・ハンの結婚生活を描く。1955年ビルマ国家文学賞、1991年英訳（Margaret Aung-Thwin）で国際的承認を得たビルマ近代女性文学の代表作。",
    background="1930-50年代英領ビルマから独立期(1948)までの社会変動、女性知識人の覚醒期。",
    development="2010年代ミャンマー民主化に伴う英訳普及で、東南アジア・フェミニズム文学研究の対象として再評価された。",
    historical_context="独立直後ビルマの社会変動と、女性作家の制度的地位確立期。",
    primary_source_url=WIKI_EN+"Journal_Kyaw_Ma_Ma_Lay",
    primary_source_type="Wikipedia: Journal Kyaw Ma Ma Lay",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="東南アジア・コロニアル小説",
    name_en="Southeast Asian colonial novel",
    name_original="colonial novel",
    period_key="東南アジア横断的・地域比較期",
    definition="19世紀末-20世紀前半の東南アジア各国（蘭領東インド・仏領インドシナ・英領マレー＝ビルマ・米領フィリピン）で、植民地行政官・宣教師・移住者により執筆された欧文小説群。マルチャテゥリ『マックス・ハーフェラール』(1860)、コンラッド『ロード・ジム』(1900)、フォーン・ウェスターハウト『恐ろしき美』(1890)等、植民地経験を文学化した重要作品群。",
    background="19世紀後半東南アジア植民地体制確立期と、欧米読者向け植民地文学市場の形成。",
    development="20世紀後半のポストコロニアル批評（サイード、スピヴァク、グハ）により、植民地視線・他者表象研究の主要対象となった。",
    historical_context="蘭領東インド倫理政策(1901)、仏領インドシナ統合(1887)、米西戦争(1898)期の東南アジア植民地体制再編期。",
    primary_source_url=WIKI_EN+"Colonial_literature",
    primary_source_type="Wikipedia: Colonial literature",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"植民地表象と他者性",
         "description":"東南アジア・コロニアル小説はサイード『オリエンタリズム』(1978)以降のポストコロニアル人類学・文化研究の中心対象。"}])

add(**C, name_ja="東南アジア英語文学（SEA Anglophone literature）",
    name_en="Southeast Asian Anglophone literature",
    name_original="SEA Anglophone literature",
    period_key="東南アジア横断的・地域比較期",
    definition="シンガポール・マレーシア・フィリピン・ミャンマー等を中心とする、英語による東南アジア現代文学。エドウィン・ティアンボ、シャリル・S・ダース、ニック・ホアキン、F・シオニル・ホセ、タン・トゥアン・エン『静かなる雨の庭』(2007)、レット・テラのMan Booker候補（2011）等を含む。グローバル英語文学圏の南方拡大を象徴する。",
    background="20世紀後半シンガポール・マレーシア独立後の英語政策、フィリピン米国植民地期(1898-1946)の英語文化的遺産。",
    development="2000年代以降のグローバル英語文学市場拡大に伴い、Man Booker・国際ブッカー賞・コモンウェルス賞の有力候補ジャンルとなった。",
    historical_context="20世紀後半東南アジア国家独立と、英語をリンガフランカ・文学言語とする戦略的選択。",
    primary_source_url=WIKI_EN+"Singapore_literature_in_English",
    primary_source_type="Wikipedia: SEA Anglophone literature",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"東南アジア英語文学は、AI翻訳普及前の「英語による南方表象」を象徴する。AI翻訳普及後の母語直接グローバル化との対比で、英語覇権・翻訳経済を再考する基準点。",
         "related_ai_phenomenon":"AI翻訳による母語直接グローバル化と英語覇権の再編"}])

add(**C, name_ja="東南アジア・ディアスポラ文学",
    name_en="SE Asian diaspora literature",
    name_original="diaspora literature",
    period_key="東南アジア横断的・地域比較期",
    definition="20世紀後半以降の東南アジア出身者・系譜による海外（米・仏・豪・英・加）拠点の文学活動。ベトナム系（ヴィエト・タン・グエン『同情者』2015）、フィリピン系（ジェシカ・ハグドルン、エルネスト・キニョネス）、カンボジア系（ヴァディ・ラトナー）、シンガポール系（ケヴィン・クワン）、マレーシア系（タッシュ・アウ）の作家を含む。グローバル英語文学市場の重要構成要素。",
    background="20世紀後半東南アジア戦争・体制変動による大規模海外移住と、移民第二・第三世代の文学的覚醒。",
    development="ヴィエト・タン・グエン『同情者』(2016ピューリッツァー賞)、現代米国文学の主流形成に寄与し、東南アジア研究と移民文学研究の交差点を形成した。",
    historical_context="ベトナム戦争(1975)、カンボジア虐殺(1975-79)、フィリピン戒厳令(1972-81)等を背景とする海外移住期。",
    primary_source_url=WIKI_EN+"Vietnamese_diaspora",
    primary_source_type="Wikipedia: SE Asian diaspora literature",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ディアスポラ文学は複数言語・複数アイデンティティの主体を文学化する。AI時代の多重ペルソナ・言語横断生成と理論的に共振する祖型。",
         "related_ai_phenomenon":"AI生成における多重アイデンティティ・言語横断主体"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ディアスポラと文化的アイデンティティ",
         "description":"東南アジア・ディアスポラ文学は、人類学的ディアスポラ研究（ジェイムズ・クリフォード、アルジュン・アパドゥライ）と密接に連動し、グローバル化下のアイデンティティ論の中心対象。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    skipped_keys: list[str] = []

    # Strip placeholder keys (defensive: some entries may carry stray keys)
    for c in CONCEPTS:
        for k in list(c.keys()):
            if k.startswith("name_ji"):
                c.pop(k)

    with LitDB() as db:
        # Create periods
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="グローバルサウス",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid

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
                print(f"  [error] {entry.get('name_ja','?')}: {e}")
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
        print(f"[c27-add] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c27-add] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
