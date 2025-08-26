# CMake generated Testfile for 
# Source directory: D:/qcjjsyx/Program File/CPP/Cmake/test
# Build directory: D:/qcjjsyx/Program File/CPP/Cmake/cmake_build/test
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
if(CTEST_CONFIGURATION_TYPE MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
  add_test([=[cgmath_test]=] "D:/qcjjsyx/Program File/CPP/Cmake/cmake_build/test/Debug/cgmath.exe")
  set_tests_properties([=[cgmath_test]=] PROPERTIES  _BACKTRACE_TRIPLES "D:/qcjjsyx/Program File/CPP/Cmake/test/CMakeLists.txt;4;add_test;D:/qcjjsyx/Program File/CPP/Cmake/test/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
  add_test([=[cgmath_test]=] "D:/qcjjsyx/Program File/CPP/Cmake/cmake_build/test/Release/cgmath.exe")
  set_tests_properties([=[cgmath_test]=] PROPERTIES  _BACKTRACE_TRIPLES "D:/qcjjsyx/Program File/CPP/Cmake/test/CMakeLists.txt;4;add_test;D:/qcjjsyx/Program File/CPP/Cmake/test/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
  add_test([=[cgmath_test]=] "D:/qcjjsyx/Program File/CPP/Cmake/cmake_build/test/MinSizeRel/cgmath.exe")
  set_tests_properties([=[cgmath_test]=] PROPERTIES  _BACKTRACE_TRIPLES "D:/qcjjsyx/Program File/CPP/Cmake/test/CMakeLists.txt;4;add_test;D:/qcjjsyx/Program File/CPP/Cmake/test/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
  add_test([=[cgmath_test]=] "D:/qcjjsyx/Program File/CPP/Cmake/cmake_build/test/RelWithDebInfo/cgmath.exe")
  set_tests_properties([=[cgmath_test]=] PROPERTIES  _BACKTRACE_TRIPLES "D:/qcjjsyx/Program File/CPP/Cmake/test/CMakeLists.txt;4;add_test;D:/qcjjsyx/Program File/CPP/Cmake/test/CMakeLists.txt;0;")
else()
  add_test([=[cgmath_test]=] NOT_AVAILABLE)
endif()
