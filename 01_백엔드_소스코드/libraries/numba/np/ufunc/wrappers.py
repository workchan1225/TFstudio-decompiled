# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wrappers.pyc (Python 3.11)

from collections import namedtuple
import numpy as np
from llvmlite.ir import Constant, IRBuilder
from llvmlite import ir
from numba.core import types, cgutils
from numba.core.compiler_lock import global_compiler_lock
from numba.core.caching import make_library_cache, NullCache
_wrapper_info = namedtuple('_wrapper_info', [
    'library',
    'env',
    'name'])

def _build_ufunc_loop_body(load, store, context, func, builder, arrays, out, offsets, store_offset, signature, pyapi, env):
