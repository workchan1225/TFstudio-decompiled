# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _manipulation_functions.pyc (Python 3.11)

from __future__ import annotations
from _array_object import Array
from _data_type_functions import result_type
from typing import List, Optional, Tuple, Union
import numpy as np

def concat(arrays = None, *, axis):
    '''
    Array API compatible wrapper for :py:func:`np.concatenate <numpy.concatenate>`.

    See its docstring for more information.
    '''
    pass
# WARNING: Decompyle incomplete


def expand_dims(x = None, *, axis):
    '''
    Array API compatible wrapper for :py:func:`np.expand_dims <numpy.expand_dims>`.

    See its docstring for more information.
    '''
    return Array._new(np.expand_dims(x._array, axis))


def flip(x = None, *, axis):
    '''
    Array API compatible wrapper for :py:func:`np.flip <numpy.flip>`.

    See its docstring for more information.
    '''
    return Array._new(np.flip(x._array, axis = axis))


def permute_dims(x = None, axes = None):
    '''
    Array API compatible wrapper for :py:func:`np.transpose <numpy.transpose>`.

    See its docstring for more information.
    '''
    return Array._new(np.transpose(x._array, axes))


def reshape(x = None, shape = None, *, copy):
    '''
    Array API compatible wrapper for :py:func:`np.reshape <numpy.reshape>`.

    See its docstring for more information.
    '''
    data = x._array
    if copy:
        data = np.copy(data)
    reshaped = np.reshape(data, shape)
    if not copy is False and np.shares_memory(data, reshaped):
        raise AttributeError('Incompatible shape for in-place modification.')
    return Array._new(reshaped)


def roll(x = None, shift = None, *, axis):
    '''
    Array API compatible wrapper for :py:func:`np.roll <numpy.roll>`.

    See its docstring for more information.
    '''
    return Array._new(np.roll(x._array, shift, axis = axis))


def squeeze(x = None, axis = None):
    '''
    Array API compatible wrapper for :py:func:`np.squeeze <numpy.squeeze>`.

    See its docstring for more information.
    '''
    return Array._new(np.squeeze(x._array, axis = axis))


def stack(arrays = None, *, axis):
    '''
    Array API compatible wrapper for :py:func:`np.stack <numpy.stack>`.

    See its docstring for more information.
    '''
    pass
# WARNING: Decompyle incomplete
