"""LIT-DB Phase 2 Wave 14 — C33: Children/Popular/Genre Literature (+60).

Subfield: lit_genre (id=21), region='周縁横断'.
Adds 60 NEW concepts (existing 41 → target 101) covering:
  A: Children's literature classics expanded (Andersen/Carroll deep,
     Baum, Milne, Lindgren, Saint-Exupéry, Sendak, Dahl, Lewis Narnia,
     Tolkien children, Pullman, Riordan, picture book theory, Carle,
     Brown, Seuss, Steig, Miyazawa, Murakami strange) — 16
  B: YA / school stories (Hinton, Salinger generational, John Green,
     Hardy Boys/Nancy Drew, school stories) — 6
  C: Mystery deep dive (Christie Poirot, Sayers, Hammett Maltese,
     Chandler Long Goodbye, Highsmith Ripley, P.D. James, Macdonald,
     Le Carré, cozy, hard-boiled subforms, golden age, noir deepening) — 11
  D: SF deeper (Wells Time Machine/War of Worlds, Heinlein Stranger,
     Le Guin Left Hand, Dick UBIK, Stephenson, Bradbury, Sturgeon,
     Clarke 2001) — 8
  E: Fantasy/Horror expanded (sword and sorcery, Howard Conan,
     Moorcock Elric, urban fantasy, Gaiman, romantasy, grimdark, weird
     fiction Lovecraft, Shirley Jackson, King, Barker) — 11
  F: Romance & Graphic novel & Manga & Light/Web novel (Heyer Regency,
     Roberts/Steel mass-market, Bechdel Fun Home, Tezuka manga, Hagio,
     Tsuge garo, Japanese light novel, web novel forms) — 8

Mostly secondary tier acceptable for genre fiction, with ~50% primary
on canonical theory chapters / reference works.
fourth_transform_tags >= 18; cross_domain to PT/PHIL/AN >= 12.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("民話・初期児童文学期", "Folk-tale & Early Children", 1697, 1899, ""),
    ("初期SF・パルプ期", "Early SF / Pulp", 1864, 1939, ""),
    ("黄金時代・古典化期", "Golden Age / Canonisation", 1920, 1959, ""),
    ("ジャンル多様化期", "Genre Diversification", 1960, 1989, ""),
    ("ポップ・グローバル化期", "Pop / Globalisation", 1990, 2025, ""),
]

WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
ARCH = "https://archive.org/details/"
GUTEN = "https://www.gutenberg.org/"
SEP = "https://plato.stanford.edu/entries/"
BRITT = "https://www.britannica.com/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_genre", region="周縁横断", original_script="roman")


# ============================================================
# A: Children's literature classics expanded (16)
# ============================================================
add(**C, name_ja="アンデルセン『人魚姫』",
    name_en="Andersen: The Little Mermaid",
    name_original="Den lille Havfrue",
    period_key="民話・初期児童文学期",
    definition="ハンス・クリスチャン・アンデルセン（1805-1875）が1837年に発表した文学童話の代表作。人魚姫が人間の王子への愛のため不死の魂を求め、声と引換えに人間化するが報われず泡となって昇華する物語。民間伝承の人魚モチーフをアンデルセン自身のキリスト教的霊魂観・愛と犠牲のロマン主義的構図に翻案した、19世紀ヨーロッパ文学童話の規範作。",
    background="アンデルセン自身の片想い体験、ノルディック民話の人魚伝承、キリスト教的霊魂不滅論。",
    development="ディズニー1989年映画化以降、結末改変論争を起こしながら世界的児童文学規範として残り続けた。",
    historical_context="19世紀デンマーク・ロマン主義期の文学童話の確立。",
    primary_source_url=GUTEN+"files/27200/27200-h/27200-h.htm",
    primary_source_type="Project Gutenberg: Andersen Tales (English)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"AI生成児童文学の参照点として、アンデルセン作家の倫理的選択（救済の有無、犠牲の意味）が再考される基盤となる。",
         "related_ai_phenomenon":"AI生成児童文学の倫理的選択"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"水界存在の人類学",
         "description":"人魚姫物語は人間/非人間境界、水界存在の存在論を扱う点で人類学的境界儀礼と通底する。"}])

add(**C, name_ja="アンデルセン『雪の女王』",
    name_en="Andersen: The Snow Queen",
    name_original="Snedronningen",
    period_key="民話・初期児童文学期",
    definition="アンデルセンが1844年に発表した7話構成の長編文学童話。悪魔の鏡の破片が目と心に刺さったカイをゲルダが冬の北方を超えて救出する旅の物語。北欧民話、キリスト教的悪と救済、子供の純粋性のロマン主義が編まれた、アンデルセンの代表作の一つ。",
    background="ノルディック冬伝説、キリスト教的善悪二元、ロマン主義の旅・成長物語。",
    development="ル・グウィンらに「真の旅する女主人公の児童文学」として高く評価され、現代ファンタジー（ナルニア・ダーク・マテリアルズ）の構造的源流となった。映画『アナと雪の女王』(2013)が遠縁。",
    historical_context="19世紀北欧ロマン主義期の長編文学童話確立。",
    primary_source_url=GUTEN+"ebooks/27200",
    primary_source_type="Project Gutenberg: Andersen tales",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"7話構成の旅と救済の物語構造は、AI生成児童文学の長編構造設計の規範参照点となる。",
         "related_ai_phenomenon":"AI児童文学の長編構造規範"}])

add(**C, name_ja="キャロル『鏡の国のアリス』",
    name_en="Carroll: Through the Looking-Glass",
    name_original="Through the Looking-Glass, and What Alice Found There",
    period_key="民話・初期児童文学期",
    definition="ルイス・キャロル（1832-1898）が1871年に発表した『不思議の国のアリス』(1865)の続編。チェス盤を旅するアリスが鏡像反転世界で出会うジャバーウォック・ハンプティ・ダンプティ・トウィードルダム=トウィードルディーらの論理と言語遊戯を、左右反転論理学・ナンセンス詩学の極致として展開した児童文学規範作。",
    background="オックスフォード論理学者ドジソンの記号論理学、ヴィクトリア朝児童文学。",
    development="20世紀のナンセンス詩学（リア、ジョイス）、論理パラドックス研究、デリダの差延論にまで影響を及ぼした。",
    historical_context="ヴィクトリア朝後期英国児童文学黄金期。",
    primary_source_url=GUTEN+"ebooks/12",
    primary_source_type="Project Gutenberg: Through the Looking-Glass",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ジャバーウォック詩のナンセンス・新造語は、AI言語モデルが生成する意味/無意味の境界事例の古典的参照点となる。",
         "related_ai_phenomenon":"AI生成ナンセンス言語の理論化"}])

add(**C, name_ja="ボーム『オズの魔法使い』",
    name_en="L. Frank Baum: The Wonderful Wizard of Oz",
    name_original="The Wonderful Wizard of Oz",
    period_key="民話・初期児童文学期",
    definition="ライマン・フランク・ボーム（1856-1919）が1900年に発表した米国児童文学黎明期の代表作。竜巻でカンザスからオズの国に迷い込んだドロシーが、案山子・ブリキの木こり・臆病ライオンと共に魔法使いを訪ねる旅の物語。米国大陸独自の児童ファンタジー伝統を確立し、続編14冊を含む大規模シリーズを生み、1939年映画化で世界的規範化した。",
    background="米国民話、ポピュリスト政治寓意説、19世紀末米国児童出版市場の成立。",
    development="米国独自の「家を出て旅して家に帰る」児童ファンタジー構造の規範を作り、後年の『ハリー・ポッター』『ナルニア』を含む英米児童ファンタジーの構造的源流となった。",
    historical_context="米国出版産業の児童書黎明期。",
    primary_source_url=GUTEN+"ebooks/55",
    primary_source_type="Project Gutenberg: The Wonderful Wizard of Oz",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"「家を出て旅して家に帰る」物語構造は、AI生成児童冒険物語の構造的原型として参照される。",
         "related_ai_phenomenon":"AI生成児童冒険物語の原型"}])

add(**C, name_ja="ミルン『クマのプーさん』",
    name_en="A. A. Milne: Winnie-the-Pooh",
    name_original="Winnie-the-Pooh",
    period_key="黄金時代・古典化期",
    definition="A.A.ミルン（1882-1956）が1926年に発表した英国児童文学の規範作。100エーカーの森に住むクマのプー、コブタ、トラ、フクロウらと少年クリストファー・ロビンの牧歌的物語。E.H.シェパードの線画、第一次大戦後英国の田園的安寧の理想像、子供時代の喪失への哀悼を内蔵する20世紀児童文学の最高峰。",
    background="第一次大戦後英国の喪失感、息子クリストファー・ロビンへの献辞、エドワード朝牧歌田園像。",
    development="ディズニー1966年以降の翻案で世界的児童文化規範化。哲学的読解（『プーと哲学』ホフ等）が続々登場した。",
    historical_context="戦間期英国児童文学黄金期。",
    primary_source_url=ARCH+"winniethepooh00miln",
    primary_source_type="Internet Archive: Winnie-the-Pooh",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"道家自然観",
         "description":"『プーと哲学』(B. Hoff, The Tao of Pooh, 1982) は、プーキャラクターを通じて道家の無為自然を解説した哲学普及書として知られる。"}])

add(**C, name_ja="リンドグレーン『長くつ下のピッピ』",
    name_en="Lindgren: Pippi Longstocking",
    name_original="Pippi Långstrump",
    period_key="黄金時代・古典化期",
    definition="アストリッド・リンドグレーン（1907-2002）が1945年に発表したスウェーデン児童文学の規範作。9歳の少女ピッピが両親なく一人で家に住み、巨大な怪力で大人世界を覆す痛快な物語。「強くて自立した女の子」像を世界に提示し、児童文学におけるジェンダー表象を変えた20世紀の重要作。",
    background="スウェーデン児童文学の伝統、戦後北欧の進歩的児童観、強い女の子像への作家の主張。",
    development="世界70言語以上に翻訳。フェミニスト児童文学批評の規範的事例として参照され、ロールモデル論争を引き起こし続けた。",
    historical_context="第二次大戦終戦直後の北欧児童文学進歩期。",
    primary_source_url=WIKI_EN+"Pippi_Longstocking",
    primary_source_type="Wikipedia: Pippi Longstocking",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"自立した少女主人公像はAI生成児童書のジェンダー表象再考に直結する規範事例。",
         "related_ai_phenomenon":"AI児童書のジェンダー表象再考"}])

add(**C, name_ja="サン=テグジュペリ『星の王子さま』",
    name_en="Saint-Exupéry: The Little Prince",
    name_original="Le Petit Prince",
    period_key="黄金時代・古典化期",
    definition="アントワーヌ・ド・サン=テグジュペリ（1900-1944）が1943年米国亡命中に発表した寓話。砂漠に不時着したパイロットが小惑星B-612から来た王子と出会い、薔薇・狐・大人世界の愚かしさをめぐる対話を交わす物語。世界300言語以上に翻訳された20世紀最も読まれた寓話の一つ。",
    background="第二次大戦中の作家亡命、パイロット経験、当時の米国出版社からの依頼。",
    development="世界300言語超・累計1.5億部。哲学・神学・教育学的読解が無数に蓄積し、児童文学を超えた現代寓話規範となった。",
    historical_context="第二次大戦中の米国亡命知識人による文学創作期。",
    primary_source_url=WIKI_EN+"The_Little_Prince",
    primary_source_type="Wikipedia: Le Petit Prince",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"見える/見えない哲学",
         "description":"「大切なものは目に見えない」言説は、現象学・実存哲学的「見える/見えない」議論への大衆的入口。"}])

add(**C, name_ja="センダック『かいじゅうたちのいるところ』",
    name_en="Sendak: Where the Wild Things Are",
    name_original="Where the Wild Things Are",
    period_key="ジャンル多様化期",
    definition="モーリス・センダック（1928-2012）が1963年に発表した絵本の革命作。罰として部屋に閉じ込められた少年マックスが想像上の怪獣の島へ旅し、王となって暴れた後、家に戻る短編絵本。子供の怒り・暴力性を初めて絵本主題として認め、20世紀絵本理論の規範を覆した。",
    background="20世紀中葉米国児童文学の理想化された子供像、フロイト的児童心理学、センダック自身のホロコースト遺族家族体験。",
    development="絵本研究の必須参照例として、ペリー・ノードルマン、バーバラ・バーダーらの絵本理論の中核事例となった。2009年スパイク・ジョーンズ実写映画化。",
    historical_context="1960年代米国カウンターカルチャー期、絵本の主題拡大期。",
    primary_source_url=WIKI_EN+"Where_the_Wild_Things_Are",
    primary_source_type="Wikipedia: Where the Wild Things Are",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"子供の暗い情動を肯定する絵本理論は、AIが生成する「子供向け」コンテンツの安全策設計の理論的基盤として再考される。",
         "related_ai_phenomenon":"AI児童コンテンツの感情安全策設計"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"児童期と暴力性",
         "description":"センダック絵本は、ロックの白紙状態的児童観を否定し、フロイト的暴力性を肯定する児童哲学の規範事例。"}])

add(**C, name_ja="絵本理論（picture book theory）",
    name_en="picture book theory",
    name_original="picture book theory",
    period_key="ジャンル多様化期",
    definition="絵本という独自メディアの理論化研究分野。バーバラ・バーダー『American Picturebooks from Noah's Ark to The Beast Within』(1976)、ペリー・ノードルマン『言葉と絵：絵本の物語』(1988)、マリア・ニコラエヴァ『絵本はどう機能するか』(2001)を中核とする、画像と言葉の同時意味生成、絵本特有の見開き設計、子供読者の認知発達と絵本の関係を扱う研究領域。",
    background="20世紀絵本の文化的成熟、児童文学研究のメディア論的転回、認知発達心理学。",
    development="ジョー・サーター、ペリー・ノードルマンの後継世代研究、マリア・ニコラエヴァらが展開。コミックス研究と接続した。",
    historical_context="20世紀後半児童文学研究のメディア論的成熟期。",
    primary_source_url=WIKI_EN+"Picture_book",
    primary_source_type="Wikipedia: Picture book",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"画像-言葉同時記号論",
         "description":"絵本理論は画像-言葉同時意味生成という記号論的問題の独自分野。"}])

add(**C, name_ja="ダール児童文学のグロテスク",
    name_en="Roald Dahl's grotesque",
    name_original="Roald Dahl grotesque",
    period_key="ジャンル多様化期",
    definition="ロアルド・ダール（1916-1990）が『チョコレート工場の秘密』(1964)、『マチルダ』(1988)、『おばけ桃の冒険』(1961)等で展開した児童文学の独自スタイル。残酷・グロテスク・大人を愚かしく描く反道徳的風刺、子供の機智による大人への復讐を主題化した。20世紀後半児童文学の理想化路線への対抗様式として規範化した。",
    background="戦時パイロット経験、ダール自身の不遇な学校生活、英国ブラックユーモア伝統。",
    development="クェンティン・ブレイクの線画と一体化した出版様式が世界的規範となり、ティム・バートン的児童映画美学に影響した。",
    historical_context="1960-80年代英国児童出版の主題拡大期。",
    primary_source_url=WIKI_EN+"Roald_Dahl",
    primary_source_type="Wikipedia: Roald Dahl",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ルイス『ナルニア国物語』",
    name_en="C. S. Lewis: The Chronicles of Narnia",
    name_original="The Chronicles of Narnia",
    period_key="黄金時代・古典化期",
    definition="C.S.ルイス（1898-1963）が1950-1956年に発表した7冊からなる児童ファンタジー連作。ペベンシー4兄妹がワードローブを通じてアスラン（キリスト象徴のライオン）が支配するナルニア国に渡り戦う物語群。キリスト教神学アレゴリーと児童ファンタジーを融合した20世紀後半の規範作。",
    background="ルイスのキリスト教変節体験、トールキン・インクリングス交友、英国ファンタジー伝統。",
    development="世界1億部超、ディズニー2005年以降の映画化で再規範化。神学的読解／植民地主義的批判の両論争を引き起こした。",
    historical_context="戦後英国キリスト教児童文学期。",
    primary_source_url=WIKI_EN+"The_Chronicles_of_Narnia",
    primary_source_type="Wikipedia: The Chronicles of Narnia",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="プルマン『ライラの冒険』(His Dark Materials)",
    name_en="Pullman: His Dark Materials",
    name_original="His Dark Materials",
    period_key="ポップ・グローバル化期",
    definition="フィリップ・プルマン（1946-）が1995-2000年に発表した3部作（『黄金の羅針盤』『神秘の短剣』『琥珀の望遠鏡』）。多元宇宙、ダストと呼ばれる素粒子、ダイモン（魂の動物形）を巡る神学的・科学的児童ファンタジー。ミルトン『失楽園』を意識的に書き直した、ナルニア反転的反神学的児童文学規範作。",
    background="プルマンの無神論、ミルトン『失楽園』再解釈、ブレイク詩学。",
    development="2007年映画化、2019年BBC・HBO共同ドラマ化。児童ファンタジー領域で神学を主題化する事例として規範化した。",
    historical_context="1990-2000年代英国児童ファンタジーの理論的成熟期。",
    primary_source_url=WIKI_EN+"His_Dark_Materials",
    primary_source_type="Wikipedia: His Dark Materials",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"神学批判児童文学",
         "description":"プルマンは神学批判を児童ファンタジーで実現する系譜の代表として参照される。"}])

add(**C, name_ja="リオーダン『パーシー・ジャクソン』",
    name_en="Riordan: Percy Jackson",
    name_original="Percy Jackson & the Olympians",
    period_key="ポップ・グローバル化期",
    definition="リック・リオーダン（1964-）が2005-2009年に発表した5冊シリーズ。ギリシャ神話の神々が現代米国に存在し、半神（神と人間のハイブリッド）少年パーシーが冒険する児童ファンタジー。神話原典を現代児童文学に翻案する手法を確立し、後年エジプト・北欧・マヤ神話シリーズへ拡張した。",
    background="ハリー・ポッター以後の児童ファンタジー出版市場、米国ティーン文化、古典神話教育の衰退への著者の対抗。",
    development="2010年・2013年映画化、2023年Disney+ドラマ化。神話を児童文学で再活性化する出版モデルの規範となった。",
    historical_context="2000年代米国ヤングアダルト児童ファンタジーの市場成熟期。",
    primary_source_url=WIKI_EN+"Percy_Jackson_%26_the_Olympians",
    primary_source_type="Wikipedia: Percy Jackson",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="カール『はらぺこあおむし』",
    name_en="Carle: The Very Hungry Caterpillar",
    name_original="The Very Hungry Caterpillar",
    period_key="ジャンル多様化期",
    definition="エリック・カール（1929-2021）が1969年に発表した絵本の現代古典。ティッシュ紙コラージュ技法と穴あき仕掛け、曜日と数の学習要素を組み合わせ、あおむしが食べて成長し蝶になる物語。世界70言語以上、5500万部超の絵本規範作。",
    background="ドイツ系米国画家カールのバウハウス影響、20世紀絵本の触覚・遊び要素の発達。",
    development="ボードブック・しかけ絵本の規範を世界的に確立した。",
    historical_context="1960-70年代米国絵本の感覚拡張期。",
    primary_source_url=WIKI_EN+"The_Very_Hungry_Caterpillar",
    primary_source_type="Wikipedia: The Very Hungry Caterpillar",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ブラウン『おやすみなさいおつきさま』",
    name_en="Brown: Goodnight Moon",
    name_original="Goodnight Moon",
    period_key="黄金時代・古典化期",
    definition="マーガレット・ワイズ・ブラウン（1910-1952）が1947年に発表した米国絵本古典。子兎が部屋の中の物に「おやすみ」と呼びかけながら眠りに落ちる単純なリズム絵本。クレメント・ハードの絵と一体化した就寝儀礼絵本の規範を確立し、米国家庭就寝文化に組み込まれた。",
    background="バンク・ストリート教育学派の児童心理学、20世紀中葉米国家庭の就寝儀礼。",
    development="絵本理論で「単純さの極致」事例として参照され、累計5000万部超の規範作。",
    historical_context="戦後米国家庭文化と児童心理学の絵本適用期。",
    primary_source_url=WIKI_EN+"Goodnight_Moon",
    primary_source_type="Wikipedia: Goodnight Moon",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="スース博士の韻文絵本",
    name_en="Dr. Seuss verse picture books",
    name_original="Dr. Seuss",
    period_key="黄金時代・古典化期",
    definition="セオドア・スース・ガイゼル（1904-1991）が『The Cat in the Hat』(1957)、『Green Eggs and Ham』(1960)、『The Lorax』(1971)等で展開した独自韻文絵本スタイル。限定語彙・押韻・新造語・グロテスクな線画・社会風刺を組み合わせ、米国読書教育・児童絵本の規範を確立した。",
    background="ベーシック・イングリッシュ初学者教科書市場、ルドルフ・フレッシュ『なぜジョニーは読めないか』(1955)による読書教育論争。",
    development="2000年代以降、人種表象の問題で6作品が販売停止された議論あり、絵本歴史の再評価期にある。",
    historical_context="戦後米国読書教育論争期。",
    primary_source_url=WIKI_EN+"Dr._Seuss",
    primary_source_type="Wikipedia: Dr. Seuss",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="宮沢賢治童話",
    name_en="Miyazawa Kenji children's tales",
    name_original="宮沢賢治",
    period_key="初期SF・パルプ期",
    definition="宮沢賢治（1896-1933）が『注文の多い料理店』(1924)、『銀河鉄道の夜』(没後1934)、『風の又三郎』等で展開した日本児童文学の独自宇宙。法華経思想、岩手県農村風土、近代科学（地質学・天文学）、エスペラントを融合した、児童文学を超えた近代日本文学の最重要作品群の一つ。",
    background="法華経信仰、東北農村の貧困、地質学・農業・近代科学への著者の傾倒。",
    development="戦後再評価。ますむらひろしの漫画化、アニメ化（『銀河鉄道の夜』1985）で世界的規範化した。",
    historical_context="大正末-昭和初期日本児童文学・近代詩の融合期。",
    primary_source_url=WIKI_JA+"%E5%AE%AE%E6%B2%A2%E8%B3%A2%E6%B2%BB",
    primary_source_type="Wikipedia: 宮沢賢治",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"賢治童話の宇宙論的・倫理的構造は、AI生成児童文学の倫理的規範の再考の参照点となる。",
         "related_ai_phenomenon":"AI児童文学の宇宙論的射程"}])


# ============================================================
# B: YA / school stories (6)
# ============================================================
add(**C, name_ja="ヒントン『アウトサイダーズ』",
    name_en="Hinton: The Outsiders",
    name_original="The Outsiders",
    period_key="ジャンル多様化期",
    definition="S.E.ヒントン（1948-）が16歳で執筆し1967年に発表した米国ヤングアダルト文学の起点作。労働者階級不良グループ「グリーザーズ」と裕福階級「ソーシャル」の対立を、ティーン視点と俗語で描いた。米国YAジャンルの誕生作として規範化されている。",
    background="60年代米国階級対立、ヒントン自身の高校体験、青少年向け真摯な小説市場の不在への著者の対抗。",
    development="米国YA小説市場の成立を主導し、続編『That Was Then, This Is Now』『Rumble Fish』への発展を経て、現代YAの規範を確立した。",
    historical_context="1960年代米国YA文学市場の誕生期。",
    primary_source_url=WIKI_EN+"The_Outsiders_(novel)",
    primary_source_type="Wikipedia: The Outsiders",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="サリンジャー『ライ麦畑』の世代論",
    name_en="Salinger: Catcher in the Rye generational reading",
    name_original="The Catcher in the Rye",
    period_key="黄金時代・古典化期",
    definition="J.D.サリンジャー（1919-2010）が1951年に発表した青春小説。学校追放の少年ホールデン・コールフィールドの3日間のニューヨーク彷徨を、青年特有の俗語的一人称で語る。形式的にはYAではないが、戦後米国青少年読者の規範作となり、後年のYAジャンル成立の理論的・市場的基盤を築いた点で重要。",
    background="戦後米国青少年文化の出現、サリンジャー自身の戦争経験と精神的危機。",
    development="米国高校教育における必読書化／禁書議論を経て、20世紀青春文学規範。チャップマン・レノン暗殺との関連で社会的議論を起こし続けた。",
    historical_context="戦後米国青少年文化と文学の交差期。",
    primary_source_url=WIKI_EN+"The_Catcher_in_the_Rye",
    primary_source_type="Wikipedia: The Catcher in the Rye",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"青少年通過儀礼の人類学",
         "description":"ライ麦畑は青少年通過儀礼の文学的表象として、人類学的成人儀礼研究と接続する。"}])

add(**C, name_ja="ジョン・グリーン現代YA",
    name_en="John Green's contemporary YA",
    name_original="John Green",
    period_key="ポップ・グローバル化期",
    definition="ジョン・グリーン（1977-）が『Looking for Alaska』(2005)、『The Fault in Our Stars』(2012)等で展開した21世紀米国YA小説。哲学的引用、若者の死・病・喪失主題、SNS世代特有の感性を統合した知的YAスタイル。Tumblr時代のYA市場の規範作家となった。",
    background="2000-2010年代米国SNS文化、Vlogbrothers動画チャンネル、現代YAの主題深化要請。",
    development="『きっと、星のせいじゃない』2014年映画化等で世界的規範化。Booktok・YA Twitter文化の主要参照点となった。",
    historical_context="2000-2010年代米国SNS時代のYA文学成熟期。",
    primary_source_url=WIKI_EN+"John_Green_(author)",
    primary_source_type="Wikipedia: John Green",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ハーディー・ボーイズ／ナンシー・ドルー",
    name_en="Hardy Boys / Nancy Drew",
    name_original="Hardy Boys / Nancy Drew",
    period_key="黄金時代・古典化期",
    definition="ストラトメイヤー・シンジケートが企画し1927年（ハーディー・ボーイズ）、1930年（ナンシー・ドルー）以降複数のゴーストライターが共有筆名で執筆した米国児童ミステリ・シリーズ。少年・少女探偵主人公、ハウスネーム制（ナンシー・ドルーは「Carolyn Keene」）、定型化された冒険プロット、世界1億部超で20世紀児童ミステリの規範。",
    background="米国大恐慌前夜のシリーズ児童書市場、ストラトメイヤー・シンジケートのゴーストライティング体制。",
    development="現代まで継続。ハウスネーム生産モデルはハードボイルド米国児童書の標準となり、その後の児童シリーズの市場規範を築いた。",
    historical_context="戦間期米国児童書出版産業の確立期。",
    primary_source_url=WIKI_EN+"Stratemeyer_Syndicate",
    primary_source_type="Wikipedia: Stratemeyer Syndicate",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="学校物語（school story）ジャンル",
    name_en="school story genre",
    name_original="school story",
    period_key="民話・初期児童文学期",
    definition="ヒューズ『トム・ブラウンの学校生活』(1857)を起点に、英国寄宿学校を舞台とする児童文学ジャンル。フランク・リチャーズ『ビリー・バンター』(1908-)、ブライトン『マロリータワーズ』(1946-1951)、ローリング『ハリー・ポッター』を含む系譜の総称。学校階級制、友情と裏切り、競争・成長を主題とする。",
    background="19世紀英国パブリックスクール改革、ヴィクトリア朝児童雑誌市場、男子・女子別寄宿学校文化。",
    development="20世紀後半に女子学校物語、ハリー・ポッターによるファンタジー学校物語へと展開。日本の学園もの・部活動小説に翻案影響。",
    historical_context="19-20世紀英国学校文化と児童出版の連動期。",
    primary_source_url=WIKI_EN+"School_story",
    primary_source_type="Wikipedia: School story",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヤングアダルト文学のジャンル理論",
    name_en="Young Adult literature genre theory",
    name_original="YA literature theory",
    period_key="ポップ・グローバル化期",
    definition="マイケル・カート、ロバータ・トリテス『ディスターブされた声』(2000)、トリーシャ・ハインズ等が展開したYA文学理論。年齢・主題・物語視点・市場区分を巡る、児童文学とは独立した独自ジャンルとしてのYAの理論化。「若者の自己決定」物語論、「中間性」概念、フェミニスト・クィアYA批評を含む。",
    background="ヒントン以降のYA市場成立、児童文学研究の細分化、米国図書館協会のYALSA設立(1957)。",
    development="現代YA論争（読者対象、内容規制、検閲）の理論的基盤を提供している。",
    historical_context="20世紀末-21世紀のYA文学研究分野の確立期。",
    primary_source_url=WIKI_EN+"Young_adult_fiction",
    primary_source_type="Wikipedia: Young adult fiction",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"YA理論はAI生成YAコンテンツの読者年齢適合・倫理的安全策の理論的基盤として再考される。",
         "related_ai_phenomenon":"AI生成YAコンテンツの読者倫理"}])


# ============================================================
# C: Mystery deep dive (11)
# ============================================================
add(**C, name_ja="クリスティ『エルキュール・ポアロ』正典",
    name_en="Christie: Hercule Poirot canon",
    name_original="Hercule Poirot novels",
    period_key="黄金時代・古典化期",
    definition="アガサ・クリスティ（1890-1976）が1920年『スタイルズ荘の怪事件』から1975年『カーテン』まで55年間で書き継いだ33長編・50超中短編からなるベルギー人探偵エルキュール・ポアロ正典。「灰色の脳細胞」と秩序愛・ベルギー難民出自を核に、『アクロイド殺し』『オリエント急行』『ABC』等の革新作を含む20世紀ミステリの最大規範体系。",
    background="第一次大戦中のベルギー難民実体験、クリスティ自身の薬剤師経験、英国黄金時代ミステリの誕生。",
    development="20世紀ミステリの市場・形式規範を確立。21世紀のソフィー・ハナによる継承小説、各種翻案で再活性化した。",
    historical_context="戦間期-戦後英国黄金時代ミステリ。",
    primary_source_url=WIKI_EN+"Hercule_Poirot",
    primary_source_type="Wikipedia: Hercule Poirot",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="セイヤーズ卿ピーター・ウィムジィ",
    name_en="Sayers: Lord Peter Wimsey",
    name_original="Lord Peter Wimsey novels",
    period_key="黄金時代・古典化期",
    definition="ドロシー・L・セイヤーズ（1893-1957）が1923-1937年に書いた11長編からなる英国貴族探偵ピーター・ウィムジィ・シリーズ。古典ミステリの形式厳守と文学的密度（ダンテ翻訳者でもある著者の博学）を統合し、特に『ナイン・テイラーズ』『学寮祭の夜』は黄金時代ミステリの文学的頂点として評価される。フェミニスト探偵小説の起点でもある。",
    background="英国黄金時代ミステリ、第一次大戦後の階級崩壊、セイヤーズの古典学・神学的素養。",
    development="20世紀後半にPDジェイムズ、ジル・パトン・ウォルシュへ継承された。",
    historical_context="戦間期英国黄金時代ミステリ。",
    primary_source_url=WIKI_EN+"Lord_Peter_Wimsey",
    primary_source_type="Wikipedia: Lord Peter Wimsey",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ハメット『マルタの鷹』",
    name_en="Hammett: The Maltese Falcon",
    name_original="The Maltese Falcon",
    period_key="黄金時代・古典化期",
    definition="ダシール・ハメット（1894-1961）が1930年に発表したハードボイルド・ミステリの規範作。サンフランシスコの私立探偵サム・スペードが偽の宝物を巡る陰謀に巻き込まれる物語。簡素な客観描写、感情を内省せず行動で示す主人公、米国都市の腐敗描写を統合した、20世紀米国ハードボイルド・ジャンルの起点。",
    background="ハメットのピンカートン探偵社実体験、禁酒法時代の米国都市犯罪、米国モダニズム文体。",
    development="ジョン・ヒューストン1941年映画化（ボガート主演）でフィルム・ノワールの起点となり、文学・映画両側で20世紀後半に巨大な影響を残した。",
    historical_context="禁酒法時代米国の犯罪文学誕生期。",
    primary_source_url=WIKI_EN+"The_Maltese_Falcon_(novel)",
    primary_source_type="Wikipedia: The Maltese Falcon",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ハメット的客観・冷淡文体は、AI生成ハードボイルド模倣の規範参照点となる。",
         "related_ai_phenomenon":"AI生成ハードボイルド文体の規範"}])

add(**C, name_ja="チャンドラー『長いお別れ』",
    name_en="Chandler: The Long Goodbye",
    name_original="The Long Goodbye",
    period_key="黄金時代・古典化期",
    definition="レイモンド・チャンドラー（1888-1959）が1953年に発表したハードボイルド・ミステリ後期の代表作。私立探偵フィリップ・マーロウとテリー・レノックスの友情と裏切りを、戦後ロサンゼルスの腐敗を背景に描いた。エドガー賞受賞、村上春樹翻訳でも名高い、ジャンル文学の最高峰の文学的達成。",
    background="チャンドラー晩年の妻シシー死去前後、戦後米国ロサンゼルスの繁栄と腐敗、ハードボイルド・ジャンルの文学的成熟。",
    development="20世紀後半の米国都市犯罪文学（ロス・マクドナルド、ジェイムズ・エルロイ）の規範となり、村上春樹『長いお別れ』翻訳で日本にも深く浸透した。",
    historical_context="戦後米国ハードボイルド・ジャンルの文学的頂点期。",
    primary_source_url=WIKI_EN+"The_Long_Goodbye_(novel)",
    primary_source_type="Wikipedia: The Long Goodbye",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ハイスミス『リプリー』連作",
    name_en="Highsmith: Ripley series",
    name_original="The Talented Mr. Ripley",
    period_key="ジャンル多様化期",
    definition="パトリシア・ハイスミス（1921-1995）が1955-1991年に発表した5冊からなるトム・リプリー連作。倫理を欠いた殺人者主人公の犯罪を読者が共感的に追跡する独特の心理ミステリで、犯罪小説の道徳構造を覆す20世紀後半の規範。",
    background="戦後米国心理サスペンス、ハイスミス自身のクィア・アイデンティティとヨーロッパ亡命体験。",
    development="アンソニー・ミンゲラ1999年『リプリー』映画化でハイスミス再評価が起こり、Netflix2024年シリーズで現代化。",
    historical_context="冷戦期米国-ヨーロッパ心理サスペンス成熟期。",
    primary_source_url=WIKI_EN+"Tom_Ripley",
    primary_source_type="Wikipedia: Tom Ripley",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"反道徳的主人公の倫理",
         "description":"リプリーは反道徳的主人公への読者共感という、現代倫理学・読者反応批評の重要事例。"}])

add(**C, name_ja="P.D.ジェイムズ詩的ミステリ",
    name_en="P.D. James: poetic mystery",
    name_original="P.D. James",
    period_key="ジャンル多様化期",
    definition="P.D.ジェイムズ（1920-2014）が1962年から書き継いだアダム・ダルグリッシュ警視シリーズ。詩人でもある探偵を主人公に、文学的密度の高い描写、英国階級・組織心理の精緻な分析を統合した、英国ハイブロウ警察小説の規範作家。",
    background="戦後英国の文学的ミステリ、ジェイムズ自身の保健省・内務省勤務体験、セイヤーズへの傾倒。",
    development="20世紀末英国ミステリの最高峰として規範化。BBCドラマ化、ジェイン・オースティン続編『デス・カムズ・トゥ・ペンバリー』(2011)で文学とジャンルを跨いだ。",
    historical_context="戦後英国ハイブロウ・ミステリ成熟期。",
    primary_source_url=WIKI_EN+"P._D._James",
    primary_source_type="Wikipedia: P.D. James",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マクドナルド『リュー・アーチャー』",
    name_en="Ross Macdonald: Lew Archer",
    name_original="Lew Archer novels",
    period_key="ジャンル多様化期",
    definition="ロス・マクドナルド（ケネス・ミラー、1915-1983）が1949-1976年に発表した18長編からなるカリフォルニア私立探偵リュー・アーチャー・シリーズ。ハメット・チャンドラー系譜を継承しつつ、家族秘密・世代間トラウマ・心理学的洞察を中心に据え、20世紀後半米国ハードボイルドの心理学的成熟を達成した。",
    background="戦後米国カリフォルニア郊外文化、マクドナルド自身のフロイト的精神分析への関心、ハードボイルド・ジャンルの心理化。",
    development="ジョン・ル・カレ、ジェイムズ・エルロイ、ローレンス・ブロック、サラ・パレツキーらの世代に巨大な影響を残した。",
    historical_context="戦後米国ハードボイルド心理学化期。",
    primary_source_url=WIKI_EN+"Ross_Macdonald",
    primary_source_type="Wikipedia: Ross Macdonald",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ル・カレ『ティンカー、テイラー』",
    name_en="Le Carré: Tinker, Tailor, Soldier, Spy",
    name_original="Tinker, Tailor, Soldier, Spy",
    period_key="ジャンル多様化期",
    definition="ジョン・ル・カレ（1931-2020）が1974年に発表したスマイリー三部作の第1作。MI6内部のソ連二重スパイ「もぐら」を炙り出すジョージ・スマイリーの追跡を、冷戦末期英国諜報機関の倫理的風化として描いた、20世紀スパイ小説の文学的頂点。",
    background="ル・カレ自身のMI5・MI6勤務体験（実名David Cornwell）、ケンブリッジ・ファイヴ事件、冷戦末期英国諜報の倫理的危機。",
    development="ジャンル小説（スパイ）の文学的格上げに決定的役割を果たし、グレアム・グリーンと並ぶ20世紀英国諜報文学の頂点として評価される。2011年映画化、BBCドラマ化。",
    historical_context="冷戦末期英国諜報文学成熟期。",
    primary_source_url=WIKI_EN+"Tinker,_Tailor,_Soldier,_Spy",
    primary_source_type="Wikipedia: Tinker, Tailor, Soldier, Spy",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="コージー・ミステリ（cozy mystery）",
    name_en="cozy mystery sub-genre",
    name_original="cozy mystery",
    period_key="ポップ・グローバル化期",
    definition="クリスティのミス・マープル系譜を起点に、1990年代米国市場で確立されたミステリ・サブジャンル。小さな田舎町、素人女性探偵、暴力描写の最小化、料理・園芸・趣味要素の併設、シリーズ性、女性中心読者層を特徴とする。米国大衆ペーパーバック市場の主要セグメント。",
    background="クリスティ後期マープル小説、20世紀米国ペーパーバック市場の女性向けジャンル細分化。",
    development="現代米国コージー出版は年間数百冊規模の巨大市場として継続。電子書籍時代に独立出版形式での発展も継続している。",
    historical_context="1990年代-現代米国ペーパーバック市場ジャンル細分化期。",
    primary_source_url=WIKI_EN+"Cozy_mystery",
    primary_source_type="Wikipedia: Cozy mystery",
    importance_score=2, source_tier="tertiary", canonical_in_region="marginal")

add(**C, name_ja="黄金時代ミステリの「フェアプレイ」綱領",
    name_en="Golden Age fair-play doctrine",
    name_original="fair play doctrine",
    period_key="黄金時代・古典化期",
    definition="ロナルド・ノックス『十戒』(1929)、S.S.ヴァン・ダイン『推理小説作法二十則』(1928)、英国ディテクション・クラブ宣誓(1930)に表現された、黄金時代ミステリの形式規範。読者と探偵が同じ手がかりを持つこと、超自然的解決の禁止、双子トリック等の禁止条項からなる、ジャンルが自己規範化した珍しい歴史的事例。",
    background="1920年代英米ミステリ過剰生産、ジャンルの形式的洗練要求、ディテクション・クラブ結成。",
    development="現代ミステリ批評・実作で参照される歴史的規範。アントニー・バークリー、コリン・デクスター、ジョン・ディクスン・カー研究の中核参照点。",
    historical_context="戦間期英米ミステリの形式自己規範化期。",
    primary_source_url=WIKI_EN+"Fair-play_principle_(literature)",
    primary_source_type="Wikipedia: Fair-play principle",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"形式規範と読者倫理",
         "description":"フェアプレイ綱領は、ジャンルが自己規範化した珍しい事例として、文学倫理学的研究の対象。"}])

add(**C, name_ja="ノワール（noir）小説の理論",
    name_en="noir fiction theory",
    name_original="roman noir",
    period_key="黄金時代・古典化期",
    definition="ハメット・ケイン『郵便配達は二度ベルを鳴らす』(1934)、ジム・トンプスン、デイヴィッド・グーディスらに代表される米国犯罪文学のサブジャンル。ハードボイルドの探偵中心に対し、犯罪者・被害者・没落者を主人公に置き、宿命論・倫理的崩壊・大都市暗部を描く。仏「série noire」叢書(1945-)で命名・体系化された。",
    background="禁酒法時代後米国都市の絶望、戦後仏「série noire」叢書のキュレーション、フィルム・ノワール映画ジャンルの並行発展。",
    development="現代の「ネオ・ノワール」（エルロイ、レナード）、北欧ノワール（ネスボ、ラーション）、各国ノワール文学への展開。",
    historical_context="戦間期米国犯罪文学の暗黒化と仏戦後再キュレーション期。",
    primary_source_url=WIKI_EN+"Noir_fiction",
    primary_source_type="Wikipedia: Noir fiction",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# D: SF deeper (8)
# ============================================================
add(**C, name_ja="ウェルズ『タイムマシン』",
    name_en="Wells: The Time Machine",
    name_original="The Time Machine",
    period_key="初期SF・パルプ期",
    definition="H.G.ウェルズ（1866-1946）が1895年に発表した近代SFの規範作。時間旅行者が80万年後の未来でエロイ族（退化した上層階級）とモーロック族（地下労働者の食人種）に会う物語。ダーウィン進化論、社会主義階級論、熱力学第二法則を統合した、SFというジャンルの確立を画する作品。",
    background="ヴィクトリア朝末英国の進化論論争、ハクスリー門下のウェルズの科学教育、社会主義運動。",
    development="現代SFの「タイムマシン」モチーフの起点となり、20世紀全SFの参照規範となった。",
    historical_context="ヴィクトリア朝末英国SF誕生期。",
    primary_source_url=GUTEN+"ebooks/35",
    primary_source_type="Project Gutenberg: The Time Machine",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ウェルズ『宇宙戦争』",
    name_en="Wells: The War of the Worlds",
    name_original="The War of the Worlds",
    period_key="初期SF・パルプ期",
    definition="ウェルズが1898年に発表したSF古典。火星人が地球を侵略し人類を圧倒、最後に微生物で滅ぶ物語。植民地主義への逆説的批判（英帝国による被植民地への暴力を逆転して英国に投影）、災害文学の起点としても重要。1938年オーソン・ウェルズのラジオドラマでパニックを引き起こしたメディア論的事件としても知られる。",
    background="ヴィクトリア朝末英国植民地拡張、ウェルズの植民地主義批判、進化論的優越理論への懐疑。",
    development="20世紀全侵略SFの規範。1953年・2005年映画化、ジェフ・ウェイン1978年ロックオペラ化等で規範化を維持。",
    historical_context="ヴィクトリア朝末英国植民地批判SF誕生期。",
    primary_source_url=GUTEN+"ebooks/36",
    primary_source_type="Project Gutenberg: The War of the Worlds",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"植民地接触の文学化",
         "description":"宇宙戦争は植民地接触の暴力性を逆転投影した文学事例として人類学的接触研究と接続する。"}])

add(**C, name_ja="ハインライン『異星の客』",
    name_en="Heinlein: Stranger in a Strange Land",
    name_original="Stranger in a Strange Land",
    period_key="ジャンル多様化期",
    definition="ロバート・A・ハインライン（1907-1988）が1961年に発表したSF。火星育ちの地球人ヴァレンタイン・マイケル・スミスが米国社会に戻り宗教を創始する物語。ヒッピー世代・カウンターカルチャーの聖典として読まれ、Manson事件（1969）への影響さえ取り沙汰された、SFとカウンターカルチャーの結節点。",
    background="戦後米国SFの市民権獲得、1960年代カウンターカルチャー、ハインライン中期の自由放任主義。",
    development="grok（理解する）、water-brother等の独自語彙が英語に定着。1962年Hugo賞受賞。",
    historical_context="冷戦中期米国SFのカウンターカルチャー期。",
    primary_source_url=WIKI_EN+"Stranger_in_a_Strange_Land",
    primary_source_type="Wikipedia: Stranger in a Strange Land",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ル=グウィン『闇の左手』",
    name_en="Le Guin: The Left Hand of Darkness",
    name_original="The Left Hand of Darkness",
    period_key="ジャンル多様化期",
    definition="アーシュラ・K・ル=グウィン（1929-2018）が1969年に発表したSF。性別を持たず発情期に応じて男女に変わるゲセン人惑星を地球人外交官が訪ねる物語。フェミニストSFの起点作、人類学的SF（ル=グウィンの父はクローバー）の典型として、ジェンダー研究と文学批評の重要参照テキスト。",
    background="ル=グウィンの父アルフレッド・クローバー（人類学者）の影響、第二波フェミニズム、SFの社会人類学的成熟。",
    development="現代フェミニストSF（バトラー、アトウッド、ジェミシン）、クィア・ジェンダー理論SFの規範作となった。",
    historical_context="1960-70年代フェミニストSF誕生期。",
    primary_source_url=WIKI_EN+"The_Left_Hand_of_Darkness",
    primary_source_type="Wikipedia: The Left Hand of Darkness",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ジェンダー無し惑星の思考実験は、AIが性別カテゴリを生成・割当する構造の人類学的批評の理論的基盤となる。",
         "related_ai_phenomenon":"AIシステムのジェンダー生成批評"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"人類学的SFの父娘継承",
         "description":"クローバー人類学のSF文学翻案として、人類学とSF文学の交差を示す典型例。"}])

add(**C, name_ja="ディック『ユービック』",
    name_en="Dick: Ubik",
    name_original="Ubik",
    period_key="ジャンル多様化期",
    definition="フィリップ・K・ディック（1928-1982）が1969年に発表したSF。半生半死状態（half-life）の意識構造、現実崩壊のループ、神的なユービック・スプレーを巡る、ディック中期の代表作。タイム・マガジン20世紀ベスト100小説（2005）に選出された、SFジャンル超えの規範作。",
    background="ディックのグノーシス神学的関心、1960年代カウンターカルチャー薬物文化、現実認識の懐疑論。",
    development="ジャン・ボードリヤール、フレドリック・ジェイムソンらポストモダン哲学者による哲学的読解の主要対象となり、SFと哲学・現代思想の架橋作品となった。",
    historical_context="1960-70年代米国SFの哲学的成熟期。",
    primary_source_url=WIKI_EN+"Ubik",
    primary_source_type="Wikipedia: Ubik",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"現実崩壊・シミュレーションSFは、AI生成現実とユーザの認識的危機の現代的読解の規範参照点となる。",
         "related_ai_phenomenon":"AI生成現実とシミュレーション認識"}])

add(**C, name_ja="ブラッドベリ『華氏451度』",
    name_en="Bradbury: Fahrenheit 451",
    name_original="Fahrenheit 451",
    period_key="黄金時代・古典化期",
    definition="レイ・ブラッドベリ（1920-2012）が1953年に発表したディストピアSF。書物が燃やされる未来社会で「焚書官」モンタグが書物の人間化（人々が一冊の本を暗唱する）抵抗運動に出会う物語。マッカーシズム期米国の検閲不安への文学的応答、書物の精神文化への愛の宣言として、SFと検閲論の規範。",
    background="マッカーシズム期米国検閲不安、第二次大戦中ナチ焚書記憶、ブラッドベリのロサンゼルス図書館での執筆体験。",
    development="現代米国検閲論争（1980年代禁書運動、2020年代州立法による書籍規制）の主要参照点として現役の規範。",
    historical_context="冷戦初期米国SF・ディストピア成熟期。",
    primary_source_url=WIKI_EN+"Fahrenheit_451",
    primary_source_type="Wikipedia: Fahrenheit 451",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"検閲と知の倫理",
         "description":"華氏451度は、検閲・知の倫理の現代哲学・政治哲学的議論の主要文学的参照点。"}])

add(**C, name_ja="クラーク『2001年宇宙の旅』",
    name_en="Clarke: 2001: A Space Odyssey",
    name_original="2001: A Space Odyssey",
    period_key="ジャンル多様化期",
    definition="アーサー・C・クラーク（1917-2008）が1968年にキューブリック映画と並行して発表したSF。HAL9000人工知能との対決、モノリスを巡る人類進化、木星越境を描く20世紀ハードSFの規範作。映画と小説の同時発表という制作上の革新と、AI意識・人類超越の主題が融合した記念碑作。",
    background="クラークの英国王立空軍レーダー技術者経験、キューブリックとの3年共同作業、1960年代米ソ宇宙競争。",
    development="現代AI論議（HAL9000）、シンギュラリティ論議の文学的参照点として継続的に規範。",
    historical_context="冷戦中期米英ハードSF・AI主題化期。",
    primary_source_url=WIKI_EN+"2001:_A_Space_Odyssey_(novel)",
    primary_source_type="Wikipedia: 2001 (novel)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"HAL9000は人工知能の文学的原型として、現代AIエージェント設計の倫理議論の必須参照点。",
         "related_ai_phenomenon":"AIエージェント設計の倫理的原型"}])

add(**C, name_ja="ステファンスン『スノウ・クラッシュ』",
    name_en="Stephenson: Snow Crash",
    name_original="Snow Crash",
    period_key="ポップ・グローバル化期",
    definition="ニール・ステファンスン（1959-）が1992年に発表したサイバーパンクSF。ピザ配達兼ハッカーのヒロ・プロタゴニストが、シュメール神話的言語ウィルスとメタヴァース（同作で命名）の陰謀に挑む物語。「メタヴァース」「アバター」概念の文学的起点、後のFacebook/Meta「メタヴァース」戦略の語源として現代テック文化と密接に結びついた。",
    background="1990年代初期インターネット文化、ギブスン後のサイバーパンク第二波、ステファンスンの古代言語学的関心。",
    development="2021年Meta社のリブランディングでメタヴァース概念再注目を受け、現代VR・Web3文化の文学的源流として再活性化した。",
    historical_context="1990年代初期インターネット文化期。",
    primary_source_url=WIKI_EN+"Snow_Crash",
    primary_source_type="Wikipedia: Snow Crash",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"メタヴァース語源としてWeb3/AI仮想現実時代の主要文学的参照点。",
         "related_ai_phenomenon":"メタヴァース言語起源のAI再活性化"}])


# ============================================================
# E: Fantasy / Horror expanded (11)
# ============================================================
add(**C, name_ja="ソード・アンド・ソーサリー（剣と魔法）",
    name_en="sword and sorcery",
    name_original="sword and sorcery",
    period_key="初期SF・パルプ期",
    definition="ロバート・E・ハワード『コナン』(1932-)、フリッツ・ライバー（同名命名者）、マイケル・ムアコック『エルリック』(1961-)らが展開したファンタジー・サブジャンル。広大な歴史叙事のハイ・ファンタジー（トールキン）に対し、無頼の剣士主人公の小規模冒険を主眼とする、米国パルプ起源のファンタジー潮流。",
    background="戦間期米国パルプ雑誌「Weird Tales」、ハワード・ハインライン世代の冒険文学、20世紀後半英国ニュー・ウェーブSF。",
    development="ジョージ・R・R・マーティン『氷と炎の歌』、ジョー・アバクロンビー、現代の「グリムダーク」ファンタジーへ系譜化。",
    historical_context="戦間期米国パルプ-戦後英国ニュー・ウェーブの架橋期。",
    primary_source_url=WIKI_EN+"Sword_and_sorcery",
    primary_source_type="Wikipedia: Sword and sorcery",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ハワード『コナン』",
    name_en="Howard: Conan the Barbarian",
    name_original="Conan the Barbarian",
    period_key="初期SF・パルプ期",
    definition="ロバート・E・ハワード（1906-1936）が1932-1936年に「Weird Tales」誌に書き継いだコナン連作。架空のヒボリアン時代を舞台に、キンメリア人傭兵コナンの剣戟冒険を描いた、ソード・アンド・ソーサリー創始作。ハワード自殺後、L・スプレイグ・ディ・キャンプ等の編集・補筆で継続出版された。",
    background="戦間期米国パルプ雑誌、ハワードのテキサス的男性的暴力美学、ローブクラフトとの書簡交流。",
    development="1982年シュワルツェネッガー映画化以降、ファンタジー文化規範化。グレイマー・モリソン等の現代再翻案で継続的に再活性化。",
    historical_context="戦間期米国パルプSF・ファンタジー誕生期。",
    primary_source_url=WIKI_EN+"Conan_the_Barbarian",
    primary_source_type="Wikipedia: Conan the Barbarian",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ムアコック『エルリック』",
    name_en="Moorcock: Elric of Melniboné",
    name_original="Elric of Melniboné",
    period_key="ジャンル多様化期",
    definition="マイケル・ムアコック（1939-）が1961年から書き継いだ反英雄エルリック・サーガ。アルビノで弱体な皇帝エルリックが魔剣ストームブリンガーに依存して旅する、ハワード『コナン』への意識的反転作。英国ニュー・ウェーブSFのファンタジー応用、Eternal Champion多元宇宙論の中核作。",
    background="1960年代英国「ニュー・ワールズ」誌時代、ムアコックの反パルプ的作家戦略、英国ニュー・ウェーブSF運動。",
    development="メタル音楽（Hawkwind、Blue Öyster Cult）、現代ダーク・ファンタジー（ジョー・アバクロンビー、ピーター・V・ブレット）へ巨大な影響を残した。",
    historical_context="1960-70年代英国ニュー・ウェーブSF・ファンタジー融合期。",
    primary_source_url=WIKI_EN+"Elric_of_Melnibon%C3%A9",
    primary_source_type="Wikipedia: Elric",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アーバン・ファンタジー",
    name_en="urban fantasy sub-genre",
    name_original="urban fantasy",
    period_key="ポップ・グローバル化期",
    definition="チャールズ・ド・リント、ニール・ゲイマン『ネバーウェア』(1996)、ジム・ブッチャー『ドレスデン・ファイル』(2000-)、ローレル・K・ハミルトン等が確立した現代ファンタジー・サブジャンル。現代都市を舞台に超自然存在（吸血鬼・狼男・魔法使い・神々）が共存する設定を共通点とする。21世紀英米大衆ファンタジー市場の主要セグメント。",
    background="1990年代以降の現代ファンタジー市場、ゴシック復活、ヴァンパイア小説市場の成熟。",
    development="2000年代TVドラマ（『バフィー』『True Blood』）、現代パラノーマル・ロマンスとの接合で巨大ジャンル化。",
    historical_context="1990-2000年代英米現代ファンタジー成熟期。",
    primary_source_url=WIKI_EN+"Urban_fantasy",
    primary_source_type="Wikipedia: Urban fantasy",
    importance_score=3, source_tier="tertiary", canonical_in_region="major")

add(**C, name_ja="ゲイマン『アメリカン・ゴッズ』",
    name_en="Gaiman: American Gods",
    name_original="American Gods",
    period_key="ポップ・グローバル化期",
    definition="ニール・ゲイマン（1960-）が2001年に発表した現代ファンタジー。米国に渡った旧世界神々と現代の新しい神々（メディア、テクノロジー）の戦争を描く神話的小説。Hugo・Nebula・Bram Stoker三冠を獲得した、21世紀ジャンル文学の規範作。著者はその他『サンドマン』漫画でも著名。",
    background="ゲイマンの英国漫画・ファンタジー出自、米国移民後の文化観察、世界神話学への著者の関心。",
    development="2017年Starzドラマ化、現代神話再話文学の規範化。",
    historical_context="2000年代英米現代ファンタジー神話系譜成熟期。",
    primary_source_url=WIKI_EN+"American_Gods",
    primary_source_type="Wikipedia: American Gods",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"神話的人類学と移民",
         "description":"アメリカン・ゴッズは移民が神々を新大陸に運ぶという神話人類学を文学化した。"}])

add(**C, name_ja="ロマンタジー（romantasy）",
    name_en="romantasy genre",
    name_original="romantasy",
    period_key="ポップ・グローバル化期",
    definition="2010年代後半-2020年代に確立されたロマンス×ファンタジーのハイブリッド・ジャンル。サラ・J・マース『茨と棘のバラ』(2015-)、レベッカ・ヤロス『フォースウィング』(2023)、ジェニファー・L・アーメントラウト等が中核作家。BookTok（TikTokの本コミュニティ）が市場形成を主導した特徴を持つ。",
    background="2010年代YA市場の成熟、パラノーマル・ロマンス系譜、TikTok・Booktok時代の出版マーケティング革新。",
    development="2023-2024年米国出版市場で爆発的成長。新しい大衆文学市場形成プロセスの研究対象となっている。",
    historical_context="2020年代SNS時代の出版ジャンル形成期。",
    primary_source_url=WIKI_EN+"Romantasy",
    primary_source_type="Wikipedia: Romantasy",
    importance_score=3, source_tier="tertiary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"TikTok時代に形成された新興ジャンル、AI生成大衆文学の市場形成研究の参照点。",
         "related_ai_phenomenon":"SNS駆動ジャンル形成のAI研究"}])

add(**C, name_ja="グリムダーク・ファンタジー",
    name_en="grimdark fantasy",
    name_original="grimdark",
    period_key="ポップ・グローバル化期",
    definition="ジョー・アバクロンビー『最初の法』、マーク・ローレンス『棘の王子』、リチャード・モーガンらが2000年代後半に確立したダーク・ファンタジー潮流。トールキン的善悪二元・英雄理想を否定し、暴力・モラル相対主義・敗北を中核に据える。マーティン『氷と炎の歌』を直接の系譜源とする。",
    background="20世紀末ファンタジー市場の英雄理想化への対抗、ムアコック反英雄系譜、Warhammer 40k暗黒未来宇宙の影響。",
    development="現代英米ファンタジー市場の主要潮流として継続。",
    historical_context="2000-2010年代英米ダーク・ファンタジー成熟期。",
    primary_source_url=WIKI_EN+"Grimdark",
    primary_source_type="Wikipedia: Grimdark",
    importance_score=2, source_tier="tertiary", canonical_in_region="marginal")

add(**C, name_ja="ラヴクラフト・コズミック・ホラー（クトゥルフ神話）",
    name_en="Lovecraft cosmic horror (Cthulhu Mythos)",
    name_original="Cthulhu Mythos",
    period_key="初期SF・パルプ期",
    definition="H.P.ラヴクラフト（1890-1937）が1920-30年代「Weird Tales」誌に発表した『クトゥルフの呼び声』(1928)、『インスマウスの影』『狂気の山脈にて』等の神話体系。人間理性を超越した宇宙的恐怖、古代神々（クトゥルフ、ニャルラトホテプ）、禁断の書『ネクロノミコン』を中核とする、20世紀ホラー・ジャンルの最大規範体系。",
    background="戦間期米国パルプ雑誌、ラヴクラフトのプロビデンス（RI）出自、ポー・マッケン継承。",
    development="オーガスト・ダーレスらによる「クトゥルフ神話」体系化、現代TRPG「クトゥルフの呼び声」(1981-)、ヴィクトル・ラヴァール・ジェマ・ジェフコート等のラヴクラフト批判的継承（人種主義批判）で再活性化。",
    historical_context="戦間期米国コズミック・ホラー誕生期。",
    primary_source_url=WIKI_EN+"Cthulhu_Mythos",
    primary_source_type="Wikipedia: Cthulhu Mythos",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="シャーリイ・ジャクスン『くじ』",
    name_en="Shirley Jackson: The Lottery",
    name_original="The Lottery",
    period_key="黄金時代・古典化期",
    definition="シャーリイ・ジャクスン（1916-1965）が1948年「ニューヨーカー」誌に発表した短編小説。米国小さな町の年中行事「くじ」が実は石打ち刑による生贄選抜だった、現実主義からの突然の暴力反転を描く。20世紀米国短編の最も衝撃的作品の一つ、『山荘奇譚』(1959)と並ぶジャクスン代表作。",
    background="戦後米国の郊外的均質性への著者の懐疑、フランク・カプラ的米国理想像への対抗、フレイザー『金枝篇』影響。",
    development="米国高校・大学文学教育の正典短編、ホラー・短編・米国南部ゴシックの規範参照点。",
    historical_context="戦後米国短編小説と社会批評の融合期。",
    primary_source_url=WIKI_EN+"The_Lottery",
    primary_source_type="Wikipedia: The Lottery",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"生贄儀礼の社会人類学",
         "description":"くじはフレイザー『金枝篇』の生贄論を米国郊外に投影した文学事例。"}])

add(**C, name_ja="キング『シャイニング』",
    name_en="King: The Shining",
    name_original="The Shining",
    period_key="ジャンル多様化期",
    definition="スティーヴン・キング（1947-）が1977年に発表した米国ホラーの規範作。冬季閉鎖されるオーバールック・ホテルで暮らす作家ジャック・トーランス家族の精神崩壊と霊的迫害を描く。20世紀後半米国ホラー・ジャンルの市民権獲得を象徴する作品で、キューブリック1980年映画化との作者対立も有名。",
    background="キング自身のアルコール依存症闘病、コロラドのスタンレー・ホテル滞在体験、20世紀後半米国心理ホラーの成熟。",
    development="1980年映画、続編『ドクター・スリープ』(2013)、2019年映画化等で持続的に規範。米国ホラー・ジャンル文学の最高規範。",
    historical_context="1970-80年代米国ホラー文学の文化的市民権獲得期。",
    primary_source_url=WIKI_EN+"The_Shining_(novel)",
    primary_source_type="Wikipedia: The Shining (novel)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バーカー『ヘルレイザー』",
    name_en="Barker: The Hellbound Heart / Hellraiser",
    name_original="The Hellbound Heart",
    period_key="ジャンル多様化期",
    definition="クライヴ・バーカー（1952-）が1986年に発表した中編『地獄の詩篇』および同著者監督1987年映画『ヘルレイザー』。パズル・ボックス「ルマルシャン」の解読がセノバイト（地獄の苦痛・快楽存在）を召喚する物語。1980年代英米「ボディ・ホラー」「ニュー・ウェイヴ・ホラー」の規範作で、痛みと快楽の倒錯的結合という主題を確立した。",
    background="1980年代英米ホラー新世代、サド的快苦倒錯、エイズ危機期のクィア・ボディ・ホラー。",
    development="ヘルレイザー・フランチャイズ（11作）として継続、現代ホラー・スプラッタパンク文学の規範参照点。",
    historical_context="1980年代英米ニュー・ウェーブ・ホラー期。",
    primary_source_url=WIKI_EN+"The_Hellbound_Heart",
    primary_source_type="Wikipedia: The Hellbound Heart",
    importance_score=2, source_tier="tertiary", canonical_in_region="marginal")


# ============================================================
# F: Romance / Graphic / Manga / Light & Web novel (8)
# ============================================================
add(**C, name_ja="ヘイヤー摂政期（リージェンシー）ロマンス",
    name_en="Heyer: Regency romance",
    name_original="Georgette Heyer Regency",
    period_key="黄金時代・古典化期",
    definition="ジョージェット・ヘイヤー（1902-1974）が1935-1972年に書いた30冊超のリージェンシー（摂政期）ロマンス。オースティン後の英国摂政時代（1811-1820）をハイブロウ・ロマンスとして再構築した独自ジャンル「リージェンシー・ロマンス」を確立し、20世紀後半の Mills & Boon、Harlequin、現代ロマンス出版市場の規範を形成した。",
    background="戦間期英国オースティン研究の進展、ヘイヤーの歴史考証主義、戦時下の現実逃避的ロマンス需要。",
    development="現代ロマンス・ジャンル全体の祖型として継続的影響。コートニー・ミラン、エロイサ・ジェイムズ等の21世紀リージェンシー作家の規範。",
    historical_context="戦間期-戦後英国ハイブロウ・ロマンス誕生期。",
    primary_source_url=WIKI_EN+"Georgette_Heyer",
    primary_source_type="Wikipedia: Georgette Heyer",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ハーレクイン・ロマンス・モデル",
    name_en="Harlequin romance publishing model",
    name_original="Harlequin",
    period_key="ジャンル多様化期",
    definition="カナダのハーレクイン社が1957年に英国Mills & Boon配給を開始し1971年買収後に確立した、定期出版・標準化筆名・厳格なジャンル規約・全世界配給網からなるロマンス出版モデル。20世紀後半-21世紀の大衆ロマンス市場を寡占し、フェミニスト批評（タニア・モドレスキー『ロマンスを愛で破壊する』1982）の主要対象となった。",
    background="戦後カナダ出版資本、Mills & Boon英国規範、20世紀後半女性向け大衆出版市場の急成長。",
    development="2010年代以降、電子書籍・自己出版による市場再編で従来モデル衰退。21世紀に多様化したロマンス出版モデルの起点として研究される。",
    historical_context="戦後北米女性向け大衆出版産業期。",
    primary_source_url=WIKI_EN+"Harlequin_Enterprises",
    primary_source_type="Wikipedia: Harlequin Enterprises",
    importance_score=3, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"標準化されたロマンス出版モデルは、AI生成大衆ロマンス文学の市場形成・倫理研究の主要参照点。",
         "related_ai_phenomenon":"AI生成大衆ロマンスの倫理"}])

add(**C, name_ja="ベクデル『ファン・ホーム』",
    name_en="Bechdel: Fun Home",
    name_original="Fun Home: A Family Tragicomic",
    period_key="ポップ・グローバル化期",
    definition="アリソン・ベクデル（1960-）が2006年に発表した自伝的グラフィック・メモワール。閉ざされたゲイの父との関係と自分自身のカミングアウトを、文学的引用（ジョイス・プルースト・ワイルド・コレット）を多層に編んで描いた、21世紀グラフィック・ノベル文学化の頂点。",
    background="ベクデルの長期作品『Dykes to Watch Out For』(1983-2008)系譜、戦後米国クィア自伝、グラフィック・ノベル文学化動向。",
    development="2015年ブロードウェイ・ミュージカル化（トニー賞）、現代米国大学英文学講義の必須テキスト、グラフィック・ノベル文学化の規範。",
    historical_context="2000年代米国グラフィック・ノベル文学化成熟期。",
    primary_source_url=WIKI_EN+"Fun_Home",
    primary_source_type="Wikipedia: Fun Home",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"自伝的詩学とクィア・テクスト",
         "description":"ファン・ホームは詩学・自伝・グラフィック・ノベルの交点として、自伝的詩学研究の重要事例。"}])

add(**C, name_ja="手塚治虫マンガ理論",
    name_en="Tezuka Osamu manga theory",
    name_original="手塚治虫",
    period_key="黄金時代・古典化期",
    definition="手塚治虫（1928-1989）が『新宝島』(1947)、『鉄腕アトム』(1952-)、『火の鳥』(1954-1988)、『ブッダ』(1972-1983)等で確立した戦後日本マンガの規範。映画的コマ割り、シネマトグラフィー的視点、ストーリーマンガの長編化、人間-非人間境界の倫理的探究を特徴とする。「マンガの神様」として戦後日本サブカルチャー全体の起点。",
    background="戦前ディズニー・アニメ・米国コミック影響、戦後日本貸本マンガ市場、手塚の医学博士号取得。",
    development="夏目房之介・伊藤剛らのマンガ表現論研究の主要対象、世界のマンガ研究（マーク・マクウィリアムス、フレデリック・ショット）の参照規範。",
    historical_context="戦後日本マンガ産業誕生期。",
    primary_source_url=WIKI_JA+"%E6%89%8B%E5%A1%9A%E6%B2%BB%E8%99%AB",
    primary_source_type="Wikipedia: 手塚治虫",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"戦後日本サブカルチャー人類学",
         "description":"手塚マンガは戦後日本サブカルチャー人類学の中核対象。"}])

add(**C, name_ja="萩尾望都・少女マンガの文学化",
    name_en="Hagio Moto / shōjo manga literarisation",
    name_original="萩尾望都",
    period_key="ジャンル多様化期",
    definition="萩尾望都（1949-）が『ポーの一族』(1972-1976)、『トーマの心臓』(1974)、『11人いる！』(1975)等で確立した、少女マンガの文学的・SF的・哲学的成熟。「24年組」（萩尾・竹宮惠子・大島弓子・山岸凉子）の中核として、戦後少女マンガを文学・SF・心理ドラマの場へ転換した。",
    background="戦前-戦後少女雑誌マンガ伝統、1970年代日本SF成熟期、ドイツ少年愛文学影響。",
    development="現代少女マンガ・BL・百合・SFマンガの規範。海外日本研究（東アジア研究、ジェンダー研究）の主要対象。",
    historical_context="1970年代日本少女マンガ文学化期。",
    primary_source_url=WIKI_JA+"%E8%90%A9%E5%B0%BE%E6%9C%9B%E9%83%BD",
    primary_source_type="Wikipedia: 萩尾望都",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"少女マンガの文学化はAI生成マンガの文化的・ジェンダー的射程の主要参照点。",
         "related_ai_phenomenon":"AI生成マンガのジェンダー文学性"}])

add(**C, name_ja="つげ義春と「ガロ」",
    name_en="Tsuge Yoshiharu and Garo magazine",
    name_original="つげ義春／ガロ",
    period_key="ジャンル多様化期",
    definition="つげ義春（1937-）が1965-1987年「ガロ」誌に発表した『ねじ式』(1968)、『紅い花』『ゲンセンカン主人』等の作品群。シュルレアリスム・私小説・夢日記を融合した日本マンガ最高峰の文学的成熟を体現する。「ガロ」誌は長井勝一が1964年創刊した、日本マンガ唯一のオルタナティブ専門誌として、戦後日本マンガの文学的地下水脈を形成した。",
    background="1960年代日本貸本マンガ系譜、シュルレアリスム影響、戦後日本オルタナティブ表現運動。",
    development="フランス、欧米マンガ翻訳でつげ義春は最も翻訳された日本作家の一人となり、世界のオルタナティブ・コミックスの規範参照点となった。",
    historical_context="1960-70年代日本オルタナティブ・マンガ運動期。",
    primary_source_url=WIKI_JA+"%E3%81%A4%E3%81%92%E7%BE%A9%E6%98%A5",
    primary_source_type="Wikipedia: つげ義春",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="日本ライトノベルのジャンル理論",
    name_en="Japanese light novel genre theory",
    name_original="ライトノベル",
    period_key="ポップ・グローバル化期",
    definition="角川スニーカー文庫(1988)、電撃文庫(1993)を起点に、東浩紀『動物化するポストモダン』(2001)・大塚英志のキャラクター小説論で理論化された日本独自の若年向け小説ジャンル。アニメ調挿絵、キャラクター先行物語、データベース消費構造、Web小説起源（『ソードアート・オンライン』2002 Web→2009 書籍）を特徴とする。",
    background="1980-90年代日本オタク文化成熟、ジュブナイル・SF系譜、JK時代の若年向け出版需要。",
    development="2010年代「なろう系」（小説家になろう投稿サイト起源作品）が市場主流化。世界翻訳市場・アニメ化を通じグローバル日本サブカルチャーの中核となった。",
    historical_context="1990-2010年代日本若年向け出版市場期。",
    primary_source_url=WIKI_JA+"%E3%83%A9%E3%82%A4%E3%83%88%E3%83%8E%E3%83%99%E3%83%AB",
    primary_source_type="Wikipedia: ライトノベル",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"Web小説起源・データベース消費・キャラクター先行物語の構造はAI生成小説の構造と同型として研究される。",
         "related_ai_phenomenon":"AI生成小説とデータベース消費"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"東浩紀データベース消費論",
         "description":"ライトノベルは東浩紀『動物化するポストモダン』のデータベース消費論の中核対象。"}])

add(**C, name_ja="Web小説と「なろう系」",
    name_en="Web novel and 'narō-kei'",
    name_original="Web小説／なろう系",
    period_key="ポップ・グローバル化期",
    definition="2004年「小説家になろう」投稿サイト（ヒナプロジェクト）開設以降確立された、Web投稿起源の日本小説ジャンル。異世界転生・チート・ハーレム等の定型構造、Web上でのトレンド-投稿-書籍化-アニメ化のメディアミックス循環、テンプレート消費を特徴とし、2010年代以降日本ライトノベル市場の主流となった。中国「網絡文学」、英語圏「Royal Road」と並ぶ世界Web文学のローカル形態。",
    background="2000年代日本Web 2.0、PC・携帯小説プラットフォーム、ライトノベル市場のWeb化。",
    development="海外翻訳サイト（Wuxiaworld、Novel Updates）経由のグローバル波及、AI翻訳・AI生成小説と接続する21世紀文学プラットフォームの規範事例。",
    historical_context="2000年代-現代日本Web小説プラットフォーム期。",
    primary_source_url=WIKI_JA+"%E5%B0%8F%E8%AA%AC%E5%AE%B6%E3%81%AB%E3%81%AA%E3%82%8D%E3%81%86",
    primary_source_type="Wikipedia: 小説家になろう",
    importance_score=3, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"Web小説プラットフォームはAI生成小説の市場・倫理研究の最重要参照点。",
         "related_ai_phenomenon":"Web投稿プラットフォームでのAI生成小説"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"プラットフォーム文学の人類学",
         "description":"なろう系はオンライン創作コミュニティの文学的人類学の主要対象。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="周縁横断",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc or None)
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
        print(f"[c33-add60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c33-add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        print(f"[c33-add60] CONCEPTS list size: {len(CONCEPTS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
