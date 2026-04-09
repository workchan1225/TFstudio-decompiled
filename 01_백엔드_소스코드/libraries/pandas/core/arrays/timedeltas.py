# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: timedeltas.pyc (Python 3.11)

from __future__ import annotations
from datetime import timedelta
import operator
from typing import TYPE_CHECKING, Self, cast
import numpy as np
from pandas._libs import lib, tslibs
from pandas._libs.tslibs import Day, NaT, NaTType, Tick, Timedelta, astype_overflowsafe, get_supported_dtype, iNaT, is_supported_dtype, periods_per_second, to_offset
from pandas._libs.tslibs.conversion import cast_from_unit_vectorized
from pandas._libs.tslibs.fields import get_timedelta_days, get_timedelta_field
from pandas._libs.tslibs.timedeltas import array_to_timedelta64, floordiv_object_array, ints_to_pytimedelta, parse_timedelta_unit, truediv_object_array
from pandas.compat.numpy import function as nv
from pandas.util._decorators import set_module
from pandas.util._validators import validate_endpoints
from pandas.core.dtypes.common import TD64NS_DTYPE, is_float_dtype, is_integer_dtype, is_object_dtype, is_scalar, is_string_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import ArrowDtype, BaseMaskedDtype, ExtensionDtype
from pandas.core.dtypes.missing import isna
from pandas.core import nanops, roperator
from pandas.core.array_algos import datetimelike_accumulations
from pandas.core.arrays import datetimelike as dtl
from pandas.core.arrays._ranges import generate_regular_range

common
from pandas.core.ops.common import unpack_zerodim_and_defer
import pandas.core.common, core
if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    from pandas._typing import AxisInt, DateTimeErrorChoices, DtypeObj, NpDtype, npt, TimeUnit
    from pandas import DataFrame
import textwrap

def _field_accessor(name = None, alias = None, docstring = None):
    pass
# WARNING: Decompyle incomplete

TimedeltaArray = <NODE:12>()

def sequence_to_td64ns(data = None, copy = None, unit = set_module('pandas.arrays'), errors = (False, None, 'raise')):
    '''
    Parameters
    ----------
    data : list-like
    copy : bool, default False
    unit : str, optional
        The timedelta unit to treat integers as multiples of. For numeric
        data this defaults to ``\'ns\'``.
        Must be un-specified if the data contains a str and ``errors=="raise"``.
    errors : {"raise", "coerce", "ignore"}, default "raise"
        How to handle elements that cannot be converted to timedelta64[ns].
        See ``pandas.to_timedelta`` for details.

    Returns
    -------
    converted : numpy.ndarray
        The sequence converted to a numpy array with dtype ``timedelta64[ns]``.
    inferred_freq : Tick, Day, or None
        The inferred frequency of the sequence.

    Raises
    ------
    ValueError : Data cannot be converted to timedelta64[ns].

    Notes
    -----
    Unlike `pandas.to_timedelta`, if setting ``errors=ignore`` will not cause
    errors to be ignored; they are caught and subsequently ignored at a
    higher level.
    '''
    pass
# WARNING: Decompyle incomplete


def _ints_to_td64ns(data = None, unit = None):
    '''
    Convert an ndarray with integer-dtype to timedelta64[ns] dtype, treating
    the integers as multiples of the given timedelta unit.

    Parameters
    ----------
    data : numpy.ndarray with integer-dtype
    unit : str, default "ns"
        The timedelta unit to treat integers as multiples of.

    Returns
    -------
    numpy.ndarray : timedelta64[ns] array converted from data
    bool : whether a copy was made
    '''
    copy_made = False
# WARNING: Decompyle incomplete


def _objects_to_td64ns(data = None, unit = None, errors = None):
    '''
    Convert an object-dtyped or string-dtyped array into a
    timedelta64[ns]-dtyped array.

    Parameters
    ----------
    data : ndarray or Index
    unit : str, default "ns"
        The timedelta unit to treat integers as multiples of.
        Must not be specified if the data contains a str.
    errors : {"raise", "coerce", "ignore"}, default "raise"
        How to handle elements that cannot be converted to timedelta64[ns].
        See ``pandas.to_timedelta`` for details.

    Returns
    -------
    numpy.ndarray : timedelta64[ns] array converted from data

    Raises
    ------
    ValueError : Data cannot be converted to timedelta64[ns].

    Notes
    -----
    Unlike `pandas.to_timedelta`, if setting `errors=ignore` will not cause
    errors to be ignored; they are caught and subsequently ignored at a
    higher level.
    '''
    values = np.asarray(data, dtype = np.object_)
    result = array_to_timedelta64(values, unit = unit, errors = errors)
    return result


def _validate_td64_dtype(dtype = None):
    dtype = pandas_dtype(dtype)
    if dtype == np.dtype('m8'):
        msg = "Passing in 'timedelta' dtype with no precision is not allowed. Please pass in 'timedelta64[ns]' instead."
        raise ValueError(msg)
    if not lib.is_np_dtype(dtype, 'm'):
        raise ValueError(f'''dtype \'{dtype}\' is invalid, should be np.timedelta64 dtype''')
    if not is_supported_dtype(dtype):
        raise ValueError("Supported timedelta64 resolutions are 's', 'ms', 'us', 'ns'")
    return dtype
