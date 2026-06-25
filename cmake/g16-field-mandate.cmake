# G16 Field Safety Mandate — mandatory for all G16 field targets (WRDT, FieldX86, …)
# Rust-grade discipline: fortify, stack protection, RELRO+NOW, PIE. No opt-out in release.

set(G16_FIELD_MANDATE_ID "G16_FIELD_SAFETY_MANDATE_v1" CACHE STRING "G16 safety mandate version")

function(g16_field_mandate target)
  if(NOT TARGET ${target})
    message(FATAL_ERROR "g16_field_mandate: unknown target ${target}")
  endif()
  target_compile_definitions(${target} PRIVATE _FORTIFY_SOURCE=3 G16_FIELD_MANDATE=1)
  target_compile_options(${target} PRIVATE
    -fstack-protector-strong
    -fstack-clash-protection
    -fcf-protection=full
    -fno-strict-aliasing
    -Wformat -Wformat-security
    -Werror=format-security
    -fPIE
  )
  if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    target_link_options(${target} PRIVATE -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -pie)
  endif()
endfunction()