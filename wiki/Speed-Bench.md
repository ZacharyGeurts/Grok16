# Speed Bench (report v4.7.1)

Web: [speed-bench.html](https://zacharygeurts.github.io/Grok16/speed-bench.html) · JSON: [field-exec-full-bench.json](https://github.com/ZacharyGeurts/Grok16/blob/main/docs/field-exec-full-bench.json)

**Grok16 distro 4.7.1** · **speed_demo suite v1.1.0** · **schema v5** · **11 runners** · **3s window** · **2026-06-27**

## Version stamps

| Field | Value |
|-------|-------|
| Report | `4.7.1` |
| Distro | `4.7.1` (`v4.7.1`) |
| g16 pkg | `Grok16-16.2.0` |
| Bench suite | `speed_demo` @ `1.1.0` |
| Schema | `grok16-field-exec-full-bench/v5` |

Doctrine: `data/grok16-speed-bench-version.json` · Plate meld: `data/grok16-plate-meld-bench-doctrine.json`

## Methodology

1. `field-plate-meld.py fuse` — plate fusion (4 plates on this witness)
2. `g16-compiler-sense-plate.py cycle` — sense profile ladder
3. Compile every runner (gcc, g16 belt_1_0/2_0, sense field_opt, CMake)
4. Execute `speed_demo` @ 3s — axis `field_execution_ops_per_sec`
5. Post-meld re-exec same ELF — verify hot path
6. Cross-ref `bench-all` from `data/bench/latest.json`

### Kernel

256×16 die · 240 frames/epoch · 512 prog_ops/frame · φ=0.618 · FieldX86 + entropy + wave + NEXUS

## Winners (cold exec, BSP rocket)

| Category | Winner | Value |
|----------|--------|------:|
| **Fastest execution** | C++ — host g++ -O2 | **95.3M ops/s** |
| **Best g16 C++** | C++ — g16 belt_2_0 | **92.6M ops/s** |
| **Fastest compile** | C — g16 belt_1_0 | **357 ms** |
| **Best amortized first-run** | C — g16 belt_1_0 | **66.4M eff.** |
| **Best Python** | host CPython 3 | **800K ops/s** |

## All executions (reference host @ 2026-06-27)

| Runner | Profile | Compile (ms) | ops/s |
|--------|---------|-------------:|------:|
| C++ — host g++ -O2 | — | 1,588 | **95.3M** |
| CMake — host g++ -O2 | — | 2,174 | 93.0M |
| C++ — g16 belt_2_0 | belt_2_0 | 1,883 | **92.6M** |
| C — g16 belt_1_0 | belt_1_0 | **357** | 90.1M |
| C++ — g16 sense field_opt | field_opt | 1,774 | 89.6M |
| C — g16 belt_2_0 | belt_2_0 | 449 | 87.5M |
| C++ — g16 belt_1_0 | belt_1_0 | 1,768 | 87.1M |
| C — host gcc -O2 | — | 496 | 82.6M |
| Python — host CPython 3 | — | — | **800K** |
| Python — gpy-16 GrokVM | — | — | 751K |

## Plate meld verdict

| Metric | Value |
|--------|-------|
| Meld generation | 2 |
| Plates fused | 4 |
| Sense vs belt_2_0 compile | **−109 ms** |
| Sense vs belt_2_0 exec ratio | **0.967** |
| Post-meld belt_2 re-exec | **82.9M ops/s** |

**Professional conclusion:** Plate meld does not block the hot path. Compiler-sense trades a small exec delta for faster wave-convert on this host; profile ladder unlocks when meld generation ≥ 2.

## Chart refresh

```bash
./scripts/grok16-toolchain.sh bench-refresh
# or: bench-charts after exec-comprehensive-bench
```

Charts: `docs/assets/speed-bench-chart.svg`, `triad-chart.svg`, `compare-chart.svg`, `bench-all-chart.svg`

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
- [Performance](Performance) — belt triad + bench-all charts