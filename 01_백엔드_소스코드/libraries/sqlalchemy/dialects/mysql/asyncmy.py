# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: asyncmy.pyc (Python 3.11)

'''
.. dialect:: mysql+asyncmy
    :name: asyncmy
    :dbapi: asyncmy
    :connectstring: mysql+asyncmy://user:password@host:port/dbname[?key=value&key=value...]
    :url: https://github.com/long2ice/asyncmy

Using a special asyncio mediation layer, the asyncmy dialect is usable
as the backend for the :ref:`SQLAlchemy asyncio <asyncio_toplevel>`
extension package.

This dialect should normally be used only with the
:func:`_asyncio.create_async_engine` engine creation function::

    from sqlalchemy.ext.asyncio import create_async_engine

    engine = create_async_engine(
        "mysql+asyncmy://user:pass@hostname/dbname?charset=utf8mb4"
    )

'''
from __future__ import annotations
from types import ModuleType
from typing import Any
from typing import NoReturn
from typing import Optional
from typing import TYPE_CHECKING
from typing import Union
from pymysql import MySQLDialect_pymysql
from  import pool
from  import util
from connectors.asyncio import AsyncAdapt_dbapi_connection
from connectors.asyncio import AsyncAdapt_dbapi_cursor
from connectors.asyncio import AsyncAdapt_dbapi_module
from connectors.asyncio import AsyncAdapt_dbapi_ss_cursor
from connectors.asyncio import AsyncAdapt_terminate
from util.concurrency import await_fallback
from util.concurrency import await_only
if TYPE_CHECKING:
    from connectors.asyncio import AsyncIODBAPIConnection
    from connectors.asyncio import AsyncIODBAPICursor
    from engine.interfaces import ConnectArgsType
    from engine.interfaces import DBAPIConnection
    from engine.interfaces import DBAPICursor
    from engine.interfaces import DBAPIModule
    from engine.interfaces import PoolProxiedConnection
    from engine.url import URL

class AsyncAdapt_asyncmy_cursor(AsyncAdapt_dbapi_cursor):
    __slots__ = ()


class AsyncAdapt_asyncmy_ss_cursor(AsyncAdapt_asyncmy_cursor, AsyncAdapt_dbapi_ss_cursor):
    __slots__ = ()
    
    def _make_new_cursor(self = None, connection = None):
        return connection.cursor(self._adapt_connection.dbapi.asyncmy.cursors.SSCursor)



class AsyncAdapt_asyncmy_connection(AsyncAdapt_dbapi_connection, AsyncAdapt_terminate):
    __slots__ = ()
    _cursor_cls = AsyncAdapt_asyncmy_cursor
    _ss_cursor_cls = AsyncAdapt_asyncmy_ss_cursor
    
    def _handle_exception(self = None, error = None):
        if isinstance(error, AttributeError):
            raise self.dbapi.InternalError('network operation failed due to asyncmy attribute error')
        raise error

    
    def ping(self = None, reconnect = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _do_ping(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def character_set_name(self = None):
        return self._connection.character_set_name()

    
    def autocommit(self = None, value = None):
        self.await_(self._connection.autocommit(value))

    
    def get_autocommit(self = None):
        return self._connection.get_autocommit()

    
    def close(self = None):
        self.await_(self._connection.ensure_closed())

    
    async def _terminate_graceful_close(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _terminate_force_close(self = None):
        self._connection.close()



class AsyncAdaptFallback_asyncmy_connection(AsyncAdapt_asyncmy_connection):
    __slots__ = ()
    await_ = staticmethod(await_fallback)


class AsyncAdapt_asyncmy_dbapi(AsyncAdapt_dbapi_module):
    
    def __init__(self = None, asyncmy = None):
        self.asyncmy = asyncmy
        self.paramstyle = 'format'
        self._init_dbapi_attributes()

    
    def _init_dbapi_attributes(self = None):
        for name in ('Warning', 'Error', 'InterfaceError', 'DataError', 'DatabaseError', 'OperationalError', 'InterfaceError', 'IntegrityError', 'ProgrammingError', 'InternalError', 'NotSupportedError'):
            setattr(self, name, getattr(self.asyncmy.errors, name))
            return None

    STRING = util.symbol('STRING')
    NUMBER = util.symbol('NUMBER')
    BINARY = util.symbol('BINARY')
    DATETIME = util.symbol('DATETIME')
    TIMESTAMP = util.symbol('TIMESTAMP')
    Binary = staticmethod(bytes)
    
    def connect(self = None, *arg, **kw):
        async_fallback = kw.pop('async_fallback', False)
        creator_fn = kw.pop('async_creator_fn', self.asyncmy.connect)
    # WARNING: Decompyle incomplete



class MySQLDialect_asyncmy(MySQLDialect_pymysql):
    pass
# WARNING: Decompyle incomplete

dialect = MySQLDialect_asyncmy
