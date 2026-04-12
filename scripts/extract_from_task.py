#!/usr/bin/env python3
"""Extract JSON entities from task notification result text (passed via stdin or file)."""

import re
import json
import sys
from pathlib import Path


def extract_all_json_arrays(text):
    """Extract JSON arrays from markdown code blocks in text."""
    pattern = r'```json\s*(\[[\s\S]*?\])\s*```'
    matches = re.findall(pattern, text)
    all_entities = []
    for m in matches:
        try:
            arr = json.loads(m)
            if isinstance(arr, list):
                all_entities.extend(arr)
        except json.JSONDecodeError:
            continue
    return all_entities


def extract_from_jsonl(filepath):
    """Extract from JSONL agent output file."""
    all_entities = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                # Look for assistant messages containing JSON
                if obj.get("type") == "assistant":
                    msg = obj.get("message", {})
                    content = msg.get("content", "")
                    if isinstance(content, list):
                        for block in content:
                            if isinstance(block, dict) and block.get("type") == "text":
                                entities = extract_all_json_arrays(block.get("text", ""))
                                all_entities.extend(entities)
                    elif isinstance(content, str):
                        entities = extract_all_json_arrays(content)
                        all_entities.extend(entities)
            except json.JSONDecodeError:
                continue
    return all_entities


def main():
    if len(sys.argv) < 4:
        print("Usage: python extract_from_task.py <input_jsonl> <output_json> <domain>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    domain = sys.argv[3]

    entities = extract_from_jsonl(input_path)

    # Deduplicate by name
    seen = set()
    unique = []
    for e in entities:
        name = e.get("name", "")
        if name and name not in seen:
            seen.add(name)
            unique.append(e)

    result = {
        "domain": domain,
        "entities": unique,
        "researchers": [],
        "relations": [],
        "cross_domain_relations": []
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(unique)} unique entities -> {output_path}")


if __name__ == "__main__":
    main()
