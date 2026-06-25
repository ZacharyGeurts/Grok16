# Profiles

Source: `data/grok16-profiles.json`. Default std: `gnu++26`.

| Profile | CMake | Bench | Use |
|---------|-------|-------|-----|
| field_opt | grok16-profile-field-opt.cmake | field-nexus-bench | FieldX86, entropy, NEXUS |
| ai | grok16-profile-ai.cmake | ai-matrix-bench | Matrix scoring |
| field_compute | grok16-profile-field.cmake | field-canvas-kernel | CANVAS dispatch |
| vulkan_rtx | grok16-profile-vulkan.cmake | field-nexus-bench | AVX2/FMA |

## CMake

```bash
cmake -S . -B build \
  -DCMAKE_TOOLCHAIN_FILE=$GROK16_ROOT/cmake/grok16-toolchain.cmake \
  -DCMAKE_PROJECT_INCLUDE=$GROK16_ROOT/cmake/grok16-profile-field-opt.cmake
```

## Bench

```bash
G16_BENCH_PROFILE=ai ./scripts/grok16-toolchain.sh bench
G16_FIELD_SPEED=1 ./scripts/grok16-toolchain.sh field-bench
```

## Mandate

Include `cmake/g16-field-mandate.cmake` on field targets (fortify, RELRO, PIE).