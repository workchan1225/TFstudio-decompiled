# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: executor.pyc (Python 3.11)

from __future__ import annotations
import functools
from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from collections.abc import Callable
    from pandas._typing import Scalar
import numpy as np
from pandas.compat._optional import import_optional_dependency
from pandas.core.util.numba_ import jit_user_function
generate_apply_looper = (lambda func, nopython, nogil, parallel = (True, True, False): pass# WARNING: Decompyle incomplete
)()
make_looper = (lambda func, result_dtype, is_grouped_kernel, nopython, nogil, parallel: pass# WARNING: Decompyle incomplete
)()
default_dtype_mapping: 'dict[np.dtype, Any]' = {
    np.dtype('complex128'): np.complex128,
    np.dtype('complex64'): np.complex128,
    np.dtype('float64'): np.float64,
    np.dtype('float32'): np.float64,
    np.dtype('uint64'): np.uint64,
    np.dtype('uint32'): np.uint64,
    np.dtype('uint16'): np.uint64,
    np.dtype('uint8'): np.uint64,
    np.dtype('int64'): np.int64,
    np.dtype('int32'): np.int64,
    np.dtype('int16'): np.int64,
    np.dtype('int8'): np.int64 }
float_dtype_mapping: 'dict[np.dtype, Any]' = {
    np.dtype('complex128'): np.float64,
    np.dtype('complex64'): np.float64,
    np.dtype('float64'): np.float64,
    np.dtype('float32'): np.float64,
    np.dtype('uint64'): np.float64,
    np.dtype('uint32'): np.float64,
    np.dtype('uint16'): np.float64,
    np.dtype('uint8'): np.float64,
    np.dtype('int64'): np.float64,
    np.dtype('int32'): np.float64,
    np.dtype('int16'): np.float64,
    np.dtype('int8'): np.float64 }
identity_dtype_mapping: 'dict[np.dtype, Any]' = {
    np.dtype('complex128'): np.complex128,
    np.dtype('complex64'): np.complex64,
    np.dtype('float64'): np.float64,
    np.dtype('float32'): np.float32,
    np.dtype('uint64'): np.uint64,
    np.dtype('uint32'): np.uint32,
    np.dtype('uint16'): np.uint16,
    np.dtype('uint8'): np.uint8,
    np.dtype('int64'): np.int64,
    np.dtype('int32'): np.int32,
    np.dtype('int16'): np.int16,
    np.dtype('int8'): np.int8 }

def generate_shared_aggregator(func, dtype_mapping, is_grouped_kernel = None, nopython = functools.cache, nogil = functools.cache, parallel = ('func', 'Callable[..., Scalar]', 'dtype_mapping', 'dict[np.dtype, np.dtype]', 'is_grouped_kernel', 'bool', 'nopython', 'bool', 'nogil', 'bool', 'parallel', 'bool')):
    '''
    Generate a Numba function that loops over the columns 2D object and applies
    a 1D numba kernel over each column.

    Parameters
    ----------
    func : function
        aggregation function to be applied to each column
    dtype_mapping: dict or None
        If not None, maps a dtype to a result dtype.
        Otherwise, will fall back to default mapping.
    is_grouped_kernel: bool, default False
        Whether func operates using the group labels (True)
        or using starts/ends arrays

        If true, you also need to pass the number of groups to this function
    nopython : bool
        nopython to be passed into numba.jit
    nogil : bool
        nogil to be passed into numba.jit
    parallel : bool
        parallel to be passed into numba.jit

    Returns
    -------
    Numba function
    '''
    pass
# WARNING: Decompyle incomplete
