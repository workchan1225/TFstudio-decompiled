# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polynomials.pyc (Python 3.11)

from libmp.backend import xrange
from calculus import defun
polyval = (lambda ctx, coeffs, x, derivative = (False,): if not coeffs:
ctx.zerop = None.convert(coeffs[0])q = ctx.zerofor c in coeffs[1:]:
if derivative:
q = p + x * qp = c + x * pif derivative:
(p, q)None)()
polyroots = (lambda ctx, coeffs, maxsteps, cleanup, extraprec, error, roots_init = (50, True, 10, False, None): pass# WARNING: Decompyle incomplete
)()
