# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: encoder.pyc (Python 3.11)

'''Code for encoding protocol message primitives.

Contains the logic for encoding every logical protocol field type
into one of the 5 physical wire types.

This code is designed to push the Python interpreter\'s performance to the
limits.

The basic idea is that at startup time, for every field (i.e. every
FieldDescriptor) we construct two functions:  a "sizer" and an "encoder".  The
sizer takes a value of this field\'s type and computes its byte size.  The
encoder takes a writer function and a value.  It encodes the value into byte
strings and invokes the writer function to write those strings.  Typically the
writer function is the write() method of a BytesIO.

We try to do as much work as possible when constructing the writer and the
sizer rather than when calling them.  In particular:
* We copy any needed global functions to local variables, so that we do not need
  to do costly global table lookups at runtime.
* Similarly, we try to do any attribute lookups at startup time if possible.
* Every field\'s tag is encoded to bytes at startup, since it can\'t change at
  runtime.
* Whatever component of the field size we can compute at startup, we do.
* We *avoid* sharing code if doing so would make the code slower and not sharing
  does not burden us too much.  For example, encoders for repeated fields do
  not just call the encoders for singular fields in a loop because this would
  add an extra function call overhead for every loop iteration; instead, we
  manually inline the single-value encoder into the loop.
* If a Python function lacks a return statement, Python actually generates
  instructions to pop the result of the last statement off the stack, push
  None onto the stack, and then return that.  If we really don\'t care what
  value is returned, then we can save two instructions by returning the
  result of the last statement.  It looks funny but it helps.
* We assume that type and bounds checking has happened at a higher level.
'''
__author__ = 'kenton@google.com (Kenton Varda)'
import struct
from google.protobuf.internal import wire_format
_POS_INF = float('inf')
_NEG_INF = -_POS_INF

def _VarintSize(value):
    '''Compute the size of a varint value.'''
    if value <= 127:
        return 1
    if None <= 16383:
        return 2
    if None <= 2097151:
        return 3
    if None <= 268435455:
        return 4
    if None <= 0x7FFFFFFFF:
        return 5
    if None <= 0x3FFFFFFFFFF:
        return 6
    if None <= 0x1FFFFFFFFFFFF:
        return 7
    if None <= 0xFFFFFFFFFFFFFF:
        return 8
    if None <= 0x7FFFFFFFFFFFFFFF:
        return 9


def _SignedVarintSize(value):
    '''Compute the size of a signed varint value.'''
    if value < 0:
        return 10
    if None <= 127:
        return 1
    if None <= 16383:
        return 2
    if None <= 2097151:
        return 3
    if None <= 268435455:
        return 4
    if None <= 0x7FFFFFFFF:
        return 5
    if None <= 0x3FFFFFFFFFF:
        return 6
    if None <= 0x1FFFFFFFFFFFF:
        return 7
    if None <= 0xFFFFFFFFFFFFFF:
        return 8
    if None <= 0x7FFFFFFFFFFFFFFF:
        return 9


def _TagSize(field_number):
    '''Returns the number of bytes required to serialize a tag with this field
  number.'''
    return _VarintSize(wire_format.PackTag(field_number, 0))


def _SimpleSizer(compute_value_size):
    '''A sizer which uses the function compute_value_size to compute the size of
  each value.  Typically compute_value_size is _VarintSize.'''
    pass
# WARNING: Decompyle incomplete


def _ModifiedSizer(compute_value_size, modify_value):
    '''Like SimpleSizer, but modify_value is invoked on each value before it is
  passed to compute_value_size.  modify_value is typically ZigZagEncode.'''
    pass
# WARNING: Decompyle incomplete


def _FixedSizer(value_size):
    '''Like _SimpleSizer except for a fixed-size field.  The input is the size
  of one value.'''
    pass
# WARNING: Decompyle incomplete

Int32Sizer = _SimpleSizer(_SignedVarintSize)
Int64Sizer = _SimpleSizer(_SignedVarintSize)
EnumSizer = _SimpleSizer(_SignedVarintSize)
UInt32Sizer = _SimpleSizer(_VarintSize)
UInt64Sizer = _SimpleSizer(_VarintSize)
SInt32Sizer = _ModifiedSizer(_SignedVarintSize, wire_format.ZigZagEncode)
SInt64Sizer = _ModifiedSizer(_SignedVarintSize, wire_format.ZigZagEncode)
Fixed32Sizer = _FixedSizer(4)
SFixed32Sizer = _FixedSizer(4)
FloatSizer = _FixedSizer(4)
Fixed64Sizer = _FixedSizer(8)
SFixed64Sizer = _FixedSizer(8)
DoubleSizer = _FixedSizer(8)
BoolSizer = _FixedSizer(1)

def StringSizer(field_number, is_repeated, is_packed):
    '''Returns a sizer for a string field.'''
    pass
# WARNING: Decompyle incomplete


def BytesSizer(field_number, is_repeated, is_packed):
    '''Returns a sizer for a bytes field.'''
    pass
# WARNING: Decompyle incomplete


def GroupSizer(field_number, is_repeated, is_packed):
    '''Returns a sizer for a group field.'''
    pass
# WARNING: Decompyle incomplete


def MessageSizer(field_number, is_repeated, is_packed):
    '''Returns a sizer for a message field.'''
    pass
# WARNING: Decompyle incomplete


def MessageSetItemSizer(field_number):
    '''Returns a sizer for extensions of MessageSet.

  The message set message looks like this:
    message MessageSet {
      repeated group Item = 1 {
        required int32 type_id = 2;
        required string message = 3;
      }
    }
  '''
    pass
# WARNING: Decompyle incomplete


def MapSizer(field_descriptor, is_message_map):
    '''Returns a sizer for a map field.'''
    pass
# WARNING: Decompyle incomplete


def _VarintEncoder():
    '''Return an encoder for a basic varint value (does not include tag).'''
    pass
# WARNING: Decompyle incomplete


def _SignedVarintEncoder():
    '''Return an encoder for a basic signed varint value (does not include
  tag).'''
    pass
# WARNING: Decompyle incomplete

_EncodeVarint = _VarintEncoder()
_EncodeSignedVarint = _SignedVarintEncoder()

def _VarintBytes(value):
    """Encode the given integer as a varint and return the bytes.  This is only
  called at startup time so it doesn't need to be fast."""
    pieces = []
    _EncodeVarint(pieces.append, value, True)
    return b''.join(pieces)


def TagBytes(field_number, wire_type):
    '''Encode the given tag and return the bytes.  Only called at startup.'''
    return bytes(_VarintBytes(wire_format.PackTag(field_number, wire_type)))


def _SimpleEncoder(wire_type, encode_value, compute_value_size):
    """Return a constructor for an encoder for fields of a particular type.

  Args:
      wire_type:  The field's wire type, for encoding tags.
      encode_value:  A function which encodes an individual value, e.g.
        _EncodeVarint().
      compute_value_size:  A function which computes the size of an individual
        value, e.g. _VarintSize().
  """
    pass
# WARNING: Decompyle incomplete


def _ModifiedEncoder(wire_type, encode_value, compute_value_size, modify_value):
    '''Like SimpleEncoder but additionally invokes modify_value on every value
  before passing it to encode_value.  Usually modify_value is ZigZagEncode.'''
    pass
# WARNING: Decompyle incomplete


def _StructPackEncoder(wire_type, format):
    """Return a constructor for an encoder for a fixed-width field.

  Args:
      wire_type:  The field's wire type, for encoding tags.
      format:  The format string to pass to struct.pack().
  """
    pass
# WARNING: Decompyle incomplete


def _FloatingPointEncoder(wire_type, format):
    """Return a constructor for an encoder for float fields.

  This is like StructPackEncoder, but catches errors that may be due to
  passing non-finite floating-point values to struct.pack, and makes a
  second attempt to encode those values.

  Args:
      wire_type:  The field's wire type, for encoding tags.
      format:  The format string to pass to struct.pack().
  """
    pass
# WARNING: Decompyle incomplete

Int32Encoder = _SimpleEncoder(wire_format.WIRETYPE_VARINT, _EncodeSignedVarint, _SignedVarintSize)
Int64Encoder = _SimpleEncoder(wire_format.WIRETYPE_VARINT, _EncodeSignedVarint, _SignedVarintSize)
EnumEncoder = _SimpleEncoder(wire_format.WIRETYPE_VARINT, _EncodeSignedVarint, _SignedVarintSize)
UInt32Encoder = _SimpleEncoder(wire_format.WIRETYPE_VARINT, _EncodeVarint, _VarintSize)
UInt64Encoder = _SimpleEncoder(wire_format.WIRETYPE_VARINT, _EncodeVarint, _VarintSize)
SInt32Encoder = _ModifiedEncoder(wire_format.WIRETYPE_VARINT, _EncodeVarint, _VarintSize, wire_format.ZigZagEncode)
SInt64Encoder = _ModifiedEncoder(wire_format.WIRETYPE_VARINT, _EncodeVarint, _VarintSize, wire_format.ZigZagEncode)
Fixed32Encoder = _StructPackEncoder(wire_format.WIRETYPE_FIXED32, '<I')
Fixed64Encoder = _StructPackEncoder(wire_format.WIRETYPE_FIXED64, '<Q')
SFixed32Encoder = _StructPackEncoder(wire_format.WIRETYPE_FIXED32, '<i')
SFixed64Encoder = _StructPackEncoder(wire_format.WIRETYPE_FIXED64, '<q')
FloatEncoder = _FloatingPointEncoder(wire_format.WIRETYPE_FIXED32, '<f')
DoubleEncoder = _FloatingPointEncoder(wire_format.WIRETYPE_FIXED64, '<d')

def BoolEncoder(field_number, is_repeated, is_packed):
    '''Returns an encoder for a boolean field.'''
    pass
# WARNING: Decompyle incomplete


def StringEncoder(field_number, is_repeated, is_packed):
    '''Returns an encoder for a string field.'''
    pass
# WARNING: Decompyle incomplete


def BytesEncoder(field_number, is_repeated, is_packed):
    '''Returns an encoder for a bytes field.'''
    pass
# WARNING: Decompyle incomplete


def GroupEncoder(field_number, is_repeated, is_packed):
    '''Returns an encoder for a group field.'''
    pass
# WARNING: Decompyle incomplete


def MessageEncoder(field_number, is_repeated, is_packed):
    '''Returns an encoder for a message field.'''
    pass
# WARNING: Decompyle incomplete


def MessageSetItemEncoder(field_number):
    '''Encoder for extensions of MessageSet.

  The message set message looks like this:
    message MessageSet {
      repeated group Item = 1 {
        required int32 type_id = 2;
        required string message = 3;
      }
    }
  '''
    pass
# WARNING: Decompyle incomplete


def MapEncoder(field_descriptor):
    '''Encoder for extensions of MessageSet.

  Maps always have a wire format like this:
    message MapEntry {
      key_type key = 1;
      value_type value = 2;
    }
    repeated MapEntry map = N;
  '''
    pass
# WARNING: Decompyle incomplete
