# Safety (2.0)

Web: [integration.html](https://zacharygeurts.github.io/Grok16/integration.html#gates)

Grok16 2.0 safety is melded into Ironclad at integrate time — compile-time mandate plus consumer depth impossibility.

## Depth fields sealed and destroyed

| Gate | Behavior |
|------|----------|
| `field-depth-singularizer` | Seal and destroy `field_depth`, zero nested layers, ledger violations |
| Queen field-net | `depth_field_impossible: true` on classify |
| Queen browser | Navigate strips depth before tab persist |
| NEXUS HTTP | 302 redirect when `?field_depth=` present |

**Rule:** one field, depth zero always. Creation cannot persist.

## Ironclad meld

- `data/g16-ironclad-meld.json` — time linear, single fabric, field sanity verses
- `g16-ironclad-sanity` gate in forge and batteries
- `G16_FIELD_SAFETY_MANDATE_v1` on field targets

## Sovereign time

Time is linear (`ironclad:time:1`). G1ID meld uses `linear_ns` only — `t` forbidden in geometry.

## Integrate

```bash
./scripts/grok16-integrate.sh
```

Publishes `data/grok16-integrate.env` and wires Queen / World_Redata / ZOCR to canonical prefix + belt profile.