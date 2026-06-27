#!/usr/bin/env bash
# Verify Queen .launch chambers wired to Grok16 — json, project, run (monitored).
set -uo pipefail

GROK16_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SG_ROOT="${SG_ROOT:-$(cd "$GROK16_ROOT/.." && pwd)}"
NL="${NEXUS_INSTALL_ROOT:-$SG_ROOT/NewLatest}"
QUEEN="${QUEEN_ROOT:-$NL/Queen}"
CHAMBER_PY="$QUEEN/lib/queen-launch-chamber.py"
MONITOR_SH="$GROK16_ROOT/scripts/g16-run-monitored.sh"
export GROK16_ROOT SG_ROOT NEXUS_INSTALL_ROOT="${NEXUS_INSTALL_ROOT:-$NL}"
export NEXUS_STATE_DIR="${NEXUS_STATE_DIR:-$NL/.nexus-state}"
mkdir -p "$NEXUS_STATE_DIR"

FAIL=0
log() { printf '[%s] launch-verify %s\n' "$(date +%H:%M:%S)" "$*"; }

[[ -f "$CHAMBER_PY" ]] || { log "FAIL missing $CHAMBER_PY"; exit 1; }
[[ -x "$GROK16_ROOT/bin/g16" ]] || log "WARN g16 not installed — python launch lanes only"

verify_launch() {
  local launch="$1" name
  name="$(basename "$launch" .launch)"
  log "START $name"
  for cmd in json project; do
    if ! bash "$MONITOR_SH" cmd "launch-$name-$cmd" 45 \
        python3 "$CHAMBER_PY" "$cmd" "$launch"; then
      log "FAIL $name $cmd"
      FAIL=$((FAIL + 1))
      return 1
    fi
  done
  if ! bash "$MONITOR_SH" cmd "launch-$name-run" 90 \
      python3 "$CHAMBER_PY" run "$launch" --timeout 60; then
    log "FAIL $name run"
    FAIL=$((FAIL + 1))
    return 1
  fi
  log "PASS $name"
  return 0
}

log "grok16-launch-verify queen=$QUEEN g16=$GROK16_ROOT"

mapfile -t LAUNCHES < <(find "$GROK16_ROOT/examples" -maxdepth 2 -name '*.launch' | sort)
if [[ ${#LAUNCHES[@]} -eq 0 ]]; then
  log "FAIL no .launch under examples/"
  exit 1
fi

for lp in "${LAUNCHES[@]}"; do
  verify_launch "$lp" || true
done

# field-g16-launch discovery (NEXUS panel lane)
if [[ -f "$NL/lib/field-g16-launch.py" ]]; then
  if bash "$MONITOR_SH" cmd "field-g16-launch-json" 60 \
      pythong "$NL/lib/field-g16-launch.py" json | grep -q 'field-g16-launch/v1'; then
    log "PASS field-g16-launch json"
  else
    log "FAIL field-g16-launch json"
    FAIL=$((FAIL + 1))
  fi
fi

if [[ "$FAIL" -eq 0 ]]; then
  log "grok16-launch-verify: PASS (${#LAUNCHES[@]} chambers)"
  exit 0
fi
log "grok16-launch-verify: FAIL ($FAIL steps)"
exit 1