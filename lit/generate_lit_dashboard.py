"""
LIT-DB Phase 5 Dashboard Generator

Generates lit.html (overview dashboard) following the textbook.html structure +
赤白CI (#CC1400) design system, per ~/.claude/rules/db-design-system.md.

Outputs:
    ~/projects/apps/miratuku-news-v2/dashboards/lit.html

Run after Phase 2-4 completion. Reads lit.sqlite and emits a single HTML file
with sidebar TOC, 24-subfield browse, fourth-transformation tag analysis,
and cross-domain link graphs.

Usage:
    python generate_lit_dashboard.py [--output PATH]
"""

from __future__ import annotations

import argparse
import sqlite3
from datetime import date
from html import escape
from pathlib import Path

DB_PATH = Path(__file__).parent / "lit.sqlite"
DEFAULT_OUTPUT = Path.home() / "projects/apps/miratuku-news-v2/dashboards/lit.html"


# CSS follows ~/.claude/rules/db-design-system.md exactly
CSS = """
:root {
  --bg: #FFFFFF; --card: #FFFFFF; --card-hover: #F7F7F5;
  --accent: #121212; --accent-soft: #555555;
  --accent-warm: #CC1400; --accent-warm-soft: #B01200;
  --accent-muted: rgba(204,20,0,0.06);
  --text: #121212; --text-secondary: #555555; --text-muted: #6B6B6B;
  --border: #D9D9D9; --border-light: #EEEEEE;
  --highlight: #CC1400; --surface: #F7F7F5;
  --font: "Noto Sans JP", "Hiragino Sans", -apple-system, sans-serif;
  --font-serif: "Noto Serif JP", "Hiragino Mincho ProN", Georgia, serif;
}
[data-theme="dark"] {
  --bg: #121212; --card: #1A1A1A; --card-hover: #222222;
  --accent: #E0E0E0; --accent-warm: #FF4030; --accent-light: #1A1A1A;
  --accent-muted: rgba(255,64,48,0.10);
  --text: #E0E0E0; --text-secondary: #AAAAAA; --text-muted: #8A8A8A;
  --border: #333333; --border-light: #2A2A2A;
  --highlight: #FF4030; --surface: #1A1A1A;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: var(--font); background: var(--bg); color: var(--text); line-height: 1.85; letter-spacing: 0.025em; font-feature-settings: "palt"; }
.top-bar { position: fixed; top: 0; left: 0; right: 0; height: 48px; background: var(--bg); border-top: 3px solid #121212; border-bottom: 1px solid var(--border-light); display: flex; align-items: center; justify-content: space-between; padding: 0 24px; z-index: 100; }
.brand { font-weight: 600; color: var(--accent-warm); font-size: 14px; letter-spacing: 0.05em; }
.theme-toggle { background: none; border: 1px solid var(--border); padding: 4px 12px; cursor: pointer; color: var(--text-secondary); font-size: 12px; }
.layout { display: flex; padding-top: 48px; min-height: 100vh; }
.toc-sidebar { width: 260px; border-right: 1px solid var(--border-light); padding: 32px 24px; position: fixed; top: 48px; bottom: 0; overflow-y: auto; font-size: 13px; }
.toc-sidebar h3 { font-size: 11px; text-transform: uppercase; color: var(--text-muted); margin-bottom: 12px; letter-spacing: 0.1em; }
.toc-sidebar ol { list-style: none; counter-reset: ch; }
.toc-sidebar ol li { counter-increment: ch; margin-bottom: 8px; }
.toc-sidebar ol li::before { content: counter(ch, decimal-leading-zero) " "; color: var(--text-muted); font-family: "SF Mono", "Fira Code", monospace; font-size: 11px; }
.toc-sidebar a { color: var(--text-secondary); text-decoration: none; }
.toc-sidebar a:hover { color: var(--accent-warm); }
.main { margin-left: 260px; padding: 64px 80px; max-width: 980px; }
.main h1 { font-family: var(--font-serif); font-size: 32px; font-weight: 600; margin-bottom: 8px; }
.main h2 { font-family: var(--font-serif); font-size: 22px; font-weight: 600; margin-top: 64px; margin-bottom: 24px; padding-bottom: 12px; border-bottom: 1px solid var(--border-light); }
.main h3 { font-family: var(--font-serif); font-size: 17px; font-weight: 600; margin-top: 32px; margin-bottom: 12px; }
.chapter-section { margin-bottom: 80px; padding-bottom: 24px; border-bottom: 1px solid var(--border-light); }
.lead { font-family: var(--font-serif); font-size: 15px; color: var(--text-secondary); margin-bottom: 24px; max-width: 720px; }
.main p { font-family: var(--font-serif); margin-bottom: 16px; max-width: 740px; text-indent: 1em; }
.main p:first-of-type { text-indent: 0; }
.metric-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin: 24px 0; }
.metric { padding: 20px; border: 1px solid var(--border-light); background: var(--card); }
.metric-value { font-size: 28px; font-weight: 700; color: var(--accent-warm); font-family: "SF Mono", monospace; }
.metric-label { font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 4px; }
table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 13px; }
table th, table td { padding: 8px 12px; border-bottom: 1px solid var(--border-light); text-align: left; }
table th { font-weight: 600; color: var(--text-secondary); font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; background: var(--surface); }
table tr:hover { background: var(--card-hover); }
.tag { display: inline-block; padding: 2px 8px; font-size: 11px; border: 1px solid var(--accent-warm); color: var(--accent-warm); margin-right: 4px; }
@media (max-width: 1000px) {
  .toc-sidebar { position: static; width: 100%; height: auto; border-right: none; border-bottom: 1px solid var(--border-light); }
  .main { margin-left: 0; padding: 32px 24px; }
}
@media print {
  .toc-sidebar, .top-bar, .theme-toggle { display: none; }
  .main { margin-left: 0; padding: 0; }
}
"""


JS = """
const t = document.documentElement;
const saved = localStorage.getItem('lit-theme');
if (saved) t.setAttribute('data-theme', saved);
document.querySelector('.theme-toggle').addEventListener('click', () => {
  const cur = t.getAttribute('data-theme') === 'dark' ? null : 'dark';
  if (cur) { t.setAttribute('data-theme', cur); localStorage.setItem('lit-theme', cur); }
  else { t.removeAttribute('data-theme'); localStorage.removeItem('lit-theme'); }
});
"""


def fetch_metrics(conn: sqlite3.Connection) -> dict:
    cur = conn.cursor()
    counts = {}
    for tbl in ["concepts", "authors", "works", "movements", "relations", "cross_domain", "fourth_transform_tags"]:
        cur.execute(f"SELECT COUNT(*) FROM {tbl}")
        counts[tbl] = cur.fetchone()[0]

    cur.execute(
        """SELECT s.code, s.name_ja, s.macro_region, s.target_concepts,
                  COUNT(c.id) AS actual
           FROM subfields s LEFT JOIN concepts c ON c.subfield_id=s.id
           GROUP BY s.id ORDER BY s.id"""
    )
    subfield_rows = [dict(r) for r in cur.fetchall()]

    cur.execute(
        """SELECT axis, COUNT(*) AS cnt
           FROM fourth_transform_tags GROUP BY axis ORDER BY cnt DESC"""
    )
    axis_rows = [dict(r) for r in cur.fetchall()]

    cur.execute(
        """SELECT target_db, COUNT(*) AS cnt
           FROM cross_domain GROUP BY target_db ORDER BY cnt DESC"""
    )
    cross_rows = [dict(r) for r in cur.fetchall()]

    cur.execute(
        """SELECT s.macro_region, COUNT(c.id) AS cnt, SUM(s.target_concepts) AS tgt
           FROM subfields s LEFT JOIN concepts c ON c.subfield_id=s.id
           GROUP BY s.macro_region"""
    )
    region_rows = [dict(r) for r in cur.fetchall()]

    return {
        "counts": counts,
        "subfields": subfield_rows,
        "axes": axis_rows,
        "cross_domain": cross_rows,
        "regions": region_rows,
        "build_date": date.today().isoformat(),
    }


def render(metrics: dict) -> str:
    c = metrics["counts"]
    sfs = metrics["subfields"]
    axes = metrics["axes"]
    cross = metrics["cross_domain"]
    regions = metrics["regions"]

    sf_rows = "".join(
        f"<tr><td>{escape(s['code'])}</td><td>{escape(s['name_ja'])}</td>"
        f"<td>{escape(s['macro_region'])}</td>"
        f"<td>{s['actual']}</td><td>{s['target_concepts']}</td>"
        f"<td>{(s['actual']/s['target_concepts']*100 if s['target_concepts'] else 0):.0f}%</td></tr>"
        for s in sfs
    )

    axis_rows = "".join(
        f"<tr><td>{escape(a['axis'])}</td><td>{a['cnt']}</td></tr>" for a in axes
    )

    cross_rows = "".join(
        f"<tr><td>{escape(c2['target_db'])}</td><td>{c2['cnt']}</td></tr>" for c2 in cross
    )

    region_rows = "".join(
        f"<tr><td>{escape(r['macro_region'])}</td><td>{r['cnt']}</td>"
        f"<td>{r['tgt']}</td><td>{(r['cnt']/r['tgt']*100 if r['tgt'] else 0):.0f}%</td></tr>"
        for r in regions
    )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LIT-DB | 文学学術知識DB</title>
<link rel="icon" href="https://esse-sense.com/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600&family=Noto+Serif+JP:wght@400;600&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="top-bar">
  <div class="brand">LIT-DB / 文学学術知識DB</div>
  <button class="theme-toggle">DARK</button>
</div>
<div class="layout">
  <nav class="toc-sidebar">
    <h3>CONTENTS</h3>
    <ol>
      <li><a href="#overview">概要</a></li>
      <li><a href="#metrics">主要指標</a></li>
      <li><a href="#regions">地域別カバレッジ</a></li>
      <li><a href="#subfields">24サブフィールド</a></li>
      <li><a href="#fourth">第四変容9軸</a></li>
      <li><a href="#cross">他DBクロスドメイン</a></li>
      <li><a href="#about">プロジェクトについて</a></li>
    </ol>
  </nav>
  <main class="main">
    <h1>文学学術知識DB</h1>
    <p class="lead">枢軸時代→ルネサンス→産業革命→第四変容（AI社会）の今、文学が積み上げた概念を地域横断で再構造化するDB。西欧中心主義を解体し、東洋・非西欧圏の文学伝統を対等な知的遺産として収録する。</p>

    <section class="chapter-section" id="overview">
      <h2>概要</h2>
      <p>本データベースは、24サブフィールド・11,000概念規模で、文学概念・作家・作品・運動・地域伝統の系譜を構造化する。Poetics DB（PT、詩学理論1,121概念）の上位包含層として作品・作家・運動を扱い、AI時代における作者性・創造性・物語・主体・正典・受容・翻訳・真正性・言語の9軸再考を全概念に紐づける。</p>
      <p>非西欧領域に68.2%の規模配分を割り当て、西欧中心主義の構造的回避を設計に内在化させた。一次資料（Perseus、CTEXT、青空文庫、GRETIL、Al-Shamela、ELO等）からの直接取得を原則とし、source_tier カラムでハルシネーション抑止を強制する。</p>
    </section>

    <section class="chapter-section" id="metrics">
      <h2>主要指標</h2>
      <div class="metric-grid">
        <div class="metric"><div class="metric-value">{c['concepts']:,}</div><div class="metric-label">concepts</div></div>
        <div class="metric"><div class="metric-value">{c['authors']:,}</div><div class="metric-label">authors</div></div>
        <div class="metric"><div class="metric-value">{c['works']:,}</div><div class="metric-label">works</div></div>
        <div class="metric"><div class="metric-value">{c['movements']:,}</div><div class="metric-label">movements</div></div>
        <div class="metric"><div class="metric-value">{c['relations']:,}</div><div class="metric-label">relations</div></div>
        <div class="metric"><div class="metric-value">{c['cross_domain']:,}</div><div class="metric-label">cross-domain</div></div>
        <div class="metric"><div class="metric-value">{c['fourth_transform_tags']:,}</div><div class="metric-label">4th transform tags</div></div>
      </div>
    </section>

    <section class="chapter-section" id="regions">
      <h2>地域別カバレッジ</h2>
      <p>マクロ地域ごとの収集規模と目標達成率。非西欧（東アジア・南西アジア・グローバルサウス・周縁横断）が西欧を上回る配分で、文学の知的遺産を西欧中心主義から解放する設計を保つ。</p>
      <table>
        <thead><tr><th>マクロ地域</th><th>収集</th><th>目標</th><th>達成率</th></tr></thead>
        <tbody>{region_rows}</tbody>
      </table>
    </section>

    <section class="chapter-section" id="subfields">
      <h2>24サブフィールド一覧</h2>
      <table>
        <thead><tr><th>code</th><th>名称</th><th>地域</th><th>収集</th><th>目標</th><th>進捗</th></tr></thead>
        <tbody>{sf_rows}</tbody>
      </table>
    </section>

    <section class="chapter-section" id="fourth">
      <h2>第四変容9軸</h2>
      <p>AI時代における文学概念の問い直しを9軸で構造化する。各軸の概念数は、その軸が今まさに再考されている領域の密度を示す。生成AIによる作者性・創造性・物語・主体の根本的問い直しを、文学が積み上げた歴史的厚みで受け止める基盤として機能する。</p>
      <table>
        <thead><tr><th>軸</th><th>該当概念数</th></tr></thead>
        <tbody>{axis_rows}</tbody>
      </table>
    </section>

    <section class="chapter-section" id="cross">
      <h2>他DBクロスドメイン接続</h2>
      <p>文学概念は哲学（PHIL-DB）、人類学（AN-DB）、詩学（PT-DB）、経営学（MG-DB）、歴史人物（Era-Talents）等と深く接続する。本DBは独立DBであるが、クロスドメインリンクを通じて学術知識基盤全体の接続を担う。</p>
      <table>
        <thead><tr><th>接続先DB</th><th>リンク数</th></tr></thead>
        <tbody>{cross_rows}</tbody>
      </table>
    </section>

    <section class="chapter-section" id="about">
      <h2>プロジェクトについて</h2>
      <p>本DBは2026年5月に着工された。実行チーム標準体制（academic-db-builder + Codex 40名）で、7段階フェーズ（スコーピング→調査設計→収集→検証→関係性構築→ダッシュボード→公開）を踏む。最終公開は西村勇也（NPO法人ミラツク代表）の承認後、Foresight Knowledge Baseの一部として公開される。</p>
      <p style="font-size: 11px; color: var(--text-muted); margin-top: 32px;">最終更新: {metrics['build_date']}</p>
    </section>
  </main>
</div>
<script>{JS}</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        m = fetch_metrics(conn)
    finally:
        conn.close()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(m), encoding="utf-8")
    print(f"wrote {args.output}")
    print(f"  concepts={m['counts']['concepts']} subfields={len(m['subfields'])}")


if __name__ == "__main__":
    main()
