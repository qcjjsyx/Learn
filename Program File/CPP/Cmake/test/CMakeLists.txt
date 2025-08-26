

add_executable(cgmath ./cgmath.cpp)#添加测试目标，生成可执行文件
add_test(NAME cgmath_test COMMAND $<TARGET_FILE:cgmath>)#添加测试
target_link_libraries(cgmath PRIVATE engine)#链接engine库
