# Explaining Haskell

![Cover — Explaining Haskell](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `haskell` only.

- **Language id:** `haskell`
- **Delta commands:** 31 (of 31 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-29T12:25:13Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** haskell
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `async` — Async / await / concurrent

- `par`

### `branch` — Branch / if / switch

- `else`
- `if`
- `then`

### `call` — Call / invoke / apply

- `>>`
- `>>=`
- `filter`
- `fold`
- `map`

### `declare` — Declare / define / let

- `in`
- `let`
- `where`

### `import` — Import / use / require

- `import`

### `io` — I/O / print / read / write file

- `getLine`
- `putStrLn`
- `readFile`
- `writeFile`

### `loop` — Loop / iterate / repeat

- `do`

### `match` — Pattern match / case

- `case`
- `of`

### `module` — Module / package / namespace

- `module`

### `return` — Return / exit function

- `return`

### `sync` — Sync / lock / mutex / atomic

- `seq`

### `throw` — Throw / raise / panic

- `error`
- `throw`

### `type` — Type / typedef / interface

- `class`
- `data`
- `instance`
- `type`

### `unsafe` — Unsafe / raw pointer

- `unsafePerformIO`

### `yield` — Yield / generator / coroutine

- `yield`

## Haskell delta command reference

### `par`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil haskell "par"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil haskell "else"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil haskell "if"`

### `then`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil haskell "then"`

### `>>`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil haskell ">>"`

### `>>=`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil haskell ">>="`

### `filter`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil haskell "filter"`

### `fold`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil haskell "fold"`

### `map`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil haskell "map"`

### `in`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil haskell "in"`

### `let`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil haskell "let"`

### `where`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil haskell "where"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil haskell "import"`

### `getLine`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil haskell "getLine"`

### `putStrLn`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil haskell "putStrLn"`

### `readFile`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil haskell "readFile"`

### `writeFile`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil haskell "writeFile"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil haskell "do"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil haskell "case"`

### `of`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil haskell "of"`

### `module`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil haskell "module"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil haskell "return"`

### `seq`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil haskell "seq"`

### `error`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil haskell "error"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil haskell "throw"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil haskell "class"`

### `data`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil haskell "data"`

### `instance`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil haskell "instance"`

### `type`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil haskell "type"`

### `unsafePerformIO`
- **Boils to:** `unsafe` — Unsafe / raw pointer
- **Verify:** `field-program-combinatronic.py boil haskell "unsafePerformIO"`

### `yield`
- **Boils to:** `yield` — Yield / generator / coroutine
- **Verify:** `field-program-combinatronic.py boil haskell "yield"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — haskell

- **Run:** `g16-secure-chamber.py run <file> --lang haskell`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil haskell`

