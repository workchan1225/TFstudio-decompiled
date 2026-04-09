# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: function_base.pyc (Python 3.11)

import collections.abc as collections
import functools
import re
import sys
import warnings
from _utils import set_module
import numpy as np

numeric
from numpy.core import transpose
import numpy.core.numeric, core
from numpy.core.numeric import ones, zeros_like, arange, concatenate, array, asarray, asanyarray, empty, ndarray, take, dot, where, intp, integer, isscalar, absolute
from numpy.core.umath import pi, add, arctan2, frompyfunc, cos, less_equal, sqrt, sin, mod, exp, not_equal, subtract
from numpy.core.fromnumeric import ravel, nonzero, partition, mean, any, sum
from numpy.core.numerictypes import typecodes
from numpy.core import overrides
from numpy.core.function_base import add_newdoc
from numpy.lib.twodim_base import diag
from numpy.core.multiarray import _place, add_docstring, bincount, normalize_axis_index, _monotonicity, interp as compiled_interp, interp_complex as compiled_interp_complex
from numpy.core.umath import _add_newdoc_ufunc as add_newdoc_ufunc
import builtins
from numpy.lib.histograms import histogram, histogramdd
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')
__all__ = [
    'select',
    'piecewise',
    'trim_zeros',
    'copy',
    'iterable',
    'percentile',
    'diff',
    'gradient',
    'angle',
    'unwrap',
    'sort_complex',
    'disp',
    'flip',
    'rot90',
    'extract',
    'place',
    'vectorize',
    'asarray_chkfinite',
    'average',
    'bincount',
    'digitize',
    'cov',
    'corrcoef',
    'msort',
    'median',
    'sinc',
    'hamming',
    'hanning',
    'bartlett',
    'blackman',
    'kaiser',
    'trapz',
    'i0',
    'add_newdoc',
    'add_docstring',
    'meshgrid',
    'delete',
    'insert',
    'append',
    'interp',
    'add_newdoc_ufunc',
    'quantile']
_QuantileMethods = dict(inverted_cdf = dict(get_virtual_index = (lambda n, quantiles: _inverted_cdf(n, quantiles)), fix_gamma = (lambda gamma, _: gamma)), averaged_inverted_cdf = dict(get_virtual_index = (lambda n, quantiles: n * quantiles - 1), fix_gamma = (lambda gamma, _: _get_gamma_mask(shape = gamma.shape, default_value = 1, conditioned_value = 0.5, where = gamma == 0))), closest_observation = dict(get_virtual_index = (lambda n, quantiles: _closest_observation(n, quantiles)), fix_gamma = (lambda gamma, _: gamma)), interpolated_inverted_cdf = dict(get_virtual_index = (lambda n, quantiles: _compute_virtual_index(n, quantiles, 0, 1)), fix_gamma = (lambda gamma, _: gamma)), hazen = dict(get_virtual_index = (lambda n, quantiles: _compute_virtual_index(n, quantiles, 0.5, 0.5)), fix_gamma = (lambda gamma, _: gamma)), weibull = dict(get_virtual_index = (lambda n, quantiles: _compute_virtual_index(n, quantiles, 0, 0)), fix_gamma = (lambda gamma, _: gamma)), linear = dict(get_virtual_index = (lambda n, quantiles: (n - 1) * quantiles), fix_gamma = (lambda gamma, _: gamma)), median_unbiased = dict(get_virtual_index = (lambda n, quantiles: _compute_virtual_index(n, quantiles, 0.333333, 0.333333)), fix_gamma = (lambda gamma, _: gamma)), normal_unbiased = dict(get_virtual_index = (lambda n, quantiles: _compute_virtual_index(n, quantiles, 0.375, 0.375)), fix_gamma = (lambda gamma, _: gamma)), lower = dict(get_virtual_index = (lambda n, quantiles: np.floor((n - 1) * quantiles).astype(np.intp)), fix_gamma = (lambda gamma, _: gamma)), higher = dict(get_virtual_index = (lambda n, quantiles: np.ceil((n - 1) * quantiles).astype(np.intp)), fix_gamma = (lambda gamma, _: gamma)), midpoint = dict(get_virtual_index = (lambda n, quantiles: 0.5 * (np.floor((n - 1) * quantiles) + np.ceil((n - 1) * quantiles))), fix_gamma = (lambda gamma, index: _get_gamma_mask(shape = gamma.shape, default_value = 0.5, conditioned_value = 0, where = index % 1 == 0))), nearest = dict(get_virtual_index = (lambda n, quantiles: np.around((n - 1) * quantiles).astype(np.intp)), fix_gamma = (lambda gamma, _: gamma)))

def _rot90_dispatcher(m, k, axes = (None, None)):
    return (m,)

rot90 = (lambda m, k, axes = (1, (0, 1)): axes = tuple(axes)if len(axes) != 2:
raise ValueError('len(axes) must be 2.')m = asanyarray(m)if axes[0] == axes[1] or absolute(axes[0] - axes[1]) == m.ndim:
raise ValueError('Axes must be different.')if axes[0] >= m.ndim and axes[0] < -(m.ndim) and axes[1] >= m.ndim or axes[1] < -(m.ndim):
raise ValueError('Axes={} out of range for array of ndim={}.'.format(axes, m.ndim))k %= 4if k == 0:
m[:]if None == 2:
flip(flip(m, axes[0]), axes[1])axes_list = None(0, m.ndim)axes_list[axes[0]], axes_list[axes[1]] = axes_list[axes[1]], axes_list[axes[0]]if k == 1:
transpose(flip(m, axes[1]), axes_list)None(transpose(m, axes_list), axes[1]))()

def _flip_dispatcher(m, axis = (None,)):
    return (m,)

flip = (lambda m, axis = (None,): if not hasattr(m, 'ndim'):
m = asarray(m)# WARNING: Decompyle incomplete
)()
iterable = (lambda y: try:
iter(y)except TypeError:
FalseTrue)()

def _average_dispatcher(a, axis = set_module('numpy'), weights = (None, None, None), returned = {
    'keepdims': None }, *, keepdims):
    return (a, weights)

average = (lambda a, axis = array_function_dispatch(_average_dispatcher), weights = (None, None, False), returned = {
    'keepdims': np._NoValue }, *, keepdims, keepdims_kw = None, avg = None, avg_as_array = None: a = np.asanyarray(a)if keepdims is np._NoValue:
keepdims_kw = { }else:
keepdims_kw = {
'keepdims': keepdims }# WARNING: Decompyle incomplete
)()
asarray_chkfinite = (lambda a, dtype, order = (None, None): a = asarray(a, dtype = dtype, order = order)if not a.dtype.char in typecodes['AllFloat'] and np.isfinite(a).all():
raise ValueError('array must not contain infs or NaNs')a)()

def _piecewise_dispatcher(x, condlist, funclist, *args, **kw):
    pass
# WARNING: Decompyle incomplete

piecewise = (lambda x, condlist, funclist: x = asanyarray(x)n2 = len(funclist)if (isscalar(condlist) or isinstance(condlist[0], (list, ndarray))) and x.ndim != 0:
condlist = [
condlist]condlist = asarray(condlist, dtype = bool)n = len(condlist)if n == n2 - 1:
condelse = ~np.any(condlist, axis = 0, keepdims = True)condlist = np.concatenate([
condlist,
condelse], axis = 0)n += 1elif n != n2:
raise ValueError('with {} condition(s), either {} or {} functions are expected'.format(n, n, n + 1))y = zeros_like(x)# WARNING: Decompyle incomplete
)()

def _select_dispatcher(condlist, choicelist, default = (None,)):
    pass
# WARNING: Decompyle incomplete

select = (lambda condlist, choicelist, default = (0,): if len(condlist) != len(choicelist):
raise ValueError('list of cases must be same length as list of conditions')if len(condlist) == 0:
raise ValueError('select with an empty condition list is not possible')choicelist = choicelist()# WARNING: Decompyle incomplete
)()

def _copy_dispatcher(a, order, subok = (None, None)):
    return (a,)

copy = (lambda a, order, subok = ('K', False): array(a, order = order, subok = subok, copy = True))()

def _gradient_dispatcher(f = array_function_dispatch(_copy_dispatcher), *, axis, edge_order, *varargs):
    pass
# WARNING: Decompyle incomplete

gradient = (lambda f = array_function_dispatch(_gradient_dispatcher), *, axis: f = np.asanyarray(f)N = f.ndim# WARNING: Decompyle incomplete
)()

def _diff_dispatcher(a, n, axis, prepend, append = (None, None, None, None)):
    return (a, prepend, append)

diff = (lambda a, n, axis, prepend, append = (1, -1, np._NoValue, np._NoValue): if n == 0:
aif None < 0:
raise ValueError('order must be non-negative but got ' + repr(n))a = asanyarray(a)nd = a.ndimif nd == 0:
raise ValueError('diff requires input that is at least one dimensional')axis = normalize_axis_index(axis, nd)combined = []if prepend is not np._NoValue:
prepend = np.asanyarray(prepend)if prepend.ndim == 0:
shape = list(a.shape)shape[axis] = 1prepend = np.broadcast_to(prepend, tuple(shape))combined.append(prepend)combined.append(a)if append is not np._NoValue:
append = np.asanyarray(append)if append.ndim == 0:
shape = list(a.shape)shape[axis] = 1append = np.broadcast_to(append, tuple(shape))combined.append(append)if len(combined) > 1:
a = np.concatenate(combined, axis)slice1 = [
slice(None)] * ndslice2 = [
slice(None)] * ndslice1[axis] = slice(1, None)slice2[axis] = slice(None, -1)slice1 = tuple(slice1)slice2 = tuple(slice2)op = not_equal if a.dtype == np.bool_ else subtractfor _ in range(n):
a = op(a[slice1], a[slice2])a)()

def _interp_dispatcher(x, xp, fp, left, right, period = (None, None, None)):
    return (x, xp, fp)

interp = (lambda x, xp, fp, left, right, period = (None, None, None): fp = np.asarray(fp)if np.iscomplexobj(fp):
interp_func = compiled_interp_complexinput_dtype = np.complex128else:
interp_func = compiled_interpinput_dtype = np.float64# WARNING: Decompyle incomplete
)()

def _angle_dispatcher(z, deg = (None,)):
    return (z,)

angle = (lambda z, deg = (False,): z = asanyarray(z)if issubclass(z.dtype.type, _nx.complexfloating):
zimag = z.imagzreal = z.realelse:
zimag = 0zreal = za = arctan2(zimag, zreal)if deg:
a *= 180 / pia)()

def _unwrap_dispatcher(p = array_function_dispatch(_angle_dispatcher), discont = (None, None), axis = {
    'period': None }, *, period):
    return (p,)

unwrap = (lambda p = array_function_dispatch(_unwrap_dispatcher), discont = (None, -1), axis = {
    'period': 2 * pi }, *, period, nd = None, dd = None: p = asarray(p)nd = p.ndimdd = diff(p, axis = axis)# WARNING: Decompyle incomplete
)()

def _sort_complex(a):
    return (a,)

sort_complex = (lambda a: b = array(a, copy = True)b.sort()if not issubclass(b.dtype.type, _nx.complexfloating):
if b.dtype.char in 'bhBH':
b.astype('F')if None.dtype.char == 'g':
b.astype('G')None.astype('D'))()

def _trim_zeros(filt, trim = (None,)):
    return (filt,)

trim_zeros = (lambda filt, trim = ('fb',): first = 0trim = trim.upper()if 'F' in trim:
for i in filt:
if i != 0:
passelse:
first = first + 1last = len(filt)if 'B' in trim:
for i in filt[::-1]:
if i != 0:
passelse:
last = last - 1filt[first:last])()

def _extract_dispatcher(condition, arr):
    return (condition, arr)

extract = (lambda condition, arr: _nx.take(ravel(arr), nonzero(ravel(condition))[0]))()

def _place_dispatcher(arr, mask, vals):
    return (arr, mask, vals)

place = (lambda arr, mask, vals: _place(arr, mask, vals))()

def disp(mesg, device, linefeed = (None, True)):
    '''
    Display a message on a device.

    Parameters
    ----------
    mesg : str
        Message to display.
    device : object
        Device to write message. If None, defaults to ``sys.stdout`` which is
        very similar to ``print``. `device` needs to have ``write()`` and
        ``flush()`` methods.
    linefeed : bool, optional
        Option whether to print a line feed or not. Defaults to True.

    Raises
    ------
    AttributeError
        If `device` does not have a ``write()`` or ``flush()`` method.

    Examples
    --------
    Besides ``sys.stdout``, a file-like object can also be used as it has
    both required methods:

    >>> from io import StringIO
    >>> buf = StringIO()
    >>> np.disp(u\'"Display" in a file\', device=buf)
    >>> buf.getvalue()
    \'"Display" in a file\\n\'

    '''
    pass
# WARNING: Decompyle incomplete

_DIMENSION_NAME = '\\w+'
_CORE_DIMENSION_LIST = '(?:{0:}(?:,{0:})*)?'.format(_DIMENSION_NAME)
_ARGUMENT = '\\({}\\)'.format(_CORE_DIMENSION_LIST)
_ARGUMENT_LIST = '{0:}(?:,{0:})*'.format(_ARGUMENT)
_SIGNATURE = '^{0:}->{0:}$'.format(_ARGUMENT_LIST)

def _parse_gufunc_signature(signature):
    '''
    Parse string signatures for a generalized universal function.

    Arguments
    ---------
    signature : string
        Generalized universal function signature, e.g., ``(m,n),(n,p)->(m,p)``
        for ``np.matmul``.

    Returns
    -------
    Tuple of input and output core dimensions parsed from the signature, each
    of the form List[Tuple[str, ...]].
    '''
    signature = re.sub('\\s+', '', signature)
    if not re.match(_SIGNATURE, signature):
        raise ValueError('not a valid gufunc signature: {}'.format(signature))
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(signature.split('->')())


def _update_dim_sizes(dim_sizes, arg, core_dims):
    '''
    Incrementally check and update core dimension sizes for a single argument.

    Arguments
    ---------
    dim_sizes : Dict[str, int]
        Sizes of existing core dimensions. Will be updated in-place.
    arg : ndarray
        Argument to examine.
    core_dims : Tuple[str, ...]
        Core dimensions for this argument.
    '''
    if not core_dims:
        return None
    num_core_dims = None(core_dims)
    if arg.ndim < num_core_dims:
        raise ValueError('%d-dimensional argument does not have enough dimensions for all core dimensions %r' % (arg.ndim, core_dims))
    core_shape = arg.shape[-num_core_dims:]
    for dim, size in zip(core_dims, core_shape):
        if dim in dim_sizes:
            if size != dim_sizes[dim]:
                raise ValueError(f'''inconsistent size for core dimension {dim!r}: {size!r} vs {dim_sizes[dim]!r}''')
            continue
        dim_sizes[dim] = size
        return None


def _parse_input_dimensions(args, input_core_dims):
    '''
    Parse broadcast and core dimensions for vectorize with a signature.

    Arguments
    ---------
    args : Tuple[ndarray, ...]
        Tuple of input arguments to examine.
    input_core_dims : List[Tuple[str, ...]]
        List of core dimensions corresponding to each input.

    Returns
    -------
    broadcast_shape : Tuple[int, ...]
        Common shape to broadcast all non-core dimensions to.
    dim_sizes : Dict[str, int]
        Common sizes for named core dimensions.
    '''
    broadcast_args = []
    dim_sizes = { }
# WARNING: Decompyle incomplete


def _calculate_shapes(broadcast_shape, dim_sizes, list_of_core_dims):
    '''Helper for calculating broadcast shapes with core dimensions.'''
    pass
# WARNING: Decompyle incomplete


def _create_arrays(broadcast_shape, dim_sizes, list_of_core_dims, dtypes, results = (None,)):
    '''Helper for creating output arrays in vectorize.'''
    shapes = _calculate_shapes(broadcast_shape, dim_sizes, list_of_core_dims)
# WARNING: Decompyle incomplete

vectorize = <NODE:12>()

def _cov_dispatcher(m, y, rowvar, bias, ddof = set_module('numpy'), fweights = (None, None, None, None, None, None), aweights = {
    'dtype': None }, *, dtype):
    return (m, y, fweights, aweights)

cov = (lambda m, y, rowvar, bias, ddof = array_function_dispatch(_cov_dispatcher), fweights = (None, True, False, None, None, None), aweights = {
    'dtype': None }, *, dtype, X = None, w = None, avg = None, w_sum = None, fact = None, X_T = None: pass# WARNING: Decompyle incomplete
)()

def _corrcoef_dispatcher(x, y, rowvar = array_function_dispatch(_place_dispatcher), bias = (None, None, None, None), ddof = {
    'dtype': None }, *, dtype):
    return (x, y)

corrcoef = (lambda x, y, rowvar = array_function_dispatch(_corrcoef_dispatcher), bias = (None, True, np._NoValue, np._NoValue), ddof = {
    'dtype': None }, *, dtype, c = None, d = None, stddev = None,
