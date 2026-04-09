# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: engine.pyc (Python 3.11)

from __future__ import annotations
import asyncio
import contextlib
from typing import Any
from typing import AsyncIterator
from typing import Callable
from typing import Dict
from typing import Generator
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import exc as async_exc
from base import asyncstartablecontext
from base import GeneratorStartableContext
from base import ProxyComparable
from base import StartableContext
from result import _ensure_sync_result
from result import AsyncResult
from result import AsyncScalarResult
from  import exc
from  import inspection
from  import util
from engine import Connection
from engine import create_engine as _create_engine
from engine import create_pool_from_url as _create_pool_from_url
from engine import Engine
from engine.base import NestedTransaction
from engine.base import Transaction
from exc import ArgumentError
from util.concurrency import greenlet_spawn
from util.typing import Concatenate
from util.typing import ParamSpec
if TYPE_CHECKING:
    from engine.cursor import CursorResult
    from engine.interfaces import _CoreAnyExecuteParams
    from engine.interfaces import _CoreSingleExecuteParams
    from engine.interfaces import _DBAPIAnyExecuteParams
    from engine.interfaces import _ExecuteOptions
    from engine.interfaces import CompiledCacheType
    from engine.interfaces import CoreExecuteOptionsParameter
    from engine.interfaces import Dialect
    from engine.interfaces import IsolationLevel
    from engine.interfaces import SchemaTranslateMapType
    from engine.result import ScalarResult
    from engine.url import URL
    from pool import Pool
    from pool import PoolProxiedConnection
    from sql._typing import _InfoType
    from sql.base import Executable
    from sql.selectable import TypedReturnsRows
_P = ParamSpec('_P')
_T = TypeVar('_T', bound = Any)

def create_async_engine(url = None, **kw):
    '''Create a new async engine instance.

    Arguments passed to :func:`_asyncio.create_async_engine` are mostly
    identical to those passed to the :func:`_sa.create_engine` function.
    The specified dialect must be an asyncio-compatible dialect
    such as :ref:`dialect-postgresql-asyncpg`.

    .. versionadded:: 1.4

    :param async_creator: an async callable which returns a driver-level
        asyncio connection. If given, the function should take no arguments,
        and return a new asyncio connection from the underlying asyncio
        database driver; the connection will be wrapped in the appropriate
        structures to be used with the :class:`.AsyncEngine`.   Note that the
        parameters specified in the URL are not applied here, and the creator
        function should use its own connection parameters.

        This parameter is the asyncio equivalent of the
        :paramref:`_sa.create_engine.creator` parameter of the
        :func:`_sa.create_engine` function.

        .. versionadded:: 2.0.16

    '''
    pass
# WARNING: Decompyle incomplete


def async_engine_from_config(configuration = None, prefix = None, **kwargs):
    '''Create a new AsyncEngine instance using a configuration dictionary.

    This function is analogous to the :func:`_sa.engine_from_config` function
    in SQLAlchemy Core, except that the requested dialect must be an
    asyncio-compatible dialect such as :ref:`dialect-postgresql-asyncpg`.
    The argument signature of the function is identical to that
    of :func:`_sa.engine_from_config`.

    .. versionadded:: 1.4.29

    '''
    pass
# WARNING: Decompyle incomplete


def create_async_pool_from_url(url = None, **kwargs):
    '''Create a new async engine instance.

    Arguments passed to :func:`_asyncio.create_async_pool_from_url` are mostly
    identical to those passed to the :func:`_sa.create_pool_from_url` function.
    The specified dialect must be an asyncio-compatible dialect
    such as :ref:`dialect-postgresql-asyncpg`.

    .. versionadded:: 2.0.10

    '''
    kwargs['_is_async'] = True
# WARNING: Decompyle incomplete


class AsyncConnectable:
    __slots__ = ('_slots_dispatch', '__weakref__')
    _no_async_engine_events = (lambda cls = None: raise NotImplementedError('asynchronous events are not implemented at this time.  Apply synchronous listeners to the AsyncEngine.sync_engine or AsyncConnection.sync_connection attributes.'))()


def AsyncConnection():
    '''AsyncConnection'''
    __doc__ = 'An asyncio proxy for a :class:`_engine.Connection`.\n\n    :class:`_asyncio.AsyncConnection` is acquired using the\n    :meth:`_asyncio.AsyncEngine.connect`\n    method of :class:`_asyncio.AsyncEngine`::\n\n        from sqlalchemy.ext.asyncio import create_async_engine\n\n        engine = create_async_engine("postgresql+asyncpg://user:pass@host/dbname")\n\n        async with engine.connect() as conn:\n            result = await conn.execute(select(table))\n\n    .. versionadded:: 1.4\n\n    '
    __slots__ = ('engine', 'sync_engine', 'sync_connection')
    
    def sync_engine: 'Engine'(self = None, async_engine = None, sync_connection = None):
        self.engine = async_engine
        self.sync_engine = async_engine.sync_engine
        self.sync_connection = self._assign_proxied(sync_connection)

    _regenerate_proxy_for_target = (lambda cls = None, target = None: AsyncConnection(AsyncEngine._retrieve_proxy_for_target(target.engine), target))()
    
    async def start(self = None, is_ctxmanager = None):
        """Start this :class:`_asyncio.AsyncConnection` object's context
        outside of using a Python ``with:`` block.

        """
        pass
    # WARNING: Decompyle incomplete

    connection = (lambda self = None: raise exc.InvalidRequestError('AsyncConnection.connection accessor is not implemented as the attribute may need to reconnect on an invalidated connection.  Use the get_raw_connection() method.'))()
    
    async def get_raw_connection(self = None):
        '''Return the pooled DBAPI-level connection in use by this
        :class:`_asyncio.AsyncConnection`.

        This is a SQLAlchemy connection-pool proxied connection
        which then has the attribute
        :attr:`_pool._ConnectionFairy.driver_connection` that refers to the
        actual driver connection. Its
        :attr:`_pool._ConnectionFairy.dbapi_connection` refers instead
        to an :class:`_engine.AdaptedConnection` instance that
        adapts the driver connection to the DBAPI protocol.

        '''
        pass
    # WARNING: Decompyle incomplete

    info = (lambda self = None: self._proxied.info)()
    _proxied = (lambda self = None: if not self.sync_connection:
self._raise_for_not_started()self.sync_connection)()
    
    def begin(self = None):
        '''Begin a transaction prior to autobegin occurring.'''
        pass
    # WARNING: Decompyle incomplete

    
    def begin_nested(self = None):
        '''Begin a nested transaction and return a transaction handle.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def invalidate(self = None, exception = None):
        '''Invalidate the underlying DBAPI connection associated with
        this :class:`_engine.Connection`.

        See the method :meth:`_engine.Connection.invalidate` for full
        detail on this method.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def get_isolation_level(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def in_transaction(self = None):
        '''Return True if a transaction is in progress.'''
        return self._proxied.in_transaction()

    
    def in_nested_transaction(self = None):
        '''Return True if a transaction is in progress.

        .. versionadded:: 1.4.0b2

        '''
        return self._proxied.in_nested_transaction()

    
    def get_transaction(self = None):
        """Return an :class:`.AsyncTransaction` representing the current
        transaction, if any.

        This makes use of the underlying synchronous connection's
        :meth:`_engine.Connection.get_transaction` method to get the current
        :class:`_engine.Transaction`, which is then proxied in a new
        :class:`.AsyncTransaction` object.

        .. versionadded:: 1.4.0b2

        """
        trans = self._proxied.get_transaction()
    # WARNING: Decompyle incomplete

    
    def get_nested_transaction(self = None):
        """Return an :class:`.AsyncTransaction` representing the current
        nested (savepoint) transaction, if any.

        This makes use of the underlying synchronous connection's
        :meth:`_engine.Connection.get_nested_transaction` method to get the
        current :class:`_engine.Transaction`, which is then proxied in a new
        :class:`.AsyncTransaction` object.

        .. versionadded:: 1.4.0b2

        """
        trans = self._proxied.get_nested_transaction()
    # WARNING: Decompyle incomplete

    execution_options = (lambda self = None, *, compiled_cache: pass# WARNING: Decompyle incomplete
)()
    execution_options = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    async def execution_options(self = None, **opt):
        '''Set non-SQL options for the connection which take effect
        during execution.

        This returns this :class:`_asyncio.AsyncConnection` object with
        the new options added.

        See :meth:`_engine.Connection.execution_options` for full details
        on this method.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def commit(self = None):
        '''Commit the transaction that is currently in progress.

        This method commits the current transaction if one has been started.
        If no transaction was started, the method has no effect, assuming
        the connection is in a non-invalidated state.

        A transaction is begun on a :class:`_engine.Connection` automatically
        whenever a statement is first executed, or when the
        :meth:`_engine.Connection.begin` method is called.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def rollback(self = None):
        '''Roll back the transaction that is currently in progress.

        This method rolls back the current transaction if one has been started.
        If no transaction was started, the method has no effect.  If a
        transaction was started and the connection is in an invalidated state,
        the transaction is cleared using this method.

        A transaction is begun on a :class:`_engine.Connection` automatically
        whenever a statement is first executed, or when the
        :meth:`_engine.Connection.begin` method is called.


        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None):
        '''Close this :class:`_asyncio.AsyncConnection`.

        This has the effect of also rolling back the transaction if one
        is in place.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        '''A synonym for :meth:`_asyncio.AsyncConnection.close`.

        The :meth:`_asyncio.AsyncConnection.aclose` name is specifically
        to support the Python standard library ``@contextlib.aclosing``
        context manager function.

        .. versionadded:: 2.0.20

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def exec_driver_sql(self = None, statement = None, parameters = None, execution_options = (None, None)):
        '''Executes a driver-level SQL string and return buffered
        :class:`_engine.Result`.

        '''
        pass
    # WARNING: Decompyle incomplete

    stream = (lambda self = None, statement = None, parameters = None, *, execution_options,
