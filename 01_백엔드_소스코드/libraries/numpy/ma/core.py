# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

'''
numpy.ma : a package to handle missing or invalid values.

This package was initially written for numarray by Paul F. Dubois
at Lawrence Livermore National Laboratory.
In 2006, the package was completely rewritten by Pierre Gerard-Marchant
(University of Georgia) to make the MaskedArray class a subclass of ndarray,
and to improve support of structured arrays.


Copyright 1999, 2000, 2001 Regents of the University of California.
Released for unlimited redistribution.

* Adapted for numpy_core 2005 by Travis Oliphant and (mainly) Paul Dubois.
* Subclassing of the base `ndarray` 2006 by Pierre Gerard-Marchant
  (pgmdevlist_AT_gmail_DOT_com)
* Improvements suggested by Reggie Dugard (reggie_AT_merfinllc_DOT_com)

.. moduleauthor:: Pierre Gerard-Marchant

'''
import builtins
import inspect
import operator
import warnings
import textwrap
import re
from functools import reduce
import numpy as np

umath

numerictypes
from numpy.core import multiarray
import numpy.core.numerictypes, core
from numpy import ndarray, amax, amin, iscomplexobj, bool_, _NoValue
from numpy import array as narray
from numpy.lib.function_base import angle
from numpy.compat import getargspec, formatargspec, long, unicode, bytes
from numpy import expand_dims
from numpy.core.numeric import normalize_axis_tuple
__all__ = [
    'MAError',
    'MaskError',
    'MaskType',
    'MaskedArray',
    'abs',
    'absolute',
    'add',
    'all',
    'allclose',
    'allequal',
    'alltrue',
    'amax',
    'amin',
    'angle',
    'anom',
    'anomalies',
    'any',
    'append',
    'arange',
    'arccos',
    'arccosh',
    'arcsin',
    'arcsinh',
    'arctan',
    'arctan2',
    'arctanh',
    'argmax',
    'argmin',
    'argsort',
    'around',
    'array',
    'asanyarray',
    'asarray',
    'bitwise_and',
    'bitwise_or',
    'bitwise_xor',
    'bool_',
    'ceil',
    'choose',
    'clip',
    'common_fill_value',
    'compress',
    'compressed',
    'concatenate',
    'conjugate',
    'convolve',
    'copy',
    'correlate',
    'cos',
    'cosh',
    'count',
    'cumprod',
    'cumsum',
    'default_fill_value',
    'diag',
    'diagonal',
    'diff',
    'divide',
    'empty',
    'empty_like',
    'equal',
    'exp',
    'expand_dims',
    'fabs',
    'filled',
    'fix_invalid',
    'flatten_mask',
    'flatten_structured_array',
    'floor',
    'floor_divide',
    'fmod',
    'frombuffer',
    'fromflex',
    'fromfunction',
    'getdata',
    'getmask',
    'getmaskarray',
    'greater',
    'greater_equal',
    'harden_mask',
    'hypot',
    'identity',
    'ids',
    'indices',
    'inner',
    'innerproduct',
    'isMA',
    'isMaskedArray',
    'is_mask',
    'is_masked',
    'isarray',
    'left_shift',
    'less',
    'less_equal',
    'log',
    'log10',
    'log2',
    'logical_and',
    'logical_not',
    'logical_or',
    'logical_xor',
    'make_mask',
    'make_mask_descr',
    'make_mask_none',
    'mask_or',
    'masked',
    'masked_array',
    'masked_equal',
    'masked_greater',
    'masked_greater_equal',
    'masked_inside',
    'masked_invalid',
    'masked_less',
    'masked_less_equal',
    'masked_not_equal',
    'masked_object',
    'masked_outside',
    'masked_print_option',
    'masked_singleton',
    'masked_values',
    'masked_where',
    'max',
    'maximum',
    'maximum_fill_value',
    'mean',
    'min',
    'minimum',
    'minimum_fill_value',
    'mod',
    'multiply',
    'mvoid',
    'ndim',
    'negative',
    'nomask',
    'nonzero',
    'not_equal',
    'ones',
    'ones_like',
    'outer',
    'outerproduct',
    'power',
    'prod',
    'product',
    'ptp',
    'put',
    'putmask',
    'ravel',
    'remainder',
    'repeat',
    'reshape',
    'resize',
    'right_shift',
    'round',
    'round_',
    'set_fill_value',
    'shape',
    'sin',
    'sinh',
    'size',
    'soften_mask',
    'sometrue',
    'sort',
    'sqrt',
    'squeeze',
    'std',
    'subtract',
    'sum',
    'swapaxes',
    'take',
    'tan',
    'tanh',
    'trace',
    'transpose',
    'true_divide',
    'var',
    'where',
    'zeros',
    'zeros_like']
MaskType = np.bool_
nomask = MaskType(0)

class MaskedArrayFutureWarning(FutureWarning):
    pass


def _deprecate_argsort_axis(arr):
    '''
    Adjust the axis passed to argsort, warning if necessary

    Parameters
    ----------
    arr
        The array which argsort was called on

    np.ma.argsort has a long-term bug where the default of the axis argument
    is wrong (gh-8701), which now must be kept for backwards compatibility.
    Thankfully, this only makes a difference when arrays are 2- or more-
    dimensional, so we only need a warning then.
    '''
    if arr.ndim <= 1:
        return -1
    None.warn('In the future the default for argsort will be axis=-1, not the current None, to match its documentation and np.argsort. Explicitly pass -1 or None to silence this warning.', MaskedArrayFutureWarning, stacklevel = 3)


def doc_note(initialdoc, note):
    '''
    Adds a Notes section to an existing docstring.

    '''
    pass
# WARNING: Decompyle incomplete


def get_object_signature(obj):
    '''
    Get the signature from obj

    '''
    pass
# WARNING: Decompyle incomplete


class MAError(Exception):
    '''
    Class for masked array related errors.

    '''
    pass


class MaskError(MAError):
    '''
    Class for mask related errors.

    '''
    pass

default_filler = {
    'b': True,
    'c': (1e+20+0j),
    'f': 1e+20,
    'i': 999999,
    'O': '?',
    'S': b'N/A',
    'u': 999999,
    'V': b'???',
    'U': 'N/A' }
for v in ('Y', 'M', 'W', 'D', 'h', 'm', 's', 'ms', 'us', 'ns', 'ps', 'fs', 'as'):
    default_filler['M8[' + v + ']'] = np.datetime64('NaT', v)
    default_filler['m8[' + v + ']'] = np.timedelta64('NaT', v)
    float_types_list = [
        np.half,
        np.single,
        np.double,
        np.longdouble,
        np.csingle,
        np.cdouble,
        np.clongdouble]
    max_filler = ntypes._minvals
    (lambda .0: [ (k, -(np.inf)) for k in .0 ])(float_types_list[:4]())
    (lambda .0: [ (k, complex(-(np.inf), -(np.inf))) for k in .0 ])(float_types_list[-3:]())
    min_filler = ntypes._maxvals
    (lambda .0: [ (k, +(np.inf)) for k in .0 ])(float_types_list[:4]())
    (lambda .0: [ (k, complex(+(np.inf), +(np.inf))) for k in .0 ])(float_types_list[-3:]())
    del float_types_list
    
    def _recursive_fill_value(dtype, f):
        '''
    Recursively produce a fill value for `dtype`, calling f on scalar dtypes
    '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_dtype_of(obj):
        ''' Convert the argument for *_fill_value into a dtype '''
        if isinstance(obj, np.dtype):
            return obj
        if None(obj, 'dtype'):
            return obj.dtype
        return None.asanyarray(obj).dtype

    
    def default_fill_value(obj):
        """
    Return the default fill value for the argument object.

    The default filling value depends on the datatype of the input
    array or the type of the input scalar:

       ========  ========
       datatype  default
       ========  ========
       bool      True
       int       999999
       float     1.e20
       complex   1.e20+0j
       object    '?'
       string    'N/A'
       ========  ========

    For structured types, a structured scalar is returned, with each field the
    default fill value for its type.

    For subarray types, the fill value is an array of the same size containing
    the default scalar fill value.

    Parameters
    ----------
    obj : ndarray, dtype or scalar
        The array data-type or scalar for which the default fill value
        is returned.

    Returns
    -------
    fill_value : scalar
        The default fill value.

    Examples
    --------
    >>> np.ma.default_fill_value(1)
    999999
    >>> np.ma.default_fill_value(np.array([1.1, 2., np.pi]))
    1e+20
    >>> np.ma.default_fill_value(np.dtype(complex))
    (1e+20+0j)

    """
        
        def _scalar_fill_value(dtype):
            if dtype.kind in 'Mm':
                return default_filler.get(dtype.str[1:], '?')
            return None.get(dtype.kind, '?')

        dtype = _get_dtype_of(obj)
        return _recursive_fill_value(dtype, _scalar_fill_value)

    
    def _extremum_fill_value(obj, extremum, extremum_name):
        pass
    # WARNING: Decompyle incomplete

    
    def minimum_fill_value(obj):
        """
    Return the maximum value that can be represented by the dtype of an object.

    This function is useful for calculating a fill value suitable for
    taking the minimum of an array with a given dtype.

    Parameters
    ----------
    obj : ndarray, dtype or scalar
        An object that can be queried for it's numeric type.

    Returns
    -------
    val : scalar
        The maximum representable value.

    Raises
    ------
    TypeError
        If `obj` isn't a suitable numeric type.

    See Also
    --------
    maximum_fill_value : The inverse function.
    set_fill_value : Set the filling value of a masked array.
    MaskedArray.fill_value : Return current fill value.

    Examples
    --------
    >>> import numpy.ma as ma
    >>> a = np.int8()
    >>> ma.minimum_fill_value(a)
    127
    >>> a = np.int32()
    >>> ma.minimum_fill_value(a)
    2147483647

    An array of numeric data can also be passed.

    >>> a = np.array([1, 2, 3], dtype=np.int8)
    >>> ma.minimum_fill_value(a)
    127
    >>> a = np.array([1, 2, 3], dtype=np.float32)
    >>> ma.minimum_fill_value(a)
    inf

    """
        return _extremum_fill_value(obj, min_filler, 'minimum')

    
    def maximum_fill_value(obj):
        """
    Return the minimum value that can be represented by the dtype of an object.

    This function is useful for calculating a fill value suitable for
    taking the maximum of an array with a given dtype.

    Parameters
    ----------
    obj : ndarray, dtype or scalar
        An object that can be queried for it's numeric type.

    Returns
    -------
    val : scalar
        The minimum representable value.

    Raises
    ------
    TypeError
        If `obj` isn't a suitable numeric type.

    See Also
    --------
    minimum_fill_value : The inverse function.
    set_fill_value : Set the filling value of a masked array.
    MaskedArray.fill_value : Return current fill value.

    Examples
    --------
    >>> import numpy.ma as ma
    >>> a = np.int8()
    >>> ma.maximum_fill_value(a)
    -128
    >>> a = np.int32()
    >>> ma.maximum_fill_value(a)
    -2147483648

    An array of numeric data can also be passed.

    >>> a = np.array([1, 2, 3], dtype=np.int8)
    >>> ma.maximum_fill_value(a)
    -128
    >>> a = np.array([1, 2, 3], dtype=np.float32)
    >>> ma.maximum_fill_value(a)
    -inf

    """
        return _extremum_fill_value(obj, max_filler, 'maximum')

    
    def _recursive_set_fill_value(fillvalue, dt):
        '''
    Create a fill value for a structured dtype.

    Parameters
    ----------
    fillvalue : scalar or array_like
        Scalar or array representing the fill value. If it is of shorter
        length than the number of fields in dt, it will be resized.
    dt : dtype
        The structured dtype for which to create the fill value.

    Returns
    -------
    val : tuple
        A tuple of values corresponding to the structured fill value.

    '''
        fillvalue = np.resize(fillvalue, len(dt.names))
        output_value = []
    # WARNING: Decompyle incomplete

    
    def _check_fill_value(fill_value, ndtype):
        '''
    Private function validating the given `fill_value` for the given dtype.

    If fill_value is None, it is set to the default corresponding to the dtype.

    If fill_value is not None, its value is forced to the given dtype.

    The result is always a 0d array.

    '''
        ndtype = np.dtype(ndtype)
    # WARNING: Decompyle incomplete

    
    def set_fill_value(a, fill_value):
        '''
    Set the filling value of a, if a is a masked array.

    This function changes the fill value of the masked array `a` in place.
    If `a` is not a masked array, the function returns silently, without
    doing anything.

    Parameters
    ----------
    a : array_like
        Input array.
    fill_value : dtype
        Filling value. A consistency test is performed to make sure
        the value is compatible with the dtype of `a`.

    Returns
    -------
    None
        Nothing returned by this function.

    See Also
    --------
    maximum_fill_value : Return the default fill value for a dtype.
    MaskedArray.fill_value : Return current fill value.
    MaskedArray.set_fill_value : Equivalent method.

    Examples
    --------
    >>> import numpy.ma as ma
    >>> a = np.arange(5)
    >>> a
    array([0, 1, 2, 3, 4])
    >>> a = ma.masked_where(a < 3, a)
    >>> a
    masked_array(data=[--, --, --, 3, 4],
                 mask=[ True,  True,  True, False, False],
           fill_value=999999)
    >>> ma.set_fill_value(a, -999)
    >>> a
    masked_array(data=[--, --, --, 3, 4],
                 mask=[ True,  True,  True, False, False],
           fill_value=-999)

    Nothing happens if `a` is not a masked array.

    >>> a = list(range(5))
    >>> a
    [0, 1, 2, 3, 4]
    >>> ma.set_fill_value(a, 100)
    >>> a
    [0, 1, 2, 3, 4]
    >>> a = np.arange(5)
    >>> a
    array([0, 1, 2, 3, 4])
    >>> ma.set_fill_value(a, 100)
    >>> a
    array([0, 1, 2, 3, 4])

    '''
        if isinstance(a, MaskedArray):
            a.set_fill_value(fill_value)

    
    def get_fill_value(a):
        '''
    Return the filling value of a, if any.  Otherwise, returns the
    default filling value for that type.

    '''
        if isinstance(a, MaskedArray):
            result = a.fill_value
        else:
            result = default_fill_value(a)
        return result

    
    def common_fill_value(a, b):
        '''
    Return the common filling value of two masked arrays, if any.

    If ``a.fill_value == b.fill_value``, return the fill value,
    otherwise return None.

    Parameters
    ----------
    a, b : MaskedArray
        The masked arrays for which to compare fill values.

    Returns
    -------
    fill_value : scalar or None
        The common fill value, or None.

    Examples
    --------
    >>> x = np.ma.array([0, 1.], fill_value=3)
    >>> y = np.ma.array([0, 1.], fill_value=3)
    >>> np.ma.common_fill_value(x, y)
    3.0

    '''
        t1 = get_fill_value(a)
        t2 = get_fill_value(b)
        if t1 == t2:
            return t1

    
    def filled(a, fill_value = (None,)):
        '''
    Return input as an array with masked data replaced by a fill value.

    If `a` is not a `MaskedArray`, `a` itself is returned.
    If `a` is a `MaskedArray` and `fill_value` is None, `fill_value` is set to
    ``a.fill_value``.

    Parameters
    ----------
    a : MaskedArray or array_like
        An input object.
    fill_value : array_like, optional.
        Can be scalar or non-scalar. If non-scalar, the
        resulting filled array should be broadcastable
        over input array. Default is None.

    Returns
    -------
    a : ndarray
        The filled array.

    See Also
    --------
    compressed

    Examples
    --------
    >>> x = np.ma.array(np.arange(9).reshape(3, 3), mask=[[1, 0, 0],
    ...                                                   [1, 0, 0],
    ...                                                   [0, 0, 0]])
    >>> x.filled()
    array([[999999,      1,      2],
           [999999,      4,      5],
           [     6,      7,      8]])
    >>> x.filled(fill_value=333)
    array([[333,   1,   2],
           [333,   4,   5],
           [  6,   7,   8]])
    >>> x.filled(fill_value=np.arange(3))
    array([[0, 1, 2],
           [0, 4, 5],
           [6, 7, 8]])

    '''
        if hasattr(a, 'filled'):
            return a.filled(fill_value)
        if None(a, ndarray):
            return a
        if None(a, dict):
            return np.array(a, 'O')
        return None.array(a)

    
    def get_masked_subclass(*arrays):
        '''
    Return the youngest subclass of MaskedArray from a list of (masked) arrays.

    In case of siblings, the first listed takes over.

    '''
        if len(arrays) == 1:
            arr = arrays[0]
            if isinstance(arr, MaskedArray):
                rcls = type(arr)
            else:
                rcls = MaskedArray
        else:
            arrcls = arrays()
            rcls = arrcls[0]
            if not issubclass(rcls, MaskedArray):
                rcls = MaskedArray
            for cls in arrcls[1:]:
                if issubclass(cls, rcls):
                    rcls = cls
                if rcls.__name__ == 'MaskedConstant':
                    return MaskedArray
                return (lambda .0: [ type(a) for a in .0 ])

    
    def getdata(a, subok = (True,)):
        '''
    Return the data of a masked array as an ndarray.

    Return the data of `a` (if any) as an ndarray if `a` is a ``MaskedArray``,
    else return `a` as a ndarray or subclass (depending on `subok`) if not.

    Parameters
    ----------
    a : array_like
        Input ``MaskedArray``, alternatively a ndarray or a subclass thereof.
    subok : bool
        Whether to force the output to be a `pure` ndarray (False) or to
        return a subclass of ndarray if appropriate (True, default).

    See Also
    --------
    getmask : Return the mask of a masked array, or nomask.
    getmaskarray : Return the mask of a masked array, or full array of False.

    Examples
    --------
    >>> import numpy.ma as ma
    >>> a = ma.masked_equal([[1,2],[3,4]], 2)
    >>> a
    masked_array(
      data=[[1, --],
            [3, 4]],
      mask=[[False,  True],
            [False, False]],
      fill_value=2)
    >>> ma.getdata(a)
    array([[1, 2],
           [3, 4]])

    Equivalently use the ``MaskedArray`` `data` attribute.

    >>> a.data
    array([[1, 2],
           [3, 4]])

    '''
        
        try:
            data = a._data
        except AttributeError:
            data = np.array(a, copy = False, subok = subok)

        if not subok:
            return data.view(ndarray)

    get_data = getdata
    
    def fix_invalid(a, mask, copy, fill_value = (nomask, True, None)):
        '''
    Return input with invalid data masked and replaced by a fill value.

    Invalid data means values of `nan`, `inf`, etc.

    Parameters
    ----------
    a : array_like
        Input array, a (subclass of) ndarray.
    mask : sequence, optional
        Mask. Must be convertible to an array of booleans with the same
        shape as `data`. True indicates a masked (i.e. invalid) data.
    copy : bool, optional
        Whether to use a copy of `a` (True) or to fix `a` in place (False).
        Default is True.
    fill_value : scalar, optional
        Value used for fixing invalid data. Default is None, in which case
        the ``a.fill_value`` is used.

    Returns
    -------
    b : MaskedArray
        The input array with invalid entries fixed.

    Notes
    -----
    A copy is performed by default.

    Examples
    --------
    >>> x = np.ma.array([1., -1, np.nan, np.inf], mask=[1] + [0]*3)
    >>> x
    masked_array(data=[--, -1.0, nan, inf],
                 mask=[ True, False, False, False],
           fill_value=1e+20)
    >>> np.ma.fix_invalid(x)
    masked_array(data=[--, -1.0, --, --],
                 mask=[ True, False,  True,  True],
           fill_value=1e+20)

    >>> fixed = np.ma.fix_invalid(x)
    >>> fixed.data
    array([ 1.e+00, -1.e+00,  1.e+20,  1.e+20])
    >>> x.data
    array([ 1., -1., nan, inf])

    '''
        a = masked_array(a, copy = copy, mask = mask, subok = True)
        invalid = np.logical_not(np.isfinite(a._data))
        if not invalid.any():
            return a
    # WARNING: Decompyle incomplete

    
    def is_string_or_list_of_strings(val):
