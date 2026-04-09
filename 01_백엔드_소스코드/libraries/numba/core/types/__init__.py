# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import struct
import numpy as np
from numba.core import utils
from abstract import *
from containers import *
from functions import *
from iterators import *
from misc import *
from npytypes import *
from scalars import *
from function_type import *
numpy_version = tuple(map(int, np.__version__.split('.')[:2]))
pyobject = PyObject('pyobject')
ffi_forced_object = Opaque('ffi_forced_object')
ffi = Opaque('ffi')
none = NoneType('none')
ellipsis = EllipsisType('...')
Any = Phantom('any')
undefined = Undefined('undefined')
py2_string_type = Opaque('str')
unicode_type = UnicodeType('unicode_type')
string = unicode_type
unknown = Dummy('unknown')
npy_rng = NumPyRandomGeneratorType('rng')
npy_bitgen = NumPyRandomBitGeneratorType('bitgen')
_undef_var = UndefVar('_undef_var')
code_type = Opaque('code')
pyfunc_type = Opaque('pyfunc')
voidptr = RawPointer('void*')
optional = Optional
deferred_type = DeferredType
slice2_type = SliceType('slice<a:b>', 2)
slice3_type = SliceType('slice<a:b:c>', 3)
void = none
if config.USE_LEGACY_TYPE_SYSTEM:
    boolean = Boolean('bool')
    bool_ = Boolean('bool')
    if numpy_version >= (2, 0):
        bool = bool_
    byte = Integer('uint8')
    uint8 = Integer('uint8')
    uint16 = Integer('uint16')
    uint32 = Integer('uint32')
    uint64 = Integer('uint64')
    int8 = Integer('int8')
    int16 = Integer('int16')
    int32 = Integer('int32')
    int64 = Integer('int64')
    intp = int32 if utils.MACHINE_BITS == 32 else int64
    uintp = uint32 if utils.MACHINE_BITS == 32 else uint64
    intc = int32 if struct.calcsize('i') == 4 else int64
    uintc = uint32 if struct.calcsize('I') == 4 else uint64
    ssize_t = int32 if struct.calcsize('n') == 4 else int64
    size_t = uint32 if struct.calcsize('N') == 4 else uint64
    float32 = Float('float32')
    float64 = Float('float64')
    float16 = Float('float16')
    complex64 = Complex('complex64', float32)
    complex128 = Complex('complex128', float64)
    range_iter32_type = RangeIteratorType(int32)
    range_iter64_type = RangeIteratorType(int64)
    unsigned_range_iter64_type = RangeIteratorType(uint64)
    range_state32_type = RangeType(int32)
    range_state64_type = RangeType(int64)
    unsigned_range_state64_type = RangeType(uint64)
    signed_domain = frozenset([
        int8,
        int16,
        int32,
        int64])
    unsigned_domain = frozenset([
        uint8,
        uint16,
        uint32,
        uint64])
    integer_domain = signed_domain | unsigned_domain
    real_domain = frozenset([
        float32,
        float64])
    complex_domain = frozenset([
        complex64,
        complex128])
    number_domain = real_domain | integer_domain | complex_domain
    c_bool = boolean
    py_bool = boolean
    np_bool_ = boolean
    c_uint8 = uint8
    np_uint8 = uint8
    c_uint16 = uint16
    np_uint16 = uint16
    c_uint32 = uint32
    np_uint32 = uint32
    c_uint64 = uint64
    np_uint64 = uint64
    c_uintp = uintp
    np_uintp = uintp
    c_int8 = int8
    np_int8 = int8
    c_int16 = int16
    np_int16 = int16
    c_int32 = int32
    np_int32 = int32
    c_int64 = int64
    np_int64 = int64
    c_intp = intp
    py_int = intp
    np_intp = intp
    c_float16 = float16
    np_float16 = float16
    c_float32 = float32
    np_float32 = float32
    c_float64 = float64
    py_float = float64
    np_float64 = float64
    np_complex64 = complex64
    py_complex = complex128
    np_complex128 = complex128
    py_signed_domain = signed_domain
    np_signed_domain = signed_domain
    np_unsigned_domain = unsigned_domain
    py_integer_domain = integer_domain
    np_integer_domain = integer_domain
    py_real_domain = real_domain
    np_real_domain = real_domain
    py_complex_domain = complex_domain
    np_complex_domain = complex_domain
    py_number_domain = number_domain
    np_number_domain = number_domain
    b1 = bool_
    i1 = int8
    i2 = int16
    i4 = int32
    i8 = int64
    u1 = uint8
    u2 = uint16
    u4 = uint32
    u8 = uint64
    f2 = float16
    f4 = float32
    f8 = float64
    c8 = complex64
    c16 = complex128
    np_float_ = float32
    np_double = float64
    double = float64
    if numpy_version < (2, 0):
        float_ = float32
    
    _make_signed = lambda x: globals()['int%d' % np.dtype(x).itemsize * 8]
    
    _make_unsigned = lambda x: globals()['uint%d' % np.dtype(x).itemsize * 8]
    char = _make_signed(np.byte)
    np_char = _make_signed(np.byte)
    uchar = _make_unsigned(np.byte)
    np_uchar = _make_unsigned(np.byte)
    byte = _make_unsigned(np.byte)
    short = _make_signed(np.short)
    np_short = _make_signed(np.short)
    ushort = _make_unsigned(np.short)
    np_ushort = _make_unsigned(np.short)
    int_ = _make_signed(np.int_)
    np_int_ = _make_signed(np.int_)
    uint = _make_unsigned(np.int_)
    np_uint = _make_unsigned(np.int_)
    intc = _make_signed(np.intc)
    np_intc = _make_signed(np.intc)
    uintc = _make_unsigned(np.uintc)
    np_uintc = _make_unsigned(np.uintc)
    long_ = _make_signed(np.int_)
    np_long = _make_signed(np.int_)
    ulong = _make_unsigned(np.int_)
    np_ulong = _make_unsigned(np.int_)
    longlong = _make_signed(np.longlong)
    np_longlong = _make_signed(np.longlong)
    ulonglong = _make_unsigned(np.longlong)
    np_ulonglong = _make_unsigned(np.longlong)
    all_str = '\n    int8\n    int16\n    int32\n    int64\n    uint8\n    uint16\n    uint32\n    uint64\n    intp\n    uintp\n    intc\n    uintc\n    ssize_t\n    size_t\n    boolean\n    float32\n    float64\n    complex64\n    complex128\n    bool_\n    byte\n    char\n    uchar\n    short\n    ushort\n    int_\n    uint\n    long_\n    ulong\n    longlong\n    ulonglong\n    float_\n    double\n    void\n    none\n    b1\n    i1\n    i2\n    i4\n    i8\n    u1\n    u2\n    u4\n    u8\n    f4\n    f8\n    c8\n    c16\n    optional\n    ffi_forced_object\n    ffi\n    deferred_type\n    '
else:
    from new_scalars import *
    c_bool = MachineBoolean('c_bool')
    c_byte = MachineInteger('c_int8')
    c_int8 = MachineInteger('c_int8')
    c_int16 = MachineInteger('c_int16')
    c_int32 = MachineInteger('c_int32')
    c_int64 = MachineInteger('c_int64')
    c_uint8 = MachineInteger('c_uint8')
    c_uint16 = MachineInteger('c_uint16')
    c_uint32 = MachineInteger('c_uint32')
    c_uint64 = MachineInteger('c_uint64')
    c_intp = c_int32 if utils.MACHINE_BITS == 32 else c_int64
    c_uintp = c_uint32 if utils.MACHINE_BITS == 32 else c_uint64
    c_float16 = MachineFloat('c_float16')
    c_float32 = MachineFloat('c_float32')
    c_float64 = MachineFloat('c_float64')
    c_complex64 = MachineComplex('c_complex64', c_float32)
    c_complex128 = MachineComplex('c_complex128', c_float64)
    c_signed_domain = frozenset([
        c_int8,
        c_int16,
        c_int32,
        c_int64])
    c_unsigned_domain = frozenset([
        c_uint8,
        c_uint16,
        c_uint32,
        c_uint64])
    c_integer_domain = c_signed_domain | c_unsigned_domain
    c_real_domain = frozenset([
        c_float32,
        c_float64])
    c_complex_domain = frozenset([
        c_complex64,
        c_complex128])
    c_number_domain = c_real_domain | c_integer_domain | c_complex_domain
    py_bool = PythonBoolean('py_bool')
    py_int = PythonInteger('py_int')
    py_float = PythonFloat('py_float')
    py_complex = PythonComplex('py_complex', py_float)
    py_signed_domain = frozenset([
        py_int])
    py_integer_domain = py_signed_domain
    py_real_domain = frozenset([
        py_float])
    py_complex_domain = frozenset([
        py_complex])
    py_number_domain = py_real_domain | py_integer_domain | py_complex_domain
    range_iter_type = RangeIteratorType(py_int)
    range_state_type = RangeType(py_int)
    np_bool_ = NumPyBoolean('np_bool_')
    np_bool = NumPyBoolean('np_bool_')
    np_byte = NumPyInteger('np_int8')
    np_int8 = NumPyInteger('np_int8')
    np_int16 = NumPyInteger('np_int16')
    np_int32 = NumPyInteger('np_int32')
    np_int64 = NumPyInteger('np_int64')
    np_uint8 = NumPyInteger('np_uint8')
    np_uint16 = NumPyInteger('np_uint16')
    np_uint32 = NumPyInteger('np_uint32')
    np_uint64 = NumPyInteger('np_uint64')
    np_intp = np_int32 if utils.MACHINE_BITS == 32 else np_int64
    np_uintp = np_uint32 if utils.MACHINE_BITS == 32 else np_uint64
    np_float16 = NumPyFloat('np_float16')
    np_float32 = NumPyFloat('np_float32')
    np_float64 = NumPyFloat('np_float64')
    np_complex64 = NumPyComplex('np_complex64', np_float32)
    np_complex128 = NumPyComplex('np_complex128', np_float64)
    np_signed_domain = frozenset([
        np_int8,
        np_int16,
        np_int32,
        np_int64])
    np_unsigned_domain = frozenset([
        np_uint8,
        np_uint16,
        np_uint32,
        np_uint64])
    np_integer_domain = np_signed_domain | np_unsigned_domain
    np_real_domain = frozenset([
        np_float32,
        np_float64])
    np_complex_domain = frozenset([
        np_complex64,
        np_complex128])
    np_number_domain = np_real_domain | np_integer_domain | np_complex_domain
    np_double = np_float64
    
    _make_signed = lambda x: globals()['np_int%d' % np.dtype(x).itemsize * 8]
    
    _make_unsigned = lambda x: globals()['np_uint%d' % np.dtype(x).itemsize * 8]
    np_char = _make_signed(np.byte)
    np_uchar = _make_unsigned(np.byte)
    byte = _make_unsigned(np.byte)
    np_short = _make_signed(np.short)
    np_ushort = _make_unsigned(np.short)
    np_int_ = _make_signed(np.int_)
    np_uint = _make_unsigned(np.int_)
    np_intc = _make_signed(np.intc)
    np_uintc = _make_unsigned(np.uintc)
    np_long_ = _make_signed(np.int_)
    np_ulong = _make_unsigned(np.int_)
    np_longlong = _make_signed(np.longlong)
    np_ulonglong = _make_unsigned(np.longlong)
    all_str = '\n    c_bool\n    c_byte\n    c_int8\n    c_int16\n    c_int32\n    c_int64\n    c_uint8\n    c_uint16\n    c_uint32\n    c_uint64\n    c_intp\n    c_uintp\n    c_float16\n    c_float32\n    c_float64\n    c_complex64\n    c_complex128\n    py_bool\n    py_int\n    py_float\n    py_complex\n    np_bool_\n    np_bool\n    np_byte\n    np_int8\n    np_int16\n    np_int32\n    np_int64\n    np_uint8\n    np_uint16\n    np_uint32\n    np_uint64\n    np_intp\n    np_uintp\n    np_float16\n    np_float32\n    np_float64\n    np_complex64\n    np_complex128\n    np_double\n    np_char\n    np_uchar\n    np_short\n    np_ushort\n    np_int_\n    np_uint\n    np_intc\n    np_uintc\n    np_long_\n    np_ulong\n    np_longlong\n    np_ulonglong\n    ffi_forced_object\n    ffi\n    none\n    optional\n    deferred_type\n    void\n    '
__all__ = all_str.split()
if numpy_version >= (2, 0) or config.USE_LEGACY_TYPE_SYSTEM:
    __all__.remove('float_')
    __all__.append('bool')
    return None
return None
