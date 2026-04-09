# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compiler.pyc (Python 3.11)

__doc__ = 'Base SQL and DDL compiler implementations.\n\nClasses provided include:\n\n:class:`.compiler.SQLCompiler` - renders SQL\nstrings\n\n:class:`.compiler.DDLCompiler` - renders DDL\n(data definition language) strings\n\n:class:`.compiler.GenericTypeCompiler` - renders\ntype specification strings.\n\nTo generate user-defined SQL strings, see\n:doc:`/ext/compiler`.\n\n'
from __future__ import annotations
import collections
from collections.abc import abc as collections_abc
import contextlib
from enum import IntEnum
import functools
import itertools
import operator
import re
from time import perf_counter
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import ClassVar
from typing import Dict
from typing import FrozenSet
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import MutableMapping
from typing import NamedTuple
from typing import NoReturn
from typing import Optional
from typing import Pattern
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import Union
from  import base
from  import coercions
from  import crud
from  import elements
from  import functions
from  import operators
from  import roles
from  import schema
from  import selectable
from  import sqltypes
from  import util as sql_util
from _typing import is_column_element
from _typing import is_dml
from base import _de_clone
from base import _from_objects
from base import _NONE_NAME
from base import _SentinelDefaultCharacterization
from base import NO_ARG
from elements import quoted_name
from sqltypes import TupleType
from visitors import prefix_anon_map
from  import exc
from  import util
from util import FastIntFlag
from util.typing import Literal
from util.typing import Protocol
from util.typing import Self
from util.typing import TypedDict
if typing.TYPE_CHECKING:
    from annotation import _AnnotationDict
    from base import _AmbiguousTableNameMap
    from base import CompileState
    from base import Executable
    from cache_key import CacheKey
    from ddl import ExecutableDDLElement
    from dml import Insert
    from dml import Update
    from dml import UpdateBase
    from dml import UpdateDMLState
    from dml import ValuesBase
    from elements import _truncated_label
    from elements import BinaryExpression
    from elements import BindParameter
    from elements import ClauseElement
    from elements import ColumnClause
    from elements import ColumnElement
    from elements import False_
    from elements import Label
    from elements import Null
    from elements import True_
    from functions import Function
    from schema import Column
    from schema import Constraint
    from schema import ForeignKeyConstraint
    from schema import Index
    from schema import PrimaryKeyConstraint
    from schema import Table
    from schema import UniqueConstraint
    from selectable import _ColumnsClauseElement
    from selectable import AliasedReturnsRows
    from selectable import CompoundSelectState
    from selectable import CTE
    from selectable import FromClause
    from selectable import NamedFromClause
    from selectable import ReturnsRows
    from selectable import Select
    from selectable import SelectState
    from type_api import _BindProcessorType
    from type_api import TypeDecorator
    from type_api import TypeEngine
    from type_api import UserDefinedType
    from visitors import Visitable
    from engine.cursor import CursorResultMetaData
    from engine.interfaces import _CoreSingleExecuteParams
    from engine.interfaces import _DBAPIAnyExecuteParams
    from engine.interfaces import _DBAPIMultiExecuteParams
    from engine.interfaces import _DBAPISingleExecuteParams
    from engine.interfaces import _ExecuteOptions
    from engine.interfaces import _GenericSetInputSizesType
    from engine.interfaces import _MutableCoreSingleExecuteParams
    from engine.interfaces import Dialect
    from engine.interfaces import SchemaTranslateMapType
_FromHintsType = Dict[('FromClause', str)]
RESERVED_WORDS = {
    'as',
    'do',
    'in',
    'is',
    'on',
    'or',
    'to',
    'all',
    'and',
    'any',
    'asc',
    'end',
    'for',
    'new',
    'not',
    'off',
    'old',
    'set',
    'both',
    'case',
    'cast',
    'desc',
    'else',
    'from',
    'full',
    'into',
    'join',
    'left',
    'like',
    'null',
    'only',
    'some',
    'then',
    'true',
    'user',
    'when',
    'array',
    'check',
    'cross',
    'false',
    'grant',
    'group',
    'ilike',
    'inner',
    'limit',
    'order',
    'outer',
    'right',
    'table',
    'union',
    'using',
    'where',
    'binary',
    'column',
    'create',
    'except',
    'freeze',
    'having',
    'isnull',
    'offset',
    'select',
    'unique',
    'analyse',
    'analyze',
    'between',
    'collate',
    'default',
    'foreign',
    'leading',
    'natural',
    'notnull',
    'placing',
    'primary',
    'similar',
    'verbose',
    'distinct',
    'overlaps',
    'trailing',
    'initially',
    'intersect',
    'localtime',
    'symmetric',
    'asymmetric',
    'constraint',
    'deferrable',
    'references',
    'current_date',
    'current_role',
    'current_time',
    'current_user',
    'session_user',
    'authorization',
    'localtimestamp',
    'current_timestamp'}
LEGAL_CHARACTERS = re.compile('^[A-Z0-9_$]+$', re.I)
LEGAL_CHARACTERS_PLUS_SPACE = re.compile('^[A-Z0-9_ $]+$', re.I)
ILLEGAL_INITIAL_CHARACTERS = range(0, 10)().union([
    '$'])
FK_ON_DELETE = re.compile('^(?:RESTRICT|CASCADE|SET NULL|NO ACTION|SET DEFAULT)$', re.I)
FK_ON_UPDATE = re.compile('^(?:RESTRICT|CASCADE|SET NULL|NO ACTION|SET DEFAULT)$', re.I)
FK_INITIALLY = re.compile('^(?:DEFERRED|IMMEDIATE)$', re.I)
BIND_PARAMS = re.compile('(?<![:\\w\\$\\x5c]):([\\w\\$]+)(?![:\\w\\$])', re.UNICODE)
BIND_PARAMS_ESC = re.compile('\\x5c(:[\\w\\$]*)(?![:\\w\\$])', re.UNICODE)
_pyformat_template = '%%(%(name)s)s'
BIND_TEMPLATES = {
    'pyformat': _pyformat_template,
    'qmark': '?',
    'format': '%%s',
    'numeric': ':[_POSITION]',
    'numeric_dollar': '$[_POSITION]',
    'named': ':%(name)s' }
# WARNING: Decompyle incomplete
