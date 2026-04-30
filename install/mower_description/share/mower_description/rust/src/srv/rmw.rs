#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[link(name = "mower_description__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__mower_description__srv__CuttingMotorControl_Request() -> *const std::ffi::c_void;
}

#[link(name = "mower_description__rosidl_generator_c")]
extern "C" {
    fn mower_description__srv__CuttingMotorControl_Request__init(msg: *mut CuttingMotorControl_Request) -> bool;
    fn mower_description__srv__CuttingMotorControl_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<CuttingMotorControl_Request>, size: usize) -> bool;
    fn mower_description__srv__CuttingMotorControl_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<CuttingMotorControl_Request>);
    fn mower_description__srv__CuttingMotorControl_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<CuttingMotorControl_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<CuttingMotorControl_Request>) -> bool;
}

// Corresponds to mower_description__srv__CuttingMotorControl_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CuttingMotorControl_Request {
    /// 0=关闭, 1=一档, 2=二档, 3=三档
    pub speed_level: i32,

}



impl Default for CuttingMotorControl_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !mower_description__srv__CuttingMotorControl_Request__init(&mut msg as *mut _) {
        panic!("Call to mower_description__srv__CuttingMotorControl_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for CuttingMotorControl_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { mower_description__srv__CuttingMotorControl_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { mower_description__srv__CuttingMotorControl_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { mower_description__srv__CuttingMotorControl_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for CuttingMotorControl_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for CuttingMotorControl_Request where Self: Sized {
  const TYPE_NAME: &'static str = "mower_description/srv/CuttingMotorControl_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__mower_description__srv__CuttingMotorControl_Request() }
  }
}


#[link(name = "mower_description__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__mower_description__srv__CuttingMotorControl_Response() -> *const std::ffi::c_void;
}

#[link(name = "mower_description__rosidl_generator_c")]
extern "C" {
    fn mower_description__srv__CuttingMotorControl_Response__init(msg: *mut CuttingMotorControl_Response) -> bool;
    fn mower_description__srv__CuttingMotorControl_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<CuttingMotorControl_Response>, size: usize) -> bool;
    fn mower_description__srv__CuttingMotorControl_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<CuttingMotorControl_Response>);
    fn mower_description__srv__CuttingMotorControl_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<CuttingMotorControl_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<CuttingMotorControl_Response>) -> bool;
}

// Corresponds to mower_description__srv__CuttingMotorControl_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CuttingMotorControl_Response {
    /// 操作是否成功
    pub success: bool,

    /// 操作结果消息
    pub message: rosidl_runtime_rs::String,

    /// 实际设置的速度 (rad/s)
    pub actual_speed: f64,

}



impl Default for CuttingMotorControl_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !mower_description__srv__CuttingMotorControl_Response__init(&mut msg as *mut _) {
        panic!("Call to mower_description__srv__CuttingMotorControl_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for CuttingMotorControl_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { mower_description__srv__CuttingMotorControl_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { mower_description__srv__CuttingMotorControl_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { mower_description__srv__CuttingMotorControl_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for CuttingMotorControl_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for CuttingMotorControl_Response where Self: Sized {
  const TYPE_NAME: &'static str = "mower_description/srv/CuttingMotorControl_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__mower_description__srv__CuttingMotorControl_Response() }
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


