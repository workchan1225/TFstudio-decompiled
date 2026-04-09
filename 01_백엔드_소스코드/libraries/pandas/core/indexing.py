# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: indexing.pyc (Python 3.11)

from __future__ import annotations
from contextlib import suppress
import sys
from typing import TYPE_CHECKING, Any, Self, cast, final
import warnings
import numpy as np
from pandas._libs.indexing import NDFrameIndexerBase
from pandas._libs.lib import item_from_zerodim
from pandas.compat import CHAINED_WARNING_DISABLED
from pandas.compat._constants import REF_COUNT_IDX
from pandas.errors import AbstractMethodError, ChainedAssignmentError, IndexingError, InvalidIndexError, LossySetitemError
from pandas.errors.cow import _chained_assignment_msg
from pandas.util._decorators import doc
from pandas.core.dtypes.cast import can_hold_element, maybe_promote
from pandas.core.dtypes.common import is_array_like, is_bool_dtype, is_hashable, is_integer, is_iterator, is_list_like, is_numeric_dtype, is_object_dtype, is_scalar, is_sequence
from pandas.core.dtypes.concat import concat_compat
from pandas.core.dtypes.dtypes import ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.dtypes.missing import construct_1d_array_from_inferred_fill_value, infer_fill_value, is_valid_na_for_dtype, isna, na_value_for_dtype
from pandas.core import algorithms as algos

common
from pandas.core.construction import array, extract_array
extract_array = extract_array
import pandas.core.common, core
from pandas.core.indexers import check_array_indexer, is_list_like_indexer, is_scalar_indexer, length_of_indexer
from pandas.core.indexes.api import Index, MultiIndex
if TYPE_CHECKING:
    from collections.abc import Hashable, Sequence
    from pandas._typing import Axis, AxisInt, T, npt
    from pandas import DataFrame, Series
_NS = slice(None, None)
_one_ellipsis_message = "indexer may only contain one '...' entry"

class _IndexSlice:
    '''
    Create an object to more easily perform multi-index slicing.

    See Also
    --------
    MultiIndex.remove_unused_levels : New MultiIndex with no unused levels.

    Notes
    -----
    See :ref:`Defined Levels <advanced.shown_levels>`
    for further info on slicing a MultiIndex.

    Examples
    --------
    >>> midx = pd.MultiIndex.from_product([["A0", "A1"], ["B0", "B1", "B2", "B3"]])
    >>> columns = ["foo", "bar"]
    >>> dfmi = pd.DataFrame(
    ...     np.arange(16).reshape((len(midx), len(columns))),
    ...     index=midx,
    ...     columns=columns,
    ... )

    Using the default slice command:

    >>> dfmi.loc[(slice(None), slice("B0", "B1")), :]
               foo  bar
        A0 B0    0    1
           B1    2    3
        A1 B0    8    9
           B1   10   11

    Using the IndexSlice class for a more intuitive command:

    >>> idx = pd.IndexSlice
    >>> dfmi.loc[idx[:, "B0":"B1"], :]
               foo  bar
        A0 B0    0    1
           B1    2    3
        A1 B0    8    9
           B1   10   11
    '''
    
    def __getitem__(self, arg):
        return arg


IndexSlice = _IndexSlice()
IndexSlice.__module__ = 'pandas'

class IndexingMixin:
    '''
    Mixin for adding .loc/.iloc/.at/.iat to Dataframes and Series.
    '''
    iloc = (lambda self = None: _iLocIndexer('iloc', self))()
    loc = (lambda self = None: _LocIndexer('loc', self))()
    at = (lambda self = None: _AtIndexer('at', self))()
    iat = (lambda self = None: _iAtIndexer('iat', self))()


class _LocationIndexer(NDFrameIndexerBase):
    _valid_types: 'str' = '_LocationIndexer'
    _takeable: 'bool' = None
    __call__ = (lambda self = None, axis = None: new_self = type(self)(self.name, self.obj)# WARNING: Decompyle incomplete
)()
    
    def _get_setitem_indexer(self, key):
        '''
        Convert a potentially-label-based key into a positional indexer.
        '''
        if self.name == 'loc':
            self._ensure_listlike_indexer(key, axis = self.axis)
    # WARNING: Decompyle incomplete

    _maybe_mask_setitem_value = (lambda self, indexer, value: if isinstance(indexer, tuple) and len(indexer) == 2 and isinstance(value, (ABCSeries, ABCDataFrame)):
(pi, icols) = indexerndim = value.ndimif com.is_bool_indexer(pi) and len(value) == len(pi):
newkey = pi.nonzero()[0]if is_scalar_indexer(icols, self.ndim - 1) and ndim == 1:
if len(newkey) == 0:
value = value.iloc[:0]else:
value = self.obj.iloc._align_series(indexer, value)indexer = (newkey, icols)elif isinstance(icols, np.ndarray) and icols.dtype.kind == 'i' and len(icols) == 1:
if ndim == 1:
value = self.obj.iloc._align_series(indexer, value)indexer = (newkey, icols)elif ndim == 2 and value.shape[1] == 1:
if len(newkey) == 0:
value = value.iloc[:0]else:
value = self.obj.iloc._align_frame(indexer, value)indexer = (newkey, icols)elif com.is_bool_indexer(indexer):
indexer = indexer.nonzero()[0](indexer, value))()
    _ensure_listlike_indexer = (lambda self = None, key = final, axis = final, value = (None, None): column_axis = 1if self.ndim != 2:
None# WARNING: Decompyle incomplete
)()
    __setitem__ = (lambda self = None, key = None, value = final: pass# WARNING: Decompyle incomplete
)()
    
    def _validate_key(self = None, key = None, axis = None):
        '''
        Ensure that key is valid for current indexer.

        Parameters
        ----------
        key : scalar, slice or list-like
            Key requested.
        axis : int
            Dimension on which the indexing is being made.

        Raises
        ------
        TypeError
            If the key (or some element of it) has wrong type.
        IndexError
            If the key (or some element of it) is out of bounds.
        KeyError
            If the key was not found.
        '''
        raise AbstractMethodError(self)

    _expand_ellipsis = (lambda self = None, tup = None:
