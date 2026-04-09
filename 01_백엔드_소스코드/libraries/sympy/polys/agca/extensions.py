# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extensions.pyc (Python 3.11)

'''Finite extensions of ring domains.'''
from sympy.polys.domains.domain import Domain
from sympy.polys.domains.domainelement import DomainElement
from sympy.polys.polyerrors import CoercionFailed, NotInvertible, GeneratorsError
from sympy.polys.polytools import Poly
from sympy.printing.defaults import DefaultPrinting

class ExtensionElement(DefaultPrinting, DomainElement):
    '''
    Element of a finite extension.

    A class of univariate polynomials modulo the ``modulus``
    of the extension ``ext``. It is represented by the
    unique polynomial ``rep`` of lowest degree. Both
    ``rep`` and the representation ``mod`` of ``modulus``
    are of class DMP.

    '''
    __slots__ = ('rep', 'ext')
    
    def __init__(self, rep, ext):
        self.rep = rep
        self.ext = ext

    
    def parent(f):
        return f.ext

    
    def as_expr(f):
        return f.ext.to_sympy(f)

    
    def __bool__(f):
        return bool(f.rep)

    
    def __pos__(f):
        return f

    
    def __neg__(f):
        return ExtElem(-(f.rep), f.ext)

    
    def _get_rep(f, g):
        if isinstance(g, ExtElem):
            if g.ext == f.ext:
                return g.rep
            return None
        
        try:
            g = f.ext.convert(g)
            return g.rep
        except CoercionFailed:
            return None


    
    def __add__(f, g):
        rep = f._get_rep(g)
    # WARNING: Decompyle incomplete

    __radd__ = __add__
    
    def __sub__(f, g):
        rep = f._get_rep(g)
    # WARNING: Decompyle incomplete

    
    def __rsub__(f, g):
        rep = f._get_rep(g)
    # WARNING: Decompyle incomplete

    
    def __mul__(f, g):
        rep = f._get_rep(g)
    # WARNING: Decompyle incomplete

    __rmul__ = __mul__
    
    def _divcheck(f):
        '''Raise if division is not implemented for this divisor'''
        if not f:
            raise NotInvertible('Zero divisor')
        if f.ext.is_Field:
            return True
        if None.rep.is_ground and f.ext.domain.is_unit(f.rep.LC()):
            return True
        msg = f'''{f} in {f.ext}. Only division by invertible constants is implemented.'''
        raise NotImplementedError(msg)

    
    def inverse(f):
        '''Multiplicative inverse.

        Raises
        ======

        NotInvertible
            If the element is a zero divisor.

        '''
        f._divcheck()
        if f.ext.is_Field:
            invrep = f.rep.invert(f.ext.mod)
        else:
            R = f.ext.ring
            invrep = R.exquo(R.one, f.rep)
        return ExtElem(invrep, f.ext)

    
    def __truediv__(f, g):
        rep = f._get_rep(g)
    # WARNING: Decompyle incomplete

    __floordiv__ = __truediv__
    
    def __rtruediv__(f, g):
        
        try:
            g = f.ext.convert(g)
        except CoercionFailed:
            return 

        return g / f

    __rfloordiv__ = __rtruediv__
    
    def __mod__(f, g):
        rep = f._get_rep(g)
    # WARNING: Decompyle incomplete

    
    def __rmod__(f, g):
        
        try:
            g = f.ext.convert(g)
        except CoercionFailed:
            return 

        return g % f

    
    def __pow__(f, n):
        if not isinstance(n, int):
            raise TypeError("exponent of type 'int' expected")
    # WARNING: Decompyle incomplete

    
    def __eq__(f, g):
