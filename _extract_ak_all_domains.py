#!/usr/bin/env python3
"""
Extract per-domain materials for ak.html dashboard, for all 5 academic domains:
- humanities_concept, social_theory, natural_discovery, engineering_method, arts_question

Pure SQL extraction. No AI generation. Mirrors the structure used by the
earlier _extract_ak_natural.py.

Output: one JSON file per domain at
  ~/projects/apps/miratuku-news-v2/dashboards/_ak_<domain>_materials.json
"""
import json
import sqlite3
from collections import defaultdict, Counter
from pathlib import Path

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
OUT_DIR = Path("/Users/nishimura+/projects/apps/miratuku-news-v2/dashboards")

DOMAINS = [
    "humanities_concept",
    "social_theory",
    "natural_discovery",
    "engineering_method",
    "arts_question",
]

OTHER_DOMAIN_TUPLE_OF = {
    d: tuple(o for o in DOMAINS if o != d) for d in DOMAINS
}

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()


def trunc(text, n=120):
    if text is None:
        return None
    return str(text)[:n]


def table_cols(table):
    return {r[1] for r in cur.execute(f"PRAGMA table_info({table})").fetchall()}


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


ERA_KEYS = ["pre1900", "y1900_1959", "y1960_1984", "y1985_1999", "y2000_2014", "y2015_plus", "unknown"]
LINEAGE_TYPES = ("extends", "derived_from", "builds_on")


def extract_domain(domain):
    """Extract one domain's materials and return as dict."""
    rel_table = f"{domain}_relations"
    res_table = f"{domain}_researchers"

    has_rel_table = bool(cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (rel_table,)
    ).fetchone())
    has_res_table = bool(cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (res_table,)
    ).fetchone())

    # Some tables have 'school_of_thought', some have different field names. Detect.
    cols = table_cols(domain)
    school_col = "school_of_thought" if "school_of_thought" in cols else None

    # ---------- A. Subfield representative (3 per subfield) ----------
    subfields = [r[0] for r in cur.execute(
        f"SELECT DISTINCT subfield FROM {domain} WHERE subfield IS NOT NULL ORDER BY subfield"
    ).fetchall()]

    subfields_rep = {}
    for sf in subfields:
        rows = cur.execute(
            f"""
            SELECT id, name_ja, name_en, subfield, era_start, era_end,
                   definition,
                   {school_col + ' AS school_of_thought,' if school_col else "NULL AS school_of_thought,"}
                   data_completeness
              FROM {domain}
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

    # ---------- B. Era × Subfield crosstab ----------
    crosstab_counter = defaultdict(lambda: Counter())
    for r in cur.execute(f"SELECT subfield, era_start FROM {domain} WHERE subfield IS NOT NULL").fetchall():
        crosstab_counter[r["subfield"]][era_bin(r["era_start"])] += 1
    era_crosstab = []
    for sf in subfields:
        row = {"subfield": sf}
        for k in ERA_KEYS:
            row[k] = crosstab_counter[sf][k]
        row["total"] = sum(row[k] for k in ERA_KEYS)
        era_crosstab.append(row)

    # ---------- C. Top researchers ----------
    top_researchers = []
    researcher_rows_count = 0
    if has_res_table:
        researcher_rows_count = cur.execute(f"SELECT COUNT(*) c FROM {res_table}").fetchone()["c"]
        # Schema for researchers_link may differ (concept_id vs source_id)
        res_cols = table_cols(res_table)
        concept_fk = "concept_id" if "concept_id" in res_cols else (
            "source_concept_id" if "source_concept_id" in res_cols else None
        )
        if concept_fk:
            researcher_link_rows = cur.execute(
                f"""
                SELECT r.id AS rid, r.name_full, r.name_ja, r.nationality,
                       COUNT(DISTINCT lnk.{concept_fk}) AS concept_count
                  FROM {res_table} lnk
                  JOIN researchers r ON r.id = lnk.researcher_id
                 GROUP BY r.id, r.name_full, r.name_ja, r.nationality
                 ORDER BY concept_count DESC, r.name_full ASC
                 LIMIT 20
                """
            ).fetchall()
            for r in researcher_link_rows:
                # primary subfield
                sf_row = cur.execute(
                    f"""
                    SELECT t.subfield, COUNT(*) AS c
                      FROM {res_table} lnk
                      JOIN {domain} t ON t.id = lnk.{concept_fk}
                     WHERE lnk.researcher_id = ?
                     GROUP BY t.subfield
                     ORDER BY c DESC
                     LIMIT 1
                    """,
                    (r["rid"],),
                ).fetchone()
                top_researchers.append({
                    "researcher_id": r["rid"],
                    "name_full": r["name_full"],
                    "name_ja": r["name_ja"],
                    "nationality": r["nationality"],
                    "concept_count": r["concept_count"],
                    "primary_subfield": sf_row["subfield"] if sf_row else None,
                })
    top_researchers_status = {
        "available_rows": len(top_researchers),
        "requested_top_n": 20,
        "raw_link_rows": researcher_rows_count,
        "note": (
            f"{res_table} has {researcher_rows_count} link rows; "
            f"{len(top_researchers)} distinct researchers surfaced."
        ),
    }

    # ---------- D. Cross-domain bridges (TOP 30 by strength) ----------
    others = OTHER_DOMAIN_TUPLE_OF[domain]
    placeholders = ",".join(["?"] * len(others))
    bridge_rows = cur.execute(
        f"""
        SELECT cdr.id, cdr.source_domain, cdr.source_id,
               cdr.target_domain, cdr.target_id,
               cdr.relation_type, cdr.relation_description, cdr.strength
          FROM cross_domain_relations cdr
         WHERE (cdr.source_domain = ? AND cdr.target_domain IN ({placeholders}))
            OR (cdr.target_domain = ? AND cdr.source_domain IN ({placeholders}))
         ORDER BY cdr.strength DESC, cdr.id ASC
         LIMIT 30
        """,
        (domain, *others, domain, *others),
    ).fetchall()

    def get_concept_name(d, cid):
        if d not in DOMAINS:
            return (None, None)
        try:
            row = cur.execute(f"SELECT name_ja, name_en FROM {d} WHERE id = ?", (cid,)).fetchone()
            if row:
                return (row["name_ja"], row["name_en"])
        except sqlite3.OperationalError:
            pass
        return (None, None)

    cross_bridges = []
    for r in bridge_rows:
        sj, se = get_concept_name(r["source_domain"], r["source_id"])
        tj, te = get_concept_name(r["target_domain"], r["target_id"])
        cross_bridges.append({
            "id": r["id"],
            "src_domain": r["source_domain"],
            "src_id": r["source_id"],
            "src_name_ja": sj,
            "src_name_en": se,
            "dst_domain": r["target_domain"],
            "dst_id": r["target_id"],
            "dst_name_ja": tj,
            "dst_name_en": te,
            "relation_type": r["relation_type"],
            "relation_description": r["relation_description"],
            "strength": r["strength"],
        })

    # ---------- E. Lineage chains ----------
    edge_count_by_type = Counter()
    lineage_chains = []
    if has_rel_table:
        rel_cols = table_cols(rel_table)
        src_col = "source_concept_id" if "source_concept_id" in rel_cols else ("source_id" if "source_id" in rel_cols else None)
        tgt_col = "target_concept_id" if "target_concept_id" in rel_cols else ("target_id" if "target_id" in rel_cols else None)
        if src_col and tgt_col:
            edges = cur.execute(
                f"""
                SELECT {src_col} AS s, {tgt_col} AS t, relation_type
                  FROM {rel_table}
                 WHERE relation_type IN {LINEAGE_TYPES}
                """
            ).fetchall()
            for e in edges:
                edge_count_by_type[e["relation_type"]] += 1
            adj = defaultdict(list)
            edge_type = {}
            for e in edges:
                adj[e["s"]].append(e["t"])
                edge_type[(e["s"], e["t"])] = e["relation_type"]

            concept_lookup = {}
            for r in cur.execute(f"SELECT id, name_ja, name_en, era_start, subfield FROM {domain}").fetchall():
                concept_lookup[r["id"]] = {
                    "id": r["id"],
                    "name_ja": r["name_ja"],
                    "name_en": r["name_en"],
                    "era_start": r["era_start"],
                    "subfield": r["subfield"],
                }

            all_chains = []
            visited = set()

            def dfs(node, path):
                if len(path) >= 6:
                    if len(path) >= 3:
                        k = tuple(path)
                        if k not in visited:
                            visited.add(k)
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
                    k = tuple(path)
                    if k not in visited:
                        visited.add(k)
                        all_chains.append(list(path))

            for s in list(adj.keys())[:2000]:
                dfs(s, [s])

            def sort_key(chain):
                eras = [concept_lookup.get(c, {}).get("era_start") for c in chain]
                eras = [e for e in eras if e is not None]
                first = min(eras) if eras else 9999
                return (-len(chain), first)

            all_chains.sort(key=sort_key)
            selected = []
            for chain in all_chains:
                if len(selected) >= 10:
                    break
                cs = set(chain)
                if any(cs.issubset(set(sel)) and len(chain) < len(sel) for sel in selected):
                    continue
                selected.append(chain)

            for chain in selected:
                nodes_out = [
                    {
                        "id": cid,
                        "name_ja": (concept_lookup.get(cid) or {}).get("name_ja"),
                        "era_start": (concept_lookup.get(cid) or {}).get("era_start"),
                        "subfield": (concept_lookup.get(cid) or {}).get("subfield"),
                    }
                    for cid in chain
                ]
                edges_out = [
                    {"from": chain[i], "to": chain[i+1], "relation_type": edge_type.get((chain[i], chain[i+1]))}
                    for i in range(len(chain)-1)
                ]
                lineage_chains.append({"length": len(chain), "nodes": nodes_out, "edges": edges_out})

    # ---------- F. Subfield summary ----------
    subfield_summary = []
    for sf in subfields:
        base = cur.execute(
            f"""
            SELECT COUNT(*) AS total,
                   AVG(era_start) AS avg_era_start,
                   SUM(CASE WHEN era_start >= 2015 THEN 1 ELSE 0 END) AS recent_count
              FROM {domain}
             WHERE subfield = ?
            """,
            (sf,),
        ).fetchone()
        rel_count = 0
        res_count = 0
        if has_rel_table:
            rel_cols = table_cols(rel_table)
            src_col = "source_concept_id" if "source_concept_id" in rel_cols else "source_id"
            tgt_col = "target_concept_id" if "target_concept_id" in rel_cols else "target_id"
            try:
                rel_row = cur.execute(
                    f"""
                    SELECT COUNT(*) AS c
                      FROM {rel_table} rt
                      JOIN {domain} a ON a.id = rt.{src_col}
                      JOIN {domain} b ON b.id = rt.{tgt_col}
                     WHERE a.subfield = ? OR b.subfield = ?
                    """,
                    (sf, sf),
                ).fetchone()
                rel_count = rel_row["c"] or 0
            except sqlite3.OperationalError:
                rel_count = 0
        if has_res_table:
            res_cols = table_cols(res_table)
            concept_fk = "concept_id" if "concept_id" in res_cols else "source_concept_id"
            try:
                res_row = cur.execute(
                    f"""
                    SELECT COUNT(DISTINCT lnk.researcher_id) AS c
                      FROM {res_table} lnk
                      JOIN {domain} t ON t.id = lnk.{concept_fk}
                     WHERE t.subfield = ?
                    """,
                    (sf,),
                ).fetchone()
                res_count = res_row["c"] or 0
            except sqlite3.OperationalError:
                res_count = 0
        total = base["total"] or 0
        recent = base["recent_count"] or 0
        subfield_summary.append({
            "subfield": sf,
            "concept_count": total,
            "avg_era_start": round(base["avg_era_start"], 1) if base["avg_era_start"] is not None else None,
            "recent_2015_plus_count": recent,
            "recent_2015_plus_ratio": round(recent / total, 4) if total else None,
            "relation_count": rel_count,
            "researcher_count": res_count,
        })

    # Totals
    totals = {
        "concepts": sum(s["concept_count"] for s in subfield_summary),
        "subfields": len(subfields),
        "relations_in_domain": cur.execute(f"SELECT COUNT(*) c FROM {rel_table}").fetchone()["c"] if has_rel_table else 0,
        "researcher_rows": researcher_rows_count,
        "cross_domain_relations_touching": cur.execute(
            "SELECT COUNT(*) c FROM cross_domain_relations WHERE source_domain=? OR target_domain=?",
            (domain, domain),
        ).fetchone()["c"],
    }

    return {
        "generated_at": "2026-05-11",
        "source_db": "academic.db",
        "source_db_path": DB_PATH,
        "domain": domain,
        "totals": totals,
        "subfields_representative": subfields_rep,
        "era_crosstab": era_crosstab,
        "era_crosstab_keys": ERA_KEYS,
        "top_researchers": top_researchers if top_researchers else None,
        "top_researchers_status": top_researchers_status,
        "cross_domain_bridges": cross_bridges if cross_bridges else None,
        "lineage_chains": lineage_chains if lineage_chains else None,
        "lineage_chains_diagnostic": {
            "edges_by_type": dict(edge_count_by_type),
            "total_lineage_edges": sum(edge_count_by_type.values()),
            "chains_selected": len(lineage_chains),
        },
        "subfield_summary": subfield_summary,
    }


def main():
    for d in DOMAINS:
        data = extract_domain(d)
        out_path = OUT_DIR / f"_ak_{d}_materials.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(
            f"{d:>22} -> {out_path.name}: "
            f"concepts={data['totals']['concepts']} "
            f"subfields={data['totals']['subfields']} "
            f"bridges={len(data['cross_domain_bridges'] or [])} "
            f"chains={len(data['lineage_chains'] or [])} "
            f"researchers={len(data['top_researchers'] or [])}"
        )


if __name__ == "__main__":
    main()
    conn.close()
