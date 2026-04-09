# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ndarray.pyc (Python 3.11)

'''
This file provides internal compiler utilities that support certain special
operations with numpy.
'''
from numba.core import types, typing
from numba.core.cgutils import unpack_tuple
from numba.core.extending import intrinsic
from numba.core.imputils import impl_ret_new_ref
from numba.core.errors import RequireLiteralValue, TypingError
from numba.cpython.unsafe.tuple import tuple_setitem
empty_inferred = (lambda typingctx, shape: pass# WARNING: Decompyle incomplete
)()
to_fixed_tuple = (lambda typingctx, array, length: pass# WARNING: Decompyle incomplete
)()
