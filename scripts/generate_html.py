#!/usr/bin/env python3
"""
Generate static index.html from the academic knowledge database.
Reads all domain tables and produces a self-contained HTML page.
"""

import sqlite3
import html as html_mod
from pathlib import Path
from collections import defaultdict

DB_PATH = Path(__file__).parent.parent / "academic.db"
OUTPUT = Path(__file__).parent.parent / "index.html"

DOMAINS = [
    {"key": "humanities_concept", "label": "人文学", "color": "var(--accent-warm)", "color_class": "accent-warm"},
    {"key": "social_theory", "label": "社会科学", "color": "var(--blue)", "color_class": "blue"},
    {"key": "natural_discovery", "label": "自然科学", "color": "var(--green)", "color_class": "green"},
    {"key": "engineering_method", "label": "工学", "color": "var(--purple)", "color_class": "purple"},
    {"key": "arts_question", "label": "芸術", "color": "var(--orange)", "color_class": "orange"},
]


def esc(text):
    if not text:
        return ""
    return html_mod.escape(str(text))


def generate():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Gather stats
    total_entries = 0
    all_subfields = set()
    total_relations = 0

    domain_data = {}
    for d in DOMAINS:
        table = d["key"]
        entries = conn.execute(f"SELECT * FROM {table} ORDER BY subfield, era_start").fetchall()
        rel_count = conn.execute(f"SELECT COUNT(*) FROM {table}_relations").fetchone()[0]

        subfields = defaultdict(list)
        for e in entries:
            sf = e["subfield"] or "未分類"
            subfields[sf].append(dict(e))

        domain_data[table] = {
            "entries": entries,
            "count": len(entries),
            "subfields": subfields,
            "sf_count": len(subfields),
            "rel_count": rel_count,
        }
        total_entries += len(entries)
        all_subfields.update(subfields.keys())
        total_relations += rel_count

    # Cross-domain relations
    cross_rels = conn.execute("SELECT * FROM cross_domain_relations ORDER BY strength DESC").fetchall()

    conn.close()

    # Build HTML
    lines = []
    lines.append("""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>学術知識データベース | Insight News</title>
  <link rel="icon" href="https://esse-sense.com/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@400;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #FFFFFF; --card: #FFFFFF; --text: #121212; --text-secondary: #555555;
      --text-muted: #6B6B6B; --border: #D9D9D9; --border-light: #EEEEEE;
      --surface: #F7F7F5; --accent-warm: #CC1400; --accent-muted: rgba(204,20,0,0.06);
      --accent: #CC1400; --surface-alt: #F7F7F5;
      --font: "Noto Sans JP", sans-serif; --font-serif: "Noto Serif JP", serif;
      --green: #16A34A; --blue: #2563EB; --purple: #7C3AED; --orange: #EA580C; --cyan: #0891B2;
      --radius: 8px;
    }
    [data-theme="dark"] {
      --bg: #121212; --card: #1A1A1A; --text: #E0E0E0; --text-secondary: #AAAAAA;
      --text-muted: #8A8A8A; --border: #333333; --border-light: #2A2A2A;
      --surface: #1A1A1A; --surface-alt: #1A1A1A;
      --accent-warm: #FF4444; --accent: #FF4444; --accent-muted: rgba(255,68,68,0.1);
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: var(--font); color: var(--text); background: var(--bg); line-height: 1.7; max-width: 1100px; margin: 0 auto; padding: 24px 20px; }
    .back { display: inline-block; margin-bottom: 20px; font-size: 0.82rem; color: var(--text-secondary); text-decoration: none; }
    .back:hover { color: var(--text); }
    h1 { font-family: var(--font-serif); font-size: 1.5rem; font-weight: 700; margin-bottom: 4px; }
    .db-id { font-family: monospace; font-size: 0.72rem; font-weight: 700; color: var(--accent-warm); background: var(--accent-muted); padding: 2px 8px; margin-right: 8px; }
    .subtitle { font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 12px; }
    .desc { font-size: 0.84rem; color: var(--text); margin-bottom: 24px; line-height: 1.8; }
    .theme-toggle { position: fixed; top: 16px; right: 16px; background: var(--surface); border: 1px solid var(--border); padding: 6px 10px; cursor: pointer; font-size: 1rem; z-index: 100; }
    .overview { display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 10px; margin-bottom: 28px; }
    .overview-card { background: var(--surface); border: 1px solid var(--border-light); padding: 14px; text-align: center; }
    .overview-value { font-family: var(--font-serif); font-size: 1.3rem; font-weight: 700; }
    .overview-value.accent { color: var(--accent-warm); }
    .overview-label { font-size: 0.68rem; color: var(--text-muted); margin-top: 2px; }
    .search-box { display: flex; align-items: center; background: var(--surface); border: 1px solid var(--border); border-radius: 24px; padding: 6px 16px; gap: 8px; min-width: 240px; margin-bottom: 20px; }
    .search-box input { background: none; border: none; color: var(--text); font-family: var(--font); font-size: 0.88rem; outline: none; width: 100%; }
    .search-box input::placeholder { color: var(--text-muted); }
    .search-count { font-size: 0.72rem; background: var(--accent-muted); color: var(--accent-warm); padding: 2px 8px; border-radius: 12px; white-space: nowrap; }
    .tabs-wrapper { display: flex; gap: 0; border-bottom: 1px solid var(--border); margin-bottom: 24px; overflow-x: auto; }
    .tab-btn { background: none; border: none; border-bottom: 3px solid transparent; padding: 10px 16px; cursor: pointer; display: flex; align-items: center; gap: 6px; white-space: nowrap; font-family: var(--font); font-size: 0.84rem; color: var(--text-muted); transition: all 0.2s; }
    .tab-btn:hover { color: var(--tab-color, var(--accent-warm)); }
    .tab-btn.active { color: var(--tab-color, var(--accent-warm)); border-bottom-color: var(--tab-color, var(--accent-warm)); font-weight: 600; }
    .tab-count { font-size: 0.7rem; background: var(--surface); padding: 2px 8px; border-radius: 12px; }
    .tab-btn.active .tab-count { background: var(--tab-color, var(--accent-warm)); color: white; }
    .main { padding: 0; }
    .tab-content { display: none; }
    .tab-content.active { display: block; }
    .domain-header { padding: 14px 16px; margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; border-bottom: 1px solid var(--border); }
    .domain-title { font-family: var(--font-serif); font-size: 1rem; font-weight: 700; }
    .domain-stats { display: flex; gap: 16px; font-size: 0.78rem; color: var(--text-muted); }
    .stat-item strong { color: var(--text); }
    .subfield-block { border-bottom: 1px solid var(--border-light); }
    .subfield-summary { list-style: none; cursor: pointer; padding: 10px 16px; display: flex; align-items: center; gap: 10px; font-weight: 500; font-size: 0.88rem; }
    .subfield-summary::-webkit-details-marker { display: none; }
    .subfield-summary::before { content: "\\25B6"; font-size: 0.6rem; color: var(--text-muted); transition: transform 0.2s; }
    .subfield-block[open] > .subfield-summary::before { transform: rotate(90deg); }
    .sf-name { flex: 1; }
    .sf-count { font-size: 0.68rem; background: var(--accent-muted); color: var(--accent-warm); padding: 2px 8px; border-radius: 12px; font-weight: 600; }
    .subfield-entries { padding: 0 16px 10px 32px; }
    .entry-item { border-bottom: 1px solid var(--border-light); }
    .entry-item:last-child { border-bottom: none; }
    .entry-summary { list-style: none; cursor: pointer; padding: 6px 0; font-size: 0.84rem; color: var(--text); }
    .entry-summary::-webkit-details-marker { display: none; }
    .entry-body { padding: 4px 0 12px; }
    .entry-def { font-size: 0.82rem; color: var(--text-secondary); line-height: 1.7; }
    .entry-school { display: inline-block; font-size: 0.68rem; background: var(--surface); color: var(--text-muted); padding: 2px 8px; border-radius: 12px; margin-top: 4px; }
    .cross-section { padding: 24px 0; }
    .section-title { font-family: var(--font-serif); font-size: 1.2rem; font-weight: 700; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 1px solid var(--border); }
    .cross-table-wrapper { overflow-x: auto; border: 1px solid var(--border-light); }
    .cross-table { width: 100%; border-collapse: collapse; font-size: 0.82rem; }
    .cross-table th { background: var(--surface); padding: 6px 10px; text-align: left; font-weight: 600; font-size: 0.72rem; color: var(--text-muted); border-bottom: 1px solid var(--border); }
    .cross-table td { padding: 6px 10px; border-bottom: 1px solid var(--border-light); }
    .cross-table tr:hover td { background: var(--accent-muted); }
    .domain-badge { display: inline-block; font-size: 0.72rem; padding: 2px 8px; border-radius: 12px; color: white; white-space: nowrap; }
    .badge-humanities_concept { background: var(--accent-warm); }
    .badge-social_theory { background: var(--blue); }
    .badge-natural_discovery { background: var(--green); }
    .badge-engineering_method { background: var(--purple); }
    .badge-arts_question { background: var(--orange); }
    .search-hidden { display: none !important; }
    .search-match .entry-summary { background: var(--accent-muted); }
    @media (max-width: 640px) {
      .search-box { min-width: 100%; }
      .domain-header { flex-direction: column; align-items: flex-start; }
    }
  </style>
</head>
<body>
<button class="theme-toggle" onclick="document.documentElement.dataset.theme=document.documentElement.dataset.theme==='dark'?'':'dark'">&#9790;</button>
<a class="back" href="https://yuyanishimura0312.github.io/miratuku-news-v2/databases.html">&larr; データベース一覧に戻る</a>
""")

    # Header
    lines.append(f'<h1><span class="db-id">AK</span>学術知識データベース</h1>')
    lines.append(f'<p class="subtitle">Academic Knowledge Database &mdash; 5分野の学術知識を体系的に構造化</p>')
    lines.append(f'<p class="desc">人文学・社会科学・自然科学・工学・芸術の5分野にわたる学術的概念・理論・発見・手法を体系的に収集し、定義・系譜関係・分野横断接続を構造化したデータベース。</p>')

    # Overview
    lines.append(f'''<div class="overview">
  <div class="overview-card"><div class="overview-value">{total_entries:,}</div><div class="overview-label">総エントリ</div></div>
  <div class="overview-card"><div class="overview-value">{len(all_subfields)}</div><div class="overview-label">サブフィールド</div></div>
  <div class="overview-card"><div class="overview-value">{total_relations:,}</div><div class="overview-label">系譜関係</div></div>
  <div class="overview-card"><div class="overview-value">{len(cross_rels)}</div><div class="overview-label">分野横断関係</div></div>
  <div class="overview-card"><div class="overview-value">5</div><div class="overview-label">分野</div></div>
</div>''')

    # Search
    lines.append('''<div class="search-box">
  <input type="text" id="searchInput" placeholder="概念名・定義を検索..." autocomplete="off">
  <span class="search-count" id="searchCount"></span>
</div>''')

    # Tabs
    lines.append('<div class="tabs-wrapper">')
    for i, d in enumerate(DOMAINS):
        active = " active" if i == 0 else ""
        cnt = domain_data[d["key"]]["count"]
        lines.append(f'  <button class="tab-btn{active}" data-tab="{d["key"]}" style="--tab-color:{d["color"]}">{d["label"]} <span class="tab-count">{cnt}</span></button>')
    lines.append(f'  <button class="tab-btn" data-tab="cross" style="--tab-color:var(--text-muted)">分野横断 <span class="tab-count">{len(cross_rels)}</span></button>')
    lines.append('</div>')

    # Main content
    lines.append('<main class="main">')

    for i, d in enumerate(DOMAINS):
        table = d["key"]
        dd = domain_data[table]
        active = " active" if i == 0 else ""

        lines.append(f'  <div class="tab-content{active}" id="tab-{table}">')
        lines.append(f'    <div class="domain-header">')
        lines.append(f'      <h2 class="domain-title">{d["label"]}</h2>')
        lines.append(f'      <div class="domain-stats">')
        lines.append(f'        <span class="stat-item"><strong>{dd["count"]}</strong> エントリ</span>')
        lines.append(f'        <span class="stat-item"><strong>{dd["sf_count"]}</strong> サブフィールド</span>')
        lines.append(f'        <span class="stat-item"><strong>{dd["rel_count"]}</strong> 系譜関係</span>')
        lines.append(f'      </div>')
        lines.append(f'    </div>')
        lines.append(f'    <div class="subfields-container">')

        # Sort subfields by count (descending)
        sorted_sfs = sorted(dd["subfields"].items(), key=lambda x: -len(x[1]))

        for sf_name, entries in sorted_sfs:
            count = len(entries)
            lines.append(f'      <details class="subfield-block">')
            lines.append(f'        <summary class="subfield-summary" style="--sf-color:{d["color"]}">')
            lines.append(f'          <span class="sf-name">{esc(sf_name)}</span>')
            lines.append(f'          <span class="sf-count">{count}件</span>')
            lines.append(f'        </summary>')
            lines.append(f'        <div class="subfield-entries">')

            for e in entries:
                name_ja = esc(e.get("name_ja", ""))
                name_en = esc(e.get("name_en", ""))
                era_start = e.get("era_start", "")
                era_end = e.get("era_end", "")
                definition = esc(e.get("definition", ""))
                school = esc(e.get("school_of_thought", ""))

                era_str = f"{era_start}年" if era_start else ""
                if era_end:
                    era_str += f"〜{era_end}年"
                elif era_start:
                    era_str += "〜"

                title = f"{name_ja}"
                if name_en:
                    title += f" ({name_en})"
                if era_str:
                    title += f" — {era_str}"

                lines.append(f'          <details class="entry-item">')
                lines.append(f'            <summary class="entry-summary">{title}</summary>')
                lines.append(f'            <div class="entry-body">')
                if definition:
                    lines.append(f'              <p class="entry-def">{definition}</p>')
                if school:
                    lines.append(f'              <span class="entry-school">{school}</span>')
                lines.append(f'            </div>')
                lines.append(f'          </details>')

            lines.append(f'        </div>')
            lines.append(f'      </details>')

        lines.append(f'    </div>')
        lines.append(f'  </div>')

    # Cross-domain tab
    lines.append(f'  <div class="tab-content" id="tab-cross">')
    lines.append(f'    <div class="cross-section">')
    lines.append(f'      <h2 class="section-title">分野横断関係 ({len(cross_rels)}件)</h2>')
    if cross_rels:
        lines.append(f'      <div class="cross-table-wrapper"><table class="cross-table"><thead><tr>')
        lines.append(f'        <th>起点</th><th>関係</th><th>終点</th><th>強度</th>')
        lines.append(f'      </tr></thead><tbody>')
        for r in cross_rels:
            sd = esc(r["source_domain"])
            td = esc(r["target_domain"])
            rt = esc(r["relation_type"])
            st = r["strength"]
            desc = esc(r["relation_description"] if r["relation_description"] else "")
            lines.append(f'        <tr><td><span class="domain-badge badge-{sd}">{sd}</span></td>')
            lines.append(f'        <td class="rel-type">{rt}</td>')
            lines.append(f'        <td><span class="domain-badge badge-{td}">{td}</span></td>')
            lines.append(f'        <td class="rel-strength">{st}</td></tr>')
        lines.append(f'      </tbody></table></div>')
    lines.append(f'    </div>')
    lines.append(f'  </div>')

    lines.append('</main>')

    # JavaScript
    lines.append("""
<script>
// Tab switching
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
    const tab = btn.dataset.tab;
    document.getElementById('tab-' + tab).classList.add('active');
  });
});

// Search
const searchInput = document.getElementById('searchInput');
const searchCount = document.getElementById('searchCount');
let debounce;
searchInput.addEventListener('input', () => {
  clearTimeout(debounce);
  debounce = setTimeout(() => {
    const q = searchInput.value.toLowerCase().trim();
    let count = 0;
    document.querySelectorAll('.entry-item').forEach(item => {
      const text = item.textContent.toLowerCase();
      if (!q || text.includes(q)) {
        item.classList.remove('search-hidden');
        if (q) { item.classList.add('search-match'); count++; }
        else item.classList.remove('search-match');
      } else {
        item.classList.add('search-hidden');
        item.classList.remove('search-match');
      }
    });
    document.querySelectorAll('.subfield-block').forEach(block => {
      const visible = block.querySelectorAll('.entry-item:not(.search-hidden)').length;
      if (q && visible === 0) block.classList.add('search-hidden');
      else { block.classList.remove('search-hidden'); if (q && visible > 0) block.open = true; }
    });
    searchCount.textContent = q ? count + '件' : '';
  }, 200);
});
</script>
</body>
</html>""")

    html_content = "\n".join(lines)
    OUTPUT.write_text(html_content, encoding="utf-8")
    print(f"Generated: {OUTPUT}")
    print(f"Size: {len(html_content):,} bytes")
    print(f"Entries: {total_entries:,}, Subfields: {len(all_subfields)}, Relations: {total_relations:,}")


if __name__ == "__main__":
    generate()
