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
    profile = sys.argv[1] if len(sys.argv) > 1 else _default_profile()
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
    elif kind == "source":
        src = prof.get("bench_source", "")
        if not src:
            src = doc.get("profiles", {}).get("field_opt", {}).get("bench_source", "")
        print(src)
    else:
        parts = prof.get("cxx_flags", []) + defs
        pgo = doc.get("pgo", {})
        root_s = str(root)
        if kind == "cxx_pgo_gen":
            gen = [f.replace("${GROK16_ROOT}", root_s) for f in pgo.get("generate_flags", [])]
            parts.extend(gen)
        elif kind == "cxx_pgo_use" or (_env_true("G16_ENABLE_PGO") and kind == "cxx"):
            use = [f.replace("${GROK16_ROOT}", root_s) for f in pgo.get("use_flags", [])]
            parts.extend(use)
        print(" ".join(parts))
    return 0


def _env_true(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in ("1", "true", "yes", "on")


def _default_profile() -> str:
    if _env_true("G16_FIELD_SPEED"):
        return "field_opt"
    return os.environ.get("G16_BENCH_PROFILE", "field_opt")


if __name__ == "__main__":
    raise SystemExit(main())