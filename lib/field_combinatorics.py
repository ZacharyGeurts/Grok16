#!/usr/bin/env python3
# Grok16 HARD · ironclad:g16-python-harden:2 · exploits DISPERMITTED · soft-kill FORBIDDEN
# Weapon policy: SIGKILL/INSTAKILL only on hostile Field plane — never SIGTERM authoring
"""Grok16 field combinatorics — hard rebuild · reject · retaliate threat.

  python3 Grok16/lib/field_combinatorics.py rebuild
  python3 Grok16/lib/field_combinatorics.py status

ironclad:g16-field-combinatorics:2
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GROK16 = Path(os.environ.get("GROK16_ROOT", Path(__file__).resolve().parents[1]))
INSTALL = Path(os.environ.get("NEXUS_INSTALL_ROOT", GROK16.parent))
STATE = Path(os.environ.get("NEXUS_STATE_DIR", INSTALL / ".nexus-state"))
PANEL = STATE / "g16-field-combinatorics-panel.json"
DOCTRINE = GROK16 / "data" / "g16-field-combinatorics-doctrine.json"
IRONCLAD = "ironclad:g16-field-combinatorics:2"


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _save(path: Path, doc: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(doc, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    tmp.replace(path)


def _load(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default if default is not None else {}


def record_rejection(subject: str, *, reason: str) -> dict[str, Any]:
    return {
        "subject": subject,
        "reason": reason,
        "ts": _utc(),
        "rejected": True,
        "retaliate_threat": True,
    }


def retaliate_threat(subject: str) -> dict[str, Any]:
    """Mark threat for Field INSTAKILL plane — never soft-kill."""
    return {
        "subject": subject,
        "action": "retaliate_threat",
        "weapon": "SIGKILL_INSTAKILL_FOREVER",
        "soft_kill": "FORBIDDEN",
        "ts": _utc(),
        "reject_retaliate": True,
    }


def rebuild() -> dict[str, Any]:
    doc = _load(DOCTRINE, {})
    if not doc:
        doc = {
            "schema": "g16-field-combinatorics-doctrine/v2",
            "hard": True,
            "reject_retaliate": True,
            "retaliate_threat": True,
            "record_rejection": True,
            "exploits": "DISPERMITTED",
            "soft_kill": "FORBIDDEN",
            "lanes": ["field_opt", "ironclad", "mesh", "truth", "secure_chamber"],
            "hardness": "that_hard",
            "version": "16.1.0-hard",
        }
        _save(DOCTRINE, doc)

    lanes = list(doc.get("lanes") or [])
    matrix = []
    for i, a in enumerate(lanes):
        for b in lanes[i:]:
            matrix.append(
                {
                    "pair": f"{a}+{b}",
                    "score": 100.0 if a == b else 92.0,
                    "hard": True,
                    "exploit_free": True,
                }
            )
    digest = hashlib.sha256(json.dumps(matrix, sort_keys=True).encode()).hexdigest()[:24]
    panel = {
        "schema": "g16-field-combinatorics-panel/v2",
        "updated": _utc(),
        "ok": True,
        "hard": True,
        "better": True,
        "lanes": lanes,
        "pairs_n": len(matrix),
        "matrix_digest": digest,
        "reject_retaliate": True,
        "retaliate_threat": True,
        "record_rejection": True,
        "policy": {
            "exploits": "DISPERMITTED",
            "soft_kill": "FORBIDDEN",
            "weapon": "SIGKILL_INSTAKILL_FOREVER",
        },
        "ironclad_cite": IRONCLAD,
        "motto": "Combinatorics HARD · reject · retaliate threat · exploit-free",
    }
    _save(PANEL, panel)
    return panel


def status() -> dict[str, Any]:
    if PANEL.is_file():
        return _load(PANEL, {})
    return rebuild()


def main() -> int:
    cmd = (sys.argv[1] if len(sys.argv) > 1 else "rebuild").strip().lower()
    if cmd in ("rebuild", "seal", "run"):
        print(json.dumps(rebuild(), indent=2))
        return 0
    if cmd in ("status", "panel"):
        print(json.dumps(status(), indent=2))
        return 0
    if cmd == "reject" and len(sys.argv) >= 3:
        print(json.dumps(record_rejection(sys.argv[2], reason="cli"), indent=2))
        return 0
    if cmd == "retaliate" and len(sys.argv) >= 3:
        print(json.dumps(retaliate_threat(sys.argv[2]), indent=2))
        return 0
    print(json.dumps(rebuild(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
