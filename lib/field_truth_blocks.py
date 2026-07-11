#!/usr/bin/env python3
# Grok16 HARD · ironclad:g16-python-harden:2 · exploits DISPERMITTED · soft-kill FORBIDDEN
# Weapon policy: SIGKILL/INSTAKILL only on hostile Field plane — never SIGTERM authoring
"""Grok16 field truth blocks — publish Ironclad TRUTH for compile plane.

  python3 Grok16/lib/field_truth_blocks.py publish
  python3 Grok16/lib/field_truth_blocks.py status

ironclad:g16-field-truth-blocks:2
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
PANEL = STATE / "g16-truth-blocks-panel.json"
BLOCKS = STATE / "g16-truth-blocks.json"
IRONCLAD = "ironclad:g16-field-truth-blocks:2"


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _save(path: Path, doc: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(doc, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    tmp.replace(path)


def publish() -> dict[str, Any]:
    blocks = [
        {
            "id": "truth_required",
            "text": "All Grok16 compile/run outputs return TRUTH or source is refused.",
            "hard": True,
        },
        {
            "id": "no_lies",
            "text": "No lies on network or systems. Lie class → EAT_SOURCE / refuse.",
            "hard": True,
        },
        {
            "id": "no_exploits",
            "text": "Exploit-class source is blocked by g16-code-security gate.",
            "hard": True,
        },
        {
            "id": "no_soft_kill",
            "text": "Soft-kill (SIGTERM) authoring is FORBIDDEN. Hostiles: INSTAKILL FOREVER.",
            "hard": True,
        },
        {
            "id": "field_one",
            "text": "Field One only. Always Field. Mesh edge SAW.",
            "hard": True,
        },
        {
            "id": "harder_better",
            "text": "Grok16 16.1.0-hard — better flags, fortify, PIE, stack protector, no-plt.",
            "hard": True,
        },
    ]
    doc = {
        "schema": "g16-truth-blocks/v2",
        "updated": _utc(),
        "ok": True,
        "blocks": blocks,
        "blocks_n": len(blocks),
        "ironclad_cite": IRONCLAD,
    }
    _save(BLOCKS, doc)
    panel = {
        "schema": "g16-truth-blocks-panel/v2",
        "updated": _utc(),
        "ok": True,
        "blocks_n": len(blocks),
        "published": True,
        "ironclad_cite": IRONCLAD,
        "motto": "Truth blocks published · Grok16 HARD",
    }
    _save(PANEL, panel)
    return panel


def status() -> dict[str, Any]:
    if PANEL.is_file():
        try:
            return json.loads(PANEL.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    return publish()


def main() -> int:
    cmd = (sys.argv[1] if len(sys.argv) > 1 else "publish").strip().lower()
    if cmd in ("publish", "seal", "run"):
        print(json.dumps(publish(), indent=2))
        return 0
    if cmd in ("status", "panel"):
        print(json.dumps(status(), indent=2))
        return 0
    print(json.dumps(publish(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
