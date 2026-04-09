# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multinomial.pyc (Python 3.11)

from sympy.utilities.misc import as_int

def binomial_coefficients(n):
    '''Return a dictionary containing pairs :math:`{(k1,k2) : C_kn}` where
    :math:`C_kn` are binomial coefficients and :math:`n=k1+k2`.

    Examples
    ========

    >>> from sympy.ntheory import binomial_coefficients
    >>> binomial_coefficients(9)
    {(0, 9): 1, (1, 8): 9, (2, 7): 36, (3, 6): 84,
     (4, 5): 126, (5, 4): 126, (6, 3): 84, (7, 2): 36, (8, 1): 9, (9, 0): 1}

    See Also
    ========

    binomial_coefficients_list, multinomial_coefficients
    '''
    n = as_int(n)
    d = {
        (n, 0): 1,
        (0, n): 1 }
    a = 1
    for k in range(1, n // 2 + 1):
        a = a * ((n - k) + 1) // k
        d[(k, n - k)] = a
        d[(n - k, k)] = a
        return d


def binomial_coefficients_list(n):
    """ Return a list of binomial coefficients as rows of the Pascal's
    triangle.

    Examples
    ========

    >>> from sympy.ntheory import binomial_coefficients_list
    >>> binomial_coefficients_list(9)
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

    See Also
    ========

    binomial_coefficients, multinomial_coefficients
    """
    n = as_int(n)
    d = [
        1] * (n + 1)
    a = 1
    for k in range(1, n // 2 + 1):
        a = a * ((n - k) + 1) // k
        d[k] = a
        d[n - k] = a
        return d


def multinomial_coefficients(m, n):
    '''Return a dictionary containing pairs ``{(k1,k2,..,km) : C_kn}``
    where ``C_kn`` are multinomial coefficients such that
    ``n=k1+k2+..+km``.

    Examples
    ========

    >>> from sympy.ntheory import multinomial_coefficients
    >>> multinomial_coefficients(2, 5) # indirect doctest
    {(0, 5): 1, (1, 4): 5, (2, 3): 10, (3, 2): 10, (4, 1): 5, (5, 0): 1}

    Notes
    =====

    The algorithm is based on the following result:

    .. math::
        \\binom{n}{k_1, \\ldots, k_m} =
        \\frac{k_1 + 1}{n - k_1} \\sum_{i=2}^m \\binom{n}{k_1 + 1, \\ldots, k_i - 1, \\ldots}

    Code contributed to Sage by Yann Laigle-Chapuy, copied with permission
    of the author.

    See Also
    ========

    binomial_coefficients_list, binomial_coefficients
    '''
    m = as_int(m)
    n = as_int(n)
    if not m:
        if n:
            return { }
        return {
            None: 1 }
    if None == 2:
        return binomial_coefficients(n)
    if None >= 2 * n and n > 1:
        return dict(multinomial_coefficients_iterator(m, n))
    t = [
        None] + [
        0] * (m - 1)
    r = {
        tuple(t): 1 }
    if n:
        j = 0
    else:
        j = m
# WARNING: Decompyle incomplete


def multinomial_coefficients_iterator(m, n, _tuple = (tuple,)):
    '''multinomial coefficient iterator

    This routine has been optimized for `m` large with respect to `n` by taking
    advantage of the fact that when the monomial tuples `t` are stripped of
    zeros, their coefficient is the same as that of the monomial tuples from
    ``multinomial_coefficients(n, n)``. Therefore, the latter coefficients are
    precomputed to save memory and time.

    >>> from sympy.ntheory.multinomial import multinomial_coefficients
    >>> m53, m33 = multinomial_coefficients(5,3), multinomial_coefficients(3,3)
    >>> m53[(0,0,0,1,2)] == m53[(0,0,1,0,2)] == m53[(1,0,2,0,0)] == m33[(0,1,2)]
    True

    Examples
    ========

    >>> from sympy.ntheory.multinomial import multinomial_coefficients_iterator
    >>> it = multinomial_coefficients_iterator(20,3)
    >>> next(it)
    ((3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 1)
    '''
    pass
# WARNING: Decompyle incomplete
