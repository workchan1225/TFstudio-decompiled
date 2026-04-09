# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bessel.pyc (Python 3.11)

from functions import defun, defun_wrapped
j0 = (lambda ctx, x: ctx.besselj(0, x))()
j1 = (lambda ctx, x: ctx.besselj(1, x))()
besselj = (lambda ctx, n, z, derivative = (0,): pass# WARNING: Decompyle incomplete
)()
besseli = (lambda ctx, n, z, derivative = (0,): pass# WARNING: Decompyle incomplete
)()
bessely = (lambda ctx, n, z, derivative = (0,): if not z:
if derivative:
raise ValueErrorif not n:
-(ctx.inf) + n + zif None.im(n):
ctx.nan * (n + z)r = None.re(n)q = n + 0.5if ctx.isint(q):
if n > 0:
-(ctx.inf) + n + zNone * (n + z)if None < 0 and int(ctx.floor(q)) % 2:
ctx.inf + n + zNone.ninf + n + z(m, d) = ctx.nint_distance(n)if d < -(ctx.prec):
h = +(ctx.eps)n += h = ctx, ctx.prec *= 2, .precelif d < 0:
pass(cos, sin) = ctx.cospi_sinpi(n)# WARNING: Decompyle incomplete
)()
besselk = (lambda ctx, n, z: pass# WARNING: Decompyle incomplete
)()
hankel1 = (lambda ctx, n, x: pass# WARNING: Decompyle incomplete
)()
hankel2 = (lambda ctx, n, x: pass# WARNING: Decompyle incomplete
)()
whitm = (lambda ctx, k, m, z: if z == 0:
if ctx.re(m) > -0.5:
zif None.re(m) < -0.5:
ctx.inf + zNone.nan * zx = None.fmul(-0.5, z, exact = True)y = 0.5 + m# WARNING: Decompyle incomplete
)()
whitw = (lambda ctx, k, m, z: if z == 0:
g = abs(ctx.re(m))if g < 0.5:
zif None > 0.5:
ctx.inf + zNone.nan * zx = None.fmul(-0.5, z, exact = True)y = 0.5 + m# WARNING: Decompyle incomplete
)()
hyperu = (lambda ctx, a, b, z: pass# WARNING: Decompyle incomplete
)()
struveh = (lambda ctx, n, z: pass# WARNING: Decompyle incomplete
)()
struvel = (lambda ctx, n, z: pass# WARNING: Decompyle incomplete
)()

def _anger(ctx, which, v, z, **kwargs):
    pass
# WARNING: Decompyle incomplete

angerj = (lambda ctx, v, z: pass# WARNING: Decompyle incomplete
)()
webere = (lambda ctx, v, z: pass# WARNING: Decompyle incomplete
)()
lommels1 = (lambda ctx, u, v, z: pass# WARNING: Decompyle incomplete
)()
lommels2 = (lambda ctx, u, v, z: pass# WARNING: Decompyle incomplete
)()
ber = (lambda ctx, n, z: pass# WARNING: Decompyle incomplete
)()
bei = (lambda ctx, n, z: pass# WARNING: Decompyle incomplete
)()
ker = (lambda ctx, n, z: pass# WARNING: Decompyle incomplete
)()
kei = (lambda ctx, n, z: pass# WARNING: Decompyle incomplete
)()

def c_memo(f):
    pass
# WARNING: Decompyle incomplete

_airyai_C1 = (lambda ctx: 1 / (ctx.cbrt(9) * ctx.gamma(ctx.mpf(2) / 3)))()
_airyai_C2 = (lambda ctx: -1 / (ctx.cbrt(3) * ctx.gamma(ctx.mpf(1) / 3)))()
_airybi_C1 = (lambda ctx: 1 / (ctx.nthroot(3, 6) * ctx.gamma(ctx.mpf(2) / 3)))()
_airybi_C2 = (lambda ctx: ctx.nthroot(3, 6) / ctx.gamma(ctx.mpf(1) / 3))()

def _airybi_n2_inf(ctx):
    prec = ctx.prec
    
    try:
        v = ctx.power(3, '2/3') * ctx.gamma('2/3') / (2 * ctx.pi)
        ctx.prec = prec
    except:
        ctx.prec = prec

    return +v


def _airyderiv_0(ctx, z, n, ntype, which):
    if ntype == 'Z':
        if n < 0:
            return z
        r = None.mpq_1_3
        prec = ctx.prec
        
        try:
            ctx.gamma((n + 1) * r) * ctx.power(3, n * r) / ctx.pi = ctx, ctx.prec += 10, .prec
            if which == 0:
                v *= ctx.sinpi(2 * (n + 1) * r)
                v /= ctx.power(3, '2/3')
            else:
                v *= abs(ctx.sinpi(2 * (n + 1) * r))
                v /= ctx.power(3, '1/6')
            ctx.prec = prec
        except:
            ctx.prec = prec

        return +v + z
    raise NotImplementedError

airyai = (lambda ctx, z, derivative = (0,): pass# WARNING: Decompyle incomplete
)()
airybi = (lambda ctx, z, derivative = (0,): pass# WARNING: Decompyle incomplete
)()

def _airy_zero(ctx, which, k, derivative, complex = (False,)):
    pass
# WARNING: Decompyle incomplete

airyaizero = (lambda ctx, k, derivative = (0,): _airy_zero(ctx, 0, k, derivative, False))()
airybizero = (lambda ctx, k, derivative, complex = (0, False): _airy_zero(ctx, 1, k, derivative, complex))()

def _scorer(ctx, z, which, kwargs):
    pass
# WARNING: Decompyle incomplete

scorergi = (lambda ctx, z: _scorer(ctx, z, 0, kwargs))()
scorerhi = (lambda ctx, z: _scorer(ctx, z, 1, kwargs))()
coulombc = (lambda ctx, l, eta, _cache = ({ },): if (l, eta) in _cache and _cache[(l, eta)][0] >= ctx.prec:
+_cache[(l, eta)][1]G3 = None.loggamma(2 * l + 2)G1 = ctx.loggamma(1 + l + ctx.j * eta)G2 = ctx.loggamma(1 + l - ctx.j * eta)v = 2 ** l * ctx.exp((-(ctx.pi) * eta + G1 + G2) / 2 - G3)if not ctx.im(l) and ctx.im(eta):
v = ctx.re(v)_cache[(l, eta)] = (ctx.prec, v)v)()
coulombf = (lambda ctx, l, eta, z, w, chop = (1, True): pass# WARNING: Decompyle incomplete
)()
_coulomb_chi = (lambda ctx, l, eta, _cache = ({ },): pass# WARNING: Decompyle incomplete
)()
coulombg = (lambda ctx, l, eta, z, w, chop = (1, True): pass# WARNING: Decompyle incomplete
)()

def mcmahon(ctx, kind, prime, v, m):
    """
    Computes an estimate for the location of the Bessel function zero
    j_{v,m}, y_{v,m}, j'_{v,m} or y'_{v,m} using McMahon's asymptotic
    expansion (Abramowitz & Stegun 9.5.12-13, DLMF 20.21(vi)).

    Returns (r,err) where r is the estimated location of the root
    and err is a positive number estimating the error of the
    asymptotic expansion.
    """
    u = 4 * v ** 2
    if not kind == 1 and prime:
        b = (4 * m + 2 * v - 1) * ctx.pi / 4
    if not kind == 2 and prime:
        b = (4 * m + 2 * v - 3) * ctx.pi / 4
    if kind == 1 and prime:
        b = (4 * m + 2 * v - 3) * ctx.pi / 4
    if kind == 2 and prime:
        b = (4 * m + 2 * v - 1) * ctx.pi / 4
    if not prime:
        s1 = b
        s2 = -(u - 1) / (8 * b)
        s3 = -4 * (u - 1) * (7 * u - 31) / (3 * (8 * b) ** 3)
        s4 = -32 * (u - 1) * ((83 * u ** 2 - 982 * u) + 3779) / (15 * (8 * b) ** 5)
        s5 = -64 * (u - 1) * ((6949 * u ** 3 - 153855 * u ** 2) + 1585743 * u - 6277237) / (105 * (8 * b) ** 7)
    if prime:
        s1 = b
        s2 = -(u + 3) / (8 * b)
        s3 = -4 * (7 * u ** 2 + 82 * u - 9) / (3 * (8 * b) ** 3)
        s4 = -32 * ((83 * u ** 3 + 2075 * u ** 2 - 3039 * u) + 3537) / (15 * (8 * b) ** 5)
        s5 = -64 * ((6949 * u ** 4 + 296492 * u ** 3 - 1248002 * u ** 2) + 7414380 * u - 5853627) / (105 * (8 * b) ** 7)
    terms = [
        s1,
        s2,
        s3,
        s4,
        s5]
    s = s1
    err = 0
    for i in range(1, len(terms)):
        if abs(terms[i]) < abs(terms[i - 1]):
            s += terms[i]
            continue
        err = abs(terms[i])
        if i == len(terms) - 1:
            err = abs(terms[-1])
    return (s, err)


def generalized_bisection(ctx, f, a, b, n):
    '''
    Given f known to have exactly n simple roots within [a,b],
    return a list of n intervals isolating the roots
    and having opposite signs at the endpoints.

    TODO: this can be optimized, e.g. by reusing evaluation points.
    '''
    pass
# WARNING: Decompyle incomplete


def find_in_interval(ctx, f, ab):
    return ctx.findroot(f, ab, solver = 'illinois', verify = False)


def bessel_zero(ctx, kind, prime, v, m, isoltol, _interval_cache = (0.01, { })):
    pass
# WARNING: Decompyle incomplete

besseljzero = (lambda ctx, v, m, derivative = (0,): +bessel_zero(ctx, 1, derivative, v, m))()
besselyzero = (lambda ctx, v, m, derivative = (0,): +bessel_zero(ctx, 2, derivative, v, m))()
