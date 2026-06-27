# Performance

Web: [performance.html](https://zacharygeurts.github.io/Grok16/performance.html)

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

- **belt_1_0** — matches host runtime; compile ~8% faster
- **belt_2_0** — single fabric production belt; 512 slots, chunked redata

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

| Profile | Workload |
|---------|----------|
| `belt_2_0` | field-nexus-bench (2.0 default) |
| `belt_1_0` | field-nexus-bench baseline |
| `field_opt` | field-nexus-bench |
| `ai` | ai-matrix-bench |
| `field_compute` | field-canvas-kernel |
| `vulkan_rtx` | RTX SIMD (gated) |

## Gates

- `test-battery-heavy` — release profile bench
- `test-battery-belt` — 2.0 belt validation