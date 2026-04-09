# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''
Base and utility classes for pandas objects.
'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Generic, Literal, Self, cast, final, overload
import numpy as np
from pandas._libs import lib
from pandas._typing import AxisInt, DtypeObj, IndexLabel, NDFrameT, Shape, npt
from pandas.compat import PYPY
from pandas.compat.numpy import function as nv
from pandas.errors import AbstractMethodError
from pandas.util._decorators import cache_readonly
from pandas.core.dtypes.cast import can_hold_element
from pandas.core.dtypes.common import is_object_dtype, is_scalar
from pandas.core.dtypes.dtypes import ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCIndex, ABCMultiIndex, ABCSeries
from pandas.core.dtypes.missing import isna, remove_na_arraylike
from pandas.core import algorithms, nanops, ops
from pandas.core.accessor import DirNamesMixin
from pandas.core.arraylike import OpsMixin
from pandas.core.arrays import ExtensionArray
from pandas.core.construction import ensure_wrapped_if_datetimelike, extract_array
if TYPE_CHECKING:
    from collections.abc import Hashable, Iterator
    from pandas._typing import DropKeep, NumpySorter, NumpyValueArrayLike, ScalarLike_co
    from pandas import DataFrame, Index, Series

class PandasObject(DirNamesMixin):
    pass
# WARNING: Decompyle incomplete


class NoNewAttributesMixin:
    '''
    Mixin which prevents adding new attributes.

    Prevents additional attributes via xxx.attribute = "something" after a
    call to `self.__freeze()`. Mainly used to prevent the user from using
    wrong attributes on an accessor (`Series.cat/.str/.dt`).

    If you really want to add a new attribute at a later time, you need to use
    `object.__setattr__(self, key, value)`.
    '''
    
    def _freeze(self = None):
        '''
        Prevents setting additional attributes.
        '''
        object.__setattr__(self, '__frozen', True)

    
    def __setattr__(self = None, key = None, value = None):
        pass
    # WARNING: Decompyle incomplete



def SelectionMixin():
    '''SelectionMixin'''
    obj: 'NDFrameT' = '\n    mixin implementing the selection & aggregation interface on a group-like\n    object sub-classes need to define: obj, exclusions\n    '
    exclusions: 'frozenset[Hashable]' = None
    _internal_names = [
        '_cache',
        '__setstate__']
    _internal_names_set = set(_internal_names)
    _selection_list = (lambda self: if not isinstance(self._selection, (list, tuple, ABCSeries, ABCIndex, np.ndarray)):
[
self._selection]None._selection)()()
    _selected_obj = (lambda self: pass# WARNING: Decompyle incomplete
)()
    ndim = (lambda self = cache_readonly: self._selected_obj.ndim)()()
    _obj_with_exclusions = (lambda self: if isinstance(self.obj, ABCSeries):
self.obj# WARNING: Decompyle incomplete
)()()
    
    def __getitem__(self, key):
        pass
    # WARNING: Decompyle incomplete

    
    def _gotitem(self = property, key = final, ndim = cache_readonly, subset = (None,)):
        '''
        sub-classes to define
        return a sliced object

        Parameters
        ----------
        key : str / list of selections
        ndim : {1, 2}
            requested ndim of result
        subset : object, default None
            subset to act on
        '''
        raise AbstractMethodError(self)

    _infer_selection = (lambda self = None, key = final, subset = final: selection = Noneif subset.ndim == 2:
if lib.is_scalar(key) or key in subset or lib.is_list_like(key):
selection = keyelif subset.ndim == 1 and lib.is_scalar(key) and key == subset.name:
selection = keyselection)()
    
    def aggregate(self, func, *args, **kwargs):
        raise AbstractMethodError(self)

    agg = aggregate

SelectionMixin = <NODE:27>(SelectionMixin, 'SelectionMixin', Generic[NDFrameT])

class IndexOpsMixin(OpsMixin):
    '''
    Common ops mixin to support a unified interface / docs for Series / Index
    '''
    __array_priority__ = 1000
    _hidden_attrs: 'frozenset[str]' = frozenset([
        'tolist'])
    dtype = (lambda self = None: raise AbstractMethodError(self))()
    _values = (lambda self = None: raise AbstractMethodError(self))()
    transpose = (lambda self = None: nv.validate_transpose(args, kwargs)self)()
    T = property(transpose, doc = "\n        Return the transpose, which is by definition self.\n\n        See Also\n        --------\n        Index : Immutable sequence used for indexing and alignment.\n\n        Examples\n        --------\n        For Series:\n\n        >>> s = pd.Series(['Ant', 'Bear', 'Cow'])\n        >>> s\n        0     Ant\n        1    Bear\n        2     Cow\n        dtype: str\n        >>> s.T\n        0     Ant\n        1    Bear\n        2     Cow\n        dtype: str\n\n        For Index:\n\n        >>> idx = pd.Index([1, 2, 3])\n        >>> idx.T\n        Index([1, 2, 3], dtype='int64')\n        ")
    shape = (lambda self = None: self._values.shape)()
    
    def __len__(self = None):
        raise AbstractMethodError(self)

    ndim = (lambda self = None: 1)()
    item = (lambda self: if len(self) == 1:
next(iter(self))raise None('can only convert an array of size 1 to a Python scalar'))()
    nbytes = (lambda self = None: self._values.nbytes)()
    size = (lambda self = None: len(self._values))()
    array = (lambda self = None: raise AbstractMethodError(self))()
    
    def to_numpy(self = None, dtype = None, copy = None, na_value = (None, False, lib.no_default), **kwargs):
        '''
        A NumPy ndarray representing the values in this Series or Index.

        Parameters
        ----------
        dtype : str or numpy.dtype, optional
            The dtype to pass to :meth:`numpy.asarray`.
        copy : bool, default False
            Whether to ensure that the returned value is not a view on
            another array. Note that ``copy=False`` does not *ensure* that
            ``to_numpy()`` is no-copy. Rather, ``copy=True`` ensure that
            a copy is made, even if not strictly necessary.
        na_value : Any, optional
            The value to use for missing values. The default value depends
            on `dtype` and the type of the array.
        **kwargs
            Additional keywords passed through to the ``to_numpy`` method
            of the underlying array (for extension arrays).

        Returns
        -------
        numpy.ndarray
            The NumPy ndarray holding the values from this Series or Index.
            The dtype of the array may differ. See Notes.

        See Also
        --------
        Series.array : Get the actual data stored within.
        Index.array : Get the actual data stored within.
        DataFrame.to_numpy : Similar method for DataFrame.

        Notes
        -----
        The returned array will be the same up to equality (values equal
        in `self` will be equal in the returned array; likewise for values
        that are not equal). When `self` contains an ExtensionArray, the
        dtype may be different. For example, for a category-dtype Series,
        ``to_numpy()`` will return a NumPy array and the categorical dtype
        will be lost.

        For NumPy dtypes, this will be a reference to the actual data stored
        in this Series or Index (assuming ``copy=False``). Modifying the result
        in place will modify the data stored in the Series or Index (not that
        we recommend doing that).

        For extension types, ``to_numpy()`` *may* require copying data and
        coercing the result to a NumPy type (possibly object), which may be
        expensive. When you need a no-copy reference to the underlying data,
        :attr:`Series.array` should be used instead.

        This table lays out the different dtypes and default return types of
        ``to_numpy()`` for various dtypes within pandas.

        ================== ================================
        dtype              array type
        ================== ================================
        category[T]        ndarray[T] (same dtype as input)
        period             ndarray[object] (Periods)
        interval           ndarray[object] (Intervals)
        IntegerNA          ndarray[object]
        datetime64[ns]     datetime64[ns]
        datetime64[ns, tz] ndarray[object] (Timestamps)
        ================== ================================

        Examples
        --------
        >>> ser = pd.Series(pd.Categorical(["a", "b", "a"]))
        >>> ser.to_numpy()
        array([\'a\', \'b\', \'a\'], dtype=object)

        Specify the `dtype` to control how datetime-aware data is represented.
        Use ``dtype=object`` to return an ndarray of pandas :class:`Timestamp`
        objects, each with the correct ``tz``.

        >>> ser = pd.Series(pd.date_range("2000", periods=2, tz="CET"))
        >>> ser.to_numpy(dtype=object)
        array([Timestamp(\'2000-01-01 00:00:00+0100\', tz=\'CET\'),
               Timestamp(\'2000-01-02 00:00:00+0100\', tz=\'CET\')],
              dtype=object)

        Or ``dtype=\'datetime64[ns]\'`` to return an ndarray of native
        datetime64 values. The values are converted to UTC and the timezone
        info is dropped.

        >>> ser.to_numpy(dtype="datetime64[ns]")
        ... # doctest: +ELLIPSIS
        array([\'1999-12-31T23:00:00.000000000\', \'2000-01-01T23:00:00...\'],
              dtype=\'datetime64[ns]\')
        '''
        pass
    # WARNING: Decompyle incomplete

    empty = (lambda self = None: not (self.size))()()
    
    def argmax(self = None, axis = None, skipna = None, *args, **kwargs):
        '''
        Return int position of the largest value in the Series.

        If the maximum is achieved in multiple locations,
        the first row position is returned.

        Parameters
        ----------
        axis : None
            Unused. Parameter needed for compatibility with DataFrame.
        skipna : bool, default True
            Exclude NA/null values. If the entire Series is NA, or if ``skipna=False``
            and there is an NA value, this method will raise a ``ValueError``.
        *args, **kwargs
            Additional arguments and keywords for compatibility with NumPy.

        Returns
        -------
        int
            Row position of the maximum value.

        See Also
        --------
        Series.argmax : Return position of the maximum value.
        Series.argmin : Return position of the minimum value.
        numpy.ndarray.argmax : Equivalent method for numpy arrays.
        Series.idxmax : Return index label of the maximum values.
        Series.idxmin : Return index label of the minimum values.

        Examples
        --------
        Consider dataset containing cereal calories

        >>> s = pd.Series(
        ...     [100.0, 110.0, 120.0, 110.0],
        ...     index=[
        ...         "Corn Flakes",
        ...         "Almond Delight",
        ...         "Cinnamon Toast Crunch",
        ...         "Cocoa Puff",
        ...     ],
        ... )
        >>> s
        Corn Flakes              100.0
        Almond Delight           110.0
        Cinnamon Toast Crunch    120.0
        Cocoa Puff               110.0
        dtype: float64

        >>> s.argmax()
        np.int64(2)
        >>> s.argmin()
        np.int64(0)

        The maximum cereal calories is the third element and
        the minimum cereal calories is the first element,
        since series is zero-indexed.
        '''
        delegate = self._values
        nv.validate_minmax_axis(axis)
        skipna = nv.validate_argmax_with_skipna(skipna, args, kwargs)
        if isinstance(delegate, ExtensionArray):
            return delegate.argmax(skipna = skipna)
        result = None.nanargmax(delegate, skipna = skipna)
        return result

    
    def argmin(self = None, axis = None, skipna = None, *args, **kwargs):
        '''
        Return int position of the smallest value in the Series.

        If the minimum is achieved in multiple locations,
        the first row position is returned.

        Parameters
        ----------
        axis : None
            Unused. Parameter needed for compatibility with DataFrame.
        skipna : bool, default True
            Exclude NA/null values. If the entire Series is NA, or if ``skipna=False``
            and there is an NA value, this method will raise a ``ValueError``.
        *args, **kwargs
            Additional arguments and keywords for compatibility with NumPy.

        Returns
        -------
        int
            Row position of the minimum value.

        See Also
        --------
        Series.argmin : Return position of the minimum value.
        Series.argmax : Return position of the maximum value.
        numpy.ndarray.argmin : Equivalent method for numpy arrays.
        Series.idxmin : Return index label of the minimum values.
        Series.idxmax : Return index label of the maximum values.

        Examples
        --------
        Consider dataset containing cereal calories

        >>> s = pd.Series(
        ...     [100.0, 110.0, 120.0, 110.0],
        ...     index=[
        ...         "Corn Flakes",
        ...         "Almond Delight",
        ...         "Cinnamon Toast Crunch",
        ...         "Cocoa Puff",
        ...     ],
        ... )
        >>> s
        Corn Flakes              100.0
        Almond Delight           110.0
        Cinnamon Toast Crunch    120.0
        Cocoa Puff               110.0
        dtype: float64

        >>> s.argmax()
        np.int64(2)
        >>> s.argmin()
        np.int64(0)

        The maximum cereal calories is the third element and
        the minimum cereal calories is the first element,
        since series is zero-indexed.
        '''
        delegate = self._values
        nv.validate_minmax_axis(axis)
        skipna = nv.validate_argmax_with_skipna(skipna, args, kwargs)
        if isinstance(delegate, ExtensionArray):
            return delegate.argmin(skipna = skipna)
        result = None.nanargmin(delegate, skipna = skipna)
        return result

    
    def tolist(self = None):
        """
        Return a list of the values.

        These are each a scalar type, which is a Python scalar
        (for str, int, float) or a pandas scalar
        (for Timestamp/Timedelta/Interval/Period)

        Returns
        -------
        list
            List containing the values as Python or pandas scalers.

        See Also
        --------
        numpy.ndarray.tolist : Return the array as an a.ndim-levels deep
            nested list of Python scalars.

        Examples
        --------
        For Series

        >>> s = pd.Series([1, 2, 3])
        >>> s.to_list()
        [1, 2, 3]

        For Index:

        >>> idx = pd.Index([1, 2, 3])
        >>> idx
        Index([1, 2, 3], dtype='int64')

        >>> idx.to_list()
        [1, 2, 3]
        """
        return self._values.tolist()

    to_list = tolist
    
    def __iter__(self = None):
        '''
        Return an iterator of the values.

        These are each a scalar type, which is a Python scalar
        (for str, int, float) or a pandas scalar
        (for Timestamp/Timedelta/Interval/Period)

        Returns
        -------
        iterator
            An iterator yielding scalar values from the Series.

        See Also
        --------
        Series.items : Lazily iterate over (index, value) tuples.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3])
        >>> for x in s:
        ...     print(x)
        1
        2
        3
        '''
        if not isinstance(self._values, np.ndarray):
            return iter(self._values)
        return None(self._values.item, range(self._values.size))

    hasnans = (lambda self = None: bool(isna(self).any()))()
    _map_values = (lambda self, mapper, na_action = (None,): arr = self._valuesif isinstance(arr, ExtensionArray):
arr.map(mapper, na_action = na_action)None.map_array(arr, mapper, na_action = na_action))()
    
    def value_counts(self, normalize = None, sort = None, ascending = final, bins = (False, True, False, None, True), dropna = ('normalize', 'bool', 'sort', 'bool', 'ascending', 'bool', 'dropna', 'bool', 'return', 'Series')):
        '''
        Return a Series containing counts of unique values.

        The resulting object will be in descending order so that the
        first element is the most frequently-occurring element.
        Excludes NA values by default.

        Parameters
        ----------
        normalize : bool, default False
            If True then the object returned will contain the relative
            frequencies of the unique values.
        sort : bool, default True
            Stable sort by frequencies when True. Preserve the order of the data
            when False.

            .. versionchanged:: 3.0.0

                Prior to 3.0.0, the sort was unstable.
        ascending : bool, default False
            Sort in ascending order.
        bins : int, optional
            Rather than count values, group them into half-open bins,
            a convenience for ``pd.cut``, only works with numeric data.
        dropna : bool, default True
            Don\'t include counts of NaN.

        Returns
        -------
        Series
            Series containing counts of unique values.

        See Also
        --------
        Series.count: Number of non-NA elements in a Series.
        DataFrame.count: Number of non-NA elements in a DataFrame.
        DataFrame.value_counts: Equivalent method on DataFrames.

        Examples
        --------
        >>> index = pd.Index([3, 1, 2, 3, 4, np.nan])
        >>> index.value_counts()
        3.0    2
        1.0    1
        2.0    1
        4.0    1
        Name: count, dtype: int64

        With `normalize` set to `True`, returns the relative frequency by
        dividing all values by the sum of values.

        >>> s = pd.Series([3, 1, 2, 3, 4, np.nan])
        >>> s.value_counts(normalize=True)
        3.0    0.4
        1.0    0.2
        2.0    0.2
        4.0    0.2
        Name: proportion, dtype: float64

        **bins**

        Bins can be useful for going from a continuous variable to a
        categorical variable; instead of counting unique
        apparitions of values, divide the index in the specified
        number of half-open bins.

        >>> s.value_counts(bins=3)
        (0.996, 2.0]    2
        (2.0, 3.0]      2
        (3.0, 4.0]      1
        Name: count, dtype: int64

        **dropna**

        With `dropna` set to `False` we can also see NaN index values.

        >>> s.value_counts(dropna=False)
        3.0    2
        1.0    1
        2.0    1
        4.0    1
        NaN    1
        Name: count, dtype: int64

        **Categorical Dtypes**

        Rows with categorical type will be counted as one group
        if they have same categories and order.
        In the example below, even though ``a``, ``c``, and ``d``
        all have the same data types of ``category``,
        only ``c`` and ``d`` will be counted as one group
        since ``a`` doesn\'t have the same categories.

        >>> df = pd.DataFrame({"a": [1], "b": ["2"], "c": [3], "d": [3]})
        >>> df = df.astype({"a": "category", "c": "category", "d": "category"})
        >>> df
           a  b  c  d
        0  1  2  3  3

        >>> df.dtypes
        a    category
        b      str
        c    category
        d    category
        dtype: object

        >>> df.dtypes.value_counts()
        category    2
        category    1
        str         1
        Name: count, dtype: int64
        '''
        return algorithms.value_counts_internal(self, sort = sort, ascending = ascending, normalize = normalize, bins = bins, dropna = dropna)

    
    def unique(self):
        values = self._values
        if not isinstance(values, np.ndarray):
            result = values.unique()
        else:
            result = algorithms.unique1d(values)
        return result

    nunique = (lambda self = None, dropna = None: uniqs = self.unique()if dropna:
uniqs = remove_na_arraylike(uniqs)len(uniqs))()
    is_unique = (lambda self = None: self.nunique(dropna = False) == len(self))()
    is_monotonic_increasing = (lambda self = None: Index = Indeximport pandasIndex(self).is_monotonic_increasing)()
    is_monotonic_decreasing = (lambda self = None: Index = Indeximport pandasIndex(self).is_monotonic_decreasing)()
    _memory_usage = (lambda self = None, deep = None: if hasattr(self.array, 'memory_usage'):
self.array.memory_usage(deep = deep)v = None.array.nbytesif not deep and is_object_dtype(self.dtype) and PYPY:
values = cast(np.ndarray, self._values)v += lib.memory_usage_of_objects(values)v)()
    
    def factorize(self = None, sort = None, use_na_sentinel = None):
        '''
        Encode the object as an enumerated type or categorical variable.

        This method is useful for obtaining a numeric representation of an
        array when all that matters is identifying distinct values. `factorize`
        is available as both a top-level function :func:`pandas.factorize`,
        and as a method :meth:`Series.factorize` and :meth:`Index.factorize`.

        Parameters
        ----------
        sort : bool, default False
            Sort `uniques` and shuffle `codes` to maintain the
            relationship.
        use_na_sentinel : bool, default True
            If True, the sentinel -1 will be used for NaN values. If False,
            NaN values will be encoded as non-negative integers and will not drop the
            NaN from the uniques of the values.

        Returns
        -------
        codes : ndarray
            An integer ndarray that\'s an indexer into `uniques`.
            ``uniques.take(codes)`` will have the same values as `values`.
        uniques : ndarray, Index, or Categorical
            The unique valid values. When `values` is Categorical, `uniques`
            is a Categorical. When `values` is some other pandas object, an
            `Index` is returned. Otherwise, a 1-D ndarray is returned.

            .. note::

                Even if there\'s a missing value in `values`, `uniques` will
                *not* contain an entry for it.

        See Also
        --------
        cut : Discretize continuous-valued array.
        unique : Find the unique value in an array.

        Notes
        -----
        Reference :ref:`the user guide <reshaping.factorize>` for more examples.

        Examples
        --------
        These examples all show factorize as a top-level method like
        ``pd.factorize(values)``. The results are identical for methods like
        :meth:`Series.factorize`.

        >>> codes, uniques = pd.factorize(
        ...     np.array(["b", "b", "a", "c", "b"], dtype="O")
        ... )
        >>> codes
        array([0, 0, 1, 2, 0])
        >>> uniques
        array([\'b\', \'a\', \'c\'], dtype=object)

        With ``sort=True``, the `uniques` will be sorted, and `codes` will be
        shuffled so that the relationship is the maintained.

        >>> codes, uniques = pd.factorize(
        ...     np.array(["b", "b", "a", "c", "b"], dtype="O"), sort=True
        ... )
        >>> codes
        array([1, 1, 0, 2, 1])
        >>> uniques
        array([\'a\', \'b\', \'c\'], dtype=object)

        When ``use_na_sentinel=True`` (the default), missing values are indicated in
        the `codes` with the sentinel value ``-1`` and missing values are not
        included in `uniques`.

        >>> codes, uniques = pd.factorize(
        ...     np.array(["b", None, "a", "c", "b"], dtype="O")
        ... )
        >>> codes
        array([ 0, -1,  1,  2,  0])
        >>> uniques
        array([\'b\', \'a\', \'c\'], dtype=object)

        Thus far, we\'ve only factorized lists (which are internally coerced to
        NumPy arrays). When factorizing pandas objects, the type of `uniques`
        will differ. For Categoricals, a `Categorical` is returned.

        >>> cat = pd.Categorical(["a", "a", "c"], categories=["a", "b", "c"])
        >>> codes, uniques = pd.factorize(cat)
        >>> codes
        array([0, 0, 1])
        >>> uniques
        [\'a\', \'c\']
        Categories (3, str): [\'a\', \'b\', \'c\']

        Notice that ``\'b\'`` is in ``uniques.categories``, despite not being
        present in ``cat.values``.

        For all other pandas objects, an Index of the appropriate type is
        returned.

        >>> cat = pd.Series(["a", "a", "c"])
        >>> codes, uniques = pd.factorize(cat)
        >>> codes
        array([0, 0, 1])
        >>> uniques
        Index([\'a\', \'c\'], dtype=\'str\')

        If NaN is in the values, and we want to include NaN in the uniques of the
        values, it can be achieved by setting ``use_na_sentinel=False``.

        >>> values = np.array([1, 2, 1, np.nan])
        >>> codes, uniques = pd.factorize(values)  # default: use_na_sentinel=True
        >>> codes
        array([ 0,  1,  0, -1])
        >>> uniques
        array([1., 2.])

        >>> codes, uniques = pd.factorize(values, use_na_sentinel=False)
        >>> codes
        array([0, 1, 0, 2])
        >>> uniques
        array([ 1.,  2., nan])
        '''
        (codes, uniques) = algorithms.factorize(self._values, sort = sort, use_na_sentinel = use_na_sentinel)
        if uniques.dtype == np.float16:
            uniques = uniques.astype(np.float32)
        if isinstance(self, ABCMultiIndex):
            if len(self) == 0:
                uniques = self[:0]
            else:
                uniques = self._constructor(uniques)
        else:
            Index = Index
            import pandas
            
            try:
                uniques = Index(uniques, dtype = self.dtype, copy = False)
            except NotImplementedError:
                uniques = Index(uniques, copy = False)

            return (codes, uniques)

    searchsorted = (lambda self = None, value = None, side = overload, sorter = (..., ...): pass)()
    searchsorted = (lambda self = None, value = None, side = overload, sorter = (..., ...): pass)()
    
    def searchsorted(self = None, value = None, side = None, sorter = ('left', None)):
        '''
        Find indices where elements should be inserted to maintain order.

        Find the indices into a sorted Index `self` such that, if the
        corresponding elements in `value` were inserted before the indices,
        the order of `self` would be preserved.

        .. note::

            The Index *must* be monotonically sorted, otherwise
            wrong locations will likely be returned. Pandas does *not*
            check this for you.

        Parameters
        ----------
        value : array-like or scalar
            Values to insert into `self`.
        side : {{\'left\', \'right\'}}, optional
            If \'left\', the index of the first suitable location found is given.
            If \'right\', return the last such index.  If there is no suitable
            index, return either 0 or N (where N is the length of `self`).
        sorter : 1-D array-like, optional
            Optional array of integer indices that sort `self` into ascending
            order. They are typically the result of ``np.argsort``.

        Returns
        -------
        int or array of int
            A scalar or array of insertion points with the
            same shape as `value`.

        See Also
        --------
        sort_values : Sort by the values along either axis.
        numpy.searchsorted : Similar method from NumPy.

        Notes
        -----
        Binary search is used to find the required insertion points.

        Examples
        --------
        >>> ser = pd.Series([1, 2, 3])
        >>> ser
        0    1
        1    2
        2    3
        dtype: int64

        >>> ser.searchsorted(4)
        np.int64(3)

        >>> ser.searchsorted([0, 4])
        array([0, 3])

        >>> ser.searchsorted([1, 3], side="left")
        array([0, 2])

        >>> ser.searchsorted([1, 3], side="right")
        array([1, 3])

        >>> ser = pd.Series(pd.to_datetime(["3/11/2000", "3/12/2000", "3/13/2000"]))
        >>> ser
        0   2000-03-11
        1   2000-03-12
        2   2000-03-13
        dtype: datetime64[us]

        >>> ser.searchsorted("3/14/2000")
        np.int64(3)

        >>> ser = pd.Categorical(
        ...     ["apple", "bread", "bread", "cheese", "milk"], ordered=True
        ... )
        >>> ser
        [\'apple\', \'bread\', \'bread\', \'cheese\', \'milk\']
        Categories (4, str): [\'apple\' < \'bread\' < \'cheese\' < \'milk\']

        >>> ser.searchsorted("bread")
        np.int64(1)

        >>> ser.searchsorted(["bread"], side="right")
        array([3])

        If the values are not monotonically sorted, wrong locations
        may be returned:

        >>> ser = pd.Series([2, 1, 3])
        >>> ser
        0    2
        1    1
        2    3
        dtype: int64

        >>> ser.searchsorted(1)  # doctest: +SKIP
        0  # wrong result, correct would be 1
        '''
        if isinstance(value, ABCDataFrame):
            msg = f'''Value must be 1-D array-like or scalar, {type(value).__name__} is not supported'''
            raise ValueError(msg)
        values = self._values
        if not isinstance(values, np.ndarray):
            return values.searchsorted(value, side = side, sorter = sorter)
        return None.searchsorted(values, value, side = side, sorter = sorter)

    
    def drop_duplicates(self = None, *, keep):
        duplicated = self._duplicated(keep = keep)
        return self[~duplicated]

    _duplicated = (lambda self = None, keep = None: arr = self._valuesif isinstance(arr, ExtensionArray):
arr.duplicated(keep = keep)None.duplicated(arr, keep = keep))()
    
    def _arith_method(self, other, op):
        res_name = ops.get_op_result_name(self, other)
        lvalues = self._values
        rvalues = extract_array(other, extract_numpy = True, extract_range = True)
        rvalues = ops.maybe_prepare_scalar_for_op(rvalues, lvalues.shape)
        rvalues = ensure_wrapped_if_datetimelike(rvalues)
        if isinstance(rvalues, range):
            rvalues = np.arange(rvalues.start, rvalues.stop, rvalues.step)
        np.errstate(all = 'ignore')
        result = ops.arithmetic_op(lvalues, rvalues, op)
        None(None, None)

    
    def _construct_result(self, result, name, other):
        '''
        Construct an appropriately-wrapped result from the ArrayLike result
        of an arithmetic-like operation.
        '''
        raise AbstractMethodError(self)
