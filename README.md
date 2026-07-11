# Grok16 · 16.1.0-hard

**Sovereign Field compiler + native Field toolplane**

| Badge | Value |
|-------|-------|
| Field hard | **16.1.0-hard** |
| Editor pair | [AmmoCode 6.1](https://github.com/ZacharyGeurts/AmmoCode) |
| Stack | [Hostess7](https://github.com/ZacharyGeurts/Hostess7) · [AmmoOS](https://github.com/ZacharyGeurts/AmmoOS) |
| Pages | https://zacharygeurts.github.io/Grok16/ |

## Best version policy

| Surface | Use |
|---------|-----|
| **Compile / link / Field bins** | This tree · `16.1.0-hard` |
| **Editor UI (Pages)** | AmmoCode 6.1 |
| **Brain / ops hub** | Hostess 7 |

Hard plane: C++ Field binaries under `bin/` · no Python control plane for DNS/DHCP/elevate.

## Tools

```bash
# Compilers (wrappers)
./bin/g16   -c foo.c -o foo.o
./bin/g++16 -c foo.cpp -o foo.o

# Field plane (examples)
./bin/field-elevate autoelevate      # elevation · polkit HOSTILE
./bin/field-world-dns status
./bin/field-world-dhcp status
./bin/field-hostess7-stack-update pulse
./bin/field-ammolang                 # Python obsolete intercept
```

## Policy

| Surface | Policy |
|---------|--------|
| Exploits | **DISPERMITTED** |
| Soft-kill (SIGTERM) authoring | **FORBIDDEN** |
| Polkit | **HOSTILE** · field-elevate only |
| Elevation | `sudo -n field-elevate` allowlist |
| Link | RELRO · NOW · PIE · noexecstack |

Ironclad: `ironclad:g16-hard:2` · autoelevate: `ironclad:field-autoelevate-cpp:2`

## Layout

- `bin/` — g16/g++16 + Field C++ tools (elevate, DNS, DHCP, mesh, swallows, …)
- `lib/` · `forge/` · `cmake/` · `data/` — hard plane support
- Docs HTML on this branch for GitHub Pages manuals

## License

GPLv3 for G16 tooling surfaces · Field operational doctrine additional.

© 2025–2026 Zachary Robert Geurts
