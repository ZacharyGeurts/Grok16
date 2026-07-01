# Explaining Elixir

![Cover — Explaining Elixir](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `elixir` only.

- **Language id:** `elixir`
- **Delta commands:** 27 (of 27 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:44:23Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** elixir
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `async` — Async / await / concurrent

- `receive`
- `send`
- `spawn`
- `Task`

### `branch` — Branch / if / switch

- `cond`
- `if`
- `unless`

### `call` — Call / invoke / apply

- `|>`

### `catch` — Catch / rescue / except

- `rescue`
- `try`

### `declare` — Declare / define / let

- `def`

### `import` — Import / use / require

- `alias`
- `import`
- `require`
- `use`

### `io` — I/O / print / read / write file

- `IO.puts`
- `IO.read`

### `lambda` — Lambda / closure / fn

- `&`
- `fn`

### `loop` — Loop / iterate / repeat

- `Enum.map`
- `for`
- `while`

### `match` — Pattern match / case

- `case`

### `meta` — Macro / reflection / eval

- `defmacro`

### `module` — Module / package / namespace

- `defmodule`

### `struct` — Struct / record / object

- `defstruct`

### `throw` — Throw / raise / panic

- `raise`

## Elixir delta command reference

### `receive`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil elixir "receive"`

### `send`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil elixir "send"`

### `spawn`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil elixir "spawn"`

### `Task`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil elixir "Task"`

### `cond`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil elixir "cond"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil elixir "if"`

### `unless`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil elixir "unless"`

### `|>`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil elixir "|>"`

### `rescue`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil elixir "rescue"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil elixir "try"`

### `def`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil elixir "def"`

### `alias`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil elixir "alias"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil elixir "import"`

### `require`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil elixir "require"`

### `use`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil elixir "use"`

### `IO.puts`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil elixir "IO.puts"`

### `IO.read`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil elixir "IO.read"`

### `&`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Verify:** `field-program-combinatronic.py boil elixir "&"`

### `fn`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Verify:** `field-program-combinatronic.py boil elixir "fn"`

### `Enum.map`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil elixir "Enum.map"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil elixir "for"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil elixir "while"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil elixir "case"`

### `defmacro`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil elixir "defmacro"`

### `defmodule`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil elixir "defmodule"`

### `defstruct`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil elixir "defstruct"`

### `raise`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil elixir "raise"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — elixir

- **Run:** `g16-secure-chamber.py run <file> --lang elixir`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil elixir`

