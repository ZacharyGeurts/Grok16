# Grok16 5.3.2 — Platform release · C64 Ultimate

**Tag:** `v5.3.2` · **Repo:** [ZacharyGeurts/Grok16](https://github.com/ZacharyGeurts/Grok16)  
**g16:** `16.2.0` · **Model:** source bootstrap per platform + hardware pairs

## Platforms (18 total)

| Class | Count | IDs |
|-------|------:|-----|
| **Bootstrap** | 17 | linux-gnu (x86_64, i386, aarch64, arm, riscv64), android (aarch64, arm, x86_64), darwin (x86_64, aarch64), ios-aarch64, win32 (x86_64, aarch64), bare-elf (x86_64, aarch64, riscv64) |
| **Hardware pair** | 1 | **`pair-c64-ultimate`** — Commodore 64 Ultimate / C64C Ultimate FPGA |

### Commodore 64 Ultimate

- **Pair ID:** `pair-c64-ultimate` — g16 runs on your **host** (Linux/macOS/Windows), not on classic MOS 6510
- **Hardware:** [Commodore 64 Ultimate](https://commodore.net/computer/) · Artix-7 FPGA · PRG/CRT/D64 media
- **Queen lane:** `c64_ultimate` game room · `pair/C64Ultimate` CHIPS
- **Classic C64:** separate Queen/catalog lane (`retro_c64`) — not a g16 bootstrap target
- **Manual:** [c64-ultimate.html](https://zacharygeurts.github.io/Grok16/c64-ultimate.html) · [Wiki C64-Ultimate](https://github.com/ZacharyGeurts/Grok16/wiki/C64-Ultimate)

## What changed in 5.3.2

- Full **platform matrix** JSON + PLATFORMS.md on every release
- **linux-x86_64 binary package** — g16 prefix + AmmoCode bundle + default settings
- **AmmoCode syntax editor** — [github.io/Grok16](https://zacharygeurts.github.io/Grok16/) with Hostess7 textbook flyout
- **79 languages** — registry unchanged; 58 explaining manuals on Dewey 000

## Assets

| File | Purpose |
|------|---------|
| `grok16-5.3.2-src.tar.gz` | Full source + forge |
| `grok16-5.3.2-platforms.json` | 17 bootstrap + C64 Ultimate pair |
| `grok16-5.3.2-PLATFORMS.md` | Human-readable matrix |
| `grok16-5.3.2-linux-x86_64-manifest.json` | Binary package manifest (on release) |
| `grok16-5.3.2-linux-x86_64.tar.gz` | Built locally (~2.7G) — exceeds GitHub 2GB asset cap; run `scripts/grok16-binary-package.sh 5.3.2` |

## Quick start

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16 && git checkout v5.3.2
export G16_PREFIX="$(pwd)" G16_BELT_PROFILE=belt_2_0 SG_ROOT=/path/to/SG
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh verify
```

Binary extract (linux x86_64):

```bash
tar xzf grok16-5.3.2-linux-x86_64.tar.gz
cd grok16-5.3.2-linux-x86_64 && source grok16-env.sh
./share/ammocode/ammocode
```

## Pairing

- **Hostess7:** plain tar.gz stacks · `doctrine/grok16-github-pair.json`
- **AmmoCode:** [github.io/AmmoCode](https://zacharygeurts.github.io/AmmoCode/) Programmerland manual
- **C64 Ultimate:** host compiles with g16; FPGA C64 runs media — see platform manifest `pair-c64-ultimate`