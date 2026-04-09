# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: expintegrals.pyc (Python 3.11)

from functions import defun, defun_wrapped
_erf_complex = (lambda ctx, z: z2 = ctx.square_exp_arg(z, -1)v = (2 / ctx.sqrt(ctx.pi)) * z * ctx.hyp1f1((1, 2), (3, 2), z2)if not ctx._re(z):
v = ctx._im(v) * ctx.jv)()
_erfc_complex = (lambda ctx, z: if ctx.re(z) > 2:
z2 = ctx.square_exp_arg(z)nz2 = ctx.fneg(z2, exact = True)v = (ctx.exp(nz2) / ctx.sqrt(ctx.pi)) * ctx.hyperu((1, 2), (1, 2), z2)else:
v = 1 - ctx._erf_complex(z)if not ctx._re(z):
v = 1 + ctx._im(v) * ctx.jv)()
erf = (lambda ctx, z:
