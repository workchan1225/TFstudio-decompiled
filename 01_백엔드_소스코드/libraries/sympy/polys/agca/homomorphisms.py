# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: homomorphisms.pyc (Python 3.11)

'''
Computations with homomorphisms of modules and rings.

This module implements classes for representing homomorphisms of rings and
their modules. Instead of instantiating the classes directly, you should use
the function ``homomorphism(from, to, matrix)`` to create homomorphism objects.
'''
from sympy.polys.agca.modules import Module, FreeModule, QuotientModule, SubModule, SubQuotientModule
from sympy.polys.polyerrors import CoercionFailed

class ModuleHomomorphism:
    '''
    Abstract base class for module homomoprhisms. Do not instantiate.

    Instead, use the ``homomorphism`` function:

    >>> from sympy import QQ
    >>> from sympy.abc import x
    >>> from sympy.polys.agca import homomorphism

    >>> F = QQ.old_poly_ring(x).free_module(2)
    >>> homomorphism(F, F, [[1, 0], [0, 1]])
    Matrix([
    [1, 0], : QQ[x]**2 -> QQ[x]**2
    [0, 1]])

    Attributes:

    - ring - the ring over which we are considering modules
    - domain - the domain module
    - codomain - the codomain module
    - _ker - cached kernel
    - _img - cached image

    Non-implemented methods:

    - _kernel
    - _image
    - _restrict_domain
    - _restrict_codomain
    - _quotient_domain
    - _quotient_codomain
    - _apply
    - _mul_scalar
    - _compose
    - _add
    '''
    
    def __init__(self, domain, codomain):
        if not isinstance(domain, Module):
            raise TypeError('Source must be a module, got %s' % domain)
        if not isinstance(codomain, Module):
            raise TypeError('Target must be a module, got %s' % codomain)
        if domain.ring != codomain.ring:
            raise ValueError(f'''Source and codomain must be over same ring, got {domain!s} != {codomain!s}''')
        self.domain = domain
        self.codomain = codomain
        self.ring = domain.ring
        self._ker = None
        self._img = None

    
    def kernel(self):
        '''
        Compute the kernel of ``self``.

        That is, if ``self`` is the homomorphism `\\phi: M \\to N`, then compute
        `ker(\\phi) = \\{x \\in M | \\phi(x) = 0\\}`.  This is a submodule of `M`.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> homomorphism(F, F, [[1, 0], [x, 0]]).kernel()
        <[x, -1]>
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def image(self):
        '''
        Compute the image of ``self``.

        That is, if ``self`` is the homomorphism `\\phi: M \\to N`, then compute
        `im(\\phi) = \\{\\phi(x) | x \\in M \\}`.  This is a submodule of `N`.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> homomorphism(F, F, [[1, 0], [x, 0]]).image() == F.submodule([1, 0])
        True
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _kernel(self):
        '''Compute the kernel of ``self``.'''
        raise NotImplementedError

    
    def _image(self):
        '''Compute the image of ``self``.'''
        raise NotImplementedError

    
    def _restrict_domain(self, sm):
        '''Implementation of domain restriction.'''
        raise NotImplementedError

    
    def _restrict_codomain(self, sm):
        '''Implementation of codomain restriction.'''
        raise NotImplementedError

    
    def _quotient_domain(self, sm):
        '''Implementation of domain quotient.'''
        raise NotImplementedError

    
    def _quotient_codomain(self, sm):
        '''Implementation of codomain quotient.'''
        raise NotImplementedError

    
    def restrict_domain(self, sm):
        '''
        Return ``self``, with the domain restricted to ``sm``.

        Here ``sm`` has to be a submodule of ``self.domain``.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2
        [0, 0]])
        >>> h.restrict_domain(F.submodule([1, 0]))
        Matrix([
        [1, x], : <[1, 0]> -> QQ[x]**2
        [0, 0]])

        This is the same as just composing on the right with the submodule
        inclusion:

        >>> h * F.submodule([1, 0]).inclusion_hom()
        Matrix([
        [1, x], : <[1, 0]> -> QQ[x]**2
        [0, 0]])
        '''
        if not self.domain.is_submodule(sm):
            raise ValueError(f'''sm must be a submodule of {self.domain!s}, got {sm!s}''')
        if sm == self.domain:
            return self
        return None._restrict_domain(sm)

    
    def restrict_codomain(self, sm):
        '''
        Return ``self``, with codomain restricted to to ``sm``.

        Here ``sm`` has to be a submodule of ``self.codomain`` containing the
        image.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2
        [0, 0]])
        >>> h.restrict_codomain(F.submodule([1, 0]))
        Matrix([
        [1, x], : QQ[x]**2 -> <[1, 0]>
        [0, 0]])
        '''
        if not sm.is_submodule(self.image()):
            raise ValueError(f'''the image {self.image()!s} must contain sm, got {sm!s}''')
        if sm == self.codomain:
            return self
        return None._restrict_codomain(sm)

    
    def quotient_domain(self, sm):
        '''
        Return ``self`` with domain replaced by ``domain/sm``.

        Here ``sm`` must be a submodule of ``self.kernel()``.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2
        [0, 0]])
        >>> h.quotient_domain(F.submodule([-x, 1]))
        Matrix([
        [1, x], : QQ[x]**2/<[-x, 1]> -> QQ[x]**2
        [0, 0]])
        '''
        if not self.kernel().is_submodule(sm):
            raise ValueError(f'''kernel {self.kernel()!s} must contain sm, got {sm!s}''')
        if sm.is_zero():
            return self
        return None._quotient_domain(sm)

    
    def quotient_codomain(self, sm):
        '''
        Return ``self`` with codomain replaced by ``codomain/sm``.

        Here ``sm`` must be a submodule of ``self.codomain``.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2
        [0, 0]])
        >>> h.quotient_codomain(F.submodule([1, 1]))
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2/<[1, 1]>
        [0, 0]])

        This is the same as composing with the quotient map on the left:

        >>> (F/[(1, 1)]).quotient_hom() * h
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2/<[1, 1]>
        [0, 0]])
        '''
        if not self.codomain.is_submodule(sm):
            raise ValueError(f'''sm must be a submodule of codomain {self.codomain!s}, got {sm!s}''')
        if sm.is_zero():
            return self
        return None._quotient_codomain(sm)

    
    def _apply(self, elem):
        '''Apply ``self`` to ``elem``.'''
        raise NotImplementedError

    
    def __call__(self, elem):
        return self.codomain.convert(self._apply(self.domain.convert(elem)))

    
    def _compose(self, oth):
        '''
        Compose ``self`` with ``oth``, that is, return the homomorphism
        obtained by first applying then ``self``, then ``oth``.

        (This method is private since in this syntax, it is non-obvious which
        homomorphism is executed first.)
        '''
        raise NotImplementedError

    
    def _mul_scalar(self, c):
        '''Scalar multiplication. ``c`` is guaranteed in self.ring.'''
        raise NotImplementedError

    
    def _add(self, oth):
        '''
        Homomorphism addition.
        ``oth`` is guaranteed to be a homomorphism with same domain/codomain.
        '''
        raise NotImplementedError

    
    def _check_hom(self, oth):
