# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: properties.pyc (Python 3.11)

'''MapperProperty implementations.

This is a private module which defines the behavior of individual ORM-
mapped attributes.

'''
from __future__ import annotations
from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import attributes
from  import exc as orm_exc
from  import strategy_options
from base import _DeclarativeMapped
from base import class_mapper
from descriptor_props import CompositeProperty
from descriptor_props import ConcreteInheritedProperty
from descriptor_props import SynonymProperty
from interfaces import _AttributeOptions
from interfaces import _DEFAULT_ATTRIBUTE_OPTIONS
from interfaces import _IntrospectsAnnotations
from interfaces import _MapsColumns
from interfaces import MapperProperty
from interfaces import PropComparator
from interfaces import StrategizedProperty
from relationships import RelationshipProperty
from util import de_stringify_annotation
from  import exc as sa_exc
from  import ForeignKey
from  import log
from  import util
from sql import coercions
from sql import roles
from sql.base import _NoArg
from sql.schema import Column
from sql.schema import SchemaConst
from sql.type_api import TypeEngine
from util.typing import de_optionalize_union_types
from util.typing import get_args
from util.typing import includes_none
from util.typing import is_a_type
from util.typing import is_fwd_ref
from util.typing import is_pep593
from util.typing import is_pep695
from util.typing import Self
if TYPE_CHECKING:
    from _typing import _IdentityKeyType
    from _typing import _InstanceDict
    from _typing import _ORMColumnExprArgument
    from _typing import _RegistryType
    from base import Mapped
    from decl_base import _ClassScanMapperConfig
    from mapper import Mapper
    from session import Session
    from state import _InstallLoaderCallableProto
    from state import InstanceState
    from sql._typing import _InfoType
    from sql.elements import ColumnElement
    from sql.elements import NamedColumn
    from sql.operators import OperatorType
    from util.typing import _AnnotationScanType
    from util.typing import RODescriptorReference
_T = TypeVar('_T', bound = Any)
_PT = TypeVar('_PT', bound = Any)
_NC = TypeVar('_NC', bound = 'NamedColumn[Any]')
__all__ = [
    'ColumnProperty',
    'CompositeProperty',
    'ConcreteInheritedProperty',
    'RelationshipProperty',
    'SynonymProperty']

def ColumnProperty():
    '''ColumnProperty'''
    pass
# WARNING: Decompyle incomplete

ColumnProperty = <NODE:27>(ColumnProperty, 'ColumnProperty', _MapsColumns[_T], StrategizedProperty[_T], _IntrospectsAnnotations, log.Identified)()

def MappedSQLExpression():
    '''MappedSQLExpression'''
    __doc__ = 'Declarative front-end for the :class:`.ColumnProperty` class.\n\n    Public constructor is the :func:`_orm.column_property` function.\n\n    .. versionchanged:: 2.0 Added :class:`_orm.MappedSQLExpression` as\n       a Declarative compatible subclass for :class:`_orm.ColumnProperty`.\n\n    .. seealso::\n\n        :class:`.MappedColumn`\n\n    '
    inherit_cache = True

MappedSQLExpression = <NODE:27>(MappedSQLExpression, 'MappedSQLExpression', ColumnProperty[_T], _DeclarativeMapped[_T])

def MappedColumn():
    '''MappedColumn'''
    __doc__ = 'Maps a single :class:`_schema.Column` on a class.\n\n    :class:`_orm.MappedColumn` is a specialization of the\n    :class:`_orm.ColumnProperty` class and is oriented towards declarative\n    configuration.\n\n    To construct :class:`_orm.MappedColumn` objects, use the\n    :func:`_orm.mapped_column` constructor function.\n\n    .. versionadded:: 2.0\n\n\n    '
    _attribute_options: '_AttributeOptions' = ('column', '_creation_order', '_sort_order', 'foreign_keys', '_has_nullable', '_has_insert_default', 'deferred', 'deferred_group', 'deferred_raiseload', 'active_history', '_attribute_options', '_has_dataclass_arguments', '_use_existing_column')
    
    def __init__(self = None, *arg, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def _copy(self = None, **kw):
        new = self.__class__.__new__(self.__class__)
    # WARNING: Decompyle incomplete

    name = (lambda self = None: self.column.name)()
    mapper_property_to_assign = (lambda self = None:
