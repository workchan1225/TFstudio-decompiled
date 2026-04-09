# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: range.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable, Hashable, Iterator
from datetime import timedelta
import operator
from sys import getsizeof
from typing import TYPE_CHECKING, Any, Literal, Self, cast, overload
import numpy as np
from pandas._libs import index as libindex, lib
from pandas._libs.lib import no_default
from pandas.compat.numpy import function as nv
from pandas.util._decorators import cache_readonly, set_module
from pandas.core.dtypes.base import ExtensionDtype
from pandas.core.dtypes.common import ensure_platform_int, ensure_python_int, is_float, is_integer, is_scalar, is_signed_integer_dtype
from pandas.core.dtypes.generic import ABCTimedeltaIndex
from pandas.core import ops

common
from pandas.core.construction import extract_array
import pandas.core.common, core
from pandas.core.indexers import check_array_indexer


base
from pandas.core.indexes.base import Index, maybe_extract_name
maybe_extract_name = maybe_extract_name
import pandas.core.indexes.base, core, indexes
from pandas.core.ops.common import unpack_zerodim_and_defer
if TYPE_CHECKING:
    from pandas._typing import Axis, Dtype, JoinHow, NaPosition, NumpySorter, npt
    from pandas import Series
_empty_range = range(0)
_dtype_int64 = np.dtype(np.int64)

def min_fitting_element(start = None, step = None, lower_limit = None):
    '''Returns the smallest element greater than or equal to the limit'''
    no_steps = -(-(lower_limit - start) // abs(step))
    return start + abs(step) * no_steps

RangeIndex = <NODE:12>()
