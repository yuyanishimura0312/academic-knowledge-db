#!/usr/bin/env python3
"""Import Phase 6 poetics expansion (12 Codex workers) into academic.db."""

import json, sqlite3, uuid
from pathlib import Path

DB_PATH = Path(__file__).parent / "academic.db"
COLLECT_DIR = Path("/tmp/poetics_collect_p6")
FILES = sorted(f.name for f in COLLECT_DIR.glob("P6_*.json"))

POETICS_SUBFIELDS = (
    '古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム',
    '近代美学・詩学','現象学的詩学','中世・ルネサンス詩学',
    'ポスト構造主義詩学','受容理論','認知詩学','比較詩学','デジタル詩学'
)

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=OFF")
    cur = conn.cursor()

    concepts, researchers, relations = {}, {}, []
    for fname in FILES:
        d = json.loads((COLLECT_DIR / fname).read_text())
        for c in d.get("concepts", []):
            cid = c.get("id")
            if cid and cid not in concepts:
                concepts[cid] = c
        for r in d.get("researchers", []):
            rid = r.get("id")
            if rid and rid not in researchers:
                researchers[rid] = r
        for rel in d.get("relations", []):
            relations.append(rel)

    print(f"Loaded: {len(concepts)} concepts, {len(researchers)} researchers, {len(relations)} relations")

    cur.execute("SELECT id FROM humanities_concept")
    existing_c = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT id FROM researchers")
    existing_r = {r[0] for r in cur.fetchall()}

    r_ins = r_skip = 0
    for r in researchers.values():
        if r["id"] in existing_r:
            r_skip += 1; continue
        name_full = r.get("name_full") or r.get("name_en") or r.get("name") or r["id"]
        cur.execute("""INSERT INTO researchers (id,name_full,name_ja,birth_year,death_year,nationality,primary_institution,research_themes,biography_brief) VALUES (?,?,?,?,?,?,?,?,?)""",
            (r["id"], name_full, r.get("name_ja"), r.get("birth_year") or r.get("born"), r.get("death_year"), r.get("nationality") or r.get("country"), r.get("primary_institution"), r.get("research_themes") or r.get("field"), r.get("biography_brief") or r.get("contribution")))
        existing_r.add(r["id"]); r_ins += 1
    print(f"Researchers: inserted {r_ins}, skipped {r_skip}")

    c_ins = c_skip = c_err = 0
    for c in concepts.values():
        if c["id"] in existing_c:
            c_skip += 1; continue
        name_ja = c.get("name_ja") or c.get("name_en") or c["id"]
        if not name_ja:
            c_err += 1; continue
        cur.execute("""INSERT INTO humanities_concept (id,name_ja,name_en,name_original,definition,impact_summary,subfield,school_of_thought,era_start,era_end,methodology_level,keywords_ja,keywords_en,status,source_reliability,data_completeness) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (c["id"], name_ja, c.get("name_en"), c.get("name_original"), c.get("definition"), c.get("impact_summary"), c.get("subfield"), c.get("school_of_thought"), c.get("era_start"), c.get("era_end"), c.get("methodology_level"), c.get("keywords_ja"), c.get("keywords_en"), "active", "secondary", 70))
        existing_c.add(c["id"]); c_ins += 1
        oid = c.get("originator_id")
        if oid and oid in existing_r:
            try:
                cur.execute("INSERT OR IGNORE INTO humanities_concept_researchers (concept_id,researcher_id,role,year_associated,note) VALUES (?,?,?,?,?)",
                    (c["id"], oid, "originator", c.get("year_proposed"), c.get("founding_work")))
            except sqlite3.IntegrityError:
                pass
    print(f"Concepts: inserted {c_ins}, skipped {c_skip}, errors {c_err}")

    rel_ins = rel_skip = rel_dup = 0
    seen = set()
    for rel in relations:
        s, t, rt = rel.get("source_id"), rel.get("target_id"), rel.get("relation_type","related")
        if s not in existing_c or t not in existing_c:
            rel_skip += 1; continue
        key = (s, t, rt)
        if key in seen:
            rel_dup += 1; continue
        seen.add(key)
        cur.execute("INSERT INTO humanities_concept_relations (id,source_concept_id,target_concept_id,relation_type,relation_description,strength,is_confirmed) VALUES (?,?,?,?,?,?,?)",
            (str(uuid.uuid4()), s, t, rt, rel.get("description"), rel.get("strength",5), 1))
        rel_ins += 1
    print(f"Relations: inserted {rel_ins}, skipped(missing) {rel_skip}, skipped(dup) {rel_dup}")

    conn.commit()

    cur.execute("SELECT subfield, COUNT(*) FROM humanities_concept WHERE subfield IN ({}) GROUP BY subfield ORDER BY COUNT(*) DESC".format(",".join("?"*len(POETICS_SUBFIELDS))), POETICS_SUBFIELDS)
    print("\n=== Final Poetics DB stats ===")
    total = 0
    for sf, n in cur.fetchall():
        print(f"  {sf}: {n}")
        total += n
    print(f"  TOTAL: {total}")
    print(f"  Coverage: {total}/1650 (estimated total) = {total/1650*100:.1f}%")
    print(f"  vs 70% target (1,155): {total/1155*100:.1f}%")

    cur.execute("SELECT COUNT(DISTINCT r.id) FROM researchers r JOIN humanities_concept_researchers hcr ON r.id=hcr.researcher_id JOIN humanities_concept hc ON hc.id=hcr.concept_id WHERE hc.subfield IN ({})".format(",".join("?"*len(POETICS_SUBFIELDS))), POETICS_SUBFIELDS)
    print(f"  Researchers linked: {cur.fetchone()[0]}")

    cur.execute("SELECT COUNT(*) FROM humanities_concept_relations rel JOIN humanities_concept c1 ON rel.source_concept_id=c1.id JOIN humanities_concept c2 ON rel.target_concept_id=c2.id WHERE c1.subfield LIKE '%詩学%' OR c2.subfield LIKE '%詩学%' OR c1.subfield LIKE '%美学%' OR c2.subfield LIKE '%美学%' OR c1.subfield LIKE '%修辞%' OR c2.subfield LIKE '%修辞%' OR c1.subfield LIKE '%受容%' OR c2.subfield LIKE '%受容%' OR c1.subfield LIKE '%フォルマ%' OR c2.subfield LIKE '%フォルマ%'")
    print(f"  Relations: {cur.fetchone()[0]}")

    cur.execute("SELECT COUNT(*) FROM researchers")
    print(f"  Total researchers in DB: {cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
