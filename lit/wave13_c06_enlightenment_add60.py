"""LIT-DB Phase 2 Wave 13 — C06: Enlightenment / Romanticism ADD 60.

Subfield: lit_eu_enlightenment (id=4).
Existing: 80 (Wave 7 covered Enlightenment + Romanticism core).
This wave: ADD 60 NEW covering French/British 18c, German Klassik,
Romantic poetry (EN/DE/RU), American Romanticism, Latin American /
Italian / Spanish Romantic.

Sources: Project Gutenberg, Wikisource (en/fr/de/it/es/ru), Frantext,
BVMC, archive.org. Primary >= 85%.

Targets: fourth_transform_tags >= 18, cross_domain to PT/PHIL >= 14.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("18世紀フランス啓蒙拡張期", "French Enlightenment Expanded (18th c.)",
     1715, 1789,
     "摂政期から大革命前夜までのフランス文学。ディドロ、ルソー、ヴォルテール、マリヴォー、プレヴォ、ボーマルシェ、ラクロ、サド、レチフを擁する啓蒙散文・劇作の成熟期。"),
    ("18世紀英国小説興隆期", "British 18th-century Novel",
     1700, 1800,
     "デフォー、リチャードソン、フィールディング、スターン、スモレット、バーニー、ラドクリフ、ウォルポール、ルイスを擁する英国小説の興隆とゴシック小説の確立期。"),
    ("ドイツ・シュトゥルム・ウント・ドラング期", "German Sturm und Drang / Klassik",
     1760, 1830,
     "レッシング、ヘルダー、ゲーテ、シラー、ヘルダーリン、ジャン・パウル、ヴィーラント、モーリッツを擁する疾風怒濤期からヴァイマル古典主義・ロマン派初期。"),
    ("英国ロマン主義詩期", "British Romantic Poetry",
     1780, 1840,
     "ワーズワース、コールリッジ、ブレイク、キーツ、シェリー、バイロンを擁する英国ロマン主義詩の中核期。"),
    ("ドイツ・ロマン派期", "German Romanticism",
     1795, 1840,
     "ノヴァーリス、ティーク、ブレンターノ、アイヒェンドルフ、E.T.A.ホフマンを擁するイエナ・ハイデルベルク・ベルリン・ロマン派の連続期。"),
    ("ロシア・ロマン主義期", "Russian Romanticism",
     1815, 1845,
     "プーシキン、レールモントフ、ゴーゴリを中心とするロシア近代文学黄金期初頭。"),
    ("米国ロマン主義期", "American Romanticism",
     1820, 1865,
     "ホーソーン、メルヴィル、ポー、エマソン、ソロー、ホイットマン、ディキンソンを擁するアメリカン・ルネサンス期。"),
    ("ラテンアメリカ・ロマン主義期", "Latin American Romanticism",
     1830, 1890,
     "エチェベリーア、イサークスを擁する独立後ラテンアメリカのロマン主義文学期。"),
    ("イタリア・スペイン・ロマン主義期", "Italian / Spanish Romanticism",
     1815, 1870,
     "マンゾーニ、レオパルディ、ベッケル、ラーラを擁する南欧ロマン主義期。"),
]


GUTEN = "https://www.gutenberg.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WIKI_IT = "https://it.wikipedia.org/wiki/"
WIKI_ES = "https://es.wikipedia.org/wiki/"
WIKI_RU = "https://ru.wikipedia.org/wiki/"
WSRC_FR = "https://fr.wikisource.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
WSRC_DE = "https://de.wikisource.org/wiki/"
WSRC_IT = "https://it.wikisource.org/wiki/"
WSRC_ES = "https://es.wikisource.org/wiki/"
WSRC_RU = "https://ru.wikisource.org/wiki/"
ARCH = "https://archive.org/details/"
BVMC = "https://www.cervantesvirtual.com/"
FRANTEXT = "https://www.frantext.fr/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_eu_enlightenment", region="西欧",
         original_script="roman")
CRU = dict(subfield_code="lit_eu_enlightenment", region="ロシア",
           original_script="cyrillic")
CAM = dict(subfield_code="lit_eu_enlightenment", region="米国",
           original_script="roman")
CLA = dict(subfield_code="lit_eu_enlightenment", region="ラテンアメリカ",
           original_script="roman")


# ============================================================
# A: French Enlightenment Expanded (10)
# ============================================================
add(**C, name_ja="ディドロ『百科全書』文学項目",
    name_en="Diderot's Encyclopédie literary articles",
    name_original="Encyclopédie",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ドゥニ・ディドロ（1713-1784）とジャン・ル・ロン・ダランベールが編集した『百科全書、または科学・芸術・職業の理論的辞典』(1751-72)所収の文学関連項目群。「ENCYCLOPÉDIE」「BEAU」「GENIE」「IMITATION」「IMAGINATION」等の項目で、啓蒙期の美学・詩学観を体系的に提示し、18世紀フランス啓蒙文学観の理論的中核を成した。",
    background="アカデミー・フランセーズ系統の規範主義詩学への対抗、ベーコン的経験主義知識分類の文学への適用。",
    development="19世紀ロマン主義詩学および文学百科事典類の祖型となり、ヴォルテール『哲学辞典』と並んで啓蒙的批評形式の原型となった。",
    historical_context="1751-72年フランスにおける検閲・宗教統制と知の世俗化運動。",
    primary_source_url=ARCH+"encyclopdieoudic01didegoog",
    primary_source_type="archive.org: Encyclopédie",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"啓蒙百科事典主義",
         "description":"ディドロ百科全書は啓蒙哲学と文学批評を統合した知識体系として、哲学DB側の啓蒙項目と直接対応する。"}])

add(**C, name_ja="ルソー『エミール』",
    name_en="Rousseau's Émile, ou De l'éducation",
    name_original="Émile, ou De l'éducation",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ジャン=ジャック・ルソー（1712-1778）が1762年に発表した教育論を兼ねた哲学小説。架空の少年エミールの誕生から結婚までの教育過程を5巻にわたって叙述し、第4巻「サヴォア司祭の信仰告白」では自然宗教を提示した。発表後パリ高等法院・ジュネーブで焚書処分を受けた。教育思想史と18世紀小説形式を統合した独自のジャンルを成す。",
    background="ロック『教育論』(1693)以降の近代教育論の系譜と、ルソーの自然状態論の応用。",
    development="ペスタロッチ、フレーベル、19-20世紀児童中心主義教育論の祖となり、教養小説（Bildungsroman）の哲学的祖型として機能した。",
    historical_context="アンシャン・レジーム期フランスの宗教的検閲下における自然宗教論議。",
    primary_source_url=GUTEN+"ebooks/30433",
    primary_source_type="Project Gutenberg: Émile",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"『エミール』は教育による主体形成を理念化する。AIによる学習・主体形成プロセスとの対比で、自然主義的人間形成論の意義を再検討する基準点。",
         "related_ai_phenomenon":"AI学習プロセスと自然主義的教育論の対比"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"自然教育・自然宗教",
         "description":"『エミール』はルソー哲学（自然状態論・社会契約論）の文学的具体化として、哲学DBと直接接続する。"}])

add(**C, name_ja="ルソー『孤独な散歩者の夢想』",
    name_en="Rousseau's Reveries of a Solitary Walker",
    name_original="Les Rêveries du promeneur solitaire",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ルソー晩年の遺作（執筆1776-78、刊行1782）。10の「散歩」から成る自伝的瞑想録で、孤独・自然・記憶・死を主題とする。『告白』『対話』に続く自伝三部作の最終巻として、近代自伝文学および散文詩的瞑想録の祖型を成し、ロマン主義的内省散文の出発点となった。",
    background="晩年の社会的孤立と被害妄想期、自伝的執筆実践の継続。",
    development="シャトーブリアン『墓の彼方からの回想』、ロマン主義散文詩、19-20世紀自伝文学に深い影響を与えた。",
    historical_context="ルソー晩年（1770年代）のパリ近郊での隠遁生活。",
    primary_source_url=GUTEN+"ebooks/4267",
    primary_source_type="Project Gutenberg: Les Rêveries",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マリヴォーのマリヴォダージュ",
    name_en="Marivaux's marivaudage",
    name_original="marivaudage",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ピエール・ド・マリヴォー（1688-1763）の劇作・小説に見られる繊細な心理分析と機知に富む対話様式。『愛と偶然との戯れ』(1730)、『マリアンヌの生涯』(1731-41)に代表される。18世紀フランス劇および小説の心理的精緻化を象徴する文体カテゴリで、19世紀以後「マリヴォダージュ」として批評的固有名詞化した。",
    background="レジャンス期サロン文化の機知会話と、フランス古典悲劇後の喜劇形式の刷新。",
    development="後の心理小説（ラディゲ、プルースト）に文体的影響を残し、19-20世紀フランス批評の文体カテゴリとなった。",
    historical_context="摂政期から路易15世前期パリのサロン社交文化。",
    primary_source_url=GUTEN+"ebooks/12862",
    primary_source_type="Project Gutenberg: Marivaux works",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="プレヴォ『マノン・レスコー』",
    name_en="Prévost's Manon Lescaut",
    name_original="Histoire du chevalier Des Grieux et de Manon Lescaut",
    period_key="18世紀フランス啓蒙拡張期",
    definition="アベ・プレヴォ（1697-1763）が1731年に発表した中編小説。シュヴァリエ・デ・グリューと不実な恋人マノン・レスコーの破滅的恋愛を一人称回想形式で描く。フランス18世紀情念小説の祖型で、プッチーニ・マスネのオペラ化を経て19-20世紀にかけて世界的影響を持つ古典となった。",
    background="リバティナージュ文学と感傷文学の交錯、18世紀英仏小説交流。",
    development="フローベール『ボヴァリー夫人』、デュマ『椿姫』、19世紀情念小説の祖型となった。",
    historical_context="摂政期パリの新興ブルジョワ・娼婦・流刑制度の社会的現実。",
    primary_source_url=GUTEN+"ebooks/468",
    primary_source_type="Project Gutenberg: Manon Lescaut",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ボーマルシェ『フィガロの結婚』",
    name_en="Beaumarchais's Le Mariage de Figaro",
    name_original="La Folle journée, ou Le Mariage de Figaro",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ピエール・オーギュスタン・カロン・ド・ボーマルシェ（1732-1799）が執筆し1784年に上演された喜劇。下僕フィガロが伯爵の初夜権要求を機知で打ち破る筋書きで、貴族特権を風刺的に解体した。フランス革命前夜の社会的緊張を文学的に体現し、モーツァルト=ダ・ポンテのオペラ（1786）化により世界古典となった。",
    background="路易16世期の検閲と上演禁止運動、第三身分の社会的台頭。",
    development="フランス革命直前のイデオロギー的影響、19世紀社会風刺劇への系譜的影響を与えた。",
    historical_context="1784年上演前の3年余の上演禁止と、それを覆した世論の革命前夜性。",
    primary_source_url=GUTEN+"ebooks/20577",
    primary_source_type="Project Gutenberg: Le Mariage de Figaro",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ラクロ『危険な関係』",
    name_en="Laclos's Les Liaisons dangereuses",
    name_original="Les Liaisons dangereuses",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ピエール・コデルロス・ド・ラクロ（1741-1803）が1782年に発表した書簡体小説。メルトイユ侯爵夫人とヴァルモン子爵による恋愛操作の往復書簡で構成され、リバティナージュ的官能と冷徹な心理分析を統合した18世紀後期フランス小説の頂点。革命前夜の貴族モラルの解体を体現する作品として古典化した。",
    background="リチャードソン書簡体小説の仏受容、ロココ期リバティナージュ文学の到達点。",
    development="バルザック・スタンダールの心理リアリズムへ橋渡しされ、20世紀映画化（1988、1989）を通じて世界古典となった。",
    historical_context="1782年フランス、革命前夜のアンシャン・レジーム貴族文化の道徳的崩壊期。",
    primary_source_url=GUTEN+"ebooks/13965",
    primary_source_type="Project Gutenberg: Les Liaisons dangereuses",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="サドの哲学小説",
    name_en="Sade's philosophical novel",
    name_original="roman philosophique sadien",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ドナティアン・アルフォンス・フランソワ・ド・サド（1740-1814）が獄中で執筆した『ジュスティーヌ』(1791)、『ジュリエット』(1797-1801)、『ソドム百二十日』（1785草稿）を中心とする哲学小説群。リバティナージュ哲学と暴力描写を組み合わせ、啓蒙期理性主義の暗部を体現する。20世紀以降バタイユ、ブランショ、フーコー、バルトの読解で再評価された。",
    background="獄中生活、リバティナージュ伝統、唯物論的啓蒙哲学（ドルバック、ラ・メトリ）の極限化。",
    development="20世紀フランス批評（バタイユ『エロティシズム』、ブランショ『ロートレアモンとサド』）、ラカン派精神分析の中心参照点となった。",
    historical_context="アンシャン・レジーム末期から大革命・ナポレオン期にかけての監獄文学。",
    primary_source_url=WSRC_FR+"Auteur:Donatien_Alphonse_Fran%C3%A7ois_de_Sade",
    primary_source_type="Wikisource FR: Sade",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"啓蒙の弁証法",
         "description":"サドの哲学小説はホルクハイマー=アドルノ『啓蒙の弁証法』のサド章を通じて、啓蒙理性の暗部理論の中心参照点となった。"}])

add(**C, name_ja="レチフ・ド・ラ・ブルトンヌの自伝小説",
    name_en="Restif de la Bretonne's autobiographical novel",
    name_original="Monsieur Nicolas",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ニコラ・エドム・レチフ・ド・ラ・ブルトンヌ（1734-1806）が1794-97年に発表した自伝『ムッシュー・ニコラ、または明かされた人間心情』全16巻。ルソー『告白』に応答する詳細な自伝を、18世紀末パリの民衆生活描写と結びつけた。後の自然主義作家（ゾラ）に先駆ける都市民俗誌的方法を用い、18世紀フランス自伝・社会観察文学の独自系譜を成す。",
    background="ルソー自伝形式の継承、18世紀パリ民衆文学・出版文化の興隆。",
    development="後のフランス自然主義（ゾラ、ユイスマンス）の都市観察方法に先駆け、19-20世紀パリ民俗誌的文学の祖型となった。",
    historical_context="フランス革命期から総裁政府・統領政府期にかけてのパリ民衆生活。",
    primary_source_url=GUTEN+"author/3290",
    primary_source_type="Project Gutenberg: Restif de la Bretonne",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ヴォルテール『カンディード』批評受容",
    name_en="Voltaire's Candide reception",
    name_original="Candide ou l'Optimisme — réception",
    period_key="18世紀フランス啓蒙拡張期",
    definition="ヴォルテール（1694-1778）の哲学コント『カンディード』(1759)の18-21世紀批評受容史。ライプニッツ的楽観主義への風刺、リスボン地震(1755)への文学的応答、終結部「我々の畑を耕すべし」をめぐる解釈論争の集積。啓蒙期文学の最も読まれる古典の一つとして、批評史自体が研究対象化されている。",
    background="リスボン地震への神学的論議、ライプニッツ『弁神論』への論争。",
    development="20世紀バルト記号論、現代啓蒙論争（ホルクハイマー、ハーバーマス、トドロフ）における中心参照テクスト。",
    historical_context="七年戦争期(1756-63)とリスボン地震後の啓蒙的悲観主義論議。",
    primary_source_url=GUTEN+"ebooks/4650",
    primary_source_type="Project Gutenberg: Candide",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"楽観主義論争",
         "description":"『カンディード』はライプニッツ楽観主義論争の文学的中核として、哲学DB側の弁神論項目と直接対応する。"}])


# ============================================================
# B: British 18th-century Novel (10)
# ============================================================
add(**C, name_ja="デフォー『モル・フランダース』",
    name_en="Defoe's Moll Flanders",
    name_original="The Fortunes and Misfortunes of the Famous Moll Flanders",
    period_key="18世紀英国小説興隆期",
    definition="デフォーが1722年に発表した擬似自伝小説。窃盗・売春・植民地での再生に至る女性主人公モルの一人称回想録。18世紀英国小説の主要起源の一つで、女性主人公・犯罪伝記・植民地経験の三要素を統合した。20世紀フェミニズム批評・経済史的読解の中心テクストとなった。",
    background="17世紀末犯罪伝記文学、18世紀初頭英国の植民地化と女性労働問題。",
    development="リチャードソン『パメラ』、19世紀社会小説、20世紀フェミニズム批評（イアン・ワット、サンドラ・ギルバート）に重要な参照点を提供した。",
    historical_context="ジョージ朝初期英国の社会階層流動・植民地犯罪流刑制度。",
    primary_source_url=GUTEN+"ebooks/370",
    primary_source_type="Project Gutenberg: Moll Flanders",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="リチャードソン『パメラ』",
    name_en="Richardson's Pamela",
    name_original="Pamela; or, Virtue Rewarded",
    period_key="18世紀英国小説興隆期",
    definition="サミュエル・リチャードソン（1689-1761）が1740年に発表した書簡体小説。下女パメラが主人B氏の誘惑に貞節で抵抗し最終的に結婚する物語。英国近代小説確立の決定的瞬間とされ、出版直後に一大流行を起こし、フィールディング『シャミラ』『ジョセフ・アンドルーズ』等のパロディと反作品を誘発した。",
    background="ピューリタン的道徳論議、18世紀英国出版文化の興隆と中流読者層の拡大。",
    development="ルソー『新エロイーズ』、ゲーテ『ウェルテル』、書簡体小説伝統の起源、現代英国小説論（イアン・ワット『小説の興起』1957）の中心テクスト。",
    historical_context="1740年代英国の道徳的・性的論争、女性読者層の文学市場参入期。",
    primary_source_url=GUTEN+"ebooks/6124",
    primary_source_type="Project Gutenberg: Pamela",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="リチャードソン『クラリッサ』",
    name_en="Richardson's Clarissa",
    name_original="Clarissa, or the History of a Young Lady",
    period_key="18世紀英国小説興隆期",
    definition="リチャードソンが1747-48年に発表した書簡体小説。約100万語にのぼる英語圏で最も長い古典小説の一つ。誘拐・薬物・強姦を経て死に至るクラリッサ・ハーロウの悲劇を、複数視点の書簡で構成する。18世紀心理リアリズムの頂点で、サド、ディドロ、フロイトに重要な参照を与えた。",
    background="『パメラ』の成功後、書簡体小説形式の野心的拡張、英国貴族・ジェントリー階級の家父長制問題化。",
    development="ディドロ『リチャードソン頌』、ルソー『新エロイーズ』、20世紀心理小説論・フェミニズム批評の中心研究対象。",
    historical_context="1740年代英国における女性財産権・結婚法・家父長制論議。",
    primary_source_url=GUTEN+"ebooks/9296",
    primary_source_type="Project Gutenberg: Clarissa",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"『クラリッサ』は書簡体による複数主体の意識ポリフォニーを実現する。AI時代の多主体テクスト生成（複数ペルソナ並列生成）を理論化する古典的祖型として再読される。",
         "related_ai_phenomenon":"AI多主体並列生成と書簡体の比較"}])

add(**C, name_ja="フィールディング『トム・ジョーンズ』",
    name_en="Fielding's Tom Jones",
    name_original="The History of Tom Jones, a Foundling",
    period_key="18世紀英国小説興隆期",
    definition="ヘンリー・フィールディング（1707-1754）が1749年に発表した長編小説。捨て子トム・ジョーンズの冒険・恋愛・出自判明を、自意識的な作家介入と古典叙事詩風の構成で描く。リチャードソン書簡体小説への対抗として「散文による喜劇的叙事詩」を提唱し、英国小説の二大系譜の一翼を成した。",
    background="リチャードソン心理書簡体への喜劇的反作用、英国古典学的（ホメロス・ウェルギリウス・セルバンテス）小説論の精緻化。",
    development="ディケンズ『デイヴィッド・コパフィールド』、サッカレー『虚栄の市』、19世紀英国全知視点リアリズム小説の祖型。",
    historical_context="1745年ジャコバイト反乱直後の英国社会の文学的反映。",
    primary_source_url=GUTEN+"ebooks/6593",
    primary_source_type="Project Gutenberg: Tom Jones",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="フィールディング『ジョセフ・アンドルーズ』",
    name_en="Fielding's Joseph Andrews",
    name_original="The History of the Adventures of Joseph Andrews",
    period_key="18世紀英国小説興隆期",
    definition="フィールディングが1742年に発表した小説。リチャードソン『パメラ』のパロディとして開始され、パメラの兄ジョセフを主人公に据えた。前書「散文による喜劇的叙事詩」で英国小説論の重要な理論化を行い、フィールディング小説論の出発点となった。",
    background="『シャミラ』(1741)に続くリチャードソン批判、古典叙事詩理論の散文小説への適用。",
    development="『トム・ジョーンズ』『アミリア』に続く小説論の発展、英国小説論ジャンルの確立。",
    historical_context="1740年代英国の「パメラ熱狂」と批判運動。",
    primary_source_url=GUTEN+"ebooks/9611",
    primary_source_type="Project Gutenberg: Joseph Andrews",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スターン『トリストラム・シャンディ』",
    name_en="Sterne's Tristram Shandy",
    name_original="The Life and Opinions of Tristram Shandy, Gentleman",
    period_key="18世紀英国小説興隆期",
    definition="ローレンス・スターン（1713-1768）が1759-67年に発表した9巻の小説。主人公の誕生にすら最後まで到達しない自意識的脱線・印刷上の遊戯（白頁・黒頁・大理石模様頁）に満ちた前衛的形式で、18世紀小説の方法的限界を踏破した。20世紀モダニズム・ポストモダニズム小説の祖型として再評価された。",
    background="ロック『人間悟性論』(1690)の連想理論の小説への応用、ラブレー・セルバンテスからの脱線伝統の継承。",
    development="ジョイス『ユリシーズ』、ヴァージニア・ウルフ、ボルヘス、ロシア・フォルマリズム（シュクロフスキー『散文の理論』1925）の中心研究対象となった。",
    historical_context="1760年代英国の出版文化と読書実践の多様化。",
    primary_source_url=GUTEN+"ebooks/1079",
    primary_source_type="Project Gutenberg: Tristram Shandy",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"形式","status":"rethinking",
         "rationale":"『トリストラム・シャンディ』は脱線・余談・印刷的遊戯による物語形式の脱構築を達成する。AI生成の非線形・断片的テクストの理論的祖型として再読される。",
         "related_ai_phenomenon":"AI生成の非線形テクストと自意識的形式"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"脱線・自意識的物語",
         "description":"『トリストラム・シャンディ』はシュクロフスキー以来のロシア・フォルマリズム物語論の中心研究対象であり、現代ナラトロジーと直接接続する。"}])

add(**C, name_ja="バーニー『エヴェリーナ』",
    name_en="Burney's Evelina",
    name_original="Evelina, or the History of a Young Lady's Entrance into the World",
    period_key="18世紀英国小説興隆期",
    definition="ファニー（フランシス）・バーニー（1752-1840）が1778年に匿名発表した書簡体小説。地方育ちの娘エヴェリーナのロンドン社交界進出を描く。リチャードソン書簡体伝統と社交描写を統合し、ジェイン・オースティンへ橋渡しする18世紀後期英国女性小説家の代表作となった。",
    background="18世紀後期英国における女性作家の制度的台頭、ロンドン社交季節の文学化。",
    development="バーニー後期作品『セシリア』(1782)、『カミラ』(1796)、ジェイン・オースティン作品（『高慢と偏見』タイトルが『セシリア』結尾に由来）への直接的影響。",
    historical_context="1770年代英国における女性出版・読書文化の制度化期。",
    primary_source_url=GUTEN+"ebooks/4276",
    primary_source_type="Project Gutenberg: Evelina",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ラドクリフ『ユードルフォの謎』",
    name_en="Radcliffe's The Mysteries of Udolpho",
    name_original="The Mysteries of Udolpho",
    period_key="18世紀英国小説興隆期",
    definition="アン・ラドクリフ（1764-1823）が1794年に発表した小説。イタリア・アペニン山中の城を舞台に女性主人公エミリーが超自然的恐怖と人間悪に直面する物語。「説明されたゴシック」と呼ばれる手法で、超自然事象を最終的に合理的に解明する点が特徴。後期ゴシック小説の規範を確立した。",
    background="ウォルポール『オトラント城』以降のゴシック小説伝統、フランス革命期英国のヨーロッパ大陸への文学的視線。",
    development="ジェイン・オースティン『ノーサンガー・アビー』のパロディ対象、ヴィクトリア朝センセーション小説、19世紀後期ゴシック復興の祖型となった。",
    historical_context="1790年代英国における革命期不安とゴシック小説市場拡大。",
    primary_source_url=GUTEN+"ebooks/3268",
    primary_source_type="Project Gutenberg: The Mysteries of Udolpho",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ウォルポール『オトラント城』",
    name_en="Walpole's The Castle of Otranto",
    name_original="The Castle of Otranto",
    period_key="18世紀英国小説興隆期",
    definition="ホレス・ウォルポール（1717-1797）が1764年に匿名発表した小説。第二版(1765)で「ゴシック物語（A Gothic Story）」の副題を付したことで、ゴシック小説サブジャンルの命名起源となった。中世イタリアの城を舞台にした超自然的恐怖譚で、18世紀末から19世紀ゴシック小説運動の制度的出発点。",
    background="18世紀中葉英国の中世復興趣味、ストロベリー・ヒルでのウォルポールのゴシック建築実践。",
    development="ベックフォード、ラドクリフ、ルイス、メアリー・シェリー、ポー、ホーソーンを経て、ヴィクトリア朝ゴシックから20世紀ホラー小説に直接連なる。",
    historical_context="18世紀中葉英国の趣味（taste）論議とゴシック・リバイバル運動。",
    primary_source_url=GUTEN+"ebooks/696",
    primary_source_type="Project Gutenberg: The Castle of Otranto",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# C: German Sturm und Drang / Klassik (8)
# ============================================================
add(**C, name_ja="ヘルダー民謡集",
    name_en="Herder's Folksongs",
    name_original="Stimmen der Völker in Liedern",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="ヨハン・ゴットフリート・ヘルダー（1744-1803）が1778-79年に編纂した世界各民族の民謡集。後継版で『諸民族の声、歌における』(1807)として再刊。民謡を「民族（Volk）」の根源的詩的表現として理論化し、18世紀末から19世紀ヨーロッパの民俗学・国民文学運動・浪漫派詩学の理論的出発点となった。",
    background="マクファーソン『オシアン』(1760-65)、パーシー『古代英詩拾遺』(1765)による民俗詩関心の興隆。",
    development="グリム兄弟『子供と家庭の童話集』(1812-15)、グリム『ドイツ神話学』(1835)、19世紀各国の民俗学・国民文学運動の祖型となった。",
    historical_context="七年戦争後ドイツの国民文化形成期、ハーマン経由の啓蒙批判運動。",
    primary_source_url=WSRC_DE+"Stimmen_der_V%C3%B6lker_in_Liedern",
    primary_source_type="Wikisource DE: Stimmen der Völker",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ヘルダー民族精神論",
         "description":"ヘルダー民謡論はヘルダー歴史哲学（『人類史の哲学考』）の文学的具体化として、哲学DBの民族精神項目と直接接続する。"}])

add(**C, name_ja="ゲーテ『ヴィルヘルム・マイスターの修業時代』",
    name_en="Goethe's Wilhelm Meister's Apprenticeship",
    name_original="Wilhelm Meisters Lehrjahre",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="ヨハン・ヴォルフガング・フォン・ゲーテ（1749-1832）が1795-96年に発表した長編小説。商人の息子ヴィルヘルムの劇団遍歴・社会経験・自己形成過程を描き、教養小説（Bildungsroman）ジャンルの規範作品となった。シラーとの書簡対話の中で執筆され、ヴァイマル古典主義の小説形式の頂点。",
    background="ロココ小説、英国小説（フィールディング、ステルン、ヴィーラント仲介）、ヴァイマル古典主義詩学。",
    development="ノヴァーリス『ハインリヒ・フォン・オフターディンゲン』、ケラー『緑のハインリヒ』、トーマス・マン『魔の山』、20世紀教養小説論の中心テクスト。",
    historical_context="1790年代ヴァイマル古典主義期、フランス革命を視野に入れた近代主体形成論議。",
    primary_source_url=GUTEN+"ebooks/2335",
    primary_source_type="Project Gutenberg: Wilhelm Meisters Lehrjahre",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"『ヴィルヘルム・マイスター』は近代教養主体の理念を文学的に確立する。AI時代における個人形成・キャリア形成のあり方を再考する古典的参照点。",
         "related_ai_phenomenon":"AI時代の主体形成論と教養小説"}])

add(**C, name_ja="ゲーテ『ファウスト』第一部",
    name_en="Goethe's Faust Part I",
    name_original="Faust. Eine Tragödie. Erster Teil",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="ゲーテが1808年に発表した戯曲『ファウスト』第一部。学者ファウストとメフィストフェレスの契約、グレートヒェン悲劇を中核とする。シュトゥルム・ウント・ドラング期から執筆を開始し、ヴァイマル古典主義期に第一部を完成、晩年に第二部(1832)を完結した。ドイツ文学の最高峰として世界文学史の中心テクスト。",
    background="16世紀ファウスト民間伝承、マーロウ『ファウスタス博士』、シュトゥルム・ウント・ドラング期の独自構想。",
    development="第二部、19-20世紀世界文学への深い影響、トーマス・マン『ファウストゥス博士』(1947)を経て20世紀芸術家小説論の中心参照点。",
    historical_context="フランス革命期からナポレオン期、神聖ローマ帝国解体期のドイツ文化。",
    primary_source_url=GUTEN+"ebooks/14591",
    primary_source_type="Project Gutenberg: Faust I",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ゲーテ『ファウスト』第二部",
    name_en="Goethe's Faust Part II",
    name_original="Faust. Der Tragödie zweiter Teil",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="ゲーテが1832年に死後発表された『ファウスト』第二部。古典ヴァルプルギスの夜、ヘレナとの結婚、土地干拓事業、ファウストの救済を描く5幕構成。古典主義・ロマン主義・象徴主義を統合した晩年ゲーテの総合的作品で、20世紀シュペングラー、ベンヤミン、ブレヒトの「現代性」論議の中心参照点となった。",
    background="ヴァイマル古典主義成熟期から晩年期にわたる60年間の構想期間。",
    development="トーマス・マン、シュタイナー、ベンヤミン、20世紀ファウスト論議の中心テクスト。マーシャル・バーマン『現代性とは何か』(1982)で開発主義主体論として再読された。",
    historical_context="1830年フランス七月革命前後のヨーロッパ近代化期、産業化前夜のドイツ。",
    primary_source_url=GUTEN+"ebooks/21000",
    primary_source_type="Project Gutenberg: Faust II",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="シラーの理念劇",
    name_en="Schiller's idealist drama",
    name_original="Schillers Ideendrama",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="フリードリヒ・シラー（1759-1805）が『群盗』(1781)から『ヴァレンシュタイン』三部作(1798-99)、『マリア・ストゥアルト』(1800)、『ヴィルヘルム・テル』(1804)に展開した古典悲劇形式。歴史的素材を通じて自由・道徳・崇高の理念を演劇化し、ヴァイマル古典主義劇の規範を確立した。19世紀ドイツ国民劇の理論的支柱。",
    background="シュトゥルム・ウント・ドラング期の急進的反抗劇から、カント哲学受容を経たヴァイマル古典主義への転換。",
    development="ヘーゲル『美学』の悲劇論、19世紀ドイツ国民劇、ブレヒト『大胆な母とその子供たち』までドイツ劇文学の理論的源泉。",
    historical_context="フランス革命とナポレオン期ヨーロッパ、神聖ローマ帝国解体期。",
    primary_source_url=GUTEN+"author/759",
    primary_source_type="Project Gutenberg: Schiller works",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"カント美学・崇高論",
         "description":"シラー『美的教育論』は理念劇の哲学的基礎であり、カント『判断力批判』と直接接続する。"}])

add(**C, name_ja="ヘルダーリン『ヒュペーリオン』",
    name_en="Hölderlin's Hyperion",
    name_original="Hyperion oder Der Eremit in Griechenland",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="フリードリヒ・ヘルダーリン（1770-1843）が1797-99年に発表した書簡体小説。近代ギリシアの青年ヒュペーリオンの革命的希望と幻滅を、ピンダロス的散文詩語で描く。ドイツ・ロマン主義の哲学的散文の頂点で、20世紀ハイデガー、ベンヤミン、ガダマーのヘルダーリン論の中心テクスト。",
    background="テュービンゲン神学校でヘーゲル・シェリングと共有した汎神論的思想、フランス革命の幻滅期。",
    development="20世紀のハイデガー『ヘルダーリンの詩の解明』、ベンヤミンの初期ヘルダーリン論など、現代詩学・哲学の中心研究対象となった。",
    historical_context="1790年代後半の革命幻滅期と汎神論論議。",
    primary_source_url=GUTEN+"ebooks/6342",
    primary_source_type="Project Gutenberg: Hyperion",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ヘルダーリン受容（ハイデガー）",
         "description":"ヘルダーリン『ヒュペーリオン』はハイデガー後期哲学の中心参照点であり、哲学DB側の存在論項目と直接接続する。"}])

add(**C, name_ja="ジャン・パウルの幽默小説",
    name_en="Jean Paul's humoristic novel",
    name_original="Jean Pauls humoristischer Roman",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="ジャン・パウル（ヨハン・パウル・フリードリヒ・リヒター、1763-1825）が『ヘスペルス』(1795)、『ティタン』(1800-03)、『ジーベンケース』(1796-97)等で展開した特異な散文形式。ステルン的脱線・カント受容・幽默（Humor）・幻想的構成を統合し、ヴァイマル古典主義とロマン主義の中間に位置する独自系譜を成した。",
    background="スターン『トリストラム・シャンディ』のドイツ受容、ヴァイマル古典主義への対抗。",
    development="ノヴァーリス、E.T.A.ホフマン、19世紀ドイツ散文の独自系譜、20世紀ベンヤミン『ジャン・パウル論』の中心研究対象。",
    historical_context="1790年代から1820年代にかけてのドイツ散文の多様化期。",
    primary_source_url=GUTEN+"author/1196",
    primary_source_type="Project Gutenberg: Jean Paul works",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ヴィーラント『オーベロン』",
    name_en="Wieland's Oberon",
    name_original="Oberon",
    period_key="ドイツ・シュトゥルム・ウント・ドラング期",
    definition="クリストフ・マルティン・ヴィーラント（1733-1813）が1780年に発表した叙事詩。シェイクスピア『真夏の夜の夢』に着想した妖精オーベロンを枠物語として、フランス中世物語『ユオン・ド・ボルドー』を語り直す。ドイツ・ロココ叙事詩の頂点で、ヴァイマル古典主義の詩形成に直接的影響を与えた。",
    background="フランスロココ騎士物語伝統と、シェイクスピア・ドイツ受容の早期段階。",
    development="ヴァイマル古典主義詩、19世紀ドイツ叙事詩、ヴェーバー・オペラ『オーベロン』(1826)の原作となった。",
    historical_context="1780年代ヴァイマル文化圏の形成期、ヴィーラントのヴァイマル招聘期。",
    primary_source_url=GUTEN+"ebooks/52450",
    primary_source_type="Project Gutenberg: Oberon (Wieland)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# D: British Romantic Poetry (8)
# ============================================================
add(**C, name_ja="ワーズワース『序曲（プレリュード）』",
    name_en="Wordsworth's The Prelude",
    name_original="The Prelude, or, Growth of a Poet's Mind",
    period_key="英国ロマン主義詩期",
    definition="ウィリアム・ワーズワース（1770-1850）が生涯にわたり改訂した自伝的長詩。1799年版（2巻）、1805年版（13巻）、1850年版（14巻、死後刊行）が存在。詩人の内的形成史を主題化し、英国ロマン主義の自伝的長詩形式を確立した。20世紀M.H.エイブラムズ『自然な超自然主義』(1971)が浪漫派詩学の中心テクストとして再評価。",
    background="ルソー『告白』『新エロイーズ』の自伝的散文の英国詩形式への翻訳、フランス革命期の幻滅と再帰的内省。",
    development="シェリー、キーツの自伝的長詩、19世紀英国詩の中心モデル、20世紀ロマン主義批評（エイブラムズ、ハーロルド・ブルーム）の中心テクスト。",
    historical_context="フランス革命期から英国保守反動期にかけての詩人内省記録。",
    primary_source_url=GUTEN+"ebooks/8774",
    primary_source_type="Project Gutenberg: The Prelude",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ブレイク『無垢と経験の歌』",
    name_en="Blake's Songs of Innocence and of Experience",
    name_original="Songs of Innocence and of Experience",
    period_key="英国ロマン主義詩期",
    definition="ウィリアム・ブレイク（1757-1827）が1789年『無垢の歌』、1794年に『経験の歌』を併合した自著彫版による詩画集。「人間魂の二つの対照的状態」を副題とし、対をなす詩編で無垢と経験の弁証法を展開した。19世紀後半（ロセッティ、エリス、イェイツ）まで地下的存在だったブレイクが20世紀に世界詩史の中心へ復帰した起点。",
    background="18世紀末英国の急進主義（プライス、ペイン）思想、神秘主義的キリスト教伝統、自著彫版印刷の独自実践。",
    development="ロセッティ・スウィンバーン経由の19世紀末再評価、20世紀イェイツ『ブレイク論』、ノースロップ・フライ『恐ろしき対称』(1947)の中心研究対象。",
    historical_context="フランス革命期英国の急進主義運動と保守反動。",
    primary_source_url=GUTEN+"ebooks/1934",
    primary_source_type="Project Gutenberg: Songs of Innocence and Experience",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ブレイクの予言書",
    name_en="Blake's Prophetic Books",
    name_original="Blake's Prophetic Books",
    period_key="英国ロマン主義詩期",
    definition="ブレイクが1789-1820年に制作した独自神話体系を持つ大型詩画集。『セルの書』『アルビヨンの娘たちの幻覚』『アメリカ』『ユリゼンの第一の書』『ミルトン』『エルサレム』を中核とする。独自の神話的人物（ユリゼン、ロス、オーク、エルサレム、アルビヨン）による宇宙論的神話を構築し、20世紀後半詩学の中心研究対象となった。",
    background="ミルトン『失楽園』、聖書黙示文学、グノーシス的神秘主義の独自統合。",
    development="20世紀イェイツ、ノースロップ・フライ、ハーロルド・ブルーム『ブレイクの黙示録』(1963)の中心研究対象。",
    historical_context="フランス革命期からナポレオン戦争期にかけての英国の急進神秘主義系譜。",
    primary_source_url=GUTEN+"ebooks/45315",
    primary_source_type="Project Gutenberg: Blake Prophetic Books",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="キーツの大頌歌群",
    name_en="Keats's Great Odes",
    name_original="Keats's Great Odes (1819)",
    period_key="英国ロマン主義詩期",
    definition="ジョン・キーツ（1795-1821）が1819年4月から9月の僅か数ヶ月に書いた頌歌群。「プシュケーへの頌歌」「ナイチンゲールへの頌歌」「ギリシア壺の頌歌」「メランコリーへの頌歌」「怠惰への頌歌」「秋に寄せて」を含む。英国ロマン主義詩の頂点で、20世紀新批評・ハーロルド・ブルームのロマン主義批評の中心テクスト。",
    background="1818-19年の劇的詩的成熟期、結核症状の進展、シェイクスピア研究の集中期。",
    development="20世紀英米新批評（クリーンス・ブルックス『精緻に組まれた壺』1947）、ハーロルド・ブルーム『影響の不安』のロマン主義詩学の中心テクスト。",
    historical_context="1819年英国「ピータールー虐殺」前後の社会的動乱期、キーツ最後の創作期。",
    primary_source_url=GUTEN+"ebooks/23684",
    primary_source_type="Project Gutenberg: Keats poems",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="キーツ書簡",
    name_en="Keats's Letters",
    name_original="Keats's Letters",
    period_key="英国ロマン主義詩期",
    definition="キーツが1814-20年に家族・友人に送った書簡集。「消極的能力（negative capability）」「魂の創造の谷（vale of soul-making）」「カメレオン的詩人」等の重要詩学概念がここに表明されており、英国ロマン主義詩学の主要源泉として20世紀詩学の中心テクストとなった。",
    background="ロマン主義期英国の書簡文化、キーツの形式的詩論不在を補う重要資料。",
    development="20世紀T.S.エリオット『伝統と個人の才能』、リチャーズ、ハーロルド・ブルームのロマン主義詩学の中心参照源。",
    historical_context="1817-20年キーツ短い創作期と、結核闘病・財政困窮期。",
    primary_source_url=GUTEN+"ebooks/35698",
    primary_source_type="Project Gutenberg: Letters of Keats",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"キーツ「消極的能力」「カメレオン的詩人」概念は、固定主体を解体する詩人観を提示する。AI生成における「主体なき声」を再考する古典的祖型。",
         "related_ai_phenomenon":"AIにおける主体性・声の流動性"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"消極的能力・カメレオン的詩人",
         "description":"キーツ書簡の詩学概念は20世紀英米詩学の中心理論用語であり、現代詩論と直接接続する。"}])

add(**C, name_ja="シェリー『アドーニス』",
    name_en="Shelley's Adonais",
    name_original="Adonais: An Elegy on the Death of John Keats",
    period_key="英国ロマン主義詩期",
    definition="パーシー・ビッシュ・シェリー（1792-1822）が1821年にキーツの死を悼んで書いた55スパンサー連詩節の挽歌。テオクリトス・モスコス・ミルトン『リシダス』の挽歌伝統を継承しつつ、ロマン主義的神秘主義的世界観を展開した。英国ロマン主義挽歌の頂点。",
    background="キーツの死(1821年2月、ローマ)への直接的応答、ピンダロス・ミルトン挽歌伝統の継承。",
    development="19世紀英国挽歌、テニスン『イン・メモリアム』、ハーディ・ハーディ詩への影響、20世紀ロマン主義詩学の中心テクスト。",
    historical_context="1821年英国・イタリアの自由主義運動期と、ロマン主義詩人のイタリア亡命期。",
    primary_source_url=GUTEN+"ebooks/4800",
    primary_source_type="Project Gutenberg: Adonais",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バイロン『ドン・ジュアン』",
    name_en="Byron's Don Juan",
    name_original="Don Juan",
    period_key="英国ロマン主義詩期",
    definition="ジョージ・ゴードン・バイロン（1788-1824）が1819-24年に発表した未完の風刺叙事詩。16曲17,000行余で、伝統的ドン・ファン伝説を反転させ、女性に翻弄される受動的ドン・ジュアンの遍歴を描く。オッターヴァ・リーマ詩節を用いた風刺・脱線・自意識的詩形式で、英国ロマン主義叙事詩の独自系譜を成した。",
    background="プルチ、ベルニ、アリオストのイタリア・オッターヴァ・リーマ風刺伝統の英国移植。",
    development="プーシキン『エヴゲーニー・オネーギン』への直接影響、19-20世紀風刺長詩の祖型、現代英米風刺詩の中心参照点。",
    historical_context="1820年代バイロンのイタリア・ギリシア亡命期と独立戦争関与期。",
    primary_source_url=GUTEN+"ebooks/21700",
    primary_source_type="Project Gutenberg: Don Juan",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バイロン『チャイルド・ハロルドの巡礼』",
    name_en="Byron's Childe Harold's Pilgrimage",
    name_original="Childe Harold's Pilgrimage",
    period_key="英国ロマン主義詩期",
    definition="バイロンが1812-18年に発表した4曲のスパンサー連詩節叙事詩。半自伝的主人公チャイルド・ハロルドのヨーロッパ巡礼を描き、第3-4曲(1816-18)では一人称詩人へ接近した。第1-2曲(1812)発表時の「朝目覚めて有名になっていた」現象は欧州的現象となり、「バイロン的英雄」の典型を確立した。",
    background="ナポレオン戦争期英国の大陸旅行制限、戦後再開された大陸旅行。",
    development="プーシキン、レールモントフ、19世紀ロマン主義英雄像、20世紀『バイロン的英雄』論議の中心テクスト。",
    historical_context="ナポレオン戦争末期から戦後ヨーロッパの再編期。",
    primary_source_url=GUTEN+"ebooks/5131",
    primary_source_type="Project Gutenberg: Childe Harold",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: German Romanticism (5)
# ============================================================
add(**C, name_ja="ノヴァーリス『ハインリヒ・フォン・オフターディンゲン』",
    name_en="Novalis's Heinrich von Ofterdingen",
    name_original="Heinrich von Ofterdingen",
    period_key="ドイツ・ロマン派期",
    definition="ノヴァーリス（フリードリヒ・フォン・ハルデンベルク、1772-1801）が1799-1800年に執筆し未完のまま1802年に死後発表された小説。中世吟遊詩人ハインリヒの詩人形成を通じ、有名な「青い花」象徴を提示。ゲーテ『ヴィルヘルム・マイスター』への対抗的応答として書かれ、ドイツ・ロマン派教養小説の典型作品となった。",
    background="ヴァイマル古典主義への対抗、イエナ・ロマン派サークルでの議論、シェリング自然哲学受容。",
    development="19世紀ドイツ・ロマン派教養小説、20世紀ロマン派研究、「青い花」象徴の世界文学的普及。",
    historical_context="1800年前後のイエナ・ロマン派サークル形成期、シェリング自然哲学興隆期。",
    primary_source_url=GUTEN+"ebooks/4023",
    primary_source_type="Project Gutenberg: Heinrich von Ofterdingen",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"イエナ・ロマン派哲学",
         "description":"ノヴァーリス小説はシェリング自然哲学・シュレーゲル・ロマン派哲学の文学的具体化として、哲学DBと直接接続する。"}])

add(**C, name_ja="ティークの幻想物語",
    name_en="Tieck's fantastic tales",
    name_original="Tiecks phantastische Erzählungen",
    period_key="ドイツ・ロマン派期",
    definition="ルートヴィヒ・ティーク（1773-1853）が1797年『ペーター・レーバレヒト民衆物語』、『金髪のエックベルト』(1797)、『ルーネンベルク』(1804)で確立したドイツ・ロマン派幻想物語形式。民間伝承的素材を心理的不安と統合し、E.T.A.ホフマン以前のドイツ・ロマン派短編幻想小説の祖型を成した。",
    background="ドイツ民間伝承研究、ロマン派短編形式の独自展開、エディンバラ・レビュー受容。",
    development="E.T.A.ホフマン、19世紀ドイツ・ロマン派短編、20世紀幻想文学論（トドロフ『幻想文学序説』1970）の中心研究対象。",
    historical_context="1790年代後半から1810年代にかけてのドイツ・ロマン派短編形式の独自確立期。",
    primary_source_url=GUTEN+"author/1140",
    primary_source_type="Project Gutenberg: Tieck works",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ブレンターノとアルニム『少年の魔法の角笛』",
    name_en="Brentano and Arnim's Des Knaben Wunderhorn",
    name_original="Des Knaben Wunderhorn",
    period_key="ドイツ・ロマン派期",
    definition="クレメンス・ブレンターノ（1778-1842）とアヒム・フォン・アルニム（1781-1831）が1805-08年に編纂した古いドイツ民謡集。3巻600編余を収録し、ヘルダー民謡論を実践した。ハイデルベルク・ロマン派の中心成果で、グリム兄弟『童話集』、19世紀ドイツ国民詩運動の理論的・実践的源泉となった。",
    background="ヘルダー民謡論、ハイデルベルク・ロマン派サークル、ナポレオン期ドイツの国民意識形成。",
    development="グリム兄弟『童話集』、19世紀ドイツ・リート（シューベルト、シューマン、マーラー『角笛交響曲』）の中核テクスト源。",
    historical_context="ナポレオン戦争期ドイツの国民詩運動、神聖ローマ帝国解体期(1806)。",
    primary_source_url=GUTEN+"ebooks/30828",
    primary_source_type="Project Gutenberg: Des Knaben Wunderhorn",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アイヒェンドルフ『たわけ者の生活より』",
    name_en="Eichendorff's From the Life of a Good-for-Nothing",
    name_original="Aus dem Leben eines Taugenichts",
    period_key="ドイツ・ロマン派期",
    definition="ヨーゼフ・フォン・アイヒェンドルフ（1788-1857）が1826年に発表した中編小説。粉ひきの息子の遍歴と恋愛を、ドイツ・ロマン派の散文として最も澄明な抒情で描く。後期ドイツ・ロマン派散文の頂点で、19世紀ドイツ国民愛唱小説の地位を獲得した。",
    background="ハイデルベルク・ロマン派、ナポレオン戦争期の祖国愛、カトリック保守主義詩学。",
    development="19世紀ドイツ国民詩・散文の定着、20世紀ドイツ文学教育の中心テクスト。",
    historical_context="ヴィーン体制期ドイツの保守的ロマン主義文化。",
    primary_source_url=GUTEN+"ebooks/16267",
    primary_source_type="Project Gutenberg: Aus dem Leben eines Taugenichts",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="E.T.A.ホフマン『砂男』",
    name_en="E.T.A. Hoffmann's The Sandman",
    name_original="Der Sandmann",
    period_key="ドイツ・ロマン派期",
    definition="エルンスト・テオドア・アマデウス・ホフマン（1776-1822)が1816年『夜想曲集』所収の中編小説『砂男』。学生ナタナエルの人形オリンピアへの恋愛と狂気を描く。フロイト『不気味なもの』(1919)が「不気味なもの（das Unheimliche）」概念の中心分析対象とし、20世紀文学理論の中心テクストとなった。",
    background="ドイツ後期ロマン派の幻想・心理探究、自動人形に対する啓蒙期以来の関心。",
    development="フロイト『不気味なもの』、ラカン精神分析、20世紀の幻想文学・SF（ホフマン的人形・自動機械主題）の中心テクスト。",
    historical_context="1810年代後期ロマン派の心理的・形而上学的暗部探究期。",
    primary_source_url=GUTEN+"ebooks/41390",
    primary_source_type="Project Gutenberg: Der Sandmann",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"『砂男』のオリンピア（自動人形）と人間の混同主題は、AI時代における人間-人工存在の境界問題（ChatGPT等への愛着）を予言する古典的祖型。フロイト『不気味なもの』を経由してAI不気味の谷理論と接続。",
         "related_ai_phenomenon":"AI/ロボットへの愛着・不気味の谷"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"自動人形と人間の見分けがつかなくなる主題は、AI生成と人間生成の見分けがつかなくなるTuring問題の文学的祖型。",
         "related_ai_phenomenon":"AI生成と人間生成の識別不能性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"不気味なもの（フロイト）",
         "description":"『砂男』はフロイト『不気味なもの』の中心分析対象で、哲学DB・精神分析項目と直接接続する。"}])


# ============================================================
# F: Russian Romanticism (5)
# ============================================================
add(**CRU, name_ja="プーシキン『エヴゲーニー・オネーギン』",
    name_en="Pushkin's Eugene Onegin",
    name_original="Евгений Онегин",
    period_key="ロシア・ロマン主義期",
    definition="アレクサンドル・プーシキン（1799-1837）が1825-32年に発表した「韻文小説（роман в стихах）」。8章のオネーギン詩節（独自14行詩節）で、貴族青年オネーギンとタチヤーナの悲恋を中心に、ロシア社会の全層を抒情的に描く。ロシア近代文学の出発点として、ベリンスキー以来「ロシア生活の百科事典」と称される。",
    background="バイロン『ドン・ジュアン』のオッターヴァ・リーマ風刺叙事詩の独自的応用、ロシア社会の文学的全体把握の野心。",
    development="ロシア小説（ゴーゴリ、トゥルゲーネフ、ドストエフスキー、トルストイ）の出発点、チャイコフスキー・オペラ(1879)、20世紀ナボコフ訳・注釈版(1964)。",
    historical_context="アレクサンドル1世期からニコライ1世期のロシア貴族社会、デカブリスト蜂起(1825)前後。",
    primary_source_url=GUTEN+"ebooks/23997",
    primary_source_type="Project Gutenberg: Eugene Onegin",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CRU, name_ja="プーシキン『ベールキン物語』",
    name_en="Pushkin's Belkin Tales",
    name_original="Повести покойного Ивана Петровича Белкина",
    period_key="ロシア・ロマン主義期",
    definition="プーシキンが1830年「ボルディノの秋」期に書いた5編の短編集（『一発』『吹雪』『葬儀屋』『駅長』『百姓令嬢』）。架空の編者ベールキン枠を介する物語で、ロシア近代散文の出発点とされる。簡潔な散文、複層的語り、社会階層の戯謔的描写によって、後のロシア短編小説の規範となった。",
    background="プーシキンのバルディノでの3ヶ月の集中創作期、ロシア散文形式の確立期。",
    development="ゴーゴリ短編、19世紀後半ロシア短編（チェーホフ）、20世紀短編論の中心テクスト。",
    historical_context="1830年バルディノでのコレラ流行下隔離期。",
    primary_source_url=GUTEN+"ebooks/13437",
    primary_source_type="Project Gutenberg: Belkin Tales",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CRU, name_ja="レールモントフ『現代の英雄』",
    name_en="Lermontov's A Hero of Our Time",
    name_original="Герой нашего времени",
    period_key="ロシア・ロマン主義期",
    definition="ミハイル・レールモントフ（1814-1841）が1840年に発表した小説。コーカサス駐留将校ペチョーリンを「我々の時代の英雄」として、複数視点による5章の物語で描く。バイロン的英雄像のロシア化、ロシア最初の心理小説、複数視点語りの早期実例として、ロシア近代小説の重要起源の一つ。",
    background="バイロン『ドン・ジュアン』『チャイルド・ハロルド』のロシア受容、ニコライ1世期反動下のコーカサス戦線。",
    development="トルストイ・ドストエフスキー心理小説、20世紀バフチン対話論、ナボコフ評価による西側受容。",
    historical_context="ニコライ1世反動期、コーカサス戦争期(1817-64)、レールモントフ自身のコーカサス流刑。",
    primary_source_url=GUTEN+"ebooks/913",
    primary_source_type="Project Gutenberg: A Hero of Our Time",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CRU, name_ja="ゴーゴリ『ペテルブルグ物語』",
    name_en="Gogol's Petersburg Tales",
    name_original="Петербургские повести",
    period_key="ロシア・ロマン主義期",
    definition="ニコライ・ゴーゴリ（1809-1852）が1835-42年に発表した短編集（『ネフスキー大通り』『鼻』『肖像画』『外套』『狂人日記』）。ペテルブルグの官吏・芸術家・小市民の幻想的生を、ロマン主義的グロテスクで描く。ドストエフスキー「我々は皆ゴーゴリの『外套』から出てきた」（伝承）の通り、ロシアリアリズムの出発点。",
    background="ペテルブルグ官僚都市の文学化、ロマン主義的グロテスク（ホフマン）のロシア応用。",
    development="ドストエフスキー『貧しき人々』『二重人格』、19世紀ロシア・リアリズム、20世紀世界小説論の中心研究対象。",
    historical_context="ニコライ1世反動期ペテルブルグの官僚社会・芸術家環境。",
    primary_source_url=GUTEN+"ebooks/36238",
    primary_source_type="Project Gutenberg: Gogol Petersburg Tales",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CRU, name_ja="ゴーゴリ『死せる魂』",
    name_en="Gogol's Dead Souls",
    name_original="Мёртвые души",
    period_key="ロシア・ロマン主義期",
    definition="ゴーゴリが1842年に発表した第一部・1855年（死後）に発表された第二部断片からなる長編小説。詐欺師チチコフがロシア地主から「死せる魂」（戸籍上生存する死者農奴）を買い集める旅を描く。プーシキンの示唆を受けて執筆され、19世紀ロシア社会の縮図として、ロシア小説の中心古典となった。",
    background="ロシア農奴制の社会的現実、ダンテ『神曲』を範とした構想（地獄・煉獄・天国の三部）。",
    development="ロシアリアリズム小説（ドストエフスキー・トルストイ）、20世紀ナボコフ『ニコライ・ゴーゴリ』(1944)による西側受容。",
    historical_context="ニコライ1世反動期、農奴制廃止(1861)前夜の社会的緊張。",
    primary_source_url=GUTEN+"ebooks/1081",
    primary_source_type="Project Gutenberg: Dead Souls",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# G: American Romanticism (10)
# ============================================================
add(**CAM, name_ja="ホーソーン『緋文字』",
    name_en="Hawthorne's The Scarlet Letter",
    name_original="The Scarlet Letter",
    period_key="米国ロマン主義期",
    definition="ナサニエル・ホーソーン（1804-1864）が1850年に発表した長編小説。17世紀ニューイングランド・ピューリタン社会で姦通の罪に問われたヘスター・プリンを中心に、罪・道徳・象徴を中核とする心理アレゴリー。米国ロマン主義小説の頂点で、20世紀ヘンリー・ジェイムズ『ホーソーン論』(1879)以降、米国国民文学の起源として位置づけられた。",
    background="セイラム魔女裁判(1692)を含むニューイングランド・ピューリタン史への内省的関心、ホーソーン自身の家系（裁判官祖先）への意識。",
    development="ヘンリー・ジェイムズ『ホーソーン』(1879)、20世紀F.O.マシーセン『アメリカン・ルネサンス』(1941)による国民文学化。",
    historical_context="1850年合衆国「逃亡奴隷法」期の道徳的緊張、ホーソーン自身の税関職解雇期。",
    primary_source_url=GUTEN+"ebooks/25344",
    primary_source_type="Project Gutenberg: The Scarlet Letter",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CAM, name_ja="メルヴィル『白鯨』",
    name_en="Melville's Moby-Dick",
    name_original="Moby-Dick; or, The Whale",
    period_key="米国ロマン主義期",
    definition="ハーマン・メルヴィル（1819-1891）が1851年に発表した長編小説。捕鯨船ピークォド号船長エイハブによる白鯨追跡を、語り手イシュメイルの一人称で叙述する。シェイクスピア劇・聖書・百科全書的記述・哲学的思索を統合した形式は、20世紀F.O.マシーセン『アメリカン・ルネサンス』(1941)以降、米国小説の最高峰として再評価された。",
    background="ナンタケット・ニューベッドフォードの捕鯨産業の文学化、ホーソーン親交期(1850-51)、シェイクスピア集中読書期。",
    development="20世紀メルヴィル復興（マシーセン、オールセン、ハロルド・ブルーム）、現代米国国民文学の中心テクスト。",
    historical_context="1850年逃亡奴隷法、米国産業資本主義興隆期、シェイクスピア再評価期。",
    primary_source_url=GUTEN+"ebooks/2701",
    primary_source_type="Project Gutenberg: Moby-Dick",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"形而上学的探究小説",
         "description":"『白鯨』はカルヴァン主義神学・近代形而上学の文学的応答として、哲学DBの宗教哲学項目と接続する。"}])

add(**CAM, name_ja="メルヴィル『書記バートルビー』",
    name_en="Melville's Bartleby, the Scrivener",
    name_original="Bartleby, the Scrivener: A Story of Wall-Street",
    period_key="米国ロマン主義期",
    definition="メルヴィルが1853年に発表した中編小説。ウォール街の弁護士事務所で「するつもりはありません（I would prefer not to）」を反復する書記バートルビーを描く。20世紀後半デリダ、アガンベン、ドゥルーズ、ジジェクのバートルビー論によって、抵抗の哲学・潜勢力の理論の中心テクストとなった。",
    background="メルヴィル後期の小品時代、米国産業資本主義初期のオフィス労働の文学化。",
    development="20世紀ドゥルーズ「バートルビー、または定式」(1989)、アガンベン『バートルビー』(1993)、現代抵抗哲学・批判理論の中心テクスト。",
    historical_context="1850年代初頭のニューヨーク商業地区拡大期。",
    primary_source_url=GUTEN+"ebooks/11231",
    primary_source_type="Project Gutenberg: Bartleby",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"バートルビーの「I would prefer not to」は労働拒否・主体的抵抗の極限形態を文学化する。AI時代における人間労働の意味問題と直接共振する古典的祖型。",
         "related_ai_phenomenon":"AI時代の労働拒否・人間労働の意味"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"潜勢力の哲学（アガンベン）",
         "description":"『バートルビー』はアガンベン潜勢力哲学の中心テクストで、哲学DBと直接接続する。"}])

add(**CAM, name_ja="ポーの短編詩学",
    name_en="Poe's short story poetics",
    name_original="Poe's poetics of the short story",
    period_key="米国ロマン主義期",
    definition="エドガー・アラン・ポー（1809-1849）が「ホーソーン書評」(1842)、「構成の原理」(1846)、「詩の原理」(1850)で展開した短編・詩の理論。「単一効果（unity of effect）」「一気に読める長さ」「効果からの逆算」を中核理念とし、近代短編・近代探偵小説・象徴主義詩学の理論的祖型を提供した。",
    background="米国雑誌文化の興隆と短編形式の経済的成熟、英国ロマン主義詩論（コールリッジ）の独自展開。",
    development="ボードレール訳によるフランス象徴主義への決定的影響、後の英米短編論（マシーセン、新批評）、近代探偵小説論の起源。",
    historical_context="1840年代米国雑誌文化興隆期と、英米文化交流期。",
    primary_source_url=GUTEN+"ebooks/55749",
    primary_source_type="Project Gutenberg: Poe critical works",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"単一効果・短編詩学",
         "description":"ポー単一効果論は20世紀短編詩学の中心理論用語であり、現代物語論と直接接続する。"}])

add(**CAM, name_ja="エマソン『自己信頼』",
    name_en="Emerson's Self-Reliance",
    name_original="Self-Reliance",
    period_key="米国ロマン主義期",
    definition="ラルフ・ウォルドー・エマソン（1803-1882）が1841年『エッセー第一集』所収の代表的エッセー。「独自の魂を信頼せよ」「一貫性は小さき精神の妖怪」等の名句で、米国超越主義の中心思想を表明した。エマソン自伝『自然論』(1836)、講演集とともに、米国ロマン主義思想の制度的中核を成す。",
    background="ニューイングランド・ユニテリアニズム、独逸観念論受容、英国ロマン主義（コールリッジ、カーライル）受容。",
    development="ニーチェ受容（『人類学的なるもの、人間的なるもの』に影響）、20世紀米国プラグマティズム、現代米国個人主義論の中心源泉。",
    historical_context="1840年代ニューイングランド超越主義運動期、米国国民文化形成期。",
    primary_source_url=GUTEN+"ebooks/16643",
    primary_source_type="Project Gutenberg: Essays (Emerson)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"超越主義・米国観念論",
         "description":"エマソン『自己信頼』は米国超越主義の中心テクストで、哲学DBの観念論項目と直接接続する。"}])

add(**CAM, name_ja="ソロー『ウォルデン』",
    name_en="Thoreau's Walden",
    name_original="Walden; or, Life in the Woods",
    period_key="米国ロマン主義期",
    definition="ヘンリー・デイヴィッド・ソロー（1817-1862）が1854年に発表した自然観察と社会批評の散文集。1845-47年にウォルデン湖畔で過ごした2年2ヶ月の隠棲経験を再構成し、簡素な生活・自然観察・市民社会批判を統合した。米国ロマン主義散文の最高峰で、20世紀環境思想・自発的隠棲思想の祖型となった。",
    background="エマソン超越主義の実践化、米国産業資本主義初期への批判、ヒンドゥー教典『バガヴァッド・ギーター』受容。",
    development="20世紀環境思想（レイチェル・カーソン）、ガンディー非暴力抵抗論、現代エコクリティシズムの中心テクスト。",
    historical_context="1840年代ニューイングランド超越主義運動期、米墨戦争期(1846-48)。",
    primary_source_url=GUTEN+"ebooks/205",
    primary_source_type="Project Gutenberg: Walden",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CAM, name_ja="ホイットマン『草の葉』",
    name_en="Whitman's Leaves of Grass",
    name_original="Leaves of Grass",
    period_key="米国ロマン主義期",
    definition="ウォルト・ホイットマン（1819-1892）が1855年に初版を自費出版し、生涯にわたり改訂を続けた詩集。1855年版「自分自身の歌（Song of Myself）」を中核に、自由詩・カタログ詩形式・民主主義的同化の詩学を確立した。米国国民詩の出発点とされ、20世紀世界自由詩の祖型となった。",
    background="エマソン超越主義の影響、米国民主主義拡大期、ジャーナリスト経験の詩学への統合。",
    development="20世紀世界自由詩（ネルーダ、ロルカ、マヤコフスキー）、ビート世代（ギンズバーグ）の詩学的源泉。",
    historical_context="1855年米国南北戦争前夜の社会的緊張、米国国民文化形成期。",
    primary_source_url=GUTEN+"ebooks/1322",
    primary_source_type="Project Gutenberg: Leaves of Grass",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ホイットマン「自分自身の歌」の自己同一化的拡張（「我は群衆を含む」）は、AI時代の集合的主体・複数声生成と理論的に共振する。",
         "related_ai_phenomenon":"AI生成における集合的主体・複数声"}])

add(**CAM, name_ja="ディキンソン詩",
    name_en="Dickinson's poems",
    name_original="Emily Dickinson's poems",
    period_key="米国ロマン主義期",
    definition="エミリー・ディキンソン（1830-1886）が生涯1,800編余を私的に書き、死後発表（1890年初版）された詩群。ダッシュ多用、独特の押韻、神秘主義・死・自然・内面を主題とする凝縮された短詩形式。20世紀以降、米国詩の最高峰の一つとして再評価され、現代女性詩学の中心テクストとなった。",
    background="ニューイングランド・ピューリタン文化、家庭内隠棲、独自の詩的形式実験。",
    development="20世紀ディキンソン復興（トマス・ジョンソン編1955年版）、現代女性詩学・米国詩学の中心研究対象。",
    historical_context="米国南北戦争期から再建期にかけてのマサチューセッツ・アマースト隠棲生活。",
    primary_source_url=GUTEN+"ebooks/12242",
    primary_source_type="Project Gutenberg: Dickinson poems",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CAM, name_ja="ポー『詩集』とフランス象徴主義への影響",
    name_en="Poe's poems and French Symbolism",
    name_original="Poe's poems / influence on Symbolism",
    period_key="米国ロマン主義期",
    definition="ポー『大鴉』(1845)、『鐘』『アナベル・リー』等の詩作と「詩の原理」が、ボードレール訳（1856-65）、マラルメ「ポーの墓」(1876)、ヴァレリーを経由して、フランス象徴主義詩学の最重要海外源泉となった経路。米国ロマン主義詩が19世紀フランス文学変革を引き起こした特異な事例。",
    background="ボードレールのポー没後翻訳事業、マラルメ・ヴァレリーの継承的受容。",
    development="フランス象徴主義（マラルメ、ヴァレリー）、英米モダニズム（T.S.エリオット）の中心源泉となった。",
    historical_context="19世紀後半のフランス・米国文化交流、ボードレール『悪の華』(1857)期。",
    primary_source_url=GUTEN+"ebooks/10031",
    primary_source_type="Project Gutenberg: Poe poems",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CAM, name_ja="ホーソーン『大理石の牧神』",
    name_en="Hawthorne's The Marble Faun",
    name_original="The Marble Faun; or, The Romance of Monte Beni",
    period_key="米国ロマン主義期",
    definition="ホーソーンが1860年に発表した最後の長編小説。ローマを舞台に米国人芸術家と神秘的イタリア人の交錯を描く。ホーソーン後期の罪・芸術・歴史を統合した複雑な作品で、ヘンリー・ジェイムズ『ローダリック・ハドソン』『黄金の盃』等の米欧文化交流主題への直接的先駆をなした。",
    background="1850年代後半のホーソーン・イタリア滞在、米国ロマン主義のヨーロッパ志向期。",
    development="ヘンリー・ジェイムズ『ローダリック・ハドソン』(1875)以降の米欧主題小説への直接的影響。",
    historical_context="米国南北戦争前夜、ホーソーンのリヴァプール領事および欧州滞在期。",
    primary_source_url=GUTEN+"ebooks/2181",
    primary_source_type="Project Gutenberg: The Marble Faun",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# H: Latin American Romanticism (2)
# ============================================================
add(**CLA, name_ja="エチェベリーア『屠殺場』",
    name_en="Echeverría's El Matadero",
    name_original="El Matadero",
    period_key="ラテンアメリカ・ロマン主義期",
    definition="エステバン・エチェベリーア（1805-1851）が1838-40年頃に書き1871年（死後）に発表した中編小説。ロサス独裁期ブエノスアイレスの屠殺場でユニタリオ党員が虐殺される場面を凝視的に描く。ラテンアメリカ・ロマン主義散文の最初期傑作で、19世紀後半のリアリズム・自然主義へ橋渡しする決定的作品。",
    background="ロサス連邦派独裁(1829-52)、エチェベリーアのフランス・ロマン主義受容、若きアルゼンチン世代の活動。",
    development="サルミエント『ファクンド』(1845)、19世紀末ラテンアメリカ・リアリズム、20世紀ラテンアメリカ独裁小説の祖型。",
    historical_context="ロサス連邦派独裁期(1829-52)アルゼンチンの政治的弾圧期。",
    primary_source_url=WSRC_ES+"El_matadero",
    primary_source_type="Wikisource ES: El Matadero",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CLA, name_ja="ホルヘ・イサークス『マリーア』",
    name_en="Jorge Isaacs's María",
    name_original="María",
    period_key="ラテンアメリカ・ロマン主義期",
    definition="ホルヘ・イサークス（1837-1895）が1867年に発表したコロンビア・ロマン主義小説の代表作。カウカ渓谷を舞台に、エフライムとマリーアの悲恋を抒情的散文で描く。19世紀ラテンアメリカ・ロマン主義感傷小説の頂点で、コロンビアおよびラテンアメリカ全域でほぼ全ての読書層に読まれる国民文学の地位を獲得した。",
    background="コロンビア独立後の地方主義文学、フランス・ロマン主義（シャトーブリアン『アタラ』）の受容。",
    development="ラテンアメリカ19世紀ロマン主義感傷小説の規範、20世紀大陸的国民文学の祖型。",
    historical_context="19世紀後半コロンビア・カウカ渓谷の社会と、ラテンアメリカ独立後の文化的アイデンティティ形成。",
    primary_source_url=GUTEN+"ebooks/26865",
    primary_source_type="Project Gutenberg: María",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# I: Italian / Spanish Romanticism (2)
# ============================================================
add(**C, name_ja="マンゾーニ『いいなづけ』",
    name_en="Manzoni's I Promessi Sposi",
    name_original="I Promessi Sposi",
    period_key="イタリア・スペイン・ロマン主義期",
    definition="アレッサンドロ・マンゾーニ（1785-1873）が1827年初版・1840-42年改訂版を発表した長編歴史小説。17世紀ロンバルディーアを舞台にレンツォとルチーアの婚姻を阻む権力者・疫病・戦乱を描く。ウォルター・スコット『ウェイヴァリー』を範に、イタリア国民文学・近代イタリア語確立の中心作品となった。",
    background="ウォルター・スコット歴史小説のイタリア受容、リソルジメント期のイタリア国民意識形成。",
    development="19世紀後半イタリア国民文学、20世紀グラムシ『獄中ノート』のマンゾーニ論、現代イタリア教養層の中心古典。",
    historical_context="リソルジメント期(1815-71)イタリア国民国家形成運動期。",
    primary_source_url=GUTEN+"ebooks/45334",
    primary_source_type="Project Gutenberg: I Promessi Sposi",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="レオパルディ『カンティ』",
    name_en="Leopardi's Canti",
    name_original="Canti",
    period_key="イタリア・スペイン・ロマン主義期",
    definition="ジャコモ・レオパルディ（1798-1837）が1831年・1835年の二度にわたり編纂した詩集。「無限」「シルヴィアに」「夜の歌」「アジアの遊牧の羊飼いの夜の歌」等を含む41編。哲学的悲観主義・無限への憧憬・形而上学的孤独を主題とし、イタリア・ロマン主義詩の頂点として、現代世界詩学にも深い影響を残した。",
    background="マンチェスターのレオパルディ家邸宅での古典研究、イタリア・ロマン主義の哲学的成熟期。",
    development="ニーチェ・受容、20世紀イタリア・モンターレ等への影響、現代世界詩学の中心研究対象（ハーロルド・ブルーム『西欧正典』）。",
    historical_context="リソルジメント前期イタリアの政治的閉塞と、レオパルディ自身の身体的虚弱・宗教的危機。",
    primary_source_url=GUTEN+"ebooks/52717",
    primary_source_type="Project Gutenberg: Canti (Leopardi)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"哲学的悲観主義",
         "description":"レオパルディ『ジバルドーネ』および『カンティ』はショーペンハウアー悲観主義と並ぶ19世紀哲学的悲観主義の中心テクスト。"}])

add(**C, name_ja="ベッケル『リーマス』",
    name_en="Bécquer's Rimas",
    name_original="Rimas",
    period_key="イタリア・スペイン・ロマン主義期",
    definition="グスタボ・アドルフォ・ベッケル（1836-1870）が生前発表し死後編纂された短詩集（76編）。簡潔な形式で恋・自然・神秘・幻滅を主題とし、19世紀後期スペイン・ロマン主義詩の頂点を成した。ハイネ・ドイツ・ロマン派の影響を受け、スペイン現代詩（マチャード兄弟、ヒメネス、世代27年）の祖型となった。",
    background="ハイネ・ドイツ・ロマン派の独自スペイン受容、後期ロマン主義から世紀末への過渡期。",
    development="スペイン世代98、世代27、20世紀スペイン詩学の祖型。",
    historical_context="19世紀後半スペイン王政復古期前夜の文化的動乱期。",
    primary_source_url=GUTEN+"ebooks/27770",
    primary_source_type="Project Gutenberg: Rimas",
    importance_score=4, source_tier="primary", canonical_in_region="major")


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
        print(f"[c06-add60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c06-add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
