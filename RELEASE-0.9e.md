# Grok16 0.9e (development — not released)

**Status:** Pre-release development on `main`. **No tag. No GitHub Release.**  
Compiler lineage **16.1.1** · last tagged distro **v0.9c**.

Roadmap: **0.9e → linker/battery gate hardening → expert + heavy → 1.0**

## What's on 0.9e (main)

- **Carry our own rebuilt toolkits** — `data/grok16-toolkits.json`
- **Built-in GPY-16** — `python/` GrokVM + `scripts/gpy-16` → `bin/gpy-16` on languages install
- **Unified `g16` discern** — C, C++, Python, ASM, Rust, Go, Zig, Fortran, D, Ada, ObjC
- G16 field linker, ironclad/sanity meld, RTX gate (from 0.9c)

## Still WIP before 1.0

- Linker BFD flag hardening (PIE / `-znoexecstack`)
- Heavy battery gate integrity (fail on real link errors)
- CI workflow (local draft; needs OAuth `workflow` scope to push)

## Validation

| Tier | Command |
|------|---------|
| Expert | `./scripts/grok16-toolchain.sh test-battery-expert` |
| Heavy | `./scripts/grok16-toolchain.sh test-battery-heavy` |
| Languages | `./scripts/grok16-languages.sh discern` |

## Checkout

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16
git checkout main   # 0.9e — no v0.9e tag yet
export G16_PREFIX="$(pwd)"
./scripts/grok16-languages.sh install
./scripts/grok16-toolchain.sh rebuild
```

For last **released** distro point, use tag **v0.9c**.