# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rings.pyc (Python 3.11)

'''Sparse polynomial rings. '''
from __future__ import annotations
from typing import Any
from operator import add, mul, lt, le, gt, ge
from functools import reduce
from types import GeneratorType
from sympy.core.expr import Expr
from sympy.core.intfunc import igcd
from sympy.core.symbol import Symbol, symbols as _symbols
from sympy.core.sympify import CantSympify, sympify
from sympy.ntheory.multinomial import multinomial_coefficients
from sympy.polys.compatibility import IPolys
from sympy.polys.constructor import construct_domain
from sympy.polys.densebasic import ninf, dmp_to_dict, dmp_from_dict
from sympy.polys.domains.domainelement import DomainElement
from sympy.polys.domains.polynomialring import PolynomialRing
from sympy.polys.heuristicgcd import heugcd
from sympy.polys.monomials import MonomialOps
from sympy.polys.orderings import lex
from sympy.polys.polyerrors import CoercionFailed, GeneratorsError, ExactQuotientFailed, MultivariatePolynomialError
from sympy.polys.polyoptions import Domain as DomainOpt, Order as OrderOpt, build_options
from sympy.polys.polyutils import expr_from_dict, _dict_reorder, _parallel_dict_from_expr
from sympy.printing.defaults import DefaultPrinting
from sympy.utilities import public, subsets
from sympy.utilities.iterables import is_sequence
from sympy.utilities.magic import pollute
ring = (lambda symbols, domain, order = (lex,): _ring = PolyRing(symbols, domain, order)(_ring,) + _ring.gens)()
xring = (lambda symbols, domain, order = (lex,): _ring = PolyRing(symbols, domain, order)(_ring, _ring.gens))()
vring = (lambda symbols, domain, order = (lex,): _ring = PolyRing(symbols, domain, order)(lambda .0: [ sym.name for sym in .0 ])(_ring.symbols(), _ring.gens)
    return _ring
)()
sring = (lambda exprs: pass# WARNING: Decompyle incomplete
)()

def _parse_symbols(symbols):
    if isinstance(symbols, str):
        return _symbols(symbols, seq = True) if symbols else ()
    if None(symbols, Expr):
        return (symbols,)
    if None(symbols):
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(symbols()):
            return _symbols(symbols)
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(symbols()):
            return symbols
        raise all('expected a string, Symbol or expression or a non-empty sequence of strings, Symbols or expressions')

_ring_cache: 'dict[Any, Any]' = { }

class PolyRing(IPolys, DefaultPrinting):
    '''Multivariate distributed polynomial ring. '''
    
    def __new__(cls, symbols, domain, order = (lex,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _gens(self):
        '''Return a list of polynomial generators. '''
        one = self.domain.one
        _gens = []
        for i in range(self.ngens):
            expv = self.monomial_basis(i)
            poly = self.zero
            poly[expv] = one
            _gens.append(poly)
            return tuple(_gens)

    
    def __getnewargs__(self):
        return (self.symbols, self.domain, self.order)

    
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['leading_expv']
        for key in state:
            if key.startswith('monomial_'):
                del state[key]
            return state

    
    def __hash__(self):
        return self._hash

    
    def __eq__(self, other):
        if isinstance(other, PolyRing):
            pass
        return (self.symbols, self.domain, self.ngens, self.order) == (other.symbols, other.domain, other.ngens, other.order)

    
    def __ne__(self, other):
        return not (self == other)

    
    def clone(self, symbols, domain, order = (None, None, None)):
