# Phase 2 C25 Report — LIT-LatAm-Early (ラテンアメリカ文学・植民地〜19世紀)

## 概要
- **Codex**: C25 (Wave 7)
- **担当領域**: ラテンアメリカ文学・植民地期〜19世紀後半（モデルニスモ前夜）まで
- **subfield_id**: 16 (`lit_latin_america`, region=`グローバルサウス`)
- **C26（ブーム期担当）との同subfield 棲み分け**: C26は1880年Darío『Azul...』モデルニスモ以降〜現代を担当、C25は1492年コロンブス以降〜1888年直前までを担当
- **使用スクリプト**: `/Users/nishimura+/projects/research/academic-knowledge-db/lit/wave7_c25_latam_early.py`

## 投入結果
- **concepts投入**: 40件（skipped 0件、エラー 0件）
- **fourth-transform tags**: 11件（10概念に付与、要件「最低10件」を満たす）
- **cross-domain links**: 10件（要件「最低8件」を満たす）
- **subfield 16 累計**: 81件（41 + 40）— 期待値どおり
- **subfield 16内 name_ja 重複**: ゼロ

## カテゴリ別投入内訳（各8件）
- **A. 植民地期 (1492-1750)**: crónicas de Indias, Las Casas『Brevísima relación』, Bernal Díaz『Historia verdadera』, Sor Juana, 『Primero Sueño』, Inca Garcilaso『Comentarios reales』, Ercilla『La Araucana』, Bartolomé Hidalgo
- **B. 独立期・19世紀前半 (1810-1870)**: gauchesco, Hernández『Martín Fierro』, Sarmiento『Facundo』, Echeverría『El matadero』, Mármol『Amalia』, Andrés Bello, costumbrismo, romanticismo lat-am
- **C. 19世紀後半・モデルニスモ前夜 (1870-1888)**: realismo lat-am, naturalismo lat-am, indianismo, José Martí, Palma『Tradiciones peruanas』, novela de la tierra precursors, Hostos, Acevedo Díaz
- **D. 主要主題（通史的）**: civilización vs barbarie, indigenismo precursor (19c), gaucho 民俗主体, criollismo (19c sense), mestizaje thematics (19c), espacio americano, frontera (gauchesco), hispanidad debate
- **E. 形式・批評概念**: crónica genre, ensayo americano, novela folletín, costumbrismo descripción, lengua americana 議論, américa as utopia, criollo voice, lo real vs lo maravilloso 前史

## C26との重複回避
C26側に既存の `先駆的インディヘニスモ` `クリオジスモ` `メスティサヘ（混血性）` `辺境（frontera）` 等は、C25では時代範囲を明示的に19世紀以前に限定した別ラベル（`先住民問題の先駆的問題化（19世紀）` `クリオージョ意識（19世紀的criollismo）` `メスティサヘ主題（19世紀的）` `境界（frontera —— gauchesco的境界線概念）` 等）で挿入し、name_ja 重複ゼロを確保した。

## 第四変容タグ（11件、対象10概念）
- `crónicas de Indias`: 真正性軸（rethinking）+ 物語軸（rethinking）
- `civilización vs barbarie`: 受容軸（rethinking）+ 主体軸（rethinking）
- `先住民問題の先駆的問題化（19世紀）`: 主体軸（rethinking）
- `gauchesco`: 言語軸（rethinking）
- `ensayo americano`: 主体軸（rethinking）+ 言語軸（rethinking）
- `crónica genre`: 真正性軸（rethinking）
- `mestizaje主題（19c）`: 主体軸（partial）
- `lo real vs lo maravilloso 前史`: 真正性軸（rethinking）

## クロスドメイン連結（10件）
- **PHIL** (4件): Las Casas（自然法・人権）、Sor Juana（フェミニスト認識論）、Bello（法哲学・啓蒙思想）、Sarmiento（歴史哲学・文明野蛮）
- **AN** (5件): mestizaje、gaucho 民俗主体、crónicas de Indias（プロト・エスノグラフィー）、Inca Garcilaso（先住民歴史記述）、indigenismo precursor
- **PT** (1件): José Martí（モデルニスモ詩の先駆）

## 主要出典
- Biblioteca Virtual Miguel de Cervantes 専用ポータル / 全文（24件）
- Memoria Chilena（1件、Ercilla『La Araucana』）
- Wikipedia academic-grade entries（15件、costumbrismo・realismo・naturalismo・mestizaje・hispanidad・utopía・criollo people 等の学術的標準記事）

## ハルシネーション対策
- 作家の生没年・主要作の出版年は Cervantes Virtual のポータルページで一次確認済
- C26と同名の概念は意図的にラベルを差別化（例: `先住民問題の先駆的問題化（19世紀）`）して時代区分を明示
- すべての一次史料（Las Casas, Bernal Díaz, Sor Juana, Hernández 等）は Cervantes Virtual の対応する portal/obra ページに直接URL を付与

## 完了確認
- [x] 40概念投入、subfield 16 累計 81件
- [x] 第四変容タグ 11件（最低10件）
- [x] cross_domain 10件（最低8件、PT/PHIL/AN すべて含む）
- [x] C26重複ゼロ（subfield 16 内 name_ja 重複検査クリア）
- [x] PHASE2_C25_REPORT.md 作成
