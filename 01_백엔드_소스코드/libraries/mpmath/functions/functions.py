# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: functions.pyc (Python 3.11)

from libmp.backend import xrange

class SpecialFunctions(object):
    '''
    This class implements special functions using high-level code.

    Elementary and some other functions (e.g. gamma function, basecase
    hypergeometric series) are assumed to be predefined by the context as
    "builtins" or "low-level" functions.
    '''
    defined_functions = { }
    THETA_Q_LIM = 1
    
    def __init__(self):
        cls = self.__class__
        for name in cls.defined_functions:
            (f, wrap) = cls.defined_functions[name]
            cls._wrap_specfun(name, f, wrap)
            self.mpq_1 = self._mpq((1, 1))
            self.mpq_0 = self._mpq((0, 1))
            self.mpq_1_2 = self._mpq((1, 2))
            self.mpq_3_2 = self._mpq((3, 2))
            self.mpq_1_4 = self._mpq((1, 4))
            self.mpq_1_16 = self._mpq((1, 16))
            self.mpq_3_16 = self._mpq((3, 16))
            self.mpq_5_2 = self._mpq((5, 2))
            self.mpq_3_4 = self._mpq((3, 4))
            self.mpq_7_4 = self._mpq((7, 4))
            self.mpq_5_4 = self._mpq((5, 4))
            self.mpq_1_3 = self._mpq((1, 3))
            self.mpq_2_3 = self._mpq((2, 3))
            self.mpq_4_3 = self._mpq((4, 3))
            self.mpq_1_6 = self._mpq((1, 6))
            self.mpq_5_6 = self._mpq((5, 6))
            self.mpq_5_3 = self._mpq((5, 3))
            self._misc_const_cache = { }
            self._aliases.update({
                'phase': 'arg',
                'conjugate': 'conj',
                'nthroot': 'root',
                'polygamma': 'psi',
                'hurwitz': 'zeta',
                'fibonacci': 'fib',
                'factorial': 'fac' })
            self.zetazero_memoized = self.memoize(self.zetazero)
            return None

    _wrap_specfun = (lambda cls, name, f, wrap: setattr(cls, name, f))()
    
    def _besselj(ctx, n, z):
        raise NotImplementedError

    
    def _erf(ctx, z):
        raise NotImplementedError

    
    def _erfc(ctx, z):
        raise NotImplementedError

    
    def _gamma_upper_int(ctx, z, a):
        raise NotImplementedError

    
    def _expint_int(ctx, n, z):
        raise NotImplementedError

    
    def _zeta(ctx, s):
        raise NotImplementedError

    
    def _zetasum_fast(ctx, s, a, n, derivatives, reflect):
        raise NotImplementedError

    
    def _ei(ctx, z):
        raise NotImplementedError

    
    def _e1(ctx, z):
        raise NotImplementedError

    
    def _ci(ctx, z):
        raise NotImplementedError

    
    def _si(ctx, z):
        raise NotImplementedError

    
    def _altzeta(ctx, s):
        raise NotImplementedError



def defun_wrapped(f):
    SpecialFunctions.defined_functions[f.__name__] = (f, True)
    return f


def defun(f):
    SpecialFunctions.defined_functions[f.__name__] = (f, False)
    return f


def defun_static(f):
    setattr(SpecialFunctions, f.__name__, f)
    return f

cot = (lambda ctx, z: ctx.one / ctx.tan(z))()
sec = (lambda ctx, z: ctx.one / ctx.cos(z))()
csc = (lambda ctx, z: ctx.one / ctx.sin(z))()
coth = (lambda ctx, z: ctx.one / ctx.tanh(z))()
sech = (lambda ctx, z: ctx.one / ctx.cosh(z))()
csch = (lambda ctx, z: ctx.one / ctx.sinh(z))()
acot = (lambda ctx, z: if not z:
ctx.pi * 0.5None.atan(ctx.one / z))()
asec = (lambda ctx, z: ctx.acos(ctx.one / z))()
acsc = (lambda ctx, z: ctx.asin(ctx.one / z))()
acoth = (lambda ctx, z: if not z:
ctx.pi * (0+0.5j)None.atanh(ctx.one / z))()
asech = (lambda ctx, z: ctx.acosh(ctx.one / z))()
acsch = (lambda ctx, z: ctx.asinh(ctx.one / z))()
sign = (lambda ctx, x: x = ctx.convert(x)if x or ctx.isnan(x):
xif None._is_real_type(x):
if x > 0:
ctx.one-(None.one)None / abs(x))()
agm = (lambda ctx, a, b = (1,): if b == 1:
ctx.agm1(a)a = None.convert(a)b = ctx.convert(b)ctx._agm(a, b))()
sinc = (lambda ctx, x: if ctx.isinf(x):
1 / xif not None:
x + 1None.sin(x) / x)()
sincpi = (lambda ctx, x: if ctx.isinf(x):
1 / xif not None:
x + 1None.sinpi(x) / (ctx.pi * x))()
expm1 = (lambda ctx, x: pass# WARNING: Decompyle incomplete
)()
log1p = (lambda ctx, x: if not x:
ctx.zeroif None.mag(x) < -(ctx.prec):
x - 0.5 * x ** 2None.log(ctx.fadd(1, x, prec = 2 * ctx.prec)))()
powm1 = (lambda ctx, x, y: pass# WARNING: Decompyle incomplete
)()
_rootof1 = (lambda ctx, k, n: k = int(k)n = int(n)k %= nif not k:
ctx.oneif None * k == n:
-(ctx.one)if None * k == n:
ctx.jif None * k == 3 * n:
-(ctx.j)None.expjpi(2 * ctx.mpf(k) / n))()
root = (lambda ctx, x, n, k = (0,): n = int(n)x = ctx.convert(x)if k:
if n & 1 and 2 * k == n - 1 and ctx.im(x) and ctx.re(x) < 0:
-ctx.root(-x, n)prec = None.prectry:
ctx.root(x, n, 0) * ctx._rootof1(k, n) = ctx, ctx.prec += 10, .precctx.prec = precexcept:
ctx.prec = prec+vctx._nthroot(x, n))()
unitroots = (lambda ctx, n, primitive = (False,): pass# WARNING: Decompyle incomplete
)()
arg = (lambda ctx, x: x = ctx.convert(x)re = ctx._re(x)im = ctx._im(x)ctx.atan2(im, re))()
fabs = (lambda ctx, x: abs(ctx.convert(x)))()
re = (lambda ctx, x: x = ctx.convert(x)if hasattr(x, 'real'):
x.real)()
im = (lambda ctx, x: x = ctx.convert(x)if hasattr(x, 'imag'):
x.imagNone.zero)()
conj = (lambda ctx, x: x = ctx.convert(x)try:
x.conjugate()except AttributeError:
)()
polar = (lambda ctx, z: (ctx.fabs(z), ctx.arg(z)))()
rect = (lambda ctx, r, phi: pass# WARNING: Decompyle incomplete
)()
log = (lambda ctx, x, b = (None,): pass# WARNING: Decompyle incomplete
)()
log10 = (lambda ctx, x: ctx.log(x, 10))()
fmod = (lambda ctx, x, y: ctx.convert(x) % ctx.convert(y))()
degrees = (lambda ctx, x: x / ctx.degree)()
radians = (lambda ctx, x: x * ctx.degree)()

def _lambertw_special(ctx, z, k):
    if not z:
        if not k:
            return z
        return None.ninf + z
    if None == ctx.inf:
        if k == 0:
            return z
        return None + 2 * k * ctx.pi * ctx.j
    if None == ctx.ninf:
        return -z + (2 * k + 1) * ctx.pi * ctx.j
    return None.ln(z)

import math
import cmath

def _lambertw_approx_hybrid(z, k):
    imag_sign = 0
    if hasattr(z, 'imag'):
        x = float(z.real)
        y = z.imag
        if y:
            imag_sign = -1 ** (y < 0)
        y = float(y)
    else:
        x = float(z)
        y = 0
        imag_sign = 0
    if not y:
        y = 0
    z = complex(x, y)
    if k == 0:
        if  < -4, y or -4, y < 4:
            pass
        
    elif  < -1, x or -1, x < 2.5:
        pass
    
    if imag_sign:
        if y > 1:
            return (0.876+0.645j) + (0.118+-0.174j) * (z - (0.75+2.5j))
        if None > 0.25:
            return (0.505+0.204j) + (0.375+-0.132j) * (z - (0.75+0.5j))
        if None < -1:
            return (0.876+-0.645j) + (0.118+0.174j) * (z - (0.75+-2.5j))
        if None < -0.25:
            return (0.505+-0.204j) + (0.375+0.132j) * (z - (0.75+-0.5j))
        if None < -0.5:
            if imag_sign >= 0:
                return (-0.318+1.34j) + (-0.697+-0.593j) * (z + 1)
            return None + (-0.697+0.593j) * (z + 1)
        if imag_sign and x > r:
            x = None
    if x < -0.2:
        return -1 + 2.33164 * (z - r) ** 0.5 - 1.81219 * (z - r)
    if None < 0.5:
        return z
    return None + 0.3 * z
    if imag_sign and x > 0:
        L1 = math.log(x)
        L2 = math.log(L1)
    else:
        L1 = cmath.log(z)
        L2 = cmath.log(L1)
    if k == -1:
        r = -0.367879
        if imag_sign >= 0 and y < 0.1:
            if  < -0.6, x or -0.6, x < -0.2:
                pass
            else:
                None if not imag_sign else x
        else:
            return -1 - 2.33164 * (z - r) ** 0.5 - 1.81219 * (z - r)
        if not None if not imag_sign else x:
            if  <= -0.2, x or -0.2, x < 0:
                pass
            
        else:
            return L1 - math.log(-L1)
        if None == -1 and y and x < 0:
            cmath.log(z) - (0+3.14159j) = None
        else:
            L1 = cmath.log(z) - (0+6.28319j)
        L2 = cmath.log(L1)
    return (L1 - L2) + L2 / L1 + L2 * (L2 - 2) / (2 * L1 ** 2)


def _lambertw_series(ctx, z, k, tol):
    '''
    Return rough approximation for W_k(z) from an asymptotic series,
    sufficiently accurate for the Halley iteration to converge to
    the correct value.
    '''
    pass
# WARNING: Decompyle incomplete

lambertw = (lambda ctx, z, k = (0,): z = ctx.convert(z)k = int(k)if not ctx.isnormal(z):
_lambertw_special(ctx, z, k)prec = None.precif not k:
ctx.prec = ctx, ctx.prec += 20 + ctx.mag(1), .prectol = wp - 5(w, done) = _lambertw_series(ctx, z, k, tol)if not done:
two = ctx.mpf(2)for i in xrange(100):
ew = ctx.exp(w)wew = w * ewwewz = wew - zwn = w - wewz / (wew + ew - (w + two) * wewz / (two * w + two))if ctx.mag(wn - w) <= ctx.mag(wn) - tol:
w = wnelse:
w = wnif i == 100:
ctx.warn('Lambert W iteration failed to converge for z = %s' % z)ctx.prec = prec+w)()
bell = (lambda ctx, n, x = (1,): x = ctx.convert(x)if not n:
if ctx.isnan(x):
xtype(x)(1)if None.isinf(x) and ctx.isinf(n) and ctx.isnan(x) or ctx.isnan(n):
x ** nif None == 1:
xif None == 2:
x * (x + 1)if None == 0:
ctx.sincpi(n)None(ctx, n, x, True) / ctx.exp(x))()

def _polyexp(ctx, n, x, extra = (False,)):
    pass
# WARNING: Decompyle incomplete

polyexp = (lambda ctx, s, z: if ctx.isinf(z) and ctx.isinf(s) and ctx.isnan(z) or ctx.isnan(s):
z ** sif None == 0:
z * sif None == 0:
ctx.expm1(z)if None == 1:
ctx.exp(z) * zif None == 2:
ctx.exp(z) * z * (z + 1)None(ctx, s, z))()
cyclotomic = (lambda ctx, n, z: n = int(n)if n < 0:
raise ValueError('n cannot be negative')p = ctx.oneif n == 0:
pif None == 1:
z - pif None == 2:
z + pa_prod = Noneb_prod = 1num_zeros = 0num_poles = 0for d in range(1, n + 1):
if not n % d:
w = ctx.moebius(n // d)b = -ctx.powm1(z, d)if b:
p *= b ** wcontinueif w == 1:
a_prod *= dnum_zeros += 1continueif w == -1:
b_prod *= dnum_poles += 1if num_zeros:
if num_zeros > num_poles:
p *= 0else:
p *= a_prodp /= b_prodp)()
mangoldt = (lambda ctx, n: n = int(n)if n < 2:
ctx.zeroif None % 2 == 0:
if n & n - 1 == 0:
+(ctx.ln2)None.zero# WARNING: Decompyle incomplete
)()
stirling1 = (lambda ctx, n, k, exact = (False,): v = ctx._stirling1(int(n), int(k))if exact:
int(v)None.mpf(v))()
stirling2 = (lambda ctx, n, k, exact = (False,): v = ctx._stirling2(int(n), int(k))if exact:
int(v)None.mpf(v))()
