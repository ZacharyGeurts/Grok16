#!/usr/bin/env pythong
"""Rebuild Grok16 GitHub Pages manual (docs/) for distro 1.0.0."""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
DISTRO = "1.0.0"
G16 = "16.1.1"
CACHE = "v8"

NAV = [
    ("index.html", "Home"),
    ("release.html", "Release 1.0"),
    ("getting-started.html", "Getting Started"),
    ("architecture.html", "Architecture"),
    ("batteries.html", "Batteries"),
    ("toolkits.html", "Toolkits"),
    ("linker.html", "Linker"),
    ("profiles.html", "Profiles"),
    ("performance.html", "Performance"),
    ("integration.html", "Integration"),
    ("concepts.html", "Concepts"),
    ("master-coder.html", "Master Coder"),
    ("field-primer.html", "Field Primer"),
    ("reference.html", "Reference"),
]


def head(title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>Grok16 — {title}</title>
  <meta name="description" content="Grok16 {DISTRO} programmer manual — unified g16 @ {G16}, batteries, linker, profiles." />
  <link rel="canonical" href="https://zacharygeurts.github.io/Grok16/{title.lower().replace(' ', '-')}.html" />
  <script>
  (function (d) {{
    try {{
      var t = localStorage.getItem("g16-theme");
      if (t !== "dark" && t !== "light") {{
        t = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
      }}
      d.documentElement.setAttribute("data-theme", t);
    }} catch (e) {{
      d.documentElement.setAttribute("data-theme", "dark");
    }}
  }})(document);
  </script>
  <script src="manual-theme.js?{CACHE}"></script>
  <script src="manual-search.js?{CACHE}"></script>
  <script src="manual-layout.js?{CACHE}"></script>
  <link rel="stylesheet" href="manual.css?{CACHE}" />
</head>
<body>
"""


def nav() -> str:
    links = "\n".join(f'      <a href="{href}">{label}</a>' for href, label in NAV)
    return f"""  <nav>
    <div class="nav-top">
      <div class="nav-brand">
        <strong>Grok16</strong>
        <span class="nav-version">distro {DISTRO}</span>
        <span class="nav-g16">g16 @ {G16}</span>
      </div>
      <div class="nav-controls" aria-label="Display preferences">
        <div class="control-chip">
          <label class="control-label" for="g16-font-scale">Size</label>
          <select id="g16-font-scale" class="g16-select" aria-label="Font size">
            <option value="0.875">S</option>
            <option value="1" selected>M</option>
            <option value="1.125">L</option>
            <option value="1.25">XL</option>
          </select>
        </div>
        <div class="theme-switch" role="group" aria-label="Color theme">
          <button type="button" class="g16-seg" id="g16-theme-light" data-theme="light" aria-pressed="false">Light</button>
          <button type="button" class="g16-seg" id="g16-theme-dark" data-theme="dark" aria-pressed="false">Dark</button>
        </div>
      </div>
    </div>
    <div class="nav-links">
{links}
    </div>
  </nav>
"""


def foot() -> str:
    return f"""  <footer>
    <a href="index.html">Home</a> ·
    <a href="release.html">Release {DISTRO}</a> ·
    <a href="https://github.com/ZacharyGeurts/Grok16">GitHub</a> ·
    <a href="https://github.com/ZacharyGeurts/Grok16/wiki">Wiki</a>
    <p class="footer-meta">Grok16 {DISTRO} · g16 @ {G16} · GPLv3</p>
  </footer>
</body>
</html>
"""


def page(title: str, body: str) -> str:
    return head(title) + nav() + body + foot()


PAGES: dict[str, tuple[str, str]] = {
    "index.html": (
        "Home",
        """
  <div class="hero hero-image">
    <img src="assets/g16-hero-banner.png" alt="" class="hero-bg" width="1200" height="675" />
    <div class="hero-overlay">
      <p class="hero-badge">Stable release {DISTRO}</p>
      <h1>Grok16 Field Compiler</h1>
      <p class="lead">Self-hosted <code>g16</code> @ <strong>{G16}</strong> — unified driver, <code>gnu++26</code> / <code>gnu17</code>, batteries through release gate.</p>
      <p class="hero-cta">Press <kbd>Ctrl</kbd>+<kbd>K</kbd> to search commands, batteries, profiles, env vars.</p>
    </div>
  </div>

  <h2>Engineer workflow</h2>
  <div class="workflow">
    <a href="getting-started.html#bootstrap"><strong>1 clone</strong>v{DISTRO} tag</a>
    <a href="getting-started.html#rebuild"><strong>2 rebuild</strong>self-host g16</a>
    <a href="batteries.html#release"><strong>3 gate</strong>test-battery-release</a>
    <a href="performance.html#field-bench"><strong>4 bench</strong>field_opt metrics</a>
    <a href="integration.html#gates"><strong>5 integrate</strong>Queen / WRDT</a>
  </div>

  <div class="figure-row">
    <figure class="fig-card">
      <img src="assets/g16-arch-visual.png" alt="Grok16 architecture layers" width="640" height="360" loading="lazy" />
      <figcaption>Forge → GCC self-host → unified <code>g16</code> with in-tree toolkits</figcaption>
    </figure>
    <figure class="fig-card">
      <img src="assets/battery-gate.svg" alt="Battery validation tiers" width="920" height="200" loading="lazy" />
      <figcaption>Smoke → expert → heavy → <code>test-battery-release</code></figcaption>
    </figure>
  </div>

  <h2>Manuals</h2>
  <table>
    <tr><th>Doc</th><th>For engineers who need…</th></tr>
    <tr><td><a href="release.html">Release 1.0</a></td><td>What shipped, upgrade path from v0.9c</td></tr>
    <tr><td><a href="getting-started.html">Getting Started</a></td><td>Bootstrap, rebuild modes, first verify</td></tr>
    <tr><td><a href="architecture.html">Architecture</a></td><td>Forge pipeline, unified driver, directories</td></tr>
    <tr><td><a href="batteries.html">Batteries</a></td><td>Validation tiers, CI gate, failure triage</td></tr>
    <tr><td><a href="toolkits.html">Toolkits</a></td><td>gpy-16, binutils, language drivers in-tree</td></tr>
    <tr><td><a href="linker.html">Linker</a></td><td>g16-ld, 16 targets, mandate flags</td></tr>
    <tr><td><a href="profiles.html">Profiles</a></td><td>field_opt, expert, heavy, RTX gate</td></tr>
    <tr><td><a href="performance.html">Performance</a></td><td>Bench matrix, LTO/PGO, release rebuild</td></tr>
    <tr><td><a href="reference.html">Reference</a></td><td>Commands, env vars, manifest paths</td></tr>
    <tr><td><a href="master-coder.html">Master Coder</a></td><td>Indexed hub — every command and hook</td></tr>
  </table>
""".format(DISTRO=DISTRO, G16=G16),
    ),
    "release.html": (
        "Release 1.0",
        """
  <h1>Release {DISTRO}</h1>
  <p>First <strong>stable</strong> Grok16 distro. Compiler lineage <strong>{G16}</strong>. Tag <code>v{DISTRO}</code>. Previous tagged point: <code>v0.9c</code>.</p>

  <h2 id="checkout">Checkout</h2>
  <pre><code>git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16
git checkout v{DISTRO}
export G16_PREFIX="$(pwd)"
export G16_RELEASE_PROFILE=1
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh test-battery-release</code></pre>

  <h2 id="shipped">What shipped</h2>
  <ul>
    <li>Unified <code>g16</code> — C, C++, Python/GPY-16, ASM, Rust, Go, Zig, Fortran, D, Ada, ObjC</li>
    <li>In-tree toolkits — <code>data/grok16-toolkits.json</code>, binutils field tools</li>
    <li>G16 field linker — 16 silicon targets, Ironclad witness, mandate hardening</li>
    <li><code>test-battery-release</code> — production gate (heavy + py + forever + binutils + verify)</li>
    <li>Linker fix — no <code>-pie</code> on <code>-shared</code> links (prevents <code>libgcc_s.so.1</code> corruption)</li>
    <li>Profile/LTO/PGO — <code>-flto=thin</code> normalize, conditional PGO, expert/heavy flags</li>
  </ul>

  <h2 id="upgrade">Upgrade from v0.9c</h2>
  <ol>
    <li>Checkout <code>v{DISTRO}</code></li>
    <li><code>G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild</code></li>
    <li>Run <code>test-battery-release</code> before pointing consumers at prefix</li>
  </ol>
  <p>Full notes: <a href="https://github.com/ZacharyGeurts/Grok16/blob/main/RELEASE-1.0.md">RELEASE-1.0.md</a></p>
""".format(DISTRO=DISTRO, G16=G16),
    ),
    "getting-started.html": (
        "Getting Started",
        """
  <h1>Getting Started</h1>
  <p>Grok16 <strong>{DISTRO}</strong> ships a unified <code>g16</code> driver. One binary compiles C and C++; backends live in <code>libexec/grok16/</code>. <code>g++16</code> is a compat symlink.</p>

  <h2>Requirements</h2>
  <ul>
    <li>Linux x86_64</li>
    <li>Host <code>gcc</code>/<code>g++</code>, <code>git</code>, <code>cmake</code>, Python 3 / GPY-16</li>
    <li>GCC build deps (gmp, mpfr, mpc, flex, bison)</li>
    <li>~6 GB disk for <code>vendor/</code>, <code>build/</code>, prefix</li>
  </ul>

  <h2 id="bootstrap">Bootstrap</h2>
  <pre><code>git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16
git checkout v{DISTRO}
export G16_PREFIX="$(pwd)"

./scripts/grok16-toolchain.sh bootstrap
./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh verify</code></pre>

  <h2 id="rebuild">Rebuild modes</h2>
  <table>
    <tr><th>Mode</th><th>Env</th><th>Use when</th></tr>
    <tr><td>Fast (default)</td><td><code>G16_FAST_REBUILD=1</code></td><td>Day-to-day iteration</td></tr>
    <tr><td>Full</td><td><code>G16_FULL_REBUILD=1</code></td><td>distclean + 3-stage bootstrap</td></tr>
    <tr><td>Release</td><td><code>G16_RELEASE_PROFILE=1</code></td><td>Production prefix — LTO + PGO + field_opt</td></tr>
  </table>
  <pre><code>./scripts/grok16-toolchain.sh rebuild
G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild</code></pre>

  <h2 id="verify">Verify &amp; gate</h2>
  <pre><code>./scripts/grok16-toolchain.sh verify
./scripts/grok16-toolchain.sh test-battery-expert
./scripts/grok16-toolchain.sh test-battery-release</code></pre>
  <p>See <a href="batteries.html">Batteries</a> for tier breakdown.</p>

  <h2 id="bench">Benchmarks</h2>
  <pre><code>./scripts/grok16-toolchain.sh field-bench
./scripts/grok16-toolchain.sh bench-all
./scripts/grok16-toolchain.sh profile</code></pre>
""".format(DISTRO=DISTRO, G16=G16),
    ),
    "architecture.html": (
        "Architecture",
        """
  <h1>Architecture</h1>
  <figure class="fig-wide">
    <img src="assets/g16-arch-visual.png" alt="Grok16 layer architecture" width="960" height="540" loading="lazy" />
  </figure>

  <h2 id="forge-flow">Forge pipeline</h2>
  <pre><code>forge/grok16-forge.py run gcc_fetch
forge/grok16-forge.py run gcc_configure   # host gcc
forge/grok16-forge.py run gcc_build
forge/grok16-forge.py run gcc_rebuild     # self-host with g16</code></pre>

  <h2 id="unified-driver">Unified driver</h2>
  <table>
    <tr><th>Artifact</th><th>Path</th><th>Role</th></tr>
    <tr><td><code>g16</code></td><td><code>bin/g16</code></td><td>Discern C/C++/Python/ASM + delegate</td></tr>
    <tr><td><code>g16-cc</code></td><td><code>libexec/grok16/g16-cc</code></td><td>C backend (gnu17)</td></tr>
    <tr><td><code>g16-cxx</code></td><td><code>libexec/grok16/g16-cxx</code></td><td>C++ backend (gnu++26)</td></tr>
    <tr><td><code>g16-ld</code></td><td><code>bin/g16-ld</code></td><td>Field linker wrapper → <code>forge/g16-linker.py</code></td></tr>
  </table>

  <h2 id="directories">Directory layout</h2>
  <table>
    <tr><th>Path</th><th>Contents</th></tr>
    <tr><td><code>vendor/gcc</code></td><td>Upstream gcc-15, BASE-VER {G16}</td></tr>
    <tr><td><code>build/gcc</code></td><td>Object files, stage builds</td></tr>
    <tr><td><code>bin/</code></td><td>Installed tools (gitignored until bootstrap)</td></tr>
    <tr><td><code>forge/</code></td><td>Python forge — fetch, build, linker, ironclad</td></tr>
    <tr><td><code>data/</code></td><td>Profiles, doctrines, manifests, bench JSON</td></tr>
  </table>

  <h2 id="selfhost">Self-host stamp</h2>
  <p>Successful rebuild writes <code>SELFHOST.json</code> at repo root with compiler version and timestamp.</p>
""".format(G16=G16),
    ),
    "batteries.html": (
        "Batteries",
        """
  <h1>Battery validation</h1>
  <p>Grok16 {DISTRO} gates releases through layered batteries. Run locally before tagging or deploying a prefix.</p>

  <figure class="fig-wide">
    <img src="assets/battery-gate.svg" alt="Battery tier diagram" width="920" height="200" />
  </figure>

  <h2 id="smoke">Smoke — <code>test-battery</code></h2>
  <pre><code>./scripts/grok16-toolchain.sh test-battery</code></pre>
  <p>paths · discern · status · verify · manifest · ironclad sanity · hostess gate</p>

  <h2 id="expert">Expert — <code>test-battery-expert</code></h2>
  <pre><code>./scripts/grok16-toolchain.sh test-battery-expert</code></pre>
  <p>Smoke + ironclad verify + linker verify + RTX gate + <code>expert</code> profile compile</p>

  <h2 id="heavy">Heavy — <code>test-battery-heavy</code></h2>
  <pre><code>G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh test-battery-heavy</code></pre>
  <p>Expert chain + <code>profile=heavy</code> bench + field-bench under release profile</p>

  <h2 id="release">Release — <code>test-battery-release</code></h2>
  <pre><code>G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh test-battery-release</code></pre>
  <table>
    <tr><th>Step</th><th>What it proves</th></tr>
    <tr><td>heavy</td><td>Release-profile compile + bench</td></tr>
    <tr><td>py-battery</td><td><code>tests/test_g16_battery.py</code></td></tr>
    <tr><td>forever-battery</td><td>Hostess7 forever profile contract</td></tr>
    <tr><td>binutils-battery</td><td>g16-as / g16-ld / g16-objdump</td></tr>
    <tr><td>verify</td><td>Full verify incl. linker link smoke</td></tr>
  </table>

  <h2 id="triage">Failure triage</h2>
  <ul>
    <li><strong>Linker / libgcc_s</strong> — ensure <code>file lib64/libgcc_s.so.1</code> shows <em>shared object</em>, not PIE executable</li>
    <li><strong>LTO</strong> — profile flags normalize <code>-flto=thin</code> per compiler capability</li>
    <li><strong>PGO</strong> — use flags only when <code>data/pgo/*.gcda</code> exist</li>
    <li><strong>g16-ld missing</strong> — <code>./scripts/grok16-binutils.sh install</code></li>
  </ul>
""".format(DISTRO=DISTRO),
    ),
    "toolkits.html": (
        "Toolkits",
        """
  <h1>In-tree toolkits</h1>
  <p>Grok16 {DISTRO} carries rebuilt toolkits in-tree. Manifest: <code>data/grok16-toolkits.json</code>. No sibling-repo bootstrap required for core languages.</p>

  <h2 id="gpy16">GPY-16 (built-in)</h2>
  <table>
    <tr><th>Item</th><th>Path</th></tr>
    <tr><td>Tree</td><td><code>python/</code> — GrokVM</td></tr>
    <tr><td>Driver</td><td><code>bin/gpy-16</code> (from <code>scripts/gpy-16</code>)</td></tr>
    <tr><td>Discern</td><td><code>g16 foo.py</code> auto-routes to GPY-16</td></tr>
  </table>

  <h2 id="binutils">Field binutils</h2>
  <pre><code>./scripts/grok16-binutils.sh bootstrap
./scripts/grok16-binutils.sh install
./scripts/grok16-binutils.sh verify</code></pre>
  <p>Tools: <code>g16-as</code>, <code>g16-ld</code>, <code>g16-objdump</code>, <code>g16-ar</code>, <code>g16-nm</code>, …</p>

  <h2 id="languages">Language drivers</h2>
  <p>Install language wrappers to prefix:</p>
  <pre><code>./scripts/grok16-languages.sh install
./scripts/grok16-languages.sh discern
./scripts/grok16-languages.sh hostess-gate</code></pre>
  <p>Rust/Go/Zig/Fortran/D/Ada/ObjC drivers link through <code>g16-ld</code> where applicable.</p>
""".format(DISTRO=DISTRO),
    ),
    "linker.html": (
        "Linker",
        """
  <h1>G16 field linker</h1>
  <p><code>g16-ld</code> is a bash wrapper around <code>forge/g16-linker.py</code>. BFD backend: <code>libexec/grok16/g16-ld-bfd</code>. Doctrine: <code>data/g16-linker-doctrine.json</code> — 16 active targets.</p>

  <figure class="fig-wide">
    <img src="assets/linker-flow.svg" alt="Linker pass flow" width="880" height="220" />
  </figure>

  <h2 id="verify">Verify</h2>
  <pre><code>./scripts/grok16-toolchain.sh verify   # includes linker smoke
pythong forge/g16-linker.py targets
pythong forge/g16-linker.py json</code></pre>

  <h2 id="mandate">ELF mandate flags</h2>
  <table>
    <tr><th>Link kind</th><th>Injected flags</th></tr>
    <tr><td>Executable</td><td><code>-pie -zrelro -znow -znoexecstack</code></td></tr>
    <tr><td><code>-shared</code></td><td><code>-zrelro -znow -znoexecstack</code> — <strong>no -pie</strong> (1.0)</td></tr>
    <tr><td><code>-r</code> / <code>-static</code></td><td>none</td></tr>
  </table>

  <h2 id="targets">Target families</h2>
  <p>linux-gnu (x86_64, aarch64, arm, riscv), android (NDK), darwin/ios (mach-o), win32 (PE), bare-elf.</p>
  <p>Env overrides: <code>G16_LINK_TARGET</code>, <code>ANDROID_NDK_ROOT</code>, <code>G16_CROSS_PREFIX</code>.</p>
""",
    ),
}

SEARCH_INDEX = [
    {"t": "test-battery-release", "p": "batteries.html#release", "g": "Battery", "d": "1.0 production gate — heavy py forever binutils verify"},
    {"t": "test-battery-expert", "p": "batteries.html#expert", "g": "Battery", "d": "Ironclad linker RTX expert profile"},
    {"t": "test-battery-heavy", "p": "batteries.html#heavy", "g": "Battery", "d": "Release profile heavy bench gate"},
    {"t": "g16-ld", "p": "linker.html", "g": "Linker", "d": "Field linker 16 targets mandate flags"},
    {"t": "libgcc_s", "p": "batteries.html#triage", "g": "Linker", "d": "Shared lib corruption triage -pie on -shared"},
    {"t": "GPY-16", "p": "toolkits.html#gpy16", "g": "Toolkit", "d": "Built-in Python GrokVM gpy-16"},
    {"t": "v1.0.0", "p": "release.html", "g": "Release", "d": "Stable distro tag checkout rebuild gate"},
    {"t": "bootstrap", "p": "getting-started.html#bootstrap", "g": "Workflow", "d": "First GCC fetch host build install"},
    {"t": "rebuild", "p": "getting-started.html#rebuild", "g": "Workflow", "d": "Self-host fast full release modes"},
    {"t": "g16 unified", "p": "architecture.html#unified-driver", "g": "Driver", "d": "Single g16 C C++ Python discern"},
    {"t": "field_opt", "p": "profiles.html#field-opt", "g": "Profile", "d": "Primary Field throughput entropy NEXUS"},
    {"t": "G16_RELEASE_PROFILE", "p": "getting-started.html#rebuild", "g": "Env", "d": "LTO PGO field_opt production rebuild"},
    {"t": "gnu++26", "p": "field-primer.html#standard", "g": "C++", "d": "Default C++ standard"},
    {"t": "forge gcc_rebuild", "p": "architecture.html#forge-flow", "g": "Forge", "d": "Self-host GCC with g16 backends"},
]


def write_pages() -> None:
    for name, (title, body) in PAGES.items():
        (ROOT / name).write_text(page(title, body), encoding="utf-8")
        print(f"wrote {name}")


def write_search() -> None:
    (ROOT / "search-index.json").write_text(
        json.dumps(SEARCH_INDEX, indent=2) + "\n", encoding="utf-8"
    )
    print("wrote search-index.json")


def patch_legacy_pages() -> None:
    """Bump cache version and nav on hand-maintained pages."""
    legacy = [
        "profiles.html", "performance.html", "integration.html",
        "field-primer.html", "reference.html", "concepts.html", "io.html",
        "master-coder.html", "master-coder-c.html", "master-coder-cxx.html",
    ]
    old_nav_marker = '<a href="index.html">Index</a>'
    new_links = "\n".join(
        f'      <a href="{h}">{l}</a>' for h, l in NAV if h != "index.html"
    )
    new_nav_block = f"""    <div class="nav-links">
      <a href="index.html">Home</a>
{new_links}
    </div>"""
    for fname in legacy:
        path = ROOT / fname
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        text = text.replace("manual.css?v=7", f"manual.css?{CACHE}")
        text = text.replace("manual-theme.js?v=7", f"manual-theme.js?{CACHE}")
        text = text.replace("manual-search.js?v=7", f"manual-search.js?{CACHE}")
        text = text.replace("manual-layout.js?v=7", f"manual-layout.js?{CACHE}")
        text = text.replace('<span class="nav-version">v16.1.1</span>',
                            f'<span class="nav-version">distro {DISTRO}</span><span class="nav-g16">g16 @ {G16}</span>')
        text = text.replace("<strong>Grok16 Manual</strong>", "<strong>Grok16</strong>")
        if '<div class="nav-links">' in text:
            import re
            text = re.sub(
                r'<div class="nav-links">.*?</div>',
                new_nav_block,
                text,
                count=1,
                flags=re.DOTALL,
            )
        path.write_text(text, encoding="utf-8")
        print(f"patched {fname}")


def main() -> int:
    write_pages()
    write_search()
    patch_legacy_pages()
    gen = ROOT / "gen-master-pages.py"
    if gen.is_file():
        subprocess.run([sys.executable, str(gen)], check=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())