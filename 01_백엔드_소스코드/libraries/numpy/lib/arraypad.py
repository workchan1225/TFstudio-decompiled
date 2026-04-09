# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: arraypad.pyc (Python 3.11)

'''
The arraypad module contains a group of functions to pad values onto the edges
of an n-dimensional array.

'''
import numpy as np
from numpy.core.overrides import array_function_dispatch
from numpy.lib.index_tricks import ndindex
__all__ = [
    'pad']

def _round_if_needed(arr, dtype):
    '''
    Rounds arr inplace if destination dtype is integer.

    Parameters
    ----------
    arr : ndarray
        Input array.
    dtype : dtype
        The dtype of the destination array.
    '''
    if np.issubdtype(dtype, np.integer):
        arr.round(out = arr)
        return None


def _slice_at_axis(sl, axis):
    '''
    Construct tuple of slices to slice an array in the given dimension.

    Parameters
    ----------
    sl : slice
        The slice for the given dimension.
    axis : int
        The axis to which `sl` is applied. All other dimensions are left
        "unsliced".

    Returns
    -------
    sl : tuple of slices
        A tuple with slices matching `shape` in length.

    Examples
    --------
    >>> _slice_at_axis(slice(None, 3, -1), 1)
    (slice(None, None, None), slice(None, 3, -1), (...,))
    '''
    return (slice(None),) * axis + (sl,) + (...,)


def _view_roi(array, original_area_slice, axis):
    '''
    Get a view of the current region of interest during iterative padding.

    When padding multiple dimensions iteratively corner values are
    unnecessarily overwritten multiple times. This function reduces the
    working area for the first dimensions so that corners are excluded.

    Parameters
    ----------
    array : ndarray
        The array with the region of interest.
    original_area_slice : tuple of slices
        Denotes the area with original values of the unpadded array.
    axis : int
        The currently padded dimension assuming that `axis` is padded before
        `axis` + 1.

    Returns
    -------
    roi : ndarray
        The region of interest of the original `array`.
    '''
    axis += 1
    sl = (slice(None),) * axis + original_area_slice[axis:]
    return array[sl]


def _pad_simple(array, pad_width, fill_value = (None,)):
    '''
    Pad array on all sides with either a single value or undefined values.

    Parameters
    ----------
    array : ndarray
        Array to grow.
    pad_width : sequence of tuple[int, int]
        Pad width on both sides for each dimension in `arr`.
    fill_value : scalar, optional
        If provided the padded area is filled with this value, otherwise
        the pad area left undefined.

    Returns
    -------
    padded : ndarray
        The padded array with the same dtype as`array`. Its order will default
        to C-style if `array` is not F-contiguous.
    original_area_slice : tuple
        A tuple of slices pointing to the area of the original array.
    '''
    new_shape = (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(array.shape, pad_width)())
    order = 'F' if array.flags.fnc else 'C'
    padded = np.empty(new_shape, dtype = array.dtype, order = order)
# WARNING: Decompyle incomplete


def _set_pad_area(padded, axis, width_pair, value_pair):
    '''
    Set empty-padded area in given dimension.

    Parameters
    ----------
    padded : ndarray
        Array with the pad area which is modified inplace.
    axis : int
        Dimension with the pad area to set.
    width_pair : (int, int)
        Pair of widths that mark the pad area on both sides in the given
        dimension.
    value_pair : tuple of scalars or ndarrays
        Values inserted into the pad area on each side. It must match or be
        broadcastable to the shape of `arr`.
    '''
    left_slice = _slice_at_axis(slice(None, width_pair[0]), axis)
    padded[left_slice] = value_pair[0]
    right_slice = _slice_at_axis(slice(padded.shape[axis] - width_pair[1], None), axis)
    padded[right_slice] = value_pair[1]


def _get_edges(padded, axis, width_pair):
    '''
    Retrieve edge values from empty-padded array in given dimension.

    Parameters
    ----------
    padded : ndarray
        Empty-padded array.
    axis : int
        Dimension in which the edges are considered.
    width_pair : (int, int)
        Pair of widths that mark the pad area on both sides in the given
        dimension.

    Returns
    -------
    left_edge, right_edge : ndarray
        Edge values of the valid area in `padded` in the given dimension. Its
        shape will always match `padded` except for the dimension given by
        `axis` which will have a length of 1.
    '''
    left_index = width_pair[0]
    left_slice = _slice_at_axis(slice(left_index, left_index + 1), axis)
    left_edge = padded[left_slice]
    right_index = padded.shape[axis] - width_pair[1]
    right_slice = _slice_at_axis(slice(right_index - 1, right_index), axis)
    right_edge = padded[right_slice]
    return (left_edge, right_edge)


def _get_linear_ramps(padded, axis, width_pair, end_value_pair):
    '''
    Construct linear ramps for empty-padded array in given dimension.

    Parameters
    ----------
    padded : ndarray
        Empty-padded array.
    axis : int
        Dimension in which the ramps are constructed.
    width_pair : (int, int)
        Pair of widths that mark the pad area on both sides in the given
        dimension.
    end_value_pair : (scalar, scalar)
        End values for the linear ramps which form the edge of the fully padded
        array. These values are included in the linear ramps.

    Returns
    -------
    left_ramp, right_ramp : ndarray
        Linear ramps to set on both sides of `padded`.
    '''
    pass
# WARNING: Decompyle incomplete


def _get_stats(padded, axis, width_pair, length_pair, stat_func):
    '''
    Calculate statistic for the empty-padded array in given dimension.

    Parameters
    ----------
    padded : ndarray
        Empty-padded array.
    axis : int
        Dimension in which the statistic is calculated.
    width_pair : (int, int)
        Pair of widths that mark the pad area on both sides in the given
        dimension.
    length_pair : 2-element sequence of None or int
        Gives the number of values in valid area from each side that is
        taken into account when calculating the statistic. If None the entire
        valid area in `padded` is considered.
    stat_func : function
        Function to compute statistic. The expected signature is
        ``stat_func(x: ndarray, axis: int, keepdims: bool) -> ndarray``.

    Returns
    -------
    left_stat, right_stat : ndarray
        Calculated statistic for both sides of `padded`.
    '''
    left_index = width_pair[0]
    right_index = padded.shape[axis] - width_pair[1]
    max_length = right_index - left_index
    (left_length, right_length) = length_pair
# WARNING: Decompyle incomplete


def _set_reflect_both(padded, axis, width_pair, method, include_edge = (False,)):
    """
    Pad `axis` of `arr` with reflection.

    Parameters
    ----------
    padded : ndarray
        Input array of arbitrary shape.
    axis : int
        Axis along which to pad `arr`.
    width_pair : (int, int)
        Pair of widths that mark the pad area on both sides in the given
        dimension.
    method : str
        Controls method of reflection; options are 'even' or 'odd'.
    include_edge : bool
        If true, edge value is included in reflection, otherwise the edge
        value forms the symmetric axis to the reflection.

    Returns
    -------
    pad_amt : tuple of ints, length 2
        New index positions of padding to do along the `axis`. If these are
        both 0, padding is done in this dimension.
    """
    (left_pad, right_pad) = width_pair
    old_length = padded.shape[axis] - right_pad - left_pad
    if include_edge:
        edge_offset = 1
    else:
        edge_offset = 0
        old_length -= 1
    if left_pad > 0:
        chunk_length = min(old_length, left_pad)
        stop = left_pad - edge_offset
        start = stop + chunk_length
        left_slice = _slice_at_axis(slice(start, stop, -1), axis)
        left_chunk = padded[left_slice]
        if method == 'odd':
            edge_slice = _slice_at_axis(slice(left_pad, left_pad + 1), axis)
            left_chunk = 2 * padded[edge_slice] - left_chunk
        start = left_pad - chunk_length
        stop = left_pad
        pad_area = _slice_at_axis(slice(start, stop), axis)
        padded[pad_area] = left_chunk
        left_pad -= chunk_length
    if right_pad > 0:
        chunk_length = min(old_length, right_pad)
        start = -right_pad + edge_offset - 2
        stop = start - chunk_length
        right_slice = _slice_at_axis(slice(start, stop, -1), axis)
        right_chunk = padded[right_slice]
        if method == 'odd':
            edge_slice = _slice_at_axis(slice(-right_pad - 1, -right_pad), axis)
            right_chunk = 2 * padded[edge_slice] - right_chunk
        start = padded.shape[axis] - right_pad
        stop = start + chunk_length
        pad_area = _slice_at_axis(slice(start, stop), axis)
        padded[pad_area] = right_chunk
        right_pad -= chunk_length
    return (left_pad, right_pad)


def _set_wrap_both(padded, axis, width_pair, original_period):
    '''
    Pad `axis` of `arr` with wrapped values.

    Parameters
    ----------
    padded : ndarray
        Input array of arbitrary shape.
    axis : int
        Axis along which to pad `arr`.
    width_pair : (int, int)
        Pair of widths that mark the pad area on both sides in the given
        dimension.
    original_period : int
        Original length of data on `axis` of `arr`.

    Returns
    -------
    pad_amt : tuple of ints, length 2
        New index positions of padding to do along the `axis`. If these are
        both 0, padding is done in this dimension.
    '''
    (left_pad, right_pad) = width_pair
    period = padded.shape[axis] - right_pad - left_pad
    period = (period // original_period) * original_period
    new_left_pad = 0
    new_right_pad = 0
    if left_pad > 0:
        slice_end = left_pad + period
        slice_start = slice_end - min(period, left_pad)
        right_slice = _slice_at_axis(slice(slice_start, slice_end), axis)
        right_chunk = padded[right_slice]
        if left_pad > period:
            pad_area = _slice_at_axis(slice(left_pad - period, left_pad), axis)
            new_left_pad = left_pad - period
        else:
            pad_area = _slice_at_axis(slice(None, left_pad), axis)
        padded[pad_area] = right_chunk
    if right_pad > 0:
        slice_start = -right_pad - period
        slice_end = slice_start + min(period, right_pad)
        left_slice = _slice_at_axis(slice(slice_start, slice_end), axis)
        left_chunk = padded[left_slice]
        if right_pad > period:
            pad_area = _slice_at_axis(slice(-right_pad, -right_pad + period), axis)
            new_right_pad = right_pad - period
        else:
            pad_area = _slice_at_axis(slice(-right_pad, None), axis)
        padded[pad_area] = left_chunk
    return (new_left_pad, new_right_pad)


def _as_pairs(x, ndim, as_index = (False,)):
    '''
    Broadcast `x` to an array with the shape (`ndim`, 2).

    A helper function for `pad` that prepares and validates arguments like
    `pad_width` for iteration in pairs.

    Parameters
    ----------
    x : {None, scalar, array-like}
        The object to broadcast to the shape (`ndim`, 2).
    ndim : int
        Number of pairs the broadcasted `x` will have.
    as_index : bool, optional
        If `x` is not None, try to round each element of `x` to an integer
        (dtype `np.intp`) and ensure every element is positive.

    Returns
    -------
    pairs : nested iterables, shape (`ndim`, 2)
        The broadcasted version of `x`.

    Raises
    ------
    ValueError
        If `as_index` is True and `x` contains negative elements.
        Or if `x` is not broadcastable to the shape (`ndim`, 2).
    '''
    pass
# WARNING: Decompyle incomplete


def _pad_dispatcher(array, pad_width, mode = (None,), **kwargs):
    return (array,)

pad = (lambda array, pad_width, mode = ('constant',): array = np.asarray(array)pad_width = np.asarray(pad_width)if not pad_width.dtype.kind == 'i':
raise TypeError('`pad_width` must be of integral type.')pad_width = _as_pairs(pad_width, array.ndim, as_index = True)if callable(mode):
function = mode(padded, _) = _pad_simple(array, pad_width, fill_value = 0)for axis in range(padded.ndim):
view = np.moveaxis(padded, axis, -1)inds = ndindex(view.shape[:-1])inds = inds()for ind in inds:
function(view[ind], pad_width[axis], axis, kwargs)paddedallowed_kwargs = {
'empty': [],
'edge': [],
'wrap': [],
'constant': [
'constant_values'],
'linear_ramp': [
'end_values'],
'maximum': [
'stat_length'],
'mean': [
'stat_length'],
'median': [
'stat_length'],
'minimum': [
'stat_length'],
'reflect': [
'reflect_type'],
'symmetric': [
'reflect_type'] }try:
unsupported_kwargs = set(kwargs) - set(allowed_kwargs[mode])except KeyError:
raise ValueError("mode '{}' is not supported".format(mode)), Noneif unsupported_kwargs:
raise ValueError("unsupported keyword arguments for mode '{}': {}".format(mode, unsupported_kwargs))stat_functions = {
'maximum': np.amax,
'minimum': np.amin,
'mean': np.mean,
'median': np.median }(padded, original_area_slice) = _pad_simple(array, pad_width)axes = range(padded.ndim)if mode == 'constant':
values = kwargs.get('constant_values', 0)values = _as_pairs(values, padded.ndim)for axis, width_pair, value_pair in zip(axes, pad_width, values):
roi = _view_roi(padded, original_area_slice, axis)_set_pad_area(roi, axis, width_pair, value_pair)if mode == 'empty':
passelif array.size == 0:
for axis, width_pair in zip(axes, pad_width):
if array.shape[axis] == 0 and any(width_pair):
raise ValueError("can't extend empty axis {} using modes other than 'constant' or 'empty'".format(axis))if mode == 'edge':
for axis, width_pair in zip(axes, pad_width):
roi = _view_roi(padded, original_area_slice, axis)edge_pair = _get_edges(roi, axis, width_pair)_set_pad_area(roi, axis, width_pair, edge_pair)if mode == 'linear_ramp':
end_values = kwargs.get('end_values', 0)end_values = _as_pairs(end_values, padded.ndim)for axis, width_pair, value_pair in zip(axes, pad_width, end_values):
roi = _view_roi(padded, original_area_slice, axis)ramp_pair = _get_linear_ramps(roi, axis, width_pair, value_pair)_set_pad_area(roi, axis, width_pair, ramp_pair)if mode in stat_functions:
func = stat_functions[mode]length = kwargs.get('stat_length', None)length = _as_pairs(length, padded.ndim, as_index = True)for axis, width_pair, length_pair in zip(axes, pad_width, length):
roi = _view_roi(padded, original_area_slice, axis)stat_pair = _get_stats(roi, axis, width_pair, length_pair, func)_set_pad_area(roi, axis, width_pair, stat_pair)# WARNING: Decompyle incomplete
)()
