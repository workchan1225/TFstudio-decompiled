# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

'''
Common type operations.
'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any
import warnings
import numpy as np
from pandas._config import using_string_dtype
from pandas._libs import Interval, Period, algos, lib
from pandas._libs.tslibs import conversion
from pandas.errors import Pandas4Warning
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.base import _registry as registry
from pandas.core.dtypes.dtypes import CategoricalDtype, DatetimeTZDtype, ExtensionDtype, IntervalDtype, PeriodDtype, SparseDtype
from pandas.core.dtypes.generic import ABCIndex
from pandas.core.dtypes.inference import is_array_like, is_bool, is_complex, is_dataclass, is_decimal, is_dict_like, is_file_like, is_float, is_hashable, is_integer, is_iterator, is_list_like, is_named_tuple, is_nested_list_like, is_number, is_re, is_re_compilable, is_scalar, is_sequence
if TYPE_CHECKING:
    from collections.abc import Callable
    from pandas._typing import ArrayLike, DtypeObj
DT64NS_DTYPE = conversion.DT64NS_DTYPE
TD64NS_DTYPE = conversion.TD64NS_DTYPE
INT64_DTYPE = np.dtype(np.int64)
_is_scipy_sparse: 'Callable[[ArrayLike], bool] | None' = None
ensure_float64 = algos.ensure_float64
ensure_int64 = algos.ensure_int64
ensure_int32 = algos.ensure_int32
ensure_int16 = algos.ensure_int16
ensure_int8 = algos.ensure_int8
ensure_platform_int = algos.ensure_platform_int
ensure_object = algos.ensure_object
ensure_uint64 = algos.ensure_uint64

def ensure_str(value = None):
    '''
    Ensure that bytes and non-strings get converted into ``str`` objects.
    '''
    if isinstance(value, bytes):
        value = value.decode('utf-8')
    elif not isinstance(value, str):
        value = str(value)
    return value


def ensure_python_int(value = None):
    """
    Ensure that a value is a python int.

    Parameters
    ----------
    value: int or numpy.integer

    Returns
    -------
    int

    Raises
    ------
    TypeError: if the value isn't an int or can't be converted to one.
    """
    if not is_integer(value) and is_float(value):
        if not is_scalar(value):
            raise TypeError(f'''Value needs to be a scalar value, was type {type(value).__name__}''')
        raise TypeError(f'''Wrong type {type(value)} for value {value}''')
# WARNING: Decompyle incomplete


def classes(*klasses):
    '''Evaluate if the tipo is a subclass of the klasses.'''
    pass
# WARNING: Decompyle incomplete


def _classes_and_not_datetimelike(*klasses):
    '''
    Evaluate if the tipo is a subclass of the klasses
    and not a datetimelike.
    '''
    pass
# WARNING: Decompyle incomplete

is_object_dtype = (lambda arr_or_dtype = None: _is_dtype_type(arr_or_dtype, classes(np.object_)))()
is_sparse = (lambda arr = None: warnings.warn('is_sparse is deprecated and will be removed in a future version. Check `isinstance(dtype, pd.SparseDtype)` instead.', Pandas4Warning, stacklevel = 2)dtype = getattr(arr, 'dtype', arr)isinstance(dtype, SparseDtype))()

def is_scipy_sparse(arr = None):
    '''
    Check whether an array-like is a scipy.sparse.spmatrix instance.

    Parameters
    ----------
    arr : array-like
        The array-like to check.

    Returns
    -------
    boolean
        Whether or not the array-like is a scipy.sparse.spmatrix instance.

    Notes
    -----
    If scipy is not installed, this function will always return False.

    Examples
    --------
    >>> from scipy.sparse import bsr_matrix
    >>> is_scipy_sparse(bsr_matrix([1, 2, 3]))
    True
    >>> is_scipy_sparse(pd.arrays.SparseArray([1, 2, 3]))
    False
    '''
    pass
# WARNING: Decompyle incomplete

is_datetime64_dtype = (lambda arr_or_dtype = None: if isinstance(arr_or_dtype, np.dtype):
arr_or_dtype.kind == 'M'None(arr_or_dtype, classes(np.datetime64)))()
is_datetime64tz_dtype = (lambda arr_or_dtype = None: warnings.warn('is_datetime64tz_dtype is deprecated and will be removed in a future version. Check `isinstance(dtype, pd.DatetimeTZDtype)` instead.', Pandas4Warning, stacklevel = 2)if isinstance(arr_or_dtype, DatetimeTZDtype):
True# WARNING: Decompyle incomplete
)()
is_timedelta64_dtype = (lambda arr_or_dtype = None: if isinstance(arr_or_dtype, np.dtype):
arr_or_dtype.kind == 'm'None(arr_or_dtype, classes(np.timedelta64)))()
is_period_dtype = (lambda arr_or_dtype = None: warnings.warn('is_period_dtype is deprecated and will be removed in a future version. Use `isinstance(dtype, pd.PeriodDtype)` instead', Pandas4Warning, stacklevel = 2)if isinstance(arr_or_dtype, ExtensionDtype):
arr_or_dtype.type is Period# WARNING: Decompyle incomplete
)()
is_interval_dtype = (lambda arr_or_dtype = None: warnings.warn('is_interval_dtype is deprecated and will be removed in a future version. Use `isinstance(dtype, pd.IntervalDtype)` instead', Pandas4Warning, stacklevel = 2)if isinstance(arr_or_dtype, ExtensionDtype):
arr_or_dtype.type is Interval# WARNING: Decompyle incomplete
)()
is_categorical_dtype = (lambda arr_or_dtype = None: warnings.warn('is_categorical_dtype is deprecated and will be removed in a future version. Use isinstance(dtype, pd.CategoricalDtype) instead', Pandas4Warning, stacklevel = 2)if isinstance(arr_or_dtype, ExtensionDtype):
arr_or_dtype.name == 'category'# WARNING: Decompyle incomplete
)()

def is_string_or_object_np_dtype(dtype = None):
