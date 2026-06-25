#!/usr/bin/env bash
# One-time: pull Queen gcc/build into Grok16 and symlink Queen → Grok16 source
set -euo pipefail
GROK16="$(cd "$(dirname "$0")/.." && pwd)"
SG="$(cd "$GROK16/.." && pwd)"
QUEEN="$SG/NewLatest/Queen"

echo "Grok16 consolidate — whole G16 in $GROK16"

if [[ ! -d "$GROK16/vendor/gcc/.git" ]]; then
  if [[ -d "$QUEEN/vendor/gcc/.git" && ! -L "$QUEEN/vendor/gcc" ]]; then
    echo "Moving $QUEEN/vendor/gcc → $GROK16/vendor/gcc"
    mkdir -p "$GROK16/vendor"
    mv "$QUEEN/vendor/gcc" "$GROK16/vendor/gcc"
  else
    echo "No gcc source — run: $GROK16/scripts/grok16-toolchain.sh bootstrap" >&2
    exit 1
  fi
fi

if [[ -d "$QUEEN/build/gcc" && ! -d "$GROK16/build/gcc" ]]; then
  echo "Moving $QUEEN/build/gcc → $GROK16/build/gcc"
  mkdir -p "$GROK16/build"
  mv "$QUEEN/build/gcc" "$GROK16/build/gcc"
fi

mkdir -p "$QUEEN/vendor"
ln -sfn "$GROK16/vendor/gcc" "$QUEEN/vendor/gcc"
echo "Queen vendor/gcc → Grok16/vendor/gcc"

cat "$GROK16/vendor/gcc/gcc/BASE-VER"
git -C "$GROK16/vendor/gcc" branch --show-current
"$GROK16/scripts/grok16-toolchain.sh" status