# Grok16 speed-demo — compile + execution benchmark

**Report version:** 3.0.0 · **Distro:** 3.0.0 (v3.0.0)  
**Compiler:** Grok16-16.2.0 · dumpversion `16.1.1`  
**Bench suite:** speed_demo @ 1.0.0  
**Bench date:** 2026-06-27T03:02:28Z  
**Target execution window:** 3s per runner  
**Kernel:** speed_demo — FieldX86 loop (256×16 die, 240 frames/epoch, 512 prog_ops/frame)  
**Host:** default-X870-Pro-RS

## Summary

This report separates **wave-convert / compile time** (one-time, chamber can cache ahead) from **bin execution time** (timed field run). Python runners have zero compile — they execute on the interpreter.

- **Fastest execution:** C++ — g16 belt_2_0 — **85,294,665.80 ops/s**
- **Fastest compile:** C — g16 belt_2_0 — **318 ms**
- **Best Python (interpreter):** python_host — **777,876.44 ops/s**

## Full results

| Runner | Compile (ms) | Exec wall (ms) | ops/s | Binary bytes |
|--------|-------------:|---------------:|------:|-------------:|
| C++ — g16 belt_2_0 | 2,494 | 3,001 | 85,294,665.80 | 22,912 |
| C++ — host g++ -O2 | 1,710 | 3,001 | 83,153,507.73 | 21,640 |
| CMake — host g++ -O2 | 3,682 | 3,001 | 82,620,718.84 | 21,640 |
| C — g16 belt_2_0 | 318 | 3,000 | 79,451,081.93 | 16,248 |
| C — host gcc -O2 | 347 | 3,000 | 73,440,210.44 | 24,568 |
| Python — host CPython 3 | — | 3,001 | 777,876.44 | — |
| Python — gpy-16 GrokVM | — | 3,049 | 765,841.56 | — |

## Winners by category

- **C:** C — g16 belt_2_0 — 79,451,081.93 ops/s
- **CXX:** C++ — g16 belt_2_0 — 85,294,665.80 ops/s
- **CMAKE:** CMake — host g++ -O2 — 82,620,718.84 ops/s
- **PYTHON:** Python — host CPython 3 — 777,876.44 ops/s
- **Best first-run amortized** (exec ÷ (1 + compile_sec)): C — g16 belt_2_0 — 60,287,953.14 effective ops/s

## Doctrine

- **Dev / uncompiled:** Python runs at interpreter speed (~0.8M ops/s). C/C++ rely on chamber organization + compile ahead (cached on singular plane).
- **Release / plane:** Staged binaries reach ~84–91M ops/s on this host; compile is not in the timed execution path after cache hit.
- **Compare axis:** `field_execution_ops_per_sec` on identical `speed_demo` kernel.

## Reproduce

```bash
cd Grok16
SPEED_DEMO_TARGET_SEC=3 python3 scripts/field-exec-full-bench.py
python3 scripts/field-exec-stage.py
SPEED_DEMO_TARGET_SEC=3 python3 scripts/field-exec-compare.py
```

Machine JSON: `data/bench/exec-plane/field-exec-full-bench.json`

