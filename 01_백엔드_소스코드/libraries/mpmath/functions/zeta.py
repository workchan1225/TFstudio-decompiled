# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: zeta.pyc (Python 3.11)

from __future__ import print_function
from libmp.backend import xrange
from functions import defun, defun_wrapped, defun_static
stieltjes = (lambda ctx, n, a = (1,): pass# WARNING: Decompyle incomplete
)()
siegeltheta = (lambda ctx, t, derivative = (0,): d = int(derivative)if t == ctx.inf or t == ctx.ninf:
if d < 2:
if t == ctx.ninf and d == 0:
ctx.ninfNone.infNone.zeroif None == 0:
if ctx._im(t):
a = ctx.loggamma(0.25 + (0+0.5j) * t)b = ctx.loggamma(0.25 - (0+0.5j) * t)(-ctx.ln(ctx.pi) / 2) * t - (0+0.5j) * (a - b)if None.isinf(t):
tNone._im(ctx.loggamma(0.25 + (0+0.5j) * t)) - (ctx.ln(ctx.pi) / 2) * tif None > 0:
a = (-0+-0.5j) ** (d - 1) * ctx.polygamma(d - 1, 0.25 - (0+0.5j) * t)b = (0+0.5j) ** (d - 1) * ctx.polygamma(d - 1, 0.25 + (0+0.5j) * t)if ctx._im(t):
if d == 1:
-0.5 * ctx.log(ctx.pi) + 0.25 * (a + b)None * (a + b)if None == 1:
ctx._re(-0.5 * ctx.log(ctx.pi) + 0.25 * (a + b))None._re(0.25 * (a + b)))()
grampoint = (lambda ctx, n: pass# WARNING: Decompyle incomplete
)()
siegelz = (lambda ctx, t: pass# WARNING: Decompyle incomplete
)()
_zeta_zeros = [
    14.1347,
    21.022,
    25.0109,
    30.4249,
    32.9351,
    37.5862,
    40.9187,
    43.3271,
    48.0052,
    49.7738,
    52.9703,
    56.4462,
    59.347,
    60.8318,
    65.1125,
    67.0798,
    69.5464,
    72.0672,
    75.7047,
    77.1448,
    79.3374,
    82.9104,
    84.7355,
    87.4253,
    88.8091,
    92.4919,
    94.6513,
    95.8706,
    98.8312,
    101.318,
    103.726,
    105.447,
    107.169,
    111.03,
    111.875,
    114.32,
    116.227,
    118.791,
    121.37,
    122.947,
    124.257,
    127.517,
    129.579,
    131.088,
    133.498,
    134.757,
    138.116,
    139.736,
    141.124,
    143.112,
    146.001,
    147.423,
    150.054,
    150.925,
    153.025,
    156.113,
    157.598,
    158.85,
    161.189,
    163.031,
    165.537,
    167.184,
    169.095,
    169.912,
    173.412,
    174.754,
    176.441,
    178.377,
    179.916,
    182.207,
    184.874,
    185.599,
    187.229,
    189.416,
    192.027,
    193.08,
    195.265,
    196.876,
    198.015,
    201.265,
    202.494,
    204.19,
    205.395,
    207.906,
    209.577,
    211.691,
    213.348,
    214.547,
    216.17,
    219.068,
    220.715,
    221.431,
    224.007,
    224.983,
    227.421,
    229.337,
    231.25,
    231.987,
    233.693,
    236.524]

def _load_zeta_zeros(url):
    import urllib
    d = urllib.urlopen(url)
    L = d.readlines()()
# WARNING: Decompyle incomplete

oldzetazero = (lambda ctx, n, url = ('http://www.dtc.umn.edu/~odlyzko/zeta_tables/zeros1',): n = int(n)if n < 0:
ctx.zetazero(-n).conjugate()if None == 0:
raise ValueError('n must be nonzero')if n > len(_zeta_zeros) and n <= 100000:
_load_zeta_zeros(url)if n > len(_zeta_zeros):
raise NotImplementedError('n too large for zetazeros')ctx.mpc(0.5, ctx.findroot(ctx.siegelz, _zeta_zeros[n - 1])))()
riemannr = (lambda ctx, x: if x == 0:
ctx.zeroif None(x) > 1000:
a = ctx.li(x)b = 0.5 * ctx.li(ctx.sqrt(x))if abs(b) < abs(a) * ctx.eps:
aif None(x) < 0.01:
passctx.one = ctx.onet = ctx, ctx.prec += int(-ctx.log(abs(x), 2)), .precu = ctx.ln(x)k = 1# WARNING: Decompyle incomplete
)()
primepi = (lambda ctx, x: x = int(x)if x < 2:
0None(ctx.list_primes(x)))()
primepi2 = (lambda ctx, x: x = int(x)if x < 2:
ctx._iv.zeroif None < 2657:
ctx._iv.mpf(ctx.primepi(x))mid = None.li(x)err = ctx.sqrt(x, rounding = 'u') * ctx.ln(x, rounding = 'u') / 8 / ctx.pi(rounding = 'd')a = ctx.floor((ctx._iv.mpf(mid) - err).a, rounding = 'd')b = ctx.ceil((ctx._iv.mpf(mid) + err).b, rounding = 'u')ctx._iv.mpf([
a,
b]))()
primezeta = (lambda ctx, s: pass# WARNING: Decompyle incomplete
)()
bernpoly = (lambda ctx, n, z: pass# WARNING: Decompyle incomplete
)()
eulerpoly = (lambda ctx, n, z: pass# WARNING: Decompyle incomplete
)()
eulernum = (lambda ctx, n, exact = (False,): n = int(n)if exact:
int(ctx._eulernum(n))if None < 100:
ctx.mpf(ctx._eulernum(n))if None % 2:
ctx.zeroNone.ldexp(ctx.eulerpoly(n, 0.5), n))()

def polylog_series(ctx, s, z):
    tol = +(ctx.eps)
    l = ctx.zero
    k = 1
    zk = z
    term = zk / k ** s
    l += term
    if abs(term) < tol:
        pass
    else:
        zk *= z
        k += 1
    return l


def polylog_continuation(ctx, n, z):
    if n < 0:
        return z * 0
    twopij = None * ctx.pi
    a = (-twopij ** n / ctx.fac(n)) * ctx.bernpoly(n, ctx.ln(z) / twopij)
    if ctx._is_real_type(z) and z < 0:
        a = ctx._re(a)
    if (ctx._im(z) < 0 or ctx._im(z) == 0) and ctx._re(z) >= 1:
        a -= twopij * ctx.ln(z) ** (n - 1) / ctx.fac(n - 1)
    return a


def polylog_unitcircle(ctx, n, z):
    tol = +(ctx.eps)
    if n > 1:
        l = ctx.zero
        logz = ctx.ln(z)
        logmz = ctx.one
        m = 0
        if n - m != 1:
            term = ctx.zeta(n - m) * logmz / ctx.fac(m)
            if term and abs(term) < tol:
                pass
            else:
                l += term
                logmz *= logz
                m += 1
            l += (ctx.ln(z) ** (n - 1) / ctx.fac(n - 1)) * (ctx.harmonic(n - 1) - ctx.ln(-ctx.ln(z)))
        elif n < 1:
            l = ctx.fac(-n) * (-ctx.ln(z)) ** (n - 1)
            logz = ctx.ln(z)
            logkz = ctx.one
            k = 0
            b = ctx.bernoulli((k - n) + 1)
            if b:
                term = b * logkz / (ctx.fac(k) * ((k - n) + 1))
                if abs(term) < tol:
                    pass
                else:
                    l -= term
                    logkz *= logz
                    k += 1
            else:
                raise ValueError
            if ctx._is_real_type(z) and z < 0:
                l = ctx._re(l)
    return l


def polylog_general(ctx, s, z):
    v = ctx.zero
    u = ctx.ln(z)
    if not abs(u) < 5:
        j = ctx.j
        v = 1 - s
        y = ctx.ln(-z) / (2 * ctx.pi * j)
        return ctx.gamma(v) * (j ** v * ctx.zeta(v, 0.5 + y) + j ** (-v) * ctx.zeta(v, 0.5 - y)) / (2 * ctx.pi) ** v
    t = None
    k = 0
    term = ctx.zeta(s - k) * t
    if abs(term) < ctx.eps:
        pass
    else:
        v += term
        k += 1
        t *= u
        t /= k
    return ctx.gamma(1 - s) * (-u) ** (s - 1) + v

polylog = (lambda ctx, s, z: s = ctx.convert(s)z = ctx.convert(z)if z == 1:
ctx.zeta(s)if None == -1:
-ctx.altzeta(s)if None == 0:
z / (1 - z)if None == 1:
-ctx.ln(1 - z)if None == -1:
z / (1 - z) ** 2if (None(z) <= 0.75 or ctx.isint(s)) and abs(z) < 0.9:
polylog_series(ctx, s, z)if None(z) >= 1.4 and ctx.isint(s):
-1 ** (s + 1) * polylog_series(ctx, s, 1 / z) + polylog_continuation(ctx, int(ctx.re(s)), z)if None.isint(s):
polylog_unitcircle(ctx, int(ctx.re(s)), z)None(ctx, s, z))()
clsin = (lambda ctx, s, z, pi = (False,): if ctx.isint(s) and s < 0 and int(s) % 2 == 1:
z * 0if None:
a = ctx.expjpi(z)else:
a = ctx.expj(z)if ctx._is_real_type(z) and ctx._is_real_type(s):
ctx.im(ctx.polylog(s, a))b = None / a(-0+-0.5j) * (ctx.polylog(s, a) - ctx.polylog(s, b)))()
clcos = (lambda ctx, s, z, pi = (False,): if ctx.isint(s) and s < 0 and int(s) % 2 == 0:
z * 0if None:
a = ctx.expjpi(z)else:
a = ctx.expj(z)if ctx._is_real_type(z) and ctx._is_real_type(s):
ctx.re(ctx.polylog(s, a))b = None / a0.5 * (ctx.polylog(s, a) + ctx.polylog(s, b)))()
altzeta = (lambda ctx, s: pass# WARNING: Decompyle incomplete
)()
_altzeta_generic = (lambda ctx, s: if s == 1:
ctx.ln2 + 0 * s-None.powm1(2, 1 - s) * ctx.zeta(s))()
zeta = (lambda ctx, s, a, derivative, method = (1, 0, None): d = int(derivative)# WARNING: Decompyle incomplete
)()
_hurwitz = (lambda ctx, s, a, d = (1, 0): prec = ctx.precverbose = kwargs.get('verbose')try:
extraprec = 10(a, atype) = ctx._convert_param(a)if ctx.re(s) < 0:
if verbose:
print('zeta: Attempting reflection formula')try:
ctx.prec = prec_hurwitz_reflection(ctx, s, a, d, atype)except NotImplementedError:
try:
passtry:
if verbose:
print('zeta: Reflection formula failed')if verbose:
print('zeta: Using the Euler-Maclaurin algorithm')ctx.prec = prec + extraprec(T1, T2) = _hurwitz_em(ctx, s, a, d, prec + 10, verbose)cancellation = ctx.mag(T1) - ctx.mag(T1 + T2)if verbose:
print('Term 1:', T1)print('Term 2:', T2)print('Cancellation:', cancellation, 'bits')if cancellation < extraprec:
ctx.prec = precT1 + T2extraprec = None(2 * extraprec, min(cancellation + 5, 100 * prec))if extraprec > kwargs.get('maxprec', 100 * prec):
raise ctx.NoConvergence('zeta: too much cancellation')continueexcept:
ctx.prec = prec)()

def _hurwitz_reflection(ctx, s, a, d, atype):
    pass
# WARNING: Decompyle incomplete


def _hurwitz_em(ctx, s, a, d, prec, verbose):
    a = ctx.convert(a)
    tol = -prec
    M1 = 0
    M2 = prec // 3
    N = M2
    lsum = 0
    if ctx.isint(s):
        s = int(ctx._re(s))
    s1 = s - 1
    l = ctx._zetasum(s, M1 + a, M2 - M1 - 1, [
        d])[0][0]
    lsum += l
    M2a = M2 + a
    logM2a = ctx.ln(M2a)
    logM2ad = logM2a ** d
    logs = [
        logM2ad]
    logr = 1 / logM2a
    rM2a = 1 / M2a
    M2as = M2a ** (-s)
    if d:
        tailsum = ctx.gammainc(d + 1, s1 * logM2a) / s1 ** (d + 1)
    else:
        tailsum = 1 / (s1 * M2a ** s1)
    tailsum += 0.5 * logM2ad * M2as
    U = [
        1]
    r = M2as
    fact = 2
    for j in range(1, N + 1):
        j2 = 2 * j
        if j == 1:
            upds = [
                1]
        else:
            upds = [
                j2 - 2,
                j2 - 1]
        for m in upds:
            D = min(m, d + 1)
            if m <= d:
                logs.append(logs[-1] * logr)
            Un = [
                0] * (D + 1)
            for i in xrange(D):
                Un[i] = (1 - m - s) * U[i]
                for i in xrange(1, D + 1):
                    Un = None
                    r *= rM2a
                    t = ctx.fdot(U, logs) * r * ctx.bernoulli(j2) / -fact
                    tailsum += t
                    if ctx.mag(t) < tol:
                        
                        return None, (lsum, -1 ** d * tailsum)
                    if verbose:
                        print('Sum range:', M1, M2, 'term magnitude', ctx.mag(t), 'tolerance', tol)
    M2 * 2 = M2
    None *= (j2 + 1) * (j2 + 2)
    if ctx.re(s) < 0:
        N += N // 2
    continue

_zetasum = (lambda ctx, s, a, n, derivatives, reflect = ([
    0], False): pass# WARNING: Decompyle incomplete
)()
dirichlet = (lambda ctx, s, chi, derivative = ([
    1], 0): s = ctx.convert(s)q = len(chi)d = int(derivative)if d > 2:
raise NotImplementedError('arbitrary order derivatives')prec = ctx.prectry:
if s == 1:
True = ctx, ctx.prec += 10, .precfor x in chi:
if x and x != 1:
have_pole = Falseh = +(ctx.eps)s += h = ctx, ctx.prec *= 2 * (d + 1), .precif have_pole:
ctx.prec = prec+(ctx.inf)z = None.zerofor p in range(1, q + 1):
if chi[p % q]:
if d == 1:
z += chi[p % q] * (ctx.zeta(s, (p, q), 1) - ctx.zeta(s, (p, q)) * ctx.log(q))continuez += chi[p % q] * ctx.zeta(s, (p, q))z /= q ** sctx.prec = precctx.prec = prec+z)()

def secondzeta_main_term(ctx, s, a, **kwargs):
    pass
# WARNING: Decompyle incomplete


def secondzeta_prime_term(ctx, s, a, **kwargs):
    pass
# WARNING: Decompyle incomplete


def secondzeta_exp_term(ctx, s, a):
    pass
# WARNING: Decompyle incomplete


def secondzeta_singular_term(ctx, s, a, **kwargs):
    pass
# WARNING: Decompyle incomplete

secondzeta = (lambda ctx, s, a = (0.015,): s = ctx.convert(s)a = ctx.convert(a)tol = ctx.epsif ctx.isint(s) and ctx.re(s) <= 1:
if abs(s - 1) < tol * 1000:
ctx.infm = None(round(ctx.re(s)))if m & 1:
ctx.infNone ** (-m // 2) * ctx.fraction(8 - ctx.eulernum(-m, exact = True), 2 ** (-m + 3))prec = None.prectry:
t3 = secondzeta_exp_term(ctx, s, a)extraprec = max(ctx.mag(t3), 0)(t1, r1, gt) = secondzeta_main_term(ctx, s, a, error = 'True', verbose = 'True')(t2, r2, pt) = secondzeta_prime_term(ctx, s, a, error = 'True', verbose = 'True')(t4, r4) = secondzeta_singular_term(ctx, s, a, error = 'True')t3 = secondzeta_exp_term(ctx, s, a)err = r1 + r2 + r4t = (t1 - t2) + t3 - t4if kwargs.get('verbose'):
print('main term =', t1)print('    computed using', gt, 'zeros of zeta')print('prime term =', t2)print('    computed using', pt, 'values of the von Mangoldt function')print('exponential term =', t3)print('singular term =', t4)ctx.prec = precexcept:
ctx.prec = precif kwargs.get('error'):
w = max(ctx.mag(abs(t)), 0)err = max(err * 2 ** w, ctx.eps * 1 * 2 ** w)(+t, err)+ctx, ctx.prec += extraprec + 3, .prec)()
lerchphi = (lambda ctx, z, s, a: pass# WARNING: Decompyle incomplete
)()
