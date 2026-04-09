# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: align.pyc (Python 3.11)

'''
Core eval alignment algorithms.
'''
from __future__ import annotations
from functools import partial, wraps
from typing import TYPE_CHECKING
import warnings
import numpy as np
from pandas._config.config import get_option
from pandas.errors import PerformanceWarning
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.base import PandasObject

common
from pandas.core.computation.common import result_type_many
import pandas.core.common, core
if TYPE_CHECKING:
    from collections.abc import Callable, Sequence
    from pandas._typing import F
    from pandas.core.generic import NDFrame
    from pandas.core.indexes.api import Index

def _align_core_single_unary_op(term = None):
    axes = None
    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype = term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, 'axes'):
            axes = _zip_axes_from_type(typ, term.value.axes)
    return (typ, axes)


def _zip_axes_from_type(typ = None, new_axes = None):
    pass
# WARNING: Decompyle incomplete


def _any_pandas_objects(terms = None):
    '''
    Check a sequence of terms for instances of PandasObject.
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(terms())


def _filter_special_cases(f = None):
    pass
# WARNING: Decompyle incomplete

_align_core = (lambda terms: pass# WARNING: Decompyle incomplete
)()

def align_terms(terms):
    '''
    Align a set of terms.
    '''
    
    try:
        terms = list(com.flatten(terms))
    except TypeError:
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return 
        return 

# WARNING: Decompyle incomplete


def reconstruct_object(typ, obj, axes, dtype, name):
    '''
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    '''
    
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)
# WARNING: Decompyle incomplete
