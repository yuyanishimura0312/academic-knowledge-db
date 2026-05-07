#!/usr/bin/env python3
"""Phase 9-C: 詩学教科書HTML自動生成（3層クロスリファレンス）。"""
import sqlite3
import html
from collections import defaultdict
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
OUTPUT = Path.home() / "projects/apps/miratuku-news-v2/dashboards/pt-textbook.html"

POETICS = ('古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム',
    '近代美学・詩学','現象学的詩学','中世・ルネサンス詩学','ポスト構造主義詩学',
    '受容理論','認知詩学','比較詩学','デジタル詩学')

CHAPTERS = [
    ("第一章 古代詩学の基礎", ["古典詩学", "修辞学・弁論術"]),
    ("第二章 中世・ルネサンス詩学", ["中世・ルネサンス詩学"]),
    ("第三章 近代美学・現象学的詩学", ["近代美学・詩学", "現象学的詩学"]),
    ("第四章 形式主義と構造主義", ["ロシア・フォルマリズム", "構造主義詩学"]),
    ("第五章 受容理論と読者", ["受容理論"]),
    ("第六章 ポスト構造主義の展開", ["ポスト構造主義詩学"]),
    ("第七章 認知詩学", ["認知詩学"]),
    ("第八章 比較詩学（東洋・南アジア・横断的視座）", ["比較詩学"]),
    ("第九章 デジタル詩学", ["デジタル詩学"]),
]

CSS = """
:root { --bg:#FFFFFF; --card:#FFFFFF; --accent-warm:#CC1400;
  --accent-muted:rgba(204,20,0,0.06); --text:#121212;
  --text-secondary:#555555; --text-muted:#6B6B6B;
  --border:#D9D9D9; --border-light:#EEEEEE; --surface:#F7F7F5;
  --font:"Noto Sans JP","Hiragino Sans",sans-serif;
  --font-serif:"Noto Serif JP","Hiragino Mincho ProN",Georgia,serif; }
[data-theme="dark"] { --bg:#121212; --card:#1A1A1A; --accent-warm:#FF4030;
  --accent-muted:rgba(255,64,48,0.10); --text:#E0E0E0;
  --text-secondary:#AAAAAA; --text-muted:#8A8A8A;
  --border:#333333; --border-light:#2A2A2A; --surface:#1A1A1A; }
*, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
body { font-family:var(--font); color:var(--text); background:var(--bg);
  line-height:1.85; letter-spacing:0.025em; font-feature-settings:"palt"; }
.top-bar { position:fixed; top:0; left:0; right:0; height:48px;
  background:var(--bg); border-top:3px solid #121212;
  border-bottom:1px solid var(--border); display:flex; align-items:center;
  padding:0 20px; z-index:100; justify-content:space-between; }
.brand { font-family:var(--font-serif); font-size:1rem; font-weight:700; color:var(--accent-warm); }
.theme-toggle { background:none; border:1px solid var(--border); padding:4px 10px; cursor:pointer; }
.layout { display:flex; padding-top:60px; }
.toc-sidebar { width:260px; min-width:260px; padding:28px 16px;
  border-right:1px solid var(--border-light); position:sticky; top:60px;
  height:calc(100vh - 60px); overflow-y:auto; font-size:0.82rem; }
.toc-sidebar h4 { font-family:var(--font-serif); margin-bottom:12px; color:var(--accent-warm); }
.toc-sidebar ol { list-style:none; padding-left:0; }
.toc-sidebar ol ol { padding-left:14px; margin-top:4px; }
.toc-sidebar li { margin-bottom:4px; }
.toc-sidebar a { color:var(--text); text-decoration:none; }
.toc-sidebar a:hover { color:var(--accent-warm); }
.toc-n { font-size:0.72rem; color:var(--text-muted); }
main { flex:1; max-width:760px; margin:0 auto; padding:36px 32px 80px; }
.intro { background:var(--surface); border-left:4px solid var(--accent-warm);
  padding:18px 22px; margin-bottom:40px; }
.intro h1 { font-family:var(--font-serif); font-size:1.6rem; margin-bottom:8px; }
.intro p { font-size:0.92rem; line-height:1.85; }
.summary-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin:16px 0 24px; }
.sum-card { background:var(--surface); padding:14px; text-align:center; border:1px solid var(--border-light); }
.sum-val { font-family:var(--font-serif); font-size:1.6rem; color:var(--accent-warm); font-weight:700; }
.sum-lbl { font-size:0.74rem; color:var(--text-muted); margin-top:2px; }
.chapter-section { margin-bottom:64px; padding-bottom:32px; border-bottom:1px solid var(--border-light); }
.chapter-section h2 { font-family:var(--font-serif); font-size:1.4rem;
  color:var(--accent-warm); padding:12px 0 8px;
  border-bottom:2px solid var(--accent-warm); margin-bottom:24px; }
.chapter-section h3 { font-family:var(--font-serif); font-size:1.1rem;
  margin:28px 0 16px; padding:6px 12px;
  background:var(--accent-muted); color:var(--accent-warm); }
.sub-count { font-size:0.78rem; color:var(--text-muted); font-weight:400; margin-left:8px; }
.concept-entry { margin-bottom:28px; padding-bottom:18px; border-bottom:1px dashed var(--border-light); }
.concept-entry h4 { font-family:var(--font-serif); font-size:1rem; margin-bottom:6px; }
.concept-entry h4 .en { font-size:0.84rem; color:var(--text-secondary);
  font-weight:400; margin-left:8px; font-style:italic; }
.concept-entry h4 .orig { font-size:0.84rem; color:var(--accent-warm);
  font-weight:500; margin-left:8px; }
.concept-meta { font-size:0.74rem; color:var(--text-muted); margin-bottom:8px; }
.concept-def { font-family:var(--font-serif); font-size:0.92rem; line-height:1.85;
  margin-bottom:8px; text-indent:1em; }
.concept-def:first-of-type { text-indent:0; }
.concept-impact { font-size:0.86rem; color:var(--text-secondary);
  margin-bottom:12px; padding-left:12px; border-left:2px solid var(--border); }
.quote-block { margin:14px 0; padding:12px 16px;
  background:var(--surface); border-left:3px solid var(--accent-warm); }
.quote-entry { margin-bottom:10px; }
.quote-ref { font-size:0.78rem; color:var(--accent-warm); font-weight:600; margin-bottom:4px; }
.q-original { font-family:var(--font-serif); font-size:0.88rem; line-height:1.7;
  padding:6px 12px; margin:4px 0; background:var(--bg);
  border:1px solid var(--border-light); white-space:pre-wrap; }
.q-ja { font-size:0.84rem; color:var(--text-secondary); padding:4px 12px; }
.q-sig { font-size:0.82rem; color:var(--text); padding:4px 0;
  border-top:1px dotted var(--border); margin-top:6px; }
.exemplars { margin-top:12px; padding:8px 12px; background:var(--accent-muted); }
.exemplars h5 { font-size:0.84rem; color:var(--accent-warm); margin-bottom:6px; }
.exemplars ul { list-style:none; padding-left:0; }
.exemplars li { margin-bottom:6px; font-size:0.84rem; }
.ex-meta { color:var(--text-muted); font-size:0.76rem; }
.ex-excerpt { font-family:var(--font-serif); font-size:0.78rem;
  color:var(--text-secondary); margin-top:2px; padding-left:8px;
  border-left:1px solid var(--border-light); }
@media (max-width:1000px) { .layout { flex-direction:column; }
  .toc-sidebar { width:100%; min-width:0; position:relative; height:auto;
    border-right:none; border-bottom:1px solid var(--border); }
  main { padding:24px 16px; } }
@media print { .toc-sidebar, .top-bar, .theme-toggle { display:none; }
  body { padding-top:0; } main { max-width:none; } }
"""


def fetch():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    placeholders = ",".join("?" * len(POETICS))
    cur.execute(f"""SELECT id, name_ja, name_en, name_original, definition,
                          impact_summary, subfield, school_of_thought,
                          era_start, era_end FROM humanities_concept
                   WHERE subfield IN ({placeholders})
                   ORDER BY subfield, COALESCE(era_start, 9999), name_ja""", POETICS)
    concepts = cur.fetchall()
    cur.execute("""SELECT concept_id, source_work_title, source_locator,
                          source_year, source_author, source_language,
                          quote_original, quote_japanese, quote_english,
                          quote_significance FROM concept_original_source""")
    quotes = defaultdict(list)
    for r in cur.fetchall():
        quotes[r[0]].append({"work":r[1],"locator":r[2],"year":r[3],"author":r[4],
                             "lang":r[5],"original":r[6],"ja":r[7],"en":r[8],"sig":r[9]})
    cur.execute("""SELECT ctst.concept_id, pt.title_ja, pt.author_name_display,
                          pt.culture_region, pt.era_year, pt.language_original,
                          pt.full_text_or_excerpt, ctst.relationship_note
                   FROM concept_text_source_triple ctst
                   JOIN poetics_text pt ON ctst.text_id = pt.id
                   ORDER BY ctst.confidence DESC""")
    triples = defaultdict(list)
    for r in cur.fetchall():
        triples[r[0]].append({"title":r[1],"author":r[2],"culture":r[3],
                              "year":r[4],"lang":r[5],"excerpt":r[6][:200] if r[6] else "",
                              "note":r[7]})
    cur.execute("""SELECT ptcl.concept_id, pt.title_ja, pt.author_name_display,
                          pt.culture_region, pt.era_year, pt.language_original,
                          pt.full_text_or_excerpt, ptcl.discussion_locus
                   FROM poetics_text_concept_link ptcl
                   JOIN poetics_text pt ON ptcl.text_id = pt.id
                   WHERE ptcl.concept_id NOT IN (SELECT DISTINCT concept_id FROM concept_text_source_triple)""")
    for r in cur.fetchall():
        triples[r[0]].append({"title":r[1],"author":r[2],"culture":r[3],
                              "year":r[4],"lang":r[5],"excerpt":r[6][:200] if r[6] else "",
                              "note":r[7] or ""})
    conn.close()
    return concepts, quotes, triples


def render(concepts, quotes, triples):
    by_sf = defaultdict(list)
    for c in concepts:
        by_sf[c[6]].append(c)
    total_concepts = len(concepts)
    total_quotes = sum(len(v) for v in quotes.values())
    total_triples = sum(len(v) for v in triples.values())

    toc = ['<nav class="toc-sidebar"><h4>目次</h4><ol>']
    for ch_idx, (chapter, subs) in enumerate(CHAPTERS, 1):
        n = sum(len(by_sf.get(sf, [])) for sf in subs)
        toc.append(f'<li><a href="#chapter-{ch_idx}">{chapter}</a> <span class="toc-n">({n})</span><ol>')
        for sf in subs:
            sf_id = f"sf-{ch_idx}-{sf}"
            toc.append(f'<li><a href="#{sf_id}">{sf}</a> <span class="toc-n">({len(by_sf.get(sf, []))})</span></li>')
        toc.append('</ol></li>')
    toc.append('</ol></nav>')
    toc_html = "\n".join(toc)

    body = []
    for ch_idx, (chapter, subs) in enumerate(CHAPTERS, 1):
        body.append(f'<section class="chapter-section" id="chapter-{ch_idx}">')
        body.append(f'<h2>{html.escape(chapter)}</h2>')
        for sf in subs:
            sf_concepts = by_sf.get(sf, [])
            if not sf_concepts:
                continue
            sf_id = f"sf-{ch_idx}-{sf}"
            body.append(f'<h3 id="{sf_id}">{html.escape(sf)} <span class="sub-count">{len(sf_concepts)}概念</span></h3>')
            for c in sf_concepts[:120]:
                cid, name_ja, name_en, name_orig, defn, impact, _, school, era_s, era_e = c
                qs = quotes.get(cid, [])
                ts = triples.get(cid, [])
                body.append(f'<article class="concept-entry" id="{cid}">')
                title = [html.escape(name_ja or "")]
                if name_en:
                    title.append(f'<span class="en">{html.escape(name_en)}</span>')
                if name_orig:
                    title.append(f'<span class="orig">{html.escape(name_orig)}</span>')
                body.append(f'<h4>{" ".join(title)}</h4>')
                meta = []
                if school:
                    meta.append(f'学派: {html.escape(school)}')
                if era_s:
                    era_str = f'{abs(era_s)}{"BCE" if era_s < 0 else ""}'
                    meta.append(f'時代: {era_str}')
                if meta:
                    body.append(f'<p class="concept-meta">{" / ".join(meta)}</p>')
                if defn:
                    body.append(f'<p class="concept-def">{html.escape(defn)}</p>')
                if impact:
                    body.append(f'<p class="concept-impact"><strong>影響:</strong> {html.escape(impact)}</p>')
                if qs:
                    body.append('<div class="quote-block">')
                    for q in qs[:2]:
                        body.append('<div class="quote-entry">')
                        ref = []
                        if q.get("author"):
                            ref.append(html.escape(q["author"]))
                        if q.get("work"):
                            ref.append(f'『{html.escape(q["work"])}』')
                        if q.get("locator"):
                            ref.append(html.escape(q["locator"]))
                        body.append(f'<div class="quote-ref">{" ".join(ref)}</div>')
                        if q.get("original"):
                            body.append(f'<blockquote class="q-original">{html.escape(q["original"][:600])}</blockquote>')
                        if q.get("ja"):
                            body.append(f'<blockquote class="q-ja"><em>訳:</em> {html.escape(q["ja"][:400])}</blockquote>')
                        if q.get("sig"):
                            body.append(f'<p class="q-sig"><em>意義:</em> {html.escape(q["sig"][:400])}</p>')
                        body.append('</div>')
                    body.append('</div>')
                if ts:
                    body.append('<div class="exemplars"><h5>例証テクスト</h5><ul>')
                    for t in ts[:3]:
                        meta_t = []
                        if t.get("author"):
                            meta_t.append(html.escape(t["author"]))
                        if t.get("culture"):
                            meta_t.append(html.escape(t["culture"]))
                        if t.get("year"):
                            meta_t.append(str(t["year"]))
                        body.append(f'<li><strong>{html.escape(t["title"] or "")}</strong> <span class="ex-meta">({" / ".join(meta_t)})</span>')
                        if t.get("excerpt"):
                            body.append(f'<div class="ex-excerpt">{html.escape(t["excerpt"][:120])}…</div>')
                        body.append('</li>')
                    body.append('</ul></div>')
                body.append('</article>')
        body.append('</section>')
    body_html = "\n".join(body)

    return f"""<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>詩学概念教科書 — 概念・原典・例証の3層構造</title>
<link rel="icon" href="https://esse-sense.com/favicon.ico">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="top-bar">
<div class="brand">詩学概念教科書 <span style="font-size:0.74rem;color:var(--text-muted);font-weight:400">— Poetics DB v2.1 三層連結版</span></div>
<button class="theme-toggle" onclick="document.documentElement.setAttribute('data-theme',document.documentElement.getAttribute('data-theme')==='dark'?'':'dark')">&#9789;</button>
</div>
<div class="layout">
{toc_html}
<main>
<div class="intro">
<h1>詩学概念教科書</h1>
<p>本書は Poetics DB v2.1 の収録データを教科書形式で再編成したものである。プラトン『国家』におけるミメーシス批判（前380年頃）から21世紀のデジタル詩学・認知詩学に至るまで、東西の詩学概念を9章・12サブフィールドに体系化し、各概念について <strong>(1) 定義と影響</strong>、<strong>(2) 原典の founding passage（原語＋日訳＋意義分析）</strong>、<strong>(3) 例証となる詩文</strong> の3層を一覧できる構成とした。学派は時代順に並べ、各概念のなかで Aristotle, Plato, Bharata, Anandavardhana, 世阿弥, 鴨長明, 司空圖, 王國維, Shklovsky, Bakhtin, Genette, Jakobson, Ingarden, Jauss, Iser, Lakoff, Derrida, Kristeva, Eliot, Brooks 等の原典に直接接続できるよう編集している。</p>
<div class="summary-grid">
<div class="sum-card"><div class="sum-val">{total_concepts:,}</div><div class="sum-lbl">概念</div></div>
<div class="sum-card"><div class="sum-val">{total_quotes:,}</div><div class="sum-lbl">原典引用</div></div>
<div class="sum-card"><div class="sum-val">{total_triples:,}</div><div class="sum-lbl">三項リンク</div></div>
<div class="sum-card"><div class="sum-val">{len(CHAPTERS)}</div><div class="sum-lbl">章</div></div>
</div>
</div>
{body_html}
<footer style="margin-top:48px;padding-top:24px;border-top:1px solid var(--border-light);font-size:0.78rem;color:var(--text-muted);text-align:center">
Poetics DB v2.1 三層連結教科書 &middot; academic-knowledge-db / Insight News<br>
{total_concepts:,} concepts &middot; {total_quotes:,} founding quotes &middot; {total_triples:,} concept-text-source triples
</footer>
</main></div></body></html>
"""


def main():
    concepts, quotes, triples = fetch()
    h = render(concepts, quotes, triples)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(h, encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size:,} bytes")
    print(f"Concepts: {len(concepts)}")
    print(f"Quote concepts: {len(quotes)}")
    print(f"Triple concepts: {len(triples)}")


if __name__ == "__main__":
    main()
