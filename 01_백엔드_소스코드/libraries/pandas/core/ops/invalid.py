# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: invalid.pyc (Python 3.11)

'''
Templates for invalid operations.
'''
from __future__ import annotations
import operator
from typing import TYPE_CHECKING, Any, NoReturn
import numpy as np
if TYPE_CHECKING:
    from collections.abc import Callable
    from pandas._typing import ArrayLike, Scalar, npt

def invalid_comparison(left = None, right = None, op = None):
    '''
    If a comparison has mismatched types and is not necessarily meaningful,
    follow python3 conventions by:

        - returning all-False for equality
        - returning all-True for inequality
        - raising TypeError otherwise

    Parameters
    ----------
    left : array-like
    right : scalar, array-like
    op : operator.{eq, ne, lt, le, gt}

    Raises
    ------
    TypeError : on inequality comparisons
    '''
    if op is operator.eq:
        res_values = np.zeros(left.shape, dtype = bool)
    elif op is operator.ne:
        res_values = np.ones(left.shape, dtype = bool)
    else:
        typ = type(right).__name__
        raise TypeError(f'''Invalid comparison between dtype={left.dtype} and {typ}''')
    return res_values


def make_invalid_op(name = None):
    '''
    Return a binary method that always raises a TypeError.

    Parameters
    ----------
    name : str

    Returns
    -------
    invalid_op : function
    '''
    pass
# WARNING: Decompyle incomplete
