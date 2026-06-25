#!/usr/bin/env python3
"""Emit CXX/LINK flags for a Grok16 profile (used by bench and CMake wrappers)."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "forge"))
from grok16_lto import normalize_lto_flags  # noqa: E402


def main() -> int:
    root = Path(os.environ.get("GROK16_ROOT", Path(__file__).resolve().parents[1]))
    profile = sys.argv[1] if len(sys.argv) > 1 else "ai"
    kind = sys.argv[2] if len(sys.argv) > 2 else "cxx"
    path = root / "data" / "grok16-profiles.json"
    if not path.is_file():
        print("", end="")
        return 1
    doc = json.loads(path.read_text(encoding="utf-8"))
    prof = doc.get("profiles", {}).get(profile, {})
    defs = [f"-D{d}" for d in prof.get("definitions", [])]
    if kind == "link":
        print(" ".join(normalize_lto_flags(prof.get("link_flags", []))))
    elif kind == "defs":
        print(" ".join(defs))
    else:
        parts = prof.get("cxx_flags", []) + defs
        if _env_true("G16_ENABLE_PGO") and kind == "cxx_pgo_use":
            parts.extend(doc.get("pgo", {}).get("use_flags", []))
        elif _env_true("G16_ENABLE_PGO") and kind == "cxx_pgo_gen":
            parts.extend(doc.get("pgo", {}).get("generate_flags", []))
        print(" ".join(parts))
    return 0


def _env_true(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in ("1", "true", "yes", "on")


if __name__ == "__main__":
    raise SystemExit(main())