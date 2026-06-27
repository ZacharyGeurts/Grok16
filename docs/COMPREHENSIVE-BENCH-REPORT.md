# Grok16 comprehensive benchmark report

**Assembled:** 2026-06-27T03:14:37Z  
**Report:** 3.1.0  
**Runners:** 11 speed_demo executions  
**bench-all profiles:** 9  

## Pipeline

1. `bench-all` — field-nexus-bench across field_opt, belt_1_0, belt_2_0, ai, field_compute, vulkan_rtx
2. `field-exec-stage.py` — wave-convert once to exec plane
3. `field-exec-full-bench.py` — speed_demo @ 1s, all runners, plate meld cycle
4. `field-exec-compare.py` — staged execution only (compile excluded)

## Plate meld verdict

- Post-meld re-exec ratio: **0.9982**
- Sense profile `field_opt` vs belt_2_0 ops ratio: **0.995**
- Meld helps profile ladder: **yes**

Full speed bench: [SPEED-BENCH-REPORT.md](SPEED-BENCH-REPORT.md) · JSON: [field-exec-full-bench.json](field-exec-full-bench.json)

