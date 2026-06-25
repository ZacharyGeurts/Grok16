# Grok16

![Status](https://img.shields.io/badge/status-beta-orange)
![Version](https://img.shields.io/badge/G16-16.0.0-blue)
![License](https://img.shields.io/badge/license-GPLv3-green)
![Base](https://img.shields.io/badge/upstream-gcc--15-lightgrey)

**Grok16** is a **self-hosted G16 field compiler** — real ELF `g16` / `g++16` @ **16.0.0**, C++20-capable, built via the Grok16 forge. Scripts and CMake integration ship in git; **no prebuilt binaries** (reproducible bootstrap from GPL GCC sources).

> **Beta** — APIs and layout may change before 1.0. This is a **gcc-15 field rewrite** (BASE-VER 16.0.0), not upstream `releases/gcc-16`.

## What you get

| Artifact | Role |
|----------|------|
| `g16` / `g++16` | C and C++ drivers (pkgversion `Grok16-16.0.0`) |
| `grok16-toolchain.cmake` | CMake toolchain file |
| `grok16-toolchain.sh` | bootstrap · rebuild · verify · status · paths |
| `forge/grok16-forge.py` | Fetch → configure → build → self-host |
| `examples/minimal-cmake-project` | Copy-paste CMake consumer |

Local trees (`vendor/`, `build/`, `bin/`) are produced on your machine (~6G). See [ARCHITECTURE.md](ARCHITECTURE.md).

## Architecture (short)

```mermaid
flowchart TB
  subgraph repo [GitHub repo]
    F[forge/]
    S[scripts/]
    P[patches/]
    E[examples/]
  end
  subgraph local [Local build]
    V[vendor/gcc gcc-15]
    B[build/gcc]
    I[bin/g16 g++16]
  end
  F --> V
  V --> B
  B --> I
  I --> E
```

1. **Fetch** `releases/gcc-15`, patch `BASE-VER` → 16.0.0  
2. **Host build** with system gcc, install to `G16_PREFIX`  
3. **Self-host** with `g16`/`g++16`, stamp `SELFHOST.json`  
4. **Consume** via CMake toolchain or Queen/World_Redata probes  

Full detail: [ARCHITECTURE.md](ARCHITECTURE.md).

## First build (new clone)

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16
export G16_PREFIX="$(pwd)"          # install prefix = repo root
export G16_PKGVERSION=Grok16-16.0.0

./scripts/grok16-toolchain.sh bootstrap   # fetch + host build + install
./scripts/grok16-toolchain.sh rebuild     # self-host (optional G16_DISABLE_BOOTSTRAP=1)
./scripts/grok16-toolchain.sh verify      # C++20 compile + optional CMake smoke
./scripts/grok16-toolchain.sh status
```

**Requirements:** Linux x86_64, `git`, host `gcc`/`g++`, build deps for GCC (see upstream docs). Bootstrap takes significant time and disk.

## Configuration

No hardcoded Desktop paths. Override via environment:

```bash
./scripts/grok16-toolchain.sh paths    # resolved layout
./scripts/grok16-toolchain.sh config   # paths + config template
```

| Variable | Purpose |
|----------|---------|
| `GROK16_ROOT` | Repo root |
| `G16_PREFIX` | Install prefix (`bin/g16`, `lib/`, …) |
| `GROK16_QUEEN_ROOT` | Queen tree for `consolidate` (default `$SG/NewLatest/Queen`) |
| `GROK16_GCC_SRC` / `GROK16_GCC_BUILD` | Source and build trees |
| `G16_DISABLE_BOOTSTRAP` | `1` → faster rebuild (`make all` not 3-stage) |

Template: `data/grok16-config.json`.

## SG desktop (Queen → Grok16)

If gcc already lived under Queen:

```bash
export GROK16_QUEEN_ROOT=/path/to/NewLatest/Queen   # optional
./scripts/consolidate.sh
./scripts/grok16-toolchain.sh rebuild
```

## CMake example

```bash
cmake -S examples/minimal-cmake-project -B examples/minimal-cmake-project/build \
  -DCMAKE_TOOLCHAIN_FILE=cmake/grok16-toolchain.cmake
cmake --build examples/minimal-cmake-project/build
./examples/minimal-cmake-project/build/grok16_smoke
```

## Commands

```bash
./scripts/grok16-toolchain.sh bootstrap   # first-time fetch + build
./scripts/grok16-toolchain.sh rebuild     # self-host
./scripts/grok16-toolchain.sh verify      # compile smoke test
./scripts/grok16-toolchain.sh status
./scripts/grok16-toolchain.sh paths
python3 forge/grok16-forge.py status      # JSON toolchain state
```

## Integration (Field_Primer / SG stack)

Grok16 is the **sovereign C/C++ toolchain** for the SG ecosystem:

- **[World_Redata](https://github.com/ZacharyGeurts)** — L2 C++ engine (`build-cpp.sh`, `field_g16.hh`); methodology layer **L5 Toolchain** expects real `g++16` @ 16.0.0.
- **Queen** — `compiler_probe` / `g16-toolchain.json`; consolidate keeps Queen symlinked to Grok16 source.
- **redata pipeline** — L0–L1 bytes/plates; L2 native code must roundtrip formats compiled with G16.
- **Hostess7 / ZAC** — orthogonal storage/teach layers; Grok16 builds the engine that reads/writes WRDT/WRZC contracts.

**Field_Primer build requirement:** bootstrap Grok16 once, run `verify`, export `G16_PREFIX`, point downstream CMake at `grok16-toolchain.cmake`. Downstream gates (`security`, `asm`, `parity` in World_Redata) fail closed on fake wrappers.

## Repo layout (git vs local)

```
Grok16/
  forge/ scripts/ patches/ examples/ data/   # in git
  ARCHITECTURE.md README.md LICENSE
  vendor/gcc/ build/gcc/ bin/ lib/           # local only (gitignored)
```

## CI

GitHub Actions runs script lint, Python compile, `paths`, and forge `status` on Linux x86_64. Full bootstrap is local/optional (too heavy for default CI).

## License

**GPLv3** — [LICENSE](LICENSE). GCC: Copyright (C) Free Software Foundation, Inc. Grok16 scripts: Copyright (C) 2026 Zachary Geurts.

## Credits

[CREDITS.md](CREDITS.md) — FSF, GCC contributors, Grok16 maintainers.