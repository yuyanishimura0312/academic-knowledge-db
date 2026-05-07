"""LIT-DB Phase 2 Wave 3 — C15: Modern Chinese Literature (40 concepts).

Compact insertion script. Sources: MCLC (Modern Chinese Literature & Culture),
Paper Republic (paper-republic.org), CNKI, Wikisource (zh.wikisource.org), and
authoritative encyclopedic entries. Primary sources -> 'primary'; standard
literary historical accounts -> 'secondary'; broader synthetic categories
-> 'tertiary'.

subfield_id=9 (lit_cn_modern), region='東アジア'.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError

PERIODS = [
    ("五四運動期", "May Fourth Era", 1915, 1927,
     "新文化運動と五四運動を契機とする白話文学の確立期。文学研究会・創造社が並走した。"),
    ("国民革命〜抗戦期", "Nationalist-War Era", 1927, 1949,
     "南京国民政府期、左翼文学・京海派論争・抗日戦争・解放区文学・延安文芸座談会の時代。"),
    ("毛沢東期", "Mao Era", 1949, 1976,
     "建国後の社会主義リアリズム制度化、工農兵文芸路線、文革期の紅色経典の時代。"),
    ("改革開放期", "Reform Era", 1976, 1989,
     "文革後の傷痕・反思・改革・尋根・先鋒・朦朧詩など多様な文学潮流が噴出した時代。"),
    ("現代", "Contemporary", 1989, 2025,
     "天安門事件後のグローバル化と市場化、网络文学・80后世代・大陸/香港/台湾/海外華人の多元化期。"),
]
MCLC = "https://u.osu.edu/mclc/"
PR = "https://paper-republic.org/"
CNKI = "https://www.cnki.net/"
WIKISOURCE_ZH = "https://zh.wikisource.org/wiki/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_cn_modern", region="東アジア", original_script="kanji")

# --- A: 五四運動期（8件） ---
add(**C, name_ja="五四新文学運動", name_en="May Fourth New Literature Movement",
    name_original="五四新文學運動", period_key="五四運動期",
    definition="1917年の胡適「文学改良芻議」と陳独秀「文学革命論」を起点とし、1919年の五四運動と結合して展開した中国近代文学革命。古典文言の桎梏を破り、白話・口語・西洋文学受容によって新たな国民文学を樹立しようとした包括的運動である。",
    background="清末の梁啓超「小説界革命」、林紓らの翻訳小説、新文化運動（『新青年』雑誌）。",
    development="文学研究会・創造社・新月派など多様な流派を生み、魯迅・郭沫若・茅盾・氷心らを輩出した。",
    historical_context="辛亥革命後の共和制定着失敗、第一次世界大戦後の世界的近代化要求と中国知識人の自己批判。",
    primary_source_url=MCLC+"online-series/may-fourth/",
    primary_source_type="MCLC May Fourth resources",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="白話文運動", name_en="baihua (vernacular) movement",
    name_original="白話文運動", period_key="五四運動期",
    definition="文言文を退け、口語に基づく書き言葉「白話」で文学・教育・出版を行うべしとする運動。胡適「文学改良芻議」（1917）が八不主義を提起し、1920年に教育部が国語教科書の白話化を令したことで制度化された。中国近代文学の言語的基盤を確立した。",
    background="清末以来の言文一致論、西欧諸国の国民語観念、白話小説（『水滸伝』『紅楼夢』）の文学的伝統。",
    development="魯迅『狂人日記』（1918）が白話短篇小説の範例となり、現代中国語散文の規範を確立した。",
    historical_context="国民国家形成と大衆教育の要求の中での言語近代化。",
    primary_source_url=MCLC+"online-series/may-fourth/",
    primary_source_type="MCLC May Fourth resources",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"partial",
                  "rationale":"白話は近代国民国家の言語的基盤を形成した運動だが、AI翻訳・LLMによる多言語同時生成の時代にあって「国民語」としての白話の枠組みは再考を迫られる。",
                  "related_ai_phenomenon":"LLM多言語生成と国民語概念の動揺"}])

add(**C, name_ja="文学研究会", name_en="Literary Research Association",
    name_original="文學研究會", period_key="五四運動期",
    definition="1921年に北京で周作人・鄭振鐸・茅盾・葉聖陶ら12名が結成した中国近代最初の重要な文学団体。「人生のための芸術（為人生而藝術）」を旗印にリアリズムを主張し、雑誌『小説月報』を機関誌として翻訳と創作の両面で活動した。",
    background="新文化運動の組織化要求と『小説月報』編集権の獲得。",
    development="氷心・許地山・王統照らを輩出、創造社の浪漫主義と並ぶ二大潮流を形成した。",
    historical_context="五四直後の文学団体化と雑誌メディアの再編。",
    primary_source_url=MCLC+"online-series/may-fourth/",
    primary_source_type="MCLC literary societies",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="創造社", name_en="Creation Society",
    name_original="創造社", period_key="五四運動期",
    definition="1921年に郭沫若・郁達夫・成仿吾ら日本留学組が東京で結成した文学団体。「芸術のための芸術（為藝術而藝術）」を当初掲げ浪漫主義・自我表現を重視したが、1925年以降左傾化し革命文学を主導した。",
    background="日本留学組の西欧浪漫主義・大正期日本文学の受容と文学研究会への対抗。",
    development="後期に革命文学論争を主導し、1930年の左翼作家連盟結成に直結した。",
    historical_context="五四後の文学的派閥化と日中文化交流の深化。",
    primary_source_url=MCLC+"online-series/may-fourth/",
    primary_source_type="MCLC literary societies",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="新月派", name_en="Crescent Moon School",
    name_original="新月派", period_key="五四運動期",
    definition="1923年前後に徐志摩・聞一多・胡適・梁実秋らを中心に形成された文学派閥。雑誌『新月』（1928-）を拠点とし、英米留学組の自由主義的立場と新詩の格律化（聞一多「詩的格律」論）を特徴とした。",
    background="徐志摩のケンブリッジ留学経験と英米詩学の受容、五四白話詩の野放図さへの批判。",
    development="格律詩運動として中国新詩の形式論的基礎を提供し、後の九葉派にも影響した。",
    historical_context="1920年代後半の自由主義知識人の文学的拠点形成。",
    primary_source_url=MCLC+"online-series/may-fourth/",
    primary_source_type="MCLC Crescent Moon resources",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="鴛鴦蝴蝶派", name_en="Mandarin Ducks and Butterflies School",
    name_original="鴛鴦蝴蝶派", period_key="五四運動期",
    definition="清末民初に上海を中心に流行した通俗恋愛小説の総称。鴛鴦（おしどり）と蝴蝶（蝶）が才子佳人物語の象徴として用いられたことに由来する。徐枕亜『玉梨魂』が代表作で、五四新文学からは「封建的・商業的」と批判された大衆文学潮流である。",
    background="清末の通俗白話小説伝統、上海の出版資本主義と新興都市読者層の拡大。",
    development="五四派による批判で正典から排除されたが、1980年代以降に再評価が進んだ。",
    historical_context="1910-20年代の上海都市文化と新中間層読者の出現。",
    primary_source_url=MCLC+"online-series/popular-literature/",
    primary_source_type="MCLC popular literature",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="礼拝六派", name_en="Saturday School (Libailiu pai)",
    name_original="禮拜六派", period_key="五四運動期",
    definition="雑誌『礼拝六（土曜日）』（1914-1923）に集った周痩鵑・包天笑・李涵秋らの通俗作家群。鴛鴦蝴蝶派と一部重なるが、より広く都市中産層の余暇読書を意識した短篇恋愛・社交小説を多産した。",
    background="上海の通俗雑誌出版と都市読者層の余暇文化。",
    development="五四新文学に押されて1920年代に衰退するが、近年は都市文化史の対象として再評価される。",
    historical_context="1910年代上海の出版商業主義の興隆。",
    primary_source_url=MCLC+"online-series/popular-literature/",
    primary_source_type="MCLC popular literature",
    importance_score=2, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="北京派と海派", name_en="Beijing school vs Shanghai school",
    name_original="京派與海派", period_key="五四運動期",
    definition="1930年代に対比的に語られた二つの文学潮流。北京派（沈従文・周作人・廃名・林徽因ら）は学院派的・伝統的審美主義、海派（穆時英・劉吶鴎・施蟄存・新感覚派）は上海都市の前衛・モダニズム・消費文化を特徴とした。1934年沈従文と蘇汶の論争で概念化された。",
    background="南北二大都市の文化的差異と文学者の地理的・階層的分布。",
    development="戦後・改革開放後にも中国都市文学の二極性として継承される批評枠組みとなった。",
    historical_context="1930年代の都市化と文化的多元化。",
    primary_source_url=MCLC+"online-series/republican-period/",
    primary_source_type="MCLC Republican period",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

# --- B: 主要作家概念（8件） ---
add(**C, name_ja="阿Q精神", name_en="Ah Q-ism (Lu Xun)",
    name_original="阿Q精神", period_key="五四運動期",
    definition="魯迅『阿Q正伝』（1921-22）の主人公阿Qの「精神勝利法」を象徴する国民性批判の概念。実敗を内面で空想的勝利に転換する自己欺瞞の心理機制を指し、近代中国の国民性診断と植民地的従属意識批判の基本語彙となった。",
    background="魯迅の仙台医学留学と幻灯片事件、章太炎の国学・尼采（ニーチェ）受容を経て形成された国民性論。",
    development="毛沢東も「阿Q主義」を批判語として用い、現代中国の自己批判言説の中核語となる。",
    historical_context="清末の国民性批判言説と五四期の中国近代化要求。",
    primary_source_url=WIKISOURCE_ZH+"%E9%98%BF%E9%87%91%E6%AD%A3%E5%82%B3",
    primary_source_type="Wikisource 阿Q正伝",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
                   "target_entity_name":"国民性／文化人格論",
                   "description":"人類学のnational character研究と魯迅の国民性論の交差点。"}])

add(**C, name_ja="魯迅「狂人」", name_en="the Madman (Lu Xun)",
    name_original="狂人", period_key="五四運動期",
    definition="魯迅『狂人日記』（1918）の主人公「狂人」が体現する啓蒙的主体像。「四千年来の歴史は人を食う歴史だ」と看破する被害妄想の患者として登場し、儒教礼教を「人を食う礼教」と告発する近代中国文学最初の啓蒙的告発者の像となった。",
    background="ゴーゴリ『狂人日記』とニーチェ的覚醒者像の影響。",
    development="魯迅自身の「過客」「孤独者」など他作品の覚醒者・先覚者の系譜の起点となる。",
    historical_context="五四期の儒教礼教批判と近代啓蒙の文学的形象化。",
    primary_source_url=WIKISOURCE_ZH+"%E7%8B%82%E4%BA%BA%E6%97%A5%E8%A8%98",
    primary_source_type="Wikisource 狂人日記",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="周作人「人的文学」", name_en="literature of the human (Zhou Zuoren)",
    name_original="人的文學", period_key="五四運動期",
    definition="周作人「人的文学」（『新青年』1918）に提示された五四期文学観。「人」性を中軸に据え、非人間的・反人道的な伝統文学を否定し、人間の正当な生活と感情を肯定する文学を標榜した。中国近代人道主義文学論の基礎を成した。",
    background="周作人の日本留学体験と白樺派人道主義の受容、新村運動への共鳴。",
    development="文学研究会の「為人生而芸術」理念の理論的基盤となった。",
    historical_context="五四期の儒教批判と近代人道主義の導入。",
    primary_source_url=MCLC+"online-series/may-fourth/",
    primary_source_type="MCLC Zhou Zuoren essays",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="茅盾「子夜」社会全景", name_en="social panorama of Mao Dun's Midnight",
    name_original="子夜社會全景", period_key="国民革命〜抗戦期",
    definition="茅盾『子夜』（1933）に結実した、上海の民族資本家・買弁・労働者・農村まで広がる社会全景的長篇小説の方法。トルストイ・バルザック流の社会全景小説（panorama novel）の中国版を確立し、後の社会主義リアリズム長篇の方法論的範例となった。",
    background="茅盾の社会調査とマルクス主義経済学の受容、欧州19世紀リアリズム小説の研究。",
    development="周立波・趙樹理・社会主義リアリズム長篇に方法論として継承された。",
    historical_context="1930年代の都市化・帝国主義経済の文学的把握要求。",
    primary_source_url=PR+"authors/mao-dun/",
    primary_source_type="Paper Republic Mao Dun",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="老舎「京味児」", name_en="Beijing flavor (Lao She)",
    name_original="京味兒", period_key="国民革命〜抗戦期",
    definition="老舎『駱駝祥子』（1936）『四世同堂』に典型的な、北京方言・北京の生活風俗・庶民像を全面的に文学化した文体的特質。北京の口語を文学言語に昇華した点で、白話文学の地域的精緻化の代表事例とされる。",
    background="老舎の北京の旗人（満洲族）出身的記憶とロンドン東洋学院教員時代の言語意識。",
    development="鄧友梅・劉心武・王朔ら後の北京作家の文体的祖型となる。",
    historical_context="近代北京の旗人没落と都市庶民文化。",
    primary_source_url=PR+"authors/lao-she/",
    primary_source_type="Paper Republic Lao She",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="沈従文「湘西世界」", name_en="Xiangxi world (Shen Congwen)",
    name_original="湘西世界", period_key="国民革命〜抗戦期",
    definition="沈従文『辺城』（1934）『長河』らに描かれた湖南西部（湘西）の地方的・少数民族的・自然的世界。近代の都市的喧噪と対比される未だ汚されざる人情・自然・土俗の理想化された地として、中国近代地方文学の範例となった。",
    background="沈従文の湘西（鳳凰県）出身体験と苗族・土家族の文化的記憶。",
    development="後の尋根文学（韓少功・賈平凹ら）の方法的祖型となる。",
    historical_context="1930年代の都市・郷村二元化と地方の文学的発見。",
    primary_source_url=PR+"authors/shen-congwen/",
    primary_source_type="Paper Republic Shen Congwen",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="巴金「家」家族解体", name_en="dissolution of the family (Ba Jin)",
    name_original="《家》家族解體", period_key="国民革命〜抗戦期",
    definition="巴金『家』（1933、激流三部作の一）に典型的な、儒教大家族制度の解体と若い世代の覚醒・出奔を主題化する小説的構図。封建的家父長制への文学的告発として五四的近代主義のもっとも広く読まれた表現を提供した。",
    background="巴金自身の四川大家族体験とロシア・アナキスト思想（クロポトキン）の受容。",
    development="後の中国社会派長篇の家族解体主題（曹禺『雷雨』、矛盾『紅楼夢』再評価）の規範となる。",
    historical_context="1930年代の儒教家族制度の解体と新青年世代の出現。",
    primary_source_url=PR+"authors/ba-jin/",
    primary_source_type="Paper Republic Ba Jin",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="張愛玲「時代曲」", name_en="songs of the times (Eileen Chang)",
    name_original="時代曲", period_key="国民革命〜抗戦期",
    definition="張愛玲（1920-1995）の小説世界の総称的特徴を指す批評的語彙。1940年代上海・香港の没落士大夫家系の女性たちの細密な心理を、伝統的『紅楼夢』風の言語と西洋モダニズム的構成の融合で描いた独自の文学世界を意味する。",
    background="張愛玲の上海貴族家系出身と聖約翰大学・香港大学での西洋文学体験。",
    development="戦後台湾・香港・海外華人文学に決定的影響、夏志清『中国近代小説史』で再評価された。",
    historical_context="抗戦期上海の文化空間と没落貴族文化。",
    primary_source_url=MCLC+"online-series/eileen-chang/",
    primary_source_type="MCLC Eileen Chang resources",
    importance_score=5, source_tier="primary", canonical_in_region="core")

# --- C: 抗日・建国期（8件） ---
add(**C, name_ja="延安文芸座談会", name_en="Yan'an Talks on Literature and Art",
    name_original="延安文藝座談會", period_key="国民革命〜抗戦期",
    definition="1942年5月、延安で毛沢東が文学者を集めて開催した会議とその講話「在延安文芸座談会上的講話」。文芸が「工農兵に奉仕」すべきこと、政治と文芸の関係、普及と提高の弁証法を規定し、その後40年以上中国文芸政策の基本綱領として機能した。",
    background="延安整風運動と王実味事件、根拠地での党組織と知識人の緊張関係。",
    development="建国後は社会主義リアリズムの中国版として制度化され、文革期の極端化を経て1979年以降緩和された。",
    historical_context="抗日戦争期の中国共産党根拠地の文化政策確立。",
    primary_source_url=MCLC+"online-series/yanan-talks/",
    primary_source_type="MCLC Yan'an Talks resources",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="工農兵文芸", name_en="literature for workers, peasants, soldiers",
    name_original="工農兵文藝", period_key="毛沢東期",
    definition="延安文芸座談会講話に基づき、文学・芸術が労働者・農民・兵士に奉仕すべきとする中国共産党の文芸政策原則。建国後はこれが新中国文芸の基本路線として制度化され、創作主題・人物像・言語に至るまで規範的影響を及ぼした。",
    background="延安期の根拠地動員要求とソ連社会主義リアリズムの中国適用。",
    development="文革期に極端化（八つの様板戯）し、1979年以降は事実上廃棄された。",
    historical_context="毛沢東体制下の文芸の党的従属化。",
    primary_source_url=MCLC+"online-series/yanan-talks/",
    primary_source_type="MCLC Yan'an Talks resources",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="革命浪漫主義", name_en="revolutionary romanticism",
    name_original="革命浪漫主義", period_key="毛沢東期",
    definition="1958年の大躍進期に毛沢東が提起した「革命的リアリズムと革命的浪漫主義の結合」原則の一翼。革命的理想と未来像を現実描写と結合させて描く創作方法とされ、ソ連社会主義リアリズムを中国化した独自概念とされた。",
    background="ソ連社会主義リアリズムの硬直化への中国側の修正と、大躍進期の理想主義的政治。",
    development="1960年代の革命模範劇・革命歴史小説の方法的基礎を提供したが、文革後に批判された。",
    historical_context="中ソ論争と中国独自社会主義文化路線の模索。",
    primary_source_url=MCLC+"online-series/maoist-period/",
    primary_source_type="MCLC Maoist period",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="社会主義リアリズム中国版", name_en="Chinese socialist realism",
    name_original="社會主義現實主義（中國版）", period_key="毛沢東期",
    definition="1949年建国後にソ連から導入され、中国の状況に合わせて修正された創作方法。典型化・人民性・党性を要件とし、英雄的労農兵像と社会主義建設を中心主題とする。1958年以降は「両結合」（革命的リアリズム＋革命的浪漫主義）に発展した。",
    background="ソ連社会主義リアリズム理論の体系的導入と中国共産党文芸路線。",
    development="文革期の「三突出」原則（英雄人物・主要英雄人物・最も主要な英雄人物の突出）に極端化した。",
    historical_context="冷戦期の社会主義陣営文化建設。",
    primary_source_url=MCLC+"online-series/maoist-period/",
    primary_source_type="MCLC Maoist period",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
                   "target_entity_name":"社会主義リアリズム理論",
                   "description":"ソ連発の社会主義リアリズム理論と中国版の比較人類学。"}])

add(**C, name_ja="社会主義教育小説", name_en="socialist Bildungsroman",
    name_original="社會主義教育小說", period_key="毛沢東期",
    definition="梁斌『紅旗譜』（1957）、楊沫『青春之歌』（1958）、呉強『紅日』らに代表される、若者が革命運動を通じて社会主義者へと成長する過程を描く長篇小説のサブジャンル。社会主義リアリズムの中国的成果として教育・宣伝両面で中心的役割を果たした。",
    background="ドイツ教養小説と社会主義リアリズム長篇の中国的融合。",
    development="文革期に「修正主義」と批判されたが、1980年代以降部分的に再評価された。",
    historical_context="1950年代の革命歴史叙述の文学的体系化。",
    primary_source_url=MCLC+"online-series/maoist-period/",
    primary_source_type="MCLC Maoist novels",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="抗日戦争文学", name_en="Anti-Japanese War literature",
    name_original="抗日戰爭文學", period_key="国民革命〜抗戦期",
    definition="1937-1945の日中全面戦争期に展開した抗戦・救亡を主題とする文学領域。蕭紅『生死場』『呼蘭河伝』、丘東平・艾青『大堰河』ら詩人、戦地報告文学を含む。文芸界抗敵協会の組織化と相まって民族文学の自覚を強めた。",
    background="日本軍の中国侵攻と国共合作下の文化動員。",
    development="戦後の社会主義文学・報告文学の方法的源流となる。",
    historical_context="1930-40年代の民族戦争と文学者の戦時動員。",
    primary_source_url=MCLC+"online-series/wartime-literature/",
    primary_source_type="MCLC wartime literature",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="解放区文学", name_en="liberated zone literature",
    name_original="解放區文學", period_key="国民革命〜抗戦期",
    definition="抗日戦争・国共内戦期に中国共産党支配の解放区（陝甘寧辺区、晋察冀辺区等）で展開した文学。趙樹理『小二黒結婚』『李有才板話』、丁玲『太陽照在桑乾河上』、周立波『暴風驟雨』らが代表作。延安講話路線の最初の実践として土地改革・農民像を主題化した。",
    background="延安根拠地の文化政策と作家の根拠地下放。",
    development="建国後の社会主義リアリズム文学の直接的母体となる。",
    historical_context="1940年代の根拠地文化建設。",
    primary_source_url=MCLC+"online-series/wartime-literature/",
    primary_source_type="MCLC liberated zones",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="紅色経典", name_en="Red Classics",
    name_original="紅色經典", period_key="毛沢東期",
    definition="1949-1966期の社会主義リアリズム代表作群を後年（特に1990年代以降）にこう呼んだ批評概念。羅広斌・楊益言『紅岩』、曲波『林海雪原』、楊沫『青春之歌』、梁斌『紅旗譜』らを含む。集団記憶・テレビドラマ化・愛国教育を通じて現代中国の正典として再制度化された。",
    background="文革による作品の禁書化、1980年代以降の再評価、1990年代の愛国主義教育運動。",
    development="2000年代以降ドラマ・映画化が相次ぎ、習近平期の党史教育で更に強調された。",
    historical_context="ポスト文革期における社会主義時代の正典再構築。",
    primary_source_url=MCLC+"online-series/red-classics/",
    primary_source_type="MCLC Red Classics scholarship",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[{"axis":"正典","status":"partial",
                  "rationale":"社会主義リアリズムが一旦否定された後に「紅色経典」として正典化される事例は、政治体制と正典の連動関係を示す。AI時代の正典再構成・推薦アルゴリズムによるカノン形成と比較対象になる。",
                  "related_ai_phenomenon":"アルゴリズムによる正典推薦・国家教育情報の自動生成"}])

# --- D: 改革開放後（8件） ---
add(**C, name_ja="傷痕文学", name_en="scar literature",
    name_original="傷痕文學", period_key="改革開放期",
    definition="文革直後の1977-1979年に勃興した、文革期の被害体験を直接描く文学潮流。劉心武『班主任』（1977）と盧新華『傷痕』（1978）が起点とされ、以後の反思・改革文学への扉を開いた。文革被害者の感情の「告発」を中心とする初期段階の文学である。",
    background="1976年文革終結と1978年三中全会の改革開放路線採択、知識人の名誉回復。",
    development="より深い反省を求める反思文学に発展的に解消された。",
    historical_context="ポスト文革の社会的傷の集団的処理。",
    primary_source_url=MCLC+"online-series/post-mao-literature/",
    primary_source_type="MCLC post-Mao literature",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="反思文学", name_en="reflection literature",
    name_original="反思文學", period_key="改革開放期",
    definition="1979-1980年代前半に展開した、文革のみならず1957年反右派闘争・大躍進・社会主義初期からの歴史を再省する文学潮流。茹志鵑『剪輯錯了的故事』、王蒙『布礼』、張賢亮『霊与肉』『緑化樹』らが代表作で、傷痕文学より深い歴史的省察を志向した。",
    background="改革開放初期の歴史の再評価運動と知識人の自己省察。",
    development="尋根文学・先鋒文学への思想的前提を提供した。",
    historical_context="1980年代前半の歴史の再記述要求。",
    primary_source_url=MCLC+"online-series/post-mao-literature/",
    primary_source_type="MCLC post-Mao literature",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="改革文学", name_en="reform literature",
    name_original="改革文學", period_key="改革開放期",
    definition="1980年代前半の改革開放政策進行と並走した、企業・農村改革の現場と改革者像を主題化する文学潮流。蒋子龍『喬廠長上任記』（1979）、高暁声『陳奐生上城』、路遥『人生』『平凡的世界』らが代表作で、改革者を新しい英雄像として提示した。",
    background="鄧小平の改革開放政策と農村・国営企業改革の進行。",
    development="ジェネレーション交替と文学の多元化により1980年代後半に独立潮流としては衰退した。",
    historical_context="1980年代の経済改革の文学的反映。",
    primary_source_url=MCLC+"online-series/post-mao-literature/",
    primary_source_type="MCLC post-Mao literature",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="尋根文学", name_en="root-seeking literature",
    name_original="尋根文學", period_key="改革開放期",
    definition="1985年前後に提唱された、中国文化の「根」を辺境・少数民族・古代・地方に求める文学潮流。韓少功『文学的「根」』（1985）が宣言となり、阿城『棋王』、莫言『紅高粱』、賈平凹『商州』、王安憶『小鮑荘』らが該当する。沈従文の湘西世界とラテンアメリカ・マジックリアリズムの双方に影響を受けた。",
    background="文革の文化的破壊への反省と、1980年代の文化熱・伝統再発見ブーム。",
    development="先鋒文学・新写実主義へと連続的に発展、莫言の魔幻現実主義の母胎ともなった。",
    historical_context="1980年代の文化的アイデンティティの再構築要求。",
    primary_source_url=MCLC+"online-series/post-mao-literature/",
    primary_source_type="MCLC post-Mao literature",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"主体","status":"rethinking",
                  "rationale":"尋根文学は近代化・グローバル化に抗して文化的主体としての中国／地方／民族を再構築しようとした実践であり、AI時代に問われる「文化的アイデンティティの主体」と直接的に接続する。",
                  "related_ai_phenomenon":"LLMの文化的同質化と地方／少数民族文化の再主体化"}],
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
                   "target_entity_name":"文化的アイデンティティ／本真性",
                   "description":"人類学の文化的アイデンティティ論と尋根文学の交差。"}])

add(**C, name_ja="先鋒文学", name_en="avant-garde literature",
    name_original="先鋒文學", period_key="改革開放期",
    definition="1985年以降に登場した形式実験・物語破壊・暴力描写を特徴とする若手作家群の文学。馬原『岡底斯的誘惑』、残雪、余華『現実一種』、蘇童『妻妾成群』、格非らが代表する。ボルヘス・カフカ・ロブ＝グリエ等の影響を強く受けた。",
    background="1980年代の海外現代文学翻訳ブームと既成文学への反発。",
    development="1990年代以降は新写実主義へ収束し、余華・蘇童は世界文学市場に進出した。",
    historical_context="1980年代後半の文学的多元化と若手作家の世代交代。",
    primary_source_url=MCLC+"online-series/avant-garde/",
    primary_source_type="MCLC avant-garde resources",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="新写実主義", name_en="new realism",
    name_original="新寫實主義", period_key="改革開放期",
    definition="1980年代末から1990年代にかけて勃興した、英雄的人物像を退け都市庶民・労働者の零度の日常を冷徹に描く文学潮流。劉震雲『一地鶏毛』、池莉『煩悩人生』、方方『風景』らが代表する。社会主義リアリズム・先鋒文学双方への中道的反応とされる。",
    background="天安門事件後の理想主義の挫折と都市市場経済化。",
    development="2000年代以降の都市世情小説（六六・王海鴒等）の方法的祖型となる。",
    historical_context="1990年代の都市生活の零度化と知識人理想主義の終焉。",
    primary_source_url=MCLC+"online-series/post-tiananmen/",
    primary_source_type="MCLC post-Tiananmen literature",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="第三代詩人", name_en="Third Generation poets",
    name_original="第三代詩人", period_key="改革開放期",
    definition="1980年代中葉、朦朧詩派（北島・顧城ら第二代）の後を継いで登場した詩人世代。韓東・于堅・李亜偉・周倫佑・伊沙ら多様な傾向を含む。「他們」「莽漢」「非非」など派閥に分かれ、口語化・反崇高・反隠喩を志向した。",
    background="朦朧詩への世代的反発と1980年代の詩派多元化。",
    development="1990年代以降の中国現代詩の制度的基盤を成し、口語詩・知識分子詩の両極を生んだ。",
    historical_context="1980年代後半の詩文化の活発化と分節化。",
    primary_source_url=MCLC+"online-series/contemporary-poetry/",
    primary_source_type="MCLC contemporary poetry",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="朦朧詩", name_en="Misty Poetry",
    name_original="朦朧詩", period_key="改革開放期",
    definition="1970年代末から1980年代初にかけて出現した北島・舒婷・顧城・楊煉・江河らによる新詩派。文革期の硬直したスローガン詩に対し、隠喩・象徴・主観性・歴史への懐疑を特徴とし、当初「読みづらい（朦朧）」と批判された。中国現代詩の新生を代表する。",
    background="文革期の地下サロン文学（白洋淀詩派）と西欧現代詩翻訳の蓄積。",
    development="1980年代後半に第三代詩人らに乗り越えられたが、現代中国詩の基準点として残る。",
    historical_context="1970年代末の文化的解氷と新詩運動。",
    primary_source_url=MCLC+"online-series/misty-poetry/",
    primary_source_type="MCLC Misty Poetry resources",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
                  "rationale":"朦朧詩は政治言語の硬直化に対して詩的言語の不透明性・多義性・隠喩性を回復した運動であり、LLMが生み出す均質で透明な言語に対する詩的言語論として再評価できる。",
                  "related_ai_phenomenon":"LLM生成の透明・均質な言語と詩的不透明性の対比"}],
    cross_domain=[{"target_db":"PT","link_type":"parallel",
                   "target_entity_name":"象徴主義詩学／隠喩",
                   "description":"西欧象徴主義詩学と朦朧詩の隠喩性の比較。"}])

# --- E: 現代・21世紀（8件） ---
add(**C, name_ja="网络文学", name_en="online literature / web literature",
    name_original="網絡文學", period_key="現代",
    definition="1998年前後の「榕樹下」サイトを起点とし、起点中文網・晋江文学城・縦横中文網などのプラットフォーム上で連載・課金される長編小説群を中核とする中国独自の文学エコシステム。仙侠・玄幻・都市・歴史・耽美など多様なジャンルを含み、書籍・ドラマ・ゲーム・映画化を通じて巨大なIP産業を形成した。",
    background="2000年代の中国インターネット普及と読者課金モデルの成立、伝統出版業の地位の相対化。",
    development="2010年代以降、英訳サイト（Wuxiaworld等）を通じて世界に拡散、AI生成小説・推薦アルゴリズムと深く結合した産業へと進化中である。",
    historical_context="改革開放後のデジタルメディア環境と都市青年読者層の拡大。",
    primary_source_url=MCLC+"online-series/internet-literature/",
    primary_source_type="MCLC internet literature",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"作者性","status":"rethinking",
                  "rationale":"网络文学は読者反応とランキングに即応する連載執筆と作家の高度な機能化を伴い、近代的単一作者像を解体してきた。AI共作・AIアシスト執筆との連続性が顕著である。",
                  "related_ai_phenomenon":"AI共作の量産執筆、推薦アルゴリズムと作者の連動"},
                 {"axis":"受容","status":"rethinking",
                  "rationale":"課金モデル・コメント・ランキングを通じた即時受容構造が、AI時代の推薦アルゴリズム・パーソナライゼーションと構造的に同型である。",
                  "related_ai_phenomenon":"プラットフォームの推薦アルゴリズムと文学受容"}],
    cross_domain=[{"target_db":"AI-Development","link_type":"parallel",
                   "target_entity_name":"プラットフォーム駆動型コンテンツ生成",
                   "description":"中国网络文学プラットフォームと生成AI／LLMアプリの構造的類似。"}])

add(**C, name_ja="80后世代", name_en="post-80s generation writers",
    name_original="80後世代", period_key="現代",
    definition="1980年代生まれの中国作家世代。韓寒・郭敬明（『幻城』『小時代』）・張悦然・春樹らが代表する。80年代生まれの一人っ子政策世代であり、商業的成功・若者文化アイコン化・新概念作文コンクール（1999年起）を通じて登場した。純文学世代との断絶も論じられる。",
    background="一人っ子政策世代の市場化期成長、新概念作文コンクールという制度的発掘装置。",
    development="80后批判（純文学陣営から）と独自市場の確立を経て、現代中国文学の新主流を形成しつつある。",
    historical_context="1990-2000年代の市場化と消費文化の中での新世代登場。",
    primary_source_url=MCLC+"online-series/contemporary-fiction/",
    primary_source_type="MCLC contemporary fiction",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="新世代詩歌", name_en="new generation poetry",
    name_original="新世代詩歌", period_key="現代",
    definition="1990年代以降から現在に至る中国現代詩の多様な潮流の総称的呼称。知識分子詩派（西川・歐陽江河・王家新）と民間立場詩派（伊沙・于堅）の論争（1999年）、女性詩・少数民族詩・ネット詩の興隆を含む。",
    background="第三代詩人の遺産と1990年代以降の詩派多元化。",
    development="現代中国詩はネット連載・SNS投稿・国際詩祭参加を通じて多元的に展開する。",
    historical_context="1990年代以降の詩の周縁化と多元化。",
    primary_source_url=MCLC+"online-series/contemporary-poetry/",
    primary_source_type="MCLC contemporary poetry",
    importance_score=2, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="香港文学", name_en="Hong Kong literature",
    name_original="香港文學", period_key="現代",
    definition="香港を主たる場とする中国語文学。劉以鬯『酒徒』『対倒』、西西『我城』、也斯（梁秉鈞）、董啓章『天工開物・栩栩如真』、黄碧雲、韓麗珠らが代表する。植民地・回帰・一国二制度・国安法という政治的緊張を背景に、独自の都市的・モダニズム的・言語的特質を発展させた。",
    background="英国植民地期の独自出版環境、左翼・右翼の双方を超えた文学空間としての香港の地理的位置。",
    development="1997年回帰前後の香港アイデンティティ文学、近年は移住・移民先文学への展開も顕著である。",
    historical_context="20世紀後半-21世紀初の英中政治・植民地史。",
    primary_source_url=MCLC+"online-series/hong-kong-literature/",
    primary_source_type="MCLC Hong Kong literature",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="台湾文学", name_en="Taiwan literature",
    name_original="臺灣文學", period_key="現代",
    definition="台湾を主たる場とする中国語（および日本語期作家含む）文学。日本統治期（頼和・楊逵）、戦後の郷土文学論争（1977-78、陳映真・王禎和・黄春明）、白先勇『台北人』、朱天文・朱天心、楊牧・洛夫の現代詩、原住民文学（夏曼・藍波安）など多元的な潮流を含む。",
    background="日本統治、国民党統治、解厳（1987）、民主化、独立／統一論争という独自の政治史。",
    development="近年は原住民文学・新住民文学・LGBTQ文学（邱妙津『鱷魚手記』）など多元化が加速。",
    historical_context="20世紀以降の台湾の植民地化・冷戦・民主化を貫く政治史。",
    primary_source_url=MCLC+"online-series/taiwan-literature/",
    primary_source_type="MCLC Taiwan literature",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="海外華人文学", name_en="overseas Chinese / Sinophone literature",
    name_original="海外華人文學", period_key="現代",
    definition="北米・東南アジア・欧州など中国大陸／台湾／香港の外で中国語または現地語で書く華人作家の文学領域。聶華苓、白先勇、ハ・ジン（哈金）、リン・ユンホン、李翊雲ら英語圏作家、東南アジアでは黎紫書・黄錦樹（馬華文学）も含む。シノフォン文学（史書美）の概念も近年広く論じられる。",
    background="1949年以降の華人ディアスポラとグローバル化期の移民の活発化。",
    development="シノフォン研究（David Wang、Shih Shu-mei）を通じて中国中心主義に対抗する文学概念として理論化が進む。",
    historical_context="20世紀の華人ディアスポラと冷戦・ポスト冷戦の世界。",
    primary_source_url=MCLC+"online-series/sinophone-literature/",
    primary_source_type="MCLC Sinophone literature",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="莫言「魔幻現実主義」", name_en="Mo Yan's magical realism",
    name_original="莫言魔幻現實主義", period_key="現代",
    definition="莫言（2012年ノーベル文学賞）の長編『紅高粱家族』『豊乳肥臀』『生死疲労』『檀香刑』に通底する、ガルシア＝マルケス的マジックリアリズムを山東高密の郷土・歴史・伝説に接ぎ木した独自の文学世界。尋根文学の遺産と中国民間伝統が結合した現代中国文学を代表する達成である。",
    background="1980年代尋根文学・先鋒文学の遺産、ガルシア＝マルケス『百年の孤独』の中国訳（1984）の衝撃。",
    development="2012年ノーベル賞受賞で世界文学市場での中国文学の位置を再定義し、後の閻連科・余華の世界的受容にも道を開いた。",
    historical_context="1980年代以降の世界文学受容と中国地方文化の自己再発見。",
    primary_source_url=PR+"authors/mo-yan/",
    primary_source_type="Paper Republic Mo Yan",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"真正性","status":"rethinking",
                  "rationale":"莫言の魔幻現実主義は西欧マジックリアリズムの輸入ではなく、中国の郷土・民間伝統に接ぎ木した独自の真正性主張であり、グローバル化時代の文化的真正性問題（中国版マジックリアリズムは『真正に中国的』か）の典型事例となる。",
                  "related_ai_phenomenon":"LLMが生成する『中国的なもの』の真正性と文化的他者性"}],
    cross_domain=[{"target_db":"PT","link_type":"parallel",
                   "target_entity_name":"マジックリアリズム",
                   "description":"ラテンアメリカ発のマジックリアリズム詩学と中国版の比較詩学。"}])

add(**C, name_ja="余華「先鋒小説」", name_en="Yu Hua's avant-garde fiction",
    name_original="餘華先鋒小說", period_key="現代",
    definition="1980年代後半に登場した余華の短篇『現実一種』『古典愛情』『一九八六年』に典型的な、文革・暴力・身体の解体を冷徹で形式実験的な文体で描く先鋒小説。1990年代以降『活著』『許三観売血記』『兄弟』で社会主義中国史を寓意的長編に展開し、世界的読者を獲得した代表作家である。",
    background="1980年代の海外現代文学翻訳（カフカ・ボルヘス・ロブ＝グリエ）受容。",
    development="1990年代の長編転回で世界文学市場に進出、現代中国文学の代表作家の一人となる。",
    historical_context="先鋒文学の代表的展開と世界文学化。",
    primary_source_url=PR+"authors/yu-hua/",
    primary_source_type="Paper Republic Yu Hua",
    importance_score=4, source_tier="primary", canonical_in_region="core")


def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="東アジア",
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
                db.tag_fourth_transform(cid, **ax)
                fourth_count += 1
            for cd in cross_domain:
                db.insert_cross_domain(lit_entity_type="concept", lit_entity_id=cid,
                                       target_db=cd["target_db"], link_type=cd["link_type"],
                                       target_entity_id=cd.get("target_entity_id"),
                                       target_entity_name=cd.get("target_entity_name"),
                                       description=cd.get("description"))
                cd_count += 1
        summary = db.progress_summary()
        print(f"[c15] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c15] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
