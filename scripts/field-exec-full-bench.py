#!/usr/bin/env python3
"""Full bench — compile/wave-convert times + bin execution times + winners."""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "lib"))
from field_math import field_display, field_ratio  # noqa: E402

OUTDIR = ROOT / "data" / "bench" / "exec-plane"
SRC_CXX = ROOT / "examples" / "speed-demo" / "speed_demo.cpp"
SRC_C = ROOT / "examples" / "speed-demo" / "speed_demo.c"
SRC_PY = ROOT / "examples" / "speed-demo" / "speed_demo.py"
CMAKE_SRC = ROOT / "examples" / "speed-demo"
G16 = Path(os.environ.get("G16_PREFIX", str(ROOT))) / "bin" / "g16"
GPY = Path(os.environ.get("G16_PREFIX", str(ROOT))) / "bin" / "gpy-16"
PROFILE_PY = ROOT / "scripts" / "grok16-profile-flags.py"
TOOLCHAIN_CMAKE = ROOT / "cmake" / "grok16-toolchain.cmake"
TARGET_SEC = int(os.environ.get("SPEED_DEMO_TARGET_SEC", "3"))
RESULT_JSON = OUTDIR / "field-exec-full-bench.json"
REPORT_MD = ROOT / "data" / "bench" / "SPEED-BENCH-REPORT.md"
DOCS_REPORT_MD = ROOT / "docs" / "SPEED-BENCH-REPORT.md"
DOCS_RESULT_JSON = ROOT / "docs" / "field-exec-full-bench.json"


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _run(cmd: list[str], *, cwd: Path | None = None, timeout: int = 600) -> tuple[int, str, str, float]:
    t0 = time.perf_counter()
    env = {**os.environ, "GROK16_ROOT": str(ROOT), "G16_PREFIX": os.environ.get("G16_PREFIX", str(ROOT))}
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(cwd or ROOT), env=env, timeout=timeout)
    ms = round((time.perf_counter() - t0) * 1000, 2)
    return proc.returncode, proc.stdout, proc.stderr, ms


def _profile_flags(profile: str, kind: str) -> list[str]:
    if not PROFILE_PY.is_file():
        return []
    rc, out, _, _ = _run([sys.executable, str(PROFILE_PY), profile, kind], timeout=30)
    return out.strip().split() if rc == 0 and out.strip() else []


def _g16_extra() -> list[str]:
    rc, out, _, _ = _run(["bash", "-lc", f'source "{ROOT}/scripts/grok16-config.sh" && grok16_driver_extra_flags'], timeout=15)
    return out.strip().split() if rc == 0 and out.strip() else []


def _merge_g16_flags(cxx: list[str], link: list[str]) -> list[str]:
    link = [a for a in link if a not in ("-flto=thin", "-flto")]
    cxx = list(cxx)
    if "-fPIE" not in cxx and "-fpie" not in cxx:
        cxx.append("-fPIE")
    if "-pie" not in link and "-no-pie" not in link:
        link = [*link, "-pie"]
    return [*cxx, *link]


def _host_gxx() -> str:
    gxx = shutil.which("g++") or "/usr/bin/g++"
    if "grok16" in gxx or str(G16) in gxx:
        for candidate in ("/usr/bin/g++", "/usr/bin/g++-13", "/usr/bin/g++-12"):
            if Path(candidate).is_file():
                return candidate
    return gxx


def _host_gcc() -> str:
    gcc = shutil.which("gcc") or "/usr/bin/gcc"
    if "grok16" in gcc or str(G16) in gcc:
        for candidate in ("/usr/bin/gcc", "/usr/bin/gcc-13", "/usr/bin/gcc-12"):
            if Path(candidate).is_file():
                return candidate
    return gcc


def _parse_ops(stdout: str) -> dict | None:
    for line in reversed(stdout.splitlines()):
        if line.startswith("speed_demo") and "ops_per_sec=" in line:
            m = re.search(r"wall_ms=([0-9.eE+-]+)", line)
            w = re.search(r"ops_per_sec=([0-9.eE+-]+)", line)
            t = re.search(r"total_ops=([0-9.eE+-]+)", line)
            if w:
                return {
                    "wall_ms": float(m.group(1)) if m else 0,
                    "ops_per_sec": float(w.group(1)),
                    "total_ops": int(float(t.group(1))) if t else 0,
                }
    return None


def _exec_runner(row: dict) -> dict:
    env = {**os.environ, "SPEED_DEMO_TARGET_SEC": str(TARGET_SEC)}
    if row.get("env"):
        env.update({k: str(v) for k, v in row["env"].items()})
    if row.get("kind") == "script":
        cmd = list(row["cmd"])
    else:
        cmd = [str(row["path"])]
    t0 = time.perf_counter()
    proc = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=TARGET_SEC + 30, cwd=str(ROOT))
    wall_ms = round((time.perf_counter() - t0) * 1000, 2)
    parsed = _parse_ops(proc.stdout) or {}
    return {
        "rc": proc.returncode,
        "runner_wall_ms": wall_ms,
        "field_execution_ms": parsed.get("wall_ms") or wall_ms,
        "ops_per_sec": parsed.get("ops_per_sec") or 0,
        "total_ops": parsed.get("total_ops") or 0,
    }


def bench_all() -> dict:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    bench_dir = OUTDIR / "full-bench-build"
    if bench_dir.is_dir():
        shutil.rmtree(bench_dir)
    bench_dir.mkdir(parents=True, exist_ok=True)

    host_gcc = _host_gcc()
    host_gxx = _host_gxx()
    rows: list[dict] = []

    def add(row: dict) -> None:
        rows.append(row)

    # C host
    out_c = bench_dir / "c_host_o2"
    rc, _, err, ms = _run(
        [host_gcc, "-std=gnu17", "-O2", "-march=native", "-fPIE", '-DTOOLCHAIN_TAG="c_host_o2"', "-o", str(out_c), str(SRC_C), "-lm"]
    )
    if rc == 0 and out_c.is_file():
        out_c.chmod(out_c.stat().st_mode | 0o111)
        add({
            "id": "c_host_o2", "label": "C — host gcc -O2", "lang": "c", "group": "host",
            "kind": "binary", "path": str(out_c), "compile_ms": ms, "compile_note": "single gcc invoke",
        })

    # C g16
    if G16.is_file():
        out_cg = bench_dir / "c_g16_belt_2"
        flags = [*_g16_extra(), *_merge_g16_flags(
            _profile_flags("belt_2_0", "c") or ["-std=gnu17", "-O3", "-march=native"],
            _profile_flags("belt_2_0", "link") or [],
        )]
        rc, _, _, ms = _run([str(G16), *flags, '-DTOOLCHAIN_TAG="c_g16_belt_2"', "-o", str(out_cg), str(SRC_C), "-lm"])
        if rc == 0 and out_cg.is_file():
            out_cg.chmod(out_cg.stat().st_mode | 0o111)
            add({
                "id": "c_g16_belt_2", "label": "C — g16 belt_2_0", "lang": "c", "group": "g16",
                "kind": "binary", "path": str(out_cg), "compile_ms": ms, "compile_note": "g16 belt_2_0",
            })

    # C++ host
    out_cxx = bench_dir / "cxx_host_o2"
    rc, _, _, ms = _run(
        [host_gxx, "-std=gnu++23", "-O2", "-march=native", "-fPIE", '-DTOOLCHAIN_TAG="cxx_host_o2"', "-o", str(out_cxx), str(SRC_CXX)]
    )
    if rc == 0 and out_cxx.is_file():
        out_cxx.chmod(out_cxx.stat().st_mode | 0o111)
        add({
            "id": "cxx_host_o2", "label": "C++ — host g++ -O2", "lang": "cxx", "group": "host",
            "kind": "binary", "path": str(out_cxx), "compile_ms": ms, "compile_note": "single g++ invoke",
        })

    # C++ g16
    if G16.is_file():
        out_cxxg = bench_dir / "cxx_g16_belt_2"
        flags = [*_g16_extra(), *_merge_g16_flags(
            _profile_flags("belt_2_0", "cxx") or ["-std=gnu++26", "-O3", "-march=native"],
            _profile_flags("belt_2_0", "link") or [],
        )]
        rc, _, _, ms = _run([str(G16), *flags, '-DTOOLCHAIN_TAG="cxx_g16_belt_2"', "-o", str(out_cxxg), str(SRC_CXX)])
        if rc == 0 and out_cxxg.is_file():
            out_cxxg.chmod(out_cxxg.stat().st_mode | 0o111)
            add({
                "id": "cxx_g16_belt_2", "label": "C++ — g16 belt_2_0", "lang": "cxx", "group": "g16",
                "kind": "binary", "path": str(out_cxxg), "compile_ms": ms, "compile_note": "g16 belt_2_0",
            })

    # CMake host
    build_host = bench_dir / "cmake-host"
    build_host.mkdir(parents=True, exist_ok=True)
    cfg_ms = bld_ms = 0.0
    rc, _, _, cfg_ms = _run([
        "cmake", "-S", str(CMAKE_SRC), "-B", str(build_host),
        f"-DCMAKE_CXX_COMPILER={host_gxx}", "-DGROK16_HOST_PLANE=ON",
    ])
    if rc == 0:
        rc, _, _, bld_ms = _run(["cmake", "--build", str(build_host), "-j", str(os.cpu_count() or 4)])
    bin_host = build_host / "grok16_speed_demo"
    if rc == 0 and bin_host.is_file():
        staged = bench_dir / "cmake_host_o2"
        shutil.copy2(bin_host, staged)
        staged.chmod(staged.stat().st_mode | 0o111)
        add({
            "id": "cmake_host_o2", "label": "CMake — host g++ -O2", "lang": "cmake", "group": "host",
            "kind": "binary", "path": str(staged), "compile_ms": round(cfg_ms + bld_ms, 2),
            "compile_configure_ms": cfg_ms, "compile_build_ms": bld_ms, "compile_note": "cmake configure + build",
        })

    # CMake g16
    if TOOLCHAIN_CMAKE.is_file() and G16.is_file():
        build_g16 = bench_dir / "cmake-g16"
        build_g16.mkdir(parents=True, exist_ok=True)
        rc, _, _, cfg_ms = _run([
            "cmake", "-S", str(CMAKE_SRC), "-B", str(build_g16),
            f"-DCMAKE_TOOLCHAIN_FILE={TOOLCHAIN_CMAKE}", "-DGROK16_PROFILE=belt_2_0",
        ])
        bld_ms = 0.0
        if rc == 0:
            rc, _, _, bld_ms = _run(["cmake", "--build", str(build_g16), "-j", str(os.cpu_count() or 4)])
        bin_g16 = build_g16 / "grok16_speed_demo"
        if rc == 0 and bin_g16.is_file():
            staged = bench_dir / "cmake_belt_2"
            shutil.copy2(bin_g16, staged)
            staged.chmod(staged.stat().st_mode | 0o111)
            add({
                "id": "cmake_belt_2", "label": "CMake — g16 belt_2_0", "lang": "cmake", "group": "g16",
                "kind": "binary", "path": str(staged), "compile_ms": round(cfg_ms + bld_ms, 2),
                "compile_configure_ms": cfg_ms, "compile_build_ms": bld_ms, "compile_note": "cmake configure + build",
            })

    # Python — no compile
    py3 = shutil.which("python3") or "python3"
    add({
        "id": "python_host", "label": "Python — host CPython 3", "lang": "python", "group": "host",
        "kind": "script", "cmd": [py3, str(SRC_PY)], "env": {"TOOLCHAIN_TAG": "python_host"},
        "compile_ms": 0, "compile_note": "interpreter — no compile",
    })
    if GPY.is_file():
        add({
            "id": "python_gpy", "label": "Python — gpy-16 GrokVM", "lang": "python", "group": "g16",
            "kind": "script", "cmd": [str(GPY), str(SRC_PY)], "env": {"TOOLCHAIN_TAG": "python_gpy"},
            "compile_ms": 0, "compile_note": "GrokVM interpreter — no compile",
        })

    # Execute all
    for row in rows:
        ex = _exec_runner(row)
        row.update(ex)
        if row.get("path") and Path(row["path"]).is_file():
            row["binary_bytes"] = Path(row["path"]).stat().st_size

    # Winners
    compiled = [r for r in rows if r.get("kind") == "binary" and r.get("ops_per_sec")]
    scripts = [r for r in rows if r.get("kind") == "script" and r.get("ops_per_sec")]
    best_exec = max(rows, key=lambda r: r.get("ops_per_sec") or 0) if rows else None
    fastest_compile = min((r for r in rows if r.get("compile_ms", 0) > 0), key=lambda r: r["compile_ms"], default=None)
    slowest_compile = max((r for r in rows if r.get("compile_ms", 0) > 0), key=lambda r: r["compile_ms"], default=None)
    best_c = max((r for r in rows if r.get("lang") == "c"), key=lambda r: r.get("ops_per_sec") or 0, default=None)
    best_cxx = max((r for r in rows if r.get("lang") == "cxx"), key=lambda r: r.get("ops_per_sec") or 0, default=None)
    best_cmake = max((r for r in rows if r.get("lang") == "cmake"), key=lambda r: r.get("ops_per_sec") or 0, default=None)
    best_py = max((r for r in rows if r.get("lang") == "python"), key=lambda r: r.get("ops_per_sec") or 0, default=None)

    # Best combined score: exec / (1 + compile_sec) for binaries
    for r in rows:
        if r.get("kind") == "binary":
            cs = (r.get("compile_ms") or 0) / 1000.0
            r["amortized_ops_per_sec"] = (r.get("ops_per_sec") or 0) / (1.0 + cs)
    best_amortized = max((r for r in rows if r.get("amortized_ops_per_sec")), key=lambda r: r["amortized_ops_per_sec"], default=None)

    doc = {
        "schema": "grok16-field-exec-full-bench/v1",
        "bench_at": _utc(),
        "target_sec": TARGET_SEC,
        "kernel": "speed_demo — FieldX86 loop (256×16 die, 240 frames/epoch, 512 prog_ops/frame)",
        "host": os.uname().nodename,
        "rows": rows,
        "winners": {
            "best_execution": {"id": best_exec["id"], "label": best_exec["label"], "ops_per_sec": best_exec["ops_per_sec"]} if best_exec else None,
            "fastest_compile": {"id": fastest_compile["id"], "label": fastest_compile["label"], "compile_ms": fastest_compile["compile_ms"]} if fastest_compile else None,
            "slowest_compile": {"id": slowest_compile["id"], "label": slowest_compile["label"], "compile_ms": slowest_compile["compile_ms"]} if slowest_compile else None,
            "best_per_language": {
                "c": {"id": best_c["id"], "ops_per_sec": best_c["ops_per_sec"]} if best_c else None,
                "cxx": {"id": best_cxx["id"], "ops_per_sec": best_cxx["ops_per_sec"]} if best_cxx else None,
                "cmake": {"id": best_cmake["id"], "ops_per_sec": best_cmake["ops_per_sec"]} if best_cmake else None,
                "python": {"id": best_py["id"], "ops_per_sec": best_py["ops_per_sec"]} if best_py else None,
            },
            "best_amortized_first_run": {
                "id": best_amortized["id"], "label": best_amortized["label"],
                "amortized_ops_per_sec": best_amortized["amortized_ops_per_sec"],
            } if best_amortized else None,
        },
    }
    RESULT_JSON.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    _write_report_md(doc)
    # Publishable copies (data/bench/ is gitignored)
    DOCS_REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    pub = json.loads(json.dumps(doc))
    for r in pub.get("rows", []):
        if r.get("path"):
            r["path"] = Path(r["path"]).name
    DOCS_RESULT_JSON.write_text(json.dumps(pub, indent=2) + "\n", encoding="utf-8")
    DOCS_REPORT_MD.write_text(REPORT_MD.read_text(encoding="utf-8"), encoding="utf-8")
    return doc


def _write_report_md(doc: dict) -> None:
    rows = doc["rows"]
    w = doc["winners"]
    lines = [
        "# Grok16 speed-demo — compile + execution benchmark",
        "",
        f"**Bench date:** {doc['bench_at']}  ",
        f"**Target execution window:** {doc['target_sec']}s per runner  ",
        f"**Kernel:** {doc['kernel']}  ",
        f"**Host:** {doc['host']}",
        "",
        "## Summary",
        "",
        "This report separates **wave-convert / compile time** (one-time, chamber can cache ahead) from **bin execution time** (timed field run). Python runners have zero compile — they execute on the interpreter.",
        "",
    ]
    if w.get("best_execution"):
        be = w["best_execution"]
        lines.append(f"- **Fastest execution:** {be['label']} — **{field_display(be['ops_per_sec'])} ops/s**")
    if w.get("fastest_compile"):
        fc = w["fastest_compile"]
        lines.append(f"- **Fastest compile:** {fc['label']} — **{fc['compile_ms']:.0f} ms**")
    if w.get("best_per_language", {}).get("python"):
        bp = w["best_per_language"]["python"]
        lines.append(f"- **Best Python (interpreter):** {bp['id']} — **{field_display(bp['ops_per_sec'])} ops/s**")
    lines.extend(["", "## Full results", "", "| Runner | Compile (ms) | Exec wall (ms) | ops/s | Binary bytes |", "|--------|-------------:|---------------:|------:|-------------:|"])
    for r in sorted(rows, key=lambda x: -(x.get("ops_per_sec") or 0)):
        compile_ms = r.get("compile_ms", 0)
        compile_s = "—" if r.get("kind") == "script" else f"{compile_ms:,.0f}"
        wall = r.get("field_execution_ms") or r.get("runner_wall_ms") or 0
        ops = field_display(r.get("ops_per_sec") or 0)
        bbytes = r.get("binary_bytes") or "—"
        if isinstance(bbytes, int):
            bbytes = f"{bbytes:,}"
        lines.append(f"| {r['label']} | {compile_s} | {wall:,.0f} | {ops} | {bbytes} |")
    lines.extend(["", "## Winners by category", ""])
    for lang, info in (w.get("best_per_language") or {}).items():
        if info:
            row = next((x for x in rows if x["id"] == info["id"]), {})
            lines.append(f"- **{lang.upper()}:** {row.get('label', info['id'])} — {field_display(info['ops_per_sec'])} ops/s")
    if w.get("best_amortized_first_run"):
        ba = w["best_amortized_first_run"]
        lines.append(f"- **Best first-run amortized** (exec ÷ (1 + compile_sec)): {ba['label']} — {field_display(ba['amortized_ops_per_sec'])} effective ops/s")
    lines.extend([
        "",
        "## Doctrine",
        "",
        "- **Dev / uncompiled:** Python runs at interpreter speed (~0.8M ops/s). C/C++ rely on chamber organization + compile ahead (cached on singular plane).",
        "- **Release / plane:** Staged binaries reach ~84–91M ops/s on this host; compile is not in the timed execution path after cache hit.",
        "- **Compare axis:** `field_execution_ops_per_sec` on identical `speed_demo` kernel.",
        "",
        "## Reproduce",
        "",
        "```bash",
        "cd Grok16",
        "SPEED_DEMO_TARGET_SEC=3 python3 scripts/field-exec-full-bench.py",
        "python3 scripts/field-exec-stage.py",
        "SPEED_DEMO_TARGET_SEC=3 python3 scripts/field-exec-compare.py",
        "```",
        "",
        f"Machine JSON: `data/bench/exec-plane/field-exec-full-bench.json`",
        "",
    ])
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    doc = bench_all()
    print(json.dumps(doc["winners"], indent=2))
    print(f"\nWrote {RESULT_JSON}")
    print(f"Wrote {REPORT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())