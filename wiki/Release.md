# Release 5.0.1 — AmmoOS incorporation

Tag: `v5.0.1` · `distro_version: 5.0.1` · `g16` @ `16.2.0`  
Pairs with: **[AmmoOS 1.9.9h — Grok Expert Review](https://github.com/ZacharyGeurts/AmmoOS/releases/tag/v1.9.9h)**

Prior 2.x–4.x tracks remain in git; **operator docs start at 5.0 = v1.0**. This patch closes the Grok Build incorporation loop for AmmoOS.

## Shipped in 5.0.1

- **`ammoos` profile** — `cmake/grok16-profile-ammoos.cmake`
- **Integration** — `integrate-ammoos`, `verify-ammoos-surfaces`, `grok16-ammoos-integrate.json`
- **Smoke chamber** — `examples/ammoos-smoke/`
- **Review doc** — `docs/AMMOOS-REVIEW-FOR-GROK-BUILD.md`
- **Wiki + Pages** — field platform, ZNetwork connect, integration refresh

## Carried from 5.0.0

- **belt_2_0** single fabric default
- **field_physics** profile — thermal guard, no `-ffast-math`
- **Binary package** — g16 + AmmoCode + signed settings
- **2D field platform** doctrine — no field files
- **ZNetwork field wire** design — egress convert / ingress deconvert
- **Speed Bench v5** — live JSON + SVG charts
- **AmmoCode field instill** — flat field, defield on rest
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
# → dist/grok16-5.0.1-linux-x86_64.tar.gz
```

## Known gaps

- Full `gcc_rebuild` bootstrap may fail libgomp stage-1 on some hosts
- ZNetwork **ACTIVE** behind review checklist
- HTTP tunnel queue in-memory (AmmoCode)

Full notes: `RELEASE-5.0.1.md` in repo.