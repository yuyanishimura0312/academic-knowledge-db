#!/usr/bin/env python3
"""Phase 10-B: 概念-概念系譜関係の拡張。"""
import sqlite3
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
DB_PATH = ROOT.parent / "academic.db"
OUTPUT_DIR = Path("/tmp/poetics_relations_p10")
LOG_DIR = Path("/tmp/poetics_relations_p10_logs")
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

CLUSTERS = [
    ("greek_classical", "古典詩学", -800, -200, "Greek classical poetics: Plato/Aristotle/Longinus/Horace genealogy"),
    ("hellenistic_roman", "古典詩学", -200, 500, "Hellenistic to Roman late antique"),
    ("rasa_dhvani", "比較詩学", 200, 1500, "Sanskrit rasa-dhvani-alankara genealogy"),
    ("japanese_karon", "比較詩学", 800, 1900, "Japanese karon (歌論) lineage"),
    ("chinese_shihua", "比較詩学", 200, 1900, "Chinese 詩論 lineage"),
    ("arabic_balagha", "修辞学・弁論術", 700, 1500, "Arabic balagha tradition"),
    ("russian_formalism", "ロシア・フォルマリズム", 1910, 1940, "Russian Formalism lineage"),
    ("structuralism", "構造主義詩学", 1950, 1980, "Structuralism: Saussure→Jakobson→Barthes→Greimas→Genette"),
    ("phenomenology", "現象学的詩学", 1900, 1980, "Phenomenology: Husserl→Heidegger→Ingarden→Ricœur"),
    ("reception", "受容理論", 1960, 2000, "Reception: Hirsch→Iser→Jauss→Fish"),
    ("cognitive", "認知詩学", 1980, 2025, "Cognitive: Lakoff→Turner-Fauconnier→Stockwell→Herman"),
    ("deconstruction", "ポスト構造主義詩学", 1960, 2010, "Deconstruction: Derrida→de Man→Spivak"),
    ("kristeva_foucault", "ポスト構造主義詩学", 1960, 2010, "Kristeva intertextuality + Foucault discourse"),
    ("genette_narratology", "構造主義詩学", 1970, 2000, "Genette narratology branches"),
    ("longinus_sublime", "古典詩学", 100, 1800, "Longinian sublime: Boileau→Burke→Kant→Schiller→Coleridge"),
    ("aristotle_reception", "中世・ルネサンス詩学", 1000, 1700, "Aristotle Poetics reception"),
    ("zen_haikai", "比較詩学", 1100, 1900, "Zen-haikai: 道元→Saigyō→Bashō→Buson→Issa→Shiki"),
    ("noh", "比較詩学", 1300, 1700, "Noh aesthetics: Kannami→Zeami→Zenchiku"),
    ("modernist_critics", "近代美学・詩学", 1900, 1960, "Modernist criticism: Pound→Eliot→Brooks→Frye"),
    ("postcolonial", "比較詩学", 1960, 2020, "Postcolonial: Said→Spivak→Bhabha→Glissant"),
    ("digital_media", "デジタル詩学", 1990, 2025, "Digital: Aarseth→Hayles→Manovich"),
    ("metaphor_branches", "認知詩学", 1980, 2020, "Conceptual metaphor branches"),
    ("ecocriticism", "近代美学・詩学", 1990, 2025, "Ecocriticism waves"),
    ("queer_feminist", "近代美学・詩学", 1970, 2025, "Queer/feminist poetics: Cixous→Butler→Sedgwick"),
    ("translation", "比較詩学", 1900, 2025, "Translation theory: Benjamin→Venuti→Apter→Spivak"),
    ("byzantine_carolingian", "中世・ルネサンス詩学", 500, 1300, "Byzantine and Carolingian poetics"),
    ("medieval_arts", "中世・ルネサンス詩学", 1100, 1500, "Medieval Arts of Poetry"),
    ("renaissance", "中世・ルネサンス詩学", 1450, 1650, "Renaissance Italian poetics treatises"),
    ("reception_phenom", "受容理論", 1900, 1990, "Phenomenology-reception bridge: Ingarden→Iser"),
    ("formalism_structuralism", "構造主義詩学", 1920, 1970, "Formalism→Structuralism transition: Jakobson"),
]

PER_WORKER = 50


def get_concepts(subfield, era_min, era_max):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""SELECT id, name_ja, name_en, school_of_thought, era_start
                   FROM humanities_concept WHERE subfield = ?
                   AND COALESCE(era_start, 9999) BETWEEN ? AND ?
                   ORDER BY COALESCE(era_start, 9999), id LIMIT 60""",
                (subfield, era_min, era_max))
    rows = cur.fetchall()
    conn.close()
    return rows


def build_prompt(wid, sf, axis_desc, concepts):
    lines = []
    for cid, nm, nen, school, era in concepts:
        line = f"  - {cid}: {nm}"
        if nen:
            line += f" ({nen})"
        if school:
            line += f" — {school}"
        if era:
            line += f" / era {era}"
        lines.append(line)
    cl = "\n".join(lines)
    return f"""Generate {PER_WORKER} genealogical relations among these poetics concepts.

CLUSTER: {axis_desc}
SUBFIELD: {sf}

CONCEPTS (use EXACT IDs):
{cl}

OUTPUT (only JSON, no commentary):
{{"worker_id": "{wid}", "relations": [
  {{"source_concept_id": "<id>",
    "target_concept_id": "<id>",
    "relation_type": "<extends|critiques|opposes|synthesizes|derived_from|reinterprets|enables|complements|applies_to|related_to>",
    "relation_description": "<100-200字 in Japanese>",
    "strength": <integer 1-10>,
    "is_confirmed": 1
  }},
  ... ({PER_WORKER} relations)
]}}

Source != target. Use only ids from list. Output JSON only.
"""


def main():
    procs = []
    log_files = []
    for wid, sf, era_min, era_max, axis in CLUSTERS:
        out_file = OUTPUT_DIR / f"P10R_{wid}.json"
        log_file = LOG_DIR / f"P10R_{wid}.log"
        if out_file.exists() and out_file.stat().st_size > 1000:
            print(f"Skip {out_file.name}")
            continue
        concepts = get_concepts(sf, era_min, era_max)
        if len(concepts) < 5:
            print(f"WARN {wid} too few ({len(concepts)})")
            continue
        prompt = build_prompt(wid, sf, axis, concepts)
        cmd = ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only",
               "--output-last-message", str(out_file), prompt]
        log = open(log_file, "w")
        p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
        procs.append((wid, p))
        log_files.append(log)
        print(f"Launched P10R_{wid} (pid {p.pid})")

    print(f"\n{len(procs)} relation workers running")
    for wid, p in procs:
        rc = p.wait()
    for lf in log_files:
        lf.close()


if __name__ == "__main__":
    main()
