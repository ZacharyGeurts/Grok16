# Explaining Javascript

![Cover — Explaining Javascript](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `javascript` only.

- **Language id:** `javascript`
- **Delta commands:** 46 (of 46 total after inherit)
- **Extends:** — (root pack)
- **Family:** `javascript`
- **secure_chamber:** True
- **Generated:** 2026-06-29T12:25:47Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** javascript
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `new`

### `async` — Async / await / concurrent

- `async`
- `await`
- `Promise`
- `setTimeout`

### `branch` — Branch / if / switch

- `case`
- `else`
- `if`
- `switch`

### `break` — Break / leave loop

- `break`

### `call` — Call / invoke / apply

- `JSON.parse`
- `JSON.stringify`
- `super`

### `catch` — Catch / rescue / except

- `catch`
- `finally`
- `try`

### `compare` — Compare / eq / ord

- `!==`
- `===`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `const`
- `function`
- `let`
- `var`

### `exec` — Execute / eval / run

- `eval`
- `Function`

### `export` — Export / pub / module out

- `export`
- `module.exports`

### `free` — Free / delete / drop

- `delete`

### `import` — Import / use / require

- `import`
- `require`

### `io` — I/O / print / read / write file

- `console.log`
- `fetch`
- `readFile`
- `writeFile`

### `lambda` — Lambda / closure / fn

- `=>`

### `load` — Load / read memory

- `this`

### `loop` — Loop / iterate / repeat

- `do`
- `for`
- `while`

### `return` — Return / exit function

- `return`

### `struct` — Struct / record / object

- `Array`
- `Object`

### `throw` — Throw / raise / panic

- `throw`

### `type` — Type / typedef / interface

- `class`
- `instanceof`
- `typeof`

## Javascript delta command reference

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil javascript "new"`

### `async`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil javascript "async"`

### `await`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil javascript "await"`

### `Promise`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil javascript "Promise"`

### `setTimeout`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil javascript "setTimeout"`

### `case`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil javascript "case"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil javascript "else"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil javascript "if"`

### `switch`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil javascript "switch"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil javascript "break"`

### `JSON.parse`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil javascript "JSON.parse"`

### `JSON.stringify`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil javascript "JSON.stringify"`

### `super`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil javascript "super"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil javascript "catch"`

### `finally`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil javascript "finally"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil javascript "try"`

### `!==`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil javascript "!=="`

### `===`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil javascript "==="`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil javascript "continue"`

### `const`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil javascript "const"`

### `function`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil javascript "function"`

### `let`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil javascript "let"`

### `var`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil javascript "var"`

### `eval`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil javascript "eval"`

### `Function`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil javascript "Function"`

### `export`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil javascript "export"`

### `module.exports`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil javascript "module.exports"`

### `delete`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil javascript "delete"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil javascript "import"`

### `require`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil javascript "require"`

### `console.log`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil javascript "console.log"`

### `fetch`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil javascript "fetch"`

### `readFile`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil javascript "readFile"`

### `writeFile`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil javascript "writeFile"`

### `=>`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Verify:** `field-program-combinatronic.py boil javascript "=>"`

### `this`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil javascript "this"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil javascript "do"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil javascript "for"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil javascript "while"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil javascript "return"`

### `Array`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil javascript "Array"`

### `Object`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil javascript "Object"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil javascript "throw"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil javascript "class"`

### `instanceof`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil javascript "instanceof"`

### `typeof`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil javascript "typeof"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — javascript

- **Run:** `g16-secure-chamber.py run <file> --lang javascript`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil javascript`

