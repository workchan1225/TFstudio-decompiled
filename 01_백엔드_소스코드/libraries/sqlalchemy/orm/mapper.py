# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mapper.pyc (Python 3.11)

'''Logic to map Python classes to and from selectables.

Defines the :class:`~sqlalchemy.orm.mapper.Mapper` class, the central
configurational unit which associates a class with a database table.

This is a semi-private module; the main configurational API of the ORM is
available in :class:`~sqlalchemy.orm.`.

'''
from __future__ import annotations
from collections import deque
from functools import reduce
from itertools import chain
import sys
import threading
from typing import Any
from typing import Callable
from typing import cast
from typing import Collection
from typing import Deque
from typing import Dict
from typing import FrozenSet
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import weakref
from  import attributes
from  import exc as orm_exc
from  import instrumentation
from  import loading
from  import properties
from  import util as orm_util
from _typing import _O
from base import _class_to_mapper
from base import _parse_mapper_argument
from base import _state_mapper
from base import PassiveFlag
from base import state_str
from interfaces import _MappedAttribute
from interfaces import EXT_SKIP
from interfaces import InspectionAttr
from interfaces import MapperProperty
from interfaces import ORMEntityColumnsClauseRole
from interfaces import ORMFromClauseRole
from interfaces import StrategizedProperty
from path_registry import PathRegistry
from  import event
from  import exc as sa_exc
from  import inspection
from  import log
from  import schema
from  import sql
from  import util
from event import dispatcher
from event import EventTarget
from sql import base as sql_base
from sql import coercions
from sql import expression
from sql import operators
from sql import roles
from sql import TableClause
from sql import util as sql_util
from sql import visitors
from sql.cache_key import MemoizedHasCacheKey
from sql.elements import KeyedColumnElement
from sql.schema import Column
from sql.schema import Table
from sql.selectable import LABEL_STYLE_TABLENAME_PLUS_COL
from util import HasMemoized
from util import HasMemoized_ro_memoized_attribute
from util.typing import Literal
if TYPE_CHECKING:
    from _typing import _IdentityKeyType
    from _typing import _InstanceDict
    from _typing import _ORMColumnExprArgument
    from _typing import _RegistryType
    from decl_api import registry
    from dependency import DependencyProcessor
    from descriptor_props import CompositeProperty
    from descriptor_props import SynonymProperty
    from events import MapperEvents
    from instrumentation import ClassManager
    from path_registry import CachingEntityRegistry
    from properties import ColumnProperty
    from relationships import RelationshipProperty
    from state import InstanceState
    from util import ORMAdapter
    from engine import Row
    from engine import RowMapping
    from sql._typing import _ColumnExpressionArgument
    from sql._typing import _EquivalentColumnMap
    from sql.base import ReadOnlyColumnCollection
    from sql.elements import ColumnClause
    from sql.elements import ColumnElement
    from sql.selectable import FromClause
    from util import OrderedSet
_T = TypeVar('_T', bound = Any)
_MP = TypeVar('_MP', bound = 'MapperProperty[Any]')
_Fn = TypeVar('_Fn', bound = 'Callable[..., Any]')
_WithPolymorphicArg = Union[(Literal['*'], Tuple[(Union[(Literal['*'], Sequence[Union[('Mapper[Any]', Type[Any])]])], Optional['FromClause'])], Sequence[Union[('Mapper[Any]', Type[Any])]])]
_mapper_registries: 'weakref.WeakKeyDictionary[_RegistryType, bool]' = weakref.WeakKeyDictionary()

def _all_registries():
    _CONFIGURE_MUTEX
    None(None, None)
    return 
    with None:
        if not None, set(_mapper_registries):
            pass


def _unconfigured_mappers():
    pass
# WARNING: Decompyle incomplete

_already_compiling = False
NO_ATTRIBUTE = util.symbol('NO_ATTRIBUTE')
_CONFIGURE_MUTEX = threading.RLock()

def Mapper():
    '''Mapper'''
    dispatch: 'dispatcher[Mapper[_O]]' = 'Defines an association between a Python class and a database table or\n    other relational structure, so that ORM operations against the class may\n    proceed.\n\n    The :class:`_orm.Mapper` object is instantiated using mapping methods\n    present on the :class:`_orm.registry` object.  For information\n    about instantiating new :class:`_orm.Mapper` objects, see\n    :ref:`orm_mapping_classes_toplevel`.\n\n    '
    _dispose_called = False
    _configure_failed: 'Any' = False
    _ready_for_configure = False
    __init__ = (lambda self, class_, local_table, properties, primary_key, non_primary, inherits, inherit_condition, inherit_foreign_keys, always_refresh, version_id_col, version_id_generator, polymorphic_on, _polymorphic_map, polymorphic_identity, concrete, with_polymorphic, polymorphic_abstract, polymorphic_load, allow_partial_pks, batch, column_prefix, include_properties, exclude_properties, passive_updates, passive_deletes = None, confirm_deleted_rows = None, eager_defaults = util.deprecated_params(non_primary = ('1.3', 'The :paramref:`.mapper.non_primary` parameter is deprecated, and will be removed in a future release.  The functionality of non primary mappers is now better suited using the :class:`.AliasedClass` construct, which can also be used as the target of a :func:`_orm.relationship` in 1.3.')), legacy_is_orphan = (None, None, None, False, None, None, None, False, None, None, None, None, None, False, None, False, None, True, True, None, None, None, True, False, True, 'auto', False, 100), _compiled_cache_size = ('class_', 'Type[_O]', 'local_table', 'Optional[FromClause]', 'properties', 'Optional[Mapping[str, MapperProperty[Any]]]', 'primary_key', 'Optional[Iterable[_ORMColumnExprArgument[Any]]]', 'non_primary', 'bool', 'inherits', 'Optional[Union[Mapper[Any], Type[Any]]]', 'inherit_condition', 'Optional[_ColumnExpressionArgument[bool]]', 'inherit_foreign_keys', 'Optional[Sequence[_ORMColumnExprArgument[Any]]]', 'always_refresh', 'bool', 'version_id_col', 'Optional[_ORMColumnExprArgument[Any]]', 'version_id_generator', 'Optional[Union[Literal[False], Callable[[Any], Any]]]', 'polymorphic_on', 'Optional[Union[_ORMColumnExprArgument[Any], str, MapperProperty[Any]]]', '_polymorphic_map', 'Optional[Dict[Any, Mapper[Any]]]', 'polymorphic_identity', 'Optional[Any]', 'concrete', 'bool', 'with_polymorphic', 'Optional[_WithPolymorphicArg]', 'polymorphic_abstract', 'bool', 'polymorphic_load', "Optional[Literal['selectin', 'inline']]", 'allow_partial_pks', 'bool', 'batch', 'bool', 'column_prefix', 'Optional[str]', 'include_properties', 'Optional[Sequence[str]]', 'exclude_properties', 'Optional[Sequence[str]]', 'passive_updates', 'bool', 'passive_deletes', 'bool', 'confirm_deleted_rows', 'bool', 'eager_defaults', "Literal[True, False, 'auto']", 'legacy_is_orphan', 'bool', '_compiled_cache_size', 'int'): self.class_ = util.assert_arg_type(class_, type, 'class_')self._sort_key = f'''{self.class_.__module__!s}.{self.class_.__name__!s}'''self._primary_key_argument = util.to_list(primary_key)self.non_primary = non_primaryself.always_refresh = always_refreshif isinstance(version_id_col, MapperProperty):
self.version_id_prop = version_id_colself.version_id_col = None# WARNING: Decompyle incomplete
)()
    
    def _prefer_eager_defaults(self, dialect, table):
