# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shape_base.pyc (Python 3.11)

__all__ = [
    'atleast_1d',
    'atleast_2d',
    'atleast_3d',
    'block',
    'hstack',
    'stack',
    'vstack']
import functools
import itertools
import operator
import warnings
from  import numeric as _nx
from  import overrides
from multiarray import array, asanyarray, normalize_axis_index
from  import fromnumeric as _from_nx
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')

def _atleast_1d_dispatcher(*arys):
    return arys

atleast_1d = (lambda : res = []for ary in arys:
ary = asanyarray(ary)if ary.ndim == 0:
result = ary.reshape(1)else:
result = aryres.append(result)if len(res) == 1:
res[0]None)()

def _atleast_2d_dispatcher(*arys):
    return arys

atleast_2d = (lambda : res = []for ary in arys:
ary = asanyarray(ary)if ary.ndim == 0:
result = ary.reshape(1, 1)elif ary.ndim == 1:
result = ary[(_nx.newaxis, :)]else:
result = aryres.append(result)if len(res) == 1:
res[0]None)()

def _atleast_3d_dispatcher(*arys):
    return arys

atleast_3d = (lambda : res = []for ary in arys:
ary = asanyarray(ary)if ary.ndim == 0:
result = ary.reshape(1, 1, 1)elif ary.ndim == 1:
result = ary[(_nx.newaxis, :, _nx.newaxis)]elif ary.ndim == 2:
result = ary[(:, :, _nx.newaxis)]else:
result = aryres.append(result)if len(res) == 1:
res[0]None)()

def _arrays_for_stack_dispatcher(arrays):
    if not hasattr(arrays, '__getitem__'):
        raise TypeError('arrays to stack must be passed as a "sequence" type such as list or tuple.')
    return tuple(arrays)


def _vhstack_dispatcher(tup = array_function_dispatch(_atleast_3d_dispatcher), *, dtype, casting):
    return _arrays_for_stack_dispatcher(tup)

vstack = (lambda tup = array_function_dispatch(_vhstack_dispatcher), *, dtype: pass# WARNING: Decompyle incomplete
)()
hstack = (lambda tup = array_function_dispatch(_vhstack_dispatcher), *, dtype: pass# WARNING: Decompyle incomplete
)()

def _stack_dispatcher(arrays = array_function_dispatch(_atleast_2d_dispatcher), axis = (None, None), out = {
    'dtype': None,
    'casting': None }, *, dtype, casting):
    arrays = _arrays_for_stack_dispatcher(arrays)
# WARNING: Decompyle incomplete

stack = (lambda arrays = array_function_dispatch(_stack_dispatcher), axis = (0, None), out = {
    'dtype': None,
    'casting': 'same_kind' }, *, dtype, casting, shapes = None: pass# WARNING: Decompyle incomplete
)()
_size = getattr(_from_nx.size, '__wrapped__', _from_nx.size)
_ndim = getattr(_from_nx.ndim, '__wrapped__', _from_nx.ndim)
_concatenate = getattr(_from_nx.concatenate, '__wrapped__', _from_nx.concatenate)

def _block_format_index(index):
    '''
    Convert a list of indices ``[0, 1, 2]`` into ``"arrays[0][1][2]"``.
    '''
    idx_str = (lambda .0: pass# WARNING: Decompyle incomplete
)(index())
    return 'arrays' + idx_str


def _block_check_depths_match(arrays, parent_index = ([],)):
    '''
    Recursive function checking that the depths of nested lists in `arrays`
    all match. Mismatch raises a ValueError as described in the block
    docstring below.

    The entire index (rather than just the depth) needs to be calculated
    for each innermost list, in case an error needs to be raised, so that
    the index of the offending list can be printed as part of the error.

    Parameters
    ----------
    arrays : nested list of arrays
        The arrays to check
    parent_index : list of int
        The full index of `arrays` within the nested lists passed to
        `_block_check_depths_match` at the top of the recursion.

    Returns
    -------
    first_index : list of int
        The full index of an element from the bottom of the nesting in
        `arrays`. If any element at the bottom is an empty list, this will
        refer to it, and the last index along the empty axis will be None.
    max_arr_ndim : int
        The maximum of the ndims of the arrays nested in `arrays`.
    final_size: int
        The number of elements in the final array. This is used the motivate
        the choice of algorithm used using benchmarking wisdom.

    '''
    pass
# WARNING: Decompyle incomplete


def _atleast_nd(a, ndim):
    return array(a, ndmin = ndim, copy = False, subok = True)


def _accumulate(values):
    return list(itertools.accumulate(values))


def _concatenate_shapes(shapes, axis):
    '''Given array shapes, return the resulting shape and slices prefixes.

    These help in nested concatenation.

    Returns
    -------
    shape: tuple of int
        This tuple satisfies::

            shape, _ = _concatenate_shapes([arr.shape for shape in arrs], axis)
            shape == concatenate(arrs, axis).shape

    slice_prefixes: tuple of (slice(start, end), )
        For a list of arrays being concatenated, this returns the slice
        in the larger array at axis that needs to be sliced into.

        For example, the following holds::

            ret = concatenate([a, b, c], axis)
            _, (sl_a, sl_b, sl_c) = concatenate_slices([a, b, c], axis)

            ret[(slice(None),) * axis + sl_a] == a
            ret[(slice(None),) * axis + sl_b] == b
            ret[(slice(None),) * axis + sl_c] == c

        These are called slice prefixes since they are used in the recursive
        blocking algorithm to compute the left-most slices during the
        recursion. Therefore, they must be prepended to rest of the slice
        that was computed deeper in the recursion.

        These are returned as tuples to ensure that they can quickly be added
        to existing slice tuple without creating a new tuple every time.

    '''
    pass
# WARNING: Decompyle incomplete


def _block_info_recursion(arrays, max_depth, result_ndim, depth = (0,)):
    '''
    Returns the shape of the final array, along with a list
    of slices and a list of arrays that can be used for assignment inside the
    new array

    Parameters
    ----------
    arrays : nested list of arrays
        The arrays to check
    max_depth : list of int
        The number of nested lists
    result_ndim : int
        The number of dimensions in thefinal array.

    Returns
    -------
    shape : tuple of int
        The shape that the final array will take on.
    slices: list of tuple of slices
        The slices into the full array required for assignment. These are
        required to be prepended with ``(Ellipsis, )`` to obtain to correct
        final index.
    arrays: list of ndarray
        The data to assign to each slice of the full array

    '''
    pass
# WARNING: Decompyle incomplete


def _block(arrays, max_depth, result_ndim, depth = (0,)):
    '''
    Internal implementation of block based on repeated concatenation.
    `arrays` is the argument passed to
    block. `max_depth` is the depth of nested lists within `arrays` and
    `result_ndim` is the greatest of the dimensions of the arrays in
    `arrays` and the depth of the lists in `arrays` (see block docstring
    for details).
    '''
    pass
# WARNING: Decompyle incomplete


def _block_dispatcher(arrays):
    pass
# WARNING: Decompyle incomplete

block = (lambda arrays: (arrays, list_ndim, result_ndim, final_size) = _block_setup(arrays)if list_ndim * final_size > 524288:
_block_slicing(arrays, list_ndim, result_ndim)None(arrays, list_ndim, result_ndim))()

def _block_setup(arrays):
    '''
    Returns
    (`arrays`, list_ndim, result_ndim, final_size)
    '''
    (bottom_index, arr_ndim, final_size) = _block_check_depths_match(arrays)
    list_ndim = len(bottom_index)
# WARNING: Decompyle incomplete


def _block_slicing(arrays, list_ndim, result_ndim):
    (shape, slices, arrays) = _block_info_recursion(arrays, list_ndim, result_ndim)
# WARNING: Decompyle incomplete


def _block_concatenate(arrays, list_ndim, result_ndim):
    result = _block(arrays, list_ndim, result_ndim)
    if list_ndim == 0:
        result = result.copy()
    return result
