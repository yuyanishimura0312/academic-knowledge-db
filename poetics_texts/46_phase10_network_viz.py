#!/usr/bin/env python3
"""Phase 10-C: 概念ネットワーク可視化HTML生成（D3.js force-directed graph）。"""
import sqlite3
import json
import html
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
OUTPUT = Path.home() / "projects/apps/miratuku-news-v2/dashboards/pt-network.html"

POETICS = ('古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム',
    '近代美学・詩学','現象学的詩学','中世・ルネサンス詩学','ポスト構造主義詩学',
    '受容理論','認知詩学','比較詩学','デジタル詩学')

SF_COLORS = {
    "古典詩学": "#CC1400", "修辞学・弁論術": "#A01000",
    "構造主義詩学": "#0066CC", "ロシア・フォルマリズム": "#0044AA",
    "近代美学・詩学": "#996600", "現象学的詩学": "#774400",
    "中世・ルネサンス詩学": "#88AA22", "ポスト構造主義詩学": "#660099",
    "受容理論": "#22AA88", "認知詩学": "#AA22AA",
    "比較詩学": "#008844", "デジタル詩学": "#444444"
}

REL_COLORS = {
    "extends": "#22AA22", "critiques": "#CC2200", "opposes": "#FF4400",
    "synthesizes": "#0066CC", "derived_from": "#888888", "reinterprets": "#AA8800",
    "enables": "#00AA88", "complements": "#0088AA", "applies_to": "#666666",
    "related_to": "#AAAAAA"
}


def fetch():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    placeholders = ",".join("?" * len(POETICS))
    cur.execute(f"""SELECT id, name_ja, name_en, subfield, school_of_thought, era_start
                   FROM humanities_concept WHERE subfield IN ({placeholders})""", POETICS)
    nodes = []
    node_ids = set()
    for r in cur.fetchall():
        nodes.append({
            "id": r[0], "name": r[1], "name_en": r[2] or "",
            "subfield": r[3], "school": r[4] or "",
            "era": r[5] if r[5] else 0,
            "color": SF_COLORS.get(r[3], "#999")
        })
        node_ids.add(r[0])

    cur.execute("""SELECT source_concept_id, target_concept_id, relation_type, strength
                   FROM humanities_concept_relations""")
    edges = []
    for s, t, rt, st in cur.fetchall():
        if s in node_ids and t in node_ids:
            edges.append({
                "source": s, "target": t, "type": rt or "related_to",
                "strength": st or 5,
                "color": REL_COLORS.get(rt, "#999")
            })

    cur.execute("SELECT COUNT(*) FROM concept_original_source")
    n_quotes = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM poetics_text")
    n_texts = cur.fetchone()[0]

    conn.close()
    return nodes, edges, n_quotes, n_texts


def render(nodes, edges, n_quotes, n_texts):
    nodes_json = json.dumps(nodes, ensure_ascii=False)
    edges_json = json.dumps(edges, ensure_ascii=False)
    sf_legend = "".join(
        f'<span class="legend-item"><span class="dot" style="background:{c}"></span>{html.escape(sf)}</span>'
        for sf, c in SF_COLORS.items()
    )
    rel_legend = "".join(
        f'<span class="legend-item"><span class="line" style="background:{c}"></span>{html.escape(rt)}</span>'
        for rt, c in REL_COLORS.items()
    )

    return f"""<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>詩学概念ネットワーク — Poetics DB v2.3</title>
<link rel="icon" href="https://esse-sense.com/favicon.ico">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@400;700&display=swap" rel="stylesheet">
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
:root {{ --bg:#FFFFFF; --text:#121212; --text-secondary:#555;
  --accent-warm:#CC1400; --border:#D9D9D9; --surface:#F7F7F5;
  --font:"Noto Sans JP",sans-serif; --font-serif:"Noto Serif JP",serif; }}
[data-theme="dark"] {{ --bg:#121212; --text:#E0E0E0; --text-secondary:#AAA;
  --accent-warm:#FF4030; --border:#333; --surface:#1A1A1A; }}
*, *::before, *::after {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ font-family:var(--font); color:var(--text); background:var(--bg); }}
.top-bar {{ position:fixed; top:0; left:0; right:0; height:48px;
  background:var(--bg); border-top:3px solid #121212;
  border-bottom:1px solid var(--border); display:flex; align-items:center;
  padding:0 20px; z-index:100; justify-content:space-between; }}
.brand {{ font-family:var(--font-serif); font-size:1rem; font-weight:700; color:var(--accent-warm); }}
.theme-toggle {{ background:none; border:1px solid var(--border); padding:4px 10px; cursor:pointer; }}
main {{ padding-top:60px; min-height:100vh; }}
.intro {{ background:var(--surface); border-left:4px solid var(--accent-warm);
  padding:14px 20px; margin:16px 20px; }}
.intro h1 {{ font-family:var(--font-serif); font-size:1.4rem; margin-bottom:6px; }}
.intro p {{ font-size:0.86rem; line-height:1.7; }}
.controls {{ display:flex; gap:14px; align-items:center; padding:8px 20px;
  flex-wrap:wrap; font-size:0.84rem; }}
.controls input[type=text] {{ padding:6px 10px; border:1px solid var(--border);
  background:var(--bg); color:var(--text); width:240px; }}
.controls select {{ padding:6px 10px; border:1px solid var(--border);
  background:var(--bg); color:var(--text); }}
.legend-block {{ padding:8px 20px; font-size:0.74rem; color:var(--text-secondary);
  border-top:1px solid var(--border); border-bottom:1px solid var(--border); }}
.legend-row {{ margin-bottom:4px; display:flex; flex-wrap:wrap; gap:10px; }}
.legend-row strong {{ font-weight:600; min-width:90px; }}
.legend-item {{ display:inline-flex; align-items:center; gap:4px; margin-right:8px; }}
.dot {{ width:10px; height:10px; border-radius:50%; display:inline-block; }}
.line {{ width:14px; height:2px; display:inline-block; }}
#graph {{ width:100%; height:calc(100vh - 240px); background:var(--bg); }}
.node circle {{ stroke:#fff; stroke-width:1.5px; cursor:pointer; }}
.node text {{ font-size:9px; pointer-events:none; fill:var(--text); }}
.link {{ stroke-opacity:0.5; fill:none; }}
.tooltip {{ position:absolute; padding:8px 12px; background:rgba(0,0,0,0.85);
  color:#fff; font-size:0.78rem; border-radius:4px; pointer-events:none;
  max-width:300px; line-height:1.5; }}
.summary {{ display:grid; grid-template-columns:repeat(4,1fr); gap:10px;
  padding:8px 20px; }}
.sum-card {{ background:var(--surface); padding:10px; text-align:center;
  border:1px solid var(--border); }}
.sum-val {{ font-family:var(--font-serif); font-size:1.4rem; color:var(--accent-warm); font-weight:700; }}
.sum-lbl {{ font-size:0.72rem; color:var(--text-secondary); }}
</style></head><body>
<div class="top-bar">
  <div class="brand">詩学概念ネットワーク <span style="font-size:0.74rem;color:var(--text-secondary);font-weight:400">— Poetics DB v2.3</span></div>
  <button class="theme-toggle" onclick="document.documentElement.setAttribute('data-theme',document.documentElement.getAttribute('data-theme')==='dark'?'':'dark')">&#9789;</button>
</div>
<main>
<div class="intro">
<h1>概念系譜ネットワーク</h1>
<p>{len(nodes):,}概念 × {len(edges):,}関係をD3.js force-directed graphで可視化。サブフィールド毎に色分けし、関係タイプ毎にエッジ色を変えています。検索・フィルタリング・ノードクリックで詳細表示が可能です。</p>
</div>
<div class="summary">
<div class="sum-card"><div class="sum-val">{len(nodes):,}</div><div class="sum-lbl">概念ノード</div></div>
<div class="sum-card"><div class="sum-val">{len(edges):,}</div><div class="sum-lbl">関係エッジ</div></div>
<div class="sum-card"><div class="sum-val">{n_quotes:,}</div><div class="sum-lbl">原著引用</div></div>
<div class="sum-card"><div class="sum-val">{n_texts:,}</div><div class="sum-lbl">詩文</div></div>
</div>
<div class="controls">
<input type="text" id="search" placeholder="概念名で検索...">
<select id="sf-filter"><option value="">全サブフィールド</option></select>
<select id="rel-filter"><option value="">全関係タイプ</option></select>
<button id="reset" style="padding:6px 12px;border:1px solid var(--border);background:var(--bg);color:var(--text);cursor:pointer">リセット</button>
</div>
<div class="legend-block">
<div class="legend-row"><strong>サブフィールド:</strong>{sf_legend}</div>
<div class="legend-row"><strong>関係タイプ:</strong>{rel_legend}</div>
</div>
<svg id="graph"></svg>
<div class="tooltip" id="tooltip" style="display:none"></div>
</main>
<script>
const allNodes = {nodes_json};
const allEdges = {edges_json};
let visibleNodes = [...allNodes];
let visibleEdges = [...allEdges];

const sfFilter = document.getElementById('sf-filter');
const sfs = [...new Set(allNodes.map(n=>n.subfield))].sort();
sfs.forEach(sf=>{{const o=document.createElement('option');o.value=sf;o.textContent=sf;sfFilter.appendChild(o);}});

const relFilter = document.getElementById('rel-filter');
const rels = [...new Set(allEdges.map(e=>e.type))].sort();
rels.forEach(r=>{{const o=document.createElement('option');o.value=r;o.textContent=r;relFilter.appendChild(o);}});

const svg = d3.select('#graph');
const width = window.innerWidth;
const height = window.innerHeight - 240;
svg.attr('viewBox',`0 0 ${{width}} ${{height}}`);

const g = svg.append('g');
const linkLayer = g.append('g').attr('class','links');
const nodeLayer = g.append('g').attr('class','nodes');

const zoom = d3.zoom().scaleExtent([0.1,8]).on('zoom',e=>g.attr('transform',e.transform));
svg.call(zoom);

const tooltip = d3.select('#tooltip');

let simulation = null;

function render(nodes, edges){{
  if (simulation) simulation.stop();
  simulation = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(edges).id(d=>d.id).distance(80).strength(0.6))
    .force('charge', d3.forceManyBody().strength(-180))
    .force('center', d3.forceCenter(width/2, height/2))
    .force('collide', d3.forceCollide(12));

  linkLayer.selectAll('line').remove();
  const link = linkLayer.selectAll('line').data(edges).enter().append('line')
    .attr('class','link')
    .attr('stroke', d=>d.color)
    .attr('stroke-width', d=>Math.max(0.5, d.strength/4));

  nodeLayer.selectAll('g.node').remove();
  const node = nodeLayer.selectAll('g.node').data(nodes).enter().append('g')
    .attr('class','node')
    .call(d3.drag()
      .on('start',(e,d)=>{{if(!e.active)simulation.alphaTarget(0.3).restart();d.fx=d.x;d.fy=d.y;}})
      .on('drag',(e,d)=>{{d.fx=e.x;d.fy=e.y;}})
      .on('end',(e,d)=>{{if(!e.active)simulation.alphaTarget(0);d.fx=null;d.fy=null;}}));

  node.append('circle')
    .attr('r', d=>4+Math.min(8, edges.filter(e=>e.source===d.id||e.target===d.id||e.source.id===d.id||e.target.id===d.id).length/3))
    .attr('fill', d=>d.color)
    .on('mouseover', (e,d)=>{{
      tooltip.style('display','block')
        .style('left',(e.pageX+10)+'px').style('top',(e.pageY+10)+'px')
        .html(`<strong>${{d.name}}</strong><br>${{d.name_en}}<br><em>${{d.subfield}}</em>${{d.school?'<br>'+d.school:''}}${{d.era?'<br>era: '+d.era:''}}`);
    }})
    .on('mouseout', ()=>tooltip.style('display','none'));

  node.append('text').attr('dx',8).attr('dy',3).text(d=>d.name).style('font-size','9px');

  simulation.on('tick',()=>{{
    link.attr('x1',d=>d.source.x).attr('y1',d=>d.source.y)
        .attr('x2',d=>d.target.x).attr('y2',d=>d.target.y);
    node.attr('transform',d=>`translate(${{d.x}},${{d.y}})`);
  }});
}}

function applyFilters(){{
  const search = document.getElementById('search').value.toLowerCase();
  const sfVal = sfFilter.value;
  const relVal = relFilter.value;
  let nodes = allNodes;
  let edges = allEdges;
  if (sfVal) nodes = nodes.filter(n=>n.subfield===sfVal);
  if (search) nodes = nodes.filter(n=>n.name.toLowerCase().includes(search) || (n.name_en||'').toLowerCase().includes(search));
  const ids = new Set(nodes.map(n=>n.id));
  edges = edges.filter(e=>ids.has(typeof e.source==='string'?e.source:e.source.id) && ids.has(typeof e.target==='string'?e.target:e.target.id));
  if (relVal) edges = edges.filter(e=>e.type===relVal);
  // Reset link source/target to id strings for fresh simulation
  edges = edges.map(e=>({{...e, source:typeof e.source==='string'?e.source:e.source.id, target:typeof e.target==='string'?e.target:e.target.id}}));
  visibleNodes = nodes.map(n=>({{...n}}));
  visibleEdges = edges;
  render(visibleNodes, visibleEdges);
}}

document.getElementById('search').addEventListener('input', applyFilters);
sfFilter.addEventListener('change', applyFilters);
relFilter.addEventListener('change', applyFilters);
document.getElementById('reset').addEventListener('click',()=>{{
  document.getElementById('search').value='';
  sfFilter.value='';
  relFilter.value='';
  applyFilters();
}});

// Initial render — limit to reduce CPU on first load
const initialNodes = allNodes.slice(0, 800).map(n=>({{...n}}));
const initialIds = new Set(initialNodes.map(n=>n.id));
const initialEdges = allEdges.filter(e=>initialIds.has(e.source) && initialIds.has(e.target)).map(e=>({{...e}}));
render(initialNodes, initialEdges);
</script>
</body></html>
"""


def main():
    nodes, edges, n_quotes, n_texts = fetch()
    h = render(nodes, edges, n_quotes, n_texts)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(h, encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size:,} bytes")
    print(f"Nodes: {len(nodes)}, Edges: {len(edges)}, Quotes: {n_quotes}, Texts: {n_texts}")


if __name__ == "__main__":
    main()
