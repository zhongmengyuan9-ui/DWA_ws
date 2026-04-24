// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from mower_description:srv/CuttingMotorControl.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "mower_description/srv/detail/cutting_motor_control__rosidl_typesupport_introspection_c.h"
#include "mower_description/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "mower_description/srv/detail/cutting_motor_control__functions.h"
#include "mower_description/srv/detail/cutting_motor_control__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  mower_description__srv__CuttingMotorControl_Request__init(message_memory);
}

void mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_fini_function(void * message_memory)
{
  mower_description__srv__CuttingMotorControl_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_message_member_array[1] = {
  {
    "speed_level",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mower_description__srv__CuttingMotorControl_Request, speed_level),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_message_members = {
  "mower_description__srv",  // message namespace
  "CuttingMotorControl_Request",  // message name
  1,  // number of fields
  sizeof(mower_description__srv__CuttingMotorControl_Request),
  mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_message_member_array,  // message members
  mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_message_type_support_handle = {
  0,
  &mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mower_description
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mower_description, srv, CuttingMotorControl_Request)() {
  if (!mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_message_type_support_handle.typesupport_identifier) {
    mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &mower_description__srv__CuttingMotorControl_Request__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "mower_description/srv/detail/cutting_motor_control__rosidl_typesupport_introspection_c.h"
// already included above
// #include "mower_description/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "mower_description/srv/detail/cutting_motor_control__functions.h"
// already included above
// #include "mower_description/srv/detail/cutting_motor_control__struct.h"


// Include directives for member types
// Member `message`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  mower_description__srv__CuttingMotorControl_Response__init(message_memory);
}

void mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_fini_function(void * message_memory)
{
  mower_description__srv__CuttingMotorControl_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_message_member_array[3] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mower_description__srv__CuttingMotorControl_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mower_description__srv__CuttingMotorControl_Response, message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "actual_speed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mower_description__srv__CuttingMotorControl_Response, actual_speed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_message_members = {
  "mower_description__srv",  // message namespace
  "CuttingMotorControl_Response",  // message name
  3,  // number of fields
  sizeof(mower_description__srv__CuttingMotorControl_Response),
  mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_message_member_array,  // message members
  mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_message_type_support_handle = {
  0,
  &mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mower_description
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mower_description, srv, CuttingMotorControl_Response)() {
  if (!mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_message_type_support_handle.typesupport_identifier) {
    mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &mower_description__srv__CuttingMotorControl_Response__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "mower_description/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "mower_description/srv/detail/cutting_motor_control__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers mower_description__srv__detail__cutting_motor_control__rosidl_typesupport_introspection_c__CuttingMotorControl_service_members = {
  "mower_description__srv",  // service namespace
  "CuttingMotorControl",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // mower_description__srv__detail__cutting_motor_control__rosidl_typesupport_introspection_c__CuttingMotorControl_Request_message_type_support_handle,
  NULL  // response message
  // mower_description__srv__detail__cutting_motor_control__rosidl_typesupport_introspection_c__CuttingMotorControl_Response_message_type_support_handle
};

static rosidl_service_type_support_t mower_description__srv__detail__cutting_motor_control__rosidl_typesupport_introspection_c__CuttingMotorControl_service_type_support_handle = {
  0,
  &mower_description__srv__detail__cutting_motor_control__rosidl_typesupport_introspection_c__CuttingMotorControl_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mower_description, srv, CuttingMotorControl_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mower_description, srv, CuttingMotorControl_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mower_description
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mower_description, srv, CuttingMotorControl)() {
  if (!mower_description__srv__detail__cutting_motor_control__rosidl_typesupport_introspection_c__CuttingMotorControl_service_type_support_handle.typesupport_identifier) {
    mower_description__srv__detail__cutting_motor_control__rosidl_typesupport_introspection_c__CuttingMotorControl_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)mower_description__srv__detail__cutting_motor_control__rosidl_typesupport_introspection_c__CuttingMotorControl_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mower_description, srv, CuttingMotorControl_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mower_description, srv, CuttingMotorControl_Response)()->data;
  }

  return &mower_description__srv__detail__cutting_motor_control__rosidl_typesupport_introspection_c__CuttingMotorControl_service_type_support_handle;
}
