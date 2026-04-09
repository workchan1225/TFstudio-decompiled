# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _typing.pyc (Python 3.11)

from __future__ import annotations
import operator
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import roles
from  import exc
from  import util
from inspection import Inspectable
from util.typing import Literal
from util.typing import Protocol
from util.typing import TypeAlias
if TYPE_CHECKING:
    from datetime import date
    from datetime import datetime
    from datetime import time
    from datetime import timedelta
    from decimal import Decimal
    from uuid import UUID
    from base import Executable
    from compiler import Compiled
    from compiler import DDLCompiler
    from compiler import SQLCompiler
    from dml import UpdateBase
    from dml import ValuesBase
    from elements import ClauseElement
    from elements import ColumnElement
    from elements import KeyedColumnElement
    from elements import quoted_name
    from elements import SQLCoreOperations
    from elements import TextClause
    from lambdas import LambdaElement
    from roles import FromClauseRole
    from schema import Column
    from selectable import Alias
    from selectable import CompoundSelect
    from selectable import CTE
    from selectable import FromClause
    from selectable import Join
    from selectable import NamedFromClause
    from selectable import ReturnsRows
    from selectable import Select
    from selectable import Selectable
    from selectable import SelectBase
    from selectable import Subquery
    from selectable import TableClause
    from sqltypes import TableValueType
    from sqltypes import TupleType
    from type_api import TypeEngine
    from engine import Connection
    from engine import Dialect
    from engine import Engine
    from engine.mock import MockConnection
    from util.typing import TypeGuard
_T = TypeVar('_T', bound = Any)
_T_co = TypeVar('_T_co', bound = Any, covariant = True)
_CE = TypeVar('_CE', bound = 'ColumnElement[Any]')
_CLE = TypeVar('_CLE', bound = 'ClauseElement')

def _HasClauseElement():
    '''_HasClauseElement'''
    __doc__ = 'indicates a class that has a __clause_element__() method'
    
    def __clause_element__(self = None):
        pass


_HasClauseElement = <NODE:27>(_HasClauseElement, '_HasClauseElement', Protocol, Generic[_T_co])

class _CoreAdapterProto(Protocol):
    '''protocol for the ClauseAdapter/ColumnAdapter.traverse() method.'''
    
    def __call__(self = None, obj = None):
        pass



class _HasDialect(Protocol):
    '''protocol for Engine/Connection-like objects that have dialect
    attribute.
    '''
    dialect = (lambda self = None: pass)()

_NOT_ENTITY = TypeVar('_NOT_ENTITY', int, str, bool, 'datetime', 'date', 'time', 'timedelta', 'UUID', float, 'Decimal')
_StarOrOne = Literal[('*', 1)]
_MAYBE_ENTITY = TypeVar('_MAYBE_ENTITY', roles.ColumnsClauseRole, _StarOrOne, Type[Any], Inspectable[_HasClauseElement[Any]], _HasClauseElement[Any])
_TextCoercedExpressionArgument = Union[(str, 'TextClause', 'ColumnElement[_T]', _HasClauseElement[_T], roles.ExpressionElementRole[_T])]
_ColumnsClauseArgument = Union[(roles.TypedColumnsClauseRole[_T], roles.ColumnsClauseRole, 'SQLCoreOperations[_T]', _StarOrOne, Type[_T], Inspectable[_HasClauseElement[_T]], _HasClauseElement[_T])]
_TypedColumnClauseArgument = Union[(roles.TypedColumnsClauseRole[_T], 'SQLCoreOperations[_T]', Type[_T])]
_TP = TypeVar('_TP', bound = Tuple[(Any, ...)])
_T0 = TypeVar('_T0', bound = Any)
_T1 = TypeVar('_T1', bound = Any)
_T2 = TypeVar('_T2', bound = Any)
_T3 = TypeVar('_T3', bound = Any)
_T4 = TypeVar('_T4', bound = Any)
_T5 = TypeVar('_T5', bound = Any)
_T6 = TypeVar('_T6', bound = Any)
_T7 = TypeVar('_T7', bound = Any)
_T8 = TypeVar('_T8', bound = Any)
_T9 = TypeVar('_T9', bound = Any)
_ColumnExpressionArgument = Union[('ColumnElement[_T]', _HasClauseElement[_T], 'SQLCoreOperations[_T]', roles.ExpressionElementRole[_T], roles.TypedColumnsClauseRole[_T], Callable[([], 'ColumnElement[_T]')], 'LambdaElement')]
ColumnExpressionArgument: 'TypeAlias' = _ColumnExpressionArgument[_T]
_ColumnExpressionOrLiteralArgument = Union[(Any, _ColumnExpressionArgument[_T])]
_ColumnExpressionOrStrLabelArgument = Union[(str, _ColumnExpressionArgument[_T])]
_ByArgument = Union[(Iterable[_ColumnExpressionOrStrLabelArgument[Any]], _ColumnExpressionOrStrLabelArgument[Any])]
_InfoType = Dict[(Any, Any)]
_FromClauseArgument = Union[(roles.FromClauseRole, Type[Any], Inspectable[_HasClauseElement[Any]], _HasClauseElement[Any])]
_JoinTargetArgument = Union[(_FromClauseArgument, roles.JoinTargetRole)]
_OnClauseArgument = Union[(_ColumnExpressionArgument[Any], roles.OnClauseRole)]
_SelectStatementForCompoundArgument = Union[('Select[_TP]', 'CompoundSelect[_TP]', roles.CompoundElementRole)]
_DMLColumnArgument = Union[(str, _HasClauseElement[Any], roles.DMLColumnRole, 'SQLCoreOperations[Any]')]
_DMLKey = TypeVar('_DMLKey', bound = _DMLColumnArgument)
_DMLColumnKeyMapping = Mapping[(_DMLKey, Any)]
_DDLColumnArgument = Union[(str, 'Column[Any]', roles.DDLConstraintColumnRole)]
_DMLTableArgument = Union[('TableClause', 'Join', 'Alias', 'CTE', Type[Any], Inspectable[_HasClauseElement[Any]], _HasClauseElement[Any])]
_PropagateAttrsType = util.immutabledict[(str, Any)]
_TypeEngineArgument = Union[(Type['TypeEngine[_T]'], 'TypeEngine[_T]')]
_EquivalentColumnMap = Dict[('ColumnElement[Any]', Set['ColumnElement[Any]'])]
_LimitOffsetType = Union[(int, _ColumnExpressionArgument[int], None)]
_AutoIncrementType = Union[(bool, Literal[('auto', 'ignore_fk')])]
_CreateDropBind = Union[('Engine', 'Connection', 'MockConnection')]

def has_schema_attr(t = None):
    return hasattr(t, 'schema')


def is_quoted_name(s = None):
    return hasattr(s, 'quote')


def is_has_clause_element(s = None):
    return hasattr(s, '__clause_element__')


def is_insert_update(c = None):
