# Grok16 @ 1.0.0

**Stable release** for field engineers — self-hosted `g16` @ **16.1.1**, unified driver, `gnu++26` / `gnu17`.

| | |
|---|---|
| **Web manual** | https://zacharygeurts.github.io/Grok16/ |
| **Repo** | https://github.com/ZacharyGeurts/Grok16 |
| **Tag** | `v1.0.0` |
| **Compiler** | `g16 (Grok16-16.1.1) 16.1.1` |

## Start here (engineers)

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16 && git checkout v1.0.0
export G16_PREFIX="$(pwd)"
G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh test-battery-release
```

## Manual map

| Wiki | Web | Topic |
|------|-----|-------|
| [Release](Release) | [release.html](https://zacharygeurts.github.io/Grok16/release.html) | 1.0.0 changelog, upgrade |
| [Getting Started](Getting-Started) | [getting-started.html](https://zacharygeurts.github.io/Grok16/getting-started.html) | Bootstrap, rebuild, verify |
| [Architecture](Architecture) | [architecture.html](https://zacharygeurts.github.io/Grok16/architecture.html) | Forge, unified driver |
| [Batteries](Batteries) | [batteries.html](https://zacharygeurts.github.io/Grok16/batteries.html) | Validation tiers, release gate |
| [Toolkits](Toolkits) | [toolkits.html](https://zacharygeurts.github.io/Grok16/toolkits.html) | GPY-16, binutils, languages |
| [Linker](Linker) | [linker.html](https://zacharygeurts.github.io/Grok16/linker.html) | g16-ld, 16 targets |
| [Profiles](Profiles) | [profiles.html](https://zacharygeurts.github.io/Grok16/profiles.html) | field_opt, expert, heavy |
| [Performance](Performance) | [performance.html](https://zacharygeurts.github.io/Grok16/performance.html) | Bench, LTO, PGO |
| [Integration](Integration) | [integration.html](https://zacharygeurts.github.io/Grok16/integration.html) | Queen, World_Redata |
| [Reference](Reference) | [reference.html](https://zacharygeurts.github.io/Grok16/reference.html) | Commands, env vars |
| [Master Coder](Master-Coder) | [master-coder.html](https://zacharygeurts.github.io/Grok16/master-coder.html) | Indexed command hub |