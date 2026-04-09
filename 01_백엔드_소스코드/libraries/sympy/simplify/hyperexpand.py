# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hyperexpand.pyc (Python 3.11)

'''
Expand Hypergeometric (and Meijer G) functions into named
special functions.

The algorithm for doing this uses a collection of lookup tables of
hypergeometric functions, and various of their properties, to expand
many hypergeometric functions in terms of special functions.

It is based on the following paper:
      Kelly B. Roach.  Meijer G Function Representations.
      In: Proceedings of the 1997 International Symposium on Symbolic and
      Algebraic Computation, pages 205-211, New York, 1997. ACM.

It is described in great(er) detail in the Sphinx documentation.
'''
from collections import defaultdict
from itertools import product
from functools import reduce
from math import prod
from sympy import SYMPY_DEBUG
from sympy.core import S, Dummy, symbols, sympify, Tuple, expand, I, pi, Mul, EulerGamma, oo, zoo, expand_func, Add, nan, Expr, Rational
from sympy.core.mod import Mod
from sympy.core.sorting import default_sort_key
from sympy.functions import exp, sqrt, root, log, lowergamma, cos, besseli, gamma, uppergamma, expint, erf, sin, besselj, Ei, Ci, Si, Shi, sinh, cosh, Chi, fresnels, fresnelc, polar_lift, exp_polar, floor, ceiling, rf, factorial, lerchphi, Piecewise, re, elliptic_k, elliptic_e
from sympy.functions.elementary.complexes import polarify, unpolarify
from sympy.functions.special.hyper import hyper, HyperRep_atanh, HyperRep_power1, HyperRep_power2, HyperRep_log1, HyperRep_asin1, HyperRep_asin2, HyperRep_sqrts1, HyperRep_sqrts2, HyperRep_log2, HyperRep_cosasin, HyperRep_sinasin, meijerg
from sympy.matrices import Matrix, eye, zeros
from sympy.polys import apart, poly, Poly
from sympy.series import residue
from sympy.simplify.powsimp import powdenest
from sympy.utilities.iterables import sift

def _mod1(x):
    if x.is_Number:
        return Mod(x, 1)
    (c, x) = None.as_coeff_Add()
    return Mod(c, 1) + x


def add_formulae(formulae):
    ''' Create our knowledge base. '''
    pass
# WARNING: Decompyle incomplete


def add_meijerg_formulae(formulae):
    pass
# WARNING: Decompyle incomplete


def make_simp(z):
    ''' Create a function that simplifies rational functions in ``z``. '''
    pass
# WARNING: Decompyle incomplete


def debug(*args):
    if SYMPY_DEBUG:
        for a in args:
            print(a, end = '')
            print()
            return None
            return None


class Hyper_Function(Expr):
    pass
# WARNING: Decompyle incomplete


class G_Function(Expr):
    pass
# WARNING: Decompyle incomplete

_x = Dummy('x')

class Formula:
    '''
    This class represents hypergeometric formulae.

    Explanation
    ===========

    Its data members are:
    - z, the argument
    - closed_form, the closed form expression
    - symbols, the free symbols (parameters) in the formula
    - func, the function
    - B, C, M (see _compute_basis)

    Examples
    ========

    >>> from sympy.abc import a, b, z
    >>> from sympy.simplify.hyperexpand import Formula, Hyper_Function
    >>> func = Hyper_Function((a/2, a/3 + b, (1+a)/2), (a, b, (a+b)/7))
    >>> f = Formula(func, z, None, [a, b])

    '''
    
    def _compute_basis(self, closed_form):
        '''
        Compute a set of functions B=(f1, ..., fn), a nxn matrix M
        and a 1xn matrix C such that:
           closed_form = C B
           z d/dz B = M B.
        '''
        afactors = self.func.ap()
        bfactors = self.func.bq()
    # WARNING: Decompyle incomplete

    
    def __init__(self, func, z, res, symbols, B, C, M = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    closed_form = (lambda self: reduce((lambda s, m: s + m[0] * m[1]), zip(self.C, self.B), S.Zero)
)()
    
    def find_instantiations(self, func):
        '''
        Find substitutions of the free symbols that match ``func``.

        Return the substitution dictionaries as a list. Note that the returned
        instantiations need not actually match, or be valid!

        '''
        pass
    # WARNING: Decompyle incomplete



class FormulaCollection:
    ''' A collection of formulae to use as origins. '''
    
    def __init__(self):
        ''' Doing this globally at module init time is a pain ... '''
        self.symbolic_formulae = { }
        self.concrete_formulae = { }
        self.formulae = []
        add_formulae(self.formulae)
        for f in self.formulae:
            sizes = f.func.sizes
            if len(f.symbols) > 0:
                self.symbolic_formulae.setdefault(sizes, []).append(f)
                continue
            inv = f.func.build_invariants()
            self.concrete_formulae.setdefault(sizes, { })[inv] = f
            return None

    
    def lookup_origin(self, func):
        """
        Given the suitable target ``func``, try to find an origin in our
        knowledge base.

        Examples
        ========

        >>> from sympy.simplify.hyperexpand import (FormulaCollection,
        ...     Hyper_Function)
        >>> f = FormulaCollection()
        >>> f.lookup_origin(Hyper_Function((), ())).closed_form
        exp(_z)
        >>> f.lookup_origin(Hyper_Function([1], ())).closed_form
        HyperRep_power1(-1, _z)

        >>> from sympy import S
        >>> i = Hyper_Function([S('1/4'), S('3/4 + 4')], [S.Half])
        >>> f.lookup_origin(i).closed_form
        HyperRep_sqrts1(-1/4, _z)
        """
        inv = func.build_invariants()
        sizes = func.sizes
        if sizes in self.concrete_formulae and inv in self.concrete_formulae[sizes]:
            return self.concrete_formulae[sizes][inv]
        if None not in self.symbolic_formulae:
            return None
        possible = None
        for f in self.symbolic_formulae[sizes]:
            repls = f.find_instantiations(func)
            for repl in repls:
                func2 = f.func.xreplace(repl)
                if not func2._is_suitable_origin():
                    continue
                diff = func2.difficulty(func)
                if diff == -1:
                    continue
                possible.append((diff, repl, f, func2))
                possible.sort(key = (lambda x: x[0]))
                for _, repl, f, func2 in possible:
                    f2 = Formula(func2, f.z, None, [], f.B.subs(repl), f.C.subs(repl), f.M.subs(repl))
                    if not (lambda .0: pass# WARNING: Decompyle incomplete
)((f2.B, f2.M, f2.C)()):
                        
                        return any, f2
                    return None



class MeijerFormula:
    '''
    This class represents a Meijer G-function formula.

    Its data members are:
    - z, the argument
    - symbols, the free symbols (parameters) in the formula
    - func, the function
    - B, C, M (c/f ordinary Formula)
    '''
    
    def __init__(self, an, ap, bm, bq, z, symbols, B, C, M, matcher):
        (an, ap, bm, bq) = (an, ap, bm, bq)()
        self.func = G_Function(an, ap, bm, bq)
        self.z = z
        self.symbols = symbols
        self._matcher = matcher
        self.B = B
        self.C = C
        self.M = M

    closed_form = (lambda self: reduce((lambda s, m: s + m[0] * m[1]), zip(self.C, self.B), S.Zero)
)()
    
    def try_instantiate(self, func):
        '''
        Try to instantiate the current formula to (almost) match func.
        This uses the _matcher passed on init.
        '''
        if func.signature != self.func.signature:
            return None
        res = None._matcher(func)
    # WARNING: Decompyle incomplete



class MeijerFormulaCollection:
    '''
    This class holds a collection of meijer g formulae.
    '''
    
    def __init__(self):
        formulae = []
        add_meijerg_formulae(formulae)
        self.formulae = defaultdict(list)
        for formula in formulae:
            self.formulae[formula.func.signature].append(formula)
        self.formulae = dict(self.formulae)

    
    def lookup_origin(self, func):
        ''' Try to find a formula that matches func. '''
        if func.signature not in self.formulae:
            return None
    # WARNING: Decompyle incomplete



class Operator:
    '''
    Base class for operators to be applied to our functions.

    Explanation
    ===========

    These operators are differential operators. They are by convention
    expressed in the variable D = z*d/dz (although this base class does
    not actually care).
    Note that when the operator is applied to an object, we typically do
    *not* blindly differentiate but instead use a different representation
    of the z*d/dz operator (see make_derivative_operator).

    To subclass from this, define a __init__ method that initializes a
    self._poly variable. This variable stores a polynomial. By convention
    the generator is z*d/dz, and acts to the right of all coefficients.

    Thus this poly
        x**2 + 2*z*x + 1
    represents the differential operator
        (z*d/dz)**2 + 2*z**2*d/dz.

    This class is used only in the implementation of the hypergeometric
    function expansion algorithm.
    '''
    
    def apply(self, obj, op):
        '''
        Apply ``self`` to the object ``obj``, where the generator is ``op``.

        Examples
        ========

        >>> from sympy.simplify.hyperexpand import Operator
        >>> from sympy.polys.polytools import Poly
        >>> from sympy.abc import x, y, z
        >>> op = Operator()
        >>> op._poly = Poly(x**2 + z*x + y, x)
        >>> op.apply(z**7, lambda f: f.diff(z))
        y*z**7 + 7*z**7 + 42*z**5
        '''
        coeffs = self._poly.all_coeffs()
        coeffs.reverse()
        diffs = [
            obj]
        for c in coeffs[1:]:
            diffs.append(op(diffs[-1]))
            r = coeffs[0] * diffs[0]
            for c, d in zip(coeffs[1:], diffs[1:]):
                r += c * d
                return r



class MultOperator(Operator):
    ''' Simply multiply by a "constant" '''
    
    def __init__(self, p):
        self._poly = Poly(p, _x)



class ShiftA(Operator):
    ''' Increment an upper index. '''
    
    def __init__(self, ai):
        ai = sympify(ai)
        if ai == 0:
            raise ValueError('Cannot increment zero upper index.')
        self._poly = Poly(_x / ai + 1, _x)

    
    def __str__(self):
        return '<Increment upper %s.>' % 1 / self._poly.all_coeffs()[0]



class ShiftB(Operator):
    ''' Decrement a lower index. '''
    
    def __init__(self, bi):
        bi = sympify(bi)
        if bi == 1:
            raise ValueError('Cannot decrement unit lower index.')
        self._poly = Poly(_x / (bi - 1) + 1, _x)

    
    def __str__(self):
        return '<Decrement lower %s.>' % (1 / self._poly.all_coeffs()[0] + 1)



class UnShiftA(Operator):
    ''' Decrement an upper index. '''
    
    def __init__(self, ap, bq, i, z):
        ''' Note: i counts from zero! '''
        (ap, bq, i) = list(map(sympify, [
            ap,
            bq,
            i]))
        self._ap = ap
        self._bq = bq
        self._i = i
        ap = list(ap)
        bq = list(bq)
        ai = ap.pop(i) - 1
        if ai == 0:
            raise ValueError('Cannot decrement unit upper index.')
        m = Poly(z * ai, _x)
        for a in ap:
            m *= Poly(_x + a, _x)
            A = Dummy('A')
            n = Poly(ai * A - ai, A)
            D = Poly(ai * A - ai, A)
            for b in bq:
                n *= D + (b - 1).as_poly(A)
                b0 = -n.nth(0)
                if b0 == 0:
                    raise ValueError('Cannot decrement upper index: cancels with lower')
                n = Poly(Poly(n.all_coeffs()[:-1], A).as_expr().subs(A, _x / ai + 1), _x)
                self._poly = Poly((n - m) / b0, _x)
                return None

    
    def __str__(self):
        return f'''<Decrement upper index #{self._i!s} of {self._ap!s}, {self._bq!s}.>'''



class UnShiftB(Operator):
    ''' Increment a lower index. '''
    
    def __init__(self, ap, bq, i, z):
        ''' Note: i counts from zero! '''
        (ap, bq, i) = list(map(sympify, [
            ap,
            bq,
            i]))
        self._ap = ap
        self._bq = bq
        self._i = i
        ap = list(ap)
        bq = list(bq)
        bi = bq.pop(i) + 1
        if bi == 0:
            raise ValueError('Cannot increment -1 lower index.')
        m = Poly(_x * (bi - 1), _x)
        for b in bq:
            m *= Poly(_x + b - 1, _x)
            B = Dummy('B')
            D = Poly(((bi - 1) * B - bi) + 1, B)
            n = Poly(z, B)
            for a in ap:
                n *= D + a.as_poly(B)
                b0 = n.nth(0)
                if b0 == 0:
                    raise ValueError('Cannot increment index: cancels with upper')
                n = Poly(Poly(n.all_coeffs()[:-1], B).as_expr().subs(B, _x / (bi - 1) + 1), _x)
                self._poly = Poly((m - n) / b0, _x)
                return None

    
    def __str__(self):
        return f'''<Increment lower index #{self._i!s} of {self._ap!s}, {self._bq!s}.>'''



class MeijerShiftA(Operator):
    ''' Increment an upper b index. '''
    
    def __init__(self, bi):
        bi = sympify(bi)
        self._poly = Poly(bi - _x, _x)

    
    def __str__(self):
        return '<Increment upper b=%s.>' % self._poly.all_coeffs()[1]



class MeijerShiftB(Operator):
    ''' Decrement an upper a index. '''
    
    def __init__(self, bi):
        bi = sympify(bi)
        self._poly = Poly((1 - bi) + _x, _x)

    
    def __str__(self):
        return '<Decrement upper a=%s.>' % (1 - self._poly.all_coeffs()[1])



class MeijerShiftC(Operator):
    ''' Increment a lower b index. '''
    
    def __init__(self, bi):
        bi = sympify(bi)
        self._poly = Poly(-bi + _x, _x)

    
    def __str__(self):
        return '<Increment lower b=%s.>' % -self._poly.all_coeffs()[1]



class MeijerShiftD(Operator):
    ''' Decrement a lower a index. '''
    
    def __init__(self, bi):
        bi = sympify(bi)
        self._poly = Poly(bi - 1 - _x, _x)

    
    def __str__(self):
        return '<Decrement lower a=%s.>' % (self._poly.all_coeffs()[1] + 1)



class MeijerUnShiftA(Operator):
    ''' Decrement an upper b index. '''
    
    def __init__(self, an, ap, bm, bq, i, z):
        ''' Note: i counts from zero! '''
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return f'''<Decrement upper b index #{self._i!s} of {self._an!s}, {self._ap!s}, {self._bm!s}, {self._bq!s}.>'''



class MeijerUnShiftB(Operator):
    ''' Increment an upper a index. '''
    
    def __init__(self, an, ap, bm, bq, i, z):
        ''' Note: i counts from zero! '''
        (an, ap, bm, bq, i) = list(map(sympify, [
            an,
            ap,
            bm,
            bq,
            i]))
        self._an = an
        self._ap = ap
        self._bm = bm
        self._bq = bq
        self._i = i
        an = list(an)
        ap = list(ap)
        bm = list(bm)
        bq = list(bq)
        ai = an.pop(i) + 1
        m = Poly(z, _x)
        for a in an:
            m *= Poly((1 - a) + _x, _x)
            for a in ap:
                m *= Poly(a - 1 - _x, _x)
                B = Dummy('B')
                D = Poly(B + ai - 1, B)
                n = Poly(1, B)
                for b in bm:
                    n *= -D + b
                    for b in bq:
                        n *= D - b
                        b0 = n.nth(0)
                        if b0 == 0:
                            raise ValueError('Cannot increment upper a index (cancels)')
                        n = Poly(Poly(n.all_coeffs()[:-1], B).as_expr().subs(B, (1 - ai) + _x), _x)
                        self._poly = Poly((m - n) / b0, _x)
                        return None

    
    def __str__(self):
        return f'''<Increment upper a index #{self._i!s} of {self._an!s}, {self._ap!s}, {self._bm!s}, {self._bq!s}.>'''



class MeijerUnShiftC(Operator):
    ''' Decrement a lower b index. '''
    
    def __init__(self, an, ap, bm, bq, i, z):
        ''' Note: i counts from zero! '''
        (an, ap, bm, bq, i) = list(map(sympify, [
            an,
            ap,
            bm,
            bq,
            i]))
        self._an = an
        self._ap = ap
        self._bm = bm
        self._bq = bq
        self._i = i
        an = list(an)
        ap = list(ap)
        bm = list(bm)
        bq = list(bq)
        bi = bq.pop(i) - 1
        m = Poly(1, _x)
        for b in bm:
            m *= Poly(b - _x, _x)
            for b in bq:
                m *= Poly(_x - b, _x)
                C = Dummy('C')
                D = Poly(bi + C, C)
                n = Poly(z, C)
                for a in an:
                    n *= D + 1 - a
                    for a in ap:
                        n *= -D + a - 1
                        b0 = n.nth(0)
                        if b0 == 0:
                            raise ValueError('Cannot decrement lower b index (cancels)')
                        n = Poly(Poly(n.all_coeffs()[:-1], C).as_expr().subs(C, _x - bi), _x)
                        self._poly = Poly((m - n) / b0, _x)
                        return None

    
    def __str__(self):
        return f'''<Decrement lower b index #{self._i!s} of {self._an!s}, {self._ap!s}, {self._bm!s}, {self._bq!s}.>'''



class MeijerUnShiftD(Operator):
    ''' Increment a lower a index. '''
    
    def __init__(self, an, ap, bm, bq, i, z):
        ''' Note: i counts from zero! '''
        (an, ap, bm, bq, i) = list(map(sympify, [
            an,
            ap,
            bm,
            bq,
            i]))
        self._an = an
        self._ap = ap
        self._bm = bm
        self._bq = bq
        self._i = i
        an = list(an)
        ap = list(ap)
        bm = list(bm)
        bq = list(bq)
        ai = ap.pop(i) + 1
        m = Poly(z, _x)
        for a in an:
            m *= Poly((1 - a) + _x, _x)
            for a in ap:
                m *= Poly(a - 1 - _x, _x)
                B = Dummy('B')
                D = Poly(ai - 1 - B, B)
                n = Poly(1, B)
                for b in bm:
                    n *= -D + b
                    for b in bq:
                        n *= D - b
                        b0 = n.nth(0)
                        if b0 == 0:
                            raise ValueError('Cannot increment lower a index (cancels)')
                        n = Poly(Poly(n.all_coeffs()[:-1], B).as_expr().subs(B, ai - 1 - _x), _x)
                        self._poly = Poly((m - n) / b0, _x)
                        return None

    
    def __str__(self):
        return f'''<Increment lower a index #{self._i!s} of {self._an!s}, {self._ap!s}, {self._bm!s}, {self._bq!s}.>'''



class ReduceOrder(Operator):
    ''' Reduce Order by cancelling an upper and a lower index. '''
    
    def __new__(cls, ai, bj):
        ''' For convenience if reduction is not possible, return None. '''
        ai = sympify(ai)
        bj = sympify(bj)
        n = ai - bj
        if n.is_Integer or n < 0:
            return None
        if None.is_integer and bj.is_nonpositive:
            return None
        expr = None.__new__(cls)
        p = S.One
        for k in range(n):
            p *= (_x + bj + k) / (bj + k)
            expr._poly = Poly(p, _x)
            expr._a = ai
            expr._b = bj
            return expr

    _meijer = (lambda cls, b, a, sign: b = sympify(b)a = sympify(a)n = b - aif not n.is_negative or n.is_Integer:
Noneexpr = None.__new__(cls)p = S.Onefor k in range(n):
p *= sign * _x + a + kexpr._poly = Poly(p, _x)if sign == -1:
expr._a = bexpr._b = aelse:
expr._b = Add(1, a - 1, evaluate = False)expr._a = Add(1, b - 1, evaluate = False)expr)()
    meijer_minus = (lambda cls, b, a: cls._meijer(b, a, -1))()
    meijer_plus = (lambda cls, a, b: cls._meijer(1 - a, 1 - b, 1))()
    
    def __str__(self):
        return f'''<Reduce order by cancelling upper {self._a!s} with lower {self._b!s}.>'''



def _reduce_order(ap, bq, gen, key):
    ''' Order reduction algorithm used in Hypergeometric and Meijer G '''
    ap = list(ap)
    bq = list(bq)
    ap.sort(key = key)
    bq.sort(key = key)
    nap = []
    operators = []
# WARNING: Decompyle incomplete


def reduce_order(func):
    '''
    Given the hypergeometric function ``func``, find a sequence of operators to
    reduces order as much as possible.

    Explanation
    ===========

    Return (newfunc, [operators]), where applying the operators to the
    hypergeometric function newfunc yields func.

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import reduce_order, Hyper_Function
    >>> reduce_order(Hyper_Function((1, 2), (3, 4)))
    (Hyper_Function((1, 2), (3, 4)), [])
    >>> reduce_order(Hyper_Function((1,), (1,)))
    (Hyper_Function((), ()), [<Reduce order by cancelling upper 1 with lower 1.>])
    >>> reduce_order(Hyper_Function((2, 4), (3, 3)))
    (Hyper_Function((2,), (3,)), [<Reduce order by cancelling
    upper 4 with lower 3.>])
    '''
    (nap, nbq, operators) = _reduce_order(func.ap, func.bq, ReduceOrder, default_sort_key)
# WARNING: Decompyle incomplete


def reduce_order_meijer(func):
    '''
    Given the Meijer G function parameters, ``func``, find a sequence of
    operators that reduces order as much as possible.

    Return newfunc, [operators].

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import (reduce_order_meijer,
    ...                                         G_Function)
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [3, 4], [1, 2]))[0]
    G_Function((4, 3), (5, 6), (3, 4), (2, 1))
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [3, 4], [1, 8]))[0]
    G_Function((3,), (5, 6), (3, 4), (1,))
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [7, 5], [1, 5]))[0]
    G_Function((3,), (), (), (1,))
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [7, 5], [5, 3]))[0]
    G_Function((), (), (), ())
    '''
    (nan, nbq, ops1) = _reduce_order(func.an, func.bq, ReduceOrder.meijer_plus, (lambda x: default_sort_key(-x)))
    (nbm, nap, ops2) = _reduce_order(func.bm, func.ap, ReduceOrder.meijer_minus, default_sort_key)
    return (G_Function(nan, nap, nbm, nbq), ops1 + ops2)


def make_derivative_operator(M, z):
    ''' Create a derivative operator, to be passed to Operator.apply. '''
    pass
# WARNING: Decompyle incomplete


def apply_operators(obj, ops, op):
    '''
    Apply the list of operators ``ops`` to object ``obj``, substituting
    ``op`` for the generator.
    '''
    res = obj
    for o in reversed(ops):
        res = o.apply(res, op)
        return res


def devise_plan(target, origin, z):
    """
    Devise a plan (consisting of shift and un-shift operators) to be applied
    to the hypergeometric function ``target`` to yield ``origin``.
    Returns a list of operators.

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import devise_plan, Hyper_Function
    >>> from sympy.abc import z

    Nothing to do:

    >>> devise_plan(Hyper_Function((1, 2), ()), Hyper_Function((1, 2), ()), z)
    []
    >>> devise_plan(Hyper_Function((), (1, 2)), Hyper_Function((), (1, 2)), z)
    []

    Very simple plans:

    >>> devise_plan(Hyper_Function((2,), ()), Hyper_Function((1,), ()), z)
    [<Increment upper 1.>]
    >>> devise_plan(Hyper_Function((), (2,)), Hyper_Function((), (1,)), z)
    [<Increment lower index #0 of [], [1].>]

    Several buckets:

    >>> from sympy import S
    >>> devise_plan(Hyper_Function((1, S.Half), ()),
    ...             Hyper_Function((2, S('3/2')), ()), z) #doctest: +NORMALIZE_WHITESPACE
    [<Decrement upper index #0 of [3/2, 1], [].>,
    <Decrement upper index #0 of [2, 3/2], [].>]

    A slightly more complicated plan:

    >>> devise_plan(Hyper_Function((1, 3), ()), Hyper_Function((2, 2), ()), z)
    [<Increment upper 2.>, <Decrement upper index #0 of [2, 2], [].>]

    Another more complicated plan: (note that the ap have to be shifted first!)

    >>> devise_plan(Hyper_Function((1, -1), (2,)), Hyper_Function((3, -2), (4,)), z)
    [<Decrement lower 3.>, <Decrement lower 4.>,
    <Decrement upper index #1 of [-1, 2], [4].>,
    <Decrement upper index #1 of [-1, 3], [4].>, <Increment upper -2.>]
    """
    pass
# WARNING: Decompyle incomplete


def try_shifted_sum(func, z):
    ''' Try to recognise a hypergeometric sum that starts from k > 0. '''
    pass
# WARNING: Decompyle incomplete


def try_polynomial(func, z):
    ''' Recognise polynomial cases. Returns None if not such a case.
        Requires order to be fully reduced. '''
    pass
# WARNING: Decompyle incomplete


def try_lerchphi(func):
    '''
    Try to find an expression for Hyper_Function ``func`` in terms of Lerch
    Transcendents.

    Return None if no such expression can be found.
    '''
    bbuckets = sift(func.bq, _mod1)
    abuckets = sift(func.ap, _mod1)
    paired = { }
# WARNING: Decompyle incomplete


def build_hypergeometric_formula(func):
    '''
    Create a formula object representing the hypergeometric function ``func``.

    '''
    z = Dummy('z')
# WARNING: Decompyle incomplete


def hyperexpand_special(ap, bq, z):
