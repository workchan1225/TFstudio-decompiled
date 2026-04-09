# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: npdatetime.pyc (Python 3.11)

__doc__ = '\nImplementation of operations on numpy timedelta64.\n'
import numpy as np
import operator
import llvmlite.ir as llvmlite
from llvmlite.ir import Constant
from numba.core import types, cgutils
from numba.core.cgutils import create_constant_array
from numba.core.imputils import lower_builtin, lower_constant, impl_ret_untracked, lower_cast
from numba.np import npdatetime_helpers, numpy_support, npyfuncs
from numba.extending import overload_method
from numba.core.config import IS_32BITS
from numba.core.errors import LoweringError
DATETIME64 = llvmlite.ir.IntType(64)
TIMEDELTA64 = llvmlite.ir.IntType(64)
NAT = Constant(TIMEDELTA64, npdatetime_helpers.NAT)
TIMEDELTA_BINOP_SIG = (types.NPTimedelta,) * 2

def scale_by_constant(builder, val, factor):
    '''
    Multiply *val* by the constant *factor*.
    '''
    return builder.mul(val, Constant(TIMEDELTA64, factor))


def unscale_by_constant(builder, val, factor):
    '''
    Divide *val* by the constant *factor*.
    '''
    return builder.sdiv(val, Constant(TIMEDELTA64, factor))


def add_constant(builder, val, const):
    '''
    Add constant *const* to *val*.
    '''
    return builder.add(val, Constant(TIMEDELTA64, const))


def scale_timedelta(context, builder, val, srcty, destty):
    '''
    Scale the timedelta64 *val* from *srcty* to *destty*
    (both numba.types.NPTimedelta instances)
    '''
    factor = npdatetime_helpers.get_timedelta_conversion_factor(srcty.unit, destty.unit)
# WARNING: Decompyle incomplete


def normalize_timedeltas(context, builder, left, right, leftty, rightty):
    """
    Scale either *left* or *right* to the other's unit, in order to have
    homogeneous units.
    """
    factor = npdatetime_helpers.get_timedelta_conversion_factor(leftty.unit, rightty.unit)
# WARNING: Decompyle incomplete


def alloc_timedelta_result(builder, name = ('ret',)):
    '''
    Allocate a NaT-initialized datetime64 (or timedelta64) result slot.
    '''
    ret = cgutils.alloca_once(builder, TIMEDELTA64, name = name)
    builder.store(NAT, ret)
    return ret


def alloc_boolean_result(builder, name = ('ret',)):
    '''
    Allocate an uninitialized boolean result slot.
    '''
    ret = cgutils.alloca_once(builder, llvmlite.ir.IntType(1), name = name)
    return ret


def is_not_nat(builder, val):
    '''
    Return a predicate which is true if *val* is not NaT.
    '''
    return builder.icmp_unsigned('!=', val, NAT)


def are_not_nat(builder, vals):
    '''
    Return a predicate which is true if all of *vals* are not NaT.
    '''
    pass
# WARNING: Decompyle incomplete

normal_year_months = create_constant_array(TIMEDELTA64, [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31])
leap_year_months = create_constant_array(TIMEDELTA64, [
    31,
    29,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31])
normal_year_months_acc = create_constant_array(TIMEDELTA64, [
    0,
    31,
    59,
    90,
    120,
    151,
    181,
    212,
    243,
    273,
    304,
    334])
leap_year_months_acc = create_constant_array(TIMEDELTA64, [
    0,
    31,
    60,
    91,
    121,
    152,
    182,
    213,
    244,
    274,
    305,
    335])
datetime_constant = (lambda context, builder, ty, pyval: DATETIME64(pyval.astype(np.int64)))()()
timedelta_pos_impl = (lambda context, builder, sig, args: res = args[0]impl_ret_untracked(context, builder, sig.return_type, res))()
timedelta_neg_impl = (lambda context, builder, sig, args: res = builder.neg(args[0])impl_ret_untracked(context, builder, sig.return_type, res))()
timedelta_abs_impl = (lambda context, builder, sig, args:
