# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from enum import Enum
from typing import Callable

class ManipulationMode(Enum):
    LastChild = 'LAST_CHILD'
    FirstChild = 'FIRST_CHILD'
    Before = 'BEFORE'
    After = 'AFTER'
    Replace = 'REPLACE'


class DOMEventHandler:
    
    def __init__(self, callback = None, prevent_default = None, stop_propagation = None, stop_immediate_propagation = (False, False, False, 0), debounce = ('callback', Callable, 'prevent_default', bool, 'stop_propagation', bool, 'stop_immediate_propagation', bool, 'debounce', int)):
        self._DOMEventHandler__callback = callback
        self._DOMEventHandler__prevent_default = prevent_default
        self._DOMEventHandler__stop_propagation = stop_propagation
        self._DOMEventHandler__stop_immediate_propagation = stop_immediate_propagation
        self._DOMEventHandler__debounce = debounce

    callback = (lambda self: self._DOMEventHandler__callback)()
    prevent_default = (lambda self: self._DOMEventHandler__prevent_default)()
    stop_propagation = (lambda self: self._DOMEventHandler__stop_propagation)()
    stop_immediate_propagation = (lambda self: self._DOMEventHandler__stop_immediate_propagation)()
    debounce = (lambda self: self._DOMEventHandler__debounce)()

_dnd_state = {
    'num_listeners': 0,
    'paths': [] }
