CMake 是一个工程生成器，会生成一个工程，不一定是VS工程
1. 创建CMakeLists.txt ,官方指定的脚本文件名称
2. cmake 初始化命令行：cmake -S . -B cmake_build；-B后面跟的是你希望输出到的文件夹
3. 基于CMake的vs工程与传统的VS工程不一样，不能直接使用vs进行配置，只能在cmake上配置
4. cmake -G 可以看到所有能够生成的工程
5. cmake --build 工程文件夹就可以编译

单元测试
