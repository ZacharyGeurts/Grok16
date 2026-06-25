# Grok16

![Status](https://img.shields.io/badge/status-beta-orange)
![Version](https://img.shields.io/badge/G16-16.0.0-blue)
![License](https://img.shields.io/badge/license-GPLv3-green)
![Base](https://img.shields.io/badge/upstream-gcc--15-lightgrey)

**Grok16** is the **whole G16 field rewrite** — one folder on your Desktop under `SG/Grok16`:

- **`vendor/gcc`** — cloned `releases/gcc-15`, field `BASE-VER` **16.0.0**
- **`build/gcc`** — configured GCC build tree
- **`bin/g16` `bin/g++16`** — installed ELF compilers (pkgversion `Grok16-16.0.0`)
- **`forge/`** — build orchestrator (no Queen dependency)
- **`patches/`** — documented field deltas

> **Beta** — layout and forge APIs may change before 1.0. This is **not** upstream `releases/gcc-16`; it is a **gcc-15 field rewrite** branded G16 @ 16.0.0.

## Field rewrite (what G16 means here)

| Layer | Value |
|-------|--------|
| Upstream clone | `releases/gcc-15` |
| Field `gcc/BASE-VER` | `16.0.0` (was `15.3.1`) |
| Binary names | `g16`, `g++16` via `program-transform-name` |
| Pkgversion | `Grok16-16.0.0` |
| Install prefix | `Grok16/` (`G16_PREFIX`) |

See `data/gcc-source.json` and `patches/gcc-base-ver-16.0.0.patch`.

## Whole folder layout

```
SG/Grok16/
  vendor/gcc/           # gcc-15 clone + field BASE-VER (local, ~1.6G)
  build/gcc/            # make tree (local, ~4G)
  bin/ lib/ libexec/ …  # installed compiler prefix
  forge/                # grok16-forge.py + compiler_tools
  scripts/              # grok16-toolchain.sh, consolidate.sh
  patches/              # field rewrite patches
  data/gcc-source.json  # source manifest (in git)
```

**GitHub** ships `forge/`, `scripts/`, `patches/`, docs — not `vendor/` or `bin/` (too large; GPL source fetched/built locally).

## Quick start (fresh clone from GitHub)

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16
export G16_PREFIX="$(pwd)"
export G16_PKGVERSION=Grok16-16.0.0

./scripts/grok16-toolchain.sh bootstrap   # gcc_fetch gcc-15 + host build + install
./scripts/grok16-toolchain.sh status
```

## SG desktop (already have Queen gcc-15 clone)

If gcc lived under `NewLatest/Queen/vendor/gcc`, consolidate into Grok16:

```bash
chmod +x scripts/consolidate.sh
./scripts/consolidate.sh
```

Then rebuild/self-host:

```bash
export G16_DISABLE_BOOTSTRAP=1   # optional faster pass
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh status
```

## Commands

```bash
./scripts/grok16-toolchain.sh bootstrap   # first-time: fetch gcc-15 + build
./scripts/grok16-toolchain.sh rebuild     # self-host with g16/g++16
./scripts/grok16-toolchain.sh status
./scripts/grok16-toolchain.sh paths
python3 forge/grok16-forge.py run gcc_fetch
```

## License

**GNU General Public License v3** — see [LICENSE](LICENSE). GCC: Copyright (C) Free Software Foundation, Inc. Grok16 scripts: Copyright (C) 2026 Zachary Geurts.

## Credits

[CREDITS.md](CREDITS.md) — FSF, GCC contributors, Grok16 maintainers.