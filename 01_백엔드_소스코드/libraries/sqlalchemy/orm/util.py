# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import annotations
import enum
import functools
import re
import types
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
from typing import Match
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import weakref
from  import attributes
from  import exc
from  import exc as orm_exc
from _typing import _O
from _typing import insp_is_aliased_class
from _typing import insp_is_mapper
from _typing import prop_is_relationship
from base import _class_to_mapper
from base import _MappedAnnotationBase
from base import _never_set
from base import _none_only_set
from base import _none_set
from base import attribute_str
from base import class_mapper
from base import DynamicMapped
from base import InspectionAttr
from base import instance_str
from base import Mapped
from base import object_mapper
from base import object_state
from base import opt_manager_of_class
from base import ORMDescriptor
from base import state_attribute_str
from base import state_class_str
from base import state_str
from base import WriteOnlyMapped
from interfaces import CriteriaOption
from interfaces import MapperProperty
from interfaces import ORMColumnsClauseRole
from interfaces import ORMEntityColumnsClauseRole
from interfaces import ORMFromClauseRole
from path_registry import PathRegistry
from  import event
from  import exc as sa_exc
from  import inspection
from  import sql
from  import util
from engine.result import result_tuple
from sql import coercions
from sql import expression
from sql import lambdas
from sql import roles
from sql import util as sql_util
from sql import visitors
from sql._typing import is_selectable
from sql.annotation import SupportsCloneAnnotations
from sql.base import ColumnCollection
from sql.cache_key import HasCacheKey
from sql.cache_key import MemoizedHasCacheKey
from sql.elements import ColumnElement
from sql.elements import KeyedColumnElement
from sql.selectable import FromClause
from util.langhelpers import MemoizedSlots
from util.typing import de_stringify_annotation as _de_stringify_annotation
from util.typing import eval_name_only as _eval_name_only
from util.typing import fixup_container_fwd_refs
from util.typing import get_origin
from util.typing import is_origin_of_cls
from util.typing import Literal
from util.typing import Protocol
if typing.TYPE_CHECKING:
    from _typing import _EntityType
    from _typing import _IdentityKeyType
    from _typing import _InternalEntityType
    from _typing import _ORMCOLEXPR
    from context import _MapperEntity
    from context import ORMCompileState
    from mapper import Mapper
    from path_registry import AbstractEntityRegistry
    from query import Query
    from relationships import RelationshipProperty
    from engine import Row
    from engine import RowMapping
    from sql._typing import _CE
    from sql._typing import _ColumnExpressionArgument
    from sql._typing import _EquivalentColumnMap
    from sql._typing import _FromClauseArgument
    from sql._typing import _OnClauseArgument
    from sql._typing import _PropagateAttrsType
    from sql.annotation import _SA
    from sql.base import ReadOnlyColumnCollection
    from sql.elements import BindParameter
    from sql.selectable import _ColumnsClauseElement
    from sql.selectable import Select
    from sql.selectable import Selectable
    from sql.visitors import anon_map
    from util.typing import _AnnotationScanType
_T = TypeVar('_T', bound = Any)
all_cascades = frozenset(('delete', 'delete-orphan', 'all', 'merge', 'expunge', 'save-update', 'refresh-expire', 'none'))
_de_stringify_partial = functools.partial(functools.partial, locals_ = util.immutabledict({
    'Mapped': Mapped,
    'WriteOnlyMapped': WriteOnlyMapped,
    'DynamicMapped': DynamicMapped }))

class _DeStringifyAnnotation(Protocol):
    
    def __call__(self = None, cls = None, annotation = None, originating_module = None, *, str_cleanup_fn, include_generic):
        pass


de_stringify_annotation = cast(_DeStringifyAnnotation, _de_stringify_partial(_de_stringify_annotation))

class _EvalNameOnly(Protocol):
    
    def __call__(self = None, name = None, module_name = None):
        pass


eval_name_only = cast(_EvalNameOnly, _de_stringify_partial(_eval_name_only))

def CascadeOptions():
    '''CascadeOptions'''
    pass
# WARNING: Decompyle incomplete

CascadeOptions = <NODE:27>(CascadeOptions, 'CascadeOptions', FrozenSet[str])

def _validator_events(desc, key, validator, include_removes, include_backrefs):
    '''Runs a validation method on an attribute value to be set or
    appended.
    '''
    pass
# WARNING: Decompyle incomplete


def polymorphic_union(table_map, typecolname, aliasname, cast_nulls = ('p_union', True)):
    '''Create a ``UNION`` statement used by a polymorphic mapper.

    See  :ref:`concrete_inheritance` for an example of how
    this is used.

    :param table_map: mapping of polymorphic identities to
     :class:`_schema.Table` objects.
    :param typecolname: string name of a "discriminator" column, which will be
     derived from the query, producing the polymorphic identity for
     each row.  If ``None``, no polymorphic discriminator is generated.
    :param aliasname: name of the :func:`~sqlalchemy.sql.expression.alias()`
     construct generated.
    :param cast_nulls: if True, non-existent columns, which are represented
     as labeled NULLs, will be passed into CAST.   This is a legacy behavior
     that is problematic on some backends such as Oracle - in which case it
     can be set to False.

    '''
    pass
# WARNING: Decompyle incomplete


def identity_key(class_ = None, ident = None, *, instance, row, identity_token):
    '''Generate "identity key" tuples, as are used as keys in the
    :attr:`.Session.identity_map` dictionary.

    This function has several call styles:

    * ``identity_key(class, ident, identity_token=token)``

      This form receives a mapped class and a primary key scalar or
      tuple as an argument.

      E.g.::

        >>> identity_key(MyClass, (1, 2))
        (<class \'__main__.MyClass\'>, (1, 2), None)

      :param class: mapped class (must be a positional argument)
      :param ident: primary key, may be a scalar or tuple argument.
      :param identity_token: optional identity token

        .. versionadded:: 1.2 added identity_token


    * ``identity_key(instance=instance)``

      This form will produce the identity key for a given instance.  The
      instance need not be persistent, only that its primary key attributes
      are populated (else the key will contain ``None`` for those missing
      values).

      E.g.::

        >>> instance = MyClass(1, 2)
        >>> identity_key(instance=instance)
        (<class \'__main__.MyClass\'>, (1, 2), None)

      In this form, the given instance is ultimately run though
      :meth:`_orm.Mapper.identity_key_from_instance`, which will have the
      effect of performing a database check for the corresponding row
      if the object is expired.

      :param instance: object instance (must be given as a keyword arg)

    * ``identity_key(class, row=row, identity_token=token)``

      This form is similar to the class/tuple form, except is passed a
      database result row as a :class:`.Row` or :class:`.RowMapping` object.

      E.g.::

        >>> row = engine.execute(text("select * from table where a=1 and b=2")).first()
        >>> identity_key(MyClass, row=row)
        (<class \'__main__.MyClass\'>, (1, 2), None)

      :param class: mapped class (must be a positional argument)
      :param row: :class:`.Row` row returned by a :class:`_engine.CursorResult`
       (must be given as a keyword arg)
      :param identity_token: optional identity token

        .. versionadded:: 1.2 added identity_token

    '''
    pass
# WARNING: Decompyle incomplete


class _TraceAdaptRole(enum.Enum):
    '''Enumeration of all the use cases for ORMAdapter.

    ORMAdapter remains one of the most complicated aspects of the ORM, as it is
    used for in-place adaption of column expressions to be applied to a SELECT,
    replacing :class:`.Table` and other objects that are mapped to classes with
    aliases of those tables in the case of joined eager loading, or in the case
    of polymorphic loading as used with concrete mappings or other custom "with
    polymorphic" parameters, with whole user-defined subqueries. The
    enumerations provide an overview of all the use cases used by ORMAdapter, a
    layer of formality as to the introduction of new ORMAdapter use cases (of
    which none are anticipated), as well as a means to trace the origins of a
    particular ORMAdapter within runtime debugging.

    SQLAlchemy 2.0 has greatly scaled back ORM features which relied heavily on
    open-ended statement adaption, including the ``Query.with_polymorphic()``
    method and the ``Query.select_from_entity()`` methods, favoring
    user-explicit aliasing schemes using the ``aliased()`` and
    ``with_polymorphic()`` standalone constructs; these still use adaption,
    however the adaption is applied in a narrower scope.

    '''
    ALIASED_INSP = enum.auto()
    JOINEDLOAD_USER_DEFINED_ALIAS = enum.auto()
    JOINEDLOAD_PATH_WITH_POLYMORPHIC = enum.auto()
    JOINEDLOAD_MEMOIZED_ADAPTER = enum.auto()
    MAPPER_POLYMORPHIC_ADAPTER = enum.auto()
    WITH_POLYMORPHIC_ADAPTER = enum.auto()
    WITH_POLYMORPHIC_ADAPTER_RIGHT_JOIN = enum.auto()
    DEPRECATED_JOIN_ADAPT_RIGHT_SIDE = enum.auto()
    ADAPT_FROM_STATEMENT = enum.auto()
    COMPOUND_EAGER_STATEMENT = enum.auto()
    LEGACY_SELECT_FROM_ALIAS = enum.auto()


class ORMStatementAdapter(sql_util.ColumnAdapter):
    pass
# WARNING: Decompyle incomplete


class ORMAdapter(sql_util.ColumnAdapter):
    pass
# WARNING: Decompyle incomplete


def AliasedClass():
    '''AliasedClass'''
    __name__: 'str' = 'Represents an "aliased" form of a mapped class for usage with Query.\n\n    The ORM equivalent of a :func:`~sqlalchemy.sql.expression.alias`\n    construct, this object mimics the mapped class using a\n    ``__getattr__`` scheme and maintains a reference to a\n    real :class:`~sqlalchemy.sql.expression.Alias` object.\n\n    A primary purpose of :class:`.AliasedClass` is to serve as an alternate\n    within a SQL statement generated by the ORM, such that an existing\n    mapped entity can be used in multiple contexts.   A simple example::\n\n        # find all pairs of users with the same name\n        user_alias = aliased(User)\n        session.query(User, user_alias).join(\n            (user_alias, User.id > user_alias.id)\n        ).filter(User.name == user_alias.name)\n\n    :class:`.AliasedClass` is also capable of mapping an existing mapped\n    class to an entirely new selectable, provided this selectable is column-\n    compatible with the existing mapped selectable, and it can also be\n    configured in a mapping as the target of a :func:`_orm.relationship`.\n    See the links below for examples.\n\n    The :class:`.AliasedClass` object is constructed typically using the\n    :func:`_orm.aliased` function.   It also is produced with additional\n    configuration when using the :func:`_orm.with_polymorphic` function.\n\n    The resulting object is an instance of :class:`.AliasedClass`.\n    This object implements an attribute scheme which produces the\n    same attribute and method interface as the original mapped\n    class, allowing :class:`.AliasedClass` to be compatible\n    with any attribute technique which works on the original class,\n    including hybrid attributes (see :ref:`hybrids_toplevel`).\n\n    The :class:`.AliasedClass` can be inspected for its underlying\n    :class:`_orm.Mapper`, aliased selectable, and other information\n    using :func:`_sa.inspect`::\n\n        from sqlalchemy import inspect\n\n        my_alias = aliased(MyClass)\n        insp = inspect(my_alias)\n\n    The resulting inspection object is an instance of :class:`.AliasedInsp`.\n\n\n    .. seealso::\n\n        :func:`.aliased`\n\n        :func:`.with_polymorphic`\n\n        :ref:`relationship_aliased_class`\n\n        :ref:`relationship_to_window_function`\n\n\n    '
    
    def __init__(self, mapped_class_or_ac, alias, name, flat, adapt_on_names, with_polymorphic_mappers = None, with_polymorphic_discriminator = None, base_alias = None, use_mapper_path = (None, None, False, False, None, None, None, False, False), represents_outer_join = ('mapped_class_or_ac', '_EntityType[_O]', 'alias', 'Optional[FromClause]', 'name', 'Optional[str]', 'flat', 'bool', 'adapt_on_names', 'bool', 'with_polymorphic_mappers', 'Optional[Sequence[Mapper[Any]]]', 'with_polymorphic_discriminator', 'Optional[ColumnElement[Any]]', 'base_alias', 'Optional[AliasedInsp[Any]]', 'use_mapper_path', 'bool', 'represents_outer_join', 'bool')):
        insp = cast('_InternalEntityType[_O]', inspection.inspect(mapped_class_or_ac))
        mapper = insp.mapper
        nest_adapters = False
    # WARNING: Decompyle incomplete

    _reconstitute_from_aliased_insp = (lambda cls = None, aliased_insp = None: obj = cls.__new__(cls)obj.__name__ = f'''aliased({aliased_insp.mapper.class_.__name__})'''obj._aliased_insp = aliased_inspif aliased_insp._is_with_polymorphic:
for sub_aliased_insp in aliased_insp._with_polymorphic_entities:
if sub_aliased_insp is not aliased_insp:
ent = AliasedClass._reconstitute_from_aliased_insp(sub_aliased_insp)setattr(obj, sub_aliased_insp.class_.__name__, ent)obj)()
    
    def __getattr__(self = None, key = None):
        
        try:
            _aliased_insp = self.__dict__['_aliased_insp']
            target = _aliased_insp._target
            attr = getattr(target, key)
        except KeyError:
            raise AttributeError()

        if hasattr(attr, '__call__') and hasattr(attr, '__self__'):
            return types.MethodType(attr.__func__, self)
        if None(attr, '__get__'):
            attr = attr.__get__(None, self)
        if hasattr(attr, 'adapt_to_entity'):
            attr = attr.adapt_to_entity(_aliased_insp)
            setattr(self, key, attr)
        return attr

    
    def _get_from_serialized(self = None, key = None, mapped_class = None, aliased_insp = ('key', 'str', 'mapped_class', '_O', 'aliased_insp', 'AliasedInsp[_O]', 'return', 'Any')):
        attr = getattr(mapped_class, key)
        if hasattr(attr, '__call__') and hasattr(attr, '__self__'):
            return types.MethodType(attr.__func__, self)
        if None(attr, '__get__'):
            attr = attr.__get__(None, self)
        if hasattr(attr, 'adapt_to_entity'):
            aliased_insp._weak_entity = weakref.ref(self)
            attr = attr.adapt_to_entity(aliased_insp)
            setattr(self, key, attr)
        return attr

    
    def __repr__(self = None):
        return '<AliasedClass at 0x%x; %s>' % (id(self), self._aliased_insp._target.__name__)

    
    def __str__(self = None):
        return str(self._aliased_insp)


AliasedClass = <NODE:27>(AliasedClass, 'AliasedClass', inspection.Inspectable['AliasedInsp[_O]'], ORMColumnsClauseRole[_O])

def AliasedInsp():
    '''AliasedInsp'''
    __doc__ = 'Provide an inspection interface for an\n    :class:`.AliasedClass` object.\n\n    The :class:`.AliasedInsp` object is returned\n    given an :class:`.AliasedClass` using the\n    :func:`_sa.inspect` function::\n\n        from sqlalchemy import inspect\n        from sqlalchemy.orm import aliased\n\n        my_alias = aliased(MyMappedClass)\n        insp = inspect(my_alias)\n\n    Attributes on :class:`.AliasedInsp`\n    include:\n\n    * ``entity`` - the :class:`.AliasedClass` represented.\n    * ``mapper`` - the :class:`_orm.Mapper` mapping the underlying class.\n    * ``selectable`` - the :class:`_expression.Alias`\n      construct which ultimately\n      represents an aliased :class:`_schema.Table` or\n      :class:`_expression.Select`\n      construct.\n    * ``name`` - the name of the alias.  Also is used as the attribute\n      name when returned in a result tuple from :class:`_query.Query`.\n    * ``with_polymorphic_mappers`` - collection of :class:`_orm.Mapper`\n      objects\n      indicating all those mappers expressed in the select construct\n      for the :class:`.AliasedClass`.\n    * ``polymorphic_on`` - an alternate column or SQL expression which\n      will be used as the "discriminator" for a polymorphic load.\n\n    .. seealso::\n\n        :ref:`inspection_toplevel`\n\n    '
    __slots__ = ('__weakref__', '_weak_entity', 'mapper', 'selectable', 'name', '_adapt_on_names', 'with_polymorphic_mappers', 'polymorphic_on', '_use_mapper_path', '_base_alias', 'represents_outer_join', 'persist_selectable', 'local_table', '_is_with_polymorphic', '_with_polymorphic_entities', '_adapter', '_target', '__clause_element__', '_memoized_values', '_all_column_expressions', '_nest_adapters')
    _target: 'Union[Type[_O], AliasedClass[_O]]' = [
        ('name', visitors.ExtendedInternalTraversal.dp_string),
        ('_adapt_on_names', visitors.ExtendedInternalTraversal.dp_boolean),
        ('_use_mapper_path', visitors.ExtendedInternalTraversal.dp_boolean),
        ('_target', visitors.ExtendedInternalTraversal.dp_inspectable),
        ('selectable', visitors.ExtendedInternalTraversal.dp_clauseelement),
        ('with_polymorphic_mappers', visitors.InternalTraversal.dp_has_cache_key_list),
        ('polymorphic_on', visitors.InternalTraversal.dp_clauseelement)]
    
    def __init__(self, entity, inspected, selectable, name, with_polymorphic_mappers, polymorphic_on, _base_alias, _use_mapper_path = None, adapt_on_names = None, represents_outer_join = None, nest_adapters = ('entity', 'AliasedClass[_O]', 'inspected', '_InternalEntityType[_O]', 'selectable', 'FromClause', 'name', 'Optional[str]', 'with_polymorphic_mappers', 'Optional[Sequence[Mapper[Any]]]', 'polymorphic_on', 'Optional[ColumnElement[Any]]', '_base_alias', 'Optional[AliasedInsp[Any]]', '_use_mapper_path', 'bool', 'adapt_on_names', 'bool', 'represents_outer_join', 'bool', 'nest_adapters', 'bool')):
        pass
    # WARNING: Decompyle incomplete

    _alias_factory = (lambda cls, element = None, alias = None, name = classmethod, flat = (None, None, False, False), adapt_on_names = ('element', 'Union[_EntityType[_O], FromClause]', 'alias', 'Optional[FromClause]', 'name', 'Optional[str]', 'flat', 'bool', 'adapt_on_names', 'bool', 'return', 'Union[AliasedClass[_O], FromClause]'): if isinstance(element, FromClause):
if adapt_on_names:
raise sa_exc.ArgumentError('adapt_on_names only applies to ORM elements')if name:
element.alias(name = name, flat = flat)None.expect(roles.AnonymizedFromClauseRole, element, flat = flat)None(element, alias = alias, flat = flat, name = name, adapt_on_names = adapt_on_names))()
    _with_polymorphic_factory = (lambda cls, base, classes, selectable, flat, polymorphic_on, aliased = None, innerjoin = None, adapt_on_names = classmethod, name = (False, False, None, False, False, False, None, False), _use_mapper_path = ('base', 'Union[Type[_O], Mapper[_O]]', 'classes', "Union[Literal['*'], Iterable[_EntityType[Any]]]", 'selectable', 'Union[Literal[False, None], FromClause]', 'flat', 'bool', 'polymorphic_on', 'Optional[ColumnElement[Any]]', 'aliased', 'bool', 'innerjoin', 'bool', 'adapt_on_names', 'bool', 'name', 'Optional[str]', '_use_mapper_path', 'bool', 'return', 'AliasedClass[_O]'): primary_mapper = _class_to_mapper(base)if selectable not in (None, False) and flat:
raise sa_exc.ArgumentError("the 'flat' and 'selectable' arguments cannot be passed simultaneously to with_polymorphic()")(mappers, selectable) = primary_mapper._with_polymorphic_args(classes, selectable, innerjoin = innerjoin)# WARNING: Decompyle incomplete
)()
    entity = (lambda self = None: ent = self._weak_entity()# WARNING: Decompyle incomplete
)()
    is_aliased_class = True
    
    def _memoized_method___clause_element__(self = None):
        return self.selectable._annotate({
            'parentmapper': self.mapper,
            'parententity': self,
            'entity_namespace': self })._set_propagate_attrs({
            'compile_state_plugin': 'orm',
            'plugin_subject': self })

    entity_namespace = (lambda self = None: self.entity)()
    class_ = (lambda self = None: self.mapper.class_)()
    _path_registry = (lambda self = None: if self._use_mapper_path:
self.mapper._path_registryNone.per_mapper(self))()
    
    def __getstate__(self = None):
        return {
            'entity': self.entity,
            'mapper': self.mapper,
            'alias': self.selectable,
            'name': self.name,
            'adapt_on_names': self._adapt_on_names,
            'with_polymorphic_mappers': self.with_polymorphic_mappers,
            'with_polymorphic_discriminator': self.polymorphic_on,
            'base_alias': self._base_alias(),
            'use_mapper_path': self._use_mapper_path,
            'represents_outer_join': self.represents_outer_join,
            'nest_adapters': self._nest_adapters }

    
    def __setstate__(self = None, state = None):
        self.__init__(state['entity'], state['mapper'], state['alias'], state['name'], state['with_polymorphic_mappers'], state['with_polymorphic_discriminator'], state['base_alias'], state['use_mapper_path'], state['adapt_on_names'], state['represents_outer_join'], state['nest_adapters'])

    
    def _merge_with(self = None, other = None):
        primary_mapper = other.mapper
    # WARNING: Decompyle incomplete

    
    def _adapt_element(self = None, expr = None, key = None):
        pass
    # WARNING: Decompyle incomplete

    if TYPE_CHECKING:
        
        def _orm_adapt_element(self = None, obj = None, key = None):
            pass

    else:
        _orm_adapt_element = _adapt_element
    
    def _entity_for_mapper(self, mapper):
        self_poly = self.with_polymorphic_mappers
        if mapper in self_poly:
            if mapper is self.mapper:
                return self
            return None(self.entity, mapper.class_.__name__)._aliased_insp
        if None.isa(self.mapper):
            return self
        raise f'''mapper {mapper!s} doesn\'t correspond to {self!s}'''()

    
    def _memoized_attr__get_clause(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _memoized_attr__memoized_values(self):
        return { }

    
    def _memoized_attr__all_column_expressions(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _memo(self, key, callable_, *args, **kw):
        if key in self._memoized_values:
            return self._memoized_values[key]
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '<AliasedInsp at 0x%x; %s%s>' % (id(self), self.class_.__name__, with_poly)

    
    def __str__(self):
        pass
    # WARNING: Decompyle incomplete


AliasedInsp = <NODE:27>(AliasedInsp, 'AliasedInsp', ORMEntityColumnsClauseRole[_O], ORMFromClauseRole, HasCacheKey, InspectionAttr, MemoizedSlots, inspection.Inspectable['AliasedInsp[_O]'], Generic[_O])()

class _WrapUserEntity:
    '''A wrapper used within the loader_criteria lambda caller so that
    we can bypass declared_attr descriptors on unmapped mixins, which
    normally emit a warning for such use.

    might also be useful for other per-lambda instrumentations should
    the need arise.

    '''
    __slots__ = ('subject',)
    
    def __init__(self, subject):
        self.subject = subject

    __getattribute__ = (lambda self, name: decl_api = util.preloaded.orm.decl_apisubject = object.__getattribute__(self, 'subject')if name in subject.__dict__ and isinstance(subject.__dict__[name], decl_api.declared_attr):
subject.__dict__[name].fget(subject)None(subject, name))()


class LoaderCriteriaOption(CriteriaOption):
    '''Add additional WHERE criteria to the load for all occurrences of
    a particular entity.

    :class:`_orm.LoaderCriteriaOption` is invoked using the
    :func:`_orm.with_loader_criteria` function; see that function for
    details.

    .. versionadded:: 1.4

    '''
    __slots__ = ('root_entity', 'entity', 'deferred_where_criteria', 'where_criteria', '_where_crit_orig', 'include_aliases', 'propagate_to_loaders')
    _where_crit_orig: 'Any' = [
        ('root_entity', visitors.ExtendedInternalTraversal.dp_plain_obj),
        ('entity', visitors.ExtendedInternalTraversal.dp_has_cache_key),
        ('where_criteria', visitors.InternalTraversal.dp_clauseelement),
        ('include_aliases', visitors.InternalTraversal.dp_boolean),
        ('propagate_to_loaders', visitors.InternalTraversal.dp_boolean)]
    
    def __init__(self, entity_or_base, where_criteria = None, loader_only = None, include_aliases = None, propagate_to_loaders = (False, False, True, True), track_closure_variables = ('entity_or_base', '_EntityType[Any]', 'where_criteria', 'Union[_ColumnExpressionArgument[bool], Callable[[Any], _ColumnExpressionArgument[bool]]]', 'loader_only', 'bool', 'include_aliases', 'bool', 'propagate_to_loaders', 'bool', 'track_closure_variables', 'bool')):
        entity = cast('_InternalEntityType[Any]', inspection.inspect(entity_or_base, False))
    # WARNING: Decompyle incomplete

    _unreduce = (lambda cls, entity, where_criteria, include_aliases, propagate_to_loaders: LoaderCriteriaOption(entity, where_criteria, include_aliases = include_aliases, propagate_to_loaders = propagate_to_loaders))()
    
    def __reduce__(self):
        return (LoaderCriteriaOption._unreduce, (self.entity.class_ if self.entity else self.root_entity, self._where_crit_orig, self.include_aliases, self.propagate_to_loaders))

    
    def _all_mappers(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _should_include(self = None, compile_state = None):
        if compile_state.select_statement._annotations.get('for_loader_criteria', None) is self:
            return False

    
    def _resolve_where_criteria(self = None, ext_info = None):
        if self.deferred_where_criteria:
            crit = cast('ColumnElement[bool]', self.where_criteria._resolve_with_args(ext_info.entity))
        else:
            crit = self.where_criteria
    # WARNING: Decompyle incomplete

    
    def process_compile_state_replaced_entities(self = None, compile_state = None, mapper_entities = None):
        self.process_compile_state(compile_state)

    
    def process_compile_state(self = None, compile_state = None):
        '''Apply a modification to a given :class:`.CompileState`.'''
        self.get_global_criteria(compile_state.global_attributes)

    
    def get_global_criteria(self = None, attributes = None):
        for mp in self._all_mappers():
            load_criteria = attributes.setdefault(('additional_entity_criteria', mp), [])
            load_criteria.append(self)
            return None


inspection._inspects(AliasedClass)((lambda target: target._aliased_insp))
_inspect_mc = (lambda class_ = None: pass# WARNING: Decompyle incomplete
)()
GenericAlias = type(List[Any])
_inspect_generic_alias = (lambda class_ = None: origin = cast('Type[_O]', get_origin(class_))_inspect_mc(origin))()

def Bundle():
    '''Bundle'''
    __doc__ = 'A grouping of SQL expressions that are returned by a :class:`.Query`\n    under one namespace.\n\n    The :class:`.Bundle` essentially allows nesting of the tuple-based\n    results returned by a column-oriented :class:`_query.Query` object.\n    It also\n    is extensible via simple subclassing, where the primary capability\n    to override is that of how the set of expressions should be returned,\n    allowing post-processing as well as custom return types, without\n    involving ORM identity-mapped classes.\n\n    .. seealso::\n\n        :ref:`bundles`\n\n\n    '
    single_entity = False
    is_clause_element = False
    is_mapper = False
    is_aliased_class = False
    is_bundle = True
    _propagate_attrs: '_PropagateAttrsType' = util.immutabledict()
    exprs: 'List[_ColumnsClauseElement]' = util.EMPTY_SET
    
    def __init__(self = None, name = None, *exprs, **kw):
        '''Construct a new :class:`.Bundle`.

        e.g.::

            bn = Bundle("mybundle", MyClass.x, MyClass.y)

            for row in session.query(bn).filter(bn.c.x == 5).filter(bn.c.y == 4):
                print(row.mybundle.x, row.mybundle.y)

        :param name: name of the bundle.
        :param \\*exprs: columns or SQL expressions comprising the bundle.
        :param single_entity=False: if True, rows for this :class:`.Bundle`
         can be returned as a "single entity" outside of any enclosing tuple
         in the same manner as a mapped entity.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _gen_cache_key(self = None, anon_map = None, bindparams = None):
        pass
    # WARNING: Decompyle incomplete

    mapper = (lambda self = None: mp = self.exprs[0]._annotations.get('parentmapper', None)mp)()
    entity = (lambda self = None: ie = self.exprs[0]._annotations.get('parententity', None)ie)()
    c: 'ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]' = (lambda self = None: self.c)()
    
    def _clone(self, **kw):
        cloned = self.__class__.__new__(self.__class__)
        cloned.__dict__.update(self.__dict__)
        return cloned

    
    def __clause_element__(self):
        annotations = {
            'bundle': self,
            'entity_namespace': self }
        annotations.update(self._annotations)
        plugin_subject = self.exprs[0]._propagate_attrs.get('plugin_subject', self.entity)
    # WARNING: Decompyle incomplete

    clauses = (lambda self: self.__clause_element__().clauses)()
    
    def label(self, name):
        '''Provide a copy of this :class:`.Bundle` passing a new label.'''
        cloned = self._clone()
        cloned.name = name
        return cloned

    
    def create_row_processor(self = None, query = None, procs = property, labels = ('query', 'Select[Any]', 'procs', 'Sequence[Callable[[Row[Any]], Any]]', 'labels', 'Sequence[str]', 'return', 'Callable[[Row[Any]], Any]')):
        '''Produce the "row processing" function for this :class:`.Bundle`.

        May be overridden by subclasses to provide custom behaviors when
        results are fetched. The method is passed the statement object and a
        set of "row processor" functions at query execution time; these
        processor functions when given a result row will return the individual
        attribute value, which can then be adapted into any kind of return data
        structure.

        The example below illustrates replacing the usual :class:`.Row`
        return structure with a straight Python dictionary::

            from sqlalchemy.orm import Bundle


            class DictBundle(Bundle):
                def create_row_processor(self, query, procs, labels):
                    "Override create_row_processor to return values as dictionaries"

                    def proc(row):
                        return dict(zip(labels, (proc(row) for proc in procs)))

                    return proc

        A result from the above :class:`_orm.Bundle` will return dictionary
        values::

            bn = DictBundle("mybundle", MyClass.data1, MyClass.data2)
            for row in session.execute(select(bn)).where(bn.c.data1 == "d1"):
                print(row.mybundle["data1"], row.mybundle["data2"])

        '''
        pass
    # WARNING: Decompyle incomplete


Bundle = <NODE:27>(Bundle, 'Bundle', ORMColumnsClauseRole[_T], SupportsCloneAnnotations, MemoizedHasCacheKey, inspection.Inspectable['Bundle[_T]'], InspectionAttr)()

def _orm_annotate(element = None, exclude = None):
    '''Deep copy the given ClauseElement, annotating each element with the
    "_orm_adapt" flag.

    Elements within the exclude collection will be cloned but not annotated.

    '''
    return sql_util._deep_annotate(element, {
        '_orm_adapt': True }, exclude)


def _orm_deannotate(element = None):
    '''Remove annotations that link a column to a particular mapping.

    Note this doesn\'t affect "remote" and "foreign" annotations
    passed by the :func:`_orm.foreign` and :func:`_orm.remote`
    annotators.

    '''
    return sql_util._deep_deannotate(element, values = ('_orm_adapt', 'parententity'))


def _orm_full_deannotate(element = None):
    return sql_util._deep_deannotate(element)


class _ORMJoin(expression.Join):
    '''Extend Join to support ORM constructs as input.'''
    __visit_name__ = expression.Join.__visit_name__
    inherit_cache = True
    
    def __init__(self, left, right, onclause, isouter = None, full = None, _left_memo = None, _right_memo = (None, False, False, None, None, ()), _extra_criteria = ('left', '_FromClauseArgument', 'right', '_FromClauseArgument', 'onclause', 'Optional[_OnClauseArgument]', 'isouter', 'bool', 'full', 'bool', '_left_memo', 'Optional[Any]', '_right_memo', 'Optional[Any]', '_extra_criteria', 'Tuple[ColumnElement[bool], ...]')):
        left_info = cast('Union[FromClause, _InternalEntityType[Any]]', inspection.inspect(left))
        right_info = cast('Union[FromClause, _InternalEntityType[Any]]', inspection.inspect(right))
        adapt_to = right_info.selectable
        self._left_memo = _left_memo
        self._right_memo = _right_memo
    # WARNING: Decompyle incomplete

    
    def _splice_into_center(self, other):
        '''Splice a join into the center.

        Given join(a, b) and join(b, c), return join(a, b).join(c)

        '''
        leftmost = other
    # WARNING: Decompyle incomplete

    
    def join(self = None, right = None, onclause = None, isouter = (None, False, False), full = ('right', '_FromClauseArgument', 'onclause', 'Optional[_OnClauseArgument]', 'isouter', 'bool', 'full', 'bool', 'return', '_ORMJoin')):
        return _ORMJoin(self, right, onclause, full = full, isouter = isouter)

    
    def outerjoin(self = None, right = None, onclause = None, full = (None, False)):
        return _ORMJoin(self, right, onclause, isouter = True, full = full)



def with_parent(instance = None, prop = None, from_entity = None):
    '''Create filtering criterion that relates this query\'s primary entity
    to the given related instance, using established
    :func:`_orm.relationship()`
    configuration.

    E.g.::

        stmt = select(Address).where(with_parent(some_user, User.addresses))

    The SQL rendered is the same as that rendered when a lazy loader
    would fire off from the given parent on that attribute, meaning
    that the appropriate state is taken from the parent object in
    Python without the need to render joins to the parent table
    in the rendered statement.

    The given property may also make use of :meth:`_orm.PropComparator.of_type`
    to indicate the left side of the criteria::


        a1 = aliased(Address)
        a2 = aliased(Address)
        stmt = select(a1, a2).where(with_parent(u1, User.addresses.of_type(a2)))

    The above use is equivalent to using the
    :func:`_orm.with_parent.from_entity` argument::

        a1 = aliased(Address)
        a2 = aliased(Address)
        stmt = select(a1, a2).where(
            with_parent(u1, User.addresses, from_entity=a2)
        )

    :param instance:
      An instance which has some :func:`_orm.relationship`.

    :param property:
      Class-bound attribute, which indicates
      what relationship from the instance should be used to reconcile the
      parent/child relationship.

    :param from_entity:
      Entity in which to consider as the left side.  This defaults to the
      "zero" entity of the :class:`_query.Query` itself.

      .. versionadded:: 1.2

    '''
    if isinstance(prop, str):
        raise sa_exc.ArgumentError('with_parent() accepts class-bound mapped attributes, not strings')
# WARNING: Decompyle incomplete


def has_identity(object_ = None):
    '''Return True if the given object has a database
    identity.

    This typically corresponds to the object being
    in either the persistent or detached state.

    .. seealso::

        :func:`.was_deleted`

    '''
    state = attributes.instance_state(object_)
    return state.has_identity


def was_deleted(object_ = None):
    '''Return True if the given object was deleted
    within a session flush.

    This is regardless of whether or not the object is
    persistent or detached.

    .. seealso::

        :attr:`.InstanceState.was_deleted`

    '''
    state = attributes.instance_state(object_)
    return state.was_deleted


def _entity_corresponds_to(given = None, entity = None):
    """determine if 'given' corresponds to 'entity', in terms
    of an entity passed to Query that would match the same entity
    being referred to elsewhere in the query.

    """
    if insp_is_aliased_class(entity):
        if insp_is_aliased_class(given) and entity._base_alias() is given._base_alias():
            return True
        return None
    if None(given):
        if given._use_mapper_path:
            return entity in given.with_polymorphic_mappers
        return None is given
# WARNING: Decompyle incomplete


def _entity_corresponds_to_use_path_impl(given = None, entity = None):
