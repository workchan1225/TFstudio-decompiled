# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _array_api.pyc (Python 3.11)

'''Tools to support array_api.'''
import itertools
import math
import os
import numpy
import scipy
from scipy.sparse import sparse as sp
from scipy.special import special
from sklearn._config import get_config
from sklearn.externals import array_api_compat
from sklearn.externals import array_api_extra as xpx
from sklearn.externals.array_api_compat import numpy as np_compat
from sklearn.utils._dataframe import is_df_or_series
from sklearn.utils.fixes import parse_version
__all__ = [
    'xpx']
_NUMPY_NAMESPACE_NAMES = {
    'numpy',
    'sklearn.externals.array_api_compat.numpy'}

def yield_namespaces(include_numpy_namespaces = (True,)):
    '''Yield supported namespace.

    This is meant to be used for testing purposes only.

    Parameters
    ----------
    include_numpy_namespaces : bool, default=True
        If True, also yield numpy namespaces.

    Returns
    -------
    array_namespace : str
        The name of the Array API namespace.
    '''
    pass
# WARNING: Decompyle incomplete


def yield_namespace_device_dtype_combinations(include_numpy_namespaces = (True,)):
    '''Yield supported namespace, device, dtype tuples for testing.

    Use this to test that an estimator works with all combinations.
    Use in conjunction with `ids=_get_namespace_device_dtype_ids` to give
    clearer pytest parametrization ID names.

    Parameters
    ----------
    include_numpy_namespaces : bool, default=True
        If True, also yield numpy namespaces.

    Returns
    -------
    array_namespace : str
        The name of the Array API namespace.

    device : str
        The name of the device on which to allocate the arrays. Can be None to
        indicate that the default value should be used.

    dtype_name : str
        The name of the data type to use for arrays. Can be None to indicate
        that the default value should be used.
    '''
    pass
# WARNING: Decompyle incomplete


def _get_namespace_device_dtype_ids(param):
    '''Get pytest parametrization IDs for `yield_namespace_device_dtype_combinations`'''
    
    try:
        import array_api_strict
        if param == array_api_strict.Device('CPU_DEVICE'):
            return 'CPU_DEVICE'
        if None == array_api_strict.Device('device1'):
            return 'device1'
        if None == array_api_strict.Device('device2'):
            return 'device2'
        return None
    except ImportError:
        return None



def _check_array_api_dispatch(array_api_dispatch):
    '''Checks that array API support is functional.

    In particular scipy needs to be recent enough and the environment variable
    needs to be set: SCIPY_ARRAY_API=1.
    '''
    if not array_api_dispatch:
        return None
    scipy_version = None(scipy.__version__)
    min_scipy_version = '1.14.0'
    if scipy_version < parse_version(min_scipy_version):
        raise ImportError(f'''SciPy must be {min_scipy_version} or newer (found {{scipy.__version__}}) to dispatch array using the array API specification''')
    if os.environ.get('SCIPY_ARRAY_API') != '1':
        raise RuntimeError("Scikit-learn array API support was enabled but scipy's own support is not enabled. Please set the SCIPY_ARRAY_API=1 environment variable before importing sklearn or scipy. More details at: https://docs.scipy.org/doc/scipy/dev/api-dev/array_api.html")


def _single_array_device(array):
    '''Hardware device where the array data resides on.'''
    if not hasattr(array, 'device') or get_config()['array_api_dispatch']:
        return None
    return None.device


def device(*, remove_none, remove_types, *array_list):
    '''Hardware device where the array data resides on.

    If the hardware device is not the same for all arrays, an error is raised.

    Parameters
    ----------
    *array_list : arrays
        List of array instances from NumPy or an array API compatible library.

    remove_none : bool, default=True
        Whether to ignore None objects passed in array_list.

    remove_types : tuple or list, default=(str,)
        Types to ignore in array_list.

    Returns
    -------
    out : device
        `device` object (see the "Device Support" section of the array API spec).
    '''
    pass
# WARNING: Decompyle incomplete


def size(x):
    '''Return the total number of elements of x.

    Parameters
    ----------
    x : array
        Array instance from NumPy or an array API compatible library.

    Returns
    -------
    out : int
        Total number of elements.
    '''
    return math.prod(x.shape)


def _is_numpy_namespace(xp):
    '''Return True if xp is backed by NumPy.'''
    return xp.__name__ in _NUMPY_NAMESPACE_NAMES


def _union1d(a, b, xp):
    if _is_numpy_namespace(xp):
        cached_unique = cached_unique
        import sklearn.utils._unique
        (a_unique, b_unique) = cached_unique(a, b, xp = xp)
        return xp.asarray(numpy.union1d(a_unique, b_unique))
    if not  == None.ndim, b.ndim or None.ndim, b.ndim == 1:
        pass
    
# WARNING: Decompyle incomplete


def supported_float_dtypes(xp, device = (None,)):
    '''Supported floating point types for the namespace.

    Parameters
    ----------
    xp : module
        Array namespace to inspect.

    device : str or device instance from xp, default=None
        Device to use for dtype selection. If ``None``, then a default device
        is assumed.

    Returns
    -------
    supported_dtypes : tuple
        Tuple of real floating data types supported by the provided array namespace,
        ordered from the highest precision to lowest.

    See Also
    --------
    max_precision_float_dtype : Maximum float dtype for a namespace/device pair.

    Notes
    -----
    `float16` is not officially part of the Array API spec at the
    time of writing but scikit-learn estimators and functions can choose
    to accept it when xp.float16 is defined.

    Additionally, some devices available within a namespace may not support
    all floating-point types that the namespace provides.

    https://data-apis.org/array-api/latest/API_specification/data_types.html
    '''
    dtypes_dict = xp.__array_namespace_info__().dtypes(kind = 'real floating', device = device)
    valid_float_dtypes = []
    for dtype_key in ('float64', 'float32'):
        if dtype_key in dtypes_dict:
            valid_float_dtypes.append(dtypes_dict[dtype_key])
        if hasattr(xp, 'float16'):
            valid_float_dtypes.append(xp.float16)
    return tuple(valid_float_dtypes)


def _remove_non_arrays(*, remove_none, remove_types, *arrays):
    '''Filter arrays to exclude None and/or specific types.

    Sparse arrays are always filtered out.

    Parameters
    ----------
    *arrays : array objects
        Array objects.

    remove_none : bool, default=True
        Whether to ignore None objects passed in arrays.

    remove_types : tuple or list, default=(str,)
        Types to ignore in the arrays.

    Returns
    -------
    filtered_arrays : list
        List of arrays filtered as requested. An empty list is returned if no input
        passes the filters.
    '''
    filtered_arrays = []
    remove_types = tuple(remove_types)
# WARNING: Decompyle incomplete


def get_namespace(*, remove_none, remove_types, xp, *arrays):
    '''Get namespace of arrays.

    Introspect `arrays` arguments and return their common Array API compatible
    namespace object, if any.

    Note that sparse arrays are filtered by default.

    See: https://numpy.org/neps/nep-0047-array-api-standard.html

    If `arrays` are regular numpy arrays, `array_api_compat.numpy` is returned instead.

    Namespace support is not enabled by default. To enabled it call:

      sklearn.set_config(array_api_dispatch=True)

    or:

      with sklearn.config_context(array_api_dispatch=True):
          # your code here

    Otherwise `array_api_compat.numpy` is
    always returned irrespective of the fact that arrays implement the
    `__array_namespace__` protocol or not.

    Note that if no arrays pass the set filters, ``_NUMPY_API_WRAPPER_INSTANCE, False``
    is returned.

    Parameters
    ----------
    *arrays : array objects
        Array objects.

    remove_none : bool, default=True
        Whether to ignore None objects passed in arrays.

    remove_types : tuple or list, default=(str,)
        Types to ignore in the arrays.

    xp : module, default=None
        Precomputed array namespace module. When passed, typically from a caller
        that has already performed inspection of its own inputs, skips array
        namespace inspection.

    Returns
    -------
    namespace : module
        Namespace shared by array objects. If any of the `arrays` are not arrays,
        the namespace defaults to the NumPy namespace.

    is_array_api_compliant : bool
        True if the arrays are containers that implement the array API spec (see
        https://data-apis.org/array-api/latest/index.html).
        Always False when array_api_dispatch=False.
    '''
    array_api_dispatch = get_config()['array_api_dispatch']
# WARNING: Decompyle incomplete


def get_namespace_and_device(*, remove_none, remove_types, xp, *array_list):
    '''Combination into one single function of `get_namespace` and `device`.

    Parameters
    ----------
    *array_list : array objects
        Array objects.
    remove_none : bool, default=True
        Whether to ignore None objects passed in arrays.
    remove_types : tuple or list, default=(str,)
        Types to ignore in the arrays.
    xp : module, default=None
        Precomputed array namespace module. When passed, typically from a caller
        that has already performed inspection of its own inputs, skips array
        namespace inspection.

    Returns
    -------
    namespace : module
        Namespace shared by array objects. If any of the `arrays` are not arrays,
        the namespace defaults to NumPy.
    is_array_api_compliant : bool
        True if the arrays are containers that implement the Array API spec.
        Always False when array_api_dispatch=False.
    device : device
        `device` object (see the "Device Support" section of the array API spec).
    '''
    skip_remove_kwargs = dict(remove_none = False, remove_types = [])
# WARNING: Decompyle incomplete


def move_to(*, xp, device, *arrays):
    '''Move all arrays to `xp` and `device`.

    Each array will be moved to the reference namespace and device if
    it is not already using it. Otherwise the array is left unchanged.

    `array` may contain `None` entries, these are left unchanged.

    Sparse arrays are accepted (as pass through) if the reference namespace is
    NumPy, in which case they are returned unchanged. Otherwise a `TypeError`
    is raised.

    Parameters
    ----------
    *arrays : iterable of arrays
        Arrays to (potentially) move.

    xp : namespace
        Array API namespace to move arrays to.

    device : device
        Array API device to move arrays to.

    Returns
    -------
    arrays : tuple or array
        Tuple of arrays with the same namespace and device as reference. Single array
        returned if only one `arrays` input.
    '''
    sparse_mask = arrays()
    none_mask = arrays()
    if not any(sparse_mask) and _is_numpy_namespace(xp):
        raise TypeError('Sparse arrays are only accepted (and passed through) when the target namespace is Numpy')
    converted_arrays = []
    for array, is_sparse, is_none in zip(arrays, sparse_mask, none_mask):
        if is_none:
            converted_arrays.append(None)
            continue
        if is_sparse:
            converted_arrays.append(array)
            continue
        (xp_array, _, device_array) = get_namespace_and_device(array)
        if xp == xp_array and device == device_array:
            converted_arrays.append(array)
            continue
        array_converted = xp.from_dlpack(array, device = device)
    except (AttributeError, TypeError, NotImplementedError, BufferError, ValueError):
        (lambda .0: [ sp.issparse(array) for array in .0 ])
        if _is_numpy_namespace(xp):
            array_converted = _convert_to_numpy(array, xp_array)
        elif _is_numpy_namespace(xp_array):
            array_converted = xp.asarray(array, device = device)
        else:
            array_np = _convert_to_numpy(array, xp_array)
            array_converted = xp.asarray(array_np, device = device)
    converted_arrays.append(array_converted)
    continue
    return converted_arrays[0] if len(converted_arrays) == 1 else tuple(converted_arrays)


def _expit(X, xp = (None,)):
    (xp, _) = get_namespace(X, xp = xp)
    if _is_numpy_namespace(xp):
        return xp.asarray(special.expit(numpy.asarray(X)))
    return None / (1 + xp.exp(-X))


def _validate_diagonal_args(array, value, xp):
    '''Validate arguments to `_fill_diagonal`/`_add_to_diagonal`.'''
    if array.ndim != 2:
        raise ValueError(f'''`array` should be 2D. Got array with shape {tuple(array.shape)}''')
    value = xp.asarray(value, dtype = array.dtype, device = device(array))
    if value.ndim not in (0, 1):
        raise ValueError(f'''`value` needs to be a scalar or a 1D array, got a {value.ndim}D array instead.''')
    min_rows_columns = min(array.shape)
    if value.ndim == 1 and value.shape[0] != min_rows_columns:
        raise ValueError(f'''`value` needs to be a scalar or 1D array of the same length as the diagonal of `array` ({min_rows_columns}). Got {value.shape[0]}''')
    return (value, min_rows_columns)


def _fill_diagonal(array, value, xp):
    '''Minimal implementation of `numpy.fill_diagonal`.

    `wrap` is not supported (i.e. always False). `value` should be a scalar or
    1D of greater or equal length as the diagonal (i.e., `value` is never repeated
    when shorter).

    Note `array` is altered in place.
    '''
    (value, min_rows_columns) = _validate_diagonal_args(array, value, xp)
    if _is_numpy_namespace(xp):
        xp.fill_diagonal(array, value, wrap = False)
        return None
    if None.ndim == 0:
        for i in range(min_rows_columns):
            array[(i, i)] = value
            return None
            for i in range(min_rows_columns):
                array[(i, i)] = value[i]
                return None


def _add_to_diagonal(array, value, xp):
    '''Add `value` to diagonal of `array`.

    Related to `fill_diagonal`. `value` should be a scalar or
    1D of greater or equal length as the diagonal (i.e., `value` is never repeated
    when shorter).

    Note `array` is altered in place.
    '''
    (value, min_rows_columns) = _validate_diagonal_args(array, value, xp)
    if _is_numpy_namespace(xp):
        step = array.shape[1] + 1
        end = array.shape[1] * array.shape[1]
        return None
    None.linalg.diagonal(array) + value = None
    for i in range(min_rows_columns):
        array[(i, i)] = value[i]
        return None


def _is_xp_namespace(xp, name):
    return xp.__name__ in (name, f'''array_api_compat.{name}''', f'''sklearn.externals.array_api_compat.{name}''')


def _max_precision_float_dtype(xp, device):
    '''Return the float dtype with the highest precision supported by the device.'''
    if _is_xp_namespace(xp, 'torch') and str(device).startswith('mps'):
        return xp.float32
    return None.float64


def _find_matching_floating_dtype(*, xp, *arrays):
    '''Find a suitable floating point dtype when computing with arrays.

    If any of the arrays are floating point, return the dtype with the highest
    precision by following official type promotion rules:

    https://data-apis.org/array-api/latest/API_specification/type_promotion.html

    If there are no floating point input arrays (all integral inputs for
    instance), return the default floating point dtype for the namespace.
    '''
    pass
# WARNING: Decompyle incomplete


def _average(a, axis, weights, normalize, xp = (None, None, True, None)):
    '''Partial port of np.average to support the Array API.

    It does a best effort at mimicking the return dtype rule described at
    https://numpy.org/doc/stable/reference/generated/numpy.average.html but
    only for the common cases needed in scikit-learn.
    '''
    (xp, _, device_) = get_namespace_and_device(a, weights, xp = xp)
# WARNING: Decompyle incomplete


def _median(x, axis, keepdims, xp = (None, False, None)):
    (xp, _, device) = get_namespace_and_device(x, xp = xp)
    if array_api_compat.is_torch_namespace(xp):
        return xp.quantile(x, q = 0.5, dim = axis, keepdim = keepdims)
    if None(xp, 'median'):
        return xp.median(x, axis = axis, keepdims = keepdims)
    x_np = None(x, xp = xp)
    return xp.asarray(numpy.median(x_np, axis = axis, keepdims = keepdims), device = device)


def _xlogy(x, y, xp = (None,)):
    (xp, _, device_) = get_namespace_and_device(x, y, xp = xp)
    numpy.errstate(divide = 'ignore', invalid = 'ignore')
    temp = x * xp.log(y)
    None(None, None)


def _nanmin(X, axis, xp = (None, None)):
    (xp, _, device_) = get_namespace_and_device(X, xp = xp)
    if _is_numpy_namespace(xp):
        return xp.asarray(numpy.nanmin(X, axis = axis))
    mask = None.isnan(X)
    X = xp.min(xp.where(mask, xp.asarray(+(xp.inf), dtype = X.dtype, device = device_), X), axis = axis)
    mask = xp.all(mask, axis = axis)
    if xp.any(mask):
        X = xp.where(mask, xp.asarray(xp.nan, dtype = X.dtype, device = device_), X)
    return X


def _nanmax(X, axis, xp = (None, None)):
    (xp, _, device_) = get_namespace_and_device(X, xp = xp)
    if _is_numpy_namespace(xp):
        return xp.asarray(numpy.nanmax(X, axis = axis))
    mask = None.isnan(X)
    X = xp.max(xp.where(mask, xp.asarray(-(xp.inf), dtype = X.dtype, device = device_), X), axis = axis)
    mask = xp.all(mask, axis = axis)
    if xp.any(mask):
        X = xp.where(mask, xp.asarray(xp.nan, dtype = X.dtype, device = device_), X)
    return X


def _nanmean(X, axis, xp = (None, None)):
    (xp, _, device_) = get_namespace_and_device(X, xp = xp)
    if _is_numpy_namespace(xp):
        return xp.asarray(numpy.nanmean(X, axis = axis))
    mask = None.isnan(X)
    total = xp.sum(xp.where(mask, xp.asarray(0, dtype = X.dtype, device = device_), X), axis = axis)
    count = xp.sum(xp.astype(xp.logical_not(mask), X.dtype), axis = axis)
    return total / count


def _nansum(X, axis, xp, keepdims, dtype = (None, None, False, None)):
    (xp, _, X_device) = get_namespace_and_device(X, xp = xp)
    if _is_numpy_namespace(xp):
        return xp.asarray(numpy.nansum(X, axis = axis, keepdims = keepdims, dtype = dtype))
    mask = None.isnan(X)
    masked_arr = xp.where(mask, xp.asarray(0, device = X_device, dtype = X.dtype), X)
    return xp.sum(masked_arr, axis = axis, keepdims = keepdims, dtype = dtype)


def _asarray_with_order(array, dtype = None, order = (None, None, None), copy = {
    'xp': None,
    'device': None }, *, xp, device):
    '''Helper to support the order kwarg only for NumPy-backed arrays

    Memory layout parameter `order` is not exposed in the Array API standard,
    however some input validation code in scikit-learn needs to work both
    for classes and functions that will leverage Array API only operations
    and for code that inherently relies on NumPy backed data containers with
    specific memory layout constraints (e.g. our own Cython code). The
    purpose of this helper is to make it possible to share code for data
    container validation without memory copies for both downstream use cases:
    the `order` parameter is only enforced if the input array implementation
    is NumPy based, otherwise `order` is just silently ignored.
    '''
    (xp, _) = get_namespace(array, xp = xp)
    if _is_numpy_namespace(xp):
        if copy is True:
            array = numpy.array(array, order = order, dtype = dtype)
        else:
            array = numpy.asarray(array, order = order, dtype = dtype)
        return xp.asarray(array)
    return None.asarray(array, dtype = dtype, copy = copy, device = device)


def _ravel(array, xp = (None,)):
    '''Array API compliant version of np.ravel.

    For non numpy namespaces, it just returns a flattened array, that might
    be or not be a copy.
    '''
    (xp, _) = get_namespace(array, xp = xp)
    if _is_numpy_namespace(xp):
        array = numpy.asarray(array)
        return xp.asarray(numpy.ravel(array, order = 'C'))
    return None.reshape(array, shape = (-1,))


def _convert_to_numpy(array, xp):
    '''Convert X into a NumPy ndarray on the CPU.'''
    if _is_xp_namespace(xp, 'torch'):
        return array.cpu().numpy()
    if None(xp, 'cupy'):
        return array.get()
    if None(xp, 'array_api_strict'):
        return numpy.asarray(xp.asarray(array, device = xp.Device('CPU_DEVICE')))
    return None.asarray(array)


def _estimator_with_converted_arrays(estimator, converter):
    '''Create new estimator which converting all attributes that are arrays.

    The converter is called on all NumPy arrays and arrays that support the
    `DLPack interface <https://dmlc.github.io/dlpack/latest/>`__.

    Parameters
    ----------
    estimator : Estimator
        Estimator to convert

    converter : callable
        Callable that takes an array attribute and returns the converted array.

    Returns
    -------
    new_estimator : Estimator
        Convert estimator
    '''
    clone = clone
    import sklearn.base
    new_estimator = clone(estimator)
    for key, attribute in vars(estimator).items():
        if hasattr(attribute, '__dlpack__') or isinstance(attribute, numpy.ndarray):
            attribute = converter(attribute)
        setattr(new_estimator, key, attribute)
        return new_estimator


def _atol_for_type(dtype_or_dtype_name):
    '''Return the absolute tolerance for a given numpy dtype.'''
    pass
# WARNING: Decompyle incomplete


def indexing_dtype(xp):
    '''Return a platform-specific integer dtype suitable for indexing.

    On 32-bit platforms, this will typically return int32 and int64 otherwise.

    Note: using dtype is recommended for indexing transient array
    datastructures. For long-lived arrays, such as the fitted attributes of
    estimators, it is instead recommended to use platform-independent int32 if
    we do not expect to index more 2B elements. Using fixed dtypes simplifies
    the handling of serialized models, e.g. to deploy a model fit on a 64-bit
    platform to a target 32-bit platform such as WASM/pyodide.
    '''
    return xp.asarray(0).dtype


def _isin(element, test_elements, xp, assume_unique, invert = (False, False)):
    '''Calculates ``element in test_elements``, broadcasting over `element`
    only.

    Returns a boolean array of the same shape as `element` that is True
    where an element of `element` is in `test_elements` and False otherwise.
    '''
    if _is_numpy_namespace(xp):
        return xp.asarray(numpy.isin(element = element, test_elements = test_elements, assume_unique = assume_unique, invert = invert))
    original_element_shape = None.shape
    element = xp.reshape(element, (-1,))
    test_elements = xp.reshape(test_elements, (-1,))
    return xp.reshape(_in1d(ar1 = element, ar2 = test_elements, xp = xp, assume_unique = assume_unique, invert = invert), original_element_shape)


def _in1d(ar1, ar2, xp, assume_unique, invert = (False, False)):
    '''Checks whether each element of an array is also present in a
    second array.

    Returns a boolean array the same length as `ar1` that is True
    where an element of `ar1` is in `ar2` and False otherwise.

    This function has been adapted using the original implementation
    present in numpy:
    https://github.com/numpy/numpy/blob/v1.26.0/numpy/lib/arraysetops.py#L524-L758
    '''
    (xp, _) = get_namespace(ar1, ar2, xp = xp)
    if ar2.shape[0] < 10 * ar1.shape[0] ** 0.145:
        if invert:
            mask = xp.ones(ar1.shape[0], dtype = xp.bool, device = device(ar1))
            for a in ar2:
                mask &= (ar1 != a)
        mask = xp.zeros(ar1.shape[0], dtype = xp.bool, device = device(ar1))
        for a in ar2:
            mask |= (ar1 == a)
            return mask
            if not assume_unique:
                (ar1, rev_idx) = xp.unique_inverse(ar1)
                ar2 = xp.unique_values(ar2)
    ar = xp.concat((ar1, ar2))
    device_ = device(ar)
    order = xp.argsort(ar, stable = True)
    reverse_order = xp.argsort(order, stable = True)
    sar = xp.take(ar, order, axis = 0)
    if size(sar) >= 1:
        bool_ar = sar[1:] != sar[:-1] if invert else sar[1:] == sar[:-1]
    elif invert:
        pass
    
    bool_ar = xp.asarray([
        True])
    flag = xp.concat((bool_ar, xp.asarray([
        invert], device = device_)))
    ret = xp.take(flag, reverse_order, axis = 0)
    if assume_unique:
        return ret[:ar1.shape[0]]
    return xp.asarray([
        False]).take(ret, rev_idx, axis = 0)


def _count_nonzero(X, axis, sample_weight, xp, device = (None, None, None, None)):
    '''A variant of `sklearn.utils.sparsefuncs.count_nonzero` for the Array API.

    If the array `X` is sparse, and we are using the numpy namespace then we
    simply call the original function. This function only supports 2D arrays.
    '''
    count_nonzero = count_nonzero
    import sklearn.utils.sparsefuncs
    (xp, _) = get_namespace(X, sample_weight, xp = xp)
    if _is_numpy_namespace(xp) and sp.issparse(X):
        return count_nonzero(X, axis = axis, sample_weight = sample_weight)
# WARNING: Decompyle incomplete


def _modify_in_place_if_numpy(xp = None, func = {
    'out': None }, *, out, *args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def _bincount(array, weights, minlength, xp = (None, None, None)):
    (xp, _) = get_namespace(array, xp = xp)
    if hasattr(xp, 'bincount'):
        return xp.bincount(array, weights = weights, minlength = minlength)
    array_np = None(array, xp = xp)
# WARNING: Decompyle incomplete


def _tolist(array, xp = (None,)):
    (xp, _) = get_namespace(array, xp = xp)
    if _is_numpy_namespace(xp):
        return array.tolist()
    array_np = None(array, xp = xp)
    return array_np()


def _logsumexp(array, axis, xp = (None, None)):
    (xp, _, device) = get_namespace_and_device(array, xp = xp)
# WARNING: Decompyle incomplete


def _cholesky(covariance, xp):
    if _is_numpy_namespace(xp):
        return scipy.linalg.cholesky(covariance, lower = True)
    return None.linalg.cholesky(covariance)


def _linalg_solve(cov_chol, eye_matrix, xp):
    if _is_numpy_namespace(xp):
        return scipy.linalg.solve_triangular(cov_chol, eye_matrix, lower = True)
    return None.linalg.solve(cov_chol, eye_matrix)


def _half_multinomial_loss(y, pred, sample_weight, xp = (None, None)):
    '''A version of the multinomial loss that is compatible with the array API'''
    (xp, _, device_) = get_namespace_and_device(y, pred, sample_weight)
    log_sum_exp = _logsumexp(pred, axis = 1, xp = xp)
    y = xp.asarray(y, dtype = xp.int64, device = device_)
    class_margins = xp.arange(y.shape[0], device = device_) * pred.shape[1]
    label_predictions = xp.take(_ravel(pred), y + class_margins)
    return float(_average(log_sum_exp - label_predictions, weights = sample_weight, xp = xp))
