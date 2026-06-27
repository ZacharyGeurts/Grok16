# Release 3.0.0

**Tag:** `v3.0.0` · **Compiler:** 16.2.0 · **Previous tag:** v2.0.0

Web: [release.html](https://zacharygeurts.github.io/Grok16/release.html) · Repo: [RELEASE-3.0.md](https://github.com/ZacharyGeurts/Grok16/blob/main/RELEASE-3.0.md)

## Speed bench (report v3.0.0)

Versioned **compile + execution** benchmark — `speed_demo` suite @ `1.0.0`, 3s window.

| Category | Winner |
|----------|--------|
| Fastest execution | C++ g16 belt_2_0 — **85.3M ops/s** |
| Fastest compile | C g16 belt_2_0 — **318 ms** |
| Best Python | host CPython — **778K ops/s** (no compile) |

Wiki: [Speed-Bench](Speed-Bench) · [Uncompiled-Execution](Uncompiled-Execution) · [CMake-and-Linking](CMake-and-Linking)

## Checkout & gates

```bash
git checkout v3.0.0
export G16_PREFIX="$(pwd)"
export G16_BELT_PROFILE=belt_2_0
G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh test-battery-release
./scripts/grok16-toolchain.sh test-battery-belt
SPEED_DEMO_TARGET_SEC=3 ./scripts/grok16-toolchain.sh exec-full-bench
./scripts/grok16-toolchain.sh integrate
```

## Highlights

- **Speed bench v3.0.0** — compile ms + execution ops/s with version stamps
- **Uncompiled doctrine** — Python interpreter; C/C++ chamber compile-ahead
- **Queen-themed manual** — speed-bench, uncompiled, cmake-linking pages
- **exec-full-bench** / **exec-compare** toolchain hooks
- Single fabric + safety from 2.0 — `belt_2_0` default unchanged

## Upgrade from 2.0.0

1. `git checkout v3.0.0`
2. Set `G16_BELT_PROFILE=belt_2_0` and release-profile rebuild
3. `test-battery-release` + `test-battery-belt`
4. `SPEED_DEMO_TARGET_SEC=3 ./scripts/grok16-toolchain.sh exec-full-bench`
5. `./scripts/grok16-integrate.sh` before consumer deploy