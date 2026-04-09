# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: array_comprehension.pyc (Python 3.11)

import functools
import itertools
from sympy.core.sympify import _sympify, sympify
from sympy.core.expr import Expr
from sympy.core import Basic, Tuple
from sympy.tensor.array import ImmutableDenseNDimArray
from sympy.core.symbol import Symbol
from sympy.core.numbers import Integer

class ArrayComprehension(Basic):
    """
    Generate a list comprehension.

    Explanation
    ===========

    If there is a symbolic dimension, for example, say [i for i in range(1, N)] where
    N is a Symbol, then the expression will not be expanded to an array. Otherwise,
    calling the doit() function will launch the expansion.

    Examples
    ========

    >>> from sympy.tensor.array import ArrayComprehension
    >>> from sympy import symbols
    >>> i, j, k = symbols('i j k')
    >>> a = ArrayComprehension(10*i + j, (i, 1, 4), (j, 1, 3))
    >>> a
    ArrayComprehension(10*i + j, (i, 1, 4), (j, 1, 3))
    >>> a.doit()
    [[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]]
    >>> b = ArrayComprehension(10*i + j, (i, 1, 4), (j, 1, k))
    >>> b.doit()
    ArrayComprehension(10*i + j, (i, 1, 4), (j, 1, k))
    """
    
    def __new__(cls, function, *symbols, **assumptions):
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(symbols()):
            raise ValueError('ArrayComprehension requires values lower and upper bound for the expression')
        arglist = [
            sympify(function)]
        arglist.extend(cls._check_limits_validity(function, symbols))
    # WARNING: Decompyle incomplete

    function = (lambda self: self._args[0])()
    limits = (lambda self: self._limits)()
    free_symbols = (lambda self: expr_free_sym = self.function.free_symbolsfor var, inf, sup in self._limits:
expr_free_sym.discard(var)curr_free_syms = inf.free_symbols.union(sup.free_symbols)expr_free_sym = expr_free_sym.union(curr_free_syms)expr_free_sym)()
    variables = (lambda self: self._limits())()
    bound_symbols = (lambda self: self._limits())()
    shape = (lambda self: self._shape)()
    is_shape_numeric = (lambda self: for _, inf, sup in self._limits:
if Basic(inf, sup).atoms(Symbol):
FalseTrue)()
    
    def rank(self):
        """The rank of the expanded array.

        Examples
        ========

        >>> from sympy.tensor.array import ArrayComprehension
        >>> from sympy import symbols
        >>> i, j, k = symbols('i j k')
        >>> a = ArrayComprehension(10*i + j, (i, 1, 4), (j, 1, 3))
        >>> a.rank()
        2
        """
        return self._rank

    
    def __len__(self):
        """
        The length of the expanded array which means the number
        of elements in the array.

        Raises
        ======

        ValueError : When the length of the array is symbolic

        Examples
        ========

        >>> from sympy.tensor.array import ArrayComprehension
        >>> from sympy import symbols
        >>> i, j = symbols('i j')
        >>> a = ArrayComprehension(10*i + j, (i, 1, 4), (j, 1, 3))
        >>> len(a)
        12
        """
        if self._loop_size.free_symbols:
            raise ValueError('Symbolic length is not supported')
        return self._loop_size

    _check_limits_validity = (lambda cls, function, limits: new_limits = []# WARNING: Decompyle incomplete
)()
    _calculate_shape_from_limits = (lambda cls, limits: (lambda .0: [ (sup - inf) + 1 for _, inf, sup in .0 ])(limits())
)()
    _calculate_loop_size = (lambda cls, shape: if not shape:
0loop_size = Nonefor l in shape:
loop_size = loop_size * lloop_size)()
    
    def doit(self, **hints):
        if not self.is_shape_numeric:
            return self
        return None._expand_array()

    
    def _expand_array(self):
        res = []
    # WARNING: Decompyle incomplete

    
    def _get_element(self, values):
        temp = self.function
        for var, val in zip(self.variables, values):
            temp = temp.subs(var, val)
            return temp

    
    def tolist(self):
        """Transform the expanded array to a list.

        Raises
        ======

        ValueError : When there is a symbolic dimension

        Examples
        ========

        >>> from sympy.tensor.array import ArrayComprehension
        >>> from sympy import symbols
        >>> i, j = symbols('i j')
        >>> a = ArrayComprehension(10*i + j, (i, 1, 4), (j, 1, 3))
        >>> a.tolist()
        [[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]]
        """
        if self.is_shape_numeric:
            return self._expand_array().tolist()
        raise None('A symbolic array cannot be expanded to a list')

    
    def tomatrix(self):
        """Transform the expanded array to a matrix.

        Raises
        ======

        ValueError : When there is a symbolic dimension
        ValueError : When the rank of the expanded array is not equal to 2

        Examples
        ========

        >>> from sympy.tensor.array import ArrayComprehension
        >>> from sympy import symbols
        >>> i, j = symbols('i j')
        >>> a = ArrayComprehension(10*i + j, (i, 1, 4), (j, 1, 3))
        >>> a.tomatrix()
        Matrix([
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33],
        [41, 42, 43]])
        """
        Matrix = Matrix
        import sympy.matrices
        if not self.is_shape_numeric:
            raise ValueError('A symbolic array cannot be expanded to a matrix')
        if self._rank != 2:
            raise ValueError('Dimensions must be of size of 2')
        return Matrix(self._expand_array().tomatrix())



def isLambda(v):
