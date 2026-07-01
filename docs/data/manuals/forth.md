# Explaining Forth

![Cover — Explaining Forth](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `forth` only.

- **Language id:** `forth`
- **Delta commands:** 32 (of 32 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:45:22Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** forth
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `ALLOT`

### `branch` — Branch / if / switch

- `ELSE`
- `IF`
- `THEN`

### `break` — Break / leave loop

- `EXIT`
- `LEAVE`

### `declare` — Declare / define / let

- `:`
- `CONSTANT`
- `CREATE`
- `VALUE`
- `VARIABLE`

### `exec` — Execute / eval / run

- `EVALUATE`
- `EXECUTE`

### `free` — Free / delete / drop

- `FREE`

### `import` — Import / use / require

- `INCLUDE`
- `REQUIRE`

### `io` — I/O / print / read / write file

- `.`
- `ACCEPT`
- `EMIT`
- `KEY`
- `TYPE`

### `load` — Load / read memory

- `@`
- `C@`

### `loop` — Loop / iterate / repeat

- `+LOOP`
- `AGAIN`
- `BEGIN`
- `DO`
- `LOOP`
- `UNTIL`

### `return` — Return / exit function

- `;`

### `store` — Store / write memory

- `!`
- `C!`

## Forth delta command reference

### `ALLOT`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil forth "ALLOT"`

### `ELSE`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil forth "ELSE"`

### `IF`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil forth "IF"`

### `THEN`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil forth "THEN"`

### `EXIT`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil forth "EXIT"`

### `LEAVE`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil forth "LEAVE"`

### `:`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil forth ":"`

### `CONSTANT`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil forth "CONSTANT"`

### `CREATE`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil forth "CREATE"`

### `VALUE`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil forth "VALUE"`

### `VARIABLE`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil forth "VARIABLE"`

### `EVALUATE`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil forth "EVALUATE"`

### `EXECUTE`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil forth "EXECUTE"`

### `FREE`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil forth "FREE"`

### `INCLUDE`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil forth "INCLUDE"`

### `REQUIRE`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil forth "REQUIRE"`

### `.`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil forth "."`

### `ACCEPT`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil forth "ACCEPT"`

### `EMIT`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil forth "EMIT"`

### `KEY`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil forth "KEY"`

### `TYPE`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil forth "TYPE"`

### `@`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil forth "@"`

### `C@`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil forth "C@"`

### `+LOOP`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil forth "+LOOP"`

### `AGAIN`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil forth "AGAIN"`

### `BEGIN`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil forth "BEGIN"`

### `DO`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil forth "DO"`

### `LOOP`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil forth "LOOP"`

### `UNTIL`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil forth "UNTIL"`

### `;`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil forth ";"`

### `!`
- **Boils to:** `store` — Store / write memory
- **Verify:** `field-program-combinatronic.py boil forth "!"`

### `C!`
- **Boils to:** `store` — Store / write memory
- **Verify:** `field-program-combinatronic.py boil forth "C!"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — forth

- **Run:** `g16-secure-chamber.py run <file> --lang forth`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil forth`

