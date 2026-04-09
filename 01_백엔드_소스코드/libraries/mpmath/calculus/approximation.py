# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: approximation.pyc (Python 3.11)

from libmp.backend import xrange
from calculus import defun

def chebcoeff(ctx, f, a, b, j, N):
    s = ctx.mpf(0)
    h = ctx.mpf(0.5)
    for k in range(1, N + 1):
        t = ctx.cospi((k - h) / N)
        s += f(t * (b - a) * h + (b + a) * h) * ctx.cospi(j * (k - h) / N)
        return 2 * s / N


def chebT(ctx, a, b = (1, 0)):
    pass
# WARNING: Decompyle incomplete

chebyfit = (lambda ctx, f, interval, N, error = (False,): pass# WARNING: Decompyle incomplete
)()
fourier = (lambda ctx, f, interval, N: pass# WARNING: Decompyle incomplete
)()
fourierval = (lambda ctx, series, interval, x: pass# WARNING: Decompyle incomplete
)()
