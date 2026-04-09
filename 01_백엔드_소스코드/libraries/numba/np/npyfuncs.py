# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: npyfuncs.pyc (Python 3.11)

"""Codegen for functions used as kernels in NumPy functions

Typically, the kernels of several ufuncs that can't map directly to
Python builtins
"""
import math
import llvmlite.ir as llvmlite
import numpy as np
from numba.core.extending import overload
from numba.core.imputils import impl_ret_untracked
from numba.core import typing, types, errors, lowering, cgutils, config
from numba.core.extending import register_jitable
from numba.np import npdatetime
from numba.np.math import cmathimpl, mathimpl, numbers
from numba.np.numpy_support import numpy_version
_NPY_LOG2E = 1.4427
_NPY_LOG10E = 0.434294
_NPY_LOGE2 = 0.693147

def _check_arity_and_homogeneity(sig, args, arity, return_type = (None,)):
    """checks that the following are true:
    - args and sig.args have arg_count elements
    - all input types are homogeneous
    - return type is 'return_type' if provided, otherwise it must be
      homogeneous with the input types.
    """
    pass
# WARNING: Decompyle incomplete

if config.USE_LEGACY_TYPE_SYSTEM:
    cast_arg_ty = types.float64
else:
    cast_arg_ty = types.np_float64

def _call_func_by_name_with_cast(context, builder, sig, args, func_name, ty = (cast_arg_ty,)):
    pass
# WARNING: Decompyle incomplete


def _dispatch_func_by_name_type(context, builder, sig, args, table, user_name):
    pass
# WARNING: Decompyle incomplete


def np_int_sdiv_impl(context, builder, sig, args):
