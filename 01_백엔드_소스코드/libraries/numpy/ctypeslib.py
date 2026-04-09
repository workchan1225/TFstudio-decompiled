# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ctypeslib.pyc (Python 3.11)

__doc__ = '\n============================\n``ctypes`` Utility Functions\n============================\n\nSee Also\n--------\nload_library : Load a C library.\nndpointer : Array restype/argtype with verification.\nas_ctypes : Create a ctypes array from an ndarray.\nas_array : Create an ndarray from a ctypes array.\n\nReferences\n----------\n.. [1] "SciPy Cookbook: ctypes", https://scipy-cookbook.readthedocs.io/items/Ctypes.html\n\nExamples\n--------\nLoad the C library:\n\n>>> _lib = np.ctypeslib.load_library(\'libmystuff\', \'.\')     #doctest: +SKIP\n\nOur result type, an ndarray that must be of type double, be 1-dimensional\nand is C-contiguous in memory:\n\n>>> array_1d_double = np.ctypeslib.ndpointer(\n...                          dtype=np.double,\n...                          ndim=1, flags=\'CONTIGUOUS\')    #doctest: +SKIP\n\nOur C-function typically takes an array and updates its values\nin-place.  For example::\n\n    void foo_func(double* x, int length)\n    {\n        int i;\n        for (i = 0; i < length; i++) {\n            x[i] = i*i;\n        }\n    }\n\nWe wrap it using:\n\n>>> _lib.foo_func.restype = None                      #doctest: +SKIP\n>>> _lib.foo_func.argtypes = [array_1d_double, c_int] #doctest: +SKIP\n\nThen, we\'re ready to call ``foo_func``:\n\n>>> out = np.empty(15, dtype=np.double)\n>>> _lib.foo_func(out, len(out))                #doctest: +SKIP\n\n'
__all__ = [
    'load_library',
    'ndpointer',
    'c_intp',
    'as_ctypes',
    'as_array',
    'as_ctypes_type']
import os
from numpy import integer, ndarray, dtype as _dtype, asarray, frombuffer
from numpy.core.multiarray import _flagdict, flagsobj

try:
    import ctypes
except ImportError:
    ctypes = None

# WARNING: Decompyle incomplete
