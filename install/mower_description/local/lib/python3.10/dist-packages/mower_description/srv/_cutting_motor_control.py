# generated from rosidl_generator_py/resource/_idl.py.em
# with input from mower_description:srv/CuttingMotorControl.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CuttingMotorControl_Request(type):
    """Metaclass of message 'CuttingMotorControl_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('mower_description')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mower_description.srv.CuttingMotorControl_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__cutting_motor_control__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__cutting_motor_control__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__cutting_motor_control__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__cutting_motor_control__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__cutting_motor_control__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CuttingMotorControl_Request(metaclass=Metaclass_CuttingMotorControl_Request):
    """Message class 'CuttingMotorControl_Request'."""

    __slots__ = [
        '_speed_level',
    ]

    _fields_and_field_types = {
        'speed_level': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.speed_level = kwargs.get('speed_level', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.speed_level != other.speed_level:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def speed_level(self):
        """Message field 'speed_level'."""
        return self._speed_level

    @speed_level.setter
    def speed_level(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'speed_level' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'speed_level' field must be an integer in [-2147483648, 2147483647]"
        self._speed_level = value


# Import statements for member types

# already imported above
# import builtins

import math  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_CuttingMotorControl_Response(type):
    """Metaclass of message 'CuttingMotorControl_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('mower_description')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mower_description.srv.CuttingMotorControl_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__cutting_motor_control__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__cutting_motor_control__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__cutting_motor_control__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__cutting_motor_control__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__cutting_motor_control__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CuttingMotorControl_Response(metaclass=Metaclass_CuttingMotorControl_Response):
    """Message class 'CuttingMotorControl_Response'."""

    __slots__ = [
        '_success',
        '_message',
        '_actual_speed',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'message': 'string',
        'actual_speed': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.message = kwargs.get('message', str())
        self.actual_speed = kwargs.get('actual_speed', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.success != other.success:
            return False
        if self.message != other.message:
            return False
        if self.actual_speed != other.actual_speed:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @builtins.property
    def message(self):
        """Message field 'message'."""
        return self._message

    @message.setter
    def message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'message' field must be of type 'str'"
        self._message = value

    @builtins.property
    def actual_speed(self):
        """Message field 'actual_speed'."""
        return self._actual_speed

    @actual_speed.setter
    def actual_speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'actual_speed' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'actual_speed' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._actual_speed = value


class Metaclass_CuttingMotorControl(type):
    """Metaclass of service 'CuttingMotorControl'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('mower_description')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mower_description.srv.CuttingMotorControl')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__cutting_motor_control

            from mower_description.srv import _cutting_motor_control
            if _cutting_motor_control.Metaclass_CuttingMotorControl_Request._TYPE_SUPPORT is None:
                _cutting_motor_control.Metaclass_CuttingMotorControl_Request.__import_type_support__()
            if _cutting_motor_control.Metaclass_CuttingMotorControl_Response._TYPE_SUPPORT is None:
                _cutting_motor_control.Metaclass_CuttingMotorControl_Response.__import_type_support__()


class CuttingMotorControl(metaclass=Metaclass_CuttingMotorControl):
    from mower_description.srv._cutting_motor_control import CuttingMotorControl_Request as Request
    from mower_description.srv._cutting_motor_control import CuttingMotorControl_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
