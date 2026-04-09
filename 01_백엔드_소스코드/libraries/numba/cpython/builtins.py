# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: builtins.pyc (Python 3.11)

from collections import namedtuple
import math
from functools import reduce
import numpy as np
import operator
import warnings
from llvmlite import ir
from numba.core.imputils import lower_builtin, lower_getattr, lower_getattr_generic, lower_cast, lower_constant, iternext_impl, call_getiter, call_iternext, impl_ret_borrowed, impl_ret_untracked, numba_typeref_ctor
from numba.core import typing, types, utils, cgutils
from numba.core.extending import overload, intrinsic
from numba.core.typeconv import Conversion
from numba.core.errors import TypingError, LoweringError, NumbaExperimentalFeatureWarning, NumbaTypeError, RequireLiteralValue, NumbaPerformanceWarning
from numba.core.typing.templates import AbstractTemplate, infer_global, signature
from numba.misc.special import literal_unroll
from numba.core.typing.asnumbatype import as_numba_type
ol_truth = (lambda val: if isinstance(val, types.Boolean):

def impl(val):
valimpl)()
generic_is_not = (lambda context, builder, sig, args: is_impl = context.get_function(operator.is_, sig)builder.not_(is_impl(builder, args)))()
generic_is = (lambda context, builder, sig, args: (lhs_type, rhs_type) = sig.argsif lhs_type == rhs_type:
if lhs_type.mutable:
msg = 'no default `is` implementation'raise LoweringError(msg)try:
eq_impl = context.get_function(operator.eq, sig)eq_impl(builder, args)except NotImplementedError:
cgutils.false_bit)()
opaque_is = (lambda context, builder, sig, args: (lhs_type, rhs_type) = sig.argsif lhs_type == rhs_type:
lhs_ptr = builder.ptrtoint(args[0], cgutils.intp_t)rhs_ptr = builder.ptrtoint(args[1], cgutils.intp_t)builder.icmp_unsigned('==', lhs_ptr, rhs_ptr)None.false_bit)()
bool_is_impl = (lambda context, builder, sig, args: (arg1, arg2) = args(arg1_type, arg2_type) = sig.args_arg1 = context.cast(builder, arg1, arg1_type, types.boolean)_arg2 = context.cast(builder, arg2, arg2_type, types.boolean)eq_impl = context.get_function(operator.eq, typing.signature(types.boolean, types.boolean, types.boolean))eq_impl(builder, (_arg1, _arg2)))()
const_eq_impl = (lambda context, builder, sig, args: (arg1, arg2) = sig.argsval = 0if arg1.literal_value == arg2.literal_value:
val = 1res = ir.Constant(ir.IntType(1), val)impl_ret_untracked(context, builder, sig.return_type, res))()()
const_ne_impl = (lambda context, builder, sig, args: (arg1, arg2) = sig.argsval = 0if arg1.literal_value != arg2.literal_value:
val = 1res = ir.Constant(ir.IntType(1), val)impl_ret_untracked(context, builder, sig.return_type, res))()()

def gen_non_eq(val):
    pass
# WARNING: Decompyle incomplete

overload(operator.eq)(gen_non_eq(True))
overload(operator.ne)(gen_non_eq(False))
deferred_getattr = (lambda context, builder, typ, value, attr: inner_type = typ.get()val = context.cast(builder, value, typ, inner_type)imp = context.get_getattr(inner_type, attr)imp(context, builder, inner_type, val, attr))()
any_to_deferred = (lambda context, builder, fromty, toty, val: actual = context.cast(builder, val, fromty, toty.get())model = context.data_model_manager[toty]model.set(builder, model.make_uninitialized(), actual))()()()
deferred_to_any = (lambda context, builder, fromty, toty, val: model = context.data_model_manager[fromty]val = model.get(builder, val)context.cast(builder, val, fromty.get(), toty))()()()
getitem_cpointer = (lambda context, builder, sig, args: (base_ptr, idx) = argselem_ptr = builder.gep(base_ptr, [
idx])res = builder.load(elem_ptr)impl_ret_borrowed(context, builder, sig.return_type, res))()
setitem_cpointer = (lambda context, builder, sig, args: (base_ptr, idx, val) = argselem_ptr = builder.gep(base_ptr, [
idx])builder.store(val, elem_ptr))()

def do_minmax(context, builder, argtys, args, cmpop):
    pass
# WARNING: Decompyle incomplete

max_iterable = (lambda context, builder, sig, args: argtys = list(sig.args[0])args = cgutils.unpack_tuple(builder, args[0])do_minmax(context, builder, argtys, args, operator.gt))()
max_vararg = (lambda context, builder, sig, args: do_minmax(context, builder, sig.args, args, operator.gt))()
min_iterable = (lambda context, builder, sig, args: argtys = list(sig.args[0])args = cgutils.unpack_tuple(builder, args[0])do_minmax(context, builder, argtys, args, operator.lt))()
min_vararg = (lambda context, builder, sig, args: do_minmax(context, builder, sig.args, args, operator.lt))()

def _round_intrinsic(tp):
    return 'llvm.rint.f%d' % (tp.bitwidth,)

round_impl_unary = (lambda context, builder, sig, args: fltty = sig.args[0]llty = context.get_value_type(fltty)module = builder.modulefnty = ir.FunctionType(llty, [
llty])fn = cgutils.get_or_insert_function(module, fnty, _round_intrinsic(fltty))res = builder.call(fn, args)res = builder.fptosi(res, context.get_value_type(sig.return_type))impl_ret_untracked(context, builder, sig.return_type, res))()
round_impl_binary = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()
int_impl = (lambda context, builder, sig, args: (ty,) = sig.args(val,) = argsres = context.cast(builder, val, ty, sig.return_type)impl_ret_untracked(context, builder, sig.return_type, res))()()
float_literal_impl = (lambda context, builder, sig, args: (ty,) = sig.argsres = context.get_constant(sig.return_type, float(ty.literal_value))impl_ret_untracked(context, builder, sig.return_type, res))()
complex_impl = (lambda context, builder, sig, args: complex_type = sig.return_typefloat_type = complex_type.underlying_floatif len(sig.args) == 1:
(argty,) = sig.args(arg,) = argsif isinstance(argty, types.Complex):
res = context.cast(builder, arg, argty, complex_type)impl_ret_untracked(context, builder, sig.return_type, res)real = None.cast(builder, arg, argty, float_type)imag = context.get_constant(float_type, 0)elif len(sig.args) == 2:
(realty, imagty) = sig.args(real, imag) = argsreal = context.cast(builder, real, realty, float_type)imag = context.cast(builder, imag, imagty, float_type)cmplx = context.make_complex(builder, complex_type)cmplx.real = realcmplx.imag = imagres = cmplx._getvalue()impl_ret_untracked(context, builder, sig.return_type, res))()
number_constructor = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()
constant_dummy = (lambda context, builder, ty, pyval: context.get_dummy_value())()
constant_function_pointer = (lambda context, builder, ty, pyval: ptrty = context.get_function_pointer_type(ty)ptrval = context.add_dynamic_addr(builder, ty.get_pointer(pyval), info = str(pyval))builder.bitcast(ptrval, ptrty))()
constant_optional = (lambda context, builder, ty, pyval: pass# WARNING: Decompyle incomplete
)()
type_impl = (lambda context, builder, sig, args: context.get_dummy_value())()
iter_impl = (lambda context, builder, sig, args: (ty,) = sig.args(val,) = argsiterval = call_getiter(context, builder, ty, val)iterval)()
next_impl = (lambda context, builder, sig, args: (iterty,) = sig.args(iterval,) = argsres = call_iternext(context, builder, iterty, iterval)builder.if_then(builder.not_(res.is_valid()), likely = False)context.call_conv.return_user_exc(builder, StopIteration, ())None(None, None))()
not_in = (lambda context, builder, sig, args: 
def in_impl(a, b):
operator.contains(b, a)res = context.compile_internal(builder, in_impl, sig, args)builder.not_(res))()
constsized_len = (lambda context, builder, sig, args: (ty,) = sig.argsretty = sig.return_typeres = context.get_constant(retty, len(ty.types))impl_ret_untracked(context, builder, sig.return_type, res))()
sized_bool = (lambda context, builder, sig, args: (ty,) = sig.argsif len(ty):
cgutils.true_bitNone.false_bit)()
lower_empty_tuple = (lambda context, builder, sig, args: retty = sig.return_typeres = context.get_constant_undef(retty)impl_ret_untracked(context, builder, sig.return_type, res))()
lower_tuple = (lambda context, builder, sig, args: (val,) = argsimpl_ret_borrowed(context, builder, sig.return_type, val))()
bool_sequence = (lambda x: valid_types = (types.CharSeq, types.UnicodeCharSeq, types.DictType, types.ListType, types.UnicodeType, types.Set)if isinstance(x, valid_types):

def bool_impl(x):
len(x) > 0bool_impl)()
bool_none = (lambda x: pass# WARNING: Decompyle incomplete
)()

def get_type_max_value(typ):
    if isinstance(typ, types.Float):
        return np.inf
    if None(typ, types.Integer):
        return typ.maxval
    raise None('Unsupported type')


def get_type_min_value(typ):
    if isinstance(typ, types.Float):
        return -(np.inf)
    if None(typ, types.Integer):
        return typ.minval
    raise None('Unsupported type')

MinValInfer = <NODE:12>()()
lower_get_type_min_value = (lambda context, builder, sig, args: typ = sig.args[0].dtypeif isinstance(typ, types.Integer):
bw = typ.bitwidthlty = ir.IntType(bw)val = typ.minvalres = ir.Constant(lty, val)elif isinstance(typ, types.Float):
bw = typ.bitwidthif bw == 32:
lty = ir.FloatType()elif bw == 64:
lty = ir.DoubleType()else:
raise NotImplementedError('llvmlite only supports 32 and 64 bit floats')npty = getattr(np, 'float{}'.format(bw))res = ir.Constant(lty, -(np.inf))elif isinstance(typ, (types.NPDatetime, types.NPTimedelta)):
bw = 64lty = ir.IntType(bw)val = types.int64.minval + 1res = ir.Constant(lty, val)impl_ret_untracked(context, builder, lty, res))()()
lower_get_type_max_value = (lambda context, builder, sig, args: typ = sig.args[0].dtypeif isinstance(typ, types.Integer):
bw = typ.bitwidthlty = ir.IntType(bw)val = typ.maxvalres = ir.Constant(lty, val)elif isinstance(typ, types.Float):
bw = typ.bitwidthif bw == 32:
lty = ir.FloatType()elif bw == 64:
lty = ir.DoubleType()else:
raise NotImplementedError('llvmlite only supports 32 and 64 bit floats')npty = getattr(np, 'float{}'.format(bw))res = ir.Constant(lty, np.inf)elif isinstance(typ, (types.NPDatetime, types.NPTimedelta)):
bw = 64lty = ir.IntType(bw)val = types.int64.maxvalres = ir.Constant(lty, val)impl_ret_untracked(context, builder, lty, res))()()
from numba.core.typing.builtins import IndexValue, IndexValueType
from numba.extending import overload, register_jitable
impl_index_value = (lambda context, builder, sig, args: typ = sig.return_type(index, value) = argsindex_value = cgutils.create_struct_proxy(typ)(context, builder)index_value.index = indexindex_value.value = valueindex_value._getvalue())()()
indval_min = (lambda indval1, indval2: if isinstance(indval1, IndexValueType) or isinstance(indval2, IndexValueType):

def min_impl(indval1, indval2):
if np.isnan(indval1.value):
if np.isnan(indval2.value):
if indval1.index < indval2.index:
indval1NoneNoneif None.isnan(indval2.value):
indval2if None.value > indval2.value:
indval2if None.value == indval2.value:
if indval1.index < indval2.index:
indval1Nonemin_implNone)()
boolval_min = (lambda val1, val2: if isinstance(val1, types.Boolean) or isinstance(val2, types.Boolean):

def bool_min_impl(val1, val2):
