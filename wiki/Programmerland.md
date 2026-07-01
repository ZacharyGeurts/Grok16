# Programmerland

**A place where programmers and AI agents are treated well.**

Programmerland is the design theme for Grok16, AmmoCode, and the AmmoOS stack: clear docs, honest tooling, no dark patterns, and interfaces that respect both human focus and agent context windows.

## Principles

| For programmers | For AI agents |
|-----------------|---------------|
| Plain language in docs and errors | Copy-paste primers in every AmmoCode tab |
| One obvious path to compile and run | MCP tools with stable JSON schemas |
| Non-destructive defaults (export, don't overwrite) | Truthful stack context — no fake file APIs |
| 79 languages in one registry — no surprise drop-offs | `grok16-languages.json` is the single source of truth |
| Loopback-only surfaces — your machine, your data | Ironclad citations when docs reference code |

## Where you land

| Surface | URL | Role |
|---------|-----|------|
| **AmmoCode manual** | [zacharygeurts.github.io/AmmoCode](https://zacharygeurts.github.io/AmmoCode/) | Primary **GitHub Pages** home for programmers |
| **Grok16 repo** | [github.com/ZacharyGeurts/Grok16](https://github.com/ZacharyGeurts/Grok16) | Compiler distro — own GitHub, `v5.3.1` |
| **Grok16 wiki** | [Grok16 wiki](Home) | Deep reference (you are here) |
| **Local editor** | `http://127.0.0.1:9555/` | AmmoCode stack editor |

## Languages (all still here)

Grok16 registers **79 languages** in `data/grok16-languages.json`. AmmoCode discerns them via `g16 --g16-discern`. Combinatronic seed packs map editor UX. Nothing was removed when packaging moved to plain archives — only *how* releases ship changed.

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16 && git checkout v5.3.1
./scripts/grok16-languages.sh list | head
```

## Stack pair (5.3.1)

- **Grok16** — separate GitHub; full source tarball per release
- **Hostess7** — plain `.tar.gz` / `.zip`; common runtime + optional full clone
- **AmmoCode 6.1** — [AmmoCode](https://github.com/ZacharyGeurts/AmmoCode); pairs `g16-ammocode-field-doctrine.json`

## Kind defaults

- **Boot:** common runtime first; 10s Y/N for full Grok16 clone — never silent multi-GB downloads
- **AmmoCode:** read-only disk API; save = export; run jails for system paths
- **Agents:** [MCP](MCP) — version, toolchain, rtx_gate, speed_bench without mystery side effects

Welcome to Programmerland. Build something good.