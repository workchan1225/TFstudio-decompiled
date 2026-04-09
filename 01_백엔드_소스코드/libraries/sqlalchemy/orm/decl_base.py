# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: decl_base.pyc (Python 3.11)

'''Internal implementation for declarative.'''
from __future__ import annotations
import collections
import dataclasses
import re
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Iterable
from typing import List
from typing import Mapping
from typing import NamedTuple
from typing import NoReturn
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import weakref
from  import attributes
from  import clsregistry
from  import exc as orm_exc
from  import instrumentation
from  import mapperlib
from _typing import _O
from _typing import attr_is_internal_proxy
from attributes import InstrumentedAttribute
from attributes import QueryableAttribute
from base import _is_mapped_class
from base import InspectionAttr
from descriptor_props import CompositeProperty
from descriptor_props import SynonymProperty
from interfaces import _AttributeOptions
from interfaces import _DCAttributeOptions
from interfaces import _IntrospectsAnnotations
from interfaces import _MappedAttribute
from interfaces import _MapsColumns
from interfaces import MapperProperty
from mapper import Mapper
from properties import ColumnProperty
from properties import MappedColumn
from util import _extract_mapped_subtype
from util import _is_mapped_annotation
from util import class_mapper
from util import de_stringify_annotation
from  import event
from  import exc
from  import util
from sql import expression
from sql.base import _NoArg
from sql.schema import Column
from sql.schema import Table
from util import topological
from util.typing import _AnnotationScanType
from util.typing import get_args
from util.typing import is_fwd_ref
from util.typing import is_literal
from util.typing import Protocol
from util.typing import TypedDict
if TYPE_CHECKING:
    from _typing import _ClassDict
    from _typing import _RegistryType
    from base import Mapped
    from decl_api import declared_attr
    from instrumentation import ClassManager
    from sql.elements import NamedColumn
    from sql.schema import MetaData
    from sql.selectable import FromClause
_T = TypeVar('_T', bound = Any)
_MapperKwArgs = Mapping[(str, Any)]
_TableArgsType = Union[(Tuple[(Any, ...)], Dict[(str, Any)])]

def MappedClassProtocol():
    '''MappedClassProtocol'''
    __table__: 'FromClause' = 'A protocol representing a SQLAlchemy mapped class.\n\n    The protocol is generic on the type of class, use\n    ``MappedClassProtocol[Any]`` to allow any mapped class.\n    '
    
    def __call__(self = None, **kw):
        pass


MappedClassProtocol = <NODE:27>(MappedClassProtocol, 'MappedClassProtocol', Protocol[_O])

def _DeclMappedClassProtocol():
    '''_DeclMappedClassProtocol'''
    _sa_apply_dc_transforms: 'Optional[_DataclassArguments]' = 'Internal more detailed version of ``MappedClassProtocol``.'
    
    def __declare_first__(self = None):
        pass

    
    def __declare_last__(self = None):
        pass


_DeclMappedClassProtocol = <NODE:27>(_DeclMappedClassProtocol, '_DeclMappedClassProtocol', MappedClassProtocol[_O], Protocol)

class _DataclassArguments(TypedDict):
    dataclass_callable: 'Union[_NoArg, Callable[..., Type[Any]]]' = '_DataclassArguments'


def _declared_mapping_info(cls = None):
    if _DeferredMapperConfig.has_cls(cls):
        return _DeferredMapperConfig.config_for_cls(cls)
    if None(cls):
        return class_mapper(cls, configure = False)


def _is_supercls_for_inherits(cls = None):
    '''return True if this class will be used as a superclass to set in
    \'inherits\'.

    This includes deferred mapper configs that aren\'t mapped yet, however does
    not include classes with _sa_decl_prepare_nocascade (e.g.
    ``AbstractConcreteBase``); these concrete-only classes are not set up as
    "inherits" until after mappers are configured using
    mapper._set_concrete_base()

    '''
    if _DeferredMapperConfig.has_cls(cls):
        return not _get_immediate_cls_attr(cls, '_sa_decl_prepare_nocascade', strict = True)
    if None(cls):
        return True


def _resolve_for_abstract_or_classical(cls = None):
    if cls is object:
        return None
# WARNING: Decompyle incomplete


def _get_immediate_cls_attr(cls = None, attrname = None, strict = None):
    '''return an attribute of the class that is either present directly
    on the class, e.g. not on a superclass, or is from a superclass but
    this superclass is a non-mapped mixin, that is, not a descendant of
    the declarative base and is also not classically mapped.

    This is used to detect attributes that indicate something about
    a mapped class independently from any mapped classes that it may
    inherit from.

    '''
    pass
# WARNING: Decompyle incomplete


def _dive_for_cls_manager(cls = None):
    for base in cls.__mro__:
        manager = attributes.opt_manager_of_class(base)
        if manager:
            
            return None, manager
        return None


def _as_declarative(registry = None, cls = None, dict_ = None):
    return _MapperConfig.setup_mapping(registry, cls, dict_, None, { })


def _mapper(registry = None, cls = None, table = None, mapper_kw = ('registry', '_RegistryType', 'cls', 'Type[_O]', 'table', 'Optional[FromClause]', 'mapper_kw', '_MapperKwArgs', 'return', 'Mapper[_O]')):
    _ImperativeMapperConfig(registry, cls, table, mapper_kw)
    return cast('MappedClassProtocol[_O]', cls).__mapper__

_is_declarative_props = (lambda obj = None: _declared_attr_common = util.preloaded.orm_decl_api._declared_attr_commonisinstance(obj, (_declared_attr_common, util.classproperty)))()

def _check_declared_props_nocascade(obj = None, name = None, cls = None):
    if _is_declarative_props(obj):
        if getattr(obj, '_cascading', False):
            util.warn(f'''@declared_attr.cascading is not supported on the {name!s} attribute on class {cls!s}.  This attribute invokes for subclasses in any case.''')
        return True


class _MapperConfig:
    declared_attr_reg: 'Dict[declared_attr[Any], Any]' = ('cls', 'classname', 'properties', 'declared_attr_reg', '__weakref__')
    setup_mapping = (lambda cls, registry, cls_ = None, dict_ = None, table = classmethod, mapper_kw = ('registry', '_RegistryType', 'cls_', 'Type[_O]', 'dict_', '_ClassDict', 'table', 'Optional[FromClause]', 'mapper_kw', '_MapperKwArgs', 'return', 'Optional[_MapperConfig]'):
