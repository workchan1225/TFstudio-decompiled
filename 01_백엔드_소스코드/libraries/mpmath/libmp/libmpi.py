# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: libmpi.pyc (Python 3.11)

'''
Computational functions for interval arithmetic.

'''
from backend import xrange
from libmpf import ComplexResult, round_down, round_up, round_floor, round_ceiling, round_nearest, prec_to_dps, repr_dps, dps_to_prec, bitcount, from_float, fnan, finf, fninf, fzero, fhalf, fone, fnone, mpf_sign, mpf_lt, mpf_le, mpf_gt, mpf_ge, mpf_eq, mpf_cmp, mpf_min_max, mpf_floor, from_int, to_int, to_str, from_str, mpf_abs, mpf_neg, mpf_pos, mpf_add, mpf_sub, mpf_mul, mpf_mul_int, mpf_div, mpf_shift, mpf_pow_int, from_man_exp, MPZ_ONE
from libelefun import mpf_log, mpf_exp, mpf_sqrt, mpf_atan, mpf_atan2, mpf_pi, mod_pi2, mpf_cos_sin
from gammazeta import mpf_gamma, mpf_rgamma, mpf_loggamma, mpc_loggamma

def mpi_str(s, prec):
    (sa, sb) = s
    dps = prec_to_dps(prec) + 5
    return f'''[{to_str(sa, dps)!s}, {to_str(sb, dps)!s}]'''

mpi_zero = (fzero, fzero)
mpi_one = (fone, fone)

def mpi_eq(s, t):
    return s == t


def mpi_ne(s, t):
    return s != t


def mpi_lt(s, t):
    (sa, sb) = s
    (ta, tb) = t
    if mpf_lt(sb, ta):
        return True
    if None(sa, tb):
        return False


def mpi_le(s, t):
    (sa, sb) = s
    (ta, tb) = t
    if mpf_le(sb, ta):
        return True
    if None(sa, tb):
        return False


def mpi_gt(s, t):
    return mpi_lt(t, s)


def mpi_ge(s, t):
    return mpi_le(t, s)


def mpi_add(s, t, prec = (0,)):
    (sa, sb) = s
    (ta, tb) = t
    a = mpf_add(sa, ta, prec, round_floor)
    b = mpf_add(sb, tb, prec, round_ceiling)
    if a == fnan:
        a = fninf
    if b == fnan:
        b = finf
    return (a, b)


def mpi_sub(s, t, prec = (0,)):
    (sa, sb) = s
    (ta, tb) = t
    a = mpf_sub(sa, tb, prec, round_floor)
    b = mpf_sub(sb, ta, prec, round_ceiling)
    if a == fnan:
        a = fninf
    if b == fnan:
        b = finf
    return (a, b)


def mpi_delta(s, prec):
    (sa, sb) = s
    return mpf_sub(sb, sa, prec, round_up)


def mpi_mid(s, prec):
    (sa, sb) = s
    return mpf_shift(mpf_add(sa, sb, prec, round_nearest), -1)


def mpi_pos(s, prec):
    (sa, sb) = s
    a = mpf_pos(sa, prec, round_floor)
    b = mpf_pos(sb, prec, round_ceiling)
    return (a, b)


def mpi_neg(s, prec = (0,)):
    (sa, sb) = s
    a = mpf_neg(sb, prec, round_floor)
    b = mpf_neg(sa, prec, round_ceiling)
    return (a, b)


def mpi_abs(s, prec = (0,)):
    (sa, sb) = s
    sas = mpf_sign(sa)
    sbs = mpf_sign(sb)
    if sas >= 0:
        a = mpf_pos(sa, prec, round_floor)
        b = mpf_pos(sb, prec, round_ceiling)
    elif sbs >= 0:
        a = fzero
        negsa = mpf_neg(sa)
        if mpf_lt(negsa, sb):
            b = mpf_pos(sb, prec, round_ceiling)
        else:
            b = mpf_pos(negsa, prec, round_ceiling)
    else:
        a = mpf_neg(sb, prec, round_floor)
        b = mpf_neg(sa, prec, round_ceiling)
    return (a, b)


def mpi_mul_mpf(s, t, prec):
    return mpi_mul(s, (t, t), prec)


def mpi_div_mpf(s, t, prec):
    return mpi_div(s, (t, t), prec)


def mpi_mul(s, t, prec = (0,)):
    (sa, sb) = s
    (ta, tb) = t
    sas = mpf_sign(sa)
    sbs = mpf_sign(sb)
    tas = mpf_sign(ta)
    tbs = mpf_sign(tb)
    if  == sas, sbs or sas, sbs == 0:
        pass
    
    if ta == fninf or tb == finf:
        return (fninf, finf)
    return (None, fzero)
    if  == tas, tbs or tas, tbs == 0:
        pass
    
    if sa == fninf or sb == finf:
        return (fninf, finf)
    return (None, fzero)
    if sas >= 0:
        if tas >= 0:
            mpf_mul(sb, tb, prec, round_ceiling) = mpf_mul(sa, ta, prec, round_floor)
            if a == fnan:
                a = fzero
            if b == fnan:
                b = finf
            elif tbs <= 0:
                a = mpf_mul(sb, ta, prec, round_floor)
                b = mpf_mul(sa, tb, prec, round_ceiling)
                if a == fnan:
                    a = fninf
                if b == fnan:
                    b = fzero
                else:
                    a = mpf_mul(sb, ta, prec, round_floor)
                    b = mpf_mul(sb, tb, prec, round_ceiling)
                    if a == fnan:
                        a = fninf
                    if b == fnan:
                        b = finf
                    elif sbs <= 0:
                        if tas >= 0:
                            a = mpf_mul(sa, tb, prec, round_floor)
                            b = mpf_mul(sb, ta, prec, round_ceiling)
                            if a == fnan:
                                a = fninf
                            if b == fnan:
                                b = fzero
                            elif tbs <= 0:
                                a = mpf_mul(sb, tb, prec, round_floor)
                                b = mpf_mul(sa, ta, prec, round_ceiling)
                                if a == fnan:
                                    a = fzero
                                if b == fnan:
                                    b = finf
                                else:
                                    a = mpf_mul(sa, tb, prec, round_floor)
                                    b = mpf_mul(sa, ta, prec, round_ceiling)
                                    if a == fnan:
                                        a = fninf
                                    if b == fnan:
                                        b = finf
                                    else:
                                        cases = [
                                            mpf_mul(sa, ta),
                                            mpf_mul(sa, tb),
                                            mpf_mul(sb, ta),
                                            mpf_mul(sb, tb)]
                                        if fnan in cases:
                                            b = finf
                                            a = fninf
                                        else:
                                            (a, b) = mpf_min_max(cases)
                                            a = mpf_pos(a, prec, round_floor)
                                            b = mpf_pos(b, prec, round_ceiling)
    return (a, b)


def mpi_square(s, prec = (0,)):
    (sa, sb) = s
    if mpf_ge(sa, fzero):
        a = mpf_mul(sa, sa, prec, round_floor)
        b = mpf_mul(sb, sb, prec, round_ceiling)
    elif mpf_le(sb, fzero):
        a = mpf_mul(sb, sb, prec, round_floor)
        b = mpf_mul(sa, sa, prec, round_ceiling)
    else:
        sa = mpf_neg(sa)
        (sa, sb) = mpf_min_max([
            sa,
            sb])
        a = fzero
        b = mpf_mul(sb, sb, prec, round_ceiling)
    return (a, b)


def mpi_div(s, t, prec):
    (sa, sb) = s
    (ta, tb) = t
    sas = mpf_sign(sa)
    sbs = mpf_sign(sb)
    tas = mpf_sign(ta)
    tbs = mpf_sign(tb)
    if  == sas, sbs or sas, sbs == 0:
        pass
    
    if (tas < 0 or tbs > 0) and tas == 0 or tbs == 0:
        return (fninf, finf)
    return (None, fzero)
    if tas < 0 and tbs > 0:
        return (fninf, finf)
    if None < 0:
        return mpi_div(mpi_neg(s), mpi_neg(t), prec)
    if None == 0:
        if sas < 0 and sbs > 0:
            return (fninf, finf)
        if None == tbs:
            return (fninf, finf)
        if None >= 0:
            finf = mpf_div(sa, tb, prec, round_floor)
        if sbs <= 0:
            a = fninf
            b = mpf_div(sb, tb, prec, round_ceiling)
        elif sas >= 0:
            a = mpf_div(sa, tb, prec, round_floor)
            b = mpf_div(sb, ta, prec, round_ceiling)
            if a == fnan:
                a = fzero
            if b == fnan:
                b = finf
            elif sbs <= 0:
                a = mpf_div(sa, ta, prec, round_floor)
                b = mpf_div(sb, tb, prec, round_ceiling)
                if a == fnan:
                    a = fninf
                if b == fnan:
                    b = fzero
                else:
                    a = mpf_div(sa, ta, prec, round_floor)
                    b = mpf_div(sb, ta, prec, round_ceiling)
                    if a == fnan:
                        a = fninf
                    if b == fnan:
                        b = finf
    return (a, b)


def mpi_pi(prec):
    a = mpf_pi(prec, round_floor)
    b = mpf_pi(prec, round_ceiling)
    return (a, b)


def mpi_exp(s, prec):
    (sa, sb) = s
    a = mpf_exp(sa, prec, round_floor)
    b = mpf_exp(sb, prec, round_ceiling)
    return (a, b)


def mpi_log(s, prec):
    (sa, sb) = s
    a = mpf_log(sa, prec, round_floor)
    b = mpf_log(sb, prec, round_ceiling)
    return (a, b)


def mpi_sqrt(s, prec):
    (sa, sb) = s
    a = mpf_sqrt(sa, prec, round_floor)
    b = mpf_sqrt(sb, prec, round_ceiling)
    return (a, b)


def mpi_atan(s, prec):
    (sa, sb) = s
    a = mpf_atan(sa, prec, round_floor)
    b = mpf_atan(sb, prec, round_ceiling)
    return (a, b)


def mpi_pow_int(s, n, prec):
    (sa, sb) = s
    if n < 0:
        return mpi_div((fone, fone), mpi_pow_int(s, -n, prec + 20), prec)
    if None == 0:
        return (fone, fone)
    if None == 1:
        return s
    if None == 2:
        return mpi_square(s, prec)
    if None & 1:
        a = mpf_pow_int(sa, n, prec, round_floor)
        b = mpf_pow_int(sb, n, prec, round_ceiling)
    else:
        sas = mpf_sign(sa)
        sbs = mpf_sign(sb)
        if sas >= 0:
            a = mpf_pow_int(sa, n, prec, round_floor)
            b = mpf_pow_int(sb, n, prec, round_ceiling)
        elif sbs <= 0:
            a = mpf_pow_int(sb, n, prec, round_floor)
            b = mpf_pow_int(sa, n, prec, round_ceiling)
        else:
            a = fzero
            sa = mpf_neg(sa)
            if mpf_ge(sa, sb):
                b = mpf_pow_int(sa, n, prec, round_ceiling)
            else:
                b = mpf_pow_int(sb, n, prec, round_ceiling)
    return (a, b)


def mpi_pow(s, t, prec):
