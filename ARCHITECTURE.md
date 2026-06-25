# Grok16 Architecture

Grok16 is a **self-hosted G16 field compiler distribution**: real ELF `g16` / `g++16` drivers at version **16.0.0**, built from upstream **GCC `releases/gcc-15`** with a documented field rewrite. This repository ships **scripts, forge, patches, and CMake metadata** — not prebuilt binaries (GPL source is fetched and built locally).

## Field rewrite vs stock GCC

| Aspect | Stock GCC 15 | Grok16 G16 field build |
|--------|----------------|-------------------------|
| Upstream branch | `releases/gcc-15` | Same clone |
| `gcc/BASE-VER` | `15.3.1` | **`16.0.0`** (patched) |
| Driver names | `gcc`, `g++` | **`g16`, `g++16`** (`program-transform-name`) |
| Pkgversion | (default) | **`Grok16-16.0.0`** |
| Identity | Upstream GCC 15 | **Field G16 @ 16.0.0** — not `releases/gcc-16` |

The rewrite is intentional sovereignty branding: one coherent toolchain version string across Queen, World_Redata L2 C++, and CMake consumers, while staying on the maintained gcc-15 tree.

## Build flow

```mermaid
flowchart LR
  subgraph fetch [Fetch]
    A[grok16-forge gcc_fetch] --> B[vendor/gcc clone]
    B --> C[BASE-VER 16.0.0 patch]
  end
  subgraph host [Host build]
    C --> D[gcc_prereqs]
    D --> E[gcc_configure host gcc]
    E --> F[make install → G16_PREFIX]
  end
  subgraph selfhost [Self-host]
    F --> G[gcc_rebuild]
    G --> H[g16/g++16 compile GCC]
    H --> I[SELFHOST.json stamp]
  end
  subgraph meta [Metadata]
    I --> J[grok16-toolchain.cmake]
    I --> K[data/grok16-toolchain.json]
  end
```

**Bootstrap** (`grok16-toolchain.sh bootstrap`) runs the full host pipeline via `forge/grok16-forge.py run gcc`.

**Rebuild** (`grok16-toolchain.sh rebuild`) distcleans, reconfigures with `g16`/`g++16` as CC/CXX, runs `make bootstrap` (or `make all` when `G16_DISABLE_BOOTSTRAP=1`), installs, and writes `SELFHOST.json`.

## Directory roles

| Path | Role |
|------|------|
| `forge/` | Python forge — `compiler_tools.py`, `grok16-forge.py` |
| `vendor/gcc/` | Upstream clone (local, ~1.6G, gitignored) |
| `build/gcc/` | Configure/make tree (local, ~4G, gitignored) |
| `bin/` `lib/` `libexec/` | Install prefix (`G16_PREFIX`, gitignored) |
| `cmake/grok16-toolchain.cmake` | Generated CMake toolchain file |
| `data/grok16-toolchain.json` | Machine-readable status manifest |
| `patches/` | Documented field deltas |
| `examples/` | Minimal CMake consumer |

## Configuration

All paths are **environment-driven** (no hardcoded Desktop layout). See `data/grok16-config.json`.

| Variable | Default when unset |
|----------|-------------------|
| `GROK16_ROOT` | Repo root (auto from `scripts/`) |
| `G16_PREFIX` | `$GROK16_ROOT` |
| `GROK16_SG_ROOT` | Parent of `GROK16_ROOT` |
| `GROK16_QUEEN_ROOT` | `$GROK16_SG_ROOT/NewLatest/Queen` |
| `GROK16_GCC_SRC` | `$GROK16_ROOT/vendor/gcc` |
| `GROK16_GCC_BUILD` | `$GROK16_ROOT/build/gcc` |
| `GROK16_GCC_REPO` | `https://gcc.gnu.org/git/gcc.git` |
| `GROK16_GCC_BRANCH` | `releases/gcc-15` |
| `G16_PKGVERSION` | `Grok16-16.0.0` |
| `G16_DISABLE_BOOTSTRAP` | unset → bootstrap on rebuild |
| `GROK16_BUILD_JOBS` | `nproc` |

`scripts/grok16-config.sh` resolves these for shell entry points; `ForgeContext.from_env()` reads `GROK16_ROOT` and job count for Python.

## Self-host and verification

After rebuild, `G16_PREFIX/SELFHOST.json` records:

- `selfhosted: true`
- `bootstrap` flag (whether 3-stage bootstrap ran)
- Paths to `g16` / `g++16` and pkgversion

`./scripts/grok16-toolchain.sh verify` checks driver version, compiles the C++20 example (`-c`), and optionally builds `examples/minimal-cmake-project` when CMake is available.

## Queen and consolidate

Queen historically hosted the gcc clone and forge probes. **Grok16 is the canonical home** for the G16 tree on the SG desktop. `scripts/consolidate.sh` moves Queen `vendor/gcc` and `build/gcc` into Grok16 (paths configurable via `GROK16_QUEEN_ROOT`) and symlinks Queen `vendor/gcc` → Grok16 source.

Queen `compiler_probe` / `g16-toolchain.json` can point at Grok16's prefix after install.

## Integration with the SG stack

Grok16 is the **L5 toolchain layer** in the World_Redata methodology (assembly view L0–L5):

- **World_Redata L2** — C++ engine built with `g++16` via `build-cpp.sh` and `field_g16.hh` contracts.
- **World_Redata gates** — `security`, `asm`, and `parity` assume a real G16 @ 16.0.0 (no bash wrappers).
- **Queen forge** — `compiler_probe` writes `g16-toolchain.json`; Grok16 forge is the standalone equivalent.
- **Hostess7 / ZAC / redata** — lossless segments and plates are format layers (L0–L1); Grok16 compiles the native L2 engine that roundtrips those bytes.
- **Field_Primer** — treat Grok16 as the sovereign C/C++ build requirement: bootstrap once, verify, then point CMake at `grok16-toolchain.cmake`.

Set `G16_PREFIX` (or symlink Queen prefix) so downstream manifests resolve the same ELF drivers.

## Licensing

- **GCC** — GPLv3 (FSF). Runtime libraries may use GCC Runtime Library Exception.
- **Grok16 scripts/forge** — GPLv3, Copyright (C) 2026 Zachary Geurts.

See [LICENSE](LICENSE) and [CREDITS.md](CREDITS.md).

## Releases (planned)

When stable: tag `v16.0.0-beta.1`, document optional binary tarball **outside git** (install prefix archive), keep source-of-truth in forge bootstrap.