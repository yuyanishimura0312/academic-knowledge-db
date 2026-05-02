# 詩学（Poetics）DB構築 引き継ぎ書

**作成日:** 2026-05-03
**プロジェクト:** academic-knowledge-db
**対象テーブル:** humanities_concept（subfield: 古典詩学 他）

---

## 1. 現状サマリ

| 項目 | 値 |
|------|-----|
| 推定総概念数 | 1,650 |
| 70%カバー目標 | 1,155 |
| 登録済み | 88件（既存57 + 古典詩学31） |
| カバー率 | 7.6% |
| 研究者 | 6名登録済み |
| 系譜関係 | 33件登録済み |
| スコープJSON | survey_frames/humanities_poetics_scope.json |

## 2. 完了済みの作業

### Phase 0: スコーピング（完了）
- Princeton Encyclopedia of Poetry and Poetics（1,350項目）等のハンドブック構造分析
- 12サブフィールド x 7時代区分のギャップマトリクス算出
- 収集優先順位の決定

### Phase 2: 古典詩学の収集（完了）
- **31概念**: プラトン3、アリストテレス17、ホラティウス3、ロンギノス2、修辞学6
- **6研究者**: プラトン、アリストテレス、ホラティウス、プセウド・ロンギノス、キケロ、クインティリアヌス
- **33関係**: 批判的継承、拡張、対立、前提条件等
- IDプレフィクス: 概念=`cp_*`、研究者=`res_*`
- 挿入スクリプト: `insert_classical_poetics.py`

### databases.html掲載（完了）
- AK統計値更新済み（8,243知識単位 / 83系譜関係）
- 古典詩学カードを書籍セクションに追加済み

## 3. 未着手の作業（優先順）

### 収集待ちサブフィールド（gap順）

| 優先度 | サブフィールド | 推定 | 現在 | gap | 主な内容 |
|--------|--------------|------|------|-----|---------|
| 1 | 構造主義詩学 | 110 | 3 | 74 | ジュネット、トドロフ、ナラトロジー体系 |
| 2 | 修辞学・弁論術 | 88 | 0 | 62 | 古代〜現代修辞学、メタファー理論 |
| 3 | 古典詩学（追加） | 85 | 2+31 | 27 | 残りの古典概念 |
| 4 | 近代美学・詩学 | 95 | 10 | 57 | カント、ヘーゲル、ロマン主義 |
| 5 | 比較詩学 | 78 | 0 | 55 | ラサ理論、和歌論、中国詩論 |
| 6 | ポスト構造主義詩学 | 75 | 1 | 52 | デリダ、ド・マン、脱構築 |
| 7 | 認知詩学 | 68 | 0 | 48 | ラコフ、ターナー、概念メタファー |
| 8 | 現象学的詩学 | 62 | 0 | 43 | ハイデガー、ガダマー、リクール |
| 9 | 中世・ルネサンス詩学 | 65 | 4 | 42 | ダンテ、シドニー、新古典主義 |
| 10 | 受容理論 | 58 | 0 | 41 | ヤウス、イーザー、読者反応批評 |
| 11 | デジタル詩学 | 56 | 4 | 35 | 電子文学、ハイパーテキスト |
| 12 | ロシア・フォルマリズム | 52 | 1 | 35 | シクロフスキー、ヤコブソン |

### 推奨フェーズ構成

- **Phase 1（基礎）**: 古典詩学追加 + 修辞学 + 近代美学 → 目標350件
- **Phase 2（モダニズム）**: フォルマリズム + 構造主義 + 現象学 → 目標320件
- **Phase 3（現代理論）**: 受容理論 + ポスト構造主義 + 認知詩学 → 目標280件
- **Phase 4（拡張）**: 比較詩学 + デジタル詩学 → 目標205件

## 4. 再開コマンド

```bash
# 次のサブフィールドを収集
/academic-db collect humanities 構造主義詩学
/academic-db collect humanities 修辞学・弁論術
/academic-db collect humanities 近代美学・詩学

# 一括で進める場合
/academic-db collect humanities 比較詩学
/academic-db collect humanities 認知詩学
/academic-db collect humanities ロシア・フォルマリズム

# 監査（ある程度収集後）
/academic-db audit humanities

# 検証
/academic-db verify humanities
```

## 5. DB技術メモ

### テーブル構造
- `humanities_concept`: 主テーブル（subfield='古典詩学' で抽出）
- `researchers`: 研究者テーブル（id=res_* で古典詩学研究者）
- `humanities_concept_relations`: 系譜関係（source/target が cp_* で古典詩学）
- `humanities_concept_researchers`: 概念-研究者の紐付け

### IDルール
- 概念ID: `cp_{英語短縮名}` (例: cp_mimesis, cp_catharsis)
- 研究者ID: `res_{英語名}` (例: res_aristotle, res_plato)
- 関係ID: UUID自動生成

### 確認クエリ
```sql
-- 古典詩学の概念一覧
SELECT name_ja, era_start, status FROM humanities_concept WHERE subfield='古典詩学' ORDER BY era_start;

-- 詩学関連の全サブフィールド件数
SELECT subfield, COUNT(*) FROM humanities_concept WHERE subfield LIKE '%詩%' OR subfield LIKE '%美学%' GROUP BY subfield;

-- 関係一覧
SELECT c1.name_ja, r.relation_type, c2.name_ja
FROM humanities_concept_relations r
JOIN humanities_concept c1 ON r.source_concept_id = c1.id
JOIN humanities_concept c2 ON r.target_concept_id = c2.id
WHERE c1.id LIKE 'cp_%' OR c2.id LIKE 'cp_%';
```

## 6. 注意点

- humanities_conceptとarts_questionの両方に詩学関連データが散在している（arts_questionに文学サブフィールドで6件）
- 今回はhumanities_conceptに集約して収集。artsとの分野横断関係は後で cross-ref で接続予定
- スコーピングの推定値は ±15-20% の誤差範囲あり（詩学の領域境界が美学・修辞学・ナラトロジーと重複するため）
- 古典詩学の既存1件（`1bdb63dc` アリストテレス詩学・カタルシス論, subfield=美学・文芸理論）は別IDで残存。重複ではなく視点が異なる
