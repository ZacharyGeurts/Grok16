# Explaining Economics

![Cover — Explaining Economics](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `economics` only.

- **Language id:** `economics`
- **Delta commands:** 89 (of 89 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-30T06:44:03Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** economics
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `credit`
- `quantitative_easing`

### `assign` — Assign / bind / set

- `discount_rate`
- `interest_rate`
- `price`
- `quantity`
- `stimulus`
- `subsidy`
- `tax`

### `branch` — Branch / if / switch

- `budget_constraint`
- `competition`
- `fiscal_policy`

### `call` — Call / invoke / apply

- `master_economist`
- `production_function`

### `catch` — Catch / rescue / except

- `hedge`
- `recovery`

### `compare` — Compare / eq / ord

- `comparative_advantage`
- `equilibrium`
- `opportunity_cost`
- `risk`
- `trade_balance`
- `truth_gate`

### `declare` — Declare / define / let

- `balance_of_payments`
- `capital`
- `debt`
- `demand`
- `employment`
- `entrepreneurship`
- `fixed_cost`
- `GDP`
- `GNP`
- `labor`
- `land`
- `money_supply`
- `preference`
- `sovereign_compute`
- `sunk_cost`
- `supply`
- `unemployment`
- `unit_economics`
- `utility`
- `variable_cost`

### `export` — Export / pub / module out

- `export`

### `free` — Free / delete / drop

- `austerity`

### `import` — Import / use / require

- `import`
- `openstax`
- `tariff`

### `index` — Index / subscript / slice

- `CPI`
- `PPI`
- `stock`

### `loop` — Loop / iterate / repeat

- `indifference_curve`

### `math` — Math / arithmetic

- `average_cost`
- `bandwidth_cost`
- `burn_rate`
- `CAC`
- `deadweight`
- `defense_cost`
- `deflation`
- `elasticity`
- `energy_cost`
- `inflation`
- `loss`
- `LTV`
- `marginal_cost`
- `marginal_revenue`
- `profit`
- `return`
- `revenue`
- `runway`
- `surplus`

### `module` — Module / package / namespace

- `bank`
- `field_economics`
- `market`

### `struct` — Struct / record / object

- `bond`
- `derivative`
- `externality`
- `monopoly`
- `oligopoly`
- `portfolio`
- `private_good`
- `public_good`

### `sync` — Sync / lock / mutex / atomic

- `diversification`
- `monetary_policy`
- `quota`

### `throw` — Throw / raise / panic

- `default`
- `depression`
- `recession`
- `stagflation`

### `verify` — verify

- `corroborate`

## Economics delta command reference

### `credit`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil economics "credit"`

### `quantitative_easing`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil economics "quantitative_easing"`

### `discount_rate`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil economics "discount_rate"`

### `interest_rate`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil economics "interest_rate"`

### `price`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil economics "price"`

### `quantity`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil economics "quantity"`

### `stimulus`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil economics "stimulus"`

### `subsidy`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil economics "subsidy"`

### `tax`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil economics "tax"`

### `budget_constraint`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil economics "budget_constraint"`

### `competition`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil economics "competition"`

### `fiscal_policy`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil economics "fiscal_policy"`

### `master_economist`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil economics "master_economist"`

### `production_function`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil economics "production_function"`

### `hedge`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil economics "hedge"`

### `recovery`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil economics "recovery"`

### `comparative_advantage`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil economics "comparative_advantage"`

### `equilibrium`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil economics "equilibrium"`

### `opportunity_cost`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil economics "opportunity_cost"`

### `risk`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil economics "risk"`

### `trade_balance`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil economics "trade_balance"`

### `truth_gate`
- **Boils to:** `compare` — Compare / eq / ord
- **Verify:** `field-program-combinatronic.py boil economics "truth_gate"`

### `balance_of_payments`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "balance_of_payments"`

### `capital`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "capital"`

### `debt`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "debt"`

### `demand`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "demand"`

### `employment`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "employment"`

### `entrepreneurship`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "entrepreneurship"`

### `fixed_cost`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "fixed_cost"`

### `GDP`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "GDP"`

### `GNP`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "GNP"`

### `labor`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "labor"`

### `land`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "land"`

### `money_supply`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "money_supply"`

### `preference`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "preference"`

### `sovereign_compute`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "sovereign_compute"`

### `sunk_cost`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "sunk_cost"`

### `supply`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "supply"`

### `unemployment`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "unemployment"`

### `unit_economics`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "unit_economics"`

### `utility`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "utility"`

### `variable_cost`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil economics "variable_cost"`

### `export`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil economics "export"`

### `austerity`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil economics "austerity"`

### `import`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil economics "import"`

### `openstax`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil economics "openstax"`

### `tariff`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil economics "tariff"`

### `CPI`
- **Boils to:** `index` — Index / subscript / slice
- **Verify:** `field-program-combinatronic.py boil economics "CPI"`

### `PPI`
- **Boils to:** `index` — Index / subscript / slice
- **Verify:** `field-program-combinatronic.py boil economics "PPI"`

### `stock`
- **Boils to:** `index` — Index / subscript / slice
- **Verify:** `field-program-combinatronic.py boil economics "stock"`

### `indifference_curve`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil economics "indifference_curve"`

### `average_cost`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "average_cost"`

### `bandwidth_cost`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "bandwidth_cost"`

### `burn_rate`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "burn_rate"`

### `CAC`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "CAC"`

### `deadweight`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "deadweight"`

### `defense_cost`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "defense_cost"`

### `deflation`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "deflation"`

### `elasticity`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "elasticity"`

### `energy_cost`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "energy_cost"`

### `inflation`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "inflation"`

### `loss`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "loss"`

### `LTV`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "LTV"`

### `marginal_cost`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "marginal_cost"`

### `marginal_revenue`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "marginal_revenue"`

### `profit`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "profit"`

### `return`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "return"`

### `revenue`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "revenue"`

### `runway`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "runway"`

### `surplus`
- **Boils to:** `math` — Math / arithmetic
- **Verify:** `field-program-combinatronic.py boil economics "surplus"`

### `bank`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil economics "bank"`

### `field_economics`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil economics "field_economics"`

### `market`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil economics "market"`

### `bond`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil economics "bond"`

### `derivative`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil economics "derivative"`

### `externality`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil economics "externality"`

### `monopoly`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil economics "monopoly"`

### `oligopoly`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil economics "oligopoly"`

### `portfolio`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil economics "portfolio"`

### `private_good`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil economics "private_good"`

### `public_good`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil economics "public_good"`

### `diversification`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil economics "diversification"`

### `monetary_policy`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil economics "monetary_policy"`

### `quota`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil economics "quota"`

### `default`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil economics "default"`

### `depression`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil economics "depression"`

### `recession`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil economics "recession"`

### `stagflation`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil economics "stagflation"`

### `corroborate`
- **Boils to:** `verify` — verify
- **Verify:** `field-program-combinatronic.py boil economics "corroborate"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — economics

- **Run:** `g16-secure-chamber.py run <file> --lang economics`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil economics`

