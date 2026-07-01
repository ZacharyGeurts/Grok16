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
    exec bash "${_AML_ROOT}/lib/ammolang-run.sh" exec "script:Grok16/scripts/g16-combinatronic-rebalance.sh" "$@"
  fi
fi
unset -f _aml_find_root 2>/dev/null || true

#!/usr/bin/env bash
# G16 Universal Combinatronic — rebalance, condense, combine, connect optimally.
set -euo pipefail
SG_ROOT="${SG_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"
export SG_ROOT
export NEXUS_INSTALL_ROOT="${NEXUS_INSTALL_ROOT:-$SG_ROOT/NewLatest}"
export NEXUS_STATE_DIR="${NEXUS_STATE_DIR:-$NEXUS_INSTALL_ROOT/.nexus-state}"
export GROK16_ROOT="${GROK16_ROOT:-$SG_ROOT/Grok16}"
PY="${PYTHON:-python3}"
REB="$NEXUS_INSTALL_ROOT/lib/g16-combinatronic-rebalance.py"
ACTION="${1:-optimal}"
shift || true
exec "$PY" "$REB" "$ACTION" "$@"