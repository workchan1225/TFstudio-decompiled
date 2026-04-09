# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numeric.pyc (Python 3.11)

import functools
import itertools
import operator
import sys
import warnings
import numbers
import builtins
import numpy as np
from  import multiarray
from multiarray import fastCopyAndTranspose, ALLOW_THREADS, BUFSIZE, CLIP, MAXDIMS, MAY_SHARE_BOUNDS, MAY_SHARE_EXACT, RAISE, WRAP, arange, array, asarray, asanyarray, ascontiguousarray, asfortranarray, broadcast, can_cast, compare_chararrays, concatenate, copyto, dot, dtype, empty, empty_like, flatiter, frombuffer, from_dlpack, fromfile, fromiter, fromstring, inner, lexsort, matmul, may_share_memory, min_scalar_type, ndarray, nditer, nested_iters, promote_types, putmask, result_type, set_numeric_ops, shares_memory, vdot, where, zeros, normalize_axis_index, _get_promotion_state, _set_promotion_state, _using_numpy2_behavior
from  import overrides
from  import umath
from  import shape_base
from overrides import set_array_function_like_doc, set_module
from umath import multiply, invert, sin, PINF, NAN
from  import numerictypes
from numerictypes import longlong, intc, int_, float_, complex_, bool_
from exceptions import ComplexWarning, TooHardError, AxisError
from _ufunc_config import errstate, _no_nep50_warning
bitwise_not = invert
ufunc = type(sin)
newaxis = None
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')
__all__ = [
    'newaxis',
    'ndarray',
    'flatiter',
    'nditer',
    'nested_iters',
    'ufunc',
    'arange',
    'array',
    'asarray',
    'asanyarray',
    'ascontiguousarray',
    'asfortranarray',
    'zeros',
    'count_nonzero',
    'empty',
    'broadcast',
    'dtype',
    'fromstring',
    'fromfile',
    'frombuffer',
    'from_dlpack',
    'where',
    'argwhere',
    'copyto',
    'concatenate',
    'fastCopyAndTranspose',
    'lexsort',
    'set_numeric_ops',
    'can_cast',
    'promote_types',
    'min_scalar_type',
    'result_type',
    'isfortran',
    'empty_like',
    'zeros_like',
    'ones_like',
    'correlate',
    'convolve',
    'inner',
    'dot',
    'outer',
    'vdot',
    'roll',
    'rollaxis',
    'moveaxis',
    'cross',
    'tensordot',
    'little_endian',
    'fromiter',
    'array_equal',
    'array_equiv',
    'indices',
    'fromfunction',
    'isclose',
    'isscalar',
    'binary_repr',
    'base_repr',
    'ones',
    'identity',
    'allclose',
    'compare_chararrays',
    'putmask',
    'flatnonzero',
    'Inf',
    'inf',
    'infty',
    'Infinity',
    'nan',
    'NaN',
    'False_',
    'True_',
    'bitwise_not',
    'CLIP',
    'RAISE',
    'WRAP',
    'MAXDIMS',
    'BUFSIZE',
    'ALLOW_THREADS',
    'full',
    'full_like',
    'matmul',
    'shares_memory',
    'may_share_memory',
    'MAY_SHARE_BOUNDS',
    'MAY_SHARE_EXACT',
    '_get_promotion_state',
    '_set_promotion_state',
    '_using_numpy2_behavior']

def _zeros_like_dispatcher(a, dtype, order, subok, shape = (None, None, None, None)):
    return (a,)

zeros_like = (lambda a, dtype, order, subok, shape = (None, 'K', True, None): res = empty_like(a, dtype = dtype, order = order, subok = subok, shape = shape)z = zeros(1, dtype = res.dtype)multiarray.copyto(res, z, casting = 'unsafe')res)()
ones = (lambda shape = set_module('numpy'), dtype = (None, 'C'), order = {
    'like': None }, *, like, a = None,
