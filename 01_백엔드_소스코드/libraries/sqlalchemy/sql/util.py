# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

'''High level utilities which build upon other modules here.'''
from __future__ import annotations
from collections import deque
import copy
from itertools import chain
import typing
from typing import AbstractSet
from typing import Any
from typing import Callable
from typing import cast
from typing import Collection
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import coercions
from  import operators
from  import roles
from  import visitors
from _typing import is_text_clause
from annotation import _deep_annotate
from annotation import _deep_deannotate
from annotation import _shallow_annotate
from base import _expand_cloned
from base import _from_objects
from cache_key import HasCacheKey
from ddl import sort_tables
from elements import _find_columns
from elements import _label_reference
from elements import _textual_label_reference
from elements import BindParameter
from elements import ClauseElement
from elements import ColumnClause
from elements import ColumnElement
from elements import Grouping
from elements import KeyedColumnElement
from elements import Label
from elements import NamedColumn
from elements import Null
from elements import UnaryExpression
from schema import Column
from selectable import Alias
from selectable import FromClause
from selectable import FromGrouping
from selectable import Join
from selectable import ScalarSelect
from selectable import SelectBase
from selectable import TableClause
from visitors import _ET
from  import exc
from  import util
from util.typing import Literal
from util.typing import Protocol
if typing.TYPE_CHECKING:
    from _typing import _EquivalentColumnMap
    from _typing import _LimitOffsetType
    from _typing import _TypeEngineArgument
    from elements import BinaryExpression
    from elements import TextClause
    from selectable import _JoinTargetElement
    from selectable import _SelectIterable
    from selectable import Selectable
    from visitors import _TraverseCallableType
    from visitors import ExternallyTraversible
    from visitors import ExternalTraversal
    from engine.interfaces import _AnyExecuteParams
    from engine.interfaces import _AnyMultiExecuteParams
    from engine.interfaces import _AnySingleExecuteParams
    from engine.interfaces import _CoreSingleExecuteParams
    from engine.row import Row
_CE = TypeVar('_CE', bound = 'ColumnElement[Any]')

def join_condition(a = None, b = None, a_subset = None, consider_as_foreign_keys = (None, None)):
    '''Create a join condition between two tables or selectables.

    e.g.::

        join_condition(tablea, tableb)

    would produce an expression along the lines of::

        tablea.c.id == tableb.c.tablea_id

    The join is determined based on the foreign key relationships
    between the two selectables.   If there are multiple ways
    to join, or no way to join, an error is raised.

    :param a_subset: An optional expression that is a sub-component
        of ``a``.  An attempt will be made to join to just this sub-component
        first before looking at the full ``a`` construct, and if found
        will be successful even if there are other ways to join to ``a``.
        This allows the "right side" of a join to be passed thereby
        providing a "natural join".

    '''
    return Join._join_condition(a, b, a_subset = a_subset, consider_as_foreign_keys = consider_as_foreign_keys)


def find_join_source(clauses = None, join_to = None):
    '''Given a list of FROM clauses and a selectable,
    return the first index and element from the list of
    clauses which can be joined against the selectable.  returns
    None, None if no match is found.

    e.g.::

        clause1 = table1.join(table2)
        clause2 = table4.join(table5)

        join_to = table2.join(table3)

        find_join_source([clause1, clause2], join_to) == clause1

    '''
    selectables = list(_from_objects(join_to))
    idx = []
    for i, f in enumerate(clauses):
        for s in selectables:
            if f.is_derived_from(s):
                idx.append(i)
        return idx


def find_left_clause_that_matches_given(clauses = None, join_from = None):
    '''Given a list of FROM clauses and a selectable,
    return the indexes from the list of
    clauses which is derived from the selectable.

    '''
    selectables = list(_from_objects(join_from))
    liberal_idx = []
    for i, f in enumerate(clauses):
        for s in selectables:
            if f.is_derived_from(s):
                liberal_idx.append(i)
            
            if len(liberal_idx) > 1:
                conservative_idx = []
                for idx in liberal_idx:
                    f = clauses[idx]
                    for s in selectables:
                        if set(surface_selectables(f)).intersection(surface_selectables(s)):
                            conservative_idx.append(idx)
                        
                        if conservative_idx:
                            return conservative_idx
                        return None


def find_left_clause_to_join_from(clauses = None, join_to = None, onclause = None):
    '''Given a list of FROM clauses, a selectable,
    and optional ON clause, return a list of integer indexes from the
    clauses list indicating the clauses that can be joined from.

    The presence of an "onclause" indicates that at least one clause can
    definitely be joined from; if the list of clauses is of length one
    and the onclause is given, returns that index.   If the list of clauses
    is more than length one, and the onclause is given, attempts to locate
    which clauses contain the same columns.

    '''
    pass
# WARNING: Decompyle incomplete


def visit_binary_product(fn = None, expr = None):
    '''Produce a traversal of the given expression, delivering
    column comparisons to the given function.

    The function is of the form::

        def my_fn(binary, left, right): ...

    For each binary expression located which has a
    comparison operator, the product of "left" and
    "right" will be delivered to that function,
    in terms of that binary.

    Hence an expression like::

        and_((a + b) == q + func.sum(e + f), j == r)

    would have the traversal:

    .. sourcecode:: text

        a <eq> q
        a <eq> e
        a <eq> f
        b <eq> q
        b <eq> e
        b <eq> f
        j <eq> r

    That is, every combination of "left" and
    "right" that doesn\'t further contain
    a binary comparison is passed as pairs.

    '''
    pass
# WARNING: Decompyle incomplete


def find_tables(clause = None, *, check_columns, include_aliases, include_joins, include_selects, include_crud):
    '''locate Table objects within the given expression.'''
    pass
# WARNING: Decompyle incomplete


def unwrap_order_by(clause = None):
    """Break up an 'order by' expression into individual column-expressions,
    without DESC/ASC/NULLS FIRST/NULLS LAST"""
    cols = util.column_set()
    result = []
    stack = deque([
        clause])
# WARNING: Decompyle incomplete


def unwrap_label_reference(element):
    
    def replace(element = None, **kw):
        if isinstance(element, _label_reference):
            return element.element
    # WARNING: Decompyle incomplete

    return visitors.replacement_traverse(element, { }, replace)


def expand_column_list_from_order_by(collist, order_by):
    '''Given the columns clause and ORDER BY of a selectable,
    return a list of column expressions that can be added to the collist
    corresponding to the ORDER BY, without repeating those already
    in the collist.

    '''
    pass
# WARNING: Decompyle incomplete


def clause_is_present(clause, search):
    '''Given a target clause and a second to search within, return True
    if the target is plainly present in the search without any
    subqueries or aliases involved.

    Basically descends through Joins.

    '''
    for elem in surface_selectables(search):
        if clause == elem:
            return True
        return False


def tables_from_leftmost(clause = None):
    pass
# WARNING: Decompyle incomplete


def surface_selectables(clause):
    pass
# WARNING: Decompyle incomplete


def surface_selectables_only(clause = None):
    pass
# WARNING: Decompyle incomplete


def extract_first_column_annotation(column, annotation_name):
    filter_ = (FromGrouping, SelectBase)
    stack = deque([
        column])
# WARNING: Decompyle incomplete


def selectables_overlap(left = None, right = None):
    '''Return True if left/right have some overlapping selectable'''
    return bool(set(surface_selectables(left)).intersection(surface_selectables(right)))


def bind_values(clause):
    '''Return an ordered list of "bound" values in the given clause.

    E.g.::

        >>> expr = and_(table.c.foo == 5, table.c.foo == 7)
        >>> bind_values(expr)
        [5, 7]
    '''
    pass
# WARNING: Decompyle incomplete


def _quote_ddl_expr(element):
    if isinstance(element, str):
        element = element.replace("'", "''")
        return "'%s'" % element
    return None(element)


class _repr_base:
    _LIST: 'int' = 0
    _TUPLE: 'int' = 1
    _DICT: 'int' = 2
    max_chars: 'int' = ('max_chars',)
    
    def trunc(self = None, value = None):
        rep = repr(value)
        lenrep = len(rep)
        if lenrep > self.max_chars:
            segment_length = self.max_chars // 2
            rep = rep[0:segment_length] + ' ... (%d characters truncated) ... ' % (lenrep - self.max_chars) + rep[-segment_length:]
        return rep



def _repr_single_value(value):
    rp = _repr_base()
    rp.max_chars = 300
    return rp.trunc(value)


class _repr_row(_repr_base):
    '''Provide a string view of a row.'''
    __slots__ = ('row',)
    
    def __init__(self = None, row = None, max_chars = None):
        self.row = row
        self.max_chars = max_chars

    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete



class _long_statement(str):
    
    def __str__(self = None):
        lself = len(self)
        if lself > 500:
            lleft = 250
            lright = 100
            trunc = lself - lleft - lright
            return f'''{self[0:lleft]} ... {trunc} characters truncated ... {self[-lright:]}'''
        return None.__str__(self)



class _repr_params(_repr_base):
    """Provide a string view of bound parameters.

    Truncates display to a given number of 'multi' parameter sets,
    as well as long values to a given number of characters.

    """
    __slots__ = ('params', 'batches', 'ismulti', 'max_params')
    
    def __init__(self, params = None, batches = None, max_params = None, max_chars = (100, 300, None), ismulti = ('params', 'Optional[_AnyExecuteParams]', 'batches', 'int', 'max_params', 'int', 'max_chars', 'int', 'ismulti', 'Optional[bool]')):
        self.params = params
        self.ismulti = ismulti
        self.batches = batches
        self.max_chars = max_chars
        self.max_params = max_params

    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _repr_multi(self = None, multi_params = None, typ = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_batches(self = None, params = None):
        lparams = list(params)
        lenparams = len(lparams)
        if lenparams > self.max_params:
            lleft = self.max_params // 2
            return (lparams[0:lleft], lparams[-lleft:], lenparams - self.max_params)
        return (None, None, None)

    
    def _repr_params(self = None, params = None, typ = None):
        if typ is self._DICT:
            return self._repr_param_dict(cast('_CoreSingleExecuteParams', params))
        if None is self._TUPLE:
            return self._repr_param_tuple(cast('Sequence[Any]', params))
        return None._repr_param_list(params)

    
    def _repr_param_dict(self = None, params = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _repr_param_tuple(self = None, params = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _repr_param_list(self = None, params = None):
        pass
    # WARNING: Decompyle incomplete



def adapt_criterion_to_null(crit = None, nulls = None):
    '''given criterion containing bind params, convert selected elements
    to IS NULL.

    '''
    pass
# WARNING: Decompyle incomplete


def splice_joins(left = None, right = None, stop_on = None):
    pass
# WARNING: Decompyle incomplete

reduce_columns = (lambda columns = None: pass)()
reduce_columns = (lambda columns = None: pass)()

def reduce_columns(columns = None, *clauses, **kw):
    '''given a list of columns, return a \'reduced\' set based on natural
    equivalents.

    the set is reduced to the smallest list of columns which have no natural
    equivalent present in the list.  A "natural equivalent" means that two
    columns will ultimately represent the same value because they are related
    by a foreign key.

    \\*clauses is an optional list of join clauses which will be traversed
    to further identify columns that are "equivalent".

    \\**kw may specify \'ignore_nonexistent_tables\' to ignore foreign keys
    whose tables are not yet configured, or columns that aren\'t yet present.

    This function is primarily used to determine the most minimal "primary
    key" from a selectable, by reducing the set of primary key columns present
    in the selectable to just those that are not repeated.

    '''
    pass
# WARNING: Decompyle incomplete


def criterion_as_pairs(expression, consider_as_foreign_keys, consider_as_referenced_keys, any_operator = (None, None, False)):
    '''traverse an expression and locate binary criterion pairs.'''
    pass
# WARNING: Decompyle incomplete


class ClauseAdapter(visitors.ReplacingExternalTraversal):
    '''Clones and modifies clauses based on column correspondence.

    E.g.::

      table1 = Table(
          "sometable",
          metadata,
          Column("col1", Integer),
          Column("col2", Integer),
      )
      table2 = Table(
          "someothertable",
          metadata,
          Column("col1", Integer),
          Column("col2", Integer),
      )

      condition = table1.c.col1 == table2.c.col1

    make an alias of table1::

      s = table1.alias("foo")

    calling ``ClauseAdapter(s).traverse(condition)`` converts
    condition to read::

      s.c.col1 == table2.c.col1

    '''
    __slots__ = ('__traverse_options__', 'selectable', 'include_fn', 'exclude_fn', 'equivalents', 'adapt_on_names', 'adapt_from_selectables')
    
    def __init__(self, selectable, equivalents, include_fn = None, exclude_fn = None, adapt_on_names = None, anonymize_labels = (None, None, None, False, False, None), adapt_from_selectables = ('selectable', 'Selectable', 'equivalents', 'Optional[_EquivalentColumnMap]', 'include_fn', 'Optional[Callable[[ClauseElement], bool]]', 'exclude_fn', 'Optional[Callable[[ClauseElement], bool]]', 'adapt_on_names', 'bool', 'anonymize_labels', 'bool', 'adapt_from_selectables', 'Optional[AbstractSet[FromClause]]')):
