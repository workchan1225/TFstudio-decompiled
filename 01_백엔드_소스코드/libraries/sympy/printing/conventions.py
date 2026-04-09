# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conventions.pyc (Python 3.11)

'''
A few practical conventions common to all printers.
'''
import re
from collections.abc import Iterable
from sympy.core.function import Derivative
_name_with_digits_p = re.compile('^([^\\W\\d_]+)(\\d+)$', re.U)

def split_super_sub(text):
    '''Split a symbol name into a name, superscripts and subscripts

    The first part of the symbol name is considered to be its actual
    \'name\', followed by super- and subscripts. Each superscript is
    preceded with a "^" character or by "__". Each subscript is preceded
    by a "_" character.  The three return values are the actual name, a
    list with superscripts and a list with subscripts.

    Examples
    ========

    >>> from sympy.printing.conventions import split_super_sub
    >>> split_super_sub(\'a_x^1\')
    (\'a\', [\'1\'], [\'x\'])
    >>> split_super_sub(\'var_sub1__sup_sub2\')
    (\'var\', [\'sup\'], [\'sub1\', \'sub2\'])

    '''
    if not text:
        return (text, [], [])
    pos = None
    name = None
    supers = []
    subs = []
# WARNING: Decompyle incomplete


def requires_partial(expr):
    '''Return whether a partial derivative symbol is required for printing

    This requires checking how many free variables there are,
    filtering out the ones that are integers. Some expressions do not have
    free variables. In that case, check its variable list explicitly to
    get the context of the expression.
    '''
    if isinstance(expr, Derivative):
        return requires_partial(expr.expr)
    if not None(expr.free_symbols, Iterable):
        return len(set(expr.variables)) > 1
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(expr.free_symbols()) > 1
