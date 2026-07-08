# Explaining Visual Basic

![Cover — Explaining Visual Basic](h7fig:cover)

Hostess 7 programming language manual — complete reference distilled from the
Visual Basic combinatronic pack and boiled to the g16 program facet (36 canonical ops).

- **Language id:** `visual_basic`
- **Command entries:** 79
- **Canonical ops used:** 23
- **Generated:** 2026-06-29T12:23:20Z
- **Format:** H7c v3 with embedded figures

## At a glance

Visual Basic is catalogued in the Field program combinatronic seed.
Profile metadata fills in when Hostess7 langs corpus matches this id.

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Introduction

This manual explains every seeded Visual Basic construct: surface syntax, semantic role,
canonical combinatronic op, belt runner, and NEXUS-Shield integration paths.
Use the GUI reader (`/field-lang-manuals`) or text mode (`field-lang-manual-reader.py text`).

## Reading guide

1. **At a glance** — paradigm, typing, memory model.
2. **Canonical atoms** — the 36 ops all languages boil to.
3. **Commands by op** — every keyword grouped by canonical target.
4. **Full command index** — alphabetical reference.
5. **G16 & NEXUS** — compile, belt, API, pitfalls.

## Canonical combinatronic atoms

- ✓ **exec** — Execute / eval / run (runner: native_bsp, belt: belt_2_0)
- ✓ **assign** — Assign / bind / set (runner: python, belt: belt_1_0)
- ✓ **call** — Call / invoke / apply (runner: native_bsp, belt: belt_2_0)
- ✓ **return** — Return / exit function (runner: native_bsp, belt: belt_2_0)
- ✓ **branch** — Branch / if / switch (runner: native_bsp, belt: belt_1_0)
- ✓ **loop** — Loop / iterate / repeat (runner: native_bsp, belt: belt_1_0)
- ✓ **break** — Break / leave loop (runner: native_bsp, belt: belt_1_0)
- ✓ **continue** — Continue / next iteration (runner: native_bsp, belt: belt_1_0)
- ✓ **declare** — Declare / define / let (runner: python, belt: belt_1_0)
- ✓ **type** — Type / typedef / interface (runner: native_bsp, belt: belt_2_0)
- ✓ **cast** — Cast / convert / coerce (runner: native_bsp, belt: belt_2_0)
- ✓ **load** — Load / read memory (runner: native_bsp, belt: belt_2_0)
- ✓ **store** — Store / write memory (runner: native_bsp, belt: belt_2_0)
- · **alloc** — Allocate / new / malloc (runner: native_bsp, belt: belt_2_0)
- ✓ **free** — Free / delete / drop (runner: native_bsp, belt: belt_2_0)
- ✓ **io** — I/O / print / read / write file (runner: python, belt: belt_1_0)
- ✓ **import** — Import / use / require (runner: python, belt: belt_1_0)
- ✓ **export** — Export / pub / module out (runner: native_bsp, belt: belt_2_0)
- · **module** — Module / package / namespace (runner: python, belt: belt_1_0)
- ✓ **compare** — Compare / eq / ord (runner: native_bsp, belt: belt_1_0)
- · **logic** — Logic / and / or / not (runner: native_bsp, belt: belt_1_0)
- ✓ **math** — Math / arithmetic (runner: native_bsp, belt: belt_1_0)
- ✓ **string** — String / format / concat (runner: python, belt: belt_1_0)
- · **struct** — Struct / record / object (runner: native_bsp, belt: belt_2_0)
- · **index** — Index / subscript / slice (runner: python, belt: belt_1_0)
- ✓ **throw** — Throw / raise / panic (runner: native_bsp, belt: belt_2_0)
- ✓ **catch** — Catch / rescue / except (runner: native_bsp, belt: belt_2_0)
- · **yield** — Yield / generator / coroutine (runner: python, belt: belt_1_0)
- · **lambda** — Lambda / closure / fn (runner: python, belt: belt_1_0)
- ✓ **match** — Pattern match / case (runner: native_bsp, belt: belt_2_0)
- · **async** — Async / await / concurrent (runner: python, belt: belt_1_0)
- · **sync** — Sync / lock / mutex / atomic (runner: native_bsp, belt: belt_2_0)
- · **asm** — Inline asm / intrinsics (runner: native_bsp, belt: belt_2_0)
- · **unsafe** — Unsafe / raw pointer (runner: native_bsp, belt: belt_2_0)
- · **meta** — Macro / reflection / eval (runner: python, belt: belt_1_0)
- · **query** — Query / select / SQL (runner: python, belt: belt_1_0)

## Visual Basic commands by canonical op

### `assign` — Assign / bind / set

- `LET`
- `Set`

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
- `RaiseEvent`
- `USR`

### `cast` — Cast / convert / coerce

- `CINT`
- `VAL`

### `catch` — Catch / rescue / except

- `On Error GoTo`
- `Resume`

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
- `Dim`
- `Event`
- `Function`
- `Private`
- `Property`
- `REM`
- `Sub`

### `exec` — Execute / eval / run

- `NEW`
- `RUN`

### `export` — Export / pub / module out

- `Public`

### `free` — Free / delete / drop

- `CLEAR`

### `import` — Import / use / require

- `CHAIN`

### `io` — I/O / print / read / write file

- `CLOSE`
- `Debug.Print`
- `INPUT`
- `INPUT#`
- `InputBox`
- `MsgBox`
- `OPEN`
- `PRINT`
- `PRINT#`
- `READ`
- `RESTORE`

### `load` — Load / read memory

- `ASC`
- `PEEK`
- `With`

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

### `match` — Pattern match / case

- `Select Case`

### `math` — Math / arithmetic

- `ABS`
- `INT`
- `RND`
- `SGN`

### `return` — Return / exit function

- `END`
- `End Function`
- `End Sub`
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

### `throw` — Throw / raise / panic

- `Err.Raise`

### `type` — Type / typedef / interface

- `As`

## Visual Basic full command reference

### `LET`
- **Boils to:** `assign` — Assign / bind / set
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "LET"`

### `Set`
- **Boils to:** `assign` — Assign / bind / set
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Set"`

### `ELSE`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "ELSE"`

### `ELSEIF`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "ELSEIF"`

### `ENDIF`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "ENDIF"`

### `GOTO`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "GOTO"`

### `IF`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "IF"`

### `ON`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "ON"`

### `THEN`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "THEN"`

### `EXIT`
- **Boils to:** `break` — Break / leave loop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "EXIT"`

### `CALL`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "CALL"`

### `GOSUB`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "GOSUB"`

### `LEN`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "LEN"`

### `RaiseEvent`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "RaiseEvent"`

### `USR`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "USR"`

### `CINT`
- **Boils to:** `cast` — Cast / convert / coerce
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "CINT"`

### `VAL`
- **Boils to:** `cast` — Cast / convert / coerce
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "VAL"`

### `On Error GoTo`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "On Error GoTo"`

### `Resume`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Resume"`

### `INSTR`
- **Boils to:** `compare` — Compare / eq / ord
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "INSTR"`

### `CONTINUE`
- **Boils to:** `continue` — Continue / next iteration
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "CONTINUE"`

### `DATA`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "DATA"`

### `DEF`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "DEF"`

### `DEFINT`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "DEFINT"`

### `DEFSTR`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "DEFSTR"`

### `DIM`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "DIM"`

### `Dim`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Dim"`

### `Event`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Event"`

### `Function`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Function"`

### `Private`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Private"`

### `Property`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Property"`

### `REM`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "REM"`

### `Sub`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Sub"`

### `NEW`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "NEW"`

### `RUN`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "RUN"`

### `Public`
- **Boils to:** `export` — Export / pub / module out
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Public"`

### `CLEAR`
- **Boils to:** `free` — Free / delete / drop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "CLEAR"`

### `CHAIN`
- **Boils to:** `import` — Import / use / require
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "CHAIN"`

### `CLOSE`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "CLOSE"`

### `Debug.Print`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Debug.Print"`

### `INPUT`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "INPUT"`

### `INPUT#`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "INPUT#"`

### `InputBox`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "InputBox"`

### `MsgBox`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "MsgBox"`

### `OPEN`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "OPEN"`

### `PRINT`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "PRINT"`

### `PRINT#`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "PRINT#"`

### `READ`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "READ"`

### `RESTORE`
- **Boils to:** `io` — I/O / print / read / write file
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "RESTORE"`

### `ASC`
- **Boils to:** `load` — Load / read memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "ASC"`

### `PEEK`
- **Boils to:** `load` — Load / read memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "PEEK"`

### `With`
- **Boils to:** `load` — Load / read memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "With"`

### `DO`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "DO"`

### `FOR`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "FOR"`

### `LOOP`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "LOOP"`

### `NEXT`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "NEXT"`

### `STEP`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "STEP"`

### `TO`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "TO"`

### `UNTIL`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "UNTIL"`

### `WEND`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "WEND"`

### `WHILE`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "WHILE"`

### `Select Case`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Select Case"`

### `ABS`
- **Boils to:** `math` — Math / arithmetic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "ABS"`

### `INT`
- **Boils to:** `math` — Math / arithmetic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "INT"`

### `RND`
- **Boils to:** `math` — Math / arithmetic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "RND"`

### `SGN`
- **Boils to:** `math` — Math / arithmetic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "SGN"`

### `END`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "END"`

### `End Function`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "End Function"`

### `End Sub`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "End Sub"`

### `RETURN`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "RETURN"`

### `STOP`
- **Boils to:** `return` — Return / exit function
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "STOP"`

### `POKE`
- **Boils to:** `store` — Store / write memory
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "POKE"`

### `CHR$`
- **Boils to:** `string` — String / format / concat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "CHR$"`

### `LEFT$`
- **Boils to:** `string` — String / format / concat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "LEFT$"`

### `MID$`
- **Boils to:** `string` — String / format / concat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "MID$"`

### `RIGHT$`
- **Boils to:** `string` — String / format / concat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "RIGHT$"`

### `STR$`
- **Boils to:** `string` — String / format / concat
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "STR$"`

### `Err.Raise`
- **Boils to:** `throw` — Throw / raise / panic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "Err.Raise"`

### `As`
- **Boils to:** `type` — Type / typedef / interface
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil visual_basic "As"`

## Execution model

Visual Basic programs execute through the Field program combinatronic facet. Surface syntax
maps to 36 canonical ops; each op selects a belt runner (native_bsp on belt_2_0 or
python on belt_1_0). The explaining manual documents semantics — not a tutorial walkthrough.

- **Paradigm:** multi-paradigm
- **Typing discipline:** see language reference
- **Memory:** runtime-managed
- **Commands in seed:** 79
- **Canonical ops exercised:** 23

![Memory and objects](h7fig:memory)

## Lexical structure

Tokens partition into identifiers, literals, operators, and significant whitespace
per Visual Basic reference rules. Hostess7 boil heuristics treat unknown tokens as exec
unless a seed keyword maps them. Extended packs inherit parent commands.

- `ABS` → `math`
- `As` → `type`
- `ASC` → `load`
- `CALL` → `call`
- `CHAIN` → `import`
- `CHR$` → `string`
- `CINT` → `cast`
- `CLEAR` → `free`
- `CLOSE` → `io`
- `CONTINUE` → `continue`
- `DATA` → `declare`
- `Debug.Print` → `io`
- `DEF` → `declare`
- `DEFINT` → `declare`
- `DEFSTR` → `declare`
- `DIM` → `declare`
- `Dim` → `declare`
- `DO` → `loop`
- `ELSE` → `branch`
- `ELSEIF` → `branch`
- `END` → `return`
- `End Function` → `return`
- `End Sub` → `return`
- `ENDIF` → `branch`

## Type and value space

The Visual Basic value space follows the language reference: primitives, aggregates,
and callables compose through assign, call, and return canonical ops.

## Control flow

branch · loop · break · continue · return — all languages converge on these atoms.
In Visual Basic, control constructs in the seed pack boil as follows:

- **branch:** `IF`, `THEN`, `ELSE`, `ELSEIF`, `ENDIF`, `GOTO`, `ON`
- **loop:** `FOR`, `TO`, `STEP`, `NEXT`, `WHILE`, `WEND`, `DO`, `LOOP`
- **return:** `RETURN`, `END`, `STOP`, `End Sub`, `End Function`
- **throw:** `Err.Raise`

## Modules and boundaries

import · export · module · package — boundary ops isolate compilation units.
NEXUS-Shield indexes each manual under Dewey 000; combinatronic rebalance may extend packs.

![G16 compile path](h7fig:compile)

## Standard library surface

Where the seed lists I/O or runtime commands, they map to the io and call ops.
Verify any keyword with `field-program-combinatronic.py boil visual_basic "<cmd>"`.

- `CALL`
- `CHAIN`
- `CLOSE`
- `Debug.Print`
- `GOSUB`
- `INPUT`
- `INPUT#`
- `InputBox`
- `LEN`
- `MsgBox`
- `OPEN`
- `PRINT`
- `PRINT#`
- `RaiseEvent`
- `READ`
- `RESTORE`

## Interop and embedding

Visual Basic may embed in Queen Code, Grok16 belt builds, or NEXUS panel scripts.
G16 unified driver (`g16`) compiles C/C++ neighbors; python runner hosts dynamic facets.
Use `g16-compile-combinatronics.py` when program facet gates must pass at compile time.

## Secure compile & run chamber

Every Visual Basic compile and run path is sealed — **no bare host exec**. User code passes
`g16-code-security.py` first, then executes inside `g16-secure-chamber.py` with scrubbed
env (`HOME`, `TMPDIR`, `PATH` limited) so AmmoOS, Hostess 7, and Grok16/bin stay protected.

- **Check:** `g16-secure-chamber.py compile` (stdin JSON: content, lang)
- **Run:** `g16-secure-chamber.py run <path> --lang visual_basic`
- **Posture:** `/api/g16/secure-chamber` · `nexus-g16-bridge.py json` → `secure_chamber`
- **Queen launch:** `runner_policy.visual_basic` = `chamber` in `.launch` manifests
- **Forbidden:** Hostess7, AmmoCode, Grok16/bin, /usr/bin — cannot execute in place

## Performance notes

belt_2_0 native_bsp is the default for hot paths; belt_1_0 python runner applies
when combinatorics bridge degrades the gate. Always-optimal panel pins the best belt
from bench receipts — not guessed from language family alone.

## Research references

Training manuals (school-style textbooks) complement this explaining manual.
See `training_visual_basic` on the Dewey shelf when published.
Field Research book and g16-power-sort plates inform algorithm choices in tooling.

## G16 compile path

- **Boil:** `field-program-combinatronic.py boil visual_basic`
- **Universal facet:** `field-g16-universal-combinatronic.json`
- **Grok16 compile:** `g16-compile-combinatronics.py` with program facet profile
- **Belt runners:** native_bsp (belt_2_0) and python (belt_1_0) per canonical op
- **Secure chamber:** `lib/g16-secure-chamber.py` — mandatory for all 57 Grok16 languages
- **Filetype actions:** `run` / `compile` → `secure_chamber` in field-programming-filetypes.json

## Code patterns

Representative Visual Basic patterns map to canonical ops as follows:

- **Declaration + assign** → declare, assign
- **Conditional** → branch
- **Iteration** → loop, break, continue
- **Procedure call** → call, return
- **Module boundary** → import, export, module
- **I/O** → io
- **Error handling** → throw, catch

## Pitfalls

- Case sensitivity varies — Visual Basic keywords may not match heuristic boil.
- Extended packs inherit parent commands; check `extends` in the seed.
- Unknown tokens fall through to heuristic_keywords before defaulting to exec.
- CDN and macro expansion are advisory until combinatronic rebalance runs.
- **Never run Visual Basic on the bare host** — shell escapes, `eval`, `system`, and JVM/Node
  subprocess calls are blocked transparently; use the sealed chamber lane.
- Missing host toolchains (javac, node, cobc, fpc) return clear errors inside the chamber.

## Where in NEXUS-Shield

- Seed: `data/field-program-combinatronic-seed.json`
- Battery: `field-program-combinatronic.json` (STATE)
- Manual: `library/dewey/000-computer-science/explaining_visual_basic/`
- Reader API: `/api/lang-manuals` · `/api/lang-manuals/visual_basic`
- H7c figures: cover, syntax, op_map, memory, compile (field plate + meld)

- **Extends pack:** `basic`

