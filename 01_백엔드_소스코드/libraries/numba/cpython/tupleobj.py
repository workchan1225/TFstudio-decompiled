# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tupleobj.pyc (Python 3.11)

'''
Implementation of tuple objects
'''
import operator
from numba.core.imputils import lower_builtin, lower_getattr_generic, lower_cast, lower_constant, iternext_impl, impl_ret_borrowed, impl_ret_untracked, RefType
from numba.core import typing, types, cgutils
from numba.core.extending import overload_method, overload, intrinsic
namedtuple_constructor = (lambda context, builder, sig, args: newargs = []for i, arg in enumerate(args):
casted = context.cast(builder, arg, sig.args[i], sig.return_type[i])newargs.append(casted)res = context.make_tuple(builder, sig.return_type, tuple(newargs))impl_ret_borrowed(context, builder, sig.return_type, res))()
tuple_add = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()

def tuple_cmp_ordered(context, builder, op, sig, args):
    (tu, tv) = sig.args
    (u, v) = args
    res = cgutils.alloca_once_value(builder, cgutils.true_bit)
    bbend = builder.append_basic_block('cmp_end')
    for ta, tb in enumerate(zip(tu.types, tv.types)):
        a = builder.extract_value(u, i)
        b = builder.extract_value(v, i)
        not_equal = context.generic_compare(builder, operator.ne, (ta, tb), (a, b))
        builder.if_then(not_equal)
        pred = context.generic_compare(builder, op, (ta, tb), (a, b))
        builder.store(pred, res)
        builder.branch(bbend)
        None(None, None)
    with None:
        if not None:
            pass
    continue
    len_compare = op(len(tu.types), len(tv.types))
    pred = context.get_constant(types.boolean, len_compare)
    builder.store(pred, res)
    builder.branch(bbend)
    builder.position_at_end(bbend)
    return builder.load(res)

tuple_eq = (lambda context, builder, sig, args: (tu, tv) = sig.args(u, v) = argsif len(tu.types) != len(tv.types):
res = context.get_constant(types.boolean, False)impl_ret_untracked(context, builder, sig.return_type, res)res = None.get_constant(types.boolean, True)for ta, tb in enumerate(zip(tu.types, tv.types)):
a = builder.extract_value(u, i)b = builder.extract_value(v, i)pred = context.generic_compare(builder, operator.eq, (ta, tb), (a, b))res = builder.and_(res, pred)impl_ret_untracked(context, builder, sig.return_type, res))()
tuple_ne = (lambda context, builder, sig, args: res = builder.not_(tuple_eq(context, builder, sig, args))impl_ret_untracked(context, builder, sig.return_type, res))()
tuple_lt = (lambda context, builder, sig, args: res = tuple_cmp_ordered(context, builder, operator.lt, sig, args)impl_ret_untracked(context, builder, sig.return_type, res))()
tuple_le = (lambda context, builder, sig, args: res = tuple_cmp_ordered(context, builder, operator.le, sig, args)impl_ret_untracked(context, builder, sig.return_type, res))()
tuple_gt = (lambda context, builder, sig, args: res = tuple_cmp_ordered(context, builder, operator.gt, sig, args)impl_ret_untracked(context, builder, sig.return_type, res))()
tuple_ge = (lambda context, builder, sig, args: res = tuple_cmp_ordered(context, builder, operator.ge, sig, args)impl_ret_untracked(context, builder, sig.return_type, res))()
namedtuple_getattr = (lambda context, builder, typ, value, attr: index = typ.fields.index(attr)res = builder.extract_value(value, index)impl_ret_borrowed(context, builder, typ[index], res))()
unituple_constant = (lambda context, builder, ty, pyval: pass# WARNING: Decompyle incomplete
)()()
unituple_constant = (lambda context, builder, ty, pyval: pass# WARNING: Decompyle incomplete
)()()
getiter_unituple = (lambda context, builder, sig, args: (tupty,) = sig.args(tup,) = argsiterval = context.make_helper(builder, types.UniTupleIter(tupty))index0 = context.get_constant(types.intp, 0)indexptr = cgutils.alloca_once(builder, index0.type)builder.store(index0, indexptr)iterval.index = indexptriterval.tuple = tupres = iterval._getvalue()impl_ret_borrowed(context, builder, sig.return_type, res))()()
iternext_unituple = (lambda context, builder, sig, args, result: (tupiterty,) = sig.args(tupiter,) = argsiterval = context.make_helper(builder, tupiterty, value = tupiter)tup = iterval.tupleidxptr = iterval.indexidx = builder.load(idxptr)count = context.get_constant(types.intp, tupiterty.container.count)is_valid = builder.icmp_signed('<', idx, count)result.set_valid(is_valid)builder.if_then(is_valid)getitem_sig = typing.signature(tupiterty.container.dtype, tupiterty.container, types.intp)getitem_out = getitem_unituple(context, builder, getitem_sig, [
tup,
idx])if context.enable_nrt:
context.nrt.decref(builder, tupiterty.container.dtype, getitem_out)result.yield_(getitem_out)nidx = builder.add(idx, context.get_constant(types.intp, 1))builder.store(nidx, iterval.index)None(None, None)Nonewith None:
if not None:
pass)()()
getitem_literal_idx = (lambda tup, idx: pass# WARNING: Decompyle incomplete
)()
getitem_typed = (lambda context, builder, sig, args:
