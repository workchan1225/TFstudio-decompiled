# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: risch.pyc (Python 3.11)

"""
The Risch Algorithm for transcendental function integration.

The core algorithms for the Risch algorithm are here.  The subproblem
algorithms are in the rde.py and prde.py files for the Risch
Differential Equation solver and the parametric problems solvers,
respectively.  All important information concerning the differential extension
for an integrand is stored in a DifferentialExtension object, which in the code
is usually called DE.  Throughout the code and Inside the DifferentialExtension
object, the conventions/attribute names are that the base domain is QQ and each
differential extension is x, t0, t1, ..., tn-1 = DE.t. DE.x is the variable of
integration (Dx == 1), DE.D is a list of the derivatives of
x, t1, t2, ..., tn-1 = t, DE.T is the list [x, t1, t2, ..., tn-1], DE.t is the
outer-most variable of the differential extension at the given level (the level
can be adjusted using DE.increment_level() and DE.decrement_level()),
k is the field C(x, t0, ..., tn-2), where C is the constant field.  The
numerator of a fraction is denoted by a and the denominator by
d.  If the fraction is named f, fa == numer(f) and fd == denom(f).
Fractions are returned as tuples (fa, fd).  DE.d and DE.t are used to
represent the topmost derivation and extension variable, respectively.
The docstring of a function signifies whether an argument is in k[t], in
which case it will just return a Poly in t, or in k(t), in which case it
will return the fraction (fa, fd). Other variable names probably come
from the names used in Bronstein's book.
"""
from types import GeneratorType
from functools import reduce
from sympy.core.function import Lambda
from sympy.core.mul import Mul
from sympy.core.intfunc import ilcm
from sympy.core.numbers import I
from sympy.core.power import Pow
from sympy.core.relational import Ne
from sympy.core.singleton import S
from sympy.core.sorting import ordered, default_sort_key
from sympy.core.symbol import Dummy, Symbol
from sympy.functions.elementary.exponential import log, exp
from sympy.functions.elementary.hyperbolic import cosh, coth, sinh, tanh
from sympy.functions.elementary.piecewise import Piecewise
from sympy.functions.elementary.trigonometric import atan, sin, cos, tan, acot, cot, asin, acos
from integrals import integrate, Integral
from heurisch import _symbols
from sympy.polys.polyerrors import PolynomialError
from sympy.polys.polytools import real_roots, cancel, Poly, gcd, reduced
from sympy.polys.rootoftools import RootSum
from sympy.utilities.iterables import numbered_symbols

def integer_powers(exprs):
    '''
    Rewrites a list of expressions as integer multiples of each other.

    Explanation
    ===========

    For example, if you have [x, x/2, x**2 + 1, 2*x/3], then you can rewrite
    this as [(x/6) * 6, (x/6) * 3, (x**2 + 1) * 1, (x/6) * 4]. This is useful
    in the Risch integration algorithm, where we must write exp(x) + exp(x/2)
    as (exp(x/2))**2 + exp(x/2), but not as exp(x) + sqrt(exp(x)) (this is
    because only the transcendental case is implemented and we therefore cannot
    integrate algebraic extensions). The integer multiples returned by this
    function for each term are the smallest possible (their content equals 1).

    Returns a list of tuples where the first element is the base term and the
    second element is a list of `(item, factor)` terms, where `factor` is the
    integer multiplicative factor that must multiply the base term to obtain
    the original item.

    The easiest way to understand this is to look at an example:

    >>> from sympy.abc import x
    >>> from sympy.integrals.risch import integer_powers
    >>> integer_powers([x, x/2, x**2 + 1, 2*x/3])
    [(x/6, [(x, 6), (x/2, 3), (2*x/3, 4)]), (x**2 + 1, [(x**2 + 1, 1)])]

    We can see how this relates to the example at the beginning of the
    docstring.  It chose x/6 as the first base term.  Then, x can be written as
    (x/2) * 2, so we get (0, 2), and so on. Now only element (x**2 + 1)
    remains, and there are no other terms that can be written as a rational
    multiple of that, so we get that it can be written as (x**2 + 1) * 1.

    '''
    pass
# WARNING: Decompyle incomplete


class DifferentialExtension:
    '''
    A container for all the information relating to a differential extension.

    Explanation
    ===========

    The attributes of this object are (see also the docstring of __init__):

    - f: The original (Expr) integrand.
    - x: The variable of integration.
    - T: List of variables in the extension.
    - D: List of derivations in the extension; corresponds to the elements of T.
    - fa: Poly of the numerator of the integrand.
    - fd: Poly of the denominator of the integrand.
    - Tfuncs: Lambda() representations of each element of T (except for x).
      For back-substitution after integration.
    - backsubs: A (possibly empty) list of further substitutions to be made on
      the final integral to make it look more like the integrand.
    - exts:
    - extargs:
    - cases: List of string representations of the cases of T.
    - t: The top level extension variable, as defined by the current level
      (see level below).
    - d: The top level extension derivation, as defined by the current
      derivation (see level below).
    - case: The string representation of the case of self.d.
    (Note that self.T and self.D will always contain the complete extension,
    regardless of the level.  Therefore, you should ALWAYS use DE.t and DE.d
    instead of DE.T[-1] and DE.D[-1].  If you want to have a list of the
    derivations or variables only up to the current level, use
    DE.D[:len(DE.D) + DE.level + 1] and DE.T[:len(DE.T) + DE.level + 1].  Note
    that, in particular, the derivation() function does this.)

    The following are also attributes, but will probably not be useful other
    than in internal use:
    - newf: Expr form of fa/fd.
    - level: The number (between -1 and -len(self.T)) such that
      self.T[self.level] == self.t and self.D[self.level] == self.d.
      Use the methods self.increment_level() and self.decrement_level() to change
      the current level.
    '''
    __slots__ = ('f', 'x', 'T', 'D', 'fa', 'fd', 'Tfuncs', 'backsubs', 'exts', 'extargs', 'cases', 'case', 't', 'd', 'newf', 'level', 'ts', 'dummy')
    
    def __init__(self, f, x, handle_first, dummy, extension, rewrite_complex = (None, None, 'log', False, None, None)):
        '''
        Tries to build a transcendental extension tower from ``f`` with respect to ``x``.

        Explanation
        ===========

        If it is successful, creates a DifferentialExtension object with, among
        others, the attributes fa, fd, D, T, Tfuncs, and backsubs such that
        fa and fd are Polys in T[-1] with rational coefficients in T[:-1],
        fa/fd == f, and D[i] is a Poly in T[i] with rational coefficients in
        T[:i] representing the derivative of T[i] for each i from 1 to len(T).
        Tfuncs is a list of Lambda objects for back replacing the functions
        after integrating.  Lambda() is only used (instead of lambda) to make
        them easier to test and debug. Note that Tfuncs corresponds to the
        elements of T, except for T[0] == x, but they should be back-substituted
        in reverse order.  backsubs is a (possibly empty) back-substitution list
        that should be applied on the completed integral to make it look more
        like the original integrand.

        If it is unsuccessful, it raises NotImplementedError.

        You can also create an object by manually setting the attributes as a
        dictionary to the extension keyword argument.  You must include at least
        D.  Warning, any attribute that is not given will be set to None. The
        attributes T, t, d, cases, case, x, and level are set automatically and
        do not need to be given.  The functions in the Risch Algorithm will NOT
        check to see if an attribute is None before using it.  This also does not
        check to see if the extension is valid (non-algebraic) or even if it is
        self-consistent.  Therefore, this should only be used for
        testing/debugging purposes.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __getattr__(self, attr):
        if attr not in self.__slots__:
            raise AttributeError(f'''{repr(self)!s} has no attribute {repr(attr)!s}''')

    
    def _rewrite_exps_pows(self, exps, pows, numpows, sympows, log_new_extension):
        '''
        Rewrite exps/pows for better processing.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _rewrite_logs(self, logs, symlogs):
        '''
        Rewrite logs for better processing.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _auto_attrs(self):
        '''
        Set attributes that are generated automatically.
        '''
        if not self.T:
            self.T = self.D()
        if not self.x:
            self.x = self.T[0]
        self.cases = zip(self.D, self.T)()
        self.level = -1
        self.t = self.T[self.level]
        self.d = self.D[self.level]
        self.case = self.cases[self.level]

    
    def _exp_part(self, exps):
        '''
        Try to build an exponential extension.

        Returns
        =======

        Returns True if there was a new extension, False if there was no new
        extension but it was able to rewrite the given exponentials in terms
        of the existing extension, and None if the entire extension building
        process should be restarted.  If the process fails because there is no
        way around an algebraic extension (e.g., exp(log(x)/2)), it will raise
        NotImplementedError.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _log_part(self, logs):
        '''
        Try to build a logarithmic extension.

        Returns
        =======

        Returns True if there was a new extension and False if there was no new
        extension but it was able to rewrite the given logarithms in terms
        of the existing extension.  Unlike with exponential extensions, there
        is no way that a logarithm is not transcendental over and cannot be
        rewritten in terms of an already existing extension in a non-algebraic
        way, so this function does not ever return None or raise
        NotImplementedError.
        '''
        is_deriv_k = is_deriv_k
        import prde
        new_extension = False
        logargs = logs()
    # WARNING: Decompyle incomplete

    _important_attrs = (lambda self: (self.fa, self.fd, self.D, self.T, self.Tfuncs, self.backsubs, self.exts, self.extargs))()
    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return self.__class__.__name__ + f'''({{fa={self.fa!s}, fd={self.fd!s}, D={self.D!s}}})'''

    
    def __eq__(self, other):
        for attr in self.__class__.__slots__:
            d2 = getattr(other, attr)
            d1 = getattr(self, attr)
            if not isinstance(d1, GeneratorType) and d1 == d2:
                return False
            return True

    
    def reset(self):
        '''
        Reset self to an initial state.  Used by __init__.
        '''
        self.t = self.x
        self.T = [
            self.x]
        self.D = [
            Poly(1, self.x)]
        self.level = -1
        self.exts = [
            None]
        self.extargs = [
            None]
        if self.dummy:
            self.ts = numbered_symbols('t', cls = Dummy)
        else:
            self.ts = numbered_symbols('t')
        self.backsubs = []
        self.Tfuncs = []
        self.newf = self.f

    
    def indices(self, extension):
        """
        Parameters
        ==========

        extension : str
            Represents a valid extension type.

        Returns
        =======

        list: A list of indices of 'exts' where extension of
            type 'extension' is present.

        Examples
        ========

        >>> from sympy.integrals.risch import DifferentialExtension
        >>> from sympy import log, exp
        >>> from sympy.abc import x
        >>> DE = DifferentialExtension(log(x) + exp(x), x, handle_first='exp')
        >>> DE.indices('log')
        [2]
        >>> DE.indices('exp')
        [1]

        """
        pass
    # WARNING: Decompyle incomplete

    
    def increment_level(self):
        '''
        Increment the level of self.

        Explanation
        ===========

        This makes the working differential extension larger.  self.level is
        given relative to the end of the list (-1, -2, etc.), so we do not need
        do worry about it when building the extension.
        '''
        if self.level >= -1:
            raise ValueError('The level of the differential extension cannot be incremented any further.')
        self.T[self.level] = self, self.level += 1, .level
        self.d = self.D[self.level]
        self.case = self.cases[self.level]

    
    def decrement_level(self):
        '''
        Decrease the level of self.

        Explanation
        ===========

        This makes the working differential extension smaller.  self.level is
        given relative to the end of the list (-1, -2, etc.), so we do not need
        do worry about it when building the extension.
        '''
        if self.level <= -len(self.T):
            raise ValueError('The level of the differential extension cannot be decremented any further.')
        self.T[self.level] = self, self.level -= 1, .level
        self.d = self.D[self.level]
        self.case = self.cases[self.level]



def update_sets(seq, atoms, func):
    s = set(seq)
    s = atoms.intersection(s)
    new = atoms - s
    s.update(list(filter(func, new)))
    return list(s)


class DecrementLevel:
    '''
    A context manager for decrementing the level of a DifferentialExtension.
    '''
    __slots__ = ('DE',)
    
    def __init__(self, DE):
        self.DE = DE

    
    def __enter__(self):
        self.DE.decrement_level()

    
    def __exit__(self, exc_type, exc_value, traceback):
        self.DE.increment_level()



class NonElementaryIntegralException(Exception):
    '''
    Exception used by subroutines within the Risch algorithm to indicate to one
    another that the function being integrated does not have an elementary
    integral in the given differential field.
    '''
    pass


def gcdex_diophantine(a, b, c):
    '''
    Extended Euclidean Algorithm, Diophantine version.

    Explanation
    ===========

    Given ``a``, ``b`` in K[x] and ``c`` in (a, b), the ideal generated by ``a`` and
    ``b``, return (s, t) such that s*a + t*b == c and either s == 0 or s.degree()
    < b.degree().
    '''
    (s, g) = a.half_gcdex(b)
    s *= c.exquo(g)
    if s and s.degree() >= b.degree():
        (_, s) = s.div(b)
    t = (c - s * a).exquo(b)
    return (s, t)


def frac_in(f = None, t = {
    'cancel': False }, *, cancel, **kwargs):
    '''
    Returns the tuple (fa, fd), where fa and fd are Polys in t.

    Explanation
    ===========

    This is a common idiom in the Risch Algorithm functions, so we abstract
    it out here. ``f`` should be a basic expression, a Poly, or a tuple (fa, fd),
    where fa and fd are either basic expressions or Polys, and f == fa/fd.
    **kwargs are applied to Poly.
    '''
    if isinstance(f, tuple):
        (fa, fd) = f
        f = fa.as_expr() / fd.as_expr()
    (fa, fd) = f.as_expr().as_numer_denom()
# WARNING: Decompyle incomplete


def as_poly_1t(p, t, z):
    '''
    (Hackish) way to convert an element ``p`` of K[t, 1/t] to K[t, z].

    In other words, ``z == 1/t`` will be a dummy variable that Poly can handle
    better.

    See issue 5131.

    Examples
    ========

    >>> from sympy import random_poly
    >>> from sympy.integrals.risch import as_poly_1t
    >>> from sympy.abc import x, z

    >>> p1 = random_poly(x, 10, -10, 10)
    >>> p2 = random_poly(x, 10, -10, 10)
    >>> p = p1 + p2.subs(x, 1/x)
    >>> as_poly_1t(p, x, z).as_expr().subs(z, 1/x) == p
    True
    '''
    (pa, pd) = frac_in(p, t, cancel = True)
    if not pd.is_monomial:
        raise PolynomialError(f'''{p!s} is not an element of K[{t!s}, 1/{t!s}].''')
    (t_part, remainder) = pa.div(pd)
    ans = t_part.as_poly(t, z, expand = False)
    if remainder:
        one = remainder.one
        tp = t * one
        r = pd.degree() - remainder.degree()
        z_part = remainder.transform(one, tp) * tp ** r
        z_part = z_part.replace(t, z).to_field().quo_ground(pd.LC())
        ans += z_part.as_poly(t, z, expand = False)
    return ans


def derivation(p, DE, coefficientD, basic = (False, False)):
    '''
    Computes Dp.

    Explanation
    ===========

    Given the derivation D with D = d/dx and p is a polynomial in t over
    K(x), return Dp.

    If coefficientD is True, it computes the derivation kD
    (kappaD), which is defined as kD(sum(ai*Xi**i, (i, 0, n))) ==
    sum(Dai*Xi**i, (i, 1, n)) (Definition 3.2.2, page 80).  X in this case is
    T[-1], so coefficientD computes the derivative just with respect to T[:-1],
    with T[-1] treated as a constant.

    If ``basic=True``, the returns a Basic expression.  Elements of D can still be
    instances of Poly.
    '''
    if basic:
        r = 0
    else:
        r = Poly(0, DE.t)
    t = DE.t
    if coefficientD:
        if DE.level <= -len(DE.T):
            return r
        None.decrement_level()
    D = DE.D[:len(DE.D) + DE.level + 1]
    T = DE.T[:len(DE.T) + DE.level + 1]
# WARNING: Decompyle incomplete


def get_case(d, t):
    """
    Returns the type of the derivation d.

    Returns one of {'exp', 'tan', 'base', 'primitive', 'other_linear',
    'other_nonlinear'}.
    """
    if not d.expr.has(t):
        if d.is_one:
            return 'base'
        return None
    if None.rem(Poly(t, t)).is_zero:
        return 'exp'
    if None.rem(Poly(1 + t ** 2, t)).is_zero:
        return 'tan'
    if None.degree(t) > 1:
        return 'other_nonlinear'


def splitfactor(p, DE, coefficientD, z = (False, None)):
    '''
    Splitting factorization.

    Explanation
    ===========

    Given a derivation D on k[t] and ``p`` in k[t], return (p_n, p_s) in
    k[t] x k[t] such that p = p_n*p_s, p_s is special, and each square
    factor of p_n is normal.

    Page. 100
    '''
    kinv = DE.T[:DE.level]()
    if z:
        kinv.append(z)
    One = Poly(1, DE.t, domain = p.get_domain())
    Dp = derivation(p, DE, coefficientD = coefficientD)
    if p.is_zero:
        return (p, One)
# WARNING: Decompyle incomplete


def splitfactor_sqf(p, DE, coefficientD, z, basic = (False, None, False)):
    '''
    Splitting Square-free Factorization.

    Explanation
    ===========

    Given a derivation D on k[t] and ``p`` in k[t], returns (N1, ..., Nm)
    and (S1, ..., Sm) in k[t]^m such that p =
    (N1*N2**2*...*Nm**m)*(S1*S2**2*...*Sm**m) is a splitting
    factorization of ``p`` and the Ni and Si are square-free and coprime.
    '''
    kkinv = DE.T[:DE.level]() + DE.T[:DE.level]
    if z:
        kkinv = [
            z]
    S = []
    N = []
    p_sqf = p.sqf_list_include()
    if p.is_zero:
        return (((p, 1),), ())
# WARNING: Decompyle incomplete


def canonical_representation(a, d, DE):
    '''
    Canonical Representation.

    Explanation
    ===========

    Given a derivation D on k[t] and f = a/d in k(t), return (f_p, f_s,
    f_n) in k[t] x k(t) x k(t) such that f = f_p + f_s + f_n is the
    canonical representation of f (f_p is a polynomial, f_s is reduced
    (has a special denominator), and f_n is simple (has a normal
    denominator).
    '''
    l = Poly(1 / d.LC(), DE.t)
    d = d.mul(l)
    a = a.mul(l)
    (q, r) = a.div(d)
    (dn, ds) = splitfactor(d, DE)
    (b, c) = gcdex_diophantine(dn.as_poly(DE.t), ds.as_poly(DE.t), r.as_poly(DE.t))
    c = c.as_poly(DE.t)
    b = b.as_poly(DE.t)
    return (q, (b, ds), (c, dn))


def hermite_reduce(a, d, DE):
    """
    Hermite Reduction - Mack's Linear Version.

    Given a derivation D on k(t) and f = a/d in k(t), returns g, h, r in
    k(t) such that f = Dg + h + r, h is simple, and r is reduced.

    """
    l = Poly(1 / d.LC(), DE.t)
    d = d.mul(l)
    a = a.mul(l)
    (fp, fs, fn) = canonical_representation(a, d, DE)
    (a, d) = fn
    l = Poly(1 / d.LC(), DE.t)
    d = d.mul(l)
    a = a.mul(l)
    ga = Poly(0, DE.t)
    gd = Poly(1, DE.t)
    dd = derivation(d, DE)
    dm = gcd(d.to_field(), dd.to_field()).as_poly(DE.t)
    (ds, _) = d.div(dm)
# WARNING: Decompyle incomplete


def polynomial_reduce(p, DE):
    '''
    Polynomial Reduction.

    Explanation
    ===========

    Given a derivation D on k(t) and p in k[t] where t is a nonlinear
    monomial over k, return q, r in k[t] such that p = Dq  + r, and
    deg(r) < deg_t(Dt).
    '''
    q = Poly(0, DE.t)
# WARNING: Decompyle incomplete


def laurent_series(a, d, F, n, DE):
    '''
    Contribution of ``F`` to the full partial fraction decomposition of A/D.

    Explanation
    ===========

    Given a field K of characteristic 0 and ``A``,``D``,``F`` in K[x] with D monic,
    nonzero, coprime with A, and ``F`` the factor of multiplicity n in the square-
    free factorization of D, return the principal parts of the Laurent series of
    A/D at all the zeros of ``F``.
    '''
    if F.degree() == 0:
        return 0
    Z = None('z', n)
    z = Symbol('z')
    Z.insert(0, z)
    delta_a = Poly(0, DE.t)
    delta_d = Poly(1, DE.t)
    E = d.quo(F ** n)
    hd = E * Poly(z ** n, DE.t)
    ha = a
    dF = derivation(F, DE)
    (B, _) = gcdex_diophantine(E, F, Poly(1, DE.t))
    (C, _) = gcdex_diophantine(dF, F, Poly(1, DE.t))
    F_store = F
    H_list = []
    DE_D_list = []
    V = []
    for j in range(0, n):
        F_store = derivation(F_store, DE)
        v = F_store.as_expr() / (j + 1)
        V.append(v)
        DE_D_list.append(Poly(Z[j + 1], Z[j]))
        DE_new = DifferentialExtension(extension = {
            'D': DE_D_list })
        for j in range(0, n):
            zEha = Poly(z ** (n + j), DE.t) * E ** (j + 1) * ha
            zEhd = hd
            Pd = cancel((zEha, zEhd))[2]
            Pa = cancel((zEha, zEhd))[1]
            Q = Pa.quo(Pd)
            for i in range(0, j + 1):
                Q = Q.subs(Z[i], V[i])
                Dha = hd * derivation(ha, DE, basic = True).as_poly(DE.t) + ha * derivation(hd, DE, basic = True).as_poly(DE.t) + hd * derivation(ha, DE_new, basic = True).as_poly(DE.t) + ha * derivation(hd, DE_new, basic = True).as_poly(DE.t)
                Dhd = Poly(j + 1, DE.t) * hd ** 2
                hd = Dhd
                ha = Dha
                (Ff, _) = F.div(gcd(F, Q))
                (F_stara, F_stard) = frac_in(Ff, DE.t)
                if F_stara.degree(DE.t) - F_stard.degree(DE.t) > 0:
                    QBC = Poly(Q, DE.t) * B ** (1 + j) * C ** (n + j)
                    H = QBC
                    H_list.append(H)
                    H = (QBC * F_stard).rem(F_stara)
                    alphas = real_roots(F_stara)
                    for alpha in list(alphas):
                        delta_a = delta_a * Poly((DE.t - alpha) ** (n - j), DE.t) + Poly(H.eval(alpha), DE.t)
                        delta_d = delta_d * Poly((DE.t - alpha) ** (n - j), DE.t)
                        return (delta_a, delta_d, H_list)


def recognize_derivative(a, d, DE, z = (None,)):
    '''
    Compute the squarefree factorization of the denominator of f
    and for each Di the polynomial H in K[x] (see Theorem 2.7.1), using the
    LaurentSeries algorithm. Write Di = GiEi where Gj = gcd(Hn, Di) and
    gcd(Ei,Hn) = 1. Since the residues of f at the roots of Gj are all 0, and
    the residue of f at a root alpha of Ei is Hi(a) != 0, f is the derivative of a
    rational function if and only if Ei = 1 for each i, which is equivalent to
    Di | H[-1] for each i.
    '''
    flag = True
    (a, d) = a.cancel(d, include = True)
    (_, r) = a.div(d)
    (Np, Sp) = splitfactor_sqf(d, DE, coefficientD = True, z = z)
    j = 1
    for s, _ in Sp:
        (delta_a, delta_d, H) = laurent_series(r, d, s, j, DE)
        g = gcd(d, H[-1]).as_poly()
        if g is not d:
            flag = False
        else:
            j = j + 1
        return flag


def recognize_log_derivative(a, d, DE, z = (None,)):
    '''
    There exists a v in K(x)* such that f = dv/v
    where f a rational function if and only if f can be written as f = A/D
    where D is squarefree,deg(A) < deg(D), gcd(A, D) = 1,
    and all the roots of the Rothstein-Trager resultant are integers. In that case,
    any of the Rothstein-Trager, Lazard-Rioboo-Trager or Czichowski algorithm
    produces u in K(x) such that du/dx = uf.
    '''
    if not z:
        pass
    z = Dummy('z')
    (a, d) = a.cancel(d, include = True)
    (_, a) = a.div(d)
    pz = Poly(z, DE.t)
    Dd = derivation(d, DE)
    q = a - pz * Dd
    (r, _) = d.resultant(q, includePRS = True)
    r = Poly(r, z)
    (Np, Sp) = splitfactor_sqf(r, DE, coefficientD = True, z = z)
    for s, _ in Sp:
        a = real_roots(s.as_poly(z))
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(a()):
            all
            return False
        return True


def residue_reduce(a, d, DE, z, invert = (None, True)):
    '''
    Lazard-Rioboo-Rothstein-Trager resultant reduction.

    Explanation
    ===========

    Given a derivation ``D`` on k(t) and f in k(t) simple, return g
    elementary over k(t) and a Boolean b in {True, False} such that f -
    Dg in k[t] if b == True or f + h and f + h - Dg do not have an
    elementary integral over k(t) for any h in k<t> (reduced) if b ==
    False.

    Returns (G, b), where G is a tuple of tuples of the form (s_i, S_i),
    such that g = Add(*[RootSum(s_i, lambda z: z*log(S_i(z, t))) for
    S_i, s_i in G]). f - Dg is the remaining integral, which is elementary
    only if b == True, and hence the integral of f is elementary only if
    b == True.

    f - Dg is not calculated in this function because that would require
    explicitly calculating the RootSum.  Use residue_reduce_derivation().
    '''
    pass
# WARNING: Decompyle incomplete


def residue_reduce_to_basic(H, DE, z):
    '''
    Converts the tuple returned by residue_reduce() into a Basic expression.
    '''
    pass
# WARNING: Decompyle incomplete


def residue_reduce_derivation(H, DE, z):
    '''
    Computes the derivation of an expression returned by residue_reduce().

    In general, this is a rational function in t, so this returns an
    as_expr() result.
    '''
    pass
# WARNING: Decompyle incomplete


def integrate_primitive_polynomial(p, DE):
    '''
    Integration of primitive polynomials.

    Explanation
    ===========

    Given a primitive monomial t over k, and ``p`` in k[t], return q in k[t],
    r in k, and a bool b in {True, False} such that r = p - Dq is in k if b is
    True, or r = p - Dq does not have an elementary integral over k(t) if b is
    False.
    '''
    Zero = Poly(0, DE.t)
    q = Poly(0, DE.t)
    if not p.expr.has(DE.t):
        return (Zero, p, True)
    limited_integrate = limited_integrate
    import prde
    if not p.expr.has(DE.t):
        return (q, p, True)
    (Dta, Dtb) = None(DE.d, DE.T[DE.level - 1])
    DecrementLevel(DE)
    a = p.LC()
    (aa, ad) = frac_in(a, DE.t)
    rv = limited_integrate(aa, ad, [
        (Dta, Dtb)], DE)
# WARNING: Decompyle incomplete


def integrate_primitive(a, d, DE, z = (None,)):
    '''
    Integration of primitive functions.

    Explanation
    ===========

    Given a primitive monomial t over k and f in k(t), return g elementary over
    k(t), i in k(t), and b in {True, False} such that i = f - Dg is in k if b
    is True or i = f - Dg does not have an elementary integral over k(t) if b
    is False.

    This function returns a Basic expression for the first argument.  If b is
    True, the second argument is Basic expression in k to recursively integrate.
    If b is False, the second argument is an unevaluated Integral, which has
    been proven to be nonelementary.
    '''
    pass
# WARNING: Decompyle incomplete


def integrate_hyperexponential_polynomial(p, DE, z):
    '''
    Integration of hyperexponential polynomials.

    Explanation
    ===========

    Given a hyperexponential monomial t over k and ``p`` in k[t, 1/t], return q in
    k[t, 1/t] and a bool b in {True, False} such that p - Dq in k if b is True,
    or p - Dq does not have an elementary integral over k(t) if b is False.
    '''
    t1 = DE.t
    dtt = DE.d.exquo(Poly(DE.t, DE.t))
    qa = Poly(0, DE.t)
    qd = Poly(1, DE.t)
    b = True
    if p.is_zero:
        return (qa, qd, b)
    rischDE = rischDE
    import sympy.integrals.rde
    DecrementLevel(DE)
    for i in range(-p.degree(z), p.degree(t1) + 1):
        if not i:
            continue
        if i < 0:
            a = p.as_poly(z, expand = False).nth(-i)
        else:
            a = p.as_poly(t1, expand = False).nth(i)
        (aa, ad) = frac_in(a, DE.t, field = True)
        (aa, ad) = aa.cancel(ad, include = True)
        iDt = Poly(i, t1) * dtt
        (iDta, iDtd) = frac_in(iDt, DE.t, field = True)
        (va, vd) = rischDE(iDta, iDtd, Poly(aa, DE.t), Poly(ad, DE.t), DE)
        (va, vd) = frac_in((va, vd), t1, cancel = True)
        qa = qa * vd + va * Poly(t1 ** i) * qd
        qd *= vd
        except NonElementaryIntegralException:
            b = False
            continue
        None(None, None)
    with None:
        if not None:
            pass
    return (qa, qd, b)


def integrate_hyperexponential(a, d, DE, z, conds = (None, 'piecewise')):
    '''
    Integration of hyperexponential functions.

    Explanation
    ===========

    Given a hyperexponential monomial t over k and f in k(t), return g
    elementary over k(t), i in k(t), and a bool b in {True, False} such that
    i = f - Dg is in k if b is True or i = f - Dg does not have an elementary
    integral over k(t) if b is False.

    This function returns a Basic expression for the first argument.  If b is
    True, the second argument is Basic expression in k to recursively integrate.
    If b is False, the second argument is an unevaluated Integral, which has
    been proven to be nonelementary.
    '''
    pass
# WARNING: Decompyle incomplete


def integrate_hypertangent_polynomial(p, DE):
    '''
    Integration of hypertangent polynomials.

    Explanation
    ===========

    Given a differential field k such that sqrt(-1) is not in k, a
    hypertangent monomial t over k, and p in k[t], return q in k[t] and
    c in k such that p - Dq - c*D(t**2 + 1)/(t**1 + 1) is in k and p -
    Dq does not have an elementary integral over k(t) if Dc != 0.
    '''
    (q, r) = polynomial_reduce(p, DE)
    a = DE.d.exquo(Poly(DE.t ** 2 + 1, DE.t))
    c = Poly(r.nth(1) / (2 * a.as_expr()), DE.t)
    return (q, c)


def integrate_nonlinear_no_specials(a, d, DE, z = (None,)):
    '''
    Integration of nonlinear monomials with no specials.

    Explanation
    ===========

    Given a nonlinear monomial t over k such that Sirr ({p in k[t] | p is
    special, monic, and irreducible}) is empty, and f in k(t), returns g
    elementary over k(t) and a Boolean b in {True, False} such that f - Dg is
    in k if b == True, or f - Dg does not have an elementary integral over k(t)
    if b == False.

    This function is applicable to all nonlinear extensions, but in the case
    where it returns b == False, it will only have proven that the integral of
    f - Dg is nonelementary if Sirr is empty.

    This function returns a Basic expression.
    '''
    pass
# WARNING: Decompyle incomplete


class NonElementaryIntegral(Integral):
    """
    Represents a nonelementary Integral.

    Explanation
    ===========

    If the result of integrate() is an instance of this class, it is
    guaranteed to be nonelementary.  Note that integrate() by default will try
    to find any closed-form solution, even in terms of special functions which
    may themselves not be elementary.  To make integrate() only give
    elementary solutions, or, in the cases where it can prove the integral to
    be nonelementary, instances of this class, use integrate(risch=True).
    In this case, integrate() may raise NotImplementedError if it cannot make
    such a determination.

    integrate() uses the deterministic Risch algorithm to integrate elementary
    functions or prove that they have no elementary integral.  In some cases,
    this algorithm can split an integral into an elementary and nonelementary
    part, so that the result of integrate will be the sum of an elementary
    expression and a NonElementaryIntegral.

    Examples
    ========

    >>> from sympy import integrate, exp, log, Integral
    >>> from sympy.abc import x

    >>> a = integrate(exp(-x**2), x, risch=True)
    >>> print(a)
    Integral(exp(-x**2), x)
    >>> type(a)
    <class 'sympy.integrals.risch.NonElementaryIntegral'>

    >>> expr = (2*log(x)**2 - log(x) - x**2)/(log(x)**3 - x**2*log(x))
    >>> b = integrate(expr, x, risch=True)
    >>> print(b)
    -log(-x + log(x))/2 + log(x + log(x))/2 + Integral(1/log(x), x)
    >>> type(b.atoms(Integral).pop())
    <class 'sympy.integrals.risch.NonElementaryIntegral'>

    """
    pass


def risch_integrate(f, x, extension, handle_first, separate_integral, rewrite_complex, conds = (None, 'log', False, None, 'piecewise')):
    """
    The Risch Integration Algorithm.

    Explanation
    ===========

    Only transcendental functions are supported.  Currently, only exponentials
    and logarithms are supported, but support for trigonometric functions is
    forthcoming.

    If this function returns an unevaluated Integral in the result, it means
    that it has proven that integral to be nonelementary.  Any errors will
    result in raising NotImplementedError.  The unevaluated Integral will be
    an instance of NonElementaryIntegral, a subclass of Integral.

    handle_first may be either 'exp' or 'log'.  This changes the order in
    which the extension is built, and may result in a different (but
    equivalent) solution (for an example of this, see issue 5109).  It is also
    possible that the integral may be computed with one but not the other,
    because not all cases have been implemented yet.  It defaults to 'log' so
    that the outer extension is exponential when possible, because more of the
    exponential case has been implemented.

    If ``separate_integral`` is ``True``, the result is returned as a tuple (ans, i),
    where the integral is ans + i, ans is elementary, and i is either a
    NonElementaryIntegral or 0.  This useful if you want to try further
    integrating the NonElementaryIntegral part using other algorithms to
    possibly get a solution in terms of special functions.  It is False by
    default.

    Examples
    ========

    >>> from sympy.integrals.risch import risch_integrate
    >>> from sympy import exp, log, pprint
    >>> from sympy.abc import x

    First, we try integrating exp(-x**2). Except for a constant factor of
    2/sqrt(pi), this is the famous error function.

    >>> pprint(risch_integrate(exp(-x**2), x))
      /
     |
     |    2
     |  -x
     | e    dx
     |
    /

    The unevaluated Integral in the result means that risch_integrate() has
    proven that exp(-x**2) does not have an elementary anti-derivative.

    In many cases, risch_integrate() can split out the elementary
    anti-derivative part from the nonelementary anti-derivative part.
    For example,

    >>> pprint(risch_integrate((2*log(x)**2 - log(x) - x**2)/(log(x)**3 -
    ... x**2*log(x)), x))
                                             /
                                            |
      log(-x + log(x))   log(x + log(x))    |   1
    - ---------------- + --------------- +  | ------ dx
             2                  2           | log(x)
                                            |
                                           /

    This means that it has proven that the integral of 1/log(x) is
    nonelementary.  This function is also known as the logarithmic integral,
    and is often denoted as Li(x).

    risch_integrate() currently only accepts purely transcendental functions
    with exponentials and logarithms, though note that this can include
    nested exponentials and logarithms, as well as exponentials with bases
    other than E.

    >>> pprint(risch_integrate(exp(x)*exp(exp(x)), x))
     / x\\
     \\e /
    e
    >>> pprint(risch_integrate(exp(exp(x)), x))
      /
     |
     |  / x\\
     |  \\e /
     | e     dx
     |
    /

    >>> pprint(risch_integrate(x*x**x*log(x) + x**x + x*x**x, x))
       x
    x*x
    >>> pprint(risch_integrate(x**x, x))
      /
     |
     |  x
     | x  dx
     |
    /

    >>> pprint(risch_integrate(-1/(x*log(x)*log(log(x))**2), x))
         1
    -----------
    log(log(x))

    """
    f = S(f)
    if not extension:
        pass
    DE = DifferentialExtension(f, x, handle_first = handle_first, dummy = True, rewrite_complex = rewrite_complex)
    fd = DE.fd
    fa = DE.fa
    result = S.Zero
    for case in reversed(DE.cases):
        if not fa.expr.has(DE.t) and fd.expr.has(DE.t) and case == 'base':
            DE.decrement_level()
            (fa, fd) = frac_in((fa, fd), DE.t)
            continue
        (fa, fd) = fa.cancel(fd, include = True)
        if case == 'exp':
            (ans, i, b) = integrate_hyperexponential(fa, fd, DE, conds = conds)
        elif case == 'primitive':
            (ans, i, b) = integrate_primitive(fa, fd, DE)
        elif case == 'base':
            ans = integrate(fa.as_expr() / fd.as_expr(), DE.x, risch = False)
            b = False
            i = S.Zero
        else:
            raise NotImplementedError('Only exponential and logarithmic extensions are currently supported.')
        result += ans
        if b:
            DE.decrement_level()
            (fa, fd) = frac_in(i, DE.t)
            continue
        result = result.subs(DE.backsubs)
        if not i.is_zero:
            i = NonElementaryIntegral(i.function.subs(DE.backsubs), i.limits)
        if not separate_integral:
            result += i
            
            return None, result
        if None(i, NonElementaryIntegral):
            
            return None, (result, i)
        
        return None, (None, 0)
        return None
