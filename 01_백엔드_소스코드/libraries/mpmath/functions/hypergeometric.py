# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hypergeometric.pyc (Python 3.11)

from libmp.backend import xrange
from functions import defun, defun_wrapped

def _check_need_perturb(ctx, terms, prec, discard_known_zeros):
    perturb = False
    recompute = False
    extraprec = 0
    discard = []
    for term_index, term in enumerate(terms):
        (w_s, c_s, alpha_s, beta_s, a_s, b_s, z) = term
        have_singular_nongamma_weight = False
        for k, w in enumerate(w_s):
            if w and ctx.re(c_s[k]) <= 0 and c_s[k]:
                perturb = True
                recompute = True
                have_singular_nongamma_weight = True
            pole_count = [
                0,
                0,
                0]
            for data_index, data in enumerate([
                alpha_s,
                beta_s,
                b_s]):
                for i, x in enumerate(data):
                    (n, d) = ctx.nint_distance(x)
                    if n > 0:
                        continue
                    if d == ctx.ninf:
                        ok = False
                        if data_index == 2:
                            for u in a_s:
                                if ctx.isnpint(u) and u >= int(n):
                                    ok = True
                                
                                if ok:
                                    continue
                        continue
                    if d < -4:
                        extraprec += -d = None
                        recompute = True
                    if not discard_known_zeros and pole_count[1] > pole_count[0] + pole_count[2] and have_singular_nongamma_weight:
                        discard.append(term_index)
                        continue
        if sum(pole_count):
            perturb = True
            recompute = True
        return (perturb, recompute, extraprec, discard)

_hypercomb_msg = '\nhypercomb() failed to converge to the requested %i bits of accuracy\nusing a working precision of %i bits. The function value may be zero or\ninfinite; try passing zeroprec=N or infprec=M to bound finite values between\n2^(-N) and 2^M. Otherwise try a higher maxprec or maxterms.\n'
hypercomb = (lambda ctx, function, params, discard_known_zeros = ([], True): pass# WARNING: Decompyle incomplete
)()
hyper = (lambda ctx, a_s, b_s, z: pass# WARNING: Decompyle incomplete
)()
hyp0f1 = (lambda ctx, b, z: pass# WARNING: Decompyle incomplete
)()
hyp1f1 = (lambda ctx, a, b, z: pass# WARNING: Decompyle incomplete
)()
hyp1f2 = (lambda ctx, a1, b1, b2, z: pass# WARNING: Decompyle incomplete
)()
hyp2f1 = (lambda ctx, a, b, c, z: pass# WARNING: Decompyle incomplete
)()
hyp2f2 = (lambda ctx, a1, a2, b1, b2, z: pass# WARNING: Decompyle incomplete
)()
hyp2f3 = (lambda ctx, a1, a2, b1, b2, b3, z: pass# WARNING: Decompyle incomplete
)()
hyp2f0 = (lambda ctx, a, b, z: pass# WARNING: Decompyle incomplete
)()
hyp3f2 = (lambda ctx, a1, a2, a3, b1, b2, z: pass# WARNING: Decompyle incomplete
)()
_hyp1f0 = (lambda ctx, a, z: (1 - z) ** (-a))()
_hyp0f1 = (lambda ctx, b_s, z: pass# WARNING: Decompyle incomplete
)()
_hyp1f1 = (lambda ctx, a_s, b_s, z: pass# WARNING: Decompyle incomplete
)()

def _hyp2f1_gosper(ctx, a, b, c, z, **kwargs):
    (_a, _b, _c, _z) = (a, b, c, z)
    orig = ctx.prec
    maxprec = kwargs.get('maxprec', 100 * orig)
    extra = 10
    ctx.prec = orig + extra
    z = ctx.convert(_z)
    d = ctx.mpf(0)
    e = ctx.mpf(1)
    f = ctx.mpf(0)
    k = 0
    abz = a * b * z
    ch = c * ctx.mpq_1_2
    c1h = (c + 1) * ctx.mpq_1_2
    nz = 1 - z
    g = z / nz
    abg = a * b * g
    cba = c - b - a
    z2 = z - 2
    tol = -(ctx.prec) - 10
    nstr = ctx.nstr
    nprint = ctx.nprint
    mag = ctx.mag
    maxmag = ctx.ninf
    kch = k + ch
    kakbz = (k + a) * (k + b) * z / (4 * (k + 1) * kch * (k + c1h))
    d1 = kakbz * (e - (k + cba) * d * g)
    e1 = kakbz * (d * abg + (k + c) * e)
    ft = d * (k * (cba * z + k * z2 - c) - abz) / (2 * kch * nz)
    f1 = f + e - ft
    maxmag = max(maxmag, mag(f1))
    if mag(f1 - f) < tol:
        pass
    else:
        f = f1
        e = e1
        d = d1
        k += 1
    cancellation = maxmag - mag(f1)
    if cancellation < extra:
        pass
    else:
        extra += cancellation
        if extra > maxprec:
            raise ctx.NoConvergence
    return f1

_hyp2f1 = (lambda ctx, a_s, b_s, z: pass# WARNING: Decompyle incomplete
)()
_hypq1fq = (lambda ctx, p, q, a_s, b_s, z: pass# WARNING: Decompyle incomplete
)()
_hyp_borel = (lambda ctx, p, q, a_s, b_s, z: pass# WARNING: Decompyle incomplete
)()
_hyp2f2 = (lambda ctx, a_s, b_s, z: pass# WARNING: Decompyle incomplete
)()
_hyp1f2 = (lambda ctx, a_s, b_s, z: pass# WARNING: Decompyle incomplete
)()
_hyp2f3 = (lambda ctx, a_s, b_s, z: pass# WARNING: Decompyle incomplete
)()
_hyp2f0 = (lambda ctx, a_s, b_s, z: pass# WARNING: Decompyle incomplete
)()
meijerg = (lambda ctx, a_s, b_s, z, r, series = (1, None): pass# WARNING: Decompyle incomplete
)()
appellf1 = (lambda ctx, a, b1, b2, c, x, y: if abs(x) > abs(y):
y = xx = yb2 = b1b1 = b2
def ok(x):
abs(x) < 0.99if ctx.isnpint(a):
passelif ctx.isnpint(b1):
passelif ctx.isnpint(b2):
(x, y, b1, b2) = (y, x, b2, b1)# WARNING: Decompyle incomplete
)()
appellf2 = (lambda ctx, a, b1, b2, c1, c2, x, y: pass# WARNING: Decompyle incomplete
)()
appellf3 = (lambda ctx, a1, a2, b1, b2, c, x, y: if not ctx.isnpint(a1):
outer_polynomial = ctx.isnpint(b1)if not ctx.isnpint(a2):
inner_polynomial = ctx.isnpint(b2)if not outer_polynomial:
if inner_polynomial or abs(x) > abs(y):
y = xx = y(a1, a2, b1, b2) = (a2, a1, b2, b1)# WARNING: Decompyle incomplete
)()
appellf4 = (lambda ctx, a, b, c1, c2, x, y: pass# WARNING: Decompyle incomplete
)()
hyper2d = (lambda ctx, a, b, x, y: pass# WARNING: Decompyle incomplete
)()
bihyper = (lambda ctx, a_s, b_s, z: pass# WARNING: Decompyle incomplete
)()
