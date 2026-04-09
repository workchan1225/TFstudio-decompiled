# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multi.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable, Collection, Generator, Hashable, Iterable, Sequence
from functools import wraps
from itertools import zip_longest
from sys import getsizeof
from typing import TYPE_CHECKING, Any, Literal, Self, cast
import warnings
import numpy as np
from pandas._config import get_option
from pandas._libs import algos as libalgos, index as libindex, lib
from pandas._libs.hashtable import duplicated
from pandas._typing import AnyAll, AnyArrayLike, Axis, DropKeep, DtypeObj, F, IgnoreRaise, IndexLabel, IndexT, NaPosition, Scalar, Shape, npt
from pandas.compat.numpy import function as nv
from pandas.errors import InvalidIndexError, PerformanceWarning, UnsortedIndexError
from pandas.util._decorators import cache_readonly, set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.cast import coerce_indexer_dtype, maybe_unbox_numpy_scalar
from pandas.core.dtypes.common import ensure_int64, ensure_platform_int, is_hashable, is_integer, is_iterator, is_list_like, is_object_dtype, is_scalar, is_string_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype, ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.dtypes.inference import is_array_like
from pandas.core.dtypes.missing import array_equivalent, isna

algorithms
from pandas.core.array_algos.putmask import validate_putmask
import pandas.core.algorithms, core
from pandas.core.arrays import Categorical, ExtensionArray
from pandas.core.arrays.categorical import factorize_from_iterables, recode_for_categories

common
from pandas.core.construction import sanitize_array
import pandas.core.common, core


base
from pandas.core.indexes.base import Index, ensure_index, get_unanimous_names
ensure_index = ensure_index
get_unanimous_names = get_unanimous_names
import pandas.core.indexes.base, core, indexes
from pandas.core.indexes.frozen import FrozenList
from pandas.core.ops.invalid import make_invalid_op
from pandas.core.sorting import get_group_index, lexsort_indexer
from pandas.io.formats.printing import pprint_thing
if TYPE_CHECKING:
    from pandas import CategoricalIndex, DataFrame, Series

class MultiIndexUInt64Engine(libindex.UInt64Engine, libindex.BaseMultiIndexCodesEngine):
    '''Manages a MultiIndex by mapping label combinations to positive integers.

    The number of possible label combinations must not overflow the 64 bits integers.
    '''
    _base = libindex.UInt64Engine
    _codes_dtype = 'uint64'


class MultiIndexUInt32Engine(libindex.UInt32Engine, libindex.BaseMultiIndexCodesEngine):
    '''Manages a MultiIndex by mapping label combinations to positive integers.

    The number of possible label combinations must not overflow the 32 bits integers.
    '''
    _base = libindex.UInt32Engine
    _codes_dtype = 'uint32'


class MultiIndexUInt16Engine(libindex.UInt16Engine, libindex.BaseMultiIndexCodesEngine):
    '''Manages a MultiIndex by mapping label combinations to positive integers.

    The number of possible label combinations must not overflow the 16 bits integers.
    '''
    _base = libindex.UInt16Engine
    _codes_dtype = 'uint16'


class MultiIndexUInt8Engine(libindex.UInt8Engine, libindex.BaseMultiIndexCodesEngine):
    '''Manages a MultiIndex by mapping label combinations to positive integers.

    The number of possible label combinations must not overflow the 8 bits integers.
    '''
    _base = libindex.UInt8Engine
    _codes_dtype = 'uint8'


class MultiIndexPyIntEngine(libindex.ObjectEngine, libindex.BaseMultiIndexCodesEngine):
    '''Manages a MultiIndex by mapping label combinations to positive integers.

    This class manages those (extreme) cases in which the number of possible
    label combinations overflows the 64 bits integers, and uses an ObjectEngine
    containing Python integers.
    '''
    _base = libindex.ObjectEngine
    _codes_dtype = 'object'


def names_compat(meth = None):
    '''
    A decorator to allow either `name` or `names` keyword but not both.

    This makes it easier to share code with base class.
    '''
    pass
# WARNING: Decompyle incomplete

MultiIndex = <NODE:12>()

def _lexsort_depth(codes = None, nlevels = None):
    '''Count depth (up to a maximum of `nlevels`) with which codes are lexsorted.'''
    int64_codes = codes()
    for k in range(nlevels, 0, -1):
        if libalgos.is_lexsorted(int64_codes[:k]):
            
            return (lambda .0: [ ensure_int64(level_codes) for level_codes in .0 ]), k
        return 0


def sparsify_labels(label_list = None, start = None, sentinel = None):
    pass
# WARNING: Decompyle incomplete


def _get_na_rep(dtype = None):
    if isinstance(dtype, ExtensionDtype):
        return f'''{dtype.na_value}'''
    dtype_type = None.type
    return {
        np.timedelta64: 'NaT',
        np.datetime64: 'NaT' }.get(dtype_type, 'NaN')


def maybe_droplevels(index = None, key = None):
    '''
    Attempt to drop level or levels from the given index.

    Parameters
    ----------
    index: Index
    key : scalar or tuple

    Returns
    -------
    Index
    '''
    original_index = index
    if isinstance(key, tuple):
        for _ in key:
            index = index._drop_level_numbers([
                0])
        except ValueError:
            
            return None, original_index, 
    else:
        
        try:
            pass
        except ValueError:
            pass

        return index


def _coerce_indexer_frozen(array_like = None, categories = None, copy = None):
    '''
    Coerce the array-like indexer to the smallest integer dtype that can encode all
    of the given categories.

    Parameters
    ----------
    array_like : array-like
    categories : array-like
    copy : bool

    Returns
    -------
    np.ndarray
        Non-writeable.
    '''
    array_like = coerce_indexer_dtype(array_like, categories)
    if copy:
        array_like = array_like.copy()
    array_like.flags.writeable = False
    return array_like


def _require_listlike(level = None, arr = None, arrname = None):
    '''
    Ensure that level is either None or listlike, and arr is list-of-listlike.
    '''
    pass
# WARNING: Decompyle incomplete


def cartesian_product(X = None):
    '''
    Numpy version of itertools.product.
    Sometimes faster (for large inputs)...

    Parameters
    ----------
    X : list-like of list-likes

    Returns
    -------
    product : list of ndarrays

    Examples
    --------
    >>> cartesian_product([list("ABC"), [1, 2]])
    [array([\'A\', \'A\', \'B\', \'B\', \'C\', \'C\'], dtype=\'<U1\'), array([1, 2, 1, 2, 1, 2])]

    See Also
    --------
    itertools.product : Cartesian product of input iterables.  Equivalent to
        nested for-loops.
    '''
    pass
# WARNING: Decompyle incomplete
