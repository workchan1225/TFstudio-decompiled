# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: twodim_base.pyc (Python 3.11)

''' Basic functions for manipulating 2d arrays

'''
import functools
import operator
from numpy.core.numeric import asanyarray, arange, zeros, greater_equal, multiply, ones, asarray, where, int8, int16, int32, int64, intp, empty, promote_types, diagonal, nonzero, indices
from numpy.core.overrides import set_array_function_like_doc, set_module
from numpy.core import overrides
from numpy.core import iinfo
from numpy.lib.stride_tricks import broadcast_to
__all__ = [
    'diag',
    'diagflat',
    'eye',
    'fliplr',
    'flipud',
    'tri',
    'triu',
    'tril',
    'vander',
    'histogram2d',
    'mask_indices',
    'tril_indices',
    'tril_indices_from',
    'triu_indices',
    'triu_indices_from']
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')
i1 = iinfo(int8)
i2 = iinfo(int16)
i4 = iinfo(int32)

def _min_int(low, high):
    ''' get small int that fits the range '''
    if high <= i1.max and low >= i1.min:
        return int8
    if None <= i2.max and low >= i2.min:
        return int16
    if None <= i4.max and low >= i4.min:
        return int32


def _flip_dispatcher(m):
    return (m,)

fliplr = (lambda m: m = asanyarray(m)if m.ndim < 2:
raise ValueError('Input must be >= 2-d.')m[(:, ::-1)])()
flipud = (lambda m: m = asanyarray(m)if m.ndim < 1:
raise ValueError('Input must be >= 1-d.')m[(::-1, ...)])()
eye = (lambda N, M, k = set_module('numpy'), dtype = (None, 0, float, 'C'), order = {
    'like': None }, *, like, m = None, i = None,
