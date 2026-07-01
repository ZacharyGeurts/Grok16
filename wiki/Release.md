# Release 5.3.2 — Platforms + C64 Ultimate

Tag: `v5.3.2` · `distro_version: 5.3.2` · `g16` @ `16.2.0`

## Shipped in 5.3.2

| Area | Detail |
|------|--------|
| Platforms | **17 bootstrap** + **`pair-c64-ultimate`** (Commodore 64 Ultimate FPGA) |
| GitHub assets | src tarball, platforms JSON, PLATFORMS.md, binary manifest |
| Binary | Build locally — `grok16-5.3.2-linux-x86_64.tar.gz` (~2.7G, over GitHub 2GB cap) |
| Web | [AmmoCode editor](https://zacharygeurts.github.io/Grok16/) + [manual](https://zacharygeurts.github.io/Grok16/manual.html) |

---

# Release 5.3.1 — Programmerland · own GitHub

Tag: `v5.3.1` · `distro_version: 5.3.1` · `g16` @ `16.2.0`

## Shipped in 5.3.1

| Area | Detail |
|------|--------|
| GitHub | Full source tarball + platforms JSON — **Grok16 is its own repo** |
| Hostess7 pair | Plain `tar.gz`/`zip` stacks; `grok16-github-pair.json`; no H7e |
| AmmoCode Pages | [zacharygeurts.github.io/AmmoCode](https://zacharygeurts.github.io/AmmoCode/) — programmer manual |
| Wiki | [Programmerland](Programmerland) theme |
| Languages | **79** in `grok16-languages.json` — unchanged |

## Boot (Hostess7 / NewLatest)

```bash
./hostess7-boot
# Common runtime bundled; 10s Y/N clones full Grok16 from GitHub
```

```bash
git clone https://github.com/ZacharyGeurts/Grok16.git
# → SG/Grok16 — full forge + 79 langs
```

## Assets

- `grok16-5.3.1-src.tar.gz`
- `grok16-5.3.1-platforms.json`
- `grok16-5.3.1-PLATFORMS.md`

Full notes: `RELEASE-5.3.1.md` in repo.