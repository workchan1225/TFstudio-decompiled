# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: concat.pyc (Python 3.11)

'''
Concat routines.
'''
from __future__ import annotations
from collections import abc
from itertools import pairwise
import types
from typing import TYPE_CHECKING, Literal, cast, overload
import warnings
import numpy as np
from pandas._libs import lib
from pandas.errors import Pandas4Warning
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.common import is_bool, is_scalar
from pandas.core.dtypes.concat import concat_compat
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.dtypes.missing import isna
from pandas.core.arrays.categorical import factorize_from_iterable, factorize_from_iterables

common
from pandas.core.indexes.api import Index, MultiIndex, all_indexes_same, default_index, ensure_index, get_objs_combined_axis, get_unanimous_names, union_indexes
MultiIndex = MultiIndex
all_indexes_same = all_indexes_same
default_index = default_index
ensure_index = ensure_index
get_objs_combined_axis = get_objs_combined_axis
get_unanimous_names = get_unanimous_names
union_indexes = union_indexes
import pandas.core.common, core
from pandas.core.indexes.datetimes import DatetimeIndex
from pandas.core.internals import concatenate_managers
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Iterable, Mapping
    from pandas._typing import Axis, AxisInt, HashableT
    from pandas import DataFrame, Series
concat = (lambda objs = None, *, axis: pass)()
concat = (lambda objs = None, *, axis: pass)()
concat = (lambda objs = None, *, axis: pass)()
concat = (lambda objs = None, *, axis: pass)()
concat = (lambda objs = None, *, axis: pass)()
concat = (lambda objs = None, *, axis: pass# WARNING: Decompyle incomplete
)()

def _sanitize_mixed_ndim(objs = None, sample = None, ignore_index = None, axis = ('objs', 'list[Series | DataFrame]', 'sample', 'Series | DataFrame', 'ignore_index', 'bool', 'axis', 'AxisInt', 'return', 'list[Series | DataFrame]')):
    new_objs = []
    current_column = 0
    max_ndim = sample.ndim
# WARNING: Decompyle incomplete


def _get_result(objs, is_series, bm_axis, ignore_index, intersect, sort, keys, levels = None, verify_integrity = None, names = None, axis = ('objs', 'list[Series | DataFrame]', 'is_series', 'bool', 'bm_axis', 'AxisInt', 'ignore_index', 'bool', 'intersect', 'bool', 'sort', 'bool | lib.NoDefault', 'keys', 'Iterable[Hashable] | None', 'verify_integrity', 'bool', 'names', 'list[HashableT] | None', 'axis', 'AxisInt')):
    if is_series:
        sample = cast('Series', objs[0])
        if bm_axis == 0:
            name = com.consensus_name_attr(objs)
            cons = sample._constructor
            arrs = objs()
            res = concat_compat(arrs, axis = 0)
            mgr = type(sample._mgr).from_array(res, index = new_index)
            result = sample._constructor_from_mgr(mgr, axes = mgr.axes)
            result._name = name
            return result.__finalize__(types.SimpleNamespace(input_objs = objs, objs = objs), method = 'concat')
        data = None(enumerate(objs))
        cons = sample._constructor_expanddim
        index = get_objs_combined_axis(objs, axis = objs[0]._get_block_manager_axis(0), intersect = intersect, sort = sort)
        columns = _get_concat_axis_series(objs, ignore_index, bm_axis, keys, levels, verify_integrity, names)
        df = cons(data, index = index, copy = False)
        df.columns = columns
        return df.__finalize__(types.SimpleNamespace(input_objs = objs, objs = objs), method = 'concat')
    sample = None('DataFrame', objs[0])
    mgrs_indexers = []
    result_axes = new_axes(objs, bm_axis, intersect, sort, keys, names, axis, levels, verify_integrity, ignore_index)
    for obj in objs:
        indexers = { }
        for ax, new_labels in enumerate(result_axes):
            if ax == bm_axis:
                continue
            obj_labels = obj.axes[1 - ax]
            if not new_labels.equals(obj_labels):
                indexers[ax] = obj_labels.get_indexer(new_labels)
            mgrs_indexers.append((obj._mgr, indexers))
            new_data = concatenate_managers(mgrs_indexers, result_axes, concat_axis = bm_axis, copy = False)
            out = sample._constructor_from_mgr(new_data, axes = new_data.axes)
            return out.__finalize__(types.SimpleNamespace(input_objs = objs, objs = objs), method = 'concat')


def new_axes(objs, bm_axis, intersect, sort, keys, names, axis = None, levels = None, verify_integrity = None, ignore_index = ('objs', 'list[Series | DataFrame]', 'bm_axis', 'AxisInt', 'intersect', 'bool', 'sort', 'bool | lib.NoDefault', 'keys', 'Iterable[Hashable] | None', 'names', 'list[HashableT] | None', 'axis', 'AxisInt', 'verify_integrity', 'bool', 'ignore_index', 'bool', 'return', 'list[Index]')):
    '''Return the new [index, column] result for concat.'''
    pass
# WARNING: Decompyle incomplete


def _get_concat_axis_series(objs, ignore_index, bm_axis, keys = None, levels = None, verify_integrity = None, names = ('objs', 'list[Series | DataFrame]', 'ignore_index', 'bool', 'bm_axis', 'AxisInt', 'keys', 'Iterable[Hashable] | None', 'verify_integrity', 'bool', 'names', 'list[HashableT] | None', 'return', 'Index')):
    '''Return result concat axis when concatenating Series objects.'''
    if ignore_index:
        return default_index(len(objs))
# WARNING: Decompyle incomplete


def _get_concat_axis_dataframe(objs, axis, ignore_index, keys = None, names = None, levels = None, verify_integrity = ('objs', 'list[Series | DataFrame]', 'axis', 'AxisInt', 'ignore_index', 'bool', 'keys', 'Iterable[Hashable] | None', 'names', 'list[HashableT] | None', 'verify_integrity', 'bool', 'return', 'Index')):
    '''Return result concat axis when concatenating DataFrame objects.'''
    pass
# WARNING: Decompyle incomplete


def _clean_keys_and_objs(objs = None, keys = None):
    '''
    Returns
    -------
    clean_objs : list[Series | DataFrame]
        List of DataFrame and Series with Nones removed.
    keys : Index | None
        None if keys was None
        Index if objs was a Mapping or keys was not None. Filtered where objs was None.
    ndim : set[int]
        Unique .ndim attribute of obj encountered.
    '''
    pass
# WARNING: Decompyle incomplete


def _get_sample_object(objs, ndims, keys = None, names = None, levels = None, intersect = ('objs', 'list[Series | DataFrame]', 'ndims', 'set[int]', 'intersect', 'bool', 'return', 'tuple[Series | DataFrame, list[Series | DataFrame]]')):
    if len(ndims) > 1:
        max_ndim = max(ndims)
        for obj in objs:
            if obj.ndim == max_ndim and sum(obj.shape):
                
                return None, (obj, objs)
# WARNING: Decompyle incomplete


def _concat_indexes(indexes = None):
    return indexes[0].append(indexes[1:])


def validate_unique_levels(levels = None):
    for level in levels:
        if not level.is_unique:
            raise ValueError(f'''Level values not unique: {level.tolist()}''')
        return None


def _make_concat_multiindex(indexes = None, keys = None, levels = None, names = (None, None)):
    pass
# WARNING: Decompyle incomplete
