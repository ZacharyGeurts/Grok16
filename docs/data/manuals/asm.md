# Explaining Asm

![Cover — Explaining Asm](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `asm` only.

- **Language id:** `asm`
- **Delta commands:** 34 (of 34 total after inherit)
- **Extends:** — (root pack)
- **Family:** `c`
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:46:58Z

## At a glance

- **Driver:** g16-as
- **Runtime:** asm
- **Belt:** field_opt

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `assign` — Assign / bind / set

- `mov`

### `branch` — Branch / if / switch

- `je`
- `jmp`
- `jne`
- `jnz`
- `jz`

### `call` — Call / invoke / apply

- `call`

### `compare` — Compare / eq / ord

- `cmp`
- `test`

### `declare` — Declare / define / let

- `db`
- `dd`
- `dq`
- `dw`

### `exec` — Execute / eval / run

- `nop`

### `export` — Export / pub / module out

- `.global`

### `import` — Import / use / require

- `.extern`

### `io` — I/O / print / read / write file

- `int`
- `syscall`

### `load` — Load / read memory

- `lea`
- `pop`

### `logic` — Logic / and / or / not

- `and`
- `not`
- `or`
- `xor`

### `loop` — Loop / iterate / repeat

- `loop`

### `math` — Math / arithmetic

- `add`
- `dec`
- `div`
- `inc`
- `mul`
- `sub`

### `module` — Module / package / namespace

- `.section`

### `return` — Return / exit function

- `ret`

### `store` — Store / write memory

- `push`

## Asm delta command reference

### `mov`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil asm "mov"`

### `je`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil asm "je"`

### `jmp`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil asm "jmp"`

### `jne`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil asm "jne"`

### `jnz`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil asm "jnz"`

### `jz`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil asm "jz"`

### `call`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil asm "call"`

### `cmp`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil asm "cmp"`

### `test`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil asm "test"`

### `db`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil asm "db"`

### `dd`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil asm "dd"`

### `dq`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil asm "dq"`

### `dw`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil asm "dw"`

### `nop`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil asm "nop"`

### `.global`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil asm ".global"`

### `.extern`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil asm ".extern"`

### `int`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil asm "int"`

### `syscall`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil asm "syscall"`

### `lea`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil asm "lea"`

### `pop`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil asm "pop"`

### `and`
- **Boils to:** `logic` — Logic / and / or / not
- **Verify:** `field-program-combinatronic.py boil asm "and"`

### `not`
- **Boils to:** `logic` — Logic / and / or / not
- **Verify:** `field-program-combinatronic.py boil asm "not"`

### `or`
- **Boils to:** `logic` — Logic / and / or / not
- **Verify:** `field-program-combinatronic.py boil asm "or"`

### `xor`
- **Boils to:** `logic` — Logic / and / or / not
- **Verify:** `field-program-combinatronic.py boil asm "xor"`

### `loop`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil asm "loop"`

### `add`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil asm "add"`

### `dec`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil asm "dec"`

### `div`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil asm "div"`

### `inc`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil asm "inc"`

### `mul`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil asm "mul"`

### `sub`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil asm "sub"`

### `.section`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil asm ".section"`

### `ret`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil asm "ret"`

### `push`
- **Boils to:** `store` — Store / write memory
- **Verify:** `field-program-combinatronic.py boil asm "push"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — asm

- **Run:** `g16-secure-chamber.py run <file> --lang asm`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil asm`

