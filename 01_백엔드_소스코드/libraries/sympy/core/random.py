# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: random.pyc (Python 3.11)

"""
When you need to use random numbers in SymPy library code, import from here
so there is only one generator working for SymPy. Imports from here should
behave the same as if they were being imported from Python's random module.
But only the routines currently used in SymPy are included here. To use others
import ``rng`` and access the method directly. For example, to capture the
current state of the generator use ``rng.getstate()``.

There is intentionally no Random to import from here. If you want
to control the state of the generator, import ``seed`` and call it
with or without an argument to set the state.

Examples
========

>>> from sympy.core.random import random, seed
>>> assert random() < 1
>>> seed(1); a = random()
>>> b = random()
>>> seed(1); c = random()
>>> assert a == c
>>> assert a != b  # remote possibility this will fail

"""
from sympy.utilities.iterables import is_sequence
from sympy.utilities.misc import as_int
import random as _random
rng = _random.Random()
choice = rng.choice
random = rng.random
randint = rng.randint
randrange = rng.randrange
sample = rng.sample
shuffle = rng.shuffle
uniform = rng.uniform
_assumptions_rng = _random.Random()
_assumptions_shuffle = _assumptions_rng.shuffle

def seed(a, version = (None, 2)):
    rng.seed(a = a, version = version)
    _assumptions_rng.seed(a = a, version = version)


def random_complex_number(a, b, c, d, rational, tolerance = (2, -1, 3, 1, False, None)):
    '''
    Return a random complex number.

    To reduce chance of hitting branch cuts or anything, we guarantee
    b <= Im z <= d, a <= Re z <= c

    When rational is True, a rational approximation to a random number
    is obtained within specified tolerance, if any.
    '''
    I = I
    import sympy.core.numbers
    nsimplify = nsimplify
    import sympy.simplify.simplify
    B = uniform(b, d)
    A = uniform(a, c)
    if not rational:
        return A + I * B
    return nsimplify(A, rational = True, tolerance = tolerance) + I * nsimplify(B, rational = True, tolerance = tolerance)


def verify_numerically(f, g, z, tol, a, b, c, d = (None, 1e-06, 2, -1, 3, 1)):
    '''
    Test numerically that f and g agree when evaluated in the argument z.

    If z is None, all symbols will be tested. This routine does not test
    whether there are Floats present with precision higher than 15 digits
    so if there are, your results may not be what you expect due to round-
    off errors.

    Examples
    ========

    >>> from sympy import sin, cos
    >>> from sympy.abc import x
    >>> from sympy.core.random import verify_numerically as tn
    >>> tn(sin(x)**2 + cos(x)**2, 1, x)
    True
    '''
    pass
# WARNING: Decompyle incomplete


def test_derivative_numerically(f, z, tol, a, b, c, d = (1e-06, 2, -1, 3, 1)):
    '''
    Test numerically that the symbolically computed derivative of f
    with respect to z is correct.

    This routine does not test whether there are Floats present with
    precision higher than 15 digits so if there are, your results may
    not be what you expect due to round-off errors.

    Examples
    ========

    >>> from sympy import sin
    >>> from sympy.abc import x
    >>> from sympy.core.random import test_derivative_numerically as td
    >>> td(sin(x), x)
    True
    '''
    comp = comp
    import sympy.core.numbers
    Derivative = Derivative
    import sympy.core.function
    z0 = random_complex_number(a, b, c, d)
    f1 = f.diff(z).subs(z, z0)
    f2 = Derivative(f, z).doit_numerically(z0)
    return comp(f1.n(), f2.n(), tol)


def _randrange(seed = (None,)):
    '''Return a randrange generator.

    ``seed`` can be

    * None - return randomly seeded generator
    * int - return a generator seeded with the int
    * list - the values to be returned will be taken from the list
      in the order given; the provided list is not modified.

    Examples
    ========

    >>> from sympy.core.random import _randrange
    >>> rr = _randrange()
    >>> rr(1000) # doctest: +SKIP
    999
    >>> rr = _randrange(3)
    >>> rr(1000) # doctest: +SKIP
    238
    >>> rr = _randrange([0, 5, 1, 3, 4])
    >>> rr(3), rr(3)
    (0, 1)
    '''
    pass
# WARNING: Decompyle incomplete


def _randint(seed = (None,)):
    '''Return a randint generator.

    ``seed`` can be

    * None - return randomly seeded generator
    * int - return a generator seeded with the int
    * list - the values to be returned will be taken from the list
      in the order given; the provided list is not modified.

    Examples
    ========

    >>> from sympy.core.random import _randint
    >>> ri = _randint()
    >>> ri(1, 1000) # doctest: +SKIP
    999
    >>> ri = _randint(3)
    >>> ri(1, 1000) # doctest: +SKIP
    238
    >>> ri = _randint([0, 5, 1, 2, 4])
    >>> ri(1, 3), ri(1, 3)
    (1, 2)
    '''
    pass
# WARNING: Decompyle incomplete
