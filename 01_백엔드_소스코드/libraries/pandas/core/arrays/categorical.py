# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: categorical.pyc (Python 3.11)

from __future__ import annotations
from csv import QUOTE_NONNUMERIC
from functools import partial
import itertools
import operator
from shutil import get_terminal_size
from typing import TYPE_CHECKING, Literal, Self, cast, overload
import warnings
import numpy as np
from pandas._config import get_option
from pandas._libs import NaT, algos as libalgos, lib
from pandas._libs.arrays import NDArrayBacked
from pandas.compat.numpy import function as nv
from pandas.errors import Pandas4Warning
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import validate_bool_kwarg
from pandas.core.dtypes.cast import coerce_indexer_dtype, find_common_type
from pandas.core.dtypes.common import ensure_int64, ensure_platform_int, is_any_real_numeric_dtype, is_bool_dtype, is_dict_like, is_hashable, is_integer_dtype, is_list_like, is_scalar, needs_i8_conversion, pandas_dtype
from pandas.core.dtypes.dtypes import ArrowDtype, CategoricalDtype, CategoricalDtypeType, ExtensionDtype
from pandas.core.dtypes.generic import ABCIndex, ABCSeries
from pandas.core.dtypes.missing import is_valid_na_for_dtype, isna
from pandas.core import algorithms, arraylike, ops
from pandas.core.accessor import PandasDelegate, delegate_names
from pandas.core.algorithms import factorize, take_nd
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray, ravel_compat
from pandas.core.base import ExtensionArray, NoNewAttributesMixin, PandasObject

common
from pandas.core.construction import extract_array, sanitize_array
sanitize_array = sanitize_array
import pandas.core.common, core
from pandas.core.ops.common import unpack_zerodim_and_defer
from pandas.core.sorting import nargsort
from pandas.core.strings.object_array import ObjectStringArrayMixin
from pandas.io.formats import console
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Iterator, Sequence
    from pandas._typing import ArrayLike, AstypeArg, AxisInt, Dtype, NpDtype, Ordered, Shape, SortKind, npt
    from pandas import DataFrame, Index, Series

def _cat_compare_op(op):
    pass
# WARNING: Decompyle incomplete


def contains(cat = None, key = None, container = None):
    '''
    Helper for membership check for ``key`` in ``cat``.

    This is a helper method for :method:`__contains__`
    and :class:`CategoricalIndex.__contains__`.

    Returns True if ``key`` is in ``cat.categories`` and the
    location of ``key`` in ``categories`` is in ``container``.

    Parameters
    ----------
    cat : :class:`Categorical`or :class:`categoricalIndex`
    key : a hashable object
        The key to check membership for.
    container : Container (e.g. list-like or mapping)
        The container to check for membership in.

    Returns
    -------
    is_in : bool
        True if ``key`` is in ``self.categories`` and location of
        ``key`` in ``categories`` is in ``container``, else False.

    Notes
    -----
    This method does not check for NaN values. Do that separately
    before calling this method.
    '''
    pass
# WARNING: Decompyle incomplete

Categorical = <NODE:12>()
CategoricalAccessor = <NODE:12>()()

def _get_codes_for_values(values = set_module('pandas'), categories = delegate_names(delegate = Categorical, accessors = [
    'categories',
    'ordered'], typ = 'property')):
    '''
    utility routine to turn values into codes given the specified categories

    If `values` is known to be a Categorical, use recode_for_categories instead.
    '''
    codes = categories.get_indexer_for(values)
    wrong = (codes == -1) & ~isna(values)
    if wrong.any():
        warnings.warn("Constructing a Categorical with a dtype and values containing non-null entries not in that dtype's categories is deprecated and will raise in a future version.", Pandas4Warning, stacklevel = find_stack_level())
    return coerce_indexer_dtype(codes, categories)


def recode_for_categories(codes = None, old_categories = None, new_categories = None, *, copy, warn):
    '''
    Convert a set of codes for to a new set of categories

    Parameters
    ----------
    codes : np.ndarray
    old_categories, new_categories : Index
    copy: bool, default True
        Whether to copy if the codes are unchanged.
    warn : bool, default False
        Whether to warn on silent-NA mapping.

    Returns
    -------
    new_codes : np.ndarray[np.int64]

    Examples
    --------
    >>> old_cat = pd.Index(["b", "a", "c"])
    >>> new_cat = pd.Index(["a", "b"])
    >>> codes = np.array([0, 1, 1, 2])
    >>> recode_for_categories(codes, old_cat, new_cat, copy=True)
    array([ 1,  0,  0, -1], dtype=int8)
    '''
    if len(old_categories) == 0:
        if copy:
            return codes.copy()
        return None
    if None.equals(old_categories):
        if copy:
            return codes.copy()
        return None
    codes_in_old_cats = None.get_indexer_for(old_categories)
    if warn:
        wrong = codes_in_old_cats == -1
        if wrong.any():
            warnings.warn("Constructing a Categorical with a dtype and values containing non-null entries not in that dtype's categories is deprecated and will raise in a future version.", Pandas4Warning, stacklevel = find_stack_level())
    indexer = coerce_indexer_dtype(codes_in_old_cats, new_categories)
    new_codes = take_nd(indexer, codes, fill_value = -1)
    return new_codes


def factorize_from_iterable(values = None):
    '''
    Factorize an input `values` into `categories` and `codes`. Preserves
    categorical dtype in `categories`.

    Parameters
    ----------
    values : list-like

    Returns
    -------
    codes : ndarray
    categories : Index
        If `values` has a categorical dtype, then `categories` is
        a CategoricalIndex keeping the categories and order of `values`.
    '''
    CategoricalIndex = CategoricalIndex
    import pandas
    if not is_list_like(values):
        raise TypeError('Input must be list-like')
    vdtype = getattr(values, 'dtype', None)
    if isinstance(vdtype, CategoricalDtype):
        values = extract_array(values)
        cat_codes = np.arange(len(values.categories), dtype = values.codes.dtype)
        cat = Categorical.from_codes(cat_codes, dtype = values.dtype, validate = False)
        categories = CategoricalIndex(cat)
        codes = values.codes
    else:
        cat = Categorical(values, ordered = False)
        categories = cat.categories
        codes = cat.codes
    return (codes, categories)


def factorize_from_iterables(iterables = None):
    '''
    A higher-level wrapper over `factorize_from_iterable`.

    Parameters
    ----------
    iterables : list-like of list-likes

    Returns
    -------
    codes : list of ndarrays
    categories : list of Indexes

    Notes
    -----
    See `factorize_from_iterable` for more info.
    '''
    if len(iterables) == 0:
        return ([], [])
# WARNING: Decompyle incomplete
