#!/usr/bin/env python3
# Grok16 HARD · ironclad:g16-python-harden:2 · exploits DISPERMITTED · soft-kill FORBIDDEN
"""Grok16 RTX gate — foreign NVIDIA/RTX path DISPERMITTED on Field plane.

We do not open RTX/foreign GPU exploit surface. Field mesh only.

  python3 Grok16/forge/rtx_gate.py seal
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GROK16 = Path(os.environ.get("GROK16_ROOT", Path(__file__).resolve().parents[1]))
INSTALL = Path(os.environ.get("NEXUS_INSTALL_ROOT", GROK16.parent))
STATE = Path(os.environ.get("NEXUS_STATE_DIR", INSTALL / ".nexus-state"))
PANEL = STATE / "g16-rtx-gate-panel.json"
IRONCLAD = "ironclad:g16-rtx-gate:2"


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def seal() -> dict[str, Any]:
    # Force closed unless explicit Field permit (default: dispermitted)
    permit = os.environ.get("NEXUS_RTX_PERMIT", "0").strip().lower() in ("1", "true", "yes")
    panel = {
        "schema": "g16-rtx-gate/v2",
        "updated": _utc(),
        "ok": True,
        "rtx": "DISPERMITTED" if not permit else "PERMITTED_EXPLICIT",
        "nvidia": "DISPERMITTED",
        "foreign_gpu": "DISPERMITTED",
        "permit_env": "NEXUS_RTX_PERMIT",
        "open": bool(permit),
        "hard": True,
        "reason": "No foreign RTX/NVIDIA exploit surface on default Field Grok16 plane",
        "ironclad_cite": IRONCLAD,
        "motto": "RTX gate CLOSED · Field-only · no foreign GPU inject",
    }
    PANEL.parent.mkdir(parents=True, exist_ok=True)
    PANEL.write_text(json.dumps(panel, indent=2) + "\n", encoding="utf-8")
    return panel


def main() -> int:
    print(json.dumps(seal(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
