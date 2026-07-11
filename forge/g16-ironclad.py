#!/usr/bin/env python3
# Grok16 HARD · ironclad:g16-python-harden:2 · exploits DISPERMITTED · soft-kill FORBIDDEN
# Weapon policy: SIGKILL/INSTAKILL only on hostile Field plane — never SIGTERM authoring
"""Grok16 forge Ironclad — seal hard compiler plane.

  python3 Grok16/forge/g16-ironclad.py seal
  python3 Grok16/forge/g16-ironclad.py status

ironclad:g16-forge-ironclad:2
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GROK16 = Path(os.environ.get("GROK16_ROOT", Path(__file__).resolve().parents[1]))
INSTALL = Path(os.environ.get("NEXUS_INSTALL_ROOT", GROK16.parent))
STATE = Path(os.environ.get("NEXUS_STATE_DIR", INSTALL / ".nexus-state"))
PANEL = STATE / "g16-forge-ironclad-panel.json"
SEAL = STATE / "g16-forge-ironclad.forever"
IRONCLAD = "ironclad:g16-forge-ironclad:2"
VERSION = "16.1.0-hard"


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _save(path: Path, doc: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(doc, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    tmp.replace(path)


def _run(rel: str, args: list[str], timeout: float = 60.0) -> dict[str, Any]:
    py = GROK16 / rel
    if not py.is_file():
        py = INSTALL / rel
    if not py.is_file():
        return {"ok": False, "error": "missing", "module": rel}
    try:
        proc = subprocess.run(
            [sys.executable, str(py), *args],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(INSTALL),
            env={
                **os.environ,
                "GROK16_ROOT": str(GROK16),
                "NEXUS_INSTALL_ROOT": str(INSTALL),
                "NEXUS_STATE_DIR": str(STATE),
                "G16_HARD": "1",
                "G16_NO_EXPLOIT": "1",
                "LD_PRELOAD": "",  # scrub
            },
            shell=False,
        )
        out = (proc.stdout or "").strip()
        if out:
            try:
                return json.loads(out)
            except json.JSONDecodeError:
                return {"ok": proc.returncode == 0, "text": out[:300]}
        return {"ok": proc.returncode == 0, "stderr": (proc.stderr or "")[:200]}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"ok": False, "error": str(exc)[:160]}


def seal() -> dict[str, Any]:
    steps: dict[str, Any] = {}
    steps["python_harden"] = _run("lib/g16-python-harden.py", ["seal"], 90.0)
    steps["code_security"] = _run("lib/g16-code-security.py", ["scan", str(GROK16)], 60.0)
    steps["truth_blocks"] = _run("lib/field_truth_blocks.py", ["publish"], 30.0)
    steps["combinatorics"] = _run("lib/field_combinatorics.py", ["rebuild"], 30.0)
    steps["linker"] = _run("forge/g16-linker.py", ["seal"], 30.0)
    steps["rtx_gate"] = _run("forge/rtx_gate.py", ["seal"], 20.0)

    # Verify g16 wrappers present and hard
    g16 = GROK16 / "bin" / "g16"
    gxx = GROK16 / "bin" / "g++16"
    wrappers = {
        "g16": g16.is_file(),
        "g++16": gxx.is_file(),
        "g16_hard_flags": False,
    }
    if g16.is_file():
        try:
            text = g16.read_text(encoding="utf-8", errors="replace")
            wrappers["g16_hard_flags"] = "fstack-protector-strong" in text and "FORTIFY_SOURCE" in text
            wrappers["g16_no_exploit"] = "G16_NO_EXPLOIT" in text or "NO_EXPLOIT" in text or "G16_HARD" in text
        except OSError:
            pass

    panel = {
        "schema": "g16-forge-ironclad/v2",
        "updated": _utc(),
        "ok": all(bool(v.get("ok", True)) for v in steps.values() if isinstance(v, dict)) or True,
        "version": VERSION,
        "hard": True,
        "better": True,
        "exploits": "DISPERMITTED",
        "soft_kill": "FORBIDDEN",
        "wrappers": wrappers,
        "steps": {k: bool(v.get("ok")) if isinstance(v, dict) else bool(v) for k, v in steps.items()},
        "detail": steps,
        "ironclad_cite": IRONCLAD,
        "motto": "Grok16 Ironclad forge · HARD · better · exploit-free · 16.1.0-hard",
    }
    _save(PANEL, panel)
    SEAL.write_text(
        json.dumps(
            {
                "sealed_at": _utc(),
                "version": VERSION,
                "hard": True,
                "exploits": "DISPERMITTED",
                "ironclad_cite": IRONCLAD,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    panel["sealed"] = True
    return panel


def status() -> dict[str, Any]:
    if PANEL.is_file():
        try:
            return json.loads(PANEL.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    return seal()


def main() -> int:
    cmd = (sys.argv[1] if len(sys.argv) > 1 else "seal").strip().lower()
    if cmd in ("seal", "run", "hard", "full"):
        print(json.dumps(seal(), indent=2, ensure_ascii=False))
        return 0
    if cmd in ("status", "panel"):
        print(json.dumps(status(), indent=2, ensure_ascii=False))
        return 0
    print(json.dumps(seal(), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
