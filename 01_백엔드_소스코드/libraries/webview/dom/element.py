# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: element.pyc (Python 3.11)

import logging
from collections import defaultdict
from functools import wraps
from typing import Any, Callable, Dict, Iterable, List, Optional, Union
from webview.dom import DOMEventHandler, ManipulationMode, _dnd_state
from webview.dom.classlist import ClassList
from webview.dom.propsdict import DOMPropType, PropsDict
from webview.errors import JavascriptException
from webview.event import EventContainer
logger = logging.getLogger('pywebview')

def _ignore_window_document(func):
    pass
# WARNING: Decompyle incomplete


def _exists(func):
    pass
# WARNING: Decompyle incomplete


class Element:
    
    def __init__(self = None, window = None, node_id = None):
        self._window = window
        self.events = EventContainer()
        self._node_id = node_id
        self._query_command = f'''\n            var element;\n\n            if (\'{self._node_id}\' === \'document\') {{\n                element = document;\n            }} else if (\'{self._node_id}\' === \'window\') {{\n                element = window;\n            }} else if (\'{self._node_id}\' === \'body\') {{\n                element = document.body;\n            }} else {{\n                element = document.querySelector(\'[data-pywebview-id="{self._node_id}"]\');\n            }}\n\n            if (!element) {{\n                throw new Error(\'Element with pywebview-id {self._node_id} not found\', {{ cause: \'ELEMENT_NOT_FOUND\' }});\n            }}\n        '''.replace('\n', '')
        self._event_handlers = defaultdict(list)
        self._event_handler_ids = { }
        self._exists = True
        self._classes = ClassList(self)
        self._style = PropsDict(self, DOMPropType.Style)
        self._attributes = PropsDict(self, DOMPropType.Attribute)
        self._Element__original_display = None
        self.__generate_events()

    tag = (lambda self = property: self._window.evaluate_js(f'''{self._query_command}; element.tagName''').lower())()()()
    id = (lambda self = property: self._window.evaluate_js(f'''{self._query_command}; element.id'''))()()()
    id = (lambda self = id.setter, id = _exists: self._window.run_js(f'''{self._query_command}; element.id = \'{id}\''''))()()()
    classes = (lambda self = property: self._classes)()()()
    classes = (lambda self = None, classes = None: self._classes = ClassList(self, classes))()
    attributes = (lambda self = property: self._attributes)()()()
    attributes = (lambda self = attributes.setter, attributes = _exists: self._attributes = PropsDict(self, DOMPropType.Attribute, attributes))()()()
    node = (lambda self = None: self._window.evaluate_js(f'''{self._query_command}; var r2 = pywebview._processElements([element])[0]; r2'''))()()
    style = (lambda self = property: self._style)()()()
    style = (lambda self = style.setter, style = _exists: self._style = PropsDict(self, DOMPropType.Style, style))()()()
    tabindex = (lambda self = property: self._window.evaluate_js(f'''{self._query_command}; element.tabIndex'''))()()()
    tabindex = (lambda self = tabindex.setter, tab_index = _exists: self._window.run_js(f'''{self._query_command}; element.tabIndex = {tab_index}'''))()()()
    text = (lambda self = property: self._window.evaluate_js(f'''{self._query_command}; element.textContent'''))()()()
    text = (lambda self = text.setter, text = _exists: self._window.run_js(f'''{self._query_command}; element.textContent = \'{text}\''''))()()()
    value = (lambda self = property: self._window.evaluate_js(f'''{self._query_command}; element.value'''))()()()
    visible = (lambda self = property: self._window.evaluate_js(f'''{self._query_command}; element.offsetParent !== null'''))()()()
    focused = (lambda self = property: self._window.evaluate_js(f'''{self._query_command}; document.activeElement === element'''))()()()
    value = (lambda self = value.setter, value = _exists: self._window.run_js(f'''{self._query_command}; if (\'value\' in element) {{ element.value = \'{value}\' }}'''))()()()
    blur = (lambda self = None: self._window.run_js(f'''{self._query_command}; element.blur()'''))()()
    focus = (lambda self = None: self._window.run_js(f'''{self._query_command}; element.focus()'''))()()
    children = (lambda self = property: pass# WARNING: Decompyle incomplete
)()()()
    parent = (lambda self = property: node_id = self._window.evaluate_js(f'''\n            {self._query_command};\n            var parent = element.parentElement;\n            parent ? pywebview._getNodeId(parent) : null\n        ''')Element(self._window, node_id) if node_id else None)()()()
    next = (lambda self = property: node_id = self._window.evaluate_js(f'''\n            {self._query_command};\n            var nextSibling = element.nextElementSibling;\n            nextSibling ? pywebview._getNodeId(nextSibling) : null\n        ''')Element(self._window, node_id) if node_id else None)()()()
    previous = (lambda self = property: node_id = self._window.evaluate_js(f'''\n            {self._query_command};\n            var previousSibling = element.previousElementSibling;\n            previousSibling ? pywebview._getNodeId(previousSibling) : null\n        ''')Element(self._window, node_id) if node_id else None)()()()
    hide = (lambda self = None: self._Element__original_display = self._window.evaluate_js(f'''{self._query_command}; element.style.display''')self._window.run_js(f'''{self._query_command}; element.style.display = \'none\''''))()()
    show = (lambda self = None:
