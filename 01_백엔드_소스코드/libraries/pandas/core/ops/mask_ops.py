# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mask_ops.pyc (Python 3.11)

'''
Ops for masked arrays.
'''
from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
from pandas._libs import lib, missing as libmissing
if TYPE_CHECKING:
    from pandas._typing import npt

def kleene_or(left = None, right = None, left_mask = None, right_mask = ('left', 'bool | np.ndarray | libmissing.NAType', 'right', 'bool | np.ndarray | libmissing.NAType', 'left_mask', 'np.ndarray | None', 'right_mask', 'np.ndarray | None', 'return', 'tuple[npt.NDArray[np.bool_], npt.NDArray[np.bool_]]')):
    '''
    Boolean ``or`` using Kleene logic.

    Values are NA where we have ``NA | NA`` or ``NA | False``.
    ``NA | True`` is considered True.

    Parameters
    ----------
    left, right : ndarray, NA, or bool
        The values of the array.
    left_mask, right_mask : ndarray, optional
        The masks. Only one of these may be None, which implies that
        the associated `left` or `right` value is a scalar.

    Returns
    -------
    result, mask: ndarray[bool]
        The result of the logical or, and the new mask.
    '''
    pass
# WARNING: Decompyle incomplete


def kleene_xor(left = None, right = None, left_mask = None, right_mask = ('left', 'bool | np.ndarray | libmissing.NAType', 'right', 'bool | np.ndarray | libmissing.NAType', 'left_mask', 'np.ndarray | None', 'right_mask', 'np.ndarray | None', 'return', 'tuple[npt.NDArray[np.bool_], npt.NDArray[np.bool_]]')):
    '''
    Boolean ``xor`` using Kleene logic.

    This is the same as ``or``, with the following adjustments

    * True, True -> False
    * True, NA   -> NA

    Parameters
    ----------
    left, right : ndarray, NA, or bool
        The values of the array.
    left_mask, right_mask : ndarray, optional
        The masks. Only one of these may be None, which implies that
        the associated `left` or `right` value is a scalar.

    Returns
    -------
    result, mask: ndarray[bool]
        The result of the logical xor, and the new mask.
    '''
    pass
# WARNING: Decompyle incomplete


def kleene_and(left = None, right = None, left_mask = None, right_mask = ('left', 'bool | libmissing.NAType | np.ndarray', 'right', 'bool | libmissing.NAType | np.ndarray', 'left_mask', 'np.ndarray | None', 'right_mask', 'np.ndarray | None', 'return', 'tuple[npt.NDArray[np.bool_], npt.NDArray[np.bool_]]')):
    '''
    Boolean ``and`` using Kleene logic.

    Values are ``NA`` for ``NA & NA`` or ``True & NA``.

    Parameters
    ----------
    left, right : ndarray, NA, or bool
        The values of the array.
    left_mask, right_mask : ndarray, optional
        The masks. Only one of these may be None, which implies that
        the associated `left` or `right` value is a scalar.

    Returns
    -------
    result, mask: ndarray[bool]
        The result of the logical xor, and the new mask.
    '''
    pass
# WARNING: Decompyle incomplete


def raise_for_nan(value = None, method = None):
    if lib.is_float(value) or np.isnan(value):
        raise ValueError(f'''Cannot perform logical \'{method}\' with floating NaN''')
    return None
