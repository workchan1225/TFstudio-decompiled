# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: orderings.pyc (Python 3.11)

'''Definitions of monomial orderings. '''
from __future__ import annotations
__all__ = [
    'lex',
    'grlex',
    'grevlex',
    'ilex',
    'igrlex',
    'igrevlex']
from sympy.core import Symbol
from sympy.utilities.iterables import iterable

class MonomialOrder:
    '''Base class for monomial orderings. '''
    alias: 'str | None' = None
    is_global: 'bool | None' = None
    is_default = False
    
    def __repr__(self):
        return self.__class__.__name__ + '()'

    
    def __str__(self):
        return self.alias

    
    def __call__(self, monomial):
        raise NotImplementedError

    
    def __eq__(self, other):
        return self.__class__ == other.__class__

    
    def __hash__(self):
        return hash(self.__class__)

    
    def __ne__(self, other):
        return not (self == other)



class LexOrder(MonomialOrder):
    '''Lexicographic order of monomials. '''
    alias = 'lex'
    is_global = True
    is_default = True
    
    def __call__(self, monomial):
        return monomial



class GradedLexOrder(MonomialOrder):
    '''Graded lexicographic order of monomials. '''
    alias = 'grlex'
    is_global = True
    
    def __call__(self, monomial):
        return (sum(monomial), monomial)



class ReversedGradedLexOrder(MonomialOrder):
    '''Reversed graded lexicographic order of monomials. '''
    alias = 'grevlex'
    is_global = True
    
    def __call__(self, monomial):
        return (tuple, reversed((lambda .0: [ -m for m in .0 ])(monomial())))



class ProductOrder(MonomialOrder):
    '''
    A product order built from other monomial orders.

    Given (not necessarily total) orders O1, O2, ..., On, their product order
    P is defined as M1 > M2 iff there exists i such that O1(M1) = O2(M2),
    ..., Oi(M1) = Oi(M2), O{i+1}(M1) > O{i+1}(M2).

    Product orders are typically built from monomial orders on different sets
    of variables.

    ProductOrder is constructed by passing a list of pairs
    [(O1, L1), (O2, L2), ...] where Oi are MonomialOrders and Li are callables.
    Upon comparison, the Li are passed the total monomial, and should filter
    out the part of the monomial to pass to Oi.

    Examples
    ========

    We can use a lexicographic order on x_1, x_2 and also on
    y_1, y_2, y_3, and their product on {x_i, y_i} as follows:

    >>> from sympy.polys.orderings import lex, grlex, ProductOrder
    >>> P = ProductOrder(
    ...     (lex, lambda m: m[:2]), # lex order on x_1 and x_2 of monomial
    ...     (grlex, lambda m: m[2:]) # grlex on y_1, y_2, y_3
    ... )
    >>> P((2, 1, 1, 0, 0)) > P((1, 10, 0, 2, 0))
    True

    Here the exponent `2` of `x_1` in the first monomial
    (`x_1^2 x_2 y_1`) is bigger than the exponent `1` of `x_1` in the
    second monomial (`x_1 x_2^10 y_2^2`), so the first monomial is greater
    in the product ordering.

    >>> P((2, 1, 1, 0, 0)) < P((2, 1, 0, 2, 0))
    True

    Here the exponents of `x_1` and `x_2` agree, so the grlex order on
    `y_1, y_2, y_3` is used to decide the ordering. In this case the monomial
    `y_2^2` is ordered larger than `y_1`, since for the grlex order the degree
    of the monomial is most important.
    '''
    
    def __init__(self, *args):
        self.args = args

    
    def __call__(self, monomial):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        contents = self.args()
        return self.__class__.__name__ + '(' + ', '.join(contents) + ')'

    
    def __str__(self):
        contents = self.args()
        return self.__class__.__name__ + '(' + ', '.join(contents) + ')'

    
    def __eq__(self, other):
        if not isinstance(other, ProductOrder):
            return False
        return None.args == other.args

    
    def __hash__(self):
        return hash((self.__class__, self.args))

    is_global = (lambda self: if (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
            return True
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
            return False
        return all
)()


class InverseOrder(MonomialOrder):
    '''
    The "inverse" of another monomial order.

    If O is any monomial order, we can construct another monomial order iO
    such that `A >_{iO} B` if and only if `B >_O A`. This is useful for
    constructing local orders.

    Note that many algorithms only work with *global* orders.

    For example, in the inverse lexicographic order on a single variable `x`,
    high powers of `x` count as small:

    >>> from sympy.polys.orderings import lex, InverseOrder
    >>> ilex = InverseOrder(lex)
    >>> ilex((5,)) < ilex((0,))
    True
    '''
    
    def __init__(self, O):
        self.O = O

    
    def __str__(self):
        return 'i' + str(self.O)

    
    def __call__(self, monomial):
        pass
    # WARNING: Decompyle incomplete

    is_global = (lambda self: if self.O.is_global is True:
Falseif None.O.is_global is False:
True)()
    
    def __eq__(self, other):
