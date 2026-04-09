# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _mixins.pyc (Python 3.11)

from __future__ import annotations
from functools import wraps
from typing import TYPE_CHECKING, Any, Literal, Self, cast, overload
import numpy as np
from pandas._libs import lib
from pandas._libs.arrays import NDArrayBacked
from pandas._libs.tslibs import is_supported_dtype
from pandas._typing import ArrayLike, AxisInt, Dtype, F, FillnaOptions, PositionalIndexer2D, PositionalIndexerTuple, ScalarIndexer, SequenceIndexer, Shape, TakeIndexer, npt
from pandas.errors import AbstractMethodError
from pandas.util._decorators import doc
from pandas.util._validators import validate_bool_kwarg, validate_insert_loc
from pandas.core.dtypes.common import pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype, ExtensionDtype, PeriodDtype
from pandas.core.dtypes.missing import array_equivalent
from pandas.core import missing
from pandas.core.algorithms import take, unique, value_counts_internal as value_counts
from pandas.core.array_algos.quantile import quantile_with_mask
from pandas.core.array_algos.transforms import shift
from pandas.core.arrays.base import ExtensionArray
from pandas.core.construction import extract_array
from pandas.core.indexers import check_array_indexer, getitem_returns_view
from pandas.core.sorting import nargminmax
if TYPE_CHECKING:
    from collections.abc import Sequence
    from pandas._typing import NumpySorter, NumpyValueArrayLike
    from pandas import Series

def ravel_compat(meth = None):
    '''
    Decorator to ravel a 2D array before passing it to a cython operation,
    then reshape the result to our own shape.
    '''
    pass
# WARNING: Decompyle incomplete


class NDArrayBackedExtensionArray(ExtensionArray, NDArrayBacked):
    pass
# WARNING: Decompyle incomplete
