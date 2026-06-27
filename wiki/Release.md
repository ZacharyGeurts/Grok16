# Release 2.0.0

**Tag:** `v2.0.0` · **Compiler:** 16.2.0 · **Previous tag:** v1.0.0

Web: [release.html](https://zacharygeurts.github.io/Grok16/release.html) · Repo: [RELEASE-2.0.md](https://github.com/ZacharyGeurts/Grok16/blob/main/RELEASE-2.0.md)

## Single fabric

Grok16 2.0 centers on **single fabric knowing** — one belt die, one field amplitude, chunked dispatch without nested depth fields.

## Checkout & gates

```bash
git checkout v2.0.0
export G16_PREFIX="$(pwd)"
export G16_BELT_PROFILE=belt_2_0
G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh test-battery-release
./scripts/grok16-toolchain.sh test-battery-belt
./scripts/grok16-toolchain.sh bench-triad
./scripts/grok16-toolchain.sh integrate
```

## Highlights

- **Single fabric doctrine** — `data/grok16-single-fabric-doctrine.json`
- **Belt 2.0** — `belt_2_0` default; chunked redata 8192, wave-massive
- **Safety meld** — depth-field impossible, time linear, Ironclad field sanity
- **bench-triad** — host gcc vs belt_1_0 vs belt_2_0
- **grok16-integrate.sh** — auto-wire Queen, World_Redata, ZOCR, PythonG
- **test-battery-belt** — 2.0 gate atop release tier
- g16 @ **16.2.0** — compat with belt_1_0 / field_opt

## Upgrade from 1.0.0

1. `git checkout v2.0.0`
2. Set `G16_BELT_PROFILE=belt_2_0` and release-profile rebuild
3. `test-battery-release` + `test-battery-belt`
4. `./scripts/grok16-integrate.sh` before consumer deploy