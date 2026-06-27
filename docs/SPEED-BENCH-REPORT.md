# Grok16 speed-demo — compile + execution benchmark

**Bench date:** 2026-06-27T02:57:38Z  
**Target execution window:** 3s per runner  
**Kernel:** speed_demo — FieldX86 loop (256×16 die, 240 frames/epoch, 512 prog_ops/frame)  
**Host:** default-X870-Pro-RS

## Summary

This report separates **wave-convert / compile time** (one-time, chamber can cache ahead) from **bin execution time** (timed field run). Python runners have zero compile — they execute on the interpreter.

- **Fastest execution:** C++ — g16 belt_2_0 — **88,487,346.90 ops/s**
- **Fastest compile:** C — g16 belt_2_0 — **434 ms**
- **Best Python (interpreter):** python_gpy — **763,849.82 ops/s**

## Full results

| Runner | Compile (ms) | Exec wall (ms) | ops/s | Binary bytes |
|--------|-------------:|---------------:|------:|-------------:|
| C++ — g16 belt_2_0 | 2,738 | 3,001 | 88,487,346.90 | 22,912 |
| CMake — host g++ -O2 | 2,417 | 3,001 | 85,739,968.42 | 21,640 |
| C++ — host g++ -O2 | 2,035 | 3,001 | 85,339,576.29 | 21,640 |
| C — host gcc -O2 | 621 | 3,001 | 81,437,641.13 | 24,568 |
| C — g16 belt_2_0 | 434 | 3,000 | 80,485,448.98 | 16,248 |
| Python — gpy-16 GrokVM | — | 3,057 | 763,849.82 | — |
| Python — host CPython 3 | — | 3,076 | 719,081.10 | — |

## Winners by category

- **C:** C — host gcc -O2 — 81,437,641.13 ops/s
- **CXX:** C++ — g16 belt_2_0 — 88,487,346.90 ops/s
- **CMAKE:** CMake — host g++ -O2 — 85,739,968.42 ops/s
- **PYTHON:** Python — gpy-16 GrokVM — 763,849.82 ops/s
- **Best first-run amortized** (exec ÷ (1 + compile_sec)): C — g16 belt_2_0 — 56,140,235.75 effective ops/s

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

