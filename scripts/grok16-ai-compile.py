#!/usr/bin/env pythong
"""Grok16 AI agent compile — structured JSON for machines, not humans at the TTY."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(os.environ.get("GROK16_ROOT", Path(__file__).resolve().parents[1]))
PREFIX = Path(os.environ.get("G16_PREFIX", ROOT))
G16 = PREFIX / "bin" / "g16"
PROFILE = os.environ.get("G16_AI_PROFILE", "ai_agent")
PROFILE_SCRIPT = ROOT / "scripts" / "grok16-profile-flags.py"


def _profile_flags(kind: str = "cxx") -> list[str]:
    if not PROFILE_SCRIPT.is_file():
        return ["-std=gnu++26", "-O2"]
    env = {**os.environ, "GROK16_ROOT": str(ROOT), "G16_PREFIX": str(PREFIX), "G16_BENCH_PROFILE": PROFILE}
    proc = subprocess.run(
        [sys.executable, str(PROFILE_SCRIPT), PROFILE, kind],
        capture_output=True, text=True, timeout=30, env=env,
    )
    if proc.returncode != 0:
        return ["-std=gnu++26", "-O2"]
    return proc.stdout.strip().split()


def _parse_errors(stderr: str) -> list[dict]:
    rows: list[dict] = []
    for line in stderr.splitlines():
        m = re.match(r"([^:]+):(\d+):(\d+):\s*(error|warning|note):\s*(.*)", line)
        if m:
            rows.append({
                "file": m.group(1),
                "line": int(m.group(2)),
                "column": int(m.group(3)),
                "severity": m.group(4),
                "message": m.group(5),
            })
    return rows


def compile_source(
    source: str,
    *,
    lang: str = "cxx",
    out_name: str = "g16_ai_out",
) -> dict:
    if not G16.is_file():
        return {"ok": False, "error": f"missing g16 at {G16}"}
    suffix = ".cpp" if lang == "cxx" else ".c"
    std_flag = "-std=gnu++26" if lang == "cxx" else "-std=gnu17"
    with tempfile.TemporaryDirectory(prefix="g16-ai-") as td:
        src = Path(td) / f"snippet{suffix}"
        out = Path(td) / out_name
        src.write_text(source, encoding="utf-8")
        flags = _profile_flags("cxx" if lang == "cxx" else "c")
        if std_flag not in flags:
            flags = [std_flag, *flags]
        cmd = [str(G16), *flags, "-o", str(out), str(src)]
        t0 = time.time()
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        ms = int((time.time() - t0) * 1000)
        errors = _parse_errors(proc.stderr)
        return {
            "schema": "grok16-ai-compile/v1",
            "ok": proc.returncode == 0,
            "profile": PROFILE,
            "lang": lang,
            "compile_ms": ms,
            "returncode": proc.returncode,
            "diagnostics": errors,
            "stderr_tail": proc.stderr[-4000:] if proc.stderr else "",
            "stdout": proc.stdout.strip(),
            "binary": str(out) if out.is_file() else "",
            "hostess_truth_floor": 58,
        }


def main() -> int:
    if len(sys.argv) < 2:
        print(json.dumps({
            "usage": "grok16-ai-compile.py -c 'code' | file.cpp | --json doc.json",
            "profile": PROFILE,
            "default_for": "AI agents — presumes compiler used more than human TTY",
        }, indent=2))
        return 2
    if sys.argv[1] in ("-c", "--code"):
        code = sys.argv[2] if len(sys.argv) > 2 else sys.stdin.read()
        lang = "cxx" if "int main" in code or "#include" in code else "cxx"
        doc = compile_source(code, lang=lang)
        print(json.dumps(doc, indent=2))
        return 0 if doc.get("ok") else 1
    path = Path(sys.argv[1])
    if path.is_file():
        lang = "cxx" if path.suffix in (".cpp", ".cxx", ".cc") else "c"
        doc = compile_source(path.read_text(encoding="utf-8"), lang=lang)
        print(json.dumps(doc, indent=2))
        return 0 if doc.get("ok") else 1
    print(json.dumps({"ok": False, "error": "usage: -c code or file"}, indent=2))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())