# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rootoftools.pyc (Python 3.11)

'''Implementation of RootOf class and related tools. '''
from sympy.core.basic import Basic
from sympy.core import S, Expr, Integer, Float, I, oo, Add, Lambda, symbols, sympify, Rational, Dummy
from sympy.core.cache import cacheit
from sympy.core.relational import is_le
from sympy.core.sorting import ordered
from sympy.polys.domains import QQ
from sympy.polys.polyerrors import MultivariatePolynomialError, GeneratorsNeeded, PolynomialError, DomainError
from sympy.polys.polyfuncs import symmetrize, viete
from sympy.polys.polyroots import roots_linear, roots_quadratic, roots_binomial, preprocess_roots, roots
from sympy.polys.polytools import Poly, PurePoly, factor
from sympy.polys.rationaltools import together
from sympy.polys.rootisolation import dup_isolate_complex_roots_sqf, dup_isolate_real_roots_sqf
from sympy.utilities import lambdify, public, sift, numbered_symbols
from mpmath import mpf, mpc, findroot, workprec
from mpmath.libmp.libmpf import dps_to_prec, prec_to_dps
from sympy.multipledispatch import dispatch
from itertools import chain
__all__ = [
    'CRootOf']

class _pure_key_dict:
    """A minimal dictionary that makes sure that the key is a
    univariate PurePoly instance.

    Examples
    ========

    Only the following actions are guaranteed:

    >>> from sympy.polys.rootoftools import _pure_key_dict
    >>> from sympy import PurePoly
    >>> from sympy.abc import x, y

    1) creation

    >>> P = _pure_key_dict()

    2) assignment for a PurePoly or univariate polynomial

    >>> P[x] = 1
    >>> P[PurePoly(x - y, x)] = 2

    3) retrieval based on PurePoly key comparison (use this
       instead of the get method)

    >>> P[y]
    1

    4) KeyError when trying to retrieve a nonexisting key

    >>> P[y + 1]
    Traceback (most recent call last):
    ...
    KeyError: PurePoly(y + 1, y, domain='ZZ')

    5) ability to query with ``in``

    >>> x + 1 in P
    False

    NOTE: this is a *not* a dictionary. It is a very basic object
    for internal use that makes sure to always address its cache
    via PurePoly instances. It does not, for example, implement
    ``get`` or ``setdefault``.
    """
    
    def __init__(self):
        self._dict = { }

    
    def __getitem__(self, k):
        if not isinstance(k, PurePoly):
            if not isinstance(k, Expr) or len(k.free_symbols) == 1:
                raise KeyError
            k = PurePoly(k, expand = False)
        return self._dict[k]

    
    def __setitem__(self, k, v):
        if not isinstance(k, PurePoly):
            if not isinstance(k, Expr) or len(k.free_symbols) == 1:
                raise ValueError('expecting univariate expression')
            k = PurePoly(k, expand = False)
        self._dict[k] = v

    
    def __contains__(self, k):
        
        try:
            self[k]
            return True
        except KeyError:
            return False



_reals_cache = _pure_key_dict()
_complexes_cache = _pure_key_dict()

def _pure_factors(poly):
    (_, factors) = poly.factor_list()
    return factors()


def _imag_count_of_factor(f):
