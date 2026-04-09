# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: overrides.pyc (Python 3.11)

'''Tools for testing implementations of __array_function__ and ufunc overrides


'''
from numpy.core.overrides import ARRAY_FUNCTIONS as _array_functions
from numpy import ufunc as _ufunc

umath
(lambda : ufuncs = _umath.__dict__.values()()ufuncs) = import numpy.core.umath, core

def allows_array_ufunc_override(func):
    '''Determine if a function can be overridden via `__array_ufunc__`

    Parameters
    ----------
    func : callable
        Function that may be overridable via `__array_ufunc__`

    Returns
    -------
    bool
        `True` if `func` is overridable via `__array_ufunc__` and
        `False` otherwise.

    Notes
    -----
    This function is equivalent to ``isinstance(func, np.ufunc)`` and
    will work correctly for ufuncs defined outside of Numpy.

    '''
    return isinstance(func, np.ufunc)


def get_overridable_numpy_array_functions():
    '''List all numpy functions overridable via `__array_function__`

    Parameters
    ----------
    None

    Returns
    -------
    set
        A set containing all functions in the public numpy API that are
        overridable via `__array_function__`.

    '''
    recfunctions = recfunctions
    import numpy.lib
    return _array_functions.copy()


def allows_array_function_override(func):
    '''Determine if a Numpy function can be overridden via `__array_function__`

    Parameters
    ----------
    func : callable
        Function that may be overridable via `__array_function__`

    Returns
    -------
    bool
        `True` if `func` is a function in the Numpy API that is
        overridable via `__array_function__` and `False` otherwise.
    '''
    return func in _array_functions
