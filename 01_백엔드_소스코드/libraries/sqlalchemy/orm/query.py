# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: query.pyc (Python 3.11)

'''The Query class and support.

Defines the :class:`_query.Query` class, the central
construct used by the ORM to construct database queries.

The :class:`_query.Query` class should not be confused with the
:class:`_expression.Select` class, which defines database
SELECT operations at the SQL (non-ORM) level.  ``Query`` differs from
``Select`` in that it returns ORM-mapped objects and interacts with an
ORM session, whereas the ``Select`` construct interacts directly with the
database to return iterable result sets.

'''
from __future__ import annotations
from collections.abc import abc as collections_abc
import operator
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import attributes
from  import interfaces
from  import loading
from  import util as orm_util
from _typing import _O
from base import _assertions
from context import _column_descriptions
from context import _determine_last_joined_entity
from context import _legacy_filter_by_entity_zero
from context import FromStatement
from context import ORMCompileState
from context import QueryContext
from interfaces import ORMColumnDescription
from interfaces import ORMColumnsClauseRole
from util import AliasedClass
from util import object_mapper
from util import with_parent
from  import exc as sa_exc
from  import inspect
from  import inspection
from  import log
from  import sql
from  import util
from engine import Result
from engine import Row
from event import dispatcher
from event import EventTarget
from sql import coercions
from sql import expression
from sql import roles
from sql import Select
from sql import util as sql_util
from sql import visitors
from sql._typing import _FromClauseArgument
from sql._typing import _TP
from sql.annotation import SupportsCloneAnnotations
from sql.base import _entity_namespace_key
from sql.base import _generative
from sql.base import _NoArg
from sql.base import Executable
from sql.base import Generative
from sql.elements import BooleanClauseList
from sql.expression import Exists
from sql.selectable import _MemoizedSelectEntities
from sql.selectable import _SelectFromElements
from sql.selectable import ForUpdateArg
from sql.selectable import HasHints
from sql.selectable import HasPrefixes
from sql.selectable import HasSuffixes
from sql.selectable import LABEL_STYLE_TABLENAME_PLUS_COL
from sql.selectable import SelectLabelStyle
from util.typing import Literal
from util.typing import Self
if TYPE_CHECKING:
    from _typing import _EntityType
    from _typing import _ExternalEntityType
    from _typing import _InternalEntityType
    from _typing import SynchronizeSessionArgument
    from mapper import Mapper
    from path_registry import PathRegistry
    from session import _PKIdentityArgument
    from session import Session
    from state import InstanceState
    from engine.cursor import CursorResult
    from engine.interfaces import _ImmutableExecuteOptions
    from engine.interfaces import CompiledCacheType
    from engine.interfaces import IsolationLevel
    from engine.interfaces import SchemaTranslateMapType
    from engine.result import FrozenResult
    from engine.result import ScalarResult
    from sql._typing import _ColumnExpressionArgument
    from sql._typing import _ColumnExpressionOrStrLabelArgument
    from sql._typing import _ColumnsClauseArgument
    from sql._typing import _DMLColumnArgument
    from sql._typing import _JoinTargetArgument
    from sql._typing import _LimitOffsetType
    from sql._typing import _MAYBE_ENTITY
    from sql._typing import _no_kw
    from sql._typing import _NOT_ENTITY
    from sql._typing import _OnClauseArgument
    from sql._typing import _PropagateAttrsType
    from sql._typing import _T0
    from sql._typing import _T1
    from sql._typing import _T2
    from sql._typing import _T3
    from sql._typing import _T4
    from sql._typing import _T5
    from sql._typing import _T6
    from sql._typing import _T7
    from sql._typing import _TypedColumnClauseArgument as _TCCA
    from sql.base import CacheableOptions
    from sql.base import ExecutableOption
    from sql.dml import UpdateBase
    from sql.elements import ColumnElement
    from sql.elements import Label
    from sql.selectable import _ForUpdateOfArgument
    from sql.selectable import _JoinTargetElement
    from sql.selectable import _SetupJoinsElement
    from sql.selectable import Alias
    from sql.selectable import CTE
    from sql.selectable import ExecutableReturnsRows
    from sql.selectable import FromClause
    from sql.selectable import ScalarSelect
    from sql.selectable import Subquery
__all__ = [
    'Query',
    'QueryContext']
_T = TypeVar('_T', bound = Any)

def Query():
    '''Query'''
    __doc__ = 'ORM-level SQL construction object.\n\n    .. legacy:: The ORM :class:`.Query` object is a legacy construct\n       as of SQLAlchemy 2.0.   See the notes at the top of\n       :ref:`query_api_toplevel` for an overview, including links to migration\n       documentation.\n\n    :class:`_query.Query` objects are normally initially generated using the\n    :meth:`~.Session.query` method of :class:`.Session`, and in\n    less common cases by instantiating the :class:`_query.Query` directly and\n    associating with a :class:`.Session` using the\n    :meth:`_query.Query.with_session`\n    method.\n\n    '
    _where_criteria: 'Tuple[ColumnElement[Any], ...]' = ()
    _having_criteria: 'Tuple[ColumnElement[Any], ...]' = ()
    _order_by_clauses: 'Tuple[ColumnElement[Any], ...]' = ()
    _group_by_clauses: 'Tuple[ColumnElement[Any], ...]' = ()
    _limit_clause: 'Optional[ColumnElement[Any]]' = None
    _offset_clause: 'Optional[ColumnElement[Any]]' = None
    _distinct: 'bool' = False
    _distinct_on: 'Tuple[ColumnElement[Any], ...]' = ()
    _for_update_arg: 'Optional[ForUpdateArg]' = None
    _correlate: 'Tuple[FromClause, ...]' = ()
    _auto_correlate: 'bool' = True
    _from_obj: 'Tuple[FromClause, ...]' = ()
    _setup_joins: 'Tuple[_SetupJoinsElement, ...]' = ()
    _label_style: 'SelectLabelStyle' = SelectLabelStyle.LABEL_STYLE_LEGACY_ORM
    _memoized_select_entities = ()
    _with_options: 'Tuple[ExecutableOption, ...]' = ORMCompileState.default_compile_options
    load_options = QueryContext.default_load_options + {
        '_legacy_uniquing': True }
    _params: 'util.immutabledict[str, Any]' = util.EMPTY_DICT
    _enable_assertions = True
    dispatch: 'dispatcher[Query[_T]]' = None
    _propagate_attrs = (lambda self = None: util.EMPTY_DICT)()
    
    def __init__(self = None, entities = None, session = None):
        '''Construct a :class:`_query.Query` directly.

        E.g.::

            q = Query([User, Address], session=some_session)

        The above is equivalent to::

            q = some_session.query(User, Address)

        :param entities: a sequence of entities and/or SQL expressions.

        :param session: a :class:`.Session` with which the
         :class:`_query.Query`
         will be associated.   Optional; a :class:`_query.Query`
         can be associated
         with a :class:`.Session` generatively via the
         :meth:`_query.Query.with_session` method as well.

        .. seealso::

            :meth:`.Session.query`

            :meth:`_query.Query.with_session`

        '''
        self.session = session
        self._set_entities(entities)

    
    def _set_propagate_attrs(self = None, values = None):
        self._propagate_attrs = util.immutabledict(values)
        return self

    
    def _set_entities(self = None, entities = None):
        pass
    # WARNING: Decompyle incomplete

    
    def tuples(self = None):
        '''return a tuple-typed form of this :class:`.Query`.

        This method invokes the :meth:`.Query.only_return_tuples`
        method with a value of ``True``, which by itself ensures that this
        :class:`.Query` will always return :class:`.Row` objects, even
        if the query is made against a single entity.  It then also
        at the typing level will return a "typed" query, if possible,
        that will type result rows as ``Tuple`` objects with typed
        elements.

        This method can be compared to the :meth:`.Result.tuples` method,
        which returns "self", but from a typing perspective returns an object
        that will yield typed ``Tuple`` objects for results.   Typing
        takes effect only if this :class:`.Query` object is a typed
        query object already.

        .. versionadded:: 2.0

        .. seealso::

            :meth:`.Result.tuples` - v2 equivalent method.

        '''
        return self.only_return_tuples(True)

    
    def _entity_from_pre_ent_zero(self = None):
        if not self._raw_columns:
            return None
        ent = None._raw_columns[0]
        if 'parententity' in ent._annotations:
            return ent._annotations['parententity']
        if None in ent._annotations:
            return ent._annotations['bundle']
        for element in None.iterate(ent):
            if 'parententity' in element._annotations:
                
                return None, element._annotations['parententity']
            return None

    
    def _only_full_mapper_zero(self = None, methname = None):
        if not len(self._raw_columns) != 1 and 'parententity' not in self._raw_columns[0]._annotations or self._raw_columns[0].is_selectable:
            raise sa_exc.InvalidRequestError('%s() can only be used against a single mapped class.' % methname)
        return self._raw_columns[0]._annotations['parententity']

    
    def _set_select_from(self = None, obj = None, set_base_alias = None):
        pass
    # WARNING: Decompyle incomplete

    _set_lazyload_from = (lambda self = None, state = None: self)()
    
    def _get_condition(self = None):
        '''used by legacy BakedQuery'''
        self._no_criterion_condition('get', order_by = False, distinct = False)

    
    def _get_existing_condition(self = None):
        self._no_criterion_assertion('get', order_by = False, distinct = False)

    
    def _no_criterion_assertion(self = None, meth = None, order_by = None, distinct = (True, True)):
        if not self._enable_assertions:
            return None
    # WARNING: Decompyle incomplete

    
    def _no_criterion_condition(self = None, meth = None, order_by = None, distinct = (True, True)):
        self._no_criterion_assertion(meth, order_by, distinct)
        self._from_obj = ()
        self._setup_joins = ()
    # WARNING: Decompyle incomplete

    
    def _no_clauseelement_condition(self = None, meth = None):
        if not self._enable_assertions:
            return None
        if None._order_by_clauses:
            raise sa_exc.InvalidRequestError('Query.%s() being called on a Query with existing criterion. ' % meth)
        self._no_criterion_condition(meth)

    
    def _no_statement_condition(self = None, meth = None):
        if not self._enable_assertions:
            return None
    # WARNING: Decompyle incomplete

    
    def _no_limit_offset(self = None, meth = None):
        if not self._enable_assertions:
            return None
    # WARNING: Decompyle incomplete

    _has_row_limiting_clause = (lambda self = None:
