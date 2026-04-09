# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: collections.pyc (Python 3.11)

'''Support for collections of mapped entities.

The collections package supplies the machinery used to inform the ORM of
collection membership changes.  An instrumentation via decoration approach is
used, allowing arbitrary types (including built-ins) to be used as entity
collections without requiring inheritance from a base class.

Instrumentation decoration relays membership change events to the
:class:`.CollectionAttributeImpl` that is currently managing the collection.
The decorators observe function call arguments and return values, tracking
entities entering or leaving the collection.  Two decorator approaches are
provided.  One is a bundle of generic decorators that map function arguments
and return values to events::

  from sqlalchemy.orm.collections import collection


  class MyClass:
      # ...

      @collection.adds(1)
      def store(self, item):
          self.data.append(item)

      @collection.removes_return()
      def pop(self):
          return self.data.pop()

The second approach is a bundle of targeted decorators that wrap appropriate
append and remove notifiers around the mutation methods present in the
standard Python ``list``, ``set`` and ``dict`` interfaces.  These could be
specified in terms of generic decorator recipes, but are instead hand-tooled
for increased efficiency.  The targeted decorators occasionally implement
adapter-like behavior, such as mapping bulk-set methods (``extend``,
``update``, ``__setslice__``, etc.) into the series of atomic mutation events
that the ORM requires.

The targeted decorators are used internally for automatic instrumentation of
entity collection classes.  Every collection class goes through a
transformation process roughly like so:

1. If the class is a built-in, substitute a trivial sub-class
2. Is this class already instrumented?
3. Add in generic decorators
4. Sniff out the collection interface through duck-typing
5. Add targeted decoration to any undecorated interface method

This process modifies the class at runtime, decorating methods and adding some
bookkeeping properties.  This isn\'t possible (or desirable) for built-in
classes like ``list``, so trivial sub-classes are substituted to hold
decoration::

  class InstrumentedList(list):
      pass

Collection classes can be specified in ``relationship(collection_class=)`` as
types or a function that returns an instance.  Collection classes are
inspected and instrumented during the mapper compilation phase.  The
collection_class callable will be executed once to produce a specimen
instance, and the type of that specimen will be instrumented.  Functions that
return built-in types like ``lists`` will be adapted to produce instrumented
instances.

When extending a known type like ``list``, additional decorations are not
generally not needed.  Odds are, the extension method will delegate to a
method that\'s already instrumented.  For example::

  class QueueIsh(list):
      def push(self, item):
          self.append(item)

      def shift(self):
          return self.pop(0)

There\'s no need to decorate these methods.  ``append`` and ``pop`` are already
instrumented as part of the ``list`` interface.  Decorating them would fire
duplicate events, which should be avoided.

The targeted decoration tries not to rely on other methods in the underlying
collection class, but some are unavoidable.  Many depend on \'read\' methods
being present to properly instrument a \'write\', for example, ``__setitem__``
needs ``__getitem__``.  "Bulk" methods like ``update`` and ``extend`` may also
reimplemented in terms of atomic appends and removes, so the ``extend``
decoration will actually perform many ``append`` operations and not call the
underlying method at all.

Tight control over bulk operation and the firing of events is also possible by
implementing the instrumentation internally in your methods.  The basic
instrumentation package works under the general assumption that collection
mutation will not raise unusual exceptions.  If you want to closely
orchestrate append and remove events with exception management, internal
instrumentation may be the answer.  Within your method,
``collection_adapter(self)`` will retrieve an object that you can use for
explicit control over triggering append and remove events.

The owning object and :class:`.CollectionAttributeImpl` are also reachable
through the adapter, allowing for some very sophisticated behavior.

'''
from __future__ import annotations
import operator
import threading
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Collection
from typing import Dict
from typing import Iterable
from typing import List
from typing import NoReturn
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import weakref
from base import NO_KEY
from  import exc as sa_exc
from  import util
from sql.base import NO_ARG
from util.compat import inspect_getfullargspec
from util.typing import Protocol
if typing.TYPE_CHECKING:
    from attributes import AttributeEventToken
    from attributes import CollectionAttributeImpl
    attribute_keyed_dict = attribute_keyed_dict
    import mapped_collection
    column_keyed_dict = column_keyed_dict
    import mapped_collection
    keyfunc_mapping = keyfunc_mapping
    import mapped_collection
    KeyFuncDict = KeyFuncDict
    import mapped_collection
    from state import InstanceState
__all__ = [
    'collection',
    'collection_adapter',
    'keyfunc_mapping',
    'column_keyed_dict',
    'attribute_keyed_dict',
    'KeyFuncDict',
    'mapped_collection',
    'column_mapped_collection',
    'attribute_mapped_collection',
    'MappedCollection']
__instrumentation_mutex = threading.Lock()
_CollectionFactoryType = Callable[([], '_AdaptedCollectionProtocol')]
_T = TypeVar('_T', bound = Any)
_KT = TypeVar('_KT', bound = Any)
_VT = TypeVar('_VT', bound = Any)
_COL = TypeVar('_COL', bound = 'Collection[Any]')
_FN = TypeVar('_FN', bound = 'Callable[..., Any]')

class _CollectionConverterProtocol(Protocol):
    
    def __call__(self = None, collection = None):
        pass



class _AdaptedCollectionProtocol(Protocol):
    _sa_converter: '_CollectionConverterProtocol' = '_AdaptedCollectionProtocol'


class collection:
    '''Decorators for entity collection classes.

    The decorators fall into two groups: annotations and interception recipes.

    The annotating decorators (appender, remover, iterator, converter,
    internally_instrumented) indicate the method\'s purpose and take no
    arguments.  They are not written with parens::

        @collection.appender
        def append(self, append): ...

    The recipe decorators all require parens, even those that take no
    arguments::

        @collection.adds("entity")
        def insert(self, position, entity): ...


        @collection.removes_return()
        def popitem(self): ...

    '''
    appender = (lambda fn: fn._sa_instrument_role = 'appender'fn)()
    remover = (lambda fn: fn._sa_instrument_role = 'remover'fn)()
    iterator = (lambda fn: fn._sa_instrument_role = 'iterator'fn)()
    internally_instrumented = (lambda fn: fn._sa_instrumented = Truefn)()
    converter = (lambda fn: fn._sa_instrument_role = 'converter'fn)()()
    adds = (lambda arg = staticmethod: pass# WARNING: Decompyle incomplete
)()
    replaces = (lambda arg: pass# WARNING: Decompyle incomplete
)()
    removes = (lambda arg: pass# WARNING: Decompyle incomplete
)()
    removes_return = (lambda : 
def decorator(fn):
fn._sa_instrument_after = 'fire_remove_event'fndecorator)()


class CollectionAdapter:
    '''Bridges between the ORM and arbitrary Python collections.

    Proxies base-level collection operations (append, remove, iterate)
    to the underlying Python collection, and emits add/remove events for
    entities entering or leaving the collection.

    The ORM uses :class:`.CollectionAdapter` exclusively for interaction with
    entity collections.


    '''
    empty: 'bool' = ('attr', '_key', '_data', 'owner_state', '_converter', 'invalidated', 'empty')
    
    def __init__(self = None, attr = None, owner_state = None, data = ('attr', 'CollectionAttributeImpl', 'owner_state', 'InstanceState[Any]', 'data', '_AdaptedCollectionProtocol')):
        self.attr = attr
        self._key = attr.key
        self._data = weakref.ref(data)
        self.owner_state = owner_state
        data._sa_adapter = self
        self._converter = data._sa_converter
        self.invalidated = False
        self.empty = False

    
    def _warn_invalidated(self = None):
        util.warn('This collection has been invalidated.')

    data = (lambda self = None: self._data())()
    _referenced_by_owner = (lambda self = None: self.owner_state.dict[self._key] is self._data())()
    
    def bulk_appender(self):
        return self._data()._sa_appender

    
    def append_with_event(self = None, item = None, initiator = None):
        '''Add an entity to the collection, firing mutation events.'''
        self._data()._sa_appender(item, _sa_initiator = initiator)

    
    def _set_empty(self, user_data):
        pass
    # WARNING: Decompyle incomplete

    
    def _reset_empty(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _refuse_empty(self = None):
        raise sa_exc.InvalidRequestError("This is a special 'empty' collection which cannot accommodate internal mutation operations")

    
    def append_without_event(self = None, item = None):
        '''Add or restore an entity to the collection, firing no events.'''
        if self.empty:
            self._refuse_empty()
        self._data()._sa_appender(item, _sa_initiator = False)

    
    def append_multiple_without_event(self = None, items = None):
        '''Add or restore an entity to the collection, firing no events.'''
        if self.empty:
            self._refuse_empty()
        appender = self._data()._sa_appender
        for item in items:
            appender(item, _sa_initiator = False)
            return None

    
    def bulk_remover(self):
        return self._data()._sa_remover

    
    def remove_with_event(self = None, item = None, initiator = None):
        '''Remove an entity from the collection, firing mutation events.'''
        self._data()._sa_remover(item, _sa_initiator = initiator)

    
    def remove_without_event(self = None, item = None):
        '''Remove an entity from the collection, firing no events.'''
        if self.empty:
            self._refuse_empty()
        self._data()._sa_remover(item, _sa_initiator = False)

    
    def clear_with_event(self = None, initiator = None):
        '''Empty the collection, firing a mutation event for each entity.'''
        if self.empty:
            self._refuse_empty()
        remover = self._data()._sa_remover
        for item in list(self):
            remover(item, _sa_initiator = initiator)
            return None

    
    def clear_without_event(self = None):
        '''Empty the collection, firing no events.'''
        if self.empty:
            self._refuse_empty()
        remover = self._data()._sa_remover
        for item in list(self):
            remover(item, _sa_initiator = False)
            return None

    
    def __iter__(self):
        '''Iterate over entities in the collection.'''
        return iter(self._data()._sa_iterator())

    
    def __len__(self):
        '''Count entities in the collection.'''
        return len(list(self._data()._sa_iterator()))

    
    def __bool__(self):
        return True

    
    def _fire_append_wo_mutation_event_bulk(self, items, initiator, key = (None, NO_KEY)):
        if not items:
            return None
        if None is not False:
            if self.invalidated:
                self._warn_invalidated()
            if self.empty:
                self._reset_empty()
            for item in items:
                self.attr.fire_append_wo_mutation_event(self.owner_state, self.owner_state.dict, item, initiator, key)
                return None
                return None

    
    def fire_append_wo_mutation_event(self, item, initiator, key = (None, NO_KEY)):
        '''Notify that a entity is entering the collection but is already
        present.


        Initiator is a token owned by the InstrumentedAttribute that
        initiated the membership mutation, and should be left as None
        unless you are passing along an initiator value from a chained
        operation.

        .. versionadded:: 1.4.15

        '''
        if initiator is not False:
            if self.invalidated:
                self._warn_invalidated()
            if self.empty:
                self._reset_empty()
            return self.attr.fire_append_wo_mutation_event(self.owner_state, self.owner_state.dict, item, initiator, key)

    
    def fire_append_event(self, item, initiator, key = (None, NO_KEY)):
        '''Notify that a entity has entered the collection.

        Initiator is a token owned by the InstrumentedAttribute that
        initiated the membership mutation, and should be left as None
        unless you are passing along an initiator value from a chained
        operation.

        '''
        if initiator is not False:
            if self.invalidated:
                self._warn_invalidated()
            if self.empty:
                self._reset_empty()
            return self.attr.fire_append_event(self.owner_state, self.owner_state.dict, item, initiator, key)

    
    def _fire_remove_event_bulk(self, items, initiator, key = (None, NO_KEY)):
        if not items:
            return None
        if None is not False:
            if self.invalidated:
                self._warn_invalidated()
            if self.empty:
                self._reset_empty()
            for item in items:
                self.attr.fire_remove_event(self.owner_state, self.owner_state.dict, item, initiator, key)
                return None
                return None

    
    def fire_remove_event(self, item, initiator, key = (None, NO_KEY)):
        '''Notify that a entity has been removed from the collection.

        Initiator is the InstrumentedAttribute that initiated the membership
        mutation, and should be left as None unless you are passing along
        an initiator value from a chained operation.

        '''
        if initiator is not False:
            if self.invalidated:
                self._warn_invalidated()
            if self.empty:
                self._reset_empty()
            self.attr.fire_remove_event(self.owner_state, self.owner_state.dict, item, initiator, key)
            return None

    
    def fire_pre_remove_event(self, initiator, key = (None, NO_KEY)):
        '''Notify that an entity is about to be removed from the collection.

        Only called if the entity cannot be removed after calling
        fire_remove_event().

        '''
        if self.invalidated:
            self._warn_invalidated()
        self.attr.fire_pre_remove_event(self.owner_state, self.owner_state.dict, initiator = initiator, key = key)

    
    def __getstate__(self):
        return {
            'key': self._key,
            'owner_state': self.owner_state,
            'owner_cls': self.owner_state.class_,
            'data': self.data,
            'invalidated': self.invalidated,
            'empty': self.empty }

    
    def __setstate__(self, d):
        self._key = d['key']
        self.owner_state = d['owner_state']
        self._data = weakref.ref(d['data'])
        self._converter = d['data']._sa_converter
        d['data']._sa_adapter = self
        self.invalidated = d['invalidated']
        self.attr = getattr(d['owner_cls'], self._key).impl
        self.empty = d.get('empty', False)



def bulk_replace(values, existing_adapter, new_adapter, initiator = (None,)):
    '''Load a new collection, firing events based on prior like membership.

    Appends instances in ``values`` onto the ``new_adapter``. Events will be
    fired for any instance not present in the ``existing_adapter``.  Any
    instances in ``existing_adapter`` not present in ``values`` will have
    remove events fired upon them.

    :param values: An iterable of collection member instances

    :param existing_adapter: A :class:`.CollectionAdapter` of
     instances to be replaced

    :param new_adapter: An empty :class:`.CollectionAdapter`
     to load with ``values``


    '''
    pass
# WARNING: Decompyle incomplete


def prepare_instrumentation(factory = None):
    '''Prepare a callable for future use as a collection class factory.

    Given a collection class factory (either a type or no-arg callable),
    return another factory that will produce compatible instances when
    called.

    This function is responsible for converting collection_class=list
    into the run-time behavior of collection_class=InstrumentedList.

    '''
    if factory in __canned_instrumentation:
        impl_factory = __canned_instrumentation[factory]
    else:
        impl_factory = cast(_CollectionFactoryType, factory)
    cls = type(impl_factory())
    if cls in __canned_instrumentation:
        impl_factory = __canned_instrumentation[cls]
        cls = type(impl_factory())
    if __instrumentation_mutex.acquire():
        
        try:
            if getattr(cls, '_sa_instrumented', None) != id(cls):
                _instrument_class(cls)
            __instrumentation_mutex.release()
        except:
            __instrumentation_mutex.release()

        return impl_factory


def _instrument_class(cls):
    '''Modify methods in a class and install instrumentation.'''
    if cls.__module__ == '__builtin__':
        raise sa_exc.ArgumentError('Can not instrument a built-in type. Use a subclass, even a trivial one.')
    (roles, methods) = _locate_roles_and_methods(cls)
    _setup_canned_roles(cls, roles, methods)
    _assert_required_roles(cls, roles, methods)
    _set_collection_attributes(cls, roles, methods)


def _locate_roles_and_methods(cls):
    '''search for _sa_instrument_role-decorated methods in
    method resolution order, assign to roles.

    '''
    roles = { }
    methods = { }
# WARNING: Decompyle incomplete


def _setup_canned_roles(cls, roles, methods):
    '''see if this class has "canned" roles based on a known
    collection type (dict, set, list).  Apply those roles
    as needed to the "roles" dictionary, and also
    prepare "decorator" methods

    '''
    collection_type = util.duck_type_collection(cls)
# WARNING: Decompyle incomplete


def _assert_required_roles(cls, roles, methods):
    '''ensure all roles are present, and apply implicit instrumentation if
    needed

    '''
    if not 'appender' not in roles or hasattr(cls, roles['appender']):
        raise sa_exc.ArgumentError('Type %s must elect an appender method to be a collection class' % cls.__name__)
    if not roles['appender'] not in methods and hasattr(getattr(cls, roles['appender']), '_sa_instrumented'):
        methods[roles['appender']] = ('fire_append_event', 1, None)
    if not 'remover' not in roles or hasattr(cls, roles['remover']):
        raise sa_exc.ArgumentError('Type %s must elect a remover method to be a collection class' % cls.__name__)
    if not roles['remover'] not in methods and hasattr(getattr(cls, roles['remover']), '_sa_instrumented'):
        methods[roles['remover']] = ('fire_remove_event', 1, None)
    if not 'iterator' not in roles or hasattr(cls, roles['iterator']):
        raise sa_exc.ArgumentError('Type %s must elect an iterator method to be a collection class' % cls.__name__)


def _set_collection_attributes(cls, roles, methods):
    '''apply ad-hoc instrumentation from decorators, class-level defaults
    and implicit role declarations

    '''
    for before, argument, after in methods.items():
        setattr(cls, method_name, _instrument_membership_mutator(getattr(cls, method_name), before, argument, after))
        for role, method_name in roles.items():
            setattr(cls, '_sa_%s' % role, getattr(cls, method_name))
            cls._sa_adapter = None
            if not hasattr(cls, '_sa_converter'):
                cls._sa_converter = None
    cls._sa_instrumented = id(cls)


def _instrument_membership_mutator(method, before, argument, after):
    '''Route method args and/or return value through the collection
    adapter.'''
    pass
# WARNING: Decompyle incomplete


def __set_wo_mutation(collection, item, _sa_initiator = (None,)):
    '''Run set wo mutation events.

    The collection is not mutated.

    '''
    if _sa_initiator is not False:
        executor = collection._sa_adapter
        if executor:
            executor.fire_append_wo_mutation_event(item, _sa_initiator, key = None)
            return None
        return None


def __set(collection, item, _sa_initiator, key):
    '''Run set events.

    This event always occurs before the collection is actually mutated.

    '''
    if _sa_initiator is not False:
        executor = collection._sa_adapter
        if executor:
            item = executor.fire_append_event(item, _sa_initiator, key = key)
    return item


def __del(collection, item, _sa_initiator, key):
    '''Run del events.

    This event occurs before the collection is actually mutated, *except*
    in the case of a pop operation, in which case it occurs afterwards.
    For pop operations, the __before_pop hook is called before the
    operation occurs.

    '''
    if _sa_initiator is not False:
        executor = collection._sa_adapter
        if executor:
            executor.fire_remove_event(item, _sa_initiator, key = key)
            return None
        return None


def __before_pop(collection, _sa_initiator = (None,)):
    '''An event which occurs on a before a pop() operation occurs.'''
    executor = collection._sa_adapter
    if executor:
        executor.fire_pre_remove_event(_sa_initiator)
        return None


def _list_decorators():
    '''Tailored instrumentation wrappers for any list-like class.'''
    pass
# WARNING: Decompyle incomplete


def _dict_decorators():
    '''Tailored instrumentation wrappers for any dict-like mapping class.'''
    pass
# WARNING: Decompyle incomplete

_set_binop_bases = (set, frozenset)

def _set_binops_check_strict(self = None, obj = None):
    '''Allow only set, frozenset and self.__class__-derived
    objects in binops.'''
    return isinstance(obj, _set_binop_bases + (self.__class__,))


def _set_binops_check_loose(self = None, obj = None):
