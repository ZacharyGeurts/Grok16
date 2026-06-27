# Performance

Web: [performance.html](https://zacharygeurts.github.io/Grok16/performance.html) · [speed-bench.html](https://zacharygeurts.github.io/Grok16/speed-bench.html)

## Speed bench (3.0 — report v3.2.0)

**Suite:** `speed_demo` @ `1.1.0` · **3s execution window** · Schema: `grok16-field-exec-full-bench/v4`

```bash
SPEED_DEMO_TARGET_SEC=3 ./scripts/grok16-toolchain.sh exec-full-bench
./scripts/grok16-toolchain.sh exec-compare
```

| Runner | Compile (ms) | ops/s |
|--------|-------------:|------:|
| C++ g16 belt_2_0 (post-meld) | BSP hit | **93.3M** |
| CMake host g++ -O2 | BSP hit | **91.8M** |
| C++ host g++ -O2 | BSP hit | 91.7M |
| C++ g16 belt_2_0 | BSP hit | **89.3M** |
| C g16 belt_2_0 | BSP hit | 89.2M |
| Python gpy-16 GrokVM | — | **849K** |
| Python host CPython 3 | — | 793K |

Artifacts: `docs/SPEED-BENCH-REPORT.md` · `docs/field-exec-full-bench.json` · Wiki: [Speed-Bench](Speed-Bench)

## Belt triad (2.0)

```bash
./scripts/grok16-toolchain.sh bench-triad
```

Workload: `field-nexus-bench` (240 frames, FieldX86 + entropy + wave + NEXUS).

| Toolchain | Profile | compile_ms | run wall_ms | binary bytes |
|-----------|---------|------------|-------------|--------------|
| host `g++` | `-O3 -march=native` | ~2575 | ~3 | ~27264 |
| `g16` | **belt_1_0** | ~2377 | ~3 | ~22712 |
| `g16` | **belt_2_0** | ~3708 | ~5 | ~22840 |

Artifact: `data/bench/triad-latest.json`

## Primary metric

```bash
export G16_BELT_PROFILE=belt_2_0
./scripts/grok16-toolchain.sh field-bench
```

## Release rebuild

```bash
export G16_RELEASE_PROFILE=1
export G16_ENABLE_LTO=1
export G16_BELT_PROFILE=belt_2_0
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh profile
G16_ENABLE_PGO=1 ./scripts/grok16-toolchain.sh field-bench
```

## Bench matrix

```bash
./scripts/grok16-toolchain.sh bench-all
```

## Gates

- `test-battery-heavy` — release profile bench
- `test-battery-belt` — 2.0 belt validation
- `exec-full-bench` — 3.0 compile + execution speed gate