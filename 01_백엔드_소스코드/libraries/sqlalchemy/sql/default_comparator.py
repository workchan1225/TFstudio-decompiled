# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: default_comparator.pyc (Python 3.11)

__doc__ = 'Default implementation of SQL comparison operations.'
from __future__ import annotations
import typing
from typing import Any
from typing import Callable
from typing import Dict
from typing import NoReturn
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union
from  import coercions
from  import operators
from  import roles
from  import type_api
from elements import and_
from elements import BinaryExpression
from elements import ClauseElement
from elements import CollationClause
from elements import CollectionAggregate
from elements import ExpressionClauseList
from elements import False_
from elements import Null
from elements import OperatorExpression
from elements import or_
from elements import True_
from elements import UnaryExpression
from operators import OperatorType
from  import exc
from  import util
_T = typing.TypeVar('_T', bound = Any)
if typing.TYPE_CHECKING:
    from elements import ColumnElement
    from operators import custom_op
    from type_api import TypeEngine

def _boolean_compare(expr = None, op = None, obj = None, *, negate_op, reverse, _python_is_types, result_type, **kwargs):
    pass
# WARNING: Decompyle incomplete


def _custom_op_operate(expr = None, op = None, obj = None, reverse = (False, None), result_type = ('expr', 'ColumnElement[Any]', 'op', 'custom_op[Any]', 'obj', 'Any', 'reverse', 'bool', 'result_type', 'Optional[TypeEngine[Any]]', 'kw', 'Any', 'return', 'ColumnElement[Any]'), **kw):
    pass
# WARNING: Decompyle incomplete


def _binary_operate(expr = None, op = None, obj = None, *, reverse, result_type, **kw):
    coerced_obj = coercions.expect(roles.BinaryElementRole, obj, expr = expr, operator = op)
    if reverse:
        right = expr
        left = coerced_obj
    else:
        right = coerced_obj
        left = expr
# WARNING: Decompyle incomplete


def _conjunction_operate(expr = None, op = None, other = None, **kw):
    if op is operators.and_:
        return and_(expr, other)
    if None is operators.or_:
        return or_(expr, other)
    raise None()


def _scalar(expr = None, op = None, fn = None, **kw):
    return fn(expr)


def _in_impl(expr = None, op = None, seq_or_selectable = None, negate_op = ('expr', 'ColumnElement[Any]', 'op', 'OperatorType', 'seq_or_selectable', 'ClauseElement', 'negate_op', 'OperatorType', 'kw', 'Any', 'return', 'ColumnElement[Any]'), **kw):
    seq_or_selectable = coercions.expect(roles.InElementRole, seq_or_selectable, expr = expr, operator = op)
    if 'in_ops' in seq_or_selectable._annotations:
        (op, negate_op) = seq_or_selectable._annotations['in_ops']
# WARNING: Decompyle incomplete


def _getitem_impl(expr = None, op = None, other = None, **kw):
    pass
# WARNING: Decompyle incomplete


def _unsupported_impl(expr = None, op = None, *arg, **kw):
    raise NotImplementedError("Operator '%s' is not supported on this expression" % op.__name__)


def _inv_impl(expr = None, op = None, **kw):
    '''See :meth:`.ColumnOperators.__inv__`.'''
    if hasattr(expr, 'negation_clause'):
        return expr.negation_clause
    return None._negate()


def _neg_impl(expr = None, op = None, **kw):
    '''See :meth:`.ColumnOperators.__neg__`.'''
    return UnaryExpression(expr, operator = operators.neg, type_ = expr.type)


def _bitwise_not_impl(expr = None, op = None, **kw):
    '''See :meth:`.ColumnOperators.bitwise_not`.'''
    return UnaryExpression(expr, operator = operators.bitwise_not_op, type_ = expr.type)


def _match_impl(expr = None, op = None, other = None, **kw):
    '''See :meth:`.ColumnOperators.match`.'''
    pass
# WARNING: Decompyle incomplete


def _distinct_impl(expr = None, op = None, **kw):
    '''See :meth:`.ColumnOperators.distinct`.'''
    return UnaryExpression(expr, operator = operators.distinct_op, type_ = expr.type)


def _between_impl(expr = None, op = None, cleft = None, cright = ('expr', 'ColumnElement[Any]', 'op', 'OperatorType', 'cleft', 'Any', 'cright', 'Any', 'kw', 'Any', 'return', 'ColumnElement[Any]'), **kw):
    '''See :meth:`.ColumnOperators.between`.'''
    return BinaryExpression(expr, ExpressionClauseList._construct_for_list(operators.and_, type_api.NULLTYPE, coercions.expect(roles.BinaryElementRole, cleft, expr = expr, operator = operators.and_), coercions.expect(roles.BinaryElementRole, cright, expr = expr, operator = operators.and_), group = False), op, negate = operators.not_between_op if op is operators.between_op else operators.between_op, modifiers = kw)


def _collate_impl(expr = None, op = None, collation = None, **kw):
    return CollationClause._create_collation_expression(expr, collation)


def _regexp_match_impl(expr = None, op = None, pattern = None, flags = ('expr', 'ColumnElement[str]', 'op', 'OperatorType', 'pattern', 'Any', 'flags', 'Optional[str]', 'kw', 'Any', 'return', 'ColumnElement[Any]'), **kw):
    return BinaryExpression(expr, coercions.expect(roles.BinaryElementRole, pattern, expr = expr, operator = operators.comma_op), op, negate = operators.not_regexp_match_op, modifiers = {
        'flags': flags })


def _regexp_replace_impl(expr, op = None, pattern = None, replacement = None, flags = ('expr', 'ColumnElement[Any]', 'op', 'OperatorType', 'pattern', 'Any', 'replacement', 'Any', 'flags', 'Optional[str]', 'kw', 'Any', 'return', 'ColumnElement[Any]'), **kw):
    return BinaryExpression(expr, ExpressionClauseList._construct_for_list(operators.comma_op, type_api.NULLTYPE, coercions.expect(roles.BinaryElementRole, pattern, expr = expr, operator = operators.comma_op), coercions.expect(roles.BinaryElementRole, replacement, expr = expr, operator = operators.comma_op), group = False), op, modifiers = {
        'flags': flags })

# WARNING: Decompyle incomplete
