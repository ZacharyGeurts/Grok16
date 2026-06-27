# Grok16 comprehensive benchmark report

**Assembled:** 2026-06-27T14:31:48Z  
**Report:** 4.7.1  
**Runners:** 11 speed_demo executions  
**bench-all profiles:** 9  
**Pipeline wall:** 26055.04 ms  
**Self-monitor:** 4 runs · dropped 0 · timeouts 0  

## Pipeline

1. `bench-all` — field-nexus-bench across field_opt, belt_1_0, belt_2_0, ai, field_compute, vulkan_rtx
2. `field-exec-stage.py` — wave-convert once to exec plane
3. `field-exec-full-bench.py` — speed_demo @ 1s, all runners, plate meld cycle
4. `field-exec-compare.py` — staged execution only (compile excluded)

## Metrics (exec-full)

- Bench wall: **14517.31** ms · mean ops/s **60706863.49**
- Compile total: **0** ms · exec total: **11125.7** ms
- Dropped runners: **0** · timeouts: **0**

## Plate meld verdict

- Post-meld re-exec ratio: **0.9322**
- Sense profile `hostess_secure` vs belt_2_0 ops ratio: **1.0602**
- Meld helps profile ladder: **yes**

Full speed bench: [SPEED-BENCH-REPORT.md](SPEED-BENCH-REPORT.md) · JSON: [field-exec-full-bench.json](field-exec-full-bench.json)

