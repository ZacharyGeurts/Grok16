#!/usr/bin/env python3
"""Build Grok16 GitHub Pages AmmoCode syntax editor — languages, library, manuals."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DOCS = Path(__file__).resolve().parent
GROK16 = DOCS.parent
SG = GROK16.parent
NEXUS = SG / "NewLatest"
AMMOCODE = NEXUS / "AmmoCode"
SHELF = NEXUS / "library" / "dewey" / "000-computer-science"
LANG_READER = NEXUS / "lib" / "field-lang-manual-reader.py"
HOSTESS7_RAW = "https://raw.githubusercontent.com/ZacharyGeurts/Hostess7/main"


def load_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default if default is not None else {}


def lang_label(lang_id: str) -> str:
    return lang_id.replace("_", " ").replace("-", " ").title()


def build_languages_index(g16: dict) -> dict:
    langs = g16.get("languages") or {}
    ammo = load_json(AMMOCODE / "data" / "languages.json", {})
    ext_map = ammo.get("extensions") or {}
    items = []
    for lang_id in sorted(langs.keys()):
        entry = langs[lang_id] or {}
        exts = entry.get("extensions") or []
        book_id = f"explaining_{lang_id}"
        book_path = SHELF / book_id
        has_book = (book_path / f"{book_id}.h7c").is_file() or (book_path / "book.json").is_file()
        items.append({
            "id": lang_id,
            "label": lang_label(lang_id),
            "extensions": exts,
            "book_id": book_id if has_book else None,
            "has_manual": has_book,
            "driver": entry.get("driver"),
            "memory": entry.get("memory"),
        })
    return {
        "schema": "grok16-editor-languages/v1",
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "count": len(items),
        "extensions": ext_map,
        "languages": items,
    }


def build_books_catalog(shelf: dict) -> dict:
    books = []
    for b in shelf.get("books") or []:
        bid = b.get("id") or ""
        if not bid.startswith("explaining_"):
            continue
        lang_id = bid.replace("explaining_", "", 1)
        base = f"{HOSTESS7_RAW}/library/dewey/000-computer-science/{bid}"
        books.append({
            "id": bid,
            "lang_id": lang_id,
            "title": b.get("title") or lang_label(lang_id),
            "author": b.get("author") or "Hostess 7",
            "cover": b.get("cover"),
            "ready": bool(b.get("ready")),
            "book_json": f"{base}/book.json",
            "h7c": f"{base}/{bid}.h7c",
            "github_tree": f"https://github.com/ZacharyGeurts/Hostess7/tree/main/library/dewey/000-computer-science/{bid}",
        })
    books.sort(key=lambda x: x["lang_id"])
    return {
        "schema": "grok16-editor-books/v1",
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "shelf": "000-computer-science",
        "hostess7_repo": "https://github.com/ZacharyGeurts/Hostess7",
        "count": len(books),
        "books": books,
    }


def export_manuals(lang_ids: list[str], out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    if not LANG_READER.is_file():
        print("WARN: field-lang-manual-reader.py missing — skip manual export", file=sys.stderr)
        return 0
    n = 0
    for lang_id in lang_ids:
        book_id = f"explaining_{lang_id}"
        h7c = SHELF / book_id / f"{book_id}.h7c"
        if not h7c.is_file():
            continue
        try:
            proc = subprocess.run(
                [sys.executable, str(LANG_READER), "text", lang_id],
                cwd=str(NEXUS),
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
            )
            if proc.returncode != 0 or not proc.stdout.strip():
                continue
            (out_dir / f"{lang_id}.md").write_text(proc.stdout, encoding="utf-8")
            n += 1
        except (subprocess.TimeoutExpired, OSError) as exc:
            print(f"WARN: manual export {lang_id}: {exc}", file=sys.stderr)
    return n


def sync_assets() -> None:
    lib = DOCS / "lib"
    assets = DOCS / "assets"
    lib.mkdir(parents=True, exist_ok=True)
    assets.mkdir(parents=True, exist_ok=True)
    for name in ("highlight.js",):
        src = AMMOCODE / "lib" / name
        if src.is_file():
            shutil.copy2(src, lib / name)
    for name in ("ammocode-nexus-c2.css", "ammocode-syntax.css"):
        src = AMMOCODE / "assets" / name
        if src.is_file():
            shutil.copy2(src, assets / name)


def main() -> int:
    g16 = load_json(GROK16 / "data" / "grok16-languages.json")
    shelf = load_json(SHELF / "shelf.json")
    if not g16.get("languages"):
        print("FAIL: grok16-languages.json missing", file=sys.stderr)
        return 1

    data_dir = DOCS / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    lang_doc = build_languages_index(g16)
    (data_dir / "languages-index.json").write_text(
        json.dumps(lang_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"languages-index.json — {lang_doc['count']} languages")

    book_doc = build_books_catalog(shelf)
    (data_dir / "books-catalog.json").write_text(
        json.dumps(book_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"books-catalog.json — {book_doc['count']} textbooks")

    manual_langs = [b["lang_id"] for b in book_doc["books"]]
    n = export_manuals(manual_langs, data_dir / "manuals")
    print(f"manuals/ — exported {n} language textbooks")

    sync_assets()
    print("assets + highlight.js synced from AmmoCode")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())