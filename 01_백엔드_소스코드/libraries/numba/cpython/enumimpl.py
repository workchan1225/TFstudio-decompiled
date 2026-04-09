# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: enumimpl.pyc (Python 3.11)

'''
Implementation of enums.
'''
import operator
from numba.core.imputils import lower_builtin, lower_getattr, lower_getattr_generic, lower_cast, lower_constant, impl_ret_untracked
from numba.core import types
from numba.core.extending import overload_method
enum_eq = (lambda context, builder, sig, args: (tu, tv) = sig.args(u, v) = argsres = context.generic_compare(builder, operator.eq, (tu.dtype, tv.dtype), (u, v))impl_ret_untracked(context, builder, sig.return_type, res))()
enum_is = (lambda context, builder, sig, args: (tu, tv) = sig.args(u, v) = argsif tu == tv:
res = context.generic_compare(builder, operator.eq, (tu.dtype, tv.dtype), (u, v))else:
res = context.get_constant(sig.return_type, False)impl_ret_untracked(context, builder, sig.return_type, res))()
enum_ne = (lambda context, builder, sig, args: (tu, tv) = sig.args(u, v) = argsres = context.generic_compare(builder, operator.ne, (tu.dtype, tv.dtype), (u, v))impl_ret_untracked(context, builder, sig.return_type, res))()
enum_value = (lambda context, builder, ty, val: val)()
int_enum_to_int = (lambda context, builder, fromty, toty, val: context.cast(builder, val, fromty.dtype, toty))()
enum_constant = (lambda context, builder, ty, pyval: context.get_constant_generic(builder, ty.dtype, pyval.value))()
enum_class_getattr = (lambda context, builder, ty, val, attr: member = getattr(ty.instance_class, attr)context.get_constant_generic(builder, ty.dtype, member.value))()
enum_class_getitem = (lambda context, builder, sig, args: (enum_cls_typ, idx) = sig.argsmember = enum_cls_typ.instance_class[idx.literal_value]context.get_constant_generic(builder, enum_cls_typ.dtype, member.value))()
intenum_hash = (lambda val: 
def hash_impl(val):
hash(val.value)hash_impl)()
