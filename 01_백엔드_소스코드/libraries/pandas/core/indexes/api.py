# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: api.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, cast
import numpy as np
from pandas._libs import NaT, lib
from pandas.errors import InvalidIndexError
from pandas.core.dtypes.cast import find_common_type
from pandas.core.algorithms import safe_sort
from pandas.core.indexes.base import Index, _new_Index, ensure_index, ensure_index_from_sequences, get_unanimous_names, maybe_sequence_to_range
from pandas.core.indexes.category import CategoricalIndex
from pandas.core.indexes.datetimes import DatetimeIndex
from pandas.core.indexes.interval import IntervalIndex
from pandas.core.indexes.multi import MultiIndex
from pandas.core.indexes.period import PeriodIndex
from pandas.core.indexes.range import RangeIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex
if TYPE_CHECKING:
    from pandas._typing import Axis
__all__ = [
    'CategoricalIndex',
    'DatetimeIndex',
    'Index',
    'IntervalIndex',
    'InvalidIndexError',
    'MultiIndex',
    'NaT',
    'PeriodIndex',
    'RangeIndex',
    'TimedeltaIndex',
    '_new_Index',
    'all_indexes_same',
    'default_index',
    'ensure_index',
    'ensure_index_from_sequences',
    'get_objs_combined_axis',
    'get_unanimous_names',
    'maybe_sequence_to_range',
    'safe_sort_index',
    'union_indexes']

def get_objs_combined_axis(objs = None, intersect = None, axis = None, sort = (False, 0, True)):
    '''
    Extract combined index: return intersection or union (depending on the
    value of "intersect") of indexes on given axis, or None if all objects
    lack indexes (e.g. they are numpy arrays).

    Parameters
    ----------
    objs : list
        Series or DataFrame objects, may be mix of the two.
    intersect : bool, default False
        If True, calculate the intersection between indexes. Otherwise,
        calculate the union.
    axis : {0 or \'index\', 1 or \'outer\'}, default 0
        The axis to extract indexes from.
    sort : bool, default True
        Whether the result index should come out sorted or not. NoDefault
        use for deprecation in GH#57335.

    Returns
    -------
    Index
    '''
    pass
# WARNING: Decompyle incomplete


def _get_distinct_objs(objs = None):
    '''
    Return a list with distinct elements of "objs" (different ids).
    Preserves order.
    '''
    ids = set()
    res = []
    for obj in objs:
        if id(obj) not in ids:
            ids.add(id(obj))
            res.append(obj)
        return res


def _get_combined_index(indexes = None, intersect = None, sort = None):
    '''
    Return the union or intersection of indexes.

    Parameters
    ----------
    indexes : list of Index or list objects
        When intersect=True, do not accept list of lists.
    intersect : bool, default False
        If True, calculate the intersection between indexes. Otherwise,
        calculate the union.
    sort : bool, default False
        Whether the result index should come out sorted or not. NoDefault
        used for deprecation of GH#57335

    Returns
    -------
    Index
    '''
    indexes = _get_distinct_objs(indexes)
    if len(indexes) == 0:
        index = default_index(0)
    elif len(indexes) == 1:
        index = indexes[0]
    elif intersect:
        index = indexes[0]
        for other in indexes[1:]:
            index = index.intersection(other)
    index = union_indexes(indexes, sort = sort if sort is lib.no_default else False)
    index = ensure_index(index)
    if sort and sort is not lib.no_default:
        index = safe_sort_index(index)
    return index


def safe_sort_index(index = None):
    '''
    Returns the sorted index

    We keep the dtypes and the name attributes.

    Parameters
    ----------
    index : an Index

    Returns
    -------
    Index
    '''
    if index.is_monotonic_increasing:
        return index
    
    try:
        array_sorted = safe_sort(index)
        if isinstance(array_sorted, Index):
            return array_sorted
        array_sorted = None(np.ndarray, array_sorted)
        if isinstance(index, MultiIndex):
            index = MultiIndex.from_tuples(array_sorted, names = index.names)
        else:
            index = Index(array_sorted, name = index.name, dtype = index.dtype)
    except TypeError:
        pass

    return index


def union_indexes(indexes = None, sort = None):
    '''
    Return the union of indexes.

    The behavior of sort and names is not consistent.

    Parameters
    ----------
    indexes : list of Index or list objects
    sort : bool, default True
        Whether the result index should come out sorted or not. NoDefault
        used for deprecation of GH#57335.

    Returns
    -------
    Index
    '''
    pass
# WARNING: Decompyle incomplete


def _sanitize_and_check(indexes):
