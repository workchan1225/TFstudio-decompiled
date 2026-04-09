# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from numba.np.ufunc.decorators import Vectorize, GUVectorize, vectorize, guvectorize
from numba.np.ufunc._internal import PyUFunc_None, PyUFunc_Zero, PyUFunc_One
from numba.np.ufunc import _internal, array_exprs
from numba.np.ufunc.parallel import threading_layer, get_num_threads, set_num_threads, get_thread_id, set_parallel_chunksize, get_parallel_chunksize
if hasattr(_internal, 'PyUFunc_ReorderableNone'):
    PyUFunc_ReorderableNone = _internal.PyUFunc_ReorderableNone
del _internal
del array_exprs

def _init():
    
    def init_cuda_vectorize():
        CUDAVectorize = CUDAVectorize
        import numba.cuda.vectorizers
        return CUDAVectorize

    
    def init_cuda_guvectorize():
        CUDAGUFuncVectorize = CUDAGUFuncVectorize
        import numba.cuda.vectorizers
        return CUDAGUFuncVectorize

    Vectorize.target_registry.ondemand['cuda'] = init_cuda_vectorize
    GUVectorize.target_registry.ondemand['cuda'] = init_cuda_guvectorize

_init()
del _init
