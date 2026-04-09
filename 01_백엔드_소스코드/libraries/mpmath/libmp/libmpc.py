# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: libmpc.pyc (Python 3.11)

'''
Low-level functions for complex arithmetic.
'''
import sys
from backend import MPZ, MPZ_ZERO, MPZ_ONE, MPZ_TWO, BACKEND
from libmpf import round_floor, round_ceiling, round_down, round_up, round_nearest, round_fast, bitcount, bctable, normalize, normalize1, reciprocal_rnd, rshift, lshift, giant_steps, negative_rnd, to_str, to_fixed, from_man_exp, from_float, to_float, from_int, to_int, fzero, fone, ftwo, fhalf, finf, fninf, fnan, fnone, mpf_abs, mpf_pos, mpf_neg, mpf_add, mpf_sub, mpf_mul, mpf_div, mpf_mul_int, mpf_shift, mpf_sqrt, mpf_hypot, mpf_rdiv_int, mpf_floor, mpf_ceil, mpf_nint, mpf_frac, mpf_sign, mpf_hash, ComplexResult
from libelefun import mpf_pi, mpf_exp, mpf_log, mpf_cos_sin, mpf_cosh_sinh, mpf_tan, mpf_pow_int, mpf_log_hypot, mpf_cos_sin_pi, mpf_phi, mpf_cos, mpf_sin, mpf_cos_pi, mpf_sin_pi, mpf_atan, mpf_atan2, mpf_cosh, mpf_sinh, mpf_tanh, mpf_asin, mpf_acos, mpf_acosh, mpf_nthroot, mpf_fibonacci
mpc_one = (fone, fzero)
mpc_zero = (fzero, fzero)
mpc_two = (ftwo, fzero)
mpc_half = (fhalf, fzero)
_infs = (finf, fninf)
_infs_nan = (finf, fninf, fnan)

def mpc_is_inf(z):
    '''Check if either real or imaginary part is infinite'''
    (re, im) = z
    if re in _infs:
        return True
    if None in _infs:
        return True


def mpc_is_infnan(z):
    '''Check if either real or imaginary part is infinite or nan'''
    (re, im) = z
    if re in _infs_nan:
        return True
    if None in _infs_nan:
        return True


def mpc_to_str(z, dps, **kwargs):
    (re, im) = z
    rs = to_str(re, dps)
# WARNING: Decompyle incomplete


def mpc_to_complex(z, strict, rnd = (False, round_fast)):
    (re, im) = z
    return complex(to_float(re, strict, rnd), to_float(im, strict, rnd))


def mpc_hash(z):
    if sys.version_info >= (3, 2):
        (re, im) = z
        h = mpf_hash(re) + sys.hash_info.imag * mpf_hash(im)
        h = h % 2 ** sys.hash_info.width
        return int(h)
    
    try:
        return hash(mpc_to_complex(z, strict = True))
    except OverflowError:
        return 



def mpc_conjugate(z, prec, rnd = (round_fast,)):
    (re, im) = z
    return (re, mpf_neg(im, prec, rnd))


def mpc_is_nonzero(z):
    return z != mpc_zero


def mpc_add(z, w, prec, rnd = (round_fast,)):
    (a, b) = z
    (c, d) = w
    return (mpf_add(a, c, prec, rnd), mpf_add(b, d, prec, rnd))


def mpc_add_mpf(z, x, prec, rnd = (round_fast,)):
    (a, b) = z
    return (mpf_add(a, x, prec, rnd), b)


def mpc_sub(z, w, prec, rnd = (0, round_fast)):
    (a, b) = z
    (c, d) = w
    return (mpf_sub(a, c, prec, rnd), mpf_sub(b, d, prec, rnd))


def mpc_sub_mpf(z, p, prec, rnd = (0, round_fast)):
    (a, b) = z
    return (mpf_sub(a, p, prec, rnd), b)


def mpc_pos(z, prec, rnd = (round_fast,)):
    (a, b) = z
    return (mpf_pos(a, prec, rnd), mpf_pos(b, prec, rnd))


def mpc_neg(z, prec, rnd = (None, round_fast)):
    (a, b) = z
    return (mpf_neg(a, prec, rnd), mpf_neg(b, prec, rnd))


def mpc_shift(z, n):
    (a, b) = z
    return (mpf_shift(a, n), mpf_shift(b, n))


def mpc_abs(z, prec, rnd = (round_fast,)):
    '''Absolute value of a complex number, |a+bi|.
    Returns an mpf value.'''
    (a, b) = z
    return mpf_hypot(a, b, prec, rnd)


def mpc_arg(z, prec, rnd = (round_fast,)):
    '''Argument of a complex number. Returns an mpf value.'''
    (a, b) = z
    return mpf_atan2(b, a, prec, rnd)


def mpc_floor(z, prec, rnd = (round_fast,)):
    (a, b) = z
    return (mpf_floor(a, prec, rnd), mpf_floor(b, prec, rnd))


def mpc_ceil(z, prec, rnd = (round_fast,)):
    (a, b) = z
    return (mpf_ceil(a, prec, rnd), mpf_ceil(b, prec, rnd))


def mpc_nint(z, prec, rnd = (round_fast,)):
    (a, b) = z
    return (mpf_nint(a, prec, rnd), mpf_nint(b, prec, rnd))


def mpc_frac(z, prec, rnd = (round_fast,)):
    (a, b) = z
    return (mpf_frac(a, prec, rnd), mpf_frac(b, prec, rnd))


def mpc_mul(z, w, prec, rnd = (round_fast,)):
    '''
    Complex multiplication.

    Returns the real and imaginary part of (a+bi)*(c+di), rounded to
    the specified precision. The rounding mode applies to the real and
    imaginary parts separately.
    '''
    (a, b) = z
    (c, d) = w
    p = mpf_mul(a, c)
    q = mpf_mul(b, d)
    r = mpf_mul(a, d)
    s = mpf_mul(b, c)
    re = mpf_sub(p, q, prec, rnd)
    im = mpf_add(r, s, prec, rnd)
    return (re, im)


def mpc_square(z, prec, rnd = (round_fast,)):
    (a, b) = z
    p = mpf_mul(a, a)
    q = mpf_mul(b, b)
    r = mpf_mul(a, b, prec, rnd)
    re = mpf_sub(p, q, prec, rnd)
    im = mpf_shift(r, 1)
    return (re, im)


def mpc_mul_mpf(z, p, prec, rnd = (round_fast,)):
    (a, b) = z
    re = mpf_mul(a, p, prec, rnd)
    im = mpf_mul(b, p, prec, rnd)
    return (re, im)


def mpc_mul_imag_mpf(z, x, prec, rnd = (round_fast,)):
    '''
    Multiply the mpc value z by I*x where x is an mpf value.
    '''
    (a, b) = z
    re = mpf_neg(mpf_mul(b, x, prec, rnd))
    im = mpf_mul(a, x, prec, rnd)
    return (re, im)


def mpc_mul_int(z, n, prec, rnd = (round_fast,)):
    (a, b) = z
    re = mpf_mul_int(a, n, prec, rnd)
    im = mpf_mul_int(b, n, prec, rnd)
    return (re, im)


def mpc_div(z, w, prec, rnd = (round_fast,)):
    (a, b) = z
    (c, d) = w
    wp = prec + 10
    mag = mpf_add(mpf_mul(c, c), mpf_mul(d, d), wp)
    t = mpf_add(mpf_mul(a, c), mpf_mul(b, d), wp)
    u = mpf_sub(mpf_mul(b, c), mpf_mul(a, d), wp)
    return (mpf_div(t, mag, prec, rnd), mpf_div(u, mag, prec, rnd))


def mpc_div_mpf(z, p, prec, rnd = (round_fast,)):
    '''Calculate z/p where p is real'''
    (a, b) = z
    re = mpf_div(a, p, prec, rnd)
    im = mpf_div(b, p, prec, rnd)
    return (re, im)


def mpc_reciprocal(z, prec, rnd = (round_fast,)):
    '''Calculate 1/z efficiently'''
    (a, b) = z
    m = mpf_add(mpf_mul(a, a), mpf_mul(b, b), prec + 10)
    re = mpf_div(a, m, prec, rnd)
    im = mpf_neg(mpf_div(b, m, prec, rnd))
    return (re, im)


def mpc_mpf_div(p, z, prec, rnd = (round_fast,)):
    '''Calculate p/z where p is real efficiently'''
    (a, b) = z
    m = mpf_add(mpf_mul(a, a), mpf_mul(b, b), prec + 10)
    re = mpf_div(mpf_mul(a, p), m, prec, rnd)
    im = mpf_div(mpf_neg(mpf_mul(b, p)), m, prec, rnd)
    return (re, im)


def complex_int_pow(a, b, n):
    '''Complex integer power: computes (a+b*I)**n exactly for
    nonnegative n (a and b must be Python ints).'''
    wre = 1
    wim = 0
# WARNING: Decompyle incomplete


def mpc_pow(z, w, prec, rnd = (round_fast,)):
    if w[1] == fzero:
        return mpc_pow_mpf(z, w[0], prec, rnd)
    return None(mpc_mul(mpc_log(z, prec + 10), w, prec + 10), prec, rnd)


def mpc_pow_mpf(z, p, prec, rnd = (round_fast,)):
    (psign, pman, pexp, pbc) = p
    if pexp >= 0:
        return mpc_pow_int(z, -1 ** psign * (pman << pexp), prec, rnd)
    if None == -1:
        sqrtz = mpc_sqrt(z, prec + 10)
        return mpc_pow_int(sqrtz, -1 ** psign * pman, prec, rnd)
    return None(mpc_mul_mpf(mpc_log(z, prec + 10), p, prec + 10), prec, rnd)


def mpc_pow_int(z, n, prec, rnd = (round_fast,)):
    (a, b) = z
    if b == fzero:
        return (mpf_pow_int(a, n, prec, rnd), fzero)
    if None == fzero:
        v = mpf_pow_int(b, n, prec, rnd)
        n %= 4
        if n == 0:
            return (v, fzero)
        if None == 1:
            return (fzero, v)
        if None == 2:
            return (mpf_neg(v), fzero)
        if None == 3:
            return (fzero, mpf_neg(v))
        if None == 0:
            return mpc_one
        if None == 1:
            return mpc_pos(z, prec, rnd)
        if None == 2:
            return mpc_square(z, prec, rnd)
        if None == -1:
            return mpc_reciprocal(z, prec, rnd)
        if None < 0:
            return mpc_reciprocal(mpc_pow_int(z, -n, prec + 4), prec, rnd)
        (asign, aman, aexp, abc) = None
        (bsign, bman, bexp, bbc) = b
        if asign:
            aman = -aman
    if bsign:
        bman = -bman
    de = aexp - bexp
    abs_de = abs(de)
    exact_size = n * (abs_de + max(abc, bbc))
    if exact_size < 10000:
        if de > 0:
            aman <<= de
            aexp = bexp
        else:
            bman <<= -de
            bexp = aexp
        (re, im) = complex_int_pow(aman, bman, n)
        re = from_man_exp(re, int(n * aexp), prec, rnd)
        im = from_man_exp(im, int(n * bexp), prec, rnd)
        return (re, im)
    return None(mpc_mul_int(mpc_log(z, prec + 10), n, prec + 10), prec, rnd)


def mpc_sqrt(z, prec, rnd = (round_fast,)):
    '''Complex square root (principal branch).

    We have sqrt(a+bi) = sqrt((r+a)/2) + b/sqrt(2*(r+a))*i where
    r = abs(a+bi), when a+bi is not a negative real number.'''
    (a, b) = z
    if b == fzero:
        if a == fzero:
            return (a, b)
        if None[0]:
            im = mpf_sqrt(mpf_neg(a), prec, rnd)
            return (fzero, im)
        re = None(a, prec, rnd)
        return (re, fzero)
    wp = None + 20
    if not a[0]:
        t = mpf_add(mpc_abs((a, b), wp), a, wp)
        u = mpf_shift(t, -1)
        re = mpf_sqrt(u, prec, rnd)
        v = mpf_shift(t, 1)
        w = mpf_sqrt(v, wp)
        im = mpf_div(b, w, prec, rnd)
    else:
        t = mpf_sub(mpc_abs((a, b), wp), a, wp)
        u = mpf_shift(t, -1)
        im = mpf_sqrt(u, prec, rnd)
        v = mpf_shift(t, 1)
        w = mpf_sqrt(v, wp)
        re = mpf_div(b, w, prec, rnd)
        if b[0]:
            re = mpf_neg(re)
            im = mpf_neg(im)
    return (re, im)


def mpc_nthroot_fixed(a, b, n, prec):
    start = 50
    a1 = int(rshift(a, prec - n * start))
    b1 = int(rshift(b, prec - n * start))
    
    try:
        r = (a1 + (0+1j) * b1) ** (1 / n)
        re = r.real
        im = r.imag
        re = MPZ(int(re))
        im = MPZ(int(im))
    except OverflowError:
        a1 = from_int(a1, start)
        b1 = from_int(b1, start)
        fn = from_int(n)
        nth = mpf_rdiv_int(1, fn, start)
        (re, im) = mpc_pow((a1, b1), (nth, fzero), start)
        re = to_int(re)
        im = to_int(im)

    extra = 10
    prevp = start
    extra1 = n
    for p in giant_steps(start, prec + extra):
        (re2, im2) = complex_int_pow(re, im, n - 1)
        re2 = rshift(re2, (n - 1) * prevp - p - extra1)
        im2 = rshift(im2, (n - 1) * prevp - p - extra1)
        r4 = re2 * re2 + im2 * im2 >> p + extra1
        ap = rshift(a, prec - p)
        bp = rshift(b, prec - p)
        rec = ap * re2 + bp * im2 >> p
        imc = -ap * im2 + bp * re2 >> p
        reb = (rec << p) // r4
        imb = (imc << p) // r4
        re = (reb + (n - 1) * lshift(re, p - prevp)) // n
        im = (imb + (n - 1) * lshift(im, p - prevp)) // n
        prevp = p
        return (re, im)


def mpc_nthroot(z, n, prec, rnd = (round_fast,)):
