#!/usr/bin/env python3
"""
Extract natural_discovery materials for ak.html dashboard.
Pure SQL extraction — no AI generation, no embellishment.
"""
import json
import sqlite3
from collections import defaultdict, Counter
from pathlib import Path

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
OUT_PATH = "/Users/nishimura+/projects/apps/miratuku-news-v2/dashboards/_ak_natural_materials.json"

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()


def trunc(text, n=120):
    if text is None:
        return None
    s = str(text)
    return s[:n]


# ---------- A. Subfield representative (3 per subfield) ----------
subfields = [r["subfield"] for r in cur.execute(
    "SELECT DISTINCT subfield FROM natural_discovery WHERE subfield IS NOT NULL ORDER BY subfield"
).fetchall()]

subfields_rep = {}
for sf in subfields:
    rows = cur.execute(
        """
        SELECT id, name_ja, name_en, subfield, era_start, era_end,
               definition, school_of_thought, data_completeness
          FROM natural_discovery
         WHERE subfield = ?
         ORDER BY data_completeness DESC,
                  CASE WHEN era_start IS NULL THEN 1 ELSE 0 END,
                  era_start ASC
         LIMIT 3
        """,
        (sf,),
    ).fetchall()
    subfields_rep[sf] = [
        {
            "id": r["id"],
            "name_ja": r["name_ja"],
            "name_en": r["name_en"],
            "subfield": r["subfield"],
            "era_start": r["era_start"],
            "era_end": r["era_end"],
            "definition": trunc(r["definition"], 120),
            "school_of_thought": r["school_of_thought"],
            "data_completeness": r["data_completeness"],
        }
        for r in rows
    ]


# ---------- B. Era x Subfield crosstab ----------
def era_bin(era):
    if era is None:
        return "unknown"
    if era < 1900:
        return "pre1900"
    if era < 1960:
        return "y1900_1959"
    if era < 1985:
        return "y1960_1984"
    if era < 2000:
        return "y1985_1999"
    if era < 2015:
        return "y2000_2014"
    return "y2015_plus"


crosstab_counter = defaultdict(lambda: Counter())
for r in cur.execute(
    "SELECT subfield, era_start FROM natural_discovery WHERE subfield IS NOT NULL"
).fetchall():
    crosstab_counter[r["subfield"]][era_bin(r["era_start"])] += 1

era_keys = ["pre1900", "y1900_1959", "y1960_1984", "y1985_1999", "y2000_2014", "y2015_plus", "unknown"]
era_crosstab = []
for sf in subfields:
    row = {"subfield": sf}
    for k in era_keys:
        row[k] = crosstab_counter[sf][k]
    row["total"] = sum(row[k] for k in era_keys)
    era_crosstab.append(row)


# ---------- C. Top researchers (TOP20) ----------
# Only 7 rows exist in natural_discovery_researchers; report all real rows
researcher_rows = cur.execute(
    """
    SELECT r.id, r.name_full, r.name_ja, r.nationality,
           COUNT(DISTINCT ndr.concept_id) AS concept_count
      FROM natural_discovery_researchers ndr
      JOIN researchers r ON r.id = ndr.researcher_id
     GROUP BY r.id, r.name_full
     ORDER BY concept_count DESC, r.name_full ASC
     LIMIT 20
    """
).fetchall()

top_researchers = []
for r in researcher_rows:
    # primary subfield (most frequent across this researcher's concepts)
    sf_rows = cur.execute(
        """
        SELECT nd.subfield, COUNT(*) AS c
          FROM natural_discovery_researchers ndr
          JOIN natural_discovery nd ON nd.id = ndr.concept_id
         WHERE ndr.researcher_id = ?
         GROUP BY nd.subfield
         ORDER BY c DESC
         LIMIT 1
        """,
        (r["id"],),
    ).fetchone()
    top_researchers.append({
        "researcher_id": r["id"],
        "name_full": r["name_full"],
        "name_ja": r["name_ja"],
        "nationality": r["nationality"],
        "concept_count": r["concept_count"],
        "primary_subfield": sf_rows["subfield"] if sf_rows else None,
    })

# Mark sparse-data status explicitly
top_researchers_status = {
    "available_rows": len(top_researchers),
    "requested_top_n": 20,
    "note": "natural_discovery_researchers table contains only 7 distinct researchers; remaining slots are NULL by data availability."
}


# ---------- D. Cross-domain bridges (top 30) ----------
# Bridges where natural_discovery participates with the four other domains.
OTHER_DOMAINS = ("humanities_concept", "social_theory", "engineering_method", "arts_question")

bridge_rows = cur.execute(
    f"""
    SELECT cdr.id, cdr.source_domain, cdr.source_id,
           cdr.target_domain, cdr.target_id,
           cdr.relation_type, cdr.relation_description, cdr.strength
      FROM cross_domain_relations cdr
     WHERE (cdr.source_domain = 'natural_discovery' AND cdr.target_domain IN {OTHER_DOMAINS})
        OR (cdr.target_domain = 'natural_discovery' AND cdr.source_domain IN {OTHER_DOMAINS})
     ORDER BY cdr.strength DESC, cdr.id ASC
     LIMIT 30
    """
).fetchall()


def get_concept_name(domain, cid):
    """Resolve concept name from the relevant domain table."""
    table_map = {
        "natural_discovery": "natural_discovery",
        "humanities_concept": "humanities_concept",
        "social_theory": "social_theory",
        "engineering_method": "engineering_method",
        "arts_question": "arts_question",
    }
    tbl = table_map.get(domain)
    if not tbl:
        return (None, None)
    try:
        row = cur.execute(
            f"SELECT name_ja, name_en FROM {tbl} WHERE id = ?",
            (cid,),
        ).fetchone()
        if row:
            return (row["name_ja"], row["name_en"])
    except sqlite3.OperationalError:
        return (None, None)
    return (None, None)


cross_domain_bridges = []
for r in bridge_rows:
    src_name_ja, src_name_en = get_concept_name(r["source_domain"], r["source_id"])
    dst_name_ja, dst_name_en = get_concept_name(r["target_domain"], r["target_id"])
    cross_domain_bridges.append({
        "id": r["id"],
        "src_domain": r["source_domain"],
        "src_id": r["source_id"],
        "src_name_ja": src_name_ja,
        "src_name_en": src_name_en,
        "dst_domain": r["target_domain"],
        "dst_id": r["target_id"],
        "dst_name_ja": dst_name_ja,
        "dst_name_en": dst_name_en,
        "relation_type": r["relation_type"],
        "relation_description": r["relation_description"],
        "strength": r["strength"],
    })


# ---------- E. Lineage chains (length >= 3) ----------
# Build adjacency: source -> [target] for relation types in (extends, derived_from, builds_on)
LINEAGE_TYPES = ("extends", "derived_from", "builds_on")
edges = cur.execute(
    f"""
    SELECT source_concept_id, target_concept_id, relation_type
      FROM natural_discovery_relations
     WHERE relation_type IN {LINEAGE_TYPES}
    """
).fetchall()

# Verify availability
edge_count_by_type = Counter()
for e in edges:
    edge_count_by_type[e["relation_type"]] += 1

adj = defaultdict(list)
edge_type = {}
for e in edges:
    s = e["source_concept_id"]
    t = e["target_concept_id"]
    adj[s].append(t)
    edge_type[(s, t)] = e["relation_type"]

# Concept lookup
concept_lookup = {}
for r in cur.execute("SELECT id, name_ja, name_en, era_start, subfield FROM natural_discovery").fetchall():
    concept_lookup[r["id"]] = {
        "id": r["id"],
        "name_ja": r["name_ja"],
        "name_en": r["name_en"],
        "era_start": r["era_start"],
        "subfield": r["subfield"],
    }


# DFS for chains; we collect all simple paths of length >=3 (>=3 nodes, i.e., >=2 edges)
# To keep this tractable, cap path length at 6, dedupe by node tuple, and pick max 10 longest.
all_chains = []
visited_chain_keys = set()


def dfs(node, path):
    if len(path) >= 6:
        # record this path if length>=3
        if len(path) >= 3:
            key = tuple(path)
            if key not in visited_chain_keys:
                visited_chain_keys.add(key)
                all_chains.append(list(path))
        return
    extended = False
    for nxt in adj.get(node, []):
        if nxt in path:
            continue
        path.append(nxt)
        dfs(nxt, path)
        path.pop()
        extended = True
    if not extended and len(path) >= 3:
        key = tuple(path)
        if key not in visited_chain_keys:
            visited_chain_keys.add(key)
            all_chains.append(list(path))


# Start DFS from every node that has outgoing edges; cap exploration size
max_starts = 2000
starts = list(adj.keys())[:max_starts]
for s in starts:
    dfs(s, [s])

# Sort by length desc, then by earliest era of first concept ascending
def chain_sort_key(chain):
    eras = [concept_lookup.get(c, {}).get("era_start") for c in chain]
    eras = [e for e in eras if e is not None]
    first_era = min(eras) if eras else 9999
    return (-len(chain), first_era)


all_chains.sort(key=chain_sort_key)

# Pick top 10 maximal chains that don't subsume each other
selected = []
for chain in all_chains:
    if len(selected) >= 10:
        break
    # ensure not a subsequence of an already-selected chain
    chain_set = set(chain)
    subsumed = False
    for sel in selected:
        sel_set = set(sel)
        if chain_set.issubset(sel_set) and len(chain) < len(sel):
            subsumed = True
            break
    if not subsumed:
        selected.append(chain)


lineage_chains = []
for chain in selected:
    nodes_out = []
    for cid in chain:
        c = concept_lookup.get(cid)
        if c:
            nodes_out.append({
                "id": cid,
                "name_ja": c["name_ja"],
                "era_start": c["era_start"],
                "subfield": c["subfield"],
            })
        else:
            nodes_out.append({"id": cid, "name_ja": None, "era_start": None, "subfield": None})
    edges_out = []
    for i in range(len(chain) - 1):
        edges_out.append({
            "from": chain[i],
            "to": chain[i + 1],
            "relation_type": edge_type.get((chain[i], chain[i + 1])),
        })
    lineage_chains.append({
        "length": len(chain),
        "nodes": nodes_out,
        "edges": edges_out,
    })


# ---------- F. Subfield summary stats ----------
subfield_summary = []
for sf in subfields:
    base = cur.execute(
        """
        SELECT COUNT(*) AS total,
               AVG(era_start) AS avg_era_start,
               SUM(CASE WHEN era_start >= 2015 THEN 1 ELSE 0 END) AS recent_count
          FROM natural_discovery
         WHERE subfield = ?
        """,
        (sf,),
    ).fetchone()
    rel_row = cur.execute(
        """
        SELECT COUNT(*) AS c
          FROM natural_discovery_relations ndr
          JOIN natural_discovery a ON a.id = ndr.source_concept_id
          JOIN natural_discovery b ON b.id = ndr.target_concept_id
         WHERE a.subfield = ? OR b.subfield = ?
        """,
        (sf, sf),
    ).fetchone()
    res_row = cur.execute(
        """
        SELECT COUNT(DISTINCT ndr.researcher_id) AS c
          FROM natural_discovery_researchers ndr
          JOIN natural_discovery nd ON nd.id = ndr.concept_id
         WHERE nd.subfield = ?
        """,
        (sf,),
    ).fetchone()
    total = base["total"] or 0
    recent_count = base["recent_count"] or 0
    subfield_summary.append({
        "subfield": sf,
        "concept_count": total,
        "avg_era_start": round(base["avg_era_start"], 1) if base["avg_era_start"] is not None else None,
        "recent_2015_plus_count": recent_count,
        "recent_2015_plus_ratio": round(recent_count / total, 4) if total else None,
        "relation_count": rel_row["c"] or 0,
        "researcher_count": res_row["c"] or 0,
    })


# ---------- Assemble output ----------
data = {
    "generated_at": "2026-05-11",
    "source_db": "academic.db",
    "source_db_path": DB_PATH,
    "domain": "natural_discovery",
    "totals": {
        "concepts": sum(s["concept_count"] for s in subfield_summary),
        "subfields": len(subfields),
        "relations_in_domain": cur.execute("SELECT COUNT(*) c FROM natural_discovery_relations").fetchone()["c"],
        "researcher_rows": cur.execute("SELECT COUNT(*) c FROM natural_discovery_researchers").fetchone()["c"],
        "cross_domain_relations_touching_natural": cur.execute(
            "SELECT COUNT(*) c FROM cross_domain_relations WHERE source_domain='natural_discovery' OR target_domain='natural_discovery'"
        ).fetchone()["c"],
    },
    "subfields_representative": subfields_rep,
    "era_crosstab": era_crosstab,
    "era_crosstab_keys": era_keys,
    "top_researchers": top_researchers if top_researchers else None,
    "top_researchers_status": top_researchers_status,
    "cross_domain_bridges": cross_domain_bridges if cross_domain_bridges else None,
    "lineage_chains": lineage_chains if lineage_chains else None,
    "lineage_chains_diagnostic": {
        "edges_by_type": dict(edge_count_by_type),
        "total_lineage_edges": sum(edge_count_by_type.values()),
        "chains_found_total": len(all_chains),
        "chains_selected": len(lineage_chains),
    },
    "subfield_summary": subfield_summary,
}

Path(OUT_PATH).parent.mkdir(parents=True, exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Wrote {OUT_PATH}")
print(f"File size bytes: {Path(OUT_PATH).stat().st_size}")
print(json.dumps({
    "subfields": len(subfields),
    "subfields_rep_total_items": sum(len(v) for v in subfields_rep.values()),
    "era_crosstab_rows": len(era_crosstab),
    "top_researchers_count": len(top_researchers),
    "cross_domain_bridges_count": len(cross_domain_bridges),
    "lineage_chains_count": len(lineage_chains),
    "subfield_summary_rows": len(subfield_summary),
}, ensure_ascii=False, indent=2))

conn.close()
