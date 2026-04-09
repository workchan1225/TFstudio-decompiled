# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: modules.pyc (Python 3.11)

'''Modules in number fields.

The classes defined here allow us to work with finitely generated, free
modules, whose generators are algebraic numbers.

There is an abstract base class called :py:class:`~.Module`, which has two
concrete subclasses, :py:class:`~.PowerBasis` and :py:class:`~.Submodule`.

Every module is defined by its basis, or set of generators:

* For a :py:class:`~.PowerBasis`, the generators are the first $n$ powers
  (starting with the zeroth) of an algebraic integer $\\theta$ of degree $n$.
  The :py:class:`~.PowerBasis` is constructed by passing either the minimal
  polynomial of $\\theta$, or an :py:class:`~.AlgebraicField` having $\\theta$
  as its primitive element.

* For a :py:class:`~.Submodule`, the generators are a set of
  $\\mathbb{Q}$-linear combinations of the generators of another module. That
  other module is then the "parent" of the :py:class:`~.Submodule`. The
  coefficients of the $\\mathbb{Q}$-linear combinations may be given by an
  integer matrix, and a positive integer denominator. Each column of the matrix
  defines a generator.

>>> from sympy.polys import Poly, cyclotomic_poly, ZZ
>>> from sympy.abc import x
>>> from sympy.polys.matrices import DomainMatrix, DM
>>> from sympy.polys.numberfields.modules import PowerBasis
>>> T = Poly(cyclotomic_poly(5, x))
>>> A = PowerBasis(T)
>>> print(A)
PowerBasis(x**4 + x**3 + x**2 + x + 1)
>>> B = A.submodule_from_matrix(2 * DomainMatrix.eye(4, ZZ), denom=3)
>>> print(B)
Submodule[[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]/3
>>> print(B.parent)
PowerBasis(x**4 + x**3 + x**2 + x + 1)

Thus, every module is either a :py:class:`~.PowerBasis`,
or a :py:class:`~.Submodule`, some ancestor of which is a
:py:class:`~.PowerBasis`. (If ``S`` is a :py:class:`~.Submodule`, then its
ancestors are ``S.parent``, ``S.parent.parent``, and so on).

The :py:class:`~.ModuleElement` class represents a linear combination of the
generators of any module. Critically, the coefficients of this linear
combination are not restricted to be integers, but may be any rational
numbers. This is necessary so that any and all algebraic integers be
representable, starting from the power basis in a primitive element $\\theta$
for the number field in question. For example, in a quadratic field
$\\mathbb{Q}(\\sqrt{d})$ where $d \\equiv 1 \\mod{4}$, a denominator of $2$ is
needed.

A :py:class:`~.ModuleElement` can be constructed from an integer column vector
and a denominator:

>>> U = Poly(x**2 - 5)
>>> M = PowerBasis(U)
>>> e = M(DM([[1], [1]], ZZ), denom=2)
>>> print(e)
[1, 1]/2
>>> print(e.module)
PowerBasis(x**2 - 5)

The :py:class:`~.PowerBasisElement` class is a subclass of
:py:class:`~.ModuleElement` that represents elements of a
:py:class:`~.PowerBasis`, and adds functionality pertinent to elements
represented directly over powers of the primitive element $\\theta$.


Arithmetic with module elements
===============================

While a :py:class:`~.ModuleElement` represents a linear combination over the
generators of a particular module, recall that every module is either a
:py:class:`~.PowerBasis` or a descendant (along a chain of
:py:class:`~.Submodule` objects) thereof, so that in fact every
:py:class:`~.ModuleElement` represents an algebraic number in some field
$\\mathbb{Q}(\\theta)$, where $\\theta$ is the defining element of some
:py:class:`~.PowerBasis`. It thus makes sense to talk about the number field
to which a given :py:class:`~.ModuleElement` belongs.

This means that any two :py:class:`~.ModuleElement` instances can be added,
subtracted, multiplied, or divided, provided they belong to the same number
field. Similarly, since $\\mathbb{Q}$ is a subfield of every number field,
any :py:class:`~.ModuleElement` may be added, multiplied, etc. by any
rational number.

>>> from sympy import QQ
>>> from sympy.polys.numberfields.modules import to_col
>>> T = Poly(cyclotomic_poly(5))
>>> A = PowerBasis(T)
>>> C = A.submodule_from_matrix(3 * DomainMatrix.eye(4, ZZ))
>>> e = A(to_col([0, 2, 0, 0]), denom=3)
>>> f = A(to_col([0, 0, 0, 7]), denom=5)
>>> g = C(to_col([1, 1, 1, 1]))
>>> e + f
[0, 10, 0, 21]/15
>>> e - f
[0, 10, 0, -21]/15
>>> e - g
[-9, -7, -9, -9]/3
>>> e + QQ(7, 10)
[21, 20, 0, 0]/30
>>> e * f
[-14, -14, -14, -14]/15
>>> e ** 2
[0, 0, 4, 0]/9
>>> f // g
[7, 7, 7, 7]/15
>>> f * QQ(2, 3)
[0, 0, 0, 14]/15

However, care must be taken with arithmetic operations on
:py:class:`~.ModuleElement`, because the module $C$ to which the result will
belong will be the nearest common ancestor (NCA) of the modules $A$, $B$ to
which the two operands belong, and $C$ may be different from either or both
of $A$ and $B$.

>>> A = PowerBasis(T)
>>> B = A.submodule_from_matrix(2 * DomainMatrix.eye(4, ZZ))
>>> C = A.submodule_from_matrix(3 * DomainMatrix.eye(4, ZZ))
>>> print((B(0) * C(0)).module == A)
True

Before the arithmetic operation is performed, copies of the two operands are
automatically converted into elements of the NCA (the operands themselves are
not modified). This upward conversion along an ancestor chain is easy: it just
requires the successive multiplication by the defining matrix of each
:py:class:`~.Submodule`.

Conversely, downward conversion, i.e. representing a given
:py:class:`~.ModuleElement` in a submodule, is also supported -- namely by
the :py:meth:`~sympy.polys.numberfields.modules.Submodule.represent` method
-- but is not guaranteed to succeed in general, since the given element may
not belong to the submodule. The main circumstance in which this issue tends
to arise is with multiplication, since modules, while closed under addition,
need not be closed under multiplication.


Multiplication
--------------

Generally speaking, a module need not be closed under multiplication, i.e. need
not form a ring. However, many of the modules we work with in the context of
number fields are in fact rings, and our classes do support multiplication.

Specifically, any :py:class:`~.Module` can attempt to compute its own
multiplication table, but this does not happen unless an attempt is made to
multiply two :py:class:`~.ModuleElement` instances belonging to it.

>>> A = PowerBasis(T)
>>> print(A._mult_tab is None)
True
>>> a = A(0)*A(1)
>>> print(A._mult_tab is None)
False

Every :py:class:`~.PowerBasis` is, by its nature, closed under multiplication,
so instances of :py:class:`~.PowerBasis` can always successfully compute their
multiplication table.

When a :py:class:`~.Submodule` attempts to compute its multiplication table,
it converts each of its own generators into elements of its parent module,
multiplies them there, in every possible pairing, and then tries to
represent the results in itself, i.e. as $\\mathbb{Z}$-linear combinations
over its own generators. This will succeed if and only if the submodule is
in fact closed under multiplication.


Module Homomorphisms
====================

Many important number theoretic algorithms require the calculation of the
kernel of one or more module homomorphisms. Accordingly we have several
lightweight classes, :py:class:`~.ModuleHomomorphism`,
:py:class:`~.ModuleEndomorphism`, :py:class:`~.InnerEndomorphism`, and
:py:class:`~.EndomorphismRing`, which provide the minimal necessary machinery
to support this.

'''
from sympy.core.intfunc import igcd, ilcm
from sympy.core.symbol import Dummy
from sympy.polys.polyclasses import ANP
from sympy.polys.polytools import Poly
from sympy.polys.densetools import dup_clear_denoms
from sympy.polys.domains.algebraicfield import AlgebraicField
from sympy.polys.domains.finitefield import FF
from sympy.polys.domains.rationalfield import QQ
from sympy.polys.domains.integerring import ZZ
from sympy.polys.matrices.domainmatrix import DomainMatrix
from sympy.polys.matrices.exceptions import DMBadInputError
from sympy.polys.matrices.normalforms import hermite_normal_form
from sympy.polys.polyerrors import CoercionFailed, UnificationFailed
from sympy.polys.polyutils import IntegerPowerable
from exceptions import ClosureFailure, MissingUnityError, StructureError
from utilities import AlgIntPowers, is_rat, get_num_denom

def to_col(coeffs):
    '''Transform a list of integer coefficients into a column vector.'''
    return (lambda .0: [ ZZ(c) for c in .0 ])([
        coeffs()], (1, len(coeffs)), ZZ).transpose()


class Module:
    '''
    Generic finitely-generated module.

    This is an abstract base class, and should not be instantiated directly.
    The two concrete subclasses are :py:class:`~.PowerBasis` and
    :py:class:`~.Submodule`.

    Every :py:class:`~.Submodule` is derived from another module, referenced
    by its ``parent`` attribute. If ``S`` is a submodule, then we refer to
    ``S.parent``, ``S.parent.parent``, and so on, as the "ancestors" of
    ``S``. Thus, every :py:class:`~.Module` is either a
    :py:class:`~.PowerBasis` or a :py:class:`~.Submodule`, some ancestor of
    which is a :py:class:`~.PowerBasis`.
    '''
    n = (lambda self: raise NotImplementedError)()
    
    def mult_tab(self):
        '''
        Get the multiplication table for this module (if closed under mult).

        Explanation
        ===========

        Computes a dictionary ``M`` of dictionaries of lists, representing the
        upper triangular half of the multiplication table.

        In other words, if ``0 <= i <= j < self.n``, then ``M[i][j]`` is the
        list ``c`` of coefficients such that
        ``g[i] * g[j] == sum(c[k]*g[k], k in range(self.n))``,
        where ``g`` is the list of generators of this module.

        If ``j < i`` then ``M[i][j]`` is undefined.

        Examples
        ========

        >>> from sympy.polys import Poly, cyclotomic_poly
        >>> from sympy.polys.numberfields.modules import PowerBasis
        >>> T = Poly(cyclotomic_poly(5))
        >>> A = PowerBasis(T)
        >>> print(A.mult_tab())  # doctest: +SKIP
        {0: {0: [1, 0, 0, 0], 1: [0, 1, 0, 0], 2: [0, 0, 1, 0],     3: [0, 0, 0, 1]},
                          1: {1: [0, 0, 1, 0], 2: [0, 0, 0, 1],     3: [-1, -1, -1, -1]},
                                           2: {2: [-1, -1, -1, -1], 3: [1, 0, 0, 0]},
                                                                3: {3: [0, 1, 0, 0]}}

        Returns
        =======

        dict of dict of lists

        Raises
        ======

        ClosureFailure
            If the module is not closed under multiplication.

        '''
        raise NotImplementedError

    parent = (lambda self: pass)()
    
    def represent(self, elt):
        '''
        Represent a module element as an integer-linear combination over the
        generators of this module.

        Explanation
        ===========

        In our system, to "represent" always means to write a
        :py:class:`~.ModuleElement` as a :ref:`ZZ`-linear combination over the
        generators of the present :py:class:`~.Module`. Furthermore, the
        incoming :py:class:`~.ModuleElement` must belong to an ancestor of
        the present :py:class:`~.Module` (or to the present
        :py:class:`~.Module` itself).

        The most common application is to represent a
        :py:class:`~.ModuleElement` in a :py:class:`~.Submodule`. For example,
        this is involved in computing multiplication tables.

        On the other hand, representing in a :py:class:`~.PowerBasis` is an
        odd case, and one which tends not to arise in practice, except for
        example when using a :py:class:`~.ModuleEndomorphism` on a
        :py:class:`~.PowerBasis`.

        In such a case, (1) the incoming :py:class:`~.ModuleElement` must
        belong to the :py:class:`~.PowerBasis` itself (since the latter has no
        proper ancestors) and (2) it is "representable" iff it belongs to
        $\\mathbb{Z}[\\theta]$ (although generally a
        :py:class:`~.PowerBasisElement` may represent any element of
        $\\mathbb{Q}(\\theta)$, i.e. any algebraic number).

        Examples
        ========

        >>> from sympy import Poly, cyclotomic_poly
        >>> from sympy.polys.numberfields.modules import PowerBasis, to_col
        >>> from sympy.abc import zeta
        >>> T = Poly(cyclotomic_poly(5))
        >>> A = PowerBasis(T)
        >>> a = A(to_col([2, 4, 6, 8]))

        The :py:class:`~.ModuleElement` ``a`` has all even coefficients.
        If we represent ``a`` in the submodule ``B = 2*A``, the coefficients in
        the column vector will be halved:

        >>> B = A.submodule_from_gens([2*A(i) for i in range(4)])
        >>> b = B.represent(a)
        >>> print(b.transpose())  # doctest: +SKIP
        DomainMatrix([[1, 2, 3, 4]], (1, 4), ZZ)

        However, the element of ``B`` so defined still represents the same
        algebraic number:

        >>> print(a.poly(zeta).as_expr())
        8*zeta**3 + 6*zeta**2 + 4*zeta + 2
        >>> print(B(b).over_power_basis().poly(zeta).as_expr())
        8*zeta**3 + 6*zeta**2 + 4*zeta + 2

        Parameters
        ==========

        elt : :py:class:`~.ModuleElement`
            The module element to be represented. Must belong to some ancestor
            module of this module (including this module itself).

        Returns
        =======

        :py:class:`~.DomainMatrix` over :ref:`ZZ`
            This will be a column vector, representing the coefficients of a
            linear combination of this module\'s generators, which equals the
            given element.

        Raises
        ======

        ClosureFailure
            If the given element cannot be represented as a :ref:`ZZ`-linear
            combination over this module.

        See Also
        ========

        .Submodule.represent
        .PowerBasis.represent

        '''
        raise NotImplementedError

    
    def ancestors(self, include_self = (False,)):
        '''
        Return the list of ancestor modules of this module, from the
        foundational :py:class:`~.PowerBasis` downward, optionally including
        ``self``.

        See Also
        ========

        Module

        '''
        c = self.parent
    # WARNING: Decompyle incomplete

    
    def power_basis_ancestor(self):
        '''
        Return the :py:class:`~.PowerBasis` that is an ancestor of this module.

        See Also
        ========

        Module

        '''
        if isinstance(self, PowerBasis):
            return self
        c = None.parent
    # WARNING: Decompyle incomplete

    
    def nearest_common_ancestor(self, other):
        '''
        Locate the nearest common ancestor of this module and another.

        Returns
        =======

        :py:class:`~.Module`, ``None``

        See Also
        ========

        Module

        '''
        sA = self.ancestors(include_self = True)
        oA = other.ancestors(include_self = True)
        nca = None
        for sa, oa in zip(sA, oA):
            if sa == oa:
                nca = sa
                continue
            return nca

    number_field = (lambda self: self.power_basis_ancestor().number_field)()
    
    def is_compat_col(self, col):
