# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: packer.pyc (Python 3.11)

'''Provide pre-compiled struct packers for encoding and decoding.

See: https://docs.python.org/2/library/struct.html#format-characters
'''
import struct
from  import compat
boolean = struct.Struct(compat.struct_bool_decl)
uint8 = struct.Struct('<B')
uint16 = struct.Struct('<H')
uint32 = struct.Struct('<I')
uint64 = struct.Struct('<Q')
int8 = struct.Struct('<b')
int16 = struct.Struct('<h')
int32 = struct.Struct('<i')
int64 = struct.Struct('<q')
float32 = struct.Struct('<f')
float64 = struct.Struct('<d')
uoffset = uint32
soffset = int32
voffset = uint16
