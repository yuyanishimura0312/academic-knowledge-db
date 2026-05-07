#!/bin/bash
# Quick status check for the 40 Codex parallel run
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT" || exit 1

echo "=== Codex 40 status @ $(date +%H:%M:%S) ==="
total=$(ls prompts/*.md 2>/dev/null | wc -l | tr -d ' ')
done_count=$(find outputs -name '*.json' -size +100c 2>/dev/null | wc -l | tr -d ' ')
empty_count=$(find outputs -name '*.json' -size -100c 2>/dev/null | wc -l | tr -d ' ')
running=$(pgrep -fc "codex exec.*--full-auto" 2>/dev/null | head -1 || echo 0)

echo "  prompts ready: $total"
echo "  outputs >100b: $done_count"
echo "  outputs <100b (running/empty): $empty_count"
echo "  codex processes alive: $running"
echo ""
echo "=== outputs (size sorted) ==="
ls -laS outputs/ 2>/dev/null | grep -v '^total' | grep -v '^d' | head -15
echo ""
echo "=== recent master.log ==="
tail -10 master.log 2>/dev/null
