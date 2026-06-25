# Performance

Host: Linux x86_64, `g++16 (Grok16-16.0.0)`.

## field-nexus-bench

| Build | kernel wall_ms | bytes |
|-------|----------------|-------|
| -O2 baseline | 2.65 | 17144 |
| field_opt | 2.11–2.19 | 22616 |

~19% faster vs -O2 baseline.

## bench-all

| Profile | compile_ms | kernel |
|---------|------------|--------|
| field_opt | ~830–870 | ~2.1 ms |
| ai | ~735 | ~4.0 ms |
| field_compute | ~543 | dispatch OK |
| vulkan_rtx | ~870 | ~2.1 ms |

## Commands

```bash
./scripts/grok16-toolchain.sh field-bench
./scripts/grok16-toolchain.sh bench-all
cat data/bench/latest.json
```

## PGO

```bash
./scripts/grok16-toolchain.sh profile
G16_ENABLE_PGO=1 ./scripts/grok16-toolchain.sh field-bench
```