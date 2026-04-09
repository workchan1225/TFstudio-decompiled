# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: functions.pyc (Python 3.11)

from collections.abc import Iterable
from functools import singledispatch
from sympy.core.expr import Expr
from sympy.core.mul import Mul
from sympy.core.singleton import S
from sympy.core.sympify import sympify
from sympy.core.parameters import global_parameters

class TensorProduct(Expr):
    '''
    Generic class for tensor products.
    '''
    is_number = False
    
    def __new__(cls, *args, **kwargs):
        NDimArray = NDimArray
        tensorproduct = tensorproduct
        Array = Array
        import sympy.tensor.array
        MatrixExpr = MatrixExpr
        import sympy.matrices.expressions.matexpr
        MatrixBase = MatrixBase
        import sympy.matrices.matrixbase
        flatten = flatten
        import sympy.strategies
        args = args()
        evaluate = kwargs.get('evaluate', global_parameters.evaluate)
    # WARNING: Decompyle incomplete

    
    def rank(self):
        return len(self.shape)

    
    def _get_args_shapes(self):
        pass
    # WARNING: Decompyle incomplete

    shape = (lambda self: shape_list = self._get_args_shapes()sum(shape_list, ()))()
    
    def __getitem__(self, index):
        pass
    # WARNING: Decompyle incomplete


shape = (lambda expr: if hasattr(expr, 'shape'):
expr.shaperaise None('%s does not have shape, or its type is not registered to shape().' % expr))()

class NoShapeError(Exception):
    '''
    Raised when ``shape()`` is called on non-array object.

    This error can be imported from ``sympy.tensor.functions``.

    Examples
    ========

    >>> from sympy import shape
    >>> from sympy.abc import x
    >>> shape(x)
    Traceback (most recent call last):
      ...
    sympy.tensor.functions.NoShapeError: shape() called on non-array object: x
    '''
    pass
