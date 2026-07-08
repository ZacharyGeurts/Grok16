# Explaining Kotlin

![Cover — Explaining Kotlin](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `kotlin` only.

- **Language id:** `kotlin`
- **Delta commands:** 36 (of 36 total after inherit)
- **Extends:** — (root pack)
- **Family:** `java`
- **secure_chamber:** True
- **Generated:** 2026-06-29T12:26:22Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** kotlin
- **Belt:** memory_safe

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `async` — Async / await / concurrent

- `async`
- `await`
- `coroutine`
- `suspend`

### `branch` — Branch / if / switch

- `?:`
- `else`
- `if`

### `break` — Break / leave loop

- `break`

### `cast` — Cast / convert / coerce

- `as`

### `catch` — Catch / rescue / except

- `catch`
- `finally`
- `try`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `fun`
- `lateinit`
- `lazy`
- `null`
- `private`
- `val`
- `var`

### `export` — Export / pub / module out

- `public`

### `import` — Import / use / require

- `import`

### `io` — I/O / print / read / write file

- `println`
- `readLine`

### `loop` — Loop / iterate / repeat

- `for`
- `while`

### `match` — Pattern match / case

- `when`

### `module` — Module / package / namespace

- `package`

### `return` — Return / exit function

- `return`

### `struct` — Struct / record / object

- `data class`
- `object`

### `throw` — Throw / raise / panic

- `throw`

### `type` — Type / typedef / interface

- `class`
- `interface`
- `is`

### `unsafe` — Unsafe / raw pointer

- `!!`

## Kotlin delta command reference

### `async`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil kotlin "async"`

### `await`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil kotlin "await"`

### `coroutine`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil kotlin "coroutine"`

### `suspend`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil kotlin "suspend"`

### `?:`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil kotlin "?:"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil kotlin "else"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil kotlin "if"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil kotlin "break"`

### `as`
- **Boils to:** `cast` — Cast / convert / coerce
- **Verify:** `field-program-combinatronic.py boil kotlin "as"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil kotlin "catch"`

### `finally`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil kotlin "finally"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil kotlin "try"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil kotlin "continue"`

### `fun`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil kotlin "fun"`

### `lateinit`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil kotlin "lateinit"`

### `lazy`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil kotlin "lazy"`

### `null`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil kotlin "null"`

### `private`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil kotlin "private"`

### `val`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil kotlin "val"`

### `var`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil kotlin "var"`

### `public`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil kotlin "public"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil kotlin "import"`

### `println`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil kotlin "println"`

### `readLine`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil kotlin "readLine"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil kotlin "for"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil kotlin "while"`

### `when`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil kotlin "when"`

### `package`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil kotlin "package"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil kotlin "return"`

### `data class`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil kotlin "data class"`

### `object`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil kotlin "object"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil kotlin "throw"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil kotlin "class"`

### `interface`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil kotlin "interface"`

### `is`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil kotlin "is"`

### `!!`
- **Boils to:** `unsafe` — Unsafe / raw pointer
- **Verify:** `field-program-combinatronic.py boil kotlin "!!"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — kotlin

- **Run:** `g16-secure-chamber.py run <file> --lang kotlin`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil kotlin`

