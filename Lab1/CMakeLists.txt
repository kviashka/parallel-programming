project(Lab1 CXX)

add_executable(matrix-mul src/main.cpp src/matrix.cpp)
target_compile_options(matrix-mul PRIVATE -O2)