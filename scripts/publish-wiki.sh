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
    exec bash "${_AML_ROOT}/lib/ammolang-run.sh" exec "script:Grok16/scripts/publish-wiki.sh" "$@"
  fi
fi
unset -f _aml_find_root 2>/dev/null || true

#!/usr/bin/env bash
# Publish wiki/*.md to GitHub wiki repo (full replace).
set -euo pipefail

GROK16_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_SRC="${GROK16_ROOT}/wiki"
WIKI_REPO="${WIKI_REPO:-${GROK16_ROOT}/.wiki-publish}"
WIKI_REMOTE="${WIKI_REMOTE:-https://github.com/ZacharyGeurts/Grok16.wiki.git}"
VER="${1:-$(python3 -c "import json; print(json.load(open('${GROK16_ROOT}/data/grok16-version.json'))['distro_version'])" 2>/dev/null || echo unknown)}"

[[ -d "$WIKI_SRC" ]] || { echo "Missing ${WIKI_SRC}" >&2; exit 1; }

if [[ ! -d "${WIKI_REPO}/.git" ]]; then
  rm -rf "$WIKI_REPO"
  git clone "$WIKI_REMOTE" "$WIKI_REPO"
fi

rsync -a --delete --exclude='.git' "${WIKI_SRC}/" "${WIKI_REPO}/"

cd "$WIKI_REPO"
git add -A
git diff --cached --quiet && { echo "Wiki already up to date."; exit 0; }
git -c user.email="gzac5314@users.noreply.github.com" -c user.name="ZacharyGeurts" \
  commit -m "wiki: Grok16 ${VER}"
git push origin master 2>/dev/null || git push origin main 2>/dev/null || git push
echo "Wiki published: https://github.com/ZacharyGeurts/Grok16/wiki"