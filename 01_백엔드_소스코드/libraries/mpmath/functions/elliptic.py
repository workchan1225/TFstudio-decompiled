# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: elliptic.pyc (Python 3.11)

__doc__ = '\nElliptic functions historically comprise the elliptic integrals\nand their inverses, and originate from the problem of computing the\narc length of an ellipse. From a more modern point of view,\nan elliptic function is defined as a doubly periodic function, i.e.\na function which satisfies\n\n.. math ::\n\n    f(z + 2 \\omega_1) = f(z + 2 \\omega_2) = f(z)\n\nfor some half-periods `\\omega_1, \\omega_2` with\n`\\mathrm{Im}[\\omega_1 / \\omega_2] > 0`. The canonical elliptic\nfunctions are the Jacobi elliptic functions. More broadly, this section\nincludes  quasi-doubly periodic functions (such as the Jacobi theta\nfunctions) and other functions useful in the study of elliptic functions.\n\nMany different conventions for the arguments of\nelliptic functions are in use. It is even standard to use\ndifferent parameterizations for different functions in the same\ntext or software (and mpmath is no exception).\nThe usual parameters are the elliptic nome `q`, which usually\nmust satisfy `|q| < 1`; the elliptic parameter `m` (an arbitrary\ncomplex number); the elliptic modulus `k` (an arbitrary complex\nnumber); and the half-period ratio `\\tau`, which usually must\nsatisfy `\\mathrm{Im}[\\tau] > 0`.\nThese quantities can be expressed in terms of each other\nusing the following relations:\n\n.. math ::\n\n    m = k^2\n\n.. math ::\n\n    \\tau = i \\frac{K(1-m)}{K(m)}\n\n.. math ::\n\n    q = e^{i \\pi \\tau}\n\n.. math ::\n\n    k = \\frac{\\vartheta_2^2(q)}{\\vartheta_3^2(q)}\n\nIn addition, an alternative definition is used for the nome in\nnumber theory, which we here denote by q-bar:\n\n.. math ::\n\n    \\bar{q} = q^2 = e^{2 i \\pi \\tau}\n\nFor convenience, mpmath provides functions to convert\nbetween the various parameters (:func:`~mpmath.qfrom`, :func:`~mpmath.mfrom`,\n:func:`~mpmath.kfrom`, :func:`~mpmath.taufrom`, :func:`~mpmath.qbarfrom`).\n\n**References**\n\n1. [AbramowitzStegun]_\n\n2. [WhittakerWatson]_\n\n'
from functions import defun, defun_wrapped
eta = (lambda ctx, tau: if ctx.im(tau) <= 0:
raise ValueError('eta is only defined in the upper half-plane')q = ctx.expjpi(tau / 12)q * ctx.qp(q ** 24))()

def nome(ctx, m):
    m = ctx.convert(m)
    if not m:
        return m
    if None == ctx.one:
        return m
    if None.isnan(m):
        return m
    if None.isinf(m):
        if m == ctx.ninf:
            return type(m)(-1)
        return None.mpc(-1)
    a = None.ellipk(ctx.one - m)
    b = ctx.ellipk(m)
    v = ctx.exp(-(ctx.pi) * a / b)
    if ctx._im(m) and ctx._re(m) < 1:
        if ctx._is_real_type(m):
            return v.real
        return None.real + (0+0j)
    if None == 2:
        v = ctx.mpc(0, v.imag)
    return v

qfrom = (lambda ctx, q, m, k, tau, qbar = (None, None, None, None, None): pass# WARNING: Decompyle incomplete
)()
qbarfrom = (lambda ctx, q, m, k, tau, qbar = (None, None, None, None, None): pass# WARNING: Decompyle incomplete
)()
taufrom = (lambda ctx, q, m, k, tau, qbar = (None, None, None, None, None): pass# WARNING: Decompyle incomplete
)()
kfrom = (lambda ctx, q, m, k, tau, qbar = (None, None, None, None, None): pass# WARNING: Decompyle incomplete
)()
mfrom = (lambda ctx, q, m, k, tau, qbar = (None, None, None, None, None): pass# WARNING: Decompyle incomplete
)()
# WARNING: Decompyle incomplete
