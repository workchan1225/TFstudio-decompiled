# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ctypes_utils.pyc (Python 3.11)

'''
Support for typing ctypes function pointers.
'''
import ctypes
import sys
from numba.core import types, config
from numba.core.typing import templates
from typeof import typeof_impl
if config.USE_LEGACY_TYPE_SYSTEM:
    _FROM_CTYPES = {
        ctypes.py_object: types.ffi_forced_object,
        ctypes.c_void_p: types.voidptr,
        ctypes.c_double: types.float64,
        ctypes.c_float: types.float32,
        ctypes.c_uint64: types.uint64,
        ctypes.c_uint32: types.uint32,
        ctypes.c_uint16: types.uint16,
        ctypes.c_uint8: types.uint8,
        ctypes.c_int64: types.int64,
        ctypes.c_int32: types.int32,
        ctypes.c_int16: types.int16,
        ctypes.c_int8: types.int8,
        ctypes.c_bool: types.boolean }
else:
    _FROM_CTYPES = {
        ctypes.py_object: types.ffi_forced_object,
        ctypes.c_void_p: types.voidptr,
        ctypes.c_double: types.c_float64,
        ctypes.c_float: types.c_float32,
        ctypes.c_uint64: types.c_uint64,
        ctypes.c_uint32: types.c_uint32,
        ctypes.c_uint16: types.c_uint16,
        ctypes.c_uint8: types.c_uint8,
        ctypes.c_int64: types.c_int64,
        ctypes.c_int32: types.c_int32,
        ctypes.c_int16: types.c_int16,
        ctypes.c_int8: types.c_int8,
        ctypes.c_bool: types.c_bool }
_TO_CTYPES = _FROM_CTYPES.items()()

def from_ctypes(ctypeobj):
    '''
    Convert the given ctypes type to a Numba type.
    '''
    pass
# WARNING: Decompyle incomplete


def to_ctypes(ty):
    '''
    Convert the given Numba type to a ctypes type.
    '''
    pass
# WARNING: Decompyle incomplete


def is_ctypes_funcptr(obj):
    
    try:
        ctypes.cast(obj, ctypes.c_void_p)
        if hasattr(obj, 'argtypes'):
            return hasattr(obj, 'restype')
        except ctypes.ArgumentError:
            return False



def get_pointer(ctypes_func):
    '''
    Get a pointer to the underlying function for a ctypes function as an
    integer.
    '''
    return ctypes.cast(ctypes_func, ctypes.c_void_p).value


def make_function_type(cfnptr):
    '''
    Return a Numba type for the given ctypes function pointer.
    '''
    pass
# WARNING: Decompyle incomplete
