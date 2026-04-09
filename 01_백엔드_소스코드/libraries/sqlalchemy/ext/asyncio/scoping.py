# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scoping.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import Callable
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from session import _AS
from session import async_sessionmaker
from session import AsyncSession
from  import exc as sa_exc
from  import util
from orm.session import Session
from util import create_proxy_methods
from util import ScopedRegistry
from util import warn
from util import warn_deprecated
if TYPE_CHECKING:
    from engine import AsyncConnection
    from result import AsyncResult
    from result import AsyncScalarResult
    from session import AsyncSessionTransaction
    from engine import Connection
    from engine import Engine
    from engine import Result
    from engine import Row
    from engine import RowMapping
    from engine.interfaces import _CoreAnyExecuteParams
    from engine.interfaces import CoreExecuteOptionsParameter
    from engine.result import ScalarResult
    from orm._typing import _IdentityKeyType
    from orm._typing import _O
    from orm._typing import OrmExecuteOptionsParameter
    from orm.interfaces import ORMOption
    from orm.session import _BindArguments
    from orm.session import _EntityBindKey
    from orm.session import _PKIdentityArgument
    from orm.session import _SessionBind
    from sql.base import Executable
    from sql.elements import ClauseElement
    from sql.selectable import ForUpdateParameter
    from sql.selectable import TypedReturnsRows
_T = TypeVar('_T', bound = Any)

def async_scoped_session():
    '''async_scoped_session'''
    __doc__ = 'Provides scoped management of :class:`.AsyncSession` objects.\n\n    See the section :ref:`asyncio_scoped_session` for usage details.\n\n    .. versionadded:: 1.4.19\n\n\n    '
    registry: 'ScopedRegistry[_AS]' = True
    
    def __init__(self = None, session_factory = None, scopefunc = None):
        '''Construct a new :class:`_asyncio.async_scoped_session`.

        :param session_factory: a factory to create new :class:`_asyncio.AsyncSession`
         instances. This is usually, but not necessarily, an instance
         of :class:`_asyncio.async_sessionmaker`.

        :param scopefunc: function which defines
         the current scope.   A function such as ``asyncio.current_task``
         may be useful here.

        '''
        self.session_factory = session_factory
        self.registry = ScopedRegistry(session_factory, scopefunc)

    _proxied = (lambda self = None: self.registry())()
    
    def __call__(self = None, **kw):
        '''Return the current :class:`.AsyncSession`, creating it
        using the :attr:`.scoped_session.session_factory` if not present.

        :param \\**kw: Keyword arguments will be passed to the
         :attr:`.scoped_session.session_factory` callable, if an existing
         :class:`.AsyncSession` is not present.  If the
         :class:`.AsyncSession` is present
         and keyword arguments have been passed,
         :exc:`~sqlalchemy.exc.InvalidRequestError` is raised.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def configure(self = None, **kwargs):
        '''reconfigure the :class:`.sessionmaker` used by this
        :class:`.scoped_session`.

        See :meth:`.sessionmaker.configure`.

        '''
        if self.registry.has():
            warn('At least one scoped session is already present.  configure() can not affect sessions that have already been created.')
    # WARNING: Decompyle incomplete

    
    async def remove(self = None):
        """Dispose of the current :class:`.AsyncSession`, if present.

        Different from scoped_session's remove method, this method would use
        await to wait for the close method of AsyncSession.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self = None, instance = None):
        '''Return True if the instance is associated with this session.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.



        '''
        return self._proxied.__iter__()

    
    async def aclose(self = None):
        '''A synonym for :meth:`_asyncio.AsyncSession.close`.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        The :meth:`_asyncio.AsyncSession.aclose` name is specifically
        to support the Python standard library ``@contextlib.aclosing``
        context manager function.

        .. versionadded:: 2.0.20


        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add(self = None, instance = None, _warn = None):
        '''Place an object into this :class:`_orm.Session`.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

    
    def begin(self = None):
        '''Return an :class:`_asyncio.AsyncSessionTransaction` object.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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
        return self._proxied.begin()

    
    def begin_nested(self = None):
        '''Return an :class:`_asyncio.AsyncSessionTransaction` object
        which will begin a "nested" transaction, e.g. SAVEPOINT.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        Behavior is the same as that of :meth:`_asyncio.AsyncSession.begin`.

        For a general description of ORM begin nested, see
        :meth:`_orm.Session.begin_nested`.

        .. seealso::

            :ref:`aiosqlite_serializable` - special workarounds required
            with the SQLite asyncio driver in order for SAVEPOINT to work
            correctly.


        '''
        return self._proxied.begin_nested()

    
    async def close(self = None):
        '''Close out the transactional resources and ORM objects used by this
        :class:`_asyncio.AsyncSession`.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

    
    async def commit(self = None):
        '''Commit the current transaction in progress.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        .. seealso::

            :meth:`_orm.Session.commit` - main documentation for
            "commit"

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def connection(self = None, bind_arguments = None, execution_options = None, **kw):
        '''Return a :class:`_asyncio.AsyncConnection` object corresponding to
        this :class:`.Session` object\'s transactional state.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

    
    async def delete(self = None, instance = None):
        '''Mark an instance as deleted.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        The database delete operation occurs upon ``flush()``.

        As this operation may need to cascade along unloaded relationships,
        it is awaitable to allow for those queries to take place.

        .. seealso::

            :meth:`_orm.Session.delete` - main documentation for delete


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

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        .. seealso::

            :meth:`_orm.Session.execute` - main documentation for execute


        '''
        pass
    # WARNING: Decompyle incomplete

    
    def expire(self = None, instance = None, attribute_names = None):
        """Expire the attributes on an instance.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        This is equivalent to calling ``expunge(obj)`` on all objects in this
        ``Session``.



        '''
        return self._proxied.expunge_all()

    
    async def flush(self = None, objects = None):
        '''Flush all the object changes to the database.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        .. seealso::

            :meth:`_orm.Session.flush` - main documentation for flush


        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_bind(self = None, mapper = None, clause = None, bind = (None, None, None), **kw):
        '''Return a "bind" to which the synchronous proxied :class:`_orm.Session`
        is bound.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

    
    def is_modified(self = None, instance = None, include_collections = None):
        '''Return ``True`` if the given instance has locally
        modified attributes.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

    
    async def invalidate(self = None):
        '''Close this Session, using connection invalidation.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        For a complete description, see :meth:`_orm.Session.invalidate`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def merge(self = None, instance = None, *, load, options):
        '''Copy the state of a given instance into a corresponding instance
        within this :class:`_asyncio.AsyncSession`.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        .. seealso::

            :meth:`_orm.Session.merge` - main documentation for merge


        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def refresh(self = None, instance = None, attribute_names = None, with_for_update = (None, None)):
        '''Expire and refresh the attributes on the given instance.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        A query will be issued to the database and all attributes will be
        refreshed with their current database value.

        This is the async version of the :meth:`_orm.Session.refresh` method.
        See that method for a complete description of all options.

        .. seealso::

            :meth:`_orm.Session.refresh` - main documentation for refresh


        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def rollback(self = None):
        '''Rollback the current transaction in progress.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        .. seealso::

            :meth:`_orm.Session.rollback` - main documentation for
            "rollback"

        '''
        pass
    # WARNING: Decompyle incomplete

    scalar = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    scalar = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    
    async def scalar(self = None, statement = None, params = None, *, execution_options, bind_arguments, **kw):
        '''Execute a statement and return a scalar result.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        .. seealso::

            :meth:`_orm.Session.get` - main documentation for get



        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def get_one(self = None, entity = None, ident = None, *, options, populate_existing, with_for_update, identity_token, execution_options):
        '''Return an instance based on the given primary key identifier,
        or raise an exception if not found.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

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

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.


        '''
        pass
    # WARNING: Decompyle incomplete

    stream_scalars = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    stream_scalars = (lambda self = None, statement = None, params = None, *, execution_options, bind_arguments, kw = None: pass# WARNING: Decompyle incomplete
)()
    
    async def stream_scalars(self = None, statement = None, params = None, *, execution_options, bind_arguments, **kw):
        '''Execute a statement and return a stream of scalar results.

        .. container:: class_bases

            Proxied for the :class:`_asyncio.AsyncSession` class on
            behalf of the :class:`_asyncio.scoping.async_scoped_session` class.

        :return: an :class:`_asyncio.AsyncScalarResult` object

        .. versionadded:: 1.4.24

        .. seealso::

            :meth:`_orm.Session.scalars` - main documentation for scalars

            :meth:`_asyncio.AsyncSession.scalars` - non streaming version


        '''
        pass
    # WARNING: Decompyle incomplete

    bind = (lambda self = None: self._proxied.bind)()
    bind = (lambda self = None, attr = None: self._proxied.bind = attr)()
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
    close_all = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    object_session = (lambda cls = None, instance = None: AsyncSession.object_session(instance))()
    identity_key = (lambda cls = None, class_ = None, ident = None, *, instance, row, identity_token: AsyncSession.identity_key(class_ = class_, ident = ident, instance = instance, row = row, identity_token = identity_token))()

async_scoped_session = <NODE:27>(async_scoped_session, 'async_scoped_session', Generic[_AS])()
