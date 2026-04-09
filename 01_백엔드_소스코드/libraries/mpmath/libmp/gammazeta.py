# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gammazeta.pyc (Python 3.11)

__doc__ = '\n-----------------------------------------------------------------------\nThis module implements gamma- and zeta-related functions:\n\n* Bernoulli numbers\n* Factorials\n* The gamma function\n* Polygamma functions\n* Harmonic numbers\n* The Riemann zeta function\n* Constants related to these functions\n\n-----------------------------------------------------------------------\n'
import math
import sys
from backend import xrange
from backend import MPZ, MPZ_ZERO, MPZ_ONE, MPZ_THREE, gmpy
from libintmath import list_primes, ifac, ifac2, moebius
from libmpf import round_floor, round_ceiling, round_down, round_up, round_nearest, round_fast, lshift, sqrt_fixed, isqrt_fast, fzero, fone, fnone, fhalf, ftwo, finf, fninf, fnan, from_int, to_int, to_fixed, from_man_exp, from_rational, mpf_pos, mpf_neg, mpf_abs, mpf_add, mpf_sub, mpf_mul, mpf_mul_int, mpf_div, mpf_sqrt, mpf_pow_int, mpf_rdiv_int, mpf_perturb, mpf_le, mpf_lt, mpf_gt, mpf_shift, negative_rnd, reciprocal_rnd, bitcount, to_float, mpf_floor, mpf_sign, ComplexResult
from libelefun import constant_memo, def_mpf_constant, mpf_pi, pi_fixed, ln2_fixed, log_int_fixed, mpf_ln2, mpf_exp, mpf_log, mpf_pow, mpf_cosh, mpf_cos_sin, mpf_cosh_sinh, mpf_cos_sin_pi, mpf_cos_pi, mpf_sin_pi, ln_sqrt2pi_fixed, mpf_ln_sqrt2pi, sqrtpi_fixed, mpf_sqrtpi, cos_sin_fixed, exp_fixed
from libmpc import mpc_zero, mpc_one, mpc_half, mpc_two, mpc_abs, mpc_shift, mpc_pos, mpc_neg, mpc_add, mpc_sub, mpc_mul, mpc_div, mpc_add_mpf, mpc_mul_mpf, mpc_div_mpf, mpc_mpf_div, mpc_mul_int, mpc_pow_int, mpc_log, mpc_exp, mpc_pow, mpc_cos_pi, mpc_sin_pi, mpc_reciprocal, mpc_square, mpc_sub_mpf
catalan_fixed = (lambda prec: prec = prec + 20a = MPZ_ONE << precone = MPZ_ONE << prec(s, t, n) = (0, 1, 1)# WARNING: Decompyle incomplete
)()
khinchin_fixed = (lambda prec: wp = int(prec + prec ** 0.5 + 15)s = MPZ_ZEROfac = from_int(4)t = MPZ_ONE << wpONE = MPZ_ONE << wppi = mpf_pi(wp)pipow = mpf_shift(mpf_mul(pi, pi, wp), 2)twopi2 = mpf_shift(mpf_mul(pi, pi, wp), 2)n = 1zeta2n = mpf_abs(mpf_bernoulli(2 * n, wp))zeta2n = mpf_mul(zeta2n, pipow, wp)zeta2n = mpf_div(zeta2n, fac, wp)zeta2n = to_fixed(zeta2n, wp)term = (zeta2n - ONE) * t // n >> wpif term < 100:
passelse:
s += termt += ONE // (2 * n + 1) - ONE // 2 * nn += 1fac = mpf_mul_int(fac, 2 * n * (2 * n - 1), wp)pipow = mpf_mul(pipow, twopi2, wp)s = (s << wp) // ln2_fixed(wp)K = mpf_exp(from_man_exp(s, -wp), wp)K = to_fixed(K, prec)K)()
glaisher_fixed = (lambda prec: wp = prec + 30N = int(0.33 * prec + 5)ONE = MPZ_ONE << wps = MPZ_ZEROfor k in range(2, N):
s += log_int_fixed(k, wp) // k ** 2logN = log_int_fixed(N, wp)s += (ONE + logN) // Ns += logN // N ** 2 * 2pN = N ** 3a = 1b = -2j = 3fac = from_int(2)k = 1D = ((a << wp) + b * logN) // pND = from_man_exp(D, -wp)B = mpf_bernoulli(2 * k, wp)term = mpf_mul(B, D, wp)term = mpf_div(term, fac, wp)term = to_fixed(term, wp)if abs(term) < 100:
passelse:
s -= term(a, b, pN, j) = (b - a * j, -j * b, pN * N, j + 1)(a, b, pN, j) = (b - a * j, -j * b, pN * N, j + 1)k += 1fac = mpf_mul_int(fac, 2 * k * (2 * k - 1), wp)pi = pi_fixed(wp)s *= 6s = (s << wp) // (pi ** 2 >> wp)s += euler_fixed(wp)s += to_fixed(mpf_log(from_man_exp(2 * pi, -wp), wp), wp)s //= 12A = mpf_exp(from_man_exp(s, -wp), wp)to_fixed(A, prec))()
apery_fixed = (lambda prec: prec += 20d = MPZ_ONE << precterm = MPZ(77) << precn = 1s = MPZ_ZERO# WARNING: Decompyle incomplete
)()
euler_fixed = (lambda prec: extra = 30prec += extrap = int(math.log((prec / 4) * math.log(2), 2)) + 1n = 2 ** pA = -p * ln2_fixed(prec)U = -p * ln2_fixed(prec)B = MPZ_ONE << precV = MPZ_ONE << preck = 1B = B * n ** 2 // k ** 2A = (A * n ** 2 // k + B) // kU += AV += Bif max(abs(A), abs(B)) < 100:
passelse:
k += 1(U << prec - extra) // V)()
mertens_fixed = (lambda prec: wp = prec + 20m = 2s = mpf_euler(wp)t = mpf_zeta_int(m, wp)if t == fone:
passelse:
t = mpf_log(t, wp)t = mpf_mul_int(t, moebius(m), wp)t = mpf_div(t, from_int(m), wp)s = mpf_add(s, t)m += 1to_fixed(s, prec))()
twinprime_fixed = (lambda prec: pass# WARNING: Decompyle incomplete
)()
mpf_euler = def_mpf_constant(euler_fixed)
mpf_apery = def_mpf_constant(apery_fixed)
mpf_khinchin = def_mpf_constant(khinchin_fixed)
mpf_glaisher = def_mpf_constant(glaisher_fixed)
mpf_catalan = def_mpf_constant(catalan_fixed)
mpf_mertens = def_mpf_constant(mertens_fixed)
mpf_twinprime = def_mpf_constant(twinprime_fixed)
MAX_BERNOULLI_CACHE = 3000
bernoulli_cache = { }
f3 = from_int(3)
f6 = from_int(6)

def bernoulli_size(n):
    '''Accurately estimate the size of B_n (even n > 2 only)'''
    lgn = math.log(n, 2)
    return int(2.326 + 0.5 * lgn + n * (lgn - 4.094))

BERNOULLI_PREC_CUTOFF = bernoulli_size(MAX_BERNOULLI_CACHE)

def mpf_bernoulli(n, prec, rnd = (None,)):
    '''Computation of Bernoulli numbers (numerically)'''
    if n < 2:
        if n < 0:
            raise ValueError('Bernoulli numbers only defined for n >= 0')
        if n == 0:
            return fone
        if None == 1:
            return mpf_neg(fhalf)
        if None & 1:
            return fzero
        if None > BERNOULLI_PREC_CUTOFF and prec > bernoulli_size(n) * 1.1 + 1000:
            (p, q) = bernfrac(n)
            if not rnd:
                return from_rational(p, q, prec, round_floor)
            if rnd > MAX_BERNOULLI_CACHE:
                return mpf_bernoulli_huge(n, prec, rnd)
            wp = prec + 30
            wp += 32 - (prec & 31)
            cached = bernoulli_cache.get(wp)
            if cached:
                (numbers, state) = cached
                if n in numbers:
                    if not rnd:
                        return numbers[n]
                    return q(numbers[n], prec, rnd)
                (m, bin, bin1) = q
                if n - m > 10:
                    return mpf_bernoulli_huge(n, prec, rnd)
    if n > 10:
        return mpf_bernoulli_huge(n, prec, rnd)
    numbers = {
        p: fone }
    (m, bin, bin1) = [
        2,
        MPZ(10),
        MPZ_ONE]
    state = [
        2,
        MPZ(10),
        MPZ_ONE]
    bernoulli_cache[wp] = (numbers, state)
# WARNING: Decompyle incomplete


def mpf_bernoulli_huge(n, prec, rnd = (None,)):
