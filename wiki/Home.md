# Grok16 5.0 — Version One

**Grok16 5.0 is a clean start.** Prior release numbering stays in git history; operator docs treat **5.0 as v1.0** — one sovereign Field compiler, one 2D platform, one belt.

| | |
|---|---|
| **Distro** | `5.0.1` · tag `v5.0.1` |
| **Compiler** | `g16` @ `16.2.0` (`Grok16-5.0.1`) |
| **AmmoOS pair** | [1.9.9e Grok Expert Review](https://github.com/ZacharyGeurts/AmmoOS/releases/tag/v1.9.9e) |
| **Default belt** | `belt_2_0` — single fabric, 8192 redata chunk, 512 die slots |
| **Production safety** | `field_physics` — no `-ffast-math`, thermal guard |
| **GUI** | AmmoCode in binary package · memory vault · ZNetwork attach |

## Read this first

> **DO NOT CREATE FIELD FILES.** Standalone `.field`, depth-field, or subfield JSON heats neighboring fields on the fabric. Use the **[2D field platform](Field-Platform)** — placement on the plane *is* field at depth 0.

## What ships in 5.0.1

- **g16 prefix** — self-hosted toolchain, `g16-ld`, CMake/Ninja fabric
- **AmmoOS incorporation** — `ammoos` profile, integrate + verify hooks ([Integration](Integration))
- **Binary package** — `grok16-5.0.1-linux-x86_64.tar.gz` + AmmoCode + signed defaults
- **2D auto-field platform** — flat plane, no nested amplitude files
- **ZNetwork field wire** — convert at egress, deconvert at ingress ([design](ZNetwork-Connect))
- **Benchmarks** — Speed Bench v5, belt triad, bench-all ([numbers](Speed-Bench))

## Quick start

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16 && git checkout v5.0.1
export G16_PREFIX="$(pwd)" G16_BELT_PROFILE=belt_2_0 SG_ROOT=/path/to/SG
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh verify
./scripts/grok16-toolchain.sh integrate-ammoos
```

Binary package (no build):

```bash
tar xzf grok16-5.0.1-linux-x86_64.tar.gz
cd grok16-5.0.1-linux-x86_64 && source grok16-env.sh
./share/ammocode/ammocode
```

## Manual

**Web:** [zacharygeurts.github.io/Grok16](https://zacharygeurts.github.io/Grok16/)

**Wiki:** you are here.