# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: adjoint.pyc (Python 3.11)

from sympy.core import Basic
from sympy.functions import adjoint, conjugate
from sympy.matrices.expressions.matexpr import MatrixExpr

class Adjoint(MatrixExpr):
    """
    The Hermitian adjoint of a matrix expression.

    This is a symbolic object that simply stores its argument without
    evaluating it. To actually compute the adjoint, use the ``adjoint()``
    function.

    Examples
    ========

    >>> from sympy import MatrixSymbol, Adjoint, adjoint
    >>> A = MatrixSymbol('A', 3, 5)
    >>> B = MatrixSymbol('B', 5, 3)
    >>> Adjoint(A*B)
    Adjoint(A*B)
    >>> adjoint(A*B)
    Adjoint(B)*Adjoint(A)
    >>> adjoint(A*B) == Adjoint(A*B)
    False
    >>> adjoint(A*B) == Adjoint(A*B).doit()
    True
    """
    is_Adjoint = True
    
    def doit(self, **hints):
        arg = self.arg
    # WARNING: Decompyle incomplete

    arg = (lambda self: self.args[0])()
    shape = (lambda self: self.arg.shape[::-1])()
    
    def _entry(self, i, j, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_adjoint(self):
        return self.arg

    
    def _eval_transpose(self):
        return self.arg.conjugate()

    
    def _eval_conjugate(self):
        return self.arg.transpose()

    
    def _eval_trace(self):
        Trace = Trace
        import sympy.matrices.expressions.trace
        return conjugate(Trace(self.arg))
