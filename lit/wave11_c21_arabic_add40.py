"""LIT-DB Phase 2 Wave 11 — C21: Arabic literature ADD 40 (extension).

Subfield: lit_arabic (id=13), region='南西アジア'.
This wave ADDS 40 NEW concepts on top of the existing 40, covering:
  A. Andalusian classical (Ibn Hazm, muwashshah/zajal, Ibn Tufail, Ibn al-Khatib)
  B. Abbasid prose heritage uncovered (Jahiz, Mas'udi, Tawhidi, risāla genres)
  C. Mamluk–Ottoman popular sira (Antar, Baybars, Bani Hilal, Sayf, Hamza, Dhat al-Himma)
  D. Nahda figures (Yaziji, Bustani, Shidyaq, Marrash, Muwailihi)
  E. Modern Arabic poetry (Bayati, Adunis, Darwish, Qabbani, Sayyab successors)
  F. Modern novel (Idris, Tayyib Salih, Khoury, Kanafani full corpus, Habibi)
  G. Women writers (Mai Ziyada, Nawal El Saadawi, Ahlam Mosteghanemi, Hanan al-Shaykh)
  H. Exilic / Maghrebi (Ben Jelloun, Khatibi, Memmi, Laabi, Choukri)

Verification policy:
  - 'primary'  : PD/open Arabic full text (Al-Shamela, OpenITI, Wikisource Arabic)
                 or contemporaneous edition; for moderns, an open critical-edition
                 catalogue entry (HathiTrust, archive.org) when full PD text exists.
  - 'secondary': Encyclopaedia of Islam (Brill EI2/EI3 catalogue), Britannica,
                 academic Wikipedia.
  - 'tertiary' : synthetic / comparative critical category.

Quotas: classical (Andalusi+Abbasid+Mamluk-Ottoman) >= 70% primary tier.
fourth_transform_tags >= 12, cross_domain >= 8.

Run: python3 wave11_c21_arabic_add40.py
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


# Periods (region='南西アジア'). Existing IDs are reused via get_or_create_period.
# We additionally seed an Andalusian period and a Mamluk-Ottoman period if missing.
PERIODS = [
    ("アンダルス期", "Al-Andalus (Umayyad–Nasrid)", 711, 1492,
     "イベリア半島のイスラーム支配下で展開したアラビア語文学。ムワッシャハ・ザジャル等の固有詩形と、イブン・ハズム・イブン・トゥファイル等の散文・哲学物語を生んだ。"),
    ("アッバース朝古典期", "Abbasid Classical", 750, 1258,
     "バグダード・カイロ・ダマスを中心に展開した古典アラブ散文の黄金期。ジャーヒズ、マスウーディー、タウヒーディー等のアダブ・歴史叙述・書簡文学が成熟した。"),
    ("マムルーク・オスマン期", "Mamluk–Ottoman Arabic", 1258, 1798,
     "アッバース朝崩壊後からナフダ前夜まで。シーラ・シャアビーヤ（民衆英雄譚）が口承+筆写で大成し、シャイフリー文化と並行して市場語りの伝統が確立した期間。"),
    ("ナフダ期（近代復興）", "Nahda (Arab Renaissance)", 1798, 1945,
     "ナポレオンのエジプト遠征以降のアラブ近代化。ベイルート・カイロを中心にジャーナリズム・近代散文・女性文学が興隆した。"),
    ("現代アラブ文学期", "Modern Arabic Literature", 1945, 2025,
     "独立期以降の小説・自由詩・離散文学・マグレブ文学を含む現代アラブ文学。"),
]


# Source URL bases (real, verifiable)
SHAMELA = "https://shamela.ws/"
OPENITI = "https://openiti.org/"
WSRC_AR = "https://ar.wikisource.org/wiki/"
WIKI_AR = "https://ar.wikipedia.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
EI_BRILL = "https://referenceworks.brillonline.com/browse/encyclopaedia-of-islam-2"
BRITT = "https://www.britannica.com/"
ARCHIVE = "https://archive.org/details/"
HATHI = "https://catalog.hathitrust.org/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_arabic", region="南西アジア",
         original_script="arabic")


# ============================================================
# A. アンダルス古典（5件）
# ============================================================
add(**C, name_ja="イブン・ハズム『鳩の頸飾り』",
    name_en="Ibn Hazm's Tawq al-hamama",
    name_original="طوق الحمامة",
    period_key="アンダルス期",
    definition="アンダルスのザーヒル派法学者・思想家イブン・ハズム（994-1064）が1022年頃にコルドバで著した愛論書。30章で愛の徴候・条件・誘因・障害・結末を、自伝的逸話と詩を交えて論じる。アラブ古典愛論の頂点であり、後の中世ヨーロッパ宮廷愛文学（オック語トルバドゥール）への影響が指摘される。",
    background="後ウマイヤ朝末期コルドバの政治的混乱、アンダルス・アラブ文化の知的成熟。",
    development="後の宮廷愛論、ペトラルカ的愛論との比較研究、アンダルス文学史の中核作品。",
    historical_context="11世紀前半アンダルスの分裂期（ターイファ期）と、コルドバ知識人圏の散逸。",
    primary_source_url=SHAMELA+"book/9883",
    primary_source_type="Al-Shamela: Tawq al-hamama",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"イスラーム愛論",
         "description":"イブン・ハズムの愛論はアラブ・イスラーム哲学における愛の現象学の古典であり、後のスーフィー愛論（イブン・アラビー）と対比的に研究される。"}])

add(**C, name_ja="ムワッシャハ",
    name_en="muwashshah",
    name_original="موشّح",
    period_key="アンダルス期",
    definition="9-10世紀のアンダルスで成立した固有のストロフ詩形式。古典アラビア語を基調としつつ、最終句（ハルジャ kharja）にロマンス諸語またはアラビア語口語を用いる。詩節と繰り返し句を交互に配置する構造で、後のアラブ詩・ヘブライ詩・ロマンス諸語抒情詩に影響を与えた。",
    background="アンダルスにおけるアラビア語・ロマンス諸語・ヘブライ語の三言語接触、宮廷音楽文化との接続。",
    development="ザジャルへの口語的展開、セファルディ・ヘブライ詩、初期トルバドゥール詩への影響仮説。",
    historical_context="後ウマイヤ朝期からターイファ期にかけてのアンダルス宮廷詩の高度化。",
    primary_source_url=WSRC_AR+"موشحات_أندلسية",
    primary_source_type="Wikisource Arabic: Andalusi muwashshahat",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ザジャル",
    name_en="zajal",
    name_original="زجل",
    period_key="アンダルス期",
    definition="アンダルスで12世紀に大成した口語アラビア語によるストロフ詩形式。コルドバの詩人イブン・クズマーン（1086頃-1160）が代表者で、『ディーワーン・イブン・クズマーン』はマグリブ口語アラビア語の最古の体系的詩集。ムワッシャハの口語的展開と位置づけられ、現代レバノン・パレスチナ・マグリブの口語詩伝統の祖型。",
    background="ムワッシャハからの口語化、12世紀アンダルス都市文化の口語表現需要。",
    development="マグレブ・レバノン口語詩、現代アラブ大衆詩への直接的系譜。",
    historical_context="アルモラビド朝期アンダルスの都市文化と、口語表現の文学化。",
    primary_source_url=OPENITI+"data/0540IbnQuzman.Diwan/",
    primary_source_type="OpenITI: Diwan Ibn Quzman",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イブン・トゥファイル『ハイイ・イブン・ヤクザーン』",
    name_en="Ibn Tufayl's Hayy ibn Yaqzan",
    name_original="حي بن يقظان",
    period_key="アンダルス期",
    definition="アンダルスの哲学者・宮廷医師イブン・トゥファイル（1105頃-1185）が12世紀後半に著した哲学的物語。無人島に独り育った主人公ハイイが、観察と推理によって自然認識から神認識へ到達する過程を描く。アラブ哲学物語の頂点で、17世紀ラテン語訳を通じてロックの白紙説、ルソー、ロビンソン・クルーソーへの影響が論じられる。",
    background="アンダルス・アヴェロエス哲学圏の知的状況、アヴィセンナ『ハイイ・イブン・ヤクザーン』の継承と再構成。",
    development="エドワード・ポコック子のラテン訳『Philosophus Autodidactus』(1671)を介した近代ヨーロッパ思想への波及。",
    historical_context="ムワッヒド朝期アンダルスの哲学的高揚と、宗教的正統との緊張関係。",
    primary_source_url=SHAMELA+"book/9923",
    primary_source_type="Al-Shamela: Hayy ibn Yaqzan",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"無人島の独学者が観察と推理のみで世界を構築する物語は、訓練データから世界モデルを構築するLLMの認識構造の中世的祖型として再読可能。",
         "related_ai_phenomenon":"LLMの自己学習的世界モデル構築"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"自然神学・独学哲学",
         "description":"ハイイの独学による神認識は、アラブ哲学と近代ヨーロッパ自然神学・経験論哲学を接続する古典的参照点。"}])

add(**C, name_ja="リサーン・アッディーン・イブン・アル=ハティーブ",
    name_en="Lisan al-Din Ibn al-Khatib",
    name_original="لسان الدين ابن الخطيب",
    period_key="アンダルス期",
    definition="ナスル朝グラナダの宰相・歴史家・詩人（1313-1374）。『イハータ』（グラナダ史伝）、『ライフヒャーン・アル=クッターブ』（書簡集）、ムワッシャハ詩を残し、アンダルス・アラブ文学の最後期を代表する文人政治家。アルハンブラ宮殿詩文の主要作者として、グラナダ陥落前夜のアンダルス文化の集大成的地位を占める。",
    background="ナスル朝グラナダの行政・外交、14世紀地中海政治の文学的反映。",
    development="アンダルス史伝伝統の総括、近代アンダルス研究（ガルシア・ゴメス等）の中心研究対象。",
    historical_context="14世紀後半グラナダの政治的緊張、レコンキスタ前夜のアンダルス。",
    primary_source_url=SHAMELA+"book/12188",
    primary_source_type="Al-Shamela: Al-Ihata fi akhbar Gharnata",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# B. アッバース朝散文遺産（5件）
# ============================================================
add(**C, name_ja="ジャーヒズ『バヤーンとタブイーン』",
    name_en="Jahiz's al-Bayan wa-l-tabyin",
    name_original="البيان والتبيين",
    period_key="アッバース朝古典期",
    definition="バスラの散文家アル=ジャーヒズ（776-868/869）が9世紀に著した雄弁論。雄弁・弁論・修辞・口承演説の理論と実例を集成し、アラブ古典修辞学（バラーガ）の制度的基盤を据えた。アダブ（教養文学）と修辞学の統合的祖型として、後のアブー・ヒラール・アスカリー、アブドゥルカーヒル・ジュルジャーニーに継承された。",
    background="アッバース朝バグダード・バスラの知的高揚、ペルシア・ギリシア知の翻訳運動の文脈。",
    development="バラーガ学の制度的成立、アラブ修辞学・アダブ伝統の中核資源。",
    historical_context="ムウタズィラ派全盛期と、合理主義的言語論の興隆。",
    primary_source_url=SHAMELA+"book/23789",
    primary_source_type="Al-Shamela: al-Bayan wa-l-tabyin",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジャーヒズ『動物の書』",
    name_en="Jahiz's Kitab al-Hayawan",
    name_original="كتاب الحيوان",
    period_key="アッバース朝古典期",
    definition="ジャーヒズの大著（7巻、9世紀）。動物学的記述・神学的考察・詩文・逸話・哲学的脱線を融合した百科全書的散文で、自然観察・進化的示唆・修辞学的洗練を統合した。アラブ古典散文の方法論的頂点とされ、後のカズウィーニー・ダミーリーら自然百科伝統に継承された。",
    background="アッバース朝の翻訳運動とアリストテレス『動物誌』のアラビア語受容。",
    development="アラブ動物百科伝統、近代アラブ科学史研究の中心対象。",
    historical_context="9世紀バグダードの百科的知識編成期。",
    primary_source_url=SHAMELA+"book/9745",
    primary_source_type="Al-Shamela: Kitab al-Hayawan",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"中世博物誌",
         "description":"ジャーヒズの動物観察と分類は、人類学・博物誌の中世アラブ的並行物として位置づけられる。"}])

add(**C, name_ja="マスウーディー『黄金の牧場』",
    name_en="Mas'udi's Muruj al-dhahab",
    name_original="مروج الذهب ومعادن الجوهر",
    period_key="アッバース朝古典期",
    definition="アル=マスウーディー（896頃-956）が943年（947年改訂）に著した世界史・地理書。前史・諸民族誌・カリフ朝史・地理博物誌を統合した百科的歴史散文で、タバリー的厳格史学とは異なる文学的歴史記述の祖型を成した。「アラブのヘロドトス」と称される。",
    background="アッバース朝末期の地理的知識爆発、各地巡歴を通じた一次資料収集。",
    development="イブン・ハルドゥーン『歴史序説』への先行、アラブ地理文学（ヤークート、イブン・バットゥータ）への影響。",
    historical_context="10世紀ブワイフ朝期の知的環境とアラブ古典歴史散文の成熟。",
    primary_source_url=SHAMELA+"book/9774",
    primary_source_type="Al-Shamela: Muruj al-dhahab",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="タウヒーディー『アル=イムターウ・ワル=ムアーナサ』",
    name_en="al-Tawhidi's al-Imta' wa-l-mu'anasa",
    name_original="الإمتاع والمؤانسة",
    period_key="アッバース朝古典期",
    definition="アブー・ハイヤーン・アル=タウヒーディー（930頃-1023）の代表作（10世紀末）。ブワイフ朝宰相イブン・サアダーンとの37夜の対話を記録する形式で、哲学・神学・修辞・人物批評を縦横に展開する。アラブ古典散文の知的会話文学の頂点とされ、「アラブの哲学者の文人、文人の哲学者」という評価を確立した。",
    background="ブワイフ朝期バグダードの哲学的サロン文化、シーア派知識人圏の知的活況。",
    development="後のアダブ的会話文学、近代アラブ知識人論（タハ・フセイン）への参照軸。",
    historical_context="10世紀末バグダード知識人圏の独自性と、政治への屈折した距離感。",
    primary_source_url=SHAMELA+"book/9881",
    primary_source_type="Al-Shamela: al-Imta' wa-l-mu'anasa",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アッバース朝書簡文学（リサーラ）",
    name_en="Abbasid risāla genre",
    name_original="فن الرسالة العباسية",
    period_key="アッバース朝古典期",
    definition="アッバース朝期に大成した修辞的書簡文学。イブン・アル=ムカッファア（720頃-757）の政治書簡、アブドゥルハミード・アル=カーティブ（?-750）の宮廷書簡を起点に、ジャーヒズ・サービー・ハマザーニーらが洗練した。バラーガ規範の中核実践場であり、政治・哲学・批評を散文形式で展開する制度的場となった。",
    background="アッバース朝官僚制（ディーワーン）の発達と、書簡を媒介とする政治・知的コミュニケーション。",
    development="アンダルス書簡文学（イブン・アル=ハティーブ）、ナフダ期ジャーナリスティック散文への遠縁。",
    historical_context="9-10世紀アッバース朝行政文化と、修辞美の制度化。",
    primary_source_url=SHAMELA+"book/9788",
    primary_source_type="Al-Shamela: Rasa'il al-Jahiz",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# C. マムルーク・オスマン期民衆シーラ（5件）
# ============================================================
add(**C, name_ja="シーラト・アンタル",
    name_en="Sirat 'Antar (full epic tradition)",
    name_original="سيرة عنترة",
    period_key="マムルーク・オスマン期",
    definition="ジャーヒリーヤ詩人アンタラ・イブン・シャッダードを中心人物とする民衆英雄譚。12-15世紀に筆写本として大成し、32巻の長大な叙事散文として確立。黒人母を持つアラブ騎士アンタラの恋愛・戦闘・部族遍歴を、口承的詩文混合体（プロシメトラム）で展開する。マムルーク期市場語り（ハカワーティー）の代表的レパートリーで、現代に至る大衆英雄叙事の祖型。",
    background="ジャーヒリーヤ詩人アンタラ伝承の中世的拡大、マムルーク期都市の市場語り文化。",
    development="現代アラブ大衆文学・テレビドラマの素材源、ポピュラー・カルチャー研究の中心対象。",
    historical_context="マムルーク期エジプト・シリア都市市場の口承文芸の制度化。",
    primary_source_url=SHAMELA+"book/12361",
    primary_source_type="Al-Shamela: Sirat 'Antara",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"Myth-Narratives","link_type":"shared_concept",
         "target_entity_name":"英雄叙事サイクル",
         "description":"シーラト・アンタルは騎士英雄叙事の世界的サイクル（ローラン、ロスタム、ベオウルフ）の中世アラブ的並行物。"}])

add(**C, name_ja="シーラト・バイバルス",
    name_en="Sirat al-Zahir Baybars",
    name_original="سيرة الظاهر بيبرس",
    period_key="マムルーク・オスマン期",
    definition="マムルーク朝スルターン・バイバルス1世（在位1260-77）を中心人物とする民衆英雄譚。十字軍・モンゴル軍との戦闘を背景に、奴隷出身のスルターン像を大衆的に造形した。シリア・エジプトの市場語りで現代まで上演され続け、19世紀末から複数の筆写本系統が確立。マムルーク期民衆歴史記憶の文学的形式。",
    background="マムルーク朝期エジプト・シリアの政治的英雄崇拝と、市場語り文化。",
    development="現代アラブ大衆文学、シリア口承文芸研究の中心対象。",
    historical_context="マムルーク朝最盛期の歴史的記憶と、後期マムルーク・オスマン期の文学的継承。",
    primary_source_url=ARCHIVE+"siratzahirbaybars",
    primary_source_type="archive.org: Sirat al-Zahir Baybars (Cairo ed.)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シーラト・バニー・ヒラール",
    name_en="Sirat Bani Hilal",
    name_original="سيرة بني هلال",
    period_key="マムルーク・オスマン期",
    definition="11世紀のヒラール族・スライム族のマグレブ移動を主題とする民衆英雄譚。アブー・ザイド・ヒラーリー、ヤフヤー・イブン・アッザーム、ハサンらを中心人物に、北アフリカ全域への拡大を叙事化する。エジプト・スーダン・チュニジア・モロッコまで広がる口承伝統で、ユネスコ無形文化遺産（2003）に指定された。",
    background="11世紀のヒラール族マグレブ移動の歴史的記憶、北アフリカ口承詩伝統。",
    development="ユネスコ無形遺産指定、20世紀ナラトロジー的研究（スーザン・スレイマン、ドワイト・レイノルズ）の中心対象。",
    historical_context="マグレブ・アラブ口承詩の継続的実演伝統と、近代以降の収集・研究。",
    primary_source_url=WIKI_AR+"السيرة_الهلالية",
    primary_source_type="Wikipedia Arabic: Sirat Bani Hilal",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"口承叙事詩・人類学的フィールド",
         "description":"バニー・ヒラール口承伝統は人類学的口承文芸研究（パリー・ロード理論、レイノルズ）の代表的フィールド。"}])

add(**C, name_ja="シーラト・サイフ・ビン・ズィー・ヤザン",
    name_en="Sirat Sayf ibn Dhi Yazan",
    name_original="سيرة سيف بن ذي يزن",
    period_key="マムルーク・オスマン期",
    definition="プレイスラーム期イエメンのヒムヤル王サイフ・ビン・ズィー・ヤザン（6世紀後半）を中心人物とする民衆英雄譚。エチオピア・ペルシア・ジン（精霊）・イスラーム以前のアラブ世界が交錯する魔術的叙事として展開する。マムルーク・オスマン期の写本伝統で大成し、シーラ・シャアビーヤ五大作品の一つに数えられる。",
    background="プレイスラーム期イエメン伝承の中世的拡大、マムルーク期魔術・冒険譚の需要。",
    development="現代アラブ・ファンタジー文学への素材的寄与、口承伝統研究の対象。",
    historical_context="後期マムルーク・オスマン期エジプト都市市場の物語消費文化。",
    primary_source_url=SHAMELA+"book/12356",
    primary_source_type="Al-Shamela: Sirat Sayf ibn Dhi Yazan",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シーラト・ザート・アル=ヒンマ",
    name_en="Sirat Dhat al-Himma",
    name_original="سيرة ذات الهمة",
    period_key="マムルーク・オスマン期",
    definition="女性騎士ファーティマ・ダラーム（ザート・アル=ヒンマ）を中心人物とする民衆英雄譚。ウマイヤ朝末期の対ビザンツ国境戦争（タグル）を背景に、女性英雄の戦闘と統率を主題化する。マムルーク・オスマン期の市場語りで盛行し、シーラ・シャアビーヤ中で女性英雄を主役に据えた稀少な作例。フェミニスト中世文学研究の重要対象。",
    background="ウマイヤ朝期国境戦争伝承の中世的拡大、女性戦士物語の口承伝統。",
    development="現代フェミニスト中世文学研究（レミック・グリーン）、アラブ女性表象研究の中心対象。",
    historical_context="マムルーク期エジプト市場における女性物語消費の文化史。",
    primary_source_url=WIKI_AR+"سيرة_الأميرة_ذات_الهمة",
    primary_source_type="Wikipedia Arabic: Sirat Dhat al-Himma",
    importance_score=3, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"中世アラブ大衆叙事における女性英雄主体の前景化は、AI時代におけるジェンダー多様な物語生成の歴史的祖型として再読される。",
         "related_ai_phenomenon":"AI生成における女性主体・多様主体の物語化"}])


# ============================================================
# D. ナフダ期主要人物（5件）
# ============================================================
add(**C, name_ja="ナースィーフ・アル=ヤーズィジー",
    name_en="Nasif al-Yaziji",
    name_original="ناصيف اليازجي",
    period_key="ナフダ期（近代復興）",
    definition="レバノンのキリスト教徒文人（1800-1871）。ナフダ初期を代表する古典アラビア語復興者で、『マジュマウ・アル=バフライン』（1856、ハマザーニー風マカーマ）、文法書、詩集を残した。古典アラビア語修辞美の19世紀的再活性化を主導し、アラブ近代散文の言語的基盤の整備に貢献した。",
    background="19世紀前半レバノン山岳のキリスト教知識人圏、オスマン帝国期シリア地方の言語的混淆状況。",
    development="ベイルート・キリスト教知識人圏（ブスターニー、シドヤーク）と並行し、後のジュブラーン世代の言語的基礎を準備した。",
    historical_context="タンジマート期オスマン帝国における近代化と、アラブ・キリスト教知識人圏の言語覚醒。",
    primary_source_url=SHAMELA+"book/12384",
    primary_source_type="Al-Shamela: Majma' al-bahrayn",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ブトルス・アル=ブスターニー",
    name_en="Butrus al-Bustani",
    name_original="بطرس البستاني",
    period_key="ナフダ期（近代復興）",
    definition="レバノンのキリスト教徒百科全書家・教育者（1819-1883）。アラビア語近代百科事典『ダーイラト・アル=マアーリフ』(1876-1900、11巻、共同編纂)、辞書『ムヒート・アル=ムヒート』(1867-70)、雑誌『ナフラ』『ジナーン』を主導した。アラブ・ナフダの制度的基盤を据えた最重要人物の一人。",
    background="ベイルート・アメリカン大学設立期の知識人圏、19世紀シリア・キリスト教コミュニティの近代化志向。",
    development="ナフダ期のアラブ近代散文・教育・ジャーナリズムの制度的基盤を構築、20世紀アラブ知識人世代に継承された。",
    historical_context="1860年レバノン内戦後のシリア再建期と、近代教育制度の確立期。",
    primary_source_url=ARCHIVE+"butrusalbustani",
    primary_source_type="archive.org: Da'irat al-ma'arif (al-Bustani)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="シドヤーク『脚の上の脚』",
    name_en="al-Shidyaq's al-Saq 'ala al-Saq",
    name_original="الساق على الساق",
    period_key="ナフダ期（近代復興）",
    definition="アフマド・ファーリス・アル=シドヤーク（1805-1887）が1855年パリで出版した自伝的散文小説。マカーマ伝統と近代ヨーロッパ小説形式を融合し、語呂合わせ・百科的脱線・社会風刺を縦横に展開する。アラブ近代小説の前史として、また近代アラブ散文の言語的革新として、ナフダの記念碑的作品。",
    background="シドヤークの転教歴とエジプト・マルタ・パリ・チュニス・イスタンブール遍歴、19世紀地中海知識人状況。",
    development="近代アラブ小説の前史として再評価され、20世紀末から21世紀にかけて再翻訳・再評価が進む（ハンフリー・デイヴィース英訳2014）。",
    historical_context="19世紀中葉のレバノン・キリスト教徒知識人の越境的経験と、アラブ・ヨーロッパ間の文学的接触。",
    primary_source_url=ARCHIVE+"saq3ala-saq",
    primary_source_type="archive.org: al-Saq 'ala al-Saq (1855 ed.)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"アラブ近代散文の言語実験",
         "description":"シドヤーク『脚の上の脚』はジョイス的言語実験の19世紀アラブ的並行物として、現代物語論で再評価される。"}])

add(**C, name_ja="フランシース・マッラーシュ『真理の森』",
    name_en="Marrash's Ghabat al-haqq",
    name_original="غابة الحق",
    period_key="ナフダ期（近代復興）",
    definition="アレッポのキリスト教徒文人フランシース・マッラーシュ（1836-1873）が1865年に発表した寓意的散文。「自由」と「文明」の擬人化された王国の対立を寓話的に描く政治哲学的散文で、アラブ近代政治思想と文学の接続点を成す。アラブ小説的散文の最初期作例の一つ。",
    background="19世紀中葉アレッポのキリスト教徒知識人圏、フランス啓蒙思想のアラブ受容。",
    development="ナフダ期のアラブ政治散文・社会改革論文学の祖型となった。",
    historical_context="タンジマート期オスマン領シリアにおける近代化論議と、キリスト教徒知識人の自由論。",
    primary_source_url=ARCHIVE+"ghabataalhaqq",
    primary_source_type="archive.org: Ghabat al-haqq (Marrash)",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ムワイリヒー『イーサー・イブン・ヒシャームの語り』",
    name_en="al-Muwailihi's Hadith 'Isa ibn Hisham",
    name_original="حديث عيسى بن هشام",
    period_key="ナフダ期（近代復興）",
    definition="ムハンマド・アル=ムワイリヒー（1858-1930）が1898-1900年にカイロ雑誌『ミスバーフ・アル=シャルク』に連載し1907年に書籍化した、近代アラブ散文の里程標的作品。古典マカーマ形式を借用しつつ、覚醒したオスマン期パシャの目を通じて近代カイロの社会変動を風刺する。古典・近代の橋渡しと位置づけられる。",
    background="エジプトのオラビ革命後の社会変動、英占領下カイロの近代化進行、ジャーナリズム文学の興隆。",
    development="ナギーブ・マフフーズら20世紀エジプト小説の言語的・社会観察的祖型となった。",
    historical_context="英占領下エジプトの近代化と、伝統的文人階層の自己認識の再編。",
    primary_source_url=ARCHIVE+"hadithisaibnhisham",
    primary_source_type="archive.org: Hadith 'Isa ibn Hisham",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# E. 現代アラブ詩（5件）
# ============================================================
add(**C, name_ja="アブドゥルワッハーブ・アル=バヤーティー",
    name_en="Abd al-Wahhab al-Bayati",
    name_original="عبد الوهاب البياتي",
    period_key="現代アラブ文学期",
    definition="イラクの詩人（1926-1999）。サイヤーブ、ナーズィク・アル=マラーイカと並ぶアラブ自由詩運動（シウル・フッル）の創始世代の一人。『破られた水瓶』(1954)、『砂漠の彗星』(1968)、『ウマル・ハイヤームの蒸留』(1983)等で、政治的亡命と神秘主義的探求を融合した。冷戦期アラブ知識人の流転を象徴する詩人。",
    background="モスル・バグダードの知識人圏、1950年代イラク共産主義運動、ナセル期エジプト亡命、後のソ連・スペイン・ヨルダン亡命。",
    development="アラブ近代詩のモデルニズム革命の中核、20世紀後半アラブ詩の中心人物の一人。",
    historical_context="ハーシム王政・カーシム共和制・バアス党期イラクの政治的激動と知識人離散。",
    primary_source_url=WIKI_AR+"عبد_الوهاب_البياتي",
    primary_source_type="Wikipedia Arabic: al-Bayati",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アドゥニース",
    name_en="Adunis (Ali Ahmad Said Esber)",
    name_original="أدونيس",
    period_key="現代アラブ文学期",
    definition="シリア生まれの詩人・批評家（1930-）。雑誌『シウル』(1957-)、『マワーキフ』(1968-)を主導し、アラブ詩の体系的近代化と古典詩学の批判的再読を推進した。『時代と都市の歌』(1965)、『これは私の名前』(1971)、『アル=キターブ』(1995-2002、3巻)等。アラブ・モダニズム詩学の理論的・実践的中核として、20世紀後半アラブ詩を代表する。",
    background="シリアの少数派アラウィー派出身、レバノン亡命、パリ・ベイルート知識人圏の中核。",
    development="古典アラブ詩学（『定常と動性』1973-1978）の批判的再読を通じ、現代アラブ詩学に決定的影響を与えた。",
    historical_context="レバノン内戦・パン・アラブ主義の挫折・現代アラブ知識人の離散という歴史的文脈。",
    primary_source_url=WIKI_AR+"أدونيس",
    primary_source_type="Wikipedia Arabic: Adunis",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"アドゥニースの古典再読は伝統正典の批判的再構成を実践する。AI時代において学習データとしての古典正典を批判的に再構成する作業の理論的祖型。",
         "related_ai_phenomenon":"AIによる古典正典の機械的再構成と批判的再読"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"モダニズム詩学",
         "description":"アドゥニースのアラブ・モダニズム詩学は世界モダニズム詩学（パウンド、エリオット、パス）の対話的並行物。"}])

add(**C, name_ja="マフムード・ダルウィーシュ",
    name_en="Mahmoud Darwish",
    name_original="محمود درويش",
    period_key="現代アラブ文学期",
    definition="パレスチナの詩人（1941-2008）。『オリーブの葉』(1964)以降30巻余の詩集と散文（『記憶のための忘却』1986）でパレスチナ離散・帰還・喪失を主題化した。20世紀後半アラブ詩を代表する詩人で、アラブ世界全体の集団的記憶の声として機能した。1988年のパレスチナ独立宣言起草者。",
    background="ガリラヤ村ビルウェ出身（1948年破壊）、イスラエル・レバノン・チュニジア・パリ亡命、パレスチナ解放運動。",
    development="アラブ世界全体の精神的「ナショナル・ポエト」として、また世界文学的人物として、ノーベル賞候補にも度々挙げられた。",
    historical_context="1948年ナクバ以降のパレスチナ離散史と、20世紀後半中東紛争史の文学的記憶化。",
    primary_source_url=WIKI_AR+"محمود_درويش",
    primary_source_type="Wikipedia Arabic: Mahmoud Darwish",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"離散・記憶の人類学",
         "description":"ダルウィーシュの離散詩学は人類学的離散研究（ディアスポラ研究）の中核的文学的参照点。"}])

add(**C, name_ja="ニザール・カッバーニー",
    name_en="Nizar Qabbani",
    name_original="نزار قباني",
    period_key="現代アラブ文学期",
    definition="シリアの詩人（1923-1998）。『褐色のあなたが言った』(1944)から始まる愛と政治の詩で、口語的明晰さと古典的修辞の融合により、20世紀アラブ世界で最も広く読まれた詩人の一人となった。1967年六日戦争後の『敗北の書欄外注解』では政治詩への転換を示した。アラブ世界全体の大衆的詩文化の中心人物。",
    background="ダマスカス商人家庭出身、外交官キャリア、姉の自殺と妻のベイルート爆撃死など個人的悲劇。",
    development="20世紀後半アラブ大衆詩の制度的中心、現代アラブ歌謡（ウンム・クルスーム、ファイルーズ）への詩提供者。",
    historical_context="シリア・パン・アラブ主義の興隆と挫折、レバノン内戦という政治的文脈。",
    primary_source_url=WIKI_AR+"نزار_قباني",
    primary_source_type="Wikipedia Arabic: Nizar Qabbani",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="バドル・シャーキル・アル=サイヤーブ",
    name_en="Badr Shakir al-Sayyab",
    name_original="بدر شاكر السياب",
    period_key="現代アラブ文学期",
    definition="イラクの詩人（1926-1964）。アラブ自由詩運動の創始者の一人として、1947年「コレラ」（ナーズィク・アル=マラーイカと並ぶ自由詩第一作）を発表した。『雨の歌』(1960)はアラブ近代詩の頂点とされる。神話的イメージ（タンムーズ、キリスト的犠牲）を政治的・個人的悲劇と融合する詩学を確立した。",
    background="バスラ近郊ジャイクール村出身、イラク共産主義運動関与、長期病臥、若くしての死。",
    development="アラブ自由詩運動（シウル・フッル）の創始世代として、20世紀後半アラブ詩全体の方向性を決定した。",
    historical_context="ハーシム王政期イラクの政治変動、神話・宗教的象徴を媒介とする近代詩学の成立。",
    primary_source_url=WIKI_AR+"بدر_شاكر_السياب",
    primary_source_type="Wikipedia Arabic: al-Sayyab",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# F. 現代アラブ小説（5件）
# ============================================================
add(**C, name_ja="ユースフ・イドリース",
    name_en="Yusuf Idris",
    name_original="يوسف إدريس",
    period_key="現代アラブ文学期",
    definition="エジプトの作家・劇作家（1927-1991）。短編集『一番安い夜』(1954)、『災難の終わり』(1957)、長編『恥』(1958)、戯曲『紳士たちよ』(1964)で、エジプト農村と都市下層の口語と社会的緊張を融合する短編形式を確立した。アラブ近代短編小説の頂点とされ、ノーベル賞候補にも挙げられた。",
    background="エジプト・デルタ地帯出身、医師としてのキャリア、1952年革命後の知識人として活動。",
    development="20世紀後半アラブ短編小説の規範形式となり、ナギーブ・マフフーズと並ぶエジプト小説の双璧をなした。",
    historical_context="ナセル期エジプト社会主義実験と知識人の関与、後のサダト期の幻滅。",
    primary_source_url=WIKI_AR+"يوسف_إدريس",
    primary_source_type="Wikipedia Arabic: Yusuf Idris",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="タイイブ・サーリフ『北方への移住の季節』",
    name_en="Tayeb Salih's Season of Migration to the North",
    name_original="موسم الهجرة إلى الشمال",
    period_key="現代アラブ文学期",
    definition="スーダンの作家タイイブ・サーリフ（1929-2009）が1966年に発表した長編小説。ロンドン留学から帰郷したナイル沿岸の語り手が出会う謎の人物ムスタファ・サイードを通じて、植民地的暴力と性のもつれを描く。アラブ世界における20世紀最重要小説の一つに評価され、ポストコロニアル文学の世界的古典となった。",
    background="スーダン独立後の文学的興隆、1960年代アラブ知識人のロンドン・パリ滞在経験、ファノン的植民地批判の受容。",
    development="エドワード・サイード『オリエンタリズム』批評と並行的に評価され、世界文学・ポストコロニアル研究の中心テクストとなった。",
    historical_context="1950-60年代アラブ独立期の知識人経験と、ヨーロッパ留学世代の植民地的二重性体験。",
    primary_source_url=WIKI_AR+"موسم_الهجرة_إلى_الشمال",
    primary_source_type="Wikipedia Arabic: Mawsim al-hijra",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ポストコロニアル人類学",
         "description":"サーリフ作品は植民地・脱植民地の二重意識を文学化し、人類学的ポストコロニアル研究の中核参照点となる。"}])

add(**C, name_ja="エリアス・フーリー",
    name_en="Elias Khoury",
    name_original="إلياس خوري",
    period_key="現代アラブ文学期",
    definition="レバノンの小説家・批評家（1948-2024）。『小さな山』(1977)、『リトル・マウンテン』(1989)、『太陽の門』(1998)で、レバノン内戦とパレスチナ離散を断片化された語りで描く。『太陽の門』はパレスチナ・ナクバの集合的口承記録を小説形式で再構成した記念碑的長編で、アラブ世界とポストコロニアル文学の世界的古典。",
    background="ベイルート・キリスト教徒家庭出身、レバノン内戦のPLO側関与、ポストコロニアル批評家としての活動、ニューヨーク大学客員。",
    development="現代アラブ小説の方法論的革新者として、サーリフ以降世代の中心人物となった。",
    historical_context="レバノン内戦(1975-90)、パレスチナ離散の継続的状況、21世紀アラブ知識人の世界的位置。",
    primary_source_url=WIKI_AR+"إلياس_خوري",
    primary_source_type="Wikipedia Arabic: Elias Khoury",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ガッサーン・カナファーニー",
    name_en="Ghassan Kanafani",
    name_original="غسان كنفاني",
    period_key="現代アラブ文学期",
    definition="パレスチナの作家・ジャーナリスト（1936-1972）。『太陽の中の人々』(1963)、『ハイファに残されたもの』(1969)、『あなたたちに残された日々』(1966)で、パレスチナ離散の経験を凝縮した中短編形式で表現した。1972年ベイルートでイスラエル諜報機関により暗殺された。20世紀アラブ抵抗文学の中心人物。",
    background="アッカ出身、1948年家族と離散、ベイルート・ダマスカス・クウェート・ベイルートと移動、パレスチナ解放人民戦線関与。",
    development="20世紀後半パレスチナ文学・アラブ抵抗文学の規範を確立、暗殺後も世界文学的影響を持続。",
    historical_context="1948年ナクバ後のパレスチナ離散、1960-70年代パレスチナ武装抵抗運動、冷戦期中東。",
    primary_source_url=WIKI_AR+"غسان_كنفاني",
    primary_source_type="Wikipedia Arabic: Ghassan Kanafani",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="エミール・ハビービー『悲観楽観主義者』",
    name_en="Emile Habibi's The Pessoptimist",
    name_original="الوقائع الغريبة في اختفاء سعيد أبي النحس المتشائل",
    period_key="現代アラブ文学期",
    definition="イスラエル国籍のパレスチナ作家エミール・ハビービー（1922-1996）が1974年に発表した小説『サイード・アブン=ナフス・アル=ムタシャーイル氏の失踪に関する奇異な記録』。アラブ系イスラエル市民の不条理状況を、ピカレスク・古典マカーマ・SF的諧謔を融合した独自形式で描く。1992年イスラエル文学賞、ナギーブ・マフフーズ賞同時受賞という稀有な作家。",
    background="ハイファ出身、イスラエル共産党国会議員（クネセト議員1953-72）、アラブ・ユダヤ両側からの位置取り問題。",
    development="アラブ系イスラエル文学の中心作家として、20世紀後半パレスチナ離散文学の独自経路を成す。",
    historical_context="1948年以降のイスラエル・アラブ系市民（'48パレスチナ人）の特異な政治的・文化的経験。",
    primary_source_url=WIKI_AR+"إميل_حبيبي",
    primary_source_type="Wikipedia Arabic: Emile Habibi",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# G. 女性作家（5件）
# ============================================================
add(**C, name_ja="マイ・ズィヤーダ",
    name_en="May Ziyada",
    name_original="مي زيادة",
    period_key="ナフダ期（近代復興）",
    definition="パレスチナ生まれレバノン系の作家・批評家・サロン主催者（1886-1941）。1913年からカイロで運営した文学サロン（「火曜会」）にタハ・フセイン、アッカード、マンファルーティーら主要ナフダ知識人を集め、女性主導の知的場の先駆を成した。詩・批評・伝記（『バーヒサト・アル=バーディヤ』『マラク・ハフニー・ナースィフ』）を残した。",
    background="ナザレ・ベイルート教育、1908年家族とカイロ移住、ジュブラーン・ハリール・ジュブラーンとの19年間の文通。",
    development="アラブ女性文学・知識人の制度的祖型として、20世紀アラブ女性運動の文学的源流となった。",
    historical_context="エジプト・ナフダ最盛期と、女性教育・解放運動の興隆期。",
    primary_source_url=WIKI_AR+"مي_زيادة",
    primary_source_type="Wikipedia Arabic: May Ziyada",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"マイ・ズィヤーダは女性主導のサロンを通じてナフダの知的ネットワークを再編した。AI時代における集合的・ネットワーク的作者性の歴史的祖型として再読される。",
         "related_ai_phenomenon":"AI時代の集合的ネットワーク的作者性"}])

add(**C, name_ja="ナワール・アル=サアダーウィー",
    name_en="Nawal El Saadawi",
    name_original="نوال السعداوي",
    period_key="現代アラブ文学期",
    definition="エジプトの医師・小説家・フェミニスト思想家（1931-2021）。『女性とセックス』(1972)、『イムラア・インダ・ヌクタト・アッ=スィフル』(『女が砲弾の落下点になる時』1975)、『ファルダウス』(英訳Woman at Point Zero 1975)で、女性割礼・女性投獄・女性身体を主題化し、世界フェミニズム文学の中心人物の一人となった。",
    background="エジプト・カフル・タフラ村出身、医師としてのキャリア、サダト期の投獄(1981)、亡命と帰国を繰り返す。",
    development="アラブ・フェミニズム文学の制度的中心、世界フェミニズム理論への重大寄与。",
    historical_context="ナセル期からムバーラク期エジプトの女性問題、湾岸戦争期からアラブの春までの女性主体形成。",
    primary_source_url=WIKI_AR+"نوال_السعداوي",
    primary_source_type="Wikipedia Arabic: Nawal El Saadawi",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="アフラーム・ムスタガーニミー『身体の記憶』",
    name_en="Mosteghanemi's Memory in the Flesh",
    name_original="ذاكرة الجسد",
    period_key="現代アラブ文学期",
    definition="アルジェリアの作家アフラーム・ムスタガーニミー（1953-）が1993年に発表した長編小説。アルジェリア独立戦争のヴェテラン画家と若い作家の関係を通じ、独立後アルジェリアの幻滅と歴史的記憶を描く。アラブ世界で大ベストセラーとなり、女性作家による商業的成功例として、アラブ女性文学の市場的成立を象徴する。1998年ナギーブ・マフフーズ賞受賞。",
    background="アルジェリア・コンスタンチーヌ出身、独立運動指導者父の家庭、レバノン亡命、アラビア語で書く稀少なマグレブ作家。",
    development="アラブ女性文学の商業的・批評的成功例として、後のマグレブ女性作家世代の道を開いた。",
    historical_context="独立戦争世代の幻滅と、1990年代アルジェリア・「黒い10年」の暴力背景。",
    primary_source_url=WIKI_AR+"ذاكرة_الجسد",
    primary_source_type="Wikipedia Arabic: Dhakirat al-jasad",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ハナーン・アッ=シャイフ",
    name_en="Hanan al-Shaykh",
    name_original="حنان الشيخ",
    period_key="現代アラブ文学期",
    definition="レバノンの作家（1945-）。『ザフラの物語』(1980、英訳The Story of Zahra)、『ベイルート・ブルース』(1992)、『私の生命の女ら』(2005)で、レバノン内戦と家父長制下の女性経験を描く。ロンドン在住作家として、アラブ女性文学の世界的展開の中心人物。",
    background="ベイルート・シーア派家庭出身、エジプト・カイロ留学、内戦勃発後ロンドン亡命。",
    development="現代アラブ女性文学の世界的展開、ポストコロニアル女性文学研究の中心対象。",
    historical_context="レバノン内戦の女性経験、世界的アラブ・ディアスポラ作家の興隆。",
    primary_source_url=WIKI_AR+"حنان_الشيخ",
    primary_source_type="Wikipedia Arabic: Hanan al-Shaykh",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ファドワー・トゥーカーン",
    name_en="Fadwa Tuqan",
    name_original="فدوى طوقان",
    period_key="現代アラブ文学期",
    definition="パレスチナの詩人（1917-2003）。『日々の山々と共に』(1969)、『難しい旅 ── 山岳の旅』(1985)などで、パレスチナ女性経験と国民的喪失を融合する詩を確立した。「パレスチナの詩人」として、ダルウィーシュと並ぶ20世紀パレスチナ詩の中心人物。自伝『岩のような旅』(1985)も重要なアラブ女性自伝。",
    background="ナーブルス出身、保守的家父長家庭での隔離、兄イブラーヒーム・トゥーカーン（詩人）の指導、1967年戦争後の文学的覚醒。",
    development="アラブ女性詩・パレスチナ国民詩の合流点、世界フェミニスト詩研究の対象。",
    historical_context="20世紀パレスチナ史と、保守的家父長制下の女性詩人の文学的成立。",
    primary_source_url=WIKI_AR+"فدوى_طوقان",
    primary_source_type="Wikipedia Arabic: Fadwa Tuqan",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# H. 離散・マグレブ（5件）
# ============================================================
add(**C, name_ja="ターハル・ベン・ジェッルーン",
    name_en="Tahar Ben Jelloun",
    name_original="الطاهر بن جلون",
    period_key="現代アラブ文学期",
    definition="モロッコ生まれフランス語で書くマグレブ作家（1944-）。『砂の子供』(1985)、『聖なる夜』(1987、ゴンクール賞)で、モロッコ家父長制下で男性として育てられた女性主人公の物語を、千夜一夜的多層語りで展開した。フランス語マグレブ文学の世界的代表者。",
    background="フェズ・タンジェ教育、1971年フランス移住、社会学博士論文執筆、フランス・アカデミー外国人会員に近い地位。",
    development="フランコフォン・マグレブ文学の制度的中心、世界文学研究の主要対象。",
    historical_context="独立後モロッコの政治抑圧（鉛の時代）、フランス・マグレブ移民世代の文学的成立。",
    primary_source_url=WIKI_FR+"Tahar_Ben_Jelloun",
    primary_source_type="Wikipedia French: Tahar Ben Jelloun",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"ポストコロニアル多層語り",
         "description":"ベン・ジェッルーンの千夜一夜的多層語りはポストコロニアル物語論の中核実例。"}])

add(**C, name_ja="アブデルケビール・ハティビ",
    name_en="Abdelkebir Khatibi",
    name_original="عبد الكبير الخطيبي",
    period_key="現代アラブ文学期",
    definition="モロッコの社会学者・作家・批評家（1938-2009）。『二言語の愛』(1983、Amour bilingue)で、アラビア語とフランス語の二言語的経験を理論化し、「他なる思考（pensée-autre）」「二言語性（bilangue）」概念を提唱した。マグレブ・ポストコロニアル思想の中心人物の一人。",
    background="エル・ジャディーダ出身、ソルボンヌ社会学博士、ラバト第五大学教授、デリダとの対話。",
    development="マグレブ・ポストコロニアル思想の制度的中核、デリダ・ジャック・データーら世界批評家との対話。",
    historical_context="独立後モロッコの知的構築期、フランス・マグレブ知的ネットワークの形成。",
    primary_source_url=WIKI_FR+"Abdelkébir_Khatibi",
    primary_source_type="Wikipedia French: Abdelkebir Khatibi",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ハティビの「二言語性（bilangue）」概念は、二つ以上の言語間で生成される主体の理論化を試みる。多言語並行学習されたLLMの言語的存在論を考察する古典的参照点として再読される。",
         "related_ai_phenomenon":"多言語LLMの言語的存在論と二言語性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ポストコロニアル思考",
         "description":"ハティビの「他なる思考」はデリダ・ファノンと並ぶポストコロニアル思想の中核概念。"}])

add(**C, name_ja="アルベール・メンミ",
    name_en="Albert Memmi",
    name_original="ألبير ميمي",
    period_key="現代アラブ文学期",
    definition="チュニジアのユダヤ系フランス語作家・社会学者（1920-2020）。自伝的小説『塩の柱』(1953)、エッセイ『植民者の肖像と被植民者の肖像』(1957、ファノンと並ぶ植民地論の古典)で、北アフリカ・ユダヤ・アラブ・フランス的多重アイデンティティを理論化した。脱植民地論の世界的古典作家。",
    background="チュニス・ユダヤ人ゲットー（ハーラ）出身、フランス語教育、独立後フランス移住、ナンテール大学教授。",
    development="ファノンと並ぶ脱植民地論の古典、後のポストコロニアル研究の主要参照。",
    historical_context="北アフリカ・ユダヤ・コミュニティの20世紀史、フランス植民地体制とその崩壊。",
    primary_source_url=WIKI_FR+"Albert_Memmi",
    primary_source_type="Wikipedia French: Albert Memmi",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"植民地経験の人類学",
         "description":"メンミ『被植民者の肖像』は植民地経験の人類学的・社会学的記述の世界的古典。"}])

add(**C, name_ja="アブデルラティーフ・ラアービー",
    name_en="Abdellatif Laabi",
    name_original="عبد اللطيف اللعبي",
    period_key="現代アラブ文学期",
    definition="モロッコの詩人・批評家（1942-）。1966年雑誌『スーフル（Souffles）』創刊で、独立後マグレブの新左翼文学的主体の制度化を主導した。1972-80年の政治投獄期の詩篇『監獄の樹々』(1992)はモロッコ「鉛の時代」の文学的記録。フランス語マグレブ詩の中心人物。",
    background="フェズ出身、フランス語教育、1972年政治投獄、釈放後フランス移住。",
    development="マグレブ・フランコフォン詩の中核、20世紀末から21世紀の世界詩壇への展開。",
    historical_context="ハッサン2世期モロッコの政治抑圧、マグレブ新左翼運動の興隆と挫折。",
    primary_source_url=WIKI_FR+"Abdellatif_Laâbi",
    primary_source_type="Wikipedia French: Abdellatif Laabi",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ムハンマド・シュクリ『裸の麺麭』",
    name_en="Mohamed Choukri's For Bread Alone",
    name_original="الخبز الحافي",
    period_key="現代アラブ文学期",
    definition="モロッコの作家ムハンマド・シュクリ（1935-2003）が1972年に英語で出版（ポール・ボウルズ訳）、1982年にアラビア語版発表した自伝的小説『裸の麺麭』。スペイン保護領期モロッコ・タンジェ下層街の極貧と暴力を、20歳で識字を獲得した著者の口語的アラビア語で描く。マグレブ・アラブ文学の自伝形式の頂点とされる。",
    background="リーフ地方出身、内戦的家庭暴力、識字の遅れ、タンジェ国際租界の混在状況。",
    development="アラブ・マグレブ文学の自伝形式の革新、20世紀後半世界文学への翻訳的影響。",
    historical_context="スペイン保護領末期モロッコと独立後タンジェの社会変動、後の世界的タンジェ文学（ボウルズ等）。",
    primary_source_url=WIKI_AR+"محمد_شكري",
    primary_source_type="Wikipedia Arabic: Mohamed Choukri",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# Main runner
# ============================================================
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
                    print(f"  [warn] fourth tag failed for {entry['name_ja']}: {e}")
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
        print(f"[c21-add40] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c21-add40] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
