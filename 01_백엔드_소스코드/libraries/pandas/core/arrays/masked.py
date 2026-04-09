# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: masked.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Literal, Self, cast, overload
import warnings
import numpy as np
from pandas._config import is_nan_na, using_python_scalars
from pandas._libs import algos as libalgos, lib, missing as libmissing
from pandas._libs.tslibs import is_supported_dtype
from pandas.compat import IS64, is_platform_windows
from pandas.errors import AbstractMethodError
from pandas.core.dtypes.astype import astype_is_view
from pandas.core.dtypes.base import ExtensionDtype
from pandas.core.dtypes.cast import maybe_downcast_to_dtype
from pandas.core.dtypes.common import is_bool, is_integer_dtype, is_list_like, is_scalar, is_string_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import ArrowDtype, BaseMaskedDtype
from pandas.core.dtypes.missing import array_equivalent, is_valid_na_for_dtype, isna, notna
from pandas.core import algorithms as algos, arraylike, missing, nanops, ops
from pandas.core.algorithms import factorize_array, isin, map_array, mode, take
from pandas.core.array_algos import masked_accumulations, masked_reductions
from pandas.core.array_algos.quantile import quantile_with_mask
from pandas.core.array_algos.transforms import shift
from pandas.core.arraylike import OpsMixin
from pandas.core.arrays._utils import to_numpy_dtype_inference
from pandas.core.arrays.base import ExtensionArray
from pandas.core.construction import array as pd_array, ensure_wrapped_if_datetimelike, extract_array
from pandas.core.indexers import check_array_indexer, getitem_returns_view
from pandas.core.ops import invalid_comparison
from pandas.core.util.hashing import hash_array
if TYPE_CHECKING:
    from collections.abc import Callable
    from collections.abc import Iterator, Sequence
    from pandas import Series
    from pandas.core.arrays import BooleanArray
    from pandas._typing import NumpySorter, NumpyValueArrayLike, ArrayLike, AstypeArg, AxisInt, DtypeObj, FillnaOptions, InterpolateOptions, NpDtype, PositionalIndexer, Scalar, ScalarIndexer, SequenceIndexer, Shape, npt
    from pandas._libs.missing import NAType
    from pandas.core.arrays import FloatingArray
from pandas.compat.numpy import function as nv

class BaseMaskedArray(ExtensionArray, OpsMixin):
    pass
# WARNING: Decompyle incomplete


def transpose_homogeneous_masked_arrays(masked_arrays = None):
    '''Transpose masked arrays in a list, but faster.

    Input should be a list of 1-dim masked arrays of equal length and all have the
    same dtype. The caller is responsible for ensuring validity of input data.
    '''
    masked_arrays = list(masked_arrays)
    dtype = masked_arrays[0].dtype
    values = masked_arrays()
    transposed_values = np.concatenate(values, axis = 0, out = np.empty((len(masked_arrays), len(masked_arrays[0])), order = 'F', dtype = dtype.numpy_dtype))
    masks = masked_arrays()
    transposed_masks = np.concatenate(masks, axis = 0, out = np.empty_like(transposed_values, dtype = bool))
    arr_type = dtype.construct_array_type()
    transposed_arrays = []
    for i in range(transposed_values.shape[1]):
        transposed_arr = arr_type(transposed_values[(:, i)], mask = transposed_masks[(:, i)])
        transposed_arrays.append(transposed_arr)
        return transposed_arrays
