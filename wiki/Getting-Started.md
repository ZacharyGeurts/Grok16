# Getting Started

## Requirements

- Linux x86_64
- Host gcc/g++, git, cmake, python3
- GCC build dependencies
- ~6 GB disk

## Bootstrap

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16
git checkout v16.0.0
export G16_PREFIX="$(pwd)"

./scripts/grok16-toolchain.sh bootstrap
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh verify
./scripts/grok16-toolchain.sh field-bench
```

## Rebuild

| Mode | Command |
|------|---------|
| Default (fast) | `./scripts/grok16-toolchain.sh rebuild` |
| Full bootstrap | `G16_FULL_REBUILD=1 ./scripts/grok16-toolchain.sh rebuild` |
| Release | `G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild` |

## Queen consolidate

```bash
export GROK16_QUEEN_ROOT=/path/to/Queen   # optional
./scripts/consolidate.sh
./scripts/grok16-toolchain.sh rebuild
```

## Docker

```bash
docker build -t grok16 .
```