# Explaining Modula2

![Cover — Explaining Modula2](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `modula2` only.

- **Language id:** `modula2`
- **Delta commands:** 14 (of 62 total after inherit)
- **Extends:** `pascal`
- **Family:** `pascal`
- **secure_chamber:** True
- **Generated:** 2026-06-29T12:27:51Z

## At a glance

Inherits from: pascal → `modula2`

- **Driver:** g16-fpc
- **Runtime:** pascal
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `break` — Break / leave loop

- `EXIT`

### `cast` — Cast / convert / coerce

- `CHR`
- `ORD`

### `export` — Export / pub / module out

- `DEFINITION`
- `EXPORT`
- `QUALIFIED`

### `import` — Import / use / require

- `FROM`

### `load` — Load / read memory

- `WITH`

### `loop` — Loop / iterate / repeat

- `LOOP`

### `math` — Math / arithmetic

- `DEC`
- `INC`

### `module` — Module / package / namespace

- `IMPLEMENTATION`
- `MODULE`

### `return` — Return / exit function

- `RETURN`

## Modula2 delta command reference

### `EXIT`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil modula2 "EXIT"`

### `CHR`
- **Boils to:** `cast` — Cast / convert / coerce
- **Verify:** `field-program-combinatronic.py boil modula2 "CHR"`

### `ORD`
- **Boils to:** `cast` — Cast / convert / coerce
- **Verify:** `field-program-combinatronic.py boil modula2 "ORD"`

### `DEFINITION`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil modula2 "DEFINITION"`

### `EXPORT`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil modula2 "EXPORT"`

### `QUALIFIED`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil modula2 "QUALIFIED"`

### `FROM`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil modula2 "FROM"`

### `WITH`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil modula2 "WITH"`

### `LOOP`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil modula2 "LOOP"`

### `DEC`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil modula2 "DEC"`

### `INC`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil modula2 "INC"`

### `IMPLEMENTATION`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil modula2 "IMPLEMENTATION"`

### `MODULE`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil modula2 "MODULE"`

### `RETURN`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil modula2 "RETURN"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — modula2

- **Run:** `g16-secure-chamber.py run <file> --lang modula2`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil modula2`

- **Parent manual:** `explaining_pascal`

