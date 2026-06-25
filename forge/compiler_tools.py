"""Grok16 forge — G16 compiler build (g16 / g++16 @ 16.0.0). GPLv3."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from common import fail_result, ok_result
from engine import ForgeContext, ForgeEngine, ForgeResult
from grok16_lto import resolve_lto_flag

G16_VERSION = "16.0.0"
G16_CC = "g16"
G16_CXX = "g++16"
GCC_REPO = os.environ.get("GROK16_GCC_REPO", "https://gcc.gnu.org/git/gcc.git")
# G16 field rewrite: gcc-15 tree, BASE-VER 16.0.0, g16/g++16 binary names
GCC_BRANCH = os.environ.get("GROK16_GCC_BRANCH", "releases/gcc-15")
FIELD_REWRITE = "gcc-15 → field 16.0.0 (BASE-VER + program-transform-name)"
MANIFEST_NAME = "grok16-toolchain.json"
CMAKE_FILE = "grok16-toolchain.cmake"
G16_PROGRAM_TRANSFORM = "s/^gcc$/g16/; s/^g++$/g++16/; s/^gcc-/g16-/"


def _env_true(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in ("1", "true", "yes", "on")


def _fast_rebuild() -> bool:
    return _env_true("G16_FAST_REBUILD")


def _make_env(ctx: ForgeContext, *, selfhost: bool) -> dict[str, str]:
    env = _gcc_configure_env(ctx, selfhost=selfhost)
    env["MAKEFLAGS"] = f"-j{ctx.jobs}"
    if _use_ccache():
        for key in ("CC", "CXX"):
            if key in env and not str(env[key]).startswith("ccache "):
                env[key] = f"ccache {env[key]}"
    if _env_true("G16_ENABLE_LTO"):
        extra = resolve_lto_flag()
        if not extra:
            extra = "-flto"
        env["CFLAGS"] = f"{env.get('CFLAGS', '')} {extra}".strip()
        env["CXXFLAGS"] = f"{env.get('CXXFLAGS', '')} {extra}".strip()
        env["LDFLAGS"] = f"{env.get('LDFLAGS', '')} {extra}".strip()
    return env


def _use_ccache() -> bool:
    return _env_true("GROK16_USE_CCACHE") and shutil.which("ccache") is not None


def _append_configure_speedups(argv: list[str]) -> str:
    notes: list[str] = []
    if _env_true("G16_ENABLE_LTO"):
        argv.append("--enable-lto")
        notes.append("thin-lto")
    if _fast_rebuild() or _env_true("G16_DISABLE_BOOTSTRAP"):
        if "--disable-bootstrap" not in argv:
            argv.append("--disable-bootstrap")
            notes.append("bootstrap-off")
    return ", ".join(notes) if notes else ""


def _ts() -> str:
    return datetime.now(timezone.utc).isoformat()


def gcc_src(ctx: ForgeContext) -> Path:
    override = os.environ.get("GROK16_GCC_SRC", "").strip()
    if override:
        return Path(override)
    return ctx.vendor / "gcc"


def gcc_build_dir(ctx: ForgeContext) -> Path:
    override = os.environ.get("GROK16_GCC_BUILD", "").strip()
    if override:
        return Path(override)
    return ctx.queen / "build/gcc"


def g16_prefix(ctx: ForgeContext) -> Path:
    env = os.environ.get("G16_PREFIX", "").strip()
    return Path(env) if env else ctx.queen


def g16_bin(ctx: ForgeContext, name: str) -> Path:
    return g16_prefix(ctx) / "bin" / name


def _is_real_compiler(bin_path: Path) -> bool:
    if not (bin_path.is_file() and os.access(bin_path, os.X_OK)):
        return False
    try:
        return bin_path.read_bytes()[:2] != b"#!"
    except OSError:
        return False


def _pkgversion(ctx: ForgeContext) -> str:
    override = os.environ.get("G16_PKGVERSION", "").strip()
    return override or f"Grok16-{G16_VERSION}"


def patch_gcc_field_version(ctx: ForgeContext, engine: ForgeEngine) -> None:
    base_ver = gcc_src(ctx) / "gcc/BASE-VER"
    if not base_ver.is_file():
        raise RuntimeError(f"missing {base_ver}")
    current = base_ver.read_text(encoding="utf-8").strip()
    if current != G16_VERSION:
        base_ver.write_text(G16_VERSION + "\n", encoding="utf-8")
        engine.log(f"gcc_field — patched BASE-VER {current} → {G16_VERSION}")


def apply_grok16_patches(ctx: ForgeContext, engine: ForgeEngine) -> None:
    patch = ctx.queen / "patches/gcc-base-ver-16.0.0.patch"
    src = gcc_src(ctx)
    if not patch.is_file() or not (src / ".git").is_dir():
        return
    rc = engine.run_stream(["git", "apply", "--check", str(patch)], cwd=src)
    if rc == 0:
        engine.run_stream(["git", "apply", str(patch)], cwd=src)
        engine.log(f"applied {patch.name}")


def _run_version(bin_path: Path, flag: str) -> str:
    try:
        return subprocess.check_output([str(bin_path), flag], text=True, timeout=5).strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def g16_status(ctx: ForgeContext) -> dict[str, Any]:
    gxx = g16_bin(ctx, G16_CXX)
    g16 = g16_bin(ctx, G16_CC)
    gxx_ok = gxx.is_file() and os.access(gxx, os.X_OK)
    g16_ok = g16.is_file() and os.access(g16, os.X_OK)
    stamp = read_selfhost_stamp(ctx)
    return {
        "product": "Grok16",
        "g16_version": G16_VERSION,
        "field_rewrite": FIELD_REWRITE,
        "branch": GCC_BRANCH,
        "repo": GCC_REPO,
        "src": str(gcc_src(ctx)),
        "src_ready": (gcc_src(ctx) / ".git").is_dir(),
        "prereqs_ready": check_gcc_prereqs(ctx),
        "build_dir": str(gcc_build_dir(ctx)),
        "prefix": str(g16_prefix(ctx)),
        "engine_real": _is_real_compiler(gxx) if gxx_ok else False,
        "ready": gxx_ok and g16_ok,
        "selfhosted": bool(stamp.get("selfhosted")),
        "dumpversion": _run_version(gxx, "-dumpversion") if gxx_ok else "",
        "version": _run_version(gxx, "--version").splitlines()[0] if gxx_ok else "",
        "paths": {
            "g16": str(g16) if g16_ok else "",
            "g++16": str(gxx) if gxx_ok else "",
            "cmake": str(ctx.queen / "cmake" / CMAKE_FILE),
        },
    }


def read_selfhost_stamp(ctx: ForgeContext) -> dict[str, Any]:
    path = g16_prefix(ctx) / "SELFHOST.json"
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def write_selfhost_stamp(ctx: ForgeContext, *, bootstrap: bool) -> Path:
    g16 = g16_bin(ctx, G16_CC)
    gxx = g16_bin(ctx, G16_CXX)
    doc = {
        "selfhosted": True,
        "bootstrap": bootstrap,
        "g16_version": G16_VERSION,
        "cc": str(g16),
        "cxx": str(gxx),
        "prefix": str(g16_prefix(ctx)),
        "pkgversion": _pkgversion(ctx),
        "engine_dumpversion": _run_version(gxx, "-dumpfullversion"),
        "updated": _ts(),
    }
    path = g16_prefix(ctx) / "SELFHOST.json"
    path.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    return path


def _load_profiles() -> dict[str, Any]:
    path = Path(os.environ.get("GROK16_ROOT", Path(__file__).resolve().parents[1])) / "data" / "grok16-profiles.json"
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def write_manifest(ctx: ForgeContext) -> Path:
    profiles = _load_profiles()
    doc = {
        "product": "Grok16",
        "schema": "grok16-toolchain/v1",
        "updated": _ts(),
        **g16_status(ctx),
        "cxx_std_default": profiles.get("cxx_std_default", "gnu++26"),
        "ai": profiles.get("profiles", {}).get("ai", {}),
        "profiles": profiles.get("profiles", {}),
        "speedups": {
            "jobs": ctx.jobs,
            "fast_rebuild": _fast_rebuild(),
            "lto": _env_true("G16_ENABLE_LTO"),
            "pgo": _env_true("G16_ENABLE_PGO"),
            "ccache": _use_ccache(),
            "disable_bootstrap": _fast_rebuild() or _env_true("G16_DISABLE_BOOTSTRAP"),
        },
    }
    out = ctx.queen / "data" / MANIFEST_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    return out


def write_cmake_toolchain(ctx: ForgeContext) -> Path | None:
    cc = g16_bin(ctx, G16_CC)
    cxx = g16_bin(ctx, G16_CXX)
    if not (cc.is_file() and cxx.is_file()):
        return None
    path = ctx.queen / "cmake" / CMAKE_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    prefix = g16_prefix(ctx)
    path.write_text(
        f'set(CMAKE_C_COMPILER "{cc}" CACHE FILEPATH "Grok16 G16 C compiler" FORCE)\n'
        f'set(CMAKE_CXX_COMPILER "{cxx}" CACHE FILEPATH "Grok16 G16 C++ compiler" FORCE)\n'
        f'set(WRDT_G16_VERSION "{G16_VERSION}" CACHE STRING "G16 version" FORCE)\n'
        f'set(GROK16_PREFIX "{prefix}" CACHE PATH "Grok16 install prefix" FORCE)\n',
        encoding="utf-8",
    )
    return path


def verify_g16_install(ctx: ForgeContext, engine: ForgeEngine | None = None) -> bool:
    g16 = g16_bin(ctx, G16_CC)
    gxx = g16_bin(ctx, G16_CXX)
    if not (g16.is_file() and gxx.is_file()):
        if engine:
            engine.log("g16: missing g16/g++16 in prefix")
        return False
    if not (_is_real_compiler(g16) and _is_real_compiler(gxx)):
        if engine:
            engine.log("g16: refuse shell wrappers")
        return False
    if _run_version(gxx, "-dumpversion") != G16_VERSION:
        if engine:
            engine.log(f"g16: bad dumpversion (expected {G16_VERSION})")
        return False
    prefix = g16_prefix(ctx)
    (prefix / "VERSION").write_text(
        f"GROK16={G16_VERSION}\nG16_FIELD_GCC={G16_VERSION}\n"
        f"G16_CXX=g++16\nG16_CC=g16\nG16_PREFIX={prefix}\n"
        f"PRODUCT=Grok16\nROOT={ctx.queen}\n",
        encoding="utf-8",
    )
    if engine:
        engine.log(f"g16: verified {gxx} ({_run_version(gxx, '--version').splitlines()[0]})")
    return True


install_g16 = verify_g16_install


def check_gcc_fetch(ctx: ForgeContext) -> bool:
    return (gcc_src(ctx) / ".git").is_dir()


def run_gcc_fetch(ctx: ForgeContext, engine: ForgeEngine) -> ForgeResult:
    engine.log(f"=== grok16:gcc_fetch — {GCC_BRANCH} ===")
    dest = gcc_src(ctx)
    if (dest / ".git").is_dir():
        rc = engine.run_stream(["git", "-C", str(dest), "pull", "--ff-only"])
        if rc != 0:
            return fail_result(engine, "gcc_fetch", "pull failed", rc)
    else:
        ctx.vendor.mkdir(parents=True, exist_ok=True)
        depth = os.environ.get("GROK16_CLONE_DEPTH", "1")
        rc = engine.run_stream([
            "git", "clone", f"--depth={depth}", "--branch", GCC_BRANCH, "--single-branch",
            GCC_REPO, str(dest),
        ])
        if rc != 0:
            return fail_result(engine, "gcc_fetch", "clone failed", rc)
    patch_gcc_field_version(ctx, engine)
    apply_grok16_patches(ctx, engine)
    write_manifest(ctx)
    return ok_result(engine, "gcc_fetch", GCC_BRANCH)


def check_gcc_prereqs(ctx: ForgeContext) -> bool:
    src = gcc_src(ctx)
    return (src / "gmp").is_dir() and (src / "mpfr").is_dir() and (src / "mpc").is_dir()


def run_gcc_prereqs(ctx: ForgeContext, engine: ForgeEngine) -> ForgeResult:
    src = gcc_src(ctx)
    if not (src / ".git").is_dir():
        return fail_result(engine, "gcc_prereqs", "run gcc_fetch first")
    script = src / "contrib/download_prerequisites"
    if not script.is_file():
        return fail_result(engine, "gcc_prereqs", "missing download_prerequisites")
    rc = engine.run_stream([str(script)], cwd=src, timeout=3600)
    return ok_result(engine, "gcc_prereqs") if rc == 0 else fail_result(engine, "gcc_prereqs", "failed", rc)


def _gcc_configure_argv(ctx: ForgeContext, *, selfhost: bool) -> tuple[list[str], str]:
    argv = [
        str(gcc_src(ctx) / "configure"),
        f"--prefix={g16_prefix(ctx)}",
        "--disable-multilib",
        "--enable-languages=c,c++",
        f"--with-pkgversion={_pkgversion(ctx)}",
        f"--program-transform-name={G16_PROGRAM_TRANSFORM}",
    ]
    if selfhost:
        if _fast_rebuild() or _env_true("G16_DISABLE_BOOTSTRAP"):
            argv.append("--disable-bootstrap")
            note = "bootstrap disabled"
        else:
            note = "bootstrap enabled"
    else:
        argv.append("--disable-bootstrap")
        note = "host gcc build"
    speed = _append_configure_speedups(argv)
    if speed:
        note = f"{note}; {speed}"
    return argv, note


def _compiler_for_selfhost(ctx: ForgeContext, name: str) -> Path:
    p = g16_bin(ctx, name)
    if p.is_file() and _is_real_compiler(p):
        return p
    host = shutil.which("g++" if name == G16_CXX else "gcc")
    if host:
        return Path(host)
    raise RuntimeError(f"{name} not available — run bootstrap first or install host gcc/g++")


def _gcc_configure_env(ctx: ForgeContext, *, selfhost: bool) -> dict[str, str]:
    env = os.environ.copy()
    if selfhost:
        env["CC"] = str(_compiler_for_selfhost(ctx, G16_CC))
        env["CXX"] = str(_compiler_for_selfhost(ctx, G16_CXX))
    return env


def check_gcc_configure(ctx: ForgeContext) -> bool:
    return (gcc_build_dir(ctx) / "Makefile").is_file()


def run_gcc_configure(ctx: ForgeContext, engine: ForgeEngine) -> ForgeResult:
    if not check_gcc_prereqs(ctx):
        return fail_result(engine, "gcc_configure", "run gcc_prereqs first")
    patch_gcc_field_version(ctx, engine)
    bdir = gcc_build_dir(ctx)
    if (bdir / "Makefile").is_file():
        return ok_result(engine, "gcc_configure", "skipped")
    bdir.mkdir(parents=True, exist_ok=True)
    argv, note = _gcc_configure_argv(ctx, selfhost=False)
    engine.log(f"gcc_configure — {note}")
    rc = engine.run_stream(argv, cwd=bdir, env=_gcc_configure_env(ctx, selfhost=False))
    return ok_result(engine, "gcc_configure") if rc == 0 else fail_result(engine, "gcc_configure", "failed", rc)


def run_gcc_distclean(ctx: ForgeContext, engine: ForgeEngine) -> ForgeResult:
    bdir = gcc_build_dir(ctx)
    if not bdir.exists():
        return ok_result(engine, "gcc_distclean", "no build tree")
    if (bdir / "Makefile").is_file():
        engine.run_stream(["make", "distclean"], cwd=bdir, timeout=600)
    shutil.rmtree(bdir, ignore_errors=True)
    bdir.mkdir(parents=True, exist_ok=True)
    return ok_result(engine, "gcc_distclean")


def run_gcc_configure_selfhost(ctx: ForgeContext, engine: ForgeEngine) -> ForgeResult:
    if not check_gcc_prereqs(ctx):
        return fail_result(engine, "gcc_configure_selfhost", "run gcc_prereqs first")
    patch_gcc_field_version(ctx, engine)
    try:
        cc = _compiler_for_selfhost(ctx, G16_CC)
        cxx = _compiler_for_selfhost(ctx, G16_CXX)
    except RuntimeError as exc:
        return fail_result(engine, "gcc_configure_selfhost", str(exc))
    bdir = gcc_build_dir(ctx)
    bdir.mkdir(parents=True, exist_ok=True)
    argv, note = _gcc_configure_argv(ctx, selfhost=True)
    engine.log(f"gcc_configure_selfhost — CC={cc} CXX={cxx} ({note})")
    rc = engine.run_stream(argv, cwd=bdir, env=_gcc_configure_env(ctx, selfhost=True))
    return ok_result(engine, "gcc_configure_selfhost") if rc == 0 else fail_result(engine, "gcc_configure_selfhost", "failed", rc)


def check_gcc_build(ctx: ForgeContext) -> bool:
    st = g16_status(ctx)
    return st["ready"] and st["dumpversion"] == G16_VERSION and st.get("engine_real") is True


def run_gcc_build(ctx: ForgeContext, engine: ForgeEngine) -> ForgeResult:
    bdir = gcc_build_dir(ctx)
    if not (bdir / "Makefile").is_file():
        return fail_result(engine, "gcc_build", "run gcc_configure first")
    menv = _make_env(ctx, selfhost=False)
    if engine.run_stream(["make", f"-j{ctx.jobs}"], cwd=bdir, env=menv, timeout=None) != 0:
        return fail_result(engine, "gcc_build", "make failed")
    if engine.run_stream(["make", "install"], cwd=bdir, timeout=None) != 0:
        return fail_result(engine, "gcc_build", "install failed")
    if not install_g16(ctx, engine):
        return fail_result(engine, "gcc_build", "g16 install failed")
    write_cmake_toolchain(ctx)
    write_manifest(ctx)
    return ok_result(engine, "gcc_build", g16_status(ctx).get("version", ""))


def check_gcc_rebuild(_ctx: ForgeContext) -> bool:
    return False


def run_gcc_rebuild(ctx: ForgeContext, engine: ForgeEngine) -> ForgeResult:
    mode = "fast incremental" if _fast_rebuild() else "full self-host"
    engine.log(f"=== grok16:gcc_rebuild — {mode} @ 16.0.0 ===")
    try:
        _compiler_for_selfhost(ctx, G16_CC)
        _compiler_for_selfhost(ctx, G16_CXX)
    except RuntimeError as exc:
        return fail_result(engine, "gcc_rebuild", str(exc))
    bootstrap = not (_fast_rebuild() or _env_true("G16_DISABLE_BOOTSTRAP"))
    build_env = _make_env(ctx, selfhost=True)
    bdir = gcc_build_dir(ctx)

    if _fast_rebuild() and (bdir / "Makefile").is_file():
        engine.log("gcc_rebuild — G16_FAST_REBUILD: skip distclean, incremental make -j")
    else:
        for run_fn in (run_gcc_distclean, run_gcc_configure_selfhost):
            r = run_fn(ctx, engine)
            if not r.ok:
                return fail_result(engine, "gcc_rebuild", r.message)

    target = "bootstrap" if bootstrap else "all"
    if engine.run_stream(["make", target, f"-j{ctx.jobs}"], cwd=bdir, env=build_env, timeout=None) != 0:
        return fail_result(engine, "gcc_rebuild", f"make {target} failed")
    if engine.run_stream(["make", "install"], cwd=bdir, env=build_env, timeout=None) != 0:
        return fail_result(engine, "gcc_rebuild", "install failed")
    if not install_g16(ctx, engine):
        return fail_result(engine, "gcc_rebuild", "install verify failed")
    write_selfhost_stamp(ctx, bootstrap=bootstrap)
    write_cmake_toolchain(ctx)
    write_manifest(ctx)
    return ok_result(engine, "gcc_rebuild", g16_status(ctx).get("version", ""))


def run_gcc(ctx: ForgeContext, engine: ForgeEngine) -> ForgeResult:
    for step, run_fn, check_fn in (
        ("gcc_fetch", run_gcc_fetch, check_gcc_fetch),
        ("gcc_prereqs", run_gcc_prereqs, check_gcc_prereqs),
        ("gcc_configure", run_gcc_configure, check_gcc_configure),
        ("gcc_build", run_gcc_build, check_gcc_build),
    ):
        if check_fn(ctx) and step != "gcc_build":
            continue
        r = run_fn(ctx, engine)
        if not r.ok:
            return r
    return ok_result(engine, "gcc", g16_status(ctx).get("version", ""))


GCC_TOOLS: dict[str, tuple[str, object, object]] = {
    "gcc_fetch": (run_gcc_fetch, check_gcc_fetch),
    "gcc_prereqs": (run_gcc_prereqs, check_gcc_prereqs),
    "gcc_configure": (run_gcc_configure, check_gcc_configure),
    "gcc_build": (run_gcc_build, check_gcc_build),
    "gcc_rebuild": (run_gcc_rebuild, check_gcc_rebuild),
    "gcc": (run_gcc, check_gcc_build),
}

GCC_ORDER = ["gcc_fetch", "gcc_prereqs", "gcc_configure", "gcc_build"]