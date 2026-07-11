#!/usr/bin/env python3
# Grok16 HARD · ironclad:g16-python-harden:2 · exploits DISPERMITTED · soft-kill FORBIDDEN
# Weapon policy: SIGKILL/INSTAKILL only on hostile Field plane — never SIGTERM authoring
"""Grok16 native compile — secure argv-only gcc/g16 path (no shell, no exploits).

  Used by g16-secure-chamber. Hard flags throughout.

ironclad:g16-native-compile:2
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

GROK16 = Path(os.environ.get("GROK16_ROOT", Path(__file__).resolve().parents[1]))
INSTALL = Path(os.environ.get("NEXUS_INSTALL_ROOT", GROK16.parent))

# Harder default flags
HARD_CFLAGS = [
    "-O2",
    "-g0",
    "-fstack-protector-strong",
    "-D_FORTIFY_SOURCE=2",
    "-fPIE",
    "-fno-plt",
    "-Wall",
    "-Wextra",
    "-Wformat",
    "-Wformat-security",
    "-Werror=format-security",
    "-fstack-clash-protection",
    "-DFIELD_MESH=1",
    "-DFIELD_ONE=1",
    "-DHOSTESS7_AUTHORITY=1",
    "-DG16_HARD=1",
    "-DG16_NO_EXPLOIT=1",
]
HARD_LDFLAGS = ["-pie", "-Wl,-z,relro", "-Wl,-z,now", "-Wl,-z,noexecstack"]


def _which_cc() -> str:
    g16 = GROK16 / "bin" / "g16"
    if g16.is_file() and os.access(g16, os.X_OK):
        return str(g16)
    for c in ("gcc", "clang", "cc"):
        w = shutil.which(c)
        if w:
            return w
    return "gcc"


def _security_gate(content: str, *, lang: str, path: str = "") -> dict[str, Any]:
    sec = GROK16 / "lib" / "g16-code-security.py"
    if not sec.is_file():
        return {"ok": True, "blocked": False}
    import importlib.util

    spec = importlib.util.spec_from_file_location("g16_sec", sec)
    if not spec or not spec.loader:
        return {"ok": True, "blocked": False}
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.gate(content, lang=lang, path=path)


def compile_source(
    content: str,
    *,
    lang: str = "c",
    out_name: str = "a.out",
    chamber: Path | None = None,
) -> dict[str, Any]:
    gate = _security_gate(content, lang=lang, path=out_name)
    if gate.get("blocked"):
        return {
            "ok": False,
            "error": "security_gate_blocked",
            "security": gate,
            "hard": True,
        }

    chamber = chamber or Path(tempfile.mkdtemp(prefix="g16-native-"))
    chamber.mkdir(parents=True, exist_ok=True)
    ext = {".c": "c", "c": ".c", "cxx": ".cpp", "cpp": ".cpp"}.get(lang, ".c")
    if not str(ext).startswith("."):
        ext = ".c"
    src = chamber / f"src{ext if ext.startswith('.') else '.c'}"
    if lang in ("cxx", "cpp", "c++"):
        src = chamber / "src.cpp"
    src.write_text(content, encoding="utf-8")
    out = chamber / out_name

    cc = _which_cc()
    # If using g16 wrapper, it already injects hard flags — still pass extra
    argv = [cc, str(src), "-o", str(out), *HARD_CFLAGS, *HARD_LDFLAGS]
    env = {
        k: v
        for k, v in os.environ.items()
        if k not in ("LD_PRELOAD", "LD_LIBRARY_PATH", "PYTHONPATH")
    }
    env["G16_HARD"] = "1"
    env["G16_NO_EXPLOIT"] = "1"
    try:
        proc = subprocess.run(
            argv,
            capture_output=True,
            text=True,
            timeout=180,
            cwd=str(chamber),
            env=env,
            shell=False,  # NEVER True
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"ok": False, "error": str(exc)[:160], "hard": True}

    return {
        "ok": proc.returncode == 0,
        "returncode": proc.returncode,
        "stdout": (proc.stdout or "")[-4000:],
        "stderr": (proc.stderr or "")[-4000:],
        "out": str(out) if out.is_file() else None,
        "argv": argv[:6],
        "hard": True,
        "exploits": "gated",
        "shell": False,
        "security": gate,
    }


def main() -> int:
    if len(sys.argv) < 2:
        print(json.dumps({"usage": "g16-native-compile.py <source.c>", "hard": True}, indent=2))
        return 1
    p = Path(sys.argv[1])
    content = p.read_text(encoding="utf-8", errors="replace")
    print(json.dumps(compile_source(content, lang="c", out_name=p.stem), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
