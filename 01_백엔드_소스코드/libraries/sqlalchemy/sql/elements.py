# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: elements.pyc (Python 3.11)

'''Core SQL expression elements, including :class:`_expression.ClauseElement`,
:class:`_expression.ColumnElement`, and derived classes.

'''
from __future__ import annotations
from decimal import Decimal
from enum import Enum
import itertools
import operator
import re
import typing
from typing import AbstractSet
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import FrozenSet
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Tuple as typing_Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import coercions
from  import operators
from  import roles
from  import traversals
from  import type_api
from _typing import has_schema_attr
from _typing import is_named_from_clause
from _typing import is_quoted_name
from _typing import is_tuple_type
from annotation import Annotated
from annotation import SupportsWrappingAnnotations
from base import _clone
from base import _expand_cloned
from base import _generative
from base import _NoArg
from base import Executable
from base import Generative
from base import HasMemoized
from base import Immutable
from base import NO_ARG
from base import SingletonConstant
from cache_key import MemoizedHasCacheKey
from cache_key import NO_CACHE
from coercions import _document_text_coercion
from operators import ColumnOperators
from traversals import HasCopyInternals
from visitors import cloned_traverse
from visitors import ExternallyTraversible
from visitors import InternalTraversal
from visitors import traverse
from visitors import Visitable
from  import exc
from  import inspection
from  import util
from util import HasMemoized_ro_memoized_attribute
from util import TypingOnly
from util.typing import Literal
from util.typing import ParamSpec
from util.typing import Self
if typing.TYPE_CHECKING:
    from _typing import _ByArgument
    from _typing import _ColumnExpressionArgument
    from _typing import _ColumnExpressionOrStrLabelArgument
    from _typing import _HasDialect
    from _typing import _InfoType
    from _typing import _PropagateAttrsType
    from _typing import _TypeEngineArgument
    from base import _EntityNamespace
    from base import ColumnSet
    from cache_key import _CacheKeyTraversalType
    from cache_key import CacheKey
    from compiler import Compiled
    from compiler import SQLCompiler
    from functions import FunctionElement
    from operators import OperatorType
    from schema import Column
    from schema import DefaultGenerator
    from schema import FetchedValue
    from schema import ForeignKey
    from selectable import _SelectIterable
    from selectable import FromClause
    from selectable import NamedFromClause
    from selectable import TextualSelect
    from sqltypes import TupleType
    from type_api import TypeEngine
    from visitors import _CloneCallableType
    from visitors import _TraverseInternalsType
    from visitors import anon_map
    from engine import Connection
    from engine import Dialect
    from engine.interfaces import _CoreMultiExecuteParams
    from engine.interfaces import CacheStats
    from engine.interfaces import CompiledCacheType
    from engine.interfaces import CoreExecuteOptionsParameter
    from engine.interfaces import SchemaTranslateMapType
    from engine.result import Result
_NUMERIC = Union[(float, Decimal)]
_NUMBER = Union[(float, int, Decimal)]
_T = TypeVar('_T', bound = 'Any')
_T_co = TypeVar('_T_co', bound = Any, covariant = True)
_OPT = TypeVar('_OPT', bound = 'Any')
_NT = TypeVar('_NT', bound = '_NUMERIC')
_NMT = TypeVar('_NMT', bound = '_NUMBER')
literal = (lambda value = None, type_ = None, literal_execute = overload: pass)()
literal = (lambda value = None, type_ = None, literal_execute = overload: pass)()
literal = (lambda value = None, type_ = None, literal_execute = overload: pass)()

def literal(value = None, type_ = None, literal_execute = None):
    '''Return a literal clause, bound to a bind parameter.

    Literal clauses are created automatically when non-
    :class:`_expression.ClauseElement` objects (such as strings, ints, dates,
    etc.) are
    used in a comparison operation with a :class:`_expression.ColumnElement`
    subclass,
    such as a :class:`~sqlalchemy.schema.Column` object.  Use this function
    to force the generation of a literal clause, which will be created as a
    :class:`BindParameter` with a bound value.

    :param value: the value to be bound. Can be any Python object supported by
     the underlying DB-API, or is translatable via the given type argument.

    :param type\\_: an optional :class:`~sqlalchemy.types.TypeEngine` which will
     provide bind-parameter translation for this literal.

    :param literal_execute: optional bool, when True, the SQL engine will
     attempt to render the bound value directly in the SQL statement at
     execution time rather than providing as a parameter value.

     .. versionadded:: 2.0

    '''
    return coercions.expect(roles.LiteralValueRole, value, type_ = type_, literal_execute = literal_execute)


def literal_column(text = None, type_ = None):
    '''Produce a :class:`.ColumnClause` object that has the
    :paramref:`_expression.column.is_literal` flag set to True.

    :func:`_expression.literal_column` is similar to
    :func:`_expression.column`, except that
    it is more often used as a "standalone" column expression that renders
    exactly as stated; while :func:`_expression.column`
    stores a string name that
    will be assumed to be part of a table and may be quoted as such,
    :func:`_expression.literal_column` can be that,
    or any other arbitrary column-oriented
    expression.

    :param text: the text of the expression; can be any SQL expression.
      Quoting rules will not be applied. To specify a column-name expression
      which should be subject to quoting rules, use the :func:`column`
      function.

    :param type\\_: an optional :class:`~sqlalchemy.types.TypeEngine`
      object which will
      provide result-set translation and additional expression semantics for
      this column. If left as ``None`` the type will be :class:`.NullType`.

    .. seealso::

        :func:`_expression.column`

        :func:`_expression.text`

        :ref:`tutorial_select_arbitrary_text`

    '''
    return ColumnClause(text, type_ = type_, is_literal = True)


class CompilerElement(Visitable):
    '''base class for SQL elements that can be compiled to produce a
    SQL string.

    .. versionadded:: 2.0

    '''
    __slots__ = ()
    __visit_name__ = 'compiler_element'
    supports_execution = False
    stringify_dialect = 'default'
    compile = (lambda self = None, bind = util.preload_module('sqlalchemy.engine.default'), dialect = util.preload_module('sqlalchemy.engine.url'): pass# WARNING: Decompyle incomplete
)()()
    
    def _default_dialect(self):
        default = util.preloaded.engine_default
        return default.StrCompileDialect()

    
    def _compiler(self = None, dialect = None, **kw):
        '''Return a compiler appropriate for this ClauseElement, given a
        Dialect.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        return str(self.compile())


ClauseElement = <NODE:12>()

class DQLDMLClauseElement(ClauseElement):
    '''represents a :class:`.ClauseElement` that compiles to a DQL or DML
    expression, not DDL.

    .. versionadded:: 2.0

    '''
    if typing.TYPE_CHECKING:
        
        def _compiler(self = None, dialect = None, **kw):
            '''Return a compiler appropriate for this ClauseElement, given a
            Dialect.'''
            pass

        
        def compile(self = None, bind = None, dialect = None, **kw):
            pass

        return None


class CompilerColumnElement(CompilerElement, roles.ColumnsClauseRole, roles.DDLConstraintColumnRole, roles.DMLColumnRole):
    '''A compiler-only column element used for ad-hoc string compilations.

    .. versionadded:: 2.0

    '''
    __slots__ = ()
    _propagate_attrs = util.EMPTY_DICT
    _is_collection_aggregate = False


def SQLCoreOperations():
    '''SQLCoreOperations'''
    __slots__ = ()
    if typing.TYPE_CHECKING:
        _propagate_attrs = (lambda self = None: pass)()
        
        def operate(self = None, op = None, *other, **kwargs):
            pass

        
        def reverse_operate(self = None, op = None, other = None, **kwargs):
            pass

        op = (lambda self = None, opstring = None, precedence = None, is_comparison = overload, *, return_type, python_impl,
