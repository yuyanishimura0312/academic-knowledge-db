#!/usr/bin/env python3
"""Extract JSON array from agent output files and save as import-ready files."""

import re
import json
import sys
from pathlib import Path

def extract_json_array(text):
    """Extract the first JSON array from text containing ```json blocks."""
    pattern = r'```json\s*(\[[\s\S]*?\])\s*```'
    match = re.search(pattern, text)
    if match:
        return json.loads(match.group(1))
    # Try finding raw JSON array
    pattern2 = r'(\[\s*\{[\s\S]*?\}\s*\])'
    match2 = re.search(pattern2, text)
    if match2:
        try:
            return json.loads(match2.group(1))
        except json.JSONDecodeError:
            pass
    return None

def process_agent_output(input_path, output_path, domain):
    """Read agent output, extract JSON, wrap in import format."""
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    entities = extract_json_array(text)
    if not entities:
        print(f"ERROR: No JSON array found in {input_path}")
        return 0

    result = {
        "domain": domain,
        "entities": entities,
        "researchers": [],
        "relations": [],
        "cross_domain_relations": []
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(entities)} entities -> {output_path}")
    return len(entities)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python extract_json.py <input> <output> <domain>")
        sys.exit(1)
    process_agent_output(sys.argv[1], sys.argv[2], sys.argv[3])
