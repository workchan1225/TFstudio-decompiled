# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hadamard.pyc (Python 3.11)

from collections import Counter
from sympy.core import Mul, sympify
from sympy.core.add import Add
from sympy.core.expr import ExprBuilder
from sympy.core.sorting import default_sort_key
from sympy.functions.elementary.exponential import log
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions._shape import validate_matadd_integer as validate
from sympy.matrices.expressions.special import ZeroMatrix, OneMatrix
from sympy.strategies import unpack, flatten, condition, exhaust, rm_id, sort
from sympy.utilities.exceptions import sympy_deprecation_warning

def hadamard_product(*matrices):
    """
    Return the elementwise (aka Hadamard) product of matrices.

    Examples
    ========

    >>> from sympy import hadamard_product, MatrixSymbol
    >>> A = MatrixSymbol('A', 2, 3)
    >>> B = MatrixSymbol('B', 2, 3)
    >>> hadamard_product(A)
    A
    >>> hadamard_product(A, B)
    HadamardProduct(A, B)
    >>> hadamard_product(A, B)[0, 1]
    A[0, 1]*B[0, 1]
    """
    if not matrices:
        raise TypeError('Empty Hadamard product is undefined')
    if len(matrices) == 1:
        return matrices[0]
# WARNING: Decompyle incomplete


class HadamardProduct(MatrixExpr):
    pass
# WARNING: Decompyle incomplete


def canonicalize(x):
    """Canonicalize the Hadamard product ``x`` with mathematical properties.

    Examples
    ========

    >>> from sympy import MatrixSymbol, HadamardProduct
    >>> from sympy import OneMatrix, ZeroMatrix
    >>> from sympy.matrices.expressions.hadamard import canonicalize
    >>> from sympy import init_printing
    >>> init_printing(use_unicode=False)

    >>> A = MatrixSymbol('A', 2, 2)
    >>> B = MatrixSymbol('B', 2, 2)
    >>> C = MatrixSymbol('C', 2, 2)

    Hadamard product associativity:

    >>> X = HadamardProduct(A, HadamardProduct(B, C))
    >>> X
    A.*(B.*C)
    >>> canonicalize(X)
    A.*B.*C

    Hadamard product commutativity:

    >>> X = HadamardProduct(A, B)
    >>> Y = HadamardProduct(B, A)
    >>> X
    A.*B
    >>> Y
    B.*A
    >>> canonicalize(X)
    A.*B
    >>> canonicalize(Y)
    A.*B

    Hadamard product identity:

    >>> X = HadamardProduct(A, OneMatrix(2, 2))
    >>> X
    A.*1
    >>> canonicalize(X)
    A

    Absorbing element of Hadamard product:

    >>> X = HadamardProduct(A, ZeroMatrix(2, 2))
    >>> X
    A.*0
    >>> canonicalize(X)
    0

    Rewriting to Hadamard Power

    >>> X = HadamardProduct(A, A, A)
    >>> X
    A.*A.*A
    >>> canonicalize(X)
     .3
    A

    Notes
    =====

    As the Hadamard product is associative, nested products can be flattened.

    The Hadamard product is commutative so that factors can be sorted for
    canonical form.

    A matrix of only ones is an identity for Hadamard product,
    so every matrices of only ones can be removed.

    Any zero matrix will make the whole product a zero matrix.

    Duplicate elements can be collected and rewritten as HadamardPower

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hadamard_product_(matrices)
    """
    rule = condition((lambda x: isinstance(x, HadamardProduct)), flatten)
    fun = exhaust(rule)
    x = fun(x)
    fun = condition((lambda x: isinstance(x, HadamardProduct)), rm_id((lambda x: isinstance(x, OneMatrix))))
    x = fun(x)
    
    def absorb(x):
        pass
    # WARNING: Decompyle incomplete

    fun = condition((lambda x: isinstance(x, HadamardProduct)), absorb)
    x = fun(x)
# WARNING: Decompyle incomplete


def hadamard_power(base, exp):
    base = sympify(base)
    exp = sympify(exp)
    if exp == 1:
        return base
    if not None.is_Matrix:
        return base ** exp
    if None.is_Matrix:
        raise ValueError('cannot raise expression to a matrix')
    return HadamardPower(base, exp)


class HadamardPower(MatrixExpr):
    pass
# WARNING: Decompyle incomplete
