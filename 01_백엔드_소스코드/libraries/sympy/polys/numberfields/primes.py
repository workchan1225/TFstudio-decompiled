# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: primes.pyc (Python 3.11)

'''Prime ideals in number fields. '''
from sympy.polys.polytools import Poly
from sympy.polys.domains.finitefield import FF
from sympy.polys.domains.rationalfield import QQ
from sympy.polys.domains.integerring import ZZ
from sympy.polys.matrices.domainmatrix import DomainMatrix
from sympy.polys.polyerrors import CoercionFailed
from sympy.polys.polyutils import IntegerPowerable
from sympy.utilities.decorator import public
from basis import round_two, nilradical_mod_p
from exceptions import StructureError
from modules import ModuleEndomorphism, find_min_poly
from utilities import coeff_search, supplement_a_subspace

def _check_formal_conditions_for_maximal_order(submodule):
    '''
    Several functions in this module accept an argument which is to be a
    :py:class:`~.Submodule` representing the maximal order in a number field,
    such as returned by the :py:func:`~sympy.polys.numberfields.basis.round_two`
    algorithm.

    We do not attempt to check that the given ``Submodule`` actually represents
    a maximal order, but we do check a basic set of formal conditions that the
    ``Submodule`` must satisfy, at a minimum. The purpose is to catch an
    obviously ill-formed argument.
    '''
    prefix = 'The submodule representing the maximal order should '
    cond = None
    if not submodule.is_power_basis_submodule():
        cond = 'be a direct submodule of a power basis.'
    elif not submodule.starts_with_unity():
        cond = 'have 1 as its first generator.'
    elif not submodule.is_sq_maxrank_HNF():
        cond = 'have square matrix, of maximal rank, in Hermite Normal Form.'
# WARNING: Decompyle incomplete


class PrimeIdeal(IntegerPowerable):
    '''
    A prime ideal in a ring of algebraic integers.
    '''
    
    def __init__(self, ZK, p, alpha, f, e = (None,)):
        '''
        Parameters
        ==========

        ZK : :py:class:`~.Submodule`
            The maximal order where this ideal lives.
        p : int
            The rational prime this ideal divides.
        alpha : :py:class:`~.PowerBasisElement`
            Such that the ideal is equal to ``p*ZK + alpha*ZK``.
        f : int
            The inertia degree.
        e : int, ``None``, optional
            The ramification index, if already known. If ``None``, we will
            compute it here.

        '''
        _check_formal_conditions_for_maximal_order(ZK)
        self.ZK = ZK
        self.p = p
        self.alpha = alpha
        self.f = f
        self._test_factor = None
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        if self.is_inert:
            return f'''({self.p})'''
        return f'''{self.p}, {self.alpha.as_expr()})'''

    is_inert = (lambda self: self.f == self.ZK.n)()
    
    def repr(self, field_gen, just_gens = (None, False)):
        '''
        Print a representation of this prime ideal.

        Examples
        ========

        >>> from sympy import cyclotomic_poly, QQ
        >>> from sympy.abc import x, zeta
        >>> T = cyclotomic_poly(7, x)
        >>> K = QQ.algebraic_field((T, zeta))
        >>> P = K.primes_above(11)
        >>> print(P[0].repr())
        [ (11, x**3 + 5*x**2 + 4*x - 1) e=1, f=3 ]
        >>> print(P[0].repr(field_gen=zeta))
        [ (11, zeta**3 + 5*zeta**2 + 4*zeta - 1) e=1, f=3 ]
        >>> print(P[0].repr(field_gen=zeta, just_gens=True))
        (11, zeta**3 + 5*zeta**2 + 4*zeta - 1)

        Parameters
        ==========

        field_gen : :py:class:`~.Symbol`, ``None``, optional (default=None)
            The symbol to use for the generator of the field. This will appear
            in our representation of ``self.alpha``. If ``None``, we use the
            variable of the defining polynomial of ``self.ZK``.
        just_gens : bool, optional (default=False)
            If ``True``, just print the "(p, alpha)" part, showing "just the
            generators" of the prime ideal. Otherwise, print a string of the
            form "[ (p, alpha) e=..., f=... ]", giving the ramification index
            and inertia degree, along with the generators.

        '''
        if not field_gen:
            pass
        field_gen = self.ZK.parent.T.gen
        (p, alpha, e, f) = (self.p, self.alpha, self.e, self.f)
        alpha_rep = str(alpha.numerator(x = field_gen).as_expr())
        if alpha.denom > 1:
            alpha_rep = f'''({alpha_rep})/{alpha.denom}'''
        gens = f'''({p}, {alpha_rep})'''
        if just_gens:
            return gens
        return f'''{gens} e={e}, f={f} ]'''

    
    def __repr__(self):
        return self.repr()

    
    def as_submodule(self):
        '''
        Represent this prime ideal as a :py:class:`~.Submodule`.

        Explanation
        ===========

        The :py:class:`~.PrimeIdeal` class serves to bundle information about
        a prime ideal, such as its inertia degree, ramification index, and
        two-generator representation, as well as to offer helpful methods like
        :py:meth:`~.PrimeIdeal.valuation` and
        :py:meth:`~.PrimeIdeal.test_factor`.

        However, in order to be added and multiplied by other ideals or
        rational numbers, it must first be converted into a
        :py:class:`~.Submodule`, which is a class that supports these
        operations.

        In many cases, the user need not perform this conversion deliberately,
        since it is automatically performed by the arithmetic operator methods
        :py:meth:`~.PrimeIdeal.__add__` and :py:meth:`~.PrimeIdeal.__mul__`.

        Raising a :py:class:`~.PrimeIdeal` to a non-negative integer power is
        also supported.

        Examples
        ========

        >>> from sympy import Poly, cyclotomic_poly, prime_decomp
        >>> T = Poly(cyclotomic_poly(7))
        >>> P0 = prime_decomp(7, T)[0]
        >>> print(P0**6 == 7*P0.ZK)
        True

        Note that, on both sides of the equation above, we had a
        :py:class:`~.Submodule`. In the next equation we recall that adding
        ideals yields their GCD. This time, we need a deliberate conversion
        to :py:class:`~.Submodule` on the right:

        >>> print(P0 + 7*P0.ZK == P0.as_submodule())
        True

        Returns
        =======

        :py:class:`~.Submodule`
            Will be equal to ``self.p * self.ZK + self.alpha * self.ZK``.

        See Also
        ========

        __add__
        __mul__

        '''
        M = self.p * self.ZK + self.alpha * self.ZK
        M._starts_with_unity = False
        M._is_sq_maxrank_HNF = True
        return M

    
    def __eq__(self, other):
        if isinstance(other, PrimeIdeal):
            return self.as_submodule() == other.as_submodule()

    
    def __add__(self, other):
        '''
        Convert to a :py:class:`~.Submodule` and add to another
        :py:class:`~.Submodule`.

        See Also
        ========

        as_submodule

        '''
        return self.as_submodule() + other

    __radd__ = __add__
    
    def __mul__(self, other):
        '''
        Convert to a :py:class:`~.Submodule` and multiply by another
        :py:class:`~.Submodule` or a rational number.

        See Also
        ========

        as_submodule

        '''
        return self.as_submodule() * other

    __rmul__ = __mul__
    
    def _zeroth_power(self):
        return self.ZK

    
    def _first_power(self):
        return self

    
    def test_factor(self):
        '''
        Compute a test factor for this prime ideal.

        Explanation
        ===========

        Write $\\mathfrak{p}$ for this prime ideal, $p$ for the rational prime
        it divides. Then, for computing $\\mathfrak{p}$-adic valuations it is
        useful to have a number $\\beta \\in \\mathbb{Z}_K$ such that
        $p/\\mathfrak{p} = p \\mathbb{Z}_K + \\beta \\mathbb{Z}_K$.

        Essentially, this is the same as the number $\\Psi$ (or the "reagent")
        from Kummer\'s 1847 paper (*Ueber die Zerlegung...*, Crelle vol. 35) in
        which ideal divisors were invented.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def valuation(self, I):
        '''
        Compute the $\\mathfrak{p}$-adic valuation of integral ideal I at this
        prime ideal.

        Parameters
        ==========

        I : :py:class:`~.Submodule`

        See Also
        ========

        prime_valuation

        '''
        return prime_valuation(I, self)

    
    def reduce_element(self, elt):
        '''
        Reduce a :py:class:`~.PowerBasisElement` to a "small representative"
        modulo this prime ideal.

        Parameters
        ==========

        elt : :py:class:`~.PowerBasisElement`
            The element to be reduced.

        Returns
        =======

        :py:class:`~.PowerBasisElement`
            The reduced element.

        See Also
        ========

        reduce_ANP
        reduce_alg_num
        .Submodule.reduce_element

        '''
        return self.as_submodule().reduce_element(elt)

    
    def reduce_ANP(self, a):
        '''
        Reduce an :py:class:`~.ANP` to a "small representative" modulo this
        prime ideal.

        Parameters
        ==========

        elt : :py:class:`~.ANP`
            The element to be reduced.

        Returns
        =======

        :py:class:`~.ANP`
            The reduced element.

        See Also
        ========

        reduce_element
        reduce_alg_num
        .Submodule.reduce_element

        '''
        elt = self.ZK.parent.element_from_ANP(a)
        red = self.reduce_element(elt)
        return red.to_ANP()

    
    def reduce_alg_num(self, a):
        '''
        Reduce an :py:class:`~.AlgebraicNumber` to a "small representative"
        modulo this prime ideal.

        Parameters
        ==========

        elt : :py:class:`~.AlgebraicNumber`
            The element to be reduced.

        Returns
        =======

        :py:class:`~.AlgebraicNumber`
            The reduced element.

        See Also
        ========

        reduce_element
        reduce_ANP
        .Submodule.reduce_element

        '''
        elt = self.ZK.parent.element_from_alg_num(a)
        red = self.reduce_element(elt)
        return a.field_element(list(reversed(red.QQ_col.flat())))



def _compute_test_factor(p, gens, ZK):
    '''
    Compute the test factor for a :py:class:`~.PrimeIdeal` $\\mathfrak{p}$.

    Parameters
    ==========

    p : int
        The rational prime $\\mathfrak{p}$ divides

    gens : list of :py:class:`PowerBasisElement`
        A complete set of generators for $\\mathfrak{p}$ over *ZK*, EXCEPT that
        an element equivalent to rational *p* can and should be omitted (since
        it has no effect except to waste time).

    ZK : :py:class:`~.Submodule`
        The maximal order where the prime ideal $\\mathfrak{p}$ lives.

    Returns
    =======

    :py:class:`~.PowerBasisElement`

    References
    ==========

    .. [1] Cohen, H. *A Course in Computational Algebraic Number Theory.*
    (See Proposition 4.8.15.)

    '''
    pass
# WARNING: Decompyle incomplete

prime_valuation = (lambda I, P:
