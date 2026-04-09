# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: asyncio.pyc (Python 3.11)

'''generic asyncio-adapted versions of DBAPI connection and cursor'''
from __future__ import annotations
import asyncio
import collections
import sys
from typing import Any
from typing import AsyncIterator
from typing import Deque
from typing import Iterator
from typing import NoReturn
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from engine import AdaptedConnection
from util import EMPTY_DICT
from util.concurrency import await_fallback
from util.concurrency import await_only
from util.concurrency import in_greenlet
from util.typing import Protocol
if TYPE_CHECKING:
    from engine.interfaces import _DBAPICursorDescription
    from engine.interfaces import _DBAPIMultiExecuteParams
    from engine.interfaces import _DBAPISingleExecuteParams
    from engine.interfaces import DBAPIModule
    from util.typing import Self

class AsyncIODBAPIConnection(Protocol):
    '''protocol representing an async adapted version of a
    :pep:`249` database connection.


    '''
    
    async def commit(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def cursor(self = None, *args, **kwargs):
        pass

    
    async def rollback(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __getattr__(self = None, key = None):
        pass

    
    def __setattr__(self = None, key = None, value = None):
        pass



class AsyncIODBAPICursor(Protocol):
    '''protocol representing an async adapted version
    of a :pep:`249` database cursor.


    '''
    
    def __aenter__(self = None):
        pass

    description = (lambda self = None: pass)()
    lastrowid: 'int' = (lambda self = None: pass)()
    
    async def close(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def execute(self = None, operation = None, parameters = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def executemany(self = None, operation = None, parameters = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def fetchone(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def fetchmany(self = None, size = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def fetchall(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def setinputsizes(self = None, sizes = None):
        pass
    # WARNING: Decompyle incomplete

    
    def setoutputsize(self = None, size = None, column = None):
        pass

    
    async def callproc(self = None, procname = None, parameters = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def nextset(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        pass



class AsyncAdapt_dbapi_module:
    if TYPE_CHECKING:
        Error = DBAPIModule.Error
        OperationalError = DBAPIModule.OperationalError
        InterfaceError = DBAPIModule.InterfaceError
        IntegrityError = DBAPIModule.IntegrityError
        
        def __getattr__(self = None, key = None):
            pass

        return None


class AsyncAdapt_dbapi_cursor:
    server_side = False
    __slots__ = ('_adapt_connection', '_connection', 'await_', '_cursor', '_rows', '_soft_closed_memoized')
    _rows: 'Deque[Any]' = True
    
    def __init__(self = None, adapt_connection = None):
        self._adapt_connection = adapt_connection
        self._connection = adapt_connection._connection
        self.await_ = adapt_connection.await_
        cursor = self._make_new_cursor(self._connection)
        self._cursor = self._aenter_cursor(cursor)
        self._soft_closed_memoized = EMPTY_DICT
        if not self.server_side:
            self._rows = collections.deque()
            return None

    
    def _aenter_cursor(self = None, cursor = None):
        return self.await_(cursor.__aenter__())

    
    def _make_new_cursor(self = None, connection = None):
        return connection.cursor()

    description = (lambda self = None: if 'description' in self._soft_closed_memoized:
self._soft_closed_memoized['description']None._cursor.description)()
    rowcount = (lambda self = None: self._cursor.rowcount)()
    arraysize = (lambda self = None: self._cursor.arraysize)()
    arraysize = (lambda self = None, value = None: self._cursor.arraysize = value)()
    lastrowid = (lambda self = None: self._cursor.lastrowid)()
    
    async def _async_soft_close(self = None):
        '''close the cursor but keep the results pending, and memoize the
        description.

        .. versionadded:: 2.0.44

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        self._rows.clear()
    # WARNING: Decompyle incomplete

    
    def execute(self = None, operation = None, parameters = None):
        
        try:
            return self.await_(self._execute_async(operation, parameters))
        except Exception:
            error = None
            self._adapt_connection._handle_exception(error)
            error = None
            del error
            return None
            error = None
            del error


    
    def executemany(self = None, operation = None, seq_of_parameters = None):
        
        try:
            return self.await_(self._executemany_async(operation, seq_of_parameters))
        except Exception:
            error = None
            self._adapt_connection._handle_exception(error)
            error = None
            del error
            return None
            error = None
            del error


    
    async def _execute_async(self = None, operation = None, parameters = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _executemany_async(self = None, operation = None, seq_of_parameters = None):
        pass
    # WARNING: Decompyle incomplete

    
    def nextset(self = None):
        self.await_(self._cursor.nextset())
        if not self._cursor.description or self.server_side:
            self._rows = collections.deque(self.await_(self._cursor.fetchall()))
            return None
        return None

    
    def setinputsizes(self = None, *inputsizes):
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, type_ = None, value = None, traceback = ('type_', 'Any', 'value', 'Any', 'traceback', 'Any', 'return', 'None')):
        self.close()

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def fetchone(self = None):
        if self._rows:
            return self._rows.popleft()

    
    def fetchmany(self = None, size = None):
        pass
    # WARNING: Decompyle incomplete

    
    def fetchall(self = None):
        retval = list(self._rows)
        self._rows.clear()
        return retval



class AsyncAdapt_dbapi_ss_cursor(AsyncAdapt_dbapi_cursor):
    __slots__ = ()
    server_side = True
    
    def close(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def fetchone(self = None):
        return self.await_(self._cursor.fetchone())

    
    def fetchmany(self = None, size = None):
        return self.await_(self._cursor.fetchmany(size = size))

    
    def fetchall(self = None):
        return self.await_(self._cursor.fetchall())

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete



class AsyncAdapt_dbapi_connection(AdaptedConnection):
    _cursor_cls = AsyncAdapt_dbapi_cursor
    _ss_cursor_cls = AsyncAdapt_dbapi_ss_cursor
    await_ = staticmethod(await_only)
    _connection: 'AsyncIODBAPIConnection' = ('dbapi', '_execute_mutex')
    
    def __init__(self = None, dbapi = None, connection = None):
        self.dbapi = dbapi
        self._connection = connection
        self._execute_mutex = asyncio.Lock()

    
    def cursor(self = None, server_side = None):
        if server_side:
            return self._ss_cursor_cls(self)
        return None._cursor_cls(self)

    
    def execute(self = None, operation = None, parameters = None):
        '''lots of DBAPIs seem to provide this, so include it'''
        cursor = self.cursor()
        cursor.execute(operation, parameters)
        return cursor

    
    def _handle_exception(self = None, error = None):
        exc_info = sys.exc_info()
        raise error.with_traceback(exc_info[2])

    
    def rollback(self = None):
        
        try:
            self.await_(self._connection.rollback())
            return None
        except Exception:
            error = None
            self._handle_exception(error)
            error = None
            del error
            return None
            error = None
            del error


    
    def commit(self = None):
        
        try:
            self.await_(self._connection.commit())
            return None
        except Exception:
            error = None
            self._handle_exception(error)
            error = None
            del error
            return None
            error = None
            del error


    
    def close(self = None):
        self.await_(self._connection.close())



class AsyncAdaptFallback_dbapi_connection(AsyncAdapt_dbapi_connection):
    __slots__ = ()
    await_ = staticmethod(await_fallback)


class AsyncAdapt_terminate:
    '''Mixin for a AsyncAdapt_dbapi_connection to add terminate support.'''
    __slots__ = ()
    
    def terminate(self = None):
        if in_greenlet():
            
            try:
                self.await_(asyncio.shield(self._terminate_graceful_close()))
                return None
            except self._terminate_handled_exceptions():
                e = None
                self._terminate_force_close()
                if isinstance(e, asyncio.CancelledError):
                    raise 
                e = None
                del e
                return None
                e = None
                del e
                self._terminate_force_close()
                return None


    
    def _terminate_handled_exceptions(self = None):
        '''Returns the exceptions that should be handled when
        calling _graceful_close.
        '''
        return (asyncio.TimeoutError, asyncio.CancelledError, OSError)

    
    async def _terminate_graceful_close(self = None):
        '''Try to close connection gracefully'''
        pass
    # WARNING: Decompyle incomplete

    
    def _terminate_force_close(self = None):
        '''Terminate the connection'''
        raise NotImplementedError
