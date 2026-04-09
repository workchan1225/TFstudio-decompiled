# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: str.pyc (Python 3.11)

'''
A Printer for generating readable representation of most SymPy classes.
'''
from __future__ import annotations
from typing import Any
from sympy.core import S, Rational, Pow, Basic, Mul, Number
from sympy.core.mul import _keep_coeff
from sympy.core.numbers import Integer
from sympy.core.relational import Relational
from sympy.core.sorting import default_sort_key
from sympy.utilities.iterables import sift
from precedence import precedence, PRECEDENCE
from printer import Printer, print_function
from mpmath.libmp import prec_to_dps, to_str as mlib_to_str

class StrPrinter(Printer):
    printmethod = '_sympystr'
    _default_settings: 'dict[str, Any]' = {
        'order': None,
        'full_prec': 'auto',
        'sympy_integers': False,
        'abbrev': False,
        'perm_cyclic': True,
        'min': None,
        'max': None }
    _relationals: 'dict[str, str]' = { }
    
    def parenthesize(self, item, level, strict = (False,)):
        if (precedence(item) < level or strict) and precedence(item) <= level:
            return '(%s)' % self._print(item)
        return None._print(item)

    
    def stringify(self, args, sep, level = (0,)):
        pass
    # WARNING: Decompyle incomplete

    
    def emptyPrinter(self, expr):
        if isinstance(expr, str):
            return expr
        if None(expr, Basic):
            return repr(expr)
        return None(expr)

    
    def _print_Add(self, expr, order = (None,)):
        terms = self._as_ordered_terms(expr, order = order)
        prec = precedence(expr)
        l = []
        for term in terms:
            t = self._print(term)
            if not t.startswith('-') and term.is_Add:
                sign = '-'
                t = t[1:]
            else:
                sign = '+'
            if precedence(term) < prec or term.is_Add:
                l.extend([
                    sign,
                    '(%s)' % t])
                continue
            l.extend([
                sign,
                t])
            sign = l.pop(0)
            if sign == '+':
                sign = ''
        return sign + ' '.join(l)

    
    def _print_BooleanTrue(self, expr):
        return 'True'

    
    def _print_BooleanFalse(self, expr):
        return 'False'

    
    def _print_Not(self, expr):
        return '~%s' % self.parenthesize(expr.args[0], PRECEDENCE['Not'])

    
    def _print_And(self, expr):
        args = list(expr.args)
        for j, i in enumerate(args):
            if isinstance(i, Relational) and i.canonical.rhs is S.NegativeInfinity:
                args.insert(0, args.pop(j))
            return self.stringify(args, ' & ', PRECEDENCE['BitwiseAnd'])

    
    def _print_Or(self, expr):
        return self.stringify(expr.args, ' | ', PRECEDENCE['BitwiseOr'])

    
    def _print_Xor(self, expr):
        return self.stringify(expr.args, ' ^ ', PRECEDENCE['BitwiseXor'])

    
    def _print_AppliedPredicate(self, expr):
        return f'''{self._print(expr.function)!s}({self.stringify(expr.arguments, ', ')!s})'''

    
    def _print_Basic(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_BlockMatrix(self, B):
        if B.blocks.shape == (1, 1):
            self._print(B.blocks[(0, 0)])
        return self._print(B.blocks)

    
    def _print_Catalan(self, expr):
        return 'Catalan'

    
    def _print_ComplexInfinity(self, expr):
        return 'zoo'

    
    def _print_ConditionSet(self, s):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_Derivative(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_dict(self, d):
        keys = sorted(d.keys(), key = default_sort_key)
        items = []
        for key in keys:
            item = f'''{self._print(key)!s}: {self._print(d[key])!s}'''
            items.append(item)
            return '{%s}' % ', '.join(items)

    
    def _print_Dict(self, expr):
        return self._print_dict(expr)

    
    def _print_RandomDomain(self, d):
        if hasattr(d, 'as_boolean'):
            return 'Domain: ' + self._print(d.as_boolean())
        if None(d, 'set'):
            return 'Domain: ' + self._print(d.symbols) + ' in ' + self._print(d.set)
        return None + self._print(d.symbols)

    
    def _print_Dummy(self, expr):
        return '_' + expr.name

    
    def _print_EulerGamma(self, expr):
        return 'EulerGamma'

    
    def _print_Exp1(self, expr):
        return 'E'

    
    def _print_ExprCondPair(self, expr):
        return f'''({self._print(expr.expr)!s}, {self._print(expr.cond)!s})'''

    
    def _print_Function(self, expr):
        return expr.func.__name__ + '(%s)' % self.stringify(expr.args, ', ')

    
    def _print_GoldenRatio(self, expr):
        return 'GoldenRatio'

    
    def _print_Heaviside(self, expr):
        return expr.func.__name__ + '(%s)' % self.stringify(expr.pargs, ', ')

    
    def _print_TribonacciConstant(self, expr):
        return 'TribonacciConstant'

    
    def _print_ImaginaryUnit(self, expr):
        return 'I'

    
    def _print_Infinity(self, expr):
        return 'oo'

    
    def _print_Integral(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_Interval(self, i):
        fin = 'Interval{m}({a}, {b})'
        (a, b, l, r) = i.args
        if a.is_infinite and b.is_infinite:
            m = ''
        elif not a.is_infinite and r:
            m = ''
        elif not b.is_infinite and l:
            m = ''
        elif not l and r:
            m = ''
        elif l and r:
            m = '.open'
        elif l:
            m = '.Lopen'
        else:
            m = '.Ropen'
    # WARNING: Decompyle incomplete

    
    def _print_AccumulationBounds(self, i):
        return f'''AccumBounds({self._print(i.min)!s}, {self._print(i.max)!s})'''

    
    def _print_Inverse(self, I):
        return '%s**(-1)' % self.parenthesize(I.arg, PRECEDENCE['Pow'])

    
    def _print_Lambda(self, obj):
        expr = obj.expr
        sig = obj.signature
        if len(sig) == 1 and sig[0].is_symbol:
            sig = sig[0]
        return f'''Lambda({self._print(sig)!s}, {self._print(expr)!s})'''

    
    def _print_LatticeOp(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_Limit(self, expr):
        (e, z, z0, dir) = expr.args
        return "Limit(%s, %s, %s, dir='%s')" % tuple(map(self._print, (e, z, z0, dir)))

    
    def _print_list(self, expr):
        return '[%s]' % self.stringify(expr, ', ')

    
    def _print_List(self, expr):
        return self._print_list(expr)

    
    def _print_MatrixBase(self, expr):
        return expr._format_str(self)

    
    def _print_MatrixElement(self, expr):
        return self.parenthesize(expr.parent, PRECEDENCE['Atom'], strict = True) + f'''[{self._print(expr.i)!s}, {self._print(expr.j)!s}]'''

    
    def _print_MatrixSlice(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_DeferredVector(self, expr):
        return expr.name

    
    def _print_Mul(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_MatMul(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_ElementwiseApplyFunction(self, expr):
        return '{}.({})'.format(expr.function, self._print(expr.expr))

    
    def _print_NaN(self, expr):
        return 'nan'

    
    def _print_NegativeInfinity(self, expr):
        return '-oo'

    
    def _print_Order(self, expr):
        if expr.variables or (lambda .0: pass# WARNING: Decompyle incomplete
)(expr.point()):
            if len(expr.variables) <= 1:
                return 'O(%s)' % self._print(expr.expr)
            return all % self.stringify((expr.expr,) + expr.variables, ', ', 0)
        return all % self.stringify(expr.args, ', ', 0)

    
    def _print_Ordinal(self, expr):
        return expr.__str__()

    
    def _print_Cycle(self, expr):
        return expr.__str__()

    
    def _print_Permutation(self, expr):
        Permutation = Permutation
        Cycle = Cycle
        import sympy.combinatorics.permutations
        sympy_deprecation_warning = sympy_deprecation_warning
        import sympy.utilities.exceptions
        perm_cyclic = Permutation.print_cyclic
    # WARNING: Decompyle incomplete

    
    def _print_Subs(self, obj):
        (expr, old, new) = obj.args
        if len(obj.point) == 1:
            old = old[0]
            new = new[0]
        return f'''Subs({self._print(expr)!s}, {self._print(old)!s}, {self._print(new)!s})'''

    
    def _print_TensorIndex(self, expr):
        return expr._print()

    
    def _print_TensorHead(self, expr):
        return expr._print()

    
    def _print_Tensor(self, expr):
        return expr._print()

    
    def _print_TensMul(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_TensAdd(self, expr):
        return expr._print()

    
    def _print_ArraySymbol(self, expr):
        return self._print(expr.name)

    
    def _print_ArrayElement(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_PermutationGroup(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_Pi(self, expr):
        return 'pi'

    
    def _print_PolyRing(self, ring):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_FracField(self, field):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_FreeGroupElement(self, elm):
        return elm.__str__()

    
    def _print_GaussianElement(self, poly):
        return f'''({poly.x!s} + {poly.y!s}*I)'''

    
    def _print_PolyElement(self, poly):
        return poly.str(self, PRECEDENCE, '%s**%s', '*')

    
    def _print_FracElement(self, frac):
        if frac.denom == 1:
            return self._print(frac.numer)
        numer = None.parenthesize(frac.numer, PRECEDENCE['Mul'], strict = True)
        denom = self.parenthesize(frac.denom, PRECEDENCE['Atom'], strict = True)
        return numer + '/' + denom

    
    def _print_Poly(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_UniversalSet(self, p):
        return 'UniversalSet'

    
    def _print_AlgebraicNumber(self, expr):
        if expr.is_aliased:
            return self._print(expr.as_poly().as_expr())
        return None._print(expr.as_expr())

    
    def _print_Pow(self, expr, rational = (False,)):
        """Printing helper function for ``Pow``

        Parameters
        ==========

        rational : bool, optional
            If ``True``, it will not attempt printing ``sqrt(x)`` or
            ``x**S.Half`` as ``sqrt``, and will use ``x**(1/2)``
            instead.

            See examples for additional details

        Examples
        ========

        >>> from sympy import sqrt, StrPrinter
        >>> from sympy.abc import x

        How ``rational`` keyword works with ``sqrt``:

        >>> printer = StrPrinter()
        >>> printer._print_Pow(sqrt(x), rational=True)
        'x**(1/2)'
        >>> printer._print_Pow(sqrt(x), rational=False)
        'sqrt(x)'
        >>> printer._print_Pow(1/sqrt(x), rational=True)
        'x**(-1/2)'
        >>> printer._print_Pow(1/sqrt(x), rational=False)
        '1/sqrt(x)'

        Notes
        =====

        ``sqrt(x)`` is canonicalized as ``Pow(x, S.Half)`` in SymPy,
        so there is no need of defining a separate printer for ``sqrt``.
        Instead, it should be handled here as well.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def _print_UnevaluatedExpr(self, expr):
        return self._print(expr.args[0])

    
    def _print_MatPow(self, expr):
        PREC = precedence(expr)
        return f'''{self.parenthesize(expr.base, PREC, strict = False)!s}**{self.parenthesize(expr.exp, PREC, strict = False)!s}'''

    
    def _print_Integer(self, expr):
        if self._settings.get('sympy_integers', False):
            return 'S(%s)' % expr
        return None(expr.p)

    
    def _print_Integers(self, expr):
        return 'Integers'

    
    def _print_Naturals(self, expr):
        return 'Naturals'

    
    def _print_Naturals0(self, expr):
        return 'Naturals0'

    
    def _print_Rationals(self, expr):
        return 'Rationals'

    
    def _print_Reals(self, expr):
        return 'Reals'

    
    def _print_Complexes(self, expr):
        return 'Complexes'

    
    def _print_EmptySet(self, expr):
        return 'EmptySet'

    
    def _print_EmptySequence(self, expr):
        return 'EmptySequence'

    
    def _print_int(self, expr):
        return str(expr)

    
    def _print_mpz(self, expr):
        return str(expr)

    
    def _print_Rational(self, expr):
        if expr.q == 1:
            return str(expr.p)
        if None._settings.get('sympy_integers', False):
            return f'''S({expr.p!s})/{expr.q!s}'''
        return f'''{None.p!s}/{expr.q!s}'''

    
    def _print_PythonRational(self, expr):
        if expr.q == 1:
            return str(expr.p)
        return None % (expr.p, expr.q)

    
    def _print_Fraction(self, expr):
        if expr.denominator == 1:
            return str(expr.numerator)
        return f'''{None.numerator!s}/{expr.denominator!s}'''

    
    def _print_mpq(self, expr):
        if expr.denominator == 1:
            return str(expr.numerator)
        return f'''{None.numerator!s}/{expr.denominator!s}'''

    
    def _print_Float(self, expr):
        prec = expr._prec
        if prec < 5:
            dps = 0
        else:
            dps = prec_to_dps(expr._prec)
        if self._settings['full_prec'] is True:
            strip = False
        elif self._settings['full_prec'] is False:
            strip = True
        elif self._settings['full_prec'] == 'auto':
            strip = self._print_level > 1
        low = self._settings['min'] if 'min' in self._settings else None
        high = self._settings['max'] if 'max' in self._settings else None
        rv = mlib_to_str(expr._mpf_, dps, strip_zeros = strip, min_fixed = low, max_fixed = high)
        if rv.startswith('-.0'):
            rv = '-0.' + rv[3:]
        elif rv.startswith('.0'):
            rv = '0.' + rv[2:]
        if rv.startswith('+'):
            rv = rv[1:]
        return rv

    
    def _print_Relational(self, expr):
