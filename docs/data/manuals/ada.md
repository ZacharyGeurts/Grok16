# Explaining Ada

![Cover — Explaining Ada](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `ada` only.

- **Language id:** `ada`
- **Delta commands:** 29 (of 29 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:46:19Z

## At a glance

- **Driver:** g16-gnat
- **Runtime:** ada
- **Belt:** memory_safe

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `new`

### `async` — Async / await / concurrent

- `entry`
- `task`

### `branch` — Branch / if / switch

- `else`
- `elsif`
- `if`

### `break` — Break / leave loop

- `exit`

### `catch` — Catch / rescue / except

- `begin`
- `exception`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `function`
- `procedure`

### `free` — Free / delete / drop

- `free`

### `import` — Import / use / require

- `use`
- `with`

### `io` — I/O / print / read / write file

- `Get`
- `Put`

### `loop` — Loop / iterate / repeat

- `for`
- `loop`
- `while`

### `match` — Pattern match / case

- `case`
- `when`

### `module` — Module / package / namespace

- `package`

### `return` — Return / exit function

- `return`

### `struct` — Struct / record / object

- `array`
- `record`

### `sync` — Sync / lock / mutex / atomic

- `protected`

### `throw` — Throw / raise / panic

- `raise`

### `type` — Type / typedef / interface

- `type`

## Ada delta command reference

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil ada "new"`

### `entry`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil ada "entry"`

### `task`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil ada "task"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil ada "else"`

### `elsif`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil ada "elsif"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil ada "if"`

### `exit`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil ada "exit"`

### `begin`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil ada "begin"`

### `exception`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil ada "exception"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil ada "continue"`

### `function`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil ada "function"`

### `procedure`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil ada "procedure"`

### `free`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil ada "free"`

### `use`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil ada "use"`

### `with`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil ada "with"`

### `Get`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil ada "Get"`

### `Put`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil ada "Put"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil ada "for"`

### `loop`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil ada "loop"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil ada "while"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil ada "case"`

### `when`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil ada "when"`

### `package`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil ada "package"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil ada "return"`

### `array`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil ada "array"`

### `record`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil ada "record"`

### `protected`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil ada "protected"`

### `raise`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil ada "raise"`

### `type`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil ada "type"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — ada

- **Run:** `g16-secure-chamber.py run <file> --lang ada`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil ada`

