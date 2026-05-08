#!/usr/bin/env python3
"""GTA (Grounded Theory Approach) analysis of the Poetics DB.

Three-stage GTA:
1. Open coding — emergent themes from concept names/definitions/relations
2. Axial coding — causal-conditional paradigms (conditions/strategies/consequences)
3. Selective coding — core categories integrating the theory

Outputs:
- /tmp/gta_communities.json (network community detection)
- /tmp/gta_open_codes.json (theme clustering)
- /tmp/gta_axial_paradigms.json (axial coding structures)
- /tmp/gta_selective_categories.json (core categories)
"""
import sqlite3
import json
import re
from pathlib import Path
from collections import defaultdict, Counter

import networkx as nx
from community import community_louvain

DB_PATH = Path(__file__).parent.parent / "academic.db"
OUT_DIR = Path("/tmp/gta_poetics")
OUT_DIR.mkdir(exist_ok=True)


POETICS_SUBFIELDS_ARTS = ('文学理論・物語論','視覚芸術論・美術史','音楽学','建築・空間芸術論',
    'デザイン理論','映画・映像論','メディアアート・デジタル芸術','舞台芸術論',
    '美学・芸術哲学','文化批評・芸術社会学','キュレーション・展示論','ゲーム・インタラクティブアート')


def load_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    placeholders = ",".join("?" * len(POETICS_SUBFIELDS_ARTS))
    cur.execute(f"""SELECT id, name_ja, name_en, name_original, definition,
                          impact_summary, subfield, school_of_thought, era_start
                   FROM arts_question WHERE subfield IN ({placeholders})""", POETICS_SUBFIELDS_ARTS)
    concepts = {r[0]: {
        "id": r[0], "name": r[1] or "", "name_en": r[2] or "",
        "name_orig": r[3] or "", "definition": r[4] or "",
        "impact": r[5] or "", "subfield": r[6] or "",
        "school": r[7] or "", "era": r[8]
    } for r in cur.fetchall()}

    cur.execute("""SELECT source_concept_id, target_concept_id, relation_type, strength
                   FROM arts_question_relations""")
    relations = [(r[0], r[1], r[2], r[3] or 5) for r in cur.fetchall()
                 if r[0] in concepts and r[1] in concepts]

    # Quotes were attached to old cp_ ids; we map them by name match where possible
    cur.execute("""SELECT concept_id, source_author, source_work_title,
                          source_year, quote_significance
                   FROM concept_original_source""")
    quotes_raw = list(cur.fetchall())
    quotes = defaultdict(list)
    # Quote concepts are orphan after migration; we'll skip exact match
    # For analysis purposes, treat orphan quotes as legacy data
    for r in quotes_raw:
        if r[0] in concepts:
            quotes[r[0]].append({"author": r[1], "work": r[2], "year": r[3], "sig": r[4] or ""})

    cur.execute("""SELECT ctst.concept_id, pt.title_ja, pt.culture_region, pt.era_year
                   FROM concept_text_source_triple ctst
                   JOIN poetics_text pt ON ctst.text_id = pt.id""")
    triples = defaultdict(list)
    for r in cur.fetchall():
        if r[0] in concepts:
            triples[r[0]].append({"title": r[1], "culture": r[2], "year": r[3]})

    conn.close()
    return concepts, relations, quotes, triples


def stage1_open_coding(concepts, relations):
    """Open coding via Louvain community detection on relation network."""
    G = nx.Graph()
    for cid, c in concepts.items():
        G.add_node(cid, name=c["name"], subfield=c["subfield"], era=c["era"] or 0)
    for s, t, rt, w in relations:
        if G.has_edge(s, t):
            G[s][t]['weight'] += w
        else:
            G.add_edge(s, t, weight=w, rel_type=rt)

    print(f"Network: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    # Louvain detection
    partition = community_louvain.best_partition(G, random_state=42, weight='weight')
    communities = defaultdict(list)
    for cid, comm_id in partition.items():
        communities[comm_id].append(cid)

    # Sort by size
    comm_list = sorted(communities.items(), key=lambda x: -len(x[1]))

    print(f"\nDetected {len(comm_list)} communities")
    print(f"Sizes: top 10 = {[len(c[1]) for c in comm_list[:10]]}")

    # For each large community, extract themes
    open_codes = []
    for cid_comm, members in comm_list:
        if len(members) < 5:
            continue
        # Top concepts by degree within community
        sub = G.subgraph(members)
        degree = dict(sub.degree(weight='weight'))
        top = sorted(members, key=lambda x: -degree.get(x, 0))[:8]
        # Subfield distribution
        sf_counter = Counter(concepts[m]["subfield"] for m in members)
        # Era distribution
        eras = [concepts[m]["era"] for m in members if concepts[m]["era"]]
        era_avg = sum(eras) / len(eras) if eras else None
        # Author distribution from quotes - skipped here; use schools
        schools = Counter(concepts[m]["school"] for m in members if concepts[m]["school"])
        open_codes.append({
            "community_id": cid_comm,
            "size": len(members),
            "top_concepts": [(m, concepts[m]["name"]) for m in top],
            "subfield_dist": dict(sf_counter.most_common(5)),
            "era_avg": int(era_avg) if era_avg else None,
            "top_schools": dict(schools.most_common(5))
        })
    return open_codes, partition, G


def stage2_axial_coding(concepts, relations, open_codes, partition, G):
    """Axial coding: for each major community, identify the paradigm
    (conditions/strategies/consequences) using relation types."""
    # Group relations by community
    paradigms = []
    for code in open_codes[:20]:
        comm_id = code["community_id"]
        members = [m for m, c in partition.items() if c == comm_id]
        member_set = set(members)
        # Internal relations
        internal_rels = [(s, t, rt) for s, t, rt, w in relations if s in member_set and t in member_set]
        # External relations (community → outside)
        outgoing = [(s, t, rt) for s, t, rt, w in relations if s in member_set and t not in member_set]
        incoming = [(s, t, rt) for s, t, rt, w in relations if t in member_set and s not in member_set]

        rel_internal = Counter(rt for _, _, rt in internal_rels)
        rel_out = Counter(rt for _, _, rt in outgoing)
        rel_in = Counter(rt for _, _, rt in incoming)

        # Identify conditions (incoming derived_from), strategies (internal extends/synthesizes), consequences (outgoing enables)
        conditions = [(s, concepts[s]["name"]) for s, t, rt in incoming if rt in ("derived_from", "precursor_of")][:8]
        strategies_internal = [(s, t, rt) for s, t, rt in internal_rels if rt in ("extends", "synthesizes", "complements", "reinterprets")][:8]
        consequences = [(t, concepts[t]["name"]) for s, t, rt in outgoing if rt in ("enables", "applies_to")][:8]

        paradigms.append({
            "community_id": comm_id,
            "size": code["size"],
            "top_concepts": code["top_concepts"][:5],
            "subfield_dominant": list(code["subfield_dist"].items())[:1][0][0] if code["subfield_dist"] else None,
            "era_avg": code["era_avg"],
            "rel_internal": dict(rel_internal),
            "rel_outgoing": dict(rel_out),
            "rel_incoming": dict(rel_in),
            "conditions_examples": conditions,
            "strategies_examples": [(concepts[s]["name"], concepts[t]["name"], rt) for s, t, rt in strategies_internal],
            "consequences_examples": consequences
        })
    return paradigms


def stage3_selective_coding(concepts, relations, paradigms, G, quotes, triples):
    """Selective coding: identify core categories integrating paradigms."""
    # Use betweenness centrality to find concepts that bridge multiple communities
    print("Computing betweenness centrality (this may take a moment)...")
    betweenness = nx.betweenness_centrality(G, k=200, weight='weight', seed=42)
    top_bridges = sorted(betweenness.items(), key=lambda x: -x[1])[:30]

    # Concepts with most quotes (well-grounded) - quotes are mostly orphan
    quote_counts = Counter({cid: len(qs) for cid, qs in quotes.items()})
    top_quoted = quote_counts.most_common(20)

    # Concepts with most triples
    triple_counts = Counter({cid: len(ts) for cid, ts in triples.items()})
    top_tripled = triple_counts.most_common(20)

    # Degree centrality (alternative to betweenness for ranking)
    degree_cent = nx.degree_centrality(G)

    # Core categories: bridging + degree + well-grounded
    core_scores = {}
    for cid in concepts:
        b = betweenness.get(cid, 0) * 1000  # scale
        d = degree_cent.get(cid, 0) * 100
        q = len(quotes.get(cid, [])) * 0.3
        t = min(len(triples.get(cid, [])), 50) * 0.5  # cap to avoid skew
        core_scores[cid] = b + d + q + t

    core_categories = sorted(core_scores.items(), key=lambda x: -x[1])[:30]

    # For each core category, build the integrated description
    integrated = []
    for cid, score in core_categories:
        c = concepts[cid]
        comm_id = nx.get_node_attributes(G, 'community')  # not set; skip
        integrated.append({
            "id": cid,
            "name": c["name"],
            "name_en": c["name_en"],
            "subfield": c["subfield"],
            "era": c["era"],
            "score": round(score, 3),
            "betweenness": round(betweenness.get(cid, 0) * 1000, 3),
            "quote_count": len(quotes.get(cid, [])),
            "triple_count": len(triples.get(cid, [])),
            "definition_short": (c["definition"] or "")[:200]
        })

    return {
        "top_bridges": [{"id": cid, "name": concepts[cid]["name"], "subfield": concepts[cid]["subfield"], "betweenness": round(b * 1000, 3)} for cid, b in top_bridges],
        "top_quoted": [{"id": cid, "name": concepts[cid]["name"], "n_quotes": n} for cid, n in top_quoted],
        "top_tripled": [{"id": cid, "name": concepts[cid]["name"], "n_triples": n} for cid, n in top_tripled],
        "core_categories": integrated
    }


def main():
    print("=== GTA Analysis: Poetics DB v2.4 ===\n")
    concepts, relations, quotes, triples = load_data()
    print(f"Loaded: {len(concepts)} concepts, {len(relations)} relations, "
          f"{sum(len(qs) for qs in quotes.values())} quotes, "
          f"{sum(len(ts) for ts in triples.values())} triples\n")

    print("--- Stage 1: Open Coding (Louvain communities) ---")
    open_codes, partition, G = stage1_open_coding(concepts, relations)
    (OUT_DIR / "gta_open_codes.json").write_text(
        json.dumps(open_codes, ensure_ascii=False, indent=2))
    print(f"Saved {len(open_codes)} community codes")

    print("\n--- Stage 2: Axial Coding (paradigms) ---")
    paradigms = stage2_axial_coding(concepts, relations, open_codes, partition, G)
    (OUT_DIR / "gta_axial_paradigms.json").write_text(
        json.dumps(paradigms, ensure_ascii=False, indent=2))
    print(f"Saved {len(paradigms)} paradigm structures")

    print("\n--- Stage 3: Selective Coding (core categories) ---")
    selective = stage3_selective_coding(concepts, relations, paradigms, G, quotes, triples)
    (OUT_DIR / "gta_selective_categories.json").write_text(
        json.dumps(selective, ensure_ascii=False, indent=2))
    print(f"Saved {len(selective['core_categories'])} core categories")

    print("\n=== Top 5 Communities (Open Codes) ===")
    for c in open_codes[:5]:
        print(f"\nC{c['community_id']} (size={c['size']}, era~{c['era_avg']}):")
        print(f"  Top: {[n for _, n in c['top_concepts'][:5]]}")
        print(f"  Subfield: {list(c['subfield_dist'].items())[:2]}")

    print("\n=== Top 10 Core Categories (Selective Coding) ===")
    for cc in selective['core_categories'][:10]:
        print(f"  {cc['name']} ({cc['subfield']}) - score={cc['score']}, "
              f"betw={cc['betweenness']}, quotes={cc['quote_count']}, "
              f"triples={cc['triple_count']}")


if __name__ == "__main__":
    main()
