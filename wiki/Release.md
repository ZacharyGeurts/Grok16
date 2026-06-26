# Release 1.0.0

**Tag:** `v1.0.0` · **Compiler:** 16.1.1 · **Previous tag:** v0.9c

Web: [release.html](https://zacharygeurts.github.io/Grok16/release.html) · Repo: [RELEASE-1.0.md](https://github.com/ZacharyGeurts/Grok16/blob/main/RELEASE-1.0.md)

## Checkout & gate

```bash
git checkout v1.0.0
export G16_PREFIX="$(pwd)"
export G16_RELEASE_PROFILE=1
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh test-battery-release
```

## Highlights

- Unified `g16` — C, C++, Python, ASM, Rust, Go, Zig, Fortran, D, Ada, ObjC
- In-tree toolkits (`grok16-toolkits.json`, GPY-16, field binutils)
- G16 field linker — 16 targets, Ironclad witness
- `test-battery-release` — production validation gate
- Linker fix: no `-pie` on `-shared` (libgcc_s integrity)
- Profile/LTO/PGO hardening for expert + heavy tiers

## Upgrade from v0.9c

1. `git checkout v1.0.0`
2. Release-profile rebuild
3. `test-battery-release` must pass before consumer deploy