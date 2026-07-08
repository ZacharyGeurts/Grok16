# Grok16 5.3.0 — Common runtime boot + AmmoCode pair

**Released:** 2026-07-01  
**Tag:** `v5.3.0` · **Compiler:** `g16` @ `16.2.0` (`Grok16-5.3.0`)

## Highlights

- **Common runtime at boot** — NewLatest / Hostess7 always provision `SG/Grok16-common` (~400MB gpy-16 + combinatorics) via `lib/grok16-boot-prompt.sh`
- **10s Y/N full clone** — interactive hosts may download **full Grok16 source** from GitHub for **79+** programming languages (~8GB + build)
- **GitHub = full source** — repo ships forge, scripts, and doctrine; `vendor/` and `bin/g16` built locally with `grok16-integrate.sh`
- **AmmoCode pair** — `g16-ammocode-field-doctrine.json` wires `SG/Grok16` ↔ `SG/NewLatest/AmmoCode`; `sg_paths.grok16_root()` resolves full or common tree

## Boot flow

```bash
# Runs on nexus boot, field-stack start, and world-node bootstrap
bash NewLatest/lib/grok16-boot-prompt.sh boot
# GROK16_BOOT_PROMPT=0  — skip Y/N (CI / headless VMs)
# GROK16_BOOT_PROMPT_SECS=10  — prompt timeout (default 10)
```

## Quick start (full tree)

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16 && git checkout v5.3.0
export G16_PREFIX="$(pwd)" G16_BELT_PROFILE=belt_2_0 SG_ROOT=/path/to/SG
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-integrate.sh
```

## AmmoCode

```bash
cd SG/NewLatest/AmmoCode && python3 ammocode.py --check
# grok16_root → SG/Grok16 or SG/Grok16-common
```

## Release

```bash
./scripts/grok16-release.sh 5.3.0 --push
```