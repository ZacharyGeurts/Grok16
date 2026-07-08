# Explaining Ruby

![Cover — Explaining Ruby](h7fig:cover)

Hostess 7 programming language manual — complete reference distilled from the
Ruby combinatronic pack and boiled to the g16 program facet (36 canonical ops).

- **Language id:** `ruby`
- **Command entries:** 38
- **Canonical ops used:** 18
- **Generated:** 2026-06-29T12:16:27Z
- **Format:** H7c v3 with embedded figures

## At a glance

- **Paradigm:** oop dynamic
- **Typing:** dynamic strong duck
- **Memory:** gc
- **Year originated:** 1995

Ruby: everything object, blocks, mixins, Rails ecosystem. MRI vs JRuby implementations.

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Introduction

This manual explains every seeded Ruby construct: surface syntax, semantic role,
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
- · **return** — Return / exit function (runner: native_bsp, belt: belt_2_0)
- ✓ **branch** — Branch / if / switch (runner: native_bsp, belt: belt_1_0)
- ✓ **loop** — Loop / iterate / repeat (runner: native_bsp, belt: belt_1_0)
- ✓ **break** — Break / leave loop (runner: native_bsp, belt: belt_1_0)
- ✓ **continue** — Continue / next iteration (runner: native_bsp, belt: belt_1_0)
- ✓ **declare** — Declare / define / let (runner: python, belt: belt_1_0)
- ✓ **type** — Type / typedef / interface (runner: native_bsp, belt: belt_2_0)
- · **cast** — Cast / convert / coerce (runner: native_bsp, belt: belt_2_0)
- · **load** — Load / read memory (runner: native_bsp, belt: belt_2_0)
- · **store** — Store / write memory (runner: native_bsp, belt: belt_2_0)
- ✓ **alloc** — Allocate / new / malloc (runner: native_bsp, belt: belt_2_0)
- ✓ **free** — Free / delete / drop (runner: native_bsp, belt: belt_2_0)
- ✓ **io** — I/O / print / read / write file (runner: python, belt: belt_1_0)
- ✓ **import** — Import / use / require (runner: python, belt: belt_1_0)
- · **export** — Export / pub / module out (runner: native_bsp, belt: belt_2_0)
- ✓ **module** — Module / package / namespace (runner: python, belt: belt_1_0)
- · **compare** — Compare / eq / ord (runner: native_bsp, belt: belt_1_0)
- · **logic** — Logic / and / or / not (runner: native_bsp, belt: belt_1_0)
- · **math** — Math / arithmetic (runner: native_bsp, belt: belt_1_0)
- · **string** — String / format / concat (runner: python, belt: belt_1_0)
- · **struct** — Struct / record / object (runner: native_bsp, belt: belt_2_0)
- · **index** — Index / subscript / slice (runner: python, belt: belt_1_0)
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

## Ruby commands by canonical op

### `alloc` — Allocate / new / malloc

- `new`

### `async` — Async / await / concurrent

- `Fiber`
- `Thread`

### `branch` — Branch / if / switch

- `else`
- `elsif`
- `if`
- `unless`

### `break` — Break / leave loop

- `break`

### `catch` — Catch / rescue / except

- `begin`
- `ensure`
- `rescue`

### `continue` — Continue / next iteration

- `next`
- `redo`

### `declare` — Declare / define / let

- `attr`
- `def`

### `free` — Free / delete / drop

- `delete`

### `import` — Import / use / require

- `extend`
- `include`
- `load`
- `require`

### `io` — I/O / print / read / write file

- `gets`
- `p`
- `print`
- `puts`

### `lambda` — Lambda / closure / fn

- `block`
- `lambda`
- `proc`

### `loop` — Loop / iterate / repeat

- `for`
- `loop`
- `until`
- `while`

### `match` — Pattern match / case

- `case`
- `when`

### `module` — Module / package / namespace

- `module`

### `sync` — Sync / lock / mutex / atomic

- `Mutex`

### `throw` — Throw / raise / panic

- `raise`

### `type` — Type / typedef / interface

- `class`

### `yield` — Yield / generator / coroutine

- `yield`

## Ruby full command reference

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "new"`

### `Fiber`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "Fiber"`

### `Thread`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "Thread"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "else"`

### `elsif`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "elsif"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "if"`

### `unless`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "unless"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "break"`

### `begin`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "begin"`

### `ensure`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "ensure"`

### `rescue`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "rescue"`

### `next`
- **Boils to:** `continue` — Continue / next iteration
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "next"`

### `redo`
- **Boils to:** `continue` — Continue / next iteration
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "redo"`

### `attr`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "attr"`

### `def`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "def"`

### `delete`
- **Boils to:** `free` — Free / delete / drop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "delete"`

### `extend`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "extend"`

### `include`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "include"`

### `load`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "load"`

### `require`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "require"`

### `gets`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "gets"`

### `p`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "p"`

### `print`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "print"`

### `puts`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "puts"`

### `block`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "block"`

### `lambda`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "lambda"`

### `proc`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "proc"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "for"`

### `loop`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "loop"`

### `until`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "until"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "while"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "case"`

### `when`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "when"`

### `module`
- **Boils to:** `module` — Module / package / namespace
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "module"`

### `Mutex`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "Mutex"`

### `raise`
- **Boils to:** `throw` — Throw / raise / panic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "raise"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "class"`

### `yield`
- **Boils to:** `yield` — Yield / generator / coroutine
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil ruby "yield"`

## Execution model

Ruby programs execute through the Field program combinatronic facet. Surface syntax
maps to 36 canonical ops; each op selects a belt runner (native_bsp on belt_2_0 or
python on belt_1_0). The explaining manual documents semantics — not a tutorial walkthrough.

- **Paradigm:** oop dynamic
- **Typing discipline:** dynamic strong duck
- **Memory:** gc
- **Commands in seed:** 38
- **Canonical ops exercised:** 18

![Memory and objects](h7fig:memory)

## Lexical structure

Tokens partition into identifiers, literals, operators, and significant whitespace
per Ruby reference rules. Hostess7 boil heuristics treat unknown tokens as exec
unless a seed keyword maps them. Extended packs inherit parent commands.

- `attr` → `declare`
- `begin` → `catch`
- `block` → `lambda`
- `break` → `break`
- `case` → `match`
- `class` → `type`
- `def` → `declare`
- `delete` → `free`
- `else` → `branch`
- `elsif` → `branch`
- `ensure` → `catch`
- `extend` → `import`
- `Fiber` → `async`
- `for` → `loop`
- `gets` → `io`
- `if` → `branch`
- `include` → `import`
- `lambda` → `lambda`
- `load` → `import`
- `loop` → `loop`
- `module` → `module`
- `Mutex` → `sync`
- `new` → `alloc`
- `next` → `continue`

## Type and value space

Ruby: everything object, blocks, mixins, Rails ecosystem. MRI vs JRuby implementations.

## Control flow

branch · loop · break · continue · return — all languages converge on these atoms.
In Ruby, control constructs in the seed pack boil as follows:

- **branch:** `if`, `elsif`, `else`, `unless`
- **loop:** `for`, `while`, `until`, `loop`
- **throw:** `raise`

## Modules and boundaries

import · export · module · package — boundary ops isolate compilation units.
NEXUS-Shield indexes each manual under Dewey 000; combinatronic rebalance may extend packs.

![G16 compile path](h7fig:compile)

## Standard library surface

Where the seed lists I/O or runtime commands, they map to the io and call ops.
Verify any keyword with `field-program-combinatronic.py boil ruby "<cmd>"`.

- `extend`
- `gets`
- `include`
- `load`
- `p`
- `print`
- `puts`
- `require`

## Interop and embedding

Ruby may embed in Queen Code, Grok16 belt builds, or NEXUS panel scripts.
G16 unified driver (`g16`) compiles C/C++ neighbors; python runner hosts dynamic facets.
Use `g16-compile-combinatronics.py` when program facet gates must pass at compile time.

## Secure compile & run chamber

Every Ruby compile and run path is sealed — **no bare host exec**. User code passes
`g16-code-security.py` first, then executes inside `g16-secure-chamber.py` with scrubbed
env (`HOME`, `TMPDIR`, `PATH` limited) so AmmoOS, Hostess 7, and Grok16/bin stay protected.

- **Check:** `g16-secure-chamber.py compile` (stdin JSON: content, lang)
- **Run:** `g16-secure-chamber.py run <path> --lang ruby`
- **Posture:** `/api/g16/secure-chamber` · `nexus-g16-bridge.py json` → `secure_chamber`
- **Queen launch:** `runner_policy.ruby` = `chamber` in `.launch` manifests
- **Forbidden:** Hostess7, AmmoCode, Grok16/bin, /usr/bin — cannot execute in place

## Performance notes

belt_2_0 native_bsp is the default for hot paths; belt_1_0 python runner applies
when combinatorics bridge degrades the gate. Always-optimal panel pins the best belt
from bench receipts — not guessed from language family alone.

## Research references

Training manuals (school-style textbooks) complement this explaining manual.
See `training_ruby` on the Dewey shelf when published.
Field Research book and g16-power-sort plates inform algorithm choices in tooling.

## G16 compile path

- **Boil:** `field-program-combinatronic.py boil ruby`
- **Universal facet:** `field-g16-universal-combinatronic.json`
- **Grok16 compile:** `g16-compile-combinatronics.py` with program facet profile
- **Belt runners:** native_bsp (belt_2_0) and python (belt_1_0) per canonical op
- **Secure chamber:** `lib/g16-secure-chamber.py` — mandatory for all 57 Grok16 languages
- **Filetype actions:** `run` / `compile` → `secure_chamber` in field-programming-filetypes.json

## Code patterns

Representative Ruby patterns map to canonical ops as follows:

- **Declaration + assign** → declare, assign
- **Conditional** → branch
- **Iteration** → loop, break, continue
- **Procedure call** → call, return
- **Module boundary** → import, export, module
- **I/O** → io
- **Error handling** → throw, catch

## Pitfalls

- Case sensitivity varies — Ruby keywords may not match heuristic boil.
- Extended packs inherit parent commands; check `extends` in the seed.
- Unknown tokens fall through to heuristic_keywords before defaulting to exec.
- CDN and macro expansion are advisory until combinatronic rebalance runs.
- **Never run Ruby on the bare host** — shell escapes, `eval`, `system`, and JVM/Node
  subprocess calls are blocked transparently; use the sealed chamber lane.
- Missing host toolchains (javac, node, cobc, fpc) return clear errors inside the chamber.

## Where in NEXUS-Shield

- Seed: `data/field-program-combinatronic-seed.json`
- Battery: `field-program-combinatronic.json` (STATE)
- Manual: `library/dewey/000-computer-science/explaining_ruby/`
- Reader API: `/api/lang-manuals` · `/api/lang-manuals/ruby`
- H7c figures: cover, syntax, op_map, memory, compile (field plate + meld)

