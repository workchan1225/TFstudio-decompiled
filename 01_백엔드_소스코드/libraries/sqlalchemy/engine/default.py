# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: default.pyc (Python 3.11)

'''Default implementations of per-dialect sqlalchemy.engine classes.

These are semi-private implementation classes which are only of importance
to database dialect authors; dialects will usually use the classes here
as the base class for their own corresponding classes.

'''
from __future__ import annotations
import functools
import operator
import random
import re
from time import perf_counter
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import List
from typing import Mapping
from typing import MutableMapping
from typing import MutableSequence
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import Union
import weakref
from  import characteristics
from  import cursor as _cursor
from  import interfaces
from base import Connection
from interfaces import CacheStats
from interfaces import DBAPICursor
from interfaces import Dialect
from interfaces import ExecuteStyle
from interfaces import ExecutionContext
from reflection import ObjectKind
from reflection import ObjectScope
from  import event
from  import exc
from  import pool
from  import util
from sql import compiler
from sql import dml
from sql import expression
from sql import type_api
from sql import util as sql_util
from sql._typing import is_tuple_type
from sql.base import _NoArg
from sql.compiler import DDLCompiler
from sql.compiler import InsertmanyvaluesSentinelOpts
from sql.compiler import SQLCompiler
from sql.elements import quoted_name
from util.typing import Final
from util.typing import Literal
if typing.TYPE_CHECKING:
    from types import ModuleType
    from base import Engine
    from cursor import ResultFetchStrategy
    from interfaces import _CoreMultiExecuteParams
    from interfaces import _CoreSingleExecuteParams
    from interfaces import _DBAPICursorDescription
    from interfaces import _DBAPIMultiExecuteParams
    from interfaces import _DBAPISingleExecuteParams
    from interfaces import _ExecuteOptions
    from interfaces import _MutableCoreSingleExecuteParams
    from interfaces import _ParamStyle
    from interfaces import ConnectArgsType
    from interfaces import DBAPIConnection
    from interfaces import DBAPIModule
    from interfaces import IsolationLevel
    from row import Row
    from url import URL
    from event import _ListenerFnType
    from pool import Pool
    from pool import PoolProxiedConnection
    from sql import Executable
    from sql.compiler import Compiled
    from sql.compiler import Linting
    from sql.compiler import ResultColumnsEntry
    from sql.dml import DMLState
    from sql.dml import UpdateBase
    from sql.elements import BindParameter
    from sql.schema import Column
    from sql.type_api import _BindProcessorType
    from sql.type_api import _ResultProcessorType
    from sql.type_api import TypeEngine
SERVER_SIDE_CURSOR_RE = re.compile('\\s*SELECT', re.I | re.UNICODE)
(CACHE_HIT, CACHE_MISS, CACHING_DISABLED, NO_CACHE_KEY, NO_DIALECT_SUPPORT) = list(CacheStats)

class DefaultDialect(Dialect):
    '''Default implementation of Dialect'''
    statement_compiler = compiler.SQLCompiler
    ddl_compiler = compiler.DDLCompiler
    type_compiler_cls = compiler.GenericTypeCompiler
    preparer = compiler.IdentifierPreparer
    supports_alter = True
    supports_comments = False
    supports_constraint_comments = False
    inline_comments = False
    supports_statement_cache = True
    div_is_floordiv = True
    bind_typing = interfaces.BindTyping.NONE
    include_set_input_sizes: 'Optional[Set[Any]]' = None
    exclude_set_input_sizes: 'Optional[Set[Any]]' = None
    default_sequence_base = 1
    execute_sequence_format = tuple
    supports_schemas = True
    supports_views = True
    supports_sequences = False
    sequences_optional = False
    preexecute_autoincrement_sequences = False
    supports_identity_columns = False
    postfetch_lastrowid = True
    favor_returning_over_lastrowid = False
    insert_null_pk_still_autoincrements = False
    update_returning = False
    delete_returning = False
    update_returning_multifrom = False
    delete_returning_multifrom = False
    insert_returning = False
    cte_follows_insert = False
    supports_native_enum = False
    supports_native_boolean = False
    supports_native_uuid = False
    returns_native_bytes = False
    non_native_boolean_check_constraint = True
    supports_simple_order_by_label = True
    tuple_in_values = False
    connection_characteristics = util.immutabledict({
        'isolation_level': characteristics.IsolationLevelCharacteristic(),
        'logging_token': characteristics.LoggingTokenCharacteristic() })
    engine_config_types: 'Mapping[str, Any]' = util.immutabledict({
        'pool_timeout': util.asint,
        'echo': util.bool_or_str('debug'),
        'echo_pool': util.bool_or_str('debug'),
        'pool_recycle': util.asint,
        'pool_size': util.asint,
        'max_overflow': util.asint,
        'future': util.asbool })
    supports_native_decimal = False
    name = 'default'
    max_identifier_length = 9999
    _user_defined_max_identifier_length: 'Optional[int]' = None
    isolation_level: 'Optional[str]' = None
    max_index_name_length: 'Optional[int]' = None
    max_constraint_name_length: 'Optional[int]' = None
    supports_sane_rowcount = True
    supports_sane_multi_rowcount = True
    colspecs: 'MutableMapping[Type[TypeEngine[Any]], Type[TypeEngine[Any]]]' = { }
    default_paramstyle = 'named'
    supports_default_values = False
    supports_default_metavalue = False
    default_metavalue_token = 'DEFAULT'
    supports_empty_insert = True
    supports_multivalues_insert = False
    use_insertmanyvalues: 'bool' = False
    use_insertmanyvalues_wo_returning: 'bool' = False
    insertmanyvalues_implicit_sentinel: 'InsertmanyvaluesSentinelOpts' = InsertmanyvaluesSentinelOpts.NOT_SUPPORTED
    insertmanyvalues_page_size: 'int' = 1000
    insertmanyvalues_max_parameters = 32700
    supports_is_distinct_from = True
    supports_server_side_cursors = False
    server_side_cursors = False
    supports_for_update_of = False
    server_version_info = None
    default_schema_name: 'Optional[str]' = None
    requires_name_normalize = False
    is_async = False
    has_terminate = False
    _legacy_binary_type_literal_encoding = 'utf-8'
    __init__ = (lambda self, paramstyle, isolation_level, dbapi, implicit_returning, supports_native_boolean, max_identifier_length, label_length, insertmanyvalues_page_size = None, use_insertmanyvalues = None, compiler_linting = util.deprecated_params(empty_in_strategy = ('1.4', 'The :paramref:`_sa.create_engine.empty_in_strategy` keyword is deprecated, and no longer has any effect.  All IN expressions are now rendered using the "expanding parameter" strategy which renders a set of boundexpressions, or an "empty set" SELECT, at statement executiontime.'), server_side_cursors = ('1.4', 'The :paramref:`_sa.create_engine.server_side_cursors` parameter is deprecated and will be removed in a future release.  Please use the :paramref:`_engine.Connection.execution_options.stream_results` parameter.')), server_side_cursors = (None, None, None, True, None, None, None, _NoArg.NO_ARG, None, int(compiler.NO_LINTING), False, False), skip_autocommit_rollback = ('paramstyle', 'Optional[_ParamStyle]', 'isolation_level', 'Optional[IsolationLevel]', 'dbapi', 'Optional[ModuleType]', 'implicit_returning', 'Literal[True]', 'supports_native_boolean', 'Optional[bool]', 'max_identifier_length', 'Optional[int]', 'label_length', 'Optional[int]', 'insertmanyvalues_page_size', 'Union[_NoArg, int]', 'use_insertmanyvalues', 'Optional[bool]', 'compiler_linting', 'Linting', 'server_side_cursors', 'bool', 'skip_autocommit_rollback', 'bool', 'kwargs', 'Any'): if server_side_cursors:
if not self.supports_server_side_cursors:
raise exc.ArgumentError('Dialect %s does not support server side cursors' % self)self.server_side_cursors = Trueif getattr(self, 'use_setinputsizes', False):
util.warn_deprecated('The dialect-level use_setinputsizes attribute is deprecated.  Please use bind_typing = BindTyping.SETINPUTSIZES', '2.0')self.bind_typing = interfaces.BindTyping.SETINPUTSIZESself.positional = Falseself._ischema = Noneself.dbapi = dbapiself.skip_autocommit_rollback = skip_autocommit_rollback# WARNING: Decompyle incomplete
)()
    full_returning = (lambda self:
