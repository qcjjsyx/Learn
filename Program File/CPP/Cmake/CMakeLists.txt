cmake_minimum_required(VERSION 3.20)

project(
    engine
    LANGUAGES CXX C
    VERSION 1.0.0
)
set(EXPORT_COMPILE_COMMANDS ON)

add_subdirectory(3rdlibs)
add_library(engine STATIC src/main.cpp include/core/assert.hpp include/core/log.hpp include/core/cgmath.hpp)
target_include_directories(engine PUBLIC include)
target_compile_features(engine PUBLIC cxx_std_17) # 改变c++标准
include(CTest)#添加CTest模块
enable_testing()#启用测试
add_subdirectory(test)