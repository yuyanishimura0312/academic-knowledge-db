# 自然科学 DB 品質バックログ

2026-05-11 ak.html 質的向上 Phase 1 で発見した、次フェーズで対処すべき項目。

## P1: 研究者リンクの致命的不足
- `natural_discovery_researchers` テーブル: 現状 **7 行のみ**（全 3,641 概念に対し）
- 登録済み: Curtis Suttle / Farooq Azam / Jay Lennon / Jo Handelsman / Mitchell Sogin / Sergei Winogradsky / Thomas Brock
- いずれも理論生態学・群集生態学に偏り、物理学・化学・神経科学・数学の代表研究者は構造化されていない
- 概念側の `主要研究者` 自由記述フィールドにのみ存在する想定
- **対処**: 自由記述フィールドを抽出 → researchers マスタへ正規化 → リンクテーブル化

## P2: 関係タイプの単一化
- 系譜系の関係は `derived_from` 7,498 件のみ
- `extends` / `builds_on` は **0 件**（他分野では使われている）
- 「批判」「対立」「拡張」「反証」等の関係軸の解像度が低い
- **対処**: 既存の `derived_from` を再分類するか、追加の関係抽出パスを走らせる

## P3: サブフィールド分類の境界事例
- 「化学」サブフィールドに「大気大循環」「ニュートンの光学」など、地球科学・物理学に近い概念が混入
- Phase 11/12 で境界調整したが完全ではない
- **対処**: 概念名+definition を Codex に与え、サブフィールド再判定 → 人手レビュー

## P4: 2015 年以降の比率の薄さ
- 自然科学 2015+ = 16.6%（5 分野中最下位）
- 生成 AI 時代の生命科学・量子計算・気候モデリング等が手薄
- **対処**: 次フェーズの収集計画で現代側を優先

## P5: 系譜チェーンのサブフィールド labeling 矛盾
- 「コペルニクスの地動説」「ニュートンの光学」が `理論生態学` サブフィールドに分類されている系譜チェーンが抽出された
- これは P3 と同根の問題（キーワード自動分類の暴走）
- **対処**: P3 と同時に修正

## 関連
- 元ダッシュボード: `~/projects/apps/miratuku-news-v2/dashboards/ak.html`
- 抽出データ: `~/projects/apps/miratuku-news-v2/dashboards/_ak_natural_materials.json`
- 抽出スクリプト: `_extract_ak_natural.py`
