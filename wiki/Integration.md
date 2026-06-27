# Integration

Web: [integration.html](https://zacharygeurts.github.io/Grok16/integration.html)

Requires Grok16 **v2.0.0** with `test-battery-release` + `test-battery-belt` green.

## Auto-integrate (2.0)

```bash
./scripts/grok16-integrate.sh
```

Wires canonical prefix + `G16_BELT_PROFILE=belt_2_0` to:

- `NewLatest/Queen`
- `World_Redata`
- `ZOCR` / Final_Ear
- `PythonG`

Env template: `data/grok16-integrate.env`

## Safety at consumers {#gates}

Integrated SG tree enforces **single fabric** safety:

| Consumer | Depth field | Ironclad |
|----------|-------------|----------|
| Queen field-net | `depth_field_impossible` | classify strip |
| Queen browser | navigate enforce | tab URL clean |
| NEXUS panel | HTTP 302 strip | field-depth-singularizer |
| Field sanity | integral preflight | `ironclad:field_sanity:4` |

Doctrine cross-ref: `NewLatest/data/single-field-depth-doctrine.json`

## World_Redata

```bash
cd World_Redata
./build-cpp.sh
PYTHONPATH=. pythong -m redata.cli parity
PYTHONPATH=. pythong -m redata.cli security
```

## Env

```bash
export G16_PREFIX=/path/to/Grok16
export G16_BELT_PROFILE=belt_2_0
export WRDT_G16_PREFIX="$G16_PREFIX"
source data/grok16-integrate.env
```

## Queen

`./scripts/grok16-integrate.sh` updates Queen `g16-toolchain.json` and browser doctrine.

## Ironclad

`data/g16-ironclad-meld.json` — single fabric, linear time, field sanity absorbed at forge link pass.