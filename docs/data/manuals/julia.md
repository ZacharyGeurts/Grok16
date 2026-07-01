# Explaining Julia

![Cover — Explaining Julia](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `julia` only.

- **Language id:** `julia`
- **Delta commands:** 28 (of 28 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-29T12:26:05Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** julia
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `async` — Async / await / concurrent

- `@async`
- `@spawn`

### `branch` — Branch / if / switch

- `else`
- `elseif`
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

- `function`

### `exec` — Execute / eval / run

- `@eval`

### `export` — Export / pub / module out

- `export`

### `import` — Import / use / require

- `import`
- `using`

### `io` — I/O / print / read / write file

- `print`
- `println`
- `read`
- `write`

### `loop` — Loop / iterate / repeat

- `for`
- `while`

### `meta` — Macro / reflection / eval

- `macro`

### `module` — Module / package / namespace

- `module`

### `return` — Return / exit function

- `return`

### `struct` — Struct / record / object

- `mutable`
- `struct`

### `sync` — Sync / lock / mutex / atomic

- `lock`

### `throw` — Throw / raise / panic

- `throw`

## Julia delta command reference

### `@async`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil julia "@async"`

### `@spawn`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil julia "@spawn"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil julia "else"`

### `elseif`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil julia "elseif"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil julia "if"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil julia "break"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil julia "catch"`

### `finally`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil julia "finally"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil julia "try"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil julia "continue"`

### `function`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil julia "function"`

### `@eval`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil julia "@eval"`

### `export`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil julia "export"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil julia "import"`

### `using`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil julia "using"`

### `print`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil julia "print"`

### `println`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil julia "println"`

### `read`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil julia "read"`

### `write`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil julia "write"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil julia "for"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil julia "while"`

### `macro`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil julia "macro"`

### `module`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil julia "module"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil julia "return"`

### `mutable`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil julia "mutable"`

### `struct`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil julia "struct"`

### `lock`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil julia "lock"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil julia "throw"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — julia

- **Run:** `g16-secure-chamber.py run <file> --lang julia`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil julia`

