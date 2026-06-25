#!/usr/bin/env bash
# grok16-config.sh — shared path/env resolution (source from other scripts)
# Copyright (C) 2026 Zachary Geurts — GPLv3
# Usage: source "$(dirname "$0")/grok16-config.sh"   OR   GROK16_CONFIG_ONLY=1 source ...
set -euo pipefail

_grok16_config_resolve() {
  local script="${BASH_SOURCE[1]:-${BASH_SOURCE[0]}}"
  local scripts_dir
  scripts_dir="$(cd "$(dirname "$script")" && pwd)"
  GROK16_ROOT="${GROK16_ROOT:-$(cd "$scripts_dir/.." && pwd)}"
  GROK16_SCRIPTS="$scripts_dir"
  G16_PREFIX="${G16_PREFIX:-$GROK16_ROOT}"
  GROK16_SG_ROOT="${GROK16_SG_ROOT:-${SG_ROOT:-$(cd "$GROK16_ROOT/.." && pwd)}}"
  GROK16_QUEEN_ROOT="${GROK16_QUEEN_ROOT:-${QUEEN_ROOT:-$GROK16_SG_ROOT/NewLatest/Queen}}"
  GROK16_GCC_SRC="${GROK16_GCC_SRC:-$GROK16_ROOT/vendor/gcc}"
  GROK16_GCC_BUILD="${GROK16_GCC_BUILD:-$GROK16_ROOT/build/gcc}"
  GROK16_GCC_REPO="${GROK16_GCC_REPO:-https://gcc.gnu.org/git/gcc.git}"
  GROK16_GCC_BRANCH="${GROK16_GCC_BRANCH:-releases/gcc-15}"
  if [[ -f "$GROK16_ROOT/data/grok16-version.json" ]]; then
    eval "$(python3 - <<'PY'
import json, os
from pathlib import Path
root = Path(os.environ.get("GROK16_ROOT", "."))
doc = json.loads((root / "data/grok16-version.json").read_text(encoding="utf-8"))
for key in ("g16_version", "pkgversion", "cxx_std_default", "c_std_default"):
    val = doc.get(key, "")
    if val:
        env = {"g16_version": "G16_VERSION", "pkgversion": "G16_PKGVERSION",
               "cxx_std_default": "G16_CXX_STD", "c_std_default": "G16_C_STD"}[key]
        print(f'export {env}="{val}"')
PY
)"
  fi
  G16_VERSION="${G16_VERSION:-16.1.1}"
  G16_PKGVERSION="${G16_PKGVERSION:-Grok16-16.1.1}"
  G16_CXX_STD="${G16_CXX_STD:-gnu++26}"
  G16_C_STD="${G16_C_STD:-gnu17}"
  GROK16_BUILD_JOBS="${GROK16_BUILD_JOBS:-${QUEEN_BUILD_JOBS:-$(nproc 2>/dev/null || echo 4)}}"
  if [[ -z ${GROK16_USE_CCACHE:-} ]] && command -v ccache >/dev/null 2>&1; then
    GROK16_USE_CCACHE=1
  fi
  if [[ ${G16_RELEASE_PROFILE:-} == 1 || ${G16_RELEASE_PROFILE:-} == true ]]; then
    : "${G16_ENABLE_LTO:=1}"
    : "${G16_ENABLE_PGO:=1}"
    : "${G16_FIELD_SPEED:=1}"
  fi
  if [[ ${G16_FIELD_SPEED:-} == 1 || ${G16_FIELD_SPEED:-} == true ]]; then
    : "${G16_BENCH_PROFILE:=field_opt}"
  fi
  # Dev fast path default for rebuild iteration (override with G16_FULL_REBUILD=1)
  if [[ -z ${G16_FULL_REBUILD:-} && -z ${G16_FAST_REBUILD:-} ]]; then
    G16_FAST_REBUILD=1
  fi
  if [[ ${G16_FAST_REBUILD:-} == 1 || ${G16_FAST_REBUILD:-} == true || ${G16_FAST_REBUILD:-} == yes ]]; then
    : "${G16_DISABLE_BOOTSTRAP:=1}"
  fi
  export GROK16_ROOT GROK16_SCRIPTS G16_PREFIX GROK16_SG_ROOT GROK16_QUEEN_ROOT
  export GROK16_GCC_SRC GROK16_GCC_BUILD GROK16_GCC_REPO GROK16_GCC_BRANCH
  export G16_VERSION G16_PKGVERSION G16_CXX_STD G16_C_STD GROK16_BUILD_JOBS GROK16_USE_CCACHE
  export G16_RELEASE_PROFILE G16_FIELD_SPEED G16_FAST_REBUILD G16_FULL_REBUILD
  export GROK16_ROOT G16_DISABLE_BOOTSTRAP G16_ENABLE_LTO G16_ENABLE_PGO G16_BENCH_PROFILE
}

# Extra driver flags when install prefix lacks full lib/gcc (dev/consolidated layouts).
grok16_driver_extra_flags() {
  local ver="${G16_VERSION:-16.1.1}"
  local inc="$G16_PREFIX/lib/gcc/x86_64-pc-linux-gnu/${ver}/include"
  if [[ ! -d "$inc" && -d "$GROK16_GCC_BUILD/gcc" ]]; then
    printf -- '-B%s/gcc/\n' "$GROK16_GCC_BUILD"
  fi
}

_grok16_config_resolve

if [[ -n ${GROK16_CONFIG_ONLY:-} ]]; then
  return 0 2>/dev/null || exit 0
fi