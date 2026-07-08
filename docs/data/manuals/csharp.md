# Explaining Csharp

![Cover — Explaining Csharp](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `csharp` only.

- **Language id:** `csharp`
- **Delta commands:** 37 (of 37 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:47:56Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** csharp
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `new`

### `async` — Async / await / concurrent

- `async`
- `await`
- `Task`

### `branch` — Branch / if / switch

- `case`
- `else`
- `if`
- `switch`

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

- `private`
- `protected`
- `static`
- `var`

### `export` — Export / pub / module out

- `public`

### `import` — Import / use / require

- `using`

### `io` — I/O / print / read / write file

- `Console.WriteLine`

### `lambda` — Lambda / closure / fn

- `=>`
- `delegate`

### `loop` — Loop / iterate / repeat

- `do`
- `for`
- `foreach`
- `while`

### `module` — Module / package / namespace

- `namespace`

### `return` — Return / exit function

- `return`

### `struct` — Struct / record / object

- `record`
- `struct`

### `sync` — Sync / lock / mutex / atomic

- `lock`

### `throw` — Throw / raise / panic

- `throw`

### `type` — Type / typedef / interface

- `class`
- `enum`
- `interface`
- `is`

## Csharp delta command reference

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil csharp "new"`

### `async`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil csharp "async"`

### `await`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil csharp "await"`

### `Task`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil csharp "Task"`

### `case`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil csharp "case"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil csharp "else"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil csharp "if"`

### `switch`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil csharp "switch"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil csharp "break"`

### `as`
- **Boils to:** `cast` — Cast / convert / coerce
- **Verify:** `field-program-combinatronic.py boil csharp "as"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil csharp "catch"`

### `finally`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil csharp "finally"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil csharp "try"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil csharp "continue"`

### `private`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil csharp "private"`

### `protected`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil csharp "protected"`

### `static`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil csharp "static"`

### `var`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil csharp "var"`

### `public`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil csharp "public"`

### `using`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil csharp "using"`

### `Console.WriteLine`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil csharp "Console.WriteLine"`

### `=>`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Verify:** `field-program-combinatronic.py boil csharp "=>"`

### `delegate`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Verify:** `field-program-combinatronic.py boil csharp "delegate"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil csharp "do"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil csharp "for"`

### `foreach`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil csharp "foreach"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil csharp "while"`

### `namespace`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil csharp "namespace"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil csharp "return"`

### `record`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil csharp "record"`

### `struct`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil csharp "struct"`

### `lock`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil csharp "lock"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil csharp "throw"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil csharp "class"`

### `enum`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil csharp "enum"`

### `interface`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil csharp "interface"`

### `is`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil csharp "is"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — csharp

- **Run:** `g16-secure-chamber.py run <file> --lang csharp`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil csharp`

