# Explaining SQL

![Cover — Explaining SQL](h7fig:cover)

Hostess 7 programming language manual — complete reference distilled from the
SQL combinatronic pack and boiled to the g16 program facet (36 canonical ops).

- **Language id:** `sql`
- **Command entries:** 27
- **Canonical ops used:** 10
- **Generated:** 2026-06-29T12:20:03Z
- **Format:** H7c v3 with embedded figures

## At a glance

- **Paradigm:** declarative
- **Typing:** static schema
- **Memory:** n/a
- **Year originated:** 1974

SQL: relational algebra — SELECT FROM WHERE JOIN GROUP BY. Declarative query language; implementations: PostgreSQL, SQLite, MySQL.

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Introduction

This manual explains every seeded SQL construct: surface syntax, semantic role,
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
- · **return** — Return / exit function (runner: native_bsp, belt: belt_2_0)
- ✓ **branch** — Branch / if / switch (runner: native_bsp, belt: belt_1_0)
- · **loop** — Loop / iterate / repeat (runner: native_bsp, belt: belt_1_0)
- · **break** — Break / leave loop (runner: native_bsp, belt: belt_1_0)
- · **continue** — Continue / next iteration (runner: native_bsp, belt: belt_1_0)
- ✓ **declare** — Declare / define / let (runner: python, belt: belt_1_0)
- · **type** — Type / typedef / interface (runner: native_bsp, belt: belt_2_0)
- · **cast** — Cast / convert / coerce (runner: native_bsp, belt: belt_2_0)
- · **load** — Load / read memory (runner: native_bsp, belt: belt_2_0)
- · **store** — Store / write memory (runner: native_bsp, belt: belt_2_0)
- · **alloc** — Allocate / new / malloc (runner: native_bsp, belt: belt_2_0)
- ✓ **free** — Free / delete / drop (runner: native_bsp, belt: belt_2_0)
- · **io** — I/O / print / read / write file (runner: python, belt: belt_1_0)
- · **import** — Import / use / require (runner: python, belt: belt_1_0)
- · **export** — Export / pub / module out (runner: native_bsp, belt: belt_2_0)
- · **module** — Module / package / namespace (runner: python, belt: belt_1_0)
- · **compare** — Compare / eq / ord (runner: native_bsp, belt: belt_1_0)
- · **logic** — Logic / and / or / not (runner: native_bsp, belt: belt_1_0)
- · **math** — Math / arithmetic (runner: native_bsp, belt: belt_1_0)
- · **string** — String / format / concat (runner: python, belt: belt_1_0)
- · **struct** — Struct / record / object (runner: native_bsp, belt: belt_2_0)
- · **index** — Index / subscript / slice (runner: python, belt: belt_1_0)
- · **throw** — Throw / raise / panic (runner: native_bsp, belt: belt_2_0)
- ✓ **catch** — Catch / rescue / except (runner: native_bsp, belt: belt_2_0)
- · **yield** — Yield / generator / coroutine (runner: python, belt: belt_1_0)
- · **lambda** — Lambda / closure / fn (runner: python, belt: belt_1_0)
- ✓ **match** — Pattern match / case (runner: native_bsp, belt: belt_2_0)
- · **async** — Async / await / concurrent (runner: python, belt: belt_1_0)
- ✓ **sync** — Sync / lock / mutex / atomic (runner: native_bsp, belt: belt_2_0)
- · **asm** — Inline asm / intrinsics (runner: native_bsp, belt: belt_2_0)
- · **unsafe** — Unsafe / raw pointer (runner: native_bsp, belt: belt_2_0)
- · **meta** — Macro / reflection / eval (runner: python, belt: belt_1_0)
- ✓ **query** — Query / select / SQL (runner: python, belt: belt_1_0)

## SQL commands by canonical op

### `assign` — Assign / bind / set

- `SET`

### `branch` — Branch / if / switch

- `ELSE`
- `HAVING`
- `IF`
- `THEN`
- `WHERE`

### `call` — Call / invoke / apply

- `CALL`

### `catch` — Catch / rescue / except

- `ROLLBACK`

### `declare` — Declare / define / let

- `ALTER`
- `CREATE`
- `DECLARE`
- `WITH`

### `exec` — Execute / eval / run

- `EXEC`

### `free` — Free / delete / drop

- `DROP`

### `match` — Pattern match / case

- `CASE`
- `WHEN`

### `query` — Query / select / SQL

- `DELETE`
- `FROM`
- `GROUP BY`
- `INSERT`
- `JOIN`
- `ORDER BY`
- `SELECT`
- `UNION`
- `UPDATE`

### `sync` — Sync / lock / mutex / atomic

- `BEGIN`
- `COMMIT`

## SQL full command reference

### `SET`
- **Boils to:** `assign` — Assign / bind / set
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "SET"`

### `ELSE`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "ELSE"`

### `HAVING`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "HAVING"`

### `IF`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "IF"`

### `THEN`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "THEN"`

### `WHERE`
- **Boils to:** `branch` — Branch / if / switch
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "WHERE"`

### `CALL`
- **Boils to:** `call` — Call / invoke / apply
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "CALL"`

### `ROLLBACK`
- **Boils to:** `catch` — Catch / rescue / except
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "ROLLBACK"`

### `ALTER`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "ALTER"`

### `CREATE`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "CREATE"`

### `DECLARE`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "DECLARE"`

### `WITH`
- **Boils to:** `declare` — Declare / define / let
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "WITH"`

### `EXEC`
- **Boils to:** `exec` — Execute / eval / run
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "EXEC"`

### `DROP`
- **Boils to:** `free` — Free / delete / drop
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "DROP"`

### `CASE`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "CASE"`

### `WHEN`
- **Boils to:** `match` — Pattern match / case
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "WHEN"`

### `DELETE`
- **Boils to:** `query` — Query / select / SQL
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "DELETE"`

### `FROM`
- **Boils to:** `query` — Query / select / SQL
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "FROM"`

### `GROUP BY`
- **Boils to:** `query` — Query / select / SQL
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "GROUP BY"`

### `INSERT`
- **Boils to:** `query` — Query / select / SQL
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "INSERT"`

### `JOIN`
- **Boils to:** `query` — Query / select / SQL
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "JOIN"`

### `ORDER BY`
- **Boils to:** `query` — Query / select / SQL
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "ORDER BY"`

### `SELECT`
- **Boils to:** `query` — Query / select / SQL
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "SELECT"`

### `UNION`
- **Boils to:** `query` — Query / select / SQL
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "UNION"`

### `UPDATE`
- **Boils to:** `query` — Query / select / SQL
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "UPDATE"`

### `BEGIN`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "BEGIN"`

### `COMMIT`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Runner:** from canonical op belt map
- **Verify:** `field-program-combinatronic.py boil sql "COMMIT"`

## Execution model

SQL programs execute through the Field program combinatronic facet. Surface syntax
maps to 36 canonical ops; each op selects a belt runner (native_bsp on belt_2_0 or
python on belt_1_0). The explaining manual documents semantics — not a tutorial walkthrough.

- **Paradigm:** declarative
- **Typing discipline:** static schema
- **Memory:** n/a
- **Commands in seed:** 27
- **Canonical ops exercised:** 10

![Memory and objects](h7fig:memory)

## Lexical structure

Tokens partition into identifiers, literals, operators, and significant whitespace
per SQL reference rules. Hostess7 boil heuristics treat unknown tokens as exec
unless a seed keyword maps them. Extended packs inherit parent commands.

- `ALTER` → `declare`
- `BEGIN` → `sync`
- `CALL` → `call`
- `CASE` → `match`
- `COMMIT` → `sync`
- `CREATE` → `declare`
- `DECLARE` → `declare`
- `DELETE` → `query`
- `DROP` → `free`
- `ELSE` → `branch`
- `EXEC` → `exec`
- `FROM` → `query`
- `GROUP BY` → `query`
- `HAVING` → `branch`
- `IF` → `branch`
- `INSERT` → `query`
- `JOIN` → `query`
- `ORDER BY` → `query`
- `ROLLBACK` → `catch`
- `SELECT` → `query`
- `SET` → `assign`
- `THEN` → `branch`
- `UNION` → `query`
- `UPDATE` → `query`

## Type and value space

SQL: relational algebra — SELECT FROM WHERE JOIN GROUP BY. Declarative query language; implementations: PostgreSQL, SQLite, MySQL.

## Control flow

branch · loop · break · continue · return — all languages converge on these atoms.
In SQL, control constructs in the seed pack boil as follows:

- **branch:** `WHERE`, `HAVING`, `IF`, `THEN`, `ELSE`

## Modules and boundaries

import · export · module · package — boundary ops isolate compilation units.
NEXUS-Shield indexes each manual under Dewey 000; combinatronic rebalance may extend packs.

![G16 compile path](h7fig:compile)

## Standard library surface

Where the seed lists I/O or runtime commands, they map to the io and call ops.
Verify any keyword with `field-program-combinatronic.py boil sql "<cmd>"`.

- `CALL`

## Interop and embedding

SQL may embed in Queen Code, Grok16 belt builds, or NEXUS panel scripts.
G16 unified driver (`g16`) compiles C/C++ neighbors; python runner hosts dynamic facets.
Use `g16-compile-combinatronics.py` when program facet gates must pass at compile time.

## Secure compile & run chamber

Every SQL compile and run path is sealed — **no bare host exec**. User code passes
`g16-code-security.py` first, then executes inside `g16-secure-chamber.py` with scrubbed
env (`HOME`, `TMPDIR`, `PATH` limited) so AmmoOS, Hostess 7, and Grok16/bin stay protected.

- **Check:** `g16-secure-chamber.py compile` (stdin JSON: content, lang)
- **Run:** `g16-secure-chamber.py run <path> --lang sql`
- **Posture:** `/api/g16/secure-chamber` · `nexus-g16-bridge.py json` → `secure_chamber`
- **Queen launch:** `runner_policy.sql` = `chamber` in `.launch` manifests
- **Forbidden:** Hostess7, AmmoCode, Grok16/bin, /usr/bin — cannot execute in place

## Performance notes

belt_2_0 native_bsp is the default for hot paths; belt_1_0 python runner applies
when combinatorics bridge degrades the gate. Always-optimal panel pins the best belt
from bench receipts — not guessed from language family alone.

## Research references

Training manuals (school-style textbooks) complement this explaining manual.
See `training_sql` on the Dewey shelf when published.
Field Research book and g16-power-sort plates inform algorithm choices in tooling.

## G16 compile path

- **Boil:** `field-program-combinatronic.py boil sql`
- **Universal facet:** `field-g16-universal-combinatronic.json`
- **Grok16 compile:** `g16-compile-combinatronics.py` with program facet profile
- **Belt runners:** native_bsp (belt_2_0) and python (belt_1_0) per canonical op
- **Secure chamber:** `lib/g16-secure-chamber.py` — mandatory for all 57 Grok16 languages
- **Filetype actions:** `run` / `compile` → `secure_chamber` in field-programming-filetypes.json

## Code patterns

Representative SQL patterns map to canonical ops as follows:

- **Declaration + assign** → declare, assign
- **Conditional** → branch
- **Iteration** → loop, break, continue
- **Procedure call** → call, return
- **Module boundary** → import, export, module
- **I/O** → io
- **Error handling** → throw, catch

## Pitfalls

- Case sensitivity varies — SQL keywords may not match heuristic boil.
- Extended packs inherit parent commands; check `extends` in the seed.
- Unknown tokens fall through to heuristic_keywords before defaulting to exec.
- CDN and macro expansion are advisory until combinatronic rebalance runs.
- **Never run SQL on the bare host** — shell escapes, `eval`, `system`, and JVM/Node
  subprocess calls are blocked transparently; use the sealed chamber lane.
- Missing host toolchains (javac, node, cobc, fpc) return clear errors inside the chamber.

## Where in NEXUS-Shield

- Seed: `data/field-program-combinatronic-seed.json`
- Battery: `field-program-combinatronic.json` (STATE)
- Manual: `library/dewey/000-computer-science/explaining_sql/`
- Reader API: `/api/lang-manuals` · `/api/lang-manuals/sql`
- H7c figures: cover, syntax, op_map, memory, compile (field plate + meld)

