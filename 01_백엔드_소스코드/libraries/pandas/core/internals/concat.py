# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: concat.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, cast
import numpy as np
from pandas._libs import NaT, algos as libalgos, internals as libinternals, lib
from pandas._libs.missing import NA
from pandas.util._decorators import cache_readonly
from pandas.core.dtypes.cast import ensure_dtype_can_hold_na, find_common_type
from pandas.core.dtypes.common import is_1d_only_ea_dtype, needs_i8_conversion
from pandas.core.dtypes.concat import concat_compat
from pandas.core.dtypes.dtypes import ExtensionDtype
from pandas.core.dtypes.missing import is_valid_na_for_dtype
from pandas.core.construction import ensure_wrapped_if_datetimelike
from pandas.core.internals.blocks import ensure_block_shape, new_block_2d
from pandas.core.internals.managers import BlockManager, make_na_array
if TYPE_CHECKING:
    from collections.abc import Generator, Sequence
    from pandas._typing import ArrayLike, AxisInt, DtypeObj, Shape
    from pandas import Index
    from pandas.core.internals.blocks import Block, BlockPlacement

def concatenate_managers(mgrs_indexers = None, axes = None, concat_axis = None, copy = ('axes', 'list[Index]', 'concat_axis', 'AxisInt', 'copy', 'bool', 'return', 'BlockManager')):
    '''
    Concatenate block managers into one.

    Parameters
    ----------
    mgrs_indexers : list of (BlockManager, {axis: indexer,...}) tuples
    axes : list of Index
    concat_axis : int
    copy : bool

    Returns
    -------
    BlockManager
    '''
    pass
# WARNING: Decompyle incomplete


def _maybe_reindex_columns_na_proxy(axes = None, mgrs_indexers = None, needs_copy = None):
    """
    Reindex along columns so that all of the BlockManagers being concatenated
    have matching columns.

    Columns added in this reindexing have dtype=np.void, indicating they
    should be ignored when choosing a column's final dtype.
    """
    new_mgrs = []
    for mgr, indexers in mgrs_indexers:
        for i, indexer in indexers.items():
            mgr = mgr.reindex_indexer(axes[i], indexer, axis = i, only_slice = True, allow_dups = True, use_na_proxy = True)
            if not needs_copy and indexers:
                mgr = mgr.copy(deep = True)
        new_mgrs.append(mgr)
        return new_mgrs


def _is_homogeneous_mgr(mgr = None, first_dtype = None):
    '''
    Check if this Manager can be treated as a single ndarray.
    '''
    if mgr.nblocks != 1:
        return False
    blk = None.blocks[0]
    if not blk.mgr_locs.is_slice_like or blk.mgr_locs.as_slice.step == 1:
        return False
    return None.dtype == first_dtype


def _concat_homogeneous_fastpath(mgrs_indexers = None, shape = None, first_dtype = None):
    '''
    With single-Block managers with homogeneous dtypes (that can already hold nan),
    we avoid [...]
    '''
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(mgrs_indexers()):
        arrs = mgrs_indexers()
        arr = np.concatenate(arrs).T
        bp = libinternals.BlockPlacement(slice(shape[0]))
        nb = new_block_2d(arr, bp)
        return nb
    arr = all.empty(shape, dtype = first_dtype)
    if first_dtype == np.float64:
        take_func = libalgos.take_2d_axis0_float64_float64
    else:
        take_func = libalgos.take_2d_axis0_float32_float32
    start = 0
    for mgr, indexers in mgrs_indexers:
        mgr_len = mgr.shape[1]
        end = start + mgr_len
        if 0 in indexers:
            take_func(mgr.blocks[0].values, indexers[0], arr[(:, start:end)])
        else:
            arr[(:, start:end)] = mgr.blocks[0].values
        start += mgr_len
        bp = libinternals.BlockPlacement(slice(shape[0]))
        nb = new_block_2d(arr, bp)
        return nb


def _get_combined_plan(mgrs = None):
    pass
# WARNING: Decompyle incomplete


def _get_block_for_concat_plan(mgr = None, bp = None, blkno = None, *, max_len):
    blk = mgr.blocks[blkno]
    if len(bp) == len(blk.mgr_locs) and blk.mgr_locs.is_slice_like and blk.mgr_locs.as_slice.step == 1:
        nb = blk
    else:
        ax0_blk_indexer = mgr.blklocs[bp.indexer]
        slc = lib.maybe_indices_to_slice(ax0_blk_indexer, max_len)
        if isinstance(slc, slice):
            nb = blk.slice_block_columns(slc)
        else:
            nb = blk.take_block_columns(slc)
    return nb


class JoinUnit:
    
    def __init__(self = None, block = None):
        self.block = block

    
    def __repr__(self = None):
        return f'''{type(self).__name__}({self.block!r})'''

    
    def _is_valid_na_for(self = None, dtype = None):
        '''
        Check that we are all-NA of a type/dtype that is compatible with this dtype.
        Augments `self.is_na` with an additional check of the type of NA values.
        '''
        pass
    # WARNING: Decompyle incomplete

    is_na = (lambda self = None: blk = self.blockif blk.dtype.kind == 'V':
True)()
    
    def get_reindexed_values(self = None, empty_dtype = None, upcasted_na = None):
        pass
    # WARNING: Decompyle incomplete



def _concatenate_join_units(join_units = None, copy = None):
    '''
    Concatenate values from several join units along axis=1.
    '''
    pass
# WARNING: Decompyle incomplete


def _dtype_to_na_value(dtype = None, has_none_blocks = None):
    '''
    Find the NA value to go with this dtype.
    '''
    if isinstance(dtype, ExtensionDtype):
        return dtype.na_value
    if None.kind in 'mM':
        return dtype.type('NaT')
    if None.kind in 'fc':
        return dtype.type('NaN')
    if None.kind == 'b':
        return None
    if None.kind in 'iu':
        if not has_none_blocks:
            return None
        return None.nan
    if None.kind == 'O':
        return np.nan
    raise None


def _get_empty_dtype(join_units = None):
    '''
    Return dtype and N/A values to use when concatenating specified units.

    Returned N/A value may be None which means there was no casting involved.

    Returns
    -------
    dtype
    '''
    if (lambda .0: [ ju.block.dtype for ju in .0 ])(join_units()):
        empty_dtype = join_units[0].block.dtype
        return empty_dtype
    has_none_blocks = (lambda .0: pass# WARNING: Decompyle incomplete
)(join_units())
    dtypes = join_units()
    dtype = find_common_type(dtypes)
    if has_none_blocks:
        dtype = ensure_dtype_can_hold_na(dtype)
    return dtype


def _is_uniform_join_units(join_units = None):
    '''
    Check if the join units consist of blocks of uniform type that can
    be concatenated using Block.concat_same_type instead of the generic
    _concatenate_join_units (which uses `concat_compat`).

    '''
    pass
# WARNING: Decompyle incomplete
