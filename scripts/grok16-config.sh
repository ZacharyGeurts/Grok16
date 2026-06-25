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
  G16_PKGVERSION="${G16_PKGVERSION:-Grok16-16.0.0}"
  GROK16_BUILD_JOBS="${GROK16_BUILD_JOBS:-${QUEEN_BUILD_JOBS:-$(nproc 2>/dev/null || echo 4)}}"
  export GROK16_ROOT GROK16_SCRIPTS G16_PREFIX GROK16_SG_ROOT GROK16_QUEEN_ROOT
  export GROK16_GCC_SRC GROK16_GCC_BUILD GROK16_GCC_REPO GROK16_GCC_BRANCH
  export G16_PKGVERSION GROK16_BUILD_JOBS
  export GROK16_ROOT  # forge engine reads GROK16_ROOT
}

_grok16_config_resolve

if [[ -n ${GROK16_CONFIG_ONLY:-} ]]; then
  return 0 2>/dev/null || exit 0
fi