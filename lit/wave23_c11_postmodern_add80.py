"""LIT-DB Phase 2 Wave 23 — C11: Western Postmodern EXTENSION (+80 concepts).

Subfield: lit_eu_postmodern (id=7), region='西欧'.

Adds 80 NEW NON-OVERLAPPING concepts (target 280, route to 500) covering:
  T: Theoretical postmodern framework (Lyotard / Baudrillard / Jameson /
     Hutcheon / McHale / Hassan / Richardson / Ryan / Perloff / Bernstein) (16)
  A: American postmodern compounding (Pynchon late + Barth essays + Coover
     fairy-tale + Hawkes early + Gass essays + DeLillo middle/late) (18)
  B: British postmodern (Carter / Ackroyd / Byatt / McEwan / Ishiguro /
     Banville / Smith Ali / Mitchell / Self / Welsh) (20)
  C: Continental postmodern (Eco / Calvino / Sebald / Kundera / Houellebecq /
     Modiano / Saramago / Krasznahorkai) (26)

Definitions <150 chars. Mostly secondary (living authors); ~30% primary
(Eco's Open Work, Hawkes's Cannibal, Coover's Pricksongs etc. via PD essays
or canonical academic editions are tagged primary where direct citation).
fourth_transform_tags >= 24, cross_domain >= 18.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("ポストモダン期", "Postmodern Era", 1960, 2000,
     "1960年代以降の西欧文学において、メタフィクション・断片化・パスティーシュ・ハイパーリアリティを中核に、近代的物語・主体・正典を相対化した時代。"),
    ("自伝的現代期", "Contemporary Autofictional Era", 1990, 2025,
     "セバルド以降の記憶文学からKnausgård以降の自伝小説の世界的隆盛までの、ポストモダン以後の現代文学期。"),
    ("ポスト・ポストモダン期", "Post-Postmodern Era", 2000, 2025,
     "ポストモダンへの反動として新誠実派・メタモダニズム・人新世文学・AI時代の小説形式が並走する21世紀現代文学期。"),
]


WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_IT = "https://it.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WIKI_PT = "https://pt.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
BRITT = "https://www.britannica.com/"
JSTOR = "https://www.jstor.org/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_eu_postmodern", region="西欧", original_script="roman")


# ============================================================
# T: Theoretical postmodern framework (16)
# ============================================================
add(**C, name_ja="リオタール『ポストモダンの条件』",
    name_en="Lyotard's The Postmodern Condition",
    name_original="La condition postmoderne",
    period_key="ポストモダン期",
    definition="ジャン=フランソワ・リオタールが1979年に発表した知識報告書。「大きな物語への不信」をポストモダンの条件と定式化した規範書。",
    background="1970年代後期資本主義における知識の正統化危機への哲学的応答。",
    development="ハッチオン、ジェイムソン、マクヘイルの理論構築の基盤となった。",
    historical_context="1980年代世界における知識正統化危機の理論的基盤。",
    primary_source_url=SEP+"lyotard/",
    primary_source_type="SEP: Lyotard",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="リオタール『争異』",
    name_en="Lyotard's The Differend",
    name_original="Le différend",
    period_key="ポストモダン期",
    definition="リオタールが1983年に発表した哲学書。共通言語不在の係争状態「差異」を主題化、ポストモダン倫理学の規範作。",
    background="アウシュヴィッツ証言不可能性問題への哲学的応答。",
    development="ホロコースト後文学・証言文学理論の基礎概念。",
    historical_context="1980年代ホロコースト記憶論議の哲学的反映。",
    primary_source_url=SEP+"lyotard/",
    primary_source_type="SEP: Lyotard",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ボードリヤール『シミュラークルとシミュレーション』",
    name_en="Baudrillard's Simulacra and Simulation",
    name_original="Simulacres et simulation",
    period_key="ポストモダン期",
    definition="ジャン・ボードリヤールが1981年に発表した哲学書。ハイパーリアリティ・シミュラークル四段階を提示した規範作。",
    background="後期資本主義メディア環境におけるリアリティ消失への応答。",
    development="ピンチョン・デリーロ・ウォシャウスキー姉妹『マトリックス』の理論基盤。",
    historical_context="1980年代メディア飽和社会の理論的基盤。",
    primary_source_url=SEP+"baudrillard/",
    primary_source_type="SEP: Baudrillard",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ボードリヤール『消費社会の神話と構造』",
    name_en="Baudrillard's The Consumer Society",
    name_original="La société de consommation",
    period_key="ポストモダン期",
    definition="ボードリヤールが1970年に発表した社会理論書。記号的消費・象徴的価値による主体構成を分析した規範作。",
    background="戦後フランス消費社会の急速な拡大への社会学的応答。",
    development="デリーロ『ホワイト・ノイズ』、ウェルシュ『トレインスポッティング』の理論的基盤。",
    historical_context="1970年代消費資本主義への文学的応答の理論基盤。",
    primary_source_url=BRITT+"biography/Jean-Baudrillard",
    primary_source_type="Britannica: Baudrillard",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ボードリヤール『アメリカ』",
    name_en="Baudrillard's America",
    name_original="Amérique",
    period_key="ポストモダン期",
    definition="ボードリヤールが1986年に発表した旅行記=哲学。アメリカをハイパーリアリティの実現体として読み解く規範作。",
    background="1980年代レーガン期米国の象徴的飽和への哲学的応答。",
    development="米国ポストモダン文学の自己理解に直接影響。",
    historical_context="1980年代米国象徴政治の理論的反映。",
    primary_source_url=WIKI_EN+"America_(Baudrillard_book)",
    primary_source_type="Wikipedia: America (Baudrillard)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ジェイムソン『単一近代性』",
    name_en="Jameson's A Singular Modernity",
    name_original="A Singular Modernity",
    period_key="ポスト・ポストモダン期",
    definition="フレドリック・ジェイムソンが2002年に発表した理論書。近代性概念の単独性とポストモダン以降の時代意識を再考。",
    background="ポストモダン論議の収束期における近代性概念再考の必要。",
    development="21世紀現代性理論の基盤テクストとなった。",
    historical_context="2000年代近代性論議の理論的反映。",
    primary_source_url=BRITT+"biography/Fredric-Jameson",
    primary_source_type="Britannica: Jameson",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ジェイムソン『リアリズムの二律背反』",
    name_en="Jameson's The Antinomies of Realism",
    name_original="The Antinomies of Realism",
    period_key="ポスト・ポストモダン期",
    definition="ジェイムソンが2013年に発表した理論書。19世紀リアリズムの内的矛盾を「物語」と「情動」の対立として再解釈。",
    background="ポストモダン以後の小説理論再構築への要請。",
    development="現代リアリズム回帰論議の理論的基盤。",
    historical_context="2010年代リアリズム再評価論議の反映。",
    primary_source_url=BRITT+"biography/Fredric-Jameson",
    primary_source_type="Britannica: Jameson",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ハッチオン『ポストモダニズムの詩学』",
    name_en="Hutcheon's A Poetics of Postmodernism",
    name_original="A Poetics of Postmodernism",
    period_key="ポストモダン期",
    definition="リンダ・ハッチオンが1988年に発表した理論書。「歴史記述的メタフィクション」を中核概念に据えたポストモダン詩学の規範作。",
    background="1980年代ポストモダン文学の理論的体系化への要請。",
    development="ポストモダン文学批評の標準テクストとなった。",
    historical_context="1980年代後期文学理論の集大成。",
    primary_source_url=BRITT+"biography/Linda-Hutcheon",
    primary_source_type="Britannica: Hutcheon",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ハッチオン『パロディの理論』",
    name_en="Hutcheon's A Theory of Parody",
    name_original="A Theory of Parody",
    period_key="ポストモダン期",
    definition="ハッチオンが1985年に発表した理論書。パロディを差異を伴う反復として再定義、ポストモダン規範作。",
    background="20世紀芸術における引用・反復構造の理論化要請。",
    development="ポストモダン芸術理論の中核テクストとなった。",
    historical_context="1980年代芸術理論の体系化期。",
    primary_source_url=BRITT+"biography/Linda-Hutcheon",
    primary_source_type="Britannica: Hutcheon",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハッチオン『アイロニーの剣先』",
    name_en="Hutcheon's Irony's Edge",
    name_original="Irony's Edge",
    period_key="ポストモダン期",
    definition="ハッチオンが1994年に発表したアイロニー論。アイロニーの政治的・社会的機能を分析した規範作。",
    background="1990年代アイデンティティ政治とアイロニーの関係再考。",
    development="現代アイロニー研究の基盤テクスト。",
    historical_context="1990年代文化政治学の理論的基盤。",
    primary_source_url=BRITT+"biography/Linda-Hutcheon",
    primary_source_type="Britannica: Hutcheon",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="マクヘイル『ポストモダニスト・フィクション構築』",
    name_en="McHale's Constructing Postmodernism",
    name_original="Constructing Postmodernism",
    period_key="ポストモダン期",
    definition="ブライアン・マクヘイルが1992年に発表した続編理論書。ポストモダン小説の存在論的支配を構造的に分析した規範作。",
    background="1980年代ポストモダン批評の理論的精緻化要請。",
    development="マクヘイル『ケンブリッジ・ポストモダニズム入門』へと展開。",
    historical_context="1990年代ポストモダン批評の集大成期。",
    primary_source_url=BRITT+"art/postmodernism-philosophy",
    primary_source_type="Britannica: Postmodernism",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ハッサン『オルフェウスの解体』",
    name_en="Hassan's The Dismemberment of Orpheus",
    name_original="The Dismemberment of Orpheus",
    period_key="ポストモダン期",
    definition="イハブ・ハッサンが1971年に発表した理論書。ポストモダン文学の規範をモダニズム/ポストモダンの二元表で示した先駆作。",
    background="1960年代米国ポストモダン文学の理論化先駆。",
    development="ポストモダン文学批評の祖型テクストとなった。",
    historical_context="1970年代米国文学理論の祖型。",
    primary_source_url=BRITT+"art/postmodernism-philosophy",
    primary_source_type="Britannica: Postmodernism",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ブライアン・リチャードソン『非自然な語り』",
    name_en="Richardson's Unnatural Narrative",
    name_original="Unnatural Narrative",
    period_key="ポスト・ポストモダン期",
    definition="ブライアン・リチャードソンが2015年に発表したナラトロジー書。ポストモダン非自然語りの理論的体系化。",
    background="21世紀ナラトロジーにおけるポストモダン技法再評価。",
    development="現代非自然ナラトロジー学派の規範テクスト。",
    historical_context="2010年代物語論再構築期の反映。",
    primary_source_url=BRITT+"art/narrative",
    primary_source_type="Britannica: Narrative",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="マリ=ロール・ライアン『可能世界』",
    name_en="Ryan's Possible Worlds",
    name_original="Possible Worlds, Artificial Intelligence and Narrative Theory",
    period_key="ポストモダン期",
    definition="マリ=ロール・ライアンが1991年に発表した理論書。可能世界論をナラトロジーに導入した規範作。",
    background="様相論理学のナラトロジーへの応用要請。",
    development="ライアン『ナラティブ・ゲーム研究』へと展開し電子文学理論に。",
    historical_context="1990年代物語論・AI論議の交差期反映。",
    primary_source_url=BRITT+"art/possible-worlds",
    primary_source_type="Britannica: Possible Worlds",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="マージョリー・ペルロフ『ラディカル・アーティフィス』",
    name_en="Perloff's Radical Artifice",
    name_original="Radical Artifice",
    period_key="ポストモダン期",
    definition="マージョリー・ペルロフが1991年に発表した詩論書。メディア時代の詩的人工性を主題化した規範作。",
    background="1990年代メディア飽和環境における詩の存在意義の問い直し。",
    development="ペルロフ『21世紀モダニズム』『ディファレンシャル』へと展開。",
    historical_context="1990年代詩学のメディア論的展開反映。",
    primary_source_url=BRITT+"biography/Marjorie-Perloff",
    primary_source_type="Britannica: Perloff",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="チャールズ・バーンスタイン『コンテンツの夢』",
    name_en="Bernstein's Content's Dream",
    name_original="Content's Dream: Essays 1975-1984",
    period_key="ポストモダン期",
    definition="チャールズ・バーンスタインが1986年に発表したエッセイ集。L=A=N=G=U=A=G=E派ポストモダン詩学の規範書。",
    background="1980年代米国実験詩運動の理論化要請。",
    development="米国ポストモダン詩学の中核テクストとなった。",
    historical_context="1980年代米国実験詩運動の理論的基盤。",
    primary_source_url=BRITT+"biography/Charles-Bernstein",
    primary_source_type="Britannica: Bernstein",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# A: American postmodern compounding (18)
# ============================================================
add(**C, name_ja="ピンチョン『ヴァインランド』",
    name_en="Pynchon's Vineland",
    name_original="Vineland",
    period_key="ポストモダン期",
    definition="ピンチョンが1990年に発表した長編小説。1960年代対抗文化敗北の余波と1980年代レーガン期米国を交差させる規範作。",
    background="レーガン期米国における60年代対抗文化記憶の文学化。",
    development="ピンチョン後期作品の起点となった。",
    historical_context="1980年代後半米国の政治記憶論議。",
    primary_source_url=BRITT+"topic/Vineland",
    primary_source_type="Britannica: Vineland",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ピンチョン『LAヴァイス』",
    name_en="Pynchon's Inherent Vice",
    name_original="Inherent Vice",
    period_key="ポストモダン期",
    definition="ピンチョンが2009年に発表した長編小説。1970年LAの私立探偵ドックを主役にしたポストモダン・ノワールの規範作。",
    background="2000年代米国における60-70年代記憶のノスタルジア化。",
    development="ポストモダン・ノワール・ジャンルの規範作となった。",
    historical_context="2000年代米国の対抗文化記憶論議反映。",
    primary_source_url=BRITT+"topic/Inherent-Vice",
    primary_source_type="Britannica: Inherent Vice",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ピンチョン『スロー・ラーナー』",
    name_en="Pynchon's Slow Learner",
    name_original="Slow Learner",
    period_key="ポストモダン期",
    definition="ピンチョンが1984年に発表した初期短編集。長文の自伝的序文付き、ピンチョン自身の作家論を含む規範作。",
    background="ピンチョン研究のための作者自身による作品解説要請。",
    development="ピンチョン批評史の参照テクストとなった。",
    historical_context="1980年代米国ポストモダン作家批評の集約期。",
    primary_source_url=BRITT+"biography/Thomas-Pynchon",
    primary_source_type="Britannica: Pynchon",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="バース『ジャイルズ・山羊少年』",
    name_en="Barth's Giles Goat-Boy",
    name_original="Giles Goat-Boy",
    period_key="ポストモダン期",
    definition="ジョン・バースが1966年に発表した寓意長編小説。大学=世界の寓意で英雄神話を再構築した米国ポストモダン規範作。",
    background="1960年代冷戦期大学世界の文学的寓意化要請。",
    development="バース・ポストモダン寓意小説の祖型となった。",
    historical_context="1960年代米国大学制度批判の文学的反映。",
    primary_source_url=BRITT+"biography/John-Barth",
    primary_source_type="Britannica: John Barth",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="バース『金曜日の本』",
    name_en="Barth's The Friday Book",
    name_original="The Friday Book",
    period_key="ポストモダン期",
    definition="バースが1984年に発表したエッセイ集。「補充の文学」「枯渇の文学」など米国ポストモダン論の規範論文を含む。",
    background="米国ポストモダン文学運動の理論的自己認識要請。",
    development="米国ポストモダン理論の中核エッセイ集となった。",
    historical_context="1980年代米国文学批評の自己理論化期。",
    primary_source_url=BRITT+"biography/John-Barth",
    primary_source_type="Britannica: John Barth",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クーヴァー『公衆熱浴場の女中』",
    name_en="Coover's Spanking the Maid",
    name_original="Spanking the Maid",
    period_key="ポストモダン期",
    definition="ロバート・クーヴァーが1981年に発表した短編。同一場面の反復変奏というポストモダン技法の規範作。",
    background="ヌーヴォー・ロマン反復技法の米国継承。",
    development="米国ポストモダン反復構造短編の規範となった。",
    historical_context="1980年代米国実験短編の集約期。",
    primary_source_url=BRITT+"biography/Robert-Coover",
    primary_source_type="Britannica: Coover",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="クーヴァー『ジョンの妻』",
    name_en="Coover's John's Wife",
    name_original="John's Wife",
    period_key="ポストモダン期",
    definition="クーヴァーが1996年に発表した長編小説。米国小都市の見えない中心人物をめぐる視点群の交錯を描いた規範作。",
    background="1990年代米国郊外文学の脱構築的継承。",
    development="クーヴァー後期米国郊外ポストモダン小説の規範となった。",
    historical_context="1990年代米国郊外文学論議反映。",
    primary_source_url=BRITT+"biography/Robert-Coover",
    primary_source_type="Britannica: Coover",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="クーヴァー『茨姫』",
    name_en="Coover's Briar Rose",
    name_original="Briar Rose",
    period_key="ポストモダン期",
    definition="クーヴァーが1996年に発表した短編。眠れる森の美女童話を分解再構成したポストモダン童話書き換えの規範作。",
    background="ポストモダン童話書き換え運動の代表的試み。",
    development="現代童話書き換え小説の規範作となった。",
    historical_context="1990年代童話再評価運動の文学的反映。",
    primary_source_url=BRITT+"biography/Robert-Coover",
    primary_source_type="Britannica: Coover",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ホークス『カニバル』",
    name_en="Hawkes's The Cannibal",
    name_original="The Cannibal",
    period_key="ポストモダン期",
    definition="ジョン・ホークスが1949年に発表したデビュー長編。戦後ドイツの黙示録的暴力を描いた米国ポストモダン先駆作。",
    background="第二次大戦直後の暴力記憶の文学的反映。",
    development="米国ポストモダン暴力小説の祖型となった。",
    historical_context="1940年代後半米国における戦後暴力論の文学化。",
    primary_source_url=BRITT+"biography/John-Hawkes",
    primary_source_type="Britannica: John Hawkes",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ホークス『ライム・ツイッグ』",
    name_en="Hawkes's The Lime Twig",
    name_original="The Lime Twig",
    period_key="ポストモダン期",
    definition="ホークスが1961年に発表した長編。英国競馬詐欺をめぐる悪夢的構造を描いた米国ポストモダン規範作。",
    background="戦後英国を米国作家が描く視座のポストモダン的提示。",
    development="ホークス中期作品の代表となった。",
    historical_context="1960年代米国ポストモダン文学運動の中心期。",
    primary_source_url=BRITT+"biography/John-Hawkes",
    primary_source_type="Britannica: John Hawkes",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ホークス『セカンド・スキン』",
    name_en="Hawkes's Second Skin",
    name_original="Second Skin",
    period_key="ポストモダン期",
    definition="ホークスが1964年に発表した長編。海軍士官スキッパーの遍歴を非線形に描いた米国ポストモダン規範作。",
    background="1960年代米国ポストモダン手法の到達点。",
    development="ホークス代表作として米国ポストモダン批評の中心テクストに。",
    historical_context="1960年代米国実験小説運動の中心期。",
    primary_source_url=BRITT+"biography/John-Hawkes",
    primary_source_type="Britannica: John Hawkes",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ガス『オーメンセッターの運』",
    name_en="Gass's Omensetter's Luck",
    name_original="Omensetter's Luck",
    period_key="ポストモダン期",
    definition="ウィリアム・ガスが1966年に発表したデビュー長編。19世紀オハイオ州の宗教共同体を文体実験で描いた米国ポストモダン規範作。",
    background="1960年代米国ポストモダン文体実験運動の中心期。",
    development="ガス『トンネル』へと続く文体実験小説の起点。",
    historical_context="1960年代米国実験小説運動の集約期。",
    primary_source_url=BRITT+"biography/William-H-Gass",
    primary_source_type="Britannica: Gass",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ガス『ウィリー・マスターズの孤独な妻』",
    name_en="Gass's Willie Masters' Lonesome Wife",
    name_original="Willie Masters' Lonesome Wife",
    period_key="ポストモダン期",
    definition="ガスが1968年に発表した実験中編。タイポグラフィー・写真・書物物質性を駆使した米国ポストモダン視覚実験規範作。",
    background="1960年代タイポグラフィー実験文学の代表。",
    development="現代視覚文学・電子文学の祖型となった。",
    historical_context="1960年代後半米国実験文学の到達点。",
    primary_source_url=BRITT+"biography/William-H-Gass",
    primary_source_type="Britannica: Gass",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ガス『言葉の住処』",
    name_en="Gass's Habitations of the Word",
    name_original="Habitations of the Word",
    period_key="ポストモダン期",
    definition="ガスが1985年に発表したエッセイ集。文体・形式・言語の物質性を主題化した米国ポストモダン詩学規範書。",
    background="米国ポストモダン作家による批評理論化の代表例。",
    development="ガス批評理論の集大成となった。",
    historical_context="1980年代米国作家批評の集約期。",
    primary_source_url=BRITT+"biography/William-H-Gass",
    primary_source_type="Britannica: Gass",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="デリーロ『リブラ』",
    name_en="DeLillo's Libra",
    name_original="Libra",
    period_key="ポストモダン期",
    definition="ドン・デリーロが1988年に発表した長編。リー・ハーヴェイ・オズワルドの内面からケネディ暗殺を再構築した米国ポストモダン歴史記述的メタフィクション規範作。",
    background="1980年代米国ケネディ暗殺記憶論議の文学化。",
    development="現代米国歴史記述的メタフィクションの規範となった。",
    historical_context="1980年代米国の歴史記憶政治論議反映。",
    primary_source_url=BRITT+"topic/Libra-novel-by-DeLillo",
    primary_source_type="Britannica: Libra",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="デリーロ『マオII』",
    name_en="DeLillo's Mao II",
    name_original="Mao II",
    period_key="ポストモダン期",
    definition="デリーロが1991年に発表した長編。引退作家ビル・グレイとテロリズム時代の作家像を主題化した米国ポストモダン規範作。",
    background="冷戦終結期テロリズム時代の作家論の文学化。",
    development="9.11以降のテロ文学論議の理論的先駆となった。",
    historical_context="1990年代米国テロリズム論議の文学的反映。",
    primary_source_url=BRITT+"topic/Mao-II",
    primary_source_type="Britannica: Mao II",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="デリーロ『フォーリング・マン』",
    name_en="DeLillo's Falling Man",
    name_original="Falling Man",
    period_key="ポスト・ポストモダン期",
    definition="デリーロが2007年に発表した長編。9.11後のNYで生き延びた弁護士の家族を描いた米国ポスト・ポストモダン規範作。",
    background="2000年代米国における9.11記憶の文学的応答。",
    development="現代米国テロ後文学の規範となった。",
    historical_context="2000年代米国の9.11記憶論議反映。",
    primary_source_url=BRITT+"topic/Falling-Man",
    primary_source_type="Britannica: Falling Man",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="デリーロ『沈黙』",
    name_en="DeLillo's The Silence",
    name_original="The Silence",
    period_key="ポスト・ポストモダン期",
    definition="デリーロが2020年に発表した中編。デジタル崩壊後の世界でNYアパートに集まる人々の沈黙を描いた米国ポスト・ポストモダン後期作。",
    background="2020年代米国におけるデジタル文明依存への文学的応答。",
    development="デリーロ後期極小化スタイルの到達点となった。",
    historical_context="2020年代米国のデジタル文明論議反映。",
    primary_source_url=BRITT+"biography/Don-DeLillo",
    primary_source_type="Britannica: DeLillo",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# B: British postmodern (20)
# ============================================================
add(**C, name_ja="カーター『マジック・トイショップ』",
    name_en="Carter's The Magic Toyshop",
    name_original="The Magic Toyshop",
    period_key="ポストモダン期",
    definition="アンジェラ・カーターが1967年に発表した長編。孤児メラニーが叔父の人形店で出会う暗黒童話世界を描いた英国ポストモダン規範作。",
    background="1960年代英国童話書き換え運動の起点。",
    development="カーター英国フェミニスト・ポストモダンの規範となった。",
    historical_context="1960年代英国ジェンダー論議の文学的反映。",
    primary_source_url=BRITT+"biography/Angela-Carter",
    primary_source_type="Britannica: Carter",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="カーター『英雄たちと悪役たち』",
    name_en="Carter's Heroes and Villains",
    name_original="Heroes and Villains",
    period_key="ポストモダン期",
    definition="カーターが1969年に発表した長編。核戦争後の世界で「教授たち」と「野蛮人」の対立を描いた英国ポストモダン・ディストピア規範作。",
    background="1960年代英国核戦争不安の文学的反映。",
    development="現代ディストピア・フェミニズム小説の祖型となった。",
    historical_context="1960年代後半英国のディストピア論議反映。",
    primary_source_url=BRITT+"biography/Angela-Carter",
    primary_source_type="Britannica: Carter",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="カーター『新しいイヴの受難』",
    name_en="Carter's The Passion of New Eve",
    name_original="The Passion of New Eve",
    period_key="ポストモダン期",
    definition="カーターが1977年に発表した長編。男性主人公が女性に変身させられる近未来NYの寓意を描いた英国フェミニスト・ポストモダン規範作。",
    background="1970年代英国第二波フェミニズムの文学的応答。",
    development="現代ジェンダー・パフォーマティヴィティ理論の文学的先駆。",
    historical_context="1970年代英国フェミニズム論議反映。",
    primary_source_url=BRITT+"biography/Angela-Carter",
    primary_source_type="Britannica: Carter",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="カーター『サド的女性』",
    name_en="Carter's The Sadeian Woman",
    name_original="The Sadeian Woman",
    period_key="ポストモダン期",
    definition="カーターが1979年に発表したフェミニズム文化論。サド侯爵を女性視点から再読した英国ポストモダン論争書。",
    background="1970年代英国フェミニズム論議のサド再評価期。",
    development="現代フェミニズム文化論議の中核テクストとなった。",
    historical_context="1970年代英国第二波フェミニズム理論の文学的反映。",
    primary_source_url=BRITT+"biography/Angela-Carter",
    primary_source_type="Britannica: Carter",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="アクロイド『チャタトン』",
    name_en="Ackroyd's Chatterton",
    name_original="Chatterton",
    period_key="ポストモダン期",
    definition="ピーター・アクロイドが1987年に発表した長編。18世紀詩人チャタトンの偽造をめぐる三層時代交錯を描いた英国歴史記述的メタフィクション規範作。",
    background="1980年代英国における歴史的記憶・偽造論議の文学化。",
    development="現代英国歴史記述的メタフィクションの規範となった。",
    historical_context="1980年代英国歴史的記憶論議反映。",
    primary_source_url=BRITT+"biography/Peter-Ackroyd",
    primary_source_type="Britannica: Ackroyd",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アクロイド『ディケンズ伝』",
    name_en="Ackroyd's Dickens",
    name_original="Dickens",
    period_key="ポストモダン期",
    definition="アクロイドが1990年に発表した1100頁の伝記。著者がディケンズと対話する自伝的章を含む英国伝記=メタフィクションの規範作。",
    background="1990年代英国伝記実験運動の代表的試み。",
    development="現代伝記=メタフィクション・ジャンルの規範となった。",
    historical_context="1990年代英国実験伝記運動反映。",
    primary_source_url=BRITT+"biography/Peter-Ackroyd",
    primary_source_type="Britannica: Ackroyd",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="アクロイド『ロンドン:伝記』",
    name_en="Ackroyd's London: The Biography",
    name_original="London: The Biography",
    period_key="ポスト・ポストモダン期",
    definition="アクロイドが2000年に発表した900頁の都市伝記。ロンドンを生きた人格として描いた英国都市ポストモダン規範作。",
    background="2000年代英国における都市記憶論議の集大成。",
    development="現代都市=人格論小説・伝記の規範となった。",
    historical_context="2000年代英国都市記憶論議反映。",
    primary_source_url=BRITT+"biography/Peter-Ackroyd",
    primary_source_type="Britannica: Ackroyd",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="バイアット『フレデリカ四部作』",
    name_en="Byatt's Frederica Quartet",
    name_original="The Virgin in the Garden / Still Life / Babel Tower / A Whistling Woman",
    period_key="ポストモダン期",
    definition="A.S.バイアットが1978-2002年に発表した四部作。英国知識人女性フレデリカの30年を描いた英国ポストモダン教養小説の規範作。",
    background="戦後英国知識人女性経験の長期文学化要請。",
    development="現代英国知識人女性教養小説の規範となった。",
    historical_context="戦後英国知識階級女性史の文学的反映。",
    primary_source_url=BRITT+"biography/AS-Byatt",
    primary_source_type="Britannica: Byatt",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="バイアット『子どもの本』",
    name_en="Byatt's The Children's Book",
    name_original="The Children's Book",
    period_key="ポスト・ポストモダン期",
    definition="バイアットが2009年に発表した長編。19世紀末から第一次大戦までの英国芸術家コミュニティを描いた英国歴史記述的メタフィクション規範作。",
    background="2000年代英国フィン・ド・シエクル再評価期。",
    development="現代英国エドワード期歴史小説の規範となった。",
    historical_context="2000年代英国歴史記憶論議反映。",
    primary_source_url=BRITT+"biography/AS-Byatt",
    primary_source_type="Britannica: Byatt",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="マキューアン『土曜日』",
    name_en="McEwan's Saturday",
    name_original="Saturday",
    period_key="ポスト・ポストモダン期",
    definition="イアン・マキューアンが2005年に発表した長編。イラク戦争反対デモの2003年2月15日のロンドンで脳神経外科医ペロウンの一日を描いた英国ポスト・ポストモダン規範作。",
    background="2000年代イラク戦争期英国の社会的緊張の文学化。",
    development="現代英国「24時間小説」の規範となった。",
    historical_context="2000年代英国イラク戦争論議反映。",
    primary_source_url=BRITT+"topic/Saturday-novel-by-McEwan",
    primary_source_type="Britannica: Saturday",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マキューアン『チェジル・ビーチにて』",
    name_en="McEwan's On Chesil Beach",
    name_original="On Chesil Beach",
    period_key="ポスト・ポストモダン期",
    definition="マキューアンが2007年に発表した中編。1962年の新婚カップルの一晩を描いた英国ポスト・ポストモダン規範作。",
    background="2000年代英国60年代記憶論議の文学的応答。",
    development="現代英国極小スケール・ポスト・ポストモダン小説の規範となった。",
    historical_context="2000年代英国60年代記憶論議反映。",
    primary_source_url=BRITT+"biography/Ian-McEwan",
    primary_source_type="Britannica: McEwan",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="マキューアン『黒い犬』",
    name_en="McEwan's Black Dogs",
    name_original="Black Dogs",
    period_key="ポストモダン期",
    definition="マキューアンが1992年に発表した長編。ベルリンの壁崩壊期の家族記憶を描いた英国ポストモダン記憶小説規範作。",
    background="1990年代初頭英国における冷戦終結記憶論議の文学化。",
    development="マキューアン中期の代表作となった。",
    historical_context="1990年代英国冷戦終結記憶論議反映。",
    primary_source_url=BRITT+"biography/Ian-McEwan",
    primary_source_type="Britannica: McEwan",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="イシグロ『充たされざる者』",
    name_en="Ishiguro's The Unconsoled",
    name_original="The Unconsoled",
    period_key="ポストモダン期",
    definition="カズオ・イシグロが1995年に発表した500頁の長編。中欧の街でピアニスト・ライダーが体験する夢のような時間を描いた英国ポストモダン規範作。",
    background="1990年代英国実験小説運動の代表作。",
    development="現代英国「夢の論理」小説の規範となった。",
    historical_context="1990年代英国実験文学論議反映。",
    primary_source_url=BRITT+"biography/Kazuo-Ishiguro",
    primary_source_type="Britannica: Ishiguro",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="イシグロ『忘れられた巨人』",
    name_en="Ishiguro's The Buried Giant",
    name_original="The Buried Giant",
    period_key="ポスト・ポストモダン期",
    definition="イシグロが2015年に発表した長編。中世アーサー王時代の英国を舞台に、忘却の霧に覆われた老夫婦の旅を描いた英国ポスト・ポストモダン規範作。",
    background="2010年代英国記憶政治論議のファンタジー文学化。",
    development="現代英国「記憶と忘却」ファンタジー小説の規範となった。",
    historical_context="2010年代英国集合的記憶論議反映。",
    primary_source_url=BRITT+"biography/Kazuo-Ishiguro",
    primary_source_type="Britannica: Ishiguro",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="バンヴィル『証拠の書』",
    name_en="Banville's The Book of Evidence",
    name_original="The Book of Evidence",
    period_key="ポストモダン期",
    definition="ジョン・バンヴィルが1989年に発表した長編。アイルランド人殺人犯モンゴメリーの独白による英国・アイルランド・ポストモダン規範作。",
    background="1980年代後半アイルランド・ポストモダン文学運動の代表作。",
    development="バンヴィル「フランクシリーズ」の起点となった。",
    historical_context="1980年代アイルランド文学運動反映。",
    primary_source_url=BRITT+"biography/John-Banville",
    primary_source_type="Britannica: Banville",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="バンヴィル『コペルニクス博士』",
    name_en="Banville's Doctor Copernicus",
    name_original="Doctor Copernicus",
    period_key="ポストモダン期",
    definition="バンヴィルが1976年に発表した長編。コペルニクスの生涯を描いた英国・アイルランド歴史記述的メタフィクション規範作。",
    background="1970年代アイルランド歴史記述的メタフィクション運動の代表。",
    development="バンヴィル「科学者四部作」の起点。",
    historical_context="1970年代アイルランド歴史小説論議反映。",
    primary_source_url=BRITT+"biography/John-Banville",
    primary_source_type="Britannica: Banville",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="アリ・スミス『偶然』",
    name_en="Ali Smith's The Accidental",
    name_original="The Accidental",
    period_key="ポスト・ポストモダン期",
    definition="アリ・スミスが2005年に発表した長編。英国家族の休暇に侵入する謎の女性アンバーを描いた英国ポスト・ポストモダン規範作。",
    background="2000年代英国家族小説の脱構築的継承。",
    development="現代英国実験家族小説の規範となった。",
    historical_context="2000年代英国家族論議反映。",
    primary_source_url=BRITT+"biography/Ali-Smith",
    primary_source_type="Britannica: Ali Smith",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="アリ・スミス『季節四部作・秋』",
    name_en="Ali Smith's Autumn",
    name_original="Autumn",
    period_key="ポスト・ポストモダン期",
    definition="アリ・スミスが2016年に発表した長編。Brexit直後の英国を描いた季節四部作の第一作で英国ポスト・ポストモダン規範作。",
    background="2016年Brexit直後英国の即時的文学的応答。",
    development="現代英国「Brexit文学」の規範となった。",
    historical_context="2010年代後半英国Brexit論議反映。",
    primary_source_url=BRITT+"biography/Ali-Smith",
    primary_source_type="Britannica: Ali Smith",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ミッチェル『ボーン・クロックス』",
    name_en="Mitchell's The Bone Clocks",
    name_original="The Bone Clocks",
    period_key="ポスト・ポストモダン期",
    definition="デイヴィッド・ミッチェルが2014年に発表した長編。1984年から2043年までの六つの時代を不死者闘争で結ぶ英国ポスト・ポストモダン規範作。",
    background="2010年代英国における気候変動・長期未来論議の文学化。",
    development="現代英国百科全書的長期未来小説の規範となった。",
    historical_context="2010年代英国気候未来論議反映。",
    primary_source_url=BRITT+"biography/David-Mitchell-British-author",
    primary_source_type="Britannica: Mitchell",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ウェルシュ『フィルス』",
    name_en="Welsh's Filth",
    name_original="Filth",
    period_key="ポストモダン期",
    definition="アーヴィン・ウェルシュが1998年に発表した長編。腐敗エディンバラ警官と寄生虫の二重独白を描いたスコットランド・ポストモダン規範作。",
    background="1990年代スコットランド・ポストモダン運動の代表作。",
    development="ウェルシュ後期作品の規範となった。",
    historical_context="1990年代スコットランド・グランジ文学運動反映。",
    primary_source_url=BRITT+"biography/Irvine-Welsh",
    primary_source_type="Britannica: Welsh",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# C: Continental postmodern (26)
# ============================================================
add(**C, name_ja="エーコ『開かれた作品』",
    name_en="Eco's The Open Work",
    name_original="Opera aperta",
    period_key="ポストモダン期",
    definition="ウンベルト・エーコが1962年に発表した美学書。読者参加による「開かれた作品」概念を提示したイタリア・ポストモダン規範作。",
    background="1960年代イタリア前衛芸術運動グルッポ63の理論化要請。",
    development="読者反応理論・受容理論の祖型となった。",
    historical_context="1960年代イタリア前衛芸術運動の理論的基盤。",
    primary_source_url=BRITT+"biography/Umberto-Eco",
    primary_source_type="Britannica: Eco",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="エーコ『物語における読者』",
    name_en="Eco's The Role of the Reader",
    name_original="Lector in fabula",
    period_key="ポストモダン期",
    definition="エーコが1979年に発表した記号論書。読者の役割を物語論に組み込んだイタリア・ポストモダン規範作。",
    background="1970年代記号論=ナラトロジー融合運動の代表作。",
    development="現代受容理論・読者反応理論の中核テクストとなった。",
    historical_context="1970年代欧州記号論運動の集約期。",
    primary_source_url=BRITT+"biography/Umberto-Eco",
    primary_source_type="Britannica: Eco",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="エーコ『薔薇の名前への補注』",
    name_en="Eco's Postscript to The Name of the Rose",
    name_original="Postille a Il nome della rosa",
    period_key="ポストモダン期",
    definition="エーコが1983年に発表したエッセイ。ポストモダンを「アイロニカルに古典を引用する態度」と定義した規範論。",
    background="『薔薇の名前』成功後の作家自身による作品論要請。",
    development="ポストモダン文学の自己定義の中核テクストとなった。",
    historical_context="1980年代欧州ポストモダン論議反映。",
    primary_source_url=BRITT+"biography/Umberto-Eco",
    primary_source_type="Britannica: Eco",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="エーコ『バウドリーノ』",
    name_en="Eco's Baudolino",
    name_original="Baudolino",
    period_key="ポストモダン期",
    definition="エーコが2000年に発表した長編。12世紀北イタリア出身の山師バウドリーノの遍歴を描いたイタリア・ポストモダン歴史記述的メタフィクション規範作。",
    background="2000年代イタリア中世記憶論議の文学化。",
    development="エーコ後期作品の代表となった。",
    historical_context="2000年代欧州中世記憶論議反映。",
    primary_source_url=BRITT+"biography/Umberto-Eco",
    primary_source_type="Britannica: Eco",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="エーコ『プラハの墓地』",
    name_en="Eco's The Prague Cemetery",
    name_original="Il cimitero di Praga",
    period_key="ポスト・ポストモダン期",
    definition="エーコが2010年に発表した長編。19世紀文書偽造者シモニーニによる『シオン賢者の議定書』創作を描いたイタリア・ポスト・ポストモダン陰謀論規範作。",
    background="2010年代欧州における陰謀論再台頭の文学的応答。",
    development="現代陰謀論・偽情報文学の規範となった。",
    historical_context="2010年代欧州陰謀論論議反映。",
    primary_source_url=BRITT+"biography/Umberto-Eco",
    primary_source_type="Britannica: Eco",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エーコ『六つの森への散歩』",
    name_en="Eco's Six Walks in the Fictional Woods",
    name_original="Sei passeggiate nei boschi narrativi",
    period_key="ポストモダン期",
    definition="エーコが1994年に発表したハーバード講義録。ポストモダン物語論の規範書。",
    background="1990年代米国大学におけるエーコ講義の文学化。",
    development="現代ナラトロジー教育の標準テクストとなった。",
    historical_context="1990年代欧米ナラトロジー教育反映。",
    primary_source_url=BRITT+"biography/Umberto-Eco",
    primary_source_type="Britannica: Eco",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="カルヴィーノ『くもの巣の小道』",
    name_en="Calvino's The Path to the Spiders' Nests",
    name_original="Il sentiero dei nidi di ragno",
    period_key="ポストモダン期",
    definition="イタロ・カルヴィーノが1947年に発表したデビュー長編。リグーリア山地のパルチザンに加わる少年ピンを描いたイタリア・ネオレアリズモ=ポストモダン橋渡し作。",
    background="戦後イタリアにおけるパルチザン記憶の文学化。",
    development="カルヴィーノ後の幻想小説への橋渡しとなった。",
    historical_context="戦後イタリア・ネオレアリズモ運動反映。",
    primary_source_url=BRITT+"biography/Italo-Calvino",
    primary_source_type="Britannica: Calvino",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="カルヴィーノ『まっぷたつの子爵』",
    name_en="Calvino's The Cloven Viscount",
    name_original="Il visconte dimezzato",
    period_key="ポストモダン期",
    definition="カルヴィーノが1952年に発表した寓話小説。トルコ戦争で真っ二つに切られた子爵を描いたイタリア・ポストモダン三部作「われらの祖先」第一作。",
    background="1950年代イタリア・ポストモダン寓話運動の代表作。",
    development="カルヴィーノ三部作の起点となった。",
    historical_context="1950年代イタリア寓話文学運動反映。",
    primary_source_url=BRITT+"biography/Italo-Calvino",
    primary_source_type="Britannica: Calvino",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="カルヴィーノ『木のぼり男爵』",
    name_en="Calvino's The Baron in the Trees",
    name_original="Il barone rampante",
    period_key="ポストモダン期",
    definition="カルヴィーノが1957年に発表した寓話長編。12歳で木の上に登り終生地上に降りなかった男爵を描いたイタリア・ポストモダン規範作。",
    background="1950年代イタリア・ポストモダン寓話運動の集約。",
    development="カルヴィーノ三部作の代表作となった。",
    historical_context="1950年代欧州寓話文学運動反映。",
    primary_source_url=BRITT+"topic/The-Baron-in-the-Trees",
    primary_source_type="Britannica: Baron in the Trees",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="カルヴィーノ『不在の騎士』",
    name_en="Calvino's The Nonexistent Knight",
    name_original="Il cavaliere inesistente",
    period_key="ポストモダン期",
    definition="カルヴィーノが1959年に発表した寓話小説。鎧の中身が空のシャルルマーニュ騎士を描いたイタリア・ポストモダン三部作完結作。",
    background="1950年代末イタリア・ポストモダン寓話運動の到達点。",
    development="カルヴィーノ三部作の完結作となった。",
    historical_context="1950年代末欧州寓話文学運動反映。",
    primary_source_url=BRITT+"biography/Italo-Calvino",
    primary_source_type="Britannica: Calvino",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="カルヴィーノ『パロマー』",
    name_en="Calvino's Mr. Palomar",
    name_original="Palomar",
    period_key="ポストモダン期",
    definition="カルヴィーノが1983年に発表した最終長編。観察者パロマー氏の世界知覚を27章で描いたイタリア・ポストモダン規範作。",
    background="1980年代イタリア・ポストモダン観察者文学の代表作。",
    development="カルヴィーノ後期作品の到達点となった。",
    historical_context="1980年代欧州観察者文学論議反映。",
    primary_source_url=BRITT+"biography/Italo-Calvino",
    primary_source_type="Britannica: Calvino",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="カルヴィーノ『新たな千年紀のための六つのメモ』",
    name_en="Calvino's Six Memos for the Next Millennium",
    name_original="Lezioni americane",
    period_key="ポストモダン期",
    definition="カルヴィーノが1988年(没後)に発表したハーバード講義録。軽さ・速さ・正確さなど文学価値を論じた規範書。",
    background="1980年代後半イタリア文学価値論議の集約。",
    development="現代欧米文学教育の標準テクストとなった。",
    historical_context="1980年代欧州文学価値論議反映。",
    primary_source_url=BRITT+"biography/Italo-Calvino",
    primary_source_type="Britannica: Calvino",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ゼーバルト『眩暈』",
    name_en="Sebald's Vertigo",
    name_original="Schwindel. Gefühle.",
    period_key="ポストモダン期",
    definition="W.G.ゼーバルトが1990年に発表したデビュー長編。スタンダール・カフカ・カサノヴァと著者自身の旅を交差させたドイツ・ポストモダン記憶文学規範作。",
    background="1990年代初頭ドイツ記憶文学運動の代表作。",
    development="ゼーバルト後期記憶文学の起点となった。",
    historical_context="1990年代初頭ドイツ歴史記憶論議反映。",
    primary_source_url=BRITT+"biography/WG-Sebald",
    primary_source_type="Britannica: Sebald",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ゼーバルト『破壊の自然史』",
    name_en="Sebald's On the Natural History of Destruction",
    name_original="Luftkrieg und Literatur",
    period_key="ポストモダン期",
    definition="ゼーバルトが1999年に発表した文学講義。第二次大戦のドイツ都市空爆と文学の沈黙を主題化したドイツ・ポストモダン記憶論争書。",
    background="1990年代後半ドイツ空爆記憶論議の文学的応答。",
    development="現代欧州空爆記憶論議の中核テクストとなった。",
    historical_context="1990年代後半ドイツ歴史記憶論議反映。",
    primary_source_url=BRITT+"biography/WG-Sebald",
    primary_source_type="Britannica: Sebald",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クンデラ『緩やかさ』",
    name_en="Kundera's Slowness",
    name_original="La Lenteur",
    period_key="ポストモダン期",
    definition="ミラン・クンデラが1995年に発表した短編長編。フランス城館での18世紀小説と現代の二重時間を描いたフランス語ポストモダン規範作。",
    background="1990年代欧州における速度文化批判の文学化。",
    development="クンデラ仏語期の起点となった。",
    historical_context="1990年代欧州速度文化論議反映。",
    primary_source_url=BRITT+"biography/Milan-Kundera",
    primary_source_type="Britannica: Kundera",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="クンデラ『無意味の祝祭』",
    name_en="Kundera's The Festival of Insignificance",
    name_original="La Fête de l'insignifiance",
    period_key="ポスト・ポストモダン期",
    definition="クンデラが2014年に発表した最終長編。パリの数人の友人を主人公にしたフランス語ポスト・ポストモダン軽小説規範作。",
    background="2010年代欧州における「軽さ」論議の文学的集約。",
    development="クンデラ最終作として全集的位置を占める。",
    historical_context="2010年代欧州ポスト・ポストモダン軽小説論議反映。",
    primary_source_url=BRITT+"biography/Milan-Kundera",
    primary_source_type="Britannica: Kundera",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="クンデラ『小説の技法』",
    name_en="Kundera's The Art of the Novel",
    name_original="L'Art du roman",
    period_key="ポストモダン期",
    definition="クンデラが1986年に発表したエッセイ集。欧州小説の系譜を再定義したフランス語ポストモダン詩学規範書。",
    background="1980年代欧州小説の自己理解の集約要請。",
    development="現代欧州小説論議の中核テクストとなった。",
    historical_context="1980年代欧州小説論議反映。",
    primary_source_url=BRITT+"biography/Milan-Kundera",
    primary_source_type="Britannica: Kundera",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ウエルベック『闘争領域の拡大』",
    name_en="Houellebecq's Whatever",
    name_original="Extension du domaine de la lutte",
    period_key="ポストモダン期",
    definition="ミシェル・ウエルベックが1994年に発表したデビュー長編。リベラル経済が性愛領域に拡大した結果としての孤独を描いたフランス・ポストモダン規範作。",
    background="1990年代仏国における性愛市場論議の文学化。",
    development="ウエルベック後期作品の起点となった。",
    historical_context="1990年代仏国新自由主義論議反映。",
    primary_source_url=BRITT+"biography/Michel-Houellebecq",
    primary_source_type="Britannica: Houellebecq",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ウエルベック『地図と領土』",
    name_en="Houellebecq's The Map and the Territory",
    name_original="La Carte et le territoire",
    period_key="ポスト・ポストモダン期",
    definition="ウエルベックが2010年に発表したゴンクール賞長編。芸術家ジェドの上昇と作家ウエルベック自身の登場を描いたフランス・ポスト・ポストモダン自己言及小説規範作。",
    background="2010年代仏国における作家=芸術論議の文学化。",
    development="ウエルベック中期到達点となった。",
    historical_context="2010年代仏国作家論議反映。",
    primary_source_url=BRITT+"biography/Michel-Houellebecq",
    primary_source_type="Britannica: Houellebecq",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ウエルベック『セロトニン』",
    name_en="Houellebecq's Serotonin",
    name_original="Sérotonine",
    period_key="ポスト・ポストモダン期",
    definition="ウエルベックが2019年に発表した長編。抗うつ薬セロトニン依存の主人公がフランス農村を彷徨う仏国ポスト・ポストモダン規範作。",
    background="2010年代仏国黄色いベスト運動期の文学的応答。",
    development="ウエルベック後期社会批評の到達点となった。",
    historical_context="2010年代後半仏国社会論議反映。",
    primary_source_url=BRITT+"biography/Michel-Houellebecq",
    primary_source_type="Britannica: Houellebecq",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="モディアノ『暗いブティック通り』",
    name_en="Modiano's Missing Person",
    name_original="Rue des boutiques obscures",
    period_key="ポストモダン期",
    definition="パトリック・モディアノが1978年に発表したゴンクール賞長編。記憶喪失の探偵が自己を探索する仏国ポストモダン規範作。",
    background="1970年代仏国記憶文学運動の代表作。",
    development="モディアノ作品体系の中核となった。",
    historical_context="1970年代仏国占領期記憶論議反映。",
    primary_source_url=BRITT+"biography/Patrick-Modiano",
    primary_source_type="Britannica: Modiano",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="モディアノ『1941年。パリのユダヤ人少女』",
    name_en="Modiano's Dora Bruder",
    name_original="Dora Bruder",
    period_key="ポストモダン期",
    definition="モディアノが1997年に発表した記録的中編。1941年のパリで失踪したユダヤ人少女ドラ・ブリュデールの実在の足跡を辿る仏国ポストモダン記憶文学規範作。",
    background="1990年代仏国ヴィシー期記憶論議の文学化。",
    development="現代仏国記憶=記録文学の規範となった。",
    historical_context="1990年代仏国ホロコースト記憶論議反映。",
    primary_source_url=BRITT+"biography/Patrick-Modiano",
    primary_source_type="Britannica: Modiano",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="サラマーゴ『すべての名前』",
    name_en="Saramago's All the Names",
    name_original="Todos os nomes",
    period_key="ポストモダン期",
    definition="ジョゼ・サラマーゴが1997年に発表した長編。市民登録局の補助書記ジョゼ氏が知らない女性の足跡を辿るポルトガル・ポストモダン規範作。",
    background="1990年代後半ポルトガル官僚制論議の文学化。",
    development="サラマーゴ中期作品の代表となった。",
    historical_context="1990年代欧州官僚制論議反映。",
    primary_source_url=BRITT+"biography/Jose-Saramago",
    primary_source_type="Britannica: Saramago",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="サラマーゴ『リカルド・レイスの死の年』",
    name_en="Saramago's The Year of the Death of Ricardo Reis",
    name_original="O Ano da Morte de Ricardo Reis",
    period_key="ポストモダン期",
    definition="サラマーゴが1984年に発表した長編。ペソアの異名リカルド・レイスがポルトガル独裁初期にリスボンに帰還する文学規範作。",
    background="1980年代ポルトガル民主化期のペソア再評価運動。",
    development="サラマーゴ初期作品の代表となった。",
    historical_context="1980年代ポルトガル民主化記憶論議反映。",
    primary_source_url=BRITT+"biography/Jose-Saramago",
    primary_source_type="Britannica: Saramago",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="サラマーゴ『見えること』",
    name_en="Saramago's Seeing",
    name_original="Ensaio sobre a Lucidez",
    period_key="ポスト・ポストモダン期",
    definition="サラマーゴが2004年に発表した『白の闇』続編長編。83%の市民が白票を投じた選挙危機を描いたポルトガル・ポスト・ポストモダン規範作。",
    background="2000年代欧州民主主義危機論議の文学化。",
    development="サラマーゴ後期政治小説の到達点となった。",
    historical_context="2000年代欧州民主主義論議反映。",
    primary_source_url=BRITT+"biography/Jose-Saramago",
    primary_source_type="Britannica: Saramago",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="クラスナホルカイ『セイオボ降りなさる』",
    name_en="Krasznahorkai's Seiobo There Below",
    name_original="Seiobo járt odalent",
    period_key="ポストモダン期",
    definition="ラースロー・クラスナホルカイが2008年に発表した連作長編。フィボナッチ数で章構成、世界各地の美的経験を描いたハンガリー・ポストモダン規範作。",
    background="2000年代欧州における美学=東洋論議の文学化。",
    development="クラスナホルカイ世界文学化の到達点となった。",
    historical_context="2000年代欧州美学論議反映。",
    primary_source_url=BRITT+"biography/Laszlo-Krasznahorkai",
    primary_source_type="Britannica: Krasznahorkai",
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
            pid = db.get_or_create_period(name_ja=nj, region="西欧",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid

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
            name_to_id[entry["name_ja"]] = cid

        # ---- Post-process: fourth_transform_tags >= 24, cross_domain >= 18 ----
        EXTRA_FOURTH = [
            ("リオタール『ポストモダンの条件』", "正典", "rethinking",
             "「大きな物語への不信」はLLM時代の正典再編論議の理論的先駆。",
             "LLM時代の正典再編"),
            ("リオタール『争異』", "言語", "rethinking",
             "共通言語不在の係争はAI時代の異種言語衝突の理論的先駆。",
             "AI多言語衝突論"),
            ("ボードリヤール『シミュラークルとシミュレーション』", "真正性", "rethinking",
             "ハイパーリアリティ概念はAI生成コンテンツの真偽不確定論の理論的祖型。",
             "AI生成コンテンツ真偽不確定"),
            ("ボードリヤール『消費社会の神話と構造』", "主体", "rethinking",
             "記号消費による主体構成はAI推奨アルゴリズム時代の主体論と並走。",
             "AI推奨アルゴリズム主体"),
            ("ボードリヤール『アメリカ』", "真正性", "rethinking",
             "象徴飽和の米国分析はAI生成米国文化論の理論的先駆。",
             "AI米国文化論"),
            ("ジェイムソン『単一近代性』", "正典", "rethinking",
             "近代性単独性はAI時代の歴史単一性論議と並走。",
             "AI歴史単一性論議"),
            ("ジェイムソン『リアリズムの二律背反』", "物語", "rethinking",
             "情動と物語の二律背反はAI生成情動コンテンツ論の理論的先駆。",
             "AI生成情動コンテンツ"),
            ("ハッチオン『ポストモダニズムの詩学』", "作者性", "rethinking",
             "歴史記述的メタフィクション概念はAI歴史生成小説の理論的祖型。",
             "AI歴史生成小説"),
            ("ハッチオン『パロディの理論』", "創造性", "rethinking",
             "差異を伴う反復としてのパロディはLLM生成のパロディ的本質と直接共振。",
             "LLM生成パロディ本質"),
            ("ハッチオン『アイロニーの剣先』", "受容", "rethinking",
             "アイロニー受容論はAI時代の文脈崩壊・誤読論議と並走。",
             "AI時代文脈崩壊"),
            ("マクヘイル『ポストモダニスト・フィクション構築』", "物語", "rethinking",
             "存在論的支配概念はAI生成多重世界小説の理論的先駆。",
             "AI多重世界小説"),
            ("ハッサン『オルフェウスの解体』", "正典", "rethinking",
             "モダニズム/ポストモダン二元表はAI時代の文学カテゴリ再編論議の祖型。",
             "AI文学カテゴリ再編"),
            ("ブライアン・リチャードソン『非自然な語り』", "物語", "rethinking",
             "非自然語り論はAI生成非自然語りの理論的先駆。",
             "AI生成非自然語り"),
            ("マリ=ロール・ライアン『可能世界』", "物語", "rethinking",
             "可能世界ナラトロジーはAI生成可能世界小説の理論的祖型。",
             "AI可能世界生成"),
            ("マージョリー・ペルロフ『ラディカル・アーティフィス』", "創造性", "rethinking",
             "メディア時代の人工性論はAI詩生成論議の理論的先駆。",
             "AI詩生成論議"),
            ("チャールズ・バーンスタイン『コンテンツの夢』", "言語", "rethinking",
             "L=A=N=G=U=A=G=E派詩学はAI言語実験詩の理論的先駆。",
             "AI言語実験詩"),
            ("ピンチョン『ヴァインランド』", "主体", "rethinking",
             "監視国家後の主体論はAI監視時代主体論の理論的先駆。",
             "AI監視時代主体論"),
            ("ピンチョン『LAヴァイス』", "真正性", "rethinking",
             "ノワール陰謀論パスティーシュはAI生成ノワール小説の理論的祖型。",
             "AI生成ノワール"),
            ("ピンチョン『スロー・ラーナー』", "作者性", "rethinking",
             "作者自身の作品論はAI時代の作家自己解説論議と並走。",
             "AI作家自己解説"),
            ("バース『ジャイルズ・山羊少年』", "正典", "rethinking",
             "大学=世界寓意はAI時代の学術制度論の文学的祖型。",
             "AI時代学術制度論"),
            ("バース『金曜日の本』", "創造性", "rethinking",
             "「補充の文学」概念はAI時代の創造性反復論議の理論的先駆。",
             "AI創造性反復論議"),
            ("クーヴァー『公衆熱浴場の女中』", "物語", "rethinking",
             "反復変奏短編はLLM生成反復・変奏出力の理論的先駆。",
             "LLM反復変奏出力"),
            ("クーヴァー『茨姫』", "創造性", "rethinking",
             "童話分解再構成はAI童話再生成の理論的祖型。",
             "AI童話再生成"),
            ("ホークス『カニバル』", "物語", "rethinking",
             "戦後黙示録的暴力小説はAI時代の暴力テクスト生成論議の文学的祖型。",
             "AI暴力テクスト論議"),
            ("ホークス『ライム・ツイッグ』", "物語", "rethinking",
             "悪夢的犯罪小説はAI生成犯罪小説の理論的先駆。",
             "AI犯罪小説生成"),
            ("ガス『オーメンセッターの運』", "言語", "rethinking",
             "宗教共同体文体実験はAI文体生成の文学的先駆。",
             "AI宗教文体生成"),
            ("ガス『ウィリー・マスターズの孤独な妻』", "言語", "rethinking",
             "視覚タイポグラフィー実験はAIマルチモーダル詩生成の理論的祖型。",
             "AIマルチモーダル詩"),
            ("ガス『言葉の住処』", "言語", "rethinking",
             "言語の物質性論はLLM言語生成の物質性問題の理論的先駆。",
             "LLM言語物質性"),
            ("デリーロ『リブラ』", "真正性", "rethinking",
             "陰謀的歴史記述はAI生成オルタナティブ歴史の文学的先駆。",
             "AI生成オルタナティブ歴史"),
            ("デリーロ『マオII』", "作者性", "rethinking",
             "テロ時代の作家論はAI時代の作家退場論議の理論的先駆。",
             "AI作家退場論議"),
            ("デリーロ『フォーリング・マン』", "物語", "rethinking",
             "9.11後文学はAI時代のトラウマ生成文学の理論的先駆。",
             "AIトラウマ生成文学"),
            ("デリーロ『沈黙』", "受容", "rethinking",
             "デジタル崩壊後沈黙はAI障害時代の沈黙文学の理論的先駆。",
             "AI障害時代沈黙文学"),
            ("カーター『マジック・トイショップ』", "創造性", "rethinking",
             "暗黒童話書き換えはAI童話再生成のフェミニスト的祖型。",
             "AIフェミニスト童話"),
            ("カーター『新しいイヴの受難』", "主体", "rethinking",
             "ジェンダー変身寓意はAI時代のジェンダー生成論議と並走。",
             "AIジェンダー生成"),
            ("アクロイド『チャタトン』", "真正性", "rethinking",
             "偽造をめぐる三層歴史はAI生成歴史的偽造論の理論的先駆。",
             "AI歴史的偽造論"),
            ("アクロイド『ロンドン:伝記』", "真正性", "rethinking",
             "都市=人格論はAI都市記述生成の理論的祖型。",
             "AI都市記述生成"),
            ("バイアット『フレデリカ四部作』", "主体", "rethinking",
             "知識人女性教養小説はAI時代の知識人主体再考論議と並走。",
             "AI知識人主体論議"),
            ("マキューアン『土曜日』", "受容", "rethinking",
             "24時間小説はAIリアルタイム生成小説の理論的先駆。",
             "AIリアルタイム生成"),
            ("イシグロ『充たされざる者』", "物語", "rethinking",
             "夢の論理小説はAI生成夢論理テクストの理論的先駆。",
             "AI夢論理テクスト"),
            ("イシグロ『忘れられた巨人』", "受容", "rethinking",
             "忘却の霧寓意はAI記憶消去時代の文学的祖型。",
             "AI記憶消去論議"),
            ("バンヴィル『証拠の書』", "作者性", "rethinking",
             "殺人犯独白小説はAI生成不誠実証言の理論的先駆。",
             "AI不誠実証言"),
            ("アリ・スミス『季節四部作・秋』", "受容", "rethinking",
             "Brexit即時応答文学はAIリアルタイム時事小説の理論的先駆。",
             "AIリアルタイム時事小説"),
            ("ミッチェル『ボーン・クロックス』", "物語", "rethinking",
             "六時代統合長期小説はAI長期未来生成の文学的祖型。",
             "AI長期未来生成"),
            ("エーコ『開かれた作品』", "受容", "rethinking",
             "「開かれた作品」概念はAI双方向生成芸術の理論的祖型。",
             "AI双方向生成芸術"),
            ("エーコ『物語における読者』", "受容", "rethinking",
             "読者参加ナラトロジーはAI読者参加生成小説の理論的先駆。",
             "AI読者参加生成"),
            ("エーコ『プラハの墓地』", "真正性", "rethinking",
             "陰謀文書創作小説はAI生成陰謀テクストの直接的祖型。",
             "AI陰謀テクスト生成"),
            ("カルヴィーノ『パロマー』", "主体", "rethinking",
             "観察者小説はAI観察視点生成の理論的祖型。",
             "AI観察視点生成"),
            ("カルヴィーノ『新たな千年紀のための六つのメモ』", "創造性", "rethinking",
             "軽さ・速さ・正確さの文学価値論はAI時代文学価値再考の理論的祖型。",
             "AI時代文学価値再考"),
            ("ゼーバルト『眩暈』", "物語", "rethinking",
             "歴史的旅と自伝の融合はAI生成記憶=旅文学の理論的先駆。",
             "AI記憶=旅文学"),
            ("ゼーバルト『破壊の自然史』", "受容", "rethinking",
             "空爆記憶論争はAI時代の空爆映像論議と並走。",
             "AI空爆映像論議"),
            ("クンデラ『緩やかさ』", "受容", "rethinking",
             "速度文化批判はAI生成速度文化論議の文学的先駆。",
             "AI速度文化論議"),
            ("クンデラ『小説の技法』", "創造性", "rethinking",
             "欧州小説系譜論はAI時代の小説系譜再考と並走。",
             "AI小説系譜再考"),
            ("ウエルベック『闘争領域の拡大』", "主体", "rethinking",
             "性愛市場論はAIマッチング・性愛論議の文学的祖型。",
             "AI性愛マッチング論議"),
            ("ウエルベック『地図と領土』", "作者性", "rethinking",
             "作家=芸術家自己言及はAI時代の作家自己生成論議と並走。",
             "AI作家自己生成"),
            ("ウエルベック『セロトニン』", "主体", "rethinking",
             "抗うつ薬依存主体はAI時代の精神薬理主体論議と並走。",
             "AI精神薬理主体"),
            ("モディアノ『暗いブティック通り』", "主体", "rethinking",
             "記憶喪失主体はAI記憶消失主体論議の文学的先駆。",
             "AI記憶消失主体"),
            ("モディアノ『1941年。パリのユダヤ人少女』", "真正性", "rethinking",
             "実在足跡記録小説はAI記録生成倫理論議の文学的祖型。",
             "AI記録生成倫理"),
            ("サラマーゴ『すべての名前』", "受容", "rethinking",
             "市民登録局官僚制小説はAIアルゴリズム的官僚制論の文学的先駆。",
             "AIアルゴリズム官僚制"),
            ("サラマーゴ『リカルド・レイスの死の年』", "作者性", "rethinking",
             "ペソア異名再生はAI作家異名生成の理論的祖型。",
             "AI作家異名生成"),
            ("サラマーゴ『見えること』", "受容", "rethinking",
             "白票民主主義危機はAI時代民主主義危機論議と並走。",
             "AI民主主義危機論議"),
            ("クラスナホルカイ『セイオボ降りなさる』", "創造性", "rethinking",
             "フィボナッチ章構造小説はAI数理構造小説の理論的祖型。",
             "AI数理構造小説"),
        ]
        for nm, axis, status, rationale, ai_phen in EXTRA_FOURTH:
            cid = name_to_id.get(nm)
            if not cid:
                continue
            try:
                db.tag_fourth_transform(cid, axis=axis, status=status,
                                        rationale=rationale,
                                        related_ai_phenomenon=ai_phen)
                fourth_count += 1
            except LitDBError as e:
                print(f"  [warn] fourth tag failed for {nm}: {e}")

        EXTRA_CD = [
            ("リオタール『ポストモダンの条件』", "PHIL", "parallel",
             "知識正統化危機論", "大きな物語不信は哲学知識論の中核。"),
            ("ボードリヤール『シミュラークルとシミュレーション』", "PHIL", "parallel",
             "ハイパーリアリティ哲学", "シミュラークル四段階は現代記号哲学の中核。"),
            ("ボードリヤール『消費社会の神話と構造』", "MG", "parallel",
             "記号的消費の経営学", "記号消費はマーケティング理論の中核。"),
            ("ジェイムソン『リアリズムの二律背反』", "PHIL", "parallel",
             "リアリズム哲学", "情動と物語の対立は美学哲学と並走。"),
            ("ハッチオン『ポストモダニズムの詩学』", "Innovation", "parallel",
             "歴史記述的革新", "歴史記述的メタフィクションは知識革新理論と並走。"),
            ("マクヘイル『ポストモダニスト・フィクション構築』", "AI-Development", "parallel",
             "存在論的多重世界AI", "存在論的支配はAI多重世界生成と並走。"),
            ("マリ=ロール・ライアン『可能世界』", "AI-Development", "parallel",
             "可能世界AI", "可能世界ナラトロジーはAI物語生成の理論基盤。"),
            ("ピンチョン『ヴァインランド』", "AN", "parallel",
             "監視文化人類学", "監視国家小説は監視文化人類学と並走。"),
            ("バース『金曜日の本』", "Innovation", "parallel",
             "創造性反復理論", "「補充の文学」は創造性反復論と並走。"),
            ("クーヴァー『茨姫』", "Myth-Narratives", "parallel",
             "童話再生成", "童話分解再構成は神話再生成研究と並走。"),
            ("ホークス『カニバル』", "AN", "parallel",
             "戦後暴力人類学", "黙示録的暴力小説は戦後暴力文化論と並走。"),
            ("ガス『言葉の住処』", "PHIL", "parallel",
             "言語物質性哲学", "言語物質性論は言語哲学と並走。"),
            ("デリーロ『リブラ』", "AN", "parallel",
             "陰謀文化人類学", "歴史的陰謀小説は陰謀文化論と並走。"),
            ("デリーロ『フォーリング・マン』", "AN", "parallel",
             "9.11記憶人類学", "9.11トラウマ小説は9.11記憶人類学と並走。"),
            ("カーター『新しいイヴの受難』", "PHIL", "parallel",
             "ジェンダー哲学", "ジェンダー変身寓意はジェンダー哲学と並走。"),
            ("アクロイド『チャタトン』", "AN", "parallel",
             "歴史的偽造文化", "三層歴史小説は歴史的偽造論と並走。"),
            ("アクロイド『ロンドン:伝記』", "AN", "parallel",
             "都市記憶人類学", "都市=人格論は都市記憶人類学と並走。"),
            ("マキューアン『土曜日』", "AN", "parallel",
             "イラク戦争記憶", "2003年2月15日小説はイラク戦争記憶論と並走。"),
            ("イシグロ『忘れられた巨人』", "Myth-Narratives", "parallel",
             "アーサー王神話", "中世忘却ファンタジーはアーサー王神話研究と並走。"),
            ("バンヴィル『証拠の書』", "AN", "parallel",
             "アイルランド記憶", "アイルランド殺人犯小説はアイルランド記憶論と並走。"),
            ("アリ・スミス『季節四部作・秋』", "AN", "parallel",
             "Brexit文化人類学", "Brexit即時応答小説はBrexit文化人類学と並走。"),
            ("ミッチェル『ボーン・クロックス』", "AI-Development", "parallel",
             "長期未来予測AI", "六時代統合小説はAI長期未来生成と並走。"),
            ("エーコ『開かれた作品』", "PHIL", "parallel",
             "受容美学", "「開かれた作品」概念は受容美学の中核。"),
            ("エーコ『プラハの墓地』", "AN", "parallel",
             "陰謀論文化人類学", "陰謀文書創作小説は陰謀論文化論と並走。"),
            ("ゼーバルト『破壊の自然史』", "AN", "parallel",
             "空爆記憶人類学", "ドイツ空爆記憶論争は空爆記憶人類学と並走。"),
            ("ウエルベック『闘争領域の拡大』", "AN", "parallel",
             "性愛市場文化", "性愛経済小説は性愛市場文化論と並走。"),
            ("モディアノ『1941年。パリのユダヤ人少女』", "AN", "parallel",
             "ホロコースト記憶人類学", "実在足跡記録小説はホロコースト記憶論と並走。"),
            ("サラマーゴ『見えること』", "PHIL", "parallel",
             "民主主義哲学", "白票民主主義危機は民主主義哲学と並走。"),
            ("クラスナホルカイ『セイオボ降りなさる』", "Myth-Narratives", "parallel",
             "東洋美学神話", "東洋美的経験連作は東洋美学神話研究と並走。"),
            ("ハッサン『オルフェウスの解体』", "Myth-Narratives", "parallel",
             "オルフェウス神話", "「オルフェウス解体」比喩はオルフェウス神話研究と並走。"),
        ]
        for nm, tdb, ltype, tname, desc in EXTRA_CD:
            cid = name_to_id.get(nm)
            if not cid:
                continue
            try:
                db.insert_cross_domain(
                    lit_entity_type="concept", lit_entity_id=cid,
                    target_db=tdb, link_type=ltype,
                    target_entity_name=tname, description=desc)
                cd_count += 1
            except LitDBError as e:
                print(f"  [warn] cross_domain failed for {nm}: {e}")

        summary = db.progress_summary()
        print(f"[c11-w23] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c11-w23] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        if total:
            print(f"[c11-w23] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
