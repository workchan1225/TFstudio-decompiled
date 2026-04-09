# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shape_base.pyc (Python 3.11)

import functools

numeric
from numpy.core.numeric import asarray, zeros, array, asanyarray
zeros = zeros
array = array
asanyarray = asanyarray
import numpy.core.numeric, core
from numpy.core.fromnumeric import reshape, transpose
from numpy.core.multiarray import normalize_axis_index
from numpy.core import overrides
from numpy.core import vstack, atleast_3d
from numpy.core.numeric import normalize_axis_tuple
from numpy.core.shape_base import _arrays_for_stack_dispatcher
from numpy.lib.index_tricks import ndindex
from numpy.matrixlib.defmatrix import matrix
__all__ = [
    'column_stack',
    'row_stack',
    'dstack',
    'array_split',
    'split',
    'hsplit',
    'vsplit',
    'dsplit',
    'apply_over_axes',
    'expand_dims',
    'apply_along_axis',
    'kron',
    'tile',
    'get_array_wrap',
    'take_along_axis',
    'put_along_axis']
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')

def _make_along_axis_idx(arr_shape, indices, axis):
    if not _nx.issubdtype(indices.dtype, _nx.integer):
        raise IndexError('`indices` must be an integer array')
    if len(arr_shape) != indices.ndim:
        raise ValueError('`indices` and `arr` must have the same number of dimensions')
    shape_ones = (1,) * indices.ndim
    dest_dims = list(range(axis)) + [
        None] + list(range(axis + 1, indices.ndim))
    fancy_index = []
# WARNING: Decompyle incomplete


def _take_along_axis_dispatcher(arr, indices, axis):
    return (arr, indices)

take_along_axis = (lambda arr, indices, axis: pass# WARNING: Decompyle incomplete
)()

def _put_along_axis_dispatcher(arr, indices, values, axis):
    return (arr, indices, values)

put_along_axis = (lambda arr, indices, values, axis: pass# WARNING: Decompyle incomplete
)()

def _apply_along_axis_dispatcher(func1d, axis, arr, *args, **kwargs):
    return (arr,)

apply_along_axis = (lambda func1d, axis, arr: arr = asanyarray(arr)nd = arr.ndimaxis = normalize_axis_index(axis, nd)in_dims = list(range(nd))inarr_view = transpose(arr, in_dims[:axis] + in_dims[axis + 1:] + [
axis])inds = ndindex(inarr_view.shape[:-1])inds = inds()try:
ind0 = next(inds)except StopIteration:
raise ValueError('Cannot apply_along_axis when any iteration dimensions are 0'), None# WARNING: Decompyle incomplete
)()

def _apply_over_axes_dispatcher(func, a, axes):
    return (a,)

apply_over_axes = (lambda func, a, axes: val = asarray(a)N = a.ndimif array(axes).ndim == 0:
axes = (axes,)# WARNING: Decompyle incomplete
)()

def _expand_dims_dispatcher(a, axis):
    return (a,)

expand_dims = (lambda a, axis: pass# WARNING: Decompyle incomplete
)()
row_stack = vstack

def _column_stack_dispatcher(tup):
    return _arrays_for_stack_dispatcher(tup)

column_stack = (lambda tup: arrays = []for v in tup:
arr = asanyarray(v)if arr.ndim < 2:
arr = array(arr, copy = False, subok = True, ndmin = 2).Tarrays.append(arr)_nx.concatenate(arrays, 1))()

def _dstack_dispatcher(tup):
    return _arrays_for_stack_dispatcher(tup)

dstack = (lambda tup: pass# WARNING: Decompyle incomplete
)()

def _replace_zero_by_x_arrays(sub_arys):
    for i in range(len(sub_arys)):
        if _nx.ndim(sub_arys[i]) == 0:
            sub_arys[i] = _nx.empty(0, dtype = sub_arys[i].dtype)
            continue
        if _nx.sometrue(_nx.equal(_nx.shape(sub_arys[i]), 0)):
            sub_arys[i] = _nx.empty(0, dtype = sub_arys[i].dtype)
        return sub_arys


def _array_split_dispatcher(ary, indices_or_sections, axis = (None,)):
    return (ary, indices_or_sections)

array_split = (lambda ary, indices_or_sections, axis = (0,): try:
Ntotal = ary.shape[axis]except AttributeError:
Ntotal = len(ary)try:
Nsections = len(indices_or_sections) + 1div_points = [
0] + list(indices_or_sections) + [
Ntotal]except TypeError:
Nsections = int(indices_or_sections)if Nsections <= 0:
raise ValueError('number sections must be larger than 0.'), None(Neach_section, extras) = divmod(Ntotal, Nsections)section_sizes = [
0] + extras * [
Neach_section + 1] + (Nsections - extras) * [
Neach_section]div_points = _nx.array(section_sizes, dtype = _nx.intp).cumsum()sub_arys = []sary = _nx.swapaxes(ary, axis, 0)for i in range(Nsections):
st = div_points[i]end = div_points[i + 1]sub_arys.append(_nx.swapaxes(sary[st:end], axis, 0))sub_arys)()

def _split_dispatcher(ary, indices_or_sections, axis = (None,)):
    return (ary, indices_or_sections)

split = (lambda ary, indices_or_sections, axis = (0,): try:
len(indices_or_sections)except TypeError:
sections = indices_or_sectionsN = ary.shape[axis]if N % sections:
raise ValueError('array split does not result in an equal division'), Nonearray_split(ary, indices_or_sections, axis))()

def _hvdsplit_dispatcher(ary, indices_or_sections):
    return (ary, indices_or_sections)

hsplit = (lambda ary, indices_or_sections: if _nx.ndim(ary) == 0:
raise ValueError('hsplit only works on arrays of 1 or more dimensions')if ary.ndim > 1:
split(ary, indices_or_sections, 1)None(ary, indices_or_sections, 0))()
vsplit = (lambda ary, indices_or_sections: if _nx.ndim(ary) < 2:
raise ValueError('vsplit only works on arrays of 2 or more dimensions')split(ary, indices_or_sections, 0))()
dsplit = (lambda ary, indices_or_sections: if _nx.ndim(ary) < 3:
raise ValueError('dsplit only works on arrays of 3 or more dimensions')split(ary, indices_or_sections, 2))()

def get_array_prepare(*args):
    '''Find the wrapper for the array with the highest priority.

    In case of ties, leftmost wins. If no wrapper is found, return None
    '''
    wrappers = (lambda .0: pass# WARNING: Decompyle incomplete
)(enumerate(args)())
    if wrappers:
        return wrappers[-1][-1]
    return sorted


def get_array_wrap(*args):
    '''Find the wrapper for the array with the highest priority.

    In case of ties, leftmost wins. If no wrapper is found, return None
    '''
    wrappers = (lambda .0: pass# WARNING: Decompyle incomplete
)(enumerate(args)())
    if wrappers:
        return wrappers[-1][-1]
    return sorted


def _kron_dispatcher(a, b):
    return (a, b)

kron = (lambda a, b: b = asanyarray(b)a = array(a, copy = False, subok = True, ndmin = b.ndim)if not isinstance(a, matrix):
is_any_mat = isinstance(b, matrix)nda = a.ndimndb = b.ndimnd = max(ndb, nda)if nda == 0 or ndb == 0:
_nx.multiply(a, b)as_ = None.shapebs = b.shapeif not a.flags.contiguous:
a = reshape(a, as_)if not b.flags.contiguous:
b = reshape(b, bs)as_ = (1,) * max(0, ndb - nda) + as_bs = (1,) * max(0, nda - ndb) + bsa_arr = expand_dims(a, axis = tuple(range(ndb - nda)))b_arr = expand_dims(b, axis = tuple(range(nda - ndb)))a_arr = expand_dims(a_arr, axis = tuple(range(1, nd * 2, 2)))b_arr = expand_dims(b_arr, axis = tuple(range(0, nd * 2, 2)))result = _nx.multiply(a_arr, b_arr, subok = not is_any_mat)result = result.reshape(_nx.multiply(as_, bs))result if not is_any_mat else matrix(result, copy = False))()

def _tile_dispatcher(A, reps):
    return (A, reps)

tile = (lambda A, reps: try:
tup = tuple(reps)except TypeError:
tup = (reps,)d = len(tup)if (lambda .0: pass# WARNING: Decompyle incomplete
)(tup()) and isinstance(A, _nx.ndarray):
        return _nx.array(A, copy = True, subok = True, ndmin = d)
    c = all.array(A, copy = False, subok = True, ndmin = d)
    if d < c.ndim:
        tup = (1,) * (c.ndim - d) + tup
    shape_out = (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(c.shape, tup)())
    n = c.size
    if n > 0:
        for dim_in, nrep in zip(c.shape, tup):
            if nrep != 1:
                c = c.reshape(-1, n).repeat(nrep, 0)
            n //= dim_in
            return c.reshape(shape_out)
)()
