# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subfield.pyc (Python 3.11)

'''
Functions in ``polys.numberfields.subfield`` solve the "Subfield Problem" and
allied problems, for algebraic number fields.

Following Cohen (see [Cohen93]_ Section 4.5), we can define the main problem as
follows:

* **Subfield Problem:**

  Given two number fields $\\mathbb{Q}(\\alpha)$, $\\mathbb{Q}(\\beta)$
  via the minimal polynomials for their generators $\\alpha$ and $\\beta$, decide
  whether one field is isomorphic to a subfield of the other.

From a solution to this problem flow solutions to the following problems as
well:

* **Primitive Element Problem:**

  Given several algebraic numbers
  $\\alpha_1, \\ldots, \\alpha_m$, compute a single algebraic number $\\theta$
  such that $\\mathbb{Q}(\\alpha_1, \\ldots, \\alpha_m) = \\mathbb{Q}(\\theta)$.

* **Field Isomorphism Problem:**

  Decide whether two number fields
  $\\mathbb{Q}(\\alpha)$, $\\mathbb{Q}(\\beta)$ are isomorphic.

* **Field Membership Problem:**

  Given two algebraic numbers $\\alpha$,
  $\\beta$, decide whether $\\alpha \\in \\mathbb{Q}(\\beta)$, and if so write
  $\\alpha = f(\\beta)$ for some $f(x) \\in \\mathbb{Q}[x]$.
'''
from sympy.core.add import Add
from sympy.core.numbers import AlgebraicNumber
from sympy.core.singleton import S
from sympy.core.symbol import Dummy
from sympy.core.sympify import sympify, _sympify
from sympy.ntheory import sieve
from sympy.polys.densetools import dup_eval
from sympy.polys.domains import QQ
from sympy.polys.numberfields.minpoly import _choose_factor, minimal_polynomial
from sympy.polys.polyerrors import IsomorphismFailed
from sympy.polys.polytools import Poly, PurePoly, factor_list
from sympy.utilities import public
from mpmath import MPContext

def is_isomorphism_possible(a, b):
    '''Necessary but not sufficient test for isomorphism. '''
    n = a.minpoly.degree()
    m = b.minpoly.degree()
    if m % n != 0:
        return False
    if None == m:
        return True
    da = None.minpoly.discriminant()
    db = b.minpoly.discriminant()
    half = db // 2
    k = m // n
    i = 1
    p = sieve[i]
    P = p ** k
    if P > half:
        pass
    elif not da % p % 2 and db % P:
        return False
    i += 1
    continue
    return True


def field_isomorphism_pslq(a, b):
    '''Construct field isomorphism using PSLQ algorithm. '''
    pass
# WARNING: Decompyle incomplete


def field_isomorphism_factor(a, b):
    '''Construct field isomorphism via factorization. '''
    (_, factors) = factor_list(a.minpoly, extension = b)
# WARNING: Decompyle incomplete

field_isomorphism = (lambda a = public, b = {
    'fast': True }, *, fast, n = None: b = sympify(b)a = sympify(a)if not a.is_AlgebraicNumber:
a = AlgebraicNumber(a)if not b.is_AlgebraicNumber:
b = AlgebraicNumber(b)a = a.to_primitive_element()b = b.to_primitive_element()if a == b:
a.coeffs()n = None.minpoly.degree()m = b.minpoly.degree()if n == 1:
[
a.root]if None % n != 0:
None# WARNING: Decompyle incomplete
)()

def _switch_domain(g, K):
    frep = g.rep.inject()
    hrep = frep.eject(K, front = True)
    return g.new(hrep, g.gens[0])


def _linsolve(p):
    (c, d) = p.rep.to_list()
    return -d / c

primitive_element = (lambda extension = public, x = (None,), *, ex, polys: pass# WARNING: Decompyle incomplete
)()
to_number_field = (lambda extension = public, theta = (None,), *, gen, alias: if hasattr(extension, '__iter__'):
extension = list(extension)else:
extension = [
extension]if len(extension) == 1 and isinstance(extension[0], tuple):
AlgebraicNumber(extension[0], alias = alias)(minpoly, coeffs) = None(extension, gen, polys = True)root = (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(coeffs, extension)())
# WARNING: Decompyle incomplete
)()
