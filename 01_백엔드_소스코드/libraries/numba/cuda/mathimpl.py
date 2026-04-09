# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mathimpl.pyc (Python 3.11)

import math
import operator
from llvmlite import ir
from numba.core import types, typing, cgutils, targetconfig
from numba.core.imputils import Registry
from numba.types import float32, float64, int64, uint64
from numba.cuda import libdevice
from numba import cuda
registry = Registry()
lower = registry.lower
booleans = []
booleans += [
    ('isnand', 'isnanf', math.isnan)]
booleans += [
    ('isinfd', 'isinff', math.isinf)]
booleans += [
    ('isfinited', 'finitef', math.isfinite)]
unarys = []
unarys += [
    ('ceil', 'ceilf', math.ceil)]
unarys += [
    ('floor', 'floorf', math.floor)]
unarys += [
    ('fabs', 'fabsf', math.fabs)]
unarys += [
    ('exp', 'expf', math.exp)]
unarys += [
    ('expm1', 'expm1f', math.expm1)]
unarys += [
    ('erf', 'erff', math.erf)]
unarys += [
    ('erfc', 'erfcf', math.erfc)]
unarys += [
    ('tgamma', 'tgammaf', math.gamma)]
unarys += [
    ('lgamma', 'lgammaf', math.lgamma)]
unarys += [
    ('sqrt', 'sqrtf', math.sqrt)]
unarys += [
    ('log', 'logf', math.log)]
unarys += [
    ('log2', 'log2f', math.log2)]
unarys += [
    ('log10', 'log10f', math.log10)]
unarys += [
    ('log1p', 'log1pf', math.log1p)]
unarys += [
    ('acosh', 'acoshf', math.acosh)]
unarys += [
    ('acos', 'acosf', math.acos)]
unarys += [
    ('cos', 'cosf', math.cos)]
unarys += [
    ('cosh', 'coshf', math.cosh)]
unarys += [
    ('asinh', 'asinhf', math.asinh)]
unarys += [
    ('asin', 'asinf', math.asin)]
unarys += [
    ('sin', 'sinf', math.sin)]
unarys += [
    ('sinh', 'sinhf', math.sinh)]
unarys += [
    ('atan', 'atanf', math.atan)]
unarys += [
    ('atanh', 'atanhf', math.atanh)]
unarys += [
    ('tan', 'tanf', math.tan)]
unarys += [
    ('trunc', 'truncf', math.trunc)]
unarys_fastmath = { }
unarys_fastmath['cosf'] = 'fast_cosf'
unarys_fastmath['sinf'] = 'fast_sinf'
unarys_fastmath['tanf'] = 'fast_tanf'
unarys_fastmath['expf'] = 'fast_expf'
unarys_fastmath['log2f'] = 'fast_log2f'
unarys_fastmath['log10f'] = 'fast_log10f'
unarys_fastmath['logf'] = 'fast_logf'
binarys = []
binarys += [
    ('copysign', 'copysignf', math.copysign)]
binarys += [
    ('atan2', 'atan2f', math.atan2)]
binarys += [
    ('pow', 'powf', math.pow)]
binarys += [
    ('fmod', 'fmodf', math.fmod)]
binarys += [
    ('hypot', 'hypotf', math.hypot)]
binarys += [
    ('remainder', 'remainderf', math.remainder)]
binarys_fastmath = { }
binarys_fastmath['powf'] = 'fast_powf'
math_isinf_isnan_int = (lambda context, builder, sig, args: context.get_constant(types.boolean, 0))()()
maybe_fast_truediv = (lambda context, builder, sig, args: if context.fastmath:
sig = typing.signature(float32, float32, float32)impl = context.get_function(libdevice.fast_fdividef, sig)impl(builder, args)None.if_zero(builder, args[1])context.error_model.fp_zero_division(builder, ('division by zero',))None(None, None)# WARNING: Decompyle incomplete
)()
math_isfinite_int = (lambda context, builder, sig, args: context.get_constant(types.boolean, 1))()
fp16_sin_impl = (lambda context, builder, sig, args: 
def fp16_sin(x):
cuda.fp16.hsin(x)context.compile_internal(builder, fp16_sin, sig, args))()
fp16_cos_impl = (lambda context, builder, sig, args: 
def fp16_cos(x):
cuda.fp16.hcos(x)context.compile_internal(builder, fp16_cos, sig, args))()
fp16_log_impl = (lambda context, builder, sig, args: 
def fp16_log(x):
cuda.fp16.hlog(x)context.compile_internal(builder, fp16_log, sig, args))()
fp16_log10_impl = (lambda context, builder, sig, args: 
def fp16_log10(x):
cuda.fp16.hlog10(x)context.compile_internal(builder, fp16_log10, sig, args))()
fp16_log2_impl = (lambda context, builder, sig, args: 
def fp16_log2(x):
cuda.fp16.hlog2(x)context.compile_internal(builder, fp16_log2, sig, args))()
fp16_exp_impl = (lambda context, builder, sig, args: 
def fp16_exp(x):
cuda.fp16.hexp(x)context.compile_internal(builder, fp16_exp, sig, args))()
fp16_floor_impl = (lambda context, builder, sig, args: 
def fp16_floor(x):
cuda.fp16.hfloor(x)context.compile_internal(builder, fp16_floor, sig, args))()
fp16_ceil_impl = (lambda context, builder, sig, args: 
def fp16_ceil(x):
cuda.fp16.hceil(x)context.compile_internal(builder, fp16_ceil, sig, args))()
fp16_sqrt_impl = (lambda context, builder, sig, args: 
def fp16_sqrt(x):
cuda.fp16.hsqrt(x)context.compile_internal(builder, fp16_sqrt, sig, args))()
fp16_fabs_impl = (lambda context, builder, sig, args: 
def fp16_fabs(x):
cuda.fp16.habs(x)context.compile_internal(builder, fp16_fabs, sig, args))()
fp16_trunc_impl = (lambda context, builder, sig, args: 
def fp16_trunc(x):
cuda.fp16.htrunc(x)context.compile_internal(builder, fp16_trunc, sig, args))()

def impl_boolean(key, ty, libfunc):
    pass
# WARNING: Decompyle incomplete


def get_lower_unary_impl(key, ty, libfunc):
    pass
# WARNING: Decompyle incomplete


def get_unary_impl_for_fn_and_ty(fn, ty):
    tanh_impls = ('tanh', 'tanhf', math.tanh)
    for fname64, fname32, key in unarys + [
        tanh_impls]:
        if fn == key:
            if ty == float32:
                impl = getattr(libdevice, fname32)
            elif ty == float64:
                impl = getattr(libdevice, fname64)
            
            return None, get_lower_unary_impl(key, ty, impl)
        raise RuntimeError(f'''Implementation of {fn} for {ty} not found''')


def impl_unary(key, ty, libfunc):
    lower_unary_impl = get_lower_unary_impl(key, ty, libfunc)
    lower(key, ty)(lower_unary_impl)


def impl_unary_int(key, ty, libfunc):
    pass
# WARNING: Decompyle incomplete


def get_lower_binary_impl(key, ty, libfunc):
    pass
# WARNING: Decompyle incomplete


def get_binary_impl_for_fn_and_ty(fn, ty):
    for fname64, fname32, key in binarys:
        if fn == key:
            if ty == float32:
                impl = getattr(libdevice, fname32)
            elif ty == float64:
                impl = getattr(libdevice, fname64)
            
            return None, get_lower_binary_impl(key, ty, impl)
        raise RuntimeError(f'''Implementation of {fn} for {ty} not found''')


def impl_binary(key, ty, libfunc):
    lower_binary_impl = get_lower_binary_impl(key, ty, libfunc)
    lower(key, ty, ty)(lower_binary_impl)


def impl_binary_int(key, ty, libfunc):
    pass
# WARNING: Decompyle incomplete

for fname64, fname32, key in booleans:
    impl32 = getattr(libdevice, fname32)
    impl64 = getattr(libdevice, fname64)
    impl_boolean(key, float32, impl32)
    impl_boolean(key, float64, impl64)
    for fname64, fname32, key in unarys:
        impl32 = getattr(libdevice, fname32)
        impl64 = getattr(libdevice, fname64)
        impl_unary(key, float32, impl32)
        impl_unary(key, float64, impl64)
        impl_unary_int(key, int64, impl64)
        impl_unary_int(key, uint64, impl64)
        for fname64, fname32, key in binarys:
            impl32 = getattr(libdevice, fname32)
            impl64 = getattr(libdevice, fname64)
            impl_binary(key, float32, impl32)
            impl_binary(key, float64, impl64)
            impl_binary_int(key, int64, impl64)
            impl_binary_int(key, uint64, impl64)
            
            def impl_pow_int(ty, libfunc):
                pass
            # WARNING: Decompyle incomplete

            impl_pow_int(types.float32, libdevice.powif)
            impl_pow_int(types.float64, libdevice.powi)
            
            def impl_modf(ty, libfunc):
                pass
            # WARNING: Decompyle incomplete

            impl_modf(types.float32, libdevice.modff)
            impl_modf(types.float64, libdevice.modf)
            
            def impl_frexp(ty, libfunc):
                pass
            # WARNING: Decompyle incomplete

            impl_frexp(types.float32, libdevice.frexpf)
            impl_frexp(types.float64, libdevice.frexp)
            
            def impl_ldexp(ty, libfunc):
                pass
            # WARNING: Decompyle incomplete

            impl_ldexp(types.float32, libdevice.ldexpf)
            impl_ldexp(types.float64, libdevice.ldexp)
            
            def impl_tanh(ty, libfunc):
                pass
            # WARNING: Decompyle incomplete

            impl_tanh(types.float32, libdevice.tanhf)
            impl_tanh(types.float64, libdevice.tanh)
            impl_unary_int(math.tanh, int64, libdevice.tanh)
            impl_unary_int(math.tanh, uint64, libdevice.tanh)
            
            def cpow_implement(fty, cty):
                pass
            # WARNING: Decompyle incomplete

            cpow_implement(types.float32, types.complex64)
            cpow_implement(types.float64, types.complex128)
            return None
