cmake_minimum_required(VERSION 3.12)
project(Lab2)

set(CMAKE_CXX_STANDARD 17)

find_package(OpenMP REQUIRED)

add_executable(matrix_mult_omp scr/main.cpp)

# Подключение флагов OpenMP к проекту
if(OpenMP_CXX_FOUND)
    target_link_libraries(matrix_mult_omp PRIVATE OpenMP::OpenMP_CXX)
endif()