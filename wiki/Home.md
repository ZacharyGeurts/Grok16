# Grok16 5.3 — Common runtime boot + AmmoCode pair

**Grok16 5.x is the sovereign Field compiler line.** **5.3.0** boots a **common runtime** (~400MB) in NewLatest/Hostess7 and offers an optional **10s Y/N** full GitHub clone for **79+** languages.

| | |
|---|---|
| **Distro** | `5.3.0` · tag `v5.3.0` |
| **Compiler** | `g16` @ `16.2.0` (`Grok16-5.3.0`) |
| **AmmoCode pair** | [AmmoCode 6.1](https://github.com/ZacharyGeurts/AmmoCode) · `g16-ammocode-field-doctrine.json` |
| **AmmoOS pair** | [AmmoOS 2.0 Stack](https://github.com/ZacharyGeurts/AmmoOS) |
| **C64 pair** | [C64 Ultimate](C64) — `pair-c64-ultimate` (host-only g16) |
| **Bootstrap** | 17 platforms — Linux, Android, Darwin, iOS, Windows, bare-ELF, RISC-V |
| **Agents** | [MCP stdio](MCP) |

## Read this first

> **DO NOT CREATE FIELD FILES.** Use the **[2D field platform](Field-Platform)** — placement on the plane *is* field at depth 0.

## What ships in 5.3.0

- **Common runtime boot** — `grok16-boot-prompt.sh` ensures gpy-16 before stack start
- **Full source on GitHub** — clone always includes forge + scripts; build `g16` locally
- **AmmoCode field instill** — flat field doctrine, defield when resting on a field
- **C64 Ultimate pair** — FPGA hardware from [commodore.net](https://commodore.net/computer/)

## Quick start

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16 && git checkout v5.3.0
export G16_PREFIX="$(pwd)" G16_BELT_PROFILE=belt_2_0 SG_ROOT=/path/to/SG
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-integrate.sh
```

## Links

- [Release 5.3](Release) · [Field Platform](Field-Platform) · [Speed Bench](Speed-Bench)
- **Web manual:** https://zacharygeurts.github.io/Grok16/