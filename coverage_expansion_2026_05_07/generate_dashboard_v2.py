#!/usr/bin/env python3
"""新ダッシュボード生成: textbook style + 赤白CI

出力: academic-knowledge-db/index.html, miratuku-news-v2/dashboards/ak.html
"""
from __future__ import annotations
import json
import sqlite3
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent  # academic-knowledge-db
DB = REPO_ROOT / "academic.db"
SITE_OUT = REPO_ROOT / "index.html"
DASHBOARD_OUT = Path("/Users/nishimura+/projects/apps/miratuku-news-v2/dashboards/ak.html")

DOMAINS = [
    ("humanities_concept", "人文学", "humanities-color"),
    ("social_theory", "社会科学", "social-color"),
    ("natural_discovery", "自然科学", "natural-color"),
    ("engineering_method", "工学", "engineering-color"),
    ("arts_question", "芸術・デザイン", "arts-color"),
]


def collect_data():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    data = {"domains": {}, "totals": {}, "era": {}, "researchers": {}}

    for tbl, label, color in DOMAINS:
        rows = conn.execute(f"SELECT subfield, COUNT(*) c FROM {tbl} GROUP BY subfield ORDER BY c DESC").fetchall()
        subfields = [(r["subfield"], r["c"]) for r in rows]
        total = sum(c for _, c in subfields)
        recent = conn.execute(f"SELECT COUNT(*) FROM {tbl} WHERE era_start >= 2015").fetchone()[0]

        # Era distribution
        eras = conn.execute(f"""
            SELECT
                CASE
                    WHEN era_start < 1900 THEN 'Pre-1900'
                    WHEN era_start < 1960 THEN '1900-1959'
                    WHEN era_start < 1985 THEN '1960-1984'
                    WHEN era_start < 2000 THEN '1985-1999'
                    WHEN era_start < 2015 THEN '2000-2014'
                    ELSE '2015-'
                END as era,
                COUNT(*) c
            FROM {tbl} WHERE era_start IS NOT NULL
            GROUP BY era ORDER BY MIN(era_start)
        """).fetchall()

        # Top researchers (extract from JSON-like strings)
        researchers_raw = conn.execute(f"SELECT key_researchers FROM {tbl} WHERE key_researchers IS NOT NULL LIMIT 500").fetchall() if "key_researchers" in [c[1] for c in conn.execute(f"PRAGMA table_info({tbl})").fetchall()] else []

        data["domains"][tbl] = {
            "label": label, "color": color, "total": total,
            "subfields": subfields,
            "era": [(r["era"], r["c"]) for r in eras],
            "recent_2015": recent,
            "recent_pct": round(recent / total * 100, 1) if total else 0,
        }

    # Total stats
    data["totals"] = {
        "concepts": sum(d["total"] for d in data["domains"].values()),
        "relations_intra": sum(conn.execute(f"SELECT COUNT(*) FROM {tbl}_relations").fetchone()[0] for tbl, _, _ in DOMAINS),
        "relations_cross": conn.execute("SELECT COUNT(*) FROM cross_domain_relations").fetchone()[0],
        "subfields_total": sum(len(d["subfields"]) for d in data["domains"].values()),
    }
    data["totals"]["relations_total"] = data["totals"]["relations_intra"] + data["totals"]["relations_cross"]
    data["totals"]["recent_2015_total"] = sum(d["recent_2015"] for d in data["domains"].values())
    data["totals"]["recent_pct"] = round(data["totals"]["recent_2015_total"] / data["totals"]["concepts"] * 100, 1)

    conn.close()
    return data


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ja" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>学術知識データベース | Academic Knowledge DB</title>
<link rel="icon" href="https://esse-sense.com/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@400;600;700&family=Fira+Code&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #FFFFFF; --card: #FFFFFF; --card-hover: #F7F7F5;
  --accent: #121212; --accent-soft: #555555;
  --accent-warm: #CC1400; --accent-warm-soft: #B01200; --accent-muted: rgba(204,20,0,0.06);
  --text: #121212; --text-secondary: #555555; --text-muted: #6B6B6B;
  --border: #D9D9D9; --border-light: #EEEEEE;
  --highlight: #CC1400; --surface: #F7F7F5;
  --font: "Noto Sans JP", "Hiragino Sans", -apple-system, sans-serif;
  --font-serif: "Noto Serif JP", "Hiragino Mincho ProN", Georgia, serif;
  --font-mono: "Fira Code", SFMono-Regular, Menlo, monospace;
}}
[data-theme="dark"] {{
  --bg: #121212; --card: #1A1A1A; --card-hover: #222222;
  --accent: #E0E0E0; --accent-soft: #999999;
  --accent-warm: #FF4030; --accent-warm-soft: #FF6050; --accent-muted: rgba(255,64,48,0.10);
  --text: #E0E0E0; --text-secondary: #AAAAAA; --text-muted: #8A8A8A;
  --border: #333333; --border-light: #2A2A2A;
  --highlight: #FF4030; --surface: #1A1A1A;
}}
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ font-size: 16px; scroll-behavior: smooth; -webkit-font-smoothing: antialiased; }}
body {{
  font-family: var(--font); color: var(--text); background: var(--bg);
  line-height: 1.85; letter-spacing: 0.025em; font-feature-settings: "palt";
  min-height: 100vh; transition: background 0.2s, color 0.2s;
}}
a {{ color: var(--accent-warm); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}

.top-bar {{
  background: var(--bg); border-top: 3px solid var(--accent);
  border-bottom: 1px solid var(--border); padding: 0 24px;
  display: flex; align-items: center; justify-content: space-between;
  height: 48px; position: sticky; top: 0; z-index: 100;
}}
.top-bar-brand {{
  font-family: var(--font); font-size: 0.75rem; font-weight: 700;
  letter-spacing: 0.1em; text-transform: uppercase; color: var(--text-muted);
}}
.top-bar-brand span {{ color: var(--accent-warm); }}
.theme-toggle {{
  background: none; border: 1px solid var(--border); color: var(--text-muted);
  cursor: pointer; padding: 4px 10px; font-size: 0.72rem; font-family: var(--font);
  letter-spacing: 0.05em; transition: all 0.2s;
}}
.theme-toggle:hover {{ border-color: var(--accent-warm); color: var(--accent-warm); }}

.book-layout {{
  display: grid; grid-template-columns: 240px 1fr;
  max-width: 1200px; margin: 0 auto; padding: 0 24px;
}}
.toc-sidebar {{
  position: sticky; top: 48px; height: calc(100vh - 48px); overflow-y: auto;
  padding: 32px 16px 32px 0; border-right: 1px solid var(--border-light);
}}
.toc-title {{
  font-family: var(--font); font-size: 0.65rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.15em;
  color: var(--text-muted); padding: 0 12px 12px; border-bottom: 1px solid var(--border-light); margin-bottom: 12px;
}}
.toc a {{
  display: block; padding: 6px 12px; font-family: var(--font);
  font-size: 0.78rem; color: var(--text-secondary);
  border-left: 2px solid transparent; transition: all 0.15s;
}}
.toc a:hover {{ color: var(--accent-warm); border-left-color: var(--accent-warm); background: var(--accent-muted); text-decoration: none; }}
.toc-num {{ font-family: var(--font-mono); font-size: 0.7rem; color: var(--text-muted); margin-right: 8px; }}

.main {{ padding: 32px 0 32px 32px; max-width: 760px; }}
.hero {{
  margin-bottom: 56px; padding-bottom: 48px; border-bottom: 1px solid var(--border-light);
}}
.hero-title {{
  font-family: var(--font-serif); font-size: 2.0rem; font-weight: 700;
  letter-spacing: 0.04em; line-height: 1.5; color: var(--text);
  margin-bottom: 12px;
}}
.hero-subtitle {{
  font-family: var(--font); font-size: 0.85rem; color: var(--text-muted);
  letter-spacing: 0.08em; text-transform: uppercase;
}}
.hero-lead {{
  font-family: var(--font-serif); font-size: 1.0rem; color: var(--text-secondary);
  margin-top: 24px; line-height: 1.95;
}}

.stat-grid {{
  display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1px; background: var(--border-light); border: 1px solid var(--border-light); margin: 32px 0;
}}
.stat {{
  background: var(--bg); padding: 18px 16px; text-align: center;
}}
.stat-value {{
  font-family: var(--font-serif); font-size: 1.6rem; font-weight: 700;
  color: var(--accent-warm); line-height: 1.1;
}}
.stat-label {{
  font-family: var(--font); font-size: 0.7rem; color: var(--text-muted);
  margin-top: 4px; letter-spacing: 0.05em;
}}

.chapter {{ margin: 48px 0 64px; padding-bottom: 32px; border-bottom: 1px solid var(--border-light); }}
.chapter:last-child {{ border-bottom: 0; }}
.chapter-num {{
  font-family: var(--font-mono); font-size: 0.7rem; color: var(--accent-warm);
  letter-spacing: 0.2em; text-transform: uppercase;
}}
.chapter-title {{
  font-family: var(--font-serif); font-size: 1.4rem; font-weight: 700;
  letter-spacing: 0.04em; color: var(--text); margin: 8px 0 24px;
}}
.chapter p {{
  font-family: var(--font-serif); font-size: 0.92rem; color: var(--text-secondary);
  line-height: 1.95; text-indent: 1em; margin-bottom: 16px;
}}
.chapter p:first-of-type {{ text-indent: 0; }}

.domain-card {{
  background: var(--surface); border: 1px solid var(--border-light);
  padding: 20px 24px; margin: 16px 0;
}}
.domain-header {{
  display: flex; justify-content: space-between; align-items: baseline;
  margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid var(--border-light);
}}
.domain-name {{
  font-family: var(--font-serif); font-size: 1.05rem; font-weight: 700;
  color: var(--text);
}}
.domain-count {{
  font-family: var(--font-mono); font-size: 0.95rem; color: var(--accent-warm); font-weight: 700;
}}
.domain-meta {{
  font-family: var(--font); font-size: 0.72rem; color: var(--text-muted);
  margin-bottom: 12px;
}}
.subfield-bars {{ display: grid; gap: 4px; margin-top: 12px; }}
.subfield-bar {{ display: grid; grid-template-columns: 1fr auto 60px; gap: 8px; align-items: center; font-size: 0.78rem; }}
.subfield-bar .name {{ font-family: var(--font); color: var(--text-secondary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.subfield-bar .count {{ font-family: var(--font-mono); color: var(--text-muted); font-size: 0.72rem; text-align: right; min-width: 44px; }}
.subfield-bar .bar-fill {{ height: 8px; background: var(--accent-warm); border-radius: 1px; }}

.era-grid {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 1px; background: var(--border-light); border: 1px solid var(--border-light); margin: 16px 0; }}
.era-cell {{ background: var(--bg); padding: 10px 8px; text-align: center; }}
.era-label {{ font-family: var(--font); font-size: 0.62rem; color: var(--text-muted); }}
.era-value {{ font-family: var(--font-mono); font-size: 0.95rem; color: var(--text); font-weight: 700; }}
.era-pct {{ font-family: var(--font); font-size: 0.62rem; color: var(--accent-warm); }}

.timeline {{ margin: 24px 0; padding-left: 16px; border-left: 2px solid var(--border); }}
.timeline-item {{ margin: 16px 0; position: relative; }}
.timeline-item::before {{
  content: ""; position: absolute; left: -22px; top: 6px; width: 8px; height: 8px;
  background: var(--accent-warm); border-radius: 50%;
}}
.timeline-date {{ font-family: var(--font-mono); font-size: 0.7rem; color: var(--accent-warm); letter-spacing: 0.1em; }}
.timeline-title {{ font-family: var(--font-serif); font-size: 0.92rem; font-weight: 700; color: var(--text); margin: 4px 0; }}
.timeline-desc {{ font-family: var(--font); font-size: 0.78rem; color: var(--text-secondary); }}

footer {{
  margin-top: 64px; padding: 32px 0; border-top: 1px solid var(--border-light);
  text-align: center; font-family: var(--font); font-size: 0.72rem; color: var(--text-muted);
  letter-spacing: 0.05em;
}}

@media (max-width: 1000px) {{
  .book-layout {{ grid-template-columns: 1fr; }}
  .toc-sidebar {{ position: relative; top: 0; height: auto; border-right: 0; border-bottom: 1px solid var(--border-light); padding: 20px 0; }}
  .main {{ padding: 24px 0; }}
}}
@media print {{
  .toc-sidebar, .top-bar, .theme-toggle {{ display: none !important; }}
  .book-layout {{ display: block; }}
}}
</style>
</head>
<body>

<header class="top-bar">
  <div class="top-bar-brand"><span>AK</span> Academic Knowledge Database</div>
  <div class="top-bar-actions">
    <button class="theme-toggle" onclick="toggleTheme()">DARK</button>
  </div>
</header>

<div class="book-layout">

<aside class="toc-sidebar">
  <div class="toc-title">目次</div>
  <nav class="toc">
    <a href="#overview"><span class="toc-num">00</span>概要</a>
    <a href="#stats"><span class="toc-num">01</span>規模統計</a>
    <a href="#humanities"><span class="toc-num">02</span>人文学</a>
    <a href="#social"><span class="toc-num">03</span>社会科学</a>
    <a href="#natural"><span class="toc-num">04</span>自然科学</a>
    <a href="#engineering"><span class="toc-num">05</span>工学</a>
    <a href="#arts"><span class="toc-num">06</span>芸術・デザイン</a>
    <a href="#era"><span class="toc-num">07</span>時代分布</a>
    <a href="#network"><span class="toc-num">08</span>関係ネットワーク</a>
    <a href="#history"><span class="toc-num">09</span>構築の経緯</a>
    <a href="#methodology"><span class="toc-num">10</span>方法論</a>
  </nav>
</aside>

<main class="main">

<section class="hero" id="overview">
  <div class="hero-subtitle">Academic Knowledge Database — v1.9.1</div>
  <h1 class="hero-title">学術知識データベース</h1>
  <p class="hero-lead">
  人文学・社会科学・自然科学・工学・芸術の5分野について、Oxford Handbook 基準のサブフィールド体系で
  {concepts:,} の学術概念・理論・モデル・運動を体系的に収集・構造化したデータベースです。
  各概念は定義・学派・時代・キーワード・主要研究者・基幹文献を含み、{relations_total:,} の関係ネットワークで
  系譜・対立・拡張・批判のつながりを可視化します。
  BCE 〜 2025 年の全時代をカバーし、特に 2015 年以降の最新理論を {recent_pct}% 含みます。
  </p>
</section>

<section id="stats">
  <div class="chapter-num">CHAPTER 01</div>
  <h2 class="chapter-title">規模統計</h2>
  <div class="stat-grid">
    <div class="stat"><div class="stat-value">{concepts:,}</div><div class="stat-label">学術概念</div></div>
    <div class="stat"><div class="stat-value">{subfields_total}</div><div class="stat-label">サブフィールド</div></div>
    <div class="stat"><div class="stat-value">{relations_intra:,}</div><div class="stat-label">分野内関係</div></div>
    <div class="stat"><div class="stat-value">{relations_cross:,}</div><div class="stat-label">分野横断関係</div></div>
    <div class="stat"><div class="stat-value">{recent_2015_total:,}</div><div class="stat-label">2015年以降</div></div>
    <div class="stat"><div class="stat-value">{recent_pct}%</div><div class="stat-label">最新比率</div></div>
  </div>
  <p style="font-family: var(--font-serif); font-size: 0.92rem; color: var(--text-secondary); line-height: 1.95; margin-top: 16px;">
  本データベースは2026年5月の集中拡張（Phase 7〜12）により、約8,000概念から{concepts:,}概念へと2倍以上に成長しました。
  全分野でサブフィールド偏在比 30倍以下、2015年以降比率 16% 以上を達成し、
  NULLs・重複・未分類すべてゼロのクリーンな状態を保持しています。
  </p>
</section>

{domain_sections}

<section id="era" class="chapter">
  <div class="chapter-num">CHAPTER 07</div>
  <h2 class="chapter-title">時代分布</h2>
  <p>5分野横断で見ると、本DBはBCE古代から現代AI時代まで連続的にカバーしています。
  特に2015年以降の現代理論（生成AI・気候・ポストヒューマン等）を意識的に補強しており、
  全分野で15%以上の比率を確保しています。</p>
  <div class="era-grid">
    {era_cells}
  </div>
</section>

<section id="network" class="chapter">
  <div class="chapter-num">CHAPTER 08</div>
  <h2 class="chapter-title">関係ネットワーク</h2>
  <p>各概念は時代順の系譜（extends/derived_from）、批判関係（critiques）、
  実証関係（empirically_tests）、対立（competes_with）等で結ばれます。
  2026年5月時点で分野内関係 {relations_intra:,} 件、分野横断関係 {relations_cross:,} 件、
  合計 {relations_total:,} 件のネットワークが構築されています。
  概念に対する関係比は {ratio:.2f} で、各概念が平均 {ratio_int} 件の関係を持ちます。</p>
  <p>分野横断関係には、innovation_theory・startup_theory ハブ経由の既存接続に加え、
  2026年5月のPhase 11で5コア分野間の直接接続 +1,788件を追加。これにより
  人文学から芸術へ、自然科学から工学へなど、領域横断的な概念探索が可能になっています。</p>
</section>

<section id="history" class="chapter">
  <div class="chapter-num">CHAPTER 09</div>
  <h2 class="chapter-title">構築の経緯</h2>
  <p>本データベースは2026年4月の v3 エージェント体系から始まり、6回のフェーズ拡張を経て現在の形に至りました。
  各フェーズは課題解決と品質向上を交互に行い、量的拡張と構造均衡化を両立させました。</p>
  <div class="timeline">
    <div class="timeline-item">
      <div class="timeline-date">2026-05-07</div>
      <div class="timeline-title">Phase 7: 初期コア5分野拡張</div>
      <div class="timeline-desc">Codex 40並列で +3,295概念 (8,074→11,369)。心理学パイロット完了後の初の本格拡張。</div>
    </div>
    <div class="timeline-item">
      <div class="timeline-date">2026-05-08</div>
      <div class="timeline-title">Phase 8: サブフィールド正規化＋追加収集</div>
      <div class="timeline-desc">600+ サブフィールド → 60カノニカル統合 (Oxford Handbook基準)。Codex 42並列で +3,430概念。</div>
    </div>
    <div class="timeline-item">
      <div class="timeline-date">2026-05-08</div>
      <div class="timeline-title">Phase 9: 大規模サブフィールド細分化</div>
      <div class="timeline-desc">古典詩学・生態学・文化人類学・心理学を時代/keyword分割。偏在比 119× → 22×へ大幅改善。</div>
    </div>
    <div class="timeline-item">
      <div class="timeline-date">2026-05-09</div>
      <div class="timeline-title">Phase 10: 構造均衡化完成</div>
      <div class="timeline-desc">構造主義・近代詩学・中世詩学さらなる細分化。未分類 560→0。全分野偏在比 &lt; 50 達成。</div>
    </div>
    <div class="timeline-item">
      <div class="timeline-date">2026-05-09</div>
      <div class="timeline-title">Phase 11: 質的深化＋cross_domain強化</div>
      <div class="timeline-desc">arts 2015+ 11.8% → 17.3%、5コア分野直接cross_domain +1,788件。検証ゲート全PASS。</div>
    </div>
    <div class="timeline-item">
      <div class="timeline-date">2026-05-09</div>
      <div class="timeline-title">Phase 12: 量的バランス調整</div>
      <div class="timeline-desc">humanities/engineering 14並列 +543件。詩学を arts へ統一。{concepts:,} 概念到達。</div>
    </div>
  </div>
</section>

<section id="methodology" class="chapter">
  <div class="chapter-num">CHAPTER 10</div>
  <h2 class="chapter-title">方法論</h2>
  <p><strong>収集方法:</strong>OpenAI Codex CLI を最大8並列で起動し、サブフィールド毎に60-200件の概念を JSON 配列で生成。
  各エントリには日本語/英語名、定義（100文字以上）、影響まとめ、サブフィールド、学派、時代、キーワード、主要研究者、基幹文献を含めます。</p>
  <p><strong>正規化:</strong>当初600以上に分散していたサブフィールド名を、Oxford Handbook / Cambridge Handbook の構造を参照しつつ
  各分野12〜15のカノニカルカテゴリに統合。94%は keyword ルールで自動分類、残り6%は name_en/keywords による二次分類で「未分類」を解消。</p>
  <p><strong>検証ゲート:</strong>(1) 量的増加 ≥ 30%、(2) サブフィールド数 ≤ 20、(3) 偏在比 &lt; 50、
  (4) 2015年以降 ≥ 15%、(5) NULLs/重複ゼロ、(6) 関係比 ≥ 1.0 の6項目で各フェーズ後に評価。
  軽微な課題のみであれば次フェーズへ移行する仕組みを採用しました。</p>
  <p><strong>関係構築:</strong>サブフィールド内では era_start 順にチェーン (extends/derived_from)、
  サブフィールド間ではキーワードJaccard類似度 ≥ 0.15 で related_to を追加。
  分野横断は5コア分野相互で直接マッチング、innovation/startup ハブ経由の既存関係も維持。</p>
  <p><strong>データ構造:</strong>SQLite で5分野テーブル + 各分野関係テーブル + cross_domain_relations。
  全テーブルで name_en による重複検出、フィールド充填率モニタリング、era_start 整数値検証を実施。</p>
</section>

</main>
</div>

<footer>
  <p>Academic Knowledge Database | v1.9.1 (2026-05-09) | Built by Yuya Nishimura with Claude Opus 4.7</p>
  <p style="margin-top:6px;">概念 {concepts:,} / 関係 {relations_total:,} / サブフィールド {subfields_total} / 5分野統合</p>
</footer>

<script>
function toggleTheme() {{
  const r = document.documentElement;
  const cur = r.getAttribute('data-theme');
  const next = cur === 'dark' ? 'light' : 'dark';
  r.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
  document.querySelector('.theme-toggle').textContent = next === 'dark' ? 'LIGHT' : 'DARK';
}}
const savedTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', savedTheme);
document.querySelector('.theme-toggle').textContent = savedTheme === 'dark' ? 'LIGHT' : 'DARK';
</script>
</body>
</html>
"""


def build_domain_section(idx: int, tbl: str, info: dict) -> str:
    label = info["label"]
    total = info["total"]
    subs = info["subfields"]
    max_count = max((c for _, c in subs), default=1)
    bars = ""
    for name, count in subs:
        pct = count / max_count * 100
        bars += f'<div class="subfield-bar"><div class="name">{name}</div><div class="bar-fill" style="width:{pct:.0f}%"></div><div class="count">{count}</div></div>\n'
    recent_pct = info["recent_pct"]
    sub_count = len(subs)
    return f"""
<section id="{tbl.replace('_', '-')}" class="chapter">
  <div class="chapter-num">CHAPTER {idx:02d}</div>
  <h2 class="chapter-title">{label}</h2>
  <div class="domain-card">
    <div class="domain-header">
      <div class="domain-name">{label}</div>
      <div class="domain-count">{total:,} 概念</div>
    </div>
    <div class="domain-meta">{sub_count} サブフィールド / 2015年以降 {info["recent_2015"]:,} 件 ({recent_pct}%)</div>
    <div class="subfield-bars">
      {bars}
    </div>
  </div>
</section>
"""


def build_era_cells(data: dict) -> str:
    # Aggregate era across all domains
    era_total = defaultdict(int)
    for tbl, _, _ in DOMAINS:
        for era, c in data["domains"][tbl]["era"]:
            era_total[era] += c
    total = sum(era_total.values())
    era_order = ["Pre-1900", "1900-1959", "1960-1984", "1985-1999", "2000-2014", "2015-"]
    cells = []
    for era in era_order:
        c = era_total.get(era, 0)
        pct = round(c / total * 100, 1) if total else 0
        cells.append(f'<div class="era-cell"><div class="era-label">{era}</div><div class="era-value">{c:,}</div><div class="era-pct">{pct}%</div></div>')
    return "\n".join(cells)


def main():
    data = collect_data()

    domain_sections = ""
    for i, (tbl, _, _) in enumerate(DOMAINS, start=2):
        domain_sections += build_domain_section(i, tbl, data["domains"][tbl])

    era_cells = build_era_cells(data)

    t = data["totals"]
    ratio = t["relations_total"] / t["concepts"] if t["concepts"] else 0
    html = HTML_TEMPLATE.format(
        concepts=t["concepts"],
        subfields_total=t["subfields_total"],
        relations_intra=t["relations_intra"],
        relations_cross=t["relations_cross"],
        relations_total=t["relations_total"],
        recent_2015_total=t["recent_2015_total"],
        recent_pct=t["recent_pct"],
        ratio=ratio,
        ratio_int=round(ratio),
        domain_sections=domain_sections,
        era_cells=era_cells,
    )

    SITE_OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {SITE_OUT} ({len(html):,} bytes)")
    DASHBOARD_OUT.parent.mkdir(parents=True, exist_ok=True)
    DASHBOARD_OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {DASHBOARD_OUT} ({len(html):,} bytes)")

    # Also write a JSON data file for programmatic access
    json_out = REPO_ROOT / "data_v2.json"
    json_out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
