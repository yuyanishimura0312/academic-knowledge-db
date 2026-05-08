#!/usr/bin/env python3
"""Generate poetics dashboard v2.0 (concepts + texts) for miratuku-news-v2.

Two-layer dashboard: theory (concepts) + primary texts (詩文).
"""

import sqlite3
import json
from collections import Counter
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
OUTPUT = Path.home() / "projects/apps/miratuku-news-v2/dashboards/pt.html"

POETICS = ('古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム',
    '近代美学・詩学','現象学的詩学','中世・ルネサンス詩学','ポスト構造主義詩学',
    '受容理論','認知詩学','比較詩学','デジタル詩学')

CATEGORIES = {
    "A": {"name": "A. 古典・修辞学的伝統", "color": "#CC1400",
          "subs": ["古典詩学", "修辞学・弁論術", "中世・ルネサンス詩学", "比較詩学"]},
    "B": {"name": "B. 形式主義・構造主義", "color": "#0066CC",
          "subs": ["ロシア・フォルマリズム", "構造主義詩学"]},
    "C": {"name": "C. 美学・現象学的伝統", "color": "#996600",
          "subs": ["近代美学・詩学", "現象学的詩学"]},
    "D": {"name": "D. 現代理論・読者・認知・デジタル", "color": "#008844",
          "subs": ["ポスト構造主義詩学", "受容理論", "認知詩学", "デジタル詩学"]},
}

CULTURE_ORDER = [
    "古代ギリシャ・ローマ", "中世ヨーロッパ", "近代ヨーロッパ", "20-21世紀グローバル",
    "中国古典", "日本古典", "東アジア", "仏典詩偈",
    "サンスクリット", "アラビア・ペルシア",
    "アフリカ", "先住民・口承"
]


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    qs = ",".join(["?"] * len(POETICS))

    # === Concept layer (existing) ===
    cur.execute(f"SELECT subfield, COUNT(*) FROM humanities_concept WHERE id LIKE 'cp_%' GROUP BY subfield")
    sf_counts = dict(cur.fetchall())

    cur.execute(f"SELECT era_start FROM humanities_concept WHERE id LIKE 'cp_%' AND era_start IS NOT NULL")
    years = [r[0] for r in cur.fetchall()]

    cur.execute(f"""SELECT relation_type, COUNT(*) FROM humanities_concept_relations rel
        WHERE rel.source_concept_id IN (SELECT id FROM humanities_concept WHERE id LIKE 'cp_%')
           OR rel.target_concept_id IN (SELECT id FROM humanities_concept WHERE id LIKE 'cp_%')
        GROUP BY relation_type ORDER BY COUNT(*) DESC""")
    rel_types = cur.fetchall()
    rel_total = sum(n for _, n in rel_types)

    cur.execute(f"""SELECT r.name_ja, r.name_full, COUNT(DISTINCT hcr.concept_id) AS n
        FROM researchers r JOIN humanities_concept_researchers hcr ON r.id = hcr.researcher_id
        JOIN humanities_concept hc ON hc.id = hcr.concept_id
        WHERE hc.id LIKE 'cp_%'
        GROUP BY r.id ORDER BY n DESC LIMIT 24""")
    researchers = cur.fetchall()

    cur.execute(f"""SELECT COUNT(DISTINCT r.id) FROM researchers r
        JOIN humanities_concept_researchers hcr ON r.id = hcr.researcher_id
        JOIN humanities_concept hc ON hc.id = hcr.concept_id
        WHERE hc.id LIKE 'cp_%'""")
    researcher_total = cur.fetchone()[0]

    cur.execute(f"""SELECT school_of_thought, COUNT(*) FROM humanities_concept
        WHERE id LIKE 'cp_%' AND school_of_thought IS NOT NULL
        GROUP BY school_of_thought ORDER BY COUNT(*) DESC LIMIT 18""")
    schools = cur.fetchall()

    era_buckets_disp = [
        ("古代（BC500-AD500）", sum(1 for y in years if -500 <= y < 500)),
        ("中世（500-1400）", sum(1 for y in years if 500 <= y < 1400)),
        ("ルネサンス・近世（1400-1750）", sum(1 for y in years if 1400 <= y < 1750)),
        ("18-19世紀（1750-1900）", sum(1 for y in years if 1750 <= y < 1900)),
        ("20世紀前半（1900-1950）", sum(1 for y in years if 1900 <= y < 1950)),
        ("20世紀後半（1950-2000）", sum(1 for y in years if 1950 <= y < 2000)),
        ("21世紀（2000-）", sum(1 for y in years if 2000 <= y < 2100)),
    ]
    total_concepts = sum(sf_counts.values())

    # === Text layer (new in v2) ===
    cur.execute("SELECT COUNT(*) FROM poetics_text")
    text_total = cur.fetchone()[0]

    cur.execute("SELECT culture_region, COUNT(*) FROM poetics_text GROUP BY culture_region ORDER BY 2 DESC")
    text_by_culture = cur.fetchall()

    cur.execute("SELECT canonical_tier, COUNT(*) FROM poetics_text GROUP BY canonical_tier")
    text_by_tier = dict(cur.fetchall())

    cur.execute("SELECT era_year FROM poetics_text WHERE era_year IS NOT NULL")
    text_years = [r[0] for r in cur.fetchall()]
    text_era_buckets = [
        ("古代（BC1500-AD500）", sum(1 for y in text_years if -1500 <= y < 500)),
        ("中世（500-1400）", sum(1 for y in text_years if 500 <= y < 1400)),
        ("ルネサンス・近世（1400-1750）", sum(1 for y in text_years if 1400 <= y < 1750)),
        ("18-19世紀（1750-1900）", sum(1 for y in text_years if 1750 <= y < 1900)),
        ("20-21世紀（1900-）", sum(1 for y in text_years if 1900 <= y < 2100)),
    ]

    cur.execute("SELECT form_genre, COUNT(*) FROM poetics_text WHERE form_genre IS NOT NULL GROUP BY form_genre ORDER BY 2 DESC LIMIT 20")
    text_forms = cur.fetchall()

    cur.execute("SELECT source_archive, COUNT(*) FROM poetics_text WHERE source_archive IS NOT NULL GROUP BY source_archive ORDER BY 2 DESC LIMIT 15")
    text_archives = cur.fetchall()

    cur.execute("""
        SELECT hc.name_ja, COUNT(*) AS texts
        FROM poetics_text_concept_link l
        JOIN humanities_concept hc ON hc.id = l.concept_id
        GROUP BY hc.name_ja ORDER BY texts DESC LIMIT 15
    """)
    top_concept_links = cur.fetchall()

    cur.execute("SELECT COUNT(*) FROM poetics_text_concept_link")
    link_total = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM poetics_text_motif")
    motif_total = cur.fetchone()[0]

    # === Phase 8: founding quotes layer ===
    try:
        cur.execute("SELECT COUNT(*) FROM concept_original_source")
        quote_total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT concept_id) FROM concept_original_source")
        concepts_with_quotes = cur.fetchone()[0]
        cur.execute("SELECT source_author, COUNT(*) FROM concept_original_source WHERE source_author IS NOT NULL GROUP BY source_author ORDER BY 2 DESC LIMIT 15")
        top_quote_authors = cur.fetchall()
        cur.execute("SELECT source_language, COUNT(*) FROM concept_original_source WHERE source_language IS NOT NULL GROUP BY source_language ORDER BY 2 DESC LIMIT 12")
        quote_languages = cur.fetchall()
        cur.execute("""SELECT hc.name_ja, cos.source_work_title, cos.source_locator, cos.source_author,
                              substr(cos.quote_original, 1, 80) AS qsnip
                       FROM concept_original_source cos JOIN humanities_concept hc ON cos.concept_id = hc.id
                       ORDER BY hc.name_ja LIMIT 25""")
        sample_quotes = [{"name": r[0], "work": r[1], "loc": r[2], "author": r[3], "snip": r[4]} for r in cur.fetchall()]
    except Exception:
        quote_total = 0
        concepts_with_quotes = 0
        top_quote_authors = []
        quote_languages = []
        sample_quotes = []

    cur.execute("SELECT motif_category, COUNT(*) FROM poetics_text_motif WHERE motif_category IS NOT NULL GROUP BY motif_category ORDER BY 2 DESC LIMIT 12")
    motif_cats = cur.fetchall()

    cur.execute("""
        SELECT culture_region, title_ja, author_name_display, era_year, form_genre, source_archive
        FROM poetics_text
        ORDER BY culture_region, era_year
    """)
    text_samples_all = cur.fetchall()
    samples_by_culture = {}
    for cr, ti, au, yr, fg, src in text_samples_all:
        samples_by_culture.setdefault(cr, []).append({
            "title_ja": ti, "author": au, "era": yr, "form": fg, "src": src
        })
    text_samples_show = {cr: samples_by_culture[cr][:8] for cr in samples_by_culture}

    sf_data_js = []
    for cat_id, cat in CATEGORIES.items():
        for sub in cat["subs"]:
            cnt = sf_counts.get(sub, 0)
            sf_data_js.append({"id": cat_id, "ja": sub, "count": cnt, "cat": cat_id})

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>詩学（Poetics）DB v2.0 | Insight News</title>
<link rel="icon" href="https://esse-sense.com/favicon.ico">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@400;700&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #FFFFFF; --card: #FFFFFF; --text: #121212; --text-secondary: #555555;
  --text-muted: #6B6B6B; --border: #D9D9D9; --border-light: #EEEEEE;
  --surface: #F7F7F5; --accent-warm: #CC1400; --accent-muted: rgba(204,20,0,0.06);
  --font: "Noto Sans JP", sans-serif; --font-serif: "Noto Serif JP", serif;
}}
[data-theme="dark"] {{
  --bg: #121212; --card: #1A1A1A; --text: #E0E0E0; --text-secondary: #AAAAAA;
  --text-muted: #8A8A8A; --border: #333333; --border-light: #2A2A2A;
  --surface: #1A1A1A; --accent-warm: #FF4040; --accent-muted: rgba(255,64,64,0.1);
}}
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: var(--font); color: var(--text); background: var(--bg); line-height: 1.7; max-width: 960px; margin: 0 auto; padding: 24px 20px; }}
.back {{ display: inline-block; margin-bottom: 20px; font-size: 0.82rem; color: var(--text-secondary); text-decoration: none; }}
.back:hover {{ color: var(--text); }}
h1 {{ font-family: var(--font-serif); font-size: 1.5rem; font-weight: 700; margin-bottom: 4px; }}
.db-id {{ font-family: monospace; font-size: 0.72rem; font-weight: 700; color: var(--accent-warm); background: var(--accent-muted); padding: 2px 8px; margin-right: 8px; }}
.subtitle {{ font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 12px; }}
.desc {{ font-size: 0.84rem; color: var(--text); margin-bottom: 24px; line-height: 1.85; }}
.overview {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px; margin-bottom: 28px; }}
.overview-card {{ background: var(--surface); border: 1px solid var(--border-light); padding: 14px; text-align: center; }}
.overview-value {{ font-family: var(--font-serif); font-size: 1.4rem; font-weight: 700; }}
.overview-label {{ font-size: 0.7rem; color: var(--text-muted); margin-top: 2px; }}
h2 {{ font-family: var(--font-serif); font-size: 1.25rem; font-weight: 700; margin: 40px 0 14px; padding: 8px 14px; background: var(--accent-muted); border-left: 4px solid var(--accent-warm); }}
h3 {{ font-family: var(--font-serif); font-size: 1rem; font-weight: 700; margin: 28px 0 12px; padding-bottom: 6px; border-bottom: 1px solid var(--border); }}
.note {{ font-size: 0.78rem; color: var(--text-muted); margin-top: 6px; line-height: 1.6; }}
.theme-toggle {{ position: fixed; top: 16px; right: 16px; background: var(--surface); border: 1px solid var(--border); padding: 6px 10px; cursor: pointer; font-size: 1rem; z-index: 10; }}
.subfield-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 8px; margin: 12px 0; }}
.subfield-item {{ display: flex; justify-content: space-between; align-items: center; padding: 10px 14px; background: var(--surface); border: 1px solid var(--border-light); font-size: 0.82rem; }}
.subfield-name-ja {{ font-weight: 500; }}
.subfield-count {{ font-weight: 700; color: var(--text-secondary); font-family: monospace; min-width: 40px; text-align: right; }}
.subfield-bar {{ height: 3px; opacity: 0.5; margin-top: 4px; }}
.type-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 6px; margin: 12px 0; }}
.type-item {{ display: flex; justify-content: space-between; padding: 8px 12px; background: var(--surface); border: 1px solid var(--border-light); font-size: 0.82rem; }}
.type-count {{ font-weight: 700; color: var(--text-secondary); font-family: monospace; }}
.researcher-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 6px; margin: 12px 0; }}
.researcher-item {{ display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: var(--surface); border: 1px solid var(--border-light); font-size: 0.82rem; }}
.researcher-name {{ font-weight: 500; }}
.researcher-meta {{ font-family: monospace; color: var(--text-muted); font-size: 0.75rem; }}
.era-bar-row {{ display: flex; align-items: center; margin-bottom: 6px; }}
.era-label {{ min-width: 220px; font-size: 0.78rem; color: var(--text-secondary); padding-right: 12px; }}
.era-bar {{ height: 22px; background: var(--accent-warm); opacity: 0.55; display: flex; align-items: center; padding-left: 8px; }}
.era-count {{ font-size: 0.72rem; color: #fff; font-weight: 600; }}
.cat-block {{ margin-bottom: 10px; }}
.cat-header {{ font-size: 0.82rem; font-weight: 600; padding: 6px 0 4px; }}
.cat-dot {{ display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 8px; vertical-align: middle; }}
.school-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 6px; margin: 12px 0; }}
.school-item {{ display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: var(--surface); border: 1px solid var(--border-light); font-size: 0.82rem; }}
.status-banner {{ background: var(--accent-muted); border-left: 3px solid var(--accent-warm); padding: 12px 16px; font-size: 0.84rem; margin-bottom: 24px; line-height: 1.7; }}
.layer-banner {{ background: var(--surface); border: 1px solid var(--border); padding: 14px 18px; margin: 18px 0; }}
.layer-title {{ font-size: 0.75rem; color: var(--text-muted); font-weight: 700; letter-spacing: 0.1em; margin-bottom: 4px; }}
.layer-desc {{ font-size: 0.84rem; line-height: 1.75; }}
.text-list {{ display: grid; gap: 4px; margin: 10px 0 18px; }}
.text-item {{ padding: 8px 12px; background: var(--surface); border-left: 2px solid var(--border); font-size: 0.8rem; line-height: 1.5; }}
.text-item-title {{ font-weight: 500; }}
.text-item-meta {{ font-size: 0.72rem; color: var(--text-muted); margin-top: 2px; }}
.culture-block {{ margin-bottom: 18px; }}
.culture-header {{ font-size: 0.88rem; font-weight: 700; color: var(--accent-warm); margin-bottom: 6px; padding-bottom: 4px; border-bottom: 1px dashed var(--border); }}
.link-btn {{ display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; background: var(--accent-warm); color: #fff; font-size: 0.82rem; font-weight: 600; text-decoration: none; transition: opacity 0.2s; margin-right: 8px; margin-bottom: 8px; }}
.link-btn:hover {{ opacity: 0.85; }}
.link-btn-outline {{ background: transparent; color: var(--accent-warm); border: 1px solid var(--accent-warm); }}
.link-btn-outline:hover {{ background: var(--accent-muted); }}
footer {{ margin-top: 48px; padding-top: 20px; border-top: 1px solid var(--border-light); font-size: 0.72rem; color: var(--text-muted); text-align: center; }}
</style>
</head>
<body>
<button class="theme-toggle" onclick="document.documentElement.setAttribute('data-theme',document.documentElement.getAttribute('data-theme')==='dark'?'':'dark')">&#9789;</button>
<a class="back" href="../databases.html">&larr; データベース一覧に戻る</a>

<h1><span class="db-id">PT v2.0</span>詩学（Poetics）DB</h1>
<p class="subtitle">理論層（{total_concepts}概念・{researcher_total}研究者）+ 詩文層（{text_total}テクスト）の二層構造</p>
<p class="desc">プラトン『国家』のミメーシス批判（前380年）から21世紀のデジタル詩学・認知詩学に至るまで、西洋・東洋の詩学・文学理論・修辞学を体系的に統合した補助知識データベース。v2.0では従来の<strong>理論層</strong>（{total_concepts}概念・{researcher_total}名の研究者・{rel_total}件の系譜関係）に加え、詩学が分析対象としてきた<strong>詩文層</strong>（{text_total}件の一次テクスト）を追加し、理論×実例の双方向参照を可能にした。Princeton Encyclopedia of Poetry and Poetics、Routledge Encyclopedia、Stanford Encyclopedia of Philosophyを主要典拠とし、詩文は Perseus Digital Library・Project Gutenberg・維基文庫・青空文庫・GRETIL・Ganjoor・Bibliotheca Augustana 等のパブリックドメイン原典から取得。</p>

<div class="status-banner">
v2.0 Phase 1完了。スキーマ4テーブル（poetics_text/translation/concept_link/motif）稼働、詩文 {text_total} テクスト・概念リンク {link_total} 件・モチーフ {motif_total} 件投入済。Phase 2-4 では Codex 並列収集により詩文を 4,000-5,000 件規模へ拡張、文化圏バランス（西欧55%・東アジア25%・南西アジア15%・他5%）を達成する計画。
</div>

<div style="margin-bottom:20px">
  <a class="link-btn link-btn-outline" href="https://github.com/yuyanishimura0312/academic-knowledge-db">GitHub <span style="font-size:0.72rem;opacity:0.85">&rarr;</span></a>
</div>

<div class="overview">
  <div class="overview-card"><div class="overview-value">{total_concepts}</div><div class="overview-label">概念</div></div>
  <div class="overview-card"><div class="overview-value">{researcher_total}</div><div class="overview-label">研究者</div></div>
  <div class="overview-card"><div class="overview-value">{rel_total}</div><div class="overview-label">系譜関係</div></div>
  <div class="overview-card"><div class="overview-value">{text_total}</div><div class="overview-label">詩文（一次）</div></div>
  <div class="overview-card"><div class="overview-value">{link_total}</div><div class="overview-label">理論↔詩文リンク</div></div>
  <div class="overview-card"><div class="overview-value">{quote_total}</div><div class="overview-label">原著引用</div></div>
  <div class="overview-card"><div class="overview-value">{motif_total}</div><div class="overview-label">モチーフ</div></div>
  <div class="overview-card"><div class="overview-value">12</div><div class="overview-label">サブフィールド</div></div>
  <div class="overview-card"><div class="overview-value">2,500</div><div class="overview-label">年代カバー</div></div>
</div>

<h2>第三層: 原著引用（concept_original_source）</h2>

<div class="layer-banner">
  <div class="layer-title">FOUNDING QUOTE LAYER — 概念の原典証跡</div>
  <div class="layer-desc">各概念がどの原著のどの一節で確立・定義されたかを示す{quote_total}件の引用層。Aristotle Poetics・Plato Republic・Bharata Natyashastra・Anandavardhana Dhvanyaloka・Liu Xie 文心雕龍・Zeami 風姿花伝・Mumyōshō・Shklovsky 'Art as Technique'・Bakhtin Dialogic Imagination・Genette Figures III・Ingarden Literary Work・Jauss Provocation・Iser Act of Reading・Lakoff-Johnson Metaphors We Live By・Derrida Of Grammatology・Kristeva Revolution in Poetic Language・Eliot Sacred Wood・Brooks-Wimsatt 等の原典から、概念の founding passage を原語＋訳＋意義分析として記録。</div>
</div>

<h3>引用が紐づいた主要研究者・著者</h3>
<div class="type-grid" id="quote-author-grid"></div>

<h3>原著言語分布</h3>
<div class="type-grid" id="quote-lang-grid"></div>

<h3>引用サンプル（25件）</h3>
<div id="quote-samples"></div>

<h2>第一層: 理論（概念・研究者）</h2>

<div class="layer-banner">
  <div class="layer-title">THEORY LAYER — 詩学理論の系譜</div>
  <div class="layer-desc">12サブフィールドにわたる詩学・文学理論・修辞学概念の系譜。プラトン／アリストテレスからシュクロフスキー、リクール、ジャンル、リファテール、ファイン、エコへ至る思考の連鎖。</div>
</div>

<h3>12サブフィールド構成</h3>
<p class="note">4つの大分類（A. 古典・修辞学的伝統、B. 形式主義・構造主義、C. 美学・現象学的伝統、D. 現代理論）に属する12のサブフィールド。</p>
<div id="subfield-container"></div>

<h3>時代別分布（理論層）</h3>
<div id="era-distribution"></div>

<h3>主要研究者（概念originator頻度順）</h3>
<div class="researcher-grid" id="researcher-grid"></div>

<h3>主要学派・思想流派</h3>
<div class="school-grid" id="school-grid"></div>

<h3>系譜関係の構成（{rel_total}件）</h3>
<div class="type-grid" id="relation-grid"></div>


<h2>第二層: 詩文（一次テクスト）</h2>

<div class="layer-banner">
  <div class="layer-title">PRIMARY TEXT LAYER — 分析対象としての詩</div>
  <div class="layer-desc">詩学が分析対象としてきた一次テクスト。古代ギリシャ・ローマ／中国古典／日本古典／中世・近代ヨーロッパ／サンスクリット／アラビア・ペルシア／仏典詩偈／アフリカ・先住民口承を横断する。各テクストはパブリックドメイン原典から取得し、<code>poetics_text</code>テーブルに格納。理論層の概念とは <code>poetics_text_concept_link</code> で双方向参照される。</div>
</div>

<h3>文化圏別の詩文分布</h3>
<div class="type-grid" id="text-culture-grid"></div>

<h3>時代別の詩文分布</h3>
<div id="text-era-distribution"></div>

<h3>形式・ジャンル分布</h3>
<div class="type-grid" id="text-form-grid"></div>

<h3>一次ソース・アーカイブ別</h3>
<div class="type-grid" id="text-archive-grid"></div>

<h3>例証として最も多くリンクされた概念</h3>
<p class="note">理論層の概念のうち、詩文層からの例証リンクが多いもの。理論×実例の接点が強い概念群。</p>
<div class="type-grid" id="text-toplinks-grid"></div>

<h3>モチーフ・カテゴリ分布</h3>
<div class="type-grid" id="text-motif-grid"></div>

<h3>文化圏ごとの代表的詩文（一部抜粋）</h3>
<p class="note">各文化圏から代表的な詩文を最大8件まで表示。完全リストはDB直接クエリ参照。</p>
<div id="text-samples"></div>

<footer>
  Poetics DB v2.0 &mdash; academic-knowledge-db / Insight News<br>
  {total_concepts} concepts · {researcher_total} researchers · {rel_total} relations · {text_total} primary texts · {link_total} text↔concept links · {motif_total} motifs<br>
  Last updated: 2026-05-07
</footer>

<script>
const sfData = {json.dumps(sf_data_js, ensure_ascii=False)};
const catColors = {{"A":"#CC1400","B":"#0066CC","C":"#996600","D":"#008844"}};
const catNames = {{"A":"A. 古典・修辞学的伝統","B":"B. 形式主義・構造主義","C":"C. 美学・現象学的伝統","D":"D. 現代理論・読者・認知・デジタル"}};
const sfContainer = document.getElementById('subfield-container');
const grouped = {{}};
sfData.forEach(s => {{ if(!grouped[s.cat]) grouped[s.cat]=[]; grouped[s.cat].push(s); }});
const maxSf = Math.max(...sfData.map(s=>s.count));
Object.keys(catNames).forEach(catId => {{
  const block = document.createElement('div');
  block.className = 'cat-block';
  block.innerHTML = `<div class="cat-header"><span class="cat-dot" style="background:${{catColors[catId]}}"></span>${{catNames[catId]}}</div>`;
  const grid = document.createElement('div');
  grid.className = 'subfield-grid';
  (grouped[catId]||[]).forEach(s => {{
    const el = document.createElement('div');
    el.className = 'subfield-item';
    el.innerHTML = `<div style="flex:1"><div class="subfield-name-ja">${{s.ja}}</div><div class="subfield-bar" style="width:${{s.count/maxSf*100}}%;background:${{catColors[s.cat]}}"></div></div><div class="subfield-count">${{s.count}}</div>`;
    grid.appendChild(el);
  }});
  block.appendChild(grid);
  sfContainer.appendChild(block);
}});

const eraData = {json.dumps(era_buckets_disp, ensure_ascii=False)};
const eraEl = document.getElementById('era-distribution');
const maxEra = Math.max(...eraData.map(d=>d[1]),1);
eraData.forEach(([label,cnt]) => {{
  const wrap = document.createElement('div');
  wrap.className = 'era-bar-row';
  wrap.innerHTML = `<div class="era-label">${{label}}</div><div class="era-bar" style="width:${{cnt/maxEra*70}}%"><span class="era-count">${{cnt}}</span></div>`;
  eraEl.appendChild(wrap);
}});

const researchers = {json.dumps([{"name": (nj or nf), "n": n} for nj, nf, n in researchers], ensure_ascii=False)};
const resGrid = document.getElementById('researcher-grid');
researchers.forEach(r => {{
  const el = document.createElement('div');
  el.className = 'researcher-item';
  el.innerHTML = `<span class="researcher-name">${{r.name}}</span><span class="researcher-meta">${{r.n}} concepts</span>`;
  resGrid.appendChild(el);
}});

const schools = {json.dumps([{"name": s, "n": n} for s, n in schools], ensure_ascii=False)};
const schoolGrid = document.getElementById('school-grid');
schools.forEach(s => {{
  const el = document.createElement('div');
  el.className = 'school-item';
  el.innerHTML = `<span>${{s.name}}</span><span class="type-count">${{s.n}}</span>`;
  schoolGrid.appendChild(el);
}});

const relTypes = {json.dumps([{"type": t, "n": n} for t, n in rel_types], ensure_ascii=False)};
const relMeta = {{
  "synthesizes":"統合","extends":"拡張","enables":"発展可能化","derived_from":"派生",
  "reinterprets":"再解釈","opposes":"対立","critiques":"批判","applies_to":"適用",
  "complements":"補完","related_to":"関連"
}};
const relGrid = document.getElementById('relation-grid');
relTypes.forEach(r => {{
  const ja = relMeta[r.type] || r.type;
  const el = document.createElement('div');
  el.className = 'type-item';
  el.innerHTML = `<span>${{ja}} <span style="font-size:0.7rem;color:var(--text-muted)">${{r.type}}</span></span><span class="type-count">${{r.n}}</span>`;
  relGrid.appendChild(el);
}});

// === Text layer rendering ===
function renderKVGrid(elId, items) {{
  const grid = document.getElementById(elId);
  if(!grid) return;
  items.forEach(([k, v]) => {{
    const el = document.createElement('div');
    el.className = 'type-item';
    el.innerHTML = `<span>${{k}}</span><span class="type-count">${{v}}</span>`;
    grid.appendChild(el);
  }});
}}

renderKVGrid('quote-author-grid', {json.dumps(top_quote_authors, ensure_ascii=False)});
renderKVGrid('quote-lang-grid', {json.dumps(quote_languages, ensure_ascii=False)});

const quoteSamples = {json.dumps(sample_quotes, ensure_ascii=False)};
const qsEl = document.getElementById('quote-samples');
quoteSamples.forEach(q => {{
  const el = document.createElement('div');
  el.className = 'text-item';
  const meta = [q.work, q.loc, q.author].filter(x=>x).join(' · ');
  el.innerHTML = `<div class="text-item-title">${{q.name}}</div><div class="text-item-meta">${{meta}}</div><div style="font-size:0.78rem;margin-top:4px;color:var(--text-secondary);font-family:var(--font-serif)">${{q.snip}}…</div>`;
  qsEl.appendChild(el);
}});

renderKVGrid('text-culture-grid', {json.dumps(text_by_culture, ensure_ascii=False)});
renderKVGrid('text-form-grid', {json.dumps(text_forms, ensure_ascii=False)});
renderKVGrid('text-archive-grid', {json.dumps(text_archives, ensure_ascii=False)});
renderKVGrid('text-toplinks-grid', {json.dumps(top_concept_links, ensure_ascii=False)});
renderKVGrid('text-motif-grid', {json.dumps(motif_cats, ensure_ascii=False)});

const textEraData = {json.dumps(text_era_buckets, ensure_ascii=False)};
const textEraEl = document.getElementById('text-era-distribution');
const maxTextEra = Math.max(...textEraData.map(d=>d[1]),1);
textEraData.forEach(([label,cnt]) => {{
  const wrap = document.createElement('div');
  wrap.className = 'era-bar-row';
  wrap.innerHTML = `<div class="era-label">${{label}}</div><div class="era-bar" style="width:${{cnt/maxTextEra*70}}%"><span class="era-count">${{cnt}}</span></div>`;
  textEraEl.appendChild(wrap);
}});

const textSamples = {json.dumps(text_samples_show, ensure_ascii=False)};
const textSamplesEl = document.getElementById('text-samples');
const cultureOrder = {json.dumps(CULTURE_ORDER, ensure_ascii=False)};
cultureOrder.forEach(cr => {{
  if (!textSamples[cr]) return;
  const block = document.createElement('div');
  block.className = 'culture-block';
  const header = document.createElement('div');
  header.className = 'culture-header';
  header.textContent = cr + '（' + textSamples[cr].length + '件抜粋）';
  block.appendChild(header);
  const list = document.createElement('div');
  list.className = 'text-list';
  textSamples[cr].forEach(t => {{
    const el = document.createElement('div');
    el.className = 'text-item';
    const meta = [t.author, t.era, t.form, t.src].filter(x=>x!=null).join(' · ');
    el.innerHTML = `<div class="text-item-title">${{t.title_ja}}</div><div class="text-item-meta">${{meta}}</div>`;
    list.appendChild(el);
  }});
  block.appendChild(list);
  textSamplesEl.appendChild(block);
}});
// Show any remaining cultures not in CULTURE_ORDER
Object.keys(textSamples).forEach(cr => {{
  if (cultureOrder.includes(cr)) return;
  const block = document.createElement('div');
  block.className = 'culture-block';
  const header = document.createElement('div');
  header.className = 'culture-header';
  header.textContent = cr + '（' + textSamples[cr].length + '件抜粋）';
  block.appendChild(header);
  const list = document.createElement('div');
  list.className = 'text-list';
  textSamples[cr].forEach(t => {{
    const el = document.createElement('div');
    el.className = 'text-item';
    const meta = [t.author, t.era, t.form, t.src].filter(x=>x!=null).join(' · ');
    el.innerHTML = `<div class="text-item-title">${{t.title_ja}}</div><div class="text-item-meta">${{meta}}</div>`;
    list.appendChild(el);
  }});
  block.appendChild(list);
  textSamplesEl.appendChild(block);
}});
</script>
</body></html>
"""

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size:,} bytes")
    print(f"Concepts: {total_concepts}, Researchers: {researcher_total}, Relations: {rel_total}")
    print(f"Texts: {text_total}, Links: {link_total}, Motifs: {motif_total}")
    conn.close()


if __name__ == "__main__":
    main()
