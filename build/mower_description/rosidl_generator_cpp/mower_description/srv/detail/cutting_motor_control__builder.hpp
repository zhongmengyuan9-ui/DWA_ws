// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mower_description:srv/CuttingMotorControl.idl
// generated code does not contain a copyright notice

#ifndef MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__BUILDER_HPP_
#define MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "mower_description/srv/detail/cutting_motor_control__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace mower_description
{

namespace srv
{

namespace builder
{

class Init_CuttingMotorControl_Request_speed_level
{
public:
  Init_CuttingMotorControl_Request_speed_level()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::mower_description::srv::CuttingMotorControl_Request speed_level(::mower_description::srv::CuttingMotorControl_Request::_speed_level_type arg)
  {
    msg_.speed_level = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mower_description::srv::CuttingMotorControl_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::mower_description::srv::CuttingMotorControl_Request>()
{
  return mower_description::srv::builder::Init_CuttingMotorControl_Request_speed_level();
}

}  // namespace mower_description


namespace mower_description
{

namespace srv
{

namespace builder
{

class Init_CuttingMotorControl_Response_actual_speed
{
public:
  explicit Init_CuttingMotorControl_Response_actual_speed(::mower_description::srv::CuttingMotorControl_Response & msg)
  : msg_(msg)
  {}
  ::mower_description::srv::CuttingMotorControl_Response actual_speed(::mower_description::srv::CuttingMotorControl_Response::_actual_speed_type arg)
  {
    msg_.actual_speed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mower_description::srv::CuttingMotorControl_Response msg_;
};

class Init_CuttingMotorControl_Response_message
{
public:
  explicit Init_CuttingMotorControl_Response_message(::mower_description::srv::CuttingMotorControl_Response & msg)
  : msg_(msg)
  {}
  Init_CuttingMotorControl_Response_actual_speed message(::mower_description::srv::CuttingMotorControl_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return Init_CuttingMotorControl_Response_actual_speed(msg_);
  }

private:
  ::mower_description::srv::CuttingMotorControl_Response msg_;
};

class Init_CuttingMotorControl_Response_success
{
public:
  Init_CuttingMotorControl_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CuttingMotorControl_Response_message success(::mower_description::srv::CuttingMotorControl_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_CuttingMotorControl_Response_message(msg_);
  }

private:
  ::mower_description::srv::CuttingMotorControl_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::mower_description::srv::CuttingMotorControl_Response>()
{
  return mower_description::srv::builder::Init_CuttingMotorControl_Response_success();
}

}  // namespace mower_description

#endif  // MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__BUILDER_HPP_
