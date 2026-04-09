# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scimath.pyc (Python 3.11)

'''
Wrapper functions to more user-friendly calling of certain math functions
whose output data-type is different than the input data-type in certain
domains of the input.

For example, for functions like `log` with branch cuts, the versions in this
module provide the mathematically valid answers in the complex plane::

  >>> import math
  >>> np.emath.log(-math.exp(1)) == (1+1j*math.pi)
  True

Similarly, `sqrt`, other base logarithms, `power` and trig functions are
correctly handled.  See their respective docstrings for specific examples.

Functions
---------

.. autosummary::
   :toctree: generated/

   sqrt
   log
   log2
   logn
   log10
   power
   arccos
   arcsin
   arctanh

'''

numeric

numerictypes
from numpy.core.numeric import asarray, any
any = any
import numpy.core.numerictypes, core
from numpy.core.overrides import array_function_dispatch
from numpy.lib.type_check import isreal
__all__ = [
    'sqrt',
    'log',
    'log2',
    'logn',
    'log10',
    'power',
    'arccos',
    'arcsin',
    'arctanh']
_ln2 = nx.log(2)

def _tocomplex(arr):
    """Convert its input `arr` to a complex array.

    The input is returned as a complex array of the smallest type that will fit
    the original data: types like single, byte, short, etc. become csingle,
    while others become cdouble.

    A copy of the input is always made.

    Parameters
    ----------
    arr : array

    Returns
    -------
    array
        An array with the same input data as the input but in complex form.

    Examples
    --------

    First, consider an input of type short:

    >>> a = np.array([1,2,3],np.short)

    >>> ac = np.lib.scimath._tocomplex(a); ac
    array([1.+0.j, 2.+0.j, 3.+0.j], dtype=complex64)

    >>> ac.dtype
    dtype('complex64')

    If the input is of type double, the output is correspondingly of the
    complex double type as well:

    >>> b = np.array([1,2,3],np.double)

    >>> bc = np.lib.scimath._tocomplex(b); bc
    array([1.+0.j, 2.+0.j, 3.+0.j])

    >>> bc.dtype
    dtype('complex128')

    Note that even if the input was complex to begin with, a copy is still
    made, since the astype() method always copies:

    >>> c = np.array([1,2,3],np.csingle)

    >>> cc = np.lib.scimath._tocomplex(c); cc
    array([1.+0.j,  2.+0.j,  3.+0.j], dtype=complex64)

    >>> c *= 2; c
    array([2.+0.j,  4.+0.j,  6.+0.j], dtype=complex64)

    >>> cc
    array([1.+0.j,  2.+0.j,  3.+0.j], dtype=complex64)
    """
    if issubclass(arr.dtype.type, (nt.single, nt.byte, nt.short, nt.ubyte, nt.ushort, nt.csingle)):
        return arr.astype(nt.csingle)
    return None.astype(nt.cdouble)


def _fix_real_lt_zero(x):
    '''Convert `x` to complex if it has real, negative components.

    Otherwise, output is just the array version of the input (via asarray).

    Parameters
    ----------
    x : array_like

    Returns
    -------
    array

    Examples
    --------
    >>> np.lib.scimath._fix_real_lt_zero([1,2])
    array([1, 2])

    >>> np.lib.scimath._fix_real_lt_zero([-1,2])
    array([-1.+0.j,  2.+0.j])

    '''
    x = asarray(x)
    if any(isreal(x) & (x < 0)):
        x = _tocomplex(x)
    return x


def _fix_int_lt_zero(x):
    '''Convert `x` to double if it has real, negative components.

    Otherwise, output is just the array version of the input (via asarray).

    Parameters
    ----------
    x : array_like

    Returns
    -------
    array

    Examples
    --------
    >>> np.lib.scimath._fix_int_lt_zero([1,2])
    array([1, 2])

    >>> np.lib.scimath._fix_int_lt_zero([-1,2])
    array([-1.,  2.])
    '''
    x = asarray(x)
    if any(isreal(x) & (x < 0)):
        x = x * 1
    return x


def _fix_real_abs_gt_1(x):
    '''Convert `x` to complex if it has real components x_i with abs(x_i)>1.

    Otherwise, output is just the array version of the input (via asarray).

    Parameters
    ----------
    x : array_like

    Returns
    -------
    array

    Examples
    --------
    >>> np.lib.scimath._fix_real_abs_gt_1([0,1])
    array([0, 1])

    >>> np.lib.scimath._fix_real_abs_gt_1([0,2])
    array([0.+0.j, 2.+0.j])
    '''
    x = asarray(x)
    if any(isreal(x) & (abs(x) > 1)):
        x = _tocomplex(x)
    return x


def _unary_dispatcher(x):
    return (x,)

sqrt = (lambda x: x = _fix_real_lt_zero(x)nx.sqrt(x))()
log = (lambda x: x = _fix_real_lt_zero(x)nx.log(x))()
log10 = (lambda x: x = _fix_real_lt_zero(x)nx.log10(x))()

def _logn_dispatcher(n, x):
    return (n, x)

logn = (lambda n, x: x = _fix_real_lt_zero(x)n = _fix_real_lt_zero(n)nx.log(x) / nx.log(n))()
log2 = (lambda x: x = _fix_real_lt_zero(x)nx.log2(x))()

def _power_dispatcher(x, p):
    return (x, p)

power = (lambda x, p: x = _fix_real_lt_zero(x)p = _fix_int_lt_zero(p)nx.power(x, p))()
arccos = (lambda x: x = _fix_real_abs_gt_1(x)nx.arccos(x))()
arcsin = (lambda x: x = _fix_real_abs_gt_1(x)nx.arcsin(x))()
arctanh = (lambda x: x = _fix_real_abs_gt_1(x)nx.arctanh(x))()
