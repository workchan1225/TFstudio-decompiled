# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as c
import sys
import typing as t
import weakref
from collections import defaultdict
from contextlib import contextmanager
from functools import cached_property
from inspect import iscoroutinefunction
from _utilities import make_id
from _utilities import make_ref
from _utilities import Symbol
F = t.TypeVar('F', bound = c.Callable[(..., t.Any)])
ANY = Symbol('ANY')
ANY_ID = 0

class Signal:
    '''A notification emitter.

    :param doc: The docstring for the signal.
    '''
    ANY = ANY
    set_class: 'type[set[t.Any]]' = set
    receiver_connected = (lambda self = None: Signal(doc = 'Emitted after a receiver connects.'))()
    receiver_disconnected = (lambda self = None: Signal(doc = 'Emitted after a receiver disconnects.'))()
    
    def __init__(self = None, doc = None):
        if doc:
            self.__doc__ = doc
        self.receivers = { }
        self.is_muted = False
        self._by_receiver = defaultdict(self.set_class)
        self._by_sender = defaultdict(self.set_class)
        self._weak_senders = { }

    
    def connect(self = None, receiver = None, sender = None, weak = (ANY, True)):
        '''Connect ``receiver`` to be called when the signal is sent by
        ``sender``.

        :param receiver: The callable to call when :meth:`send` is called with
            the given ``sender``, passing ``sender`` as a positional argument
            along with any extra keyword arguments.
        :param sender: Any object or :data:`ANY`. ``receiver`` will only be
            called when :meth:`send` is called with this sender. If ``ANY``, the
            receiver will be called for any sender. A receiver may be connected
            to multiple senders by calling :meth:`connect` multiple times.
        :param weak: Track the receiver with a :mod:`weakref`. The receiver will
            be automatically disconnected when it is garbage collected. When
            connecting a receiver defined within a function, set to ``False``,
            otherwise it will be disconnected when the function scope ends.
        '''
        receiver_id = make_id(receiver)
        sender_id = ANY_ID if sender is ANY else make_id(sender)
        if weak:
            self.receivers[receiver_id] = make_ref(receiver, self._make_cleanup_receiver(receiver_id))
        else:
            self.receivers[receiver_id] = receiver
        self._by_sender[sender_id].add(receiver_id)
        self._by_receiver[receiver_id].add(sender_id)
        if sender is not ANY and sender_id not in self._weak_senders:
            
            try:
                self._weak_senders[sender_id] = make_ref(sender, self._make_cleanup_sender(sender_id))
            except TypeError:
                pass

            if 'receiver_connected' in self.__dict__ and self.receiver_connected.receivers:
                
                try:
                    self.receiver_connected.send(self, receiver = receiver, sender = sender, weak = weak)
                except TypeError:
                    self.disconnect(receiver, sender)
                    raise 

                return receiver

    
    def connect_via(self = None, sender = None, weak = None):
        '''Connect the decorated function to be called when the signal is sent
        by ``sender``.

        The decorated function will be called when :meth:`send` is called with
        the given ``sender``, passing ``sender`` as a positional argument along
        with any extra keyword arguments.

        :param sender: Any object or :data:`ANY`. ``receiver`` will only be
            called when :meth:`send` is called with this sender. If ``ANY``, the
            receiver will be called for any sender. A receiver may be connected
            to multiple senders by calling :meth:`connect` multiple times.
        :param weak: Track the receiver with a :mod:`weakref`. The receiver will
            be automatically disconnected when it is garbage collected. When
            connecting a receiver defined within a function, set to ``False``,
            otherwise it will be disconnected when the function scope ends.=

        .. versionadded:: 1.1
        '''
        pass
    # WARNING: Decompyle incomplete

    connected_to = (lambda self = None, receiver = None, sender = contextmanager: pass# WARNING: Decompyle incomplete
)()
    muted = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def send(self = None, sender = None, *, _async_wrapper, **kwargs):
        '''Call all receivers that are connected to the given ``sender``
        or :data:`ANY`. Each receiver is called with ``sender`` as a positional
        argument along with any extra keyword arguments. Return a list of
        ``(receiver, return value)`` tuples.

        The order receivers are called is undefined, but can be influenced by
        setting :attr:`set_class`.

        If a receiver raises an exception, that exception will propagate up.
        This makes debugging straightforward, with an assumption that correctly
        implemented receivers will not raise.

        :param sender: Call receivers connected to this sender, in addition to
            those connected to :data:`ANY`.
        :param _async_wrapper: Will be called on any receivers that are async
            coroutines to turn them into sync callables. For example, could run
            the receiver with an event loop.
        :param kwargs: Extra keyword arguments to pass to each receiver.

        .. versionchanged:: 1.7
            Added the ``_async_wrapper`` argument.
        '''
        if self.is_muted:
            return []
        results = None
    # WARNING: Decompyle incomplete

    
    async def send_async(self = None, sender = None, *, _sync_wrapper, **kwargs):
        '''Await all receivers that are connected to the given ``sender``
        or :data:`ANY`. Each receiver is called with ``sender`` as a positional
        argument along with any extra keyword arguments. Return a list of
        ``(receiver, return value)`` tuples.

        The order receivers are called is undefined, but can be influenced by
        setting :attr:`set_class`.

        If a receiver raises an exception, that exception will propagate up.
        This makes debugging straightforward, with an assumption that correctly
        implemented receivers will not raise.

        :param sender: Call receivers connected to this sender, in addition to
            those connected to :data:`ANY`.
        :param _sync_wrapper: Will be called on any receivers that are sync
            callables to turn them into async coroutines. For example,
            could call the receiver in a thread.
        :param kwargs: Extra keyword arguments to pass to each receiver.

        .. versionadded:: 1.7
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def has_receivers_for(self = None, sender = None):
        '''Check if there is at least one receiver that will be called with the
        given ``sender``. A receiver connected to :data:`ANY` will always be
        called, regardless of sender. Does not check if weakly referenced
        receivers are still live. See :meth:`receivers_for` for a stronger
        search.

        :param sender: Check for receivers connected to this sender, in addition
            to those connected to :data:`ANY`.
        '''
        if not self.receivers:
            return False
        if None._by_sender[ANY_ID]:
            return True
        if None is ANY:
            return False
        return None(sender) in self._by_sender

    
    def receivers_for(self = None, sender = None):
        '''Yield each receiver to be called for ``sender``, in addition to those
        to be called for :data:`ANY`. Weakly referenced receivers that are not
        live will be disconnected and skipped.

        :param sender: Yield receivers connected to this sender, in addition
            to those connected to :data:`ANY`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def disconnect(self = None, receiver = None, sender = None):
        '''Disconnect ``receiver`` from being called when the signal is sent by
        ``sender``.

        :param receiver: A connected receiver callable.
        :param sender: Disconnect from only this sender. By default, disconnect
            from all senders.
        '''
        if sender is ANY:
            sender_id = ANY_ID
        else:
            sender_id = make_id(sender)
        receiver_id = make_id(receiver)
        self._disconnect(receiver_id, sender_id)
        if 'receiver_disconnected' in self.__dict__ or self.receiver_disconnected.receivers:
            self.receiver_disconnected.send(self, receiver = receiver, sender = sender)
            return None
        return None

    
    def _disconnect(self = None, receiver_id = None, sender_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _make_cleanup_receiver(self = None, receiver_id = None):
        '''Create a callback function to disconnect a weakly referenced
        receiver when it is garbage collected.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _make_cleanup_sender(self = None, sender_id = None):
        '''Create a callback function to disconnect all receivers for a weakly
        referenced sender when it is garbage collected.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _cleanup_bookkeeping(self = None):
        '''Prune unused sender/receiver bookkeeping. Not threadsafe.

        Connecting & disconnecting leaves behind a small amount of bookkeeping
        data. Typical workloads using Blinker, for example in most web apps,
        Flask, CLI scripts, etc., are not adversely affected by this
        bookkeeping.

        With a long-running process performing dynamic signal routing with high
        volume, e.g. connecting to function closures, senders are all unique
        object instances. Doing all of this over and over may cause memory usage
        to grow due to extraneous bookkeeping. (An empty ``set`` for each stale
        sender/receiver pair.)

        This method will prune that bookkeeping away, with the caveat that such
        pruning is not threadsafe. The risk is that cleanup of a fully
        disconnected receiver/sender pair occurs while another thread is
        connecting that same pair. If you are in the highly dynamic, unique
        receiver/sender situation that has lead you to this method, that failure
        mode is perhaps not a big deal for you.
        '''
        for mapping in (self._by_sender, self._by_receiver):
            for ident, bucket in list(mapping.items()):
                if not bucket:
                    mapping.pop(ident, None)
                return None

    
    def _clear_state(self = None):
        '''Disconnect all receivers and senders. Useful for tests.'''
        self._weak_senders.clear()
        self.receivers.clear()
        self._by_sender.clear()
        self._by_receiver.clear()



class NamedSignal(Signal):
    pass
# WARNING: Decompyle incomplete


def Namespace():
    '''Namespace'''
    __doc__ = 'A dict mapping names to signals.'
    
    def signal(self = None, name = None, doc = None):
        '''Return the :class:`NamedSignal` for the given ``name``, creating it
        if required. Repeated calls with the same name return the same signal.

        :param name: The name of the signal.
        :param doc: The docstring of the signal.
        '''
        if name not in self:
            self[name] = NamedSignal(name, doc)
        return self[name]


Namespace = <NODE:27>(Namespace, 'Namespace', dict[(str, NamedSignal)])

class _PNamespaceSignal(t.Protocol):
    
    def __call__(self = None, name = None, doc = None):
        pass


default_namespace: 'Namespace' = Namespace()
signal: '_PNamespaceSignal' = default_namespace.signal
