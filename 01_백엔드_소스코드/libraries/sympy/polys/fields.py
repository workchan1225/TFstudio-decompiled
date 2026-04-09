# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fields.pyc (Python 3.11)

'''Sparse rational function fields. '''
from __future__ import annotations
from typing import Any
from functools import reduce
from operator import add, mul, lt, le, gt, ge
from sympy.core.expr import Expr
from sympy.core.mod import Mod
from sympy.core.numbers import Exp1
from sympy.core.singleton import S
from sympy.core.symbol import Symbol
from sympy.core.sympify import CantSympify, sympify
from sympy.functions.elementary.exponential import ExpBase
from sympy.polys.domains.domainelement import DomainElement
from sympy.polys.domains.fractionfield import FractionField
from sympy.polys.domains.polynomialring import PolynomialRing
from sympy.polys.constructor import construct_domain
from sympy.polys.orderings import lex
from sympy.polys.polyerrors import CoercionFailed
from sympy.polys.polyoptions import build_options
from sympy.polys.polyutils import _parallel_dict_from_expr
from sympy.polys.rings import PolyElement
from sympy.printing.defaults import DefaultPrinting
from sympy.utilities import public
from sympy.utilities.iterables import is_sequence
from sympy.utilities.magic import pollute
field = (lambda symbols, domain, order = (lex,): _field = FracField(symbols, domain, order)(_field,) + _field.gens)()
xfield = (lambda symbols, domain, order = (lex,): _field = FracField(symbols, domain, order)(_field, _field.gens))()
vfield = (lambda symbols, domain, order = (lex,): _field = FracField(symbols, domain, order)(lambda .0: [ sym.name for sym in .0 ])(_field.symbols(), _field.gens)
    return _field
)()
sfield = (lambda exprs: single = Falseif not is_sequence(exprs):
single = Trueexprs = [
exprs]exprs = list(map(sympify, exprs))opt = build_options(symbols, options)numdens = []# WARNING: Decompyle incomplete
)()
_field_cache: 'dict[Any, Any]' = { }

class FracField(DefaultPrinting):
    '''Multivariate distributed rational function field. '''
    
    def __new__(cls, symbols, domain, order = (lex,)):
        PolyRing = PolyRing
        import sympy.polys.rings
        ring = PolyRing(symbols, domain, order)
        symbols = ring.symbols
        ngens = ring.ngens
        domain = ring.domain
        order = ring.order
        _hash_tuple = (cls.__name__, symbols, ngens, domain, order)
        obj = _field_cache.get(_hash_tuple)
    # WARNING: Decompyle incomplete

    
    def _gens(self):
        '''Return a list of polynomial generators. '''
        pass
    # WARNING: Decompyle incomplete

    
    def __getnewargs__(self):
        return (self.symbols, self.domain, self.order)

    
    def __hash__(self):
        return self._hash

    
    def index(self, gen):
        if isinstance(gen, self.dtype):
            return self.ring.index(gen.to_poly())
        raise None(f'''expected a {self.dtype!s}, got {gen!s} instead''')

    
    def __eq__(self, other):
        if isinstance(other, FracField):
            pass
        return (self.symbols, self.ngens, self.domain, self.order) == (other.symbols, other.ngens, other.domain, other.order)

    
    def __ne__(self, other):
        return not (self == other)

    
    def raw_new(self, numer, denom = (None,)):
        return self.dtype(numer, denom)

    
    def new(self, numer, denom = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def domain_new(self, element):
        return self.domain.convert(element)

    
    def ground_new(self, element):
        
        try:
            return self.new(self.ring.ground_new(element))
        except CoercionFailed:
            domain = self.domain
            if domain.is_Field and domain.has_assoc_Field:
                ring = self.ring
                ground_field = domain.get_field()
                element = ground_field.convert(element)
                numer = ring.ground_new(ground_field.numer(element))
                denom = ring.ground_new(ground_field.denom(element))
                return 


    
    def field_new(self, element):
        if isinstance(element, FracElement):
            if self == element.field:
                return element
            if None(self.domain, FractionField) and self.domain.field == element.field:
                return self.ground_new(element)
            if None(self.domain, PolynomialRing) and self.domain.ring.to_field() == element.field:
                return self.ground_new(element)
            raise None('conversion')
        if isinstance(element, PolyElement):
            (denom, numer) = element.clear_denoms()
            if isinstance(self.domain, PolynomialRing) and numer.ring == self.domain.ring:
                numer = self.ring.ground_new(numer)
            elif isinstance(self.domain, FractionField) and numer.ring == self.domain.field.to_ring():
                numer = self.ring.ground_new(numer)
            else:
                numer = numer.set_ring(self.ring)
            denom = self.ring.ground_new(denom)
            return self.raw_new(numer, denom)
        if None(element, tuple) and len(element) == 2:
            (numer, denom) = list(map(self.ring.ring_new, element))
            return self.new(numer, denom)
        if None(element, str):
            raise NotImplementedError('parsing')
        if isinstance(element, Expr):
            return self.from_expr(element)
        return None.ground_new(element)

    __call__ = field_new
    
    def _rebuild_expr(self, expr, mapping):
        pass
    # WARNING: Decompyle incomplete

    
    def from_expr(self, expr):
        mapping = dict(list(zip(self.symbols, self.gens)))
        
        try:
            frac = self._rebuild_expr(sympify(expr), mapping)
            return self.field_new(frac)
        except CoercionFailed:
            raise ValueError(f'''expected an expression convertible to a rational function in {self!s}, got {expr!s}''')


    
    def to_domain(self):
        return FractionField(self)

    
    def to_ring(self):
        PolyRing = PolyRing
        import sympy.polys.rings
        return PolyRing(self.symbols, self.domain, self.order)



class FracElement(CantSympify, DefaultPrinting, DomainElement):
    '''Element of multivariate distributed rational function field. '''
    
    def __init__(self, numer, denom = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def raw_new(f, numer, denom):
        return f.__class__(numer, denom)

    
    def new(f, numer, denom):
        pass
    # WARNING: Decompyle incomplete

    
    def to_poly(f):
        if f.denom != 1:
            raise ValueError('f.denom should be 1')
        return f.numer

    
    def parent(self):
        return self.field.to_domain()

    
    def __getnewargs__(self):
        return (self.field, self.numer, self.denom)

    _hash = None
    
    def __hash__(self):
        _hash = self._hash
    # WARNING: Decompyle incomplete

    
    def copy(self):
        return self.raw_new(self.numer.copy(), self.denom.copy())

    
    def set_field(self, new_field):
        if self.field == new_field:
            return self
        new_ring = None.ring
        numer = self.numer.set_ring(new_ring)
        denom = self.denom.set_ring(new_ring)
        return new_field.new(numer, denom)

    
    def as_expr(self, *symbols):
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(f, g):
