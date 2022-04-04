cmake_minimum_required(VERSION 3.5)
set(CMAKE_CXX_STANDARD 14)
project(readthedoc-tutorial)

include_directories(
    ${PROJECT_SOURCE_DIR}/include
)
add_library(sample_class src/sample_class.cpp)

add_executable(test src/main.cpp)
target_link_libraries(test
    sample_class
)