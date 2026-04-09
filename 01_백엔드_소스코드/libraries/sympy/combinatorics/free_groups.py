# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: free_groups.pyc (Python 3.11)

from __future__ import annotations
from sympy.core import S
from sympy.core.expr import Expr
from sympy.core.symbol import Symbol, symbols as _symbols
from sympy.core.sympify import CantSympify
from sympy.printing.defaults import DefaultPrinting
from sympy.utilities import public
from sympy.utilities.iterables import flatten, is_sequence
from sympy.utilities.magic import pollute
from sympy.utilities.misc import as_int
free_group = (lambda symbols: _free_group = FreeGroup(symbols)(_free_group,) + tuple(_free_group.generators))()
xfree_group = (lambda symbols: _free_group = FreeGroup(symbols)(_free_group, _free_group.generators))()
vfree_group = (lambda symbols: _free_group = FreeGroup(symbols)(lambda .0: [ sym.name for sym in .0 ])(_free_group.symbols(), _free_group.generators)
    return _free_group
)()

def _parse_symbols(symbols):
    if not symbols:
        return ()
    if None(symbols, str):
        return _symbols(symbols, seq = True)
    if None(symbols, (Expr, FreeGroupElement)):
        return (symbols,)
    if None(symbols):
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(symbols()):
            return _symbols(symbols)
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(symbols()):
            return symbols
        raise all('The type of `symbols` must be one of the following: a str, Symbol/Expr or a sequence of one of these types')

_free_group_cache: 'dict[int, FreeGroup]' = { }

class FreeGroup(DefaultPrinting):
    '''
    Free group with finite or infinite number of generators. Its input API
    is that of a str, Symbol/Expr or a sequence of one of
    these types (which may be empty)

    See Also
    ========

    sympy.polys.rings.PolyRing

    References
    ==========

    .. [1] https://www.gap-system.org/Manuals/doc/ref/chap37.html

    .. [2] https://en.wikipedia.org/wiki/Free_group

    '''
    is_associative = True
    is_group = True
    is_FreeGroup = True
    is_PermutationGroup = False
    relators: 'list[Expr]' = []
    
    def __new__(cls, symbols):
        symbols = tuple(_parse_symbols(symbols))
        rank = len(symbols)
        _hash = hash((cls.__name__, symbols, rank))
        obj = _free_group_cache.get(_hash)
    # WARNING: Decompyle incomplete

    
    def _generators(group):
        '''Returns the generators of the FreeGroup.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y, z = free_group("x, y, z")
        >>> F.generators
        (x, y, z)

        '''
        gens = []
        for sym in group.symbols:
            elm = ((sym, 1),)
            gens.append(group.dtype(elm))
            return tuple(gens)

    
    def clone(self, symbols = (None,)):
