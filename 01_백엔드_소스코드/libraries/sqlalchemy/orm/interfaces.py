# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: interfaces.pyc (Python 3.11)

'''

Contains various base classes used throughout the ORM.

Defines some key base classes prominent within the internals.

This module and the classes within are mostly private, though some attributes
are exposed when inspecting mappings.

'''
from __future__ import annotations
import collections
import dataclasses
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import ClassVar
from typing import Dict
from typing import Generic
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NamedTuple
from typing import NoReturn
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import exc as orm_exc
from  import path_registry
from base import _MappedAttribute
from base import EXT_CONTINUE
from base import EXT_SKIP
from base import EXT_STOP
from base import InspectionAttr
from base import InspectionAttrInfo
from base import MANYTOMANY
from base import MANYTOONE
from base import NO_KEY
from base import NO_VALUE
from base import NotExtension
from base import ONETOMANY
from base import RelationshipDirection
from base import SQLORMOperations
from  import ColumnElement
from  import exc as sa_exc
from  import inspection
from  import util
from sql import operators
from sql import roles
from sql import visitors
from sql.base import _NoArg
from sql.base import ExecutableOption
from sql.cache_key import HasCacheKey
from sql.operators import ColumnOperators
from sql.schema import Column
from sql.type_api import TypeEngine
from util import warn_deprecated
from util.typing import RODescriptorReference
from util.typing import TypedDict
if typing.TYPE_CHECKING:
    from _typing import _EntityType
    from _typing import _IdentityKeyType
    from _typing import _InstanceDict
    from _typing import _InternalEntityType
    from _typing import _ORMAdapterProto
    from attributes import InstrumentedAttribute
    from base import Mapped
    from context import _MapperEntity
    from context import ORMCompileState
    from context import QueryContext
    from decl_api import RegistryType
    from decl_base import _ClassScanMapperConfig
    from loading import _PopulatorDict
    from mapper import Mapper
    from path_registry import AbstractEntityRegistry
    from query import Query
    from session import Session
    from state import InstanceState
    from strategy_options import _LoadElement
    from util import AliasedInsp
    from util import ORMAdapter
    from engine.result import Result
    from sql._typing import _ColumnExpressionArgument
    from sql._typing import _ColumnsClauseArgument
    from sql._typing import _DMLColumnArgument
    from sql._typing import _InfoType
    from sql.operators import OperatorType
    from sql.visitors import _TraverseInternalsType
    from util.typing import _AnnotationScanType
_StrategyKey = Tuple[(Any, ...)]
_T = TypeVar('_T', bound = Any)
_T_co = TypeVar('_T_co', bound = Any, covariant = True)
_TLS = TypeVar('_TLS', bound = 'Type[LoaderStrategy]')

class ORMStatementRole(roles.StatementRole):
    __slots__ = ()
    _role_name = 'Executable SQL or text() construct, including ORM aware objects'


def ORMColumnsClauseRole():
    '''ORMColumnsClauseRole'''
    __slots__ = ()
    _role_name = 'ORM mapped entity, aliased entity, or Column expression'

ORMColumnsClauseRole = <NODE:27>(ORMColumnsClauseRole, 'ORMColumnsClauseRole', roles.ColumnsClauseRole, roles.TypedColumnsClauseRole[_T])

def ORMEntityColumnsClauseRole():
    '''ORMEntityColumnsClauseRole'''
    __slots__ = ()
    _role_name = 'ORM mapped or aliased entity'

ORMEntityColumnsClauseRole = <NODE:27>(ORMEntityColumnsClauseRole, 'ORMEntityColumnsClauseRole', ORMColumnsClauseRole[_T])

class ORMFromClauseRole(roles.StrictFromClauseRole):
    __slots__ = ()
    _role_name = 'ORM mapped entity, aliased entity, or FROM expression'


class ORMColumnDescription(TypedDict):
    entity: 'Optional[_ColumnsClauseArgument[Any]]' = 'ORMColumnDescription'


class _IntrospectsAnnotations:
    __slots__ = ()
    _mapper_property_name = (lambda cls = None: cls.__name__)()
    
    def found_in_pep593_annotated(self = None):
        '''return a copy of this object to use in declarative when the
        object is found inside of an Annotated object.'''
        raise NotImplementedError(f'''Use of the {self._mapper_property_name()!r} construct inside of an Annotated object is not yet supported.''')

    
    def declarative_scan(self, decl_scan, registry, cls, originating_module, key, mapped_container = None, annotation = None, extracted_mapped_annotation = None, is_dataclass_field = ('decl_scan', '_ClassScanMapperConfig', 'registry', 'RegistryType', 'cls', 'Type[Any]', 'originating_module', 'Optional[str]', 'key', 'str', 'mapped_container', 'Optional[Type[Mapped[Any]]]', 'annotation', 'Optional[_AnnotationScanType]', 'extracted_mapped_annotation', 'Optional[_AnnotationScanType]', 'is_dataclass_field', 'bool', 'return', 'None')):
        '''Perform class-specific initializaton at early declarative scanning
        time.

        .. versionadded:: 2.0

        '''
        pass

    
    def _raise_for_required(self = None, key = None, cls = None):
        raise sa_exc.ArgumentError(f'''Python typing annotation is required for attribute "{cls.__name__}.{key}" when primary argument(s) for "{self._mapper_property_name()}" construct are None or not present''')



class _AttributeOptions(NamedTuple):
    dataclasses_dataclass_metadata: 'Union[_NoArg, Mapping[Any, Any], None]' = 'define Python-local attribute behavior options common to all\n    :class:`.MapperProperty` objects.\n\n    Currently this includes dataclass-generation arguments.\n\n    .. versionadded:: 2.0\n\n    '
    
    def _as_dataclass_field(self = None, key = None):
        '''Return a ``dataclasses.Field`` object given these arguments.'''
        pass
    # WARNING: Decompyle incomplete

    _get_arguments_for_make_dataclass = (lambda cls, key = None, annotation = None, mapped_container = classmethod, elem = ('key', 'str', 'annotation', '_AnnotationScanType', 'mapped_container', 'Optional[Any]', 'elem', 'Any', 'return', 'Union[Tuple[str, _AnnotationScanType], Tuple[str, _AnnotationScanType, dataclasses.Field[Any]]]'): if isinstance(elem, _DCAttributeOptions):
dc_field = elem._attribute_options._as_dataclass_field(key)(key, annotation, dc_field)if None is not _NoArg.NO_ARG:
(key, annotation, elem)# WARNING: Decompyle incomplete
)()

_DEFAULT_ATTRIBUTE_OPTIONS = _AttributeOptions(_NoArg.NO_ARG, _NoArg.NO_ARG, _NoArg.NO_ARG, _NoArg.NO_ARG, _NoArg.NO_ARG, _NoArg.NO_ARG, _NoArg.NO_ARG, _NoArg.NO_ARG)
_DEFAULT_READONLY_ATTRIBUTE_OPTIONS = _AttributeOptions(False, _NoArg.NO_ARG, _NoArg.NO_ARG, _NoArg.NO_ARG, _NoArg.NO_ARG, _NoArg.NO_ARG, _NoArg.NO_ARG, _NoArg.NO_ARG)

class _DCAttributeOptions:
    '''mixin for descriptors or configurational objects that include dataclass
    field options.

    This includes :class:`.MapperProperty`, :class:`._MapsColumn` within
    the ORM, but also includes :class:`.AssociationProxy` within ext.
    Can in theory be used for other descriptors that serve a similar role
    as association proxy.   (*maybe* hybrids, not sure yet.)

    '''
    _has_dataclass_arguments: 'bool' = ()


def _MapsColumns():
    '''_MapsColumns'''
    __doc__ = 'interface for declarative-capable construct that delivers one or more\n    Column objects to the declarative process to be part of a Table.\n    '
    __slots__ = ()
    mapper_property_to_assign = (lambda self = None: raise NotImplementedError())()
    columns_to_assign = (lambda self = None: raise NotImplementedError())()

_MapsColumns = <NODE:27>(_MapsColumns, '_MapsColumns', _DCAttributeOptions, _MappedAttribute[_T])

def MapperProperty():
    '''MapperProperty'''
    __doc__ = 'Represent a particular class attribute mapped by :class:`_orm.Mapper`.\n\n    The most common occurrences of :class:`.MapperProperty` are the\n    mapped :class:`_schema.Column`, which is represented in a mapping as\n    an instance of :class:`.ColumnProperty`,\n    and a reference to another class produced by :func:`_orm.relationship`,\n    represented in the mapping as an instance of\n    :class:`.Relationship`.\n\n    '
    __slots__ = ('_configure_started', '_configure_finished', '_attribute_options', '_has_dataclass_arguments', 'parent', 'key', 'info', 'doc')
    _cache_key_traversal: '_TraverseInternalsType' = [
        ('parent', visitors.ExtendedInternalTraversal.dp_has_cache_key),
        ('key', visitors.ExtendedInternalTraversal.dp_string)]
    if not TYPE_CHECKING:
        cascade = None
    parent: 'Mapper[Any]' = True
    info: '_InfoType' = False
    
    def _memoized_attr_info(self = None):
        '''Info dictionary associated with the object, allowing user-defined
        data to be associated with this :class:`.InspectionAttr`.

        The dictionary is generated when first accessed.  Alternatively,
        it can be specified as a constructor argument to the
        :func:`.column_property`, :func:`_orm.relationship`, or
        :func:`.composite`
        functions.

        .. seealso::

            :attr:`.QueryableAttribute.info`

            :attr:`.SchemaItem.info`

        '''
        return { }

    
    def setup(self, context = None, query_entity = None, path = None, adapter = ('context', 'ORMCompileState', 'query_entity', '_MapperEntity', 'path', 'AbstractEntityRegistry', 'adapter', 'Optional[ORMAdapter]', 'kwargs', 'Any', 'return', 'None'), **kwargs):
        '''Called by Query for the purposes of constructing a SQL statement.

        Each MapperProperty associated with the target mapper processes the
        statement referenced by the query context, adding columns and/or
        criterion as appropriate.

        '''
        pass

    
    def create_row_processor(self, context, query_entity, path, mapper = None, result = None, adapter = None, populators = ('context', 'ORMCompileState', 'query_entity', '_MapperEntity', 'path', 'AbstractEntityRegistry', 'mapper', 'Mapper[Any]', 'result', 'Result[Any]', 'adapter', 'Optional[ORMAdapter]', 'populators', '_PopulatorDict', 'return', 'None')):
        '''Produce row processing functions and append to the given
        set of populators lists.

        '''
        pass

    
    def cascade_iterator(self, type_ = None, state = None, dict_ = None, visited_states = (None,), halt_on = ('type_', 'str', 'state', 'InstanceState[Any]', 'dict_', '_InstanceDict', 'visited_states', 'Set[InstanceState[Any]]', 'halt_on', 'Optional[Callable[[InstanceState[Any]], bool]]', 'return', 'Iterator[Tuple[object, Mapper[Any], InstanceState[Any], _InstanceDict]]')):
        """Iterate through instances related to the given instance for
        a particular 'cascade', starting with this MapperProperty.

        Return an iterator3-tuples (instance, mapper, state).

        Note that the 'cascade' collection on this MapperProperty is
        checked first for the given type before cascade_iterator is called.

        This method typically only applies to Relationship.

        """
        return iter(())

    
    def set_parent(self = None, parent = None, init = None):
        '''Set the parent mapper that references this MapperProperty.

        This method is overridden by some subclasses to perform extra
        setup when the mapper is first known.

        '''
        self.parent = parent

    
    def instrument_class(self = None, mapper = None):
        '''Hook called by the Mapper to the property to initiate
        instrumentation of the class attribute managed by this
        MapperProperty.

        The MapperProperty here will typically call out to the
        attributes module to set up an InstrumentedAttribute.

        This step is the first of two steps to set up an InstrumentedAttribute,
        and is called early in the mapper setup process.

        The second step is typically the init_class_attribute step,
        called from StrategizedProperty via the post_instrument_class()
        hook.  This step assigns additional state to the InstrumentedAttribute
        (specifically the "impl") which has been determined after the
        MapperProperty has determined what kind of persistence
        management it needs to do (e.g. scalar, object, collection, etc).

        '''
        pass

    
    def __init__(self = None, attribute_options = None, _assume_readonly_dc_attributes = None):
        self._configure_started = False
        self._configure_finished = False
        if _assume_readonly_dc_attributes:
            default_attrs = _DEFAULT_READONLY_ATTRIBUTE_OPTIONS
        else:
            default_attrs = _DEFAULT_ATTRIBUTE_OPTIONS
        if attribute_options and attribute_options != default_attrs:
            self._has_dataclass_arguments = True
            self._attribute_options = attribute_options
            return None
        self._has_dataclass_arguments = None
        self._attribute_options = default_attrs

    
    def init(self = None):
        '''Called after all mappers are created to assemble
        relationships between mappers and perform other post-mapper-creation
        initialization steps.


        '''
        self._configure_started = True
        self.do_init()
        self._configure_finished = True

    class_attribute = (lambda self = None: getattr(self.parent.class_, self.key))()
    
    def do_init(self = None):
        """Perform subclass-specific initialization post-mapper-creation
        steps.

        This is a template method called by the ``MapperProperty``
        object's init() method.

        """
        pass

    
    def post_instrument_class(self = None, mapper = None):
        '''Perform instrumentation adjustments that need to occur
        after init() has completed.

        The given Mapper is the Mapper invoking the operation, which
        may not be the same Mapper as self.parent in an inheritance
        scenario; however, Mapper will always at least be a sub-mapper of
        self.parent.

        This method is typically used by StrategizedProperty, which delegates
        it to LoaderStrategy.init_class_attribute() to perform final setup
        on the class-bound InstrumentedAttribute.

        '''
        pass

    
    def merge(self, session, source_state, source_dict, dest_state, dest_dict = None, load = None, _recursive = None, _resolve_conflict_map = ('session', 'Session', 'source_state', 'InstanceState[Any]', 'source_dict', '_InstanceDict', 'dest_state', 'InstanceState[Any]', 'dest_dict', '_InstanceDict', 'load', 'bool', '_recursive', 'Dict[Any, object]', '_resolve_conflict_map', 'Dict[_IdentityKeyType[Any], object]', 'return', 'None')):
        '''Merge the attribute represented by this ``MapperProperty``
        from source to destination object.

        '''
        pass

    
    def __repr__(self = None):
        return '<%s at 0x%x; %s>' % (self.__class__.__name__, id(self), getattr(self, 'key', 'no key'))


MapperProperty = <NODE:27>(MapperProperty, 'MapperProperty', HasCacheKey, _DCAttributeOptions, _MappedAttribute[_T], InspectionAttrInfo, util.MemoizedSlots)()

def PropComparator():
    '''PropComparator'''
    __doc__ = 'Defines SQL operations for ORM mapped attributes.\n\n    SQLAlchemy allows for operators to\n    be redefined at both the Core and ORM level.  :class:`.PropComparator`\n    is the base class of operator redefinition for ORM-level operations,\n    including those of :class:`.ColumnProperty`,\n    :class:`.Relationship`, and :class:`.Composite`.\n\n    User-defined subclasses of :class:`.PropComparator` may be created. The\n    built-in Python comparison and math operator methods, such as\n    :meth:`.operators.ColumnOperators.__eq__`,\n    :meth:`.operators.ColumnOperators.__lt__`, and\n    :meth:`.operators.ColumnOperators.__add__`, can be overridden to provide\n    new operator behavior. The custom :class:`.PropComparator` is passed to\n    the :class:`.MapperProperty` instance via the ``comparator_factory``\n    argument. In each case,\n    the appropriate subclass of :class:`.PropComparator` should be used::\n\n        # definition of custom PropComparator subclasses\n\n        from sqlalchemy.orm.properties import (\n            ColumnProperty,\n            Composite,\n            Relationship,\n        )\n\n\n        class MyColumnComparator(ColumnProperty.Comparator):\n            def __eq__(self, other):\n                return self.__clause_element__() == other\n\n\n        class MyRelationshipComparator(Relationship.Comparator):\n            def any(self, expression):\n                "define the \'any\' operation"\n                # ...\n\n\n        class MyCompositeComparator(Composite.Comparator):\n            def __gt__(self, other):\n                "redefine the \'greater than\' operation"\n\n                return sql.and_(\n                    *[\n                        a > b\n                        for a, b in zip(\n                            self.__clause_element__().clauses,\n                            other.__composite_values__(),\n                        )\n                    ]\n                )\n\n\n        # application of custom PropComparator subclasses\n\n        from sqlalchemy.orm import column_property, relationship, composite\n        from sqlalchemy import Column, String\n\n\n        class SomeMappedClass(Base):\n            some_column = column_property(\n                Column("some_column", String),\n                comparator_factory=MyColumnComparator,\n            )\n\n            some_relationship = relationship(\n                SomeOtherClass, comparator_factory=MyRelationshipComparator\n            )\n\n            some_composite = composite(\n                Column("a", String),\n                Column("b", String),\n                comparator_factory=MyCompositeComparator,\n            )\n\n    Note that for column-level operator redefinition, it\'s usually\n    simpler to define the operators at the Core level, using the\n    :attr:`.TypeEngine.comparator_factory` attribute.  See\n    :ref:`types_operators` for more detail.\n\n    .. seealso::\n\n        :class:`.ColumnProperty.Comparator`\n\n        :class:`.Relationship.Comparator`\n\n        :class:`.Composite.Comparator`\n\n        :class:`.ColumnOperators`\n\n        :ref:`types_operators`\n\n        :attr:`.TypeEngine.comparator_factory`\n\n    '
    __slots__ = ('prop', '_parententity', '_adapt_to_entity')
    prop: 'RODescriptorReference[MapperProperty[_T_co]]' = 'orm_prop_comparator'
    
    def __init__(self = None, prop = None, parentmapper = None, adapt_to_entity = (None,)):
