# Grok16 Vulkan/RTX-oriented CPU kernel profile (AMOURANTHRTX-style prep)
if(NOT GROK16_PROFILE STREQUAL "vulkan_rtx")
  set(GROK16_PROFILE "vulkan_rtx" CACHE STRING "Grok16 build profile" FORCE)
endif()
set(GROK16_CXX_STD "gnu++26" CACHE STRING "Grok16 C++ standard" FORCE)
add_compile_definitions(GROK16_PROFILE_VULKAN=1 FIELD_X86_DIE=1)
add_compile_options(
  -std=gnu++26 -O3 -march=native
  -msse4.2 -mavx2 -mfma -ffast-math -funroll-loops
)
add_link_options(-flto)