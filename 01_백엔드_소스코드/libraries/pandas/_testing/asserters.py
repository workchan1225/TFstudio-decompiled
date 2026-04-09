# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: asserters.pyc (Python 3.11)

from __future__ import annotations
import operator
from typing import TYPE_CHECKING, Literal, NoReturn, cast
import warnings
import numpy as np
from pandas._libs import lib
from pandas._libs.missing import is_matching_na
from pandas._libs.sparse import SparseIndex

testing
from pandas._libs.tslibs.np_datetime import compare_mismatched_resolutions
import pandas._libs.testing, _libs
from pandas.errors import Pandas4Warning
from pandas.util._decorators import deprecate_kwarg, set_module
from pandas.core.dtypes.common import is_bool, is_float_dtype, is_integer_dtype, is_number, is_numeric_dtype, needs_i8_conversion
from pandas.core.dtypes.dtypes import CategoricalDtype, DatetimeTZDtype, ExtensionDtype, NumpyEADtype
from pandas.core.dtypes.missing import array_equivalent
import pandas as pd
from pandas import Categorical, DataFrame, DatetimeIndex, Index, IntervalDtype, IntervalIndex, MultiIndex, PeriodIndex, RangeIndex, Series, TimedeltaIndex
from pandas.core.arrays import DatetimeArray, ExtensionArray, IntervalArray, PeriodArray, TimedeltaArray
from pandas.core.arrays.datetimelike import DatetimeLikeArrayMixin
from pandas.core.arrays.string_ import StringDtype
from pandas.core.indexes.api import safe_sort_index
from pandas.io.formats.printing import pprint_thing
if TYPE_CHECKING:
    from pandas._typing import DtypeObj

def assert_almost_equal(left = None, right = None, check_dtype = None, rtol = ('equiv', 1e-05, 1e-08), atol = ('check_dtype', "bool | Literal['equiv']", 'rtol', 'float', 'atol', 'float', 'return', 'None'), **kwargs):
    """
    Check that the left and right objects are approximately equal.

    By approximately equal, we refer to objects that are numbers or that
    contain numbers which may be equivalent to specific levels of precision.

    Parameters
    ----------
    left : object
    right : object
    check_dtype : bool or {'equiv'}, default 'equiv'
        Check dtype if both a and b are the same type. If 'equiv' is passed in,
        then `RangeIndex` and `Index` with int64 dtype are also considered
        equivalent when doing type checking.
    rtol : float, default 1e-5
        Relative tolerance.
    atol : float, default 1e-8
        Absolute tolerance.
    """
    pass
# WARNING: Decompyle incomplete


def _check_isinstance(left = None, right = None, cls = None):
    '''
    Helper method for our assert_* methods that ensures that
    the two objects being compared have the right type before
    proceeding with the comparison.

    Parameters
    ----------
    left : The first object being compared.
    right : The second object being compared.
    cls : The class type to check against.

    Raises
    ------
    AssertionError : Either `left` or `right` is not an instance of `cls`.
    '''
    cls_name = cls.__name__
    if not isinstance(left, cls):
        raise AssertionError(f'''{cls_name} Expected type {cls}, found {type(left)} instead''')
    if not isinstance(right, cls):
        raise AssertionError(f'''{cls_name} Expected type {cls}, found {type(right)} instead''')


def assert_dict_equal(left = None, right = None, compare_keys = None):
    _check_isinstance(left, right, dict)
    _testing.assert_dict_equal(left, right, compare_keys = compare_keys)

assert_index_equal = (lambda left, right, exact, check_names, check_exact, check_categorical = None, check_order = None, rtol = set_module('pandas.testing'), atol = ('equiv', True, True, True, True, 1e-05, 1e-08, None), obj = ('left', 'Index', 'right', 'Index', 'exact', 'bool | str', 'check_names', 'bool', 'check_exact', 'bool', 'check_categorical', 'bool', 'check_order', 'bool', 'rtol', 'float', 'atol', 'float', 'obj', 'str | None', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()

def assert_class_equal(left = None, right = None, exact = None, obj = (True, 'Input')):
    '''
    Checks classes are equal.
    '''
    __tracebackhide__ = True
    
    def repr_class(x):
        if isinstance(x, Index):
            return x
        return None(x).__name__

    
    def is_class_equiv(idx = None):
