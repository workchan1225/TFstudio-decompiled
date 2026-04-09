# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: quotientring.pyc (Python 3.11)

'''Implementation of :class:`QuotientRing` class.'''
from sympy.polys.agca.modules import FreeModuleQuotientRing
from sympy.polys.domains.ring import Ring
from sympy.polys.polyerrors import NotReversible, CoercionFailed
from sympy.utilities import public
QuotientRingElement = <NODE:12>()

class QuotientRing(Ring):
    '''
    Class representing (commutative) quotient rings.

    You should not usually instantiate this by hand, instead use the constructor
    from the base ring in the construction.

    >>> from sympy.abc import x
    >>> from sympy import QQ
    >>> I = QQ.old_poly_ring(x).ideal(x**3 + 1)
    >>> QQ.old_poly_ring(x).quotient_ring(I)
    QQ[x]/<x**3 + 1>

    Shorter versions are possible:

    >>> QQ.old_poly_ring(x)/I
    QQ[x]/<x**3 + 1>

    >>> QQ.old_poly_ring(x)/[x**3 + 1]
    QQ[x]/<x**3 + 1>

    Attributes:

    - ring - the base ring
    - base_ideal - the ideal used to form the quotient
    '''
    has_assoc_Ring = True
    has_assoc_Field = False
    dtype = QuotientRingElement
    
    def __init__(self, ring, ideal):
        if not ideal.ring == ring:
            raise ValueError(f'''Ideal must belong to {ring!s}, got {ideal!s}''')
        self.ring = ring
        self.base_ideal = ideal
        self.zero = self(self.ring.zero)
        self.one = self(self.ring.one)

    
    def __str__(self):
        return str(self.ring) + '/' + str(self.base_ideal)

    
    def __hash__(self):
        return hash((self.__class__.__name__, self.dtype, self.ring, self.base_ideal))

    
    def new(self, a):
        '''Construct an element of ``self`` domain from ``a``. '''
        if not isinstance(a, self.ring.dtype):
            a = self.ring(a)
        return self.dtype(self, self.base_ideal.reduce_element(a))

    
    def __eq__(self, other):
