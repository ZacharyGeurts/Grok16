#!/usr/bin/env bash
# Grok16 — G16 field compiler @ 16.0.0 (real ELF g16/g++16, no wrappers)
# Install prefix: /home/default/Desktop/SG/Grok16
set -euo pipefail
GROK16="$(cd "$(dirname "$0")/.." && pwd)"
SG="$(cd "$GROK16/.." && pwd)"
QUEEN="$SG/NewLatest/Queen"
G16_PREFIX="${G16_PREFIX:-$GROK16}"
BIN="$G16_PREFIX/bin"
G16_VERSION="16.0.0"
FORGE="$QUEEN/lib/queen-forge.py"

usage() {
  echo "Usage: $0 install|rebuild|status|paths|manifest" >&2
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
G16_CXX=g++16
G16_CC=g16
G16_PREFIX=${G16_PREFIX}
PRODUCT=Grok16
ROOT=${GROK16}
EOF
}

write_cmake_toolchain() {
  mkdir -p "$GROK16/cmake"
  cat >"$GROK16/cmake/grok16-toolchain.cmake" <<EOF
set(CMAKE_C_COMPILER "${G16_PREFIX}/bin/g16" CACHE FILEPATH "Grok16 G16 C compiler" FORCE)
set(CMAKE_CXX_COMPILER "${G16_PREFIX}/bin/g++16" CACHE FILEPATH "Grok16 G16 C++ compiler" FORCE)
set(WRDT_G16_VERSION "${G16_VERSION}" CACHE STRING "G16 version" FORCE)
set(GROK16_PREFIX "${G16_PREFIX}" CACHE PATH "Grok16 install prefix" FORCE)
EOF
}

write_manifest() {
  mkdir -p "$GROK16/data"
  local ver dv selfhosted_py
  ver="$("$BIN/g++16" --version 2>/dev/null | head -1 || true)"
  dv="$("$BIN/g++16" -dumpversion 2>/dev/null || true)"
  if [[ -f "$G16_PREFIX/SELFHOST.json" ]]; then
    selfhosted_py="True"
  else
    selfhosted_py="False"
  fi
  python3 - <<PY
import json
from datetime import datetime, timezone
doc = {
    "product": "Grok16",
    "schema": "grok16-toolchain/v1",
    "updated": datetime.now(timezone.utc).isoformat(),
    "g16_version": "${G16_VERSION}",
    "prefix": "${G16_PREFIX}",
    "root": "${GROK16}",
    "sg_root": "${SG}",
    "forge": "${QUEEN}",
    "engine_real": True,
    "selfhosted": ${selfhosted_py},
    "dumpversion": "${dv}",
    "version": "${ver}",
    "paths": {
        "g16": "${G16_PREFIX}/bin/g16",
        "g++16": "${G16_PREFIX}/bin/g++16",
        "cmake": "${GROK16}/cmake/grok16-toolchain.cmake",
        "version_file": "${G16_PREFIX}/VERSION",
        "selfhost_stamp": "${G16_PREFIX}/SELFHOST.json",
    },
    "usage": {
        "status": "${GROK16}/scripts/grok16-toolchain.sh status",
        "rebuild": "${GROK16}/scripts/grok16-toolchain.sh rebuild",
        "paths": "${GROK16}/scripts/grok16-toolchain.sh paths",
    },
}
open("${GROK16}/data/grok16-toolchain.json", "w", encoding="utf-8").write(
    json.dumps(doc, indent=2) + "\\n"
)
PY
  echo "manifest: $GROK16/data/grok16-toolchain.json"
}

cmd_install() {
  if ! is_real_compiler "$BIN/g++16" || ! is_real_compiler "$BIN/g16"; then
    echo "Grok16 binaries missing at $BIN — run: $0 rebuild" >&2
    exit 1
  fi
  dv="$("$BIN/g++16" -dumpversion 2>/dev/null || true)"
  if [[ "$dv" != "$G16_VERSION" ]]; then
    echo "g++16 reports $dv; expected $G16_VERSION — rebuild" >&2
    exit 1
  fi
  write_version_file
  write_cmake_toolchain
  write_manifest
  echo "Grok16 prefix: $G16_PREFIX"
  echo "g++16: $("$BIN/g++16" --version | head -1)"
}

cmd_rebuild() {
  echo "Grok16 rebuild → prefix $G16_PREFIX (forge gcc_rebuild)"
  if [[ ! -f "$FORGE" ]]; then
    echo "Queen forge missing: $FORGE" >&2
    exit 1
  fi
  export G16_PREFIX
  export G16_PKGVERSION="Grok16-${G16_VERSION}"
  exec python3 "$FORGE" run gcc_rebuild
}

cmd_status() {
  if is_real_compiler "$BIN/g++16" && [[ "$("$BIN/g++16" -dumpversion)" == "$G16_VERSION" ]]; then
    echo "ready Grok16 g++16=$BIN/g++16"
    "$BIN/g++16" --version | head -1
    exit 0
  fi
  echo "not ready — run: $0 rebuild"
  exit 1
}

cmd_paths() {
  printf 'GROK16=%s\nG16_PREFIX=%s\nG16_CC=%s/bin/g16\nG16_CXX=%s/bin/g++16\nCMAKE_TOOLCHAIN=%s/cmake/grok16-toolchain.cmake\n' \
    "$GROK16" "$G16_PREFIX" "$G16_PREFIX" "$G16_PREFIX" "$GROK16"
}

case "${1:-}" in
  install) cmd_install ;;
  rebuild) cmd_rebuild ;;
  status) cmd_status ;;
  paths) cmd_paths ;;
  manifest) write_cmake_toolchain; write_manifest ;;
  *) usage ;;
esac