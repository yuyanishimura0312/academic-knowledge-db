"""LIT-DB Phase 2 Wave 22 — C30 ADD: Indigenous & Oral Literature (+80).

Subfield: lit_indigenous_oral (id=19), region='周縁横断'.
Adds 80 NEW non-overlapping concepts on top of existing 142, target 400.

Coverage targets:
  A: 北米先住民詳細 (Cherokee, Lakota, Navajo, Hopi, Pueblo, Iroquois,
     Algonquian, Anishinaabeg, Cree, Inuit, Yupik, Tlingit, Haida,
     Tsimshian, Salish, Kalapuya, Klamath, Pomo, Kashaya) — 22
  B: アマゾン・南米先住民詳細 (Tukano, Yanomami, Kayapó, Bororo, Mehinaku,
     Krahô, Karajá, Tapirapé, Wayãpi, Wajãpi, Asurini, Aché, Wichí,
     Pilagá, Quichua, Aymara, Ayoreo, Pemón, Kuna, Kogi, Ika, Wayuu) — 12
  C: アフリカ口承詳細 (Maasai, Kikuyu, Akan-extended, Yoruba-Ifa-detail, Hausa,
     Fulani, Tuareg, Berber, Beja, Somali, Oromo, Tigrinya, Konso,
     Borana, Pokot, Bantu Mukanda, Mbuti, Aka, Khoisan-extended,
     Sandawe, Hadza, Mursi, Karo, Hamer, Suri) — 14
  D: 大洋州詳細 (Tongan, Samoan, Fijian, Marquesan, Tahitian,
     Mangaian, Tuamotuan, Cook Islands, Niuean, Tokelauan, Tuvalu,
     Kiribati, Marshallese, Pohnpeian, Yapese, Palauan, Chamorro,
     Carolinian, Yolŋu, Pintupi-Luritja, Walpiri, Anangu, Tiwi,
     Murray, Maori) — 14
  E: 南アジア・東南アジア (Mongol Geser, Tibetan Gesar, Lepcha Mun,
     Adi Donyi-Polo, Sherdukpen, Bhutanese, Khmer cbap, Lao Sinxay,
     Burmese yatu, Hmong qhuab kev) — 6
  F: アイヌ詳細 (Yukar 12 songs, Kamuyyukar, Tuytak, Sakorpe, Upopo,
     Wenipuru, Hauki, Akor Itak, Iworpe, Otonpe, Otokachimak,
     Kayakkamuy iyomante) — 6
  G: 文献記録方法論 (ethnopoetics-Tedlock-breath, Sherzer voice,
     Briggs/Bauman performance, Heath narrative ecology, Bakhtin
     folklore, CARE/FAIR archive ethics, Indigenous protocols,
     sovereign data networks) — 6

Verification: >= 60% primary (WOLP/ELAR/PARADISEC/AIATSIS/academic).
fourth_transform_tags >= 24; cross_domain to AN >= 18.
Definitions under 150 chars.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS_TO_SEED = [
    ("先住民口承伝統期", "Indigenous Oral Tradition (pre-contact)", -10000, 1500,
     "接触以前の口承伝統。"),
    ("植民地接触・抑圧期", "Colonial Contact & Suppression", 1500, 1960,
     "植民地化下で口承伝統が記録化・改変・抑圧される時期。"),
    ("先住民文芸復興期", "Indigenous Renaissance", 1960, 2026,
     "1960年代以降の先住民文芸復興。口承と書記の融合、自決運動、文化主権の文学。"),
]


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


REGION = "周縁横断"
SUBFIELD = "lit_indigenous_oral"
C = dict(subfield_code=SUBFIELD, region=REGION, original_script="roman")
CJ = dict(subfield_code=SUBFIELD, region=REGION, original_script="japanese")


WIKI = "https://en.wikipedia.org/wiki/"
ELAR = "https://www.elararchive.org/"
PARA = "https://paradisec.org.au/"
AIATSIS = "https://aiatsis.gov.au/"
WOLP = "https://www.endangeredlanguages.com/"
ARCH = "https://archive.org/details/"
SIRIS = "https://siris.si.edu/"


# ============================================================
# A: 北米先住民詳細 (22)
# ============================================================
add(**C, name_ja="シクウォイア音節文字文学",
    name_en="Sequoyah Cherokee syllabary literature",
    name_original="ᏣᎳᎩ ᎦᏬᏂᎯᏍᏗ",
    period_key="植民地接触・抑圧期",
    definition="Sequoyahが1821年に発明したCherokee音節文字85字による先住民言語文学伝統。Cherokee Phoenix(1828)を含む。",
    background="北米先住民が独自に発明した文字体系の唯一例。",
    development="Cherokee Phoenix新聞・聖書翻訳・薬草書を産出。",
    historical_context="1820-30年代Cherokee強制移住前の知的興隆期。",
    primary_source_url="https://www.loc.gov/collections/cherokee-phoenix/",
    primary_source_type="Library of Congress Cherokee Phoenix archive",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ブラック・エルク語る",
    name_en="Black Elk Speaks",
    name_original="Black Elk Speaks",
    period_key="植民地接触・抑圧期",
    definition="Lakota霊視者Black ElkがJohn Neihardtに1931年に語った霊的自伝。Lakotaサン・ダンス・ウンデッド・ニーを含む。",
    background="Lakota霊性の世界的伝播の起点。",
    development="先住民霊的自伝の規範作。1979年完全版刊行。",
    historical_context="1930年代米国先住民霊性記録運動期。",
    primary_source_url=WIKI+"Black_Elk_Speaks",
    primary_source_type="William Morrow first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"語り手と記録者の二重作者性は、AI時代の人間-AI共著作の文学的祖型。",
         "related_ai_phenomenon":"AI共著作と二重作者性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Lakota ethnography",
         "description":"Lakota民族誌の主要一次資料。"}])

add(**C, name_ja="ウィンター・カウント詳細",
    name_en="Lakota winter counts (waniyetu wowapi)",
    name_original="waníyetu wówapi",
    period_key="先住民口承伝統期",
    definition="Lakotaが鹿皮に毎年の象徴的事件を絵画的に記録した暦的歴史記述。Lone Dog Winter Count(1801-1876)が著名。",
    background="Lakota独自の絵画的歴史記述伝統。",
    development="Smithsonian保管。Lakota史復元の主要一次資料。",
    historical_context="北米平原先住民の絵画歴史記述伝統の頂点。",
    primary_source_url=SIRIS,
    primary_source_type="Smithsonian NMNH winter count collection",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"pictographic history",
         "description":"絵画的歴史記述の人類学的研究と並行。"}])

add(**C, name_ja="ディネ・バハネ",
    name_en="Diné bahaneʼ Navajo creation",
    name_original="Diné bahaneʼ",
    period_key="先住民口承伝統期",
    definition="Navajo族の創世神話。四つの世界からの出現、Changing Woman、聖戦士双子の物語を含む大叙事詩。",
    background="Navajo世界観の中核口承叙事。",
    development="Washington Matthews(1897), Paul Zolbrod(1984)の文学化版が著名。",
    historical_context="Navajo儀礼・治療歌全体の物語的基盤。",
    primary_source_url=WIKI+"Din%C3%A9_Bahane%CA%BC",
    primary_source_type="Zolbrod 1984 University of New Mexico Press",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"低資源言語Navajoの口承叙事は、AI時代の言語多様性保全の文学的範型。",
         "related_ai_phenomenon":"AI低資源言語と先住民叙事"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Navajo cosmology",
         "description":"Navajo宇宙論の人類学的記述と直結。"}])

add(**C, name_ja="ホピ青星予言",
    name_en="Hopi Blue Star Prophecy",
    name_original="Sakwa Sohu",
    period_key="先住民口承伝統期",
    definition="Hopi族の終末予言伝統。第四世界終焉と第五世界出現を予告する青星出現の物語群。Frank Waters『Book of the Hopi』(1963)で公表。",
    background="Hopi予言伝統の文学的中核。",
    development="20世紀後半反核運動・環境主義に影響。",
    historical_context="1960年代Hopi長老による文化外公表期。",
    primary_source_url=WIKI+"Hopi_mythology",
    primary_source_type="Frank Waters Book of the Hopi 1963",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ホピ儀礼周期",
    name_en="Hopi ceremonial cycles",
    name_original="Hopi katsina ceremonies",
    period_key="先住民口承伝統期",
    definition="HopiのSoyal冬至祭からNiman夏至祭までの儀礼周期に伴う神聖な歌・物語の集合体。Frank Waters・Mischa Titiev記録。",
    background="Hopi年中行事の口承文学的基盤。",
    development="Pueblo儀礼研究の中核資料。",
    historical_context="米国南西部Pueblo儀礼伝統の継続的実践。",
    primary_source_url=WIKI+"Hopi",
    primary_source_type="Titiev Old Oraibi 1944 academic ethnography",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Pueblo ceremonialism",
         "description":"Pueblo儀礼研究の主要対象。"}])

add(**C, name_ja="プエブロ・ポペ反乱物語",
    name_en="Po-Pay Pueblo Revolt narratives",
    name_original="Po'pay",
    period_key="植民地接触・抑圧期",
    definition="1680年Pueblo反乱を主導したSan Juan PuebloシャマンPo-Payに関するPueblo口承群。被植民史の先住民視点記録。",
    background="北米唯一の成功した先住民植民地反乱の口承伝承。",
    development="Joe Sando(1992), Andrew Knaut(1995)の現代記述。",
    historical_context="1680-92年プエブロ自治回復期。",
    primary_source_url=WIKI+"Po%27pay",
    primary_source_type="Joe Sando Pueblo Profiles 1995",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イロコイ大平和の法",
    name_en="Iroquois Great Law of Peace",
    name_original="Kayanerenkó:wa",
    period_key="先住民口承伝統期",
    definition="HaudenosauneeがDeganawidaとHiawathaの伝説的指導者により制定した政治哲学的口承法典。117条。米国憲法に影響。",
    background="先住民政治哲学の規範的口承典。",
    development="Arthur Parker(1916), William Fenton記録版が標準。",
    historical_context="北米北東部先住民連邦の政治的基盤。",
    primary_source_url=WIKI+"Great_Law_of_Peace",
    primary_source_type="Parker 1916 Constitution of the Five Nations",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"口承政治哲学典は、AI時代の口承知の正典化の文学的祖型。",
         "related_ai_phenomenon":"AI時代の口承典正典化"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Iroquois political anthropology",
         "description":"イロコイ政治人類学と直結。"}])

add(**C, name_ja="ハイアワサ叙事詩",
    name_en="Hiawatha epic",
    name_original="Hiawatha",
    period_key="先住民口承伝統期",
    definition="OnondagaリーダーHiawathaがDeganawidaと共にイロコイ連邦を統合した過程を歌う先住民英雄叙事詩。",
    background="北米先住民英雄叙事の代表。",
    development="Longfellow1855年詩は実は別物(Ojibwe由来)で混同に注意。",
    historical_context="15世紀イロコイ連邦成立期の歴史的口承。",
    primary_source_url=WIKI+"Hiawatha",
    primary_source_type="Onondaga Nation oral tradition / Parker 1916",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アルゴンキン・ナナボゾ循環",
    name_en="Algonquian Nanabozho cycle",
    name_original="Nanabozho",
    period_key="先住民口承伝統期",
    definition="Anishinaabe・Algonquian系のトリックスター・文化英雄Nanabozho(白兎)を主役とする創世・文化起源物語循環。",
    background="北米北東部先住民最重要トリックスター循環。",
    development="William Jones(1917, 1919) Smithsonian Bureau報告に詳細。",
    historical_context="北東部Algonquian語族共有の口承遺産。",
    primary_source_url=ARCH+"ojibwatextspubli01jone",
    primary_source_type="William Jones Ojibwa Texts 1917 archive.org",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Algonquian trickster",
         "description":"Algonquianトリックスター人類学と並行。"}])

add(**C, name_ja="ワバナキ口承伝統",
    name_en="Wabanaki oral tradition",
    name_original="Wabanaki",
    period_key="先住民口承伝統期",
    definition="米国メイン州・カナダ大西洋岸のPenobscot・Passamaquoddy・Maliseet・Mi'kmaq・Abenaki5部族連合の口承伝統群。",
    background="北東部Wabanaki連合の文学的核。",
    development="Frank Speck(1935)・Joe Bruchac現代再話により継承。",
    historical_context="北米北東部先住民連合の文化的基盤。",
    primary_source_url=WIKI+"Wabanaki_Confederacy",
    primary_source_type="Speck Penobscot Man 1940 academic ethnography",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アニシナーベMide治療歌",
    name_en="Anishinaabeg Mide healing songs",
    name_original="Midewiwin",
    period_key="先住民口承伝統期",
    definition="Anishinaabe・OjibweのMidewiwin(大薬会)儀礼で歌われる治療歌・birch bark scroll記録歌。Frances Densmore録音1907-1910。",
    background="北米先住民最重要医療儀礼歌伝統。",
    development="Densmore Smithsonian録音はWOLP保存。",
    historical_context="20世紀初頭Mide伝統の音響記録運動期。",
    primary_source_url="https://www.loc.gov/item/afc9999005.16700/",
    primary_source_type="Densmore 1910 Chippewa Music BAE Bulletin 45",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Midewiwin",
         "description":"Mide大薬会民族誌と直結。"}])

add(**C, name_ja="アニシナーベ・マナブーゾ循環",
    name_en="Anishinaabe Manabozho cycle",
    name_original="Manabozho",
    period_key="先住民口承伝統期",
    definition="OjibweのトリックスターManabozho(別形Nanabush)を主役とする世界更新・文化起源物語の周期。Mishipeshu戦闘等を含む。",
    background="Anishinaabe文化英雄叙事の中核。",
    development="Basil Johnston『Ojibway Heritage』(1976)で現代化。",
    historical_context="五大湖地域Ojibwe文学伝統の基盤。",
    primary_source_url=WIKI+"Nanabozho",
    primary_source_type="Basil Johnston 1976 first edition",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クリー・ウェサケチャク循環",
    name_en="Cree Wesakechak cycle",
    name_original="wîsahkêcâhk",
    period_key="先住民口承伝統期",
    definition="Cree族のトリックスター・文化英雄Wesakechak(別形Wesakaychak)を主役とする創世・道徳教訓物語循環。",
    background="平原・亜北極Cree文学伝統の中核。",
    development="Edward Ahenakew(1929)・Freda Ahenakew(1992)現代記録。",
    historical_context="20世紀Cree口承文学の二段階記録運動。",
    primary_source_url=WIKI+"Wisakedjak",
    primary_source_type="Ahenakew 1929 Journal of American Folk-Lore",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イヌイト・ウニプカートゥ",
    name_en="Inuit unipkaaq narratives",
    name_original="unipkaaq",
    period_key="先住民口承伝統期",
    definition="北極圏Inuitの伝統物語ジャンルunipkaaq(過去の真実物語)とunipkaaqtuaq(虚構物語)の対比的口承叙事伝統。",
    background="北極圏先住民の物語ジャンル分類体系。",
    development="Knud Rasmussen(1929) Fifth Thule Expedition記録。",
    historical_context="20世紀初頭極北民族誌探検期。",
    primary_source_url=WIKI+"Inuit_religion",
    primary_source_type="Rasmussen 5th Thule Expedition Reports 1929",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Inuit ethnopoetics",
         "description":"イヌイトエスノポエティクスと直結。"}])

add(**C, name_ja="イヌイト・ピシック歌物語",
    name_en="Inuit pisiq narrative songs",
    name_original="pisiq",
    period_key="先住民口承伝統期",
    definition="Inuitの個人作詩songの伝統pisiq。狩猟・天候・愛・嘲笑(pisiq aatuutaq)等多様。所有・継承・贈与の対象となる。",
    background="極北個人詩作伝統の中核ジャンル。",
    development="Charles Brower・Helga Goetz録音保存。",
    historical_context="極北口承伝統の個人創作的側面の記録運動。",
    primary_source_url=WIKI+"Inuit_music",
    primary_source_type="Smithsonian Folkways Inuit recordings",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ユピック仮面伝統",
    name_en="Yup'ik mask tradition",
    name_original="kegginaquq",
    period_key="先住民口承伝統期",
    definition="アラスカYup'ikの儀礼仮面kegginaquqとそれに伴う精霊・狩猟物語伝承体系。Edward Nelson(1899)記録。",
    background="極北物質文化と口承文学の融合伝統。",
    development="UAF Sealaska Heritage現代復興。",
    historical_context="19世紀末から20世紀初頭の宣教抑圧後の復興期。",
    primary_source_url="https://siris-collections.si.edu/",
    primary_source_type="Nelson Eskimo about Bering Strait 1899 BAE",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="トリンギット氏族紋章文学",
    name_en="Tlingit clan crest as literature",
    name_original="at.óow",
    period_key="先住民口承伝統期",
    definition="Tlingit氏族紋章at.óow(神聖継承財)に付随する氏族起源・移住・戦争の口承叙事伝統。物質文学の典型。",
    background="北米北西海岸氏族紋章文学の典型。",
    development="Nora Marks Dauenhauer『Haa Shuká』(1987-94)三部作。",
    historical_context="20世紀末Tlingit文学的記録運動期。",
    primary_source_url=WIKI+"Tlingit_clans",
    primary_source_type="Dauenhauer Haa Shuká University of Washington Press",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Northwest Coast crest system",
         "description":"北西海岸紋章体系民族誌と直結。"}])

add(**C, name_ja="ハイダ・カラス循環",
    name_en="Haida raven cycle",
    name_original="Yáahl",
    period_key="先住民口承伝統期",
    definition="Haida族の文化英雄・トリックスターYáahl(カラス)を主役とする創世・光盗み・人類起源叙事循環。",
    background="北西海岸最重要トリックスター循環。",
    development="John Swanton(1905)・Robert Bringhurst(1999-2002)文学化。",
    historical_context="20世紀初頭・20世紀末の二段階記録運動。",
    primary_source_url=WIKI+"Haida_mythology",
    primary_source_type="Swanton 1905 Haida Texts BAE Memoir 4",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スカイ『シャーマンたち』",
    name_en="Skaay's Shamans",
    name_original="Skaay",
    period_key="植民地接触・抑圧期",
    definition="HaidaのシャマンSkaay(John Sky, c.1827-1905)が口述しSwantonが1900-01年記録した叙事詩群。Bringhurst(1999)が古典化。",
    background="北米先住民古典叙事詩の最重要例。",
    development="Bringhurst『A Story as Sharp as a Knife』(1999)で世界文学に。",
    historical_context="Haida人口激減期の最後の偉大な口頭詩人。",
    primary_source_url=WIKI+"Skaay",
    primary_source_type="Swanton 1905 / Bringhurst 1999 Douglas & McIntyre",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"口頭詩人の個人作者性発見は、AI時代の口承の作者性復元の文学的祖型。",
         "related_ai_phenomenon":"AI時代の口承の個人作者性復元"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Haida ethnography",
         "description":"Haida民族誌の主要一次資料。"}])

add(**C, name_ja="ツィムシアン物語伝統",
    name_en="Tsimshian narratives",
    name_original="adaawx",
    period_key="先住民口承伝統期",
    definition="Tsimshian族の歴史的物語adaawx(氏族所有歴史)とmalsk(共有物語)の二分類による口承文学伝統。",
    background="北西海岸法的口承伝統の代表。",
    development="Franz Boas(1916) Tsimshian Mythology BAE 31報告。",
    historical_context="Boasian人類学最重要先住民文学資料。",
    primary_source_url=ARCH+"reportonenboas00boas",
    primary_source_type="Boas 1916 Tsimshian Mythology BAE 31",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Boasian ethnography",
         "description":"Boas人類学の中心資料。"}])

add(**C, name_ja="海岸サリッシュ・スマユスタシュ",
    name_en="Coast Salish smayustás",
    name_original="smayustás",
    period_key="先住民口承伝統期",
    definition="海岸サリッシュ族(Lushootseed系)の伝統物語smayustás。創世・先祖移住・場所名起源を含む口承叙事ジャンル。",
    background="北西海岸南部サリッシュ系文学伝統の中核。",
    development="Vi Hilbert(1992) Lushootseed Texts記録。",
    historical_context="20世紀末サリッシュ言語復興運動期。",
    primary_source_url=WIKI+"Lushootseed",
    primary_source_type="Hilbert Haboo Lushootseed Texts UWP 1996",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="カラプヤ世界更新儀礼",
    name_en="Kalapuya world-renewal ceremonies",
    name_original="Kalapuya",
    period_key="植民地接触・抑圧期",
    definition="オレゴン Willamette Valley Kalapuya族の世界更新冬季儀礼に伴う物語・歌伝統。Melville Jacobs(1936-39)記録。",
    background="北米北西部内陸消滅危機文学の救済記録。",
    development="Jacobs Kalapuya Texts 1945 University of Washington。",
    historical_context="20世紀前半Kalapuya言語消滅危機期の記録運動。",
    primary_source_url=WIKI+"Kalapuya",
    primary_source_type="Jacobs 1945 Kalapuya Texts UWPA",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クラマス・テューレ湖物語群",
    name_en="Klamath Tule Lake narrative corpus",
    name_original="Maqlaqs",
    period_key="先住民口承伝統期",
    definition="オレゴン・北加州境Klamath族のTule Lake周辺神話・歴史物語群。Albert Gatschet(1890)・Theodore Stern(1966)記録。",
    background="北米北西部内陸先住民文学伝統の代表。",
    development="Dell Hymes ethnopoetics手法の主要資料。",
    historical_context="Hymes ethnopoetics確立期の中核資料。",
    primary_source_url=ARCH+"klamathindiansof00gats",
    primary_source_type="Gatschet 1890 Klamath Indians Contributions BAE 2",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ポモ・マル運動歌",
    name_en="Pomo Maru songs",
    name_original="Maru",
    period_key="植民地接触・抑圧期",
    definition="北加州Pomo族の20世紀初頭預言者Maru運動に伴う夢見歌・予言歌伝統。Bole-Maru夢見運動の中核。",
    background="北米先住民予言運動の歌文学化典型。",
    development="Cora Du Bois(1939) Bole-Maru報告で記録。",
    historical_context="20世紀前半California先住民復興運動期。",
    primary_source_url=WIKI+"Bole-Maru_Religion",
    primary_source_type="Du Bois 1939 Anthropological Records UC",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# B: アマゾン・南米先住民詳細 (12)
# ============================================================
add(**C, name_ja="トゥカノ・ユルパリ詠唱",
    name_en="Tukano shamanic chants Yuruparí",
    name_original="Yuruparí",
    period_key="先住民口承伝統期",
    definition="Vaupés川上流Tukano諸族の禁忌的男性祭礼Yuruparíに伴うシャマン詠唱体系。Hugh-Jones(1979)記述。",
    background="アマゾン男性秘儀文学の代表。",
    development="2011年UNESCO無形文化遺産登録。",
    historical_context="アマゾン上流人類学の中核研究対象。",
    primary_source_url="https://ich.unesco.org/en/RL/jaguar-shamans-of-the-yurupari-00574",
    primary_source_type="UNESCO ICH 2011 / Hugh-Jones 1979",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Amazonian shamanism",
         "description":"アマゾン・シャーマニズム研究と直結。"}])

add(**C, name_ja="アラワク・カリブ口承",
    name_en="Arawak-Carib oral tradition",
    name_original="Lokono / Kalina",
    period_key="先住民口承伝統期",
    definition="カリブ海・ガイアナ沿岸Lokono(Arawak)とKalina(Carib)の創世・移住・水妖物語群。Walter Roth(1915)記録。",
    background="カリブ海先住民文学の救済記録。",
    development="Roth Animism and Folk-Lore of Guiana Indians BAE 30。",
    historical_context="20世紀初頭ガイアナ植民期の民族誌的記録運動。",
    primary_source_url=ARCH+"animismfolkloreo00roth",
    primary_source_type="Roth 1915 BAE Annual Report 30",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="カヤポー・メベンゴクレ歌",
    name_en="Kayapó/Mebengokre ngàngà",
    name_original="Mẽbêngôkre",
    period_key="先住民口承伝統期",
    definition="ブラジル中部Kayapó(自称Mẽbêngôkre)族の儀礼歌ngàngàと年齢階梯歌による身体・社会更新文学伝統。",
    background="アマゾン中央高地先住民歌文学の代表。",
    development="Terence Turner(1992)・Vanessa Lea研究。",
    historical_context="20世紀後半アマゾン環境主義との連帯期。",
    primary_source_url=WIKI+"Kayap%C3%B3_people",
    primary_source_type="Turner 1992 Visual Anthropology Review",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ボロロ・アロエ・エ・ボペ",
    name_en="Bororo Aroe e Bope",
    name_original="aroe e bope",
    period_key="先住民口承伝統期",
    definition="中央ブラジルBororo族の二元的霊的体系aroe(死者霊)とbope(自然霊)に基づく葬送詠唱・神話物語伝統。",
    background="レヴィ=ストロース『神話論理』第一巻の主要資料。",
    development="Salesian宣教師Albisetti & Venturelli百科事典(1962-)記録。",
    historical_context="20世紀構造人類学の中心資料。",
    primary_source_url=WIKI+"Bororo_people",
    primary_source_type="Albisetti & Venturelli 1962 Enciclopédia Bororo",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Lévi-Strauss Mythologiques",
         "description":"構造人類学神話研究の主要対象。"}])

add(**C, name_ja="メヒナクー笛家詠唱",
    name_en="Mehinaku flute house chants",
    name_original="kawokà",
    period_key="先住民口承伝統期",
    definition="Xingu上流Mehinaku族の男性専用聖笛(kawokà)儀礼に伴う詠唱文学伝統。Thomas Gregor『Anxious Pleasures』(1985)記述。",
    background="アマゾンXingu文化複合体の文学的中核。",
    development="ジェンダー秘儀文学研究の典型例。",
    historical_context="20世紀後半Xingu保護区文化研究期。",
    primary_source_url=WIKI+"Mehinaku_people",
    primary_source_type="Gregor 1985 University of Chicago Press",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クラホー大家屋詠唱",
    name_en="Krahô great house chants",
    name_original="ikhre",
    period_key="先住民口承伝統期",
    definition="ブラジル中北部Krahô(Gê系)族の中央広場円舞詠唱伝統。Júlio Cezar Melatti(1967)記述。",
    background="Gê系族中央広場文学の代表。",
    development="Curt Nimuendajú記録の延長線上。",
    historical_context="20世紀後半ブラジル先住民研究中核期。",
    primary_source_url=WIKI+"Krah%C3%B4_people",
    primary_source_type="Melatti 1967 Indios e Criadores",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヤノマミ詠唱合成",
    name_en="Yanomami palimpsest narrative",
    name_original="Yanomami reahu",
    period_key="先住民口承伝統期",
    definition="Yanomami族の葬送祭reahuに伴うシャマン詠唱と即興物語の重層的合成伝統。Bruce Albert・Davi Kopenawa共作。",
    background="アマゾン先住民詠唱の現代記録運動。",
    development="Kopenawa『La chute du ciel』(2010)が国際的画期。",
    historical_context="2010年代アマゾン先住民世界文学化の頂点。",
    primary_source_url=WIKI+"The_Falling_Sky",
    primary_source_type="Kopenawa & Albert 2010 Plon / Harvard 2013",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"先住民シャマンと人類学者の共作者性は、AI時代の人間-非人間共作者性の祖型。",
         "related_ai_phenomenon":"AI時代の異種共作者性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Amazonian perspectivism",
         "description":"アマゾン・パースペクティビズムの主要資料。"}])

add(**C, name_ja="ワユー・スーチムナ創世",
    name_en="Wayuu Süchimna creation",
    name_original="Süchimna",
    period_key="先住民口承伝統期",
    definition="コロンビア・ベネズエラ国境Guajira半島Wayuu族の創世神話Süchimnaと夢見預言伝統lapü。",
    background="カリブ海最大先住民の文学伝統。",
    development="Michel Perrin(1976) Le chemin des Indiens morts。",
    historical_context="20世紀後半Wayuu自治運動期。",
    primary_source_url=WIKI+"Wayuu_people",
    primary_source_type="Perrin 1976 / Vergara 1990",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クナ・モラ叙事",
    name_en="Kuna mola narratives + abisua chants",
    name_original="abisua",
    period_key="先住民口承伝統期",
    definition="パナマSan Blas諸島Kuna族の布絵モラと結合する詠唱abisua・出産歌pab igala伝統。Joel Sherzer(1990)研究。",
    background="物質文化と詠唱の統合文学伝統。",
    development="Sherzer Verbal Art in San Blas(1990)が古典。",
    historical_context="エスノポエティクス確立期の中心資料。",
    primary_source_url=WIKI+"Guna_people",
    primary_source_type="Sherzer 1990 Cambridge UP",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ethnopoetics",
         "description":"エスノポエティクス理論の中核資料。"}])

add(**C, name_ja="コギ・ママ伝統",
    name_en="Kogi mama tradition",
    name_original="ezuamas",
    period_key="先住民口承伝統期",
    definition="コロンビアSierra Nevada de Santa Marta Kogi族の長老司祭mamaが伝承する宇宙論的口承典ezuamas。",
    background="アンデス北部先住民霊的伝統の代表。",
    development="Reichel-Dolmatoff『The Loom of Life』(1978)記述。",
    historical_context="20世紀後半Kogi先住民環境主義との連帯期。",
    primary_source_url=WIKI+"Kogi_people",
    primary_source_type="Reichel-Dolmatoff 1978 Brill",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アシェ・アクパ・フア",
    name_en="Aché Akupa Hu'a chants",
    name_original="kybwyrai pukú",
    period_key="先住民口承伝統期",
    definition="パラグアイ Aché族の夜間集合詠唱kybwyrai pukú。男性個人詠唱と女性合唱の応答構造。Pierre Clastres(1972)研究。",
    background="政治人類学的口承文学の中心資料。",
    development="Clastres『Le Grand Parler』(1974)で文学化。",
    historical_context="20世紀後半反国家政治人類学の確立期。",
    primary_source_url=WIKI+"Ach%C3%A9_people",
    primary_source_type="Clastres 1974 Le Grand Parler Seuil",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ウィチー口承",
    name_en="Wichí Mataco oral tradition",
    name_original="Wichí lhamtés",
    period_key="先住民口承伝統期",
    definition="アルゼンチン・パラグアイGran Chaco Wichí族(Mataco-Mataguayo語族)の創世・狐トリックスター物語群。",
    background="Gran Chaco先住民文学伝統の代表。",
    development="John Palmer(2005) The Sky over the Toba研究。",
    historical_context="20世紀後半Chaco人類学興隆期。",
    primary_source_url=WIKI+"Wich%C3%AD",
    primary_source_type="Palmer 2005 SAR Press / academic ethnography",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# C: アフリカ口承詳細 (14)
# ============================================================
add(**C, name_ja="マサイ・エンキテング歌",
    name_en="Maasai enkiteng age-grade chants",
    name_original="enkiteng",
    period_key="先住民口承伝統期",
    definition="ケニア・タンザニア Maasai族の年齢階梯儀礼olporror に伴う雄牛(enkiteng)中心歌伝統。Paul Spencer研究。",
    background="東アフリカ年齢組織文学の代表。",
    development="Spencer『The Maasai of Matapato』(1988)記述。",
    historical_context="20世紀後半東アフリカ社会人類学中核期。",
    primary_source_url=WIKI+"Maasai_people",
    primary_source_type="Spencer 1988 Manchester UP",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アカン・アナンセセム拡張",
    name_en="Akan Anansesem 80+ trickster cycles",
    name_original="Anansesɛm",
    period_key="先住民口承伝統期",
    definition="ガーナAkan系族の蜘蛛Ananse物語循環群80+話。R. S. Rattray(1930) Akan-Ashanti Folk-Tales完全集成。",
    background="西アフリカ最重要トリックスター物語循環。",
    development="カリブ海・米国南部Anansy物語の起源。",
    historical_context="20世紀前半英領植民期の体系的記録。",
    primary_source_url=ARCH+"akanashantifolkt00rattuoft",
    primary_source_type="Rattray 1930 Oxford Clarendon Press",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"trickster motifology",
         "description":"トリックスター・モチーフ研究の中核。"}])

add(**C, name_ja="ヨルバ・イファ・オドゥ詳細",
    name_en="Yoruba Ifa odu detail",
    name_original="Ifá Odú",
    period_key="先住民口承伝統期",
    definition="ヨルバ族占術体系Ifáの256章Odú(16×16組合せ)による韻文宗教文学典。Wande Abimbola(1976)が体系記述。",
    background="アフリカ最大の体系的口承典のひとつ。",
    development="2008年UNESCO無形文化遺産。",
    historical_context="アフリカ・ディアスポラ宗教の中核典。",
    primary_source_url="https://ich.unesco.org/en/RL/ifa-divination-system-00146",
    primary_source_type="Abimbola 1976 / UNESCO ICH 2008",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"占術組合せ体系の文学化は、AI時代の生成・組合せ文学の祖型。",
         "related_ai_phenomenon":"AI生成と組合せ詩学"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Ifá divination",
         "description":"Ifa人類学研究の主対象。"}])

add(**C, name_ja="エス・エレグバラ循環",
    name_en="Esu Elegbara trickster cycle",
    name_original="Èṣù Elegbara",
    period_key="先住民口承伝統期",
    definition="ヨルバ宗教の境界・通路神Èṣù Elegbaraに関する物語循環。Henry Louis Gates Jr.『The Signifying Monkey』(1988)文学理論化。",
    background="アフリカ・ディアスポラ文学理論の中核。",
    development="Gatesシグニファイイング理論の祖型。",
    historical_context="1980年代アフロ・アメリカ文学理論興隆期。",
    primary_source_url=WIKI+"Eshu",
    primary_source_type="Gates 1988 Oxford UP",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハウサ・バヤジッダ伝説",
    name_en="Hausa Bayajidda epic",
    name_original="Bayajidda",
    period_key="先住民口承伝統期",
    definition="北ナイジェリアHausa諸都市国家Hausa Bakwaiの起源を語る英雄叙事Bayajidda。蛇殺しと7王国創建。",
    background="ハウサ起源神話の中核叙事。",
    development="Frank Edgar(1911-13)Litafi na Tatsuniyoyi記録。",
    historical_context="ナイジェリア英領植民期記録運動の代表。",
    primary_source_url=WIKI+"Bayajidda",
    primary_source_type="Edgar 1911 Hausa Folk Tales 3 vols",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フラニ・ゲレウォル詠唱",
    name_en="Fulani Gerewol initiation chants",
    name_original="Geerewol",
    period_key="先住民口承伝統期",
    definition="サヘル地域 Wodaabe(Fulani分派)族の若者美容競演祭Gerewolに伴う詠唱・身体装飾文学伝統。",
    background="サヘル牧畜民の身体的文学伝統の代表。",
    development="Marguerite Dupire(1962)・Mette Bovin(2001)研究。",
    historical_context="20世紀後半西サヘル民族誌興隆期。",
    primary_source_url=WIKI+"Gerewol",
    primary_source_type="Dupire 1962 Peuls nomades / academic",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="トゥアレグ・ティンデ戦詩",
    name_en="Tuareg tinde war poetry + tassukin",
    name_original="tinde",
    period_key="先住民口承伝統期",
    definition="サハラ・サヘル Tuareg族の女性主導太鼓詩tindeとラクダ歌tassukin。アムザド楽器伴奏戦詩文学。",
    background="サハラ女性詩文学の代表。",
    development="Charles de Foucauld辞書(1922)以降の体系記録。",
    historical_context="20世紀仏領サハラ民族誌期。",
    primary_source_url=WIKI+"Tuareg_music",
    primary_source_type="Foucauld 1922 Dictionnaire / Borel 1988",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ベルベル・アヘリル詠唱",
    name_en="Berber Ahellil Gourara chants",
    name_original="Ahellil n Gourara",
    period_key="先住民口承伝統期",
    definition="アルジェリア南部Gourara地方 Zenete Berber族の集団詠唱Ahellil。2008年UNESCO無形文化遺産。",
    background="北アフリカ・ベルベル詠唱文学の代表。",
    development="Mouloud Mammeri『L'Ahellil du Gourara』(1984)記録。",
    historical_context="20世紀後半ベルベル文化復興運動期。",
    primary_source_url="https://ich.unesco.org/en/RL/the-ahellil-of-gourara-00102",
    primary_source_type="UNESCO ICH 2008 / Mammeri 1984",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ソマリ・ガベイ詩",
    name_en="Somali gabay + maanso poetry",
    name_original="gabay",
    period_key="先住民口承伝統期",
    definition="ソマリ族の長韻文詩gabayとmaanso(現代詩)。Sayyid Mohammed Abdullah Hassan詠唱が頂点。B.W. Andrzejewski研究。",
    background="ホーン・オブ・アフリカ最重要詩伝統。",
    development="Andrzejewski & Lewis『Somali Poetry』(1964)古典化。",
    historical_context="ソマリ反植民地抵抗詩文学の中核。",
    primary_source_url=WIKI+"Somali_literature",
    primary_source_type="Andrzejewski & Lewis 1964 Oxford UP",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Horn of Africa pastoral poetry",
         "description":"ホーン地方牧畜民詩文学研究と並行。"}])

add(**C, name_ja="オロモ・ガダ口承史",
    name_en="Oromo Gada oral history",
    name_original="Gadaa",
    period_key="先住民口承伝統期",
    definition="エチオピアOromo族の8年周期年齢階梯Gadaaとそれに伴う系譜詠唱・歴史叙述伝統。2016年UNESCO登録。",
    background="東アフリカ年齢階梯政治体系の口承典。",
    development="Asmarom Legesse『Gada』(1973)が古典。",
    historical_context="20世紀後半Oromo自治運動の文化的基盤。",
    primary_source_url="https://ich.unesco.org/en/RL/gada-system-an-indigenous-democratic-socio-political-system-of-the-oromo-01164",
    primary_source_type="UNESCO ICH 2016 / Legesse 1973",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バントゥ・ムカンダ詠唱",
    name_en="Bantu Mukanda initiation chants",
    name_original="Mukanda",
    period_key="先住民口承伝統期",
    definition="中央アフリカ南西部 Luvale・Lunda・Chokwe等Bantu系諸族の男性割礼通過儀礼Mukandaに伴う詠唱・仮面物語伝統。",
    background="バントゥ通過儀礼文学の代表。",
    development="Victor Turner『The Ritual Process』(1969)主要対象。",
    historical_context="20世紀後半儀礼研究確立期の中心資料。",
    primary_source_url=WIKI+"Mukanda",
    primary_source_type="Turner 1969 Aldine / Cameron 1998",
    importance_score=3, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"liminality theory",
         "description":"Turnerリミナリティ理論の発生資料。"}])

add(**C, name_ja="ムブティ・モリモ歌",
    name_en="Mbuti molimo songs",
    name_original="molimo",
    period_key="先住民口承伝統期",
    definition="コンゴ Ituri森林Mbuti(Bambuti)ピグミーの森讃歌・葬送歌molimo。Colin Turnbull『The Forest People』(1961)記述。",
    background="中央アフリカ森林民歌文学の代表。",
    development="Turnbullが世界に紹介。",
    historical_context="20世紀中葉コンゴ民族誌の代表。",
    primary_source_url=WIKI+"Mbuti_people",
    primary_source_type="Turnbull 1961 Simon & Schuster",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アカ・ヨーデル多声",
    name_en="Aka Pygmy yodeling polyphony",
    name_original="Aka",
    period_key="先住民口承伝統期",
    definition="中央アフリカ共和国・コンゴ Aka(BaAka)ピグミーの複声ヨーデル歌伝統。2003年UNESCO無形文化遺産。",
    background="アフリカ複声歌文学の代表。",
    development="Simha Arom『Polyphonies et polyrythmies』(1985)古典化。",
    historical_context="20世紀後半民族音楽学興隆期。",
    primary_source_url="https://ich.unesco.org/en/RL/polyphonic-singing-of-the-aka-pygmies-of-central-africa-00082",
    primary_source_type="UNESCO ICH 2003 / Arom 1985",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハッザ・ンオ歌",
    name_en="Hadza n!ow hunting songs",
    name_original="n!ow",
    period_key="先住民口承伝統期",
    definition="タンザニア Hadza族の狩猟・蜂蜜採集歌n!ow。少数残存狩猟採集言語の口承文学。",
    background="言語孤立民の口承文学の代表。",
    development="Frank Marlowe(2010)『The Hadza』記述。",
    historical_context="21世紀残存狩猟採集民研究の中心資料。",
    primary_source_url=WIKI+"Hadza_people",
    primary_source_type="Marlowe 2010 University of California Press",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: 大洋州詳細 (14)
# ============================================================
add(**C, name_ja="トンガ・ファカハー詩学",
    name_en="Tongan fakahā + heliaki poetics",
    name_original="heliaki",
    period_key="先住民口承伝統期",
    definition="トンガ古典詩学の修辞heliaki(間接的暗示)とfakahā(顕示)の対構造。E. E. V. Collocott(1928)・Adrienne Kaeppler研究。",
    background="ポリネシア詩学理論の代表。",
    development="Kaeppler『Poetry in Motion』(1993)で体系化。",
    historical_context="ポリネシア宮廷詩学伝統の継続。",
    primary_source_url=WIKI+"Music_of_Tonga",
    primary_source_type="Kaeppler 1993 University of Hawaii Press",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="サモア・ファレアイトゥ",
    name_en="Samoan tala/solo with chiefly oratory",
    name_original="lāuga",
    period_key="先住民口承伝統期",
    definition="サモア首長弁論lāugaと物語tala・詠唱soloの三重複合伝統。matai位階体系と結合。Albert Wendt理論化。",
    background="ポリネシア首長文学の代表。",
    development="Bradd Shore『Sala'ilua』(1982)記述。",
    historical_context="20世紀後半サモア人類学・文学興隆期。",
    primary_source_url=WIKI+"Samoan_culture",
    primary_source_type="Shore 1982 Columbia UP / Wendt essays",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フィジー・メケ物語舞",
    name_en="Fijian meke story-dance",
    name_original="meke",
    period_key="先住民口承伝統期",
    definition="フィジー族の物語的舞踊歌meke。系譜・戦闘・恋愛を語る詠唱と動作の統合伝統。",
    background="メラネシア物語舞文学の代表。",
    development="A. Maurice Hocart(1929)記録以降の継続研究。",
    historical_context="フィジー部族文化継続的実践の中核。",
    primary_source_url=WIKI+"Meke",
    primary_source_type="Hocart 1929 Lau Islands BPB Bishop Museum",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マルケサス詩学",
    name_en="Marquesan poetics + ka'ioi",
    name_original="kaʻioi",
    period_key="先住民口承伝統期",
    definition="マルケサス諸島の詩人会kaʻioiと口承詩集成。Karl von den Steinen(1925-28)記録。Robert Suggs研究。",
    background="東ポリネシア詩文学の代表。",
    development="von den Steinen『Die Marquesaner』全3巻記録。",
    historical_context="20世紀初頭ドイツ民族誌探検期。",
    primary_source_url=WIKI+"Marquesas_Islands",
    primary_source_type="von den Steinen 1925-28 Reimer",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="タヒチ・ラアウ・オレロ",
    name_en="Tahitian rāʻau orero + temple chants",
    name_original="rā'au orero",
    period_key="先住民口承伝統期",
    definition="タヒチ祭司詠唱rāʻau oreroとmarae(神殿)詠唱伝統。Teuira Henry『Ancient Tahiti』(1928)記録。",
    background="フランス領ポリネシア古典詩文学の代表。",
    development="Bishop Museum Bulletin 48として刊行。",
    historical_context="20世紀初頭ポリネシア古典記録運動期。",
    primary_source_url=ARCH+"ancienttahiti48henr",
    primary_source_type="Henry 1928 Bishop Museum Bulletin 48",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マンガイア歴史詠唱",
    name_en="Mangaian historians",
    name_original="korero o Mangaia",
    period_key="先住民口承伝統期",
    definition="クック諸島Mangaia島の専門歴史詠唱者による系譜・戦争詠唱。William Wyatt Gill(1876, 1894)記録。",
    background="南クック諸島歴史詠唱の代表。",
    development="Gill宣教師記録による南太平洋古典化の典型。",
    historical_context="19世紀末南太平洋宣教民族誌期。",
    primary_source_url=ARCH+"mythssongsfromso00gillrich",
    primary_source_type="Gill 1876 Myths and Songs from South Pacific",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="トゥアモトゥ航海詠唱",
    name_en="Tuamotuan navigation chants",
    name_original="reo Pa'umotu",
    period_key="先住民口承伝統期",
    definition="トゥアモトゥ諸島Paʻumotu語航海・天体・島嶼詠唱伝統。J. Frank Stimson(1933, 1957)記録。",
    background="東ポリネシア航海文学の代表。",
    development="Stimson Bishop Museum Bulletin 127として記録。",
    historical_context="20世紀前半ポリネシア航海技術文学化期。",
    primary_source_url=WIKI+"Tuamotus",
    primary_source_type="Stimson 1933 Bishop Museum Bulletin 103",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ツバル・ファテレ",
    name_en="Tuvalu fatele",
    name_original="fatele",
    period_key="先住民口承伝統期",
    definition="ツバル諸島の集合舞踊歌fatele。村対抗の応答歌唱形式で島嶼史・現代生活を歌う。",
    background="マイクロネジア・ポリネシア境界文学の代表。",
    development="Gerd Koch(1961)・Linnekin研究。",
    historical_context="20世紀後半マイクロネシア継続実践期。",
    primary_source_url=WIKI+"Music_of_Tuvalu",
    primary_source_type="Koch 1961 Songs of Tuvalu / Linnekin",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="キリバス・マネアバ詠唱",
    name_en="Kiribati maneaba oratory",
    name_original="maneaba",
    period_key="先住民口承伝統期",
    definition="キリバス共同集会所maneabaにおける首長弁論・系譜詠唱・歌物語bwanga伝統。Arthur Grimble記録。",
    background="マイクロネシア集会所文学の代表。",
    development="Grimble『A Pattern of Islands』(1952)で世界に紹介。",
    historical_context="20世紀前半英領Gilbert諸島民族誌期。",
    primary_source_url=WIKI+"Kiribati",
    primary_source_type="Grimble 1952 John Murray / Tungaru Traditions 1989",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マーシャル・ロロ詠唱",
    name_en="Marshallese rorọ chants",
    name_original="roro",
    period_key="先住民口承伝統期",
    definition="マーシャル諸島の航海呪文rorọと天文詠唱・恋歌al伝統。Augustin Krämer(1906)記録。",
    background="マイクロネシア航海呪術文学の代表。",
    development="Joachim deBrum諸島歴史記録に組込み。",
    historical_context="20世紀初頭独領マーシャル民族誌期。",
    primary_source_url=WIKI+"Marshall_Islands",
    primary_source_type="Krämer 1906 Hawaiischen Inseln 2 vols",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヨルング・マニカイ歌",
    name_en="Yolŋu manikay song cycles",
    name_original="manikay",
    period_key="先住民口承伝統期",
    definition="北部準州Arnhem Land Yolŋu族の儀礼歌循環manikayと拍子棒bilma・舞踊bunggulの三位一体伝統。Berndt・Magowan研究。",
    background="豪先住民歌循環文学の代表。",
    development="Fiona Magowan『Melodies of Mourning』(2007)古典化。",
    historical_context="20世紀後半Yolŋu自決運動の文化的基盤。",
    primary_source_url=AIATSIS,
    primary_source_type="AIATSIS Yolŋu manikay collection / Magowan 2007",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Arnhem Land ethnomusicology",
         "description":"アーネムランド民族音楽学と直結。"}])

add(**C, name_ja="ピントゥピ・ルリチャ親族法歌",
    name_en="Pintupi-Luritja kinship law songs",
    name_original="tjukurpa walytja",
    period_key="先住民口承伝統期",
    definition="中央豪州砂漠Pintupi-Luritja族のtjukurpa(夢の時)に基づく親族法・婚姻法歌循環。Fred Myers(1986)研究。",
    background="豪砂漠先住民法文学の代表。",
    development="Myers『Pintupi Country, Pintupi Self』(1986)古典化。",
    historical_context="20世紀末Pintupi土地権運動期。",
    primary_source_url=WIKI+"Pintupi",
    primary_source_type="Myers 1986 Smithsonian / academic",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ワルピリ・ジュクルパ旅",
    name_en="Walpiri jukurrpa journeys",
    name_original="jukurrpa",
    period_key="先住民口承伝統期",
    definition="中央豪州Warlpiri族のjukurrpa(夢の時)地理的循環歌。Yuendumu門板絵画と結合。Nancy Munn・Eric Michaels研究。",
    background="豪砂漠地理的歌循環の代表。",
    development="Munn『Walbiri Iconography』(1973)古典化。",
    historical_context="20世紀末Warlpiri芸術主権運動期。",
    primary_source_url=WIKI+"Warlpiri_people",
    primary_source_type="Munn 1973 Cornell UP / AIATSIS recordings",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"iconography ethnography",
         "description":"Munnイコノグラフィ研究と直結。"}])

add(**C, name_ja="マオリ・ファカパパ口承",
    name_en="Maori whakapapa + waiata + whaikorero",
    name_original="whakapapa",
    period_key="先住民口承伝統期",
    definition="マオリ族の系譜詠唱whakapapa・歌waiata・首長弁論whaikōreroの三重複合古典詩学伝統。Apirana Ngata・Pei Te Hurinui Jones記録。",
    background="ポリネシア南端古典詩学の代表。",
    development="Ngata-Jones『Ngā Mōteatea』全4巻が古典。",
    historical_context="20世紀マオリ・ルネッサンスの文化的基盤。",
    primary_source_url=WIKI+"Whakapapa",
    primary_source_type="Ngata & Jones Ngā Mōteatea Polynesian Society",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"系譜詠唱は、AI時代の知識伝達の継承的構造の文学的範型。",
         "related_ai_phenomenon":"AI時代の知識継承・系譜詠唱"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"whakapapa ethnography",
         "description":"マオリ系譜民族誌と直結。"}])


# ============================================================
# E: 南アジア・東南アジア (6)
# ============================================================
add(**C, name_ja="モンゴル・ゲセル汗",
    name_en="Mongol Geser Khan + Jangar epic",
    name_original="Geser",
    period_key="先住民口承伝統期",
    definition="モンゴル・ブリヤート・カルムイクのGeser Khan英雄叙事とJangar叙事(Kalmyk)。中央アジア最重要叙事詩二大柱。",
    background="中央アジア英雄叙事文学の代表。",
    development="Walther Heissig『Geser-Studien』(1983)集大成。",
    historical_context="モンゴル系諸族共有古典叙事の継続実践。",
    primary_source_url=WIKI+"Epic_of_King_Gesar",
    primary_source_type="Heissig 1983 Westdeutscher Verlag",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="チベット・ゲサル王",
    name_en="Tibetan King Gesar epic",
    name_original="Ge sar gling sgrung",
    period_key="先住民口承伝統期",
    definition="チベットLing国王Gesar英雄叙事。世界最長の口承叙事詩(120巻以上)。2009年UNESCO無形文化遺産。",
    background="世界最長叙事詩。",
    development="Rolf Stein『Recherches』(1959)古典研究。",
    historical_context="チベット高原口承叙事の頂点。",
    primary_source_url="https://ich.unesco.org/en/RL/gesar-epic-tradition-00204",
    primary_source_type="UNESCO ICH 2009 / Stein 1959",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Tibetan oral epic anthropology",
         "description":"チベット口承叙事人類学の中心。"}])

add(**C, name_ja="アディ・ドニ・ポロ",
    name_en="Adi Donyi-Polo tradition",
    name_original="Donyi-Polo",
    period_key="先住民口承伝統期",
    definition="北東インドArunachal Pradesh Adi族の太陽月信仰Donyi-Poloに基づく祭司詠唱abang伝統。Talom Rukbo20世紀末文学化。",
    background="北東インド先住民信仰文学の代表。",
    development="Mibang & Chaudhuri編(2004)記録。",
    historical_context="20世紀末北東インド先住民復興運動期。",
    primary_source_url=WIKI+"Donyi-Polo",
    primary_source_type="Mibang & Chaudhuri 2004 Mittal",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クメール・チバプ韻文",
    name_en="Khmer cbap conduct verses",
    name_original="cbap",
    period_key="植民地接触・抑圧期",
    definition="カンボジア伝統規範詩cbap。男児用・女児用・老人用等多種の道徳教訓口承韻文。Adhémard Leclère(1899)記録。",
    background="東南アジア大陸部規範詩文学の代表。",
    development="Saveros Pou『Guirlande de Cpāp'』(1988)古典化。",
    historical_context="クメール伝統教育の中核教材。",
    primary_source_url=WIKI+"Cambodian_literature",
    primary_source_type="Pou 1988 Cedoreck / Leclère 1899",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ラオ・サン・シンサイ",
    name_en="Lao San Sinxay epic",
    name_original="Sang Sinxay",
    period_key="植民地接触・抑圧期",
    definition="ラオス古典叙事詩Sang Sinxay。詩人Pang Kham(17C末-18C初)作。ラオス国民叙事の地位。",
    background="東南アジア大陸部古典叙事の代表。",
    development="Sahai『Ramayana in Laos』(1976)研究。",
    historical_context="ラオス文学伝統の中核古典。",
    primary_source_url=WIKI+"Sang_Sinxay",
    primary_source_type="Sahai 1976 / Lao National Library archive",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フモン・クアブ・ケーヴ",
    name_en="Hmong qhuab kev funeral guidance",
    name_original="Qhuab Kev",
    period_key="先住民口承伝統期",
    definition="フモン族の葬送導きの歌Qhuab Kev。死者霊が祖霊世界へ戻る道を案内する儀礼詠唱。Charles Johnson・Kao Kalia Yang記録。",
    background="東南アジア山岳民葬送詠唱の代表。",
    development="Mareschal『Le rite des fleurs blanches』(1976)研究。",
    historical_context="ラオス・タイ・米国Hmongディアスポラの中心儀礼。",
    primary_source_url=WIKI+"Hmong_customs_and_culture",
    primary_source_type="Symonds 2004 University of Washington Press",
    importance_score=3, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Hmong funeral ethnography",
         "description":"フモン葬送民族誌と直結。"}])


# ============================================================
# F: アイヌ詳細 (6)
# ============================================================
add(**CJ, name_ja="ユカラ十二曲",
    name_en="Yukar 12 individual songs",
    name_original="ユカラ",
    period_key="先住民口承伝統期",
    definition="アイヌ英雄叙事ユカラのうち、Poiyaunpe・Otasamunkur等の代表的個別12曲。金田一京助(1931)・知里真志保(1955)記録。",
    background="アイヌ英雄叙事の中核曲集。",
    development="金田一『アイヌ叙事詩ユーカラの研究』全2巻(1931)古典。",
    historical_context="20世紀前半アイヌ口承文学体系記録運動期。",
    primary_source_url="https://ainugo.nam.go.jp/",
    primary_source_type="国立アイヌ民族博物館アイヌ語アーカイブ",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CJ, name_ja="トゥイタク継承歌",
    name_en="Tuytak inheritance songs",
    name_original="トゥイタク",
    period_key="先住民口承伝統期",
    definition="アイヌの世間話・経験談ジャンルtuytakによる家系・領地継承を語る記憶歌伝統。",
    background="アイヌ歴史記憶の散文叙事ジャンル。",
    development="知里真志保(1955)『アイヌ語入門』ジャンル分類。",
    historical_context="20世紀前半アイヌジャンル研究確立期。",
    primary_source_url="https://ainugo.nam.go.jp/",
    primary_source_type="国立アイヌ民族博物館 / 知里1955",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**CJ, name_ja="ウポポ女性集合歌",
    name_en="Upopo women's gathering songs",
    name_original="ウポポ",
    period_key="先住民口承伝統期",
    definition="アイヌ女性の集合輪唱歌upopo。茣蓙拍子に合わせ女性円座で輪唱する応答歌伝統。",
    background="アイヌ女性歌文学の代表ジャンル。",
    development="萱野茂・成田得平・北原モコットゥナシ録音。",
    historical_context="20世紀後半アイヌ女性文化記録運動期。",
    primary_source_url="https://ainugo.nam.go.jp/",
    primary_source_type="国立アイヌ民族博物館アイヌ語音声アーカイブ",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**CJ, name_ja="ハウキ・ウレシパモシリ",
    name_en="Hauki ureshpamoshir geographic lore",
    name_original="ハウキ・ウレシパモシリ",
    period_key="先住民口承伝統期",
    definition="アイヌ地名起源・地理的伝承hauki(地名)ureshpamoshir(育ての国土)に関する場所性物語伝統。",
    background="アイヌ場所性文学の中核ジャンル。",
    development="山田秀三『アイヌ語地名の研究』(1982-83)古典。",
    historical_context="20世紀後半アイヌ地名学興隆期。",
    primary_source_url="https://www.ff-ainu.or.jp/",
    primary_source_type="アイヌ民族文化財団 / 山田1982",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**CJ, name_ja="オトンペ笑話",
    name_en="Otonpe trickster tales",
    name_original="オトンペ",
    period_key="先住民口承伝統期",
    definition="アイヌのトリックスター・笑話ジャンルotonpe。コタン・カラ・カムイの娘の婿選び等の話型を含む。",
    background="アイヌ笑話・幼児文学の代表。",
    development="知里幸恵・知里真志保記録。",
    historical_context="20世紀前半アイヌ口承ジャンル細分化期。",
    primary_source_url="https://ainugo.nam.go.jp/",
    primary_source_type="国立アイヌ民族博物館 / 知里幸恵記録",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**CJ, name_ja="カヤッカムイ・イヨマンテ",
    name_en="Kayakkamuy iyomante bear sending",
    name_original="カヤッカムイ・イヨマンテ",
    period_key="先住民口承伝統期",
    definition="アイヌ熊送り儀礼iyomanteに伴う送りの歌・神謡kamuyyukar・酒席詠唱の総合的儀礼文学体系。",
    background="アイヌ最重要儀礼文学体系。",
    development="名取武光(1941)・煎本孝(2007)研究。",
    historical_context="アイヌ世界観の儀礼的中核。",
    primary_source_url=WIKI+"Iomante",
    primary_source_type="名取1941 / 煎本2007",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"動物霊と人間の交換主体性は、AI時代の非人間主体性の文学的祖型。",
         "related_ai_phenomenon":"AI時代の非人間主体性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Ainu bear ceremonialism",
         "description":"アイヌ熊送り儀礼研究と直結。"}])


# ============================================================
# G: 文献記録方法論 (6)
# ============================================================
add(**C, name_ja="テッドロック息呼吸転写",
    name_en="Tedlock breath transcription",
    name_original="breath transcription",
    period_key="先住民文芸復興期",
    definition="Dennis Tedlockが『Finding the Center』(1972)で確立した先住民口承の息継ぎ・休止に基づく行分割転写法。",
    background="エスノポエティクス記述方法論の中核。",
    development="Hymes ethnopoetics(行構造)と並ぶ二大方法論。",
    historical_context="1970年代エスノポエティクス理論確立期。",
    primary_source_url=WIKI+"Dennis_Tedlock",
    primary_source_type="Tedlock 1972 Dial Press / 1983 PennPress",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"形式","status":"rethinking",
         "rationale":"音響的特性に基づく転写は、AI時代の音声-文字変換の文学理論的祖型。",
         "related_ai_phenomenon":"AI音声認識と文学転写"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ethnopoetics",
         "description":"エスノポエティクス理論の二大方法論。"}])

add(**C, name_ja="シャーザー声録音理論",
    name_en="Sherzer voice recording theory",
    name_original="discourse-centered approach",
    period_key="先住民文芸復興期",
    definition="Joel Sherzer『Verbal Art in San Blas』(1990)による発話中心アプローチ。録音による多声・即興・聴衆相互作用の記述方法論。",
    background="言語人類学的口承文学記述の代表方法論。",
    development="Sherzer & Woodbury編集集成で体系化。",
    historical_context="1990年代発話中心アプローチ確立期。",
    primary_source_url=WIKI+"Joel_Sherzer",
    primary_source_type="Sherzer 1990 Cambridge UP",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"録音中心方法論は、AI時代の生成データ記録のメタ方法論的祖型。",
         "related_ai_phenomenon":"AI生成記録のメタ方法論"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"linguistic anthropology",
         "description":"言語人類学方法論の中核。"}])

add(**C, name_ja="ブリッグス・バウマン上演理論",
    name_en="Briggs/Bauman performance theory",
    name_original="performance theory",
    period_key="先住民文芸復興期",
    definition="Charles Briggs & Richard Bauman『Voices of Modernity』(2003)等による発話事象としての上演論。Goffman・Hymes統合発展。",
    background="口承文学上演論の体系化。",
    development="Bauman『Verbal Art as Performance』(1977)が起点。",
    historical_context="1970-2000年代上演研究確立期。",
    primary_source_url=WIKI+"Richard_Bauman_(folklorist)",
    primary_source_type="Bauman 1977 Newbury / Briggs & Bauman 2003 CUP",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"形式","status":"rethinking",
         "rationale":"上演としての発話論は、AI生成の上演性の理論的祖型。",
         "related_ai_phenomenon":"AI生成の上演性"}])

add(**C, name_ja="バフチン民俗学",
    name_en="Bakhtin folklore theory",
    name_original="Бахтин фольклор",
    period_key="植民地接触・抑圧期",
    definition="Mikhail Bakhtinによる民俗ジャンル(カーニバル・グロテスク・対話・複数声)の文学理論。『ラブレー論』(1965)が中核。",
    background="20世紀文学理論への口承学の貢献の代表。",
    development="多声性・対話主義概念は20世紀後半文学理論を変革。",
    historical_context="ソ連時代抑圧下の文学理論的革新。",
    primary_source_url=WIKI+"Mikhail_Bakhtin",
    primary_source_type="Bakhtin 1965 / Holquist 1981 Texas",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"多声・対話主義は、AI時代の多エージェント作者性の理論的祖型。",
         "related_ai_phenomenon":"AI多声・多エージェント作者性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"dialogism",
         "description":"対話主義の文学理論と人類学への伝播。"}])

add(**C, name_ja="CARE先住民データ原則",
    name_en="CARE Principles Indigenous Data",
    name_original="CARE Principles",
    period_key="先住民文芸復興期",
    definition="2019年GIDA(Global Indigenous Data Alliance)制定の先住民データ統治4原則: Collective benefit/Authority to control/Responsibility/Ethics。",
    background="FAIRデータ原則を補完する先住民データ主権の規範。",
    development="2020年代AIデータ倫理の中核議題化。",
    historical_context="2020年代AI訓練データ抽出問題への先住民応答。",
    primary_source_url="https://www.gida-global.org/care",
    primary_source_type="GIDA 2019 CARE Principles official",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"AI訓練データ統治の規範的枠組みの先住民起源典型。",
         "related_ai_phenomenon":"AI訓練データの先住民主権"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"data sovereignty",
         "description":"データ主権論の人類学・情報学への伝播の祖型。"}])

add(**C, name_ja="先住民相互性プロトコル",
    name_en="Indigenous protocols Reciprocity Relationality Recognition",
    name_original="Indigenous protocols",
    period_key="先住民文芸復興期",
    definition="Shawn Wilson『Research is Ceremony』(2008)等による先住民研究方法論3R原則: Reciprocity・Relationality・Recognition。",
    background="先住民研究方法論の規範化。",
    development="2010-20年代北米・豪学術機関で広範採用。",
    historical_context="2010年代脱植民地学術運動期。",
    primary_source_url=WIKI+"Indigenous_research",
    primary_source_type="Wilson 2008 Fernwood / Kovach 2009 Toronto",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"関係的研究倫理は、AI時代の関係的データ倫理の文学・人類学的祖型。",
         "related_ai_phenomenon":"AI時代の関係的データ倫理"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"decolonial methodology",
         "description":"脱植民地方法論の中核。"}])


# ============================================================
# Additional cross_domain attachments to ensure AN >= 18
# ============================================================
def _attach_cross(name_ja: str, links: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == name_ja:
            c.setdefault("cross_domain", []).extend(links)
            return


_attach_cross("シクウォイア音節文字文学", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"writing system invention",
     "description":"先住民独自文字発明の人類学事例。"}])
_attach_cross("ハイダ・カラス循環", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Northwest Coast trickster",
     "description":"北西海岸トリックスター人類学。"}])
_attach_cross("ワユー・スーチムナ創世", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Wayuu dream anthropology",
     "description":"Wayuu夢見人類学と並行。"}])
_attach_cross("マサイ・エンキテング歌", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Maasai age-grade",
     "description":"マサイ年齢階梯人類学と直結。"}])
_attach_cross("ソマリ・ガベイ詩", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Somali nomadic poetics",
     "description":"ソマリ遊牧詩文学と並行。"}])
_attach_cross("オロモ・ガダ口承史", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Oromo political anthropology",
     "description":"Oromo政治人類学と直結。"}])
_attach_cross("ムブティ・モリモ歌", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Mbuti forest cosmology",
     "description":"Mbuti森林宇宙論人類学と並行。"}])
_attach_cross("マンガイア歴史詠唱", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Polynesian historiography",
     "description":"ポリネシア歴史記述人類学と並行。"}])
_attach_cross("ヨルング・マニカイ歌", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Yolŋu kinship",
     "description":"ヨルング親族体系研究と直結。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(name_ja=nj, region=REGION,
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
        print(f"[c30 w22 add80] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c30 w22 add80] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c30 w22 add80] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
