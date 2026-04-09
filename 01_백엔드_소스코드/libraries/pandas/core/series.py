# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: series.pyc (Python 3.11)

'''
Data structure for 1-dimensional cross-sectional and time series data
'''
from __future__ import annotations
from collections.abc import Callable, Hashable, Iterable, Mapping, Sequence
import functools
import operator
import sys
from textwrap import dedent
from typing import IO, TYPE_CHECKING, Any, Literal, Self, cast, overload
import warnings
import numpy as np
from pandas._libs import lib, properties, reshape
from pandas._libs.lib import is_range_indexer
from pandas.compat import CHAINED_WARNING_DISABLED
from pandas.compat._constants import REF_COUNT, REF_COUNT_METHOD
from pandas.compat._optional import import_optional_dependency
from pandas.compat.numpy import function as nv
from pandas.errors import ChainedAssignmentError, InvalidIndexError, Pandas4Warning
from pandas.errors.cow import _chained_assignment_method_update_msg, _chained_assignment_msg
from pandas.util._decorators import Appender, deprecate_nonkeyword_arguments, doc, set_module
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import validate_ascending, validate_bool_kwarg, validate_percentile
from pandas.core.dtypes.astype import astype_is_view
from pandas.core.dtypes.cast import LossySetitemError, construct_1d_arraylike_from_scalar, find_common_type, infer_dtype_from, maybe_box_native, maybe_unbox_numpy_scalar
from pandas.core.dtypes.common import is_dict_like, is_float, is_integer, is_iterator, is_list_like, is_object_dtype, is_scalar, pandas_dtype, validate_all_hashable
from pandas.core.dtypes.dtypes import ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.dtypes.inference import is_hashable
from pandas.core.dtypes.missing import isna, na_value_for_dtype, notna, remove_na_arraylike
from pandas.core import algorithms, base, common as com, nanops, ops, roperator
from pandas.core.accessor import Accessor
from pandas.core.apply import SeriesApply
from pandas.core.arrays import ExtensionArray
from pandas.core.arrays.arrow import ListAccessor, StructAccessor
from pandas.core.arrays.categorical import CategoricalAccessor
from pandas.core.arrays.sparse import SparseAccessor
from pandas.core.construction import array as pd_array, extract_array, sanitize_array
from pandas.core.generic import NDFrame
from pandas.core.indexers import disallow_ndim_indexing, unpack_1tuple
from pandas.core.indexes.accessors import CombinedDatetimelikeProperties
from pandas.core.indexes.api import DatetimeIndex, Index, MultiIndex, PeriodIndex, default_index, ensure_index, maybe_sequence_to_range


base
from pandas.core.indexes.multi import maybe_droplevels
import pandas.core.indexes.base, core, indexes
from pandas.core.indexing import check_bool_indexer, check_dict_or_set_indexers
from pandas.core.internals import SingleBlockManager
from pandas.core.methods import selectn
from pandas.core.shared_docs import _shared_docs
from pandas.core.sorting import ensure_key_mapped, nargsort
from pandas.core.strings.accessor import StringMethods
from pandas.core.tools.datetimes import to_datetime


format
from pandas.io.formats.info import SeriesInfo
import pandas.io.formats.format, io, formats
import pandas.plotting as pandas
if TYPE_CHECKING:
    from pandas._libs.internals import BlockValuesRefs
    from pandas._typing import AggFuncType, AnyAll, AnyArrayLike, ArrayLike, ArrowArrayExportable, ArrowStreamExportable, Axis, AxisInt, CorrelationMethod, DropKeep, Dtype, DtypeObj, FilePath, Frequency, IgnoreRaise, IndexKeyFunc, IndexLabel, Level, ListLike, MutableMappingT, NaPosition, NumpySorter, NumpyValueArrayLike, QuantileInterpolation, ReindexMethod, Renamer, Scalar, SortKind, StorageOptions, Suffixes, ValueKeyFunc, WriteBuffer, npt
    from pandas.core.frame import DataFrame
    from pandas.core.groupby.generic import SeriesGroupBy
__all__ = [
    'Series']
_shared_doc_kwargs = {
    'axes': 'index',
    'klass': 'Series',
    'axes_single_arg': "{0 or 'index'}",
    'axis': "axis : {0 or 'index'}\n        Unused. Parameter needed for compatibility with DataFrame.",
    'inplace': 'inplace : bool, default False\n        If True, performs operation inplace and returns None.',
    'unique': 'np.ndarray',
    'duplicated': 'Series',
    'optional_by': '',
    'optional_reindex': '\nindex : array-like, optional\n    New labels for the index. Preferably an Index object to avoid\n    duplicating data.\naxis : int or str, optional\n    Unused.' }
Series = <NODE:12>()
