# Explaining Cxx

![Cover — Explaining Cxx](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `cxx` only.

- **Language id:** `cxx`
- **Delta commands:** 47 (of 47 total after inherit)
- **Extends:** — (root pack)
- **Family:** `c`
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:48:06Z

## At a glance

- **Driver:** g16-cxx
- **Runtime:** cxx
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `malloc`
- `new`

### `async` — Async / await / concurrent

- `std::async`
- `std::thread`

### `branch` — Branch / if / switch

- `case`
- `else`
- `if`
- `switch`

### `break` — Break / leave loop

- `break`

### `call` — Call / invoke / apply

- `->`
- `operator`

### `cast` — Cast / convert / coerce

- `dynamic_cast`
- `reinterpret_cast`
- `static_cast`

### `catch` — Catch / rescue / except

- `catch`
- `try`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `auto`
- `constexpr`
- `nullptr`
- `private`

### `export` — Export / pub / module out

- `export`
- `public`

### `free` — Free / delete / drop

- `delete`
- `free`

### `import` — Import / use / require

- `#include`

### `index` — Index / subscript / slice

- `[]`

### `io` — I/O / print / read / write file

- `cin`
- `cout`
- `printf`

### `lambda` — Lambda / closure / fn

- `lambda`

### `load` — Load / read memory

- `this`

### `loop` — Loop / iterate / repeat

- `do`
- `for`
- `while`

### `meta` — Macro / reflection / eval

- `template`

### `module` — Module / package / namespace

- `::`
- `namespace`

### `return` — Return / exit function

- `return`

### `struct` — Struct / record / object

- `struct`

### `sync` — Sync / lock / mutex / atomic

- `atomic`
- `mutex`

### `throw` — Throw / raise / panic

- `throw`

### `type` — Type / typedef / interface

- `class`
- `enum`
- `override`
- `virtual`

## Cxx delta command reference

### `malloc`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil cxx "malloc"`

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil cxx "new"`

### `std::async`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil cxx "std::async"`

### `std::thread`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil cxx "std::thread"`

### `case`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil cxx "case"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil cxx "else"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil cxx "if"`

### `switch`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil cxx "switch"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil cxx "break"`

### `->`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil cxx "->"`

### `operator`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil cxx "operator"`

### `dynamic_cast`
- **Boils to:** `cast` — Cast / convert / coerce
- **Verify:** `field-program-combinatronic.py boil cxx "dynamic_cast"`

### `reinterpret_cast`
- **Boils to:** `cast` — Cast / convert / coerce
- **Verify:** `field-program-combinatronic.py boil cxx "reinterpret_cast"`

### `static_cast`
- **Boils to:** `cast` — Cast / convert / coerce
- **Verify:** `field-program-combinatronic.py boil cxx "static_cast"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil cxx "catch"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil cxx "try"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil cxx "continue"`

### `auto`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil cxx "auto"`

### `constexpr`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil cxx "constexpr"`

### `nullptr`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil cxx "nullptr"`

### `private`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil cxx "private"`

### `export`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil cxx "export"`

### `public`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil cxx "public"`

### `delete`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil cxx "delete"`

### `free`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil cxx "free"`

### `#include`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil cxx "#include"`

### `[]`
- **Boils to:** `index` — Index / subscript / slice
- **Verify:** `field-program-combinatronic.py boil cxx "[]"`

### `cin`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cxx "cin"`

### `cout`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cxx "cout"`

### `printf`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cxx "printf"`

### `lambda`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Verify:** `field-program-combinatronic.py boil cxx "lambda"`

### `this`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil cxx "this"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil cxx "do"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil cxx "for"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil cxx "while"`

### `template`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil cxx "template"`

### `::`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil cxx "::"`

### `namespace`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil cxx "namespace"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil cxx "return"`

### `struct`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil cxx "struct"`

### `atomic`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil cxx "atomic"`

### `mutex`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil cxx "mutex"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil cxx "throw"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil cxx "class"`

### `enum`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil cxx "enum"`

### `override`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil cxx "override"`

### `virtual`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil cxx "virtual"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — cxx

- **Run:** `g16-secure-chamber.py run <file> --lang cxx`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil cxx`

