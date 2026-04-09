# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''Base constructs for connection pools.'''
from __future__ import annotations
from collections import deque
import dataclasses
from enum import Enum
import threading
import time
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Deque
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import TYPE_CHECKING
from typing import Union
import weakref
from  import event
from  import exc
from  import log
from  import util
from util.typing import Literal
from util.typing import Protocol
if TYPE_CHECKING:
    from engine.interfaces import DBAPIConnection
    from engine.interfaces import DBAPICursor
    from engine.interfaces import Dialect
    from event import _DispatchCommon
    from event import _ListenerFnType
    from event import dispatcher
    from sql._typing import _InfoType
PoolResetState = <NODE:12>()

class ResetStyle(Enum):
    '''Describe options for "reset on return" behaviors.'''
    reset_rollback = 0
    reset_commit = 1
    reset_none = 2

_ResetStyleArgType = Union[(ResetStyle, Literal[(True, None, False, 'commit', 'rollback')])]
(reset_rollback, reset_commit, reset_none) = list(ResetStyle)

class _ConnDialect:
    '''partial implementation of :class:`.Dialect`
    which provides DBAPI connection methods.

    When a :class:`_pool.Pool` is combined with an :class:`_engine.Engine`,
    the :class:`_engine.Engine` replaces this with its own
    :class:`.Dialect`.

    '''
    is_async = False
    has_terminate = False
    
    def do_rollback(self = None, dbapi_connection = None):
        dbapi_connection.rollback()

    
    def do_commit(self = None, dbapi_connection = None):
        dbapi_connection.commit()

    
    def do_terminate(self = None, dbapi_connection = None):
        dbapi_connection.close()

    
    def do_close(self = None, dbapi_connection = None):
        dbapi_connection.close()

    
    def _do_ping_w_event(self = None, dbapi_connection = None):
        raise NotImplementedError('The ping feature requires that a dialect is passed to the connection pool.')

    
    def get_driver_connection(self = None, connection = None):
        return connection



class _AsyncConnDialect(_ConnDialect):
    is_async = True


class _CreatorFnType(Protocol):
    
    def __call__(self = None):
        pass



class _CreatorWRecFnType(Protocol):
    
    def __call__(self = None, rec = None):
        pass



class Pool(event.EventTarget, log.Identified):
    _orig_logging_name: 'Optional[str]' = 'Abstract base class for connection pools.'
    _invalidate_time: 'float' = _ConnDialect()
    
    def __init__(self, creator, recycle, echo, logging_name, reset_on_return = None, events = None, dialect = None, pre_ping = (-1, None, None, True, None, None, False, None), _dispatch = ('creator', 'Union[_CreatorFnType, _CreatorWRecFnType]', 'recycle', 'int', 'echo', 'log._EchoFlagType', 'logging_name', 'Optional[str]', 'reset_on_return', '_ResetStyleArgType', 'events', 'Optional[List[Tuple[_ListenerFnType, str]]]', 'dialect', 'Optional[Union[_ConnDialect, Dialect]]', 'pre_ping', 'bool', '_dispatch', 'Optional[_DispatchCommon[Pool]]')):
        '''
        Construct a Pool.

        :param creator: a callable function that returns a DB-API
          connection object.  The function will be called with
          parameters.

        :param recycle: If set to a value other than -1, number of
          seconds between connection recycling, which means upon
          checkout, if this timeout is surpassed the connection will be
          closed and replaced with a newly opened connection. Defaults to -1.

        :param logging_name:  String identifier which will be used within
          the "name" field of logging records generated within the
          "sqlalchemy.pool" logger. Defaults to a hexstring of the object\'s
          id.

        :param echo: if True, the connection pool will log
         informational output such as when connections are invalidated
         as well as when connections are recycled to the default log handler,
         which defaults to ``sys.stdout`` for output..   If set to the string
         ``"debug"``, the logging will include pool checkouts and checkins.

         The :paramref:`_pool.Pool.echo` parameter can also be set from the
         :func:`_sa.create_engine` call by using the
         :paramref:`_sa.create_engine.echo_pool` parameter.

         .. seealso::

             :ref:`dbengine_logging` - further detail on how to configure
             logging.

        :param reset_on_return: Determine steps to take on
         connections as they are returned to the pool, which were
         not otherwise handled by a :class:`_engine.Connection`.
         Available from :func:`_sa.create_engine` via the
         :paramref:`_sa.create_engine.pool_reset_on_return` parameter.

         :paramref:`_pool.Pool.reset_on_return` can have any of these values:

         * ``"rollback"`` - call rollback() on the connection,
           to release locks and transaction resources.
           This is the default value.  The vast majority
           of use cases should leave this value set.
         * ``"commit"`` - call commit() on the connection,
           to release locks and transaction resources.
           A commit here may be desirable for databases that
           cache query plans if a commit is emitted,
           such as Microsoft SQL Server.  However, this
           value is more dangerous than \'rollback\' because
           any data changes present on the transaction
           are committed unconditionally.
         * ``None`` - don\'t do anything on the connection.
           This setting may be appropriate if the database / DBAPI
           works in pure "autocommit" mode at all times, or if
           a custom reset handler is established using the
           :meth:`.PoolEvents.reset` event handler.

         * ``True`` - same as \'rollback\', this is here for
           backwards compatibility.
         * ``False`` - same as None, this is here for
           backwards compatibility.

         For further customization of reset on return, the
         :meth:`.PoolEvents.reset` event hook may be used which can perform
         any connection activity desired on reset.

         .. seealso::

            :ref:`pool_reset_on_return`

            :meth:`.PoolEvents.reset`

        :param events: a list of 2-tuples, each of the form
         ``(callable, target)`` which will be passed to :func:`.event.listen`
         upon construction.   Provided here so that event listeners
         can be assigned via :func:`_sa.create_engine` before dialect-level
         listeners are applied.

        :param dialect: a :class:`.Dialect` that will handle the job
         of calling rollback(), close(), or commit() on DBAPI connections.
         If omitted, a built-in "stub" dialect is used.   Applications that
         make use of :func:`_sa.create_engine` should not use this parameter
         as it is handled by the engine creation strategy.

        :param pre_ping: if True, the pool will emit a "ping" (typically
         "SELECT 1", but is dialect-specific) on the connection
         upon checkout, to test if the connection is alive or not.   If not,
         the connection is transparently re-connected and upon success, all
         other pooled connections established prior to that timestamp are
         invalidated.     Requires that a dialect is passed as well to
         interpret the disconnection error.

         .. versionadded:: 1.2

        '''
        if logging_name:
            self.logging_name = logging_name
            self._orig_logging_name = logging_name
        else:
            self._orig_logging_name = None
        log.instance_logger(self, echoflag = echo)
        self._creator = creator
        self._recycle = recycle
        self._invalidate_time = 0
        self._pre_ping = pre_ping
        self._reset_on_return = util.parse_user_argument_for_enum(reset_on_return, {
            ResetStyle.reset_commit: [
                'commit'],
            ResetStyle.reset_none: [
                'none',
                None,
                False],
            ResetStyle.reset_rollback: [
                'rollback',
                True] }, 'reset_on_return')
        self.echo = echo
        if _dispatch:
            self.dispatch._update(_dispatch, only_propagate = False)
        if dialect:
            self._dialect = dialect
        if events:
            for fn, target in events:
                event.listen(self, target, fn)
                return None
                return None

    _is_asyncio = (lambda self = None: self._dialect.is_async)()
    _creator = (lambda self = None: self._creator_arg)()
    _creator = (lambda self = None, creator = None: self._creator_arg = creatorself._invoke_creator = self._should_wrap_creator(creator))()
    _creator = (lambda self = None: del self._creator_argdel self._invoke_creator)()
    
    def _should_wrap_creator(self = None, creator = None):
        '''Detect if creator accepts a single argument, or is sent
        as a legacy style no-arg function.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _close_connection(self = None, connection = None, *, terminate):
        self.logger.debug('%s connection %r', 'Hard-closing' if terminate else 'Closing', connection)
        
        try:
            if terminate:
                self._dialect.do_terminate(connection)
                return None
            None._dialect.do_close(connection)
            return None
        except BaseException:
            e = None
            self.logger.error(f'''Exception {'terminating' if terminate else 'closing'} connection %r''', connection, exc_info = True)
            if not isinstance(e, Exception):
                raise 
            e = None
            del e
            return None
            e = None
            del e


    
    def _create_connection(self = None):
        '''Called by subclasses to create a new ConnectionRecord.'''
        return _ConnectionRecord(self)

    
    def _invalidate(self = None, connection = None, exception = None, _checkin = (None, True)):
        """Mark all connections established within the generation
        of the given connection as invalidated.

        If this pool's last invalidate time is before when the given
        connection was created, update the timestamp til now.  Otherwise,
        no action is performed.

        Connections with a start time prior to this pool's invalidation
        time will be recycled upon next checkout.
        """
        rec = getattr(connection, '_connection_record', None)
        if rec or self._invalidate_time < rec.starttime:
            self._invalidate_time = time.time()
        if _checkin or getattr(connection, 'is_valid', False):
            connection.invalidate(exception)
            return None
        return None

    
    def recreate(self = None):
        '''Return a new :class:`_pool.Pool`, of the same class as this one
        and configured with identical creation arguments.

        This method is used in conjunction with :meth:`dispose`
        to close out an entire :class:`_pool.Pool` and create a new one in
        its place.

        '''
        raise NotImplementedError()

    
    def dispose(self = None):
        '''Dispose of this pool.

        This method leaves the possibility of checked-out connections
        remaining open, as it only affects connections that are
        idle in the pool.

        .. seealso::

            :meth:`Pool.recreate`

        '''
        raise NotImplementedError()

    
    def connect(self = None):
        '''Return a DBAPI connection from the pool.

        The connection is instrumented such that when its
        ``close()`` method is called, the connection will be returned to
        the pool.

        '''
        return _ConnectionFairy._checkout(self)

    
    def _return_conn(self = None, record = None):
        '''Given a _ConnectionRecord, return it to the :class:`_pool.Pool`.

        This method is called when an instrumented DBAPI connection
        has its ``close()`` method called.

        '''
        self._do_return_conn(record)

    
    def _do_get(self = None):
        '''Implementation for :meth:`get`, supplied by subclasses.'''
        raise NotImplementedError()

    
    def _do_return_conn(self = None, record = None):
        '''Implementation for :meth:`return_conn`, supplied by subclasses.'''
        raise NotImplementedError()

    
    def status(self = None):
        '''Returns a brief description of the state of this pool.'''
        raise NotImplementedError()



class ManagesConnection:
    '''Common base for the two connection-management interfaces
    :class:`.PoolProxiedConnection` and :class:`.ConnectionPoolEntry`.

    These two objects are typically exposed in the public facing API
    via the connection pool event hooks, documented at :class:`.PoolEvents`.

    .. versionadded:: 2.0

    '''
    driver_connection: 'Optional[Any]' = ()
    info = (lambda self = None: raise NotImplementedError())()
    record_info = (lambda self = None: raise NotImplementedError())()
    
    def invalidate(self = None, e = None, soft = None):
        """Mark the managed connection as invalidated.

        :param e: an exception object indicating a reason for the invalidation.

        :param soft: if True, the connection isn't closed; instead, this
         connection will be recycled on next checkout.

        .. seealso::

            :ref:`pool_connection_invalidation`


        """
        raise NotImplementedError()



class ConnectionPoolEntry(ManagesConnection):
    '''Interface for the object that maintains an individual database
    connection on behalf of a :class:`_pool.Pool` instance.

    The :class:`.ConnectionPoolEntry` object represents the long term
    maintainance of a particular connection for a pool, including expiring or
    invalidating that connection to have it replaced with a new one, which will
    continue to be maintained by that same :class:`.ConnectionPoolEntry`
    instance. Compared to :class:`.PoolProxiedConnection`, which is the
    short-term, per-checkout connection manager, this object lasts for the
    lifespan of a particular "slot" within a connection pool.

    The :class:`.ConnectionPoolEntry` object is mostly visible to public-facing
    API code when it is delivered to connection pool event hooks, such as
    :meth:`_events.PoolEvents.connect` and :meth:`_events.PoolEvents.checkout`.

    .. versionadded:: 2.0  :class:`.ConnectionPoolEntry` provides the public
       facing interface for the :class:`._ConnectionRecord` internal class.

    '''
    __slots__ = ()
    in_use = (lambda self = None: raise NotImplementedError())()
    
    def close(self = None):
        '''Close the DBAPI connection managed by this connection pool entry.'''
        raise NotImplementedError()



class _ConnectionRecord(ConnectionPoolEntry):
    '''Maintains a position in a connection pool which references a pooled
    connection.

    This is an internal object used by the :class:`_pool.Pool` implementation
    to provide context management to a DBAPI connection maintained by
    that :class:`_pool.Pool`.   The public facing interface for this class
    is described by the :class:`.ConnectionPoolEntry` class.  See that
    class for public API details.

    .. seealso::

        :class:`.ConnectionPoolEntry`

        :class:`.PoolProxiedConnection`

    '''
    starttime: 'float' = ('__pool', 'fairy_ref', 'finalize_callback', 'fresh', 'starttime', 'dbapi_connection', '__weakref__', '__dict__')
    
    def dbapi_connection: 'Optional[DBAPIConnection]'(self = None, pool = None, connect = None):
        self.fresh = False
        self.fairy_ref = None
        self.starttime = 0
        self.dbapi_connection = None
        self._ConnectionRecord__pool = pool
        if connect:
            self._ConnectionRecord__connect()
        self.finalize_callback = deque()

    driver_connection = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    connection = (lambda self = None: self.dbapi_connection)()()
    _soft_invalidate_time: 'float' = 0
    info = (lambda self = None: { })()
    record_info = (lambda self = None: { })()
    checkout = (lambda cls = None, pool = None: pass# WARNING: Decompyle incomplete
)()
    
    def _checkin_failed(self = None, err = None, _fairy_was_created = None):
        self.invalidate(e = err)
        self.checkin(_fairy_was_created = _fairy_was_created)

    
    def checkin(self = None, _fairy_was_created = None):
        pass
    # WARNING: Decompyle incomplete

    in_use = (lambda self = None: self.fairy_ref is not None)()
    last_connect_time = (lambda self = None: self.starttime)()
    
    def close(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def invalidate(self = None, e = None, soft = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_connection(self = None):
        recycle = False
    # WARNING: Decompyle incomplete

    
    def _is_hard_or_soft_invalidated(self = None):
