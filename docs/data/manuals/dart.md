# Explaining Dart

![Cover — Explaining Dart](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `dart` only.

- **Language id:** `dart`
- **Delta commands:** 29 (of 29 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:48:27Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** dart
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `new`

### `async` — Async / await / concurrent

- `async`
- `await`
- `Future`

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

### `export` — Export / pub / module out

- `export`

### `import` — Import / use / require

- `import`

### `io` — I/O / print / read / write file

- `print`
- `read`
- `write`

### `lambda` — Lambda / closure / fn

- `=>`

### `loop` — Loop / iterate / repeat

- `do`
- `for`
- `while`

### `module` — Module / package / namespace

- `library`

### `return` — Return / exit function

- `return`

### `throw` — Throw / raise / panic

- `throw`

### `type` — Type / typedef / interface

- `class`
- `enum`
- `extension`
- `mixin`

## Dart delta command reference

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil dart "new"`

### `async`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil dart "async"`

### `await`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil dart "await"`

### `Future`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil dart "Future"`

### `case`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil dart "case"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil dart "else"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil dart "if"`

### `switch`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil dart "switch"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil dart "break"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil dart "catch"`

### `finally`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil dart "finally"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil dart "try"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil dart "continue"`

### `export`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil dart "export"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil dart "import"`

### `print`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil dart "print"`

### `read`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil dart "read"`

### `write`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil dart "write"`

### `=>`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Verify:** `field-program-combinatronic.py boil dart "=>"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil dart "do"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil dart "for"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil dart "while"`

### `library`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil dart "library"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil dart "return"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil dart "throw"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil dart "class"`

### `enum`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil dart "enum"`

### `extension`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil dart "extension"`

### `mixin`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil dart "mixin"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — dart

- **Run:** `g16-secure-chamber.py run <file> --lang dart`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil dart`

