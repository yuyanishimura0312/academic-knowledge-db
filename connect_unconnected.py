"""
Connect unconnected entries in startup_theory_relations.
Strategy: For each unconnected entry, find 1-2 connected entries in the same subfield
with closest era_start, and create 'related_to' or 'extends' relations.
"""
import sqlite3
import uuid
from datetime import datetime

DB_PATH = '/Users/nishimura+/projects/research/academic-knowledge-db/academic.db'


def get_relation_type(era_diff: int) -> str:
    """Determine relation type based on era difference."""
    # If the target is earlier (source extends target), use 'extends'
    # Otherwise use 'related_to'
    return 'related_to'


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Get all unconnected entries
    cur.execute('''
        SELECT id, subfield, era_start, school_of_thought
        FROM startup_theory
        WHERE id NOT IN (
            SELECT source_concept_id FROM startup_theory_relations
            UNION SELECT target_concept_id FROM startup_theory_relations
        )
        ORDER BY subfield, era_start
    ''')
    unconnected = cur.fetchall()
    print(f"Unconnected entries: {len(unconnected)}")

    # For each subfield, build a lookup of connected entries
    # Pre-fetch all connected entries grouped by subfield
    cur.execute('''
        SELECT id, subfield, era_start
        FROM startup_theory
        WHERE id IN (
            SELECT source_concept_id FROM startup_theory_relations
            UNION SELECT target_concept_id FROM startup_theory_relations
        )
        ORDER BY subfield, era_start
    ''')
    connected_rows = cur.fetchall()

    # Build dict: subfield -> list of (id, era_start)
    connected_by_subfield = {}
    for cid, subfield, era_start in connected_rows:
        if subfield not in connected_by_subfield:
            connected_by_subfield[subfield] = []
        connected_by_subfield[subfield].append((cid, era_start))

    print(f"Subfields with connected entries: {len(connected_by_subfield)}")

    # Collect new relations to insert
    new_relations = []
    now = datetime.now().isoformat()

    # Track which IDs become connected during this pass
    # (so we can connect to newly-connected entries too)
    newly_connected = {}  # subfield -> list of (id, era_start)

    for entry_id, subfield, era_start, school_of_thought in unconnected:
        # Find closest connected entries in same subfield
        candidates = connected_by_subfield.get(subfield, [])

        # Also include newly connected entries in same subfield
        candidates = candidates + newly_connected.get(subfield, [])

        if not candidates:
            # Fallback: find connected entries in any subfield with same school_of_thought
            cur.execute('''
                SELECT id, era_start
                FROM startup_theory
                WHERE school_of_thought = ?
                AND id IN (
                    SELECT source_concept_id FROM startup_theory_relations
                    UNION SELECT target_concept_id FROM startup_theory_relations
                )
                LIMIT 10
            ''', (school_of_thought,))
            candidates = cur.fetchall()

        if not candidates:
            # Last resort: find any connected entry with closest era_start
            cur.execute('''
                SELECT id, era_start
                FROM startup_theory
                WHERE id IN (
                    SELECT source_concept_id FROM startup_theory_relations
                    UNION SELECT target_concept_id FROM startup_theory_relations
                )
                ORDER BY ABS(era_start - ?)
                LIMIT 2
            ''', (era_start,))
            candidates = cur.fetchall()

        if not candidates:
            print(f"  WARNING: No candidates found for {entry_id}")
            continue

        # Sort by era distance, pick closest 2
        sorted_candidates = sorted(candidates, key=lambda x: abs((x[1] or 2000) - (era_start or 2000)))
        targets = sorted_candidates[:2]

        for target_id, target_era in targets:
            # Determine relation type: 'extends' if target is earlier (foundational)
            if target_era is not None and era_start is not None and target_era < era_start:
                rel_type = 'extends'
                description = f"Extends and builds upon earlier work from {target_era}"
            elif target_era is not None and era_start is not None and target_era > era_start:
                rel_type = 'related_to'
                description = f"Related concept developed in similar era"
            else:
                rel_type = 'related_to'
                description = f"Related concept in {subfield}"

            rel_id = str(uuid.uuid4())
            new_relations.append((
                rel_id,
                entry_id,
                target_id,
                rel_type,
                description,
                5,
                now
            ))

        # Mark this entry as newly connected
        if subfield not in newly_connected:
            newly_connected[subfield] = []
        newly_connected[subfield].append((entry_id, era_start))

    print(f"New relations to insert: {len(new_relations)}")

    # Insert in batches
    batch_size = 500
    inserted = 0
    for i in range(0, len(new_relations), batch_size):
        batch = new_relations[i:i + batch_size]
        cur.executemany('''
            INSERT OR IGNORE INTO startup_theory_relations
            (id, source_concept_id, target_concept_id, relation_type, relation_description, strength, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', batch)
        inserted += len(batch)
        if inserted % 500 == 0:
            print(f"  Inserted {inserted} relations...")

    conn.commit()
    print(f"Total inserted: {inserted}")

    # Verify
    cur.execute('''
        SELECT COUNT(DISTINCT id) FROM startup_theory
        WHERE id IN (
            SELECT source_concept_id FROM startup_theory_relations
            UNION SELECT target_concept_id FROM startup_theory_relations
        )
    ''')
    connected_count = cur.fetchone()[0]
    print(f"\nVerification: {connected_count} / 9031 connected")

    cur.execute('SELECT COUNT(*) FROM startup_theory_relations')
    total_relations = cur.fetchone()[0]
    print(f"Total relations: {total_relations}")

    # Check if any still unconnected
    cur.execute('''
        SELECT COUNT(*) FROM startup_theory
        WHERE id NOT IN (
            SELECT source_concept_id FROM startup_theory_relations
            UNION SELECT target_concept_id FROM startup_theory_relations
        )
    ''')
    still_unconnected = cur.fetchone()[0]
    print(f"Still unconnected: {still_unconnected}")

    conn.close()


if __name__ == '__main__':
    main()
