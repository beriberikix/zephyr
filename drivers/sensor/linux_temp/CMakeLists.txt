# SPDX-License-Identifier: Apache-2.0

zephyr_library()

if(NOT CONFIG_NATIVE_HOST_HAS_SYSFS)
  message(FATAL_ERROR
    "CONFIG_NATIVE_LINUX_TEMP reads a sysfs thermal file, which this build "
    "host (${CMAKE_HOST_SYSTEM_NAME}) does not provide "
    "(CONFIG_NATIVE_HOST_HAS_SYSFS=n).")
endif()

zephyr_library_sources(linux_temp.c)
target_sources(native_simulator INTERFACE linux_temp_bottom.c)
