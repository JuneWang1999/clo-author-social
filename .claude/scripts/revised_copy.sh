#!/bin/bash
# revised_copy.sh — Turn an edited snapshot into a revised Word copy for Review › Compare.
#
# Usage: .claude/scripts/revised_copy.sh <edited_snapshot.md> <topic>
# Output: paper/revisions/manuscript_<YYYY-MM-DD>_<topic>.docx
#
# Workflow (Word-master phase, large rewrites only):
#   1. .claude/scripts/docx_snapshot.sh             (fresh snapshot of paper/manuscript.docx)
#   2. copy the snapshot, edit the copy, keep the original snapshot untouched
#   3. this script -> revised .docx with the APA reference styles
#   4. the user runs Word: Review › Compare › Compare Documents
#      (original = paper/manuscript.docx, revised = the new copy) and accepts/rejects
# Never writes to paper/manuscript.docx. Run with tracked changes in the snapshot
# resolved (accept or reject them in the copy first) so Compare shows only new edits.
set -euo pipefail
SRC="${1:?usage: revised_copy.sh <edited_snapshot.md> <topic>}"
TOPIC="${2:?usage: revised_copy.sh <edited_snapshot.md> <topic>}"
OUT="paper/revisions/manuscript_$(date +%Y-%m-%d)_${TOPIC}.docx"
[[ "$OUT" != "paper/manuscript.docx" ]] || exit 1
[[ -e "$OUT" ]] && { echo "$OUT exists — pick a different topic name." >&2; exit 1; }
mkdir -p paper/revisions
pandoc "$SRC" -o "$OUT" --reference-doc=paper/word/apa7-reference.docx \
  --resource-path="$(dirname "$SRC"):paper"
echo "Revised copy: $OUT — compare it with paper/manuscript.docx in Word (Review › Compare)."
