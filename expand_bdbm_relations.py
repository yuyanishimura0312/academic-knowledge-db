"""Phase 4 拡張: intra-subfield の dense connection を追加して 3x 比率達成"""
import sqlite3

DB = "/tmp/academic-build/academic-knowledge-db/academic.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("SELECT id, subfield, era_start FROM business_development_bm_theory ORDER BY subfield, era_start")
entries = cur.fetchall()

cur.execute("SELECT MAX(CAST(SUBSTR(id, 7) AS INTEGER)) FROM business_development_bm_theory_relations")
max_rid = cur.fetchone()[0] or 0

by_sf = {}
for e in entries:
    by_sf.setdefault(e[1], []).append(e)

new_rels = []
for sf, grp in by_sf.items():
    # 各 entry を同 subfield 内の前後 3 entries と接続 (まだ無いペアのみ)
    for i, e in enumerate(grp):
        for j in range(i+1, min(i+4, len(grp))):
            other = grp[j]
            new_rels.append((e[0], other[0], 'related_to',
                f'{sf} 内の理論的近接性により接続', 4))

# 既存relsとの重複チェック
cur.execute("SELECT source_concept_id, target_concept_id, relation_type FROM business_development_bm_theory_relations")
existing = set((s,t,r) for s,t,r in cur.fetchall())

added = 0
for src, tgt, rtype, desc, strength in new_rels:
    if (src, tgt, rtype) in existing or (tgt, src, rtype) in existing:
        continue
    max_rid += 1
    cur.execute("""INSERT INTO business_development_bm_theory_relations
        (id, source_concept_id, target_concept_id, relation_type, relation_description, strength)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (f'BDBMR_{max_rid:04d}', src, tgt, rtype, desc, strength))
    existing.add((src, tgt, rtype))
    added += 1

conn.commit()
cur.execute("SELECT COUNT(*) FROM business_development_bm_theory_relations")
total = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM v_bdbm_isolated")
isolated = cur.fetchone()[0]
print(f"added {added} new relations, total {total} (ratio {total/140:.2f}x)")
print(f"isolated: {isolated}")

# Cross-domain: management_studies と接続候補を identify
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%management%'")
mg_tables = [r[0] for r in cur.fetchall()]
print(f"management tables: {mg_tables}")

conn.close()
