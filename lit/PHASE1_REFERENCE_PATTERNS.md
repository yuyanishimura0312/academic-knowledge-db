# LIT-DB Phase 1: 5参照パターン 詳細手順書

**作成日**: 2026-05-07
**作成者**: academic-db-survey（Phase 1 担当）
**対象**: Phase 0 で定義された5つの収集参照パターン
**目的**: Codex 20名が一致した手順で `concepts/authors/works/movements` テーブルを埋め、`relations/geneal_links/cross_domain/fourth_transform_tags` を整合的に記述する

---

## 0. 本書の位置づけ

LIT-DB の Phase 2 における収集はサブフィールドごとに独立して進めるが、収集の論理は5つの参照パターンに収斂する。各パターンには起点となる入力情報と、それを概念・作家・作品・運動という4軸へ展開する標準手順がある。本書は各パターンについて、入力・利用ツール・データ抽出フィールド・関係性記述ルール・ハルシネーション検証手順・収集ペース目安を定義する。

5パターンは以下である。

1. **Canonical Primary Pursuit**（正典型一次資料追跡）— 古典領域
2. **Movement-Driven Aggregation**（文学運動・流派起点）— 近代以降の主義系領域
3. **Theorist-Genealogy Pattern**（理論家・批評家系譜）— 理論・批評領域
4. **Regional Cluster Expansion**（地域・言語クラスター展開）— グローバル・サウス・先住民領域
5. **Fourth-Transformation Cross-Cut**（第四変容軸クロスカット）— 全領域横断

---

## 1. Canonical Primary Pursuit（正典型一次資料追跡）

### 1.1 適用領域
古典古代文学（lit_eu_classical）、中国古典文学（lit_cn_classical）、日本古典文学（lit_jp_classical）、インド古典（lit_india の前半）、アラブ古典（lit_arabic の前半）、ペルシア古典（lit_persian_turkish の前半）、中世文学（lit_eu_medieval）。

### 1.2 入力（収集の起点）
正典作品リストから出発する。具体的には、(a) 各領域の標準的学術通史で言及される代表作、(b) 各領域の批判校訂版叢書（Loeb / Murty / 新編日本古典文学全集 / 中華書局点校本）に収録される作品群、の合致を起点リストとする。Codex 担当者は Phase 2 開始時に各サブフィールドで30-50件の起点作品リストを作成し、C20（横断検証）の承認を得る。

### 1.3 利用ツール・DB・検索戦略
古典古代は Perseus Digital Library（perseus.tufts.edu）と TLG（要機関契約）を併用、英訳補完に Loeb と Project Gutenberg。中国古典は CTEXT（ctext.org）の API、維基文庫、Scripta Sinica（漢籍電子文獻資料庫）、Kanripo（GitHub `kanripo/KR1`〜`KR6`）。日本古典は国文学研究資料館 新日本古典籍総合データベース、NDLデジタルコレクション、青空文庫、ジャパンナレッジ。インドは GRETIL、SARIT、Sanskrit Heritage Site、Murty Classical Library。アラブは Al-Maktaba al-Shamela、OpenITI（GitHub `OpenITI/RELEASE`）。検索戦略は (1) 作品タイトル検索 → 原典本文取得、(2) 作品本文中の概念語の文脈付き抽出、(3) 注釈・序跋からの理論用語抽出、の3段階。

### 1.4 データ抽出フィールド

`works` テーブルへの投入項目: title_ja, title_en, title_original, original_script（greek/latin/sanskrit/arabic/kanji/hiragana等）, author_id（または author_name_text）, publication_year（推定可、負数=BCE）, period_id, region, genre, language, summary, significance, influence_summary, primary_source_url（一次資料の直接URL）, importance_score（4-5を正典作品に付与）, source_tier='primary', canonical_in_region='core'。

`authors` テーブルへの投入項目: name_ja, name_en, name_original, birth_year, death_year, region, nationality, primary_language, period_id, biography, contributions, importance_score（4-5）, primary_source_url, source_tier='primary', canonical_in_region。

`concepts` テーブルへの投入項目: 作品本文・序跋・注釈に登場する文学的概念（mimesis、karuna、mono no aware、mu'arada等）について、name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition, background（成立文脈）, development（後代展開）, primary_source_url, primary_source_type='classical_text'/'commentary', importance_score, source_tier='primary'。

`movements` テーブルへの投入項目: 該当領域に運動概念がある場合（例: 古典古代の悲劇詩人グループ、中国の建安文学、日本の和歌結社）、name_ja, name_en, region, start_year, end_year, description, key_principles, primary_source_url。

### 1.5 関係性記述ルール

**relations**: 作品-概念間（'contains'/'exemplifies'）、作家-作品間（'authored_by'）、作家-作家間（'influences'/'criticizes'）。bidirectional は影響関係でtrue（双方向）の場合のみ1。confidence は一次資料に明記される場合5、注釈経由4、二次文献経由3。

**geneal_links**: 概念-概念間で系譜が辿れる場合（例: ギリシャ mimesis → ラテン imitatio → ルネサンス imitatio veterum → ロマン主義 mimesis批判）。transformation_type は extension/inversion/critique/translation/syncretism のいずれか。transmission_path には文化圏間の伝播経路（例: 「ギリシャ→ラテン→中世スコラ→ルネサンス・イタリア」）を記述。

**cross_domain**: 哲学概念と重なる場合（例: 古典古代の poiesis → PHIL の創造行為論）、Poetics DB と重なる場合（例: 古典古代の muthos → PT の plot）に target_db を 'PHIL' / 'PT' として登録。link_type は shared_concept/borrowed_from/parallel。

### 1.6 ハルシネーション検証手順

正典領域は最も検証が容易である。手順: (1) 概念・作品・作家の名前を必ず一次資料の URL とともに記録、(2) 引用文（key quotes）を最低1つ概念ごとに保存、(3) 成立年・著者名は批判校訂版（Loeb・Murty・新編日本古典文学全集）の序文記述と合致するか確認、(4) C20が概念名で逆検索を行い、一次資料に存在するか抜き打ち検証。`source_tier` は原則 'primary' とし、批判校訂版経由なら 'secondary'。

### 1.7 1日あたり収集ペース目安

1名の Codex が1日に処理できる規模: concepts 15-25件、authors 5-8件、works 8-12件、relations 30-50件。これは古典領域では概念抽出に時間を要する（一次資料の注釈確認が必要）ためで、近代領域より低い水準となる。

---

## 2. Movement-Driven Aggregation（文学運動・流派起点）

### 2.1 適用領域
ルネサンス・近世文学、啓蒙・ロマン主義、リアリズム・自然主義・象徴主義、モダニズム、ポストモダン・現代、中国近現代文学、日本近現代文学、ラテンアメリカ文学（特にブーム期）、ロシア・スラヴ文学、児童・大衆・ジャンル文学。

### 2.2 入力（収集の起点）
文学運動・流派・主義の名称リストから出発する。各サブフィールドあたり15-30件程度の運動を起点とする（例: ルネサンス領域なら「人文主義」「フィレンツェ・プラトン主義」「マニエリスム」「バロック」「古典主義」等）。各運動について、それを定義した宣言・批評論考・代表作家・代表作の四点を最初に確定する。

### 2.3 利用ツール・DB・検索戦略
Cambridge Companions / Oxford Handbooks の各運動巻、Routledge Critical Concepts in Literary and Cultural Studies、JSTOR、Project MUSE、MLA International Bibliography が二次文献の主要源。原典は Modernist Journals Project（modjourn.org）、Modernist Versions Project、Project Gutenberg、HathiTrust、Gallica、青空文庫、CNKI、Biblioteca Virtual Miguel de Cervantes など各領域の一次資料アーカイブ。検索戦略は (1) 運動名で総説論文を取得 → 主要メンバー・代表作リスト確定、(2) 各メンバーの主要作品から概念を抽出、(3) 運動の宣言文（Manifeste du Surréalisme 等）を一次資料として直接参照。

### 2.4 データ抽出フィールド

`movements` テーブルが起点となる: name_ja, name_en, name_original, region, start_year, end_year, description（300-500字）, key_principles（運動の中心原理）, historical_context, legacy（後代への影響）, primary_source_url（宣言文・主要論考の URL）。

`authors` への投入: 運動の主要メンバー（典型的に5-15名）。movements_belonged にカンマ区切りで運動名を記録。importance_score は中心メンバー4-5、周辺メンバー3。

`works` への投入: 運動を代表する作品（典型的に10-30作品）。significance フィールドに「運動内での位置づけ」を記述。

`concepts` への投入: 運動が打ち出した新概念（例: Naturalisme の「実験小説」、Symbolisme の「対応 correspondance」、Surrealism の「自動筆記 écriture automatique」）。definition には運動内での意味、development には後代への展開を記述。

### 2.5 関係性記述ルール

**relations**: 運動-作家間（'belongs_to'）、運動-作品間（'represented_by'）、運動-運動間（'precedes'/'reacts_against'）、運動-概念間（'introduced_by'）。

**geneal_links**: 運動-運動間の系譜（例: Romanticism → Symbolism → Surrealism）。transformation_type は inversion または critique が多い。

**cross_domain**: 運動が哲学・社会理論と密接な場合（例: Existentialism literature → PHIL Existentialism）、PHIL の運動・学派と接続。Movement → Movement Cross-Region 接続（例: 仏 Symbolisme → 露 Symbolism、墨 Modernismo → 西 Modernismo）も Phase 4 で重点化。

### 2.6 ハルシネーション検証手順

運動領域は二次文献に依存しやすいため検証が重要。手順: (1) 運動の宣言文・代表テクストの一次資料 URL を必ず記録、(2) 運動メンバーの所属は最低2つの独立した二次文献（学術通史）で合致確認、(3) 運動概念の出典は宣言文または運動内主要論考に限定、(4) C20 が運動内メンバー間の関係性に矛盾がないか週次で確認。`source_tier` は宣言文経由 'primary'、批判校訂版経由 'secondary'、二次文献経由 'tertiary'。

### 2.7 1日あたり収集ペース目安

1名の Codex が1日に処理できる規模: concepts 25-40件、authors 8-12件、works 12-20件、movements 1-2件、relations 50-80件。運動概念は集中的に収集できるため古典領域より高ペース。

---

## 3. Theorist-Genealogy Pattern（理論家・批評家系譜）

### 3.1 適用領域
文学理論・批評（lit_theory）、比較文学・世界文学・翻訳論（lit_world_translation）、デジタル人文学・AI時代の文学（lit_digital_ai）。一部のモダニズム・ポストモダンの理論家（バルト、デリダ等）にも適用。

### 3.2 入力（収集の起点）
主要理論家の系譜リストから出発する。例えば「ロシア・フォルマリズム → プラハ言語学派 → 構造主義 → ポスト構造主義 → 脱構築」のような系譜を10-15本程度設定し、各系譜上の中心人物（5-10名）を起点とする。

### 3.3 利用ツール・DB・検索戦略
Stanford Encyclopedia of Philosophy（plato.stanford.edu）は理論家伝記・概念解説の信頼源で哲学DBと共有。PhilPapers（philpapers.org）は理論論文書誌コーパス。Cambridge Companions Online（要機関契約）、Norton Anthology of Theory and Criticism（標準教科書、書誌情報入手）、Critical Inquiry / New Literary History / Diacritics 各誌のオンラインアーカイブ。検索戦略は (1) 理論家名で SEP / PhilPapers エントリ取得、(2) 主要著作リストと中心概念を抽出、(3) 影響関係（誰を読み、誰に読まれたか）を批判校訂版または学術伝記から確定、(4) 主要著作の原典本文（PD化されているものは Project Gutenberg / Internet Archive）から概念引用を取得。

### 3.4 データ抽出フィールド

`authors` テーブルに理論家として投入: 通常の文学作家と異なり contributions に「理論家としての主要貢献」を記述（例: バフチン → 異言語混淆 heteroglossia、対話的想像力、カーニヴァル）。movements_belonged には学派名（ロシア・フォルマリズム、フランクフルト学派等）。

`concepts` への投入: 理論家が導入した概念（例: heteroglossia, dialogism, defamiliarization, iterability, différance, stratification）。definition には理論家自身の定義（一次資料からの引用）、background には導入の理論的文脈、development には後代理論家による展開・批判を記述。importance_score は理論的影響力に応じて3-5。

`works` への投入: 理論的著作（例: バフチン『ドストエフスキーの詩学』、デリダ『グラマトロジーについて』）。works.genre は 'theory' / 'criticism' とする。

`movements` への投入: 学派・理論潮流（例: New Criticism、Frankfurt School、Yale School of Deconstruction）。

### 3.5 関係性記述ルール

**relations**: 理論家-理論家間（'influences'/'criticizes'/'extends'）が中心、bidirectionalは原則false（A→Bは多くの場合一方向）。confidence は一次資料の引用関係から5、二次文献経由3。

**geneal_links** が本パターンの中核: 概念の系譜を追跡する。例えば「シクロフスキー異化 → バフチン対話 → クリステヴァ間テクスト性 → ジュネット間テクスト性」のような4世代以上の系譜を多数構築。transformation_type は extension が多いが、inversion（前世代の批判）や critique も含む。

**cross_domain** の重点的活用: 文学理論は哲学・記号学・人類学と境界が曖昧なため、PHIL/AN/PT への cross_domain 登録を頻繁に行う。link_type は shared_concept が多いが、PHIL から借用された場合 borrowed_from。

### 3.6 ハルシネーション検証手順

理論領域は概念定義の一次資料との合致が最重要。手順: (1) 各概念について、理論家本人の著作からの引用を1つ以上記録、(2) 影響関係の主張（A→B）について、A・B双方の著作の相互参照箇所を確認、(3) 翻訳経由で知られる概念は原語表記を必須記録（例: différance はフランス語、Verfremdung はドイツ語）、(4) SEP / PhilPapers のエントリと不整合がある場合は再検証。`source_tier` は理論家著作直接 'primary'、批判校訂版 'secondary'、二次文献経由 'tertiary'。

### 3.7 1日あたり収集ペース目安

1名の Codex が1日に処理できる規模: concepts 20-30件（理論概念は定義精度が必要なため低め）、authors 5-8件、works 10-15件、relations 60-100件、geneal_links 15-25件。本パターンは relations / geneal_links の密度が他パターンの2倍程度になる。

---

## 4. Regional Cluster Expansion（地域・言語クラスター展開）

### 4.1 適用領域
アフリカ文学（lit_africa）、ラテンアメリカ文学（lit_latin_america の一部）、東南アジア・韓国文学（lit_se_asia_korea）、ディアスポラ・移民文学（lit_diaspora）、先住民・口承文学（lit_indigenous_oral）。

### 4.2 入力（収集の起点）
言語または地域クラスターを起点とする。例えばアフリカ文学なら (a) 言語別（スワヒリ語、ヨルバ語、ハウサ語、英語アフリカ文学、仏語アフリカ文学、葡語アフリカ文学）、(b) 地域別（東アフリカ、西アフリカ、南アフリカ、北アフリカ）の二軸でクラスターを設定。各クラスター内で代表的アンソロジー、国家文学史叙述、領域研究学会誌の3層から起点リストを作成。

### 4.3 利用ツール・DB・検索戦略
African Storybook Project（africanstorybook.org）、World Oral Literature Project（Cambridge）、African Journals Online（AJOL）、Endangered Languages Archive（ELAR, SOAS）、PARADISEC（Sydney大）、Smithsonian National Anthropological Archives、UNESCO Intangible Cultural Heritage、各国国立図書館（National Library of Korea等）、Vietnamese Nôm Preservation Foundation、SEAlang Library。アンソロジー（Heinemann African Writers Series 全書誌、Granta International、Words Without Borders）からの起点抽出。

### 4.4 データ抽出フィールド

`authors`: 各地域の代表作家。primary_language を必ず記録（多言語作家の場合は最も創作量の多い言語）。region は macro_region（'グローバルサウス' 等）と nationality（具体的な国名）の両方を記録。

`works`: 各地域の代表作。language を必ず記録（例: スワヒリ語、英語、ヨルバ語）。original_script は適宜（チューノム、ハングル、アラビア文字、ラテン文字等）。

`concepts`: 地域固有の文学概念（例: ネグリチュード négritude、魔術的リアリズム realismo mágico、testimonio、han 恨）。definition では地域内での原義を記述し、development で他地域への波及（あるいは押し付け）を記述。

`movements`: 地域固有の運動（例: Negritude、Boom Latinoamericano、Onitsha Market Literature、한국 모더니즘）。

口承文学の場合の特別ルール: primary_source_type に 'oral_recording' / 'transcribed_oral' / 'collector_record' を区別して記録し、原資料との隔たりを可視化する。

### 4.5 関係性記述ルール

**relations**: 地域内作家-作家間、地域横断（diaspora）の作家-地域間（'belongs_to'/'addressed_to'）。

**geneal_links**: 西欧理論との借用関係（'borrowed_from'）と、非西欧から西欧への影響関係（'influences' with reverse direction）の双方を記録。後者の数を意識的に確保することで、PROJECT_PLANで定めた「非西欧→西欧の影響リンクが、西欧→非西欧の50%以上」目標を達成する。

**cross_domain**: アフリカ・ラテンアメリカ・先住民領域は AN（人類学）との連携が多い。link_type は parallel が多い（人類学と文学が同じ現象を別言語で扱う場合）。

口承文学の場合は AN との cross_domain を必須付与。

### 4.6 ハルシネーション検証手順

本パターンは資料アクセス困難により最もハルシネーションリスクが高い。手順: (1) 全ての地域固有概念は、地域内学者の論考（一次レベルの権威ある記述）からの引用を必須、(2) 地域言語を読めない場合は二重翻訳経由を明示記録（例: スワヒリ語 → 英語 → 日本語）、(3) C20 と地域専門の Codex が二重チェック、(4) 「西欧理論で解釈された非西欧概念」と「非西欧自身の自己理解」を区別して記録、(5) 口承文学は録音アーカイブの存在を必須確認。`source_tier` は録音アーカイブ・地域内学者の論考 'primary'、批判校訂版 'secondary'、西欧経由二次文献 'tertiary' とし、Tier 3 のみの概念は importance_score を1段下げる。

### 4.7 1日あたり収集ペース目安

1名の Codex が1日に処理できる規模: concepts 15-25件、authors 5-8件、works 8-12件、relations 30-50件。資料アクセス困難により他パターンより低めとなる。地域専門 Codex の作業時間を確保し、無理なペースを設定しない。

---

## 5. Fourth-Transformation Cross-Cut（第四変容軸クロスカット）

### 5.1 適用領域
全24サブフィールドに横断付与。本パターンは独立した収集ではなく、他4パターンで収集された概念に対する横断的なタグ付けと、新規の AI時代固有概念の補充の両方を担う。

### 5.2 入力（収集の起点）
9軸（作者性・創造性・物語・主体・正典・受容・翻訳・真正性・言語）それぞれについて、(a) 古典的代表概念のリスト（PHASE1_AXES_DEFINITION.md 参照）、(b) AI時代に再考対象となる代表概念のリスト、の二重起点。具体的には軸ごとに古典側30概念・AI側10概念程度の起点を確保。

### 5.3 利用ツール・DB・検索戦略
arXiv（cs.CL カテゴリ）と ACL Anthology は AI 技術側の論考、Critical AI 誌（Duke 大）、electronic book review、Ada New Media は AI 時代の文学批評の主要源。AI Index Report（Stanford HAI）は技術動向の参照、MLA Commons の Generative AI Working Group は学界の応答。検索戦略は (1) 9軸キーワード × AI関連語のクロス検索、(2) 既収集概念に対する軸タグ評価、(3) AI時代固有概念（prompt poetics、co-authorship with LLM等）の新規追加。

### 5.4 データ抽出フィールド

主に `fourth_transform_tags` テーブルへの登録: concept_id, axis（9軸のいずれか）, status（'rethinking'/'invariant'/'partial'）, rationale（300-500字）, related_ai_phenomenon。

新規概念追加の場合は `concepts` テーブルへも登録: subfield_id は通常 `lit_digital_ai`（24番目）、region は '横断'、period_id は AI 時代相当。fourth_transform_status を3値で記録。

`relations` への投入: AI時代概念と古典的概念間（'rethinks'/'destabilizes'/'updates'）。例えば「prompt poetics」rethinks 「authorship」のような関係を記録。

### 5.5 関係性記述ルール

**fourth_transform_tags**: 1概念につき複数軸の評価を許容（UNIQUE constraint は concept_id, axis のペア）。3軸以上 'rethinking' となる概念を Phase 4 で「critical concept」として抽出する。

**geneal_links**: AI 時代概念から古典的概念への遡及関係（例: AI co-authorship → Foucault author-function → medieval auctoritas）。transformation_type は extension（古典概念が AI時代に拡張） または critique（AI時代概念が古典概念を批判的に更新）。

**cross_domain**: AI時代概念は PHIL（哲学）と AI Development DB との連携が多い。

### 5.6 ハルシネーション検証手順

本パターンは「AI時代に何が再考対象か」という解釈的判断を含むため、検証が最も繊細。手順: (1) 各 fourth_transform_tag について rationale に必ず参照論考（学術論考または信頼できる批評）を1つ以上記録、(2) related_ai_phenomenon は具体的なAI技術・現象を記述（「生成AI一般」のような曖昧な記述を禁ずる）、(3) 'rethinking' タグの根拠論考は出版年が2020年以降（生成AI普及期以降）であることを優先、(4) C20が9軸の判定基準（PHASE1_AXES_DEFINITION.md）から逸脱がないか週次で確認、(5) 'invariant' タグも積極的に付与し、後段の批判的検証を可能にする。

### 5.7 1日あたり収集ペース目安

本パターンは収集ペースより検証ペースで考える。1名の Codex（C19が主、C20が検証）が1日に処理できる規模: 既収集概念へのタグ付与 50-80件、新規 AI時代概念の追加 5-10件、related_ai_phenomenon 記述 30-50件。Phase 2 期間中の総タグ数目標は 4,000-5,000 件（11,000概念のうち約40%が複数軸タグを持つ想定）。

---

## 6. パターン横断の運用ルール

### 6.1 パターン併用
1つのサブフィールドが複数パターンを併用する場合がある。例えば「ルネサンス・近世文学」はパターン1（古典回帰の側面）とパターン2（人文主義運動）の併用、「日本近現代文学」はパターン2（自然主義・白樺派等の運動）とパターン4（私小説の地域性）の併用となる。Codex 担当者は Phase 2 開始時に各サブフィールドで主パターン1つと副パターン1-2つを宣言する。

### 6.2 source_tier の判定統一基準

- **primary**: PD原典・宣言文・理論家本人の著作からの直接抽出。Tier 1。
- **secondary**: 批判校訂版（Loeb・Murty・新編日本古典文学全集等）・SEP/PhilPapers の理論家エントリ・Cambridge Companion 等の学術解説経由。Tier 2。
- **tertiary**: 上記2層が利用不可で、複数の独立した学術二次文献（最低3件）の合致をもって採録。Tier 3。Phase 3 で再検査対象。

### 6.3 importance_score の判定統一基準

- **5**: 領域内の正典中の正典。標準的学術通史で必ず言及される作品・作家・概念。
- **4**: 重要だが正典中核ではない。学術通史で章節を割いて扱われる。
- **3**: 当該領域の研究者には知られているが、教養レベルでは知られない。
- **2**: 専門研究の対象だが、影響範囲が限定的。
- **1**: 補完的・周辺的。重複・冗長を防ぐためのみ採録。

### 6.4 canonical_in_region の判定基準

- **core**: 当該地域の正典中核。アンソロジー・教科書での言及率が高い。
- **major**: 重要な正典作品だが核ではない。
- **minor**: 専門書では扱われるが一般的な正典リストには入らない。
- **marginal**: 周縁化された存在で、再評価対象。

地域横断の影響度は別軸（importance_score）で評価。例えば古事記は日本文学では canonical_in_region='core'、世界文学全体では importance_score=4。

### 6.5 重複検出と統合

5パターンは独立して走るため、同一概念が複数パターンから登録されるリスクがある。重複検出は (1) name_ja + region + period_id の3キーで一意性チェック（schema.sql の UNIQUE constraint）、(2) name_en・name_original の表記揺れに対しては Phase 3 でファジーマッチング、(3) 同一作家の異なる作品が異なるパターンから登録される場合は authors.id で統合確認。

---

## 7. Phase 1 完了確認

- 5パターンそれぞれの適用領域・入力・利用ツール・抽出フィールド・関係性ルール・検証手順・収集ペースを定義
- パターン横断の source_tier / importance_score / canonical_in_region の判定基準を統一
- 重複検出ルールを確定
- 本書を Phase 2 開始時の Codex 全員のキックオフ資料として配布
