# Grok16 patches (upstream GCC)

Patches apply to the GCC tree in `vendor/gcc` after `gcc_fetch`.

| Patch | Purpose |
|-------|---------|
| `gcc-base-ver-16.0.0.patch` | Field version `16.0.0` (`gcc/BASE-VER`) |

The forge also writes `BASE-VER` at configure time; this patch documents the
intended delta for reviewers and matches our self-host field build.

Upstream: https://gcc.gnu.org/git/gcc.git — branch `releases/gcc-16` (or nearest
available; forge may use `GROK16_GCC_BRANCH` to override).