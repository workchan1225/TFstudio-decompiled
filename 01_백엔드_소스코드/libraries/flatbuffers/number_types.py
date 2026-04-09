# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: number_types.pyc (Python 3.11)

import collections
import struct
from  import packer
from compat import NumpyRequiredForThisFeature, import_numpy
np = import_numpy()

class BoolFlags(object):
    bytewidth = 1
    min_val = False
    max_val = True
    py_type = bool
    name = 'bool'
    packer_type = packer.boolean


class Uint8Flags(object):
    bytewidth = 1
    min_val = 0
    max_val = 255
    py_type = int
    name = 'uint8'
    packer_type = packer.uint8


class Uint16Flags(object):
    bytewidth = 2
    min_val = 0
    max_val = 65535
    py_type = int
    name = 'uint16'
    packer_type = packer.uint16


class Uint32Flags(object):
    bytewidth = 4
    min_val = 0
    max_val = 0xFFFFFFFF
    py_type = int
    name = 'uint32'
    packer_type = packer.uint32


class Uint64Flags(object):
    bytewidth = 8
    min_val = 0
    max_val = 0xFFFFFFFFFFFFFFFF
    py_type = int
    name = 'uint64'
    packer_type = packer.uint64


class Int8Flags(object):
    bytewidth = 1
    min_val = -128
    max_val = 127
    py_type = int
    name = 'int8'
    packer_type = packer.int8


class Int16Flags(object):
    bytewidth = 2
    min_val = -32768
    max_val = 32767
    py_type = int
    name = 'int16'
    packer_type = packer.int16


class Int32Flags(object):
    bytewidth = 4
    min_val = -2147483648
    max_val = 2147483647
    py_type = int
    name = 'int32'
    packer_type = packer.int32


class Int64Flags(object):
    bytewidth = 8
    min_val = -0x8000000000000000
    max_val = 0x7FFFFFFFFFFFFFFF
    py_type = int
    name = 'int64'
    packer_type = packer.int64


class Float32Flags(object):
    bytewidth = 4
    min_val = None
    max_val = None
    py_type = float
    name = 'float32'
    packer_type = packer.float32


class Float64Flags(object):
    bytewidth = 8
    min_val = None
    max_val = None
    py_type = float
    name = 'float64'
    packer_type = packer.float64


class SOffsetTFlags(Int32Flags):
    pass


class UOffsetTFlags(Uint32Flags):
    pass


class VOffsetTFlags(Uint16Flags):
    pass


def valid_number(n, flags):
    pass
# WARNING: Decompyle incomplete


def enforce_number(n, flags):
    pass
# WARNING: Decompyle incomplete


def float32_to_uint32(n):
    packed = struct.pack('<1f', n)
    (converted,) = struct.unpack('<1L', packed)
    return converted


def uint32_to_float32(n):
    packed = struct.pack('<1L', n)
    (unpacked,) = struct.unpack('<1f', packed)
    return unpacked


def float64_to_uint64(n):
    packed = struct.pack('<1d', n)
    (converted,) = struct.unpack('<1Q', packed)
    return converted


def uint64_to_float64(n):
    packed = struct.pack('<1Q', n)
    (unpacked,) = struct.unpack('<1d', packed)
    return unpacked


def to_numpy_type(number_type):
    pass
# WARNING: Decompyle incomplete
