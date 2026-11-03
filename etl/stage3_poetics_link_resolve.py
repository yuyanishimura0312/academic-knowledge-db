"""Stage 3: poetics_text_concept_link.concept_id (cp_*) -> humanities_concept / arts_question.
Only identifier evidence resolves a pair. Exact-name matches are stored as CANDIDATES only.
Add-on tables only; existing tables/columns/values are untouched.
"""
import sqlite3, re, random, datetime, json

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
SEED = 20261104
c = sqlite3.connect(DB, timeout=60)
c.execute("PRAGMA busy_timeout=60000")
now = datetime.datetime.now().isoformat(timespec="seconds")
c.executescript("""
CREATE TABLE IF NOT EXISTS poetics_link_resolved(
 link_id TEXT PRIMARY KEY, original_concept_id TEXT NOT NULL, resolved_table TEXT NOT NULL,
 resolved_id TEXT NOT NULL, method TEXT NOT NULL, checked_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS poetics_link_status(
 link_id TEXT PRIMARY KEY, original_concept_id TEXT NOT NULL,
 status TEXT NOT NULL CHECK(status IN('resolved','unresolved')), checked_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS poetics_link_candidate(
 original_concept_id TEXT NOT NULL, candidate_table TEXT NOT NULL, candidate_id TEXT NOT NULL,
 method TEXT NOT NULL, n_candidates_for_slug INTEGER, candidate_name_en TEXT, candidate_subfield TEXT,
 checked_at TEXT NOT NULL, PRIMARY KEY(original_concept_id, candidate_table, candidate_id));
""")
# 1. identifier-based resolution: direct id existence in either table (cp_* ids)
links = c.execute("select id, concept_id from poetics_text_concept_link").fetchall()
ids_h = {r[0] for r in c.execute("select id from humanities_concept")}
ids_a = {r[0] for r in c.execute("select id from arts_question")}
res = []
for lid, cid in links:
    if cid in ids_h:
        res.append((lid, cid, "humanities_concept", cid, "id_exact", now))
    elif cid in ids_a:
        res.append((lid, cid, "arts_question", cid, "id_exact", now))
c.executemany("insert or ignore into poetics_link_resolved values(?,?,?,?,?,?)", res)
resolved = {r[0] for r in res}
c.executemany("insert or replace into poetics_link_status values(?,?,?,?)",
              [(lid, cid, "resolved" if lid in resolved else "unresolved", now) for lid, cid in links])
# 2. candidates by exact normalized name (NOT resolution)
def norm(s): return re.sub(r"[^a-z0-9]+", "_", (s or "").lower()).strip("_")
by = {}
for i, n, sf in c.execute("select id,name_en,subfield from humanities_concept where name_en is not null"):
    by.setdefault(norm(n), []).append((i, n, sf))
cands = 0
for cid in {cid for _, cid in links}:
    m = by.get(cid[3:], [])
    for i, n, sf in m:
        c.execute("insert or ignore into poetics_link_candidate values(?,?,?,?,?,?,?,?)",
                  (cid, "humanities_concept", i, "name_en_slug_exact_CANDIDATE_ONLY", len(m), n, sf, now)); cands += 1
c.executescript("""
DROP VIEW IF EXISTS v_poetics_link_usable;
CREATE VIEW v_poetics_link_usable AS
 SELECT l.*, r.resolved_table, r.resolved_id, r.method AS resolve_method
 FROM poetics_text_concept_link l JOIN poetics_link_resolved r ON r.link_id = l.id;
""")
c.commit()
# verification
n_res = c.execute("select count(*) from poetics_link_resolved").fetchone()[0]
dangling = c.execute("""select count(*) from poetics_link_resolved r where not exists
 (select 1 from humanities_concept h where r.resolved_table='humanities_concept' and h.id=r.resolved_id)
 and not exists (select 1 from arts_question a where r.resolved_table='arts_question' and a.id=r.resolved_id)""").fetchone()[0]
slugs = c.execute("select count(distinct concept_id) from poetics_text_concept_link").fetchone()[0]
cand_slugs = c.execute("select count(distinct original_concept_id) from poetics_link_candidate").fetchone()[0]
cand_unique = c.execute("select count(*) from (select original_concept_id from poetics_link_candidate group by 1 having count(*)=1)").fetchone()[0]
cand_links = c.execute("select count(*) from poetics_text_concept_link where concept_id in (select original_concept_id from poetics_link_candidate)").fetchone()[0]
print(json.dumps(dict(links=len(links), distinct_cp=slugs, resolved_links=n_res, dangling=dangling,
  unresolved=len(links) - n_res, usable_view=c.execute("select count(*) from v_poetics_link_usable").fetchone()[0],
  candidate_slugs=cand_slugs, candidate_slugs_unique=cand_unique, links_with_candidate=cand_links)))
# 20-pair sample (from candidates; resolved set is empty). pairs = (link, concept slug, candidate)
pool = c.execute("""select l.id, l.concept_id, l.text_id, l.discussion_locus, k.candidate_id, k.candidate_name_en, k.candidate_subfield, substr(h.definition,1,160)
 from poetics_text_concept_link l join poetics_link_candidate k on k.original_concept_id=l.concept_id and k.n_candidates_for_slug=1
 join humanities_concept h on h.id=k.candidate_id order by l.id""").fetchall()
random.Random(SEED).shuffle(pool)
out = ["# 無作為20対（乱数種 %d・候補は名前完全一致のみ・一意に当たった概念に限る・母集団 %d リンク）" % (SEED, len(pool)), ""]
for r in pool[:20]:
    out.append("- link=%s | 元ID=%s | text=%s | locus=%s | 候補=%s (%s / %s) | 定義冒頭=%s" % r)
open("/Users/nishimura+/work/rite-editorial-renewal/docs/run/stage3-poetics-sample20.md", "w").write("\n".join(out) + "\n")
