# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ops.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, NamedTuple
from pandas.core.dtypes.common import is_1d_only_ea_dtype
if TYPE_CHECKING:
    from collections.abc import Iterator
    from pandas._libs.internals import BlockPlacement
    from pandas._typing import ArrayLike
    from pandas.core.internals.blocks import Block
    from pandas.core.internals.managers import BlockManager

class BlockPairInfo(NamedTuple):
    rblk: 'Block' = 'BlockPairInfo'


def _iter_block_pairs(left = None, right = None):
    pass
# WARNING: Decompyle incomplete


def operate_blockwise(left = None, right = None, array_op = None):
    res_blks = []
    for lvals, rvals, locs, left_ea, right_ea, rblk in _iter_block_pairs(left, right):
        res_values = array_op(lvals, rvals)
        if not left_ea and right_ea and hasattr(res_values, 'reshape') and is_1d_only_ea_dtype(res_values.dtype):
            res_values = res_values.reshape(1, -1)
        nbs = rblk._split_op_result(res_values)
        _reset_block_mgr_locs(nbs, locs)
        res_blks.extend(nbs)
        new_mgr = type(right)(tuple(res_blks), axes = right.axes, verify_integrity = False)
        return new_mgr


def _reset_block_mgr_locs(nbs = None, locs = None):
    '''
    Reset mgr_locs to correspond to our original DataFrame.
    '''
    for nb in nbs:
        nblocs = locs[nb.mgr_locs.indexer]
        nb.mgr_locs = nblocs
        return None


def _get_same_shape_values(lblk = None, rblk = None, left_ea = None, right_ea = ('lblk', 'Block', 'rblk', 'Block', 'left_ea', 'bool', 'right_ea', 'bool', 'return', 'tuple[ArrayLike, ArrayLike]')):
    '''
    Slice lblk.values to align with rblk.  Squeeze if we have EAs.
    '''
    lvals = lblk.values
    rvals = rblk.values
# WARNING: Decompyle incomplete


def blockwise_all(left = None, right = None, op = None):
    '''
    Blockwise `all` reduction.
    '''
    for info in _iter_block_pairs(left, right):
        res = op(info.lvals, info.rvals)
        if not res:
            return False
        return True
