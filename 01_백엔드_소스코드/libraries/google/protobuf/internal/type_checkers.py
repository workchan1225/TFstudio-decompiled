# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: type_checkers.pyc (Python 3.11)

__doc__ = 'Provides type checking routines.\n\nThis module defines type checking utilities in the forms of dictionaries:\n\nVALUE_CHECKERS: A dictionary of field types and a value validation object.\nTYPE_TO_BYTE_SIZE_FN: A dictionary with field types and a size computing\n  function.\nTYPE_TO_SERIALIZE_METHOD: A dictionary with field types and serialization\n  function.\nFIELD_TYPE_TO_WIRE_TYPE: A dictionary with field typed and their\n  corresponding wire types.\nTYPE_TO_DESERIALIZE_METHOD: A dictionary with field types and deserialization\n  function.\n'
__author__ = 'robinson@google.com (Will Robinson)'
import ctypes
import numbers
from google.protobuf.internal import decoder
from google.protobuf.internal import encoder
from google.protobuf.internal import wire_format
from google.protobuf import descriptor
_FieldDescriptor = descriptor.FieldDescriptor

def TruncateToFourByteFloat(original):
    return ctypes.c_float(original).value


def ToShortestFloat(original):
    '''Returns the shortest float that has same value in wire.'''
    precision = 6
    rounded = float('{0:.{1}g}'.format(original, precision))
# WARNING: Decompyle incomplete


def GetTypeChecker(field):
    '''Returns a type checker for a message field of the specified types.

  Args:
    field: FieldDescriptor object for this field.

  Returns:
    An instance of TypeChecker which can be used to verify the types
    of values assigned to a field of the specified type.
  '''
    if field.cpp_type == _FieldDescriptor.CPPTYPE_STRING and field.type == _FieldDescriptor.TYPE_STRING:
        return UnicodeValueChecker()
    if None.cpp_type == _FieldDescriptor.CPPTYPE_ENUM:
        if field.enum_type.is_closed:
            return EnumValueChecker(field.enum_type)
        return None[_FieldDescriptor.CPPTYPE_INT32]
    return None[field.cpp_type]


class TypeChecker(object):
    '''Type checker used to catch type errors as early as possible
  when the client is setting scalar fields in protocol messages.
  '''
    
    def __init__(self, *acceptable_types):
        self._acceptable_types = acceptable_types

    
    def CheckValue(self, proposed_value):
        '''Type check the provided value and return it.

    The returned value might have been normalized to another type.
    '''
        if not isinstance(proposed_value, self._acceptable_types):
            message = '%.1024r has type %s, but expected one of: %s' % (proposed_value, type(proposed_value), self._acceptable_types)
            raise TypeError(message)
        return proposed_value



class TypeCheckerWithDefault(TypeChecker):
    
    def __init__(self, default_value, *acceptable_types):
        pass
    # WARNING: Decompyle incomplete

    
    def DefaultValue(self):
        return self._default_value



class BoolValueChecker(object):
    '''Type checker used for bool fields.'''
    
    def CheckValue(self, proposed_value):
        if (hasattr(proposed_value, '__index__') or type(proposed_value).__module__ == 'numpy') and type(proposed_value).__name__ == 'ndarray':
            message = '%.1024r has type %s, but expected one of: %s' % (proposed_value, type(proposed_value), (bool, int))
            raise TypeError(message)
        return bool(proposed_value)

    
    def DefaultValue(self):
        return False



class IntValueChecker(object):
    '''Checker used for integer fields.  Performs type-check and range check.'''
    
    def CheckValue(self, proposed_value):
        if (hasattr(proposed_value, '__index__') or type(proposed_value).__module__ == 'numpy') and type(proposed_value).__name__ == 'ndarray':
            message = '%.1024r has type %s, but expected one of: %s' % (proposed_value, type(proposed_value), (int,))
            raise TypeError(message)
        if not  <= self._MIN, int(proposed_value) or self._MIN, int(proposed_value) <= self._MAX:
            pass
        
        raise ValueError('Value out of range: %d' % proposed_value)
        return proposed_value

    
    def DefaultValue(self):
        return 0



class EnumValueChecker(object):
    '''Checker used for enum fields.  Performs type-check and range check.'''
    
    def __init__(self, enum_type):
        self._enum_type = enum_type

    
    def CheckValue(self, proposed_value):
        if not isinstance(proposed_value, numbers.Integral):
            message = '%.1024r has type %s, but expected one of: %s' % (proposed_value, type(proposed_value), (int,))
            raise TypeError(message)
        if int(proposed_value) not in self._enum_type.values_by_number:
            raise ValueError('Unknown enum value: %d' % proposed_value)
        return proposed_value

    
    def DefaultValue(self):
        return self._enum_type.values[0].number



class UnicodeValueChecker(object):
    '''Checker used for string fields.

  Always returns a unicode value, even if the input is of type str.
  '''
    
    def CheckValue(self, proposed_value):
        if not isinstance(proposed_value, (bytes, str)):
            message = '%.1024r has type %s, but expected one of: %s' % (proposed_value, type(proposed_value), (bytes, str))
            raise TypeError(message)
        if isinstance(proposed_value, bytes):
            
            try:
                proposed_value = proposed_value.decode('utf-8')
            except UnicodeDecodeError:
                raise ValueError("%.1024r has type bytes, but isn't valid UTF-8 encoding. Non-UTF-8 strings must be converted to unicode objects before being added." % proposed_value)
                
                try:
                    proposed_value.encode('utf8')
                except UnicodeEncodeError:
                    raise ValueError("%.1024r isn't a valid unicode string and can't be encoded in UTF-8." % proposed_value)

                return proposed_value


    
    def DefaultValue(self):
        return ''



class Int32ValueChecker(IntValueChecker):
    _MIN = -2147483648
    _MAX = 2147483647


class Uint32ValueChecker(IntValueChecker):
    _MIN = 0
    _MAX = 0xFFFFFFFF


class Int64ValueChecker(IntValueChecker):
    _MIN = -0x8000000000000000
    _MAX = 0x7FFFFFFFFFFFFFFF


class Uint64ValueChecker(IntValueChecker):
    _MIN = 0
    _MAX = 0xFFFFFFFFFFFFFFFF

_FLOAT_MAX = float.fromhex('0x1.fffffep+127')
_FLOAT_MIN = -_FLOAT_MAX
_INF = float('inf')
_NEG_INF = float('-inf')

class DoubleValueChecker(object):
    '''Checker used for double fields.

  Performs type-check and range check.
  '''
    
    def CheckValue(self, proposed_value):
        '''Check and convert proposed_value to float.'''
        if (hasattr(proposed_value, '__float__') or hasattr(proposed_value, '__index__') or type(proposed_value).__module__ == 'numpy') and type(proposed_value).__name__ == 'ndarray':
            message = '%.1024r has type %s, but expected one of: int, float' % (proposed_value, type(proposed_value))
            raise TypeError(message)
        return float(proposed_value)

    
    def DefaultValue(self):
        return 0



class FloatValueChecker(DoubleValueChecker):
    pass
# WARNING: Decompyle incomplete

_VALUE_CHECKERS = {
    _FieldDescriptor.CPPTYPE_STRING: TypeCheckerWithDefault(b'', bytes),
    _FieldDescriptor.CPPTYPE_BOOL: BoolValueChecker(),
    _FieldDescriptor.CPPTYPE_FLOAT: FloatValueChecker(),
    _FieldDescriptor.CPPTYPE_DOUBLE: DoubleValueChecker(),
    _FieldDescriptor.CPPTYPE_UINT64: Uint64ValueChecker(),
    _FieldDescriptor.CPPTYPE_UINT32: Uint32ValueChecker(),
    _FieldDescriptor.CPPTYPE_INT64: Int64ValueChecker(),
    _FieldDescriptor.CPPTYPE_INT32: Int32ValueChecker() }
# WARNING: Decompyle incomplete
