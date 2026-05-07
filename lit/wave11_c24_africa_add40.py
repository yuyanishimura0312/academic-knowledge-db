"""LIT-DB Phase 2 Wave 11 — C24 ADDITION: African Modern/Contemporary (+40 concepts).

Subfield: lit_africa (id=15), region='グローバルサウス'.

Existing 40 concepts in subfield_id=15 cover oral traditions and early
colonial-era négritude (C23). This wave ADDS 40 NEW concepts to extend the
Africa subfield into modern feminist, Lusophone, Maghrebi, Afrofuturist,
popular, children's literature, and decolonization theory.

To avoid duplication risk with the not-yet-executed wave8_c24, this wave
intentionally avoids names already targeted there (Achebe, Soyinka, Ngũgĩ
the writer (we cover his theorist-side via Mazrui/Mbembe instead), Coetzee,
Gordimer, Mia Couto, Agualusa, Adichie, Bulawayo, Mengiste, Cheikh Hamidou
Kane, Mariama Bâ, Sembène, Mongo Beti, Tahar Ben Jelloun, Bessie Head,
Mphahlele, Fugard, Brink, Aidoo, p'Bitek, Farah, Teju Cole, Habila,
Dangarembga, Owuor) and instead covers Buchi Emecheta, Florence Nwapa,
Nawal El Saadawi, Pepetela, Sony Labou Tansi, Assia Djebar, Khatibi,
Memmi, Khoury, Nnedi Okorafor, Lauren Beukes, Tade Thompson, Onitsha
market, Nairobi pulp/Spear Books, African children's literature,
decolonization theorists (Mbembe, Mudimbe, Mazrui, Cabral), among others.

40 concepts, five blocks of 8:
  A. African feminist literature (8)
  B. Lusophone Africa beyond Couto/Agualusa (8)
  C. Maghrebi literature in French and Arabic (8)
  D. Afrofuturism, African SF, and popular literature (8)
  E. Decolonization theory in literature + new voices (8)
"""
from __future__ import annotations

import sys

from lit_db_helper import LitDB, LitDBError


# ------------------------------------------------------------
# Periods (reuse existing labels if already seeded; else create)
# ------------------------------------------------------------

PERIODS = [
    ("独立後初期", "Early Post-Independence", 1960, 1980,
     "アフリカ諸国の独立直後の文学的高揚期。脱植民地化・言語論争・新しい美学の模索。"),
    ("独立後中期", "Mid Post-Independence", 1980, 2000,
     "アパルトヘイト終結（1994）・冷戦終結期の文学。ジェンダー・国民国家の幻滅・移動の主題化。"),
    ("21世紀アフリカ文学", "21st Century African Literature", 2000, 2030,
     "アフリカ系ディアスポラ作家の世界文学的台頭期。Caine Prize・Booker等を通じた国際的承認。"),
    ("マグレブ近代", "Maghreb Modern", 1950, 2010,
     "アルジェリア独立戦争前後から21世紀初頭までのマグレブ文学（仏語・アラビア語）。"),
    ("葡語圏アフリカ独立後", "Lusophone Africa Post-Independence", 1975, 2025,
     "アンゴラ・モザンビーク・カーボヴェルデ独立（1975）以降の葡語圏アフリカ文学。"),
]

REGION = "グローバルサウス"
SUBFIELD = "lit_africa"

CONCEPTS: list[dict] = []

def add(**e): CONCEPTS.append(e)


WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_PT = "https://pt.wikipedia.org/wiki/"
WIKI_AR = "https://ar.wikipedia.org/wiki/"
BRITT = "https://www.britannica.com/"
SEP = "https://plato.stanford.edu/entries/"
GUTEN = "https://www.gutenberg.org/"


C = dict(subfield_code=SUBFIELD, region=REGION)


# ============================================================
# A. アフリカ・フェミニズム文学 (8)
# ============================================================
add(**C, name_ja="フローラ・ンワパ『エフル』",
    name_en="Flora Nwapa's Efuru",
    name_original="Efuru",
    period_key="独立後初期",
    definition="ナイジェリア人作家フローラ・ンワパ（1931-1993）が1966年に発表した長編小説。Heinemann African Writers Seriesに迎えられた最初の女性作家による作品で、イボ族の女性エフルを主人公に、結婚・不妊・水の女神ウハミリへの献身を通じてイボ社会における女性の主体性を描いた。アフリカ女性による現代アフリカ文学の出発点と位置づけられる。",
    background="アチェベ『崩れゆく絆』(1958)以後の英語圏ナイジェリア小説の制度化と、女性作家の参入。",
    development="ブチ・エメチェタ、アディーチェ等のナイジェリア女性作家系譜の祖型。タナンディウェ・ニュベジ、フェミニスト批評（フロレンス・スティーディマン）の中心研究対象。",
    historical_context="ビアフラ戦争(1967-70)直前のナイジェリアにおける女性主体表象の文学化。",
    primary_source_url=WIKI_EN+"Flora_Nwapa",
    primary_source_type="Wikipedia: Flora Nwapa",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"アフリカ女性の主体表象を文学的に開いた『エフル』は、AI生成における「他者の声」を誰がどう代行するかという主体性問題の歴史的参照点。",
         "related_ai_phenomenon":"AI生成における周縁主体表象の代行可能性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"イボ女性民族誌",
         "description":"『エフル』は人類学的イボ女性民族誌（アメリカ女性人類学の1970年代諸研究）の文学的並行物として位置づけられる。"}])

add(**C, name_ja="ブチ・エメチェタ『母性の喜び』",
    name_en="Buchi Emecheta's The Joys of Motherhood",
    name_original="The Joys of Motherhood",
    period_key="独立後初期",
    definition="ナイジェリア出身英国在住作家ブチ・エメチェタ（1944-2017）が1979年に発表した長編小説。植民地期ラゴスの女性ヌヌ・エゴの生涯を、伝統的「母性の称賛」の皮肉な転倒として描く。アフリカ女性のジェンダー・経済的従属・植民地支配の交差を主題化し、第三世界フェミニズム文学の中心作として国際的に評価された。",
    background="1970年代英国における第三世界フェミニズム議論興隆と、エメチェタ自身の単親母としての英国生活経験。",
    development="チンウェイズ・オグンイェミ「マザリズム（motherism）」概念、フィレドゥウェ・スティーディマン、アメ・モフォロのアフロ・フェミニスト批評の中心対象。",
    historical_context="第二波フェミニズムへのアフリカからの応答と、ディアスポラ女性作家の制度化期。",
    primary_source_url=WIKI_EN+"The_Joys_of_Motherhood",
    primary_source_type="Wikipedia: The Joys of Motherhood",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"エメチェタはディアスポラ女性として「アフリカ女性」を代弁する位置の問題を提起する。AI時代の「誰が誰を代弁できるか」議論の文学的祖型。",
         "related_ai_phenomenon":"AI生成における代弁主体性の問題"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"第三世界フェミニズム哲学",
         "description":"エメチェタの『母性の喜び』はチャンドラ・モハンティー、グロリア・アンザルドゥア等の第三世界フェミニズム哲学の文学的対応物。"}])

add(**C, name_ja="ナワル・エル＝サアダーウィー『女性とセックス』",
    name_en="Nawal El Saadawi's Women and Sex",
    name_original="المرأة والجنس",
    original_script="arabic",
    period_key="独立後初期",
    definition="エジプト人医師・作家ナワル・エル＝サアダーウィー（1931-2021）が1972年に発表したアラビア語著作。エジプト・アラブ社会における女性の身体・性・宗教的抑圧を医学的観点と文学的観点から告発し、アラブ・フェミニズム文学の出発点となった。発表後著者は職を失い、1981年には投獄された。アフリカ・アラブ世界における女性身体の文学化の決定的契機。",
    background="サダト政権下エジプトにおける女性医学・社会運動の興隆と、保守的宗教言説への対抗。",
    development="『ゼロ度の女』(1975)、『イマームの転落』(1987)等の小説に展開、20世紀後半のアラブ・フェミニズム文学・批評の中心源流となった。",
    historical_context="1970年代エジプトの宗教保守化と、女性割礼・名誉殺人等の問題化。",
    primary_source_url=WIKI_EN+"Nawal_El_Saadawi",
    primary_source_type="Wikipedia: Nawal El Saadawi",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"エル＝サアダーウィーは女性身体を医学・文学・政治の交差として理論化した。AI時代における身体性とジェンダーのデータ化の問題へ歴史的視座を与える。",
         "related_ai_phenomenon":"AIにおける身体・ジェンダーのデータ化"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"女性身体の人類学",
         "description":"エル＝サアダーウィーは医学的身体記述と人類学的身体観察を文学的に統合し、女性身体の文化人類学（ロイス・パウル等）と並行する仕事を行った。"}])

add(**C, name_ja="アフリカ・フェミニズム文学批評",
    name_en="African feminist literary criticism",
    name_original="African feminist criticism",
    period_key="独立後中期",
    definition="1980-90年代に成立したアフリカ女性文学を対象とする批評諸潮流。チンウェイズ・オグンイェミ「マザリズム（motherism）」(1985)、フィレドゥウェ・スティーディマン「アフリカ女性とフェミニズム」(1987)、モルヒ・オゴンディポ＝レスリー「ストィウォ（stiwanism）」(1994)、オバイオマ・ナナエメカ「ネゴ・フェミニズム」(2003)など、欧米第二波フェミニズムへの批判的応答として、アフリカ独自の女性主体・共同体・母性の理論を提唱した。",
    background="1980年代アフリカ女性作家・学者の制度化と、欧米フェミニズムの普遍主義への批判。",
    development="2000年代以降のアフリカ・フェミニスト文学批評（ステファニー・ニューウェル、シナ・ニャドルコ等）に発展した。",
    historical_context="ナイロビ世界女性会議(1985)、北京会議(1995)等のグローバル女性運動の中での非西欧フェミニズム理論化期。",
    primary_source_url=WIKI_EN+"African_feminism",
    primary_source_type="Wikipedia: African feminism",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"アフリカ・フェミニズム批評は欧米の普遍主義への批判から非西欧主体性を理論化する。AIの「中立性」言説における西洋中心バイアス問題の文学批評的祖型。",
         "related_ai_phenomenon":"AIにおける普遍主義 vs 非西欧主体性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"非西欧フェミニズム哲学",
         "description":"アフリカ・フェミニズム批評はオイェロンケ・オイェウミ、サイディヤ・ハートマン等の非西欧フェミニズム哲学と理論的対応関係を持つ。"}])

add(**C, name_ja="マザリズム（motherism）",
    name_en="motherism",
    name_original="motherism",
    period_key="独立後中期",
    definition="ナイジェリアの批評家チンウェイズ・オグンイェミ（Chikwenye Okonjo Ogunyemi）が1985年論文「Womanism: The Dynamics of the Contemporary Black Female Novel in English」で提唱したアフリカ女性文学批評概念。アリス・ウォーカー「ウーマニズム（womanism）」を継承しつつ、母性・共同体・男女協調を中核とするアフリカ独自のフェミニズム思想を理論化した。アフリカ女性文学批評の基本概念の一つ。",
    background="1980年代アフリカ・カリブ海・米国黒人女性運動の交差と、アリス・ウォーカー「ウーマニズム」(1983)の影響。",
    development="アフリカ女性作家研究（モルヒ・オゴンディポ＝レスリー、オバイオマ・ナナエメカ）の理論的中核となり、2000年代以降の黒人フェミニズム哲学に継承された。",
    historical_context="冷戦末期の第三世界女性運動と、グローバル・サウスのフェミニズム理論化期。",
    primary_source_url=WIKI_EN+"Motherism",
    primary_source_type="Wikipedia: Motherism",
    importance_score=3, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ウーマニズム / 黒人フェミニズム",
         "description":"マザリズムはアリス・ウォーカー「ウーマニズム」、パトリシア・ヒル・コリンズ「黒人フェミニスト思想」と並ぶ非西欧フェミニズム哲学の中核概念。"}])

add(**C, name_ja="ストィワニズム（stiwanism）",
    name_en="stiwanism",
    name_original="STIWA / stiwanism",
    period_key="独立後中期",
    definition="ナイジェリアの批評家モルヒ・オゴンディポ＝レスリー（Molara Ogundipe-Leslie）が1994年著書『再創造を遂行する：アフリカ女性と批評的変革』で提唱した概念。STIWA = Social Transformations Including Women in Africa。アフリカ女性が直面する六重の抑圧（植民地遺産・伝統・資本主義・人種・階級・自己）を分析し、男女協働による社会変革を提唱する。アフリカ・フェミニズム批評の中心概念の一つ。",
    background="1980年代後半アフリカ女性運動の制度化と、欧米第二波フェミニズムの限界に対する応答。",
    development="2000年代以降のアフリカ女性文学批評・社会理論に継承された。",
    historical_context="ナイロビ会議(1985)以降のアフリカ女性連帯運動の理論化期。",
    primary_source_url=WIKI_EN+"Molara_Ogundipe-Leslie",
    primary_source_type="Wikipedia: Molara Ogundipe-Leslie",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ネゴ・フェミニズム",
    name_en="nego-feminism",
    name_original="nego-feminism",
    period_key="21世紀アフリカ文学",
    definition="ナイジェリアの批評家オバイオマ・ナナエメカ（Obioma Nnaemeka）が2003年論文で提唱した概念。「ネゴ」は「ネゴシエーション（交渉）」と「ノー・エゴ（自我なし）」の二重の意味を持つ。対立的・破壊的フェミニズムへの代替として、文化交渉・共有・パートナーシップを基軸とする非西欧フェミニズム実践を提唱する。21世紀アフリカ・フェミニズム理論の中心概念。",
    background="21世紀初頭グローバル・フェミニズム議論の多元化と、アフリカからの理論的応答。",
    development="2000年代以降のアフリカ女性文学批評・国際フェミニズム研究の重要枠組みとなった。",
    historical_context="ポスト冷戦期グローバルサウスのフェミニズム理論的成熟期。",
    primary_source_url=WIKI_EN+"Obioma_Nnaemeka",
    primary_source_type="Wikipedia: Obioma Nnaemeka",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="アミナタ・フォーナ",
    name_en="Aminatta Forna",
    name_original="Aminatta Forna",
    period_key="21世紀アフリカ文学",
    definition="シエラレオネ系英国人作家アミナタ・フォーナ（1964-）。回想録『悪魔は恐れていた』(2002、政治家だった父の処刑をめぐる)、長編『記憶の風景』(2010、ハロルド・ピンター賞、シエラレオネ内戦後の社会的記憶)、『ハッピネス』(2018)で知られる。21世紀アフリカ・ディアスポラ女性作家を代表する一人。心理的トラウマ・歴史的記憶・移動の交差を主題化する。",
    background="シエラレオネ内戦(1991-2002)の歴史的経験と、英国アカデミー文学制度におけるアフリカ・ディアスポラ作家の位置確立。",
    development="ノヴァイオレット・ブラワヨ、ヤァ・ジャシ、エシ・エドゥヤン等の21世紀アフリカ女性作家系譜の中心。",
    historical_context="シエラレオネ・リベリア内戦後の記憶政治と、世界文学制度におけるアフリカ女性の位置確立期。",
    primary_source_url=WIKI_EN+"Aminatta_Forna",
    primary_source_type="Wikipedia: Aminatta Forna",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# B. 葡語圏アフリカ（Couto/Agualusa以外） (8)
# ============================================================
add(**C, name_ja="ペペテーラ『マヨンベ』",
    name_en="Pepetela's Mayombe",
    name_original="Mayombe",
    period_key="葡語圏アフリカ独立後",
    definition="アンゴラ人作家ペペテーラ（Artur Carlos Maurício Pestana dos Santos、1941-）が1980年に発表した長編小説。アンゴラ独立戦争時のMPLAゲリラ部隊を描き、革命運動内部の民族・地域・階級の緊張を批判的に展開した。ペペテーラ自身がMPLAゲリラ参加者であった経験に基づき、葡語圏アフリカ独立後文学の中心作として位置づけられる。1997年カモンイス賞受賞。",
    background="アンゴラ独立戦争(1961-75)の歴史的経験と、独立後MPLA一党制下の批判的文学の制度化。",
    development="アグアルーザ、ジョゼ・エドゥアルド・アグアルーザ等のアンゴラ現代文学に系譜的影響を与えた。",
    historical_context="ポルトガル革命(1974)、アンゴラ独立(1975)後の内戦期のアンゴラ社会。",
    primary_source_url=WIKI_PT+"Mayombe",
    primary_source_type="Wikipedia (PT): Mayombe",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ペペテーラはゲリラ参加者でありながら革命を内側から批判する作家像を確立した。AI時代における当事者性と批判性の関係を再考する歴史的事例。",
         "related_ai_phenomenon":"AI時代の当事者性と批判性"}])

add(**C, name_ja="ジョゼ・クラヴェイリーニャ",
    name_en="José Craveirinha",
    name_original="José Craveirinha",
    period_key="葡語圏アフリカ独立後",
    definition="モザンビーク人詩人ジョゼ・クラヴェイリーニャ（1922-2003）。詩集『シゲンバ』(1964)、『ストッペル氏の死』(1979)等で、植民地期モザンビーク社会の人種的抑圧と独立闘争を、ロンガ語・ロンゲ語の韻律を葡語に融合する独自の詩学で展開した。1991年カモンイス賞（葡語圏文学最高賞）をアフリカ人として初受賞。葡語圏アフリカ文学の詩的中核。",
    background="ポルトガル植民地期モザンビーク社会のアフリカ人ジャーナリズムと、ネグリチュード詩学の葡語圏受容。",
    development="ミア・コウト、パウリーナ・チジアネ等のモザンビーク現代文学に直接影響を与えた。",
    historical_context="モザンビーク独立戦争(1964-74)期の文化的抵抗運動の中心人物。",
    primary_source_url=WIKI_PT+"José_Craveirinha",
    primary_source_type="Wikipedia (PT): José Craveirinha",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="パウリーナ・チジアネ",
    name_en="Paulina Chiziane",
    name_original="Paulina Chiziane",
    period_key="葡語圏アフリカ独立後",
    definition="モザンビーク人作家パウリーナ・チジアネ（1955-）。葡語圏アフリカで最初の女性長編小説作家とされる。代表作『複婚の風』(2002)、『ニケトチェ：愛の物語』(2002)で、モザンビーク南部の女性のジェンダー・複婚・伝統と近代の交差を、口承詩学を組み込んだ葡語散文で展開した。2021年カモンイス賞受賞。葡語圏アフリカ女性文学の中心。",
    background="独立後モザンビークの女性作家制度化と、口承伝統と書記文学の融合の探求。",
    development="ミア・コウト、ウンガリーニャ・バーリ等の葡語圏アフリカ現代文学に並行する重要作家。",
    historical_context="モザンビーク内戦(1977-92)後の和解期と、女性主体の文学化。",
    primary_source_url=WIKI_PT+"Paulina_Chiziane",
    primary_source_type="Wikipedia (PT): Paulina Chiziane",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ボアヴェントゥラ・カルドーゾ",
    name_en="Boaventura Cardoso",
    name_original="Boaventura Cardoso",
    period_key="葡語圏アフリカ独立後",
    definition="アンゴラ人作家ボアヴェントゥラ・カルドーゾ（1944-）。短編集『Dizanga dia Muenhu』(1977)、『O Fogo da Fala』(1980)、長編『Maio, mês de Maria』(1997)で、キンブンドゥ語・ウンブンドゥ語の口承表現を葡語小説に組み込み、アンゴラ独自の「クレオール散文」を確立した。葡語圏アフリカの言語的多層性の文学化に決定的貢献。",
    background="アンゴラ独立後の言語政策論議（葡語と土着諸言語の関係）と、土着言語表現の文学化の探求。",
    development="ミア・コウト『毎人は人種なり』、アグアルーザの言語実験に直接影響を与えた葡語圏アフリカ言語的革新の祖型。",
    historical_context="独立後アンゴラの文化的アイデンティティ模索期。",
    primary_source_url=WIKI_PT+"Boaventura_Cardoso",
    primary_source_type="Wikipedia (PT): Boaventura Cardoso",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ジェルマーノ・アルメイダ",
    name_en="Germano Almeida",
    name_original="Germano Almeida",
    period_key="葡語圏アフリカ独立後",
    definition="カーボヴェルデ人作家ジェルマーノ・アルメイダ（1945-）。代表作『ナポムセノ・ダ・シルヴァ・アラウージョ氏の遺言』(1989)で、カーボヴェルデの島嶼社会の家族・遺産・道徳の皮肉な構造を、独特のユーモアと観察眼で描いた。2018年カモンイス賞受賞。カーボヴェルデ近代文学の世界的代表者。",
    background="カーボヴェルデ独立(1975)後の島嶼文学制度化と、土着クレオール語と葡語の関係の文学化。",
    development="カーボヴェルデ現代散文の規範形式を確立し、葡語圏の世界文学的拡張に貢献した。",
    historical_context="独立後カーボヴェルデの社会変動と、ディアスポラ社会との関係。",
    primary_source_url=WIKI_PT+"Germano_Almeida",
    primary_source_type="Wikipedia (PT): Germano Almeida",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ンゴンガ・ナリーニャ",
    name_en="Ungulani Ba Ka Khosa",
    name_original="Ungulani Ba Ka Khosa",
    period_key="葡語圏アフリカ独立後",
    definition="モザンビーク人作家ウンガリーニャ・バー・カ・コーザ（Francisco Esaú Cossa、1957-）。代表作『ウアラランガ』(1987)で、モザンビーク北部マラヴィ族のシャカ王国移動の歴史を、口承伝説と歴史小説手法で展開した。葡語圏アフリカにおける歴史小説・口承文学融合の代表作。",
    background="モザンビーク独立後の歴史的アイデンティティ模索期と、口承歴史伝統の文学化。",
    development="モザンビーク現代文学（コウト、チジアネ）と並行する歴史的記憶の文学的探求。",
    historical_context="モザンビーク内戦期(1977-92)の文化的回復運動。",
    primary_source_url=WIKI_PT+"Ungulani_Ba_Ka_Khosa",
    primary_source_type="Wikipedia (PT): Ungulani Ba Ka Khosa",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="ソニー・ラブー・タンシ",
    name_en="Sony Labou Tansi",
    name_original="Sony Labou Tansi",
    period_key="独立後中期",
    definition="コンゴ共和国人作家ソニー・ラブー・タンシ（Marcel Ntsoni、1947-1995）。長編『一人半の生』(1979)、『七つの寂しさ』(1985)、『反人民の状態』(1981)で、ザイール・モブツ独裁を寓意化した独裁者批判文学を、グロテスクで言語破壊的なフランス語で展開した。葡語圏アグアルーザと並ぶ「アフリカ・マジック・リアリズム」の代表者。",
    background="モブツ独裁下中部アフリカの政治的閉塞と、ガルシア・マルケス的マジック・リアリズムのアフリカ受容。",
    development="アグアルーザ、コウト、ラブダニ等のアフリカ・マジック・リアリズム作家系譜の中心。",
    historical_context="1970-90年代中部アフリカの独裁政権下の文学的抵抗。",
    primary_source_url=WIKI_FR+"Sony_Labou_Tansi",
    primary_source_type="Wikipedia (FR): Sony Labou Tansi",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"マジック・リアリズム",
         "description":"ラブー・タンシのアフリカ・マジック・リアリズムはガルシア・マルケス系譜とアフリカ口承伝統の融合として、世界マジック・リアリズム研究の中心対象。"}])

add(**C, name_ja="アンゴラ独立戦争詩",
    name_en="Angolan independence war poetry",
    name_original="poesia da luta angolana",
    period_key="葡語圏アフリカ独立後",
    definition="アンゴラ独立戦争(1961-75)期に成立した詩的運動。アゴスティーニョ・ネト（後初代大統領、1922-79）『神聖な希望』(1974、ロータス文学賞)、アントニオ・ジャシント、アグスティーニョ・メンデス・デ・カルヴァーリョ等を代表する。アンゴラ独立闘争のイデオロギー的・文化的中核を成し、葡語圏アフリカ「闘争詩」の規範を確立した。",
    background="MPLA独立闘争のイデオロギー的・文化的動員と、ネグリチュード詩学の葡語圏受容。",
    development="独立後アンゴラ国民文化の象徴的源流として継承され、ペペテーラ等のアンゴラ近代散文への前提条件となった。",
    historical_context="ポルトガル植民地末期(1961-74)のアンゴラ抵抗運動と、独立闘争の文化動員。",
    primary_source_url=WIKI_PT+"Agostinho_Neto",
    primary_source_type="Wikipedia (PT): Agostinho Neto",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# C. マグレブ文学（仏語・アラビア語） (8)
# ============================================================
add(**C, name_ja="アシア・ジェバール『部屋の中のアルジェの女たち』",
    name_en="Assia Djebar's Femmes d'Alger dans leur appartement",
    name_original="Femmes d'Alger dans leur appartement",
    period_key="マグレブ近代",
    definition="アルジェリア人作家アシア・ジェバール（Fatima-Zohra Imalayène、1936-2015）が1980年に発表した短編集。ドラクロワの絵画『アルジェの女たち』(1834)を起点に、独立後アルジェリアの女性の語り・身体・記憶を多層的に展開した。1996年ヌースタッド国際文学賞、2005年フランス・アカデミー会員選出（マグレブ出身者初）。マグレブ女性文学の世界的代表者。",
    background="アルジェリア独立戦争(1954-62)後の女性の地位後退と、ジェバール自身のアルジェリア・ベルベル系女性史研究。",
    development="20世紀末-21世紀初頭のマグレブ女性文学（マレク・アルーラ、レイラ・スリマニ等）に決定的影響を与えた。",
    historical_context="1980年代アルジェリアの宗教保守化と、女性身体・記憶の文学的回復運動。",
    primary_source_url=WIKI_FR+"Assia_Djebar",
    primary_source_type="Wikipedia (FR): Assia Djebar",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ジェバールはアルジェリア女性の声を歴史・絵画・口承の交差から立ち上げた。AI生成における周縁主体の声の構築可能性に対する文学的挑戦。",
         "related_ai_phenomenon":"AI生成における周縁主体の声"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"オリエンタリズム表象批判",
         "description":"ジェバールのドラクロワ絵画への応答はサイード『オリエンタリズム』と並ぶ植民地表象批判の代表的実践。"}])

add(**C, name_ja="アブデルケビール・ハティビ",
    name_en="Abdelkébir Khatibi",
    name_original="Abdelkébir Khatibi",
    period_key="マグレブ近代",
    definition="モロッコ人作家・思想家アブデルケビール・ハティビ（1938-2009）。『二言語のラブストーリー』(1983)、『刺青された記憶』(1971)、『マグレブ複数性』(1983)で、アラビア語・フランス語・ベルベル語の交差をハティビ独自の「他言語愛（amour bilingue）」「複数アイデンティティ」概念として理論化した。マグレブ・ポストコロニアル思想の世界的代表者。",
    background="フランス植民地期モロッコ生まれのマグレブ・バイリンガル世代の経験と、デリダ脱構築の受容。",
    development="ジャック・デリダとの友情を通じて、ヨーロッパ・ポストコロニアル思想に直接影響を与えた。エドゥアール・グリッサン「クレオール化」概念とも理論的並行関係。",
    historical_context="独立後モロッコのアイデンティティ論議と、20世紀後半マグレブ思想の世界的展開期。",
    primary_source_url=WIKI_FR+"Abdelkébir_Khatibi",
    primary_source_type="Wikipedia (FR): Abdelkébir Khatibi",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ハティビの「他言語愛」概念は複数言語間の主体性を理論化する。LLMの多言語処理における「言語間の主体性」問題の哲学的祖型。",
         "related_ai_phenomenon":"多言語LLMにおける言語間主体性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"複数性の哲学",
         "description":"ハティビの「複数アイデンティティ」概念はデリダ、グリッサン、エドワード・サイードと並ぶポストコロニアル思想の中心源流。"}])

add(**C, name_ja="アルベール・メミ『植民者の肖像』",
    name_en="Albert Memmi's Portrait du colonisé",
    name_original="Portrait du colonisé, précédé du portrait du colonisateur",
    period_key="マグレブ近代",
    definition="チュニジア出身フランス在住作家アルベール・メミ（1920-2020）が1957年に発表したエッセイ。植民者と被植民者の心理的・社会的関係を双方の側から構造的に分析し、植民地状況の心理人類学的解剖を試みた。ジャン＝ポール・サルトルの序文を伴って刊行され、フランツ・ファノン『黒い皮膚、白い仮面』『地に呪われたる者』と並ぶ脱植民地化思想の古典となった。",
    background="チュニジア・ユダヤ人共同体出身というメミの三重周縁性（アラブ社会内ユダヤ人、フランス植民地下、独立後マグレブ）。",
    development="フランツ・ファノン、エドワード・サイード、ホミ・バーバ等のポストコロニアル理論に直接影響を与えた。",
    historical_context="アルジェリア独立戦争初期(1954-)、チュニジア独立(1956)直後の脱植民地化思想形成期。",
    primary_source_url=WIKI_FR+"Albert_Memmi",
    primary_source_type="Wikipedia (FR): Albert Memmi",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"メミは植民者・被植民者の主体構造を相補的に分析した。AI開発者と利用者・データ提供者の関係性を植民地的構造として再考する基盤。",
         "related_ai_phenomenon":"AI開発者-利用者関係の植民地論的読解"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"植民地心理学",
         "description":"メミの植民者-被植民者構造分析は、ファノン、サルトル、サイードと並ぶ植民地心理学・ポストコロニアル思想の古典。"}])

add(**C, name_ja="ターハル・ウェター",
    name_en="Tahar Ouettar",
    name_original="الطاهر وطار",
    original_script="arabic",
    period_key="マグレブ近代",
    definition="アルジェリア人アラビア語作家ターハル・ウェター（1936-2010）。『ロバ』(1974)、『ジハードを呼ぶ者』(1980)、『恋』(1981)等で、アルジェリア独立戦争・社会主義建設・宗教保守化の各段階のアルジェリア社会をアラビア語小説で描き、フランス語マグレブ文学（ジェバール、カテブ）と並ぶアラビア語マグレブ文学の中心作家となった。",
    background="アルジェリア独立後のアラビア語化政策と、フランス語文学に対するアラビア語文学の制度確立。",
    development="20世紀後半マグレブ・アラビア語文学の規範形式を確立し、後のアラブ世界アラビア語小説に系譜的影響を与えた。",
    historical_context="独立後アルジェリアのアラビア語化政策論議と、社会主義期から自由化期にかけての社会変動。",
    primary_source_url=WIKI_AR+"الطاهر_وطار",
    primary_source_type="Wikipedia (AR): Tahar Ouettar",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="カテブ・ヤシン『ネジマ』",
    name_en="Kateb Yacine's Nedjma",
    name_original="Nedjma",
    period_key="マグレブ近代",
    definition="アルジェリア人作家カテブ・ヤシン（1929-1989）が1956年に発表した長編小説。アルジェリア独立戦争初期に刊行され、四人の青年がネジマという女性を中心に旋回する非線形構造で、植民地末期アルジェリアの集合的主体性を表現した。フォークナー『響きと怒り』に比較される実験的構造を持ち、マグレブ近代小説の決定的傑作とされる。",
    background="アルジェリア・セティフ虐殺(1945)経験と、フランス・モダニズム小説（フォークナー、ジョイス）の影響。",
    development="マグレブ近代フランス語文学（ジェバール、ハティビ、ベン・ジェルーン）の方法的祖型となった。",
    historical_context="アルジェリア独立戦争初期(1954-62)の文化的中心作品。",
    primary_source_url=WIKI_FR+"Nedjma_(roman)",
    primary_source_type="Wikipedia (FR): Nedjma (roman)",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ナギーブ・マフフーズ『カイロ三部作』",
    name_en="Naguib Mahfouz's Cairo Trilogy",
    name_original="ثلاثية القاهرة",
    original_script="arabic",
    period_key="独立後初期",
    definition="エジプト人作家ナギーブ・マフフーズ（1911-2006）が1956-57年に発表した三部作（『二宮殿通り』『欲望宮殿』『砂糖通り』）。1917年から1944年までのカイロのアブド・アル・ジャワード家三世代を中軸に、エジプト近代化・独立運動・宗教保守化・世俗化を統合的に描いた。1988年アラビア語作家として最初のノーベル文学賞受賞。アラブ近代小説の頂点。",
    background="エジプト独立期(1922-)、ナセル革命(1952)前夜のエジプト社会と、ヨーロッパ近代小説（バルザック、トルストイ）のアラブ世界受容。",
    development="20世紀後半アラブ世界全体の近代小説の規範形式となり、世界文学的承認を獲得した。",
    historical_context="エジプト・アラブ世界の近代化・独立・社会変動の文学的総合。",
    primary_source_url=WIKI_EN+"Cairo_Trilogy",
    primary_source_type="Wikipedia: Cairo Trilogy",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"アラブ家族民族誌",
         "description":"マフフーズ三部作はカイロ・ブルジョワ家族の三世代描写として、20世紀中葉のアラブ家族民族誌の文学的並行物。"}])

add(**C, name_ja="エリアス・コーリィ『太陽の門』",
    name_en="Elias Khoury's Bab al-Shams",
    name_original="باب الشمس",
    original_script="arabic",
    period_key="独立後中期",
    definition="レバノン人作家エリアス・コーリィ（1948-2024）が1998年に発表した長編小説。1948年ナクバ（パレスチナ大破滅）以降のパレスチナ難民の物語を、語りが語りを生む千夜一夜物語的構造で展開した。アラブ世界における「ナクバ文学」の頂点として国際的に評価され、ホアン・ゴイティソロら世界文学者から最高評価を得た。",
    background="ナクバ50周年(1998)前後のパレスチナ記憶政治と、アラビア語小説のポストモダン的革新。",
    development="ガッサーン・カナファーニー以降のパレスチナ・アラブ文学の世界的展開を象徴し、21世紀アラビア語文学の中心作となった。",
    historical_context="オスロ合意(1993)後のパレスチナ・イスラエル関係の文学的応答。",
    primary_source_url=WIKI_EN+"Bab_al-Shams",
    primary_source_type="Wikipedia: Bab al-Shams",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アシア・ジェバール『アルジェリア白書』",
    name_en="Assia Djebar's Le Blanc de l'Algérie",
    name_original="Le Blanc de l'Algérie",
    period_key="マグレブ近代",
    definition="ジェバールが1995年に発表したエッセイ＝小説的散文。1990年代アルジェリア内戦期に暗殺された友人作家・知識人（ジャン・センナック、マウルード・フェラウン、カテブ・ヤシン等）への弔辞として書かれ、アラビア語・フランス語・ベルベル語の重層的記憶を「白の余白」として展開した。アルジェリア内戦期の暴力の文学化として、20世紀末マグレブ文学の中心作。",
    background="アルジェリア内戦(1991-2002)の知識人暗殺と、亡命生活下のジェバールの記憶政治。",
    development="ジェバール自身の自伝的三部作の中心作品となり、20世紀末マグレブ知識人記憶文学の規範となった。",
    historical_context="アルジェリア内戦下の知識人弾圧と、亡命作家による記憶の文学化。",
    primary_source_url=WIKI_FR+"Assia_Djebar",
    primary_source_type="Wikipedia (FR): Assia Djebar (Le Blanc)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# D. アフロフューチャリズム・SF・大衆文学 (8)
# ============================================================
add(**C, name_ja="ンネディ・オコラフォー",
    name_en="Nnedi Okorafor",
    name_original="Nnedi Okorafor",
    period_key="21世紀アフリカ文学",
    definition="ナイジェリア系米国人作家ンネディ・オコラフォー（1974-）。長編『誰が死を恐れるか』(2010、世界幻想文学大賞)、『ラグーン』(2014)、ビンティ三部作(2015-18、ヒューゴー賞・ネビュラ賞)で、アフリカ未来主義（Africanfuturism）を確立した。マーベル『シュリ』コミック原作も担当。21世紀アフリカSFの世界的代表者。",
    background="2000年代以降のアフロフューチャリズム概念興隆と、アフリカ系ディアスポラ作家のSF制度化。",
    development="トミ・アデイェミ、タデ・トンプソン等のアフリカSF作家系譜の中心。Marvel『ブラックパンサー』映画文化現象とも交差。",
    historical_context="2010年代の世界文学・大衆文化におけるアフリカ未来表象の制度化期。",
    primary_source_url=WIKI_EN+"Nnedi_Okorafor",
    primary_source_type="Wikipedia: Nnedi Okorafor",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"オコラフォーはアフリカ未来主義として既存SF（白人中心）の物語規範を脱構築する。AI生成における物語構造の文化的偏向問題に対する文学的応答。",
         "related_ai_phenomenon":"AI生成物語の文化的偏向と多様化"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"アフロフューチャリズム",
         "description":"オコラフォーのアフリカ未来主義はマーク・デリー命名のアフロフューチャリズム（1993）と並ぶ、ディアスポラ未来文化の文学的中核。"}])

add(**C, name_ja="アフロフューチャリズム",
    name_en="Afrofuturism",
    name_original="Afrofuturism",
    period_key="21世紀アフリカ文学",
    definition="マーク・デリーが1993年論文「Black to the Future」で命名した、黒人ディアスポラの未来表象を中核とする美学・文化運動。サン・ラ、ジョージ・クリントン（音楽）、サミュエル・R・ディレイニー、オクテイヴィア・バトラー（SF）に源流を持ち、2010年代以降ンネディ・オコラフォー、N・K・ジェミシン等のアフリカ系作家、映画『ブラックパンサー』(2018)を通じて世界的注目を獲得した。",
    background="20世紀後半の黒人ディアスポラ文化（音楽・SF・視覚芸術）の累積と、21世紀デジタル文化における黒人未来表象の制度化。",
    development="アフリカ未来主義（オコラフォー、エマイサル・サリエ）と区別されつつ、21世紀グローバル黒人文化運動の中核となった。",
    historical_context="ポスト9.11米国の人種問題と、デジタル時代の黒人文化運動の交差。",
    primary_source_url=WIKI_EN+"Afrofuturism",
    primary_source_type="Wikipedia: Afrofuturism",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"アフロフューチャリズムは未来表象の人種的多元化を達成する文化運動。AI生成における未来表象の文化的偏向問題への対抗運動の文学的祖型。",
         "related_ai_phenomenon":"AI生成における未来表象の人種的偏向"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"アフロフューチャリズムの作者性は集合的・離散的であり、AI生成における集合的作者性の文化的祖型を提供する。",
         "related_ai_phenomenon":"AI生成における集合的・離散的作者性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"未来の脱植民地化",
         "description":"アフロフューチャリズムはアシール・ムベンベ「アフリカ未来」、ウォルター・ミニョーロ「脱植民地化」と並ぶ未来表象の脱西欧化思想。"}])

add(**C, name_ja="ローレン・ボイケス『ザ・シャイニング・ガールズ』",
    name_en="Lauren Beukes's The Shining Girls",
    name_original="The Shining Girls",
    period_key="21世紀アフリカ文学",
    definition="南アフリカ人作家ローレン・ボイケス（1976-）が2013年に発表したスリラー長編小説。時間旅行する連続殺人犯と被害者の追跡を、20世紀シカゴの社会階層変動を背景に展開した。『Zoo City』(2010、アーサー・C・クラーク賞)で確立したアフリカSF/スリラー手法を世界市場に展開し、21世紀南アフリカ大衆文学の世界的代表となった。",
    background="2000年代以降の南アフリカ・ジャンル文学制度化と、世界市場における非西欧大衆文学の需要拡大。",
    development="南アフリカ・ディーオン・メイヤー（クライム）、デオン・マイヤー（スリラー）と並ぶ南アフリカ・ジャンル文学の中心。",
    historical_context="ポストアパルトヘイト南アフリカの大衆文学制度化と国際進出期。",
    primary_source_url=WIKI_EN+"Lauren_Beukes",
    primary_source_type="Wikipedia: Lauren Beukes",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="タデ・トンプソン『ロザリオ』三部作",
    name_en="Tade Thompson's Wormwood Trilogy",
    name_original="Rosewater Trilogy",
    period_key="21世紀アフリカ文学",
    definition="ナイジェリア系英国人作家タデ・トンプソン（1972-）が2016-19年に発表したSF三部作。エイリアン降臨後のナイジェリア・ロザリオを舞台に、テレパシー・バイオパンク・植民地遺産を結合した独自のアフリカSFを展開した。第1部『ロザリオ』(2016)はアーサー・C・クラーク賞受賞。21世紀アフリカSFの代表作の一つ。",
    background="2010年代アフリカ系ディアスポラSF作家の制度化と、英米SF出版界における非西欧SFの需要拡大。",
    development="ンネディ・オコラフォー、トミ・アデイェミ、エマイサル・サリエ等のアフリカSF作家系譜の中心。",
    historical_context="2010-20年代世界SF制度におけるアフリカSFの躍進期。",
    primary_source_url=WIKI_EN+"Tade_Thompson",
    primary_source_type="Wikipedia: Tade Thompson",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="オニチャ市場文学（後期）",
    name_en="Onitsha market literature (later phase)",
    name_original="Onitsha market literature",
    period_key="独立後初期",
    definition="ナイジェリア・オニチャ市場で1947年以降発行された大衆文学群。安価な小冊子として、英語・ピジン英語による道徳教育・恋愛・実業助言を扱った。1960-70年代独立後にも継続し、ナイジェリア大衆文化と都市読書市場の中核を成した。サイプリアン・エクウェンシ、オグウィ・ウバなど後の正典作家の出発点となり、近年「アフリカ大衆文学」研究（ステファニー・ニューウェル等）の中心対象。",
    background="独立後ナイジェリアの識字率拡大と、都市労働者向け安価な読み物市場の興隆。",
    development="ハウサ語『カノ印刷文学（Soyayya小説）』、ナイロビSpear Books等のアフリカ大衆文学諸潮流と並行する。",
    historical_context="1960-70年代ナイジェリア社会の都市化・教育拡大期。",
    primary_source_url=WIKI_EN+"Onitsha_Market_Literature",
    primary_source_type="Wikipedia: Onitsha Market Literature",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ナイロビ大衆文学（Spear Books）",
    name_en="Nairobi popular literature (Spear Books)",
    name_original="Spear Books / Heinemann Kenya",
    period_key="独立後中期",
    definition="ケニア・ハイネマン社が1975年から発行した大衆文学叢書「Spear Books」を中核とする東アフリカ大衆文学群。デヴィッド・マイランギ『あなたが死ぬとき』、メジャ・ムワンギ『カラを下りて』(1976)、サム・カヘイガ等を代表とする。スリラー・恋愛・社会風刺を中心に、ケニア・タンザニアの都市読者市場を形成し、21世紀アフリカ大衆文学研究の中心対象となった。",
    background="独立後ケニアの教育拡大と、ハイネマン社のアフリカ大衆文学市場開拓戦略。",
    development="メジャ・ムワンギは後により正典的作家として再評価され、ナイロビ大衆文学は21世紀アフリカ大衆文化研究の中心対象となった。",
    historical_context="1970-90年代東アフリカの都市文化形成期。",
    primary_source_url=WIKI_EN+"Meja_Mwangi",
    primary_source_type="Wikipedia: Meja Mwangi / Spear Books",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="ハウサ語ソヤッヤ小説（Kano印刷後期）",
    name_en="Hausa Soyayya novels",
    name_original="Soyayya / soyayyar Hausa",
    period_key="独立後中期",
    definition="北部ナイジェリア・カノを中心に1980年代以降発展したハウサ語大衆恋愛小説群（「ソヤッヤ」=「愛」）。バルキス・ガダンヤ、ヘリーナ・タッカイ、ザヤナブ・アラワ・スルー等の女性作家を中核とし、ハウサ・ムスリム女性の結婚・教育・宗教の交差を扱う。アフリカ語土着文学の現代的展開として、ステファニー・ニューウェル等のアフリカ大衆文学研究の中心対象となった。",
    background="独立後北部ナイジェリアのハウサ語識字拡大と、女性読者・作者市場の拡大。",
    development="2000年代以降のハウサ映画（Kannywood）の物語的源泉ともなり、北部ナイジェリア大衆文化の中核を成した。",
    historical_context="北部ナイジェリアの宗教保守化・シャリーア法導入(2000-)期と、女性公共圏の拡大の緊張。",
    primary_source_url=WIKI_EN+"Soyayya",
    primary_source_type="Wikipedia: Soyayya",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ムスリム女性公共圏",
         "description":"ソヤッヤ小説は北部ナイジェリア・ムスリム女性の文学的公共圏を成し、ムスリム女性民族誌（ステファニー・ニューウェル等）と並行する。"}])

add(**C, name_ja="アフリカ児童文学",
    name_en="African children's literature",
    name_original="African children's literature",
    period_key="独立後中期",
    definition="独立後アフリカ諸国で展開した児童文学運動。ナイジェリアのチヌア・アチェベ『チケと川』(1966)、ガーナのメシャック・アサーレ『太鼓を売った少年』(1981、ノマ賞)、ケニアのメジャ・ムワンギ『リトル・ホワイト・マン』、東南部アフリカのChimwemwe Undi等が代表的。植民地教育で押しつけられた英語・フランス語の児童書（『不思議の国のアリス』等）への対抗として、土着的・現代的児童物語を確立した。",
    background="独立後アフリカ諸国の教育制度確立と、欧米児童文学への文化的応答。",
    development="21世紀のアフリカ系ディアスポラ児童文学（クリストファー・マイヤー、ジュリー・フリン等）に継承された。",
    historical_context="1970-90年代アフリカ諸国の教育拡大と、文化的アイデンティティ形成のための児童文学化。",
    primary_source_url=WIKI_EN+"African_children%27s_literature",
    primary_source_type="Wikipedia: African children's literature",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"児童期の人類学",
         "description":"アフリカ児童文学は児童期の人類学的研究（マーガレット・ミード以降）と並行する文化的児童期構築の文学的形式。"}])


# ============================================================
# E. 脱植民地化理論と新しい声 (8)
# ============================================================
add(**C, name_ja="アシール・ムベンベ『ポストコロニーについて』",
    name_en="Achille Mbembe's On the Postcolony",
    name_original="De la postcolonie",
    period_key="独立後中期",
    definition="カメルーン人哲学者アシール・ムベンベ（1957-）が2000年に発表した著作。独立後アフリカの政治的・象徴的構造を「グロテスクの審美学」「権力の親密性」「死後の生」等の独自概念で分析し、21世紀アフリカ・ポストコロニアル思想の中心作となった。文学的散文と政治分析の融合は、サイード『オリエンタリズム』、ファノン『地に呪われたる者』と並ぶ脱植民地化思想の世界的影響力を獲得した。",
    background="1990年代アフリカ諸国の民主化挫折と、ポストコロニアル理論のアフリカ的展開の必要性。",
    development="ムベンベ『黒人理性批判』(2013)、『野蛮主義』(2020)等に展開し、世界ポストコロニアル思想の中心源流となった。",
    historical_context="冷戦終結後アフリカの「失敗国家」言説と、それへの哲学的応答。",
    primary_source_url=WIKI_EN+"Achille_Mbembe",
    primary_source_type="Wikipedia: Achille Mbembe",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ムベンベの「権力の親密性」概念は、AI時代の主体・権力関係（プラットフォーム資本主義における主体形成）を再考する哲学的祖型。",
         "related_ai_phenomenon":"AIプラットフォームにおける権力の親密性"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"ムベンベの脱植民地化思想は、AI時代における知識生産の脱西欧化問題への基盤を提供する。",
         "related_ai_phenomenon":"AI知識生産の脱西欧化"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ポストコロニアル哲学",
         "description":"ムベンベはサイード、スピヴァク、バーバと並ぶ21世紀ポストコロニアル哲学の中心人物。"}])

add(**C, name_ja="V・Y・ムディンベ『アフリカの発明』",
    name_en="V. Y. Mudimbe's The Invention of Africa",
    name_original="The Invention of Africa",
    period_key="独立後中期",
    definition="コンゴ民主共和国出身の哲学者V・Y・ムディンベ（1941-2024）が1988年に発表した著作。「アフリカ」概念そのものが西欧植民地的言説の構築物であることを、フーコー的言説分析手法で明らかにした。サイード『オリエンタリズム』のアフリカ版として国際的に評価され、ポストコロニアル理論・アフリカ哲学・アフリカ文学批評の交差点に位置する。",
    background="フーコー言説分析の影響と、1980年代アフリカ・ポストコロニアル思想の哲学的成熟。",
    development="ムディンベ『土着の知識、土着の権力』(1991)等に展開し、21世紀のアフリカ哲学・アフリカ文学批評（ムベンベ、ニアミ・ヌクワビ）の中心源流となった。",
    historical_context="冷戦末期アフリカ知識人の理論的世界進出期。",
    primary_source_url=WIKI_EN+"V._Y._Mudimbe",
    primary_source_type="Wikipedia: V. Y. Mudimbe",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ムディンベは「アフリカ」概念そのものが西欧言説の構築物であることを示した。AI生成における地理的・文化的概念の言説的構築の哲学的祖型。",
         "related_ai_phenomenon":"AI生成における文化概念の言説的構築"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"アフリカ哲学・言説分析",
         "description":"ムディンベはアフリカ哲学とフーコー言説分析を結合した、20世紀後半アフリカ思想の中心人物。"}])

add(**C, name_ja="アリ・マズルイ『アフリカ：トリプル・ヘリテージ』",
    name_en="Ali Mazrui's The Africans: A Triple Heritage",
    name_original="The Africans: A Triple Heritage",
    period_key="独立後中期",
    definition="ケニア出身の政治学者・思想家アリ・マズルイ（1933-2014）が1986年に発表した著作（およびBBCドキュメンタリー）。アフリカが「土着・イスラーム・西欧キリスト教」の三重遺産の交差として構成されているという文化哲学を提唱した。アフリカ思想の世界的普及に決定的影響を与え、21世紀アフリカ・アイデンティティ論の基本枠組みとなった。",
    background="冷戦末期アフリカ知識人のグローバル進出と、汎アフリカ思想の20世紀総括。",
    development="マズルイ『アフリカン・コンディション』(1980)等に展開し、21世紀アフリカ思想・文学批評の前提条件となった。",
    historical_context="1980年代アフリカ諸国の経済危機（構造調整プログラム）期と、汎アフリカ思想の再構築。",
    primary_source_url=WIKI_EN+"Ali_Mazrui",
    primary_source_type="Wikipedia: Ali Mazrui",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"トリプル・ヘリテージ",
         "description":"マズルイの三重遺産論は20世紀末アフリカ文化人類学の基本枠組みとなった。"}])

add(**C, name_ja="アミルカル・カブラル",
    name_en="Amílcar Cabral",
    name_original="Amílcar Cabral",
    period_key="独立後初期",
    definition="ギニアビサウ・カーボヴェルデの革命家・思想家アミルカル・カブラル（1924-1973）。PAIGC（独立闘争組織）指導者として、また文化理論家として、エッセイ集『国民解放と文化』(1970)、『闘争の武器としての国民文化』等を発表した。「文化への回帰」概念で、植民地化されたアフリカの文化的回復が政治闘争と不可分であることを理論化し、葡語圏アフリカ思想・世界脱植民地化思想に決定的影響を与えた。1973年暗殺。",
    background="ポルトガル植民地ギニアビサウ・カーボヴェルデの独立闘争(1956-74)と、ファノン的脱植民地化思想の葡語圏受容。",
    development="ファノン、エメ・セゼール、サミール・アミンと並ぶ20世紀脱植民地化思想の中心人物。",
    historical_context="1960-70年代アフリカ・ポルトガル植民地の独立闘争期。",
    primary_source_url=WIKI_EN+"Amílcar_Cabral",
    primary_source_type="Wikipedia: Amílcar Cabral",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"脱植民地化哲学",
         "description":"カブラルはファノン、セゼール、ンクルマと並ぶアフリカ脱植民地化哲学の中心源流。"}])

add(**C, name_ja="ンギュギ・ワ・ティオンゴ「文化のリ・センタリング」",
    name_en="Ngũgĩ wa Thiong'o's recentering culture",
    name_original="Moving the Centre",
    period_key="独立後中期",
    definition="ンギュギ・ワ・ティオンゴが1993年エッセイ集『中心を動かす（Moving the Centre）』で展開した文化理論。20世紀後半における世界文学・知識生産の中心がヨーロッパからグローバルな多中心構造へと移行する過程を理論化し、アフリカ文学・非西欧文学の制度化を歴史哲学的に位置づけた。21世紀世界文学制度の理論的前提条件。",
    background="20世紀末グローバル化の中での非西欧文学の制度化と、世界文学概念の理論化期。",
    development="パスカル・カザノヴァ『世界文学の共和国』(1999)、フランコ・モレッティ等の世界文学理論に系譜的影響を与えた。",
    historical_context="冷戦末期からグローバル化期にかけての世界文学制度の再編期。",
    primary_source_url=WIKI_EN+"Ngũgĩ_wa_Thiong%27o",
    primary_source_type="Wikipedia: Ngũgĩ wa Thiong'o",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ンギュギの「中心の移動」概念は、AI生成における文化的中心バイアスの問題（学習データの西欧中心性）への理論的応答の祖型。",
         "related_ai_phenomenon":"AI生成における文化的中心バイアス"}])

add(**C, name_ja="ベン・オクリ『飢えた道』",
    name_en="Ben Okri's The Famished Road",
    name_original="The Famished Road",
    period_key="独立後中期",
    definition="ナイジェリア系英国人作家ベン・オクリ（1959-）が1991年に発表した長編小説。1991年ブッカー賞受賞（最年少受賞者の一人）。ヨルバ伝説の「アビク（dying-and-returning child）」アザロを語り手に、独立後ナイジェリアの社会変動を生死の境界を交差する幻視的散文で描いた。アフリカ・マジック・リアリズムの世界文学的代表作。",
    background="1980-90年代英国出版界のアフリカ文学受容拡大と、マジック・リアリズム（ガルシア・マルケス）のアフリカ的応用。",
    development="ソニー・ラブー・タンシ、ミア・コウト、アグアルーザと並ぶアフリカ・マジック・リアリズム潮流の中心。",
    historical_context="1990年代世界文学制度におけるアフリカ・ディアスポラ文学の制度化。",
    primary_source_url=WIKI_EN+"The_Famished_Road",
    primary_source_type="Wikipedia: The Famished Road",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"アビク信仰",
         "description":"オクリの小説中心概念「アビク」はヨルバ宗教の死と再生を繰り返す子の信仰であり、人類学的ヨルバ宗教研究と直接結合する。"}])

add(**C, name_ja="ザケス・ムダ『赤の心』",
    name_en="Zakes Mda's The Heart of Redness",
    name_original="The Heart of Redness",
    period_key="21世紀アフリカ文学",
    definition="南アフリカ人作家ザケス・ムダ（1948-）が2000年に発表した長編小説。19世紀コーサ族の予言者ノングワウセによる「牛の屠殺」(1856-57、コーサ族集団自殺事件)を、ポストアパルトヘイト現代と重層化させて描いた。ポストアパルトヘイト南アフリカ文学の中心作の一つで、ムダはクッツェー、ゴーディマー以後の世代を代表する作家として国際的評価を確立した。",
    background="ポストアパルトヘイト南アフリカの歴史的記憶政治と、コーサ族口承伝統の文学化。",
    development="ダンガレンガ、ニャマンジョ、ニュンギ等のポストアパルトヘイト南アフリカ女性・若手作家系譜への前提条件。",
    historical_context="真実和解委員会(1996-98)後の南アフリカの記憶政治期。",
    primary_source_url=WIKI_EN+"Zakes_Mda",
    primary_source_type="Wikipedia: Zakes Mda",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="イヴォンヌ・ヴェラ",
    name_en="Yvonne Vera",
    name_original="Yvonne Vera",
    period_key="独立後中期",
    definition="ジンバブエ人女性作家イヴォンヌ・ヴェラ（1964-2005）。長編『燃え盛る蝶』(1998、コモンウェルス賞)、『地下から』(1996)、『恥辱』(2002)で、ジンバブエ社会における女性の身体・暴力・記憶を、詩的散文で展開した。アフリカ女性作家の中で最も詩的に革新的な散文家とされ、ダンガレンガ、ノヴァイオレット・ブラワヨ等のジンバブエ女性作家系譜の中核となった。",
    background="ジンバブエ独立(1980)後の女性作家制度化と、ショナ族口承伝統の散文化。",
    development="21世紀ジンバブエ女性作家（ペティナ・ガッパ、ノヴァイオレット・ブラワヨ）の方法的祖型。",
    historical_context="独立後ジンバブエの社会変動と、ムガベ政権下の文化的緊張。",
    primary_source_url=WIKI_EN+"Yvonne_Vera",
    primary_source_type="Wikipedia: Yvonne Vera",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region=REGION,
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid

        for raw in CONCEPTS:
            entry = dict(raw)
            entry.setdefault("original_script", "roman")
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
        print(f"[wave11_c24] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave11_c24] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
