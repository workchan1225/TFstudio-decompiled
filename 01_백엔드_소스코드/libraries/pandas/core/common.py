# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

__doc__ = '\nMisc tools for implementing data structures\n\nNote: pandas.core.common is *not* part of the public API.\n'
from __future__ import annotations
import builtins
from collections import abc, defaultdict
from collections.abc import Callable, Collection, Generator, Hashable, Iterable, Sequence
import contextlib
from functools import partial
import inspect
import sys
from typing import TYPE_CHECKING, Any, Concatenate, TypeVar, cast, overload
import numpy as np
from pandas._libs import lib
from pandas.core.dtypes.cast import construct_1d_object_array_from_listlike
from pandas.core.dtypes.common import is_bool_dtype, is_integer
from pandas.core.dtypes.generic import ABCExtensionArray, ABCIndex, ABCMultiIndex, ABCNumpyExtensionArray, ABCSeries
from pandas.core.dtypes.inference import iterable_not_string
from pandas.core.col import Expression
if TYPE_CHECKING:
    from pandas._typing import AnyArrayLike, ArrayLike, NpDtype, P, RandomState, T
    from pandas import Index

def flatten(line):
    """
    Flatten an arbitrarily nested sequence.

    Parameters
    ----------
    line : sequence
        The non string sequence to flatten

    Notes
    -----
    This doesn't consider strings sequences.

    Returns
    -------
    flattened : generator
    """
    pass
# WARNING: Decompyle incomplete


def consensus_name_attr(objs):
    name = objs[0].name
    for obj in objs[1:]:
        if obj.name != name:
            name = None
        
        except ValueError:
            name = None
        return name


def is_bool_indexer(key = None):
    '''
    Check whether `key` is a valid boolean indexer.

    Parameters
    ----------
    key : Any
        Only list-likes may be considered boolean indexers.
        All other types are not considered a boolean indexer.
        For array-like input, boolean ndarrays or ExtensionArrays
        with ``_is_boolean`` set are considered boolean indexers.

    Returns
    -------
    bool
        Whether `key` is a valid boolean indexer.

    Raises
    ------
    ValueError
        When the array is an object-dtype ndarray or ExtensionArray
        and contains missing values.

    See Also
    --------
    check_array_indexer : Check that `key` is a valid array to index,
        and convert to an ndarray.
    '''
    if not isinstance(key, (ABCSeries, np.ndarray, ABCIndex, ABCExtensionArray, ABCNumpyExtensionArray)) and isinstance(key, ABCMultiIndex):
        if key.dtype == np.object_:
            key_array = np.asarray(key)
            if not lib.is_bool_array(key_array):
                na_msg = 'Cannot mask with non-boolean array containing NA / NaN values'
                if lib.is_bool_array(key_array, skipna = True):
                    raise ValueError(na_msg)
                return False
            return None
        if None(key.dtype):
            return True
    if isinstance(key, list) and len(key) > 0:
        if type(key) is not list:
            key = list(key)
        return lib.is_bool_list(key)


def cast_scalar_indexer(val):
    '''
    Disallow indexing with a float key, even if that key is a round number.

    Parameters
    ----------
    val : scalar

    Returns
    -------
    outval : scalar
    '''
    if lib.is_float(val) and val.is_integer():
        raise IndexError('Indexing with a float is no longer supported. Manually convert to an integer key instead.')
    return val


def not_none(*args):
    '''
    Returns a generator consisting of the arguments that are not None.
    '''
    return args()


def any_none(*args):
    '''
    Returns a boolean indicating if any argument is None.
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(args())


def all_none(*args):
    '''
    Returns a boolean indicating if all arguments are None.
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(args())


def any_not_none(*args):
    '''
    Returns a boolean indicating if any argument is not None.
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(args())


def all_not_none(*args):
    '''
    Returns a boolean indicating if all arguments are not None.
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(args())


def count_not_none(*args):
    '''
    Returns the count of arguments that are not None.
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(args())

asarray_tuplesafe = (lambda values = None, dtype = None: pass)()
asarray_tuplesafe = (lambda values = None, dtype = None: pass)()

def asarray_tuplesafe(values = None, dtype = None):
    if not isinstance(values, (list, tuple)) and hasattr(values, '__array__'):
        values = list(values)
    elif isinstance(values, ABCIndex):
        return values._values
    if isinstance(values, ABCSeries):
        return values._values
    if None(values, list) and dtype in (np.object_, object):
        return construct_1d_object_array_from_listlike(values)
    
    try:
        result = np.asarray(values, dtype = dtype)
    except ValueError:
        return 

    if issubclass(result.dtype.type, str):
        pass
    if result.ndim == 2:
        
        def values()(.0):
            return [ tuple(x) for x in .0 ]

        result = construct_1d_object_array_from_listlike(values)
    return result


def index_labels_to_array(labels = None, dtype = None):
    '''
    Transform label or iterable of labels to array, for use in Index.

    Parameters
    ----------
    dtype : dtype
        If specified, use as dtype of the resulting array, otherwise infer.

    Returns
    -------
    array
    '''
    if isinstance(labels, (str, tuple)):
        labels = [
            labels]
    if not isinstance(labels, (list, np.ndarray)):
        
        try:
            labels = list(labels)
        except TypeError:
            labels = [
                labels]

        rlabels = asarray_tuplesafe(labels, dtype = dtype)
        return rlabels


def maybe_make_list(obj):
    pass
# WARNING: Decompyle incomplete


def maybe_iterable_to_list(obj = None):
    '''
    If obj is Iterable but not list-like, consume into list.
    '''
    if not isinstance(obj, abc.Iterable) and isinstance(obj, abc.Sized):
        return list(obj)
    obj = None(Collection, obj)
    return obj


def is_null_slice(obj = None):
