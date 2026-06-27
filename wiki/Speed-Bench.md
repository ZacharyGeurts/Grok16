# Speed Bench (report v3.0.0)

Web: [speed-bench.html](https://zacharygeurts.github.io/Grok16/speed-bench.html) · JSON: [field-exec-full-bench.json](https://github.com/ZacharyGeurts/Grok16/blob/main/docs/field-exec-full-bench.json)

**Grok16 distro 3.0.0** · **speed_demo suite v1.0.0** · **3s execution window**

## Version stamps

| Field | Value |
|-------|-------|
| Report | `3.0.0` |
| Distro | `3.0.0` (`v3.0.0`) |
| g16 pkg | `Grok16-16.2.0` |
| Bench suite | `speed_demo` @ `1.0.0` |
| Schema | `grok16-field-exec-full-bench/v3` |

Doctrine: `data/grok16-speed-bench-version.json`

## Winners (reference host)

| Category | Winner | Compile | Execution |
|----------|--------|--------:|----------:|
| **Fastest execution** | C++ g16 belt_2_0 | 2,494 ms | **85.3M ops/s** |
| **Fastest compile** | C g16 belt_2_0 | **318 ms** | 79.5M ops/s |
| **Best C** | C g16 belt_2_0 | 318 ms | 79.5M ops/s |
| **Best CMake** | CMake host g++ -O2 | 3,682 ms | 82.6M ops/s |
| **Best Python** | host CPython 3 | — | **778K ops/s** |
| **Best amortized first-run** | C g16 belt_2_0 | 318 ms | 60.3M effective |

Python has **no compile** — interpreter lane only.

## Reproduce

```bash
cd Grok16
git checkout v3.0.0
export G16_PREFIX="$(pwd)"
SPEED_DEMO_TARGET_SEC=3 ./scripts/grok16-toolchain.sh exec-full-bench
./scripts/grok16-toolchain.sh exec-compare
```

## Related

- [Uncompiled Execution](Uncompiled-Execution) — chamber, not compiling, compile ahead
- [CMake and Linking](CMake-and-Linking) — toolchain file, g16-ld
- [Performance](Performance) — belt triad, field-nexus-bench