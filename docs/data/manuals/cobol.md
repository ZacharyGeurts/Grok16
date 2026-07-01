# Explaining Cobol

![Cover — Explaining Cobol](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `cobol` only.

- **Language id:** `cobol`
- **Delta commands:** 26 (of 26 total after inherit)
- **Extends:** — (root pack)
- **Family:** `cobol`
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:47:36Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** cobol
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `assign` — Assign / bind / set

- `MOVE`

### `branch` — Branch / if / switch

- `ELSE`
- `END-IF`
- `GO TO`
- `IF`

### `call` — Call / invoke / apply

- `CALL`
- `PERFORM`

### `declare` — Declare / define / let

- `DATA DIVISION`

### `free` — Free / delete / drop

- `DELETE`

### `import` — Import / use / require

- `COPY`

### `io` — I/O / print / read / write file

- `ACCEPT`
- `CLOSE`
- `DISPLAY`
- `OPEN`
- `READ`
- `WRITE`

### `match` — Pattern match / case

- `EVALUATE`
- `WHEN`

### `math` — Math / arithmetic

- `ADD`
- `COMPUTE`
- `DIVIDE`
- `MULTIPLY`
- `SUBTRACT`

### `module` — Module / package / namespace

- `PROCEDURE DIVISION`

### `return` — Return / exit function

- `EXIT`
- `STOP RUN`

## Cobol delta command reference

### `MOVE`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil cobol "MOVE"`

### `ELSE`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil cobol "ELSE"`

### `END-IF`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil cobol "END-IF"`

### `GO TO`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil cobol "GO TO"`

### `IF`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil cobol "IF"`

### `CALL`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil cobol "CALL"`

### `PERFORM`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil cobol "PERFORM"`

### `DATA DIVISION`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil cobol "DATA DIVISION"`

### `DELETE`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil cobol "DELETE"`

### `COPY`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil cobol "COPY"`

### `ACCEPT`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cobol "ACCEPT"`

### `CLOSE`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cobol "CLOSE"`

### `DISPLAY`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cobol "DISPLAY"`

### `OPEN`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cobol "OPEN"`

### `READ`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cobol "READ"`

### `WRITE`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cobol "WRITE"`

### `EVALUATE`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil cobol "EVALUATE"`

### `WHEN`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil cobol "WHEN"`

### `ADD`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil cobol "ADD"`

### `COMPUTE`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil cobol "COMPUTE"`

### `DIVIDE`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil cobol "DIVIDE"`

### `MULTIPLY`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil cobol "MULTIPLY"`

### `SUBTRACT`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil cobol "SUBTRACT"`

### `PROCEDURE DIVISION`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil cobol "PROCEDURE DIVISION"`

### `EXIT`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil cobol "EXIT"`

### `STOP RUN`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil cobol "STOP RUN"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — cobol

- **Run:** `g16-secure-chamber.py run <file> --lang cobol`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil cobol`

