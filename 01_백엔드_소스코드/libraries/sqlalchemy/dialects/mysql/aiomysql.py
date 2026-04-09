# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: aiomysql.pyc (Python 3.11)

'''
.. dialect:: mysql+aiomysql
    :name: aiomysql
    :dbapi: aiomysql
    :connectstring: mysql+aiomysql://user:password@host:port/dbname[?key=value&key=value...]
    :url: https://github.com/aio-libs/aiomysql

The aiomysql dialect is SQLAlchemy\'s second Python asyncio dialect.

Using a special asyncio mediation layer, the aiomysql dialect is usable
as the backend for the :ref:`SQLAlchemy asyncio <asyncio_toplevel>`
extension package.

This dialect should normally be used only with the
:func:`_asyncio.create_async_engine` engine creation function::

    from sqlalchemy.ext.asyncio import create_async_engine

    engine = create_async_engine(
        "mysql+aiomysql://user:pass@hostname/dbname?charset=utf8mb4"
    )

'''
from __future__ import annotations
from types import ModuleType
from typing import Any
from typing import Dict
from typing import Optional
from typing import Tuple
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

class AsyncAdapt_aiomysql_cursor(AsyncAdapt_dbapi_cursor):
    __slots__ = ()
    
    def _make_new_cursor(self = None, connection = None):
        return connection.cursor(self._adapt_connection.dbapi.Cursor)



class AsyncAdapt_aiomysql_ss_cursor(AsyncAdapt_aiomysql_cursor, AsyncAdapt_dbapi_ss_cursor):
    __slots__ = ()
    
    def _make_new_cursor(self = None, connection = None):
        return connection.cursor(self._adapt_connection.dbapi.aiomysql.cursors.SSCursor)



class AsyncAdapt_aiomysql_connection(AsyncAdapt_dbapi_connection, AsyncAdapt_terminate):
    __slots__ = ()
    _cursor_cls = AsyncAdapt_aiomysql_cursor
    _ss_cursor_cls = AsyncAdapt_aiomysql_ss_cursor
    
    def ping(self = None, reconnect = None):
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



class AsyncAdaptFallback_aiomysql_connection(AsyncAdapt_aiomysql_connection):
    __slots__ = ()
    await_ = staticmethod(await_fallback)


class AsyncAdapt_aiomysql_dbapi(AsyncAdapt_dbapi_module):
    
    def __init__(self = None, aiomysql = None, pymysql = None):
        self.aiomysql = aiomysql
        self.pymysql = pymysql
        self.paramstyle = 'format'
        self._init_dbapi_attributes()
        (self.Cursor, self.SSCursor) = self._init_cursors_subclasses()

    
    def _init_dbapi_attributes(self = None):
        for name in ('Warning', 'Error', 'InterfaceError', 'DataError', 'DatabaseError', 'OperationalError', 'InterfaceError', 'IntegrityError', 'ProgrammingError', 'InternalError', 'NotSupportedError'):
            setattr(self, name, getattr(self.aiomysql, name))
            for name in ('NUMBER', 'STRING', 'DATETIME', 'BINARY', 'TIMESTAMP', 'Binary'):
                setattr(self, name, getattr(self.pymysql, name))
                return None

    
    def connect(self = None, *arg, **kw):
        async_fallback = kw.pop('async_fallback', False)
        creator_fn = kw.pop('async_creator_fn', self.aiomysql.connect)
    # WARNING: Decompyle incomplete

    
    def _init_cursors_subclasses(self = None):
        
        class Cursor(self.aiomysql.Cursor):
            
            async def _show_warnings(self = None, conn = None):
                pass
            # WARNING: Decompyle incomplete


        
        class SSCursor(self.aiomysql.SSCursor):
            
            async def _show_warnings(self = None, conn = None):
                pass
            # WARNING: Decompyle incomplete


        return (Cursor, SSCursor)



class MySQLDialect_aiomysql(MySQLDialect_pymysql):
    pass
# WARNING: Decompyle incomplete

dialect = MySQLDialect_aiomysql
