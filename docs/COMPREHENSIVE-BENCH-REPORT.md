# Grok16 comprehensive benchmark report

**Assembled:** 2026-06-27T03:12:38Z  
**Report:** 3.1.0  
**Runners:** 11 speed_demo executions  
**bench-all profiles:** 9  

## Pipeline

1. `bench-all` — field-nexus-bench across field_opt, belt_1_0, belt_2_0, ai, field_compute, vulkan_rtx
2. `field-exec-stage.py` — wave-convert once to exec plane
3. `field-exec-full-bench.py` — speed_demo @ 3s, all runners, plate meld cycle
4. `field-exec-compare.py` — staged execution only (compile excluded)

## Plate meld verdict

- Post-meld re-exec ratio: **0.9901**
- Sense profile `expert` vs belt_2_0 ops ratio: **1.0002**
- Meld helps profile ladder: **yes**

Full speed bench: [SPEED-BENCH-REPORT.md](SPEED-BENCH-REPORT.md) · JSON: [field-exec-full-bench.json](field-exec-full-bench.json)

