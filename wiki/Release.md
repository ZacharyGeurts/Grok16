# Release 4.0.0

**Tag:** `v4.0.0` · **Compiler:** 16.2.0 · **Previous tag:** v3.0.0

Web: [release.html](https://zacharygeurts.github.io/Grok16/release.html) · Repo: [RELEASE-4.0.md](https://github.com/ZacharyGeurts/Grok16/blob/main/RELEASE-4.0.md)

## Speed bench (report v4.0.0)

Versioned **compile + execution** benchmark — `speed_demo` suite @ `1.1.0`, 3s window, schema v4.

| Category | Winner |
|----------|--------|
| Fastest execution | CMake host g++ -O2 — **85.8M ops/s** |
| Best g16 C++ (plate meld) | g16 sense expert — **82.1M ops/s** |
| Best Python | gpy-16 GrokVM — **777K ops/s** |

Wiki: [Speed-Bench](Speed-Bench) · [Field-Research](Field-Research)

## MCP server (new in 4.0)

Agents connect via [mcp/grok16_mcp_server.py](https://github.com/ZacharyGeurts/Grok16/blob/main/mcp/grok16_mcp_server.py):

- `grok16_version` — distro 4.0.0 stamps
- `grok16_toolchain` — status, verify, bench gates
- `grok16_rtx_gate` — queen_rtx permit
- `grok16_speed_bench` — published JSON
- `grok16_power_sort` — cool combinatorics plate

Setup: [mcp/README.md](https://github.com/ZacharyGeurts/Grok16/blob/main/mcp/README.md)

## Checkout & gates

```bash
git checkout v4.0.0
export G16_PREFIX="$(pwd)"
export G16_BELT_PROFILE=belt_2_0
G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh test-battery-release
./scripts/grok16-toolchain.sh test-battery-belt
SPEED_DEMO_TARGET_SEC=3 ./scripts/grok16-toolchain.sh exec-full-bench
./scripts/grok16-toolchain.sh integrate
pip install -r requirements-mcp.txt
```

## Highlights

- **Power sort plate** — Ironclad meld, cool_sort thermal layers, section availability
- **Speed bench v4.0.0** — distro tag + schema v4 on every bench run
- **MCP** — Cursor / Claude Desktop toolchain bridge
- Single fabric + safety from 2.0 — `belt_2_0` default unchanged

## Upgrade from 3.0.0

1. `git checkout v4.0.0`
2. `test-battery-release` + `test-battery-belt`
3. `SPEED_DEMO_TARGET_SEC=3 ./scripts/grok16-toolchain.sh exec-full-bench` — compare to `docs/field-exec-full-bench.json`
4. Wire MCP: copy `mcp/cursor-mcp.json.example` into your Cursor config
5. `./scripts/grok16-integrate.sh` before consumer deploy