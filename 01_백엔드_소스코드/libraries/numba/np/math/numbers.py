# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numbers.pyc (Python 3.11)

import math
import numbers
import numpy as np
from llvmlite import ir
from llvmlite.ir import Constant
from numba.core.imputils import impl_ret_untracked
from numba.core import typing, types, errors, cgutils
from numba.cpython.unsafe.numbers import viewer

def _int_arith_flags(rettype):
    '''
    Return the modifier flags for integer arithmetic.
    '''
    if rettype.signed:
        return [
            'nsw']


def int_add_impl(context, builder, sig, args):
    (va, vb) = args
    (ta, tb) = sig.args
    a = context.cast(builder, va, ta, sig.return_type)
    b = context.cast(builder, vb, tb, sig.return_type)
    res = builder.add(a, b, flags = _int_arith_flags(sig.return_type))
    return impl_ret_untracked(context, builder, sig.return_type, res)


def int_sub_impl(context, builder, sig, args):
    (va, vb) = args
    (ta, tb) = sig.args
    a = context.cast(builder, va, ta, sig.return_type)
    b = context.cast(builder, vb, tb, sig.return_type)
    res = builder.sub(a, b, flags = _int_arith_flags(sig.return_type))
    return impl_ret_untracked(context, builder, sig.return_type, res)


def int_mul_impl(context, builder, sig, args):
    (va, vb) = args
    (ta, tb) = sig.args
    a = context.cast(builder, va, ta, sig.return_type)
    b = context.cast(builder, vb, tb, sig.return_type)
    res = builder.mul(a, b, flags = _int_arith_flags(sig.return_type))
    return impl_ret_untracked(context, builder, sig.return_type, res)


def int_divmod_signed(context, builder, ty, x, y):
    """
    Reference Objects/intobject.c
    xdivy = x / y;
    xmody = (long)(x - (unsigned long)xdivy * y);
    /* If the signs of x and y differ, and the remainder is non-0,
     * C89 doesn't define whether xdivy is now the floor or the
     * ceiling of the infinitely precise quotient.  We want the floor,
     * and we have it iff the remainder's sign matches y's.
     */
    if (xmody && ((y ^ xmody) < 0) /* i.e. and signs differ */) {
        xmody += y;
        --xdivy;
        assert(xmody && ((y ^ xmody) >= 0));
    }
    *p_xdivy = xdivy;
    *p_xmody = xmody;
    """
    pass
# WARNING: Decompyle incomplete


def int_divmod(context, builder, ty, x, y):
    '''
    Integer divmod(x, y).  The caller must ensure that y != 0.
    '''
    if ty.signed:
        return int_divmod_signed(context, builder, ty, x, y)
    return (None.udiv(x, y), builder.urem(x, y))


def _int_divmod_impl(context, builder, sig, args, zerodiv_message):
