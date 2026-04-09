# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: event.pyc (Python 3.11)

import logging
from typing import Any, Callable
from typing_extensions import Self
from webview.dom.element import Element
logger = logging.getLogger(__file__)

class DOMEvent:
    
    def __init__(self = None, event = None, element = None):
        self.event = event
        self._DOMEvent__element = element
        self._items = []

    
    def __add__(self = None, item = None):
        self._items.append(item)
        self._DOMEvent__element.on(self.event, item)
        return self

    
    def __sub__(self = None, item = None):
        self._items.remove(item)
        self._DOMEvent__element.off(self.event, item)
        return self

    
    def __iadd__(self = None, item = None):
        self._items.append(item)
        self._DOMEvent__element.on(self.event, item)
        return self

    
    def __isub__(self = None, item = None):
        if item in self._items:
            self._items.remove(item)
            self._DOMEvent__element.off(self.event, item)
        else:
            logger.warning(f'''Event handler {item} not found''')
        return self
