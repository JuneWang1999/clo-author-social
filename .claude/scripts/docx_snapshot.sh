#!/bin/bash
# docx_snapshot.sh — Read-only Markdown snapshot of a Word file for agents.
#
# Usage: .claude/scripts/docx_snapshot.sh [paper/manuscript.docx] [output.md]
# Default output: quality_reports/snapshots/<name>_<YYYY-MM-DD>.md (+ _media/ for images)
#
# Includes tracked changes and comments (pandoc --track-changes=all), so critics
# see pending edits. Never modifies the .docx. Agents read the snapshot; they
# never edit the snapshot expecting the change to reach Word.
set -euo pipefail
IN="${1:-paper/manuscript.docx}"
[[ -f "$IN" ]] || { echo "No such file: $IN" >&2; exit 1; }
NAME="$(basename "${IN%.docx}")"
OUT="${2:-quality_reports/snapshots/${NAME}_$(date +%Y-%m-%d).md}"
mkdir -p "$(dirname "$OUT")"
MEDIA="${OUT%.md}_media"
pandoc "$IN" --track-changes=all --wrap=none --extract-media="$MEDIA" -t markdown -o "$OUT"
echo "Snapshot: $OUT ($(wc -w < "$OUT" | tr -d ' ') words)"
