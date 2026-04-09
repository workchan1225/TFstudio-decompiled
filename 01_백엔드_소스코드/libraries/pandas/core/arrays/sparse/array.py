# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: array.pyc (Python 3.11)

'''
SparseArray data structure
'''
from __future__ import annotations
from collections import abc
import numbers
import operator
from typing import TYPE_CHECKING, Any, Literal, Self, cast, overload
import warnings
import numpy as np
from pandas._config.config import get_option
from pandas._libs import lib

sparse
from pandas._libs.sparse import BlockIndex, IntIndex, SparseIndex
IntIndex = IntIndex
SparseIndex = SparseIndex
import pandas._libs.sparse, _libs
from pandas._libs.tslibs import NaT
from pandas.compat.numpy import function as nv
from pandas.errors import PerformanceWarning
from pandas.util._decorators import doc, set_module
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import validate_bool_kwarg, validate_insert_loc
from pandas.core.dtypes.astype import astype_array
from pandas.core.dtypes.cast import find_common_type, maybe_box_datetimelike
from pandas.core.dtypes.common import is_bool_dtype, is_integer, is_list_like, is_object_dtype, is_scalar, is_string_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype, SparseDtype
from pandas.core.dtypes.generic import ABCIndex, ABCSeries
from pandas.core.dtypes.missing import isna, na_value_for_dtype, notna
from pandas.core import arraylike

algorithms
from pandas.core.arraylike import OpsMixin
import pandas.core.algorithms, core
from pandas.core.arrays import ExtensionArray
from pandas.core.base import PandasObject

common
from pandas.core.construction import ensure_wrapped_if_datetimelike, extract_array, sanitize_array
extract_array = extract_array
sanitize_array = sanitize_array
import pandas.core.common, core
from pandas.core.indexers import check_array_indexer, unpack_tuple_and_ellipses
from pandas.core.nanops import check_below_min_count
from pandas.io.formats import printing
if TYPE_CHECKING:
    from collections.abc import Callable, Sequence
    from types import EllipsisType
    from typing import Protocol, type_check_only
    from scipy.sparse import csc_array, csc_matrix
    _SparseMatrixLike = <NODE:12>()
    from pandas._typing import NumpySorter
    SparseIndexKind = Literal[('integer', 'block')]
    from pandas._typing import ArrayLike, AstypeArg, Axis, AxisInt, Dtype, NpDtype, PositionalIndexer, Scalar, ScalarIndexer, SequenceIndexer, npt
    from pandas import Series
_sparray_doc_kwargs = {
    'klass': 'SparseArray' }

def _get_fill(arr = None):
    '''
    Create a 0-dim ndarray containing the fill value

    Parameters
    ----------
    arr : SparseArray

    Returns
    -------
    fill_value : ndarray
        0-dim ndarray with just the fill value.

    Notes
    -----
    coerce fill_value to arr dtype if possible
    int64 SparseArray can have NaN as fill_value if there is no missing
    '''
    
    try:
        return np.asarray(arr.fill_value, dtype = arr.dtype.subtype)
    except ValueError:
        return 



def _sparse_array_op(left = None, right = None, op = None, name = ('left', 'SparseArray', 'right', 'SparseArray', 'op', 'Callable', 'name', 'str', 'return', 'SparseArray')):
