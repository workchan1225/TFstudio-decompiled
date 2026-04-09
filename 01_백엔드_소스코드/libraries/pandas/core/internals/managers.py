# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: managers.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable, Hashable, Sequence
import itertools
from typing import TYPE_CHECKING, Any, Literal, NoReturn, Self, cast, final
import warnings
import numpy as np
from pandas._config.config import get_option
from pandas._libs import algos as libalgos, internals as libinternals, lib
from pandas._libs.internals import BlockPlacement, BlockValuesRefs
from pandas._libs.tslibs import Timestamp
from pandas.errors import AbstractMethodError, PerformanceWarning
from pandas.util._decorators import cache_readonly
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import validate_bool_kwarg
from pandas.core.dtypes.cast import find_common_type, infer_dtype_from_scalar, np_can_hold_element
from pandas.core.dtypes.common import ensure_platform_int, is_1d_only_ea_dtype, is_list_like
from pandas.core.dtypes.dtypes import CategoricalDtype, DatetimeTZDtype, ExtensionDtype, SparseDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.dtypes.missing import array_equals, isna

algorithms
from pandas.core.arrays import DatetimeArray
import pandas.core.algorithms, core
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray
from pandas.core.base import PandasObject
from pandas.core.construction import ensure_wrapped_if_datetimelike, extract_array
from pandas.core.indexers import maybe_convert_indices
from pandas.core.indexes.api import Index, default_index, ensure_index
from pandas.core.internals.blocks import Block, NumpyBlock, ensure_block_shape, extend_blocks, get_block_type, maybe_coerce_values, new_block, new_block_2d
from pandas.core.internals.ops import blockwise_all, operate_blockwise
if TYPE_CHECKING:
    from collections.abc import Generator
    from pandas._typing import ArrayLike, AxisInt, DtypeObj, QuantileInterpolation, Shape, npt
    from pandas.api.extensions import ExtensionArray

def interleaved_dtype(dtypes = None):
    '''
    Find the common dtype for `blocks`.

    Parameters
    ----------
    blocks : List[DtypeObj]

    Returns
    -------
    dtype : np.dtype, ExtensionDtype, or None
        None is returned when `blocks` is empty.
    '''
    if not len(dtypes):
        return None
    return None(dtypes)


def ensure_np_dtype(dtype = None):
    if isinstance(dtype, SparseDtype):
        dtype = dtype.subtype
        dtype = cast(np.dtype, dtype)
    elif isinstance(dtype, ExtensionDtype):
        dtype = np.dtype('object')
    elif dtype == np.dtype(str):
        dtype = np.dtype('object')
    return dtype


class BaseBlockManager(PandasObject):
    """
    Core internal data structure to implement DataFrame, Series, etc.

    Manage a bunch of labeled 2D mixed-type ndarrays. Essentially it's a
    lightweight blocked set of labeled data to be manipulated by the DataFrame
    public API class

    Attributes
    ----------
    shape
    ndim
    axes
    values
    items

    Methods
    -------
    set_axis(axis, new_labels)
    copy(deep=True)

    get_dtypes

    apply(func, axes, block_filter_fn)

    get_bool_data
    get_numeric_data

    get_slice(slice_like, axis)
    get(label)
    iget(loc)

    take(indexer, axis)
    reindex_axis(new_labels, axis)
    reindex_indexer(new_labels, indexer, axis)

    delete(label)
    insert(loc, label, value)
    set(label, value)

    Parameters
    ----------
    blocks: Sequence of Block
    axes: Sequence of Index
    verify_integrity: bool, default True

    Notes
    -----
    This is *not* a public API class
    """
    axes: 'list[Index]' = ()
    _is_consolidated: 'bool' = (lambda self = None: raise NotImplementedError)()
    
    def __init__(self = None, blocks = None, axes = None, verify_integrity = (True,)):
        raise NotImplementedError

    __len__ = (lambda self = None: len(self.items))()
    shape = (lambda self = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(self.axes())
)()
    from_blocks = (lambda cls = None, blocks = None, axes = classmethod: raise NotImplementedError)()
    blknos = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    blklocs = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def make_empty(self = None, axes = None):
        '''return an empty BlockManager with the items axis of len 0'''
        pass
    # WARNING: Decompyle incomplete

    
    def __bool__(self = None):
        return True

    
    def set_axis(self = None, axis = None, new_labels = None):
        self._validate_set_axis(axis, new_labels)
        self.axes[axis] = new_labels

    _validate_set_axis = (lambda self = None, axis = None, new_labels = final: old_len = len(self.axes[axis])new_len = len(new_labels)if axis == 1 and len(self.items) == 0:
Noneif None != old_len:
raise ValueError(f'''Length mismatch: Expected axis has {old_len} elements, new values have {new_len} elements'''))()
    is_single_block = (lambda self = None: len(self.blocks) == 1)()
    items = (lambda self = None: self.axes[0])()
    
    def _has_no_reference(self = None, i = None):
        '''
        Check for column `i` if it has references.
        (whether it references another array or is itself being referenced)
        Returns True if the column has no references.
        '''
        blkno = self.blknos[i]
        return self._has_no_reference_block(blkno)

    
    def _has_no_reference_block(self = None, blkno = None):
        '''
        Check for block `i` if it has references.
        (whether it references another array or is itself being referenced)
        Returns True if the block has no references.
        '''
        return not self.blocks[blkno].refs.has_reference()

    
    def add_references(self = None, mgr = None):
        '''
        Adds the references from one manager to another. We assume that both
        managers have the same block structure.
        '''
        if len(self.blocks) != len(mgr.blocks):
            return None
        for i, blk in None(self.blocks):
            blk.refs = mgr.blocks[i].refs
            blk.refs.add_reference(blk)
            return None

    
    def references_same_values(self = None, mgr = None, blkno = None):
        '''
        Checks if two blocks from two different block managers reference the
        same underlying values.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_dtypes(self = None):
        dtypes = (lambda .0: [ blk.dtype for blk in .0 ])(self.blocks(), dtype = object)
        return dtypes.take(self.blknos)

    arrays = (lambda self = None: self.blocks())()
    
    def __repr__(self = None):
        output = type(self).__name__
        for i, ax in enumerate(self.axes):
            if i == 0:
                output += f'''\nItems: {ax}'''
                continue
            output += f'''\nAxis {i}: {ax}'''
            for block in self.blocks:
                output += f'''\n{block}'''
                return output

    
    def _equal_values(self = None, other = None):
        '''
        To be implemented by the subclasses. Only check the column values
        assuming shape and indexes have already been checked.
        '''
        raise AbstractMethodError(self)

    equals = (lambda self = None, other = None: if not isinstance(other, type(self)):
Falseother_axes = other.axesself_axes = None.axesif len(self_axes) != len(other_axes):
Falseif not (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(self_axes, other_axes, strict = True)()):
            return False
        return None._equal_values(other)
)()
    
    def apply(self = None, f = None, align_keys = None, **kwargs):
        '''
        Iterate over the blocks, collect and create a new BlockManager.

        Parameters
        ----------
        f : str or callable
            Name of the Block method to apply.
        align_keys: List[str] or None, default None
        **kwargs
            Keywords to pass to `f`

        Returns
        -------
        BlockManager
        '''
        pass
    # WARNING: Decompyle incomplete

    isna = (lambda self = None, func = None: self.apply('apply', func = func))()
    fillna = (lambda self = None, value = None, limit = final, inplace = ('limit', 'int | None', 'inplace', 'bool', 'return', 'Self'): pass# WARNING: Decompyle incomplete
)()
    where = (lambda self = None, other = None, cond = final, align = ('align', 'bool', 'return', 'Self'): if align:
align_keys = [
'other',
'cond']else:
align_keys = [
'cond']other = extract_array(other, extract_numpy = True)self.apply('where', align_keys = align_keys, other = other, cond = cond))()
    putmask = (lambda self = None, mask = None, new = final, align = (True,): if align:
align_keys = [
'new',
'mask']else:
align_keys = [
'mask']new = extract_array(new, extract_numpy = True)self.apply('putmask', align_keys = align_keys, mask = mask, new = new))()
    round = (lambda self = None, decimals = None: self.apply('round', decimals = decimals))()
    replace = (lambda self = None, to_replace = None, value = final, inplace = ('inplace', 'bool', 'return', 'Self'): inplace = validate_bool_kwarg(inplace, 'inplace')# WARNING: Decompyle incomplete
)()
    replace_regex = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    replace_list = (lambda self = None, src_list = None, dest_list = final, inplace = (False, False), regex = ('src_list', 'list[Any]', 'dest_list', 'list[Any]', 'inplace', 'bool', 'regex', 'bool', 'return', 'Self'): inplace = validate_bool_kwarg(inplace, 'inplace')bm = self.apply('replace_list', src_list = src_list, dest_list = dest_list, inplace = inplace, regex = regex)bm._consolidate_inplace()bm)()
    
    def interpolate(self = None, inplace = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def pad_or_backfill(self = None, inplace = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def shift(self = None, periods = None, fill_value = None):
        if fill_value is lib.no_default:
            fill_value = None
        return self.apply('shift', periods = periods, fill_value = fill_value)

    
    def setitem(self = None, indexer = None, value = None):
