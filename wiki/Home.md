# Grok16 @ 3.0.0

**Stable release** — self-hosted `g16` @ **16.2.0**, **versioned speed bench**, uncompiled doctrine, Queen-themed manual.

| | |
|---|---|
| **Web manual** | https://zacharygeurts.github.io/Grok16/ |
| **Speed bench** | https://zacharygeurts.github.io/Grok16/speed-bench.html |
| **Repo** | https://github.com/ZacharyGeurts/Grok16 |
| **Tag** | `v3.0.0` |
| **Compiler** | `g16 (Grok16-16.2.0) 16.2.0` |

## Speed bench (report v3.0.0)

| Category | Winner | Compile | Execution |
|----------|--------|--------:|----------:|
| **Fastest execution** | C++ g16 belt_2_0 | 2,494 ms | **85.3M ops/s** |
| **Fastest compile** | C g16 belt_2_0 | **318 ms** | 79.5M ops/s |
| **Best Python** | host CPython 3 | — | **778K ops/s** |

Report: [SPEED-BENCH-REPORT.md](https://github.com/ZacharyGeurts/Grok16/blob/main/docs/SPEED-BENCH-REPORT.md) · Wiki: [Speed-Bench](Speed-Bench)

## Single fabric (2.0 technology)

**Knowing is fixed-size.** Parallel I/O may fan in; truth collapses to **one belt amplitude** at depth 0.

- `belt_2_0` — chunked redata (8192), wave-massive, single-location reads
- Depth-field creation **forbidden** at integrated consumers
- Time is **linear** — sovereign `linear_ns` (`ironclad:time:1`)

## Start here

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16 && git checkout v3.0.0
export G16_PREFIX="$(pwd)"
export G16_BELT_PROFILE=belt_2_0
G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh test-battery-release
./scripts/grok16-toolchain.sh test-battery-belt
SPEED_DEMO_TARGET_SEC=3 ./scripts/grok16-toolchain.sh exec-full-bench
./scripts/grok16-toolchain.sh integrate
```

## Manual map

| Wiki | Web | Topic |
|------|-----|-------|
| [Speed Bench](Speed-Bench) | [speed-bench.html](https://zacharygeurts.github.io/Grok16/speed-bench.html) | Versioned compile + exec bench |
| [Uncompiled Execution](Uncompiled-Execution) | [uncompiled.html](https://zacharygeurts.github.io/Grok16/uncompiled.html) | Python interpreter, chamber compile-ahead |
| [CMake and Linking](CMake-and-Linking) | [cmake-linking.html](https://zacharygeurts.github.io/Grok16/cmake-linking.html) | Toolchain, g16-ld, speed_demo CMake |
| [Release 3.0](Release) | [release.html](https://zacharygeurts.github.io/Grok16/release.html) | 3.0 changelog |
| [Single Fabric](Single-Fabric) | [single-fabric.html](https://zacharygeurts.github.io/Grok16/single-fabric.html) | Belt knowing, one amplitude |
| [Safety](Safety) | [safety.html](https://zacharygeurts.github.io/Grok16/safety.html) | Depth impossible, Ironclad |
| [Getting Started](Getting-Started) | [getting-started.html](https://zacharygeurts.github.io/Grok16/getting-started.html) | Bootstrap, rebuild, verify |
| [Performance](Performance) | [performance.html](https://zacharygeurts.github.io/Grok16/performance.html) | Belt triad + speed bench |
| [Integration](Integration) | [integration.html](https://zacharygeurts.github.io/Grok16/integration.html) | Queen, World_Redata, integrate |