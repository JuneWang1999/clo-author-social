#!/bin/bash
# build_talk.sh — Build a PowerPoint talk from Markdown slides.
#
# Usage (from the project root):
#   paper/talks/build_talk.sh <name>            # -> paper/talks/drafts/<name>_draft.pptx
#   paper/talks/build_talk.sh <name> --handoff  # -> paper/talks/<name>.pptx (MASTER)
#
# Source: paper/talks/<name>.md (pandoc slide Markdown: one "## Title" per slide,
# "::: notes" for speaker notes). Design: paper/talks/reference.pptx — replace it
# with your institution's template (keep its layout names) to restyle every talk.
# --handoff refuses to overwrite an existing master: once you edit the .pptx in
# PowerPoint, it is the source of truth.
set -euo pipefail
NAME="${1:?usage: build_talk.sh <name> [--handoff]}"
DIR="$(cd "$(dirname "$0")" && pwd)"
SRC="$DIR/$NAME.md"
MASTER="$DIR/$NAME.pptx"
DRAFT="$DIR/drafts/${NAME}_draft.pptx"
[[ -f "$SRC" ]] || { echo "No slide source: $SRC" >&2; exit 1; }
if [[ "${2:-}" == "--handoff" && -e "$MASTER" ]]; then
  echo "$MASTER already exists — it is the master copy and will not be overwritten." >&2
  exit 1
fi
mkdir -p "$DIR/drafts"
pandoc "$SRC" -o "$DRAFT" --reference-doc="$DIR/reference.pptx" \
  --resource-path="$DIR:$DIR/../figures:$DIR/.." --slide-level=2
if [[ "${2:-}" == "--handoff" ]]; then
  cp -n "$DRAFT" "$MASTER"
  echo "Master copy created: $MASTER — edit it in PowerPoint from now on."
else
  echo "Draft built: $DRAFT"
fi
