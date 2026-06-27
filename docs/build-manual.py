#!/usr/bin/env pythong
"""Rebuild Grok16 GitHub Pages manual (docs/) for distro 2.0.0."""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
DISTRO = "2.0.0"
G16 = "16.2.0"
CACHE = "v9"

NAV = [
    ("index.html", "Home"),
    ("release.html", "Release 2.0"),
    ("single-fabric.html", "Single Fabric"),
    ("safety.html", "Safety"),
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
      <p class="hero-badge">Stable release {DISTRO} — single fabric</p>
      <h1>Grok16 Field Compiler</h1>
      <p class="lead">Self-hosted <code>g16</code> @ <strong>{G16}</strong> — <strong>single fabric</strong> belt (<code>belt_2_0</code>), Ironclad safety meld, unified driver, batteries through belt gate.</p>
      <p class="hero-cta">Press <kbd>Ctrl</kbd>+<kbd>K</kbd> to search commands, batteries, profiles, env vars.</p>
    </div>
  </div>

  <h2>Engineer workflow</h2>
  <div class="workflow">
    <a href="getting-started.html#bootstrap"><strong>1 clone</strong>v{DISTRO} tag</a>
    <a href="getting-started.html#rebuild"><strong>2 rebuild</strong>belt_2_0 + release</a>
    <a href="batteries.html#belt"><strong>3 gate</strong>release + belt battery</a>
    <a href="performance.html#triad"><strong>4 bench</strong>belt triad</a>
    <a href="integration.html#integrate"><strong>5 integrate</strong>Queen / WRDT + safety</a>
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
    <tr><td><a href="release.html">Release 2.0</a></td><td>Single fabric, safety meld, upgrade from v1.0.0</td></tr>
    <tr><td><a href="single-fabric.html">Single Fabric</a></td><td>2.0 technology — one belt die, one field amplitude</td></tr>
    <tr><td><a href="safety.html">Safety</a></td><td>Depth-field impossible, linear time, Ironclad gates</td></tr>
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
        "Release 2.0",
        """
  <h1>Release {DISTRO}</h1>
  <p>Grok16 <strong>2.0</strong> — <strong>single fabric</strong> belt dispatch. Compiler <strong>{G16}</strong>. Tag <code>v{DISTRO}</code>. Previous: <code>v1.0.0</code>.</p>

  <h2 id="checkout">Checkout</h2>
  <pre><code>git clone https://github.com/ZacharyGeurts/Grok16.git
cd Grok16
git checkout v{DISTRO}
export G16_PREFIX="$(pwd)"
export G16_BELT_PROFILE=belt_2_0
G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild
./scripts/grok16-toolchain.sh test-battery-release
./scripts/grok16-toolchain.sh test-battery-belt
./scripts/grok16-toolchain.sh bench-triad
./scripts/grok16-toolchain.sh integrate</code></pre>

  <h2 id="shipped">What shipped</h2>
  <ul>
    <li><strong>Single fabric</strong> — <code>belt_2_0</code> chunked redata (8192), wave-massive, single-location reads</li>
    <li><strong>Safety meld</strong> — depth fields sealed and destroyed; time is linear (<code>ironclad:time:1</code>)</li>
    <li><code>grok16-integrate.sh</code> — auto-wire Queen, World_Redata, ZOCR, PythonG</li>
    <li><code>test-battery-belt</code> — 2.0 validation atop release tier</li>
    <li><code>bench-triad</code> — host gcc vs <code>belt_1_0</code> vs <code>belt_2_0</code></li>
    <li>Unified <code>g16</code> @ {G16} — compat with 1.0 profiles (<code>belt_1_0</code> aliases <code>field_opt</code>)</li>
  </ul>

  <h2 id="upgrade">Upgrade from v1.0.0</h2>
  <ol>
    <li>Checkout <code>v{DISTRO}</code></li>
    <li><code>G16_BELT_PROFILE=belt_2_0 G16_RELEASE_PROFILE=1 ./scripts/grok16-toolchain.sh rebuild</code></li>
    <li><code>test-battery-release</code> then <code>test-battery-belt</code></li>
    <li><code>./scripts/grok16-integrate.sh</code> to publish env to SG consumers</li>
  </ol>
  <p>Full notes: <a href="https://github.com/ZacharyGeurts/Grok16/blob/main/RELEASE-2.0.md">RELEASE-2.0.md</a> · <a href="single-fabric.html">Single Fabric</a> · <a href="safety.html">Safety</a></p>
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
./scripts/grok16-toolchain.sh test-battery-release
./scripts/grok16-toolchain.sh test-battery-belt</code></pre>
  <p>See <a href="batteries.html">Batteries</a> for tier breakdown.</p>

  <h2 id="bench">Benchmarks</h2>
  <pre><code>export G16_BELT_PROFILE=belt_2_0
./scripts/grok16-toolchain.sh bench-triad
./scripts/grok16-toolchain.sh field-bench
./scripts/grok16-toolchain.sh bench-all</code></pre>
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

  <h2 id="belt">Belt — <code>test-battery-belt</code> (2.0)</h2>
  <pre><code>./scripts/grok16-toolchain.sh test-battery-belt</code></pre>
  <p>Doctrine <code>data/grok16-single-fabric-doctrine.json</code> · profiles <code>belt_1_0</code> / <code>belt_2_0</code> · <code>tests/test_g16_belt_battery.py</code> · triad artifact optional.</p>

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
    "single-fabric.html": (
        "Single Fabric",
        """
  <h1>Single fabric (2.0)</h1>
  <p><strong>Single fabric</strong> is the Grok16 2.0 technology: fixed-size <strong>knowing</strong> on one belt die — not nested fields, not monolithic blast.</p>
  <p>Doctrine: <code>data/grok16-single-fabric-doctrine.json</code> · Citation: <code>ironclad:field_sanity:5</code></p>

  <h2 id="rules">Rules</h2>
  <table>
    <tr><th>Layer</th><th>Rule</th></tr>
    <tr><td>Belt</td><td><code>belt_2_0</code> — 8192 redata chunk, wave-massive, <strong>single-location reads</strong></td></tr>
    <tr><td>Field</td><td>One amplitude at depth 0 — parallel I/O fans in, truth stays single</td></tr>
    <tr><td>Time</td><td>Linear sovereign clock — <code>ironclad:time:1</code>, not geometry <code>t</code></td></tr>
    <tr><td>Safety</td><td>Depth-field creation <strong>forbidden</strong> — stripped at every gate</td></tr>
  </table>

  <h2 id="profiles">Belt profiles</h2>
  <table>
    <tr><th>Profile</th><th>Role</th></tr>
    <tr><td><code>belt_1_0</code></td><td>1.0 baseline (aliases <code>field_opt</code>) — triad compare</td></tr>
    <tr><td><code>belt_2_0</code></td><td><strong>2.0 production</strong> — single fabric dispatch, 512 die slots</td></tr>
  </table>
  <pre><code>export G16_BELT_PROFILE=belt_2_0
./scripts/grok16-toolchain.sh bench-triad</code></pre>
  <p>See <a href="profiles.html#belt">Profiles</a> · <a href="performance.html#triad">Belt triad</a> · <a href="safety.html">Safety</a></p>
""",
    ),
    "safety.html": (
        "Safety",
        """
  <h1>Safety (2.0)</h1>
  <p>Grok16 2.0 safety is melded into Ironclad at integrate time — compile-time mandate plus consumer depth impossibility.</p>

  <h2 id="depth">Depth fields sealed and destroyed</h2>
  <table>
    <tr><th>Gate</th><th>Behavior</th></tr>
    <tr><td><code>field-depth-singularizer</code></td><td>Seal and destroy <code>field_depth</code>, zero nested layers, ledger violations</td></tr>
    <tr><td>Queen field-net</td><td><code>depth_field_impossible: true</code> on classify</td></tr>
    <tr><td>Queen browser</td><td>Navigate strips depth before tab persist</td></tr>
    <tr><td>NEXUS HTTP</td><td>302 redirect when <code>?field_depth=</code> present</td></tr>
  </table>
  <p><strong>Rule:</strong> one field, depth zero always. Creation cannot persist.</p>

  <h2 id="ironclad">Ironclad meld</h2>
  <ul>
    <li><code>data/g16-ironclad-meld.json</code> — time linear, single fabric, field sanity verses</li>
    <li><code>g16-ironclad-sanity</code> gate in forge and batteries</li>
    <li><code>G16_FIELD_SAFETY_MANDATE_v1</code> on field targets</li>
  </ul>

  <h2 id="time">Sovereign time</h2>
  <p>Time is linear (<code>ironclad:time:1</code>). G1ID meld uses <code>linear_ns</code> only — <code>t</code> forbidden in geometry.</p>

  <h2 id="integrate">Integrate</h2>
  <pre><code>./scripts/grok16-integrate.sh</code></pre>
  <p>Publishes <code>data/grok16-integrate.env</code> and wires Queen / World_Redata / ZOCR to canonical prefix + belt profile. See <a href="integration.html">Integration</a>.</p>
""",
    ),
    "performance.html": (
        "Performance",
        """
  <h1>Performance</h1>
  <p>Measured: Linux x86_64, <code>g16 (Grok16-{G16}) {G16}</code>, gnu++26. Repo: <code>PERFORMANCE.md</code>.</p>

  <h2 id="triad">Belt triad (bench-triad)</h2>
  <p>Workload: <code>examples/field-nexus-bench</code> — 240 frames, FieldX86 + entropy + wave + NEXUS.</p>
  <table>
    <tr><th>Toolchain</th><th>Profile</th><th>compile_ms</th><th>run wall_ms</th><th>binary bytes</th></tr>
    <tr><td>host <code>g++</code></td><td>-O3 -march=native</td><td>~2575</td><td>~3</td><td>~27264</td></tr>
    <tr><td><code>g16</code></td><td><code>belt_1_0</code></td><td>~2377</td><td>~3</td><td>~22712</td></tr>
    <tr><td><code>g16</code></td><td><code>belt_2_0</code></td><td>~3708</td><td>~5</td><td>~22840</td></tr>
  </table>
  <p><code>belt_1_0</code> matches host runtime; <code>belt_2_0</code> trades compile time for production single-fabric belt.</p>
  <pre><code>./scripts/grok16-toolchain.sh bench-triad
cat data/bench/triad-latest.json</code></pre>

  <h2 id="field-bench">Field-Opt vs baseline</h2>
  <table>
    <tr><th>Build</th><th>Flags</th><th>kernel wall_ms</th><th>binary bytes</th></tr>
    <tr><td>baseline</td><td>-std=gnu++26 -O2</td><td>2.65</td><td>17144</td></tr>
    <tr><td>field_opt / belt_1_0</td><td>profile flags</td><td>2.11–2.19</td><td>22616</td></tr>
  </table>
  <p>Delta: ~19% faster kernel vs -O2 on same source.</p>

  <h2 id="bench-all">Profile suite (bench-all)</h2>
  <table>
    <tr><th>Profile</th><th>compile_ms</th><th>run_ms</th><th>bytes</th><th>kernel</th></tr>
    <tr><td>field_opt</td><td>828–874</td><td>4–5</td><td>22616</td><td>wall_ms ~2.1</td></tr>
    <tr><td>belt_2_0</td><td>~3708</td><td>~5</td><td>22840</td><td>single fabric</td></tr>
    <tr><td>ai</td><td>735</td><td>6–7</td><td>18232</td><td>wall_ms ~4.0</td></tr>
    <tr><td>vulkan_rtx</td><td>864–876</td><td>4–5</td><td>22728</td><td>wall_ms ~2.1</td></tr>
  </table>

  <h2 id="reproduce">Reproduce</h2>
  <pre><code>export G16_PREFIX="$(pwd)"
export G16_BELT_PROFILE=belt_2_0
./scripts/grok16-toolchain.sh bench-triad
./scripts/grok16-toolchain.sh field-bench
./scripts/grok16-toolchain.sh bench-all</code></pre>

  <h2 id="pgo">PGO</h2>
  <pre><code>./scripts/grok16-toolchain.sh profile
G16_ENABLE_PGO=1 ./scripts/grok16-toolchain.sh field-bench</code></pre>
""".format(G16=G16),
    ),
    "integration.html": (
        "Integration",
        """
  <h1>Integration</h1>
  <p>Requires Grok16 <strong>v{DISTRO}</strong> with <code>test-battery-release</code> + <code>test-battery-belt</code> green.</p>

  <h2 id="integrate">Auto-integrate (2.0)</h2>
  <pre><code>./scripts/grok16-integrate.sh</code></pre>
  <p>Wires canonical prefix + <code>G16_BELT_PROFILE=belt_2_0</code> to Queen, World_Redata, ZOCR/Final_Ear, PythonG. Env: <code>data/grok16-integrate.env</code></p>

  <h2 id="gates">Safety at consumers</h2>
  <p>Integrated SG tree enforces <strong>single fabric</strong> safety:</p>
  <table>
    <tr><th>Consumer</th><th>Depth field</th><th>Ironclad</th></tr>
    <tr><td>Queen field-net</td><td><code>depth_field_impossible</code></td><td>classify strip</td></tr>
    <tr><td>Queen browser</td><td>navigate enforce</td><td>tab URL clean</td></tr>
    <tr><td>NEXUS panel</td><td>HTTP 302 strip</td><td>field-depth-singularizer</td></tr>
    <tr><td>Field sanity</td><td>integral preflight</td><td><code>ironclad:field_sanity:4</code></td></tr>
  </table>
  <p>Doctrine: <code>NewLatest/data/single-field-depth-doctrine.json</code> · <a href="safety.html">Safety manual</a></p>

  <h2 id="wrdt">World_Redata</h2>
  <pre><code>cd World_Redata
./build-cpp.sh
PYTHONPATH=. pythong -m redata.cli parity
PYTHONPATH=. pythong -m redata.cli security</code></pre>

  <h2 id="env">Downstream env</h2>
  <pre><code>export G16_PREFIX=/path/to/Grok16
export G16_BELT_PROFILE=belt_2_0
export WRDT_G16_PREFIX="$G16_PREFIX"
source data/grok16-integrate.env</code></pre>

  <h2 id="ironclad">Ironclad</h2>
  <p><code>data/g16-ironclad-meld.json</code> — single fabric, linear time, field sanity absorbed at forge link pass.</p>
""".format(DISTRO=DISTRO),
    ),
    "profiles.html": (
        "Profiles",
        """
  <h1>Build Profiles</h1>
  <p>Defined in <code>data/grok16-profiles.json</code>. Default C++ standard: <code>gnu++26</code>. Distro 2.0 default belt: <code>belt_2_0</code>.</p>

  <h2 id="belt">Belt profiles (2.0)</h2>
  <table>
    <tr><th>Name</th><th>CMake</th><th>Use</th></tr>
    <tr id="belt-2"><td><strong>belt_2_0</strong></td><td>grok16-profile-belt-2.cmake</td><td>Single fabric production — 8192 chunk, wave-massive, 512 slots</td></tr>
    <tr id="belt-1"><td>belt_1_0</td><td>grok16-profile-field-opt.cmake</td><td>1.0 baseline (field_opt) — triad compare</td></tr>
  </table>
  <pre><code>export G16_BELT_PROFILE=belt_2_0
G16_BENCH_PROFILE=belt_2_0 ./scripts/grok16-toolchain.sh bench</code></pre>

  <h2>Classic profiles</h2>
  <table>
    <tr><th>Name</th><th>CMake</th><th>Bench source</th><th>Use</th></tr>
    <tr id="field-opt"><td>field_opt</td><td>grok16-profile-field-opt.cmake</td><td>examples/field-nexus-bench/</td><td>FieldX86, entropy, NEXUS (1.0 primary)</td></tr>
    <tr id="ai"><td>ai</td><td>grok16-profile-ai.cmake</td><td>examples/ai-matrix-bench/</td><td>Matrix / scoring loops</td></tr>
    <tr id="field-compute"><td>field_compute</td><td>grok16-profile-field.cmake</td><td>examples/field-canvas-kernel/</td><td>CANVAS-style dispatch</td></tr>
    <tr id="vulkan-rtx"><td>vulkan_rtx</td><td>grok16-profile-vulkan.cmake</td><td>field-nexus-bench</td><td>AVX2/FMA CPU kernels</td></tr>
  </table>

  <h2 id="bench">Bench profile selection</h2>
  <pre><code>G16_BENCH_PROFILE=belt_2_0 ./scripts/grok16-toolchain.sh bench
G16_FIELD_SPEED=1 ./scripts/grok16-toolchain.sh field-bench
./scripts/grok16-toolchain.sh bench-triad</code></pre>

  <h2 id="mandate">Safety mandate</h2>
  <p>All field targets include <code>cmake/g16-field-mandate.cmake</code> (<code>G16_FIELD_SAFETY_MANDATE_v1</code>). See <a href="safety.html">Safety</a>.</p>
""",
    ),
}

SEARCH_INDEX = [
    {"t": "single fabric", "p": "single-fabric.html", "g": "2.0", "d": "One belt die one field amplitude knowing fixed-size"},
    {"t": "belt_2_0", "p": "profiles.html#belt-2", "g": "Profile", "d": "2.0 production belt chunked redata 8192"},
    {"t": "bench-triad", "p": "performance.html#triad", "g": "Bench", "d": "host gcc vs belt_1_0 vs belt_2_0"},
    {"t": "test-battery-belt", "p": "batteries.html#belt", "g": "Battery", "d": "2.0 belt validation atop release"},
    {"t": "grok16-integrate", "p": "integration.html#integrate", "g": "Integrate", "d": "Auto-wire Queen WRDT ZOCR belt_2_0"},
    {"t": "depth fields sealed and destroyed", "p": "safety.html#depth", "g": "Safety", "d": "field_depth sealed and destroyed at gates"},
    {"t": "ironclad:time:1", "p": "safety.html#time", "g": "Safety", "d": "Sovereign linear time linear_ns only"},
    {"t": "test-battery-release", "p": "batteries.html#release", "g": "Battery", "d": "Production gate heavy py forever binutils verify"},
    {"t": "test-battery-expert", "p": "batteries.html#expert", "g": "Battery", "d": "Ironclad linker RTX expert profile"},
    {"t": "g16-ld", "p": "linker.html", "g": "Linker", "d": "Field linker 16 targets mandate flags"},
    {"t": "GPY-16", "p": "toolkits.html#gpy16", "g": "Toolkit", "d": "Built-in Python GrokVM gpy-16"},
    {"t": "v2.0.0", "p": "release.html", "g": "Release", "d": "Single fabric distro tag checkout belt gate"},
    {"t": "bootstrap", "p": "getting-started.html#bootstrap", "g": "Workflow", "d": "First GCC fetch host build install"},
    {"t": "g16 unified", "p": "architecture.html#unified-driver", "g": "Driver", "d": "Single g16 C C++ Python discern"},
    {"t": "field_opt", "p": "profiles.html#field-opt", "g": "Profile", "d": "1.0 primary Field throughput belt_1_0 alias"},
    {"t": "G16_BELT_PROFILE", "p": "profiles.html#belt", "g": "Env", "d": "Default belt_2_0 single fabric dispatch"},
    {"t": "G16_RELEASE_PROFILE", "p": "getting-started.html#rebuild", "g": "Env", "d": "LTO PGO production rebuild"},
    {"t": "gnu++26", "p": "field-primer.html#standard", "g": "C++", "d": "Default C++ standard"},
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
        "field-primer.html", "reference.html", "concepts.html", "io.html",
        "master-coder.html", "master-coder-c.html", "master-coder-cxx.html",
    ]
    new_links = "\n".join(
        f'      <a href="{h}">{l}</a>' for h, l in NAV if h != "index.html"
    )
    new_nav_block = f"""    <div class="nav-links">
      <a href="index.html">Home</a>
{new_links}
    </div>"""
    cache_pat = re.compile(r"manual-(?:css|theme|search|layout)\.js\?v\d+|manual\.css\?v\d+")
    for fname in legacy:
        path = ROOT / fname
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        text = cache_pat.sub(lambda m: m.group(0).rsplit("v", 1)[0] + CACHE, text)
        text = text.replace('<span class="nav-version">v16.1.1</span>',
                            f'<span class="nav-version">distro {DISTRO}</span><span class="nav-g16">g16 @ {G16}</span>')
        text = text.replace(f'<span class="nav-version">distro 1.0.0</span><span class="nav-g16">g16 @ 16.1.1</span>',
                            f'<span class="nav-version">distro {DISTRO}</span><span class="nav-g16">g16 @ {G16}</span>')
        text = text.replace("<strong>Grok16 Manual</strong>", "<strong>Grok16</strong>")
        if '<div class="nav-links">' in text:
            text = re.sub(
                r'<div class="nav-links">.*?</div>',
                new_nav_block,
                text,
                count=1,
                flags=re.DOTALL,
            )
        path.write_text(text, encoding="utf-8")
        print(f"patched {fname}")


def patch_concepts_single_fabric() -> None:
    """Insert 2.0 single-fabric callout on concepts page."""
    path = ROOT / "concepts.html"
    if not path.is_file():
        return
    marker = '<aside class="callout">\n    <strong>Workflow tip:</strong>'
    insert = """  <aside class="callout callout-accent">
    <strong>Single fabric (2.0):</strong> Knowing is fixed-size on one belt die — parallel I/O fans in, truth stays one amplitude at depth 0. Time is linear (<code>ironclad:time:1</code>). See <a href="single-fabric.html">Single Fabric</a> and <a href="safety.html">Safety</a>.
  </aside>

"""
    text = path.read_text(encoding="utf-8")
    if "Single fabric (2.0)" not in text and marker in text:
        text = text.replace(marker, insert + marker, 1)
        path.write_text(text, encoding="utf-8")
        print("patched concepts.html (single fabric callout)")


def main() -> int:
    write_pages()
    write_search()
    patch_legacy_pages()
    patch_concepts_single_fabric()
    gen = ROOT / "gen-master-pages.py"
    if gen.is_file():
        subprocess.run([sys.executable, str(gen)], check=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())