# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bufproto.pyc (Python 3.11)

'''
Typing support for the buffer protocol (PEP 3118).
'''
import array
from numba.core import types, config
from numba.core.errors import NumbaValueError
_pep3118_int_types = set('bBhHiIlLqQnN')
if config.USE_LEGACY_TYPE_SYSTEM:
    _pep3118_scalar_map = {
        'f': types.float32,
        'd': types.float64,
        'Zf': types.complex64,
        'Zd': types.complex128 }
else:
    _pep3118_scalar_map = {
        'd': types.py_float,
        'Zd': types.py_complex }
_type_map = {
    array.array: types.PyArray,
    bytearray: types.ByteArray }
_type_map[memoryview] = types.MemoryView
_type_map[bytes] = types.Bytes

def decode_pep3118_format(fmt, itemsize):
    '''
    Return the Numba type for an item with format string *fmt* and size
    *itemsize* (in bytes).
    '''
    if fmt in _pep3118_int_types:
        name = 'int%d' % (itemsize * 8,)
        if fmt.isupper():
            name = 'u' + name
        return types.Integer(name)
    
    try:
        return _pep3118_scalar_map[fmt.lstrip('=')]
    except KeyError:
        raise NumbaValueError(f'''unsupported PEP 3118 format {fmt!r}''')



def get_type_class(typ):
    '''
    Get the Numba type class for buffer-compatible Python *typ*.
    '''
    
    try:
        return _type_map[typ]
    except KeyError:
        return 



def infer_layout(val):
    '''
    Infer layout of the given memoryview *val*.
    '''
    if val.c_contiguous:
        pass
    elif val.f_contiguous:
        pass
    
    return 'A'
