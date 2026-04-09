# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hashing.pyc (Python 3.11)

'''
data hash pandas / numpy objects
'''
from __future__ import annotations
import itertools
from typing import TYPE_CHECKING
import numpy as np
from pandas._libs.hashing import hash_object_array
from pandas.core.dtypes.common import is_list_like
from pandas.core.dtypes.dtypes import CategoricalDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCExtensionArray, ABCIndex, ABCMultiIndex, ABCSeries
if TYPE_CHECKING:
    from collections.abc import Hashable, Iterable, Iterator
    from pandas._typing import ArrayLike, npt
    from pandas import DataFrame, Index, MultiIndex, Series
_default_hash_key = '0123456789123456'

def combine_hash_arrays(arrays = None, num_items = None):
    """
    Parameters
    ----------
    arrays : Iterator[np.ndarray]
    num_items : int

    Returns
    -------
    np.ndarray[uint64]

    Should be the same as CPython's tupleobject.c
    """
    
    try:
        first = next(arrays)
    except StopIteration:
        return 

    np.uint64(1000003) = itertools.chain([
        first], arrays)
    out = np.zeros_like(first) + np.uint64(3430008)
    last_i = 0
# WARNING: Decompyle incomplete


def hash_pandas_object(obj = None, index = None, encoding = None, hash_key = (True, 'utf8', _default_hash_key, True), categorize = ('obj', 'Index | DataFrame | Series', 'index', 'bool', 'encoding', 'str', 'hash_key', 'str | None', 'categorize', 'bool', 'return', 'Series')):
    """
    Return a data hash of the Index/Series/DataFrame.

    The hash is computed element-wise using the underlying data values,
    and optionally includes the index when hashing a Series or DataFrame.

    Parameters
    ----------
    obj : Index, Series, or DataFrame
        The pandas object to hash.
    index : bool, default True
        Include the index in the hash (if Series/DataFrame).
    encoding : str, default 'utf8'
        Encoding for data & key when strings.
    hash_key : str, default _default_hash_key
        Hash_key for string key to encode.
    categorize : bool, default True
        Whether to first categorize object arrays before hashing. This is more
        efficient when the array contains duplicate values.

    Returns
    -------
    Series of uint64
        Same length as the object.

    See Also
    --------
    util.hash_array : Return a hash of the given array.
    util.hash_tuples : Hash a MultiIndex or listlike-of-tuples efficiently.

    Examples
    --------
    >>> pd.util.hash_pandas_object(pd.Series([1, 2, 3]))
    0    14639053686158035780
    1     3869563279212530728
    2      393322362522515241
    dtype: uint64
    """
    pass
# WARNING: Decompyle incomplete


def hash_tuples(vals = None, encoding = None, hash_key = None):
    """
    Hash a MultiIndex / listlike-of-tuples efficiently.

    Parameters
    ----------
    vals : MultiIndex or listlike-of-tuples
    encoding : str, default 'utf8'
    hash_key : str, default _default_hash_key

    Returns
    -------
    ndarray[np.uint64] of hashed values
    """
    pass
# WARNING: Decompyle incomplete


def hash_array(vals = None, encoding = None, hash_key = None, categorize = ('utf8', _default_hash_key, True)):
    """
    Given a 1d array, return an array of deterministic integers.

    Parameters
    ----------
    vals : ndarray or ExtensionArray
        The input array to hash.
    encoding : str, default 'utf8'
        Encoding for data & key when strings.
    hash_key : str, default _default_hash_key
        Hash_key for string key to encode.
    categorize : bool, default True
        Whether to first categorize object arrays before hashing. This is more
        efficient when the array contains duplicate values.

    Returns
    -------
    ndarray[np.uint64, ndim=1]
        Hashed values, same length as the vals.

    See Also
    --------
    util.hash_pandas_object : Return a data hash of the Index/Series/DataFrame.
    util.hash_tuples : Hash a MultiIndex / listlike-of-tuples efficiently.

    Examples
    --------
    >>> pd.util.hash_array(np.array([1, 2, 3]))
    array([ 6238072747940578789, 15839785061582574730,  2185194620014831856],
      dtype=uint64)
    """
    if not hasattr(vals, 'dtype'):
        raise TypeError('must pass an ndarray-like')
    if isinstance(vals, ABCExtensionArray):
        return vals._hash_pandas_object(encoding = encoding, hash_key = hash_key, categorize = categorize)
    if not None(vals, np.ndarray):
        raise TypeError(f'''hash_array requires np.ndarray or ExtensionArray, not {type(vals).__name__}. Use hash_pandas_object instead.''')
    return _hash_ndarray(vals, encoding, hash_key, categorize)


def _hash_ndarray(vals = None, encoding = None, hash_key = None, categorize = ('utf8', _default_hash_key, True)):
    '''
    See hash_array.__doc__.
    '''
    dtype = vals.dtype
    if np.issubdtype(dtype, np.complex128):
        hash_real = _hash_ndarray(vals.real, encoding, hash_key, categorize)
        hash_imag = _hash_ndarray(vals.imag, encoding, hash_key, categorize)
        return hash_real + 23 * hash_imag
    if None == bool:
        vals = vals.astype('u8')
    elif issubclass(dtype.type, (np.datetime64, np.timedelta64)):
        vals = vals.view('i8').astype('u8', copy = False)
    elif issubclass(dtype.type, np.number) and dtype.itemsize <= 8:
        vals = vals.view(f'''u{vals.dtype.itemsize}''').astype('u8')
    elif categorize:
        Categorical = Categorical
        Index = Index
        factorize = factorize
        import pandas
        (codes, categories) = factorize(vals, sort = False)
        tdtype = CategoricalDtype(categories = Index(categories, copy = False), ordered = False)
        cat = Categorical._simple_new(codes, tdtype)
        return cat._hash_pandas_object(encoding = encoding, hash_key = hash_key, categorize = False)
    
    try:
        vals = hash_object_array(vals, hash_key, encoding)
    except TypeError:
        vals = hash_object_array(vals.astype(str).astype(object), hash_key, encoding)

    vals ^= vals >> 30
    vals *= np.uint64(0xBF58476D1CE4E5B9)
    vals ^= vals >> 27
    vals *= np.uint64(0x94D049BB133111EB)
    vals ^= vals >> 31
    return vals
