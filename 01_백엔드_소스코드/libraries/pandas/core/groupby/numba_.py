# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numba_.pyc (Python 3.11)

'''Common utilities for Numba operations with groupby ops'''
from __future__ import annotations
import functools
import inspect
from typing import TYPE_CHECKING, Any
import numpy as np
from pandas.compat._optional import import_optional_dependency
from pandas.core.util.numba_ import NumbaUtilError, jit_user_function
if TYPE_CHECKING:
    from collections.abc import Callable
    from pandas._typing import Scalar

def validate_udf(func = None):
    '''
    Validate user defined function for ops when using Numba with groupby ops.

    The first signature arguments should include:

    def f(values, index, ...):
        ...

    Parameters
    ----------
    func : function, default False
        user defined function

    Returns
    -------
    None

    Raises
    ------
    NumbaUtilError
    '''
    if not callable(func):
        raise NotImplementedError('Numba engine can only be used with a single function.')
    udf_signature = list(inspect.signature(func).parameters.keys())
    expected_args = [
        'values',
        'index']
    min_number_args = len(expected_args)
    if len(udf_signature) < min_number_args or udf_signature[:min_number_args] != expected_args:
        raise NumbaUtilError(f'''The first {min_number_args} arguments to {func.__name__} must be {expected_args}''')

generate_numba_agg_func = (lambda func = None, nopython = None, nogil = functools.cache, parallel = ('func', 'Callable[..., Scalar]', 'nopython', 'bool', 'nogil', 'bool', 'parallel', 'bool', 'return', 'Callable[[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int, Any], np.ndarray]'): pass# WARNING: Decompyle incomplete
)()
generate_numba_transform_func = (lambda func = None, nopython = None, nogil = functools.cache, parallel = ('func', 'Callable[..., np.ndarray]', 'nopython', 'bool', 'nogil', 'bool', 'parallel', 'bool', 'return', 'Callable[[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int, Any], np.ndarray]'): pass# WARNING: Decompyle incomplete
)()
