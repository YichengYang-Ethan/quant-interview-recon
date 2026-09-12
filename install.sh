#!/usr/bin/env bash
# Install quant-interview-recon as a Claude Code skill.
#
#   ./install.sh            # symlink (recommended — git pull updates the skill)
#   ./install.sh --copy     # copy instead, if you don't want a symlink
#
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO/skill/quant-interview-recon"
DEST_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
DEST="$DEST_DIR/quant-interview-recon"
MODE="symlink"
[[ "${1:-}" == "--copy" ]] && MODE="copy"

[[ -d "$SRC" ]] || { echo "error: $SRC not found — run this from inside the repo" >&2; exit 1; }
mkdir -p "$DEST_DIR"

if [[ -e "$DEST" || -L "$DEST" ]]; then
  echo "note: $DEST already exists — replacing"
  rm -rf "$DEST"
fi

if [[ "$MODE" == "symlink" ]]; then
  ln -s "$SRC" "$DEST"
  echo "linked  $DEST -> $SRC"
else
  cp -R "$SRC" "$DEST"
  echo "copied  $SRC -> $DEST"
fi

chmod +x "$SRC/scripts/"*.py 2>/dev/null || true

echo
echo "Checking dependencies:"
command -v python3 >/dev/null && echo "  ok   python3 ($(python3 --version 2>&1))" || echo "  MISS python3 — required"
command -v pandoc  >/dev/null && echo "  ok   pandoc"  || echo "  MISS pandoc  — PDF disabled. brew install pandoc"
if command -v xelatex >/dev/null || command -v tectonic >/dev/null; then
  echo "  ok   LaTeX engine"
else
  echo "  MISS xelatex — PDF disabled. brew install --cask mactex-no-gui   (or: brew install tectonic)"
fi
command -v gh >/dev/null && echo "  ok   gh (optional)" || echo "  --   gh not found (optional)"

echo
echo "Smoke test:"
python3 "$SRC/scripts/qbank.py" --help >/dev/null 2>&1 \
  && echo "  ok   qbank.py runs" \
  || { echo "  FAIL qbank.py did not run" >&2; exit 1; }

echo
echo "Done. In Claude Code, run:  /quant-interview-recon Optiver QT"
