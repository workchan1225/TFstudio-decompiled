# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: orthogonal.pyc (Python 3.11)

from functions import defun, defun_wrapped

def _hermite_param(ctx, n, z, parabolic_cylinder):
    '''
    Combined calculation of the Hermite polynomial H_n(z) (and its
    generalization to complex n) and the parabolic cylinder
    function D.
    '''
    (n, ntyp) = ctx._convert_param(n)
    z = ctx.convert(z)
    q = -(ctx.mpq_1_2)
    if not z:
        T1 = ([
            2,
            ctx.pi], [
            n,
            0.5], [], [
            q * (n - 1)], [], [], 0)
        if parabolic_cylinder:
            pass
        return (T1,)
    if not None.isnpint(-n):
        if not ctx.re(z) > 0:
            if ctx.re(z) == 0:
                ctx.im(z) > 0 = None
                expprec = ctx.prec * 4 + 20
                if parabolic_cylinder:
                    u = ctx.fmul(ctx.fmul(z, z, prec = expprec), -0.25, exact = True)
                    w = ctx.fmul(z, ctx.sqrt(0.5, prec = expprec), prec = expprec)
                else:
                    w = z
    w2 = ctx.fmul(w, w, prec = expprec)
    rw2 = ctx.fdiv(1, w2, prec = expprec)
    nrw2 = ctx.fneg(rw2, exact = True)
    nw = ctx.fneg(w, exact = True)
    if can_use_2f0:
        T1 = ([
            2,
            w], [
            n,
            n], [], [], [
            q * n,
            q * (n - 1)], [], nrw2)
        terms = [
            T1]
    else:
        T1 = ([
            2,
            nw], [
            n,
            n], [], [], [
            q * n,
            q * (n - 1)], [], nrw2)
        T2 = ([
            2,
            ctx.pi,
            nw], [
            n + 2,
            0.5,
            1], [], [
            q * n], [
            q * (n - 1)], [
            1 - q], w2)
        terms = [
            T1,
            T2]
    if parabolic_cylinder:
        expu = ctx.exp(u)
        for i in range(len(terms)):
            terms[i][0].append(expu)
            terms[i][1].append(1)
            return tuple(terms)

hermite = (lambda ctx, n, z: pass# WARNING: Decompyle incomplete
)()
pcfd = (lambda ctx, n, z: pass# WARNING: Decompyle incomplete
)()
pcfu = (lambda ctx, a, z: (n, _) = ctx._convert_param(a)ctx.pcfd(-n - ctx.mpq_1_2, z))()
pcfv = (lambda ctx, a, z: pass# WARNING: Decompyle incomplete
)()
pcfw = (lambda ctx, a, z: pass# WARNING: Decompyle incomplete
)()
gegenbauer = (lambda ctx, n, a, z: pass# WARNING: Decompyle incomplete
)()
jacobi = (lambda ctx, n, a, b, x: pass# WARNING: Decompyle incomplete
)()
laguerre = (lambda ctx, n, a, z: pass# WARNING: Decompyle incomplete
)()
legendre = (lambda ctx, n, x: if ctx.isint(n):
n = int(n)if n + (n < 0) & 1:
if not x:
xmag = None.mag(x)if mag < -2 * ctx.prec - 10:
xif None < -5:
pass# WARNING: Decompyle incomplete
)()
legenp = (lambda ctx, n, m, z, type = (2,): pass# WARNING: Decompyle incomplete
)()
legenq = (lambda ctx, n, m, z, type = (2,): pass# WARNING: Decompyle incomplete
)()
chebyt = (lambda ctx, n, x: if x and ctx.isint(n) and int(ctx._re(n)) % 2 == 1:
x * 0# WARNING: Decompyle incomplete
)()
chebyu = (lambda ctx, n, x: if x and ctx.isint(n) and int(ctx._re(n)) % 2 == 1:
x * 0# WARNING: Decompyle incomplete
)()
spherharm = (lambda ctx, l, m, theta, phi: pass# WARNING: Decompyle incomplete
)()
