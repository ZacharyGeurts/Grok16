# Performance

Web: [performance.html](https://zacharygeurts.github.io/Grok16/performance.html) · [speed-bench.html](https://zacharygeurts.github.io/Grok16/speed-bench.html)

## Speed bench (4.7 — report v4.7.0)

**Suite:** `speed_demo` @ `1.1.0` · **3s execution window** · Schema: `grok16-field-exec-full-bench/v5`

```bash
./scripts/grok16-toolchain.sh bench-refresh
# or stepwise:
SPEED_DEMO_TARGET_SEC=3 ./scripts/grok16-toolchain.sh exec-full-bench
./scripts/grok16-toolchain.sh exec-compare
./scripts/grok16-toolchain.sh bench-charts
```

| Runner | Compile (ms) | ops/s |
|--------|-------------:|------:|
| C++ host g++ -O2 | 1,588 | **95.3M** |
| CMake host g++ -O2 | 2,174 | 93.0M |
| C++ g16 belt_2_0 | 1,883 | **92.6M** |
| C g16 belt_1_0 | **357** | 90.1M |
| Python host CPython 3 | — | **800K** |
| Python gpy-16 GrokVM | — | 751K |

Charts: `docs/assets/speed-bench-chart.svg`, `triad-chart.svg`, `compare-chart.svg`, `bench-all-chart.svg`

Artifacts: `docs/SPEED-BENCH-REPORT.md` · `docs/field-exec-full-bench.json` · Wiki: [Speed-Bench](Speed-Bench)

## Belt triad (2.0)

```bash
./scripts/grok16-toolchain.sh bench-triad
./scripts/grok16-toolchain.sh bench-charts
```

Workload: `field-nexus-bench` (240 frames, FieldX86 + entropy + wave + NEXUS). Host witness: **gcc-14**.

| Toolchain | Profile | compile_ms | run wall_ms | binary bytes |
|-----------|---------|------------|-------------|--------------|
| host `g++` | `-O3 -march=native` | live | live | live |
| `g16` | **belt_1_0** | live | live | live |
| `g16` | **belt_2_0** | live | live | live |

Artifact: `data/bench/triad-latest.json` · Chart: `docs/assets/triad-chart.svg`

## bench-all profiles

```bash
./scripts/grok16-toolchain.sh bench-all
```

| Profile | compile_ms | kernel wall_ms |
|---------|------------|----------------|
| belt_1_0 | 1,369 | 2.49 |
| belt_2_0 | 1,376 | 4.15 |
| field_opt | 1,296 | 2.77 |
| heavy | 1,667 | 2.79 |
| expert | 2,275 | 3.30 |

Artifact: `data/bench/latest.json` · Chart: `docs/assets/bench-all-chart.svg`

## Field vs host compare

```bash
./scripts/grok16-toolchain.sh bench-compare
```

Artifact: `data/bench/compare-latest.json` · Chart: `docs/assets/compare-chart.svg`

## Related

- [Speed Bench](Speed-Bench) — full runner table + plate meld
- [Profiles](Profiles) — belt_1_0, belt_2_0, field_opt, expert
- [Release 4.7](Release) — bench-refresh pipeline