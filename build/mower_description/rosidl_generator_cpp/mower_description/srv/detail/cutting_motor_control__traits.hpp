// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from mower_description:srv/CuttingMotorControl.idl
// generated code does not contain a copyright notice

#ifndef MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__TRAITS_HPP_
#define MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "mower_description/srv/detail/cutting_motor_control__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace mower_description
{

namespace srv
{

inline void to_flow_style_yaml(
  const CuttingMotorControl_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: speed_level
  {
    out << "speed_level: ";
    rosidl_generator_traits::value_to_yaml(msg.speed_level, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CuttingMotorControl_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: speed_level
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "speed_level: ";
    rosidl_generator_traits::value_to_yaml(msg.speed_level, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CuttingMotorControl_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace mower_description

namespace rosidl_generator_traits
{

[[deprecated("use mower_description::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const mower_description::srv::CuttingMotorControl_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  mower_description::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use mower_description::srv::to_yaml() instead")]]
inline std::string to_yaml(const mower_description::srv::CuttingMotorControl_Request & msg)
{
  return mower_description::srv::to_yaml(msg);
}

template<>
inline const char * data_type<mower_description::srv::CuttingMotorControl_Request>()
{
  return "mower_description::srv::CuttingMotorControl_Request";
}

template<>
inline const char * name<mower_description::srv::CuttingMotorControl_Request>()
{
  return "mower_description/srv/CuttingMotorControl_Request";
}

template<>
struct has_fixed_size<mower_description::srv::CuttingMotorControl_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<mower_description::srv::CuttingMotorControl_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<mower_description::srv::CuttingMotorControl_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace mower_description
{

namespace srv
{

inline void to_flow_style_yaml(
  const CuttingMotorControl_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << ", ";
  }

  // member: actual_speed
  {
    out << "actual_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.actual_speed, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CuttingMotorControl_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }

  // member: actual_speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "actual_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.actual_speed, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CuttingMotorControl_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace mower_description

namespace rosidl_generator_traits
{

[[deprecated("use mower_description::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const mower_description::srv::CuttingMotorControl_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  mower_description::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use mower_description::srv::to_yaml() instead")]]
inline std::string to_yaml(const mower_description::srv::CuttingMotorControl_Response & msg)
{
  return mower_description::srv::to_yaml(msg);
}

template<>
inline const char * data_type<mower_description::srv::CuttingMotorControl_Response>()
{
  return "mower_description::srv::CuttingMotorControl_Response";
}

template<>
inline const char * name<mower_description::srv::CuttingMotorControl_Response>()
{
  return "mower_description/srv/CuttingMotorControl_Response";
}

template<>
struct has_fixed_size<mower_description::srv::CuttingMotorControl_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<mower_description::srv::CuttingMotorControl_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<mower_description::srv::CuttingMotorControl_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<mower_description::srv::CuttingMotorControl>()
{
  return "mower_description::srv::CuttingMotorControl";
}

template<>
inline const char * name<mower_description::srv::CuttingMotorControl>()
{
  return "mower_description/srv/CuttingMotorControl";
}

template<>
struct has_fixed_size<mower_description::srv::CuttingMotorControl>
  : std::integral_constant<
    bool,
    has_fixed_size<mower_description::srv::CuttingMotorControl_Request>::value &&
    has_fixed_size<mower_description::srv::CuttingMotorControl_Response>::value
  >
{
};

template<>
struct has_bounded_size<mower_description::srv::CuttingMotorControl>
  : std::integral_constant<
    bool,
    has_bounded_size<mower_description::srv::CuttingMotorControl_Request>::value &&
    has_bounded_size<mower_description::srv::CuttingMotorControl_Response>::value
  >
{
};

template<>
struct is_service<mower_description::srv::CuttingMotorControl>
  : std::true_type
{
};

template<>
struct is_service_request<mower_description::srv::CuttingMotorControl_Request>
  : std::true_type
{
};

template<>
struct is_service_response<mower_description::srv::CuttingMotorControl_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__TRAITS_HPP_
