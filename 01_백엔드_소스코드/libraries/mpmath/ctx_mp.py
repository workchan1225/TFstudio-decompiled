# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ctx_mp.pyc (Python 3.11)

'''
This module defines the mpf, mpc classes, and standard functions for
operating with them.
'''
__docformat__ = 'plaintext'
import functools
import re
from ctx_base import StandardBaseContext
from libmp.backend import basestring, BACKEND
from  import libmp
from libmp import MPZ, MPZ_ZERO, MPZ_ONE, int_types, repr_dps, round_floor, round_ceiling, dps_to_prec, round_nearest, prec_to_dps, ComplexResult, to_pickable, from_pickable, normalize, from_int, from_float, from_str, to_int, to_float, to_str, from_rational, from_man_exp, fone, fzero, finf, fninf, fnan, mpf_abs, mpf_pos, mpf_neg, mpf_add, mpf_sub, mpf_mul, mpf_mul_int, mpf_div, mpf_rdiv_int, mpf_pow_int, mpf_mod, mpf_eq, mpf_cmp, mpf_lt, mpf_gt, mpf_le, mpf_ge, mpf_hash, mpf_rand, mpf_sum, bitcount, to_fixed, mpc_to_str, mpc_to_complex, mpc_hash, mpc_pos, mpc_is_nonzero, mpc_neg, mpc_conjugate, mpc_abs, mpc_add, mpc_add_mpf, mpc_sub, mpc_sub_mpf, mpc_mul, mpc_mul_mpf, mpc_mul_int, mpc_div, mpc_div_mpf, mpc_pow, mpc_pow_mpf, mpc_pow_int, mpc_mpf_div, mpf_pow, mpf_pi, mpf_degree, mpf_e, mpf_phi, mpf_ln2, mpf_ln10, mpf_euler, mpf_catalan, mpf_apery, mpf_khinchin, mpf_glaisher, mpf_twinprime, mpf_mertens, int_types
from  import function_docs
from  import rational
new = object.__new__
get_complex = re.compile('^\\(?(?P<re>[\\+\\-]?\\d*(\\.\\d*)?(e[\\+\\-]?\\d+)?)??(?P<im>[\\+\\-]?\\d*(\\.\\d*)?(e[\\+\\-]?\\d+)?j)?\\)?$')
if BACKEND == 'sage':
    from sage.libs.mpmath.ext_main import Context as BaseMPContext
    
    
    ext_main
else:
    from ctx_mp_python import PythonMPContext
    import sage.libs.mpmath.ext_main, libs, mpmath
    from  import ctx_mp_python as _mpf_module
from ctx_mp_python import _mpf, _mpc, mpnumeric

class MPContext(StandardBaseContext, BaseMPContext):
    '''
    Context for multiprecision arithmetic with a global precision.
    '''
    
    def __init__(ctx):
        BaseMPContext.__init__(ctx)
        ctx.trap_complex = False
        ctx.pretty = False
        ctx.types = [
            ctx.mpf,
            ctx.mpc,
            ctx.constant]
        ctx._mpq = rational.mpq
        ctx.default()
        StandardBaseContext.__init__(ctx)
        ctx.mpq = rational.mpq
        ctx.init_builtins()
        ctx.hyp_summators = { }
        ctx._init_aliases()
        
        try:
            ctx.bernoulli.im_func.func_doc = function_docs.bernoulli
            ctx.primepi.im_func.func_doc = function_docs.primepi
            ctx.psi.im_func.func_doc = function_docs.psi
            ctx.atan2.im_func.func_doc = function_docs.atan2
        except AttributeError:
            ctx.bernoulli.__func__.func_doc = function_docs.bernoulli
            ctx.primepi.__func__.func_doc = function_docs.primepi
            ctx.psi.__func__.func_doc = function_docs.psi
            ctx.atan2.__func__.func_doc = function_docs.atan2

        ctx.digamma.func_doc = function_docs.digamma
        ctx.cospi.func_doc = function_docs.cospi
        ctx.sinpi.func_doc = function_docs.sinpi

    
    def init_builtins(ctx):
        mpf = ctx.mpf
        mpc = ctx.mpc
        ctx.one = ctx.make_mpf(fone)
        ctx.zero = ctx.make_mpf(fzero)
        ctx.j = ctx.make_mpc((fzero, fone))
        ctx.inf = ctx.make_mpf(finf)
        ctx.ninf = ctx.make_mpf(fninf)
        ctx.nan = ctx.make_mpf(fnan)
        eps = ctx.constant((lambda prec, rnd: (0, MPZ_ONE, 1 - prec, 1)), 'epsilon of working precision', 'eps')
        ctx.eps = eps
        ctx.pi = ctx.constant(mpf_pi, 'pi', 'pi')
        ctx.ln2 = ctx.constant(mpf_ln2, 'ln(2)', 'ln2')
        ctx.ln10 = ctx.constant(mpf_ln10, 'ln(10)', 'ln10')
        ctx.phi = ctx.constant(mpf_phi, 'Golden ratio phi', 'phi')
        ctx.e = ctx.constant(mpf_e, 'e = exp(1)', 'e')
        ctx.euler = ctx.constant(mpf_euler, "Euler's constant", 'euler')
        ctx.catalan = ctx.constant(mpf_catalan, "Catalan's constant", 'catalan')
        ctx.khinchin = ctx.constant(mpf_khinchin, "Khinchin's constant", 'khinchin')
        ctx.glaisher = ctx.constant(mpf_glaisher, "Glaisher's constant", 'glaisher')
        ctx.apery = ctx.constant(mpf_apery, "Apery's constant", 'apery')
        ctx.degree = ctx.constant(mpf_degree, '1 deg = pi / 180', 'degree')
        ctx.twinprime = ctx.constant(mpf_twinprime, 'Twin prime constant', 'twinprime')
        ctx.mertens = ctx.constant(mpf_mertens, "Mertens' constant", 'mertens')
        ctx.sqrt = ctx._wrap_libmp_function(libmp.mpf_sqrt, libmp.mpc_sqrt)
        ctx.cbrt = ctx._wrap_libmp_function(libmp.mpf_cbrt, libmp.mpc_cbrt)
        ctx.ln = ctx._wrap_libmp_function(libmp.mpf_log, libmp.mpc_log)
        ctx.atan = ctx._wrap_libmp_function(libmp.mpf_atan, libmp.mpc_atan)
        ctx.exp = ctx._wrap_libmp_function(libmp.mpf_exp, libmp.mpc_exp)
        ctx.expj = ctx._wrap_libmp_function(libmp.mpf_expj, libmp.mpc_expj)
        ctx.expjpi = ctx._wrap_libmp_function(libmp.mpf_expjpi, libmp.mpc_expjpi)
        ctx.sin = ctx._wrap_libmp_function(libmp.mpf_sin, libmp.mpc_sin)
        ctx.cos = ctx._wrap_libmp_function(libmp.mpf_cos, libmp.mpc_cos)
        ctx.tan = ctx._wrap_libmp_function(libmp.mpf_tan, libmp.mpc_tan)
        ctx.sinh = ctx._wrap_libmp_function(libmp.mpf_sinh, libmp.mpc_sinh)
        ctx.cosh = ctx._wrap_libmp_function(libmp.mpf_cosh, libmp.mpc_cosh)
        ctx.tanh = ctx._wrap_libmp_function(libmp.mpf_tanh, libmp.mpc_tanh)
        ctx.asin = ctx._wrap_libmp_function(libmp.mpf_asin, libmp.mpc_asin)
        ctx.acos = ctx._wrap_libmp_function(libmp.mpf_acos, libmp.mpc_acos)
        ctx.atan = ctx._wrap_libmp_function(libmp.mpf_atan, libmp.mpc_atan)
        ctx.asinh = ctx._wrap_libmp_function(libmp.mpf_asinh, libmp.mpc_asinh)
        ctx.acosh = ctx._wrap_libmp_function(libmp.mpf_acosh, libmp.mpc_acosh)
        ctx.atanh = ctx._wrap_libmp_function(libmp.mpf_atanh, libmp.mpc_atanh)
        ctx.sinpi = ctx._wrap_libmp_function(libmp.mpf_sin_pi, libmp.mpc_sin_pi)
        ctx.cospi = ctx._wrap_libmp_function(libmp.mpf_cos_pi, libmp.mpc_cos_pi)
        ctx.floor = ctx._wrap_libmp_function(libmp.mpf_floor, libmp.mpc_floor)
        ctx.ceil = ctx._wrap_libmp_function(libmp.mpf_ceil, libmp.mpc_ceil)
        ctx.nint = ctx._wrap_libmp_function(libmp.mpf_nint, libmp.mpc_nint)
        ctx.frac = ctx._wrap_libmp_function(libmp.mpf_frac, libmp.mpc_frac)
        ctx.fib = ctx._wrap_libmp_function(libmp.mpf_fibonacci, libmp.mpc_fibonacci)
        ctx.fibonacci = ctx._wrap_libmp_function(libmp.mpf_fibonacci, libmp.mpc_fibonacci)
        ctx.gamma = ctx._wrap_libmp_function(libmp.mpf_gamma, libmp.mpc_gamma)
        ctx.rgamma = ctx._wrap_libmp_function(libmp.mpf_rgamma, libmp.mpc_rgamma)
        ctx.loggamma = ctx._wrap_libmp_function(libmp.mpf_loggamma, libmp.mpc_loggamma)
        ctx.fac = ctx._wrap_libmp_function(libmp.mpf_factorial, libmp.mpc_factorial)
        ctx.factorial = ctx._wrap_libmp_function(libmp.mpf_factorial, libmp.mpc_factorial)
        ctx.digamma = ctx._wrap_libmp_function(libmp.mpf_psi0, libmp.mpc_psi0)
        ctx.harmonic = ctx._wrap_libmp_function(libmp.mpf_harmonic, libmp.mpc_harmonic)
        ctx.ei = ctx._wrap_libmp_function(libmp.mpf_ei, libmp.mpc_ei)
        ctx.e1 = ctx._wrap_libmp_function(libmp.mpf_e1, libmp.mpc_e1)
        ctx._ci = ctx._wrap_libmp_function(libmp.mpf_ci, libmp.mpc_ci)
        ctx._si = ctx._wrap_libmp_function(libmp.mpf_si, libmp.mpc_si)
        ctx.ellipk = ctx._wrap_libmp_function(libmp.mpf_ellipk, libmp.mpc_ellipk)
        ctx._ellipe = ctx._wrap_libmp_function(libmp.mpf_ellipe, libmp.mpc_ellipe)
        ctx.agm1 = ctx._wrap_libmp_function(libmp.mpf_agm1, libmp.mpc_agm1)
        ctx._erf = ctx._wrap_libmp_function(libmp.mpf_erf, None)
        ctx._erfc = ctx._wrap_libmp_function(libmp.mpf_erfc, None)
        ctx._zeta = ctx._wrap_libmp_function(libmp.mpf_zeta, libmp.mpc_zeta)
        ctx._altzeta = ctx._wrap_libmp_function(libmp.mpf_altzeta, libmp.mpc_altzeta)
        ctx.sqrt = getattr(ctx, '_sage_sqrt', ctx.sqrt)
        ctx.exp = getattr(ctx, '_sage_exp', ctx.exp)
        ctx.ln = getattr(ctx, '_sage_ln', ctx.ln)
        ctx.cos = getattr(ctx, '_sage_cos', ctx.cos)
        ctx.sin = getattr(ctx, '_sage_sin', ctx.sin)

    
    def to_fixed(ctx, x, prec):
        return x.to_fixed(prec)

    
    def hypot(ctx, x, y):
        '''
        Computes the Euclidean norm of the vector `(x, y)`, equal
        to `\\sqrt{x^2 + y^2}`. Both `x` and `y` must be real.'''
        x = ctx.convert(x)
        y = ctx.convert(y)
    # WARNING: Decompyle incomplete

    
    def _gamma_upper_int(ctx, n, z):
        n = int(ctx._re(n))
        if n == 0:
            return ctx.e1(z)
        if not None(z, '_mpf_'):
            raise NotImplementedError
        (prec, rounding) = ctx._prec_rounding
        (real, imag) = libmp.mpf_expint(n, z._mpf_, prec, rounding, gamma = True)
    # WARNING: Decompyle incomplete

    
    def _expint_int(ctx, n, z):
        n = int(n)
        if n == 1:
            return ctx.e1(z)
        if not None(z, '_mpf_'):
            raise NotImplementedError
        (prec, rounding) = ctx._prec_rounding
        (real, imag) = libmp.mpf_expint(n, z._mpf_, prec, rounding)
    # WARNING: Decompyle incomplete

    
    def _nthroot(ctx, x, n):
        pass
    # WARNING: Decompyle incomplete

    
    def _besselj(ctx, n, z):
        (prec, rounding) = ctx._prec_rounding
        if hasattr(z, '_mpf_'):
            return ctx.make_mpf(libmp.mpf_besseljn(n, z._mpf_, prec, rounding))
        if None(z, '_mpc_'):
            return ctx.make_mpc(libmp.mpc_besseljn(n, z._mpc_, prec, rounding))

    
    def _agm(ctx, a, b = (1,)):
        (prec, rounding) = ctx._prec_rounding
        if hasattr(a, '_mpf_') and hasattr(b, '_mpf_'):
            
            try:
                v = libmp.mpf_agm(a._mpf_, b._mpf_, prec, rounding)
                return ctx.make_mpf(v)
            except ComplexResult:
                pass

            if hasattr(a, '_mpf_'):
                a = (a._mpf_, libmp.fzero)
            else:
                a = a._mpc_
        if hasattr(b, '_mpf_'):
            b = (b._mpf_, libmp.fzero)
        else:
            b = b._mpc_
        return ctx.make_mpc(libmp.mpc_agm(a, b, prec, rounding))

    
    def bernoulli(ctx, n):
        pass
    # WARNING: Decompyle incomplete

    
    def _zeta_int(ctx, n):
        pass
    # WARNING: Decompyle incomplete

    
    def atan2(ctx, y, x):
        x = ctx.convert(x)
        y = ctx.convert(y)
    # WARNING: Decompyle incomplete

    
    def psi(ctx, m, z):
        z = ctx.convert(z)
        m = int(m)
    # WARNING: Decompyle incomplete

    
    def cos_sin(ctx, x, **kwargs):
        if type(x) not in ctx.types:
            x = ctx.convert(x)
        (prec, rounding) = ctx._parse_prec(kwargs)
        if hasattr(x, '_mpf_'):
            (c, s) = libmp.mpf_cos_sin(x._mpf_, prec, rounding)
            return (ctx.make_mpf(c), ctx.make_mpf(s))
        if None(x, '_mpc_'):
            (c, s) = libmp.mpc_cos_sin(x._mpc_, prec, rounding)
            return (ctx.make_mpc(c), ctx.make_mpc(s))
    # WARNING: Decompyle incomplete

    
    def cospi_sinpi(ctx, x, **kwargs):
        if type(x) not in ctx.types:
            x = ctx.convert(x)
        (prec, rounding) = ctx._parse_prec(kwargs)
        if hasattr(x, '_mpf_'):
            (c, s) = libmp.mpf_cos_sin_pi(x._mpf_, prec, rounding)
            return (ctx.make_mpf(c), ctx.make_mpf(s))
        if None(x, '_mpc_'):
            (c, s) = libmp.mpc_cos_sin_pi(x._mpc_, prec, rounding)
            return (ctx.make_mpc(c), ctx.make_mpc(s))
    # WARNING: Decompyle incomplete

    
    def clone(ctx):
        '''
        Create a copy of the context, with the same working precision.
        '''
        a = ctx.__class__()
        a.prec = ctx.prec
        return a

    
    def _is_real_type(ctx, x):
        if hasattr(x, '_mpc_') or type(x) is complex:
            return False

    
    def _is_complex_type(ctx, x):
        if hasattr(x, '_mpc_') or type(x) is complex:
            return True

    
    def isnan(ctx, x):
        '''
        Return *True* if *x* is a NaN (not-a-number), or for a complex
        number, whether either the real or complex part is NaN;
        otherwise return *False*::

            >>> from mpmath import *
            >>> isnan(3.14)
            False
            >>> isnan(nan)
            True
            >>> isnan(mpc(3.14,2.72))
            False
            >>> isnan(mpc(3.14,nan))
            True

        '''
        if hasattr(x, '_mpf_'):
            return x._mpf_ == fnan
        if None(x, '_mpc_'):
            return fnan in x._mpc_
        if None(x, int_types) or isinstance(x, rational.mpq):
            return False
        x = None.convert(x)
        if hasattr(x, '_mpf_') or hasattr(x, '_mpc_'):
            return ctx.isnan(x)
        raise None('isnan() needs a number as input')

    
    def isfinite(ctx, x):
        '''
        Return *True* if *x* is a finite number, i.e. neither
        an infinity or a NaN.

            >>> from mpmath import *
            >>> isfinite(inf)
            False
            >>> isfinite(-inf)
            False
            >>> isfinite(3)
            True
            >>> isfinite(nan)
            False
            >>> isfinite(3+4j)
            True
            >>> isfinite(mpc(3,inf))
            False
            >>> isfinite(mpc(nan,3))
            False

        '''
        if ctx.isinf(x) or ctx.isnan(x):
            return False

    
    def isnpint(ctx, x):
