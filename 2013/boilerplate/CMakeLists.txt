project(x_round_y)
cmake_minimum_required(VERSION 3.11.0)

set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(TASKS "task1;task2;task3")

foreach(TASK ${TASKS})
    add_executable(${TASK} ${TASK}.cpp)
endforeach()