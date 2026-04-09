# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cffi_utils.pyc (Python 3.11)

'''
Support for CFFI. Allows checking whether objects are CFFI functions and
obtaining the pointer and numba signature.
'''
from types import BuiltinFunctionType
import ctypes
from functools import partial
import numpy as np
from numba.core import types
from numba.core.errors import TypingError
from numba.core.typing import templates
from numba.np import numpy_support

try:
    import cffi
    ffi = cffi.FFI()
except ImportError:
    ffi = None

SUPPORTED = ffi is not None
_ool_func_types = { }
_ool_func_ptr = { }
_ffi_instances = set()

def is_ffi_instance(obj):
    
    try:
        if not obj in _ffi_instances:
            pass
        return isinstance(obj, cffi.FFI)
    except TypeError:
        return False



def is_cffi_func(obj):
    '''Check whether the obj is a CFFI function'''
    
    try:
        return ffi.typeof(obj).kind == 'function'
    except TypeError:
        return 
        None, obj in _ool_func_types
        return False



def get_pointer(cffi_func):
    '''
    Get a pointer to the underlying function for a CFFI function as an
    integer.
    '''
    if cffi_func in _ool_func_ptr:
        return _ool_func_ptr[cffi_func]
    return None(ffi.cast('uintptr_t', cffi_func))

_cached_type_map = None

def _type_map():
    '''
    Lazily compute type map, as calling ffi.typeof() involves costly
    parsing of C code...
    '''
    pass
# WARNING: Decompyle incomplete


def map_type(cffi_type, use_record_dtype = (False,)):
    '''
    Map CFFI type to numba type.

    Parameters
    ----------
    cffi_type:
        The CFFI type to be converted.
    use_record_dtype: bool (default: False)
        When True, struct types are mapped to a NumPy Record dtype.

    '''
    pass
# WARNING: Decompyle incomplete


def map_struct_to_record_dtype(cffi_type):
    '''Convert a cffi type into a NumPy Record dtype
    '''
    fields = {
        'names': [],
        'formats': [],
        'offsets': [],
        'itemsize': ffi.sizeof(cffi_type) }
    is_aligned = True
    for k, v in cffi_type.fields:
        if v.bitshift != -1:
            msg = 'field {!r} has bitshift, this is not supported'
            raise ValueError(msg.format(k))
        if v.flags != 0:
            msg = 'field {!r} has flags, this is not supported'
            raise ValueError(msg.format(k))
        if v.bitsize != -1:
            msg = 'field {!r} has bitsize, this is not supported'
            raise ValueError(msg.format(k))
        dtype = numpy_support.as_dtype(map_type(v.type, use_record_dtype = True))
        fields['names'].append(k)
        fields['formats'].append(dtype)
        fields['offsets'].append(v.offset)
        is_aligned &= (v.offset % dtype.alignment == 0)
        return numpy_support.from_dtype(np.dtype(fields, align = is_aligned))


def make_function_type(cffi_func, use_record_dtype = (False,)):
