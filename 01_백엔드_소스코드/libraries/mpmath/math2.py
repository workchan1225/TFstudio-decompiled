# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: math2.pyc (Python 3.11)

'''
This module complements the math and cmath builtin modules by providing
fast machine precision versions of some additional functions (gamma, ...)
and wrapping math/cmath functions so that they can be called with either
real or complex arguments.
'''
import operator
import math
import cmath
pi = 3.14159
e = 2.71828
sqrt2 = 1.41421
sqrt5 = 2.23607
phi = 1.61803
ln2 = 0.693147
ln10 = 2.30259
euler = 0.577216
catalan = 0.915966
khinchin = 2.68545
apery = 1.20206
logpi = 1.14473

def _mathfun_real(f_real, f_complex):
    pass
# WARNING: Decompyle incomplete


def _mathfun(f_real, f_complex):
    pass
# WARNING: Decompyle incomplete


def _mathfun_n(f_real, f_complex):
    pass
# WARNING: Decompyle incomplete


try:
    math.log(-2)
    
    def math_log(x):
        if x <= 0:
            raise ValueError('math domain error')
        return math.log(x)

    
    def math_sqrt(x):
        if x < 0:
            raise ValueError('math domain error')
        return math.sqrt(x)

except (ValueError, TypeError):
    math_log = math.log
    math_sqrt = math.sqrt

pow = _mathfun_n(operator.pow, (lambda x, y: complex(x) ** y))
log = _mathfun_n(math_log, cmath.log)
sqrt = _mathfun(math_sqrt, cmath.sqrt)
exp = _mathfun_real(math.exp, cmath.exp)
cos = _mathfun_real(math.cos, cmath.cos)
sin = _mathfun_real(math.sin, cmath.sin)
tan = _mathfun_real(math.tan, cmath.tan)
acos = _mathfun(math.acos, cmath.acos)
asin = _mathfun(math.asin, cmath.asin)
atan = _mathfun_real(math.atan, cmath.atan)
cosh = _mathfun_real(math.cosh, cmath.cosh)
sinh = _mathfun_real(math.sinh, cmath.sinh)
tanh = _mathfun_real(math.tanh, cmath.tanh)
floor = _mathfun_real(math.floor, (lambda z: complex(math.floor(z.real), math.floor(z.imag))))
ceil = _mathfun_real(math.ceil, (lambda z: complex(math.ceil(z.real), math.ceil(z.imag))))
cos_sin = _mathfun_real((lambda x: (math.cos(x), math.sin(x))), (lambda z: (cmath.cos(z), cmath.sin(z))))
cbrt = _mathfun((lambda x: x ** 0.333333), (lambda z: z ** 0.333333))

def nthroot(x, n):
    r = 1 / n
    
    try:
        return float(x) ** r
    except (ValueError, TypeError):
        return 



def _sinpi_real(x):
    if x < 0:
        return -_sinpi_real(-x)
    (n, r) = None(x, 0.5)
    r *= pi
    n %= 4
    if n == 0:
        return math.sin(r)
    if None == 1:
        return math.cos(r)
    if None == 2:
        return -math.sin(r)
    if None == 3:
        return -math.cos(r)


def _cospi_real(x):
    if x < 0:
        x = -x
    (n, r) = divmod(x, 0.5)
    r *= pi
    n %= 4
    if n == 0:
        return math.cos(r)
    if None == 1:
        return -math.sin(r)
    if None == 2:
        return -math.cos(r)
    if None == 3:
        return math.sin(r)


def _sinpi_complex(z):
    if z.real < 0:
        return -_sinpi_complex(-z)
    (n, r) = None(z.real, 0.5)
    z = pi * complex(r, z.imag)
    n %= 4
    if n == 0:
        return cmath.sin(z)
    if None == 1:
        return cmath.cos(z)
    if None == 2:
        return -cmath.sin(z)
    if None == 3:
        return -cmath.cos(z)


def _cospi_complex(z):
    if z.real < 0:
        z = -z
    (n, r) = divmod(z.real, 0.5)
    z = pi * complex(r, z.imag)
    n %= 4
    if n == 0:
        return cmath.cos(z)
    if None == 1:
        return -cmath.sin(z)
    if None == 2:
        return -cmath.cos(z)
    if None == 3:
        return cmath.sin(z)

cospi = _mathfun_real(_cospi_real, _cospi_complex)
sinpi = _mathfun_real(_sinpi_real, _sinpi_complex)

def tanpi(x):
    
    try:
        return sinpi(x) / cospi(x)
    except OverflowError:
        if complex(x).imag > 10:
            return (0+1j)
        if None(x).imag < 10:
            return (-0+-1j)



def cotpi(x):
    
    try:
        return cospi(x) / sinpi(x)
    except OverflowError:
        if complex(x).imag > 10:
            return (-0+-1j)
        if None(x).imag < 10:
            return (0+1j)


INF = float('inf')
NINF = -INF
NAN = INF - INF
EPS = 2.22045e-16
_exact_gamma = (INF, 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3.6288e+06, 3.99168e+07, 4.79002e+08, 6.22702e+09, 8.71783e+10, 1.30767e+12, 2.09228e+13, 3.55687e+14, 6.40237e+15, 1.21645e+17, 2.4329e+18)
_max_exact_gamma = len(_exact_gamma) - 1
_lanczos_g = 7
_lanczos_p = (1, 676.52, -1259.14, 771.323, -176.615, 12.5073, -0.138571, 9.98437e-06, 1.50563e-07)

def _gamma_real(x):
    _intx = int(x)
    if _intx == x:
        if _intx <= 0:
            raise ZeroDivisionError('gamma function pole')
        if _intx <= _max_exact_gamma:
            return _exact_gamma[_intx]
        if None < 0.5:
            return pi / (_sinpi_real(x) * _gamma_real(1 - x))
        None -= 1
        r = _lanczos_p[0]
        for i in range(1, _lanczos_g + 2):
            r += _lanczos_p[i] / (x + i)
            t = x + _lanczos_g + 0.5
            return 2.50663 * t ** (x + 0.5) * math.exp(-t) * r


def _gamma_complex(x):
    if not x.imag:
        return complex(_gamma_real(x.real))
    if None.real < 0.5:
        return pi / (_sinpi_complex(x) * _gamma_complex(1 - x))
    None -= 1
    r = _lanczos_p[0]
    for i in range(1, _lanczos_g + 2):
        r += _lanczos_p[i] / (x + i)
        t = x + _lanczos_g + 0.5
        return 2.50663 * t ** (x + 0.5) * cmath.exp(-t) * r

gamma = _mathfun_real(_gamma_real, _gamma_complex)

def rgamma(x):
    
    try:
        return 1 / gamma(x)
    except ZeroDivisionError:
        return 



def factorial(x):
    return gamma(x + 1)


def arg(x):
    if type(x) is float:
        return math.atan2(0, x)
    return None.atan2(x.imag, x.real)


def loggamma(x):
    if type(x) not in (float, complex):
        
        try:
            x = float(x)
        except (ValueError, TypeError):
            x = complex(x)

        
        try:
            xreal = x.real
            ximag = x.imag
        except AttributeError:
            xreal = x
            ximag = 0

        if xreal < 0:
            if abs(x) < 0.5:
                v = log(gamma(x))
                if ximag == 0:
                    v = v.conjugate()
                return v
            z = None - x
            
            try:
                re = z.real
                im = z.imag
            except AttributeError:
                re = z
                im = 0

            refloor = floor(re)
            if im == 0:
                imsign = 0
            elif im < 0:
                imsign = -1
            else:
                imsign = 1
            return (-pi * (0+1j) * abs(refloor) * (1 - abs(imsign)) + logpi - log(sinpi(z - refloor)) - loggamma(z)) + (0+1j) * pi * refloor * imsign
    if x == 1 or x == 2:
        return x * 0
    p = None
# WARNING: Decompyle incomplete

_psi_coeff = [
    0.0833333,
    -0.00833333,
    0.00396825,
    -0.00416667,
    0.00757576,
    -0.0210928,
    0.0833333,
    -0.44326,
    3.05395,
    -26.4562]

def _digamma_real(x):
    _intx = int(x)
    if _intx == x and _intx <= 0:
        raise ZeroDivisionError('polygamma pole')
    if x < 0.5:
        x = 1 - x
        s = pi * cotpi(x)
    else:
        s = 0
# WARNING: Decompyle incomplete


def _digamma_complex(x):
    if not x.imag:
        return complex(_digamma_real(x.real))
    if None.real < 0.5:
        x = 1 - x
        s = pi * cotpi(x)
    else:
        s = 0
# WARNING: Decompyle incomplete

digamma = _mathfun_real(_digamma_real, _digamma_complex)
_erfc_coeff_P = [
    1,
    2.12753,
    2.22804,
    1.46955,
    0.662759,
    0.209248,
    0.0454597,
    0.0063066,
    0.000445603][::-1]
_erfc_coeff_Q = [
    1,
    3.25591,
    4.90194,
    4.49715,
    2.78456,
    1.2146,
    0.376471,
    0.0809701,
    0.0111781,
    0.00078981][::-1]

def _polyval(coeffs, x):
    p = coeffs[0]
    for c in coeffs[1:]:
        p = c + x * p
        return p


def _erf_taylor(x):
    x2 = x * x
    s = x
    t = x
    n = 1
# WARNING: Decompyle incomplete


def _erfc_mid(x):
    return exp(-x * x) * _polyval(_erfc_coeff_P, x) / _polyval(_erfc_coeff_Q, x)


def _erfc_asymp(x):
    x2 = x * x
    v = (exp(-x2) / x) * 0.56419
    r = 0.5 / x2
    t = 0.5 / x2
    s = 1
    for n in range(1, 22, 4):
        s -= t
        t *= r * (n + 2)
        s += t
        t *= r * (n + 4)
        if abs(t) < 1e-17:
            pass
        
        return s * v


def erf(x):
    '''
    erf of a real number.
    '''
    x = float(x)
    if x != x:
        return x
    if None < 0:
        return -erf(-x)
    if None >= 1:
        if x >= 6:
            return 1
        return None - _erfc_mid(x)
    return None(x)


def erfc(x):
    '''
    erfc of a real number.
    '''
    x = float(x)
    if x != x:
        return x
    if None < 0:
        if x < -6:
            return 2
        return None - erfc(-x)
    if None > 9:
        return _erfc_asymp(x)
    if None >= 1:
        return _erfc_mid(x)
    return None - _erf_taylor(x)

gauss42 = [
    (0.9984, 0.004106),
    (-0.9984, 0.004106),
    (0.991577, 0.00953622),
    (-0.991577, 0.00953622),
    (0.979343, 0.0149224),
    (-0.979343, 0.0149224),
    (0.961759, 0.0202279),
    (-0.961759, 0.0202279),
    (0.938924, 0.025423),
    (-0.938924, 0.025423),
    (0.91096, 0.0304792),
    (-0.91096, 0.0304792),
    (0.878021, 0.0353691),
    (-0.878021, 0.0353691),
    (0.840286, 0.0400657),
    (-0.840286, 0.0400657),
    (0.797962, 0.0445436),
    (-0.797962, 0.0445436),
    (0.75128, 0.0487781),
    (-0.75128, 0.0487781),
    (0.700495, 0.0527463),
    (-0.700495, 0.0527463),
    (0.645883, 0.0564264),
    (-0.645883, 0.0564264),
    (0.587745, 0.0597983),
    (-0.587745, 0.0597983),
    (0.526396, 0.0628436),
    (-0.526396, 0.0628436),
    (0.462172, 0.0655456),
    (-0.462172, 0.0655456),
    (0.395424, 0.0678897),
    (-0.395424, 0.0678897),
    (0.326516, 0.069863),
    (-0.326516, 0.069863),
    (0.255825, 0.0714547),
    (-0.255825, 0.0714547),
    (0.183737, 0.0726562),
    (-0.183737, 0.0726562),
    (0.110645, 0.0734608),
    (-0.110645, 0.0734608),
    (0.0369489, 0.0738642),
    (-0.0369489, 0.0738642)]
EI_ASYMP_CONVERGENCE_RADIUS = 40

def ei_asymp(z, _e1 = (False,)):
    r = 1 / z
    s = 1
    t = 1
    k = 1
    t *= k * r
    s += t
    if abs(t) < 1e-16:
        pass
    else:
        k += 1
    v = s * exp(z) / z
    if _e1:
        if type(z) is complex:
            zreal = z.real
            zimag = z.imag
        else:
            zreal = z
            zimag = 0
        if zimag == 0 and zreal > 0:
            v += pi * (0+1j)
        elif type(z) is complex:
            if z.imag > 0:
                v += pi * (0+1j)
            if z.imag < 0:
                v -= pi * (0+1j)
    return v


def ei_taylor(z, _e1 = (False,)):
    s = z
    t = z
    k = 2
    t = t * z / k
    term = t / k
    if abs(term) < 1e-17:
        pass
    else:
        s += term
        k += 1
    s += euler
    if _e1:
        s += log(-z)
    elif type(z) is float or z.imag == 0:
        s += math_log(abs(z))
    else:
        s += cmath.log(z)
    return s


def ei(z, _e1 = (False,)):
    typez = type(z)
    if typez not in (float, complex):
        
        try:
            z = float(z)
            typez = float
        except (TypeError, ValueError):
            z = complex(z)
            typez = complex

        if not z:
            return -INF
        absz = None(z)
        if absz > EI_ASYMP_CONVERGENCE_RADIUS:
            return ei_asymp(z, _e1)
        if (None <= 2 or typez is float) and z > 0:
            return ei_taylor(z, _e1)
        if None is complex and z.real > 0:
            zref = z / absz
            ref = ei_taylor(zref, _e1)
        else:
            zref = EI_ASYMP_CONVERGENCE_RADIUS * z / absz
            ref = ei_asymp(zref, _e1)
    C = (zref - z) * 0.5
    D = (zref + z) * 0.5
    s = 0
    if type(z) is complex:
        _exp = cmath.exp
    else:
        _exp = math.exp
    for x, w in gauss42:
        t = C * x + D
        s += w * _exp(t) / t
        ref -= C * s
        return ref


def e1(z):
    typez = type(z)
    if type(z) not in (float, complex):
        
        try:
            z = float(z)
            typez = float
        except (TypeError, ValueError):
            z = complex(z)
            typez = complex

        if not typez is complex and z.imag:
            z = complex(z.real, 0)
    return -ei(-z, _e1 = True)

_zeta_int = [
    -0.5,
    0,
    1.64493,
    1.20206,
    1.08232,
    1.03693,
    1.01734,
    1.00835,
    1.00408,
    1.00201,
    1.00099,
    1.00049,
    1.00025,
    1.00012,
    1.00006,
    1.00003,
    1.00002,
    1.00001,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1]
_zeta_P = [
    -3.5,
    -0.701274,
    -0.0672313,
    -0.00398731,
    -0.000160949,
    -4.67633e-06,
    -1.02078e-07,
    -1.6803e-09,
    -1.85232e-11][::-1]
_zeta_Q = [
    1,
    -0.936553,
    -0.0588835,
    -0.00441499,
    -0.000143417,
    -5.10692e-06,
    -9.58813e-08,
    -1.72964e-09,
    -1.83528e-11][::-1]
_zeta_1 = [
    3.03769e-10,
    -1.21925e-08,
    2.01202e-07,
    -1.53917e-06,
    -5.0989e-07,
    0.000122465,
    -0.000905722,
    -0.00239315,
    0.0842398,
    0.418939,
    0.5]
_zeta_0 = [
    -3.46092e-10,
    -6.4261e-09,
    1.76409e-07,
    -1.47141e-06,
    -6.3888e-07,
    0.000122641,
    -0.000905895,
    -0.00239303,
    0.0842397,
    0.418939,
    0.5]

def zeta(s):
