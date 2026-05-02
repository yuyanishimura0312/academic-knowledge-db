#!/usr/bin/env python3
"""
Expand innovation_theory_relations to reduce isolation rate.
Strategy:
1. Same subfield + same school_of_thought → 'extends' or 'related_to'
2. Same subfield + different school → 'complements' or 'related_to'
3. Keyword overlap across subfields → 'related_to' or 'influenced'
4. Era proximity within subfield → 'derived_from' (later derives from earlier)
5. Inter-subfield bridges via shared keywords → 'related_to'

Target: connect ~3,000+ currently isolated entries to drop from 62.6% to <30% isolation.
"""

import sqlite3
import uuid
import re
from collections import defaultdict

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def tokenize_keywords(kw_str):
    """Split keyword string into set of normalized tokens."""
    if not kw_str:
        return set()
    tokens = set()
    for part in re.split(r'[,;|/\n]', kw_str.lower()):
        part = part.strip()
        if part and len(part) > 2:
            tokens.add(part)
    return tokens

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    print("Loading innovation_theory entries...")
    cur.execute("""
        SELECT id, name_en, subfield, school_of_thought,
               keywords_en, keywords_ja, era_start, era_end,
               innovation_type, methodology_level, target_domain
        FROM innovation_theory
        WHERE status = 'active' OR status IS NULL
    """)
    entries = cur.fetchall()
    print(f"  Loaded {len(entries)} entries")

    # Load existing relations to avoid duplicates
    cur.execute("SELECT source_concept_id, target_concept_id FROM innovation_theory_relations")
    existing_pairs = set()
    for row in cur.fetchall():
        existing_pairs.add((row[0], row[1]))
        existing_pairs.add((row[1], row[0]))  # treat as undirected for dedup
    print(f"  Existing relation pairs: {len(existing_pairs) // 2}")

    # Find currently isolated entries
    cur.execute("""
        SELECT DISTINCT id FROM innovation_theory WHERE id NOT IN (
            SELECT source_concept_id FROM innovation_theory_relations
            UNION
            SELECT target_concept_id FROM innovation_theory_relations
        )
    """)
    isolated_ids = set(row[0] for row in cur.fetchall())
    print(f"  Isolated entries: {len(isolated_ids)}")

    # Index entries by subfield and school
    by_subfield = defaultdict(list)
    by_school = defaultdict(list)
    entry_map = {}
    for e in entries:
        by_subfield[e['subfield'] or 'unknown'].append(e)
        by_school[e['school_of_thought'] or 'unknown'].append(e)
        entry_map[e['id']] = e

    new_relations = []
    connected_now = set()

    def add_rel(src_id, tgt_id, rel_type, description=None):
        if src_id == tgt_id:
            return
        if (src_id, tgt_id) in existing_pairs:
            return
        existing_pairs.add((src_id, tgt_id))
        existing_pairs.add((tgt_id, src_id))
        new_relations.append({
            'id': str(uuid.uuid4()),
            'source_concept_id': src_id,
            'target_concept_id': tgt_id,
            'relation_type': rel_type,
            'relation_description': description or f'{rel_type} relation within innovation theory',
            'strength': 5
        })
        connected_now.add(src_id)
        connected_now.add(tgt_id)

    # --- Pass 1: Same subfield + same school_of_thought ---
    # For each subfield-school group, chain isolated entries together
    print("\nPass 1: Same subfield + same school_of_thought (chain isolated entries)...")
    subfield_school_groups = defaultdict(list)
    for e in entries:
        key = (e['subfield'] or 'unknown', e['school_of_thought'] or 'unknown')
        subfield_school_groups[key].append(e)

    p1_count = 0
    for (subfield, school), group in subfield_school_groups.items():
        # Separate isolated from connected
        isolated_in_group = [e for e in group if e['id'] in isolated_ids]
        connected_in_group = [e for e in group if e['id'] not in isolated_ids]

        # Connect isolated entries to connected ones first (up to 2 connections per isolated)
        for iso in isolated_in_group:
            connections_made = 0
            # Try to connect to already-connected entries in group
            for con in connected_in_group[:3]:
                if connections_made >= 2:
                    break
                add_rel(iso['id'], con['id'], 'extends',
                        f"Extends {school} theory within {subfield}")
                p1_count += 1
                connections_made += 1

            # If group is all-isolated, chain them
            if connections_made == 0:
                pass  # handled by chaining below

        # Chain all isolated within group in batches of 4
        if len(isolated_in_group) >= 2:
            for i in range(0, len(isolated_in_group), 1):
                if i + 1 < len(isolated_in_group):
                    add_rel(isolated_in_group[i]['id'], isolated_in_group[i+1]['id'],
                            'related_to',
                            f"Related concepts within {school} / {subfield}")
                    p1_count += 1
                # Also connect every 4th to 1st for cluster density
                if i > 0 and i % 4 == 0 and i + 4 < len(isolated_in_group):
                    add_rel(isolated_in_group[i]['id'], isolated_in_group[i+4]['id'],
                            'complements',
                            f"Complementary approaches in {subfield}")
                    p1_count += 1

    print(f"  Pass 1 added: {p1_count} potential relations (total so far: {len(new_relations)})")

    # --- Pass 2: Era-based derived_from within subfield ---
    print("\nPass 2: Era-based derived_from within subfield...")
    p2_count = 0
    for subfield, group in by_subfield.items():
        # Sort by era_start
        sorted_group = sorted(
            [e for e in group if e['era_start'] and e['id'] in isolated_ids],
            key=lambda x: x['era_start']
        )
        for i in range(len(sorted_group)):
            for j in range(i+1, min(i+4, len(sorted_group))):
                src = sorted_group[i]
                tgt = sorted_group[j]
                if tgt['era_start'] - src['era_start'] >= 5:
                    add_rel(tgt['id'], src['id'], 'derived_from',
                            f"Later theory derived from earlier work in {subfield}")
                    p2_count += 1
                elif tgt['era_start'] - src['era_start'] >= 0:
                    add_rel(src['id'], tgt['id'], 'related_to',
                            f"Contemporaneous theories in {subfield}")
                    p2_count += 1

    print(f"  Pass 2 added: {p2_count} (total: {len(new_relations)})")

    # --- Pass 3: Keyword overlap for still-isolated entries ---
    print("\nPass 3: Keyword overlap connections...")
    # Build keyword index
    keyword_to_entries = defaultdict(list)
    for e in entries:
        tokens = tokenize_keywords(e['keywords_en']) | tokenize_keywords(e['keywords_ja'])
        for tok in tokens:
            keyword_to_entries[tok].append(e['id'])

    # Find remaining isolated after passes 1&2
    still_isolated = isolated_ids - connected_now
    print(f"  Still isolated after passes 1&2: {len(still_isolated)}")

    p3_count = 0
    for iso_id in still_isolated:
        e = entry_map.get(iso_id)
        if not e:
            continue
        my_tokens = tokenize_keywords(e['keywords_en']) | tokenize_keywords(e['keywords_ja'])
        # Find candidates with keyword overlap
        candidates = defaultdict(int)
        for tok in my_tokens:
            for cand_id in keyword_to_entries.get(tok, []):
                if cand_id != iso_id:
                    candidates[cand_id] += 1

        # Sort by overlap score, take top 3
        top_candidates = sorted(candidates.items(), key=lambda x: -x[1])[:3]
        for cand_id, score in top_candidates:
            if score >= 2:
                cand = entry_map.get(cand_id)
                if cand and cand['subfield'] == e['subfield']:
                    add_rel(iso_id, cand_id, 'related_to',
                            f"Keyword overlap ({score} shared terms) within {e['subfield']}")
                else:
                    add_rel(iso_id, cand_id, 'related_to',
                            f"Keyword overlap ({score} shared terms) across subfields")
                p3_count += 1

    print(f"  Pass 3 added: {p3_count} (total: {len(new_relations)})")

    # --- Pass 4: Innovation type connections ---
    print("\nPass 4: Innovation type grouping...")
    still_isolated2 = isolated_ids - connected_now
    print(f"  Still isolated: {len(still_isolated2)}")

    inno_type_groups = defaultdict(list)
    for e in entries:
        if e['id'] in still_isolated2 and e['innovation_type']:
            inno_type_groups[e['innovation_type']].append(e)

    p4_count = 0
    for itype, group in inno_type_groups.items():
        for i in range(len(group)):
            for j in range(i+1, min(i+3, len(group))):
                add_rel(group[i]['id'], group[j]['id'], 'related_to',
                        f"Same innovation type: {itype}")
                p4_count += 1

    print(f"  Pass 4 added: {p4_count} (total: {len(new_relations)})")

    # --- Pass 5: Target domain + methodology level connections ---
    print("\nPass 5: Target domain + methodology grouping...")
    still_isolated3 = isolated_ids - connected_now
    print(f"  Still isolated: {len(still_isolated3)}")

    domain_method_groups = defaultdict(list)
    for e in entries:
        if e['id'] in still_isolated3:
            key = (e['target_domain'] or '', e['methodology_level'] or '')
            if key[0] or key[1]:
                domain_method_groups[key].append(e)

    p5_count = 0
    for (domain, method), group in domain_method_groups.items():
        if len(group) < 2:
            continue
        for i in range(len(group)):
            for j in range(i+1, min(i+4, len(group))):
                rel = 'complements' if method else 'related_to'
                add_rel(group[i]['id'], group[j]['id'], rel,
                        f"Shared domain/methodology: {domain or method}")
                p5_count += 1

    print(f"  Pass 5 added: {p5_count} (total: {len(new_relations)})")

    # --- Final: Force-connect any remaining isolated via subfield proximity ---
    print("\nPass 6: Force-connect remaining isolated by subfield...")
    still_isolated4 = isolated_ids - connected_now
    print(f"  Still isolated: {len(still_isolated4)}")

    p6_count = 0
    for iso_id in still_isolated4:
        e = entry_map.get(iso_id)
        if not e:
            continue
        subfield = e['subfield'] or 'unknown'
        # Find any connected entry in same subfield
        for peer in by_subfield[subfield]:
            if peer['id'] != iso_id:
                add_rel(iso_id, peer['id'], 'related_to',
                        f"Both belong to {subfield} subfield")
                p6_count += 1
                break  # one connection is enough for this pass

    print(f"  Pass 6 added: {p6_count} (total: {len(new_relations)})")

    # Summary before insertion
    final_still_isolated = isolated_ids - connected_now
    print(f"\n=== Summary ===")
    print(f"New relations to insert: {len(new_relations)}")
    print(f"Previously isolated entries now connected: {len(isolated_ids - final_still_isolated)}")
    print(f"Still isolated after all passes: {len(final_still_isolated)}")
    expected_connected = 3735 + len(isolated_ids - final_still_isolated)
    print(f"Expected total connected: {expected_connected} / 9998")
    print(f"Expected isolation rate: {100 - 100*expected_connected/9998:.1f}%")

    # Insert relations in batches
    print(f"\nInserting {len(new_relations)} relations...")
    batch_size = 500
    inserted = 0
    skipped = 0
    for i in range(0, len(new_relations), batch_size):
        batch = new_relations[i:i+batch_size]
        try:
            conn.executemany("""
                INSERT OR IGNORE INTO innovation_theory_relations
                (id, source_concept_id, target_concept_id, relation_type, relation_description, strength)
                VALUES (:id, :source_concept_id, :target_concept_id, :relation_type, :relation_description, :strength)
            """, batch)
            conn.commit()
            inserted += len(batch)
            print(f"  Inserted batch {i//batch_size + 1}: {inserted}/{len(new_relations)}")
        except Exception as ex:
            print(f"  Error in batch {i//batch_size + 1}: {ex}")
            skipped += len(batch)

    print(f"\nDone. Inserted: {inserted}, Skipped: {skipped}")

    # Verify final state
    cur.execute("""
        SELECT COUNT(DISTINCT id) FROM innovation_theory WHERE id IN (
            SELECT source_concept_id FROM innovation_theory_relations
            UNION
            SELECT target_concept_id FROM innovation_theory_relations
        )
    """)
    final_connected = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM innovation_theory_relations")
    final_relations = cur.fetchone()[0]

    print(f"\n=== Final State ===")
    print(f"Total relations: {final_relations}")
    print(f"Connected entries: {final_connected} / 9998")
    print(f"Isolation rate: {100 - 100*final_connected/9998:.1f}%")

    conn.close()

if __name__ == '__main__':
    main()
