# Integration

## World_Redata

```bash
cd World_Redata
./build-cpp.sh
PYTHONPATH=. pythong -m redata.cli parity
PYTHONPATH=. pythong -m redata.cli security
```

Uses `../Grok16/scripts/grok16-toolchain.sh` by default.

## Env

```bash
export G16_PREFIX=/path/to/Grok16
export WRDT_G16_PREFIX="$G16_PREFIX"
```

## Stack (L0–L5)

| Layer | Component |
|-------|-----------|
| L0–L1 | WRZC/WRDT/ZAC7 |
| L2 | C++ engine (Grok16) |
| L3 | Python redata |
| L4 | CLI, GUI |
| L5 | Grok16 |

## Queen

`./scripts/consolidate.sh` — symlink Queen vendor → Grok16.

## Manifest

`data/grok16-toolchain.json` at install. Python helper: `World_Redata/redata/grok16.py`.

## Sense package / OBS (orthogonal)

Grok16 and OBS-FieldVoiceFilter share field vocabulary but operate on different planes:

| Plane | Component | Security model |
|-------|-----------|----------------|
| **Compile-time (Grok16)** | `g16-field-mandate`, linker mandate, `redata.cli security` | Binary hardening — RELRO, PIE, fortify, World_Redata L2 gates |
| **Runtime (OBS)** | `field-security-posterity.c`, `field-repeat-field.c` | Streaming threat confirmation — posterity ring decides repeating hostile signatures |

- **No Grok16 code dependency** on OBS posterity or threat ledger.
- **NewLatest** bridges OBS via `lib/obs-threat-posterity-bridge.py` and `field-sense-package-meld.py` (see `NewLatest/data/field-sense-package-doctrine.json`).
- **Optional:** build `obs-field-voice-filter.so` with Grok16 toolchain + `g16-field-mandate.cmake` for hardened native plugin binaries — does not change posterity logic.
- Grok16 CI batteries (`test-battery-expert`, `test-battery-heavy`) validate the **toolchain**, not OBS runtime threats.