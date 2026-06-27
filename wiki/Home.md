# Grok16 @ 4.7.1

**Stable release** — self-hosted `g16` @ **16.2.0**, **versioned speed bench**, benchmark chart refresh, uncompiled doctrine, Queen-themed manual.

| | |
|---|---|
| **Web manual** | https://zacharygeurts.github.io/Grok16/ |
| **Field Research book** | https://zacharygeurts.github.io/Field_Research/ |
| **Speed bench** | https://zacharygeurts.github.io/Grok16/speed-bench.html |
| **Repo** | https://github.com/ZacharyGeurts/Grok16 |
| **Tag** | `v4.7.1` |
| **Compiler** | `g16 (Grok16-16.2.0) 16.2.0` |

## Speed bench (report v4.7.1)

| Category | Winner | Compile | Execution |
|----------|--------|--------:|----------:|
| **Fastest execution** | C++ host g++ -O2 | BSP hit | **95.3M ops/s** |
| **Best g16 C++** | g16 belt_2_0 | BSP hit | **92.6M ops/s** |
| **Fastest compile** | C g16 belt_1_0 | rocket | **357 ms** |
| **Best Python** | host CPython 3 | — | **800K ops/s** |

Report: [SPEED-BENCH-REPORT.md](https://github.com/ZacharyGeurts/Grok16/blob/main/docs/SPEED-BENCH-REPORT.md) · Wiki: [Speed-Bench](Speed-Bench)

Refresh all charts:

```bash
./scripts/grok16-toolchain.sh bench-refresh
```

## What's new in 4.7

- **bench-refresh** — triad + compare + bench-all + comprehensive exec + SVG charts + manual rebuild
- **bench-charts** — `scripts/grok16-bench-charts.py` from live JSON
- **gcc-14 host pin** — bench-triad and bench-compare witness Ubuntu gcc-14
- **Legacy isolation chamber** — sealed BASIC/Pascal/VB tests in SG/NewLatest
- **README front page** — GitHub Pages home mirrors repository README

## MCP (since 4.0)

**Model Context Protocol** — `mcp/grok16_mcp_server.py` exposes version, toolchain, RTX gate, speed bench, power sort. [Setup](https://github.com/ZacharyGeurts/Grok16/blob/main/mcp/README.md)

## Field Research book (technology spine)

Thirteen chapters from combinatorics endpoint to compatibility layers — [Field Research](Field-Research) wires the book into Grok16 doctrine (`g16-field-research-book.json`). Run `python3 lib/field-research-book.py verify` after pull.

## Single fabric (2.0 technology)

**Knowing is fixed-size.** Parallel I/O may fan in; truth collapses to **one belt amplitude** at depth 0.

- `belt_2_0` — chunked redata (8192), wave-massive, single-location reads
- Depth-field creation **forbidden** at integrated consumers
- Time is **linear** — sovereign `linear_ns` (`ironclad:time:1`)

## Start here

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16 && git checkout v4.7.1
export G16_PREFIX="$(pwd)"
export G16_BELT_PROFILE=belt_2_0
G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh test-battery-release
./scripts/grok16-toolchain.sh test-battery-belt
./scripts/grok16-toolchain.sh bench-refresh
./scripts/grok16-toolchain.sh integrate
```

## Manual map

| Wiki | Web | Topic |
|------|-----|-------|
| [Speed Bench](Speed-Bench) | [speed-bench.html](https://zacharygeurts.github.io/Grok16/speed-bench.html) | Versioned compile + exec bench |
| [Uncompiled Execution](Uncompiled-Execution) | [uncompiled.html](https://zacharygeurts.github.io/Grok16/uncompiled.html) | Python interpreter, chamber compile-ahead |
| [CMake and Linking](CMake-and-Linking) | [cmake-linking.html](https://zacharygeurts.github.io/Grok16/cmake-linking.html) | Toolchain, g16-ld, speed_demo CMake |
| [Release 4.7](Release) | [release.html](https://zacharygeurts.github.io/Grok16/release.html) | 4.7 changelog |
| [Single Fabric](Single-Fabric) | [single-fabric.html](https://zacharygeurts.github.io/Grok16/single-fabric.html) | Belt knowing, one amplitude |
| [Safety](Safety) | [safety.html](https://zacharygeurts.github.io/Grok16/safety.html) | Depth impossible, Ironclad |
| [Getting Started](Getting-Started) | [getting-started.html](https://zacharygeurts.github.io/Grok16/getting-started.html) | Bootstrap, rebuild, verify |
| [Performance](Performance) | [performance.html](https://zacharygeurts.github.io/Grok16/performance.html) | Belt triad + speed bench + charts |
| [Integration](Integration) | [integration.html](https://zacharygeurts.github.io/Grok16/integration.html) | Queen, World_Redata, integrate |
| [Field Research](Field-Research) | [field-research.html](https://zacharygeurts.github.io/Grok16/field-research.html) | Book spine, combinatorics → layers |