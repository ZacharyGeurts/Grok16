# Explaining Clojure

![Cover — Explaining Clojure](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `clojure` only.

- **Language id:** `clojure`
- **Delta commands:** 27 (of 27 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:47:26Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** clojure
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `async` — Async / await / concurrent

- `future`
- `promise`

### `branch` — Branch / if / switch

- `cond`
- `if`
- `when`

### `catch` — Catch / rescue / except

- `catch`
- `try`

### `declare` — Declare / define / let

- `def`
- `defn`
- `let`

### `import` — Import / use / require

- `require`
- `use`

### `io` — I/O / print / read / write file

- `println`
- `prn`
- `slurp`
- `spit`

### `lambda` — Lambda / closure / fn

- `fn`

### `loop` — Loop / iterate / repeat

- `doseq`
- `dotimes`
- `loop`
- `recur`

### `match` — Pattern match / case

- `case`

### `meta` — Macro / reflection / eval

- `defmacro`

### `module` — Module / package / namespace

- `ns`

### `sync` — Sync / lock / mutex / atomic

- `atom`
- `ref`

### `throw` — Throw / raise / panic

- `throw`

## Clojure delta command reference

### `future`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil clojure "future"`

### `promise`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil clojure "promise"`

### `cond`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil clojure "cond"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil clojure "if"`

### `when`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil clojure "when"`

### `catch`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil clojure "catch"`

### `try`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil clojure "try"`

### `def`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil clojure "def"`

### `defn`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil clojure "defn"`

### `let`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil clojure "let"`

### `require`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil clojure "require"`

### `use`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil clojure "use"`

### `println`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil clojure "println"`

### `prn`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil clojure "prn"`

### `slurp`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil clojure "slurp"`

### `spit`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil clojure "spit"`

### `fn`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Verify:** `field-program-combinatronic.py boil clojure "fn"`

### `doseq`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil clojure "doseq"`

### `dotimes`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil clojure "dotimes"`

### `loop`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil clojure "loop"`

### `recur`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil clojure "recur"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil clojure "case"`

### `defmacro`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil clojure "defmacro"`

### `ns`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil clojure "ns"`

### `atom`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil clojure "atom"`

### `ref`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil clojure "ref"`

### `throw`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil clojure "throw"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — clojure

- **Run:** `g16-secure-chamber.py run <file> --lang clojure`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil clojure`

