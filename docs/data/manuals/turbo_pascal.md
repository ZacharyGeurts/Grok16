# Explaining Turbo Pascal

![Cover — Explaining Turbo Pascal](h7fig:cover)

Hostess 7 programming language manual — complete reference distilled from the
Turbo Pascal combinatronic pack and boiled to the g16 program facet (36 canonical ops).

- **Language id:** `turbo_pascal`
- **Command entries:** 81
- **Canonical ops used:** 23
- **Generated:** 2026-06-29T12:21:15Z
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

This manual explains every seeded Turbo Pascal construct: surface syntax, semantic role,
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
- ✓ **store** — Store / write memory (runner: native_bsp, belt: belt_2_0)
- ✓ **alloc** — Allocate / new / malloc (runner: native_bsp, belt: belt_2_0)
- ✓ **free** — Free / delete / drop (runner: native_bsp, belt: belt_2_0)
- ✓ **io** — I/O / print / read / write file (runner: python, belt: belt_1_0)
- ✓ **import** — Import / use / require (runner: python, belt: belt_1_0)
- ✓ **export** — Export / pub / module out (runner: native_bsp, belt: belt_2_0)
- ✓ **module** — Module / package / namespace (runner: python, belt: belt_1_0)
- · **compare** — Compare / eq / ord (runner: native_bsp, belt: belt_1_0)
- · **logic** — Logic / and / or / not (runner: native_bsp, belt: belt_1_0)
- ✓ **math** — Math / arithmetic (runner: native_bsp, belt: belt_1_0)
- · **string** — String / format / concat (runner: python, belt: belt_1_0)
- ✓ **struct** — Struct / record / object (runner: native_bsp, belt: belt_2_0)
- · **index** — Index / subscript / slice (runner: python, belt: belt_1_0)
- ✓ **throw** — Throw / raise / panic (runner: native_bsp, belt: belt_2_0)
- · **catch** — Catch / rescue / except (runner: native_bsp, belt: belt_2_0)
- · **yield** — Yield / generator / coroutine (runner: python, belt: belt_1_0)
- · **lambda** — Lambda / closure / fn (runner: python, belt: belt_1_0)
- ✓ **match** — Pattern match / case (runner: native_bsp, belt: belt_2_0)
- · **async** — Async / await / concurrent (runner: python, belt: belt_1_0)
- · **sync** — Sync / lock / mutex / atomic (runner: native_bsp, belt: belt_2_0)
- ✓ **asm** — Inline asm / intrinsics (runner: native_bsp, belt: belt_2_0)
- · **unsafe** — Unsafe / raw pointer (runner: native_bsp, belt: belt_2_0)
- ✓ **meta** — Macro / reflection / eval (runner: python, belt: belt_1_0)
- · **query** — Query / select / SQL (runner: python, belt: belt_1_0)

## Turbo Pascal commands by canonical op

### `alloc` — Allocate / new / malloc

- `getmem`
- `new`

### `asm` — Inline asm / intrinsics

- `assembler`
- `inline`
- `interrupt`

### `branch` — Branch / if / switch

- `else`
- `goto`
- `if`
- `then`

### `break` — Break / leave loop

- `break`

### `call` — Call / invoke / apply

- `ParamCount`
- `SizeOf`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `$F`
- `$M`
- `absolute`
- `const`
- `external`
- `far`
- `function`
- `near`
- `Overlay`
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

- `$I`
- `$O`
- `CRT`
- `Dos`
- `System`
- `Units`
- `uses`
- `Windows`
- `WinProcs`

### `io` — I/O / print / read / write file

- `closefile`
- `file`
- `FillChar`
- `Graph`
- `ParamStr`
- `port`
- `read`
- `readln`
- `reset`
- `rewrite`
- `text`
- `write`
- `writeln`

### `load` — Load / read memory

- `mem`
- `ofs`
- `seg`
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

### `math` — Math / arithmetic

- `Random`
- `Swap`

### `meta` — Macro / reflection / eval

- `$R`
- `$U`

### `module` — Module / package / namespace

- `implementation`
- `program`
- `unit`

### `return` — Return / exit function

- `end`
- `end.`
- `exit`
- `Halt`

### `store` — Store / write memory

- `Move`

### `struct` — Struct / record / object

- `array`
- `record`
- `set`

### `throw` — Throw / raise / panic

- `RunError`

### `type` — Type / typedef / interface

- `packed`
- `type`

## Turbo Pascal full command reference

### `getmem`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "getmem"`

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "new"`

### `assembler`
- **Boils to:** `asm` — Inline asm / intrinsics
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "assembler"`

### `inline`
- **Boils to:** `asm` — Inline asm / intrinsics
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "inline"`

### `interrupt`
- **Boils to:** `asm` — Inline asm / intrinsics
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "interrupt"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "else"`

### `goto`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "goto"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "if"`

### `then`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "then"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "break"`

### `ParamCount`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "ParamCount"`

### `SizeOf`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "SizeOf"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "continue"`

### `$F`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "$F"`

### `$M`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "$M"`

### `absolute`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "absolute"`

### `const`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "const"`

### `external`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "external"`

### `far`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "far"`

### `function`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "function"`

### `near`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "near"`

### `Overlay`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "Overlay"`

### `procedure`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "procedure"`

### `var`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "var"`

### `begin`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "begin"`

### `interface`
- **Boils to:** `export` — Export / pub / module out
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "interface"`

### `dispose`
- **Boils to:** `free` — Free / delete / drop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "dispose"`

### `freemem`
- **Boils to:** `free` — Free / delete / drop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "freemem"`

### `$I`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "$I"`

### `$O`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "$O"`

### `CRT`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "CRT"`

### `Dos`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "Dos"`

### `System`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "System"`

### `Units`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "Units"`

### `uses`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "uses"`

### `Windows`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "Windows"`

### `WinProcs`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "WinProcs"`

### `closefile`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "closefile"`

### `file`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "file"`

### `FillChar`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "FillChar"`

### `Graph`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "Graph"`

### `ParamStr`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "ParamStr"`

### `port`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "port"`

### `read`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "read"`

### `readln`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "readln"`

### `reset`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "reset"`

### `rewrite`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "rewrite"`

### `text`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "text"`

### `write`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "write"`

### `writeln`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "writeln"`

### `mem`
- **Boils to:** `load` — Load / read memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "mem"`

### `ofs`
- **Boils to:** `load` — Load / read memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "ofs"`

### `seg`
- **Boils to:** `load` — Load / read memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "seg"`

### `with`
- **Boils to:** `load` — Load / read memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "with"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "do"`

### `downto`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "downto"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "for"`

### `repeat`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "repeat"`

### `to`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "to"`

### `until`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "until"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "while"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "case"`

### `of`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "of"`

### `Random`
- **Boils to:** `math` — Math / arithmetic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "Random"`

### `Swap`
- **Boils to:** `math` — Math / arithmetic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "Swap"`

### `$R`
- **Boils to:** `meta` — Macro / reflection / eval
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "$R"`

### `$U`
- **Boils to:** `meta` — Macro / reflection / eval
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "$U"`

### `implementation`
- **Boils to:** `module` — Module / package / namespace
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "implementation"`

### `program`
- **Boils to:** `module` — Module / package / namespace
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "program"`

### `unit`
- **Boils to:** `module` — Module / package / namespace
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "unit"`

### `end`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "end"`

### `end.`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "end."`

### `exit`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "exit"`

### `Halt`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "Halt"`

### `Move`
- **Boils to:** `store` — Store / write memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "Move"`

### `array`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "array"`

### `record`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "record"`

### `set`
- **Boils to:** `struct` — Struct / record / object
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "set"`

### `RunError`
- **Boils to:** `throw` — Throw / raise / panic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "RunError"`

### `packed`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "packed"`

### `type`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil turbo_pascal "type"`

## Execution model

Turbo Pascal programs execute through the Field program combinatronic facet. Surface syntax
maps to 36 canonical ops; each op selects a belt runner (native_bsp on belt_2_0 or
python on belt_1_0). The explaining manual documents semantics — not a tutorial walkthrough.

- **Paradigm:** imperative
- **Typing discipline:** static strong
- **Memory:** manual
- **Commands in seed:** 81
- **Canonical ops exercised:** 23

![Memory and objects](h7fig:memory)

## Lexical structure

Tokens partition into identifiers, literals, operators, and significant whitespace
per Turbo Pascal reference rules. Hostess7 boil heuristics treat unknown tokens as exec
unless a seed keyword maps them. Extended packs inherit parent commands.

- `$F` → `declare`
- `$I` → `import`
- `$M` → `declare`
- `$O` → `import`
- `$R` → `meta`
- `$U` → `meta`
- `absolute` → `declare`
- `array` → `struct`
- `assembler` → `asm`
- `begin` → `exec`
- `break` → `break`
- `case` → `match`
- `closefile` → `io`
- `const` → `declare`
- `continue` → `continue`
- `CRT` → `import`
- `dispose` → `free`
- `do` → `loop`
- `Dos` → `import`
- `downto` → `loop`
- `else` → `branch`
- `end` → `return`
- `end.` → `return`
- `exit` → `return`

## Type and value space

Pascal: structured programming teaching language — strong typing, nested procedures. Delphi/Object Pascal OOP extension.

## Control flow

branch · loop · break · continue · return — all languages converge on these atoms.
In Turbo Pascal, control constructs in the seed pack boil as follows:

- **branch:** `if`, `then`, `else`, `goto`
- **loop:** `for`, `to`, `downto`, `do`, `while`, `repeat`, `until`
- **return:** `end`, `end.`, `exit`, `Halt`
- **throw:** `RunError`

## Modules and boundaries

import · export · module · package — boundary ops isolate compilation units.
NEXUS-Shield indexes each manual under Dewey 000; combinatronic rebalance may extend packs.

![G16 compile path](h7fig:compile)

## Standard library surface

Where the seed lists I/O or runtime commands, they map to the io and call ops.
Verify any keyword with `field-program-combinatronic.py boil turbo_pascal "<cmd>"`.

- `$I`
- `$O`
- `closefile`
- `CRT`
- `Dos`
- `file`
- `FillChar`
- `Graph`
- `ParamCount`
- `ParamStr`
- `port`
- `read`
- `readln`
- `reset`
- `rewrite`
- `SizeOf`

## Interop and embedding

Turbo Pascal may embed in Queen Code, Grok16 belt builds, or NEXUS panel scripts.
G16 unified driver (`g16`) compiles C/C++ neighbors; python runner hosts dynamic facets.
Use `g16-compile-combinatronics.py` when program facet gates must pass at compile time.

## Secure compile & run chamber

Every Turbo Pascal compile and run path is sealed — **no bare host exec**. User code passes
`g16-code-security.py` first, then executes inside `g16-secure-chamber.py` with scrubbed
env (`HOME`, `TMPDIR`, `PATH` limited) so AmmoOS, Hostess 7, and Grok16/bin stay protected.

- **Check:** `g16-secure-chamber.py compile` (stdin JSON: content, lang)
- **Run:** `g16-secure-chamber.py run <path> --lang turbo_pascal`
- **Posture:** `/api/g16/secure-chamber` · `nexus-g16-bridge.py json` → `secure_chamber`
- **Queen launch:** `runner_policy.turbo_pascal` = `chamber` in `.launch` manifests
- **Forbidden:** Hostess7, AmmoCode, Grok16/bin, /usr/bin — cannot execute in place

## Performance notes

belt_2_0 native_bsp is the default for hot paths; belt_1_0 python runner applies
when combinatorics bridge degrades the gate. Always-optimal panel pins the best belt
from bench receipts — not guessed from language family alone.

## Research references

Training manuals (school-style textbooks) complement this explaining manual.
See `training_turbo_pascal` on the Dewey shelf when published.
Field Research book and g16-power-sort plates inform algorithm choices in tooling.

## G16 compile path

- **Boil:** `field-program-combinatronic.py boil turbo_pascal`
- **Universal facet:** `field-g16-universal-combinatronic.json`
- **Grok16 compile:** `g16-compile-combinatronics.py` with program facet profile
- **Belt runners:** native_bsp (belt_2_0) and python (belt_1_0) per canonical op
- **Secure chamber:** `lib/g16-secure-chamber.py` — mandatory for all 57 Grok16 languages
- **Filetype actions:** `run` / `compile` → `secure_chamber` in field-programming-filetypes.json

## Code patterns

Representative Turbo Pascal patterns map to canonical ops as follows:

- **Declaration + assign** → declare, assign
- **Conditional** → branch
- **Iteration** → loop, break, continue
- **Procedure call** → call, return
- **Module boundary** → import, export, module
- **I/O** → io
- **Error handling** → throw, catch

## Pitfalls

- Case sensitivity varies — Turbo Pascal keywords may not match heuristic boil.
- Extended packs inherit parent commands; check `extends` in the seed.
- Unknown tokens fall through to heuristic_keywords before defaulting to exec.
- CDN and macro expansion are advisory until combinatronic rebalance runs.
- **Never run Turbo Pascal on the bare host** — shell escapes, `eval`, `system`, and JVM/Node
  subprocess calls are blocked transparently; use the sealed chamber lane.
- Missing host toolchains (javac, node, cobc, fpc) return clear errors inside the chamber.

## Where in NEXUS-Shield

- Seed: `data/field-program-combinatronic-seed.json`
- Battery: `field-program-combinatronic.json` (STATE)
- Manual: `library/dewey/000-computer-science/explaining_turbo_pascal/`
- Reader API: `/api/lang-manuals` · `/api/lang-manuals/turbo_pascal`
- H7c figures: cover, syntax, op_map, memory, compile (field plate + meld)

- **Extends pack:** `pascal`

