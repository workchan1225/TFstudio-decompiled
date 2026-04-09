# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sharedctypes.pyc (Python 3.11)

import ctypes
import weakref
from  import heap
from  import get_context
from context import reduction, assert_spawning
_ForkingPickler = reduction.ForkingPickler
__all__ = [
    'RawValue',
    'RawArray',
    'Value',
    'Array',
    'copy',
    'synchronized']
typecode_to_type = {
    'c': ctypes.c_char,
    'u': ctypes.c_wchar,
    'b': ctypes.c_byte,
    'B': ctypes.c_ubyte,
    'h': ctypes.c_short,
    'H': ctypes.c_ushort,
    'i': ctypes.c_int,
    'I': ctypes.c_uint,
    'l': ctypes.c_long,
    'L': ctypes.c_ulong,
    'q': ctypes.c_longlong,
    'Q': ctypes.c_ulonglong,
    'f': ctypes.c_float,
    'd': ctypes.c_double }

def _new_value(type_):
    size = ctypes.sizeof(type_)
    wrapper = heap.BufferWrapper(size)
    return rebuild_ctype(type_, wrapper, None)


def RawValue(typecode_or_type, *args):
    '''
    Returns a ctypes object allocated from shared memory
    '''
    type_ = typecode_to_type.get(typecode_or_type, typecode_or_type)
    obj = _new_value(type_)
    ctypes.memset(ctypes.addressof(obj), 0, ctypes.sizeof(obj))
# WARNING: Decompyle incomplete


def RawArray(typecode_or_type, size_or_initializer):
    '''
    Returns a ctypes array allocated from shared memory
    '''
    type_ = typecode_to_type.get(typecode_or_type, typecode_or_type)
    if isinstance(size_or_initializer, int):
        type_ = type_ * size_or_initializer
        obj = _new_value(type_)
        ctypes.memset(ctypes.addressof(obj), 0, ctypes.sizeof(obj))
        return obj
    type_ = None * len(size_or_initializer)
    result = _new_value(type_)
# WARNING: Decompyle incomplete


def Value(typecode_or_type = None, *, lock, ctx, *args):
    '''
    Return a synchronization wrapper for a Value
    '''
    pass
# WARNING: Decompyle incomplete


def Array(typecode_or_type = None, size_or_initializer = {
    'lock': True,
    'ctx': None }, *, lock, ctx):
