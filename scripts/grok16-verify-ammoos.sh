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
    exec bash "${_AML_ROOT}/lib/ammolang-run.sh" exec "script:Grok16/scripts/grok16-verify-ammoos.sh" "$@"
  fi
fi
unset -f _aml_find_root 2>/dev/null || true

#!/usr/bin/env bash
# Verify AmmoOS surfaces wired to Grok16 — profile smoke + launch-verify hooks
set -euo pipefail

GROK16_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SG_ROOT="${SG_ROOT:-$(cd "$GROK16_ROOT/.." && pwd)}"
NL="${NEXUS_INSTALL_ROOT:-$SG_ROOT/NewLatest}"
export GROK16_ROOT SG_ROOT NEXUS_INSTALL_ROOT="${NEXUS_INSTALL_ROOT:-$NL}"

log() { printf '[%s] verify-ammoos %s\n' "$(date +%H:%M:%S)" "$*"; }
FAIL=0

log "profile ammoos smoke (g16)"
if [[ -x "$GROK16_ROOT/bin/g16" ]]; then
  tmp="$(mktemp -d)"
  defs="$("$GROK16_ROOT/scripts/grok16-profile-flags.py" ammoos defs 2>/dev/null || true)"
  # Smoke gate: static no-pie (field desktop link uses profile PIE separately)
  # shellcheck disable=SC2086
  "$GROK16_ROOT/bin/g16" -std=gnu17 -O2 -fno-pie $defs -c -o "$tmp/ammoos_smoke.o" \
    "$GROK16_ROOT/examples/ammoos-smoke/ammoos_smoke.c" && \
  # shellcheck disable=SC2086
  "$GROK16_ROOT/bin/g16" -std=gnu17 -O2 -no-pie -static $defs -o "$tmp/ammoos_smoke" "$tmp/ammoos_smoke.o" && \
  "$tmp/ammoos_smoke" | grep -q 'ammoos-smoke ok' && \
    log "PASS g16 ammoos compile+run" || { log "FAIL g16 ammoos smoke"; FAIL=1; }
  rm -rf "$tmp"
else
  log "WARN g16 missing — skip compile smoke"
fi

if [[ -f "$NL/scripts/ammoos-launch-verify.sh" ]]; then
  log "AmmoOS launch-verify"
  if bash "$NL/scripts/ammoos-launch-verify.sh" 2>&1 | tail -5; then
    log "PASS ammoos-launch-verify"
  else
    log "WARN ammoos-launch-verify partial (non-fatal)"
  fi
fi

if [[ -f "$NL/data/field-stack-layer-doctrine.json" ]]; then
  log "field-stack-layer doctrine present"
fi

if [[ -f "$GROK16_ROOT/data/grok16-ammoos-integrate.json" ]]; then
  log "integrate manifest present"
else
  log "WARN grok16-ammoos-integrate.json missing — run grok16-integrate.sh"
fi

[[ "$FAIL" -eq 0 ]] || exit 1
log "verify-ammoos: PASS"