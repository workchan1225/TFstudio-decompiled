# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: indexing.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Iterable
from typing import TYPE_CHECKING, Literal, cast
import numpy as np
from pandas.util._decorators import cache_readonly, doc
from pandas.core.dtypes.common import is_integer, is_list_like
if TYPE_CHECKING:
    from pandas._typing import PositionalIndexer
    from pandas import DataFrame, Series
    from pandas.core.groupby import groupby

class GroupByIndexingMixin:
    '''
    Mixin for adding ._positional_selector to GroupBy.
    '''
    _positional_selector = (lambda self = None: if TYPE_CHECKING:
groupby_self = cast(groupby.GroupBy, self)else:
groupby_self = selfGroupByPositionalSelector(groupby_self))()
    
    def _make_mask_from_positional_indexer(self = None, arg = None):
        if is_list_like(arg):
            if (lambda .0: pass# WARNING: Decompyle incomplete
)(cast(Iterable, arg)()):
                mask = self._make_mask_from_list(cast(Iterable[int], arg))
            else:
                mask = self._make_mask_from_tuple(cast(tuple, arg))
        elif isinstance(arg, slice):
            mask = self._make_mask_from_slice(arg)
        elif is_integer(arg):
            mask = self._make_mask_from_int(cast(int, arg))
        else:
            raise TypeError(f'''Invalid index {type(arg)}. Must be integer, list-like, slice or a tuple of integers and slices''')
        if isinstance(mask, bool):
            pass
        return cast(np.ndarray, mask)

    
    def _make_mask_from_int(self = None, arg = None):
        if arg >= 0:
            return self._ascending_count == arg
        return None._descending_count == -arg - 1

    
    def _make_mask_from_list(self = None, args = None):
        positive = args()
        negative = args()
        mask = False
        if positive:
            mask |= np.isin(self._ascending_count, positive)
        if negative:
            mask |= np.isin(self._descending_count, negative)
        return mask

    
    def _make_mask_from_tuple(self = None, args = None):
        mask = False
        for arg in args:
            if is_integer(arg):
                mask |= self._make_mask_from_int(cast(int, arg))
                continue
            if isinstance(arg, slice):
                mask |= self._make_mask_from_slice(arg)
                continue
            raise ValueError(f'''Invalid argument {type(arg)}. Should be int or slice.''')
            return mask

    
    def _make_mask_from_slice(self = None, arg = None):
        start = arg.start
        stop = arg.stop
        step = arg.step
    # WARNING: Decompyle incomplete

    _ascending_count = (lambda self = None: if TYPE_CHECKING:
groupby_self = cast(groupby.GroupBy, self)else:
groupby_self = selfgroupby_self._cumcount_array())()
    _descending_count = (lambda self = None: if TYPE_CHECKING:
groupby_self = cast(groupby.GroupBy, self)else:
groupby_self = selfgroupby_self._cumcount_array(ascending = False))()

GroupByPositionalSelector = <NODE:12>()

class GroupByNthSelector:
    '''
    Dynamically substituted for GroupBy.nth to enable both call and index
    '''
    
    def __init__(self = None, groupby_object = None):
        self.groupby_object = groupby_object

    
    def __call__(self = None, n = None, dropna = None):
        return self.groupby_object._nth(n, dropna)

    
    def __getitem__(self = None, n = None):
        return self.groupby_object._nth(n)
