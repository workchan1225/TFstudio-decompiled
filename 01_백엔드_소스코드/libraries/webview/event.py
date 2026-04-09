# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: event.pyc (Python 3.11)

from __future__ import annotations
import inspect
import logging
import threading
from typing import TYPE_CHECKING, Any, Callable
from typing_extensions import Self
if TYPE_CHECKING:
    from typing import type_check_only
logger = logging.getLogger('pywebview')

class EventContainer:
    _serializable = False
    if TYPE_CHECKING:
        __getattr__ = (lambda self = None, _EventContainer__name = None: pass)()
        __setattr__ = (lambda self = None, _EventContainer__name = None, _EventContainer__value = type_check_only: pass)()
        return None


class Event:
    
    def __init__(self = None, window = None, should_lock = None):
        self._items = []
        self._should_lock = should_lock
        self._event = threading.Event()
        self._window = window

    
    def set(self = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def is_set(self = None):
        return self._event.is_set()

    
    def wait(self = None, timeout = None):
        return self._event.wait(timeout)

    
    def clear(self = None):
        return self._event.clear()

    
    def __add__(self = None, item = None):
        self._items.append(item)
        return self

    
    def __sub__(self = None, item = None):
        self._items.remove(item)
        return self

    
    def __iadd__(self = None, item = None):
        self._items.append(item)
        return self

    
    def __isub__(self = None, item = None):
        self._items.remove(item)
        return self

    
    def __len__(self = None):
        return len(self._items)
