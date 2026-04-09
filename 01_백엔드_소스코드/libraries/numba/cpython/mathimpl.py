# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mathimpl.pyc (Python 3.11)

'''
Provide math calls that uses intrinsics or libc math functions.
'''
import math
import operator
import sys
import numpy as np
import llvmlite.ir as llvmlite
from llvmlite.ir import Constant
from numba.core.imputils import Registry, impl_ret_untracked
from numba import typeof
from numba.core import types, utils, config, cgutils
from numba.core.extending import overload
from numba.core.typing import signature
from numba.cpython.unsafe.numbers import trailing_zeros
registry = Registry('mathimpl')
lower = registry.lower
_NP_FLT_FINFO = np.finfo(np.dtype('float32'))
FLT_MAX = _NP_FLT_FINFO.max
FLT_MIN = _NP_FLT_FINFO.tiny
_NP_DBL_FINFO = np.finfo(np.dtype('float64'))
DBL_MAX = _NP_DBL_FINFO.max
DBL_MIN = _NP_DBL_FINFO.tiny
FLOAT_ABS_MASK = 2147483647
FLOAT_SIGN_MASK = 0x80000000
DOUBLE_ABS_MASK = 0x7FFFFFFFFFFFFFFF
DOUBLE_SIGN_MASK = 0x8000000000000000

def is_nan(builder, val):
    '''
    Return a condition testing whether *val* is a NaN.
    '''
    return builder.fcmp_unordered('uno', val, val)


def is_inf(builder, val):
    '''
    Return a condition testing whether *val* is an infinite.
    '''
    pos_inf = Constant(val.type, float('+inf'))
    neg_inf = Constant(val.type, float('-inf'))
    isposinf = builder.fcmp_ordered('==', val, pos_inf)
    isneginf = builder.fcmp_ordered('==', val, neg_inf)
    return builder.or_(isposinf, isneginf)


def is_finite(builder, val):
    '''
    Return a condition testing whether *val* is a finite.
    '''
    val_minus_val = builder.fsub(val, val)
    return builder.fcmp_ordered('ord', val_minus_val, val_minus_val)


def f64_as_int64(builder, val):
    '''
    Bitcast a double into a 64-bit integer.
    '''
    pass
# WARNING: Decompyle incomplete


def int64_as_f64(builder, val):
    '''
    Bitcast a 64-bit integer into a double.
    '''
    pass
# WARNING: Decompyle incomplete


def f32_as_int32(builder, val):
    '''
    Bitcast a float into a 32-bit integer.
    '''
    pass
# WARNING: Decompyle incomplete


def int32_as_f32(builder, val):
    '''
    Bitcast a 32-bit integer into a float.
    '''
    pass
# WARNING: Decompyle incomplete


def negate_real(builder, val):
    '''
    Negate real number *val*, with proper handling of zeros.
    '''
    return builder.fsub(Constant(val.type, -0), val)


def call_fp_intrinsic(builder, name, args):
    '''
    Call a LLVM intrinsic floating-point operation.
    '''
    mod = builder.module
    
    def <listcomp>(.0):
        return [ a.type for a in .0 ]

    intr = name(<listcomp>, args())
    return builder.call(intr, args)


def _unary_int_input_wrapper_impl(wrapped_impl):
    '''
    Return an implementation factory to convert the single integral input
    argument to a float64, then defer to the *wrapped_impl*.
    '''
    pass
# WARNING: Decompyle incomplete


def unary_math_int_impl(fn, float_impl):
    impl = _unary_int_input_wrapper_impl(float_impl)
    lower(fn, types.Integer)(impl)


def unary_math_intr(fn, intrcode):
    '''
    Implement the math function *fn* using the LLVM intrinsic *intrcode*.
    '''
    pass
# WARNING: Decompyle incomplete


def unary_math_extern(fn, f32extern, f64extern, int_restype = (False,)):
    """
    Register implementations of Python function *fn* using the
    external function named *f32extern* and *f64extern* (for float32
    and float64 inputs, respectively).
    If *int_restype* is true, then the function's return value should be
    integral, otherwise floating-point.
    """
    pass
# WARNING: Decompyle incomplete

unary_math_intr(math.fabs, 'llvm.fabs')
exp_impl = unary_math_intr(math.exp, 'llvm.exp')
if sys.version_info >= (3, 11):
    exp2_impl = unary_math_intr(math.exp2, 'llvm.exp2')
log_impl = unary_math_intr(math.log, 'llvm.log')
log10_impl = unary_math_intr(math.log10, 'llvm.log10')
log2_impl = unary_math_intr(math.log2, 'llvm.log2')
sin_impl = unary_math_intr(math.sin, 'llvm.sin')
cos_impl = unary_math_intr(math.cos, 'llvm.cos')
log1p_impl = unary_math_extern(math.log1p, 'log1pf', 'log1p')
expm1_impl = unary_math_extern(math.expm1, 'expm1f', 'expm1')
erf_impl = unary_math_extern(math.erf, 'erff', 'erf')
erfc_impl = unary_math_extern(math.erfc, 'erfcf', 'erfc')
tan_impl = unary_math_extern(math.tan, 'tanf', 'tan')
asin_impl = unary_math_extern(math.asin, 'asinf', 'asin')
acos_impl = unary_math_extern(math.acos, 'acosf', 'acos')
atan_impl = unary_math_extern(math.atan, 'atanf', 'atan')
asinh_impl = unary_math_extern(math.asinh, 'asinhf', 'asinh')
acosh_impl = unary_math_extern(math.acosh, 'acoshf', 'acosh')
atanh_impl = unary_math_extern(math.atanh, 'atanhf', 'atanh')
sinh_impl = unary_math_extern(math.sinh, 'sinhf', 'sinh')
cosh_impl = unary_math_extern(math.cosh, 'coshf', 'cosh')
tanh_impl = unary_math_extern(math.tanh, 'tanhf', 'tanh')
log2_impl = unary_math_extern(math.log2, 'log2f', 'log2')
ceil_impl = unary_math_extern(math.ceil, 'ceilf', 'ceil', True)
floor_impl = unary_math_extern(math.floor, 'floorf', 'floor', True)
gamma_impl = unary_math_extern(math.gamma, 'numba_gammaf', 'numba_gamma')
sqrt_impl = unary_math_extern(math.sqrt, 'sqrtf', 'sqrt')
trunc_impl = unary_math_extern(math.trunc, 'truncf', 'trunc', True)
lgamma_impl = unary_math_extern(math.lgamma, 'lgammaf', 'lgamma')
isnan_float_impl = (lambda context, builder, sig, args: (val,) = argsres = is_nan(builder, val)impl_ret_untracked(context, builder, sig.return_type, res))()
isnan_int_impl = (lambda context, builder, sig, args: res = cgutils.false_bitimpl_ret_untracked(context, builder, sig.return_type, res))()
isinf_float_impl = (lambda context, builder, sig, args: (val,) = argsres = is_inf(builder, val)impl_ret_untracked(context, builder, sig.return_type, res))()
isinf_int_impl = (lambda context, builder, sig, args: res = cgutils.false_bitimpl_ret_untracked(context, builder, sig.return_type, res))()
isfinite_float_impl = (lambda context, builder, sig, args: (val,) = argsres = is_finite(builder, val)impl_ret_untracked(context, builder, sig.return_type, res))()
isfinite_int_impl = (lambda context, builder, sig, args: res = cgutils.true_bitimpl_ret_untracked(context, builder, sig.return_type, res))()
copysign_float_impl = (lambda context, builder, sig, args: lty = args[0].typemod = builder.modulefn = cgutils.get_or_insert_function(mod, llvmlite.ir.FunctionType(lty, (lty, lty)), 'llvm.copysign.%s' % lty.intrinsic_name)res = builder.call(fn, args)impl_ret_untracked(context, builder, sig.return_type, res))()
frexp_impl = (lambda context, builder, sig, args: (val,) = argsfltty = context.get_data_type(sig.args[0])intty = context.get_data_type(sig.return_type[1])expptr = cgutils.alloca_once(builder, intty, name = 'exp')fnty = llvmlite.ir.FunctionType(fltty, (fltty, llvmlite.ir.PointerType(intty)))fname = {
'float': 'numba_frexpf',
'double': 'numba_frexp' }[str(fltty)]fn = cgutils.get_or_insert_function(builder.module, fnty, fname)res = builder.call(fn, (val, expptr))res = cgutils.make_anonymous_struct(builder, (res, builder.load(expptr)))impl_ret_untracked(context, builder, sig.return_type, res))()
ldexp_impl = (lambda context, builder, sig, args: (val, exp) = args(fltty, intty) = map(context.get_data_type, sig.args)fnty = llvmlite.ir.FunctionType(fltty, (fltty, intty))fname = {
'float': 'numba_ldexpf',
'double': 'numba_ldexp' }[str(fltty)]fn = cgutils.insert_pure_function(builder.module, fnty, name = fname)res = builder.call(fn, (val, exp))impl_ret_untracked(context, builder, sig.return_type, res))()
atan2_s64_impl = (lambda context, builder, sig, args: (y, x) = argsy = builder.sitofp(y, llvmlite.ir.DoubleType())x = builder.sitofp(x, llvmlite.ir.DoubleType())fsig = signature(types.float64, types.float64, types.float64)atan2_float_impl(context, builder, fsig, (y, x)))()
atan2_u64_impl = (lambda context, builder, sig, args: (y, x) = argsy = builder.uitofp(y, llvmlite.ir.DoubleType())x = builder.uitofp(x, llvmlite.ir.DoubleType())fsig = signature(types.float64, types.float64, types.float64)atan2_float_impl(context, builder, fsig, (y, x)))()
atan2_float_impl = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()
hypot_s64_impl = (lambda context, builder, sig, args: (x, y) = argsy = builder.sitofp(y, llvmlite.ir.DoubleType())x = builder.sitofp(x, llvmlite.ir.DoubleType())fsig = signature(types.float64, types.float64, types.float64)res = hypot_float_impl(context, builder, fsig, (x, y))impl_ret_untracked(context, builder, sig.return_type, res))()
hypot_u64_impl = (lambda context, builder, sig, args: (x, y) = argsy = builder.sitofp(y, llvmlite.ir.DoubleType())x = builder.sitofp(x, llvmlite.ir.DoubleType())fsig = signature(types.float64, types.float64, types.float64)res = hypot_float_impl(context, builder, fsig, (x, y))impl_ret_untracked(context, builder, sig.return_type, res))()
hypot_float_impl = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()
radians_float_impl = (lambda context, builder, sig, args: (x,) = argscoef = context.get_constant(sig.return_type, math.pi / 180)res = builder.fmul(x, coef)impl_ret_untracked(context, builder, sig.return_type, res))()
unary_math_int_impl(math.radians, radians_float_impl)
degrees_float_impl = (lambda context, builder, sig, args: (x,) = argscoef = context.get_constant(sig.return_type, 180 / math.pi)res = builder.fmul(x, coef)impl_ret_untracked(context, builder, sig.return_type, res))()
unary_math_int_impl(math.degrees, degrees_float_impl)
pow_impl = (lambda context, builder, sig, args: impl = context.get_function(operator.pow, sig)impl(builder, args))()()
nextafter_impl = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()

def _unsigned(T):
    '''Convert integer to unsigned integer of equivalent width.'''
    pass

_unsigned_impl = (lambda T: pass# WARNING: Decompyle incomplete
)()

def gcd_impl(context, builder, sig, args):
    (xty, yty) = sig.args
    if not  == xty, yty or xty, yty == sig.return_type:
        pass
    
# WARNING: Decompyle incomplete

lower(math.gcd, types.Integer, types.Integer)(gcd_impl)
