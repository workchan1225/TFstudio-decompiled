# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: instrumentation.pyc (Python 3.11)

"""Defines SQLAlchemy's system of class instrumentation.

This module is usually not directly visible to user applications, but
defines a large part of the ORM's interactivity.

instrumentation.py deals with registration of end-user classes
for state tracking.   It interacts closely with state.py
and attributes.py which establish per-instance and per-class-attribute
instrumentation, respectively.

The class instrumentation system can be customized on a per-class
or global basis using the :mod:`sqlalchemy.ext.instrumentation`
module, which provides the means to build and specify
alternate instrumentation forms.

.. versionchanged: 0.8
   The instrumentation extension system was moved out of the
   ORM and into the external :mod:`sqlalchemy.ext.instrumentation`
   package.  When that package is imported, it installs
   itself within sqlalchemy.orm so that its more comprehensive
   resolution mechanics take effect.

"""
from __future__ import annotations
from typing import Any
from typing import Callable
from typing import cast
from typing import Collection
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import weakref
from  import base
from  import collections
from  import exc
from  import interfaces
from  import state
from _typing import _O
from attributes import _is_collection_attribute_impl
from  import util
from event import EventTarget
from util import HasMemoized
from util.typing import Literal
from util.typing import Protocol
if TYPE_CHECKING:
    from _typing import _RegistryType
    from attributes import AttributeImpl
    from attributes import QueryableAttribute
    from collections import _AdaptedCollectionProtocol
    from collections import _CollectionFactoryType
    from decl_base import _MapperConfig
    from events import InstanceEvents
    from mapper import Mapper
    from state import InstanceState
    from event import dispatcher
_T = TypeVar('_T', bound = Any)
DEL_ATTR = util.symbol('DEL_ATTR')

class _ExpiredAttributeLoaderProto(Protocol):
    
    def __call__(self = None, state = None, toload = None, passive = ('state', 'state.InstanceState[Any]', 'toload', 'Set[str]', 'passive', 'base.PassiveFlag', 'return', 'None')):
        pass



class _ManagerFactory(Protocol):
    
    def __call__(self = None, class_ = None):
        pass



def ClassManager():
    '''ClassManager'''
    dispatch: 'dispatcher[ClassManager[_O]]' = 'Tracks state information at the class level.'
    MANAGER_ATTR = base.DEFAULT_MANAGER_ATTR
    STATE_ATTR = base.DEFAULT_STATE_ATTR
    init_method: 'Optional[Callable[..., None]]' = staticmethod(util.attrsetter(STATE_ATTR))
    factory: 'Optional[_ManagerFactory]' = None
    registry: '_RegistryType' = None
    if not TYPE_CHECKING:
        registry = None
    class_: 'Type[_O]'
    _bases: 'List[ClassManager[Any]]'
    deferred_scalar_loader = (lambda self: self.expired_attribute_loader)()()
    deferred_scalar_loader = (lambda self, obj: self.expired_attribute_loader = obj)()()
    
    def __init__(self, class_):
        self.class_ = class_
        self.info = { }
        self.new_init = None
        self.local_attrs = { }
        self.originals = { }
        self._finalized = False
        self.factory = None
        self.init_method = None
        
        def <listcomp>(.0):
            pass
        # WARNING: Decompyle incomplete

        self._bases = 'List[Optional[ClassManager[Any]]]'(<listcomp>, self.class_.__bases__())()
    # WARNING: Decompyle incomplete

    
    def _update_state(self, finalize, mapper = util.deprecated('1.4', message = 'The ClassManager.deferred_scalar_loader attribute is now named expired_attribute_loader'), registry = deferred_scalar_loader.setter, declarative_scan = util.deprecated('1.4', message = 'The ClassManager.deferred_scalar_loader attribute is now named expired_attribute_loader'), expired_attribute_loader = (False, None, None, None, None, None), init_method = ('finalize', 'bool', 'mapper', 'Optional[Mapper[_O]]', 'registry', 'Optional[_RegistryType]', 'declarative_scan', 'Optional[_MapperConfig]', 'expired_attribute_loader', 'Optional[_ExpiredAttributeLoaderProto]', 'init_method', 'Optional[Callable[..., None]]', 'return', 'None')):
        if mapper:
            self.mapper = mapper
        if registry:
            registry._add_manager(self)
        if declarative_scan:
            self.declarative_scan = weakref.ref(declarative_scan)
        if expired_attribute_loader:
            self.expired_attribute_loader = expired_attribute_loader
    # WARNING: Decompyle incomplete

    
    def _finalize(self = None):
        if self._finalized:
            return None
        self._finalized = None
        self._instrument_init()
        _instrumentation_factory.dispatch.class_instrument(self.class_)

    
    def __hash__(self = None):
        return id(self)

    
    def __eq__(self = None, other = None):
        return other is self

    is_mapped = (lambda self = None: 'mapper' in self.__dict__)()
    _all_key_set = (lambda self: frozenset(self))()
    _collection_impl_keys = (lambda self: (lambda .0: pass# WARNING: Decompyle incomplete
)(self.values()())
)()
    _scalar_loader_impls = (lambda self: (lambda .0: pass# WARNING: Decompyle incomplete
)(self.values()())
)()
    _loader_impls = (lambda self: (lambda .0: [ attr.impl for attr in .0 ])(self.values()())
)()
    mapper = (lambda self = HasMemoized.memoized_attribute: raise exc.UnmappedClassError(self.class_))()
    
    def _all_sqla_attributes(self, exclude = (None,)):
        '''return an iterator of all classbound attributes that are
        implement :class:`.InspectionAttr`.

        This includes :class:`.QueryableAttribute` as well as extension
        types such as :class:`.hybrid_property` and
        :class:`.AssociationProxy`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_class_attr_mro(self, key, default = (None,)):
        '''return an attribute on the class without tripping it.'''
        for supercls in self.class_.__mro__:
            if key in supercls.__dict__:
                
                return None, supercls.__dict__[key]
            return default

    
    def _attr_has_impl(self = None, key = HasMemoized.memoized_attribute):
        '''Return True if the given attribute is fully initialized.

        i.e. has an impl.
        '''
        if key in self:
            pass
        return self[key].impl is not None

    
    def _subclass_manager(self = None, cls = None):
        """Create a new ClassManager for a subclass of this ClassManager's
        class.

        This is called automatically when attributes are instrumented so that
        the attributes can be propagated to subclasses against their own
        class-local manager, without the need for mappers etc. to have already
        pre-configured managers for the full class hierarchy.   Mappers
        can post-configure the auto-generated ClassManager when needed.

        """
        return register_class(cls, finalize = False)

    
    def _instrument_init(self):
        self.new_init = _generate_init(self.class_, self, self.original_init)
        self.install_member('__init__', self.new_init)

    _state_constructor = (lambda self = None: self.dispatch.first_init(self, self.class_)state.InstanceState)()
    
    def manage(self):
        '''Mark this instance as the manager for its class.'''
        setattr(self.class_, self.MANAGER_ATTR, self)

    manager_getter = (lambda self: _default_manager_getter)()
    state_getter = (lambda self: _default_state_getter)()
    dict_getter = (lambda self: _default_dict_getter)()
    
    def instrument_attribute(self = util.hybridmethod, key = util.hybridmethod, inst = util.hybridmethod, propagated = (False,)):
        if propagated:
            if key in self.local_attrs:
                return None
        self.local_attrs[key] = inst
        self.install_descriptor(key, inst)
        self._reset_memoizations()
        self[key] = inst
        for cls in self.class_.__subclasses__():
            manager = self._subclass_manager(cls)
            manager.instrument_attribute(key, inst, True)
            return None

    
    def subclass_managers(self, recursive):
        pass
    # WARNING: Decompyle incomplete

    
    def post_configure_attribute(self, key):
        _instrumentation_factory.dispatch.attribute_instrument(self.class_, key, self[key])

    
    def uninstrument_attribute(self, key, propagated = (False,)):
        if key not in self:
            return None
        if None:
            if key in self.local_attrs:
                return None
        del self.local_attrs[key]
        self.uninstall_descriptor(key)
        self._reset_memoizations()
        del self[key]
        for cls in self.class_.__subclasses__():
            manager = opt_manager_of_class(cls)
            if manager:
                manager.uninstrument_attribute(key, True)
            return None

    
    def unregister(self = None):
        '''remove all instrumentation established by this ClassManager.'''
        for key in list(self.originals):
            self.uninstall_member(key)
            self.mapper = None
            self.dispatch = None
            self.new_init = None
            self.info.clear()
            for key in list(self):
                if key in self.local_attrs:
                    self.uninstrument_attribute(key)
                if self.MANAGER_ATTR in self.class_.__dict__:
                    delattr(self.class_, self.MANAGER_ATTR)
                    return None
                return None

    
    def install_descriptor(self = None, key = None, inst = None):
        if key in (self.STATE_ATTR, self.MANAGER_ATTR):
            raise KeyError('%r: requested attribute name conflicts with instrumentation attribute of the same name.' % key)
        setattr(self.class_, key, inst)

    
    def uninstall_descriptor(self = None, key = None):
        delattr(self.class_, key)

    
    def install_member(self = None, key = None, implementation = None):
        if key in (self.STATE_ATTR, self.MANAGER_ATTR):
            raise KeyError('%r: requested attribute name conflicts with instrumentation attribute of the same name.' % key)
        self.originals.setdefault(key, self.class_.__dict__.get(key, DEL_ATTR))
        setattr(self.class_, key, implementation)

    
    def uninstall_member(self = None, key = None):
        original = self.originals.pop(key, None)
        if original is not DEL_ATTR:
            setattr(self.class_, key, original)
            return None
        None(self.class_, key)

    
    def instrument_collection_class(self = None, key = None, collection_class = None):
        return collections.prepare_instrumentation(collection_class)

    
    def initialize_collection(self = None, key = None, state = None, factory = ('key', 'str', 'state', 'InstanceState[_O]', 'factory', '_CollectionFactoryType', 'return', 'Tuple[collections.CollectionAdapter, _AdaptedCollectionProtocol]')):
        user_data = factory()
        impl = self.get_impl(key)
    # WARNING: Decompyle incomplete

    
    def is_instrumented(self = None, key = None, search = None):
        if search:
            return key in self
        return None in self.local_attrs

    
    def get_impl(self = None, key = None):
        return self[key].impl

    attributes = (lambda self = None: iter(self.values()))()
    
    def new_instance(self = None, state = None):
        instance = self.class_.__new__(self.class_)
    # WARNING: Decompyle incomplete

    
    def setup_instance(self = None, instance = None, state = None):
        pass
    # WARNING: Decompyle incomplete

    
    def teardown_instance(self = None, instance = None):
        delattr(instance, self.STATE_ATTR)

    
    def _serialize(self = None, state = None, state_dict = None):
        return _SerializeManager(state, state_dict)

    
    def _new_state_if_none(self = None, instance = None):
        '''Install a default InstanceState if none is present.

        A private convenience method used by the __init__ decorator.

        '''
        if hasattr(instance, self.STATE_ATTR):
            return False
        if None.class_ is not instance.__class__ and self.is_mapped:
            return self._subclass_manager(instance.__class__)._new_state_if_none(instance)
        state = None._state_constructor(instance, self)
        self._state_setter(instance, state)
        return state

    
    def has_state(self = None, instance = None):
        return hasattr(instance, self.STATE_ATTR)

    
    def has_parent(self = None, state = None, key = None, optimistic = (False,)):
        '''TODO'''
        return self.get_impl(key).hasparent(state, optimistic = optimistic)

    
    def __bool__(self = None):
        '''All ClassManagers are non-zero regardless of attribute state.'''
        return True

    
    def __repr__(self = None):
        return '<%s of %r at %x>' % (self.__class__.__name__, self.class_, id(self))


ClassManager = <NODE:27>(ClassManager, 'ClassManager', HasMemoized, Dict[(str, 'QueryableAttribute[Any]')], Generic[_O], EventTarget)

class _SerializeManager:
    '''Provide serialization of a :class:`.ClassManager`.

    The :class:`.InstanceState` uses ``__init__()`` on serialize
    and ``__call__()`` on deserialize.

    '''
    
    def __init__(self = None, state = None, d = None):
        self.class_ = state.class_
        manager = state.manager
        manager.dispatch.pickle(state, d)

    
    def __call__(self, state, inst, state_dict):
        state.manager = opt_manager_of_class(self.class_)
        manager = opt_manager_of_class(self.class_)
    # WARNING: Decompyle incomplete



class InstrumentationFactory(EventTarget):
    dispatch: 'dispatcher[InstrumentationFactory]' = 'Factory for new ClassManager instances.'
    
    def create_manager_for_cls(self = None, class_ = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _locate_extended_factory(self = None, class_ = None):
        '''Overridden by a subclass to do an extended lookup.'''
        return (None, None)

    
    def _check_conflicts(self = None, class_ = None, factory = None):
        '''Overridden by a subclass to test for conflicting factories.'''
        pass

    
    def unregister(self = None, class_ = None):
        manager = manager_of_class(class_)
        manager.unregister()
        self.dispatch.class_uninstrument(class_)


_instrumentation_factory = InstrumentationFactory()
instance_state = base.instance_state
_default_state_getter = base.instance_state
instance_dict = base.instance_dict
_default_dict_getter = base.instance_dict
manager_of_class = base.manager_of_class
_default_manager_getter = base.manager_of_class
opt_manager_of_class = base.opt_manager_of_class
_default_opt_manager_getter = base.opt_manager_of_class

def register_class(class_, finalize, mapper = None, registry = None, declarative_scan = None, expired_attribute_loader = (True, None, None, None, None, None), init_method = ('class_', 'Type[_O]', 'finalize', 'bool', 'mapper', 'Optional[Mapper[_O]]', 'registry', 'Optional[_RegistryType]', 'declarative_scan', 'Optional[_MapperConfig]', 'expired_attribute_loader', 'Optional[_ExpiredAttributeLoaderProto]', 'init_method', 'Optional[Callable[..., None]]', 'return', 'ClassManager[_O]')):
    '''Register class instrumentation.

    Returns the existing or newly created class manager.

    '''
    manager = opt_manager_of_class(class_)
# WARNING: Decompyle incomplete


def unregister_class(class_):
    '''Unregister class instrumentation.'''
    _instrumentation_factory.unregister(class_)


def is_instrumented(instance, key):
    '''Return True if the given attribute on the given instance is
    instrumented by the attributes package.

    This function may be used regardless of instrumentation
    applied directly to the class, i.e. no descriptors are required.

    '''
    return manager_of_class(instance.__class__).is_instrumented(key, search = True)


def _generate_init(class_, class_manager, original_init):
    '''Build an __init__ decorator that triggers ClassManager events.'''
    pass
# WARNING: Decompyle incomplete
