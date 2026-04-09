# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: old_polynomialring.pyc (Python 3.11)

'''Implementation of :class:`PolynomialRing` class. '''
from sympy.polys.agca.modules import FreeModulePolyRing
from sympy.polys.domains.compositedomain import CompositeDomain
from sympy.polys.domains.old_fractionfield import FractionField
from sympy.polys.domains.ring import Ring
from sympy.polys.orderings import monomial_key, build_product_order
from sympy.polys.polyclasses import DMP, DMF
from sympy.polys.polyerrors import GeneratorsNeeded, PolynomialError, CoercionFailed, ExactQuotientFailed, NotReversible
from sympy.polys.polyutils import dict_from_basic, basic_from_dict, _dict_reorder
from sympy.utilities import public
from sympy.utilities.iterables import iterable
PolynomialRingBase = <NODE:12>()

def _vector_to_sdm_helper(v, order):
    '''Helper method for common code in Global and Local poly rings.'''
    sdm_from_dict = sdm_from_dict
    import sympy.polys.distributedmodules
    d = { }
    for i, e in enumerate(v):
        for key, value in e.to_dict().items():
            d[(i,) + key] = value
            return sdm_from_dict(d, order)

GlobalPolynomialRing = <NODE:12>()

class GeneralizedPolynomialRing(PolynomialRingBase):
    '''A generalized polynomial ring, with objects DMF. '''
    dtype = DMF
    
    def new(self, a):
        '''Construct an element of ``self`` domain from ``a``. '''
        res = self.dtype(a, self.dom, len(self.gens) - 1)
        if res.denom().terms(order = self.order)[0][0] != (0,) * len(self.gens):
            sstr = sstr
            import sympy.printing.str
            raise CoercionFailed(f'''denominator {sstr(res)!s} not allowed in {self!s}''')
        return res

    
    def __contains__(self, a):
        
        try:
            a = self.convert(a)
        except CoercionFailed:
            return False

        return a.denom().terms(order = self.order)[0][0] == (0,) * len(self.gens)

    
    def to_sympy(self, a):
        '''Convert ``a`` to a SymPy object. '''
        pass
    # WARNING: Decompyle incomplete

    
    def from_sympy(self, a):
        """Convert SymPy's expression to ``dtype``. """
        (p, q) = a.as_numer_denom()
        (num, _) = dict_from_basic(p, gens = self.gens)
        (den, _) = dict_from_basic(q, gens = self.gens)
        for k, v in num.items():
            num[k] = self.dom.from_sympy(v)
            for k, v in den.items():
                den[k] = self.dom.from_sympy(v)
                return self((num, den)).cancel()

    
    def exquo(self, a, b):
        '''Exact quotient of ``a`` and ``b``. '''
        r = a / b
        
        try:
            r = self.new((r.num, r.den))
        except CoercionFailed:
            raise ExactQuotientFailed(a, b, self)

        return r

    
    def from_FractionField(K1, a, K0):
        dmf = K1.get_field().from_FractionField(a, K0)
        return K1((dmf.num, dmf.den))

    
    def _vector_to_sdm(self, v, order):
        '''
        Turn an iterable into a sparse distributed module.

        Note that the vector is multiplied by a unit first to make all entries
        polynomials.

        Examples
        ========

        >>> from sympy import ilex, QQ
        >>> from sympy.abc import x, y
        >>> R = QQ.old_poly_ring(x, y, order=ilex)
        >>> f = R.convert((x + 2*y) / (1 + x))
        >>> g = R.convert(x * y)
        >>> R._vector_to_sdm([f, g], ilex)
        [((0, 0, 1), 2), ((0, 1, 0), 1), ((1, 1, 1), 1), ((1,
          2, 1), 1)]
        '''
        pass
    # WARNING: Decompyle incomplete


PolynomialRing = (lambda dom: order = opts.get('order', GeneralizedPolynomialRing.default_order)if iterable(order):
order = build_product_order(order, gens)order = monomial_key(order)opts['order'] = order# WARNING: Decompyle incomplete
)()
