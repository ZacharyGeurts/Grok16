# Explaining Rust

![Cover — Explaining Rust](h7fig:cover)

Hostess 7 programming language manual — complete reference distilled from the
Rust combinatronic pack and boiled to the g16 program facet (36 canonical ops).

- **Language id:** `rust`
- **Command entries:** 52
- **Canonical ops used:** 24
- **Generated:** 2026-06-29T12:17:03Z
- **Format:** H7c v3 with embedded figures

## At a glance

- **Paradigm:** multi-paradigm
- **Typing:** static strong
- **Memory:** ownership
- **Year originated:** 2010

Rust: ownership, borrowing, lifetimes — compile-time memory safety without GC. unsafe for FFI. Cargo ecosystem. Ideal mental model for Hostess systems advice alongside C++ Field code.

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Introduction

This manual explains every seeded Rust construct: surface syntax, semantic role,
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
- ✓ **assign** — Assign / bind / set (runner: python, belt: belt_1_0)
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
- ✓ **throw** — Throw / raise / panic (runner: native_bsp, belt: belt_2_0)
- · **catch** — Catch / rescue / except (runner: native_bsp, belt: belt_2_0)
- · **yield** — Yield / generator / coroutine (runner: python, belt: belt_1_0)
- · **lambda** — Lambda / closure / fn (runner: python, belt: belt_1_0)
- ✓ **match** — Pattern match / case (runner: native_bsp, belt: belt_2_0)
- ✓ **async** — Async / await / concurrent (runner: python, belt: belt_1_0)
- ✓ **sync** — Sync / lock / mutex / atomic (runner: native_bsp, belt: belt_2_0)
- ✓ **asm** — Inline asm / intrinsics (runner: native_bsp, belt: belt_2_0)
- ✓ **unsafe** — Unsafe / raw pointer (runner: native_bsp, belt: belt_2_0)
- ✓ **meta** — Macro / reflection / eval (runner: python, belt: belt_1_0)
- · **query** — Query / select / SQL (runner: python, belt: belt_1_0)

## Rust commands by canonical op

### `alloc` — Allocate / new / malloc

- `Box::new`
- `Vec::new`

### `asm` — Inline asm / intrinsics

- `asm!`

### `assign` — Assign / bind / set

- `move`

### `async` — Async / await / concurrent

- `async`
- `await`
- `spawn`

### `branch` — Branch / if / switch

- `else`
- `if`

### `break` — Break / leave loop

- `break`

### `call` — Call / invoke / apply

- `clone`
- `expect`
- `unwrap`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `const`
- `fn`
- `let`
- `mut`
- `None`
- `Some`
- `static`

### `export` — Export / pub / module out

- `pub`

### `free` — Free / delete / drop

- `drop`

### `import` — Import / use / require

- `use`

### `io` — I/O / print / read / write file

- `print!`
- `println!`
- `read`
- `write`

### `load` — Load / read memory

- `deref`
- `ref`

### `loop` — Loop / iterate / repeat

- `for`
- `loop`
- `while`

### `match` — Pattern match / case

- `match`

### `meta` — Macro / reflection / eval

- `#[`
- `derive`
- `macro_rules!`

### `module` — Module / package / namespace

- `crate`
- `mod`

### `return` — Return / exit function

- `return`

### `struct` — Struct / record / object

- `struct`

### `sync` — Sync / lock / mutex / atomic

- `Arc`
- `Mutex`

### `throw` — Throw / raise / panic

- `?`

### `type` — Type / typedef / interface

- `enum`
- `impl`
- `Option`
- `Result`
- `trait`
- `type`

### `unsafe` — Unsafe / raw pointer

- `transmute`
- `unsafe`

## Rust full command reference

### `Box::new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "Box::new"`

### `Vec::new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "Vec::new"`

### `asm!`
- **Boils to:** `asm` — Inline asm / intrinsics
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "asm!"`

### `move`
- **Boils to:** `assign` — Assign / bind / set
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "move"`

### `async`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "async"`

### `await`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "await"`

### `spawn`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "spawn"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "else"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "if"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "break"`

### `clone`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "clone"`

### `expect`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "expect"`

### `unwrap`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "unwrap"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "continue"`

### `const`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "const"`

### `fn`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "fn"`

### `let`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "let"`

### `mut`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "mut"`

### `None`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "None"`

### `Some`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "Some"`

### `static`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "static"`

### `pub`
- **Boils to:** `export` — Export / pub / module out
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "pub"`

### `drop`
- **Boils to:** `free` — Free / delete / drop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "drop"`

### `use`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "use"`

### `print!`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "print!"`

### `println!`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "println!"`

### `read`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "read"`

### `write`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "write"`

### `deref`
- **Boils to:** `load` — Load / read memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "deref"`

### `ref`
- **Boils to:** `load` — Load / read memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "ref"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "for"`

### `loop`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "loop"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "while"`

### `match`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "match"`

### `#[`
- **Boils to:** `meta` — Macro / reflection / eval
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "#["`

### `derive`
- **Boils to:** `meta` — Macro / reflection / eval
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "derive"`

### `macro_rules!`
- **Boils to:** `meta` — Macro / reflection / eval
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "macro_rules!"`

### `crate`
- **Boils to:** `module` — Module / package / namespace
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "crate"`

### `mod`
- **Boils to:** `module` — Module / package / namespace
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "mod"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "return"`

### `struct`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "struct"`

### `Arc`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "Arc"`

### `Mutex`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "Mutex"`

### `?`
- **Boils to:** `throw` — Throw / raise / panic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "?"`

### `enum`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "enum"`

### `impl`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "impl"`

### `Option`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "Option"`

### `Result`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "Result"`

### `trait`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "trait"`

### `type`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "type"`

### `transmute`
- **Boils to:** `unsafe` — Unsafe / raw pointer
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "transmute"`

### `unsafe`
- **Boils to:** `unsafe` — Unsafe / raw pointer
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil rust "unsafe"`

## Execution model

Rust programs execute through the Field program combinatronic facet. Surface syntax
maps to 36 canonical ops; each op selects a belt runner (native_bsp on belt_2_0 or
python on belt_1_0). The explaining manual documents semantics — not a tutorial walkthrough.

- **Paradigm:** multi-paradigm
- **Typing discipline:** static strong
- **Memory:** ownership
- **Commands in seed:** 52
- **Canonical ops exercised:** 24

![Memory and objects](h7fig:memory)

## Lexical structure

Tokens partition into identifiers, literals, operators, and significant whitespace
per Rust reference rules. Hostess7 boil heuristics treat unknown tokens as exec
unless a seed keyword maps them. Extended packs inherit parent commands.

- `#[` → `meta`
- `?` → `throw`
- `Arc` → `sync`
- `asm!` → `asm`
- `async` → `async`
- `await` → `async`
- `Box::new` → `alloc`
- `break` → `break`
- `clone` → `call`
- `const` → `declare`
- `continue` → `continue`
- `crate` → `module`
- `deref` → `load`
- `derive` → `meta`
- `drop` → `free`
- `else` → `branch`
- `enum` → `type`
- `expect` → `call`
- `fn` → `declare`
- `for` → `loop`
- `if` → `branch`
- `impl` → `type`
- `let` → `declare`
- `loop` → `loop`

## Type and value space

Rust: ownership, borrowing, lifetimes — compile-time memory safety without GC. unsafe for FFI. Cargo ecosystem. Ideal mental model for Hostess systems advice alongside C++ Field code.

## Control flow

branch · loop · break · continue · return — all languages converge on these atoms.
In Rust, control constructs in the seed pack boil as follows:

- **branch:** `if`, `else`
- **loop:** `loop`, `while`, `for`
- **return:** `return`
- **throw:** `?`

## Modules and boundaries

import · export · module · package — boundary ops isolate compilation units.
NEXUS-Shield indexes each manual under Dewey 000; combinatronic rebalance may extend packs.

![G16 compile path](h7fig:compile)

## Standard library surface

Where the seed lists I/O or runtime commands, they map to the io and call ops.
Verify any keyword with `field-program-combinatronic.py boil rust "<cmd>"`.

- `clone`
- `expect`
- `print!`
- `println!`
- `read`
- `unwrap`
- `use`
- `write`

## Interop and embedding

Rust may embed in Queen Code, Grok16 belt builds, or NEXUS panel scripts.
G16 unified driver (`g16`) compiles C/C++ neighbors; python runner hosts dynamic facets.
Use `g16-compile-combinatronics.py` when program facet gates must pass at compile time.

## Secure compile & run chamber

Every Rust compile and run path is sealed — **no bare host exec**. User code passes
`g16-code-security.py` first, then executes inside `g16-secure-chamber.py` with scrubbed
env (`HOME`, `TMPDIR`, `PATH` limited) so AmmoOS, Hostess 7, and Grok16/bin stay protected.

- **Check:** `g16-secure-chamber.py compile` (stdin JSON: content, lang)
- **Run:** `g16-secure-chamber.py run <path> --lang rust`
- **Posture:** `/api/g16/secure-chamber` · `nexus-g16-bridge.py json` → `secure_chamber`
- **Queen launch:** `runner_policy.rust` = `chamber` in `.launch` manifests
- **Forbidden:** Hostess7, AmmoCode, Grok16/bin, /usr/bin — cannot execute in place

## Performance notes

belt_2_0 native_bsp is the default for hot paths; belt_1_0 python runner applies
when combinatorics bridge degrades the gate. Always-optimal panel pins the best belt
from bench receipts — not guessed from language family alone.

## Research references

Training manuals (school-style textbooks) complement this explaining manual.
See `training_rust` on the Dewey shelf when published.
Field Research book and g16-power-sort plates inform algorithm choices in tooling.

## G16 compile path

- **Boil:** `field-program-combinatronic.py boil rust`
- **Universal facet:** `field-g16-universal-combinatronic.json`
- **Grok16 compile:** `g16-compile-combinatronics.py` with program facet profile
- **Belt runners:** native_bsp (belt_2_0) and python (belt_1_0) per canonical op
- **Secure chamber:** `lib/g16-secure-chamber.py` — mandatory for all 57 Grok16 languages
- **Filetype actions:** `run` / `compile` → `secure_chamber` in field-programming-filetypes.json

## Code patterns

Representative Rust patterns map to canonical ops as follows:

- **Declaration + assign** → declare, assign
- **Conditional** → branch
- **Iteration** → loop, break, continue
- **Procedure call** → call, return
- **Module boundary** → import, export, module
- **I/O** → io
- **Error handling** → throw, catch

## Pitfalls

- Case sensitivity varies — Rust keywords may not match heuristic boil.
- Extended packs inherit parent commands; check `extends` in the seed.
- Unknown tokens fall through to heuristic_keywords before defaulting to exec.
- CDN and macro expansion are advisory until combinatronic rebalance runs.
- **Never run Rust on the bare host** — shell escapes, `eval`, `system`, and JVM/Node
  subprocess calls are blocked transparently; use the sealed chamber lane.
- Missing host toolchains (javac, node, cobc, fpc) return clear errors inside the chamber.

## Where in NEXUS-Shield

- Seed: `data/field-program-combinatronic-seed.json`
- Battery: `field-program-combinatronic.json` (STATE)
- Manual: `library/dewey/000-computer-science/explaining_rust/`
- Reader API: `/api/lang-manuals` · `/api/lang-manuals/rust`
- H7c figures: cover, syntax, op_map, memory, compile (field plate + meld)

