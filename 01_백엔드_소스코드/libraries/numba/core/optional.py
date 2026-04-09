# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: optional.pyc (Python 3.11)

import operator
from numba.core import types, typing, cgutils
from numba.core.imputils import lower_cast, lower_builtin, lower_getattr_generic, impl_ret_untracked, lower_setattr_generic

def always_return_true_impl(context, builder, sig, args):
    return cgutils.true_bit


def always_return_false_impl(context, builder, sig, args):
    return cgutils.false_bit


def optional_is_none(context, builder, sig, args):
    '''
    Check if an Optional value is invalid
    '''
    (lty, rty) = sig.args
    (lval, rval) = args
    if lty == types.none:
        rty = lty
        lty = rty
        rval = lval
        lval = rval
    opt_type = lty
    opt_val = lval
    opt = context.make_helper(builder, opt_type, opt_val)
    res = builder.not_(cgutils.as_bool_bit(builder, opt.valid))
    return impl_ret_untracked(context, builder, sig.return_type, res)

lower_builtin(operator.is_, types.none, types.none)(always_return_true_impl)
lower_builtin(operator.is_, types.Optional, types.none)(optional_is_none)
lower_builtin(operator.is_, types.none, types.Optional)(optional_is_none)
optional_getattr = (lambda context, builder, typ, value, attr: inner_type = typ.typeval = context.cast(builder, value, typ, inner_type)imp = context.get_getattr(inner_type, attr)imp(context, builder, inner_type, val, attr))()
optional_setattr = (lambda context, builder, sig, args, attr: (basety, valty) = sig.args(target, val) = argstarget_type = basety.typetarget = context.cast(builder, target, basety, target_type)newsig = typing.signature(sig.return_type, target_type, valty)imp = context.get_setattr(attr, newsig)imp(builder, (target, val)))()
optional_to_optional = (lambda context, builder, fromty, toty, val:
