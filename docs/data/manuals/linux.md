# Explaining Linux

![Cover — Explaining Linux](h7fig:cover)

**Grok15 condensed manual** — shared sections live in `explaining_core`; this file is the
non-redundant **delta** for `linux` only.

- **Language id:** `linux`
- **Delta commands:** 112 (of 112 total after inherit)
- **Extends:** — (root pack)
- **Family:** —
- **secure_chamber:** True
- **Generated:** 2026-06-29T12:26:40Z

## At a glance

- **Driver:** g16-interp
- **Runtime:** linux
- **Belt:** belt_1_0

![Syntax overview](h7fig:syntax)

![Canonical op map](h7fig:op_map)

## Language delta — commands not in parent pack

### `alloc` — Allocate / new / malloc

- `mkdir`

### `assign` — Assign / bind / set

- `chgrp`
- `chmod`
- `chown`
- `ldconfig`
- `mv`
- `nice`
- `passwd`
- `renice`
- `sysctl`

### `async` — Async / await / concurrent

- `&`
- `at`
- `bg`
- `nohup`
- `wait`

### `branch` — Branch / if / switch

- `elif`
- `else`
- `esac`
- `if`
- `iptables`
- `nft`
- `tristate`

### `break` — Break / leave loop

- `break`

### `call` — Call / invoke / apply

- `ld`
- `service`
- `su`
- `systemctl`

### `catch` — Catch / rescue / except

- `trap`

### `continue` — Continue / next iteration

- `continue`

### `declare` — Declare / define / let

- `cgroup`
- `function`
- `groupadd`
- `HostPassthrough`
- `ln`
- `umask`
- `unshare`
- `useradd`

### `exec` — Execute / eval / run

- `$(...)`
- `cgexec`
- `cmake`
- `eval`
- `exec`
- `fork`
- `g++`
- `gcc`
- `Hostess7.sh`
- `install-all.sh`
- `linux.sh`
- `make`
- `spawn`

### `export` — Export / pub / module out

- `export`

### `free` — Free / delete / drop

- `rm`
- `rmdir`
- `rmmod`

### `import` — Import / use / require

- `.`
- `apt`
- `apt-get`
- `dnf`
- `dpkg`
- `insmod`
- `modprobe`
- `pacman`
- `source`

### `io` — I/O / print / read / write file

- `<`
- `>`
- `>>`
- `cat`
- `cp`
- `echo`
- `ip`
- `journalctl`
- `ldd`
- `ls`
- `lsmod`
- `ltrace`
- `mount`
- `netstat`
- `printf`
- `ps`
- `read`
- `ss`
- `strace`
- `tee`
- `umount`
- `|`

### `load` — Load / read memory

- `/proc`
- `/proc/kilroy_field`
- `/sys`
- `kilroy`
- `proc`

### `logic` — Logic / and / or / not

- `&&`
- `||`

### `loop` — Loop / iterate / repeat

- `cron`
- `find`
- `for`
- `until`
- `while`

### `match` — Pattern match / case

- `case`

### `module` — Module / package / namespace

- `docker`
- `namespace`
- `podman`
- `systemd`

### `query` — Query / select / SQL

- `grep`

### `return` — Return / exit function

- `exit`
- `return`

### `struct` — Struct / record / object

- `container`

### `sync` — Sync / lock / mutex / atomic

- `nftables`
- `polkit`
- `sudo`

### `throw` — Throw / raise / panic

- `kill`
- `killall`
- `set -e`

## Linux delta command reference

### `mkdir`
- **Boils to:** `alloc` — Allocate / new / malloc
- **Verify:** `field-program-combinatronic.py boil linux "mkdir"`

### `chgrp`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil linux "chgrp"`

### `chmod`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil linux "chmod"`

### `chown`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil linux "chown"`

### `ldconfig`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil linux "ldconfig"`

### `mv`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil linux "mv"`

### `nice`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil linux "nice"`

### `passwd`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil linux "passwd"`

### `renice`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil linux "renice"`

### `sysctl`
- **Boils to:** `assign` — Assign / bind / set
- **Verify:** `field-program-combinatronic.py boil linux "sysctl"`

### `&`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil linux "&"`

### `at`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil linux "at"`

### `bg`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil linux "bg"`

### `nohup`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil linux "nohup"`

### `wait`
- **Boils to:** `async` — Async / await / concurrent
- **Verify:** `field-program-combinatronic.py boil linux "wait"`

### `elif`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil linux "elif"`

### `else`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil linux "else"`

### `esac`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil linux "esac"`

### `if`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil linux "if"`

### `iptables`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil linux "iptables"`

### `nft`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil linux "nft"`

### `tristate`
- **Boils to:** `branch` — Branch / if / switch
- **Verify:** `field-program-combinatronic.py boil linux "tristate"`

### `break`
- **Boils to:** `break` — Break / leave loop
- **Verify:** `field-program-combinatronic.py boil linux "break"`

### `ld`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil linux "ld"`

### `service`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil linux "service"`

### `su`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil linux "su"`

### `systemctl`
- **Boils to:** `call` — Call / invoke / apply
- **Verify:** `field-program-combinatronic.py boil linux "systemctl"`

### `trap`
- **Boils to:** `catch` — Catch / rescue / except
- **Verify:** `field-program-combinatronic.py boil linux "trap"`

### `continue`
- **Boils to:** `continue` — Continue / next iteration
- **Verify:** `field-program-combinatronic.py boil linux "continue"`

### `cgroup`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil linux "cgroup"`

### `function`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil linux "function"`

### `groupadd`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil linux "groupadd"`

### `HostPassthrough`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil linux "HostPassthrough"`

### `ln`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil linux "ln"`

### `umask`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil linux "umask"`

### `unshare`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil linux "unshare"`

### `useradd`
- **Boils to:** `declare` — Declare / define / let
- **Verify:** `field-program-combinatronic.py boil linux "useradd"`

### `$(...)`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "$(...)"`

### `cgexec`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "cgexec"`

### `cmake`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "cmake"`

### `eval`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "eval"`

### `exec`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "exec"`

### `fork`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "fork"`

### `g++`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "g++"`

### `gcc`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "gcc"`

### `Hostess7.sh`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "Hostess7.sh"`

### `install-all.sh`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "install-all.sh"`

### `linux.sh`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "linux.sh"`

### `make`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "make"`

### `spawn`
- **Boils to:** `exec` — Execute / eval / run
- **Verify:** `field-program-combinatronic.py boil linux "spawn"`

### `export`
- **Boils to:** `export` — Export / pub / module out
- **Verify:** `field-program-combinatronic.py boil linux "export"`

### `rm`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil linux "rm"`

### `rmdir`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil linux "rmdir"`

### `rmmod`
- **Boils to:** `free` — Free / delete / drop
- **Verify:** `field-program-combinatronic.py boil linux "rmmod"`

### `.`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil linux "."`

### `apt`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil linux "apt"`

### `apt-get`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil linux "apt-get"`

### `dnf`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil linux "dnf"`

### `dpkg`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil linux "dpkg"`

### `insmod`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil linux "insmod"`

### `modprobe`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil linux "modprobe"`

### `pacman`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil linux "pacman"`

### `source`
- **Boils to:** `import` — Import / use / require
- **Verify:** `field-program-combinatronic.py boil linux "source"`

### `<`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "<"`

### `>`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux ">"`

### `>>`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux ">>"`

### `cat`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "cat"`

### `cp`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "cp"`

### `echo`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "echo"`

### `ip`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "ip"`

### `journalctl`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "journalctl"`

### `ldd`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "ldd"`

### `ls`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "ls"`

### `lsmod`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "lsmod"`

### `ltrace`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "ltrace"`

### `mount`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "mount"`

### `netstat`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "netstat"`

### `printf`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "printf"`

### `ps`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "ps"`

### `read`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "read"`

### `ss`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "ss"`

### `strace`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "strace"`

### `tee`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "tee"`

### `umount`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "umount"`

### `|`
- **Boils to:** `io` — I/O / print / read / write file
- **Verify:** `field-program-combinatronic.py boil linux "|"`

### `/proc`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil linux "/proc"`

### `/proc/kilroy_field`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil linux "/proc/kilroy_field"`

### `/sys`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil linux "/sys"`

### `kilroy`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil linux "kilroy"`

### `proc`
- **Boils to:** `load` — Load / read memory
- **Verify:** `field-program-combinatronic.py boil linux "proc"`

### `&&`
- **Boils to:** `logic` — Logic / and / or / not
- **Verify:** `field-program-combinatronic.py boil linux "&&"`

### `||`
- **Boils to:** `logic` — Logic / and / or / not
- **Verify:** `field-program-combinatronic.py boil linux "||"`

### `cron`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil linux "cron"`

### `find`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil linux "find"`

### `for`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil linux "for"`

### `until`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil linux "until"`

### `while`
- **Boils to:** `loop` — Loop / iterate / repeat
- **Verify:** `field-program-combinatronic.py boil linux "while"`

### `case`
- **Boils to:** `match` — Pattern match / case
- **Verify:** `field-program-combinatronic.py boil linux "case"`

### `docker`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil linux "docker"`

### `namespace`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil linux "namespace"`

### `podman`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil linux "podman"`

### `systemd`
- **Boils to:** `module` — Module / package / namespace
- **Verify:** `field-program-combinatronic.py boil linux "systemd"`

### `grep`
- **Boils to:** `query` — Query / select / SQL
- **Verify:** `field-program-combinatronic.py boil linux "grep"`

### `exit`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil linux "exit"`

### `return`
- **Boils to:** `return` — Return / exit function
- **Verify:** `field-program-combinatronic.py boil linux "return"`

### `container`
- **Boils to:** `struct` — Struct / record / object
- **Verify:** `field-program-combinatronic.py boil linux "container"`

### `nftables`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil linux "nftables"`

### `polkit`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil linux "polkit"`

### `sudo`
- **Boils to:** `sync` — Sync / lock / mutex / atomic
- **Verify:** `field-program-combinatronic.py boil linux "sudo"`

### `kill`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil linux "kill"`

### `killall`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil linux "killall"`

### `set -e`
- **Boils to:** `throw` — Throw / raise / panic
- **Verify:** `field-program-combinatronic.py boil linux "set -e"`

## Shared reference (explaining_core)

The following sections are **not duplicated** per language — read once:

- Canonical combinatronic atoms (36 ops)
- Secure compile & run chamber
- G16 compile path · performance · pitfalls · NEXUS paths

→ `library/dewey/000-computer-science/explaining_core/explaining_core.md`

## G16 & secure chamber — linux

- **Run:** `g16-secure-chamber.py run <file> --lang linux`
- **Compile:** `g16-secure-chamber.py compile` (stdin JSON)
- **Boil:** `field-program-combinatronic.py boil linux`

