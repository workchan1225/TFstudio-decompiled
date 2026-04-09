# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: from_array_to_indexed.pyc (Python 3.11)

import collections.abc as collections
import operator
from itertools import accumulate
from sympy import Mul, Sum, Dummy, Add
from sympy.tensor.array.expressions import PermuteDims, ArrayAdd, ArrayElementwiseApplyFunc, Reshape
from sympy.tensor.array.expressions.array_expressions import ArrayTensorProduct, get_rank, ArrayContraction, ArrayDiagonal, get_shape, _get_array_element_or_slice, _ArrayExpr
from sympy.tensor.array.expressions.utils import _apply_permutation_to_list

def convert_array_to_indexed(expr, indices):
    return _ConvertArrayToIndexed().do_convert(expr, indices)


class _ConvertArrayToIndexed:
    
    def __init__(self):
        self.count_dummies = 0

    
    def do_convert(self, expr, indices):
        pass
    # WARNING: Decompyle incomplete
