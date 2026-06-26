# Profiles

Web: [profiles.html](https://zacharygeurts.github.io/Grok16/profiles.html)

Manifest: `data/grok16-profiles.json`

## Build profiles

| Profile | Use |
|---------|-----|
| `field_opt` | Primary Field throughput |
| `ai` | NEXUS matrix scoring |
| `field_compute` | CANVAS wave dispatch |
| `vulkan_rtx` | RTX SIMD (requires RTX GPU) |
| `expert` | Battery expert tier |
| `heavy` | Battery heavy / 1.0 gate |
| `hostess_secure` | Hostess7 pair |
| `forever` | Forever battery contract |

## CMake

```bash
cmake -S examples/field-nexus-bench -B build \
  -DCMAKE_TOOLCHAIN_FILE=cmake/grok16-toolchain.cmake \
  -DCMAKE_PROJECT_INCLUDE=cmake/grok16-profile-field-opt.cmake
```

## Flag introspection

```bash
pythong scripts/grok16-profile-flags.py field_opt cxx
pythong scripts/grok16-profile-flags.py heavy source
```