# Credits

Grok16 is beta packaging and tooling around a self-hosted **G16** (`g16` / `g++16`)
field build. All software here is under the **GNU General Public License v3**
unless a file states otherwise.

## GNU Compiler Collection (GCC)

- **Project:** [GNU Compiler Collection](https://gcc.gnu.org/)
- **Source repository:** https://gcc.gnu.org/git/gcc.git
- **Branch used:** `releases/gcc-16`
- **Copyright:** Free Software Foundation, Inc. and GCC contributors
- **License:** GPLv3; runtime components may use the [GCC Runtime Library Exception](https://www.gnu.org/licenses/gcc-exception-3.1.html)

Grok16 does not replace or subsume GCC — it configures, self-hosts, and installs
a field build with `g16` / `g++16` program names and pkgversion `Grok16-16.0.0`.

## Free Software Foundation

Thank you to the **Free Software Foundation** for GCC, the GPL, and decades of
free software infrastructure.

## Grok16 maintainers

- **Zachary Geurts** — Grok16 scripts, toolchain layout, Queen forge integration (2026)

## Third-party tools (build-time)

Building GCC typically also uses **GMP**, **MPFR**, and **MPC** (their respective
GNU or LGPL licenses apply via the GCC prerequisite bundle). Queen forge handles
fetching prerequisites from the upstream GCC `contrib/download_prerequisites` flow.