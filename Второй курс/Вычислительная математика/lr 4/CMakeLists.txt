cmake_minimum_required(VERSION 3.16)
project(lr4)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_CXX_FLAGS "-Wextra -lpthread -ltbb")

add_executable(lr4 main.cpp logo.h colors.h)
target_link_libraries(${CMAKE_PROJECT_NAME} ${CMAKE_CXX_FLAGS})
