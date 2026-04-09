# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: decl_api.pyc (Python 3.11)

'''Public API functions and helpers for declarative.'''
from __future__ import annotations
import itertools
import re
import typing
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Dict
from typing import FrozenSet
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import Mapping
from typing import Optional
from typing import overload
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import weakref
from  import attributes
from  import clsregistry
from  import instrumentation
from  import interfaces
from  import mapperlib
from _orm_constructors import composite
from _orm_constructors import deferred
from _orm_constructors import mapped_column
from _orm_constructors import relationship
from _orm_constructors import synonym
from attributes import InstrumentedAttribute
from base import _inspect_mapped_class
from base import _is_mapped_class
from base import Mapped
from base import ORMDescriptor
from decl_base import _add_attribute
from decl_base import _as_declarative
from decl_base import _ClassScanMapperConfig
from decl_base import _declarative_constructor
from decl_base import _DeferredMapperConfig
from decl_base import _del_attribute
from decl_base import _mapper
from descriptor_props import Composite
from descriptor_props import Synonym
from descriptor_props import Synonym as _orm_synonym
from mapper import Mapper
from properties import MappedColumn
from relationships import RelationshipProperty
from state import InstanceState
from  import exc
from  import inspection
from  import util
from sql import sqltypes
from sql.base import _NoArg
from sql.elements import SQLCoreOperations
from sql.schema import MetaData
from sql.selectable import FromClause
from util import hybridmethod
from util import hybridproperty
from util import typing as compat_typing
from util import warn_deprecated
from util.typing import CallableReference
from util.typing import de_optionalize_union_types
from util.typing import flatten_newtype
from util.typing import is_generic
from util.typing import is_literal
from util.typing import is_newtype
from util.typing import is_pep593
from util.typing import is_pep695
from util.typing import Literal
from util.typing import LITERAL_TYPES
from util.typing import Self
if TYPE_CHECKING:
    from _typing import _O
    from _typing import _RegistryType
    from decl_base import _DataclassArguments
    from instrumentation import ClassManager
    from interfaces import MapperProperty
    from state import InstanceState
    from sql._typing import _TypeEngineArgument
    from sql.type_api import _MatchedOnType
_T = TypeVar('_T', bound = Any)
_TT = TypeVar('_TT', bound = Any)
_TypeAnnotationMapType = Mapping[(Any, '_TypeEngineArgument[Any]')]
_MutableTypeAnnotationMapType = Dict[(Any, '_TypeEngineArgument[Any]')]
_DeclaredAttrDecorated = Callable[(..., Union[(Mapped[_T], ORMDescriptor[_T], SQLCoreOperations[_T])])]

def has_inherited_table(cls = None):
    '''Given a class, return True if any of the classes it inherits from has a
    mapped table, otherwise return False.

    This is used in declarative mixins to build attributes that behave
    differently for the base class vs. a subclass in an inheritance
    hierarchy.

    .. seealso::

        :ref:`decl_mixin_inheritance`

    '''
    pass
# WARNING: Decompyle incomplete


class _DynamicAttributesType(type):
    
    def __setattr__(cls = None, key = None, value = None):
        if '__mapper__' in cls.__dict__:
            _add_attribute(cls, key, value)
            return None
        None.__setattr__(cls, key, value)

    
    def __delattr__(cls = None, key = None):
        if '__mapper__' in cls.__dict__:
            _del_attribute(cls, key)
            return None
        None.__delattr__(cls, key)



def DeclarativeAttributeIntercept():
    '''DeclarativeAttributeIntercept'''
    __doc__ = 'Metaclass that may be used in conjunction with the\n    :class:`_orm.DeclarativeBase` class to support addition of class\n    attributes dynamically.\n\n    '

DeclarativeAttributeIntercept = <NODE:27>(DeclarativeAttributeIntercept, 'DeclarativeAttributeIntercept', _DynamicAttributesType, inspection.Inspectable[Mapper[Any]])
DCTransformDeclarative = <NODE:12>()

class DeclarativeMeta(DeclarativeAttributeIntercept):
    registry: 'RegistryType' = 'DeclarativeMeta'
    
    def __init__(cls = None, classname = None, bases = None, dict_ = ('classname', 'Any', 'bases', 'Any', 'dict_', 'Any', 'kw', 'Any', 'return', 'None'), **kw):
        dict_ = cls.__dict__
        reg = getattr(cls, '_sa_registry', None)
    # WARNING: Decompyle incomplete



def synonym_for(name = None, map_column = compat_typing.dataclass_transform(field_specifiers = (MappedColumn, RelationshipProperty, Composite, Synonym, mapped_column, relationship, composite, synonym, deferred))):
    '''Decorator that produces an :func:`_orm.synonym`
    attribute in conjunction with a Python descriptor.

    The function being decorated is passed to :func:`_orm.synonym` as the
    :paramref:`.orm.synonym.descriptor` parameter::

        class MyClass(Base):
            __tablename__ = "my_table"

            id = Column(Integer, primary_key=True)
            _job_status = Column("job_status", String(50))

            @synonym_for("job_status")
            @property
            def job_status(self):
                return "Status: %s" % self._job_status

    The :ref:`hybrid properties <mapper_hybrids>` feature of SQLAlchemy
    is typically preferred instead of synonyms, which is a more legacy
    feature.

    .. seealso::

        :ref:`synonyms` - Overview of synonyms

        :func:`_orm.synonym` - the mapper-level function

        :ref:`mapper_hybrids` - The Hybrid Attribute extension provides an
        updated approach to augmenting attribute behavior more flexibly than
        can be achieved with synonyms.

    '''
    pass
# WARNING: Decompyle incomplete


class _declared_attr_common:
    
    def __init__(self = None, fn = None, cascading = None, quiet = (False, False)):
        if isinstance(fn, classmethod):
            fn = fn.__func__
        self.fget = fn
        self._cascading = cascading
        self._quiet = quiet
        self.__doc__ = fn.__doc__

    
    def _collect_return_annotation(self = None):
        return util.get_annotations(self.fget).get('return')

    
    def __get__(self = None, instance = None, owner = None):
        cls = owner
        manager = attributes.opt_manager_of_class(cls)
    # WARNING: Decompyle incomplete



def _declared_directive():
    '''_declared_directive'''
    if typing.TYPE_CHECKING:
        
        def __init__(self = None, fn = None, cascading = None):
            pass

        
        def __get__(self = None, instance = None, owner = None):
            pass

        
        def __set__(self = None, instance = None, value = None):
            pass

        
        def __delete__(self = None, instance = None):
            pass

        
        def __call__(self = None, fn = None):
            pass

        return None

_declared_directive = <NODE:27>(_declared_directive, '_declared_directive', _declared_attr_common, Generic[_T])

def declared_attr():
    '''declared_attr'''
    __doc__ = 'Mark a class-level method as representing the definition of\n    a mapped property or Declarative directive.\n\n    :class:`_orm.declared_attr` is typically applied as a decorator to a class\n    level method, turning the attribute into a scalar-like property that can be\n    invoked from the uninstantiated class. The Declarative mapping process\n    looks for these :class:`_orm.declared_attr` callables as it scans classes,\n    and assumes any attribute marked with :class:`_orm.declared_attr` will be a\n    callable that will produce an object specific to the Declarative mapping or\n    table configuration.\n\n    :class:`_orm.declared_attr` is usually applicable to\n    :ref:`mixins <orm_mixins_toplevel>`, to define relationships that are to be\n    applied to different implementors of the class. It may also be used to\n    define dynamically generated column expressions and other Declarative\n    attributes.\n\n    Example::\n\n        class ProvidesUserMixin:\n            "A mixin that adds a \'user\' relationship to classes."\n\n            user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))\n\n            @declared_attr\n            def user(cls) -> Mapped["User"]:\n                return relationship("User")\n\n    When used with Declarative directives such as ``__tablename__``, the\n    :meth:`_orm.declared_attr.directive` modifier may be used which indicates\n    to :pep:`484` typing tools that the given method is not dealing with\n    :class:`_orm.Mapped` attributes::\n\n        class CreateTableName:\n            @declared_attr.directive\n            def __tablename__(cls) -> str:\n                return cls.__name__.lower()\n\n    :class:`_orm.declared_attr` can also be applied directly to mapped\n    classes, to allow for attributes that dynamically configure themselves\n    on subclasses when using mapped inheritance schemes.   Below\n    illustrates :class:`_orm.declared_attr` to create a dynamic scheme\n    for generating the :paramref:`_orm.Mapper.polymorphic_identity` parameter\n    for subclasses::\n\n        class Employee(Base):\n            __tablename__ = "employee"\n\n            id: Mapped[int] = mapped_column(primary_key=True)\n            type: Mapped[str] = mapped_column(String(50))\n\n            @declared_attr.directive\n            def __mapper_args__(cls) -> Dict[str, Any]:\n                if cls.__name__ == "Employee":\n                    return {\n                        "polymorphic_on": cls.type,\n                        "polymorphic_identity": "Employee",\n                    }\n                else:\n                    return {"polymorphic_identity": cls.__name__}\n\n\n        class Engineer(Employee):\n            pass\n\n    :class:`_orm.declared_attr` supports decorating functions that are\n    explicitly decorated with ``@classmethod``. This is never necessary from a\n    runtime perspective, however may be needed in order to support :pep:`484`\n    typing tools that don\'t otherwise recognize the decorated function as\n    having class-level behaviors for the ``cls`` parameter::\n\n        class SomethingMixin:\n            x: Mapped[int]\n            y: Mapped[int]\n\n            @declared_attr\n            @classmethod\n            def x_plus_y(cls) -> Mapped[int]:\n                return column_property(cls.x + cls.y)\n\n    .. versionadded:: 2.0 - :class:`_orm.declared_attr` can accommodate a\n       function decorated with ``@classmethod`` to help with :pep:`484`\n       integration where needed.\n\n\n    .. seealso::\n\n        :ref:`orm_mixins_toplevel` - Declarative Mixin documentation with\n        background on use patterns for :class:`_orm.declared_attr`.\n\n    '
    if typing.TYPE_CHECKING:
        
        def __init__(self = None, fn = None, cascading = None):
            pass

        
        def __set__(self = None, instance = None, value = None):
            pass

        
        def __delete__(self = None, instance = None):
            pass

        __get__ = (lambda self = None, instance = None, owner = overload: pass)()
        __get__ = (lambda self = None, instance = None, owner = overload: pass)()
        
        def __get__(self = None, instance = None, owner = None):
            pass

    _stateful = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    directive = (lambda cls = None: _declared_directive)()
    cascading = (lambda cls = None: cls._stateful(cascading = True))()

declared_attr = <NODE:27>(declared_attr, 'declared_attr', interfaces._MappedAttribute[_T], _declared_attr_common)

def _stateful_declared_attr():
    '''_stateful_declared_attr'''
    kw: 'Dict[str, Any]' = '_stateful_declared_attr'
    
    def __init__(self = None, **kw):
        self.kw = kw

    _stateful = (lambda self = None: new_kw = self.kw.copy()new_kw.update(kw)# WARNING: Decompyle incomplete
)()
    
    def __call__(self = None, fn = None):
        pass
    # WARNING: Decompyle incomplete


_stateful_declared_attr = <NODE:27>(_stateful_declared_attr, '_stateful_declared_attr', declared_attr[_T])

def declarative_mixin(cls = None):
    '''Mark a class as providing the feature of "declarative mixin".

    E.g.::

        from sqlalchemy.orm import declared_attr
        from sqlalchemy.orm import declarative_mixin


        @declarative_mixin
        class MyMixin:

            @declared_attr
            def __tablename__(cls):
                return cls.__name__.lower()

            __table_args__ = {"mysql_engine": "InnoDB"}
            __mapper_args__ = {"always_refresh": True}

            id = Column(Integer, primary_key=True)


        class MyModel(MyMixin, Base):
            name = Column(String(1000))

    The :func:`_orm.declarative_mixin` decorator currently does not modify
    the given class in any way; it\'s current purpose is strictly to assist
    the :ref:`Mypy plugin <mypy_toplevel>` in being able to identify
    SQLAlchemy declarative mixin classes when no other context is present.

    .. versionadded:: 1.4.6

    .. legacy:: This api is considered legacy and will be deprecated in the next
      SQLAlchemy version.

    .. seealso::

        :ref:`orm_mixins_toplevel`

        :ref:`mypy_declarative_mixins` - in the
        :ref:`Mypy plugin documentation <mypy_toplevel>`

    '''
    return cls


def _setup_declarative_base(cls = None):
    if 'metadata' in cls.__dict__:
        metadata = cls.__dict__['metadata']
    else:
        metadata = None
    if 'type_annotation_map' in cls.__dict__:
        type_annotation_map = cls.__dict__['type_annotation_map']
    else:
        type_annotation_map = None
    reg = cls.__dict__.get('registry', None)
# WARNING: Decompyle incomplete


def MappedAsDataclass():
    '''MappedAsDataclass'''
    pass
# WARNING: Decompyle incomplete

MappedAsDataclass = <NODE:27>(MappedAsDataclass, 'MappedAsDataclass', metaclass = DCTransformDeclarative)

def DeclarativeBase():
    '''DeclarativeBase'''
    pass
# WARNING: Decompyle incomplete

DeclarativeBase = <NODE:27>(DeclarativeBase, 'DeclarativeBase', inspection.Inspectable[InstanceState[Any]], metaclass = DeclarativeAttributeIntercept)

def _check_not_declarative(cls = None, base = None):
    cls_dict = cls.__dict__
    if '__table__' in cls_dict and callable(cls_dict['__table__']) or hasattr(cls_dict['__table__'], '__get__') or isinstance(cls_dict.get('__tablename__', None), str):
        raise exc.InvalidRequestError(f'''Cannot use {base.__name__!r} directly as a declarative base class. Create a Base by creating a subclass of it.''')


def DeclarativeBaseNoMeta():
    '''DeclarativeBaseNoMeta'''
    pass
# WARNING: Decompyle incomplete

DeclarativeBaseNoMeta = <NODE:27>(DeclarativeBaseNoMeta, 'DeclarativeBaseNoMeta', inspection.Inspectable[InstanceState[Any]])

def add_mapped_attribute(target = None, key = None, attr = None):
    '''Add a new mapped attribute to an ORM mapped class.

    E.g.::

        add_mapped_attribute(User, "addresses", relationship(Address))

    This may be used for ORM mappings that aren\'t using a declarative
    metaclass that intercepts attribute set operations.

    .. versionadded:: 2.0


    '''
    _add_attribute(target, key, attr)


def declarative_base(*, metadata, mapper, cls, name, class_registry, type_annotation_map, constructor, metaclass):
    '''Construct a base class for declarative class definitions.

    The new base class will be given a metaclass that produces
    appropriate :class:`~sqlalchemy.schema.Table` objects and makes
    the appropriate :class:`_orm.Mapper` calls based on the
    information provided declaratively in the class and any subclasses
    of the class.

    .. versionchanged:: 2.0 Note that the :func:`_orm.declarative_base`
       function is superseded by the new :class:`_orm.DeclarativeBase` class,
       which generates a new "base" class using subclassing, rather than
       return value of a function.  This allows an approach that is compatible
       with :pep:`484` typing tools.

    The :func:`_orm.declarative_base` function is a shorthand version
    of using the :meth:`_orm.registry.generate_base`
    method.  That is, the following::

        from sqlalchemy.orm import declarative_base

        Base = declarative_base()

    Is equivalent to::

        from sqlalchemy.orm import registry

        mapper_registry = registry()
        Base = mapper_registry.generate_base()

    See the docstring for :class:`_orm.registry`
    and :meth:`_orm.registry.generate_base`
    for more details.

    .. versionchanged:: 1.4  The :func:`_orm.declarative_base`
       function is now a specialization of the more generic
       :class:`_orm.registry` class.  The function also moves to the
       ``sqlalchemy.orm`` package from the ``declarative.ext`` package.


    :param metadata:
      An optional :class:`~sqlalchemy.schema.MetaData` instance.  All
      :class:`~sqlalchemy.schema.Table` objects implicitly declared by
      subclasses of the base will share this MetaData.  A MetaData instance
      will be created if none is provided.  The
      :class:`~sqlalchemy.schema.MetaData` instance will be available via the
      ``metadata`` attribute of the generated declarative base class.

    :param mapper:
      An optional callable, defaults to :class:`_orm.Mapper`. Will
      be used to map subclasses to their Tables.

    :param cls:
      Defaults to :class:`object`. A type to use as the base for the generated
      declarative base class. May be a class or tuple of classes.

    :param name:
      Defaults to ``Base``.  The display name for the generated
      class.  Customizing this is not required, but can improve clarity in
      tracebacks and debugging.

    :param constructor:
      Specify the implementation for the ``__init__`` function on a mapped
      class that has no ``__init__`` of its own.  Defaults to an
      implementation that assigns \\**kwargs for declared
      fields and relationships to an instance.  If ``None`` is supplied,
      no __init__ will be provided and construction will fall back to
      cls.__init__ by way of the normal Python semantics.

    :param class_registry: optional dictionary that will serve as the
      registry of class names-> mapped classes when string names
      are used to identify classes inside of :func:`_orm.relationship`
      and others.  Allows two or more declarative base classes
      to share the same registry of class names for simplified
      inter-base relationships.

    :param type_annotation_map: optional dictionary of Python types to
        SQLAlchemy :class:`_types.TypeEngine` classes or instances.  This
        is used exclusively by the :class:`_orm.MappedColumn` construct
        to produce column types based on annotations within the
        :class:`_orm.Mapped` type.


        .. versionadded:: 2.0

        .. seealso::

            :ref:`orm_declarative_mapped_column_type_map`

    :param metaclass:
      Defaults to :class:`.DeclarativeMeta`.  A metaclass or __metaclass__
      compatible callable to use as the meta type of the generated
      declarative base class.

    .. seealso::

        :class:`_orm.registry`

    '''
    return registry(metadata = metadata, class_registry = class_registry, constructor = constructor, type_annotation_map = type_annotation_map).generate_base(mapper = mapper, cls = cls, name = name, metaclass = metaclass)


class registry:
    _new_mappers: 'bool' = 'Generalized registry for mapping classes.\n\n    The :class:`_orm.registry` serves as the basis for maintaining a collection\n    of mappings, and provides configurational hooks used to map classes.\n\n    The three general kinds of mappings supported are Declarative Base,\n    Declarative Decorator, and Imperative Mapping.   All of these mapping\n    styles may be used interchangeably:\n\n    * :meth:`_orm.registry.generate_base` returns a new declarative base\n      class, and is the underlying implementation of the\n      :func:`_orm.declarative_base` function.\n\n    * :meth:`_orm.registry.mapped` provides a class decorator that will\n      apply declarative mapping to a class without the use of a declarative\n      base class.\n\n    * :meth:`_orm.registry.map_imperatively` will produce a\n      :class:`_orm.Mapper` for a class without scanning the class for\n      declarative class attributes. This method suits the use case historically\n      provided by the ``sqlalchemy.orm.mapper()`` classical mapping function,\n      which is removed as of SQLAlchemy 2.0.\n\n    .. versionadded:: 1.4\n\n    .. seealso::\n\n        :ref:`orm_mapping_classes_toplevel` - overview of class mapping\n        styles.\n\n    '
    
    def __init__(self = None, *, metadata, class_registry, type_annotation_map, constructor):
        '''Construct a new :class:`_orm.registry`

        :param metadata:
          An optional :class:`_schema.MetaData` instance.  All
          :class:`_schema.Table` objects generated using declarative
          table mapping will make use of this :class:`_schema.MetaData`
          collection.  If this argument is left at its default of ``None``,
          a blank :class:`_schema.MetaData` collection is created.

        :param constructor:
          Specify the implementation for the ``__init__`` function on a mapped
          class that has no ``__init__`` of its own.  Defaults to an
          implementation that assigns \\**kwargs for declared
          fields and relationships to an instance.  If ``None`` is supplied,
          no __init__ will be provided and construction will fall back to
          cls.__init__ by way of the normal Python semantics.

        :param class_registry: optional dictionary that will serve as the
          registry of class names-> mapped classes when string names
          are used to identify classes inside of :func:`_orm.relationship`
          and others.  Allows two or more declarative base classes
          to share the same registry of class names for simplified
          inter-base relationships.

        :param type_annotation_map: optional dictionary of Python types to
          SQLAlchemy :class:`_types.TypeEngine` classes or instances.
          The provided dict will update the default type mapping.  This
          is used exclusively by the :class:`_orm.MappedColumn` construct
          to produce column types based on annotations within the
          :class:`_orm.Mapped` type.

          .. versionadded:: 2.0

          .. seealso::

              :ref:`orm_declarative_mapped_column_type_map`


        '''
        if not metadata:
            pass
        lcl_metadata = MetaData()
    # WARNING: Decompyle incomplete

    
    def update_type_annotation_map(self = None, type_annotation_map = None):
        '''update the :paramref:`_orm.registry.type_annotation_map` with new
        values.'''
        (lambda .0: pass# WARNING: Decompyle incomplete
)(type_annotation_map.items()())

    
    def _resolve_type(self = None, python_type = None, _do_fallbacks = None):
        pass
    # WARNING: Decompyle incomplete

    mappers = (lambda self = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(self._managers()).union(self._non_primary_mappers)
)()
    
    def _set_depends_on(self = None, registry = None):
        if registry is self:
            return None
        None._dependents.add(self)
        self._dependencies.add(registry)

    
    def _flag_new_mapper(self = None, mapper = None):
        mapper._ready_for_configure = True
        if self._new_mappers:
            return None
        for reg in None._recurse_with_dependents({
            self}):
            reg._new_mappers = True
            return None

    _recurse_with_dependents = (lambda cls = None, registries = None: pass# WARNING: Decompyle incomplete
)()
    _recurse_with_dependencies = (lambda cls = None, registries = None: pass# WARNING: Decompyle incomplete
)()
    
    def _mappers_to_configure(self = None):
        
        def <genexpr>(.0):
            pass
        # WARNING: Decompyle incomplete

        return list(self._managers)()(<genexpr>, list(self._non_primary_mappers)())

    
    def _add_non_primary_mapper(self = None, np_mapper = None):
        self._non_primary_mappers[np_mapper] = True

    
    def _dispose_cls(self = None, cls = None):
        clsregistry.remove_class(cls.__name__, cls, self._class_registry)

    
    def _add_manager(self = None, manager = None):
        self._managers[manager] = True
        if manager.is_mapped:
            raise exc.ArgumentError("Class '%s' already has a primary mapper defined. " % manager.class_)
    # WARNING: Decompyle incomplete

    
    def configure(self = None, cascade = None):
        '''Configure all as-yet unconfigured mappers in this
        :class:`_orm.registry`.

        The configure step is used to reconcile and initialize the
        :func:`_orm.relationship` linkages between mapped classes, as well as
        to invoke configuration events such as the
        :meth:`_orm.MapperEvents.before_configured` and
        :meth:`_orm.MapperEvents.after_configured`, which may be used by ORM
        extensions or user-defined extension hooks.

        If one or more mappers in this registry contain
        :func:`_orm.relationship` constructs that refer to mapped classes in
        other registries, this registry is said to be *dependent* on those
        registries. In order to configure those dependent registries
        automatically, the :paramref:`_orm.registry.configure.cascade` flag
        should be set to ``True``. Otherwise, if they are not configured, an
        exception will be raised.  The rationale behind this behavior is to
        allow an application to programmatically invoke configuration of
        registries while controlling whether or not the process implicitly
        reaches other registries.

        As an alternative to invoking :meth:`_orm.registry.configure`, the ORM
        function :func:`_orm.configure_mappers` function may be used to ensure
        configuration is complete for all :class:`_orm.registry` objects in
        memory. This is generally simpler to use and also predates the usage of
        :class:`_orm.registry` objects overall. However, this function will
        impact all mappings throughout the running Python process and may be
        more memory/time consuming for an application that has many registries
        in use for different purposes that may not be needed immediately.

        .. seealso::

            :func:`_orm.configure_mappers`


        .. versionadded:: 1.4.0b2

        '''
        mapperlib._configure_registries({
            self}, cascade = cascade)

    
    def dispose(self = None, cascade = None):
        '''Dispose of all mappers in this :class:`_orm.registry`.

        After invocation, all the classes that were mapped within this registry
        will no longer have class instrumentation associated with them. This
        method is the per-:class:`_orm.registry` analogue to the
        application-wide :func:`_orm.clear_mappers` function.

        If this registry contains mappers that are dependencies of other
        registries, typically via :func:`_orm.relationship` links, then those
        registries must be disposed as well. When such registries exist in
        relation to this one, their :meth:`_orm.registry.dispose` method will
        also be called, if the :paramref:`_orm.registry.dispose.cascade` flag
        is set to ``True``; otherwise, an error is raised if those registries
        were not already disposed.

        .. versionadded:: 1.4.0b2

        .. seealso::

            :func:`_orm.clear_mappers`

        '''
        mapperlib._dispose_registries({
            self}, cascade = cascade)

    
    def _dispose_manager_and_mapper(self = None, manager = None):
        if 'mapper' in manager.__dict__:
            mapper = manager.mapper
            mapper._set_dispose_flags()
        class_ = manager.class_
        self._dispose_cls(class_)
        instrumentation._instrumentation_factory.unregister(class_)

    
    def generate_base(self = None, mapper = None, cls = None, name = (None, object, 'Base', DeclarativeMeta), metaclass = ('mapper', 'Optional[Callable[..., Mapper[Any]]]', 'cls', 'Type[Any]', 'name', 'str', 'metaclass', 'Type[Any]', 'return', 'Any')):
        '''Generate a declarative base class.

        Classes that inherit from the returned class object will be
        automatically mapped using declarative mapping.

        E.g.::

            from sqlalchemy.orm import registry

            mapper_registry = registry()

            Base = mapper_registry.generate_base()


            class MyClass(Base):
                __tablename__ = "my_table"
                id = Column(Integer, primary_key=True)

        The above dynamically generated class is equivalent to the
        non-dynamic example below::

            from sqlalchemy.orm import registry
            from sqlalchemy.orm.decl_api import DeclarativeMeta

            mapper_registry = registry()


            class Base(metaclass=DeclarativeMeta):
                __abstract__ = True
                registry = mapper_registry
                metadata = mapper_registry.metadata

                __init__ = mapper_registry.constructor

        .. versionchanged:: 2.0 Note that the
           :meth:`_orm.registry.generate_base` method is superseded by the new
           :class:`_orm.DeclarativeBase` class, which generates a new "base"
           class using subclassing, rather than return value of a function.
           This allows an approach that is compatible with :pep:`484` typing
           tools.

        The :meth:`_orm.registry.generate_base` method provides the
        implementation for the :func:`_orm.declarative_base` function, which
        creates the :class:`_orm.registry` and base class all at once.

        See the section :ref:`orm_declarative_mapping` for background and
        examples.

        :param mapper:
          An optional callable, defaults to :class:`_orm.Mapper`.
          This function is used to generate new :class:`_orm.Mapper` objects.

        :param cls:
          Defaults to :class:`object`. A type to use as the base for the
          generated declarative base class. May be a class or tuple of classes.

        :param name:
          Defaults to ``Base``.  The display name for the generated
          class.  Customizing this is not required, but can improve clarity in
          tracebacks and debugging.

        :param metaclass:
          Defaults to :class:`.DeclarativeMeta`.  A metaclass or __metaclass__
          compatible callable to use as the meta type of the generated
          declarative base class.

        .. seealso::

            :ref:`orm_declarative_mapping`

            :func:`_orm.declarative_base`

        '''
        metadata = self.metadata
        if not isinstance(cls, tuple):
            if not (cls,):
                bases = cls
                class_dict = dict(registry = self, metadata = metadata)
                if isinstance(cls, type):
                    class_dict['__doc__'] = cls.__doc__
    # WARNING: Decompyle incomplete

    mapped_as_dataclass = (lambda self = None, _registry__cls = compat_typing.dataclass_transform(field_specifiers = (MappedColumn, RelationshipProperty, Composite, Synonym, mapped_column, relationship, composite, synonym, deferred)): pass)()()
    mapped_as_dataclass = (lambda self = None, _registry__cls = None, *, init, repr: pass)()
    
    def mapped_as_dataclass(self = None, _registry__cls = None, *, init, repr, eq, order, unsafe_hash, match_args, kw_only, dataclass_callable):
        '''Class decorator that will apply the Declarative mapping process
        to a given class, and additionally convert the class to be a
        Python dataclass.

        .. seealso::

            :ref:`orm_declarative_native_dataclasses` - complete background
            on SQLAlchemy native dataclass mapping

            :func:`_orm.mapped_as_dataclass` - functional version that may
            provide better compatibility with mypy

        .. versionadded:: 2.0


        '''
        pass
    # WARNING: Decompyle incomplete

    
    def mapped(self = None, cls = None):
        '''Class decorator that will apply the Declarative mapping process
        to a given class.

        E.g.::

            from sqlalchemy.orm import registry

            mapper_registry = registry()


            @mapper_registry.mapped
            class Foo:
                __tablename__ = "some_table"

                id = Column(Integer, primary_key=True)
                name = Column(String)

        See the section :ref:`orm_declarative_mapping` for complete
        details and examples.

        :param cls: class to be mapped.

        :return: the class that was passed.

        .. seealso::

            :ref:`orm_declarative_mapping`

            :meth:`_orm.registry.generate_base` - generates a base class
            that will apply Declarative mapping to subclasses automatically
            using a Python metaclass.

        .. seealso::

            :meth:`_orm.registry.mapped_as_dataclass`

        '''
        _as_declarative(self, cls, cls.__dict__)
        return cls

    
    def as_declarative_base(self = None, **kw):
        '''
        Class decorator which will invoke
        :meth:`_orm.registry.generate_base`
        for a given base class.

        E.g.::

            from sqlalchemy.orm import registry

            mapper_registry = registry()


            @mapper_registry.as_declarative_base()
            class Base:
                @declared_attr
                def __tablename__(cls):
                    return cls.__name__.lower()

                id = Column(Integer, primary_key=True)


            class MyMappedClass(Base): ...

        All keyword arguments passed to
        :meth:`_orm.registry.as_declarative_base` are passed
        along to :meth:`_orm.registry.generate_base`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def map_declaratively(self = None, cls = None):
        '''Map a class declaratively.

        In this form of mapping, the class is scanned for mapping information,
        including for columns to be associated with a table, and/or an
        actual table object.

        Returns the :class:`_orm.Mapper` object.

        E.g.::

            from sqlalchemy.orm import registry

            mapper_registry = registry()


            class Foo:
                __tablename__ = "some_table"

                id = Column(Integer, primary_key=True)
                name = Column(String)


            mapper = mapper_registry.map_declaratively(Foo)

        This function is more conveniently invoked indirectly via either the
        :meth:`_orm.registry.mapped` class decorator or by subclassing a
        declarative metaclass generated from
        :meth:`_orm.registry.generate_base`.

        See the section :ref:`orm_declarative_mapping` for complete
        details and examples.

        :param cls: class to be mapped.

        :return: a :class:`_orm.Mapper` object.

        .. seealso::

            :ref:`orm_declarative_mapping`

            :meth:`_orm.registry.mapped` - more common decorator interface
            to this function.

            :meth:`_orm.registry.map_imperatively`

        '''
        _as_declarative(self, cls, cls.__dict__)
        return cls.__mapper__

    
    def map_imperatively(self = None, class_ = None, local_table = None, **kw):
        '''Map a class imperatively.

        In this form of mapping, the class is not scanned for any mapping
        information.  Instead, all mapping constructs are passed as
        arguments.

        This method is intended to be fully equivalent to the now-removed
        SQLAlchemy ``mapper()`` function, except that it\'s in terms of
        a particular registry.

        E.g.::

            from sqlalchemy.orm import registry

            mapper_registry = registry()

            my_table = Table(
                "my_table",
                mapper_registry.metadata,
                Column("id", Integer, primary_key=True),
            )


            class MyClass:
                pass


            mapper_registry.map_imperatively(MyClass, my_table)

        See the section :ref:`orm_imperative_mapping` for complete background
        and usage examples.

        :param class\\_: The class to be mapped.  Corresponds to the
         :paramref:`_orm.Mapper.class_` parameter.

        :param local_table: the :class:`_schema.Table` or other
         :class:`_sql.FromClause` object that is the subject of the mapping.
         Corresponds to the
         :paramref:`_orm.Mapper.local_table` parameter.

        :param \\**kw: all other keyword arguments are passed to the
         :class:`_orm.Mapper` constructor directly.

        .. seealso::

            :ref:`orm_imperative_mapping`

            :ref:`orm_declarative_mapping`

        '''
        return _mapper(self, class_, local_table, kw)


RegistryType = registry
if not TYPE_CHECKING:
    _RegistryType = registry

def as_declarative(**kw):
    '''
    Class decorator which will adapt a given class into a
    :func:`_orm.declarative_base`.

    This function makes use of the :meth:`_orm.registry.as_declarative_base`
    method, by first creating a :class:`_orm.registry` automatically
    and then invoking the decorator.

    E.g.::

        from sqlalchemy.orm import as_declarative


        @as_declarative()
        class Base:
            @declared_attr
            def __tablename__(cls):
                return cls.__name__.lower()

            id = Column(Integer, primary_key=True)


        class MyMappedClass(Base): ...

    .. seealso::

        :meth:`_orm.registry.as_declarative_base`

    '''
    class_registry = kw.pop('class_registry', None)
    metadata = kw.pop('metadata', None)
# WARNING: Decompyle incomplete

mapped_as_dataclass = (lambda registry = None, *, init: registry.mapped_as_dataclass(init = init, repr = repr, eq = eq, order = order, unsafe_hash = unsafe_hash, match_args = match_args, kw_only = kw_only, dataclass_callable = dataclass_callable))()
_inspect_decl_meta = (lambda cls = None: mp = _inspect_mapped_class(cls)# WARNING: Decompyle incomplete
)()
