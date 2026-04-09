# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: merge.pyc (Python 3.11)

'''
SQL-style merge routines
'''
from __future__ import annotations
from collections.abc import Hashable, Sequence
import datetime
from functools import partial
import types
from typing import TYPE_CHECKING, Literal, cast, final
import uuid
import warnings
import numpy as np
from pandas._libs import Timedelta, hashtable as libhashtable, join as libjoin, lib
from pandas._libs.lib import is_range_indexer
from pandas._typing import AnyArrayLike, ArrayLike, IndexLabel, JoinHow, MergeHow, Shape, Suffixes, npt
from pandas.errors import MergeError
from pandas.util._decorators import cache_readonly, set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.base import ExtensionDtype
from pandas.core.dtypes.cast import find_common_type
from pandas.core.dtypes.common import ensure_int64, ensure_object, is_bool, is_bool_dtype, is_float_dtype, is_integer, is_integer_dtype, is_list_like, is_number, is_numeric_dtype, is_object_dtype, is_string_dtype, needs_i8_conversion
from pandas.core.dtypes.dtypes import CategoricalDtype, DatetimeTZDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.dtypes.missing import isna, na_value_for_dtype
from pandas import ArrowDtype, Categorical, Index, MultiIndex, Series

algorithms
from pandas.core.arrays import ArrowExtensionArray, BaseMaskedArray, ExtensionArray
BaseMaskedArray = BaseMaskedArray
ExtensionArray = ExtensionArray
import pandas.core.algorithms, core
from pandas.core.arrays.string_ import StringDtype

common
from pandas.core.construction import ensure_wrapped_if_datetimelike, extract_array
extract_array = extract_array
import pandas.core.common, core
from pandas.core.indexes.api import default_index
from pandas.core.sorting import get_group_index, is_int64_overflow_possible
if TYPE_CHECKING:
    from pandas import DataFrame
    from pandas.core import groupby
    from pandas.core.arrays import DatetimeArray
    from pandas.core.indexes.frozen import FrozenList
_factorizers = {
    np.object_: libhashtable.ObjectFactorizer,
    np.complex128: libhashtable.Complex128Factorizer,
    np.complex64: libhashtable.Complex64Factorizer,
    np.float32: libhashtable.Float32Factorizer,
    np.float64: libhashtable.Float64Factorizer,
    np.bool_: libhashtable.UInt8Factorizer,
    np.uint8: libhashtable.UInt8Factorizer,
    np.uint16: libhashtable.UInt16Factorizer,
    np.uint32: libhashtable.UInt32Factorizer,
    np.uint64: libhashtable.UInt64Factorizer,
    np.int8: libhashtable.Int8Factorizer,
    np.int16: libhashtable.Int16Factorizer,
    np.int32: libhashtable.Int32Factorizer,
    np.longlong: libhashtable.Int64Factorizer,
    np.int64: libhashtable.Int64Factorizer }
if np.intc is not np.int32:
    if np.dtype(np.intc).itemsize == 4:
        _factorizers[np.intc] = libhashtable.Int32Factorizer
    else:
        _factorizers[np.intc] = libhashtable.Int64Factorizer
if np.uintc is not np.uint32:
    if np.dtype(np.uintc).itemsize == 4:
        _factorizers[np.uintc] = libhashtable.UInt32Factorizer
    else:
        _factorizers[np.uintc] = libhashtable.UInt64Factorizer
_known = (np.ndarray, ExtensionArray, Index, ABCSeries)
merge = (lambda left, right, how, on, left_on, right_on, left_index, right_index, sort = None, suffixes = None, copy = set_module('pandas'), indicator = ('inner', None, None, None, False, False, False, ('_x', '_y'), lib.no_default, False, None), validate = ('left', 'DataFrame | Series', 'right', 'DataFrame | Series', 'how', 'MergeHow', 'on', 'IndexLabel | AnyArrayLike | None', 'left_on', 'IndexLabel | AnyArrayLike | None', 'right_on', 'IndexLabel | AnyArrayLike | None', 'left_index', 'bool', 'right_index', 'bool', 'sort', 'bool', 'suffixes', 'Suffixes', 'copy', 'bool | lib.NoDefault', 'indicator', 'str | bool', 'validate', 'str | None', 'return', 'DataFrame'): left_df = _validate_operand(left)left._check_copy_deprecation(copy)right_df = _validate_operand(right)if how == 'cross':
_cross_merge(left_df, right_df, on = on, left_on = left_on, right_on = right_on, left_index = left_index, right_index = right_index, sort = sort, suffixes = suffixes, indicator = indicator, validate = validate)op = None(left_df, right_df, how = how, on = on, left_on = left_on, right_on = right_on, left_index = left_index, right_index = right_index, sort = sort, suffixes = suffixes, indicator = indicator, validate = validate)op.get_result())()

def _cross_merge(left, right, on, left_on, right_on, left_index, right_index = None, sort = None, suffixes = None, indicator = (None, None, None, False, False, False, ('_x', '_y'), False, None), validate = ('left', 'DataFrame', 'right', 'DataFrame', 'on', 'IndexLabel | AnyArrayLike | None', 'left_on', 'IndexLabel | AnyArrayLike | None', 'right_on', 'IndexLabel | AnyArrayLike | None', 'left_index', 'bool', 'right_index', 'bool', 'sort', 'bool', 'suffixes', 'Suffixes', 'indicator', 'str | bool', 'validate', 'str | None', 'return', 'DataFrame')):
    """
    See merge.__doc__ with how='cross'
    """
    pass
# WARNING: Decompyle incomplete


def _groupby_and_merge(by = None, left = None, right = None, merge_pieces = ('left', 'DataFrame | Series', 'right', 'DataFrame | Series')):
    '''
    groupby & merge; we are always performing a left-by type operation

    Parameters
    ----------
    by: field to group
    left: DataFrame
    right: DataFrame
    merge_pieces: function for merging
    '''
    pass
# WARNING: Decompyle incomplete

merge_ordered = (lambda left, right, on, left_on, right_on, left_by = None, right_by = None, fill_method = set_module('pandas'), suffixes = (None, None, None, None, None, None, ('_x', '_y'), 'outer'), how = ('left', 'DataFrame | Series', 'right', 'DataFrame | Series', 'on', 'IndexLabel | None', 'left_on', 'IndexLabel | None', 'right_on', 'IndexLabel | None', 'fill_method', 'str | None', 'suffixes', 'Suffixes', 'how', 'JoinHow', 'return', 'DataFrame'): pass# WARNING: Decompyle incomplete
)()
merge_asof = (lambda left, right, on, left_on, right_on, left_index, right_index, by, left_by, right_by = None, suffixes = None, tolerance = set_module('pandas'), allow_exact_matches = (None, None, None, False, False, None, None, None, ('_x', '_y'), None, True, 'backward'), direction = ('left', 'DataFrame | Series', 'right', 'DataFrame | Series', 'on', 'IndexLabel | None', 'left_on', 'IndexLabel | None', 'right_on', 'IndexLabel | None', 'left_index', 'bool', 'right_index', 'bool', 'suffixes', 'Suffixes', 'tolerance', 'int | datetime.timedelta | None', 'allow_exact_matches', 'bool', 'direction', 'str', 'return', 'DataFrame'): op = _AsOfMerge(left, right, on = on, left_on = left_on, right_on = right_on, left_index = left_index, right_index = right_index, by = by, left_by = left_by, right_by = right_by, suffixes = suffixes, how = 'asof', tolerance = tolerance, allow_exact_matches = allow_exact_matches, direction = direction)op.get_result())()

class _MergeOperation:
    '''
    Perform a database (SQL) merge operation between two DataFrame or Series
    objects using either columns as keys or their row indexes
    '''
    left_join_keys: 'list[ArrayLike]' = 'merge'
    
    def __init__(self, left, right, how, on, left_on, right_on, left_index, right_index = None, sort = None, suffixes = None, indicator = ('inner', None, None, None, False, False, True, ('_x', '_y'), False, None), validate = ('left', 'DataFrame | Series', 'right', 'DataFrame | Series', 'how', "JoinHow | Literal['left_anti', 'right_anti', 'asof']", 'on', 'IndexLabel | AnyArrayLike | None', 'left_on', 'IndexLabel | AnyArrayLike | None', 'right_on', 'IndexLabel | AnyArrayLike | None', 'left_index', 'bool', 'right_index', 'bool', 'sort', 'bool', 'suffixes', 'Suffixes', 'indicator', 'str | bool', 'validate', 'str | None', 'return', 'None')):
        _left = _validate_operand(left)
        _right = _validate_operand(right)
        self.left = _left
        self.orig_left = _left
        self.right = _right
        self.orig_right = _right
        (self.how, self.anti_join) = self._validate_how(how)
        self.on = com.maybe_make_list(on)
        self.suffixes = suffixes
        if not sort:
            self.sort = how == 'outer'
            self.left_index = left_index
            self.right_index = right_index
            self.indicator = indicator
            if not is_bool(left_index):
                raise ValueError(f'''left_index parameter must be of type bool, not {type(left_index)}''')
            if not is_bool(right_index):
                raise ValueError(f'''right_index parameter must be of type bool, not {type(right_index)}''')
            if _left.columns.nlevels != _right.columns.nlevels:
                msg = f'''Not allowed to merge between different levels. ({_left.columns.nlevels} levels on the left, {_right.columns.nlevels} on the right)'''
                raise MergeError(msg)
            (self.left_on, self.right_on) = self._validate_left_right_on(left_on, right_on)
            (self.left_join_keys, self.right_join_keys, self.join_names, left_drop, right_drop) = self._get_merge_keys()
            if left_drop:
                self.left = self.left._drop_labels_or_levels(left_drop)
        if right_drop:
            self.right = self.right._drop_labels_or_levels(right_drop)
        self._maybe_require_matching_dtypes(self.left_join_keys, self.right_join_keys)
        self._validate_tolerance(self.left_join_keys)
        self._maybe_coerce_merge_keys()
    # WARNING: Decompyle incomplete

    _validate_how = (lambda self = None, how = None: merge_type = {
'asof',
'left',
'cross',
'inner',
'outer',
'right',
'left_anti',
'right_anti'}if how not in merge_type:
raise ValueError(f'''\'{how}\' is not a valid Merge type: left, right, inner, outer, left_anti, right_anti, cross, asof''')anti_join = Falseif how in frozenset({'left_anti', 'right_anti'}):
how = how.split('_')[0]anti_join = Truehow = cast(JoinHow | Literal['asof'], how)(how, anti_join))()
    
    def _maybe_require_matching_dtypes(self = None, left_join_keys = None, right_join_keys = None):
        pass

    
    def _validate_tolerance(self = None, left_join_keys = None):
        pass

    _reindex_and_concat = (lambda self = None, join_index = None, left_indexer = final, right_indexer = ('join_index', 'Index', 'left_indexer', 'npt.NDArray[np.intp] | None', 'right_indexer', 'npt.NDArray[np.intp] | None', 'return', 'DataFrame'): left = self.left[:]right = self.right[:](llabels, rlabels) = _items_overlap_with_suffix(self.left._info_axis, self.right._info_axis, self.suffixes)# WARNING: Decompyle incomplete
)()
    
    def get_result(self = None):
        '''
        Execute the merge.
        '''
        if self.indicator:
            (self.left, self.right) = self._indicator_pre_merge(self.left, self.right)
        (join_index, left_indexer, right_indexer) = self._get_join_info()
        result = self._reindex_and_concat(join_index, left_indexer, right_indexer)
        if self.indicator:
            result = self._indicator_post_merge(result)
        self._maybe_add_join_keys(result, left_indexer, right_indexer)
        self._maybe_restore_index_levels(result)
        return result.__finalize__(types.SimpleNamespace(input_objs = [
            self.left,
            self.right], left = self.left, right = self.right), method = 'merge')

    _indicator_name = (lambda self = None: if isinstance(self.indicator, str):
self.indicatorif None(self.indicator, bool):
'_merge' if self.indicator else Noneraise None('indicator option can only accept boolean or string arguments'))()()
    _indicator_pre_merge = (lambda self = None, left = None, right = final: columns = left.columns.union(right.columns)for i in ('_left_indicator', '_right_indicator'):
if i in columns:
raise ValueError(f'''Cannot use `indicator=True` option when data contains a column named {i}''')if self._indicator_name in columns:
raise ValueError('Cannot use name of an existing column for indicator column')left = left.copy(deep = False)right = right.copy(deep = False)left['_left_indicator'] = 1left['_left_indicator'] = left['_left_indicator'].astype('int8')right['_right_indicator'] = 2right['_right_indicator'] = right['_right_indicator'].astype('int8')(left, right))()
    _indicator_post_merge = (lambda self = None, result = None: result['_left_indicator'] = result['_left_indicator'].fillna(0)result['_right_indicator'] = result['_right_indicator'].fillna(0)result[self._indicator_name] = Categorical(result['_left_indicator'] + result['_right_indicator'], categories = [
1,
2,
3])result[self._indicator_name] = result[self._indicator_name].cat.rename_categories([
'left_only',
'right_only',
'both'])result = result.drop(labels = [
'_left_indicator',
'_right_indicator'], axis = 1)result)()
    _maybe_restore_index_levels = (lambda self = None, result = None: names_to_restore = []for name, left_key, right_key in zip(self.join_names, self.left_on, self.right_on, strict = True):
if self.orig_left._is_level_reference(left_key) and self.orig_right._is_level_reference(right_key) and left_key == right_key and name not in result.index.names:
names_to_restore.append(name)if names_to_restore:
result.set_index(names_to_restore, inplace = True)NoneNone)()
    _maybe_add_join_keys = (lambda self = None, result = None, left_indexer = final, right_indexer = ('result', 'DataFrame', 'left_indexer', 'npt.NDArray[np.intp] | None', 'right_indexer', 'npt.NDArray[np.intp] | None', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    
    def _get_join_indexers(self = None):
        '''return the join indexers'''
        pass
    # WARNING: Decompyle incomplete

    _get_join_info = (lambda self = None: left_ax = self.left.indexright_ax = self.right.indexif self.left_index and self.right_index and self.how != 'asof':
(join_index, left_indexer, right_indexer) = left_ax.join(right_ax, how = self.how, return_indexers = True, sort = self.sort)elif self.right_index and self.how == 'left':
(join_index, left_indexer, right_indexer) = _left_join_on_index(left_ax, right_ax, self.left_join_keys, sort = self.sort)elif self.left_index and self.how == 'right':
(join_index, right_indexer, left_indexer) = _left_join_on_index(right_ax, left_ax, self.right_join_keys, sort = self.sort)# WARNING: Decompyle incomplete
)()
    _create_join_index = (lambda self = None, index = None, other_index = final, indexer = ('left',), how = ('index', 'Index', 'other_index', 'Index', 'indexer', 'npt.NDArray[np.intp] | None', 'how', 'JoinHow', 'return', 'Index'): if not self.how in (how, 'outer') and isinstance(other_index, MultiIndex):
mask = indexer == -1if np.any(mask):
fill_value = na_value_for_dtype(index.dtype, compat = False)if not index._can_hold_na:
new_index = Index([
fill_value])else:
new_index = Index([
fill_value], dtype = index.dtype)index = index.append(new_index)# WARNING: Decompyle incomplete
)()
    _handle_anti_join = (lambda self = None, join_index = None, left_indexer = final, right_indexer = ('join_index', 'Index', 'left_indexer', 'npt.NDArray[np.intp] | None', 'right_indexer', 'npt.NDArray[np.intp] | None', 'return', 'tuple[Index, npt.NDArray[np.intp] | None, npt.NDArray[np.intp] | None]'): pass# WARNING: Decompyle incomplete
)()
    _get_merge_keys = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _maybe_coerce_merge_keys = (lambda self = None: for lk, rk, name in zip(self.left_join_keys, self.right_join_keys, self.join_names, strict = True):
if (len(lk) or len(rk) or len(lk)) and len(rk):
continuelk = extract_array(lk, extract_numpy = True)rk = extract_array(rk, extract_numpy = True)lk_is_cat = isinstance(lk.dtype, CategoricalDtype)rk_is_cat = isinstance(rk.dtype, CategoricalDtype)if not is_object_dtype(lk.dtype):
lk_is_object_or_string = is_string_dtype(lk.dtype)if not is_object_dtype(rk.dtype):
rk_is_object_or_string = is_string_dtype(rk.dtype)if lk_is_cat and rk_is_cat:
lk = cast(Categorical, lk)rk = cast(Categorical, rk)if lk._categories_match_up_to_permutation(rk):
continueelif lk_is_cat or rk_is_cat:
passelif lk.dtype == rk.dtype:
continuemsg = f'''You are trying to merge on {lk.dtype} and {rk.dtype} columns for key \'{name}\'. If you wish to proceed you should use pd.concat'''if is_numeric_dtype(lk.dtype) and is_numeric_dtype(rk.dtype):
if lk.dtype.kind == rk.dtype.kind:
continueif not isinstance(lk.dtype, ExtensionDtype) and isinstance(rk.dtype, ExtensionDtype):
ct = find_common_type([
lk.dtype,
rk.dtype])if isinstance(ct, ExtensionDtype):
com_cls = ct.construct_array_type()rk = com_cls._from_sequence(rk, dtype = ct, copy = False)else:
rk = rk.astype(ct)elif isinstance(rk.dtype, ExtensionDtype):
ct = find_common_type([
lk.dtype,
rk.dtype])if isinstance(ct, ExtensionDtype):
com_cls = ct.construct_array_type()lk = com_cls._from_sequence(lk, dtype = ct, copy = False)else:
lk = lk.astype(ct)if is_integer_dtype(rk.dtype) and is_float_dtype(lk.dtype):
np.errstate(invalid = 'ignore')casted = lk.astype(rk.dtype)None(None, None)else:
with None:
if not None:
passmask = ~np.isnan(lk)match = lk == castedif not match[mask].all():
warnings.warn('You are merging on int and float columns where the float values are not equal to their int representation.', UserWarning, stacklevel = find_stack_level())continueif is_float_dtype(rk.dtype) and is_integer_dtype(lk.dtype):
np.errstate(invalid = 'ignore')casted = rk.astype(lk.dtype)None(None, None)else:
with None:
if not None:
passmask = ~np.isnan(rk)match = rk == castedif not match[mask].all():
warnings.warn('You are merging on int and float columns where the float values are not equal to their int representation.', UserWarning, stacklevel = find_stack_level())continueif lib.infer_dtype(lk, skipna = False) == lib.infer_dtype(rk, skipna = False):
continueelif (lk_is_object_or_string or is_bool_dtype(rk.dtype) or is_bool_dtype(lk.dtype)) and rk_is_object_or_string:
passelif (lk_is_object_or_string or is_numeric_dtype(rk.dtype) or is_numeric_dtype(lk.dtype)) and rk_is_object_or_string:
inferred_left = lib.infer_dtype(lk, skipna = False)inferred_right = lib.infer_dtype(rk, skipna = False)bool_types = [
'integer',
'mixed-integer',
'boolean',
'empty']string_types = [
'string',
'unicode',
'mixed',
'bytes',
'empty']if inferred_left in bool_types and inferred_right in bool_types:
passelif (inferred_left in string_types or inferred_right not in string_types or inferred_right in string_types) and inferred_left not in string_types:
raise ValueError(msg)elif not needs_i8_conversion(lk.dtype) and needs_i8_conversion(rk.dtype):
raise ValueError(msg)if needs_i8_conversion(lk.dtype) and needs_i8_conversion(rk.dtype):
raise ValueError(msg)if not isinstance(lk.dtype, DatetimeTZDtype) and isinstance(rk.dtype, DatetimeTZDtype):
raise ValueError(msg)if isinstance(lk.dtype, DatetimeTZDtype) and isinstance(rk.dtype, DatetimeTZDtype):
raise ValueError(msg)if (isinstance(lk.dtype, DatetimeTZDtype) or isinstance(rk.dtype, DatetimeTZDtype) or lk.dtype.kind == 'M') and rk.dtype.kind == 'M':
continueif lk.dtype.kind == 'M' and rk.dtype.kind == 'm':
raise ValueError(msg)if lk.dtype.kind == 'm' and rk.dtype.kind == 'M':
raise ValueError(msg)if is_object_dtype(lk.dtype) and is_object_dtype(rk.dtype):
continueif name in self.left.columns:
typ = cast(Categorical, lk).categories.dtype if lk_is_cat else objectself.left = self.left.copy(deep = False)self.left[name] = self.left[name].astype(typ)if name in self.right.columns:
typ = cast(Categorical, rk).categories.dtype if rk_is_cat else objectself.right = self.right.copy(deep = False)self.right[name] = self.right[name].astype(typ)None)()
    
    def _validate_left_right_on(self, left_on, right_on):
        left_on = com.maybe_make_list(left_on)
        right_on = com.maybe_make_list(right_on)
    # WARNING: Decompyle incomplete

    _validate_validate_kwd = (lambda self = None, validate = None: pass# WARNING: Decompyle incomplete
)()


def get_join_indexers(left_keys = None, right_keys = None, sort = None, how = (False, 'inner')):
    """

    Parameters
    ----------
    left_keys : list[ndarray, ExtensionArray, Index, Series]
    right_keys : list[ndarray, ExtensionArray, Index, Series]
    sort : bool, default False
    how : {'inner', 'outer', 'left', 'right'}, default 'inner'

    Returns
    -------
    np.ndarray[np.intp] or None
        Indexer into the left_keys.
    np.ndarray[np.intp] or None
        Indexer into the right_keys.
    """
    pass
# WARNING: Decompyle incomplete


def get_join_indexers_non_unique(left = None, right = None, sort = None, how = (False, 'inner')):
    """
    Get join indexers for left and right.

    Parameters
    ----------
    left : ArrayLike
    right : ArrayLike
    sort : bool, default False
    how : {'inner', 'outer', 'left', 'right'}, default 'inner'

    Returns
    -------
    np.ndarray[np.intp]
        Indexer into left.
    np.ndarray[np.intp]
        Indexer into right.
    """
    (lkey, rkey, count) = _factorize_keys(left, right, sort = sort, how = how)
    if count == -1:
        return (lkey, rkey)
    if None == 'left':
        (lidx, ridx) = libjoin.left_outer_join(lkey, rkey, count, sort = sort)
    elif how == 'right':
        (ridx, lidx) = libjoin.left_outer_join(rkey, lkey, count, sort = sort)
    elif how == 'inner':
        (lidx, ridx) = libjoin.inner_join(lkey, rkey, count, sort = sort)
    elif how == 'outer':
        (lidx, ridx) = libjoin.full_outer_join(lkey, rkey, count)
    return (lidx, ridx)


def restore_dropped_levels_multijoin(left, right, dropped_level_names = None, join_index = None, lindexer = None, rindexer = ('left', 'MultiIndex', 'right', 'MultiIndex', 'join_index', 'Index', 'lindexer', 'npt.NDArray[np.intp]', 'rindexer', 'npt.NDArray[np.intp]', 'return', 'tuple[FrozenList, FrozenList, FrozenList]')):
    '''
    *this is an internal non-public method*

    Returns the levels, labels and names of a multi-index to multi-index join.
    Depending on the type of join, this method restores the appropriate
    dropped levels of the joined multi-index.
    The method relies on lindexer, rindexer which hold the index positions of
    left and right, where a join was feasible

    Parameters
    ----------
    left : MultiIndex
        left index
    right : MultiIndex
        right index
    dropped_level_names : str array
        list of non-common level names
    join_index : Index
        the index of the join between the
        common levels of left and right
    lindexer : np.ndarray[np.intp]
        left indexer
    rindexer : np.ndarray[np.intp]
        right indexer

    Returns
    -------
    levels : list of Index
        levels of combined multiindexes
    labels : np.ndarray[np.intp]
        labels of combined multiindexes
    names : List[Hashable]
        names of combined multiindex levels

    '''
    
    def _convert_to_multiindex(index = None):
        if isinstance(index, MultiIndex):
            return index
        return None.from_arrays([
            index._values], names = [
            index.name])

    join_index = _convert_to_multiindex(join_index)
    join_levels = join_index.levels
    join_codes = join_index.codes
    join_names = join_index.names
# WARNING: Decompyle incomplete


class _OrderedMerge(_MergeOperation):
    _merge_type = 'ordered_merge'
    
    def __init__(self, left, right, on, left_on, right_on, left_index = None, right_index = None, suffixes = None, fill_method = (None, None, None, False, False, ('_x', '_y'), None, 'outer'), how = ('left', 'DataFrame | Series', 'right', 'DataFrame | Series', 'on', 'IndexLabel | None', 'left_on', 'IndexLabel | None', 'right_on', 'IndexLabel | None', 'left_index', 'bool', 'right_index', 'bool', 'suffixes', 'Suffixes', 'fill_method', 'str | None', 'how', "JoinHow | Literal['asof']", 'return', 'None')):
        self.fill_method = fill_method
        _MergeOperation.__init__(self, left, right, on = on, left_on = left_on, left_index = left_index, right_index = right_index, right_on = right_on, how = how, suffixes = suffixes, sort = True)

    
    def get_result(self = None):
        (join_index, left_indexer, right_indexer) = self._get_join_info()
    # WARNING: Decompyle incomplete



def _asof_by_function(direction = None):
    name = f'''asof_join_{direction}_on_X_by_Y'''
    return getattr(libjoin, name, None)


class _AsOfMerge(_OrderedMerge):
    pass
# WARNING: Decompyle incomplete


def _get_multiindex_indexer(join_keys = None, index = None, sort = None):
    pass
# WARNING: Decompyle incomplete


def _get_empty_indexer():
    '''Return empty join indexers.'''
    return (np.array([], dtype = np.intp), np.array([], dtype = np.intp))


def _get_no_sort_one_missing_indexer(n = None, left_missing = None):
    """
    Return join indexers where all of one side is selected without sorting
    and none of the other side is selected.

    Parameters
    ----------
    n : int
        Length of indexers to create.
    left_missing : bool
        If True, the left indexer will contain only -1's.
        If False, the right indexer will contain only -1's.

    Returns
    -------
    np.ndarray[np.intp]
        Left indexer
    np.ndarray[np.intp]
        Right indexer
    """
    idx = np.arange(n, dtype = np.intp)
    idx_missing = np.full(shape = n, fill_value = -1, dtype = np.intp)
    if left_missing:
        return (idx_missing, idx)
    return (None, idx_missing)


def _left_join_on_index(left_ax = None, right_ax = None, join_keys = None, sort = (False,)):
    if isinstance(right_ax, MultiIndex):
        (lkey, rkey) = _get_multiindex_indexer(join_keys, right_ax, sort = sort)
    else:
        lkey = join_keys[0]
        rkey = right_ax._values
    (left_key, right_key, count) = _factorize_keys(lkey, rkey, sort = sort)
    (left_indexer, right_indexer) = libjoin.left_outer_join(left_key, right_key, count, sort = sort)
    if sort or len(left_ax) != len(left_indexer):
        join_index = left_ax.take(left_indexer)
        return (join_index, left_indexer, right_indexer)
    return (None, None, right_indexer)


def _factorize_keys(lk = None, rk = None, sort = None, how = (True, None)):
    '''
    Encode left and right keys as enumerated types.

    This is used to get the join indexers to be used when merging DataFrames.

    Parameters
    ----------
    lk : ndarray, ExtensionArray
        Left key.
    rk : ndarray, ExtensionArray
        Right key.
    sort : bool, defaults to True
        If True, the encoding is done such that the unique elements in the
        keys are sorted.
    how: str, optional
        Used to determine if we can use hash-join. If not given, then just factorize
        keys.

    Returns
    -------
    np.ndarray[np.intp]
        Left (resp. right if called with `key=\'right\'`) labels, as enumerated type.
    np.ndarray[np.intp]
        Right (resp. left if called with `key=\'right\'`) labels, as enumerated type.
    int
        Number of unique elements in union of left and right labels. -1 if we used
        a hash-join.

    See Also
    --------
    merge : Merge DataFrame or named Series objects
        with a database-style join.
    algorithms.factorize : Encode the object as an enumerated type
        or categorical variable.

    Examples
    --------
    >>> lk = np.array(["a", "c", "b"])
    >>> rk = np.array(["a", "c"])

    Here, the unique values are `\'a\', \'b\', \'c\'`. With the default
    `sort=True`, the encoding will be `{0: \'a\', 1: \'b\', 2: \'c\'}`:

    >>> pd.core.reshape.merge._factorize_keys(lk, rk)
    (array([0, 2, 1]), array([0, 2]), 3)

    With the `sort=False`, the encoding will correspond to the order
    in which the unique elements first appear: `{0: \'a\', 1: \'c\', 2: \'b\'}`:

    >>> pd.core.reshape.merge._factorize_keys(lk, rk, sort=False)
    (array([0, 1, 2]), array([0, 1]), 3)
    '''
    if (isinstance(lk.dtype, DatetimeTZDtype) or isinstance(rk.dtype, DatetimeTZDtype) or lib.is_np_dtype(lk.dtype, 'M')) and lib.is_np_dtype(rk.dtype, 'M'):
        (lk, rk) = cast('DatetimeArray', lk)._ensure_matching_resos(rk)
        lk = cast('DatetimeArray', lk)._ndarray
        rk = cast('DatetimeArray', rk)._ndarray
# WARNING: Decompyle incomplete


def _convert_arrays_and_get_rizer_klass(lk = None, rk = None):
    if is_numeric_dtype(lk.dtype):
        if lk.dtype != rk.dtype:
            dtype = find_common_type([
                lk.dtype,
                rk.dtype])
            if isinstance(dtype, ExtensionDtype):
                cls = dtype.construct_array_type()
                if not isinstance(lk, ExtensionArray):
                    lk = cls._from_sequence(lk, dtype = dtype, copy = False)
                else:
                    lk = lk.astype(dtype, copy = False)
                if not isinstance(rk, ExtensionArray):
                    rk = cls._from_sequence(rk, dtype = dtype, copy = False)
                else:
                    rk = rk.astype(dtype, copy = False)
            else:
                lk = lk.astype(dtype, copy = False)
                rk = rk.astype(dtype, copy = False)
        if isinstance(lk, BaseMaskedArray):
            klass = _factorizers[lk.dtype.type]
        elif isinstance(lk.dtype, ArrowDtype):
            klass = _factorizers[lk.dtype.numpy_dtype.type]
        else:
            klass = _factorizers[lk.dtype.type]
    else:
        klass = libhashtable.ObjectFactorizer
        lk = ensure_object(lk)
        rk = ensure_object(rk)
    return (klass, lk, rk)


def _sort_labels(uniques = None, left = None, right = None):
    llength = len(left)
    labels = np.concatenate([
        left,
        right])
    (_, new_labels) = algos.safe_sort(uniques, labels, use_na_sentinel = True)
    new_right = new_labels[llength:]
    new_left = new_labels[:llength]
    return (new_left, new_right)


def _get_join_keys(llab = None, rlab = None, shape = None, sort = ('llab', 'list[npt.NDArray[np.int64 | np.intp]]', 'rlab', 'list[npt.NDArray[np.int64 | np.intp]]', 'shape', 'Shape', 'sort', 'bool', 'return', 'tuple[npt.NDArray[np.int64], npt.NDArray[np.int64]]')):
    pass
# WARNING: Decompyle incomplete


def _should_fill(lname = None, rname = None):
    if not isinstance(lname, str) or isinstance(rname, str):
        return True
    return None == rname


def _any(x = None):
    if x is not None:
        pass
# WARNING: Decompyle incomplete


def _validate_operand(obj = None):
    if isinstance(obj, ABCDataFrame):
        return obj
# WARNING: Decompyle incomplete


def _items_overlap_with_suffix(left = None, right = None, suffixes = None):
    '''
    Suffixes type validation.

    If two indices overlap, add suffixes to overlapping entries.

    If corresponding suffix is empty, the entry is simply converted to string.

    '''
    pass
# WARNING: Decompyle incomplete
