# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: repr.pyc (Python 3.11)

'''
A Printer for generating executable code.

The most important function here is srepr that returns a string so that the
relation eval(srepr(expr))=expr holds in an appropriate environment.
'''
from __future__ import annotations
from typing import Any
from sympy.core.function import AppliedUndef
from sympy.core.mul import Mul
from mpmath.libmp import repr_dps, to_str as mlib_to_str
from printer import Printer, print_function

class ReprPrinter(Printer):
    printmethod = '_sympyrepr'
    _default_settings: 'dict[str, Any]' = {
        'order': None,
        'perm_cyclic': True }
    
    def reprify(self, args, sep):
        '''
        Prints each item in `args` and joins them with `sep`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def emptyPrinter(self, expr):
        '''
        The fallback printer.
        '''
        if isinstance(expr, str):
            return expr
        if None(expr, '__srepr__'):
            return expr.__srepr__()
        if None(expr, 'args') and hasattr(expr.args, '__iter__'):
            l = []
            for o in expr.args:
                l.append(self._print(o))
                return expr.__class__.__name__ + '(%s)' % ', '.join(l)
                if hasattr(expr, '__module__') and hasattr(expr, '__name__'):
                    return f'''<\'{expr.__module__!s}.{expr.__name__!s}\'>'''
                return None(expr)

    
    def _print_Add(self, expr, order = (None,)):
        args = self._as_ordered_terms(expr, order = order)
        args = map(self._print, args)
        clsname = type(expr).__name__
        return clsname + '(%s)' % ', '.join(args)

    
    def _print_Cycle(self, expr):
        return expr.__repr__()

    
    def _print_Permutation(self, expr):
        Permutation = Permutation
        Cycle = Cycle
        import sympy.combinatorics.permutations
        sympy_deprecation_warning = sympy_deprecation_warning
        import sympy.utilities.exceptions
        perm_cyclic = Permutation.print_cyclic
    # WARNING: Decompyle incomplete

    
    def _print_Function(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_Heaviside(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_FunctionClass(self, expr):
        if issubclass(expr, AppliedUndef):
            return 'Function(%r)' % expr.__name__
        return None.__name__

    
    def _print_Half(self, expr):
        return 'Rational(1, 2)'

    
    def _print_RationalConstant(self, expr):
        return str(expr)

    
    def _print_AtomicExpr(self, expr):
        return str(expr)

    
    def _print_NumberSymbol(self, expr):
        return str(expr)

    
    def _print_Integer(self, expr):
        return 'Integer(%i)' % expr.p

    
    def _print_Complexes(self, expr):
        return 'Complexes'

    
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

    
    def _print_EmptySet(self, expr):
        return 'EmptySet'

    
    def _print_UniversalSet(self, expr):
        return 'UniversalSet'

    
    def _print_EmptySequence(self, expr):
        return 'EmptySequence'

    
    def _print_list(self, expr):
        return '[%s]' % self.reprify(expr, ', ')

    
    def _print_dict(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_set(self, expr):
        if not expr:
            return 'set()'
        return None % self.reprify(expr, ', ')

    
    def _print_MatrixBase(self, expr):
        if (expr.rows == 0) ^ (expr.cols == 0):
            return f'''{expr.__class__.__name__!s}({self._print(expr.rows)!s}, {self._print(expr.cols)!s}, {self._print([])!s})'''
        l = None
        for i in range(expr.rows):
            l.append([])
            for j in range(expr.cols):
                l[-1].append(expr[(i, j)])
                return f'''{expr.__class__.__name__!s}({self._print(l)!s})'''

    
    def _print_BooleanTrue(self, expr):
        return 'true'

    
    def _print_BooleanFalse(self, expr):
        return 'false'

    
    def _print_NaN(self, expr):
        return 'nan'

    
    def _print_Mul(self, expr, order = (None,)):
        if self.order not in ('old', 'none'):
            args = expr.as_ordered_factors()
        else:
            args = Mul.make_args(expr)
        args = map(self._print, args)
        clsname = type(expr).__name__
        return clsname + '(%s)' % ', '.join(args)

    
    def _print_Rational(self, expr):
        return f'''Rational({self._print(expr.p)!s}, {self._print(expr.q)!s})'''

    
    def _print_PythonRational(self, expr):
        return '%s(%d, %d)' % (expr.__class__.__name__, expr.p, expr.q)

    
    def _print_Fraction(self, expr):
        return f'''Fraction({self._print(expr.numerator)!s}, {self._print(expr.denominator)!s})'''

    
    def _print_Float(self, expr):
        r = mlib_to_str(expr._mpf_, repr_dps(expr._prec))
        return "%s('%s', precision=%i)" % (expr.__class__.__name__, r, expr._prec)

    
    def _print_Sum2(self, expr):
        return f'''Sum2({self._print(expr.f)!s}, ({self._print(expr.i)!s}, {self._print(expr.a)!s}, {self._print(expr.b)!s}))'''

    
    def _print_Str(self, s):
        return f'''{s.__class__.__name__!s}({self._print(s.name)!s})'''

    
    def _print_Symbol(self, expr):
