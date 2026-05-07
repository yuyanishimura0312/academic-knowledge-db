#!/bin/bash
# Phases 3-7 continuation: run after launch_codex_40 completes.
# Each phase is gated. Re-run safely.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
PROJECT="$(cd "$ROOT/.." && pwd)"
CUTOFF_FILE="$ROOT/.cutoff_iso"

cd "$ROOT"

if [ ! -f "$CUTOFF_FILE" ]; then
  date -u +"%Y-%m-%dT%H:%M:%S" > "$CUTOFF_FILE"
fi
CUTOFF=$(cat "$CUTOFF_FILE")
echo "[continuation] cutoff: $CUTOFF"

echo "==[Phase 3]== validate & ingest"
python3 ingest_results.py
read -p "Press enter to commit ingest, Ctrl-C to abort: " _
python3 ingest_results.py --commit

echo "==[Phase 4]== build relations"
python3 build_relations.py --since "$CUTOFF"
read -p "Press enter to commit relations: " _
python3 build_relations.py --since "$CUTOFF" --commit

echo "==[Phase 5]== refresh dashboard data"
cd "$PROJECT"
sqlite3 academic.db "SELECT
  'humanities_concept' as t, COUNT(*) c FROM humanities_concept
  UNION ALL SELECT 'social_theory', COUNT(*) FROM social_theory
  UNION ALL SELECT 'natural_discovery', COUNT(*) FROM natural_discovery
  UNION ALL SELECT 'engineering_method', COUNT(*) FROM engineering_method
  UNION ALL SELECT 'arts_question', COUNT(*) FROM arts_question;" | tee "$ROOT/post_expansion_counts.txt"

echo "==[Phase 6]== verify (manual /doc-verify recommended)"
echo "  Run: /doc-verify (in Claude Code) or inspect post_expansion_counts.txt"

echo "==[Phase 7]== git commit & push"
cd "$PROJECT"
git add -A
git commit -m "feat: coverage expansion via Codex 40 parallel — $(wc -l < $ROOT/post_expansion_counts.txt) tables refreshed

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>" || echo "no changes to commit"
git push

echo "[continuation] done at $(date)"
