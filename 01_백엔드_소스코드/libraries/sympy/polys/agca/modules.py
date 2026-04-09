# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: modules.pyc (Python 3.11)

'''
Computations with modules over polynomial rings.

This module implements various classes that encapsulate groebner basis
computations for modules. Most of them should not be instantiated by hand.
Instead, use the constructing routines on objects you already have.

For example, to construct a free module over ``QQ[x, y]``, call
``QQ[x, y].free_module(rank)`` instead of the ``FreeModule`` constructor.
In fact ``FreeModule`` is an abstract base class that should not be
instantiated, the ``free_module`` method instead returns the implementing class
``FreeModulePolyRing``.

In general, the abstract base classes implement most functionality in terms of
a few non-implemented methods. The concrete base classes supply only these
non-implemented methods. They may also supply new implementations of the
convenience methods, for example if there are faster algorithms available.
'''
from copy import copy
from functools import reduce
from sympy.polys.agca.ideals import Ideal
from sympy.polys.domains.field import Field
from sympy.polys.orderings import ProductOrder, monomial_key
from sympy.polys.polyclasses import DMP
from sympy.polys.polyerrors import CoercionFailed
from sympy.core.basic import _aresame
from sympy.utilities.iterables import iterable

class Module:
    '''
    Abstract base class for modules.

    Do not instantiate - use ring explicit constructors instead:

    >>> from sympy import QQ
    >>> from sympy.abc import x
    >>> QQ.old_poly_ring(x).free_module(2)
    QQ[x]**2

    Attributes:

    - dtype - type of elements
    - ring - containing ring

    Non-implemented methods:

    - submodule
    - quotient_module
    - is_zero
    - is_submodule
    - multiply_ideal

    The method convert likely needs to be changed in subclasses.
    '''
    
    def __init__(self, ring):
        self.ring = ring

    
    def convert(self, elem, M = (None,)):
        '''
        Convert ``elem`` into internal representation of this module.

        If ``M`` is not None, it should be a module containing it.
        '''
        if not isinstance(elem, self.dtype):
            raise CoercionFailed
        return elem

    
    def submodule(self, *gens):
        '''Generate a submodule.'''
        raise NotImplementedError

    
    def quotient_module(self, other):
        '''Generate a quotient module.'''
        raise NotImplementedError

    
    def __truediv__(self, e):
        pass
    # WARNING: Decompyle incomplete

    
    def contains(self, elem):
        '''Return True if ``elem`` is an element of this module.'''
        
        try:
            self.convert(elem)
            return True
        except CoercionFailed:
            return False


    
    def __contains__(self, elem):
        return self.contains(elem)

    
    def subset(self, other):
        '''
        Returns True if ``other`` is is a subset of ``self``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> F.subset([(1, x), (x, 2)])
        True
        >>> F.subset([(1/x, x), (x, 2)])
        False
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
