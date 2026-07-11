#!/usr/bin/env python3
# Grok16 HARD · ironclad:g16-python-harden:2 · exploits DISPERMITTED · soft-kill FORBIDDEN
"""Grok16 hard linker doctrine — RELRO/NOW/PIE/noexecstack only.

  python3 Grok16/forge/g16-linker.py seal
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
PANEL = STATE / "g16-linker-panel.json"
DOCTRINE = GROK16 / "data" / "g16-linker-doctrine.json"
IRONCLAD = "ironclad:g16-linker:2"

HARD_LDFLAGS = [
    "-pie",
    "-Wl,-z,relro",
    "-Wl,-z,now",
    "-Wl,-z,noexecstack",
    "-Wl,--as-needed",
]


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def seal() -> dict[str, Any]:
    doctrine = {
        "schema": "g16-linker-doctrine/v2",
        "updated": _utc(),
        "hard": True,
        "better": True,
        "ldflags": HARD_LDFLAGS,
        "forbid": ["--export-dynamic-untrusted", "rpath_untrusted", "lazy_bind_only"],
        "relro": "full",
        "now": True,
        "noexecstack": True,
        "pie": True,
        "exploits": "DISPERMITTED",
        "ironclad_cite": IRONCLAD,
        "motto": "Hard linker · full RELRO · NOW · PIE · noexecstack",
    }
    DOCTRINE.parent.mkdir(parents=True, exist_ok=True)
    DOCTRINE.write_text(json.dumps(doctrine, indent=2) + "\n", encoding="utf-8")
    panel = {
        "schema": "g16-linker-panel/v2",
        "updated": _utc(),
        "ok": True,
        "hard": True,
        "ldflags_n": len(HARD_LDFLAGS),
        "ldflags": HARD_LDFLAGS,
        "ironclad_cite": IRONCLAD,
        "motto": doctrine["motto"],
    }
    PANEL.parent.mkdir(parents=True, exist_ok=True)
    PANEL.write_text(json.dumps(panel, indent=2) + "\n", encoding="utf-8")
    return panel


def main() -> int:
    cmd = (sys.argv[1] if len(sys.argv) > 1 else "seal").strip().lower()
    print(json.dumps(seal(), indent=2))
    return 0 if cmd else 0


if __name__ == "__main__":
    raise SystemExit(main())
