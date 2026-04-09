# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pretty.pyc (Python 3.11)

import itertools
from sympy.core import S
from sympy.core.add import Add
from sympy.core.containers import Tuple
from sympy.core.function import Function
from sympy.core.mul import Mul
from sympy.core.numbers import Number, Rational
from sympy.core.power import Pow
from sympy.core.sorting import default_sort_key
from sympy.core.symbol import Symbol
from sympy.core.sympify import SympifyError
from sympy.printing.conventions import requires_partial
from sympy.printing.precedence import PRECEDENCE, precedence, precedence_traditional
from sympy.printing.printer import Printer, print_function
from sympy.printing.str import sstr
from sympy.utilities.iterables import has_variety
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.printing.pretty.stringpict import prettyForm, stringPict
from sympy.printing.pretty.pretty_symbology import hobj, vobj, xobj, xsym, pretty_symbol, pretty_atom, pretty_use_unicode, greek_unicode, U, pretty_try_use_unicode, annotated, is_subscriptable_in_unicode, center_pad, root as nth_root
pprint_use_unicode = pretty_use_unicode
pprint_try_use_unicode = pretty_try_use_unicode

class PrettyPrinter(Printer):
    '''Printer, which converts an expression into 2D ASCII-art figure.'''
    printmethod = '_pretty'
    _default_settings = {
        'order': None,
        'full_prec': 'auto',
        'use_unicode': None,
        'wrap_line': True,
        'num_columns': None,
        'use_unicode_sqrt_char': True,
        'root_notation': True,
        'mat_symbol_style': 'plain',
        'imaginary_unit': 'i',
        'perm_cyclic': True }
    
    def __init__(self, settings = (None,)):
        Printer.__init__(self, settings)
        if not isinstance(self._settings['imaginary_unit'], str):
            raise TypeError("'imaginary_unit' must a string, not {}".format(self._settings['imaginary_unit']))
        if self._settings['imaginary_unit'] not in ('i', 'j'):
            raise ValueError("'imaginary_unit' must be either 'i' or 'j', not '{}'".format(self._settings['imaginary_unit']))

    
    def emptyPrinter(self, expr):
        return prettyForm(str(expr))

    _use_unicode = (lambda self: if self._settings['use_unicode']:
TrueNone())()
    
    def doprint(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_stringPict(self, e):
        return e

    
    def _print_basestring(self, e):
        return prettyForm(e)

    
    def _print_atan2(self, e):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_Symbol(self, e, bold_name = (False,)):
        symb = pretty_symbol(e.name, bold_name)
        return prettyForm(symb)

    _print_RandomSymbol = _print_Symbol
    
    def _print_MatrixSymbol(self, e):
        return self._print_Symbol(e, self._settings['mat_symbol_style'] == 'bold')

    
    def _print_Float(self, e):
        full_prec = self._settings['full_prec']
        if full_prec == 'auto':
            full_prec = self._print_level == 1
        return prettyForm(sstr(e, full_prec = full_prec))

    
    def _print_Cross(self, e):
        vec1 = e._expr1
        vec2 = e._expr2
        pform = self._print(vec2)
    # WARNING: Decompyle incomplete

    
    def _print_Curl(self, e):
        vec = e._expr
        pform = self._print(vec)
    # WARNING: Decompyle incomplete

    
    def _print_Divergence(self, e):
        vec = e._expr
        pform = self._print(vec)
    # WARNING: Decompyle incomplete

    
    def _print_Dot(self, e):
        vec1 = e._expr1
        vec2 = e._expr2
        pform = self._print(vec2)
    # WARNING: Decompyle incomplete

    
    def _print_Gradient(self, e):
        func = e._expr
        pform = self._print(func)
    # WARNING: Decompyle incomplete

    
    def _print_Laplacian(self, e):
        func = e._expr
        pform = self._print(func)
    # WARNING: Decompyle incomplete

    
    def _print_Atom(self, e):
        
        try:
            return prettyForm(pretty_atom(e.__class__.__name__, printer = self))
        except KeyError:
            return 


    _print_Infinity = _print_Atom
    _print_NegativeInfinity = _print_Atom
    _print_EmptySet = _print_Atom
    _print_Naturals = _print_Atom
    _print_Naturals0 = _print_Atom
    _print_Integers = _print_Atom
    _print_Rationals = _print_Atom
    _print_Complexes = _print_Atom
    _print_EmptySequence = _print_Atom
    
    def _print_Reals(self, e):
        if self._use_unicode:
            return self._print_Atom(e)
        inf_list = [
            None,
            'oo']
        return self._print_seq(inf_list, '(', ')')

    
    def _print_subfactorial(self, e):
        x = e.args[0]
        pform = self._print(x)
    # WARNING: Decompyle incomplete

    
    def _print_factorial(self, e):
        x = e.args[0]
        pform = self._print(x)
    # WARNING: Decompyle incomplete

    
    def _print_factorial2(self, e):
        x = e.args[0]
        pform = self._print(x)
    # WARNING: Decompyle incomplete

    
    def _print_binomial(self, e):
        (n, k) = e.args
        n_pform = self._print(n)
        k_pform = self._print(k)
        bar = ' ' * max(n_pform.width(), k_pform.width())
    # WARNING: Decompyle incomplete

    
    def _print_Relational(self, e):
        op = prettyForm(' ' + xsym(e.rel_op) + ' ')
        l = self._print(e.lhs)
        r = self._print(e.rhs)
    # WARNING: Decompyle incomplete

    
    def _print_Not(self, e):
        Equivalent = Equivalent
        Implies = Implies
        import sympy.logic.boolalg
    # WARNING: Decompyle incomplete

    
    def __print_Boolean(self, e, char, sort = (True,)):
        args = e.args
        if sort:
            args = sorted(e.args, key = default_sort_key)
        arg = args[0]
        pform = self._print(arg)
    # WARNING: Decompyle incomplete

    
    def _print_And(self, e):
        if self._use_unicode:
            return self.__print_Boolean(e, pretty_atom('And'))
        return None._print_Function(e, sort = True)

    
    def _print_Or(self, e):
        if self._use_unicode:
            return self.__print_Boolean(e, pretty_atom('Or'))
        return None._print_Function(e, sort = True)

    
    def _print_Xor(self, e):
        if self._use_unicode:
            return self.__print_Boolean(e, pretty_atom('Xor'))
        return None._print_Function(e, sort = True)

    
    def _print_Nand(self, e):
        if self._use_unicode:
            return self.__print_Boolean(e, pretty_atom('Nand'))
        return None._print_Function(e, sort = True)

    
    def _print_Nor(self, e):
        if self._use_unicode:
            return self.__print_Boolean(e, pretty_atom('Nor'))
        return None._print_Function(e, sort = True)

    
    def _print_Implies(self, e, altchar = (None,)):
