# Explaining Basic

![Cover — Explaining Basic](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `basic` only.

- **Language id:** `basic`
- **Delta commands:** 59 (of 59 total after inherit)
- **Extends:** — (root pack)
- **Family:** `basic`
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:47:07Z

## At a glance

- **Driver:** g16-qbasic
- **Runtime:** basic
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `assign` — Assign / bind / set

- `LET`

### `branch` — Branch / if / switch

- `ELSE`
- `ELSEIF`
- `ENDIF`
- `GOTO`
- `IF`
- `ON`
- `THEN`

### `break` — Break / leave loop

- `EXIT`

### `call` — Call / invoke / apply

- `CALL`
- `GOSUB`
- `LEN`
- `USR`

### `cast` — Cast / convert / coerce

- `CINT`
- `VAL`

### `compare` — Compare / eq / ord

- `INSTR`

### `continue` — Continue / next iteration

- `CONTINUE`

### `declare` — Declare / define / let

- `DATA`
- `DEF`
- `DEFINT`
- `DEFSTR`
- `DIM`
- `REM`

### `exec` — Execute / eval / run

- `NEW`
- `RUN`

### `free` — Free / delete / drop

- `CLEAR`

### `import` — Import / use / require

- `CHAIN`

### `io` — I/O / print / read / write file

- `CLOSE`
- `INPUT`
- `INPUT#`
- `OPEN`
- `PRINT`
- `PRINT#`
- `READ`
- `RESTORE`

### `load` — Load / read memory

- `ASC`
- `PEEK`

### `loop` — Loop / iterate / repeat

- `DO`
- `FOR`
- `LOOP`
- `NEXT`
- `STEP`
- `TO`
- `UNTIL`
- `WEND`
- `WHILE`

### `math` — Math / arithmetic

- `ABS`
- `INT`
- `RND`
- `SGN`

### `return` — Return / exit function

- `END`
- `RETURN`
- `STOP`

### `store` — Store / write memory

- `POKE`

### `string` — String / format / concat

- `CHR$`
- `LEFT$`
- `MID$`
- `RIGHT$`
- `STR$`

## Basic delta command reference

### `LET`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil basic "LET"`

### `ELSE`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil basic "ELSE"`

### `ELSEIF`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil basic "ELSEIF"`

### `ENDIF`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil basic "ENDIF"`

### `GOTO`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil basic "GOTO"`

### `IF`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil basic "IF"`

### `ON`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil basic "ON"`

### `THEN`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil basic "THEN"`

### `EXIT`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil basic "EXIT"`

### `CALL`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil basic "CALL"`

### `GOSUB`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil basic "GOSUB"`

### `LEN`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil basic "LEN"`

### `USR`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil basic "USR"`

### `CINT`
- **Boils to:** `cast` — Cast / convert / coerce
- **Verify:** `field-program-combinatronic.py boil basic "CINT"`

### `VAL`
- **Boils to:** `cast` — Cast / convert / coerce
- **Verify:** `field-program-combinatronic.py boil basic "VAL"`

### `INSTR`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil basic "INSTR"`

### `CONTINUE`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil basic "CONTINUE"`

### `DATA`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil basic "DATA"`

### `DEF`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil basic "DEF"`

### `DEFINT`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil basic "DEFINT"`

### `DEFSTR`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil basic "DEFSTR"`

### `DIM`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil basic "DIM"`

### `REM`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil basic "REM"`

### `NEW`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil basic "NEW"`

### `RUN`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil basic "RUN"`

### `CLEAR`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil basic "CLEAR"`

### `CHAIN`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil basic "CHAIN"`

### `CLOSE`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil basic "CLOSE"`

### `INPUT`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil basic "INPUT"`

### `INPUT#`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil basic "INPUT#"`

### `OPEN`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil basic "OPEN"`

### `PRINT`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil basic "PRINT"`

### `PRINT#`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil basic "PRINT#"`

### `READ`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil basic "READ"`

### `RESTORE`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil basic "RESTORE"`

### `ASC`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil basic "ASC"`

### `PEEK`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil basic "PEEK"`

### `DO`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil basic "DO"`

### `FOR`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil basic "FOR"`

### `LOOP`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil basic "LOOP"`

### `NEXT`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil basic "NEXT"`

### `STEP`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil basic "STEP"`

### `TO`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil basic "TO"`

### `UNTIL`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil basic "UNTIL"`

### `WEND`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil basic "WEND"`

### `WHILE`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil basic "WHILE"`

### `ABS`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil basic "ABS"`

### `INT`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil basic "INT"`

### `RND`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil basic "RND"`

### `SGN`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil basic "SGN"`

### `END`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil basic "END"`

### `RETURN`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil basic "RETURN"`

### `STOP`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil basic "STOP"`

### `POKE`
- **Boils to:** `store` — Store / write memory
- **Verify:** `field-program-combinatronic.py boil basic "POKE"`

### `CHR$`
- **Boils to:** `string` — String / format / concat
- **Verify:** `field-program-combinatronic.py boil basic "CHR$"`

### `LEFT$`
- **Boils to:** `string` — String / format / concat
- **Verify:** `field-program-combinatronic.py boil basic "LEFT$"`

### `MID$`
- **Boils to:** `string` — String / format / concat
- **Verify:** `field-program-combinatronic.py boil basic "MID$"`

### `RIGHT$`
- **Boils to:** `string` — String / format / concat
- **Verify:** `field-program-combinatronic.py boil basic "RIGHT$"`

### `STR$`
- **Boils to:** `string` — String / format / concat
- **Verify:** `field-program-combinatronic.py boil basic "STR$"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — basic

- **Run:** `g16-secure-chamber.py run <file> --lang basic`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil basic`

