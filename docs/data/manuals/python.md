# Explaining Python

![Cover — Explaining Python](h7fig:cover)

Hostess 7 programming language manual — complete reference distilled from the
Python combinatronic pack and boiled to the g16 program facet (36 canonical ops).

- **Language id:** `python`
- **Command entries:** 54
- **Canonical ops used:** 25
- **Generated:** 2026-06-29T12:13:59Z
- **Format:** H7c v3 with embedded figures

## At a glance

- **Paradigm:** multi-paradigm
- **Typing:** dynamic gradual
- **Memory:** gc
- **Year originated:** 1991

Python 3: Hostess 7 brain scripts — field_superintelligence.py, corpora, QA gates. Dynamic typing, GIL, asyncio optional. dataclasses, pathlib, json for lossless brain shards.

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Introduction

This manual explains every seeded Python construct: surface syntax, semantic role,
canonical combinatronic op, belt runner, and NEXUS-Shield integration paths.
Use the GUI reader (`/field-lang-manuals`) or text mode (`field-lang-manual-reader.py text`).

## Reading guide

1. **At a glance** — paradigm, typing, memory model.
2. **Canonical atoms** — the 36 ops all languages boil to.
3. **Commands by op** — every keyword grouped by canonical target.
4. **Full command index** — alphabetical reference.
5. **G16 & NEXUS** — compile, belt, API, pitfalls.

## Canonical combinatronic atoms

- ✓ **exec** — Execute / eval / run (runner: native_bsp, belt: belt_2_0)
- · **assign** — Assign / bind / set (runner: python, belt: belt_1_0)
- ✓ **call** — Call / invoke / apply (runner: native_bsp, belt: belt_2_0)
- ✓ **return** — Return / exit function (runner: native_bsp, belt: belt_2_0)
- ✓ **branch** — Branch / if / switch (runner: native_bsp, belt: belt_1_0)
- ✓ **loop** — Loop / iterate / repeat (runner: native_bsp, belt: belt_1_0)
- ✓ **break** — Break / leave loop (runner: native_bsp, belt: belt_1_0)
- ✓ **continue** — Continue / next iteration (runner: native_bsp, belt: belt_1_0)
- ✓ **declare** — Declare / define / let (runner: python, belt: belt_1_0)
- ✓ **type** — Type / typedef / interface (runner: native_bsp, belt: belt_2_0)
- · **cast** — Cast / convert / coerce (runner: native_bsp, belt: belt_2_0)
- ✓ **load** — Load / read memory (runner: native_bsp, belt: belt_2_0)
- · **store** — Store / write memory (runner: native_bsp, belt: belt_2_0)
- · **alloc** — Allocate / new / malloc (runner: native_bsp, belt: belt_2_0)
- ✓ **free** — Free / delete / drop (runner: native_bsp, belt: belt_2_0)
- ✓ **io** — I/O / print / read / write file (runner: python, belt: belt_1_0)
- ✓ **import** — Import / use / require (runner: python, belt: belt_1_0)
- · **export** — Export / pub / module out (runner: native_bsp, belt: belt_2_0)
- · **module** — Module / package / namespace (runner: python, belt: belt_1_0)
- ✓ **compare** — Compare / eq / ord (runner: native_bsp, belt: belt_1_0)
- ✓ **logic** — Logic / and / or / not (runner: native_bsp, belt: belt_1_0)
- · **math** — Math / arithmetic (runner: native_bsp, belt: belt_1_0)
- ✓ **string** — String / format / concat (runner: python, belt: belt_1_0)
- ✓ **struct** — Struct / record / object (runner: native_bsp, belt: belt_2_0)
- ✓ **index** — Index / subscript / slice (runner: python, belt: belt_1_0)
- ✓ **throw** — Throw / raise / panic (runner: native_bsp, belt: belt_2_0)
- ✓ **catch** — Catch / rescue / except (runner: native_bsp, belt: belt_2_0)
- ✓ **yield** — Yield / generator / coroutine (runner: python, belt: belt_1_0)
- ✓ **lambda** — Lambda / closure / fn (runner: python, belt: belt_1_0)
- ✓ **match** — Pattern match / case (runner: native_bsp, belt: belt_2_0)
- ✓ **async** — Async / await / concurrent (runner: python, belt: belt_1_0)
- ✓ **sync** — Sync / lock / mutex / atomic (runner: native_bsp, belt: belt_2_0)
- · **asm** — Inline asm / intrinsics (runner: native_bsp, belt: belt_2_0)
- · **unsafe** — Unsafe / raw pointer (runner: native_bsp, belt: belt_2_0)
- · **meta** — Macro / reflection / eval (runner: python, belt: belt_1_0)
- · **query** — Query / select / SQL (runner: python, belt: belt_1_0)

## Python commands by canonical op

### `async` — Async / await / concurrent

- `async`
- `await`

### `branch` — Branch / if / switch

- `elif`
- `else`
- `if`

### `break` — Break / leave loop

- `break`

### `call` — Call / invoke / apply

- `super`

### `catch` — Catch / rescue / except

- `except`
- `finally`
- `try`

### `compare` — Compare / eq / ord

- `is`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `__init__`
- `def`
- `global`
- `nonlocal`
- `property`

### `exec` — Execute / eval / run

- `eval`
- `exec`
- `pass`

### `free` — Free / delete / drop

- `del`

### `import` — Import / use / require

- `as`
- `from`
- `import`

### `index` — Index / subscript / slice

- `in`

### `io` — I/O / print / read / write file

- `open`
- `print`
- `read`
- `write`

### `lambda` — Lambda / closure / fn

- `lambda`

### `load` — Load / read memory

- `self`

### `logic` — Logic / and / or / not

- `and`
- `not`
- `or`

### `loop` — Loop / iterate / repeat

- `for`
- `while`

### `match` — Pattern match / case

- `case`
- `match`

### `return` — Return / exit function

- `return`

### `string` — String / format / concat

- `f-string`
- `format`
- `str`

### `struct` — Struct / record / object

- `dataclass`
- `dict`
- `list`
- `set`
- `tuple`

### `sync` — Sync / lock / mutex / atomic

- `with`

### `throw` — Throw / raise / panic

- `assert`
- `raise`

### `type` — Type / typedef / interface

- `class`
- `enum`
- `typing`

### `yield` — Yield / generator / coroutine

- `yield`

## Python full command reference

### `async`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "async"`

### `await`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "await"`

### `elif`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "elif"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "else"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "if"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "break"`

### `super`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "super"`

### `except`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "except"`

### `finally`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "finally"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "try"`

### `is`
- **Boils to:** `compare` — Compare / eq / ord
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "is"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "continue"`

### `__init__`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "__init__"`

### `def`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "def"`

### `global`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "global"`

### `nonlocal`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "nonlocal"`

### `property`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "property"`

### `eval`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "eval"`

### `exec`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "exec"`

### `pass`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "pass"`

### `del`
- **Boils to:** `free` — Free / delete / drop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "del"`

### `as`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "as"`

### `from`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "from"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "import"`

### `in`
- **Boils to:** `index` — Index / subscript / slice
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "in"`

### `open`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "open"`

### `print`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "print"`

### `read`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "read"`

### `write`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "write"`

### `lambda`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "lambda"`

### `self`
- **Boils to:** `load` — Load / read memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "self"`

### `and`
- **Boils to:** `logic` — Logic / and / or / not
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "and"`

### `not`
- **Boils to:** `logic` — Logic / and / or / not
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "not"`

### `or`
- **Boils to:** `logic` — Logic / and / or / not
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "or"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "for"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "while"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "case"`

### `match`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "match"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "return"`

### `f-string`
- **Boils to:** `string` — String / format / concat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "f-string"`

### `format`
- **Boils to:** `string` — String / format / concat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "format"`

### `str`
- **Boils to:** `string` — String / format / concat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "str"`

### `dataclass`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "dataclass"`

### `dict`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "dict"`

### `list`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "list"`

### `set`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "set"`

### `tuple`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "tuple"`

### `with`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "with"`

### `assert`
- **Boils to:** `throw` — Throw / raise / panic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "assert"`

### `raise`
- **Boils to:** `throw` — Throw / raise / panic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "raise"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "class"`

### `enum`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "enum"`

### `typing`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "typing"`

### `yield`
- **Boils to:** `yield` — Yield / generator / coroutine
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil python "yield"`

## Execution model

Python programs execute through the Field program combinatronic facet. Surface syntax
maps to 36 canonical ops; each op selects a belt runner (native_bsp on belt_2_0 or
python on belt_1_0). The explaining manual documents semantics — not a tutorial walkthrough.

- **Paradigm:** multi-paradigm
- **Typing discipline:** dynamic gradual
- **Memory:** gc
- **Commands in seed:** 54
- **Canonical ops exercised:** 25

![Memory and objects](h7fig:memory)

## Lexical structure

Tokens partition into identifiers, literals, operators, and significant whitespace
per Python reference rules. Hostess7 boil heuristics treat unknown tokens as exec
unless a seed keyword maps them. Extended packs inherit parent commands.

- `__init__` → `declare`
- `and` → `logic`
- `as` → `import`
- `assert` → `throw`
- `async` → `async`
- `await` → `async`
- `break` → `break`
- `case` → `match`
- `class` → `type`
- `continue` → `continue`
- `dataclass` → `struct`
- `def` → `declare`
- `del` → `free`
- `dict` → `struct`
- `elif` → `branch`
- `else` → `branch`
- `enum` → `type`
- `eval` → `exec`
- `except` → `catch`
- `exec` → `exec`
- `f-string` → `string`
- `finally` → `catch`
- `for` → `loop`
- `format` → `string`

## Type and value space

Python 3: Hostess 7 brain scripts — field_superintelligence.py, corpora, QA gates. Dynamic typing, GIL, asyncio optional. dataclasses, pathlib, json for lossless brain shards.

## Control flow

branch · loop · break · continue · return — all languages converge on these atoms.
In Python, control constructs in the seed pack boil as follows:

- **branch:** `if`, `elif`, `else`
- **loop:** `for`, `while`
- **return:** `return`
- **throw:** `raise`, `assert`

## Modules and boundaries

import · export · module · package — boundary ops isolate compilation units.
NEXUS-Shield indexes each manual under Dewey 000; combinatronic rebalance may extend packs.

![G16 compile path](h7fig:compile)

## Standard library surface

Where the seed lists I/O or runtime commands, they map to the io and call ops.
Verify any keyword with `field-program-combinatronic.py boil python "<cmd>"`.

- `as`
- `from`
- `import`
- `open`
- `print`
- `read`
- `super`
- `write`

## Interop and embedding

Python may embed in Queen Code, Grok16 belt builds, or NEXUS panel scripts.
G16 unified driver (`g16`) compiles C/C++ neighbors; python runner hosts dynamic facets.
Use `g16-compile-combinatronics.py` when program facet gates must pass at compile time.

## Secure compile & run chamber

Every Python compile and run path is sealed — **no bare host exec**. User code passes
`g16-code-security.py` first, then executes inside `g16-secure-chamber.py` with scrubbed
env (`HOME`, `TMPDIR`, `PATH` limited) so AmmoOS, Hostess 7, and Grok16/bin stay protected.

- **Check:** `g16-secure-chamber.py compile` (stdin JSON: content, lang)
- **Run:** `g16-secure-chamber.py run <path> --lang python`
- **Posture:** `/api/g16/secure-chamber` · `nexus-g16-bridge.py json` → `secure_chamber`
- **Queen launch:** `runner_policy.python` = `chamber` in `.launch` manifests
- **Forbidden:** Hostess7, AmmoCode, Grok16/bin, /usr/bin — cannot execute in place

## Performance notes

belt_2_0 native_bsp is the default for hot paths; belt_1_0 python runner applies
when combinatorics bridge degrades the gate. Always-optimal panel pins the best belt
from bench receipts — not guessed from language family alone.

## Research references

Training manuals (school-style textbooks) complement this explaining manual.
See `training_python` on the Dewey shelf when published.
Field Research book and g16-power-sort plates inform algorithm choices in tooling.

## G16 compile path

- **Boil:** `field-program-combinatronic.py boil python`
- **Universal facet:** `field-g16-universal-combinatronic.json`
- **Grok16 compile:** `g16-compile-combinatronics.py` with program facet profile
- **Belt runners:** native_bsp (belt_2_0) and python (belt_1_0) per canonical op
- **Secure chamber:** `lib/g16-secure-chamber.py` — mandatory for all 57 Grok16 languages
- **Filetype actions:** `run` / `compile` → `secure_chamber` in field-programming-filetypes.json

## Code patterns

Representative Python patterns map to canonical ops as follows:

- **Declaration + assign** → declare, assign
- **Conditional** → branch
- **Iteration** → loop, break, continue
- **Procedure call** → call, return
- **Module boundary** → import, export, module
- **I/O** → io
- **Error handling** → throw, catch

## Pitfalls

- Case sensitivity varies — Python keywords may not match heuristic boil.
- Extended packs inherit parent commands; check `extends` in the seed.
- Unknown tokens fall through to heuristic_keywords before defaulting to exec.
- CDN and macro expansion are advisory until combinatronic rebalance runs.
- **Never run Python on the bare host** — shell escapes, `eval`, `system`, and JVM/Node
  subprocess calls are blocked transparently; use the sealed chamber lane.
- Missing host toolchains (javac, node, cobc, fpc) return clear errors inside the chamber.

## Where in NEXUS-Shield

- Seed: `data/field-program-combinatronic-seed.json`
- Battery: `field-program-combinatronic.json` (STATE)
- Manual: `library/dewey/000-computer-science/explaining_python/`
- Reader API: `/api/lang-manuals` · `/api/lang-manuals/python`
- H7c figures: cover, syntax, op_map, memory, compile (field plate + meld)

