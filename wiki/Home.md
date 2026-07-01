# Grok16 5.3.1 — Programmerland

**Grok16 is its own GitHub.** Distro **5.3.1** · tag `v5.3.1` · `g16` @ `16.2.0`.

| | |
|---|---|
| **Web home (programmers)** | [AmmoCode on GitHub Pages](https://zacharygeurts.github.io/AmmoCode/) |
| **This repo** | [github.com/ZacharyGeurts/Grok16](https://github.com/ZacharyGeurts/Grok16) |
| **Languages** | **79** in `data/grok16-languages.json` |
| **AmmoCode pair** | [AmmoCode 6.1](https://github.com/ZacharyGeurts/AmmoCode) |
| **Theme** | [Programmerland](Programmerland) — kind to programmers and AI |

## Read this first

> **DO NOT CREATE FIELD FILES.** Use the **[2D field platform](Field-Platform)** — placement on the plane *is* field at depth 0.

## What 5.3.1 changes

- **Own GitHub releases** — `grok16-5.3.1-src.tar.gz` + platform matrix (no Hostess7 H7e embed)
- **Hostess7 pairs here** — `doctrine/grok16-github-pair.json` in stack packs
- **Programmerland docs** — AmmoCode GitHub Pages is the friendly manual front door
- **All 79 languages** — registry unchanged; full tree via clone or boot prompt

## Quick start

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16 && git checkout v5.3.1
export G16_PREFIX="$(pwd)" G16_BELT_PROFILE=belt_2_0 SG_ROOT=/path/to/SG
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-integrate.sh
```

## Links

- [Programmerland](Programmerland) · [Release 5.3.1](Release) · [Field Platform](Field-Platform)
- [AmmoCode manual](https://zacharygeurts.github.io/AmmoCode/) · [MCP for agents](MCP)