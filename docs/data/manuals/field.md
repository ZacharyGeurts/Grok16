# Explaining Field

![Cover — Explaining Field](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `field` only.

- **Language id:** `field`
- **Delta commands:** 20 (of 20 total after inherit)
- **Extends:** — (root pack)
- **Family:** `field`
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:45:02Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** field
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `assign` — Assign / bind / set

- `chain_hash`

### `branch` — Branch / if / switch

- `verdict`

### `call` — Call / invoke / apply

- `runner`

### `catch` — Catch / rescue / except

- `retaliate`

### `compare` — Compare / eq / ord

- `verify`

### `declare` — Declare / define / let

- `die_slots`
- `leaf`
- `truth`

### `exec` — Execute / eval / run

- `combinatorics`
- `condense`
- `meld`
- `native_bsp`
- `rebuild`

### `io` — I/O / print / read / write file

- `publish`

### `loop` — Loop / iterate / repeat

- `walk_tree`

### `module` — Module / package / namespace

- `plate`

### `sync` — Sync / lock / mutex / atomic

- `lock`

### `throw` — Throw / raise / panic

- `reject`

### `type` — Type / typedef / interface

- `belt`
- `facet`

## Field delta command reference

### `chain_hash`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil field "chain_hash"`

### `verdict`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil field "verdict"`

### `runner`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil field "runner"`

### `retaliate`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil field "retaliate"`

### `verify`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil field "verify"`

### `die_slots`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil field "die_slots"`

### `leaf`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil field "leaf"`

### `truth`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil field "truth"`

### `combinatorics`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil field "combinatorics"`

### `condense`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil field "condense"`

### `meld`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil field "meld"`

### `native_bsp`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil field "native_bsp"`

### `rebuild`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil field "rebuild"`

### `publish`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil field "publish"`

### `walk_tree`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil field "walk_tree"`

### `plate`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil field "plate"`

### `lock`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil field "lock"`

### `reject`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil field "reject"`

### `belt`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil field "belt"`

### `facet`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil field "facet"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — field

- **Run:** `g16-secure-chamber.py run <file> --lang field`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil field`

