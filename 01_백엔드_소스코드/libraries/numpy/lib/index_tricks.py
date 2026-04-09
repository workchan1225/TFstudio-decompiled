# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: index_tricks.pyc (Python 3.11)

import functools
import sys
import math
import warnings
import numpy as np
from _utils import set_module

numeric
from numpy.core.numeric import ScalarType, array
array = array
import numpy.core.numeric, core
from numpy.core.numerictypes import issubdtype
from numpy.matrixlib import matrixlib
from function_base import diff
from numpy.core.multiarray import ravel_multi_index, unravel_index
from numpy.core import overrides, linspace
from numpy.lib.stride_tricks import as_strided
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')
__all__ = [
    'ravel_multi_index',
    'unravel_index',
    'mgrid',
    'ogrid',
    'r_',
    'c_',
    's_',
    'index_exp',
    'ix_',
    'ndenumerate',
    'ndindex',
    'fill_diagonal',
    'diag_indices',
    'diag_indices_from']

def _ix__dispatcher(*args):
    return args

ix_ = (lambda : out = []nd = len(args)for k, new in enumerate(args):
if not isinstance(new, _nx.ndarray):
new = np.asarray(new)if new.size == 0:
new = new.astype(_nx.intp)if new.ndim != 1:
raise ValueError('Cross index must be 1 dimensional')if issubdtype(new.dtype, _nx.bool_):
(new,) = new.nonzero()new = new.reshape((1,) * k + (new.size,) + (1,) * (nd - k - 1))out.append(new)tuple(out))()

class nd_grid:
    '''
    Construct a multi-dimensional "meshgrid".

    ``grid = nd_grid()`` creates an instance which will return a mesh-grid
    when indexed.  The dimension and number of the output arrays are equal
    to the number of indexing dimensions.  If the step length is not a
    complex number, then the stop is not inclusive.

    However, if the step length is a **complex number** (e.g. 5j), then the
    integer part of its magnitude is interpreted as specifying the
    number of points to create between the start and stop values, where
    the stop value **is inclusive**.

    If instantiated with an argument of ``sparse=True``, the mesh-grid is
    open (or not fleshed out) so that only one-dimension of each returned
    argument is greater than 1.

    Parameters
    ----------
    sparse : bool, optional
        Whether the grid is sparse or not. Default is False.

    Notes
    -----
    Two instances of `nd_grid` are made available in the NumPy namespace,
    `mgrid` and `ogrid`, approximately defined as::

        mgrid = nd_grid(sparse=False)
        ogrid = nd_grid(sparse=True)

    Users should use these pre-defined instances instead of using `nd_grid`
    directly.
    '''
    
    def __init__(self, sparse = (False,)):
        self.sparse = sparse

    
    def __getitem__(self, key):
        pass
    # WARNING: Decompyle incomplete



class MGridClass(nd_grid):
    pass
# WARNING: Decompyle incomplete

mgrid = MGridClass()

class OGridClass(nd_grid):
    pass
# WARNING: Decompyle incomplete

ogrid = OGridClass()

class AxisConcatenator:
    '''
    Translates slice objects to concatenation along an axis.

    For detailed documentation on usage, see `r_`.
    '''
    concatenate = staticmethod(_nx.concatenate)
    makemat = staticmethod(matrixlib.matrix)
    
    def __init__(self, axis, matrix, ndmin, trans1d = (0, False, 1, -1)):
        self.axis = axis
        self.matrix = matrix
        self.trans1d = trans1d
        self.ndmin = ndmin

    
    def __getitem__(self, key):
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self):
        return 0



class RClass(AxisConcatenator):
    """
    Translates slice objects to concatenation along the first axis.

    This is a simple way to build up arrays quickly. There are two use cases.

    1. If the index expression contains comma separated arrays, then stack
       them along their first axis.
    2. If the index expression contains slice notation or scalars then create
       a 1-D array with a range indicated by the slice notation.

    If slice notation is used, the syntax ``start:stop:step`` is equivalent
    to ``np.arange(start, stop, step)`` inside of the brackets. However, if
    ``step`` is an imaginary number (i.e. 100j) then its integer portion is
    interpreted as a number-of-points desired and the start and stop are
    inclusive. In other words ``start:stop:stepj`` is interpreted as
    ``np.linspace(start, stop, step, endpoint=1)`` inside of the brackets.
    After expansion of slice notation, all comma separated sequences are
    concatenated together.

    Optional character strings placed as the first element of the index
    expression can be used to change the output. The strings 'r' or 'c' result
    in matrix output. If the result is 1-D and 'r' is specified a 1 x N (row)
    matrix is produced. If the result is 1-D and 'c' is specified, then a N x 1
    (column) matrix is produced. If the result is 2-D then both provide the
    same matrix result.

    A string integer specifies which axis to stack multiple comma separated
    arrays along. A string of two comma-separated integers allows indication
    of the minimum number of dimensions to force each entry into as the
    second integer (the axis to concatenate along is still the first integer).

    A string with three comma-separated integers allows specification of the
    axis to concatenate along, the minimum number of dimensions to force the
    entries to, and which axis should contain the start of the arrays which
    are less than the specified number of dimensions. In other words the third
    integer allows you to specify where the 1's should be placed in the shape
    of the arrays that have their shapes upgraded. By default, they are placed
    in the front of the shape tuple. The third argument allows you to specify
    where the start of the array should be instead. Thus, a third argument of
    '0' would place the 1's at the end of the array shape. Negative integers
    specify where in the new shape tuple the last dimension of upgraded arrays
    should be placed, so the default is '-1'.

    Parameters
    ----------
    Not a function, so takes no parameters


    Returns
    -------
    A concatenated ndarray or matrix.

    See Also
    --------
    concatenate : Join a sequence of arrays along an existing axis.
    c_ : Translates slice objects to concatenation along the second axis.

    Examples
    --------
    >>> np.r_[np.array([1,2,3]), 0, 0, np.array([4,5,6])]
    array([1, 2, 3, ..., 4, 5, 6])
    >>> np.r_[-1:1:6j, [0]*3, 5, 6]
    array([-1. , -0.6, -0.2,  0.2,  0.6,  1. ,  0. ,  0. ,  0. ,  5. ,  6. ])

    String integers specify the axis to concatenate along or the minimum
    number of dimensions to force entries into.

    >>> a = np.array([[0, 1, 2], [3, 4, 5]])
    >>> np.r_['-1', a, a] # concatenate along last axis
    array([[0, 1, 2, 0, 1, 2],
           [3, 4, 5, 3, 4, 5]])
    >>> np.r_['0,2', [1,2,3], [4,5,6]] # concatenate along first axis, dim>=2
    array([[1, 2, 3],
           [4, 5, 6]])

    >>> np.r_['0,2,0', [1,2,3], [4,5,6]]
    array([[1],
           [2],
           [3],
           [4],
           [5],
           [6]])
    >>> np.r_['1,2,0', [1,2,3], [4,5,6]]
    array([[1, 4],
           [2, 5],
           [3, 6]])

    Using 'r' or 'c' as a first string argument creates a matrix.

    >>> np.r_['r',[1,2,3], [4,5,6]]
    matrix([[1, 2, 3, 4, 5, 6]])

    """
    
    def __init__(self):
        AxisConcatenator.__init__(self, 0)


r_ = RClass()

class CClass(AxisConcatenator):
    """
    Translates slice objects to concatenation along the second axis.

    This is short-hand for ``np.r_['-1,2,0', index expression]``, which is
    useful because of its common occurrence. In particular, arrays will be
    stacked along their last axis after being upgraded to at least 2-D with
    1's post-pended to the shape (column vectors made out of 1-D arrays).

    See Also
    --------
    column_stack : Stack 1-D arrays as columns into a 2-D array.
    r_ : For more detailed documentation.

    Examples
    --------
    >>> np.c_[np.array([1,2,3]), np.array([4,5,6])]
    array([[1, 4],
           [2, 5],
           [3, 6]])
    >>> np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]
    array([[1, 2, 3, ..., 4, 5, 6]])

    """
    
    def __init__(self):
        AxisConcatenator.__init__(self, -1, ndmin = 2, trans1d = 0)


c_ = CClass()
ndenumerate = <NODE:12>()
ndindex = <NODE:12>()

class IndexExpression:
    """
    A nicer way to build up index tuples for arrays.

    .. note::
       Use one of the two predefined instances `index_exp` or `s_`
       rather than directly using `IndexExpression`.

    For any index combination, including slicing and axis insertion,
    ``a[indices]`` is the same as ``a[np.index_exp[indices]]`` for any
    array `a`. However, ``np.index_exp[indices]`` can be used anywhere
    in Python code and returns a tuple of slice objects that can be
    used in the construction of complex index expressions.

    Parameters
    ----------
    maketuple : bool
        If True, always returns a tuple.

    See Also
    --------
    index_exp : Predefined instance that always returns a tuple:
       `index_exp = IndexExpression(maketuple=True)`.
    s_ : Predefined instance without tuple conversion:
       `s_ = IndexExpression(maketuple=False)`.

    Notes
    -----
    You can do all this with `slice()` plus a few special objects,
    but there's a lot to remember and this version is simpler because
    it uses the standard array indexing syntax.

    Examples
    --------
    >>> np.s_[2::2]
    slice(2, None, 2)
    >>> np.index_exp[2::2]
    (slice(2, None, 2),)

    >>> np.array([0, 1, 2, 3, 4])[np.s_[2::2]]
    array([2, 4])

    """
    
    def __init__(self, maketuple):
        self.maketuple = maketuple

    
    def __getitem__(self, item):
        if not self.maketuple and isinstance(item, tuple):
            return (item,)


index_exp = IndexExpression(maketuple = True)
s_ = IndexExpression(maketuple = False)

def _fill_diagonal_dispatcher(a, val, wrap = (None,)):
    return (a,)

fill_diagonal = (lambda a, val, wrap = (False,): if a.ndim < 2:
raise ValueError('array must be at least 2-d')end = Noneif a.ndim == 2:
step = a.shape[1] + 1if not wrap:
end = a.shape[1] * a.shape[1]elif not np.all(diff(a.shape) == 0):
raise ValueError('All dimensions of input must be of equal length')step = 1 + np.cumprod(a.shape[:-1]).sum()a.flat[:end:step] = val)()
diag_indices = (lambda n, ndim = (2,): idx = np.arange(n)(idx,) * ndim)()

def _diag_indices_from(arr):
    return (arr,)

diag_indices_from = (lambda arr: if not arr.ndim >= 2:
raise ValueError('input array must be at least 2-d')if not np.all(diff(arr.shape) == 0):
raise ValueError('All dimensions of input must be of equal length')diag_indices(arr.shape[0], arr.ndim))()
