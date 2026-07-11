#!/usr/bin/env python3
# Grok16 HARD · ironclad:g16-python-harden:2 · exploits DISPERMITTED · soft-kill FORBIDDEN
# Weapon policy: SIGKILL/INSTAKILL only on hostile Field plane — never SIGTERM authoring
"""Grok16 Python harden — rewrite Field Python to remove exploit-class patterns.

Harder throughout:
  - Strip/refuse shell=True, eval/exec on untrusted, soft-kill authoring
  - Prefer list argv subprocess, SIGKILL-only for hostiles
  - Seal Grok16 forge + lib + bin wrappers
  - Never rewrite this file or g16-code-security (self-stable)

  python3 Grok16/lib/g16-python-harden.py rewrite
  python3 Grok16/lib/g16-python-harden.py scan
  python3 Grok16/lib/g16-python-harden.py seal
  python3 Grok16/lib/g16-python-harden.py status

ironclad:g16-python-harden:2
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GROK16 = Path(os.environ.get("GROK16_ROOT", Path(__file__).resolve().parents[1]))
INSTALL = Path(os.environ.get("NEXUS_INSTALL_ROOT", GROK16.parent))
STATE = Path(os.environ.get("NEXUS_STATE_DIR", INSTALL / ".nexus-state"))
PANEL = STATE / "g16-python-harden-panel.json"
LEDGER = STATE / "g16-python-harden-ledger.jsonl"
SEAL = STATE / "g16-python-harden.forever"
IRONCLAD = "ironclad:g16-python-harden:2"
SCHEMA = "g16-python-harden/v2"
VERSION = "16.1.0-hard"

# Never auto-rewrite these (they contain pattern strings / gate logic)
SKIP_NAMES = frozenset(
    {
        "g16-python-harden.py",
        "g16-code-security.py",
    }
)

HARD_HEADER = (
    "# Grok16 HARD · ironclad:g16-python-harden:2 · exploits DISPERMITTED · soft-kill FORBIDDEN\n"
    "# Weapon policy: SIGKILL/INSTAKILL only on hostile Field plane — never SIGTERM authoring\n"
)


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _save(path: Path, doc: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(doc, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    tmp.replace(path)


def _append(row: dict[str, Any]) -> None:
    try:
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        with LEDGER.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({"ts": _utc(), **row}, ensure_ascii=False, default=str) + "\n")
    except OSError:
        pass


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()[:24]


def harden_text(text: str, *, path: str = "") -> tuple[str, list[str]]:
    """Apply safe rewrites; return (new_text, applied_tags)."""
    applied: list[str] = []
    out = text

    # shell=True -> shell=False (FORBIDDEN)
    new, n = re.subn(
        r"(subprocess\.(?:run|Popen|call|check_call|check_output)\([^)]*?)shell\s*=\s*True",
        r"\1shell=False  # G16-HARD: shell=True FORBIDDEN",
        out,
        flags=re.MULTILINE,
    )
    if n:
        out = new
        applied.append(f"shell_true_to_false:{n}")

    # Comment bare os.system( calls (not in strings already commented)
    new, n = re.subn(
        r"(?m)^(\s*)os\.system\(",
        r"\1# G16-HARD: os.system FORBIDDEN — use subprocess.run(argv, shell=False)\n\1# os.system(",
        out,
    )
    if n:
        out = new
        applied.append(f"os_system_comment:{n}")

    # Comment bare eval( / exec( at statement start only
    new, n = re.subn(r"(?m)^(\s*)eval\s*\(", r"\1# G16-HARD: eval FORBIDDEN\n\1# eval(", out)
    if n:
        out = new
        applied.append(f"eval_comment:{n}")
    new, n = re.subn(r"(?m)^(\s*)exec\s*\(", r"\1# G16-HARD: exec FORBIDDEN on untrusted\n\1# exec(", out)
    if n:
        out = new
        applied.append(f"exec_comment:{n}")

    # Ensure hard header once on Grok16-owned forge/lib files
    norm = path.replace("\\", "/")
    if path and ("Grok16/forge" in norm or "Grok16/lib" in norm):
        if "ironclad:g16-python-harden" not in out[:500]:
            if out.startswith("#!"):
                nl = out.find("\n")
                out = out[: nl + 1] + HARD_HEADER + out[nl + 1 :]
            else:
                out = HARD_HEADER + out
            applied.append("hard_header")
    return out, applied


def _iter_py(root: Path) -> list[Path]:
    out: list[Path] = []
    for p in root.rglob("*.py"):
        if any(x in p.parts for x in (".git", "__pycache__", "qemu-racks", "node_modules")):
            continue
        if p.name in SKIP_NAMES:
            continue
        out.append(p)
    return out


def rewrite_tree(root: Path | None = None) -> dict[str, Any]:
    root = root or GROK16
    extra = [
        INSTALL / "lib" / "g16-secure-chamber.py",
        INSTALL / "lib" / "field-g16-untouchable-binaries.py",
        INSTALL / "lib" / "field-g16-script-compile.py",
        INSTALL / "lib" / "field-g16-launch.py",
        INSTALL / "lib" / "field-g16-hard-rewrite.py",
        INSTALL / "lib" / "hostess7-g16.py",
        INSTALL / "lib" / "nexus-g16-bridge.py",
        INSTALL / "lib" / "nexus-g16-recompile.py",
    ]
    files = _iter_py(root) + [p for p in extra if p.is_file() and p.name not in SKIP_NAMES]
    changed: list[dict[str, Any]] = []
    for path in files:
        try:
            old = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        new, tags = harden_text(old, path=str(path))
        if new != old and tags:
            try:
                path.write_text(new, encoding="utf-8")
                changed.append({"path": str(path), "tags": tags, "digest": _digest(new)})
                _append({"event": "rewrite", "path": str(path), "tags": tags})
            except OSError as exc:
                changed.append({"path": str(path), "error": str(exc)[:120]})
    return {
        "schema": "g16-python-rewrite/v2",
        "updated": _utc(),
        "ok": True,
        "version": VERSION,
        "root": str(root),
        "changed_n": len([c for c in changed if "error" not in c]),
        "changed": changed[:60],
        "ironclad_cite": IRONCLAD,
    }


def scan() -> dict[str, Any]:
    sec = GROK16 / "lib" / "g16-code-security.py"
    if not sec.is_file():
        return {"ok": False, "error": "g16-code-security missing"}
    import importlib.util

    spec = importlib.util.spec_from_file_location("g16_code_security", sec)
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    g16 = mod.scan_path(GROK16)
    g16_lib_hits: list[dict[str, Any]] = []
    scanned_extra = 0
    for name in (
        "g16-secure-chamber.py",
        "field-g16-untouchable-binaries.py",
        "field-g16-script-compile.py",
        "field-g16-launch.py",
        "field-g16-hard-rewrite.py",
        "hostess7-g16.py",
        "nexus-g16-bridge.py",
        "nexus-g16-recompile.py",
    ):
        p = INSTALL / "lib" / name
        if not p.is_file():
            continue
        scanned_extra += 1
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        g = mod.gate(text, lang="python", path=str(p))
        if g.get("blocked"):
            g16_lib_hits.append({"path": name, "findings_n": g.get("findings_n")})
    return {
        "ok": True,
        "g16": g16,
        "install_g16_scanned": scanned_extra,
        "install_g16_blocked_n": len(g16_lib_hits),
        "install_g16_blocked": g16_lib_hits[:20],
        "ironclad_cite": IRONCLAD,
    }


def seal() -> dict[str, Any]:
    rew = rewrite_tree(GROK16)
    sc = scan()
    ver = {
        "schema": "grok16-version/v2",
        "version": VERSION,
        "updated": _utc(),
        "hard": True,
        "better": True,
        "exploits": "DISPERMITTED",
        "soft_kill_source": "FORBIDDEN",
        "weapon": "SIGKILL_INSTAKILL_FOREVER_on_hostile_plane",
        "ironclad_cite": IRONCLAD,
        "motto": "Grok16 HARD · better · exploit-free Python · Field Ironclad",
    }
    try:
        (GROK16 / "VERSION").write_text(VERSION + "\n", encoding="utf-8")
        (GROK16 / "data" / "g16-hard-version.json").write_text(json.dumps(ver, indent=2) + "\n", encoding="utf-8")
    except OSError:
        pass

    panel = {
        "schema": SCHEMA,
        "updated": _utc(),
        "ok": True,
        "version": VERSION,
        "hard": True,
        "better": True,
        "rewrite": {"changed_n": rew.get("changed_n"), "files": rew.get("changed")},
        "security": {
            "g16_blocked_n": (sc.get("g16") or {}).get("blocked_n"),
            "g16_scanned": (sc.get("g16") or {}).get("scanned"),
            "install_g16_blocked_n": sc.get("install_g16_blocked_n"),
        },
        "policy": {
            "exploits": "DISPERMITTED",
            "shell_true": "FORBIDDEN",
            "eval_exec": "FORBIDDEN",
            "soft_kill_source": "FORBIDDEN",
            "harder": True,
        },
        "ironclad_cite": IRONCLAD,
        "motto": ver["motto"],
        "cli": "g16-python-harden.py [rewrite|scan|seal|status]",
    }
    _save(PANEL, panel)
    SEAL.write_text(json.dumps({**ver, "sealed_at": _utc()}, indent=2) + "\n", encoding="utf-8")
    panel["sealed"] = True
    _append({"event": "seal", "version": VERSION, "changed": rew.get("changed_n")})
    return panel


def status() -> dict[str, Any]:
    if PANEL.is_file():
        try:
            doc = json.loads(PANEL.read_text(encoding="utf-8"))
            doc["seal_present"] = SEAL.is_file()
            if (GROK16 / "VERSION").is_file():
                doc["version_file"] = (GROK16 / "VERSION").read_text(encoding="utf-8").strip()
            return doc
        except (OSError, json.JSONDecodeError):
            pass
    return seal()


def main() -> int:
    cmd = (sys.argv[1] if len(sys.argv) > 1 else "seal").strip().lower()
    if cmd in ("rewrite", "harden"):
        print(json.dumps(rewrite_tree(), indent=2, ensure_ascii=False))
        return 0
    if cmd == "scan":
        print(json.dumps(scan(), indent=2, ensure_ascii=False))
        return 0
    if cmd in ("seal", "run", "full"):
        print(json.dumps(seal(), indent=2, ensure_ascii=False))
        return 0
    if cmd in ("status", "panel"):
        print(json.dumps(status(), indent=2, ensure_ascii=False))
        return 0
    print(json.dumps(seal(), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
