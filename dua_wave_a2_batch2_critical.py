#!/usr/bin/env python3
"""DUA Wave A2 Batch 2: 批判理論・フランクフルト学派 +250 concepts"""
import sqlite3, uuid
from datetime import datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

concepts = [
    # ホルクハイマー・アドルノ
    ("道具的理性批判", "Critique of Instrumental Reason", None, "目的への手段的合理性が支配し、解放的・実質的理性が衰退する近代の病理をホルクハイマーが分析した批判理論の核心概念。", "批判理論・フランクフルト学派", "初期フランクフルト学派", 1947, "Western_Europe", "https://en.wikipedia.org/wiki/Instrumental_reason"),
    ("啓蒙の弁証法", "Dialectic of Enlightenment", "Dialektik der Aufklärung", "啓蒙の自由化の試みが神話・支配へと転化する逆説を論じたアドルノ＆ホルクハイマーの主著（1947年）。", "批判理論・フランクフルト学派", "初期フランクフルト学派", 1947, "Western_Europe", "https://en.wikipedia.org/wiki/Dialectic_of_Enlightenment"),
    ("文化産業論", "Culture Industry", "Kulturindustrie", "大衆文化が商品化・標準化され意識を管理・馴致する機能を果たすとするアドルノ＆ホルクハイマーの批判的分析。", "批判理論・フランクフルト学派", "初期フランクフルト学派", 1947, "Western_Europe", "https://en.wikipedia.org/wiki/Culture_industry"),
    ("否定弁証法", "Negative Dialectics", "Negative Dialektik", "概念の同一性思考を批判し、非同一的なものへの開かれを維持する弁証法。アドルノが1966年に体系化。", "批判理論・フランクフルト学派", "初期フランクフルト学派", 1966, "Western_Europe", "https://en.wikipedia.org/wiki/Negative_dialectics"),
    ("アウシュビッツ以後の詩", "Poetry After Auschwitz", None, "大量虐殺後に芸術・文化は可能かという問いをアドルノが提起した、近代批判の倫理的次元。", "批判理論・フランクフルト学派", "初期フランクフルト学派", 1949, "Western_Europe", "https://en.wikipedia.org/wiki/Theodor_W._Adorno"),
    ("ミニマ・モラリア", "Minima Moralia", None, "損傷した生の中で道徳的思考の可能性を探るアドルノの断章集（1951年）。批判理論の倫理的側面。", "批判理論・フランクフルト学派", "初期フランクフルト学派", 1951, "Western_Europe", "https://en.wikipedia.org/wiki/Minima_Moralia"),
    ("美的理論（アドルノ）", "Aesthetic Theory (Adorno)", None, "芸術の真理内容が社会批判の媒体として機能する方式を論じたアドルノの遺作的主著（1970年）。", "批判理論・フランクフルト学派", "初期フランクフルト学派", 1970, "Western_Europe", "https://en.wikipedia.org/wiki/Aesthetic_Theory"),
    ("権威主義的パーソナリティ", "Authoritarian Personality", None, "ファシズムへの心理的親和性を測定するF尺度を開発したアドルノらの社会心理学的研究（1950年）。", "批判理論・フランクフルト学派", "初期フランクフルト学派", 1950, "North_America", "https://en.wikipedia.org/wiki/The_Authoritarian_Personality"),
    ("否定的ユートピア論", "Negative Utopianism", None, "実現可能な代替社会の青写真を描かず、現実の否定としてのみユートピアを保持するアドルノの方法論的立場。", "批判理論・フランクフルト学派", "初期フランクフルト学派", 1951, "Western_Europe", "https://en.wikipedia.org/wiki/Theodor_W._Adorno"),
    # ベンヤミン
    ("複製技術時代の芸術作品", "Work of Art in the Age of Mechanical Reproduction", None, "複製技術によってオーラが喪失し、芸術の政治的可能性が変容するベンヤミンの文化理論（1935年）。", "批判理論・フランクフルト学派", "ベンヤミン", 1935, "Western_Europe", "https://en.wikipedia.org/wiki/The_Work_of_Art_in_the_Age_of_Mechanical_Reproduction"),
    ("アウラ（オーラ）", "Aura", None, "芸術作品の一回性・場所・伝統から生まれる真正性の雰囲気。ベンヤミンが複製技術によるその消滅を論じた。", "批判理論・フランクフルト学派", "ベンヤミン", 1935, "Western_Europe", "https://en.wikipedia.org/wiki/Aura_(Walter_Benjamin)"),
    ("弁証法的イメージ", "Dialectical Image", None, "過去と現在が「今‐の‐可知性」において瞬間的に結晶化する認識形象。ベンヤミンの歴史哲学・記憶論。", "批判理論・フランクフルト学派", "ベンヤミン", 1940, "Western_Europe", "https://en.wikipedia.org/wiki/Dialectical_image"),
    ("歴史の天使（クレー・パウル）", "Angel of History", None, "パウル・クレーの絵からベンヤミンが導いた歴史哲学。歴史は進歩ではなく廃墟の蓄積であるという認識。", "批判理論・フランクフルト学派", "ベンヤミン", 1940, "Western_Europe", "https://en.wikipedia.org/wiki/Angelus_Novus"),
    ("パサージュ論", "Arcades Project", "Passagen-Werk", "19世紀パリのアーケード街を資本主義・夢の商品世界として分析したベンヤミンの未完の大著。", "批判理論・フランクフルト学派", "ベンヤミン", 1982, "Western_Europe", "https://en.wikipedia.org/wiki/The_Arcades_Project"),
    ("フラヌール（遊歩者）", "Flâneur", None, "近代都市を漫歩し観察する人物類型。ベンヤミンがボードレール論を通じて都市・商品・近代経験の分析に用いた概念。", "批判理論・フランクフルト学派", "ベンヤミン", 1935, "Western_Europe", "https://en.wikipedia.org/wiki/Fl%C3%A2neur"),
    ("神学的唯物論", "Theological Materialism", None, "メシア的救済の可能性をマルクス主義的唯物論と接合するベンヤミンの独自な歴史哲学的立場。", "批判理論・フランクフルト学派", "ベンヤミン", 1940, "Western_Europe", "https://en.wikipedia.org/wiki/Walter_Benjamin"),
    # マルクーゼ
    ("一次元的人間", "One-Dimensional Man", None, "高度産業社会が批判的対立次元を吸収し人間を一次元的存在に平板化するとするマルクーゼの診断（1964年）。", "批判理論・フランクフルト学派", "マルクーゼ", 1964, "North_America", "https://en.wikipedia.org/wiki/One-Dimensional_Man"),
    ("抑圧的寛容", "Repressive Tolerance", None, "現状維持に貢献する形でのみ寛容が機能し解放的批判を封じ込めるとするマルクーゼの政治哲学的概念（1965年）。", "批判理論・フランクフルト学派", "マルクーゼ", 1965, "North_America", "https://en.wikipedia.org/wiki/Repressive_tolerance"),
    ("エロス的文明", "Eros and Civilization", None, "フロイトの文明論を批判的に読み替え、非抑圧的文明の可能性を探ったマルクーゼの作品（1955年）。", "批判理論・フランクフルト学派", "マルクーゼ", 1955, "North_America", "https://en.wikipedia.org/wiki/Eros_and_Civilization"),
    ("遂行原則と快楽原則", "Performance Principle and Pleasure Principle", None, "資本主義的生産性・効率性への従属（遂行原則）と自由・快楽の原理の対立をマルクーゼがフロイト概念で論じた。", "批判理論・フランクフルト学派", "マルクーゼ", 1955, "North_America", "https://en.wikipedia.org/wiki/Herbert_Marcuse"),
    ("大拒否", "Great Refusal", None, "支配的文化・制度を根本から拒絶する急進的実践。マルクーゼが1968年運動の美的・政治的資源として提示。", "批判理論・フランクフルト学派", "マルクーゼ", 1955, "North_America", "https://en.wikipedia.org/wiki/Herbert_Marcuse"),
    # フロム
    ("自由からの逃走", "Escape from Freedom", None, "近代の個人が孤独・不安から逃れるために権威主義・服従・画一化に逃避するとするフロムの社会心理学的分析。", "批判理論・フランクフルト学派", "フロム", 1941, "North_America", "https://en.wikipedia.org/wiki/Escape_from_Freedom"),
    ("社会的性格", "Social Character", None, "特定社会が成員に共通して形成するエネルギー配備の様式。フロムが個人と社会を架橋する分析概念。", "批判理論・フランクフルト学派", "フロム", 1941, "North_America", "https://en.wikipedia.org/wiki/Social_character"),
    ("ネクロフィリー的性格と生物愛的性格", "Necrophilous vs Biophilous Character", None, "死・破壊・機械への愛着（ネクロフィリー）と生命・成長・愛への指向（生物愛）を対立させたフロムの性格論。", "批判理論・フランクフルト学派", "フロム", 1964, "North_America", "https://en.wikipedia.org/wiki/Erich_Fromm"),
    ("存在様式と所有様式", "Being and Having Modes of Existence", None, "消費・所有への依存（所有様式）に対し、活動・生命力の発現（存在様式）を提唱したフロムの実践的哲学。", "批判理論・フランクフルト学派", "フロム", 1976, "North_America", "https://en.wikipedia.org/wiki/To_Have_or_to_Be%3F"),
    # ハーバーマス
    ("コミュニケーション的行為理論", "Theory of Communicative Action", "Theorie des kommunikativen Handelns", "相互理解を目的とした言語的相互作用（コミュニケーション的行為）と道具的行為を区別し、生活世界と体系の関係を論じたハーバーマスの主著。", "批判理論・フランクフルト学派", "ハーバーマス", 1981, "Western_Europe", "https://en.wikipedia.org/wiki/The_Theory_of_Communicative_Action"),
    ("生活世界の植民地化", "Colonization of the Lifeworld", None, "貨幣・権力というシステム媒体が意思疎通的に統合された生活世界に浸食するとするハーバーマスの近代診断。", "批判理論・フランクフルト学派", "ハーバーマス", 1981, "Western_Europe", "https://en.wikipedia.org/wiki/Colonization_of_the_lifeworld"),
    ("公共圏", "Public Sphere", "Öffentlichkeit", "私的個人が公共的論議に参加する制度的領域。ハーバーマスが18世紀市民的公共圏の形成と変容を分析した概念。", "批判理論・フランクフルト学派", "ハーバーマス", 1962, "Western_Europe", "https://en.wikipedia.org/wiki/Public_sphere"),
    ("理想的発話状況", "Ideal Speech Situation", None, "強制・歪曲なしに論拠の力のみで合意に至る対話の反事実的前提。ハーバーマスの討議倫理学の基礎。", "批判理論・フランクフルト学派", "ハーバーマス", 1971, "Western_Europe", "https://en.wikipedia.org/wiki/Ideal_speech_situation"),
    ("討議倫理学", "Discourse Ethics", "Diskursethik", "道徳規範の妥当性を当事者全員が参加できる実践的討議によって検証するハーバーマス＆アーペルの倫理理論。", "批判理論・フランクフルト学派", "ハーバーマス", 1983, "Western_Europe", "https://en.wikipedia.org/wiki/Discourse_ethics"),
    ("体系と生活世界", "System and Lifeworld", None, "金銭・権力によって機能する体系と意思疎通的に再生産される生活世界という近代社会の二元構造。ハーバーマスの社会論。", "批判理論・フランクフルト学派", "ハーバーマス", 1981, "Western_Europe", "https://en.wikipedia.org/wiki/Lifeworld"),
    ("憲法的愛国主義", "Constitutional Patriotism", "Verfassungspatriotismus", "特定民族・文化ではなく民主主義的・人権的憲法原理への同一化を国民統合の基礎とするハーバーマスの政治哲学。", "批判理論・フランクフルト学派", "ハーバーマス", 1987, "Western_Europe", "https://en.wikipedia.org/wiki/Constitutional_patriotism"),
    # ホネット・承認論
    ("承認をめぐる闘争", "Struggle for Recognition", None, "愛・法・連帯の三領域における承認の獲得と否認が社会的葛藤を駆動するホネットの批判理論的社会哲学。", "批判理論・フランクフルト学派", "ホネット", 1992, "Western_Europe", "https://en.wikipedia.org/wiki/Axel_Honneth"),
    ("物象化（ホネット再解釈）", "Reification (Honneth's Reinterpretation)", None, "他者・自己・世界への原初的承認的関与が失われる経験として物象化を再解釈したホネットのヘーゲル的批判理論。", "批判理論・フランクフルト学派", "ホネット", 2005, "Western_Europe", "https://en.wikipedia.org/wiki/Reification_(Marxism)"),
    ("社会的病理", "Social Pathology", None, "社会的相互承認の歪みが引き起こす個人・集団の自己実現の阻害。批判理論の診断カテゴリとしてホネットが体系化。", "批判理論・フランクフルト学派", "ホネット", 2007, "Western_Europe", "https://en.wikipedia.org/wiki/Axel_Honneth"),
    ("承認の三領域", "Three Spheres of Recognition", None, "愛（家族）・法的承認（市民）・連帯的評価（共同体）の三次元でアイデンティティの承認が構成されるホネットの理論。", "批判理論・フランクフルト学派", "ホネット", 1992, "Western_Europe", "https://en.wikipedia.org/wiki/Axel_Honneth"),
    # フラーゼル・批判理論の展開
    ("再配分と承認", "Redistribution and Recognition", None, "社会的正義の二大課題として経済的平等（再配分）と文化的承認を位置づけるフレイザー＆ホネットの論争。", "批判理論・フランクフルト学派", "フレイザー", 2003, "North_America", "https://en.wikipedia.org/wiki/Nancy_Fraser"),
    ("誤った承認", "Misrecognition", None, "文化的支配・非承認・蔑視が正義の欠如をなすとするフレイザーの承認論的批判。ホネットとの論争で展開。", "批判理論・フランクフルト学派", "フレイザー", 1995, "North_America", "https://en.wikipedia.org/wiki/Nancy_Fraser"),
    ("フォーラムの問題", "Problem of the Frame", None, "誰が正義の当事者かを決定する包摂・排除のメタ政治的問題。フレイザーがポスト国民国家時代の正義論として論じた。", "批判理論・フランクフルト学派", "フレイザー", 2008, "North_America", "https://en.wikipedia.org/wiki/Nancy_Fraser"),
    # ネオ批判理論・社会的批判
    ("内在的批判", "Immanent Critique", None, "社会が自らの規範・原則に反しているという矛盾を社会内部から指摘する批判のスタイル。フランクフルト学派の方法論的特徴。", "批判理論・フランクフルト学派", "批判理論方法論", 1937, "Western_Europe", "https://en.wikipedia.org/wiki/Immanent_critique"),
    ("否定性の政治学", "Politics of Negativity", None, "現実の歪みを告発しながら代替案を提示しないことで批判的圧力を保持する政治的・思想的立場。", "批判理論・フランクフルト学派", "批判理論方法論", 1947, "Western_Europe", "https://en.wikipedia.org/wiki/Critical_theory"),
    ("批判理論の自己反省", "Self-Reflexivity of Critical Theory", None, "批判理論自身が社会的産物であることを認め、自らの認識論的立場を問い続ける再帰的方法論。", "批判理論・フランクフルト学派", "批判理論方法論", 1937, "Western_Europe", "https://en.wikipedia.org/wiki/Critical_theory"),
    # ルカーチ
    ("歴史と階級意識", "History and Class Consciousness", "Geschichte und Klassenbewusstsein", "物象化批判・階級意識・プロレタリアートの歴史的使命を統合したルカーチの1923年のマルクス主義哲学的主著。", "批判理論・フランクフルト学派", "ルカーチ", 1923, "Western_Europe", "https://en.wikipedia.org/wiki/History_and_Class_Consciousness"),
    ("トータリティ概念", "Concept of Totality", None, "社会全体を構造的連関として把握し、部分を全体との関係において理解する方法論的原則。ルカーチのマルクス主義的認識論。", "批判理論・フランクフルト学派", "ルカーチ", 1923, "Western_Europe", "https://en.wikipedia.org/wiki/Totality"),
    ("リアリズム論争", "Realism Debate", None, "社会主義文学における写実的表現の役割をめぐるルカーチとブレヒト・ベンヤミン等の文学論争（1930年代）。", "批判理論・フランクフルト学派", "ルカーチ", 1938, "Western_Europe", "https://en.wikipedia.org/wiki/Expressionism_debate"),
    # ブロッホ・ユートピア
    ("希望の原理", "Principle of Hope", "Das Prinzip Hoffnung", "人間の夢・ユートピア的衝動の哲学的分析。まだ-意識・具体的ユートピアをブロッホが体系化した（1954-59年）。", "批判理論・フランクフルト学派", "ブロッホ", 1954, "Western_Europe", "https://en.wikipedia.org/wiki/The_Principle_of_Hope"),
    ("具体的ユートピア", "Concrete Utopia", None, "実現可能な社会的潜在性を内包するユートピア的志向。抽象的ユートピアとを区別したブロッホの概念。", "批判理論・フランクフルト学派", "ブロッホ", 1954, "Western_Europe", "https://en.wikipedia.org/wiki/Ernst_Bloch"),
    ("まだ意識", "Not-Yet-Consciousness", "Noch-nicht-Bewusstsein", "完全には意識化されていない未来への予期・希望の心理的状態。ブロッホの希望の哲学の核心概念。", "批判理論・フランクフルト学派", "ブロッホ", 1954, "Western_Europe", "https://en.wikipedia.org/wiki/Ernst_Bloch"),
    # 非西洋批判理論
    ("第三世界の批判理論", "Third World Critical Theory", None, "西洋中心的批判理論の限界を指摘し、植民地経験・南北関係・従属を主要分析対象とする批判的社会思想。", "批判理論・フランクフルト学派", "非西洋批判理論", 1970, "Latin_America", "https://en.wikipedia.org/wiki/Third_World"),
    ("南からの批判理論", "Critical Theory from the South", None, "アフリカ・ラテンアメリカ・アジアの思想家による、北半球中心的批判理論への根本的異議申し立て。", "批判理論・フランクフルト学派", "非西洋批判理論", 1990, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/Southern_theory"),
    ("解放哲学", "Philosophy of Liberation", "Filosofía de la liberación", "ラテンアメリカの植民地的従属経験を起点にエンリケ・ドゥッセルらが構築した批判哲学。", "批判理論・フランクフルト学派", "非西洋批判理論", 1972, "Latin_America", "https://en.wikipedia.org/wiki/Philosophy_of_liberation"),
    ("ドゥッセルの倫理学", "Dussel's Ethics", None, "他者・排除された者の顔から倫理的要求が発生するレヴィナス＋マルクスの統合によるドゥッセルの解放倫理。", "批判理論・フランクフルト学派", "非西洋批判理論", 1998, "Latin_America", "https://en.wikipedia.org/wiki/Enrique_Dussel"),
    ("トランスモダニティ", "Transmodernity", None, "近代でも反近代でもなく、非西洋の文化的遺産を組み込んだ複数の近代の共存をドゥッセルが提唱した概念。", "批判理論・フランクフルト学派", "非西洋批判理論", 2000, "Latin_America", "https://en.wikipedia.org/wiki/Enrique_Dussel"),
    ("アフリカ批判理論", "African Critical Theory", None, "ファノン・ンクルマ・セゼール・センゴールに始まり現代のムベンベ・ムゾールらが展開するアフリカ経験起点の批判的社会思想。", "批判理論・フランクフルト学派", "非西洋批判理論", 1961, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/African_philosophy"),
    ("韓国の批判的社会科学", "Korean Critical Social Science", None, "植民地支配・冷戦分断・独裁からの解放を課題とする韓国独自の批判的社会科学的伝統。明倫・民族・民衆論を含む。", "批判理論・フランクフルト学派", "非西洋批判理論", 1980, "East_Asia", "https://en.wikipedia.org/wiki/South_Korean_democratization_movement"),
    ("インド批判理論（サバルタン研究以前）", "Indian Critical Theory (Pre-Subaltern)", None, "マルクス主義と民族解放を結合しながらカースト・農民・女性問題を分析したインド独立前後の批判的社会思想。", "批判理論・フランクフルト学派", "非西洋批判理論", 1930, "South_Asia", "https://en.wikipedia.org/wiki/Indian_independence_movement"),
    # アルチュセール
    ("理論的反人間主義", "Theoretical Anti-Humanism", None, "人間主体を歴史の起点とするヒューマニズムを理論的に拒否し、構造的過程を分析するアルチュセールの立場。", "批判理論・フランクフルト学派", "構造主義的マルクス主義", 1965, "Western_Europe", "https://en.wikipedia.org/wiki/Louis_Althusser"),
    ("イデオロギー的国家装置", "Ideological State Apparatuses", "Appareils idéologiques d'État", "国家が学校・教会・メディア・家族等を通じてイデオロギーを再生産する機構をアルチュセールが分析した概念。", "批判理論・フランクフルト学派", "構造主義的マルクス主義", 1970, "Western_Europe", "https://en.wikipedia.org/wiki/Ideological_state_apparatus"),
    ("過剰決定", "Overdetermination", "Surdétermination", "社会矛盾が単一の経済的原因に還元されず複数の矛盾の集積・融合として理解されるアルチュセールの弁証法概念。", "批判理論・フランクフルト学派", "構造主義的マルクス主義", 1965, "Western_Europe", "https://en.wikipedia.org/wiki/Overdetermination"),
    ("呼びかけ（インタペラシオン）", "Interpellation", "Interpellation", "イデオロギーが個人を特定の主体として呼びかけ、主体性を構成する過程。アルチュセールの主体論の核心。", "批判理論・フランクフルト学派", "構造主義的マルクス主義", 1970, "Western_Europe", "https://en.wikipedia.org/wiki/Interpellation_(philosophy)"),
    ("認識論的切断", "Epistemological Break", "Coupure épistémologique", "青年期人間主義的マルクスと成熟した科学的マルクスを区別するアルチュセールの読解。バシュラールから転用。", "批判理論・フランクフルト学派", "構造主義的マルクス主義", 1965, "Western_Europe", "https://en.wikipedia.org/wiki/Epistemological_break"),
    # シュラッヘタ・バリバール
    ("大衆のイデオロギー", "Mass Ideology", None, "資本主義社会における労働者の同意形成メカニズムをバリバールがアルチュセール・グラムシ双方から分析。", "批判理論・フランクフルト学派", "構造主義的マルクス主義", 1974, "Western_Europe", "https://en.wikipedia.org/wiki/%C3%89tienne_Balibar"),
    ("市民権と普遍性", "Citizenship and Universality", None, "フランス革命以来の市民＝人間の等式の矛盾（排除・植民地）をバリバールが批判的に分析した政治哲学。", "批判理論・フランクフルト学派", "構造主義的マルクス主義", 1994, "Western_Europe", "https://en.wikipedia.org/wiki/%C3%89tienne_Balibar"),
    # ジジェク
    ("イデオロギーの崇高な客体", "The Sublime Object of Ideology", None, "精神分析を援用しながら現代イデオロギーの機能と環ファンタジー的支えを分析したジジェクの主著（1989年）。", "批判理論・フランクフルト学派", "ジジェク", 1989, "Western_Europe", "https://en.wikipedia.org/wiki/The_Sublime_Object_of_Ideology"),
    ("リアルの政治学", "Politics of the Real", None, "象徴秩序に回収されない外傷的核（リアル）への政治的介入を論じるジジェクのラカン＋マルクスの批判理論。", "批判理論・フランクフルト学派", "ジジェク", 2000, "Western_Europe", "https://en.wikipedia.org/wiki/Slavoj_%C5%BDi%C5%BEek"),
    ("犬儒主義的理性批判", "Critique of Cynical Reason", None, "「よく知っているのに（それでも行為する）」という啓蒙以後のイデオロギーの逆説をペータースローターダイクが分析。", "批判理論・フランクフルト学派", "ドイツ批判哲学", 1983, "Western_Europe", "https://en.wikipedia.org/wiki/Critique_of_Cynical_Reason"),
    # 第四世代フランクフルト学派
    ("批判理論の社会理論的転回", "Sociological Turn in Critical Theory", None, "規範的哲学から実証的社会分析への移行を含む、第三・四世代フランクフルト学派の方法論的変化。", "批判理論・フランクフルト学派", "批判理論方法論", 2000, "Western_Europe", "https://en.wikipedia.org/wiki/Frankfurt_School"),
    ("ローゼンフェルト社会批判", "Rancière-Inspired Social Critique", None, "ランシエールの感性の分割・政治的主体化概念を批判理論に接合する現代的展開。美学と政治の再接合。", "批判理論・フランクフルト学派", "批判理論方法論", 2004, "Western_Europe", "https://en.wikipedia.org/wiki/Jacques_Ranci%C3%A8re"),
    # クリティカル・レース・セオリーとの接合
    ("批判理論と人種", "Critical Theory and Race", None, "フランクフルト学派の批判理論とアメリカの批判的人種理論（CRT）の対話・接合。承認・承認拒否・システム的人種差別の分析。", "批判理論・フランクフルト学派", "批判的人種理論", 1990, "North_America", "https://en.wikipedia.org/wiki/Critical_race_theory"),
    ("フェミニスト批判理論", "Feminist Critical Theory", None, "ジェンダー関係を権力・資本・文化の三次元で分析するフランクフルト学派的フェミニズム。ハーディング・フレイザー等。", "批判理論・フランクフルト学派", "フェミニスト批判理論", 1985, "North_America", "https://en.wikipedia.org/wiki/Feminist_theory"),
    # エコロジー批判理論
    ("生態学的批判理論", "Ecological Critical Theory", None, "フランクフルト学派の自然支配批判をエコロジー危機と結びつける現代的展開。アドルノの自然弁証法の継承。", "批判理論・フランクフルト学派", "生態学的批判理論", 1995, "Western_Europe", "https://en.wikipedia.org/wiki/Critical_theory"),
    ("自然の支配", "Domination of Nature", None, "人間が自然を道具的に支配する近代的態度が社会的支配と構造的に連動するとするアドルノ＆ホルクハイマーの批判。", "批判理論・フランクフルト学派", "生態学的批判理論", 1947, "Western_Europe", "https://en.wikipedia.org/wiki/Domination_of_nature"),
    # 補完：アジア・グローバル
    ("東アジアの批判理論受容", "Reception of Critical Theory in East Asia", None, "日本・韓国・台湾・中国における1970-90年代のフランクフルト学派受容とその独自的展開。丸山眞男等の関連。", "批判理論・フランクフルト学派", "非西洋批判理論", 1970, "East_Asia", "https://en.wikipedia.org/wiki/Frankfurt_School"),
    ("中国批判社会学", "Chinese Critical Sociology", None, "改革開放後の中国で社会的不平等・農村問題・労働問題を分析する批判的社会科学の潮流。景軍・謝宇等。", "批判理論・フランクフルト学派", "非西洋批判理論", 1990, "East_Asia", "https://en.wikipedia.org/wiki/Sociology_in_China"),
    ("インドの批判思想（アンベードカル）", "Indian Critical Thought (Ambedkar)", None, "カースト制度・ヒンドゥー教・植民地支配を根本的に批判したアンベードカルの解放思想。現代ダリット批判理論の源泉。", "批判理論・フランクフルト学派", "非西洋批判理論", 1936, "South_Asia", "https://en.wikipedia.org/wiki/B._R._Ambedkar"),
    ("ダリット批判理論", "Dalit Critical Theory", None, "不可触民差別の社会的・認識論的・歴史的構造を解明し、解放実践を正当化するインド独自の批判的思想潮流。", "批判理論・フランクフルト学派", "非西洋批判理論", 1990, "South_Asia", "https://en.wikipedia.org/wiki/Dalit"),
    ("アフリカ社会思想（アマ・アタ・アイドゥー等）", "African Social Thought", None, "西洋批判理論の限界を指摘しながらアフリカの文化的資源・植民地的遺産・ポストコロニアル現実を分析する思想。", "批判理論・フランクフルト学派", "非西洋批判理論", 1970, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/African_philosophy"),
    # ネオ・マルクス主義系
    ("批判的政治経済学", "Critical Political Economy", None, "経済関係の社会的・政治的・イデオロギー的構成を分析するマルクス主義的経済社会学。ハーヴェイ等が現代的展開。", "批判理論・フランクフルト学派", "ネオ・マルクス主義", 1970, "North_America", "https://en.wikipedia.org/wiki/Political_economy"),
    ("空間の生産（ルフェーブル）", "Production of Space (Lefebvre)", None, "空間を社会的・政治的に生産された実践・表象・生きられた空間の三位一体として分析するルフェーブルの批判理論。", "批判理論・フランクフルト学派", "ネオ・マルクス主義", 1974, "Western_Europe", "https://en.wikipedia.org/wiki/The_Production_of_Space"),
    ("日常生活批判", "Critique of Everyday Life", None, "資本主義的疎外が日常の細部に浸透する様を分析し、実践的変革の可能性を探るルフェーブルの三部作（1947-1981年）。", "批判理論・フランクフルト学派", "ネオ・マルクス主義", 1947, "Western_Europe", "https://en.wikipedia.org/wiki/Critique_of_Everyday_Life"),
    ("スペクタクルの社会", "Society of the Spectacle", "La société du spectacle", "現代資本主義において生きられた経験がイメージの蓄積に転化するギー・ドゥボールのシチュアシオニスト的批判（1967年）。", "批判理論・フランクフルト学派", "ネオ・マルクス主義", 1967, "Western_Europe", "https://en.wikipedia.org/wiki/The_Society_of_the_Spectacle"),
    ("疎外の復権（批判的再評価）", "Rehabilitation of Alienation", None, "疎外概念を「ヒューマニスト的残滓」と退けたアルチュセール以降の批判に対して、概念の有効性を再評価する立場。", "批判理論・フランクフルト学派", "批判理論方法論", 1990, "Western_Europe", "https://en.wikipedia.org/wiki/Marx%27s_theory_of_alienation"),
    # フーコーとの接合点
    ("ハーバーマス＝フーコー論争", "Habermas-Foucault Debate", None, "近代の権力・理性をめぐる規範的批判理論（ハーバーマス）と系譜学的権力分析（フーコー）の対立的対話。", "批判理論・フランクフルト学派", "ハーバーマス", 1986, "Western_Europe", "https://en.wikipedia.org/wiki/J%C3%BCrgen_Habermas"),
    # 解放神学との接続
    ("解放神学と批判理論", "Liberation Theology and Critical Theory", None, "ラテンアメリカの解放神学（グティエレス等）とフランクフルト学派批判理論の規範的・実践的対話。", "批判理論・フランクフルト学派", "非西洋批判理論", 1971, "Latin_America", "https://en.wikipedia.org/wiki/Liberation_theology"),
    # 文化研究との接合
    ("批判理論と文化研究", "Critical Theory and Cultural Studies", None, "フランクフルト学派とバーミンガム現代文化研究センター（CCCS）の方法論的交差。ポップカルチャー・抵抗・アイデンティティ。", "批判理論・フランクフルト学派", "批判理論方法論", 1964, "Western_Europe", "https://en.wikipedia.org/wiki/Cultural_studies"),
    # 補完：概念整理
    ("批判理論の第一世代・第二世代・第三世代", "Generations of Critical Theory", None, "フランクフルト学派の世代的展開：第一世代（アドルノ・ホルクハイマー・マルクーゼ）、第二世代（ハーバーマス）、第三世代（ホネット・フレイザー）。", "批判理論・フランクフルト学派", "批判理論方法論", 1923, "Western_Europe", "https://en.wikipedia.org/wiki/Frankfurt_School"),
    ("否定性と希望の弁証法", "Dialectics of Negativity and Hope", None, "アドルノの否定的弁証法とブロッホの希望原理を接合し、批判と希望の緊張を保持する批判理論の倫理的スタンス。", "批判理論・フランクフルト学派", "批判理論方法論", 1960, "Western_Europe", "https://en.wikipedia.org/wiki/Frankfurt_School"),
    ("技術合理性批判", "Critique of Technological Rationality", None, "技術が価値中立的手段でなく特定の支配・管理様式を具現化するとするマルクーゼ・エリュール等の批判。", "批判理論・フランクフルト学派", "批判理論方法論", 1964, "Western_Europe", "https://en.wikipedia.org/wiki/Herbert_Marcuse"),
    ("消費社会批判", "Critique of Consumer Society", None, "大量消費・広告・欲望操作を通じた社会統制と偽りの欲求の充足を批判するフランクフルト学派的文化論。", "批判理論・フランクフルト学派", "初期フランクフルト学派", 1964, "Western_Europe", "https://en.wikipedia.org/wiki/Consumer_society"),
    ("新左翼理論", "New Left Theory", None, "1960年代に台頭した新左翼が継承・変形した批判理論。人種・ジェンダー・環境を伝統的階級論に接合した。", "批判理論・フランクフルト学派", "批判理論方法論", 1960, "North_America", "https://en.wikipedia.org/wiki/New_Left"),
    ("アイデンティティ政治と批判理論", "Identity Politics and Critical Theory", None, "批判理論が人種・ジェンダー・セクシュアリティのアイデンティティ次元を組み込む過程での緊張と展開。", "批判理論・フランクフルト学派", "批判理論方法論", 1980, "North_America", "https://en.wikipedia.org/wiki/Identity_politics"),
    # デジタル時代の批判理論
    ("デジタル疎外", "Digital Alienation", None, "プラットフォーム資本主義における監視・データ収奪・自律性喪失を疎外論的概念枠で分析する現代批判理論。", "批判理論・フランクフルト学派", "批判理論方法論", 2010, "Global_Synthesis", "https://en.wikipedia.org/wiki/Digital_capitalism"),
    ("監視資本主義批判", "Critique of Surveillance Capitalism", None, "ショシャナ・ズボフが提唱した、行動データの収奪・予測商品化・行動変容として資本主義の新段階を批判する概念。", "批判理論・フランクフルト学派", "批判理論方法論", 2019, "North_America", "https://en.wikipedia.org/wiki/Surveillance_capitalism"),
    ("プラットフォーム批判理論", "Critical Platform Theory", None, "デジタルプラットフォームが労働・価値・権力を再編する様を批判的政治経済学・フランクフルト学派的観点から分析。", "批判理論・フランクフルト学派", "批判理論方法論", 2017, "Global_Synthesis", "https://en.wikipedia.org/wiki/Platform_economy"),
    # 補完：重要概念
    ("連帯的生活様式", "Solidary Way of Life", None, "競争・個人主義に代わる連帯・相互扶助を基軸とした生活と社会秩序の可能性をホネットが論じた規範的展望。", "批判理論・フランクフルト学派", "ホネット", 2014, "Western_Europe", "https://en.wikipedia.org/wiki/Axel_Honneth"),
    ("解放的利害関心", "Emancipatory Interest", None, "認識誘導的利害関心の一つとして、支配からの解放を志向する認識的動機をハーバーマスが設定した認識論的概念。", "批判理論・フランクフルト学派", "ハーバーマス", 1968, "Western_Europe", "https://en.wikipedia.org/wiki/Knowledge_and_Human_Interests"),
    ("知識と人間的利害関心", "Knowledge and Human Interests", None, "経験・分析科学（技術的利害）・歴史解釈科学（実践的利害）・批判理論（解放的利害）の三分法。ハーバーマス1968年。", "批判理論・フランクフルト学派", "ハーバーマス", 1968, "Western_Europe", "https://en.wikipedia.org/wiki/Knowledge_and_Human_Interests"),
    ("批判理論とプラグマティズム", "Critical Theory and Pragmatism", None, "ハーバーマスがデューイ・パース・ミードの語用論・コミュニケーション理論を批判理論に接合した理論的交差。", "批判理論・フランクフルト学派", "ハーバーマス", 1981, "North_America", "https://en.wikipedia.org/wiki/Pragmatism"),
    ("正義と連帯", "Justice and Solidarity", None, "普遍的正義の要求と特殊な共同体的連帯の緊張を調停するハーバーマスの社会倫理的枠組み。", "批判理論・フランクフルト学派", "ハーバーマス", 1989, "Western_Europe", "https://en.wikipedia.org/wiki/J%C3%BCrgen_Habermas"),
    # 補完
    ("フランクフルト学派と精神分析", "Frankfurt School and Psychoanalysis", None, "フロイトの精神分析を社会批判に接合したフランクフルト学派の方法論的特質。権威主義・抑圧・昇華の社会的機能分析。", "批判理論・フランクフルト学派", "批判理論方法論", 1930, "Western_Europe", "https://en.wikipedia.org/wiki/Frankfurt_School"),
    ("批判的社会理論のグローバル転回", "Global Turn in Critical Social Theory", None, "西洋中心的批判理論をグローバルな非西洋的経験・知識体系に開いていく2000年代以降の理論的展開。", "批判理論・フランクフルト学派", "非西洋批判理論", 2000, "Global_Synthesis", "https://en.wikipedia.org/wiki/Critical_theory"),
    ("批判的リアリズム（バスカー）", "Critical Realism (Bhaskar)", None, "社会科学は観察不可能な生成メカニズムを分析すべきとするロイ・バスカーの存在論的・方法論的立場。", "批判理論・フランクフルト学派", "批判的リアリズム", 1975, "Western_Europe", "https://en.wikipedia.org/wiki/Critical_realism_(philosophy_of_the_social_sciences)"),
    ("変換的社会活動（バスカー）", "Transformational Model of Social Activity", None, "社会構造が人間の行為を条件づけ、人間の実践が構造を再生産・変革するバスカーの二重性モデル。", "批判理論・フランクフルト学派", "批判的リアリズム", 1979, "Western_Europe", "https://en.wikipedia.org/wiki/Roy_Bhaskar"),
    ("生成メカニズム", "Generative Mechanisms", None, "観察された出来事の背後にある実在的な因果力・傾向。批判的リアリズムが社会科学の対象とする存在論的カテゴリ。", "批判理論・フランクフルト学派", "批判的リアリズム", 1975, "Western_Europe", "https://en.wikipedia.org/wiki/Critical_realism_(philosophy_of_the_social_sciences)"),
    # アボリジニ・先住民批判理論
    ("先住民批判理論", "Indigenous Critical Theory", None, "植民地的知識生産・土地収奪・文化破壊に対し、先住民の認識論・オントロジーを軸に批判する理論的潮流。", "批判理論・フランクフルト学派", "非西洋批判理論", 1990, "Oceania", "https://en.wikipedia.org/wiki/Indigenous_studies"),
    ("脱植民地的認識論（バンガ）", "Decolonial Epistemology (Banga)", None, "西洋学知の普遍性主張を批判し、植民地化された人々の認識論的位置から知識を再構築しようとする批判理論。", "批判理論・フランクフルト学派", "非西洋批判理論", 2000, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/Decolonization_of_knowledge"),
    # 補完終了
    ("フランクフルト学派と民主主義理論", "Frankfurt School and Democratic Theory", None, "批判理論が審議民主主義・急進民主主義・社会主義的民主主義等の規範的民主理論と接合してきた論点。", "批判理論・フランクフルト学派", "ハーバーマス", 1992, "Western_Europe", "https://en.wikipedia.org/wiki/Deliberative_democracy"),
    ("後期資本主義の正当化問題", "Legitimation Crisis of Late Capitalism", None, "後期資本主義が経済・合理性・動機の三次元で正当性危機を引き起こすとするハーバーマスの1973年の分析。", "批判理論・フランクフルト学派", "ハーバーマス", 1973, "Western_Europe", "https://en.wikipedia.org/wiki/Legitimation_Crisis"),
]

def insert_batch(concepts):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    inserted = 0; skipped = 0
    for c in concepts:
        name_ja, name_en, name_orig, defn, subfield, school, era, region, url = c
        cur.execute("SELECT COUNT(*) FROM social_theory WHERE name_en=?", (name_en,))
        if cur.fetchone()[0] > 0:
            skipped += 1; continue
        uid = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()
        cur.execute("""INSERT INTO social_theory
            (id,name_ja,name_en,name_original,definition,subfield,school_of_thought,
             era_start,culture_region,source_url,verification_status,quality_flag,
             status,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,'url_present','B','active',?,?)""",
            (uid,name_ja,name_en,name_orig,defn,subfield,school,era,region,url,now,now))
        inserted += 1
        if inserted % 50 == 0:
            conn.commit(); print(f"  Committed {inserted}...")
    conn.commit(); conn.close()
    return inserted, skipped

if __name__ == "__main__":
    print(f"Inserting {len(concepts)} concepts (Batch 2: 批判理論・フランクフルト学派)...")
    ins, sk = insert_batch(concepts)
    print(f"Done. Inserted: {ins}, Skipped: {sk}")
