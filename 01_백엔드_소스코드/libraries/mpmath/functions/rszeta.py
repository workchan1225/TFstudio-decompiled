# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rszeta.pyc (Python 3.11)

"""
---------------------------------------------------------------------
.. sectionauthor:: Juan Arias de Reyna <arias@us.es>

This module implements zeta-related functions using the Riemann-Siegel
expansion: zeta_offline(s,k=0)

* coef(J, eps): Need in the computation of Rzeta(s,k)

* Rzeta_simul(s, der=0) computes Rzeta^(k)(s) and Rzeta^(k)(1-s) simultaneously
  for  0 <= k <= der. Used by zeta_offline and z_offline

* Rzeta_set(s, derivatives) computes Rzeta^(k)(s) for given derivatives, used by
  z_half(t,k) and zeta_half

* z_offline(w,k): Z(w) and its derivatives of order k <= 4
* z_half(t,k): Z(t) (Riemann Siegel function) and its derivatives of order k <= 4
* zeta_offline(s): zeta(s) and its derivatives of order k<= 4
* zeta_half(1/2+it,k):  zeta(s)  and its derivatives of order k<= 4

* rs_zeta(s,k=0) Computes zeta^(k)(s)   Unifies zeta_half and zeta_offline
* rs_z(w,k=0)    Computes Z^(k)(w)      Unifies z_offline and z_half
----------------------------------------------------------------------

This program uses Riemann-Siegel expansion even to compute
zeta(s) on points s = sigma + i t  with sigma arbitrary not
necessarily equal to 1/2.

It is founded on a new deduction of the formula, with rigorous
and sharp bounds for the  terms and rest of this expansion.

More information on the papers:

 J. Arias de Reyna, High Precision Computation of Riemann's
 Zeta Function by the Riemann-Siegel Formula I, II

 We refer to them as I, II.

 In them we shall find detailed explanation of all the
 procedure.

The program uses Riemann-Siegel expansion.
This  is useful when t is big, ( say  t > 10000 ).
The precision is limited, roughly it can compute zeta(sigma+it)
with an error less than exp(-c t) for some constant c depending
on sigma.  The program gives an error when the Riemann-Siegel
formula can not compute to the wanted precision.

"""
import math

class RSCache(object):
    
    def __init__(ctx):
        ctx._rs_cache = [
            0,
            10,
            { },
            { }]


from functions import defun

def _coef(ctx, J, eps):
    '''
    Computes the coefficients  `c_n`  for `0\\le n\\le 2J` with error less than eps

    **Definition**

    The coefficients c_n are defined by

    .. math ::

        \\begin{equation}
        F(z)=\\frac{e^{\\pi i
        \\bigl(\\frac{z^2}{2}+\\frac38\\bigr)}-i\\sqrt{2}\\cos\\frac{\\pi}{2}z}{2\\cos\\pi
        z}=\\sum_{n=0}^\\infty c_{2n} z^{2n}
        \\end{equation}

    they are computed applying the relation

    .. math ::

        \\begin{multline}
        c_{2n}=-\\frac{i}{\\sqrt{2}}\\Bigl(\\frac{\\pi}{2}\\Bigr)^{2n}
        \\sum_{k=0}^n\\frac{(-1)^k}{(2k)!}
        2^{2n-2k}\\frac{(-1)^{n-k}E_{2n-2k}}{(2n-2k)!}+\\\\
        +e^{3\\pi i/8}\\sum_{j=0}^n(-1)^j\\frac{
        E_{2j}}{(2j)!}\\frac{i^{n-j}\\pi^{n+j}}{(n-j)!2^{n-j+1}}.
        \\end{multline}
    '''
    newJ = J + 2
    neweps6 = eps / 2
    wpvw = max(ctx.mag(10 * (newJ + 3)), 4 * newJ + 5 - ctx.mag(neweps6))
    E = ctx._eulernum(2 * newJ)
    wppi = max(ctx.mag(40 * newJ), ctx.mag(newJ) + 3 + wpvw)
    ctx.prec = wppi
    pipower = { }
    pipower[0] = ctx.one
    pipower[1] = ctx.pi
    for n in range(2, 2 * newJ + 1):
        pipower[n] = pipower[n - 1] * ctx.pi
        ctx.prec = wpvw + 2
        v = { }
        w = { }
        for n in range(0, newJ + 1):
            va = -1 ** n * ctx._eulernum(2 * n)
            va = ctx.mpf(va) / ctx.fac(2 * n)
            v[n] = va * pipower[2 * n]
            for n in range(0, 2 * newJ + 1):
                wa = ctx.one / ctx.fac(n)
                wa = wa / 2 ** n
                w[n] = wa * pipower[n]
                ctx.prec = 15
                wpp1a = 9 - ctx.mag(neweps6)
                P1 = { }
                for n in range(0, newJ + 1):
                    ctx.prec = 15
                    wpp1 = max(ctx.mag(10 * (n + 4)), 4 * n + wpp1a)
                    ctx.prec = wpp1
                    sump = 0
                    for k in range(0, n + 1):
                        sump += -1 ** k * v[k] * w[2 * n - 2 * k]
                        P1[n] = -1 ** (n + 1) * ctx.j * sump
                        P2 = { }
                        for n in range(0, newJ + 1):
                            ctx.prec = 15
                            wpp2 = max(ctx.mag(10 * (n + 4)), 4 * n + wpp1a)
                            ctx.prec = wpp2
                            sump = 0
                            for k in range(0, n + 1):
                                sump += ctx.j ** (n - k) * v[k] * w[n - k]
                                P2[n] = sump
                                ctx.prec = 15
                                wpc0 = 5 - ctx.mag(neweps6)
                                wpc = max(6, 4 * newJ + wpc0)
                                ctx.prec = wpc
                                mu = ctx.sqrt(ctx.mpf('2')) / 2
                                nu = ctx.expjpi(0.375) / 2
                                c = { }
                                for n in range(0, newJ):
                                    ctx.prec = 15
                                    wpc = max(6, 4 * n + wpc0)
                                    ctx.prec = wpc
                                    c[2 * n] = mu * P1[n] + nu * P2[n]
                                    for n in range(1, 2 * newJ, 2):
                                        c[n] = 0
                                        return [
                                            newJ,
                                            neweps6,
                                            c,
                                            pipower]


def coef(ctx, J, eps):
    pass
# WARNING: Decompyle incomplete


def aux_M_Fp(ctx, xA, xeps4, a, xB1, xL):
    aux1 = 126.066 * xA / xeps4
    aux1 = ctx.ln(aux1)
    aux2 = (2 * ctx.ln(ctx.pi) + ctx.ln(xB1) + ctx.ln(a)) / 3 - ctx.ln(2 * ctx.pi) / 2
    m = 3 * xL - 3
    aux3 = (ctx.loggamma(m + 1) - ctx.loggamma(m / 3 + 2)) / 2 - ctx.loggamma((m + 1) / 2)
# WARNING: Decompyle incomplete


def aux_J_needed(ctx, xA, xeps4, a, xB1, xM):
    h1 = xeps4 / (632 * xA)
    h2 = xB1 * a * 126.313
    h2 = h1 * ctx.power(h2 / xM ** 2, (xM - 1) / 3) / xM
    h3 = min(h1, h2)
    return h3


def Rzeta_simul(ctx, s, der = (0,)):
    pass
# WARNING: Decompyle incomplete


def Rzeta_set(ctx, s, derivatives = ([
    0],)):
    '''
    Computes several derivatives of the auxiliary function of Riemann `R(s)`.

    **Definition**

    The function is defined by

    .. math ::

        \\begin{equation}
        {\\mathop{\\mathcal R }\\nolimits}(s)=
        \\int_{0\\swarrow1}\\frac{x^{-s} e^{\\pi i x^2}}{e^{\\pi i x}-
        e^{-\\pi i x}}\\,dx
        \\end{equation}

    To this function we apply the Riemann-Siegel expansion.
    '''
    pass
# WARNING: Decompyle incomplete


def z_half(ctx, t, der = (0,)):
    '''
    z_half(t,der=0) Computes Z^(der)(t)
    '''
    s = ctx.mpf('0.5') + ctx.j * t
    wpinitial = ctx.prec
    ctx.prec = 15
    tt = t / (2 * ctx.pi)
    wptheta = wpinitial + 1 + ctx.mag(3 * tt ** 1.5 * ctx.ln(tt))
    wpz = wpinitial + 1 + ctx.mag(12 * tt * ctx.ln(tt))
    ctx.prec = wptheta
    theta = ctx.siegeltheta(t)
    ctx.prec = wpz
    rz = Rzeta_set(ctx, s, range(der + 1))
    if der > 0:
        ps1 = ctx._re(ctx.psi(0, s / 2) / 2 - ctx.ln(ctx.pi) / 2)
    if der > 1:
        ps2 = ctx._re(ctx.j * ctx.psi(1, s / 2) / 4)
    if der > 2:
        ps3 = ctx._re(-ctx.psi(2, s / 2) / 8)
    if der > 3:
        ps4 = ctx._re(-(ctx.j) * ctx.psi(3, s / 2) / 16)
    exptheta = ctx.expj(theta)
    if der == 0:
        z = 2 * exptheta * rz[0]
    if der == 1:
        zf = (0+2j) * exptheta
        z = zf * (ps1 * rz[0] + rz[1])
    if der == 2:
        zf = 2 * exptheta
        z = -zf * (2 * rz[1] * ps1 + rz[0] * ps1 ** 2 + rz[2] - ctx.j * rz[0] * ps2)
    if der == 3:
        zf = (-0+-2j) * exptheta
        z = 3 * rz[1] * ps1 ** 2 + rz[0] * ps1 ** 3 + 3 * ps1 * rz[2]
        z = zf * ((z - (0+3j) * rz[1] * ps2 - (0+3j) * rz[0] * ps1 * ps2) + rz[3] - rz[0] * ps3)
    if der == 4:
        zf = 2 * exptheta
        z = 4 * rz[1] * ps1 ** 3 + rz[0] * ps1 ** 4 + 6 * ps1 ** 2 * rz[2]
        z = z - (0+12j) * rz[1] * ps1 * ps2 - (0+6j) * rz[0] * ps1 ** 2 * ps2 - (0+6j) * rz[2] * ps2 - 3 * rz[0] * ps2 * ps2
        z = (z + 4 * ps1 * rz[3] - 4 * rz[1] * ps3 - 4 * rz[0] * ps1 * ps3) + rz[4] + ctx.j * rz[0] * ps4
        z = zf * z
    ctx.prec = wpinitial
    return ctx._re(z)


def zeta_half(ctx, s, k = (0,)):
    '''
    zeta_half(s,k=0) Computes zeta^(k)(s) when Re s = 0.5
    '''
    wpinitial = ctx.prec
    sigma = ctx._re(s)
    t = ctx._im(s)
    ctx.prec = 53
    if sigma > 0:
        X = ctx.sqrt(abs(s))
    else:
        X = (2 * ctx.pi) ** (sigma - 1) * abs(1 - s) ** (0.5 - sigma)
    if sigma > 0:
        M1 = 2 * ctx.sqrt(t / (2 * ctx.pi))
    else:
        M1 = 4 * t * X
    abst = abs(0.5 - s)
    T = 2 * abst * math.log(abst)
    wpbasic = max(6, 3 + ctx.mag(t))
    wpbasic2 = 2 + ctx.mag(2.12 * M1 + 21.2 * M1 * X + 1.3 * M1 * X * T) + wpinitial + 1
    wpbasic = max(wpbasic, wpbasic2)
    wptheta = max(4, 3 + ctx.mag(2.7 * M1 * X) + wpinitial + 1)
    wpR = 3 + ctx.mag(1.1 + 2 * X) + wpinitial + 1
    ctx.prec = wptheta
    theta = ctx.siegeltheta(t - ctx.j * (sigma - ctx.mpf('0.5')))
    if k > 0:
        ps1 = ctx._re(ctx.psi(0, s / 2)) / 2 - ctx.ln(ctx.pi) / 2
    if k > 1:
        ps2 = -ctx._im(ctx.psi(1, s / 2)) / 4
    if k > 2:
        ps3 = -ctx._re(ctx.psi(2, s / 2)) / 8
    if k > 3:
        ps4 = ctx._im(ctx.psi(3, s / 2)) / 16
    ctx.prec = wpR
    xrz = Rzeta_set(ctx, s, range(k + 1))
    yrz = { }
    for chi in range(0, k + 1):
        yrz[chi] = ctx.conj(xrz[chi])
        ctx.prec = wpbasic
        exptheta = ctx.expj(-2 * theta)
        if k == 0:
            zv = xrz[0] + exptheta * yrz[0]
    if k == 1:
        zv1 = -yrz[1] - 2 * yrz[0] * ps1
        zv = xrz[1] + exptheta * zv1
    if k == 2:
        zv1 = 4 * yrz[1] * ps1 + 4 * yrz[0] * ps1 ** 2 + yrz[2] + (0+2j) * yrz[0] * ps2
        zv = xrz[2] + exptheta * zv1
    if k == 3:
        zv1 = -12 * yrz[1] * ps1 ** 2 - 8 * yrz[0] * ps1 ** 3 - 6 * yrz[2] * ps1 - (0+6j) * yrz[1] * ps2
        zv1 = (zv1 - (0+12j) * yrz[0] * ps1 * ps2 - yrz[3]) + 2 * yrz[0] * ps3
        zv = xrz[3] + exptheta * zv1
    if k == 4:
        zv1 = 32 * yrz[1] * ps1 ** 3 + 16 * yrz[0] * ps1 ** 4 + 24 * yrz[2] * ps1 ** 2
        zv1 = zv1 + (0+48j) * yrz[1] * ps1 * ps2 + (0+48j) * yrz[0] * ps1 ** 2 * ps2
        zv1 = (zv1 + (0+12j) * yrz[2] * ps2 - 12 * yrz[0] * ps2 ** 2) + 8 * yrz[3] * ps1 - 8 * yrz[1] * ps3
        zv1 = (zv1 - 16 * yrz[0] * ps1 * ps3) + yrz[4] - (0+2j) * yrz[0] * ps4
        zv = xrz[4] + exptheta * zv1
    ctx.prec = wpinitial
    return zv


def zeta_offline(ctx, s, k = (0,)):
    '''
    Computes zeta^(k)(s) off the line
    '''
    wpinitial = ctx.prec
    sigma = ctx._re(s)
    t = ctx._im(s)
    ctx.prec = 53
    if sigma > 0:
        X = ctx.power(abs(s), 0.5)
    else:
        X = ctx.power(2 * ctx.pi, sigma - 1) * ctx.power(abs(1 - s), 0.5 - sigma)
    if sigma > 0:
        M1 = 2 * ctx.sqrt(t / (2 * ctx.pi))
    else:
        M1 = 4 * t * X
    if 1 - sigma > 0:
        M2 = 2 * ctx.sqrt(t / (2 * ctx.pi))
    else:
        M2 = 4 * t * ctx.power(2 * ctx.pi, -sigma) * ctx.power(abs(s), sigma - 0.5)
    abst = abs(0.5 - s)
    T = 2 * abst * math.log(abst)
    wpbasic = max(6, 3 + ctx.mag(t))
    wpbasic2 = 2 + ctx.mag(2.12 * M1 + 21.2 * M2 * X + 1.3 * M2 * X * T) + wpinitial + 1
    wpbasic = max(wpbasic, wpbasic2)
    wptheta = max(4, 3 + ctx.mag(2.7 * M2 * X) + wpinitial + 1)
    wpR = 3 + ctx.mag(1.1 + 2 * X) + wpinitial + 1
    ctx.prec = wptheta
    theta = ctx.siegeltheta(t - ctx.j * (sigma - ctx.mpf('0.5')))
    s1 = s
    s2 = ctx.conj(1 - s1)
    ctx.prec = wpR
    (xrz, yrz) = Rzeta_simul(ctx, s, k)
    if k > 0:
        ps1 = (ctx.psi(0, s1 / 2) + ctx.psi(0, (1 - s1) / 2)) / 4 - ctx.ln(ctx.pi) / 2
    if k > 1:
        ps2 = ctx.j * (ctx.psi(1, s1 / 2) - ctx.psi(1, (1 - s1) / 2)) / 8
    if k > 2:
        ps3 = -(ctx.psi(2, s1 / 2) + ctx.psi(2, (1 - s1) / 2)) / 16
    if k > 3:
        ps4 = -(ctx.j) * (ctx.psi(3, s1 / 2) - ctx.psi(3, (1 - s1) / 2)) / 32
    ctx.prec = wpbasic
    exptheta = ctx.expj(-2 * theta)
    if k == 0:
        zv = xrz[0] + exptheta * yrz[0]
    if k == 1:
        zv1 = -yrz[1] - 2 * yrz[0] * ps1
        zv = xrz[1] + exptheta * zv1
    if k == 2:
        zv1 = 4 * yrz[1] * ps1 + 4 * yrz[0] * ps1 ** 2 + yrz[2] + (0+2j) * yrz[0] * ps2
        zv = xrz[2] + exptheta * zv1
    if k == 3:
        zv1 = -12 * yrz[1] * ps1 ** 2 - 8 * yrz[0] * ps1 ** 3 - 6 * yrz[2] * ps1 - (0+6j) * yrz[1] * ps2
        zv1 = (zv1 - (0+12j) * yrz[0] * ps1 * ps2 - yrz[3]) + 2 * yrz[0] * ps3
        zv = xrz[3] + exptheta * zv1
    if k == 4:
        zv1 = 32 * yrz[1] * ps1 ** 3 + 16 * yrz[0] * ps1 ** 4 + 24 * yrz[2] * ps1 ** 2
        zv1 = zv1 + (0+48j) * yrz[1] * ps1 * ps2 + (0+48j) * yrz[0] * ps1 ** 2 * ps2
        zv1 = (zv1 + (0+12j) * yrz[2] * ps2 - 12 * yrz[0] * ps2 ** 2) + 8 * yrz[3] * ps1 - 8 * yrz[1] * ps3
        zv1 = (zv1 - 16 * yrz[0] * ps1 * ps3) + yrz[4] - (0+2j) * yrz[0] * ps4
        zv = xrz[4] + exptheta * zv1
    ctx.prec = wpinitial
    return zv


def z_offline(ctx, w, k = (0,)):
    '''
    Computes Z(w) and its derivatives off the line
    '''
    s = ctx.mpf('0.5') + ctx.j * w
    s1 = s
    s2 = ctx.conj(1 - s1)
    wpinitial = ctx.prec
    ctx.prec = 35
    if ctx._re(s1) >= 0:
        M1 = 2 * ctx.sqrt(ctx._im(s1) / (2 * ctx.pi))
        X = ctx.sqrt(abs(s1))
    else:
        X = (2 * ctx.pi) ** (ctx._re(s1) - 1) * abs(1 - s1) ** (0.5 - ctx._re(s1))
        M1 = 4 * ctx._im(s1) * X
    if ctx._re(s2) >= 0:
        M2 = 2 * ctx.sqrt(ctx._im(s2) / (2 * ctx.pi))
    else:
        M2 = 4 * ctx._im(s2) * (2 * ctx.pi) ** (ctx._re(s2) - 1) * abs(1 - s2) ** (0.5 - ctx._re(s2))
    T = 2 * abs(ctx.siegeltheta(w))
    aux1 = ctx.sqrt(X)
    aux2 = aux1 * (M1 + M2)
    aux3 = 3 + wpinitial
    wpbasic = max(6, 3 + ctx.mag(T), ctx.mag(aux2 * (26 + 2 * T)) + aux3)
    wptheta = max(4, ctx.mag(2.04 * aux2) + aux3)
    wpR = ctx.mag(4 * aux1) + aux3
    ctx.prec = wptheta
    theta = ctx.siegeltheta(w)
    ctx.prec = wpR
    (xrz, yrz) = Rzeta_simul(ctx, s, k)
    pta = 0.25 + (0+0.5j) * w
    ptb = 0.25 - (0+0.5j) * w
    if k > 0:
        ps1 = 0.25 * (ctx.psi(0, pta) + ctx.psi(0, ptb)) - ctx.ln(ctx.pi) / 2
    if k > 1:
        ps2 = (0+0.125j) * (ctx.psi(1, pta) - ctx.psi(1, ptb))
    if k > 2:
        ps3 = -0.0625 * (ctx.psi(2, pta) + ctx.psi(2, ptb))
    if k > 3:
        ps4 = (-0+-0.03125j) * (ctx.psi(3, pta) - ctx.psi(3, ptb))
    ctx.prec = wpbasic
    exptheta = ctx.expj(theta)
    if k == 0:
        zv = exptheta * xrz[0] + yrz[0] / exptheta
    j = ctx.j
    if k == 1:
        zv = j * exptheta * (xrz[1] + xrz[0] * ps1) - j * (yrz[1] + yrz[0] * ps1) / exptheta
    if k == 2:
        zv = exptheta * ((-2 * xrz[1] * ps1 - xrz[0] * ps1 ** 2 - xrz[2]) + j * xrz[0] * ps2)
        zv = zv + (-2 * yrz[1] * ps1 - yrz[0] * ps1 ** 2 - yrz[2] - j * yrz[0] * ps2) / exptheta
    if k == 3:
        zv1 = (-3 * xrz[1] * ps1 ** 2 - xrz[0] * ps1 ** 3 - 3 * xrz[2] * ps1) + j * 3 * xrz[1] * ps2
        zv1 = ((zv1 + (0+3j) * xrz[0] * ps1 * ps2 - xrz[3]) + xrz[0] * ps3) * j * exptheta
        zv2 = 3 * yrz[1] * ps1 ** 2 + yrz[0] * ps1 ** 3 + 3 * yrz[2] * ps1 + j * 3 * yrz[1] * ps2
        zv2 = j * (zv2 + (0+3j) * yrz[0] * ps1 * ps2 + yrz[3] - yrz[0] * ps3) / exptheta
        zv = zv1 + zv2
    if k == 4:
        zv1 = 4 * xrz[1] * ps1 ** 3 + xrz[0] * ps1 ** 4 + 6 * xrz[2] * ps1 ** 2
        zv1 = zv1 - (0+12j) * xrz[1] * ps1 * ps2 - (0+6j) * xrz[0] * ps1 ** 2 * ps2 - (0+6j) * xrz[2] * ps2
        zv1 = (zv1 - 3 * xrz[0] * ps2 * ps2) + 4 * xrz[3] * ps1 - 4 * xrz[1] * ps3 - 4 * xrz[0] * ps1 * ps3
        zv1 = zv1 + xrz[4] + j * xrz[0] * ps4
        zv2 = 4 * yrz[1] * ps1 ** 3 + yrz[0] * ps1 ** 4 + 6 * yrz[2] * ps1 ** 2
        zv2 = zv2 + (0+12j) * yrz[1] * ps1 * ps2 + (0+6j) * yrz[0] * ps1 ** 2 * ps2 + (0+6j) * yrz[2] * ps2
        zv2 = (zv2 - 3 * yrz[0] * ps2 * ps2) + 4 * yrz[3] * ps1 - 4 * yrz[1] * ps3 - 4 * yrz[0] * ps1 * ps3
        zv2 = zv2 + yrz[4] - j * yrz[0] * ps4
        zv = exptheta * zv1 + zv2 / exptheta
    ctx.prec = wpinitial
    return zv

rs_zeta = (lambda ctx, s, derivative = (0,): if derivative > 4:
raise NotImplementedErrors = ctx.convert(s)re = ctx._re(s)im = ctx._im(s)if im < 0:
z = ctx.conj(ctx.rs_zeta(ctx.conj(s), derivative))zcritical_line = None == 0.5if critical_line:
zeta_half(ctx, s, derivative)None(ctx, s, derivative))()
rs_z = (lambda ctx, w, derivative = (0,): w = ctx.convert(w)re = ctx._re(w)im = ctx._im(w)if re < 0:
rs_z(ctx, -w, derivative)critical_line = None == 0if critical_line:
z_half(ctx, w, derivative)None(ctx, w, derivative))()
