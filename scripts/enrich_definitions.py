#!/usr/bin/env python3
"""
Enrich short definitions in the database with detailed academic descriptions.
Targets concepts with definitions < 100 chars. Uses Claude API in small batches.
"""

import json
import sqlite3
import subprocess
import time
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"

TABLES = [
    "humanities_concept",
    "social_theory",
    "natural_discovery",
    "engineering_method",
    "arts_question",
]

DOMAIN_NAMES = {
    "humanities_concept": "人文学",
    "social_theory": "社会科学",
    "natural_discovery": "自然科学",
    "engineering_method": "工学",
    "arts_question": "芸術",
}


def get_api_key():
    result = subprocess.run(
        ["security", "find-generic-password", "-a", "anthropic", "-w"],
        capture_output=True, text=True
    )
    return result.stdout.strip()


def call_claude_api(prompt, api_key):
    import urllib.request
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }
    body = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 4000,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body, headers=headers, method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read())
    return result["content"][0]["text"]


def extract_json(text):
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        start = 1
        end = len(lines) - 1
        if lines[-1].strip() == "```":
            text = "\n".join(lines[start:end])
        else:
            text = "\n".join(lines[start:])
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        s = text.find("[")
        if s >= 0:
            for e in range(len(text), s, -1):
                try:
                    return json.loads(text[s:e])
                except:
                    continue
        raise


def enrich_all():
    api_key = get_api_key()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    total_updated = 0

    for table in TABLES:
        domain_name = DOMAIN_NAMES[table]
        # Get concepts with short definitions
        rows = conn.execute(
            f"SELECT id, name_ja, name_en, definition, era_start, school_of_thought "
            f"FROM {table} WHERE length(definition) < 100 OR definition IS NULL"
        ).fetchall()

        if not rows:
            print(f"{domain_name}: all definitions OK")
            continue

        print(f"\n{domain_name}: {len(rows)} concepts need enrichment")

        # Process in batches of 5
        batch_size = 5
        for i in range(0, len(rows), batch_size):
            batch = rows[i:i+batch_size]
            batch_num = i // batch_size + 1
            total_batches = (len(rows) + batch_size - 1) // batch_size

            concept_list = "\n".join(
                f"  {j+1}. {r['name_ja']} ({r['name_en']}, {r['era_start']}年, {r['school_of_thought'] or ''})"
                for j, r in enumerate(batch)
            )

            prompt = f"""以下の{domain_name}の学術概念に対して、学術的に正確���定義文を生成してください。
各定義は2-3文で、概念の本質、提唱者の貢献、学問的意義を含めてください。

{concept_list}

JSON配列のみ出力してください:
[
  {{"name_en": "概念の英語名", "definition": "学術的定義文（日本語、2-3文）"}}
]
"""
            try:
                response = call_claude_api(prompt, api_key)
                definitions = extract_json(response)

                for defn in definitions:
                    name_en = defn.get("name_en", "")
                    new_def = defn.get("definition", "")
                    if not new_def or len(new_def) < 50:
                        continue

                    # Find matching row
                    for r in batch:
                        if r["name_en"] == name_en:
                            conn.execute(
                                f"UPDATE {table} SET definition = ? WHERE id = ?",
                                (new_def, r["id"])
                            )
                            total_updated += 1
                            break

                conn.commit()
                print(f"  Batch {batch_num}/{total_batches}: updated {len(definitions)} definitions")
                time.sleep(1)

            except Exception as e:
                print(f"  Batch {batch_num}/{total_batches}: ERROR - {e}")
                time.sleep(2)
                continue

    conn.close()
    print(f"\nTotal updated: {total_updated}")


if __name__ == "__main__":
    enrich_all()
