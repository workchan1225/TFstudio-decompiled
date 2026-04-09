# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: registry.pyc (Python 3.11)

'''Provides managed registration services on behalf of :func:`.listen`
arguments.

By "managed registration", we mean that event listening functions and
other objects can be added to various collections in such a way that their
membership in all those collections can be revoked at once, based on
an equivalent :class:`._EventKey`.

'''
from __future__ import annotations
import collections
import types
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Deque
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import Union
import weakref
from  import exc
from  import util
if typing.TYPE_CHECKING:
    from attr import RefCollection
    from base import dispatcher
_ListenerFnType = Callable[(..., Any)]
_ListenerFnKeyType = Union[(int, Tuple[(int, int)])]
_EventKeyTupleType = Tuple[(int, str, _ListenerFnKeyType)]
_ET = TypeVar('_ET', bound = 'EventTarget')

class EventTarget:
    '''represents an event target, that is, something we can listen on
    either with that target as a class or as an instance.

    Examples include:  Connection, Mapper, Table, Session,
    InstrumentedAttribute, Engine, Pool, Dialect.

    '''
    dispatch: 'dispatcher[Any]' = ()

_RefCollectionToListenerType = Dict[('weakref.ref[RefCollection[Any]]', 'weakref.ref[_ListenerFnType]')]
_key_to_collection: 'Dict[_EventKeyTupleType, _RefCollectionToListenerType]' = collections.defaultdict(dict)
_ListenerToEventKeyType = Dict[('weakref.ref[_ListenerFnType]', _EventKeyTupleType)]
_collection_to_key: 'Dict[weakref.ref[RefCollection[Any]], _ListenerToEventKeyType]' = collections.defaultdict(dict)

def _collection_gced(ref = None):
    if _collection_to_key or ref not in _collection_to_key:
        return None
    ref = None('weakref.ref[RefCollection[EventTarget]]', ref)
    listener_to_key = _collection_to_key.pop(ref)
    for key in listener_to_key.values():
        if key in _key_to_collection:
            dispatch_reg = _key_to_collection[key]
            dispatch_reg.pop(ref)
            if not dispatch_reg:
                _key_to_collection.pop(key)
        return None


def _stored_in_collection(event_key = None, owner = None):
    key = event_key._key
    dispatch_reg = _key_to_collection[key]
    owner_ref = owner.ref
    listen_ref = weakref.ref(event_key._listen_fn)
    if owner_ref in dispatch_reg:
        return False
    dispatch_reg[owner_ref] = None
    listener_to_key = _collection_to_key[owner_ref]
    listener_to_key[listen_ref] = key
    return True


def _removed_from_collection(event_key = None, owner = None):
    key = event_key._key
    dispatch_reg = _key_to_collection[key]
    listen_ref = weakref.ref(event_key._listen_fn)
    owner_ref = owner.ref
    dispatch_reg.pop(owner_ref, None)
    if not dispatch_reg:
        del _key_to_collection[key]
    if owner_ref in _collection_to_key:
        listener_to_key = _collection_to_key[owner_ref]
        listener_to_key.pop(listen_ref, None)
        return None


def _stored_in_collection_multi(newowner = None, oldowner = None, elements = None):
    if not elements:
        return None
    oldowner_ref = None.ref
    newowner_ref = newowner.ref
    old_listener_to_key = _collection_to_key[oldowner_ref]
    new_listener_to_key = _collection_to_key[newowner_ref]
    for listen_fn in elements:
        listen_ref = weakref.ref(listen_fn)
        key = old_listener_to_key[listen_ref]
    except KeyError:
        continue
    dispatch_reg = _key_to_collection[key]
# WARNING: Decompyle incomplete


def _clear(owner = None, elements = None):
    if not elements:
        return None
    owner_ref = None.ref
    listener_to_key = _collection_to_key[owner_ref]
    for listen_fn in elements:
        listen_ref = weakref.ref(listen_fn)
        key = listener_to_key[listen_ref]
        dispatch_reg = _key_to_collection[key]
        dispatch_reg.pop(owner_ref, None)
        if not dispatch_reg:
            del _key_to_collection[key]
        return None


def _EventKey():
    '''_EventKey'''
    __doc__ = 'Represent :func:`.listen` arguments.'
    _fn_wrap: 'Optional[_ListenerFnType]' = ('target', 'identifier', 'fn', 'fn_key', 'fn_wrap', 'dispatch_target')
    
    def __init__(self, target = None, identifier = None, fn = None, dispatch_target = (None,), _fn_wrap = ('target', '_ET', 'identifier', 'str', 'fn', '_ListenerFnType', 'dispatch_target', 'Any', '_fn_wrap', 'Optional[_ListenerFnType]')):
        self.target = target
        self.identifier = identifier
        self.fn = fn
        if isinstance(fn, types.MethodType):
            self.fn_key = (id(fn.__func__), id(fn.__self__))
        else:
            self.fn_key = id(fn)
        self.fn_wrap = _fn_wrap
        self.dispatch_target = dispatch_target

    _key = (lambda self = None: (id(self.target), self.identifier, self.fn_key))()
    
    def with_wrapper(self = None, fn_wrap = None):
        if fn_wrap is self._listen_fn:
            return self
        return None(self.target, self.identifier, self.fn, self.dispatch_target, _fn_wrap = fn_wrap)

    
    def with_dispatch_target(self = None, dispatch_target = None):
        if dispatch_target is self.dispatch_target:
            return self
        return None(self.target, self.identifier, self.fn, dispatch_target, _fn_wrap = self.fn_wrap)

    
    def listen(self = None, *args, **kw):
        once = kw.pop('once', False)
        once_unless_exception = kw.pop('_once_unless_exception', False)
        named = kw.pop('named', False)
        fn = self._listen_fn
        identifier = self.identifier
        target = self.dispatch_target
        dispatch_collection = getattr(target.dispatch, identifier)
        adjusted_fn = dispatch_collection._adjust_fn_spec(fn, named)
        self = self.with_wrapper(adjusted_fn)
        stub_function = getattr(self.dispatch_target.dispatch._events, self.identifier)
        if hasattr(stub_function, '_sa_warn'):
            stub_function._sa_warn()
    # WARNING: Decompyle incomplete

    
    def remove(self = None):
        key = self._key
        if key not in _key_to_collection:
            raise exc.InvalidRequestError(f'''No listeners found for event {self.target!s} / {self.identifier!r} / {self.fn!s} ''')
        dispatch_reg = _key_to_collection.pop(key)
    # WARNING: Decompyle incomplete

    
    def contains(self = None):
        '''Return True if this event key is registered to listen.'''
        return self._key in _key_to_collection

    
    def base_listen(self, propagate = None, insert = None, named = None, retval = (False, False, False, None, False), asyncio = ('propagate', 'bool', 'insert', 'bool', 'named', 'bool', 'retval', 'Optional[bool]', 'asyncio', 'bool', 'return', 'None')):
        identifier = self.identifier
        target = self.dispatch_target
        dispatch_collection = getattr(target.dispatch, identifier)
        for_modify = dispatch_collection.for_modify(target.dispatch)
        if asyncio:
            for_modify._set_asyncio()
        if insert:
            for_modify.insert(self, propagate)
            return None
        None.append(self, propagate)

    _listen_fn = (lambda self = None:
