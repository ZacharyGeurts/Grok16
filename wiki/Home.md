# Grok16 @ 2.0.0

**Stable release** — self-hosted `g16` @ **16.2.0**, **single fabric** belt, Ironclad safety meld.

| | |
|---|---|
| **Web manual** | https://zacharygeurts.github.io/Grok16/ |
| **Repo** | https://github.com/ZacharyGeurts/Grok16 |
| **Tag** | `v2.0.0` |
| **Compiler** | `g16 (Grok16-16.2.0) 16.2.0` |

## Single fabric (2.0 technology)

**Knowing is fixed-size.** Parallel I/O may fan in; truth collapses to **one belt amplitude** at depth 0.

- `belt_2_0` — chunked redata (8192), wave-massive, single-location reads
- Depth-field creation **forbidden** at integrated consumers
- Time is **linear** — sovereign `linear_ns` (`ironclad:time:1`)

Doctrine: `data/grok16-single-fabric-doctrine.json`

## Start here

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16 && git checkout v2.0.0
export G16_PREFIX="$(pwd)"
export G16_BELT_PROFILE=belt_2_0
G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh test-battery-release
./scripts/grok16-toolchain.sh test-battery-belt
./scripts/grok16-toolchain.sh integrate
```

## Manual map

| Wiki | Web | Topic |
|------|-----|-------|
| [Release 2.0](Release) | [release.html](https://zacharygeurts.github.io/Grok16/release.html) | 2.0 changelog, single fabric |
| [Single Fabric](Single-Fabric) | [concepts.html](https://zacharygeurts.github.io/Grok16/concepts.html) | Belt knowing, one amplitude |
| [Safety](Safety) | [integration.html](https://zacharygeurts.github.io/Grok16/integration.html) | Depth impossible, Ironclad |
| [Getting Started](Getting-Started) | [getting-started.html](https://zacharygeurts.github.io/Grok16/getting-started.html) | Bootstrap, rebuild, verify |
| [Architecture](Architecture) | [architecture.html](https://zacharygeurts.github.io/Grok16/architecture.html) | Forge, unified driver |
| [Batteries](Batteries) | [batteries.html](https://zacharygeurts.github.io/Grok16/batteries.html) | release + belt gates |
| [Profiles](Profiles) | [profiles.html](https://zacharygeurts.github.io/Grok16/profiles.html) | belt_1_0, belt_2_0, field_opt |
| [Performance](Performance) | [performance.html](https://zacharygeurts.github.io/Grok16/performance.html) | bench-triad, LTO, PGO |
| [Integration](Integration) | [integration.html](https://zacharygeurts.github.io/Grok16/integration.html) | Queen, World_Redata, integrate |
| [Reference](Reference) | [reference.html](https://zacharygeurts.github.io/Grok16/reference.html) | Commands, env vars |