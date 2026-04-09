# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numeric.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Literal
import numpy as np
from pandas._libs import lib, missing as libmissing
from pandas._libs.tslibs import Timedelta, Timestamp
from pandas.util._decorators import set_module
from pandas.util._validators import check_dtype_backend
from pandas.core.dtypes.cast import maybe_downcast_numeric
from pandas.core.dtypes.common import ensure_object, is_bool_dtype, is_decimal, is_integer_dtype, is_number, is_numeric_dtype, is_scalar, is_string_dtype, needs_i8_conversion
from pandas.core.dtypes.dtypes import ArrowDtype
from pandas.core.dtypes.generic import ABCIndex, ABCSeries
from pandas.core.arrays import BaseMaskedArray
from pandas.core.arrays.string_ import StringDtype
if TYPE_CHECKING:
    from pandas._typing import DateTimeErrorChoices, DtypeBackend, npt
to_numeric = (lambda arg = None, errors = None, downcast = set_module('pandas'), dtype_backend = ('raise', None, lib.no_default): if downcast not in (None, 'integer', 'signed', 'unsigned', 'float'):
raise ValueError('invalid downcasting method provided')if errors not in ('raise', 'coerce'):
raise ValueError('invalid error value specified')check_dtype_backend(dtype_backend)is_series = Falseis_index = Falseis_scalars = Falseif isinstance(arg, ABCSeries):
is_series = Truevalues = arg.valueselif isinstance(arg, ABCIndex):
is_index = Trueif needs_i8_conversion(arg.dtype):
values = arg.view('i8')else:
values = arg.valueselif isinstance(arg, (list, tuple)):
values = np.array(arg, dtype = 'O')elif is_scalar(arg):
if is_decimal(arg):
float(arg)if None(arg):
argif None(arg, (Timedelta, Timestamp)):
arg._valueis_scalars = Nonevalues = np.array([
arg], dtype = 'O')elif getattr(arg, 'ndim', 1) > 1:
raise TypeError('arg must be a list, tuple, 1-d array, or Series')values = argmask = Noneif isinstance(values, BaseMaskedArray):
mask = values._maskvalues = values._data[~mask]values_dtype = getattr(values, 'dtype', None)if isinstance(values_dtype, ArrowDtype):
mask = values.isna()values = values.dropna().to_numpy()new_mask = Noneif is_numeric_dtype(values_dtype):
passelif lib.is_np_dtype(values_dtype, 'mM'):
values = values.view(np.int64)# WARNING: Decompyle incomplete
)()
