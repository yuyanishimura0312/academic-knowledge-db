"""LIT-DB Phase 2 Wave 20 — C08: European Realism / Naturalism / Symbolism (+80).

Subfield: lit_eu_realism (id=5), region='西欧'.
Adds 80 NEW NON-OVERLAPPING concepts on top of existing 183.
Target after run: 263 (toward 600 goal).

Coverage (no duplicate with existing 183):
  A: French extension (Stendhal/Balzac/Flaubert/Maupassant/Sand/Loti) — 14
  B: British extension (Dickens/Hardy/Trollope/Conrad/Bennett/Wells/Ford) — 14
  C: German extension (Raabe/Keller/Meyer/Hauptmann/Schnitzler/Wassermann) — 8
  D: Italian Verismo+ (Verga/Pirandello/Deledda/Fogazzaro) — 8
  E: Spanish (Galdós/Pardo Bazán/Pereda/Valera/Blasco Ibáñez/Echegaray/Benavente) — 12
  F: Russian (Dostoevsky/Tolstoy/Turgenev/Goncharov/Saltykov/Leskov) — 12
  G: Portuguese + American Naturalism (Eça/Norris/London/Dreiser/Garland) — 8
  H: Symbolist+Decadent extras (Mallarmé/Verlaine/Rimbaud/Maeterlinck/Wilde/Pater/Dowson) — 4

>= 85% primary; fourth_transform_tags >= 24, cross_domain >= 18.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("19世紀フランス・リアリズム期", "French Realism (19th c.)", 1830, 1880,
     "ルイ・フィリップ王政期から第三共和制初期にかけてのフランス文学。"),
    ("19世紀英米・北欧リアリズム期", "British/American/Nordic Realism (19th c.)",
     1840, 1900,
     "ヴィクトリア朝中期以降の英米と北欧におけるリアリズム小説・社会劇の隆盛期。"),
    ("自然主義期", "Naturalism (late 19th c.)", 1865, 1910,
     "ゾラを中心とするフランス自然主義と、その英米・独語圏への波及期。"),
    ("ロシア・リアリズム期", "Russian Realism (19th c.)", 1840, 1910,
     "ツルゲーネフ、ゴンチャロフ、サルトィコフ＝シチェドリン、チェーホフ、ゴーリキーを擁するロシア・リアリズム期。"),
    ("イタリア・ヴェリズモ期", "Italian Verismo", 1870, 1910,
     "ヴェルガを中心とするシチリア発のヴェリズモ運動と、北イタリア・ナポリ派の写実主義。"),
    ("イベリア・リアリズム期", "Iberian Realism", 1860, 1910,
     "ガルドス、パルド・バサン、クラリン、エサ・デ・ケイロスらスペイン・ポルトガル写実主義の隆盛期。"),
    ("ドイツ詩的リアリズム期", "German Poetic Realism", 1850, 1900,
     "フォンターネ、ストルム、ケラー、ラーベらドイツ語圏の市民的・詩的リアリズム期。"),
    ("ウィーン・モデルネ期", "Viennese Modernism", 1890, 1920,
     "シュニッツラー、ホフマンスタール、ヴァッサーマンらのウィーン世紀末文学。"),
    ("英国モダニズム前夜期", "Edwardian/Pre-Modernist Britain", 1895, 1925,
     "コンラッド、フォード、ベネット、ウェルズ、ゴールズワージーらエドワード朝期英国小説。"),
    ("象徴主義・デカダンス期", "Symbolism & Decadence", 1857, 1910,
     "マラルメ、ヴェルレーヌ、ランボー、メーテルランク、ペーター、ワイルドらの象徴主義・デカダンス文学運動。"),
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
WSRC_IT = "https://it.wikisource.org/wiki/"
WSRC_ES = "https://es.wikisource.org/wiki/"
WSRC_DE = "https://de.wikisource.org/wiki/"
WSRC_RU = "https://ru.wikisource.org/wiki/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_eu_realism", region="西欧", original_script="roman")
CCYR = dict(subfield_code="lit_eu_realism", region="西欧", original_script="cyrillic")


# ============================================================
# A: フランス補完（14）
# ============================================================
add(**C, name_ja="スタンダール『ラミエル』",
    name_en="Stendhal's Lamiel",
    name_original="Lamiel",
    period_key="19世紀フランス・リアリズム期",
    definition="スタンダールが1839-42年に執筆した未完の長編（1889年刊）。ノルマンディーの孤児ラミエルが社会通念を逸脱し犯罪者と恋愛する物語。スタンダール晩年の女性主人公小説。",
    background="七月王政期フランスの女性逸脱者観察。",
    development="20世紀フランス女性小説、逸脱者文学に継承。",
    historical_context="七月王政末期フランス。",
    primary_source_url=GUTEN+"ebooks/49658",
    primary_source_type="Project Gutenberg: Lamiel",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="スタンダール『アンリ・ブリュラールの生涯』",
    name_en="Stendhal's Vie de Henry Brulard",
    name_original="Vie de Henry Brulard",
    period_key="19世紀フランス・リアリズム期",
    definition="スタンダールが1835-36年に執筆した自伝（1890年刊）。グルノーブル幼年期から1799年のミラノ初訪問までを描き、19世紀フランス自伝文学の規範となった。",
    background="王政復古末期フランスの自伝文学伝統。",
    development="プルースト、20世紀自伝小説に継承。",
    historical_context="七月王政期フランス。",
    primary_source_url=WSRC_FR+"Vie_de_Henry_Brulard",
    primary_source_type="Wikisource: Vie de Henry Brulard",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バルザック『二人の若妻の手記』",
    name_en="Balzac's Mémoires de deux jeunes mariées",
    name_original="Mémoires de deux jeunes mariées",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1841-42年に発表した書簡体小説。修道院学校友人ルイーズとルネの結婚生活を往復書簡で対比し、情熱結婚と理性結婚の対立を観察した。",
    background="七月王政期フランス女性教育と結婚観。",
    development="20世紀フランス書簡体小説、女性結婚論小説の祖型。",
    historical_context="七月王政期フランスの女性結婚論議。",
    primary_source_url=GUTEN+"ebooks/1727",
    primary_source_type="Project Gutenberg: Letters of Two Brides",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="バルザック『十三人組物語』",
    name_en="Balzac's Histoire des Treize",
    name_original="Histoire des Treize",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1833-35年に発表した三部小説連作（『フェラギュス』『ランジェ公爵夫人』『金色の眼の娘』）。パリの秘密結社「十三人組」を共通の枠組とした犯罪・恋愛・社交圏の解剖。",
    background="七月王政期パリの秘密結社的想像力。",
    development="20世紀犯罪小説、パリ群像小説の祖型。",
    historical_context="七月王政期パリ社交界。",
    primary_source_url=GUTEN+"ebooks/1334",
    primary_source_type="Project Gutenberg: History of the Thirteen",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バルザック『村の司祭』",
    name_en="Balzac's Le Curé de village",
    name_original="Le Curé de village",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1841年に発表した長編小説。リムーザン地方の女主人公ヴェロニクが過去の罪を償うため農村改良に身を捧げる物語。バルザックの社会改良論文学化。",
    background="七月王政期フランス農村開発と宗教的贖罪。",
    development="19世紀末社会改良小説、農村改革小説に継承。",
    historical_context="七月王政期フランス農村政策。",
    primary_source_url=GUTEN+"ebooks/1899",
    primary_source_type="Project Gutenberg: The Country Parson",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="フローベール書簡選集",
    name_en="Flaubert's Selected Correspondence",
    name_original="Correspondance",
    period_key="19世紀フランス・リアリズム期",
    definition="フローベール（1821-80）の40年にわたる膨大な書簡群。ルイーズ・コレ宛・ジョルジュ・サンド宛等で「正確な言葉」「非個人性」を理論化し、19世紀リアリズム詩学の最重要文献。",
    background="19世紀フランス書簡文化と作家詩学論議。",
    development="20世紀作家詩学、エクリチュール理論の理論的源泉。",
    historical_context="第二帝政〜第三共和制初期フランス文芸論議。",
    primary_source_url=WSRC_FR+"Correspondance_(Flaubert)",
    primary_source_type="Wikisource: Correspondance Flaubert",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="モーパッサン『マドモワゼル・フィフィ』",
    name_en="Maupassant's Mademoiselle Fifi",
    name_original="Mademoiselle Fifi",
    period_key="19世紀フランス・リアリズム期",
    definition="モーパッサンが1882年に発表した短編集の表題作。普仏戦争中ルーアン城を占領するプロイセン将校と地元娼婦の対立を描き、戦時の愛国と性の交差を観察した自然主義短編。",
    background="普仏戦争後フランスの戦争記憶論議。",
    development="20世紀フランス戦争短編に継承。",
    historical_context="第三共和制初期フランスの戦争記憶。",
    primary_source_url=GUTEN+"ebooks/3079",
    primary_source_type="Project Gutenberg: Mademoiselle Fifi",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="モーパッサン『イヴェット』",
    name_en="Maupassant's Yvette",
    name_original="Yvette",
    period_key="19世紀フランス・リアリズム期",
    definition="モーパッサンが1884年に発表した中編小説。パリ高級娼婦の娘イヴェットの母娘関係と社会的偽善を描き、19世紀末パリ社交界の道徳的解剖を行った。",
    background="第三共和制中期パリ社交界観察。",
    development="20世紀パリ風俗小説に継承。",
    historical_context="第三共和制中期フランス社交文化。",
    primary_source_url=GUTEN+"ebooks/3083",
    primary_source_type="Project Gutenberg: Yvette",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="モーパッサン『われらが心』",
    name_en="Maupassant's Notre Cœur",
    name_original="Notre Cœur",
    period_key="19世紀フランス・リアリズム期",
    definition="モーパッサンが1890年に発表した最後の長編小説。社交界の独身男アンドレ・マリオルとブルチカ未亡人の恋愛心理劇。モーパッサン晩年の心理リアリズム傑作。",
    background="第三共和制中期パリ社交界の心理学化。",
    development="20世紀フランス心理小説に継承。",
    historical_context="第三共和制中期フランス心理学興隆。",
    primary_source_url=GUTEN+"ebooks/3081",
    primary_source_type="Project Gutenberg: Notre Cœur",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ジョルジュ・サンド『アンディアナ』",
    name_en="Sand's Indiana",
    name_original="Indiana",
    period_key="19世紀フランス・リアリズム期",
    definition="ジョルジュ・サンドが1832年に発表したデビュー長編。クレオール出身の人妻アンディアナの結婚不満と恋愛を描き、19世紀フランス女性問題小説の起点となった。",
    background="七月王政期フランスの女性問題と離婚論議。",
    development="フランス女性文学・フェミニズム小説の祖型。",
    historical_context="七月王政期フランスの女性問題論議。",
    primary_source_url=GUTEN+"ebooks/13708",
    primary_source_type="Project Gutenberg: Indiana",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョルジュ・サンド『コンスエロ』",
    name_en="Sand's Consuelo",
    name_original="Consuelo",
    period_key="19世紀フランス・リアリズム期",
    definition="サンドが1842-43年に発表した長編小説。ヴェネチアの歌姫コンスエロが18世紀ヨーロッパ各地を遍歴する物語で、芸術家小説と歴史ロマンスを融合した。",
    background="七月王政期フランスの音楽文化と18世紀ヨーロッパ歴史復興。",
    development="20世紀フランス芸術家小説に継承。",
    historical_context="七月王政中期フランスの音楽文化。",
    primary_source_url=GUTEN+"ebooks/27098",
    primary_source_type="Project Gutenberg: Consuelo",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ジョルジュ・サンド『わが生涯の物語』",
    name_en="Sand's Histoire de ma vie",
    name_original="Histoire de ma vie",
    period_key="19世紀フランス・リアリズム期",
    definition="サンドが1854-55年に発表した自伝。ベリー地方の幼年期からショパン関係までを20巻に渡り叙述し、19世紀フランス女性自伝の規範となった。",
    background="第二共和制〜第二帝政初期フランス自伝文学。",
    development="19世紀末女性自伝、20世紀フェミニズム自伝に継承。",
    historical_context="第二帝政初期フランス。",
    primary_source_url=WSRC_FR+"Histoire_de_ma_vie_(Sand)",
    primary_source_type="Wikisource: Histoire de ma vie",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ロティ『お菊さん』",
    name_en="Loti's Madame Chrysanthème",
    name_original="Madame Chrysanthème",
    period_key="19世紀フランス・リアリズム期",
    definition="ピエール・ロティが1887年に発表した日本長編小説。長崎滞在時の仮想結婚体験を描き、プッチーニ歌劇『蝶々夫人』の源流となった。19世紀末ジャポニスム文学の代表作。",
    background="19世紀末フランスのジャポニスムと日本観察。",
    development="プッチーニ『蝶々夫人』、20世紀東洋主義文学に継承。",
    historical_context="19世紀末日仏文化交流。",
    primary_source_url=GUTEN+"ebooks/3995",
    primary_source_type="Project Gutenberg: Madame Chrysanthème",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ロティ『わが兄イヴ』",
    name_en="Loti's Mon frère Yves",
    name_original="Mon frère Yves",
    period_key="19世紀フランス・リアリズム期",
    definition="ロティが1883年に発表した自伝的長編。海軍士官ロティとブルターニュ水兵イヴの友情を描き、19世紀末フランス海軍リアリズム小説の代表作。",
    background="第三共和制中期フランス海軍と地方水兵文化。",
    development="20世紀フランス海洋小説、男性友情小説に継承。",
    historical_context="第三共和制中期フランス海軍。",
    primary_source_url=GUTEN+"ebooks/12554",
    primary_source_type="Project Gutenberg: My Brother Yves",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# B: 英国補完（14）
# ============================================================
add(**C, name_ja="ディケンズ『バーナビー・ラッジ』",
    name_en="Dickens' Barnaby Rudge",
    name_original="Barnaby Rudge",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ディケンズが1841年に発表した歴史長編。1780年ゴードン暴動を背景に、知的障害青年バーナビーと群衆暴動を描いた。19世紀英国歴史リアリズム小説の代表作。",
    background="19世紀中葉英国の歴史小説伝統と暴動記憶。",
    development="20世紀英国歴史小説、群衆心理小説に継承。",
    historical_context="ヴィクトリア朝初期英国。",
    primary_source_url=GUTEN+"ebooks/917",
    primary_source_type="Project Gutenberg: Barnaby Rudge",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ディケンズ『エドウィン・ドルードの謎』",
    name_en="Dickens' The Mystery of Edwin Drood",
    name_original="The Mystery of Edwin Drood",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ディケンズが1870年に分冊刊行中に死去し未完となった長編。アヘン中毒の聖歌隊長ジャスパーとその甥エドウィン失踪の謎を描き、英国推理小説の祖型となった。",
    background="ヴィクトリア朝後期英国のアヘン問題と推理小説興隆。",
    development="20世紀英国推理小説の祖型となった。",
    historical_context="ヴィクトリア朝後期英国。",
    primary_source_url=GUTEN+"ebooks/564",
    primary_source_type="Project Gutenberg: The Mystery of Edwin Drood",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ジョージ・エリオット『テオフラストス・サッチ』",
    name_en="Eliot's Impressions of Theophrastus Such",
    name_original="Impressions of Theophrastus Such",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ジョージ・エリオット（1819-80）が1879年に発表した最後の作品。架空の独身者テオフラストスの観察記によるエッセー集で、19世紀末英国社会・道徳論を風刺的に観察した。",
    background="ヴィクトリア朝後期英国エッセー伝統。",
    development="20世紀英国エッセー文学、社会風刺に継承。",
    historical_context="ヴィクトリア朝後期英国。",
    primary_source_url=GUTEN+"ebooks/1471",
    primary_source_type="Project Gutenberg: Impressions of Theophrastus Such",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ハーディ『青い目の二人』",
    name_en="Hardy's A Pair of Blue Eyes",
    name_original="A Pair of Blue Eyes",
    period_key="19世紀英米・北欧リアリズム期",
    definition="トマス・ハーディが1873年に発表した第三長編小説。コーンウォール牧師の娘エルフリーデを巡る青年三角関係を描き、ハーディ「ウェセックス小説」の地理的萌芽となった作品。",
    background="ヴィクトリア朝中期英国のコーンウォール地方文化。",
    development="ハーディ「ウェセックス小説」群の起点となった。",
    historical_context="ヴィクトリア朝中期英国。",
    primary_source_url=GUTEN+"ebooks/3836",
    primary_source_type="Project Gutenberg: A Pair of Blue Eyes",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ハーディ『ラッパ手長』",
    name_en="Hardy's The Trumpet-Major",
    name_original="The Trumpet-Major",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ハーディが1880年に発表した歴史長編。ナポレオン戦争期(1804-08)ドーセット海岸を舞台に、ラッパ手ジョン・ラヴデイと弟・恋人を描き、英国歴史リアリズム小説の代表作。",
    background="ヴィクトリア朝中期英国のナポレオン戦争記憶論議。",
    development="20世紀英国歴史小説に継承。",
    historical_context="ヴィクトリア朝中期英国。",
    primary_source_url=GUTEN+"ebooks/3187",
    primary_source_type="Project Gutenberg: The Trumpet-Major",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ハーディ『ウェセックス物語』",
    name_en="Hardy's Wessex Tales",
    name_original="Wessex Tales",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ハーディが1888年に編んだ初の短編集。「枯腕」「三人の男」等7篇を収録し、19世紀英国西南部地方の民俗・運命を描いた。ハーディ短編形式の規範。",
    background="ヴィクトリア朝後期英国のドーセット地方民俗。",
    development="20世紀英国地方短編に継承。",
    historical_context="ヴィクトリア朝後期英国。",
    primary_source_url=GUTEN+"ebooks/3070",
    primary_source_type="Project Gutenberg: Wessex Tales",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="トロロップ『ユースタス・ダイヤモンド』",
    name_en="Trollope's The Eustace Diamonds",
    name_original="The Eustace Diamonds",
    period_key="19世紀英米・北欧リアリズム期",
    definition="アンソニー・トロロップが1871-73年に発表した「パラサー小説」第三作。リジー・ユースタスとダイヤモンドネックレスを巡る詐欺と上流社会を描き、19世紀英国法廷リアリズム小説の代表作。",
    background="ヴィクトリア朝後期英国法廷文化と社交界。",
    development="19世紀末英国法廷小説に継承。",
    historical_context="ヴィクトリア朝後期英国。",
    primary_source_url=GUTEN+"ebooks/4894",
    primary_source_type="Project Gutenberg: The Eustace Diamonds",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="トロロップ『ドクター・ソーン』",
    name_en="Trollope's Doctor Thorne",
    name_original="Doctor Thorne",
    period_key="19世紀英米・北欧リアリズム期",
    definition="トロロップが1858年に発表した「バーチェスター物語」第三作。地方医師ソーンの姪メアリーと地主息子フランクの結婚困難を描き、19世紀英国地方ジェントリ社会のリアリズム的観察。",
    background="ヴィクトリア朝中期英国地方ジェントリ社会。",
    development="19世紀末英国地方リアリズム小説に継承。",
    historical_context="ヴィクトリア朝中期英国。",
    primary_source_url=GUTEN+"ebooks/3166",
    primary_source_type="Project Gutenberg: Doctor Thorne",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="コンラッド『密偵』",
    name_en="Conrad's The Secret Agent",
    name_original="The Secret Agent",
    period_key="英国モダニズム前夜期",
    definition="ジョゼフ・コンラッドが1907年に発表した政治長編。ロンドンに潜む無政府主義者組織と二重スパイ・ヴァーロックの家庭悲劇を描き、20世紀政治小説・テロリズム小説の祖型となった。",
    background="エドワード朝期英国の無政府主義者・テロリズム不安。",
    development="20世紀政治小説、テロリズム小説の規範となった。",
    historical_context="エドワード朝期英国。",
    primary_source_url=GUTEN+"ebooks/974",
    primary_source_type="Project Gutenberg: The Secret Agent",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"無政府主義テロと二重スパイの観察は、AI時代の情報戦・サイバーテロ問題の歴史的祖型。",
         "related_ai_phenomenon":"AI時代の情報戦とサイバーテロ"}])

add(**C, name_ja="コンラッド『西欧の眼の下に』",
    name_en="Conrad's Under Western Eyes",
    name_original="Under Western Eyes",
    period_key="英国モダニズム前夜期",
    definition="コンラッドが1911年に発表した政治長編。ロシア学生ラズーモフが革命家暗殺後にスイスへ亡命し罪を抱える物語。19世紀末ロシア政治を西欧視点から観察した代表作。",
    background="エドワード朝期英国のロシア革命前夜観察。",
    development="20世紀亡命者文学、東西認識論小説に継承。",
    historical_context="エドワード朝期英国。",
    primary_source_url=GUTEN+"ebooks/2480",
    primary_source_type="Project Gutenberg: Under Western Eyes",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フォード『パレーズ・エンド』",
    name_en="Ford's Parade's End",
    name_original="Parade's End",
    period_key="英国モダニズム前夜期",
    definition="フォード・マドックス・フォード（1873-1939）が1924-28年に発表した四部作長編。第一次大戦前後の英国貴族クリストファー・ティージェンスを描き、20世紀英国大戦小説の規範となった。",
    background="エドワード朝末期から第一次大戦期英国上流階級観察。",
    development="20世紀英国大戦小説、モダニズム長編に継承。",
    historical_context="第一次大戦期英国。",
    primary_source_url=WIKI_EN+"Parade%27s_End",
    primary_source_type="Wikipedia: Parade's End",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ベネット『老婦人物語』",
    name_en="Bennett's The Old Wives' Tale",
    name_original="The Old Wives' Tale",
    period_key="英国モダニズム前夜期",
    definition="アーノルド・ベネットが1908年に発表した長編。スタッフォードシャー陶磁器産業地帯の姉妹コンスタンスとソフィアの一生を描き、英国地方産業地帯リアリズム小説の最高傑作。",
    background="エドワード朝期英国スタッフォードシャー陶磁器産業文化。",
    development="20世紀英国地方産業小説に継承。",
    historical_context="エドワード朝期英国。",
    primary_source_url=GUTEN+"ebooks/5247",
    primary_source_type="Project Gutenberg: The Old Wives' Tale",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ベネット『クレイハンガー』",
    name_en="Bennett's Clayhanger",
    name_original="Clayhanger",
    period_key="英国モダニズム前夜期",
    definition="ベネットが1910年に発表した長編。「クレイハンガー三部作」第一作で、印刷業者の息子エドウィン・クレイハンガーの成長と父との葛藤を描いた。英国地方教養小説の代表作。",
    background="エドワード朝期英国地方印刷業文化。",
    development="20世紀英国教養小説に継承。",
    historical_context="エドワード朝期英国。",
    primary_source_url=GUTEN+"ebooks/5343",
    primary_source_type="Project Gutenberg: Clayhanger",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ウェルズ『アン・ヴェロニカ』",
    name_en="Wells' Ann Veronica",
    name_original="Ann Veronica",
    period_key="英国モダニズム前夜期",
    definition="H.G.ウェルズが1909年に発表した女性問題長編。中産階級令嬢アン・ヴェロニカが家を出て自立とフェミニスト運動に参加する物語。エドワード朝期英国フェミニズム小説の代表作。",
    background="エドワード朝期英国の女性参政権運動。",
    development="20世紀英国フェミニズム小説に継承。",
    historical_context="エドワード朝期英国。",
    primary_source_url=GUTEN+"ebooks/524",
    primary_source_type="Project Gutenberg: Ann Veronica",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# C: ドイツ補完（8）
# ============================================================
add(**C, name_ja="ラーベ『飢えた牧師』",
    name_en="Raabe's Der Hungerpastor",
    name_original="Der Hungerpastor",
    period_key="ドイツ詩的リアリズム期",
    definition="ヴィルヘルム・ラーベ（1831-1910）が1864年に発表した教養長編。靴職人の息子ハンスが牧師として成長する物語で、19世紀末ドイツ詩的リアリズム教養小説の代表作。",
    background="19世紀中葉北ドイツ市民文化と教養理想。",
    development="20世紀ドイツ教養小説に継承。",
    historical_context="19世紀中葉北ドイツ。",
    primary_source_url=WSRC_DE+"Der_Hungerpastor",
    primary_source_type="Wikisource: Der Hungerpastor",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="シュトルム『アクィス・スブメルスス』",
    name_en="Storm's Aquis Submersus",
    name_original="Aquis Submersus",
    period_key="ドイツ詩的リアリズム期",
    definition="テオドール・シュトルム（1817-88）が1876年に発表した中編小説。17世紀北ドイツの画家ヨハネスが幼馴染の人妻と再会し失った息子を描く悲劇のノヴェレ。",
    background="19世紀中葉北ドイツの17世紀文化復興。",
    development="シュトルム後期ノヴェレ群、20世紀ドイツ歴史短編に継承。",
    historical_context="19世紀末ドイツ第二帝国期。",
    primary_source_url=WSRC_DE+"Aquis_submersus",
    primary_source_type="Wikisource: Aquis submersus",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ケラー『チューリヒ短編集』",
    name_en="Keller's Züricher Novellen",
    name_original="Züricher Novellen",
    period_key="ドイツ詩的リアリズム期",
    definition="ゴットフリート・ケラー（1819-90）が1878年に発表した連作短編集。チューリヒ歴史を背景にした5篇からなり、スイス・ドイツ語圏歴史リアリズム短編の規範となった。",
    background="19世紀末スイス・チューリヒ歴史復興運動。",
    development="20世紀スイス・ドイツ語圏歴史短編に継承。",
    historical_context="19世紀末スイス。",
    primary_source_url=WSRC_DE+"Züricher_Novellen",
    primary_source_type="Wikisource: Züricher Novellen",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="マイヤー『パスカラの誘惑』",
    name_en="Meyer's Die Versuchung des Pescara",
    name_original="Die Versuchung des Pescara",
    period_key="ドイツ詩的リアリズム期",
    definition="コンラート・フェルディナント・マイヤー（1825-98）が1887年に発表した歴史中編。16世紀イタリア戦争のスペイン将軍パスカラの忠誠の試練を描き、スイス歴史ノヴェレの代表作。",
    background="19世紀末スイスのルネサンス期歴史復興。",
    development="20世紀ドイツ語圏歴史短編に継承。",
    historical_context="19世紀末スイス。",
    primary_source_url=WSRC_DE+"Die_Versuchung_des_Pescara",
    primary_source_type="Wikisource: Die Versuchung des Pescara",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ハウプトマン『日の出前』",
    name_en="Hauptmann's Vor Sonnenaufgang",
    name_original="Vor Sonnenaufgang",
    period_key="自然主義期",
    definition="ゲルハルト・ハウプトマン（1862-1946）が1889年に発表した自然主義劇デビュー作。シレジア炭鉱地帯のクラウゼ家のアルコール依存と道徳崩壊を描き、ドイツ自然主義劇の起点となった。",
    background="19世紀末ドイツ自然主義劇運動。",
    development="20世紀ドイツ社会派劇に継承。",
    historical_context="19世紀末ドイツ第二帝国期。",
    primary_source_url=WSRC_DE+"Vor_Sonnenaufgang",
    primary_source_type="Wikisource: Vor Sonnenaufgang",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハウプトマン『沈鐘』",
    name_en="Hauptmann's Die versunkene Glocke",
    name_original="Die versunkene Glocke",
    period_key="自然主義期",
    definition="ハウプトマンが1896年に発表した象徴詩劇。鐘鋳造師ハインリヒと森の精ラウテンデラインの恋愛を描き、自然主義から象徴主義への転換点となった。",
    background="19世紀末ドイツの自然主義から象徴主義への転換。",
    development="20世紀ドイツ象徴詩劇に継承。",
    historical_context="19世紀末ドイツ第二帝国期。",
    primary_source_url=GUTEN+"ebooks/14903",
    primary_source_type="Project Gutenberg: The Sunken Bell",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="シュニッツラー『アナトール』",
    name_en="Schnitzler's Anatol",
    name_original="Anatol",
    period_key="ウィーン・モデルネ期",
    definition="アルトゥル・シュニッツラー（1862-1931）が1893年に発表した7編連作の戯曲集。ウィーンの独身青年アナトールの愛人遍歴を描き、世紀末ウィーン・モデルネ劇の起点となった。",
    background="19世紀末ウィーンのデカダンス文化と心理学興隆。",
    development="20世紀ウィーン・モデルネ劇に継承。",
    historical_context="19世紀末オーストリア＝ハンガリー。",
    primary_source_url=GUTEN+"ebooks/30305",
    primary_source_type="Project Gutenberg: Anatol",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ヴァッサーマン『カスパー・ハウザー』",
    name_en="Wassermann's Caspar Hauser",
    name_original="Caspar Hauser oder die Trägheit des Herzens",
    period_key="ウィーン・モデルネ期",
    definition="ヤーコプ・ヴァッサーマン（1873-1934）が1908年に発表した歴史長編。19世紀ニュルンベルクで発見された孤児カスパー・ハウザーの謎の生涯と暗殺を描いた。",
    background="19世紀末から20世紀初頭ドイツ語圏の歴史心理小説。",
    development="20世紀ドイツ語圏歴史心理小説に継承。",
    historical_context="20世紀初頭ドイツ。",
    primary_source_url=WSRC_DE+"Caspar_Hauser_oder_die_Trägheit_des_Herzens",
    primary_source_type="Wikisource: Caspar Hauser",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"言語社会から隔離された孤児の主体形成は、AI時代の社会化なき主体生成問題の歴史的祖型。",
         "related_ai_phenomenon":"AI時代の社会化と主体形成"}])


# ============================================================
# D: イタリア・ヴェリズモ補完（8）
# ============================================================
add(**C, name_ja="ヴェルガ『エロス』",
    name_en="Verga's Eros",
    name_original="Eros",
    period_key="イタリア・ヴェリズモ期",
    definition="ジョヴァンニ・ヴェルガ（1840-1922）が1875年に発表したロマン主義長編。シチリア貴族青年アルベルトの愛欲生活を描き、ヴェリズモ転換前のヴェルガを示す重要作品。",
    background="19世紀末イタリア統一後のロマン主義小説伝統。",
    development="ヴェルガ後期ヴェリズモ運動の出発点として位置付けられた。",
    historical_context="19世紀末イタリア統一後南部社会。",
    primary_source_url=WSRC_IT+"Eros",
    primary_source_type="Wikisource: Eros (Verga)",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ヴェルガ『虎の女王』",
    name_en="Verga's Tigre reale",
    name_original="Tigre reale",
    period_key="イタリア・ヴェリズモ期",
    definition="ヴェルガが1875年に発表したロマン主義長編。ロシア女性ナタリーをめぐる青年外交官の恋愛悲劇を描き、ヴェルガ初期ロマン主義の代表作。",
    background="19世紀末イタリアのロマン主義恋愛小説伝統。",
    development="ヴェルガ・ヴェリズモ転換前の重要作品として再評価。",
    historical_context="19世紀末イタリア統一後社会。",
    primary_source_url=WSRC_IT+"Tigre_reale",
    primary_source_type="Wikisource: Tigre reale",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ヴェルガ『田舎の小説集』",
    name_en="Verga's Novelle rusticane",
    name_original="Novelle rusticane",
    period_key="イタリア・ヴェリズモ期",
    definition="ヴェルガが1883年に発表したシチリア農村短編集。「自由主義」「マラリア」等12篇収録で、シチリア農村社会の貧困・宗教・移民を観察した。",
    background="19世紀末シチリア農村社会の経済構造観察。",
    development="20世紀イタリア地方リアリズム短編に継承。",
    historical_context="19世紀末イタリア統一後南部問題。",
    primary_source_url=WSRC_IT+"Novelle_rusticane",
    primary_source_type="Wikisource: Novelle rusticane",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ピランデッロ『一人、誰でもなく、十万人』",
    name_en="Pirandello's Uno, nessuno e centomila",
    name_original="Uno, nessuno e centomila",
    period_key="イタリア・ヴェリズモ期",
    definition="ルイジ・ピランデッロが1925-26年に発表した最後の長編小説。鼻の左右の歪みに気づいたヴィタンジェロが他者の視線で構築されるアイデンティティの解体を経験する物語。",
    background="20世紀初頭イタリアの心理学とアイデンティティ哲学。",
    development="20世紀世界アイデンティティ小説の規範となった。",
    historical_context="20世紀初頭イタリア。",
    primary_source_url=WSRC_IT+"Uno,_nessuno_e_centomila",
    primary_source_type="Wikisource: Uno, nessuno e centomila",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"他者視線で構築される多重アイデンティティの物語は、AI時代のソーシャルメディア・データ・ダブル問題の歴史的祖型。",
         "related_ai_phenomenon":"AI時代のソーシャルメディアと多重アイデンティティ"}])

add(**C, name_ja="ピランデッロ『撮影者セラフィーノ・グッビオの手記』",
    name_en="Pirandello's Quaderni di Serafino Gubbio operatore",
    name_original="Quaderni di Serafino Gubbio operatore",
    period_key="イタリア・ヴェリズモ期",
    definition="ピランデッロが1915-16年に発表した長編小説（『回り続ける』改題）。映画撮影技師セラフィーノの手記による初期映画産業の文学化で、20世紀メディア小説の祖型。",
    background="20世紀初頭イタリアの初期映画産業観察。",
    development="20世紀メディア小説、技術と人間関係小説に継承。",
    historical_context="20世紀初頭イタリア。",
    primary_source_url=WSRC_IT+"Quaderni_di_Serafino_Gubbio_operatore",
    primary_source_type="Wikisource: Quaderni di Serafino Gubbio",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"映画撮影技師による機械的記録の手記は、AI時代の自動記録・観察者主体性消失問題の歴史的祖型。",
         "related_ai_phenomenon":"AI時代の自動記録と観察者主体性"}])

add(**C, name_ja="ピランデッロ『古い人と若い人』",
    name_en="Pirandello's I vecchi e i giovani",
    name_original="I vecchi e i giovani",
    period_key="イタリア・ヴェリズモ期",
    definition="ピランデッロが1909年に発表した歴史長編。1893年シチリア「ファッシ」運動を背景に、リソルジメント世代と新世代の対立を観察した。",
    background="20世紀初頭イタリアのリソルジメント評価論議。",
    development="20世紀イタリア歴史小説に継承。",
    historical_context="20世紀初頭イタリア。",
    primary_source_url=WSRC_IT+"I_vecchi_e_i_giovani",
    primary_source_type="Wikisource: I vecchi e i giovani",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="デレッダ『母』",
    name_en="Deledda's La Madre",
    name_original="La Madre",
    period_key="イタリア・ヴェリズモ期",
    definition="グラツィア・デレッダが1920年に発表した中編小説。サルデーニャの神父息子と村女性との愛欲を母親が見守る物語。デレッダの宗教的内面描写の代表作。",
    background="19世紀末サルデーニャ農村のカトリック文化。",
    development="20世紀イタリア宗教文学に継承。",
    historical_context="19世紀末サルデーニャ。",
    primary_source_url=WSRC_IT+"La_madre_(Deledda)",
    primary_source_type="Wikisource: La Madre",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="フォガッツァーロ『ダニエレ・コルティス』",
    name_en="Fogazzaro's Daniele Cortis",
    name_original="Daniele Cortis",
    period_key="イタリア・ヴェリズモ期",
    definition="アントニオ・フォガッツァーロが1885年に発表した長編小説。カトリック議員ダニエレ・コルティスといとこエレナの禁断の愛を描き、19世紀末イタリア・カトリック・リアリズム小説の代表作。",
    background="19世紀末イタリアのカトリック政治論議。",
    development="20世紀イタリア・カトリック小説に継承。",
    historical_context="19世紀末イタリア統一後社会。",
    primary_source_url=WSRC_IT+"Daniele_Cortis",
    primary_source_type="Wikisource: Daniele Cortis",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# E: スペイン補完（12）
# ============================================================
add(**C, name_ja="ガルドス『バイレン』",
    name_en="Galdós' Bailén",
    name_original="Bailén",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1873年に発表した『国民挿話集』第四作。1808年バイレンの戦いでスペイン軍がフランス軍に勝利した最初の戦いを少年ガブリエルの一人称で描いた。",
    background="19世紀末スペインの独立戦争記憶論議。",
    development="『国民挿話集』全46巻における重要作。",
    historical_context="19世紀末スペイン王政復古期。",
    primary_source_url=WSRC_ES+"Bailén",
    primary_source_type="Wikisource: Bailén",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ガルドス『サラゴサ』",
    name_en="Galdós' Zaragoza",
    name_original="Zaragoza",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1874年に発表した『国民挿話集』第六作。1808-09年サラゴサ包囲戦をガブリエル・アラセリの一人称で描き、スペイン市民抵抗の英雄叙事詩。",
    background="19世紀末スペインの独立戦争記憶論議。",
    development="『国民挿話集』における英雄叙事詩的代表作。",
    historical_context="19世紀末スペイン王政復古期。",
    primary_source_url=GUTEN+"ebooks/18092",
    primary_source_type="Project Gutenberg: Zaragoza",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ガルドス『1808年5月19日』",
    name_en="Galdós' El 19 de marzo y el 2 de mayo",
    name_original="El 19 de marzo y el 2 de mayo",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1873年に発表した『国民挿話集』第三作。1808年3月19日アランフェス暴動と5月2日マドリード蜂起を描き、スペイン独立戦争の起点を文学化した。",
    background="19世紀末スペインの独立戦争記憶論議。",
    development="『国民挿話集』スペイン国民史小説の重要作。",
    historical_context="19世紀末スペイン王政復古期。",
    primary_source_url=WSRC_ES+"El_19_de_marzo_y_el_2_de_mayo",
    primary_source_type="Wikisource: El 19 de marzo",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ガルドス『友人マンソ』",
    name_en="Galdós' El amigo Manso",
    name_original="El amigo Manso",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1882年に発表した長編小説。マドリードの哲学教師マンソが教え子の妻に恋する物語を、自己が架空人物と告白する自己反省的形式で描いた。",
    background="19世紀末スペインの心理小説興隆と知識人観察。",
    development="20世紀スペイン自己反省的小説に継承。",
    historical_context="19世紀末スペイン王政復古期。",
    primary_source_url=WSRC_ES+"El_amigo_Manso",
    primary_source_type="Wikisource: El amigo Manso",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ガルドス『ミアウ』",
    name_en="Galdós' Miau",
    name_original="Miau",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1888年に発表した長編小説。マドリード官僚ラモン・ヴィリャアミルの失職と家族の没落を描き、19世紀末スペイン都市中産階級の悲劇を観察した。",
    background="19世紀末マドリード官僚社会と中産階級没落。",
    development="20世紀スペイン都市リアリズム小説に継承。",
    historical_context="19世紀末スペイン王政復古期。",
    primary_source_url=WSRC_ES+"Miau",
    primary_source_type="Wikisource: Miau",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ガルドス『トルメント』",
    name_en="Galdós' Tormento",
    name_original="Tormento",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1884年に発表した長編小説。マドリードの孤児アマパロを巡る既婚インディアーノと神父の三角関係を描き、19世紀末スペイン都市道徳の解剖。",
    background="19世紀末マドリードのインディアーノ階級と性道徳。",
    development="20世紀スペイン都市リアリズム小説に継承。",
    historical_context="19世紀末スペイン王政復古期。",
    primary_source_url=WSRC_ES+"Tormento",
    primary_source_type="Wikisource: Tormento",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ガルドス『アンヘル・ゲーラ』",
    name_en="Galdós' Ángel Guerra",
    name_original="Ángel Guerra",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1890-91年に発表した長編小説。革命家アンヘル・ゲーラがトレドに移住し神秘主義的キリスト教へ転向する物語。19世紀末スペイン宗教論議の文学化。",
    background="19世紀末スペインの政治・宗教転換論議。",
    development="20世紀スペイン宗教文学に継承。",
    historical_context="19世紀末スペイン王政復古期。",
    primary_source_url=WSRC_ES+"Ángel_Guerra",
    primary_source_type="Wikisource: Ángel Guerra",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="パルド・バサン『ラ・トリブナ』",
    name_en="Pardo Bazán's La Tribuna",
    name_original="La Tribuna",
    period_key="イベリア・リアリズム期",
    definition="エミリア・パルド・バサンが1883年に発表した長編小説。ア・コルーニャのタバコ工場女工アマパロが共和派演説家になる物語で、スペイン女性労働者文学の先駆。",
    background="19世紀末ガリシア工場労働文化観察。",
    development="20世紀スペイン女性労働文学に継承。",
    historical_context="19世紀末スペイン王政復古期。",
    primary_source_url=WSRC_ES+"La_Tribuna",
    primary_source_type="Wikisource: La Tribuna",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ペレダ『岩山の上』",
    name_en="Pereda's Peñas arriba",
    name_original="Peñas arriba",
    period_key="イベリア・リアリズム期",
    definition="ホセ・マリア・デ・ペレダ（1833-1906）が1895年に発表した長編小説。マドリードの紳士マルセロがカンタブリア山岳村で田舎貴族として継承する物語。スペイン地方主義小説の代表作。",
    background="19世紀末カンタブリア山岳村文化。",
    development="20世紀スペイン地方リアリズム小説に継承。",
    historical_context="19世紀末スペイン王政復古期。",
    primary_source_url=WSRC_ES+"Peñas_arriba",
    primary_source_type="Wikisource: Peñas arriba",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="バレラ『フアニータ・ラ・ラルガ』",
    name_en="Valera's Juanita la Larga",
    name_original="Juanita la Larga",
    period_key="イベリア・リアリズム期",
    definition="フアン・バレラ（1824-1905）が1895年に発表した長編小説。アンダルシア村の貧しい娘フアニータと裕福な老市議の恋愛を描き、19世紀末スペイン地方ロマンス小説の代表作。",
    background="19世紀末アンダルシア地方文化観察。",
    development="20世紀スペイン地方ロマンス小説に継承。",
    historical_context="19世紀末スペイン王政復古期。",
    primary_source_url=WSRC_ES+"Juanita_la_Larga",
    primary_source_type="Wikisource: Juanita la Larga",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ブラスコ・イバニェス『葦と泥』",
    name_en="Blasco Ibáñez's Cañas y barro",
    name_original="Cañas y barro",
    period_key="イベリア・リアリズム期",
    definition="ビセンテ・ブラスコ・イバニェス（1867-1928）が1902年に発表した長編小説。バレンシア・アルブフェラ湖の漁民共同体を描き、スペイン地方自然主義小説の代表作。",
    background="19世紀末バレンシア地方の漁民・農民観察。",
    development="20世紀スペイン地方自然主義小説に継承。",
    historical_context="19世紀末スペイン王政復古期。",
    primary_source_url=WSRC_ES+"Cañas_y_barro",
    primary_source_type="Wikisource: Cañas y barro",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ブラスコ・イバニェス『黙示録の四騎士』",
    name_en="Blasco Ibáñez's Los Cuatro Jinetes del Apocalipsis",
    name_original="Los Cuatro Jinetes del Apocalipsis",
    period_key="イベリア・リアリズム期",
    definition="ブラスコ・イバニェスが1916年に発表した第一次大戦長編。アルゼンチンのスペイン系一族が大戦で分断される物語で、スペイン語圏世界文学の最初の世界的ベストセラー。",
    background="第一次大戦期スペイン語圏世界文化観察。",
    development="20世紀スペイン語圏世界文学の祖型となった。",
    historical_context="第一次大戦期スペイン。",
    primary_source_url=GUTEN+"ebooks/27418",
    primary_source_type="Project Gutenberg: The Four Horsemen",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# F: ロシア補完（12）
# ============================================================
add(**CCYR, name_ja="ドストエフスキー『ネートチカ・ネズワーノワ』",
    name_en="Dostoevsky's Netochka Nezvanova",
    name_original="Неточка Незванова",
    period_key="ロシア・リアリズム期",
    definition="フョードル・ドストエフスキー（1821-81）が1849年に発表した未完長編。孤児ネートチカの幼年期と養父音楽家エフィモフの破滅を描き、ドストエフスキー初期心理リアリズムの代表作。",
    background="19世紀中葉ロシア・リアリズム心理小説興隆。",
    development="20世紀ロシア女性自伝小説に継承。",
    historical_context="19世紀中葉ロシア帝国。",
    primary_source_url=WSRC_RU+"Неточка_Незванова",
    primary_source_type="Wikisource: Неточка Незванова",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CCYR, name_ja="ドストエフスキー『おとなしい女』",
    name_en="Dostoevsky's A Gentle Creature",
    name_original="Кроткая",
    period_key="ロシア・リアリズム期",
    definition="ドストエフスキーが1876年に『作家の日記』に発表した中編。質屋の夫が自殺した妻の独白を再構築する一人称物語で、ドストエフスキー後期心理リアリズムの代表作。",
    background="19世紀末ロシア都市中産階級の心理学化。",
    development="20世紀ロシア独白形式小説に継承。",
    historical_context="19世紀末ロシア帝国。",
    primary_source_url=GUTEN+"ebooks/2638",
    primary_source_type="Project Gutenberg: A Gentle Creature",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CCYR, name_ja="ドストエフスキー『ボボーク』",
    name_en="Dostoevsky's Bobok",
    name_original="Бобок",
    period_key="ロシア・リアリズム期",
    definition="ドストエフスキーが1873年に『作家の日記』に発表した短編。墓地で死者の会話を盗み聞きする幻想的物語で、ドストエフスキー晩年のメニッペア的グロテスク短編の代表作。",
    background="19世紀末ロシアのグロテスク文学伝統。",
    development="20世紀ロシア・グロテスク短編に継承。",
    historical_context="19世紀末ロシア帝国。",
    primary_source_url=WSRC_RU+"Бобок",
    primary_source_type="Wikisource: Бобок",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CCYR, name_ja="ドストエフスキー『作家の日記』",
    name_en="Dostoevsky's A Writer's Diary",
    name_original="Дневник писателя",
    period_key="ロシア・リアリズム期",
    definition="ドストエフスキーが1873年と1876-81年に発表した雑誌（一人雑誌）。時事評論・短編・回想を混合した形式で、19世紀末ロシア言論文化の特異な記録となった。",
    background="19世紀末ロシア言論・新聞文化観察。",
    development="20世紀ロシア知識人エッセー文学に継承。",
    historical_context="19世紀末ロシア帝国。",
    primary_source_url=WSRC_RU+"Дневник_писателя",
    primary_source_type="Wikisource: Дневник писателя",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CCYR, name_ja="トルストイ『セルギイ神父』",
    name_en="Tolstoy's Father Sergius",
    name_original="Отец Сергий",
    period_key="ロシア・リアリズム期",
    definition="レフ・トルストイ（1828-1910）が1898年に執筆した中編小説（1912年刊）。社交界貴族カサツキー公爵が修道士セルギイとして隠遁し誘惑と試練を経験する物語。トルストイ晩年の宗教文学。",
    background="19世紀末ロシア修道院文化と宗教論議。",
    development="20世紀ロシア宗教文学に継承。",
    historical_context="19世紀末ロシア帝国。",
    primary_source_url=GUTEN+"ebooks/985",
    primary_source_type="Project Gutenberg: Father Sergius",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CCYR, name_ja="トルストイ『悪魔』",
    name_en="Tolstoy's The Devil",
    name_original="Дьявол",
    period_key="ロシア・リアリズム期",
    definition="トルストイが1889年に執筆した中編小説（1911年刊）。地主青年エヴゲーニイが農婦への性的衝動と道徳的破綻を経験する物語。晩年トルストイ性道徳論の文学化。",
    background="19世紀末ロシア地主階級の性道徳観察。",
    development="20世紀ロシア性道徳文学に継承。",
    historical_context="19世紀末ロシア帝国。",
    primary_source_url=GUTEN+"ebooks/2375",
    primary_source_type="Project Gutenberg: The Devil",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CCYR, name_ja="トルストイ『家庭の幸福』",
    name_en="Tolstoy's Family Happiness",
    name_original="Семейное счастие",
    period_key="ロシア・リアリズム期",
    definition="トルストイが1859年に発表した中編小説。17歳の少女マーシャと年長後見人セルゲイの結婚生活を女性一人称で描き、トルストイ初期心理リアリズム結婚小説の代表作。",
    background="19世紀中葉ロシア地主階級女性観察。",
    development="トルストイ後期『アンナ・カレーニナ』へ理論的に継承。",
    historical_context="19世紀中葉ロシア帝国。",
    primary_source_url=GUTEN+"ebooks/986",
    primary_source_type="Project Gutenberg: Family Happiness",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CCYR, name_ja="トルストイ『幼年時代』",
    name_en="Tolstoy's Childhood",
    name_original="Детство",
    period_key="ロシア・リアリズム期",
    definition="トルストイが1852年に発表したデビュー作。三部作『幼年時代・少年時代・青年時代』第一作で、貴族少年ニコライの心理的成長を一人称で描き、ロシア・リアリズム自伝的小説の起点。",
    background="19世紀中葉ロシア・リアリズム自伝的小説伝統。",
    development="20世紀ロシア自伝的小説に継承。",
    historical_context="19世紀中葉ロシア帝国。",
    primary_source_url=GUTEN+"ebooks/2142",
    primary_source_type="Project Gutenberg: Childhood",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CCYR, name_ja="ツルゲーネフ『煙』",
    name_en="Turgenev's Smoke",
    name_original="Дым",
    period_key="ロシア・リアリズム期",
    definition="イワン・ツルゲーネフ（1818-83）が1867年に発表した長編小説。バーデン＝バーデンに集うロシア貴族・革命家の幻滅を描き、19世紀末ロシア亡命知識人観察の代表作。",
    background="19世紀末ロシア亡命知識人文化観察。",
    development="20世紀ロシア亡命者小説に継承。",
    historical_context="19世紀末ロシア帝国。",
    primary_source_url=GUTEN+"ebooks/8597",
    primary_source_type="Project Gutenberg: Smoke",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CCYR, name_ja="ツルゲーネフ『処女地』",
    name_en="Turgenev's Virgin Soil",
    name_original="Новь",
    period_key="ロシア・リアリズム期",
    definition="ツルゲーネフが1877年に発表した最後の長編小説。1870年代「ヴ・ナロード（人民の中へ）」運動の青年革命家ネジダーノフの挫折を描き、ロシア・ナロードニキ運動の文学的記録。",
    background="19世紀末ロシア・ナロードニキ運動観察。",
    development="20世紀ロシア革命運動小説に継承。",
    historical_context="19世紀末ロシア帝国。",
    primary_source_url=GUTEN+"ebooks/8581",
    primary_source_type="Project Gutenberg: Virgin Soil",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CCYR, name_ja="ゴンチャロフ『平凡物語』",
    name_en="Goncharov's An Ordinary Story",
    name_original="Обыкновенная история",
    period_key="ロシア・リアリズム期",
    definition="イワン・ゴンチャロフ（1812-91）が1847年に発表したデビュー長編。地方青年アレクサンドルがペテルブルクで叔父の影響を受け幻滅する物語。19世紀中葉ロシア・リアリズム小説の起点。",
    background="19世紀中葉ロシア地方青年のペテルブルク化観察。",
    development="ゴンチャロフ後期『オブローモフ』へ理論的に継承。",
    historical_context="19世紀中葉ロシア帝国。",
    primary_source_url=WSRC_RU+"Обыкновенная_история",
    primary_source_type="Wikisource: Обыкновенная история",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CCYR, name_ja="レスコフ『魅せられた旅人』",
    name_en="Leskov's The Enchanted Wanderer",
    name_original="Очарованный странник",
    period_key="ロシア・リアリズム期",
    definition="ニコライ・レスコフ（1831-95）が1873年に発表した中編小説。元農奴イヴァン・フリャーギンがロシア各地を遍歴する物語で、19世紀末ロシア民衆語り口リアリズムの代表作。",
    background="19世紀末ロシア民衆口承文学観察。",
    development="20世紀ロシア民衆語り口小説に継承。",
    historical_context="19世紀末ロシア帝国。",
    primary_source_url=GUTEN+"ebooks/53533",
    primary_source_type="Project Gutenberg: The Enchanted Wanderer",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# G: ポルトガル+米国自然主義（8）
# ============================================================
add(**C, name_ja="エサ・デ・ケイロス『アマロ神父の罪』",
    name_en="Eça de Queirós' O Crime do Padre Amaro",
    name_original="O Crime do Padre Amaro",
    period_key="イベリア・リアリズム期",
    definition="ジョゼ・マリア・デ・エサ・デ・ケイロス（1845-1900）が1875年に発表した長編小説。ポルトガル地方都市レイリアで若い神父アマロが下宿屋娘アメリアと不倫する物語。ポルトガル・リアリズム小説の起点。",
    background="19世紀末ポルトガル・カトリック社会観察。",
    development="20世紀ポルトガル・リアリズム小説の規範となった。",
    historical_context="19世紀末ポルトガル王国。",
    primary_source_url=WSRC_PT if False else GUTEN+"ebooks/22156",
    primary_source_type="Project Gutenberg: The Sin of Father Amaro",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="エサ・デ・ケイロス『従兄バジリオ』",
    name_en="Eça de Queirós' O Primo Basílio",
    name_original="O Primo Basílio",
    period_key="イベリア・リアリズム期",
    definition="エサ・デ・ケイロスが1878年に発表した長編小説。リスボン中産階級主婦ルイザと帰国した従兄バジリオの不倫を描き、ポルトガル都市自然主義小説の代表作。",
    background="19世紀末リスボン中産階級観察。",
    development="20世紀ポルトガル都市リアリズム小説に継承。",
    historical_context="19世紀末ポルトガル王国。",
    primary_source_url=GUTEN+"ebooks/24086",
    primary_source_type="Project Gutenberg: Cousin Bazilio",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="エサ・デ・ケイロス『ラミレス家の栄光』",
    name_en="Eça de Queirós' A Ilustre Casa de Ramires",
    name_original="A Ilustre Casa de Ramires",
    period_key="イベリア・リアリズム期",
    definition="エサ・デ・ケイロスが1900年に発表した最後の完成長編。中世由来の没落貴族ゴンサロ・ラミレスが家史小説執筆を通じてポルトガル国民史と接続する物語。",
    background="19世紀末ポルトガル没落貴族文化観察。",
    development="20世紀ポルトガル歴史小説に継承。",
    historical_context="19世紀末ポルトガル王国。",
    primary_source_url=WIKI_EN+"A_Ilustre_Casa_de_Ramires",
    primary_source_type="Wikipedia: A Ilustre Casa de Ramires",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ノリス『オクトパス』",
    name_en="Norris' The Octopus",
    name_original="The Octopus: A Story of California",
    period_key="自然主義期",
    definition="フランク・ノリス（1870-1902）が1901年に発表した長編小説。「小麦の叙事詩」三部作第一作で、カリフォルニアの小麦農場と鉄道独占資本（オクトパス）の闘争を描いた米国自然主義の最高傑作。",
    background="19世紀末米国西部の鉄道独占とポピュリズム運動。",
    development="20世紀米国社会批判小説に継承。",
    historical_context="19世紀末米国西部。",
    primary_source_url=GUTEN+"ebooks/2925",
    primary_source_type="Project Gutenberg: The Octopus",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"鉄道独占資本批判の自然主義文学化は、AI時代のテクノロジー独占資本批判の歴史的祖型。",
         "related_ai_phenomenon":"AI時代のテクノロジー独占資本"}])

add(**C, name_ja="ジャック・ロンドン『荒野の呼び声』",
    name_en="London's The Call of the Wild",
    name_original="The Call of the Wild",
    period_key="自然主義期",
    definition="ジャック・ロンドン（1876-1916）が1903年に発表した中編小説。カリフォルニア家庭犬バックがクロンダイク金鉱掘り橇犬として原始性を取り戻す物語。米国自然主義動物文学の代表作。",
    background="19世紀末アラスカ・ゴールドラッシュ観察。",
    development="20世紀米国動物文学・自然主義小説に継承。",
    historical_context="19世紀末米国西部。",
    primary_source_url=GUTEN+"ebooks/215",
    primary_source_type="Project Gutenberg: The Call of the Wild",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジャック・ロンドン『マーティン・イーデン』",
    name_en="London's Martin Eden",
    name_original="Martin Eden",
    period_key="自然主義期",
    definition="ジャック・ロンドンが1909年に発表した自伝的長編。労働者階級水夫マーティン・イーデンが独学で作家となり成功と幻滅の末に自殺する物語。米国自然主義作家小説の代表作。",
    background="19世紀末米国労働者階級の自己教育文化観察。",
    development="20世紀米国作家小説に継承。",
    historical_context="19世紀末米国西部。",
    primary_source_url=GUTEN+"ebooks/1056",
    primary_source_type="Project Gutenberg: Martin Eden",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ドライサー『シスター・キャリー』",
    name_en="Dreiser's Sister Carrie",
    name_original="Sister Carrie",
    period_key="自然主義期",
    definition="シオドア・ドライサー（1871-1945）が1900年に発表したデビュー長編。地方娘キャリー・ミーバーがシカゴで上昇しニューヨーク女優となる物語。米国都市自然主義の起点。",
    background="19世紀末米国シカゴ・ニューヨーク都市観察。",
    development="20世紀米国都市リアリズム小説の規範となった。",
    historical_context="19世紀末米国都市。",
    primary_source_url=GUTEN+"ebooks/233",
    primary_source_type="Project Gutenberg: Sister Carrie",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"地方娘の都市消費社会への上昇物語は、AI時代のソーシャルメディア上昇願望の歴史的祖型。",
         "related_ai_phenomenon":"AI時代のソーシャルメディア上昇願望"}])

add(**C, name_ja="ガーランド『街道沿いの街』",
    name_en="Garland's Main-Travelled Roads",
    name_original="Main-Travelled Roads",
    period_key="自然主義期",
    definition="ハムリン・ガーランド（1860-1940）が1891年に発表した短編集。中西部農民生活の貧困を描く6篇からなり、米国地方自然主義「ヴェリティズム」運動の起点となった。",
    background="19世紀末米国中西部農民観察。",
    development="20世紀米国地方リアリズム短編に継承。",
    historical_context="19世紀末米国中西部。",
    primary_source_url=GUTEN+"ebooks/26088",
    primary_source_type="Project Gutenberg: Main-Travelled Roads",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# H: 象徴主義・デカダンス補完（4）
# ============================================================
add(**C, name_ja="ヴェルレーヌ『昔と今』",
    name_en="Verlaine's Jadis et Naguère",
    name_original="Jadis et Naguère",
    period_key="象徴主義・デカダンス期",
    definition="ポール・ヴェルレーヌ（1844-96）が1884年に発表した詩集。「詩法（Art poétique）」を含み象徴主義詩学の理論詩として19世紀末フランス象徴主義運動の規範文献となった。",
    background="19世紀末フランス象徴主義運動の理論化。",
    development="20世紀フランス象徴主義詩学の理論的源泉。",
    historical_context="19世紀末フランス第三共和制。",
    primary_source_url=WSRC_FR+"Jadis_et_Naguère",
    primary_source_type="Wikisource: Jadis et Naguère",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"「音楽性以前にすべて」の象徴主義詩学は、AI生成詩における音楽性・意味のバランス問題の理論的祖型。",
         "related_ai_phenomenon":"AI生成詩における音楽性と意味"}])

add(**C, name_ja="ランボー『見者の手紙』",
    name_en="Rimbaud's Lettres du voyant",
    name_original="Lettres du voyant",
    period_key="象徴主義・デカダンス期",
    definition="アルチュール・ランボー（1854-91）が1871年5月にイザンバール・ドゥムニーに宛てて書いた二通の書簡。「私は他者である」「詩人は見者でなければならない」と述べ19世紀末象徴主義詩学の理論的源泉となった。",
    background="19世紀末フランス象徴主義詩学運動の起点。",
    development="20世紀フランス象徴主義・シュルレアリスム詩学の理論的源泉。",
    historical_context="19世紀末フランス第三共和制初期。",
    primary_source_url=WSRC_FR+"Lettre_à_Paul_Demeny_du_15_mai_1871",
    primary_source_type="Wikisource: Lettre du voyant",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"「私は他者である（Je est un autre）」の主体論は、AI時代の主体性脱中心化問題の理論的源泉。",
         "related_ai_phenomenon":"AI時代の主体脱中心化"}])

add(**C, name_ja="メーテルランク『蜜蜂の生活』",
    name_en="Maeterlinck's La Vie des abeilles",
    name_original="La Vie des abeilles",
    period_key="象徴主義・デカダンス期",
    definition="モーリス・メーテルランク（1862-1949）が1901年に発表したエッセー。蜜蜂の社会観察を象徴主義的形而上学と融合させ、19世紀末ベルギー象徴主義自然観察文学の代表作。1911年ノーベル文学賞主要業績の一つ。",
    background="19世紀末ベルギー象徴主義の自然観察観想化。",
    development="20世紀フランス自然観察文学に継承。",
    historical_context="19世紀末ベルギー。",
    primary_source_url=GUTEN+"ebooks/4511",
    primary_source_type="Project Gutenberg: The Life of the Bee",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ワイルド『獄中記』",
    name_en="Wilde's De Profundis",
    name_original="De Profundis",
    period_key="象徴主義・デカダンス期",
    definition="オスカー・ワイルド（1854-1900）が1897年にレディング刑務所で執筆した書簡形式エッセー（1905年刊）。元恋人アルフレッド・ダグラスへの長文書簡で、19世紀末英国デカダンスの自己反省的告白文学の代表作。",
    background="19世紀末英国デカダンス文化と告白文学伝統。",
    development="20世紀英国獄中文学・告白文学に継承。",
    historical_context="19世紀末英国ヴィクトリア朝末期。",
    primary_source_url=GUTEN+"ebooks/921",
    primary_source_type="Project Gutenberg: De Profundis",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"獄中の他者宛書簡における自己解剖は、AI時代の公的告白・自己ナラティブ生成の理論的祖型。",
         "related_ai_phenomenon":"AI時代の公的告白とナラティブ"}])


# ============================================================
# Cross-domain attachments and additional fourth_transform
# ============================================================
def _attach_cross(concept_name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


def _attach_axes(concept_name: str, ax_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("fourth_axes", [])
            c["fourth_axes"] = existing + ax_list
            return


# Additional fourth_transform tags to reach >=24
_attach_axes("スタンダール『ラミエル』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"社会通念を逸脱する女性主体の物語は、AI時代の規範外主体生成問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の規範外主体"}])
_attach_axes("スタンダール『アンリ・ブリュラールの生涯』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"自伝における記憶の再構成は、AI時代の主体的記憶生成と自伝書き換え問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の自伝記憶生成"}])
_attach_axes("バルザック『二人の若妻の手記』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"書簡体小説における二人称言語の交互生成は、AI対話生成の理論的祖型。",
     "related_ai_phenomenon":"AI対話における二人称生成"}])
_attach_axes("バルザック『十三人組物語』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"秘密結社の枠組による複数物語連結は、AI時代の物語連鎖・グラフ生成の理論的祖型。",
     "related_ai_phenomenon":"AI時代の物語連鎖グラフ"}])
_attach_axes("フローベール書簡選集", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"「正確な言葉」「非個人性」のリアリズム詩学は、AI生成における客観性問題の理論的源泉。",
     "related_ai_phenomenon":"AI生成における客観性詩学"}])
_attach_axes("モーパッサン『マドモワゼル・フィフィ』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"戦時の階級・性の交差観察は、AI時代の戦時アイデンティティ生成問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の戦時アイデンティティ"}])
_attach_axes("ジョルジュ・サンド『アンディアナ』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"クレオール出身女性の主体形成は、AI時代の周縁的アイデンティティ・自己決定問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の周縁的アイデンティティ"}])
_attach_axes("ジョルジュ・サンド『わが生涯の物語』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"女性自伝20巻の規範的形式は、AI時代の女性自伝・自己ナラティブ生成の理論的祖型。",
     "related_ai_phenomenon":"AI時代の女性自伝生成"}])
_attach_axes("ロティ『お菊さん』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"19世紀末ジャポニスムにおける異文化観察と仮想結婚は、AI時代の異文化シミュレーション問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の異文化シミュレーション"}])
_attach_axes("ディケンズ『バーナビー・ラッジ』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"群衆暴動と知的障害青年を絡める手法は、AI時代の集合行動・個別主体性の絡み合い問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の集合行動と個別主体性"}])
_attach_axes("ディケンズ『エドウィン・ドルードの謎』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"未完作品の作者死による未解決ミステリーは、AI時代の生成中断・物語完成問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の生成中断と完成"}])
_attach_axes("ハーディ『青い目の二人』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"地理的舞台「ウェセックス」の文学的構築は、AI時代の架空空間生成と一貫性維持問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の架空空間生成"}])
_attach_axes("トロロップ『ユースタス・ダイヤモンド』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"法廷リアリズムにおける証拠と物語の関係は、AI時代の生成的証拠・偽造証拠問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の生成的証拠"}])
_attach_axes("コンラッド『西欧の眼の下に』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"亡命者言語と西欧視点の媒介問題は、AI時代の翻訳・媒介言語問題の理論的祖型。",
     "related_ai_phenomenon":"AI時代の翻訳と媒介言語"}])
_attach_axes("フォード『パレーズ・エンド』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"四部作大戦小説における時間圧縮・断片化技法は、AI時代の長大物語の構造化問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の長大物語構造化"}])
_attach_axes("ベネット『老婦人物語』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"姉妹一生の対比叙述は、AI時代の生涯軌道シミュレーション・並列分析の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の生涯軌道シミュレーション"}])
_attach_axes("ハウプトマン『日の出前』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"アルコール依存・遺伝決定論の劇化は、AI時代の決定論的予測モデル批判の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の決定論的予測"}])
_attach_axes("ヴェルガ『田舎の小説集』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"シチリア方言の標準イタリア語表記化は、AI多言語生成における方言再現問題の歴史的祖型。",
     "related_ai_phenomenon":"AI多言語生成における方言"}])
_attach_axes("デレッダ『母』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"母の沈黙的監視主体性は、AI時代の沈黙的観察・モニタリング主体問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の沈黙的観察主体"}])
_attach_axes("ガルドス『友人マンソ』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"主人公が架空であることを告白する自己反省的形式は、AI生成における自己言及性の歴史的祖型。",
     "related_ai_phenomenon":"AI生成における自己言及性"}])
_attach_axes("パルド・バサン『ラ・トリブナ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"工場女工の演説者化は、AI時代の労働者声・公的発話問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の労働者声と公的発話"}])
_attach_axes("ドストエフスキー『ネートチカ・ネズワーノワ』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"幼児期の心理的形成過程の文学化は、AI時代の幼児期主体形成シミュレーション問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の幼児期主体形成"}])
_attach_axes("トルストイ『家庭の幸福』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"少女視点による結婚生活の一人称語りは、AI時代の異性主体ナラティブ生成問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の異性主体ナラティブ"}])
_attach_axes("ツルゲーネフ『煙』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"亡命知識人共同体観察は、AI時代のディアスポラ・コミュニティ分析の歴史的祖型。",
     "related_ai_phenomenon":"AI時代のディアスポラ分析"}])
_attach_axes("レスコフ『魅せられた旅人』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"民衆語り口（スカース）の文学的記録は、AI時代の口承文学・声の再現問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の口承文学再現"}])
_attach_axes("エサ・デ・ケイロス『アマロ神父の罪』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"地方カトリック社会の偽善観察は、AI時代の制度的偽善検出問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の制度的偽善検出"}])
_attach_axes("ジャック・ロンドン『荒野の呼び声』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"家庭犬から野生狼への退行物語は、AI時代の文明化と原始性の往復問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の文明化と原始性"}])
_attach_axes("ジャック・ロンドン『マーティン・イーデン』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"労働者階級独学作家の成功と幻滅は、AI時代の自己教育・成功幻滅サイクルの歴史的祖型。",
     "related_ai_phenomenon":"AI時代の自己教育と成功幻滅"}])
_attach_axes("ガーランド『街道沿いの街』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"中西部農民貧困の文学的告発は、AI時代の周縁地域貧困可視化問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の周縁地域貧困可視化"}])
_attach_axes("メーテルランク『蜜蜂の生活』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"蜜蜂集団の象徴主義観察は、AI時代の集合知能・群知能観察問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の集合知能観察"}])


# Cross-domain links (>=18)
_attach_cross("スタンダール『ラミエル』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"女性逸脱者人類学",
     "description":"社会通念を逸脱する女性主体の文学化は19世紀末逸脱者人類学の祖型。"}])
_attach_cross("バルザック『十三人組物語』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"秘密結社人類学",
     "description":"19世紀パリ秘密結社の文学化は19世紀末結社人類学の祖型。"}])
_attach_cross("バルザック『村の司祭』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"農村開発政策",
     "description":"贖罪としての農村改良物語は19世紀フランス農村政策の文学的記録。"}])
_attach_cross("フローベール書簡選集", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"リアリズム詩学理論",
     "description":"「正確な言葉」「非個人性」の理論化は19世紀末リアリズム詩学の理論的源泉。"}])
_attach_cross("モーパッサン『われらが心』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"心理リアリズム詩学",
     "description":"独身男の恋愛心理劇は19世紀末心理リアリズム詩学の規範例。"}])
_attach_cross("ロティ『お菊さん』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"ジャポニスム異文化観察",
     "description":"長崎仮想結婚体験の文学化は19世紀末日仏異文化人類学の祖型。"}])
_attach_cross("ロティ『わが兄イヴ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"ブルターニュ水兵民族誌",
     "description":"ブルターニュ水兵共同体の文学的記録は19世紀末仏国海軍民族誌の祖型。"}])
_attach_cross("ディケンズ『バーナビー・ラッジ』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"暴動・治安政策",
     "description":"1780年ゴードン暴動の文学化は19世紀英国治安政策論議の文学的記録。"}])
_attach_cross("ハーディ『ラッパ手長』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"ナポレオン戦争動員史",
     "description":"ナポレオン戦争期英国海岸防衛の文学化は英国軍事政策史の文学的記録。"}])
_attach_cross("トロロップ『ドクター・ソーン』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"地方ジェントリ家族経営",
     "description":"地方ジェントリの結婚・財産経営は19世紀英国家族経営の文学的事例。"}])
_attach_cross("コンラッド『密偵』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"無政府主義テロ政策",
     "description":"19世紀末無政府主義者組織観察は20世紀テロリズム政策の文学的祖型。"}])
_attach_cross("コンラッド『西欧の眼の下に』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"亡命者人類学",
     "description":"スイス亡命ロシア知識人の観察は19世紀末亡命者人類学の祖型。"}])
_attach_cross("フォード『パレーズ・エンド』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"大戦小説詩学",
     "description":"四部作大戦小説の時間構造は20世紀英国大戦小説詩学の規範。"}])
_attach_cross("ベネット『老婦人物語』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"地方産業地帯経営",
     "description":"スタッフォードシャー陶磁器産業の文学化は19世紀末英国産業地帯経営の文学的事例。"}])
_attach_cross("ハウプトマン『日の出前』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"労働運動と社会改革",
     "description":"シレジア炭鉱地帯の自然主義劇は19世紀末ドイツ社会改革論議の文学的記録。"}])
_attach_cross("シュニッツラー『アナトール』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"世紀末ウィーン都市民族誌",
     "description":"独身青年の愛人遍歴は19世紀末ウィーン社交界民族誌の祖型。"}])
_attach_cross("ピランデッロ『撮影者セラフィーノ・グッビオの手記』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"映画・メディア詩学",
     "description":"映画撮影技師の手記は20世紀メディア詩学の理論的祖型。"}])
_attach_cross("ピランデッロ『古い人と若い人』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"リソルジメント評価",
     "description":"シチリア・ファッシ運動の文学化は19世紀末イタリア政治論議の文学的記録。"}])
_attach_cross("フォガッツァーロ『ダニエレ・コルティス』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"カトリック政治論",
     "description":"カトリック議員の禁断の愛は19世紀末イタリア・カトリック政治論議の文学的記録。"}])
_attach_cross("ガルドス『バイレン』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"独立戦争記憶政策",
     "description":"バイレン勝利の文学化は19世紀末スペイン独立戦争記憶政策の文学的記録。"}])
_attach_cross("ガルドス『ミアウ』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"官僚機構経営",
     "description":"マドリード官僚の失職物語は19世紀末スペイン官僚機構経営の文学的事例。"}])
_attach_cross("ペレダ『岩山の上』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"カンタブリア山岳村民族誌",
     "description":"カンタブリア山岳村の文学的記録は19世紀末スペイン地方民族誌の祖型。"}])
_attach_cross("ブラスコ・イバニェス『葦と泥』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"バレンシア漁民民族誌",
     "description":"アルブフェラ湖漁民共同体の文学的描写は19世紀末スペイン漁民民族誌の祖型。"}])
_attach_cross("ブラスコ・イバニェス『黙示録の四騎士』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"第一次大戦記憶政策",
     "description":"第一次大戦アルゼンチン・スペイン系一族物語は20世紀大戦記憶の文学的記録。"}])
_attach_cross("ドストエフスキー『おとなしい女』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"独白形式詩学",
     "description":"夫の自殺妻独白再構築は19世紀末独白形式詩学の規範例。"}])
_attach_cross("ドストエフスキー『作家の日記』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"19世紀末ロシア言論政策",
     "description":"一人雑誌『作家の日記』は19世紀末ロシア言論政策の文学的記録。"}])
_attach_cross("トルストイ『セルギイ神父』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"修道院的隠遁哲学",
     "description":"修道士の誘惑と試練は19世紀末ロシア宗教哲学の文学的記録。"}])
_attach_cross("ツルゲーネフ『処女地』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"ナロードニキ運動",
     "description":"「ヴ・ナロード」運動の文学化は19世紀末ロシア・ナロードニキ運動の文学的記録。"}])
_attach_cross("エサ・デ・ケイロス『従兄バジリオ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"リスボン中産階級民族誌",
     "description":"リスボン中産階級主婦不倫物語は19世紀末ポルトガル都市民族誌の祖型。"}])
_attach_cross("ノリス『オクトパス』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"独占資本批判",
     "description":"鉄道独占資本批判の自然主義文学化は19世紀末米国独占資本論の文学的記録。"}])
_attach_cross("ドライサー『シスター・キャリー』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"米国都市消費社会民族誌",
     "description":"地方娘の都市上昇物語は19世紀末米国都市消費社会民族誌の祖型。"}])
_attach_cross("ジャック・ロンドン『マーティン・イーデン』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"作家経営・成功論",
     "description":"独学作家の成功と幻滅は19世紀末米国作家経営論の文学的事例。"}])
_attach_cross("ヴェルレーヌ『昔と今』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"象徴主義詩学",
     "description":"「詩法」は19世紀末フランス象徴主義詩学の規範文献。"}])
_attach_cross("ランボー『見者の手紙』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"主体性脱中心化",
     "description":"「私は他者である」は20世紀主体性脱中心化哲学の理論的源泉。"}])
_attach_cross("メーテルランク『蜜蜂の生活』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"昆虫社会民族誌",
     "description":"蜜蜂社会の象徴主義観察は19世紀末昆虫社会民族誌の祖型。"}])
_attach_cross("ワイルド『獄中記』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"獄中告白哲学",
     "description":"獄中での自己解剖告白は19世紀末英国デカダンス告白哲学の規範例。"}])


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
        print(f"[c08-w20] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c08-w20] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        if total:
            print(f"[c08-w20] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
