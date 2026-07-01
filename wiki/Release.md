# Release 5.3.0 — Common runtime boot + AmmoCode pair

Tag: `v5.3.0` · `distro_version: 5.3.0` · `g16` @ `16.2.0`

## Shipped in 5.3.0

| Area | Detail |
|------|--------|
| Boot | `NewLatest/lib/grok16-boot-prompt.sh` — common runtime always; 10s Y/N for full clone |
| GitHub | Full source (forge, scripts, doctrine); vendor/bin built on host |
| AmmoCode | `g16-ammocode-field-doctrine.json` — `SG/Grok16` ↔ `SG/NewLatest/AmmoCode` |
| Hostess7 | Embeds common runtime only (~400MB); full tree optional at boot |
| Languages | 79+ in `grok16-languages.json` (full tree) |

## Boot prompt

```bash
bash NewLatest/lib/grok16-boot-prompt.sh boot
# GROK16_BOOT_PROMPT=0     — headless / CI
# GROK16_BOOT_PROMPT_SECS=10
```

## Previous 5.2.0

- C64 Ultimate hardware pair · 17 bootstrap platforms · AmmoLang ship timing

Full notes: `RELEASE-5.3.0.md` in repo.