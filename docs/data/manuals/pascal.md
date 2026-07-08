# Explaining Pascal

![Cover — Explaining Pascal](h7fig:cover)

Hostess 7 programming language manual — complete reference distilled from the
Pascal combinatronic pack and boiled to the g16 program facet (36 canonical ops).

- **Language id:** `pascal`
- **Command entries:** 48
- **Canonical ops used:** 18
- **Generated:** 2026-06-29T12:11:31Z
- **Format:** H7c v3 with embedded figures

## At a glance

- **Paradigm:** imperative
- **Typing:** static strong
- **Memory:** manual
- **Year originated:** 1970

Pascal: structured programming teaching language — strong typing, nested procedures. Delphi/Object Pascal OOP extension.

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Introduction

This manual explains every seeded Pascal construct: surface syntax, semantic role,
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
- · **call** — Call / invoke / apply (runner: native_bsp, belt: belt_2_0)
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
- ✓ **alloc** — Allocate / new / malloc (runner: native_bsp, belt: belt_2_0)
- ✓ **free** — Free / delete / drop (runner: native_bsp, belt: belt_2_0)
- ✓ **io** — I/O / print / read / write file (runner: python, belt: belt_1_0)
- ✓ **import** — Import / use / require (runner: python, belt: belt_1_0)
- ✓ **export** — Export / pub / module out (runner: native_bsp, belt: belt_2_0)
- ✓ **module** — Module / package / namespace (runner: python, belt: belt_1_0)
- · **compare** — Compare / eq / ord (runner: native_bsp, belt: belt_1_0)
- · **logic** — Logic / and / or / not (runner: native_bsp, belt: belt_1_0)
- · **math** — Math / arithmetic (runner: native_bsp, belt: belt_1_0)
- · **string** — String / format / concat (runner: python, belt: belt_1_0)
- ✓ **struct** — Struct / record / object (runner: native_bsp, belt: belt_2_0)
- · **index** — Index / subscript / slice (runner: python, belt: belt_1_0)
- · **throw** — Throw / raise / panic (runner: native_bsp, belt: belt_2_0)
- · **catch** — Catch / rescue / except (runner: native_bsp, belt: belt_2_0)
- · **yield** — Yield / generator / coroutine (runner: python, belt: belt_1_0)
- · **lambda** — Lambda / closure / fn (runner: python, belt: belt_1_0)
- ✓ **match** — Pattern match / case (runner: native_bsp, belt: belt_2_0)
- · **async** — Async / await / concurrent (runner: python, belt: belt_1_0)
- · **sync** — Sync / lock / mutex / atomic (runner: native_bsp, belt: belt_2_0)
- ✓ **asm** — Inline asm / intrinsics (runner: native_bsp, belt: belt_2_0)
- · **unsafe** — Unsafe / raw pointer (runner: native_bsp, belt: belt_2_0)
- · **meta** — Macro / reflection / eval (runner: python, belt: belt_1_0)
- · **query** — Query / select / SQL (runner: python, belt: belt_1_0)

## Pascal commands by canonical op

### `alloc` — Allocate / new / malloc

- `getmem`
- `new`

### `asm` — Inline asm / intrinsics

- `inline`

### `branch` — Branch / if / switch

- `else`
- `goto`
- `if`
- `then`

### `break` — Break / leave loop

- `break`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `const`
- `function`
- `procedure`
- `var`

### `exec` — Execute / eval / run

- `begin`

### `export` — Export / pub / module out

- `interface`

### `free` — Free / delete / drop

- `dispose`
- `freemem`

### `import` — Import / use / require

- `uses`

### `io` — I/O / print / read / write file

- `closefile`
- `file`
- `read`
- `readln`
- `reset`
- `rewrite`
- `text`
- `write`
- `writeln`

### `load` — Load / read memory

- `with`

### `loop` — Loop / iterate / repeat

- `do`
- `downto`
- `for`
- `repeat`
- `to`
- `until`
- `while`

### `match` — Pattern match / case

- `case`
- `of`

### `module` — Module / package / namespace

- `implementation`
- `program`
- `unit`

### `return` — Return / exit function

- `end`
- `end.`
- `exit`

### `struct` — Struct / record / object

- `array`
- `record`
- `set`

### `type` — Type / typedef / interface

- `packed`
- `type`

## Pascal full command reference

### `getmem`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "getmem"`

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "new"`

### `inline`
- **Boils to:** `asm` — Inline asm / intrinsics
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "inline"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "else"`

### `goto`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "goto"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "if"`

### `then`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "then"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "break"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "continue"`

### `const`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "const"`

### `function`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "function"`

### `procedure`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "procedure"`

### `var`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "var"`

### `begin`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "begin"`

### `interface`
- **Boils to:** `export` — Export / pub / module out
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "interface"`

### `dispose`
- **Boils to:** `free` — Free / delete / drop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "dispose"`

### `freemem`
- **Boils to:** `free` — Free / delete / drop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "freemem"`

### `uses`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "uses"`

### `closefile`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "closefile"`

### `file`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "file"`

### `read`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "read"`

### `readln`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "readln"`

### `reset`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "reset"`

### `rewrite`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "rewrite"`

### `text`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "text"`

### `write`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "write"`

### `writeln`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "writeln"`

### `with`
- **Boils to:** `load` — Load / read memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "with"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "do"`

### `downto`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "downto"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "for"`

### `repeat`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "repeat"`

### `to`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "to"`

### `until`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "until"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "while"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "case"`

### `of`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "of"`

### `implementation`
- **Boils to:** `module` — Module / package / namespace
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "implementation"`

### `program`
- **Boils to:** `module` — Module / package / namespace
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "program"`

### `unit`
- **Boils to:** `module` — Module / package / namespace
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "unit"`

### `end`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "end"`

### `end.`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "end."`

### `exit`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "exit"`

### `array`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "array"`

### `record`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "record"`

### `set`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "set"`

### `packed`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "packed"`

### `type`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil pascal "type"`

## Execution model

Pascal programs execute through the Field program combinatronic facet. Surface syntax
maps to 36 canonical ops; each op selects a belt runner (native_bsp on belt_2_0 or
python on belt_1_0). The explaining manual documents semantics — not a tutorial walkthrough.

- **Paradigm:** imperative
- **Typing discipline:** static strong
- **Memory:** manual
- **Commands in seed:** 48
- **Canonical ops exercised:** 18

![Memory and objects](h7fig:memory)

## Lexical structure

Tokens partition into identifiers, literals, operators, and significant whitespace
per Pascal reference rules. Hostess7 boil heuristics treat unknown tokens as exec
unless a seed keyword maps them. Extended packs inherit parent commands.

- `array` → `struct`
- `begin` → `exec`
- `break` → `break`
- `case` → `match`
- `closefile` → `io`
- `const` → `declare`
- `continue` → `continue`
- `dispose` → `free`
- `do` → `loop`
- `downto` → `loop`
- `else` → `branch`
- `end` → `return`
- `end.` → `return`
- `exit` → `return`
- `file` → `io`
- `for` → `loop`
- `freemem` → `free`
- `function` → `declare`
- `getmem` → `alloc`
- `goto` → `branch`
- `if` → `branch`
- `implementation` → `module`
- `inline` → `asm`
- `interface` → `export`

## Type and value space

Pascal: structured programming teaching language — strong typing, nested procedures. Delphi/Object Pascal OOP extension.

## Control flow

branch · loop · break · continue · return — all languages converge on these atoms.
In Pascal, control constructs in the seed pack boil as follows:

- **branch:** `if`, `then`, `else`, `goto`
- **loop:** `for`, `to`, `downto`, `do`, `while`, `repeat`, `until`
- **return:** `end`, `end.`, `exit`

## Modules and boundaries

import · export · module · package — boundary ops isolate compilation units.
NEXUS-Shield indexes each manual under Dewey 000; combinatronic rebalance may extend packs.

![G16 compile path](h7fig:compile)

## Standard library surface

Where the seed lists I/O or runtime commands, they map to the io and call ops.
Verify any keyword with `field-program-combinatronic.py boil pascal "<cmd>"`.

- `closefile`
- `file`
- `read`
- `readln`
- `reset`
- `rewrite`
- `text`
- `uses`
- `write`
- `writeln`

## Interop and embedding

Pascal may embed in Queen Code, Grok16 belt builds, or NEXUS panel scripts.
G16 unified driver (`g16`) compiles C/C++ neighbors; python runner hosts dynamic facets.
Use `g16-compile-combinatronics.py` when program facet gates must pass at compile time.

## Secure compile & run chamber

Every Pascal compile and run path is sealed — **no bare host exec**. User code passes
`g16-code-security.py` first, then executes inside `g16-secure-chamber.py` with scrubbed
env (`HOME`, `TMPDIR`, `PATH` limited) so AmmoOS, Hostess 7, and Grok16/bin stay protected.

- **Check:** `g16-secure-chamber.py compile` (stdin JSON: content, lang)
- **Run:** `g16-secure-chamber.py run <path> --lang pascal`
- **Posture:** `/api/g16/secure-chamber` · `nexus-g16-bridge.py json` → `secure_chamber`
- **Queen launch:** `runner_policy.pascal` = `chamber` in `.launch` manifests
- **Forbidden:** Hostess7, AmmoCode, Grok16/bin, /usr/bin — cannot execute in place

## Performance notes

belt_2_0 native_bsp is the default for hot paths; belt_1_0 python runner applies
when combinatorics bridge degrades the gate. Always-optimal panel pins the best belt
from bench receipts — not guessed from language family alone.

## Research references

Training manuals (school-style textbooks) complement this explaining manual.
See `training_pascal` on the Dewey shelf when published.
Field Research book and g16-power-sort plates inform algorithm choices in tooling.

## G16 compile path

- **Boil:** `field-program-combinatronic.py boil pascal`
- **Universal facet:** `field-g16-universal-combinatronic.json`
- **Grok16 compile:** `g16-compile-combinatronics.py` with program facet profile
- **Belt runners:** native_bsp (belt_2_0) and python (belt_1_0) per canonical op
- **Secure chamber:** `lib/g16-secure-chamber.py` — mandatory for all 57 Grok16 languages
- **Filetype actions:** `run` / `compile` → `secure_chamber` in field-programming-filetypes.json

## Code patterns

Representative Pascal patterns map to canonical ops as follows:

- **Declaration + assign** → declare, assign
- **Conditional** → branch
- **Iteration** → loop, break, continue
- **Procedure call** → call, return
- **Module boundary** → import, export, module
- **I/O** → io
- **Error handling** → throw, catch

## Pitfalls

- Case sensitivity varies — Pascal keywords may not match heuristic boil.
- Extended packs inherit parent commands; check `extends` in the seed.
- Unknown tokens fall through to heuristic_keywords before defaulting to exec.
- CDN and macro expansion are advisory until combinatronic rebalance runs.
- **Never run Pascal on the bare host** — shell escapes, `eval`, `system`, and JVM/Node
  subprocess calls are blocked transparently; use the sealed chamber lane.
- Missing host toolchains (javac, node, cobc, fpc) return clear errors inside the chamber.

## Where in NEXUS-Shield

- Seed: `data/field-program-combinatronic-seed.json`
- Battery: `field-program-combinatronic.json` (STATE)
- Manual: `library/dewey/000-computer-science/explaining_pascal/`
- Reader API: `/api/lang-manuals` · `/api/lang-manuals/pascal`
- H7c figures: cover, syntax, op_map, memory, compile (field plate + meld)

