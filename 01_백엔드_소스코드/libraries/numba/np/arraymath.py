# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: arraymath.pyc (Python 3.11)

'''
Implementation of math operations on Array objects.
'''
import math
from collections import namedtuple
import operator
import warnings
import llvmlite.ir as llvmlite
import numpy as np
from numba.core import types, cgutils
from numba.core.extending import overload, overload_method, register_jitable
from numba.np.numpy_support import as_dtype, type_can_asarray, type_is_scalar, numpy_version, is_nonelike, check_is_integer, lt_floats, lt_complex
from numba.core.imputils import lower_builtin, impl_ret_borrowed, impl_ret_new_ref, impl_ret_untracked
from numba.np.arrayobj import make_array, load_item, store_item, _empty_nd_impl
from numba.np.linalg import ensure_blas
from numba.core.extending import intrinsic
from numba.core.errors import RequireLiteralValue, TypingError, NumbaValueError, NumbaNotImplementedError, NumbaTypeError, NumbaDeprecationWarning
from numba.cpython.unsafe.tuple import tuple_setitem

def _check_blas():
    
    try:
        ensure_blas()
    except ImportError:
        return False

    return True

_HAVE_BLAS = _check_blas()
_create_tuple_result_shape = (lambda tyctx, shape_list, shape_tuple: pass# WARNING: Decompyle incomplete
)()
_gen_index_tuple = (lambda tyctx, shape_tuple, value, axis: pass# WARNING: Decompyle incomplete
)()
array_sum = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()()
_array_sum_axis_nop = (lambda arr, v: arr)()

def gen_sum_axis_impl(is_axis_const, const_axis_val, op, zero):
    pass
# WARNING: Decompyle incomplete

array_sum_axis_dtype = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()()()()
array_sum_dtype = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()()
array_sum_axis = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()()()()

def get_accumulator(dtype, value):
    if dtype.type == np.timedelta64:
        acc_init = np.int64(value).view(dtype)
    else:
        acc_init = dtype.type(value)
    return acc_init

array_prod = (lambda a: pass# WARNING: Decompyle incomplete
)()()
array_cumsum = (lambda a: pass# WARNING: Decompyle incomplete
)()()
array_cumprod = (lambda a: pass# WARNING: Decompyle incomplete
)()()
array_mean = (lambda a: pass# WARNING: Decompyle incomplete
)()()
array_var = (lambda a: if isinstance(a, types.Array):

def array_var_impl(a):
m = a.mean()ssd = 0for v in np.nditer(a):
val = v.item() - mssd += np.real(val * np.conj(val))ssd / a.sizearray_var_impl)()()
array_std = (lambda a: if isinstance(a, types.Array):

def array_std_impl(a):
a.var() ** 0.5array_std_impl)()()
min_comparator = (lambda a, min_val: a < min_val)()
max_comparator = (lambda a, min_val: a > min_val)()
return_false = (lambda a: False)()
npy_min = (lambda a: pass# WARNING: Decompyle incomplete
)()()()
npy_max = (lambda a: pass# WARNING: Decompyle incomplete
)()()()
array_argmin_impl_datetime = (lambda arry: if arry.size == 0:
raise ValueError('attempt to get argmin of an empty sequence')it = np.nditer(arry)min_value = next(it).take(0)min_idx = 0if np.isnat(min_value):
min_idxidx = Nonefor view in it:
v = view.item()if np.isnat(v):
None, idxif None < min_value:
idx = vidx += 1min_idx)()
array_argmin_impl_float = (lambda arry: if arry.size == 0:
raise ValueError('attempt to get argmin of an empty sequence')for v in arry.flat:
min_value = vmin_idx = 0if np.isnan(min_value):
min_idxidx = Nonefor v in arry.flat:
if np.isnan(v):
None, idxif None < min_value:
idx = vidx += 1min_idx)()
array_argmin_impl_generic = (lambda arry: if arry.size == 0:
raise ValueError('attempt to get argmin of an empty sequence')for v in arry.flat:
min_value = vmin_idx = 0raise RuntimeError('unreachable')idx = 0for v in arry.flat:
if v < min_value:
min_value = vmin_idx = idxidx += 1min_idx)()
array_argmin = (lambda a, axis = (None,): pass# WARNING: Decompyle incomplete
)()()
array_argmax_impl_datetime = (lambda arry: if arry.size == 0:
raise ValueError('attempt to get argmax of an empty sequence')it = np.nditer(arry)max_value = next(it).take(0)max_idx = 0if np.isnat(max_value):
max_idxidx = Nonefor view in it:
v = view.item()if np.isnat(v):
None, idxif None > max_value:
idx = vidx += 1max_idx)()
array_argmax_impl_float = (lambda arry: if arry.size == 0:
raise ValueError('attempt to get argmax of an empty sequence')for v in arry.flat:
max_value = vmax_idx = 0if np.isnan(max_value):
max_idxidx = Nonefor v in arry.flat:
if np.isnan(v):
None, idxif None > max_value:
idx = vidx += 1max_idx)()
array_argmax_impl_generic = (lambda arry: if arry.size == 0:
raise ValueError('attempt to get argmax of an empty sequence')for v in arry.flat:
max_value = vmax_idx = 0idx = 0for v in arry.flat:
if v > max_value:
max_value = vmax_idx = idxidx += 1max_idx)()

def build_argmax_or_argmin_with_axis_impl(a, axis, flatten_impl):
    '''
    Given a function that implements the logic for handling a flattened
    array, return the implementation function.
    '''
    pass
# WARNING: Decompyle incomplete

array_argmax = (lambda a, axis = (None,): pass# WARNING: Decompyle incomplete
)()()
np_all = (lambda a: 
def flat_all(a):
for v in np.nditer(a):
if not v.item():
FalseTrueflat_all)()()
_allclose_scalars = (lambda a_v, b_v, rtol, atol, equal_nan = (1e-05, 1e-08, False): a_v_isnan = np.isnan(a_v)b_v_isnan = np.isnan(b_v)if not (a_v_isnan or b_v_isnan or a_v_isnan) and b_v_isnan:
Falseif None and b_v_isnan:
if not equal_nan:
Falseif np.isinf(a_v) or np.isinf(b_v):
a_v == b_vif None.abs(a_v - b_v) > atol + rtol * np.abs(b_v * 1):
False)()
np_allclose = (lambda a, b, rtol, atol, equal_nan = (1e-05, 1e-08, False): if not type_can_asarray(a):
raise TypingError('The first argument "a" must be array-like')if not type_can_asarray(b):
raise TypingError('The second argument "b" must be array-like')if not isinstance(rtol, (float, types.Float)):
raise TypingError('The third argument "rtol" must be a floating point')if not isinstance(atol, (float, types.Float)):
raise TypingError('The fourth argument "atol" must be a floating point')if not isinstance(equal_nan, (bool, types.Boolean)):
raise TypingError('The fifth argument "equal_nan" must be a boolean')is_a_scalar = isinstance(a, types.Number)is_b_scalar = isinstance(b, types.Number)if is_a_scalar and is_b_scalar:

def np_allclose_impl_scalar_scalar(a, b, rtol, atol, equal_nan = (1e-05, 1e-08, False)):
_allclose_scalars(a, b, rtol = rtol, atol = atol, equal_nan = equal_nan)np_allclose_impl_scalar_scalarif not None and is_b_scalar:

def np_allclose_impl_scalar_array(a, b, rtol, atol, equal_nan = (1e-05, 1e-08, False)):
b = np.asarray(b)for bv in np.nditer(b):
if not _allclose_scalars(a, bv.item(), rtol = rtol, atol = atol, equal_nan = equal_nan):
FalseTruenp_allclose_impl_scalar_arrayif None and is_b_scalar:

def np_allclose_impl_array_scalar(a, b, rtol, atol, equal_nan = (1e-05, 1e-08, False)):
a = np.asarray(a)for av in np.nditer(a):
if not _allclose_scalars(av.item(), b, rtol = rtol, atol = atol, equal_nan = equal_nan):
FalseTruenp_allclose_impl_array_scalarif not None or is_b_scalar:

def np_allclose_impl_array_array(a, b, rtol, atol, equal_nan = (1e-05, 1e-08, False)):
a = np.asarray(a)b = np.asarray(b)(a_a, b_b) = np.broadcast_arrays(a, b)for av, bv in np.nditer((a_a, b_b)):
if not _allclose_scalars(av.item(), bv.item(), rtol = rtol, atol = atol, equal_nan = equal_nan):
FalseTruenp_allclose_impl_array_arrayNone)()()
np_any = (lambda a: 
def flat_any(a):
for v in np.nditer(a):
if v.item():
TrueFalseflat_any)()()
np_average = (lambda a, axis, weights = (None, None): pass# WARNING: Decompyle incomplete
)()

def get_isnan(dtype):
    '''
    A generic isnan() function
    '''
    if isinstance(dtype, (types.Float, types.Complex)):
        return np.isnan
    _trivial_isnan = (lambda x: False)()
    return _trivial_isnan

np_iscomplex = (lambda x: if type_can_asarray(x):
(lambda x: np.asarray(x).imag != 0)
)()
np_isreal = (lambda x: if type_can_asarray(x):
(lambda x: np.asarray(x).imag == 0)
)()
iscomplexobj = (lambda x: pass# WARNING: Decompyle incomplete
)()
isrealobj = (lambda x: 
def impl(x):
not np.iscomplexobj(x)impl)()
np_isscalar = (lambda element: pass# WARNING: Decompyle incomplete
)()

def is_np_inf_impl(x, out, fn):
    pass
# WARNING: Decompyle incomplete

isneginf = (lambda x, out = (None,): fn = register_jitable((lambda x: x))
    return is_np_inf_impl(x, out, fn)
)()
isposinf = (lambda x, out = (None,): fn = register_jitable((lambda x: ~x))
    return is_np_inf_impl(x, out, fn)
)()
less_than = (lambda a, b: a < b)()
greater_than = (lambda a, b: a > b)()
check_array = (lambda a: if a.size == 0:
raise ValueError('zero-size array to reduction operation not possible'))()

def nan_min_max_factory(comparison_op, is_complex_dtype):
    pass
# WARNING: Decompyle incomplete

real_nanmin = register_jitable(nan_min_max_factory(less_than, is_complex_dtype = False))
real_nanmax = register_jitable(nan_min_max_factory(greater_than, is_complex_dtype = False))
complex_nanmin = register_jitable(nan_min_max_factory(less_than, is_complex_dtype = True))
complex_nanmax = register_jitable(nan_min_max_factory(greater_than, is_complex_dtype = True))
_isclose_item = (lambda x, y, rtol, atol, equal_nan: if np.isnan(x) and np.isnan(y):
equal_nanif None.isinf(x) and np.isinf(y):
(x > 0) == (y > 0)if None.isinf(x) or np.isinf(y):
FalseNone(x - y) <= atol + rtol * abs(y))()
isclose = (lambda a, b, rtol, atol, equal_nan = (1e-05, 1e-08, False): if not type_can_asarray(a):
raise TypingError('The first argument "a" must be array-like')if not type_can_asarray(b):
raise TypingError('The second argument "b" must be array-like')if not isinstance(rtol, (float, types.Float)):
raise TypingError('The third argument "rtol" must be a floating point')if not isinstance(atol, (float, types.Float)):
raise TypingError('The fourth argument "atol" must be a floating point')if not isinstance(equal_nan, (bool, types.Boolean)):
raise TypingError('The fifth argument "equal_nan" must be a boolean')if isinstance(a, types.Array) and isinstance(b, types.Number):

def isclose_impl(a, b, rtol, atol, equal_nan = (1e-05, 1e-08, False)):
x = a.reshape(-1)y = bout = np.zeros(len(x), np.bool_)for i in range(len(out)):
out[i] = _isclose_item(x[i], y, rtol, atol, equal_nan)out.reshape(a.shape)elif isinstance(a, types.Number) and isinstance(b, types.Array):

def isclose_impl(a, b, rtol, atol, equal_nan = (1e-05, 1e-08, False)):
x = ay = b.reshape(-1)out = np.zeros(len(y), np.bool_)for i in range(len(out)):
out[i] = _isclose_item(x, y[i], rtol, atol, equal_nan)out.reshape(b.shape)elif isinstance(a, types.Array) and isinstance(b, types.Array):

def isclose_impl(a, b, rtol, atol, equal_nan = (1e-05, 1e-08, False)):
shape = np.broadcast_shapes(a.shape, b.shape)a_ = np.broadcast_to(a, shape)b_ = np.broadcast_to(b, shape)out = np.zeros(len(a_), dtype = np.bool_)for av, bv in enumerate(np.nditer((a_, b_))):
out[i] = _isclose_item(av.item(), bv.item(), rtol, atol, equal_nan)np.broadcast_to(out, shape)else:

def isclose_impl(a, b, rtol, atol, equal_nan = (1e-05, 1e-08, False)):
_isclose_item(a, b, rtol, atol, equal_nan)isclose_impl)()
np_nanmin = (lambda a: dt = determine_dtype(a)if np.issubdtype(dt, np.complexfloating):
complex_nanmin)()
np_nanmax = (lambda a: dt = determine_dtype(a)if np.issubdtype(dt, np.complexfloating):
complex_nanmax)()
np_nanmean = (lambda a: pass# WARNING: Decompyle incomplete
)()
np_nanvar = (lambda a: pass# WARNING: Decompyle incomplete
)()
np_nanstd = (lambda a:
