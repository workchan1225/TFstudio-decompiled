# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: factortools.pyc (Python 3.11)

'''Polynomial factorization routines in characteristic zero. '''
from sympy.external.gmpy import GROUND_TYPES
from sympy.core.random import _randint
from sympy.polys.galoistools import gf_from_int_poly, gf_to_int_poly, gf_lshift, gf_add_mul, gf_mul, gf_div, gf_rem, gf_gcdex, gf_sqf_p, gf_factor_sqf, gf_factor
from sympy.polys.densebasic import dup_LC, dmp_LC, dmp_ground_LC, dup_TC, dup_convert, dmp_convert, dup_degree, dmp_degree, dmp_degree_in, dmp_degree_list, dmp_from_dict, dmp_zero_p, dmp_one, dmp_nest, dmp_raise, dup_strip, dmp_ground, dup_inflate, dmp_exclude, dmp_include, dmp_inject, dmp_eject, dup_terms_gcd, dmp_terms_gcd
from sympy.polys.densearith import dup_neg, dmp_neg, dup_add, dmp_add, dup_sub, dmp_sub, dup_mul, dmp_mul, dup_sqr, dmp_pow, dup_div, dmp_div, dup_quo, dmp_quo, dmp_expand, dmp_add_mul, dup_sub_mul, dmp_sub_mul, dup_lshift, dup_max_norm, dmp_max_norm, dup_l1_norm, dup_mul_ground, dmp_mul_ground, dup_quo_ground, dmp_quo_ground
from sympy.polys.densetools import dup_clear_denoms, dmp_clear_denoms, dup_trunc, dmp_ground_trunc, dup_content, dup_monic, dmp_ground_monic, dup_primitive, dmp_ground_primitive, dmp_eval_tail, dmp_eval_in, dmp_diff_eval_in, dup_shift, dmp_shift, dup_mirror
from sympy.polys.euclidtools import dmp_primitive, dup_inner_gcd, dmp_inner_gcd
from sympy.polys.sqfreetools import dup_sqf_p, dup_sqf_norm, dmp_sqf_norm, dup_sqf_part, dmp_sqf_part, _dup_check_degrees, _dmp_check_degrees
from sympy.polys.polyutils import _sort_factors
from sympy.polys.polyconfig import query
from sympy.polys.polyerrors import ExtraneousFactors, DomainError, CoercionFailed, EvaluationFailed
from sympy.utilities import subsets
from math import ceil as _ceil, log as _log, log2 as _log2
if GROUND_TYPES == 'flint':
    from flint import fmpz_poly
else:
    fmpz_poly = None

def dup_trial_division(f, factors, K):
    '''
    Determine multiplicities of factors for a univariate polynomial
    using trial division.

    An error will be raised if any factor does not divide ``f``.
    '''
    result = []
    for factor in factors:
        k = 0
        (q, r) = dup_div(f, factor, K)
        if not r:
            k = k + 1
            f = q
        
    continue
    if k == 0:
        raise RuntimeError('trial division failed')
    result.append((factor, k))
    continue
    return _sort_factors(result)


def dmp_trial_division(f, factors, u, K):
    '''
    Determine multiplicities of factors for a multivariate polynomial
    using trial division.

    An error will be raised if any factor does not divide ``f``.
    '''
    result = []
    for factor in factors:
        k = 0
        (q, r) = dmp_div(f, factor, u, K)
        if dmp_zero_p(r, u):
            k = k + 1
            f = q
        
    continue
    if k == 0:
        raise RuntimeError('trial division failed')
    result.append((factor, k))
    continue
    return _sort_factors(result)


def dup_zz_mignotte_bound(f, K):
    '''
    The Knuth-Cohen variant of Mignotte bound for
    univariate polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> f = x**3 + 14*x**2 + 56*x + 64
    >>> R.dup_zz_mignotte_bound(f)
    152

    By checking ``factor(f)`` we can see that max coeff is 8

    Also consider a case that ``f`` is irreducible for example
    ``f = 2*x**2 + 3*x + 4``. To avoid a bug for these cases, we return the
    bound plus the max coefficient of ``f``

    >>> f = 2*x**2 + 3*x + 4
    >>> R.dup_zz_mignotte_bound(f)
    6

    Lastly, to see the difference between the new and the old Mignotte bound
    consider the irreducible polynomial:

    >>> f = 87*x**7 + 4*x**6 + 80*x**5 + 17*x**4 + 9*x**3 + 12*x**2 + 49*x + 26
    >>> R.dup_zz_mignotte_bound(f)
    744

    The new Mignotte bound is 744 whereas the old one (SymPy 1.5.1) is 1937664.


    References
    ==========

    ..[1] [Abbott13]_

    '''
    binomial = binomial
    import sympy.functions.combinatorial.factorials
    d = dup_degree(f)
    delta = _ceil(d / 2)
    delta2 = _ceil(delta / 2)
    eucl_norm = sum((lambda .0: pass# WARNING: Decompyle incomplete
)(f()))
    t1 = binomial(delta - 1, delta2)
    t2 = binomial(delta - 1, delta2 - 1)
    lc = K.abs(dup_LC(f, K))
    bound = t1 * eucl_norm + t2 * lc
    bound += dup_max_norm(f, K)
    bound = _ceil(bound / 2) * 2
    return bound


def dmp_zz_mignotte_bound(f, u, K):
    '''Mignotte bound for multivariate polynomials in `K[X]`. '''
    a = dmp_max_norm(f, u, K)
    b = abs(dmp_ground_LC(f, u, K))
    n = sum(dmp_degree_list(f, u))
    return K.sqrt(K(n + 1)) * 2 ** n * a * b


def dup_zz_hensel_step(m, f, g, h, s, t, K):
    '''
    One step in Hensel lifting in `Z[x]`.

    Given positive integer `m` and `Z[x]` polynomials `f`, `g`, `h`, `s`
    and `t` such that::

        f = g*h (mod m)
        s*g + t*h = 1 (mod m)

        lc(f) is not a zero divisor (mod m)
        lc(h) = 1

        deg(f) = deg(g) + deg(h)
        deg(s) < deg(h)
        deg(t) < deg(g)

    returns polynomials `G`, `H`, `S` and `T`, such that::

        f = G*H (mod m**2)
        S*G + T*H = 1 (mod m**2)

    References
    ==========

    .. [1] [Gathen99]_

    '''
    M = m ** 2
    e = dup_sub_mul(f, g, h, K)
    e = dup_trunc(e, M, K)
    (q, r) = dup_div(dup_mul(s, e, K), h, K)
    q = dup_trunc(q, M, K)
    r = dup_trunc(r, M, K)
    u = dup_add(dup_mul(t, e, K), dup_mul(q, g, K), K)
    G = dup_trunc(dup_add(g, u, K), M, K)
    H = dup_trunc(dup_add(h, r, K), M, K)
    u = dup_add(dup_mul(s, G, K), dup_mul(t, H, K), K)
    b = dup_trunc(dup_sub(u, [
        K.one], K), M, K)
    (c, d) = dup_div(dup_mul(s, b, K), H, K)
    c = dup_trunc(c, M, K)
    d = dup_trunc(d, M, K)
    u = dup_add(dup_mul(t, b, K), dup_mul(c, G, K), K)
    S = dup_trunc(dup_sub(s, d, K), M, K)
    T = dup_trunc(dup_sub(t, u, K), M, K)
    return (G, H, S, T)


def dup_zz_hensel_lift(p, f, f_list, l, K):
    '''
    Multifactor Hensel lifting in `Z[x]`.

    Given a prime `p`, polynomial `f` over `Z[x]` such that `lc(f)`
    is a unit modulo `p`, monic pair-wise coprime polynomials `f_i`
    over `Z[x]` satisfying::

        f = lc(f) f_1 ... f_r (mod p)

    and a positive integer `l`, returns a list of monic polynomials
    `F_1,\\ F_2,\\ \\dots,\\ F_r` satisfying::

       f = lc(f) F_1 ... F_r (mod p**l)

       F_i = f_i (mod p), i = 1..r

    References
    ==========

    .. [1] [Gathen99]_

    '''
    r = len(f_list)
    lc = dup_LC(f, K)
    if r == 1:
        F = dup_mul_ground(f, K.gcdex(lc, p ** l)[0], K)
        return [
            dup_trunc(F, p ** l, K)]
    m = None
    k = r // 2
    d = int(_ceil(_log2(l)))
    g = gf_from_int_poly([
        lc], p)
    for f_i in f_list[:k]:
        g = gf_mul(g, gf_from_int_poly(f_i, p), p, K)
        h = gf_from_int_poly(f_list[k], p)
        for f_i in f_list[k + 1:]:
            h = gf_mul(h, gf_from_int_poly(f_i, p), p, K)
            (s, t, _) = gf_gcdex(g, h, p, K)
            g = gf_to_int_poly(g, p)
            h = gf_to_int_poly(h, p)
            s = gf_to_int_poly(s, p)
            t = gf_to_int_poly(t, p)
            for _ in range(1, d + 1):
                (g, h, s, t) = 
                m = dup_zz_hensel_step(m, f, g, h, s, t, K), m ** 2
                return dup_zz_hensel_lift(p, g, f_list[:k], l, K) + dup_zz_hensel_lift(p, h, f_list[k:], l, K)


def _test_pl(fc, q, pl):
    if q > pl // 2:
        q = q - pl
    if not q:
        return True
    return None % q == 0


def dup_zz_zassenhaus(f, K):
    '''Factor primitive square-free polynomials in `Z[x]`. '''
    pass
# WARNING: Decompyle incomplete


def dup_zz_irreducible_p(f, K):
    """Test irreducibility using Eisenstein's criterion. """
    lc = dup_LC(f, K)
    tc = dup_TC(f, K)
    e_fc = dup_content(f[1:], K)
    if e_fc:
        factorint = factorint
        import sympy.ntheory
        e_ff = factorint(int(e_fc))
        for p in e_ff.keys():
            if lc % p and tc % p ** 2:
                return True
            return None
            return None


def dup_cyclotomic_p(f, K, irreducible = (False,)):
    '''
    Efficiently test if ``f`` is a cyclotomic polynomial.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> f = x**16 + x**14 - x**10 + x**8 - x**6 + x**2 + 1
    >>> R.dup_cyclotomic_p(f)
    False

    >>> g = x**16 + x**14 - x**10 - x**8 - x**6 + x**2 + 1
    >>> R.dup_cyclotomic_p(g)
    True

    References
    ==========

    Bradford, Russell J., and James H. Davenport. "Effective tests for
    cyclotomic polynomials." In International Symposium on Symbolic and
    Algebraic Computation, pp. 244-251. Springer, Berlin, Heidelberg, 1988.

    '''
    if K.is_QQ:
        
        try:
            K = K.get_ring()
            K0 = K
            f = dup_convert(f, K0, K)
        except CoercionFailed:
            return False
            if not K.is_ZZ:
                return False
            lc = None(f, K)
            tc = dup_TC(f, K)
            if (lc != 1 or tc != -1) and tc != 1:
                return False
            if not None:
                (coeff, factors) = dup_factor_list(f, K)
                if coeff != K.one or factors != [
                    (f, 1)]:
                    return False
                n = None(f)
                h = []
                g = []
                for i in range(n, -1, -2):
                    g.insert(0, f[i])
                    for i in range(n - 1, -1, -2):
                        h.insert(0, f[i])
                        g = dup_sqr(dup_strip(g), K)
                        h = dup_sqr(dup_strip(h), K)
                        F = dup_sub(g, dup_lshift(h, 1, K), K)
                        if K.is_negative(dup_LC(F, K)):
                            F = dup_neg(F, K)

    if F == f:
        return True
    g = None(f, K)
    if K.is_negative(dup_LC(g, K)):
        g = dup_neg(g, K)
    if F == g and dup_cyclotomic_p(g, K):
        return True
    G = None(F, K)
    if dup_sqr(G, K) == F and dup_cyclotomic_p(G, K):
        return True


def dup_zz_cyclotomic_poly(n, K):
    '''Efficiently generate n-th cyclotomic polynomial. '''
    factorint = factorint
    import sympy.ntheory
    h = [
        K.one,
        -(K.one)]
    for p, k in factorint(n).items():
        h = dup_quo(dup_inflate(h, p, K), h, K)
        h = dup_inflate(h, p ** (k - 1), K)
        return h


def _dup_cyclotomic_decompose(n, K):
    pass
# WARNING: Decompyle incomplete


def dup_zz_cyclotomic_factor(f, K):
    """
    Efficiently factor polynomials `x**n - 1` and `x**n + 1` in `Z[x]`.

    Given a univariate polynomial `f` in `Z[x]` returns a list of factors
    of `f`, provided that `f` is in the form `x**n - 1` or `x**n + 1` for
    `n >= 1`. Otherwise returns None.

    Factorization is performed using cyclotomic decomposition of `f`,
    which makes this method much faster that any other direct factorization
    approach (e.g. Zassenhaus's).

    References
    ==========

    .. [1] [Weisstein09]_

    """
    tc_f = dup_TC(f, K)
    lc_f = dup_LC(f, K)
    if dup_degree(f) <= 0:
        return None
    if None != 1 or tc_f not in (-1, 1):
        return None
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(f[1:-1]()):
        return None
    n = None(f)
    F = _dup_cyclotomic_decompose(n, K)
    if not K.is_one(tc_f):
        return F
    H = None
    for h in _dup_cyclotomic_decompose(2 * n, K):
        if h not in F:
            H.append(h)
        return H


def dup_zz_factor_sqf(f, K):
    '''Factor square-free (non-primitive) polynomials in `Z[x]`. '''
    (cont, g) = dup_primitive(f, K)
    n = dup_degree(g)
    if dup_LC(g, K) < 0:
        g = dup_neg(g, K)
        cont = -cont
    if n <= 0:
        return (cont, [])
    if None == 1:
        return (cont, [
            g])
    if None('USE_IRREDUCIBLE_IN_FACTOR') and dup_zz_irreducible_p(g, K):
        return (cont, [
            g])
    factors = None
    if query('USE_CYCLOTOMIC_FACTOR'):
        factors = dup_zz_cyclotomic_factor(g, K)
# WARNING: Decompyle incomplete


def dup_zz_factor(f, K):
    '''
    Factor (non square-free) polynomials in `Z[x]`.

    Given a univariate polynomial `f` in `Z[x]` computes its complete
    factorization `f_1, ..., f_n` into irreducibles over integers::

                f = content(f) f_1**k_1 ... f_n**k_n

    The factorization is computed by reducing the input polynomial
    into a primitive square-free polynomial and factoring it using
    Zassenhaus algorithm. Trial division is used to recover the
    multiplicities of factors.

    The result is returned as a tuple consisting of::

              (content(f), [(f_1, k_1), ..., (f_n, k_n))

    Examples
    ========

    Consider the polynomial `f = 2*x**4 - 2`::

        >>> from sympy.polys import ring, ZZ
        >>> R, x = ring("x", ZZ)

        >>> R.dup_zz_factor(2*x**4 - 2)
        (2, [(x - 1, 1), (x + 1, 1), (x**2 + 1, 1)])

    In result we got the following factorization::

                 f = 2 (x - 1) (x + 1) (x**2 + 1)

    Note that this is a complete factorization over integers,
    however over Gaussian integers we can factor the last term.

    By default, polynomials `x**n - 1` and `x**n + 1` are factored
    using cyclotomic decomposition to speedup computations. To
    disable this behaviour set cyclotomic=False.

    References
    ==========

    .. [1] [Gathen99]_

    '''
    if GROUND_TYPES == 'flint':
        f_flint = fmpz_poly(f[::-1])
        (cont, factors) = f_flint.factor()
        factors = factors()
        return (cont, _sort_factors(factors))
    (cont, g) = None(f, K)
    n = dup_degree(g)
    if dup_LC(g, K) < 0:
        g = dup_neg(g, K)
        cont = -cont
    if n <= 0:
        return (cont, [])
    if None == 1:
        return (cont, [
            (g, 1)])
    if None('USE_IRREDUCIBLE_IN_FACTOR') and dup_zz_irreducible_p(g, K):
        return (cont, [
            (g, 1)])
    g = None(g, K)
    H = None
    if query('USE_CYCLOTOMIC_FACTOR'):
        H = dup_zz_cyclotomic_factor(g, K)
# WARNING: Decompyle incomplete


def dmp_zz_wang_non_divisors(E, cs, ct, K):
    '''Wang/EEZ: Compute a set of valid divisors.  '''
    result = [
        cs * ct]
# WARNING: Decompyle incomplete


def dmp_zz_wang_test_points(f, T, ct, A, u, K):
    '''Wang/EEZ: Test evaluation points for suitability. '''
    pass
# WARNING: Decompyle incomplete


def dmp_zz_wang_lead_coeffs(f, T, cs, E, H, A, u, K):
    '''Wang/EEZ: Compute correct leading coefficients. '''
    v = u - 1
    J = [
        0] * len(E)
    C = []
# WARNING: Decompyle incomplete


def dup_zz_diophantine(F, m, p, K):
    '''Wang/EEZ: Solve univariate Diophantine equations. '''
    if len(F) == 2:
        (a, b) = F
        f = gf_from_int_poly(a, p)
        g = gf_from_int_poly(b, p)
        (s, t, G) = gf_gcdex(g, f, p, K)
        s = gf_lshift(s, m, K)
        t = gf_lshift(t, m, K)
        (q, s) = gf_div(s, f, p, K)
        t = gf_add_mul(t, q, g, p, K)
        s = gf_to_int_poly(s, p)
        t = gf_to_int_poly(t, p)
        result = [
            s,
            t]
    else:
        G = [
            F[-1]]
        for f in reversed(F[1:-1]):
            G.insert(0, dup_mul(f, G[0], K))
            T = [
                [
                    1]]
            S = []
            for f, g in zip(F, G):
                (t, s) = dmp_zz_diophantine([
                    g,
                    f], T[-1], [], 0, p, 1, K)
                T.append(t)
                S.append(s)
                S = S + [
                    T[-1]]
                result = []
                for s, f in zip(S, F):
                    s = gf_from_int_poly(s, p)
                    f = gf_from_int_poly(f, p)
                    r = gf_rem(gf_lshift(s, m, K), f, p, K)
                    s = gf_to_int_poly(r, p)
                    result.append(s)
                    return result


def dmp_zz_diophantine(F, c, A, d, p, u, K):
    '''Wang/EEZ: Solve multivariate Diophantine equations. '''
    pass
# WARNING: Decompyle incomplete


def dmp_zz_wang_hensel_lifting(f, H, LC, A, p, u, K):
    '''Wang/EEZ: Parallel Hensel lifting algorithm. '''
    v = u - 1
    n = len(A)
    S = [
        f]
    H = list(H)
    for i, a in enumerate(reversed(A[1:])):
        s = dmp_eval_in(S[0], a, n - i, u - i, K)
        S.insert(0, dmp_ground_trunc(s, p, v - i, K))
        d = max(dmp_degree_list(f, u)[1:])
        for j, s, a in zip(range(2, n + 2), S, A):
            w = j - 1
            G = list(H)
            J = A[j - 1:]
            I = A[:j - 2]
            for h, lc in enumerate(zip(H, LC)):
                lc = dmp_ground_trunc(dmp_eval_tail(lc, J, v, K), p, w - 1, K)
                H[i] = [
                    lc] + dmp_raise(h[1:], 1, w - 1, K)
                m = dmp_nest([
                    K.one,
                    -a], w, K)
                M = dmp_one(w, K)
                c = dmp_sub(s, dmp_expand(H, w, K), w, K)
                dj = dmp_degree_in(s, w, w)
                for k in range(0, dj):
                    if dmp_zero_p(c, w):
                        pass
                    else:
                        M = dmp_mul(M, m, w, K)
                        C = dmp_diff_eval_in(c, k + 1, a, w, w, K)
                        if not dmp_zero_p(C, w - 1):
                            C = dmp_quo_ground(C, K.factorial(K(k) + 1), w - 1, K)
                            T = dmp_zz_diophantine(G, C, I, d, p, w - 1, K)
                            for h, t in enumerate(zip(H, T)):
                                h = dmp_add_mul(h, dmp_raise(t, 1, w - 1, K), M, w, K)
                                H[i] = dmp_ground_trunc(h, p, w, K)
                                h = dmp_sub(s, dmp_expand(H, w, K), w, K)
                                c = dmp_ground_trunc(h, p, w, K)
                                if dmp_expand(H, u, K) != f:
                                    raise ExtraneousFactors
                                return H


def dmp_zz_wang(f, u, K, mod, seed = (None, None)):
    """
    Factor primitive square-free polynomials in `Z[X]`.

    Given a multivariate polynomial `f` in `Z[x_1,...,x_n]`, which is
    primitive and square-free in `x_1`, computes factorization of `f` into
    irreducibles over integers.

    The procedure is based on Wang's Enhanced Extended Zassenhaus
    algorithm. The algorithm works by viewing `f` as a univariate polynomial
    in `Z[x_2,...,x_n][x_1]`, for which an evaluation mapping is computed::

                      x_2 -> a_2, ..., x_n -> a_n

    where `a_i`, for `i = 2, \\dots, n`, are carefully chosen integers.  The
    mapping is used to transform `f` into a univariate polynomial in `Z[x_1]`,
    which can be factored efficiently using Zassenhaus algorithm. The last
    step is to lift univariate factors to obtain true multivariate
    factors. For this purpose a parallel Hensel lifting procedure is used.

    The parameter ``seed`` is passed to _randint and can be used to seed randint
    (when an integer) or (for testing purposes) can be a sequence of numbers.

    References
    ==========

    .. [1] [Wang78]_
    .. [2] [Geddes92]_

    """
    pass
# WARNING: Decompyle incomplete


def dmp_zz_factor(f, u, K):
    '''
    Factor (non square-free) polynomials in `Z[X]`.

    Given a multivariate polynomial `f` in `Z[x]` computes its complete
    factorization `f_1, \\dots, f_n` into irreducibles over integers::

                 f = content(f) f_1**k_1 ... f_n**k_n

    The factorization is computed by reducing the input polynomial
    into a primitive square-free polynomial and factoring it using
    Enhanced Extended Zassenhaus (EEZ) algorithm. Trial division
    is used to recover the multiplicities of factors.

    The result is returned as a tuple consisting of::

             (content(f), [(f_1, k_1), ..., (f_n, k_n))

    Consider polynomial `f = 2*(x**2 - y**2)`::

        >>> from sympy.polys import ring, ZZ
        >>> R, x,y = ring("x,y", ZZ)

        >>> R.dmp_zz_factor(2*x**2 - 2*y**2)
        (2, [(x - y, 1), (x + y, 1)])

    In result we got the following factorization::

                    f = 2 (x - y) (x + y)

    References
    ==========

    .. [1] [Gathen99]_

    '''
    if not u:
        return dup_zz_factor(f, K)
    if None(f, u):
        return (K.zero, [])
    (cont, g) = None(f, u, K)
    if dmp_ground_LC(g, u, K) < 0:
        g = dmp_neg(g, u, K)
        cont = -cont
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(dmp_degree_list(g, u)()):
        return (cont, [])
    (G, g) = all(g, u, K)
    factors = []
    if dmp_degree(g, u) > 0:
        g = dmp_sqf_part(g, u, K)
        H = dmp_zz_wang(g, u, K)
        factors = dmp_trial_division(f, H, u, K)
    for g, k in dmp_zz_factor(G, u - 1, K)[1]:
        factors.insert(0, ([
            g], k))
        _dmp_check_degrees(f, u, factors)
        return (cont, _sort_factors(factors))


def dup_qq_i_factor(f, K0):
    '''Factor univariate polynomials into irreducibles in `QQ_I[x]`. '''
    pass
# WARNING: Decompyle incomplete


def dup_zz_i_factor(f, K0):
    '''Factor univariate polynomials into irreducibles in `ZZ_I[x]`. '''
    K1 = K0.get_field()
    f = dup_convert(f, K0, K1)
    (coeff, factors) = dup_qq_i_factor(f, K1)
    new_factors = []
    for fac, i in factors:
        (fac_denom, fac_num) = dup_clear_denoms(fac, K1)
        fac_num_ZZ_I = dup_convert(fac_num, K1, K0)
        (content, fac_prim) = dmp_ground_primitive(fac_num_ZZ_I, 0, K0)
        coeff = coeff * content ** i // fac_denom ** i
        new_factors.append((fac_prim, i))
        factors = new_factors
        coeff = K0.convert(coeff, K1)
        return (coeff, factors)


def dmp_qq_i_factor(f, u, K0):
    '''Factor multivariate polynomials into irreducibles in `QQ_I[X]`. '''
    pass
# WARNING: Decompyle incomplete


def dmp_zz_i_factor(f, u, K0):
    '''Factor multivariate polynomials into irreducibles in `ZZ_I[X]`. '''
    K1 = K0.get_field()
    f = dmp_convert(f, u, K0, K1)
    (coeff, factors) = dmp_qq_i_factor(f, u, K1)
    new_factors = []
    for fac, i in factors:
        (fac_denom, fac_num) = dmp_clear_denoms(fac, u, K1)
        fac_num_ZZ_I = dmp_convert(fac_num, u, K1, K0)
        (content, fac_prim) = dmp_ground_primitive(fac_num_ZZ_I, u, K0)
        coeff = coeff * content ** i // fac_denom ** i
        new_factors.append((fac_prim, i))
        factors = new_factors
        coeff = K0.convert(coeff, K1)
        return (coeff, factors)


def dup_ext_factor(f, K):
    """Factor univariate polynomials over algebraic number fields.

    The domain `K` must be an algebraic number field `k(a)` (see :ref:`QQ(a)`).

    Examples
    ========

    First define the algebraic number field `K = \\mathbb{Q}(\\sqrt{2})`:

    >>> from sympy import QQ, sqrt
    >>> from sympy.polys.factortools import dup_ext_factor
    >>> K = QQ.algebraic_field(sqrt(2))

    We can now factorise the polynomial `x^2 - 2` over `K`:

    >>> p = [K(1), K(0), K(-2)] # x^2 - 2
    >>> p1 = [K(1), -K.unit]    # x - sqrt(2)
    >>> p2 = [K(1), +K.unit]    # x + sqrt(2)
    >>> dup_ext_factor(p, K) == (K.one, [(p1, 1), (p2, 1)])
    True

    Usually this would be done at a higher level:

    >>> from sympy import factor
    >>> from sympy.abc import x
    >>> factor(x**2 - 2, extension=sqrt(2))
    (x - sqrt(2))*(x + sqrt(2))

    Explanation
    ===========

    Uses Trager's algorithm. In particular this function is algorithm
    ``alg_factor`` from [Trager76]_.

    If `f` is a polynomial in `k(a)[x]` then its norm `g(x)` is a polynomial in
    `k[x]`. If `g(x)` is square-free and has irreducible factors `g_1(x)`,
    `g_2(x)`, `\\cdots` then the irreducible factors of `f` in `k(a)[x]` are
    given by `f_i(x) = \\gcd(f(x), g_i(x))` where the GCD is computed in
    `k(a)[x]`.

    The first step in Trager's algorithm is to find an integer shift `s` so
    that `f(x-sa)` has square-free norm. Then the norm is factorized in `k[x]`
    and the GCD of (shifted) `f` with each factor gives the shifted factors of
    `f`. At the end the shift is undone to recover the unshifted factors of `f`
    in `k(a)[x]`.

    The algorithm reduces the problem of factorization in `k(a)[x]` to
    factorization in `k[x]` with the main additional steps being to compute the
    norm (a resultant calculation in `k[x,y]`) and some polynomial GCDs in
    `k(a)[x]`.

    In practice in SymPy the base field `k` will be the rationals :ref:`QQ` and
    this function factorizes a polynomial with coefficients in an algebraic
    number field  like `\\mathbb{Q}(\\sqrt{2})`.

    See Also
    ========

    dmp_ext_factor:
        Analogous function for multivariate polynomials over ``k(a)``.
    dup_sqf_norm:
        Subroutine ``sqfr_norm`` also from [Trager76]_.
    sympy.polys.polytools.factor:
        The high-level function that ultimately uses this function as needed.
    """
    lc = dup_LC(f, K)
    n = dup_degree(f)
    f = dup_monic(f, K)
    if n <= 0:
        return (lc, [])
    if None == 1:
        return (lc, [
            (f, 1)])
    F = f
    f = None(f, K)
    (s, g, r) = dup_sqf_norm(f, K)
    factors = dup_factor_list_include(r, K.dom)
    if len(factors) == 1:
        return (lc, [
            (f, n // dup_degree(f))])
    H = None * K.unit
    for factor, _ in enumerate(factors):
        h = dup_convert(factor, K.dom, K)
        (h, _, g) = dup_inner_gcd(h, g, K)
        h = dup_shift(h, H, K)
        factors[i] = h
        factors = dup_trial_division(F, factors, K)
        _dup_check_degrees(F, factors)
        return (lc, factors)


def dmp_ext_factor(f, u, K):
    """Factor multivariate polynomials over algebraic number fields.

    The domain `K` must be an algebraic number field `k(a)` (see :ref:`QQ(a)`).

    Examples
    ========

    First define the algebraic number field `K = \\mathbb{Q}(\\sqrt{2})`:

    >>> from sympy import QQ, sqrt
    >>> from sympy.polys.factortools import dmp_ext_factor
    >>> K = QQ.algebraic_field(sqrt(2))

    We can now factorise the polynomial `x^2 y^2 - 2` over `K`:

    >>> p = [[K(1),K(0),K(0)], [], [K(-2)]] # x**2*y**2 - 2
    >>> p1 = [[K(1),K(0)], [-K.unit]]       # x*y - sqrt(2)
    >>> p2 = [[K(1),K(0)], [+K.unit]]       # x*y + sqrt(2)
    >>> dmp_ext_factor(p, 1, K) == (K.one, [(p1, 1), (p2, 1)])
    True

    Usually this would be done at a higher level:

    >>> from sympy import factor
    >>> from sympy.abc import x, y
    >>> factor(x**2*y**2 - 2, extension=sqrt(2))
    (x*y - sqrt(2))*(x*y + sqrt(2))

    Explanation
    ===========

    This is Trager's algorithm for multivariate polynomials. In particular this
    function is algorithm ``alg_factor`` from [Trager76]_.

    See :func:`dup_ext_factor` for explanation.

    See Also
    ========

    dup_ext_factor:
        Analogous function for univariate polynomials over ``k(a)``.
    dmp_sqf_norm:
        Multivariate version of subroutine ``sqfr_norm`` also from [Trager76]_.
    sympy.polys.polytools.factor:
        The high-level function that ultimately uses this function as needed.
    """
    pass
# WARNING: Decompyle incomplete


def dup_gf_factor(f, K):
    '''Factor univariate polynomials over finite fields. '''
    f = dup_convert(f, K, K.dom)
    (coeff, factors) = gf_factor(f, K.mod, K.dom)
    for f, k in enumerate(factors):
        factors[i] = (dup_convert(f, K.dom, K), k)
        return (K.convert(coeff, K.dom), factors)


def dmp_gf_factor(f, u, K):
    '''Factor multivariate polynomials over finite fields. '''
    raise NotImplementedError('multivariate polynomials over finite fields')


def dup_factor_list(f, K0):
    '''Factor univariate polynomials into irreducibles in `K[x]`. '''
    (j, f) = dup_terms_gcd(f, K0)
    (cont, f) = dup_primitive(f, K0)
    if K0.is_FiniteField:
        (coeff, factors) = dup_gf_factor(f, K0)
    elif K0.is_Algebraic:
        (coeff, factors) = dup_ext_factor(f, K0)
    elif K0.is_GaussianRing:
        (coeff, factors) = dup_zz_i_factor(f, K0)
    elif K0.is_GaussianField:
        (coeff, factors) = dup_qq_i_factor(f, K0)
    elif not K0.is_Exact:
        K0 = K0.get_exact()
        K0_inexact = K0
        f = dup_convert(f, K0_inexact, K0)
    else:
        K0_inexact = None
    if K0.is_Field:
        K = K0.get_ring()
        (denom, f) = dup_clear_denoms(f, K0, K)
        f = dup_convert(f, K0, K)
    else:
        K = K0
    if K.is_ZZ:
        (coeff, factors) = dup_zz_factor(f, K)
    elif K.is_Poly:
        (f, u) = dmp_inject(f, 0, K)
        (coeff, factors) = dmp_factor_list(f, u, K.dom)
        for f, k in enumerate(factors):
            factors[i] = (dmp_eject(f, u, K), k)
            coeff = K.convert(coeff, K.dom)
    raise DomainError('factorization not supported over %s' % K0)
    if K0.is_Field:
        for f, k in enumerate(factors):
            factors[i] = (dup_convert(f, K, K0), k)
            coeff = K0.convert(coeff, K)
            coeff = K0.quo(coeff, denom)
            if K0_inexact:
                for f, k in enumerate(factors):
                    max_norm = dup_max_norm(f, K0)
                    f = dup_quo_ground(f, max_norm, K0)
                    f = dup_convert(f, K0, K0_inexact)
                    factors[i] = (f, k)
                    coeff = K0.mul(coeff, K0.pow(max_norm, k))
                    coeff = K0_inexact.convert(coeff, K0)
                    K0 = K0_inexact
                    if j:
                        factors.insert(0, ([
                            K0.one,
                            K0.zero], j))
    return (coeff * cont, _sort_factors(factors))


def dup_factor_list_include(f, K):
    '''Factor univariate polynomials into irreducibles in `K[x]`. '''
    (coeff, factors) = dup_factor_list(f, K)
    if not factors:
        return [
            (dup_strip([
                coeff]), 1)]
    g = None(factors[0][0], coeff, K)
    return [
        (g, factors[0][1])] + factors[1:]


def dmp_factor_list(f, u, K0):
    '''Factor multivariate polynomials into irreducibles in `K[X]`. '''
    if not u:
        return dup_factor_list(f, K0)
    (J, f) = None(f, u, K0)
    (cont, f) = dmp_ground_primitive(f, u, K0)
    if K0.is_FiniteField:
        (coeff, factors) = dmp_gf_factor(f, u, K0)
    elif K0.is_Algebraic:
        (coeff, factors) = dmp_ext_factor(f, u, K0)
    elif K0.is_GaussianRing:
        (coeff, factors) = dmp_zz_i_factor(f, u, K0)
    elif K0.is_GaussianField:
        (coeff, factors) = dmp_qq_i_factor(f, u, K0)
    elif not K0.is_Exact:
        K0 = K0.get_exact()
        K0_inexact = K0
        f = dmp_convert(f, u, K0_inexact, K0)
    else:
        K0_inexact = None
    if K0.is_Field:
        K = K0.get_ring()
        (denom, f) = dmp_clear_denoms(f, u, K0, K)
        f = dmp_convert(f, u, K0, K)
    else:
        K = K0
    if K.is_ZZ:
        (levels, f, v) = dmp_exclude(f, u, K)
        (coeff, factors) = dmp_zz_factor(f, v, K)
        for f, k in enumerate(factors):
            factors[i] = (dmp_include(f, levels, v, K), k)
    if K.is_Poly:
        (f, v) = dmp_inject(f, u, K)
        (coeff, factors) = dmp_factor_list(f, v, K.dom)
        for f, k in enumerate(factors):
            factors[i] = (dmp_eject(f, v, K), k)
            coeff = K.convert(coeff, K.dom)
    raise DomainError('factorization not supported over %s' % K0)
    if K0.is_Field:
        for f, k in enumerate(factors):
            factors[i] = (dmp_convert(f, u, K, K0), k)
            coeff = K0.convert(coeff, K)
            coeff = K0.quo(coeff, denom)
            if K0_inexact:
                for f, k in enumerate(factors):
                    max_norm = dmp_max_norm(f, u, K0)
                    f = dmp_quo_ground(f, max_norm, u, K0)
                    f = dmp_convert(f, u, K0, K0_inexact)
                    factors[i] = (f, k)
                    coeff = K0.mul(coeff, K0.pow(max_norm, k))
                    coeff = K0_inexact.convert(coeff, K0)
                    K0 = K0_inexact
                    for i, j in enumerate(reversed(J)):
                        if not j:
                            continue
                        term = {
                            (0,) * (u - i) + (1,) + (0,) * i: K0.one }
                        factors.insert(0, (dmp_from_dict(term, u, K0), j))
                        return (coeff * cont, _sort_factors(factors))


def dmp_factor_list_include(f, u, K):
    '''Factor multivariate polynomials into irreducibles in `K[X]`. '''
    if not u:
        return dup_factor_list_include(f, K)
    (coeff, factors) = None(f, u, K)
    if not factors:
        return [
            (dmp_ground(coeff, u), 1)]
    g = None(factors[0][0], coeff, u, K)
    return [
        (g, factors[0][1])] + factors[1:]


def dup_irreducible_p(f, K):
    '''
    Returns ``True`` if a univariate polynomial ``f`` has no factors
    over its domain.
    '''
    return dmp_irreducible_p(f, 0, K)


def dmp_irreducible_p(f, u, K):
    '''
    Returns ``True`` if a multivariate polynomial ``f`` has no factors
    over its domain.
    '''
    (_, factors) = dmp_factor_list(f, u, K)
    if not factors:
        return True
    if None(factors) > 1:
        return False
    (_, k) = None[0]
    return k == 1
