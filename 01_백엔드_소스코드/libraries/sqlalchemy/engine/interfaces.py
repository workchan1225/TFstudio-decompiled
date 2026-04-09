# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: interfaces.pyc (Python 3.11)

'''Define core interfaces used by the engine system.'''
from __future__ import annotations
from enum import Enum
from typing import Any
from typing import Awaitable
from typing import Callable
from typing import ClassVar
from typing import Collection
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import MutableMapping
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import util
from event import EventTarget
from pool import Pool
from pool import PoolProxiedConnection
from sql.compiler import Compiled
from sql.compiler import Compiled
from sql.compiler import TypeCompiler
from sql.compiler import TypeCompiler
from util import immutabledict
from util.concurrency import await_only
from util.typing import Literal
from util.typing import NotRequired
from util.typing import Protocol
from util.typing import TypedDict
if TYPE_CHECKING:
    from base import Connection
    from base import Engine
    from cursor import CursorResult
    from url import URL
    from connectors.asyncio import AsyncIODBAPIConnection
    from event import _ListenerFnType
    from event import dispatcher
    from exc import StatementError
    from sql import Executable
    from sql.compiler import _InsertManyValuesBatch
    from sql.compiler import DDLCompiler
    from sql.compiler import IdentifierPreparer
    from sql.compiler import InsertmanyvaluesSentinelOpts
    from sql.compiler import Linting
    from sql.compiler import SQLCompiler
    from sql.elements import BindParameter
    from sql.elements import ClauseElement
    from sql.schema import Column
    from sql.schema import DefaultGenerator
    from sql.schema import SchemaItem
    from sql.schema import Sequence as Sequence_SchemaItem
    from sql.sqltypes import Integer
    from sql.type_api import _TypeMemoDict
    from sql.type_api import TypeEngine
    from util.langhelpers import generic_fn_descriptor
ConnectArgsType = Tuple[(Sequence[str], MutableMapping[(str, Any)])]
_T = TypeVar('_T', bound = 'Any')

class CacheStats(Enum):
    CACHE_HIT = 0
    CACHE_MISS = 1
    CACHING_DISABLED = 2
    NO_CACHE_KEY = 3
    NO_DIALECT_SUPPORT = 4


class ExecuteStyle(Enum):
    '''indicates the :term:`DBAPI` cursor method that will be used to invoke
    a statement.'''
    EXECUTE = 0
    EXECUTEMANY = 1
    INSERTMANYVALUES = 2


class DBAPIModule(Protocol):
    
    class Error(Exception):
        
        def __getattr__(self = None, key = None):
            pass


    
    class OperationalError(Error):
        pass

    
    class InterfaceError(Error):
        pass

    
    class IntegrityError(Error):
        pass

    
    def __getattr__(self = None, key = None):
        pass



class DBAPIConnection(Protocol):
    '''protocol representing a :pep:`249` database connection.

    .. versionadded:: 2.0

    .. seealso::

        `Connection Objects <https://www.python.org/dev/peps/pep-0249/#connection-objects>`_
        - in :pep:`249`

    '''
    
    def close(self = None):
        pass

    
    def commit(self = None):
        pass

    
    def cursor(self = None, *args, **kwargs):
        pass

    
    def rollback(self = None):
        pass

    
    def __getattr__(self = None, key = None):
        pass

    
    def __setattr__(self = None, key = None, value = None):
        pass



class DBAPIType(Protocol):
    '''protocol representing a :pep:`249` database type.

    .. versionadded:: 2.0

    .. seealso::

        `Type Objects <https://www.python.org/dev/peps/pep-0249/#type-objects>`_
        - in :pep:`249`

    '''
    pass


class DBAPICursor(Protocol):
    '''protocol representing a :pep:`249` database cursor.

    .. versionadded:: 2.0

    .. seealso::

        `Cursor Objects <https://www.python.org/dev/peps/pep-0249/#cursor-objects>`_
        - in :pep:`249`

    '''
    description = (lambda self = None: pass)()
    lastrowid: 'int' = (lambda self = None: pass)()
    
    def close(self = None):
        pass

    
    def execute(self = None, operation = None, parameters = None):
        pass

    
    def executemany(self = None, operation = None, parameters = None):
        pass

    
    def fetchone(self = None):
        pass

    
    def fetchmany(self = None, size = None):
        pass

    
    def fetchall(self = None):
        pass

    
    def setinputsizes(self = None, sizes = None):
        pass

    
    def setoutputsize(self = None, size = None, column = None):
        pass

    
    def callproc(self = None, procname = None, parameters = None):
        pass

    
    def nextset(self = None):
        pass

    
    def __getattr__(self = None, key = None):
        pass


_CoreSingleExecuteParams = Mapping[(str, Any)]
_MutableCoreSingleExecuteParams = MutableMapping[(str, Any)]
_CoreMultiExecuteParams = Sequence[_CoreSingleExecuteParams]
_CoreAnyExecuteParams = Union[(_CoreMultiExecuteParams, _CoreSingleExecuteParams)]
_DBAPISingleExecuteParams = Union[(Sequence[Any], _CoreSingleExecuteParams)]
_DBAPIMultiExecuteParams = Union[(Sequence[Sequence[Any]], _CoreMultiExecuteParams)]
_DBAPIAnyExecuteParams = Union[(_DBAPIMultiExecuteParams, _DBAPISingleExecuteParams)]
_DBAPICursorDescription = Sequence[Tuple[(str, 'DBAPIType', Optional[int], Optional[int], Optional[int], Optional[int], Optional[bool])]]
_AnySingleExecuteParams = _DBAPISingleExecuteParams
_AnyMultiExecuteParams = _DBAPIMultiExecuteParams
_AnyExecuteParams = _DBAPIAnyExecuteParams
CompiledCacheType = MutableMapping[(Any, 'Compiled')]
SchemaTranslateMapType = Mapping[(Optional[str], Optional[str])]
_ImmutableExecuteOptions = immutabledict[(str, Any)]
_ParamStyle = Literal[('qmark', 'numeric', 'named', 'format', 'pyformat', 'numeric_dollar')]
_GenericSetInputSizesType = List[Tuple[(str, Any, 'TypeEngine[Any]')]]
IsolationLevel = Literal[('SERIALIZABLE', 'REPEATABLE READ', 'READ COMMITTED', 'READ UNCOMMITTED', 'AUTOCOMMIT')]

def _CoreKnownExecutionOptions():
    '''_CoreKnownExecutionOptions'''
    preserve_rowcount: 'bool' = '_CoreKnownExecutionOptions'

_CoreKnownExecutionOptions = <NODE:27>(_CoreKnownExecutionOptions, '_CoreKnownExecutionOptions', TypedDict, total = False)
_ExecuteOptions = immutabledict[(str, Any)]
CoreExecuteOptionsParameter = Union[(_CoreKnownExecutionOptions, Mapping[(str, Any)])]

class ReflectedIdentity(TypedDict):
    order: 'bool' = 'represent the reflected IDENTITY structure of a column, corresponding\n    to the :class:`_schema.Identity` construct.\n\n    The :class:`.ReflectedIdentity` structure is part of the\n    :class:`.ReflectedColumn` structure, which is returned by the\n    :meth:`.Inspector.get_columns` method.\n\n    '


class ReflectedComputed(TypedDict):
    persisted: 'NotRequired[bool]' = 'Represent the reflected elements of a computed column, corresponding\n    to the :class:`_schema.Computed` construct.\n\n    The :class:`.ReflectedComputed` structure is part of the\n    :class:`.ReflectedColumn` structure, which is returned by the\n    :meth:`.Inspector.get_columns` method.\n\n    '


class ReflectedColumn(TypedDict):
    dialect_options: 'NotRequired[Dict[str, Any]]' = 'Dictionary representing the reflected elements corresponding to\n    a :class:`_schema.Column` object.\n\n    The :class:`.ReflectedColumn` structure is returned by the\n    :class:`.Inspector.get_columns` method.\n\n    '


class ReflectedConstraint(TypedDict):
    comment: 'NotRequired[Optional[str]]' = 'Dictionary representing the reflected elements corresponding to\n    :class:`.Constraint`\n\n    A base class for all constraints\n    '


class ReflectedCheckConstraint(ReflectedConstraint):
    dialect_options: 'NotRequired[Dict[str, Any]]' = 'Dictionary representing the reflected elements corresponding to\n    :class:`.CheckConstraint`.\n\n    The :class:`.ReflectedCheckConstraint` structure is returned by the\n    :meth:`.Inspector.get_check_constraints` method.\n\n    '


class ReflectedUniqueConstraint(ReflectedConstraint):
    dialect_options: 'NotRequired[Dict[str, Any]]' = 'Dictionary representing the reflected elements corresponding to\n    :class:`.UniqueConstraint`.\n\n    The :class:`.ReflectedUniqueConstraint` structure is returned by the\n    :meth:`.Inspector.get_unique_constraints` method.\n\n    '


class ReflectedPrimaryKeyConstraint(ReflectedConstraint):
    dialect_options: 'NotRequired[Dict[str, Any]]' = 'Dictionary representing the reflected elements corresponding to\n    :class:`.PrimaryKeyConstraint`.\n\n    The :class:`.ReflectedPrimaryKeyConstraint` structure is returned by the\n    :meth:`.Inspector.get_pk_constraint` method.\n\n    '


class ReflectedForeignKeyConstraint(ReflectedConstraint):
    options: 'NotRequired[Dict[str, Any]]' = 'Dictionary representing the reflected elements corresponding to\n    :class:`.ForeignKeyConstraint`.\n\n    The :class:`.ReflectedForeignKeyConstraint` structure is returned by\n    the :meth:`.Inspector.get_foreign_keys` method.\n\n    '


class ReflectedIndex(TypedDict):
    dialect_options: 'NotRequired[Dict[str, Any]]' = 'Dictionary representing the reflected elements corresponding to\n    :class:`.Index`.\n\n    The :class:`.ReflectedIndex` structure is returned by the\n    :meth:`.Inspector.get_indexes` method.\n\n    '


class ReflectedTableComment(TypedDict):
    text: 'Optional[str]' = 'Dictionary representing the reflected comment corresponding to\n    the :attr:`_schema.Table.comment` attribute.\n\n    The :class:`.ReflectedTableComment` structure is returned by the\n    :meth:`.Inspector.get_table_comment` method.\n\n    '


class BindTyping(Enum):
    '''Define different methods of passing typing information for
    bound parameters in a statement to the database driver.

    .. versionadded:: 2.0

    '''
    NONE = 1
    SETINPUTSIZES = 2
    RENDER_CASTS = 3

VersionInfoType = Tuple[(Union[(int, str)], ...)]
TableKey = Tuple[(Optional[str], str)]

class Dialect(EventTarget):
    '''Define the behavior of a specific database and DB-API combination.

    Any aspect of metadata definition, SQL query generation,
    execution, result-set handling, or anything else which varies
    between databases is defined under the general category of the
    Dialect.  The Dialect acts as a factory for other
    database-specific object implementations including
    ExecutionContext, Compiled, DefaultGenerator, and TypeEngine.

    .. note:: Third party dialects should not subclass :class:`.Dialect`
       directly.  Instead, subclass :class:`.default.DefaultDialect` or
       descendant class.

    '''
    CACHE_HIT = CacheStats.CACHE_HIT
    CACHE_MISS = CacheStats.CACHE_MISS
    CACHING_DISABLED = CacheStats.CACHING_DISABLED
    NO_CACHE_KEY = CacheStats.NO_CACHE_KEY
    dbapi: 'Optional[DBAPIModule]' = CacheStats.NO_DIALECT_SUPPORT
    supports_default_metavalue: 'bool' = (lambda self = None: raise NotImplementedError())()
    returns_native_bytes: 'bool' = 'DEFAULT'
    construct_arguments: 'Optional[List[Tuple[Type[Union[SchemaItem, ClauseElement]], Mapping[str, Any]]]]' = None
    reflection_options: 'Sequence[str]' = ()
    supports_constraint_comments: 'bool' = util.EMPTY_DICT
    _has_events = False
    _supports_statement_cache: 'bool' = True
    _type_memos: 'MutableMapping[TypeEngine[Any], _TypeMemoDict]' = BindTyping.NONE
    
    def _builtin_onconnect(self = None):
        raise NotImplementedError()

    
    def create_connect_args(self = None, url = None):
        """Build DB-API compatible connection arguments.

        Given a :class:`.URL` object, returns a tuple
        consisting of a ``(*args, **kwargs)`` suitable to send directly
        to the dbapi's connect function.   The arguments are sent to the
        :meth:`.Dialect.connect` method which then runs the DBAPI-level
        ``connect()`` function.

        The method typically makes use of the
        :meth:`.URL.translate_connect_args`
        method in order to generate a dictionary of options.

        The default implementation is::

            def create_connect_args(self, url):
                opts = url.translate_connect_args()
                opts.update(url.query)
                return ([], opts)

        :param url: a :class:`.URL` object

        :return: a tuple of ``(*args, **kwargs)`` which will be passed to the
         :meth:`.Dialect.connect` method.

        .. seealso::

            :meth:`.URL.translate_connect_args`

        """
        raise NotImplementedError()

    import_dbapi = (lambda cls = None: raise NotImplementedError())()
    
    def type_descriptor(self = None, typeobj = None):
        '''Transform a generic type to a dialect-specific type.

        Dialect classes will usually use the
        :func:`_types.adapt_type` function in the types module to
        accomplish this.

        The returned result is cached *per dialect class* so can
        contain no dialect-instance state.

        '''
        raise NotImplementedError()

    
    def initialize(self = None, connection = None):
        '''Called during strategized creation of the dialect with a
        connection.

        Allows dialects to configure options based on server version info or
        other properties.

        The connection passed here is a SQLAlchemy Connection object,
        with full capabilities.

        The initialize() method of the base dialect should be called via
        super().

        .. note:: as of SQLAlchemy 1.4, this method is called **before**
           any :meth:`_engine.Dialect.on_connect` hooks are called.

        '''
        pass

    if TYPE_CHECKING:
        
        def _overrides_default(self = None, method_name = None):
            pass

    
    def get_columns(self = None, connection = None, table_name = None, schema = (None,), **kw):
        '''Return information about columns in ``table_name``.

        Given a :class:`_engine.Connection`, a string
        ``table_name``, and an optional string ``schema``, return column
        information as a list of dictionaries
        corresponding to the :class:`.ReflectedColumn` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_columns`.

        '''
        raise NotImplementedError()

    
    def get_multi_columns(self = None, connection = None, *, schema, filter_names, **kw):
        '''Return information about columns in all tables in the
        given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_multi_columns`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        '''
        raise NotImplementedError()

    
    def get_pk_constraint(self = None, connection = None, table_name = None, schema = (None,), **kw):
        '''Return information about the primary key constraint on
        table_name`.

        Given a :class:`_engine.Connection`, a string
        ``table_name``, and an optional string ``schema``, return primary
        key information as a dictionary corresponding to the
        :class:`.ReflectedPrimaryKeyConstraint` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_pk_constraint`.

        '''
        raise NotImplementedError()

    
    def get_multi_pk_constraint(self = None, connection = None, *, schema, filter_names, **kw):
        '''Return information about primary key constraints in
        all tables in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_multi_pk_constraint`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        '''
        raise NotImplementedError()

    
    def get_foreign_keys(self = None, connection = None, table_name = None, schema = (None,), **kw):
        '''Return information about foreign_keys in ``table_name``.

        Given a :class:`_engine.Connection`, a string
        ``table_name``, and an optional string ``schema``, return foreign
        key information as a list of dicts corresponding to the
        :class:`.ReflectedForeignKeyConstraint` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_foreign_keys`.
        '''
        raise NotImplementedError()

    
    def get_multi_foreign_keys(self = None, connection = None, *, schema, filter_names, **kw):
        '''Return information about foreign_keys in all tables
        in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_multi_foreign_keys`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        '''
        raise NotImplementedError()

    
    def get_table_names(self = None, connection = None, schema = None, **kw):
        '''Return a list of table names for ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_table_names`.

        '''
        raise NotImplementedError()

    
    def get_temp_table_names(self = None, connection = None, schema = None, **kw):
        '''Return a list of temporary table names on the given connection,
        if supported by the underlying backend.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_temp_table_names`.

        '''
        raise NotImplementedError()

    
    def get_view_names(self = None, connection = None, schema = None, **kw):
        '''Return a list of all non-materialized view names available in the
        database.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_view_names`.

        :param schema: schema name to query, if not the default schema.

        '''
        raise NotImplementedError()

    
    def get_materialized_view_names(self = None, connection = None, schema = None, **kw):
        '''Return a list of all materialized view names available in the
        database.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_materialized_view_names`.

        :param schema: schema name to query, if not the default schema.

         .. versionadded:: 2.0

        '''
        raise NotImplementedError()

    
    def get_sequence_names(self = None, connection = None, schema = None, **kw):
        '''Return a list of all sequence names available in the database.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_sequence_names`.

        :param schema: schema name to query, if not the default schema.

        .. versionadded:: 1.4
        '''
        raise NotImplementedError()

    
    def get_temp_view_names(self = None, connection = None, schema = None, **kw):
        '''Return a list of temporary view names on the given connection,
        if supported by the underlying backend.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_temp_view_names`.

        '''
        raise NotImplementedError()

    
    def get_schema_names(self = None, connection = None, **kw):
        '''Return a list of all schema names available in the database.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_schema_names`.
        '''
        raise NotImplementedError()

    
    def get_view_definition(self = None, connection = None, view_name = None, schema = (None,), **kw):
        '''Return plain or materialized view definition.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_view_definition`.

        Given a :class:`_engine.Connection`, a string
        ``view_name``, and an optional string ``schema``, return the view
        definition.
        '''
        raise NotImplementedError()

    
    def get_indexes(self = None, connection = None, table_name = None, schema = (None,), **kw):
        '''Return information about indexes in ``table_name``.

        Given a :class:`_engine.Connection`, a string
        ``table_name`` and an optional string ``schema``, return index
        information as a list of dictionaries corresponding to the
        :class:`.ReflectedIndex` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_indexes`.
        '''
        raise NotImplementedError()

    
    def get_multi_indexes(self = None, connection = None, *, schema, filter_names, **kw):
        '''Return information about indexes in in all tables
        in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_multi_indexes`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        '''
        raise NotImplementedError()

    
    def get_unique_constraints(self = None, connection = None, table_name = None, schema = (None,), **kw):
        '''Return information about unique constraints in ``table_name``.

        Given a string ``table_name`` and an optional string ``schema``, return
        unique constraint information as a list of dicts corresponding
        to the :class:`.ReflectedUniqueConstraint` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_unique_constraints`.
        '''
        raise NotImplementedError()

    
    def get_multi_unique_constraints(self = None, connection = None, *, schema, filter_names, **kw):
        '''Return information about unique constraints in all tables
        in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_multi_unique_constraints`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        '''
        raise NotImplementedError()

    
    def get_check_constraints(self = None, connection = None, table_name = None, schema = (None,), **kw):
        '''Return information about check constraints in ``table_name``.

        Given a string ``table_name`` and an optional string ``schema``, return
        check constraint information as a list of dicts corresponding
        to the :class:`.ReflectedCheckConstraint` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_check_constraints`.

        '''
        raise NotImplementedError()

    
    def get_multi_check_constraints(self = None, connection = None, *, schema, filter_names, **kw):
        '''Return information about check constraints in all tables
        in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_multi_check_constraints`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        '''
        raise NotImplementedError()

    
    def get_table_options(self = None, connection = None, table_name = None, schema = (None,), **kw):
        '''Return a dictionary of options specified when ``table_name``
        was created.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_table_options`.
        '''
        raise NotImplementedError()

    
    def get_multi_table_options(self = None, connection = None, *, schema, filter_names, **kw):
        '''Return a dictionary of options specified when the tables in the
        given schema were created.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_multi_table_options`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        '''
        raise NotImplementedError()

    
    def get_table_comment(self = None, connection = None, table_name = None, schema = (None,), **kw):
        '''Return the "comment" for the table identified by ``table_name``.

        Given a string ``table_name`` and an optional string ``schema``, return
        table comment information as a dictionary corresponding to the
        :class:`.ReflectedTableComment` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_table_comment`.

        :raise: ``NotImplementedError`` for dialects that don\'t support
         comments.

        .. versionadded:: 1.2

        '''
        raise NotImplementedError()

    
    def get_multi_table_comment(self = None, connection = None, *, schema, filter_names, **kw):
        '''Return information about the table comment in all tables
        in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_multi_table_comment`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        '''
        raise NotImplementedError()

    
    def normalize_name(self = None, name = None):
        '''convert the given name to lowercase if it is detected as
        case insensitive.

        This method is only used if the dialect defines
        requires_name_normalize=True.

        '''
        raise NotImplementedError()

    
    def denormalize_name(self = None, name = None):
        '''convert the given name to a case insensitive identifier
        for the backend if it is an all-lowercase name.

        This method is only used if the dialect defines
        requires_name_normalize=True.

        '''
        raise NotImplementedError()

    
    def has_table(self = None, connection = None, table_name = None, schema = (None,), **kw):
        '''For internal dialect use, check the existence of a particular table
        or view in the database.

        Given a :class:`_engine.Connection` object, a string table_name and
        optional schema name, return True if the given table exists in the
        database, False otherwise.

        This method serves as the underlying implementation of the
        public facing :meth:`.Inspector.has_table` method, and is also used
        internally to implement the "checkfirst" behavior for methods like
        :meth:`_schema.Table.create` and :meth:`_schema.MetaData.create_all`.

        .. note:: This method is used internally by SQLAlchemy, and is
           published so that third-party dialects may provide an
           implementation. It is **not** the public API for checking for table
           presence. Please use the :meth:`.Inspector.has_table` method.

        .. versionchanged:: 2.0:: :meth:`_engine.Dialect.has_table` now
           formally supports checking for additional table-like objects:

           * any type of views (plain or materialized)
           * temporary tables of any kind

           Previously, these two checks were not formally specified and
           different dialects would vary in their behavior.   The dialect
           testing suite now includes tests for all of these object types,
           and dialects to the degree that the backing database supports views
           or temporary tables should seek to support locating these objects
           for full compliance.

        '''
        raise NotImplementedError()

    
    def has_index(self = None, connection = None, table_name = None, index_name = (None,), schema = ('connection', 'Connection', 'table_name', 'str', 'index_name', 'str', 'schema', 'Optional[str]', 'kw', 'Any', 'return', 'bool'), **kw):
        '''Check the existence of a particular index name in the database.

        Given a :class:`_engine.Connection` object, a string
        ``table_name`` and string index name, return ``True`` if an index of
        the given name on the given table exists, ``False`` otherwise.

        The :class:`.DefaultDialect` implements this in terms of the
        :meth:`.Dialect.has_table` and :meth:`.Dialect.get_indexes` methods,
        however dialects can implement a more performant version.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.has_index`.

        .. versionadded:: 1.4

        '''
        raise NotImplementedError()

    
    def has_sequence(self = None, connection = None, sequence_name = None, schema = (None,), **kw):
        '''Check the existence of a particular sequence in the database.

        Given a :class:`_engine.Connection` object and a string
        `sequence_name`, return ``True`` if the given sequence exists in
        the database, ``False`` otherwise.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.has_sequence`.
        '''
        raise NotImplementedError()

    
    def has_schema(self = None, connection = None, schema_name = None, **kw):
        '''Check the existence of a particular schema name in the database.

        Given a :class:`_engine.Connection` object, a string
        ``schema_name``, return ``True`` if a schema of the
        given exists, ``False`` otherwise.

        The :class:`.DefaultDialect` implements this by checking
        the presence of ``schema_name`` among the schemas returned by
        :meth:`.Dialect.get_schema_names`,
        however dialects can implement a more performant version.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.has_schema`.

        .. versionadded:: 2.0

        '''
        raise NotImplementedError()

    
    def _get_server_version_info(self = None, connection = None):
        '''Retrieve the server version info from the given connection.

        This is used by the default implementation to populate the
        "server_version_info" attribute and is called exactly
        once upon first connect.

        '''
        raise NotImplementedError()

    
    def _get_default_schema_name(self = None, connection = None):
        '''Return the string name of the currently selected schema from
        the given connection.

        This is used by the default implementation to populate the
        "default_schema_name" attribute and is called exactly
        once upon first connect.

        '''
        raise NotImplementedError()

    
    def do_begin(self = None, dbapi_connection = None):
        '''Provide an implementation of ``connection.begin()``, given a
        DB-API connection.

        The DBAPI has no dedicated "begin" method and it is expected
        that transactions are implicit.  This hook is provided for those
        DBAPIs that might need additional help in this area.

        :param dbapi_connection: a DBAPI connection, typically
         proxied within a :class:`.ConnectionFairy`.

        '''
        raise NotImplementedError()

    
    def do_rollback(self = None, dbapi_connection = None):
        '''Provide an implementation of ``connection.rollback()``, given
        a DB-API connection.

        :param dbapi_connection: a DBAPI connection, typically
         proxied within a :class:`.ConnectionFairy`.

        '''
        raise NotImplementedError()

    
    def do_commit(self = None, dbapi_connection = None):
        '''Provide an implementation of ``connection.commit()``, given a
        DB-API connection.

        :param dbapi_connection: a DBAPI connection, typically
         proxied within a :class:`.ConnectionFairy`.

        '''
        raise NotImplementedError()

    
    def do_terminate(self = None, dbapi_connection = None):
        '''Provide an implementation of ``connection.close()`` that tries as
        much as possible to not block, given a DBAPI
        connection.

        In the vast majority of cases this just calls .close(), however
        for some asyncio dialects may call upon different API features.

        This hook is called by the :class:`_pool.Pool`
        when a connection is being recycled or has been invalidated.

        .. versionadded:: 1.4.41

        '''
        raise NotImplementedError()

    
    def do_close(self = None, dbapi_connection = None):
        '''Provide an implementation of ``connection.close()``, given a DBAPI
        connection.

        This hook is called by the :class:`_pool.Pool`
        when a connection has been
        detached from the pool, or is being returned beyond the normal
        capacity of the pool.

        '''
        raise NotImplementedError()

    
    def _do_ping_w_event(self = None, dbapi_connection = None):
        raise NotImplementedError()

    
    def do_ping(self = None, dbapi_connection = None):
        '''ping the DBAPI connection and return True if the connection is
        usable.'''
        raise NotImplementedError()

    
    def do_set_input_sizes(self = None, cursor = None, list_of_tuples = None, context = ('cursor', 'DBAPICursor', 'list_of_tuples', '_GenericSetInputSizesType', 'context', 'ExecutionContext', 'return', 'Any')):
        '''invoke the cursor.setinputsizes() method with appropriate arguments

        This hook is called if the :attr:`.Dialect.bind_typing` attribute is
        set to the
        :attr:`.BindTyping.SETINPUTSIZES` value.
        Parameter data is passed in a list of tuples (paramname, dbtype,
        sqltype), where ``paramname`` is the key of the parameter in the
        statement, ``dbtype`` is the DBAPI datatype and ``sqltype`` is the
        SQLAlchemy type. The order of tuples is in the correct parameter order.

        .. versionadded:: 1.4

        .. versionchanged:: 2.0  - setinputsizes mode is now enabled by
           setting :attr:`.Dialect.bind_typing` to
           :attr:`.BindTyping.SETINPUTSIZES`.  Dialects which accept
           a ``use_setinputsizes`` parameter should set this value
           appropriately.


        '''
        raise NotImplementedError()

    
    def create_xid(self = None):
        '''Create a two-phase transaction ID.

        This id will be passed to do_begin_twophase(),
        do_rollback_twophase(), do_commit_twophase().  Its format is
        unspecified.
        '''
        raise NotImplementedError()

    
    def do_savepoint(self = None, connection = None, name = None):
        '''Create a savepoint with the given name.

        :param connection: a :class:`_engine.Connection`.
        :param name: savepoint name.

        '''
        raise NotImplementedError()

    
    def do_rollback_to_savepoint(self = None, connection = None, name = None):
        '''Rollback a connection to the named savepoint.

        :param connection: a :class:`_engine.Connection`.
        :param name: savepoint name.

        '''
        raise NotImplementedError()

    
    def do_release_savepoint(self = None, connection = None, name = None):
        '''Release the named savepoint on a connection.

        :param connection: a :class:`_engine.Connection`.
        :param name: savepoint name.
        '''
        raise NotImplementedError()

    
    def do_begin_twophase(self = None, connection = None, xid = None):
        '''Begin a two phase transaction on the given connection.

        :param connection: a :class:`_engine.Connection`.
        :param xid: xid

        '''
        raise NotImplementedError()

    
    def do_prepare_twophase(self = None, connection = None, xid = None):
        '''Prepare a two phase transaction on the given connection.

        :param connection: a :class:`_engine.Connection`.
        :param xid: xid

        '''
        raise NotImplementedError()

    
    def do_rollback_twophase(self = None, connection = None, xid = None, is_prepared = (True, False), recover = ('connection', 'Connection', 'xid', 'Any', 'is_prepared', 'bool', 'recover', 'bool', 'return', 'None')):
        '''Rollback a two phase transaction on the given connection.

        :param connection: a :class:`_engine.Connection`.
        :param xid: xid
        :param is_prepared: whether or not
         :meth:`.TwoPhaseTransaction.prepare` was called.
        :param recover: if the recover flag was passed.

        '''
        raise NotImplementedError()

    
    def do_commit_twophase(self = None, connection = None, xid = None, is_prepared = (True, False), recover = ('connection', 'Connection', 'xid', 'Any', 'is_prepared', 'bool', 'recover', 'bool', 'return', 'None')):
        '''Commit a two phase transaction on the given connection.


        :param connection: a :class:`_engine.Connection`.
        :param xid: xid
        :param is_prepared: whether or not
         :meth:`.TwoPhaseTransaction.prepare` was called.
        :param recover: if the recover flag was passed.

        '''
        raise NotImplementedError()

    
    def do_recover_twophase(self = None, connection = None):
        '''Recover list of uncommitted prepared two phase transaction
        identifiers on the given connection.

        :param connection: a :class:`_engine.Connection`.

        '''
        raise NotImplementedError()

    
    def _deliver_insertmanyvalues_batches(self, connection, cursor, statement = None, parameters = None, generic_setinputsizes = None, context = ('connection', 'Connection', 'cursor', 'DBAPICursor', 'statement', 'str', 'parameters', '_DBAPIMultiExecuteParams', 'generic_setinputsizes', 'Optional[_GenericSetInputSizesType]', 'context', 'ExecutionContext', 'return', 'Iterator[_InsertManyValuesBatch]')):
        '''convert executemany parameters for an INSERT into an iterator
        of statement/single execute values, used by the insertmanyvalues
        feature.

        '''
        raise NotImplementedError()

    
    def do_executemany(self = None, cursor = None, statement = None, parameters = (None,), context = ('cursor', 'DBAPICursor', 'statement', 'str', 'parameters', '_DBAPIMultiExecuteParams', 'context', 'Optional[ExecutionContext]', 'return', 'None')):
        '''Provide an implementation of ``cursor.executemany(statement,
        parameters)``.'''
        raise NotImplementedError()

    
    def do_execute(self = None, cursor = None, statement = None, parameters = (None,), context = ('cursor', 'DBAPICursor', 'statement', 'str', 'parameters', 'Optional[_DBAPISingleExecuteParams]', 'context', 'Optional[ExecutionContext]', 'return', 'None')):
        '''Provide an implementation of ``cursor.execute(statement,
        parameters)``.'''
        raise NotImplementedError()

    
    def do_execute_no_params(self = None, cursor = None, statement = None, context = (None,)):
        '''Provide an implementation of ``cursor.execute(statement)``.

        The parameter collection should not be sent.

        '''
        raise NotImplementedError()

    
    def is_disconnect(self = None, e = None, connection = None, cursor = ('e', 'DBAPIModule.Error', 'connection', 'Optional[Union[PoolProxiedConnection, DBAPIConnection]]', 'cursor', 'Optional[DBAPICursor]', 'return', 'bool')):
        '''Return True if the given DB-API error indicates an invalid
        connection'''
        raise NotImplementedError()

    
    def connect(self = None, *cargs, **cparams):
        """Establish a connection using this dialect's DBAPI.

        The default implementation of this method is::

            def connect(self, *cargs, **cparams):
                return self.dbapi.connect(*cargs, **cparams)

        The ``*cargs, **cparams`` parameters are generated directly
        from this dialect's :meth:`.Dialect.create_connect_args` method.

        This method may be used for dialects that need to perform programmatic
        per-connection steps when a new connection is procured from the
        DBAPI.


        :param \\*cargs: positional parameters returned from the
         :meth:`.Dialect.create_connect_args` method

        :param \\*\\*cparams: keyword parameters returned from the
         :meth:`.Dialect.create_connect_args` method.

        :return: a DBAPI connection, typically from the :pep:`249` module
         level ``.connect()`` function.

        .. seealso::

            :meth:`.Dialect.create_connect_args`

            :meth:`.Dialect.on_connect`

        """
        raise NotImplementedError()

    
    def on_connect_url(self = None, url = None):
        '''return a callable which sets up a newly created DBAPI connection.

        This method is a new hook that supersedes the
        :meth:`_engine.Dialect.on_connect` method when implemented by a
        dialect.   When not implemented by a dialect, it invokes the
        :meth:`_engine.Dialect.on_connect` method directly to maintain
        compatibility with existing dialects.   There is no deprecation
        for :meth:`_engine.Dialect.on_connect` expected.

        The callable should accept a single argument "conn" which is the
        DBAPI connection itself.  The inner callable has no
        return value.

        E.g.::

            class MyDialect(default.DefaultDialect):
                # ...

                def on_connect_url(self, url):
                    def do_on_connect(connection):
                        connection.execute("SET SPECIAL FLAGS etc")

                    return do_on_connect

        This is used to set dialect-wide per-connection options such as
        isolation modes, Unicode modes, etc.

        This method differs from :meth:`_engine.Dialect.on_connect` in that
        it is passed the :class:`_engine.URL` object that\'s relevant to the
        connect args.  Normally the only way to get this is from the
        :meth:`_engine.Dialect.on_connect` hook is to look on the
        :class:`_engine.Engine` itself, however this URL object may have been
        replaced by plugins.

        .. note::

            The default implementation of
            :meth:`_engine.Dialect.on_connect_url` is to invoke the
            :meth:`_engine.Dialect.on_connect` method. Therefore if a dialect
            implements this method, the :meth:`_engine.Dialect.on_connect`
            method **will not be called** unless the overriding dialect calls
            it directly from here.

        .. versionadded:: 1.4.3 added :meth:`_engine.Dialect.on_connect_url`
           which normally calls into :meth:`_engine.Dialect.on_connect`.

        :param url: a :class:`_engine.URL` object representing the
         :class:`_engine.URL` that was passed to the
         :meth:`_engine.Dialect.create_connect_args` method.

        :return: a callable that accepts a single DBAPI connection as an
         argument, or None.

        .. seealso::

            :meth:`_engine.Dialect.on_connect`

        '''
        return self.on_connect()

    
    def on_connect(self = None):
        '''return a callable which sets up a newly created DBAPI connection.

        The callable should accept a single argument "conn" which is the
        DBAPI connection itself.  The inner callable has no
        return value.

        E.g.::

            class MyDialect(default.DefaultDialect):
                # ...

                def on_connect(self):
                    def do_on_connect(connection):
                        connection.execute("SET SPECIAL FLAGS etc")

                    return do_on_connect

        This is used to set dialect-wide per-connection options such as
        isolation modes, Unicode modes, etc.

        The "do_on_connect" callable is invoked by using the
        :meth:`_events.PoolEvents.connect` event
        hook, then unwrapping the DBAPI connection and passing it into the
        callable.

        .. versionchanged:: 1.4 the on_connect hook is no longer called twice
           for the first connection of a dialect.  The on_connect hook is still
           called before the :meth:`_engine.Dialect.initialize` method however.

        .. versionchanged:: 1.4.3 the on_connect hook is invoked from a new
           method on_connect_url that passes the URL that was used to create
           the connect args.   Dialects can implement on_connect_url instead
           of on_connect if they need the URL object that was used for the
           connection in order to get additional context.

        If None is returned, no event listener is generated.

        :return: a callable that accepts a single DBAPI connection as an
         argument, or None.

        .. seealso::

            :meth:`.Dialect.connect` - allows the DBAPI ``connect()`` sequence
            itself to be controlled.

            :meth:`.Dialect.on_connect_url` - supersedes
            :meth:`.Dialect.on_connect` to also receive the
            :class:`_engine.URL` object in context.

        '''
        pass

    
    def reset_isolation_level(self = None, dbapi_connection = None):
        '''Given a DBAPI connection, revert its isolation to the default.

        Note that this is a dialect-level method which is used as part
        of the implementation of the :class:`_engine.Connection` and
        :class:`_engine.Engine`
        isolation level facilities; these APIs should be preferred for
        most typical use cases.

        .. seealso::

            :meth:`_engine.Connection.get_isolation_level`
            - view current level

            :attr:`_engine.Connection.default_isolation_level`
            - view default level

            :paramref:`.Connection.execution_options.isolation_level` -
            set per :class:`_engine.Connection` isolation level

            :paramref:`_sa.create_engine.isolation_level` -
            set per :class:`_engine.Engine` isolation level

        '''
        raise NotImplementedError()

    
    def set_isolation_level(self = None, dbapi_connection = None, level = None):
        '''Given a DBAPI connection, set its isolation level.

        Note that this is a dialect-level method which is used as part
        of the implementation of the :class:`_engine.Connection` and
        :class:`_engine.Engine`
        isolation level facilities; these APIs should be preferred for
        most typical use cases.

        If the dialect also implements the
        :meth:`.Dialect.get_isolation_level_values` method, then the given
        level is guaranteed to be one of the string names within that sequence,
        and the method will not need to anticipate a lookup failure.

        .. seealso::

            :meth:`_engine.Connection.get_isolation_level`
            - view current level

            :attr:`_engine.Connection.default_isolation_level`
            - view default level

            :paramref:`.Connection.execution_options.isolation_level` -
            set per :class:`_engine.Connection` isolation level

            :paramref:`_sa.create_engine.isolation_level` -
            set per :class:`_engine.Engine` isolation level

        '''
        raise NotImplementedError()

    
    def get_isolation_level(self = None, dbapi_connection = None):
        '''Given a DBAPI connection, return its isolation level.

        When working with a :class:`_engine.Connection` object,
        the corresponding
        DBAPI connection may be procured using the
        :attr:`_engine.Connection.connection` accessor.

        Note that this is a dialect-level method which is used as part
        of the implementation of the :class:`_engine.Connection` and
        :class:`_engine.Engine` isolation level facilities;
        these APIs should be preferred for most typical use cases.


        .. seealso::

            :meth:`_engine.Connection.get_isolation_level`
            - view current level

            :attr:`_engine.Connection.default_isolation_level`
            - view default level

            :paramref:`.Connection.execution_options.isolation_level` -
            set per :class:`_engine.Connection` isolation level

            :paramref:`_sa.create_engine.isolation_level` -
            set per :class:`_engine.Engine` isolation level


        '''
        raise NotImplementedError()

    
    def detect_autocommit_setting(self = None, dbapi_conn = None):
        '''Detect the current autocommit setting for a DBAPI connection.

        :param dbapi_connection: a DBAPI connection object
        :return: True if autocommit is enabled, False if disabled
        :rtype: bool

        This method inspects the given DBAPI connection to determine
        whether autocommit mode is currently enabled. The specific
        mechanism for detecting autocommit varies by database dialect
        and DBAPI driver, however it should be done **without** network
        round trips.

        .. note::

            Not all dialects support autocommit detection. Dialects
            that do not support this feature will raise
            :exc:`NotImplementedError`.

        '''
        raise NotImplementedError('This dialect cannot detect autocommit on a DBAPI connection')

    
    def get_default_isolation_level(self = None, dbapi_conn = None):
        '''Given a DBAPI connection, return its isolation level, or
        a default isolation level if one cannot be retrieved.

        This method may only raise NotImplementedError and
        **must not raise any other exception**, as it is used implicitly upon
        first connect.

        The method **must return a value** for a dialect that supports
        isolation level settings, as this level is what will be reverted
        towards when a per-connection isolation level change is made.

        The method defaults to using the :meth:`.Dialect.get_isolation_level`
        method unless overridden by a dialect.

        .. versionadded:: 1.3.22

        '''
        raise NotImplementedError()

    
    def get_isolation_level_values(self = None, dbapi_conn = None):
        '''return a sequence of string isolation level names that are accepted
        by this dialect.

        The available names should use the following conventions:

        * use UPPERCASE names.   isolation level methods will accept lowercase
          names but these are normalized into UPPERCASE before being passed
          along to the dialect.
        * separate words should be separated by spaces, not underscores, e.g.
          ``REPEATABLE READ``.  isolation level names will have underscores
          converted to spaces before being passed along to the dialect.
        * The names for the four standard isolation names to the extent that
          they are supported by the backend should be ``READ UNCOMMITTED``,
          ``READ COMMITTED``, ``REPEATABLE READ``, ``SERIALIZABLE``
        * if the dialect supports an autocommit option it should be provided
          using the isolation level name ``AUTOCOMMIT``.
        * Other isolation modes may also be present, provided that they
          are named in UPPERCASE and use spaces not underscores.

        This function is used so that the default dialect can check that
        a given isolation level parameter is valid, else raises an
        :class:`_exc.ArgumentError`.

        A DBAPI connection is passed to the method, in the unlikely event that
        the dialect needs to interrogate the connection itself to determine
        this list, however it is expected that most backends will return
        a hardcoded list of values.  If the dialect supports "AUTOCOMMIT",
        that value should also be present in the sequence returned.

        The method raises ``NotImplementedError`` by default.  If a dialect
        does not implement this method, then the default dialect will not
        perform any checking on a given isolation level value before passing
        it onto the :meth:`.Dialect.set_isolation_level` method.  This is
        to allow backwards-compatibility with third party dialects that may
        not yet be implementing this method.

        .. versionadded:: 2.0

        '''
        raise NotImplementedError()

    
    def _assert_and_set_isolation_level(self = None, dbapi_conn = None, level = None):
        raise NotImplementedError()

    get_dialect_cls = (lambda cls = None, url = None: cls)()
    get_async_dialect_cls = (lambda cls = None, url = None: cls.get_dialect_cls(url))()
    load_provisioning = (lambda cls = None: pass)()
    engine_created = (lambda cls = None, engine = None: pass)()
    
    def get_driver_connection(self = None, connection = None):
        '''Returns the connection object as returned by the external driver
        package.

        For normal dialects that use a DBAPI compliant driver this call
        will just return the ``connection`` passed as argument.
        For dialects that instead adapt a non DBAPI compliant driver, like
        when adapting an asyncio driver, this call will return the
        connection-like object as returned by the driver.

        .. versionadded:: 1.4.24

        '''
        raise NotImplementedError()

    
    def set_engine_execution_options(self = None, engine = None, opts = None):
        '''Establish execution options for a given engine.

        This is implemented by :class:`.DefaultDialect` to establish
        event hooks for new :class:`.Connection` instances created
        by the given :class:`.Engine` which will then invoke the
        :meth:`.Dialect.set_connection_execution_options` method for that
        connection.

        '''
        raise NotImplementedError()

    
    def set_connection_execution_options(self = None, connection = None, opts = None):
        '''Establish execution options for a given connection.

        This is implemented by :class:`.DefaultDialect` in order to implement
        the :paramref:`_engine.Connection.execution_options.isolation_level`
        execution option.  Dialects can intercept various execution options
        which may need to modify state on a particular DBAPI connection.

        .. versionadded:: 1.4

        '''
        raise NotImplementedError()

    
    def get_dialect_pool_class(self = None, url = None):
        '''return a Pool class to use for a given URL'''
        raise NotImplementedError()

    
    def validate_identifier(self = None, ident = None):
        '''Validates an identifier name, raising an exception if invalid'''
        pass



class CreateEnginePlugin:
    '''A set of hooks intended to augment the construction of an
    :class:`_engine.Engine` object based on entrypoint names in a URL.

    The purpose of :class:`_engine.CreateEnginePlugin` is to allow third-party
    systems to apply engine, pool and dialect level event listeners without
    the need for the target application to be modified; instead, the plugin
    names can be added to the database URL.  Target applications for
    :class:`_engine.CreateEnginePlugin` include:

    * connection and SQL performance tools, e.g. which use events to track
      number of checkouts and/or time spent with statements

    * connectivity plugins such as proxies

    A rudimentary :class:`_engine.CreateEnginePlugin` that attaches a logger
    to an :class:`_engine.Engine` object might look like::


        import logging

        from sqlalchemy.engine import CreateEnginePlugin
        from sqlalchemy import event


        class LogCursorEventsPlugin(CreateEnginePlugin):
            def __init__(self, url, kwargs):
                # consume the parameter "log_cursor_logging_name" from the
                # URL query
                logging_name = url.query.get(
                    "log_cursor_logging_name", "log_cursor"
                )

                self.log = logging.getLogger(logging_name)

            def update_url(self, url):
                "update the URL to one that no longer includes our parameters"
                return url.difference_update_query(["log_cursor_logging_name"])

            def engine_created(self, engine):
                "attach an event listener after the new Engine is constructed"
                event.listen(engine, "before_cursor_execute", self._log_event)

            def _log_event(
                self,
                conn,
                cursor,
                statement,
                parameters,
                context,
                executemany,
            ):

                self.log.info("Plugin logged cursor event: %s", statement)

    Plugins are registered using entry points in a similar way as that
    of dialects::

        entry_points = {
            "sqlalchemy.plugins": [
                "log_cursor_plugin = myapp.plugins:LogCursorEventsPlugin"
            ]
        }

    A plugin that uses the above names would be invoked from a database
    URL as in::

        from sqlalchemy import create_engine

        engine = create_engine(
            "mysql+pymysql://scott:tiger@localhost/test?"
            "plugin=log_cursor_plugin&log_cursor_logging_name=mylogger"
        )

    The ``plugin`` URL parameter supports multiple instances, so that a URL
    may specify multiple plugins; they are loaded in the order stated
    in the URL::

        engine = create_engine(
            "mysql+pymysql://scott:tiger@localhost/test?"
            "plugin=plugin_one&plugin=plugin_twp&plugin=plugin_three"
        )

    The plugin names may also be passed directly to :func:`_sa.create_engine`
    using the :paramref:`_sa.create_engine.plugins` argument::

        engine = create_engine(
            "mysql+pymysql://scott:tiger@localhost/test", plugins=["myplugin"]
        )

    .. versionadded:: 1.2.3  plugin names can also be specified
       to :func:`_sa.create_engine` as a list

    A plugin may consume plugin-specific arguments from the
    :class:`_engine.URL` object as well as the ``kwargs`` dictionary, which is
    the dictionary of arguments passed to the :func:`_sa.create_engine`
    call.  "Consuming" these arguments includes that they must be removed
    when the plugin initializes, so that the arguments are not passed along
    to the :class:`_engine.Dialect` constructor, where they will raise an
    :class:`_exc.ArgumentError` because they are not known by the dialect.

    As of version 1.4 of SQLAlchemy, arguments should continue to be consumed
    from the ``kwargs`` dictionary directly, by removing the values with a
    method such as ``dict.pop``. Arguments from the :class:`_engine.URL` object
    should be consumed by implementing the
    :meth:`_engine.CreateEnginePlugin.update_url` method, returning a new copy
    of the :class:`_engine.URL` with plugin-specific parameters removed::

        class MyPlugin(CreateEnginePlugin):
            def __init__(self, url, kwargs):
                self.my_argument_one = url.query["my_argument_one"]
                self.my_argument_two = url.query["my_argument_two"]
                self.my_argument_three = kwargs.pop("my_argument_three", None)

            def update_url(self, url):
                return url.difference_update_query(
                    ["my_argument_one", "my_argument_two"]
                )

    Arguments like those illustrated above would be consumed from a
    :func:`_sa.create_engine` call such as::

        from sqlalchemy import create_engine

        engine = create_engine(
            "mysql+pymysql://scott:tiger@localhost/test?"
            "plugin=myplugin&my_argument_one=foo&my_argument_two=bar",
            my_argument_three="bat",
        )

    .. versionchanged:: 1.4

        The :class:`_engine.URL` object is now immutable; a
        :class:`_engine.CreateEnginePlugin` that needs to alter the
        :class:`_engine.URL` should implement the newly added
        :meth:`_engine.CreateEnginePlugin.update_url` method, which
        is invoked after the plugin is constructed.

        For migration, construct the plugin in the following way, checking
        for the existence of the :meth:`_engine.CreateEnginePlugin.update_url`
        method to detect which version is running::

            class MyPlugin(CreateEnginePlugin):
                def __init__(self, url, kwargs):
                    if hasattr(CreateEnginePlugin, "update_url"):
                        # detect the 1.4 API
                        self.my_argument_one = url.query["my_argument_one"]
                        self.my_argument_two = url.query["my_argument_two"]
                    else:
                        # detect the 1.3 and earlier API - mutate the
                        # URL directly
                        self.my_argument_one = url.query.pop("my_argument_one")
                        self.my_argument_two = url.query.pop("my_argument_two")

                    self.my_argument_three = kwargs.pop("my_argument_three", None)

                def update_url(self, url):
                    # this method is only called in the 1.4 version
                    return url.difference_update_query(
                        ["my_argument_one", "my_argument_two"]
                    )

        .. seealso::

            :ref:`change_5526` - overview of the :class:`_engine.URL` change which
            also includes notes regarding :class:`_engine.CreateEnginePlugin`.


    When the engine creation process completes and produces the
    :class:`_engine.Engine` object, it is again passed to the plugin via the
    :meth:`_engine.CreateEnginePlugin.engine_created` hook.  In this hook, additional
    changes can be made to the engine, most typically involving setup of
    events (e.g. those defined in :ref:`core_event_toplevel`).

    '''
    
    def __init__(self = None, url = None, kwargs = None):
        '''Construct a new :class:`.CreateEnginePlugin`.

        The plugin object is instantiated individually for each call
        to :func:`_sa.create_engine`.  A single :class:`_engine.
        Engine` will be
        passed to the :meth:`.CreateEnginePlugin.engine_created` method
        corresponding to this URL.

        :param url: the :class:`_engine.URL` object.  The plugin may inspect
         the :class:`_engine.URL` for arguments.  Arguments used by the
         plugin should be removed, by returning an updated :class:`_engine.URL`
         from the :meth:`_engine.CreateEnginePlugin.update_url` method.

         .. versionchanged::  1.4

            The :class:`_engine.URL` object is now immutable, so a
            :class:`_engine.CreateEnginePlugin` that needs to alter the
            :class:`_engine.URL` object should implement the
            :meth:`_engine.CreateEnginePlugin.update_url` method.

        :param kwargs: The keyword arguments passed to
         :func:`_sa.create_engine`.

        '''
        self.url = url

    
    def update_url(self = None, url = None):
        '''Update the :class:`_engine.URL`.

        A new :class:`_engine.URL` should be returned.   This method is
        typically used to consume configuration arguments from the
        :class:`_engine.URL` which must be removed, as they will not be
        recognized by the dialect.  The
        :meth:`_engine.URL.difference_update_query` method is available
        to remove these arguments.   See the docstring at
        :class:`_engine.CreateEnginePlugin` for an example.


        .. versionadded:: 1.4

        '''
        raise NotImplementedError()

    
    def handle_dialect_kwargs(self = None, dialect_cls = None, dialect_args = None):
        '''parse and modify dialect kwargs'''
        pass

    
    def handle_pool_kwargs(self = None, pool_cls = None, pool_args = None):
        '''parse and modify pool kwargs'''
        pass

    
    def engine_created(self = None, engine = None):
        '''Receive the :class:`_engine.Engine`
        object when it is fully constructed.

        The plugin may make additional changes to the engine, such as
        registering engine or connection pool events.

        '''
        pass



class ExecutionContext:
    execution_options: '_ExecuteOptions' = 'A messenger object for a Dialect that corresponds to a single\n    execution.\n\n    '
    _init_ddl = (lambda cls, dialect, connection = None, dbapi_connection = None, execution_options = classmethod, compiled_ddl = ('dialect', 'Dialect', 'connection', 'Connection', 'dbapi_connection', 'PoolProxiedConnection', 'execution_options', '_ExecuteOptions', 'compiled_ddl', 'DDLCompiler', 'return', 'ExecutionContext'): raise NotImplementedError())()
    _init_compiled = (lambda cls, dialect, connection, dbapi_connection, execution_options, compiled = None, parameters = None, invoked_statement = classmethod, extracted_parameters = (CacheStats.CACHING_DISABLED,), cache_hit = ('dialect', 'Dialect', 'connection', 'Connection', 'dbapi_connection', 'PoolProxiedConnection', 'execution_options', '_ExecuteOptions', 'compiled', 'SQLCompiler', 'parameters', '_CoreMultiExecuteParams', 'invoked_statement', 'Executable', 'extracted_parameters', 'Optional[Sequence[BindParameter[Any]]]', 'cache_hit', 'CacheStats', 'return', 'ExecutionContext'): raise NotImplementedError())()
    _init_statement = (lambda cls, dialect, connection, dbapi_connection = None, execution_options = None, statement = classmethod, parameters = ('dialect', 'Dialect', 'connection', 'Connection', 'dbapi_connection', 'PoolProxiedConnection', 'execution_options', '_ExecuteOptions', 'statement', 'str', 'parameters', '_DBAPIMultiExecuteParams', 'return', 'ExecutionContext'): raise NotImplementedError())()
    _init_default = (lambda cls, dialect = None, connection = None, dbapi_connection = classmethod, execution_options = ('dialect', 'Dialect', 'connection', 'Connection', 'dbapi_connection', 'PoolProxiedConnection', 'execution_options', '_ExecuteOptions', 'return', 'ExecutionContext'): raise NotImplementedError())()
    
    def _exec_default(self = None, column = None, default = None, type_ = ('column', 'Optional[Column[Any]]', 'default', 'DefaultGenerator', 'type_', 'Optional[TypeEngine[Any]]', 'return', 'Any')):
        raise NotImplementedError()

    
    def _prepare_set_input_sizes(self = None):
        raise NotImplementedError()

    
    def _get_cache_stats(self = None):
        raise NotImplementedError()

    
    def _setup_result_proxy(self = None):
        raise NotImplementedError()

    
    def fire_sequence(self = None, seq = None, type_ = None):
        '''given a :class:`.Sequence`, invoke it and return the next int
        value'''
        raise NotImplementedError()

    
    def create_cursor(self = None):
        '''Return a new cursor generated from this ExecutionContext\'s
        connection.

        Some dialects may wish to change the behavior of
        connection.cursor(), such as postgresql which may return a PG
        "server side" cursor.
        '''
        raise NotImplementedError()

    
    def pre_exec(self = None):
        '''Called before an execution of a compiled statement.

        If a compiled statement was passed to this ExecutionContext,
        the `statement` and `parameters` datamembers must be
        initialized after this statement is complete.
        '''
        raise NotImplementedError()

    
    def get_out_parameter_values(self = None, out_param_names = None):
        """Return a sequence of OUT parameter values from a cursor.

        For dialects that support OUT parameters, this method will be called
        when there is a :class:`.SQLCompiler` object which has the
        :attr:`.SQLCompiler.has_out_parameters` flag set.  This flag in turn
        will be set to True if the statement itself has :class:`.BindParameter`
        objects that have the ``.isoutparam`` flag set which are consumed by
        the :meth:`.SQLCompiler.visit_bindparam` method.  If the dialect
        compiler produces :class:`.BindParameter` objects with ``.isoutparam``
        set which are not handled by :meth:`.SQLCompiler.visit_bindparam`, it
        should set this flag explicitly.

        The list of names that were rendered for each bound parameter
        is passed to the method.  The method should then return a sequence of
        values corresponding to the list of parameter objects. Unlike in
        previous SQLAlchemy versions, the values can be the **raw values** from
        the DBAPI; the execution context will apply the appropriate type
        handler based on what's present in self.compiled.binds and update the
        values.  The processed dictionary will then be made available via the
        ``.out_parameters`` collection on the result object.  Note that
        SQLAlchemy 1.4 has multiple kinds of result object as part of the 2.0
        transition.

        .. versionadded:: 1.4 - added
           :meth:`.ExecutionContext.get_out_parameter_values`, which is invoked
           automatically by the :class:`.DefaultExecutionContext` when there
           are :class:`.BindParameter` objects with the ``.isoutparam`` flag
           set.  This replaces the practice of setting out parameters within
           the now-removed ``get_result_proxy()`` method.

        """
        raise NotImplementedError()

    
    def post_exec(self = None):
        '''Called after the execution of a compiled statement.

        If a compiled statement was passed to this ExecutionContext,
        the `last_insert_ids`, `last_inserted_params`, etc.
        datamembers should be available after this method completes.
        '''
        raise NotImplementedError()

    
    def handle_dbapi_exception(self = None, e = None):
        '''Receive a DBAPI exception which occurred upon execute, result
        fetch, etc.'''
        raise NotImplementedError()

    
    def lastrow_has_defaults(self = None):
        '''Return True if the last INSERT or UPDATE row contained
        inlined or database-side defaults.
        '''
        raise NotImplementedError()

    
    def get_rowcount(self = None):
        '''Return the DBAPI ``cursor.rowcount`` value, or in some
        cases an interpreted value.

        See :attr:`_engine.CursorResult.rowcount` for details on this.

        '''
        raise NotImplementedError()

    
    def fetchall_for_returning(self = None, cursor = None):
        '''For a RETURNING result, deliver cursor.fetchall() from the
        DBAPI cursor.

        This is a dialect-specific hook for dialects that have special
        considerations when calling upon the rows delivered for a
        "RETURNING" statement.   Default implementation is
        ``cursor.fetchall()``.

        This hook is currently used only by the :term:`insertmanyvalues`
        feature.   Dialects that don\'t set ``use_insertmanyvalues=True``
        don\'t need to consider this hook.

        .. versionadded:: 2.0.10

        '''
        raise NotImplementedError()



class ConnectionEventsTarget(EventTarget):
    dispatch: 'dispatcher[ConnectionEventsTarget]' = 'An object which can accept events from :class:`.ConnectionEvents`.\n\n    Includes :class:`_engine.Connection` and :class:`_engine.Engine`.\n\n    .. versionadded:: 2.0\n\n    '

Connectable = ConnectionEventsTarget

class ExceptionContext:
    '''Encapsulate information about an error condition in progress.

    This object exists solely to be passed to the
    :meth:`_events.DialectEvents.handle_error` event,
    supporting an interface that
    can be extended without backwards-incompatibility.


    '''
    is_pre_ping: 'bool' = ()


class AdaptedConnection:
    '''Interface of an adapted connection object to support the DBAPI protocol.

    Used by asyncio dialects to provide a sync-style pep-249 facade on top
    of the asyncio connection/cursor API provided by the driver.

    .. versionadded:: 1.4.24

    '''
    _connection: 'AsyncIODBAPIConnection' = ('_connection',)
    driver_connection = (lambda self = None: self._connection)()
    
    def run_async(self = None, fn = None):
        '''Run the awaitable returned by the given function, which is passed
        the raw asyncio driver connection.

        This is used to invoke awaitable-only methods on the driver connection
        within the context of a "synchronous" method, like a connection
        pool event handler.

        E.g.::

            engine = create_async_engine(...)


            @event.listens_for(engine.sync_engine, "connect")
            def register_custom_types(
                dbapi_connection,  # ...
            ):
                dbapi_connection.run_async(
                    lambda connection: connection.set_type_codec(
                        "MyCustomType", encoder, decoder, ...
                    )
                )

        .. versionadded:: 1.4.30

        .. seealso::

            :ref:`asyncio_events_run_async`

        '''
        return await_only(fn(self._connection))

    
    def __repr__(self = None):
        return '<AdaptedConnection %s>' % self._connection
