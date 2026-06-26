# Batteries

Web: [batteries.html](https://zacharygeurts.github.io/Grok16/batteries.html)

Grok16 1.0 gates releases through layered batteries. Run locally before tagging or pointing consumers at your prefix.

## Tiers

| Tier | Command | Profile |
|------|---------|---------|
| Smoke | `test-battery` | default |
| Expert | `test-battery-expert` | `expert` + ironclad + linker + RTX |
| Heavy | `test-battery-heavy` | `heavy` + release bench |
| **Release** | `test-battery-release` | heavy + py + forever + binutils + verify |

## Release gate (1.0)

```bash
export G16_RELEASE_PROFILE=1
./scripts/grok16-toolchain.sh test-battery-release
```

Steps bundled:
- `test-battery-heavy`
- `tests/test_g16_battery.py`
- `tests/test_g16_forever_battery.py`
- `tests/g16-binutils-battery.sh`
- `verify` (linker smoke required)

## Triage

| Symptom | Check |
|---------|-------|
| `libgcc_s.so.1` link error | `file lib64/libgcc_s.so.1` → must be **shared object** |
| LTO failure | `grok16-profile-flags.py` thin LTO normalize |
| PGO warnings | Only use when `data/pgo/*.gcda` exist |
| Linker missing | `grok16-binutils.sh install` |