# Release 4.7.1

**Tag:** `v4.7.1` · **Compiler:** `g16 @ 16.2.0` · **Previous tag:** v4.2.0 · **Platforms:** 17 (incl. RISC-V)

Web: [release.html](https://zacharygeurts.github.io/Grok16/release.html) · Repo: [RELEASE-4.7.md](https://github.com/ZacharyGeurts/Grok16/blob/main/RELEASE-4.7.md)

## Speed & comparison charts (refreshed)

```bash
./scripts/grok16-toolchain.sh bench-refresh
# stepwise: bench-triad · bench-compare · bench-all · exec-comprehensive-bench · bench-charts
```

| Chart | Asset |
|-------|-------|
| speed_demo compile + exec | `docs/assets/speed-bench-chart.svg` |
| belt triad | `docs/assets/triad-chart.svg` |
| field vs host compare | `docs/assets/compare-chart.svg` |
| bench-all profiles | `docs/assets/bench-all-chart.svg` |

Manifest: `data/bench/charts-manifest.json`

## Speed bench (report v4.7.1)

Versioned **compile + execution** benchmark — `speed_demo` suite @ `1.1.0`, 3s window, schema v5.

| Category | Winner |
|----------|--------|
| Fastest execution | C++ host g++ -O2 — **95.3M ops/s** |
| Best g16 C++ | g16 belt_2_0 — **92.6M ops/s** |
| Fastest compile | C g16 belt_1_0 — **357 ms** |
| Best Python | host CPython 3 — **800K ops/s** |

Wiki: [Speed-Bench](Speed-Bench) · [Performance](Performance) · [Field-Research](Field-Research)

## Toolchain pairing

- **Host gcc-14** — bench-triad and bench-compare witness
- **pythong 16.1.0-gpy16** — GPY-16 driver pairing on speed bench reports
- **g16 @ 16.2.0** — `belt_2_0` default single-fabric profile

## .launch chambers

```bash
export GROK16_ROOT=/path/to/Grok16 SG_ROOT=/path/to/SG
./scripts/grok16-launch-verify.sh
```

## MCP server (since 4.0)

Agents connect via [mcp/grok16_mcp_server.py](https://github.com/ZacharyGeurts/Grok16/blob/main/mcp/grok16_mcp_server.py):

- `grok16_version` — distro 4.7.1 stamps
- `grok16_toolchain` — status, verify, bench gates
- `grok16_rtx_gate` — queen_rtx permit
- `grok16_speed_bench` — published JSON
- `grok16_power_sort` — power sort plate

Setup: [mcp/README.md](https://github.com/ZacharyGeurts/Grok16/blob/main/mcp/README.md)

## Checkout & gates

```bash
git checkout v4.7.1
export G16_PREFIX="$(pwd)"
export G16_BELT_PROFILE=belt_2_0
G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh test-battery-release
./scripts/grok16-toolchain.sh test-battery-belt
./scripts/grok16-toolchain.sh bench-refresh
./scripts/grok16-toolchain.sh integrate
```

## Highlights

- **bench-refresh** — one-shot pipeline for all comparison charts and JSON reports
- **performance.html** — embeds triad, compare, and bench-all charts
- **Legacy isolation chamber** — sealed legacy language tests in SG/NewLatest
- **README front page** — GitHub Pages home mirrors repository README
- Portable `.launch` chambers and 17-platform release matrix
- Single fabric + safety from 2.0 — `belt_2_0` default unchanged

## Upgrade from 4.2.0

1. `git checkout v4.7.1`
2. `test-battery-release` + `test-battery-belt`
3. `./scripts/grok16-toolchain.sh bench-refresh` — compare charts to `docs/assets/`
4. `./scripts/grok16-integrate.sh` before consumer deploy