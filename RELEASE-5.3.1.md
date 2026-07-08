# Grok16 5.3.1

**Tag:** `v5.3.1` · **Repo:** [ZacharyGeurts/Grok16](https://github.com/ZacharyGeurts/Grok16)

Grok16 is its **own GitHub** — full compiler distro, forge, and 79+ language packs ship here, not inside Hostess7 archives.

## What changed

- Hostess7 2.0.7j drops H7e condenser packaging — plain `.tar.gz` / `.zip` only
- Hostess7 bundles **common runtime** (~400MB) + boot prompt; full tree clones from this repo
- Pairing manifest: `doctrine/grok16-github-pair.json` in Hostess7 platform packs

## Assets

| File | Purpose |
|------|---------|
| `grok16-5.3.1-src.tar.gz` | Full source + forge (bootstrap g16 on any platform) |
| `grok16-5.3.1-platforms.json` | 17 bootstrap platforms + hardware pairs |
| `grok16-5.3.1-PLATFORMS.md` | Human-readable matrix |
| `grok16-5.3.1-linux-x86_64.tar.gz` | Binary package when g16 is built locally |

## Quick start

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16
./scripts/grok16-toolchain.sh bootstrap
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-launch-verify.sh
```

Or extract release tarball:

```bash
tar xzf grok16-5.3.1-src.tar.gz && cd grok16-5.3.1-src
export G16_PREFIX=$(pwd)
./scripts/grok16-toolchain.sh bootstrap
```

## Hostess7 pair

- **Hostess7:** [ZacharyGeurts/Hostess7](https://github.com/ZacharyGeurts/Hostess7) `v2.0.7j`
- Boot: `./hostess7-boot` → 10s Y/N clones full Grok16 from GitHub
- Programmerland manual: https://zacharygeurts.github.io/AmmoCode/