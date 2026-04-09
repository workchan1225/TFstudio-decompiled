# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: evaluator.pyc (Python 3.11)

'''Evaluation functions used **INTERNALLY** by ORM DML use cases.


This module is **private, for internal use by SQLAlchemy**.

.. versionchanged:: 2.0.4 renamed ``EvaluatorCompiler`` to
   ``_EvaluatorCompiler``.

'''
from __future__ import annotations
from typing import Type
from  import exc as orm_exc
from base import LoaderCallableStatus
from base import PassiveFlag
from  import exc
from  import inspect
from sql import and_
from sql import operators
from sql.sqltypes import Concatenable
from sql.sqltypes import Integer
from sql.sqltypes import Numeric
from util import warn_deprecated

class UnevaluatableError(exc.InvalidRequestError):
    pass


class _NoObject(operators.ColumnOperators):
    
    def operate(self, *arg, **kw):
        pass

    
    def reverse_operate(self, *arg, **kw):
        pass



class _ExpiredObject(operators.ColumnOperators):
    
    def operate(self, *arg, **kw):
        return self

    
    def reverse_operate(self, *arg, **kw):
        return self


_NO_OBJECT = _NoObject()
_EXPIRED_OBJECT = _ExpiredObject()

class _EvaluatorCompiler:
    
    def __init__(self, target_cls = (None,)):
        self.target_cls = target_cls

    
    def process(self, clause, *clauses):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_grouping(self, clause):
        return self.process(clause.element)

    
    def visit_null(self, clause):
        return (lambda obj: pass)

    
    def visit_false(self, clause):
        return (lambda obj: False)

    
    def visit_true(self, clause):
        return (lambda obj: True)

    
    def visit_column(self, clause):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_tuple(self, clause):
        return self.visit_clauselist(clause)

    
    def visit_expression_clauselist(self, clause):
        return self.visit_clauselist(clause)

    
    def visit_clauselist(self, clause):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_binary(self, clause):
        eval_left = self.process(clause.left)
        eval_right = self.process(clause.right)
        dispatch = f'''visit_{clause.operator.__name__.rstrip('_')}_binary_op'''
        meth = getattr(self, dispatch, None)
        if meth:
            return meth(clause.operator, eval_left, eval_right, clause)
        raise None(f'''Cannot evaluate {type(clause).__name__} with operator {clause.operator}''')

    
    def visit_or_clauselist_op(self, operator, evaluators, clause):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_and_clauselist_op(self, operator, evaluators, clause):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_comma_op_clauselist_op(self, operator, evaluators, clause):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_custom_op_binary_op(self, operator, eval_left, eval_right, clause):
        if operator.python_impl:
            return self._straight_evaluate(operator, eval_left, eval_right, clause)
        raise None(f'''Custom operator {operator.opstring!r} can\'t be evaluated in Python unless it specifies a callable using `.python_impl`.''')

    
    def visit_is_binary_op(self, operator, eval_left, eval_right, clause):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_is_not_binary_op(self, operator, eval_left, eval_right, clause):
        pass
    # WARNING: Decompyle incomplete

    
    def _straight_evaluate(self, operator, eval_left, eval_right, clause):
        pass
    # WARNING: Decompyle incomplete

    
    def _straight_evaluate_numeric_only(self, operator, eval_left, eval_right, clause):
        if clause.left.type._type_affinity not in (Numeric, Integer) or clause.right.type._type_affinity not in (Numeric, Integer):
            raise UnevaluatableError(f'''Cannot evaluate math operator "{operator.__name__}" for datatypes {clause.left.type}, {clause.right.type}''')
        return self._straight_evaluate(operator, eval_left, eval_right, clause)

    visit_add_binary_op = _straight_evaluate_numeric_only
    visit_mul_binary_op = _straight_evaluate_numeric_only
    visit_sub_binary_op = _straight_evaluate_numeric_only
    visit_mod_binary_op = _straight_evaluate_numeric_only
    visit_truediv_binary_op = _straight_evaluate_numeric_only
    visit_lt_binary_op = _straight_evaluate
    visit_le_binary_op = _straight_evaluate
    visit_ne_binary_op = _straight_evaluate
    visit_gt_binary_op = _straight_evaluate
    visit_ge_binary_op = _straight_evaluate
    visit_eq_binary_op = _straight_evaluate
    
    def visit_in_op_binary_op(self, operator, eval_left, eval_right, clause):
        return self._straight_evaluate((lambda a, b: a in b if a is not _NO_OBJECT else None), eval_left, eval_right, clause)

    
    def visit_not_in_op_binary_op(self, operator, eval_left, eval_right, clause):
        return self._straight_evaluate((lambda a, b: a not in b if a is not _NO_OBJECT else None), eval_left, eval_right, clause)

    
    def visit_concat_op_binary_op(self, operator, eval_left, eval_right, clause):
        if not issubclass(clause.left.type._type_affinity, Concatenable) or issubclass(clause.right.type._type_affinity, Concatenable):
            raise UnevaluatableError(f'''Cannot evaluate concatenate operator "{operator.__name__}" for datatypes {clause.left.type}, {clause.right.type}''')
        return self._straight_evaluate((lambda a, b: a + b), eval_left, eval_right, clause)

    
    def visit_startswith_op_binary_op(self, operator, eval_left, eval_right, clause):
        return self._straight_evaluate((lambda a, b: a.startswith(b)), eval_left, eval_right, clause)

    
    def visit_endswith_op_binary_op(self, operator, eval_left, eval_right, clause):
        return self._straight_evaluate((lambda a, b: a.endswith(b)), eval_left, eval_right, clause)

    
    def visit_unary(self, clause):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_bindparam(self, clause):
        pass
    # WARNING: Decompyle incomplete



def __getattr__(name = None):
    if name == 'EvaluatorCompiler':
        warn_deprecated("Direct use of 'EvaluatorCompiler' is not supported, and this name will be removed in a future release.  '_EvaluatorCompiler' is for internal use only", '2.0')
        return _EvaluatorCompiler
    raise None(f'''module {__name__!r} has no attribute {name!r}''')
