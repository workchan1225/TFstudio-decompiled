# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ops.pyc (Python 3.11)

'''
Operator classes for eval.
'''
from __future__ import annotations
from datetime import datetime
from functools import partial
import operator
from typing import TYPE_CHECKING, Literal
import numpy as np
from pandas._libs.tslibs import Timestamp
from pandas.core.dtypes.common import is_list_like, is_scalar

common
from pandas.core.computation.common import ensure_decoded, result_type_many
result_type_many = result_type_many
import pandas.core.common, core
from pandas.core.computation.scope import DEFAULT_GLOBALS
from pandas.io.formats.printing import pprint_thing, pprint_thing_encoded
if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator
REDUCTIONS = ('sum', 'prod', 'min', 'max')
_unary_math_ops = ('sin', 'cos', 'tan', 'exp', 'log', 'expm1', 'log1p', 'sqrt', 'sinh', 'cosh', 'tanh', 'arcsin', 'arccos', 'arctan', 'arccosh', 'arcsinh', 'arctanh', 'abs', 'log10', 'floor', 'ceil')
_binary_math_ops = ('arctan2',)
MATHOPS = _unary_math_ops + _binary_math_ops
LOCAL_TAG = '__pd_eval_local_'

class Term:
    pass
# WARNING: Decompyle incomplete


class Constant(Term):
    
    def _resolve_name(self):
        return self._name

    name = (lambda self: self.value)()
    
    def __repr__(self = None):
        return repr(self.name)


_bool_op_map = {
    'not': '~',
    'and': '&',
    'or': '|' }

class Op:
    op: 'str' = '\n    Hold an operator of arbitrary arity.\n    '
    
    def __init__(self = None, op = None, operands = None, encoding = (None,)):
        self.op = _bool_op_map.get(op, op)
        self.operands = operands
        self.encoding = encoding

    
    def __iter__(self = None):
        return iter(self.operands)

    
    def __repr__(self = None):
        '''
        Print a generic n-ary operator and its operands using infix notation.
        '''
        parened = self.operands()
        return pprint_thing(f''' {self.op} '''.join(parened))

    return_type = (lambda self: if self.op in CMP_OPS_SYMS + BOOL_OPS_SYMS:
np.bool_# WARNING: Decompyle incomplete
)()
    has_invalid_return_type = (lambda self = None:
