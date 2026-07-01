# Explaining Delphi

![Cover — Explaining Delphi](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `delphi` only.

- **Language id:** `delphi`
- **Delta commands:** 23 (of 71 total after inherit)
- **Extends:** `pascal`
- **Family:** `pascal`
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:43:43Z

## At a glance

Inherits from: pascal → `delphi`

- **Driver:** g16-fpc
- **Runtime:** pascal
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `asm` — Inline asm / intrinsics

- `asm`

### `call` — Call / invoke / apply

- `inherited`

### `catch` — Catch / rescue / except

- `except`
- `finally`
- `on`
- `try`

### `compare` — Compare / eq / ord

- `assigned`

### `declare` — Declare / define / let

- `cdecl`
- `constructor`
- `private`
- `property`
- `protected`
- `register`
- `stdcall`

### `export` — Export / pub / module out

- `public`
- `published`

### `free` — Free / delete / drop

- `destructor`
- `freeandnil`

### `string` — String / format / concat

- ` PChar`
- `string`

### `throw` — Throw / raise / panic

- `raise`

### `type` — Type / typedef / interface

- `class`
- `object`

## Delphi delta command reference

### `asm`
- **Boils to:** `asm` — Inline asm / intrinsics
- **Verify:** `field-program-combinatronic.py boil delphi "asm"`

### `inherited`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil delphi "inherited"`

### `except`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil delphi "except"`

### `finally`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil delphi "finally"`

### `on`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil delphi "on"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil delphi "try"`

### `assigned`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil delphi "assigned"`

### `cdecl`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil delphi "cdecl"`

### `constructor`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil delphi "constructor"`

### `private`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil delphi "private"`

### `property`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil delphi "property"`

### `protected`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil delphi "protected"`

### `register`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil delphi "register"`

### `stdcall`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil delphi "stdcall"`

### `public`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil delphi "public"`

### `published`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil delphi "published"`

### `destructor`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil delphi "destructor"`

### `freeandnil`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil delphi "freeandnil"`

### ` PChar`
- **Boils to:** `string` — String / format / concat
- **Verify:** `field-program-combinatronic.py boil delphi " PChar"`

### `string`
- **Boils to:** `string` — String / format / concat
- **Verify:** `field-program-combinatronic.py boil delphi "string"`

### `raise`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil delphi "raise"`

### `class`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil delphi "class"`

### `object`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil delphi "object"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — delphi

- **Run:** `g16-secure-chamber.py run <file> --lang delphi`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil delphi`

- **Parent manual:** `explaining_pascal`

