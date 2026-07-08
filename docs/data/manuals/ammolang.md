# Explaining Ammolang

![Cover — Explaining Ammolang](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `ammolang` only.

- **Language id:** `ammolang`
- **Delta commands:** 38 (of 58 total after inherit)
- **Extends:** `field`
- **Family:** `field`
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:46:38Z

## At a glance

Inherits from: field → `ammolang`

- **Driver:** g16-aml
- **Runtime:** ammolang
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `assign` — Assign / bind / set

- `canonical_bonus`

### `async` — Async / await / concurrent

- `par`

### `call` — Call / invoke / apply

- `combine`
- `S`

### `compare` — Compare / eq / ord

- `coolness`
- `facet_spread`
- `score`

### `declare` — Declare / define / let

- `adjacency`
- `bind`
- `K`
- `pack`
- `width`

### `exec` — Execute / eval / run

- `collapse`
- `fill`
- `rebalance`
- `scan`
- `seq`
- `sequence`

### `import` — Import / use / require

- `connect`
- `source`
- `universal`

### `io` — I/O / print / read / write file

- `emit`
- `outward`

### `load` — Load / read memory

- `I`
- `observe`

### `loop` — Loop / iterate / repeat

- `gapless`
- `traversal`

### `math` — Math / arithmetic

- `manhattan`
- `path_pct`

### `meta` — Macro / reflection / eval

- `boil`
- `gap`
- `grow`
- `surface`

### `module` — Module / package / namespace

- `combinamatrix`
- `combinator`

### `sync` — Sync / lock / mutex / atomic

- `ironclad`
- `spider`
- `wire`

## Ammolang delta command reference

### `canonical_bonus`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil ammolang "canonical_bonus"`

### `par`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil ammolang "par"`

### `combine`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil ammolang "combine"`

### `S`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil ammolang "S"`

### `coolness`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil ammolang "coolness"`

### `facet_spread`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil ammolang "facet_spread"`

### `score`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil ammolang "score"`

### `adjacency`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil ammolang "adjacency"`

### `bind`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil ammolang "bind"`

### `K`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil ammolang "K"`

### `pack`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil ammolang "pack"`

### `width`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil ammolang "width"`

### `collapse`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil ammolang "collapse"`

### `fill`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil ammolang "fill"`

### `rebalance`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil ammolang "rebalance"`

### `scan`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil ammolang "scan"`

### `seq`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil ammolang "seq"`

### `sequence`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil ammolang "sequence"`

### `connect`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil ammolang "connect"`

### `source`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil ammolang "source"`

### `universal`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil ammolang "universal"`

### `emit`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil ammolang "emit"`

### `outward`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil ammolang "outward"`

### `I`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil ammolang "I"`

### `observe`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil ammolang "observe"`

### `gapless`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil ammolang "gapless"`

### `traversal`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil ammolang "traversal"`

### `manhattan`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil ammolang "manhattan"`

### `path_pct`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil ammolang "path_pct"`

### `boil`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil ammolang "boil"`

### `gap`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil ammolang "gap"`

### `grow`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil ammolang "grow"`

### `surface`
- **Boils to:** `meta` — Macro / reflection / eval
- **Verify:** `field-program-combinatronic.py boil ammolang "surface"`

### `combinamatrix`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil ammolang "combinamatrix"`

### `combinator`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil ammolang "combinator"`

### `ironclad`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil ammolang "ironclad"`

### `spider`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil ammolang "spider"`

### `wire`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil ammolang "wire"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — ammolang

- **Run:** `g16-secure-chamber.py run <file> --lang ammolang`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil ammolang`

- **Parent manual:** `explaining_field`

