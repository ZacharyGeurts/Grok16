# Explaining Freebasic

![Cover — Explaining Freebasic](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `freebasic` only.

- **Language id:** `freebasic`
- **Delta commands:** 18 (of 28 total after inherit)
- **Extends:** `quickbasic`
- **Family:** `basic`
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:46:04Z

## At a glance

Inherits from: quickbasic → `freebasic`

- **Driver:** g16-fpc
- **Runtime:** qbasic
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `new`

### `async` — Async / await / concurrent

- `sleep`
- `threadcreate`

### `call` — Call / invoke / apply

- `operator`

### `declare` — Declare / define / let

- `constructor`
- `property`
- `withevents`

### `free` — Free / delete / drop

- `delete`
- `destructor`

### `import` — Import / use / require

- `#include`
- `using`

### `load` — Load / read memory

- `@`
- `pointer`
- `ptr`

### `meta` — Macro / reflection / eval

- `#define`

### `module` — Module / package / namespace

- `namespace`

### `sync` — Sync / lock / mutex / atomic

- `mutexcreate`

### `type` — Type / typedef / interface

- `implements`

## Freebasic delta command reference

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil freebasic "new"`

### `sleep`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil freebasic "sleep"`

### `threadcreate`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil freebasic "threadcreate"`

### `operator`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil freebasic "operator"`

### `constructor`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil freebasic "constructor"`

### `property`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil freebasic "property"`

### `withevents`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil freebasic "withevents"`

### `delete`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil freebasic "delete"`

### `destructor`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil freebasic "destructor"`

### `#include`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil freebasic "#include"`

### `using`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil freebasic "using"`

### `@`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil freebasic "@"`

### `pointer`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil freebasic "pointer"`

### `ptr`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil freebasic "ptr"`

### `#define`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil freebasic "#define"`

### `namespace`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil freebasic "namespace"`

### `mutexcreate`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil freebasic "mutexcreate"`

### `implements`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil freebasic "implements"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — freebasic

- **Run:** `g16-secure-chamber.py run <file> --lang freebasic`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil freebasic`

- **Parent manual:** `explaining_quickbasic`

