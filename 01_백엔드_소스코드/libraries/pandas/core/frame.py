# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: frame.pyc (Python 3.11)

'''
DataFrame
---------
An efficient 2D container for potentially mixed-type time series or other
labeled data series.

Similar to its R counterpart, data.frame, except providing automatic data
alignment and a host of useful data manipulation methods having to do with the
labeling information
'''
from __future__ import annotations
import collections
from collections import abc
from collections.abc import Callable, Hashable, Iterable, Iterator, Mapping, Sequence
import functools
from io import StringIO
import itertools
import operator
import sys
from textwrap import dedent
from typing import TYPE_CHECKING, Any, Literal, Self, cast, overload
import warnings
import numpy as np
from numpy import ma
from pandas._config import get_option
from pandas._libs import algos as libalgos, lib, properties
from pandas._libs.hashtable import duplicated
from pandas._libs.lib import is_range_indexer
from pandas.compat import CHAINED_WARNING_DISABLED
from pandas.compat._constants import REF_COUNT, REF_COUNT_METHOD
from pandas.compat._optional import import_optional_dependency
from pandas.compat.numpy import function as nv
from pandas.errors import ChainedAssignmentError, InvalidIndexError, Pandas4Warning
from pandas.errors.cow import _chained_assignment_method_update_msg, _chained_assignment_msg
from pandas.util._decorators import Appender, Substitution, deprecate_nonkeyword_arguments, set_module
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import validate_ascending, validate_bool_kwarg, validate_percentile
from pandas.core.dtypes.cast import LossySetitemError, can_hold_element, construct_1d_arraylike_from_scalar, construct_2d_arraylike_from_scalar, find_common_type, infer_dtype_from_scalar, invalidate_string_dtypes, maybe_downcast_to_dtype, maybe_unbox_numpy_scalar
from pandas.core.dtypes.common import infer_dtype_from_object, is_1d_only_ea_dtype, is_array_like, is_bool_dtype, is_dataclass, is_dict_like, is_float, is_float_dtype, is_hashable, is_integer, is_integer_dtype, is_iterator, is_list_like, is_scalar, is_sequence, is_string_dtype, needs_i8_conversion, pandas_dtype
from pandas.core.dtypes.concat import concat_compat
from pandas.core.dtypes.dtypes import ArrowDtype, BaseMaskedDtype, ExtensionDtype
from pandas.core.dtypes.generic import ABCIndex, ABCSeries
from pandas.core.dtypes.missing import isna, notna
from pandas.core import algorithms, common as com, nanops, ops, roperator
from pandas.core.accessor import Accessor
from pandas.core.apply import reconstruct_and_relabel_result
from pandas.core.array_algos.take import take_2d_multi
from pandas.core.arraylike import OpsMixin
from pandas.core.arrays import BaseMaskedArray, DatetimeArray, ExtensionArray, PeriodArray, TimedeltaArray
from pandas.core.arrays.sparse import SparseFrameAccessor
from pandas.core.arrays.string_ import StringDtype
from pandas.core.construction import ensure_wrapped_if_datetimelike, sanitize_array, sanitize_masked_array
from pandas.core.generic import NDFrame
from pandas.core.indexers import check_key_length
from pandas.core.indexes.api import DatetimeIndex, Index, PeriodIndex, default_index, ensure_index, ensure_index_from_sequences
from pandas.core.indexes.multi import MultiIndex, maybe_droplevels
from pandas.core.indexing import check_bool_indexer, check_dict_or_set_indexers
from pandas.core.internals import BlockManager
from pandas.core.internals.construction import arrays_to_mgr, dataclasses_to_dicts, dict_to_mgr, ndarray_to_mgr, nested_data_to_arrays, rec_array_to_mgr, reorder_arrays, to_arrays, treat_as_nested
from pandas.core.methods import selectn
from pandas.core.reshape.melt import melt
from pandas.core.series import Series
from pandas.core.shared_docs import _shared_docs
from pandas.core.sorting import get_group_index, lexsort_indexer, nargsort
from pandas.io.common import get_handle
from pandas.io.formats import console, format as fmt
from pandas.io.formats.info import DataFrameInfo
import pandas.plotting as pandas
if TYPE_CHECKING:
    import datetime
    from pandas._libs.internals import BlockValuesRefs
    from pandas._typing import AggFuncType, AnyAll, AnyArrayLike, ArrayLike, ArrowArrayExportable, ArrowStreamExportable, Axes, Axis, AxisInt, ColspaceArgType, CompressionOptions, CorrelationMethod, DropKeep, Dtype, DtypeObj, FilePath, FloatFormatType, FormattersType, Frequency, FromDictOrient, HashableT, HashableT2, IgnoreRaise, IndexKeyFunc, IndexLabel, JoinValidate, Level, ListLike, MergeHow, MergeValidate, MutableMappingT, NaPosition, NsmallestNlargestKeep, ParquetCompressionOptions, PythonFuncType, QuantileInterpolation, ReadBuffer, ReindexMethod, Renamer, Scalar, SequenceNotStr, SortKind, StorageOptions, Suffixes, T, ToStataByteorder, ToTimestampHow, UpdateJoin, ValueKeyFunc, WriteBuffer, XMLParsers, npt
    from pandas.core.groupby.generic import DataFrameGroupBy
    from pandas.core.interchange.dataframe_protocol import DataFrame as DataFrameXchg
    from pandas.core.internals.managers import SingleBlockManager
    from pandas.io.formats.style import Styler
_shared_doc_kwargs = {
    'axes': 'index, columns',
    'klass': 'DataFrame',
    'axes_single_arg': "{0 or 'index', 1 or 'columns'}",
    'axis': "axis : {0 or 'index', 1 or 'columns'}, default 0\n        If 0 or 'index': apply function to each column.\n        If 1 or 'columns': apply function to each row.",
    'inplace': '\n    inplace : bool, default False\n        Whether to modify the DataFrame rather than creating a new one.',
    'optional_by': "\nby : str or list of str\n    Name or list of names to sort by.\n\n    - if `axis` is 0 or `'index'` then `by` may contain index\n      levels and/or column labels.\n    - if `axis` is 1 or `'columns'` then `by` may contain column\n      levels and/or index labels.",
    'optional_reindex': "\nlabels : array-like, optional\n    New labels / index to conform the axis specified by 'axis' to.\nindex : array-like, optional\n    New labels for the index. Preferably an Index object to avoid\n    duplicating data.\ncolumns : array-like, optional\n    New labels for the columns. Preferably an Index object to avoid\n    duplicating data.\naxis : int or str, optional\n    Axis to target. Can be either the axis name ('index', 'columns')\n    or number (0, 1)." }
_merge_doc = '\nMerge DataFrame or named Series objects with a database-style join.\n\nA named Series object is treated as a DataFrame with a single named column.\n\nThe join is done on columns or indexes. If joining columns on\ncolumns, the DataFrame indexes *will be ignored*. Otherwise if joining indexes\non indexes or indexes on a column or columns, the index will be passed on.\nWhen performing a cross merge, no column specifications to merge on are\nallowed.\n\n.. warning::\n\n    If both key columns contain rows where the key is a null value, those\n    rows will be matched against each other. This is different from usual SQL\n    join behaviour and can lead to unexpected results.\n\nParameters\n----------%s\nright : DataFrame or named Series\n    Object to merge with.\nhow : {\'left\', \'right\', \'outer\', \'inner\', \'cross\', \'left_anti\', \'right_anti\'},\n    default \'inner\'\n    Type of merge to be performed.\n\n    * left: use only keys from left frame, similar to a SQL left outer join;\n      preserve key order.\n    * right: use only keys from right frame, similar to a SQL right outer join;\n      preserve key order.\n    * outer: use union of keys from both frames, similar to a SQL full outer\n      join; sort keys lexicographically.\n    * inner: use intersection of keys from both frames, similar to a SQL inner\n      join; preserve the order of the left keys.\n    * cross: creates the cartesian product from both frames, preserves the order\n      of the left keys.\n    * left_anti: use only keys from left frame that are not in right frame, similar\n      to SQL left anti join; preserve key order.\n\n      .. versionadded:: 3.0\n    * right_anti: use only keys from right frame that are not in left frame, similar\n      to SQL right anti join; preserve key order.\n\n      .. versionadded:: 3.0\non : Hashable or a sequence of the previous\n    Column or index level names to join on. These must be found in both\n    DataFrames. If `on` is None and not merging on indexes then this defaults\n    to the intersection of the columns in both DataFrames.\nleft_on : Hashable or a sequence of the previous, or array-like\n    Column or index level names to join on in the left DataFrame. Can also\n    be an array or list of arrays of the length of the left DataFrame.\n    These arrays are treated as if they are columns.\nright_on : Hashable or a sequence of the previous, or array-like\n    Column or index level names to join on in the right DataFrame. Can also\n    be an array or list of arrays of the length of the right DataFrame.\n    These arrays are treated as if they are columns.\nleft_index : bool, default False\n    Use the index from the left DataFrame as the join key(s). If it is a\n    MultiIndex, the number of keys in the other DataFrame (either the index\n    or a number of columns) must match the number of levels.\nright_index : bool, default False\n    Use the index from the right DataFrame as the join key. Same caveats as\n    left_index.\nsort : bool, default False\n    Sort the join keys lexicographically in the result DataFrame. If False,\n    the order of the join keys depends on the join type (how keyword).\nsuffixes : list-like, default is ("_x", "_y")\n    A length-2 sequence where each element is optionally a string\n    indicating the suffix to add to overlapping column names in\n    `left` and `right` respectively. Pass a value of `None` instead\n    of a string to indicate that the column name from `left` or\n    `right` should be left as-is, with no suffix. At least one of the\n    values must not be None.\ncopy : bool, default False\n    This keyword is now ignored; changing its value will have no\n    impact on the method.\n\n    .. deprecated:: 3.0.0\n\n        This keyword is ignored and will be removed in pandas 4.0. Since\n        pandas 3.0, this method always returns a new object using a lazy\n        copy mechanism that defers copies until necessary\n        (Copy-on-Write). See the `user guide on Copy-on-Write\n        <https://pandas.pydata.org/docs/dev/user_guide/copy_on_write.html>`__\n        for more details.\n\nindicator : bool or str, default False\n    If True, adds a column to the output DataFrame called "_merge" with\n    information on the source of each row. The column can be given a different\n    name by providing a string argument. The column will have a Categorical\n    type with the value of "left_only" for observations whose merge key only\n    appears in the left DataFrame, "right_only" for observations\n    whose merge key only appears in the right DataFrame, and "both"\n    if the observation\'s merge key is found in both DataFrames.\n\nvalidate : str, optional\n    If specified, checks if merge is of specified type.\n\n    * "one_to_one" or "1:1": check if merge keys are unique in both\n      left and right datasets.\n    * "one_to_many" or "1:m": check if merge keys are unique in left\n      dataset.\n    * "many_to_one" or "m:1": check if merge keys are unique in right\n      dataset.\n    * "many_to_many" or "m:m": allowed, but does not result in checks.\n\nReturns\n-------\nDataFrame\n    A DataFrame of the two merged objects.\n\nSee Also\n--------\nmerge_ordered : Merge with optional filling/interpolation.\nmerge_asof : Merge on nearest keys.\nDataFrame.join : Similar method using indices.\n\nExamples\n--------\n>>> df1 = pd.DataFrame({\'lkey\': [\'foo\', \'bar\', \'baz\', \'foo\'],\n...                     \'value\': [1, 2, 3, 5]})\n>>> df2 = pd.DataFrame({\'rkey\': [\'foo\', \'bar\', \'baz\', \'foo\'],\n...                     \'value\': [5, 6, 7, 8]})\n>>> df1\n    lkey value\n0   foo      1\n1   bar      2\n2   baz      3\n3   foo      5\n>>> df2\n    rkey value\n0   foo      5\n1   bar      6\n2   baz      7\n3   foo      8\n\nMerge df1 and df2 on the lkey and rkey columns. The value columns have\nthe default suffixes, _x and _y, appended.\n\n>>> df1.merge(df2, left_on=\'lkey\', right_on=\'rkey\')\n  lkey  value_x rkey  value_y\n0  foo        1  foo        5\n1  foo        1  foo        8\n2  bar        2  bar        6\n3  baz        3  baz        7\n4  foo        5  foo        5\n5  foo        5  foo        8\n\nMerge DataFrames df1 and df2 with specified left and right suffixes\nappended to any overlapping columns.\n\n>>> df1.merge(df2, left_on=\'lkey\', right_on=\'rkey\',\n...           suffixes=(\'_left\', \'_right\'))\n  lkey  value_left rkey  value_right\n0  foo           1  foo            5\n1  foo           1  foo            8\n2  bar           2  bar            6\n3  baz           3  baz            7\n4  foo           5  foo            5\n5  foo           5  foo            8\n\nMerge DataFrames df1 and df2, but raise an exception if the DataFrames have\nany overlapping columns.\n\n>>> df1.merge(df2, left_on=\'lkey\', right_on=\'rkey\', suffixes=(False, False))\nTraceback (most recent call last):\n...\nValueError: columns overlap but no suffix specified:\n    Index([\'value\'], dtype=\'object\')\n\n>>> df1 = pd.DataFrame({\'a\': [\'foo\', \'bar\'], \'b\': [1, 2]})\n>>> df2 = pd.DataFrame({\'a\': [\'foo\', \'baz\'], \'c\': [3, 4]})\n>>> df1\n      a  b\n0   foo  1\n1   bar  2\n>>> df2\n      a  c\n0   foo  3\n1   baz  4\n\n>>> df1.merge(df2, how=\'inner\', on=\'a\')\n      a  b  c\n0   foo  1  3\n\n>>> df1.merge(df2, how=\'left\', on=\'a\')\n      a  b  c\n0   foo  1  3.0\n1   bar  2  NaN\n\n>>> df1 = pd.DataFrame({\'left\': [\'foo\', \'bar\']})\n>>> df2 = pd.DataFrame({\'right\': [7, 8]})\n>>> df1\n    left\n0   foo\n1   bar\n>>> df2\n    right\n0   7\n1   8\n\n>>> df1.merge(df2, how=\'cross\')\n   left  right\n0   foo      7\n1   foo      8\n2   bar      7\n3   bar      8\n'
DataFrame = <NODE:12>()

def _from_nested_dict(data = None):
    new_data = collections.defaultdict(dict)
    for index, s in data.items():
        for col, v in s.items():
            new_data[col][index] = v
            return new_data


def _reindex_for_setitem(value = None, index = None):
    if not value.index.equals(index) or len(index):
        if isinstance(value, Series):
            return (value._values, value._references)
        return (None._values.copy(), None)
    
    try:
        reindexed_value = value.reindex(index)._values
    except ValueError:
        err = None
        if not value.index.is_unique:
            raise err
        raise TypeError('incompatible index of inserted column with frame index'), err
        err = None
        del err

    return (reindexed_value, None)
