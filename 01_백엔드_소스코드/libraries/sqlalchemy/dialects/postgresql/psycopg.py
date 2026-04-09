# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: psycopg.pyc (Python 3.11)

'''
.. dialect:: postgresql+psycopg
    :name: psycopg (a.k.a. psycopg 3)
    :dbapi: psycopg
    :connectstring: postgresql+psycopg://user:password@host:port/dbname[?key=value&key=value...]
    :url: https://pypi.org/project/psycopg/

``psycopg`` is the package and module name for version 3 of the ``psycopg``
database driver, formerly known as ``psycopg2``.  This driver is different
enough from its ``psycopg2`` predecessor that SQLAlchemy supports it
via a totally separate dialect; support for ``psycopg2`` is expected to remain
for as long as that package continues to function for modern Python versions,
and also remains the default dialect for the ``postgresql://`` dialect
series.

The SQLAlchemy ``psycopg`` dialect provides both a sync and an async
implementation under the same dialect name. The proper version is
selected depending on how the engine is created:

* calling :func:`_sa.create_engine` with ``postgresql+psycopg://...`` will
  automatically select the sync version, e.g.::

    from sqlalchemy import create_engine

    sync_engine = create_engine(
        "postgresql+psycopg://scott:tiger@localhost/test"
    )

* calling :func:`_asyncio.create_async_engine` with
  ``postgresql+psycopg://...`` will automatically select the async version,
  e.g.::

    from sqlalchemy.ext.asyncio import create_async_engine

    asyncio_engine = create_async_engine(
        "postgresql+psycopg://scott:tiger@localhost/test"
    )

The asyncio version of the dialect may also be specified explicitly using the
``psycopg_async`` suffix, as::

    from sqlalchemy.ext.asyncio import create_async_engine

    asyncio_engine = create_async_engine(
        "postgresql+psycopg_async://scott:tiger@localhost/test"
    )

.. seealso::

    :ref:`postgresql_psycopg2` - The SQLAlchemy ``psycopg``
    dialect shares most of its behavior with the ``psycopg2`` dialect.
    Further documentation is available there.

Using a different Cursor class
------------------------------

One of the differences between ``psycopg`` and the older ``psycopg2``
is how bound parameters are handled: ``psycopg2`` would bind them
client side, while ``psycopg`` by default will bind them server side.

It\'s possible to configure ``psycopg`` to do client side binding by
specifying the ``cursor_factory`` to be ``ClientCursor`` when creating
the engine::

    from psycopg import ClientCursor

    client_side_engine = create_engine(
        "postgresql+psycopg://...",
        connect_args={"cursor_factory": ClientCursor},
    )

Similarly when using an async engine the ``AsyncClientCursor`` can be
specified::

    from psycopg import AsyncClientCursor

    client_side_engine = create_async_engine(
        "postgresql+psycopg://...",
        connect_args={"cursor_factory": AsyncClientCursor},
    )

.. seealso::

    `Client-side-binding cursors <https://www.psycopg.org/psycopg3/docs/advanced/cursors.html#client-side-binding-cursors>`_

'''
from __future__ import annotations
from collections import deque
import logging
import re
from typing import cast
from typing import TYPE_CHECKING
from  import ranges
from _psycopg_common import _PGDialect_common_psycopg
from _psycopg_common import _PGExecutionContext_common_psycopg
from base import INTERVAL
from base import PGCompiler
from base import PGIdentifierPreparer
from base import REGCONFIG
from json import JSON
from json import JSONB
from json import JSONPathType
from types import CITEXT
from  import pool
from  import util
from engine import AdaptedConnection
from sql import sqltypes
from util.concurrency import await_fallback
from util.concurrency import await_only
if TYPE_CHECKING:
    from typing import Iterable
    from psycopg import AsyncConnection
logger = logging.getLogger('sqlalchemy.dialects.postgresql')

class _PGString(sqltypes.String):
    render_bind_cast = True


class _PGREGCONFIG(REGCONFIG):
    render_bind_cast = True


class _PGJSON(JSON):
    
    def bind_processor(self, dialect):
        return self._make_bind_processor(None, dialect._psycopg_Json)

    
    def result_processor(self, dialect, coltype):
        pass



class _PGJSONB(JSONB):
    
    def bind_processor(self, dialect):
        return self._make_bind_processor(None, dialect._psycopg_Jsonb)

    
    def result_processor(self, dialect, coltype):
        pass



class _PGJSONIntIndexType(sqltypes.JSON.JSONIntIndexType):
    __visit_name__ = 'json_int_index'
    render_bind_cast = True


class _PGJSONStrIndexType(sqltypes.JSON.JSONStrIndexType):
    __visit_name__ = 'json_str_index'
    render_bind_cast = True


class _PGJSONPathType(JSONPathType):
    pass


class _PGInterval(INTERVAL):
    render_bind_cast = True


class _PGTimeStamp(sqltypes.DateTime):
    render_bind_cast = True


class _PGDate(sqltypes.Date):
    render_bind_cast = True


class _PGTime(sqltypes.Time):
    render_bind_cast = True


class _PGInteger(sqltypes.Integer):
    render_bind_cast = True


class _PGSmallInteger(sqltypes.SmallInteger):
    render_bind_cast = True


class _PGNullType(sqltypes.NullType):
    render_bind_cast = True


class _PGBigInteger(sqltypes.BigInteger):
    render_bind_cast = True


class _PGBoolean(sqltypes.Boolean):
    render_bind_cast = True


class _PsycopgRange(ranges.AbstractSingleRangeImpl):
    
    def bind_processor(self, dialect):
        pass
    # WARNING: Decompyle incomplete

    
    def result_processor(self, dialect, coltype):
        
        def to_range(value):
            pass
        # WARNING: Decompyle incomplete

        return to_range



class _PsycopgMultiRange(ranges.AbstractMultiRangeImpl):
    
    def bind_processor(self, dialect):
        pass
    # WARNING: Decompyle incomplete

    
    def result_processor(self, dialect, coltype):
        
        def to_range(value):
            pass
        # WARNING: Decompyle incomplete

        return to_range



class PGExecutionContext_psycopg(_PGExecutionContext_common_psycopg):
    pass


class PGCompiler_psycopg(PGCompiler):
    pass


class PGIdentifierPreparer_psycopg(PGIdentifierPreparer):
    pass


def _log_notices(diagnostic):
    logger.info('%s: %s', diagnostic.severity, diagnostic.message_primary)


class PGDialect_psycopg(_PGDialect_common_psycopg):
    pass
# WARNING: Decompyle incomplete


class AsyncAdapt_psycopg_cursor:
    __slots__ = ('_cursor', 'await_', '_rows')
    _psycopg_ExecStatus = None
    
    def __init__(self = None, cursor = None, await_ = None):
        self._cursor = cursor
        self.await_ = await_
        self._rows = deque()

    
    def __getattr__(self, name):
        return getattr(self._cursor, name)

    arraysize = (lambda self: self._cursor.arraysize)()
    arraysize = (lambda self, value: self._cursor.arraysize = value)()
    
    async def _async_soft_close(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self):
        self._rows.clear()
        self._cursor._close()

    
    def execute(self, query, params = (None,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def executemany(self, query, params_seq):
        return self.await_(self._cursor.executemany(query, params_seq))

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def fetchone(self):
        if self._rows:
            return self._rows.popleft()

    
    def fetchmany(self, size = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def fetchall(self):
        retval = list(self._rows)
        self._rows.clear()
        return retval



class AsyncAdapt_psycopg_ss_cursor(AsyncAdapt_psycopg_cursor):
    
    def execute(self, query, params = (None,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self):
        self.await_(self._cursor.close())

    
    def fetchone(self):
        return self.await_(self._cursor.fetchone())

    
    def fetchmany(self, size = (0,)):
        return self.await_(self._cursor.fetchmany(size))

    
    def fetchall(self):
        return self.await_(self._cursor.fetchall())

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete



class AsyncAdapt_psycopg_connection(AdaptedConnection):
    _connection: 'AsyncConnection' = 'AsyncAdapt_psycopg_connection'
    __slots__ = ()
    await_ = staticmethod(await_only)
    
    def __init__(self = None, connection = None):
        self._connection = connection

    
    def __getattr__(self, name):
        return getattr(self._connection, name)

    
    def execute(self, query, params = (None,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def cursor(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def commit(self):
        self.await_(self._connection.commit())

    
    def rollback(self):
        self.await_(self._connection.rollback())

    
    def close(self):
        self.await_(self._connection.close())

    autocommit = (lambda self: self._connection.autocommit)()
    autocommit = (lambda self, value: self.set_autocommit(value))()
    
    def set_autocommit(self, value):
        self.await_(self._connection.set_autocommit(value))

    
    def set_isolation_level(self, value):
        self.await_(self._connection.set_isolation_level(value))

    
    def set_read_only(self, value):
        self.await_(self._connection.set_read_only(value))

    
    def set_deferrable(self, value):
        self.await_(self._connection.set_deferrable(value))



class AsyncAdaptFallback_psycopg_connection(AsyncAdapt_psycopg_connection):
    __slots__ = ()
    await_ = staticmethod(await_fallback)


class PsycopgAdaptDBAPI:
    
    def __init__(self = None, psycopg = None):
        self.psycopg = psycopg
        for k, v in self.psycopg.__dict__.items():
            if k != 'connect':
                self.__dict__[k] = v
            return None

    
    def connect(self, *arg, **kw):
        async_fallback = kw.pop('async_fallback', False)
        creator_fn = kw.pop('async_creator_fn', self.psycopg.AsyncConnection.connect)
    # WARNING: Decompyle incomplete



class PGDialectAsync_psycopg(PGDialect_psycopg):
    is_async = True
    supports_statement_cache = True
    import_dbapi = (lambda cls: import psycopgExecStatus = ExecStatusimport psycopg.pqAsyncAdapt_psycopg_cursor._psycopg_ExecStatus = ExecStatusPsycopgAdaptDBAPI(psycopg))()
    get_pool_class = (lambda cls, url: async_fallback = url.query.get('async_fallback', False)if util.asbool(async_fallback):
pool.FallbackAsyncAdaptedQueuePoolNone.AsyncAdaptedQueuePool)()
    
    def _type_info_fetch(self, connection, name):
        TypeInfo = TypeInfo
        import psycopg.types
        adapted = connection.connection
        return adapted.await_(TypeInfo.fetch(adapted.driver_connection, name))

    
    def _do_isolation_level(self, connection, autocommit, isolation_level):
        connection.set_autocommit(autocommit)
        connection.set_isolation_level(isolation_level)

    
    def _do_autocommit(self, connection, value):
        connection.set_autocommit(value)

    
    def set_readonly(self, connection, value):
        connection.set_read_only(value)

    
    def set_deferrable(self, connection, value):
        connection.set_deferrable(value)

    
    def get_driver_connection(self, connection):
        return connection._connection


dialect = PGDialect_psycopg
dialect_async = PGDialectAsync_psycopg
