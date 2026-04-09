# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: events.pyc (Python 3.11)

'''ORM event interfaces.'''
from __future__ import annotations
from typing import Any
from typing import Callable
from typing import Collection
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import weakref
from  import instrumentation
from  import interfaces
from  import mapperlib
from attributes import QueryableAttribute
from base import _mapper_or_none
from base import NO_KEY
from instrumentation import ClassManager
from instrumentation import InstrumentationFactory
from query import BulkDelete
from query import BulkUpdate
from query import Query
from scoping import scoped_session
from session import Session
from session import sessionmaker
from  import event
from  import exc
from  import util
from event import EventTarget
from event.registry import _ET
from util.compat import inspect_getfullargspec
if TYPE_CHECKING:
    from weakref import ReferenceType
    from _typing import _InstanceDict
    from _typing import _InternalEntityType
    from _typing import _O
    from _typing import _T
    from attributes import Event
    from base import EventConstants
    from session import ORMExecuteState
    from session import SessionTransaction
    from unitofwork import UOWTransaction
    from engine import Connection
    from event.base import _Dispatch
    from event.base import _HasEventsDispatch
    from event.registry import _EventKey
    from orm.collections import CollectionAdapter
    from orm.context import QueryContext
    from orm.decl_api import DeclarativeAttributeIntercept
    from orm.decl_api import DeclarativeMeta
    from orm.mapper import Mapper
    from orm.state import InstanceState
_KT = TypeVar('_KT', bound = Any)
_ET2 = TypeVar('_ET2', bound = EventTarget)

def InstrumentationEvents():
    '''InstrumentationEvents'''
    pass
# WARNING: Decompyle incomplete

InstrumentationEvents = <NODE:27>(InstrumentationEvents, 'InstrumentationEvents', event.Events[InstrumentationFactory])

class _InstrumentationEventsHold:
    '''temporary marker object used to transfer from _accept_with() to
    _listen() on the InstrumentationEvents class.

    '''
    
    def __init__(self = None, class_ = None):
        self.class_ = class_

    dispatch = event.dispatcher(InstrumentationEvents)


def InstanceEvents():
    '''InstanceEvents'''
    pass
# WARNING: Decompyle incomplete

InstanceEvents = <NODE:27>(InstanceEvents, 'InstanceEvents', event.Events[ClassManager[Any]])

def _EventsHold():
    '''_EventsHold'''
    all_holds: 'weakref.WeakKeyDictionary[Any, Any]' = "Hold onto listeners against unmapped, uninstrumented classes.\n\n    Establish _listen() for that class' mapper/instrumentation when\n    those objects are created for that class.\n\n    "
    
    def __init__(self = None, class_ = None):
        self.class_ = class_

    _clear = (lambda cls = None: cls.all_holds.clear())()
    
    def HoldEvents():
        '''_EventsHold.HoldEvents'''
        _dispatch_target: 'Optional[Type[_ET2]]' = None
        _listen = (lambda cls = None, event_key = None, raw = classmethod, propagate = (False, False, False), retval = ('event_key', '_EventKey[_ET2]', 'raw', 'bool', 'propagate', 'bool', 'retval', 'bool', 'kw', 'Any', 'return', 'None'): target = event_key.dispatch_targetif target.class_ in target.all_holds:
collection = target.all_holds[target.class_]else:
collection = { }target.all_holds[target.class_] = { }event.registry._stored_in_collection(event_key, target)collection[event_key._key] = (event_key, raw, propagate, retval, kw)# WARNING: Decompyle incomplete
)()

    HoldEvents = <NODE:27>(HoldEvents, 'HoldEvents', Generic[_ET2])
    
    def remove(self = None, event_key = None):
        target = event_key.dispatch_target
        if isinstance(target, _EventsHold):
            collection = target.all_holds[target.class_]
            del collection[event_key._key]
            return None

    populate = (lambda cls = None, class_ = None, subject = classmethod: pass# WARNING: Decompyle incomplete
)()

_EventsHold = <NODE:27>(_EventsHold, '_EventsHold', event.RefCollection[_ET])

def _InstanceEventsHold():
    '''_InstanceEventsHold'''
    all_holds: 'weakref.WeakKeyDictionary[Any, Any]' = weakref.WeakKeyDictionary()
    
    def resolve(self = None, class_ = None):
        return instrumentation.opt_manager_of_class(class_)

    
    def HoldInstanceEvents():
        '''_InstanceEventsHold.HoldInstanceEvents'''
        pass

    HoldInstanceEvents = <NODE:27>(HoldInstanceEvents, 'HoldInstanceEvents', _EventsHold.HoldEvents[_ET], InstanceEvents)
    dispatch = event.dispatcher(HoldInstanceEvents)

_InstanceEventsHold = <NODE:27>(_InstanceEventsHold, '_InstanceEventsHold', _EventsHold[_ET])

def MapperEvents():
    '''MapperEvents'''
    pass
# WARNING: Decompyle incomplete

MapperEvents = <NODE:27>(MapperEvents, 'MapperEvents', event.Events[mapperlib.Mapper[Any]])

def _MapperEventsHold():
    '''_MapperEventsHold'''
    all_holds = weakref.WeakKeyDictionary()
    
    def resolve(self = None, class_ = None):
        return _mapper_or_none(class_)

    
    def HoldMapperEvents():
        '''_MapperEventsHold.HoldMapperEvents'''
        pass

    HoldMapperEvents = <NODE:27>(HoldMapperEvents, 'HoldMapperEvents', _EventsHold.HoldEvents[_ET], MapperEvents)
    dispatch = event.dispatcher(HoldMapperEvents)

_MapperEventsHold = <NODE:27>(_MapperEventsHold, '_MapperEventsHold', _EventsHold[_ET])
_sessionevents_lifecycle_event_names: 'Set[str]' = set()

def SessionEvents():
    '''SessionEvents'''
    __doc__ = 'Define events specific to :class:`.Session` lifecycle.\n\n    e.g.::\n\n        from sqlalchemy import event\n        from sqlalchemy.orm import sessionmaker\n\n\n        def my_before_commit(session):\n            print("before commit!")\n\n\n        Session = sessionmaker()\n\n        event.listen(Session, "before_commit", my_before_commit)\n\n    The :func:`~.event.listen` function will accept\n    :class:`.Session` objects as well as the return result\n    of :class:`~.sessionmaker()` and :class:`~.scoped_session()`.\n\n    Additionally, it accepts the :class:`.Session` class which\n    will apply listeners to all :class:`.Session` instances\n    globally.\n\n    :param raw=False: When True, the "target" argument passed\n       to applicable event listener functions that work on individual\n       objects will be the instance\'s :class:`.InstanceState` management\n       object, rather than the mapped instance itself.\n\n       .. versionadded:: 1.3.14\n\n    :param restore_load_context=False: Applies to the\n       :meth:`.SessionEvents.loaded_as_persistent` event.  Restores the loader\n       context of the object when the event hook is complete, so that ongoing\n       eager load operations continue to target the object appropriately.  A\n       warning is emitted if the object is moved to a new loader context from\n       within this event if this flag is not set.\n\n       .. versionadded:: 1.3.14\n\n    '
    _target_class_doc = 'SomeSessionClassOrObject'
    _dispatch_target = Session
    
    def _lifecycle_event(fn = None):
        _sessionevents_lifecycle_event_names.add(fn.__name__)
        return fn

    _accept_with = (lambda cls = None, target = None, identifier = classmethod: if isinstance(target, scoped_session):
target = target.session_factoryif not isinstance(target, sessionmaker):
if not isinstance(target, type) or issubclass(target, Session):
raise exc.ArgumentError('Session event listen on a scoped_session requires that its creation callable is associated with the Session class.')if isinstance(target, sessionmaker):
target.class_if None(target, type):
if issubclass(target, scoped_session):
Sessionif None(target, Session):
targetNoneif None(target, Session):
targetif None(target, '_no_async_engine_events'):
target._no_async_engine_events()NoneNone.Events._accept_with(target, identifier))()
    _listen = (lambda cls = None, event_key = None, *, raw, restore_load_context: pass# WARNING: Decompyle incomplete
)()
    
    def do_orm_execute(self = None, orm_execute_state = None):
        """Intercept statement executions that occur on behalf of an
        ORM :class:`.Session` object.

        This event is invoked for all top-level SQL statements invoked from the
        :meth:`_orm.Session.execute` method, as well as related methods such as
        :meth:`_orm.Session.scalars` and :meth:`_orm.Session.scalar`. As of
        SQLAlchemy 1.4, all ORM queries that run through the
        :meth:`_orm.Session.execute` method as well as related methods
        :meth:`_orm.Session.scalars`, :meth:`_orm.Session.scalar` etc.
        will participate in this event.
        This event hook does **not** apply to the queries that are
        emitted internally within the ORM flush process, i.e. the
        process described at :ref:`session_flushing`.

        .. note::  The :meth:`_orm.SessionEvents.do_orm_execute` event hook
           is triggered **for ORM statement executions only**, meaning those
           invoked via the :meth:`_orm.Session.execute` and similar methods on
           the :class:`_orm.Session` object. It does **not** trigger for
           statements that are invoked by SQLAlchemy Core only, i.e. statements
           invoked directly using :meth:`_engine.Connection.execute` or
           otherwise originating from an :class:`_engine.Engine` object without
           any :class:`_orm.Session` involved. To intercept **all** SQL
           executions regardless of whether the Core or ORM APIs are in use,
           see the event hooks at :class:`.ConnectionEvents`, such as
           :meth:`.ConnectionEvents.before_execute` and
           :meth:`.ConnectionEvents.before_cursor_execute`.

           Also, this event hook does **not** apply to queries that are
           emitted internally within the ORM flush process,
           i.e. the process described at :ref:`session_flushing`; to
           intercept steps within the flush process, see the event
           hooks described at :ref:`session_persistence_events` as
           well as :ref:`session_persistence_mapper`.

        This event is a ``do_`` event, meaning it has the capability to replace
        the operation that the :meth:`_orm.Session.execute` method normally
        performs.  The intended use for this includes sharding and
        result-caching schemes which may seek to invoke the same statement
        across  multiple database connections, returning a result that is
        merged from each of them, or which don't invoke the statement at all,
        instead returning data from a cache.

        The hook intends to replace the use of the
        ``Query._execute_and_instances`` method that could be subclassed prior
        to SQLAlchemy 1.4.

        :param orm_execute_state: an instance of :class:`.ORMExecuteState`
         which contains all information about the current execution, as well
         as helper functions used to derive other commonly required
         information.   See that object for details.

        .. seealso::

            :ref:`session_execute_events` - top level documentation on how
            to use :meth:`_orm.SessionEvents.do_orm_execute`

            :class:`.ORMExecuteState` - the object passed to the
            :meth:`_orm.SessionEvents.do_orm_execute` event which contains
            all information about the statement to be invoked.  It also
            provides an interface to extend the current statement, options,
            and parameters as well as an option that allows programmatic
            invocation of the statement at any point.

            :ref:`examples_session_orm_events` - includes examples of using
            :meth:`_orm.SessionEvents.do_orm_execute`

            :ref:`examples_caching` - an example of how to integrate
            Dogpile caching with the ORM :class:`_orm.Session` making use
            of the :meth:`_orm.SessionEvents.do_orm_execute` event hook.

            :ref:`examples_sharding` - the Horizontal Sharding example /
            extension relies upon the
            :meth:`_orm.SessionEvents.do_orm_execute` event hook to invoke a
            SQL statement on multiple backends and return a merged result.


        .. versionadded:: 1.4

        """
        pass

    
    def after_transaction_create(self = None, session = None, transaction = None):
        '''Execute when a new :class:`.SessionTransaction` is created.

        This event differs from :meth:`~.SessionEvents.after_begin`
        in that it occurs for each :class:`.SessionTransaction`
        overall, as opposed to when transactions are begun
        on individual database connections.  It is also invoked
        for nested transactions and subtransactions, and is always
        matched by a corresponding
        :meth:`~.SessionEvents.after_transaction_end` event
        (assuming normal operation of the :class:`.Session`).

        :param session: the target :class:`.Session`.
        :param transaction: the target :class:`.SessionTransaction`.

         To detect if this is the outermost
         :class:`.SessionTransaction`, as opposed to a "subtransaction" or a
         SAVEPOINT, test that the :attr:`.SessionTransaction.parent` attribute
         is ``None``::

                @event.listens_for(session, "after_transaction_create")
                def after_transaction_create(session, transaction):
                    if transaction.parent is None:
                        ...  # work with top-level transaction

         To detect if the :class:`.SessionTransaction` is a SAVEPOINT, use the
         :attr:`.SessionTransaction.nested` attribute::

                @event.listens_for(session, "after_transaction_create")
                def after_transaction_create(session, transaction):
                    if transaction.nested:
                        ...  # work with SAVEPOINT transaction

        .. seealso::

            :class:`.SessionTransaction`

            :meth:`~.SessionEvents.after_transaction_end`

        '''
        pass

    
    def after_transaction_end(self = None, session = None, transaction = None):
        '''Execute when the span of a :class:`.SessionTransaction` ends.

        This event differs from :meth:`~.SessionEvents.after_commit`
        in that it corresponds to all :class:`.SessionTransaction`
        objects in use, including those for nested transactions
        and subtransactions, and is always matched by a corresponding
        :meth:`~.SessionEvents.after_transaction_create` event.

        :param session: the target :class:`.Session`.
        :param transaction: the target :class:`.SessionTransaction`.

         To detect if this is the outermost
         :class:`.SessionTransaction`, as opposed to a "subtransaction" or a
         SAVEPOINT, test that the :attr:`.SessionTransaction.parent` attribute
         is ``None``::

                @event.listens_for(session, "after_transaction_create")
                def after_transaction_end(session, transaction):
                    if transaction.parent is None:
                        ...  # work with top-level transaction

         To detect if the :class:`.SessionTransaction` is a SAVEPOINT, use the
         :attr:`.SessionTransaction.nested` attribute::

                @event.listens_for(session, "after_transaction_create")
                def after_transaction_end(session, transaction):
                    if transaction.nested:
                        ...  # work with SAVEPOINT transaction

        .. seealso::

            :class:`.SessionTransaction`

            :meth:`~.SessionEvents.after_transaction_create`

        '''
        pass

    
    def before_commit(self = None, session = None):
        '''Execute before commit is called.

        .. note::

            The :meth:`~.SessionEvents.before_commit` hook is *not* per-flush,
            that is, the :class:`.Session` can emit SQL to the database
            many times within the scope of a transaction.
            For interception of these events, use the
            :meth:`~.SessionEvents.before_flush`,
            :meth:`~.SessionEvents.after_flush`, or
            :meth:`~.SessionEvents.after_flush_postexec`
            events.

        :param session: The target :class:`.Session`.

        .. seealso::

            :meth:`~.SessionEvents.after_commit`

            :meth:`~.SessionEvents.after_begin`

            :meth:`~.SessionEvents.after_transaction_create`

            :meth:`~.SessionEvents.after_transaction_end`

        '''
        pass

    
    def after_commit(self = None, session = None):
        '''Execute after a commit has occurred.

        .. note::

            The :meth:`~.SessionEvents.after_commit` hook is *not* per-flush,
            that is, the :class:`.Session` can emit SQL to the database
            many times within the scope of a transaction.
            For interception of these events, use the
            :meth:`~.SessionEvents.before_flush`,
            :meth:`~.SessionEvents.after_flush`, or
            :meth:`~.SessionEvents.after_flush_postexec`
            events.

        .. note::

            The :class:`.Session` is not in an active transaction
            when the :meth:`~.SessionEvents.after_commit` event is invoked,
            and therefore can not emit SQL.  To emit SQL corresponding to
            every transaction, use the :meth:`~.SessionEvents.before_commit`
            event.

        :param session: The target :class:`.Session`.

        .. seealso::

            :meth:`~.SessionEvents.before_commit`

            :meth:`~.SessionEvents.after_begin`

            :meth:`~.SessionEvents.after_transaction_create`

            :meth:`~.SessionEvents.after_transaction_end`

        '''
        pass

    
    def after_rollback(self = None, session = None):
        '''Execute after a real DBAPI rollback has occurred.

        Note that this event only fires when the *actual* rollback against
        the database occurs - it does *not* fire each time the
        :meth:`.Session.rollback` method is called, if the underlying
        DBAPI transaction has already been rolled back.  In many
        cases, the :class:`.Session` will not be in
        an "active" state during this event, as the current
        transaction is not valid.   To acquire a :class:`.Session`
        which is active after the outermost rollback has proceeded,
        use the :meth:`.SessionEvents.after_soft_rollback` event, checking the
        :attr:`.Session.is_active` flag.

        :param session: The target :class:`.Session`.

        '''
        pass

    
    def after_soft_rollback(self = None, session = None, previous_transaction = None):
        '''Execute after any rollback has occurred, including "soft"
        rollbacks that don\'t actually emit at the DBAPI level.

        This corresponds to both nested and outer rollbacks, i.e.
        the innermost rollback that calls the DBAPI\'s
        rollback() method, as well as the enclosing rollback
        calls that only pop themselves from the transaction stack.

        The given :class:`.Session` can be used to invoke SQL and
        :meth:`.Session.query` operations after an outermost rollback
        by first checking the :attr:`.Session.is_active` flag::

            @event.listens_for(Session, "after_soft_rollback")
            def do_something(session, previous_transaction):
                if session.is_active:
                    session.execute(text("select * from some_table"))

        :param session: The target :class:`.Session`.
        :param previous_transaction: The :class:`.SessionTransaction`
         transactional marker object which was just closed.   The current
         :class:`.SessionTransaction` for the given :class:`.Session` is
         available via the :attr:`.Session.transaction` attribute.

        '''
        pass

    
    def before_flush(self = None, session = None, flush_context = None, instances = ('session', 'Session', 'flush_context', 'UOWTransaction', 'instances', 'Optional[Sequence[_O]]', 'return', 'None')):
        '''Execute before flush process has started.

        :param session: The target :class:`.Session`.
        :param flush_context: Internal :class:`.UOWTransaction` object
         which handles the details of the flush.
        :param instances: Usually ``None``, this is the collection of
         objects which can be passed to the :meth:`.Session.flush` method
         (note this usage is deprecated).

        .. seealso::

            :meth:`~.SessionEvents.after_flush`

            :meth:`~.SessionEvents.after_flush_postexec`

            :ref:`session_persistence_events`

        '''
        pass

    
    def after_flush(self = None, session = None, flush_context = None):
        """Execute after flush has completed, but before commit has been
        called.

        Note that the session's state is still in pre-flush, i.e. 'new',
        'dirty', and 'deleted' lists still show pre-flush state as well
        as the history settings on instance attributes.

        .. warning:: This event runs after the :class:`.Session` has emitted
           SQL to modify the database, but **before** it has altered its
           internal state to reflect those changes, including that newly
           inserted objects are placed into the identity map.  ORM operations
           emitted within this event such as loads of related items
           may produce new identity map entries that will immediately
           be replaced, sometimes causing confusing results.  SQLAlchemy will
           emit a warning for this condition as of version 1.3.9.

        :param session: The target :class:`.Session`.
        :param flush_context: Internal :class:`.UOWTransaction` object
         which handles the details of the flush.

        .. seealso::

            :meth:`~.SessionEvents.before_flush`

            :meth:`~.SessionEvents.after_flush_postexec`

            :ref:`session_persistence_events`

        """
        pass

    
    def after_flush_postexec(self = None, session = None, flush_context = None):
        """Execute after flush has completed, and after the post-exec
        state occurs.

        This will be when the 'new', 'dirty', and 'deleted' lists are in
        their final state.  An actual commit() may or may not have
        occurred, depending on whether or not the flush started its own
        transaction or participated in a larger transaction.

        :param session: The target :class:`.Session`.
        :param flush_context: Internal :class:`.UOWTransaction` object
         which handles the details of the flush.


        .. seealso::

            :meth:`~.SessionEvents.before_flush`

            :meth:`~.SessionEvents.after_flush`

            :ref:`session_persistence_events`

        """
        pass

    
    def after_begin(self = None, session = None, transaction = None, connection = ('session', 'Session', 'transaction', 'SessionTransaction', 'connection', 'Connection', 'return', 'None')):
        '''Execute after a transaction is begun on a connection.

        .. note:: This event is called within the process of the
          :class:`_orm.Session` modifying its own internal state.
          To invoke SQL operations within this hook, use the
          :class:`_engine.Connection` provided to the event;
          do not run SQL operations using the :class:`_orm.Session`
          directly.

        :param session: The target :class:`.Session`.
        :param transaction: The :class:`.SessionTransaction`.
        :param connection: The :class:`_engine.Connection` object
         which will be used for SQL statements.

        .. seealso::

            :meth:`~.SessionEvents.before_commit`

            :meth:`~.SessionEvents.after_commit`

            :meth:`~.SessionEvents.after_transaction_create`

            :meth:`~.SessionEvents.after_transaction_end`

        '''
        pass

    before_attach = (lambda self = None, session = None, instance = _lifecycle_event: pass)()
    after_attach = (lambda self = None, session = None, instance = _lifecycle_event: pass)()
    after_bulk_update = (lambda self = None, update_context = None: pass)()
    after_bulk_delete = (lambda self = None, delete_context = None: pass)()
    transient_to_pending = (lambda self = None, session = None, instance = _lifecycle_event: pass)()
    pending_to_transient = (lambda self = None, session = None, instance = _lifecycle_event: pass)()
    persistent_to_transient = (lambda self = None, session = None, instance = _lifecycle_event: pass)()
    pending_to_persistent = (lambda self = None, session = None, instance = _lifecycle_event: pass)()
    detached_to_persistent = (lambda self = None, session = None, instance = _lifecycle_event: pass)()
    loaded_as_persistent = (lambda self = None, session = None, instance = _lifecycle_event: pass)()
    persistent_to_deleted = (lambda self = None, session = None, instance = _lifecycle_event: pass)()
    deleted_to_persistent = (lambda self = None, session = None, instance = _lifecycle_event: pass)()
    deleted_to_detached = (lambda self = None, session = None, instance = _lifecycle_event: pass)()
    persistent_to_detached = (lambda self = None, session = None, instance = _lifecycle_event: pass)()

SessionEvents = <NODE:27>(SessionEvents, 'SessionEvents', event.Events[Session])

def AttributeEvents():
    '''AttributeEvents'''
    __doc__ = 'Define events for object attributes.\n\n    These are typically defined on the class-bound descriptor for the\n    target class.\n\n    For example, to register a listener that will receive the\n    :meth:`_orm.AttributeEvents.append` event::\n\n        from sqlalchemy import event\n\n\n        @event.listens_for(MyClass.collection, "append", propagate=True)\n        def my_append_listener(target, value, initiator):\n            print("received append event for target: %s" % target)\n\n    Listeners have the option to return a possibly modified version of the\n    value, when the :paramref:`.AttributeEvents.retval` flag is passed to\n    :func:`.event.listen` or :func:`.event.listens_for`, such as below,\n    illustrated using the :meth:`_orm.AttributeEvents.set` event::\n\n        def validate_phone(target, value, oldvalue, initiator):\n            "Strip non-numeric characters from a phone number"\n\n            return re.sub(r"\\D", "", value)\n\n\n        # setup listener on UserContact.phone attribute, instructing\n        # it to use the return value\n        listen(UserContact.phone, "set", validate_phone, retval=True)\n\n    A validation function like the above can also raise an exception\n    such as :exc:`ValueError` to halt the operation.\n\n    The :paramref:`.AttributeEvents.propagate` flag is also important when\n    applying listeners to mapped classes that also have mapped subclasses,\n    as when using mapper inheritance patterns::\n\n\n        @event.listens_for(MySuperClass.attr, "set", propagate=True)\n        def receive_set(target, value, initiator):\n            print("value set: %s" % target)\n\n    The full list of modifiers available to the :func:`.event.listen`\n    and :func:`.event.listens_for` functions are below.\n\n    :param active_history=False: When True, indicates that the\n      "set" event would like to receive the "old" value being\n      replaced unconditionally, even if this requires firing off\n      database loads. Note that ``active_history`` can also be\n      set directly via :func:`.column_property` and\n      :func:`_orm.relationship`.\n\n    :param propagate=False: When True, the listener function will\n      be established not just for the class attribute given, but\n      for attributes of the same name on all current subclasses\n      of that class, as well as all future subclasses of that\n      class, using an additional listener that listens for\n      instrumentation events.\n    :param raw=False: When True, the "target" argument to the\n      event will be the :class:`.InstanceState` management\n      object, rather than the mapped instance itself.\n    :param retval=False: when True, the user-defined event\n      listening must return the "value" argument from the\n      function.  This gives the listening function the opportunity\n      to change the value that is ultimately used for a "set"\n      or "append" event.\n\n    '
    _target_class_doc = 'SomeClass.some_attribute'
    _dispatch_target = QueryableAttribute
    _set_dispatch = (lambda cls = None, dispatch_cls = None: dispatch = event.Events._set_dispatch(cls, dispatch_cls)dispatch_cls._active_history = Falsedispatch)()
    _accept_with = (lambda cls = None, target = None, identifier = classmethod: if isinstance(target, interfaces.MapperProperty):
getattr(target.parent.class_, target.key))()
    _listen = (lambda cls, event_key, active_history = None, raw = None, retval = classmethod, propagate = (False, False, False, False, False), include_key = ('event_key', '_EventKey[QueryableAttribute[Any]]', 'active_history', 'bool', 'raw', 'bool', 'retval', 'bool', 'propagate', 'bool', 'include_key', 'bool', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    
    def append(self = None, target = None, value = None, initiator = None, *, key):
        '''Receive a collection append event.

        The append event is invoked for each element as it is appended
        to the collection.  This occurs for single-item appends as well
        as for a "bulk replace" operation.

        :param target: the object instance receiving the event.
          If the listener is registered with ``raw=True``, this will
          be the :class:`.InstanceState` object.
        :param value: the value being appended.  If this listener
          is registered with ``retval=True``, the listener
          function must return this value, or a new value which
          replaces it.
        :param initiator: An instance of :class:`.attributes.Event`
          representing the initiation of the event.  May be modified
          from its original value by backref handlers in order to control
          chained event propagation, as well as be inspected for information
          about the source of the event.
        :param key: When the event is established using the
         :paramref:`.AttributeEvents.include_key` parameter set to
         True, this will be the key used in the operation, such as
         ``collection[some_key_or_index] = value``.
         The parameter is not passed
         to the event at all if the the
         :paramref:`.AttributeEvents.include_key`
         was not used to set up the event; this is to allow backwards
         compatibility with existing event handlers that don\'t include the
         ``key`` parameter.

         .. versionadded:: 2.0

        :return: if the event was registered with ``retval=True``,
         the given value, or a new effective value, should be returned.

        .. seealso::

            :class:`.AttributeEvents` - background on listener options such
            as propagation to subclasses.

            :meth:`.AttributeEvents.bulk_replace`

        '''
        pass

    
    def append_wo_mutation(self = None, target = None, value = None, initiator = None, *, key):
        """Receive a collection append event where the collection was not
        actually mutated.

        This event differs from :meth:`_orm.AttributeEvents.append` in that
        it is fired off for de-duplicating collections such as sets and
        dictionaries, when the object already exists in the target collection.
        The event does not have a return value and the identity of the
        given object cannot be changed.

        The event is used for cascading objects into a :class:`_orm.Session`
        when the collection has already been mutated via a backref event.

        :param target: the object instance receiving the event.
          If the listener is registered with ``raw=True``, this will
          be the :class:`.InstanceState` object.
        :param value: the value that would be appended if the object did not
          already exist in the collection.
        :param initiator: An instance of :class:`.attributes.Event`
          representing the initiation of the event.  May be modified
          from its original value by backref handlers in order to control
          chained event propagation, as well as be inspected for information
          about the source of the event.
        :param key: When the event is established using the
         :paramref:`.AttributeEvents.include_key` parameter set to
         True, this will be the key used in the operation, such as
         ``collection[some_key_or_index] = value``.
         The parameter is not passed
         to the event at all if the the
         :paramref:`.AttributeEvents.include_key`
         was not used to set up the event; this is to allow backwards
         compatibility with existing event handlers that don't include the
         ``key`` parameter.

         .. versionadded:: 2.0

        :return: No return value is defined for this event.

        .. versionadded:: 1.4.15

        """
        pass

    
    def bulk_replace(self = None, target = None, values = None, initiator = None, *, keys):
        '''Receive a collection \'bulk replace\' event.

        This event is invoked for a sequence of values as they are incoming
        to a bulk collection set operation, which can be
        modified in place before the values are treated as ORM objects.
        This is an "early hook" that runs before the bulk replace routine
        attempts to reconcile which objects are already present in the
        collection and which are being removed by the net replace operation.

        It is typical that this method be combined with use of the
        :meth:`.AttributeEvents.append` event.    When using both of these
        events, note that a bulk replace operation will invoke
        the :meth:`.AttributeEvents.append` event for all new items,
        even after :meth:`.AttributeEvents.bulk_replace` has been invoked
        for the collection as a whole.  In order to determine if an
        :meth:`.AttributeEvents.append` event is part of a bulk replace,
        use the symbol :attr:`~.attributes.OP_BULK_REPLACE` to test the
        incoming initiator::

            from sqlalchemy.orm.attributes import OP_BULK_REPLACE


            @event.listens_for(SomeObject.collection, "bulk_replace")
            def process_collection(target, values, initiator):
                values[:] = [_make_value(value) for value in values]


            @event.listens_for(SomeObject.collection, "append", retval=True)
            def process_collection(target, value, initiator):
                # make sure bulk_replace didn\'t already do it
                if initiator is None or initiator.op is not OP_BULK_REPLACE:
                    return _make_value(value)
                else:
                    return value

        .. versionadded:: 1.2

        :param target: the object instance receiving the event.
          If the listener is registered with ``raw=True``, this will
          be the :class:`.InstanceState` object.
        :param value: a sequence (e.g. a list) of the values being set.  The
          handler can modify this list in place.
        :param initiator: An instance of :class:`.attributes.Event`
          representing the initiation of the event.
        :param keys: When the event is established using the
         :paramref:`.AttributeEvents.include_key` parameter set to
         True, this will be the sequence of keys used in the operation,
         typically only for a dictionary update.  The parameter is not passed
         to the event at all if the the
         :paramref:`.AttributeEvents.include_key`
         was not used to set up the event; this is to allow backwards
         compatibility with existing event handlers that don\'t include the
         ``key`` parameter.

         .. versionadded:: 2.0

        .. seealso::

            :class:`.AttributeEvents` - background on listener options such
            as propagation to subclasses.


        '''
        pass

    
    def remove(self = None, target = None, value = None, initiator = None, *, key):
        """Receive a collection remove event.

        :param target: the object instance receiving the event.
          If the listener is registered with ``raw=True``, this will
          be the :class:`.InstanceState` object.
        :param value: the value being removed.
        :param initiator: An instance of :class:`.attributes.Event`
          representing the initiation of the event.  May be modified
          from its original value by backref handlers in order to control
          chained event propagation.

        :param key: When the event is established using the
         :paramref:`.AttributeEvents.include_key` parameter set to
         True, this will be the key used in the operation, such as
         ``del collection[some_key_or_index]``.  The parameter is not passed
         to the event at all if the the
         :paramref:`.AttributeEvents.include_key`
         was not used to set up the event; this is to allow backwards
         compatibility with existing event handlers that don't include the
         ``key`` parameter.

         .. versionadded:: 2.0

        :return: No return value is defined for this event.


        .. seealso::

            :class:`.AttributeEvents` - background on listener options such
            as propagation to subclasses.

        """
        pass

    
    def set(self, target = None, value = None, oldvalue = None, initiator = ('target', '_O', 'value', '_T', 'oldvalue', '_T', 'initiator', 'Event', 'return', 'None')):
        '''Receive a scalar set event.

        :param target: the object instance receiving the event.
          If the listener is registered with ``raw=True``, this will
          be the :class:`.InstanceState` object.
        :param value: the value being set.  If this listener
          is registered with ``retval=True``, the listener
          function must return this value, or a new value which
          replaces it.
        :param oldvalue: the previous value being replaced.  This
          may also be the symbol ``NEVER_SET`` or ``NO_VALUE``.
          If the listener is registered with ``active_history=True``,
          the previous value of the attribute will be loaded from
          the database if the existing value is currently unloaded
          or expired.
        :param initiator: An instance of :class:`.attributes.Event`
          representing the initiation of the event.  May be modified
          from its original value by backref handlers in order to control
          chained event propagation.

        :return: if the event was registered with ``retval=True``,
         the given value, or a new effective value, should be returned.

        .. seealso::

            :class:`.AttributeEvents` - background on listener options such
            as propagation to subclasses.

        '''
        pass

    
    def init_scalar(self = None, target = None, value = None, dict_ = ('target', '_O', 'value', '_T', 'dict_', 'Dict[Any, Any]', 'return', 'None')):
        '''Receive a scalar "init" event.

        This event is invoked when an uninitialized, unpersisted scalar
        attribute is accessed, e.g. read::


            x = my_object.some_attribute

        The ORM\'s default behavior when this occurs for an un-initialized
        attribute is to return the value ``None``; note this differs from
        Python\'s usual behavior of raising ``AttributeError``.    The
        event here can be used to customize what value is actually returned,
        with the assumption that the event listener would be mirroring
        a default generator that is configured on the Core
        :class:`_schema.Column`
        object as well.

        Since a default generator on a :class:`_schema.Column`
        might also produce
        a changing value such as a timestamp, the
        :meth:`.AttributeEvents.init_scalar`
        event handler can also be used to **set** the newly returned value, so
        that a Core-level default generation function effectively fires off
        only once, but at the moment the attribute is accessed on the
        non-persisted object.   Normally, no change to the object\'s state
        is made when an uninitialized attribute is accessed (much older
        SQLAlchemy versions did in fact change the object\'s state).

        If a default generator on a column returned a particular constant,
        a handler might be used as follows::

            SOME_CONSTANT = 3.1415926


            class MyClass(Base):
                # ...

                some_attribute = Column(Numeric, default=SOME_CONSTANT)


            @event.listens_for(
                MyClass.some_attribute, "init_scalar", retval=True, propagate=True
            )
            def _init_some_attribute(target, dict_, value):
                dict_["some_attribute"] = SOME_CONSTANT
                return SOME_CONSTANT

        Above, we initialize the attribute ``MyClass.some_attribute`` to the
        value of ``SOME_CONSTANT``.   The above code includes the following
        features:

        * By setting the value ``SOME_CONSTANT`` in the given ``dict_``,
          we indicate that this value is to be persisted to the database.
          This supersedes the use of ``SOME_CONSTANT`` in the default generator
          for the :class:`_schema.Column`.  The ``active_column_defaults.py``
          example given at :ref:`examples_instrumentation` illustrates using
          the same approach for a changing default, e.g. a timestamp
          generator.    In this particular example, it is not strictly
          necessary to do this since ``SOME_CONSTANT`` would be part of the
          INSERT statement in either case.

        * By establishing the ``retval=True`` flag, the value we return
          from the function will be returned by the attribute getter.
          Without this flag, the event is assumed to be a passive observer
          and the return value of our function is ignored.

        * The ``propagate=True`` flag is significant if the mapped class
          includes inheriting subclasses, which would also make use of this
          event listener.  Without this flag, an inheriting subclass will
          not use our event handler.

        In the above example, the attribute set event
        :meth:`.AttributeEvents.set` as well as the related validation feature
        provided by :obj:`_orm.validates` is **not** invoked when we apply our
        value to the given ``dict_``.  To have these events to invoke in
        response to our newly generated value, apply the value to the given
        object as a normal attribute set operation::

            SOME_CONSTANT = 3.1415926


            @event.listens_for(
                MyClass.some_attribute, "init_scalar", retval=True, propagate=True
            )
            def _init_some_attribute(target, dict_, value):
                # will also fire off attribute set events
                target.some_attribute = SOME_CONSTANT
                return SOME_CONSTANT

        When multiple listeners are set up, the generation of the value
        is "chained" from one listener to the next by passing the value
        returned by the previous listener that specifies ``retval=True``
        as the ``value`` argument of the next listener.

        :param target: the object instance receiving the event.
         If the listener is registered with ``raw=True``, this will
         be the :class:`.InstanceState` object.
        :param value: the value that is to be returned before this event
         listener were invoked.  This value begins as the value ``None``,
         however will be the return value of the previous event handler
         function if multiple listeners are present.
        :param dict\\_: the attribute dictionary of this mapped object.
         This is normally the ``__dict__`` of the object, but in all cases
         represents the destination that the attribute system uses to get
         at the actual value of this attribute.  Placing the value in this
         dictionary has the effect that the value will be used in the
         INSERT statement generated by the unit of work.


        .. seealso::

            :meth:`.AttributeEvents.init_collection` - collection version
            of this event

            :class:`.AttributeEvents` - background on listener options such
            as propagation to subclasses.

            :ref:`examples_instrumentation` - see the
            ``active_column_defaults.py`` example.

        '''
        pass

    
    def init_collection(self = None, target = None, collection = None, collection_adapter = ('target', '_O', 'collection', 'Type[Collection[Any]]', 'collection_adapter', 'CollectionAdapter', 'return', 'None')):
        '''Receive a \'collection init\' event.

        This event is triggered for a collection-based attribute, when
        the initial "empty collection" is first generated for a blank
        attribute, as well as for when the collection is replaced with
        a new one, such as via a set event.

        E.g., given that ``User.addresses`` is a relationship-based
        collection, the event is triggered here::

            u1 = User()
            u1.addresses.append(a1)  #  <- new collection

        and also during replace operations::

            u1.addresses = [a2, a3]  #  <- new collection

        :param target: the object instance receiving the event.
         If the listener is registered with ``raw=True``, this will
         be the :class:`.InstanceState` object.
        :param collection: the new collection.  This will always be generated
         from what was specified as
         :paramref:`_orm.relationship.collection_class`, and will always
         be empty.
        :param collection_adapter: the :class:`.CollectionAdapter` that will
         mediate internal access to the collection.

        .. seealso::

            :class:`.AttributeEvents` - background on listener options such
            as propagation to subclasses.

            :meth:`.AttributeEvents.init_scalar` - "scalar" version of this
            event.

        '''
        pass

    
    def dispose_collection(self = None, target = None, collection = None, collection_adapter = ('target', '_O', 'collection', 'Collection[Any]', 'collection_adapter', 'CollectionAdapter', 'return', 'None')):
        """Receive a 'collection dispose' event.

        This event is triggered for a collection-based attribute when
        a collection is replaced, that is::

            u1.addresses.append(a1)

            u1.addresses = [a2, a3]  # <- old collection is disposed

        The old collection received will contain its previous contents.

        .. versionchanged:: 1.2 The collection passed to
           :meth:`.AttributeEvents.dispose_collection` will now have its
           contents before the dispose intact; previously, the collection
           would be empty.

        .. seealso::

            :class:`.AttributeEvents` - background on listener options such
            as propagation to subclasses.

        """
        pass

    
    def modified(self = None, target = None, initiator = None):
        """Receive a 'modified' event.

        This event is triggered when the :func:`.attributes.flag_modified`
        function is used to trigger a modify event on an attribute without
        any specific value being set.

        .. versionadded:: 1.2

        :param target: the object instance receiving the event.
          If the listener is registered with ``raw=True``, this will
          be the :class:`.InstanceState` object.

        :param initiator: An instance of :class:`.attributes.Event`
          representing the initiation of the event.

        .. seealso::

            :class:`.AttributeEvents` - background on listener options such
            as propagation to subclasses.

        """
        pass


AttributeEvents = <NODE:27>(AttributeEvents, 'AttributeEvents', event.Events[QueryableAttribute[Any]])

def QueryEvents():
    '''QueryEvents'''
    __doc__ = 'Represent events within the construction of a :class:`_query.Query`\n    object.\n\n    .. legacy:: The :class:`_orm.QueryEvents` event methods are legacy\n        as of SQLAlchemy 2.0, and only apply to direct use of the\n        :class:`_orm.Query` object. They are not used for :term:`2.0 style`\n        statements. For events to intercept and modify 2.0 style ORM use,\n        use the :meth:`_orm.SessionEvents.do_orm_execute` hook.\n\n\n    The :class:`_orm.QueryEvents` hooks are now superseded by the\n    :meth:`_orm.SessionEvents.do_orm_execute` event hook.\n\n    '
    _target_class_doc = 'SomeQuery'
    _dispatch_target = Query
    
    def before_compile(self = None, query = None):
        '''Receive the :class:`_query.Query`
        object before it is composed into a
        core :class:`_expression.Select` object.

        .. deprecated:: 1.4  The :meth:`_orm.QueryEvents.before_compile` event
           is superseded by the much more capable
           :meth:`_orm.SessionEvents.do_orm_execute` hook.   In version 1.4,
           the :meth:`_orm.QueryEvents.before_compile` event is **no longer
           used** for ORM-level attribute loads, such as loads of deferred
           or expired attributes as well as relationship loaders.   See the
           new examples in :ref:`examples_session_orm_events` which
           illustrate new ways of intercepting and modifying ORM queries
           for the most common purpose of adding arbitrary filter criteria.


        This event is intended to allow changes to the query given::

            @event.listens_for(Query, "before_compile", retval=True)
            def no_deleted(query):
                for desc in query.column_descriptions:
                    if desc["type"] is User:
                        entity = desc["entity"]
                        query = query.filter(entity.deleted == False)
                return query

        The event should normally be listened with the ``retval=True``
        parameter set, so that the modified query may be returned.

        The :meth:`.QueryEvents.before_compile` event by default
        will disallow "baked" queries from caching a query, if the event
        hook returns a new :class:`_query.Query` object.
        This affects both direct
        use of the baked query extension as well as its operation within
        lazy loaders and eager loaders for relationships.  In order to
        re-establish the query being cached, apply the event adding the
        ``bake_ok`` flag::

            @event.listens_for(Query, "before_compile", retval=True, bake_ok=True)
            def my_event(query):
                for desc in query.column_descriptions:
                    if desc["type"] is User:
                        entity = desc["entity"]
                        query = query.filter(entity.deleted == False)
                return query

        When ``bake_ok`` is set to True, the event hook will only be invoked
        once, and not called for subsequent invocations of a particular query
        that is being cached.

        .. versionadded:: 1.3.11  - added the "bake_ok" flag to the
           :meth:`.QueryEvents.before_compile` event and disallowed caching via
           the "baked" extension from occurring for event handlers that
           return  a new :class:`_query.Query` object if this flag is not set.

        .. seealso::

            :meth:`.QueryEvents.before_compile_update`

            :meth:`.QueryEvents.before_compile_delete`

            :ref:`baked_with_before_compile`

        '''
        pass

    
    def before_compile_update(self = None, query = None, update_context = None):
        '''Allow modifications to the :class:`_query.Query` object within
        :meth:`_query.Query.update`.

        .. deprecated:: 1.4  The :meth:`_orm.QueryEvents.before_compile_update`
           event is superseded by the much more capable
           :meth:`_orm.SessionEvents.do_orm_execute` hook.

        Like the :meth:`.QueryEvents.before_compile` event, if the event
        is to be used to alter the :class:`_query.Query` object, it should
        be configured with ``retval=True``, and the modified
        :class:`_query.Query` object returned, as in ::

            @event.listens_for(Query, "before_compile_update", retval=True)
            def no_deleted(query, update_context):
                for desc in query.column_descriptions:
                    if desc["type"] is User:
                        entity = desc["entity"]
                        query = query.filter(entity.deleted == False)

                        update_context.values["timestamp"] = datetime.datetime.now(
                            datetime.UTC
                        )
                return query

        The ``.values`` dictionary of the "update context" object can also
        be modified in place as illustrated above.

        :param query: a :class:`_query.Query` instance; this is also
         the ``.query`` attribute of the given "update context"
         object.

        :param update_context: an "update context" object which is
         the same kind of object as described in
         :paramref:`.QueryEvents.after_bulk_update.update_context`.
         The object has a ``.values`` attribute in an UPDATE context which is
         the dictionary of parameters passed to :meth:`_query.Query.update`.
         This
         dictionary can be modified to alter the VALUES clause of the
         resulting UPDATE statement.

        .. versionadded:: 1.2.17

        .. seealso::

            :meth:`.QueryEvents.before_compile`

            :meth:`.QueryEvents.before_compile_delete`


        '''
        pass

    
    def before_compile_delete(self = None, query = None, delete_context = None):
        '''Allow modifications to the :class:`_query.Query` object within
        :meth:`_query.Query.delete`.

        .. deprecated:: 1.4  The :meth:`_orm.QueryEvents.before_compile_delete`
           event is superseded by the much more capable
           :meth:`_orm.SessionEvents.do_orm_execute` hook.

        Like the :meth:`.QueryEvents.before_compile` event, this event
        should be configured with ``retval=True``, and the modified
        :class:`_query.Query` object returned, as in ::

            @event.listens_for(Query, "before_compile_delete", retval=True)
            def no_deleted(query, delete_context):
                for desc in query.column_descriptions:
                    if desc["type"] is User:
                        entity = desc["entity"]
                        query = query.filter(entity.deleted == False)
                return query

        :param query: a :class:`_query.Query` instance; this is also
         the ``.query`` attribute of the given "delete context"
         object.

        :param delete_context: a "delete context" object which is
         the same kind of object as described in
         :paramref:`.QueryEvents.after_bulk_delete.delete_context`.

        .. versionadded:: 1.2.17

        .. seealso::

            :meth:`.QueryEvents.before_compile`

            :meth:`.QueryEvents.before_compile_update`


        '''
        pass

    _listen = (lambda cls = None, event_key = None, retval = classmethod, bake_ok = (False, False): pass# WARNING: Decompyle incomplete
)()

QueryEvents = <NODE:27>(QueryEvents, 'QueryEvents', event.Events[Query[Any]])
