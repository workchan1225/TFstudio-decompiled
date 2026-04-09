# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cmathimpl.pyc (Python 3.11)

'''
Implement the cmath module functions.
'''
import cmath
import math
from numba.core.imputils import Registry, impl_ret_untracked
from numba.core import types, cgutils
from numba.core.typing import signature
from numba.cpython import builtins, mathimpl
from numba.core.extending import overload
registry = Registry('cmathimpl')
lower = registry.lower

def is_nan(builder, z):
    return builder.fcmp_unordered('uno', z.real, z.imag)


def is_inf(builder, z):
    return builder.or_(mathimpl.is_inf(builder, z.real), mathimpl.is_inf(builder, z.imag))


def is_finite(builder, z):
    return builder.and_(mathimpl.is_finite(builder, z.real), mathimpl.is_finite(builder, z.imag))

isnan_float_impl = (lambda context, builder, sig, args: (typ,) = sig.args(value,) = argsz = context.make_complex(builder, typ, value = value)res = is_nan(builder, z)impl_ret_untracked(context, builder, sig.return_type, res))()
isinf_float_impl = (lambda context, builder, sig, args: (typ,) = sig.args(value,) = argsz = context.make_complex(builder, typ, value = value)res = is_inf(builder, z)impl_ret_untracked(context, builder, sig.return_type, res))()
isfinite_float_impl = (lambda context, builder, sig, args: (typ,) = sig.args(value,) = argsz = context.make_complex(builder, typ, value = value)res = is_finite(builder, z)impl_ret_untracked(context, builder, sig.return_type, res))()
impl_cmath_rect = (lambda r, phi: if (lambda .0: [ isinstance(typ, types.Float) for typ in .0 ])((r, phi)()):
        
        def impl(r, phi):
            if not math.isfinite(phi):
                if not r:
                    return abs(r)
                if None.isinf(r):
                    return complex(r, phi)
                real = None.cos(phi)
                imag = math.sin(phi)
                if real == 0 and math.isinf(r):
                    real /= r
                else:
                    real *= r
            if imag == 0 and math.isinf(r):
                imag /= r
            else:
                imag *= r
            return complex(real, imag)

        return impl
    return all
)()

def intrinsic_complex_unary(inner_func):
    pass
# WARNING: Decompyle incomplete

NAN = float('nan')
INF = float('inf')
exp_impl = (lambda x, y, x_is_finite, y_is_finite: if x_is_finite:
if y_is_finite:
c = math.cos(y)s = math.sin(y)r = math.exp(x)complex(r * c, r * s)None(NAN, NAN)if None.isnan(x):
if y:
complex(x, x)None(x, y)if None > 0:
if y_is_finite:
real = math.cos(y)imag = math.sin(y)if real != 0:
real *= xif imag != 0:
imag *= xcomplex(real, imag)None(x, NAN)if None:
r = math.exp(x)c = math.cos(y)s = math.sin(y)complex(r * c, r * s)r = Nonecomplex(r, r))()()
log_impl = (lambda x, y, x_is_finite, y_is_finite: a = math.log(math.hypot(x, y))b = math.atan2(y, x)complex(a, b))()()
log_base_impl = (lambda context, builder, sig, args: (z, base) = args
def log_base(z, base):
cmath.log(z) / cmath.log(base)res = context.compile_internal(builder, log_base, sig, args)impl_ret_untracked(context, builder, sig, res))()
impl_cmath_log10 = (lambda z: pass# WARNING: Decompyle incomplete
)()
phase_impl = (lambda x:
