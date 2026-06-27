# Uncompiled Execution

Web: [uncompiled.html](https://zacharygeurts.github.io/Grok16/uncompiled.html)

**Grok16 3.0** — dev runs at normal speed; compile is chamber-organized and **ahead**, not on every click.

## Doctrine

`data/field-exec-uncompiled-doctrine.json`

| Lane | Dev behavior | Speed (speed_demo @ 3s) |
|------|--------------|---------------------------|
| **Python** | True interpreter (`pythong` / CPython / gpy-16) | ~0.72–0.76M ops/s |
| **C / C++** | No line-by-line interpreter — chamber **compile ahead** | ~80–88M ops/s after plane cache |
| **CMake** | Configure + build once; bin reused | ~85.7M ops/s |

## Queen .launch chamber

1. **Folder mirror** — compartment code in `.launch` chamber  
2. **Trim excess** — strip README, lockfiles, build cruft on singular plane  
3. **Pick runner** — Python entry stays interpreted; native sibling wave-converts  
4. **Cache** — fingerprinted `launch-singular-plane/<hash>/plane-<stem>`  
5. **Run like a bin** — execution timed; convert_ms excluded after cache hit  

Module: `Queen/lib/queen-launch-singular-field.py`

## Not compiling C/C++

There is no C/C++ REPL. **Chamber organization** presents a bin-like run:

- Reuse staged binary from `data/bench/exec-plane/` (~0.2 ms copy)  
- Or compile once into plane cache (434 ms – 2.7 s first run)  
- Operator uses **Compile mode** only for release-day wave convert  

## Commands

```bash
# Uncompiled Python via chamber
QUEEN_LAUNCH_SINGULAR_FIELD=0 python3 Queen/lib/queen-launch-chamber.py run examples/speed-demo/speed-demo.launch

# Singular plane (compile ahead + cache)
python3 Queen/lib/queen-launch-singular-field.py run examples/speed-demo/
```

See [Speed Bench](Speed-Bench) for versioned compile + exec numbers.