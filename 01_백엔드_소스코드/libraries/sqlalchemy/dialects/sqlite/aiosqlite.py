# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: aiosqlite.pyc (Python 3.11)

'''

.. dialect:: sqlite+aiosqlite
    :name: aiosqlite
    :dbapi: aiosqlite
    :connectstring: sqlite+aiosqlite:///file_path
    :url: https://pypi.org/project/aiosqlite/

The aiosqlite dialect provides support for the SQLAlchemy asyncio interface
running on top of pysqlite.

aiosqlite is a wrapper around pysqlite that uses a background thread for
each connection.   It does not actually use non-blocking IO, as SQLite
databases are not socket-based.  However it does provide a working asyncio
interface that\'s useful for testing and prototyping purposes.

Using a special asyncio mediation layer, the aiosqlite dialect is usable
as the backend for the :ref:`SQLAlchemy asyncio <asyncio_toplevel>`
extension package.

This dialect should normally be used only with the
:func:`_asyncio.create_async_engine` engine creation function::

    from sqlalchemy.ext.asyncio import create_async_engine

    engine = create_async_engine("sqlite+aiosqlite:///filename")

The URL passes through all arguments to the ``pysqlite`` driver, so all
connection arguments are the same as they are for that of :ref:`pysqlite`.

.. _aiosqlite_udfs:

User-Defined Functions
----------------------

aiosqlite extends pysqlite to support async, so we can create our own user-defined functions (UDFs)
in Python and use them directly in SQLite queries as described here: :ref:`pysqlite_udfs`.

.. _aiosqlite_serializable:

Serializable isolation / Savepoints / Transactional DDL (asyncio version)
-------------------------------------------------------------------------

A newly revised version of this important section is now available
at the top level of the SQLAlchemy SQLite documentation, in the section
:ref:`sqlite_transactions`.


.. _aiosqlite_pooling:

Pooling Behavior
----------------

The SQLAlchemy ``aiosqlite`` DBAPI establishes the connection pool differently
based on the kind of SQLite database that\'s requested:

* When a ``:memory:`` SQLite database is specified, the dialect by default
  will use :class:`.StaticPool`. This pool maintains a single
  connection, so that all access to the engine
  use the same ``:memory:`` database.
* When a file-based database is specified, the dialect will use
  :class:`.AsyncAdaptedQueuePool` as the source of connections.

  .. versionchanged:: 2.0.38

    SQLite file database engines now use :class:`.AsyncAdaptedQueuePool` by default.
    Previously, :class:`.NullPool` were used.  The :class:`.NullPool` class
    may be used by specifying it via the
    :paramref:`_sa.create_engine.poolclass` parameter.

'''
from __future__ import annotations
import asyncio
from collections import deque
from functools import partial
from types import ModuleType
from typing import Any
from typing import cast
from typing import Deque
from typing import Iterator
from typing import NoReturn
from typing import Optional
from typing import Sequence
from typing import TYPE_CHECKING
from typing import Union
from base import SQLiteExecutionContext
from pysqlite import SQLiteDialect_pysqlite
from  import pool
from  import util
from connectors.asyncio import AsyncAdapt_dbapi_module
from engine import AdaptedConnection
from util.concurrency import await_fallback
from util.concurrency import await_only
if TYPE_CHECKING:
    from connectors.asyncio import AsyncIODBAPIConnection
    from connectors.asyncio import AsyncIODBAPICursor
    from engine.interfaces import _DBAPICursorDescription
    from engine.interfaces import _DBAPIMultiExecuteParams
    from engine.interfaces import _DBAPISingleExecuteParams
    from engine.interfaces import DBAPIConnection
    from engine.interfaces import DBAPICursor
    from engine.interfaces import DBAPIModule
    from engine.url import URL
    from pool.base import PoolProxiedConnection

class AsyncAdapt_aiosqlite_cursor:
    __slots__ = ('_adapt_connection', '_connection', 'description', 'await_', '_rows', 'arraysize', 'rowcount', 'lastrowid')
    server_side = False
    
    def __init__(self = None, adapt_connection = None):
        self._adapt_connection = adapt_connection
        self._connection = adapt_connection._connection
        self.await_ = adapt_connection.await_
        self.arraysize = 1
        self.rowcount = -1
        self.description = None
        self._rows = deque()

    
    async def _async_soft_close(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        self._rows.clear()

    
    def execute(self = None, operation = None, parameters = None):
        pass
    # WARNING: Decompyle incomplete

    
    def executemany(self = None, operation = None, seq_of_parameters = None):
        
        try:
            _cursor = self.await_(self._connection.cursor())
            self.await_(_cursor.executemany(operation, seq_of_parameters))
            self.description = None
            self.lastrowid = _cursor.lastrowid
            self.rowcount = _cursor.rowcount
            self.await_(_cursor.close())
            return None
        except Exception:
            error = None
            self._adapt_connection._handle_exception(error)
            error = None
            del error
            return None
            error = None
            del error


    
    def setinputsizes(self = None, *inputsizes):
        pass

    
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



class AsyncAdapt_aiosqlite_ss_cursor(AsyncAdapt_aiosqlite_cursor):
    pass
# WARNING: Decompyle incomplete


class AsyncAdapt_aiosqlite_connection(AdaptedConnection):
    await_ = staticmethod(await_only)
    __slots__ = ('dbapi',)
    
    def __init__(self = None, dbapi = None, connection = None):
        self.dbapi = dbapi
        self._connection = connection

    isolation_level = (lambda self = None: cast(str, self._connection.isolation_level))()
    isolation_level = (lambda self = None, value = None: 
def set_iso(connection = None, value = None):
connection.isolation_level = valuefunction = partial(set_iso, self._connection._conn, value)future = asyncio.get_event_loop().create_future()self._connection._tx.put_nowait((future, function))try:
self.await_(future)Noneexcept Exception:
error = Noneself._handle_exception(error)error = Nonedel errorNoneerror = Nonedel error)()
    
    def create_function(self = None, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def cursor(self = None, server_side = None):
        if server_side:
            return AsyncAdapt_aiosqlite_ss_cursor(self)
        return None(self)

    
    def execute(self = None, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
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
        
        try:
            self.await_(self._connection.close())
            return None
        except ValueError:
            return None
            except Exception:
                error = None
                self._handle_exception(error)
                error = None
                del error
                return None
                error = None
                del error


    
    def _handle_exception(self = None, error = None):
        if isinstance(error, ValueError) and error.args[0] == 'no active connection':
            raise self.dbapi.sqlite.OperationalError('no active connection'), error
        raise error



class AsyncAdaptFallback_aiosqlite_connection(AsyncAdapt_aiosqlite_connection):
    __slots__ = ()
    await_ = staticmethod(await_fallback)


class AsyncAdapt_aiosqlite_dbapi(AsyncAdapt_dbapi_module):
    
    def __init__(self = None, aiosqlite = None, sqlite = None):
        self.aiosqlite = aiosqlite
        self.sqlite = sqlite
        self.paramstyle = 'qmark'
        self._init_dbapi_attributes()

    
    def _init_dbapi_attributes(self = None):
        for name in ('DatabaseError', 'Error', 'IntegrityError', 'NotSupportedError', 'OperationalError', 'ProgrammingError', 'sqlite_version', 'sqlite_version_info'):
            setattr(self, name, getattr(self.aiosqlite, name))
            for name in ('PARSE_COLNAMES', 'PARSE_DECLTYPES'):
                setattr(self, name, getattr(self.sqlite, name))
                for name in ('Binary',):
                    setattr(self, name, getattr(self.sqlite, name))
                    return None

    
    def connect(self = None, *arg, **kw):
        async_fallback = kw.pop('async_fallback', False)
        creator_fn = kw.pop('async_creator_fn', None)
    # WARNING: Decompyle incomplete



class SQLiteExecutionContext_aiosqlite(SQLiteExecutionContext):
    
    def create_server_side_cursor(self = None):
        return self._dbapi_connection.cursor(server_side = True)



class SQLiteDialect_aiosqlite(SQLiteDialect_pysqlite):
    pass
# WARNING: Decompyle incomplete

dialect = SQLiteDialect_aiosqlite
