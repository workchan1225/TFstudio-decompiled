# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cast.pyc (Python 3.11)

'''
Routines for casting.
'''
from __future__ import annotations
import datetime as dt
import functools
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast, overload
import warnings
import numpy as np
from pandas._config import is_nan_na, using_python_scalars, using_string_dtype
from pandas._libs import Interval, Period, lib
from pandas._libs.missing import NA, NAType, checknull
from pandas._libs.tslibs import NaT, OutOfBoundsDatetime, OutOfBoundsTimedelta, Timedelta, Timestamp, is_supported_dtype
from pandas._libs.tslibs.timedeltas import array_to_timedelta64
from pandas.errors import IntCastingNaNError, LossySetitemError
from pandas.core.dtypes.common import ensure_int8, ensure_int16, ensure_int32, ensure_int64, ensure_object, ensure_str, is_bool, is_complex, is_float, is_integer, is_object_dtype, is_scalar, is_string_dtype, pandas_dtype as pandas_dtype_func
from pandas.core.dtypes.dtypes import ArrowDtype, BaseMaskedDtype, CategoricalDtype, DatetimeTZDtype, ExtensionDtype, IntervalDtype, PandasExtensionDtype, PeriodDtype
from pandas.core.dtypes.generic import ABCExtensionArray, ABCIndex, ABCSeries
from pandas.core.dtypes.inference import is_list_like
from pandas.core.dtypes.missing import is_valid_na_for_dtype, isna, na_value_for_dtype, notna
from pandas.io._util import _arrow_dtype_mapping
if TYPE_CHECKING:
    from collections.abc import Collection, Sequence
    from pandas._typing import ArrayLike, Dtype, DtypeObj, NumpyIndexT, Scalar, TimeUnit
    from pandas import Index
    from pandas.core.arrays import Categorical, DatetimeArray, ExtensionArray, IntervalArray, PeriodArray, TimedeltaArray
_int8_max = np.iinfo(np.int8).max
_int16_max = np.iinfo(np.int16).max
_int32_max = np.iinfo(np.int32).max
_dtype_obj = np.dtype(object)
NumpyArrayT = TypeVar('NumpyArrayT', bound = np.ndarray)

def maybe_convert_platform(values = None):
    '''try to do platform conversion, allow ndarray or list here'''
    if isinstance(values, (list, tuple, range)):
        arr = construct_1d_object_array_from_listlike(values)
    else:
        arr = values
    if arr.dtype == _dtype_obj:
        arr = cast(np.ndarray, arr)
        arr = lib.maybe_convert_objects(arr)
    return arr


def is_nested_object(obj = None):
