# Explaining Java

![Cover — Explaining Java](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `java` only.

- **Language id:** `java`
- **Delta commands:** 38 (of 38 total after inherit)
- **Extends:** — (root pack)
- **Family:** `java`
- **secure_chamber:** True
- **Generated:** 2026-06-29T12:25:30Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** java
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `new`

### `async` — Async / await / concurrent

- `Thread`

### `branch` — Branch / if / switch

- `case`
- `else`
- `if`
- `switch`

### `break` — Break / leave loop

- `break`

### `call` — Call / invoke / apply

- `super`

### `cast` — Cast / convert / coerce

- `cast`

### `catch` — Catch / rescue / except

- `catch`
- `finally`
- `try`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `final`
- `null`
- `private`
- `protected`
- `static`

### `export` — Export / pub / module out

- `public`

### `import` — Import / use / require

- `import`

### `io` — I/O / print / read / write file

- `Scanner`
- `System.out.println`

### `load` — Load / read memory

- `this`

### `loop` — Loop / iterate / repeat

- `do`
- `for`
- `while`

### `module` — Module / package / namespace

- `package`

### `return` — Return / exit function

- `return`

### `struct` — Struct / record / object

- `record`

### `sync` — Sync / lock / mutex / atomic

- `synchronized`
- `volatile`

### `throw` — Throw / raise / panic

- `throw`

### `type` — Type / typedef / interface

- `class`
- `enum`
- `extends`
- `implements`
- `instanceof`
- `interface`

## Java delta command reference

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil java "new"`

### `Thread`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil java "Thread"`

### `case`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil java "case"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil java "else"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil java "if"`

### `switch`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil java "switch"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil java "break"`

### `super`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil java "super"`

### `cast`
- **Boils to:** `cast` — Cast / convert / coerce
- **Verify:** `field-program-combinatronic.py boil java "cast"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil java "catch"`

### `finally`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil java "finally"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil java "try"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil java "continue"`

### `final`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil java "final"`

### `null`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil java "null"`

### `private`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil java "private"`

### `protected`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil java "protected"`

### `static`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil java "static"`

### `public`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil java "public"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil java "import"`

### `Scanner`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil java "Scanner"`

### `System.out.println`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil java "System.out.println"`

### `this`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil java "this"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil java "do"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil java "for"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil java "while"`

### `package`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil java "package"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil java "return"`

### `record`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil java "record"`

### `synchronized`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil java "synchronized"`

### `volatile`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil java "volatile"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil java "throw"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil java "class"`

### `enum`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil java "enum"`

### `extends`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil java "extends"`

### `implements`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil java "implements"`

### `instanceof`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil java "instanceof"`

### `interface`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil java "interface"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — java

- **Run:** `g16-secure-chamber.py run <file> --lang java`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil java`

