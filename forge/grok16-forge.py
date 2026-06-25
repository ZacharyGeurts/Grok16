#!/usr/bin/env python3
"""Grok16 forge — build g16/g++16 from upstream GCC (GPLv3)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from compiler_tools import GCC_TOOLS, g16_status  # noqa: E402
from engine import ForgeContext, ForgeEngine  # noqa: E402


def forge_status() -> dict:
    ctx = ForgeContext.from_env()
    return {"product": "Grok16", "ok": True, **g16_status(ctx)}


def run_tool(tool_id: str) -> dict:
    if tool_id not in GCC_TOOLS:
        return {"ok": False, "error": f"unknown tool: {tool_id}", "tools": list(GCC_TOOLS)}
    run_fn, _check = GCC_TOOLS[tool_id]
    ctx = ForgeContext.from_env()
    engine = ForgeEngine(ctx)
    result = run_fn(ctx, engine)
    return result.to_dict()


def main() -> int:
    if len(sys.argv) >= 2 and sys.argv[1] == "status":
        print(json.dumps(forge_status(), indent=2))
        return 0
    if len(sys.argv) < 3 or sys.argv[1] != "run":
        print(json.dumps({
            "product": "Grok16",
            "usage": "grok16-forge.py status | grok16-forge.py run TOOL",
            "tools": list(GCC_TOOLS),
        }, indent=2))
        return 2
    out = run_tool(sys.argv[2])
    print(json.dumps(out, indent=2))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())