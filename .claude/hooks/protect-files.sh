#!/bin/bash
# Block accidental edits to protected files
# Customize PROTECTED_PATTERNS below for your project
#
# Also enforces INV-25: the user's Word/PowerPoint masters
# (paper/manuscript.docx, paper/talks/<name>.pptx) are never written,
# moved, or deleted by Claude — via Edit/Write or via Bash.
INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')
FILE=""

# ============================================================
# Masters owned by the user (INV-25)
# ============================================================
is_master() {
  case "$1" in
    *paper/manuscript.docx) return 0 ;;
    *paper/talks/drafts/*) return 1 ;;
    *paper/talks/reference.pptx) return 1 ;;
    *paper/talks/*.pptx) return 0 ;;
  esac
  return 1
}

if [ "$TOOL" = "Bash" ]; then
  CMD=$(echo "$INPUT" | jq -r '.tool_input.command // empty')
  M='[^[:space:]|;&]*paper/(manuscript\.docx|talks/[^/[:space:]]+\.pptx)'
  hit=0
  # Output flags or redirects pointing at a master
  echo "$CMD" | grep -Eq "(-o[[:space:]]*|--output[= ]|>[[:space:]]*)$M" && hit=1
  # rm / mv / touch / truncate / zip anywhere on a master (unzip only reads, so it is allowed)
  echo "$CMD" | grep -Eq "(^|[[:space:];&|(])(rm|mv|touch|truncate|zip)[[:space:]][^|;&]*$M" && hit=1
  echo "$CMD" | grep -Eq "\bsed\b[^|;&]*-i[^|;&]*$M" && hit=1
  # cp / tee with a master as the destination (last argument); copying FROM it is fine
  echo "$CMD" | grep -Eq "(^|[[:space:];&|(])(cp|tee)[[:space:]][^|;&]*[[:space:]]$M[[:space:]]*($|[|;&])" && hit=1
  # Drafts and the talk design template are not masters
  echo "$CMD" | grep -Eq "\b(cp|tee)\b[^|;&]*[[:space:]][^[:space:]]*paper/talks/(drafts/|reference\.pptx)" && hit=0
  if [ "$hit" = 1 ]; then
    echo "Blocked: this command would modify a user-owned master (paper/manuscript.docx or paper/talks/*.pptx). Propose changes as a change list or a revised copy instead (INV-25)." >&2
    exit 2
  fi
  exit 0
fi

# Extract file path based on tool type
if [ "$TOOL" = "Edit" ] || [ "$TOOL" = "Write" ]; then
  FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
fi

# No file path = not a file operation, allow
if [ -z "$FILE" ]; then
  exit 0
fi

if is_master "$FILE"; then
  echo "Protected master: $(basename "$FILE") is owned by the user. Propose changes as a change list or revised copy (INV-25)." >&2
  exit 2
fi

# ============================================================
# CUSTOMIZE: Add patterns for files you want to protect
# Uses basename matching — add full paths for more precision
# ============================================================
PROTECTED_PATTERNS=(
  "settings.json"
  "strategy-memo-*.md"
  "referee-report-*.md"
  "quality-score-*.json"
)

BASENAME=$(basename "$FILE")
for PATTERN in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$BASENAME" == "$PATTERN" ]]; then
    echo "Protected file: $BASENAME. Edit manually or remove protection in .claude/hooks/protect-files.sh" >&2
    exit 2
  fi
done

exit 0
