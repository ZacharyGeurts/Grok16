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
    exec bash "${_AML_ROOT}/lib/ammolang-run.sh" exec "script:Grok16/scripts/grok16-forever.sh" "$@"
  fi
fi
unset -f _aml_find_root 2>/dev/null || true

#!/usr/bin/env bash
# Grok16 forever — full stack: binutils + g16 + languages + Hostess 7 gate
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export GROK16_ROOT="$ROOT" G16_PREFIX="${G16_PREFIX:-$ROOT}"

run() { echo "forever: $1"; "$@"; }

if [[ -x "$ROOT/scripts/grok16-binutils.sh" ]]; then
  run "$ROOT/scripts/grok16-binutils.sh" status || run "$ROOT/scripts/grok16-binutils.sh" bootstrap
fi
run "$ROOT/scripts/grok16-toolchain.sh" status || true
run "$ROOT/scripts/grok16-languages.sh" install
run "$ROOT/scripts/grok16-languages.sh" discern
run "$ROOT/scripts/grok16-toolchain.sh" test-battery
if "$ROOT/scripts/grok16-toolchain.sh" status >/dev/null 2>&1; then
  run "$ROOT/scripts/grok16-toolchain.sh" bench-compare
fi
run "$ROOT/scripts/grok16-languages.sh" hostess-gate
if [[ -x "$ROOT/scripts/grok16-integrate.sh" ]]; then
  run "$ROOT/scripts/grok16-integrate.sh" integrate
fi
if [[ -f "$ROOT/data/grok16-field-native.json" ]]; then
  echo "forever: field-native doctrine active"
fi
echo "forever: PASS — Hostess 7 satisfied, belt 2.0 integrated"