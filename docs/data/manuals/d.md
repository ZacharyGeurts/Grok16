# Explaining D

![Cover — Explaining D](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `d` only.

- **Language id:** `d`
- **Delta commands:** 31 (of 31 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:48:16Z

## At a glance

- **Driver:** g16-gdc
- **Runtime:** d
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `new`

### `branch` — Branch / if / switch

- `case`
- `else`
- `if`
- `switch`

### `break` — Break / leave loop

- `break`

### `catch` — Catch / rescue / except

- `catch`
- `finally`
- `try`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `private`
- `void`

### `export` — Export / pub / module out

- `public`

### `free` — Free / delete / drop

- `delete`

### `import` — Import / use / require

- `import`

### `io` — I/O / print / read / write file

- `writeln`

### `loop` — Loop / iterate / repeat

- `do`
- `for`
- `foreach`
- `while`

### `meta` — Macro / reflection / eval

- `mixin`
- `template`

### `module` — Module / package / namespace

- `module`

### `return` — Return / exit function

- `return`

### `struct` — Struct / record / object

- `struct`

### `sync` — Sync / lock / mutex / atomic

- `shared`
- `synchronized`

### `throw` — Throw / raise / panic

- `throw`

### `type` — Type / typedef / interface

- `class`
- `enum`
- `interface`

## D delta command reference

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil d "new"`

### `case`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil d "case"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil d "else"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil d "if"`

### `switch`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil d "switch"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil d "break"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil d "catch"`

### `finally`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil d "finally"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil d "try"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil d "continue"`

### `private`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil d "private"`

### `void`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil d "void"`

### `public`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil d "public"`

### `delete`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil d "delete"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil d "import"`

### `writeln`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil d "writeln"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil d "do"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil d "for"`

### `foreach`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil d "foreach"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil d "while"`

### `mixin`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil d "mixin"`

### `template`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil d "template"`

### `module`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil d "module"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil d "return"`

### `struct`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil d "struct"`

### `shared`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil d "shared"`

### `synchronized`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil d "synchronized"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil d "throw"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil d "class"`

### `enum`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil d "enum"`

### `interface`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil d "interface"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — d

- **Run:** `g16-secure-chamber.py run <file> --lang d`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil d`

