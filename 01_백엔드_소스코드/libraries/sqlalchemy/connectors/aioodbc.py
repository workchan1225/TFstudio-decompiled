# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: aioodbc.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
from asyncio import AsyncAdapt_dbapi_connection
from asyncio import AsyncAdapt_dbapi_cursor
from asyncio import AsyncAdapt_dbapi_ss_cursor
from asyncio import AsyncAdaptFallback_dbapi_connection
from pyodbc import PyODBCConnector
from  import pool
from  import util
from util.concurrency import await_fallback
from util.concurrency import await_only
if TYPE_CHECKING:
    from engine.interfaces import ConnectArgsType
    from engine.url import URL

class AsyncAdapt_aioodbc_cursor(AsyncAdapt_dbapi_cursor):
    __slots__ = ()
    
    def setinputsizes(self, *inputsizes):
        pass
    # WARNING: Decompyle incomplete



class AsyncAdapt_aioodbc_ss_cursor(AsyncAdapt_dbapi_ss_cursor, AsyncAdapt_aioodbc_cursor):
    __slots__ = ()


class AsyncAdapt_aioodbc_connection(AsyncAdapt_dbapi_connection):
    pass
# WARNING: Decompyle incomplete


class AsyncAdaptFallback_aioodbc_connection(AsyncAdapt_aioodbc_connection, AsyncAdaptFallback_dbapi_connection):
    __slots__ = ()


class AsyncAdapt_aioodbc_dbapi:
    
    def __init__(self, aioodbc, pyodbc):
        self.aioodbc = aioodbc
        self.pyodbc = pyodbc
        self.paramstyle = pyodbc.paramstyle
        self._init_dbapi_attributes()
        self.Cursor = AsyncAdapt_dbapi_cursor
        self.version = pyodbc.version

    
    def _init_dbapi_attributes(self):
        for name in ('Warning', 'Error', 'InterfaceError', 'DataError', 'DatabaseError', 'OperationalError', 'InterfaceError', 'IntegrityError', 'ProgrammingError', 'InternalError', 'NotSupportedError', 'NUMBER', 'STRING', 'DATETIME', 'BINARY', 'Binary', 'BinaryNull', 'SQL_VARCHAR', 'SQL_WVARCHAR'):
            setattr(self, name, getattr(self.pyodbc, name))
            return None

    
    def connect(self, *arg, **kw):
        async_fallback = kw.pop('async_fallback', False)
        creator_fn = kw.pop('async_creator_fn', self.aioodbc.connect)
    # WARNING: Decompyle incomplete



class aiodbcConnector(PyODBCConnector):
    pass
# WARNING: Decompyle incomplete
