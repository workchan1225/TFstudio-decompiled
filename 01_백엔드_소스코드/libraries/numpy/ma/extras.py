# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extras.pyc (Python 3.11)

__doc__ = '\nMasked arrays add-ons.\n\nA collection of utilities for `numpy.ma`.\n\n:author: Pierre Gerard-Marchant\n:contact: pierregm_at_uga_dot_edu\n:version: $Id: extras.py 3473 2007-10-29 15:18:13Z jarrod.millman $\n\n'
__all__ = [
    'apply_along_axis',
    'apply_over_axes',
    'atleast_1d',
    'atleast_2d',
    'atleast_3d',
    'average',
    'clump_masked',
    'clump_unmasked',
    'column_stack',
    'compress_cols',
    'compress_nd',
    'compress_rowcols',
    'compress_rows',
    'count_masked',
    'corrcoef',
    'cov',
    'diagflat',
    'dot',
    'dstack',
    'ediff1d',
    'flatnotmasked_contiguous',
    'flatnotmasked_edges',
    'hsplit',
    'hstack',
    'isin',
    'in1d',
    'intersect1d',
    'mask_cols',
    'mask_rowcols',
    'mask_rows',
    'masked_all',
    'masked_all_like',
    'median',
    'mr_',
    'ndenumerate',
    'notmasked_contiguous',
    'notmasked_edges',
    'polyfit',
    'row_stack',
    'setdiff1d',
    'setxor1d',
    'stack',
    'unique',
    'union1d',
    'vander',
    'vstack']
import itertools
import warnings
from  import core as ma
from core import MaskedArray, MAError, add, array, asarray, concatenate, filled, count, getmask, getmaskarray, make_mask_descr, masked, masked_array, mask_or, nomask, ones, sort, zeros, getdata, get_masked_subclass, dot
import numpy as np
from numpy import ndarray, array as nxarray
from numpy.core.multiarray import normalize_axis_index
from numpy.core.numeric import normalize_axis_tuple
from numpy.lib.function_base import _ureduce
from numpy.lib.index_tricks import AxisConcatenator

def issequence(seq):
    '''
    Is seq a sequence (ndarray, list or tuple)?

    '''
    return isinstance(seq, (ndarray, tuple, list))


def count_masked(arr, axis = (None,)):
    '''
    Count the number of masked elements along the given axis.

    Parameters
    ----------
    arr : array_like
        An array with (possibly) masked elements.
    axis : int, optional
        Axis along which to count. If None (default), a flattened
        version of the array is used.

    Returns
    -------
    count : int, ndarray
        The total number of masked elements (axis=None) or the number
        of masked elements along each slice of the given axis.

    See Also
    --------
    MaskedArray.count : Count non-masked elements.

    Examples
    --------
    >>> import numpy.ma as ma
    >>> a = np.arange(9).reshape((3,3))
    >>> a = ma.array(a)
    >>> a[1, 0] = ma.masked
    >>> a[1, 2] = ma.masked
    >>> a[2, 1] = ma.masked
    >>> a
    masked_array(
      data=[[0, 1, 2],
            [--, 4, --],
            [6, --, 8]],
      mask=[[False, False, False],
            [ True, False,  True],
            [False,  True, False]],
      fill_value=999999)
    >>> ma.count_masked(a)
    3

    When the `axis` keyword is used an array is returned.

    >>> ma.count_masked(a, axis=0)
    array([1, 1, 1])
    >>> ma.count_masked(a, axis=1)
    array([0, 2, 1])

    '''
    m = getmaskarray(arr)
    return m.sum(axis)


def masked_all(shape, dtype = (float,)):
    """
    Empty masked array with all elements masked.

    Return an empty masked array of the given shape and dtype, where all the
    data are masked.

    Parameters
    ----------
    shape : int or tuple of ints
        Shape of the required MaskedArray, e.g., ``(2, 3)`` or ``2``.
    dtype : dtype, optional
        Data type of the output.

    Returns
    -------
    a : MaskedArray
        A masked array with all data masked.

    See Also
    --------
    masked_all_like : Empty masked array modelled on an existing array.

    Examples
    --------
    >>> import numpy.ma as ma
    >>> ma.masked_all((3, 3))
    masked_array(
      data=[[--, --, --],
            [--, --, --],
            [--, --, --]],
      mask=[[ True,  True,  True],
            [ True,  True,  True],
            [ True,  True,  True]],
      fill_value=1e+20,
      dtype=float64)

    The `dtype` parameter defines the underlying data type.

    >>> a = ma.masked_all((3, 3))
    >>> a.dtype
    dtype('float64')
    >>> a = ma.masked_all((3, 3), dtype=np.int32)
    >>> a.dtype
    dtype('int32')

    """
    a = masked_array(np.empty(shape, dtype), mask = np.ones(shape, make_mask_descr(dtype)))
    return a


def masked_all_like(arr):
    """
    Empty masked array with the properties of an existing array.

    Return an empty masked array of the same shape and dtype as
    the array `arr`, where all the data are masked.

    Parameters
    ----------
    arr : ndarray
        An array describing the shape and dtype of the required MaskedArray.

    Returns
    -------
    a : MaskedArray
        A masked array with all data masked.

    Raises
    ------
    AttributeError
        If `arr` doesn't have a shape attribute (i.e. not an ndarray)

    See Also
    --------
    masked_all : Empty masked array with all elements masked.

    Examples
    --------
    >>> import numpy.ma as ma
    >>> arr = np.zeros((2, 3), dtype=np.float32)
    >>> arr
    array([[0., 0., 0.],
           [0., 0., 0.]], dtype=float32)
    >>> ma.masked_all_like(arr)
    masked_array(
      data=[[--, --, --],
            [--, --, --]],
      mask=[[ True,  True,  True],
            [ True,  True,  True]],
      fill_value=1e+20,
      dtype=float32)

    The dtype of the masked array matches the dtype of `arr`.

    >>> arr.dtype
    dtype('float32')
    >>> ma.masked_all_like(arr).dtype
    dtype('float32')

    """
    a = np.empty_like(arr).view(MaskedArray)
    a._mask = np.ones(a.shape, dtype = make_mask_descr(a.dtype))
    return a


class _fromnxfunction:
    '''
    Defines a wrapper to adapt NumPy functions to masked arrays.


    An instance of `_fromnxfunction` can be called with the same parameters
    as the wrapped NumPy function. The docstring of `newfunc` is adapted from
    the wrapped function as well, see `getdoc`.

    This class should not be used directly. Instead, one of its extensions that
    provides support for a specific type of input should be used.

    Parameters
    ----------
    funcname : str
        The name of the function to be adapted. The function should be
        in the NumPy namespace (i.e. ``np.funcname``).

    '''
    
    def __init__(self, funcname):
        self.__name__ = funcname
        self.__doc__ = self.getdoc()

    
    def getdoc(self):
        '''
        Retrieve the docstring and signature from the function.

        The ``__doc__`` attribute of the function is used as the docstring for
        the new masked array version of the function. A note on application
        of the function to the mask is appended.

        Parameters
        ----------
        None

        '''
        npfunc = getattr(np, self.__name__, None)
        doc = getattr(npfunc, '__doc__', None)
        if doc:
            sig = self.__name__ + ma.get_object_signature(npfunc)
            doc = ma.doc_note(doc, 'The function is applied to both the _data and the _mask, if any.')
            return '\n\n'.join((sig, doc))

    
    def __call__(self, *args, **params):
        pass



class _fromnxfunction_single(_fromnxfunction):
    '''
    A version of `_fromnxfunction` that is called with a single array
    argument followed by auxiliary args that are passed verbatim for
    both the data and mask calls.
    '''
    
    def __call__(self, x, *args, **params):
        func = getattr(np, self.__name__)
    # WARNING: Decompyle incomplete



class _fromnxfunction_seq(_fromnxfunction):
    '''
    A version of `_fromnxfunction` that is called with a single sequence
    of arrays followed by auxiliary args that are passed verbatim for
    both the data and mask calls.
    '''
    
    def __call__(self, x, *args, **params):
        func = getattr(np, self.__name__)
    # WARNING: Decompyle incomplete



class _fromnxfunction_args(_fromnxfunction):
    '''
    A version of `_fromnxfunction` that is called with multiple array
    arguments. The first non-array-like input marks the beginning of the
    arguments that are passed verbatim for both the data and mask calls.
    Array arguments are processed independently and the results are
    returned in a list. If only one array is found, the return value is
    just the processed array instead of a list.
    '''
    
    def __call__(self, *args, **params):
        func = getattr(np, self.__name__)
        arrays = []
        args = list(args)
    # WARNING: Decompyle incomplete



class _fromnxfunction_allargs(_fromnxfunction):
    '''
    A version of `_fromnxfunction` that is called with multiple array
    arguments. Similar to `_fromnxfunction_args` except that all args
    are converted to arrays even if they are not so already. This makes
    it possible to process scalars as 1-D arrays. Only keyword arguments
    are passed through verbatim for the data and mask calls. Arrays
    arguments are processed independently and the results are returned
    in a list. If only one arg is present, the return value is just the
    processed array instead of a list.
    '''
    
    def __call__(self, *args, **params):
        func = getattr(np, self.__name__)
        res = []
    # WARNING: Decompyle incomplete


atleast_1d = _fromnxfunction_allargs('atleast_1d')
atleast_2d = _fromnxfunction_allargs('atleast_2d')
atleast_3d = _fromnxfunction_allargs('atleast_3d')
vstack = _fromnxfunction_seq('vstack')
row_stack = _fromnxfunction_seq('vstack')
hstack = _fromnxfunction_seq('hstack')
column_stack = _fromnxfunction_seq('column_stack')
dstack = _fromnxfunction_seq('dstack')
stack = _fromnxfunction_seq('stack')
hsplit = _fromnxfunction_single('hsplit')
diagflat = _fromnxfunction_single('diagflat')

def flatten_inplace(seq):
    '''Flatten a sequence in place.'''
    k = 0
# WARNING: Decompyle incomplete


def apply_along_axis(func1d, axis, arr, *args, **kwargs):
    '''
    (This docstring should be overwritten)
    '''
    arr = array(arr, copy = False, subok = True)
    nd = arr.ndim
    axis = normalize_axis_index(axis, nd)
    ind = [
        0] * (nd - 1)
    i = np.zeros(nd, 'O')
    indlist = list(range(nd))
    indlist.remove(axis)
    i[axis] = slice(None, None)
    outshape = np.asarray(arr.shape).take(indlist)
    i.put(indlist, ind)
# WARNING: Decompyle incomplete

apply_along_axis.__doc__ = np.apply_along_axis.__doc__

def apply_over_axes(func, a, axes):
    '''
    (This docstring will be overwritten)
    '''
    val = asarray(a)
    N = a.ndim
    if array(axes).ndim == 0:
        axes = (axes,)
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
