# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eigen_symmetric.pyc (Python 3.11)

'''
The symmetric eigenvalue problem.
---------------------------------

This file contains routines for the symmetric eigenvalue problem.

high level routines:

  eigsy : real symmetric (ordinary) eigenvalue problem
  eighe : complex hermitian (ordinary) eigenvalue problem
  eigh  : unified interface for eigsy and eighe
  svd_r : singular value decomposition for real matrices
  svd_c : singular value decomposition for complex matrices
  svd   : unified interface for svd_r and svd_c


low level routines:

  r_sy_tridiag : reduction of real symmetric matrix to real symmetric tridiagonal matrix
  c_he_tridiag_0 : reduction of complex hermitian matrix to real symmetric tridiagonal matrix
  c_he_tridiag_1 : auxiliary routine to c_he_tridiag_0
  c_he_tridiag_2 : auxiliary routine to c_he_tridiag_0
  tridiag_eigen : solves the real symmetric tridiagonal matrix eigenvalue problem
  svd_r_raw : raw singular value decomposition for real matrices
  svd_c_raw : raw singular value decomposition for complex matrices
'''
from libmp.backend import xrange
from eigen import defun

def r_sy_tridiag(ctx, A, D, E, calc_ev = (True,)):
    """
    This routine transforms a real symmetric matrix A to a real symmetric
    tridiagonal matrix T using an orthogonal similarity transformation:
          Q' * A * Q = T     (here ' denotes the matrix transpose).
    The orthogonal matrix Q is build up from Householder reflectors.

    parameters:
      A         (input/output) On input, A contains the real symmetric matrix of
                dimension (n,n). On output, if calc_ev is true, A contains the
                orthogonal matrix Q, otherwise A is destroyed.

      D         (output) real array of length n, contains the diagonal elements
                of the tridiagonal matrix

      E         (output) real array of length n, contains the offdiagonal elements
                of the tridiagonal matrix in E[0:(n-1)] where is the dimension of
                the matrix A. E[n-1] is undefined.

      calc_ev   (input) If calc_ev is true, this routine explicitly calculates the
                orthogonal matrix Q which is then returned in A. If calc_ev is
                false, Q is not explicitly calculated resulting in a shorter run time.

    This routine is a python translation of the fortran routine tred2.f in the
    software library EISPACK (see netlib.org) which itself is based on the algol
    procedure tred2 described in:
      - Num. Math. 11, p.181-195 (1968) by Martin, Reinsch and Wilkonson
      - Handbook for auto. comp., Vol II, Linear Algebra, p.212-226 (1971)

    For a good introduction to Householder reflections, see also
      Stoer, Bulirsch - Introduction to Numerical Analysis.
    """
    n = A.rows
    for i in xrange(n - 1, 0, -1):
        scale = 0
        for k in xrange(0, i):
            scale += abs(A[(k, i)])
            scale_inv = 0
            if scale != 0:
                scale_inv = 1 / scale
        if i == 1 and scale == 0 or ctx.isinf(scale_inv):
            E[i] = A[(i - 1, i)]
            D[i] = 0
            continue
        H = 0
        for k in xrange(0, i):
            H += A[(k, i)] * A[(k, i)] = None
            F = A[(i - 1, i)]
            G = ctx.sqrt(H)
            if F > 0:
                G = -G
        E[i] = scale * G
        H -= F * G
        A[(i - 1, i)] = F - G
        F = 0
        for j in xrange(0, i):
            if calc_ev:
                A[(i, j)] = A[(j, i)] / H
            G = 0
            for k in xrange(0, j + 1):
                G += A[(k, j)] * A[(k, i)]
                for k in xrange(j + 1, i):
                    G += A[(j, k)] * A[(k, i)]
                    E[j] = G / H
                    F += E[j] * A[(j, i)]
                    HH = F / (2 * H)
                    for j in xrange(0, i):
                        F = A[(j, i)]
                        G = E[j] - HH * F
                        E[j] = G
                        for k in xrange(0, j + 1):
                            H = None
                            for i in xrange(1, n):
                                E[i - 1] = E[i]
                                E[n - 1] = 0
                                if calc_ev:
                                    D[0] = 0
                                    for i in xrange(0, n):
                                        if D[i] != 0:
                                            for j in xrange(0, i):
                                                G = 0
                                                for k in xrange(0, i):
                                                    G += A[(i, k)] * A[(k, j)]
                                                    for k in xrange(0, i):
                                                        A[(i, i)] = None
                                                        A[(i, i)] = 1
                                                        for j in xrange(0, i):
                                                            A[(j, i)] = 0
                                                            A[(i, j)] = 0
                                                            return None
                                                            for i in xrange(0, n):
                                                                D[i] = A[(i, i)]
                                                                return None


def c_he_tridiag_0(ctx, A, D, E, T):
    """
    This routine transforms a complex hermitian matrix A to a real symmetric
    tridiagonal matrix T using an unitary similarity transformation:
          Q' * A * Q = T     (here ' denotes the hermitian matrix transpose,
                              i.e. transposition und conjugation).
    The unitary matrix Q is build up from Householder reflectors and
    an unitary diagonal matrix.

    parameters:
      A         (input/output) On input, A contains the complex hermitian matrix
                of dimension (n,n). On output, A contains the unitary matrix Q
                in compressed form.

      D         (output) real array of length n, contains the diagonal elements
                of the tridiagonal matrix.

      E         (output) real array of length n, contains the offdiagonal elements
                of the tridiagonal matrix in E[0:(n-1)] where is the dimension of
                the matrix A. E[n-1] is undefined.

      T         (output) complex array of length n, contains a unitary diagonal
                matrix.

    This routine is a python translation (in slightly modified form) of the fortran
    routine htridi.f in the software library EISPACK (see netlib.org) which itself
    is a complex version of the algol procedure tred1 described in:
      - Num. Math. 11, p.181-195 (1968) by Martin, Reinsch and Wilkonson
      - Handbook for auto. comp., Vol II, Linear Algebra, p.212-226 (1971)

    For a good introduction to Householder reflections, see also
      Stoer, Bulirsch - Introduction to Numerical Analysis.
    """
    n = A.rows
    T[n - 1] = 1
    for i in xrange(n - 1, 0, -1):
        scale = 0
        for k in xrange(0, i):
            scale += abs(ctx.re(A[(k, i)])) + abs(ctx.im(A[(k, i)]))
            scale_inv = 0
            if scale != 0:
                scale_inv = 1 / scale
        if scale == 0 or ctx.isinf(scale_inv):
            E[i] = 0
            D[i] = 0
            T[i - 1] = 1
            continue
        if i == 1:
            F = A[(i - 1, i)]
            f = abs(F)
            E[i] = f
            D[i] = 0
            if f != 0:
                T[i - 1] = T[i] * F / f
            else:
                T[i - 1] = T[i]
            continue
        H = 0
        for k in xrange(0, i):
            ctx.re(A[(k, i)]) = None
            ii = ctx.im(A[(k, i)])
            H += rr * rr + ii * ii
            F = A[(i - 1, i)]
            f = abs(F)
            G = ctx.sqrt(H)
            H += G * f
            E[i] = scale * G
            if f != 0:
                F = F / f
                TZ = -T[i] * F
                G *= F
            else:
                TZ = -T[i]
        0 = None
        for j in xrange(0, i):
            A[(i, j)] = A[(j, i)] / H
            G = 0
            for k in xrange(0, j + 1):
                G += ctx.conj(A[(k, j)]) * A[(k, i)]
                for k in xrange(j + 1, i):
                    G += A[(j, k)] * A[(k, i)]
                    T[j] = G / H
                    F += ctx.conj(T[j]) * A[(j, i)]
                    HH = F / (2 * H)
                    for j in xrange(0, i):
                        F = A[(j, i)]
                        G = T[j] - HH * F
                        T[j] = G
                        for k in xrange(0, j + 1):
                            TZ = None
                            D[i] = H
                            for i in xrange(1, n):
                                E[i - 1] = E[i]
                                E[n - 1] = 0
                                D[0] = 0
                                for i in xrange(0, n):
                                    zw = D[i]
                                    D[i] = ctx.re(A[(i, i)])
                                    A[(i, i)] = zw
                                    return None


def c_he_tridiag_1(ctx, A, T):
    '''
    This routine forms the unitary matrix Q described in c_he_tridiag_0.

    parameters:
      A    (input/output) On input, A is the same matrix as delivered by
           c_he_tridiag_0. On output, A is set to Q.

      T    (input) On input, T is the same array as delivered by c_he_tridiag_0.

    '''
    n = A.rows
    for i in xrange(0, n):
        if A[(i, i)] != 0:
            for j in xrange(0, i):
                G = 0
                for k in xrange(0, i):
                    G += ctx.conj(A[(i, k)]) * A[(k, j)]
                    for k in xrange(0, i):
                        1 = None
                        for j in xrange(0, i):
                            A[(j, i)] = 0
                            A[(i, j)] = 0
                            for i in xrange(0, n):
                                for k in xrange(0, n):
                                    return None


def c_he_tridiag_2(ctx, A, T, B):
    '''
    This routine applied the unitary matrix Q described in c_he_tridiag_0
    onto the the matrix B, i.e. it forms Q*B.

    parameters:
      A    (input) On input, A is the same matrix as delivered by c_he_tridiag_0.

      T    (input) On input, T is the same array as delivered by c_he_tridiag_0.

      B    (input/output) On input, B is a complex matrix. On output B is replaced
           by Q*B.

    This routine is a python translation of the fortran routine htribk.f in the
    software library EISPACK (see netlib.org). See c_he_tridiag_0 for more
    references.
    '''
    n = A.rows
    for i in xrange(0, n):
        for k in xrange(0, n):
            for None in xrange(0, n):
                if A[(i, i)] != 0:
                    for j in xrange(0, n):
                        G = 0
                        for k in xrange(0, i):
                            G += ctx.conj(A[(i, k)]) * B[(k, j)]
                            for k in xrange(0, i):
                                return None


def tridiag_eigen(ctx, d, e, z = (False,)):
    '''
    This subroutine find the eigenvalues and the first components of the
    eigenvectors of a real symmetric tridiagonal matrix using the implicit
    QL method.

    parameters:

      d (input/output) real array of length n. on input, d contains the diagonal
        elements of the input matrix. on output, d contains the eigenvalues in
        ascending order.

      e (input) real array of length n. on input, e contains the offdiagonal
        elements of the input matrix in e[0:(n-1)]. On output, e has been
        destroyed.

      z (input/output) If z is equal to False, no eigenvectors will be computed.
        Otherwise on input z should have the format z[0:m,0:n] (i.e. a real or
        complex matrix of dimension (m,n) ). On output this matrix will be
        multiplied by the matrix of the eigenvectors (i.e. the columns of this
        matrix are the eigenvectors): z --> z*EV
        That means if z[i,j]={1 if j==j; 0 otherwise} on input, then on output
        z will contain the first m components of the eigenvectors. That means
        if m is equal to n, the i-th eigenvector will be z[:,i].

    This routine is a python translation (in slightly modified form) of the
    fortran routine imtql2.f in the software library EISPACK (see netlib.org)
    which itself is based on the algol procudure imtql2 desribed in:
     - num. math. 12, p. 377-383(1968) by matrin and wilkinson
     - modified in num. math. 15, p. 450(1970) by dubrulle
     - handbook for auto. comp., vol. II-linear algebra, p. 241-248 (1971)
    See also the routine gaussq.f in netlog.org or acm algorithm 726.
    '''
    n = len(d)
    e[n - 1] = 0
    iterlim = 2 * ctx.dps
    for l in xrange(n):
        j = 0
        m = l
        if m + 1 == n:
            pass
        elif abs(e[m]) <= ctx.eps * (abs(d[m]) + abs(d[m + 1])):
            pass
        else:
            m = m + 1
        if m == l:
            pass
        elif j >= iterlim:
            raise RuntimeError('tridiag_eigen: no convergence to an eigenvalue after %d iterations' % iterlim)
        j += 1
        p = d[l]
        g = (d[l + 1] - p) / (2 * e[l])
        r = ctx.hypot(g, 1)
        if g < 0:
            s = g - r
        else:
            s = g + r
        g = (d[m] - p) + e[l] / s
        (s, c, p) = (1, 1, 0)
        for i in xrange(m - 1, l - 1, -1):
            f = s * e[i]
            b = c * e[i]
            if abs(f) > abs(g):
                c = g / f
                r = ctx.hypot(c, 1)
                e[i + 1] = f * r
                s = 1 / r
                c = c * s
            else:
                s = f / g
                r = ctx.hypot(s, 1)
                e[i + 1] = g * r
                c = 1 / r
                s = s * c
            g = d[i + 1] - p
            r = (d[i] - g) * s + 2 * c * b
            p = s * r
            d[i + 1] = g + p
            g = c * r - b
            if not isinstance(z, bool):
                for w in xrange(z.rows):
                    f = z[(w, i + 1)]
                    z[(w, i + 1)] = s * z[(w, i)] + c * f
                    z[(w, i)] = c * z[(w, i)] - s * f
                    d[l] = d[l] - p
                    e[l] = g
                    e[m] = 0
                    for ii in xrange(1, n):
                        i = ii - 1
                        k = i
                        p = d[i]
                        for j in xrange(ii, n):
                            if d[j] >= p:
                                continue
                            k = j
                            p = d[k]
                            if k == i:
                                continue
                        d[k] = d[i]
                        d[i] = p
                        if not isinstance(z, bool):
                            for w in xrange(z.rows):
                                p = z[(w, i)]
                                z[(w, i)] = z[(w, k)]
                                z[(w, k)] = p
                                return None

eigsy = (lambda ctx, A, eigvals_only, overwrite_a = (False, False): if not overwrite_a:
A = A.copy()d = ctx.zeros(A.rows, 1)e = ctx.zeros(A.rows, 1)if eigvals_only:
r_sy_tridiag(ctx, A, d, e, calc_ev = False)tridiag_eigen(ctx, d, e, False)dNone(ctx, A, d, e, calc_ev = True)tridiag_eigen(ctx, d, e, A)(d, A))()
eighe = (lambda ctx, A, eigvals_only, overwrite_a = (False, False): if not overwrite_a:
A = A.copy()d = ctx.zeros(A.rows, 1)e = ctx.zeros(A.rows, 1)t = ctx.zeros(A.rows, 1)if eigvals_only:
c_he_tridiag_0(ctx, A, d, e, t)tridiag_eigen(ctx, d, e, False)dNone(ctx, A, d, e, t)B = ctx.eye(A.rows)tridiag_eigen(ctx, d, e, B)c_he_tridiag_2(ctx, A, t, B)(d, B))()
eigh = (lambda ctx, A, eigvals_only, overwrite_a = (False, False): pass# WARNING: Decompyle incomplete
)()
gauss_quadrature = (lambda ctx, n, qtype, alpha, beta = ('legendre', 0, 0): d = ctx.zeros(n, 1)e = ctx.zeros(n, 1)z = ctx.zeros(1, n)z[(0, 0)] = 1if qtype == 'legendre':
w = 2for i in xrange(n):
j = i + 1e[i] = ctx.sqrt(j * j / (4 * j * j - ctx.mpf(1)))if qtype == 'legendre01':
w = 1for i in xrange(n):
d[i] = 1 / ctx.mpf(2)j = i + 1e[i] = ctx.sqrt(j * j / (16 * j * j - ctx.mpf(4)))if qtype == 'hermite':
w = ctx.sqrt(ctx.pi)for i in xrange(n):
j = i + 1e[i] = ctx.sqrt(j / ctx.mpf(2))if qtype == 'laguerre':
w = 1for i in xrange(n):
j = i + 1d[i] = 2 * j - 1e[i] = jif qtype == 'chebyshev1':
w = ctx.pifor i in xrange(n):
e[i] = 1 / ctx.mpf(2)e[0] = ctx.sqrt(1 / ctx.mpf(2))if qtype == 'chebyshev2':
w = ctx.pi / 2for i in xrange(n):
e[i] = 1 / ctx.mpf(2)if qtype == 'glaguerre':
w = ctx.gamma(1 + alpha)for i in xrange(n):
j = i + 1d[i] = (2 * j - 1) + alphae[i] = ctx.sqrt(j * (j + alpha))if qtype == 'jacobi':
alpha = ctx.mpf(alpha)beta = ctx.mpf(beta)ab = alpha + betaabi = ab + 2w = 2 ** (ab + 1) * ctx.gamma(alpha + 1) * ctx.gamma(beta + 1) / ctx.gamma(abi)d[0] = (beta - alpha) / abie[0] = ctx.sqrt(4 * (1 + alpha) * (1 + beta) / ((abi + 1) * abi * abi))a2b2 = beta * beta - alpha * alphafor i in xrange(1, n):
j = i + 1abi = 2 * j + abd[i] = a2b2 / ((abi - 2) * abi)e[i] = ctx.sqrt(4 * j * (j + alpha) * (j + beta) * (j + ab) / ((abi * abi - 1) * abi * abi))if isinstance(qtype, str):
raise ValueError('unknown quadrature rule "%s"' % qtype)if not isinstance(qtype, str):
w = qtype(d, e)# WARNING: Decompyle incomplete
)()

def svd_r_raw(ctx, A, V, calc_u = (False, False)):
    """
    This routine computes the singular value decomposition of a matrix A.
    Given A, two orthogonal matrices U and V are calculated such that

                    A = U S V

    where S is a suitable shaped matrix whose off-diagonal elements are zero.
    The diagonal elements of S are the singular values of A, i.e. the
    squareroots of the eigenvalues of A' A or A A'. Here ' denotes the transpose.
    Householder bidiagonalization and a variant of the QR algorithm is used.

    overview of the matrices :

      A : m*n       A gets replaced by U
      U : m*n       U replaces A. If n>m then only the first m*m block of U is
                    non-zero. column-orthogonal: U' U = B
                    here B is a n*n matrix whose first min(m,n) diagonal
                    elements are 1 and all other elements are zero.
      S : n*n       diagonal matrix, only the diagonal elements are stored in
                    the array S. only the first min(m,n) diagonal elements are non-zero.
      V : n*n       orthogonal: V V' = V' V = 1

    parameters:
      A        (input/output) On input, A contains a real matrix of shape m*n.
               On output, if calc_u is true A contains the column-orthogonal
               matrix U; otherwise A is simply used as workspace and thus destroyed.

      V        (input/output) if false, the matrix V is not calculated. otherwise
               V must be a matrix of shape n*n.

      calc_u   (input) If true, the matrix U is calculated and replaces A.
               if false, U is not calculated and A is simply destroyed

    return value:
      S        an array of length n containing the singular values of A sorted by
               decreasing magnitude. only the first min(m,n) elements are non-zero.

    This routine is a python translation of the fortran routine svd.f in the
    software library EISPACK (see netlib.org) which itself is based on the
    algol procedure svd described in:
      - num. math. 14, 403-420(1970) by golub and reinsch.
      - wilkinson/reinsch: handbook for auto. comp., vol ii-linear algebra, 134-151(1971).

    """
    n = A.cols
    m = A.rows
    S = ctx.zeros(n, 1)
    work = ctx.zeros(n, 1)
    g = 0
    scale = 0
    anorm = 0
    maxits = 3 * ctx.dps
    for i in xrange(n):
        work[i] = scale * g
        g = 0
        s = 0
        scale = 0
        if i < m:
            for k in xrange(i, m):
                scale += ctx.fabs(A[(k, i)])
                if scale != 0:
                    for k in xrange(i, m):
                        s += A[(k, i)] * A[(k, i)] = None
                        f = A[(i, i)]
                        g = -ctx.sqrt(s)
                        if f < 0:
                            g = -g
                    h = f * g - s
                    A[(i, i)] = f - g
                    for j in xrange(i + 1, n):
                        s = 0
                        for k in xrange(i, m):
                            s += A[(k, i)] * A[(k, j)]
                            f = s / h
                            for k in xrange(i, m):
                                for None in xrange(i, m):
                                    scale * g = None
                                    g = 0
                                    s = 0
                                    scale = 0
                                    if i < m and i != n - 1:
                                        for k in xrange(i + 1, n):
                                            scale += ctx.fabs(A[(i, k)])
                                            if scale:
                                                for k in xrange(i + 1, n):
                                                    s += A[(i, k)] * A[(i, k)] = None
                                                    f = A[(i, i + 1)]
                                                    g = -ctx.sqrt(s)
                                                    if f < 0:
                                                        g = -g
                                                h = f * g - s
                                                A[(i, i + 1)] = f - g
                                                for k in xrange(i + 1, n):
                                                    work[k] = A[(i, k)] / h
                                                    for j in xrange(i + 1, m):
                                                        s = 0
                                                        for k in xrange(i + 1, n):
                                                            s += A[(j, k)] * A[(i, k)]
                                                            for k in xrange(i + 1, n):
                                                                for None in xrange(i + 1, n):
                                                                    max(anorm, ctx.fabs(S[i]) + ctx.fabs(work[i])) = None
                                                                    if not isinstance(V, bool):
                                                                        for i in xrange(n - 2, -1, -1):
                                                                            V[(i + 1, i + 1)] = 1
                                                                            if work[i + 1] != 0:
                                                                                for j in xrange(i + 1, n):
                                                                                    V[(i, j)] = A[(i, j)] / A[(i, i + 1)] / work[i + 1]
                                                                                    for j in xrange(i + 1, n):
                                                                                        s = 0
                                                                                        for k in xrange(i + 1, n):
                                                                                            s += A[(i, k)] * V[(j, k)]
                                                                                            for k in xrange(i + 1, n):
                                                                                                for None in xrange(i + 1, n):
                                                                                                    V[(j, i)] = 0
                                                                                                    V[(i, j)] = 0
                                                                                                    V[(0, 0)] = 1
                                                                                                    if m < n:
                                                                                                        minnm = m
                                                                                                    else:
                                                                                                        minnm = n
    if calc_u:
        for i in xrange(minnm - 1, -1, -1):
            g = S[i]
            for j in xrange(i + 1, n):
                A[(i, j)] = 0
                if g != 0:
                    g = 1 / g
                    for j in xrange(i + 1, n):
                        s = 0
                        for k in xrange(i + 1, m):
                            s += A[(k, i)] * A[(k, j)]
                            f = (s / A[(i, i)]) * g
                            for k in xrange(i, m):
                                for None in xrange(i, m):
                                    pass
                                for None in xrange(i, m):
                                    A[(j, i)] = 0
                                    for None in xrange(n - 1, -1, -1):
                                        its = 0
                                        its += 1
                                        flag = True
                                        for l in xrange(k, -1, -1):
                                            nm = l - 1
                                            if ctx.fabs(work[l]) + anorm == anorm:
                                                flag = False
                                            elif ctx.fabs(S[nm]) + anorm == anorm:
                                                pass
                                            
                                            if flag:
                                                c = 0
                                                s = 1
                                                for i in xrange(l, k + 1):
                                                    f = s * work[i]
                                                    if ctx.fabs(f) + anorm == anorm:
                                                        pass
                                                    else:
                                                        S[i] = None
                                                        h = ctx.hypot(f, g)
                                                        S[i] = h
                                                        h = 1 / h
                                                        c = g * h
                                                        s = -f * h
                                                        if calc_u:
                                                            for j in xrange(m):
                                                                y = A[(j, nm)]
                                                                z = A[(j, i)]
                                                                A[(j, nm)] = y * c + z * s
                                                                A[(j, i)] = z * c - y * s
                                                                z = S[k]
                                                                if l == k:
                                                                    if z < 0:
                                                                        S[k] = -z
                                                                        if not isinstance(V, bool):
                                                                            for j in xrange(n):
                                                                                V[(k, j)] = -V[(k, j)]
                                                                            if its >= maxits:
                                                                                raise RuntimeError('svd: no convergence to an eigenvalue after %d iterations' % its)
                                                                            x = S[l]
                                                                            nm = k - 1
                                                                            y = S[nm]
                                                                            g = work[nm]
                                                                            h = work[k]
                                                                            f = ((y - z) * (y + z) + (g - h) * (g + h)) / (2 * h * y)
                                                                            g = ctx.hypot(f, 1)
                                                                            if f >= 0:
                                                                                f = ((x - z) * (x + z) + h * (y / (f + g) - h)) / x
                                                                            else:
                                                                                f = ((x - z) * (x + z) + h * (y / (f - g) - h)) / x
                                        c = 1
                                        s = 1
                                        for j in xrange(l, nm + 1):
                                            g = work[j + 1]
                                            y = S[j + 1]
                                            h = s * g
                                            g = c * g
                                            z = ctx.hypot(f, h)
                                            work[j] = z
                                            c = f / z
                                            s = h / z
                                            f = x * c + g * s
                                            g = g * c - x * s
                                            h = y * s
                                            y *= c
                                            if not isinstance(V, bool):
                                                for jj in xrange(n):
                                                    x = V[(j, jj)]
                                                    z = V[(j + 1, jj)]
                                                    V[(j, jj)] = x * c + z * s
                                                    V[(j + 1, jj)] = z * c - x * s
                                                    z = ctx.hypot(f, h)
                                                    S[j] = z
                                                    if z != 0:
                                                        z = 1 / z
                                                        c = f * z
                                                        s = h * z
                                            f = c * g + s * y
                                            x = c * y - s * g
                                            if calc_u:
                                                for jj in xrange(m):
                                                    y = A[(jj, j)]
                                                    z = A[(jj, j + 1)]
                                                    A[(jj, j)] = y * c + z * s
                                                    A[(jj, j + 1)] = z * c - y * s
                                                    work[l] = 0
                                                    work[k] = f
                                                    S[k] = x
                                                    for i in xrange(n):
                                                        imax = i
                                                        s = ctx.fabs(S[i])
                                                        for j in xrange(i + 1, n):
                                                            c = ctx.fabs(S[j])
                                                            if c > s:
                                                                s = c
                                                                imax = j
                                                            if imax != i:
                                                                z = S[i]
                                                                S[i] = S[imax]
                                                                S[imax] = z
                                                                if calc_u:
                                                                    for j in xrange(m):
                                                                        z = A[(j, i)]
                                                                        A[(j, i)] = A[(j, imax)]
                                                                        A[(j, imax)] = z
                                                                        if not isinstance(V, bool):
                                                                            for j in xrange(n):
                                                                                z = V[(i, j)]
                                                                                V[(i, j)] = V[(imax, j)]
                                                                                V[(imax, j)] = z
                                                                                return S


def svd_c_raw(ctx, A, V, calc_u = (False, False)):
    """
    This routine computes the singular value decomposition of a matrix A.
    Given A, two unitary matrices U and V are calculated such that

                    A = U S V

    where S is a suitable shaped matrix whose off-diagonal elements are zero.
    The diagonal elements of S are the singular values of A, i.e. the
    squareroots of the eigenvalues of A' A or A A'. Here ' denotes the hermitian
    transpose (i.e. transposition and conjugation). Householder bidiagonalization
    and a variant of the QR algorithm is used.

    overview of the matrices :

      A : m*n       A gets replaced by U
      U : m*n       U replaces A. If n>m then only the first m*m block of U is
                    non-zero. column-unitary: U' U = B
                    here B is a n*n matrix whose first min(m,n) diagonal
                    elements are 1 and all other elements are zero.
      S : n*n       diagonal matrix, only the diagonal elements are stored in
                    the array S. only the first min(m,n) diagonal elements are non-zero.
      V : n*n       unitary: V V' = V' V = 1

    parameters:
      A        (input/output) On input, A contains a complex matrix of shape m*n.
               On output, if calc_u is true A contains the column-unitary
               matrix U; otherwise A is simply used as workspace and thus destroyed.

      V        (input/output) if false, the matrix V is not calculated. otherwise
               V must be a matrix of shape n*n.

      calc_u   (input) If true, the matrix U is calculated and replaces A.
               if false, U is not calculated and A is simply destroyed

    return value:
      S        an array of length n containing the singular values of A sorted by
               decreasing magnitude. only the first min(m,n) elements are non-zero.

    This routine is a python translation of the fortran routine svd.f in the
    software library EISPACK (see netlib.org) which itself is based on the
    algol procedure svd described in:
      - num. math. 14, 403-420(1970) by golub and reinsch.
      - wilkinson/reinsch: handbook for auto. comp., vol ii-linear algebra, 134-151(1971).

    """
    n = A.cols
    m = A.rows
    S = ctx.zeros(n, 1)
    work = ctx.zeros(n, 1)
    lbeta = ctx.zeros(n, 1)
    rbeta = ctx.zeros(n, 1)
    dwork = ctx.zeros(n, 1)
    g = 0
    scale = 0
    anorm = 0
    maxits = 3 * ctx.dps
    for i in xrange(n):
        dwork[i] = scale * g
        g = 0
        s = 0
        scale = 0
        if i < m:
            for k in xrange(i, m):
                scale += ctx.fabs(ctx.re(A[(k, i)])) + ctx.fabs(ctx.im(A[(k, i)]))
                if scale != 0:
                    for k in xrange(i, m):
                        ctx.re(A[(k, i)]) = None
                        ai = ctx.im(A[(k, i)])
                        s += ar * ar + ai * ai
                        f = A[(i, i)]
                        g = -ctx.sqrt(s)
                        if ctx.re(f) < 0:
                            beta = -g - ctx.conj(f)
                            g = -g
                        else:
                            beta = -g + ctx.conj(f)
                    beta /= ctx.conj(beta)
                    beta += 1
                    h = 2 * (ctx.re(f) * g - s)
                    A[(i, i)] = f - g
                    beta /= h
                    lbeta[i] = beta / scale / scale
                    for j in xrange(i + 1, n):
                        s = 0
                        for k in xrange(i, m):
                            s += ctx.conj(A[(k, i)]) * A[(k, j)]
                            f = beta * s
                            for k in xrange(i, m):
                                for None in xrange(i, m):
                                    scale * g = None
                                    g = 0
                                    s = 0
                                    scale = 0
                                    if i < m and i != n - 1:
                                        for k in xrange(i + 1, n):
                                            scale += ctx.fabs(ctx.re(A[(i, k)])) + ctx.fabs(ctx.im(A[(i, k)]))
                                            if scale:
                                                for k in xrange(i + 1, n):
                                                    ctx.re(A[(i, k)]) = None
                                                    ai = ctx.im(A[(i, k)])
                                                    s += ar * ar + ai * ai
                                                    f = A[(i, i + 1)]
                                                    g = -ctx.sqrt(s)
                                                    if ctx.re(f) < 0:
                                                        beta = -g - ctx.conj(f)
                                                        g = -g
                                                    else:
                                                        beta = -g + ctx.conj(f)
                                                beta /= ctx.conj(beta)
                                                beta += 1
                                                h = 2 * (ctx.re(f) * g - s)
                                                A[(i, i + 1)] = f - g
                                                beta /= h
                                                rbeta[i] = beta / scale / scale
                                                for k in xrange(i + 1, n):
                                                    work[k] = A[(i, k)]
                                                    for j in xrange(i + 1, m):
                                                        s = 0
                                                        for k in xrange(i + 1, n):
                                                            s += ctx.conj(A[(i, k)]) * A[(j, k)]
                                                            f = s * beta
                                                            for k in xrange(i + 1, n):
                                                                for None in xrange(i + 1, n):
                                                                    max(anorm, ctx.fabs(S[i]) + ctx.fabs(dwork[i])) = None
                                                                    if not isinstance(V, bool):
                                                                        for i in xrange(n - 2, -1, -1):
                                                                            V[(i + 1, i + 1)] = 1
                                                                            if dwork[i + 1] != 0:
                                                                                f = ctx.conj(rbeta[i])
                                                                                for j in xrange(i + 1, n):
                                                                                    V[(i, j)] = A[(i, j)] * f
                                                                                    for j in xrange(i + 1, n):
                                                                                        s = 0
                                                                                        for k in xrange(i + 1, n):
                                                                                            s += ctx.conj(A[(i, k)]) * V[(j, k)]
                                                                                            for k in xrange(i + 1, n):
                                                                                                for None in xrange(i + 1, n):
                                                                                                    V[(j, i)] = 0
                                                                                                    V[(i, j)] = 0
                                                                                                    V[(0, 0)] = 1
                                                                                                    if m < n:
                                                                                                        minnm = m
                                                                                                    else:
                                                                                                        minnm = n
    if calc_u:
        for i in xrange(minnm - 1, -1, -1):
            g = S[i]
            for j in xrange(i + 1, n):
                A[(i, j)] = 0
                if g != 0:
                    g = 1 / g
                    for j in xrange(i + 1, n):
                        s = 0
                        for k in xrange(i + 1, m):
                            s += ctx.conj(A[(k, i)]) * A[(k, j)]
                            f = s * ctx.conj(lbeta[i])
                            for k in xrange(i, m):
                                for None in xrange(i, m):
                                    pass
                                for None in xrange(i, m):
                                    A[(j, i)] = 0
                                    for None in xrange(n - 1, -1, -1):
                                        its = 0
                                        its += 1
                                        flag = True
                                        for l in xrange(k, -1, -1):
                                            nm = l - 1
                                            if ctx.fabs(dwork[l]) + anorm == anorm:
                                                flag = False
                                            elif ctx.fabs(S[nm]) + anorm == anorm:
                                                pass
                                            
                                            if flag:
                                                c = 0
                                                s = 1
                                                for i in xrange(l, k + 1):
                                                    f = s * dwork[i]
                                                    if ctx.fabs(f) + anorm == anorm:
                                                        pass
                                                    else:
                                                        S[i] = None
                                                        h = ctx.hypot(f, g)
                                                        S[i] = h
                                                        h = 1 / h
                                                        c = g * h
                                                        s = -f * h
                                                        if calc_u:
                                                            for j in xrange(m):
                                                                y = A[(j, nm)]
                                                                z = A[(j, i)]
                                                                A[(j, nm)] = y * c + z * s
                                                                A[(j, i)] = z * c - y * s
                                                                z = S[k]
                                                                if l == k:
                                                                    if z < 0:
                                                                        S[k] = -z
                                                                        if not isinstance(V, bool):
                                                                            for j in xrange(n):
                                                                                V[(k, j)] = -V[(k, j)]
                                                                            if its >= maxits:
                                                                                raise RuntimeError('svd: no convergence to an eigenvalue after %d iterations' % its)
                                                                            x = S[l]
                                                                            nm = k - 1
                                                                            y = S[nm]
                                                                            g = dwork[nm]
                                                                            h = dwork[k]
                                                                            f = ((y - z) * (y + z) + (g - h) * (g + h)) / (2 * h * y)
                                                                            g = ctx.hypot(f, 1)
                                                                            if f >= 0:
                                                                                f = ((x - z) * (x + z) + h * (y / (f + g) - h)) / x
                                                                            else:
                                                                                f = ((x - z) * (x + z) + h * (y / (f - g) - h)) / x
                                        c = 1
                                        s = 1
                                        for j in xrange(l, nm + 1):
                                            g = dwork[j + 1]
                                            y = S[j + 1]
                                            h = s * g
                                            g = c * g
                                            z = ctx.hypot(f, h)
                                            dwork[j] = z
                                            c = f / z
                                            s = h / z
                                            f = x * c + g * s
                                            g = g * c - x * s
                                            h = y * s
                                            y *= c
                                            if not isinstance(V, bool):
                                                for jj in xrange(n):
                                                    x = V[(j, jj)]
                                                    z = V[(j + 1, jj)]
                                                    V[(j, jj)] = x * c + z * s
                                                    V[(j + 1, jj)] = z * c - x * s
                                                    z = ctx.hypot(f, h)
                                                    S[j] = z
                                                    if z != 0:
                                                        z = 1 / z
                                                        c = f * z
                                                        s = h * z
                                            f = c * g + s * y
                                            x = c * y - s * g
                                            if calc_u:
                                                for jj in xrange(m):
                                                    y = A[(jj, j)]
                                                    z = A[(jj, j + 1)]
                                                    A[(jj, j)] = y * c + z * s
                                                    A[(jj, j + 1)] = z * c - y * s
                                                    dwork[l] = 0
                                                    dwork[k] = f
                                                    S[k] = x
                                                    for i in xrange(n):
                                                        imax = i
                                                        s = ctx.fabs(S[i])
                                                        for j in xrange(i + 1, n):
                                                            c = ctx.fabs(S[j])
                                                            if c > s:
                                                                s = c
                                                                imax = j
                                                            if imax != i:
                                                                z = S[i]
                                                                S[i] = S[imax]
                                                                S[imax] = z
                                                                if calc_u:
                                                                    for j in xrange(m):
                                                                        z = A[(j, i)]
                                                                        A[(j, i)] = A[(j, imax)]
                                                                        A[(j, imax)] = z
                                                                        if not isinstance(V, bool):
                                                                            for j in xrange(n):
                                                                                z = V[(i, j)]
                                                                                V[(i, j)] = V[(imax, j)]
                                                                                V[(imax, j)] = z
                                                                                return S

svd_r = (lambda ctx, A, full_matrices, compute_uv, overwrite_a = (False, True, False): n = A.colsm = A.rowsif not compute_uv:
if not overwrite_a:
A = A.copy()S = svd_r_raw(ctx, A, V = False, calc_u = False)S = S[:min(m, n)]Sif None and n < m:
V = ctx.zeros(m, m)A0 = ctx.zeros(m, m)A0[(:, :n)] = AS = svd_r_raw(ctx, A0, V, calc_u = True)S = S[:n]V = V[(:n, :n)](A0, S, V)if not None:
A = A.copy()V = ctx.zeros(n, n)S = svd_r_raw(ctx, A, V, calc_u = True)if n > m:
if full_matrices == False:
V = V[(:m, :)]S = S[:m]A = A[(:, :m)](A, S, V))()
svd_c = (lambda ctx, A, full_matrices, compute_uv, overwrite_a = (False, True, False): n = A.colsm = A.rowsif not compute_uv:
if not overwrite_a:
A = A.copy()S = svd_c_raw(ctx, A, V = False, calc_u = False)S = S[:min(m, n)]Sif None and n < m:
V = ctx.zeros(m, m)A0 = ctx.zeros(m, m)A0[(:, :n)] = AS = svd_c_raw(ctx, A0, V, calc_u = True)S = S[:n]V = V[(:n, :n)](A0, S, V)if not None:
A = A.copy()V = ctx.zeros(n, n)S = svd_c_raw(ctx, A, V, calc_u = True)if n > m:
if full_matrices == False:
V = V[(:m, :)]S = S[:m]A = A[(:, :m)](A, S, V))()
svd = (lambda ctx, A, full_matrices, compute_uv, overwrite_a = (False, True, False): pass# WARNING: Decompyle incomplete
)()
