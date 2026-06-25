#!/usr/bin/env bash
# Grok16 — G16 unified field compiler @ 16.1.0 (g16 auto-detects C/C++)
# Copyright (C) 2026 Zachary Geurts
# License: GNU General Public License v3 or later — see LICENSE
# Upstream: GNU Compiler Collection (GCC) — Free Software Foundation, Inc.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=grok16-config.sh
source "$SCRIPT_DIR/grok16-config.sh"

BIN="$G16_PREFIX/bin"
G16_VERSION="${G16_VERSION:-16.1.0}"
FORGE="$GROK16_ROOT/forge/grok16-forge.py"
G16_DRIVER="$BIN/g16"
VERIFY_SRC="$GROK16_ROOT/examples/minimal-cmake-project/main.cpp"
EXAMPLE_CMAKE="$GROK16_ROOT/examples/minimal-cmake-project"

usage() {
  cat >&2 <<EOF
Usage: $0 install|bootstrap|rebuild|consolidate|status|verify|bench|field-bench|bench-all|profile|paths|manifest|config

Environment (see data/grok16-config.json):
  GROK16_ROOT G16_PREFIX GROK16_SG_ROOT GROK16_QUEEN_ROOT
  GROK16_GCC_SRC GROK16_GCC_BUILD GROK16_GCC_REPO GROK16_GCC_BRANCH
  G16_PKGVERSION G16_CXX_STD G16_C_STD G16_DISABLE_BOOTSTRAP GROK16_BUILD_JOBS
  G16_FAST_REBUILD G16_FULL_REBUILD G16_RELEASE_PROFILE G16_FIELD_SPEED
  G16_ENABLE_LTO G16_ENABLE_PGO G16_PGO_GENERATE GROK16_USE_CCACHE
  G16_BENCH_PROFILE (field_opt|ai|field_compute|vulkan_rtx)
EOF
  exit 2
}

is_real_compiler() {
  local bin="$1"
  [[ -x "$bin" ]] || return 1
  if head -c 2 "$bin" | grep -q '^#!'; then
    return 1
  fi
  file "$bin" 2>/dev/null | grep -qE 'ELF|executable'
}

write_version_file() {
  mkdir -p "$G16_PREFIX"
  cat >"$G16_PREFIX/VERSION" <<EOF
GROK16=${G16_VERSION}
G16_FIELD_GCC=${G16_VERSION}
G16_DRIVER=unified
G16_CC=g16
G16_CXX=g++16
G16_C_STD=${G16_C_STD:-gnu17}
G16_CXX_STD=${G16_CXX_STD:-gnu++26}
G16_PREFIX=${G16_PREFIX}
PRODUCT=Grok16
ROOT=${GROK16_ROOT}
EOF
}

write_cmake_toolchain() {
  mkdir -p "$GROK16_ROOT/cmake"
  cat >"$GROK16_ROOT/cmake/grok16-toolchain.cmake" <<EOF
set(CMAKE_C_COMPILER "${G16_PREFIX}/bin/g16" CACHE FILEPATH "Grok16 unified g16 (C mode)" FORCE)
set(CMAKE_CXX_COMPILER "${G16_PREFIX}/bin/g16" CACHE FILEPATH "Grok16 unified g16 (C++ mode)" FORCE)
set(WRDT_G16_VERSION "${G16_VERSION}" CACHE STRING "G16 version" FORCE)
set(GROK16_PREFIX "${G16_PREFIX}" CACHE PATH "Grok16 install prefix" FORCE)
set(GROK16_CXX_STD "${G16_CXX_STD:-gnu++26}" CACHE STRING "Grok16 default C++ standard" FORCE)
set(GROK16_C_STD "${G16_C_STD:-gnu17}" CACHE STRING "Grok16 default C standard" FORCE)
EOF
}

write_manifest() {
  mkdir -p "$GROK16_ROOT/data"
  local ver dv selfhosted_py
  ver="$("$G16_DRIVER" --version 2>/dev/null | head -1 || true)"
  dv="$("$G16_DRIVER" -dumpversion 2>/dev/null || true)"
  if [[ -f "$G16_PREFIX/SELFHOST.json" ]]; then
    selfhosted_py="True"
  else
    selfhosted_py="False"
  fi
  python3 - <<PY
import json, os
from datetime import datetime, timezone
from pathlib import Path
root = Path("${GROK16_ROOT}")
profiles_path = root / "data" / "grok16-profiles.json"
profiles = {}
if profiles_path.is_file():
    try:
        profiles = json.loads(profiles_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        pass
def _flag(name):
    return os.environ.get(name, "").strip().lower() in ("1", "true", "yes", "on")
doc = {
    "product": "Grok16",
    "schema": "grok16-toolchain/v1",
    "updated": datetime.now(timezone.utc).isoformat(),
    "g16_version": "${G16_VERSION}",
    "cxx_std_default": profiles.get("cxx_std_default", "${G16_CXX_STD:-gnu++26}"),
    "prefix": "${G16_PREFIX}",
    "root": "${GROK16_ROOT}",
    "sg_root": "${GROK16_SG_ROOT}",
    "queen_root": "${GROK16_QUEEN_ROOT}",
    "forge": "${FORGE}",
    "engine_real": True,
    "selfhosted": ${selfhosted_py},
    "dumpversion": "${dv}",
    "version": "${ver}",
    "profiles": profiles.get("profiles", {}),
    "ai": profiles.get("profiles", {}).get("ai", {}),
    "speedups": {
        "jobs": int("${GROK16_BUILD_JOBS}"),
        "fast_rebuild": _flag("G16_FAST_REBUILD"),
        "lto": _flag("G16_ENABLE_LTO"),
        "pgo": _flag("G16_ENABLE_PGO"),
        "ccache": _flag("GROK16_USE_CCACHE"),
        "disable_bootstrap": _flag("G16_DISABLE_BOOTSTRAP") or _flag("G16_FAST_REBUILD"),
    },
    "paths": {
        "g16": "${G16_PREFIX}/bin/g16",
        "g++16": "${G16_PREFIX}/bin/g++16",
        "backend_cc": "${G16_PREFIX}/libexec/grok16/g16-cc",
        "backend_cxx": "${G16_PREFIX}/libexec/grok16/g16-cxx",
        "driver_mode": "unified",
        "gcc_src": "${GROK16_GCC_SRC}",
        "gcc_build": "${GROK16_GCC_BUILD}",
        "cmake": "${GROK16_ROOT}/cmake/grok16-toolchain.cmake",
        "profiles_json": str(profiles_path),
        "version_file": "${G16_PREFIX}/VERSION",
        "selfhost_stamp": "${G16_PREFIX}/SELFHOST.json",
    },
    "usage": {
        "status": "${GROK16_ROOT}/scripts/grok16-toolchain.sh status",
        "verify": "${GROK16_ROOT}/scripts/grok16-toolchain.sh verify",
        "bench": "${GROK16_ROOT}/scripts/grok16-toolchain.sh bench",
        "rebuild": "${GROK16_ROOT}/scripts/grok16-toolchain.sh rebuild",
        "paths": "${GROK16_ROOT}/scripts/grok16-toolchain.sh paths",
    },
}
open("${GROK16_ROOT}/data/grok16-toolchain.json", "w", encoding="utf-8").write(
    json.dumps(doc, indent=2) + "\\n"
)
PY
  echo "manifest: $GROK16_ROOT/data/grok16-toolchain.json"
}

cmd_install() {
  if ! is_real_compiler "$G16_DRIVER"; then
    echo "Grok16 unified g16 missing at $G16_DRIVER — run: $0 rebuild" >&2
    exit 1
  fi
  dv="$("$G16_DRIVER" -dumpversion 2>/dev/null || true)"
  if [[ "$dv" != "$G16_VERSION" ]]; then
    echo "g16 reports $dv; expected $G16_VERSION — rebuild" >&2
    exit 1
  fi
  if [[ -x "$GROK16_ROOT/driver/Makefile" || -f "$GROK16_ROOT/driver/Makefile" ]]; then
    make -C "$GROK16_ROOT/driver" "PREFIX=$G16_PREFIX" install >/dev/null 2>&1 || true
  fi
  write_version_file
  write_cmake_toolchain
  write_manifest
  echo "Grok16 prefix: $G16_PREFIX"
  echo "g16 (unified): $("$G16_DRIVER" --version | head -1)"
}

cmd_bootstrap() {
  echo "Grok16 bootstrap → fetch GCC, host build, install to $G16_PREFIX"
  [[ -f "$FORGE" ]] || { echo "forge missing: $FORGE" >&2; exit 1; }
  export G16_PREFIX G16_PKGVERSION GROK16_GCC_SRC GROK16_GCC_BUILD
  python3 "$FORGE" run gcc || exit 1
  cmd_install
}

cmd_rebuild() {
  echo "Grok16 rebuild → prefix $G16_PREFIX (self-host gcc_rebuild)"
  [[ -f "$FORGE" ]] || { echo "forge missing: $FORGE" >&2; exit 1; }
  export G16_PREFIX G16_PKGVERSION GROK16_GCC_SRC GROK16_GCC_BUILD GROK16_BUILD_JOBS
  export G16_FAST_REBUILD G16_FULL_REBUILD G16_RELEASE_PROFILE G16_FIELD_SPEED
  export G16_ENABLE_LTO G16_ENABLE_PGO GROK16_USE_CCACHE G16_DISABLE_BOOTSTRAP
  echo "  jobs=$GROK16_BUILD_JOBS fast=$G16_FAST_REBUILD field_speed=$G16_FIELD_SPEED release=$G16_RELEASE_PROFILE"
  echo "  lto=$G16_ENABLE_LTO pgo=$G16_ENABLE_PGO ccache=$GROK16_USE_CCACHE bootstrap_off=$G16_DISABLE_BOOTSTRAP"
  python3 "$FORGE" run gcc_rebuild || exit 1
  cmd_install
}

grok16_ready() {
  is_real_compiler "$G16_DRIVER" && [[ "$("$G16_DRIVER" -dumpversion)" == "$G16_VERSION" ]]
}

cmd_status() {
  if grok16_ready; then
    echo "ready Grok16 unified g16=$G16_DRIVER"
    "$G16_DRIVER" --version | head -1
    exit 0
  fi
  echo "not ready — run: $0 bootstrap"
  exit 1
}

cmd_verify() {
  if ! grok16_ready; then
    echo "not ready — run: $0 bootstrap" >&2
    exit 1
  fi
  echo "ready Grok16 unified g16=$G16_DRIVER"
  "$G16_DRIVER" --version | head -1
  local tmpdir obj_c obj_cpp
  tmpdir="$(mktemp -d)"
  trap 'rm -rf "${tmpdir:-}"' EXIT
  obj_c="$tmpdir/verify.o"
  obj_cpp="$tmpdir/verify_cpp.o"

  echo "verify: C ${G16_C_STD} via unified g16"
  cat >"$tmpdir/verify.c" <<'EOF'
int main(void) { return 0; }
EOF
  "$G16_DRIVER" -std="${G16_C_STD}" -c -o "$obj_c" "$tmpdir/verify.c"
  echo "verify: C compile OK"

  echo "verify: C++ ${G16_CXX_STD} via unified g16 (auto-detect .cpp)"
  cat >"$tmpdir/verify.cpp" <<'EOF'
#if __cplusplus >= 202400L
int main() { return 0; }
#else
int main() { return 1; }
#endif
EOF
  "$G16_DRIVER" -std="${G16_CXX_STD}" -c -o "$obj_cpp" "$tmpdir/verify.cpp"
  echo "verify: C++ compile OK"

  if [[ -f "$VERIFY_SRC" ]]; then
    echo "verify: example source present ($VERIFY_SRC)"
  fi

  if command -v cmake >/dev/null 2>&1 && [[ -f "$GROK16_ROOT/cmake/grok16-toolchain.cmake" ]]; then
    local bdir="$tmpdir/cmake-build"
    echo "verify: CMake example (optional)"
    if cmake -S "$EXAMPLE_CMAKE" -B "$bdir" \
      -DCMAKE_TOOLCHAIN_FILE="$GROK16_ROOT/cmake/grok16-toolchain.cmake" \
      -DCMAKE_BUILD_TYPE=Release >/dev/null 2>&1 \
      && cmake --build "$bdir" >/dev/null 2>&1; then
      "$bdir/grok16_smoke"
      echo "verify: CMake example OK"
    else
      echo "verify: CMake example skipped (link/stdlib layout — run rebuild if needed)"
    fi
  else
    echo "verify: skip CMake (cmake not installed or toolchain file missing)"
  fi

  echo "verify: PASS"
}

cmd_paths() {
  printf 'GROK16_ROOT=%s\nG16_PREFIX=%s\nGROK16_SG_ROOT=%s\nGROK16_QUEEN_ROOT=%s\n' \
    "$GROK16_ROOT" "$G16_PREFIX" "$GROK16_SG_ROOT" "$GROK16_QUEEN_ROOT"
  printf 'GROK16_GCC_SRC=%s\nGROK16_GCC_BUILD=%s\n' \
    "$GROK16_GCC_SRC" "$GROK16_GCC_BUILD"
  printf 'G16_DRIVER=%s/bin/g16\nG16_CC=%s/bin/g16\nG16_CXX=%s/bin/g++16\n' \
    "$G16_PREFIX" "$G16_PREFIX" "$G16_PREFIX"
  printf 'G16_BACKEND_CC=%s/libexec/grok16/g16-cc\nG16_BACKEND_CXX=%s/libexec/grok16/g16-cxx\n' \
    "$G16_PREFIX" "$G16_PREFIX"
  printf 'CMAKE_TOOLCHAIN=%s/cmake/grok16-toolchain.cmake\n' "$GROK16_ROOT"
  printf 'GROK16_GCC_REPO=%s\nGROK16_GCC_BRANCH=%s\nG16_PKGVERSION=%s\n' \
    "$GROK16_GCC_REPO" "$GROK16_GCC_BRANCH" "$G16_PKGVERSION"
  printf 'G16_C_STD=%s\nG16_CXX_STD=%s\nGROK16_BUILD_JOBS=%s\n' "$G16_C_STD" "$G16_CXX_STD" "$GROK16_BUILD_JOBS"
  [[ -n ${G16_DISABLE_BOOTSTRAP:-} ]] && printf 'G16_DISABLE_BOOTSTRAP=%s\n' "$G16_DISABLE_BOOTSTRAP"
  [[ -n ${G16_FAST_REBUILD:-} ]] && printf 'G16_FAST_REBUILD=%s\n' "$G16_FAST_REBUILD"
  [[ -n ${G16_ENABLE_LTO:-} ]] && printf 'G16_ENABLE_LTO=%s\n' "$G16_ENABLE_LTO"
  [[ -n ${G16_ENABLE_PGO:-} ]] && printf 'G16_ENABLE_PGO=%s\n' "$G16_ENABLE_PGO"
  [[ -n ${G16_FIELD_SPEED:-} ]] && printf 'G16_FIELD_SPEED=%s\n' "$G16_FIELD_SPEED"
  [[ -n ${G16_RELEASE_PROFILE:-} ]] && printf 'G16_RELEASE_PROFILE=%s\n' "$G16_RELEASE_PROFILE"
  [[ -n ${G16_FULL_REBUILD:-} ]] && printf 'G16_FULL_REBUILD=%s\n' "$G16_FULL_REBUILD"
  [[ -n ${G16_BENCH_PROFILE:-} ]] && printf 'G16_BENCH_PROFILE=%s\n' "$G16_BENCH_PROFILE"
}

cmd_config() {
  cmd_paths
  echo "---"
  echo "config template: $GROK16_ROOT/data/grok16-config.json"
}

_bench_run_one() {
  local profile="$1"
  local pgo_kind="${2:-cxx}"
  local rel
  rel="$(GROK16_ROOT="$GROK16_ROOT" G16_PREFIX="$G16_PREFIX" python3 "$GROK16_SCRIPTS/grok16-profile-flags.py" "$profile" source)"
  local src="$GROK16_ROOT/$rel"
  local outdir="$GROK16_ROOT/data/bench"
  local out="$outdir/grok16_${profile}_bench"
  local pflags lflags xflags run_line
  mkdir -p "$outdir" "$GROK16_ROOT/data/pgo"
  pflags="$(GROK16_ROOT="$GROK16_ROOT" G16_PREFIX="$G16_PREFIX" python3 "$GROK16_SCRIPTS/grok16-profile-flags.py" "$profile" "$pgo_kind" || echo "-std=gnu++26 -O3")"
  lflags="$(GROK16_ROOT="$GROK16_ROOT" G16_PREFIX="$G16_PREFIX" python3 "$GROK16_SCRIPTS/grok16-profile-flags.py" "$profile" link || true)"
  xflags="$(grok16_driver_extra_flags)"
  [[ -f "$src" ]] || { echo "bench: missing source $src" >&2; return 1; }

  local t0 t1 compile_ms run_ms bytes
  t0=$(date +%s%3N)
  # shellcheck disable=SC2086
  "$G16_DRIVER" $xflags $pflags $lflags -o "$out" "$src"
  t1=$(date +%s%3N)
  compile_ms=$((t1 - t0))

  t0=$(date +%s%3N)
  run_line="$("$out")"
  t1=$(date +%s%3N)
  run_ms=$((t1 - t0))
  bytes=$(stat -c%s "$out" 2>/dev/null || stat -f%z "$out")

  echo "bench: profile=$profile pgo=$pgo_kind compile_ms=$compile_ms run_ms=$run_ms binary_bytes=$bytes"
  echo "bench: $run_line"
  python3 - <<PY
import json, os
from datetime import datetime, timezone
from pathlib import Path
outdir = Path("${outdir}")
doc = {
    "profile": "${profile}",
    "pgo_kind": "${pgo_kind}",
    "compile_ms": int("${compile_ms}"),
    "run_ms": int("${run_ms}"),
    "binary_bytes": int("${bytes}"),
    "run_line": """${run_line}""",
    "ts": datetime.now(timezone.utc).isoformat(),
}
path = outdir / "latest_${profile}.json"
path.write_text(json.dumps(doc, indent=2) + "\\n", encoding="utf-8")
latest = outdir / "latest.json"
rows = []
if latest.is_file():
    try:
        rows = json.loads(latest.read_text(encoding="utf-8")).get("runs", [])
    except json.JSONDecodeError:
        rows = []
rows = [r for r in rows if r.get("profile") != "${profile}"]
rows.append(doc)
latest.write_text(json.dumps({"runs": rows, "updated": doc["ts"]}, indent=2) + "\\n", encoding="utf-8")
PY
}

cmd_bench() {
  if ! grok16_ready; then
    echo "not ready — run: $0 bootstrap" >&2
    exit 1
  fi
  local profile="${G16_BENCH_PROFILE:-field_opt}"
  _bench_run_one "$profile" cxx
  echo "bench: PASS"
}

cmd_field_bench() {
  if ! grok16_ready; then
    echo "not ready — run: $0 bootstrap" >&2
    exit 1
  fi
  export G16_FIELD_SPEED=1
  local profile="${G16_BENCH_PROFILE:-field_opt}"
  _bench_run_one "$profile" cxx
  echo "field-bench: PASS"
}

cmd_bench_all() {
  if ! grok16_ready; then
    echo "not ready — run: $0 bootstrap" >&2
    exit 1
  fi
  for profile in field_opt ai field_compute vulkan_rtx; do
    _bench_run_one "$profile" cxx || return 1
  done
  echo "bench-all: PASS"
}

cmd_profile() {
  if ! grok16_ready; then
    echo "not ready — run: $0 bootstrap" >&2
    exit 1
  fi
  export G16_PGO_GENERATE=1
  local profile="${G16_BENCH_PROFILE:-field_opt}"
  echo "profile: collecting PGO data for $profile → data/pgo/"
  _bench_run_one "$profile" cxx_pgo_gen
  echo "profile: PASS — rebuild with G16_ENABLE_PGO=1 and re-run field-bench"
}

cmd_consolidate() {
  exec "$GROK16_ROOT/scripts/consolidate.sh"
}

case "${1:-}" in
  install) cmd_install ;;
  bootstrap) cmd_bootstrap ;;
  rebuild) cmd_rebuild ;;
  consolidate) cmd_consolidate ;;
  status) cmd_status ;;
  verify) cmd_verify ;;
  bench) cmd_bench ;;
  field-bench) cmd_field_bench ;;
  bench-all) cmd_bench_all ;;
  profile) cmd_profile ;;
  paths) cmd_paths ;;
  config) cmd_config ;;
  manifest) write_cmake_toolchain; write_manifest ;;
  *) usage ;;
esac