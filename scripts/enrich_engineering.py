#!/usr/bin/env python3
"""Enrich engineering_method definitions only."""
import json, sqlite3, subprocess, sys, time, urllib.request
sys.stdout.reconfigure(line_buffering=True)

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
TABLE = "engineering_method"

def get_key():
    return subprocess.run(["security","find-generic-password","-a","anthropic","-w"], capture_output=True, text=True).stdout.strip()

def call_api(prompt, key):
    body = json.dumps({"model":"claude-sonnet-4-20250514","max_tokens":4000,"messages":[{"role":"user","content":prompt}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={"Content-Type":"application/json","x-api-key":key,"anthropic-version":"2023-06-01"}, method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())["content"][0]["text"]

def extract_json(t):
    t = t.strip()
    if t.startswith("```"):
        lines = t.split("\n")
        t = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])
    try: return json.loads(t)
    except:
        s = t.find("[")
        if s >= 0:
            for e in range(len(t), s, -1):
                try: return json.loads(t[s:e])
                except: continue
        raise

key = get_key()
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
rows = conn.execute(f"SELECT id,name_ja,name_en,definition,era_start,school_of_thought FROM {TABLE} WHERE length(definition)<100 OR definition IS NULL").fetchall()
print(f"Engineering: {len(rows)} to enrich")

updated = 0
for i in range(0, len(rows), 5):
    batch = rows[i:i+5]
    bn = i // 5 + 1
    tb = (len(rows) + 4) // 5
    clist = "\n".join(f"  {j+1}. {r['name_ja']} ({r['name_en']}, {r['era_start']}年)" for j, r in enumerate(batch))
    prompt = f"以下の工学の概念・技術に対して、学術的に正確な定義文を生成してください。各定義は2-3文。\n\n{clist}\n\nJSON配列のみ出力:\n[{{\"name_en\":\"name\",\"definition\":\"定義文\"}}]"
    try:
        resp = call_api(prompt, key)
        defs = extract_json(resp)
        for d in defs:
            for r in batch:
                if r["name_en"] == d.get("name_en", "") and len(d.get("definition", "")) >= 50:
                    conn.execute(f"UPDATE {TABLE} SET definition=? WHERE id=?", (d["definition"], r["id"]))
                    updated += 1
                    break
        conn.commit()
        print(f"  Batch {bn}/{tb}: OK")
        time.sleep(1)
    except Exception as e:
        print(f"  Batch {bn}/{tb}: ERROR {e}")
        time.sleep(2)

conn.close()
print(f"Engineering DONE: {updated} updated")
