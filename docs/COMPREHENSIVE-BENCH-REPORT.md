# Grok16 comprehensive benchmark report

**Assembled:** 2026-06-27T13:15:46Z  
**Report:** 4.2.0  
**Runners:** 11 speed_demo executions  
**bench-all profiles:** 9  
**Pipeline wall:** 74216.35 ms  
**Self-monitor:** 4 runs · dropped 0 · timeouts 0  

## Pipeline

1. `bench-all` — field-nexus-bench across field_opt, belt_1_0, belt_2_0, ai, field_compute, vulkan_rtx
2. `field-exec-stage.py` — wave-convert once to exec plane
3. `field-exec-full-bench.py` — speed_demo @ 3s, all runners, plate meld cycle
4. `field-exec-compare.py` — staged execution only (compile excluded)

## Metrics (exec-full)

- Bench wall: **33961.86** ms · mean ops/s **77632259.5**
- Compile total: **0** ms · exec total: **33103.8** ms
- Dropped runners: **0** · timeouts: **0**

## Plate meld verdict

- Post-meld re-exec ratio: **0.9611**
- Sense profile `field_opt` vs belt_2_0 ops ratio: **0.9526**
- Meld helps profile ladder: **yes**

Full speed bench: [SPEED-BENCH-REPORT.md](SPEED-BENCH-REPORT.md) · JSON: [field-exec-full-bench.json](field-exec-full-bench.json)

