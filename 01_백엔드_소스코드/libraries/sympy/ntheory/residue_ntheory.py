# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: residue_ntheory.pyc (Python 3.11)

from __future__ import annotations
from sympy.external.gmpy import gcd, lcm, invert, sqrt, jacobi, bit_scan1, remove
from sympy.polys import Poly
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import gf_crt1, gf_crt2, linear_congruence, gf_csolve
from primetest import isprime
from generate import primerange
from factor_ import factorint, _perfect_power
from modular import crt
from sympy.utilities.decorator import deprecated
from sympy.utilities.memoization import recurrence_memo
from sympy.utilities.misc import as_int
from sympy.utilities.iterables import iproduct
from sympy.core.random import _randint, randint
from itertools import product

def n_order(a, n):
    ''' Returns the order of ``a`` modulo ``n``.

    Explanation
    ===========

    The order of ``a`` modulo ``n`` is the smallest integer
    ``k`` such that `a^k` leaves a remainder of 1 with ``n``.

    Parameters
    ==========

    a : integer
    n : integer, n > 1. a and n should be relatively prime

    Returns
    =======

    int : the order of ``a`` modulo ``n``

    Raises
    ======

    ValueError
        If `n \\le 1` or `\\gcd(a, n) \\neq 1`.
        If ``a`` or ``n`` is not an integer.

    Examples
    ========

    >>> from sympy.ntheory import n_order
    >>> n_order(3, 7)
    6
    >>> n_order(4, 7)
    3

    See Also
    ========

    is_primitive_root
        We say that ``a`` is a primitive root of ``n``
        when the order of ``a`` modulo ``n`` equals ``totient(n)``

    '''
    n = as_int(n)
    a = as_int(a)
    if n <= 1:
        raise ValueError('n should be an integer greater than 1')
    a = a % n
    if a == 1:
        return 1
    if None(a, n) != 1:
        raise ValueError('The two numbers should be relatively prime')
    a_order = 1
# WARNING: Decompyle incomplete


def _primitive_root_prime_iter(p):
    ''' Generates the primitive roots for a prime ``p``.

    Explanation
    ===========

    The primitive roots generated are not necessarily sorted.
    However, the first one is the smallest primitive root.

    Find the element whose order is ``p-1`` from the smaller one.
    If we can find the first primitive root ``g``, we can use the following theorem.

    .. math ::
        \\operatorname{ord}(g^k) = \\frac{\\operatorname{ord}(g)}{\\gcd(\\operatorname{ord}(g), k)}

    From the assumption that `\\operatorname{ord}(g)=p-1`,
    it is a necessary and sufficient condition for
    `\\operatorname{ord}(g^k)=p-1` that `\\gcd(p-1, k)=1`.

    Parameters
    ==========

    p : odd prime

    Yields
    ======

    int
        the primitive roots of ``p``

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _primitive_root_prime_iter
    >>> sorted(_primitive_root_prime_iter(19))
    [2, 3, 10, 13, 14, 15]

    References
    ==========

    .. [1] W. Stein "Elementary Number Theory" (2011), page 44

    '''
    pass
# WARNING: Decompyle incomplete


def _primitive_root_prime_power_iter(p, e):
    ''' Generates the primitive roots of `p^e`.

    Explanation
    ===========

    Let ``g`` be the primitive root of ``p``.
    If `g^{p-1} \\not\\equiv 1 \\pmod{p^2}`, then ``g`` is primitive root of `p^e`.
    Thus, if we find a primitive root ``g`` of ``p``,
    then `g, g+p, g+2p, \\ldots, g+(p-1)p` are primitive roots of `p^2` except one.
    That one satisfies `\\hat{g}^{p-1} \\equiv 1 \\pmod{p^2}`.
    If ``h`` is the primitive root of `p^2`,
    then `h, h+p^2, h+2p^2, \\ldots, h+(p^{e-2}-1)p^e` are primitive roots of `p^e`.

    Parameters
    ==========

    p : odd prime
    e : positive integer

    Yields
    ======

    int
        the primitive roots of `p^e`

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _primitive_root_prime_power_iter
    >>> sorted(_primitive_root_prime_power_iter(5, 2))
    [2, 3, 8, 12, 13, 17, 22, 23]

    '''
    pass
# WARNING: Decompyle incomplete


def _primitive_root_prime_power2_iter(p, e):
    ''' Generates the primitive roots of `2p^e`.

    Explanation
    ===========

    If ``g`` is the primitive root of ``p**e``,
    then the odd one of ``g`` and ``g+p**e`` is the primitive root of ``2*p**e``.

    Parameters
    ==========

    p : odd prime
    e : positive integer

    Yields
    ======

    int
        the primitive roots of `2p^e`

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _primitive_root_prime_power2_iter
    >>> sorted(_primitive_root_prime_power2_iter(5, 2))
    [3, 13, 17, 23, 27, 33, 37, 47]

    '''
    pass
# WARNING: Decompyle incomplete


def primitive_root(p, smallest = (True,)):
    ''' Returns a primitive root of ``p`` or None.

    Explanation
    ===========

    For the definition of primitive root,
    see the explanation of ``is_primitive_root``.

    The primitive root of ``p`` exist only for
    `p = 2, 4, q^e, 2q^e` (``q`` is an odd prime).
    Now, if we know the primitive root of ``q``,
    we can calculate the primitive root of `q^e`,
    and if we know the primitive root of `q^e`,
    we can calculate the primitive root of `2q^e`.
    When there is no need to find the smallest primitive root,
    this property can be used to obtain a fast primitive root.
    On the other hand, when we want the smallest primitive root,
    we naively determine whether it is a primitive root or not.

    Parameters
    ==========

    p : integer, p > 1
    smallest : if True the smallest primitive root is returned or None

    Returns
    =======

    int | None :
        If the primitive root exists, return the primitive root of ``p``.
        If not, return None.

    Raises
    ======

    ValueError
        If `p \\le 1` or ``p`` is not an integer.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import primitive_root
    >>> primitive_root(19)
    2
    >>> primitive_root(21) is None
    True
    >>> primitive_root(50, smallest=False)
    27

    See Also
    ========

    is_primitive_root

    References
    ==========

    .. [1] W. Stein "Elementary Number Theory" (2011), page 44
    .. [2] P. Hackman "Elementary Number Theory" (2009), Chapter C

    '''
    p = as_int(p)
    if p <= 1:
        raise ValueError('p should be an integer greater than 1')
    if p <= 4:
        return p - 1
    p_even = None % 2 == 0
    if not p_even:
        q = p
    elif p % 4:
        q = p // 2
    else:
        return None
    if None(q):
        e = 1
    else:
        m = _perfect_power(q, 3)
        if not m:
            return None
        (q, e) = None
        if not isprime(q):
            return None
        if not None:
            if p_even:
                return next(_primitive_root_prime_power2_iter(q, e))
            return None(_primitive_root_prime_power_iter(q, e))
        if None:
            for i in range(3, p, 2):
                if i % q and is_primitive_root(i, p):
                    
                    return None, i
                if e == 1 or pow(g, q - 1, q ** 2) != 1:
                    return g
                for None in next(_primitive_root_prime_iter(q))(g + 1, p):
                    if i % q and is_primitive_root(i, p):
                        
                        return None, i
                    return None


def is_primitive_root(a, p):
    """ Returns True if ``a`` is a primitive root of ``p``.

    Explanation
    ===========

    ``a`` is said to be the primitive root of ``p`` if `\\gcd(a, p) = 1` and
    `\\phi(p)` is the smallest positive number s.t.

        `a^{\\phi(p)} \\equiv 1 \\pmod{p}`.

    where `\\phi(p)` is Euler's totient function.

    The primitive root of ``p`` exist only for
    `p = 2, 4, q^e, 2q^e` (``q`` is an odd prime).
    Hence, if it is not such a ``p``, it returns False.
    To determine the primitive root, we need to know
    the prime factorization of ``q-1``.
    The hardness of the determination depends on this complexity.

    Parameters
    ==========

    a : integer
    p : integer, ``p`` > 1. ``a`` and ``p`` should be relatively prime

    Returns
    =======

    bool : If True, ``a`` is the primitive root of ``p``.

    Raises
    ======

    ValueError
        If `p \\le 1` or `\\gcd(a, p) \\neq 1`.
        If ``a`` or ``p`` is not an integer.

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import totient
    >>> from sympy.ntheory import is_primitive_root, n_order
    >>> is_primitive_root(3, 10)
    True
    >>> is_primitive_root(9, 10)
    False
    >>> n_order(3, 10) == totient(10)
    True
    >>> n_order(9, 10) == totient(10)
    False

    See Also
    ========

    primitive_root

    """
    pass
# WARNING: Decompyle incomplete


def _sqrt_mod_tonelli_shanks(a, p):
    '''
    Returns the square root in the case of ``p`` prime with ``p == 1 (mod 8)``

    Assume that the root exists.

    Parameters
    ==========

    a : int
    p : int
        prime number. should be ``p % 8 == 1``

    Returns
    =======

    int : Generally, there are two roots, but only one is returned.
          Which one is returned is random.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _sqrt_mod_tonelli_shanks
    >>> _sqrt_mod_tonelli_shanks(2, 17) in [6, 11]
    True

    References
    ==========

    .. [1] Carl Pomerance, Richard Crandall, Prime Numbers: A Computational Perspective,
           2nd Edition (2005), page 101, ISBN:978-0387252827

    '''
    s = bit_scan1(p - 1)
    t = p >> s
    if p % 12 == 5:
        d = 3
    elif p % 5 in (2, 3):
        d = 5
    else:
        d = randint(6, p - 1)
        if jacobi(d, p) == -1:
            pass
        
    A = pow(a, t, p)
    D = pow(d, t, p)
    m = 0
    for i in range(s):
        adm = A * pow(D, m, p) % p
        adm = pow(adm, 2 ** (s - 1 - i), p)
        if adm % p == p - 1:
            m += 2 ** i
        x = pow(a, (t + 1) // 2, p) * pow(D, m // 2, p) % p
        return x


def sqrt_mod(a, p, all_roots = (False,)):
    '''
    Find a root of ``x**2 = a mod p``.

    Parameters
    ==========

    a : integer
    p : positive integer
    all_roots : if True the list of roots is returned or None

    Notes
    =====

    If there is no root it is returned None; else the returned root
    is less or equal to ``p // 2``; in general is not the smallest one.
    It is returned ``p // 2`` only if it is the only root.

    Use ``all_roots`` only when it is expected that all the roots fit
    in memory; otherwise use ``sqrt_mod_iter``.

    Examples
    ========

    >>> from sympy.ntheory import sqrt_mod
    >>> sqrt_mod(11, 43)
    21
    >>> sqrt_mod(17, 32, True)
    [7, 9, 23, 25]
    '''
    if all_roots:
        return sorted(sqrt_mod_iter(a, p))
    p = None(as_int(p))
    halfp = p // 2
    x = None
    for r in sqrt_mod_iter(a, p):
        if r < halfp:
            
            return None, r
        if None > halfp:
            
            return None, p - r
        return x


def sqrt_mod_iter(a, p, domain = (int,)):
    '''
    Iterate over solutions to ``x**2 = a mod p``.

    Parameters
    ==========

    a : integer
    p : positive integer
    domain : integer domain, ``int``, ``ZZ`` or ``Integer``

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import sqrt_mod_iter
    >>> list(sqrt_mod_iter(11, 43))
    [21, 22]

    See Also
    ========

    sqrt_mod : Same functionality, but you want a sorted list or only one solution.

    '''
    pass
# WARNING: Decompyle incomplete


def _sqrt_mod_prime_power(a, p, k):
    '''
    Find the solutions to ``x**2 = a mod p**k`` when ``a % p != 0``.
    If no solution exists, return ``None``.
    Solutions are returned in an ascending list.

    Parameters
    ==========

    a : integer
    p : prime number
    k : positive integer

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _sqrt_mod_prime_power
    >>> _sqrt_mod_prime_power(11, 43, 1)
    [21, 22]

    References
    ==========

    .. [1] P. Hackman "Elementary Number Theory" (2009), page 160
    .. [2] http://www.numbertheory.org/php/squareroot.html
    .. [3] [Gathen99]_
    '''
    pk = p ** k
    a = a % pk
    if p == 2:
        if a % 8 != 1:
            return None
        if None <= 3:
            return list(range(1, pk, 2))
        r = None
        for nx in range(3, k):
            if (r ** 2 - a >> nx) % 2:
                r += 1 << nx - 1
            h = 1 << k - 1
            return sorted([
                r,
                pk - r,
                (r + h) % pk,
                -(r + h) % pk])
            if jacobi(a, p) != 1:
                return None
            if None % 4 == 3:
                res = pow(a, (p + 1) // 4, p)
            elif p % 8 == 5:
                res = pow(a, (p + 3) // 8, p)
                if pow(res, 2, p) != a % p:
                    res = res * pow(2, (p - 1) // 4, p) % p
                else:
                    res = _sqrt_mod_tonelli_shanks(a, p)
    if k > 1:
        px = p
        for _ in range(k.bit_length() - 1):
            px = px ** 2
            frinv = invert(2 * res, px)
            res = (res - (res ** 2 - a) * frinv) % px
            if k & k - 1:
                frinv = invert(2 * res, pk)
                res = (res - (res ** 2 - a) * frinv) % pk
    return sorted([
        res,
        pk - res])


def _sqrt_mod1(a, p, n):
    '''
    Find solution to ``x**2 == a mod p**n`` when ``a % p == 0``.
    If no solution exists, return ``None``.

    Parameters
    ==========

    a : integer
    p : prime number, p must divide a
    n : positive integer

    References
    ==========

    .. [1] http://www.numbertheory.org/php/squareroot.html
    '''
    pass
# WARNING: Decompyle incomplete


def is_quad_residue(a, p):
    '''
    Returns True if ``a`` (mod ``p``) is in the set of squares mod ``p``,
    i.e a % p in set([i**2 % p for i in range(p)]).

    Parameters
    ==========

    a : integer
    p : positive integer

    Returns
    =======

    bool : If True, ``x**2 == a (mod p)`` has solution.

    Raises
    ======

    ValueError
        If ``a``, ``p`` is not integer.
        If ``p`` is not positive.

    Examples
    ========

    >>> from sympy.ntheory import is_quad_residue
    >>> is_quad_residue(21, 100)
    True

    Indeed, ``pow(39, 2, 100)`` would be 21.

    >>> is_quad_residue(21, 120)
    False

    That is, for any integer ``x``, ``pow(x, 2, 120)`` is not 21.

    If ``p`` is an odd
    prime, an iterative method is used to make the determination:

    >>> from sympy.ntheory import is_quad_residue
    >>> sorted(set([i**2 % 7 for i in range(7)]))
    [0, 1, 2, 4]
    >>> [j for j in range(7) if is_quad_residue(j, 7)]
    [0, 1, 2, 4]

    See Also
    ========

    legendre_symbol, jacobi_symbol, sqrt_mod
    '''
    p = as_int(p)
    a = as_int(a)
    if p < 1:
        raise ValueError('p must be > 0')
    a %= p
    if a < 2 or p < 3:
        return True
    t = None(p)
    if t:
        a_ = a % (1 << t)
        if a_:
            r = bit_scan1(a_)
            if r % 2 or a_ >> r & 6:
                return False
            None >>= t
            a %= p
            if a < 2 or p < 3:
                return True
            j = None(a, p)
            if j == -1 or isprime(p):
                return j == 1
            for px, ex in None(p).items():
                if a % px:
                    if jacobi(a, px) != 1:
                        return False
                a_ = a % px ** ex
                if a_ == 0:
                    continue
                (a_, r) = remove(a_, px)
                if r % 2 or jacobi(a_, px) != 1:
                    return False
                return True


def is_nthpow_residue(a, n, m):
    '''
    Returns True if ``x**n == a (mod m)`` has solutions.

    References
    ==========

    .. [1] P. Hackman "Elementary Number Theory" (2009), page 76

    '''
    pass
# WARNING: Decompyle incomplete


def _is_nthpow_residue_bign_prime_power(a, n, p, k):
    '''
    Returns True if `x^n = a \\pmod{p^k}` has solutions for `n > 2`.

    Parameters
    ==========

    a : positive integer
    n : integer, n > 2
    p : prime number
    k : positive integer

    '''
    pass
# WARNING: Decompyle incomplete


def _nthroot_mod1(s, q, p, all_roots):
    '''
    Root of ``x**q = s mod p``, ``p`` prime and ``q`` divides ``p - 1``.
    Assume that the root exists.

    Parameters
    ==========

    s : integer
    q : integer, n > 2. ``q`` divides ``p - 1``.
    p : prime number
    all_roots : if False returns the smallest root, else the list of roots

    Returns
    =======

    list[int] | int :
        Root of ``x**q = s mod p``. If ``all_roots == True``,
        returned ascending list. otherwise, returned an int.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _nthroot_mod1
    >>> _nthroot_mod1(5, 3, 13, False)
    7
    >>> _nthroot_mod1(13, 4, 17, True)
    [3, 5, 12, 14]

    References
    ==========

    .. [1] A. M. Johnston, A Generalized qth Root Algorithm,
           ACM-SIAM Symposium on Discrete Algorithms (1999), pp. 929-930

    '''
    g = next(_primitive_root_prime_iter(p))
    r = s
# WARNING: Decompyle incomplete


def _nthroot_mod_prime_power(a, n, p, k):
    ''' Root of ``x**n = a mod p**k``.

    Parameters
    ==========

    a : integer
    n : integer, n > 2
    p : prime number
    k : positive integer

    Returns
    =======

    list[int] :
        Ascending list of roots of ``x**n = a mod p**k``.
        If no solution exists, return ``[]``.

    '''
    if not _is_nthpow_residue_bign_prime_power(a, n, p, k):
        return []
    a_mod_p = None % p
    if a_mod_p == 0:
        base_roots = [
            0]
    elif (p - 1) % n == 0:
        base_roots = _nthroot_mod1(a_mod_p, n, p, all_roots = True)
# WARNING: Decompyle incomplete


def nthroot_mod(a, n, p, all_roots = (False,)):
    '''
    Find the solutions to ``x**n = a mod p``.

    Parameters
    ==========

    a : integer
    n : positive integer
    p : positive integer
    all_roots : if False returns the smallest root, else the list of roots

    Returns
    =======

        list[int] | int | None :
            solutions to ``x**n = a mod p``.
            The table of the output type is:

            ========== ========== ==========
            all_roots  has roots  Returns
            ========== ========== ==========
            True       Yes        list[int]
            True       No         []
            False      Yes        int
            False      No         None
            ========== ========== ==========

    Raises
    ======

        ValueError
            If ``a``, ``n`` or ``p`` is not integer.
            If ``n`` or ``p`` is not positive.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import nthroot_mod
    >>> nthroot_mod(11, 4, 19)
    8
    >>> nthroot_mod(11, 4, 19, True)
    [8, 11]
    >>> nthroot_mod(68, 3, 109)
    23

    References
    ==========

    .. [1] P. Hackman "Elementary Number Theory" (2009), page 76

    '''
    pass
# WARNING: Decompyle incomplete


def quadratic_residues(p = None):
    '''
    Returns the list of quadratic residues.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import quadratic_residues
    >>> quadratic_residues(7)
    [0, 1, 2, 4]
    '''
    pass
# WARNING: Decompyle incomplete

legendre_symbol = (lambda a, p: _legendre_symbol = legendre_symbolimport sympy.functions.combinatorial.numbers_legendre_symbol(a, p))()
jacobi_symbol = (lambda m, n: _jacobi_symbol = jacobi_symbolimport sympy.functions.combinatorial.numbers_jacobi_symbol(m, n))()
mobius = (lambda n: _mobius = mobiusimport sympy.functions.combinatorial.numbers_mobius(n))()

def _discrete_log_trial_mul(n, a, b, order = (None,)):
    '''
    Trial multiplication algorithm for computing the discrete logarithm of
    ``a`` to the base ``b`` modulo ``n``.

    The algorithm finds the discrete logarithm using exhaustive search. This
    naive method is used as fallback algorithm of ``discrete_log`` when the
    group order is very small.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _discrete_log_trial_mul
    >>> _discrete_log_trial_mul(41, 15, 7)
    3

    See Also
    ========

    discrete_log

    References
    ==========

    .. [1] "Handbook of applied cryptography", Menezes, A. J., Van, O. P. C., &
        Vanstone, S. A. (1997).
    '''
    a %= n
    b %= n
# WARNING: Decompyle incomplete


def _discrete_log_shanks_steps(n, a, b, order = (None,)):
    '''
    Baby-step giant-step algorithm for computing the discrete logarithm of
    ``a`` to the base ``b`` modulo ``n``.

    The algorithm is a time-memory trade-off of the method of exhaustive
    search. It uses `O(sqrt(m))` memory, where `m` is the group order.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _discrete_log_shanks_steps
    >>> _discrete_log_shanks_steps(41, 15, 7)
    3

    See Also
    ========

    discrete_log

    References
    ==========

    .. [1] "Handbook of applied cryptography", Menezes, A. J., Van, O. P. C., &
        Vanstone, S. A. (1997).
    '''
    a %= n
    b %= n
# WARNING: Decompyle incomplete


def _discrete_log_pollard_rho(n, a, b, order, retries, rseed = (None, 10, None)):
    '''
    Pollard\'s Rho algorithm for computing the discrete logarithm of ``a`` to
    the base ``b`` modulo ``n``.

    It is a randomized algorithm with the same expected running time as
    ``_discrete_log_shanks_steps``, but requires a negligible amount of memory.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _discrete_log_pollard_rho
    >>> _discrete_log_pollard_rho(227, 3**7, 3)
    7

    See Also
    ========

    discrete_log

    References
    ==========

    .. [1] "Handbook of applied cryptography", Menezes, A. J., Van, O. P. C., &
        Vanstone, S. A. (1997).
    '''
    a %= n
    b %= n
# WARNING: Decompyle incomplete


def _discrete_log_is_smooth(n = deprecated('The `sympy.ntheory.residue_ntheory.legendre_symbol` has been moved to `sympy.functions.combinatorial.numbers.legendre_symbol`.', deprecated_since_version = '1.13', active_deprecations_target = 'deprecated-ntheory-symbolic-functions'), factorbase = deprecated('The `sympy.ntheory.residue_ntheory.jacobi_symbol` has been moved to `sympy.functions.combinatorial.numbers.jacobi_symbol`.', deprecated_since_version = '1.13', active_deprecations_target = 'deprecated-ntheory-symbolic-functions')):
    '''Try to factor n with respect to a given factorbase.
    Upon success a list of exponents with repect to the factorbase is returned.
    Otherwise None.'''
    factors = [
        0] * len(factorbase)
# WARNING: Decompyle incomplete


def _discrete_log_index_calculus(n, a, b, order, rseed = (None,)):
    '''
    Index Calculus algorithm for computing the discrete logarithm of ``a`` to
    the base ``b`` modulo ``n``.

    The group order must be given and prime. It is not suitable for small orders
    and the algorithm might fail to find a solution in such situations.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _discrete_log_index_calculus
    >>> _discrete_log_index_calculus(24570203447, 23859756228, 2, 12285101723)
    4519867240

    See Also
    ========

    discrete_log

    References
    ==========

    .. [1] "Handbook of applied cryptography", Menezes, A. J., Van, O. P. C., &
        Vanstone, S. A. (1997).
    '''
    pass
# WARNING: Decompyle incomplete


def _discrete_log_pohlig_hellman(n, a, b, order, order_factors = (None, None)):
    '''
    Pohlig-Hellman algorithm for computing the discrete logarithm of ``a`` to
    the base ``b`` modulo ``n``.

    In order to compute the discrete logarithm, the algorithm takes advantage
    of the factorization of the group order. It is more efficient when the
    group order factors into many small primes.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _discrete_log_pohlig_hellman
    >>> _discrete_log_pohlig_hellman(251, 210, 71)
    197

    See Also
    ========

    discrete_log

    References
    ==========

    .. [1] "Handbook of applied cryptography", Menezes, A. J., Van, O. P. C., &
        Vanstone, S. A. (1997).
    '''
    crt = crt
    import modular
    a %= n
    b %= n
# WARNING: Decompyle incomplete


def discrete_log(n, a, b, order, prime_order = (None, None)):
    '''
    Compute the discrete logarithm of ``a`` to the base ``b`` modulo ``n``.

    This is a recursive function to reduce the discrete logarithm problem in
    cyclic groups of composite order to the problem in cyclic groups of prime
    order.

    It employs different algorithms depending on the problem (subgroup order
    size, prime order or not):

        * Trial multiplication
        * Baby-step giant-step
        * Pollard\'s Rho
        * Index Calculus
        * Pohlig-Hellman

    Examples
    ========

    >>> from sympy.ntheory import discrete_log
    >>> discrete_log(41, 15, 7)
    3

    References
    ==========

    .. [1] https://mathworld.wolfram.com/DiscreteLogarithm.html
    .. [2] "Handbook of applied cryptography", Menezes, A. J., Van, O. P. C., &
        Vanstone, S. A. (1997).

    '''
    sqrt = sqrt
    log = log
    import math
    b = as_int(b)
    a = as_int(a)
    n = as_int(n)
# WARNING: Decompyle incomplete


def quadratic_congruence(a, b, c, n):
    '''
    Find the solutions to `a x^2 + b x + c \\equiv 0 \\pmod{n}`.

    Parameters
    ==========

    a : int
    b : int
    c : int
    n : int
        A positive integer.

    Returns
    =======

    list[int] :
        A sorted list of solutions. If no solution exists, ``[]``.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import quadratic_congruence
    >>> quadratic_congruence(2, 5, 3, 7) # 2x^2 + 5x + 3 = 0 (mod 7)
    [2, 6]
    >>> quadratic_congruence(8, 6, 4, 15) # No solution
    []

    See Also
    ========

    polynomial_congruence : Solve the polynomial congruence

    '''
    pass
# WARNING: Decompyle incomplete


def _valid_expr(expr):
    '''
    return coefficients of expr if it is a univariate polynomial
    with integer coefficients else raise a ValueError.
    '''
    if not expr.is_polynomial():
        raise ValueError('The expression should be a polynomial')
    polynomial = Poly(expr)
    if not polynomial.is_univariate:
        raise ValueError('The expression should be univariate')
    if not polynomial.domain == ZZ:
        raise ValueError('The expression should should have integer coefficients')
    return polynomial.all_coeffs()


def polynomial_congruence(expr, m):
    '''
    Find the solutions to a polynomial congruence equation modulo m.

    Parameters
    ==========

    expr : integer coefficient polynomial
    m : positive integer

    Examples
    ========

    >>> from sympy.ntheory import polynomial_congruence
    >>> from sympy.abc import x
    >>> expr = x**6 - 2*x**5 -35
    >>> polynomial_congruence(expr, 6125)
    [3257]

    See Also
    ========

    sympy.polys.galoistools.gf_csolve : low level solving routine used by this routine

    '''
    pass
# WARNING: Decompyle incomplete


def binomial_mod(n, m, k):
    """Compute ``binomial(n, m) % k``.

    Explanation
    ===========

    Returns ``binomial(n, m) % k`` using a generalization of Lucas'
    Theorem for prime powers given by Granville [1]_, in conjunction with
    the Chinese Remainder Theorem.  The residue for each prime power
    is calculated in time O(log^2(n) + q^4*log(n)log(p) + q^4*p*log^3(p)).

    Parameters
    ==========

    n : an integer
    m : an integer
    k : a positive integer

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import binomial_mod
    >>> binomial_mod(10, 2, 6)  # binomial(10, 2) = 45
    3
    >>> binomial_mod(17, 9, 10)  # binomial(17, 9) = 24310
    0

    References
    ==========

    .. [1] Binomial coefficients modulo prime powers, Andrew Granville,
        Available: https://web.archive.org/web/20170202003812/http://www.dms.umontreal.ca/~andrew/PDF/BinCoeff.pdf
    """
    pass
# WARNING: Decompyle incomplete


def _binomial_mod_prime_power(n, m, p, q):
    '''Compute ``binomial(n, m) % p**q`` for a prime ``p``.

    Parameters
    ==========

    n : positive integer
    m : a nonnegative integer
    p : a prime
    q : a positive integer (the prime exponent)

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import _binomial_mod_prime_power
    >>> _binomial_mod_prime_power(10, 2, 3, 2)  # binomial(10, 2) = 45
    0
    >>> _binomial_mod_prime_power(17, 9, 2, 4)  # binomial(17, 9) = 24310
    6

    References
    ==========

    .. [1] Binomial coefficients modulo prime powers, Andrew Granville,
        Available: https://web.archive.org/web/20170202003812/http://www.dms.umontreal.ca/~andrew/PDF/BinCoeff.pdf
    '''
    pass
# WARNING: Decompyle incomplete
