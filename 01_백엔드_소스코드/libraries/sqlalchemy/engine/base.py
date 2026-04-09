# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''Defines :class:`_engine.Connection` and :class:`_engine.Engine`.'''
from __future__ import annotations
import contextlib
import sys
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
from interfaces import BindTyping
from interfaces import ConnectionEventsTarget
from interfaces import DBAPICursor
from interfaces import ExceptionContext
from interfaces import ExecuteStyle
from interfaces import ExecutionContext
from interfaces import IsolationLevel
from util import _distill_params_20
from util import _distill_raw_params
from util import TransactionalContext
from  import exc
from  import inspection
from  import log
from  import util
from sql import compiler
from sql import util as sql_util
if typing.TYPE_CHECKING:
    from  import CursorResult
    from  import ScalarResult
    from interfaces import _AnyExecuteParams
    from interfaces import _AnyMultiExecuteParams
    from interfaces import _CoreAnyExecuteParams
    from interfaces import _CoreMultiExecuteParams
    from interfaces import _CoreSingleExecuteParams
    from interfaces import _DBAPIAnyExecuteParams
    from interfaces import _DBAPISingleExecuteParams
    from interfaces import _ExecuteOptions
    from interfaces import CompiledCacheType
    from interfaces import CoreExecuteOptionsParameter
    from interfaces import Dialect
    from interfaces import SchemaTranslateMapType
    from reflection import Inspector
    from url import URL
    from event import dispatcher
    from log import _EchoFlagType
    from pool import _ConnectionFairy
    from pool import Pool
    from pool import PoolProxiedConnection
    from sql import Executable
    from sql._typing import _InfoType
    from sql.compiler import Compiled
    from sql.ddl import ExecutableDDLElement
    from sql.ddl import InvokeDDLBase
    from sql.functions import FunctionElement
    from sql.schema import DefaultGenerator
    from sql.schema import HasSchemaAttr
    from sql.schema import SchemaVisitable
    from sql.selectable import TypedReturnsRows
_T = TypeVar('_T', bound = Any)
_EMPTY_EXECUTION_OPTS: '_ExecuteOptions' = util.EMPTY_DICT
NO_OPTIONS: 'Mapping[str, Any]' = util.EMPTY_DICT

def Connection():
    '''Connection'''
    dispatch: 'dispatcher[ConnectionEventsTarget]' = 'Provides high-level functionality for a wrapped DB-API connection.\n\n    The :class:`_engine.Connection` object is procured by calling the\n    :meth:`_engine.Engine.connect` method of the :class:`_engine.Engine`\n    object, and provides services for execution of SQL statements as well\n    as transaction control.\n\n    The Connection object is **not** thread-safe. While a Connection can be\n    shared among threads using properly synchronized access, it is still\n    possible that the underlying DBAPI connection may not support shared\n    access between threads. Check the DBAPI documentation for details.\n\n    The Connection object represents a single DBAPI connection checked out\n    from the connection pool. In this state, the connection pool has no\n    affect upon the connection, including its expiration or timeout state.\n    For the connection pool to properly manage connections, connections\n    should be returned to the connection pool (i.e. ``connection.close()``)\n    whenever the connection is not in use.\n\n    .. index::\n      single: thread safety; Connection\n\n    '
    _sqla_logger_namespace = 'sqlalchemy.engine.Connection'
    _trans_context_manager: 'Optional[TransactionalContext]' = None
    _nested_transaction: 'Optional[NestedTransaction]' = False
    
    def __init__(self, engine = None, connection = None, _has_events = None, _allow_revalidate = (None, None, True, True), _allow_autobegin = ('engine', 'Engine', 'connection', 'Optional[PoolProxiedConnection]', '_has_events', 'Optional[bool]', '_allow_revalidate', 'bool', '_allow_autobegin', 'bool')):
        '''Construct a new Connection.'''
        self.engine = engine
        self.dialect = engine.dialect
        dialect = engine.dialect
    # WARNING: Decompyle incomplete

    _message_formatter: 'Any' = None
    
    def _log_info(self = None, message = None, *arg, **kw):
        fmt = self._message_formatter
        if fmt:
            message = fmt(message)
        if log.STACKLEVEL:
            kw['stacklevel'] = 1 + log.STACKLEVEL_OFFSET
    # WARNING: Decompyle incomplete

    
    def _log_debug(self = None, message = None, *arg, **kw):
        fmt = self._message_formatter
        if fmt:
            message = fmt(message)
        if log.STACKLEVEL:
            kw['stacklevel'] = 1 + log.STACKLEVEL_OFFSET
    # WARNING: Decompyle incomplete

    _schema_translate_map = (lambda self = None: schema_translate_map = self._execution_options.get('schema_translate_map', None)schema_translate_map)()
    
    def schema_for_object(self = None, obj = None):
        '''Return the schema name for the given schema item taking into
        account current schema translate map.

        '''
        name = obj.schema
        schema_translate_map = self._execution_options.get('schema_translate_map', None)
        if schema_translate_map and name in schema_translate_map and obj._use_schema_map:
            return schema_translate_map[name]

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, type_ = None, value = None, traceback = ('type_', 'Any', 'value', 'Any', 'traceback', 'Any', 'return', 'None')):
        self.close()

    execution_options = (lambda self = None, *, compiled_cache: pass)()
    execution_options = (lambda self = None: pass)()
    
    def execution_options(self = None, **opt):
        '''Set non-SQL options for the connection which take effect
        during execution.

        This method modifies this :class:`_engine.Connection` **in-place**;
        the return value is the same :class:`_engine.Connection` object
        upon which the method is called.   Note that this is in contrast
        to the behavior of the ``execution_options`` methods on other
        objects such as :meth:`_engine.Engine.execution_options` and
        :meth:`_sql.Executable.execution_options`.  The rationale is that many
        such execution options necessarily modify the state of the base
        DBAPI connection in any case so there is no feasible means of
        keeping the effect of such an option localized to a "sub" connection.

        .. versionchanged:: 2.0  The :meth:`_engine.Connection.execution_options`
           method, in contrast to other objects with this method, modifies
           the connection in-place without creating copy of it.

        As discussed elsewhere, the :meth:`_engine.Connection.execution_options`
        method accepts any arbitrary parameters including user defined names.
        All parameters given are consumable in a number of ways including
        by using the :meth:`_engine.Connection.get_execution_options` method.
        See the examples at :meth:`_sql.Executable.execution_options`
        and :meth:`_engine.Engine.execution_options`.

        The keywords that are currently recognized by SQLAlchemy itself
        include all those listed under :meth:`.Executable.execution_options`,
        as well as others that are specific to :class:`_engine.Connection`.

        :param compiled_cache: Available on: :class:`_engine.Connection`,
          :class:`_engine.Engine`.

          A dictionary where :class:`.Compiled` objects
          will be cached when the :class:`_engine.Connection`
          compiles a clause
          expression into a :class:`.Compiled` object.  This dictionary will
          supersede the statement cache that may be configured on the
          :class:`_engine.Engine` itself.   If set to None, caching
          is disabled, even if the engine has a configured cache size.

          Note that the ORM makes use of its own "compiled" caches for
          some operations, including flush operations.  The caching
          used by the ORM internally supersedes a cache dictionary
          specified here.

        :param logging_token: Available on: :class:`_engine.Connection`,
          :class:`_engine.Engine`, :class:`_sql.Executable`.

          Adds the specified string token surrounded by brackets in log
          messages logged by the connection, i.e. the logging that\'s enabled
          either via the :paramref:`_sa.create_engine.echo` flag or via the
          ``logging.getLogger("sqlalchemy.engine")`` logger. This allows a
          per-connection or per-sub-engine token to be available which is
          useful for debugging concurrent connection scenarios.

          .. versionadded:: 1.4.0b2

          .. seealso::

            :ref:`dbengine_logging_tokens` - usage example

            :paramref:`_sa.create_engine.logging_name` - adds a name to the
            name used by the Python logger object itself.

        :param isolation_level: Available on: :class:`_engine.Connection`,
          :class:`_engine.Engine`.

          Set the transaction isolation level for the lifespan of this
          :class:`_engine.Connection` object.
          Valid values include those string
          values accepted by the :paramref:`_sa.create_engine.isolation_level`
          parameter passed to :func:`_sa.create_engine`.  These levels are
          semi-database specific; see individual dialect documentation for
          valid levels.

          The isolation level option applies the isolation level by emitting
          statements on the DBAPI connection, and **necessarily affects the
          original Connection object overall**. The isolation level will remain
          at the given setting until explicitly changed, or when the DBAPI
          connection itself is :term:`released` to the connection pool, i.e. the
          :meth:`_engine.Connection.close` method is called, at which time an
          event handler will emit additional statements on the DBAPI connection
          in order to revert the isolation level change.

          .. note:: The ``isolation_level`` execution option may only be
             established before the :meth:`_engine.Connection.begin` method is
             called, as well as before any SQL statements are emitted which
             would otherwise trigger "autobegin", or directly after a call to
             :meth:`_engine.Connection.commit` or
             :meth:`_engine.Connection.rollback`. A database cannot change the
             isolation level on a transaction in progress.

          .. note:: The ``isolation_level`` execution option is implicitly
             reset if the :class:`_engine.Connection` is invalidated, e.g. via
             the :meth:`_engine.Connection.invalidate` method, or if a
             disconnection error occurs. The new connection produced after the
             invalidation will **not** have the selected isolation level
             re-applied to it automatically.

          .. seealso::

                :ref:`dbapi_autocommit`

                :meth:`_engine.Connection.get_isolation_level`
                - view current actual level

        :param no_parameters: Available on: :class:`_engine.Connection`,
          :class:`_sql.Executable`.

          When ``True``, if the final parameter
          list or dictionary is totally empty, will invoke the
          statement on the cursor as ``cursor.execute(statement)``,
          not passing the parameter collection at all.
          Some DBAPIs such as psycopg2 and mysql-python consider
          percent signs as significant only when parameters are
          present; this option allows code to generate SQL
          containing percent signs (and possibly other characters)
          that is neutral regarding whether it\'s executed by the DBAPI
          or piped into a script that\'s later invoked by
          command line tools.

        :param stream_results: Available on: :class:`_engine.Connection`,
          :class:`_sql.Executable`.

          Indicate to the dialect that results should be "streamed" and not
          pre-buffered, if possible.  For backends such as PostgreSQL, MySQL
          and MariaDB, this indicates the use of a "server side cursor" as
          opposed to a client side cursor.  Other backends such as that of
          Oracle Database may already use server side cursors by default.

          The usage of
          :paramref:`_engine.Connection.execution_options.stream_results` is
          usually combined with setting a fixed number of rows to to be fetched
          in batches, to allow for efficient iteration of database rows while
          at the same time not loading all result rows into memory at once;
          this can be configured on a :class:`_engine.Result` object using the
          :meth:`_engine.Result.yield_per` method, after execution has
          returned a new :class:`_engine.Result`.   If
          :meth:`_engine.Result.yield_per` is not used,
          the :paramref:`_engine.Connection.execution_options.stream_results`
          mode of operation will instead use a dynamically sized buffer
          which buffers sets of rows at a time, growing on each batch
          based on a fixed growth size up until a limit which may
          be configured using the
          :paramref:`_engine.Connection.execution_options.max_row_buffer`
          parameter.

          When using the ORM to fetch ORM mapped objects from a result,
          :meth:`_engine.Result.yield_per` should always be used with
          :paramref:`_engine.Connection.execution_options.stream_results`,
          so that the ORM does not fetch all rows into new ORM objects at once.

          For typical use, the
          :paramref:`_engine.Connection.execution_options.yield_per` execution
          option should be preferred, which sets up both
          :paramref:`_engine.Connection.execution_options.stream_results` and
          :meth:`_engine.Result.yield_per` at once. This option is supported
          both at a core level by :class:`_engine.Connection` as well as by the
          ORM :class:`_engine.Session`; the latter is described at
          :ref:`orm_queryguide_yield_per`.

          .. seealso::

            :ref:`engine_stream_results` - background on
            :paramref:`_engine.Connection.execution_options.stream_results`

            :paramref:`_engine.Connection.execution_options.max_row_buffer`

            :paramref:`_engine.Connection.execution_options.yield_per`

            :ref:`orm_queryguide_yield_per` - in the :ref:`queryguide_toplevel`
            describing the ORM version of ``yield_per``

        :param max_row_buffer: Available on: :class:`_engine.Connection`,
          :class:`_sql.Executable`.  Sets a maximum
          buffer size to use when the
          :paramref:`_engine.Connection.execution_options.stream_results`
          execution option is used on a backend that supports server side
          cursors.  The default value if not specified is 1000.

          .. seealso::

            :paramref:`_engine.Connection.execution_options.stream_results`

            :ref:`engine_stream_results`


        :param yield_per: Available on: :class:`_engine.Connection`,
          :class:`_sql.Executable`.  Integer value applied which will
          set the :paramref:`_engine.Connection.execution_options.stream_results`
          execution option and invoke :meth:`_engine.Result.yield_per`
          automatically at once.  Allows equivalent functionality as
          is present when using this parameter with the ORM.

          .. versionadded:: 1.4.40

          .. seealso::

            :ref:`engine_stream_results` - background and examples
            on using server side cursors with Core.

            :ref:`orm_queryguide_yield_per` - in the :ref:`queryguide_toplevel`
            describing the ORM version of ``yield_per``

        :param insertmanyvalues_page_size: Available on: :class:`_engine.Connection`,
            :class:`_engine.Engine`. Number of rows to format into an
            INSERT statement when the statement uses "insertmanyvalues" mode,
            which is a paged form of bulk insert that is used for many backends
            when using :term:`executemany` execution typically in conjunction
            with RETURNING. Defaults to 1000. May also be modified on a
            per-engine basis using the
            :paramref:`_sa.create_engine.insertmanyvalues_page_size` parameter.

            .. versionadded:: 2.0

            .. seealso::

                :ref:`engine_insertmanyvalues`

        :param schema_translate_map: Available on: :class:`_engine.Connection`,
          :class:`_engine.Engine`, :class:`_sql.Executable`.

          A dictionary mapping schema names to schema names, that will be
          applied to the :paramref:`_schema.Table.schema` element of each
          :class:`_schema.Table`
          encountered when SQL or DDL expression elements
          are compiled into strings; the resulting schema name will be
          converted based on presence in the map of the original name.

          .. seealso::

            :ref:`schema_translating`

        :param preserve_rowcount: Boolean; when True, the ``cursor.rowcount``
          attribute will be unconditionally memoized within the result and
          made available via the :attr:`.CursorResult.rowcount` attribute.
          Normally, this attribute is only preserved for UPDATE and DELETE
          statements.  Using this option, the DBAPIs rowcount value can
          be accessed for other kinds of statements such as INSERT and SELECT,
          to the degree that the DBAPI supports these statements.  See
          :attr:`.CursorResult.rowcount` for notes regarding the behavior
          of this attribute.

          .. versionadded:: 2.0.28

        .. seealso::

            :meth:`_engine.Engine.execution_options`

            :meth:`.Executable.execution_options`

            :meth:`_engine.Connection.get_execution_options`

            :ref:`orm_queryguide_execution_options` - documentation on all
            ORM-specific execution options

        '''
        if self._has_events or self.engine._has_events:
            self.dispatch.set_connection_execution_options(self, opt)
        self._execution_options = self._execution_options.union(opt)
        self.dialect.set_connection_execution_options(self, opt)
        return self

    
    def get_execution_options(self = None):
        '''Get the non-SQL options which will take effect during execution.

        .. versionadded:: 1.3

        .. seealso::

            :meth:`_engine.Connection.execution_options`
        '''
        return self._execution_options

    _still_open_and_dbapi_connection_is_valid = (lambda self = None:
