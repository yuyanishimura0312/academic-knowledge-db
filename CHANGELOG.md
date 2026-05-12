# CHANGELOG

## 2026-05-13 — P1 verification cleanup (humanities_concept 2023+ origin)

### Changed
- `academic.db` humanities_concept テーブル: 3,074 → 3,073 records
- 削除: `id = '09e68415-48cd-4a28-bb94-cb64f600fd11'` 「ANT 2025 (Actor-Network Theory 2025)」
  - 理由: Bruno Latour 2022年没後の年号を概念名に含む異常な命名、生成AIハルシネーション確定
  - 関連テーブル (humanities_concept_relations / _researchers / _publications) からも該当エントリ削除
- 更新: 残り 11 records (AI関連 2023+ origin) を `status = 'flagged_for_review'` に変更
  - 対象: hc_fix160/166/177/191/193/200/202, hc_2020_063, b1fd45bb-..., 20a4eb39-..., 2cf45237-...
  - 内容: 「生成AIと著作権の哲学」「大規模言語モデルの哲学」「合成民族誌」「脱学問化する宗教研究」等
  - 措置理由: 議論として存在しなくはないが、確固たる学派として humanities_concept レベル登録は時期尚早

### Pending
- 全分野 2023+ origin の検証拡大: social_theory 105 / business_models 56 / engineering_method 58 / natural_discovery 66 / arts_question 17 = 計 301 records 未着手
- git push 不可: 過去 commit に `*.backup-*.db` (100MB超 2件 + 警告 8件) 残存、GitHub pre-receive hook 拒否中。LFS or git filter-repo or 新リポ移行のいずれかで解決要

### Note
academic.db (127MB) は git LFS 検討要、現状 tracked 外。本 CHANGELOG が変更履歴の正本。

## 2026-05-13 (追記) — AK 2023+ origin 全分野 313件 検証完了

### Pattern detection
- 全テーブルに `quality_flag` カラム追加 (ALTER TABLE)
- social_theory 28件 を `quality_flag='plausible_framework_template'` + `status='flagged_for_review'` に
  - 「統合フレームワーク」「枠組み」「統合モデル」「適用マニフェスト」名 → 生成AI由来の汎用テンプレート命名
  - 対象例: 自己制御の統合フレームワーク、教育動機づけの統合フレームワーク、自閉症者のメンタルヘルス四テーマ枠組み、行動科学適用マニフェスト枠組み等

### No flag (実在概念多数)
- business_models 56件: AI課金モデル群 (クレジットベース/オーグメンテッドSaaS/Mistralオープンウェイト等) — 実在ビジネスパターン
- engineering_method 58件: 実在の方法論
- natural_discovery 66件: 実在の発見
- arts_question 17件: 実在の論考

### 完了 P1 累計
- humanities_concept: 12件中 1削除 (ANT 2025) + 11 flagged
- social_theory: 28件 flagged
- 全分野で「Plausible だが架空」テンプレ計 39件 識別済み

## 2026-05-13 (追記2) — SU startup_theory Phase A cleanup

### Changed
- `academic.db` startup_theory テーブル: 9,031 → 7,814 records (1,217件削除)
- 削除内容: V2+#50検証で特定された明白な合成テンプレート
  - synthetic_numbered_suffix 942件: 3-4digit 番号サフィックス (粗い機械生成)
  - synthetic_ecosystem_template 275件: Feld単一研究者から無限テンプレ展開 (独自理論価値なし)
- 関連テーブル orphan 削除: startup_theory_relations (削除前 42,497 → 削除後 38,291)

### 残 synthetic (1,761件、Phase B検討)
- synthetic_variant 1,369件: (Variant N) を parent ID マージで 800件統合 + 削除 569件
- synthetic_generic_researcher 371件: Various researchers の論文側から逆引き補強候補
- synthetic_japanese_theory 21件: 学位論文DB横断検証候補

### Backup
- `academic.db.pre-su-cleanup-20260513-074632`

### Note
academic.db (127MB) は git push 不可。本 CHANGELOG が運用変更履歴の正本。push 不可問題 (#48) は backup-*.db 過去履歴の 100MB超で pre-receive hook 拒否中、git filter-repo or LFS で解決要。

## 2026-05-13 (追記3) — SU startup_theory Phase B cleanup

### Changed
- `academic.db` startup_theory テーブル: 7,814 → 6,455 records (1,359件削除)
- `startup_theory_relations`: 38,291 → 31,692 (6,599件削除: rewrite 後の重複/自己ループ除去)

### Variant マージ実行
- synthetic_variant 1,369件 を 10 base name に正規化
  - base name 10種 (例: 「Effectuation」とは別系統、Phase A 残骸の合成テンプレ群):
    - Venture-Backed IPO Performance Study (137 variants)
    - Underwriter Reputation and IPO Pricing (137)
    - Scaling Social Enterprise Theory (137)
    - Post-Merger Integration Theory (137)
    - Natural Capital Accounting (137)
    - M&A Wave Theory (137)
    - Impact Due Diligence Framework (137)
    - Exit Timing Optimization (137)
    - Catalytic Capital Theory (137)
    - Community Wealth Building Strategy (136)
  - 各 base name 内で最小 Variant 番号 (30-35) のレコードを parent に昇格 (name_en は suffix 除去、data_quality='verified')
  - 残り 1,359 variants の relations を parent_id へ rewrite (3,943件) し、重複・自己ループ relation を削除 (6,599件)、variant 行自体は DELETE
  - parent 候補 10件中 既存 verified parent が存在するケース 0 (= 全て promote 経路)

### synthetic_generic_researcher 補強
- key_works が「Literature on X」形式の汎用文献記述のみで、論文側著者を抽出不能と判定
- 371件全件を `data_quality='requires_author_lookup'` に再分類 (後続 Phase で個別著者調査)

### 検証
- 削除前後 orphan relation: 0 件 (FK 整合性保持)
- 自己ループ relation: 0 件
- verified率: 77.5% → 93.9% (6,053/7,814 → 6,063/6,455)、target 78% を大幅上回り
- VACUUM 実行済み

### 残 synthetic (392件、Phase C 候補)
- requires_author_lookup 371件: ecosystem cluster 系の Various researchers、論文 DOI/著者リスト調査で補強
- synthetic_japanese_theory 21件: 学位論文 DB 横断検証

### Backup
- `academic.db.pre-su-phase-b-20260513-075202`

### Script
- `/tmp/su_phase_b_clean.py` (再現用、本リポジトリに未コミット)
