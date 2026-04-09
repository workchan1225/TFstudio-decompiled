# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: expressions.pyc (Python 3.11)

__doc__ = '\nExpressions\n-----------\n\nOffer fast expression evaluation through numexpr\n\n'
from __future__ import annotations
import operator
from typing import TYPE_CHECKING
import warnings
import numpy as np
from pandas._config import get_option
from pandas.util._exceptions import find_stack_level
from pandas.core import roperator
from pandas.core.computation.check import NUMEXPR_INSTALLED
if NUMEXPR_INSTALLED:
    import numexpr as ne
if TYPE_CHECKING:
    from pandas._typing import FuncType
_TEST_MODE: 'bool | None' = None
_TEST_RESULT: 'list[bool]' = []
USE_NUMEXPR = NUMEXPR_INSTALLED
_evaluate: 'FuncType | None' = None
_where: 'FuncType | None' = None
_ALLOWED_DTYPES = {
    'evaluate': {
        'bool',
        'int32',
        'int64',
        'float32',
        'float64'},
    'where': {
        'bool',
        'int64',
        'float64'} }
_MIN_ELEMENTS = 1000000

def set_use_numexpr(v = None):
    global USE_NUMEXPR, _evaluate, _where
    if NUMEXPR_INSTALLED:
        USE_NUMEXPR = v
    _evaluate = _evaluate_numexpr if USE_NUMEXPR else _evaluate_standard
    _where = _where_numexpr if USE_NUMEXPR else _where_standard


def set_numexpr_threads(n = None):
    pass
# WARNING: Decompyle incomplete


def _evaluate_standard(op, op_str, left_op, right_op):
    '''
    Standard evaluation.
    '''
    if _TEST_MODE:
        _store_test_result(False)
    return op(left_op, right_op)


def _can_use_numexpr(op, op_str = None, left_op = None, right_op = None, dtype_check = ('return', 'bool')):
    '''return left_op boolean if we WILL be using numexpr'''
    pass
# WARNING: Decompyle incomplete


def _evaluate_numexpr(op, op_str, left_op, right_op):
    result = None
    if _can_use_numexpr(op, op_str, left_op, right_op, 'evaluate'):
        is_reversed = op.__name__.strip('_').startswith('r')
        if is_reversed:
            right_op = left_op
            left_op = right_op
        left_value = left_op
        right_value = right_op
        
        try:
            result = ne.evaluate(f'''left_value {op_str} right_value''', local_dict = {
                'left_value': left_value,
                'right_value': right_value }, casting = 'safe')
        except TypeError:
            pass
        except NotImplementedError:
            if _bool_arith_fallback(op_str, left_op, right_op):
                pass
            else:
                raise 

        if is_reversed:
            right_op = left_op
            left_op = right_op
    if _TEST_MODE:
        _store_test_result(result is not None)
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
