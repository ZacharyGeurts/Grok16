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
    exec bash "${_AML_ROOT}/lib/ammolang-run.sh" exec "script:Grok16/scripts/grok16-riscv-smoke.sh" "$@"
  fi
fi
unset -f _aml_find_root 2>/dev/null || true

#!/usr/bin/env bash
# RISC-V cross-compile smoke — optional gate when linux-gnu-riscv64 toolchain present.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TRIPLE="${G16_RISCV_TRIPLE:-riscv64-linux-gnu}"
GCC="${TRIPLE}-gcc"
if ! command -v "$GCC" >/dev/null 2>&1; then
  echo "riscv-smoke: skip — $GCC not in PATH"
  exit 0
fi
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cat >"$TMP/smoke.c" <<'EOF'
int main(void) { return 0; }
EOF
"$GCC" -O2 -o "$TMP/smoke" "$TMP/smoke.c"
file "$TMP/smoke" | grep -qi riscv
echo "riscv-smoke: PASS ($TRIPLE)"