# Explaining Lua

![Cover — Explaining Lua](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `lua` only.

- **Language id:** `lua`
- **Delta commands:** 22 (of 22 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-29T12:27:16Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** lua
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `async` — Async / await / concurrent

- `coroutine`

### `branch` — Branch / if / switch

- `else`
- `elseif`
- `if`

### `break` — Break / leave loop

- `break`

### `catch` — Catch / rescue / except

- `pcall`

### `declare` — Declare / define / let

- `function`
- `local`

### `import` — Import / use / require

- `require`

### `io` — I/O / print / read / write file

- `io.read`
- `io.write`
- `print`

### `loop` — Loop / iterate / repeat

- `for`
- `repeat`
- `while`

### `math` — Math / arithmetic

- `math`

### `module` — Module / package / namespace

- `module`

### `return` — Return / exit function

- `return`

### `string` — String / format / concat

- `string`

### `struct` — Struct / record / object

- `table`

### `throw` — Throw / raise / panic

- `error`

### `yield` — Yield / generator / coroutine

- `yield`

## Lua delta command reference

### `coroutine`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil lua "coroutine"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil lua "else"`

### `elseif`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil lua "elseif"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil lua "if"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil lua "break"`

### `pcall`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil lua "pcall"`

### `function`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil lua "function"`

### `local`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil lua "local"`

### `require`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil lua "require"`

### `io.read`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil lua "io.read"`

### `io.write`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil lua "io.write"`

### `print`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil lua "print"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil lua "for"`

### `repeat`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil lua "repeat"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil lua "while"`

### `math`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil lua "math"`

### `module`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil lua "module"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil lua "return"`

### `string`
- **Boils to:** `string` — String / format / concat
- **Verify:** `field-program-combinatronic.py boil lua "string"`

### `table`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil lua "table"`

### `error`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil lua "error"`

### `yield`
- **Boils to:** `yield` — Yield / generator / coroutine
- **Verify:** `field-program-combinatronic.py boil lua "yield"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — lua

- **Run:** `g16-secure-chamber.py run <file> --lang lua`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil lua`

