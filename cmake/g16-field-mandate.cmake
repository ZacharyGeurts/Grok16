# Grok16 HARD field mandate — 16.1.0-hard
# Exploits DISPERMITTED · fortify · PIE · full RELRO

set(G16_HARD ON)
set(G16_NO_EXPLOIT ON)
set(G16_VERSION "16.1.0-hard")

add_compile_options(
  -O2 -g0
  -fstack-protector-strong
  -D_FORTIFY_SOURCE=2
  -fPIE -fno-plt
  -fstack-clash-protection
  -Wall -Wextra -Wformat -Wformat-security -Werror=format-security
  -DFIELD_MESH=1 -DFIELD_ONE=1 -DHOSTESS7_AUTHORITY=1
  -DG16_HARD=1 -DG16_NO_EXPLOIT=1 -DNO_SOFT_KILL=1
)

add_link_options(
  -pie
  -Wl,-z,relro
  -Wl,-z,now
  -Wl,-z,noexecstack
)

# x86 Field CHIP instructions (software ISA · SSE4.2/POPCNT when host supports)
add_compile_options(-DFIELD_X86_CHIP=1 -msse4.2 -mpopcnt)
