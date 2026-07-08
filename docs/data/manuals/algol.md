# Explaining Algol

![Cover — Explaining Algol](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `algol` only.

- **Language id:** `algol`
- **Delta commands:** 19 (of 19 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:46:28Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** algol
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `branch` — Branch / if / switch

- `else`
- `go to`
- `if`
- `then`

### `declare` — Declare / define / let

- `boolean`
- `comment`
- `integer`
- `own`
- `procedure`
- `real`
- `value`

### `exec` — Execute / eval / run

- `begin`

### `loop` — Loop / iterate / repeat

- `do`
- `for`
- `step`
- `until`
- `while`

### `return` — Return / exit function

- `end`

### `struct` — Struct / record / object

- `array`

## Algol delta command reference

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil algol "else"`

### `go to`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil algol "go to"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil algol "if"`

### `then`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil algol "then"`

### `boolean`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil algol "boolean"`

### `comment`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil algol "comment"`

### `integer`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil algol "integer"`

### `own`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil algol "own"`

### `procedure`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil algol "procedure"`

### `real`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil algol "real"`

### `value`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil algol "value"`

### `begin`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil algol "begin"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil algol "do"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil algol "for"`

### `step`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil algol "step"`

### `until`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil algol "until"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil algol "while"`

### `end`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil algol "end"`

### `array`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil algol "array"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — algol

- **Run:** `g16-secure-chamber.py run <file> --lang algol`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil algol`

