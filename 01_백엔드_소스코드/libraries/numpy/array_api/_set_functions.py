# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _set_functions.pyc (Python 3.11)

from __future__ import annotations
from _array_object import Array
from typing import NamedTuple
import numpy as np

class UniqueAllResult(NamedTuple):
    counts: 'Array' = 'UniqueAllResult'


class UniqueCountsResult(NamedTuple):
    counts: 'Array' = 'UniqueCountsResult'


class UniqueInverseResult(NamedTuple):
    inverse_indices: 'Array' = 'UniqueInverseResult'


def unique_all(x = None):
    '''
    Array API compatible wrapper for :py:func:`np.unique <numpy.unique>`.

    See its docstring for more information.
    '''
    (values, indices, inverse_indices, counts) = np.unique(x._array, return_counts = True, return_index = True, return_inverse = True, equal_nan = False)
    inverse_indices = inverse_indices.reshape(x.shape)
    return UniqueAllResult(Array._new(values), Array._new(indices), Array._new(inverse_indices), Array._new(counts))


def unique_counts(x = None):
    res = np.unique(x._array, return_counts = True, return_index = False, return_inverse = False, equal_nan = False)
# WARNING: Decompyle incomplete


def unique_inverse(x = None):
    '''
    Array API compatible wrapper for :py:func:`np.unique <numpy.unique>`.

    See its docstring for more information.
    '''
    (values, inverse_indices) = np.unique(x._array, return_counts = False, return_index = False, return_inverse = True, equal_nan = False)
    inverse_indices = inverse_indices.reshape(x.shape)
    return UniqueInverseResult(Array._new(values), Array._new(inverse_indices))


def unique_values(x = None):
    '''
    Array API compatible wrapper for :py:func:`np.unique <numpy.unique>`.

    See its docstring for more information.
    '''
    res = np.unique(x._array, return_counts = False, return_index = False, return_inverse = False, equal_nan = False)
    return Array._new(res)
