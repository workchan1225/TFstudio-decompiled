# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: theta.pyc (Python 3.11)

from functions import defun, defun_wrapped
_jacobi_theta2 = (lambda ctx, z, q: extra1 = 10extra2 = 20MIN = 2# WARNING: Decompyle incomplete
)()
_djacobi_theta2 = (lambda ctx, z, q, nd: MIN = 2extra1 = 10extra2 = 20# WARNING: Decompyle incomplete
)()
_jacobi_theta3 = (lambda ctx, z, q: extra1 = 10extra2 = 20MIN = 2# WARNING: Decompyle incomplete
)()
_djacobi_theta3 = (lambda ctx, z, q, nd: MIN = 2extra1 = 10extra2 = 20# WARNING: Decompyle incomplete
)()
_jacobi_theta2a = (lambda ctx, z, q: n = int(ctx._im(z) / ctx._re(ctx.log(q)) - 0.5)n0 = int(ctx._im(z) / ctx._re(ctx.log(q)) - 0.5)e2 = ctx.expj(2 * z)e = ctx.expj((2 * n + 1) * z)e0 = ctx.expj((2 * n + 1) * z)a = q ** (n * n + n)term = a * es = termeps1 = ctx.eps * abs(term)n += 1e = e * e2term = q ** (n * n + n) * eif abs(term) < eps1:
passelse:
s += terme = e0e2 = ctx.expj(-2 * z)n = n0n -= 1e = e * e2term = q ** (n * n + n) * eif abs(term) < eps1:
passelse:
s += terms = s * ctx.nthroot(q, 4)s)()
_jacobi_theta3a = (lambda ctx, z, q: n = int(-ctx._im(z) / abs(ctx._re(ctx.log(q))))n0 = int(-ctx._im(z) / abs(ctx._re(ctx.log(q))))e2 = ctx.expj(2 * z)e = ctx.expj(2 * n * z)e0 = ctx.expj(2 * n * z)s = q ** (n * n) * eterm = q ** (n * n) * eeps1 = ctx.eps * abs(term)n += 1e = e * e2term = q ** (n * n) * eif abs(term) < eps1:
passelse:
s += terme = e0e2 = ctx.expj(-2 * z)n = n0n -= 1e = e * e2term = q ** (n * n) * eif abs(term) < eps1:
passelse:
s += terms)()
_djacobi_theta2a = (lambda ctx, z, q, nd: n = int(ctx._im(z) / ctx._re(ctx.log(q)) - 0.5)n0 = int(ctx._im(z) / ctx._re(ctx.log(q)) - 0.5)e2 = ctx.expj(2 * z)e = ctx.expj((2 * n + 1) * z)e0 = ctx.expj((2 * n + 1) * z)a = q ** (n * n + n)term = (2 * n + 1) ** nd * a * es = termeps1 = ctx.eps * abs(term)n += 1e = e * e2term = (2 * n + 1) ** nd * q ** (n * n + n) * eif abs(term) < eps1:
passelse:
s += terme = e0e2 = ctx.expj(-2 * z)n = n0n -= 1e = e * e2term = (2 * n + 1) ** nd * q ** (n * n + n) * eif abs(term) < eps1:
passelse:
s += termctx.j ** nd * s * ctx.nthroot(q, 4))()
_djacobi_theta3a = (lambda ctx, z, q, nd: n = int(-ctx._im(z) / abs(ctx._re(ctx.log(q))))n0 = int(-ctx._im(z) / abs(ctx._re(ctx.log(q))))e2 = ctx.expj(2 * z)e = ctx.expj(2 * n * z)e0 = ctx.expj(2 * n * z)a = q ** (n * n) * es = n ** nd * aterm = n ** nd * aif n != 0:
eps1 = ctx.eps * abs(term)else:
eps1 = ctx.eps * abs(a)n += 1e = e * e2a = q ** (n * n) * eterm = n ** nd * aif n != 0:
aterm = abs(term)else:
aterm = abs(a)if aterm < eps1:
passelse:
s += terme = e0e2 = ctx.expj(-2 * z)n = n0n -= 1e = e * e2a = q ** (n * n) * eterm = n ** nd * aif n != 0:
aterm = abs(term)else:
aterm = abs(a)if aterm < eps1:
passelse:
s += term(2 * ctx.j) ** nd * s)()
jtheta = (lambda ctx, n, z, q, derivative = (0,): if derivative:
ctx._djtheta(n, z, q, derivative)z = None.convert(z)q = ctx.convert(q)if abs(q) > ctx.THETA_Q_LIM:
raise ValueError('abs(q) > THETA_Q_LIM = %f' % ctx.THETA_Q_LIM)extra = 10if z:
M = ctx.mag(z)if (M > 5 or n == 1) and M < -5:
extra += 2 * abs(M)cz = 0.5extra2 = 50prec0 = ctx.prectry:
if n == 1:
if ctx._im(z):
if abs(ctx._im(z)) < cz * abs(ctx._re(ctx.log(q))):
ctx._jacobi_theta2(z - ctx.pi / 2, q) = ctx, ctx.dps += extra2, .dpselse:
ctx._jacobi_theta2a(z - ctx.pi / 2, q) = ctx, ctx.dps += 10, .dpselse:
res = ctx._jacobi_theta2(z - ctx.pi / 2, q)elif n == 2:
if ctx._im(z):
if abs(ctx._im(z)) < cz * abs(ctx._re(ctx.log(q))):
ctx._jacobi_theta2(z, q) = ctx, ctx.dps += extra2, .dpselse:
ctx._jacobi_theta2a(z, q) = ctx, ctx.dps += 10, .dpselse:
res = ctx._jacobi_theta2(z, q)elif n == 3:
if ctx._im(z):
if abs(ctx._im(z)) < cz * abs(ctx._re(ctx.log(q))):
ctx._jacobi_theta3(z, q) = ctx, ctx.dps += extra2, .dpselse:
ctx._jacobi_theta3a(z, q) = ctx, ctx.dps += 10, .dpselse:
res = ctx._jacobi_theta3(z, q)elif n == 4:
if ctx._im(z):
if abs(ctx._im(z)) < cz * abs(ctx._re(ctx.log(q))):
ctx._jacobi_theta3(z, -q) = ctx, ctx.dps += extra2, .dpselse:
ctx._jacobi_theta3a(z, -q) = ctx, ctx.dps += 10, .dpselse:
res = ctx._jacobi_theta3(z, -q)else:
raise ValueErrorctx.prec = prec0except:
ctx.prec = prec0res)()
_djtheta = (lambda ctx, n, z, q, derivative = (1,): z = ctx.convert(z)q = ctx.convert(q)nd = int(derivative)if abs(q) > ctx.THETA_Q_LIM:
raise ValueError('abs(q) > THETA_Q_LIM = %f' % ctx.THETA_Q_LIM)extra = 10 + ctx.prec * nd // 10if z:
M = ctx.mag(z)if (M > 5 or n != 1) and M < -5:
extra += 2 * abs(M)cz = 0.5extra2 = 50prec0 = ctx.prectry:
if n == 1:
if ctx._im(z):
if abs(ctx._im(z)) < cz * abs(ctx._re(ctx.log(q))):
ctx._djacobi_theta2(z - ctx.pi / 2, q, nd) = ctx, ctx.dps += extra2, .dpselse:
ctx._djacobi_theta2a(z - ctx.pi / 2, q, nd) = ctx, ctx.dps += 10, .dpselse:
res = ctx._djacobi_theta2(z - ctx.pi / 2, q, nd)elif n == 2:
if ctx._im(z):
if abs(ctx._im(z)) < cz * abs(ctx._re(ctx.log(q))):
ctx._djacobi_theta2(z, q, nd) = ctx, ctx.dps += extra2, .dpselse:
ctx._djacobi_theta2a(z, q, nd) = ctx, ctx.dps += 10, .dpselse:
res = ctx._djacobi_theta2(z, q, nd)elif n == 3:
if ctx._im(z):
if abs(ctx._im(z)) < cz * abs(ctx._re(ctx.log(q))):
ctx._djacobi_theta3(z, q, nd) = ctx, ctx.dps += extra2, .dpselse:
ctx._djacobi_theta3a(z, q, nd) = ctx, ctx.dps += 10, .dpselse:
res = ctx._djacobi_theta3(z, q, nd)elif n == 4:
if ctx._im(z):
if abs(ctx._im(z)) < cz * abs(ctx._re(ctx.log(q))):
ctx._djacobi_theta3(z, -q, nd) = ctx, ctx.dps += extra2, .dpselse:
ctx._djacobi_theta3a(z, -q, nd) = ctx, ctx.dps += 10, .dpselse:
res = ctx._djacobi_theta3(z, -q, nd)else:
raise ValueErrorctx.prec = prec0except:
ctx.prec = prec0+res)()
