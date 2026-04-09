# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eigen.pyc (Python 3.11)

'''
The eigenvalue problem
----------------------

This file contains routines for the eigenvalue problem.

high level routines:

  hessenberg : reduction of a real or complex square matrix to upper Hessenberg form
  schur : reduction of a real or complex square matrix to upper Schur form
  eig : eigenvalues and eigenvectors of a real or complex square matrix

low level routines:

  hessenberg_reduce_0 : reduction of a real or complex square matrix to upper Hessenberg form
  hessenberg_reduce_1 : auxiliary routine to hessenberg_reduce_0
  qr_step : a single implicitly shifted QR step for an upper Hessenberg matrix
  hessenberg_qr : Schur decomposition of an upper Hessenberg matrix
  eig_tr_r : right eigenvectors of an upper triangular matrix
  eig_tr_l : left  eigenvectors of an upper triangular matrix
'''
from libmp.backend import xrange

class Eigen(object):
    pass


def defun(f):
    setattr(Eigen, f.__name__, f)
    return f


def hessenberg_reduce_0(ctx, A, T):
    """
    This routine computes the (upper) Hessenberg decomposition of a square matrix A.
    Given A, an unitary matrix Q is calculated such that

               Q' A Q = H              and             Q' Q = Q Q' = 1

    where H is an upper Hessenberg matrix, meaning that it only contains zeros
    below the first subdiagonal. Here ' denotes the hermitian transpose (i.e.
    transposition and conjugation).

    parameters:
      A         (input/output) On input, A contains the square matrix A of
                dimension (n,n). On output, A contains a compressed representation
                of Q and H.
      T         (output) An array of length n containing the first elements of
                the Householder reflectors.
    """
    n = A.rows
    if n <= 2:
        return None
    for i in None(n - 1, 1, -1):
        scale = 0
        for k in xrange(0, i):
            scale += abs(ctx.re(A[(i, k)])) + abs(ctx.im(A[(i, k)]))
            scale_inv = 0
            if scale != 0:
                scale_inv = 1 / scale
        if scale == 0 or ctx.isinf(scale_inv):
            T[i] = 0
            A[(i, i - 1)] = 0
            continue
        H = 0
        for k in xrange(0, i):
            ctx.re(A[(i, k)]) = None
            ii = ctx.im(A[(i, k)])
            H += rr * rr + ii * ii
            F = A[(i, i - 1)]
            f = abs(F)
            G = ctx.sqrt(H)
            A[(i, i - 1)] = -G * scale
            if f == 0:
                T[i] = G
            else:
                ff = F / f
                T[i] = F + G * ff
        H += G * f = None
        H = 1 / ctx.sqrt(H)
        for None in xrange(0, i - 1):
            for None in xrange(0, i):
                G = ctx.conj(T[i]) * A[(j, i - 1)]
                for k in xrange(0, i - 1):
                    G += ctx.conj(A[(i, k)]) * A[(j, k)]
                    for None in xrange(0, i - 1):
                        for None in xrange(0, n):
                            G = T[i] * A[(i - 1, j)]
                            for k in xrange(0, i - 1):
                                G += A[(i, k)] * A[(k, j)]
                                for None in xrange(0, i - 1):
                                    return None


def hessenberg_reduce_1(ctx, A, T):
    '''
    This routine forms the unitary matrix Q described in hessenberg_reduce_0.

    parameters:
      A    (input/output) On input, A is the same matrix as delivered by
           hessenberg_reduce_0. On output, A is set to Q.

      T    (input) On input, T is the same array as delivered by hessenberg_reduce_0.
    '''
    n = A.rows
    if n == 1:
        A[(0, 0)] = 1
        return None
    A[(0, 0)] = None
    A[(1, 1)] = None
    A[(0, 1)] = 0
    A[(1, 0)] = 0
    for i in xrange(2, n):
        if T[i] != 0:
            for j in xrange(0, i):
                G = T[i] * A[(i - 1, j)]
                for k in xrange(0, i - 1):
                    G += A[(i, k)] * A[(k, j)]
                    for None in xrange(0, i - 1):
                        1 = None
                        for j in xrange(0, i):
                            A[(j, i)] = 0
                            A[(i, j)] = 0
                            return None

hessenberg = (lambda ctx, A, overwrite_a = (False,): n = A.rowsif n == 1:
(ctx.matrix([
[
1]]), A)if not None:
A = A.copy()T = ctx.matrix(n, 1)hessenberg_reduce_0(ctx, A, T)Q = A.copy()hessenberg_reduce_1(ctx, Q, T)for x in xrange(n):
for y in xrange(x + 2, n):
A[(y, x)] = 0(Q, A))()

def qr_step(ctx, n0, n1, A, Q, shift):
    '''
    This subroutine executes a single implicitly shifted QR step applied to an
    upper Hessenberg matrix A. Given A and shift as input, first an QR
    decomposition is calculated:

      Q R = A - shift * 1 .

    The output is then following matrix:

      R Q + shift * 1

    parameters:
      n0, n1    (input) Two integers which specify the submatrix A[n0:n1,n0:n1]
                on which this subroutine operators. The subdiagonal elements
                to the left and below this submatrix must be deflated (i.e. zero).
                following restriction is imposed: n1>=n0+2
      A         (input/output) On input, A is an upper Hessenberg matrix.
                On output, A is replaced by "R Q + shift * 1"
      Q         (input/output) The parameter Q is multiplied by the unitary matrix
                Q arising from the QR decomposition. Q can also be false, in which
                case the unitary matrix Q is not computated.
      shift     (input) a complex number specifying the shift. idealy close to an
                eigenvalue of the bottemmost part of the submatrix A[n0:n1,n0:n1].

    references:
      Stoer, Bulirsch - Introduction to Numerical Analysis.
      Kresser : Numerical Methods for General and Structured Eigenvalue Problems
    '''
    n = A.rows
    c = A[(n0, n0)] - shift
    s = A[(n0 + 1, n0)]
    v = ctx.hypot(ctx.hypot(ctx.re(c), ctx.im(c)), ctx.hypot(ctx.re(s), ctx.im(s)))
    if v == 0:
        v = 1
        c = 1
        s = 0
    else:
        c /= v
        s /= v
    cc = ctx.conj(c)
    cs = ctx.conj(s)
    for k in xrange(n0, n):
        x = A[(n0, k)]
        y = A[(n0 + 1, k)]
        A[(n0, k)] = cc * x + cs * y
        A[(n0 + 1, k)] = c * y - s * x
        for k in xrange(min(n1, n0 + 3)):
            x = A[(k, n0)]
            y = A[(k, n0 + 1)]
            A[(k, n0)] = c * x + s * y
            A[(k, n0 + 1)] = cc * y - cs * x
            if not isinstance(Q, bool):
                for k in xrange(n):
                    x = Q[(k, n0)]
                    y = Q[(k, n0 + 1)]
                    Q[(k, n0)] = c * x + s * y
                    Q[(k, n0 + 1)] = cc * y - cs * x
                    for j in xrange(n0, n1 - 2):
                        c = A[(j + 1, j)]
                        s = A[(j + 2, j)]
                        v = ctx.hypot(ctx.hypot(ctx.re(c), ctx.im(c)), ctx.hypot(ctx.re(s), ctx.im(s)))
                        if v == 0:
                            A[(j + 1, j)] = 0
                            v = 1
                            c = 1
                            s = 0
                        else:
                            A[(j + 1, j)] = v
                            c /= v
                            s /= v
                        A[(j + 2, j)] = 0
                        cc = ctx.conj(c)
                        cs = ctx.conj(s)
                        for k in xrange(j + 1, n):
                            x = A[(j + 1, k)]
                            y = A[(j + 2, k)]
                            A[(j + 1, k)] = cc * x + cs * y
                            A[(j + 2, k)] = c * y - s * x
                            for k in xrange(0, min(n1, j + 4)):
                                x = A[(k, j + 1)]
                                y = A[(k, j + 2)]
                                A[(k, j + 1)] = c * x + s * y
                                A[(k, j + 2)] = cc * y - cs * x
                                if not isinstance(Q, bool):
                                    for k in xrange(0, n):
                                        x = Q[(k, j + 1)]
                                        y = Q[(k, j + 2)]
                                        Q[(k, j + 1)] = c * x + s * y
                                        Q[(k, j + 2)] = cc * y - cs * x
                                        return None


def hessenberg_qr(ctx, A, Q):
    """
    This routine computes the Schur decomposition of an upper Hessenberg matrix A.
    Given A, an unitary matrix Q is determined such that

          Q' A Q = R                   and                  Q' Q = Q Q' = 1

    where R is an upper right triangular matrix. Here ' denotes the hermitian
    transpose (i.e. transposition and conjugation).

    parameters:
      A         (input/output) On input, A contains an upper Hessenberg matrix.
                On output, A is replace by the upper right triangluar matrix R.

      Q         (input/output) The parameter Q is multiplied by the unitary
                matrix Q arising from the Schur decomposition. Q can also be
                false, in which case the unitary matrix Q is not computated.
    """
    n = A.rows
    norm = 0
# WARNING: Decompyle incomplete

schur = (lambda ctx, A, overwrite_a = (False,): n = A.rowsif n == 1:
(ctx.matrix([
[
1]]), A)if not None:
A = A.copy()T = ctx.matrix(n, 1)hessenberg_reduce_0(ctx, A, T)Q = A.copy()hessenberg_reduce_1(ctx, Q, T)for x in xrange(n):
for y in xrange(x + 2, n):
A[(y, x)] = 0hessenberg_qr(ctx, A, Q)(Q, A))()

def eig_tr_r(ctx, A):
    '''
    This routine calculates the right eigenvectors of an upper right triangular matrix.

    input:
      A      an upper right triangular matrix

    output:
      ER     a matrix whose columns form the right eigenvectors of A

    return value: ER
    '''
    n = A.rows
    ER = ctx.eye(n)
    eps = ctx.eps
    unfl = ctx.ldexp(ctx.one, -(ctx.prec) * 30)
    smlnum = unfl * (n / eps)
    simin = 1 / ctx.sqrt(eps)
    rmax = 1
    for i in xrange(1, n):
        s = A[(i, i)]
        smin = max(eps * abs(s), smlnum)
        for j in xrange(i - 1, -1, -1):
            r = 0
            for k in xrange(j + 1, i + 1):
                r += A[(j, k)] * ER[(k, i)]
                t = A[(j, j)] - s
                if abs(t) < smin:
                    t = smin
            r = -r / t
            ER[(j, i)] = r
            rmax = max(rmax, abs(r))
            if rmax > simin:
                for k in xrange(j, i + 1):
                    1 = None
                    if rmax != 1:
                        for k in xrange(0, i + 1):
                            return ER


def eig_tr_l(ctx, A):
    '''
    This routine calculates the left eigenvectors of an upper right triangular matrix.

    input:
      A      an upper right triangular matrix

    output:
      EL     a matrix whose rows form the left eigenvectors of A

    return value:  EL
    '''
    n = A.rows
    EL = ctx.eye(n)
    eps = ctx.eps
    unfl = ctx.ldexp(ctx.one, -(ctx.prec) * 30)
    smlnum = unfl * (n / eps)
    simin = 1 / ctx.sqrt(eps)
    rmax = 1
    for i in xrange(0, n - 1):
        s = A[(i, i)]
        smin = max(eps * abs(s), smlnum)
        for j in xrange(i + 1, n):
            r = 0
            for k in xrange(i, j):
                r += EL[(i, k)] * A[(k, j)]
                t = A[(j, j)] - s
                if abs(t) < smin:
                    t = smin
            r = -r / t
            EL[(i, j)] = r
            rmax = max(rmax, abs(r))
            if rmax > simin:
                for k in xrange(i, j + 1):
                    1 = None
                    if rmax != 1:
                        for k in xrange(i, n):
                            return EL

eig = (lambda ctx, A, left, right, overwrite_a = (False, True, False): n = A.rowsif n == 1:
if not left and right:
([
A[0]], ctx.matrix([
[
1]]))if not None and left:
([
A[0]], ctx.matrix([
[
1]]))([
None[0]], ctx.matrix([
[
1]]), ctx.matrix([
[
1]]))if not None:
A = A.copy()T = ctx.zeros(n, 1)hessenberg_reduce_0(ctx, A, T)if left or right:
Q = A.copy()hessenberg_reduce_1(ctx, Q, T)else:
Q = Falsefor x in xrange(n):
for y in xrange(x + 2, n):
A[(y, x)] = 0hessenberg_qr(ctx, A, Q)E = xrange(n)()for i in xrange(n):
E[i] = A[(i, i)]if not left and right:
Eif (lambda .0: [ 0 for i in .0 ]):
                    EL = eig_tr_l(ctx, A)
                    EL = EL * Q.transpose_conj()
    if right:
        ER = eig_tr_r(ctx, A)
        ER = Q * ER
    if not left and right:
        return (E, EL)
    if not None and left:
        return (E, ER)
    return (None, EL, ER)
)()
eig_sort = (lambda ctx, E, EL, ER, f = (False, False, 'real'): if isinstance(f, str):
if f == 'real':
f = ctx.reelif f == 'imag':
f = ctx.imelif f == 'abs':
f = abselse:
raise RuntimeError('unknown function %s' % f)n = len(E)for i in xrange(n):
imax = is = f(E[i])for j in xrange(i + 1, n):
c = f(E[j])if c < s:
s = cimax = jif imax != i:
z = E[i]E[i] = E[imax]E[imax] = zif not isinstance(EL, bool):
for j in xrange(n):
z = EL[(i, j)]EL[(i, j)] = EL[(imax, j)]EL[(imax, j)] = zif not isinstance(ER, bool):
for j in xrange(n):
z = ER[(j, i)]ER[(j, i)] = ER[(j, imax)]ER[(j, imax)] = zif isinstance(EL, bool) and isinstance(ER, bool):
Eif not None(EL, bool) and isinstance(ER, bool):
(E, ER)if not None(ER, bool) and isinstance(EL, bool):
(E, EL)(None, EL, ER))()
