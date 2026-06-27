#!/usr/bin/env python3
"""Professional comprehensive bench — bench-all + exec-full + plate meld analysis."""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DOCS_JSON = ROOT / "docs" / "field-exec-comprehensive-bench.json"
DOCS_MD = ROOT / "docs" / "COMPREHENSIVE-BENCH-REPORT.md"


def _run(cmd: list[str], *, timeout: int = 3600) -> int:
    env = {**os.environ, "GROK16_ROOT": str(ROOT), "G16_PREFIX": os.environ.get("G16_PREFIX", str(ROOT))}
    print(f"+ {' '.join(cmd)}", flush=True)
    return subprocess.run(cmd, cwd=str(ROOT), env=env, timeout=timeout).returncode


def main() -> int:
    target = os.environ.get("SPEED_DEMO_TARGET_SEC", "3")
    steps: list[dict] = []

    # 1. Profile suite (field-nexus-bench per profile)
    rc = _run(["bash", str(SCRIPTS / "grok16-toolchain.sh"), "bench-all"], timeout=7200)
    steps.append({"step": "bench-all", "rc": rc, "profiles": ["field_opt", "belt_1_0", "belt_2_0", "ai", "field_compute", "vulkan_rtx"]})
    if rc != 0:
        print("warn: bench-all failed — continuing with exec-full-bench", file=sys.stderr)

    # 2. Stage exec plane (cached binaries for compare)
    rc_stage = _run([sys.executable, str(SCRIPTS / "field-exec-stage.py")], timeout=1800)
    steps.append({"step": "exec-stage", "rc": rc_stage})

    # 3. Full speed_demo bench (all runners + plate meld)
    rc_full = _run(
        [sys.executable, str(SCRIPTS / "field-exec-full-bench.py")],
        timeout=3600,
    )
    steps.append({"step": "exec-full-bench", "rc": rc_full, "target_sec": int(target)})
    if rc_full != 0:
        return rc_full

    # 4. Staged execution compare (no compile in timed path)
    rc_cmp = _run([sys.executable, str(SCRIPTS / "field-exec-compare.py")], timeout=3600)
    steps.append({"step": "exec-compare", "rc": rc_cmp})

    # 5. Assemble comprehensive publishable doc
    full_path = ROOT / "docs" / "field-exec-full-bench.json"
    compare_path = ROOT / "data" / "bench" / "exec-plane" / "field-exec-result.json"
    latest_path = ROOT / "data" / "bench" / "latest.json"
    doc = {
        "schema": "grok16-comprehensive-bench/v1",
        "assembled_by": "scripts/field-exec-comprehensive-bench.py",
        "steps": steps,
        "exec_full_bench": json.loads(full_path.read_text(encoding="utf-8")) if full_path.is_file() else {},
        "exec_compare": json.loads(compare_path.read_text(encoding="utf-8")) if compare_path.is_file() else {},
        "bench_all": json.loads(latest_path.read_text(encoding="utf-8")) if latest_path.is_file() else {},
    }
    DOCS_JSON.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")

    full = doc.get("exec_full_bench") or {}
    pm = full.get("plate_meld") or {}
    lines = [
        "# Grok16 comprehensive benchmark report",
        "",
        f"**Assembled:** {full.get('bench_at', '—')}  ",
        f"**Report:** {full.get('versions', {}).get('report_version', '3.1.0')}  ",
        f"**Runners:** {full.get('runners_tested', '—')} speed_demo executions  ",
        f"**bench-all profiles:** {len((doc.get('bench_all') or {}).get('runs', []))}  ",
        "",
        "## Pipeline",
        "",
        "1. `bench-all` — field-nexus-bench across field_opt, belt_1_0, belt_2_0, ai, field_compute, vulkan_rtx",
        "2. `field-exec-stage.py` — wave-convert once to exec plane",
        f"3. `field-exec-full-bench.py` — speed_demo @ {target}s, all runners, plate meld cycle",
        "4. `field-exec-compare.py` — staged execution only (compile excluded)",
        "",
        "## Plate meld verdict",
        "",
        f"- Post-meld re-exec ratio: **{pm.get('post_meld_exec_ratio', '—')}**",
        f"- Sense profile `{pm.get('context', {}).get('sense_profile', '—')}` vs belt_2_0 ops ratio: **{pm.get('sense_vs_belt_2_ops_ratio', '—')}**",
        f"- Meld helps profile ladder: **{'yes' if pm.get('meld_helps_profile') else 'no'}**",
        "",
        "Full speed bench: [SPEED-BENCH-REPORT.md](SPEED-BENCH-REPORT.md) · JSON: [field-exec-full-bench.json](field-exec-full-bench.json)",
        "",
    ]
    DOCS_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {DOCS_JSON}")
    print(f"Wrote {DOCS_MD}")
    return 0 if rc_full == 0 else rc_full


if __name__ == "__main__":
    raise SystemExit(main())