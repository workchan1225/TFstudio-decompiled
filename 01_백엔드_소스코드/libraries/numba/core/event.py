# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: event.pyc (Python 3.11)

'''
The ``numba.core.event`` module provides a simple event system for applications
to register callbacks to listen to specific compiler events.

The following events are built in:

- ``"numba:compile"`` is broadcast when a dispatcher is compiling. Events of
  this kind have ``data`` defined to be a ``dict`` with the following
  key-values:

  - ``"dispatcher"``: the dispatcher object that is compiling.
  - ``"args"``: the argument types.
  - ``"return_type"``: the return type.

- ``"numba:compiler_lock"`` is broadcast when the internal compiler-lock is
  acquired. This is mostly used internally to measure time spent with the lock
  acquired.

- ``"numba:llvm_lock"`` is broadcast when the internal LLVM-lock is acquired.
  This is used internally to measure time spent with the lock acquired.

- ``"numba:run_pass"`` is broadcast when a compiler pass is running.

    - ``"name"``: pass name.
    - ``"qualname"``: qualified name of the function being compiled.
    - ``"module"``: module name of the function being compiled.
    - ``"flags"``: compilation flags.
    - ``"args"``: argument types.
    - ``"return_type"`` return type.

Applications can register callbacks that are listening for specific events using
``register(kind: str, listener: Listener)``, where ``listener`` is an instance
of ``Listener`` that defines custom actions on occurrence of the specific event.
'''
import os
import json
import atexit
import abc
import enum
import time
import threading
from timeit import default_timer as timer
from contextlib import contextmanager, ExitStack
from collections import defaultdict
from numba.core import config, utils

class EventStatus(enum.Enum):
    '''Status of an event.
    '''
    START = enum.auto()
    END = enum.auto()

_builtin_kinds = frozenset([
    'numba:compiler_lock',
    'numba:compile',
    'numba:llvm_lock',
    'numba:run_pass'])

def _guard_kind(kind):
    '''Guard to ensure that an event kind is valid.

    All event kinds with a "numba:" prefix must be defined in the pre-defined
    ``numba.core.event._builtin_kinds``.
    Custom event kinds are allowed by not using the above prefix.

    Parameters
    ----------
    kind : str

    Return
    ------
    res : str
    '''
    if kind.startswith('numba:') and kind not in _builtin_kinds:
        msg = f'''{kind} is not a valid event kind, it starts with the reserved prefix \'numba:\''''
        raise ValueError(msg)
    return kind


class Event:
    '''An event.

    Parameters
    ----------
    kind : str
    status : EventStatus
    data : any; optional
        Additional data for the event.
    exc_details : 3-tuple; optional
        Same 3-tuple for ``__exit__``.
    '''
    
    def __init__(self, kind, status, data, exc_details = (None, None)):
        self._kind = _guard_kind(kind)
        self._status = status
        self._data = data
    # WARNING: Decompyle incomplete

    kind = (lambda self: self._kind)()
    status = (lambda self: self._status)()
    data = (lambda self: self._data)()
    is_start = (lambda self: self._status == EventStatus.START)()
    is_end = (lambda self: self._status == EventStatus.END)()
    is_failed = (lambda self: self._exc_details is None)()
    
    def __str__(self):
        pass
    # WARNING: Decompyle incomplete

    __repr__ = __str__

_registered = defaultdict(list)

def register(kind, listener):
    '''Register a listener for a given event kind.

    Parameters
    ----------
    kind : str
    listener : Listener
    '''
    pass
# WARNING: Decompyle incomplete


def unregister(kind, listener):
    '''Unregister a listener for a given event kind.

    Parameters
    ----------
    kind : str
    listener : Listener
    '''
    pass
# WARNING: Decompyle incomplete


def broadcast(event):
    '''Broadcast an event to all registered listeners.

    Parameters
    ----------
    event : Event
    '''
    for listener in _registered[event.kind]:
        listener.notify(event)
        return None


class Listener(abc.ABC):
    '''Base class for all event listeners.
    '''
    on_start = (lambda self, event: pass)()
    on_end = (lambda self, event: pass)()
    
    def notify(self, event):
        '''Notify this Listener with the given Event.

        Parameters
        ----------
        event : Event
        '''
        if event.is_start:
            self.on_start(event)
            return None
        if None.is_end:
            self.on_end(event)
            return None
        raise None('unreachable')



class TimingListener(Listener):
    '''A listener that measures the total time spent between *START* and
    *END* events during the time this listener is active.
    '''
    
    def __init__(self):
        self._depth = 0

    
    def on_start(self, event):
        if self._depth == 0:
            self._ts = timer()

    
    def on_end(self, event):
        if self._depth == 0:
            getattr(self, '_duration', 0) = self, self._depth -= 1, ._depth
            self._duration = (timer() - self._ts) + last
            return None
        return self, self._depth -= 1, ._depth

    done = (lambda self: hasattr(self, '_duration'))()
    duration = (lambda self: self._duration)()


class RecordingListener(Listener):
    '''A listener that records all events and stores them in the ``.buffer``
    attribute as a list of 2-tuple ``(float, Event)``, where the first element
    is the time the event occurred as returned by ``time.time()`` and the second
    element is the event.
    '''
    
    def __init__(self):
        self.buffer = []

    
    def on_start(self, event):
        self.buffer.append((time.time(), event))

    
    def on_end(self, event):
        self.buffer.append((time.time(), event))


install_listener = (lambda kind, listener: pass# WARNING: Decompyle incomplete
)()
install_timer = (lambda kind, callback: pass# WARNING: Decompyle incomplete
)()
install_recorder = (lambda kind: pass# WARNING: Decompyle incomplete
)()

def start_event(kind, data = (None,)):
    '''Trigger the start of an event of *kind* with *data*.

    Parameters
    ----------
    kind : str
        Event kind.
    data : any; optional
        Extra event data.
    '''
    evt = Event(kind = kind, status = EventStatus.START, data = data)
    broadcast(evt)


def end_event(kind, data, exc_details = (None, None)):
    '''Trigger the end of an event of *kind*, *exc_details*.

    Parameters
    ----------
    kind : str
        Event kind.
    data : any; optional
        Extra event data.
    exc_details : 3-tuple; optional
        Same 3-tuple for ``__exit__``. Or, ``None`` if no error.
    '''
    evt = Event(kind = kind, status = EventStatus.END, data = data, exc_details = exc_details)
    broadcast(evt)

trigger_event = (lambda kind, data = (None,): pass# WARNING: Decompyle incomplete
)()

def _prepare_chrome_trace_data(listener = contextmanager):
    '''Prepare events in `listener` for serializing as chrome trace data.
    '''
    pid = os.getpid()
    tid = threading.get_native_id()
    evs = []
    for ts, rec in listener.buffer:
        data = rec.data
        cat = str(rec.kind)
        ts_scaled = ts * 1000000
        ph = 'B' if rec.is_start else 'E'
        name = data['name']
        args = data
        ev = dict(cat = cat, pid = pid, tid = tid, ts = ts_scaled, ph = ph, name = name, args = args)
        evs.append(ev)
        return evs


def _setup_chrome_trace_exit_handler():
    '''Setup a RecordingListener and an exit handler to write the captured
    events to file.
    '''
    pass
# WARNING: Decompyle incomplete

if config.CHROME_TRACE:
    _setup_chrome_trace_exit_handler()
    return None
return contextmanager
