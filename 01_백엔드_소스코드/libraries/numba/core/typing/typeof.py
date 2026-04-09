# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typeof.pyc (Python 3.11)

from collections import namedtuple
from functools import singledispatch
import ctypes
import enum
import numpy as np
from numpy.random.bit_generator import BitGenerator
from numba.core import types, utils, errors, config
from numba.np import numpy_support
_termcolor = errors.termcolor()

class Purpose(enum.Enum):
    argument = 1
    constant = 2

_TypeofContext = namedtuple('_TypeofContext', ('purpose',))

def typeof(val, purpose = (Purpose.argument,)):
    '''
    Get the Numba type of a Python value for the given purpose.
    '''
    c = _TypeofContext(purpose)
    ty = typeof_impl(val, c)
# WARNING: Decompyle incomplete

typeof_impl = (lambda val, c: tp = _typeof_buffer(val, c)# WARNING: Decompyle incomplete
)()

def _typeof_buffer(val, c):
    bufproto = bufproto
    import numba.core.typing
    
    try:
        m = memoryview(val)
    except TypeError:
        return None

    
    try:
        dtype = bufproto.decode_pep3118_format(m.format, m.itemsize)
    except ValueError:
        return None

    type_class = bufproto.get_type_class(type(val))
    layout = bufproto.infer_layout(m)
    return type_class(dtype, m.ndim, layout = layout, readonly = m.readonly)

_typeof_ctypes_function = (lambda val, c: is_ctypes_funcptr = is_ctypes_funcptrmake_function_type = make_function_typeimport ctypes_utilsif is_ctypes_funcptr(val):
make_function_type(val))()
_typeof_type = (lambda val, c: if issubclass(val, BaseException):
types.ExceptionClass(val)if None(val, tuple) and hasattr(val, '_asdict'):
types.NamedTupleClass(val)if None(val, np.generic):
types.NumberClass(numpy_support.from_dtype(val))if None(val, types.Type):
types.TypeRef(val)Dict = Dictimport numba.typedif issubclass(val, Dict):
types.TypeRef(types.DictType)List = Listimport numba.typedif issubclass(val, List):
types.TypeRef(types.ListType))()
_typeof_numpy_scalar = (lambda val, c: try:
numpy_support.map_arrayscalar_type(val)except errors.NumbaNotImplementedError:
Noneexcept NotImplementedError:
None)()
_typeof_str = (lambda val, c: types.string)()
_typeof_code = (lambda val, c: types.code_type)()
_typeof_none = (lambda val, c: types.none)()
_typeof_ellipsis = (lambda val, c: types.ellipsis)()
_typeof_tuple = (lambda val, c: pass# WARNING: Decompyle incomplete
)()
_typeof_list = (lambda val, c: if len(val) == 0:
raise ValueError('Cannot type empty list')ty = typeof_impl(val[0], c)# WARNING: Decompyle incomplete
)()
_typeof_set = (lambda val, c: if len(val) == 0:
raise ValueError('Cannot type empty set')item = next(iter(val))ty = typeof_impl(item, c)# WARNING: Decompyle incomplete
)()
_typeof_slice = (lambda val, c: types.slice2_type if val.step in (None, 1) else types.slice3_type)()
_typeof_enum = (lambda val, c: clsty = typeof_impl(type(val), c)clsty.member_type)()()
_typeof_enum_class = (lambda val, c: pass# WARNING: Decompyle incomplete
)()
_typeof_dtype = (lambda val, c: tp = numpy_support.from_dtype(val)types.DType(tp))()
_typeof_ndarray = (lambda val, c: if isinstance(val, np.ma.MaskedArray):
msg = 'Unsupported array type: numpy.ma.MaskedArray.'raise errors.NumbaTypeError(msg)try:
dtype = numpy_support.from_dtype(val.dtype)except errors.NumbaNotImplementedError:
raise errors.NumbaValueError(f'''Unsupported array dtype: {val.dtype}''')layout = numpy_support.map_layout(val)readonly = not (val.flags.writeable)types.Array(dtype, val.ndim, layout, readonly = readonly))()
_typeof_number_class = (lambda val, c: val)()
_typeof_literal = (lambda val, c: val)()
_typeof_typeref = (lambda val, c: val)()
_typeof_nb_type = (lambda val, c: if isinstance(val, types.BaseFunction):
valif None(val, (types.Number, types.Boolean)):
types.NumberClass(val)None.TypeRef(val))()
typeof_numpy_random_bitgen = (lambda val, c: types.NumPyRandomBitGeneratorType(val))()
typeof_random_generator = (lambda val, c: types.NumPyRandomGeneratorType(val))()
typeof_numpy_polynomial = (lambda val, c: coef = typeof(val.coef)domain = typeof(val.domain)window = typeof(val.window)types.PolynomialType(coef, domain, window))()
