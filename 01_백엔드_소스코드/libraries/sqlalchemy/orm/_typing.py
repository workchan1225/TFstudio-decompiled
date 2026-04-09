# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _typing.pyc (Python 3.11)

from __future__ import annotations
import operator
from typing import Any
from typing import Dict
from typing import Mapping
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from engine.interfaces import _CoreKnownExecutionOptions
from sql import roles
from sql._orm_types import DMLStrategyArgument
from sql._orm_types import SynchronizeSessionArgument
from sql._typing import _HasClauseElement
from sql.elements import ColumnElement
from util.typing import Protocol
from util.typing import TypeGuard
if TYPE_CHECKING:
    from attributes import AttributeImpl
    from attributes import CollectionAttributeImpl
    from attributes import HasCollectionAdapter
    from attributes import QueryableAttribute
    from base import PassiveFlag
    from decl_api import registry as _registry_type
    from interfaces import InspectionAttr
    from interfaces import MapperProperty
    from interfaces import ORMOption
    from interfaces import UserDefinedOption
    from mapper import Mapper
    from relationships import RelationshipProperty
    from state import InstanceState
    from util import AliasedClass
    from util import AliasedInsp
    from sql._typing import _CE
    from sql.base import ExecutableOption
_T = TypeVar('_T', bound = Any)
_T_co = TypeVar('_T_co', bound = Any, covariant = True)
_O = TypeVar('_O', bound = object)
if TYPE_CHECKING:
    _RegistryType = _registry_type
_InternalEntityType = Union[('Mapper[_T]', 'AliasedInsp[_T]')]
_ExternalEntityType = Union[(Type[_T], 'AliasedClass[_T]')]
_EntityType = Union[(Type[_T], 'AliasedClass[_T]', 'Mapper[_T]', 'AliasedInsp[_T]')]
_ClassDict = Mapping[(str, Any)]
_InstanceDict = Dict[(str, Any)]
_IdentityKeyType = Tuple[(Type[_T], Tuple[(Any, ...)], Optional[Any])]
_ORMColumnExprArgument = Union[(ColumnElement[_T], _HasClauseElement[_T], roles.ExpressionElementRole[_T])]
_ORMCOLEXPR = TypeVar('_ORMCOLEXPR', bound = ColumnElement[Any])

def _OrmKnownExecutionOptions():
    '''_OrmKnownExecutionOptions'''
    render_nulls: 'bool' = '_OrmKnownExecutionOptions'

_OrmKnownExecutionOptions = <NODE:27>(_OrmKnownExecutionOptions, '_OrmKnownExecutionOptions', _CoreKnownExecutionOptions, total = False)
OrmExecuteOptionsParameter = Union[(_OrmKnownExecutionOptions, Mapping[(str, Any)])]

class _ORMAdapterProto(Protocol):
    '''protocol for the :class:`.AliasedInsp._orm_adapt_element` method
    which is a synonym for :class:`.AliasedInsp._adapt_element`.


    '''
    
    def __call__(self = None, obj = None, key = None):
        pass



class _LoaderCallable(Protocol):
    
    def __call__(self = None, state = None, passive = None):
        pass



def is_orm_option(opt = None):
    return not (opt._is_core)


def is_user_defined_option(opt = None):
