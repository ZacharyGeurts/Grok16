# Release 5.1.0 — Stack Fabric

Tag: `v5.1.0` · `distro_version: 5.1.0` · `g16` @ `16.2.0`  
Pairs with: **[AmmoOS 2.0.0-beta3](https://github.com/ZacharyGeurts/AmmoOS)** — source on `main`; release tarballs and Pages manual pending

Prior 2.x–4.x tracks remain in git; **operator docs start at 5.0 = v1.0**. This release seals stack fabric and agent MCP.

## Shipped in 5.1.0

- **Stack fabric G1–G15** — `lib/g16-stack-fabric.py`, receipt chain, silent bench
- **MCP stdio** — `mcp/grok16_mcp_server.py` · doctrine `data/grok16-mcp.json` · [MCP wiki](MCP)
- **Profile autoload** — belt stamps through integrate without manual env drift
- **ZNetwork wire profile** — field egress/ingress for Hub + Hostess 7 wire
- **Truth gate** — thermal downgrade on failed Ironclad receipts
- **243-filetype run** — programming filetypes sync lane
- **SPIR-V-only RTX** — `vulkan_rtx` shader path hardening
- **G1ID meld** — linear sovereign time on plate cycles

## Carried from 5.0.1

- **`ammoos` profile** — `cmake/grok16-profile-ammoos.cmake`
- **Integration** — `integrate-ammoos`, `verify-ammoos-surfaces`, `grok16-ammoos-integrate.json`
- **Smoke chamber** — `examples/ammoos-smoke/`
- **Review doc** — `docs/AMMOOS-REVIEW-FOR-GROK-BUILD.md`

## Carried from 5.0.0

- **belt_2_0** single fabric default
- **field_physics** profile — thermal guard, no `-ffast-math`
- **Binary package** — g16 + AmmoCode + signed settings
- **2D field platform** doctrine — no field files
- **ZNetwork field wire** design — egress convert / ingress deconvert
- **Speed Bench v5** — live JSON + SVG charts
- **Compiler symlinks** — `gcc`→`g16` always-optimal path
- **build-essential fabric** — self-hosted make/cmake/ninja

## Validation gates

```bash
./scripts/grok16-toolchain.sh verify
./scripts/grok16-toolchain.sh integrate-ammoos
./scripts/grok16-toolchain.sh verify-ammoos-surfaces
./scripts/grok16-toolchain.sh test-battery-belt
./scripts/grok16-toolchain.sh bench-triad
```

## Binary package

```bash
./scripts/grok16-toolchain.sh binary-package
# → dist/grok16-5.1.0-linux-x86_64.tar.gz
```

## Known gaps

- Full `gcc_rebuild` bootstrap may fail libgomp stage-1 on some hosts
- AmmoOS beta3 tarballs and Pages manual not published yet
- HTTP tunnel queue in-memory (AmmoCode)

Full notes: `RELEASE-5.1.0.md` in repo.