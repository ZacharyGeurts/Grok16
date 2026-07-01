# Explaining C

![Cover — Explaining C](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `c` only.

- **Language id:** `c`
- **Delta commands:** 46 (of 46 total after inherit)
- **Extends:** — (root pack)
- **Family:** `c`
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:47:17Z

## At a glance

- **Driver:** g16-cc
- **Runtime:** c
- **Belt:** belt_2_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `calloc`
- `malloc`
- `realloc`

### `asm` — Inline asm / intrinsics

- `__asm__`

### `assign` — Assign / bind / set

- `+=`
- `=`

### `branch` — Branch / if / switch

- `case`
- `default`
- `else`
- `goto`
- `if`
- `switch`

### `break` — Break / leave loop

- `break`

### `cast` — Cast / convert / coerce

- `cast`

### `compare` — Compare / eq / ord

- `!=`
- `==`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `char`
- `double`
- `float`
- `int`
- `static`
- `void`

### `export` — Export / pub / module out

- `extern`

### `free` — Free / delete / drop

- `free`

### `import` — Import / use / require

- `#include`

### `io` — I/O / print / read / write file

- `fclose`
- `fopen`
- `fread`
- `fwrite`
- `printf`
- `scanf`

### `logic` — Logic / and / or / not

- `&&`
- `||`

### `loop` — Loop / iterate / repeat

- `do`
- `for`
- `while`

### `math` — Math / arithmetic

- `++`
- `--`

### `return` — Return / exit function

- `return`

### `struct` — Struct / record / object

- `struct`
- `union`

### `sync` — Sync / lock / mutex / atomic

- `volatile`

### `type` — Type / typedef / interface

- `enum`
- `sizeof`
- `typedef`

## C delta command reference

### `calloc`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil c "calloc"`

### `malloc`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil c "malloc"`

### `realloc`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil c "realloc"`

### `__asm__`
- **Boils to:** `asm` — Inline asm / intrinsics
- **Verify:** `field-program-combinatronic.py boil c "__asm__"`

### `+=`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil c "+="`

### `=`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil c "="`

### `case`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil c "case"`

### `default`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil c "default"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil c "else"`

### `goto`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil c "goto"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil c "if"`

### `switch`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil c "switch"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil c "break"`

### `cast`
- **Boils to:** `cast` — Cast / convert / coerce
- **Verify:** `field-program-combinatronic.py boil c "cast"`

### `!=`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil c "!="`

### `==`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil c "=="`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil c "continue"`

### `char`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil c "char"`

### `double`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil c "double"`

### `float`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil c "float"`

### `int`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil c "int"`

### `static`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil c "static"`

### `void`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil c "void"`

### `extern`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil c "extern"`

### `free`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil c "free"`

### `#include`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil c "#include"`

### `fclose`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil c "fclose"`

### `fopen`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil c "fopen"`

### `fread`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil c "fread"`

### `fwrite`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil c "fwrite"`

### `printf`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil c "printf"`

### `scanf`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil c "scanf"`

### `&&`
- **Boils to:** `logic` — Logic / and / or / not
- **Verify:** `field-program-combinatronic.py boil c "&&"`

### `||`
- **Boils to:** `logic` — Logic / and / or / not
- **Verify:** `field-program-combinatronic.py boil c "||"`

### `do`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil c "do"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil c "for"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil c "while"`

### `++`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil c "++"`

### `--`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil c "--"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil c "return"`

### `struct`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil c "struct"`

### `union`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil c "union"`

### `volatile`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil c "volatile"`

### `enum`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil c "enum"`

### `sizeof`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil c "sizeof"`

### `typedef`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil c "typedef"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — c

- **Run:** `g16-secure-chamber.py run <file> --lang c`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil c`

