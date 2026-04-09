# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polyclasses.pyc (Python 3.11)

'''OO layer for several polynomial representations. '''
from __future__ import annotations
from sympy.external.gmpy import GROUND_TYPES
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.core.numbers import oo
from sympy.core.sympify import CantSympify
from sympy.polys.polyutils import PicklableWithSlots, _sort_factors
from sympy.polys.domains import Domain, ZZ, QQ
from sympy.polys.polyerrors import CoercionFailed, ExactQuotientFailed, DomainError, NotInvertible
from sympy.polys.densebasic import ninf, dmp_validate, dup_normal, dmp_normal, dup_convert, dmp_convert, dmp_from_sympy, dup_strip, dmp_degree_in, dmp_degree_list, dmp_negative_p, dmp_ground_LC, dmp_ground_TC, dmp_ground_nth, dmp_one, dmp_ground, dmp_zero, dmp_zero_p, dmp_one_p, dmp_ground_p, dup_from_dict, dmp_from_dict, dmp_to_dict, dmp_deflate, dmp_inject, dmp_eject, dmp_terms_gcd, dmp_list_terms, dmp_exclude, dup_slice, dmp_slice_in, dmp_permute, dmp_to_tuple
from sympy.polys.densearith import dmp_add_ground, dmp_sub_ground, dmp_mul_ground, dmp_quo_ground, dmp_exquo_ground, dmp_abs, dmp_neg, dmp_add, dmp_sub, dmp_mul, dmp_sqr, dmp_pow, dmp_pdiv, dmp_prem, dmp_pquo, dmp_pexquo, dmp_div, dmp_rem, dmp_quo, dmp_exquo, dmp_add_mul, dmp_sub_mul, dmp_max_norm, dmp_l1_norm, dmp_l2_norm_squared
from sympy.polys.densetools import dmp_clear_denoms, dmp_integrate_in, dmp_diff_in, dmp_eval_in, dup_revert, dmp_ground_trunc, dmp_ground_content, dmp_ground_primitive, dmp_ground_monic, dmp_compose, dup_decompose, dup_shift, dmp_shift, dup_transform, dmp_lift
from sympy.polys.euclidtools import dup_half_gcdex, dup_gcdex, dup_invert, dmp_subresultants, dmp_resultant, dmp_discriminant, dmp_inner_gcd, dmp_gcd, dmp_lcm, dmp_cancel
from sympy.polys.sqfreetools import dup_gff_list, dmp_norm, dmp_sqf_p, dmp_sqf_norm, dmp_sqf_part, dmp_sqf_list, dmp_sqf_list_include
from sympy.polys.factortools import dup_cyclotomic_p, dmp_irreducible_p, dmp_factor_list, dmp_factor_list_include
from sympy.polys.rootisolation import dup_isolate_real_roots_sqf, dup_isolate_real_roots, dup_isolate_all_roots_sqf, dup_isolate_all_roots, dup_refine_real_root, dup_count_real_roots, dup_count_complex_roots, dup_sturm, dup_cauchy_upper_bound, dup_cauchy_lower_bound, dup_mignotte_sep_bound_squared
from sympy.polys.polyerrors import UnificationFailed, PolynomialError
_flint_domains: 'tuple[Domain, ...]'
if GROUND_TYPES == 'flint':
    import flint
    _flint_domains = (ZZ, QQ)
else:
    flint = None
    _flint_domains = ()

class DMP(CantSympify):
    '''Dense Multivariate Polynomials over `K`. '''
    __slots__ = ()
    
    def __new__(cls, rep, dom, lev = (None,)):
        pass
    # WARNING: Decompyle incomplete

    new = (lambda cls, rep, dom, lev: pass# WARNING: Decompyle incomplete
)()
    rep = (lambda f: sympy_deprecation_warning('\n        Accessing the ``DMP.rep`` attribute is deprecated. The internal\n        representation of ``DMP`` instances can now be ``DUP_Flint`` when the\n        ground types are ``flint``. In this case the ``DMP`` instance does not\n        have a ``rep`` attribute. Use ``DMP.to_list()`` instead. Using\n        ``DMP.to_list()`` also works in previous versions of SymPy.\n        ', deprecated_since_version = '1.13', active_deprecations_target = 'dmp-rep')f.to_list())()
    
    def to_best(f):
        '''Convert to DUP_Flint if possible.

        This method should be used when the domain or level is changed and it
        potentially becomes possible to convert from DMP_Python to DUP_Flint.
        '''
        pass
    # WARNING: Decompyle incomplete

    _validate_args = (lambda cls, rep, dom, lev: pass# WARNING: Decompyle incomplete
)()
    from_dict = (lambda cls, rep, lev, dom: rep = dmp_from_dict(rep, lev, dom)cls.new(rep, dom, lev))()
    from_list = (lambda cls, rep, lev, dom: cls.new(dmp_convert(rep, lev, None, dom), dom, lev))()
    from_sympy_list = (lambda cls, rep, lev, dom: cls.new(dmp_from_sympy(rep, lev, dom), dom, lev))()
    from_monoms_coeffs = (lambda cls, monoms, coeffs, lev, dom: cls(dict(list(zip(monoms, coeffs))), dom, lev))()
    
    def convert(f, dom):
        '''Convert ``f`` to a ``DMP`` over the new domain. '''
        if f.dom == dom:
            return f
    # WARNING: Decompyle incomplete

    
    def _convert(f, dom):
        raise NotImplementedError

    zero = (lambda cls, lev, dom: DMP(dmp_zero(lev), dom, lev))()
    one = (lambda cls, lev, dom: DMP(dmp_one(lev, dom), dom, lev))()
    
    def _one(f):
        raise NotImplementedError

    
    def __repr__(f):
        return f'''{f.__class__.__name__!s}({f.to_list()!s}, {f.dom!s})'''

    
    def __hash__(f):
        return hash((f.__class__.__name__, f.to_tuple(), f.lev, f.dom))

    
    def __getnewargs__(self):
        return (self.to_list(), self.dom, self.lev)

    
    def ground_new(f, coeff):
        '''Construct a new ground instance of ``f``. '''
        raise NotImplementedError

    
    def unify_DMP(f, g):
        '''Unify and return ``DMP`` instances of ``f`` and ``g``. '''
        if isinstance(g, DMP) or f.lev != g.lev:
            raise UnificationFailed(f'''Cannot unify {f!s} with {g!s}''')
        if f.dom != g.dom:
            dom = f.dom.unify(g.dom)
            f = f.convert(dom)
            g = g.convert(dom)
        return (f, g)

    
    def to_dict(f, zero = (False,)):
        '''Convert ``f`` to a dict representation with native coefficients. '''
        return dmp_to_dict(f.to_list(), f.lev, f.dom, zero = zero)

    
    def to_sympy_dict(f, zero = (False,)):
        '''Convert ``f`` to a dict representation with SymPy coefficients. '''
        rep = f.to_dict(zero = zero)
        for k, v in rep.items():
            rep[k] = f.dom.to_sympy(v)
            return rep

    
    def to_sympy_list(f):
        '''Convert ``f`` to a list representation with SymPy coefficients. '''
        pass
    # WARNING: Decompyle incomplete

    
    def to_list(f):
        '''Convert ``f`` to a list representation with native coefficients. '''
        raise NotImplementedError

    
    def to_tuple(f):
        '''
        Convert ``f`` to a tuple representation with native coefficients.

        This is needed for hashing.
        '''
        raise NotImplementedError

    
    def to_ring(f):
        '''Make the ground domain a ring. '''
        return f.convert(f.dom.get_ring())

    
    def to_field(f):
        '''Make the ground domain a field. '''
        return f.convert(f.dom.get_field())

    
    def to_exact(f):
        '''Make the ground domain exact. '''
        return f.convert(f.dom.get_exact())

    
    def slice(f, m, n, j = (0,)):
        '''Take a continuous subsequence of terms of ``f``. '''
        if not f.lev and j:
            return f._slice(m, n)
        return None._slice_lev(m, n, j)

    
    def _slice(f, m, n):
        raise NotImplementedError

    
    def _slice_lev(f, m, n, j):
        raise NotImplementedError

    
    def coeffs(f, order = (None,)):
        '''Returns all non-zero coefficients from ``f`` in lex order. '''
        return f.terms(order = order)()

    
    def monoms(f, order = (None,)):
        '''Returns all non-zero monomials from ``f`` in lex order. '''
        return f.terms(order = order)()

    
    def terms(f, order = (None,)):
        '''Returns all non-zero terms from ``f`` in lex order. '''
        if f.is_zero:
            zero_monom = (0,) * (f.lev + 1)
            return [
                (zero_monom, f.dom.zero)]
        return None._terms(order = order)

    
    def _terms(f, order = (None,)):
        raise NotImplementedError

    
    def all_coeffs(f):
        '''Returns all coefficients from ``f``. '''
        if f.lev:
            raise PolynomialError('multivariate polynomials not supported')
        if not f:
            return [
                f.dom.zero]
        return None(f.to_list())

    
    def all_monoms(f):
        '''Returns all monomials from ``f``. '''
        pass
    # WARNING: Decompyle incomplete

    
    def all_terms(f):
        '''Returns all terms from a ``f``. '''
        pass
    # WARNING: Decompyle incomplete

    
    def lift(f):
        '''Convert algebraic coefficients to rationals. '''
        return f._lift().to_best()

    
    def _lift(f):
        raise NotImplementedError

    
    def deflate(f):
        '''Reduce degree of `f` by mapping `x_i^m` to `y_i`. '''
        raise NotImplementedError

    
    def inject(f, front = (False,)):
        '''Inject ground domain generators into ``f``. '''
        raise NotImplementedError

    
    def eject(f, dom, front = (False,)):
        '''Eject selected generators into the ground domain. '''
        raise NotImplementedError

    
    def exclude(f):
        '''
        Remove useless generators from ``f``.

        Returns the removed generators and the new excluded ``f``.

        Examples
        ========

        >>> from sympy.polys.polyclasses import DMP
        >>> from sympy.polys.domains import ZZ

        >>> DMP([[[ZZ(1)]], [[ZZ(1)], [ZZ(2)]]], ZZ).exclude()
        ([2], DMP_Python([[1], [1, 2]], ZZ))

        '''
        (J, F) = f._exclude()
        return (J, F.to_best())

    
    def _exclude(f):
        raise NotImplementedError

    
    def permute(f, P):
        '''
        Returns a polynomial in `K[x_{P(1)}, ..., x_{P(n)}]`.

        Examples
        ========

        >>> from sympy.polys.polyclasses import DMP
        >>> from sympy.polys.domains import ZZ

        >>> DMP([[[ZZ(2)], [ZZ(1), ZZ(0)]], [[]]], ZZ).permute([1, 0, 2])
        DMP_Python([[[2], []], [[1, 0], []]], ZZ)

        >>> DMP([[[ZZ(2)], [ZZ(1), ZZ(0)]], [[]]], ZZ).permute([1, 2, 0])
        DMP_Python([[[1], []], [[2, 0], []]], ZZ)

        '''
        return f._permute(P)

    
    def _permute(f, P):
        raise NotImplementedError

    
    def terms_gcd(f):
        '''Remove GCD of terms from the polynomial ``f``. '''
        raise NotImplementedError

    
    def abs(f):
        '''Make all coefficients in ``f`` positive. '''
        raise NotImplementedError

    
    def neg(f):
        '''Negate all coefficients in ``f``. '''
        raise NotImplementedError

    
    def add_ground(f, c):
        '''Add an element of the ground domain to ``f``. '''
        return f._add_ground(f.dom.convert(c))

    
    def sub_ground(f, c):
        '''Subtract an element of the ground domain from ``f``. '''
        return f._sub_ground(f.dom.convert(c))

    
    def mul_ground(f, c):
        '''Multiply ``f`` by a an element of the ground domain. '''
        return f._mul_ground(f.dom.convert(c))

    
    def quo_ground(f, c):
        '''Quotient of ``f`` by a an element of the ground domain. '''
        return f._quo_ground(f.dom.convert(c))

    
    def exquo_ground(f, c):
        '''Exact quotient of ``f`` by a an element of the ground domain. '''
        return f._exquo_ground(f.dom.convert(c))

    
    def add(f, g):
        '''Add two multivariate polynomials ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._add(G)

    
    def sub(f, g):
        '''Subtract two multivariate polynomials ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._sub(G)

    
    def mul(f, g):
        '''Multiply two multivariate polynomials ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._mul(G)

    
    def sqr(f):
        '''Square a multivariate polynomial ``f``. '''
        return f._sqr()

    
    def pow(f, n):
        '''Raise ``f`` to a non-negative power ``n``. '''
        if not isinstance(n, int):
            raise TypeError('``int`` expected, got %s' % type(n))
        return f._pow(n)

    
    def pdiv(f, g):
        '''Polynomial pseudo-division of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._pdiv(G)

    
    def prem(f, g):
        '''Polynomial pseudo-remainder of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._prem(G)

    
    def pquo(f, g):
        '''Polynomial pseudo-quotient of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._pquo(G)

    
    def pexquo(f, g):
        '''Polynomial exact pseudo-quotient of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._pexquo(G)

    
    def div(f, g):
        '''Polynomial division with remainder of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._div(G)

    
    def rem(f, g):
        '''Computes polynomial remainder of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._rem(G)

    
    def quo(f, g):
        '''Computes polynomial quotient of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._quo(G)

    
    def exquo(f, g):
        '''Computes polynomial exact quotient of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._exquo(G)

    
    def _add_ground(f, c):
        raise NotImplementedError

    
    def _sub_ground(f, c):
        raise NotImplementedError

    
    def _mul_ground(f, c):
        raise NotImplementedError

    
    def _quo_ground(f, c):
        raise NotImplementedError

    
    def _exquo_ground(f, c):
        raise NotImplementedError

    
    def _add(f, g):
        raise NotImplementedError

    
    def _sub(f, g):
        raise NotImplementedError

    
    def _mul(f, g):
        raise NotImplementedError

    
    def _sqr(f):
        raise NotImplementedError

    
    def _pow(f, n):
        raise NotImplementedError

    
    def _pdiv(f, g):
        raise NotImplementedError

    
    def _prem(f, g):
        raise NotImplementedError

    
    def _pquo(f, g):
        raise NotImplementedError

    
    def _pexquo(f, g):
        raise NotImplementedError

    
    def _div(f, g):
        raise NotImplementedError

    
    def _rem(f, g):
        raise NotImplementedError

    
    def _quo(f, g):
        raise NotImplementedError

    
    def _exquo(f, g):
        raise NotImplementedError

    
    def degree(f, j = (0,)):
        '''Returns the leading degree of ``f`` in ``x_j``. '''
        if not isinstance(j, int):
            raise TypeError('``int`` expected, got %s' % type(j))
        return f._degree(j)

    
    def _degree(f, j):
        raise NotImplementedError

    
    def degree_list(f):
        '''Returns a list of degrees of ``f``. '''
        raise NotImplementedError

    
    def total_degree(f):
        '''Returns the total degree of ``f``. '''
        raise NotImplementedError

    
    def homogenize(f, s):
        '''Return homogeneous polynomial of ``f``'''
        td = f.total_degree()
        result = { }
        new_symbol = s == len(f.terms()[0][0])
        for term in f.terms():
            d = sum(term[0])
            if d < td:
                i = td - d
            else:
                i = 0
            if new_symbol:
                result[term[0] + (i,)] = term[1]
                continue
            l = list(term[0])
            term[1] = None
            return DMP.from_dict(result, f.lev + int(new_symbol), f.dom)

    
    def homogeneous_order(f):
        '''Returns the homogeneous order of ``f``. '''
        if f.is_zero:
            return -oo
        monoms = None.monoms()
        tdeg = sum(monoms[0])
        for monom in monoms:
            _tdeg = sum(monom)
            if _tdeg != tdeg:
                return None
            return tdeg

    
    def LC(f):
        '''Returns the leading coefficient of ``f``. '''
        raise NotImplementedError

    
    def TC(f):
        '''Returns the trailing coefficient of ``f``. '''
        raise NotImplementedError

    
    def nth(f, *N):
        '''Returns the ``n``-th coefficient of ``f``. '''
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(N()):
            return f._nth(N)
        raise all('a sequence of integers expected')

    
    def _nth(f, N):
        raise NotImplementedError

    
    def max_norm(f):
        '''Returns maximum norm of ``f``. '''
        raise NotImplementedError

    
    def l1_norm(f):
        '''Returns l1 norm of ``f``. '''
        raise NotImplementedError

    
    def l2_norm_squared(f):
        '''Return squared l2 norm of ``f``. '''
        raise NotImplementedError

    
    def clear_denoms(f):
        '''Clear denominators, but keep the ground domain. '''
        raise NotImplementedError

    
    def integrate(f, m, j = (1, 0)):
        '''Computes the ``m``-th order indefinite integral of ``f`` in ``x_j``. '''
        if not isinstance(m, int):
            raise TypeError('``int`` expected, got %s' % type(m))
        if not isinstance(j, int):
            raise TypeError('``int`` expected, got %s' % type(j))
        return f._integrate(m, j)

    
    def _integrate(f, m, j):
        raise NotImplementedError

    
    def diff(f, m, j = (1, 0)):
        '''Computes the ``m``-th order derivative of ``f`` in ``x_j``. '''
        if not isinstance(m, int):
            raise TypeError('``int`` expected, got %s' % type(m))
        if not isinstance(j, int):
            raise TypeError('``int`` expected, got %s' % type(j))
        return f._diff(m, j)

    
    def _diff(f, m, j):
        raise NotImplementedError

    
    def eval(f, a, j = (0,)):
        '''Evaluates ``f`` at the given point ``a`` in ``x_j``. '''
        if not isinstance(j, int):
            raise TypeError('``int`` expected, got %s' % type(j))
        if not  <= 0, j or 0, j <= f.lev:
            pass
        
        raise ValueError('invalid variable index %s' % j)
        if f.lev:
            return f._eval_lev(a, j)
        return None._eval(a)

    
    def _eval(f, a):
        raise NotImplementedError

    
    def _eval_lev(f, a, j):
        raise NotImplementedError

    
    def half_gcdex(f, g):
        '''Half extended Euclidean algorithm, if univariate. '''
        (F, G) = f.unify_DMP(g)
        if F.lev:
            raise ValueError('univariate polynomial expected')
        return F._half_gcdex(G)

    
    def _half_gcdex(f, g):
        raise NotImplementedError

    
    def gcdex(f, g):
        '''Extended Euclidean algorithm, if univariate. '''
        (F, G) = f.unify_DMP(g)
        if F.lev:
            raise ValueError('univariate polynomial expected')
        if not F.dom.is_Field:
            raise DomainError('ground domain must be a field')
        return F._gcdex(G)

    
    def _gcdex(f, g):
        raise NotImplementedError

    
    def invert(f, g):
        '''Invert ``f`` modulo ``g``, if possible. '''
        (F, G) = f.unify_DMP(g)
        if F.lev:
            raise ValueError('univariate polynomial expected')
        return F._invert(G)

    
    def _invert(f, g):
        raise NotImplementedError

    
    def revert(f, n):
        '''Compute ``f**(-1)`` mod ``x**n``. '''
        if f.lev:
            raise ValueError('univariate polynomial expected')
        return f._revert(n)

    
    def _revert(f, n):
        raise NotImplementedError

    
    def subresultants(f, g):
        '''Computes subresultant PRS sequence of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._subresultants(G)

    
    def _subresultants(f, g):
        raise NotImplementedError

    
    def resultant(f, g, includePRS = (False,)):
        '''Computes resultant of ``f`` and ``g`` via PRS. '''
        (F, G) = f.unify_DMP(g)
        if includePRS:
            return F._resultant_includePRS(G)
        return None._resultant(G)

    
    def _resultant(f, g, includePRS = (False,)):
        raise NotImplementedError

    
    def discriminant(f):
        '''Computes discriminant of ``f``. '''
        raise NotImplementedError

    
    def cofactors(f, g):
        '''Returns GCD of ``f`` and ``g`` and their cofactors. '''
        (F, G) = f.unify_DMP(g)
        return F._cofactors(G)

    
    def _cofactors(f, g):
        raise NotImplementedError

    
    def gcd(f, g):
        '''Returns polynomial GCD of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._gcd(G)

    
    def _gcd(f, g):
        raise NotImplementedError

    
    def lcm(f, g):
        '''Returns polynomial LCM of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._lcm(G)

    
    def _lcm(f, g):
        raise NotImplementedError

    
    def cancel(f, g, include = (True,)):
        '''Cancel common factors in a rational function ``f/g``. '''
        (F, G) = f.unify_DMP(g)
        if include:
            return F._cancel_include(G)
        return None._cancel(G)

    
    def _cancel(f, g):
        raise NotImplementedError

    
    def _cancel_include(f, g):
        raise NotImplementedError

    
    def trunc(f, p):
        '''Reduce ``f`` modulo a constant ``p``. '''
        return f._trunc(f.dom.convert(p))

    
    def _trunc(f, p):
        raise NotImplementedError

    
    def monic(f):
        '''Divides all coefficients by ``LC(f)``. '''
        raise NotImplementedError

    
    def content(f):
        '''Returns GCD of polynomial coefficients. '''
        raise NotImplementedError

    
    def primitive(f):
        '''Returns content and a primitive form of ``f``. '''
        raise NotImplementedError

    
    def compose(f, g):
        '''Computes functional composition of ``f`` and ``g``. '''
        (F, G) = f.unify_DMP(g)
        return F._compose(G)

    
    def _compose(f, g):
        raise NotImplementedError

    
    def decompose(f):
        '''Computes functional decomposition of ``f``. '''
        if f.lev:
            raise ValueError('univariate polynomial expected')
        return f._decompose()

    
    def _decompose(f):
        raise NotImplementedError

    
    def shift(f, a):
        '''Efficiently compute Taylor shift ``f(x + a)``. '''
        if f.lev:
            raise ValueError('univariate polynomial expected')
        return f._shift(f.dom.convert(a))

    
    def shift_list(f, a):
        '''Efficiently compute Taylor shift ``f(X + A)``. '''
        pass
    # WARNING: Decompyle incomplete

    
    def _shift(f, a):
        raise NotImplementedError

    
    def transform(f, p, q):
        '''Evaluate functional transformation ``q**n * f(p/q)``.'''
        if f.lev:
            raise ValueError('univariate polynomial expected')
        (P, Q) = p.unify_DMP(q)
        (F, P) = f.unify_DMP(P)
        (F, Q) = F.unify_DMP(Q)
        return F._transform(P, Q)

    
    def _transform(f, p, q):
        raise NotImplementedError

    
    def sturm(f):
        '''Computes the Sturm sequence of ``f``. '''
        if f.lev:
            raise ValueError('univariate polynomial expected')
        return f._sturm()

    
    def _sturm(f):
        raise NotImplementedError

    
    def cauchy_upper_bound(f):
        '''Computes the Cauchy upper bound on the roots of ``f``. '''
        if f.lev:
            raise ValueError('univariate polynomial expected')
        return f._cauchy_upper_bound()

    
    def _cauchy_upper_bound(f):
        raise NotImplementedError

    
    def cauchy_lower_bound(f):
        '''Computes the Cauchy lower bound on the nonzero roots of ``f``. '''
        if f.lev:
            raise ValueError('univariate polynomial expected')
        return f._cauchy_lower_bound()

    
    def _cauchy_lower_bound(f):
        raise NotImplementedError

    
    def mignotte_sep_bound_squared(f):
        '''Computes the squared Mignotte bound on root separations of ``f``. '''
        if f.lev:
            raise ValueError('univariate polynomial expected')
        return f._mignotte_sep_bound_squared()

    
    def _mignotte_sep_bound_squared(f):
        raise NotImplementedError

    
    def gff_list(f):
        '''Computes greatest factorial factorization of ``f``. '''
        if f.lev:
            raise ValueError('univariate polynomial expected')
        return f._gff_list()

    
    def _gff_list(f):
        raise NotImplementedError

    
    def norm(f):
        '''Computes ``Norm(f)``.'''
        raise NotImplementedError

    
    def sqf_norm(f):
        '''Computes square-free norm of ``f``. '''
        raise NotImplementedError

    
    def sqf_part(f):
        '''Computes square-free part of ``f``. '''
        raise NotImplementedError

    
    def sqf_list(f, all = (False,)):
        '''Returns a list of square-free factors of ``f``. '''
        raise NotImplementedError

    
    def sqf_list_include(f, all = (False,)):
        '''Returns a list of square-free factors of ``f``. '''
        raise NotImplementedError

    
    def factor_list(f):
        '''Returns a list of irreducible factors of ``f``. '''
        raise NotImplementedError

    
    def factor_list_include(f):
        '''Returns a list of irreducible factors of ``f``. '''
        raise NotImplementedError

    
    def intervals(f, all, eps, inf, sup, fast, sqf = (False, None, None, None, False, False)):
        '''Compute isolating intervals for roots of ``f``. '''
        if f.lev:
            raise PolynomialError('Cannot isolate roots of a multivariate polynomial')
        if all and sqf:
            return f._isolate_all_roots_sqf(eps = eps, inf = inf, sup = sup, fast = fast)
        if not None and sqf:
            return f._isolate_all_roots(eps = eps, inf = inf, sup = sup, fast = fast)
        if None and sqf:
            return f._isolate_real_roots_sqf(eps = eps, inf = inf, sup = sup, fast = fast)
        return None._isolate_real_roots(eps = eps, inf = inf, sup = sup, fast = fast)

    
    def _isolate_all_roots(f, eps, inf, sup, fast):
        raise NotImplementedError

    
    def _isolate_all_roots_sqf(f, eps, inf, sup, fast):
        raise NotImplementedError

    
    def _isolate_real_roots(f, eps, inf, sup, fast):
        raise NotImplementedError

    
    def _isolate_real_roots_sqf(f, eps, inf, sup, fast):
        raise NotImplementedError

    
    def refine_root(f, s, t, eps, steps, fast = (None, None, False)):
        '''
        Refine an isolating interval to the given precision.

        ``eps`` should be a rational number.

        '''
        if f.lev:
            raise PolynomialError('Cannot refine a root of a multivariate polynomial')
        return f._refine_real_root(s, t, eps = eps, steps = steps, fast = fast)

    
    def _refine_real_root(f, s, t, eps, steps, fast):
        raise NotImplementedError

    
    def count_real_roots(f, inf, sup = (None, None)):
        '''Return the number of real roots of ``f`` in ``[inf, sup]``. '''
        raise NotImplementedError

    
    def count_complex_roots(f, inf, sup = (None, None)):
        '''Return the number of complex roots of ``f`` in ``[inf, sup]``. '''
        raise NotImplementedError

    is_zero = (lambda f: raise NotImplementedError)()
    is_one = (lambda f: raise NotImplementedError)()
    is_ground = (lambda f: raise NotImplementedError)()
    is_sqf = (lambda f: raise NotImplementedError)()
    is_monic = (lambda f: raise NotImplementedError)()
    is_primitive = (lambda f: raise NotImplementedError)()
    is_linear = (lambda f: raise NotImplementedError)()
    is_quadratic = (lambda f: raise NotImplementedError)()
    is_monomial = (lambda f: raise NotImplementedError)()
    is_homogeneous = (lambda f: raise NotImplementedError)()
    is_irreducible = (lambda f: raise NotImplementedError)()
    is_cyclotomic = (lambda f: raise NotImplementedError)()
    
    def __abs__(f):
        return f.abs()

    
    def __neg__(f):
        return f.neg()

    
    def __add__(f, g):
        if isinstance(g, DMP):
            return f.add(g)
        
        try:
            return f.add_ground(g)
        except CoercionFailed:
            return 


    
    def __radd__(f, g):
        return f.__add__(g)

    
    def __sub__(f, g):
        if isinstance(g, DMP):
            return f.sub(g)
        
        try:
            return f.sub_ground(g)
        except CoercionFailed:
            return 


    
    def __rsub__(f, g):
        return -f.__add__(g)

    
    def __mul__(f, g):
        if isinstance(g, DMP):
            return f.mul(g)
        
        try:
            return f.mul_ground(g)
        except CoercionFailed:
            return 


    
    def __rmul__(f, g):
        return f.__mul__(g)

    
    def __truediv__(f, g):
        if isinstance(g, DMP):
            return f.exquo(g)
        
        try:
            return f.mul_ground(g)
        except CoercionFailed:
            return 


    
    def __rtruediv__(f, g):
        if isinstance(g, DMP):
            return g.exquo(f)
        
        try:
            return f._one().mul_ground(g).exquo(f)
        except CoercionFailed:
            return 


    
    def __pow__(f, n):
        return f.pow(n)

    
    def __divmod__(f, g):
        return f.div(g)

    
    def __mod__(f, g):
        return f.rem(g)

    
    def __floordiv__(f, g):
        if isinstance(g, DMP):
            return f.quo(g)
        
        try:
            return f.quo_ground(g)
        except TypeError:
            return 


    
    def __eq__(f, g):
        if f is g:
            return True
        if not None(g, DMP):
            return NotImplemented
        
        try:
            (F, G) = f.unify_DMP(g)
            return F._strict_eq(G)
        except UnificationFailed:
            return False


    
    def _strict_eq(f, g):
        raise NotImplementedError

    
    def eq(f, g, strict = (False,)):
        if not strict:
            return f == g
        return None._strict_eq(g)

    
    def ne(f, g, strict = (False,)):
        return not f.eq(g, strict = strict)

    
    def __lt__(f, g):
        (F, G) = f.unify_DMP(g)
        return F.to_list() < G.to_list()

    
    def __le__(f, g):
        (F, G) = f.unify_DMP(g)
        return F.to_list() <= G.to_list()

    
    def __gt__(f, g):
        (F, G) = f.unify_DMP(g)
        return F.to_list() > G.to_list()

    
    def __ge__(f, g):
        (F, G) = f.unify_DMP(g)
        return F.to_list() >= G.to_list()

    
    def __bool__(f):
        return not (f.is_zero)



class DMP_Python(DMP):
    '''Dense Multivariate Polynomials over `K`. '''
    __slots__ = ('_rep', 'dom', 'lev')
    _new = (lambda cls, rep, dom, lev: obj = object.__new__(cls)obj._rep = repobj.lev = levobj.dom = domobj)()
    
    def _strict_eq(f, g):
