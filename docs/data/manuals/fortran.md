# Explaining Fortran

![Cover — Explaining Fortran](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `fortran` only.

- **Language id:** `fortran`
- **Delta commands:** 30 (of 30 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:45:43Z

## At a glance

- **Driver:** g16-gfortran
- **Runtime:** fortran
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `ALLOCATE`

### `branch` — Branch / if / switch

- `ELSE`
- `ELSEIF`
- `ENDIF`
- `IF`
- `WHERE`

### `break` — Break / leave loop

- `EXIT`

### `call` — Call / invoke / apply

- `CALL`

### `continue` — Continue / next iteration

- `CYCLE`

### `declare` — Declare / define / let

- `CHARACTER`
- `FUNCTION`
- `INTEGER`
- `LOGICAL`
- `REAL`
- `SUBROUTINE`

### `free` — Free / delete / drop

- `DEALLOCATE`

### `import` — Import / use / require

- `USE`

### `io` — I/O / print / read / write file

- `PRINT`
- `READ`
- `WRITE`

### `loop` — Loop / iterate / repeat

- `DO`
- `ENDDO`
- `FORALL`
- `WHILE`

### `match` — Pattern match / case

- `SELECT CASE`

### `module` — Module / package / namespace

- `MODULE`
- `PROGRAM`

### `return` — Return / exit function

- `RETURN`
- `STOP`

### `type` — Type / typedef / interface

- `TYPE`

## Fortran delta command reference

### `ALLOCATE`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil fortran "ALLOCATE"`

### `ELSE`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil fortran "ELSE"`

### `ELSEIF`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil fortran "ELSEIF"`

### `ENDIF`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil fortran "ENDIF"`

### `IF`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil fortran "IF"`

### `WHERE`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil fortran "WHERE"`

### `EXIT`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil fortran "EXIT"`

### `CALL`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil fortran "CALL"`

### `CYCLE`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil fortran "CYCLE"`

### `CHARACTER`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil fortran "CHARACTER"`

### `FUNCTION`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil fortran "FUNCTION"`

### `INTEGER`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil fortran "INTEGER"`

### `LOGICAL`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil fortran "LOGICAL"`

### `REAL`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil fortran "REAL"`

### `SUBROUTINE`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil fortran "SUBROUTINE"`

### `DEALLOCATE`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil fortran "DEALLOCATE"`

### `USE`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil fortran "USE"`

### `PRINT`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil fortran "PRINT"`

### `READ`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil fortran "READ"`

### `WRITE`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil fortran "WRITE"`

### `DO`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil fortran "DO"`

### `ENDDO`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil fortran "ENDDO"`

### `FORALL`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil fortran "FORALL"`

### `WHILE`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil fortran "WHILE"`

### `SELECT CASE`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil fortran "SELECT CASE"`

### `MODULE`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil fortran "MODULE"`

### `PROGRAM`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil fortran "PROGRAM"`

### `RETURN`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil fortran "RETURN"`

### `STOP`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil fortran "STOP"`

### `TYPE`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil fortran "TYPE"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — fortran

- **Run:** `g16-secure-chamber.py run <file> --lang fortran`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil fortran`

