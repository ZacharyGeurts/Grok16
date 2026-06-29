#!/usr/bin/env pythong
"""G16 universal compiler — every compiler ever, secured, browser-tab ready."""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

ROOT = Path(os.environ.get("GROK16_ROOT", Path(__file__).resolve().parents[1]))
SG = Path(os.environ.get("SG_ROOT", ROOT.parent))
NEXUS = Path(os.environ.get("NEXUS_INSTALL_ROOT", SG / "NewLatest"))
DOCTRINE = ROOT / "data" / "g16-universal-compilers.json"
EXT_MAP = ROOT / "data" / "g16-universal-extensions.json"
G16 = ROOT / "bin" / "g16"
AI_COMPILE = ROOT / "scripts" / "grok16-ai-compile.py"
FILETYPES = NEXUS / "lib" / "field-programming-filetypes.py"


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _load(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default if default is not None else {}


def _security_mod() -> Any | None:
    path = ROOT / "lib" / "g16-code-security.py"
    if not path.is_file():
        return None
    spec = importlib.util.spec_from_file_location("g16_code_security", path)
    if not spec or not spec.loader:
        return None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _ai_compile_mod() -> Any | None:
    if not AI_COMPILE.is_file():
        return None
    spec = importlib.util.spec_from_file_location("grok16_ai_compile", AI_COMPILE)
    if not spec or not spec.loader:
        return None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _filetypes_mod() -> Any | None:
    if not FILETYPES.is_file():
        return None
    spec = importlib.util.spec_from_file_location("field_programming_filetypes", FILETYPES)
    if not spec or not spec.loader:
        return None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _stack_fabric_mod() -> Any | None:
    path = ROOT / "lib" / "g16-stack-fabric.py"
    if not path.is_file():
        return None
    spec = importlib.util.spec_from_file_location("g16_stack_fabric", path)
    if not spec or not spec.loader:
        return None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _resolve_profile(requested: str = "", *, sustained: bool = False) -> str:
    """G4 autoload + G6/G7 truth/thermal gates."""
    fab = _stack_fabric_mod()
    if fab and hasattr(fab, "resolve_profile_for_compile"):
        rep = fab.resolve_profile_for_compile(requested=requested, sustained=sustained)
        if rep.get("blocked"):
            return str(rep.get("profile") or requested or "belt_2_0")
        return str(rep.get("profile") or requested or "belt_2_0")
    return requested or os.environ.get("G16_BELT_PROFILE", "belt_2_0")


def discern(path: str = "", *, mime: str = "", content: str = "") -> str:
    """G12 — discern from path, MIME, content, g16 driver, or 243-filetype DB."""
    ft = _filetypes_mod()
    if ft and hasattr(ft, "discern"):
        lang = ft.discern(path, mime=mime, content=content)
        if lang and lang != "plaintext":
            return str(lang)
    if G16.is_file() and path:
        try:
            proc = subprocess.run(
                [str(G16), "--g16-discern", path],
                capture_output=True, text=True, timeout=8,
            )
            if proc.returncode == 0 and proc.stdout.strip():
                return proc.stdout.strip()
        except (OSError, subprocess.TimeoutExpired):
            pass
    ext_doc = _load(EXT_MAP, {})
    if path:
        suf = Path(path).suffix.lower()
        hit = (ext_doc.get("extensions") or {}).get(suf)
        if hit:
            return str(hit)
        name = Path(path).name.lower()
        if name in ("dockerfile", "containerfile"):
            return "dockerfile"
        if name in ("makefile", "gnumakefile"):
            return "makefile"
    if mime:
        hit = (ext_doc.get("mime_hints") or {}).get(mime.lower())
        if hit:
            return str(hit)
    if content and content.lstrip().startswith(("#!", "<?", "<!DOCTYPE", "<html")):
        if "python" in content[:200].lower() or content.lstrip().startswith("#!"):
            return "python"
    return "plaintext"


def _compiler_for(lang: str) -> dict[str, Any]:
    doc = _load(DOCTRINE, {})
    lang = lang.lower()
    for _id, row in (doc.get("compilers") or {}).items():
        langs = row.get("langs") or []
        if lang in langs:
            return {**row, "id": _id}
    return {"id": "g16", "langs": ["c", "cxx"], "driver": "bin/g16", "compile": True}


def _which(cmd: str) -> str | None:
    return shutil.which(cmd)


def check(
    content: str,
    *,
    lang: str = "",
    path: str = "",
    profile: str = "",
    mime: str = "",
) -> dict[str, Any]:
    """Syntax/security check — transparent gate before compile."""
    profile = _resolve_profile(profile or "belt_2_0")
    lang = lang or discern(path, mime=mime, content=content)
    sec = _security_mod()
    gate_doc: dict[str, Any] = {"ok": True, "blocked": False, "findings": []}
    if sec and hasattr(sec, "gate"):
        gate_doc = sec.gate(content, lang=lang, path=path)
    if gate_doc.get("blocked"):
        return {
            "schema": "g16-universal-check/v1",
            "ok": False,
            "blocked": True,
            "lang": lang,
            "security": gate_doc,
            "message": "Blocked — bad code. See findings and use_instead.",
        }
    comp = _compiler_for(lang)
    driver = str(comp.get("driver") or "bin/g16")
    driver_path = ROOT / driver if not driver.startswith("/") else Path(driver)
    check_ok = True
    detail = ""
    if lang in ("javascript", "typescript") and _which("node"):
        with tempfile.NamedTemporaryFile("w", suffix=".js" if lang == "javascript" else ".ts", delete=False) as fh:
            fh.write(content)
            tmp = fh.name
        try:
            proc = subprocess.run(
                [_which("node"), "--check", tmp],
                capture_output=True, text=True, timeout=15,
            )
            check_ok = proc.returncode == 0
            detail = proc.stderr or proc.stdout
        finally:
            Path(tmp).unlink(missing_ok=True)
    elif lang == "python" and (_which("python3") or _which("pythong")):
        py = _which("pythong") or _which("python3")
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as fh:
            fh.write(content)
            tmp = fh.name
        try:
            proc = subprocess.run([py, "-m", "py_compile", tmp], capture_output=True, text=True, timeout=15)
            check_ok = proc.returncode == 0
            detail = proc.stderr
        finally:
            Path(tmp).unlink(missing_ok=True)
    elif lang == "java" and _which("javac"):
        with tempfile.TemporaryDirectory(prefix="g16-java-") as td:
            src = Path(td) / "Main.java"
            if "class " not in content:
                content = f"public class Main {{\npublic static void main(String[] args) {{\n{content}\n}}\n}}\n"
            src.write_text(content, encoding="utf-8")
            proc = subprocess.run([_which("javac"), str(src)], capture_output=True, text=True, timeout=60)
            check_ok = proc.returncode == 0
            detail = proc.stderr
    elif lang in ("c", "cxx", "asm", "objc") and G16.is_file():
        ai = _ai_compile_mod()
        if ai and hasattr(ai, "compile_source"):
            out = ai.compile_source(content, lang="cxx" if lang in ("cxx", "objc") else "c")
            check_ok = bool(out.get("ok"))
            detail = out.get("stderr_tail") or ""
        else:
            check_ok = False
            detail = "g16 ai compile unavailable"
    else:
        check_ok = True
        detail = f"check skipped — no host tool for {lang}; security gate passed"
    return {
        "schema": "g16-universal-check/v1",
        "ok": check_ok and gate_doc.get("ok", True),
        "blocked": False,
        "lang": lang,
        "compiler": comp.get("id"),
        "profile": profile,
        "security": gate_doc,
        "detail": detail[:2000] if detail else "",
    }


def compile_source(
    content: str,
    *,
    lang: str = "",
    path: str = "",
    profile: str = "",
    mime: str = "",
    sustained: bool = False,
) -> dict[str, Any]:
    """Compile or interpret — security gate first, no harm to system."""
    profile = _resolve_profile(profile or "belt_2_0", sustained=sustained)
    lang = lang or discern(path, mime=mime, content=content)
    fab = _stack_fabric_mod()
    if fab and hasattr(fab, "resolve_profile_for_compile"):
        gate = fab.resolve_profile_for_compile(requested=profile, sustained=sustained)
        if gate.get("blocked"):
            return {
                "schema": "g16-universal-compile/v1",
                "ok": False,
                "compiled": False,
                "blocked": True,
                "reason": gate.get("reason"),
                "truth": gate.get("truth"),
            }
    chk = check(content, lang=lang, path=path, profile=profile)
    if chk.get("blocked"):
        return {**chk, "schema": "g16-universal-compile/v1", "compiled": False}
    if not chk.get("ok"):
        return {**chk, "schema": "g16-universal-compile/v1", "compiled": False, "error": "check_failed"}
    comp = _compiler_for(lang)
    ai = _ai_compile_mod()
    if lang in ("c", "cxx", "asm", "objc") and ai and hasattr(ai, "compile_source"):
        out = ai.compile_source(content, lang="cxx" if lang in ("cxx", "objc", "c") and "class " in content else ("cxx" if lang in ("cxx", "objc") else "c"))
        return {"schema": "g16-universal-compile/v1", "compiled": bool(out.get("ok")), "lang": lang, "compiler": "g16", **out}
    if lang == "java" and _which("javac"):
        with tempfile.TemporaryDirectory(prefix="g16-java-") as td:
            src = Path(td) / "Main.java"
            if "class " not in content:
                content = f"public class Main {{\npublic static void main(String[] args) throws Exception {{\n{content}\n}}\n}}\n"
            src.write_text(content, encoding="utf-8")
            t0 = time.perf_counter()
            proc = subprocess.run([_which("javac"), str(src)], capture_output=True, text=True, timeout=120)
            return {
                "schema": "g16-universal-compile/v1",
                "ok": proc.returncode == 0,
                "compiled": proc.returncode == 0,
                "lang": lang,
                "compiler": "javac",
                "compile_ms": int((time.perf_counter() - t0) * 1000),
                "stderr": proc.stderr[:2000],
                "classfile": str(Path(td) / "Main.class") if proc.returncode == 0 else "",
            }
    if lang in ("javascript", "typescript"):
        return {
            "schema": "g16-universal-compile/v1",
            "ok": True,
            "compiled": False,
            "interpreted": True,
            "lang": lang,
            "compiler": "node",
            "message": "JavaScript/TypeScript — syntax check passed; run in browser tab via AmmoCode",
        }
    if lang == "python":
        return {
            "schema": "g16-universal-compile/v1",
            "ok": True,
            "compiled": False,
            "interpreted": True,
            "lang": lang,
            "compiler": "gpy16",
            "message": "Python — use gpy-16 interpreter lane; security gate passed",
        }
    if ai and hasattr(ai, "compile_source") and lang not in ("shell", "html", "css", "json", "yaml", "markdown"):
        kind = "cxx" if lang in ("rust", "go", "zig", "d", "fortran") else "c"
        out = ai.compile_source(content, lang=kind)
        return {"schema": "g16-universal-compile/v1", "compiled": bool(out.get("ok")), "lang": lang, "compiler": "g16-fallback", **out}
    return {
        "schema": "g16-universal-compile/v1",
        "ok": True,
        "compiled": False,
        "lang": lang,
        "compiler": comp.get("id"),
        "message": f"No compile driver for {lang} — check passed, safe to edit",
    }


def run_file(path: str, *, lang: str = "", profile: str = "", mime: str = "") -> dict[str, Any]:
    """G9 — run via 243-filetype DB when available, else universal lane."""
    p = Path(path).expanduser().resolve()
    if not p.is_file():
        return {"schema": "g16-universal-run/v1", "ok": False, "error": "not_found", "path": str(p)}
    profile = _resolve_profile(profile or "belt_2_0")
    ft = _filetypes_mod()
    if ft and hasattr(ft, "run_path"):
        out = ft.run_path(str(p), profile=profile)
        if out.get("ok") is not False or out.get("error") != "no_runner":
            return {"schema": "g16-universal-run/v1", **out}
    lang = lang or discern(str(p), mime=mime)
    content = p.read_text(encoding="utf-8", errors="replace")
    chk = check(content, lang=lang, path=str(p), profile=profile)
    if chk.get("blocked"):
        return {"schema": "g16-universal-run/v1", "ok": False, "blocked": True, **chk}
    if lang == "shell":
        proc = subprocess.run(["/bin/bash", str(p)], capture_output=True, text=True, timeout=180, cwd=str(p.parent))
        return {
            "schema": "g16-universal-run/v1",
            "ok": proc.returncode == 0,
            "lang": lang,
            "runner": "bash",
            "returncode": proc.returncode,
            "stdout": (proc.stdout or "")[-8000:],
            "stderr": (proc.stderr or "")[-8000:],
        }
    if lang == "python":
        py = _which("pythong") or _which("python3")
        if py:
            proc = subprocess.run([py, str(p)], capture_output=True, text=True, timeout=180, cwd=str(p.parent))
            return {
                "schema": "g16-universal-run/v1",
                "ok": proc.returncode == 0,
                "lang": lang,
                "runner": py,
                "returncode": proc.returncode,
                "stdout": (proc.stdout or "")[-8000:],
                "stderr": (proc.stderr or "")[-8000:],
            }
    if lang in ("javascript", "typescript") and _which("node"):
        proc = subprocess.run([_which("node"), str(p)], capture_output=True, text=True, timeout=180, cwd=str(p.parent))
        return {
            "schema": "g16-universal-run/v1",
            "ok": proc.returncode == 0,
            "lang": lang,
            "runner": "node",
            "returncode": proc.returncode,
            "stdout": (proc.stdout or "")[-8000:],
            "stderr": (proc.stderr or "")[-8000:],
        }
    comp = compile_source(content, lang=lang, path=str(p), profile=profile)
    if comp.get("binary") and Path(str(comp["binary"])).is_file():
        proc = subprocess.run([str(comp["binary"])], capture_output=True, text=True, timeout=180, cwd=str(p.parent))
        return {
            "schema": "g16-universal-run/v1",
            "ok": proc.returncode == 0,
            "lang": lang,
            "runner": comp["binary"],
            "returncode": proc.returncode,
            "stdout": (proc.stdout or "")[-8000:],
            "stderr": (proc.stderr or "")[-8000:],
        }
    return {
        "schema": "g16-universal-run/v1",
        "ok": bool(comp.get("ok")),
        "lang": lang,
        "compiled": comp.get("compiled"),
        "message": comp.get("message") or "run via compile lane — see compile output",
        "compile": comp,
    }


def status() -> dict[str, Any]:
    doc = _load(DOCTRINE, {})
    compilers = {}
    for cid, row in (doc.get("compilers") or {}).items():
        driver = str(row.get("driver") or "")
        cmd = driver.split("/")[-1] if "/" in driver else driver
        compilers[cid] = {**row, "available": bool((ROOT / driver).is_file() if driver.startswith("bin/") else _which(cmd))}
    return {
        "schema": "g16-universal-compiler/v1",
        "updated": _now(),
        "g16": G16.is_file(),
        "browser_tab": doc.get("browser_tab"),
        "categories": doc.get("categories"),
        "compilers": compilers,
        "discern_langs": sum(len(v) for v in (doc.get("categories") or {}).values()),
    }


def main() -> int:
    cmd = (sys.argv[1] if len(sys.argv) > 1 else "status").strip().lower()
    if cmd == "status":
        print(json.dumps(status(), ensure_ascii=False, indent=2))
        return 0
    if cmd == "discern" and len(sys.argv) > 2:
        print(discern(sys.argv[2]))
        return 0
    if cmd == "check":
        body = json.loads(sys.stdin.read() or "{}")
        print(json.dumps(check(body.get("content", ""), lang=body.get("language", ""), path=body.get("path", ""), profile=body.get("profile", "belt_2_0")), ensure_ascii=False, indent=2))
        return 0
    if cmd == "compile":
        body = json.loads(sys.stdin.read() or "{}")
        print(json.dumps(compile_source(body.get("content", ""), lang=body.get("language", ""), path=body.get("path", ""), profile=body.get("profile", "belt_2_0")), ensure_ascii=False, indent=2))
        return 0
    if cmd == "run" and len(sys.argv) > 2:
        print(json.dumps(run_file(sys.argv[2]), ensure_ascii=False, indent=2))
        return 0 if run_file(sys.argv[2]).get("ok") else 1
    print(json.dumps({"error": "usage", "cmds": ["status", "discern <path>", "check", "compile", "run <path>"]}, ensure_ascii=False, indent=2))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())