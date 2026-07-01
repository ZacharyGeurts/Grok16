# Explaining Lisp

![Cover — Explaining Lisp](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `lisp` only.

- **Language id:** `lisp`
- **Delta commands:** 32 (of 32 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-29T12:26:58Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** lisp
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `assign` — Assign / bind / set

- `setq`

### `branch` — Branch / if / switch

- `cond`
- `if`
- `unless`
- `when`

### `call` — Call / invoke / apply

- `apply`
- `funcall`

### `catch` — Catch / rescue / except

- `catch`
- `handler-bind`

### `declare` — Declare / define / let

- `defun`
- `let`

### `exec` — Execute / eval / run

- `eval`

### `import` — Import / use / require

- `load`
- `require`

### `io` — I/O / print / read / write file

- `format`
- `print`
- `read`
- `write`

### `lambda` — Lambda / closure / fn

- `lambda`

### `load` — Load / read memory

- `car`
- `cdr`

### `loop` — Loop / iterate / repeat

- `do`
- `dolist`
- `dotimes`
- `loop`

### `match` — Pattern match / case

- `case`

### `meta` — Macro / reflection / eval

- `defmacro`

### `return` — Return / exit function

- `return-from`

### `struct` — Struct / record / object

- `cons`
- `list`
- `vector`

### `throw` — Throw / raise / panic

- `throw`

## Lisp delta command reference

### `setq`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil lisp "setq"`

### `cond`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil lisp "cond"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil lisp "if"`

### `unless`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil lisp "unless"`

### `when`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil lisp "when"`

### `apply`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil lisp "apply"`

### `funcall`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil lisp "funcall"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil lisp "catch"`

### `handler-bind`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil lisp "handler-bind"`

### `defun`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil lisp "defun"`

### `let`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil lisp "let"`

### `eval`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil lisp "eval"`

### `load`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil lisp "load"`

### `require`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil lisp "require"`

### `format`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil lisp "format"`

### `print`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil lisp "print"`

### `read`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil lisp "read"`

### `write`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil lisp "write"`

### `lambda`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Verify:** `field-program-combinatronic.py boil lisp "lambda"`

### `car`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil lisp "car"`

### `cdr`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil lisp "cdr"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil lisp "do"`

### `dolist`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil lisp "dolist"`

### `dotimes`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil lisp "dotimes"`

### `loop`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil lisp "loop"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil lisp "case"`

### `defmacro`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil lisp "defmacro"`

### `return-from`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil lisp "return-from"`

### `cons`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil lisp "cons"`

### `list`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil lisp "list"`

### `vector`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil lisp "vector"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil lisp "throw"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — lisp

- **Run:** `g16-secure-chamber.py run <file> --lang lisp`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil lisp`

