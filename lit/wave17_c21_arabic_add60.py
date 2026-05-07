"""LIT-DB Phase 2 Wave 17 — C21: Arabic literature ADD 60 (extension).

Subfield: lit_arabic (id=13), region='南西アジア'.
Adds 60 NEW NON-OVERLAPPING concepts on top of existing 80, covering:
  A. Jahiliyya poets / Mu'allaqat individual (10)
  B. Early Islamic / Umayyad poetry (8)
  C. Abbasid poetry detail (10)
  D. Classical prose extensions (6)
  E. Maqamat full corpus (4)
  F. Andalusi extensions (6)
  G. Mamluk-Ottoman / popular sira (4)
  H. Nahda / Mahjar (5)
  I. Modern poetry / novel detail (4)
  J. Maghreb / 21c contemporary (3)

Sources: Al-Shamela, OpenITI, Wikisource Arabic, archive.org, EI2/EI3, Britannica.
>= 70% primary; fourth_transform_tags >= 18, cross_domain >= 14.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("ジャーヒリーヤ期", "Jahiliyya (Pre-Islamic)", -500, 622,
     "イスラーム以前のアラビア半島の口承詩文化期。"),
    ("初期イスラーム・ウマイヤ朝期", "Early Islamic / Umayyad", 622, 750,
     "預言者ムハンマドの活動期からウマイヤ朝期にかけてのアラブ詩・宗教文学の展開期。"),
    ("アッバース朝古典期", "Abbasid Classical", 750, 1258,
     "バグダード・カイロを中心に展開した古典アラブ散文・詩の黄金期。"),
    ("アンダルス期", "Al-Andalus (Umayyad–Nasrid)", 711, 1492,
     "イベリア半島のイスラーム支配下で展開したアラビア語文学。"),
    ("マムルーク・オスマン期", "Mamluk–Ottoman Arabic", 1258, 1798,
     "アッバース朝崩壊後からナフダ前夜までのアラブ文学期。"),
    ("ナフダ期（近代復興）", "Nahda (Modern Revival)", 1798, 1945,
     "ナポレオンのエジプト遠征以降のアラブ近代化期。"),
    ("現代アラブ文学期", "Modern / Contemporary Arabic", 1945, 2025,
     "独立期以降の小説・自由詩・離散文学・マグレブ文学を含む現代アラブ文学。"),
]


SHAMELA = "https://shamela.ws/"
OPENITI = "https://openiti.org/"
WSRC_AR = "https://ar.wikisource.org/wiki/"
WIKI_AR = "https://ar.wikipedia.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
EI_BRILL = "https://referenceworks.brillonline.com/browse/encyclopaedia-of-islam-2"
BRITT = "https://www.britannica.com/"
ARCHIVE = "https://archive.org/details/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_arabic", region="南西アジア",
         original_script="arabic")


# ============================================================
# A. ジャーヒリーヤ期詩・ムアッラカート個別（10件）
# ============================================================
add(**C, name_ja="イムルウル・カイス『ムアッラカ』",
    name_en="Mu'allaqa of Imru' al-Qais",
    name_original="معلقة امرئ القيس",
    period_key="ジャーヒリーヤ期",
    definition="ムアッラカート筆頭の長編カスィーダ。「ここに留まれ、二人の友よ」で開始する廃墟詩(アトラール)から夜の情景・砂漠彷徨・嵐描写まで展開。古典アラブ詩の構造規範を確立した6世紀の代表作。",
    background="キンダ族王家の没落、6世紀アラビア半島部族抗争。",
    development="後の全カスィーダ構成の規範となり、アラブ詩学の古典的範型を確立。",
    historical_context="プレイスラーム期半島の口承詩伝統、市場ウカーズの詩集会。",
    primary_source_url=WSRC_AR+"معلقة_امرئ_القيس",
    primary_source_type="Wikisource Arabic: Mu'allaqa of Imru' al-Qais",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="タラファ『ムアッラカ』",
    name_en="Mu'allaqa of Tarafa",
    name_original="معلقة طرفة بن العبد",
    period_key="ジャーヒリーヤ期",
    definition="バクル族のタラファ・イブン・アル＝アブド（543頃-569頃）の代表作。雌駱駝の精緻な解剖学的描写と、若くして死を予感する青年の享楽哲学が結合した103句のカスィーダ。",
    background="バフレーン地域バクル族とタグリブ族の部族抗争、若年詩人の宮廷出仕。",
    development="駱駝描写の規範例として後代詩学注釈の中心対象となった。",
    historical_context="6世紀後半ヒーラ・ラフム朝宮廷文化。",
    primary_source_url=WSRC_AR+"معلقة_طرفة_بن_العبد",
    primary_source_type="Wikisource Arabic: Mu'allaqa of Tarafa",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ズハイル『ムアッラカ』",
    name_en="Mu'allaqa of Zuhayr ibn Abi Sulma",
    name_original="معلقة زهير بن أبي سلمى",
    period_key="ジャーヒリーヤ期",
    definition="ムザイナ族のズハイル・イブン・アビー・スルマー（520頃-609）の代表作。アブス族・ズビヤーン族間のダーヒス戦争停戦を讃える賢者詩で、人生省察と道徳的箴言の集積として古典アラブ詩学の知恵詩(ヒクマ)規範となった。",
    background="アブス・ズビヤーン40年戦争の終結、部族間和解。",
    development="道徳・知恵詩の古典的規範となり、ジャーヒズ等のアダブ作家が箴言を頻繁に引用。",
    historical_context="6世紀末アラビア半島中部の部族同盟再編。",
    primary_source_url=WSRC_AR+"معلقة_زهير_بن_أبي_سلمى",
    primary_source_type="Wikisource Arabic: Mu'allaqa of Zuhayr",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ラビード『ムアッラカ』",
    name_en="Mu'allaqa of Labid ibn Rabi'a",
    name_original="معلقة لبيد بن ربيعة",
    period_key="ジャーヒリーヤ期",
    definition="アーミル族のラビード（560頃-661）が著したムアッラカ。廃墟詩の規範句「廃墟は朽ちた、留まる地も移動する地も」で開始し、自然描写・部族讃美・人生哲学を展開。後にイスラームに改宗し、長寿のサハーバ詩人として『預言者の最も真実の言葉』のハディースで言及される。",
    background="ヒジャーズ部族文化、後年のイスラーム受容。",
    development="廃墟詩の正典的範型として後代カスィーダ全般に継承された。",
    historical_context="6世紀末から7世紀ヒジャーズ部族文化の転換期。",
    primary_source_url=WSRC_AR+"معلقة_لبيد",
    primary_source_type="Wikisource Arabic: Mu'allaqa of Labid",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アンタラ『ムアッラカ』",
    name_en="Mu'allaqa of Antara ibn Shaddad",
    name_original="معلقة عنترة بن شداد",
    period_key="ジャーヒリーヤ期",
    definition="アブス族の混血戦士詩人アンタラ（525頃-608頃）の代表作。アビーラとの恋と部族戦闘での武勇を一篇に統合し、後の民衆英雄譚『アンタル物語』の祖型詩となった。",
    background="アブス族とエチオピア人女奴隷との混血、ダーヒス戦争での活躍。",
    development="後代『シーラト・アンタル』民衆英雄譚の源泉。アラブ騎士道(フトゥウワ)文学の祖型。",
    historical_context="6世紀末アラビア半島の部族戦争と混血戦士の社会的位置。",
    primary_source_url=WSRC_AR+"معلقة_عنترة",
    primary_source_type="Wikisource Arabic: Mu'allaqa of Antara",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アムル・イブン・クルスーム『ムアッラカ』",
    name_en="Mu'allaqa of Amr ibn Kulthum",
    name_original="معلقة عمرو بن كلثوم",
    period_key="ジャーヒリーヤ期",
    definition="タグリブ族のアムル・イブン・クルスーム（526頃-584頃）が著した部族自賛詩(ファフル)の代表作。バスース戦争でのバクル族との抗争を背景に、タグリブ族の栄光を誇示する。",
    background="バスース戦争(494-534)後のバクル・タグリブ族関係、ヒーラ宮廷との関わり。",
    development="部族自賛詩(ファフル)の規範例として古典詩学が継承。",
    historical_context="6世紀後半ヒーラ・ラフム朝期メソポタミア北西。",
    primary_source_url=WSRC_AR+"معلقة_عمرو_بن_كلثوم",
    primary_source_type="Wikisource Arabic: Mu'allaqa of Amr ibn Kulthum",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハーリス・イブン・ヒッリザ『ムアッラカ』",
    name_en="Mu'allaqa of al-Harith ibn Hilliza",
    name_original="معلقة الحارث بن حلزة",
    period_key="ジャーヒリーヤ期",
    definition="バクル族のハーリス・イブン・ヒッリザ（c.500-580）が著したムアッラカ。ヒーラ王アムル・イブン・ヒンドの前でバクル族とタグリブ族の係争を弁護した法廷詩で、外交・修辞詩の古典範例となった。",
    background="ヒーラ・ラフム朝宮廷とバクル・タグリブ族係争。",
    development="弁論・外交詩の古典範型としてアダブ作家が引用。",
    historical_context="6世紀後半メソポタミア北西部のラフム朝宮廷文化。",
    primary_source_url=WSRC_AR+"معلقة_الحارث_بن_حلزة",
    primary_source_type="Wikisource Arabic: Mu'allaqa of al-Harith",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハッサーン・イブン・サービト",
    name_en="Hassan ibn Thabit",
    name_original="حسان بن ثابت",
    period_key="初期イスラーム・ウマイヤ朝期",
    definition="マディーナのハズラジュ族詩人（563頃-674頃）。「預言者の詩人」と呼ばれ、メッカ・クライシュ族の異教詩人ヒジャーへの応酬詩でムハンマドを擁護。イスラーム宗教詩の祖型を確立した。",
    background="マディーナ部族抗争、預言者亡命(622)後の改宗。",
    development="後のマディーフ宗教詩、預言者讃美詩の祖型となった。",
    historical_context="預言者活動期マディーナの政治・宗教対立。",
    primary_source_url=SHAMELA+"book/12211",
    primary_source_type="Al-Shamela: Diwan Hassan ibn Thabit",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="カアブ・イブン・ズハイル『バーナト・スアード』",
    name_en="Ka'b ibn Zuhayr's Banat Su'ad",
    name_original="بانت سعاد",
    period_key="初期イスラーム・ウマイヤ朝期",
    definition="ズハイル詩人の息子カアブ（587-645頃）が、預言者を風刺した後に改悛し、預言者の前で朗唱した有名なカスィーダ。預言者からマント(ブルダ)を与えられた逸話で、後のスーフィー預言者讃美詩(ブルダ)伝統の起源となった。",
    background="預言者期マディーナ、ムハッザマ詩人(改宗詩人)の典型。",
    development="後代ブースィーリー『ブルダ』(13世紀)等の預言者讃美詩(マディーフ・ナバウィー)伝統の祖型。",
    historical_context="預言者活動末期、ジャーヒリー詩人のイスラーム受容過程。",
    primary_source_url=WSRC_AR+"بانت_سعاد",
    primary_source_type="Wikisource Arabic: Banat Su'ad",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ナービガ・ズビヤーニー",
    name_en="al-Nabigha al-Dhubyani",
    name_original="النابغة الذبياني",
    period_key="ジャーヒリーヤ期",
    definition="ズビヤーン族の宮廷詩人（535頃-604頃）。ヒーラ王ヌウマーン3世とガッサーン朝の宮廷を行き来し、宮廷讃美詩(マディーフ)の規範を確立。ムアッラカートに次ぐ重要詩人として古典詩学が位置づける。",
    background="ヒーラ・ラフム朝とガッサーン朝の宮廷詩の競合。",
    development="アッバース朝マディーフ詩(アブー・タンマーム、ブフトゥリー)の祖型。",
    historical_context="6世紀末アラビア北辺のビザンツ・ササン朝代理王朝文化。",
    primary_source_url=SHAMELA+"book/3809",
    primary_source_type="Al-Shamela: Diwan al-Nabigha",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# B. 初期イスラーム・ウマイヤ朝期（8件）
# ============================================================
add(**C, name_ja="ウマル・イブン・アビー・ラビーア",
    name_en="Umar ibn Abi Rabi'a",
    name_original="عمر بن أبي ربيعة",
    period_key="初期イスラーム・ウマイヤ朝期",
    definition="メッカのクライシュ族貴族詩人（644-712頃）。都市的・享楽的なガザル詩(ヒジャージ・ガザル)の創始者で、ウムム・アル＝バニーンを中心とする貴婦人巡礼地での恋愛逸話を散文劇的構成で詠う。",
    background="ウマイヤ朝期メッカの経済的繁栄、巡礼期社交文化。",
    development="後のアッバース朝都市ガザル(アブー・ヌワース、シャリーフ・ラディー)の祖型。",
    historical_context="ウマイヤ朝期ヒジャーズ貴族文化と巡礼社交。",
    primary_source_url=SHAMELA+"book/12219",
    primary_source_type="Al-Shamela: Diwan Umar ibn Abi Rabi'a",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジャミール・ブサイナ",
    name_en="Jamil-Buthayna",
    name_original="جميل بثينة",
    period_key="初期イスラーム・ウマイヤ朝期",
    definition="ウズラ族の純愛詩人ジャミール・イブン・マアマル(701没)とブサイナの恋愛詩。一人の女性への純粋・苦悩的愛を詠う「ウズラ的愛(フッブ・ウズリー)」の祖型で、後のスーフィー神秘的愛詩・西洋宮廷愛文学比較の中核例となった。",
    background="ヒジャーズ・ウズラ族の純愛部族文化、ウマイヤ朝期。",
    development="後のスーフィー神秘的愛論、中世西欧トルバドゥール愛詩との比較研究の中心。",
    historical_context="ウマイヤ朝期アラビア砂漠部族の純愛規範文化。",
    primary_source_url=SHAMELA+"book/12235",
    primary_source_type="Al-Shamela: Diwan Jamil",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マジュヌーン・ライラー伝説",
    name_en="Majnun-Layla legend",
    name_original="مجنون ليلى",
    period_key="初期イスラーム・ウマイヤ朝期",
    definition="アーミル族カイス・イブン・ムラッワフ(688没頃)とライラーの悲恋伝説。「ライラに狂いし者」(マジュヌーン)カイスの愛の発狂・砂漠放浪・夭逝の物語。ペルシア語ニザーミー、トルコ語フズーリーの古典叙事詩源泉。",
    background="ウマイヤ朝期ヒジャーズ・ウズラ部族文化の純愛規範。",
    development="ニザーミー『ライラとマジュヌーン』(1188)、フズーリー『レイラとメジュヌン』、世界文学普遍的愛物語へ。",
    historical_context="ウマイヤ朝期アラビア半島部族純愛文化。",
    primary_source_url=SHAMELA+"book/9737",
    primary_source_type="Al-Shamela: Akhbar Majnun Layla",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="クサイイル・アッザ",
    name_en="Kuthayyir 'Azza",
    name_original="كثير عزة",
    period_key="初期イスラーム・ウマイヤ朝期",
    definition="クザーア族の純愛詩人クサイイル・イブン・アブドゥッラフマーン(723没)とアッザの恋愛詩。ジャミール・ブサイナと並ぶウマイヤ朝期ウズラ的愛詩の代表で、ウマイヤ朝カリフ宮廷詩としても活躍。",
    background="ウマイヤ朝期ヒジャーズ部族純愛詩文化、ダマスカス宮廷出仕。",
    development="ウズラ的愛詩三対(ジャミール・ブサイナ、マジュヌーン・ライラー、クサイイル・アッザ)の規範化。",
    historical_context="ウマイヤ朝中期アラビア半島・ダマスカス宮廷文化。",
    primary_source_url=SHAMELA+"book/12247",
    primary_source_type="Al-Shamela: Diwan Kuthayyir",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ナカーイド（ジャリール・ファラズダク・アフタル）",
    name_en="Naqaid (Jarir-Farazdaq-Akhtal)",
    name_original="النقائض",
    period_key="初期イスラーム・ウマイヤ朝期",
    definition="ウマイヤ朝期バスラ・クーファ・ダマスカスを中心に展開した三大詩人ジャリール(733没)、ファラズダク(728没)、アフタル(710没)による応酬諷刺詩(ヒジャー)の体系。アラブ詩学のヒジャー詩規範を確立した。",
    background="ウマイヤ朝期イラク・シリアの政治・部族抗争、宮廷諷刺合戦。",
    development="アッバース朝期諷刺詩(イブン・アル＝ルーミー、ディウビル)、近代諷刺詩の規範。",
    historical_context="ウマイヤ朝期メソポタミア・シリア宮廷詩文化。",
    primary_source_url=SHAMELA+"book/9905",
    primary_source_type="Al-Shamela: Naqaid Jarir wa-l-Farazdaq",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジャリール",
    name_en="Jarir ibn Atiyya",
    name_original="جرير بن عطية",
    period_key="初期イスラーム・ウマイヤ朝期",
    definition="ヤルブー族の宮廷詩人ジャリール(640頃-733)。ウマイヤ朝カリフ・アブドゥルマリク・ヒシャームへのマディーフと、ファラズダク・アフタルとの応酬諷刺詩で名声を博した。ナカーイド三人組の中核。",
    background="ウマイヤ朝中期バスラ・ダマスカス宮廷文化。",
    development="アッバース朝諷刺・讃美詩への規範的影響。",
    historical_context="ウマイヤ朝中後期イラク・シリア宮廷詩。",
    primary_source_url=SHAMELA+"book/12273",
    primary_source_type="Al-Shamela: Diwan Jarir",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ファラズダク",
    name_en="al-Farazdaq",
    name_original="الفرزدق",
    period_key="初期イスラーム・ウマイヤ朝期",
    definition="タミーム族の宮廷詩人ハンマーム・イブン・ガーリブ・アル＝ファラズダク(641-728)。ジャリールとの諷刺合戦と、アリー裔ザイヌルアービディーンへの著名なマディーフ詩で知られる。",
    background="ウマイヤ朝期バスラ・ダマスカス宮廷とアリー裔シーア派同情詩。",
    development="シーア派マディーフ詩、アッバース朝シャリーフ・ラディー等への影響。",
    historical_context="ウマイヤ朝中期スンナ・シーア対立期宮廷文化。",
    primary_source_url=SHAMELA+"book/12245",
    primary_source_type="Al-Shamela: Diwan al-Farazdaq",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ズー・アル＝ルンマ",
    name_en="Dhu al-Rumma",
    name_original="ذو الرمة",
    period_key="初期イスラーム・ウマイヤ朝期",
    definition="アディー族の砂漠描写詩人ガイラーン・イブン・ウクバ(696-735)。「最後のベドウィン詩人」と称され、砂漠・駱駝・廃墟描写の精緻なジャーヒリー古典様式を継承し、都市化する詩文化に対して伝統を保持した。",
    background="ウマイヤ朝末期アラビア半島中部の部族詩文化終焉期。",
    development="アラブ詩学注釈伝統(イブン・クタイバ等)が砂漠描写の規範例として引用。",
    historical_context="ウマイヤ朝末期、都市化進行下の伝統部族詩。",
    primary_source_url=SHAMELA+"book/12259",
    primary_source_type="Al-Shamela: Diwan Dhu al-Rumma",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# C. アッバース朝詩詳細（10件）
# ============================================================
add(**C, name_ja="アブー・ヌワース『酒詩』",
    name_en="Abu Nuwas khamriyyat",
    name_original="خمريات أبي نواس",
    period_key="アッバース朝古典期",
    definition="アブー・ヌワース・アル＝ハサン・イブン・ハーニー(756頃-814)の酒讃歌(ハムリーヤート)群。ジャーヒリーヤ廃墟詩を否定し、バグダード酒場・少年愛・享楽を主題とする近代的・都市的詩学を確立。アッバース朝バディーウ詩学の祖型。",
    background="アッバース朝初期バグダード都市文化、ハールーン・ラシード宮廷。",
    development="アッバース朝バディーウ詩学、後のアンダルス詩(イブン・クズマーン)・ペルシア酒詩(ハーフィズ)に影響。",
    historical_context="アッバース朝初期バグダード都市享楽文化。",
    primary_source_url=SHAMELA+"book/9831",
    primary_source_type="Al-Shamela: Diwan Abi Nuwas",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アブー・ヌワース『ムジューン』",
    name_en="Abu Nuwas mujun",
    name_original="مجون أبي نواس",
    period_key="アッバース朝古典期",
    definition="アブー・ヌワースの好色・卑猥詩(ムジューン)群。性愛・少年愛・社会風刺を露骨に詠い、後の中世イスラーム文学における高雅(ファシーフ)と卑俗(ムジューン)の対極を確立。",
    background="アッバース朝期バグダード都市享楽文化、宮廷諷刺詩。",
    development="後の中世アラブ・ペルシア卑俗詩、近代詩研究における主体・身体論の中核資料。",
    historical_context="アッバース朝初期バグダードの享楽的都市文化。",
    primary_source_url=SHAMELA+"book/9831",
    primary_source_type="Al-Shamela: Diwan Abi Nuwas (mujun section)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バッシャール・イブン・ブルド",
    name_en="Bashshar ibn Burd",
    name_original="بشار بن برد",
    period_key="アッバース朝古典期",
    definition="ペルシア系盲目詩人バッシャール・イブン・ブルド(714頃-784)。アッバース朝初期バスラを拠点に活動し、バディーウ詩学の先駆者。シューウービーヤ運動の象徴的詩人として、後にカリフ・マフディーに処刑された。",
    background="アッバース朝初期バスラ、シューウービーヤ運動。",
    development="バディーウ詩学(イブン・アル＝ムウタッズ理論化)の先駆、近代アラブ詩学が再評価。",
    historical_context="アッバース朝初期アラブ・ペルシア文化抗争期。",
    primary_source_url=SHAMELA+"book/12199",
    primary_source_type="Al-Shamela: Diwan Bashshar",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アブー・アル＝アターヒヤ",
    name_en="Abu al-Atahiya",
    name_original="أبو العتاهية",
    period_key="アッバース朝古典期",
    definition="クーファ出身のズフド(禁欲)詩人アブー・イスハーク・イスマーイール(748-825)。世俗的恋愛詩から転じて死・禁欲・無常を主題とするズフディーヤート詩を体系化し、後のスーフィー禁欲詩の祖型を確立。",
    background="アッバース朝初期社会変動、宗教的禁欲思想の隆盛。",
    development="スーフィー禁欲詩(ラービア・アダウィーヤ、後代スーフィー詩人)の祖型。",
    historical_context="アッバース朝初期バグダードの宗教的内面化期。",
    primary_source_url=SHAMELA+"book/12233",
    primary_source_type="Al-Shamela: Diwan Abi al-Atahiya",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アル＝ブフトゥリー",
    name_en="al-Buhturi",
    name_original="البحتري",
    period_key="アッバース朝古典期",
    definition="タイイ族のアッバース朝宮廷詩人アル＝ワリード・イブン・ウバイド(821-897)。ムタワッキル・カリフ宮廷を中心に活動し、サーマッラー宮殿讃美詩・「イーワーン・キスラー(クテシフォン宮跡)」哀歌等のマディーフ・ワスフ詩で名声を確立。",
    background="アッバース朝中期サーマッラー宮廷文化。",
    development="アラブ宮殿讃美詩・廃墟哀歌の古典範例。",
    historical_context="アッバース朝中期サーマッラー時代宮廷詩。",
    primary_source_url=SHAMELA+"book/9905",
    primary_source_type="Al-Shamela: Diwan al-Buhturi",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イブン・アル＝ムウタッズ『キターブ・アル＝バディーウ』",
    name_en="Ibn al-Mu'tazz Kitab al-Badi'",
    name_original="كتاب البديع",
    period_key="アッバース朝古典期",
    definition="アッバース朝詩人・カリフ候補イブン・アル＝ムウタッズ(861-908)が887年頃に著したバディーウ詩学体系書。隠喩・対句・同音異義等の修辞美技法18種を整理し、アラブ詩学修辞学の祖を確立。",
    background="アッバース朝後期バグダード詩学論争、近代詩(ムフダス)の理論化要請。",
    development="アル＝ジュルジャーニー、サッカーキー等の後代アラブ修辞学体系の祖。",
    historical_context="アッバース朝後期バグダード文芸批評文化。",
    primary_source_url=SHAMELA+"book/14173",
    primary_source_type="Al-Shamela: Kitab al-Badi'",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アル＝ムタナッビー『マディーフ詩』",
    name_en="al-Mutanabbi panegyrics",
    name_original="مدائح المتنبي",
    period_key="アッバース朝古典期",
    definition="アル＝ムタナッビー・アフマド・イブン・アル＝フサイン(915-965)のマディーフ詩群。サイフ・アル＝ダウラ宮廷を中心とする讃美詩でアラブ古典詩の頂点と評価され、後代「アラブ詩はムタナッビーで終わる」と称される。",
    background="アッバース朝衰退期ハムダーン朝アレッポ宮廷文化。",
    development="アラブ・ペルシア・トルコ古典詩のマディーフ規範例として継承。",
    historical_context="10世紀シリア・北イラクのハムダーン朝宮廷詩文化。",
    primary_source_url=SHAMELA+"book/9821",
    primary_source_type="Al-Shamela: Diwan al-Mutanabbi",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アル＝マアッリー『ルズーミーヤート』",
    name_en="al-Ma'arri's Luzumiyyat",
    name_original="اللزوميات",
    period_key="アッバース朝古典期",
    definition="盲目哲学詩人アブー・アル＝アラー・アル＝マアッリー(973-1057)が著した押韻技巧詩集。「不必要な必須(ルズーム・マー・ラー・ヤルザム)」と称する二重韻律自己拘束のもとで、宗教批判・人生悲観・倫理省察を詠う2万句超の大作。",
    background="ファーティマ・ブワイフ朝期シリアの哲学的懐疑文化。",
    development="後代アラブ哲学詩、近代アラブ知識人の宗教批判詩学源泉。",
    historical_context="11世紀シリア・マアッラ・アル＝ヌウマーンの哲学的隠遁文化。",
    primary_source_url=SHAMELA+"book/9847",
    primary_source_type="Al-Shamela: al-Luzumiyyat",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アル＝マアッリー『リサーラト・アル＝グフラーン』",
    name_en="al-Ma'arri's Risalat al-Ghufran",
    name_original="رسالة الغفران",
    period_key="アッバース朝古典期",
    definition="アル＝マアッリーが1033年頃に著した想像旅行書簡。バグダードの文人イブン・アル＝カーリフへの返書形式で、彼が天国・地獄を訪問してジャーヒリー詩人・古代詩人と対話する幻想叙述。ダンテ『神曲』先行論で著名。",
    background="ファーティマ朝期シリアの哲学的書簡文学、宗教的寛容論争。",
    development="ダンテ『神曲』へのアラブ的影響仮説(アシン・パラシオス)、世界幻想文学比較。",
    historical_context="11世紀シリアの哲学的・文芸的書簡文化。",
    primary_source_url=SHAMELA+"book/9849",
    primary_source_type="Al-Shamela: Risalat al-Ghufran",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="シャリーフ・アル＝ラディー",
    name_en="al-Sharif al-Radi",
    name_original="الشريف الرضي",
    period_key="アッバース朝古典期",
    definition="バグダードのアリー裔シーア派詩人ムハンマド・イブン・フサイン・アッ＝シャリーフ(970-1015)。シーア派ナフジュ・アル＝バラーガ(アリーの説教集)編纂者として著名で、自らも宮廷ガザル・哀歌詩で高い評価を受けた。",
    background="ブワイフ朝期バグダードのシーア派文化興隆、アリー裔知識人。",
    development="ナフジュ・アル＝バラーガ編纂はアラブ修辞学・シーア派思想の中核文献に。",
    historical_context="ブワイフ朝期バグダードのシーア派・スンナ派並存文化。",
    primary_source_url=SHAMELA+"book/12281",
    primary_source_type="Al-Shamela: Diwan al-Sharif al-Radi",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D. 散文古典拡張（6件）
# ============================================================
add(**C, name_ja="イブン・アル＝ムカッファ『カリーラとディムナ』",
    name_en="Ibn al-Muqaffa's Kalila wa-Dimna",
    name_original="كليلة ودمنة",
    period_key="アッバース朝古典期",
    definition="ペルシア系翻訳家イブン・アル＝ムカッファ(720頃-756)がパフラヴィー語版『パンチャタントラ』をアラビア語に翻案した動物寓話集。アラブ・ペルシア・ヘブライ・カスティーリャ・ラテン語訳を介して中世世界文学最大の伝播力を持つ寓話書となった。",
    background="アッバース朝初期翻訳運動、サーサーン朝知識遺産のアラビア語化。",
    development="ヘブライ訳『鏡(ミシュレー)』、ラテン訳『人の生命の指針』を介して中世ヨーロッパ寓話文学(ラ・フォンテーヌ)に決定的影響。",
    historical_context="アッバース朝初期翻訳期、インド・サーサーン・ギリシア知の統合。",
    primary_source_url=SHAMELA+"book/9657",
    primary_source_type="Al-Shamela: Kalila wa-Dimna",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジャーヒズ『吝嗇者の書』",
    name_en="al-Jahiz Kitab al-Bukhala",
    name_original="كتاب البخلاء",
    period_key="アッバース朝古典期",
    definition="アル＝ジャーヒズ(776頃-868頃)が著した社会観察散文集。バスラ・バグダードの吝嗇家逸話を集成し、社会階層・心理・経済行動の詳細描写を行う。中世社会民族誌・心理散文の頂点。",
    background="アッバース朝中期バスラ・バグダードの都市商業文化。",
    development="後代アダブ作家、近代アラブ社会写実散文の祖型。",
    historical_context="アッバース朝中期メソポタミア都市経済文化。",
    primary_source_url=SHAMELA+"book/12399",
    primary_source_type="Al-Shamela: Kitab al-Bukhala",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="イブン・クタイバ『ウユーン・アル＝アフバール』",
    name_en="Ibn Qutayba Uyun al-akhbar",
    name_original="عيون الأخبار",
    period_key="アッバース朝古典期",
    definition="アブドゥッラー・イブン・クタイバ(828-889)が著したアダブ百科。10巻構成で支配・戦争・知識・禁欲・友情・婦人・食物等のテーマごとに格言・詩・逸話を分類集成。後代アダブ散文の規範書。",
    background="アッバース朝中期バグダード・アダブ散文の体系化期。",
    development="後代タナーリビー、ラーグィブ・アル＝イスファハーニー等のアダブ集成書の祖型。",
    historical_context="アッバース朝中期スンナ派文化集成期。",
    primary_source_url=SHAMELA+"book/9794",
    primary_source_type="Al-Shamela: Uyun al-akhbar",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="イブン・クタイバ『アダブ・アル＝カーティブ』",
    name_en="Ibn Qutayba Adab al-katib",
    name_original="أدب الكاتب",
    period_key="アッバース朝古典期",
    definition="イブン・クタイバが著した書記(カーティブ)向け教養書。文法・語彙・修辞・表記・誤用例を体系的に提示し、アッバース朝官僚機構の文学的言語規範を確立した。",
    background="アッバース朝官僚機構拡大期の書記教育要請。",
    development="後代官僚教養書(クダーマ・イブン・ジャアファル)、近代アラビア語規範文法の祖。",
    historical_context="アッバース朝中期官僚行政文化の制度化。",
    primary_source_url=SHAMELA+"book/9656",
    primary_source_type="Al-Shamela: Adab al-katib",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="サアーリビー『ヤティーマト・アッ＝ダフル』",
    name_en="Tha'alibi Yatimat al-dahr",
    name_original="يتيمة الدهر",
    period_key="アッバース朝古典期",
    definition="アブー・マンスール・アッ＝サアーリビー(961-1038)がニーシャープールで著した4世紀アラブ詩人選集。シリア・イラク・ジバール・ホラサーンの地域別に同時代詩人を分類紹介し、中世アラブ詩史の最重要1次史料となった。",
    background="サーマーン・ガズナ朝期ホラサーンのアラブ・ペルシア両言語文化交流。",
    development="後代アラブ・ペルシア詩史記述(イブン・ハッリカーン、サフディー)の規範。",
    historical_context="10-11世紀ホラサーン文化センター。",
    primary_source_url=SHAMELA+"book/9788",
    primary_source_type="Al-Shamela: Yatimat al-dahr",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バイハキー『アル＝マハースィン・ワル＝マサーウィー』",
    name_en="al-Bayhaqi al-Mahasin wa-l-masawi",
    name_original="المحاسن والمساوئ",
    period_key="アッバース朝古典期",
    definition="イブラーヒーム・アル＝バイハキー(10世紀)が著した二項対立アダブ書。「徳と悪徳」「沈黙と弁舌」等の対極概念を、各テーマで詩・逸話・格言を交互に並置する構成で論じる。後の対立論(マハースィン/マサーウィー)文学の祖型。",
    background="アッバース朝中期アダブ散文の論述構造実験期。",
    development="後代対立論散文(タウヒーディー『アル＝ハワーミル』)、現代比較文学の中世先駆例。",
    historical_context="アッバース朝中期論述散文の体系化期。",
    primary_source_url=SHAMELA+"book/12431",
    primary_source_type="Al-Shamela: al-Mahasin wa-l-masawi",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# E. マカーマ全完（4件）
# ============================================================
add(**C, name_ja="ハマザーニー『マカーマート』",
    name_en="Hamadhani Maqamat (51篇)",
    name_original="مقامات الهمذاني",
    period_key="アッバース朝古典期",
    definition="バディーウッザマーン・アル＝ハマザーニー(969-1008)が著したマカーマ51篇集。語り手イーサー・イブン・ヒシャームが流浪詩人アブー・アル＝ファトフ・アル＝イスカンダリーに各地で出会う寸劇形式で、押韻散文(サジュウ)による即興詩朗唱を組み込む。マカーマ形式の創始作。",
    background="ブワイフ朝期ニーシャープール・バグダード文芸サロン文化。",
    development="ハリーリー『マカーマート』(50篇)、サラクスティー、ヤマニーへの直接的祖型。",
    historical_context="10-11世紀ブワイフ朝期ホラサーン・イラクの口承娯楽文化。",
    primary_source_url=SHAMELA+"book/9657",
    primary_source_type="Al-Shamela: Maqamat al-Hamadhani",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ハリーリー『マカーマート』",
    name_en="Hariri Maqamat (50篇)",
    name_original="مقامات الحريري",
    period_key="アッバース朝古典期",
    definition="アル＝カースィム・アル＝ハリーリー(1054-1122)がバスラで著したマカーマ50篇集。語り手ハーリス・イブン・ハッマームが詐欺師アブー・ザイド・アッ＝サルージーに出会う構造で、ハマザーニーを継承しつつ修辞的精緻さを極限化。中世アラブ散文の頂点と評価される。",
    background="セルジューク朝期バスラの修辞学教育文化、アラブ古典学者の活躍期。",
    development="ヘブライ語翻案アル＝ハリーズィー『タフケモニ』、後代アラブ・ペルシア・トルコのマカーマへの規範。",
    historical_context="セルジューク朝期メソポタミア南部の修辞学教育文化。",
    primary_source_url=SHAMELA+"book/9655",
    primary_source_type="Al-Shamela: Maqamat al-Hariri",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="サラクスティー『マカーマート・ルズーミーヤ』",
    name_en="al-Saraqusti Maqamat al-luzumiyya",
    name_original="المقامات اللزومية",
    period_key="アンダルス期",
    definition="アンダルスのアブー・アル＝タヒル・アッ＝サラクスティー(1143没)が著したマカーマ集。ハリーリーを範としつつ、ルズーム(二重韻律)拘束を加えてアンダルス的修辞美を体系化。アンダルス・マカーマ文学の頂点。",
    background="アンダルス・ターイファ期サラゴサ周辺の修辞学文化。",
    development="後代アンダルス・マグレブのマカーマ伝統、ヘブライ語マカーマに影響。",
    historical_context="12世紀アンダルスのアラブ・ヘブライ修辞学共生文化。",
    primary_source_url=SHAMELA+"book/14441",
    primary_source_type="Al-Shamela: Maqamat al-Saraqusti",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヤマニー『マカーマート』",
    name_en="al-Yamani Maqamat",
    name_original="مقامات اليمني",
    period_key="マムルーク・オスマン期",
    definition="イエメンのアブドゥッラー・アル＝ヤマニー(13世紀)等が継承したマカーマ集。アラブ古典マカーマ伝統をマムルーク期にも継承し、地方文化（南アラブ・イエメン）の修辞文化を保持した。",
    background="ラスール朝期イエメンのアラブ古典学習文化。",
    development="周辺地域マカーマ伝統(マグレブ、北西アフリカ)に継承された地域変奏。",
    historical_context="13-14世紀イエメンのラスール朝学術文化。",
    primary_source_url=WIKI_AR+"المقامات_اليمنية",
    primary_source_type="Wikipedia Arabic: Maqamat al-Yamani",
    importance_score=2, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# F. アンダルス補完（6件）
# ============================================================
add(**C, name_ja="イブン・クズマーン『ザジャル』",
    name_en="Ibn Quzman zajal",
    name_original="زجل ابن قزمان",
    period_key="アンダルス期",
    definition="コルドバのザジャル詩人イブン・クズマーン(1078-1160頃)。ロマンス語混交のアンダルス口語(ハッサーニーヤ前駆)で著した149篇のザジャル集。アンダルス民衆詩の頂点として、後のロマンス語抒情詩・現代マグレブ口語詩への影響が指摘される。",
    background="ムラービト朝末期コルドバの口語文化、アンダルス・ロマンス語接触環境。",
    development="現代マグレブ口語詩、初期ロマンス諸語抒情詩比較研究の中核。",
    historical_context="12世紀ムラービト朝期コルドバの多言語都市文化。",
    primary_source_url=ARCHIVE+"diwan-ibn-quzman",
    primary_source_type="Archive.org: Diwan Ibn Quzman",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="イブン・サフル・アル＝アンダルスィー",
    name_en="Ibn Sahl al-Andalusi",
    name_original="ابن سهل الأندلسي",
    period_key="アンダルス期",
    definition="セビーリャのユダヤ系改宗アラブ詩人イブラーヒーム・イブン・サフル(1212-1251)。ムワッシャハ・ガザル詩でアンダルス末期詩を代表し、アラブ・ヘブライ両伝統の融合的詩学を体現。",
    background="ムワッヒド朝期アンダルスのユダヤ・ムスリム両伝統交流。",
    development="セファルディ・ヘブライ詩、後代アラブ・スーフィー愛詩比較研究の中心。",
    historical_context="13世紀ムワッヒド朝末期アンダルス。",
    primary_source_url=SHAMELA+"book/12313",
    primary_source_type="Al-Shamela: Diwan Ibn Sahl",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イブン・ハムディース",
    name_en="Ibn Hamdis",
    name_original="ابن حمديس",
    period_key="アンダルス期",
    definition="シチリア出身のアラブ詩人アブー・ムハンマド・イブン・ハムディース(1056-1133)。ノルマン征服後のシチリアからアンダルス・北アフリカに亡命し、失われたシチリアのアラブ文化を哀歌として詠った。",
    background="ノルマン朝シチリア征服(1061-1091)後のアラブ文化終焉、アンダルス亡命文化。",
    development="後代アラブ離散文学(ナフダ亡命文学、20世紀パレスチナ離散詩)の祖型。",
    historical_context="11世紀後半地中海のアラブ・ノルマン文明衝突期。",
    primary_source_url=SHAMELA+"book/12217",
    primary_source_type="Al-Shamela: Diwan Ibn Hamdis",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イブン・ハファージャ",
    name_en="Ibn Khafaja",
    name_original="ابن خفاجة",
    period_key="アンダルス期",
    definition="バレンシアの自然描写詩人イブン・ハファージャ(1058-1138)。ジャザーラ(果樹園)・庭園・河川等のアンダルス自然描写詩で名声を確立し、「庭園詩人(シャーイル・アル＝ジャナーン)」と称される。",
    background="ターイファ末期バレンシアのアンダルス庭園文化。",
    development="アンダルス庭園詩学の祖型、ペルシア・トルコ庭園詩との比較研究。",
    historical_context="11-12世紀ターイファ期バレンシア・アンダルス庭園文化。",
    primary_source_url=SHAMELA+"book/12299",
    primary_source_type="Al-Shamela: Diwan Ibn Khafaja",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イブン・ザイドゥーン＝ワッラーダ",
    name_en="Ibn Zaydun-Wallada",
    name_original="ابن زيدون وولادة",
    period_key="アンダルス期",
    definition="コルドバ詩人イブン・ザイドゥーン(1003-1071)とウマイヤ朝姫・詩人ワッラーダ・ビント・アル＝ムスタクフィー(994-1091)の有名な恋愛・離別詩往復。アンダルス宮廷愛詩の頂点として中世アラブ詩史で著名。",
    background="ターイファ期コルドバの宮廷文化、ウマイヤ朝末裔の文化的存続。",
    development="後の中世西欧宮廷愛詩、アラブ・ペルシア恋愛詩比較研究の中核例。",
    historical_context="11世紀ターイファ期コルドバ宮廷愛詩文化。",
    primary_source_url=SHAMELA+"book/12303",
    primary_source_type="Al-Shamela: Diwan Ibn Zaydun",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イブン・アル＝ハティーブ『ディーワーン』",
    name_en="Ibn al-Khatib Diwan",
    name_original="ديوان ابن الخطيب",
    period_key="アンダルス期",
    definition="ナスル朝グラナダ宰相詩人リサーン・アッディーン・イブン・アル＝ハティーブ(1313-1374)の詩集。アンダルス末期グラナダ宮廷詩・ムワッシャハ・歴史詩の集成で、彼の歴史書『イハーター』と並ぶアンダルス末期文化の頂点。",
    background="ナスル朝末期グラナダの宰相詩人文化、アンダルス文化終焉前夜。",
    development="アンダルス文化最終形態、後の北アフリカ・マグレブ・アラブ詩への伝播。",
    historical_context="14世紀ナスル朝末期グラナダ宰相文化。",
    primary_source_url=SHAMELA+"book/12347",
    primary_source_type="Al-Shamela: Diwan Ibn al-Khatib",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# G. マムルーク・オスマン期 / 民衆叙事詩（4件）
# ============================================================
add(**C, name_ja="サフィー・アッディーン・アル＝ヒッリー",
    name_en="Safi al-Din al-Hilli",
    name_original="صفي الدين الحلي",
    period_key="マムルーク・オスマン期",
    definition="イラクのマムルーク朝期詩人(1278-1349)。『シャルフ・アル＝カーフィヤ・アル＝バディーイーヤ』でバディーウ詩学を集大成し、自作100種修辞美技法詩で実例化。マムルーク期アラブ詩学の頂点。",
    background="マムルーク朝期イラクの古典学術復興、バディーウ詩学集成期。",
    development="後代オスマン期アラブ修辞学、近代アラブ詩学の規範。",
    historical_context="14世紀マムルーク朝期メソポタミアの学術文化。",
    primary_source_url=SHAMELA+"book/14517",
    primary_source_type="Al-Shamela: Sharh al-Kafiya al-Badi'iya",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イブン・ヒッジャ・アル＝ハマウィー『ヒザーナ』",
    name_en="Ibn Hijja al-Hamawi Khizanat al-adab",
    name_original="خزانة الأدب",
    period_key="マムルーク・オスマン期",
    definition="シリア・ハマー出身の詩人タキー・アッディーン・イブン・ヒッジャ(1366-1434)が著した修辞美書。バディーウ詩学規範書として、自作・古詩を例示しつつマムルーク期修辞学を集大成。",
    background="マムルーク後期シリア地方都市の文芸サロン文化。",
    development="後代オスマン期アラブ・トルコ修辞学への規範的影響。",
    historical_context="15世紀マムルーク後期シリアの古典学術復興。",
    primary_source_url=SHAMELA+"book/14289",
    primary_source_type="Al-Shamela: Khizanat al-adab",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イブン・ヌバータ",
    name_en="Ibn Nubata al-Misri",
    name_original="ابن نباتة المصري",
    period_key="マムルーク・オスマン期",
    definition="マムルーク朝エジプトの詩人ジャマール・アッディーン・イブン・ヌバータ(1287-1366)。マディーフ・ガザル・ナスィーブ詩でマムルーク期エジプト詩を代表し、彼の詩集・書簡集はマムルーク期文化の中核資料。",
    background="マムルーク期カイロの宮廷詩文化。",
    development="後代マムルーク・オスマン期アラブ詩への規範的影響。",
    historical_context="14世紀マムルーク期エジプト宮廷文化。",
    primary_source_url=SHAMELA+"book/12369",
    primary_source_type="Al-Shamela: Diwan Ibn Nubata",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シーラト・アッ＝ズィール・サーリム",
    name_en="Sirat al-Zir Salim",
    name_original="سيرة الزير سالم",
    period_key="マムルーク・オスマン期",
    definition="プレイスラーム期バスース戦争(494-534)を主題とする民衆英雄譚。タグリブ族のクライブ・イブン・ラビーアとその弟ズィール・サーリムの復讐譚を中心に展開され、シーラ・シャアビーヤ五大叙事詩の一つ。",
    background="マムルーク・オスマン期市場語り・口承叙事詩文化、ジャーヒリーヤ伝説の口承継承。",
    development="現代アラブ口承文学・民衆文化研究の中核資料。",
    historical_context="マムルーク・オスマン期アラブ世界の市場語り文化。",
    primary_source_url=ARCHIVE+"sirat-al-zir-salim",
    primary_source_type="Archive.org: Sirat al-Zir Salim",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# H. ナフダ補完・マフジャル離散文学（5件）
# ============================================================
add(**C, name_ja="ハリール・ムトラーン",
    name_en="Khalil Mutran",
    name_original="خليل مطران",
    period_key="ナフダ期（近代復興）",
    definition="レバノン系エジプト詩人ハリール・ムトラーン(1872-1949)。アラブ古典詩学を保持しつつ、近代的個人感情・自然抒情を導入し、ナフダ期アラブ詩近代化の橋渡しを行った。「アラブ詩近代化の指導者」。",
    background="ナフダ期エジプト・レバノン文学交流、フランス象徴主義の影響。",
    development="後代マフジャル詩人(ジブラーン、ヌアイマ)、シャウキー、ハーフィズへの影響。",
    historical_context="19世紀末-20世紀前半カイロのナフダ期文芸サロン文化。",
    primary_source_url=SHAMELA+"book/12453",
    primary_source_type="Al-Shamela: Diwan Khalil Mutran",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アフマド・シャウキー『ディーワーン』",
    name_en="Ahmad Shawqi diwan",
    name_original="ديوان أحمد شوقي",
    period_key="ナフダ期（近代復興）",
    definition="エジプトの「詩人の君主(アミール・アッ＝シュアラー)」アフマド・シャウキー(1868-1932)の詩集『シャウキーヤート』。アッバース朝古典詩を範としつつ、近代エジプトの政治・社会・歴史を主題化し、ナフダ期新古典派(ナフダ・ジャディーダ)の頂点。",
    background="ナフダ期エジプト王室宮廷詩、対英反植民地運動。",
    development="20世紀アラブ詩近代化、後の自由詩革命の前提となる古典詩学の最終形態。",
    historical_context="19世紀末-20世紀前半エジプト・カイロの新古典派詩文化。",
    primary_source_url=ARCHIVE+"diwan-shawqi",
    primary_source_type="Archive.org: al-Shawqiyyat",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ハーフィズ・イブラーヒーム",
    name_en="Hafiz Ibrahim",
    name_original="حافظ إبراهيم",
    period_key="ナフダ期（近代復興）",
    definition="エジプトの「ナイル詩人」ハーフィズ・イブラーヒーム(1872-1932)。シャウキーと並ぶナフダ期新古典派の代表で、社会詩・愛国詩を中心に、エジプト民衆の苦悩を古典カスィーダ形式で詠った。",
    background="ナフダ期エジプト民族主義運動、対英抵抗。",
    development="20世紀アラブ社会詩・愛国詩の祖型、現代パレスチナ抵抗詩への影響。",
    historical_context="19世紀末-20世紀前半カイロの民族主義詩文化。",
    primary_source_url=SHAMELA+"book/12463",
    primary_source_type="Al-Shamela: Diwan Hafiz Ibrahim",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジブラーン『預言者』",
    name_en="Gibran's The Prophet",
    name_original="النبي",
    period_key="現代アラブ文学期",
    definition="ジブラーン・ハリール・ジブラーン(1883-1931)が1923年にニューヨークで英語出版した散文詩集。預言者アル＝ムスタファーが船出前に26の人生主題を語る形式で、世界100言語以上に翻訳され、20世紀世界文学最大の影響力を持つアラブ系作品の一つ。",
    background="マフジャル(離散)文学運動、20世紀初頭ニューヨーク・アラブ系移民文化。",
    development="20世紀世界スピリチュアル文学、カウンターカルチャー(1960年代米国)、現代アラブ思想への巨大影響。",
    historical_context="20世紀初頭マフジャル運動とアラブ・米国知的交流。",
    primary_source_url=ARCHIVE+"the-prophet-gibran",
    primary_source_type="Archive.org: The Prophet (Gibran)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ミーハーイール・ヌアイマ",
    name_en="Mikha'il Nu'ayma",
    name_original="ميخائيل نعيمة",
    period_key="現代アラブ文学期",
    definition="レバノン系マフジャル文学者ミーハーイール・ヌアイマ(1889-1988)。1920年ニューヨークで「ペン同盟(アル＝ラービタ・アル＝カラミーヤ)」を共同設立し、批評書『アル＝グィルバール』(1923)でアラブ近代批評の祖型を確立。",
    background="マフジャル運動、20世紀初頭ニューヨーク・アラブ知識人サロン。",
    development="現代アラブ文芸批評、自由詩理論、アラブ近代散文の方向性に決定的影響。",
    historical_context="20世紀初頭ペン同盟期マフジャル文学運動。",
    primary_source_url=ARCHIVE+"al-ghirbal-nuayma",
    primary_source_type="Archive.org: al-Ghirbal",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# I. モダニズム詩・現代小説詳細（4件）
# ============================================================
add(**C, name_ja="サイヤーブ『雨の歌』",
    name_en="Sayyab's Anshudat al-matar",
    name_original="أنشودة المطر",
    period_key="現代アラブ文学期",
    definition="バドル・シャーキル・アッ＝サイヤーブ(1926-1964)が1960年に発表した自由詩集。表題作「雨の歌」はイラク農民・洪水・神話・革命のイメージを統合し、アラブ自由詩(シウル・フッル)革命の代表作となった。",
    background="1950年代バグダード自由詩運動、サイヤーブ・ナーズィク・アル＝マラーイカ論争。",
    development="現代アラブ自由詩の規範、20世紀後半アラブ詩への決定的影響。",
    historical_context="1950-60年代イラク政治変動・自由詩革命。",
    primary_source_url=ARCHIVE+"anshudat-al-matar",
    primary_source_type="Archive.org: Anshudat al-matar",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アドゥニース『ミフヤール書』",
    name_en="Adunis Aghani Mihyar al-Dimashqi",
    name_original="أغاني مهيار الدمشقي",
    period_key="現代アラブ文学期",
    definition="アドゥニース(1930-)が1961年に発表した代表詩集『ダマスカスのミフヤールの歌』。中世詩人ミフヤール・アッ＝ダイラミーを仮面とする現代詩人の声で、伝統批判・神秘主義的探求・近代革命を統合した自由詩学の頂点。",
    background="1960年代ベイルート『シウル』誌運動、アラブ詩近代主義第二波。",
    development="20世紀後半アラブ詩学・思想の中心、現代世界詩への翻訳・受容。",
    historical_context="1960年代レバノン・シリア知識人圏の近代化論争。",
    primary_source_url=ARCHIVE+"aghani-mihyar",
    primary_source_type="Archive.org: Aghani Mihyar",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マフフーズ三部作",
    name_en="Mahfouz Cairo Trilogy",
    name_original="الثلاثية",
    period_key="現代アラブ文学期",
    definition="ナギーブ・マフフーズ(1911-2006)が1956-57年に発表した連作三部作『宮殿通り』『欲望の宮殿』『砂糖通り』。1917-1944年カイロのアブドゥルジャワード家三世代を通して、エジプト近代化・革命・社会変動を描く。1988年ノーベル文学賞対象作。",
    background="20世紀前半カイロ伝統地区の社会変動、エジプト民族主義運動の世代変容。",
    development="20世紀アラブ小説の頂点、世界小説史におけるエジプト近代の決定的記録。",
    historical_context="20世紀前半エジプトの近代化・植民地・革命期。",
    primary_source_url=ARCHIVE+"mahfouz-trilogy",
    primary_source_type="Archive.org: al-Thulathiyya",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マフフーズ『ゲベラウィの子供たち』",
    name_en="Mahfouz's Awlad Haratina",
    name_original="أولاد حارتنا",
    period_key="現代アラブ文学期",
    definition="マフフーズが1959年にアル＝アハラーム紙連載した寓話小説。アダム(ジャバラーウィー)・モーセ・イエス・ムハンマド・科学を寓話的人物として描き、宗教史を寓喩化。エジプト・アラブ世界で禁書となり、サルマン・ラシュディ事件と並ぶ宗教検閲の象徴的事件となった。",
    background="ナーセル期エジプトの世俗化推進と宗教保守の対立、近代寓話小説の冒険。",
    development="後の現代アラブ宗教批判文学、サルマン・ラシュディ『悪魔の詩』比較研究。",
    historical_context="1959年エジプトのナーセル期世俗化と宗教保守抵抗。",
    primary_source_url=ARCHIVE+"awlad-haratina",
    primary_source_type="Archive.org: Awlad Haratina",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# J. マグレブ・21世紀現代（3件）
# ============================================================
add(**C, name_ja="アスィア・ジェバール『アルジェの女たち』",
    name_en="Assia Djebar's Femmes d'Alger",
    name_original="Femmes d'Alger dans leur appartement",
    period_key="現代アラブ文学期",
    definition="アルジェリア女性作家アスィア・ジェバール(1936-2015)が1980年に発表したフランス語短編集。ドラクロワの同名絵画に呼応し、植民地・独立後アルジェリア女性の視線・身体・声を多層的に描出。マグレブ女性文学の頂点。",
    background="独立後アルジェリアの女性問題、植民地視覚表象批判。",
    development="現代マグレブ女性文学・ポストコロニアル研究の中核、2005年アカデミー・フランセーズ会員選出。",
    historical_context="1980年代独立後アルジェリアの女性運動・近代化。",
    primary_source_url=WIKI_FR+"Assia_Djebar",
    primary_source_type="Wikipedia FR: Assia Djebar",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="アラー・アル＝アスワーニー『ヤアクービヤン館』",
    name_en="Alaa al-Aswany's Yacoubian Building",
    name_original="عمارة يعقوبيان",
    period_key="現代アラブ文学期",
    definition="エジプト作家アラー・アル＝アスワーニー(1957-)が2002年に発表した小説。カイロ中心部の歴史的建物ヤアクービヤン館の住人たちを通して、ムバーラク期エジプトの腐敗・性・宗教過激化・階級格差を全方位的に描いた21世紀アラブ社会小説の代表作。",
    background="ムバーラク期エジプトの社会矛盾、2000年代アラブ批判文学の台頭。",
    development="2006年映画化、世界30言語以上翻訳、2011年アラブの春予兆作品として再評価。",
    historical_context="ムバーラク期(1981-2011)エジプトの社会変動。",
    primary_source_url=WIKI_AR+"عمارة_يعقوبيان",
    primary_source_type="Wikipedia Arabic: Imarat Yaqubiyan",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ハーリド・ハリーファ『ナイフの賛美なき』",
    name_en="Khaled Khalifa's No Knives in the Kitchens of This City",
    name_original="لا سكاكين في مطابخ هذه المدينة",
    period_key="現代アラブ文学期",
    definition="シリア作家ハーリド・ハリーファ(1964-2023)が2013年に発表した小説。1963年バアス党政権成立から2010年代まで、アレッポを舞台にシリア国家と家族の崩壊を描く。2013年メディチ賞最終候補、2014年ナギーブ・マフフーズ賞受賞。",
    background="2011年シリア内戦勃発、半世紀のシリア・バアス党体制の崩壊。",
    development="21世紀アラブ内戦文学、シリア亡命作家ネットワーク形成の中核作品。",
    historical_context="2010年代シリア内戦期のアレッポ陥落と離散。",
    primary_source_url=WIKI_AR+"خالد_خليفة",
    primary_source_type="Wikipedia Arabic: Khalid Khalifa",
    importance_score=5, source_tier="secondary", canonical_in_region="core")


# ============================================================
# Cross-domain attachments (>= 14)
# ============================================================
def _attach_cross(name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


def _attach_axes(name: str, ax_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == name:
            existing = c.get("fourth_axes", [])
            c["fourth_axes"] = existing + ax_list
            return


# fourth_transform tags (>= 18)
_attach_axes("イムルウル・カイス『ムアッラカ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"古典アラビア語カスィーダの定型構造はLLMの定型生成と理論的に並行する。",
     "related_ai_phenomenon":"AI生成における古典定型詩の機械的再現可能性"}])
_attach_axes("アブー・ヌワース『酒詩』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"伝統廃墟詩を否定する都市主体の確立は、AI時代の伝統文化的アイデンティティの再構築問題と理論的に共振する。",
     "related_ai_phenomenon":"AI環境におけるアイデンティティ脱伝統化"}])
_attach_axes("マジュヌーン・ライラー伝説", [
    {"axis":"物語","status":"rethinking",
     "rationale":"純愛物語の越境・神秘化は、AI時代の感情データ化と質的経験の対比理論化点。",
     "related_ai_phenomenon":"AI環境における感情データ化と質的経験の対比"}])
_attach_axes("ナカーイド（ジャリール・ファラズダク・アフタル）", [
    {"axis":"言語","status":"rethinking",
     "rationale":"応酬諷刺詩の対話的構造は、現代SNS応酬・AI議論生成と理論的に並行する。",
     "related_ai_phenomenon":"AI生成議論・SNS応酬の構造化"}])
_attach_axes("アル＝マアッリー『リサーラト・アル＝グフラーン』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"想像旅行・幻想叙述の構造はAI生成のシミュレーション物語と理論的に共振する。",
     "related_ai_phenomenon":"AI生成シミュレーション物語の構造"}])
_attach_axes("アル＝マアッリー『ルズーミーヤート』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"二重押韻自己拘束による哲学的懐疑詩は、形式拘束下のAI生成と理論的に並行する。",
     "related_ai_phenomenon":"AI形式制約下の詩生成・自己拘束生成"}])
_attach_axes("イブン・アル＝ムウタッズ『キターブ・アル＝バディーウ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"修辞美技法体系化は、現代AI修辞分析・生成スタイル制御技術と理論的並行物。",
     "related_ai_phenomenon":"AI修辞分析・スタイル制御技術"}])
_attach_axes("イブン・アル＝ムカッファ『カリーラとディムナ』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"翻訳・翻案を介した寓話の世界伝播は、AI翻訳の文化的越境問題と歴史的並行例。",
     "related_ai_phenomenon":"AI翻訳における文化的越境・翻案の機械的可能性"}])
_attach_axes("ジャーヒズ『吝嗇者の書』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"社会階層・心理の詳細観察は、AI時代のソーシャルデータ分析と歴史的並行例。",
     "related_ai_phenomenon":"AIソーシャル分析・心理プロファイリング"}])
_attach_axes("ハマザーニー『マカーマート』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"語り手・主人公の二重視点・即興朗唱形式はAI対話生成の構造原型。",
     "related_ai_phenomenon":"AI対話生成における語り手・登場人物の二重構造"}])
_attach_axes("ハリーリー『マカーマート』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"押韻散文(サジュウ)の極限的修辞精緻化は、AI生成における形式・スタイル極限化と理論的並行。",
     "related_ai_phenomenon":"AI生成における修辞極限化・スタイル制御"}])
_attach_axes("イブン・クズマーン『ザジャル』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"多言語混交口語詩は、AI多言語生成における混交コード生成と理論的に共振する。",
     "related_ai_phenomenon":"AI多言語生成における混交コード化"}])
_attach_axes("イブン・ザイドゥーン＝ワッラーダ", [
    {"axis":"主体","status":"rethinking",
     "rationale":"宮廷愛詩の往復書簡形式は、AI対話生成における二者愛着関係構築と並行する。",
     "related_ai_phenomenon":"AI対話における愛着関係シミュレーション"}])
_attach_axes("ジブラーン『預言者』", [
    {"axis":"真正性","status":"rethinking",
     "rationale":"預言的散文詩のグローバル流通は、AI時代の精神的真正性・グローバル経典化問題と理論的並行物。",
     "related_ai_phenomenon":"AI生成スピリチュアル・テキストの真正性問題"}])
_attach_axes("サイヤーブ『雨の歌』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"自由詩革命による定型詩の解体は、AI時代の詩的形式の自由化・脱構築化と理論的並行物。",
     "related_ai_phenomenon":"AI生成詩における形式脱構築"}])
_attach_axes("アドゥニース『ミフヤール書』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"中世詩人を仮面とする近代詩人の声は、AI時代の歴史的人格再生・仮面文学と並行する。",
     "related_ai_phenomenon":"AI歴史的人格再生・仮面シミュレーション"}])
_attach_axes("マフフーズ『ゲベラウィの子供たち』", [
    {"axis":"真正性","status":"rethinking",
     "rationale":"宗教史の寓話化と検閲は、AI時代のセンシティブ・コンテンツ生成・検閲問題の歴史的先行例。",
     "related_ai_phenomenon":"AIセンシティブ・コンテンツ生成と検閲"}])
_attach_axes("ハーリド・ハリーファ『ナイフの賛美なき』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"内戦・離散の長期家族年代記は、AI時代の歴史的トラウマ・離散物語の生成可能性と理論的並行。",
     "related_ai_phenomenon":"AI生成における歴史的トラウマ・離散物語の構築"}])
_attach_axes("アスィア・ジェバール『アルジェの女たち』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"植民地視覚表象を脱構築するマグレブ女性主体の構築は、AI時代の表象批判・主体再構築理論の文学的祖型。",
     "related_ai_phenomenon":"AI画像生成における表象政治・脱構築"}])


# Cross-domain (>= 14)
_attach_cross("イムルウル・カイス『ムアッラカ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"廃墟詩・場所性詩学",
     "description":"アトラール（廃墟詩）はワーズワース等英国ロマン派廃墟詩学・記憶詩学の先行研究比較対象。"}])
_attach_cross("マジュヌーン・ライラー伝説", [
    {"target_db":"Myth-Narratives","link_type":"shared_concept",
     "target_entity_name":"愛の越境神話・狂気のテーマ",
     "description":"純愛・発狂・砂漠彷徨のテーマは世界神話の愛・狂気・聖性の交差テーマと比較される。"}])
_attach_cross("ナカーイド（ジャリール・ファラズダク・アフタル）", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"応酬詩・部族抗争の文学的儀礼化",
     "description":"応酬諷刺詩は部族抗争の儀礼化として人類学的儀礼研究と並行する。"}])
_attach_cross("アブー・ヌワース『酒詩』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"享楽哲学・都市的近代性",
     "description":"廃墟詩否定・都市享楽詩学はエピクロス享楽哲学・近代都市享楽論と理論的並行。"}])
_attach_cross("アル＝マアッリー『リサーラト・アル＝グフラーン』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"想像旅行・天国地獄叙述",
     "description":"想像旅行・天国地獄訪問叙述はダンテ『神曲』へのアラブ的影響仮説の中心(アシン・パラシオス)。"}])
_attach_cross("イブン・アル＝ムカッファ『カリーラとディムナ』", [
    {"target_db":"Myth-Narratives","link_type":"shared_concept",
     "target_entity_name":"動物寓話の世界伝播",
     "description":"パンチャタントラ→アラビア→ヘブライ→ラテン→欧州諸言語の伝播路は中世翻訳史の中核例。"}])
_attach_cross("ジャーヒズ『吝嗇者の書』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"中世都市民族誌",
     "description":"バスラ・バグダード吝嗇家逸話集は中世イスラーム都市民族誌の祖型。"}])
_attach_cross("ハマザーニー『マカーマート』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"ピカレスク小説の祖型",
     "description":"流浪詐欺師主人公の即興語り構造は、後の西欧ピカレスク小説の祖型として比較研究される。"}])
_attach_cross("ハリーリー『マカーマート』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"修辞極限主義詩学",
     "description":"押韻散文の極限的精緻化は、ヘブライ・アル＝ハリーズィー『タフケモニ』を介して中世セファルディ詩学に伝播。"}])
_attach_cross("イブン・クズマーン『ザジャル』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"トルバドゥール抒情詩比較",
     "description":"アンダルス口語ザジャルとオック語トルバドゥール詩の構造比較はロマン語学・比較文学の中核問題。"}])
_attach_cross("イブン・ザイドゥーン＝ワッラーダ", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"宮廷愛詩・往復書簡形式",
     "description":"アンダルス宮廷愛詩は中世西欧宮廷愛文学(ペトラルカ等)比較研究の中核例。"}])
_attach_cross("ジブラーン『預言者』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"スピリチュアル散文詩の世界流通",
     "description":"預言者散文詩の世界流通(100言語超翻訳)はスピリチュアル思想のグローバル化研究の中核例。"}])
_attach_cross("マフフーズ三部作", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"都市世代誌・社会変動",
     "description":"カイロ三世代家族誌は中東近代化の文学的民族誌として人類学比較研究の中核。"}])
_attach_cross("アスィア・ジェバール『アルジェの女たち』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"ポストコロニアル女性民族誌",
     "description":"ドラクロワ絵画に応答するマグレブ女性視線・声の発掘は、ポストコロニアル人類学・視覚研究の文学的並行物。"}])
_attach_cross("ハーリド・ハリーファ『ナイフの賛美なき』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"内戦民族誌・離散文学",
     "description":"シリア内戦下家族崩壊の長期叙述は、現代中東紛争人類学の文学的並行物。"}])
_attach_cross("アラー・アル＝アスワーニー『ヤアクービヤン館』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"建築民族誌・社会階層",
     "description":"カイロ中心建物住人の社会階層民族誌は、都市建築人類学の文学的並行物。"}])


def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="南西アジア",
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
        print(f"[c21-w17] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c21-w17] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c21-w17] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
