# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ordinals.pyc (Python 3.11)

from sympy.core import Basic, Integer
import operator

class OmegaPower(Basic):
    '''
    Represents ordinal exponential and multiplication terms one of the
    building blocks of the :class:`Ordinal` class.
    In ``OmegaPower(a, b)``, ``a`` represents exponent and ``b`` represents multiplicity.
    '''
    
    def __new__(cls, a, b):
        if isinstance(b, int):
            b = Integer(b)
        if isinstance(b, Integer) or b <= 0:
            raise TypeError('multiplicity must be a positive integer')
        if not isinstance(a, Ordinal):
            a = Ordinal.convert(a)
        return Basic.__new__(cls, a, b)

    exp = (lambda self: self.args[0])()
    mult = (lambda self: self.args[1])()
    
    def _compare_term(self, other, op):
        if self.exp == other.exp:
            return op(self.mult, other.mult)
        return op(self.exp, other.exp)

    
    def __eq__(self, other):
        if not isinstance(other, OmegaPower):
            
            try:
                other = OmegaPower(0, other)
            except TypeError:
                return 

            return self.args == other.args

    
    def __hash__(self):
        return Basic.__hash__(self)

    
    def __lt__(self, other):
        if not isinstance(other, OmegaPower):
            
            try:
                other = OmegaPower(0, other)
            except TypeError:
                return 

            return self._compare_term(other, operator.lt)



class Ordinal(Basic):
    pass
# WARNING: Decompyle incomplete


class OrdinalZero(Ordinal):
    '''The ordinal zero.

    OrdinalZero can be imported as ``ord0``.
    '''
    pass


class OrdinalOmega(Ordinal):
    '''The ordinal omega which forms the base of all ordinals in cantor normal form.

    OrdinalOmega can be imported as ``omega``.

    Examples
    ========

    >>> from sympy.sets.ordinals import omega
    >>> omega + omega
    w*2
    '''
    
    def __new__(cls):
        return Ordinal.__new__(cls)

    terms = (lambda self: (OmegaPower(1, 1),))()

ord0 = OrdinalZero()
omega = OrdinalOmega()
