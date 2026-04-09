# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pytables.pyc (Python 3.11)

'''manage PyTables query interface via Expressions'''
from __future__ import annotations
import ast
from decimal import Decimal, InvalidOperation
from functools import partial
from typing import TYPE_CHECKING, Any, ClassVar, Self, cast
import numpy as np
from pandas._libs import lib
from pandas._libs.tslibs import Timedelta, Timestamp
from pandas.errors import UndefinedVariableError
from pandas.core.dtypes.common import is_list_like

common
from pandas.core.computation import expr, ops, scope
ops = ops
_scope = scope
import pandas.core.common, core
from pandas.core.computation.common import ensure_decoded
from pandas.core.computation.expr import BaseExprVisitor
from pandas.core.computation.ops import is_term
from pandas.core.construction import extract_array
from pandas.core.indexes.base import Index
from pandas.io.formats.printing import pprint_thing, pprint_thing_encoded
if TYPE_CHECKING:
    from pandas._typing import TimeUnit, npt

class PyTablesScope(_scope.Scope):
    pass
# WARNING: Decompyle incomplete


class Term(ops.Term):
    pass
# WARNING: Decompyle incomplete


class Constant(Term):
    pass
# WARNING: Decompyle incomplete


class BinOp(ops.BinOp):
    pass
# WARNING: Decompyle incomplete


class FilterBinOp(BinOp):
    filter: 'tuple[Any, Any, Index] | None' = None
    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def invert(self = None):
        '''invert the filter'''
        pass
    # WARNING: Decompyle incomplete

    
    def format(self):
        '''return the actual filter format'''
        return [
            self.filter]

    
    def evaluate(self = None):
        if not self.is_valid:
            raise ValueError(f'''query term is not valid [{self}]''')
        rhs = self.conform(self.rhs)
        values = list(rhs)
        if self.is_in_table:
            if self.op in ('==', '!=') and len(values) > self._max_selectors:
                filter_op = self.generate_filter_op()
                self.filter = (self.lhs, filter_op, Index(values))
                return self
            return None
        if None.op in ('==', '!='):
            filter_op = self.generate_filter_op()
            self.filter = (self.lhs, filter_op, Index(values))
        else:
            raise TypeError(f'''passing a filterable condition to a non-table indexer [{self}]''')
        return self

    
    def generate_filter_op(self = None, invert = None):
