// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from mower_description:srv/CuttingMotorControl.idl
// generated code does not contain a copyright notice
#include "mower_description/srv/detail/cutting_motor_control__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
mower_description__srv__CuttingMotorControl_Request__init(mower_description__srv__CuttingMotorControl_Request * msg)
{
  if (!msg) {
    return false;
  }
  // speed_level
  return true;
}

void
mower_description__srv__CuttingMotorControl_Request__fini(mower_description__srv__CuttingMotorControl_Request * msg)
{
  if (!msg) {
    return;
  }
  // speed_level
}

bool
mower_description__srv__CuttingMotorControl_Request__are_equal(const mower_description__srv__CuttingMotorControl_Request * lhs, const mower_description__srv__CuttingMotorControl_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // speed_level
  if (lhs->speed_level != rhs->speed_level) {
    return false;
  }
  return true;
}

bool
mower_description__srv__CuttingMotorControl_Request__copy(
  const mower_description__srv__CuttingMotorControl_Request * input,
  mower_description__srv__CuttingMotorControl_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // speed_level
  output->speed_level = input->speed_level;
  return true;
}

mower_description__srv__CuttingMotorControl_Request *
mower_description__srv__CuttingMotorControl_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mower_description__srv__CuttingMotorControl_Request * msg = (mower_description__srv__CuttingMotorControl_Request *)allocator.allocate(sizeof(mower_description__srv__CuttingMotorControl_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(mower_description__srv__CuttingMotorControl_Request));
  bool success = mower_description__srv__CuttingMotorControl_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
mower_description__srv__CuttingMotorControl_Request__destroy(mower_description__srv__CuttingMotorControl_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    mower_description__srv__CuttingMotorControl_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
mower_description__srv__CuttingMotorControl_Request__Sequence__init(mower_description__srv__CuttingMotorControl_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mower_description__srv__CuttingMotorControl_Request * data = NULL;

  if (size) {
    data = (mower_description__srv__CuttingMotorControl_Request *)allocator.zero_allocate(size, sizeof(mower_description__srv__CuttingMotorControl_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = mower_description__srv__CuttingMotorControl_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        mower_description__srv__CuttingMotorControl_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
mower_description__srv__CuttingMotorControl_Request__Sequence__fini(mower_description__srv__CuttingMotorControl_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      mower_description__srv__CuttingMotorControl_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

mower_description__srv__CuttingMotorControl_Request__Sequence *
mower_description__srv__CuttingMotorControl_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mower_description__srv__CuttingMotorControl_Request__Sequence * array = (mower_description__srv__CuttingMotorControl_Request__Sequence *)allocator.allocate(sizeof(mower_description__srv__CuttingMotorControl_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = mower_description__srv__CuttingMotorControl_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
mower_description__srv__CuttingMotorControl_Request__Sequence__destroy(mower_description__srv__CuttingMotorControl_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    mower_description__srv__CuttingMotorControl_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
mower_description__srv__CuttingMotorControl_Request__Sequence__are_equal(const mower_description__srv__CuttingMotorControl_Request__Sequence * lhs, const mower_description__srv__CuttingMotorControl_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!mower_description__srv__CuttingMotorControl_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
mower_description__srv__CuttingMotorControl_Request__Sequence__copy(
  const mower_description__srv__CuttingMotorControl_Request__Sequence * input,
  mower_description__srv__CuttingMotorControl_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(mower_description__srv__CuttingMotorControl_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    mower_description__srv__CuttingMotorControl_Request * data =
      (mower_description__srv__CuttingMotorControl_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!mower_description__srv__CuttingMotorControl_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          mower_description__srv__CuttingMotorControl_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!mower_description__srv__CuttingMotorControl_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `message`
#include "rosidl_runtime_c/string_functions.h"

bool
mower_description__srv__CuttingMotorControl_Response__init(mower_description__srv__CuttingMotorControl_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  // message
  if (!rosidl_runtime_c__String__init(&msg->message)) {
    mower_description__srv__CuttingMotorControl_Response__fini(msg);
    return false;
  }
  // actual_speed
  return true;
}

void
mower_description__srv__CuttingMotorControl_Response__fini(mower_description__srv__CuttingMotorControl_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
  // message
  rosidl_runtime_c__String__fini(&msg->message);
  // actual_speed
}

bool
mower_description__srv__CuttingMotorControl_Response__are_equal(const mower_description__srv__CuttingMotorControl_Response * lhs, const mower_description__srv__CuttingMotorControl_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->message), &(rhs->message)))
  {
    return false;
  }
  // actual_speed
  if (lhs->actual_speed != rhs->actual_speed) {
    return false;
  }
  return true;
}

bool
mower_description__srv__CuttingMotorControl_Response__copy(
  const mower_description__srv__CuttingMotorControl_Response * input,
  mower_description__srv__CuttingMotorControl_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  // message
  if (!rosidl_runtime_c__String__copy(
      &(input->message), &(output->message)))
  {
    return false;
  }
  // actual_speed
  output->actual_speed = input->actual_speed;
  return true;
}

mower_description__srv__CuttingMotorControl_Response *
mower_description__srv__CuttingMotorControl_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mower_description__srv__CuttingMotorControl_Response * msg = (mower_description__srv__CuttingMotorControl_Response *)allocator.allocate(sizeof(mower_description__srv__CuttingMotorControl_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(mower_description__srv__CuttingMotorControl_Response));
  bool success = mower_description__srv__CuttingMotorControl_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
mower_description__srv__CuttingMotorControl_Response__destroy(mower_description__srv__CuttingMotorControl_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    mower_description__srv__CuttingMotorControl_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
mower_description__srv__CuttingMotorControl_Response__Sequence__init(mower_description__srv__CuttingMotorControl_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mower_description__srv__CuttingMotorControl_Response * data = NULL;

  if (size) {
    data = (mower_description__srv__CuttingMotorControl_Response *)allocator.zero_allocate(size, sizeof(mower_description__srv__CuttingMotorControl_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = mower_description__srv__CuttingMotorControl_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        mower_description__srv__CuttingMotorControl_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
mower_description__srv__CuttingMotorControl_Response__Sequence__fini(mower_description__srv__CuttingMotorControl_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      mower_description__srv__CuttingMotorControl_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

mower_description__srv__CuttingMotorControl_Response__Sequence *
mower_description__srv__CuttingMotorControl_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mower_description__srv__CuttingMotorControl_Response__Sequence * array = (mower_description__srv__CuttingMotorControl_Response__Sequence *)allocator.allocate(sizeof(mower_description__srv__CuttingMotorControl_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = mower_description__srv__CuttingMotorControl_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
mower_description__srv__CuttingMotorControl_Response__Sequence__destroy(mower_description__srv__CuttingMotorControl_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    mower_description__srv__CuttingMotorControl_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
mower_description__srv__CuttingMotorControl_Response__Sequence__are_equal(const mower_description__srv__CuttingMotorControl_Response__Sequence * lhs, const mower_description__srv__CuttingMotorControl_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!mower_description__srv__CuttingMotorControl_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
mower_description__srv__CuttingMotorControl_Response__Sequence__copy(
  const mower_description__srv__CuttingMotorControl_Response__Sequence * input,
  mower_description__srv__CuttingMotorControl_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(mower_description__srv__CuttingMotorControl_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    mower_description__srv__CuttingMotorControl_Response * data =
      (mower_description__srv__CuttingMotorControl_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!mower_description__srv__CuttingMotorControl_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          mower_description__srv__CuttingMotorControl_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!mower_description__srv__CuttingMotorControl_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
