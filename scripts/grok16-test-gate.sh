#!/usr/bin/env bash
# Grok16 test gate — self-monitored per-step runs (heartbeat + stall/timeout drop-out).
# Usage: ./scripts/grok16-test-gate.sh [smoke|full]
set -uo pipefail

GROK16_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SG_ROOT="${SG_ROOT:-$(cd "$GROK16_ROOT/.." && pwd)}"
NL="$SG_ROOT/NewLatest"
MONITOR_SH="$GROK16_ROOT/scripts/g16-run-monitored.sh"
export GROK16_ROOT SG_ROOT
export NEXUS_INSTALL_ROOT="${NEXUS_INSTALL_ROOT:-$NL}"
export NEXUS_STATE_DIR="${NEXUS_STATE_DIR:-$NL/.nexus-state}"
export G16_MONITOR_HEARTBEAT_SEC="${G16_MONITOR_HEARTBEAT_SEC:-8}"
mkdir -p "$NEXUS_STATE_DIR"

MODE="${1:-smoke}"
FAIL=0
GATE_STARTED="$(date +%s)"

log() { printf '[%s] %s\n' "$(date +%H:%M:%S)" "$*"; }

run_t() {
  local name="$1" sec="$2"
  shift 2
  log "START $name (monitor timeout ${sec}s)"
  if bash "$MONITOR_SH" cmd "$name" "$sec" "$@"; then
    log "PASS $name"
    return 0
  fi
  local rc=$?
  if [[ $rc -eq 124 ]]; then
    log "DROP $name timeout"
  elif [[ $rc -eq 125 ]]; then
    log "DROP $name stall"
  else
    log "FAIL $name exit=$rc"
  fi
  FAIL=$((FAIL + 1))
  return "$rc"
}

log "grok16-test-gate mode=$MODE root=$GROK16_ROOT monitor=$MONITOR_SH"

run_t toolchain-smoke 300 bash "$GROK16_ROOT/scripts/grok16-toolchain.sh" test-battery
run_t py-battery 90 pythong "$GROK16_ROOT/tests/test_g16_battery.py"
run_t py-belt 120 pythong "$GROK16_ROOT/tests/test_g16_belt_battery.py"
run_t power-sort-apply 60 python3 "$GROK16_ROOT/lib/field-power-sort.py" apply
run_t power-sort-plate 60 python3 "$GROK16_ROOT/lib/g16-power-sort-plate.py" cycle
run_t combinatorics-fast 90 python3 "$GROK16_ROOT/lib/field_combinatorics.py" fast
run_t combinatorics-verify 90 python3 "$GROK16_ROOT/lib/field_combinatorics.py" verify
run_t chip-battery 90 pythong "$NL/lib/field-chip-battery.py" verify
run_t cpu-library 90 pythong "$NL/lib/field-cpu-library.py" verify
run_t self-monitor 30 python3 "$GROK16_ROOT/tests/test_g16_self_monitor.py"
run_t launch-verify 300 bash "$GROK16_ROOT/scripts/grok16-launch-verify.sh"

if [[ "$MODE" == "full" ]]; then
  run_t toolchain-release 600 bash "$GROK16_ROOT/scripts/grok16-toolchain.sh" test-battery-release
  run_t research-book 120 python3 "$GROK16_ROOT/lib/field-research-book.py" verify
fi

GATE_ELAPSED=$(( $(date +%s) - GATE_STARTED ))
if [[ "$FAIL" -eq 0 ]]; then
  log "grok16-test-gate: PASS ($MODE) wall=${GATE_ELAPSED}s"
  exit 0
fi
log "grok16-test-gate: FAIL ($FAIL steps) mode=$MODE wall=${GATE_ELAPSED}s"
exit 1