# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session.pyc (Python 3.11)

'''Provides the Session class and related utilities.'''
from __future__ import annotations
import contextlib
from enum import Enum
import itertools
import sys
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import weakref
from  import attributes
from  import bulk_persistence
from  import context
from  import descriptor_props
from  import exc
from  import identity
from  import loading
from  import query
from  import state as statelib
from _typing import _O
from _typing import insp_is_mapper
from _typing import is_composite_class
from _typing import is_orm_option
from _typing import is_user_defined_option
from base import _class_to_mapper
from base import _none_set
from base import _state_mapper
from base import instance_str
from base import LoaderCallableStatus
from base import object_mapper
from base import object_state
from base import PassiveFlag
from base import state_str
from context import FromStatement
from context import ORMCompileState
from identity import IdentityMap
from query import Query
from state import InstanceState
from state_changes import _StateChange
from state_changes import _StateChangeState
from state_changes import _StateChangeStates
from unitofwork import UOWTransaction
from  import engine
from  import exc as sa_exc
from  import sql
from  import util
from engine import Connection
from engine import Engine
from engine.util import TransactionalContext
from event import dispatcher
from event import EventTarget
from inspection import inspect
from inspection import Inspectable
from sql import coercions
from sql import dml
from sql import roles
from sql import Select
from sql import TableClause
from sql import visitors
from sql.base import _NoArg
from sql.base import CompileState
from sql.schema import Table
from sql.selectable import ForUpdateArg
from sql.selectable import LABEL_STYLE_TABLENAME_PLUS_COL
from util import IdentitySet
from util.typing import Literal
from util.typing import Protocol
if typing.TYPE_CHECKING:
    from _typing import _EntityType
    from _typing import _IdentityKeyType
    from _typing import _InstanceDict
    from _typing import OrmExecuteOptionsParameter
    from interfaces import ORMOption
    from interfaces import UserDefinedOption
    from mapper import Mapper
    from path_registry import PathRegistry
    from query import RowReturningQuery
    from engine import Result
    from engine import Row
    from engine import RowMapping
    from engine.base import Transaction
    from engine.base import TwoPhaseTransaction
    from engine.interfaces import _CoreAnyExecuteParams
    from engine.interfaces import _CoreSingleExecuteParams
    from engine.interfaces import _ExecuteOptions
    from engine.interfaces import CoreExecuteOptionsParameter
    from engine.result import ScalarResult
    from event import _InstanceLevelDispatch
    from sql._typing import _ColumnsClauseArgument
    from sql._typing import _InfoType
    from sql._typing import _T0
    from sql._typing import _T1
    from sql._typing import _T2
    from sql._typing import _T3
    from sql._typing import _T4
    from sql._typing import _T5
    from sql._typing import _T6
    from sql._typing import _T7
    from sql._typing import _TypedColumnClauseArgument as _TCCA
    from sql.base import Executable
    from sql.base import ExecutableOption
    from sql.elements import ClauseElement
    from sql.roles import TypedColumnsClauseRole
    from sql.selectable import ForUpdateParameter
    from sql.selectable import TypedReturnsRows
_T = TypeVar('_T', bound = Any)
__all__ = [
    'Session',
    'SessionTransaction',
    'sessionmaker',
    'ORMExecuteState',
    'close_all_sessions',
    'make_transient',
    'make_transient_to_detached',
    'object_session']
_sessions: 'weakref.WeakValueDictionary[int, Session]' = weakref.WeakValueDictionary()
statelib._sessions = _sessions
_PKIdentityArgument = Union[(Any, Tuple[(Any, ...)])]
_BindArguments = Dict[(str, Any)]
_EntityBindKey = Union[(Type[_O], 'Mapper[_O]')]
_SessionBindKey = Union[(Type[Any], 'Mapper[Any]', 'TableClause', str)]
_SessionBind = Union[('Engine', 'Connection')]
JoinTransactionMode = Literal[('conditional_savepoint', 'rollback_only', 'control_fully', 'create_savepoint')]

class _ConnectionCallableProto(Protocol):
    """a callable that returns a :class:`.Connection` given an instance.

    This callable, when present on a :class:`.Session`, is called only from the
    ORM's persistence mechanism (i.e. the unit of work flush process) to allow
    for connection-per-instance schemes (i.e. horizontal sharding) to be used
    as persistence time.

    This callable is not present on a plain :class:`.Session`, however
    is established when using the horizontal sharding extension.

    """
    
    def __call__(self = None, mapper = None, instance = None, **kw):
        pass



def _state_session(state = None):
    '''Given an :class:`.InstanceState`, return the :class:`.Session`
    associated, if any.
    '''
    return state.session


class _SessionClassMethods:
    '''Class-level methods for :class:`.Session`, :class:`.sessionmaker`.'''
    close_all = (lambda cls = None: close_all_sessions())()()
    identity_key = (lambda cls = None, class_ = None, ident = classmethod, *, instance, row, identity_token: util.preloaded.orm_util.identity_key(class_, ident, instance = instance, row = row, identity_token = identity_token))()()
    object_session = (lambda cls = None, instance = None: object_session(instance))()


class SessionTransactionState(_StateChangeState):
    ACTIVE = 1
    PREPARED = 2
    COMMITTED = 3
    DEACTIVE = 4
    CLOSED = 5
    PROVISIONING_CONNECTION = 6

(ACTIVE, PREPARED, COMMITTED, DEACTIVE, CLOSED, PROVISIONING_CONNECTION) = tuple(SessionTransactionState)

class ORMExecuteState(util.MemoizedSlots):
    '''Represents a call to the :meth:`_orm.Session.execute` method, as passed
    to the :meth:`.SessionEvents.do_orm_execute` event hook.

    .. versionadded:: 1.4

    .. seealso::

        :ref:`session_execute_events` - top level documentation on how
        to use :meth:`_orm.SessionEvents.do_orm_execute`

    '''
    _update_execution_options: 'Optional[_ExecuteOptions]' = ('session', 'statement', 'parameters', 'execution_options', 'local_execution_options', 'bind_arguments', 'identity_token', '_compile_state_cls', '_starting_event_idx', '_events_todo', '_update_execution_options')
    
    def __init__(self, session, statement, parameters, execution_options = None, bind_arguments = None, compile_state_cls = None, events_todo = ('session', 'Session', 'statement', 'Executable', 'parameters', 'Optional[_CoreAnyExecuteParams]', 'execution_options', '_ExecuteOptions', 'bind_arguments', '_BindArguments', 'compile_state_cls', 'Optional[Type[ORMCompileState]]', 'events_todo', 'List[_InstanceLevelDispatch[Session]]')):
        '''Construct a new :class:`_orm.ORMExecuteState`.

        this object is constructed internally.

        '''
        self.session = session
        self.statement = statement
        self.parameters = parameters
        self.local_execution_options = execution_options
        self.execution_options = statement._execution_options.union(execution_options)
        self.bind_arguments = bind_arguments
        self._compile_state_cls = compile_state_cls
        self._events_todo = list(events_todo)

    
    def _remaining_events(self = None):
        return self._events_todo[self._starting_event_idx + 1:]

    
    def invoke_statement(self = None, statement = None, params = None, execution_options = (None, None, None, None), bind_arguments = ('statement', 'Optional[Executable]', 'params', 'Optional[_CoreAnyExecuteParams]', 'execution_options', 'Optional[OrmExecuteOptionsParameter]', 'bind_arguments', 'Optional[_BindArguments]', 'return', 'Result[Any]')):
        '''Execute the statement represented by this
        :class:`.ORMExecuteState`, without re-invoking events that have
        already proceeded.

        This method essentially performs a re-entrant execution of the current
        statement for which the :meth:`.SessionEvents.do_orm_execute` event is
        being currently invoked.    The use case for this is for event handlers
        that want to override how the ultimate
        :class:`_engine.Result` object is returned, such as for schemes that
        retrieve results from an offline cache or which concatenate results
        from multiple executions.

        When the :class:`_engine.Result` object is returned by the actual
        handler function within :meth:`_orm.SessionEvents.do_orm_execute` and
        is propagated to the calling
        :meth:`_orm.Session.execute` method, the remainder of the
        :meth:`_orm.Session.execute` method is preempted and the
        :class:`_engine.Result` object is returned to the caller of
        :meth:`_orm.Session.execute` immediately.

        :param statement: optional statement to be invoked, in place of the
         statement currently represented by :attr:`.ORMExecuteState.statement`.

        :param params: optional dictionary of parameters or list of parameters
         which will be merged into the existing
         :attr:`.ORMExecuteState.parameters` of this :class:`.ORMExecuteState`.

         .. versionchanged:: 2.0 a list of parameter dictionaries is accepted
            for executemany executions.

        :param execution_options: optional dictionary of execution options
         will be merged into the existing
         :attr:`.ORMExecuteState.execution_options` of this
         :class:`.ORMExecuteState`.

        :param bind_arguments: optional dictionary of bind_arguments
         which will be merged amongst the current
         :attr:`.ORMExecuteState.bind_arguments`
         of this :class:`.ORMExecuteState`.

        :return: a :class:`_engine.Result` object with ORM-level results.

        .. seealso::

            :ref:`do_orm_execute_re_executing` - background and examples on the
            appropriate usage of :meth:`_orm.ORMExecuteState.invoke_statement`.


        '''
        pass
    # WARNING: Decompyle incomplete

    bind_mapper = (lambda self = None: mp = self.bind_arguments.get('mapper', None)mp)()
    all_mappers = (lambda self = None: if not self.is_orm_statement:
[]if None(self.statement, (Select, FromStatement)):
result = []seen = set()for d in self.statement.column_descriptions:
ent = d['entity']if ent:
insp = inspect(ent, raiseerr = False)if insp and insp.mapper and insp.mapper not in seen:
seen.add(insp.mapper)result.append(insp.mapper)resultif self.statement.is_dml and self.bind_mapper:
[
self.bind_mapper]None)()
    is_orm_statement = (lambda self = None: self._compile_state_cls is not None)()
    is_executemany = (lambda self = None: isinstance(self.parameters, list))()
    is_select = (lambda self = None: self.statement.is_select)()
    is_from_statement = (lambda self = None: self.statement.is_from_statement)()
    is_insert = (lambda self = None:
