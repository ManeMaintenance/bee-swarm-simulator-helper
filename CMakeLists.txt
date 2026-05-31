cmake_minimum_required(VERSION 3.10)
project(bee-swarm-simulator-helper)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(bee_helper
    src/main.cpp
    src/autofarm.cpp
    src/utils.cpp
)

target_include_directories(bee_helper PRIVATE src)
target_link_libraries(bee_helper PRIVATE fmt)