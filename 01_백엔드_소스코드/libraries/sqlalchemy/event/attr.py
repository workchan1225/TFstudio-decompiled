# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: attr.pyc (Python 3.11)

'''Attribute implementation for _Dispatch classes.

The various listener targets for a particular event class are represented
as attributes, which refer to collections of listeners to be fired off.
These collections can exist at the class level as well as at the instance
level.  An event is fired off using code like this::

    some_object.dispatch.first_connect(arg1, arg2)

Above, ``some_object.dispatch`` would be an instance of ``_Dispatch`` and
``first_connect`` is typically an instance of ``_ListenerCollection``
if event listeners are present, or ``_EmptyListener`` if none are present.

The attribute mechanics here spend effort trying to ensure listener functions
are available with a minimum of function call overhead, that unnecessary
objects aren\'t created (i.e. many empty per-instance listener collections),
as well as that everything is garbage collectable when owning references are
lost.  Other features such as "propagation" of listener functions across
many ``_Dispatch`` instances, "joining" of multiple ``_Dispatch`` instances,
as well as support for subclass propagation (e.g. events assigned to
``Pool`` vs. ``QueuePool``) are all implemented here.

'''
from __future__ import annotations
import collections
from itertools import chain
import threading
from types import TracebackType
import typing
from typing import Any
from typing import cast
from typing import Collection
from typing import Deque
from typing import FrozenSet
from typing import Generic
from typing import Iterator
from typing import MutableMapping
from typing import MutableSequence
from typing import NoReturn
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
import weakref
from  import legacy
from  import registry
from registry import _ET
from registry import _EventKey
from registry import _ListenerFnType
from  import exc
from  import util
from util.concurrency import AsyncAdaptedLock
from util.typing import Protocol
_T = TypeVar('_T', bound = Any)
if typing.TYPE_CHECKING:
    from base import _Dispatch
    from base import _DispatchCommon
    from base import _HasEventsDispatch

def RefCollection():
    '''RefCollection'''
    ref: 'weakref.ref[RefCollection[_ET]]' = ('ref',)
    
    def _memoized_attr_ref(self = None):
        return weakref.ref(self, registry._collection_gced)


RefCollection = <NODE:27>(RefCollection, 'RefCollection', util.MemoizedSlots, Generic[_ET])

def _empty_collection():
    '''_empty_collection'''
    
    def append(self = None, element = None):
        pass

    
    def appendleft(self = None, element = None):
        pass

    
    def extend(self = None, other = None):
        pass

    
    def remove(self = None, element = None):
        pass

    
    def __contains__(self = None, element = None):
        return False

    
    def __iter__(self = None):
        return iter([])

    
    def clear(self = None):
        pass

    
    def __len__(self = None):
        return 0


_empty_collection = <NODE:27>(_empty_collection, '_empty_collection', Collection[_T])
_ListenerFnSequenceType = Union[(Deque[_T], _empty_collection[_T])]

def _ClsLevelDispatch():
    '''_ClsLevelDispatch'''
    __doc__ = 'Class-level events on :class:`._Dispatch` classes.'
    _clslevel: 'MutableMapping[Type[_ET], _ListenerFnSequenceType[_ListenerFnType]]' = ('clsname', 'name', 'arg_names', 'has_kw', 'legacy_signatures', '_clslevel', '__weakref__')
    
    def __init__(self = None, parent_dispatch_cls = None, fn = None):
        self.name = fn.__name__
        self.clsname = parent_dispatch_cls.__name__
        argspec = util.inspect_getfullargspec(fn)
        self.arg_names = argspec.args[1:]
        self.has_kw = bool(argspec.varkw)
        self.legacy_signatures = list(reversed(sorted(getattr(fn, '_legacy_signatures', []), key = (lambda s: s[0]))))
        fn.__doc__ = legacy._augment_fn_docs(self, parent_dispatch_cls, fn)
        self._clslevel = weakref.WeakKeyDictionary()

    
    def _adjust_fn_spec(self = None, fn = None, named = None):
        if named:
            fn = self._wrap_fn_for_kw(fn)
        if self.legacy_signatures:
            
            try:
                argspec = util.get_callable_argspec(fn, no_self = True)
                fn = legacy._wrap_fn_for_legacy(self, fn, argspec)
            except TypeError:
                pass

            return fn

    
    def _wrap_fn_for_kw(self = None, fn = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _do_insert_or_append(self = None, event_key = None, is_append = None):
        target = event_key.dispatch_target
    # WARNING: Decompyle incomplete

    
    def insert(self = None, event_key = None, propagate = None):
        self._do_insert_or_append(event_key, is_append = False)

    
    def append(self = None, event_key = None, propagate = None):
        self._do_insert_or_append(event_key, is_append = True)

    
    def update_subclass(self = None, target = None):
        pass
    # WARNING: Decompyle incomplete

    
    def remove(self = None, event_key = None):
        target = event_key.dispatch_target
        for cls in util.walk_subclasses(target):
            if cls in self._clslevel:
                self._clslevel[cls].remove(event_key._listen_fn)
            registry._removed_from_collection(event_key, self)
            return None

    
    def clear(self = None):
        '''Clear all class level listeners'''
        to_clear = set()
        for dispatcher in self._clslevel.values():
            to_clear.update(dispatcher)
            dispatcher.clear()
            registry._clear(self, to_clear)
            return None

    
    def for_modify(self = None, obj = None):
        '''Return an event collection which can be modified.

        For _ClsLevelDispatch at the class level of
        a dispatcher, this returns self.

        '''
        return self


_ClsLevelDispatch = <NODE:27>(_ClsLevelDispatch, '_ClsLevelDispatch', RefCollection[_ET])

def _InstanceLevelDispatch():
    '''_InstanceLevelDispatch'''
    parent: '_ClsLevelDispatch[_ET]' = ()
    
    def _adjust_fn_spec(self = None, fn = None, named = None):
        return self.parent._adjust_fn_spec(fn, named)

    
    def __contains__(self = None, item = None):
        raise NotImplementedError()

    
    def __len__(self = None):
        raise NotImplementedError()

    
    def __iter__(self = None):
        raise NotImplementedError()

    
    def __bool__(self = None):
        raise NotImplementedError()

    
    def exec_once(self = None, *args, **kw):
        raise NotImplementedError()

    
    def exec_once_unless_exception(self = None, *args, **kw):
        raise NotImplementedError()

    
    def _exec_w_sync_on_first_run(self = None, *args, **kw):
        raise NotImplementedError()

    
    def __call__(self = None, *args, **kw):
        raise NotImplementedError()

    
    def insert(self = None, event_key = None, propagate = None):
        raise NotImplementedError()

    
    def append(self = None, event_key = None, propagate = None):
        raise NotImplementedError()

    
    def remove(self = None, event_key = None):
        raise NotImplementedError()

    
    def for_modify(self = None, obj = None):
        '''Return an event collection which can be modified.

        For _ClsLevelDispatch at the class level of
        a dispatcher, this returns self.

        '''
        return self


_InstanceLevelDispatch = <NODE:27>(_InstanceLevelDispatch, '_InstanceLevelDispatch', RefCollection[_ET], Collection[_ListenerFnType])

def _EmptyListener():
    '''_EmptyListener'''
    __doc__ = 'Serves as a proxy interface to the events\n    served by a _ClsLevelDispatch, when there are no\n    instance-level events present.\n\n    Is replaced by _ListenerCollection when instance-level\n    events are added.\n\n    '
    __slots__ = ('parent', 'parent_listeners', 'name')
    propagate: 'FrozenSet[_ListenerFnType]' = frozenset()
    name: 'str' = ()
    
    def __init__(self = None, parent = None, target_cls = None):
        if target_cls not in parent._clslevel:
            parent.update_subclass(target_cls)
        self.parent = parent
        self.parent_listeners = parent._clslevel[target_cls]
        self.name = parent.name

    
    def for_modify(self = None, obj = None):
        '''Return an event collection which can be modified.

        For _EmptyListener at the instance level of
        a dispatcher, this generates a new
        _ListenerCollection, applies it to the instance,
        and returns it.

        '''
        obj = cast('_Dispatch[_ET]', obj)
    # WARNING: Decompyle incomplete

    
    def _needs_modify(self = None, *args, **kw):
        raise NotImplementedError('need to call for_modify()')

    
    def exec_once(self = None, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def exec_once_unless_exception(self = None, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def insert(self = None, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def append(self = None, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def remove(self = None, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def clear(self = None, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self = None, *args, **kw):
        '''Execute this event.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self = None, item = None):
        return item in self.parent_listeners

    
    def __len__(self = None):
        return len(self.parent_listeners)

    
    def __iter__(self = None):
        return iter(self.parent_listeners)

    
    def __bool__(self = None):
        return bool(self.parent_listeners)


_EmptyListener = <NODE:27>(_EmptyListener, '_EmptyListener', _InstanceLevelDispatch[_ET])

class _MutexProtocol(Protocol):
    
    def __enter__(self = None):
        pass

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'Optional[Type[BaseException]]', 'exc_val', 'Optional[BaseException]', 'exc_tb', 'Optional[TracebackType]', 'return', 'Optional[bool]')):
        pass



def _CompoundListener():
    '''_CompoundListener'''
    pass
# WARNING: Decompyle incomplete

_CompoundListener = <NODE:27>(_CompoundListener, '_CompoundListener', _InstanceLevelDispatch[_ET])

def _ListenerCollection():
    '''_ListenerCollection'''
    pass
# WARNING: Decompyle incomplete

_ListenerCollection = <NODE:27>(_ListenerCollection, '_ListenerCollection', _CompoundListener[_ET])

def _JoinedListener():
    '''_JoinedListener'''
    parent_listeners: 'Collection[_ListenerFnType]' = ('parent_dispatch', 'name', 'local', 'parent_listeners')
    
    def __init__(self = None, parent_dispatch = None, name = None, local = ('parent_dispatch', '_DispatchCommon[_ET]', 'name', 'str', 'local', '_EmptyListener[_ET]')):
        self._exec_once = False
        self._exec_w_sync_once = False
        self._exec_once_mutex = None
        self.parent_dispatch = parent_dispatch
        self.name = name
        self.local = local
        self.parent_listeners = self.local

    if not typing.TYPE_CHECKING:
        listeners = (lambda self = None: getattr(self.parent_dispatch, self.name))()
    
    def _adjust_fn_spec(self = None, fn = None, named = None):
        return self.local._adjust_fn_spec(fn, named)

    
    def for_modify(self = None, obj = None):
        self.local = self.local.for_modify(obj)
        self.parent_listeners = self.local.for_modify(obj)
        return self

    
    def insert(self = None, event_key = None, propagate = None):
        self.local.insert(event_key, propagate)

    
    def append(self = None, event_key = None, propagate = None):
        self.local.append(event_key, propagate)

    
    def remove(self = None, event_key = None):
        self.local.remove(event_key)

    
    def clear(self = None):
        raise NotImplementedError()


_JoinedListener = <NODE:27>(_JoinedListener, '_JoinedListener', _CompoundListener[_ET])
