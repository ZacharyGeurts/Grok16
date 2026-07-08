# Explaining QuickBASIC

![Cover — Explaining QuickBASIC](h7fig:cover)

Hostess 7 programming language manual — complete reference distilled from the
QuickBASIC combinatronic pack and boiled to the g16 program facet (36 canonical ops).

- **Language id:** `quickbasic`
- **Command entries:** 35
- **Canonical ops used:** 13
- **Generated:** 2026-06-29T12:15:16Z
- **Format:** H7c v3 with embedded figures

## At a glance

QuickBASIC is catalogued in the Field program combinatronic seed.
Profile metadata fills in when Hostess7 langs corpus matches this id.

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Introduction

This manual explains every seeded QuickBASIC construct: surface syntax, semantic role,
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
- ✓ **assign** — Assign / bind / set (runner: python, belt: belt_1_0)
- ✓ **call** — Call / invoke / apply (runner: native_bsp, belt: belt_2_0)
- ✓ **return** — Return / exit function (runner: native_bsp, belt: belt_2_0)
- ✓ **branch** — Branch / if / switch (runner: native_bsp, belt: belt_1_0)
- · **loop** — Loop / iterate / repeat (runner: native_bsp, belt: belt_1_0)
- · **break** — Break / leave loop (runner: native_bsp, belt: belt_1_0)
- · **continue** — Continue / next iteration (runner: native_bsp, belt: belt_1_0)
- ✓ **declare** — Declare / define / let (runner: python, belt: belt_1_0)
- ✓ **type** — Type / typedef / interface (runner: native_bsp, belt: belt_2_0)
- · **cast** — Cast / convert / coerce (runner: native_bsp, belt: belt_2_0)
- · **load** — Load / read memory (runner: native_bsp, belt: belt_2_0)
- · **store** — Store / write memory (runner: native_bsp, belt: belt_2_0)
- · **alloc** — Allocate / new / malloc (runner: native_bsp, belt: belt_2_0)
- ✓ **free** — Free / delete / drop (runner: native_bsp, belt: belt_2_0)
- ✓ **io** — I/O / print / read / write file (runner: python, belt: belt_1_0)
- ✓ **import** — Import / use / require (runner: python, belt: belt_1_0)
- · **export** — Export / pub / module out (runner: native_bsp, belt: belt_2_0)
- · **module** — Module / package / namespace (runner: python, belt: belt_1_0)
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

## QuickBASIC commands by canonical op

### `asm` — Inline asm / intrinsics

- `INTERRUPT`

### `assign` — Assign / bind / set

- `ENVIRON`
- `NAME`

### `branch` — Branch / if / switch

- `CASE ELSE`

### `call` — Call / invoke / apply

- `INT86`
- `INT86X`

### `declare` — Declare / define / let

- `$DYNAMIC`
- `$STATIC`
- `BYVAL`
- `DECLARE`
- `FIELD`
- `FUNCTION`
- `SHARED`
- `STATIC`
- `SUB`

### `exec` — Execute / eval / run

- `SHELL`

### `free` — Free / delete / drop

- `KILL`

### `import` — Import / use / require

- `$INCLUDE`

### `io` — I/O / print / read / write file

- `_SCREENSHOW`
- `CIRCLE`
- `CLS`
- `COLOR`
- `DRAW`
- `LINE`
- `LOCATE`
- `MKDIR`
- `PAINT`
- `SCREEN`

### `match` — Pattern match / case

- `CASE`
- `SELECT CASE`

### `return` — Return / exit function

- `END FUNCTION`
- `END SUB`

### `struct` — Struct / record / object

- `TYPE`
- `UNION`

### `type` — Type / typedef / interface

- `AS`

## QuickBASIC full command reference

### `INTERRUPT`
- **Boils to:** `asm` — Inline asm / intrinsics
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "INTERRUPT"`

### `ENVIRON`
- **Boils to:** `assign` — Assign / bind / set
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "ENVIRON"`

### `NAME`
- **Boils to:** `assign` — Assign / bind / set
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "NAME"`

### `CASE ELSE`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "CASE ELSE"`

### `INT86`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "INT86"`

### `INT86X`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "INT86X"`

### `$DYNAMIC`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "$DYNAMIC"`

### `$STATIC`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "$STATIC"`

### `BYVAL`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "BYVAL"`

### `DECLARE`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "DECLARE"`

### `FIELD`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "FIELD"`

### `FUNCTION`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "FUNCTION"`

### `SHARED`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "SHARED"`

### `STATIC`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "STATIC"`

### `SUB`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "SUB"`

### `SHELL`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "SHELL"`

### `KILL`
- **Boils to:** `free` — Free / delete / drop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "KILL"`

### `$INCLUDE`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "$INCLUDE"`

### `_SCREENSHOW`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "_SCREENSHOW"`

### `CIRCLE`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "CIRCLE"`

### `CLS`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "CLS"`

### `COLOR`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "COLOR"`

### `DRAW`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "DRAW"`

### `LINE`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "LINE"`

### `LOCATE`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "LOCATE"`

### `MKDIR`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "MKDIR"`

### `PAINT`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "PAINT"`

### `SCREEN`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "SCREEN"`

### `CASE`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "CASE"`

### `SELECT CASE`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "SELECT CASE"`

### `END FUNCTION`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "END FUNCTION"`

### `END SUB`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "END SUB"`

### `TYPE`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "TYPE"`

### `UNION`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "UNION"`

### `AS`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil quickbasic "AS"`

## Execution model

QuickBASIC programs execute through the Field program combinatronic facet. Surface syntax
maps to 36 canonical ops; each op selects a belt runner (native_bsp on belt_2_0 or
python on belt_1_0). The explaining manual documents semantics — not a tutorial walkthrough.

- **Paradigm:** multi-paradigm
- **Typing discipline:** see language reference
- **Memory:** runtime-managed
- **Commands in seed:** 35
- **Canonical ops exercised:** 13

![Memory and objects](h7fig:memory)

## Lexical structure

Tokens partition into identifiers, literals, operators, and significant whitespace
per QuickBASIC reference rules. Hostess7 boil heuristics treat unknown tokens as exec
unless a seed keyword maps them. Extended packs inherit parent commands.

- `$DYNAMIC` → `declare`
- `$INCLUDE` → `import`
- `$STATIC` → `declare`
- `_SCREENSHOW` → `io`
- `AS` → `type`
- `BYVAL` → `declare`
- `CASE` → `match`
- `CASE ELSE` → `branch`
- `CIRCLE` → `io`
- `CLS` → `io`
- `COLOR` → `io`
- `DECLARE` → `declare`
- `DRAW` → `io`
- `END FUNCTION` → `return`
- `END SUB` → `return`
- `ENVIRON` → `assign`
- `FIELD` → `declare`
- `FUNCTION` → `declare`
- `INT86` → `call`
- `INT86X` → `call`
- `INTERRUPT` → `asm`
- `KILL` → `free`
- `LINE` → `io`
- `LOCATE` → `io`

## Type and value space

The QuickBASIC value space follows the language reference: primitives, aggregates,
and callables compose through assign, call, and return canonical ops.

## Control flow

branch · loop · break · continue · return — all languages converge on these atoms.
In QuickBASIC, control constructs in the seed pack boil as follows:

- **branch:** `CASE ELSE`
- **return:** `END SUB`, `END FUNCTION`

## Modules and boundaries

import · export · module · package — boundary ops isolate compilation units.
NEXUS-Shield indexes each manual under Dewey 000; combinatronic rebalance may extend packs.

![G16 compile path](h7fig:compile)

## Standard library surface

Where the seed lists I/O or runtime commands, they map to the io and call ops.
Verify any keyword with `field-program-combinatronic.py boil quickbasic "<cmd>"`.

- `$INCLUDE`
- `_SCREENSHOW`
- `CIRCLE`
- `CLS`
- `COLOR`
- `DRAW`
- `INT86`
- `INT86X`
- `LINE`
- `LOCATE`
- `MKDIR`
- `PAINT`
- `SCREEN`

## Interop and embedding

QuickBASIC may embed in Queen Code, Grok16 belt builds, or NEXUS panel scripts.
G16 unified driver (`g16`) compiles C/C++ neighbors; python runner hosts dynamic facets.
Use `g16-compile-combinatronics.py` when program facet gates must pass at compile time.

## Secure compile & run chamber

Every QuickBASIC compile and run path is sealed — **no bare host exec**. User code passes
`g16-code-security.py` first, then executes inside `g16-secure-chamber.py` with scrubbed
env (`HOME`, `TMPDIR`, `PATH` limited) so AmmoOS, Hostess 7, and Grok16/bin stay protected.

- **Check:** `g16-secure-chamber.py compile` (stdin JSON: content, lang)
- **Run:** `g16-secure-chamber.py run <path> --lang quickbasic`
- **Posture:** `/api/g16/secure-chamber` · `nexus-g16-bridge.py json` → `secure_chamber`
- **Queen launch:** `runner_policy.quickbasic` = `chamber` in `.launch` manifests
- **Forbidden:** Hostess7, AmmoCode, Grok16/bin, /usr/bin — cannot execute in place

## Performance notes

belt_2_0 native_bsp is the default for hot paths; belt_1_0 python runner applies
when combinatorics bridge degrades the gate. Always-optimal panel pins the best belt
from bench receipts — not guessed from language family alone.

## Research references

Training manuals (school-style textbooks) complement this explaining manual.
See `training_quickbasic` on the Dewey shelf when published.
Field Research book and g16-power-sort plates inform algorithm choices in tooling.

## G16 compile path

- **Boil:** `field-program-combinatronic.py boil quickbasic`
- **Universal facet:** `field-g16-universal-combinatronic.json`
- **Grok16 compile:** `g16-compile-combinatronics.py` with program facet profile
- **Belt runners:** native_bsp (belt_2_0) and python (belt_1_0) per canonical op
- **Secure chamber:** `lib/g16-secure-chamber.py` — mandatory for all 57 Grok16 languages
- **Filetype actions:** `run` / `compile` → `secure_chamber` in field-programming-filetypes.json

## Code patterns

Representative QuickBASIC patterns map to canonical ops as follows:

- **Declaration + assign** → declare, assign
- **Conditional** → branch
- **Iteration** → loop, break, continue
- **Procedure call** → call, return
- **Module boundary** → import, export, module
- **I/O** → io
- **Error handling** → throw, catch

## Pitfalls

- Case sensitivity varies — QuickBASIC keywords may not match heuristic boil.
- Extended packs inherit parent commands; check `extends` in the seed.
- Unknown tokens fall through to heuristic_keywords before defaulting to exec.
- CDN and macro expansion are advisory until combinatronic rebalance runs.
- **Never run QuickBASIC on the bare host** — shell escapes, `eval`, `system`, and JVM/Node
  subprocess calls are blocked transparently; use the sealed chamber lane.
- Missing host toolchains (javac, node, cobc, fpc) return clear errors inside the chamber.

## Where in NEXUS-Shield

- Seed: `data/field-program-combinatronic-seed.json`
- Battery: `field-program-combinatronic.json` (STATE)
- Manual: `library/dewey/000-computer-science/explaining_quickbasic/`
- Reader API: `/api/lang-manuals` · `/api/lang-manuals/quickbasic`
- H7c figures: cover, syntax, op_map, memory, compile (field plate + meld)

- **Extends pack:** `qbasic`

