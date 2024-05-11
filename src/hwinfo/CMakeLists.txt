add_executable(Example example.cpp)
add_subdirectory(third_party/hwinfo)
target_link_libraries(Example PUBLIC hwinfo::HWinfo)
