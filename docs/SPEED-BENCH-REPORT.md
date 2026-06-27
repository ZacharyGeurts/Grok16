# Grok16 speed-demo — comprehensive compile + execution benchmark

**Report version:** 4.0.0 · **Distro:** 4.0.0 (v4.0.0)  
**Compiler:** Grok16-16.2.0 · dumpversion `16.1.1`  
**Bench suite:** speed_demo @ 1.1.0  
**Schema:** grok16-field-exec-full-bench/v4  
**Bench date:** 2026-06-27T07:39:24Z  
**Runners tested:** 11  
**Target execution window:** 3s per runner  
**Host:** Linux default-X870-Pro-RS 6.14.0-37-generic #37~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Nov 20 10:25:38 UTC 2 x86_64

## Methodology (professional)

1. **BSP (Binary Staged Plane)** — reuse `data/bench/exec-plane/` cache; compile only on miss (`G16_EXEC_BSP=1` default).
2. **Rocket compile** — ccache + `-pipe` + Ninja CMake on miss (`G16_ROCKET_COMPILE=1` default).
3. **Plate meld cycle** — `field-plate-meld.py fuse` then `g16-compiler-sense-plate.py cycle` before compiles.
4. **Wave-convert** — timed as `compile_ms`; BSP hits record ~0 ms.
5. **Field execution** — identical `speed_demo` kernel; axis `field_execution_ops_per_sec`; Python = interpreter (no compile).
6. **Post-meld re-exec** — same ELF as `cxx_g16_belt_2` after meld; proves meld does not slow hot path.
7. **bench-all cross-ref** — profile suite from `data/bench/latest.json` when present.

### Kernel specification

| Parameter | Value |
|-----------|------:|
| Die slots | 256 |
| Wave bands | 16 |
| Frames / epoch | 240 |
| Prog ops / frame | 512 |
| Ops / epoch | 122,880 |
| φ (entropy fold) | 0.6180339887 |
| Loops | fieldx86_run, entropy_fold, wave_phase, nexus_score |

## Summary

Separates **wave-convert / compile** (one-time, chamber cache) from **bin execution** (timed field run).

- **Fastest execution:** C++ — host g++ -O2 — **95,344,504.64 ops/s**
- **Fastest compile:** C — g16 belt_1_0 — **357 ms**
- **Best Python (interpreter):** python_host — **799,963.17 ops/s**

## Plate meld analysis

- **Meld generation:** 2 · **plates fused:** 4
- **Compiler sense profile:** `field_opt` (default) · score 0.0
- **Sense vs belt_2_0 exec ratio:** 0.9672
- **Post-meld re-exec ratio (same ELF):** 0.8945 — hot path check
- **Meld helps profile selection:** yes

## Full results (all executions)

| Runner | Profile | Compile (ms) | Exec wall (ms) | ops/s | Bytes | Pass |
|--------|---------|-------------:|---------------:|------:|------:|------|
| C++ — host g++ -O2 | — | 1,588 | 3,000 | 95,344,504.64 | 21,640 | cold |
| CMake — host g++ -O2 | — | 2,174 | 3,001 | 92,954,564.41 | 21,640 | cold |
| C++ — g16 belt_2_0 | belt_2_0 | 1,883 | 3,001 | 92,625,263.73 | 22,912 | cold |
| C — g16 belt_1_0 | belt_1_0 | 357 | 3,001 | 90,112,560.56 | 16,192 | cold |
| C++ — g16 sense field_opt | field_opt | 1,774 | 3,001 | 89,585,919.78 | 22,784 | cold |
| C — g16 belt_2_0 | belt_2_0 | 449 | 3,001 | 87,455,702.49 | 16,248 | cold |
| C++ — g16 belt_1_0 | belt_1_0 | 1,768 | 3,001 | 87,079,343.11 | 22,784 | cold |
| C++ — g16 belt_2_0 (post-meld re-exec) | belt_2_0 | 0 | 3,000 | 82,855,139.69 | 22,912 | post_meld |
| C — host gcc -O2 | — | 496 | 3,001 | 82,554,256.71 | 24,568 | cold |
| Python — host CPython 3 | — | — | 3,072 | 799,963.17 | — | cold |
| Python — gpy-16 GrokVM | — | — | 3,108 | 751,139.20 | — | cold |

## bench-all profile suite (field-nexus-bench)

| Profile | compile_ms | run_ms | binary_bytes | kernel |
|---------|------------|--------|--------------|--------|
| ai | 735 | 6 | 18232 | grok16_bench profile=ai std=gnu++26 __cplusplus=202400 n=64 iters=48 wall_ms=4.01076 checksum=141090 |
| field_compute | 543 | 3 | 16240 | field_canvas_kernel entropy_micro=500026 phi_micro=618000 wave_speed_micro=1420000 FIELD_X86_DIE=1 |
| vulkan_rtx | 876 | 4 | 22728 | grok16_field_bench profile=default std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 wall_ms=2.13762 nexus_checksum=-nan |
| ai_agent | 662 | 7 | 16672 | grok16_bench profile=ai std=gnu++26 __cplusplus=202400 n=64 iters=48 wall_ms=4.13678 checksum=141090 |
| expert | 2275 | 14 | 21200 | grok16_field_bench profile=field_opt std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 wall_ms=3.30415 nexus_checksum=-nan |
| field_opt | 1648 | 8 | 22712 | grok16_field_bench profile=field_opt std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 die_slots=256 belt_chunk=1 redata_chunk=512 wall_ms=2.50406 nexus_checksum=-nan |
| heavy | 1766 | 7 | 22840 | grok16_field_bench profile=field_opt std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 die_slots=256 belt_chunk=1 redata_chunk=512 wall_ms=2.77062 nexus_checksum=-nan |
| belt_1_0 | 1922 | 9 | 22712 | grok16_field_bench profile=belt_1_0 std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 die_slots=256 belt_chunk=1 redata_chunk=512 wall_ms=2.93492 nexus_checksum=-nan |
| belt_2_0 | 1751 | 9 | 22840 | grok16_field_bench profile=belt_2_0 std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 die_slots=512 belt_chunk=64 redata_chunk=8192 wall_ms=3.52465 nexus_checksum=-nan |

## Winners by category

- **C:** C — g16 belt_1_0 — 90,112,560.56 ops/s
- **CXX:** C++ — host g++ -O2 — 95,344,504.64 ops/s
- **CMAKE:** CMake — host g++ -O2 — 92,954,564.41 ops/s
- **PYTHON:** Python — host CPython 3 — 799,963.17 ops/s
- **Best first-run amortized** (exec ÷ (1 + compile_sec)): C — g16 belt_1_0 — 66,405,229.56 effective ops/s

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

