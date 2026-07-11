# Grok16 · 16.1.0-hard

**Sovereign Field compiler plane** · paired with **AmmoCode 6.2** full suite editor.

| | |
|--|--|
| **Hard plane** | this repo · `16.1.0-hard` |
| **Editor suite** | [AmmoCode 6.2](https://github.com/ZacharyGeurts/AmmoCode) |
| **Live editor** | https://zacharygeurts.github.io/AmmoCode/ |
| **Pages** | https://zacharygeurts.github.io/Grok16/ |
| **Hostess 7** | https://github.com/ZacharyGeurts/Hostess7 |

## AmmoCode ↔ Grok16

AmmoCode is the **full compiler suite + code editor** (language dropdown, popular/A–Z, BASIC/QBasic/…).  
Grok16 is the **hard compile plane** (`g16` / `g++16` / Field bins).

```bash
# Editor (clone AmmoCode)
python3 ammocode.py   # http://127.0.0.1:9555/
# or Pages: https://zacharygeurts.github.io/AmmoCode/

# Compile plane (this tree)
./bin/g16 -c foo.c -o foo.o
./bin/g++16 -c foo.cpp -o foo.o
./bin/field-elevate autoelevate
```

Pair: `data/ammocode-pair.json`

## Policy

Exploits dispermitted · polkit HOSTILE · field-elevate only · RELRO/NOW/PIE.

Ironclad: `ironclad:g16-hard:2`
