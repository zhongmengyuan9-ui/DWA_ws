// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from mower_description:srv/CuttingMotorControl.idl
// generated code does not contain a copyright notice

#ifndef MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__STRUCT_HPP_
#define MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__mower_description__srv__CuttingMotorControl_Request __attribute__((deprecated))
#else
# define DEPRECATED__mower_description__srv__CuttingMotorControl_Request __declspec(deprecated)
#endif

namespace mower_description
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct CuttingMotorControl_Request_
{
  using Type = CuttingMotorControl_Request_<ContainerAllocator>;

  explicit CuttingMotorControl_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->speed_level = 0l;
    }
  }

  explicit CuttingMotorControl_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->speed_level = 0l;
    }
  }

  // field types and members
  using _speed_level_type =
    int32_t;
  _speed_level_type speed_level;

  // setters for named parameter idiom
  Type & set__speed_level(
    const int32_t & _arg)
  {
    this->speed_level = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__mower_description__srv__CuttingMotorControl_Request
    std::shared_ptr<mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__mower_description__srv__CuttingMotorControl_Request
    std::shared_ptr<mower_description::srv::CuttingMotorControl_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CuttingMotorControl_Request_ & other) const
  {
    if (this->speed_level != other.speed_level) {
      return false;
    }
    return true;
  }
  bool operator!=(const CuttingMotorControl_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CuttingMotorControl_Request_

// alias to use template instance with default allocator
using CuttingMotorControl_Request =
  mower_description::srv::CuttingMotorControl_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace mower_description


#ifndef _WIN32
# define DEPRECATED__mower_description__srv__CuttingMotorControl_Response __attribute__((deprecated))
#else
# define DEPRECATED__mower_description__srv__CuttingMotorControl_Response __declspec(deprecated)
#endif

namespace mower_description
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct CuttingMotorControl_Response_
{
  using Type = CuttingMotorControl_Response_<ContainerAllocator>;

  explicit CuttingMotorControl_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
      this->actual_speed = 0.0;
    }
  }

  explicit CuttingMotorControl_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
      this->actual_speed = 0.0;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;
  using _actual_speed_type =
    double;
  _actual_speed_type actual_speed;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }
  Type & set__actual_speed(
    const double & _arg)
  {
    this->actual_speed = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__mower_description__srv__CuttingMotorControl_Response
    std::shared_ptr<mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__mower_description__srv__CuttingMotorControl_Response
    std::shared_ptr<mower_description::srv::CuttingMotorControl_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CuttingMotorControl_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    if (this->actual_speed != other.actual_speed) {
      return false;
    }
    return true;
  }
  bool operator!=(const CuttingMotorControl_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CuttingMotorControl_Response_

// alias to use template instance with default allocator
using CuttingMotorControl_Response =
  mower_description::srv::CuttingMotorControl_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace mower_description

namespace mower_description
{

namespace srv
{

struct CuttingMotorControl
{
  using Request = mower_description::srv::CuttingMotorControl_Request;
  using Response = mower_description::srv::CuttingMotorControl_Response;
};

}  // namespace srv

}  // namespace mower_description

#endif  // MOWER_DESCRIPTION__SRV__DETAIL__CUTTING_MOTOR_CONTROL__STRUCT_HPP_
