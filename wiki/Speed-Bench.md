# Speed Bench (report v3.1.0)

Web: [speed-bench.html](https://zacharygeurts.github.io/Grok16/speed-bench.html) · JSON: [field-exec-full-bench.json](https://github.com/ZacharyGeurts/Grok16/blob/main/docs/field-exec-full-bench.json)

**Grok16 distro 3.0.0** · **speed_demo suite v1.1.0** · **schema v4** · **11 runners** · **3s window**

## Version stamps

| Field | Value |
|-------|-------|
| Report | `3.1.0` |
| Distro | `3.0.0` (`v3.0.0`) |
| g16 pkg | `Grok16-16.2.0` |
| Bench suite | `speed_demo` @ `1.1.0` |
| Schema | `grok16-field-exec-full-bench/v4` |

Doctrine: `data/grok16-speed-bench-version.json` · Plate meld: `data/grok16-plate-meld-bench-doctrine.json`

## Methodology

1. `field-plate-meld.py fuse` — fast plate fusion (24 plates, ~87 ms)
2. `g16-compiler-sense-plate.py cycle` — sense profile ladder
3. Compile every runner (gcc, g16 belt_1_0/2_0, sense expert, CMake)
4. Execute `speed_demo` @ 3s — axis `field_execution_ops_per_sec`
5. Post-meld re-exec same ELF — verify hot path
6. Cross-ref `bench-all` from `data/bench/latest.json`

### Kernel

256×16 die · 240 frames/epoch · 512 prog_ops/frame · φ=0.618 · FieldX86 + entropy + wave + NEXUS

## All executions (reference host @ 2026-06-27)

| Runner | Profile | Compile | ops/s |
|--------|---------|--------:|------:|
| CMake host g++ -O2 | — | 2,814 ms | **85.8M** |
| C++ host g++ -O2 | — | 1,710 ms | 83.9M |
| C++ g16 sense expert | expert | 1,608 ms | 82.1M |
| C++ g16 belt_1_0 | belt_1_0 | 1,888 ms | 78.4M |
| C g16 belt_1_0 | belt_1_0 | 395 ms | 77.0M |
| C g16 belt_2_0 | belt_2_0 | **296 ms** | 75.0M |
| C++ g16 belt_2_0 | belt_2_0 | 2,021 ms | 74.8M |
| C host gcc -O2 | — | 459 ms | 73.7M |
| Python gpy-16 | — | — | **777K** |
| Python CPython 3 | — | — | 748K |

## Plate meld verdict

| Metric | Value |
|--------|-------|
| Meld generation | 2 |
| Plates fused | 24 |
| Sense profile | `expert` (eye_ear_green, score 0.75) |
| Sense vs belt_2_0 exec | **+9.8%** (82.1M vs 74.8M) |
| Sense vs belt_2_0 compile | **−413 ms** |
| Meld helps profile ladder | **yes** |
| Meld slows hot path | **no** |

**Professional conclusion:** Plate meld helps **situations** where compiler-sense can pick a better profile than static `belt_2_0`. It does not replace compile-ahead for C/C++; it optimizes **which** profile wave-converts.

## Reproduce

```bash
cd Grok16
export G16_PREFIX="$(pwd)"
export GROK16_SG_ROOT=/path/to/SG
export NEXUS_STATE_DIR=$GROK16_SG_ROOT/NewLatest/state
G16_PLATE_MELD_CMD=fuse SPEED_DEMO_TARGET_SEC=3 ./scripts/grok16-toolchain.sh exec-comprehensive-bench
```

## Related

- [Uncompiled Execution](Uncompiled-Execution)
- [CMake and Linking](CMake-and-Linking)
- [Performance](Performance) — belt triad + bench-all