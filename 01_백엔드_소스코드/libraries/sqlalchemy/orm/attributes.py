# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: attributes.pyc (Python 3.11)

"""Defines instrumentation for class attributes and their interaction
with instances.

This module is usually not directly visible to user applications, but
defines a large part of the ORM's interactivity.


"""
from __future__ import annotations
import dataclasses
import operator
from typing import Any
from typing import Callable
from typing import cast
from typing import ClassVar
from typing import Dict
from typing import Iterable
from typing import List
from typing import NamedTuple
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import collections
from  import exc as orm_exc
from  import interfaces
from _typing import insp_is_aliased_class
from base import _DeclarativeMapped
from base import ATTR_EMPTY
from base import ATTR_WAS_SET
from base import CALLABLES_OK
from base import DEFERRED_HISTORY_LOAD
from base import INCLUDE_PENDING_MUTATIONS
from base import INIT_OK
from base import instance_dict
from base import instance_state
from base import instance_str
from base import LOAD_AGAINST_COMMITTED
from base import LoaderCallableStatus
from base import manager_of_class
from base import Mapped
from base import NEVER_SET
from base import NO_AUTOFLUSH
from base import NO_CHANGE
from base import NO_KEY
from base import NO_RAISE
from base import NO_VALUE
from base import NON_PERSISTENT_OK
from base import opt_manager_of_class
from base import PASSIVE_CLASS_MISMATCH
from base import PASSIVE_NO_FETCH
from base import PASSIVE_NO_FETCH_RELATED
from base import PASSIVE_NO_INITIALIZE
from base import PASSIVE_NO_RESULT
from base import PASSIVE_OFF
from base import PASSIVE_ONLY_PERSISTENT
from base import PASSIVE_RETURN_NO_VALUE
from base import PassiveFlag
from base import RELATED_OBJECT_OK
from base import SQL_OK
from base import SQLORMExpression
from base import state_str
from  import event
from  import exc
from  import inspection
from  import util
from event import dispatcher
from event import EventTarget
from sql import base as sql_base
from sql import cache_key
from sql import coercions
from sql import roles
from sql import visitors
from sql.cache_key import HasCacheKey
from sql.visitors import _TraverseInternalsType
from sql.visitors import InternalTraversal
from util.typing import Literal
from util.typing import Self
from util.typing import TypeGuard
if TYPE_CHECKING:
    from _typing import _EntityType
    from _typing import _ExternalEntityType
    from _typing import _InstanceDict
    from _typing import _InternalEntityType
    from _typing import _LoaderCallable
    from _typing import _O
    from collections import _AdaptedCollectionProtocol
    from collections import CollectionAdapter
    from interfaces import MapperProperty
    from relationships import RelationshipProperty
    from state import InstanceState
    from util import AliasedInsp
    from writeonly import WriteOnlyAttributeImpl
    from event.base import _Dispatch
    from sql._typing import _ColumnExpressionArgument
    from sql._typing import _DMLColumnArgument
    from sql._typing import _InfoType
    from sql._typing import _PropagateAttrsType
    from sql.annotation import _AnnotationDict
    from sql.elements import ColumnElement
    from sql.elements import Label
    from sql.operators import OperatorType
    from sql.selectable import FromClause
_T = TypeVar('_T')
_T_co = TypeVar('_T_co', bound = Any, covariant = True)
_AllPendingType = Sequence[Tuple[(Optional['InstanceState[Any]'], Optional[object])]]
_UNKNOWN_ATTR_KEY = object()

def QueryableAttribute():
    '''QueryableAttribute'''
    __doc__ = 'Base class for :term:`descriptor` objects that intercept\n    attribute events on behalf of a :class:`.MapperProperty`\n    object.  The actual :class:`.MapperProperty` is accessible\n    via the :attr:`.QueryableAttribute.property`\n    attribute.\n\n\n    .. seealso::\n\n        :class:`.InstrumentedAttribute`\n\n        :class:`.MapperProperty`\n\n        :attr:`_orm.Mapper.all_orm_descriptors`\n\n        :attr:`_orm.Mapper.attrs`\n    '
    __slots__ = ('class_', 'key', 'impl', 'comparator', 'property', 'parent', 'expression', '_of_type', '_extra_criteria', '_slots_dispatch', '_propagate_attrs', '_doc')
    _doc: 'Optional[str]' = True
    __visit_name__ = 'orm_instrumented_attribute'
    
    def __init__(self, class_, key, parententity = None, comparator = None, impl = None, of_type = (None, None, ()), extra_criteria = ('class_', '_ExternalEntityType[_O]', 'key', 'str', 'parententity', '_InternalEntityType[_O]', 'comparator', 'interfaces.PropComparator[_T_co]', 'impl', 'Optional[AttributeImpl]', 'of_type', 'Optional[_InternalEntityType[Any]]', 'extra_criteria', 'Tuple[ColumnElement[bool], ...]')):
        self.class_ = class_
        self.key = key
        self._parententity = parententity
        self.parent = parententity
        self.impl = impl
    # WARNING: Decompyle incomplete

    _cache_key_traversal = [
        ('key', visitors.ExtendedInternalTraversal.dp_string),
        ('_parententity', visitors.ExtendedInternalTraversal.dp_multi),
        ('_of_type', visitors.ExtendedInternalTraversal.dp_multi),
        ('_extra_criteria', visitors.InternalTraversal.dp_clauseelement_list)]
    
    def __reduce__(self = None):
        return (_queryable_attribute_unreduce, (self.key, self._parententity.mapper.class_, self._parententity, self._parententity.entity))

    _impl_uses_objects = (lambda self = None: self.impl.uses_objects)()
    
    def get_history(self = None, instance = None, passive = None):
        return self.impl.get_history(instance_state(instance), instance_dict(instance), passive)

    expression: 'ColumnElement[_T_co]' = (lambda self = None: self.comparator.info)()
    
    def _memoized_attr_expression(self = None):
        entity_namespace = self._entity_namespace
    # WARNING: Decompyle incomplete

    
    def _memoized_attr__propagate_attrs(self = None):
        return util.immutabledict({
            'compile_state_plugin': 'orm',
            'plugin_subject': self._parentmapper })

    _entity_namespace = (lambda self = None: self._parententity)()
    _annotations = (lambda self = None: self.__clause_element__()._annotations)()
    
    def __clause_element__(self = None):
        return self.expression

    _from_objects = (lambda self = None: self.expression._from_objects)()
    
    def _bulk_update_tuples(self = None, value = None):
        '''Return setter tuples for a bulk UPDATE.'''
        return self.comparator._bulk_update_tuples(value)

    
    def adapt_to_entity(self = None, adapt_to_entity = None):
        pass
    # WARNING: Decompyle incomplete

    
    def of_type(self = None, entity = None):
        return QueryableAttribute(self.class_, self.key, self._parententity, impl = self.impl, comparator = self.comparator.of_type(entity), of_type = inspection.inspect(entity), extra_criteria = self._extra_criteria)

    
    def and_(self = None, *clauses):
        pass
    # WARNING: Decompyle incomplete

    
    def _clone(self = None, **kw):
        return QueryableAttribute(self.class_, self.key, self._parententity, impl = self.impl, comparator = self.comparator, of_type = self._of_type, extra_criteria = self._extra_criteria)

    
    def label(self = None, name = None):
        return self.__clause_element__().label(name)

    
    def operate(self = None, op = None, *other, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def reverse_operate(self = None, op = None, other = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def hasparent(self = None, state = None, optimistic = None):
        return self.impl.hasparent(state, optimistic = optimistic) is not False

    
    def _column_strategy_attrs(self = None):
        return (self,)

    
    def __getattr__(self = None, key = None):
        
        try:
            return util.MemoizedSlots.__getattr__(self, key)
        except AttributeError:
            pass

        
        try:
            return getattr(self.comparator, key)
        except AttributeError:
            err = None
            raise AttributeError(f'''Neither {type(self).__name__!r} object nor {type(self.comparator).__name__!r} object associated with {self!s} has an attribute {key!r}'''), err
            err = None
            del err


    
    def __str__(self = None):
        return f'''{self.class_.__name__}.{self.key}'''

    
    def _memoized_attr_property(self = None):
        return self.comparator.property


QueryableAttribute = <NODE:27>(QueryableAttribute, 'QueryableAttribute', _DeclarativeMapped[_T_co], SQLORMExpression[_T_co], interfaces.InspectionAttr, interfaces.PropComparator[_T_co], roles.JoinTargetRole, roles.OnClauseRole, sql_base.Immutable, cache_key.SlotsMemoizedHasCacheKey, util.MemoizedSlots, EventTarget)()

def _queryable_attribute_unreduce(key = None, mapped_class = None, parententity = inspection._self_inspects, entity = ('key', 'str', 'mapped_class', 'Type[_O]', 'parententity', '_InternalEntityType[_O]', 'entity', '_ExternalEntityType[Any]', 'return', 'Any')):
    if insp_is_aliased_class(parententity):
        return entity._get_from_serialized(key, mapped_class, parententity)
    return None(entity, key)


def InstrumentedAttribute():
    '''InstrumentedAttribute'''
    pass
# WARNING: Decompyle incomplete

InstrumentedAttribute = <NODE:27>(InstrumentedAttribute, 'InstrumentedAttribute', QueryableAttribute[_T_co])
AdHocHasEntityNamespace = <NODE:12>()

def create_proxied_attribute(descriptor = None):
    '''Create an QueryableAttribute / user descriptor hybrid.

    Returns a new QueryableAttribute type that delegates descriptor
    behavior and getattr() to the given descriptor.
    '''
    pass
# WARNING: Decompyle incomplete

OP_REMOVE = util.symbol('REMOVE')
OP_APPEND = util.symbol('APPEND')
OP_REPLACE = util.symbol('REPLACE')
OP_BULK_REPLACE = util.symbol('BULK_REPLACE')
OP_MODIFIED = util.symbol('MODIFIED')

class AttributeEventToken:
    '''A token propagated throughout the course of a chain of attribute
    events.

    Serves as an indicator of the source of the event and also provides
    a means of controlling propagation across a chain of attribute
    operations.

    The :class:`.Event` object is sent as the ``initiator`` argument
    when dealing with events such as :meth:`.AttributeEvents.append`,
    :meth:`.AttributeEvents.set`,
    and :meth:`.AttributeEvents.remove`.

    The :class:`.Event` object is currently interpreted by the backref
    event handlers, and is used to control the propagation of operations
    across two mutually-dependent attributes.

    .. versionchanged:: 2.0  Changed the name from ``AttributeEvent``
       to ``AttributeEventToken``.

    :attribute impl: The :class:`.AttributeImpl` which is the current event
     initiator.

    :attribute op: The symbol :attr:`.OP_APPEND`, :attr:`.OP_REMOVE`,
     :attr:`.OP_REPLACE`, or :attr:`.OP_BULK_REPLACE`, indicating the
     source operation.

    '''
    __slots__ = ('impl', 'op', 'parent_token')
    
    def __init__(self = None, attribute_impl = None, op = None):
        self.impl = attribute_impl
        self.op = op
        self.parent_token = self.impl.parent_token

    
    def __eq__(self, other):
