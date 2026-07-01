# Explaining Apl

![Cover — Explaining Apl](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `apl` only.

- **Language id:** `apl`
- **Delta commands:** 29 (of 29 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:46:48Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** apl
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `assign` — Assign / bind / set

- `←`

### `branch` — Branch / if / switch

- `→`

### `call` — Call / invoke / apply

- `⍣`
- `⍨`

### `declare` — Declare / define / let

- `:`
- `⍵`
- `⍺`
- `⎕FX`

### `index` — Index / subscript / slice

- `⊂`
- `⌷`

### `io` — I/O / print / read / write file

- `⌶`
- `⍞`
- `⎕`

### `lambda` — Lambda / closure / fn

- `∘`

### `logic` — Logic / and / or / not

- `~`
- `∧`
- `∨`

### `math` — Math / arithmetic

- `+`
- `-`
- `×`
- `÷`
- `⌹`

### `reduce` — reduce

- `/`
- `⌿`

### `scan` — scan

- `\`
- `⍀`

### `struct` — Struct / record / object

- `,`
- `↑`
- `⍴`

## Apl delta command reference

### `←`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil apl "←"`

### `→`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil apl "→"`

### `⍣`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil apl "⍣"`

### `⍨`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil apl "⍨"`

### `:`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil apl ":"`

### `⍵`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil apl "⍵"`

### `⍺`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil apl "⍺"`

### `⎕FX`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil apl "⎕FX"`

### `⊂`
- **Boils to:** `index` — Index / subscript / slice
- **Verify:** `field-program-combinatronic.py boil apl "⊂"`

### `⌷`
- **Boils to:** `index` — Index / subscript / slice
- **Verify:** `field-program-combinatronic.py boil apl "⌷"`

### `⌶`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil apl "⌶"`

### `⍞`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil apl "⍞"`

### `⎕`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil apl "⎕"`

### `∘`
- **Boils to:** `lambda` — Lambda / closure / fn
- **Verify:** `field-program-combinatronic.py boil apl "∘"`

### `~`
- **Boils to:** `logic` — Logic / and / or / not
- **Verify:** `field-program-combinatronic.py boil apl "~"`

### `∧`
- **Boils to:** `logic` — Logic / and / or / not
- **Verify:** `field-program-combinatronic.py boil apl "∧"`

### `∨`
- **Boils to:** `logic` — Logic / and / or / not
- **Verify:** `field-program-combinatronic.py boil apl "∨"`

### `+`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil apl "+"`

### `-`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil apl "-"`

### `×`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil apl "×"`

### `÷`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil apl "÷"`

### `⌹`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil apl "⌹"`

### `/`
- **Boils to:** `reduce` — reduce
- **Verify:** `field-program-combinatronic.py boil apl "/"`

### `⌿`
- **Boils to:** `reduce` — reduce
- **Verify:** `field-program-combinatronic.py boil apl "⌿"`

### `\`
- **Boils to:** `scan` — scan
- **Verify:** `field-program-combinatronic.py boil apl "\"`

### `⍀`
- **Boils to:** `scan` — scan
- **Verify:** `field-program-combinatronic.py boil apl "⍀"`

### `,`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil apl ","`

### `↑`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil apl "↑"`

### `⍴`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil apl "⍴"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — apl

- **Run:** `g16-secure-chamber.py run <file> --lang apl`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil apl`

