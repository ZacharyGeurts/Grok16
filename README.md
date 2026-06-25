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

## Source in this repo

| Path | What |
|------|------|
| `lib/grok16-forge.py` | Build orchestrator (fetch → configure → install) |
| `lib/forge/` | Forge engine + `compiler_tools.py` (Grok16 field configure) |
| `patches/` | Documented GCC deltas (`gcc/BASE-VER` → 16.0.0) |
| `scripts/grok16-toolchain.sh` | Human/CI entry: bootstrap · rebuild · status |

**Not in git:** `vendor/gcc` (~1.6 GB upstream clone) and installed `bin/`/`lib/` — produced locally.

## Quick start

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16

export G16_PREFIX="$(pwd)"
export G16_PKGVERSION=Grok16-16.0.0

# First time: clone GCC + host build + install into repo root
./scripts/grok16-toolchain.sh bootstrap

# Later: self-host rebuild with existing g16/g++16 (or host gcc)
export G16_DISABLE_BOOTSTRAP=1   # optional faster single-pass
./scripts/grok16-toolchain.sh rebuild
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

Compiler binaries are produced locally by **grok16-forge** (`lib/grok16-forge.py`).

## Requirements

- Linux x86_64
- `git`, `make`, `python3`, host `gcc`/`g++` (for first bootstrap)
- Network for `gcc_fetch` (clone https://gcc.gnu.org/git/gcc.git)
- ~2 GB disk for `vendor/gcc` + build tree

## Beta limitations

- No full 3-stage bootstrap by default (`G16_DISABLE_BOOTSTRAP=1` for dev rebuilds)
- Install prefix assumed to be the repo root (`G16_PREFIX`)
- Upstream GCC must be fetched locally (`vendor/gcc` not committed)
- No prebuilt binary releases on GitHub yet

## License

**GNU General Public License v3** — see [LICENSE](LICENSE).

Grok16 scripts and metadata: Copyright (C) 2026 Zachary Geurts, licensed under GPLv3.

Compiler binaries produced from [GCC](https://gcc.gnu.org/) are **Copyright (C) Free
Software Foundation, Inc.** and GCC contributors, also under GPLv3 (runtime
libraries may use the GCC Runtime Library Exception where applicable).

## Credits

Full attribution: [CREDITS.md](CREDITS.md).

- [GNU Compiler Collection](https://gcc.gnu.org/) — Free Software Foundation, Inc. and contributors
- [Free Software Foundation](https://www.fsf.org/) — GCC, GPL, and free software infrastructure
- Zachary Geurts — Grok16 beta packaging and toolchain scripts