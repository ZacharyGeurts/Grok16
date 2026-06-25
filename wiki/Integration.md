# Integration

## World_Redata

```bash
cd World_Redata
./build-cpp.sh
PYTHONPATH=. python3 -m redata.cli parity
PYTHONPATH=. python3 -m redata.cli security
```

Uses `../Grok16/scripts/grok16-toolchain.sh` by default.

## Env

```bash
export G16_PREFIX=/path/to/Grok16
export WRDT_G16_PREFIX="$G16_PREFIX"
```

## Stack (L0–L5)

| Layer | Component |
|-------|-----------|
| L0–L1 | WRZC/WRDT/ZAC7 |
| L2 | C++ engine (Grok16) |
| L3 | Python redata |
| L4 | CLI, GUI |
| L5 | Grok16 |

## Queen

`./scripts/consolidate.sh` — symlink Queen vendor → Grok16.

## Manifest

`data/grok16-toolchain.json` at install. Python helper: `World_Redata/redata/grok16.py`.