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
    exec bash "${_AML_ROOT}/lib/ammolang-run.sh" exec "script:Grok16/scripts/grok16-bench-refresh.sh" "$@"
  fi
fi
unset -f _aml_find_root 2>/dev/null || true

#!/usr/bin/env bash
# Regenerate all speed + comparison benchmarks and SVG charts.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=grok16-config.sh
source "$SCRIPT_DIR/grok16-config.sh"

export G16_BENCH_RUNS="${G16_BENCH_RUNS:-1}"
export G16_BENCH_PROFILE="${G16_BENCH_PROFILE:-field_opt}"
export SPEED_DEMO_TARGET_SEC="${SPEED_DEMO_TARGET_SEC:-3}"

log() { echo "[bench-refresh] $*"; }

if ! [[ -x "$G16_PREFIX/bin/g16" ]]; then
  log "WARN: g16 not ready — charts will use last JSON on disk"
fi

log "1/6 bench-triad (host gcc vs belt_1_0 vs belt_2_0)"
"$GROK16_SCRIPTS/grok16-bench-triad.sh" triad || log "triad skipped/failed"

log "2/6 bench-compare (field g16 vs host)"
"$GROK16_SCRIPTS/grok16-bench-compare.sh" compare || log "compare skipped/failed"

log "3/6 bench-all (profile suite)"
"$GROK16_SCRIPTS/grok16-toolchain.sh" bench-all || log "bench-all skipped/failed"

log "4/6 exec-comprehensive-bench (speed_demo full pipeline)"
python3 "$GROK16_SCRIPTS/field-exec-comprehensive-bench.py" || log "comprehensive bench partial"

log "5/6 bench-charts (SVG)"
python3 "$GROK16_SCRIPTS/grok16-bench-charts.py"

log "6/6 build-manual (HTML pages)"
python3 "$GROK16_ROOT/docs/build-manual.py" || true

log "DONE — charts in docs/assets/ · JSON in data/bench/ · docs/field-exec-full-bench.json"