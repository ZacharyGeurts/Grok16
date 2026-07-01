# Explaining Matlab

![Cover — Explaining Matlab](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `matlab` only.

- **Language id:** `matlab`
- **Delta commands:** 20 (of 20 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-29T12:27:34Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** matlab
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `async` — Async / await / concurrent

- `parfor`
- `spmd`

### `branch` — Branch / if / switch

- `case`
- `else`
- `elseif`
- `if`
- `switch`

### `break` — Break / leave loop

- `break`

### `catch` — Catch / rescue / except

- `catch`
- `try`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `function`

### `io` — I/O / print / read / write file

- `disp`
- `fprintf`
- `input`

### `loop` — Loop / iterate / repeat

- `for`
- `while`

### `return` — Return / exit function

- `return`

### `throw` — Throw / raise / panic

- `error`

### `type` — Type / typedef / interface

- `classdef`

## Matlab delta command reference

### `parfor`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil matlab "parfor"`

### `spmd`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil matlab "spmd"`

### `case`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil matlab "case"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil matlab "else"`

### `elseif`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil matlab "elseif"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil matlab "if"`

### `switch`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil matlab "switch"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil matlab "break"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil matlab "catch"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil matlab "try"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil matlab "continue"`

### `function`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil matlab "function"`

### `disp`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil matlab "disp"`

### `fprintf`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil matlab "fprintf"`

### `input`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil matlab "input"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil matlab "for"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil matlab "while"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil matlab "return"`

### `error`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil matlab "error"`

### `classdef`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil matlab "classdef"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — matlab

- **Run:** `g16-secure-chamber.py run <file> --lang matlab`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil matlab`

