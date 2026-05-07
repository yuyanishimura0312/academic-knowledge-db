#!/usr/bin/env python3
"""Phase 8 founding-quote dispatcher.

For 30 specialist groups of existing major concepts, add founding original-source
quotes that establish or define each concept. Each worker handles a specific
school/era and links 20-25 concepts to their founding text quotes.
"""
import subprocess
import sqlite3
from pathlib import Path

OUTPUT_DIR = Path("/tmp/poetics_quotes_p8")
LOG_DIR = Path("/tmp/poetics_quotes_p8_logs")
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

DB_PATH = Path(__file__).parent.parent / "academic.db"

# Group concepts by school/era and assign each group to a worker
# Each worker gets ~20-25 concept IDs and produces founding quotes for them
WORKER_GROUPS = [
    # Greek classical poetics
    ("PLATO_REPUBLIC", "Plato Republic Books II/III/X passages on poetry, mimesis, censorship, divine inspiration", ["mimesis", "ミメーシス", "プラトンの詩人追放", "イデア", "詩的霊感", "プラトンの詩学批判"]),
    ("ARISTOTLE_POETICS", "Aristotle Poetics 1447a-1462b passages establishing key concepts", ["カタルシス", "ミメーシス", "プロットの統一", "プロット", "性格", "思想", "言語表現", "歌曲", "視覚", "悲劇", "叙事詩", "喜劇", "ハマルティア", "ペリペテイア", "アナグノリシス", "魂の浄化"]),
    ("LONGINUS_SUBLIME", "Longinus On the Sublime passages on hypsos, 5 sources of sublime, transport, ecstasy", ["崇高", "ヒュプソス", "崇高の五源泉", "崇高による移送", "崇高の大いなる精神"]),
    ("HORACE_ARS_POETICA", "Horace Ars Poetica passages on ut pictura poesis, decorum, golden mean, dulce et utile", ["ホラティウスの詩論", "詩は絵のごとし", "甘美と有益", "適切性"]),
    # Sanskrit poetics
    ("BHARATA_NATYASHASTRA", "Bharata Natyashastra Ch.6-7 passages establishing rasa-sutra, 8+1 rasas, bhava theory", ["ラサ", "シュリンガーラ", "カルナ", "ハーシャ", "ラウドラ", "ヴィーラ", "シャーンタ", "バヴァ", "スターイビハーヴァ"]),
    ("ANANDAVARDHANA_DHVANI", "Anandavardhana Dhvanyaloka passages on dhvani as soul of poetry, vyangya, lakshana", ["ドゥヴァニ", "暗示論", "ヴィヤンジャナー", "ラクシャナー"]),
    ("BHAMAHA_DANDIN", "Bhamaha Kavyalankara + Dandin Kavyadarsha passages defining alamkaras, gunas, rasa", ["アランカーラ", "グナ", "ヴァイダルビ・リティ", "ガウディ・リティ"]),
    ("MAMMATA_KAVYA", "Mammata Kavyaprakasha passages on kavya as ramaniyartha-prati-padaka, vyanjana", ["カーヴィヤ", "詩美の本質"]),
    # Russian Formalism
    ("SHKLOVSKY_ART", "Shklovsky 'Art as Technique' (1917) passages on ostranenie, automation, priem", ["異化", "オストラネーニエ", "オストラニェニエ", "プリエム"]),
    ("EIKHENBAUM_TYNIANOV", "Eikhenbaum 'Theory of Formal Method', Tynianov 'Literary Fact' on dominant, system, evolution", ["ドミナント", "文学的事実", "文学進化"]),
    ("BAKHTIN_DIALOGIC", "Bakhtin Dialogic Imagination, Problems of Dostoevsky's Poetics passages on chronotope, polyphony, dialogism, heteroglossia, carnival", ["クロノトポス", "対話性", "ポリフォニー", "ヘテログロッシア", "カーニヴァル", "笑いの文化"]),
    # Structuralism
    ("JAKOBSON_FUNCTIONS", "Jakobson 'Linguistics and Poetics' Closing Statement passages on 6 functions, poetic function, equivalence", ["ヤコブソンの6機能", "詩的機能", "等価軸", "メタファーとメトニミー"]),
    ("BARTHES_SZ", "Barthes S/Z + Mythologies passages on 5 codes, readerly/writerly, mythologization, death of author", ["バルトの5コード", "読者的/作者的テクスト", "作者の死", "神話化"]),
    ("GENETTE_NARRATOLOGY", "Genette Figures III + Narrative Discourse passages on focalization, voice, time, frequency", ["ジュネットの焦点化", "外部焦点化", "内部焦点化", "ゼロ焦点化", "アナレプシス", "プロレプシス"]),
    ("GREIMAS_LEVI_STRAUSS", "Greimas semiotic square + Levi-Strauss Structural Anthropology myth analysis passages", ["グレマスの記号論的方陣", "アクタント・モデル", "構造分析", "神話の構造"]),
    # Phenomenology
    ("INGARDEN_LITERARY", "Ingarden The Literary Work of Art passages on 4 strata, places of indeterminacy, concretization", ["インガルデンの4層", "不定箇所", "具体化", "図式的諸相"]),
    ("HEIDEGGER_LANGUAGE", "Heidegger Hölderlin lectures + 'Origin of Work of Art' passages on poetic dwelling, world/earth", ["世界と大地", "詩的存在", "言葉の本質"]),
    # Reception theory
    ("JAUSS_HORIZON", "Jauss 'Literary History as Provocation' passages establishing Erwartungshorizont, aesthetic distance", ["期待の地平", "美的距離", "地平の変化"]),
    ("ISER_IMPLIED", "Iser Act of Reading + Implied Reader passages on gaps, indeterminacy, implied reader", ["想定された読者", "空白", "ギャップ充填"]),
    # Cognitive poetics
    ("LAKOFF_JOHNSON", "Lakoff-Johnson Metaphors We Live By + Philosophy in the Flesh passages on conceptual metaphor", ["概念メタファー", "イメージ・スキーマ", "メタファー写像"]),
    ("STOCKWELL_FAUCONNIER", "Stockwell Cognitive Poetics + Fauconnier-Turner Way We Think passages on text worlds, blends, mental spaces", ["メンタル・スペース", "概念ブレンディング", "テクスト世界理論"]),
    # Postmodern / Deconstruction
    ("DERRIDA_PLAY", "Derrida Of Grammatology + 'Structure Sign Play' passages on différance, trace, supplementarity", ["差延", "痕跡", "補完性", "脱構築"]),
    ("KRISTEVA_SEMIOTIC", "Kristeva Revolution in Poetic Language + Desire in Language passages on semiotic vs symbolic, intertextuality, abjection, chora", ["記号態", "象徴態", "間テクスト性", "アブジェクシオン", "コーラ"]),
    ("FOUCAULT_DISCOURSE", "Foucault Archaeology of Knowledge + Order of Things passages on discourse, episteme, statement", ["エピステーメー", "言説形成", "ディスクール"]),
    # Japanese poetics
    ("ZEAMI_FUSHIKADEN", "Zeami Fushikaden + Kakyo passages on yugen, hana, monomane, jo-ha-kyu, sandō", ["幽玄", "花", "物まね", "序破急", "三体"]),
    ("KAMO_NO_CHOMEI", "Kamo no Chōmei Mumyōshō passages on yugen, sabi, kokoro vs kotoba, yojō", ["余情", "もののあはれ", "心と詞", "幽玄論"]),
    ("BASHO_KYORAI", "Basho Sarumino + Kyorai-shō passages on fueki-ryūkō, sabi, shiori, hosomi, karumi", ["不易流行", "寂び", "しをり", "細み", "軽み", "風雅"]),
    ("MOTOORI_NORINAGA", "Motoori Norinaga Shibun Yōryō + Genji Monogatari Tama no Ogushi passages on mono no aware", ["もののあはれ", "古今集の風"]),
    # Chinese poetics
    ("LIU_XIE_WENXIN", "Liu Xie Wenxin Diaolong selected passages on yuán-dào, qíng-cái, xié-yún, fēng-gǔ, shén-sī", ["原道", "情采", "風骨", "神思"]),
    ("WANG_GUOWEI_RENJIAN", "Wang Guowei Renjian Cihua passages on jingjie 境界, you-wo zhi jing, wu-wo zhi jing", ["境界", "有我之境", "無我之境", "意境"]),
    # Modernist criticism
    ("ELIOT_TRADITION", "T.S. Eliot 'Tradition and the Individual Talent' + Sacred Wood passages on tradition, dissociation of sensibility, objective correlative", ["伝統と個人の才能", "感受性の分離", "客観的相関物"]),
    ("EMPSON_AMBIGUITY", "Empson Seven Types of Ambiguity passages defining each ambiguity type", ["7つの曖昧性", "曖昧性の型"]),
    ("BROOKS_WIMSATT", "Brooks Well Wrought Urn + Wimsatt Verbal Icon passages on heresy of paraphrase, intentional/affective fallacy, irony, paradox", ["パラフレーズの異端", "意図の誤謬", "感情の誤謬", "アイロニー", "パラドックス"]),
]

def get_concept_ids_by_keywords(keywords):
    """Match keywords to actual concept IDs in DB."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    matches = []
    for kw in keywords:
        cur.execute("""SELECT id, name_ja FROM humanities_concept
                       WHERE subfield IN ('古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム',
                                          '近代美学・詩学','現象学的詩学','中世・ルネサンス詩学',
                                          'ポスト構造主義詩学','受容理論','認知詩学','比較詩学','デジタル詩学')
                       AND name_ja LIKE ? LIMIT 5""", (f"%{kw}%",))
        matches.extend([(r[0], r[1]) for r in cur.fetchall()])
    conn.close()
    seen_ids = set()
    unique = []
    for cid, nm in matches:
        if cid not in seen_ids:
            seen_ids.add(cid)
            unique.append((cid, nm))
    return unique[:30]


def build_prompt(wid, axis_desc, concept_pairs):
    pairs_str = "\n".join([f"  - {cid}: {nm}" for cid, nm in concept_pairs])
    return f"""For these existing concepts, generate founding-source quotes from the original poetics texts.

WORKER AXIS: {axis_desc}

CONCEPTS (use these exact concept_id strings):
{pairs_str}

For each concept, output a single founding_quote record linking it to its founding/key original-source passage.

OUTPUT (only this JSON, no commentary):
{{"worker_id": "{wid}", "quotes": [
  {{"concept_id": "<exact_id_from_above>",
    "source_type": "founding_text",
    "source_work_title": "<e.g. 'Aristotle Poetics' or '岩波文庫『風姿花伝』'>",
    "source_locator": "<e.g. '1449b25-28' or 'Book III Ch.6' or '巻第三'>",
    "source_year": <approximate composition year>,
    "source_author": "<author>",
    "source_language": "<ISO 639-3 like grc, lat, san, lzh, jpn, fra, deu>",
    "quote_original": "<2-8 lines of the actual original-language passage>",
    "quote_japanese": "<Japanese translation 2-6 lines>",
    "quote_english": "<English translation 2-6 lines>",
    "quote_significance": "<200-300字 in Japanese: why this quote founds/defines the concept>",
    "source_url": "<URL to PD archive>",
    "source_archive": "Perseus / Project Gutenberg / GRETIL / Wikisource / 青空文庫 / 維基文庫 / etc",
    "public_domain_status": "PD-original or fair-use-excerpt"
  }},
  ... (one per concept above)
]}}

Requirements:
- Use the EXACT concept_id strings provided (do not invent new ones)
- Original-language passages MUST be in original script (Greek/Sanskrit/Chinese/Japanese/Latin/etc.)
- Quote MUST be a real attested passage where this concept is established
- Output JSON only.
"""


def main():
    procs = []
    log_files = []
    for wid, axis, keywords in WORKER_GROUPS:
        out_file = OUTPUT_DIR / f"P8Q_{wid}.json"
        log_file = LOG_DIR / f"P8Q_{wid}.log"
        if out_file.exists() and out_file.stat().st_size > 1500:
            print(f"Skip {out_file.name}")
            continue
        concept_pairs = get_concept_ids_by_keywords(keywords)
        if not concept_pairs:
            print(f"WARN no concepts for {wid}, skipping")
            continue
        prompt = build_prompt(wid, axis, concept_pairs)
        cmd = ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only",
               "--output-last-message", str(out_file), prompt]
        log = open(log_file, "w")
        p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
        procs.append((wid, p))
        log_files.append(log)
        print(f"Launched P8Q_{wid} (pid {p.pid}, {len(concept_pairs)} concepts)")

    print(f"\n{len(procs)} quote workers running...")
    for wid, p in procs:
        rc = p.wait()
        print(f"  P8Q_{wid}: exit {rc}")
    for lf in log_files:
        lf.close()


if __name__ == "__main__":
    main()
