# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: api.pyc (Python 3.11)

'''
This is a pseudo-public API for downstream libraries.  We ask that downstream
authors

1) Try to avoid using internals directly altogether, and failing that,
2) Use only functions exposed here (or in core.internals)

'''
from __future__ import annotations
from typing import TYPE_CHECKING
import warnings
import numpy as np
from pandas._libs.internals import BlockPlacement
from pandas.errors import Pandas4Warning
from pandas.core.dtypes.common import pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype, ExtensionDtype, PeriodDtype
from pandas.core.arrays import DatetimeArray, TimedeltaArray
from pandas.core.construction import extract_array
from pandas.core.internals.blocks import DatetimeLikeBlock, check_ndim, ensure_block_shape, extract_pandas_array, get_block_type, maybe_coerce_values
if TYPE_CHECKING:
    from pandas._typing import ArrayLike, Dtype
    from pandas.core.internals.blocks import Block

def _make_block(values = None, placement = None):
    '''
    This is an analogue to blocks.new_block(_2d) that ensures:
    1) correct dimension for EAs that support 2D (`ensure_block_shape`), and
    2) correct EA class for datetime64/timedelta64 (`maybe_coerce_values`).

    The input `values` is assumed to be either numpy array or ExtensionArray:
    - In case of a numpy array, it is assumed to already be in the expected
      shape for Blocks (2D, (cols, rows)).
    - In case of an ExtensionArray the input can be 1D, also for EAs that are
      internally stored as 2D.

    For the rest no preprocessing or validation is done, except for those dtypes
    that are internally stored as EAs but have an exact numpy equivalent (and at
    the moment use that numpy dtype), i.e. datetime64/timedelta64.
    '''
    dtype = values.dtype
    klass = get_block_type(dtype)
    placement_obj = BlockPlacement(placement)
    if isinstance(dtype, ExtensionDtype) or dtype._supports_2d or isinstance(values, (DatetimeArray, TimedeltaArray)):
        values = ensure_block_shape(values, ndim = 2)
    values = maybe_coerce_values(values)
    return klass(values, ndim = 2, placement = placement_obj)


class _DatetimeTZBlock(DatetimeLikeBlock):
    values: 'DatetimeArray' = 'implement a datetime64 block with a tz attribute'
    __slots__ = ()


def make_block(values = None, placement = None, klass = None, ndim = (None, None, None), dtype = ('dtype', 'Dtype | None', 'return', 'Block')):
    '''
    This is a pseudo-public analogue to blocks.new_block.

    We ask that downstream libraries use this rather than any fully-internal
    APIs, including but not limited to:

    - core.internals.blocks.make_block
    - Block.make_block
    - Block.make_block_same_class
    - Block.__init__
    '''
    warnings.warn('make_block is deprecated and will be removed in a future version. Use pd.api.internals.create_dataframe_from_blocks or (recommended) higher-level public APIs instead.', Pandas4Warning, stacklevel = 2)
# WARNING: Decompyle incomplete


def _maybe_infer_ndim(values = None, placement = None, ndim = None):
    '''
    If `ndim` is not provided, infer it from placement and values.
    '''
    pass
# WARNING: Decompyle incomplete


def maybe_infer_ndim(values = None, placement = None, ndim = None):
    '''
    If `ndim` is not provided, infer it from placement and values.
    '''
    warnings.warn('maybe_infer_ndim is deprecated and will be removed in a future version.', Pandas4Warning, stacklevel = 2)
    return _maybe_infer_ndim(values, placement, ndim)
