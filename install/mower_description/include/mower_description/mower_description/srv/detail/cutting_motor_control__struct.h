// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from mower_description:srv/CuttingMotorControl.idl
// generated code does not contain a copyright notice

#ifndef MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__STRUCT_H_
#define MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/CuttingMotorControl in the package mower_description.
typedef struct mower_description__srv__CuttingMotorControl_Request
{
  /// 0=关闭, 1=一档, 2=二档, 3=三档
  int32_t speed_level;
} mower_description__srv__CuttingMotorControl_Request;

// Struct for a sequence of mower_description__srv__CuttingMotorControl_Request.
typedef struct mower_description__srv__CuttingMotorControl_Request__Sequence
{
  mower_description__srv__CuttingMotorControl_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} mower_description__srv__CuttingMotorControl_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/CuttingMotorControl in the package mower_description.
typedef struct mower_description__srv__CuttingMotorControl_Response
{
  /// 操作是否成功
  bool success;
  /// 操作结果消息
  rosidl_runtime_c__String message;
  /// 实际设置的速度 (rad/s)
  double actual_speed;
} mower_description__srv__CuttingMotorControl_Response;

// Struct for a sequence of mower_description__srv__CuttingMotorControl_Response.
typedef struct mower_description__srv__CuttingMotorControl_Response__Sequence
{
  mower_description__srv__CuttingMotorControl_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} mower_description__srv__CuttingMotorControl_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__STRUCT_H_
