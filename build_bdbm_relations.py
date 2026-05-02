"""Phase 4: 関係ネットワーク構築
- Intra-subfield: 概念数 × 2 (era 順 chain + cross-school)
- Inter-subfield: 概念数 × 1 (keyword/school 重複)
- 目標: 140 × 3-4 = 420-560 関係、接続率100%
"""
import sqlite3
import json
import itertools

DB = "/tmp/academic-build/academic-knowledge-db/academic.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

# 全エントリ取得
cur.execute("""
SELECT id, name_en, subfield, school_of_thought, era_start, keywords_en
FROM business_development_bm_theory
ORDER BY subfield, era_start
""")
entries = [dict(zip(['id','name_en','subfield','school','era','keywords'], r)) for r in cur.fetchall()]
print(f"loaded {len(entries)} entries")

relations = []
rid = 0

def add_rel(src, tgt, rtype, desc, strength):
    global rid
    rid += 1
    relations.append({
        'id': f'BDBMR_{rid:04d}',
        'source': src, 'target': tgt,
        'type': rtype, 'desc': desc, 'strength': strength
    })

# === 1. Intra-subfield: same school chain (extends/derived_from) ===
# era 順に school 内で chain を作る
by_subfield_school = {}
for e in entries:
    key = (e['subfield'], e['school'])
    by_subfield_school.setdefault(key, []).append(e)

for (sf, school), grp in by_subfield_school.items():
    grp.sort(key=lambda x: x['era'])
    for i in range(len(grp)-1):
        prev, curr = grp[i], grp[i+1]
        add_rel(curr['id'], prev['id'], 'derived_from',
                f"{curr['name_en']} は {prev['name_en']} の理論的延長として {school} 内で発展",
                7)

# === 2. Intra-subfield: same subfield, different school (related_to/competes_with) ===
by_subfield = {}
for e in entries:
    by_subfield.setdefault(e['subfield'], []).append(e)

for sf, grp in by_subfield.items():
    # 各 entry を era 順で並べ、各 entry を 1-2 個の他 school 概念に related_to で接続
    grp.sort(key=lambda x: x['era'])
    for i, e in enumerate(grp):
        for j in range(max(0,i-2), i):
            other = grp[j]
            if other['school'] != e['school']:
                add_rel(e['id'], other['id'], 'related_to',
                        f"{sf} 内で {other['school']} と {e['school']} の系譜が並走",
                        5)
                break

# === 3. Critique relationships (固定マッピング) ===
critique_map = [
    # (critic_id, target_id, desc)
    ('BDBM_010','BDBM_002', 'Klang らは BM Canvas を含む BM 概念全般のあいまいさを批判'),
    ('BDBM_014','BDBM_011', 'Markides は BMI 研究を ambidexterity literature と接続して再解釈・補完'),
    ('BDBM_024','BDBM_023', 'Cusumano らは Platform Revolution を含む楽観論に規制視点で批判'),
    ('BDBM_035','BDBM_032', 'Park-Ungson は Relational View の楽観性に経営的複雑性で反論'),
    ('BDBM_044','BDBM_041', 'Hill-Birkinshaw は Burgelman プロセスモデルを実証的失敗率で補強・批判'),
    ('BDBM_054','BDBM_051', 'Prahalad の BoP は伝統的 Ansoff Matrix の市場開発概念を新興国向けに拡張・批判'),
    ('BDBM_064','BDBM_061', 'Trott-Hartmann は Open Innovation の概念新規性に疑問を投じる'),
    ('BDBM_074','BDBM_072', 'Felin らは Lean Startup の理論的根拠を学術的に批判'),
    ('BDBM_084','BDBM_081', 'Lepore は Christensen Disruption の歴史的事例選定を批判'),
    ('BDBM_094','BDBM_091', 'Iansiti-Lakhani は Subscription/Platform 経済の lock-in を批判'),
    ('BDBM_104','BDBM_102', 'Hahn らはサステナブル BM の楽観論にトレードオフで批判'),
    ('BDBM_114','BDBM_113', 'Webb は EC 時代のオムニチャネル管理の摩擦を実証'),
    ('BDBM_124','BDBM_123', 'Sheth-Sharma は関係性営業の限界を Challenger Sale 移行の文脈で論じる'),
    ('BDBM_134','BDBM_131', 'Cartwright-Schoenberg は 30年研究で M&A 失敗率の高さを実証し Haspeslagh-Jemison 楽観論を批判'),
]
for c, t, d in critique_map:
    add_rel(c, t, 'critiques', d, 8)

# === 4. Inter-subfield: 親和性高いペアで bridges (complements/influenced) ===
inter_bridges = [
    # (sf1, sf2, [(id1,id2,desc), ...])
    ('bmi_theory','bmi_process', [
        ('BDBM_002','BDBM_012', 'BM Canvas (理論) は Strategy-BM 階層 (プロセス) で operationalize'),
        ('BDBM_003','BDBM_015', 'Activity System view は Dynamic Capabilities for BM へと統合される'),
    ]),
    ('digital_platform','open_innov', [
        ('BDBM_021','BDBM_070', 'Two-sided market 理論は Open Business Model 概念を加速'),
        ('BDBM_023','BDBM_067', 'Platform Revolution は Crowdsourcing メカニズムを内蔵'),
    ]),
    ('alliance','ma_corp_dev', [
        ('BDBM_032','BDBM_133', 'Relational View は M&A 統合の理論基盤として参照'),
        ('BDBM_038','BDBM_137', 'Alliance Portfolio 思考は Spin-offs/Divestments 戦略にも応用'),
    ]),
    ('corp_venture','lean_startup', [
        ('BDBM_041','BDBM_071', 'Burgelman 内部ベンチャープロセスは Customer Development の組織内応用と整合'),
        ('BDBM_049','BDBM_077', 'Corporate Accelerator は Lean Canvas を主要ツールとして採用'),
    ]),
    ('disruptive','market_entry', [
        ('BDBM_086','BDBM_054', 'New-Market Disruption は BoP 戦略と非消費者市場で重なる'),
        ('BDBM_085','BDBM_057', 'Low-End Disruption は Beachhead 戦略の典型形態'),
    ]),
    ('subscription_saas','b2b_enterprise', [
        ('BDBM_093','BDBM_130', 'Customer Success は RevOps 統合の中心機能'),
        ('BDBM_099','BDBM_125', 'Product-Led Growth と ABM は B2B SaaS GTM の二大潮流'),
    ]),
    ('sustainable_bm','bmi_theory', [
        ('BDBM_102','BDBM_004', 'Bocken サステナブル BM Archetypes は BMI 批判的評価で言及される'),
        ('BDBM_107','BDBM_002', 'CSV (共有価値) は BM Canvas の価値提案を社会的価値で拡張'),
    ]),
    ('channel_gtm','b2b_enterprise', [
        ('BDBM_120','BDBM_125', 'GTM Design Pyramid は ABM 実装の基盤フレーム'),
        ('BDBM_118','BDBM_129', 'Channel Partner Program は Sales Enablement 機能と統合運用'),
    ]),
    ('lean_startup','disruptive', [
        ('BDBM_071','BDBM_082', 'Customer Development はイノベーターの解の組織アジリティ要件と整合'),
    ]),
    ('open_innov','corp_venture', [
        ('BDBM_062','BDBM_045', 'Open Innovation 編著は Strategic CVC を OI 実装手段として位置づけ'),
    ]),
    ('digital_platform','subscription_saas', [
        ('BDBM_022','BDBM_092', 'Two-sided market 戦略は MSP 戦略決定の延長で再展開'),
        ('BDBM_029','BDBM_100', 'Platform Governance は Usage-Based Pricing の境界資源として運用'),
    ]),
    ('alliance','open_innov', [
        ('BDBM_036','BDBM_061', 'Coopetition は Open Innovation のパラダイムと整合する組織間関係概念'),
    ]),
    ('ma_corp_dev','corp_venture', [
        ('BDBM_138','BDBM_045', 'CVC は M&A の代替・補完手段として戦略的 CV と連続性'),
    ]),
    ('market_entry','channel_gtm', [
        ('BDBM_055','BDBM_112', '参入モード選択は直接 vs 間接チャネルの古典的問題'),
    ]),
]
for sf1, sf2, links in inter_bridges:
    for s, t, d in links:
        add_rel(s, t, 'complements', d, 6)

# === 5. Influenced (時代横断の影響関係) ===
influenced_map = [
    ('BDBM_002','BDBM_001', 'BM Canvas は Magretta 概念確立を実装可能なフレームに発展'),
    ('BDBM_087','BDBM_081', 'Jobs-to-be-Done は Innovator\'s Dilemma の延長線上'),
    ('BDBM_023','BDBM_021', 'Platform Revolution は Two-sided Markets 理論を実務化'),
    ('BDBM_072','BDBM_071', 'Lean Startup は Customer Development を体系化・大衆化'),
    ('BDBM_106','BDBM_105', 'Circular Economy は Triple Bottom Line 思想を発展'),
    ('BDBM_109','BDBM_105', 'Doughnut Economics は Triple Bottom Line と Stakeholder Theory を統合'),
    ('BDBM_110','BDBM_105', 'Stakeholder Theory は Triple Bottom Line の理論基盤'),
    ('BDBM_123','BDBM_122', 'Challenger Sale は SPIN Selling の延長で発展'),
    ('BDBM_127','BDBM_126', 'MEDDIC は Solution Selling の qualification 強化版'),
    ('BDBM_131','BDBM_133', 'Haspeslagh-Jemison 統合4類型は King-Bauer-Schriber レビューで継承'),
    ('BDBM_088','BDBM_021', 'Modularity Theory は Two-sided market の構造的基盤を提供'),
    ('BDBM_088','BDBM_023', 'Modularity Theory は Platform Revolution の architecture 議論に直結'),
    ('BDBM_046','BDBM_080', 'Stage-Gate System は Concierge MVP の段階的検証思想と整合'),
    ('BDBM_048','BDBM_017', 'Ambidextrous Organization は BMI in Established Firms の組織論基盤'),
]
for s, t, d in influenced_map:
    add_rel(s, t, 'influenced', d, 6)

# === 6. SQL 投入 ===
print(f"generated {len(relations)} relations")

# 既存削除
cur.execute("DELETE FROM business_development_bm_theory_relations")

ins = """INSERT INTO business_development_bm_theory_relations
(id, source_concept_id, target_concept_id, relation_type, relation_description, strength)
VALUES (?, ?, ?, ?, ?, ?)"""
for r in relations:
    cur.execute(ins, (r['id'], r['source'], r['target'], r['type'], r['desc'], r['strength']))

conn.commit()

# === 7. 接続率検証 ===
cur.execute("SELECT COUNT(*) FROM business_development_bm_theory_relations")
print(f"inserted {cur.fetchone()[0]} relations")

cur.execute("SELECT COUNT(*) FROM v_bdbm_isolated")
isolated = cur.fetchone()[0]
print(f"isolated entries: {isolated}")

# 関係タイプ分布
print("\n=== relation type distribution ===")
cur.execute("SELECT relation_type, COUNT(*) FROM business_development_bm_theory_relations GROUP BY relation_type ORDER BY 2 DESC")
for t, c in cur.fetchall():
    print(f"  {t}: {c}")

conn.close()
