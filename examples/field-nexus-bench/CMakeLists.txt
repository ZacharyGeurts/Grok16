cmake_minimum_required(VERSION 3.20)
project(grok16_field_nexus_bench CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED OFF)

if(EXISTS "${CMAKE_CURRENT_LIST_DIR}/../../cmake/grok16-profile-field-opt.cmake")
  include("${CMAKE_CURRENT_LIST_DIR}/../../cmake/grok16-profile-field-opt.cmake")
elseif(EXISTS "${CMAKE_CURRENT_LIST_DIR}/../../cmake/grok16-profile-ai.cmake")
  include("${CMAKE_CURRENT_LIST_DIR}/../../cmake/grok16-profile-ai.cmake")
endif()

add_executable(grok16_field_nexus_bench field_nexus_bench.cpp)