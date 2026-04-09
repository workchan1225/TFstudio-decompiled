# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session.pyc (Python 3.11)

from __future__ import annotations
import asyncio
from typing import Any
from typing import Awaitable
from typing import Callable
from typing import cast
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import engine
from base import ReversibleProxy
from base import StartableContext
from result import _ensure_sync_result
from result import AsyncResult
from result import AsyncScalarResult
from  import util
from orm import close_all_sessions as _sync_close_all_sessions
from orm import object_session
from orm import Session
from orm import SessionTransaction
from orm import state as _instance_state
from util.concurrency import greenlet_spawn
from util.typing import Concatenate
from util.typing import ParamSpec
if TYPE_CHECKING:
    from engine import AsyncConnection
    from engine import AsyncEngine
    from engine import Connection
    from engine import Engine
    from engine import Result
    from engine import Row
    from engine import RowMapping
    from engine import ScalarResult
    from engine.interfaces import _CoreAnyExecuteParams
    from engine.interfaces import CoreExecuteOptionsParameter
    from event import dispatcher
    from orm._typing import _IdentityKeyType
    from orm._typing import _O
    from orm._typing import OrmExecuteOptionsParameter
    from orm.identity import IdentityMap
    from orm.interfaces import ORMOption
    from orm.session import _BindArguments
    from orm.session import _EntityBindKey
    from orm.session import _PKIdentityArgument
    from orm.session import _SessionBind
    from orm.session import _SessionBindKey
    from sql._typing import _InfoType
    from sql.base import Executable
    from sql.elements import ClauseElement
    from sql.selectable import ForUpdateParameter
    from sql.selectable import TypedReturnsRows
_AsyncSessionBind = Union[('AsyncEngine', 'AsyncConnection')]
_P = ParamSpec('_P')
_T = TypeVar('_T', bound = Any)
_EXECUTE_OPTIONS = util.immutabledict({
    'prebuffer_rows': True })
_STREAM_OPTIONS = util.immutabledict({
    'stream_results': True })

class AsyncAttrs:
    '''Mixin class which provides an awaitable accessor for all attributes.

    E.g.::

        from __future__ import annotations

        from typing import List

        from sqlalchemy import ForeignKey
        from sqlalchemy import func
        from sqlalchemy.ext.asyncio import AsyncAttrs
        from sqlalchemy.orm import DeclarativeBase
        from sqlalchemy.orm import Mapped
        from sqlalchemy.orm import mapped_column
        from sqlalchemy.orm import relationship


        class Base(AsyncAttrs, DeclarativeBase):
            pass


        class A(Base):
            __tablename__ = "a"

            id: Mapped[int] = mapped_column(primary_key=True)
            data: Mapped[str]
            bs: Mapped[List[B]] = relationship()


        class B(Base):
            __tablename__ = "b"
            id: Mapped[int] = mapped_column(primary_key=True)
            a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
            data: Mapped[str]

    In the above example, the :class:`_asyncio.AsyncAttrs` mixin is applied to
    the declarative ``Base`` class where it takes effect for all subclasses.
    This mixin adds a single new attribute
    :attr:`_asyncio.AsyncAttrs.awaitable_attrs` to all classes, which will
    yield the value of any attribute as an awaitable. This allows attributes
    which may be subject to lazy loading or deferred / unexpiry loading to be
    accessed such that IO can still be emitted::

        a1 = (await async_session.scalars(select(A).where(A.id == 5))).one()

        # use the lazy loader on ``a1.bs`` via the ``.awaitable_attrs``
        # interface, so that it may be awaited
        for b1 in await a1.awaitable_attrs.bs:
            print(b1)

    The :attr:`_asyncio.AsyncAttrs.awaitable_attrs` performs a call against the
    attribute that is approximately equivalent to using the
    :meth:`_asyncio.AsyncSession.run_sync` method, e.g.::

        for b1 in await async_session.run_sync(lambda sess: a1.bs):
            print(b1)

    .. versionadded:: 2.0.13

    .. seealso::

        :ref:`asyncio_orm_avoid_lazyloads`

    '''
    
    class _AsyncAttrGetitem:
        __slots__ = '_instance'
        
        def __init__(self = None, _instance = None):
            self._instance = _instance

        
        def __getattr__(self = None, name = None):
            return greenlet_spawn(getattr, self._instance, name)


    awaitable_attrs = (lambda self = None: AsyncAttrs._AsyncAttrGetitem(self))()


def AsyncSession():
    '''AsyncSession'''
    __doc__ = 'Asyncio version of :class:`_orm.Session`.\n\n    The :class:`_asyncio.AsyncSession` is a proxy for a traditional\n    :class:`_orm.Session` instance.\n\n    The :class:`_asyncio.AsyncSession` is **not safe for use in concurrent\n    tasks.**.  See :ref:`session_faq_threadsafe` for background.\n\n    .. versionadded:: 1.4\n\n    To use an :class:`_asyncio.AsyncSession` with custom :class:`_orm.Session`\n    implementations, see the\n    :paramref:`_asyncio.AsyncSession.sync_session_class` parameter.\n\n\n    '
    dispatch: 'dispatcher[Session]' = True
    
    def __init__(self = None, bind = None, *, binds, sync_session_class, **kw):
        '''Construct a new :class:`_asyncio.AsyncSession`.

        All parameters other than ``sync_session_class`` are passed to the
        ``sync_session_class`` callable directly to instantiate a new
        :class:`_orm.Session`. Refer to :meth:`_orm.Session.__init__` for
        parameter documentation.

        :param sync_session_class:
          A :class:`_orm.Session` subclass or other callable which will be used
          to construct the :class:`_orm.Session` which will be proxied. This
          parameter may be used to provide custom :class:`_orm.Session`
          subclasses. Defaults to the
          :attr:`_asyncio.AsyncSession.sync_session_class` class-level
          attribute.

          .. versionadded:: 1.4.24

        '''
        sync_bind = None
        sync_binds = None
        if bind:
            self.bind = bind
            sync_bind = engine._get_sync_engine_or_connection(bind)
        if binds:
            self.binds = binds
            sync_binds = binds.items()()
        if sync_session_class:
            self.sync_session_class = sync_session_class
    # WARNING: Decompyle incomplete

    sync_session: 'Session' = Session
    _no_async_engine_events = (lambda cls = None: raise NotImplementedError('asynchronous events are not implemented at this time.  Apply synchronous listeners to the AsyncSession.sync_session.'))()
    
    async def refresh(self = None, instance = None, attribute_names = None, with_for_update = (None, None)):
        '''Expire and refresh the attributes on the given instance.

        A query will be issued to the database and all attributes will be
        refreshed with their current database value.

        This is the async version of the :meth:`_orm.Session.refresh` method.
        See that method for a complete description of all options.

        .. seealso::

            :meth:`_orm.Session.refresh` - main documentation for refresh

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def run_sync(self = None, fn = None, *arg, **kw):
        '''Invoke the given synchronous (i.e. not async) callable,
        passing a synchronous-style :class:`_orm.Session` as the first
        argument.

        This method allows traditional synchronous SQLAlchemy functions to
        run within the context of an asyncio application.

        E.g.::

            def some_business_method(session: Session, param: str) -> str:
                """A synchronous function that does not require awaiting

                :param session: a SQLAlchemy Session, used synchronously

                :return: an optional return value is supported

                """
                session.add(MyObject(param=param))
                session.flush()
                return "success"


            async def do_something_async(async_engine: AsyncEngine) -> None:
                """an async function that uses awaiting"""

                with AsyncSession(async_engine) as async_session:
                    # run some_business_method() with a sync-style
                    # Session, proxied into an awaitable
                    return_code = await async_session.run_sync(
                        some_business_method, param="param1"
                    )
                    print(return_code)

        This method maintains the asyncio event loop all the way through
        to the database connection by running the given callable in a
        specially instrumented greenlet.

        .. tip::

            The provided callable is invoked inline within the asyncio event
            loop, and will block on traditional IO calls.  IO within this
            callable should only call into SQLAlchemy\'s asyncio database
            APIs which will be properly adapted to the greenlet context.

        .. seealso::

            :class:`.AsyncAttrs`  - a mixin for ORM mapped classes that provides
            a similar feature more succinctly on a per-attribute basis

            :meth:`.AsyncConnection.run_sync`

            :ref:`session_run_sync`
        '''
        pass
    # WARNING: Decompyle incomplete

    execute = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, _parent_execute_state: pass# WARNING: Decompyle incomplete
)()
    execute = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, _parent_execute_state: pass# WARNING: Decompyle incomplete
)()
    
    async def execute(self = None, statement = None, params = None, *, execution_options, bind_arguments, **kw):
        '''Execute a statement and return a buffered
        :class:`_engine.Result` object.

        .. seealso::

            :meth:`_orm.Session.execute` - main documentation for execute

        '''
        pass
    # WARNING: Decompyle incomplete

    scalar = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    scalar = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    
    async def scalar(self = None, statement = None, params = None, *, execution_options, bind_arguments, **kw):
        '''Execute a statement and return a scalar result.

        .. seealso::

            :meth:`_orm.Session.scalar` - main documentation for scalar

        '''
        pass
    # WARNING: Decompyle incomplete

    scalars = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    scalars = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    
    async def scalars(self = None, statement = None, params = None, *, execution_options, bind_arguments, **kw):
        '''Execute a statement and return scalar results.

        :return: a :class:`_result.ScalarResult` object

        .. versionadded:: 1.4.24 Added :meth:`_asyncio.AsyncSession.scalars`

        .. versionadded:: 1.4.26 Added
           :meth:`_asyncio.async_scoped_session.scalars`

        .. seealso::

            :meth:`_orm.Session.scalars` - main documentation for scalars

            :meth:`_asyncio.AsyncSession.stream_scalars` - streaming version

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def get(self = None, entity = None, ident = None, *, options, populate_existing, with_for_update, identity_token, execution_options):
        '''Return an instance based on the given primary key identifier,
        or ``None`` if not found.

        .. seealso::

            :meth:`_orm.Session.get` - main documentation for get


        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def get_one(self = None, entity = None, ident = None, *, options, populate_existing, with_for_update, identity_token, execution_options):
        '''Return an instance based on the given primary key identifier,
        or raise an exception if not found.

        Raises :class:`_exc.NoResultFound` if the query selects no rows.

        ..versionadded: 2.0.22

        .. seealso::

            :meth:`_orm.Session.get_one` - main documentation for get_one

        '''
        pass
    # WARNING: Decompyle incomplete

    stream = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    stream = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    
    async def stream(self = None, statement = None, params = None, *, execution_options, bind_arguments, **kw):
        '''Execute a statement and return a streaming
        :class:`_asyncio.AsyncResult` object.

        '''
        pass
    # WARNING: Decompyle incomplete

    stream_scalars = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    stream_scalars = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    
    async def stream_scalars(self = None, statement = None, params = None, *, execution_options, bind_arguments, **kw):
        '''Execute a statement and return a stream of scalar results.

        :return: an :class:`_asyncio.AsyncScalarResult` object

        .. versionadded:: 1.4.24

        .. seealso::

            :meth:`_orm.Session.scalars` - main documentation for scalars

            :meth:`_asyncio.AsyncSession.scalars` - non streaming version

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, instance = None):
        '''Mark an instance as deleted.

        The database delete operation occurs upon ``flush()``.

        As this operation may need to cascade along unloaded relationships,
        it is awaitable to allow for those queries to take place.

        .. seealso::

            :meth:`_orm.Session.delete` - main documentation for delete

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def merge(self = None, instance = None, *, load, options):
        '''Copy the state of a given instance into a corresponding instance
        within this :class:`_asyncio.AsyncSession`.

        .. seealso::

            :meth:`_orm.Session.merge` - main documentation for merge

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def flush(self = None, objects = None):
        '''Flush all the object changes to the database.

        .. seealso::

            :meth:`_orm.Session.flush` - main documentation for flush

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_transaction(self = None):
        '''Return the current root transaction in progress, if any.

        :return: an :class:`_asyncio.AsyncSessionTransaction` object, or
         ``None``.

        .. versionadded:: 1.4.18

        '''
        trans = self.sync_session.get_transaction()
    # WARNING: Decompyle incomplete

    
    def get_nested_transaction(self = None):
        '''Return the current nested transaction in progress, if any.

        :return: an :class:`_asyncio.AsyncSessionTransaction` object, or
         ``None``.

        .. versionadded:: 1.4.18

        '''
        trans = self.sync_session.get_nested_transaction()
    # WARNING: Decompyle incomplete

    
    def get_bind(self = None, mapper = None, clause = None, bind = (None, None, None), **kw):
        '''Return a "bind" to which the synchronous proxied :class:`_orm.Session`
        is bound.

        Unlike the :meth:`_orm.Session.get_bind` method, this method is
        currently **not** used by this :class:`.AsyncSession` in any way
        in order to resolve engines for requests.

        .. note::

            This method proxies directly to the :meth:`_orm.Session.get_bind`
            method, however is currently **not** useful as an override target,
            in contrast to that of the :meth:`_orm.Session.get_bind` method.
            The example below illustrates how to implement custom
            :meth:`_orm.Session.get_bind` schemes that work with
            :class:`.AsyncSession` and :class:`.AsyncEngine`.

        The pattern introduced at :ref:`session_custom_partitioning`
        illustrates how to apply a custom bind-lookup scheme to a
        :class:`_orm.Session` given a set of :class:`_engine.Engine` objects.
        To apply a corresponding :meth:`_orm.Session.get_bind` implementation
        for use with a :class:`.AsyncSession` and :class:`.AsyncEngine`
        objects, continue to subclass :class:`_orm.Session` and apply it to
        :class:`.AsyncSession` using
        :paramref:`.AsyncSession.sync_session_class`. The inner method must
        continue to return :class:`_engine.Engine` instances, which can be
        acquired from a :class:`_asyncio.AsyncEngine` using the
        :attr:`_asyncio.AsyncEngine.sync_engine` attribute::

            # using example from "Custom Vertical Partitioning"


            import random

            from sqlalchemy.ext.asyncio import AsyncSession
            from sqlalchemy.ext.asyncio import create_async_engine
            from sqlalchemy.ext.asyncio import async_sessionmaker
            from sqlalchemy.orm import Session

            # construct async engines w/ async drivers
            engines = {
                "leader": create_async_engine("sqlite+aiosqlite:///leader.db"),
                "other": create_async_engine("sqlite+aiosqlite:///other.db"),
                "follower1": create_async_engine("sqlite+aiosqlite:///follower1.db"),
                "follower2": create_async_engine("sqlite+aiosqlite:///follower2.db"),
            }


            class RoutingSession(Session):
                def get_bind(self, mapper=None, clause=None, **kw):
                    # within get_bind(), return sync engines
                    if mapper and issubclass(mapper.class_, MyOtherClass):
                        return engines["other"].sync_engine
                    elif self._flushing or isinstance(clause, (Update, Delete)):
                        return engines["leader"].sync_engine
                    else:
                        return engines[
                            random.choice(["follower1", "follower2"])
                        ].sync_engine


            # apply to AsyncSession using sync_session_class
            AsyncSessionMaker = async_sessionmaker(sync_session_class=RoutingSession)

        The :meth:`_orm.Session.get_bind` method is called in a non-asyncio,
        implicitly non-blocking context in the same manner as ORM event hooks
        and functions that are invoked via :meth:`.AsyncSession.run_sync`, so
        routines that wish to run SQL commands inside of
        :meth:`_orm.Session.get_bind` can continue to do so using
        blocking-style code, which will be translated to implicitly async calls
        at the point of invoking IO on the database drivers.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def connection(self = None, bind_arguments = None, execution_options = None, **kw):
        '''Return a :class:`_asyncio.AsyncConnection` object corresponding to
        this :class:`.Session` object\'s transactional state.

        This method may also be used to establish execution options for the
        database connection used by the current transaction.

        .. versionadded:: 1.4.24  Added \\**kw arguments which are passed
           through to the underlying :meth:`_orm.Session.connection` method.

        .. seealso::

            :meth:`_orm.Session.connection` - main documentation for
            "connection"

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def begin(self = None):
        '''Return an :class:`_asyncio.AsyncSessionTransaction` object.

        The underlying :class:`_orm.Session` will perform the
        "begin" action when the :class:`_asyncio.AsyncSessionTransaction`
        object is entered::

            async with async_session.begin():
                ...  # ORM transaction is begun

        Note that database IO will not normally occur when the session-level
        transaction is begun, as database transactions begin on an
        on-demand basis.  However, the begin block is async to accommodate
        for a :meth:`_orm.SessionEvents.after_transaction_create`
        event hook that may perform IO.

        For a general description of ORM begin, see
        :meth:`_orm.Session.begin`.

        '''
        return AsyncSessionTransaction(self)

    
    def begin_nested(self = None):
        '''Return an :class:`_asyncio.AsyncSessionTransaction` object
        which will begin a "nested" transaction, e.g. SAVEPOINT.

        Behavior is the same as that of :meth:`_asyncio.AsyncSession.begin`.

        For a general description of ORM begin nested, see
        :meth:`_orm.Session.begin_nested`.

        .. seealso::

            :ref:`aiosqlite_serializable` - special workarounds required
            with the SQLite asyncio driver in order for SAVEPOINT to work
            correctly.

        '''
        return AsyncSessionTransaction(self, nested = True)

    
    async def rollback(self = None):
        '''Rollback the current transaction in progress.

        .. seealso::

            :meth:`_orm.Session.rollback` - main documentation for
            "rollback"
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def commit(self = None):
        '''Commit the current transaction in progress.

        .. seealso::

            :meth:`_orm.Session.commit` - main documentation for
            "commit"
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None):
        '''Close out the transactional resources and ORM objects used by this
        :class:`_asyncio.AsyncSession`.

        .. seealso::

            :meth:`_orm.Session.close` - main documentation for
            "close"

            :ref:`session_closing` - detail on the semantics of
            :meth:`_asyncio.AsyncSession.close` and
            :meth:`_asyncio.AsyncSession.reset`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def reset(self = None):
        '''Close out the transactional resources and ORM objects used by this
        :class:`_orm.Session`, resetting the session to its initial state.

        .. versionadded:: 2.0.22

        .. seealso::

            :meth:`_orm.Session.reset` - main documentation for
            "reset"

            :ref:`session_closing` - detail on the semantics of
            :meth:`_asyncio.AsyncSession.close` and
            :meth:`_asyncio.AsyncSession.reset`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        '''A synonym for :meth:`_asyncio.AsyncSession.close`.

        The :meth:`_asyncio.AsyncSession.aclose` name is specifically
        to support the Python standard library ``@contextlib.aclosing``
        context manager function.

        .. versionadded:: 2.0.20

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def invalidate(self = None):
        '''Close this Session, using connection invalidation.

        For a complete description, see :meth:`_orm.Session.invalidate`.
        '''
        pass
    # WARNING: Decompyle incomplete

    close_all = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()()
    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, type_ = None, value = None, traceback = ('type_', 'Any', 'value', 'Any', 'traceback', 'Any', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _maker_context_manager(self = None):
        return _AsyncSessionContextManager(self)

    
    def __contains__(self = None, instance = None):
        '''Return True if the instance is associated with this session.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        The instance may be pending or persistent within the Session for a
        result of True.


        '''
        return self._proxied.__contains__(instance)

    
    def __iter__(self = None):
        '''Iterate over all pending or persistent instances within this
        Session.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.


        '''
        return self._proxied.__iter__()

    
    def add(self = None, instance = None, _warn = None):
        '''Place an object into this :class:`_orm.Session`.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        Objects that are in the :term:`transient` state when passed to the
        :meth:`_orm.Session.add` method will move to the
        :term:`pending` state, until the next flush, at which point they
        will move to the :term:`persistent` state.

        Objects that are in the :term:`detached` state when passed to the
        :meth:`_orm.Session.add` method will move to the :term:`persistent`
        state directly.

        If the transaction used by the :class:`_orm.Session` is rolled back,
        objects which were transient when they were passed to
        :meth:`_orm.Session.add` will be moved back to the
        :term:`transient` state, and will no longer be present within this
        :class:`_orm.Session`.

        .. seealso::

            :meth:`_orm.Session.add_all`

            :ref:`session_adding` - at :ref:`session_basics`


        '''
        return self._proxied.add(instance, _warn = _warn)

    
    def add_all(self = None, instances = None):
        '''Add the given collection of instances to this :class:`_orm.Session`.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        See the documentation for :meth:`_orm.Session.add` for a general
        behavioral description.

        .. seealso::

            :meth:`_orm.Session.add`

            :ref:`session_adding` - at :ref:`session_basics`


        '''
        return self._proxied.add_all(instances)

    
    def expire(self = None, instance = None, attribute_names = None):
        """Expire the attributes on an instance.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        Marks the attributes of an instance as out of date. When an expired
        attribute is next accessed, a query will be issued to the
        :class:`.Session` object's current transactional context in order to
        load all expired attributes for the given instance.   Note that
        a highly isolated transaction will return the same values as were
        previously read in that same transaction, regardless of changes
        in database state outside of that transaction.

        To expire all objects in the :class:`.Session` simultaneously,
        use :meth:`Session.expire_all`.

        The :class:`.Session` object's default behavior is to
        expire all state whenever the :meth:`Session.rollback`
        or :meth:`Session.commit` methods are called, so that new
        state can be loaded for the new transaction.   For this reason,
        calling :meth:`Session.expire` only makes sense for the specific
        case that a non-ORM SQL statement was emitted in the current
        transaction.

        :param instance: The instance to be refreshed.
        :param attribute_names: optional list of string attribute names
          indicating a subset of attributes to be expired.

        .. seealso::

            :ref:`session_expire` - introductory material

            :meth:`.Session.expire`

            :meth:`.Session.refresh`

            :meth:`_orm.Query.populate_existing`


        """
        return self._proxied.expire(instance, attribute_names = attribute_names)

    
    def expire_all(self = None):
        """Expires all persistent instances within this Session.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        When any attributes on a persistent instance is next accessed,
        a query will be issued using the
        :class:`.Session` object's current transactional context in order to
        load all expired attributes for the given instance.   Note that
        a highly isolated transaction will return the same values as were
        previously read in that same transaction, regardless of changes
        in database state outside of that transaction.

        To expire individual objects and individual attributes
        on those objects, use :meth:`Session.expire`.

        The :class:`.Session` object's default behavior is to
        expire all state whenever the :meth:`Session.rollback`
        or :meth:`Session.commit` methods are called, so that new
        state can be loaded for the new transaction.   For this reason,
        calling :meth:`Session.expire_all` is not usually needed,
        assuming the transaction is isolated.

        .. seealso::

            :ref:`session_expire` - introductory material

            :meth:`.Session.expire`

            :meth:`.Session.refresh`

            :meth:`_orm.Query.populate_existing`


        """
        return self._proxied.expire_all()

    
    def expunge(self = None, instance = None):
        '''Remove the `instance` from this ``Session``.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        This will free all internal references to the instance.  Cascading
        will be applied according to the *expunge* cascade rule.


        '''
        return self._proxied.expunge(instance)

    
    def expunge_all(self = None):
        '''Remove all object instances from this ``Session``.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        This is equivalent to calling ``expunge(obj)`` on all objects in this
        ``Session``.


        '''
        return self._proxied.expunge_all()

    
    def is_modified(self = None, instance = None, include_collections = None):
        '''Return ``True`` if the given instance has locally
        modified attributes.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        This method retrieves the history for each instrumented
        attribute on the instance and performs a comparison of the current
        value to its previously flushed or committed value, if any.

        It is in effect a more expensive and accurate
        version of checking for the given instance in the
        :attr:`.Session.dirty` collection; a full test for
        each attribute\'s net "dirty" status is performed.

        E.g.::

            return session.is_modified(someobject)

        A few caveats to this method apply:

        * Instances present in the :attr:`.Session.dirty` collection may
          report ``False`` when tested with this method.  This is because
          the object may have received change events via attribute mutation,
          thus placing it in :attr:`.Session.dirty`, but ultimately the state
          is the same as that loaded from the database, resulting in no net
          change here.
        * Scalar attributes may not have recorded the previously set
          value when a new value was applied, if the attribute was not loaded,
          or was expired, at the time the new value was received - in these
          cases, the attribute is assumed to have a change, even if there is
          ultimately no net change against its database value. SQLAlchemy in
          most cases does not need the "old" value when a set event occurs, so
          it skips the expense of a SQL call if the old value isn\'t present,
          based on the assumption that an UPDATE of the scalar value is
          usually needed, and in those few cases where it isn\'t, is less
          expensive on average than issuing a defensive SELECT.

          The "old" value is fetched unconditionally upon set only if the
          attribute container has the ``active_history`` flag set to ``True``.
          This flag is set typically for primary key attributes and scalar
          object references that are not a simple many-to-one.  To set this
          flag for any arbitrary mapped column, use the ``active_history``
          argument with :func:`.column_property`.

        :param instance: mapped instance to be tested for pending changes.
        :param include_collections: Indicates if multivalued collections
         should be included in the operation.  Setting this to ``False`` is a
         way to detect only local-column based properties (i.e. scalar columns
         or many-to-one foreign keys) that would result in an UPDATE for this
         instance upon flush.


        '''
        return self._proxied.is_modified(instance, include_collections = include_collections)

    
    def in_transaction(self = None):
        '''Return True if this :class:`_orm.Session` has begun a transaction.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_orm.Session.is_active`



        '''
        return self._proxied.in_transaction()

    
    def in_nested_transaction(self = None):
        '''Return True if this :class:`_orm.Session` has begun a nested
        transaction, e.g. SAVEPOINT.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        .. versionadded:: 1.4


        '''
        return self._proxied.in_nested_transaction()

    dirty = (lambda self = None: self._proxied.dirty)()
    deleted = (lambda self = None: self._proxied.deleted)()
    new = (lambda self = None: self._proxied.new)()
    identity_map = (lambda self = None: self._proxied.identity_map)()
    identity_map = (lambda self = None, attr = None: self._proxied.identity_map = attr)()
    is_active = (lambda self = None: self._proxied.is_active)()
    autoflush = (lambda self = None: self._proxied.autoflush)()
    autoflush = (lambda self = None, attr = None: self._proxied.autoflush = attr)()
    no_autoflush = (lambda self = None: self._proxied.no_autoflush)()
    info = (lambda self = None: self._proxied.info)()
    object_session = (lambda cls = None, instance = None: Session.object_session(instance))()
    identity_key = (lambda cls = None, class_ = None, ident = None, *, instance, row, identity_token: Session.identity_key(class_ = class_, ident = ident, instance = instance, row = row, identity_token = identity_token))()

AsyncSession = <NODE:27>(AsyncSession, 'AsyncSession', ReversibleProxy[Session])()
_AS = TypeVar('_AS', bound = 'AsyncSession')

def async_sessionmaker():
    '''async_sessionmaker'''
    class_: 'Type[_AS]' = 'A configurable :class:`.AsyncSession` factory.\n\n    The :class:`.async_sessionmaker` factory works in the same way as the\n    :class:`.sessionmaker` factory, to generate new :class:`.AsyncSession`\n    objects when called, creating them given\n    the configurational arguments established here.\n\n    e.g.::\n\n        from sqlalchemy.ext.asyncio import create_async_engine\n        from sqlalchemy.ext.asyncio import AsyncSession\n        from sqlalchemy.ext.asyncio import async_sessionmaker\n\n\n        async def run_some_sql(\n            async_session: async_sessionmaker[AsyncSession],\n        ) -> None:\n            async with async_session() as session:\n                session.add(SomeObject(data="object"))\n                session.add(SomeOtherObject(name="other object"))\n                await session.commit()\n\n\n        async def main() -> None:\n            # an AsyncEngine, which the AsyncSession will use for connection\n            # resources\n            engine = create_async_engine(\n                "postgresql+asyncpg://scott:tiger@localhost/"\n            )\n\n            # create a reusable factory for new AsyncSession instances\n            async_session = async_sessionmaker(engine)\n\n            await run_some_sql(async_session)\n\n            await engine.dispose()\n\n    The :class:`.async_sessionmaker` is useful so that different parts\n    of a program can create new :class:`.AsyncSession` objects with a\n    fixed configuration established up front.  Note that :class:`.AsyncSession`\n    objects may also be instantiated directly when not using\n    :class:`.async_sessionmaker`.\n\n    .. versionadded:: 2.0  :class:`.async_sessionmaker` provides a\n       :class:`.sessionmaker` class that\'s dedicated to the\n       :class:`.AsyncSession` object, including pep-484 typing support.\n\n    .. seealso::\n\n        :ref:`asyncio_orm` - shows example use\n\n        :class:`.sessionmaker`  - general overview of the\n         :class:`.sessionmaker` architecture\n\n\n        :ref:`session_getting` - introductory text on creating\n        sessions using :class:`.sessionmaker`.\n\n    '
    __init__ = (lambda self = None, bind = None, *, class_, autoflush: pass)()
    __init__ = (lambda self = None, bind = None, *, autoflush, expire_on_commit: pass)()
    
    def __init__(self = None, bind = None, *, class_, autoflush, expire_on_commit, info, **kw):
        '''Construct a new :class:`.async_sessionmaker`.

        All arguments here except for ``class_`` correspond to arguments
        accepted by :class:`.Session` directly. See the
        :meth:`.AsyncSession.__init__` docstring for more details on
        parameters.


        '''
        kw['bind'] = bind
        kw['autoflush'] = autoflush
        kw['expire_on_commit'] = expire_on_commit
    # WARNING: Decompyle incomplete

    
    def begin(self = None):
        '''Produce a context manager that both provides a new
        :class:`_orm.AsyncSession` as well as a transaction that commits.


        e.g.::

            async def main():
                Session = async_sessionmaker(some_engine)

                async with Session.begin() as session:
                    session.add(some_object)

                # commits transaction, closes session

        '''
        session = self()
        return session._maker_context_manager()

    
    def __call__(self = None, **local_kw):
        '''Produce a new :class:`.AsyncSession` object using the configuration
        established in this :class:`.async_sessionmaker`.

        In Python, the ``__call__`` method is invoked on an object when
        it is "called" in the same way as a function::

            AsyncSession = async_sessionmaker(async_engine, expire_on_commit=False)
            session = AsyncSession()  # invokes sessionmaker.__call__()

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def configure(self = None, **new_kw):
        '''(Re)configure the arguments for this async_sessionmaker.

        e.g.::

            AsyncSession = async_sessionmaker(some_engine)

            AsyncSession.configure(bind=create_async_engine("sqlite+aiosqlite://"))
        '''
        self.kw.update(new_kw)

    
    def __repr__(self = None):
        return f'''(class_={self.class_.__name__!r}, {(lambda .0: pass# WARNING: Decompyle incomplete
)(self.kw.items()())!s})'''


async_sessionmaker = <NODE:27>(async_sessionmaker, 'async_sessionmaker', Generic[_AS])

def _AsyncSessionContextManager():
    '''_AsyncSessionContextManager'''
    trans: 'AsyncSessionTransaction' = ('async_session', 'trans')
    
    def __init__(self = None, async_session = None):
        self.async_session = async_session

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, type_ = None, value = None, traceback = ('type_', 'Any', 'value', 'Any', 'traceback', 'Any', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


_AsyncSessionContextManager = <NODE:27>(_AsyncSessionContextManager, '_AsyncSessionContextManager', Generic[_AS])

def AsyncSessionTransaction():
    '''AsyncSessionTransaction'''
    __doc__ = 'A wrapper for the ORM :class:`_orm.SessionTransaction` object.\n\n    This object is provided so that a transaction-holding object\n    for the :meth:`_asyncio.AsyncSession.begin` may be returned.\n\n    The object supports both explicit calls to\n    :meth:`_asyncio.AsyncSessionTransaction.commit` and\n    :meth:`_asyncio.AsyncSessionTransaction.rollback`, as well as use as an\n    async context manager.\n\n\n    .. versionadded:: 1.4\n\n    '
    sync_transaction: 'Optional[SessionTransaction]' = ('session', 'sync_transaction', 'nested')
    
    def __init__(self = None, session = None, nested = None):
        self.session = session
        self.nested = nested
        self.sync_transaction = None

    is_active = (lambda self = None: if self._sync_transaction() is not None:
passself._sync_transaction().is_active)()
    
    def _sync_transaction(self = None):
        if not self.sync_transaction:
            self._raise_for_not_started()
        return self.sync_transaction

    
    async def rollback(self = None):
        '''Roll back this :class:`_asyncio.AsyncTransaction`.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def commit(self = None):
        '''Commit this :class:`_asyncio.AsyncTransaction`.'''
        pass
    # WARNING: Decompyle incomplete

    _regenerate_proxy_for_target = (lambda cls = None, target = None, async_session = classmethod: sync_transaction = targetnested = target.nestedobj = cls.__new__(cls)obj.session = async_sessionobj.sync_transaction = obj._assign_proxied(sync_transaction)obj.nested = nestedobj)()
    
    async def start(self = None, is_ctxmanager = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, type_ = None, value = None, traceback = ('type_', 'Any', 'value', 'Any', 'traceback', 'Any', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


AsyncSessionTransaction = <NODE:27>(AsyncSessionTransaction, 'AsyncSessionTransaction', ReversibleProxy[SessionTransaction], StartableContext['AsyncSessionTransaction'])

def async_object_session(instance = None):
    '''Return the :class:`_asyncio.AsyncSession` to which the given instance
    belongs.

    This function makes use of the sync-API function
    :class:`_orm.object_session` to retrieve the :class:`_orm.Session` which
    refers to the given instance, and from there links it to the original
    :class:`_asyncio.AsyncSession`.

    If the :class:`_asyncio.AsyncSession` has been garbage collected, the
    return value is ``None``.

    This functionality is also available from the
    :attr:`_orm.InstanceState.async_session` accessor.

    :param instance: an ORM mapped instance
    :return: an :class:`_asyncio.AsyncSession` object, or ``None``.

    .. versionadded:: 1.4.18

    '''
    session = object_session(instance)
# WARNING: Decompyle incomplete


def async_session(session = None):
    '''Return the :class:`_asyncio.AsyncSession` which is proxying the given
    :class:`_orm.Session` object, if any.

    :param session: a :class:`_orm.Session` instance.
    :return: a :class:`_asyncio.AsyncSession` instance, or ``None``.

    .. versionadded:: 1.4.18

    '''
    return AsyncSession._retrieve_proxy_for_target(session, regenerate = False)


async def close_all_sessions():
    '''Close all :class:`_asyncio.AsyncSession` sessions.

    .. versionadded:: 2.0.23

    .. seealso::

        :func:`.session.close_all_sessions`

    '''
    pass
# WARNING: Decompyle incomplete

_instance_state._async_provider = async_session
