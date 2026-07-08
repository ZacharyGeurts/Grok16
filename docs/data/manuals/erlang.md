# Explaining Erlang

![Cover — Explaining Erlang](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `erlang` only.

- **Language id:** `erlang`
- **Delta commands:** 21 (of 21 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:44:43Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** erlang
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `async` — Async / await / concurrent

- `receive`
- `send`
- `spawn`

### `branch` — Branch / if / switch

- `if`

### `catch` — Catch / rescue / except

- `catch`
- `try`

### `export` — Export / pub / module out

- `-export`

### `import` — Import / use / require

- `-import`

### `io` — I/O / print / read / write file

- `file:read`
- `file:write`
- `io:format`

### `lambda` — Lambda / closure / fn

- `fun`

### `match` — Pattern match / case

- `case`
- `of`

### `module` — Module / package / namespace

- `-module`

### `struct` — Struct / record / object

- `list`
- `record`
- `tuple`

### `sync` — Sync / lock / mutex / atomic

- `link`
- `monitor`

### `throw` — Throw / raise / panic

- `throw`

## Erlang delta command reference

### `receive`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil erlang "receive"`

### `send`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil erlang "send"`

### `spawn`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil erlang "spawn"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil erlang "if"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil erlang "catch"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil erlang "try"`

### `-export`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil erlang "-export"`

### `-import`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil erlang "-import"`

### `file:read`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil erlang "file:read"`

### `file:write`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil erlang "file:write"`

### `io:format`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil erlang "io:format"`

### `fun`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Verify:** `field-program-combinatronic.py boil erlang "fun"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil erlang "case"`

### `of`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil erlang "of"`

### `-module`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil erlang "-module"`

### `list`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil erlang "list"`

### `record`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil erlang "record"`

### `tuple`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil erlang "tuple"`

### `link`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil erlang "link"`

### `monitor`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil erlang "monitor"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil erlang "throw"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — erlang

- **Run:** `g16-secure-chamber.py run <file> --lang erlang`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil erlang`

