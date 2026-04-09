# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: interval.pyc (Python 3.11)

from __future__ import annotations
import operator
from operator import le, lt
import textwrap
from typing import TYPE_CHECKING, Literal, Self, TypeAlias, overload
import numpy as np
from pandas._libs import lib
from pandas._libs.interval import VALID_CLOSED, Interval, IntervalMixin, intervals_to_interval_bounds
from pandas._libs.missing import NA
from pandas._typing import ArrayLike, AxisInt, Dtype, IntervalClosedType, NpDtype, PositionalIndexer, ScalarIndexer, SequenceIndexer, SortKind, TimeArrayLike, npt
from pandas.compat.numpy import function as nv
from pandas.errors import IntCastingNaNError
from pandas.util._decorators import set_module
from pandas.core.dtypes.cast import LossySetitemError, maybe_upcast_numeric_to_64bit
from pandas.core.dtypes.common import is_float_dtype, is_integer_dtype, is_list_like, is_object_dtype, is_scalar, is_string_dtype, needs_i8_conversion, pandas_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype, IntervalDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCDatetimeIndex, ABCIntervalIndex, ABCPeriodIndex
from pandas.core.dtypes.missing import is_valid_na_for_dtype, isna, notna
from pandas.core.algorithms import isin, take, unique
from pandas.core.arrays import ArrowExtensionArray
from pandas.core.arrays.base import ExtensionArray
from pandas.core.arrays.datetimes import DatetimeArray
from pandas.core.arrays.timedeltas import TimedeltaArray

common
from pandas.core.construction import array, ensure_wrapped_if_datetimelike, extract_array
ensure_wrapped_if_datetimelike = ensure_wrapped_if_datetimelike
extract_array = extract_array
import pandas.core.common, core
from pandas.core.indexers import check_array_indexer, getitem_returns_view
from pandas.core.ops import invalid_comparison, unpack_zerodim_and_defer
if TYPE_CHECKING:
    from collections.abc import Callable, Iterator, Sequence
    from pandas import Index
IntervalSide: 'TypeAlias' = TimeArrayLike | np.ndarray
IntervalOrNA: 'TypeAlias' = Interval | float
_interval_shared_docs: 'dict[str, str]' = { }
_shared_docs_kwargs = {
    'klass': 'IntervalArray',
    'qualname': 'arrays.IntervalArray',
    'name': '' }
_interval_shared_docs['class'] = "\n%(summary)s\n\nParameters\n----------\ndata : array-like (1-dimensional)\n    Array-like (ndarray, :class:`DateTimeArray`, :class:`TimeDeltaArray`) containing\n    Interval objects from which to build the %(klass)s.\nclosed : {'left', 'right', 'both', 'neither'}, default 'right'\n    Whether the intervals are closed on the left-side, right-side, both or\n    neither.\ndtype : dtype or None, default None\n    If None, dtype will be inferred.\ncopy : bool, default False\n    Copy the input data.\n%(name)sverify_integrity : bool, default True\n    Verify that the %(klass)s is valid.\n\nAttributes\n----------\nleft\nright\nclosed\nmid\nlength\nis_empty\nis_non_overlapping_monotonic\n%(extra_attributes)s\nMethods\n-------\nfrom_arrays\nfrom_tuples\nfrom_breaks\ncontains\noverlaps\nset_closed\nto_tuples\n%(extra_methods)s\nSee Also\n--------\nIndex : The base pandas Index type.\nInterval : A bounded slice-like interval; the elements of an %(klass)s.\ninterval_range : Function to create a fixed frequency IntervalIndex.\ncut : Bin values into discrete Intervals.\nqcut : Bin values into equal-sized Intervals based on rank or sample quantiles.\n\nNotes\n-----\nSee the `user guide\n<https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#intervalindex>`__\nfor more.\n\n%(examples)s"
IntervalArray = <NODE:12>()

def _maybe_convert_platform_interval(values = None):
    '''
    Try to do platform conversion, with special casing for IntervalArray.
    Wrapper around maybe_convert_platform that alters the default return
    dtype in certain cases to be compatible with IntervalArray.  For example,
    empty lists return with integer dtype instead of object dtype, which is
    prohibited for IntervalArray.

    Parameters
    ----------
    values : array-like

    Returns
    -------
    array
    '''
    if isinstance(values, (list, tuple)) and len(values) == 0:
        return np.array([], dtype = np.int64)
    if None(values) or isinstance(values, ABCDataFrame):
        return values
    if None(getattr(values, 'dtype', None), CategoricalDtype):
        values = np.asarray(values)
    elif not hasattr(values, 'dtype') and isinstance(values, (list, tuple, range)):
        return values
    values = extract_array(values, extract_numpy = True)
    if not hasattr(values, 'dtype'):
        values = np.asarray(values)
        if values.dtype.kind in 'iu' and values.dtype != np.int64:
            values = values.astype(np.int64)
    return values
