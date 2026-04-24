#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "mower_description::mower_description__rosidl_generator_py" for configuration ""
set_property(TARGET mower_description::mower_description__rosidl_generator_py APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(mower_description::mower_description__rosidl_generator_py PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libmower_description__rosidl_generator_py.so"
  IMPORTED_SONAME_NOCONFIG "libmower_description__rosidl_generator_py.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS mower_description::mower_description__rosidl_generator_py )
list(APPEND _IMPORT_CHECK_FILES_FOR_mower_description::mower_description__rosidl_generator_py "${_IMPORT_PREFIX}/lib/libmower_description__rosidl_generator_py.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
