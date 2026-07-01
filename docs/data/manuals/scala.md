# Explaining Scala

![Cover — Explaining Scala](h7fig:cover)

Hostess 7 programming language manual — complete reference distilled from the
Scala combinatronic pack and boiled to the g16 program facet (36 canonical ops).

- **Language id:** `scala`
- **Command entries:** 30
- **Canonical ops used:** 17
- **Generated:** 2026-06-29T12:17:40Z
- **Format:** H7c v3 with embedded figures

## At a glance

- **Paradigm:** functional+oop
- **Typing:** static strong
- **Memory:** gc
- **Year originated:** 2004

Scala: JVM language — case classes, pattern matching, implicits, Akka actors.

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Introduction

This manual explains every seeded Scala construct: surface syntax, semantic role,
canonical combinatronic op, belt runner, and NEXUS-Shield integration paths.
Use the GUI reader (`/field-lang-manuals`) or text mode (`field-lang-manual-reader.py text`).

## Reading guide

1. **At a glance** — paradigm, typing, memory model.
2. **Canonical atoms** — the 36 ops all languages boil to.
3. **Commands by op** — every keyword grouped by canonical target.
4. **Full command index** — alphabetical reference.
5. **G16 & NEXUS** — compile, belt, API, pitfalls.

## Canonical combinatronic atoms

- · **exec** — Execute / eval / run (runner: native_bsp, belt: belt_2_0)
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
- · **load** — Load / read memory (runner: native_bsp, belt: belt_2_0)
- · **store** — Store / write memory (runner: native_bsp, belt: belt_2_0)
- · **alloc** — Allocate / new / malloc (runner: native_bsp, belt: belt_2_0)
- · **free** — Free / delete / drop (runner: native_bsp, belt: belt_2_0)
- ✓ **io** — I/O / print / read / write file (runner: python, belt: belt_1_0)
- ✓ **import** — Import / use / require (runner: python, belt: belt_1_0)
- · **export** — Export / pub / module out (runner: native_bsp, belt: belt_2_0)
- ✓ **module** — Module / package / namespace (runner: python, belt: belt_1_0)
- · **compare** — Compare / eq / ord (runner: native_bsp, belt: belt_1_0)
- · **logic** — Logic / and / or / not (runner: native_bsp, belt: belt_1_0)
- · **math** — Math / arithmetic (runner: native_bsp, belt: belt_1_0)
- · **string** — String / format / concat (runner: python, belt: belt_1_0)
- ✓ **struct** — Struct / record / object (runner: native_bsp, belt: belt_2_0)
- · **index** — Index / subscript / slice (runner: python, belt: belt_1_0)
- ✓ **throw** — Throw / raise / panic (runner: native_bsp, belt: belt_2_0)
- ✓ **catch** — Catch / rescue / except (runner: native_bsp, belt: belt_2_0)
- · **yield** — Yield / generator / coroutine (runner: python, belt: belt_1_0)
- ✓ **lambda** — Lambda / closure / fn (runner: python, belt: belt_1_0)
- ✓ **match** — Pattern match / case (runner: native_bsp, belt: belt_2_0)
- ✓ **async** — Async / await / concurrent (runner: python, belt: belt_1_0)
- ✓ **sync** — Sync / lock / mutex / atomic (runner: native_bsp, belt: belt_2_0)
- · **asm** — Inline asm / intrinsics (runner: native_bsp, belt: belt_2_0)
- · **unsafe** — Unsafe / raw pointer (runner: native_bsp, belt: belt_2_0)
- · **meta** — Macro / reflection / eval (runner: python, belt: belt_1_0)
- · **query** — Query / select / SQL (runner: python, belt: belt_1_0)

## Scala commands by canonical op

### `async` — Async / await / concurrent

- `await`
- `Future`

### `branch` — Branch / if / switch

- `else`
- `if`

### `break` — Break / leave loop

- `break`

### `catch` — Catch / rescue / except

- `catch`
- `finally`
- `try`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `def`
- `lazy`
- `val`
- `var`

### `import` — Import / use / require

- `import`

### `io` — I/O / print / read / write file

- `print`
- `println`

### `lambda` — Lambda / closure / fn

- `=>`

### `loop` — Loop / iterate / repeat

- `do`
- `for`
- `while`

### `match` — Pattern match / case

- `case`
- `match`

### `module` — Module / package / namespace

- `package`

### `return` — Return / exit function

- `return`

### `struct` — Struct / record / object

- `case class`
- `object`

### `sync` — Sync / lock / mutex / atomic

- `synchronized`

### `throw` — Throw / raise / panic

- `throw`

### `type` — Type / typedef / interface

- `class`
- `trait`

## Scala full command reference

### `await`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "await"`

### `Future`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "Future"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "else"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "if"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "break"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "catch"`

### `finally`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "finally"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "try"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "continue"`

### `def`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "def"`

### `lazy`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "lazy"`

### `val`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "val"`

### `var`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "var"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "import"`

### `print`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "print"`

### `println`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "println"`

### `=>`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "=>"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "do"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "for"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "while"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "case"`

### `match`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "match"`

### `package`
- **Boils to:** `module` — Module / package / namespace
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "package"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "return"`

### `case class`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "case class"`

### `object`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "object"`

### `synchronized`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "synchronized"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "throw"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "class"`

### `trait`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil scala "trait"`

## Execution model

Scala programs execute through the Field program combinatronic facet. Surface syntax
maps to 36 canonical ops; each op selects a belt runner (native_bsp on belt_2_0 or
python on belt_1_0). The explaining manual documents semantics — not a tutorial walkthrough.

- **Paradigm:** functional+oop
- **Typing discipline:** static strong
- **Memory:** gc
- **Commands in seed:** 30
- **Canonical ops exercised:** 17

![Memory and objects](h7fig:memory)

## Lexical structure

Tokens partition into identifiers, literals, operators, and significant whitespace
per Scala reference rules. Hostess7 boil heuristics treat unknown tokens as exec
unless a seed keyword maps them. Extended packs inherit parent commands.

- `=>` → `lambda`
- `await` → `async`
- `break` → `break`
- `case` → `match`
- `case class` → `struct`
- `catch` → `catch`
- `class` → `type`
- `continue` → `continue`
- `def` → `declare`
- `do` → `loop`
- `else` → `branch`
- `finally` → `catch`
- `for` → `loop`
- `Future` → `async`
- `if` → `branch`
- `import` → `import`
- `lazy` → `declare`
- `match` → `match`
- `object` → `struct`
- `package` → `module`
- `print` → `io`
- `println` → `io`
- `return` → `return`
- `synchronized` → `sync`

## Type and value space

Scala: JVM language — case classes, pattern matching, implicits, Akka actors.

## Control flow

branch · loop · break · continue · return — all languages converge on these atoms.
In Scala, control constructs in the seed pack boil as follows:

- **branch:** `if`, `else`
- **loop:** `for`, `while`, `do`
- **return:** `return`
- **throw:** `throw`

## Modules and boundaries

import · export · module · package — boundary ops isolate compilation units.
NEXUS-Shield indexes each manual under Dewey 000; combinatronic rebalance may extend packs.

![G16 compile path](h7fig:compile)

## Standard library surface

Where the seed lists I/O or runtime commands, they map to the io and call ops.
Verify any keyword with `field-program-combinatronic.py boil scala "<cmd>"`.

- `import`
- `print`
- `println`

## Interop and embedding

Scala may embed in Queen Code, Grok16 belt builds, or NEXUS panel scripts.
G16 unified driver (`g16`) compiles C/C++ neighbors; python runner hosts dynamic facets.
Use `g16-compile-combinatronics.py` when program facet gates must pass at compile time.

## Secure compile & run chamber

Every Scala compile and run path is sealed — **no bare host exec**. User code passes
`g16-code-security.py` first, then executes inside `g16-secure-chamber.py` with scrubbed
env (`HOME`, `TMPDIR`, `PATH` limited) so AmmoOS, Hostess 7, and Grok16/bin stay protected.

- **Check:** `g16-secure-chamber.py compile` (stdin JSON: content, lang)
- **Run:** `g16-secure-chamber.py run <path> --lang scala`
- **Posture:** `/api/g16/secure-chamber` · `nexus-g16-bridge.py json` → `secure_chamber`
- **Queen launch:** `runner_policy.scala` = `chamber` in `.launch` manifests
- **Forbidden:** Hostess7, AmmoCode, Grok16/bin, /usr/bin — cannot execute in place

## Performance notes

belt_2_0 native_bsp is the default for hot paths; belt_1_0 python runner applies
when combinatorics bridge degrades the gate. Always-optimal panel pins the best belt
from bench receipts — not guessed from language family alone.

## Research references

Training manuals (school-style textbooks) complement this explaining manual.
See `training_scala` on the Dewey shelf when published.
Field Research book and g16-power-sort plates inform algorithm choices in tooling.

## G16 compile path

- **Boil:** `field-program-combinatronic.py boil scala`
- **Universal facet:** `field-g16-universal-combinatronic.json`
- **Grok16 compile:** `g16-compile-combinatronics.py` with program facet profile
- **Belt runners:** native_bsp (belt_2_0) and python (belt_1_0) per canonical op
- **Secure chamber:** `lib/g16-secure-chamber.py` — mandatory for all 57 Grok16 languages
- **Filetype actions:** `run` / `compile` → `secure_chamber` in field-programming-filetypes.json

## Code patterns

Representative Scala patterns map to canonical ops as follows:

- **Declaration + assign** → declare, assign
- **Conditional** → branch
- **Iteration** → loop, break, continue
- **Procedure call** → call, return
- **Module boundary** → import, export, module
- **I/O** → io
- **Error handling** → throw, catch

## Pitfalls

- Case sensitivity varies — Scala keywords may not match heuristic boil.
- Extended packs inherit parent commands; check `extends` in the seed.
- Unknown tokens fall through to heuristic_keywords before defaulting to exec.
- CDN and macro expansion are advisory until combinatronic rebalance runs.
- **Never run Scala on the bare host** — shell escapes, `eval`, `system`, and JVM/Node
  subprocess calls are blocked transparently; use the sealed chamber lane.
- Missing host toolchains (javac, node, cobc, fpc) return clear errors inside the chamber.

## Where in NEXUS-Shield

- Seed: `data/field-program-combinatronic-seed.json`
- Battery: `field-program-combinatronic.json` (STATE)
- Manual: `library/dewey/000-computer-science/explaining_scala/`
- Reader API: `/api/lang-manuals` · `/api/lang-manuals/scala`
- H7c figures: cover, syntax, op_map, memory, compile (field plate + meld)

