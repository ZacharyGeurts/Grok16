# Grok16

![Status](https://img.shields.io/badge/status-beta-orange)
![Version](https://img.shields.io/badge/G16-16.0.0-blue)
![License](https://img.shields.io/badge/license-GPLv3-green)
![Compiler](https://img.shields.io/badge/binaries-g16%20%2F%20g++16-lightgrey)

**Grok16** is a self-hosted **G16 field compiler** distribution — real ELF `g16` / `g++16` binaries at **16.0.0**, not shell wrappers.

> **Beta** — toolchain layout, forge integration, and install paths may change before a stable 1.0 release. Build from source via Queen forge; prebuilt binaries are not published in this repository.

## What you get

| Tool | Role |
|------|------|
| `g16` | C compiler (GCC 16 field build) |
| `g++16` | C++ compiler (`gnu++26`) |
| `grok16-toolchain.cmake` | CMake toolchain file |
| `grok16-toolchain.sh` | install · rebuild · status · paths |

Pkgversion string: `Grok16-16.0.0`.

## Quick start

Clone beside an **SG** workspace that includes `NewLatest/Queen` (forge + GCC source), then rebuild into a local prefix:

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16

export G16_PREFIX="$(pwd)"
export G16_PKGVERSION=Grok16-16.0.0
# Optional faster single-pass self-host:
export G16_DISABLE_BOOTSTRAP=1

./scripts/grok16-toolchain.sh rebuild   # requires Queen forge
./scripts/grok16-toolchain.sh install
./scripts/grok16-toolchain.sh status
```

Export paths:

```bash
eval "$(./scripts/grok16-toolchain.sh paths)"
g++16 --version
```

CMake:

```bash
cmake -DCMAKE_TOOLCHAIN_FILE="$(pwd)/cmake/grok16-toolchain.cmake" ...
```

## Layout (after build)

```
Grok16/
  bin/g16  bin/g++16      # installed by forge (gitignored)
  lib/ libexec/ share/    # installed by forge (gitignored)
  scripts/grok16-toolchain.sh
  cmake/grok16-toolchain.cmake
  data/grok16-toolchain.json
  VERSION  SELFHOST.json
```

This repo ships **scripts and metadata only**. Compiler binaries are produced locally by the Queen forge (`gcc_rebuild`).

## Requirements

- Linux x86_64
- `NewLatest/Queen` forge at `../NewLatest/Queen` relative to SG (or set paths in the script)
- GCC 16 source fetched by Queen (`releases/gcc-16`)
- Existing `g16`/`g++16` or legacy prefix for self-host bootstrap

## Beta limitations

- No full 3-stage bootstrap by default (`G16_DISABLE_BOOTSTRAP=1` for dev rebuilds)
- Install prefix assumed to be the repo root (`G16_PREFIX`)
- Queen forge path is hardcoded relative to SG desktop layout
- No binary releases on GitHub yet

## License

Compiler binaries built from GCC are under **GPLv3** (GCC runtime libraries follow GCC's exception policy). Grok16 scripts and metadata in this repository are **Copyright (c) 2026 Zachary Geurts** — proprietary; all rights reserved unless otherwise stated.