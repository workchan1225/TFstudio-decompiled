# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: differentiation.pyc (Python 3.11)

from libmp.backend import xrange
from calculus import defun

try:
    iteritems = dict.iteritems
except AttributeError:
    iteritems = dict.items

difference = (lambda ctx, s, n: n = int(n)d = ctx.zerob = -1 ** (n & 1)for k in xrange(n + 1):
d += b * s[k]b = b * (k - n) // (k + 1)d)()

def hsteps(ctx, f, x, n, prec, **options):
    pass
# WARNING: Decompyle incomplete

diff = (lambda ctx, f, x, n = (1,): pass# WARNING: Decompyle incomplete
)()

def _partial_diff(ctx, f, xs, orders, options):
    pass
# WARNING: Decompyle incomplete

diffs = (lambda ctx, f, x, n = (None,): pass# WARNING: Decompyle incomplete
)()

def iterable_to_function(gen):
    pass
# WARNING: Decompyle incomplete

diffs_prod = (lambda ctx, factors: pass# WARNING: Decompyle incomplete
)()

def dpoly(n, _cache = ({ },)):
    """
    nth differentiation polynomial for exp (Faa di Bruno's formula).

    TODO: most exponents are zero, so maybe a sparse representation
    would be better.
    """
    if n in _cache:
        return _cache[n]
    if not None:
        _cache[0] = {
            (0,): 1 }
    R = dpoly(n - 1)
    R = (lambda .0: pass# WARNING: Decompyle incomplete
)(iteritems(R)())
    Ra = { }
    for powers, count in iteritems(R):
        powers1 = (powers[0] + 1,) + powers[1:]
        if powers1 in Ra:
            continue
        count = dict
        for powers, count in iteritems(R):
            if not sum(powers):
                continue
            for k, p in enumerate(powers):
                if p:
                    powers2 = powers[:k] + (p - 1, powers[k + 1] + 1) + powers[k + 2:]
                    if powers2 in Ra:
                        continue
                    p * count = None
                _cache[n] = Ra
                return _cache[n]

diffs_exp = (lambda ctx, fdiffs: pass# WARNING: Decompyle incomplete
)()
differint = (lambda ctx, f, x, n, x0 = (1, 0): pass# WARNING: Decompyle incomplete
)()
diffun = (lambda ctx, f, n = (1,): pass# WARNING: Decompyle incomplete
)()
taylor = (lambda ctx, f, x, n: pass# WARNING: Decompyle incomplete
)()
pade = (lambda ctx, a, L, M: if len(a) < L + M + 1:
raise ValueError('L+M+1 Coefficients should be provided')if M == 0:
if L == 0:
([
ctx.one], [
ctx.one])(None[:L + 1], [
ctx.one])A = None.matrix(M)for j in range(M):
for i in range(min(M, L + j + 1)):
A[(j, i)] = a[L + j - i]v = -ctx.matrix(a[L + 1:L + M + 1])x = ctx.lu_solve(A, v)q = [
ctx.one] + list(x)p = [
0] * (L + 1)for i in range(L + 1):
s = a[i]for j in range(1, min(M, i) + 1):
s += q[j] * a[i - j]p[i] = s(p, q))()
