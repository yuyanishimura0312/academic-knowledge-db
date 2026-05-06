# LIT-DB Phase 1 → Phase 2 起動前ゲートチェックリスト

**作成日**: 2026-05-07
**作成者**: academic-db-survey（Phase 1 担当）
**対象**: Phase 2（30日間情報収集）開始前の最終確認項目
**判定者**: 西村勇也（最終承認）+ academic-db-builder + C20

---

## 0. 本書の位置づけ

Phase 1 で確定した9軸操作的定義（PHASE1_AXES_DEFINITION.md）、5参照パターン手順（PHASE1_REFERENCE_PATTERNS.md）、Codex 20名計画（PHASE1_CODEX_PLAN.md）を前提に、Phase 2 を起動するために必要なすべての準備項目を本書で網羅的に確認する。各項目は (1) 確認内容、(2) 担当者、(3) 完了基準 を明記する。全項目クリア後、西村の最終承認をもって Phase 2 を開始する。

チェックリストは6カテゴリ・約40項目で構成される。

1. 一次資料アクセス確認
2. Codex 20名キックオフ準備
3. ハルシネーション検証パイプライン稼働確認
4. 第四変容タグ付与の運用ルール確定
5. DB投入スクリプト雛形の準備
6. Phase 2 進捗管理体制の確立

---

## 1. 一次資料アクセス確認（24領域すべて）

各サブフィールドについて、PHASE0_SCOPE_REPORT.md 1節で列挙した主要源が利用可能か確認する。要機関契約のものは契約状況、オープンのものは URL 有効性、要確認となっているものは代替源確保まで。

### 1.1 西欧文学系譜（7領域）

| # | サブフィールド | 主要源（オープン）| 主要源（要契約・要確認）| 担当 | 完了基準 |
|---|---|---|---|---|---|
| 1 | 古典古代 | Perseus / Sefaria / BibleHub / Gutenberg | TLG / Loeb（要契約） | C01 | オープン4源URL動作確認、TLG/Loebの契約有無を西村に申告 |
| 2 | 中世 | MGH digital / TEAMS / Bibliotheca Augustana / Gallica / Internet Medieval Sourcebook | Digital Medieval Manuscripts at Houghton（名称揺れ要確認） | C02 | オープン5源動作確認、要確認1源の代替確定 |
| 3 | ルネサンス・近世 | Folger Shakespeare / Open Source Shakespeare / Gutenberg / HathiTrust / Internet Archive | EEBO（要契約） | C03 | オープン5源動作、EEBO代替に Internet Archive Wayback で対応可確認 |
| 4 | 啓蒙・ロマン主義 | Gutenberg / HathiTrust / Internet Archive / ARTFL / DTA / Wikisource | （特になし） | C03 | 6源すべて動作確認 |
| 5 | リアリズム・自然主義・象徴主義 | Gutenberg / Gallica / Wikisource / HathiTrust | MLA / JSTOR（要契約） | C04 | オープン4源動作、要契約2源の契約有無申告 |
| 6 | モダニズム | Modernist Journals Project / Modernist Versions Project / Gutenberg AU / HathiTrust | Kafka Project（公式運営状況要確認）/ JSTOR | C04 | オープン4源動作、Kafka Project 代替確定 |
| 7 | ポストモダン・現代 | ELO / Internet Archive Open Library / Wikidata | MLA / JSTOR / Project MUSE（要契約） | C04 | オープン3源動作、要契約3源の契約有無申告 |

### 1.2 東アジア文学系譜（4領域）

| # | サブフィールド | 主要源（オープン）| 主要源（要契約）| 担当 | 完了基準 |
|---|---|---|---|---|---|
| 8 | 中国古典 | CTEXT / 維基文庫 / Scripta Sinica / Kanripo / CBETA | 四庫全書電子版（要契約） | C05 | オープン5源動作確認、API キー確認（CTEXT） |
| 9 | 中国近現代 | 維基文庫 / MCLC / Paper Republic / JSTOR | CNKI / 読秀（要契約） | C06 | オープン4源動作、CNKI契約有無申告 |
| 10 | 日本古典 | NIJL / NDL / J-STAGE / 青空文庫 / 日文研 | ジャパンナレッジ（要契約） | C07 | オープン5源動作、ジャパンナレッジ契約有無 |
| 11 | 日本近現代 | 青空文庫 / NDL / CiNii / J-STAGE / 日本近代文学館 | ジャパンナレッジ（要契約） | C08 | オープン5源動作 |

### 1.3 南アジア・西アジア（3領域）

| # | サブフィールド | 主要源（オープン）| 主要源（要契約・確認）| 担当 | 完了基準 |
|---|---|---|---|---|---|
| 12 | インド | GRETIL / SARIT / Sanskrit Heritage / Digital Library of India / Internet Archive | Murty Classical Library（要契約） | C09 | オープン5源動作、Murty契約有無申告 |
| 13 | アラブ | Al-Maktaba al-Shamela / OpenITI / Arabic Collections Online / Bibliotheca Alexandrina | Brill Encyclopaedia of Islam（要契約）/ AlKindi | C10 | オープン4源動作、Brill契約有無 |
| 14 | ペルシア・トルコ | Ganjoor / Encyclopaedia Iranica / İslam Ansiklopedisi / HathiTrust | Ottoman Text Archive Project（要確認） / Roshan（要確認） | C10 | オープン4源動作、要確認2源の代替確定 |

### 1.4 グローバル・サウス（3領域）

| # | サブフィールド | 主要源（オープン）| 主要源（要契約・確認）| 担当 | 完了基準 |
|---|---|---|---|---|---|
| 15 | アフリカ | African Storybook / WOLP / AJOL / UNESCO Memory of the World | JSTOR / Project MUSE（要契約） | C11 | オープン4源動作 |
| 16 | ラテンアメリカ | Biblioteca Virtual Cervantes / Hemispheric Institute / Gutenberg / Memoria Chilena | LANIC（更新状況要確認）/ JSTOR | C12 | オープン4源動作、LANIC代替確定 |
| 17 | 東南アジア・韓国 | National Library of Korea / Korean Literature Now / Vietnamese Nôm / SEAlang | KRpia / DBpia（要契約） | C13 | オープン4源動作、KRpia/DBpia 契約有無 |

### 1.5 周縁・横断（4領域）

| # | サブフィールド | 主要源（オープン）| 主要源（要契約・確認）| 担当 | 完了基準 |
|---|---|---|---|---|---|
| 18 | ロシア・スラヴ | rvb.ru / FEB / Gutenberg / Wikisource / TITUS | RUCONT / eLIBRARY.RU（要契約） | C14 | オープン5源動作 |
| 19 | 先住民・口承 | WOLP / ELAR / PARADISEC / 国立アイヌ民族博物館 / Smithsonian NAA / UNESCO ICH | （特になし） | C15 | 6源すべて動作確認 |
| 20 | ディアスポラ・移民 | AAWW / Postcolonial Studies @ Emory / The Margins | JSTOR / Project MUSE / MLA（要契約） | C16 | オープン3源動作 |
| 21 | 児童・大衆・ジャンル | ISFDB / Pulp Magazines Project / Baldwin Library / Comic Book Plus / Gutenberg | ICDL（運営状況要確認） | C17 | オープン5源動作、ICDL代替確定 |

### 1.6 理論・横断（3領域）

| # | サブフィールド | 主要源（オープン）| 主要源（要契約・確認）| 担当 | 完了基準 |
|---|---|---|---|---|---|
| 22 | 文学理論・批評 | SEP / PhilPapers | JSTOR / Project MUSE / MLA / Cambridge Companions（要契約） | C18 | オープン2源動作、要契約4源の契約有無申告 |
| 23 | 比較文学・翻訳論 | MLA Bibliography（要契約）/ Institute for World Literature / Index Translationum（要確認） | BTSB / Routledge Translation Studies（要契約） | C19 | 要確認1源の代替確定、要契約3源の契約有無申告 |
| 24 | DH・AI時代 | ELO / Electronic Literature Knowledge Base / Stanford Literary Lab / ACL Anthology / arXiv / MLA Commons | （特になし） | C19 | 6源すべて動作確認 |

### 1.7 確認手順
1. 各 Codex は Week 1 の Day 4-5 にすべての URL に実アクセスし、応答コード・ログイン要否・API有効性を記録
2. 要契約源は西村経由で機関契約状況を確認（既存の他DB契約からの転用可否を含む）
3. 要確認源（運営状況不明）は代替源を最低1つ確保
4. C20 が全結果を集約し、`access_check.md` として lit/ 配下に保存

### 1.8 完了判定
すべての主要源について、(a) 動作確認済、(b) 契約済、(c) 代替源確保済、のいずれかの状態であること。動作不能源が3以上残る場合は Phase 2 開始を1週間延期し代替確保を優先する。

---

## 2. Codex 20名キックオフ準備

### 2.1 必須資料の配布
- PROJECT_PLAN.md
- PHASE0_SCOPE_REPORT.md
- PHASE1_AXES_DEFINITION.md
- PHASE1_REFERENCE_PATTERNS.md
- PHASE1_CODEX_PLAN.md
- 本書（PHASE1_GATE_CHECKLIST.md）
- schema.sql + schema_v0.2_additions.sql + seed_subfields.sql + seed_axes_definitions.sql

### 2.2 キックオフセッション（Day 1）
- 西村による全体方針・問題意識の共有（30分）
- academic-db-builder による Phase 0/1 内容の総括（30分）
- C20 によるハルシネーション検証パイプラインの説明（30分）
- 各 Codex の質疑応答（60分）
- 共通フォーマット（DBへのSQL/Python投入）の実演（30分）

### 2.3 個別キックオフ（Day 2-3）
各 Codex は担当領域の起点リスト（30-50件）を提出。C20 が承認した時点で着手OK。

### 2.4 完了判定
全20名がキックオフ参加完了、起点リスト提出済、入力フォーマット理解確認済。

---

## 3. ハルシネーション検証パイプライン稼働確認

### 3.1 source_tier 判定基準の運用テスト
PHASE1_REFERENCE_PATTERNS.md の §6.2 で定めた3層基準（primary/secondary/tertiary）について、各 Codex が初日に投入した20-30概念の source_tier 評価が一致するか、C20 が抜き打ち検査。一致率80%以上が必要。

### 3.2 一次資料引用の必須記録
全 concepts レコードについて、primary_source_url または key_quote が必須記録。空欄の場合は INSERT 拒否される SQL 制約を Phase 2 開始前に追加：

```sql
-- Phase 2 開始前に追加すべき制約（オプション、運用負荷を見て判断）
-- ALTER TABLE concepts ADD CHECK (primary_source_url IS NOT NULL OR fourth_transform_status IS NOT NULL);
```

ただし上記は強制ではなく、Phase 3 の検証で空欄を抽出してフィードバックするワークフローでも代替可。Phase 2 開始時点では運用ルールとして徹底することで対応。

### 3.3 二重翻訳経由の明示記録
非西欧領域で翻訳経由の概念を記録する場合、概念のbackgroundフィールドに「○○語経由で日本語翻訳」と明記するルールを徹底。

### 3.4 C20 の週次サンプリング監査
各 Codex から週次で20件無作為抽出し、(1) name_original の正確性、(2) 引用の一次資料合致、(3) source_tier の妥当性、(4) cross_domain の整合性、を検査。エラー率10%超で当該 Codex は週次レビューで再教育。

### 3.5 完了判定
- source_tier 一致率テスト合格
- 全 Codex が「一次資料引用」「二重翻訳明示」のルールを口頭確認
- C20 の監査ワークフロー（サンプリングスクリプト）が稼働可能

---

## 4. 第四変容タグ付与の運用ルール確定

### 4.1 9軸操作的定義の DB 投入
seed_axes_definitions.sql で fourth_transform_axes テーブルに9軸の operational_definition / classical_concept / ai_era_phenomenon / rethink_indicator / related_disciplines を投入済（Phase 1 完了時点で確認）。

### 4.2 タグ付与判定の3値運用
- **rethinking**: AI時代に再考対象。rationale と related_ai_phenomenon 必須記入
- **partial**: 部分的に再考対象。どの側面が再考され、どの側面が不変かを rationale に明記
- **invariant**: 再考の必要なし。判定理由を rationale に明記（後段の批判検証のため）

### 4.3 多軸該当の許容
1概念に対して複数軸の評価を許容（UNIQUE constraint は concept_id, axis のペア）。3軸以上 'rethinking' となる概念を Phase 4 で「critical concept」として抽出。

### 4.4 タグ集計の自動化
Phase 3 終了時点で、軸別・サブフィールド別のタグ分布を集計するクエリを Phase 1 中に準備（lit_db_helper.py 内）。

### 4.5 完了判定
- fourth_transform_axes テーブルに9軸定義投入済（SELECT で全項目埋まっていること）
- 3値運用ルールを全 Codex が口頭確認
- 多軸該当を Phase 4 で抽出するクエリ準備完了

---

## 5. DB投入スクリプト雛形の準備

### 5.1 Python ヘルパー（lit_db_helper.py）
本ファイルは Phase 1 成果物5として作成済。以下を含む：
- DB接続ヘルパー
- concepts/authors/works/movements 挿入関数
- relations/geneal_links/cross_domain/fourth_transform_tags 登録関数
- source_tier・canonical_in_region のバリデーション
- 重複検出機能
- 9軸タグ集計クエリ

### 5.2 各 Codex への配布と動作確認
Codex は自分の Python 環境（または Codex 環境）で `lit_db_helper.py` を import し、サンプル INSERT を試行。エラーがないことを確認。

### 5.3 完了判定
- lit_db_helper.py が lit.sqlite に対して全関数のテスト通過
- 各 Codex がサンプル INSERT 成功（最低5件の試行レコード投入）

---

## 6. Phase 2 進捗管理体制の確立

### 6.1 週次レポート様式
各 Codex は週末（金曜日）までに以下を提出：
- 担当領域の concepts/authors/works/movements の累計件数
- 当週の relations / geneal_links / cross_domain 件数
- 第四変容タグの軸別件数
- 完了に近づいている領域・遅延領域の自己評価
- C20 から差し戻しを受けた件数と対応状況

### 6.2 中間レビュー（Day 15）
西村 + academic-db-builder + C20 が全 Codex の進捗を集約し、(1) C03/C04 のサブ分割判断、(2) 目標数の上下調整、(3) リソース再配分、を判断。

### 6.3 進捗ダッシュボード
Phase 2 期間中、`STATUS.md` を週次更新（または日次）。subfield_id ごとの進捗、source_tier 別件数、第四変容タグ分布をリアルタイム可視化。

### 6.4 完了判定
- 週次レポート様式を全員が把握
- 中間レビュー実施日（Day 15）を関係者カレンダーに登録
- STATUS.md の更新フォーマット確定

---

## 7. 最終承認ゲート

すべてのチェック項目（1-6）がクリアされた時点で、本ゲートチェックリストを完了とする。承認順序は以下：

1. C20: 検証パイプラインと監査ワークフロー稼働を承認
2. academic-db-builder: 全成果物の整合性を承認
3. 西村勇也: 最終承認 → Phase 2 起動

承認時刻と承認者を STATUS.md に記録した上で、Phase 2 Day 1 のキックオフセッションを開始する。

---

## 8. Phase 2 起動条件サマリー

| カテゴリ | 確認項目数 | 必達基準 |
|---|---:|---|
| 一次資料アクセス | 24領域 | 動作・契約・代替のいずれかで全領域カバー |
| Codex キックオフ | 20名 | 全員参加、起点リスト提出 |
| 検証パイプライン | 4項目 | source_tier 一致率80%以上 |
| 第四変容タグ運用 | 4項目 | 9軸定義投入、3値ルール周知 |
| 投入スクリプト | 2項目 | lit_db_helper.py 全関数テスト通過 |
| 進捗管理体制 | 4項目 | 週次レポート・中間レビュー・STATUS.md 体制確立 |

すべて完了次第、Phase 2 Day 1（30日間の収集開始日）を確定する。
