# Explaining Go

![Cover — Explaining Go](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `go` only.

- **Language id:** `go`
- **Delta commands:** 44 (of 44 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-29T12:24:55Z

## At a glance

- **Driver:** g16-go
- **Runtime:** go
- **Belt:** memory_safe

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `make`
- `new`

### `async` — Async / await / concurrent

- `chan`
- `go`
- `select`

### `branch` — Branch / if / switch

- `case`
- `default`
- `else`
- `goto`
- `if`
- `switch`

### `break` — Break / leave loop

- `break`

### `call` — Call / invoke / apply

- `append`
- `cap`
- `len`

### `catch` — Catch / rescue / except

- `defer`
- `recover`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `const`
- `func`
- `var`

### `export` — Export / pub / module out

- `export`

### `free` — Free / delete / drop

- `close`
- `delete`

### `import` — Import / use / require

- `import`

### `io` — I/O / print / read / write file

- `fmt.Printf`
- `fmt.Println`
- `io.Read`
- `os.Open`

### `load` — Load / read memory

- `*`
- `pointer`

### `loop` — Loop / iterate / repeat

- `for`
- `range`

### `module` — Module / package / namespace

- `package`

### `return` — Return / exit function

- `return`

### `store` — Store / write memory

- `&`

### `struct` — Struct / record / object

- `map`
- `slice`
- `struct`

### `sync` — Sync / lock / mutex / atomic

- `sync.Mutex`

### `throw` — Throw / raise / panic

- `panic`

### `type` — Type / typedef / interface

- `error`
- `interface`
- `type`

## Go delta command reference

### `make`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil go "make"`

### `new`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil go "new"`

### `chan`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil go "chan"`

### `go`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil go "go"`

### `select`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil go "select"`

### `case`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil go "case"`

### `default`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil go "default"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil go "else"`

### `goto`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil go "goto"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil go "if"`

### `switch`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil go "switch"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil go "break"`

### `append`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil go "append"`

### `cap`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil go "cap"`

### `len`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil go "len"`

### `defer`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil go "defer"`

### `recover`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil go "recover"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil go "continue"`

### `const`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil go "const"`

### `func`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil go "func"`

### `var`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil go "var"`

### `export`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil go "export"`

### `close`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil go "close"`

### `delete`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil go "delete"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil go "import"`

### `fmt.Printf`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil go "fmt.Printf"`

### `fmt.Println`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil go "fmt.Println"`

### `io.Read`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil go "io.Read"`

### `os.Open`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil go "os.Open"`

### `*`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil go "*"`

### `pointer`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil go "pointer"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil go "for"`

### `range`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil go "range"`

### `package`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil go "package"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil go "return"`

### `&`
- **Boils to:** `store` — Store / write memory
- **Verify:** `field-program-combinatronic.py boil go "&"`

### `map`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil go "map"`

### `slice`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil go "slice"`

### `struct`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil go "struct"`

### `sync.Mutex`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil go "sync.Mutex"`

### `panic`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil go "panic"`

### `error`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil go "error"`

### `interface`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil go "interface"`

### `type`
- **Boils to:** `type` — Type / typedef / interface
- **Verify:** `field-program-combinatronic.py boil go "type"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — go

- **Run:** `g16-secure-chamber.py run <file> --lang go`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil go`

