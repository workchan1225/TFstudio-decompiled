# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

'''
Boilerplate functions used in defining binary operations.
'''
from __future__ import annotations
from functools import wraps
from typing import TYPE_CHECKING
from pandas._libs.lib import item_from_zerodim
from pandas._libs.missing import is_matching_na
from pandas.core.dtypes.generic import ABCExtensionArray, ABCIndex, ABCSeries
from pandas.core.construction import ensure_wrapped_if_datetimelike, sanitize_array
if TYPE_CHECKING:
    from collections.abc import Callable
    from pandas._typing import F

def unpack_zerodim_and_defer(name = None):
    '''
    Boilerplate for pandas conventions in arithmetic and comparison methods.

    Parameters
    ----------
    name : str

    Returns
    -------
    decorator
    '''
    pass
# WARNING: Decompyle incomplete


def _unpack_zerodim_and_defer(method = None, name = None):
    '''
    Boilerplate for pandas conventions in arithmetic and comparison methods.

    Ensure method returns NotImplemented when operating against "senior"
    classes.  Ensure zero-dimensional ndarrays are always unpacked.

    Parameters
    ----------
    method : binary method
    name : str

    Returns
    -------
    method
    '''
    pass
# WARNING: Decompyle incomplete


def get_op_result_name(left, right):
    '''
    Find the appropriate name to pin to an operation result.  This result
    should always be either an Index or a Series.

    Parameters
    ----------
    left : {Series, Index}
    right : object

    Returns
    -------
    name : object
        Usually a string
    '''
    if isinstance(right, (ABCSeries, ABCIndex)):
        name = _maybe_match_name(left, right)
    else:
        name = left.name
    return name


def _maybe_match_name(a, b):
    '''
    Try to find a name to attach to the result of an operation between
    a and b.  If only one of these has a `name` attribute, return that
    name.  Otherwise return a consensus name if they match or None if
    they have different names.

    Parameters
    ----------
    a : object
    b : object

    Returns
    -------
    name : str or None

    See Also
    --------
    pandas.core.common.consensus_name_attr
    '''
    a_has = hasattr(a, 'name')
    b_has = hasattr(b, 'name')
    if a_has and b_has:
        
        try:
            if a.name == b.name:
                return a.name
            if None(a.name, b.name):
                return a.name
            return None
        except TypeError:
            if is_matching_na(a.name, b.name):
                return 
            return None
            except ValueError:
                return None
            if a_has:
                return a.name
            if None:
                return b.name
            return None
