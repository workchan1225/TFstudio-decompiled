# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: charseq.pyc (Python 3.11)

__doc__ = 'Implements operations on bytes and str (unicode) array items.'
import operator
import numpy as np
from llvmlite import ir
from numba.core import types, cgutils, config
from numba.core.extending import overload, intrinsic, overload_method, lower_cast, register_jitable
from numba.core.cgutils import is_nonelike
from numba.cpython import unicode
s1_dtype = np.dtype('S1')
# WARNING: Decompyle incomplete
