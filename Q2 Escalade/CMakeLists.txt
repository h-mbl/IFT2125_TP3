cmake_minimum_required(VERSION 3.22)
project(Q2_Escalade)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(Q2_Escalade
        climbing_difficulty.cpp
        ClimbingDifficultyCalculator.cpp
        ClimbingDifficultyCalculator.h)
