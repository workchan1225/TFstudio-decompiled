# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: events.pyc (Python 3.11)

from __future__ import annotations
import typing
from typing import Any
from typing import Optional
from typing import Type
from typing import Union
from base import ConnectionPoolEntry
from base import Pool
from base import PoolProxiedConnection
from base import PoolResetState
from  import event
from  import util
if typing.TYPE_CHECKING:
    from engine import Engine
    from engine.interfaces import DBAPIConnection

def PoolEvents():
    '''PoolEvents'''
    __doc__ = 'Available events for :class:`_pool.Pool`.\n\n    The methods here define the name of an event as well\n    as the names of members that are passed to listener\n    functions.\n\n    e.g.::\n\n        from sqlalchemy import event\n\n\n        def my_on_checkout(dbapi_conn, connection_rec, connection_proxy):\n            "handle an on checkout event"\n\n\n        event.listen(Pool, "checkout", my_on_checkout)\n\n    In addition to accepting the :class:`_pool.Pool` class and\n    :class:`_pool.Pool` instances, :class:`_events.PoolEvents` also accepts\n    :class:`_engine.Engine` objects and the :class:`_engine.Engine` class as\n    targets, which will be resolved to the ``.pool`` attribute of the\n    given engine or the :class:`_pool.Pool` class::\n\n        engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/test")\n\n        # will associate with engine.pool\n        event.listen(engine, "checkout", my_on_checkout)\n\n    '
    _target_class_doc = 'SomeEngineOrPool'
    _dispatch_target = Pool
    _accept_with = (lambda cls = None, target = util.preload_module('sqlalchemy.engine'), identifier = classmethod: if not typing.TYPE_CHECKING:
Engine = util.preloaded.engine.Engine# WARNING: Decompyle incomplete
)()()
    _listen = (lambda cls = None, event_key = None: target = event_key.dispatch_targetkw.setdefault('asyncio', target._is_asyncio)# WARNING: Decompyle incomplete
)()
    
    def connect(self = None, dbapi_connection = None, connection_record = None):
        '''Called at the moment a particular DBAPI connection is first
        created for a given :class:`_pool.Pool`.

        This event allows one to capture the point directly after which
        the DBAPI module-level ``.connect()`` method has been used in order
        to produce a new DBAPI connection.

        :param dbapi_connection: a DBAPI connection.
         The :attr:`.ConnectionPoolEntry.dbapi_connection` attribute.

        :param connection_record: the :class:`.ConnectionPoolEntry` managing
         the DBAPI connection.

        '''
        pass

    
    def first_connect(self = None, dbapi_connection = None, connection_record = None):
        '''Called exactly once for the first time a DBAPI connection is
        checked out from a particular :class:`_pool.Pool`.

        The rationale for :meth:`_events.PoolEvents.first_connect`
        is to determine
        information about a particular series of database connections based
        on the settings used for all connections.  Since a particular
        :class:`_pool.Pool`
        refers to a single "creator" function (which in terms
        of a :class:`_engine.Engine`
        refers to the URL and connection options used),
        it is typically valid to make observations about a single connection
        that can be safely assumed to be valid about all subsequent
        connections, such as the database version, the server and client
        encoding settings, collation settings, and many others.

        :param dbapi_connection: a DBAPI connection.
         The :attr:`.ConnectionPoolEntry.dbapi_connection` attribute.

        :param connection_record: the :class:`.ConnectionPoolEntry` managing
         the DBAPI connection.

        '''
        pass

    
    def checkout(self = None, dbapi_connection = None, connection_record = None, connection_proxy = ('dbapi_connection', 'DBAPIConnection', 'connection_record', 'ConnectionPoolEntry', 'connection_proxy', 'PoolProxiedConnection', 'return', 'None')):
        '''Called when a connection is retrieved from the Pool.

        :param dbapi_connection: a DBAPI connection.
         The :attr:`.ConnectionPoolEntry.dbapi_connection` attribute.

        :param connection_record: the :class:`.ConnectionPoolEntry` managing
         the DBAPI connection.

        :param connection_proxy: the :class:`.PoolProxiedConnection` object
          which will proxy the public interface of the DBAPI connection for the
          lifespan of the checkout.

        If you raise a :class:`~sqlalchemy.exc.DisconnectionError`, the current
        connection will be disposed and a fresh connection retrieved.
        Processing of all checkout listeners will abort and restart
        using the new connection.

        .. seealso:: :meth:`_events.ConnectionEvents.engine_connect`
           - a similar event
           which occurs upon creation of a new :class:`_engine.Connection`.

        '''
        pass

    
    def checkin(self = None, dbapi_connection = None, connection_record = None):
        '''Called when a connection returns to the pool.

        Note that the connection may be closed, and may be None if the
        connection has been invalidated.  ``checkin`` will not be called
        for detached connections.  (They do not return to the pool.)

        :param dbapi_connection: a DBAPI connection.
         The :attr:`.ConnectionPoolEntry.dbapi_connection` attribute.

        :param connection_record: the :class:`.ConnectionPoolEntry` managing
         the DBAPI connection.

        '''
        pass

    reset = (lambda self = None, dbapi_connection = None, connection_record = event._legacy_signature('2.0', [
        'dbapi_connection',
        'connection_record'], (lambda dbapi_connection, connection_record, reset_state: (dbapi_connection, connection_record))), reset_state = ('dbapi_connection', 'DBAPIConnection', 'connection_record', 'ConnectionPoolEntry', 'reset_state', 'PoolResetState', 'return', 'None'): pass)()
    
    def invalidate(self = None, dbapi_connection = None, connection_record = None, exception = ('dbapi_connection', 'DBAPIConnection', 'connection_record', 'ConnectionPoolEntry', 'exception', 'Optional[BaseException]', 'return', 'None')):
        '''Called when a DBAPI connection is to be "invalidated".

        This event is called any time the
        :meth:`.ConnectionPoolEntry.invalidate` method is invoked, either from
        API usage or via "auto-invalidation", without the ``soft`` flag.

        The event occurs before a final attempt to call ``.close()`` on the
        connection occurs.

        :param dbapi_connection: a DBAPI connection.
         The :attr:`.ConnectionPoolEntry.dbapi_connection` attribute.

        :param connection_record: the :class:`.ConnectionPoolEntry` managing
         the DBAPI connection.

        :param exception: the exception object corresponding to the reason
         for this invalidation, if any.  May be ``None``.

        .. seealso::

            :ref:`pool_connection_invalidation`

        '''
        pass

    
    def soft_invalidate(self = None, dbapi_connection = None, connection_record = None, exception = ('dbapi_connection', 'DBAPIConnection', 'connection_record', 'ConnectionPoolEntry', 'exception', 'Optional[BaseException]', 'return', 'None')):
        '''Called when a DBAPI connection is to be "soft invalidated".

        This event is called any time the
        :meth:`.ConnectionPoolEntry.invalidate`
        method is invoked with the ``soft`` flag.

        Soft invalidation refers to when the connection record that tracks
        this connection will force a reconnect after the current connection
        is checked in.   It does not actively close the dbapi_connection
        at the point at which it is called.

        :param dbapi_connection: a DBAPI connection.
         The :attr:`.ConnectionPoolEntry.dbapi_connection` attribute.

        :param connection_record: the :class:`.ConnectionPoolEntry` managing
         the DBAPI connection.

        :param exception: the exception object corresponding to the reason
         for this invalidation, if any.  May be ``None``.

        '''
        pass

    
    def close(self = None, dbapi_connection = None, connection_record = None):
        """Called when a DBAPI connection is closed.

        The event is emitted before the close occurs.

        The close of a connection can fail; typically this is because
        the connection is already closed.  If the close operation fails,
        the connection is discarded.

        The :meth:`.close` event corresponds to a connection that's still
        associated with the pool. To intercept close events for detached
        connections use :meth:`.close_detached`.

        :param dbapi_connection: a DBAPI connection.
         The :attr:`.ConnectionPoolEntry.dbapi_connection` attribute.

        :param connection_record: the :class:`.ConnectionPoolEntry` managing
         the DBAPI connection.

        """
        pass

    
    def detach(self = None, dbapi_connection = None, connection_record = None):
        '''Called when a DBAPI connection is "detached" from a pool.

        This event is emitted after the detach occurs.  The connection
        is no longer associated with the given connection record.

        :param dbapi_connection: a DBAPI connection.
         The :attr:`.ConnectionPoolEntry.dbapi_connection` attribute.

        :param connection_record: the :class:`.ConnectionPoolEntry` managing
         the DBAPI connection.

        '''
        pass

    
    def close_detached(self = None, dbapi_connection = None):
        '''Called when a detached DBAPI connection is closed.

        The event is emitted before the close occurs.

        The close of a connection can fail; typically this is because
        the connection is already closed.  If the close operation fails,
        the connection is discarded.

        :param dbapi_connection: a DBAPI connection.
         The :attr:`.ConnectionPoolEntry.dbapi_connection` attribute.

        '''
        pass


PoolEvents = <NODE:27>(PoolEvents, 'PoolEvents', event.Events[Pool])
