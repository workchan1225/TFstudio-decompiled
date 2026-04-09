# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: monomials.pyc (Python 3.11)

'''Tools and arithmetics for monomials of distributed polynomials. '''
from itertools import combinations_with_replacement, product
from textwrap import dedent
from sympy.core import Mul, S, Tuple, sympify
from sympy.polys.polyerrors import ExactQuotientFailed
from sympy.polys.polyutils import PicklableWithSlots, dict_from_expr
from sympy.utilities import public
from sympy.utilities.iterables import is_sequence, iterable
itermonomials = (lambda variables, max_degrees, min_degrees = (None,): pass# WARNING: Decompyle incomplete
)()

def monomial_count(V, N):
    """
    Computes the number of monomials.

    The number of monomials is given by the following formula:

    .. math::

        \\frac{(\\#V + N)!}{\\#V! N!}

    where `N` is a total degree and `V` is a set of variables.

    Examples
    ========

    >>> from sympy.polys.monomials import itermonomials, monomial_count
    >>> from sympy.polys.orderings import monomial_key
    >>> from sympy.abc import x, y

    >>> monomial_count(2, 2)
    6

    >>> M = list(itermonomials([x, y], 2))

    >>> sorted(M, key=monomial_key('grlex', [y, x]))
    [1, x, y, x**2, x*y, y**2]
    >>> len(M)
    6

    """
    factorial = factorial
    import sympy.functions.combinatorial.factorials
    return factorial(V + N) / factorial(V) / factorial(N)


def monomial_mul(A, B):
    '''
    Multiplication of tuples representing monomials.

    Examples
    ========

    Lets multiply `x**3*y**4*z` with `x*y**2`::

        >>> from sympy.polys.monomials import monomial_mul

        >>> monomial_mul((3, 4, 1), (1, 2, 0))
        (4, 6, 1)

    which gives `x**4*y**5*z`.

    '''
    return (lambda .0: [ a + b for a, b in .0 ])(zip(A, B)())


def monomial_div(A, B):
    '''
    Division of tuples representing monomials.

    Examples
    ========

    Lets divide `x**3*y**4*z` by `x*y**2`::

        >>> from sympy.polys.monomials import monomial_div

        >>> monomial_div((3, 4, 1), (1, 2, 0))
        (2, 2, 1)

    which gives `x**2*y**2*z`. However::

        >>> monomial_div((3, 4, 1), (1, 2, 2)) is None
        True

    `x*y**2*z**2` does not divide `x**3*y**4*z`.

    '''
    C = monomial_ldiv(A, B)
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(C()):
        return tuple(C)
    return all


def monomial_ldiv(A, B):
    '''
    Division of tuples representing monomials.

    Examples
    ========

    Lets divide `x**3*y**4*z` by `x*y**2`::

        >>> from sympy.polys.monomials import monomial_ldiv

        >>> monomial_ldiv((3, 4, 1), (1, 2, 0))
        (2, 2, 1)

    which gives `x**2*y**2*z`.

        >>> monomial_ldiv((3, 4, 1), (1, 2, 2))
        (2, 2, -1)

    which gives `x**2*y**2*z**-1`.

    '''
    return (lambda .0: [ a - b for a, b in .0 ])(zip(A, B)())


def monomial_pow(A, n):
    '''Return the n-th pow of the monomial. '''
    pass
# WARNING: Decompyle incomplete


def monomial_gcd(A, B):
    '''
    Greatest common divisor of tuples representing monomials.

    Examples
    ========

    Lets compute GCD of `x*y**4*z` and `x**3*y**2`::

        >>> from sympy.polys.monomials import monomial_gcd

        >>> monomial_gcd((1, 4, 1), (3, 2, 0))
        (1, 2, 0)

    which gives `x*y**2`.

    '''
    return (lambda .0: [ min(a, b) for a, b in .0 ])(zip(A, B)())


def monomial_lcm(A, B):
    '''
    Least common multiple of tuples representing monomials.

    Examples
    ========

    Lets compute LCM of `x*y**4*z` and `x**3*y**2`::

        >>> from sympy.polys.monomials import monomial_lcm

        >>> monomial_lcm((1, 4, 1), (3, 2, 0))
        (3, 4, 1)

    which gives `x**3*y**4*z`.

    '''
    return (lambda .0: [ max(a, b) for a, b in .0 ])(zip(A, B)())


def monomial_divides(A, B):
    '''
    Does there exist a monomial X such that XA == B?

    Examples
    ========

    >>> from sympy.polys.monomials import monomial_divides
    >>> monomial_divides((1, 2), (3, 4))
    True
    >>> monomial_divides((1, 2), (0, 2))
    False
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(A, B)())


def monomial_max(*monoms):
    '''
    Returns maximal degree for each variable in a set of monomials.

    Examples
    ========

    Consider monomials `x**3*y**4*z**5`, `y**5*z` and `x**6*y**3*z**9`.
    We wish to find out what is the maximal degree for each of `x`, `y`
    and `z` variables::

        >>> from sympy.polys.monomials import monomial_max

        >>> monomial_max((3,4,5), (0,5,1), (6,3,9))
        (6, 5, 9)

    '''
    M = list(monoms[0])
    for N in monoms[1:]:
        for i, n in enumerate(N):
            M[i] = max(M[i], n)
        return tuple(M)


def monomial_min(*monoms):
    '''
    Returns minimal degree for each variable in a set of monomials.

    Examples
    ========

    Consider monomials `x**3*y**4*z**5`, `y**5*z` and `x**6*y**3*z**9`.
    We wish to find out what is the minimal degree for each of `x`, `y`
    and `z` variables::

        >>> from sympy.polys.monomials import monomial_min

        >>> monomial_min((3,4,5), (0,5,1), (6,3,9))
        (0, 3, 1)

    '''
    M = list(monoms[0])
    for N in monoms[1:]:
        for i, n in enumerate(N):
            M[i] = min(M[i], n)
        return tuple(M)


def monomial_deg(M):
    '''
    Returns the total degree of a monomial.

    Examples
    ========

    The total degree of `xy^2` is 3:

    >>> from sympy.polys.monomials import monomial_deg
    >>> monomial_deg((1, 2))
    3
    '''
    return sum(M)


def term_div(a, b, domain):
    '''Division of two terms in over a ring/field. '''
    (a_lm, a_lc) = a
    (b_lm, b_lc) = b
    monom = monomial_div(a_lm, b_lm)
# WARNING: Decompyle incomplete


class MonomialOps:
    '''Code generator of fast monomial arithmetic functions. '''
    
    def __init__(self, ngens):
        self.ngens = ngens

    
    def _build(self, code, name):
        ns = { }
        exec(code, ns)
        return ns[name]

    
    def _vars(self, name):
        pass
    # WARNING: Decompyle incomplete

    
    def mul(self):
        name = 'monomial_mul'
        template = dedent('        def %(name)s(A, B):\n            (%(A)s,) = A\n            (%(B)s,) = B\n            return (%(AB)s,)\n        ')
        A = self._vars('a')
        B = self._vars('b')
        AB = zip(A, B)()
        code = template % {
            'name': name,
            'A': ', '.join(A),
            'B': ', '.join(B),
            'AB': ', '.join(AB) }
        return self._build(code, name)

    
    def pow(self):
        name = 'monomial_pow'
        template = dedent('        def %(name)s(A, k):\n            (%(A)s,) = A\n            return (%(Ak)s,)\n        ')
        A = self._vars('a')
        Ak = A()
        code = template % {
            'name': name,
            'A': ', '.join(A),
            'Ak': ', '.join(Ak) }
        return self._build(code, name)

    
    def mulpow(self):
        name = 'monomial_mulpow'
        template = dedent('        def %(name)s(A, B, k):\n            (%(A)s,) = A\n            (%(B)s,) = B\n            return (%(ABk)s,)\n        ')
        A = self._vars('a')
        B = self._vars('b')
        ABk = zip(A, B)()
        code = template % {
            'name': name,
            'A': ', '.join(A),
            'B': ', '.join(B),
            'ABk': ', '.join(ABk) }
        return self._build(code, name)

    
    def ldiv(self):
        name = 'monomial_ldiv'
        template = dedent('        def %(name)s(A, B):\n            (%(A)s,) = A\n            (%(B)s,) = B\n            return (%(AB)s,)\n        ')
        A = self._vars('a')
        B = self._vars('b')
        AB = zip(A, B)()
        code = template % {
            'name': name,
            'A': ', '.join(A),
            'B': ', '.join(B),
            'AB': ', '.join(AB) }
        return self._build(code, name)

    
    def div(self):
        name = 'monomial_div'
        template = dedent('        def %(name)s(A, B):\n            (%(A)s,) = A\n            (%(B)s,) = B\n            %(RAB)s\n            return (%(R)s,)\n        ')
        A = self._vars('a')
        B = self._vars('b')
        RAB = range(self.ngens)()
        R = self._vars('r')
        code = template % {
            'name': name,
            'A': ', '.join(A),
            'B': ', '.join(B),
            'RAB': '\n    '.join(RAB),
            'R': ', '.join(R) }
        return self._build(code, name)

    
    def lcm(self):
        name = 'monomial_lcm'
        template = dedent('        def %(name)s(A, B):\n            (%(A)s,) = A\n            (%(B)s,) = B\n            return (%(AB)s,)\n        ')
        A = self._vars('a')
        B = self._vars('b')
        AB = zip(A, B)()
        code = template % {
            'name': name,
            'A': ', '.join(A),
            'B': ', '.join(B),
            'AB': ', '.join(AB) }
        return self._build(code, name)

    
    def gcd(self):
        name = 'monomial_gcd'
        template = dedent('        def %(name)s(A, B):\n            (%(A)s,) = A\n            (%(B)s,) = B\n            return (%(AB)s,)\n        ')
        A = self._vars('a')
        B = self._vars('b')
        AB = zip(A, B)()
        code = template % {
            'name': name,
            'A': ', '.join(A),
            'B': ', '.join(B),
            'AB': ', '.join(AB) }
        return self._build(code, name)


Monomial = <NODE:12>()
