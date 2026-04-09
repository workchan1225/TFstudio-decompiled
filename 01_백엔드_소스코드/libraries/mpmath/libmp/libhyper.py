# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: libhyper.pyc (Python 3.11)

'''
This module implements computation of hypergeometric and related
functions. In particular, it provides code for generic summation
of hypergeometric series. Optimized versions for various special
cases are also provided.
'''
import operator
import math
from backend import MPZ_ZERO, MPZ_ONE, BACKEND, xrange, exec_
from libintmath import gcd
from libmpf import ComplexResult, round_fast, round_nearest, negative_rnd, bitcount, to_fixed, from_man_exp, from_int, to_int, from_rational, fzero, fone, fnone, ftwo, finf, fninf, fnan, mpf_sign, mpf_add, mpf_abs, mpf_pos, mpf_cmp, mpf_lt, mpf_le, mpf_gt, mpf_min_max, mpf_perturb, mpf_neg, mpf_shift, mpf_sub, mpf_mul, mpf_div, sqrt_fixed, mpf_sqrt, mpf_rdiv_int, mpf_pow_int, to_rational
from libelefun import mpf_pi, mpf_exp, mpf_log, pi_fixed, mpf_cos_sin, mpf_cos, mpf_sin, mpf_sqrt, agm_fixed
from libmpc import mpc_one, mpc_sub, mpc_mul_mpf, mpc_mul, mpc_neg, complex_int_pow, mpc_div, mpc_add_mpf, mpc_sub_mpf, mpc_log, mpc_add, mpc_pos, mpc_shift, mpc_is_infnan, mpc_zero, mpc_sqrt, mpc_abs, mpc_mpf_div, mpc_square, mpc_exp
from libintmath import ifac
from gammazeta import mpf_gamma_int, mpf_euler, euler_fixed

class NoConvergence(Exception):
    pass


def make_hyp_summator(key):
    '''
    Returns a function that sums a generalized hypergeometric series,
    for given parameter types (integer, rational, real, complex).

    '''
    (p, q, param_types, ztype) = key
    pstring = ''.join(param_types)
    fname = 'hypsum_%i_%i_%s_%s_%s' % (p, q, pstring[:p], pstring[p:], ztype)
    have_complex_param = 'C' in param_types
    have_complex_arg = ztype == 'C'
    if not have_complex_param:
        have_complex = have_complex_arg
        source = []
        add = source.append
        aint = []
        arat = []
        bint = []
        brat = []
        areal = []
        breal = []
        acomplex = []
        bcomplex = []
        add("MAX = kwargs.get('maxterms', wp*100)")
        add('HIGH = MPZ_ONE<<epsshift')
        add('LOW = -HIGH')
        add('SRE = PRE = one = (MPZ_ONE << wp)')
        if have_complex:
            add('SIM = PIM = MPZ_ZERO')
    if have_complex_arg:
        add('xsign, xm, xe, xbc = z[0]')
        add('if xsign: xm = -xm')
        add('ysign, ym, ye, ybc = z[1]')
        add('if ysign: ym = -ym')
    else:
        add('xsign, xm, xe, xbc = z')
        add('if xsign: xm = -xm')
    add('offset = xe + wp')
    add('if offset >= 0:')
    add('    ZRE = xm << offset')
    add('else:')
    add('    ZRE = xm >> (-offset)')
    if have_complex_arg:
        add('offset = ye + wp')
        add('if offset >= 0:')
        add('    ZIM = ym << offset')
        add('else:')
        add('    ZIM = ym >> (-offset)')
    for i, flag in enumerate(param_types):
        W = [
            'A',
            'B'][i >= p]
        if flag == 'Z':
            [
                aint,
                bint][i >= p].append(i)
            add('%sINT_%i = coeffs[%i]' % (W, i, i))
            continue
        if flag == 'Q':
            [
                arat,
                brat][i >= p].append(i)
            add('%sP_%i, %sQ_%i = coeffs[%i]._mpq_' % (W, i, W, i, i))
            continue
        if flag == 'R':
            [
                areal,
                breal][i >= p].append(i)
            add('xsign, xm, xe, xbc = coeffs[%i]._mpf_' % i)
            add('if xsign: xm = -xm')
            add('offset = xe + wp')
            add('if offset >= 0:')
            add('    %sREAL_%i = xm << offset' % (W, i))
            add('else:')
            add('    %sREAL_%i = xm >> (-offset)' % (W, i))
            continue
        if flag == 'C':
            [
                acomplex,
                bcomplex][i >= p].append(i)
            add('__re, __im = coeffs[%i]._mpc_' % i)
            add('xsign, xm, xe, xbc = __re')
            add('if xsign: xm = -xm')
            add('ysign, ym, ye, ybc = __im')
            add('if ysign: ym = -ym')
            add('offset = xe + wp')
            add('if offset >= 0:')
            add('    %sCRE_%i = xm << offset' % (W, i))
            add('else:')
            add('    %sCRE_%i = xm >> (-offset)' % (W, i))
            add('offset = ye + wp')
            add('if offset >= 0:')
            add('    %sCIM_%i = ym << offset' % (W, i))
            add('else:')
            add('    %sCIM_%i = ym >> (-offset)' % (W, i))
            continue
        raise ValueError
        l_areal = len(areal)
        l_breal = len(breal)
        cancellable_real = min(l_areal, l_breal)
        noncancellable_real_num = areal[cancellable_real:]
        noncancellable_real_den = breal[cancellable_real:]
        add('for n in xrange(1,10**8):')
        add('    if n in magnitude_check:')
        add('        p_mag = bitcount(abs(PRE))')
        if have_complex:
            add('        p_mag = max(p_mag, bitcount(abs(PIM)))')
    add('        magnitude_check[n] = wp-p_mag')
    multiplier = (lambda .0: [ 'AP_#'.replace('#', str(i)) for i in .0 ]) + arat()((lambda .0: [ 'BQ_#'.replace('#', str(i)) for i in .0 ]) + brat())
    divisor = (lambda .0: [ 'BP_#'.replace('#', str(i)) for i in .0 ]) + brat()((lambda .0: [ 'AQ_#'.replace('#', str(i)) for i in .0 ]) + arat() + [
        'n'])
    if multiplier:
        add('    mul = ' + multiplier)
    add('    div = ' + divisor)
    add('    if not div:')
    if multiplier:
        add('        if not mul:')
        add('            break')
    add('        raise ZeroDivisionError')
    if have_complex:
        for k in range(cancellable_real):
            add('    PRE = PRE * AREAL_%i // BREAL_%i' % (areal[k], breal[k]))
            for i in noncancellable_real_num:
                add('    PRE = (PRE * AREAL_#) >> wp'.replace('#', str(i)))
                for i in noncancellable_real_den:
                    add('    PRE = (PRE << wp) // BREAL_#'.replace('#', str(i)))
                    for k in range(cancellable_real):
                        add('    PIM = PIM * AREAL_%i // BREAL_%i' % (areal[k], breal[k]))
                        for i in noncancellable_real_num:
                            add('    PIM = (PIM * AREAL_#) >> wp'.replace('#', str(i)))
                            for i in noncancellable_real_den:
                                add('    PIM = (PIM << wp) // BREAL_#'.replace('#', str(i)))
                                if multiplier:
                                    if have_complex_arg:
                                        add('    PRE, PIM = (mul*(PRE*ZRE-PIM*ZIM))//div, (mul*(PIM*ZRE+PRE*ZIM))//div')
                                        add('    PRE >>= wp')
                                        add('    PIM >>= wp')
                                    else:
                                        add('    PRE = ((mul * PRE * ZRE) >> wp) // div')
                                        add('    PIM = ((mul * PIM * ZRE) >> wp) // div')
                                elif have_complex_arg:
                                    add('    PRE, PIM = (PRE*ZRE-PIM*ZIM)//div, (PIM*ZRE+PRE*ZIM)//div')
                                    add('    PRE >>= wp')
                                    add('    PIM >>= wp')
                                else:
                                    add('    PRE = ((PRE * ZRE) >> wp) // div')
                                    add('    PIM = ((PIM * ZRE) >> wp) // div')
        for i in acomplex:
            add('    PRE, PIM = PRE*ACRE_#-PIM*ACIM_#, PIM*ACRE_#+PRE*ACIM_#'.replace('#', str(i)))
            add('    PRE >>= wp')
            add('    PIM >>= wp')
            for i in bcomplex:
                add('    mag = BCRE_#*BCRE_#+BCIM_#*BCIM_#'.replace('#', str(i)))
                add('    re = PRE*BCRE_# + PIM*BCIM_#'.replace('#', str(i)))
                add('    im = PIM*BCRE_# - PRE*BCIM_#'.replace('#', str(i)))
                add('    PRE = (re << wp) // mag'.replace('#', str(i)))
                add('    PIM = (im << wp) // mag'.replace('#', str(i)))
            for k in range(cancellable_real):
                add('    PRE = PRE * AREAL_%i // BREAL_%i' % (areal[k], breal[k]))
                for i in noncancellable_real_num:
                    add('    PRE = (PRE * AREAL_#) >> wp'.replace('#', str(i)))
                    for i in noncancellable_real_den:
                        add('    PRE = (PRE << wp) // BREAL_#'.replace('#', str(i)))
    add('    if n > MAX:')
    add("        raise NoConvergence('Hypergeometric series converges too slowly. Try increasing maxterms.')")
    for i in aint:
        add('    AINT_# += 1'.replace('#', str(i)))
        for i in bint:
            add('    BINT_# += 1'.replace('#', str(i)))
            for i in arat:
                add('    AP_# += AQ_#'.replace('#', str(i)))
                for i in brat:
                    add('    BP_# += BQ_#'.replace('#', str(i)))
                    for i in areal:
                        add('    AREAL_# += one'.replace('#', str(i)))
                        for i in breal:
                            add('    BREAL_# += one'.replace('#', str(i)))
                            for i in acomplex:
                                add('    ACRE_# += one'.replace('#', str(i)))
                                for i in bcomplex:
                                    add('    BCRE_# += one'.replace('#', str(i)))
    source = (lambda .0: pass# WARNING: Decompyle incomplete
)(source())
    source = 'def %s(coeffs, z, prec, wp, epsshift, magnitude_check, **kwargs):\n' % fname + source
    namespace = { }
    exec_(source, globals(), namespace)
    return (source, namespace[fname])

if BACKEND == 'sage':
    
    def make_hyp_summator(key):
        '''
        Returns a function that sums a generalized hypergeometric series,
        for given parameter types (integer, rational, real, complex).
        '''
        pass
    # WARNING: Decompyle incomplete


def mpf_erf(x, prec, rnd = (round_fast,)):
    (sign, man, exp, bc) = x
    if not man:
        if x == fzero:
            return fzero
        if None == finf:
            return fone
        if None == fninf:
            return fnone
        return None
    size = None + bc
    lg = math.log
    if size > 3 and 2 * (size - 1) + 0.528766 > lg(prec, 2):
        if sign:
            return mpf_perturb(fnone, 0, prec, rnd)
        return None(fone, 1, prec, rnd)
    if None < -prec:
        x = mpf_shift(x, 1)
        c = mpf_sqrt(mpf_pi(prec + 20), prec + 20)
        return mpf_div(x, c, prec, rnd)
    wp = None + abs(size) + 25
    t = abs(to_fixed(x, wp))
    t2 = t * t >> wp
    k = 1
    term = 12345
    s = t
# WARNING: Decompyle incomplete


def erfc_check_series(x, prec):
    n = to_int(x)
    if n ** 2 * 1.44 > prec:
        return True


def mpf_erfc(x, prec, rnd = (round_fast,)):
    (sign, man, exp, bc) = x
    if not man:
        if x == fzero:
            return fone
        if None == finf:
            return fzero
        if None == fninf:
            return ftwo
        return None
    wp = None + 20
    mag = bc + exp
    wp += max(0, 2 * mag)
    if not sign:
        regular_erf = mag < 2
        if not regular_erf or erfc_check_series(x, wp):
            if regular_erf:
                return mpf_sub(fone, mpf_erf(x, prec + 10, negative_rnd[rnd]), prec, rnd)
            n = None(x) + 1
            return mpf_sub(fone, mpf_erf(x, prec + int(n ** 2 * 1.44) + 10), prec, rnd)
        s = None << wp
        term = None << wp
        term_prev = 0
        t = 2 * to_fixed(x, wp) ** 2 >> wp
        k = 1
        term = (term * (2 * k - 1) << wp) // t
        if not k > 4 or term > term_prev or term:
            pass
        elif k & 1:
            s -= term
        else:
            s += term
    term_prev = term
    k += 1
    continue
    s = (s << wp) // sqrt_fixed(pi_fixed(wp), wp)
    s = from_man_exp(s, -wp, wp)
    z = mpf_exp(mpf_neg(mpf_mul(x, x, wp), wp), wp)
    y = mpf_div(mpf_mul(z, s, wp), x, prec, rnd)
    return y


def ei_taylor(x, prec):
    s = x
    t = x
    k = 2
# WARNING: Decompyle incomplete


def complex_ei_taylor(zre, zim, prec):
    _abs = abs
    sre = zre
    tre = zre
    sim = zim
    tim = zim
    k = 2
# WARNING: Decompyle incomplete


def ei_asymptotic(x, prec):
    one = MPZ_ONE << prec
    x = (one << prec) // x
    t = (one << prec) // x
    s = one + x
    k = 2
# WARNING: Decompyle incomplete


def complex_ei_asymptotic(zre, zim, prec):
    _abs = abs
    one = MPZ_ONE << prec
    M = zim * zim + zre * zre >> prec
    xre = (zre << prec) // M
    tre = (zre << prec) // M
    xim = (-zim << prec) // M
    tim = (-zim << prec) // M
    sre = one + xre
    sim = xim
    k = 2
# WARNING: Decompyle incomplete


def mpf_ei(x, prec, rnd, e1 = (round_fast, False)):
    if e1:
        x = mpf_neg(x)
    (sign, man, exp, bc) = x
    if not e1 and sign:
        if x == fzero:
            return finf
        raise None('E1(x) for x < 0')
    if man:
        xabs = (0, man, exp, bc)
        xmag = exp + bc
        wp = prec + 20
        can_use_asymp = xmag > wp
        if not can_use_asymp:
            if exp >= 0:
                xabsint = man << exp
            else:
                xabsint = man >> -exp
            can_use_asymp = xabsint > int(wp * 0.693) + 10
        if can_use_asymp:
            if xmag > wp:
                v = fone
            else:
                v = from_man_exp(ei_asymptotic(to_fixed(x, wp), wp), -wp)
            v = mpf_mul(v, mpf_exp(x, wp), wp)
            v = mpf_div(v, x, prec, rnd)
        else:
            wp += 2 * int(to_int(xabs))
            u = to_fixed(x, wp)
            v = ei_taylor(u, wp) + euler_fixed(wp)
            t1 = from_man_exp(v, -wp)
            t2 = mpf_log(xabs, wp)
            v = mpf_add(t1, t2, prec, rnd)
    elif x == fzero:
        v = fninf
    elif x == finf:
        v = finf
    elif x == fninf:
        v = fzero
    else:
        v = fnan
    if e1:
        v = mpf_neg(v)
    return v


def mpc_ei(z, prec, rnd, e1 = (round_fast, False)):
    if e1:
        z = mpc_neg(z)
    (a, b) = z
    (asign, aman, aexp, abc) = a
    (bsign, bman, bexp, bbc) = b
    if b == fzero:
        if e1:
            x = mpf_neg(mpf_ei(a, prec, rnd))
            if not asign:
                y = mpf_neg(mpf_pi(prec, rnd))
            else:
                y = fzero
            return (x, y)
        return (None(a, prec, rnd), fzero)
    if None != fzero:
        if not aman or bman:
            return (fnan, fnan)
        wp = None + 40
        amag = aexp + abc
        bmag = bexp + bbc
        zmag = max(amag, bmag)
        can_use_asymp = zmag > wp
        if not can_use_asymp:
            zabsint = abs(to_int(a)) + abs(to_int(b))
            can_use_asymp = zabsint > int(wp * 0.693) + 20
    
    try:
        if can_use_asymp:
            if zmag > wp:
                v = (fone, fzero)
            else:
                zre = to_fixed(a, wp)
                zim = to_fixed(b, wp)
                (vre, vim) = complex_ei_asymptotic(zre, zim, wp)
                v = (from_man_exp(vre, -wp), from_man_exp(vim, -wp))
            v = mpc_mul(v, mpc_exp(z, wp), wp)
            v = mpc_div(v, z, wp)
            if e1:
                v = mpc_neg(v, prec, rnd)
            else:
                (x, y) = v
                if bsign:
                    v = (mpf_pos(x, prec, rnd), mpf_sub(y, mpf_pi(wp), prec, rnd))
                else:
                    v = (mpf_pos(x, prec, rnd), mpf_add(y, mpf_pi(wp), prec, rnd))
            return v
    except NoConvergence:
        pass

    wp += 2 * int(to_int(mpc_abs(z, 5)))
    zre = to_fixed(a, wp)
    zim = to_fixed(b, wp)
    (vre, vim) = complex_ei_taylor(zre, zim, wp)
    vre += euler_fixed(wp)
    v = (from_man_exp(vre, -wp), from_man_exp(vim, -wp))
    if e1:
        u = mpc_log(mpc_neg(z), wp)
    else:
        u = mpc_log(z, wp)
    v = mpc_add(v, u, prec, rnd)
    if e1:
        v = mpc_neg(v)
    return v


def mpf_e1(x, prec, rnd = (round_fast,)):
    return mpf_ei(x, prec, rnd, True)


def mpc_e1(x, prec, rnd = (round_fast,)):
    return mpc_ei(x, prec, rnd, True)


def mpf_expint(n, x, prec, rnd, gamma = (round_fast, False)):
    '''
    E_n(x), n an integer, x real

    With gamma=True, computes Gamma(n,x)   (upper incomplete gamma function)

    Returns (real, None) if real, otherwise (real, imag)
    The imaginary part is an optional branch cut term

    '''
    (sign, man, exp, bc) = x
    if not man:
        if gamma:
            if x == fzero:
                if n <= 0:
                    return (finf, None)
                return (None(n, prec, rnd), None)
            if None == finf:
                return (fzero, None)
            return (None, fnan)
        if None == fzero:
            if n > 1:
                return (from_rational(1, n - 1, prec, rnd), None)
            return (None, None)
        if None == finf:
            return (fzero, None)
        return (None, fnan)
    n_orig = None
    if gamma:
        n = 1 - n
    wp = prec + 20
    xmag = exp + bc
    if xmag < -10:
        raise NotImplementedError
    nmag = bitcount(abs(n))
    if n > 0:
        have_imag = sign
        negx = mpf_neg(x)
        if n == 0 or 2 * nmag - xmag < -wp:
            if gamma:
                v = mpf_exp(negx, wp)
                re = mpf_mul(v, mpf_pow_int(x, n_orig - 1, wp), prec, rnd)
            else:
                v = mpf_exp(negx, wp)
                re = mpf_div(v, x, prec, rnd)
        elif  < -3 * wp, n:
            pass
        
    if not can_use_asymptotic_series:
        abs(to_int(x)) = -3 * wp, n,  < -3 * wp, n <= 0, can_use_asymptotic_series
        m = min(max(1, xi - n), 2 * wp)
        siz = -n * nmag + (m + n) * bitcount(abs(m + n)) - m * xmag - 144 * m // 100
        tol = -wp - 10
        can_use_asymptotic_series = siz < tol
# WARNING: Decompyle incomplete


def mpf_ci_si_taylor(x, wp, which = (0,)):
    '''
    0 - Ci(x) - (euler+log(x))
    1 - Si(x)
    '''
    x = to_fixed(x, wp)
    x2 = -(x * x) >> wp
    if which == 0:
        k = 2
        t = MPZ_ONE << wp
        s = 0
    else:
        k = 3
        t = x
        s = x
# WARNING: Decompyle incomplete


def mpc_ci_si_taylor(re, im, wp, which = (0,)):
    if re[1]:
        mag = re[2] + re[3]
    elif im[1]:
        mag = im[2] + im[3]
    if im[1]:
        mag = max(mag, im[2] + im[3])
    if mag > 2 or mag < -wp:
        raise NotImplementedError
    wp += 2 - mag
    zre = to_fixed(re, wp)
    zim = to_fixed(im, wp)
    z2re = zim * zim - zre * zre >> wp
    z2im = -2 * zre * zim >> wp
    tre = zre
    tim = zim
    one = MPZ_ONE << wp
    if which == 0:
        (sre, sim, tre, tim, k) = (0, 0, MPZ_ONE << wp, 0, 2)
    else:
        (sre, sim, tre, tim, k) = (zre, zim, zre, zim, 3)
# WARNING: Decompyle incomplete


def mpf_ci_si(x, prec, rnd, which = (round_fast, 2)):
    '''
    Calculation of Ci(x), Si(x) for real x.

    which = 0 -- returns (Ci(x), -)
    which = 1 -- returns (Si(x), -)
    which = 2 -- returns (Ci(x), Si(x))

    Note: if x < 0, Ci(x) needs an additional imaginary term, pi*i.
    '''
    wp = prec + 20
    (sign, man, exp, bc) = x
    (ci, si) = (None, None)
    if not man:
        if x == fzero:
            return (fninf, fzero)
        if None == fnan:
            return (x, x)
        ci = None
        if which != 0:
            if x == finf:
                si = mpf_shift(mpf_pi(prec, rnd), -1)
            if x == fninf:
                si = mpf_neg(mpf_shift(mpf_pi(prec, negative_rnd[rnd]), -1))
        return (ci, si)
    mag = None + bc
    if mag < -wp:
        if which != 0:
            si = mpf_perturb(x, 1 - sign, prec, rnd)
        if which != 1:
            y = mpf_euler(wp)
            xabs = mpf_abs(x)
            ci = mpf_add(y, mpf_log(xabs, wp), prec, rnd)
        return (ci, si)
    if None > wp:
        if which != 0:
            if sign:
                si = mpf_neg(mpf_pi(prec, negative_rnd[rnd]))
            else:
                si = mpf_pi(prec, rnd)
            si = mpf_shift(si, -1)
        if which != 1:
            ci = mpf_div(mpf_sin(x, wp), x, prec, rnd)
        return (ci, si)
    None += abs(mag)
    asymptotic = mag - 1 > math.log(wp, 2)
    if not asymptotic:
        if which != 0:
            si = mpf_pos(mpf_ci_si_taylor(x, wp, 1), prec, rnd)
        if which != 1:
            ci = mpf_ci_si_taylor(x, wp, 0)
            ci = mpf_add(ci, mpf_euler(wp), wp)
            ci = mpf_add(ci, mpf_log(mpf_abs(x), wp), prec, rnd)
        return (ci, si)
    x = None(x)
    xf = to_fixed(x, wp)
    xr = (MPZ_ONE << 2 * wp) // xf
    s1 = MPZ_ONE << wp
    s2 = xr
    t = xr
    k = 2
# WARNING: Decompyle incomplete


def mpf_ci(x, prec, rnd = (round_fast,)):
    if mpf_sign(x) < 0:
        raise ComplexResult
    return mpf_ci_si(x, prec, rnd, 0)[0]


def mpf_si(x, prec, rnd = (round_fast,)):
    return mpf_ci_si(x, prec, rnd, 1)[1]


def mpc_ci(z, prec, rnd = (round_fast,)):
    (re, im) = z
    if im == fzero:
        ci = mpf_ci_si(re, prec, rnd, 0)[0]
        if mpf_sign(re) < 0:
            return (ci, mpf_pi(prec, rnd))
        return (None, fzero)
    wp = None + 20
    (cre, cim) = mpc_ci_si_taylor(re, im, wp, 0)
    cre = mpf_add(cre, mpf_euler(wp), wp)
    ci = mpc_add((cre, cim), mpc_log(z, wp), prec, rnd)
    return ci


def mpc_si(z, prec, rnd = (round_fast,)):
    (re, im) = z
    if im == fzero:
        return (mpf_ci_si(re, prec, rnd, 1)[1], fzero)
    wp = None + 20
    z = mpc_ci_si_taylor(re, im, wp, 1)
    return mpc_pos(z, prec, rnd)


def mpf_besseljn(n, x, prec, rounding = (round_fast,)):
    prec += 50
    if n < 0:
        negate = n & 1
        mag = x[2] + x[3]
        n = abs(n)
        wp = prec + 20 + n * bitcount(n)
        if mag < 0:
            wp -= n * mag
    x = to_fixed(x, wp)
    x2 = x ** 2 >> wp
    if not n:
        s = MPZ_ONE << wp
        t = MPZ_ONE << wp
    else:
        s = x ** n // ifac(n) >> (n - 1) * wp + n
        t = x ** n // ifac(n) >> (n - 1) * wp + n
    k = 1
# WARNING: Decompyle incomplete


def mpc_besseljn(n, z, prec, rounding = (round_fast,)):
    if n < 0:
        negate = n & 1
        n = abs(n)
        origprec = prec
        (zre, zim) = z
        mag = max(zre[2] + zre[3], zim[2] + zim[3])
        prec += 20 + n * bitcount(n) + abs(mag)
        if mag < 0:
            prec -= n * mag
    zre = to_fixed(zre, prec)
    zim = to_fixed(zim, prec)
    z2re = zre ** 2 - zim ** 2 >> prec
    z2im = zre * zim >> prec - 1
    if not n:
        sre = MPZ_ONE << prec
        tre = MPZ_ONE << prec
        sim = MPZ_ZERO
        tim = MPZ_ZERO
    else:
        (re, im) = complex_int_pow(zre, zim, n)
        sre = re // ifac(n) >> (n - 1) * prec + n
        tre = re // ifac(n) >> (n - 1) * prec + n
        sim = im // ifac(n) >> (n - 1) * prec + n
        tim = im // ifac(n) >> (n - 1) * prec + n
    k = 1
# WARNING: Decompyle incomplete


def mpf_agm(a, b, prec, rnd = (round_fast,)):
    '''
    Computes the arithmetic-geometric mean agm(a,b) for
    nonnegative mpf values a, b.
    '''
    (asign, aman, aexp, abc) = a
    (bsign, bman, bexp, bbc) = b
    if asign or bsign:
        raise ComplexResult('agm of a negative number')
    if not aman or bman:
        if a == fnan or b == fnan:
            return fnan
        if None == finf:
            if b == fzero:
                return fnan
            return None
        if None == finf:
            if a == fzero:
                return fnan
            return None
        return None
    wp = None + 20
    amag = aexp + abc
    bmag = bexp + bbc
    mag_delta = amag - bmag
    abs_mag_delta = abs(mag_delta)
# WARNING: Decompyle incomplete


def mpf_agm1(a, prec, rnd = (round_fast,)):
    '''
    Computes the arithmetic-geometric mean agm(1,a) for a nonnegative
    mpf value a.
    '''
    return mpf_agm(fone, a, prec, rnd)


def mpc_agm(a, b, prec, rnd = (round_fast,)):
    '''
    Complex AGM.

    TODO:
    * check that convergence works as intended
    * optimize
    * select a nonarbitrary branch
    '''
    if mpc_is_infnan(a) or mpc_is_infnan(b):
        return (fnan, fnan)
    if None in (a, b):
        return (fzero, fzero)
    if None(a) == b:
        return (fzero, fzero)
    wp = None + 20
    eps = mpf_shift(fone, -wp + 10)
    a1 = mpc_shift(mpc_add(a, b, wp), -1)
    b1 = mpc_sqrt(mpc_mul(a, b, wp), wp)
    b = b1
    a = a1
    size = mpf_min_max([
        mpc_abs(a, 10),
        mpc_abs(b, 10)])[1]
    err = mpc_abs(mpc_sub(a, b, 10), 10)
    if size == fzero or mpf_lt(err, mpf_mul(eps, size)):
        return a


def mpc_agm1(a, prec, rnd = (round_fast,)):
    return mpc_agm(mpc_one, a, prec, rnd)


def mpf_ellipk(x, prec, rnd = (round_fast,)):
