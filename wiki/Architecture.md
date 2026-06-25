# Architecture

## Field rewrite

| Item | Stock GCC 15 | Grok16 |
|------|--------------|--------|
| Branch | releases/gcc-15 | same |
| BASE-VER | 15.3.1 | 16.0.0 |
| Drivers | gcc, g++ | g16, g++16 |
| Pkgversion | default | Grok16-16.0.0 |

## Build flow

```
gcc_fetch → vendor/gcc
patch BASE-VER
host configure + install → G16_PREFIX
gcc_rebuild (self-host) → SELFHOST.json
install metadata → grok16-toolchain.cmake, grok16-toolchain.json
```

## Directories

| Path | In git |
|------|--------|
| forge/, scripts/, cmake/, examples/, data/ | yes |
| vendor/gcc/, build/gcc/, bin/, lib/ | no (local) |

## Scripts

- `scripts/grok16-toolchain.sh` — main entry
- `forge/grok16-forge.py` — forge orchestrator
- `forge/compiler_tools.py` — gcc build steps