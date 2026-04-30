#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to mower_description__srv__CuttingMotorControl_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CuttingMotorControl_Request {
    /// 0=关闭, 1=一档, 2=二档, 3=三档
    pub speed_level: i32,

}



impl Default for CuttingMotorControl_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::CuttingMotorControl_Request::default())
  }
}

impl rosidl_runtime_rs::Message for CuttingMotorControl_Request {
  type RmwMsg = super::srv::rmw::CuttingMotorControl_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        speed_level: msg.speed_level,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      speed_level: msg.speed_level,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      speed_level: msg.speed_level,
    }
  }
}


// Corresponds to mower_description__srv__CuttingMotorControl_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CuttingMotorControl_Response {
    /// 操作是否成功
    pub success: bool,

    /// 操作结果消息
    pub message: std::string::String,

    /// 实际设置的速度 (rad/s)
    pub actual_speed: f64,

}



impl Default for CuttingMotorControl_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::CuttingMotorControl_Response::default())
  }
}

impl rosidl_runtime_rs::Message for CuttingMotorControl_Response {
  type RmwMsg = super::srv::rmw::CuttingMotorControl_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
        message: msg.message.as_str().into(),
        actual_speed: msg.actual_speed,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
        message: msg.message.as_str().into(),
      actual_speed: msg.actual_speed,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
      message: msg.message.to_string(),
      actual_speed: msg.actual_speed,
    }
  }
}






#[link(name = "mower_description__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__mower_description__srv__CuttingMotorControl() -> *const std::ffi::c_void;
}

// Corresponds to mower_description__srv__CuttingMotorControl
#[allow(missing_docs, non_camel_case_types)]
pub struct CuttingMotorControl;

impl rosidl_runtime_rs::Service for CuttingMotorControl {
    type Request = CuttingMotorControl_Request;
    type Response = CuttingMotorControl_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__mower_description__srv__CuttingMotorControl() }
    }
}


