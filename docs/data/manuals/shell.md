# Explaining Shell

![Cover — Explaining Shell](h7fig:cover)

Hostess 7 programming language manual — complete reference distilled from the
Shell combinatronic pack and boiled to the g16 program facet (36 canonical ops).

- **Language id:** `shell`
- **Command entries:** 35
- **Canonical ops used:** 16
- **Generated:** 2026-06-29T12:18:16Z
- **Format:** H7c v3 with embedded figures

## At a glance

- **Paradigm:** imperative glue
- **Typing:** untyped
- **Memory:** n/a
- **Year originated:** 1979

Shell scripting: Hostess7.sh, linux.sh release gates — pipelines, env vars, case statements. AMOURANTHRTX orchestration layer.

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Introduction

This manual explains every seeded Shell construct: surface syntax, semantic role,
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
- · **type** — Type / typedef / interface (runner: native_bsp, belt: belt_2_0)
- · **cast** — Cast / convert / coerce (runner: native_bsp, belt: belt_2_0)
- · **load** — Load / read memory (runner: native_bsp, belt: belt_2_0)
- · **store** — Store / write memory (runner: native_bsp, belt: belt_2_0)
- · **alloc** — Allocate / new / malloc (runner: native_bsp, belt: belt_2_0)
- · **free** — Free / delete / drop (runner: native_bsp, belt: belt_2_0)
- ✓ **io** — I/O / print / read / write file (runner: python, belt: belt_1_0)
- ✓ **import** — Import / use / require (runner: python, belt: belt_1_0)
- ✓ **export** — Export / pub / module out (runner: native_bsp, belt: belt_2_0)
- · **module** — Module / package / namespace (runner: python, belt: belt_1_0)
- · **compare** — Compare / eq / ord (runner: native_bsp, belt: belt_1_0)
- ✓ **logic** — Logic / and / or / not (runner: native_bsp, belt: belt_1_0)
- · **math** — Math / arithmetic (runner: native_bsp, belt: belt_1_0)
- · **string** — String / format / concat (runner: python, belt: belt_1_0)
- · **struct** — Struct / record / object (runner: native_bsp, belt: belt_2_0)
- · **index** — Index / subscript / slice (runner: python, belt: belt_1_0)
- ✓ **throw** — Throw / raise / panic (runner: native_bsp, belt: belt_2_0)
- ✓ **catch** — Catch / rescue / except (runner: native_bsp, belt: belt_2_0)
- · **yield** — Yield / generator / coroutine (runner: python, belt: belt_1_0)
- · **lambda** — Lambda / closure / fn (runner: python, belt: belt_1_0)
- ✓ **match** — Pattern match / case (runner: native_bsp, belt: belt_2_0)
- ✓ **async** — Async / await / concurrent (runner: python, belt: belt_1_0)
- · **sync** — Sync / lock / mutex / atomic (runner: native_bsp, belt: belt_2_0)
- · **asm** — Inline asm / intrinsics (runner: native_bsp, belt: belt_2_0)
- · **unsafe** — Unsafe / raw pointer (runner: native_bsp, belt: belt_2_0)
- · **meta** — Macro / reflection / eval (runner: python, belt: belt_1_0)
- · **query** — Query / select / SQL (runner: python, belt: belt_1_0)

## Shell commands by canonical op

### `async` — Async / await / concurrent

- `&`
- `bg`
- `wait`

### `branch` — Branch / if / switch

- `elif`
- `else`
- `esac`
- `if`

### `break` — Break / leave loop

- `break`

### `catch` — Catch / rescue / except

- `trap`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `function`
- `local`

### `exec` — Execute / eval / run

- `$(...)`
- `eval`
- `exec`

### `export` — Export / pub / module out

- `export`

### `import` — Import / use / require

- `.`
- `source`

### `io` — I/O / print / read / write file

- `<`
- `>`
- `>>`
- `cat`
- `echo`
- `printf`
- `read`

### `logic` — Logic / and / or / not

- `&&`
- `||`

### `loop` — Loop / iterate / repeat

- `for`
- `until`
- `while`

### `match` — Pattern match / case

- `case`

### `pipe` — pipe

- `|`

### `return` — Return / exit function

- `exit`
- `return`

### `throw` — Throw / raise / panic

- `set -e`

## Shell full command reference

### `&`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "&"`

### `bg`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "bg"`

### `wait`
- **Boils to:** `async` — Async / await / concurrent
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "wait"`

### `elif`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "elif"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "else"`

### `esac`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "esac"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "if"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "break"`

### `trap`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "trap"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "continue"`

### `function`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "function"`

### `local`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "local"`

### `$(...)`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "$(...)"`

### `eval`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "eval"`

### `exec`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "exec"`

### `export`
- **Boils to:** `export` — Export / pub / module out
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "export"`

### `.`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "."`

### `source`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "source"`

### `<`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "<"`

### `>`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell ">"`

### `>>`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell ">>"`

### `cat`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "cat"`

### `echo`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "echo"`

### `printf`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "printf"`

### `read`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "read"`

### `&&`
- **Boils to:** `logic` — Logic / and / or / not
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "&&"`

### `||`
- **Boils to:** `logic` — Logic / and / or / not
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "||"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "for"`

### `until`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "until"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "while"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "case"`

### `|`
- **Boils to:** `pipe` — pipe
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "|"`

### `exit`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "exit"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "return"`

### `set -e`
- **Boils to:** `throw` — Throw / raise / panic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil shell "set -e"`

## Execution model

Shell programs execute through the Field program combinatronic facet. Surface syntax
maps to 36 canonical ops; each op selects a belt runner (native_bsp on belt_2_0 or
python on belt_1_0). The explaining manual documents semantics — not a tutorial walkthrough.

- **Paradigm:** imperative glue
- **Typing discipline:** untyped
- **Memory:** n/a
- **Commands in seed:** 35
- **Canonical ops exercised:** 16

![Memory and objects](h7fig:memory)

## Lexical structure

Tokens partition into identifiers, literals, operators, and significant whitespace
per Shell reference rules. Hostess7 boil heuristics treat unknown tokens as exec
unless a seed keyword maps them. Extended packs inherit parent commands.

- `$(...)` → `exec`
- `&` → `async`
- `&&` → `logic`
- `.` → `import`
- `<` → `io`
- `>` → `io`
- `>>` → `io`
- `bg` → `async`
- `break` → `break`
- `case` → `match`
- `cat` → `io`
- `continue` → `continue`
- `echo` → `io`
- `elif` → `branch`
- `else` → `branch`
- `esac` → `branch`
- `eval` → `exec`
- `exec` → `exec`
- `exit` → `return`
- `export` → `export`
- `for` → `loop`
- `function` → `declare`
- `if` → `branch`
- `local` → `declare`

## Type and value space

Shell scripting: Hostess7.sh, linux.sh release gates — pipelines, env vars, case statements. AMOURANTHRTX orchestration layer.

## Control flow

branch · loop · break · continue · return — all languages converge on these atoms.
In Shell, control constructs in the seed pack boil as follows:

- **branch:** `if`, `elif`, `else`, `esac`
- **loop:** `for`, `while`, `until`
- **return:** `return`, `exit`
- **throw:** `set -e`

## Modules and boundaries

import · export · module · package — boundary ops isolate compilation units.
NEXUS-Shield indexes each manual under Dewey 000; combinatronic rebalance may extend packs.

![G16 compile path](h7fig:compile)

## Standard library surface

Where the seed lists I/O or runtime commands, they map to the io and call ops.
Verify any keyword with `field-program-combinatronic.py boil shell "<cmd>"`.

- `.`
- `<`
- `>`
- `>>`
- `cat`
- `echo`
- `printf`
- `read`
- `source`

## Interop and embedding

Shell may embed in Queen Code, Grok16 belt builds, or NEXUS panel scripts.
G16 unified driver (`g16`) compiles C/C++ neighbors; python runner hosts dynamic facets.
Use `g16-compile-combinatronics.py` when program facet gates must pass at compile time.

## Secure compile & run chamber

Every Shell compile and run path is sealed — **no bare host exec**. User code passes
`g16-code-security.py` first, then executes inside `g16-secure-chamber.py` with scrubbed
env (`HOME`, `TMPDIR`, `PATH` limited) so AmmoOS, Hostess 7, and Grok16/bin stay protected.

- **Check:** `g16-secure-chamber.py compile` (stdin JSON: content, lang)
- **Run:** `g16-secure-chamber.py run <path> --lang shell`
- **Posture:** `/api/g16/secure-chamber` · `nexus-g16-bridge.py json` → `secure_chamber`
- **Queen launch:** `runner_policy.shell` = `chamber` in `.launch` manifests
- **Forbidden:** Hostess7, AmmoCode, Grok16/bin, /usr/bin — cannot execute in place

## Performance notes

belt_2_0 native_bsp is the default for hot paths; belt_1_0 python runner applies
when combinatorics bridge degrades the gate. Always-optimal panel pins the best belt
from bench receipts — not guessed from language family alone.

## Research references

Training manuals (school-style textbooks) complement this explaining manual.
See `training_shell` on the Dewey shelf when published.
Field Research book and g16-power-sort plates inform algorithm choices in tooling.

## G16 compile path

- **Boil:** `field-program-combinatronic.py boil shell`
- **Universal facet:** `field-g16-universal-combinatronic.json`
- **Grok16 compile:** `g16-compile-combinatronics.py` with program facet profile
- **Belt runners:** native_bsp (belt_2_0) and python (belt_1_0) per canonical op
- **Secure chamber:** `lib/g16-secure-chamber.py` — mandatory for all 57 Grok16 languages
- **Filetype actions:** `run` / `compile` → `secure_chamber` in field-programming-filetypes.json

## Code patterns

Representative Shell patterns map to canonical ops as follows:

- **Declaration + assign** → declare, assign
- **Conditional** → branch
- **Iteration** → loop, break, continue
- **Procedure call** → call, return
- **Module boundary** → import, export, module
- **I/O** → io
- **Error handling** → throw, catch

## Pitfalls

- Case sensitivity varies — Shell keywords may not match heuristic boil.
- Extended packs inherit parent commands; check `extends` in the seed.
- Unknown tokens fall through to heuristic_keywords before defaulting to exec.
- CDN and macro expansion are advisory until combinatronic rebalance runs.
- **Never run Shell on the bare host** — shell escapes, `eval`, `system`, and JVM/Node
  subprocess calls are blocked transparently; use the sealed chamber lane.
- Missing host toolchains (javac, node, cobc, fpc) return clear errors inside the chamber.

## Where in NEXUS-Shield

- Seed: `data/field-program-combinatronic-seed.json`
- Battery: `field-program-combinatronic.json` (STATE)
- Manual: `library/dewey/000-computer-science/explaining_shell/`
- Reader API: `/api/lang-manuals` · `/api/lang-manuals/shell`
- H7c figures: cover, syntax, op_map, memory, compile (field plate + meld)

