#!/usr/bin/env python3
# Grok16 HARD · ironclad:g16-python-harden:2 · exploits DISPERMITTED · soft-kill FORBIDDEN
# Weapon policy: SIGKILL/INSTAKILL only on hostile Field plane — never SIGTERM authoring
"""Grok16 code security gate — block exploit-class source before compile/run.

Harder throughout. No eval of untrusted code. No shell=True paths here.
Field Ironclad · INSTAKILL policy for hostiles is Hostess7 plane (not this gate).

  python3 Grok16/lib/g16-code-security.py gate <file>
  python3 Grok16/lib/g16-code-security.py scan <path>
  python3 Grok16/lib/g16-code-security.py status

ironclad:g16-code-security:2
"""
from __future__ import annotations

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
PANEL = STATE / "g16-code-security-panel.json"
LEDGER = STATE / "g16-code-security-ledger.jsonl"
IRONCLAD = "ironclad:g16-code-security:2"
SCHEMA = "g16-code-security/v2"

# Exploit-class patterns — BLOCK (source never compiles/runs in chamber)
BLOCK_PATTERNS: list[tuple[str, str, str]] = [
    # Python / dynamic code
    (r"\beval\s*\(", "eval", "dynamic_eval"),
    (r"\bexec\s*\(", "exec", "dynamic_exec"),
    (r"\bcompile\s*\([^)]*['\"]exec['\"]", "compile_exec", "dynamic_compile"),
    (r"\b__import__\s*\(", "__import__", "dynamic_import"),
    (r"\bimportlib\.import_module\s*\(", "importlib", "dynamic_import"),
    (r"\bpickle\.loads?\s*\(", "pickle", "deser_rce"),
    (r"\bmarshal\.loads?\s*\(", "marshal", "deser_rce"),
    (r"\byaml\.load\s*\((?!.*Loader)", "yaml_load", "deser_rce"),
    (r"\bshelve\.open\s*\(", "shelve", "deser_rce"),
    # Process / shell
    (r"shell\s*=\s*True", "shell_true", "command_injection"),
    (r"\bos\.system\s*\(", "os.system", "command_injection"),
    (r"\bos\.popen\s*\(", "os.popen", "command_injection"),
    (r"\bcommands\.getoutput\s*\(", "commands", "command_injection"),
    (r"subprocess\.[A-Za-z]+\([^)]*shell\s*=\s*True", "subprocess_shell", "command_injection"),
    # Preload / memory / low-level
    # Setting preload to a value is hostile; scrubbing/unsetting is allowed in defense
    (r'LD_PRELOAD\s*=\s*["\'][^"\']+["\']', "LD_PRELOAD_set", "preload_inject"),
    (r"export\s+LD_PRELOAD=", "LD_PRELOAD_export", "preload_inject"),
    (r"ld\.so\.preload", "ld_so_preload", "preload_inject"),
    (r"\bptrace\s*\(", "ptrace", "debug_inject"),
    (r"PTRACE_ATTACH", "PTRACE_ATTACH", "debug_inject"),
    (r"process_vm_writev", "process_vm_writev", "mem_inject"),
    (r"/dev/mem\b", "dev_mem", "mem_inject"),
    (r"\bwrmsr\b", "wrmsr", "cpu_inject"),
    (r"\brdmsr\b", "rdmsr", "cpu_inject"),
    # Reverse shells / net
    (r"/dev/tcp/", "dev_tcp", "reverse_shell"),
    (r"bash\s+-i\s*>?\s*&?\s*/dev/tcp", "bash_rev", "reverse_shell"),
    (r"\bncat\s+-e\b", "ncat_e", "reverse_shell"),
    (r"\bnc\s+-e\b", "nc_e", "reverse_shell"),
    (r"socket\.socket\s*\([^)]*\)\s*\.connect", "socket_connect", "network_probe"),
    # Soft-kill inject class (we INSTAKILL; never author soft-kill tools)
    (r"signal\.SIGTERM", "SIGTERM", "soft_kill_inject"),
    (r"kill\s+-15\b", "kill_15", "soft_kill_inject"),
    (r"kill\s+-TERM\b", "kill_TERM", "soft_kill_inject"),
    (r"sleep\s+30\s*[;&].*kill", "sleep_30_kill", "delayed_sigterm_inject"),
    # Classic exploit kits
    (r"\bmeterpreter\b", "meterpreter", "exploit_kit"),
    (r"\bmsfconsole\b", "msfconsole", "exploit_kit"),
    (r"\bcobaltstrike\b", "cobaltstrike", "exploit_kit"),
    # C/C++ dangerous
    (r"\bgets\s*\(", "gets", "buffer_overflow"),
    (r"\bstrcpy\s*\(", "strcpy", "buffer_overflow"),
    (r"\bsprintf\s*\([^,]*,\s*[^,\"]*[^%][^,\"]*,", "sprintf", "buffer_overflow"),
    (r"\bsystem\s*\(\s*[\"']", "c_system", "command_injection"),
]

# Allowlist: Field defense modules may mention SIGTERM in comments/protection lists
ALLOW_PATH_SUBSTR = (
    "g16-code-security",
    "g16-python-harden",
    "g16-native-compile",
    "g16-ironclad",
    "g16-linker",
    "rtx_gate",
    "field_combinatorics",
    "field_truth_blocks",
    "field-g16-hard-rewrite",
    "field-sigterm-inject-harden",
    "hostess7-rack-justice",
    "hostess7-sigterm-inject",
    "kilroy-ipxe-fortress",
    "g16-hard-core",
    "g16-secure-chamber",
)


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _append(row: dict[str, Any]) -> None:
    try:
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        with LEDGER.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({"ts": _utc(), **row}, ensure_ascii=False) + "\n")
    except OSError:
        pass


def _path_allowed(path: str) -> bool:
    low = (path or "").lower()
    return any(a in low for a in ALLOW_PATH_SUBSTR)


def gate(content: str, *, lang: str = "python", path: str = "") -> dict[str, Any]:
    """Return {ok, blocked, findings[]} — blocked=True means refuse compile/run."""
    findings: list[dict[str, Any]] = []
    text = content or ""
    if _path_allowed(path):
        return {
            "ok": True,
            "blocked": False,
            "findings": [],
            "lang": lang,
            "path": path,
            "allowlisted": True,
            "ironclad_cite": IRONCLAD,
        }

    for pattern, name, klass in BLOCK_PATTERNS:
        try:
            for m in re.finditer(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                # Soft allow comment-only for defense docs
                line_start = text.rfind("\n", 0, m.start()) + 1
                line = text[line_start : text.find("\n", m.start())]
                stripped = line.lstrip()
                if stripped.startswith("#") and klass in ("soft_kill_inject", "delayed_sigterm_inject"):
                    if any(w in line.lower() for w in ("forbid", "ban", "never", "ignore", "policy")):
                        continue
                findings.append(
                    {
                        "name": name,
                        "class": klass,
                        "span": [m.start(), m.end()],
                        "snippet": text[max(0, m.start() - 20) : m.end() + 20][:120],
                    }
                )
        except re.error:
            continue

    blocked = len(findings) > 0
    out = {
        "ok": not blocked,
        "blocked": blocked,
        "findings": findings[:40],
        "findings_n": len(findings),
        "lang": lang,
        "path": path,
        "policy": "exploit_class_BLOCK · soft_kill_source_BLOCK · field_hard",
        "weapon_hint": "Hostess7 INSTAKILL FOREVER on live hostiles — this gate blocks source only",
        "ironclad_cite": IRONCLAD,
        "schema": "g16-security-gate/v2",
    }
    if blocked:
        _append({"event": "gate_block", "path": path, "lang": lang, "n": len(findings)})
    return out


def scan_path(root: Path) -> dict[str, Any]:
    root = Path(root)
    blocked_files: list[dict[str, Any]] = []
    scanned = 0
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".py", ".c", ".cpp", ".h", ".cc", ".rs", ".go", ".sh", ".js"}:
            continue
        if any(x in path.parts for x in (".git", "__pycache__", "node_modules", "qemu-racks")):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        scanned += 1
        lang = "python" if path.suffix == ".py" else path.suffix.lstrip(".")
        g = gate(text, lang=lang, path=str(path))
        if g.get("blocked"):
            blocked_files.append(
                {
                    "path": str(path.relative_to(root)) if str(path).startswith(str(root)) else str(path),
                    "findings_n": g.get("findings_n"),
                    "classes": sorted({f.get("class") for f in g.get("findings") or []}),
                }
            )
    doc = {
        "schema": SCHEMA,
        "updated": _utc(),
        "ok": True,
        "root": str(root),
        "scanned": scanned,
        "blocked_n": len(blocked_files),
        "blocked": blocked_files[:80],
        "ironclad_cite": IRONCLAD,
        "motto": "Grok16 security gate · exploits blocked · harder throughout",
    }
    try:
        PANEL.parent.mkdir(parents=True, exist_ok=True)
        PANEL.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    except OSError:
        pass
    return doc


def main() -> int:
    cmd = (sys.argv[1] if len(sys.argv) > 1 else "status").strip().lower()
    if cmd == "gate" and len(sys.argv) >= 3:
        p = Path(sys.argv[2])
        text = p.read_text(encoding="utf-8", errors="replace") if p.is_file() else ""
        print(json.dumps(gate(text, path=str(p)), indent=2))
        return 0 if not gate(text, path=str(p)).get("blocked") else 2
    if cmd == "scan":
        root = Path(sys.argv[2]) if len(sys.argv) >= 3 else GROK16
        print(json.dumps(scan_path(root), indent=2))
        return 0
    if cmd in ("status", "panel"):
        if PANEL.is_file():
            print(PANEL.read_text(encoding="utf-8"))
        else:
            print(json.dumps(scan_path(GROK16), indent=2))
        return 0
    print(json.dumps({"usage": ["gate <file>", "scan [path]", "status"], "ironclad_cite": IRONCLAD}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
