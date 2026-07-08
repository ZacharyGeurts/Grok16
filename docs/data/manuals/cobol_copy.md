# Explaining Cobol Copy

![Cover — Explaining Cobol Copy](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `cobol_copy` only.

- **Language id:** `cobol_copy`
- **Delta commands:** 5 (of 31 total after inherit)
- **Extends:** `cobol`
- **Family:** `cobol`
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:47:46Z

## At a glance

Inherits from: cobol → `cobol_copy`

- **Driver:** g16-interp
- **Runtime:** cobol_copy
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `io` — I/O / print / read / write file

- `EJECT`
- `SKIP1`
- `SKIP2`
- `SKIP3`

### `meta` — Macro / reflection / eval

- `REPLACE`

## Cobol Copy delta command reference

### `EJECT`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cobol_copy "EJECT"`

### `SKIP1`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cobol_copy "SKIP1"`

### `SKIP2`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cobol_copy "SKIP2"`

### `SKIP3`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil cobol_copy "SKIP3"`

### `REPLACE`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil cobol_copy "REPLACE"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — cobol_copy

- **Run:** `g16-secure-chamber.py run <file> --lang cobol_copy`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil cobol_copy`

- **Parent manual:** `explaining_cobol`

