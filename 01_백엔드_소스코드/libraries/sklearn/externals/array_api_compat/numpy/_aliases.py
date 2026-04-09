# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _aliases.pyc (Python 3.11)

from __future__ import annotations
from builtins import bool as py_bool
from typing import TYPE_CHECKING, Any, Literal, TypeAlias, cast
import numpy as np
from _internal import get_xp
from common import _aliases, _helpers
from common._typing import NestedSequence, SupportsBufferProtocol
from _info import __array_namespace_info__
from _typing import Array, Device, DType
if TYPE_CHECKING:
    from typing_extensions import Buffer, TypeIs
_Copy: 'TypeAlias' = py_bool | Literal[2] | np._CopyMode
bool = np.bool_
acos = np.arccos
acosh = np.arccosh
asin = np.arcsin
asinh = np.arcsinh
atan = np.arctan
atan2 = np.arctan2
atanh = np.arctanh
bitwise_left_shift = np.left_shift
bitwise_invert = np.invert
bitwise_right_shift = np.right_shift
concat = np.concatenate
pow = np.power
arange = get_xp(np)(_aliases.arange)
empty = get_xp(np)(_aliases.empty)
empty_like = get_xp(np)(_aliases.empty_like)
eye = get_xp(np)(_aliases.eye)
full = get_xp(np)(_aliases.full)
full_like = get_xp(np)(_aliases.full_like)
linspace = get_xp(np)(_aliases.linspace)
ones = get_xp(np)(_aliases.ones)
ones_like = get_xp(np)(_aliases.ones_like)
zeros = get_xp(np)(_aliases.zeros)
zeros_like = get_xp(np)(_aliases.zeros_like)
UniqueAllResult = get_xp(np)(_aliases.UniqueAllResult)
UniqueCountsResult = get_xp(np)(_aliases.UniqueCountsResult)
UniqueInverseResult = get_xp(np)(_aliases.UniqueInverseResult)
unique_all = get_xp(np)(_aliases.unique_all)
unique_counts = get_xp(np)(_aliases.unique_counts)
unique_inverse = get_xp(np)(_aliases.unique_inverse)
unique_values = get_xp(np)(_aliases.unique_values)
std = get_xp(np)(_aliases.std)
var = get_xp(np)(_aliases.var)
cumulative_sum = get_xp(np)(_aliases.cumulative_sum)
cumulative_prod = get_xp(np)(_aliases.cumulative_prod)
clip = get_xp(np)(_aliases.clip)
permute_dims = get_xp(np)(_aliases.permute_dims)
reshape = get_xp(np)(_aliases.reshape)
argsort = get_xp(np)(_aliases.argsort)
sort = get_xp(np)(_aliases.sort)
nonzero = get_xp(np)(_aliases.nonzero)
ceil = get_xp(np)(_aliases.ceil)
floor = get_xp(np)(_aliases.floor)
trunc = get_xp(np)(_aliases.trunc)
matmul = get_xp(np)(_aliases.matmul)
matrix_transpose = get_xp(np)(_aliases.matrix_transpose)
tensordot = get_xp(np)(_aliases.tensordot)
sign = get_xp(np)(_aliases.sign)
finfo = get_xp(np)(_aliases.finfo)
iinfo = get_xp(np)(_aliases.iinfo)

def _supports_buffer_protocol(obj = None):
    
    try:
        memoryview(obj)
    except TypeError:
        return False

    return True


def asarray(obj = None, *, dtype, device, copy, **kwargs):
    '''
    Array API compatibility wrapper for asarray().

    See the corresponding documentation in the array library and/or the array API
    specification for more details.
    '''
    _helpers._check_device(np, device)
# WARNING: Decompyle incomplete


def astype(x = None, dtype = None, *, copy, device):
    _helpers._check_device(np, device)
    return x.astype(dtype = dtype, copy = copy)


def count_nonzero(x = None, axis = None, keepdims = None):
    result = cast('Any', np.count_nonzero(x, axis = axis, keepdims = keepdims))
# WARNING: Decompyle incomplete


def take_along_axis(x = None, indices = None, *, axis):
    return np.take_along_axis(x, indices, axis = axis)

if hasattr(np, 'vecdot'):
    vecdot = np.vecdot
else:
    vecdot = get_xp(np)(_aliases.vecdot)
if hasattr(np, 'isdtype'):
    isdtype = np.isdtype
else:
    isdtype = get_xp(np)(_aliases.isdtype)
if hasattr(np, 'unstack'):
    unstack = np.unstack
else:
    unstack = get_xp(np)(_aliases.unstack)
__all__ = [
    '__array_namespace_info__',
    'asarray',
    'astype',
    'acos',
    'acosh',
    'asin',
    'asinh',
    'atan',
    'atan2',
    'atanh',
    'bitwise_left_shift',
    'bitwise_invert',
    'bitwise_right_shift',
    'bool',
    'concat',
    'count_nonzero',
    'pow',
    'take_along_axis']
__all__ += _aliases.__all__
_all_ignore = [
    'np',
    'get_xp']

def __dir__():
    return __all__
