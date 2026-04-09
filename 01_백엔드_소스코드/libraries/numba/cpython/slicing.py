# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: slicing.pyc (Python 3.11)

'''
Implement slices and various slice computations.
'''
from itertools import zip_longest
from llvmlite import ir
from numba.core import cgutils, types, typing, utils
from numba.core.imputils import impl_ret_borrowed, impl_ret_new_ref, impl_ret_untracked, iternext_impl, lower_builtin, lower_cast, lower_constant, lower_getattr

def fix_index(builder, idx, size):
    '''
    Fix negative index by adding *size* to it.  Positive
    indices are left untouched.
    '''
    is_negative = builder.icmp_signed('<', idx, ir.Constant(size.type, 0))
    wrapped_index = builder.add(idx, size)
    return builder.select(is_negative, wrapped_index, idx)


def fix_slice(builder, slice, size):
    '''
    Fix *slice* start and stop to be valid (inclusive and exclusive, resp)
    indexing bounds for a sequence of the given *size*.
    '''
    pass
# WARNING: Decompyle incomplete


def get_slice_length(builder, slicestruct):
    '''
    Given a slice, compute the number of indices it spans, i.e. the
    number of iterations that for_range_slice() will execute.

    Pseudo-code:
        assert step != 0
        if step > 0:
            if stop <= start:
                return 0
            else:
                return (stop - start - 1) // step + 1
        else:
            if stop >= start:
                return 0
            else:
                return (stop - start + 1) // step + 1

    (see PySlice_GetIndicesEx() in CPython)
    '''
    start = slicestruct.start
    stop = slicestruct.stop
    step = slicestruct.step
    one = ir.Constant(start.type, 1)
    zero = ir.Constant(start.type, 0)
    is_step_negative = cgutils.is_neg_int(builder, step)
    delta = builder.sub(stop, start)
    pos_dividend = builder.sub(delta, one)
    neg_dividend = builder.add(delta, one)
    dividend = builder.select(is_step_negative, neg_dividend, pos_dividend)
    nominal_length = builder.add(one, builder.sdiv(dividend, step))
    is_zero_length = builder.select(is_step_negative, builder.icmp_signed('>=', delta, zero), builder.icmp_signed('<=', delta, zero))
    return builder.select(is_zero_length, zero, nominal_length)


def get_slice_bounds(builder, slicestruct):
    '''
    Return the [lower, upper) indexing bounds of a slice.
    '''
    start = slicestruct.start
    stop = slicestruct.stop
    zero = start.type(0)
    one = start.type(1)
    is_step_negative = builder.icmp_signed('<', slicestruct.step, zero)
    lower = builder.select(is_step_negative, builder.add(stop, one), start)
    upper = builder.select(is_step_negative, builder.add(start, one), stop)
    return (lower, upper)


def fix_stride(builder, slice, stride):
    """
    Fix the given stride for the slice's step.
    """
    return builder.mul(slice.step, stride)


def guard_invalid_slice(context, builder, typ, slicestruct):
    '''
    Guard against *slicestruct* having a zero step (and raise ValueError).
    '''
    if typ.has_step:
        cgutils.guard_null(context, builder, slicestruct.step, (ValueError, 'slice step cannot be zero'))
        return None


def get_defaults(context):
    """
    Get the default values for a slice's members:
    (start for positive step, start for negative step,
     stop for positive step, stop for negative step, step)
    """
    maxint = (1 << context.address_size - 1) - 1
    return (0, maxint, maxint, -maxint - 1, 1)

slice_constructor_impl = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()
slice_start_impl = (lambda context, builder, typ, value: sli = context.make_helper(builder, typ, value)sli.start)()
slice_stop_impl = (lambda context, builder, typ, value: sli = context.make_helper(builder, typ, value)sli.stop)()
slice_step_impl = (lambda context, builder, typ, value: if typ.has_step:
sli = context.make_helper(builder, typ, value)sli.stepNone.get_constant(types.intp, 1))()
slice_indices = (lambda context, builder, sig, args:
