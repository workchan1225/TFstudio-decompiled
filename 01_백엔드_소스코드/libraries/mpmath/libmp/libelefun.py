# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: libelefun.pyc (Python 3.11)

'''
This module implements computation of elementary transcendental
functions (powers, logarithms, trigonometric and hyperbolic
functions, inverse trigonometric and hyperbolic) for real
floating-point numbers.

For complex and interval implementations of the same functions,
see libmpc and libmpi.

'''
import math
from bisect import bisect
from backend import xrange
from backend import MPZ, MPZ_ZERO, MPZ_ONE, MPZ_TWO, MPZ_FIVE, BACKEND
from libmpf import round_floor, round_ceiling, round_down, round_up, round_nearest, round_fast, ComplexResult, bitcount, bctable, lshift, rshift, giant_steps, sqrt_fixed, from_int, to_int, from_man_exp, to_fixed, to_float, from_float, from_rational, normalize, fzero, fone, fnone, fhalf, finf, fninf, fnan, mpf_cmp, mpf_sign, mpf_abs, mpf_pos, mpf_neg, mpf_add, mpf_sub, mpf_mul, mpf_div, mpf_shift, mpf_rdiv_int, mpf_pow_int, mpf_sqrt, reciprocal_rnd, negative_rnd, mpf_perturb, isqrt_fast
from libintmath import ifib
if BACKEND == 'python':
    EXP_COSH_CUTOFF = 600
else:
    EXP_COSH_CUTOFF = 400
EXP_SERIES_U_CUTOFF = 1500
if BACKEND == 'python':
    COS_SIN_CACHE_PREC = 400
else:
    COS_SIN_CACHE_PREC = 200
COS_SIN_CACHE_STEP = 8
cos_sin_cache = { }
MAX_LOG_INT_CACHE = 2000
log_int_cache = { }
LOG_TAYLOR_PREC = 2500
LOG_TAYLOR_SHIFT = 9
log_taylor_cache = { }
LOG_AGM_MAG_PREC_RATIO = 20
ATAN_TAYLOR_PREC = 3000
ATAN_TAYLOR_SHIFT = 7
atan_taylor_cache = { }
cache_prec_steps = [
    22,
    22]
for k in xrange(1, bitcount(LOG_TAYLOR_PREC) + 1):
    cache_prec_steps += [
        min(2 ** k, LOG_TAYLOR_PREC) + 20] * 2 ** (k - 1)
    
    def constant_memo(f):
        '''
    Decorator for caching computed values of mathematical
    constants. This decorator should be applied to a
    function taking a single argument prec as input and
    returning a fixed-point value with the given precision.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    def def_mpf_constant(fixed):
        '''
    Create a function that computes the mpf value for a mathematical
    constant, given a function that computes the fixed-point value.

    Assumptions: the constant is positive and has magnitude ~= 1;
    the fixed-point function rounds to floor.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    def bsp_acot(q, a, b, hyperbolic):
        if b - a == 1:
            a1 = MPZ(2 * a + 3)
            if hyperbolic or a & 1:
                return (MPZ_ONE, a1 * q ** 2, a1)
            return (-None, a1 * q ** 2, a1)
        m = (None + b) // 2
        (p1, q1, r1) = bsp_acot(q, a, m, hyperbolic)
        (p2, q2, r2) = bsp_acot(q, m, b, hyperbolic)
        return (q2 * p1 + r1 * p2, q1 * q2, r1 * r2)

    
    def acot_fixed(a, prec, hyperbolic):
        '''
    Compute acot(a) or acoth(a) for an integer a with binary splitting; see
    http://numbers.computation.free.fr/Constants/Algorithms/splitting.html
    '''
        N = int(0.35 * prec / math.log(a) + 20)
        (p, q, r) = bsp_acot(a, 0, N, hyperbolic)
        return (p + q << prec) // q * a

    
    def machin(coefs, prec, hyperbolic = (False,)):
        '''
    Evaluate a Machin-like formula, i.e., a linear combination of
    acot(n) or acoth(n) for specific integer values of n, using fixed-
    point arithmetic. The input should be a list [(c, n), ...], giving
    c*acot[h](n) + ...
    '''
        extraprec = 10
        s = MPZ_ZERO
        for a, b in coefs:
            s += MPZ(a) * acot_fixed(MPZ(b), prec + extraprec, hyperbolic)
            return s >> extraprec

    ln2_fixed = (lambda prec: machin([
(18, 26),
(-2, 4801),
(8, 8749)], prec, True))()
    ln10_fixed = (lambda prec: machin([
(46, 31),
(34, 49),
(20, 161)], prec, True))()
    CHUD_A = MPZ(13591409)
    CHUD_B = MPZ(545140134)
    CHUD_C = MPZ(640320)
    CHUD_D = MPZ(12)
    
    def bs_chudnovsky(a, b, level, verbose):
        '''
    Computes the sum from a to b of the series in the Chudnovsky
    formula. Returns g, p, q where p/q is the sum as an exact
    fraction and g is a temporary value used to save work
    for recursive calls.
    '''
        if b - a == 1:
            g = MPZ((6 * b - 5) * (2 * b - 1) * (6 * b - 1))
            p = b ** 3 * CHUD_C ** 3 // 24
            q = -1 ** b * g * (CHUD_A + CHUD_B * b)
        elif verbose and level < 4:
            print('  binary splitting', a, b)
        mid = (a + b) // 2
        (g1, p1, q1) = bs_chudnovsky(a, mid, level + 1, verbose)
        (g2, p2, q2) = bs_chudnovsky(mid, b, level + 1, verbose)
        p = p1 * p2
        g = g1 * g2
        q = q1 * p2 + q2 * g1
        return (g, p, q)

    pi_fixed = (lambda prec, verbose, verbose_base = (False, None): N = int(prec / 3.32193 / 14.1816 + 2)if verbose:
print('binary splitting with N =', N)(g, p, q) = bs_chudnovsky(0, N, 0, verbose)sqrtC = isqrt_fast(CHUD_C << 2 * prec)v = p * CHUD_C * sqrtC // (q + CHUD_A * p) * CHUD_Dv)()
    
    def degree_fixed(prec):
        return pi_fixed(prec) // 180

    
    def bspe(a, b):
        '''
    Sum series for exp(1)-1 between a, b, returning the result
    as an exact fraction (p, q).
    '''
        if b - a == 1:
            return (MPZ_ONE, MPZ(b))
        m = (None + b) // 2
        (p1, q1) = bspe(a, m)
        (p2, q2) = bspe(m, b)
        return (p1 * q2 + p2, q1 * q2)

    e_fixed = (lambda prec: N = int(1.1 * prec / math.log(prec) + 20)(p, q) = bspe(0, N)(p + q << prec) // q)()
    phi_fixed = (lambda prec: prec += 10a = isqrt_fast(MPZ_FIVE << 2 * prec) + (MPZ_ONE << prec)a >> 11)()
    mpf_phi = def_mpf_constant(phi_fixed)
    mpf_pi = def_mpf_constant(pi_fixed)
    mpf_e = def_mpf_constant(e_fixed)
    mpf_degree = def_mpf_constant(degree_fixed)
    mpf_ln2 = def_mpf_constant(ln2_fixed)
    mpf_ln10 = def_mpf_constant(ln10_fixed)
    ln_sqrt2pi_fixed = (lambda prec: wp = prec + 10to_fixed(mpf_log(mpf_shift(mpf_pi(wp), 1), wp), prec - 1))()
    sqrtpi_fixed = (lambda prec: sqrt_fixed(pi_fixed(prec), prec))()
    mpf_sqrtpi = def_mpf_constant(sqrtpi_fixed)
    mpf_ln_sqrt2pi = def_mpf_constant(ln_sqrt2pi_fixed)
    
    def mpf_pow(s, t, prec, rnd = (round_fast,)):
        '''
    Compute s**t. Raises ComplexResult if s is negative and t is
    fractional.
    '''
        (ssign, sman, sexp, sbc) = s
        (tsign, tman, texp, tbc) = t
        if ssign and texp < 0:
            raise ComplexResult('negative number raised to a fractional power')
        if texp >= 0:
            return mpf_pow_int(s, -1 ** tsign * (tman << texp), prec, rnd)
        if None == -1:
            if tman == 1:
                if tsign:
                    return mpf_div(fone, mpf_sqrt(s, prec + 10, reciprocal_rnd[rnd]), prec, rnd)
                return None(s, prec, rnd)
            if None:
                return mpf_pow_int(mpf_sqrt(s, prec + 10, reciprocal_rnd[rnd]), -tman, prec, rnd)
            return None(mpf_sqrt(s, prec + 10, rnd), tman, prec, rnd)
        c = None(s, prec + 10, rnd)
        return mpf_exp(mpf_mul(t, c), prec, rnd)

    
    def int_pow_fixed(y, n, prec):
