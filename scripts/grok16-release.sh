#!/usr/bin/env bash
# Grok16 release assembler — gates, source tarball, per-platform manifest, GitHub release.
# Usage: ./scripts/grok16-release.sh [version] [--push] [--no-gh]
set -euo pipefail

GROK16_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SG_ROOT="${SG_ROOT:-$(cd "$GROK16_ROOT/.." && pwd)}"
VERSION="${1:-4.7.1}"
TAG="v${VERSION}"
PUSH=0
NO_GH=0
shift || true
for arg in "$@"; do
  case "$arg" in
    --push) PUSH=1 ;;
    --no-gh) NO_GH=1 ;;
  esac
done

export GROK16_ROOT SG_ROOT
export G16_PREFIX="${G16_PREFIX:-$GROK16_ROOT}"
export NEXUS_INSTALL_ROOT="${NEXUS_INSTALL_ROOT:-$SG_ROOT/NewLatest}"
export NEXUS_STATE_DIR="${NEXUS_STATE_DIR:-$GROK16_ROOT/.nexus-release-state}"

DIST="$GROK16_ROOT/dist"
STAGE="$DIST/grok16-${VERSION}"
TARBALL="$DIST/grok16-${VERSION}-src.tar.gz"
PLAT_JSON="$DIST/grok16-${VERSION}-platforms.json"
PLAT_MD="$DIST/grok16-${VERSION}-PLATFORMS.md"

log() { printf '[%s] release %s\n' "$(date +%H:%M:%S)" "$*"; }

refresh_launch_paths() {
  log "refresh portable .launch chamber_root"
  python3 - <<'PY'
import json
from pathlib import Path

root = Path(__import__("os").environ["GROK16_ROOT"])
for lp in sorted(root.glob("examples/*/*.launch")):
    doc = json.loads(lp.read_text(encoding="utf-8"))
    name = lp.parent.name
    doc["chamber_root"] = f"${{GROK16_ROOT}}/examples/{name}"
    lp.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  {lp.name} -> ${{GROK16_ROOT}}/examples/{name}")
PY
}

run_gates() {
  log "gates: self-monitor"
  python3 "$GROK16_ROOT/tests/test_g16_self_monitor.py"
  log "gates: test-gate smoke"
  bash "$GROK16_ROOT/scripts/grok16-test-gate.sh" smoke
  log "gates: launch-verify"
  bash "$GROK16_ROOT/scripts/grok16-launch-verify.sh"
  if "$GROK16_ROOT/scripts/grok16-toolchain.sh" status >/dev/null 2>&1; then
    log "gates: test-battery-release"
    G16_RELEASE_PROFILE=1 bash "$GROK16_ROOT/scripts/grok16-toolchain.sh" test-battery-release
  else
    log "WARN skip test-battery-release (g16 not ready)"
  fi
}

write_platform_artifacts() {
  mkdir -p "$DIST"
  python3 - <<PY
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path("$GROK16_ROOT")
dist = Path("$DIST")
ver = "$VERSION"
tag = "$TAG"
src = json.loads((root / "data/grok16-platform-release.json").read_text(encoding="utf-8"))
src["distro_version"] = ver
src["distro_tag"] = tag
src["released_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
out = dist / f"grok16-{ver}-platforms.json"
out.write_text(json.dumps(src, indent=2) + "\\n", encoding="utf-8")

lines = [
    f"# Grok16 {ver} — platform bootstrap matrix",
    "",
    f"**Tag:** \`{tag}\` · **g16:** {src.get('g16_version')} · **Model:** source bootstrap per platform",
    "",
    "Grok16 releases **source + forge**. Build `g16` locally on each target (or cross from a Linux x86_64 host).",
    "",
    "## Quick start (any Linux x86_64)",
    "",
    "\`\`\`bash",
    "tar xzf grok16-{ver}-src.tar.gz && cd grok16-{ver}-src",
    "export G16_PREFIX=\\$(pwd) G16_PKGVERSION=Grok16-16.2.0",
    "./scripts/grok16-toolchain.sh bootstrap",
    "./scripts/grok16-toolchain.sh rebuild",
    "./scripts/grok16-launch-verify.sh",
    "\`\`\`",
    "",
    "## .launch chambers",
    "",
    "Every example ships a portable \`.launch\` (schema \`queen-launch/v1\`). Run without compile:",
    "",
    "\`\`\`bash",
    "export GROK16_ROOT=\\$(pwd) SG_ROOT=/path/to/SG",
    "python3 NewLatest/Queen/lib/queen-launch-chamber.py run examples/speed-demo/speed-demo.launch",
    "\`\`\`",
    "",
    "## Platforms",
    "",
    "| ID | OS | Arch | Bootstrap |",
    "|----|-----|------|-----------|",
]
for p in src.get("platforms") or []:
    boot = p.get("bootstrap") or {}
    hint = boot.get("cross_prefix") or boot.get("CC") or boot.get("host") or boot.get("ndk") or "local"
    if isinstance(hint, bool):
        hint = "ndk" if hint else "local"
    lines.append(f"| {p.get('id')} | {p.get('os')} | {p.get('arch')} | {hint} |")

lines.extend([
    "",
    "## RISC-V (linux-gnu-riscv64)",
    "",
    "Install cross toolchain, then bootstrap with:",
    "",
    "\`\`\`bash",
    "sudo apt install gcc-riscv64-linux-gnu g++-riscv64-linux-gnu",
    "export CC=riscv64-linux-gnu-gcc CXX=riscv64-linux-gnu-g++",
    "export G16_CROSS_PREFIX=riscv64-linux-gnu-",
    "./scripts/grok16-toolchain.sh bootstrap",
    "\`\`\`",
    "",
    "Linker emulation: \`elf64lriscv\` · doctrine target \`linux-gnu-riscv64\` + \`bare-elf-riscv64\`.",
    "",
])
(dist / f"grok16-{ver}-PLATFORMS.md").write_text("\\n".join(lines) + "\\n", encoding="utf-8")
print(out)
PY
}

build_tarball() {
  log "stage source tarball"
  rm -rf "$STAGE" "$TARBALL"
  mkdir -p "$STAGE"
  tar -C "$GROK16_ROOT" \
    --exclude='./vendor' --exclude='./build' --exclude='./bin' \
    --exclude='./lib' --exclude='./libexec' --exclude='./include' \
    --exclude='./share' --exclude='./dist' --exclude='./.git' \
    --exclude='./.nexus-state' --exclude='./.nexus-release-state' \
    --exclude='./.grok16-state' --exclude='./data/bench' \
    --exclude='./cmake/grok16-toolchain.cmake' \
    -cf - . | tar -C "$STAGE" -xf -
  mv "$STAGE" "$STAGE-src"
  STAGE="$STAGE-src"
  cp "$PLAT_JSON" "$STAGE/data/grok16-platform-release.json"
  tar -czf "$TARBALL" -C "$DIST" "grok16-${VERSION}-src"
  log "wrote $TARBALL ($(du -h "$TARBALL" | awk '{print $1}'))"
}

git_release() {
  cd "$GROK16_ROOT"
  if ! git diff --quiet HEAD 2>/dev/null; then
    log "commit release tree"
    git add -A
    git commit -m "Grok16 ${VERSION} — bench-refresh, comparison charts, gcc-14 host pin"
  fi
  if git rev-parse "$TAG" >/dev/null 2>&1; then
    log "tag $TAG exists"
  else
    git tag -a "$TAG" -m "Grok16 ${VERSION}"
    log "tagged $TAG"
  fi
  if [[ "$PUSH" -eq 1 ]]; then
    git push origin main
    git push origin "$TAG"
    log "pushed main + $TAG"
  fi
}

gh_release() {
  [[ "$NO_GH" -eq 1 ]] && return 0
  command -v gh >/dev/null 2>&1 || { log "WARN gh missing — skip GitHub release"; return 0; }
  local notes="$GROK16_ROOT/RELEASE-${VERSION}.md"
  [[ -f "$notes" ]] || notes="$PLAT_MD"
  if gh release view "$TAG" >/dev/null 2>&1; then
    log "GitHub release $TAG exists — upload assets"
    gh release upload "$TAG" "$TARBALL" "$PLAT_JSON" "$PLAT_MD" --clobber
  else
    gh release create "$TAG" \
      --title "Grok16 ${VERSION}" \
      --notes-file "$notes" \
      "$TARBALL" "$PLAT_JSON" "$PLAT_MD"
    log "created GitHub release $TAG"
  fi
}

main() {
  log "Grok16 release ${VERSION} (${TAG})"
  refresh_launch_paths
  run_gates
  write_platform_artifacts
  build_tarball
  git_release
  gh_release
  log "release ${VERSION} complete"
  log "  tarball: $TARBALL"
  log "  platforms: $PLAT_JSON"
  log "  guide: $PLAT_MD"
}

main