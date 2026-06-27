# Grok16 speed-demo — comprehensive compile + execution benchmark

**Report version:** 3.1.0 · **Distro:** 3.0.0 (v3.0.0)  
**Compiler:** Grok16-16.2.0 · dumpversion `16.1.1`  
**Bench suite:** speed_demo @ 1.1.0  
**Schema:** grok16-field-exec-full-bench/v4  
**Bench date:** 2026-06-27T03:12:38Z  
**Runners tested:** 11  
**Target execution window:** 3s per runner  
**Host:** Linux default-X870-Pro-RS 6.14.0-37-generic #37~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Nov 20 10:25:38 UTC 2 x86_64

## Methodology (professional)

1. **Plate meld cycle** — `field-plate-meld.py fuse` (fast) then `g16-compiler-sense-plate.py cycle` before compiles.
2. **Wave-convert** — each binary runner: single g16/gcc invoke or CMake configure+build (timed as `compile_ms`).
3. **Field execution** — identical `speed_demo` kernel; axis `field_execution_ops_per_sec`; Python = interpreter (no compile).
4. **Post-meld re-exec** — same ELF as `cxx_g16_belt_2` after meld; proves meld does not slow hot path.
5. **bench-all cross-ref** — profile suite from `data/bench/latest.json` when present.

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

- **Fastest execution:** CMake — host g++ -O2 — **84,432,656.03 ops/s**
- **Fastest compile:** C — g16 belt_1_0 — **336 ms**
- **Best Python (interpreter):** python_host — **768,456.59 ops/s**

## Plate meld analysis

- **Meld generation:** 3 · **plates fused:** 24
- **Compiler sense profile:** `expert` (eye_ear_green) · score 0.75
- **Sense vs belt_2_0 exec ratio:** 1.0002
- **Post-meld re-exec ratio (same ELF):** 0.9901 — hot path OK
- **Meld helps profile selection:** yes

## Full results (all executions)

| Runner | Profile | Compile (ms) | Exec wall (ms) | ops/s | Bytes | Pass |
|--------|---------|-------------:|---------------:|------:|------:|------|
| CMake — host g++ -O2 | — | 2,010 | 3,001 | 84,432,656.03 | 21,640 | cold |
| C++ — g16 sense expert | expert | 1,426 | 3,000 | 82,036,773.98 | 21,272 | cold |
| C++ — g16 belt_2_0 | belt_2_0 | 1,629 | 3,001 | 82,021,104.03 | 22,912 | cold |
| C++ — host g++ -O2 | — | 1,360 | 3,001 | 81,848,194.01 | 21,640 | cold |
| C++ — g16 belt_2_0 (post-meld re-exec) | belt_2_0 | 0 | 3,001 | 81,205,972.77 | 22,912 | post_meld |
| C — host gcc -O2 | — | 385 | 3,001 | 80,589,704.68 | 24,568 | cold |
| C — g16 belt_2_0 | belt_2_0 | 369 | 3,000 | 78,518,560.97 | 16,248 | cold |
| C — g16 belt_1_0 | belt_1_0 | 336 | 3,001 | 78,129,170.15 | 16,192 | cold |
| C++ — g16 belt_1_0 | belt_1_0 | 1,612 | 3,002 | 77,776,570.91 | 22,784 | cold |
| Python — host CPython 3 | — | — | 3,038 | 768,456.59 | — | cold |
| Python — gpy-16 GrokVM | — | — | 3,076 | 758,933.40 | — | cold |

## bench-all profile suite (field-nexus-bench)

| Profile | compile_ms | run_ms | binary_bytes | kernel |
|---------|------------|--------|--------------|--------|
| ai | 735 | 6 | 18232 | grok16_bench profile=ai std=gnu++26 __cplusplus=202400 n=64 iters=48 wall_ms=4.01076 checksum=141090 |
| field_compute | 543 | 3 | 16240 | field_canvas_kernel entropy_micro=500026 phi_micro=618000 wave_speed_micro=1420000 FIELD_X86_DIE=1 |
| vulkan_rtx | 876 | 4 | 22728 | grok16_field_bench profile=default std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 wall_ms=2.13762 nexus_checksum=-nan |
| ai_agent | 662 | 7 | 16672 | grok16_bench profile=ai std=gnu++26 __cplusplus=202400 n=64 iters=48 wall_ms=4.13678 checksum=141090 |
| expert | 2275 | 14 | 21200 | grok16_field_bench profile=field_opt std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 wall_ms=3.30415 nexus_checksum=-nan |
| heavy | 1667 | 8 | 22840 | grok16_field_bench profile=field_opt std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 wall_ms=2.79452 nexus_checksum=-nan |
| field_opt | 1871 | 8 | 22712 | grok16_field_bench profile=field_opt std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 die_slots=256 belt_chunk=1 redata_chunk=512 wall_ms=2.76844 nexus_checksum=-nan |
| belt_1_0 | 1690 | 8 | 22712 | grok16_field_bench profile=belt_1_0 std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 die_slots=256 belt_chunk=1 redata_chunk=512 wall_ms=2.78679 nexus_checksum=-nan |
| belt_2_0 | 2235 | 12 | 22840 | grok16_field_bench profile=belt_2_0 std=gnu++26 __cplusplus=202400 frames=240 prog_ops=512 die_slots=512 belt_chunk=64 redata_chunk=8192 wall_ms=4.34173 nexus_checksum=-nan |

## Winners by category

- **C:** C — host gcc -O2 — 80,589,704.68 ops/s
- **CXX:** C++ — g16 sense expert — 82,036,773.98 ops/s
- **CMAKE:** CMake — host g++ -O2 — 84,432,656.03 ops/s
- **PYTHON:** Python — host CPython 3 — 768,456.59 ops/s
- **Best first-run amortized** (exec ÷ (1 + compile_sec)): C — g16 belt_1_0 — 58,497,869.97 effective ops/s

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

