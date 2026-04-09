# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: array_ops.pyc (Python 3.11)

'''
Functions for arithmetic and comparison operations on NumPy arrays and
ExtensionArrays.
'''
from __future__ import annotations
import datetime
from functools import partial
import operator
from typing import TYPE_CHECKING, Any
import numpy as np
from pandas._libs import NaT, Timedelta, Timestamp, lib, ops as libops
from pandas._libs.tslibs import BaseOffset, get_supported_dtype, is_supported_dtype, is_unitless
from pandas.core.dtypes.cast import construct_1d_object_array_from_listlike, find_common_type
from pandas.core.dtypes.common import ensure_object, is_bool_dtype, is_list_like, is_numeric_v_string_like, is_object_dtype, is_scalar
from pandas.core.dtypes.generic import ABCExtensionArray, ABCIndex, ABCSeries
from pandas.core.dtypes.missing import isna, notna
from pandas.core import roperator
from pandas.core.computation import expressions
from pandas.core.construction import ensure_wrapped_if_datetimelike, sanitize_array
from pandas.core.ops import missing
from pandas.core.ops.dispatch import should_extension_dispatch
from pandas.core.ops.invalid import invalid_comparison
if TYPE_CHECKING:
    from pandas._typing import ArrayLike, Shape

def fill_binop(left, right, fill_value):
    '''
    If a non-None fill_value is given, replace null entries in left and right
    with this value, but only in positions where _one_ of left/right is null,
    not both.

    Parameters
    ----------
    left : array-like
    right : array-like
    fill_value : object

    Returns
    -------
    left : array-like
    right : array-like

    Notes
    -----
    Makes copies if fill_value is not None and NAs are present.
    '''
    pass
# WARNING: Decompyle incomplete


def comp_method_OBJECT_ARRAY(op, x, y):
    if isinstance(y, list):
        y = construct_1d_object_array_from_listlike(y)
    if isinstance(y, (np.ndarray, ABCSeries, ABCIndex)):
        if not is_object_dtype(y.dtype):
            y = y.astype(np.object_)
        if isinstance(y, (ABCSeries, ABCIndex)):
            y = y._values
        if x.shape != y.shape:
            raise ValueError('Shapes must match', x.shape, y.shape)
        result = libops.vec_compare(x.ravel(), y.ravel(), op)
    else:
        result = libops.scalar_compare(x.ravel(), y, op)
    return result.reshape(x.shape)


def _masked_arith_op(x = None, y = None, op = None):
    '''
    If the given arithmetic operation fails, attempt it again on
    only the non-null elements of the input array(s).

    Parameters
    ----------
    x : np.ndarray
    y : np.ndarray, Series, Index
    op : binary operator
    '''
    xrav = x.ravel()
    if isinstance(y, np.ndarray):
        dtype = find_common_type([
            x.dtype,
            y.dtype])
        result = np.empty(x.size, dtype = dtype)
        if len(x) != len(y):
            raise ValueError(x.shape, y.shape)
        ymask = notna(y)
        yrav = y.ravel()
        mask = notna(xrav) & ymask.ravel()
        if mask.any():
            result[mask] = op(xrav[mask], yrav[mask])
        elif not is_scalar(y):
            raise TypeError(f'''Cannot broadcast np.ndarray with operand of type {type(y)}''')
    result = np.empty(x.size, dtype = x.dtype)
    mask = notna(xrav)
    if op is pow:
        mask = np.where(x == 1, False, mask)
    elif op is roperator.rpow:
        mask = np.where(y == 1, False, mask)
    if mask.any():
        result[mask] = op(xrav[mask], y)
    np.putmask(result, ~mask, np.nan)
    result = result.reshape(x.shape)
    return result


def _na_arithmetic_op(left = None, right = None, op = None, is_cmp = (False,)):
