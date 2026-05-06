#!/usr/bin/env python3
"""Import Phase 3 poetics deep-dive collection into academic.db.

Files: E (medieval+comparative), F (cognitive+reception),
       G (digital+rhetoric — non-standard schema),
       H (structuralist+modern+phenomenology — non-standard schema)

Normalizes heterogeneous JSON schemas from different agents before import.
"""

import json
import sqlite3
import uuid
from pathlib import Path

DB_PATH = Path(__file__).parent / "academic.db"
COLLECT_DIR = Path("/tmp/poetics_collect_p3")
FILES = [
    "E_medieval_comparative_deep.json",
    "F_cognitive_reception_deep.json",
    "G_digital_rhetoric_deep.json",
    "H_structuralist_modern_phenomenology_deep.json",
]

POETICS_SUBFIELDS = (
    '古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム',
    '近代美学・詩学','現象学的詩学','中世・ルネサンス詩学',
    'ポスト構造主義詩学','受容理論','認知詩学','比較詩学','デジタル詩学'
)

# G file uses English subfield codes → Japanese
G_SUBFIELD_MAP = {
    'digital_poetics': 'デジタル詩学',
    'digital_rhetoric': '修辞学・弁論術',
    'digital_humanities': 'デジタル詩学',
    'media_theory': 'デジタル詩学',
    'game_studies': 'デジタル詩学',
    'rhetoric': '修辞学・弁論術',
}

# H file uses school names → subfield
H_SCHOOL_SUBFIELD_MAP = {
    'post-structuralism': 'ポスト構造主義詩学',
    'deconstruction': 'ポスト構造主義詩学',
    'lacanian': 'ポスト構造主義詩学',
    'structuralist narratology': '構造主義詩学',
    'structuralism': '構造主義詩学',
    'linguistic poetics': '構造主義詩学',
    'narratology': '構造主義詩学',
    'semiotics': '構造主義詩学',
    'copenhagen': '構造主義詩学',
    'russian formalism': 'ロシア・フォルマリズム',
    'russian symbolism': 'ロシア・フォルマリズム',
    'russian stylistics': 'ロシア・フォルマリズム',
    'russian historical': 'ロシア・フォルマリズム',
    'phenomenolog': '現象学的詩学',
    'existential': '現象学的詩学',
    'peircean': '現象学的詩学',
    'hegelian': '近代美学・詩学',
    'kantian': '近代美学・詩学',
    'schopenhauerian': '近代美学・詩学',
    'nietzschean': '近代美学・詩学',
    'schillerian': '近代美学・詩学',
    'modernist': '近代美学・詩学',
    'imagism': '近代美学・詩学',
    'cambridge': '近代美学・詩学',
    'french symbolism': '近代美学・詩学',
    'kierkegaardian': '近代美学・詩学',
}


def g_subfield(raw):
    if not raw:
        return 'デジタル詩学'
    low = raw.lower()
    for key, val in G_SUBFIELD_MAP.items():
        if low.startswith(key):
            return val
    return 'デジタル詩学'


def h_subfield(school):
    if not school:
        return '構造主義詩学'
    low = school.lower()
    for key, val in H_SCHOOL_SUBFIELD_MAP.items():
        if key in low:
            return val
    return '近代美学・詩学'


def normalize_concept(c, fname):
    """Normalize concept dict to standard schema regardless of agent's output format."""
    if 'G_' in fname:
        return {
            'id': c['id'],
            'name_ja': c.get('label_ja') or c.get('label_en') or c['id'],
            'name_en': c.get('label_en'),
            'name_original': None,
            'definition': c.get('definition_ja') or c.get('definition'),
            'impact_summary': None,
            'subfield': g_subfield(c.get('subfield')),
            'school_of_thought': None,
            'era_start': c.get('year'),
            'era_end': None,
            'methodology_level': None,
            'keywords_ja': None,
            'keywords_en': None,
            'originator_id': c.get('researcher_ref'),
            'year_proposed': c.get('year'),
            'founding_work': None,
        }
    elif 'H_' in fname:
        school = c.get('school', '')
        kt = c.get('key_terms', [])
        keywords_en = ', '.join(kt) if isinstance(kt, list) else kt
        researcher_ids = c.get('researcher_ids', [])
        originator_id = researcher_ids[0] if researcher_ids else None
        name_en = c.get('name_en') or c.get('name_native')
        return {
            'id': c['id'],
            'name_ja': name_en,  # no Japanese name provided; use English
            'name_en': name_en,
            'name_original': c.get('name_native'),
            'definition': c.get('definition'),
            'impact_summary': c.get('primary_source'),
            'subfield': h_subfield(school),
            'school_of_thought': school,
            'era_start': c.get('year'),
            'era_end': None,
            'methodology_level': None,
            'keywords_ja': None,
            'keywords_en': keywords_en or None,
            'originator_id': originator_id,
            'year_proposed': c.get('year'),
            'founding_work': c.get('primary_source'),
        }
    else:
        # Standard schema (E, F)
        return {
            'id': c['id'],
            'name_ja': c.get('name_ja') or c.get('name_en') or c['id'],
            'name_en': c.get('name_en'),
            'name_original': c.get('name_original'),
            'definition': c.get('definition'),
            'impact_summary': c.get('impact_summary'),
            'subfield': c.get('subfield'),
            'school_of_thought': c.get('school_of_thought'),
            'era_start': c.get('era_start'),
            'era_end': c.get('era_end'),
            'methodology_level': c.get('methodology_level'),
            'keywords_ja': c.get('keywords_ja'),
            'keywords_en': c.get('keywords_en'),
            'originator_id': c.get('originator_id'),
            'year_proposed': c.get('year_proposed'),
            'founding_work': c.get('founding_work'),
        }


def normalize_researcher(r, fname):
    """Normalize researcher dict to standard schema."""
    if 'G_' in fname:
        return {
            'id': r['id'],
            'name_full': r.get('name') or r.get('name_full') or r['id'],
            'name_ja': r.get('name_ja'),
            'birth_year': r.get('born'),
            'death_year': r.get('death_year'),
            'nationality': r.get('country'),
            'primary_institution': None,
            'research_themes': r.get('field'),
            'biography_brief': None,
        }
    elif 'H_' in fname:
        kw = r.get('key_works', [])
        kw_str = '; '.join(kw) if isinstance(kw, list) else kw
        return {
            'id': r['id'],
            'name_full': r.get('name') or r['id'],
            'name_ja': None,
            'birth_year': r.get('birth_year'),
            'death_year': r.get('death_year'),
            'nationality': r.get('nationality'),
            'primary_institution': None,
            'research_themes': r.get('primary_school'),
            'biography_brief': r.get('contribution') or kw_str or None,
        }
    else:
        name_full = r.get('name_full') or r.get('name_en') or r.get('name_ja') or r['id']
        themes = r.get('research_themes') or ', '.join(filter(None, [r.get('main_school'), r.get('key_concepts')])) or None
        return {
            'id': r['id'],
            'name_full': name_full,
            'name_ja': r.get('name_ja'),
            'birth_year': r.get('birth_year'),
            'death_year': r.get('death_year'),
            'nationality': r.get('nationality'),
            'primary_institution': r.get('primary_institution'),
            'research_themes': themes,
            'biography_brief': r.get('biography_brief') or r.get('biography'),
        }


def load_all():
    concepts, researchers, relations = {}, {}, []
    for fname in FILES:
        path = COLLECT_DIR / fname
        if not path.exists():
            print(f"SKIP (not found): {fname}")
            continue
        with path.open() as f:
            d = json.load(f)
        for c in d.get('concepts', []):
            cid = c['id']
            if cid not in concepts:
                concepts[cid] = normalize_concept(c, fname)
        for r in d.get('researchers', []):
            rid = r['id']
            if rid not in researchers:
                researchers[rid] = normalize_researcher(r, fname)
        for rel in d.get('relations', []):
            relations.append(rel)
    return list(concepts.values()), list(researchers.values()), relations


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys=OFF')
    cur = conn.cursor()

    concepts, researchers, relations = load_all()
    print(f'Loaded: {len(concepts)} concepts, {len(researchers)} researchers, {len(relations)} relations')

    cur.execute('SELECT id FROM humanities_concept')
    existing_concept_ids = {r[0] for r in cur.fetchall()}
    cur.execute('SELECT id FROM researchers')
    existing_researcher_ids = {r[0] for r in cur.fetchall()}

    # Insert researchers
    r_ins = r_skip = 0
    for r in researchers:
        if r['id'] in existing_researcher_ids:
            r_skip += 1
            continue
        cur.execute("""
            INSERT INTO researchers (id, name_full, name_ja, birth_year, death_year,
                nationality, primary_institution, research_themes, biography_brief)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, (
            r['id'], r['name_full'], r['name_ja'],
            r['birth_year'], r['death_year'],
            r['nationality'], r['primary_institution'],
            r['research_themes'], r['biography_brief'],
        ))
        existing_researcher_ids.add(r['id'])
        r_ins += 1
    print(f'Researchers: inserted {r_ins}, skipped {r_skip}')

    # Insert concepts
    c_ins = c_skip = 0
    for c in concepts:
        if c['id'] in existing_concept_ids:
            c_skip += 1
            continue
        cur.execute("""
            INSERT INTO humanities_concept (
                id, name_ja, name_en, name_original, definition, impact_summary,
                subfield, school_of_thought, era_start, era_end,
                methodology_level, keywords_ja, keywords_en,
                status, source_reliability, data_completeness)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            c['id'], c['name_ja'], c['name_en'], c['name_original'],
            c['definition'], c['impact_summary'],
            c['subfield'], c['school_of_thought'],
            c['era_start'], c['era_end'],
            c['methodology_level'],
            c['keywords_ja'], c['keywords_en'],
            'active', 'secondary', 70,
        ))
        existing_concept_ids.add(c['id'])
        c_ins += 1

        oid = c.get('originator_id')
        if oid and oid in existing_researcher_ids:
            try:
                cur.execute("""
                    INSERT OR IGNORE INTO humanities_concept_researchers
                        (concept_id, researcher_id, role, year_associated, note)
                    VALUES (?,?,?,?,?)
                """, (c['id'], oid, 'originator', c.get('year_proposed'), c.get('founding_work')))
            except sqlite3.IntegrityError:
                pass
    print(f'Concepts: inserted {c_ins}, skipped {c_skip}')

    # Insert relations
    rel_ins = rel_skip_missing = rel_skip_dup = 0
    seen_rel = set()
    for rel in relations:
        s, t = rel.get('source_id'), rel.get('target_id')
        rt = rel.get('relation_type', 'related')
        if s not in existing_concept_ids or t not in existing_concept_ids:
            rel_skip_missing += 1
            continue
        key = (s, t, rt)
        if key in seen_rel:
            rel_skip_dup += 1
            continue
        seen_rel.add(key)
        cur.execute("""
            INSERT INTO humanities_concept_relations
                (id, source_concept_id, target_concept_id, relation_type,
                 relation_description, strength, is_confirmed)
            VALUES (?,?,?,?,?,?,?)
        """, (str(uuid.uuid4()), s, t, rt, rel.get('description'), rel.get('strength', 5), 1))
        rel_ins += 1
    print(f'Relations: inserted {rel_ins}, skipped(missing) {rel_skip_missing}, skipped(dup) {rel_skip_dup}')

    conn.commit()

    # Final stats
    cur.execute("""
        SELECT subfield, COUNT(*) FROM humanities_concept
        WHERE subfield IN ({})
        GROUP BY subfield ORDER BY COUNT(*) DESC
    """.format(','.join('?' * len(POETICS_SUBFIELDS))), POETICS_SUBFIELDS)
    print('\n=== Poetics subfield counts after Phase 3 ===')
    total = 0
    for sf, n in cur.fetchall():
        print(f'  {sf}: {n}')
        total += n
    print(f'  TOTAL: {total}')

    cur.execute("""
        SELECT COUNT(DISTINCT r.id) FROM researchers r
        JOIN humanities_concept_researchers hcr ON r.id = hcr.researcher_id
        JOIN humanities_concept hc ON hc.id = hcr.concept_id
        WHERE hc.subfield IN ({})
    """.format(','.join('?' * len(POETICS_SUBFIELDS))), POETICS_SUBFIELDS)
    print(f'  Researchers linked: {cur.fetchone()[0]}')

    cur.execute("""
        SELECT COUNT(*) FROM humanities_concept_relations rel
        JOIN humanities_concept c1 ON rel.source_concept_id = c1.id
        JOIN humanities_concept c2 ON rel.target_concept_id = c2.id
        WHERE c1.subfield LIKE '%詩学%' OR c2.subfield LIKE '%詩学%'
           OR c1.subfield LIKE '%美学%' OR c2.subfield LIKE '%美学%'
           OR c1.subfield LIKE '%修辞%' OR c2.subfield LIKE '%修辞%'
           OR c1.subfield LIKE '%受容%' OR c2.subfield LIKE '%受容%'
           OR c1.subfield LIKE '%フォルマ%' OR c2.subfield LIKE '%フォルマ%'
    """)
    print(f'  Relations: {cur.fetchone()[0]}')

    cur.execute("SELECT COUNT(*) FROM researchers WHERE id LIKE 'res_%'")
    print(f'  Total researchers in DB: {cur.fetchone()[0]}')

    conn.close()


if __name__ == '__main__':
    main()
