# AmmoLang boundary route — AML_BUILD=1 universal boundary
_aml_find_root() {
  local d="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  while [[ "$d" != "/" ]]; do
    [[ -f "$d/lib/ammolang-run.sh" ]] && echo "$d" && return 0
    d="$(dirname "$d")"
  done
  return 1
}
if [[ "${AML_BUILD:-1}" != "0" ]] && [[ -z "${AML_BOUNDARY_ACTIVE:-}" ]]; then
  _AML_ROOT="$(_aml_find_root 2>/dev/null || true)"
  if [[ -n "$_AML_ROOT" ]]; then
    export AML_BOUNDARY_ACTIVE=1
    exec bash "${_AML_ROOT}/lib/ammolang-run.sh" exec "script:Grok16/scripts/consolidate.sh" "$@"
  fi
fi
unset -f _aml_find_root 2>/dev/null || true

#!/usr/bin/env bash
# One-time: pull Queen gcc/build into Grok16 and symlink Queen → Grok16 source
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=grok16-config.sh
source "$SCRIPT_DIR/grok16-config.sh"

QUEEN="$GROK16_QUEEN_ROOT"

echo "Grok16 consolidate — whole G16 in $GROK16_ROOT"
echo "  queen=$QUEEN"

if [[ ! -d "$GROK16_GCC_SRC/.git" ]]; then
  if [[ -d "$QUEEN/vendor/gcc/.git" && ! -L "$QUEEN/vendor/gcc" ]]; then
    echo "Moving $QUEEN/vendor/gcc → $GROK16_GCC_SRC"
    mkdir -p "$(dirname "$GROK16_GCC_SRC")"
    mv "$QUEEN/vendor/gcc" "$GROK16_GCC_SRC"
  else
    echo "No gcc source — run: $GROK16_ROOT/scripts/grok16-toolchain.sh bootstrap" >&2
    exit 1
  fi
fi

if [[ -d "$QUEEN/build/gcc" && ! -d "$GROK16_GCC_BUILD" ]]; then
  echo "Moving $QUEEN/build/gcc → $GROK16_GCC_BUILD"
  mkdir -p "$(dirname "$GROK16_GCC_BUILD")"
  mv "$QUEEN/build/gcc" "$GROK16_GCC_BUILD"
fi

if [[ ! -d "$GROK16_BINUTILS_SRC/.git" ]]; then
  if [[ -d "$QUEEN/vendor/binutils/.git" && ! -L "$QUEEN/vendor/binutils" ]]; then
    echo "Moving $QUEEN/vendor/binutils → $GROK16_BINUTILS_SRC"
    mkdir -p "$(dirname "$GROK16_BINUTILS_SRC")"
    mv "$QUEEN/vendor/binutils" "$GROK16_BINUTILS_SRC"
  fi
fi

mkdir -p "$QUEEN/vendor"
ln -sfn "$GROK16_GCC_SRC" "$QUEEN/vendor/gcc"
echo "Queen vendor/gcc → $GROK16_GCC_SRC"
if [[ -d "$GROK16_BINUTILS_SRC/.git" ]]; then
  ln -sfn "$GROK16_BINUTILS_SRC" "$QUEEN/vendor/binutils"
  echo "Queen vendor/binutils → $GROK16_BINUTILS_SRC"
fi

cat "$GROK16_GCC_SRC/gcc/BASE-VER"
git -C "$GROK16_GCC_SRC" branch --show-current
"$GROK16_ROOT/scripts/grok16-toolchain.sh" status