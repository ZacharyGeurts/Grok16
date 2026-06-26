# Performance

Web: [performance.html](https://zacharygeurts.github.io/Grok16/performance.html)

## Primary metric

```bash
./scripts/grok16-toolchain.sh field-bench
```

Field-Opt kernel: `examples/field-nexus-bench/` — entropy + NEXUS scoring.

## Release rebuild

```bash
export G16_RELEASE_PROFILE=1
export G16_ENABLE_LTO=1
export G16_ENABLE_PGO=1
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh profile    # PGO → data/pgo/
G16_ENABLE_PGO=1 ./scripts/grok16-toolchain.sh field-bench
```

## Bench matrix

```bash
./scripts/grok16-toolchain.sh bench-all   # → data/bench/latest.json
```

| Profile | Workload |
|---------|----------|
| `field_opt` | field-nexus-bench |
| `ai` | ai-matrix-bench |
| `field_compute` | field-canvas-kernel |
| `vulkan_rtx` | RTX SIMD (gated on silicon) |

## Heavy tier

`test-battery-heavy` runs bench under `G16_BENCH_PROFILE=heavy` + `G16_RELEASE_PROFILE=1`.