# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: construction.pyc (Python 3.11)

'''
Functions for preparing various inputs passed to the DataFrame or Series
constructors before passing them to a BlockManager.
'''
from __future__ import annotations
from collections import abc
from typing import TYPE_CHECKING, Any
import numpy as np
from numpy import ma
from pandas._config import using_string_dtype
from pandas._libs import lib
from pandas.core.dtypes.astype import astype_is_view
from pandas.core.dtypes.cast import construct_1d_arraylike_from_scalar, dict_compat, maybe_cast_to_datetime, maybe_convert_platform
from pandas.core.dtypes.common import is_1d_only_ea_dtype, is_integer_dtype, is_list_like, is_named_tuple, is_object_dtype, is_scalar
from pandas.core.dtypes.dtypes import BaseMaskedDtype, ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.dtypes.missing import isna
from pandas.core import algorithms, common as com
from pandas.core.arrays import ExtensionArray
from pandas.core.arrays.string_ import StringDtype
from pandas.core.construction import array as pd_array, extract_array, range_to_ndarray, sanitize_array
from pandas.core.indexes.api import DatetimeIndex, Index, TimedeltaIndex, default_index, ensure_index, get_objs_combined_axis, maybe_sequence_to_range, union_indexes
from pandas.core.internals.blocks import BlockPlacement, ensure_block_shape, new_block, new_block_2d
from pandas.core.internals.managers import create_block_manager_from_blocks, create_block_manager_from_column_arrays
if TYPE_CHECKING:
    from collections.abc import Hashable, Sequence
    from pandas._typing import ArrayLike, DtypeObj, Manager, npt

def arrays_to_mgr(arrays = None, columns = None, index = None, *, dtype, verify_integrity, consolidate):
    '''
    Segregate Series based on type and coerce into matrices.

    Needs to handle a lot of exceptional cases.
    '''
    pass
# WARNING: Decompyle incomplete


def rec_array_to_mgr(data, index = None, columns = None, dtype = None, copy = ('data', 'np.rec.recarray | np.ndarray', 'dtype', 'DtypeObj | None', 'copy', 'bool', 'return', 'Manager')):
    '''
    Extract from a masked rec array and create the manager.
    '''
    fdata = ma.getdata(data)
# WARNING: Decompyle incomplete


def ndarray_to_mgr(values, index = None, columns = None, dtype = None, copy = ('dtype', 'DtypeObj | None', 'copy', 'bool', 'return', 'Manager')):
    pass
# WARNING: Decompyle incomplete


def _check_values_indices_shape_match(values = None, index = None, columns = None):
    '''
    Check that the shape implied by our axes matches the actual shape of the
    data.
    '''
    if values.shape[1] != len(columns) or values.shape[0] != len(index):
        if  == values.shape[0], 0 or values.shape[0], 0 < len(index):
            pass
        
    else:
        raise ValueError('Empty data passed with indices specified.')
    (len(index), len(columns), implied) = values.shape
    raise ValueError(f'''Shape of passed values is {passed}, indices imply {implied}''')


def dict_to_mgr(data = None, index = None, columns = None, *, dtype, copy):
    '''
    Segregate Series based on type and coerce into matrices.
    Needs to handle a lot of exceptional cases.

    Used in DataFrame.__init__
    '''
    pass
# WARNING: Decompyle incomplete


def nested_data_to_arrays(data = None, columns = None, index = None, dtype = ('data', 'Sequence', 'columns', 'Index | None', 'index', 'Index | None', 'dtype', 'DtypeObj | None', 'return', 'tuple[list[ArrayLike], Index, Index]')):
    '''
    Convert a single sequence of arrays to multiple arrays.
    '''
    pass
# WARNING: Decompyle incomplete


def treat_as_nested(data = None):
