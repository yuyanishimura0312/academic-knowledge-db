# Phase 2 — C37 Wave 7 Report
## LIT-Theory: Critical Theory（ジェンダー・ポストコロニアル・エコクリティシズム）

- 投入日: 2026-05-07
- ファイル: `wave7_c37_critical_theory.py`
- subfield_id: 22 / code: `lit_theory` / region: `理論`

## 投入サマリー

| 指標 | 投入数 | 備考 |
| --- | ---: | --- |
| concepts | 30 | A:ジェンダー10 + B:ポストコロニアル10 + C:エコクリティシズム10 |
| periods | 3（新規） | フェミニズム第一・第二波 / ポスト構造主義以後 / 環境・脱植民地・ポストヒューマン期 |
| fourth_transform_tags | 20 | 9軸全可能性のうち6軸（主体・言語・受容・翻訳・正典・物語・作者性・創造性・真正性）に分布 |
| cross_domain | 15 | PHIL: 7、AN: 4、AI-Development: 2、（重複なし） |
| relations | 35 | A内9 / B内10 / C内10 / 横断6 |

## ハルシネーション防止のための一次ソース戦略

### 直接的「primary」（著者本人テクスト・ジャーナル初出）
- Cixous "Laugh of the Medusa"（Signs 1976、JSTOR）
- Showalter "Toward a Feminist Poetics"（JSTOR）
- Crenshaw 1989（U. Chicago Legal Forum オープンアーカイブ）
- Hall "Cultural Identity and Diaspora"（1990）
- Mbembe "Necropolitics"（Public Culture 2003、Project MUSE）
- Chakrabarty "The Climate of History"（Critical Inquiry 2009）
- Woolf "A Room of One's Own"（Project Gutenberg Australia）
- Sedgwick *Epistemology of the Closet*、Bhabha *Location of Culture*、Said canonical 等

### SEP参照に降格した secondary
- Irigaray「parler-femme」: SEPエントリーから引用（一次の `Ce sexe qui n'en est pas un` の確実な無料原典がないため）
- Deep ecology: SEP環境倫理エントリー（ネス1973原典の安定URLを避けた）
- McRobbie ポストフェミニズム: 著者の書籍より、Feminist Media Studies 論文をJSTOR経由で引用

## 第四変容タグ分布

| 軸 | rethinking | 該当概念例 |
| --- | ---: | --- |
| 主体 | 7 | パフォーマティヴィティ、サバルタン、ミミクリ／ハイブリディティ、ポストヒューマニズム 等 |
| 言語 | 3 | écriture féminine、parler-femme、精神の脱植民地化 |
| 受容 | 3 | オリエンタリズム、精神の脱植民地化、人新世文学 |
| 翻訳 | 1 | ミミクリ／ハイブリディティ／第三空間 |
| 物語 | 1 | 人新世文学 |
| 正典 | 1 | ガイノクリティシズム |
| 作者性 | 1 | 自分ひとりの部屋 |
| 創造性 | 1 | ポストヒューマニズム |
| 真正性 | 1 | サバルタン |
| 物語 / 作者性 | – | 設計通り、6軸以上に拡散 |

## cross_domain 分布

| 接続先DB | 件数 | 主な接続概念 |
| --- | ---: | --- |
| PHIL | 7 | パフォーマティヴィティ・インターセクショナリティ・オリエンタリズム・サバルタン・ファノン・ハイブリディティ・ネクロポリティクス・ポストヒューマニズム |
| AN | 4 | オリエンタリズム（他者表象）、ハイブリディティ、植民地的差異、ディアスポラ、環境人文学 |
| AI-Development | 2 | ポストヒューマン主体性、人新世とAI（technosphere並行） |

## 関係性ハイライト（35件中の核）

- セゼール → ファノン → バーバ：脱植民地理論の三世代系譜
- Said → Spivak → Bhabha：ポストコロニアル批評の正典トライアングル
- Woolf → Showalter → Gilbert&Gubar：英米女性作家批評の正典系譜
- Cixous ↔ Irigaray ↔ Kristeva：フランス・フェミニズム三角形
- Butler → Queer theory ← Crenshaw：90年代差異理論の合流
- Ecocriticism → Posthumanism → Anthropocene literature：エコクリティシズム第一波→第四波
- 横断架橋（gender × postcolonial × eco）6本：交差性・エコフェミ・ポストヒューマン・ネクロポリティクス・脱植民地など

## 検証クエリ

```sql
-- 投入数確認
SELECT COUNT(*) FROM concepts WHERE subfield_id=22;
-- → 30

SELECT COUNT(*) FROM fourth_transform_tags t
JOIN concepts c ON c.id=t.concept_id WHERE c.subfield_id=22;
-- → 20

SELECT COUNT(*) FROM cross_domain cd
JOIN concepts c ON c.id=cd.lit_entity_id
WHERE cd.lit_entity_type='concept' AND c.subfield_id=22;
-- → 15

SELECT COUNT(*) FROM relations r
JOIN concepts c ON c.id=r.source_id
WHERE r.source_type='concept' AND c.subfield_id=22;
-- → 35
```

## 留意点

- 30件投入のため target=100 に対し 30%（先行投入）。後続Codexと連携して残り70件は `lit_theory` で他理論Codex（フォルマリズム・構造主義・脱構築・受容理論等）が分担する。
- ポストコロニアル領域は誤情報リスクが高いため、`source_tier='primary'` 採用は著者本人初出論文・ジャーナル初出に限定し、伝聞ベースの記述は避けた。
- 30概念中 `primary` 24 / `secondary` 6（Irigaray・deep ecology・McRobbie・ポストコロニアル理性整序など）。
