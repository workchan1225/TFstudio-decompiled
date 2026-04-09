# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utilities.pyc (Python 3.11)

from contextlib import contextmanager
from threading import local
from sympy.core.function import expand_mul

class DotProdSimpState(local):
    
    def __init__(self):
        self.state = None


_dotprodsimp_state = DotProdSimpState()
dotprodsimp = (lambda x: pass# WARNING: Decompyle incomplete
)()

def _dotprodsimp(expr, withsimp = (False,)):
    '''Wrapper for simplify.dotprodsimp to avoid circular imports.'''
    dps = dotprodsimp
    import sympy.simplify.simplify
    return dps(expr, withsimp = withsimp)


def _get_intermediate_simp(deffunc, offfunc, onfunc, dotprodsimp = ((lambda x: x), (lambda x: x), _dotprodsimp, None)):
    '''Support function for controlling intermediate simplification. Returns a
    simplification function according to the global setting of dotprodsimp
    operation.

    ``deffunc``     - Function to be used by default.
    ``offfunc``     - Function to be used if dotprodsimp has been turned off.
    ``onfunc``      - Function to be used if dotprodsimp has been turned on.
    ``dotprodsimp`` - True, False or None. Will be overridden by global
                      _dotprodsimp_state.state if that is not None.
    '''
    if dotprodsimp is False or _dotprodsimp_state.state is False:
        return offfunc
    if None is True or _dotprodsimp_state.state is True:
        return onfunc


def _get_intermediate_simp_bool(default, dotprodsimp = (False, None)):
    '''Same as ``_get_intermediate_simp`` but returns bools instead of functions
    by default.'''
    return _get_intermediate_simp(default, False, True, dotprodsimp)


def _iszero(x):
    '''Returns True if x is zero.'''
    return getattr(x, 'is_zero', None)


def _is_zero_after_expand_mul(x):
    '''Tests by expand_mul only, suitable for polynomials and rational
    functions.'''
    return expand_mul(x) == 0


def _simplify(expr):
    ''' Wrapper to avoid circular imports. '''
    simplify = simplify
    import sympy.simplify.simplify
    return simplify(expr)
