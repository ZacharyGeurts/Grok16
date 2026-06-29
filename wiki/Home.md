# Grok16 5.1 — Stack Fabric

**Grok16 5.x is the sovereign Field compiler line.** Operator docs treat **5.0 as v1.0** framing; **5.1.0** adds stack fabric G1–G15 and MCP stdio for agents.

| | |
|---|---|
| **Distro** | `5.1.0` · tag `v5.1.0` |
| **Compiler** | `g16` @ `16.2.0` (`Grok16-5.1.0`) |
| **AmmoOS pair** | [AmmoOS 2.0.0-beta3](https://github.com/ZacharyGeurts/AmmoOS) — source on `main`, building now |
| **Default belt** | `belt_2_0` — single fabric, 8192 redata chunk, 512 die slots |
| **Production safety** | `field_physics` — no `-ffast-math`, thermal guard |
| **Agents** | [MCP stdio](MCP) — `grok16_version`, toolchain, bench, RTX gate |

## Read this first

> **DO NOT CREATE FIELD FILES.** Standalone `.field`, depth-field, or subfield JSON heats neighboring fields on the fabric. Use the **[2D field platform](Field-Platform)** — placement on the plane *is* field at depth 0.

## What ships in 5.1.0

- **Stack fabric G1–G15** — sealed receipts, profile autoload, truth gate
- **MCP server** — custom stdio tools for Cursor/agents ([MCP](MCP))
- **ZNetwork wire profile** — Hub + Hostess 7 egress posture
- **g16 prefix** — self-hosted toolchain, `g16-ld`, CMake/Ninja fabric
- **AmmoOS 2.0 Stack** — `ammoos` profile, integrate + verify hooks ([Integration](Integration))
- **2D auto-field platform** — flat plane, no nested amplitude files
- **Benchmarks** — Speed Bench v5, belt triad, bench-all ([numbers](Speed-Bench))

## Quick start

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16 && git checkout v5.1.0
export G16_PREFIX="$(pwd)" G16_BELT_PROFILE=belt_2_0 SG_ROOT=/path/to/SG
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh verify
./scripts/grok16-toolchain.sh integrate-ammoos
```

Binary package (when built):

```bash
./scripts/grok16-toolchain.sh binary-package
tar xzf dist/grok16-5.1.0-linux-x86_64.tar.gz
cd grok16-5.1.0-linux-x86_64 && source grok16-env.sh
./share/ammocode/ammocode
```

## Manual

**Web:** [zacharygeurts.github.io/Grok16](https://zacharygeurts.github.io/Grok16/)

**Wiki:** you are here.